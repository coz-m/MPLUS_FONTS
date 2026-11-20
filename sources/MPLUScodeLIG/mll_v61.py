# MenuTitle: Mono Ligature Lock v61 (freeze -> resize -> restore)
# -*- coding: utf-8 -*-
from __future__ import print_function, division, unicode_literals
import re
import GlyphsApp

# ---------------------------------------------------------------
# 何をするか
#  設計時は N マス幅で作ってある合字グリフを、書き出し用に「1マス幅 + LIG.space」へ直す。
#  v59 は「グリフを1つずつ 幅変更→次へ」だったため、鏡像コンポーネント（<: >: :| -| +> <=< など）は、
#  親グリフ(:> |: など)の幅が縮んだ時点で自動整列が走り、親の幅ぶん左にズレていた。
#  v61 は 3 段階に分ける:
#    pass1: 対象と、対象を使う合成グリフの自動整列を全部止め、アウトライン位置(xMin)を記録
#    pass2: メトリクスキー除去 + 幅を1マスに固定
#    pass3: xMin が動いたレイヤーを元の位置へ戻す（動いた量をログに出す）
# ---------------------------------------------------------------
AUDIT_ONLY = False
SET_LIG_CATEGORY = True
CLEAR_GLYPH_LEVEL_KEYS = True     # グリフ単位の L/R/W キーも外す（レイヤーのキーだけ外すとグリフ側が復活する）
RESTORE_OUTLINE = True            # pass3 を実行
LEGACY_GG_ADJUST = False
LEGACY_GG_GLYPHS = ("greater_greater", "less_less")
LEGACY_GG_MIN_WIDTH = 600.0
EXTRA_GLYPHS = []
ZERO_WIDTH_GLYPHS = ("LIG.null",)   # empty glyphs with ZERO advance (compact ligatures such as mpluscodelig)
FALLBACK_SUFFIX = ".linear"

font = Glyphs.font


def zero_glyph_from_calt(code, default="LIG.null"):
    """The zero-width glyph is named in the calt header written by make_calt.py."""
    hit = re.search(r"zero-width glyph ([A-Za-z0-9_.\-]+)\)", code)
    return hit.group(1) if hit else default


def targets_from_calt(f):
    names = set()
    try:
        feat = f.features["calt"]
    except Exception:
        feat = None
    code = feat.code if feat is not None else ""
    for line in code.splitlines():
        line = line.split("#")[0]
        for m in re.finditer(r"\bby\s+([A-Za-z0-9_.\-]+)\s*;", line):
            names.add(m.group(1))
    return names


def master_layers(glyph):
    return [l for l in glyph.layers if l.isMasterLayer]


def freeze_alignment(layer):
    for comp in layer.components:
        try:
            comp.automaticAlignment = False
        except Exception:
            try:
                comp.setDisableAlignment_(True)
            except Exception:
                pass


def xmin(layer):
    b = layer.bounds
    if b is None:
        return None
    return float(b.origin.x)


def main():
    if font is None:
        print("Error: No font open.")
        return
    space = font.glyphs["space"]
    if space is None:
        print("Error: 'space' glyph not found.")
        return
    cell = {}
    for m in font.masters:
        cell[m.id] = float(space.layers[m.id].width)
    print("Cell width per master:", ", ".join("%s=%g" % (m.name, cell[m.id]) for m in font.masters))

    try:
        calt_code = font.features["calt"].code
    except Exception:
        calt_code = ""
    zero = set(ZERO_WIDTH_GLYPHS) | {zero_glyph_from_calt(calt_code)}
    print("zero-advance glyphs:", ", ".join(sorted(zero)))
    names = targets_from_calt(font)
    names.update(EXTRA_GLYPHS)
    for g in font.glyphs:
        if g.name.endswith(FALLBACK_SUFFIX):
            names.add(g.name)
    for g in font.glyphs:
        if g.name.rsplit(".", 1)[0] in names:
            names.add(g.name)
    missing = sorted(n for n in names if n not in font.glyphs)
    for n in missing:
        print("WARNING: calt が参照するグリフがフォントに無い:", n)
    names = set(n for n in names if n in font.glyphs)
    if not names:
        print("No target glyphs found.")
        return

    # 対象を部品として使っている合成グリフ（幅は変えないが、自動整列で動かされる側）
    dependents = set()
    for g in font.glyphs:
        if g.name in names:
            continue
        for l in master_layers(g):
            if any(c.componentName in names for c in l.components):
                dependents.add(g.name)
                break

    freeze_set = sorted(names | dependents)
    snapshot = {}
    fixed_w = 0
    restored = 0
    still_off = []

    font.disableUpdateInterface()
    try:
        # ---- pass1: 位置を記録して整列を止める ----
        for name in freeze_set:
            g = font.glyphs[name]
            for l in master_layers(g):
                snapshot[(name, l.layerId)] = xmin(l)
                if not AUDIT_ONLY:
                    freeze_alignment(l)
        print("pass1: frozen %d glyphs (targets=%d, dependents=%d)" % (len(freeze_set), len(names), len(dependents)))

        # ---- pass2: キー除去 + 幅固定 ----
        for name in sorted(names):
            g = font.glyphs[name]
            if not AUDIT_ONLY:
                g.beginUndo()
                if SET_LIG_CATEGORY and name != "LIG.space" and name not in zero:
                    g.category = "Ligature"
                    g.subCategory = "Ligature"
                if CLEAR_GLYPH_LEVEL_KEYS:
                    for attr in ("leftMetricsKey", "rightMetricsKey", "widthMetricsKey"):
                        try:
                            setattr(g, attr, None)
                        except Exception:
                            pass
            for l in g.layers:
                if not l.isMasterLayer:
                    if l.isSpecialLayer:
                        print("NOTE: special layer をスキップ:", name, "[%s]" % l.name)
                    continue
                target = 0.0 if name in zero else cell[l.associatedMasterId]
                if LEGACY_GG_ADJUST and name in LEGACY_GG_GLYPHS and target >= LEGACY_GG_MIN_WIDTH:
                    target -= 100.0
                if abs(float(l.width) - target) > 0.001:
                    fixed_w += 1
                    print("%s %s [%s]: width %g -> %g" % ("AUDIT" if AUDIT_ONLY else "FIX", name, l.name, l.width, target))
                if AUDIT_ONLY:
                    continue
                l.leftMetricsKey = None
                l.rightMetricsKey = None
                l.widthMetricsKey = None
                l.width = target
            if not AUDIT_ONLY:
                g.endUndo()

        # ---- pass3: 動いたアウトラインを元の位置へ ----
        if RESTORE_OUTLINE and not AUDIT_ONLY:
            for name in freeze_set:
                g = font.glyphs[name]
                for l in master_layers(g):
                    old = snapshot.get((name, l.layerId))
                    new = xmin(l)
                    if old is None or new is None:
                        continue
                    dx = old - new
                    if abs(dx) > 0.01:
                        l.applyTransform([1, 0, 0, 1, dx, 0])
                        after = xmin(l)
                        restored += 1
                        flag = "" if (after is not None and abs(after - old) <= 0.5) else "  <-- まだズレている"
                        if flag:
                            still_off.append((name, l.name))
                        print("RESTORE %s [%s]: shifted %+g%s" % (name, l.name, dx, flag))
    finally:
        font.enableUpdateInterface()

    print("DONE. targets=%d dependents=%d width_fixes=%d restored_layers=%d still_off=%d missing=%d"
          % (len(names), len(dependents), fixed_w, restored, len(still_off), len(missing)))


main()
