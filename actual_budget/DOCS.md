# Actual Budget

Actual Budget est exécuté comme App Home Assistant à partir de l'image officielle `ghcr.io/actualbudget/actual-server`.

## Accès

Le serveur Actual écoute en HTTP sur le port local `5006`.
L'accès utilisateur passe par le Cloudflare Tunnel existant via :

`https://actual.glittering-prizes.net`

Le tunnel doit router ce hostname vers :

`http://172.30.32.1:5006`

Le bouton **Ouvrir l'interface Web** de l'App pointe directement vers l'URL HTTPS Cloudflare.

## Utilisation

1. Installer ou mettre à jour l'App **Actual Budget** depuis le dépôt `philfer/glitteringprizes-ha`.
2. Démarrer l'App.
3. Ouvrir **Ouvrir l'interface Web**.
4. Lors du premier lancement, définir le mot de passe serveur Actual Budget.
5. Créer ou importer un budget.
6. Configurer ensuite la synchronisation bancaire dans Actual Budget.

## Sécurité

Le chiffrement TLS est terminé par Cloudflare Tunnel. Actual reste en HTTP sur le réseau interne Home Assistant et le port 5006 ne doit pas être exposé directement sur Internet.
Les données sont conservées dans le stockage persistant de l'App.

## Intégration GlitteringPrizes

Une étape ultérieure pourra ajouter un bridge local utilisant l'API officielle `@actual-app/api` afin que GlitteringPrizes puisse lire les comptes, soldes et transactions sans connaître les identifiants bancaires.
