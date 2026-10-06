# Limites

À lire avant de faire confiance au résultat du protocole. Ce que `write-forge` produit est un profil
indicatif, pas une signature. Sa valeur tient à sa traçabilité, chaque trait portant son origine,
pas à une exactitude mesurée. Voici ce que le protocole ne sait pas faire.

## 1. Le point aveugle de la baseline

La référence de comparaison est une réécriture neutre générée par l'agent lui-même (étape 5). Donc
**tout trait que la personne partage avec le modèle reste invisible** et disparaît du profil. Ce qui
sort est ce qui s'écarte du défaut de rédaction du modèle, pas ce qui caractérise la personne. Le
livrable penche vers l'exotique plutôt que vers le caractéristique.

Il y a un argument sérieux pour garder cette référence : le `voix.md` produit est lu par un LLM,
donc ce qu'il faut encoder est précisément l'écart au défaut du modèle, et pas une distinctivité
populationnelle que personne ne consommera. L'argument rend la limite acceptable, il ne la supprime
pas. Elle vaut quelle que soit l'option retenue.

L'étape 2 (dépistage de contamination) a le même biais et dans le même sens : elle retire du corpus
ce qui ressemble au modèle. D'où la règle d'écarter sur confirmation de la personne et jamais sur
soupçon, qui limite les dégâts sans les annuler.

## 2. Aucun ensemble de comparaison

Grant (2013, _Journal of Law and Policy_ 21(2), 467-494) pose deux hypothèses à toute analyse
comparative d'auteur, la consistance et la distinctivité, et il écarte explicitement la
distinctivité populationnelle au profit de la distinctivité **par paires** entre auteurs pertinents
au dossier. Une distinctivité par paires demande au moins deux auteurs identifiés.

Ici il y a une personne et aucun candidat concurrent. La distinctivité n'est donc pas mesurée du
tout, ni au sens de la stylométrie ni au sens de Grant. Autant le dire franchement plutôt que de se
réclamer d'une rigueur qu'on n'a pas.

Ce que le protocole mesure vraiment est la consistance, et c'est réel : du comptage à travers les
registres sur le corpus fourni. Grant note par ailleurs, et cela joue en notre faveur, que « the
idea that comparative authorship analysis rests upon a strong theoretical assertion of an idiolect
is false. The empirical discovery of consistency and distinctiveness can, however, be a sufficient
foundation for such work. » On dispose de la moitié de cette fondation.

## 3. L'invariance est graduée, pas binaire, et moins documentée qu'il n'y paraît

Le chiffre cross-genre est **82 %** : Goldstein-Stewart, Winder & Sabin (2009, EACL, 336-344),
entraînement sur 5 genres et test sur le sixième. Le 71 % que l'on cite souvent est la validation
croisée 6-fold tous genres mélangés, ce n'est pas un résultat cross-genre. L'erreur est courante.

Ce que 82 % établit et ce qu'il n'établit pas. Il s'agit d'identification en ensemble fermé parmi 21
personnes, avec environ 22 000 mots par individu et une ligne de base aléatoire d'environ 5 %. Cela
établit qu'un signal personnel traverse les genres, et solidement. Cela n'établit pas que ce
protocole capte ce signal sur environ 4 700 mots, sans ensemble de comparaison, et pour un livrable
qui n'est pas une décision de classement.

Autre confusion à éviter : dans les campagnes PAN 2018 et 2019, « cross-domain » signifie
cross-_fandom_, donc cross-topic **à l'intérieur d'un seul genre**. Ne pas s'en réclamer pour le
cross-genre, ce n'est pas la même généralisation.

Conséquence pratique. Un trait « stable sur deux registres » est un trait qui n'a pas été réfuté sur
deux registres, pas un trait garanti sur un troisième. L'invariance produite par le protocole est
une affaire de degré, et le degré n'est pas chiffré.

## 4. Le filtre de persistance est plus faible qu'une falsification

Par construction, une surcharge par une posture ne réfute pas un trait de voix : la préséance
prévoit qu'une posture prime, et c'est la contrepartie assumée de la décision de conception qui
sépare la direction (Voix) de la dose (Posture).

Le filtre ne peut donc réfuter qu'un trait qui s'évanouit dans l'espace laissé libre par les
postures. Un trait systématiquement surchargé par la posture active, quelle qu'elle soit, est
empiriquement indistinguable d'un trait qui n'existe pas. Plus l'instance retient de postures, plus
le filtre s'affaiblit.

