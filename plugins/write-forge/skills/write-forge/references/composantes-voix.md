# Composantes de la Voix

Les huit composantes du noyau personnel. Ce fichier sert à un agent qui lit un corpus, relève des
traits et doit les ranger. Il donne, par composante, ce qu'il faut chercher, comment savoir qu'on ne
s'est pas trompé de composante, et sous quelle forme encoder le résultat.

La règle de placement entre couches vit dans `modele-concepts.md`. Ne rien encoder sans avoir fait
passer le trait par le test de tri qui s'y trouve.

## Comment lire ces fiches

Six champs par composante : nom, définition, source, marqueurs observables, invariante ou
contextuelle, test discriminant.

**« Invariante » veut dire tendance par défaut stable, qu'une posture peut surcharger en le
déclarant.** Jamais une invariance inconditionnelle. Aucun gabarit livré ne doit énoncer un trait de
voix comme valant indépendamment de la posture active.

**Les marqueurs sont des indices, pas des encodages.** Un marqueur se compte dans le corpus pour
inférer une direction. La direction s'encode. La forme comptée ne s'encode pas, dès lors qu'elle
figure dans les listes de marqueurs de `composantes-posture.md` et qu'elle a une fonction
interpersonnelle. Les fiches 4 à 8 signalent les marqueurs concernés.

**Les marqueurs cités en français sont des exemples de langue, pas la définition du trait.** Le
protocole est paramétré par la langue du corpus. Chaque principe s'énonce indépendamment de la
langue : « arbitrages stables entre quasi-synonymes grammaticaux » vaut partout, « car contre parce
que » est l'instanciation française. Une instance dans une autre langue reconstruit la liste de
marqueurs et garde le principe.

**Il n'y a pas d'ensemble de comparaison.** Aucune norme de groupe n'est disponible. Les trois
substituts, par ordre de fiabilité décroissante : les textes de la personne d'un genre à l'autre,
qui servent de référence interne ; la norme d'un genre telle que le fichier de registre la déclare ;
la réécriture neutre produite par l'agent. Ce dernier substitut porte une limite structurelle à
répéter dans les fichiers livrés : **tout trait que la personne partage avec le modèle reste
invisible**.

**L'ordre des huit va du moins conscient au plus conscient**, ce qui est aussi l'ordre de difficulté
d'élicitation. Les premières s'observent sur corpus, les dernières se discutent.

Deux mises en garde générales sur les sources. Tout le travail d'attribution cité porte sur
l'anglais ; la transférabilité au français et aux autres langues est plausible et non vérifiée.
Burrows relève de la stylistique computationnelle et non de la linguistique forensique : le
regrouper avec Coulthard mélange deux traditions aux standards de preuve différents.

## 1. Substrat

**Définition.** Les préférences grammaticales et sub-lexicales hors du contrôle conscient :
fréquences relatives de mots-outils, n-grammes de caractères, arbitrages systématiques entre
quasi-synonymes grammaticaux. Composante **diagnostique et non générative** : elle sert à vérifier
qu'un brouillon sonne juste, pas à écrire une consigne.

**Source.** Mosteller & Wallace 1963 pour la méthode par mots-outils. Grieve 2007, qui compare 39
types de mesures et trouve les bigrammes et trigrammes de caractères meilleurs marqueurs isolés.
Koppel, Schler & Argamon 2009 pour la synthèse. Burrows 2002 pour la mesure Delta. Stamatatos 2013
pour la robustesse hors domaine.

**Marqueurs observables.** Rien ne se voit à l'œil nu sur un texte isolé : il faut un corpus et une
comparaison. Fréquences de prépositions, déterminants, conjonctions et pronoms rapportées à une
référence. Distribution des n-grammes de caractères de longueur 2 à 4. Arbitrages stables entre
paires équivalentes. Exemples français : « car » contre « parce que », « ceci » contre « cela »,
maintien ou chute du « ne » de négation à l'écrit familier, « afin de » contre « pour ».

