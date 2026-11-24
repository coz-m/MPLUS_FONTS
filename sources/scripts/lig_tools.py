# -*- coding: utf-8 -*-
"""lig_tools.py - helpers for building the M PLUS Code LIG families (fontTools only, no ufoLib2).

* patch_ufo(): the Glyphs-free version of the macro mll_v61.py (every ligature glyph gets a ONE-cell advance,
  ligatures are marked in GDEF). Applied to the master UFOs that `fontmake` made from the .glyphs file.
* extract_calt(): reads the calt code out of the UFO's features.fea.
* make_designspaces(): writes the designspace files for MPLUS1CodeLIG (width 50 only, no width axis)
  and MPLUSCodeLIGLatin (all masters).
"""
import plistlib
import re
from pathlib import Path

from fontTools.designspaceLib import DesignSpaceDocument, RuleDescriptor
from fontTools.pens.recordingPen import RecordingPointPen
from fontTools.ufoLib import glifLib

LINEAR_SUFFIX = ".linear"
ZERO_WIDTH_GLYPHS = ("LIG.null",)      # empty glyphs with ZERO advance
LEGACY_GG_GLYPHS = ("greater_greater", "less_less")


def zero_glyph_from_calt(code, default="LIG.null"):
    """The zero-width glyph is named in the calt header written by make_calt.py."""
    hit = re.search(r"zero-width glyph ([A-Za-z0-9_.\-]+)\)", code)
    return hit.group(1) if hit else default


def targets_from_calt(code):
    """Glyph names that calt substitutes TO (`by NAME;`). Comments are ignored."""
    names = set()
    for line in code.splitlines():
        line = line.split("#")[0]
        for m in re.finditer(r"\bby\s+([A-Za-z0-9_.\-]+)\s*;", line):
            names.add(m.group(1))
    return names


def derive_targets(code, glyph_names):
    """calt targets + every *.linear glyph + derivatives such as <target>.bold."""
    names = targets_from_calt(code)
    names |= {g for g in glyph_names if g.endswith(LINEAR_SUFFIX)}
    names |= {g for g in glyph_names if g.rsplit(".", 1)[0] in names}
    return names


def replace_calt(features_text, calt_code):
    """Replace the body of `feature calt {...} calt;` (or append the feature)."""
    block = "feature calt {\n%s\n} calt;" % calt_code.strip("\n")
    pattern = re.compile(r"feature\s+calt\s*\{.*?\}\s*calt\s*;", re.S)
    n = len(pattern.findall(features_text))
    if n == 0:
        return features_text.rstrip("\n") + "\n\n" + block + "\n", 0
    first = True

    def repl(_m):
        nonlocal first
        if first:
            first = False
            return block
        return ""          # a second calt block would double the lookups: drop it

    return pattern.sub(repl, features_text), n


def default_layer_dir(ufo_path):
    """Directory (inside the UFO) of the default layer."""
    lc = Path(ufo_path) / "layercontents.plist"
    if lc.exists():
        with open(lc, "rb") as f:
            for name, directory in plistlib.load(f):
                if name == "public.default":
                    return Path(ufo_path) / directory
    return Path(ufo_path) / "glyphs"


class _Glyph:
    """Plain holder: glifLib sets width/height/unicodes/lib/anchors/... on it."""


