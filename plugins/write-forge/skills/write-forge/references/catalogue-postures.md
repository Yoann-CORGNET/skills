# Catalogue des postures

Sept postures livrées comme menu de départ. Chacune est un jeu de coordonnées sur les sept axes
définis dans `composantes-posture.md`, qu'il faut avoir lu : ce fichier donne des positions, l'autre
donne les axes, les marqueurs et les tests.

## Statut du catalogue

La littérature ne fournit aucune liste canonique de postures de scripteur. Booth 1963 nomme des
corruptions (_pedant's stance_, _advertiser's stance_) face à un seul état sain, la _rhetorical
stance_, définie comme « a proper balance among the three elements that are at work in any
communicative effort: the available arguments about the subject itself, the interests and
peculiarities of the audience, and the voice, the implied character, of the speaker » (verbatim). Ce
sont des pathologies, pas un menu utilisable. Brown & Levinson fournissent bien une taxonomie à cinq
branches, mais de stratégies face à un acte menaçant, pas de postures.

La taxonomie ci-dessous est donc dérivée, pas citée. Le squelette vient du croisement des deux
dimensions les mieux établies, le droit à affirmer joué (composante 3, Heritage) et l'ouverture
dialogique (composante 1, White puis Martin & White), soit six cellules dont une reste vide, avec
deux cellules dédoublées par une troisième dimension : la franchise pour `diplomate`, la prise en
charge pour `provocateur`.

C'est un menu de départ et pas un carcan. À la génération d'une instance, la personne peut renommer
une posture, en fusionner deux, en ajouter une qui n'est pas ici. Ce qui est fixe, ce sont les sept
axes ; les cellules sont une commodité de parcours.

## Pourquoi l'accept ou décline est forcé sur les sept

Le protocole ne demande jamais « choisis celles qui te parlent ». Il présente les sept une par une
et exige une acceptation ou un refus explicite sur chacune, avec une raison pour le refus.

Une sélection libre reconduit le répertoire existant. Une personne retient les cellules qu'elle sait
déjà occuper et laisse tomber les autres, sans jamais distinguer « je n'en ai pas l'usage » de « je
n'y avais pas pensé ». Ce sont exactement les deux réponses qu'il faut séparer, et seule la seconde
est intéressante. Le refus explicite oblige à produire une raison, et c'est la raison qui fait
remonter l'angle mort.

Les trois trous listés juste en dessous en sont la démonstration : dans un répertoire construit par
sélection libre, ils manquent sans avoir jamais été refusés, faute d'avoir été posés. Le coût de la
question est d'une minute, le coût de la reconduction est durable, parce qu'une posture absente du
catalogue ne produit pas d'erreur visible. Elle est approximée en silence par la posture voisine, et
c'est cette approximation silencieuse que le refus explicite empêche.

Une troisième réponse existe, le report : la personne veut la posture mais le matériau manque pour
la calibrer. Elle reste explicite, et se journalise avec ce qui manquait au lieu de disparaître dans
une décline (étape 9b du protocole).

## Les trois trous que ce catalogue comble

Par rapport à un répertoire courant de quatre postures (`pair`, `guide`, `apprenant`, `provocateur`)
:

- Aucune posture pour acter une décision, comblé par `arbitre`. Le registre rapport technique
  (décision, post-mortem, recommandation) l'exige. Sollicité là, `guide` produit du conditionnel où
  il faut une décision.
- Aucune posture pour refuser franchement, comblé par `contradicteur`. `pair` sait sonder, il ne
  sait pas refuser. Quand le désaccord est déjà tranché, la question socratique cesse d'être honnête
  et le sondage devient une manœuvre, sans cellule de repli.
- Aucune posture pour l'asymétrie de pouvoir, comblé par `diplomate`.

Un quatrième écart mérite d'être signalé pour ce qu'il n'est pas : un « collègue très proche » n'est
pas une posture. C'est un déplacement sur la seule composante 5 à l'intérieur de `pair`. Le modèle
le traite comme un paramètre.