**Invariante ou contextuelle.** La plus stable en théorie, la plus incertaine en pratique.
Stamatatos 2013 part du constat que la quasi-totalité des études d'attribution testent le cas
facile, où entraînement et test se ressemblent en genre, en sujet et en distribution. Son résultat,
tel que l'éditeur le résume : les n-grammes de caractères captent mieux le style que les mots très
fréquents quand entraînement et test diffèrent sensiblement. Le Substrat reste donc exploitable hors
domaine, mais pas avec n'importe quelle famille de traits. **[NON VÉRIFIÉ]** : chiffres non
consultés, article non lu en texte intégral.

**Test discriminant.** Contre le Lexique de prédilection : supprimer tous les mots de contenu, ne
garder que mots-outils et ponctuation. Le trait qui survit est du Substrat, celui qui disparaît est
lexical. Contre l'Empan : redécouper les phrases sans changer un seul mot. Le Substrat est invariant
sous cette manipulation, l'Empan non.

**Encodage.** Aucun. Cette composante alimente le script de réfutation, pas le fichier de voix. Une
élicitation qui part de la stylométrie produit des traits que la personne ne peut pas vérifier et
que le modèle ne peut pas appliquer.

## 2. Signature typographique

**Définition.** L'usage personnel des signes qui ne sont pas des mots : ponctuation, symboles,
capitalisation, espacement, balisage, emoji. Coût d'exécution nul et visibilité maximale, ce qui les
rend très discriminants et très faciles à imiter ou à supprimer.

**Source.** Chaski 2001 pour l'évaluation empirique des techniques d'identification fondées sur la
langue. Grieve 2007, qui classe la fréquence des signes de ponctuation parmi les mesures efficaces,
contrairement à la longueur de phrase.

**Marqueurs observables.** Slash `/` compressant une alternative. Flèche `=>` en connecteur.
Point-virgule employé ou jamais. Parenthèses contre tirets pour l'incise. Majuscule ou non après
deux-points. Guillemets français contre anglais. Gras dans un texte courant. Listes à puces contre
paragraphes. Code inline sur des mots qui ne sont pas du code.

**Invariante ou contextuelle.** Nominalement stable, en pratique la plus sensible au support. Un
canal sans balisage supprime mécaniquement la moitié des marqueurs. C'est donc la composante où la
frontière Voix / Registre se joue le plus souvent, et celle où un corpus collecté sur un seul canal
trompe le plus.

**Test discriminant.** Contre le Registre : transposer le même contenu dans deux supports aux
conventions opposées, Markdown libre et texte brut contraint. Le marqueur qui survit aux deux est de
la Voix ; celui qui disparaît avec le support était une affordance du support. Contre le Geste
rhétorique : remplacer le signe par sa paraphrase lexicale. Si le mouvement de pensée reste intact
et que seule la densité change, c'est typographique. S'il disparaît, le signe véhiculait un geste, à
reclasser en composante 5.

**Encodage.** Directement exécutable, signe par signe, avec son statut d'endossement. C'est ici que
se range le résultat du filtre d'intentionnalité, et c'est ici que vit la distinction entre un
marqueur accepté et un trait observé mais non endossé, avec le registre où il reste toléré.

## 3. Empan

**Définition.** L'amplitude et la densité par défaut : longueur des phrases et des paragraphes, taux
de subordination contre juxtaposition, quantité de texte jugée nécessaire pour un contenu donné. La
« concision par défaut » est une valeur d'Empan, et non une composante à part.

**Source.** Grieve 2007, pour l'avertissement empirique : longueur de phrase et longueur de mot sont
de **mauvais** discriminants pris isolément. La formulation en delta ci-dessous ne vient d'aucune
source ; elle découle de l'ordre de préséance posé dans `modele-concepts.md`.

**Marqueurs observables.** Distribution des longueurs de phrase, pas moyenne. Présence ou absence de
phrases très courtes isolées en fin de paragraphe. Ratio principales sur subordonnées. Longueur de
la réponse rapportée à la longueur de la question. Existence ou non d'un paragraphe de synthèse
final. Tolérance aux répétitions de reformulation.

**Invariante ou contextuelle.** Contextuelle en valeur absolue, stable en écart. La longueur absolue
est dictée par le Registre. Ce qui persiste, c'est la position relative : systématiquement plus
court que la norme du genre, par exemple.

