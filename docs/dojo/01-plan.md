<!-- Converted from thiga-co/dojo-ai-native-sdlc-from-the-tranches (ai-sdlc.html). MIT License, Copyright (c) 2026 Thiga. -->

# Module 1 · Plan

## Introduction

Définition à connaître avant de commencer

**Play** : pratique concrète recommandée par le playbook pour une phase du cycle. Chaque play décrit ses prérequis, ses étapes et ce qu’il permet de mesurer.

Le playbook AI-Native SDLC d’Anthropic structure le cycle de développement en six phases, de Plan à Maintain. Il propose des plays pour travailler avec un agent au sein de ces phases.

La phase Plan ouvre le cycle en précisant le changement souhaité. Elle repose sur un seul play, *Capture as intent*. Il recommande de consigner l’intention dans `intent.md` avant la conception. Le document décrit ce qui est voulu, pourquoi et sous quelles contraintes. Cette intention peut venir d’une idée, d’un ticket déjà déposé ou d’un incident détecté pendant la phase Maintain. Le Product Owner décide si elle permet d’engager la phase Design.

La phase Plan en détail

| Cycle traditionnel | Cycle AI-native |
| --- | --- |
| Une idée passe par des entrées de backlog, des user stories, des story points et des réunions d’affinage avant que quelqu’un puisse agir. La responsabilité change à chaque transmission. Ce qui parvient à l’équipe de développement est donc éloigné de plusieurs étapes de ce que la personne à l’origine du besoin voulait exprimer. | La personne à l’origine du besoin échange avec Claude et consigne le résultat dans `intent.md`, une première spécification formulée dans ses propres termes. Le document contient ce qui est souhaité, pourquoi et sous quelles contraintes. Les processus récurrents sont encodés dans des skills. |

## Dans ce module

Vous formulerez avec Claude le besoin d’un simulateur Mars Rover qui exécute des commandes de déplacement. Vous le conserverez dans `intent/mars-rover/intent.md` avant de le soumettre à la décision du Product Owner.

Vous prendrez successivement le rôle du Platform Engineer, qui prépare les outils communs, celui de la personne à l’origine du besoin, puis celui du Product Owner, responsable de l’acceptation de l’intention.

## Ce que vous allez faire

1. **Créer un repository GitHub**

   Prendre le rôle du Platform Engineer et créer le repository `mars-rover` pour conserver et partager les documents de cadrage du besoin.
2. **Ouvrir une session**

   Prendre le rôle du Platform Engineer et préparer une session Claude Code reliée au repository `mars-rover` pour permettre la rédaction de l’intention.
3. **Équiper le harness**

   Prendre le rôle du Platform Engineer et ajouter la skill `intent` pour donner à Claude la méthode de formulation et de rédaction du besoin.
4. **Rédiger l'intention**

   Prendre le rôle de la personne à l’origine du besoin et préciser avec Claude l’intention du simulateur dans `intent.md` pour la soumettre au Product Owner à la fin de la phase Plan.
5. **Accepter l'intention**

   Prendre le rôle du Product Owner et décider si l’intention du simulateur permet de terminer la phase Plan et d’engager la conception dans la phase Design.

---

## Créer un repository GitHub

Définitions à connaître avant de commencer

**Repository** : espace qui rassemble les fichiers d’un projet.

**Git** : outil qui conserve les versions successives de ces fichiers.

**Commit** : enregistrement dans Git d’un ensemble de changements avec un auteur et une date.

**GitHub** : service en ligne qui héberge le repository pour que l’équipe puisse partager les fichiers et relire leur historique.

**Branche** : version de travail du projet où préparer des changements sans modifier la branche principale, appelée `main`.

Le projet Mars Rover a besoin d’un espace partagé pour conserver ses documents, son code et ses tests. Vous prenez le rôle du Platform Engineer.

