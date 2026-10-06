# Protocole d'extraction

Procédure exécutable, de la personne qui arrive sans rien jusqu'aux fichiers de l'instance écrits.
Elle suppose un agent en session de chat disposant de la lecture de fichiers, du dialogue, d'un
outil de questions à choix multiples (1 à 4 questions par écran, 2 à 4 options par question) et de
l'exécution de scripts Python ou bash qu'il écrit lui-même.

Treize étapes, numérotées de 0 à 12. Coût pour la personne : environ 35 minutes en session, plus 20
à 40 minutes de collecte de corpus hors session. Avec l'entretien approfondi retenu à l'étape 0, 55
à 70 minutes en session, et aucune collecte si la personne n'a pas de texte
(`protocole-entretien.md`).

Collision de noms à connaître avant de lire. L'Étape 0 ci-dessous est le cadrage du protocole
d'extraction. Le skill produit a lui aussi une Étape 0, la vérification factuelle, qui n'est jamais
suspendable. Quand ce fichier parle de la seconde, il l'appelle « l'étape de vérification factuelle
du skill produit ».

## Ce que le protocole ne fait pas

Ce n'est pas de l'attribution d'auteur. Burrows' Delta se définit comme la moyenne des écarts
absolus entre les z-scores d'un texte cible et ceux d'un groupe de textes de référence (Burrows
2002, _Literary and Linguistic Computing_ 17(3), 267-287). Sans autres auteurs, il n'y a pas de
z-score, donc pas de Delta. Le dispositif PAN et les n-grammes de caractères en mode classifieur
sont dans le même cas.

Le cadre correct est le couple consistance × distinctivité posé par Grant (2013, _Journal of Law and
Policy_ 21(2), 467-494). Des deux, seule la consistance est mesurable ici : elle se compte sur le
corpus fourni. La distinctivité demande un ensemble de comparaison, et il n'y en a aucun. Ce que le
protocole met à la place, une réécriture neutre produite par l'agent, est un écart à un défaut de
modèle, pas une mesure. Lire `limites.md` avant de faire confiance au résultat.

## Les quatre règles qui gouvernent toutes les étapes

### Règle 1. Le comptage réfute, il ne découvre pas

La substance du livrable vient de la lecture des mouvements de discours (étape 5) et de l'entretien
(étape 6). Le script de l'étape 3 est un filtre, pas une source.

Le tableau de comptage autorise quatre gestes, et quatre seulement : écarter un candidat dont la
fréquence est nulle ou confinée à un seul registre, restreindre un candidat à un registre,
corroborer un candidat venu d'ailleurs, refuser de se prononcer sous le seuil de mots. Il n'en
autorise pas un cinquième, qui serait de proposer un trait.

Le script peut signaler une forme récurrente, qu'il s'agisse d'un marqueur typographique comme le
slash ou d'un lexème qui revient dans plusieurs registres. Cette forme ne devient un candidat que
lorsque l'étape 5 lui trouve une fonction ou que l'étape 6 la fait remonter. Une ligne de tableau
sans fonction identifiée reste une ligne de tableau. La règle vaut pour la signature typographique
comme pour le lexique de prédilection : aucune exception, sinon le comptage redevient une source.

### Règle 2. Règle de preuve

Quatre clauses orientées, à appliquer telles quelles.

1. Une déclaration seule n'ajoute jamais un trait. Revendiqué sans occurrence dans le corpus, il va
   dans `voix-aspirations.md`.
2. Une déclaration seule ne retire jamais un trait. Un désaveu passe par un écran aveugle (étape 7).
3. Un trait qui disparaît à l'auto-révision sort de la Voix, même s'il a passé l'étape 7. Le test de
   survie à l'auto-révision prime sur la préférence déclarée, parce qu'il observe un comportement au
   lieu d'interroger un jugement.
4. Un trait rejeté en écran aveugle sort de la Voix.

Un texte écrit ou marqué pendant l'entretien approfondi (`protocole-entretien.md`, blocs B et C), ou
une réponse libre donnée à un écran, compte comme occurrence, au même titre qu'un item de corpus,
mais plus faible : il est produit sous observation et pour le protocole. Il porte la provenance
`séance` dans `voix.md`, jamais `corpus`. Une déclaration reste une hypothèse, et la clause 1
s'applique sans changement. La clause 3 ne s'applique qu'à une révision observée : un écran qui
propose la phrase avec et sans le trait est un écran de l'étape 7b, pas une révision.

L'asymétrie entre les clauses 1 et 2 est voulue. Désavouer un trait observé est vérifiable : le
trait existe, on teste s'il est voulu. Revendiquer un trait non observé ne l'est pas, il n'existe
nulle part. Le livrable n'est pas un portrait documentaire de la personne, c'est ce qu'elle accepte
d'envoyer sous son nom.

Aucune référence n'est invoquée à l'appui du test de survie à l'auto-révision, et il ne faut pas en
ajouter. Le test tient par son propre raisonnement : ce que la personne retire quand elle se relit
n'est pas ce qu'elle veut envoyer.

### Règle 3. Un seul axe varie par écran et par triplet

Tout écran de choix forcé et tout triplet de calibration écrit dans un fichier de posture fait
varier exactement une composante. Le contenu, le registre, le destinataire et les six autres
composantes restent constants.

Contre-exemple, détaillé dans `catalogue-postures.md` : un triplet de `pair` dont les variantes
s'écartent sur les composantes 1 (ouverture dialogique), 2 (intensité évaluative) et 4 (franchise)
en même temps. Son rejet n'identifie rien : on ignore laquelle des trois déviations a été rejetée,
donc la calibration ne se lit pas.

Conséquence sur les écrans : quatre options au plus, dont trois niveaux de la composante visée, le
niveau extrême servant de distracteur, et une option de rejet global. Conséquence sur les triplets :
un triplet par composante, jamais un triplet par posture.

### Règle 4. Paramétrage par la langue

Le corpus n'est pas forcément en français. Trois couches, à traiter séparément.

Les traits de discours se transposent tels quels. « Poser une image puis la décortiquer », « sonder
par une question plutôt qu'asserter » sont des mouvements rhétoriques, pas des faits lexicaux. C'est
l'argument pour rédiger `voix.md` au niveau du discours et non au niveau du mot.