**Encodage, règle dure.** L'Empan s'encode **en delta relatif à la norme d'empan du registre, jamais
en valeur absolue**. Un nombre de mots écrit dans un fichier de voix écrase une contrainte de
registre depuis la couche la plus basse, ce que la préséance interdit. Écrire « environ 30 % plus
court que la norme du genre », pas « 400 mots ». Cela suppose que le fichier de registre déclare sa
norme : c'est un point de contrat entre les deux fichiers, spécifié dans `contrats-interface.md`.
C'est la seule composante qui peut entrer en collision frontale avec le Registre.

**Test discriminant.** Contre le Registre : mesurer la longueur du texte rapportée à la norme du
genre, prise dans le fichier de registre à défaut d'un ensemble de comparaison réel. Ratio du même
signe d'un genre à l'autre, c'est un trait d'Empan. Ratio qui change de signe selon le genre, il n'y
a pas de trait à encoder. Contre le Réflexe interpersonnel : vérifier si la brièveté augmente avec
le désaccord ou l'inconfort. Si elle covarie avec l'enjeu social, c'est un comportement de posture.

## 4. Lexique de prédilection

**Définition.** Les mots et surtout les **cooccurrences** que la personne mobilise plus souvent que
la norme, y compris les domaines-sources où elle va chercher ses images.

**Source.** Coulthard 2004, dont la méthode repose sur « the proportion of shared vocabulary and the
number and length of shared phrases », donc sur le syntagme plutôt que sur le mot isolé. Nini &
Grant 2013 et Nini 2023 pour le cadre théorique de l'individualité linguistique, **[NON VÉRIFIÉ]**
quant au contenu, cités comme références.

**Marqueurs observables.** Verbes de raisonnement récurrents (exemples français : « ça revient à »,
« ça tient à »). Champ d'où viennent les métaphores : mécanique, biologie, jeu, réseau, cuisine,
sport. Mélange de registres lexicaux, un mot familier planté dans une phrase formelle. Anglicismes
techniques conservés ou traduits.

**Passage obligé par le filtre de forme.** Les adjectifs d'évaluation préférés et les intensifieurs
figurent dans les marqueurs d'Intensité évaluative, composante de posture. Le partage se fait sur «
quel mot » contre « combien » : le choix de « bancal » plutôt que « fragile » est du Lexique, le
nombre d'évaluations affichées par millier de mots est une dose de Posture. Encoder la préférence
lexicale, jamais la densité.

**Invariante ou contextuelle.** Mixte, et il faut séparer. Le domaine-source des images et les
préférences lexicales d'évaluation sont stables. Le vocabulaire technique est massivement contextuel
: il suit le sujet et l'écart de savoir. Retirer le lexique thématique avant toute conclusion.

**Test discriminant.** Contre le simple effet de sujet : comparer deux textes de la personne sur
deux sujets sans recouvrement. Un mot qui survit au changement de sujet est du Lexique, sinon c'est
du thème. Contre le Regard : le domaine-source d'une métaphore relève du Lexique s'il est
**interchangeable sans rien changer à l'argument**. S'il porte l'argument, c'est-à-dire si en
changer modifie ce que le texte affirme du monde, il relève du Regard.

**Angle mort.** Un profil de voix rédigé par simple entretien la laisse **vide** : personne ne pense
à demander son domaine-source métaphorique habituel. Le protocole d'extraction doit la viser
activement : sans question dédiée, elle ne remonte pas.

## 5. Geste rhétorique

**Définition.** Le mouvement de pensée court que la personne rejoue plusieurs fois à l'intérieur
d'un même texte, indépendamment du plan d'ensemble. Poser une image forte puis la démonter en est
un. Un geste est **local et répétable**, ce qui le sépare de l'Architecture, qui ne se joue qu'une
fois par texte.

**Source.** Biber & Conrad 2009 pour la justification du classement : un trait non motivé
fonctionnellement par la situation relève du style, donc de la personne. **[NON VÉRIFIÉ]** : aucun
construct nommé ne recouvre exactement ce niveau dans la littérature consultée. **« Geste rhétorique
» est une étiquette forgée ici**, pas un terme établi. Le niveau tombe entre le _foregrounding_ de
la stylistique et l'analyse de genre en _moves_, sans terme dédié. Ne pas le présenter comme un
concept reçu.