Ce n'est pas un oubli, c'est un coût accepté. Mais il faut le compter comme un coût.

## 5. Le Regard ne s'observe pas là où le skill sert le plus

La composante Regard demande des textes longs. Le skill produit, lui, travaille surtout sur du court
: un email de deux lignes, un commentaire, un message. Sur le cas d'usage le plus fréquent, il
tourne donc sans cette composante, et le corpus ne permet pas de la lui donner. La composante 6
(Architecture du propos) est logée à la même enseigne dès que le corpus manque de textes longs.

Le protocole écrit ces absences plutôt que de les taire, ce qui les rend visibles sans les résoudre.

## 6. Sur-ajustement à un échantillon non représentatif, et voix aspirée

Deux modes de défaillance distincts, tous deux probables.

Le premier est le sur-ajustement. Le chemin de moindre effort, pour la personne, est de fournir dix
items du même type. Le profil produit est alors le portrait d'un genre. Parades partielles : le
refus annoncé à l'étape 0, avant la collecte plutôt qu'après l'analyse, et le mode dégradé qui
interdit les traits de surface dans ce cas.

Le second est la voix qu'on aimerait avoir. L'écart déclaratif n'est pas du bruit aléatoire : il
suit la valeur sociale perçue de la forme (Trudgill 1972, _Language in Society_ 1(2), 179-195), et
les rapports introspectifs s'appuient sur des théories causales implicites a priori plutôt que sur
une observation (Nisbett & Wilson 1977, _Psychological Review_ 84(3), 231-259). Parades partielles :
la règle « pas de trait sans occurrence », le routage vers `voix-aspirations.md`, le test de survie
à l'auto-révision qui prime sur la préférence déclarée, et le fait que l'étape 6 demande des récits
et des actions plutôt que des explications.

Ce sont des parades, pas des corrections. Il reste un canal qu'aucune étape ne surveille : le corpus
est auto-sélectionné. Une personne qui choisit quels items déposer oriente le profil en amont de
tout le dispositif, sans avoir à déclarer quoi que ce soit.

## 7. « Deux écrans convergents » est un choix d'ingénierie

Aucun chiffre publié ne s'applique à l'auto-cohérence stylistique d'une personne seule. Les repères
disponibles mesurent autre chose : Ouyang et al. (2022, InstructGPT) rapportent 72,6 ± 1,5 %
d'accord entre annotateurs d'entraînement et 77,3 ± 1,3 % en held-out, avec 73 ± 4 % chez Stiennon
et al. (2020) pour la comparaison chercheur-chercheur. C'est de l'accord **entre annotateurs**, pas
l'auto-cohérence d'une personne.

Ces ordres de grandeur suffisent à justifier de ne pas valider un trait sur un écran unique. Ils ne
justifient pas le nombre deux. Le seuil du protocole est posé, pas dérivé.

## 8. Le choix forcé est transposé par analogie

Murphy, Allen, Stevens & Weatherhead (2005, _Environmental and Resource Economics_ 30(3), 313-325),
méta-analyse de 28 études et 83 observations, ratio médian valeur hypothétique sur valeur réelle de
1,35, concluent qu'« a choice-based elicitation mechanism is important in reducing bias ».

L'objet est le consentement à payer, pas le style. Le transfert au choix stylistique est une
analogie sur le mécanisme, choisir plutôt que déclarer, pas un résultat sur notre objet. L'appui de
l'étape 7 est donc analogique, ce qui ne l'invalide pas mais l'empêche de faire preuve.

Le seul point de l'étape 7 qui repose sur un résultat direct est l'aveuglement, appuyé sur
Johansson, Hall, Sikström & Olsson (2005, _Science_ 310(5745), 116-119).

## 9. Les seuils de volume sont extrapolés

Eder (2015, _DSH_ 30(2), 167-182) trouve un minimum de 2 500 à environ 5 000 mots, indépendant de la
méthode. Burrows (2002) situe son seuil de fonctionnement sur des « texts exceeding about 1,500
words ». Ces deux chiffres portent sur l'attribution en ensemble fermé sur de la prose littéraire,
et sur la stabilité d'une **décision de classement**, pas sur la lisibilité d'un profil.

Les transposer à la tâche de `write-forge` est une extrapolation honnête, à assumer comme telle.
Elle est probablement conservatrice pour les traits de discours, qu'on peut repérer sur trois
textes, et optimiste pour les taux de surface.

