# -*- coding: utf-8 -*-
"""MPLUS3 (漢字以外) に共有漢字 MPLUSKanji を合成して merged_ufo を作る。
MPLUS1 / MPLUS2 を作る merge.py と同じ方法(ufomerge)を使う。
漢字側に同じ名前・同じ太さのマスターが無い場合は、その太さで漢字を補間して使う。
注意: merge.py は最初に fonts フォルダを消すので、merge.py のあとに実行すること(Makefile はその順)。"""
import shutil, sys
from pathlib import Path
import ufoLib2
from ufomerge import merge_ufos
sys.path.insert(0, str(Path(__file__).parent))
import mplus_helpers as h

SRC = Path("sources")
FAM_DS = SRC / "MPLUS3/masters/MPLUS3.designspace"
KAN_DS = SRC / "MPLUSKanji/masters/M+1p.designspace"
OUT = SRC / "MPLUS3/merged_ufo"
FEA = SRC / "scripts/features.fea"          # MPLUS1/2 と共通。MPLUS3 に合わない場合は専用ファイルに差し替える
OUT.mkdir(parents=True, exist_ok=True)

operator = None
for it in h.plan_kanji_sources(FAM_DS, KAN_DS):
    print(f"- {it['ufo']}  ({it['mode']})")
    if it["mode"] == "direct":
        kanji = ufoLib2.Font.open(SRC / "MPLUSKanji/masters" / it["kanji_master"])
    else:
        if it["mode"] == "out_of_range":
            print("  !! 漢字の太さ範囲外: 最寄りの太さで代用します")
        from ufoProcessor.ufoOperator import UFOOperator
        from fontTools.designspaceLib import DesignSpaceDocument
        if operator is None:
            kds = DesignSpaceDocument.fromfile(str(KAN_DS)); kds.rules = []
            operator = UFOOperator(kds); operator.loadFonts()
        loc = it["kanji_location"] or {a.name: a.map_forward(min(max(it["user_weight"], a.minimum), a.maximum))
                                       if a.tag == "wght" else a.map_forward(a.default)
                                       for a in operator.doc.axes}
        kanji = operator.makeOneInstance(loc, doRules=False)
    with ufoLib2.Font.open(SRC / "MPLUS3/masters" / it["ufo"]) as cur:
        # 同じ文字コードを MPLUS3 側がすでに持っている場合は、漢字側のグリフを取り除く(MPLUS3 を優先)。
        # 名前が違うだけで同じ文字(例: close-han と uni3006)があると、書き出しで止まるため。
        cur_map = {}
        for g in cur:
            for u in g.unicodes:
                cur_map.setdefault(u, g.name)
        renamed = {}
        for g in list(kanji):
            hit = [cur_map[u] for u in g.unicodes if u in cur_map and cur_map[u] != g.name]
            if hit:
                renamed[g.name] = hit[0]
        for name in renamed:
            del kanji[name]
        for g in kanji:                      # 取り除いたグリフを部品に使っているものは、MPLUS3 側の名前に付け替える
            for c in g.components:
                if c.baseGlyph in renamed:
                    c.baseGlyph = renamed[c.baseGlyph]
        kanji.glyphOrder = [n for n in kanji.glyphOrder if n in kanji]
        if renamed:
            print("  文字コードの重複を回避(MPLUS3 側を優先):", ", ".join(f"{k}->{v}" for k, v in sorted(renamed.items())))
        merge_ufos(cur, kanji, layout_handling="closure", existing_handling="skip")
        if FEA.exists():
            cur.features.text = FEA.read_text()
        cur.save(OUT / it["ufo"], overwrite=True, validate=False)
shutil.copy(FAM_DS, OUT / "MPLUS3.designspace")
print("done ->", OUT)
