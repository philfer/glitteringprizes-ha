## 2.18.51

- fix

## 2.18.50

- fix

## 2.18.49

- fix sql

## 2.18.48

- fix pour 2.18.48

## 2.18.47

- Corrige le plantage au démarrage de Home Assistant (`SQLite Error 1: near "@p0"`) : les noms de tables de la migration SQLite sont désormais intégrés à la requête SQL au lieu d'être passés comme paramètres.
- Migration additive et relançable, sans suppression ni réinitialisation de la base SQLite existante.

## 2.18.46

- Corrige le plantage au démarrage de Home Assistant (`SQLite Error 1: near "@p0"`) : les noms de tables de la migration SQLite sont désormais intégrés à la requête SQL au lieu d'être passés comme paramètres.
- Migration additive et relançable, sans suppression ni réinitialisation de la base SQLite existante.

## 2.18.45

- Intègre les contrats bancaires partagés et les nouveaux fetchers BoursoBank / Actual Budget introduits par la PR #149.
- Corrige le Dockerfile Home Assistant pour copier `GlitteringBank.Common` et `GlitteringBank.EnableBanking` avant la restauration et la publication .NET.
- Rétablit la possibilité de construire l'image Home Assistant avec ces dépendances ; la validation de la publication reste à confirmer.

## 2.18.44

- Corrige l'API de détail des comptes : lecture des tables relationnelles normalisées, avec repli sur les anciennes données JSON.
- Préserve les valeurs complexes (tableaux et objets imbriqués, notamment `Operations`) pendant la transition.

## 2.18.43

- Corrige le plantage au démarrage lors de la migration des détails de comptes vers SQLite : attribution de clés uniques avant le suivi EF Core des entités TPC.
- Réutilise les détails déjà suivis en mémoire pour éviter les doublons lors de la migration et de la synchronisation BoursoBank.

## 2.18.42

- Remplace l'écriture des détails de comptes BoursoBank en JSON par des tables relationnelles spécialisées (courant, épargne, crédit, placements et positions).
- Ajoute une migration additive et relançable des données historiques vers ces tables, en conservant temporairement les anciennes colonnes JSON pour sécuriser la transition.
- Corrige les contraintes génériques C# des modèles de détails de comptes et valide la compilation en CI.

## 2.18.41

- Corrige l'échec de synchronisation automatique BoursoBank lié à une association `AccountOwner` ajoutée deux fois au suivi Entity Framework Core.
- Vérifie les associations déjà suivies en mémoire et celles enregistrées en base avant insertion, sans modifier les transactions ni supprimer les associations existantes.

## 2.18.40

- Harmonise le style C# et applique les conventions communes StyleCop dans le backend et le connecteur natif BoursoBank.
- Finalise les ajustements de formatage des classes, modèles et tests, sans modification fonctionnelle intentionnelle.
- Conserve la synchronisation BoursoBank native C#, Actual Budget et la configuration existante.

## 2.18.39

- Affiche désormais la stacktrace complète des erreurs de synchronisation automatique BoursoBank dans les journaux Home Assistant via `LogError(exception, ...)`.

## 2.18.38

- Corrige `CultureNotFoundException` lors de la récupération des détails de comptes BoursoBank par le connecteur natif C#.
- Installe les bibliothèques et données ICU dans l'image Home Assistant Alpine et désactive le mode de globalisation invariant de .NET.
- Conserve `actual-sync.mjs` et l'intégration Actual Budget inchangés.

## 2.18.37

- Passage du SDK et du runtime du backend à .NET 10 et adaptation du Dockerfile pour compiler la bibliothèque C# BoursoBank référencée.
- Mise à jour du SDK GitHub Actions de validation vers .NET 10.
- Préparation du déploiement Home Assistant avec cette correction de compilation.
- Le connecteur Python reste actuellement actif dans le backend publié ; le basculement complet vers le fetcher C# n'est pas inclus dans cette version.

## 2.18.36

- Correction des expressions régulières de parsing des positions BoursoBank : reconnaissance des libellés d'actifs et des dates de valorisation.
- Diagnostics structurels des tableaux de positions (présence, nombre de lignes, anomalies de colonnes ou libellés) sans données bancaires sensibles.
- Build backend du correctif vérifiée avec succès avant publication.

