#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""compte-traits.py — filtre de réfutation sur un corpus, pour `write-forge` (Étape 3).

CADRAGE IMPÉRATIF, À LIRE AVANT D'UTILISER LA SORTIE
-----------------------------------------------------
Ce script ne trouve la voix de personne. Il ne découvre rien. Il écarte : un candidat dont la
fréquence est nulle ou confinée à un seul registre est un trait de *registre*, pas de voix, et ce
script le dit. Un trait qui « passe » ce filtre (stable sur au moins deux registres) n'est pas pour
autant confirmé — il n'a fait que survivre à un tri grossier. La substance d'un `voix.md` vient de la
lecture des mouvements de discours et de l'entretien (protocole d'extraction, étapes 5 et 6), jamais
de ce tableau. Voir `references/protocole-extraction.md`, Règle 1 : « le comptage réfute, il ne
découvre pas ».

Ce que fait ce script
----------------------
1. Charge un corpus déjà qualifié (l'éligibilité, étape 1 du protocole, est un préalable : ce script
   ne filtre aucun item par statut de révision, il suppose qu'on ne lui donne que des items
   éligibles).
2. Calcule des taux **par registre**, en agrégeant tous les destinataires à l'intérieur d'un
   registre. Il ne calcule jamais de taux par cellule registre × destinataire : le croisement rend
   chaque cellule trop petite et bloque tout le pipeline (voir carte des fichiers de
   `write-forge/SKILL.md`, et étape 3 du protocole).
3. Normalise la typographie avant de compter les mots et les phrases (apostrophes droites/courbes,
   guillemets, espaces insécables, tirets), pour qu'une variante d'encodage ne gonfle pas un taux.
   Les compteurs de *style* typographique (guillemets français ou anglais, apostrophe droite ou
   courbe...) travaillent eux sur le texte non normalisé : leur normaliser l'entrée détruirait
   justement le signal qu'ils mesurent.
4. Refuse de produire un taux pour tout registre sous le seuil de mots (1 500 par défaut, voir
   `protocole-extraction.md`), et le dit explicitement plutôt que d'afficher un résultat trompeur.
5. Signale, sans les proposer comme candidats, les lexèmes qui reviennent sur au moins deux
   registres et qui ne sont pas des mots-outils (angle mort du Lexique de prédilection, composante 4
   de `composantes-voix.md`).
6. Signale les formes ambiguës du français (« on », le conditionnel, la forme interrogative) dans
   une section séparée, jamais routée : leur compte brut n'est pas un taux de posture, voir
   `composantes-posture.md`, section « Ambiguïté du français ».

Ce que ce script ne fait PAS
------------------------------
- Il ne décide pas qu'un trait est de la Voix. Le tri « stable sur ≥ 2 registres » qu'il imprime est
  un mouvement mécanique de present/absent, pas le test de tri à trois filtres du protocole
  (`modele-concepts.md`) : filtre de forme, filtre de persistance, filtre d'intentionnalité. Un
  candidat listé ici doit encore passer ces trois filtres, l'entretien, et l'écran de choix forcé
  aveugle avant d'entrer dans `voix.md`.
- Il ne désambiguïse pas « on », le conditionnel ou la forme interrogative : ce sont des comptes
  bruts, signalés comme tels, jamais consommés par le tri.
- Il n'écrit aucun fichier de l'instance. Il imprime un tableau.