# ----------------------------------------------------------------------------- UFO patching
def patch_ufo(ufo_path, calt_code, legacy_gg=False, set_category=True, zero_glyphs=ZERO_WIDTH_GLYPHS):
    """Patch one master UFO in place. Returns a report dict."""
    ufo = Path(ufo_path)
    gdir = default_layer_dir(ufo)
    gs = glifLib.GlyphSet(str(gdir), validateRead=False, validateWrite=False)
    names = set(gs.keys())
    if "space" not in names:
        raise SystemExit("ERROR: %s has no 'space' glyph (needed for the cell width)" % ufo.name)
    probe = _Glyph()
    gs.readGlyph("space", probe, RecordingPointPen())
    cell = float(probe.width)

    targets = derive_targets(calt_code, names)
    missing = sorted(t for t in targets_from_calt(calt_code) if t not in names)
    changes, kept = [], 0
    for name in sorted(targets & names):
        g, pen = _Glyph(), RecordingPointPen()
        gs.readGlyph(name, g, pen)
        want = 0.0 if name in zero_glyphs else cell
        if legacy_gg and name in LEGACY_GG_GLYPHS and cell >= 600.0:
            want = cell - 100.0
        cur = float(getattr(g, "width", 0) or 0)      # a glif without <advance> has width 0
        if abs(cur - want) > 0.001:
            changes.append((name, cur, want))
            g.width = want
            gs.writeGlyph(name, g, drawPointsFunc=pen.replay)
        else:
            kept += 1
    if changes:
        gs.writeContents()

    # other layers (brace / intermediate masters) are left alone, but reported
    other = []
    layer_names = []
    lc = ufo / "layercontents.plist"
    if lc.exists():
        with open(lc, "rb") as f:
            layer_names = [(n, d) for n, d in plistlib.load(f) if n != "public.default"]
    for lname, ldir in layer_names:
        try:
            ogs = glifLib.GlyphSet(str(ufo / ldir), validateRead=False, validateWrite=False)
            hit = sorted(set(ogs.keys()) & targets)
            if hit:
                other.append((lname, hit))
        except Exception:
            pass

    # GDEF category
    if set_category:
        lib_path = ufo / "lib.plist"
        lib = {}
        if lib_path.exists():
            with open(lib_path, "rb") as f:
                lib = plistlib.load(f)
        cats = dict(lib.get("public.openTypeCategories", {}))
        for name in targets & names:
            if name != "LIG.space" and name not in zero_glyphs:
                cats[name] = "ligature"
        lib["public.openTypeCategories"] = cats
        with open(lib_path, "wb") as f:
            plistlib.dump(lib, f)

    # features
    fea_path = ufo / "features.fea"
    text = fea_path.read_text(encoding="utf-8") if fea_path.exists() else ""
    new_text, n_old = replace_calt(text, calt_code)
    fea_path.write_text(new_text, encoding="utf-8")

    return dict(ufo=ufo.name, cell=cell, targets=len(targets & names), changes=changes, kept=kept,
                missing=missing, other_layers=other, calt_blocks_replaced=n_old)


def preflight_features(ufo_path):
    """Compile the patched features with feaLib against the UFO's glyph set (fast sanity check)."""
    from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
    from fontTools.feaLib.error import FeatureLibError
    from fontTools.ttLib import TTFont

    gs = glifLib.GlyphSet(str(default_layer_dir(ufo_path)), validateRead=False, validateWrite=False)
    order = [".notdef"] + sorted(n for n in gs.keys() if n != ".notdef")
    font = TTFont()
    font.setGlyphOrder(order)
    text = (Path(ufo_path) / "features.fea").read_text(encoding="utf-8")
    # feature variations (conditionset / variation blocks) need an fvar table, which this sanity check does not
    # have: leave them out of the check only (the real features.fea is not changed)
    text = re.sub(r"conditionset\s+[\w.\-]+\s*\{.*?\}\s*[\w.\-]+\s*;", "", text, flags=re.S)
    text = re.sub(r"variation\s+\w+\s+[\w.\-]+\s*\{.*?\}\s*\w+\s*;", "", text, flags=re.S)
    try:
        addOpenTypeFeaturesFromString(font, text)
    except FeatureLibError as e:
        return str(e)
    return None


# ----------------------------------------------------------------------------- calt
def extract_calt(features_text):
    """Return (body of the first `feature calt {...} calt;` block, number of calt blocks)."""
    blocks = re.findall(r"feature\s+calt\s*\{(.*?)\}\s*calt\s*;", features_text, re.S)
    return (blocks[0] if blocks else None), len(blocks)