## Identifiants et références croisées

Chaque posture porte un `id` kebab-case stable, qui va dans le frontmatter du fichier de posture
généré. Les références croisées, depuis les registres comme depuis le validateur, se font par `id`
et jamais par libellé humain. Le libellé est renommable, l'`id` ne l'est pas : dans l'instance de
référence, les fichiers se citent par « Ami » ou « Expert qui guide/nuance », si bien que renommer
une posture casse silencieusement les registres qui la citent.

## Notation des coordonnées

- `−` bas, `~` moyen, `+` haut, `−−` très bas. La graduation est ordinale, pas métrique.
- Composante 3, notation épistémique : `K−` revendique moins de savoir que le lecteur, `K=`
  symétrie, `K+` revendique davantage. Heritage écrit K+ et K− et traite l'écart comme un gradient ;
  le `K=` est une commodité de ce catalogue pour désigner la zone de symétrie, pas une catégorie de
  la source.
- Composante 7 : `pleine` ou `partielle`. L'axe est gradué, mais seule la portée de la suspension
  compte à l'usage.
- `var.` signifie que la posture ne fixe pas la valeur. Chaque fiche dit alors ce qui la fixe.
- Toutes ces valeurs sont des valeurs jouées, y compris sur la composante 3. Un `K+` joué n'implique
  aucun K+ réel : cette dissociation est précisément le mécanisme de `provocateur`.

| `id`            | 1. Ouv. dialogique | 2. Intensité | 3. Droit à affirmer | 4. Franchise | 5. Proximité | 6. Adresse | 7. Prise en charge |
| --------------- | ------------------ | ------------ | ------------------- | ------------ | ------------ | ---------- | ------------------ |
| `apprenant`     | +                  | −            | `K−`                | ~            | var.         | +          | pleine             |
| `pair`          | +                  | ~            | `K=`                | ~ à +        | +            | +          | pleine             |
| `guide`         | +                  | ~            | `K+`                | −            | ~            | +          | pleine             |
| `arbitre`       | −                  | ~            | `K+`                | +            | −            | −          | pleine             |
| `contradicteur` | −                  | +            | `K=` à `K+`         | +            | ~            | +          | pleine             |
| `diplomate`     | ~ à +              | −            | var.                | −−           | −            | ~          | pleine             |
| `provocateur`   | −                  | +            | `K+` joué           | +            | +            | +          | **partielle**      |

## Ce qui déclenche une posture

Les déclencheurs s'expriment en entrées d'audience (K, P, D) et en but. Le but n'est pas une entrée
d'audience : c'est la variable que le rédacteur fixe lui-même, et il est nommé comme tel dans chaque
fiche. Rx, la gravité de l'acte à commettre, n'est pas une entrée d'audience non plus : c'est une
propriété de l'acte, et elle relève la dose de franchise dans n'importe quelle posture. Ne jamais
router vers une posture sur le seul Rx.

## Ce que le champ `suspend:` nomme

Une fiche de posture générée peut déclarer `suspend: [<id de trait de voix>, ...]`, la liste des
invariants de voix que cette posture surcharge. Trois règles, toutes vérifiées par le validateur.

Les cibles se nomment par `id`. Une déclaration par libellé casse au premier renommage.

Les cibles se décrivent par direction sur un axe, jamais par forme. Une posture suspend « une
direction d'expansion dialogique sur la composante 1 », pas « le réflexe de la question ». Un
invariant de voix qui nomme une forme interpersonnelle est déjà mal placé, et le déclarer suspendu
reconduirait l'erreur.

La suspension est à portée partielle. La posture reste _principal_ sur le contenu propositionnel,
donc l'Étape 0 de vérification factuelle n'est jamais suspendable, y compris en `provocateur`.

Dans les fiches ci-dessous, les suspensions sont données par type, puisque les traits de voix d'une
instance ne sont connus qu'à la génération. Le validateur vérifie ensuite que chaque `id` déclaré
existe bien dans le `voix.md` de l'instance.

