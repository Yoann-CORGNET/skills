# Composantes de la posture

Sept axes sur lesquels une posture prend une valeur. Ce fichier définit les axes, donne leurs
sources, leurs marqueurs observables, ce qui les fait varier, et le test qui sépare ce qui relève de
la Posture de ce qui relève de la Voix ou du Registre. Le menu de postures livré se lit dans
`catalogue-postures.md`, qui donne la position de chaque posture sur chacun de ces sept axes.

Les composantes sont des axes de fonction, pas de forme. Une même forme réalise plusieurs axes à la
fois : une question adressée au lecteur ouvre le dialogue, atténue une menace de face, concède un
territoire de savoir et fait exister le lecteur dans le texte, simultanément. L'orthogonalité est
exigée des axes, pas des marqueurs. Cette non-orthogonalité des marqueurs est aussi ce qui rend
difficile la règle de calibration à axe unique, traitée dans `catalogue-postures.md`.

## Entrée de contexte et valeur jouée

Toutes les théories du positionnement séparent ce que la situation donne de ce que le scripteur en
fait.

| Théorie               | Entrée de contexte                                       | Valeur jouée                                              |
| --------------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| Heritage 2012         | _epistemic status_ (K+/K−) : qui sait réellement quoi    | _epistemic stance_ : ce que la forme grammaticale affiche |
| Brown & Levinson 1987 | D, P, Rx                                                 | la stratégie choisie face à l'acte menaçant               |
| Halliday 1978         | _tenor_ : relations de statut et de rôle de la situation | la sélection dans les ressources interpersonnelles        |

L'Audience fournit les entrées (K, P, D réels). La Posture fournit la valeur jouée sur ces entrées.
Heritage 2012 établit que les deux se dissocient : le résumé de l'article indique que le statut
épistémique peut être dissimulé par des locuteurs qui déploient une posture épistémique pour
paraître plus, ou moins, savants qu'ils ne le sont. Reformulation du résumé, pas citation : seul le
résumé a été consulté, via agrégateur.

La règle de nommage qui en découle est la clé de voûte du découpage Audience / Posture, et elle vaut
pour toutes les fiches de ce skill. **Aucune composante de posture ne porte le nom d'une entrée
d'audience.** L'écart de distance réelle entre le scripteur et son lecteur est l'entrée D : elle
appartient à l'Audience, le texte la reçoit et ne la choisit pas. Ce que le texte choisit, c'est la
quantité de proximité qu'il fabrique, et cette quantité peut aller contre l'entrée dans les deux
sens : construire de la familiarité malgré une entrée D élevée (un post public), ou tenir de la
réserve malgré une entrée D faible (un post-mortem entre collègues proches). La composante s'appelle
donc Proximité construite, et jamais du nom de l'entrée. Confondre les deux fait disparaître
exactement ce que la couche Posture sert à modéliser : l'écart entre la situation reçue et la
relation jouée.

La même règle protège la composante 3. Le K réel est une entrée d'audience ; le K joué est la
composante Droit à affirmer. Un scripteur K+ peut jouer K− (socratique), un scripteur K= peut jouer
K+ (usurpation).

## Frontière avec le Registre

Le Registre fixe quelles formes sont disponibles pour réaliser une valeur : un papier de recherche
interdit l'impératif adressé au lecteur dans la section résultats, un email ne l'interdit pas. La
Posture fixe quelle valeur on veut réaliser. Même valeur d'axe, formes différentes selon le registre
: c'est ce que le test discriminant exploite.

Deux composantes sont fortement plafonnées par le genre, la 4 (Franchise) et la 6 (Adresse au
lecteur). Le plafond est du travail de registre, mais la Posture doit savoir qu'il existe, sinon
elle demandera une dose irréalisable, par exemple un refus non atténué dans un papier de recherche.

## Ce que coûte une implémentation partielle

Les composantes 1 (Ouverture dialogique), 3 (Droit à affirmer) et 4 (Franchise) portent l'essentiel.
Une instance allégée peut se limiter à ces trois axes et rester utilisable : elles couvrent le
risque épistémique, la revendication de territoire de savoir et le risque social, soit les trois
décisions que toute posture doit prendre. Le squelette du catalogue est d'ailleurs bâti sur le
croisement de deux d'entre elles.

Information de coût, pour décider d'une coupe en connaissance de cause :

- Sans la 2 (Intensité évaluative), les postures gardent leur direction et perdent leur volume.
  `arbitre` et `contradicteur` se rapprochent, une partie de leur écart tenant à l'intensité.
