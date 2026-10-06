---
name: write-forge
description:
  Construit pour une personne son propre skill de rédaction, en extrayant de ses écrits et d'un
  entretien les composantes personnelles de son écriture (voix, postures), y compris sans aucun
  texte existant grâce à un entretien approfondi optionnel, puis en générant un plugin autonome prêt
  à l'emploi, avec les registres et l'audience universels livrés complets. Invoquer quand quelqu'un
  demande « un skill qui écrit comme moi », veut extraire ou formaliser sa voix éditoriale, veut
  créer, initialiser ou générer un skill de rédaction personnel, ou veut adapter un skill de
  rédaction existant à une autre personne que son auteur. Pas pour rédiger un texte (c'est le rôle
  du skill produit), pas pour faire évoluer un skill déjà généré (voir `skill-learn`).
---

# write-forge : construire le skill de rédaction de quelqu'un

Ce skill produit un **plugin autonome**, nommé `write` par défaut ou du nom que la personne choisit,
contenant le skill de rédaction d'une personne : sa voix, ses postures calibrées, les registres
qu'elle retient, la table d'audience et le plancher de qualité universel.

Il fait deux choses qu'il ne faut pas confondre. Il **livre des artéfacts universels** déposables
tels quels chez n'importe qui, et il **extrait des artéfacts personnels** qui n'existent que pour
une personne. Tout le protocole consiste à séparer proprement les deux.

## Les quatre couches

Un texte se compose de quatre couches, dans un ordre de préséance strict :

**Registre > Audience > Posture > Voix**

| Couche       | Ce qu'elle apporte | Nature                                            |
| ------------ | ------------------ | ------------------------------------------------- |
| **Registre** | la **forme**       | contraintes dures de genre                        |
| **Audience** | les **entrées**    | K (connaissance), P (pouvoir), D (distance) réels |
| **Posture**  | la **dose**        | valeur jouée sur chaque composante                |
| **Voix**     | la **direction**   | noyau personnel, remplit l'espace laissé libre    |

L'Audience porte des **entrées de contexte réelles**, la Posture des **valeurs jouées**. La distance
sociale réelle est une entrée ; la proximité construite est une posture. Cette distinction tient
tout le découpage.

Le critère qui sépare la Voix du Registre vient de Biber & Conrad (2009) : sont de la Voix les
traits qui ne sont pas fonctionnellement motivés par le contexte situationnel.

Détail complet, avec la procédure de décision qui range un trait dans sa couche :
`references/modele-concepts.md`.

## Le protocole, en trois temps

1. **Cadrage et corpus.** Langue, registres où la personne écrit, volume, de « aucun texte » à «
   plus de 10 », et option d'entretien approfondi. Ces deux réponses fixent le parcours : standard,
   avec entretien, sans corpus, ou squelette. Le refus s'annonce ici si le volume est insuffisant,
   pas à la fin du travail.
2. **Extraction.** Lecture des mouvements de discours, comptage de réfutation, entretien par
   incident critique, validation par choix forcé aveugle, puis passage du catalogue de postures (en
   accept, décline ou report) et du catalogue de registres (en accept ou décline). L'entretien
   approfondi, s'il est retenu, fait écrire la personne en séance puis trancher à l'aveugle entre
   des variantes de ses propres phrases : c'est lui qui fournit le matériau quand le corpus manque.
3. **Génération et validation.** Passe de vérification des affirmations contre les sorties d'écran
   et de script, choix du nom du plugin (`write` par défaut), écriture du plugin, vérification que
   l'audience ne route que vers des postures retenues, puis passage du validateur.

Procédure détaillée, étape par étape, avec ce qui est demandé à la personne et le coût en temps :
`references/protocole-extraction.md`.

## Règles non négociables

1. **Le comptage réfute, il ne découvre pas.** La substance vient de la lecture des mouvements de
   discours et de l'entretien. Le script écarte des faux positifs de voix, il ne trouve personne.
2. **L'intentionnalité ne se tranche jamais sans la personne.** Un trait récurrent peut être un
   choix ou un tic de flemme. Les tests instrumentent la question, ils ne la closent pas : « tic »
   est une catégorie évaluative, pas une observation.
3. **Un seul axe varie par écran de choix forcé et par triplet de calibration.** Un contraste qui
   s'écarte sur trois composantes à la fois ne permet d'identifier aucune des trois.
4. **Les catalogues de postures et de registres se traversent en accept ou décline explicite sur
   chaque entrée.** Une posture peut aussi être reportée, explicitement, quand le matériau manque
   pour la calibrer. Jamais « choisis ceux qui te parlent » : c'est le passage forcé qui fait
   remonter les angles morts, par exemple un genre que la personne écrit sans y penser.
