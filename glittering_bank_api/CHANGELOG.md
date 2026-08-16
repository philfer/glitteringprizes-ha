# Changelog

## 1.6.0

- Correction de la version installée affichée par l’écran d’administration.
- Transmission explicite de la version Home Assistant au backend .NET.
- Ajout du tag Git automatique à chaque publication du catalogue.


## 1.5.0

- Historique du solde de chaque compte depuis son solde initial.
- Écran de détail avec graphique responsive et transactions associées.
- Recherche par libellé, débit ou crédit, plage de dates et sélection de comptes.
- API sécurisées limitant chaque utilisateur aux comptes dont il est propriétaire.

## 1.4.0

- Calcul de chaque solde courant à partir du solde initial et des opérations importées.
- Ajout d’un menu administrateur pour définir le solde initial de chaque compte.
- Conservation des soldes initiaux lors de la suppression globale des transactions.
- Tests SQLite du calcul, de la persistance et des autorisations.

## 1.3.2

- Correction de l’import CSV dans l’image Alpine Home Assistant en mode de globalisation invariant.
- Analyse des dates et montants français sans dépendance à la locale `fr-FR`.
- Tests .NET et SQLite exécutés en CI dans le même mode de globalisation que le module.
- Création automatique des comptes absents lors de l’import et restitution détaillée des erreurs, introduites en 1.3.1.

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