- Sans la 5 (Proximité construite), l'humour et les marqueurs d'in-group n'ont plus de couche
  d'accueil. Ils remontent dans la Voix, ce qui est précisément la fuite de couche que le filtre de
  forme sert à détecter.
- Sans la 6 (Adresse au lecteur), tout le travail de plafonnement se reporte sur les fiches de
  registre, qui devront alors porter seules la dose et la forme.
- Sans la 7 (Prise en charge énonciative), `provocateur` devient indistinguable de `contradicteur`,
  et le mécanisme de suspension déclarée perd son fondement. Si `provocateur` est retenu au
  catalogue, la 7 n'est pas coupable.

## Avant de promettre des traits comptables

Les listes ci-dessous sont données comme comptables, en densité pour 1000 mots. Trois réserves
conditionnent cette promesse, et elles s'appliquent avant toute métrique automatique.

### Ambiguïté du français

Trois formes fréquentes portent plusieurs axes à la fois et ne se comptent pas sans désambiguïsation
par le cotexte.

- « on » [FR]. Inclusif du lecteur, il relève des composantes 5 et 6 (« on a tous connu ça »).
  Impersonnel, il relève de l'effacement de l'énonciateur et compte à l'inverse (« on observe que
  »).
- Le conditionnel [FR]. Hedge épistémique, il relève de la composante 1 (« ce serait plutôt X »).
  Politesse, il relève de la composante 4 (« il faudrait revoir ce point »). Le départage se fait
  par la présence ou l'absence d'un acte menaçant dans la même phrase.
- La forme interrogative [FR pour sa formation, universelle pour sa fonction]. Elle porte
  simultanément les composantes 1, 3, 4 et 6. Elle ne se compte jamais comme un marqueur unique :
  elle se ventile selon ce que la question fait, ouvrir une alternative, concéder un territoire,
  atténuer un acte, interpeller.

### Dépendance à la langue

Les instances produites par ce skill sont multilingues. La règle générale : la catégorie
fonctionnelle se transpose, la liste d'exemples ne se transpose pas. « Intensifieur » existe dans
toutes les langues visées, « énormément » n'existe qu'en français.

Chaque fiche porte une ligne « Transposition » qui dit ce qui passe et ce qui se re-dérive. La
marque `[FR]` signale les items dont même la catégorie est liée à la langue : l'opposition
tutoiement / vouvoiement (absente de l'anglais, qui réalise l'écart autrement), l'ambiguïté de « on
», la double valeur du conditionnel, le mode de formation des interrogatives, les apocopes. Le
suffixe « -ish » figure dans la liste de flou catégoriel de la composante 2 : c'est un item anglais,
et il montre à lui seul que ces listes sont des dérivations et non des universaux.

### Comparabilité des densités

Une densité pour 1000 mots ne se compare qu'à l'intérieur d'une même langue. La baseline de
comparaison doit être écrite dans la langue du corpus, sinon l'écart mesuré mélange l'effet de
posture et l'effet de langue.

## Le test discriminant, commun aux sept fiches

Chaque fiche se termine par la manipulation concrète du protocole suivant, appliqué à sa composante.

1. Test A, fixer la relation et changer le registre. Le trait bouge : il est gouverné par le
   Registre.
2. Test B, fixer le registre et changer la relation ou le but. Le trait bouge : il est gouverné par
   la Posture.
3. Le trait survit aux deux : il appartient à la Voix.
4. Test C, complément. Un trait qui survit à A et B mais qu'une posture de performance suspend
   explicitement est un invariant de Voix suspendu par préséance, pas une calibration de posture.

Deux précautions de lecture. La forme peut bouger au test A alors que la dose reste stable : c'est
le cas normal, le registre borne les réalisations disponibles et la posture fixe la quantité. Et un
trait de Voix surchargé par une posture n'est pas réfuté pour autant : la préséance prévoit qu'une
posture prime, c'est la contrepartie assumée du partage direction / dose / forme.

L'ancrage de « la Voix est ce qui persiste » est la _stance accretion_, où des prises de position
locales répétées se sédimentent en identité et en style durables (Bucholtz & Hall 2005, reprenant
Rauniomaa 2003 [NON VÉRIFIÉ] et Du Bois 2002 [NON VÉRIFIÉ]), complétée par Kiesling 2009, pour qui
les variantes sont d'abord associées à des prises de position interactionnelles qui se réifient
ensuite par l'usage répété. La Voix est donc de la posture sédimentée, ce qui explique qu'elle ne
contienne qu'une direction sur un axe.

---

## Composante 1. Ouverture dialogique

### Définition

