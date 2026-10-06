# Registres : bibliothèque livrée

Ce dossier contient la bibliothèque universelle de registres du skill. Un registre fournit la
**forme** d'un genre d'écrit : c'est la couche qui prime sur toutes les autres (Registre >
Audience > Posture > Voix). Les genres ne dépendent pas de la personne, donc les fichiers se livrent
complets avec l'instance, comme `anti-slop.md`, au lieu d'être extraits d'un corpus.

## Fichiers livrés

| `id`                      | Genre couvert                                                  |
| ------------------------- | -------------------------------------------------------------- |
| `email`                   | correspondance adressée, asynchrone                            |
| `message-court`           | chat, messagerie instantanée, SMS : tour de parole bref        |
| `post-social`             | diffusion publique à audience non choisie                      |
| `article-vulgarisation`   | article de fond qui transfère une compréhension                |
| `rapport`                 | rendu de compte d'un travail à un lecteur qui évalue ou décide |
| `documentation-technique` | écrit de référence consulté par fragments                      |
| `papier-recherche`        | contribution nouvelle soumise à des pairs                      |
| `lettre-motivation`       | candidature adressée à quelqu'un qui recrute                   |

`SKILL.md` construit l'inventaire des registres depuis le contenu de ce dossier, jamais depuis une
liste saisie à la main ailleurs. Ajouter un genre, c'est ajouter un fichier ici.

## Structure d'un fichier

Frontmatter : `id`, `libelle`, `norme-empan`, `surcharge`, `postures`. Corps, dans cet ordre :
caractéristiques situationnelles, contraintes dures de forme, norme d'empan développée, surcharges
déclarées avec leur justification, noyau neutre, puis une section `## Français` et une section
`## English` pour ce qui dépend réellement de la langue.

## Ce que le contrat impose

- **`id`** : identifiant kebab-case stable. Les postures et la table de routage de
  `${CLAUDE_PLUGIN_ROOT}/skills/write/references/audience.md` s'y réfèrent par cet `id`, jamais par
  le nom de fichier ni par le libellé.
- **`norme-empan`, obligatoire.** Description de l'empan par défaut du genre : longueur typique,
  densité, tolérance à la digression. Sans elle, la composante Empan d'une voix reste
  ininscriptible, puisqu'elle s'encode toujours en écart relatif à cette norme.
- **`surcharge`** : liste d'`id` de règles de
  `${CLAUDE_PLUGIN_ROOT}/skills/write/references/anti-slop.md` que le genre lève. Une règle levée
  sans figurer ici est une contradiction non déclarée, donc une erreur. Une règle marquée
  `non-surchargeable` dans ce fichier n'y figure jamais.
- **`postures`** : vide dans la bibliothèque livrée. Imposer une posture par registre reproduirait
  un choix personnel, pas une convention de genre ; la posture se route par l'audience.
- **Contraintes dures de forme** dans le corps : un fichier réduit à son frontmatter n'a pas rempli
  son rôle.

## Ce qu'un registre ne contient pas

Test de tri : garder le lecteur fixe et changer le genre, si la règle change elle est du Registre ;
garder le genre fixe et changer le lecteur, si la règle change elle est de l'Audience.

- Aucun registre ne choisit entre adresse familière et déférente : c'est une entrée d'audience, et
  son défaut de langue vit dans `adresse-tv` de l'annexe de `anti-slop.md`. Un registre décrit les
  emplacements d'ouverture et de clôture et leur cérémonie possible, jamais le choix.
- Aucun registre ne fixe un niveau d'expertise du lecteur.
- Aucun registre ne nomme un trait de voix. Il peut dire qu'un genre est plus ou moins permissif à
  une famille de procédés, jamais citer un procédé : chez quelqu'un qui n'a pas ce trait, la ligne
  serait morte.

## Repli face à un genre non couvert

Un registre absent ne se comble jamais en empruntant silencieusement les contraintes d'un autre. La
conduite, posée dans `SKILL.md`, est de nommer le registre le plus proche, de dire ce qui en est
emprunté et ce qui ne l'est pas, et de traiter ces contraintes comme une hypothèse. Un genre qui
revient souvent vaut un fichier propre, écrit sur le modèle de ceux-ci.
