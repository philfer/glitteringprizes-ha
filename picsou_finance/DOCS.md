# Picsou Finance

Cet add-on adapte Picsou Finance à Home Assistant sur **aarch64 (Raspberry Pi)** et amd64.

Il regroupe dans un seul add-on :
- Picsou Finance (frontend + backend) ;
- PostgreSQL, stocké de façon persistante dans `/data/postgresql` ;
- le sidecar local `bourso-auth` pour BoursoBank.

## Installation

Après avoir actualisé le dépôt de modules complémentaires Home Assistant, installez **Picsou Finance**, puis démarrez-le.

Ouvrez ensuite l'interface depuis le bouton **Ouvrir l'interface Web**. Le port LAN 8088 est également publié pour le diagnostic local.

Au premier lancement, Picsou affiche son assistant de configuration et crée ses secrets dans `/data/.secrets`.

## BoursoBank

Dans Picsou, utilisez le connecteur BoursoBank. Les identifiants et sessions bancaires restent dans l'instance locale. Ne placez jamais vos identifiants BoursoBank dans GitHub ou dans la configuration du dépôt.

Le sidecar Bourso écoute uniquement sur `127.0.0.1:8001` à l'intérieur de l'add-on et n'est pas exposé au réseau.

## Sauvegarde

Les données PostgreSQL et les secrets sont sous `/data` et sont donc inclus dans les sauvegardes Home Assistant de l'add-on.

## Sécurité

Picsou est prévu pour un usage personnel/local et n'a pas fait l'objet d'un audit de sécurité professionnel. L'accès Home Assistant Ingress est privilégié. N'exposez pas directement le port 8088 sur Internet.

## Mise à jour

La version 1.0.0 de cet emballage utilise les images `latest` publiées par Picsou. Une reconstruction de l'add-on récupère les images amont disponibles au moment du build.
