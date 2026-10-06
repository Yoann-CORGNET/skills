# Audience — gabarit

<!-- gabarit: ce fichier se livre complet et ne s'extrait pas : il ne dépend de la personne ni de
     son corpus. Il fait deux choses : router depuis des entrées de contexte réelles vers un `id`
     de posture, et fixer ce que le niveau du lecteur impose au contenu. La forme du tableau
     (colonnes K, P, D, but, cible), la ligne par défaut et la section sur le contenu se
     conservent telles quelles. Seules bougent à la génération les cibles de routage et le nombre
     de lignes, selon les postures retenues. -->

Quatre entrées de contexte, jamais des valeurs jouées : l'écart de connaissance (K), le pouvoir (P)
et la distance sociale (D) entre qui écrit et qui lit, plus le niveau du lecteur (N). Les trois
premières routent vers une posture, la quatrième gouverne le niveau de contenu. Ce fichier ne
fabrique rien : il constate ce que la situation donne, et route vers la posture par défaut qui en
tient compte. La proximité que le texte fabrique, la franchise qu'il s'autorise, le territoire de
savoir qu'il revendique : tout cela est joué, donc de la Posture, jamais de ce fichier. Un scripteur
qui en sait plus que son lecteur (K haut) peut très bien jouer une posture qui en revendique moins ;
ce fichier constate le premier fait, il ne décide jamais du second.

## Les quatre entrées

- **K, écart de connaissance.** Qui, du scripteur ou du lecteur, en sait le plus sur l'objet du
  texte. Trois valeurs : le scripteur en sait plus, en sait moins, ou le sait à égalité.
- **P, pouvoir.** Qui, du scripteur ou du lecteur, a la capacité de peser sur l'autre,
  indépendamment du sujet du texte : hiérarchie, rôle de décision, rôle d'évaluation.
- **D, distance sociale.** La proximité réelle de la relation, telle qu'elle existe indépendamment
  du texte à produire. Un texte peut fabriquer plus ou moins de proximité que cette distance ne le
  suggère ; c'est la Posture qui en décide, jamais cette entrée.
- **N, niveau du lecteur.** Ce que le lecteur maîtrise du sujet dans l'absolu, indépendamment de ce
  que le scripteur en sait. Trois valeurs : non-initié, dans le domaine, expert. Seule entrée qui ne
  route pas : elle règle le contenu. Voir la section suivante, qui dit pourquoi elle ne se déduit
  pas de K.

Une donnée de plus intervient au routage sans être une entrée d'audience : le **but** que le
rédacteur se fixe pour ce texte précis (obtenir une information, transférer une compréhension, clore
une décision, refuser, déclencher une discussion). Le but n'est pas subi comme K, P et D le sont ;
il est choisi, et une même situation d'audience peut se rédiger avec des buts différents. Une
propriété supplémentaire, le poids de l'acte à commettre (un refus pèse plus qu'une relance), n'est
pas non plus une entrée d'audience : elle ne route jamais seule vers une posture, elle module
seulement la franchise à l'intérieur de la posture retenue.

## Ce que N impose au contenu

<!-- gabarit: section livrée complète, sans cible de routage. Elle n'ajoute aucune ligne au tableau
     ci-dessous et ne nomme aucune posture. -->

Ce fichier a deux rôles : router vers une posture par défaut (tableau plus bas), et fixer le niveau
de contenu, c'est-à-dire le vocabulaire, le scaffolding et le jargon que le lecteur peut recevoir.
Le second rôle ne route jamais : il ne s'écrit pas comme une ligne de la table et ne désigne aucune
posture.

### Deux notions à ne pas confondre

- **L'écart K** est relationnel : il compare le scripteur au lecteur (en sait plus, moins, ou à
  égalité). Il route la posture, et seulement cela.
- **Le niveau du lecteur**, noté N, est absolu : ce que ce lecteur-là maîtrise du sujet, quel que
  soit le scripteur. Trois valeurs : non-initié, dans le domaine, expert. Il gouverne le contenu, et
  seulement cela.

K ne se déduit pas de N, ni N de K. Deux experts entre eux sont à égalité de K, deux novices aussi,
et pourtant le texte ne s'écrit pas pareil : le premier couple supporte le jargon précis, le second
exige des concepts introduits avant d'être employés. À l'inverse, un scripteur qui en sait plus (K
haut) peut s'adresser à un expert comme à un non-initié. N est donc une donnée d'audience à part
entière, posée à côté de K, P et D : comme eux, c'est un fait de la situation, jamais une valeur
jouée. Quand N manque au contexte fourni, ne pas l'inventer : demander, ou à défaut écrire pour le
niveau « dans le domaine » et le dire.

### Les trois niveaux