La catégorie « fréquences de mots-outils » est universelle, la liste ne l'est pas. Le portage
français de LIWC a demandé une reconstruction dédiée, avec modification du logiciel pour les
accents, pour une couverture moyenne d'environ 54 % des mots (Piolat, Booth, Chung, Davids &
Pennebaker 2011, _Psychologie Française_ 56, 145-159). Rybicki & Eder (2011, _LLC_ 26(3), 315-321)
trouvent que le rang optimal des mots à retenir varie par langue et par genre.

Les artefacts typographiques passent pour de la voix. En français, l'espace insécable avant `;` `:`
`?` `!` et les guillemets `« »` sont produits par l'outil. Un script naïf les compte comme des
marqueurs personnels.

Trois annexes dépendent donc de la langue active : la liste de mots-outils, la table de
normalisation typographique et la table de désambiguïsation (étape 3). Elles se régénèrent à chaque
nouvelle langue, elles ne se traduisent pas. Chaque étape qui dépend de la langue le signale
ci-dessous.

## Étape 0. Cadrage, commande de corpus, choix du parcours

L'agent ne sait rien encore. Un écran de quatre questions, 3 minutes :

1. Langue principale d'écriture du corpus.
2. Registres où la personne écrit le plus, en choix multiple sur une liste courte.
3. Volume disponible : « aucun texte », « moins de 5 textes », « 5 à 10 », « plus de 10 ».
4. « Inclure un protocole de questions-réponses et cas d'usage ? » : « oui, inclure » ou « non ». La
   description de l'option « oui » annonce le coût, 30 à 40 minutes de plus, et le recommande quand
   le volume est faible ou nul.

La révision par un tiers ou par une IA se demande item par item à l'étape 1, puis se vérifie à
l'étape 2. Sans texte, elle n'a pas d'objet.

