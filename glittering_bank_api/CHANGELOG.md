## 2.18.2

- Synchronise automatiquement BoursoBank environ toutes les 3 heures avec un décalage aléatoire de ±10 minutes.
- Stocke les identifiants BoursoBank chiffrés et conserve une empreinte salée du mot de passe.
- Historise les soldes, positions externes, informations des livrets et caractéristiques numériques des prêts.
- Ajoute les graphiques d’historique pour toutes les métriques numériques BoursoBank.
- Suspend la synchronisation et demande une validation lorsque BoursoBank impose une authentification forte.

## 2.18.1

- Intègre le frontend Vue directement dans l’image de l’add-on Home Assistant.
- Rend l’application complète accessible localement sur le port 5080.
- Le bouton « Ouvrir l’interface Web » ouvre désormais l’application GlitteringPrizes complète.

## 2.18.0

- Ajoute les caractéristiques détaillées des crédits immobiliers BoursoBank.
- Ajoute les positions de placement des comptes externes compatibles.
- Ajoute les informations détaillées des livrets BoursoBank et les transmet au frontend.

## 2.17.29

- Récupère le libellé du crédit immobilier depuis `c-info-box__account-label` sur la carte du prêt BoursoBank.
- Le libellé n’est plus bloquant lorsque la référence et le capital restant dû sont valides.

## 2.17.28

- Corrige le nom du crédit immobilier en utilisant le libellé produit dédié fourni par BoursoBank.

## 2.17.27

- Ajoute un diagnostic sécurisé de la structure de la page du crédit immobilier lorsque l’extraction d’un champ échoue.

## 2.17.26

- Ajoute temporairement dans le journal de l’add-on Home Assistant le détail métier parsé de chaque compte BoursoBank, compte externe agrégé et prêt afin de faciliter le diagnostic du connecteur.
- Les secrets d’authentification, cookies et données de session ne sont pas inclus dans ces lignes de diagnostic.

## 2.17.25

- Corrige le libellé du crédit immobilier BoursoBank en limitant son extraction au conteneur du nom du compte.
- Empêche les textes d’accessibilité de la page d’être utilisés comme nom du prêt.

## 2.17.24

- Corrige l’erreur d’exécution du parseur de crédit immobilier BoursoBank causée par l’import manquant du nettoyeur de texte partagé.

## 2.17.23

- Ajoute le crédit immobilier BoursoBank comme compte LOAN interne.
- Utilise le capital restant dû comme solde négatif et conserve la synchronisation des opérations désactivée pour ce compte.
- Génère un identifiant opaque stable sans exposer la référence du prêt, son URL, son libellé ou son montant dans les logs.

## 2.17.22

- Ajoute un diagnostic anonymisé des liens BoursoBank de crédit immobilier situés hors des routes classiques de comptes.
- Seuls le nombre de liens et la profondeur structurelle des chemins sont exposés ; aucune URL, aucun identifiant, aucun libellé et aucun montant.

## 2.17.21

- Ajoute un diagnostic anonymisé du nombre de liens de comptes crédit BoursoBank reconnus ou non par le format d’identifiant actuel.
- Aucune URL, aucun identifiant, aucun libellé et aucun montant ne sont exposés.

## 2.17.20

- Fix BoursoBank loan diagnostics and harden DOM parsing so loan cards can be individualized without exposing financial data.
- Add privacy-safe parsed/returned loan counters. Loan transaction synchronization remains disabled.

# Changelog

## 2.17.19

- Renforce l’individualisation des cartes crédit BoursoBank et ajoute des compteurs de diagnostic anonymisés.


## 2.17.18

- Conserve les comptes de la section crédit BoursoBank comme crédits internes malgré les sous-libellés produit.


## 2.17.17

- Utilise un parseur HTML structurel pour associer correctement chaque crédit BoursoBank à ses informations.


## 2.17.16

- Ajoute un diagnostic structurel anonymisé par carte crédit BoursoBank.


## 2.17.15

- Corrige la détection exacte des conteneurs de crédits BoursoBank.


## 2.17.14

- Isole chaque crédit dans son conteneur BoursoBank et retire les valeurs financières du diagnostic.


## 2.17.13

- Parse les crédits BoursoBank carte par carte pour gérer les multiples blocs de solde.


## 2.17.12

- Journalise le diagnostic anonymisé des cartes crédit avant validation du dashboard BoursoBank.


## 2.17.11

- Rend le diagnostic crédit disponible même si certaines cartes BoursoBank ne sont pas encore reconnues.


## 2.17.10

