#!/usr/bin/env python3
import json
import os
import sys
import time
import unicodedata
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

OPTIONS_PATH = "/data/options.json"
PRIM_URL = "https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring"
MONITORING_REF = "STIF:StopArea:SP:69625:"
LINE_REF = "STIF:Line::C01727:"
HA_API = "http://supervisor/core/api"
PARIS_TZ = ZoneInfo("Europe/Paris")

SUMMARY_ENTITY = "sensor.rer_c_villeneuve_le_roi_paris"
NEXT_ENTITY = "sensor.rer_c_villeneuve_le_roi_prochain_train"
STATUS_ENTITY = "sensor.prim_mobilites_villeneuve_le_roi_status"


def log(message):
    print(f"[PRIM] {message}", flush=True)


def load_options():
    with open(OPTIONS_PATH, "r", encoding="utf-8") as fh:
        options = json.load(fh)
    api_key = str(options.get("api_key") or "").strip()
    if not api_key:
        raise RuntimeError("La clé API PRIM (api_key) est obligatoire.")
    refresh_seconds = max(60, min(300, int(options.get("refresh_seconds", 60))))
    max_trains = max(1, min(10, int(options.get("max_trains", 5))))
    keywords = options.get("destination_keywords") or []
    keywords = [normalise_text(str(k)) for k in keywords if str(k).strip()]
    return api_key, refresh_seconds, max_trains, keywords


def normalise_text(value):
    value = value or ""
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_value = "".join(c for c in decomposed if not unicodedata.combining(c))
    return " ".join(ascii_value.upper().split())


def scalar(value, default=None):
    if value is None:
        return default
    if isinstance(value, dict):
        if "value" in value:
            return scalar(value.get("value"), default)
        return default
    if isinstance(value, list):
        for item in value:
            result = scalar(item, None)
            if result not in (None, ""):
                return result
        return default
    return value


def parse_dt(value):
    if not value:
        return None
    try:
        text = str(value).strip()
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        dt = datetime.fromisoformat(text)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def request_json(url, headers=None, timeout=20):
    request = Request(url, headers=headers or {}, method="GET")
    with urlopen(request, timeout=timeout) as response:
        payload = response.read().decode("utf-8")
        return json.loads(payload)


def fetch_prim(api_key):
    query = urlencode({"MonitoringRef": MONITORING_REF, "LineRef": LINE_REF})
    headers = {"Accept": "application/json", "apikey": api_key, "User-Agent": "HomeAssistant-PRIM/0.1.0"}
    return request_json(f"{PRIM_URL}?{query}", headers=headers)


def extract_visits(payload):
    siri = payload.get("Siri", payload)
    service_delivery = siri.get("ServiceDelivery", {})
    deliveries = service_delivery.get("StopMonitoringDelivery", []) or []
    if isinstance(deliveries, dict):
        deliveries = [deliveries]
    visits = []
    for delivery in deliveries:
        current = delivery.get("MonitoredStopVisit", []) or []
        if isinstance(current, dict):
            current = [current]
        visits.extend(current)
    return visits


def is_paris_bound(destination, direction, keywords):
    candidate = normalise_text(f"{destination} {direction}")
    return any(keyword in candidate for keyword in keywords)


def platform_from_call(call):
    for key in ("DeparturePlatformName", "ArrivalPlatformName", "PlatformName"):
        value = scalar(call.get(key))
        if value:
            return str(value)
    return None


