# -*- coding: utf-8 -*-
"""
mplus_helpers.py - small helpers for merging the shared Kanji into MPLUS 3.

Only fontTools is needed (no ufoLib2 / ufomerge), so everything here can be tested on its own:

    python3 sources/scripts/check_mplus3.py        # prints the merge plan and warnings
"""
from pathlib import Path

from fontTools.designspaceLib import DesignSpaceDocument

WEIGHT_TOLERANCE = 0.5      # user-space units (weight 400 vs 400.2 is the same master)


def style_of_ufo(ufo_name):
    """'MPLUS3-ExtraLight.ufo' -> 'ExtraLight' (the part after the last hyphen)."""
    return Path(str(ufo_name)).stem.rsplit("-", 1)[-1]


def weight_axis(ds):
    """The weight axis of a designspace: the axis with tag 'wght', otherwise the first axis."""
    for ax in ds.axes:
        if ax.tag == "wght":
            return ax
    if not ds.axes:
        raise ValueError("designspace has no axes")
    return ds.axes[0]


def user_weight(ds, source):
    """Weight of a master in user space (the value that ends up as OS/2 usWeightClass)."""
    ax = weight_axis(ds)
    return float(ax.map_backward(source.location[ax.name]))


def masters(ds):
    """[(ufo file name, source)] of the real masters (sources on an extra layer are skipped)."""
    seen, out = set(), []
    for s in ds.sources:
        if getattr(s, "layerName", None):
            continue                                   # brace / intermediate layer
        name = Path(s.filename or s.path or "").name
        if name and name not in seen:
            seen.add(name)
            out.append((name, s))
    return out


def plan_kanji_sources(family_ds_path, kanji_ds_path, tol=WEIGHT_TOLERANCE):
    """
    For every master of the family decide which Kanji to merge into it.

    mode "direct"       the Kanji font has a master with the same style name at the same weight
                        (this is how MPLUS 1 and MPLUS 2 are built)
    mode "interpolate"  no such master: the Kanji is interpolated at the weight of the family master
    mode "out_of_range" the family master is outside the weight range of the Kanji font
    """
    fam = DesignSpaceDocument.fromfile(str(family_ds_path))
    kan = DesignSpaceDocument.fromfile(str(kanji_ds_path))
    kax = weight_axis(kan)
    kmasters = {style_of_ufo(n): (n, user_weight(kan, s)) for n, s in masters(kan)}
    kmin, kmax = float(kax.minimum), float(kax.maximum)

    plan = []
    for name, src in masters(fam):
        style, uw = style_of_ufo(name), user_weight(fam, src)
        item = dict(ufo=name, style=style, user_weight=uw, mode=None, kanji_master=None, kanji_location=None)
        hit = kmasters.get(style)
        if hit and abs(hit[1] - uw) <= tol:
            item.update(mode="direct", kanji_master=hit[0])
        elif uw < kmin - tol or uw > kmax + tol:
            item.update(mode="out_of_range")
        else:
            loc = {}
            for ax in kan.axes:
                user = uw if ax.name == kax.name else float(ax.default)
                loc[ax.name] = float(ax.map_forward(user))
            item.update(mode="interpolate", kanji_location=loc)
        plan.append(item)
    return plan


def describe_designspace(path):
    """Short facts about a designspace file (for the check report)."""
    ds = DesignSpaceDocument.fromfile(str(path))
    return dict(
        axes=[(a.name, a.tag, a.minimum, a.default, a.maximum, bool(a.map)) for a in ds.axes],
        masters=[(n, style_of_ufo(n), user_weight(ds, s)) for n, s in masters(ds)],
        instances=len(ds.instances), rules=len(ds.rules),
    )


def check_features(glyph_names, features_text):
    """Compile `features_text` against a glyph set with feaLib. Returns None if it is fine, else the message."""
    from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
    from fontTools.ttLib import TTFont
    font = TTFont()
    font.setGlyphOrder([".notdef"] + sorted(n for n in glyph_names if n != ".notdef"))
    try:
        addOpenTypeFeaturesFromString(font, features_text)
    except Exception as e:                       # FeatureLibError and friends
        return str(e)
    return None


def ufo_glyph_names(ufo_path):
    """Glyph names of the default layer of a UFO (reads only contents.plist)."""
    import plistlib
    ufo = Path(ufo_path)
    layer_dir = ufo / "glyphs"
    lc = ufo / "layercontents.plist"
    if lc.exists():
        with open(lc, "rb") as f:
            for name, d in plistlib.load(f):
                if name == "public.default":
                    layer_dir = ufo / d
    with open(layer_dir / "contents.plist", "rb") as f:
        return set(plistlib.load(f))
