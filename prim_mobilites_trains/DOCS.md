# PRIM Mobilités - Villeneuve-le-Roi

Cet add-on interroge l'API **Prochains passages** de PRIM / Île-de-France Mobilités et publie les prochains RER C de **Villeneuve-le-Roi vers Paris** directement dans Home Assistant.

## Pré-requis

1. Créer un compte sur PRIM Île-de-France Mobilités.
2. Générer un jeton API.
3. Installer cet add-on depuis le dépôt Home Assistant `philfer/glitteringprizes-ha`.
4. Dans l'onglet **Configuration** de l'add-on, saisir le jeton dans `api_key`.

Ne placez jamais la clé PRIM dans votre dashboard Lovelace.

## Entités créées

- `sensor.rer_c_villeneuve_le_roi_paris` : nombre de trains disponibles et attribut `trains` avec les prochains passages.
- `sensor.rer_c_villeneuve_le_roi_prochain_train` : prochain départ prévu avec destination, retard, statut et voie si fournie.
- `sensor.prim_mobilites_villeneuve_le_roi_status` : état `ok` ou `error`.

## Carte Dashboard

Ajoutez une carte **Markdown** dans Lovelace et utilisez le contenu de `dashboard-card.yaml`.

## Direction Paris

Pour la SNCF, l'API est interrogée au niveau zone d'arrêt `STIF:StopArea:SP:69625:` puis filtrée sur le RER C `STIF:Line::C01727:` et sur les destinations configurées dans `destination_keywords`.

Valeurs par défaut : Versailles, Invalides, Saint-Quentin-en-Yvelines, Pontoise et Paris Austerlitz.

## Fréquence

Par défaut : 60 secondes. Le minimum est fixé à 60 secondes afin de respecter la fréquence d'actualisation recommandée pour les données temps réel PRIM.
