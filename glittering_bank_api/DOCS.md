# Glittering Bank API

Backend ASP.NET Core privé de l'application Glittering Prizes.

## Configuration

Renseignez une clé longue et aléatoire dans le champ `api_key`. Cette clé reste stockée localement par Home Assistant et n'est pas incluse dans l'image Docker.

## Endpoints

- `/health` : état du service
- `/api/dashboard` : tableau de bord fictif
- `/api/accounts` : comptes fictifs
- `/api/transactions` : transactions fictives

Les routes `/api/*` exigent l'en-tête HTTP `X-API-Key`.

## Accès local

L'API écoute sur le port `5080`. Le contrôle de santé est accessible à l'adresse :

`http://homeassistant.local:5080/health`
