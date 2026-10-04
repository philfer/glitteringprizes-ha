#!/bin/bash
set -euo pipefail

DATA_DIR=/data
PGDATA="$DATA_DIR/postgresql"
SECRETS_DIR="$DATA_DIR/.secrets"
mkdir -p "$SECRETS_DIR" "$PGDATA"
chown -R postgres:postgres "$PGDATA"

if [ ! -s "$SECRETS_DIR/postgres_password" ]; then
  openssl rand -base64 24 > "$SECRETS_DIR/postgres_password"
  chmod 600 "$SECRETS_DIR/postgres_password" || true
fi
export POSTGRES_PASSWORD="$(cat "$SECRETS_DIR/postgres_password")"
export POSTGRES_DB=picsou
export POSTGRES_USER=picsou

PG_BIN="$(dirname "$(find /usr/lib/postgresql -type f -name initdb | sort -V | tail -1)")"

if [ ! -s "$PGDATA/PG_VERSION" ]; then
  echo "[ha-addon] Initialisation de PostgreSQL..."
  PWFILE="$(mktemp)"
  printf '%s' "$POSTGRES_PASSWORD" > "$PWFILE"
  chown postgres:postgres "$PWFILE"
  runuser -u postgres -- "$PG_BIN/initdb" -D "$PGDATA" --username="$POSTGRES_USER" --pwfile="$PWFILE" --auth-host=scram-sha-256 --auth-local=trust
  rm -f "$PWFILE"
fi

runuser -u postgres -- "$PG_BIN/pg_ctl" -D "$PGDATA" -o "-c listen_addresses=127.0.0.1 -p 5432" -w start

if ! runuser -u postgres -- env PGPASSWORD="$POSTGRES_PASSWORD" psql -h 127.0.0.1 -U "$POSTGRES_USER" -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$POSTGRES_DB'" | grep -q 1; then
  runuser -u postgres -- env PGPASSWORD="$POSTGRES_PASSWORD" createdb -h 127.0.0.1 -U "$POSTGRES_USER" "$POSTGRES_DB"
fi

export SPRING_DATASOURCE_URL="jdbc:postgresql://127.0.0.1:5432/$POSTGRES_DB?sslmode=disable"
export SPRING_DATASOURCE_USERNAME="$POSTGRES_USER"
export SPRING_DATASOURCE_PASSWORD="$POSTGRES_PASSWORD"
export BOURSO_AUTH_URL="http://127.0.0.1:8001"
export SPRING_PROFILES_ACTIVE=prod
export HSTS_ENABLED=false

echo "[ha-addon] Démarrage du connecteur BoursoBank..."
(
  cd /opt/bourso
  exec python3 -m uvicorn main:app --host 127.0.0.1 --port 8001
) &
BOURSO_PID=$!

cleanup() {
  kill "$BOURSO_PID" 2>/dev/null || true
  runuser -u postgres -- "$PG_BIN/pg_ctl" -D "$PGDATA" -m fast stop 2>/dev/null || true
}
trap cleanup EXIT INT TERM

echo "[ha-addon] Démarrage de Picsou Finance..."
exec /app/entrypoint.sh