def split_feature_variations(fea_text):
    """
    Glyphs writes weight-dependent substitutions into features.fea as `conditionset` / `variation` blocks,
    wrapped in `#ifdef VARIABLE` (a Glyphs-only switch: for fontmake it is just a comment). Static fonts cannot
    contain feature variations. So: take the blocks out of the features and return them as designspace rules.

    Returns (clean_text, rules); rules = [{"name": str, "conditions": [(axisTag, min, max)], "subs": [(a, b)]}]
    with min / max in USER coordinates (as written in the .fea). Raises ValueError for anything it cannot convert.
    """
    text = re.sub(r"^[ \t]*#(?:ifdef|ifndef|else|endif)\b.*$", "", fea_text, flags=re.M)
    csets = {}
    for m in re.finditer(r"conditionset\s+([\w.\-]+)\s*\{(.*?)\}\s*\1\s*;", text, re.S):
        conds = re.findall(r"\b(\w{4})\s+(-?[\d.]+)\s+(-?[\d.]+)\s*;", m.group(2))
        if not conds:
            raise ValueError("cannot read conditionset %s" % m.group(1))
        csets[m.group(1)] = [(t, float(lo), float(hi)) for t, lo, hi in conds]
    subs = {}
    for m in re.finditer(r"variation\s+(\w+)\s+([\w.\-]+)\s*\{(.*?)\}\s*\1\s*;", text, re.S):
        tag, cs, body = m.groups()
        if tag != "rvrn":
            raise ValueError("variation block for feature %r is not supported" % tag)
        if cs not in csets:
            raise ValueError("variation uses unknown conditionset %s" % cs)
        pairs = re.findall(r"\bsub\s+([\w.\-]+)\s+by\s+([\w.\-]+)\s*;", body)
        rest = re.sub(r"\bsub\s+[\w.\-]+\s+by\s+[\w.\-]+\s*;", "", body)
        rest = re.sub(r"#.*", "", rest).strip()
        if rest:
            raise ValueError("variation %s contains statements other than 'sub X by Y;': %r" % (cs, rest[:60]))
        subs.setdefault(cs, []).extend(pairs)
    clean = re.sub(r"conditionset\s+([\w.\-]+)\s*\{.*?\}\s*\1\s*;", "", text, flags=re.S)
    clean = re.sub(r"variation\s+(\w+)\s+([\w.\-]+)\s*\{.*?\}\s*\1\s*;", "", clean, flags=re.S)
    rules = [dict(name=cs, conditions=csets[cs], subs=subs[cs]) for cs in csets if subs.get(cs)]
    return clean, rules


# ----------------------------------------------------------------------------- designspace
def _nospace(s):
    return s.replace(" ", "")


def _strip_width(style):
    """'Thin 50' -> 'Thin'"""
    return re.sub(r"\s*\d+$", "", style).strip()


def _width_axis(ds):
    for a in ds.axes:
        if a.tag == "wdth":
            return a
    others = [a for a in ds.axes if a.tag != "wght"]
    if not others:
        raise ValueError("no width axis found")
    return others[0]


def _weight_axis(ds):
    for a in ds.axes:
        if a.tag == "wght":
            return a
    raise ValueError("no weight axis found")


def _stylemap(family, style):
    """(styleMapFamilyName, styleMapStyleName) following the existing MPLUS1Code designspace."""
    if style == "Bold":
        return family, "bold"
    if style == "Regular":
        return family, "regular"
    return "%s %s" % (family, style), "regular"


def _set_copy_flags(sources, default_src):
    for s in sources:
        on = s is default_src
        s.copyLib = s.copyInfo = s.copyGroups = s.copyFeatures = on


def add_rules(doc, rules):
    """Add rules (conditions in USER coordinates) to a designspace; conditions are converted to design coordinates."""
    by_tag = {a.tag: a for a in doc.axes}
    for r in rules:
        conds = []
        for tag, lo, hi in r["conditions"]:
            ax = by_tag.get(tag)
            if ax is None:
                continue                      # axis not in this designspace (e.g. width in the Japanese version)
            conds.append(dict(name=ax.name, minimum=float(ax.map_forward(lo)), maximum=float(ax.map_forward(hi))))
        if not conds:
            continue
        rd = RuleDescriptor()
        rd.name = r["name"]
        rd.conditionSets = [conds]
        rd.subs = list(r["subs"])
        doc.addRule(rd)