5. **Aucune formule d'invariance absolue** dans la voix générée. Un trait de voix est une tendance
   par défaut qu'une posture peut surcharger en le déclarant, jamais un invariant qui « persiste peu
   importe la posture ».
6. **L'Étape 0 de vérification factuelle n'est jamais suspendable**, y compris par une posture de
   performance. Une posture peut suspendre des traits de voix ; elle reste responsable du contenu
   propositionnel.
7. **Toute contradiction entre couches se déclare.** Une posture déclare les traits de voix qu'elle
   suspend, un registre déclare les règles anti-slop qu'il surcharge. Le validateur vérifie que
   chaque identifiant nommé existe. Une contradiction silencieuse est une erreur.
8. **Les références croisées se font par identifiant stable**, jamais par libellé humain. Renommer
   une posture ne doit rien casser.
9. **Rien ne se génère sans passer le validateur.** Un skill de rédaction maintenu à la main dérive
   vers des pointeurs morts et des postures injoignables ; une instance générée dérive plus vite.

## Ce que le protocole ne sait pas faire

À lire avant de faire confiance au résultat : `references/limites.md`. Le point le plus important y
est que la baseline de comparaison est une réécriture générée par le modèle, si bien que tout trait
partagé entre la personne et le modèle reste invisible.

## Carte des fichiers

| Fichier                              | Quand le lire                                      |
| ------------------------------------ | -------------------------------------------------- |
| `references/modele-concepts.md`      | pour ranger un trait dans sa couche                |
| `references/composantes-voix.md`     | pendant l'extraction de la voix                    |
| `references/composantes-posture.md`  | pendant la calibration des postures                |
| `references/catalogue-postures.md`   | au passage accept/décline du catalogue             |
| `references/protocole-extraction.md` | du début à la fin, c'est la procédure              |
| `references/protocole-entretien.md`  | si l'entretien approfondi est retenu à l'étape 0   |
| `references/contrats-interface.md`   | pour ajouter un registre absent de la bibliothèque |
| `references/limites.md`              | avant de livrer, et avant de croire au résultat    |
| `examples/instance/`                 | le gabarit du plugin généré, registres compris     |
| `scripts/compte-traits.py`           | filtre de réfutation sur le corpus                 |
| `scripts/valide-instance.py`         | avant de déclarer une instance terminée            |

## Portée de cette version

Les quatre couches sont livrées. **Voix** et **Posture** sont personnelles : le protocole les
extrait. **Registre** et **Audience** sont universelles, elles ne dépendent pas de la personne, et
elles arrivent complètes dans le gabarit d'instance, comme `anti-slop.md`. La bibliothèque compte
huit registres, d'`id` `email`, `message-court`, `post-social`, `article-vulgarisation`, `rapport`,
`documentation-technique`, `papier-recherche` et `lettre-motivation`. `audience.md` porte la table
de routage et les règles de niveau de contenu (scaffolding, jargon).

Une instance sortie du protocole est donc exécutable sans qu'on écrive un registre à la main. La
limite qui disait le contraire, et le code `STRUCT-02` qui la signalait, ne s'appliquent plus à une
instance qui garde au moins un registre de la bibliothèque. Le protocole fait passer le catalogue
des registres en accept ou décline explicite, comme celui des postures, et l'instance ne garde que
les registres acceptés. Il retire aussi de `audience.md` les lignes des postures déclinées.

Ce qui reste vrai : les registres sont livrés à une **profondeur mécanique**. Chacun fixe ses
caractéristiques situationnelles, ses contraintes de forme, sa norme d'empan et ses surcharges
déclarées. Aucun ne vient d'une recherche de genre approfondie, genre par genre, et la bibliothèque
ne prétend pas couvrir tous les genres. Pour un registre plus fin, ou pour un genre absent, on en
ajoute un en suivant `references/contrats-interface.md`. Voir aussi `references/limites.md`.

## Portée et langue

Le skill est écrit en français ; les instances qu'il produit sont **multilingues**. Le protocole est
paramétré par la langue du corpus. Les marqueurs comptables et les tics de remplissage dépendent de
la langue et se re-dérivent, ils ne se transposent pas tels quels.

## Amélioration continue

Ce skill n'embarque aucune logique d'auto-correction. Une instance générée qui dérape se corrige
avec `skill-learn`, et le changement se journalise dans le `changelog.md` de l'instance.