**Marqueurs observables.** Image forte suivie d'un paragraphe de décorticage. Concession
systématique avant l'objection. Exemple avant la règle plutôt que l'inverse. Reformulation immédiate
de toute notion technique introduite. Chiffre systématiquement suivi de sa mise à l'échelle.

**Passage obligé par le filtre de forme.** « Question rhétorique suivie de sa propre réponse » est
un marqueur fréquent de ce niveau, et « question rhétorique » figure dans les marqueurs de Franchise
(pôle off record) et de Prise en charge énonciative. Le compter comme indice, puis vérifier dans le
corpus ce que la question y fait. Si elle sert à éviter d'assumer ou à laisser une position ouverte,
elle réalise un axe interpersonnel et la dose descend en Posture. Si elle sert seulement
l'exposition, encoder le geste sans nommer la forme : « poser le problème avant de le résoudre, dans
le même paragraphe ».

**Invariante ou contextuelle.** Stable comme disposition, contextuelle en fréquence. Un registre à
format serré réduit le nombre d'occurrences sans supprimer le geste.

**Test discriminant.** Contre l'Architecture : compter les occurrences par texte. Un geste apparaît
plusieurs fois dans un texte long, une architecture apparaît une fois. Contre la Signature
typographique : réécrire le passage en supprimant tout signe non alphabétique. Si le mouvement
subsiste, c'est un geste. Contre le Regard : demander si le geste servirait aussi bien à défendre la
position inverse. Si oui, c'est une procédure, donc un geste. Si non, c'est un Regard déguisé en
procédure.

**Encodage.** La plus générative des huit. Un geste s'écrit comme une consigne exécutable, ce qui en
fait la composante au meilleur rendement pour le temps d'élicitation investi.

## 6. Architecture du propos

**Définition.** L'ordre par défaut dans lequel la personne dispose ses éléments **quand le genre lui
laisse le choix** : conclusion d'abord ou construction progressive, place du bémol, forme de la
clôture, tolérance à la digression. Le genre impose une structure obligatoire ; l'architecture est
ce que la personne fait de la marge restante.

**Source.** Biber & Conrad 2009, pour la séparation explicite entre perspective genre, « the
conventional structures used to construct a complete text within the variety », et perspective
style, « not functionally motivated by the situational context; rather, style features reflect
aesthetic preferences, associated with particular authors ». C'est cette paire de définitions qui
autorise à découper l'ordre du propos en une part de genre et une part de personne.

**Marqueurs observables.** Thèse en première ou en dernière phrase. Caveat placé avant ou après
l'affirmation qu'il limite. Présence d'un paragraphe « ce que ça ne dit pas ». Longueur du préambule
avant d'entrer dans le sujet. Plan annoncé ou non. Place de l'anecdote, en ouverture ou en
illustration tardive.

**Passage obligé par le filtre de forme.** « Clôture sur une question ouverte » nomme une forme des
listes de posture. L'encodage se fait sur le choix de clôture, pas sur le véhicule : « clore sur une
ouverture plutôt que sur une récapitulation ». La forme que prend cette ouverture est du Registre,
sa quantité est de la Posture.

**Invariante ou contextuelle.** Fortement contrainte par le Registre, et c'est exactement pour ça
qu'il faut l'isoler. Sans elle, on attribue à la Voix ce que le genre imposait, et le skill se
retrouve à répéter une convention de genre sous l'étiquette « voix personnelle ». Ce qui reste
stable, c'est le choix fait là où **deux ordres étaient également acceptables** dans le genre.

**Test discriminant.** Contre le Registre : vérifier que le genre admet bien les deux ordres. Faute
d'ensemble de comparaison, la vérification passe par la réécriture neutre produite par l'agent et
par la norme déclarée dans le fichier de registre, avec la limite connue que ce qui est partagé avec
le modèle reste invisible. Si le genre admet les deux et que la personne en prend toujours un, c'est
de l'Architecture. S'il n'en admet qu'un, il n'y a pas de trait à extraire. Contre le Geste
rhétorique : le comptage d'occurrences de la fiche 5.

**Encodage.** Règle conditionnelle, formulée « si le genre laisse le choix, alors ».

**Angle mort.** Comme le Lexique, elle reste **vide** quand personne ne demande où se place le
bémol. Le protocole d'extraction doit la viser activement.