- Corrige l’anonymisation du diagnostic BoursoBank et ajoute les compteurs structurels nécessaires pour diagnostiquer les variantes de cartes crédit restantes.


## 2.17.9

- Détecte les crédits BoursoBank dont l’encours est affiché directement dans la carte.


## 2.17.8

- Affiche automatiquement le diagnostic anonymisé de structure des crédits BoursoBank dans l’interface locale après connexion.


## 2.17.7

- Ajoute un diagnostic anonymisé de la structure des crédits BoursoBank pour préparer leur prise en charge.


## 2.17.4

- Affiche les crédits BoursoBank et les comptes externes agrégés dans la liste locale d’association.
- Indique leur banque source et leur disponibilité de synchronisation.


## 2.17.3

- Ajoute la liste locale des comptes BoursoBank, leur association à un compte Glittering existant et leur synchronisation individuelle.
- Corrige l’import des montants décimaux renvoyés par le connecteur BoursoBank.


## 2.17.0

- Liste les comptes BoursoBank dans l’interface locale Home Assistant.
- Permet leur association à un compte GlitteringPrizes existant et leur synchronisation individuelle.
- Ajoute une protection contre les doublons lors de l’import des opérations.


## 2.16.25

- Corrige la reconnaissance des dates françaises des opérations BoursoBank.


## 2.16.24

- Corrige la finalisation des lignes d’opérations BoursoBank contenant des éléments HTML vides.


## 2.16.23

- Corrige le parsing structurel des dates, montants et libellés BoursoBank.


## 2.16.22

- Corrige le `NameError` du diagnostic d’historique BoursoBank.


## 2.16.21

- Ajoute le diagnostic anonymisé des formats nécessaires au parseur BoursoBank.


## 2.16.20

- Corrige la reconnaissance des lignes d’opérations BoursoBank et retire la trace de diagnostic temporaire.


## 2.16.19

- Adapte le parseur à la structure réelle des opérations BoursoBank observée en diagnostic.


## 2.16.18

- Ajoute le diagnostic structurel balises/classes pour finaliser le parseur des opérations BoursoBank.


## 2.16.17

- Corrige l’association des dates aux opérations BoursoBank et fiabilise la publication du backend.


## 2.16.16

- Restaure le diagnostic détaillé des lignes BoursoBank incomplètes.


## 2.16.15

- Ajoute le diagnostic structurel sûr des lignes d’opérations BoursoBank incomplètes.


## 2.16.13

- Corrige la lecture des séparateurs de dates dans l’historique BoursoBank.


## 2.16.12

- Ajoute le test local en lecture seule du parseur des opérations BoursoBank comptabilisées.


## 2.16.11

- Complète le diagnostic anonymisé nécessaire au parseur des opérations BoursoBank.


## 2.16.10

- Étend le diagnostic anonymisé de l’historique BoursoBank pour préparer le parseur des opérations.


## 2.16.9

- Ajoute le diagnostic local sécurisé de la structure d’historique BoursoBank.


## 2.16.8

- Publie l’image ARM64 GHCR vérifiée contenant le correctif du parseur BoursoBank.


## 2.16.6

- Force une image propre du parseur BoursoBank après l’incohérence observée en 2.16.5.


## 2.16.5

- Corrige la lecture des cartes de comptes du nouveau HTML BoursoBank.


## 2.16.4

- Supprime le double slash Ingress et sert l’interface Bourso à la racine sécurisée Home Assistant.


## 2.16.3

- Corrige l’ouverture de l’interface BoursoBank via Home Assistant Ingress et renforce la validation de l’origine Supervisor.


## 2.16.2

- Ajoute l’interface locale BoursoBank protégée par Home Assistant Ingress et CSRF ; les identifiants ne transitent pas par Vercel.


## 2.15.2

- Corrige le démarrage du connecteur BoursoBank sécurisé et ajoute un contrôle d’import Python au build.


## 2.15.1

- Durcissement complet du flux BoursoBank : identifiants réservés au chemin local, cookies de banque confinés au connecteur et validation stricte des hôtes BoursoBank.


## 2.14.1

- Administration BoursoBank sécurisée et import des comptes/soldes.


## 2.14.0

- Ajout du connecteur BoursoBank local et des endpoints REST administrateur pour l’authentification, la validation 2FA et la lecture des comptes.
- Le service Bourso écoute uniquement sur loopback dans l’image backend.


## 2.13.3

- Correction du module `actual-sync.mjs` sous Node.js : suppression de l'erreur `Illegal return statement` lors du chargement de la liste des comptes Actual Budget.

## 2.13.2

