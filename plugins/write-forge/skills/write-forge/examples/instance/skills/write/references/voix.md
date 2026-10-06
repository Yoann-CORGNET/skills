# Voix — gabarit

<!-- gabarit: ce fichier est remplacé intégralement par le résultat de l'extraction. La structure en
     huit composantes, l'ordre, les règles d'encodage et les phrases de statut sont à conserver ; le
     contenu de chaque bloc placeholder ne l'est pas. Un générateur qui laisse une section sans
     traits doit écrire pourquoi (« non extrait, motif : … »), jamais omettre la section. -->

Ce fichier porte la direction par défaut de huit composantes. Chacune est une tendance par défaut
que la posture chargée peut surcharger en le déclarant dans son `suspend:` ; aucune ne s'écrit comme
valable sans égard à la posture active. Une posture qui prime sur un trait ci-dessous est le
fonctionnement attendu du dispositif, pas une anomalie à corriger.

Chaque trait retenu porte un `id` kebab-case stable dans une ancre `<!-- id: … -->`, sa provenance
et un statut. Provenances admises, de la plus forte à la plus faible : `corpus` (texte écrit et
envoyé avant le protocole), `séance` (texte écrit ou marqué pendant l'entretien approfondi, ou
réponse libre à un écran), `écran` (deux écrans de choix forcé aveugles convergents), `entretien`
(récits, réservé à la philosophie de fond et au Regard) ; une combinaison s'écrit avec `+`, par
exemple `séance + écran`. Statut : `constaté` ou `hypothèse` si le test qui le confirme n'a pas été
mené. Les fichiers de posture s'y réfèrent uniquement par cet `id`, jamais par le libellé du trait.

## 1. Substrat

Composante diagnostique, jamais générative. Elle sert à vérifier qu'un brouillon sonne juste par
comparaison au corpus ; elle n'écrit aucune consigne exécutable et ne reçoit donc aucun bloc à
remplir ici. Si un script de comptage existe pour cette instance, c'est lui qui la porte, pas ce
fichier.

## 2. Signature typographique <!-- id: signature-typographique -->

Générative, à encoder signe par signe, avec son statut d'endossement. Un signe n'entre ici que s'il
est resté idiolectal après le filtre de forme, c'est-à-dire sans fonction interpersonnelle. Un signe
qui règle le rapport au lecteur ou au désaccord (question, atténuateur, adresse) n'est pas de la
Voix : il descend en Posture pour sa dose, et remonte en Registre pour la forme que le genre
autorise.

<!-- gabarit: un trait par signe retenu. Dupliquer le bloc ci-dessous autant que nécessaire. -->

- **{{LIBELLE_TRAIT_TYPOGRAPHIQUE}}** <!-- id: {{ID_TRAIT_TYPOGRAPHIQUE}} --> {{DESCRIPTION_TRAIT}}.
  Statut : {{CONSTATE_OU_HYPOTHESE}}. Provenance : {{PROVENANCE}}.

## 3. Empan <!-- id: empan -->

Règle dure d'encodage : ce trait s'écrit **en delta relatif à la norme d'empan du registre actif**,
jamais en longueur absolue. Un nombre de mots ou de phrases écrit ici écraserait une contrainte de
registre depuis la couche la plus basse, ce que l'ordre de préséance interdit. Cela suppose que
chaque fichier de registre déclare sa propre norme d'empan ; sans cette déclaration, la composante
n'est pas inscriptible et reste vide avec ce motif.

<!-- gabarit: exprimer l'écart par rapport à la norme déclarée par le registre, jamais un chiffre
     absolu. Exemple de forme : « plus court que la norme du registre actif », jamais « N mots ».
     -->

- **{{LIBELLE_TRAIT_EMPAN}}** <!-- id: {{ID_TRAIT_EMPAN}} --> Delta :
  {{DELTA_PAR_RAPPORT_A_LA_NORME}}. Statut : {{CONSTATE_OU_HYPOTHESE}}. Provenance : {{PROVENANCE}}.

## 4. Lexique de prédilection <!-- id: lexique-de-predilection -->

<!-- gabarit: composante laissée vide dans l'extraction qui a servi de point de départ à ce
     méta-skill, faute de question dédiée. Le protocole d'extraction doit la viser activement : un
     questionnaire qui ne la cible pas nommément reproduit le même trou. Ne pas laisser ce bloc vide
     par défaut ; s'il reste vide, écrire le motif explicitement plutôt que de l'omettre. -->

Le mot ou la cooccurrence compte, jamais sa densité : le nombre d'évaluations affichées par millier
de mots est une dose de Posture, pas un trait de Voix. Retirer le vocabulaire de sujet avant toute
conclusion ; un mot qui ne survit pas au changement de sujet est un marqueur thématique, pas un
trait de personne.

- **Domaine-source des images** <!-- id: domaine-source-images --> {{DOMAINE_SOURCE_METAPHORES}}.
  Statut : {{CONSTATE_OU_HYPOTHESE}}. Provenance : {{PROVENANCE}}.
- **Préférences et interdits lexicaux** <!-- id: preferences-lexicales -->
  {{PREFERENCES_ET_INTERDITS}}. Statut : {{CONSTATE_OU_HYPOTHESE}}. Provenance : {{PROVENANCE}}.

## 5. Geste rhétorique <!-- id: geste-rhetorique -->

« Geste rhétorique » est une étiquette forgée pour ce méta-skill, pas un terme établi dans la
littérature consultée : ne pas la présenter comme un concept reçu dans une instance générée. C'est
la composante la plus générative des huit : un geste s'écrit directement comme une consigne
exécutable, local et répétable à l'intérieur d'un même texte, distinct de l'Architecture qui ne se
joue qu'une fois par texte.