## 7. Réflexe interpersonnel

**Définition.** La manière habituelle de se situer face au lecteur et face au désaccord. Composante
frontalière avec la Posture, et la seule chose qui la sauve est qu'elle ne porte que la
**direction** : le côté de l'axe vers lequel la personne penche quand rien ne la contraint.

**Cette composante ne porte jamais ni la forme ni la dose.** C'est la règle la plus importante du
fichier, et la plus souvent enfreinte. Ce qu'elle contient ressemble à « devant un désaccord, le
premier mouvement est expansif plutôt que contractif ». Ce qu'elle ne contient jamais : le nom d'une
forme réalisant un axe interpersonnel (question, atténuateur, conditionnel, tutoiement,
auto-mention), et une quantité.

**Articulation avec les composantes de posture.** Chaque direction encodée ici pointe un axe de
`composantes-posture.md` et s'y arrête. La direction dit de quel côté ; la composante de posture
correspondante dit combien, pour quelle relation ; le registre dit par quel moyen. Trois couches
pour un même trait, et le fichier de voix n'en écrit qu'une :

| Direction encodée en Voix                            | Axe de posture qui porte la dose |
| ---------------------------------------------------- | -------------------------------- |
| vers l'expansion dialogique face au désaccord        | Ouverture dialogique             |
| vers la retenue ou la véhémence dans le jugement     | Intensité évaluative             |
| vers la revendication ou la concession de territoire | Droit à affirmer                 |
| vers la franchise assumée ou l'atténuation           | Franchise                        |
| vers la connivence ou la mise à distance             | Proximité construite             |
| vers la présence ou l'effacement du lecteur          | Adresse au lecteur               |
| vers l'endossement plein ou la mise en scène         | Prise en charge énonciative      |

Une posture peut suspendre une de ces directions en la déclarant par un `suspend:`. Sans
déclaration, la direction remplit l'espace que la dose laisse libre.

**Source.** Hyland 2005 pour le modèle _stance_ et _engagement_ et pour les traits comptables qui
l'instancient. Martin & White 2005 pour le nommage des axes d'engagement, contraction contre
expansion dialogique. Ivanič 1998 pour le _self as author_, le degré auquel le scripteur revendique
la paternité de ce qu'il avance.

**Marqueurs observables, à compter et non à encoder.** Ratio questions ouvertes sur
contre-affirmations dans les passages de désaccord. Atténuateurs récurrents (exemples français : «
il me semble », « à vérifier », « je peux me tromper »). Marqueurs d'engagement du lecteur :
deuxième personne, « on » inclusif, impératif d'invitation. Forme du refus, sec ou motivé. Présence
ou absence d'une concession préalable systématique. Chacun de ces marqueurs figure dans les listes
de posture : ils servent à établir de quel côté la personne penche, puis ils restent hors du fichier
de voix.

**Invariante ou contextuelle.** La direction est stable, l'intensité est contextuelle. Le contexte
fixe l'amplitude disponible ; ce qui appartient à la Voix, c'est l'option prise à l'intérieur de
cette amplitude.

**Test discriminant.** Faire varier le **seul** enjeu social, à contenu et genre constants : même
désaccord adressé à un pair, puis à un supérieur, puis à un inconnu. Si le réflexe **s'inverse**, il
est piloté par la situation et relève de la Posture. S'il ne fait que s'atténuer ou s'amplifier en
gardant le même signe, c'est un Réflexe interpersonnel de Voix. Sans ce test, le placement d'un «
réflexe de la question » reste une hypothèse ; le cas est traité de bout en bout dans
`modele-concepts.md`.

## 8. Regard

**Statut : composante optionnelle.** Elle ne s'observe pas sur texte court, et elle ne se renseigne
que si le corpus contient des textes longs. Un email de deux lignes n'en dit rien. C'est un problème
d'échantillonnage sans solution évidente, puisque le skill généré sera surtout sollicité sur des
textes courts. En l'absence de corpus long, laisser la composante vide plutôt que de l'inventer.

**Définition.** La façon constante dont la personne construit le monde dans ses textes : ce qu'elle
traite comme un problème, ce qu'elle trouve digne d'attention, le crédit qu'elle accorde au cadre
dans lequel elle écrit. Ce qui reste quand on a retiré tous les traits de surface.