## 2.18.35

- Positions BoursoBank : découverte sécurisée du lien de positions et de pfmAccountKey dans la page du compte, sans exposer la clé dans les logs.
- Extraction améliorée des libellés d'actifs et dates de valorisation depuis le tableau HTML.
- Diagnostics de provenance de la clé et horodatage des journaux Python/Uvicorn visibles dans Home Assistant.
- Correction de syntaxe Python validée par la build du backend.

## 2.18.34

- Sécurité BoursoBank : contrôle des hôtes sortants existants et blocage des destinations non approuvées, y compris les redirections ; aucun nouveau domaine externe.
- Vérification du statut HTTP du tableau de comptes, isolation des erreurs non critiques de positions, propagation des expirations de session et signalement des synchronisations concurrentes.

## 2.18.33

- Diagnostic de la synchronisation BoursoBank : statut HTTP et code d'erreur du connecteur sans données sensibles.

## 2.18.32 
- 2.18.33 : diagnostic des échecs BoursoBank /accounts avec statut HTTP et code amont filtré, sans journalisation des données sensibles.
- Diagnostic BoursoBank des placements : étapes de découverte des pages, codes HTTP, présence des tableaux et nombre de positions, avec identifiants pseudonymisés et sans données financières dans les logs. Recherche des liens de placements sans restriction au chemin PERP/PERCO.
- Recherche globale des comptes déplacée en tête de l'administration et appliquée aux sélecteurs de fusion/suppression et aux modules de gestion.
- Suppression de dossier : réaffecte les comptes et sous-dossiers directement à la racine virtuelle (FolderId/ParentFolderId nuls), au lieu du dossier parent.
- Ajoute l'action de suppression confirmée dans l'administration des dossiers.

## 2.18.30
- Corrige l'association utilisateur des comptes BoursoBank déjà existants : les comptes actifs synchronisés retrouvent leur propriétaire lors de la prochaine synchronisation.
- Supprime l'autorisation automatique fondée sur le sous-réseau local ; l'authentification reste obligatoire hors proxy Home Assistant explicitement approuvé.
- Corrige la route Vercel permettant de consulter les comptes BoursoBank synchronisés et leurs relevés.

## 2.18.29
- Administration BoursoBank : affiche les comptes actifs gérés par la synchronisation automatique.
- Présente les cinq derniers relevés de soldes disponibles, par compte et par date, avec actualisation manuelle.
- Restreint la confiance réseau locale à 192.168.1.0/24 et réserve les en-têtes d'identité Home Assistant aux adresses de proxy explicitement autorisées.
- Isole la clé de chiffrement des identifiants BoursoBank de la clé API et migre les identifiants déjà chiffrés.
- Maintient le connecteur Python BoursoBank sur l'interface loopback et ajoute des contrôles de sécurité au workflow de validation.

## 2.18.28
- Import CSV en deux étapes : prévisualisation des comptes et association explicite à un compte existant ou nouveau avant intégration.
- Conservation des opérations historiques dans les comptes bancaires sélectionnés.

## 2.18.27
- Active la tentative de synchronisation des opérations des comptes externes courants et d'épargne visibles dans BoursoBank.
- Isole les clés de déduplication par compte pour éviter les collisions entre banques.
- Signale les erreurs HTTP et redirections de connexion pendant la lecture des mouvements au lieu de les interpréter comme un historique vide.
- Les comptes externes dont BoursoBank ne fournit pas de page de mouvements compatible restent non synchronisés.

## 2.18.26
- Ajoute la gestion administrateur des comptes : prévisualisation, exclusions de synchronisation, suppression et fusion avec confirmation.
- Empêche la réimportation automatique des comptes exclus depuis BoursoBank et Actual Budget.
- Renforce l'association des comptes Actual Budget pour éviter les rapprochements par nom entre banques.
- Préserve les propriétaires, les tags et les métriques BoursoBank lors des opérations de fusion.