Degré auquel le texte reconnaît l'existence de positions alternatives à celle qu'il avance et leur
laisse de la place. Un pôle contractif écarte, réfute ou verrouille les alternatives. Un pôle
expansif les invoque et présente la position tenue comme une parmi d'autres. C'est l'axe maître : il
encode le risque épistémique pris.

### Source

Martin & White 2005, _The Language of Evaluation_, chapitre 3, système ENGAGEMENT. Texte primaire lu
(chapitre échantillon). Le système oppose **monoglossique**, aucune reconnaissance d'autres voix, et
**hétéroglossique**, puis subdivise l'hétéroglossique en **contraction dialogique** (_disclaim_ :
deny, counter ; _proclaim_ : concur, pronounce, endorse) et **expansion dialogique** (_entertain_ ;
_attribute_ : acknowledge, distance).

Le système _engagement_ est majoritairement le travail de White, publié d'abord dans White 2003,
_Text_ 23(2) : 259-284, puis intégré dans Martin & White 2005. Quelques bases indiquent 23(3) :
divergence signalée. L'attribuer au seul Martin est courant et inexact. L'origine bakhtinienne de
l'hétéroglossie est [NON VÉRIFIÉ] directement, connue via Martin & White et White.

Les _hedges_ et _boosters_ de Hyland 2005 sont des réalisations de cet axe. Le terme « hedge » vient
de Lakoff 1973, pas de Hyland, qui l'opérationnalise en trait comptable de corpus.

### Marqueurs observables

Comptable en ratio contractif / expansif pour 1000 mots.

Contractif :

- négation portant sur une proposition attribuable à autrui (« ce n'est pas que… ») ;
- connecteurs de contre-attente (« mais », « or », « pourtant », « bien que », « en réalité ») ;
- concurrence, qui pose l'accord comme déjà acquis (« évidemment », « bien sûr », « on le sait ») ;
- _pronouncement_ (« je maintiens que », « il ne fait aucun doute que ») ;
- endossement (« X a démontré que ») ;
- assertions nues au présent de vérité générale.

Expansif :

- modalisation épistémique (« il semble », « peut-être », « à mon avis », « je crois que ») ;
- conditionnel [FR], ambigu, voir la réserve de comptabilité et la composante 4 ;
- questions expositives ;
- attribution (« selon X ») et attribution distanciante (« X prétend que »).

Transposition : les deux catégories et leurs sous-types sont des fonctions, ils se transposent tels
quels. Les listes de connecteurs, de modalisateurs et le cas du conditionnel se re-dérivent par
langue.

### Ce qui la fait varier

Contextuelle. Varie selon la présence d'un désaccord à traiter et selon le but visé : obtenir
l'adhésion, ouvrir un débat, ou acter une décision. Ne varie pas directement avec l'écart de savoir
réel : un expert peut être très expansif (`guide`) ou très contractif (`arbitre`). La direction
préférentielle d'une personne sur cet axe est, elle, un trait de Voix.

### Test discriminant

Test B d'abord : prendre le même désaccord et l'écrire pour un pair, puis pour quelqu'un qui se
trompe et doit être corrigé maintenant, registre constant (email). Si le ratio contractif / expansif
bouge, l'axe est bien de la posture.

Test A ensuite : même relation, email puis rapport technique. Si seule la forme change (« tu as
envisagé X ? » devient « l'hypothèse X n'a pas été testée ») alors que le ratio reste du même côté,
la direction appartient à la Voix et la forme au Registre.

---

## Composante 2. Intensité évaluative

### Définition

Volume auquel le jugement est monté : à quel point les valeurs, les qualités et les quantités sont
amplifiées ou atténuées, et à quel point les catégories sont durcies ou floutées. Distincte de la
composante 1 : on peut être très certain sans être véhément, et très véhément tout en restant
dialogiquement ouvert.

### Source

Martin & White 2005, chapitre 3, système GRADUATION : _force_ (intensification et quantification) et
_focus_ (netteté de la catégorie). Vérifié sur le texte primaire, sections « Graduation: focus » et
« Graduation: force ». Les auteurs y rangent ensemble « hedges, downtoners, boosters, intensifiers »
selon qu'ils gradent « the force of the utterance or the focus of the categorisation ». Complété par
les _attitude markers_ de Hyland 2005 (vérifié).

Réserve de modélisation assumée : cette composante fusionne deux systèmes distincts chez Martin &
White, ATTITUDE (une évaluation est-elle présente, et de quel type) et GRADUATION (à quelle échelle
est-elle réglée). La fusion est un choix d'opérationnalisation et non une fidélité à la source :
pour un skill de rédaction, « combien de jugement affiché » est une seule manette. Le jour où il
faut distinguer ce qui est jugé de à quel volume, c'est ici qu'il faut dédoubler.

### Marqueurs observables

Comptable pour 1000 mots.

- Force haute : intensifieurs (« très », « extrêmement », « radicalement »), superlatifs, lexique
  intrinsèquement fort (« catastrophique » plutôt que « problématique »), répétition, ponctuation
  expressive.
- Force basse : atténuateurs (« un peu », « plutôt », « légèrement », « relativement »).
- Focus durci : « un vrai problème », « à proprement parler », « purement et simplement ».
- Focus flouté : « une sorte de », « en quelque sorte », suffixe « -ish » [item anglais].
- Marqueurs d'attitude : adjectifs et adverbes portant un jugement affectif (« malheureusement », «
  étonnamment », « regrettable », « élégant »).

