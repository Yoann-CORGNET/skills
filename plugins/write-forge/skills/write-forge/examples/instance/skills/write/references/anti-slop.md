---
id: anti-slop
langue: "{{CODE_LANGUE}}"
non-surchargeable:
  - attribution-vague
  - consensus-abusif
  - source-non-verifiable
  - puffery-importance
---

<!-- gabarit: le « Plancher transposable » se livre tel quel, sans retouche. Seule l'« Annexe de
     langue » se remplit, et elle se remplit par langue cible, pas par personne : deux instances qui
     écrivent dans la même langue partagent la même annexe. -->

# Anti-slop, plancher transverse

Règles pour ne pas produire les marqueurs mécaniques du texte généré par LLM (« AI slop »).
S'applique à **tous** les registres et toutes les postures, comme l'Étape 0.

## Portée

Le plancher porte sur **le texte produit pour un lecteur**. Il ne porte pas sur les fichiers de ce
skill, qui sont de la documentation machine : tableaux, listes de déclarations, identifiants. Cette
distinction est explicite pour éviter la lecture littérale où le skill viole son propre plancher.

## Ce que ces règles sont, et ne sont pas

Ce sont des **tells probabilistes**, pas des preuves d'origine IA : un humain peut en produire
aussi. Le but n'est pas de passer un détecteur (les détecteurs sont peu fiables), mais d'éviter les
tics qui appauvrissent l'écrit. Deux sources fondent ces règles :

- **Kobak, González-Márquez, Horvát & Lause (2025)**, _Delving into LLM-assisted writing in
  biomedical publications through excess vocabulary_, _Science Advances_ 11(27), arXiv:2406.07016.
  Mesure sur 15 M+ d'abstracts PubMed les mots dont la fréquence explose après ChatGPT (≥ 13,5 % des
  abstracts 2024 touchés, jusqu'à 40 % dans certains sous-corpus). Preuve quantitative.
- **Wikipedia : _Signs of AI writing_** (WikiProject AI Cleanup),
  <https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing>. Catalogue descriptif de patterns
  avec exemples cités, tenu par des éditeurs après revue de milliers d'articles.

Le tell le plus mesuré, le vocabulaire en excès, est spécifique à l'anglais biomédical. Les tells
**structurels** du plancher ci-dessous sont transposables d'une langue à l'autre et priment.

## Comment lire ce fichier

Chaque règle porte un `id` stable en kebab-case. Les identifiants sont l'interface du mécanisme de
surcharge : un fichier de registre lève une règle sur son genre en déclarant
`surcharge: [<id>, ...]` dans son frontmatter. Une règle levée sans déclaration est une erreur, pas
un arbitrage.

Par défaut, **toute règle est surchargeable par un registre**. Les exceptions sont listées en
`non-surchargeable` dans le frontmatter de ce fichier : ce sont les quatre règles dont la violation
fait dire au texte plus que ce que la preuve soutient. Elles relèvent de la même invariance que
l'Étape 0, et aucun genre ne les lève.

Renommer une règle casse les surcharges qui la nomment. Un `id` se retire, il ne se renomme pas.

## Plancher transposable

### Lexique

- `lexique-excedentaire` : ne pas employer par défaut les mots mesurés en excès par Kobak et al.
  2025, liste anglaise : _delve, underscore, showcase, intricate, pivotal, tapestry, landscape,
  realm, foster, meticulous, boast, testament to, underscores the importance_. C'est la seule liste
  mesurée ; les analogues dans une autre langue sont en annexe, et ils ne sont pas mesurés.
- `copule-gonflee` : ne pas remplacer le verbe le plus simple par une copule d'apparat quand le
  verbe simple suffit. La liste des copules concernées dépend de la langue, voir l'annexe.
- `variation-elegante` : répéter le mot juste vaut mieux qu'enchaîner trois synonymes pour éviter la
  répétition. La variation forcée brouille la référence.

### Structure de phrase

- `regle-de-trois` : pas de triplet automatique (adjectif, adjectif et adjectif ; concept, concept
  et concept) quand deux éléments, ou un seul précis, suffisent.
