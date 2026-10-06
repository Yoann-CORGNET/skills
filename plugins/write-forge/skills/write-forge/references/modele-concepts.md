# Modèle conceptuel

Fichier de référence de `write-forge`. Il fixe le découpage en couches, le critère qui sépare la
Voix du Registre, et la procédure que suit un agent qui tient un trait et doit décider où le ranger.
Le détail par composante vit dans `composantes-voix.md` et `composantes-posture.md`. Ici, seulement
la règle de placement.

## 1. Les quatre couches

Préséance stricte : **Registre > Audience > Posture > Voix**. Une couche de rang supérieur borne les
suivantes. Une couche de rang inférieur remplit l'espace laissé libre et n'écrase rien.

| Couche   | Ce qu'elle fournit                                                            | Nature              |
| -------- | ----------------------------------------------------------------------------- | ------------------- |
| Registre | la **forme** : les réalisations que le genre rend disponibles ou interdit     | contrainte dure     |
| Audience | les **entrées** : K, P, D réels                                               | donnée de contexte  |
| Posture  | la **dose** : la valeur jouée sur chaque composante, pour une relation donnée | valeur jouée        |
| Voix     | la **direction** : le côté de l'axe vers lequel la personne penche par défaut | tendance par défaut |

La formule courte, à retenir telle quelle : **Voix = direction, Posture = dose, Registre = forme.**

### Audience contre Posture

L'Audience porte des entrées **réelles** : asymétrie de connaissance (K), pouvoir (P), distance
sociale (D). Ce sont des faits de situation, jamais des valeurs à jouer. La Posture porte ce que le
texte fabrique à partir de ces entrées.

Les deux se dissocient. Heritage (2012) sépare l'_epistemic status_, qui sait réellement quoi, de
l'_epistemic stance_, ce que la forme grammaticale affiche, et pose que la seconde peut dissimuler
le premier. C'est ce qui rend possible une posture délibérément non authentique : un scripteur K+
qui joue K−, ou l'inverse.

Conséquence de nommage, à respecter littéralement : **ne jamais écrire « distance sociale » dans une
composante de posture**. La distance réelle appartient à l'Audience. La composante de posture qui
lui correspond est « Proximité construite », qui mesure la proximité que le texte fabrique,
indépendamment de la distance réelle.

