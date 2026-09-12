# Glittering Bank API

Backend ASP.NET Core privé de l'application Glittering Prizes.

## Configuration générale

- `api_key` : clé longue utilisée uniquement entre Vercel et le backend.
- `activation_code` : code temporaire choisi par l'utilisateur pour enregistrer le premier passkey du profil Philippe.

Après l'enregistrement du premier passkey, le code d'activation ne permet plus d'accéder au compte. L'empreinte digitale reste dans le téléphone : seule une clé publique WebAuthn est enregistrée dans SQLite.

## Synchronisation Actual Budget / Enable Banking

À partir de la version 2.7.0, Glittering Bank API peut alimenter automatiquement sa base depuis Actual Budget.

Paramètres :

- `actual_enabled` : active la synchronisation automatique.
- `actual_server_url` : URL interne du serveur Actual. Valeur recommandée : `http://gpt_actual_budget:5006`.
- `actual_password` : mot de passe serveur Actual Budget. Il reste dans les options Home Assistant et ne doit jamais être commité dans GitHub.
- `actual_sync_id` : Sync ID du budget Actual (Actual > Settings > Show advanced settings > Sync ID).
- `actual_encryption_password` : uniquement si le budget Actual utilise le chiffrement de bout en bout.
- `actual_sync_interval_minutes` : cadence de synchronisation. La valeur recommandée est `60`.
- `actual_lookback_days` : fenêtre de transactions relue à chaque passage. Valeur recommandée : `120`.
- `actual_run_bank_sync` : demande à Actual de lancer d'abord la synchronisation bancaire Enable Banking.

Le flux est :

`BoursoBank -> Enable Banking -> Actual Budget -> Glittering Bank API -> SQLite`

Le backend utilise le client officiel `@actual-app/api`. Il demande à Actual de synchroniser les comptes bancaires, relit les transactions, puis réalise un upsert à partir de l'identifiant Actual de chaque transaction. Une transaction déjà importée n'est donc pas dupliquée lors du passage suivant.

Les comptes existants sont rapprochés par nom lors de la première synchronisation, puis liés durablement à leur identifiant Actual. Le solde d'ouverture Glittering est recalculé pour que le solde courant affiché corresponde au solde Actual.

La première synchronisation automatique démarre environ 30 secondes après le démarrage de l'App, puis se répète suivant `actual_sync_interval_minutes`.

## Persistance

La base est stockée dans `/data/glittering-bank.db`. Home Assistant conserve ce répertoire pendant les mises à jour de l'application et l'intègre aux sauvegardes.

Le cache local utilisé par l'API Actual est stocké sous `/data/actual-api-cache`.

## Endpoints

- `/health` : état du service, de SQLite et dernier état de synchronisation Actual
- `/api/auth/*` : activation, connexion et session passkey
- `/api/dashboard` : tableau de bord authentifié
- `GET /api/admin/actual-sync/status` : état détaillé de la dernière synchronisation
- `POST /api/admin/actual-sync` : déclenche une synchronisation immédiate

Les routes `/api/*` exigent également l'en-tête privé `X-API-Key` envoyé par Vercel.
