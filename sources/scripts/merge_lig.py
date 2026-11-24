# -*- coding: utf-8 -*-
"""Builds the sources of the two M PLUS Code LIG families from the LIG masters
(sources/MPLUScodeLIG/masters, made by `make prep_MPLUScodeLIG`).

  MPLUS1CodeLIG    width-50 masters only + Kana (MPLUS1) + Kanji (MPLUSKanji)  -> sources/MPLUS1CodeLIG/merged_ufo
  MPLUSCodeLIGLatin  all masters (width 50 and 60), renamed                    -> sources/MPLUSCodeLIGLatin/merged_ufo

Usage:
  python3 sources/scripts/merge_lig.py                     both families
  python3 sources/scripts/merge_lig.py MPLUS1CodeLIG       only that family
"""
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lig_tools as lt

FAMILY_JP = "M PLUS 1 Code LIG"            # family name of the Japanese version
FAMILY_LATIN = "M PLUS Code LIG Latin"     # family name of the Latin-only version
DEFAULT_STYLE = "Regular"                  # default of the weight axis of the variable fonts

SRC = Path("sources")
LIG = SRC / "MPLUScodeLIG"
KANA_LIST = SRC / "MPLUS1Code/kana_glyphs.txt"
ALL = ["MPLUS1CodeLIG", "MPLUSCodeLIGLatin"]

targets = sys.argv[1:] or ALL
bad = [t for t in targets if t not in ALL]
if bad:
    sys.exit("Unknown family: %s (available: %s)" % (", ".join(bad), ", ".join(ALL)))

designspaces = sorted((LIG / "masters").glob("*.designspace"))
if not designspaces:
    sys.exit("No designspace in %s. Run: make prep_MPLUScodeLIG" % (LIG / "masters"))
MASTERS_DS = designspaces[0]


def jp_ufo(style):
    return "%s-%s.ufo" % (FAMILY_JP.replace(" ", ""), style)


def latin_ufo(style, width):
    return "%s-%s%s.ufo" % (FAMILY_LATIN.replace(" ", ""), style, width)


# ---------------------------------------------------------------- 1. width / ligature patch of the masters
print("*** Patching the LIG masters (one-cell advances, ligature categories) ***")
for ufo in sorted((LIG / "masters").glob("*.ufo")):
    fea = (ufo / "features.fea").read_text(encoding="utf-8")
    calt, n = lt.extract_calt(fea)
    if calt is None:
        sys.exit("No 'feature calt' in %s" % (ufo / "features.fea"))
    if n > 1:
        print("  note: %s has %d calt blocks; only the first is kept" % (ufo.name, n))
    rep = lt.patch_ufo(ufo, calt)
    print("- %s  cell=%g  ligature glyphs=%d  advance changed=%d  missing=%s"
          % (ufo.name, rep["cell"], rep["targets"], len(rep["changes"]), rep["missing"] or "none"))
    err = lt.preflight_features(ufo)
    if err:
        sys.exit("Feature compile check failed for %s:\n%s" % (ufo.name, err))

# ---------------------------------------------------------------- 2. designspaces
narrow = None
_probe = lt.make_designspaces(MASTERS_DS, FAMILY_JP, FAMILY_LATIN, jp_ufo, latin_ufo, DEFAULT_STYLE)[2]
narrow = min(w for _, w, _ in _probe)
widest = max(w for _, w, _ in _probe)
src_ufo = {}                                  # (style, width) -> master UFO path
for style, w, fn in _probe:
    src_ufo[(style, w)] = LIG / "masters" / fn

# weight-dependent substitutions: features.fea (Glyphs' `#ifdef VARIABLE` blocks) -> designspace rules
_default_fea = (src_ufo[(DEFAULT_STYLE, narrow)] / "features.fea").read_text(encoding="utf-8")
try:
    _, FV_RULES = lt.split_feature_variations(_default_fea)
except ValueError as e:
    sys.exit("Cannot convert the feature variations in features.fea: %s" % e)
# the variable fonts take features.fea from ONE master, so every master must carry the same one
_clean = {k: lt.split_feature_variations((v / "features.fea").read_text(encoding="utf-8"))[0] for k, v in src_ufo.items()}
_ref = _clean[(DEFAULT_STYLE, widest)]
for k, t in sorted(_clean.items()):
    if t != _ref:
        print("  WARNING: features.fea of %s %s differs from the default master (Regular %s)" % (k[0], k[1], widest))
for r in FV_RULES:
    print("- feature variation -> designspace rule %s: %s, %d substitutions" % (r["name"], r["conditions"], len(r["subs"])))
jp_doc, lat_doc, info = lt.make_designspaces(MASTERS_DS, FAMILY_JP, FAMILY_LATIN, jp_ufo, latin_ufo, DEFAULT_STYLE, rules=FV_RULES)


def strip_feature_variations(font):
    font.features.text = lt.split_feature_variations(font.features.text)[0]

# ---------------------------------------------------------------- 3. UFO work (ufoLib2 / ufomerge)
import ufoLib2
from ufoLib2.objects import Kerning
from ufomerge import merge_ufos
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.basePen import BasePen


