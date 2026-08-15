# Changelog

## 1.2.1

- Prise en charge des exports CSV utilisant la tabulation comme séparateur.
- Reconnaissance des colonnes Nom du compte, Nom de la connexion et N° de chèque.
- Association des comptes par leur nom ou leur suffixe x1234.
- Utilisation de Labels comme catégorie de secours.


## 1.2.0

- Ajout de l’administration des transactions.
- Import CSV cumulatif avec détection des nouvelles opérations sans doublon.
- Validation atomique des fichiers et prise en charge des comptes multiples.
- Suppression globale des transactions avec confirmation et journal d’audit.
- Correction du calcul du budget mensuel sur le stock complet des transactions.

## 1.1.2

- Correction de l'erreur 500 pendant la première activation biométrique.
- Validation des expirations des flux WebAuthn et des sessions côté .NET pour assurer la compatibilité SQLite.
- Image privée AMD64 et ARM64 construite et publiée avec succès.

## 1.1.1

- Correction de la configuration FIDO2 empêchant la compilation de l'image 1.1.0.
- Publication vérifiée de l'image privée AMD64 et ARM64.
- Le backend peut démarrer avant la configuration du code d'activation.

## 1.1.0

- Base SQLite persistante dans `/data/glittering-bank.db`.
- Données fictives pour utilisateurs, profils, banques, comptes, transactions et budgets.
- Authentification biométrique par passkey WebAuthn.
- Code d'activation initial à usage unique pour le profil Philippe.
- Sessions sécurisées, challenges temporaires et journal d'audit.
- Montants stockés en centimes pour éviter les erreurs d'arrondi.

## 1.0.2

- Publication sous forme d'image Docker privée multiarchitecture.
- Ajout des mises à jour gérées directement par Home Assistant.
- Compatibilité Raspberry Pi 64 bits et AMD64.
- Lecture sécurisée de la configuration Home Assistant avant l'abandon des privilèges.

## 1.0.1

- Correction de l'accès à `/data/options.json`.

## 1.0.0

- Première version du backend ASP.NET Core.
