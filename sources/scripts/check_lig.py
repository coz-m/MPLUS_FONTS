# -*- coding: utf-8 -*-
"""LIG(MPLUScodeLIG)のマスター構成と、漢字・かなとの対応を表示する(何も書き換えない)。
使い方(リポジトリの一番上のフォルダで):
    make prep_MPLUScodeLIG prep_MPLUSKanji prep_MPLUS1     # 先にマスターを作る
    make check_LIG"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import mplus_helpers as h
from fontTools.designspaceLib import DesignSpaceDocument

LIG_DIR = Path("sources/MPLUScodeLIG/masters")
KAN_DS = Path("sources/MPLUSKanji/masters/M+1p.designspace")
WANT = ("Thin", "Regular", "Bold")          # instancer.py が作る漢字・かなの見本

found = sorted(LIG_DIR.glob("*.designspace"))
if not found or not KAN_DS.exists():
    sys.exit("masters が見つかりません。先に make prep_MPLUScodeLIG prep_MPLUSKanji prep_MPLUS1 を実行してください。")
fam = DesignSpaceDocument.fromfile(str(found[0]))
kan = DesignSpaceDocument.fromfile(str(KAN_DS))
wax = h.weight_axis(fam)
print("設計ファイル:", found[0])
print("軸:")
for a in fam.axes:
    print("   ", a.name, a.tag, "min", a.minimum, "default", a.default, "max", a.maximum, "(map あり)" if a.map else "")
print("instances:", len(fam.instances), " rules:", len(fam.rules))

kax = h.weight_axis(kan)
kinst = {i.styleName: float(kax.map_backward(i.location[kax.name])) for i in kan.instances if i.styleName in WANT}
print("\n漢字の見本(instancer が作るもの) 太さ:", kinst)

others = [a for a in fam.axes if a.name != wax.name]
rows = []
for name, s in h.masters(fam):
    uw = h.user_weight(fam, s)
    widths = tuple(round(float(s.location[a.name]), 1) for a in others)
    rows.append((name, uw, widths))
narrow = min((r[2] for r in rows), default=())
print("\n=== マスター ===")
bad = 0
for name, uw, widths in rows:
    style = next((st for st, w in kinst.items() if abs(w - uw) <= 0.5), None)
    kind = "日本語版に使う(幅が狭いほう)" if widths == narrow else "Latin 版だけ"
    flag = "" if style or widths != narrow else "  !! 対応する漢字の見本なし"
    bad += bool(flag)
    print(f"{name:36s} 太さ(user)={uw:6.1f} 幅={widths}  {kind}  漢字見本={style}{flag}")
print("\nOK: 日本語版のすべてのマスターに漢字の見本があります" if not bad else "\n要注意: 漢字の見本が見つからないマスターがあります")

ufos = sorted(LIG_DIR.glob("*.ufo"))
if ufos:
    names = h.ufo_glyph_names(ufos[0])
    for g in ("space", "LIG.space", "LIG.null"):
        print(f"グリフ {g}:", "あり" if g in names else "なし")
    fea = (ufos[0] / "features.fea").read_text(encoding="utf-8") if (ufos[0] / "features.fea").exists() else ""
    print("features.fea に calt:", "あり" if "feature calt" in fea else "なし", f"({len(fea)} 文字)")
