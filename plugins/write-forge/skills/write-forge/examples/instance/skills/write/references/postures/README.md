# Postures — convention de dossier

Un fichier par posture retenue à la génération, nommé `<id>.md` avec l'`id` kebab-case déclaré dans
son propre frontmatter. `SKILL.md` charge ces fichiers par leur `id`, jamais par leur nom de fichier
: renommer un fichier sans mettre à jour `id` casse la référence silencieusement.

## `gabarit.md`

N'est pas une posture, et n'est pas copié dans une instance générée : le validateur l'ignore. C'est
le modèle qui montre la forme attendue d'un fichier de posture : frontmatter (`id`, `declencheur`,
`corroboration`, `suspend`), position sur les sept composantes, triplets de calibration, ton du
signalement de l'Étape 0. Chaque fichier de posture réel s'en inspire puis le remplace, il ne le
complète pas. `gabarit.md` n'est jamais cité comme cible de routage dans
`${CLAUDE_PLUGIN_ROOT}/skills/write/references/audience.md` et jamais chargé par `SKILL.md`.

## Règle dure sur les triplets de calibration

Un triplet de calibration ne fait varier qu'une seule composante à la fois, parmi les trois où la
calibration porte, 1, 3 et 4. La phrase de base reste identique dans les trois variantes ; seul un
habillage ajouté varie, et cet habillage se vérifie contre les sept listes de marqueurs de posture
du méta-skill avant d'être retenu, pas seulement contre la composante qu'il est censé viser. Un
contraste qui s'écarte sur plusieurs composantes à la fois n'identifie aucune d'elles : le rejet ou
l'acceptation d'une telle variante ne dit pas laquelle des déviations a pesé.

Quand un pôle n'est atteignable par aucun habillage à axe unique, le triplet devient un couple, la
base plus la seule borne atteignable, et la borne manquante s'obtient par une élicitation séparée
dont le déplacement multi-axes est écrit explicitement plutôt que présenté comme une borne propre.

## Ce que `suspend` peut nommer, et ce qu'il ne nomme jamais

`suspend` liste des `id` de traits du fichier de voix de l'instance
(`${CLAUDE_PLUGIN_ROOT}/skills/write/references/voix.md`), jamais des libellés humains. Chaque `id`
cité doit désigner une direction sur un axe interpersonnel, jamais une forme qui la réalise : une
posture suspend « une direction d'expansion dialogique sur la composante 1 », jamais « le réflexe de
la question ». Un trait de voix qui nomme une forme est déjà mal placé dans ce fichier ; le déclarer
suspendu ici reconduirait l'erreur au lieu de la corriger.

La suspension est toujours à portée partielle. Aucune posture, y compris une posture de performance,
ne peut suspendre l'Étape 0 de vérification factuelle ni le statut de source des affirmations
qu'elle avance : seul le ton du signalement varie d'une posture à l'autre.

## Postures sans ancrage de corpus

Une posture peut être retenue sans qu'aucun texte du corpus ne l'illustre, du moment que ses trois
écrans de calibration reviennent cohérents. Son frontmatter porte alors
`corroboration: non-corroboree` plutôt que d'être présentée au même titre qu'une posture observée.
Une posture ancrée seulement sur un texte écrit pendant l'entretien approfondi porte
`corroboration: séance`. Une posture retenue sur des écrans incohérents, ou sur des écrans sautés,
ne se rédige pas : la décision va dans le journal des évolutions de l'instance, pas dans un fichier
de posture inventé pour combler une case vide du menu de départ.