- `parallelisme-correctif` : éviter comme figure par défaut les tournures qui posent un terme pour
  le corriger aussitôt (« non seulement X, mais aussi Y » ; « ce n'est pas X, c'est Y » ; la clôture
  d'idée sur un contraste). Les garder pour un contraste réellement voulu, pas comme tic rythmique.
- `burstiness` : varier la longueur des phrases. Une suite de phrases de même longueur et de même
  moule est un tell.

### Emphase et importance

- `puffery-importance` : ne pas gonfler l'importance de ce qu'on décrit (« un moment charnière », «
  marque une étape décisive », « au cœur de »). Décrire, ne pas sacraliser.
- `portee-non-demontree` : pas de proposition en queue de phrase qui affirme une portée sans la
  démontrer (« renforçant ainsi son importance », « soulignant sa pertinence »).
- `ton-promotionnel` : ton descriptif, pas guide touristique ni communiqué de presse.

### Attribution

- `attribution-vague` : bannir « des études suggèrent », « les experts s'accordent », « il est
  largement reconnu » sans référence nommée et vérifiable.
- `consensus-abusif` : une ou deux sources ne font pas un consensus. Ne pas généraliser au-delà de
  ce que la source couvre.
- `source-non-verifiable` : si la source n'est pas vérifiable, ne pas l'invoquer. Cette règle
  recoupe l'Étape 0 et s'appuie sur le verdict de l'agent `fact-checker`.

### Clôture et plan

- `conclusion-formulaire` : pas de conclusion en « malgré ces défis » suivie d'une spéculation sur
  l'avenir plaquée.
- `plan-mecanique` : pas de plan générique appliqué par réflexe (histoire, caractéristiques, défis,
  perspectives, conclusion) quand le sujet appelle un autre découpage. Un plan **imposé par le
  commanditaire** n'est pas visé par cette règle : le registre concerné le déclare en surcharge.
- `resume-de-section` : pas de phrase-résumé qui reprend chaque section à sa fin.

### Matière et méta

- `contexte-nest-pas-matiere` : le fil de discussion mélange la matière destinée au lecteur (faits,
  chiffres, angle, citations) et le pilotage de la rédaction (consignes, corrections, jugements de
  ton, critères d'évaluation, raisonnement suivi). Faire le tri avant d'écrire : seule la matière
  entre dans le texte. Le tri vaut dans les deux sens : un élément n'entre pas dans le texte du seul
  fait qu'il a été discuté, et un fait établi en discussion dont le lecteur a besoin ne peut pas
  rester dans le fil.
- `meta-commentaire` : le texte ne parle pas de lui-même. Ne pas transcrire les notes de travail,
  les consignes reçues ou les conseils de rédaction (« il faut le dire d'emblée, parce que ça fixe
  l'échelle de ce qui suit », « c'est la charnière de la démonstration »). Ne pas reprendre les
  jugements de tonalité donnés en note (« ce n'est pas un reproche »). Test avant livraison : une
  phrase qui parle du texte, de la section, du cahier des charges ou du lecteur plutôt que du sujet
  se supprime. La rédaction pose la tension, elle ne l'annonce pas.
- `etiquettes-glosees` : un paragraphe organisé par étiquettes glosées en tête de segment (« Rapide
  : … Robuste : … Peu coûteux, enfin : … ») se lit comme un plan récité. Écrire une prose qui
  enchaîne les idées plutôt que de les étiqueter.

### Formatage

- `gras-mecanique` : pas de gras sur chaque terme clé ni sur chaque en-tête de liste.
- `liste-entete` : pas de listes « en-tête : texte » systématiques quand une phrase suffit.
- `emphase-tiret` : pas de tiret cadratin réflexif comme signe d'emphase. Préférer une virgule, des
  parenthèses, un deux-points, ou couper la phrase. Ce réflexe est une habitude de modèle, pas une
  convention de langue : la règle reste dans le plancher, dans toutes les langues. Un registre dont
  la convention typographique l'exige la déclare en surcharge.
- `emoji-separateur` : pas d'emoji en puce ni en séparateur.

## Annexe de langue ({{LANGUE}})

Ces trois rubriques dépendent de la langue cible et **pas** de la personne. Elles se re-dérivent
pour chaque nouvelle langue, et se partagent entre toutes les instances qui écrivent dans celle-ci.
Rien ici n'est mesuré : ce sont des analogues raisonnés, à traiter comme tels.

- `analogues-lexicaux` : {{ANALOGUES_LEXICAUX}}
  <!-- gabarit: la liste des tournures d'emphase creuse de la langue cible, de même fonction que la
       liste mesurée en anglais, plus les copules d'apparat visées par `copule-gonflee`. -->
- `casse-des-titres` : {{CASSE_DES_TITRES}}
  <!-- gabarit: la convention de casse des titres dans la langue cible. Ce n'est pas un tell d'IA,
       c'est une norme locale, et c'est pour ça qu'elle vit ici plutôt que dans le plancher. -->
- `adresse-tv` : {{ADRESSE_TV}}
  <!-- gabarit: la langue cible distingue-t-elle une adresse familière d'une adresse déférente ? Si
       oui, dire laquelle sert de défaut et renvoyer à l'axe D d'audience.md, qui porte le choix. Si
       non, l'écrire : « la langue cible ne porte pas cette distinction ». -->

## Angles morts assumés

{{ANGLES_MORTS_ANTI_SLOP}}

<!-- gabarit: ce qui n'a pas été couvert et qu'on sait ne pas avoir couvert. Deux candidats
     récurrents : les tells propres au medium (fil de messagerie, légende d'image) qu'aucune des deux
     sources ne documente, et le fait que les deux sources datent d'avant la génération de modèles
     utilisée aujourd'hui. Écrire « aucun angle mort identifié » est une réponse valable, écrire
     l'emplacement vide ne l'est pas. -->
