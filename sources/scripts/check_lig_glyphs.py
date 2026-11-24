# -*- coding: utf-8 -*-
"""LIG のマスター(UFO)を調べて、ビルドを止める原因になるグリフを一覧にする(何も書き換えない)。
  1. 開いた線(閉じていないパス)  ->  "Unhandled open contour" の原因
  2. マスター間で形の構造が違うグリフ(点・線・部品の数や種類) ->  "incompatible glyphs" の原因
使い方(リポジトリの一番上のフォルダで):
    make prep_MPLUScodeLIG
    make check_LIG_glyphs
    venv/bin/python sources/scripts/check_lig_glyphs.py --after-filter    # fontmake の「開いた角を取り除く」処理をかけてから比べる
"""
import sys
from collections import defaultdict
from pathlib import Path

from fontTools.pens.pointPen import AbstractPointPen
from fontTools.ufoLib import glifLib

sys.path.insert(0, str(Path(__file__).parent))
from lig_tools import default_layer_dir

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
AFTER_FILTER = "--after-filter" in sys.argv
MASTERS = Path(ARGS[0] if ARGS else "sources/MPLUScodeLIG/masters")


class Collector(AbstractPointPen):
    def __init__(self):
        self.contours, self.components = [], []
        self._cur = None
    def beginPath(self, identifier=None, **kw):
        self._cur = []
    def endPath(self):
        self.contours.append(self._cur)
        self._cur = None
    def addPoint(self, pt, segmentType=None, smooth=False, name=None, identifier=None, **kw):
        self._cur.append(segmentType)
    def addComponent(self, baseGlyph, transformation, identifier=None, **kw):
        self.components.append(baseGlyph)


class _G:
    pass


def read_all(ufo):
    gs = glifLib.GlyphSet(str(default_layer_dir(ufo)), validateRead=False, validateWrite=False)
    out = {}
    for name in gs.keys():
        pen = Collector()
        gs.readGlyph(name, _G(), pen)
        out[name] = pen
    return out


def signature(pen):
    """What must be identical in every master: components, and per contour the kinds of its points."""
    conts = tuple(tuple("off" if t is None else t for t in c) for c in pen.contours)
    return (tuple(pen.components), conts)


def describe(pen):
    n_pts = [len(c) for c in pen.contours]
    return "%d contour(s) %s, %d component(s)" % (len(pen.contours), n_pts, len(pen.components))


ufos = sorted(MASTERS.glob("*.ufo"))
if not ufos:
    sys.exit("No masters in %s. Run: make prep_MPLUScodeLIG" % MASTERS)
data = {u.name: read_all(u) for u in ufos}

# ---- 1. open contours
print("=== 1. 開いた線(閉じていないパス)を持つグリフ ===")
open_hits = defaultdict(list)
for mname, glyphs in data.items():
    for g, pen in glyphs.items():
        for i, c in enumerate(pen.contours):
            if c and c[0] == "move":
                open_hits[g].append((mname, i, len(c)))
if not open_hits:
    print("なし")
for g in sorted(open_hits):
    print("%s" % g)
    for mname, i, n in open_hits[g]:
        print("    %-34s %d 番目の線(点 %d 個)が開いています" % (mname, i + 1, n))

# ---- 2. compatibility
print("\n=== 2. マスター間で構造が違うグリフ ===")
all_names = sorted(set().union(*[set(d) for d in data.values()]))
bad = 0
for g in all_names:
    sigs = {m: signature(data[m][g]) for m in data if g in data[m]}
    missing = [m for m in data if g not in data[m]]
    if missing:
        print("%s: 次のマスターにありません: %s" % (g, ", ".join(missing)))
        bad += 1
        continue
    if len(set(sigs.values())) > 1:
        bad += 1
        groups = defaultdict(list)
        for m, s in sigs.items():
            groups[s].append(m)
        print(g)
        for s, ms in groups.items():
            print("    %-60s %s" % (", ".join(sorted(ms)), describe(data[ms[0]][g])))
print("\n違いのあるグリフ: %d 個" % bad if bad else "\nなし")
print("開いた線のあるグリフ: %d 個" % len(open_hits))


# ---- 3. the same comparison AFTER fontmake's EraseOpenCornersFilter (it works on each master separately)
if AFTER_FILTER:
    print("\n=== 3. 「開いた角を取り除く」処理(EraseOpenCornersFilter)のあとで、構造が違うグリフ ===")
    try:
        import importlib
        import pkgutil
        import ufoLib2
        import ufo2ft.filters as _F
    except ImportError as e:
        sys.exit("ufo2ft / ufoLib2 が使えません: %s (venv の python で実行してください)" % e)
    EraseOpenCornersFilter = getattr(_F, "EraseOpenCornersFilter", None)
    if EraseOpenCornersFilter is None:                      # the module name differs between ufo2ft versions
        for _m in pkgutil.iter_modules(_F.__path__):
            if _m.name.startswith("_"):          # skip __main__ etc. (importing it would run a command line tool)
                continue
            _mod = importlib.import_module("ufo2ft.filters." + _m.name)
            if hasattr(_mod, "EraseOpenCornersFilter"):
                EraseOpenCornersFilter = _mod.EraseOpenCornersFilter
                break
    if EraseOpenCornersFilter is None:
        try:
            from glyphsLib.filters.eraseOpenCorners import EraseOpenCornersFilter   # some versions ship it with glyphsLib
        except ImportError:
            sys.exit("EraseOpenCornersFilter が見つかりません。次の結果を教えてください:\n"
                     "  venv/bin/python -c \"import ufo2ft, pkgutil; print(ufo2ft.__version__, [m.name for m in pkgutil.iter_modules(__import__('ufo2ft.filters', fromlist=['x']).__path__)])\"")
    after = {}
    for u in ufos:
        font = ufoLib2.Font.open(u)
        changed = EraseOpenCornersFilter()(font) or []
        sig = {}
        for g in font:
            sig[g.name] = (tuple(c.baseGlyph for c in g.components),
                           tuple(tuple("off" if p.segmentType is None else p.segmentType for p in c.points)
                                 for c in g.contours))
        after[u.name] = (sig, set(changed))
    bad2 = 0
    for g in sorted(set().union(*[set(v[0]) for v in after.values()])):
        sigs = {m: v[0].get(g) for m, v in after.items()}
        if len(set(sigs.values())) > 1:
            bad2 += 1
            groups = defaultdict(list)
            for m, s_ in sigs.items():
                groups[s_].append(m)
            print(g)
            for s_, ms in groups.items():
                n = sum(len(c) for c in s_[1]) if s_ else 0
                print("    %-60s 点の合計 %d" % (", ".join(sorted(ms)), n))
    print("\n処理のあとで違いのあるグリフ: %d 個" % bad2)
    touched = sorted(set().union(*[v[1] for v in after.values()]))
    print("この処理で形が変わったグリフ(どれかのマスターで): %d 個" % len(touched))
    for g in touched[:40]:
        print("   ", g, "<- 変わったマスター:", ", ".join(m for m, v in after.items() if g in v[1]))