def make_designspaces(masters_ds_path, jp_family, latin_family, jp_ufo, latin_ufo, default_style="Regular", rules=()):
    """
    Build the two designspaces from the one glyphsLib wrote for the LIG source.
    jp_ufo(style)            -> UFO file name of a MPLUS1CodeLIG master
    latin_ufo(style, width)  -> UFO file name of a MPLUSCodeLIGLatin master
    Returns (jp_doc, latin_doc, info) where info lists the masters: [(style, width, source file name)].
    The weight axis default is moved to `default_style` (Regular). Japanese: narrow only. Latin: width axis default = the widest (60).
    """
    jp = DesignSpaceDocument.fromfile(str(masters_ds_path))
    lat = DesignSpaceDocument.fromfile(str(masters_ds_path))
    wax, dax = _weight_axis(jp), _width_axis(jp)
    masters = []
    for s in jp.sources:
        if getattr(s, "layerName", None):
            continue
        masters.append((_strip_width(s.styleName or ""), float(s.location[dax.name]), s))
    if not masters:
        raise ValueError("designspace has no masters")
    narrow = min(w for _, w, _ in masters)
    widest = max(w for _, w, _ in masters)      # the Latin version defaults to the widest width
    # remember the ORIGINAL file names now (the descriptors are renamed below)
    info = [(style, w, Path(s.filename or "").name) for style, w, s in masters]

    # which design coordinate is the default weight?
    default_w = None
    for style, w, s in masters:
        if style == default_style and w == narrow:
            default_w = float(s.location[wax.name])
    if default_w is None:
        raise ValueError("no master named %r at the narrow width" % default_style)

    # ---- MPLUS1CodeLIG: narrow masters only, no width axis
    jp_sources, jp_default = [], None
    for style, w, s in masters:
        if w != narrow:
            continue
        s.path = None
        s.filename = jp_ufo(style)
        s.name = "%s %s" % (jp_family, style)
        s.familyName, s.styleName = jp_family, style
        s.location = {wax.name: s.location[wax.name]}
        jp_sources.append(s)
        if style == default_style:
            jp_default = s
    _set_copy_flags(jp_sources, jp_default)
    jp.sources = jp_sources
    jp.axes = [a for a in jp.axes if a.name != dax.name]
    _weight_axis(jp).default = float(_weight_axis(jp).map_backward(default_w))
    jp_instances = []
    for i in jp.instances:
        if float(i.location[dax.name]) != narrow:
            continue
        style = _strip_width(i.styleName or "")
        i.path = None
        i.name = "%s %s" % (jp_family, style)
        i.familyName, i.styleName = jp_family, style
        i.filename = "instance_ufos/%s-%s.ufo" % (_nospace(jp_family), style)
        i.styleMapFamilyName, i.styleMapStyleName = _stylemap(jp_family, style)
        i.location = {wax.name: i.location[wax.name]}
        jp_instances.append(i)
    jp.instances = jp_instances

    # ---- MPLUSCodeLIGLatin: every master, both axes
    lat_masters, lat_default = [], None
    for s in lat.sources:
        if getattr(s, "layerName", None):
            continue
        style, w = _strip_width(s.styleName or ""), float(s.location[dax.name])
        wtxt = str(int(round(w)))
        s.path = None
        s.filename = latin_ufo(style, wtxt)
        s.name = "%s %s %s" % (latin_family, style, wtxt)
        s.familyName, s.styleName = latin_family, "%s %s" % (style, wtxt)
        lat_masters.append(s)
        if style == default_style and w == widest:
            lat_default = s
            s.styleName = style                  # the variable font is named after the default master
    _set_copy_flags(lat_masters, lat_default)
    lat.sources = lat_masters
    _weight_axis(lat).default = float(_weight_axis(lat).map_backward(default_w))
    _width_axis(lat).default = float(_width_axis(lat).map_backward(widest))
    for i in lat.instances:
        style, wtxt = _strip_width(i.styleName or ""), str(int(round(float(i.location[dax.name]))))
        fam = "%s %s" % (latin_family, wtxt)
        i.path = None
        i.name = "%s %s" % (fam, style)
        i.familyName, i.styleName = fam, style
        i.filename = "instance_ufos/%s%s-%s.ufo" % (_nospace(latin_family), wtxt, style)
        i.styleMapFamilyName, i.styleMapStyleName = _stylemap(fam, style)
    add_rules(jp, rules)
    add_rules(lat, rules)
    return jp, lat, info