- La liste de synchronisation individuelle est désormais pilotée directement par Actual Budget.
- Les comptes reliés à un fournisseur bancaire sont proposés même sans correspondance GlitteringPrizes existante.
- Les comptes Actual purement manuels sont exclus grâce à `account_sync_source`.
- La synchronisation individuelle continue de cibler le compte via son identifiant Actual Budget.

## 2.13.0

- Ajout de la synchronisation individuelle d’un compte Actual Budget / Enable Banking depuis l’écran de synchronisation.
- Une synchronisation ciblée ne déclenche la récupération bancaire que pour le compte sélectionné.

## 2.12.9

- Historique de synchronisation normalisé : seules les opérations réellement nouvelles ou financièrement modifiées sont enregistrées comme changements.
- Conservation des anciennes et nouvelles valeurs de montant/date pour les modifications.
- Migration SQLite additive et non destructive ; les anciens snapshots et tout l’historique existant sont conservés.

## 2.12.8

- Le détail de synchronisation est limité aux nouvelles opérations et aux changements financiers réels (montant, date ou compte).
- Les simples rafraîchissements de libellé, catégorie ou référence ne remplissent plus artificiellement le détail avec plusieurs mois d’opérations.

## 2.12.7

- Le détail d’une synchronisation bancaire affiche uniquement les transactions ajoutées ou modifiées pendant cette synchronisation.
- Suppression de la reconstruction trompeuse des anciennes synchronisations sans snapshot exact.

## 2.12.6

- Affichage dans le détail d’un compte de la date de la dernière synchronisation Actual Budget réussie.
- Compatibilité SQLite conservée pour la récupération de cette date.

## 2.12.5

- Diagnostic détaillé du chargement des soldes initiaux pour identifier les erreurs SQLite ou de schéma restantes.

## 2.12.4

- Durcissement du chargement des soldes initiaux pour SQLite : le tri des comptes est effectué après matérialisation en mémoire.
- Ajout d’un test de régression SQLite couvrant les transactions avec `DateTimeOffset` dans l’administration des comptes.

## 2.12.3

- Correction du chargement des soldes initiaux dans l’administration des comptes.
- Les associations de comptes sont désormais chargées avec les autres métadonnées d’organisation et ne peuvent plus faire échouer toute la page pendant une migration SQLite.

## 2.12.2

- Correction de l’administration des comptes pendant la migration de l’organisation des comptes.
- Conservation des soldes disponibles pendant cette migration.
- Publication Docker optimisée pour le Raspberry Pi : image `linux/arm64` uniquement, sans build AMD64 ni QEMU.

## 2.12.1

- Correction des détails manquants dans l’historique des synchronisations Actual Budget.
- Reconstruction d’un aperçu depuis les données importées lorsqu’un snapshot de synchronisation manque.

## 2.12.0

- Dossiers de comptes désormais hiérarchiques avec sous-dossiers.
- Création, déplacement et affichage de l’arborescence des dossiers.
- Agrégation des soldes dans l’arborescence.
- Protection contre les boucles lors du déplacement des dossiers.

## 2.11.0

- Ajout des dossiers et des étiquettes pour organiser les comptes.
- Administration des dossiers/tags et regroupement des comptes dans l’interface.

## 2.10.0

- Ajout d’un libellé personnalisé pour chaque compte.
- Utilisation de l’alias dans le tableau de bord, les transactions et les autres écrans tout en conservant le nom source.

## 2.9.1

- Affichage du nombre de résultats d’une recherche de transactions.
- Affichage de la somme signée des résultats : débits négatifs et crédits positifs.

## 2.9.0

- Association de plusieurs comptes pour les présenter comme un ensemble.
- Agrégation des comptes associés dans le tableau de bord, les recherches et le détail des comptes.
- Administration des associations de comptes.

## 2.8.12

- Affichage de l’année dans les dates des résultats de recherche.

## 2.8.11

- Restauration de la version du frontend dans le pied du menu de navigation.

## 2.8.10

- Amélioration de la disposition des actions de recherche sur mobile.

## 2.8.9

- Correction de l’affichage des contrôles de recherche repliés sur mobile.

## 2.8.8

- Correction de la recherche lancée depuis un compte : elle n’est plus exécutée automatiquement avant validation.

## 2.8.7

- Repli automatique du formulaire de recherche après l’affichage des résultats.

## 2.8.6

- Ajout d’un raccourci de recherche des transactions limité à un compte.

## 2.8.5

- Réorganisation de la vue d’ensemble et déplacement de ses fonctions dans la navigation principale.

## 2.8.4

- Le détail d’une transaction affiche désormais son compte et permet d’ouvrir directement ce compte.

## 2.8.3

