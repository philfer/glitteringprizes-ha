# Glittering Prizes — Home Assistant

Dépôt Home Assistant de Philippe.

## Apps disponibles

### Glittering Bank API
Backend bancaire utilisé par GlitteringPrizes.

### Actual Budget
Instance Actual Budget auto-hébergée dans Home Assistant, avec données persistantes dans `/data` et accès via Home Assistant Ingress.

## Installation

Ajoutez ce dépôt dans la boutique des applications Home Assistant :

`https://github.com/philfer/glitteringprizes-ha`

Puis rechargez la boutique. Les Apps disponibles apparaîtront dans ce dépôt.

## Sécurité

Ce dépôt ne contient aucun identifiant bancaire ni secret utilisateur. Actual Budget est configuré sans port réseau publié directement ; son interface passe par Home Assistant Ingress.