def parse_trains(payload, max_trains, keywords):
    now_utc = datetime.now(timezone.utc)
    trains = []
    for visit in extract_visits(payload):
        journey = visit.get("MonitoredVehicleJourney", {}) or {}
        line = str(scalar(journey.get("LineRef"), ""))
        if line and line != LINE_REF:
            continue
        call = journey.get("MonitoredCall", {}) or {}
        destination = str(scalar(call.get("DestinationDisplay"), "") or scalar(journey.get("DestinationName"), "") or "")
        direction = str(scalar(journey.get("DirectionName"), "") or "")
        if not is_paris_bound(destination, direction, keywords):
            continue
        expected = parse_dt(call.get("ExpectedDepartureTime") or call.get("ExpectedArrivalTime"))
        aimed = parse_dt(call.get("AimedDepartureTime") or call.get("AimedArrivalTime"))
        departure = expected or aimed
        if not departure or departure < now_utc.replace(second=0, microsecond=0):
            continue
        status = str(call.get("DepartureStatus") or call.get("ArrivalStatus") or "onTime")
        delay_min = None
        if expected and aimed:
            delay_min = max(0, round((expected - aimed).total_seconds() / 60))
        local_dt = departure.astimezone(PARIS_TZ)
        aimed_local = aimed.astimezone(PARIS_TZ) if aimed else None
        minutes = max(0, int((departure - now_utc).total_seconds() // 60))
        trains.append({
            "expected": departure.isoformat().replace("+00:00", "Z"),
            "time": local_dt.strftime("%H:%M"),
            "scheduled": aimed.isoformat().replace("+00:00", "Z") if aimed else None,
            "scheduled_time": aimed_local.strftime("%H:%M") if aimed_local else None,
            "destination": destination or direction or "Paris",
            "direction": direction or None,
            "status": status,
            "delay_minutes": delay_min,
            "minutes": minutes,
            "platform": platform_from_call(call),
            "vehicle_at_stop": bool(call.get("VehicleAtStop", False)),
        })
    trains.sort(key=lambda t: t["expected"])
    return trains[:max_trains]


def ha_post_state(entity_id, state, attributes):
    token = os.environ.get("SUPERVISOR_TOKEN", "")
    if not token:
        raise RuntimeError("SUPERVISOR_TOKEN absent; homeassistant_api doit être activé.")
    body = json.dumps({"state": state, "attributes": attributes}, ensure_ascii=False).encode("utf-8")
    req = Request(f"{HA_API}/states/{entity_id}", data=body, method="POST", headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    with urlopen(req, timeout=10) as response:
        response.read()


def publish_trains(trains):
    now = datetime.now(PARIS_TZ).isoformat()
    ha_post_state(SUMMARY_ENTITY, len(trains), {"friendly_name": "RER C Villeneuve-le-Roi → Paris", "icon": "mdi:train", "station": "Villeneuve-le-Roi", "direction": "Paris", "line": "RER C", "monitoring_ref": MONITORING_REF, "line_ref": LINE_REF, "updated_at": now, "trains": trains})
    if trains:
        first = trains[0]
        ha_post_state(NEXT_ENTITY, first["expected"], {"friendly_name": "Prochain RER C Villeneuve-le-Roi → Paris", "icon": "mdi:train-clock", "device_class": "timestamp", "destination": first["destination"], "direction": first["direction"], "status": first["status"], "delay_minutes": first["delay_minutes"], "minutes": first["minutes"], "platform": first["platform"], "scheduled": first["scheduled"], "updated_at": now})
    else:
        ha_post_state(NEXT_ENTITY, "unavailable", {"friendly_name": "Prochain RER C Villeneuve-le-Roi → Paris", "icon": "mdi:train-clock", "updated_at": now})


def publish_status(state, message=None):
    attrs = {"friendly_name": "PRIM Mobilités Villeneuve-le-Roi", "icon": "mdi:transit-connection-variant", "updated_at": datetime.now(PARIS_TZ).isoformat()}
    if message:
        attrs["message"] = str(message)[:500]
    ha_post_state(STATUS_ENTITY, state, attrs)


def main():
    api_key, refresh_seconds, max_trains, keywords = load_options()
    if not keywords:
        raise RuntimeError("destination_keywords ne peut pas être vide.")
    log(f"Démarrage : Villeneuve-le-Roi ({MONITORING_REF}), RER C, actualisation {refresh_seconds}s")
    while True:
        started = time.monotonic()
        try:
            payload = fetch_prim(api_key)
            trains = parse_trains(payload, max_trains, keywords)
            publish_trains(trains)
            publish_status("ok", f"{len(trains)} train(s) vers Paris")
            log(f"Mise à jour OK : {len(trains)} train(s) vers Paris")
        except HTTPError as exc:
            message = f"PRIM/HTTP {exc.code}: {exc.reason}"
            log(message)
            try:
                publish_status("error", message)
            except Exception as publish_exc:
                log(f"Impossible de publier le statut d'erreur: {publish_exc}")
        except (URLError, TimeoutError, json.JSONDecodeError, RuntimeError, KeyError, TypeError, ValueError) as exc:
            message = f"Erreur: {exc}"
            log(message)
            try:
                publish_status("error", message)
            except Exception as publish_exc:
                log(f"Impossible de publier le statut d'erreur: {publish_exc}")
        except Exception as exc:
            message = f"Erreur inattendue {type(exc).__name__}: {exc}"
            log(message)
            try:
                publish_status("error", message)
            except Exception:
                pass
        elapsed = time.monotonic() - started
        time.sleep(max(1, refresh_seconds - elapsed))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        log(f"Arrêt au démarrage: {exc}")
        sys.exit(1)
