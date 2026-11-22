# -*- coding: utf-8 -*-
"""MPLUS3 と共有漢字の「合成計画」を表示する(フォントは作らない・何も書き換えない)。
使い方(リポジトリの一番上のフォルダで):  python3 sources/scripts/check_mplus3.py
先に  make prep_MPLUS3 prep_MPLUSKanji  で masters フォルダを作っておくこと。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import mplus_helpers as h

FAM = Path("sources/MPLUS3/masters/MPLUS3.designspace")
KAN = Path("sources/MPLUSKanji/masters/M+1p.designspace")
for p in (FAM, KAN):
    if not p.exists():
        sys.exit(f"見つかりません: {p}\n先に make prep_MPLUS3 prep_MPLUSKanji を実行してください。"
                 "\n(ファイル名が違う場合は masters フォルダ内の .designspace の名前を教えてください)")
for label, p in (("MPLUS3", FAM), ("Kanji", KAN)):
    d = h.describe_designspace(p)
    print(f"[{label}] axes={d['axes']}\n         instances={d['instances']} rules={d['rules']}")
    for m in d["masters"]:
        print("         master:", m)
print("\n=== 合成計画 ===")
bad = 0
for it in h.plan_kanji_sources(FAM, KAN):
    print(f"{it['ufo']:32s} weight={it['user_weight']:6.1f}  {it['mode']:12s}", it["kanji_master"] or it["kanji_location"] or "")
    bad += it["mode"] == "out_of_range"
print("\n要注意: 漢字の太さ範囲外のマスターがあります(最寄りの太さで代用されます)" if bad else "\nOK: すべてのマスターに漢字を用意できます")
