---
name: write
description:
  "Rédige tout texte ({{INVENTAIRE_REGISTRES}}) dans la voix éditoriale personnelle de
  {{NOM_PERSONNE}}, avec une posture et un registre adaptés au contexte. Toujours consulter ce skill
  dès qu'une tâche de rédaction est demandée, pas seulement pour du contenu long, aussi pour un
  email de deux lignes ou un commentaire, dès qu'il s'agit de produire du texte destiné à être lu
  par quelqu'un d'autre (pas pour du code, pas pour de l'analyse pure sans livrable texte)."
---

<!-- gabarit: {{INVENTAIRE_REGISTRES}} est généré depuis le contenu de references/registres/, jamais
     saisi à la main. {{NOM_PERSONNE}} reçoit le nom réel : la description est aussi le matcher, un
     placeholder littéral ferait déclencher le skill sur le mot « placeholder ». -->

# Rédaction personnelle, orchestrateur

Ce skill compose une rédaction à partir de 4 couches, combinées dans un ordre de préséance strict.
Ne jamais sauter l'Étape 0.

## Étape 0, vérification factuelle (invariante, avant tout)

Avant de rédiger quoi que ce soit à partir du contexte de la conversation :

- Identifier les affirmations factuelles, chiffres et arguments présents dans le contexte fourni.
- **Si le contexte contient de telles affirmations, lancer l'agent `{{NOM_PLUGIN}}:fact-checker`**,
  sauf s'il a déjà tourné plus tôt dans la session sur l'ensemble de ces affirmations. Un texte sans
  aucune affirmation à vérifier (un message de logistique de deux lignes) n'en a pas besoin.
- Consommer **le verdict et le score**, selon la table ci-dessous. Le score ne sert qu'à dégrader un
  verdict, jamais à le remonter.

| Sortie du fact-checker   | Ce que l'Étape 0 en fait                                         |
| ------------------------ | ---------------------------------------------------------------- |
| `verified`, score ≥ 0.70 | utilisable tel quel dans le texte                                |
| `verified`, score < 0.70 | traité comme `unsourced`                                         |
| `unsourced`              | jamais donné pour acquis : attribuer la source, ou retirer       |
| `doubtful`               | la contestation se dit dans le texte, ou l'affirmation se retire |
| `refuted`                | ne pas écrire l'affirmation                                      |
| `network-unavailable`    | toutes les affirmations externes passent en `unsourced`          |

Le seuil de 0.70 est un réglage de cette instance, pas une constante universelle. Le changer se
journalise dans `changelog.md`.

- **Faits internes hors de portée du fact-checker** : un fait interne au travail rapporté (chiffre
  d'effort, rôle, décision) qu'aucune source externe ne peut confirmer se marque et se liste dans le
  compte rendu de livraison, pour validation par l'auteur. Il ne se rédige jamais comme acquis sans
  ce passage.
- **Cette étape n'est jamais suspendable.** Aucune posture, aucun registre, aucune suspension
  déclarée ne la lève, y compris une posture qui joue la provocation. La posture reste responsable
  du contenu propositionnel qu'elle avance ; seul le **ton** du signalement varie selon la posture
  active (voir `${CLAUDE_PLUGIN_ROOT}/skills/write/references/postures/`).
- Ne jamais rédiger un texte qui présente comme acquis un fait que le contexte ne permet pas de
  vérifier.

## Ordre de préséance des couches

**Registre > Audience > Posture > Voix**

- Le **Registre** impose les contraintes dures de genre (format, longueur, plan, conventions). Il
  fournit la _forme_, et elle n'est pas négociable.
- L'**Audience** porte les entrées de contexte **réelles** : asymétrie de connaissance (K), pouvoir
  (P), distance sociale (D). Ce sont des entrées, jamais des valeurs jouées. Elle détermine le
  niveau de contenu et route vers la posture par défaut.
- La **Posture** est la valeur **jouée** sur chaque composante. Elle fournit la _dose_, dans les
  limites que Registre et Audience laissent. La proximité **construite** est de la Posture ; la
  distance sociale réelle reste de l'Audience.
- La **Voix** fournit la _direction_. Elle remplit l'espace laissé libre par les trois couches
  précédentes et n'en écrase aucune.

## Contradictions déclarées

Deux couches peuvent contredire la couche du dessous, à condition de le déclarer dans leur
frontmatter. Une contradiction non déclarée est une erreur : elle ne se tranche pas en silence, elle
se signale.

- Un fichier de **registre** déclare `surcharge: [<id de règle anti-slop>]` pour lever une règle du
  plancher anti-slop sur ce genre précis.
- Un fichier de **posture** déclare `suspend: [<id de trait de voix>]` pour éteindre une tendance
  par défaut de la voix le temps de cette posture.

Ne sont jamais levables : l'Étape 0, et les règles anti-slop listées en `non-surchargeable` dans le
frontmatter de `references/anti-slop.md`.

## Workflow

1. Lire le contexte, en extraire ce qu'il faut vérifier, exécuter l'**Étape 0**.
2. Déterminer le **Registre** et charger
   `${CLAUDE_PLUGIN_ROOT}/skills/write/references/registres/<id>.md`. Le contenu de ce répertoire
   est le seul inventaire qui fasse foi. Si aucun fichier ne couvre le medium demandé, ne pas
   improviser en silence : nommer le registre le plus proche, dire ce qui est emprunté et ce qui ne
   l'est pas, et tenir ces contraintes pour une hypothèse. Si le medium revient, proposer de créer
   le registre via `skill-learn` plutôt que de réimproviser.
3. Déterminer l'**Audience** en lisant `${CLAUDE_PLUGIN_ROOT}/skills/write/references/audience.md`.
   Relever K, P et D **tels qu'ils sont**, pas tels qu'on veut les jouer. Un axe que le contexte ne
   renseigne pas se laisse vide : la table de routage a une ligne par défaut, elle n'a pas besoin
   d'une valeur inventée.
4. Charger la **Posture** que la table de routage désigne, par son `id`, depuis
   `${CLAUDE_PLUGIN_ROOT}/skills/write/references/postures/<id>.md`. Un registre peut
   court-circuiter ce routage avec son champ `postures` et charger plusieurs postures, chacune sur
   son périmètre. Une posture qui n'apparaît ni dans la table ni dans un `postures` de registre est
   injoignable : ne jamais la charger à l'intuition.
5. Appliquer la **Voix** (`${CLAUDE_PLUGIN_ROOT}/skills/write/references/voix.md`), moins les traits
   que la posture active déclare en `suspend`. L'Empan se lit en **delta** sur la norme du registre
   actif, jamais comme une longueur absolue.
6. Appliquer le plancher **anti-slop**
   (`${CLAUDE_PLUGIN_ROOT}/skills/write/references/anti-slop.md`), moins les règles que le registre
   actif déclare en `surcharge`. Les règles non surchargeables s'appliquent dans tous les cas.
7. Si le contexte est ambigu sur l'un de ces axes, poser une question brève plutôt que deviner en
   silence, mais seulement si la réponse change le résultat. Le registre et l'audience valent
   souvent la question ; la voix jamais.
8. Avant de livrer, passer la checklist ci-dessous.

## Checklist avant livraison

- Aucune affirmation sous le seuil de l'Étape 0 n'est donnée pour acquise.
- Les faits internes non vérifiables sont listés dans le compte rendu, pour arbitrage de l'auteur.
- Le plancher anti-slop est passé, surcharges du registre actif comprises.
- Les contraintes dures du registre sont tenues : plan, longueur, conventions.
- L'empan effectif correspond au delta de voix appliqué à la norme du registre.
- Aucun trait de voix suspendu n'a été appliqué, aucun trait non suspendu n'a été abandonné en
  silence.
- Le texte parle de son sujet, pas de lui-même.

## Portée du plancher anti-slop

Le plancher porte sur **le texte produit**, pas sur les fichiers de ce skill. Les fichiers de
référence sont de la documentation machine : listes de déclarations, tableaux, identifiants. Ils
obéissent aux conventions du dépôt, pas aux règles de prose destinée à un lecteur.

## Limites connues

La voix décrite ici a été extraite d'un corpus fini, avec les angles morts que ça implique. Ils sont
écrits dans `${CLAUDE_PLUGIN_ROOT}/skills/write/corpus-index.md`. Les lire avant de tirer de ce
skill une conclusion sur ce que la personne « écrit toujours ».

## Amélioration continue

Ce skill n'a pas de logique d'apprentissage intégrée. Dès qu'une correction ou un décalage apparaît
pendant l'usage, la révision se journalise dans `changelog.md`, au format que ce fichier définit.

Si un skill générique d'amélioration continue est installé par ailleurs, il peut tenir ce journal à
votre place. Rien ici n'en dépend : aucun skill de ce marketplace n'est requis pour que celui-ci
fonctionne. La règle qui compte ne change pas dans un cas comme dans l'autre : **pas d'édition
silencieuse d'un fichier de référence**, une correction se propose et se valide avant d'être écrite.

Le journal des évolutions vit dans `changelog.md` et nulle part ailleurs. Ce fichier ne porte pas de
section « notes de version » : deux compteurs finissent toujours par diverger.