Le play *Capture as intent* du playbook recommande de conserver les intentions dans un espace versionné suivi par le Product Owner. Sa préparation est une tâche ponctuelle de l’équipe technique, qui crée cet espace et décide qui peut y écrire, car les contributeurs viennent de toute l’organisation. L’historique permet ensuite de retrouver les versions des documents et les décisions prises.

Dans ce dojo, le repository `mars-rover` sur GitHub accueillera les documents de cadrage du besoin, puis le code et les tests du simulateur. Vous travaillez depuis votre navigateur, sans rien installer sur votre ordinateur.

Passons à la pratique

## À vous de jouer

Objectif

Prendre le rôle du Platform Engineer et créer le repository `mars-rover` pour conserver et partager les documents de cadrage du besoin.

01

### Créez votre compte GitHub.

Prenez le rôle du Platform Engineer. Si vous n’avez pas de compte, ouvrez [github.com/signup](https://github.com/signup). Remplissez le formulaire, puis cliquez sur Create account.

Suivez les vérifications demandées par GitHub, puis validez votre adresse avec l’e-mail reçu. Poursuivez avec « Créez le repository `mars-rover` ».

GitHubgithub.com/signup

02

### Connectez-vous à votre compte GitHub.

Si vous avez déjà un compte, ouvrez [github.com/login](https://github.com/login). Connectez-vous avec votre méthode habituelle. Poursuivez avec « Créez le repository `mars-rover` ».

GitHubgithub.com/login

03

### Créez le repository `mars-rover`.

Ouvrez [github.com/new](https://github.com/new). Remplissez le formulaire avec les paramètres indiqués ci-dessous, puis cliquez sur Create repository.

GitHubgithub.com/new

04

### Vérifiez le repository créé.

Le repository `mars-rover` doit être privé, sur la branche `main`, avec les fichiers `.gitignore`, `LICENSE` et `README.md`.

GitHubgithub.com/VOTRE-COMPTE/mars-rover

Application en entreprise

L’espace versionné peut prendre plusieurs formes. Un dossier `intent/` dans le repository garde ces documents près du code. Lorsque les besoins concernent plusieurs repositories, une équipe peut choisir un repository d’intentions séparé. Si les projets sont déjà réunis dans un même repository, un dossier suffit.

---

## Ouvrir une session

Définitions à connaître avant de commencer

**Session** : conversation avec Claude Code consacrée à une tâche. Elle contient vos demandes et les réponses de Claude.

**Environnement** : espace de travail de Claude Code où Claude peut lire et modifier les fichiers et exécuter des commandes. Il peut se trouver sur votre ordinateur ou sur un serveur distant.

Le repository `mars-rover` est disponible sur GitHub et Claude n’y a pas encore accès. Vous reprenez le rôle du Platform Engineer.

Le play *Capture as intent* du playbook recommande de permettre aux contributeurs non techniques d’enregistrer leurs intentions sans manipuler Git eux-mêmes. Il propose de relier Claude à l’espace partagé pour qu’il y enregistre les documents à leur demande, depuis claude.ai ou Cowork. Les contributeurs relisent les propositions avant leur enregistrement.

Dans ce dojo, l’environnement `Mars Rover` reliera Claude Code au repository. Pour simplifier le parcours, Claude Code sert aussi bien aux documents qu’au code du simulateur. Une session permet de formuler une demande, d’examiner le résultat et de demander les corrections nécessaires.

Passons à la pratique

## À vous de jouer

Objectif

Prendre le rôle du Platform Engineer et préparer une session Claude Code reliée au repository `mars-rover` pour permettre la rédaction de l’intention.

01

### Connectez-vous à Claude.

Toujours dans le rôle du Platform Engineer, ouvrez [claude.ai/login](https://claude.ai/login). Utilisez la connexion par e-mail et saisissez l’adresse du compte Claude prévu pour l’atelier. Validez l’envoi du lien.

Claudeclaude.ai/login

02

### Validez votre connexion à Claude.

Dans votre messagerie, ouvrez le message Votre lien sécurisé vers Claude.ai est ici envoyé par Anthropic. Cliquez sur Se connecter.

Messagerie

Si le lien affiche un code, revenez dans l’onglet Claude. Cliquez sur Saisissez le code de vérification, recopiez le code et cliquez sur Vérifier l’adresse e-mail.

03

### Ouvrez Claude Code.

Cliquez sur l’icône Code en haut de la barre latérale.

Claudeclaude.ai/new

04

### Connectez Claude Code à GitHub.

Sur son premier écran, Claude Code vous demande de connecter votre compte GitHub. Cliquez sur Se connecter à GitHub.

Claude Codeclaude.ai/code/onboarding

05

### Autorisez Claude à accéder à GitHub.

Cliquez sur Authorize Claude.

GitHubgithub.com/login/oauth/authorize

06

### Créez l’environnement `Mars Rover`.

Dans le formulaire Créez votre premier environnement cloud, remplacez le nom prérempli par `Mars Rover`. Gardez l’option De confiance sélectionnée pour permettre à Claude de télécharger les paquets depuis des sources vérifiées. Cliquez sur Créer & terminer.

Claude Codeclaude.ai/code/onboarding

07

### Sélectionnez le repository `mars-rover`.

Ouvrez Sélectionner un dépôt… au-dessus du champ de message. Saisissez `mars-rover` dans la recherche, puis cliquez sur le repository.

Claude Codeclaude.ai/code

08

### Vérifiez la configuration de Claude Code.

L’environnement `Mars Rover`, le repository `mars-rover` et la branche `main` doivent apparaître au-dessus du champ de message.

Claude Codeclaude.ai/code

---

## Équiper le harness

Définitions à connaître avant de commencer

**Skill** : méthode de travail écrite pour Claude, réutilisable d’une session à l’autre. Son fichier `SKILL.md` précise quand l’utiliser, les étapes à suivre et les règles à respecter pour accomplir un type de tâche.

**Harness** : environnement logiciel qui donne à un modèle les outils et les instructions pour agir sur un projet. Claude Code est un harness. Il permet à Claude de lire et modifier les fichiers, d’exécuter des commandes et d’utiliser des skills.

**Plugin** : ensemble de skills et d’outils regroupés pour être distribués et installés ensemble.

Le repository est créé et Claude Code peut y travailler. Vous reprenez le rôle du Platform Engineer.

Le play *Capture as intent* du playbook recommande de traduire le template d’intention de l’organisation en une skill réutilisable. Pour une tâche récurrente, on privilégie une skill à un long prompt car elle conserve la méthode et les règles de l’équipe. Ces instructions peuvent être partagées, mises à jour et réutilisées d’une session à l’autre sans les recopier à chaque demande. Un membre de l’équipe technique prépare ces instructions, puis un responsable les valide.

Dans ce dojo, la skill `intent` rejoindra le repository `mars-rover`. Elle précisera les questions à poser, les rubriques de `intent.md` et les moments où Claude doit attendre la validation de l’auteur.

Passons à la pratique

## À vous de jouer

Objectif

Prendre le rôle du Platform Engineer et ajouter la skill `intent` pour donner à Claude la méthode de formulation et de rédaction du besoin.

01

### Ajoutez la skill `intent`.

Toujours dans le rôle du Platform Engineer, envoyez ce prompt dans la session préparée pour Mars Rover.

`Crée le fichier .claude/skills/intent/SKILL.md avec exactement``le contenu ci-dessous. Ne modifie aucun autre fichier.``Commit uniquement ce fichier sur main avec le message « Ajoute la skill intent »,``puis push ce commit sur main vers GitHub. Ne lance pas la skill.`````` ````md ``````---``name: intent``description: Aide à préciser un besoin et rédige intent.md après validation du brouillon. À utiliser pour formaliser ou mettre à jour l’intention d’un produit avant sa conception.``---``# Intent``Transforme une idée en intention structurée, sans décider à la place de son auteur.``## Règles``` - Le document se trouve toujours dans `intent/<slug>/intent.md`. Si le slug `` `n'est pas fourni, demande-le avant de commencer.``- Ne prends aucune décision produit à la place de l'auteur et n'invente aucune` `contrainte ni solution technique.``` - Conserve tout point non tranché dans `Questions ouvertes`. ```- Utilise les informations d'auteur fournies dans la demande ou présentes dans` `` le document. Si elles manquent, indique `Auteur : non renseigné.`. ```- Attends une validation explicite du brouillon avant de créer ou de modifier` `le fichier.``- Cette validation autorise la création d'une branche de travail et l'écriture` `du fichier sur cette branche. L'intention sera acceptée plus tard par le` `Product Owner lors du merge de sa pull request.``- Ne développe pas le produit. Sans confirmation de la création de la pull` `request, ne commit rien, ne push rien et n'ouvre aucune pull request.` `Après confirmation, limite ces opérations au fichier d'intention concerné.``## Préciser le besoin``` Si `intent/<slug>/intent.md` existe, lis-le avant de poser tes questions et ```préserve les décisions et les informations qui ne sont pas remises en cause.``Reformule le besoin, puis pose une question à la fois pour préciser le problème,``le résultat recherché, les utilisateurs et systèmes concernés et les contraintes.``Si la personne demande le brouillon ou n'a plus d'information, arrête les``` questions et conserve les inconnues dans `Questions ouvertes`. ```Si la demande fournit déjà le problème, le résultat recherché, le slug et``l'auteur, par exemple un diagnostic accepté, passe directement au brouillon``sans poser de questions.``## Proposer le brouillon``Présente le brouillon dans la conversation avec ce modèle.``# Intent : [titre]``Auteur : [nom] ([rôle]).``## Problème``## Résultat proposé``## Utilisateurs et systèmes concernés``## Contraintes``## Questions ouvertes``Présente un nouveau brouillon après chaque correction, jusqu'à sa validation.``## Enregistrer le contenu validé``Après validation, crée une nouvelle branche de travail depuis la branche``` courante et place-toi dessus avant toute écriture dans `intent/`. Utilise un ```` nom disponible sous `claude/intent-<slug>` et respecte les contraintes de ```nommage de l'environnement. Si la création ou le changement de branche``échoue, arrête-toi sans écrire le fichier et explique le problème.``` Sur cette branche, crée ou mets à jour `intent/<slug>/intent.md`. ```Affiche le nom de la branche, le chemin et le contenu complet du fichier.``` Propose ensuite de créer une pull request vers `main` pour soumettre ```l'intention au Product Owner. Précise que cette demande permettra de relire``le document avant de décider de son passage à la phase Design. Attends une``confirmation avant toute opération de commit, de push ou de création de``pull request. Ne merge jamais la pull request.`````` ```` `````

Cliquez sur les trois points en haut à droite de la session, puis sur Fichiers. Dans le panneau Fichiers, ouvrez `.claude/skills/intent/SKILL.md` et vérifiez que son contenu reprend le texte du prompt.

02

### Lancez `/reload-skills`.

Envoyez `/reload-skills` dans la session Claude Code pour recharger les skills du repository.

Claude Codeclaude.ai/code

03

### Recherchez `/intent`.

Saisissez `/intent` dans la zone de message sans l’envoyer. Le menu de commandes doit proposer la skill `intent`.

Claude Codeclaude.ai/code

La suggestion `intent` confirme que Claude Code reconnaît la skill.

Application en entreprise

Le dojo conserve la skill dans le repository du simulateur. Une organisation peut aussi distribuer les mêmes skills à plusieurs équipes avec un plugin. Le play *Skills as institutional knowledge* du playbook prévoit cette possibilité. L’organisation centralise la maintenance des instructions et l’approbation de leurs mises à jour.

---

## Rédiger l'intention

Définitions à connaître avant de commencer

**Pull request (PR)** : proposition d’intégrer les changements d’une branche dans une autre. Elle permet d’examiner les fichiers modifiés et de discuter des corrections avant leur intégration.

**Markdown** : format de texte qui permet de structurer un document avec des titres, des listes et des liens.

L’espace de travail et la skill `intent` sont prêts. L’équipe Mars Rover veut un simulateur qui interprète des commandes de déplacement sur une carte et affiche la position et la direction finales du rover. Vous prenez le rôle de la personne à l’origine du besoin.

Le play *Capture as intent* du playbook recommande que l’auteur exprime son besoin avec ses propres mots, sans langage formel. Il décrit ce qu’il ne peut pas faire aujourd’hui, les personnes concernées, le résultat souhaité et ce qui est hors périmètre. Claude pose les questions qu’un analyste poserait, sur le périmètre, les utilisateurs, les contraintes et ce qui définit la réussite, jusqu’à rendre l’idée concrète. Il rédige ensuite une première description structurée du besoin, la proto-spec du playbook, selon le template de l’organisation. Ce template couvre le problème, le résultat proposé, les utilisateurs et systèmes concernés, les contraintes et les questions ouvertes. Son en-tête porte l’auteur. L’auteur corrige ce que Claude a mal compris avant de soumettre l’intention au Product Owner. Le document est lisible par une personne et directement exploitable par la phase suivante.

Dans ce dojo, `intent/mars-rover/intent.md` décrira ce besoin selon ces rubriques. Le fichier est rédigé en Markdown et proposé au Product Owner dans une PR depuis une branche de travail. L’intention reste une proposition jusqu’à sa décision d’acceptation.

Passons à la pratique

## À vous de jouer

Objectif

Prendre le rôle de la personne à l’origine du besoin et préciser avec Claude l’intention du simulateur dans `intent.md` pour la soumettre au Product Owner à la fin de la phase Plan.

01

### Ouvrez une nouvelle session Claude Code.

Prenez le rôle de la personne à l’origine du besoin. Cliquez sur Nouveau dans la barre latérale. La nouvelle session doit utiliser l’environnement `Mars Rover`, le repository `mars-rover` et la branche `main`.

Claude Codeclaude.ai/code

02

### Présentez le besoin à Claude.

Lancez la skill `intent` avec le besoin ci-dessous.

`/intent Je fais partie de l'équipe qui construit Mars Rover. Nous devons``développer un simulateur qui reçoit un point de départ, une carte et une``liste de commandes. Il interprète les commandes et affiche la position et la``direction finales du rover.`

La skill suit sa méthode et vous interroge sur le besoin avant d’écrire quoi que ce soit.

03

### Répondez aux questions de Claude.

Claude pose ses questions une par une. Répondez-y à partir des contraintes ci-dessous, puis relisez le brouillon. Demandez les corrections nécessaires jusqu’à ce que son contenu corresponde à l’intention.

Contraintes du simulateur

- Le simulateur reçoit un point (x, y), une orientation N, S, E ou W, une carte qui place les obstacles et une liste de commandes.
- Le rover peut avancer ou tourner de 90 degrés à droite ou à gauche.
- Il reste immobile lorsqu’un obstacle bloque son avancée.
- La carte peut employer les symboles 🟩 et 🌳 ou les symboles 🟫 et 🪨.

Claude Codeclaude.ai/code

04

### Créez le fichier.

Claude vous demande si vous voulez enregistrer le brouillon. Confirmez l’enregistrement dans la conversation. La skill crée d’abord une branche de travail, puis y écrit `intent/mars-rover/intent.md`. Claude s’arrête avant le commit et attend votre confirmation.

Claude Codeclaude.ai/code

05

### Proposez l'intention.

Lorsque le contenu vous convient, répondez « Crée la PR » dans la conversation. Claude fait le commit du fichier et le push de la branche, puis affiche le numéro de la pull request soumise au Product Owner.

Claude Codeclaude.ai/code

Application en entreprise

Le repository ne remplace pas nécessairement Jira ou un outil de gestion des exigences. Le play *Claude Code plan mode as the default starting point* du playbook décrit trois configurations lorsqu’un outil existant tient déjà le registre, Jira, ServiceNow, un outil d’exigences ou Figma. Ces systèmes sont difficiles à remplacer, car les auditeurs et les régulateurs les acceptent déjà.

Le repository peut être la référence, et l’autre outil pointe alors vers le commit. L’outil existant peut rester la référence, et Claude lit alors l’enregistrement en début de session puis y reporte le résultat par un connecteur, un moyen de relier l’agent à un outil. Le lien réciproque est le minimum, les fichiers portent l’identifiant de l’enregistrement et l’outil conserve l’identifiant du commit. Pour chaque artefact, une seule référence est nommée.

Le dojo prend les fichiers du repository `mars-rover` comme référence pour l’intention. Aucune connexion à Jira n’est nécessaire.

---

## Accepter l'intention

Définition à connaître avant de commencer

**Merge** : intégration des changements d’une branche dans une autre.

L’intention du simulateur est rédigée et proposée dans une pull request vers `main`. Vous prenez le rôle du Product Owner.

Le play *Capture as intent* du playbook confie cette décision au Product Owner. Celui-ci relit le besoin, les contraintes et les questions ouvertes, puis demande une correction, refuse la proposition ou l’accepte. Les points qui empêchent de comprendre le besoin doivent être précisés avant de poursuivre. Le commit conserve l’intention, son auteur et sa date dans l’historique. L’acceptation est enregistrée par le merge, le refus par la clôture de la review. Cette trace permet de retrouver plus tard qui a demandé quoi et qui l’a accepté.

Dans ce dojo, la PR rassemble `intent.md`, son résumé et les échanges de review. Le brouillon committé sur sa branche reste distinct de son acceptation par merge dans `main`. Le merge enregistrera l’acceptation de l’intention et la rendra disponible pour la phase Design. Les questions qui peuvent attendre la conception restent visibles dans le document.

Passons à la pratique

## À vous de jouer

Objectif

Prendre le rôle du Product Owner et décider si l’intention du simulateur permet de terminer la phase Plan et d’engager la conception dans la phase Design.

01

### Ouvrez la pull request dans GitHub.

Prenez le rôle du Product Owner pour examiner l’intention proposée. Cliquez sur le numéro de la pull request affiché par Claude. GitHub affiche la page de la pull request.

GitHubgithub.com/VOTRE-COMPTE/mars-rover/pull/…

02

### Examinez l’intention proposée.

Ouvrez l’onglet Files changed pour lire `intent/mars-rover/intent.md` tel qu’il est proposé. Vérifiez que le problème et le résultat proposé correspondent au besoin du simulateur, que les contraintes du simulateur sont reprises, et que le résumé désigne ce fichier comme seul document soumis. Les questions ouvertes doivent être compréhensibles et ne pas bloquer la conception.

Repérez les points à corriger pour les reprendre avec Claude.

03

### Acceptez l'intention.

Décidez si l’intention permet d’engager la conception. Si vous demandez des corrections, revenez dans la session Claude Code, demandez-les et demandez à Claude de mettre à jour la même pull request, puis examinez-la de nouveau.

Lorsque vous acceptez l’intention, revenez dans l’onglet Conversation. Descendez jusqu’au bouton Merge pull request, cliquez dessus, puis confirmez avec Confirm merge. Ce merge enregistre la décision du Product Owner et rend l’intention disponible dans `main` pour la phase Design.

GitHubgithub.com/VOTRE-COMPTE/mars-rover/pull/…

Application en entreprise

Le play ne situe pas la relecture du Product Owner au même moment selon ses rubriques. Son ouverture la demande avant le commit. Ses étapes font corriger le brouillon par son auteur, puis committer `intent.md` dans l’espace partagé, où le Product Owner le reprend. Sa gouvernance enregistre l’acceptation par le merge ou par la clôture de la review, donc après le commit.

Le dojo suit les étapes et la gouvernance. L’auteur corrige le brouillon avec Claude, qui committe l’intention sur une branche de travail. La pull request porte le document relu par le Product Owner, et le merge enregistre son acceptation.