---

## `apprenant`

### Déclencheur

Le lecteur détient le savoir dont j'ai besoin, K− réel ou joué. But : obtenir une information ou une
correction. P et D indifférents.

### Coordonnées

Ouverture dialogique haute, par _entertain_ et par attribution. Intensité basse. Droit à affirmer
explicitement concédé au lecteur, `K−`. Franchise moyenne : l'acte menaçant est la demande
elle-même, qui pèse sur le temps du lecteur, donc atténuation modérée et non maximale. Sur-atténuer
bascule en `diplomate` et se lit comme de la déférence. Proximité construite `var.`, fixée par
l'entrée D et par le fait que la demande s'appuie ou non sur un terrain commun pour être recevable.
Adresse au lecteur haute. Prise en charge pleine : la demande est sincère.

### Ancrage

Heritage 2012, pour la posture épistémique basse et la forme interrogative comme son véhicule
canonique. Hyland 2005 pour les questions comme ressource d'_engagement_. Brown & Levinson pour le
dosage de l'imposition.

### Susceptible de suspendre

Une direction de contraction dialogique sur la composante 1, si la voix en porte une. Une direction
de revendication haute sur la composante 3.

---

## `pair`

### Déclencheur

K comparable, P proche de zéro, socle de références commun présupposé. But : construire ou ajuster
une position ensemble.

### Coordonnées

Ouverture dialogique haute, et c'est sa signature : on sonde, on n'assène pas. Intensité moyenne.
Droit à affirmer symétrique, `K=`, sans glose ni directive. Franchise moyenne à haute, la symétrie
autorisant à assumer une part de menace sans préface. Proximité construite haute. Adresse haute.
Prise en charge pleine.

### Ancrage

Du Bois 2007, le _stance triangle_ : le sujet évalue un objet, se positionne, et s'aligne sur
d'autres sujets. La cellule paire est celle où l'alignement est en jeu à chaque tour. Martin & White
sur l'alignement et le lecteur construit. Brown & Levinson : à D et P faibles, le poids de l'acte
est bas, donc les réalisations peu atténuées deviennent disponibles sans coût.

### Susceptible de suspendre

En principe rien. C'est la cellule la plus proche du fonctionnement par défaut, et celle où l'espace
laissé libre à la Voix est le plus large. Une posture `pair` qui déclare beaucoup de suspensions
signale plutôt un `voix.md` mal découpé.

---

## `guide`

### Déclencheur

Le lecteur est K− sur l'objet et je suis K+. But : transférer de la compréhension, pas obtenir un
accord.

### Coordonnées

Ouverture dialogique haute malgré `K+`. C'est la combinaison contre-intuitive : le conditionnel
plutôt que l'affirmation tranchée, alors même que le scripteur en sait plus que son lecteur.
Intensité moyenne. Droit à affirmer haut, directives et gloses assumées. Franchise basse : la
supériorité épistémique fait porter au moindre acte direct une menace de face disproportionnée.
Proximité moyenne. Adresse haute. Prise en charge pleine.

### Ancrage

Heritage 2012, K+ de statut avec une posture épistémique volontairement abaissée. Hyland 2005,
directives et hedges coexistent dans l'écriture experte. Booth 1963 : c'est la cellule la plus
exposée à la _pedant's stance_, « ignoring or underplaying the personal relationship of speaker and
audience and depending entirely on statements about a subject » (verbatim). Montrer le raisonnement
plutôt que la seule conclusion est la contre-mesure directe.

### Susceptible de suspendre

Une direction de franchise haute sur la composante 4, la dose y étant basse. Voir aussi la question
ouverte sur le novice dans l'erreur, plus bas : c'est le point où cette cellule peut avoir à
suspendre une direction d'expansion sur la composante 1, ce que la théorie ne tranche pas.

---

## `arbitre`

### Déclencheur

