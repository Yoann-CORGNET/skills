#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""valide-instance.py — validateur de génération pour une instance de `write-forge`.

Pourquoi ce script existe
-------------------------
Le skill de rédaction qui a servi de cas d'étude, pourtant maintenu à la main par son auteur,
contient 8 pointeurs
morts vers 2 fichiers inexistants, une posture qu'aucune ligne de routage ne peut charger, et 2
chemins relatifs qui ne résolvent pas. Une instance générée dérive plus vite qu'un skill écrit à la
main. Rien ne se livre sans passer ce validateur.

Ce que le script fait
---------------------
Il lit une instance (plugin autonome `<nom>/`, `write/` par défaut, ou directement le répertoire d'un skill
contenant `SKILL.md`) et rend un rapport séparant les **erreurs** (code de retour 1) des
**avertissements** (code de retour 0). `--explique` imprime le catalogue exact des contrôles, et
surtout la liste de ce qui n'est **pas** couvert.

Conventions d'identifiants attendues
------------------------------------
Le contrat de `write-forge` impose des identifiants stables et des contradictions déclarées. Le
validateur reconnaît ces formes :

1. Entité-fichier (posture, registre) — frontmatter YAML :

       ---
       id: rapport-technique
       libelle: Rapport technique
       surcharge: [formatage-listes]     # ids de règles anti-slop surchargées
       charge: [etudiant, expert]        # override de posture : rend ces postures atteignables
       ---

   Pour une posture : `suspend: [<id de trait de voix>, ...]`.

2. Entité-bloc (trait de voix dans `voix.md`, règle anti-slop dans `anti-slop.md`) — ancre
   invisible sur la ligne du titre ou de la puce, ou sur la ligne juste avant :

       - **Métaphore puis analyse** <!-- id: metaphore-analyse -->

   La forme `{#metaphore-analyse}` est acceptée en équivalent.

3. Référence croisée en prose — code inline namespacé :

       `posture:pair`  `registre:email`  `voix:metaphore-analyse`  `anti-slop:formatage-listes`

