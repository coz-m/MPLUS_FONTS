# -*- coding: utf-8 -*-
"""指定したグリフの中身を、全マスターで並べて表示する(何も書き換えない)。
使い方:  python3 sources/scripts/inspect_glyph.py asciitilde_greater less_asciitilde ...
         (マスターの場所を変える場合は、環境変数 MASTERS で指定)"""
import os
import sys
from pathlib import Path

from fontTools.pens.pointPen import AbstractPointPen
from fontTools.ufoLib import glifLib

sys.path.insert(0, str(Path(__file__).parent))
from lig_tools import default_layer_dir

MASTERS = Path(os.environ.get("MASTERS", "sources/MPLUScodeLIG/masters"))


class Rec(AbstractPointPen):
    def __init__(self):
        self.contours, self.components, self._c = [], [], None
    def beginPath(self, identifier=None, **kw): self._c = []
    def endPath(self): self.contours.append(self._c); self._c = None
    def addPoint(self, pt, segmentType=None, smooth=False, name=None, identifier=None, **kw):
        self._c.append((pt, segmentType, smooth))
    def addComponent(self, baseGlyph, transformation, identifier=None, **kw):
        self.components.append((baseGlyph, tuple(round(v, 3) for v in transformation)))


class _G:
    pass


def area(c):
    pts = [p for p, t, s in c if t is not None] or [p for p, t, s in c]
    a = 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        a += x1 * y2 - x2 * y1
    return a / 2


def show(gs, name, indent):
    if name not in gs:
        print("%s(このマスターにありません)" % indent)
        return None
    r = Rec()
    gs.readGlyph(name, _G(), r)
    for i, c in enumerate(r.contours):
        kinds = "".join({None: "o", "line": "L", "curve": "C", "qcurve": "Q", "move": "M"}.get(t, "?") for _, t, _ in c)
        print("%s線%d: 点%d個 向き%s 始点%s  %s" % (indent, i + 1, len(c), "+" if area(c) > 0 else "-", c[0][0], kinds))
    for base, tr in r.components:
        print("%s部品: %s  変形%s" % (indent, base, tr))
    return r


ufos = sorted(MASTERS.glob("*.ufo"))
for g in sys.argv[1:]:
    print("=" * 70, "\n" + g)
    for u in ufos:
        gs = glifLib.GlyphSet(str(default_layer_dir(u)), validateRead=False, validateWrite=False)
        print("-", u.name)
        r = show(gs, g, "    ")