Une décision doit être actée et j'en réponds, ou le lecteur attend un verdict plutôt qu'un éventail.
K+ ou K= sur l'objet, mais la donnée déterminante est la responsabilité, pas le savoir. But : clore.

### Coordonnées

Contraction dialogique par _pronounce_ et _endorse_, assertions monoglossiques assumées. Intensité
moyenne, l'autorité n'ayant pas besoin de crier. Droit à affirmer haut. Franchise haute : le refus
d'atténuer fait partie de la lisibilité de la décision. Proximité basse. Adresse au lecteur basse,
par impersonnalisation et nominalisation. Prise en charge pleine, y compris des conséquences.

### Ancrage

Martin & White 2005 sur la contraction dialogique et sur le statut dialogique des assertions nues :
une assertion monoglossique n'est pas un défaut de nuance, c'est une opération rhétorique qui pose
la proposition comme non négociable.

### Susceptible de suspendre

Une direction d'expansion dialogique sur la composante 1, ce qui est le cas le plus fréquent. Une
direction de proximité haute sur la composante 5 et d'adresse haute sur la composante 6.

---

## `contradicteur`

### Déclencheur

Une position doit être refusée, et j'assume ce refus en mon nom. Distinct de `arbitre` : `arbitre`
clôt sur une décision, `contradicteur` clôt sur la position de quelqu'un d'autre. But : refuser.

### Coordonnées

Contraction dialogique par _disclaim_ (deny, counter) et non par _proclaim_ : l'écart de marqueurs
avec `arbitre` est net et se vérifie au comptage. Intensité haute. Droit à affirmer `K=` à `K+`,
fixé par le fait que le scripteur tienne ou non le territoire de savoir de la position refusée.
Franchise haute, jusqu'à l'acte non atténué quand l'enjeu le justifie. Proximité moyenne : la
politesse positive, terrain commun et humour, est le principal moyen de rendre le refus tenable sans
l'atténuer. Adresse haute. Prise en charge pleine, et c'est ce qui le sépare de `provocateur`.

### Ancrage

Martin & White pour le _disclaim_. Brown & Levinson : la combinaison d'un acte non atténué et d'une
politesse positive forte est ce que le modèle prédit entre intimes, et c'est ce qui rend un
désaccord franc compatible avec une relation préservée.

### Susceptible de suspendre

Une direction d'expansion dialogique sur la composante 1, puisqu'il contracte par refus.

---

## `diplomate`

### Déclencheur

L'entrée P. Asymétrie de pouvoir : client, régulateur, hiérarchie, investisseur, jury. K et D
indifférents, c'est P qui commande, et c'est la seule cellule du catalogue où P est la variable
pilote.

Un acte à Rx très élevé (mauvaise nouvelle, refus contraint, négociation) produit des réalisations
voisines, mais Rx n'est pas une entrée d'audience : c'est une propriété de l'acte, et elle relève la
dose de franchise dans n'importe quelle posture. Ne pas router vers `diplomate` sur le seul Rx.

### Coordonnées

Franchise très basse, `−−` : politesse négative systématique, et recours à l'évitement de
l'attribution quand l'acte est trop lourd. Intensité basse. Proximité construite basse, le marqueur
d'in-group étant un risque plutôt qu'un atout face à une asymétrie de pouvoir. Ouverture dialogique
moyenne à expansive, reconnaître les positions alternatives faisant partie de l'atténuation. Droit à
affirmer `var.`, fixé par le K réel : le `diplomate` peut être K+ ou K− sur l'objet, la posture ne
dit rien de ce point. Adresse moyenne. Prise en charge pleine.

### Ancrage

Brown & Levinson 1987, politesse négative : déférence, impersonnalisation du locuteur et du
destinataire, énonciation de l'acte menaçant comme règle générale, nominalisation. Le calcul du
poids Wx = D + P + Rx est [PARTIELLEMENT VÉRIFIÉ] et sert ici de cadre, pas de preuve.

### Question ouverte, signalée et non tranchée au-delà de ce choix