## 10. Les registres sont livrés à profondeur mécanique, sans couverture exhaustive

La bibliothèque livre huit registres : `email`, `message-court`, `post-social`,
`article-vulgarisation`, `rapport`, `documentation-technique`, `papier-recherche`,
`lettre-motivation`. Une instance tourne sans qu'on écrive de registre, mais cela ne dit rien de la
finesse de ces fichiers.

Chacun est écrit à une profondeur mécanique : caractéristiques situationnelles, contraintes de
forme, norme d'empan, surcharges déclarées. Aucun ne résulte d'une recherche de genre approfondie,
genre par genre. La norme d'empan en particulier est une valeur de départ raisonnable, pas une
mesure sur un échantillon du genre, et l'Empan de la voix s'écrit en écart contre elle.

La bibliothèque ne couvre pas tous les genres. Une personne qui écrit des comptes rendus de réunion,
des notes juridiques ou des scripts n'y trouvera pas son genre, et le protocole le signale à l'étape
10 plutôt que de ranger ses textes sous un registre voisin. Pour un registre plus fin, ou pour un
genre absent, il faut en écrire un en suivant `contrats-interface.md`. Ce travail reste à la charge
de la personne, et le protocole ne le fait pas à sa place.

L'Audience est universelle de la même façon : sa table de routage et ses règles de niveau de contenu
sont des défauts raisonnables, que le protocole filtre contre les postures retenues sans les
recalibrer sur la personne.

## 11. Le matériau de séance est produit sous observation

L'entretien approfondi (`protocole-entretien.md`) remplace le corpus par des textes écrits et
corrigés pendant la session. Ces textes ont trois défauts qu'un corpus n'a pas. Ils sont écrits
devant l'agent, en sachant qu'ils servent à décrire une voix. Ils sont souvent écrits pour
l'exercice, sans destinataire réel ni enjeu. Et ils sont peu nombreux, donc aucun taux ne se calcule
dessus.

Le premier défaut tire vers une voix jouée : celle que la personne pense avoir, ou veut montrer.
C'est le même écart déclaratif que la section 6, passé de la déclaration à la production.

Ce que la recherche donne, et ce qu'elle ne donne pas. Aucune étude trouvée ne mesure l'effet
d'écrire un texte sous observation, pour un exercice, sur les traits de style de ce texte. Deux
résultats voisins rendent le risque plausible sans le chiffrer.

- Le paradoxe de l'observateur (Labov 1972, _Sociolinguistic Patterns_) : on cherche comment les
  gens parlent quand on ne les observe pas, et on ne peut l'apprendre qu'en les observant. Chez
  Labov, le style se déplace avec l'attention portée à sa propre parole. C'est un résultat sur
  l'oral, et Bell (1984) conteste que l'attention soit le bon facteur, au profit du destinataire.
  L'écrit est déjà un mode surveillé ; le transfert n'est pas établi.
- Brennan, Afroz & Greenstadt (2012) montrent que des scripteurs non professionnels, sur consigne,
  déplacent leur style assez pour tromper la stylométrie (obfuscation ramenée au hasard, imitation
  réussie jusqu'à 67 % des cas selon la technique). Le style est donc pilotable quand on le vise. Un
  texte écrit pour montrer sa voix peut en dériver sans que la personne le décide.

Il ne faut pas emprunter d'appui à la littérature sur la verbalisation (Fox et al. 2011 ; Yang,
Zhang & Parr 2020) : elle mesure l'effet de penser à voix haute en écrivant, pas celui d'être
observé. Elle justifie seulement de ne pas faire commenter la personne pendant qu'elle écrit.

Parades partielles : préférer un texte que la personne a réellement à envoyer ; la consigne « écris
comme tu l'enverrais, pas comme tu aimerais écrire » ; le marquage des coupes, qui fait jouer le
test de survie à l'auto-révision ; la provenance `séance`, qui reste visible dans `voix.md` et pèse
moins qu'une occurrence de corpus. Ce sont des parades, pas des corrections.

Les écrans de la séance (étape 7) ont la limite inverse : ce sont des choix entre des variantes
construites par l'agent, donc un trait qui n'apparaît dans aucune variante ne peut pas être choisi.
Partir des phrases de la personne, jamais de celles de l'agent, limite ce biais sans l'annuler.

Un profil issu du seul parcours sans corpus est donc à reprendre dès que des textes réels existent.
`skill-learn` peut le faire, et le `changelog.md` de l'instance dit d'où venait chaque trait.