## 2.18.25
- Corrige les URLs `/transaction-icons/...` sous Home Assistant Ingress en les rendant relatives au préfixe dynamique de l’add-on.
- Invalide le cache PWA 2.18.24 pour diffuser immédiatement le nouveau frontend.

## 2.18.24
- Force l’invalidation du cache PWA historique qui pouvait continuer à servir un ancien frontend malgré la mise à jour de l’add-on.
- Le rendu des logos de transactions est désormais centralisé et cohérent dans tous les écrans.

## 2.18.23
- `TransactionPresentation` conserve désormais les icônes image locales ou distantes avant le mapping catégorie → emoji.
- Permet ainsi aux logos BoursoBank réellement stockés sur les transactions d’arriver jusqu’au frontend.
- Ajoute des tests de non-régression pour une transaction MAIF classée `Assurances (Auto/Moto)`.

## 2.18.22
- Met à jour les transactions BoursoBank existantes lors d’une resynchronisation afin de remplacer les anciens emojis par le logo local quand il est disponible.
- Complète également catégorie, libellé et détail natif sans créer de doublon.

## 2.18.21
- Met en cache localement dans `/data/transaction-icons` les logos des opérations BoursoBank et les sert via `/transaction-icons`.
- Parse `list__movement--label-initial` et conserve ce détail dans la référence de la transaction, sans remplacer la clé anti-doublon basée sur `data-id`.

## 2.18.20
- Ajoute l’import automatique des transactions BoursoBank sur 120 jours pour les comptes supportés et non externes.
- Parse les opérations par `list-operation-date-line` / `list-operation-item` : catégorie, libellé utilisateur, montant, logo, date et `data-id`.
- Persiste catégorie et logo et utilise le `data-id` comme clé d’import stable anti-doublon.

## 2.18.19
- Migre les anciens crédits immobiliers BoursoBank vers l’identifiant stable `bourso_mortgage_*` et désactive/masque les copies historiques portant le même libellé.

## 2.18.18
- Normalise les noms et familles de comptes BoursoBank lors de l’upsert afin de rapprocher les doublons malgré les variations de ponctuation, accents ou classification d’épargne/investissement.

## 2.18.17
- Corrige l’upsert BoursoBank lorsque l’identifiant technique amont change entre deux sessions.
- Rapproche les comptes Bourso existants par banque, nom et type et désactive/masque les doublons actifs existants sans suppression physique.

## 2.18.16
- Simplifie l’interface BoursoBank : les identifiants chiffrés déjà stockés restent masqués pendant les synchronisations et ne sont modifiables que via l’action dédiée.

## 2.18.15
- Expose les positions détaillées des comptes d’investissement BoursoBank dans le détail du compte : quantité, prix de revient, cours, valorisation, plus-value en euros et pourcentage calculé.

## 2.18.15
- Affiche les positions détaillées des comptes d’investissement BoursoBank : quantité, prix de revient, cours, valorisation et plus-value en euros.
- Calcule et affiche la plus-value latente en pourcentage lorsque les données BoursoBank permettent de déterminer le prix de revient total.

## 2.18.14
- Corrige l’extraction des caractéristiques détaillées BoursoBank pour les prêts immobiliers, les livrets/épargne et les positions des placements externes.
- Persiste ces informations afin qu’elles soient disponibles dans le détail des comptes GlitteringPrizes.

## 2.18.13
- Corrige la synchronisation BoursoBank lorsque `balanceEur` est renvoyé sous forme de chaîne JSON au lieu d’un nombre ; les formats numériques et textuels sont désormais acceptés.

## 2.18.12
- Corrige Administration > Comptes dans le frontend Home Assistant : le chargement utilise directement les endpoints backend JSON au lieu de tomber sur le fallback HTML Vue.

## 2.18.11
- Corrige la synchronisation BoursoBank avec SQLite en effectuant côté .NET le tri des administrateurs par `CreatedAt` (`DateTimeOffset`), non pris en charge par SQLite dans une clause `ORDER BY`.

## 2.18.10
- Corrige le déchiffrement AES-GCM des identifiants BoursoBank en utilisant correctement le ciphertext et le tag. Les identifiants déjà enregistrés avec le format existant restent compatibles.