Chez Brown & Levinson, P est une entrée du calcul du poids et pas une posture. On peut donc soutenir
que `diplomate` n'est pas une cellule mais un modificateur applicable aux six autres : `guide`
déférent, `arbitre` déférent. Le catalogue la garde comme posture, pour l'utilisabilité du menu et
parce qu'une cellule se parcourt là où un modificateur doit se deviner. Le choix est assumé et la
question reste ouverte. Le signal d'arbitrage est concret : si la personne se retrouve à décrire «
`guide` mais avec un client », c'est un modificateur, et la cellule doit être convertie.

### Susceptible de suspendre

Une direction de franchise haute sur la composante 4, et une direction de proximité haute sur la
composante 5. C'est la posture qui suspend le plus, ce qui est cohérent avec la réserve ci-dessus :
un modificateur se reconnaît à ce qu'il surcharge beaucoup et n'apporte pas de coordonnées propres.

---

## `provocateur`

### Déclencheur

Le but seul. Aucune entrée de relation ne route vers cette cellule : elle se choisit quand
l'objectif est de déclencher de la discussion plutôt que d'emporter l'adhésion. Registre de
visibilité.

### Coordonnées

Contraction dialogique assumée, une position tranchée appelant la réponse. Intensité haute. Droit à
affirmer joué haut, indépendamment du statut réel. Franchise haute. Proximité construite haute.
Adresse haute. Prise en charge partielle, et c'est la seule coordonnée qui la définit : sans la
composante 7, `provocateur` et `contradicteur` auraient des coordonnées quasi identiques alors
qu'ils diffèrent sur ce qui compte, l'un assume et l'autre met en scène.

### Ancrage, et sur quoi l'argument ne tient pas

Goffman 1979 : le scripteur reste _animator_ et _author_, mais n'est _principal_ que partiellement.
Heritage 2012 pour la dissociation documentée entre statut réel et posture affichée.

La raison pour laquelle une posture délibérément non authentique reste de la Posture et ne devient
jamais de la Voix n'est pas qu'une performance serait trop rare pour sédimenter. Un persona répété
des centaines de fois sédimente très bien et devient parfaitement reconnaissable. L'argument tient
au rôle : la Voix se définit par ce dont le scripteur répond de lui-même, donc elle se situe du côté
du _principal_, tandis que la performance se situe du côté de l'_animator_ et de l'_author_. Un
persona peut donc être stable, durable et identifiable sans être de la Voix. C'est cette
formulation-là qu'il faut reprendre dans une instance générée, et pas l'argument de sédimentation,
qui est faux.

### Bornes normatives

Booth 1963 donne les deux dérives et permet de dire où « constructif » cesse de l'être. Texte
intégral lu ; la mise en page à deux colonnes rend la pagination par terme non fiable, donc aucun
numéro de page n'est donné par terme.

L'_advertiser's stance_ : « undervaluing the subject and overvaluing pure effect », que Booth juge «
probably in the long run a more serious threat in our society than the danger of ignoring the
audience ». L'_entertainer's stance_ : « the willingness to sacrifice substance to personality and
charm », que Booth introduit en passant (« one could easily discover other perversions ») et non
comme un troisième terme symétrique. La présenter comme une triade équilibrée avec les deux autres
est une reconstruction postérieure.

Test praticable de la borne : si le contenu propositionnel a été modifié pour servir l'engagement,
la borne est franchie. C'est la même frontière que la suspension à portée partielle. Le cadrage est
suspendable, le fait ne l'est pas, et l'Étape 0 tient en `provocateur` comme partout ailleurs.

### Susceptible de suspendre

Une direction d'expansion dialogique sur la composante 1, puisqu'il contracte volontairement. Et
rien d'autre : ni les traits idiolectaux sans fonction interpersonnelle, ni une préférence de
concision, ni un geste rhétorique. Le rôle de _principal_ sur le contenu propositionnel n'est jamais
dans la liste.

