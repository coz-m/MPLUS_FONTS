SHELL := /bin/bash

help:
	@echo "###"
	@echo "# Build targets for MPLUS"
	@echo "###"
	@echo
	@echo "  make build: Builds the fonts and places them in the fonts/ directory"
	@echo

#############################################################
#################### venv setup scripts #####################
#############################################################

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

venv: venv/touchfile

#############################################################
################# Source preparation tools ##################
#############################################################

prep_MPLUS1: venv
	. venv/bin/activate; fontmake -g sources/MPLUS1/MPLUS-1.glyphs --master-dir sources/MPLUS1/masters -o ufo;

prep_MPLUS2: venv
	. venv/bin/activate; fontmake -g sources/MPLUS2/MPLUS-2.glyphs --master-dir sources/MPLUS2/masters -o ufo;

prep_MPLUS3: venv
	. venv/bin/activate; fontmake -g sources/MPLUS3/MPLUS-3.glyphs --master-dir sources/MPLUS3/masters -o ufo;

prep_MPLUS1Code: venv
	. venv/bin/activate; fontmake -g sources/MPLUS1Code/MPLUS1-code.glyphs --master-dir sources/MPLUS1Code/masters -o ufo;

prep_MPLUSKanji: venv
	. venv/bin/activate; fontmake -g sources/MPLUSKanji/MPLUS-kanji.glyphs --master-dir sources/MPLUSKanji/masters -o ufo;

prep_MPLUSU: venv
	. venv/bin/activate; fontmake -g sources/MPLUSU/MPLUS-U.glyphs --master-dir sources/MPLUSU/masters -o ufo;

prep: prep_MPLUS1 prep_MPLUS2 prep_MPLUSU prep_MPLUSKanji prep_MPLUS1Code

#############################################################	
###################### Compile scripts ######################
#############################################################

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

compile: compile_MPLUS1 compile_MPLUS2 compile_MPLUSU compile_MPLUS1Code compile_MPLUSCodeLatin

#############################################################	
####################### Build scripts #######################
#############################################################

merge: venv
	. venv/bin/activate; python3 sources/scripts/merge.py;

instancer: venv
	. venv/bin/activate; python3 sources/scripts/instancer.py;

clean:
	find . -depth -type d -name "masters" -exec rm -rf {} +
	find . -depth -type d -name "merged_ufo" -exec rm -rf {} +
	find . -depth -type d -name "instances" -exec rm -rf {} +

build: venv clean prep instancer merge compile

#############################################################	
######################## Misc scripts #######################
#############################################################