Configuration dépendante de la langue
---------------------------------------
Les listes de marqueurs (mots-outils, connecteurs, intensifieurs, formes ambiguës, marqueurs
typographiques) sont externalisées dans `langues/<code>.json`, jamais codées en dur dans ce fichier.
`--langue fr` charge `langues/fr.json` à côté de ce script ; `--config chemin.json` charge une
configuration arbitraire à la place (elle remplace le fichier groupé, elle ne le complète pas).
Une nouvelle langue se re-dérive dans son propre fichier de config, elle ne se traduit pas depuis
`fr.json` (protocole d'extraction, Règle 4).

Entrée
------
Deux façons de décrire le corpus, au choix :

- `--corpus DIR` : un répertoire contenant un sous-répertoire par identifiant de registre, chacun
  rempli de fichiers `.txt` ou `.md` (frontmatter YAML ignoré s'il y en a un).
      corpus/
        email/item-01.md
        email/item-02.md
        rapport-technique/item-01.md
- `--manifest FICHIER` : un CSV (colonnes `chemin,registre` et `destinataire` optionnelle) ou un
  JSON (liste d'objets `{"chemin": ..., "registre": ..., "destinataire": ...}`). Les chemins sont
  résolus depuis le répertoire du manifeste. `destinataire` n'est jamais utilisé pour calculer un
  taux, seulement compté à titre indicatif (nombre de destinataires distincts par registre).

Python 3, bibliothèque standard uniquement.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

VERSION = "1.0"
SEUIL_MOTS_DEFAUT = 1500
SCRIPT_DIR = Path(__file__).resolve().parent

def _sortir(message, code=2):
    """Erreur d'invocation ou de données : message sur stderr, code 2 (aligné sur
    valide-instance.py : 0 nominal, 2 problème d'invocation)."""
    print(message, file=sys.stderr)
    raise SystemExit(code)


CADRAGE = (
    "Ce script est un FILTRE DE RÉFUTATION, pas une source de découverte. Il ne trouve la voix de\n"
    "personne : il écarte des traits crus « personnels » qui sont en fait des traits de registre,\n"
    "ou dont la fréquence est nulle ou confinée à un seul registre. La substance d'un voix.md vient\n"
    "de la lecture des mouvements de discours et de l'entretien (protocole, étapes 5 et 6), jamais\n"
    "de ce tableau. Un trait listé ici « candidat Voix » n'est pas confirmé : il doit encore passer\n"
    "le test de tri à trois filtres, l'entretien, et l'écran de choix forcé aveugle."
)


# ---------------------------------------------------------------------------
# Normalisation typographique
# ---------------------------------------------------------------------------

# Caractères collapsés vers une forme canonique avant tout comptage de mots, de phrases ou de
# taux de mots-outils/connecteurs. Volontairement séparé du comptage des marqueurs *typographiques*
# eux-mêmes (fonction compter_marqueurs_typographiques), qui travaille sur le texte non normalisé :
# le style de guillemets ou d'apostrophe EST le signal à cet endroit-là, le normaliser l'effacerait.
_TABLE_NORMALISATION = {
    "’": "'", "‘": "'", "‛": "'", "´": "'", "`": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "«": '"', "»": '"',
    " ": " ", " ": " ", " ": " ", " ": " ",
    "–": "-", "—": "-",
}
_RE_NORMALISATION = re.compile("|".join(re.escape(c) for c in _TABLE_NORMALISATION))


def normaliser_typo(texte):
    """Forme canonique du texte pour le comptage de mots/phrases/mots-outils/connecteurs.

    Unifie apostrophes droites et courbes, guillemets (français, anglais courbes, droits),
    espaces insécables de toute largeur, et tirets moyen/cadratin. N'est JAMAIS utilisée pour
    compter le style typographique lui-même (voir docstring du module).
    """
    texte = unicodedata.normalize("NFC", texte)
    return _RE_NORMALISATION.sub(lambda m: _TABLE_NORMALISATION[m.group(0)], texte)


RE_MOT = re.compile(r"[^\W\d_]+(?:['\-][^\W\d_]+)*", re.UNICODE)


def compter_mots(texte_normalise):
    return RE_MOT.findall(texte_normalise)


def decouper_phrases(texte_normalise):
    """Découpage approximatif : ponctuation forte suivie d'une majuscule ou de fin de texte.

    Heuristique documentée comme telle : aucune gestion des abréviations, des initiales ou des
    citations imbriquées. Suffisant pour une distribution grossière, pas pour un décompte exact.
    """
    texte = texte_normalise.strip()
    if not texte:
        return []
    morceaux = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÖØ-Þ0-9\"«])", texte)
    return [m.strip() for m in morceaux if m.strip()]


def decouper_paragraphes(texte_normalise):
    morceaux = re.split(r"\n\s*\n", texte_normalise.strip())
    return [m.strip() for m in morceaux if m.strip()]


# ---------------------------------------------------------------------------
# Configuration dépendante de la langue
# ---------------------------------------------------------------------------


def charger_config(langue, chemin_config):
    if chemin_config:
        chemin = Path(chemin_config).expanduser()
        origine = str(chemin)
    else:
        chemin = SCRIPT_DIR / "langues" / ("%s.json" % langue)
        origine = str(chemin)
        if not chemin.is_file():
            langues_dispo = sorted(p.stem for p in (SCRIPT_DIR / "langues").glob("*.json"))
            _sortir(
                "Aucune configuration groupée pour la langue « %s ». Langues disponibles : %s. "
                "Pour une langue non couverte, fournissez --config avec un fichier construit sur "
                "le même schéma (voir langues/fr.json) : les listes de marqueurs ne se codent "
                "jamais en dur dans ce script, elles se dérivent par langue." % (
                    langue, ", ".join(langues_dispo) or "aucune"))
    try:
        donnees = json.loads(chemin.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        _sortir("Configuration illisible (%s) : %s" % (origine, exc))
    donnees["_origine"] = origine
    donnees.setdefault("mots_outils", [])
    donnees.setdefault("paires_quasi_synonymes", [])
    donnees.setdefault("connecteurs", {"contractifs": [], "expansifs": []})
    donnees.setdefault("intensite", {"force_haute": [], "force_basse": []})
    donnees.setdefault("formes_ambigues", {})
    donnees.setdefault("marqueurs_typographiques", {})
    return donnees


def _motif_phrase(expr):
    """Un motif insensible à la casse pour une expression d'un ou plusieurs mots."""
    morceaux = [re.escape(m) for m in expr.split(" ")]
    return re.compile(r"\b%s\b" % r"\s+".join(morceaux), re.IGNORECASE)


# ---------------------------------------------------------------------------
# Chargement du corpus
# ---------------------------------------------------------------------------


class Item:
    __slots__ = ("chemin", "registre", "destinataire", "texte_brut", "texte_normalise", "mots")

    def __init__(self, chemin, registre, destinataire=None):
        self.chemin = chemin
        self.registre = registre
        self.destinataire = destinataire
        self.texte_brut = None
        self.texte_normalise = None
        self.mots = []


def _lire_texte(chemin):
    for enc in ("utf-8", "latin-1"):
        try:
            texte = chemin.read_text(encoding=enc)
            break
        except UnicodeDecodeError:
            continue
        except OSError as exc:
            return None, str(exc)
    else:
        return None, "encodage non reconnu"
    lignes = texte.splitlines()
    if lignes and lignes[0].strip() == "---":
        for i in range(1, len(lignes)):
            if lignes[i].strip() == "---":
                texte = "\n".join(lignes[i + 1:])
                break
    return texte, None


def charger_corpus_repertoire(racine, diagnostics):
    items = []
    racine = Path(racine)
    for sous_dir in sorted(p for p in racine.iterdir() if p.is_dir()):
        registre = sous_dir.name
        for fichier in sorted(sous_dir.iterdir()):
            if not fichier.is_file() or fichier.suffix.lower() not in (".txt", ".md"):
                continue
            texte, erreur = _lire_texte(fichier)
            if erreur:
                diagnostics.append("Ignoré (%s) : %s" % (erreur, fichier))
                continue
            items.append((fichier, registre, None, texte))
    return items


def charger_corpus_manifeste(chemin_manifeste, diagnostics):
    chemin_manifeste = Path(chemin_manifeste)
    base = chemin_manifeste.parent
    lignes = []
    if chemin_manifeste.suffix.lower() == ".json":
        try:
            data = json.loads(chemin_manifeste.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            _sortir("Manifeste illisible : %s" % exc)
        for entree in data:
            lignes.append((entree.get("chemin"), entree.get("registre"),
                            entree.get("destinataire")))
    else:
        with chemin_manifeste.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                lignes.append((row.get("chemin"), row.get("registre"), row.get("destinataire")))
    items = []
    for chemin_rel, registre, destinataire in lignes:
        if not chemin_rel or not registre:
            diagnostics.append("Ligne de manifeste incomplète ignorée : %r" % ((chemin_rel,
                                                                                 registre),))
            continue
        chemin = (base / chemin_rel).expanduser()
        if not chemin.is_file():
            diagnostics.append("Fichier introuvable, ignoré : %s" % chemin)
            continue
        texte, erreur = _lire_texte(chemin)
        if erreur:
            diagnostics.append("Ignoré (%s) : %s" % (erreur, chemin))
            continue
        items.append((chemin, registre.strip(), (destinataire or "").strip() or None, texte))
    return items


# ---------------------------------------------------------------------------
# Comptage
# ---------------------------------------------------------------------------


def compter_marqueurs_typographiques(config, texte_brut):
    """Sur le texte NON normalisé : le style est le signal (voir docstring)."""
    sortie = {}
    for nom, spec in config["marqueurs_typographiques"].items():
        motif = spec.get("motif")
        if not motif:
            continue
        flags = re.MULTILINE if nom == "puce_liste" else 0
        try:
            sortie[nom] = len(re.findall(motif, texte_brut, flags))
        except re.error as exc:
            _sortir("Motif invalide pour le marqueur « %s » : %s" % (nom, exc))
    return sortie


def compter_phrase(motif_compile, texte_normalise):
    return len(motif_compile.findall(texte_normalise))


def analyser_corpus(items_bruts, config):
    """Construit les Item, calcule mots/phrases/paragraphes normalisés par item."""
    items = []
    for chemin, registre, destinataire, texte in items_bruts:
        it = Item(chemin, registre, destinataire)
        it.texte_brut = texte
        it.texte_normalise = normaliser_typo(texte)
        it.mots = compter_mots(it.texte_normalise)
        items.append(it)
    return items


def rapport_par_registre(items, config, seuil_mots):
    par_registre = defaultdict(list)
    for it in items:
        par_registre[it.registre].append(it)

    registres = {}
    for registre, items_r in sorted(par_registre.items()):
        total_mots = sum(len(it.mots) for it in items_r)
        destinataires = {it.destinataire for it in items_r if it.destinataire}
        registres[registre] = {
            "items": items_r,
            "total_mots": total_mots,
            "n_items": len(items_r),
            "n_destinataires": len(destinataires),
            "sous_seuil": total_mots < seuil_mots,
        }
    return registres


def taux_mots_outils(config, items_r, total_mots):
    outils = {m.lower() for m in config["mots_outils"]}
    n = sum(1 for it in items_r for m in it.mots if m.lower() in outils)
    return (n / total_mots) * 1000 if total_mots else 0.0


def taux_expressions(expressions, items_r, total_mots):
    n = 0
    for expr in expressions:
        motif = _motif_phrase(expr)
        for it in items_r:
            n += compter_phrase(motif, it.texte_normalise)
    return (n / total_mots) * 1000 if total_mots else 0.0


def taux_typographiques(config, items_r, total_mots):
    sortie = {}
    totaux = Counter()
    for it in items_r:
        for nom, n in compter_marqueurs_typographiques(config, it.texte_brut).items():
            totaux[nom] += n
    for nom, n in totaux.items():
        sortie[nom] = (n / total_mots) * 1000 if total_mots else 0.0
    return sortie


def compter_formes_ambigues(config, items_r):
    sortie = {}
    for nom, spec in config["formes_ambigues"].items():
        motif = spec.get("motif")
        if not motif:
            continue
        try:
            compile_motif = re.compile(motif, re.IGNORECASE)
        except re.error as exc:
            _sortir("Motif invalide pour la forme ambiguë « %s » : %s" % (nom, exc))
        sortie[nom] = sum(compter_phrase(compile_motif, it.texte_normalise) for it in items_r)
    return sortie


def compter_paires_substrat(config, items_r):
    sortie = []
    for paire in config["paires_quasi_synonymes"]:
        membres = paire.get("membres", [])
        comptes = {}
        for m in membres:
            motif = _motif_phrase(m)
            comptes[m] = sum(compter_phrase(motif, it.texte_normalise) for it in items_r)
        sortie.append({"membres": membres, "comptes": comptes, "note": paire.get("note", "")})
    return sortie


def distribution(valeurs):
    if not valeurs:
        return None
    valeurs = sorted(valeurs)
    n = len(valeurs)
    return {
        "n": n,
        "moyenne": round(statistics.mean(valeurs), 1),
        "mediane": round(statistics.median(valeurs), 1),
        "p25": round(valeurs[max(0, int(n * 0.25) - 1)], 1) if n >= 4 else valeurs[0],
        "p75": round(valeurs[min(n - 1, int(n * 0.75))], 1),
        "max": valeurs[-1],
        "min": valeurs[0],
    }


def empan_registre(items_r):
    longueurs_phrases = []
    longueurs_paragraphes = []
    for it in items_r:
        for phrase in decouper_phrases(it.texte_normalise):
            longueurs_phrases.append(len(compter_mots(phrase)))
        for para in decouper_paragraphes(it.texte_normalise):
            longueurs_paragraphes.append(len(compter_mots(para)))
    return distribution(longueurs_phrases), distribution(longueurs_paragraphes)


def lexemes_recurrents(config, registres_valides, min_occurrences, min_longueur):
    outils = {m.lower() for m in config["mots_outils"]}
    freq_par_registre = {}
    for registre, info in registres_valides.items():
        c = Counter()
        for it in info["items"]:
            for m in it.mots:
                ml = m.lower()
                if len(ml) >= min_longueur and ml not in outils:
                    c[ml] += 1
        freq_par_registre[registre] = c

    tous_lexemes = set()
    for c in freq_par_registre.values():
        tous_lexemes.update(c)

    sortie = []
    for lex in sorted(tous_lexemes):
        par_reg = {r: c[lex] for r, c in freq_par_registre.items() if c[lex] > 0}
        total = sum(par_reg.values())
        if len(par_reg) >= 2 and total >= min_occurrences:
            sortie.append((lex, total, par_reg))
    sortie.sort(key=lambda t: -t[1])
    return sortie


# ---------------------------------------------------------------------------
# Tri / routage
# ---------------------------------------------------------------------------


def router_trait(taux_par_registre_valide):
    """Mouvement mécanique de présence, PAS le test de tri du protocole (voir cadrage).

    présent = taux > 0 dans un registre passé le seuil. stable sur ≥2 registres -> candidat Voix ;
    présent sur un seul -> Registre ; présent nulle part -> écarté.
    """
    presents = [r for r, t in taux_par_registre_valide.items() if t and t > 0]
    if len(presents) >= 2:
        return "candidat Voix", presents
    if len(presents) == 1:
        return "Registre (%s seulement)" % presents[0], presents
    return "écarté (absent des registres au-dessus du seuil)", []


# ---------------------------------------------------------------------------
# Rapport texte
# ---------------------------------------------------------------------------


def imprimer_rapport(config, registres, seuil_mots, args, sortie):
    valides = {r: i for r, i in registres.items() if not i["sous_seuil"]}
    sous_seuil = {r: i for r, i in registres.items() if i["sous_seuil"]}

    print("compte-traits.py %s — filtre de réfutation (--explique pour le rappel complet)"
          % VERSION, file=sortie)
    print("Langue : %s (config : %s)" % (config.get("langue", "?"), config["_origine"]),
          file=sortie)
    print("Corpus : %d registre(s), %d item(s), seuil %d mots\n"
          % (len(registres), sum(i["n_items"] for i in registres.values()), seuil_mots),
          file=sortie)

    print("REGISTRES", file=sortie)
    print("---------", file=sortie)
    for registre, info in sorted(registres.items()):
        etat = "SOUS LE SEUIL" if info["sous_seuil"] else "seuil atteint"
        dest = (" — %d destinataire(s) distinct(s)" % info["n_destinataires"]
                if info["n_destinataires"] else "")
        print("  %-24s %6d mots  (%2d item(s))  — %s%s"
              % (registre, info["total_mots"], info["n_items"], etat, dest), file=sortie)
    print("", file=sortie)

    if sous_seuil:
        print("Registres exclus de tout taux (sous %d mots) : %s."
              % (seuil_mots, ", ".join(sorted(sous_seuil))), file=sortie)
        print("Ces items comptent pour la lecture qualitative (étapes 5/6) et pour les postures "
              "(étape 9), jamais pour un taux : produire un taux sur ce volume serait trompeur, "
              "pas seulement imprécis.\n", file=sortie)

    if len(valides) < 2:
        print("Moins de deux registres au-dessus du seuil : aucun tri Voix/Registre n'est "
              "possible (il faut au moins deux registres pour réfuter quoi que ce soit). Les "
              "taux bruts ci-dessous restent imprimés à titre de lecture, sans colonne de "
              "routage.\n", file=sortie)

    if not valides:
        print("Aucun registre au-dessus du seuil : rien à calculer. Voir la note sur les modes "
              "dégradés dans protocole-extraction.md.", file=sortie)
        return

    # --- Traits de surface : mots-outils, connecteurs, intensité, typographie ---
    traits = {}
    for registre, info in valides.items():
        items_r, total = info["items"], info["total_mots"]
        t = {}
        t["mots-outils"] = taux_mots_outils(config, items_r, total)
        t["connecteur-contractif"] = taux_expressions(
            config["connecteurs"].get("contractifs", []), items_r, total)
        t["connecteur-expansif"] = taux_expressions(
            config["connecteurs"].get("expansifs", []), items_r, total)
        t["intensifieur-force-haute"] = taux_expressions(
            config["intensite"].get("force_haute", []), items_r, total)
        t["attenuateur-force-basse"] = taux_expressions(
            config["intensite"].get("force_basse", []), items_r, total)
        t.update(taux_typographiques(config, items_r, total))
        traits[registre] = t

    tous_traits = sorted({nom for t in traits.values() for nom in t})
    largeur_nom = max(len(n) for n in tous_traits) if tous_traits else 0
    largeur_reg = max((len(r) for r in valides), default=8)

    print("TRAITS DE SURFACE (taux pour 1000 mots ; %s)"
          % ("registres au-dessus du seuil seulement" if valides else "aucun registre valide"),
          file=sortie)
    print("-" * 78, file=sortie)
    entete = "%-*s" % (largeur_nom, "trait") + "".join(
        "  %*s" % (largeur_reg, r) for r in sorted(valides))
    print(entete + "   routage (mécanique, pas le test de tri)", file=sortie)
    for nom in tous_traits:
        par_reg = {r: traits[r].get(nom, 0.0) for r in valides}
        ligne = "%-*s" % (largeur_nom, nom) + "".join(
            "  %*.1f" % (largeur_reg, par_reg[r]) for r in sorted(valides))
        if len(valides) >= 2:
            label, _ = router_trait(par_reg)
        else:
            label = "(indisponible, <2 registres valides)"
        print(ligne + "   " + label, file=sortie)
    print("", file=sortie)
    print("Rappel : « candidat Voix » signifie seulement « pas écarté par ce filtre ». Chaque "
          "candidat doit encore passer le test de tri à trois filtres de modele-concepts.md avant "
          "d'entrer dans voix.md — le filtre de forme en particulier, pour les connecteurs et "
          "l'intensité, qui figurent aussi dans les listes de marqueurs de posture.\n", file=sortie)

    # --- Formes ambiguës ---
    if config["formes_ambigues"]:
        print("FORMES AMBIGUËS (comptage brut, JAMAIS routées — voir la note de chacune)",
              file=sortie)
        print("-" * 78, file=sortie)
        for nom, spec in config["formes_ambigues"].items():
            comptes = {r: compter_formes_ambigues(config, info["items"]).get(nom, 0)
                       for r, info in valides.items()}
            print("  %s : %s" % (nom, ", ".join(
                "%s=%d" % (r, comptes[r]) for r in sorted(comptes))), file=sortie)
            print("    → %s" % spec.get("note", ""), file=sortie)
        print("", file=sortie)

    # --- Substrat (diagnostic seulement) ---
    if config["paires_quasi_synonymes"]:
        print("SUBSTRAT — arbitrages grammaticaux (diagnostic seulement, jamais encodé : "
              "composantes-voix.md, fiche 1)", file=sortie)
        print("-" * 78, file=sortie)
        for registre, info in sorted(valides.items()):
            paires = compter_paires_substrat(config, info["items"])
            for p in paires:
                if not any(p["comptes"].values()):
                    continue
                detail = ", ".join("%s=%d" % (m, n) for m, n in p["comptes"].items())
                print("  %s — %s" % (registre, detail), file=sortie)
        print("", file=sortie)

    # --- Lexèmes récurrents ---
    lexemes = lexemes_recurrents(config, valides, args.min_occurrences_lexeme,
                                  args.min_longueur_lexeme)
    print("LEXÈMES RÉCURRENTS SUR ≥ 2 REGISTRES (signalés, PAS proposés comme candidats — Règle "
          "1 : le comptage réfute, il ne découvre pas)", file=sortie)
    print("-" * 78, file=sortie)
    if not lexemes:
        print("  Aucun, au seuil actuel (--min-occurrences-lexeme %d, --min-longueur-lexeme %d)."
              % (args.min_occurrences_lexeme, args.min_longueur_lexeme), file=sortie)
    else:
        for lex, total, par_reg in lexemes[:40]:
            detail = ", ".join("%s=%d" % (r, n) for r, n in sorted(par_reg.items()))
            print("  %-20s total=%-4d %s" % (lex, total, detail), file=sortie)
        if len(lexemes) > 40:
            print("  ... et %d de plus (voir --json pour la liste complète)."
                  % (len(lexemes) - 40), file=sortie)
    print("  Un lexème listé ici n'a de fonction que si l'étape 5 ou 6 lui en trouve une. Une "
          "ligne sans fonction identifiée reste une ligne de tableau.\n", file=sortie)

    # --- Empan ---
    print("EMPAN — distribution des longueurs (pas seulement la moyenne)", file=sortie)
    print("-" * 78, file=sortie)
    normes = args.normes_chargees or {}
    for registre, info in sorted(valides.items()):
        dist_phrases, dist_paras = empan_registre(info["items"])
        if dist_phrases:
            print("  %s — phrases : n=%d moyenne=%.1f médiane=%.1f p25=%.1f p75=%.1f max=%d mots"
                  % (registre, dist_phrases["n"], dist_phrases["moyenne"], dist_phrases["mediane"],
                     dist_phrases["p25"], dist_phrases["p75"], dist_phrases["max"]), file=sortie)
        if dist_paras:
            print("  %s — paragraphes : n=%d moyenne=%.1f médiane=%.1f p25=%.1f p75=%.1f max=%d "
                  "mots" % (registre, dist_paras["n"], dist_paras["moyenne"],
                            dist_paras["mediane"], dist_paras["p25"], dist_paras["p75"],
                            dist_paras["max"]), file=sortie)
        if registre in normes and dist_phrases:
            norme = normes[registre]
            delta = ((dist_phrases["moyenne"] - norme) / norme) * 100 if norme else None
            if delta is not None:
                print("    delta vs norme (%.1f mots/phrase) : %+.0f %%" % (norme, delta),
                      file=sortie)
        else:
            print("    delta vs norme : non calculable (aucune norme fournie pour « %s » via "
                  "--normes). Ne jamais écrire une longueur absolue comme trait de voix — règle "
                  "dure du protocole (composantes-voix.md, fiche 3)." % registre, file=sortie)
    print("", file=sortie)

    print(CADRAGE, file=sortie)


def rapport_json(config, registres, seuil_mots, args):
    valides = {r: i for r, i in registres.items() if not i["sous_seuil"]}
    out = {
        "version": VERSION,
        "langue": config.get("langue"),
        "config": config["_origine"],
        "seuil_mots": seuil_mots,
        "cadrage": CADRAGE,
        "registres": {},
        "traits": {},
        "formes_ambigues": {},
        "substrat": {},
        "lexemes_recurrents": [],
        "empan": {},
    }
    for registre, info in registres.items():
        out["registres"][registre] = {
            "total_mots": info["total_mots"],
            "n_items": info["n_items"],
            "n_destinataires": info["n_destinataires"],
            "sous_seuil": info["sous_seuil"],
        }
    for registre, info in valides.items():
        items_r, total = info["items"], info["total_mots"]
        t = {"mots-outils": taux_mots_outils(config, items_r, total)}
        t["connecteur-contractif"] = taux_expressions(
            config["connecteurs"].get("contractifs", []), items_r, total)
        t["connecteur-expansif"] = taux_expressions(
            config["connecteurs"].get("expansifs", []), items_r, total)
        t["intensifieur-force-haute"] = taux_expressions(
            config["intensite"].get("force_haute", []), items_r, total)
        t["attenuateur-force-basse"] = taux_expressions(
            config["intensite"].get("force_basse", []), items_r, total)
        t.update(taux_typographiques(config, items_r, total))
        out["traits"][registre] = t
        out["formes_ambigues"][registre] = compter_formes_ambigues(config, items_r)
        out["substrat"][registre] = compter_paires_substrat(config, items_r)
        dist_phrases, dist_paras = empan_registre(items_r)
        out["empan"][registre] = {"phrases": dist_phrases, "paragraphes": dist_paras}

    if len(valides) >= 2:
        routage = {}
        tous_traits = sorted({n for t in out["traits"].values() for n in t})
        for nom in tous_traits:
            par_reg = {r: out["traits"][r].get(nom, 0.0) for r in valides}
            label, presents = router_trait(par_reg)
            routage[nom] = {"label": label, "registres_presents": presents}
        out["routage"] = routage

    out["lexemes_recurrents"] = [
        {"lexeme": lex, "total": total, "par_registre": par_reg}
        for lex, total, par_reg in lexemes_recurrents(
            config, valides, args.min_occurrences_lexeme, args.min_longueur_lexeme)
    ]
    return out


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


EXPLIQUE = """compte-traits.py — rappel complet

CE QUE C'EST : un filtre de réfutation exécuté à l'Étape 3 du protocole d'extraction de
write-forge. Il réduit un corpus à un tableau trait × registre et rien de plus.

CE QUE ÇA REFUSE DE FAIRE, ET POURQUOI :
- Choisir un trait de voix. Une ligne « candidat Voix » veut dire « pas réfuté », pas « confirmé » :
  le test de tri à trois filtres (modele-concepts.md), l'entretien (étape 6) et l'écran de choix
  forcé aveugle (étape 7) restent devant.
- Désambiguïser « on », le conditionnel ou la forme interrogative en français : ce sont des comptes
  bruts, imprimés dans une section séparée, jamais routés (composantes-posture.md, section
  « Ambiguïté du français »).
- Comparer une longueur de phrase absolue à quoi que ce soit : sans --normes, le delta d'Empan n'est
  pas calculé, et un nombre de mots brut n'est jamais imprimé comme un trait de voix.
- Trancher registre × destinataire : les taux s'agrègent toujours au niveau du registre.

CE QUE ÇA FAIT :
- Normalise la typographie avant de compter des mots ou des phrases (pas avant de compter le style
  typographique lui-même, qui est le signal).
- Refuse un taux sous 1 500 mots par registre, avec un message explicite.
- Signale les lexèmes récurrents sur au moins deux registres sans les proposer comme candidats.
- Charge ses listes de marqueurs depuis un fichier externe par langue (langues/<code>.json), jamais
  codées en dur dans ce script.
"""


def construire_parseur():
    p = argparse.ArgumentParser(
        prog="compte-traits.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="FILTRE DE RÉFUTATION sur un corpus (Étape 3 de write-forge). Ne trouve la "
                    "voix de personne : écarte les traits crus personnels qui sont en fait des "
                    "traits de registre. Voir --explique pour le rappel complet.",
        epilog="Exemples :\n"
               "  compte-traits.py --corpus corpus/ --langue fr\n"
               "  compte-traits.py --manifest corpus-index.csv --langue fr --json\n"
               "  compte-traits.py --explique\n\n" + CADRAGE)
    p.add_argument("--corpus", metavar="DIR",
                   help="répertoire du corpus, un sous-répertoire par id de registre")
    p.add_argument("--manifest", metavar="FICHIER",
                   help="CSV ou JSON listant chemin/registre/destinataire (voir docstring)")
    p.add_argument("--langue", default="fr", metavar="CODE",
                   help="code de langue du corpus (défaut : fr). Charge langues/<code>.json à "
                        "côté de ce script.")
    p.add_argument("--config", metavar="FICHIER",
                   help="configuration de marqueurs à utiliser À LA PLACE de langues/<code>.json "
                        "(remplace, ne complète pas)")
    p.add_argument("--seuil-mots", type=int, default=SEUIL_MOTS_DEFAUT, metavar="N",
                   help="mots minimum par registre pour produire un taux (défaut : %d, voir "
                        "protocole-extraction.md)" % SEUIL_MOTS_DEFAUT)
    p.add_argument("--normes", metavar="FICHIER",
                   help="JSON {id_registre: mots_par_phrase_attendus} pour calculer un delta "
                        "d'Empan relatif ; sans ce fichier, le delta n'est pas calculé (jamais de "
                        "valeur absolue à la place, voir --explique)")
    p.add_argument("--min-occurrences-lexeme", type=int, default=3, metavar="N",
                   help="occurrences totales minimum pour signaler un lexème récurrent "
                        "(défaut : 3)")
    p.add_argument("--min-longueur-lexeme", type=int, default=4, metavar="N",
                   help="longueur minimum d'un lexème pour être éligible au signalement "
                        "(défaut : 4)")
    p.add_argument("--json", action="store_true", help="sortie machine sur stdout")
    p.add_argument("--explique", action="store_true",
                   help="imprime le rappel complet du cadrage et quitte")
    p.add_argument("--version", action="version", version="compte-traits.py " + VERSION)
    return p


def main(argv=None):
    args = construire_parseur().parse_args(argv)

    if args.explique:
        print(EXPLIQUE)
        return 0

    if not args.corpus and not args.manifest:
        print("Il faut --corpus DIR ou --manifest FICHIER. --help pour l'usage, --explique pour "
              "le rappel du cadrage.", file=sys.stderr)
        return 2
    if args.corpus and args.manifest:
        print("--corpus et --manifest sont exclusifs, choisir l'un des deux.", file=sys.stderr)
        return 2

    config = charger_config(args.langue, args.config)

    diagnostics = []
    if args.corpus:
        racine = Path(args.corpus).expanduser()
        if not racine.is_dir():
            print("Répertoire de corpus introuvable : %s" % racine, file=sys.stderr)
            return 2
        items_bruts = charger_corpus_repertoire(racine, diagnostics)
    else:
        chemin_manifeste = Path(args.manifest).expanduser()
        if not chemin_manifeste.is_file():
            print("Manifeste introuvable : %s" % chemin_manifeste, file=sys.stderr)
            return 2
        items_bruts = charger_corpus_manifeste(chemin_manifeste, diagnostics)

    if not items_bruts:
        print("Aucun item chargé. Rien à compter.", file=sys.stderr)
        for d in diagnostics:
            print("  " + d, file=sys.stderr)
        return 2

    args.normes_chargees = None
    if args.normes:
        chemin_normes = Path(args.normes).expanduser()
        try:
            args.normes_chargees = json.loads(chemin_normes.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print("Fichier de normes illisible (%s) : %s" % (chemin_normes, exc), file=sys.stderr)
            return 2

    items = analyser_corpus(items_bruts, config)
    registres = rapport_par_registre(items, config, args.seuil_mots)

    if diagnostics:
        for d in diagnostics:
            print("Diagnostic : " + d, file=sys.stderr)

    if args.json:
        print(json.dumps(rapport_json(config, registres, args.seuil_mots, args),
                         ensure_ascii=False, indent=2))
    else:
        imprimer_rapport(config, registres, args.seuil_mots, args, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