**Source.** Fowler 1977, qui forge le terme _mind style_ et le définit comme « any distinctive
linguistic presentation of an individual mental self ». Attribution et définition confirmées par
Semino, « Mind Style 25 Years On », Lancaster University. **[NON VÉRIFIÉ]** : pagination chez
Fowler, et référence complète du texte de Semino. Le terme est de Fowler, pas des auteurs qui l'ont
ensuite employé. Ivanič 1998 pour l'_autobiographical self_, l'identité que le scripteur apporte
depuis son parcours, distincte du _discoursal self_ que le texte donne à voir.

**Marqueurs observables.** Ce qui est présenté comme évident contre ce qui est présenté comme
surprenant. Choix des entités mises en position de sujet grammatical : personnes, systèmes,
abstractions. Modalité dominante : obligation, possibilité, probabilité. Ce que la personne juge
inutile de justifier.

**Passage obligé par le filtre de forme.** L'humour est un marqueur récurrent à ce niveau, et il
figure dans les marqueurs de Proximité construite. Le compter comme indice de la relation que la
personne entretient avec le cadre, puis encoder la direction sans le nommer : « prendre de la
distance avec le cadre plutôt que chercher la connivence ». La quantité d'humour et son destinataire
sont une dose de Posture.

**Invariante ou contextuelle.** La plus stable des composantes exploitables, et la plus difficile à
observer.

**Test discriminant.** Contre le Geste rhétorique : l'épreuve de la position inverse de la fiche 5.
Contre la Posture : vérifier si le trait subsiste dans un écrit sans destinataire, notes
personnelles ou brouillon non envoyé. La Posture s'évapore quand il n'y a personne à qui plaire ou
déplaire, le Regard reste.

**Encodage.** Partiel, et il se dégrade vite en slogan. À traiter comme critère de relecture plutôt
que comme consigne de rédaction.

## Générateur contre diagnostique

Distinction opérationnelle qui ne recoupe pas celle de la stabilité, et que le protocole
d'extraction doit rendre explicite sous peine de faire perdre du temps.

| Composante                 | S'écrit comme consigne ?          | Usage                                                  |
| -------------------------- | --------------------------------- | ------------------------------------------------------ |
| 1. Substrat                | non                               | évaluation seulement : comparer un brouillon au corpus |
| 2. Signature typographique | oui, directement                  | règle exécutable                                       |
| 3. Empan                   | oui, en delta relatif au registre | règle paramétrée                                       |
| 4. Lexique de prédilection | oui, en préférences et interdits  | règle exécutable                                       |
| 5. Geste rhétorique        | oui, la plus générative           | règle exécutable                                       |
| 6. Architecture du propos  | oui, en règle conditionnelle      | règle conditionnelle                                   |
| 7. Réflexe interpersonnel  | oui, en direction seule           | direction bornée par la Posture                        |
| 8. Regard                  | partiellement                     | critère de relecture                                   |

Le piège : le Substrat est ce que la littérature mesure le mieux et ce qu'un skill peut le moins
utiliser.

## Ce que le protocole d'extraction doit viser activement

Les trois composantes qu'un profil rédigé par simple entretien laisse vides : **Substrat** (attendu,
elle n'est pas générative), **Lexique de prédilection** et **Architecture du propos**. Les deux
dernières sont des angles morts de l'élicitation, pas des composantes inutiles. Personne n'a demandé
le domaine-source métaphorique habituel ni la place du bémol, donc rien n'est remonté. Un
questionnaire qui ne les cible pas nommément reproduira le même trou.

Deux placements existants restent des hypothèses et non des constats : le réflexe de la question en
composante 7, et la « philosophie de fond » en composante 8. Les manipulations qui trancheraient
sont spécifiées dans les fiches correspondantes et n'ont pas été menées.

## Références

Vérifiées par requête sur le DOI ou auprès de l'éditeur, sauf mention contraire.

- Biber, D. & Conrad, S. (2009). _Register, Genre, and Style_. Cambridge Textbooks in Linguistics,
  Cambridge University Press. DOI 10.1017/cbo9780511814358. 2e éd. 2019, DOI 10.1017/9781108686136.
  Les citations verbatim de la fiche 6 ont été relevées sur l'extrait officiel de l'éditeur.
