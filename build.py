from fontTools.designspaceLib import DesignSpaceDocument
from glyphsLib.cli import main
from fontTools.ttLib import newTable, TTFont
import shutil
import subprocess
import multiprocessing
import multiprocessing.pool
from pathlib import Path
import argparse
import ufo2ft, ufoLib2, os, glob
import statmake.classes
import statmake.lib
import fontmake.instantiator
import psautohint.__main__
import cffsubr.__main__
from gftools.stat import gen_stat_tables_from_config
import yaml

def DSIG_modification(font:TTFont):
    font["DSIG"] = newTable("DSIG")     #need that stub dsig
    font["DSIG"].ulVersion = 1
    font["DSIG"].usFlag = 0
    font["DSIG"].usNumSigs = 0
    font["DSIG"].signatureRecords = []
    font["head"].flags |= 1 << 3        #sets flag to always round PPEM to integer

def GASP_set(font:TTFont):
    if "gasp" not in font:
        font["gasp"] = newTable("gasp")
        font["gasp"].gaspRange = {}
    if font["gasp"].gaspRange != {65535: 0x000A}:
        font["gasp"].gaspRange = {65535: 0x000A}

def fixStat(font:Path, STAT:str):
    fontSTAT = [TTFont(f) for f in [str(font)]]
    config = yaml.load(open(STAT), Loader=yaml.SafeLoader)
    gen_stat_tables_from_config(config, fontSTAT)

    for font in fontSTAT:
        font.save(font.reader.file.name)

def step_merge_glyphs_from_ufo(path: Path, instance: ufoLib2.Font, *args) -> None:
    textfile = ""
    for ar in args:
        textfile = ar

    ufo = ufoLib2.Font.open(path)
    if textfile:
        glyphSet = Path(textfile).read_text().split(" ")
        for glyph in glyphSet:
            instance.addGlyph(ufo[glyph])
    else:
        for glyph in ufo:
            if glyph.name not in instance:
                instance.addGlyph(ufo[glyph.name])

def make_static(instance_descriptor, generator, prefix):
    instance = generator.generate_instance(instance_descriptor)
    
    if prefix == "MplusCodeLatin":
        instance.info.openTypeOS2Panose = [2,0,0,9,0,0,0,0,0,0]

    instance.lib['com.github.googlei18n.ufo2ft.filters'] = [{ # extra safe :)
        "name": "flattenComponents",
        "pre": 1,
    }]

    static_ttf = ufo2ft.compileTTF(
        instance, 
        removeOverlaps=True, 
        overlapsBackend="pathops", 
        useProductionNames=True,
    )

    static_otf = ufo2ft.compileOTF(
        instance, 
        removeOverlaps=True, 
        overlapsBackend="pathops", 
        useProductionNames=True,
        inplace=True,
        optimizeCFF=ufo2ft.CFFOptimization.NONE,
    )

    style_name = instance.info.styleName

    if prefix == "MplusCodeLatin":
        prefix = instance_descriptor.familyName

    DSIG_modification(static_ttf)
    print ("["+prefix+"-"+str(style_name).replace(" ","")+"] Saving")
    output = "fonts/ttf/"+prefix.replace(" ","")+"-"+str(style_name).replace(" ","")+".ttf"
    outputOTF = "fonts/otf/"+prefix.replace(" ","")+"-"+str(style_name).replace(" ","")+".otf"
    if "1" in str(output) or "2" in str(output):
        GASP_set(static_ttf)
    static_ttf.save(output)
    static_otf.save(outputOTF)
    if "Latin" in output:
        autohint(output)

    psautohint.__main__.main([outputOTF])
    cffsubr.__main__.main(["-i", outputOTF])


def autohint(file):
    print ("["+str(file).split("/")[2]+"] Autohinting")
    subprocess.check_call(
            [
                "ttfautohint",
                "--stem-width",
                "nsn",
                str(file),
                str(file)[:-4]+"-hinted.ttf",
            ]
        )
    shutil.move(str(file)[:-4]+"-hinted.ttf", str(file))