- **Non-initié.** Aucun prérequis supposé. Introduire un concept avant de l'utiliser. Éviter le
  jargon ; s'il est inévitable, le définir immédiatement, à l'endroit où il apparaît.
- **Dans le domaine.** Les prérequis génériques sont acquis. Le jargon général du domaine passe sans
  définition ; le jargon très spécifique (une sous-spécialité, un outil précis, un acronyme interne)
  s'explicite.
- **Expert.** Le jargon technique précis s'emploie sans reformulation. Aller droit à ce qui
  différencie le propos plutôt que de reposer les bases que le lecteur a déjà.

### Cas particulier de l'enfant

L'enfant n'est pas un quatrième niveau : c'est un sous-cas du non-initié, avec un scaffolding
renforcé. Phrases plus courtes, analogies concrètes, aucune abstraction qui ne soit ancrée dans un
exemple connu du lecteur. Toutes les règles du non-initié s'appliquent, en plus strict.

### Comment les deux se combinent

K choisit la posture, N règle le contenu à l'intérieur de cette posture. Une même ligne de routage
peut donc se rédiger à trois niveaux de contenu, et un même niveau de contenu se rencontre sous
plusieurs postures. Les règles de niveau ne remplacent pas les règles propres à la posture et ne les
contredisent pas : elles bornent seulement ce que le lecteur peut recevoir.

## Table de routage

<!-- gabarit: une ligne par posture retenue à la génération, plus la ligne par défaut, qui reste
     obligatoire. La dernière colonne est la seule vérifiée par le validateur pour
     l'atteignabilité : elle ne contient qu'une référence `posture:<id>` entre apostrophes
     inverses, rien d'autre. Une posture définie sans ligne ici, et sans court-circuit dans un
     fichier de registre, est du
     contenu mort.

     Les sept identifiants ci-dessous (apprenant, pair, guide, arbitre, contradicteur, diplomate,
     provocateur) sont ceux du menu de départ du méta-skill, repris tels quels pour montrer la forme
     attendue. Renommer, fusionner ou ajouter une posture à la génération suppose de répercuter le
     changement ici. Comme ce dossier ne contient qu'un gabarit de posture et aucun fichier réel à
     ces sept id, le validateur signale ces sept lignes comme injoignables tant que l'extraction n'a
     pas produit les fichiers correspondants : attendu dans cet état, pas une erreur de contrat. -->

| K                                    | P                                | D             | But                          | Posture par défaut      |
| ------------------------------------ | -------------------------------- | ------------- | ---------------------------- | ----------------------- |
| le scripteur en sait moins           | indifférent                      | indifférent   | obtenir une information      | `posture:apprenant`     |
| égalité                              | proche de zéro                   | faible        | construire une position      | `posture:pair`          |
| le scripteur en sait plus            | indifférent                      | indifférent   | transférer une compréhension | `posture:guide`         |
| égalité ou le scripteur en sait plus | indifférent                      | indifférent   | acter une décision           | `posture:arbitre`       |
| égalité ou le scripteur en sait plus | indifférent                      | indifférent   | refuser une position         | `posture:contradicteur` |
| indifférent                          | le lecteur en a sur le scripteur | indifférent   | indifférent                  | `posture:diplomate`     |
| indifférent                          | indifférent                      | indifférent   | déclencher une discussion    | `posture:provocateur`   |
| non renseigné                        | non renseigné                    | non renseigné | non renseigné                | `posture:pair`          |

La dernière ligne s'applique dès qu'un des trois axes manque au contexte fourni, et aussi quand
aucune ligne ne correspond, par exemple pour un but dont la posture n'a pas été retenue. Elle ne
s'invente jamais une valeur, elle route directement vers la posture la plus proche du fonctionnement
par défaut.

## Un but seul peut router, jamais un poids d'acte seul

Une ligne peut router sur le seul but, sans condition sur K, P ou D, si aucune de ces trois entrées
ne distingue la posture visée des autres. Le poids de l'acte à commettre ne route jamais seul :
router sur ce critère revient à confondre une propriété de l'acte avec une entrée d'audience.

## Ce qu'une entrée d'audience n'est pas

<!-- gabarit: rubrique à conserver telle quelle, elle documente une erreur déjà commise sur
     l'extraction qui a servi de point de départ à ce méta-skill. -->

Un rapprochement voulu avec une personne précise (« traiter untel avec plus de familiarité ») n'est
pas une quatrième entrée d'audience : c'est un déplacement de la Posture sur sa composante de
proximité construite, à l'intérieur d'une posture déjà routée par ce tableau, pas une ligne
supplémentaire ici. Router une posture entière pour un seul interlocuteur nommé reproduirait, à
l'échelle d'une personne, l'erreur qui confond l'entrée réelle et la valeur jouée.
