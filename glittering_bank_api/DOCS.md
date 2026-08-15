# Glittering Bank API

Backend ASP.NET Core privé de l'application Glittering Prizes.

## Configuration

- `api_key` : clé longue utilisée uniquement entre Vercel et le backend.
- `activation_code` : code temporaire choisi par l'utilisateur pour enregistrer le premier passkey du profil Philippe.

Après l'enregistrement du premier passkey, le code d'activation ne permet plus d'accéder au compte. L'empreinte digitale reste dans le téléphone : seule une clé publique WebAuthn est enregistrée dans SQLite.

## Persistance

La base est stockée dans `/data/glittering-bank.db`. Home Assistant conserve ce répertoire pendant les mises à jour de l'application et l'intègre aux sauvegardes.

## Endpoints

- `/health` : état du service et de SQLite
- `/api/auth/*` : activation, connexion et session passkey
- `/api/dashboard` : tableau de bord fictif authentifié

Les routes `/api/*` exigent également l'en-tête privé `X-API-Key` envoyé par Vercel.