---

## Format des triplets de calibration

Le triplet forcé est le bon format d'élicitation : une variante à éviter par excès, une variante à
éviter par défaut, et la forme préférée. Il borne la calibration par le haut et par le bas au lieu
de la demander dans l'abstrait, ce qui transforme une préférence en coordonnée.

La règle : un triplet ne fait varier qu'une composante. Sinon le rejet n'identifie rien.

### Un triplet mal construit

Un triplet de calibration de `pair`, écrit à la main, propose « Mouais, je suis pas convaincu,
j'aurais plutôt fait Y » comme variante à éviter. Elle s'écarte simultanément sur trois composantes
: la 1 (_disclaim- deny_, donc contraction), la 2 (« Mouais » est un marqueur d'attitude à forte
charge) et la 4 (désaccord non atténué, sans préface). L'étiquette « trop brutal » vise probablement
la 4, mais le contraste proposé ne permet pas de l'établir : le rejet est compatible avec les trois.

La seconde variante, « Intéressant, mais je me demande si Y ne serait pas plus robuste ici »,
s'écarte sur deux composantes : la 4 (sur-atténuation par compliment, contre-argument et double
hedge) et la 3 (« je me demande » relocalise la question dans l'incertitude du scripteur au lieu de
la laisser sur le territoire du lecteur).

C'est un défaut du dispositif d'élicitation et pas de l'intuition de la personne. La forme retenue
est juste ; ce que le triplet ne sait pas dire, c'est pourquoi.

### Construction correcte

Quatre contraintes.

1. La phrase de base reste verbatim dans toutes les variantes. Seul un habillage ajouté varie.
2. Chaque token de l'habillage se vérifie contre les sept listes de marqueurs de
   `composantes-posture.md`, et pas seulement contre celle qu'on vise.
3. Chaque variante porte une ligne de delta sur les sept composantes, avec exactement un `≠`.
4. Le rejet s'enregistre avec la composante sur laquelle il portait.

### Exemple corrigé, sur la composante 4

Base, la forme préférée du triplet :

> Tu as envisagé ce cas d'usage dans le choix de ta solution ?

Variante basse sur la composante 4, habillage d'excuse préalable :

> Désolé de revenir là-dessus, tu as envisagé ce cas d'usage dans le choix de ta solution ?

Delta : `1 =` `2 =` `3 =` `4 ≠` (bas) `5 =` `6 =` `7 =`. Un seul axe bouge, le rejet ou
l'acceptation de cette variante identifie donc une coordonnée sur la composante 4.

Variante haute sur la composante 4 : aucun habillage propre n'est disponible. La forme de base est
déjà non atténuée, et ce qui lui reste d'atténuation tient à la forme interrogative elle-même. Aller
vers le pôle non atténué impose donc de remplacer la phrase, ce qui déplace d'autres axes. Le
candidat le plus proche, livré ici comme contre-exemple et non comme borne :

> Ce cas d'usage n'est pas couvert par ta solution.

Delta : `1 ≠` (contraction par _disclaim-deny_) `2 =` `3 ≠` (assertion sur le territoire du lecteur
au lieu d'une interrogation) `4 ≠` (haut) `5 =` `6 ≠` (l'interpellation disparaît, la deuxième
personne se réduit au possessif) `7 =`. Quatre axes bougent.

Ce que ça impose au protocole : quand un pôle n'est pas atteignable par habillage, le triplet
devient un couple, base plus une seule borne, et la borne manquante s'obtient par une élicitation
séparée dont le delta multi-axes est écrit explicitement, la question étant alors posée axe par axe.
Ne jamais présenter une variante contaminée comme une borne propre : c'est exactement l'erreur que
la règle sert à éviter.

### Habillages qui paraissent à axe unique et ne le sont pas

Vérifiés contre les listes de `composantes-posture.md`. Cette liste est courte parce que la plupart
des habillages intuitifs échouent, ce qui explique à lui seul pourquoi le triplet d'origine confond
trois axes.