Transposition : les quatre catégories (force haute, force basse, focus durci, focus flouté) et les
marqueurs d'attitude sont fonctionnels et se transposent. Toutes les listes lexicales se
re-dérivent. Le « -ish » est laissé visible comme rappel : il n'a pas d'équivalent morphologique
direct en français, qui passe par des locutions.

### Ce qui la fait varier

Contextuelle, avec un plafond de Voix. Varie selon le degré de conviction réelle et selon le but
(mobiliser ou informer). Le plafond personnel, la véhémence maximale qu'une personne s'autorise, est
un trait de Voix stable. Le genre peut imposer un second plafond, plus bas.

### Test discriminant

Réécrire le même contenu pour deux buts opposés, registre et relation constants : « informer » et «
faire réagir ». Si la densité d'intensifieurs et de marqueurs d'attitude bouge, c'est de la posture.
Si elle est écrasée par le genre quelle que soit la relation, c'est un plafond de registre. Si elle
est identique dans les deux cas, c'est de la Voix.

---

## Composante 3. Droit à affirmer

### Définition

Position que le scripteur revendique sur le territoire de connaissance en jeu : se pose-t-il comme
celui qui sait, comme l'égal, ou comme celui qui demande ? Distincte de la composante 1 : une
assertion prudente sur son propre territoire n'a pas le même effet qu'une assertion assurée sur le
territoire du lecteur. Cette composante encode à qui appartient le savoir, la composante 1 encode
combien d'espace laisse la proposition.

### Source

Heritage 2012, « Epistemics in Action », _Research on Language and Social Interaction_ 45(1) : 1-29
(référence vérifiée). Distinction _epistemic status_ (K+ / K−, donnée de contexte) et _epistemic
stance_ (affichée par la forme morphosyntaxique). Heritage soutient que le statut prime sur la
posture affichée dans la constitution de l'action, et que la posture peut dissimuler le statut ;
cette seconde thèse est reprise du résumé de l'article, pas du texte primaire. Complété par les
_self-mentions_ et _directives_ de Hyland 2005 (vérifié).

Note de notation : Heritage écrit K+ et K− et traite l'écart comme un gradient. Le « K= » employé
dans ce skill est une commodité pour désigner la zone de symétrie, pas une catégorie de la source.

### Marqueurs observables