class QuadToCubicPen(BasePen):
    def __init__(self, target):
        super().__init__(None)
        self.t = target
    def _moveTo(self, p): self.t.moveTo(p)
    def _lineTo(self, p): self.t.lineTo(p)
    def _curveToOne(self, a, b, c): self.t.curveTo(a, b, c)
    def _closePath(self): self.t.closePath()
    def _endPath(self): self.t.endPath()


def quad_to_cubic(font):
    fixed = []
    for g in font:
        if any(pt.segmentType == "qcurve" for c in g.contours for pt in c.points):
            rec = RecordingPen()
            for c in g.contours:
                c.draw(rec)
            g.clearContours()
            rec.replay(QuadToCubicPen(g.getPen()))
            fixed.append(g.name)
    return fixed


def drop_colliding(cur, incoming):
    """Remove glyphs from `incoming` whose code point `cur` already has under another name (cur wins)."""
    cur_map = {}
    for g in cur:
        for u in g.unicodes:
            cur_map.setdefault(u, g.name)
    renamed = {}
    for g in list(incoming):
        hit = [cur_map[u] for u in g.unicodes if u in cur_map and cur_map[u] != g.name]
        if hit:
            renamed[g.name] = hit[0]
    for name in renamed:
        del incoming[name]
    for g in incoming:
        for c in g.components:
            if c.baseGlyph in renamed:
                c.baseGlyph = renamed[c.baseGlyph]
    incoming.glyphOrder = [n for n in incoming.glyphOrder if n in incoming]
    if renamed:
        print("    same code point under another name (kept the LIG one):",
              ", ".join("%s->%s" % kv for kv in sorted(renamed.items())))


def set_names(font, family, style=None):
    font.info.familyName = family
    font.info.styleMapFamilyName = family
    if style:
        font.info.styleName = style
    # let the compiler derive these from the family / style
    font.info.postscriptFontName = None
    font.info.openTypeNamePreferredFamilyName = None
    font.info.openTypeNamePreferredSubfamilyName = None
    font.info.openTypeNameUniqueID = None


def write_designspace(doc, folder, name):
    folder.mkdir(parents=True, exist_ok=True)
    doc.write(str(folder / (name + ".designspace")))


if "MPLUS1CodeLIG" in targets:
    print("*** *** *** *** Processing MPLUS1CodeLIG *** *** *** ***")
    OUT = SRC / "MPLUS1CodeLIG/merged_ufo"
    OUT.mkdir(parents=True, exist_ok=True)
    glyph_set = {l.strip() for l in KANA_LIST.read_text(encoding="utf-8").splitlines()
                 if l.strip() and not l.startswith("#")}
    for style, w, fn in info:
        if w != narrow:
            continue
        print("- %s -> %s" % (fn, jp_ufo(style)))
        kana = SRC / "MPLUS1/instances" / ("MPLUS1-%s.ufo" % style)
        kanji = SRC / "MPLUSKanji/instances" / ("M+1p-%s.ufo" % style)
        for p in (kana, kanji):
            if not p.exists():
                sys.exit("Missing %s. Run: make instancer" % p)
        with ufoLib2.Font.open(src_ufo[(style, w)]) as cur:
            with ufoLib2.Font.open(kana) as ext:
                drop_colliding(cur, ext)
                merge_ufos(cur, ext, glyphs=glyph_set, layout_handling="ignore", existing_handling="skip")
            cur.kerning = Kerning()
            with ufoLib2.Font.open(kanji) as ext:
                drop_colliding(cur, ext)
                merge_ufos(cur, ext, layout_handling="ignore", existing_handling="skip")
            fixed = quad_to_cubic(cur)
            if fixed:
                print("    quadratic -> cubic:", ", ".join(fixed))
            strip_feature_variations(cur)
            set_names(cur, FAMILY_JP, style)
            cur.save(OUT / jp_ufo(style), overwrite=True, validate=False)
    write_designspace(jp_doc, SRC / "MPLUS1CodeLIG/merged_ufo", "MPLUS1CodeLIG")

if "MPLUSCodeLIGLatin" in targets:
    print("*** *** *** *** Processing MPLUSCodeLIGLatin *** *** *** ***")
    OUT = SRC / "MPLUSCodeLIGLatin/merged_ufo"
    OUT.mkdir(parents=True, exist_ok=True)
    for style, w, fn in info:
        wtxt = str(int(round(w)))
        print("- %s -> %s" % (fn, latin_ufo(style, wtxt)))
        with ufoLib2.Font.open(src_ufo[(style, w)]) as cur:
            fixed = quad_to_cubic(cur)
            if fixed:
                print("    quadratic -> cubic:", ", ".join(fixed))
            strip_feature_variations(cur)
            is_default = (style == DEFAULT_STYLE and w == widest)
            set_names(cur, FAMILY_LATIN, DEFAULT_STYLE if is_default else None)
            if is_default:
                cur.info.styleMapStyleName = "regular"
            cur.save(OUT / latin_ufo(style, wtxt), overwrite=True, validate=False)
    write_designspace(lat_doc, SRC / "MPLUSCodeLIGLatin/merged_ufo", "MPLUSCodeLIGLatin")
print("done")