<!-- gabarit: un geste par mouvement retenu, formulé sans nommer de forme interpersonnelle. Si un
     geste candidat nomme une forme des listes de marqueurs de posture (question, hedge,
     humour…), il est mal placé ici : le scinder plutôt que le garder tel quel. -->

- **{{LIBELLE_GESTE}}** <!-- id: {{ID_GESTE}} --> {{DESCRIPTION_GESTE}}. Statut :
  {{CONSTATE_OU_HYPOTHESE}}. Provenance : {{PROVENANCE}}.

## 6. Architecture du propos <!-- id: architecture-du-propos -->

<!-- gabarit: seconde composante laissée vide dans l'extraction de départ. À viser activement :
     place du bémol, forme de la clôture, ordre thèse/exemple, quand le genre laisse le choix. Sans
     texte long dans le corpus, déclarer la composante non extractible plutôt que l'omettre. -->

Ne s'encode que ce qui reste quand le genre a déjà imposé sa structure obligatoire : l'ordre choisi
**là où deux ordres étaient également acceptables**. Une règle conditionnelle, de la forme « si le
genre laisse le choix, alors … ».

- **{{LIBELLE_TRAIT_ARCHITECTURE}}** <!-- id: {{ID_TRAIT_ARCHITECTURE}} --> {{DESCRIPTION_TRAIT}}.
  Statut : {{CONSTATE_OU_HYPOTHESE}} ; ou : non extrait, motif : aucun texte long dans le corpus.
  Provenance : {{PROVENANCE}}.

## 7. Réflexe interpersonnel <!-- id: reflexe-interpersonnel -->

Règle la plus stricte du fichier : cette composante ne porte **jamais** ni une forme ni une
quantité, seulement une direction sur un axe de posture, et rien de plus. Ce qu'elle écrit ressemble
à « devant un désaccord, le premier mouvement penche vers l'expansion plutôt que la contraction ».
Ce qu'elle n'écrit jamais : le nom d'une forme qui réalise cet axe (question, atténuateur,
tutoiement, auto-mention) ni un volume. La composante de posture correspondante porte le combien,
pour quelle relation ; le registre porte le moyen.

<!-- gabarit: une direction par axe où une préférence a été constatée. Ne pas remplir un axe sans
     matériau : une direction non observée reste absente plutôt qu'inventée. -->

- **{{LIBELLE_DIRECTION}}** <!-- id: {{ID_DIRECTION}} --> Direction :
  {{DIRECTION_SANS_NOMMER_DE_FORME}}. Axe de posture concerné : {{AXE_DE_POSTURE_CORRESPONDANT}}.
  Statut : {{CONSTATE_OU_HYPOTHESE}}. Provenance : {{PROVENANCE}}.

## 8. Regard

**Statut : composante optionnelle.** Elle ne s'observe pas sur texte court et ne se renseigne que si
le corpus contient des textes longs. En l'absence de corpus long, elle reste vide avec ce motif
plutôt que d'être devinée. Quand elle est renseignée, elle se traite comme critère de relecture
plutôt que comme consigne de rédaction : elle se dégrade vite en slogan si on la force en règle.

<!-- gabarit: ne remplir que si le corpus contient des textes longs ; sinon écrire le motif
     ci-dessous et laisser le reste de la section absent. -->

- **{{LIBELLE_TRAIT_REGARD}}** {{DESCRIPTION_TRAIT}}. Statut : {{CONSTATE_OU_HYPOTHESE}} ; ou : non
  extrait, motif : aucun texte long dans le corpus. Provenance : {{PROVENANCE}}.

## Traits restreints à un registre

<!-- gabarit: un trait qui n'a été observé que sur un seul registre n'a pas passé le test de
     variation de registre, mais il peut valoir la peine d'être consigné pour ce registre précis
     plutôt que jeté. Une ligne par trait, avec l'identifiant du registre concerné, référencé via
     `${CLAUDE_PLUGIN_ROOT}/skills/write/references/registres/<id>.md`. -->

- **{{LIBELLE_TRAIT_RESTREINT}}** — observé uniquement dans le registre
  `${CLAUDE_PLUGIN_ROOT}/skills/write/references/registres/{{ID_REGISTRE}}.md`. Statut :
  {{CONSTATE_OU_HYPOTHESE}}.

## Traits observés, non endossés

<!-- gabarit: un trait présent sur plusieurs registres mais que la personne désavoue lors de l'écran
     aveugle ou du test de survie à l'auto-révision. Il ne descend pas de ce fichier en silence : il
     est consigné ici avec le registre où il reste toléré, pour qu'une révision ultérieure puisse le
     rouvrir plutôt que de le redécouvrir. -->

- **{{LIBELLE_TRAIT_NON_ENDOSSE}}** — motif du non-endossement : {{MOTIF_NON_ENDOSSEMENT}}. Reste
  toléré dans le registre
  `${CLAUDE_PLUGIN_ROOT}/skills/write/references/registres/{{ID_REGISTRE_TOLERANT}}.md`.

## Marqueurs de surface, annexe de langue ({{LANGUE}})

Les composantes ci-dessus s'écrivent au niveau du discours pour porter d'une langue à l'autre. Les
marqueurs de surface qui les illustrent (formes exactes, tics de ponctuation propres à une langue)
ne se transposent pas et vivent dans cette annexe, propre à la langue {{LANGUE}} et à re-dériver
pour toute autre langue de travail.

{{MARQUEURS_DE_SURFACE_PAR_LANGUE}}