def build_variable(type:str, ds: DesignSpaceDocument) -> None:
    output = Path("fonts/ttf")

    if type == "latin":

        ds_modified = DesignSpaceDocument.fromfile(sources / "MPLUS-latin_gf.designspace")
        ds_modified.loadSourceFonts(ufoLib2.Font.open)

        for instance in ds_modified.instances:
            instance.name = instance.name.replace("Code", "Code Latin")
            instance.familyName = instance.familyName.replace("Code", "Code Latin")
            if instance.styleMapFamilyName:
                instance.styleMapFamilyName = str(instance.styleMapFamilyName).replace("Code", "Code Latin")
        varFont = ufo2ft.compileVariableTTF(ds_modified)
        DSIG_modification(varFont)
        
        varFont["name"].setName("M PLUS Code Latin", 1, 3, 1, 1033)
        varFont["name"].setName("UFDN;MPLUSCodeLatin-Regular", 3, 3, 1, 1033)
        varFont["name"].setName("M PLUS Code Latin Regular", 4, 3, 1, 1033)
        varFont["name"].setName("MPLUSCodeLatin-Regular", 6, 3, 1, 1033)

        varFont.save(output/"MPLUSCodeLatin[wdth,wght].ttf")
        fixStat(output/"MPLUSCodeLatin[wdth,wght].ttf","sources/MPLUS_STAT.yaml")
        autohint(output/"MPLUSCodeLatin[wdth,wght].ttf")
        prefix = "MPLUSCodeLatin"

    if type == "one" or type == "two":
        print ("[MPLUS "+type+"] Importing Kanji")      
        for source in ds.sources:
            if "{" not in source.name:
                step_merge_glyphs_from_ufo(
                    Path("sources/M+1p-"+source.filename[7:-4]+".ufo"), source.font
                )
            source.font.features.text = Path("sources/features.fea").read_text()

        print ("[MPLUS "+type+"] Importing Kanji replacement rules")      
        kanji_ds = DesignSpaceDocument.fromfile("sources/MPLUS-Kanji.designspace")
        for rule in kanji_ds.rules:
            ds.rules.append(rule)


        print ("[MPLUS "+type+"] Building")
        varFont = ufo2ft.compileVariableTTF(ds)
        DSIG_modification(varFont)
        GASP_set(varFont)

        print ("[MPLUS "+type+"] Saving")      
        if type == "one":
            varFont.save(output/"MPLUS1[wght].ttf")
            prefix = "MPLUS1"
            fixStat(output/"MPLUS1[wght].ttf","sources/MPLUS_STAT.yaml")
        elif type == "two":
            varFont.save(output/"MPLUS2[wght].ttf")
            prefix = "MPLUS2"
            fixStat(output/"MPLUS2[wght].ttf","sources/MPLUS_STAT.yaml")

    if type == "code":

        for instance in ds.instances:
            instance.name = instance.name.replace("M PLUS", "M PLUS 1")
            instance.familyName = instance.familyName.replace("M PLUS", "M PLUS 1")
            if instance.styleMapFamilyName:
                instance.styleMapFamilyName = instance.styleMapFamilyName.replace("M PLUS Code", "M PLUS 1 Code")
            instance.postscriptIsFixedPitch = False

        print ("[MPLUS "+type+"] Importing glyphs")
        for source in ds.sources:
            if "{" not in source.name:
                step_merge_glyphs_from_ufo(
                    Path("sources/MPLUS1-"+str(source.name).split(" ")[3]+".ufo"), source.font,
                    "sources/kana_glyphs.txt"
                )

                step_merge_glyphs_from_ufo(
                    Path("sources/M+1p-"+str(source.name).split(" ")[3]+".ufo"), source.font
                )
            source.name = source.name.replace("M PLUS", "M PLUS 1")
            source.font.features.text = Path("sources/code.fea").read_text()
            source.font.info.postscriptIsFixedPitch = False
            source.font.info.openTypeOS2Panose = [0,0,0,0,0,0,0,0,0,0]

        print ("[MPLUS "+type+"] Importing Kanji replacement rules")      
        kanji_ds = DesignSpaceDocument.fromfile("sources/MPLUS-Kanji.designspace")
        for rule in kanji_ds.rules:
            ds.rules.append(rule)

        print ("[MPLUS "+type+"] Building")
        varFont = ufo2ft.compileVariableTTF(ds)
        DSIG_modification(varFont)
        GASP_set(varFont)

        varFont["name"].setName("M PLUS 1 Code", 1, 3, 1, 1033)
        varFont["name"].setName("UFDN;MPLUS1Code-Regular", 3, 3, 1, 1033)
        varFont["name"].setName("M PLUS 1 Code Regular", 4, 3, 1, 1033)
        varFont["name"].setName("MPLUS1Code-Regular", 6, 3, 1, 1033)

        print ("[MPLUS "+type+"] Saving")      
        varFont.save(output/"MPLUS1Code[wght].ttf")
        fixStat(output/"MPLUS1Code[wght].ttf","sources/MPLUS_STAT.yaml")
        prefix = "MPLUS1Code"

    generator = fontmake.instantiator.Instantiator.from_designspace(ds)

    pool = multiprocessing.pool.Pool(processes=multiprocessing.cpu_count())
    processes = []

    for instance_descriptor in ds.instances: # GOTTA GO FAST
        processes.append(
            pool.apply_async(
                make_static,
                (
                    instance_descriptor,
                    generator,
                    prefix
                ),
            )
        )

    pool.close()
    pool.join()
    for process in processes:
        process.get()
    del processes, pool