- Revendication haute (K+ joué) : déclaratives portant sur le territoire du lecteur ; directives («
  notons que », « il faut voir X comme », impératifs d'orientation) ; définitions et gloses non
  sollicitées d'un terme que le lecteur maîtrise ; auto-mention en source d'autorité (« d'après mon
  expérience »).
- Revendication basse (K− joué) : interrogatives portant sur le territoire du lecteur ; marquage
  évidentiel de seconde main (« d'après ce que j'ai compris », « je n'ai pas testé mais ») ;
  concession explicite de territoire (« tu connais mieux le sujet »).
- Symétrie (K=) : assertions sourcées symétriquement, absence de gloses, absence de directives.

Comptable : gloses non sollicitées et directives pour 1000 mots, rapportées au nombre de
propositions portant sur le territoire du lecteur.

Transposition : les trois positions et le comptage des gloses et directives se transposent. Le
marquage évidentiel est fortement dépendant de la langue, certaines langues le grammaticalisent :
catégorie à re-dériver.

### Ce qui la fait varier

Contextuelle. Varie selon l'écart de savoir réel (entrée K) et selon le but. La dissociation entre
les deux est le mécanisme de la posture non authentique : un scripteur K+ peut jouer K−, un
scripteur K= peut jouer K+.

### Test discriminant

Écrire la même proposition factuelle pour un expert du domaine, puis pour un novice, registre
constant. Compter les gloses non sollicitées et les directives. Si ça bouge, posture. Si le genre
les impose quoi qu'il arrive (un blog de vulgarisation glose toujours), registre.

Contre-test utile : demander à la personne d'écrire pour un expert sur un sujet où elle en sait
davantage que lui. Si les gloses reviennent malgré l'expertise du lecteur, c'est un tic de Voix.

---

## Composante 4. Franchise

### Définition

Quantité de menace de face que le scripteur assume au lieu de l'atténuer, lorsqu'il commet un acte
socialement risqué : désaccord, refus, correction, demande, critique. C'est l'axe du risque social,
là où la composante 1 est l'axe du risque épistémique.

### Source

Brown & Levinson 1987, _Politeness: Some Universals in Language Usage_, Cambridge University Press,
d'abord paru en 1978 dans Goody (éd.). Référence vérifiée.

Le contenu interne du livre est [PARTIELLEMENT VÉRIFIÉ] : les cinq super-stratégies et le calcul du
poids d'un acte menaçant Wx = D + P + Rx sont attestés par des sources secondaires concordantes,
mais le texte primaire est sous paywall et n'a pas été lu. Il sert donc de cadre conceptuel et
jamais de preuve. La numérotation des stratégies de politesse positive et négative n'est citée nulle
part dans ce skill : les règles qui s'y adossaient sont énoncées sur leur propre raisonnement.

La scission face positive / face négative est bien de Brown & Levinson. La notion de face elle-même
vient de Goffman 1955, « On Face-Work », _Psychiatry_ 18(3) : référence vérifiée, texte primaire non
lu, avec Hu 1944 comme antécédent revendiqué.

Le point qui porte le plus de poids dans ce modèle ne dépend d'aucune numérotation : substituer une
interrogative à une assertion atténue l'acte menaçant. Le raisonnement tient seul. Une assertion
impose au lecteur une proposition sur laquelle il doit se prononcer ; une question lui laisse la
main, y compris celle de répondre qu'il avait prévu le cas. Cette issue non coûteuse est ce qui
abaisse le coût social de l'acte. C'est pour cette raison que la forme interrogative compte sur cet
axe en plus de compter sur les composantes 1, 3 et 6.

### Marqueurs observables

- Acte réalisé sans atténuation : impératif nu, « non », « c'est faux », « ça ne marchera pas »,
  désaccord asserté sans préface.
- Atténuation par évitement d'imposition : conditionnel de politesse [FR] ; forme interrogative
  substituée à une assertion ; pessimisme (« je ne suis pas sûr que ce soit possible ») ;
  minimisation (« juste une petite remarque ») ; déférence ; excuse préalable ; impersonnalisation
  (« il faudrait » plutôt que « tu devrais ») ; nominalisation ; mise en règle générale (« la
  procédure veut que »).
- Évitement de l'attribution de l'acte : allusion, litote, ironie, question rhétorique sans
  destinataire assigné.

Comptables : ratio préfaces d'atténuation / actes menaçants ; nombre d'actes menaçants réalisés sans
aucune atténuation, pour 1000 mots.

Transposition : les trois régimes (assumé, atténué, évité) se transposent, ce sont des fonctions. Le
conditionnel de politesse, la déférence par le pronom et les formules d'excuse se re-dérivent : leur
poids social varie fortement d'une langue et d'une culture à l'autre, et le seuil personnel extrait
sur un corpus français ne se transporte pas tel quel.

### Ce qui la fait varier

Contextuelle. Varie avec le poids de l'acte, donc avec les entrées D et P, et avec la gravité de
l'acte lui-même. Cette gravité (Rx) n'est pas une entrée d'audience : c'est une propriété de l'acte
à commettre, et elle relève la dose de franchise attendue dans n'importe quelle posture. Le seuil
personnel, le poids à partir duquel une personne bascule d'un régime au suivant, est la calibration
à extraire.

### Test discriminant

Test B, en faisant varier P seul : même critique adressée à un pair, puis à un supérieur
hiérarchique, puis à un client, registre constant (email). Si le nombre d'atténuateurs bouge,
posture.

Test A en miroir : même critique au même pair, en email puis en revue de code puis en rapport
post-mortem. Si seule la forme de l'atténuation change alors que la quantité reste stable, le
registre borne les réalisations et la dose reste de la posture.

Piège français à traiter explicitement : le conditionnel compte sur cet axe et sur la composante 1.
Le désambiguïser par la présence ou l'absence d'un acte menaçant dans la même phrase.

---

## Composante 5. Proximité construite

### Définition

Quantité d'intimité et de terrain commun que le texte fabrique, indépendamment de l'entrée D. Le
scripteur construit le lecteur soit comme un familier partageant ses références, soit comme un
inconnu à qui tout doit être posé. C'est la contrepartie « face positive » de la composante 4, qui
est la contrepartie « face négative ».

Le nom de cette composante est contraint : voir la règle de nommage en tête de fichier. Elle est le
cas d'école du partage entrée / valeur jouée, et l'endroit où une confusion de couche coûte le plus
cher.

### Source

Brown & Levinson 1987, politesse positive, c'est-à-dire les stratégies orientées vers le désir
d'être apprécié et inclus : marqueurs d'identité de groupe, recherche de l'accord, présupposition
d'un terrain commun, plaisanterie, inclusion du locuteur et du destinataire dans une même activité.
Liste [PARTIELLEMENT VÉRIFIÉ], attestée par sources secondaires concordantes, primaire non lue, et
volontairement donnée sans numérotation. Complétée par les _appeals to shared knowledge_ et
_personal asides_ de Hyland 2005 (vérifié).

### Marqueurs observables

Comptable pour 1000 mots.

- Tutoiement ou vouvoiement [FR] ; « on » inclusif [FR] ; « nous » inclusif.
- Marqueurs d'in-group : jargon de métier non glosé, apocopes [FR] (« appli », « conf », « prod »),
  sigles internes, argot professionnel, références culturelles partagées.
- Appels au savoir partagé : « on sait tous que », « le classique X », « comme d'hab ».
- Humour et plaisanterie. C'est ici que vit l'humour, pas dans la Voix. La Voix peut porter une
  direction (« l'humour sert le recul analytique plutôt que la connivence ») ; la quantité d'humour
  et le choix des destinataires sont une dose, donc de la posture.
- Asides personnels : parenthèses de commentaire personnel interrompant l'argument.
- Ellipses présupposant un socle commun : phrases nominales, sous-entendus non explicités.

Transposition : les catégories fonctionnelles (marquage d'in-group, appel au savoir partagé, humour,
aside) se transposent. L'opposition tutoiement / vouvoiement et les apocopes sont marqués `[FR]` :
l'anglais réalise l'écart de familiarité par d'autres moyens (prénom contre titre, contractions,
registre lexical), à re-dériver intégralement.

### Ce qui la fait varier

Contextuelle. Varie avec l'entrée D, mais surtout avec la décision de traiter ou non cette entrée
comme plus faible qu'elle n'est : c'est là toute l'action posturale.

### Test discriminant

Écrire le même contenu pour un collègue proche, puis pour un inconnu du même métier, registre
constant. Compter tutoiement, marqueurs d'in-group et plaisanteries. Si ça bouge, posture.

Piège à vérifier explicitement : si les plaisanteries restent constantes quelle que soit la relation
et quel que soit le registre, c'est un trait de Voix. Sinon c'est de la posture. C'est un point de
fuite fréquent, l'humour étant régulièrement écrit dans les fichiers de voix alors qu'il réalise un
axe interpersonnel.

---

## Composante 6. Adresse au lecteur

### Définition

Degré auquel le destinataire existe grammaticalement dans le texte comme participant plutôt que
comme spectateur. Indépendante des composantes 1 et 5 : un texte peut être maximalement ouvert
dialogiquement tout en étant sans lecteur (un papier de recherche), ou dialogiquement verrouillé
tout en interpellant sans arrêt (un post d'opinion).

### Source

Hyland 2005, « Stance and engagement: a model of interaction in academic discourse », _Discourse
Studies_ 7(2) : 173-192 (vérifié). Corpus de 240 articles de recherche, 8 disciplines, plus
entretiens d'informateurs. Le volet _engagement_ comprend cinq ressources : _reader pronouns_,
_directives_, _questions_, _appeals to shared knowledge_, _personal asides_. Cette composante ne
retient que l'adresse grammaticale proprement dite : les deux dernières ressources sont rangées en
composante 5, les directives en composante 3.

### Marqueurs observables

Comptable pour 1000 mots.

- Pronoms de deuxième personne : tu, vous, ton, ta, tes, votre, vos.
- « Nous » et « on » inclusifs du lecteur, à désambiguïser du « on » impersonnel [FR] : « on observe
  que » est de l'effacement, « on a tous connu ça » est de l'adresse.
- Questions directement adressées au lecteur.
- Impératifs adressés au lecteur.
- Apostrophes et interpellations.
- À l'inverse : passif, tournures impersonnelles (« il apparaît que »), nominalisations, absence
  totale de deuxième personne.

Transposition : le comptage de la deuxième personne se transpose, mais pas sa valeur. Une langue à
distinction T/V compte deux formes là où l'anglais en compte une, et les densités brutes ne sont
donc pas comparables entre langues. La catégorie « inclusif du lecteur » se transpose, les pronoms
qui la réalisent se re-dérivent.

### Ce qui la fait varier

Fortement contrainte par le registre, puis contextuelle dans les bornes restantes. C'est la
composante la plus plafonnée par le genre, ce qui en fait le meilleur test de la frontière Posture /
Registre.

### Test discriminant

Test A d'abord, parce qu'il est décisif ici : même relation, même but, registre email puis papier de
recherche. Si la deuxième personne disparaît entièrement, le registre fixe un plafond, et ce qui
reste sous ce plafond est de la posture.

Test B ensuite, à l'intérieur d'un registre qui autorise l'adresse : si la densité de deuxième
personne bouge selon la relation, posture confirmée.

---

## Composante 7. Prise en charge énonciative

### Définition

Degré auquel le scripteur se donne comme celui dont le texte exprime réellement les positions, par
opposition à celui qui se contente de les formuler ou de les mettre en scène. C'est la seule
composante dont la valeur ne se déduit d'aucune entrée de relation : elle est fixée par le but seul.
Elle rend possible une posture délibérément non authentique.

### Source

Goffman 1979, « Footing », _Semiotica_ 25(1-2) : 1-29, repris dans _Forms of Talk_ (1981). Vérifié.
Le _production format_ décompose le locuteur en trois rôles qui se dissocient :

- _animator_, celui qui produit matériellement l'énoncé ;
- _author_, celui qui en choisit les mots ;
- _principal_, celui dont les positions et les croyances y sont exprimées.

Une posture de performance est celle où _animator_ et _author_ coïncident avec le scripteur alors
que _principal_ ne coïncide que partiellement : il énonce et il formule, mais il ne répond pas
pleinement des convictions énoncées. Adossé à Heritage 2012 sur la dissimulation du statut
épistémique par la posture affichée. Bornes normatives chez Booth 1963, « The Rhetorical Stance »,
_College Composition and Communication_ 14(3) : 139-145, texte intégral lu.

### Portée de la suspension, et ce qui n'est jamais suspendable

C'est cette composante qui fonde le champ `suspend:` des fiches de posture. Elle en fixe aussi la
limite, et la limite est dure.

La suspension est à portée partielle, jamais globale. Le rôle de _principal_ se suspend par portée :
une posture de performance peut n'être _animator_ et _author_ que sur le cadrage tout en restant
_principal_ sur le contenu propositionnel. Le modèle ne prévoit aucune suspension globale.

Il en découle que l'Étape 0, la vérification factuelle, n'est jamais suspendable, y compris en
posture `provocateur`. La friction porte sur l'angle de la discussion, jamais sur l'exactitude d'un
fait avancé. Le maintien du rôle de _principal_ sur le contenu propositionnel a exactement ce sens :
la règle ne s'ajoute pas par-dessus le modèle, elle en découle.

Troisième conséquence : ce que `suspend:` nomme est une direction sur un axe, jamais une forme. Une
posture suspend « une direction d'expansion dialogique sur la composante 1 », pas « le réflexe de la
question ». Un invariant de Voix qui nomme une forme interpersonnelle est déjà mal placé, et le
déclarer suspendu reconduirait l'erreur au lieu de la corriger.

### Marqueurs observables

- Prise en charge pleine : auto-mention en position de source (« je pense que », « mon avis est ») ;
  absence de cadre de mise à distance ; assertions non encadrées.
- Prise en charge partielle : cadres de désengagement explicites (« je joue l'avocat du diable », «
  hypothèse : », « pour lancer le débat », « disons que ») ; questions rhétoriques laissées sans
  réponse par le scripteur ; attribution distanciante appliquée à sa propre position ; changements
  de _footing_ internes au texte, passage d'une voix d'auteur à une voix de personnage ;
  provocations non suivies d'un engagement personnel.
- Signal fort de mise en scène : une position contractive (composante 1) combinée à un cadre de
  désengagement dans le même paragraphe.

Cette composante se compte mal. Les cadres de désengagement sont rares et leur absence ne prouve
rien : un texte entièrement performatif peut n'en contenir aucun. Le test ci-dessous, qui est
déclaratif, prime sur le comptage.

Transposition : les rôles de Goffman et la notion de cadre de désengagement sont universels. Les
formules qui réalisent ces cadres se re-dérivent par langue.

### Ce qui la fait varier

Contextuelle, et pilotée par le but seul. Ne varie ni avec l'écart de savoir ni avec l'entrée D.
Sans elle, une posture de performance serait indistinguable d'une posture sincère de mêmes
coordonnées.

### Test discriminant

Poser la question directement : « si le lecteur te répondait _tu le penses vraiment ?_,
répondrais-tu oui sans réserve ? ». Une réponse négative signale une prise en charge partielle, donc
une posture de performance.

Test C associé : un trait qui disparaît en posture de performance alors qu'il survit aux tests A et
B partout ailleurs est un invariant de Voix suspendu par préséance, pas une calibration de posture.

Bornes normatives à poser explicitement, en reprenant Booth : la prise en charge partielle dérive
vers l'_advertiser's stance_, « undervaluing the subject and overvaluing pure effect », et vers
l'_entertainer's stance_, « the willingness to sacrifice substance to personality and charm ». Test
praticable : si le contenu propositionnel a été modifié pour servir l'engagement, la borne est
franchie.

---

## Sources

Vérifiées, texte primaire lu quand indiqué.

1. Martin, J.R. & White, P.R.R. (2005). _The Language of Evaluation: Appraisal in English_.
   Basingstoke et New York : Palgrave Macmillan. DOI 10.1057/9780230511910. Chapitre 3. Texte
   primaire lu (chapitre échantillon, prrwhite.info).
2. White, P.R.R. (2003). « Beyond modality and hedging: A dialogic view of the language of
   intersubjective stance ». _Text_ 23(2) : 259-284. DOI 10.1515/text.2003.011. Quelques bases
   indiquent 23(3), divergence signalée.
3. Hyland, K. (2005). « Stance and engagement: a model of interaction in academic discourse ».
   _Discourse Studies_ 7(2) : 173-192. DOI 10.1177/1461445605050365.
4. Heritage, J. (2012). « Epistemics in Action: Action Formation and Territories of Knowledge ».
   _Research on Language and Social Interaction_ 45(1) : 1-29. DOI 10.1080/08351813.2012.646684.
   Référence vérifiée ; la thèse de dissimulation du statut est reprise du résumé.
5. Goffman, E. (1979). « Footing ». _Semiotica_ 25(1-2) : 1-29 ; repris dans _Forms of Talk_ (1981),
   University of Pennsylvania Press.
6. Booth, W.C. (1963). « The Rhetorical Stance ». _College Composition and Communication_ 14(3) :
   139-145. Texte intégral lu. Pagination par terme non fiabilisable, la mise en page à deux
   colonnes désordonne l'extraction : aucun numéro de page n'est donné par terme.
7. Lakoff, G. (1973). « Hedges: A study in meaning criteria and the logic of fuzzy concepts ».
   _Journal of Philosophical Logic_ 2(4) : 458-508. Origine du terme _hedge_.
8. Kiesling, S.F. (2009). « Style as Stance », dans A. Jaffe (éd.), _Stance: Sociolinguistic
   Perspectives_, Oxford University Press, pp. 171-194.
9. Bucholtz, M. & Hall, K. (2005). « Identity and interaction: a sociocultural linguistic approach
   ». _Discourse Studies_ 7(4-5) : 585-614. DOI 10.1177/1461445605054407. Source de référence pour
   la _stance accretion_.
10. Brown, P. & Levinson, S.C. (1987). _Politeness: Some Universals in Language Usage_. Cambridge :
    Cambridge University Press. Référence vérifiée ; première parution 1978 dans E. Goody (éd.),
    _Questions and Politeness_.
11. Goffman, E. (1955). « On Face-Work ». _Psychiatry_ 18(3) : 213-231 ; repris dans _Interaction
    Ritual_ (1967). Référence vérifiée, texte primaire non lu.
12. Hu, H.C. (1944). « The Chinese Concepts of "Face" ». _American Anthropologist_ 46(1) : 45-64.
    Référence vérifiée, texte primaire non lu.

Partiellement vérifiées : référence solide, détail interne attesté par des sources secondaires
concordantes, texte primaire non lu.

13. Brown & Levinson 1987, contenu interne : les cinq super-stratégies et le calcul Wx = D + P + Rx.
    Le primaire est sous paywall. Utilisé comme cadre, jamais comme preuve. La numérotation des
    stratégies n'est citée nulle part.
14. Halliday, M.A.K. (1978). _Language as Social Semiotic_. Londres : Edward Arnold. _Field_,
    _tenor_, _mode_, cités en secondaire.

Non vérifiées.

15. Rauniomaa, M. (2003), _stance accretion_ : [NON VÉRIFIÉ], mémoire de master non publié
    (Université d'Oulu), connu uniquement via Bucholtz & Hall 2005, qui attribue le concept à Du
    Bois (2002), communication de conférence, [NON VÉRIFIÉ] également.
16. Bakhtine et Volochinov, dialogisme et hétéroglossie : [NON VÉRIFIÉ] directement, connus via
    Martin & White 2005 et White 2003.
