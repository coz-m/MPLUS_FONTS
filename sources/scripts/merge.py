import shutil, os
import ufoLib2, glob
from pathlib import Path
from ufomerge import merge_ufos, subset_ufo
from ufoLib2.objects import Kerning
import shutil
import fontTools.designspaceLib
import copy
import sys

SOURCE = Path("sources")

if Path("fonts").exists():
    shutil.rmtree("fonts")

for font in ["MPLUS1", "MPLUS2", "MPLUSU", "MPLUS1Code", "MPLUSCodeLatin"]:

    print ("*** *** *** *** Processing "+font+" *** *** *** ***")
    os.makedirs("sources/"+font+"/merged_ufo/", exist_ok=True)
    EXPORT = Path("sources/"+font+"/merged_ufo")

    if font in ["MPLUS1", "MPLUS2", "MPLUSU"]: #Merging in Kanji into the three base versions
        for ufo in SOURCE.glob(font+"/masters/*.ufo"):
            ufoName = str(ufo).split("/")[3]
            print ("- "+ufoName)
            sourceName = str(ufo).split("/")[3].replace(font,"M+1p")
            with ufoLib2.Font.open(ufo) as currentUFO:
                with ufoLib2.Font.open(SOURCE/"MPLUSKanji/masters"/sourceName) as extensionUFO:
                    merge_ufos(
                        currentUFO,
                        extensionUFO,
                        layout_handling="closure",
                        existing_handling="skip",
                    )
                currentUFO.features.text = Path("sources/scripts/features.fea").read_text()
                currentUFO.save(EXPORT/ufoName,overwrite=True,validate=False)
        shutil.copy("sources/"+font+"/masters/"+font+".designspace","sources/"+font+"/merged_ufo/"+font+".designspace")

    if font == "MPLUS1Code": # Merging in Kana from MPLUS1 and Kanji from MPLUS Kanji into the Code version
        for ufo in SOURCE.glob(font+"/masters/*.ufo"):
            if "60" not in str(ufo):
                ufoName = str(ufo).split("/")[3]
                print ("- "+ufoName)
                with ufoLib2.Font.open(ufo) as currentUFO:

                    with open("sources/MPLUS1Code/kana_glyphs.txt", "r", encoding="utf-8") as f:
                        glyphSet = {line.strip() for line in f if line.strip() and not line.startswith("#")}

                        sourceName = str(ufo).split("/")[3].replace("MPLUS1Code","MPLUS1")
                        with ufoLib2.Font.open(SOURCE/"MPLUS1/instances"/sourceName) as extensionUFO:
                            merge_ufos(
                                currentUFO,
                                extensionUFO,
                                glyphs=glyphSet,
                                layout_handling="ignore",
                                existing_handling="skip",
                            )
                    currentUFO.kerning = Kerning()
                    
                    sourceName = str(ufo).split("/")[3].replace("MPLUS1Code","M+1p")
                    with ufoLib2.Font.open(SOURCE/"MPLUSKanji/instances"/sourceName) as extensionUFO:
                        merge_ufos(
                            currentUFO,
                            extensionUFO,
                            layout_handling="ignore",
                            existing_handling="skip",
                        )
                    currentUFO.features.text = Path("sources/scripts/code.fea").read_text()
                    currentUFO.save(EXPORT/ufoName,overwrite=True,validate=False)

    if font == "MPLUSCodeLatin": #renaming for Latin only
        for ufo in SOURCE.glob("MPLUS1Code/masters/*.ufo"):
            with ufoLib2.Font.open(ufo) as currentUFO:
                currentUFO.info.familyName = "M PLUS Code Latin"
                currentUFO.info.styleMapFamilyName = "M PLUS Code Latin"
                currentUFO.save(str(ufo).replace("MPLUS1Code/","MPLUSCodeLatin/").replace("masters","merged_ufo"),overwrite=True,validate=False)
        shutil.copy("sources/MPLUS1Code/masters/MPLUS1Code.designspace","sources/"+font+"/merged_ufo/"+font+".designspace")
