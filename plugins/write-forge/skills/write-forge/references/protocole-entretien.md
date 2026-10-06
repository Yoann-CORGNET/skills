# Entretien approfondi

Option proposée à l'étape 0 du protocole d'extraction (« Inclure un protocole de questions-réponses
et cas d'usage »). Malgré son nom, ce n'est pas une discussion sur le style : c'est une séance où la
personne **écrit**, puis tranche à l'aveugle entre des variantes de ses propres phrases. Elle sert à
tirer un maximum de matériau d'une personne qui a peu de textes, ou aucun. Elle ne remplace pas la
règle de preuve : elle fabrique la preuve en séance au lieu de la chercher dans un corpus.

Ce fichier distingue ce qui s'appuie sur une source de ce qui est posé sans appui publié. Les
seconds portent la marque [CHOIX D'INGÉNIERIE] et sont rassemblés dans la section « Ce qui est posé,
pas dérivé ». Sources en fin de fichier.

Durée : 30 à 40 minutes pour la personne [CHOIX D'INGÉNIERIE]. Langue : celle fixée à l'étape 0,
pour chaque consigne, chaque phrase et chaque écran.

## Pourquoi cette forme

Ce qui rapporte le plus, dans l'ordre : la production en séance, surtout le texte long ; les écrans
aveugles sur les phrases de la personne ; la calibration des postures. Les récits, la correction de
brouillons générés et les questions de jugement sur des textes d'autrui rapportent peu, et la séance
les écarte. Ce classement repose sur un seul usage réel (voir « Ce qui est posé, pas dérivé »).

D'où la règle de cette séance : **la personne produit ou choisit, elle ne commente pas.** C'est
l'extension de la règle de l'étape 6 (demander une action plutôt qu'une explication) jusqu'au bout.

## Placement dans le protocole

- **Sans corpus.** La séance démarre juste après l'étape 0. Ses blocs A à C produisent le matériau,
  qui passe ensuite par les étapes 1 à 5 comme un corpus ordinaire. L'étape 6 (récits) est sautée et
  le saut s'écrit dans `corpus-index.md`. Les étapes 7 à 12 suivent, avec les écrans élargis décrits
  au bloc D.
- **Avec un corpus.** La séance s'ajoute au protocole standard, après l'étape 5. L'étape 6 est
  gardée : sur un corpus, ses relances s'ancrent sur des textes réels, ce que la séance ne remplace
  pas. Les textes de séance rejoignent la table de qualification.

## Ce qu'on dit à la personne, et quand

Avant la séance, une ligne par bloc sur son but, sans nommer les composantes : « tu vas écrire
quelques textes courts et un long », « puis tu choisiras entre des versions de tes propres phrases
». Nommer les composantes avant la production pousse à écrire « pour » une composante.

Après la production (bloc C), l'agent explique ce qu'il extrait : les huit composantes de voix et
les sept axes de posture, en une phrase chacun, et ce que chaque texte a servi à observer. Sans
cette explication, les exercices passent pour arbitraires.

## Bloc A. Cadrage par écran

2 minutes. Aucun récit.

Un écran de choix, en choix multiple : à qui la personne écrit le plus (les quatre contrastes de
destinataire : proche de même rang, quelqu'un qui a du pouvoir sur elle, quelqu'un qui en sait plus,
quelqu'un qui en sait moins), et si elle doit refuser ou contredire par écrit. Puis une question
ouverte, facultative : « Un texte que tu dois écrire dans les jours qui viennent ? » Les textes
réels sont les meilleurs sujets du bloc B.

Sortie : la liste des situations à couvrir au bloc B, rangées sous un `id` de registre et en K, P, D
et N. Elle sert d'ancrage aux étapes 9a et 10.

## Bloc B. Production en séance

15 à 20 minutes. C'est le cœur de la séance : la personne écrit, l'agent regarde.

L'agent fixe quatre à six textes [CHOIX D'INGÉNIERIE] qui, ensemble, couvrent :

- **au moins deux registres et au moins deux des quatre contrastes de destinataire**, idéalement les
  quatre. Sans cette couverture, le routage de l'étape 4 n'a rien à comparer et la lecture des
  contrastes de l'étape 9a non plus ;
- **un texte long, de 300 mots ou plus** [CHOIX D'INGÉNIERIE], compté et non estimé. C'est la seule
  source du Geste rhétorique, de l'Architecture et du Regard dans ce parcours. Un texte sous le
  seuil ne s'appelle pas long, et ces composantes restent alors non extraites, avec ce motif ;
- **un texte de refus ou de désaccord** : refuser une demande, contester une décision. Sans lui, les
  postures `arbitre` et `contradicteur` n'ont aucun ancrage ;
- **un texte hors du domaine principal** de la personne (un message personnel, un avis sur un sujet
  sans rapport avec son métier). Sans lui, un mot récurrent ne se distingue pas d'un mot de sujet :
  sur des textes tous techniques, le lexique observé peut venir du domaine et non de la voix.
  L'étape 5 confine alors un lexème à un sujet comme l'étape 4 le confine à un registre.

Les genres choisis laissent de la place à la voix : explication, avis, message à un pair, refus. Un
genre où le registre occupe tout l'espace (formulaire administratif, section de référence d'une
documentation) ne rapporte rien.

Consignes données à la personne, telles quelles :

- Prendre de préférence un texte qu'elle a réellement à envoyer. Un texte inventé pour l'exercice
  tire vers une voix jouée. [CHOIX D'INGÉNIERIE]
- « Écris-le comme tu l'enverrais, pas comme tu aimerais écrire. » [CHOIX D'INGÉNIERIE]
- Sans IA, sans correcteur autre que celui qu'elle utilise d'habitude, sans limite de temps.
- Écrire en silence. L'agent ne demande pas de commenter pendant l'écriture : verbaliser en écrivant
  a un effet mesuré, faible mais réel, sur certains traits du texte produit (Yang, Zhang & Parr
  2020).

Chaque texte reçoit une ligne dans `corpus-index.md`, support `séance`, statut `brut`, avec son
sujet, pour que l'étape 5 puisse séparer voix et sujet.

Deux cas à traiter sans les rejeter :

- **Un texte produit hors consigne**, par exemple écrit spontanément pendant le cadrage. Il compte
  comme texte de séance, avec sa ligne et la mention de ses conditions.
- **Une demande d'ignorer l'orthographe ou la forme.** Le texte reste utilisable pour les
  composantes de discours, mais la Signature typographique (composante 2) n'est pas extractible
  dessus. La mention s'écrit sur sa ligne dans `corpus-index.md`.

## Bloc C. Test de survie

3 minutes. Deux variantes, par ordre de préférence.

1. **Marquage des coupes.** Sur deux de ses textes du bloc B, la personne marque seulement ce
   qu'elle couperait ou changerait avant un envoi réel, sans réécrire le reste. C'est un
   comportement de révision observé : chaque texte et sa version marquée forment une paire brut /
   auto-révisé, statut `auto-révisé`, et l'étape 8 s'applique avec la clause 3 de la règle de
   preuve.
2. **Écrans d'allègement**, si la personne refuse de relire. Pour chaque trait candidat présent dans
   ses textes, un écran : sa phrase telle quelle, et la même phrase sans le trait. « Laquelle tu
   envoies ? » Ce sont des écrans de l'étape 7b, rien de plus. Ils ne produisent **aucune** paire
   brut / auto-révisé, l'étape 8 reste sautée, et la clause 3 de la règle de preuve ne s'applique
   pas.

Déléguer la correction à l'agent et déclarer le reste acceptable n'est ni l'une ni l'autre. C'est un
jugement, pas un comportement : l'étape 8 reste sautée, et le statut s'écrit tel quel dans
`corpus-index.md` (« orthographe révisée par l'agent, reste accepté par la personne »).

## Bloc D. Écrans élargis

Rattaché à l'étape 7b, dont toutes les règles valent, règle 3 comprise : un seul axe varie par
écran. La séance élargit seulement ce que les écrans couvrent.

- **Un écran par lexème candidat.** Il sépare des classes de mots que le comptage confond, par
  exemple, parmi des emprunts, un jargon technique gardé et des mots courants rejetés à l'aveugle.
- **Des écrans de typographie**, un par signe candidat (point-virgule, slash, deux-points, tiret,
  guillemets). Sans eux, la composante 2 repose sur la seule occurrence.
- **La phrase de base** vient d'un texte du bloc B, jamais d'un texte de l'agent.
- **Le plafond de six écrans de l'étape 7b est levé** dans le parcours sans corpus : faute
  d'occurrence de corpus, un trait ne se valide que par deux écrans convergents, ou par un écran et
  une occurrence de séance. Ordre de priorité si le temps manque : lexèmes, puis traits plats sur
  tous les registres, puis typographie.

Les réponses libres et les pièges de construction se traitent comme à l'étape 7b.

## Bloc E. Couverture des composantes

Agent seul, avant de clore. L'agent vérifie, composante par composante, qu'un bloc a fourni du
matériau. Le Lexique de prédilection et l'Architecture du propos restent vides quand aucun bloc ne
les vise.

| Composante                 | D'où vient le matériau dans ce parcours                   |
| -------------------------- | --------------------------------------------------------- |
| 1. Substrat                | nulle part, non extractible sans corpus                   |
| 2. Signature typographique | textes du bloc B, écrans de typographie du bloc D         |
| 3. Empan                   | textes du bloc B, en delta sur la norme du registre       |
| 4. Lexique de prédilection | texte hors domaine du bloc B, écrans de lexèmes du bloc D |
| 5. Geste rhétorique        | texte long du bloc B (300 mots ou plus)                   |
| 6. Architecture du propos  | texte long du bloc B (300 mots ou plus)                   |
| 7. Réflexe interpersonnel  | contrastes de destinataire du bloc B, texte de refus      |
| 8. Regard                  | texte long du bloc B, s'il en porte ; sinon non extrait   |

Une composante sans matériau reçoit une tâche de plus, une production ou un écran, jamais une
question d'explication. Pour l'Architecture : « Voici ton texte découpé en phrases, remets-les dans
l'ordre où tu les enverrais. » Si elle reste vide, elle s'écrit non extraite, avec son motif.

## Statut de ce qui sort

Chaque trait garde sa trace dans le champ `Provenance` de `voix.md`. Le classement des poids est
posé, pas mesuré [CHOIX D'INGÉNIERIE].

| Provenance  | D'où                                                | Poids                                     |
| ----------- | --------------------------------------------------- | ----------------------------------------- |
| `corpus`    | textes écrits et envoyés avant le protocole         | le plus fort                              |
| `séance`    | blocs B et C ; réponse libre à un écran             | plus faible que `corpus`, voir ci-dessous |
| `écran`     | deux écrans aveugles convergents                    | un choix, pas un comportement d'écriture  |
| `entretien` | récits de l'étape 6, parcours avec corpus seulement | philosophie de fond et Regard seulement   |

Un texte écrit en séance est écrit sous observation, pour le protocole, et souvent jamais envoyé. Il
tire vers une voix jouée, celle qu'on montre à l'agent. La règle de preuve le compte donc comme
occurrence, mais plus faible qu'une occurrence de corpus, et la provenance l'affiche. Détail dans
`limites.md`, section 11.

Ce que ça donne avec la règle de preuve, qui ne change pas :

- Une déclaration seule n'ajoute jamais un trait. Elle ouvre une hypothèse.
- Une hypothèse entre dans `voix.md` par l'étape 7 : deux écrans aveugles convergents, ou un écran
  et une occurrence de corpus ou de séance.
- Une même réponse ne compte jamais deux fois. Une réponse libre à un écran est une occurrence de
  séance, pas un choix d'écran ; elle ne peut pas servir à la fois d'écran et d'occurrence qui le
  corrobore.
- Une hypothèse qui ne passe pas les écrans va dans `voix-aspirations.md`.

C'est la voie par laquelle un trait qu'elle n'a pas encore, mais qu'elle choisit systématiquement à
l'aveugle, devient légitimement sa voix : ce qu'elle accepte d'envoyer sous son nom.

Sortie : les situations du bloc A, les textes de séance qualifiés dans `corpus-index.md` avec leur
sujet, les paires brut / auto-révisé s'il y en a, les hypothèses ouvertes avec leur provenance, et
la liste des composantes non extraites avec leur motif.

## Ce qui est posé, pas dérivé

Les éléments marqués [CHOIX D'INGÉNIERIE] ne reposent sur aucun résultat publié. Ils sont posés pour
que le protocole soit exécutable, et peuvent être révisés sans toucher au reste.

- **Les durées**, par bloc et au total. Estimations, pas mesures sur des sessions réelles.
- **Quatre à six textes en séance.** Le minimum vient de la couverture demandée ; le maximum, du
  temps qu'on peut raisonnablement demander. Aucun chiffre publié ne dit combien de textes courts
  suffisent à un profil de voix. DITTO (Shaikh et al. 2024) aligne un modèle sur moins de dix
  démonstrations, mais c'est un réglage de modèle, pas l'extraction d'un profil lisible.
- **300 mots pour un « texte long ».** Seuil pratique pour qu'un texte laisse un choix d'ordre aux
  composantes 5, 6 et 8. Les seuils de volume du protocole (Burrows, Eder) portent sur l'attribution
  d'auteur et ne s'appliquent pas ici.
- **Les deux consignes contre la voix jouée** (texte réellement à envoyer ; « comme tu l'enverrais
  »). Elles visent l'effet d'observation décrit dans `limites.md`, section 11, mais aucune étude ne
  montre qu'elles le réduisent.
- **La suppression des récits et des jugements** dans le parcours sans corpus. Elle repose sur un
  seul usage réel, pas sur une comparaison. Elle se révise si d'autres usages montrent le contraire.
- **Le classement des provenances.** Il suit le raisonnement de la règle de preuve (un comportement
  passé pèse plus qu'un comportement observé, qui pèse plus qu'un choix, qui pèse plus qu'une
  déclaration), pas une mesure.

## Sources

Les références de l'étape 6 et de l'étape 7 (Fox, Ericsson & Best 2011 ; Johansson et al. 2005) sont
citées dans `protocole-extraction.md`. Ajouts propres à ce fichier :

1. Shaikh, O., Lam, M., Hejna, J., Shao, Y., Bernstein, M. & Yang, D. (2024). « Show, Don't Tell:
   Aligning Language Models with Demonstrated Feedback ». arXiv:2406.00888. Appui indirect au petit
   volume ; c'est un réglage de modèle, pas une extraction.
2. Yang, C., Zhang, L.J. & Parr, J.M. (2020). « The reactivity of think-alouds in writing research:
   quantitative and qualitative evidence from writing in English as a foreign language ». _Reading
   and Writing_ 33, 451-483. Sur 85 étudiants écrivant en langue étrangère, la pensée à voix haute
   n'altère que 2 mesures sur 20, dont la diversité lexicale. Appui de la consigne d'écrire en
   silence ; ne dit rien de l'effet d'être observé sans verbaliser.
3. Labov, W. (1972). _Sociolinguistic Patterns_. Philadelphia : University of Pennsylvania Press.
   Paradoxe de l'observateur. Voir `limites.md`, section 11.
4. Brennan, M., Afroz, S. & Greenstadt, R. (2012), cité dans `modele-concepts.md`. Voir
   `limites.md`, section 11.

[PARTIELLEMENT VÉRIFIÉ] : titres, années, lieux et numéros arXiv vérifiés par recherche, articles
non lus en texte intégral.