- Burrows, J. (2002). « 'Delta': a Measure of Stylistic Difference and a Guide to Likely Authorship
  ». _Literary and Linguistic Computing_ 17(3), 267-287. DOI 10.1093/llc/17.3.267. Stylistique
  computationnelle, tradition distincte du forensique.
- Chaski, C. E. (2001). « Empirical evaluations of language-based author identification techniques
  ». _International Journal of Speech, Language and the Law_ 8(1), 1-65. DOI 10.1558/sll.2001.8.1.1.
- Coulthard, M. (2004). « Author Identification, Idiolect, and Linguistic Uniqueness ». _Applied
  Linguistics_ 25(4), 431-447. DOI 10.1093/applin/25.4.431. Résumé consulté chez Oxford Academic.
- Fowler, R. (1977). _Linguistics and the Novel_. Londres : Methuen. Réédition Routledge, DOI
  10.4324/9781315015897. Paternité du terme _mind style_ et définition confirmées par Semino, « Mind
  Style 25 Years On » (Lancaster University). **[NON VÉRIFIÉ]** : pagination, et référence complète
  du texte de Semino.
- Grieve, J. (2007). « Quantitative Authorship Attribution: An Evaluation of Techniques ». _Literary
  and Linguistic Computing_ 22(3), 251-270. DOI 10.1093/llc/fqm020. Résultats utilisés (39 types de
  mesures comparés ; bigrammes et trigrammes de caractères meilleurs marqueurs isolés ; longueur de
  mot et longueur de phrase peu utiles ; fréquences de mots et de ponctuation efficaces) confirmés
  par sources secondaires concordantes, **[NON VÉRIFIÉ]** sur le texte intégral.
- Hyland, K. (2005). « Stance and engagement: a model of interaction in academic discourse ».
  _Discourse Studies_ 7(2), 173-192. DOI 10.1177/1461445605050365.
- Ivanič, R. (1998). _Writing and Identity: The Discoursal Construction of Identity in Academic
  Writing_. Studies in Written Language and Literacy 5, Amsterdam : John Benjamins. Les **quatre**
  aspects du soi sont confirmés par plusieurs sources secondaires concordantes ; **[NON VÉRIFIÉ]**
  sur le texte original.
- Koppel, M., Schler, J. & Argamon, S. (2009). « Computational methods in authorship attribution ».
  _JASIST_ 60(1), 9-26. DOI 10.1002/asi.20961. Crossref date l'enregistrement de 2008 (mise en
  ligne) ; la référence imprimée courante est 2009.
- Martin, J. R. & White, P. R. R. (2005). _The Language of Evaluation: Appraisal in English_.
  Palgrave Macmillan. DOI 10.1057/9780230511910. Chapitre 3, systèmes ENGAGEMENT et GRADUATION, lu
  en texte intégral sur le chapitre-échantillon de l'éditeur. Le système _engagement_ est
  majoritairement le travail de White (2003) ; l'attribuer au seul Martin est courant et inexact.
- Mosteller, F. & Wallace, D. L. (1963). « Inference in an Authorship Problem ». _Journal of the
  American Statistical Association_ 58(302), 275-309. DOI 10.1080/01621459.1963.10500849.
- Nini, A. (2023). _A Theory of Linguistic Individuality for Authorship Analysis_. Cambridge
  University Press. DOI 10.1017/9781108974851. **[NON VÉRIFIÉ]** : contenu, référence seulement.
- Nini, A. & Grant, T. (2013). « Bridging the gap between stylistic and cognitive approaches to
  authorship analysis using Systemic Functional Linguistics and multidimensional analysis ».
  _International Journal of Speech, Language and the Law_ 20(2), 173-202. DOI
  10.1558/ijsll.v20i2.173. **[NON VÉRIFIÉ]** : contenu, référence seulement.
- Stamatatos, E. (2013). « On the Robustness of Authorship Attribution Based on Character N-gram
  Features ». _Journal of Law and Policy_ 21(2), 421-439. Dépôt BrooklynWorks, Brooklyn Law School.
  Motivation et résultat principal relevés sur le résumé éditeur ; **résultats chiffrés non
  consultés**.