## 2.18.9

- Log manual Bourso synchronization exceptions in the Home Assistant add-on journal.
- Return the underlying Bourso synchronization error to the frontend instead of an opaque HTTP 502.

## 2.18.8

- Skip GlitteringPrizes passkey authentication for private LAN clients and Home Assistant Ingress.
- Fix local frontend authentication URLs to call the backend /api/auth/* routes instead of the Vercel proxy route.

## 2.18.7

- Trust authenticated Home Assistant Ingress requests and skip passkey authentication only through Ingress.
- Keep frontend and authentication API calls under the dynamic Home Assistant Ingress path.

## 2.18.6

- Allow the passkey flow on homeassistant.local in addition to localhost loopback origins.

## 2.18.5

- Allow the passkey flow on localhost, 127.0.0.1 and ::1 while keeping HTTPS required for non-local origins.

## 2.18.4

- Build frontend assets with relative URLs so JavaScript and CSS load correctly behind Home Assistant Ingress.

## 2.18.3

- Open the complete backend-hosted GlitteringPrizes application from the Home Assistant add-on Web UI instead of the legacy BoursoBank-only page.

## 2.18.2

- Add automatic BoursoBank synchronization every ~3 hours with a fresh random ±10 minute offset after each run.
- Store BoursoBank credentials encrypted at rest with AES-GCM and keep a salted PBKDF2 password fingerprint; secrets are never returned by the API.
- Preserve MFA: automatic synchronization pauses and reports when BoursoBank requires user validation.
- Persist timestamped numeric history for account balances, external positions, savings metadata and mortgage characteristics.
- Add generic frontend charts for every numeric BoursoBank metric.

## 2.18.1

- Bundle the Vue frontend into the Home Assistant backend image and serve it from ASP.NET Core on port 5080.
- Keep API calls relative so the same frontend works locally and on Vercel.
- Open the full GlitteringPrizes interface from the Home Assistant add-on Web UI button.

## 2.18.0

- Extract and expose detailed BoursoBank mortgage characteristics.
- Extract, persist and expose investment positions for supported aggregated external accounts.
- Extract, persist and expose BoursoBank savings databox information such as accrued interest, ceiling, opening date and interest rate.
- Surface the new account metadata in the frontend account detail view.

## 2.17.29

- Read the mortgage display name from the dashboard loan card's `c-info-box__account-label`, while keeping `Crédit immobilier` only as a final fallback.
- Do not reject a valid mortgage when its optional display label cannot be extracted, provided its reference and outstanding capital are valid.

## 2.17.28

- Parse the BoursoBank mortgage name from the dedicated `c-product-title__label` element, with the account edit-label parser retained as a fallback.

## 2.17.27

- Add a privacy-safe mortgage page diagnostic showing which required fields and relevant structural classes are present when parsing fails.

## 2.17.26

- Temporarily log the complete parsed business payload for every BoursoBank, aggregated external and loan account in the Home Assistant add-on journal for connector diagnostics.
- Authentication secrets, cookies and session material are not included in these account-detail log entries.

## 2.17.25

- Scope BoursoBank mortgage label extraction to the account edit-label container so unrelated accessibility text cannot become the account name.

## 2.17.24

- Fix the BoursoBank mortgage parser runtime failure by importing the shared text sanitizer used for the mortgage label.

## 2.17.23

- Import BoursoBank mortgage detail pages as internal LOAN accounts.
- Use the outstanding principal as a negative balance and keep mortgage transaction sync disabled.
- Derive a stable opaque external ID from the mortgage reference without logging the reference, URL, label, balance, or raw HTML.

## 2.17.22

- Add privacy-safe BoursoBank mortgage-link diagnostics for credit immobilier pages that are outside the classic account-card route.
- Report only mortgage-link counts and path-depth shapes; never URLs, identifiers, labels, balances, or raw HTML.

## 2.17.21

- Extend privacy-safe BoursoBank loan diagnostics to count all loan account hrefs and how many do not match the currently supported 32-hex account identifier shape.
- No account URLs, identifiers, labels, balances, or raw HTML are logged.

## 2.17.20

- Fix BoursoBank loan diagnostics by using a public privacy-safe parser diagnostic helper instead of calling the private `_loan_cards` symbol from `main.py`.
- Keep loan diagnostics anonymized while reporting parsed loan count, returned loan-ID count, and distinct parsed field-set count.
- Make the loan DOM parser ignore HTML void elements so its stack cannot drift and associate fields with the wrong credit card.

# Changelog

## 2.17.19

- N’accepte une carte crédit DOM que lorsqu’elle correspond à un seul ID de compte et ajoute des compteurs de diagnostic anonymisés.


## 2.17.18

- Classe les comptes de la section crédit BoursoBank comme crédits internes même lorsque leur sous-libellé décrit le financement plutôt que la banque.


## 2.17.17

- Remplace le découpage regex des crédits par un parseur HTML structurel associant ID, solde, libellé et banque au plus petit ancêtre commun.


## 2.17.16

- Ajoute un diagnostic structurel anonymisé autour de chacune des cartes crédit BoursoBank.


## 2.17.15

- Corrige la détection du conteneur exact des cartes crédit BoursoBank sans confondre les sous-classes balance/label.


## 2.17.14

- Isole chaque crédit dans son conteneur de compte BoursoBank et supprime tout contenu financier du diagnostic journalisé.


## 2.17.13

- Parse les crédits BoursoBank carte par carte afin de gérer les multiples blocs de solde présents dans la section crédit.


## 2.17.12

- Écrit le diagnostic anonymisé des cartes crédit dans les logs avant validation du dashboard.


## 2.17.11

- Rend le diagnostic des crédits accessible même lorsque le parseur principal refuse des cartes BoursoBank.


## 2.17.10

- Corrige l’anonymisation du diagnostic BoursoBank et ajoute les compteurs structurels nécessaires pour les variantes de cartes crédit.


## 2.17.9

- Détecte les crédits BoursoBank dont l’encours est affiché directement dans la carte, sans libellé « Solde : ».


## 2.17.8

- Affiche automatiquement le diagnostic anonymisé de structure des crédits BoursoBank dans l’interface locale après connexion.

- Ajoute un diagnostic anonymisé des formats date/montant et de la structure de la ligne BoursoBank en échec.

# Changelog

## 2.17.7

- Corrige définitivement le retour JSON Python du diagnostic anonymisé des crédits BoursoBank.


## 2.17.6

- Corrige la syntaxe du diagnostic anonymisé des cartes de crédit BoursoBank introduit en 2.17.5.


## 2.17.5

- Ajoute un diagnostic local anonymisé de la structure des cartes de crédit BoursoBank afin de supporter leur affichage sans exposer de données financières.


## 2.17.4

- Affiche dans l’interface locale les crédits BoursoBank et les comptes externes agrégés.
- Indique la banque source et distingue les comptes visibles des comptes dont l’historique est synchronisable.
- Conserve la synchronisation individuelle pour les comptes courants et d’épargne BoursoBank supportés.


## 2.17.3

- Supprime les séquences de nouvelle ligne échappées restées littéralement dans la source C# et rétablit la compilation.


## 2.17.2

- Corrige la compilation du parseur de montants BoursoBank ajouté en 2.17.1.


## 2.17.1

- Corrige la synchronisation individuelle BoursoBank lorsque `amountEur` est sérialisé comme chaîne décimale par le connecteur Python.


## 2.17.0

- Affiche les comptes BoursoBank dans l’interface locale Home Assistant.
- Permet d’associer chaque compte BoursoBank à un compte GlitteringPrizes existant puis de le synchroniser individuellement.
- Importe jusqu’à 120 jours d’opérations comptabilisées et ignore les autorisations en attente.
- Évite les doublons déjà présents sur le compte cible par date et montant, puis utilise un `ImportKey` Bourso stable pour les synchronisations suivantes.
- Aucun changement du frontend Vercel.


## 2.16.25

- Corrige l’échappement de la regex de date française BoursoBank (`3 octobre 2026`).


## 2.16.24

- Corrige la profondeur du parseur HTML des opérations BoursoBank en tenant compte des éléments HTML vides comme `input`.
- Limite la capture du montant et du libellé à leur élément respectif.


## 2.16.23

- Utilise réellement `HTMLParser` pour associer les en-têtes de date, montants et libellés des opérations BoursoBank, sans dépendre de l’ordre des classes HTML.


## 2.16.22

- Corrige le `NameError` du diagnostic d’historique en rendant `_shape_text` accessible au parseur.


## 2.16.20

- Corrige l’échappement de la regex des lignes d’opérations BoursoBank qui empêchait tout `<li>` d’être reconnu.
- Retire la trace structurelle temporaire devenue inutile.


## 2.16.19

- Adapte le parseur aux vrais séparateurs de date vides et aux lignes d’opérations observées chez BoursoBank.


## 2.16.18

- Ajoute une trace structurelle HTML limitée aux balises/classes autour d’une opération BoursoBank, sans contenu financier.


## 2.16.17

- Publie le parseur structurel des dates BoursoBank et fiabilise le workflow de publication du backend.


## 2.16.16

- Corrige l’association des séparateurs de date aux opérations BoursoBank et importe explicitement le parseur de montants.


## 2.16.16

- Restaure effectivement le diagnostic structurel des lignes BoursoBank incomplètes dans l’image publiée.


## 2.16.15

- Republie le diagnostic structurel des lignes d’opérations BoursoBank avec le workflow de publication corrigé.


## 2.16.14

- Ajoute un diagnostic structurel sûr pour identifier les lignes BoursoBank incomplètes sans exposer les données bancaires.


## 2.16.13

- Corrige le parseur de dates BoursoBank : les séparateurs décoratifs ne sont plus interprétés comme des dates.


## 2.16.12

- Ajoute une prévisualisation en lecture seule des opérations BoursoBank comptabilisées, sans écriture en base ni exposition des libellés/montants.


## 2.16.11

- Ajoute les formes anonymisées des dates/montants et le schéma interne des lignes d’opérations BoursoBank.


## 2.16.10

- Étend le diagnostic anonymisé pour identifier les attributs structurels des lignes d’opérations BoursoBank.


## 2.16.9

- Ajoute un diagnostic local, en lecture seule et anonymisé, pour identifier la structure actuelle de l’historique BoursoBank.


## 2.16.8

- Corrige le Dockerfile et publie une image ARM64 propre contenant le correctif du parseur BoursoBank.


## 2.16.7

- Republie le correctif BoursoBank dans une nouvelle image ARM64 GHCR vérifiable.


## 2.16.6

- Force une reconstruction propre du parseur BoursoBank et vérifie ses symboles pendant le build Docker.
- Republie explicitement l’image ARM64 2.16.6 sur GHCR après l’échec du premier build.


## 2.16.5

- Corrige le parsing des cartes de comptes BoursoBank lorsque les sections contiennent des éléments HTML imbriqués.
- Conserve le contrôle strict de complétude avant import.


## 2.16.4

- Sert l’interface Bourso directement à la racine Ingress et supprime le point d’entrée personnalisé qui produisait un double slash.


## 2.16.3

- Corrige le point d’entrée et l’identification utilisateur Home Assistant Ingress.
- Restreint l’interface Bourso à l’adresse Supervisor Ingress 172.30.32.2.


## 2.16.2

- Publie l’interface BoursoBank locale Ingress après validation de compilation.


## 2.16.1

- Corrige la compilation de l’interface locale Home Assistant Ingress.


## 2.16.0

- Ajoute une interface BoursoBank locale via Home Assistant Ingress.
- Les identifiants bancaires ne transitent plus par Vercel.
- Protège les actions locales par contexte Ingress et jeton CSRF HttpOnly.


## 2.15.2

- Corrige le démarrage du connecteur BoursoBank après le durcissement des sessions.
- Ajoute un smoke test Python au build Docker pour empêcher la publication d’un connecteur non importable.


## 2.15.1

- Corrige le packaging ARM64 des dépendances Python figées du connecteur BoursoBank.


## 2.15.0

- Durcissement BoursoBank : cookies conservés uniquement dans le connecteur local et jetons opaques temporaires.
- Authentification bancaire interdite via Vercel et réservée au chemin local.
- Validation stricte des hôtes HTTPS BoursoBank et dépendances Python figées.


## 2.14.1

- Sécurise toutes les routes BoursoBank par session administrateur.
- Ajoute l’import des comptes et soldes BoursoBank dans GlitteringPrizes.


## 2.14.0

- Ajout des endpoints REST administrateur BoursoBank (`login`, validation 2FA, comptes, health).
- Le connecteur Bourso reste isolé derrière une URL locale configurable `bourso_auth_url`; les identifiants bancaires ne sont ni journalisés ni persistés par GlitteringPrizes.


## 2.13.3

- Correction du module ES `actual-sync.mjs` : le mode de liste des comptes s'exécute désormais dans une fonction asynchrone, ce qui rend valide la sortie anticipée et supprime l'erreur `Illegal return statement` sous Node.js.

## 2.13.2

- La liste de synchronisation individuelle reste pilotée par Actual Budget, indépendamment des associations déjà présentes dans GlitteringPrizes.
- Les métadonnées ActualQL `account_sync_source` sont utilisées pour ne proposer que les comptes réellement reliés à un fournisseur de synchronisation bancaire (dont Enable Banking), au lieu d'inclure les comptes purement manuels.
- La réponse indique aussi, sans en faire un critère d'inclusion, si chaque compte Actual possède déjà une correspondance GlitteringPrizes via `ExternalId = actual:<ActualAccountId>`.
- La synchronisation individuelle continue d'utiliser l'identifiant du compte Actual pour appeler `runBankSync({ accountId })`.

## 2.13.1

- La liste de synchronisation individuelle est désormais chargée directement depuis Actual Budget au lieu de dépendre des comptes déjà associés dans GlitteringPrizes.
- Tous les comptes Actual ouverts sont proposés, y compris ceux qui n'ont pas encore été importés ou associés dans GlitteringPrizes.
- Le chargement de cette liste n'exécute aucune synchronisation bancaire et ne récupère pas l'historique des transactions.

## 2.13.0

- Ajout de la synchronisation bancaire individuelle par compte Actual Budget / Enable Banking.
- Un compte peut désormais déclencher seul `runBankSync`, puis seuls ses transactions et son solde sont importés dans GlitteringPrizes.
- Ajout d’un endpoint administrateur listant les comptes liés à Actual pour alimenter les commandes de synchronisation individuelle.

## 2.12.9

- Ajout d’un historique normalisé des synchronisations avec `ActualSyncRuns` et `ActualSyncTransactionChanges`.
- Chaque synchronisation enregistre explicitement les opérations `NEW` ou `UPDATED`, avec ancien/nouveau montant et ancienne/nouvelle date.
- Migration SQLite strictement additive : aucune table, transaction, entrée d’audit ou ancien snapshot n’est supprimé ou réécrit.
- Les anciens `ActualSyncSnapshots` restent conservés et lisibles en compatibilité ; les nouvelles synchronisations utilisent en priorité l’historique normalisé.

## 2.12.8

- Le détail d’une synchronisation ne considère plus les rafraîchissements de métadonnées Actual (libellé, catégorie, référence) comme des opérations modifiées.
- Une opération existante apparaît désormais dans le détail uniquement si son montant, sa date ou son compte a réellement changé ; les nouvelles opérations restent affichées.

## 2.12.7

- Le snapshot d’une synchronisation Actual Budget ne conserve désormais que les transactions réellement ajoutées ou modifiées pendant cette synchronisation.
- Les anciennes synchronisations sans snapshot ne sont plus reconstruites depuis l’état courant de la base, afin de ne pas attribuer de fausses modifications à une synchronisation historique.

## 2.12.6

- Le détail d’un compte expose la date de la dernière synchronisation Actual Budget réussie.
- La recherche de la dernière synchronisation reste compatible SQLite : aucune opération SQL de tri sur `DateTimeOffset`.

## 2.12.5

- Ajout d’un diagnostic serveur détaillé sur le chargement des soldes initiaux afin d’identifier précisément les erreurs SQLite ou de schéma restantes.

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