Mode hérité
-----------
Une instance sans aucun identifiant déclaré (cas d'un skill écrit avant cette convention) bascule
en **mode
hérité** : une seule erreur signale l'absence d'identifiants, et les contrôles par id se dégradent
en heuristiques de libellé, clairement étiquetées comme telles dans le rapport.

Python 3 standard library uniquement.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

VERSION = "1.0"

ERREUR = "ERREUR"
AVERT = "AVERT"

# ---------------------------------------------------------------------------
# Catalogue des contrôles. Sert au rapport ET à `--explique` : un seul point de
# vérité, pour qu'on ne puisse pas documenter un contrôle qui n'existe pas.
# ---------------------------------------------------------------------------

CATALOGUE = [
    ("STRUCT-01", ERREUR, "Fichier obligatoire manquant (SKILL.md, voix, anti-slop, audience)."),
    ("STRUCT-02", ERREUR, "Aucun fichier de posture, ou aucun fichier de registre."),
    ("STRUCT-03", AVERT, "Manifeste de plugin absent ou illisible (mode plugin)."),
    ("STRUCT-04", AVERT, "Agent `fact-checker` absent du plugin : l'Étape 0 est morte."),
    ("STRUCT-05", AVERT, "`voix-aspirations.md` est chargé quelque part alors qu'il ne doit "
                         "jamais l'être."),
    ("ID-00", ERREUR, "Aucun identifiant stable dans l'instance : mode hérité, contrôles "
                      "par id dégradés."),
    ("ID-01", ERREUR, "Fichier de posture ou de registre sans `id:` alors que d'autres en ont un."),
    ("ID-02", ERREUR, "Deux entités partagent le même identifiant."),
    ("REF-01", ERREUR, "Fichier cité qui n'existe nulle part dans l'instance."),
    ("REF-02", ERREUR, "Chemin relatif faux : la cible existe, mais pas là où le chemin pointe."),
    ("REF-03", AVERT, "Nom de fichier nu qui ne résout pas depuis le répertoire du fichier citant."),
    ("REF-04", ERREUR, "Référence `<genre>:<id>` vers un identifiant qui n'est défini nulle part."),
    ("REF-05", AVERT, "Nom de posture cité en prose sans fichier correspondant (heuristique)."),
    ("REF-06", AVERT, "Nom de registre cité en prose sans fichier correspondant (heuristique)."),
    ("INV-01", ERREUR, "Registre annoncé dans la description ou le workflow sans fichier."),
    ("INV-02", AVERT, "Registre qui a un fichier mais n'apparaît dans aucun inventaire."),
    ("INV-03", AVERT, "Repli « autre » annoncé sans fichier de registre par défaut ni règle."),
    ("ATT-01", ERREUR, "Posture définie mais injoignable : ni routage, ni override de registre."),
    ("ATT-02", ERREUR, "Cible de routage qui ne correspond à aucune posture."),
    ("SUS-01", ERREUR, "`suspend:` nomme un trait de voix qui n'existe pas."),
    ("SUS-02", ERREUR, "`surcharge:` nomme une règle anti-slop qui n'existe pas."),
    ("SUS-03", ERREUR, "Suspension de l'Étape 0 / du fact-check. Jamais suspendable."),
    ("SUS-04", AVERT, "Contradiction probable avec une règle anti-slop, non déclarée en "
                      "`surcharge:` (heuristique)."),
    ("VOIX-01", ERREUR, "Formule d'invariance absolue dans `voix.md` (« peu importe la posture »)."),
    ("VOIX-02", AVERT, "Vocabulaire d'invariance absolue hors de la formule canonique."),
    ("PERM-01", AVERT, "Marqueur de voix nommé dans un fichier de registre (heuristique)."),
    ("GAB-01", ERREUR, "Marqueur de gabarit non rempli ({{…}}, <…>, TODO, À REMPLIR)."),
    ("POST-01", AVERT, "Posture sans phrase de déclenchement."),
    ("POST-02", AVERT, "Posture sans section de ton du fact-check."),
    ("PERS-01", AVERT, "Nom propre ou marque probable dans un fichier réputé universel "
                       "(heuristique)."),
    ("PERS-02", AVERT, "Nom de la personne présent dans un fichier réputé universel."),
    ("VERS-01", AVERT, "Versions incohérentes entre SKILL.md et changelog.md."),
]

NON_COUVERT = """Ce que ce validateur ne vérifie PAS
-----------------------------------
- La qualité de l'extraction. Un `voix.md` bien formé mais faux passe sans un mot.
- Qu'un trait rangé dans la Voix y soit à sa place. Le test de couche exige de relire les postures
  et les registres, ce n'est pas mécanisable ici.
- Que les contraintes de registre soient réellement des contraintes de genre et non des habitudes
  de la personne (un axe qui mélange deux dimensions).
- Le vocabulaire métier en minuscules (« bilan comptable », « garde à vue », « taux de churn »). L'heuristique
  PERS-01 ne voit que les majuscules ; les fuites de domaine en bas de casse lui échappent.
- La cohérence de l'annexe de langue : qu'un anti-slop français ne serve pas à une instance
  anglophone.
- La dérive d'interface entre producteur et consommateur (le score de confiance du `fact-checker`
  n'est consommé par personne, ce que la lecture des fichiers ne montre pas).
- La duplication de règles entre couches sans contradiction (par exemple une consigne de concision
  répétée dans trois fichiers). Seules les contradictions de polarité sont heuristiquement détectées.
- Que l'anti-slop s'applique aux textes produits et pas aux fichiers du skill. C'est une décision
  de rédaction, pas un fait vérifiable.
- La couverture des situations par la table de routage. ATT-01 vérifie que chaque posture est
  atteignable, pas que chaque combinaison de K, P, D et but tombe sur une ligne : après le retrait
  d'une posture déclinée, son but n'est plus routé, et seule la ligne par défaut le rattrape. Les
  cellules en prose (« indifférent », « égalité ou … ») ne se prêtent pas à un contrôle fiable.
- Que chaque affirmation de `voix.md` et de `corpus-index.md` renvoie à une sortie d'écran ou du
  script de comptage. C'est la passe de vérification de l'étape 12, faite par l'agent.
- L'orthographe, le style, le respect du repli à 100 caractères. Prettier s'en charge."""


# ---------------------------------------------------------------------------
# Constats
# ---------------------------------------------------------------------------


class Constat:
    __slots__ = ("niveau", "code", "chemin", "ligne", "message", "indice")

    def __init__(self, niveau, code, message, chemin=None, ligne=None, indice=None):
        self.niveau = niveau
        self.code = code
        self.message = message
        self.chemin = chemin
        self.ligne = ligne
        self.indice = indice

    def cle_tri(self):
        return (0 if self.niveau == ERREUR else 1, str(self.chemin or ""), self.ligne or 0,
                self.code)

    def en_dict(self):
        return {
            "niveau": self.niveau,
            "code": self.code,
            "chemin": str(self.chemin) if self.chemin else None,
            "ligne": self.ligne,
            "message": self.message,
            "indice": self.indice,
        }


# ---------------------------------------------------------------------------
# Utilitaires texte
# ---------------------------------------------------------------------------

_EMPHASE = re.compile(r"\*\*|__|(?<!\w)_(?=\S)|(?<=\S)_(?!\w)|\*(?!\*)")


def sans_accents(txt):
    return "".join(c for c in unicodedata.normalize("NFD", txt)
                   if unicodedata.category(c) != "Mn")


def normalise(txt):
    """Minuscules, sans accents, espaces compactés. Base de toute comparaison de libellé."""
    txt = sans_accents(txt).lower()
    txt = re.sub(r"[^a-z0-9]+", " ", txt)
    return txt.strip()


def kebab(txt):
    return re.sub(r"\s+", "-", normalise(txt))


def sans_emphase(ligne):
    return _EMPHASE.sub("", ligne)


def lire(chemin):
    try:
        return chemin.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return []


def lire_frontmatter(lignes):
    """Sous-ensemble YAML suffisant : scalaires, listes en flux, listes en bloc, scalaires pliés.

    Renvoie (dict, index de la première ligne de corps).
    """
    if not lignes or lignes[0].strip() != "---":
        return {}, 0
    fin = None
    for i in range(1, len(lignes)):
        if lignes[i].strip() == "---":
            fin = i
            break
    if fin is None:
        return {}, 0

    donnees = {}
    cle = None
    tampon = []
    liste = None

    def cloture():
        if cle is None:
            return
        if liste is not None:
            donnees[cle] = liste
        else:
            valeur = " ".join(x.strip() for x in tampon).strip()
            if len(valeur) >= 2 and valeur[0] == valeur[-1] and valeur[0] in "'\"":
                valeur = valeur[1:-1].strip()
            donnees[cle] = valeur

    for brut in lignes[1:fin]:
        if not brut.strip():
            continue
        entete = re.match(r"^([A-Za-z_][\w.-]*)\s*:\s*(.*)$", brut)
        puce = re.match(r"^\s*-\s+(.*)$", brut)
        if entete and not brut.startswith((" ", "\t")):
            cloture()
            cle = entete.group(1)
            reste = entete.group(2).strip()
            liste = None
            tampon = []
            if reste.startswith("[") and reste.endswith("]"):
                liste = [x.strip().strip("'\"") for x in reste[1:-1].split(",") if x.strip()]
            elif reste:
                tampon = [reste]
            else:
                liste = []
        elif puce and cle is not None and liste is not None:
            liste.append(puce.group(1).strip().strip("'\""))
        elif cle is not None:
            if liste is not None and not liste:
                liste = None
                tampon = [brut.strip()]
            elif liste is None:
                tampon.append(brut.strip())
    cloture()
    return donnees, fin + 1


def lister(valeur):
    if valeur is None:
        return []
    if isinstance(valeur, list):
        return [v for v in valeur if v]
    valeur = str(valeur).strip()
    if not valeur:
        return []
    if valeur.startswith("[") and valeur.endswith("]"):
        return [x.strip().strip("'\"") for x in valeur[1:-1].split(",") if x.strip()]
    return [x.strip() for x in valeur.split(",") if x.strip()]


# Un bloc qui commence par un identifiant en code inline, suivi d'un deux-points ou d'un tiret,
# porte son `id` par cette forme. C'est la convention du fichier anti-slop livre.
RE_ID_INLINE = re.compile(r"^`([a-z0-9][a-z0-9-]*)`\s*[:\u2014-]\s")
RE_ANCRE = re.compile(r"<!--\s*id\s*:\s*([a-z0-9][a-z0-9-]*)\s*-->|\{#([a-z0-9][a-z0-9-]*)\}")
RE_REF_ID = re.compile(r"`(posture|registre|voix|anti-slop)\s*:\s*([a-z0-9][a-z0-9-]*)`")
RE_CODE = re.compile(r"`([^`]+)`")
RE_COMMENTAIRE = re.compile(r"<!--.*?-->", re.S)
RE_AUTOLIEN = re.compile(r"<[a-zA-Z][\w+.-]*:[^>\s]*>")
RE_LIEN_MD = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
RE_CHEMIN = re.compile(r"(?<![\w/`.-])((?:[\w.-]+/)*[\w.-]+\.(?:md|py|json|txt))(?![\w-])")
RE_MAJ = r"[A-ZÀ-ÖØ-Þ]"


# ---------------------------------------------------------------------------
# Modèle d'instance
# ---------------------------------------------------------------------------


class Fichier:
    def __init__(self, chemin, racine):
        self.chemin = chemin
        self.rel = chemin.relative_to(racine)
        self.lignes = lire(chemin)
        self.fm, self.debut = lire_frontmatter(self.lignes)

    def corps(self):
        return self.lignes[self.debut:]

    def enumerer(self, depuis_corps=True):
        """Itère (numéro de ligne 1-based, texte)."""
        debut = self.debut if depuis_corps else 0
        for i in range(debut, len(self.lignes)):
            yield i + 1, self.lignes[i]

    def titre(self):
        for _, ligne in self.enumerer():
            m = re.match(r"^#\s+(.*)$", ligne.strip())
            if m:
                return sans_emphase(m.group(1)).strip()
        return ""

    def texte(self):
        return "\n".join(self.corps())


class Entite:
    def __init__(self, genre, fichier):
        self.genre = genre
        self.fichier = fichier
        self.id_declare = (fichier.fm.get("id") or "").strip() or None
        self.ident = self.id_declare or kebab(fichier.chemin.stem)
        self.libelle = (fichier.fm.get("libelle") or fichier.fm.get("label")
                        or fichier.titre() or fichier.chemin.stem)

    def alias(self):
        """Tokens par lesquels cette entité peut être nommée en prose."""
        vus = set()
        brut = [self.ident, kebab(self.fichier.chemin.stem)]
        libelle = re.sub(r"^(Posture|Registre)\s*[—\-–:]\s*", "", self.libelle).strip()
        brut.append(kebab(libelle))
        for morceau in re.split(r"[/,+()]", libelle):
            morceau = morceau.strip()
            if len(morceau) >= 4:
                brut.append(kebab(morceau))
        for a in brut:
            a = a.strip("-")
            if len(a) >= 3 and a not in vus:
                vus.add(a)
        return vus


class Instance:
    def __init__(self, racine):
        self.racine_arg = racine
        self.plugin = None
        self.skill = None
        self.fichiers = {}
        self.postures = []
        self.registres = []
        self.traits_voix = {}      # id -> (chemin, ligne, texte)
        self.regles_slop = {}      # id -> (chemin, ligne, texte)
        self.ids_declares = set()

    # -- localisation ------------------------------------------------------

    def localiser(self, constats):
        racine = self.racine_arg
        if (racine / "SKILL.md").is_file():
            self.skill = racine
            parent = racine.parent
            if parent.name == "skills" and (parent.parent / ".claude-plugin").is_dir():
                self.plugin = parent.parent
            return True
        candidats = sorted(racine.glob("skills/*/SKILL.md")) or sorted(
            racine.glob("*/skills/*/SKILL.md"))
        prefere = [c for c in candidats if (c.parent / "references" / "voix.md").is_file()]
        retenus = prefere or candidats
        if not retenus:
            constats.append(Constat(
                ERREUR, "STRUCT-01",
                "Aucun SKILL.md trouvé sous ce chemin : ce n'est ni un skill, ni un plugin "
                "d'instance.", chemin=racine))
            return False
        self.skill = retenus[0].parent
        self.plugin = racine
        if len(retenus) > 1:
            constats.append(Constat(
                AVERT, "STRUCT-01",
                "Plusieurs skills trouvés, validation de %s uniquement." % retenus[0].parent.name,
                chemin=racine))
        return True

    # -- chargement --------------------------------------------------------

    def charger(self, constats):
        base = self.skill
        obligatoires = {
            "SKILL.md": base / "SKILL.md",
            "voix": base / "references" / "voix.md",
            "anti-slop": base / "references" / "anti-slop.md",
            "audience": base / "references" / "audience.md",
        }
        for nom, chemin in obligatoires.items():
            if chemin.is_file():
                self.fichiers[nom] = Fichier(chemin, base)
            else:
                constats.append(Constat(
                    ERREUR, "STRUCT-01",
                    "Fichier obligatoire absent : %s" % chemin.relative_to(base),
                    chemin=chemin))

        for chemin in sorted((base / "references" / "postures").glob("*.md")):
            # gabarit.md est le modèle de fiche livré avec le gabarit d'instance, pas une posture.
            if chemin.name.lower() in ("readme.md", "gabarit.md"):
                continue
            self.postures.append(Entite("posture", Fichier(chemin, base)))
        for chemin in sorted((base / "references" / "registres").glob("*.md")):
            if chemin.name.lower() == "readme.md":
                continue
            self.registres.append(Entite("registre", Fichier(chemin, base)))

        if not self.postures:
            constats.append(Constat(ERREUR, "STRUCT-02",
                                    "Aucun fichier de posture dans references/postures/.",
                                    chemin=base))
        if not self.registres:
            constats.append(Constat(ERREUR, "STRUCT-02",
                                    "Aucun fichier de registre dans references/registres/.",
                                    chemin=base))

        self._charger_blocs("voix", self.traits_voix)
        self._charger_blocs("anti-slop", self.regles_slop)

        for e in self.postures + self.registres:
            if e.id_declare:
                self.ids_declares.add(e.id_declare)

    def _charger_blocs(self, cle, cible):
        """Traits de voix / règles anti-slop. Ancre explicite si présente, sinon repli hérité."""
        fichier = self.fichiers.get(cle)
        if fichier is None:
            return
        section = ""
        attente = None
        for num, ligne in fichier.enumerer():
            mtitre = re.match(r"^(#{2,})\s+(.*)$", ligne)
            if mtitre:
                section = sans_emphase(mtitre.group(2)).strip()
            ancre = RE_ANCRE.search(ligne)
            ident = None
            if ancre:
                ident = ancre.group(1) or ancre.group(2)
                self.ids_declares.add(ident)
            nu = RE_COMMENTAIRE.sub("", ligne)
            nu = re.sub(r"\{#[a-z0-9-]*\}", "", nu).strip()
            est_bloc = bool(re.match(r"^(?:[-*]\s+|\d+\.\s+|#{2,}\s+)", nu))
            if ident and not nu:
                attente = ident
                continue
            if not est_bloc:
                continue
            if ident is None and attente is not None:
                ident = attente
            attente = None
            texte = sans_emphase(re.sub(r"^(?:[-*]\s+|\d+\.\s+|#{2,}\s+)", "", nu)).strip()
            if ident is None:
                mcode = RE_ID_INLINE.match(texte)
                if mcode:
                    ident = mcode.group(1)
                    self.ids_declares.add(ident)
            if ident is None:
                titre = re.match(r"^([^:.]{3,60}?)\s*[:.]", texte)
                base = titre.group(1) if titre else texte[:48]
                ident = "%s--%s" % (kebab(section) or cle, kebab(base))
                declare = False
            else:
                declare = True
            if ident and ident not in cible:
                cible[ident] = {
                    "chemin": fichier.chemin, "ligne": num, "texte": texte,
                    "section": section, "declare": declare,
                }

    def mode_herite(self):
        return not self.ids_declares

    def tous_fichiers(self):
        vus = []
        for f in self.fichiers.values():
            vus.append(f)
        for e in self.postures + self.registres:
            vus.append(e.fichier)
        return vus


# ---------------------------------------------------------------------------
# Contrôles
# ---------------------------------------------------------------------------

ANCRES_RACINE = {"skill.md", "changelog.md", "corpus-index.md", "readme.md"}


def controle_identifiants(inst, constats):
    if inst.mode_herite():
        constats.append(Constat(
            ERREUR, "ID-00",
            "Aucun identifiant stable déclaré dans l'instance. Les références croisées se font "
            "donc par libellé humain : renommer une posture casse silencieusement des registres. "
            "Mode hérité activé, les contrôles par id sont dégradés en heuristiques de libellé.",
            chemin=inst.skill))
        return
    vus = {}
    for e in inst.postures + inst.registres:
        if not e.id_declare:
            constats.append(Constat(
                ERREUR, "ID-01",
                "Fichier de %s sans `id:` en frontmatter alors que l'instance en déclare "
                "ailleurs." % e.genre, chemin=e.fichier.chemin, ligne=1))
            continue
        if e.id_declare in vus:
            constats.append(Constat(
                ERREUR, "ID-02",
                "Identifiant `%s` déjà porté par %s." % (e.id_declare, vus[e.id_declare]),
                chemin=e.fichier.chemin, ligne=1))
        else:
            vus[e.id_declare] = str(e.fichier.rel)


def _candidats_chemins(fichier):
    """Chemins cités dans un fichier, hors gabarits, autoliens et blocs de code."""
    dans_bloc = False
    for num, ligne in fichier.enumerer():
        if ligne.lstrip().startswith("```"):
            dans_bloc = not dans_bloc
            continue
        if dans_bloc:
            continue
        nu = RE_COMMENTAIRE.sub(" ", ligne)
        nu = RE_AUTOLIEN.sub(" ", nu)
        vus = set()
        for cible in RE_LIEN_MD.findall(nu):
            vus.add(cible)
        for morceau in RE_CODE.findall(nu):
            vus.update(RE_CHEMIN.findall(morceau))
        vus.update(RE_CHEMIN.findall(RE_CODE.sub(" ", nu)))
        for cible in vus:
            cible = cible.split("#")[0].strip()
            if not cible or any(c in cible for c in "<>*{}|$"):
                continue
            if cible.startswith(("http:", "https:", "mailto:")):
                continue
            yield num, cible


def controle_chemins(inst, constats):
    base = inst.skill
    index = {}
    for chemin in base.rglob("*"):
        if chemin.is_file():
            index.setdefault(chemin.name, []).append(chemin)
    for fichier in inst.tous_fichiers():
        for num, cible in _candidats_chemins(fichier):
            resolu = (fichier.chemin.parent / cible).resolve()
            if resolu.is_file():
                continue
            ailleurs = index.get(Path(cible).name, [])
            if not ailleurs:
                constats.append(Constat(
                    ERREUR, "REF-01",
                    "Fichier cité qui n'existe nulle part dans l'instance : `%s`." % cible,
                    chemin=fichier.chemin, ligne=num))
                continue
            attendu = ailleurs[0]
            if "/" in cible:
                try:
                    correct = Path(
                        __import__("os").path.relpath(attendu, fichier.chemin.parent)).as_posix()
                except ValueError:
                    correct = str(attendu)
                constats.append(Constat(
                    ERREUR, "REF-02",
                    "Chemin relatif faux : `%s` ne résout pas depuis %s." % (
                        cible, fichier.chemin.parent.relative_to(base)),
                    chemin=fichier.chemin, ligne=num,
                    indice="chemin correct : `%s`" % correct))
            elif cible.lower() in ANCRES_RACINE:
                continue
            else:
                constats.append(Constat(
                    AVERT, "REF-03",
                    "Nom de fichier nu `%s` : ne résout pas depuis ce répertoire, existe à %s."
                    % (cible, attendu.relative_to(base)),
                    chemin=fichier.chemin, ligne=num))


def controle_references_id(inst, constats):
    connus = {
        "posture": {e.ident for e in inst.postures},
        "registre": {e.ident for e in inst.registres},
        "voix": set(inst.traits_voix),
        "anti-slop": set(inst.regles_slop),
    }
    for fichier in inst.tous_fichiers():
        for num, ligne in fichier.enumerer(depuis_corps=False):
            for genre, ident in RE_REF_ID.findall(ligne):
                if ident not in connus[genre]:
                    constats.append(Constat(
                        ERREUR, "REF-04",
                        "Référence `%s:%s` : aucun %s ne porte cet identifiant."
                        % (genre, ident, genre), chemin=fichier.chemin, ligne=num))


def _alias_connus(entites):
    table = {}
    for e in entites:
        for a in e.alias():
            table.setdefault(a, e)
    return table


def _resout(cellule, table):
    n = normalise(cellule)
    trouves = set()
    for alias, entite in table.items():
        motif = r"\b%s\b" % re.escape(alias).replace(r"\-", r"[ -]")
        if re.search(motif + "s?", n):
            trouves.add(entite)
    return trouves


def controle_noms_fantomes(inst, constats, heuristiques):
    """Postures et registres nommés en prose sans fichier. Tourne aussi en mode hérité."""
    if not heuristiques:
        return
    tp = _alias_connus(inst.postures)
    tr = _alias_connus(inst.registres)
    mots_vides = {"posture", "postures", "registre", "registres", "rapport", "voix", "audience",
                  "niveau", "etape", "skill", "version", "note", "hook", "mix"}
    for fichier in inst.tous_fichiers():
        propre = fichier.chemin.stem
        for num, ligne in fichier.enumerer():
            nu = sans_emphase(RE_COMMENTAIRE.sub(" ", ligne))
            n = normalise(nu)
            for genre, table, code in (("posture", tp, "REF-05"), ("registre", tr, "REF-06")):
                if not re.search(r"\b%ss?\b" % genre, n):
                    continue
                candidats = []
                for cite in re.findall(r'"([^"]{2,40})"|«\s*([^»]{2,40})\s*»', nu):
                    txt = (cite[0] or cite[1]).strip()
                    if re.search(RE_MAJ + r"\w{2,}", txt):
                        candidats.append(txt)
                # Pas de re.IGNORECASE ici : la classe RE_MAJ sert à repérer un mot capitalisé
                # juste après « posture »/« registre ». Sous IGNORECASE, [A-Z...] matche aussi les
                # minuscules et la détection dégénère en « n'importe quel mot suivant », noyant les
                # vrais candidats (noms propres) sous des mots de liaison ordinaires. On couvre
                # quand même « Posture Ami » en tête de phrase via l'alternative capitalisée, sans
                # relâcher la casse exigée sur le mot capturé.
                motif_genre = r"\b(?:%s|%s)s?\s+(%s[\w'’-]{2,})" % (genre, genre.capitalize(),
                                                                     RE_MAJ)
                for m in re.finditer(motif_genre, nu):
                    candidats.append(m.group(1))
                for txt in candidats:
                    txt = txt.split("/")[0].strip()
                    if normalise(txt) in mots_vides or not txt:
                        continue
                    if normalise(txt) == normalise(propre):
                        continue
                    if _resout(txt, table):
                        continue
                    constats.append(Constat(
                        AVERT, code,
                        "%s « %s » nommé ici, aucun fichier ne le définit (heuristique de "
                        "libellé)." % (genre.capitalize(), txt),
                        chemin=fichier.chemin, ligne=num))


def _inventaires(inst):
    """Noms de registres annoncés dans la description et dans le workflow."""
    skill = inst.fichiers.get("SKILL.md")
    if skill is None:
        return []
    trouves = []
    description = skill.fm.get("description", "")
    # Seule la première parenthèse de la description porte l'inventaire de registres (patron du
    # gabarit : « Rédige tout texte (<inventaire>) dans la voix... »). Les parenthèses suivantes
    # sont de la prose ordinaire (clauses d'exclusion, exemples) : les scanner toutes produisait des
    # faux INV-01 sur des fragments comme « pas pour du code ».
    m_desc = re.search(r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)", description)
    if m_desc:
        bloc = m_desc.group(1)
        if "/" in bloc or "," in bloc:
            interne = re.sub(r"\([^()]*\)", "", bloc)
            for item in re.split(r"[,/]", interne):
                trouves.append(("description", 0, item))
    for num, ligne in skill.enumerer():
        if "references/registres/" not in ligne and "registres/" not in ligne:
            continue
        m = re.search(r"\(([^()]*)\)", sans_emphase(ligne))
        if not m:
            continue
        interne = re.sub(r"^[^:]*:", "", m.group(1))
        for item in re.split(r"[,/]", interne):
            trouves.append(("workflow", num, item))
    sortie = []
    for origine, num, item in trouves:
        item = sans_emphase(item).strip(" .`*_")
        n = normalise(item)
        if not n or n in {"etc", "medium", "media"} or len(n) < 3:
            continue
        sortie.append((origine, num, item, n))
    return sortie


def controle_inventaire(inst, constats):
    skill = inst.fichiers.get("SKILL.md")
    if skill is None:
        return
    table = _alias_connus(inst.registres)
    annonces = _inventaires(inst)
    atteints = set()
    repli = False
    signale = set()
    for origine, num, item, n in annonces:
        if n in {"autre", "autres", "other", "divers"}:
            repli = True
            continue
        trouves = _resout(item, table)
        if trouves:
            atteints |= trouves
            continue
        if n in signale:
            continue
        signale.add(n)
        constats.append(Constat(
            ERREUR, "INV-01",
            "Registre « %s » annoncé dans %s : aucun fichier dans references/registres/."
            % (item, "la description" if origine == "description" else "le workflow"),
            chemin=skill.chemin, ligne=num or 1,
            indice="un seul point de vérité : l'inventaire se génère depuis le répertoire."))
    for e in inst.registres:
        if e not in atteints:
            constats.append(Constat(
                AVERT, "INV-02",
                "Registre `%s` défini mais absent de l'inventaire de la description et du "
                "workflow : rien ne l'atteint." % e.ident, chemin=e.fichier.chemin, ligne=1))
    if repli:
        noms = {kebab(e.fichier.chemin.stem) for e in inst.registres}
        if not ({"defaut", "default", "generique"} & noms):
            constats.append(Constat(
                AVERT, "INV-03",
                "Repli « autre » annoncé sans fichier de registre par défaut : le comportement "
                "face à un medium non couvert n'est pas spécifié.", chemin=skill.chemin))


def _lignes_table(fichier):
    for num, ligne in fichier.enumerer():
        brut = ligne.strip()
        if not brut.startswith("|"):
            continue
        cellules = [c.strip() for c in brut.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cellules if c):
            continue
        yield num, cellules


def controle_atteignabilite(inst, constats):
    audience = inst.fichiers.get("audience")
    table = _alias_connus(inst.postures)
    atteintes = {}
    if audience is not None:
        for num, cellules in _lignes_table(audience):
            for cellule in cellules:
                for genre, ident in RE_REF_ID.findall(cellule):
                    if genre == "posture":
                        for e in inst.postures:
                            if e.ident == ident:
                                atteintes.setdefault(e.ident, ("routage", num))
                for e in _resout(cellule, table):
                    atteintes.setdefault(e.ident, ("routage", num))
            cible = cellules[-1] if cellules else ""
            _cibles_mortes(inst, cible, audience, num, table, constats)
    for e in inst.registres:
        for ident in lister(e.fichier.fm.get("charge")) + lister(e.fichier.fm.get("postures")):
            atteintes.setdefault(ident, ("override %s" % e.ident, 1))
        texte = e.fichier.texte()
        for _, ident in RE_REF_ID.findall(texte):
            atteintes.setdefault(ident, ("override %s" % e.ident, 1))
        for num, ligne in e.fichier.enumerer():
            for chemin in re.findall(r"postures?/([\w.-]+)\.md", ligne):
                atteintes.setdefault(kebab(chemin), ("override %s" % e.ident, num))
            if re.search(r"\bpostures?\b", normalise(ligne)):
                for cible in _resout(ligne, table):
                    atteintes.setdefault(cible.ident, ("override %s" % e.ident, num))
    for e in inst.postures:
        if e.ident not in atteintes:
            constats.append(Constat(
                ERREUR, "ATT-01",
                "Posture `%s` injoignable : aucune ligne de routage de l'audience et aucun "
                "override de registre ne la charge." % e.ident,
                chemin=e.fichier.chemin, ligne=1,
                indice="une posture sans voie d'activation est du contenu mort."))


def _cibles_mortes(inst, cellule, fichier, num, table, constats):
    """Un mot capitalisé non initial dans une cible de routage doit résoudre vers une posture."""
    nu = sans_emphase(cellule)
    mots = re.findall(r"[\w'’À-ÖØ-öø-ÿ-]+", nu)
    for i, mot in enumerate(mots):
        if i == 0 or len(mot) < 3 or not re.match(RE_MAJ, mot):
            continue
        if _resout(mot, table):
            continue
        if normalise(mot) in {"mix", "note", "hook", "posture", "rapport", "expert"}:
            continue
        constats.append(Constat(
            ERREUR, "ATT-02",
            "Cible de routage « %s » : le terme « %s » ne correspond à aucune posture."
            % (cellule.strip(), mot), chemin=fichier.chemin, ligne=num))


MOTS_ETAPE0 = re.compile(
    r"etape\s*0|fact\s*-?\s*check|verification\s+factuelle|fact\s*checker")
MOTS_SUSPENSION = re.compile(
    r"\b(suspend|suspendu|suspension|desactiv|neutralis|sans\s+etape|pas\s+d[eu]\s+fact|"
    r"n\s*est\s+pas\s+requis|facultati|optionnel|dispense|on\s+saute|se\s+saute)\b")


def controle_suspension(inst, constats):
    ids_voix = set(inst.traits_voix)
    ids_slop = set(inst.regles_slop)
    interdits = {"etape-0", "etape0", "fact-check", "fact-checker", "verification-factuelle",
                 "step-0", "factcheck"}
    for e in inst.postures:
        for ident in lister(e.fichier.fm.get("suspend")) + lister(e.fichier.fm.get("suspends")):
            if normalise(ident).replace(" ", "-") in interdits or MOTS_ETAPE0.search(
                    normalise(ident)):
                constats.append(Constat(
                    ERREUR, "SUS-03",
                    "La posture `%s` déclare suspendre `%s`. L'Étape 0 et le statut de principal "
                    "sur le contenu propositionnel ne sont jamais suspendables."
                    % (e.ident, ident), chemin=e.fichier.chemin, ligne=1))
            elif ident not in ids_voix:
                constats.append(Constat(
                    ERREUR, "SUS-01",
                    "La posture `%s` suspend `%s` : aucun trait de voix ne porte cet "
                    "identifiant." % (e.ident, ident), chemin=e.fichier.chemin, ligne=1))
    for e in inst.registres:
        for ident in lister(e.fichier.fm.get("surcharge")) + lister(
                e.fichier.fm.get("surcharges")):
            if ident not in ids_slop:
                constats.append(Constat(
                    ERREUR, "SUS-02",
                    "Le registre `%s` surcharge `%s` : aucune règle anti-slop ne porte cet "
                    "identifiant." % (e.ident, ident), chemin=e.fichier.chemin, ligne=1))
    for e in inst.postures + inst.registres:
        for num, ligne in e.fichier.enumerer():
            n = normalise(ligne)
            if not MOTS_ETAPE0.search(n) or not MOTS_SUSPENSION.search(n):
                continue
            if re.search(r"\b(reste|restent|toujours|jamais\s+suspend|non\s+suspend|"
                         r"n\s*est\s+jamais)\b", n):
                continue
            constats.append(Constat(
                ERREUR, "SUS-03",
                "Formulation qui paraît lever l'Étape 0 de vérification factuelle. Elle n'est "
                "jamais suspendable, y compris en posture de performance.",
                chemin=e.fichier.chemin, ligne=num))


MOTS_PERMISSION = re.compile(
    r"\b(accept[ée]e?s?|admise?s?|autoris[ée]e?s?|tol[ée]r[ée]e?s?|permise?s?|"
    r"reste(?:nt)?\s+utilisables?|peut\s+[êe]tre\s+utilis|on\s+peut|allowed|accepted|permitted)\b")
MOTS_INTERDICTION = re.compile(
    r"^\s*(pas\s+d|ne\s+pas|[ée]viter|jamais|bannir|proscri|no\s|avoid|never|don t)")
VIDES = set("""le la les un une des de du au aux et ou ni mais donc or car que qui quoi dont
ou pour par sur sous dans avec sans vers chez entre est sont etre avoir fait faire plus moins
tres bien mal quand comme si non oui ce cet cette ces son sa ses leur leurs notre nos votre vos
mon ma mes ton ta tes il elle ils elles on nous vous je tu texte phrase phrases mot mots
quand chaque tout toute tous toutes autre autres meme memes seul seule aussi alors ainsi
suffit suffire quand default the and not for with this that from""".split())


def _mots_cles(txt):
    return {m for m in normalise(txt).split()
            if len(m) >= 5 and m not in VIDES}


def controle_contradiction(inst, constats, heuristiques):
    """Une contradiction non déclarée est une erreur ; ici, détectée par polarité (heuristique)."""
    if not heuristiques or not inst.regles_slop:
        return
    interdictions = []
    frequence = {}
    for ident, regle in inst.regles_slop.items():
        if not MOTS_INTERDICTION.match(normalise(regle["texte"])):
            continue
        cles = _mots_cles(regle["texte"])
        interdictions.append((ident, regle, cles))
        for mot in cles:
            frequence[mot] = frequence.get(mot, 0) + 1
    if not interdictions:
        return
    for e in inst.registres:
        declares = set(lister(e.fichier.fm.get("surcharge")) + lister(
            e.fichier.fm.get("surcharges")))
        for num, ligne in e.fichier.enumerer():
            texte = sans_emphase(ligne)
            if not MOTS_PERMISSION.search(normalise(texte)):
                continue
            cles = _mots_cles(texte)
            meilleur = None
            for ident, regle, cles_regle in interdictions:
                if ident in declares:
                    continue
                communs = {m for m in (cles & cles_regle) if frequence.get(m, 9) <= 2}
                if not communs:
                    continue
                score = len(communs)
                if meilleur is None or score > meilleur[0]:
                    meilleur = (score, ident, regle, sorted(communs))
            if meilleur is None:
                continue
            _, ident, regle, communs = meilleur
            constats.append(Constat(
                AVERT, "SUS-04",
                "Permission de registre qui paraît contredire la règle anti-slop `%s` (%s:%d) "
                "sans la déclarer en `surcharge:`. Termes communs : %s."
                % (ident, Path(regle["chemin"]).name, regle["ligne"], ", ".join(communs)),
                chemin=e.fichier.chemin, ligne=num,
                indice="une contradiction non déclarée est une erreur du contrat ; ici elle "
                       "n'est détectée que par heuristique de polarité."))


RE_INVARIANCE = [
    (re.compile(r"peu\s+importe[^.;]{0,80}\b(posture|registre|audience)"),
     "« peu importe … la posture/le registre »"),
    (re.compile(r"(quelle?\s+que\s+soit|quels?\s+que\s+soient)[^.;]{0,80}"
                r"\b(posture|registre|audience)"), "« quelle que soit la posture »"),
    (re.compile(r"\b(en\s+toute\s+circonstance|sans\s+exception|dans\s+tous\s+les\s+cas)\b"),
     "formule d'exception nulle"),
    (re.compile(r"(persist|s\s*appliquent?|tiennent?|valent?)[^.;]{0,40}"
                r"\b(toujours|partout)\b"), "« s'applique toujours / partout »"),
    (re.compile(r"regardless\s+of[^.;]{0,60}\b(posture|register|audience)"),
     "« regardless of the posture »"),
    (re.compile(r"no\s+matter[^.;]{0,60}\b(posture|register)"), "« no matter the posture »"),
]
RE_INVARIANCE_MOU = re.compile(r"\binvariants?\b|\bimmuables?\b|\bnon\s+negociables?\b")
# Une ligne qui décrit l'interdit pour l'interdire (documentation du gabarit, rappel de règle) ne
# commet pas la formule : « ce que ce fichier ne fait jamais : dire qu'un trait s'applique quelle
# que soit la posture » cite l'anti-patron dans une négation, il n'est pas énoncé comme un fait.
RE_INVARIANCE_META = re.compile(
    r"\b(dire|dit|ecrire|ecrit|enoncer|enonce|affirmer|affirme|formuler|formule|"
    r"pretendre|pretend|poser|pose|porter|porte|employer|emploie|generaliser|generalise|"
    r"mentionner|mentionne|presenter|presente|laisser|laisse)\b")
RE_INVARIANCE_NEGATION = re.compile(r"\bne\s|\bn\s|\bjamais\b|\bsans\b")


def ligne_meta_invariance(n):
    """Vrai si la ligne PARLE de la formule interdite au lieu de la commettre.

    Deux conditions cumulees : une negation, et un verbe de parole ou d'attribution. Une phrase
    comme « ce trait ne disparait jamais, peu importe la posture » porte bien une negation, mais
    aucun verbe de parole : c'est la formule elle-meme, elle doit etre signalee.
    """
    return bool(RE_INVARIANCE_NEGATION.search(n) and RE_INVARIANCE_META.search(n))


def controle_invariance(inst, constats):
    voix = inst.fichiers.get("voix")
    if voix is None:
        return
    for num, ligne in voix.enumerer(depuis_corps=False):
        n = normalise(ligne)
        touche = False
        if ligne_meta_invariance(n):
            continue
        for motif, libelle in RE_INVARIANCE:
            if motif.search(n):
                constats.append(Constat(
                    ERREUR, "VOIX-01",
                    "Formule d'invariance absolue dans voix.md : %s. C'est le défaut de "
                    "conception que ce projet corrige : un trait de voix est une tendance par "
                    "défaut qu'une posture peut surcharger en le déclarant." % libelle,
                    chemin=voix.chemin, ligne=num))
                touche = True
                break
        if not touche and RE_INVARIANCE_MOU.search(n):
            constats.append(Constat(
                AVERT, "VOIX-02",
                "Vocabulaire d'invariance (« invariant », « immuable », « non négociable ») dans "
                "voix.md : vérifier qu'il n'induit pas une portée absolue.",
                chemin=voix.chemin, ligne=num))


RE_GABARIT = [
    (re.compile(r"\{\{[^}]{1,80}\}\}"), "moustache {{…}}"),
    (re.compile(r"\b(TODO|FIXME|XXX|TBD|PLACEHOLDER|LOREM IPSUM)\b"), "marqueur de travail"),
    (re.compile(r"[ÀA]\s+(REMPLIR|COMPL[ÉE]TER|[ÉE]CRIRE|D[ÉE]FINIR)", re.IGNORECASE),
     "emplacement annoncé"),
    (re.compile(r"_{3,}|\.{4,}\s*$"), "trou typographique"),
]
RE_CHEVRON = re.compile(r"<([^<>\n]{1,60})>")


def controle_gabarit(inst, constats, brouillon):
    niveau = AVERT if brouillon else ERREUR
    for fichier in inst.tous_fichiers():
        dans_bloc = False
        for num, ligne in fichier.enumerer(depuis_corps=False):
            if ligne.lstrip().startswith("```"):
                dans_bloc = not dans_bloc
                continue
            if dans_bloc:
                continue
            nu = RE_COMMENTAIRE.sub(" ", ligne)
            for motif, libelle in RE_GABARIT:
                m = motif.search(nu)
                if m:
                    constats.append(Constat(
                        niveau, "GAB-01",
                        "Emplacement de gabarit non rempli (%s) : « %s »."
                        % (libelle, m.group(0).strip()), chemin=fichier.chemin, ligne=num))
            hors_code = RE_CODE.sub(" ", RE_AUTOLIEN.sub(" ", nu))
            for m in RE_CHEVRON.finditer(hors_code):
                contenu = m.group(1)
                if contenu.startswith("/") or re.match(r"^[a-z]+[ />]?$", contenu):
                    continue  # balise HTML
                if re.match(r"^[a-zA-Z][\w+.-]*:", contenu):
                    continue  # autolien résiduel
                constats.append(Constat(
                    niveau, "GAB-01",
                    "Emplacement de gabarit non rempli (chevrons) : « <%s> »." % contenu,
                    chemin=fichier.chemin, ligne=num))


def controle_postures(inst, constats):
    decl = re.compile(r"declench|se\s+charge\s+quand|triggered\s+when|charg[ée]e?\s+quand")
    fc = re.compile(r"fact\s*-?\s*check|verification\s+factuelle|etape\s*0")
    for e in inst.postures:
        texte = normalise(e.fichier.texte())
        if not decl.search(texte) and not e.fichier.fm.get("declencheur"):
            constats.append(Constat(
                AVERT, "POST-01",
                "Posture `%s` sans phrase de déclenchement : rien ne dit quand elle se charge."
                % e.ident, chemin=e.fichier.chemin, ligne=1))
        if not fc.search(texte):
            constats.append(Constat(
                AVERT, "POST-02",
                "Posture `%s` sans section de ton du fact-check : l'Étape 0 n'a pas de voix dans "
                "cette posture." % e.ident, chemin=e.fichier.chemin, ligne=1))


RE_CITATION = re.compile(r"\(\s*(?:19|20)\d{2}[a-z]?\s*\)|(?:19|20)\d{2}|&|https?://|arXiv|ISBN")
MOTS_VOIX = re.compile(r"\btics?\b|\bmarqueurs?\b|\binvariants?\b|voix\.md|`voix:")


def controle_permeabilite(inst, constats, heuristiques):
    if not heuristiques:
        return
    for e in inst.registres:
        for num, ligne in e.fichier.enumerer():
            if MOTS_VOIX.search(normalise(ligne)) or "voix.md" in ligne or "`voix:" in ligne:
                constats.append(Constat(
                    AVERT, "PERM-01",
                    "Fichier de registre qui paraît nommer un marqueur de voix. Un registre "
                    "exprime une perméabilité abstraite (« le plus permissif sur les marqueurs "
                    "figuratifs »), jamais un marqueur nommé : chez quelqu'un qui n'a pas ce "
                    "trait, la ligne est morte.", chemin=e.fichier.chemin, ligne=num))


def controle_personnel(inst, constats, heuristiques, nom):
    if not heuristiques:
        return
    universels = [e.fichier for e in inst.registres]
    for cle in ("anti-slop", "SKILL.md", "audience"):
        if cle in inst.fichiers:
            universels.append(inst.fichiers[cle])
    labels = set()
    for e in inst.postures + inst.registres:
        labels |= e.alias()
    audience = inst.fichiers.get("audience")
    if audience is not None:
        for _, ligne in audience.enumerer():
            for gras in re.findall(r"\*\*([^*]{2,40})\*\*", ligne):
                labels.add(kebab(gras))
            for _, cellules in [(0, [c.strip() for c in ligne.strip().strip("|").split("|")])]:
                for c in cellules:
                    if c and len(c) < 60:
                        labels.add(kebab(c))
    labels |= {"etape", "registre", "posture", "voix", "audience", "skill", "niveau", "rapport",
               "source", "test", "note", "version", "wikipedia", "structure", "longueur",
               "public", "perimetre", "contrainte", "titre", "titres", "ton", "lexique"}
    # Vocabulaire du modèle à quatre couches : ce sont des termes techniques du skill, pas des
    # noms propres. Sans cette liste, toute instance réelle croule sous les faux PERS-01.
    labels |= {
        # 8 composantes de voix
        "substrat", "signature", "typographique", "empan", "predilection", "geste", "rhetorique",
        "architecture", "propos", "reflexe", "interpersonnel", "regard",
        # 7 composantes de posture
        "ouverture", "dialogique", "intensite", "evaluative", "droit", "affirmer", "franchise",
        "proximite", "construite", "adresse", "lecteur", "prise", "charge", "enonciative",
        # 7 postures du catalogue
        "apprenant", "pair", "pairs", "guide", "arbitre", "contradicteur", "diplomate",
        "provocateur",
        # mécanique du skill
        "composante", "composantes", "couche", "couches", "forme", "dose", "direction", "entree",
        "entrees", "valeur", "marqueur", "marqueurs", "calibration", "corpus", "delta", "norme",
        "normes", "instance", "gabarit", "plancher", "filtre", "extraction", "protocole",
        "invariant", "invariants", "suspend", "surcharge", "anti-slop", "corroboration",
    }
    # Références de méthode citées par `anti-slop.md`, livré tel quel dans toute instance : ce
    # sont des sources et des outils nommés par la méthode, pas des fuites personnelles.
    labels |= {"llm", "llms", "pubmed", "chatgpt", "cleanup", "kobak"}
    for fichier in universels:
        dans_bloc = False
        for num, ligne in fichier.enumerer():
            if ligne.lstrip().startswith("```"):
                dans_bloc = not dans_bloc
                continue
            if dans_bloc or ligne.strip().startswith("#"):
                continue
            if RE_CITATION.search(ligne) or normalise(ligne).startswith("source"):
                continue
            nu = sans_emphase(RE_COMMENTAIRE.sub(" ", ligne))
            nu = RE_CODE.sub(" ", nu)
            if nom and re.search(r"\b%s\b" % re.escape(nom), nu, re.IGNORECASE):
                constats.append(Constat(
                    AVERT, "PERS-02",
                    "Nom de la personne dans un fichier réputé universel.",
                    chemin=fichier.chemin, ligne=num))
            morceaux = re.split(r"(?:^|[.:;!?]\s+|\(|«\s*|—\s+|-\s+|\d\.\s+|\|\s*)", nu)
            for morceau in morceaux:
                mots = re.findall(r"[\w'’À-ÖØ-öø-ÿ-]+", morceau)
                for i, mot in enumerate(mots):
                    if i == 0 or len(mot) < 3:
                        continue
                    if not re.match(RE_MAJ, mot):
                        continue
                    if kebab(mot) in labels or normalise(mot) in VIDES:
                        continue
                    constats.append(Constat(
                        AVERT, "PERS-01",
                        "« %s » : nom propre ou marque probable dans un fichier réputé "
                        "universel. Les exemples situés et le vocabulaire métier vont dans une "
                        "annexe de domaine." % mot, chemin=fichier.chemin, ligne=num))


def controle_versions(inst, constats):
    skill = inst.fichiers.get("SKILL.md")
    journal = inst.skill / "changelog.md"
    if skill is None or not journal.is_file():
        return
    dans_skill = None
    for _, ligne in skill.enumerer():
        m = re.search(r"notes?\s+de\s+version\s*\(?\s*v?([\d.]+)", ligne, re.IGNORECASE)
        if m:
            dans_skill = m.group(1).rstrip(".")
            break
    dans_journal = None
    for ligne in lire(journal):
        m = re.match(r"^##\s+v?([\d.]+)", ligne.strip())
        if m:
            dans_journal = m.group(1)
            break
    if dans_skill and dans_journal and not dans_journal.startswith(dans_skill):
        constats.append(Constat(
            AVERT, "VERS-01",
            "SKILL.md annonce la version %s, changelog.md est à %s. Deux systèmes de version "
            "simultanés dérivent." % (dans_skill, dans_journal), chemin=skill.chemin))


def controle_plugin(inst, constats):
    if inst.plugin is None:
        return
    manifeste = inst.plugin / ".claude-plugin" / "plugin.json"
    if not manifeste.is_file():
        constats.append(Constat(AVERT, "STRUCT-03",
                                "Pas de .claude-plugin/plugin.json : l'instance n'est pas un "
                                "plugin autonome.", chemin=inst.plugin))
    else:
        try:
            json.loads(manifeste.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            constats.append(Constat(AVERT, "STRUCT-03",
                                    "plugin.json illisible : %s" % exc, chemin=manifeste))
    if not list(inst.plugin.glob("agents/fact-checker*.md")):
        constats.append(Constat(
            AVERT, "STRUCT-04",
            "Aucun agent `fact-checker` dans le plugin : l'Étape 0 de l'instance n'a personne à "
            "appeler.", chemin=inst.plugin))


def controle_aspirations(inst, constats):
    cible = inst.skill / "references" / "voix-aspirations.md"
    if not cible.is_file():
        return
    for fichier in inst.tous_fichiers():
        for num, ligne in fichier.enumerer():
            if "voix-aspirations" in ligne:
                constats.append(Constat(
                    AVERT, "STRUCT-05",
                    "`voix-aspirations.md` est cité ici. Il ne doit jamais être chargé : il "
                    "contient des traits revendiqués mais non observés.",
                    chemin=fichier.chemin, ligne=num))


# ---------------------------------------------------------------------------
# Rapport
# ---------------------------------------------------------------------------


def imprimer_rapport(constats, inst, racine, sortie):
    erreurs = [c for c in constats if c.niveau == ERREUR]
    averts = [c for c in constats if c.niveau == AVERT]
    for titre, lot in (("ERREURS", erreurs), ("AVERTISSEMENTS", averts)):
        if not lot:
            continue
        print("\n%s (%d)" % (titre, len(lot)), file=sortie)
        print("-" * (len(titre) + 8), file=sortie)
        for c in sorted(lot, key=Constat.cle_tri):
            lieu = ""
            if c.chemin:
                try:
                    rel = Path(c.chemin).relative_to(racine)
                except ValueError:
                    rel = Path(c.chemin)
                lieu = str(rel) + (":%d" % c.ligne if c.ligne else "")
            print("  [%s] %s" % (c.code, lieu), file=sortie)
            print("      %s" % c.message, file=sortie)
            if c.indice:
                print("      → %s" % c.indice, file=sortie)
    print("", file=sortie)
    if inst is not None and inst.mode_herite():
        print("Mode hérité : aucun identifiant stable déclaré, contrôles par id dégradés en "
              "heuristiques.", file=sortie)
    print("Bilan : %d erreur(s), %d avertissement(s)." % (len(erreurs), len(averts)),
          file=sortie)
    if erreurs:
        print("L'instance n'est pas livrable en l'état.", file=sortie)
    else:
        print("Aucune erreur bloquante. Les avertissements restent à lire : plusieurs sont des "
              "heuristiques, ils demandent un jugement.", file=sortie)
    print("`--explique` liste les contrôles effectués et surtout ce qu'ils ne couvrent pas.",
          file=sortie)


def imprimer_explication(sortie):
    print("valide-instance.py %s — catalogue des contrôles\n" % VERSION, file=sortie)
    largeur = max(len(c) for c, _, _ in CATALOGUE)
    for code, niveau, texte in CATALOGUE:
        print("  %-*s  %-6s  %s" % (largeur, code, niveau, texte), file=sortie)
    print("", file=sortie)
    print("Heuristiques (jugement requis, jamais des preuves) : REF-05, REF-06, SUS-04, PERM-01, "
          "PERS-01.", file=sortie)
    print("Elles se désactivent avec --sans-heuristiques.\n", file=sortie)
    print(NON_COUVERT, file=sortie)
    print("", file=sortie)
    print(__doc__.split("Conventions d'identifiants attendues")[1].split("Mode hérité")[0].strip(),
          file=sortie)


def construire_parseur():
    p = argparse.ArgumentParser(
        prog="valide-instance.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Valide une instance générée par write-forge : intégrité référentielle, "
                    "atteignabilité, suspensions et surcharges déclarées, emplacements non "
                    "remplis, chemins relatifs, personnel résiduel, formule d'invariance.",
        epilog="Code de retour : 0 si aucune erreur, 1 s'il y a au moins une erreur, "
               "2 en cas de problème d'invocation.\n"
               "Exemples :\n"
               "  valide-instance.py plugins/write-alex/\n"
               "  valide-instance.py plugins/write-alex/skills/write/ --brouillon\n"
               "  valide-instance.py --explique")
    p.add_argument("instance", nargs="?",
                   help="chemin du plugin d'instance, ou du répertoire du skill (celui qui "
                        "contient SKILL.md)")
    p.add_argument("--explique", action="store_true",
                   help="imprime le catalogue des contrôles et la liste de ce qui n'est pas "
                        "couvert, puis sort")
    p.add_argument("--brouillon", action="store_true",
                   help="instance en cours de construction : les emplacements de gabarit non "
                        "remplis deviennent des avertissements")
    p.add_argument("--sans-heuristiques", action="store_true",
                   help="ne garde que les contrôles déterministes")
    p.add_argument("--nom", metavar="PRÉNOM",
                   help="nom de la personne, pour vérifier qu'il ne fuit pas dans les fichiers "
                        "réputés universels")
    p.add_argument("--json", action="store_true", help="sortie machine sur stdout")
    p.add_argument("--version", action="version", version="valide-instance.py " + VERSION)
    return p


def main(argv=None):
    args = construire_parseur().parse_args(argv)
    if args.explique:
        imprimer_explication(sys.stdout)
        return 0
    if not args.instance:
        print("Il faut un chemin d'instance. `--help` pour l'usage, `--explique` pour le "
              "catalogue des contrôles.", file=sys.stderr)
        return 2
    racine = Path(args.instance).expanduser().resolve()
    if not racine.is_dir():
        print("Chemin introuvable ou pas un répertoire : %s" % racine, file=sys.stderr)
        return 2

    constats = []
    inst = Instance(racine)
    if not inst.localiser(constats):
        if args.json:
            print(json.dumps({"erreurs": [c.en_dict() for c in constats]}, ensure_ascii=False,
                             indent=2))
        else:
            imprimer_rapport(constats, None, racine, sys.stdout)
        return 1

    inst.charger(constats)
    heur = not args.sans_heuristiques

    controle_identifiants(inst, constats)
    controle_chemins(inst, constats)
    controle_references_id(inst, constats)
    controle_noms_fantomes(inst, constats, heur)
    controle_inventaire(inst, constats)
    controle_atteignabilite(inst, constats)
    controle_suspension(inst, constats)
    controle_contradiction(inst, constats, heur)
    controle_invariance(inst, constats)
    controle_gabarit(inst, constats, args.brouillon)
    controle_postures(inst, constats)
    controle_permeabilite(inst, constats, heur)
    controle_personnel(inst, constats, heur, args.nom)
    controle_versions(inst, constats)
    controle_plugin(inst, constats)
    controle_aspirations(inst, constats)

    erreurs = sum(1 for c in constats if c.niveau == ERREUR)
    if args.json:
        print(json.dumps({
            "instance": str(racine),
            "skill": str(inst.skill),
            "mode_herite": inst.mode_herite(),
            "erreurs": erreurs,
            "avertissements": len(constats) - erreurs,
            "constats": [c.en_dict() for c in sorted(constats, key=Constat.cle_tri)],
        }, ensure_ascii=False, indent=2))
    else:
        print("valide-instance.py %s — %s" % (VERSION, racine))
        print("Skill validé : %s" % inst.skill)
        imprimer_rapport(constats, inst, racine, sys.stdout)
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
