# Corpus-index — gabarit

<!-- gabarit: trace de ce qui a servi à produire `references/voix.md`, `references/postures/` et
     `references/audience.md`. Aucun texte n'est utilisé sans sa ligne dans la table de
     qualification ci-dessous. Ce fichier n'est jamais chargé par le skill en cours de rédaction :
     il documente l'extraction, il ne sert pas à écrire. -->

## Table de qualification

<!-- gabarit: une ligne par item déposé. La colonne Registre ne prend qu'un `id` de la
     bibliothèque livrée (`email`, `message-court`, `post-social`, `article-vulgarisation`,
     `rapport`, `documentation-technique`, `papier-recherche`, `lettre-motivation`), jamais une valeur libre : c'est ce
     qui permet au comptage de calculer ses taux par registre et à l'Empan d'avoir une norme contre
     laquelle s'écrire en écart. Un genre absent de la bibliothèque s'écrit d'abord comme registre,
     selon `contrats-interface.md`, avant qu'un item puisse s'y ranger. Le type de destinataire
     s'exprime en asymétrie de connaissance, pouvoir et distance (K, P, D) et en niveau du lecteur
     (N), jamais en nom de personne : un corpus qui nomme des personnes fuit exactement ce que ce
     méta-skill est censé empêcher. N est noté parce que c'est lui, et non K, qui explique le
     niveau de contenu d'un texte : sans lui, deux items à K identique mais à lecteurs de niveaux
     opposés deviennent indistinguables à la relecture. -->

| Item        | Registre        | Destinataire (K / P / D) | Niveau (N) | Sujet     | Support     | Statut de révision  | Mots        | Date     |
| ----------- | --------------- | ------------------------ | ---------- | --------- | ----------- | ------------------- | ----------- | -------- |
| {{ID_ITEM}} | {{ID_REGISTRE}} | {{K}} / {{P}} / {{D}}    | {{N}}      | {{SUJET}} | {{SUPPORT}} | {{STATUT_REVISION}} | {{NB_MOTS}} | {{DATE}} |

Statuts de révision valides : brut, auto-révisé, révisé par un tiers, assisté par IA.

Sujet : le domaine du texte en quelques mots (technique, administratif, personnel…). Il sert à
l'étape 5 à séparer un mot de voix d'un mot de sujet : un lexème qui ne revient que sur un sujet est
un marqueur de sujet. Le comptage, lui, reste calculé par registre seulement.

Support `séance` : texte écrit ou marqué pendant l'entretien approfondi, jamais envoyé avant le
protocole. Il compte comme occurrence, plus faible qu'un texte de corpus, et sa provenance dans
`references/voix.md` s'écrit `séance`.

## Items écartés

<!-- gabarit: chaque item retiré de l'analyse, avec son motif exact. Un écart sur simple soupçon
     de contamination par un modèle ne s'écrit ici qu'après confirmation explicite de la
     personne ; sans confirmation, l'item reste dans la table de qualification et le soupçon ne
     l'écarte pas. -->

- **{{ID_ITEM_ECARTE}}** — motif : {{MOTIF_ECART}}. Confirmé par la personne : {{OUI_NON}}.

## Tableau de comptage

<!-- gabarit: sortie du script de comptage, recopiée ici comme trace de ce sur quoi le profil
     s'appuie. Un registre sous le seuil de mots apparaît avec la mention explicite de l'absence
     de taux, jamais en silence. Le comptage réfute ou corrobore, il ne propose jamais un trait :
     une ligne de ce tableau sans fonction identifiée à l'étape de lecture ou d'entretien reste
     une ligne de tableau, pas un trait de `references/voix.md`. -->

| Trait candidat | {{ID_REGISTRE_1}} | {{ID_REGISTRE_2}} | {{ID_REGISTRE_3}} | Variance inter-registre |
| -------------- | ----------------- | ----------------- | ----------------- | ----------------------- |
| {{TRAIT}}      | {{TAUX_1}}        | {{TAUX_2}}        | {{TAUX_3}}        | {{VARIANCE}}            |

Registres sous le seuil de mots, sans taux produit : {{LISTE_REGISTRES_SOUS_SEUIL}}.

## Étapes sautées et modes dégradés actifs

<!-- gabarit: une ligne par déclencheur de mode dégradé effectivement rencontré. Une étape sautée
     s'écrit ici, elle ne disparaît jamais en silence. -->

- {{ETAPE_OU_MODE}} : {{RAISON}}. Conséquence sur le livrable : {{CONSEQUENCE}}.

## Traits déclarés sans occurrence de corpus

Tout trait revendiqué en entretien mais introuvable dans les items ci-dessus va dans
`references/voix-aspirations.md`, jamais dans `references/voix.md`. Cette table ne les liste pas une
seconde fois ; elle sert seulement à documenter ce qui a été effectivement lu, pas ce qui en a été
tiré.
