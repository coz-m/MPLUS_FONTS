SHELL := /bin/bash

help:
	@echo "###"
	@echo "# Build targets for MPLUS"
	@echo "###"
	@echo
	@echo "  make build:         Builds all fonts and places them in the fonts/ directory"
	@echo "  make build_MPLUS3:  Builds only MPLUS3 (Japanese, with the shared Kanji)"
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

# Merges the shared Kanji into MPLUS1 / MPLUS2 / MPLUSU, builds the Code fonts' sources.
# NOTE: merge.py deletes the fonts/ directory first.
merge: venv
	. venv/bin/activate; python3 sources/scripts/merge.py;

# Merges the shared Kanji into MPLUS3 (interpolates the Kanji if no matching master exists)
merge_MPLUS3: venv
	. venv/bin/activate; python3 sources/scripts/merge_mplus3.py;

# Prints how the Kanji will be merged into each MPLUS3 master; changes nothing
check_MPLUS3: venv
	. venv/bin/activate; python3 sources/scripts/check_mplus3.py;

# Creates interpolated instances (needed for the Code fonts)
instancer: venv
	. venv/bin/activate; python3 sources/scripts/instancer.py;

# Removes generated working directories (the fonts/ directory is kept)
clean:
	find . -depth -type d -name "masters" -exec rm -rf {} +
	find . -depth -type d -name "merged_ufo" -exec rm -rf {} +
	find . -depth -type d -name "instances" -exec rm -rf {} +

# Builds everything. merge_MPLUS3 must run after merge (merge deletes fonts/).
build: venv clean prep instancer merge merge_MPLUS3 compile

# Builds only MPLUS3 (Japanese). Does not touch the other families.
build_MPLUS3: venv prep_MPLUS3 prep_MPLUSKanji merge_MPLUS3 compile_MPLUS3
