SHELL := /bin/bash

help:
	@echo "###"
	@echo "# Build targets for MPLUS"
	@echo "###"
	@echo
	@echo "  make build:         Builds all fonts and places them in the fonts/ directory"
	@echo "  make build_<name>:  Builds a single family: MPLUS1 MPLUS2 MPLUS3 MPLUSU MPLUS1Code MPLUSCodeLatin"
	@echo "  make check_MPLUS3:  Prints the Kanji merge plan for MPLUS3 (builds nothing)"
	@echo

#############################################################
#################### venv setup scripts #####################
#############################################################

# Creates the Python virtual environment and installs requirements.txt
# (use e.g. 'python3.12 -m venv venv' beforehand if the default python3 is too old)
venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

venv: venv/touchfile

#############################################################
################# Source preparation tools ##################
#############################################################
# Converts each .glyphs source into UFO masters (sources/<name>/masters)

prep_MPLUS1: venv
	. venv/bin/activate; fontmake -g sources/MPLUS1/MPLUS-1.glyphs --master-dir sources/MPLUS1/masters -o ufo;

prep_MPLUS2: venv
	. venv/bin/activate; fontmake -g sources/MPLUS2/MPLUS-2.glyphs --master-dir sources/MPLUS2/masters -o ufo;

prep_MPLUS3: venv
	. venv/bin/activate; fontmake -g sources/MPLUS3/MPLUS-3.glyphs --master-dir sources/MPLUS3/masters -o ufo;

prep_MPLUS1Code: venv
	. venv/bin/activate; fontmake -g sources/MPLUS1Code/MPLUS1-code.glyphs --master-dir sources/MPLUS1Code/masters -o ufo;

prep_MPLUSKanji: venv
	. venv/bin/activate; fontmake -g sources/MPLUSKanji/MPLUS-Kanji.glyphs --master-dir sources/MPLUSKanji/masters -o ufo;

prep_MPLUSU: venv
	. venv/bin/activate; fontmake -g sources/MPLUSU/MPLUS-U.glyphs --master-dir sources/MPLUSU/masters -o ufo;

prep: prep_MPLUS1 prep_MPLUS2 prep_MPLUS3 prep_MPLUSU prep_MPLUSKanji prep_MPLUS1Code

#############################################################
###################### Compile scripts ######################
#############################################################
# Builds the final fonts from sources/<name>/merged_ufo into fonts/<name>

compile_MPLUS1: venv
	. venv/bin/activate; gftools builder sources/MPLUS1/config.yaml;

compile_MPLUS2: venv
	. venv/bin/activate; gftools builder sources/MPLUS2/config.yaml;

compile_MPLUS3: venv
	. venv/bin/activate; gftools builder sources/MPLUS3/config.yaml;

compile_MPLUSU: venv
	. venv/bin/activate; gftools builder sources/MPLUSU/config.yaml;

compile_MPLUS1Code: venv
	. venv/bin/activate; gftools builder sources/MPLUS1Code/config.yaml;

compile_MPLUSCodeLatin: venv
	. venv/bin/activate; gftools builder sources/MPLUSCodeLatin/config.yaml;

compile: compile_MPLUS1 compile_MPLUS2 compile_MPLUS3 compile_MPLUSU compile_MPLUS1Code compile_MPLUSCodeLatin

#############################################################
####################### Build scripts #######################
#############################################################

# Merges the shared Kanji into MPLUS1 / MPLUS2 / MPLUSU and prepares the Code fonts.
# Without arguments merge.py processes every family and deletes the whole fonts/ directory first.
merge: venv
	. venv/bin/activate; python3 sources/scripts/merge.py;

# Same, but for one family only (deletes only fonts/<name>)
merge_MPLUS1: venv
	. venv/bin/activate; python3 sources/scripts/merge.py MPLUS1;

merge_MPLUS2: venv
	. venv/bin/activate; python3 sources/scripts/merge.py MPLUS2;

merge_MPLUSU: venv
	. venv/bin/activate; python3 sources/scripts/merge.py MPLUSU;

merge_MPLUS1Code: venv
	. venv/bin/activate; python3 sources/scripts/merge.py MPLUS1Code;

merge_MPLUSCodeLatin: venv
	. venv/bin/activate; python3 sources/scripts/merge.py MPLUSCodeLatin;

# Merges the shared Kanji into MPLUS3 (interpolates the Kanji if no matching master exists)
merge_MPLUS3: venv
	. venv/bin/activate; python3 sources/scripts/merge_mplus3.py;

# Prints how the Kanji will be merged into each MPLUS3 master; changes nothing
check_MPLUS3: venv
	. venv/bin/activate; python3 sources/scripts/check_mplus3.py;

# Creates interpolated instances (needed only by the Code fonts)
instancer: venv
	. venv/bin/activate; python3 sources/scripts/instancer.py;

# Removes generated working directories (the fonts/ directory is kept)
clean:
	find . -depth -type d -name "masters" -exec rm -rf {} +
	find . -depth -type d -name "merged_ufo" -exec rm -rf {} +
	find . -depth -type d -name "instances" -exec rm -rf {} +

# Builds everything. merge_MPLUS3 must run after merge (merge deletes fonts/).
build: venv clean prep instancer merge merge_MPLUS3 compile

#############################################################
################## Build a single family ####################
#############################################################
# These do not run 'clean'. If the sources changed a lot, run 'make clean' first.

# MPLUS1 / MPLUS2 / MPLUSU: base source + shared Kanji
build_MPLUS1: venv prep_MPLUS1 prep_MPLUSKanji merge_MPLUS1 compile_MPLUS1

build_MPLUS2: venv prep_MPLUS2 prep_MPLUSKanji merge_MPLUS2 compile_MPLUS2

build_MPLUSU: venv prep_MPLUSU prep_MPLUSKanji merge_MPLUSU compile_MPLUSU

# MPLUS3: Japanese version (own Kanji handling in merge_mplus3.py)
build_MPLUS3: venv prep_MPLUS3 prep_MPLUSKanji merge_MPLUS3 compile_MPLUS3

# MPLUS1Code: width-500 masters of the Code source + Kana from MPLUS1 + shared Kanji (needs instances)
build_MPLUS1Code: venv prep_MPLUS1 prep_MPLUS1Code prep_MPLUSKanji instancer merge_MPLUS1Code compile_MPLUS1Code

# MPLUSCodeLatin: Latin-only copy of the Code source (width 500 and 600)
build_MPLUSCodeLatin: venv prep_MPLUS1Code merge_MPLUSCodeLatin compile_MPLUSCodeLatin