def cleanup():
    # Cleanup
    for ufo in sources.glob("*.ufo"):
        shutil.rmtree(ufo)
    os.remove("sources/MPLUS-1.designspace")
    os.remove("sources/MPLUS-2.designspace")
    os.remove("sources/MPLUS-code.designspace")
    os.remove("sources/MPLUS-kanji.designspace")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="build MPLUS fonts")
    parser.add_argument("-O", "--one", action="store_true", dest="one", help="Export MPlus 1")
    parser.add_argument("-T", "--two", action="store_true", dest="two", help="Export MPlus 2")
    parser.add_argument("-C", "--code", action="store_true", dest="code", help="Export MPlus Code JP")
    parser.add_argument("-L", "--latin", action="store_true", dest="latin", help="Export MPlus Code Latin")
    parser.add_argument("-A", "--all", action="store_true", dest="all", help="All variants")
    parser.add_argument("-S", "--ufo", action="store_true", dest="sources", help="Regen all sources")
    parser.add_argument("-W", "--clean", action="store_false", dest="clean", help="Don't remove all source files")

    args = parser.parse_args()
    sources = Path("sources")

    if args.all:
        args.one = True
        args.two = True
        args.code = True
        args.latin = True
        args.sources = True

    if args.sources:
        print ("[MPLUS] Generating UFO sources")
        for file in sources.glob("*.glyphs"):
            print ("["+str(file).split("/")[1]+"] generating source")
            main(("glyphs2ufo", str(file), "--write-public-skip-export-glyphs"))
        
        print ("[MPLUS] Generating Japanese instances for code use") #these are needed as MPlus1 & Kanji don't have the same master positions as Code

        kanaDS = DesignSpaceDocument.fromfile(sources / "MPLUS-1.designspace")
        #delete the substitution rules because we don't want the generator to swap masters when generating instances
        kanaDS.rules = [] 
        kanaDS.loadSourceFonts(ufoLib2.Font.open)
        generator1 = fontmake.instantiator.Instantiator.from_designspace(kanaDS)
        for instance in kanaDS.instances:
            if instance.name == "M PLUS 1 Regular":
                kanaR = generator1.generate_instance(instance)
                kanaR.save("sources/MPLUS1-Regular.ufo", overwrite = True)
            if instance.name == "M PLUS 1 Bold":
                kanaB = generator1.generate_instance(instance)
                kanaB.save("sources/MPLUS1-Bold.ufo", overwrite = True)

        kanjiDS = DesignSpaceDocument.fromfile(sources / "MPLUS-Kanji.designspace")
        kanjiDS.loadSourceFonts(ufoLib2.Font.open)
        generator2 = fontmake.instantiator.Instantiator.from_designspace(kanjiDS)
        for instance in kanjiDS.instances:
            if instance.name == "M+ 1p Regular":
                kanjiR = generator2.generate_instance(instance)
                kanjiR.save("sources/M+1p-Regular.ufo", overwrite = True)
            if instance.name == "M+ 1p Bold":
                kanjiB = generator2.generate_instance(instance)
                kanjiB.save("sources/M+1p-Bold.ufo", overwrite = True)
        
        for ufo in sources.glob("*.ufo"): # need to put this command in all the source UFOs to make sure it is implemented
            source = ufoLib2.Font.open(ufo)
            source.lib['com.github.googlei18n.ufo2ft.filters'] = [{
                "name": "flattenComponents",
                "pre": 1,
            },
            {
                "name": "decomposeTransformedComponents",
                "pre": 1,
            }]
            ufoLib2.Font.save(source)


    if args.latin:
        ds = DesignSpaceDocument.fromfile(sources / "MPLUS-code.designspace")
        ds.loadSourceFonts(ufoLib2.Font.open)
        build_variable("latin", ds)

    if args.one:
        ds1 = DesignSpaceDocument.fromfile(sources / "MPLUS-1.designspace")
        ds1.loadSourceFonts(ufoLib2.Font.open)
        build_variable("one", ds1)

    if args.two:
        ds2 = DesignSpaceDocument.fromfile(sources / "MPLUS-2.designspace")
        ds2.loadSourceFonts(ufoLib2.Font.open)
        build_variable("two", ds2)

    if args.code:
        # this one uses a custom designspace
        ds3 = DesignSpaceDocument.fromfile(sources / "code.designspace")
        ds3.loadSourceFonts(ufoLib2.Font.open)
        build_variable("code", ds3)

    if args.clean:
        print ("Cleaning build files")
        cleanup()