- Synchronisation bancaire et double authentification déplacées vers des pages dédiées.
- Navigation d’administration simplifiée.

## 2.8.2

- L’historique Actual Budget affiche par défaut les 10 dernières synchronisations ayant ramené des transactions.
- Ajout d’un formulaire de recherche, d’un filtre pour les synchronisations vides et du choix du nombre de résultats.
- Correction de compilation de l’endpoint d’historique.

## 2.8.1

- Enregistrement d’un snapshot des soldes et transactions pour chaque synchronisation Actual Budget réussie.
- Les entrées d’historique peuvent être ouvertes pour consulter le détail de la synchronisation.

## 2.8.0

- Ajout de la double authentification TOTP après le passkey.
- Compatibilité avec Google Authenticator et les applications TOTP standards.
- Administration de l’activation et de la désactivation du TOTP.

## 2.7.5

- Correction d’un tri `DateTimeOffset` incompatible avec SQLite pendant la synchronisation Actual Budget.

## 2.7.4

- Correction de l’initialisation et des permissions du cache local de l’API Actual Budget.

## 2.7.3

- Correction du tri de l’historique des synchronisations pour assurer la compatibilité SQLite.

## 2.7.2

- Ajout du panneau d’administration de la synchronisation Actual Budget.
- Affichage de l’état et de l’historique des synchronisations et déclenchement manuel.
- Correction de la lecture des valeurs de configuration Actual vides.

## 2.7.1

- Correction des permissions de lecture de la configuration Home Assistant avant l’abandon des privilèges.
- Les paramètres Actual Budget sont transmis au backend via l’environnement.

## 2.7.0

- Synchronisation automatique avec Actual Budget et Enable Banking.
- Import idempotent des comptes, soldes et transactions Actual Budget.
- Synchronisation périodique configurable et déclenchement de la synchronisation bancaire Actual.

## 2.6.0

- Frontend désormais installable comme une application mobile PWA.
- Icônes Android et iOS, lancement autonome et interface disponible hors connexion.
- Les API et les données bancaires restent exclues du cache hors ligne.

## 2.5.1

- Correction du tableau de bord lorsqu’aucun budget n’existe pour le mois courant.
- Réutilisation automatique de la dernière limite connue, ou zéro si aucun budget n’existe.
- Valeurs d’authentification initiales sécurisées pour les nouvelles installations.

## 2.5.0

- Total cumulé affiché dans l’en-tête des opérations semblables.
- Somme signée des débits et crédits, indépendante du tri.
- Affichage adapté aux écrans mobiles.

## 2.4.0

- Opérations semblables triées par défaut de la plus récente à la plus ancienne.
- Tris disponibles par date, montant absolu, libellé et score de similarité.

## 2.3.0

- Interface mobile fluide sans défilement horizontal global.
- Menu burger déplacé en haut à gauche avec tiroir latéral.
- Tableaux, graphiques et administration compactés pour les petits écrans.

## 2.2.1

- Correction du sélecteur de fichiers sur mobile pour permettre l’accès aux documents CSV.
- Validation de l’extension `.csv` et limite de 10 Mo conservées.

## 2.2.0

- Affichage du solde après chaque opération dans l’historique d’un compte.
- Montant présenté de façon compacte en petit, gris et italique.
- Calcul chronologique fiable à partir du solde initial.

## 2.1.0

- Affichage des comptes sous forme de tableau dans la vue d’ensemble.
- Liste de comptes dans les filtres de recherche.
- Administration de la visibilité des comptes.
- Exclusion des comptes masqués du tableau de bord, des recherches et de leur détail.
- Migration automatique des installations SQLite existantes.

## 2.0.0

- Attribution automatique d’une icône adaptée à la catégorie de chaque opération.
- Nouvel écran permanent des dépenses mensuelles par catégorie avec graphique camembert interactif.
- Sélection d’un mois et consultation des opérations composant chaque catégorie.
- Date mise en évidence dans la liste des opérations similaires.

## 1.9.0

- Axe des ordonnées gradué en euros dans l’analyse mensuelle.
- Sélection interactive d’un jour sur les courbes.
- Comparaison du solde de toutes les séries au jour sélectionné.

## 1.8.0

- Nouvelle vue d’analyse mensuelle dans le détail des comptes.
- Comparaison jour par jour du solde sur deux à douze mois.
- Report du dernier solde connu sur les journées sans opération.

## 1.7.0

- Fiche détaillée au clic sur chaque opération bancaire.
- Affichage des opérations semblables avec score et raison de correspondance.
- Algorithme hybride tolérant les abréviations, fautes et libellés bancaires bruités.

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
