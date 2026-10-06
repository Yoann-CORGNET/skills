# Contrats d'interface — registre et audience

Fichier de référence de `write-forge`. Il fixe ce qu'un fichier de registre et ce qu'un fichier
d'audience doivent déclarer pour qu'une instance générée s'articule sans pointeur mort ni
contradiction silencieuse. Il fixe le contrat des deux couches, pas leur contenu. Le Registre et
l'Audience sont universels : ils se livrent complets dans le gabarit, comme `anti-slop.md`, et ne
s'extraient pas de la personne. Reste propre à l'instance le choix d'accepter ou de décliner un
registre, et les écarts qu'elle déclare par le mécanisme `surcharge`. Le gabarit de dossier livré
avec ce méta-skill (`examples/instance/skills/write/references/`) montre la forme attendue ; ce
fichier en est la spécification qui fait foi en cas d'écart entre les deux.

## Pourquoi un contrat séparé

Le Registre et l'Audience sont les deux couches d'entrée du modèle à quatre couches : elles
reçoivent ce que la situation impose plutôt que d'exprimer une préférence de la personne. Elles
n'ont donc pas de protocole d'extraction propre, contrairement à la Voix et à la Posture. Ce que ce
méta-skill leur doit, c'est une interface stable : des champs nommés, des conventions de référence,
un format que le validateur d'instance peut vérifier mécaniquement, indépendamment de ce que chaque
instance en retient.

## Contrat d'un fichier de registre

Un fichier sous `references/registres/<id>.md` déclare, en frontmatter YAML :

- `id` — identifiant kebab-case stable. C'est lui, jamais le nom de fichier ni le libellé humain,
  que citent les postures et la table de routage d'audience.
- `norme-empan` — **obligatoire**. Une description de l'empan par défaut de ce genre : longueur
  typique, densité attendue, tolérance à la digression. Sans cette déclaration, la composante Empan
  d'un fichier de voix reste ininscriptible pour ce registre, puisqu'elle s'encode toujours en écart
  relatif à cette norme, jamais en valeur absolue. C'est le seul champ de registre dont l'absence
  bloque une autre couche plutôt que de simplement l'appauvrir.
- `surcharge` — liste optionnelle d'`id` de règles du plancher anti-slop que ce genre lève, par
  exemple un plan imposé par un commanditaire qui rend une règle de plan générique inapplicable. Une
  règle levée sans figurer ici est une contradiction non déclarée entre deux couches, donc une
  erreur, pas un arbitrage silencieux. Les règles marquées `non-surchargeable` dans le fichier
  anti-slop de l'instance ne peuvent jamais y figurer, quel que soit le genre.
- `postures` — liste optionnelle d'`id` de postures que ce registre charge directement, en
  court-circuitant la table de routage d'audience. Un registre qui impose sa propre posture par
  convention de genre, indépendamment de qui écrit à qui, utilise ce champ plutôt que de dupliquer
  une ligne de routage qui ne dépend en réalité pas de l'audience.

Le corps du fichier porte les contraintes dures de forme du genre : longueur, structure ou plan
imposé, conventions typographiques propres au support. C'est la seule couche qui prime sur toutes
les autres dans l'ordre de préséance ; un fichier de registre qui ne porte que des champs de
frontmatter sans ces contraintes n'a pas rempli son rôle.

## Contrat d'un fichier d'audience

Le fichier `references/audience.md` d'une instance porte trois parties, livrées complètes par le
gabarit.

Une définition des trois entrées de contexte réelles, K (écart de connaissance), P (pouvoir) et D
(distance sociale), plus le but, qui route sans être une entrée d'audience puisqu'il est choisi par
le rédacteur et non subi. Aucune de ces définitions ne se reformule en composante de posture : la
règle de nommage du méta-skill l'interdit explicitement, parce que c'est exactement la confusion que
la séparation Audience / Posture sert à éviter.

Une section de contenu, qui distingue l'écart K (relationnel, il route la posture) du niveau absolu
du lecteur (non-initié, dans le domaine, expert, il gouverne vocabulaire, scaffolding et jargon).
Cette section ne route jamais : elle n'ajoute aucune ligne à la table et ne nomme aucune posture.

Une table de routage vers des `id` de posture, avec les contraintes suivantes :

- La table porte une ligne par posture atteignable et une ligne par défaut, qui s'applique dès qu'un
  des trois axes manque au contexte fourni. La ligne par défaut ne s'invente jamais une valeur.
- Chaque cellule de routage s'écrit exactement sous la forme d'une référence `` `posture:<id>` ``
  entre apostrophes inverses, sans texte additionnel dans la même cellule. C'est cette forme précise
  que le mécanisme de vérification d'atteignabilité de l'instance reconnaît ; un nom de posture en
  toutes lettres, même correct, ne suffit pas à établir qu'elle est joignable.
- Une posture définie dans `references/postures/` doit apparaître comme cible d'au moins une ligne
  de routage ici, ou dans le champ `postures` d'au moins un fichier de registre. Une posture qui
  n'apparaît nulle part est du contenu mort : personne ne peut jamais la charger.
- Le poids de l'acte à commettre ne route jamais seul vers une posture : c'est une propriété de
  l'acte à réaliser, pas une entrée d'audience, et la confondre avec P revient à faire porter à une
  entrée de contexte une décision qui appartient à la Posture.

## Ce que ni l'un ni l'autre ne fait

Un fichier de registre ne nomme jamais un trait de voix, même pour l'autoriser : la perméabilité
d'un genre aux marqueurs personnels s'exprime en abstraction (« permissif sur les marqueurs
figuratifs »), jamais en citant le marqueur lui-même, sous peine de produire une ligne morte pour
toute personne qui n'a pas ce trait précis. Un fichier d'audience ne joue jamais une valeur : la
proximité qu'un texte fabrique, la franchise qu'il s'autorise, le territoire de savoir qu'il
revendique restent de la Posture, quelle que soit la tentation de les coder ici pour gagner une
étape.

## Portée de ce fichier

Ce fichier couvre deux contrats, et deux seulement : le fichier de registre et le fichier
d'audience. Les contrats des autres fichiers d'une instance vivent avec leur gabarit. En
particulier, le champ `corroboration`, qui marque si une posture s'appuie sur le corpus, sur un
texte de séance, ou sur les seuls écrans de calibration, est spécifié par le gabarit de posture dans
`examples/instance/skills/write/references/postures/`.
