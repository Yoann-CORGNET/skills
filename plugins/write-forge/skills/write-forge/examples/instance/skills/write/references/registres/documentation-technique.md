---
id: documentation-technique
libelle: "Documentation technique"
norme-empan:
  "Court par unité, complet par ensemble : phrases de 8 à 18 mots, paragraphes de 1 à 3 phrases, une
  page ou section tient seule. Densité haute, une instruction ou un fait par phrase. Digression
  nulle : l'explication de fond est séparée de la référence."
surcharge: [liste-entete, resume-de-section, plan-mecanique]
postures: []
---

# Registre : documentation technique

Écrit de référence, consulté par fragments pour accomplir une tâche ou vérifier un détail, pas lu en
continu.

## Caractéristiques situationnelles

- **Canal** : pages ou fichiers indexés, navigables par recherche, sommaire et liens.
- **Production** : écrit pour durer, souvent en parallèle de l'objet décrit, et réécrit à chaque
  changement de celui-ci.
- **Révision** : continue. Un texte obsolète est pire qu'un texte absent, donc il se date ou se
  versionne et il est facile à corriger.
- **Lecture** : par fragments. Le lecteur arrive par recherche ou par lien, sur une section, avec
  une tâche en cours, et part dès qu'il a sa réponse. Il ne lit ni ce qui précède ni ce qui suit.
- **Persistance** : longue, mais mouvante. Le texte est lu contre un état courant de l'objet décrit.

## Contraintes dures de forme

- **Chaque section tient seule** : elle redonne le minimum de contexte (de quoi on parle, pour quoi
  faire) plutôt que de renvoyer à « comme vu plus haut ».
- **Titre informatif et stable** : il dit la tâche ou l'objet (verbe d'action pour une procédure,
  nom pour une référence). Les titres servent d'ancres, on ne les renomme pas à la légère.
- **Quatre natures de contenu, jamais mélangées dans un même passage** : tutoriel (apprendre),
  procédure (accomplir une tâche), référence (consulter un fait), explication (comprendre pourquoi).
  Un passage dit à quelle nature il appartient par sa forme.
- **Procédure** : étapes numérotées, une action par étape, à l'impératif, dans l'ordre d'exécution.
  Le résultat attendu est dit après l'étape qui le produit.
- **Référence** : gabarit identique pour chaque entrée du même type (nom, rôle, paramètres, valeur
  par défaut, erreurs). L'uniformité est ce qui permet de balayer.
- **Éléments littéraux** : tout ce qu'on tape, voit ou nomme dans l'objet décrit (commande, chemin,
  champ, valeur) est en code. Exemples exécutables, complets, qui marchent copiés tels quels.
- **Avertissements** : placés avant l'étape qu'ils concernent, courts, réservés à ce qui peut causer
  une perte ou une panne.
- **Terminologie fixe** : un seul mot par concept dans tout l'ensemble, sans variation.
- **Datation** : version de l'objet décrit couverte par la page quand cela change le contenu.

## Norme d'empan

La référence est l'entrée de dictionnaire technique : phrases courtes, déclaratives, une information
chacune. Le paragraphe dépasse rarement trois phrases. La densité est haute mais la redondance
volontaire (rappel de contexte par section) est admise, parce que le lecteur ne voit qu'un fragment.
L'explication de fond vit dans ses propres pages, pas au milieu d'une procédure. La digression est
exclue.

## Surcharges déclarées

- `liste-entete` : une entrée de référence est précisément une liste de paires nom, description
  (paramètres, options, champs). Le lecteur balaie la colonne des noms. Cette forme est la
  convention fonctionnelle du genre, pas un réflexe de mise en forme.
- `resume-de-section` : une section lue seule ne peut pas compter sur l'ouverture de la suivante. Un
  rappel court du résultat ou de l'état atteint en fin de procédure est utile au lecteur qui n'a pas
  lu le reste.
- `plan-mecanique` : le gabarit répété d'une page à l'autre (même suite de sections pour chaque
  entrée du même type) est voulu : il permet de retrouver l'information par position.

Les surcharges ne lèvent aucune règle d'attribution ni de ton : une doc ne vante pas ce qu'elle
décrit.

## Noyau neutre

La structure (sections autonomes, gabarit par type d'entrée, code pour les littéraux) est la même
dans toute langue. Pas de formule d'ouverture ou de clôture : la page commence par son objet. La
politesse d'adresse n'a pas de place ici, et le choix de l'adresse à la personne relève d'ailleurs
de la couche Audience.

## Français

- Titres et intertitres : majuscule initiale seulement, sans point final.
- Procédures à l'infinitif ou à l'impératif, choisi une fois pour tout l'ensemble.
- Ponctuation : espace insécable avant `:`, `;`, `?`, `!` ; guillemets `« »` hors blocs de code.

## English

- Headings: sentence case, no final period. Procedures in the imperative.
- Punctuation: no space before `:`, `;`, `?`, `!` ; double quotation marks outside code blocks.
- Spelling variant (US or UK) fixed once for the whole set.