- « peut-être », « sans doute » : modalisation épistémique, composante 1.
- « on » inclusif [FR] : composantes 5 et 6.
- « ce n'est pas que… », « non pas que… » : négation d'une position attribuable, composante 1.
- « juste une petite remarque », « vite fait » : minimisation, composante 4.
- « je me demande si » : relocalise l'incertitude sur le scripteur, composante 3, en plus d'atténuer
  sur la composante 4.
- « je joue l'avocat du diable », « disons que » : cadre de désengagement, composante 7.
- un impératif d'ouverture (« explique-moi… ») : directive, composante 3, et il supprime
  l'interrogative, donc les composantes 1 et 6.

### Qui produit les variantes

Faire produire les trois variantes par le skill garantit la variation à axe unique mais risque
d'imposer des formulations étrangères. Faire produire des exemples réels par la personne garantit
l'authenticité mais confond les axes, comme le montre le triplet d'origine. La piste retenue :
partir d'un exemple réel de la personne, puis en dériver mécaniquement les variantes à axe unique.

---

## Cellules et questions laissées ouvertes

### La cellule K− par contraction est vide

Le croisement des deux dimensions principales donne six cases, et celle-ci n'a pas de posture. Le
cas existe pourtant : le contrôleur, l'auditeur, le jury qui ne connaît pas le domaine mais détient
le pouvoir de rejeter. Ils revendiquent moins de savoir que leur lecteur tout en verrouillant le
dialogue.

Dans ce catalogue, le cas est absorbé par `arbitre`, sur le principe que la responsabilité prime sur
le savoir. Le choix est discutable et il est laissé ouvert. Signal de révision : si la personne
décrit une situation où elle verrouille une décision sur un objet qu'elle ne maîtrise pas, et que
`arbitre` la force à revendiquer un `K+` qu'elle n'a pas, la cellule manque et il faut l'ouvrir.

### Le `guide` face à un novice factuellement dans l'erreur, sous contrainte de temps

La théorie ne tranche pas. C'est le point exact où une direction de Voix, le réflexe d'expansion
dialogique, et une exigence de posture, corriger maintenant, peuvent se contredire. Seule une
élicitation sur un cas réel, ou le corpus personnel, y répond.

C'est la question à poser en premier dans l'élicitation, parce que la réponse détermine le statut de
l'expansion. Si la personne contracte dans ce cas, l'expansion n'est pas une direction de Voix :
elle est la coordonnée commune de `apprenant`, `pair` et `guide`, donc de la posture, et le
`voix.md` de l'instance doit être amputé d'autant.

### `diplomate`, posture ou modificateur

Traitée dans la fiche `diplomate`. Non tranchée au-delà du choix de la garder comme cellule.

### Où le registre plafonne chaque axe

Les composantes 4 et 6 sont fortement bornées par le genre. Établir ces plafonds est du travail de
registre, hors du périmètre de ce fichier, mais une posture qui les ignore demandera des doses
irréalisables, par exemple un `contradicteur` non atténué dans un papier de recherche.

---

## Sources

Les références complètes, avec leur statut de vérification, sont dans `composantes-posture.md`. Deux
ajouts propres à ce fichier :

1. Du Bois, J.W. (2007). « The stance triangle », dans R. Englebretson (éd.), _Stancetaking in
   Discourse: Subjectivity, evaluation, interaction_, Amsterdam : John Benjamins, pp. 139-182.
   _Evaluate_, _position_, _align_.
2. Booth 1963, verbatim de la _rhetorical stance_ et de la _pedant's stance_, texte intégral lu,
   pagination par terme non fiabilisable.

Rappel de citation qui vaut pour tout le skill : la numérotation des stratégies de Brown & Levinson
n'est citée nulle part, le texte primaire étant sous paywall et le détail interne seulement
[PARTIELLEMENT VÉRIFIÉ]. Les règles qui s'y adossaient sont énoncées sur leur propre raisonnement.