Les trois entrées D, P et Rx (poids de l'imposition) viennent de Brown & Levinson (1987). La
référence est vérifiée ; le calcul de pondération qu'ils en tirent l'est seulement par sources
secondaires, **[PARTIELLEMENT VÉRIFIÉ]**, et rien ici n'en dépend.

### Ce que « tendance par défaut » veut dire

Un trait de Voix n'est pas inconditionnel. La préséance prévoit qu'une posture prime sur lui, et un
fichier de posture peut le suspendre explicitement par un `suspend:` déclaré (fondement : Goffman
1979, dissociation animator / author / principal).

Formulation interdite dans tout gabarit livré : toute phrase qui donne un invariant de voix pour
valable indépendamment de la posture active, ou qui l'énonce comme une invariance absolue. C'est une
erreur relevée dans un skill de rédaction réel, maintenu à la main, dont l'en-tête de `voix.md` est
contredit par ses propres fichiers de posture.

Formulation correcte : « tendance par défaut, qu'une posture peut surcharger en le déclarant ».

## 2. Le critère de séparation Voix / Registre

Biber & Conrad (2009) posent trois perspectives sur un même texte. Le **registre** regroupe les
traits fréquents parce que fonctionnellement adaptés à la situation. Le **genre** regroupe les
structures conventionnelles qui construisent un texte complet. Le **style** regroupe le reste.
Verbatim, relevé sur l'extrait officiel de l'éditeur :

> The key difference from the register perspective is that the use of these features is not
> functionally motivated by the situational context; rather, style features reflect aesthetic
> preferences, associated with particular authors or historical periods.

Le test tient en une question : **le trait est-il exigé par la situation ?** Si oui, Registre. Si
non, et qu'il est constant chez la personne, Voix.

Attribution, parce qu'elle se perd souvent : ce critère est de Biber & Conrad. Il ne vient pas du
_tenor_ de Halliday. Le tenor porte les relations de statut et de rôle entre participants ; il borne
l'Audience et la Posture, pas la frontière Voix / Registre. Lui attribuer le critère déplace la
frontière au mauvais endroit.

Un trait de style peut porter une fonction **sémantique** propre sans cesser d'être du style : ce
que la définition écarte, c'est la motivation par la **situation**. Le filtre 3 s'appuie sur cette
marge.

## 3. Le test de tri

Procédure de décision. Un agent qui a relevé un trait candidat l'y fait passer dans l'ordre. Les
filtres ne sont pas interchangeables : le filtre 1 peut éclater le trait en trois morceaux, et c'est
chaque morceau, pas le trait d'origine, qui descend au filtre 2.

**Entrée** : un trait candidat, formulé tel qu'observé, avec les passages de corpus qui l'attestent.
**Sortie** : un placement par morceau (Voix, Posture, Registre, écarté), plus un statut de confiance
(constaté sur corpus, ou hypothèse à vérifier).

### Filtre 1. Forme

Question : **l'énoncé du trait nomme-t-il une forme figurant dans les listes de marqueurs des
composantes de posture ?**

Liste de contrôle, tirée du champ « marqueurs observables » de `composantes-posture.md` : question,
hedge ou atténuateur, conditionnel, humour et plaisanterie, tutoiement, adresse au lecteur (deuxième
personne, impératif adressé, « on » inclusif), auto-mention. Cette liste est la version courte ; la
liste qui fait foi est celle des sept composantes.

1. **La forme n'y figure pas.** Le trait passe au filtre 2 tel quel.
2. **La forme y figure et elle a une fonction interpersonnelle.** Le trait est **mal placé** en
   Voix. Le scinder en trois, puis traiter chaque morceau séparément :
   - la **direction** (sur quel axe, vers quel pôle) reste en Voix, reformulée **sans nommer la
     forme**, et descend au filtre 2 ;
   - la **dose** (combien, pour quelle relation) descend en Posture ;
   - la **forme** (par quel moyen le genre permet de la réaliser) remonte au Registre.
3. **La forme y figure mais elle est idiolectale, sans fonction interpersonnelle.** Elle reste
   légitimement en Voix et passe au filtre 2. Le slash `/` et les autres traits de signature
   typographique relèvent de ce cas.

Test de la fonction interpersonnelle, quand le cas 2 et le cas 3 ne se départagent pas à vue : la
forme sert-elle à régler le rapport au lecteur ou au désaccord, c'est-à-dire à menacer ou atténuer
une face, à ouvrir ou fermer l'espace laissé aux positions adverses, à rapprocher ou éloigner, à
faire exister le lecteur dans la phrase ? Si oui, cas 2. Si sa suppression ne change que la densité
d'écriture et laisse le rapport au lecteur intact, cas 3.

Pourquoi cette règle, et sur quoi elle repose. Les composantes de posture sont des axes de
**fonction**, pas de forme, et une même forme réalise plusieurs axes à la fois. Une forme qui
apparaît dans ces listes réalise donc un axe interpersonnel ; ce que le texte en fait se mesure en
quantité, donc en dose ; et la dose appartient à la Posture par préséance. Un trait de Voix qui
nomme une telle forme fixe une dose depuis la couche la plus basse, ce que la préséance interdit. Ce
raisonnement se tient seul et ne s'appuie sur aucune numérotation de stratégies de politesse.

### Filtre 2. Persistance

Ne s'applique qu'à ce que le filtre 1 a laissé en Voix. Question : **la direction persiste-t-elle
dans l'espace que le Registre et la Posture laissent libre ?**

Deux variations, menées à contenu constant.

- **Variation de registre**, relation constante. Écrire le même contenu dans deux genres aux
  conventions opposées. Si la réalisation change mais que la direction reste du même côté de l'axe,
  la forme était du Registre et la direction survit. Si la direction elle-même s'inverse, le genre
  la dictait et il n'y a pas de trait de personne à extraire.
- **Variation de relation ou de but**, registre constant. Même contenu, destinataire ou objectif
  différent. Si seule l'amplitude bouge, c'est une dose de Posture et la direction reste intacte. Si
  le signe s'inverse, la direction était pilotée par la situation : elle appartient à la Posture.

**Règle de lecture, la seule qui compte ici : un changement d'amplitude ne réfute rien. Une
inversion de signe réfute.** Et une inversion observée dans un contexte où une posture est active,
avec ce trait dans son `suspend:`, n'est pas un contre-exemple : c'est la préséance qui s'applique.

L'ancrage théorique est le critère du §2. Un trait qui varie avec la situation est motivé
fonctionnellement par elle, donc du Registre au sens de Biber & Conrad. Un trait qui traverse les
variations sans changer de signe ne l'est pas.

### Filtre 3. Intentionnalité

Ne s'applique qu'aux traits que les filtres 1 et 2 ont laissés en Voix. Question : **la personne
endosse-t-elle ce trait, ou le tient-elle pour un tic ?**

Ce filtre **ne se tranche jamais sans la personne**. Trois tests l'instrumentent, aucun ne le clôt.

**Test de substitution et de charge fonctionnelle.** Remplacer le trait par son équivalent neutre le
plus proche, et regarder ce que ça coûte. Trois issues :

- une seule substitution évidente existe et elle préserve l'information : le trait était une
  abréviation de surface, verdict faible, passer au test suivant ;
- la substitution oblige à **choisir** entre plusieurs sens que le trait laissait indistincts : le
  trait **sous-spécifiait**, ce qui est l'indice le plus net en faveur du tic ;
- aucune substitution simple ne reproduit l'effet, il faut une proposition entière : le trait porte
  une charge fonctionnelle réelle, indice fort en faveur de la Voix.

**Test de survie à l'auto-révision.** Le trait apparaît-il dans les textes que la personne a relus
et qui lui importaient, ou seulement dans les écrits bruts ? Un trait qui ne survit pas au passage
de relecture de la personne elle-même est un artefact de faible attention. Ce test **prime sur la
préférence déclarée** : ce que la personne a fait en relisant pèse plus que ce qu'elle dit préférer.

**Test de contrôlabilité et de coût.** Demander un texte écrit en supprimant délibérément le trait,
puis demander ce que ça a coûté. Suppression facile et texte qui ne paraît pas appauvri : tic.
Suppression pénible et résultat qui ne semble plus être d'elle : Voix. Le test est praticable parce
que l'obfuscation stylistique manuelle marche : Brennan, Afroz & Greenstadt (2012) établissent qu'un
scripteur qui s'y met rend la stylométrie non fiable.

**Ce que le filtre produit.** Les trois tests produisent des observations, pas un verdict. « Tic »
est une catégorie **évaluative**, et aucun cadre consulté ne la définit par opposition au style. La
stylométrie étudie les traits indépendamment de l'intention ; les _composition studies_, depuis
Matsuda (2001), définissent la voix de manière à inclure explicitement ce qui est choisi «
deliberately or otherwise ». Décider qu'un trait sort de la voix relève du _self as author_ d'Ivanič
(1998), l'acte par lequel le scripteur assume ou refuse ce qu'il produit, et non du _discoursal
self_ que l'observation suffit à décrire.

**Comment l'agent s'en sert.** Présenter le résultat des trois tests, puis demander l'arbitrage.
Jamais « est-ce que tu aimes ça ? », qui fait tourner l'élicitation en rond. Le rangement de sortie
comporte deux emplacements distincts : les invariants endossés, et les **traits observés mais non
endossés**, chacun accompagné du registre où il reste toléré.

### Récapitulatif

| Filtre             | Question                                              | Ce qu'il produit                                  |
| ------------------ | ----------------------------------------------------- | ------------------------------------------------- |
| 1. Forme           | le trait nomme-t-il une forme des listes de posture ? | un éclatement direction / dose / forme            |
| 2. Persistance     | la direction survit-elle aux deux variations ?        | Voix confirmée, ou renvoi Posture / Registre      |
| 3. Intentionnalité | la personne endosse-t-elle le trait ?                 | des éléments à charge, et un arbitrage à demander |

## 4. Cas travaillé : « face à un désaccord, sonder par une question plutôt qu'asserter »

Le cas pédagogique du filtre de forme. Il vient d'un cas réel, un profil de voix écrit à la main où
ce trait figurait deux fois : comme invariant de voix, et comme calibrage de la posture Pair. Le
doublon venait de ce qu'un seul trait y était décrit à la mauvaise granularité aux deux endroits.

### Filtre 1

« Question » figure dans les listes de marqueurs de posture, à trois endroits : les questions
expositives en Ouverture dialogique, la forme interrogative employée en lieu et place d'une
assertion en Franchise, les questions adressées au lecteur en Adresse au lecteur. Fonction
interpersonnelle : la question règle à la fois l'espace laissé aux positions adverses et la menace
de face que porte un désaccord. Cas 2, donc **trait mal placé en Voix**.

Scission :

- **Direction, reste en Voix** : devant un désaccord, le premier mouvement est expansif plutôt que
  contractif. Aucune forme nommée, aucune quantité fixée.
- **Dose, descend en Posture** : combien d'atténuation, et sur le territoire de qui. Pour la
  relation de pair, ni désaccord frontal ni sur-atténuation : interrogative directe posée sur le
  territoire du lecteur, sans préface d'excuse ni emballage de compliment.
- **Forme, remonte au Registre** : l'email autorise l'interrogation adressée. Le rapport technique
  et le papier de recherche ne l'autorisent pas au même titre, et le même geste s'y réalise
  autrement : « l'hypothèse X n'a pas été testée sur le cas Y », « il reste à établir si ».

Le filtre fait apparaître au passage une **quatrième** chose que la formule condensait : interroger
le lecteur sur son propre domaine lui reconnaît son statut K+, ce qui relève de la composante Droit
à affirmer. Une phrase de six mots portait trois axes et une forme.

### Filtre 2

Variation de registre : la réalisation change, le signe ne change pas. Variation de relation : la
quantité et la fonction bougent (socratique face à quelqu'un qui se trompe, accroche en posture
Provocateur) sans que le signe s'inverse hors Provocateur.

Statut de ce résultat : **hypothèse**. Aucune des deux variations n'a été menée sur le corpus de la
personne dont vient le cas. Le raisonnement est solide, les données manquent, et un fichier généré
doit le porter comme tel.

### Filtre 3

À mener sur la direction reformulée, pas sur la formule d'origine. Point à ne pas escamoter : la
personne avait endossé une formulation qui nommait la forme. Ce qui reste après scission est un
énoncé différent, et il demande un **nouvel endossement**.

### La même fuite ailleurs

Ce `voix.md` porte aussi, sous « philosophie de fond », l'idée que l'humour sert à prendre du recul
sur le cadre. L'humour figure dans les marqueurs de Proximité construite. Découpage correct : la
direction, « prendre de la distance avec le cadre plutôt que chercher la connivence », reste en Voix
sans nommer l'humour ; la quantité d'humour et son destinataire descendent en Posture.

## 5. Second cas : `=>` contre le slash `/`

Le cas de référence du filtre d'intentionnalité. Les deux signes appartiennent à la même composante
de voix (Signature typographique), tous deux sont fréquents, tous deux sont stables, tous deux sont
probablement apparus sans intention, et la personne sait commenter les deux. Un critère qui ne les
sépare pas ne sert à rien, et les critères évidents échouent tous :

- la **délibération** échoue par construction, puisque Matsuda (2001) inclut dans la voix ce qui est
  choisi « deliberately or otherwise » ;
- la **stabilité** échoue, les deux sont stables, et la stylométrie vise précisément l'involontaire
  stable ;
- la **conscience métalinguistique** échoue, la personne peut nommer les deux ;
- la **fréquence** échoue, et elle est dangereuse : elle canonise le tic le plus répandu.

### Ce que le test de substitution donne

`=>` : pour le remplacer, il faut trancher entre « donc », « d'où » et « devient ». La flèche
cachait au lecteur une relation logique que le scripteur n'avait pas tranchée. Deuxième issue, et
systématiquement.

Le slash : « forces/limites » se réécrit « forces et limites », un mot pour un signe, rien de perdu,
première issue. « problème/feature » demanderait « à la fois un problème et une fonctionnalité selon
le point de vue adopté », dix mots pour deux, troisième issue. Le slash tombe tantôt en première
issue, tantôt en troisième, **jamais en deuxième**. Il ne sous-spécifie pas.

C'est cette asymétrie qui sépare la paire, et elle ne demande à aucun moment de deviner lequel des
deux était délibéré.

### Ce que le test ne fait pas

Il **instrumente** la question, il ne la **clôt pas**. Ce qu'il produit est une observation : «
sous-spécifie » contre « ne sous-spécifie pas ». Il ne produit pas « tic ». L'étiquette de tic est
évaluative, et c'est la personne qui l'a appliquée. Ce que `write-forge` doit retenir : le
méta-skill amène la personne devant une observation nette, puis lui laisse l'arbitrage.

### État réel de l'application

Honnêteté sur ce qui a servi. Seul le test de substitution a été mené. La survie à l'auto-révision
est **inférée** d'une remarque du `voix.md` selon laquelle `=>` « apparaît beaucoup dans les écrits
bruts », ce qui ne dit pas qu'il est absent des textes révisés. La contrôlabilité n'a jamais été
testée. La décision existante est donc retrouvée par un seul chemin, et parler de convergence des
trois tests serait faux.

## 6. Contrepartie assumée du découpage

Le filtre de forme a un prix, et c'est le filtre de persistance qui le paie.

Puisque la préséance prévoit qu'une posture prime sur un trait de voix, **une surcharge par une
posture ne réfute pas ce trait**. Le filtre 2 ne peut donc jamais être mis en échec par une
observation prise dans un contexte où une posture est active. Le cas travaillé du §4 le montre : en
posture Provocateur, la question devient une accroche et le premier mouvement peut devenir
contractif, ce qui est exactement l'inversion de signe que le filtre 2 traite comme réfutante. Elle
ne compte pas, parce qu'une posture était active.

Conséquence : le filtre 2 est **plus faible qu'une falsification sèche**. Il écarte les traits qui
s'inversent dans l'espace libre, pas ceux dont l'inversion peut toujours être imputée à une posture.
À la limite, un trait de voix suffisamment vague survit à tout.

Ce qui limite la casse, et qui relève du raisonnement propre à ce fichier plutôt que d'une source :
une inversion ne peut être écartée que par un `suspend:` **déjà déclaré** dans le fichier de posture
concerné, jamais par un `suspend:` ajouté après coup pour expliquer le contre-exemple. Le validateur
d'instance vérifie l'existence des identifiants suspendus, et l'ordre d'écriture fait le reste. Ça
resserre la faille, ça ne la ferme pas.

Deux garde-fous complètent le dispositif, et il faut les nommer plutôt que de compter sur le filtre
2 seul :

- le nombre de traits de voix retenus reste petit, et chacun doit s'appuyer sur des passages de
  corpus identifiés ;
- un trait dont la direction ne s'observe que dans un seul registre ou face à un seul type
  d'interlocuteur se range en Posture, pas en Voix, même si rien ne l'a réfuté.

Limite de fond, à écrire dans les fichiers livrés plutôt qu'à garder pour soi : il n'existe pas
d'ensemble de comparaison. Grant (2007) montre qu'un corpus de référence trop mince impose de
conclure qu'aucune attribution n'est possible, et `write-forge` travaille précisément dans ces
conditions. Ce qu'il produit est un profil de sélection utile, pas une attribution.

## Références

Toutes les références ci-dessous ont été vérifiées par requête sur le DOI ou auprès de l'éditeur,
sauf mention contraire. Les réserves sont conservées telles quelles.

- Biber, D. & Conrad, S. (2009). _Register, Genre, and Style_. Cambridge Textbooks in Linguistics,
  Cambridge University Press. DOI 10.1017/cbo9780511814358. 2e éd. 2019, DOI 10.1017/9781108686136.
  La citation verbatim du §2 a été relevée sur l'extrait officiel de l'éditeur.
- Brennan, M., Afroz, S. & Greenstadt, R. (2012). « Adversarial stylometry ». _ACM Transactions on
  Information and System Security_ 15(3), art. 12, 1-22. DOI 10.1145/2382448.2382450. Le résultat
  utilisé (l'obfuscation et l'imitation manuelles suffisent à rendre la stylométrie non fiable,
  contrairement à la traduction automatique) est confirmé par sources secondaires concordantes,
  **[NON VÉRIFIÉ]** sur le texte intégral.
- Brown, P. & Levinson, S. C. (1987). _Politeness: Some Universals in Language Usage_. Cambridge
  University Press. Première parution 1978 dans E. Goody (éd.), _Questions and Politeness_.
  Référence vérifiée. Le calcul de pondération à partir de D, P et Rx est **[PARTIELLEMENT
  VÉRIFIÉ]** : sources secondaires concordantes, primaire sous paywall. La numérotation des
  stratégies de politesse n'est invoquée nulle part dans ce fichier.
- Goffman, E. (1979). « Footing ». _Semiotica_ 25(1-2), 1-29 ; repris dans _Forms of Talk_ (1981),
  University of Pennsylvania Press. Format de production animator / author / principal.
- Grant, T. (2007). « Quantifying evidence in forensic authorship analysis ». _International Journal
  of Speech, Language and the Law_ 14(1), 1-25. DOI 10.1558/ijsll.v14i1.1. Résumé consulté : un
  corpus de référence trop mince impose de conclure à l'impossibilité d'attribuer.
- Halliday, M. A. K. & Hasan, R. (1985). _Language, Context, and Text: Aspects of Language in a
  Social-Semiotic Perspective_. Le libellé du _tenor_ est vérifié via sources secondaires
  universitaires concordantes ; **[NON VÉRIFIÉ]** pour l'éditeur et l'année exacts (Deakin
  University Press 1985 ou Oxford University Press 1989 selon les éditions) et pour la pagination.
  Cité ici seulement pour écarter une attribution fautive.
- Heritage, J. (2012). « Epistemics in Action: Action Formation and Territories of Knowledge ».
  _Research on Language and Social Interaction_ 45(1), 1-29. DOI 10.1080/08351813.2012.646684.
  L'accès s'est limité au résumé, d'où une reformulation et non une citation.
- Ivanič, R. (1998). _Writing and Identity: The Discoursal Construction of Identity in Academic
  Writing_. Studies in Written Language and Literacy 5, Amsterdam : John Benjamins. Les **quatre**
  aspects du soi (_autobiographical self_, _discoursal self_, _self as author_, _possibilities for
  selfhood_) sont confirmés par plusieurs sources secondaires concordantes ; **[NON VÉRIFIÉ]** sur
  le texte original. Le modèle en compte quatre, pas trois.
- Matsuda, P. K. (2001). « Voice in Japanese written discourse: Implications for second language
  writing ». _Journal of Second Language Writing_ 10(1-2), 35-53. DOI 10.1016/s1060-3743(00)00036-9.
  Définition de la voix citée verbatim, confirmée par plusieurs sources secondaires concordantes ;
  **[NON VÉRIFIÉ]** sur le texte original.
