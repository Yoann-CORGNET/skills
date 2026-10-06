---
id: "{{ID_POSTURE}}"
libelle: "{{LIBELLE_POSTURE}}"
declencheur: "{{RESUME_DECLENCHEUR_UNE_LIGNE}}"
corroboration: "{{CORPUS_SEANCE_OU_NON_CORROBOREE}}"
suspend: []
---

<!-- gabarit: ce fichier n'est pas une posture, c'est le modèle dont chaque fichier réel de
     `postures/<id réel>.md` dérive. Il n'est jamais chargé par le skill et jamais cité comme
     cible de routage. `corroboration` prend la valeur `corpus` si la posture a un ancrage dans
     le corpus déposé, `séance` si son seul ancrage est un texte écrit pendant l'entretien
     approfondi, `non-corroboree` si elle n'a été établie que par les écrans de choix forcé
     de l'étape de calibration. `suspend` liste des `id` de traits de voix, jamais des libellés ;
     laisser la liste vide est une réponse valide, pas une case oubliée. -->

# Posture — gabarit

## Déclencheur

<!-- gabarit: le déclencheur se formule en entrées d'audience (K, P, D) et en but, jamais en nom de
     personne ni en type de relation informel. Un déclencheur qui ne route sur aucun des trois axes
     doit router sur le but seul et le dire explicitement, comme la posture de discussion volontaire
     du catalogue du méta-skill. -->

{{DESCRIPTION_DU_DECLENCHEUR_EN_TERMES_K_P_D_BUT}}

## Coordonnées

<!-- gabarit: notation ordinale, pas métrique : `−` bas, `~` moyen, `+` haut, `−−` très bas pour les
     composantes 1, 2, 4, 5, 6 ; `K−`/`K=`/`K+` pour la composante 3 ; `pleine`/`partielle` pour la
     composante 7 ; `var.` quand la posture ne fixe pas la valeur, à condition de dire dans la
     colonne ce qui la fixe à la place. -->

| 1. Ouverture dialogique | 2. Intensité | 3. Droit à affirmer | 4. Franchise | 5. Proximité | 6. Adresse au lecteur | 7. Prise en charge |
| ----------------------- | ------------ | ------------------- | ------------ | ------------ | --------------------- | ------------------ |
| {{POS_1}}               | {{POS_2}}    | {{POS_3}}           | {{POS_4}}    | {{POS_5}}    | {{POS_6}}             | {{POS_7}}          |

{{JUSTIFICATION_DES_COORDONNEES_QUAND_NON_EVIDENTE}}

## Susceptible de suspendre

<!-- gabarit: une entrée par trait de voix effectivement suspendu par cette posture, nommée par sa
     direction sur un axe, jamais par une forme. « Une direction d'expansion dialogique sur la
     composante 1 » est correct ; nommer la forme qui la réalise ne l'est pas. Recopier chaque `id`
     retenu ici dans le champ `suspend` du frontmatter. -->

{{LISTE_DES_DIRECTIONS_DE_VOIX_SUSPENDUES_OU_EN_PRINCIPE_RIEN}}

## Triplets de calibration

<!-- gabarit: un triplet par composante parmi 1, 3 et 4, jamais un triplet par posture. Le
     triplet force une variante à éviter par excès, une variante à éviter par défaut, et la forme
     retenue ; la phrase de base reste verbatim dans les trois variantes, seul un habillage
     ajouté varie. Chaque variante porte une ligne de delta sur les sept composantes avec
     exactement un signe `≠` : un contraste qui s'écarte sur plusieurs composantes à la fois
     n'identifie aucune d'elles. Quand un pôle n'est atteignable par aucun habillage à axe
     unique, le triplet devient un couple (base plus une seule borne) et la borne manquante
     s'obtient par une élicitation séparée, jamais en présentant une variante contaminée comme si
     elle était propre. -->

### Composante 1, ouverture dialogique

- Base : {{PHRASE_DE_BASE_1}}
- Variante à éviter par excès : {{VARIANTE_EXCES_1}} Delta : `1 ≠` `2 =` `3 =` `4 =` `5 =` `6 =`
  `7 =`
- Variante à éviter par défaut : {{VARIANTE_DEFAUT_1}} Delta : `1 ≠` `2 =` `3 =` `4 =` `5 =` `6 =`
  `7 =`
- Forme retenue : {{FORME_RETENUE_1}}

### Composante 3, droit à affirmer

- Base : {{PHRASE_DE_BASE_3}}
- Variante à éviter par excès : {{VARIANTE_EXCES_3}} Delta : `1 =` `2 =` `3 ≠` `4 =` `5 =` `6 =`
  `7 =`
- Variante à éviter par défaut : {{VARIANTE_DEFAUT_3}} Delta : `1 =` `2 =` `3 ≠` `4 =` `5 =` `6 =`
  `7 =`
- Forme retenue : {{FORME_RETENUE_3}}

### Composante 4, franchise

- Base : {{PHRASE_DE_BASE_4}}
- Variante à éviter par excès : {{VARIANTE_EXCES_4}} Delta : `1 =` `2 =` `3 =` `4 ≠` `5 =` `6 =`
  `7 =`
- Variante à éviter par défaut : {{VARIANTE_DEFAUT_4}} Delta : `1 =` `2 =` `3 =` `4 ≠` `5 =` `6 =`
  `7 =`
- Forme retenue : {{FORME_RETENUE_4}}

## Ton du signalement de l'Étape 0 dans cette posture

<!-- gabarit: seul le ton varie ici. L'Étape 0 de vérification factuelle n'est jamais suspendue par
     une posture, quelle qu'elle soit, y compris une posture de performance ; ce que cette section
     calibre est la formulation du signalement, pas son existence. -->

{{FORMULATION_DU_SIGNALEMENT_DANS_CETTE_POSTURE}}
