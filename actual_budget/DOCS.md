# Actual Budget

Actual Budget est exécuté directement comme App Home Assistant à partir de l'image officielle `actualbudget/actual-server:latest-alpine`.

## Utilisation

1. Installer l'App **Actual Budget** depuis le dépôt `philfer/glitteringprizes-ha`.
2. Démarrer l'App.
3. Ouvrir l'interface via **Ouvrir l'interface Web** ou la barre latérale Home Assistant.
4. Lors du premier lancement, définir le mot de passe serveur Actual Budget.
5. Créer ou importer un budget.
6. Configurer ensuite la synchronisation bancaire dans Actual Budget.

## Sécurité

L'App n'expose volontairement aucun port réseau. L'accès passe par Home Assistant Ingress.
Les données sont conservées dans `/data`, le stockage persistant de l'App.

## Intégration GlitteringPrizes

Une étape ultérieure ajoutera un bridge local utilisant l'API officielle `@actual-app/api` afin que GlitteringPrizes puisse lire les comptes, soldes et transactions sans connaître les identifiants bancaires.