Langue : c'est ici que la langue de travail se fixe. Si le corpus est multilingue, une seule langue
de travail est retenue ; les items dans les autres langues comptent pour le volume mais sont
inéligibles à la Voix (table d'éligibilité, étape 1). L'agent charge ou régénère les trois annexes
de la langue retenue avant l'étape 3.

Les deux dernières réponses fixent le parcours. Les quatre combinaisons sont explicites :

| Volume      | Entretien | Parcours                                                                                                                                                                                                                                                                                              |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| des textes  | non       | Protocole standard. Mode dégradé si les seuils ne sont pas atteignables, annoncé ici.                                                                                                                                                                                                                 |
| des textes  | oui       | Protocole standard, plus la séance de l'entretien approfondi après l'étape 5. L'étape 6 est gardée. Les textes de séance s'ajoutent au corpus.                                                                                                                                                        |
| aucun texte | oui       | Parcours sans corpus. L'entretien démarre tout de suite et produit le matériau, qui passe par les étapes 1 à 5 comme un corpus. L'étape 2 est sans objet (textes écrits devant l'agent, sans IA), l'étape 6 est sautée, et les deux sauts s'écrivent. L'étape 3 tourne, sous les seuils : aucun taux. |
| aucun texte | non       | Squelette. `voix.md` déclaré non extrait, postures calibrées par les seuls écrans de l'étape 9c et marquées non corroborées, registres et audience livrés. L'agent recommande l'entretien avant de partir sur ce parcours.                                                                            |

Le parcours sans corpus a son propre matériau, écrit et corrigé en séance, et sa propre limite : ce
matériau est produit sous observation (`limites.md`, section 11). Il s'annonce à la personne comme
tel, avec son coût en temps.

Le refus s'annonce ici, pas à la fin. Avec des textes et sans entretien, si le volume déclaré ne
peut pas atteindre deux registres, 2 500 mots ou deux contrastes de destinataire, l'agent dit avant
la collecte que le résultat sera un `voix.md` provisoire sans traits de surface et une seule
posture. Il propose alors l'entretien, de continuer en mode dégradé, ou de revenir plus tard avec
davantage. Découvrir le mode dégradé après coup gaspille les 20 à 40 minutes de collecte.

L'agent ne va pas chercher de textes dans une source connectée (messagerie, documents) sans que la
personne le propose ou l'accepte. Un connecteur reste une option, jamais un prérequis du parcours.

Sortie : le parcours retenu, et, s'il y a collecte, la commande de corpus personnalisée ci-dessous,
remise sous forme de liste d'items à déposer, consigne de diversité de destinataires comprise. C'est
elle qu'on oublie.

### Spécification du corpus

La diversification porte sur deux axes croisés, parce que le registre (Kestemont, Luyckx, Daelemans
& Crombez 2012, _English Studies_ 93(3), 340-356) et le destinataire (Bell 1984, _Language in
Society_ 13(2), 145-204) sont deux confondants distincts, tous deux nommés par Grant (2013) comme
conditions de constitution d'un corpus de comparaison. Les deux axes se recouvrent : les items qui
servent l'axe Destinataire sont pris **dans** le registre court, ils ne s'ajoutent pas.

Axe Registre, pour isoler la Voix. Compté en items, pas en textes, parce que deux emails ne font pas
1 500 mots.

| Registre                                                       | À demander                   | Volume attendu |
| -------------------------------------------------------------- | ---------------------------- | -------------- |
| Court et transactionnel (email, message, commentaire de revue) | 10 à 15 items                | ~1 500 mots    |
| Long et argumenté (note, rapport, article, compte rendu)       | 2 textes de 800 à 1 500 mots | ~2 000 mots    |
| Public ou promotionnel (post, présentation, annonce)           | 3 à 5 items                  | ~1 200 mots    |

Axe Destinataire, pour isoler les Postures. Quatre contrastes de relation à demander, pris dans le
registre court, minimum 2 items par contraste : distance faible et pouvoir égal (collègue proche) ;
pouvoir sur la personne (manager, client, jury) ; la personne en sait moins que le lecteur (question
à un expert) ; la personne en sait plus que le lecteur (explication à un junior). Sans cette
consigne, les gens envoient douze emails à leur manager et la variation observée est du registre.

Ces quatre contrastes décrivent des entrées d'Audience (K, P, D), pas des valeurs de posture.

Bonus à fort rendement : 1 ou 2 paires brut / auto-révisé du même texte. C'est le seul matériau qui
tranche les tics sans poser de question. À demander explicitement, la personne n'y pense jamais.

| Configuration   | Items                       | Mots    | Ce qui est produisible                                                      |
| --------------- | --------------------------- | ------- | --------------------------------------------------------------------------- |
| Minimale viable | ~17 (12 + 2 + 3)            | ~4 700  | `voix.md` avec traits de discours et traits de surface attestés, 2 postures |
| Confortable     | ~22 (15 + 2 + 5) + 2 paires | ~8 000  | Le précédent, plus l'arbitrage fiable des tics, 3 à 4 postures              |
| Dégradée        | mono-registre               | < 2 500 | `voix.md` provisoire, traits de discours seuls, aucun taux, 1 posture       |

Le plancher de 1 500 mots par registre vient de Burrows (2002), dont le seuil s'énonce « texts
exceeding about 1,500 words ». La borne de 5 000 mots au total est calée sur Eder (2015, _DSH_
30(2), 167-182), qui trouve un minimum de 2 500 à 5 000 mots indépendamment de la méthode, prise en
haut de fourchette parce que le corpus est réparti sur plusieurs genres. Ces chiffres sont
extrapolés d'un autre cadre, voir `limites.md`. 8 000 mots reste un budget serré et le résultat est
un profil indicatif, pas une signature.

## Étape 1. Dépôt et qualification

La personne dépose, hors session, 20 à 40 minutes. Dans le parcours sans corpus, rien n'est déposé :
les items sont les textes produits aux blocs B et C de l'entretien, support `séance`. L'agent
demande pour chaque item déposé s'il a été relu par un tiers ou écrit avec une IA, puis construit la
table de qualification. Pour chaque item : registre, exprimé par un `id` de la bibliothèque livrée
(`email`, `message-court`, `post-social`, `article-vulgarisation`, `rapport`,
`documentation-technique`, `papier-recherche`, `lettre-motivation`), jamais par une valeur libre ;
type de destinataire, exprimé en asymétrie de connaissance, pouvoir et distance, jamais en nom de
personne ; support de rédaction (mobile, client mail, traitement de texte, éditeur markdown,
formulaire web, ou `séance` pour un texte écrit pendant l'entretien) ; statut de révision (brut,
auto-révisé, révisé par un tiers, assisté par IA) ; sujet, en quelques mots ; nombre de mots ; date.

Les trois premiers champs sont ceux que Grant (2013) exige d'un corpus de comparaison
linguistiquement pertinent : le genre, les effets d'accommodation au destinataire et le mode de
production. Sans ces champs, l'étape 4 ne peut pas router, l'étape 9 n'a pas de contrastes et
l'étape 3 compte des artefacts d'outil comme des marqueurs personnels.

Éligibilité, par statut d'item.

| Cas                                                    | Voix                           | Posture | Registre | Motif                                           |
| ------------------------------------------------------ | ------------------------------ | ------- | -------- | ----------------------------------------------- |
| Corrigé par un tiers, version finale seule             | Non                            | Non     | Oui      | Le trait observé peut être celui du relecteur   |
| Corrigé par un tiers, avec la version avant correction | Oui, sur la version avant      | Oui     | Oui      | Le diff est du matériau de premier ordre        |
| Auto-révisé                                            | Oui                            | Oui     | Oui      | Précieux, c'est l'entrée de l'étape 8           |
| Rédigé ou réécrit avec une IA                          | Non                            | Non     | Oui      | Contamination directe, écarter sur confirmation |
| Co-écrit                                               | Non, sauf sections identifiées | Non     | Oui      | Attribution impossible                          |
| Traduction, ou langue non native                       | Non                            | Non     | Oui      | Traits de la langue cible ou de l'interlangue   |
| Trame imposée (rapport de stage, template)             | Oui pour le grain de la phrase | Oui     | Oui      | La structure appartient au commanditaire        |
| Moins de 300 mots                                      | En agrégat, jamais isolément   | Oui     | Oui      | Pour la posture, le contraste prime le volume   |
| Plus de 3 ans                                          | À signaler, à ne pas mélanger  | Idem    | Oui      | Le style dérive                                 |

Sortie : `corpus-index.md`, avec la table complète et les items écartés assortis de leur motif.
Aucun texte n'est utilisé sans sa ligne dans cette table.

## Étape 2. Dépistage de contamination

Avant tout comptage, l'agent passe le corpus au crible de sa liste de marqueurs de texte généré
(`anti-slop.md` du gabarit d'instance). Ces marqueurs sont probabilistes, le fichier le dit
lui-même. Un texte signalé n'est donc pas écarté d'office : l'agent demande à la personne si ce
texte est passé par une IA et n'écarte **qu'après confirmation**. Écarter sur soupçon élimine des
textes humains dont le seul tort est de ressembler au modèle, ce qui biaise le profil vers
l'exotisme, dans la même direction que le point aveugle de la baseline.

Langue : la part mesurée de la liste est du vocabulaire anglais biomédical (Kobak, González-Márquez,
Horvát & Lause 2025, _Science Advances_ 11(27)). Les analogues français relèvent de la même
catégorie mais ne sont pas mesurés. Hors anglais, le dépistage lexical est plus faible et ce sont
les marqueurs structurels (règle de trois, clôture à moule fixe, gras mécanique) qui portent. La
liste de dépistage est propre à chaque langue.

Coût : environ 1 minute, le temps de confirmer ou d'infirmer sur les items signalés.

Sortie : la liste des items écartés, chacun sur confirmation explicite.

## Étape 3. Comptage

Script `scripts/compte-traits.py`, zéro minute pour la personne.

Les taux se calculent **par registre**, en agrégeant tous les destinataires à l'intérieur d'un
registre. Découper en cellules registre × destinataire rend chaque cellule trop petite et bloque
tout le pipeline. Les contrastes de destinataire se traitent qualitativement à l'étape 9.

Ce que le script fait : il normalise la typographie avant de compter (espaces insécables,
guillemets, apostrophes, tirets d'autocorrection, majuscules de clavier mobile) ; il désambiguïse
les formes ambiguës de la langue active avant de les compter ; il compte la ponctuation par type,
les marqueurs typographiques candidats, les connecteurs et les taux de mots-outils de la langue
active ; il sort la distribution des longueurs de phrase et de paragraphe, pas seulement la moyenne
; il encode l'Empan en delta relatif à la norme d'empan du registre, jamais en valeur absolue, sinon
la composante viole la préséance ; il refuse de produire un taux pour tout registre sous 1 500 mots
et le signale au lieu de l'afficher.

Il signale enfin, sans les proposer comme candidats, les lexèmes qui reviennent dans au moins deux
registres et qui ne sont ni des mots-outils ni des termes de sujet. C'est l'entrée visant la
composante 4 (Lexique de prédilection), angle mort d'un profil rédigé par simple entretien. La règle
1 s'y applique sans exception : ces lexèmes attendent l'étape 5 ou 6 pour devenir des candidats.

### Désambiguïsation avant comptage

En français, trois formes sont ambiguës entre une fonction de posture et autre chose. Les compter
brutes ne mesure rien.

**« on »** a quatre valeurs, à classer par substitution. On remplace l'occurrence par « les gens »,
« nous », « je », « vous et moi » : la substitution qui préserve les conditions de vérité donne la
valeur. Générique et impersonnel, il ne relève pas de la posture. Inclusif auteur plus lecteur, il
relève de la proximité construite et de l'adresse au lecteur. Exclusif d'équipe, il relève de la
prise en charge énonciative. « Je » déguisé, il relève de l'évitement de la prise en charge. Chaque
classe se compte séparément ; un total de « on » ne veut rien dire.

**Le conditionnel** a quatre valeurs. Atténuation, et il relève alors du droit à affirmer et de la
franchise. Politesse figée (« je voudrais », « pourriez-vous »), et c'est une formule de registre.
Hypothétique dans un système en si, et c'est de la syntaxe. Reprise journalistique (« le correctif
serait déployé »), et c'est du sourçage. Seul l'emploi atténuateur compte. Test : retirer le
conditionnel change-t-il l'engagement épistémique de la phrase sans casser sa syntaxe ? Si oui,
c'est un hedge, terme dû à Lakoff (1973).

**La forme interrogative** a trois valeurs, à classer par ce qui suit. Question réelle appelant une
réponse, elle relève de l'ouverture dialogique et de l'adresse au lecteur. Question rhétorique dont
l'auteur donne la réponse dans les deux phrases suivantes, elle relève du geste rhétorique, donc de
la Voix. Question qui porte un désaccord (« Tu as envisagé X ? »), elle relève de l'ouverture
dialogique et de la franchise.

Règle d'adaptation. Pour toute autre langue, l'agent construit cette table avant tout comptage, par
la même méthode : lister les formes ambiguës entre une fonction de posture et une fonction qui n'en
est pas une, donner pour chacune un test de substitution ou de contexte, ne compter qu'après
classement. Il ne traduit pas la table française. En anglais, les candidats évidents sont « we »
(inclusif, exclusif, éditorial), les modaux « would », « could », « might », les question tags et «
I think ».

Sortie : un tableau trait × registre avec la variance inter-registre de chaque trait, et la liste
des registres passés sous le seuil. Unique entrée quantitative de la suite. Ce tableau est recopié
dans `corpus-index.md` comme trace de ce sur quoi le profil repose.

## Étape 4. Routage consistance / registre

Agent seul. Chaque trait vu par le script part dans une des trois voies : stable sur au moins deux
registres, c'est un candidat Voix ; présent sur un seul registre, c'est un candidat Registre et il
sort du périmètre ; sous le seuil de mots, il est écarté avec mention explicite dans la sortie.

Le critère de fond est celui de Biber & Conrad (2009) : sont de la Voix les traits « not
functionally motivated by the situational context ». Ce n'est pas le _tenor_ de Halliday, qui borne
Audience et Posture, et il ne faut pas le lui attribuer.

Ce routage n'est pas le test de tri. Il ne classe que ce que le script voit, et les traits de
discours n'existent pas encore à ce stade. Le test de tri à trois filtres (`modele-concepts.md`)
s'applique à l'étape 7, sur la liste complète.

Les candidats Posture ne sortent pas d'ici. Ils viennent de l'étape 9.

Sortie : deux listes de candidats de surface, aucune validée, aucune substantielle.

## Étape 5. Baseline générée et lecture des mouvements de discours

Agent seul, et c'est la première des deux étapes qui produisent la substance.

La baseline d'abord. L'agent réécrit deux ou trois passages du corpus en version neutre, à contenu
et registre constants, puis diffe. Ce qui subsiste dans l'écart est candidat. Le point aveugle de
cette référence est décrit dans `limites.md` et doit être énoncé à la personne lors de la
restitution : tout trait qu'elle partage avec le modèle reste invisible.

La lecture ensuite : comment la personne ouvre, comment elle enchaîne argument et exemple, comment
elle traite un désaccord, comment elle clôt. C'est là qu'apparaissent les traits du type «
métaphore-puis-analyse », qu'aucun comptage ne produit.

Visée obligatoire sur les composantes 4 et 6, qu'un entretien libre n'élicite pas.

Pour la composante 4 (Lexique de prédilection), reprendre la liste de lexèmes signalée à l'étape 3
et chercher une fonction à chacun. Un mot qui revient parce que le sujet revient est un marqueur de
sujet, pas de personne. La colonne Sujet de la table de qualification sert ici : un lexème qui ne
revient que sur un sujet se confine à ce sujet, comme l'étape 4 confine un trait à un registre. Si
tous les items partagent le même sujet, aucun lexème ne passe ce test, et la composante 4 reste une
hypothèse à trancher par écrans. Un mot qui revient dans des sujets différents et des registres
différents, en position évaluative ou en charnière d'argument, est un candidat.

Pour la composante 6 (Architecture du propos), lire les deux textes longs. Le piège est que le plan
est presque toujours imposé de l'extérieur, et la liste des sections appartient au commanditaire. Ce
qui se relève est l'ordre des mouvements **à l'intérieur** de ce que le plan laisse libre : où tombe
la thèse dans un paragraphe, si l'objection précède ou suit l'argument, si l'exemple ouvre ou ferme.
Sans texte long dans le corpus, la composante 6 est déclarée non extractible et signalée comme telle
dans `voix.md`, pas omise.

La composante 8 (Regard) suit le même sort. Elle ne s'observe pas sur texte court, elle est
optionnelle, et son absence s'écrit.

Langue : cette étape est indépendante de la langue, c'est la couche transposable de la règle 4.

Sortie : la liste de candidats de référence, ouverte ici. Traits de discours d'abord, puis les
formes signalées à l'étape 3 auxquelles une fonction a été trouvée.

## Étape 6. Incident critique, répulsion, deux tâches ancrées

12 à 14 minutes de dialogue, second gisement de substance.

Si l'entretien approfondi a été retenu à l'étape 0 et qu'il y a un corpus, cette étape est gardée et
la séance de `protocole-entretien.md` s'y ajoute, après l'étape 5. Dans le parcours sans corpus,
cette étape est sautée : un premier usage réel a montré que, sans texte à quoi ancrer les relances,
les récits ne rapportent rien. Le saut s'écrit dans `corpus-index.md`.

Toutes les relances se formulent comme des demandes de récit ou d'action, jamais comme des demandes
d'explication. Fox, Ericsson & Best (2011, _Psychological Bulletin_ 137, 316-344) trouvent l'effet
réactif de la verbalisation simple indistinguable de zéro sur environ 3 500 participants (r = -.03),
alors que les consignes demandant explications et descriptions détaillées sont, elles,
significativement réactives. Demander à quelqu'un d'expliquer son style modifie ce qu'il produit.

Chaque relance s'ancre sur un moment ou un objet spécifié plutôt que sur une classe d'actions, règle
reprise de Vermersch (1994, _L'entretien d'explicitation en formation initiale et continue_, ESF).
Les formulations françaises de ces notions données ici sont des paraphrases, pas des citations du
texte.

Cinq relances, par ordre de priorité. Si le budget se resserre, la deuxième saute la première.

1. Incident critique, d'après la technique de Flanagan (1954, _Psychological Bulletin_ 51(4),
   327-358), conçue pour collecter des observations d'événements réels plutôt que des opinions
   générales. « La dernière fois qu'un de tes textes a été mal pris ou mal compris : c'était quoi,
   et qu'est-ce que tu as changé ensuite ? »
2. Réussite. « Un texte de toi dont tu es content : lequel, et qu'est-ce qui fait que celui-là
   marche ? »
3. Répulsion. « Colle un extrait de quelqu'un d'autre que tu trouves mal écrit, et dis ce qui te
   gêne dedans. » Le jugement négatif est plus discriminant et moins sujet à l'embellissement que le
   jugement positif. [NON VÉRIFIÉ] : cette variante se rattache à la famille des techniques
   d'élicitation par contraste répertoriées chez Cooke (1994, _IJHCS_ 41(6), 801-849), mais le
   rattachement précis est une inférence et non un résultat de Cooke.
4. Localisation du point, qui vise la composante 6. Ancrée sur un des textes longs du corpus : «
   Dans ce texte, montre-moi la phrase qui porte le point principal. » Puis : « Tu l'aurais mise
   ailleurs ? » On demande un repérage et un choix, jamais un pourquoi.
5. Réécriture à la troisième main, qui vise la composante 4. Ancrée sur un paragraphe précis : «
   Voici un paragraphe de toi. Réécris-le comme si quelqu'un d'autre l'avait écrit et que tu devais
   le corriger. » Les substitutions qu'elle opère exposent les mots qu'elle possède et ceux qu'elle
   tolère. C'est une tâche de production, pas une description.

Ne jamais poser « quels mots utilises-tu ? » ni « comment écris-tu ? ». Ce sont des demandes
d'explication, donc réactives, et la réponse est une théorie personnelle du style. Nisbett & Wilson
(1977, _Psychological Review_ 84(3), 231-259) montrent qu'il y a peu ou pas d'accès introspectif
direct aux processus de haut niveau et que les rapports s'appuient sur des théories causales
implicites a priori. Trudgill (1972, _Language in Society_ 1(2), 179-195) montre que l'écart
déclaratif n'est pas du bruit aléatoire : il est orienté par la valeur sociale que la personne
attribue à la forme.

Langue : les relances et les extraits se posent dans la langue du corpus. Traduire un extrait avant
de le montrer détruit les traits de surface qu'on sonde.

Sortie : les lignes rouges, l'effet visé, ce que la personne déteste lire, plus les candidats des
composantes 4 et 6. Ce matériau devient la section de philosophie de fond de `voix.md`.

## Étape 7. Test de tri, puis arbitrage en choix forcé aveugle

Deux parties. Le tri est du travail d'agent et ne coûte rien ; les écrans coûtent environ 5 minutes.

### 7a. Test de tri, trois filtres

Appliqués à la liste complète, traits de discours compris. C'est leur place : les traits qui font
trébucher le premier filtre sont précisément ceux que la lecture et l'entretien viennent de
produire, pas ceux du script.

**Filtre de forme.** Un candidat de Voix qui nomme une forme figurant dans les listes de marqueurs
des composantes de posture (question, hedge, conditionnel, humour, tutoiement, adresse au lecteur,
auto-mention) est mal placé. On le scinde : la direction reste dans la Voix, la dose descend dans la
Posture, la forme revient au Registre. Cas d'école (`modele-concepts.md`, section 4) : l'invariant «
réflexe de la question plutôt que l'affirmation face au désaccord » nomme une forme. Ce qui reste
dans la Voix est la direction, sonder plutôt qu'asserter devant un désaccord ; la dose appartient à
la composante 1 ; la forme interrogative appartient au registre. Les formes idiolectales sans
fonction interpersonnelle, comme le slash ou une signature typographique, restent légitimement dans
la Voix.

**Filtre de persistance.** Le trait persiste-t-il dans l'espace que les postures laissent libre ?
Une surcharge par une posture ne réfute pas un trait de voix : la préséance prévoit qu'une posture
prime. Le filtre tourne ici contre les registres, puis se rejoue après l'étape 9, une fois les
postures retenues connues. Il est plus faible qu'une falsification sèche, et c'est la contrepartie
assumée de la décision de conception, pas un oubli. Dit franchement dans `limites.md`.

**Filtre d'intentionnalité.** Choix délibéré ou tic ? Ne se tranche jamais sans la personne. Trois
instruments : substitution et charge fonctionnelle, sur table, ici ; survie à l'auto-révision, à
l'étape 8 ; contrôlabilité, par les écrans de 7b. Cas de référence : `=>` sous-spécifie, il faut
choisir entre « donc », « d'où » et « devient », donc c'est un tic ; le slash ne sous-spécifie
jamais, donc c'est un marqueur.

### 7b. Écrans de choix forcé aveugle

Six écrans au plus avec un corpus. Dans le parcours sans corpus, le plafond est levé et les écrans
s'élargissent aux lexèmes et à la typographie (`protocole-entretien.md`, bloc D). Priorité aux
traits plats sur tous les registres, les tics présumés, parce que le test de variance ne les sépare
pas d'un invariant, les deux étant plats par construction.

Un écran par candidat. Même passage, même registre, même destinataire, une seule composante variée
(règle 3), aucune indication de provenance. Quatre options au plus : trois niveaux de la composante
visée, le niveau extrême servant de distracteur, et une option de rejet global.

La question se pose en termes d'usage (« laquelle enverrais-tu à X ? »), jamais en termes
d'attribution (« laquelle as-tu écrite ? »). L'aveuglement n'est pas une précaution de confort.
Johansson, Hall, Sikström & Olsson (2005, _Science_ 310(5745), 116-119) montrent que les sujets ne
détectent la substitution de leur propre choix que dans environ 25 % des cas et fabriquent ensuite
des justifications pour le choix qu'on leur a attribué. Annoncer « voici ta version » garantit une
rationalisation, pas une donnée. Cette règle n'est pas négociable : c'est elle qui distingue l'étape
7 d'un questionnaire de complaisance.

Piège de construction propre aux écrans de voix : un mot de registre familier qui se glisse dans la
variante censée être neutre (par exemple un raccourci de jargon d'équipe à côté du mot visé). La
variante bouge alors sur deux axes, le mot visé et le registre, et le choix n'identifie plus rien.
Chaque variante se relit mot à mot contre la phrase de base avant d'être posée.

Réponse libre. L'outil de questions laisse toujours une option « autre » où la personne écrit sa
propre version. Elle n'est plus aveugle au sens strict, mais elle est souvent très informative, et
parfois elle répare un écran mal construit. Elle compte comme une **occurrence de séance**, pas
comme un choix d'écran. Une même réponse ne sert jamais deux fois : elle ne peut pas être à la fois
l'écran et l'occurrence qui le corrobore.

Un trait ne se valide pas sur un écran unique. Il faut soit deux écrans convergents, soit un écran
et une occurrence de corpus corroborante. Une occurrence de séance (`protocole-entretien.md`, blocs
B et C, ou réponse libre) tient lieu d'occurrence de corpus, avec la provenance `séance` qui signale
qu'elle pèse moins. Dans le parcours sans corpus, la phrase de base des écrans est prise dans un
texte écrit par la personne au bloc B, jamais dans un texte de l'agent. Le chiffre de deux est un
choix d'ingénierie, aucun chiffre publié ne s'applique à l'auto-cohérence d'une personne seule ;
voir `limites.md`.

Langue : les écrans s'écrivent dans la langue du corpus.

Sortie : chaque candidat passe en `confirmé`, `tic`, ou `restreint à <id de registre>`.

## Étape 8. Test de survie à l'auto-révision

Lecture, zéro minute pour la personne, conditionné à la présence de paires brut / auto-révisé dans
le corpus, ou produites au bloc C de l'entretien par marquage des coupes. Les écrans d'allègement du
même bloc ne sont pas des paires et ne déclenchent pas cette étape.

Vérifier quels traits disparaissent au passage où la personne s'est relue. Un trait qui disparaît
est reclassé en tic même s'il avait passé l'étape 7, par la clause 3 de la règle de preuve. Ce test
prime sur la préférence déclarée parce qu'il observe un comportement au lieu d'interroger un
jugement.

Si le corpus ne contient aucune paire, l'étape est sautée et le saut s'écrit dans le livrable, il ne
disparaît pas silencieusement.

Sortie : les reclassements finaux, et la mention explicite du saut le cas échéant.

## Étape 9. Traversée du catalogue de postures et calibration

Environ 5 minutes, 5 écrans. Aucun taux ici, les cellules de destinataire sont trop petites.

### 9a. Lecture des contrastes

L'agent lit les items du registre court groupés par type de relation et projette chaque groupe sur
les sept composantes de posture : ouverture dialogique, intensité évaluative, droit à affirmer,
franchise, proximité construite, adresse au lecteur, prise en charge énonciative. Il relève les
contrastes qualitatifs entre groupes, composante par composante.

Ce découpage préfère sept composantes à un partage en deux axes, social et épistémique. L'intuition
de ce partage est juste : la distance, le pouvoir et l'asymétrie de connaissance ne se confondent
pas, un client a du pouvoir sur soi et en sait moins que soi. Mais ces trois grandeurs sont des
entrées d'Audience (D, P, K), pas des valeurs jouées. Les valeurs jouées sont les sept composantes,
et elles servent mieux la même intuition.

Ne jamais écrire « distance sociale » comme valeur d'une composante de posture. La distance réelle
est une entrée d'Audience ; la proximité **construite**, composante 5, est la valeur jouée.

Les composantes 1, 3 et 4 portent l'essentiel, et une implémentation minimale sur elles seules est
possible. Les quatre autres se calibrent par cette lecture et se font valider à l'étape 12.

### 9b. Traversée accept / décline

Deux écrans, sept questions à trois options : accepter, décliner, reporter. Le catalogue livre sept
postures, d'identifiants `apprenant`, `pair`, `guide`, `arbitre`, `contradicteur`, `diplomate`,
`provocateur`. Chacune est acceptée, déclinée ou reportée explicitement. Jamais « choisis celles qui
te parlent » : c'est le accept / décline forcé qui fait remonter les angles morts, puisqu'une
posture que personne ne pense à nommer est une posture que personne ne décline.

Chaque posture est présentée avec son ancrage dans le corpus si elle en a un, ou explicitement comme
n'en ayant aucun.

Une posture observée dans le corpus mais déclinée reste une décline. Son ancrage de corpus est
journalisé dans `changelog.md` pour qu'une révision ultérieure puisse rouvrir la question. Le
fichier n'est pas écrit.

`reporter` veut dire « pas maintenant » : la personne veut la posture, mais le matériau ou le temps
manque pour la calibrer, typiquement faute d'un texte de refus pour `arbitre` ou `contradicteur`.
Une posture reportée est traitée comme déclinée pour cette instance (pas de fichier, lignes
d'audience retirées), mais journalisée dans `changelog.md` sous l'état `reporté`, avec ce qui
manquait. Une révision ultérieure rejoue les étapes 9b et 9c pour ces seules postures, sans rejouer
le reste du protocole.

### 9c. Calibration

Trois écrans, un par composante parmi 1, 3 et 4. À l'intérieur d'un écran, une question par posture
retenue, jusqu'à quatre questions. L'écran fait donc varier une composante et une seule tout en
couvrant plusieurs postures. Au-delà de quatre postures retenues, deux écrans pour cette composante.

Chaque question suit la règle 3 : trois niveaux de la composante visée plus une option de rejet,
tout le reste constant. Ces questions produisent directement les triplets de calibration écrits dans
les fichiers de posture, donc un triplet par composante et non un triplet par posture.

Posture retenue sans aucun ancrage dans le corpus : elle n'est écrite que si ses trois écrans
reviennent cohérents, et son fichier porte la mention « non corroborée par le corpus », dans le
champ de frontmatter `corroboration`, défini par le gabarit de posture dans
`examples/instance/skills/write/references/postures/`. Trois valeurs : `corpus` si un texte du
corpus l'illustre, `séance` si seul un texte écrit pendant l'entretien approfondi l'illustre,
`non-corroboree` si elle ne repose que sur les écrans. Écrans incohérents ou sautés, la posture
n'est pas écrite et la décision va dans `changelog.md`. Une posture n'est jamais inventée pour une
cellule vide ; un écran de choix forcé, lui, est de l'extraction comportementale et pas une
déclaration, ce qui suffit à fonder une calibration minimale.

Sortie : la liste des postures retenues avec la valeur de chacune des sept composantes, les triplets
de calibration pour 1, 3 et 4, et les déclines journalisées avec leur ancrage.

## Étape 10. Traversée du catalogue de registres

Environ 3 minutes, 2 écrans. Aucun taux ici.

Les registres sont universels : l'instance les reçoit du gabarit, comme `anti-slop.md`, et rien ne
s'extrait. Ce qui se décide ici est lesquels elle garde. Le catalogue livre huit registres,
d'identifiants `email`, `message-court`, `post-social`, `article-vulgarisation`, `rapport`,
`documentation-technique`, `papier-recherche`, `lettre-motivation`. Chacun est accepté ou décliné
explicitement, deux écrans de quatre questions à deux options, sur le modèle de l'étape 9b sans
l'option de report : un registre ne se calibre pas, il n'y a rien à reporter. Jamais « choisis ceux
qui te parlent » : le passage forcé fait remonter les genres que la personne écrit sans y penser, au
lieu de reconduire une liste par défaut, et c'est le même motif que pour les postures.

Chaque registre est présenté avec son ancrage dans le corpus (nombre d'items qualifiés sous cet `id`
à l'étape 1) ou explicitement comme n'en ayant aucun. Un registre observé dans le corpus mais
décliné reste une décline, l'écran garde deux options, et l'ancrage est journalisé dans
`changelog.md`. Le fichier n'est pas copié dans l'instance.

Deux cas à traiter à la sortie de l'écran :

- Un item du corpus rangé sous un registre décliné est re-rangé ou écarté de la table de
  qualification, jamais laissé sous un `id` absent de l'instance.
- Un genre que la personne écrit et qu'aucun registre de la bibliothèque ne couvre : l'agent le
  signale, et propose soit le registre le plus proche, soit l'écriture d'un nouveau fichier selon
  `contrats-interface.md`. Il n'invente pas un registre pour une cellule vide, et ne range pas un
  texte sous un `id` qui n'existe pas.

L'instance garde au moins un registre. Si tous sont déclinés, l'agent le dit et redemande : sans
registre, l'étape 2 du workflow du skill produit n'a rien à lire.

Sortie : la liste des registres retenus, les déclines journalisés avec leur ancrage, et les genres
sans registre.

## Étape 11. Contrôle de l'Audience

Aucune extraction, 0 minute. `audience.md` se livre complet : table de routage des entrées K, P et
D, plus règles de niveau de contenu. Rien n'est donc à demander à la personne.

Reste un contrôle de cohérence, à faire avant d'écrire, une fois les postures de l'étape 9 et les
registres de l'étape 10 arrêtés :

- Chaque `id` de posture cité par la table de routage désigne une posture effectivement retenue. Les
  lignes des postures déclinées sont retirées, et le retrait est journalisé dans `changelog.md`.
- Même contrôle sur le champ `postures` des fichiers de registre retenus, qui court-circuite la
  table de routage : il ne doit citer que des postures retenues.
- Chaque posture retenue reste atteignable, par une ligne de la table ou par le champ `postures`
  d'un registre. Une posture retenue qu'aucune ligne ne route est une posture injoignable, et le
  validateur la signale (`ATT-01`).
- Chaque **situation** reste couverte. Retirer une ligne retire aussi son but : une situation où K,
  P et D sont renseignés mais dont le but n'est plus routé (par exemple « refuser une position »
  après le retrait de `contradicteur`) ne correspond plus à aucune ligne. La ligne par défaut couvre
  ce cas, comme celui des axes manquants ; l'agent vérifie qu'elle le dit, et la relit contre chaque
  but retiré. Le validateur ne fait pas ce contrôle : il vérifie l'atteignabilité des postures, pas
  la couverture des situations.

Sortie : `audience.md` allégé des postures déclinées, et la liste des retraits.

## Étape 12. Restitution contestable et écriture

5 minutes.

Avant la restitution, une passe de vérification, agent seul : chaque affirmation de `voix.md` et de
`corpus-index.md` doit renvoyer à une sortie d'écran, à une sortie du script, ou à un passage de
texte cité. Trois erreurs typiques à chercher : un trait reformulé plus fort que ce que les écrans
ont retenu ; un chiffre du tableau de comptage que le script n'a pas produit, par exemple après un
reclassement d'item (relancer le script) ; un texte appelé « long » sous le seuil de 300 mots. La
passe précède le validateur, qui ne voit rien de tout cela.

L'agent affirme le profil en termes nets, pas en hypothèses prudentes : la formulation prudente
invite l'acquiescement. Chaque trait est présenté avec son origine, occurrence de corpus, arbitrage
en choix forcé ou entretien, pour que la personne puisse contester une inférence sans contester une
observation. Option de rejet explicite sur chaque élément. La restitution vient après les écrans,
jamais avant, sinon la personne valide les hypothèses de l'agent par complaisance ou par fatigue.

Le filtre de persistance se rejoue une dernière fois ici, maintenant que les postures retenues sont
connues. La restitution présente aussi les registres retenus et déclinés, et le passage de
l'étape 11.

Avant d'écrire, deux questions à la personne.

- **Le nom du plugin.** Par défaut `write`. La personne peut en choisir un autre, en kebab-case. Ce
  nom alimente le dossier `plugins/<nom>/`, le champ `name` de `plugin.json`, la référence à l'agent
  `<nom>:fact-checker` dans `SKILL.md`, et l'entrée de son propre marketplace si elle en a un. Rien
  n'entre dans le marketplace de `write-forge`.
- **La coexistence.** Si un autre skill de rédaction est déjà installé (un skill dont la description
  se déclenche sur toute tâche d'écriture), les deux se disputeront le déclenchement. L'agent le
  signale et propose soit de désactiver l'ancien, soit de garder les deux avec un nom et une
  description qui les séparent, par exemple en nommant la personne dans la description du nouveau.

Puis l'écriture. Les contrats de format de chaque fichier sont dans `contrats-interface.md` et
vérifiés par `scripts/valide-instance.py`. Les règles d'écriture qui appartiennent en propre à ce
protocole :

- Chaque trait de voix retenu reçoit un `id` kebab-case stable. Les fichiers de posture s'y réfèrent
  par `id` dans leur champ `suspend:`, jamais par libellé humain, sinon renommer casse
  silencieusement la référence.
- Ne jamais écrire qu'un trait de voix « persiste peu importe la posture », ni aucune formule
  d'invariance absolue. Formuler : tendance par défaut, qu'une posture peut surcharger en le
  déclarant.
- `voix.md` se rédige au niveau du discours et non au niveau du mot, pour que les traits portent
  d'une langue à l'autre. Les marqueurs de surface vont dans une section à part, signalée comme liée
  à la langue du corpus.
- Aucune posture ne peut suspendre l'étape de vérification factuelle du skill produit, ni le statut
  de principal sur le contenu propositionnel, y compris en posture `provocateur`.
- L'Empan s'écrit en delta relatif à la norme du registre, jamais en valeur absolue.
- Le Geste rhétorique est une étiquette forgée, sans terme établi. Le signaler comme telle dans le
  fichier.
- Toute composante non extraite s'écrit comme non extraite, avec son motif. Elle ne s'omet pas.
- Les traits restreints à un registre vont dans une section à part de `voix.md`, avec l'`id` du
  registre concerné.

### Fichiers de l'instance

Le protocole produit un plugin autonome `plugins/<nom>/`, `write` par défaut. Liste exacte, séparée
selon ce que l'extraction produit et ce qui vient du gabarit.

Produits par l'extraction :

- `skills/write/references/voix.md`
- `skills/write/references/voix-aspirations.md` : ce que la personne a déclaré sans que le corpus le
  corrobore. Écrit, et **jamais chargé** par le skill produit. Il existe pour rendre l'écart visible
  plutôt que de le faire disparaître silencieusement.
- `skills/write/references/postures/<id>.md`, un fichier par posture retenue. Le fichier
  `postures/gabarit.md` du gabarit n'est pas copié.
- `skills/write/corpus-index.md` : table de qualification, items écartés avec motif, tableau de
  comptage de l'étape 3, étapes sautées et modes dégradés actifs.
- `skills/write/changelog.md` : entrée initiale, postures et registres déclinés avec leur ancrage de
  corpus, postures reportées avec ce qui manquait, lignes d'audience retirées.

Copiés du gabarit puis filtrés par le protocole, sans extraction :

- `skills/write/references/registres/<id>.md`, un fichier par registre accepté à l'étape 10. Les
  registres déclinés ne sont pas copiés.
- `skills/write/references/audience.md`, allégé à l'étape 11 des lignes des postures déclinées. La
  table ne cite que des `id` de postures retenues.

Repris du gabarit tels quels :

- `.claude-plugin/plugin.json`, `name` rempli avec le nom choisi
- `agents/fact-checker.md`
- `skills/write/SKILL.md`, référence à l'agent remplie avec le nom choisi
- `skills/write/references/anti-slop.md`

## Tableau de coût

| Étape  | Temps personne           | Ce qui est demandé                                            |
| ------ | ------------------------ | ------------------------------------------------------------- |
| 0      | 3 min                    | 1 écran de 4 questions                                        |
| 1      | 20 à 40 min hors session | Rassembler et déposer les items de la spécification           |
| 2      | 1 min                    | Confirmer ou infirmer l'assistance IA sur les items signalés  |
| 3 à 5  | 0 min                    | Rien                                                          |
| 6      | 12 à 14 min              | Dialogue : 3 récits et 2 tâches ancrées                       |
| Séance | 30 à 40 min, si retenu   | Entretien approfondi : production en séance et écrans élargis |
| 7      | 5 min                    | 6 écrans de choix forcé au plus                               |
| 8      | 0 min                    | Rien                                                          |
| 9      | 5 min                    | 5 écrans : 2 de traversée, 3 de calibration                   |
| 10     | 3 min                    | 2 écrans de traversée du catalogue de registres               |
| 11     | 0 min                    | Rien                                                          |
| 12     | 5 min                    | Lecture et contestation                                       |
| Total  | ~34 min en session       | plus 20 à 40 min de collecte                                  |

Avec l'entretien approfondi et un corpus, 65 à 70 minutes en session, l'étape 6 restant jouée. Dans
le parcours sans corpus, environ 55 minutes et aucune collecte : l'étape 6 est sautée, mais l'étape
7 demande plus d'écrans, faute d'occurrences de corpus pour corroborer un écran unique.

## Modes dégradés

Chaque déclencheur s'annonce à l'étape 0 s'il est prévisible, et se consigne dans `corpus-index.md`
dans tous les cas.

Le parcours sans corpus est décrit à l'étape 0 et dans `protocole-entretien.md`. Les déclencheurs
ci-dessous s'y évaluent sur les textes de séance. Le plancher de mots y sera presque toujours
manqué, donc aucun taux ; en revanche les contrastes de destinataire et les paires brut /
auto-révisé sont produits en séance, et les postures suivent ces contrastes au lieu d'être réduites
à une seule.

| Déclencheur                           | Ce que le protocole produit quand même                                                                           |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Un seul registre                      | `voix.md` marqué provisoire, traits de discours seuls, aucun taux, une seule posture                             |
| Moins de 2 500 mots au total          | Idem                                                                                                             |
| Un registre sous 1 500 mots           | Aucun taux pour ce registre ; ses items comptent pour la lecture qualitative et pour les postures                |
| Moins de 2 contrastes de destinataire | Traversée du catalogue quand même, calibration par écrans seuls, postures marquées non corroborées par le corpus |
| Aucune paire brut / auto-révisé       | Étape 8 sautée, saut écrit dans `corpus-index.md` ; la clause 3 de la règle de preuve ne s'applique pas          |
| Aucun texte long                      | Composantes 6 et 8 déclarées non extractibles, avec leur motif                                                   |
