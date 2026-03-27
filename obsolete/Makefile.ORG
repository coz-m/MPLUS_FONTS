# black, heavy is not designed in monospace fonts, so it's in `ABRIDGED_GROUPS'
UNABRIDGED_GROUPS:=	hiragana1 katakana1 miscellaneous1 \
			hiragana2 katakana2 miscellaneous2 \
			katakana_half1 \
			latin_proportional1 latin_proportional2 \
			latin_clear1 latin_clear2 \
			latin_fullwidth1 latin_fullwidth2 \
			latin_full_clear1 latin_full_clear2
ABRIDGED_GROUPS:=	latin_monospace1 latin_monospace2 \
			latin_mono_new1 # latin_mono_new2
OPTIONAL_GROUPS:=	kanji/k1 kanji/k2 kanji/k3 kanji/k4 kanji/k5 kanji/k6 \
			kanji/j1 kanji/j2 kanji/j3 kanji/j4 kanji/j5 \
			kanji/l100 kanji/l101 kanji/l102 kanji/l103 kanji/l104 \
			kanji/l105 kanji/l200 kanji/l201 kanji/l202 kanji/l203 \
			kanji/l204 kanji/l205 kanji/l206 kanji/l207 kanji/l208 \
			kanji/l209 kanji/l210 kanji/l211 kanji/l212 kanji/l213 \
			kanji/l214 kanji/l215 kanji/l216
ifdef MPLUS_FULLSET
UNABRIDGED_GROUPS+=	${OPTIONAL_GROUPS}
endif
GROUPS:=		${UNABRIDGED_GROUPS} ${ABRIDGED_GROUPS}
BLACK_WEIGHTS:=		black heavy
NORMAL_WEIGHTS:=	bold medium regular light thin
WEIGHTS:=		${BLACK_WEIGHTS} ${NORMAL_WEIGHTS}
TARGETS:=		mplus-1p mplus-2p mplus-1m mplus-2m mplus-1c mplus-2c \
			mplus-1mn # mplus-2mn
ifdef MPLUS_FULLSET
TARGETS+=		mplus-1k mplus-2k
endif
BASELINE_SHIFT:=	58

SPLIT_CONCURRENCY:=	1
SCRIPTS:=scripts

ifdef MPLUS_FULLSET
KANJI1:=mplus-1k
KANJI2:=mplus-2k
else
KANJI1:=
KANJI2:=
endif

all:
	@($(MAKE) split-svgs ; $(MAKE) rebuild-ttf)

ttf: mplus-1p mplus-2p mplus-1m mplus-2m mplus-1c mplus-2c mplus-1mn # mplus-2mn

otf: mplus-1p-otf mplus-2p-otf mplus-1m-otf mplus-2m-otf mplus-1c-otf mplus-2c-otf mplus-1mn-otf # mplus-2mn-otf

mplus-1p: work.d/targets/mplus-1p/Makefile $(KANJI1)
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-2p: work.d/targets/mplus-2p/Makefile $(KANJI2)
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-1m: work.d/targets/mplus-1m/Makefile $(KANJI1)
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-2m: work.d/targets/mplus-2m/Makefile $(KANJI2)
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-1c: work.d/targets/mplus-1c/Makefile $(KANJI1)
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-2c: work.d/targets/mplus-2c/Makefile $(KANJI2)
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-1mn: work.d/targets/mplus-1mn/Makefile $(KANJI1)
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-2mn: work.d/targets/mplus-2mn/Makefile $(KANJI2)
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-1k: work.d/targets/mplus-1k/Makefile
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-2k: work.d/targets/mplus-2k/Makefile
	@(cd work.d/targets/$@ ; $(MAKE))

mplus-1p-otf: work.d/targets/mplus-1p/Makefile $(KANJI1)
	@(cd work.d/targets/mplus-1p ; $(MAKE) otf)

mplus-2p-otf: work.d/targets/mplus-2p/Makefile $(KANJI2)
	@(cd work.d/targets/mplus-2p ; $(MAKE) otf)

mplus-1m-otf: work.d/targets/mplus-1m/Makefile $(KANJI1)
	@(cd work.d/targets/mplus-1m ; $(MAKE) otf)

mplus-2m-otf: work.d/targets/mplus-2m/Makefile $(KANJI2)
	@(cd work.d/targets/mplus-2m ; $(MAKE) otf)

mplus-1c-otf: work.d/targets/mplus-1c/Makefile $(KANJI1)
	@(cd work.d/targets/mplus-1c ; $(MAKE) otf)

mplus-2c-otf: work.d/targets/mplus-2c/Makefile $(KANJI2)
	@(cd work.d/targets/mplus-2c ; $(MAKE) otf)

mplus-1mn-otf: work.d/targets/mplus-1mn/Makefile $(KANJI1)
	@(cd work.d/targets/mplus-1mn ; $(MAKE) otf)

mplus-2mn-otf: work.d/targets/mplus-2mn/Makefile $(KANJI2)
	@(cd work.d/targets/mplus-2mn ; $(MAKE) otf)

mplus-1k-otf: work.d/targets/mplus-1k/Makefile
	@(cd work.d/targets/mplus-1k ; $(MAKE) otf)

mplus-2k-otf: work.d/targets/mplus-2k/Makefile
	@(cd work.d/targets/mplus-2k ; $(MAKE) otf)

work.d/targets/mplus-1p/Makefile: $(SCRIPTS)/target-Makefile.1.tmpl dirs
	sed s/^#Mplus-1P#// $(SCRIPTS)/target-Makefile.1.tmpl > $@

work.d/targets/mplus-2p/Makefile: $(SCRIPTS)/target-Makefile.1.tmpl dirs
	sed s/^#Mplus-2P#// $(SCRIPTS)/target-Makefile.1.tmpl > $@

work.d/targets/mplus-1m/Makefile: $(SCRIPTS)/target-Makefile.1s.tmpl dirs
	sed s/^#Mplus-1M#// $(SCRIPTS)/target-Makefile.1s.tmpl > $@

work.d/targets/mplus-2m/Makefile: $(SCRIPTS)/target-Makefile.1s.tmpl dirs
	sed s/^#Mplus-2M#// $(SCRIPTS)/target-Makefile.1s.tmpl > $@

work.d/targets/mplus-1c/Makefile: $(SCRIPTS)/target-Makefile.1.tmpl dirs
	sed s/^#Mplus-1C#// $(SCRIPTS)/target-Makefile.1.tmpl > $@

work.d/targets/mplus-2c/Makefile: $(SCRIPTS)/target-Makefile.1.tmpl dirs
	sed s/^#Mplus-2C#// $(SCRIPTS)/target-Makefile.1.tmpl > $@

work.d/targets/mplus-1mn/Makefile: $(SCRIPTS)/target-Makefile.1s.tmpl dirs
	sed s/^#Mplus-1mN#// $(SCRIPTS)/target-Makefile.1s.tmpl > $@

work.d/targets/mplus-2mn/Makefile: $(SCRIPTS)/target-Makefile.1s.tmpl dirs
	sed s/^#Mplus-2mN#// $(SCRIPTS)/target-Makefile.1s.tmpl > $@

work.d/targets/mplus-1k/Makefile: $(SCRIPTS)/target-Makefile.1.tmpl dirs
	sed s/^#Mplus-1k#// $(SCRIPTS)/target-Makefile.1.tmpl > $@

work.d/targets/mplus-2k/Makefile: $(SCRIPTS)/target-Makefile.1.tmpl dirs
	sed s/^#Mplus-2k#// $(SCRIPTS)/target-Makefile.1.tmpl > $@

dirs:
	for w in $(NORMAL_WEIGHTS) ; do \
		for g in $(GROUPS) ; do \
			mkdir -p work.d/splitted/$$w/$$g/ ;\
		done ;\
		for t in $(TARGETS); do \
			mkdir -p work.d/targets/$$t/$$w/ ;\
		done \
	done
	for w in $(BLACK_WEIGHTS) ; do \
		for g in $(UNABRIDGED_GROUPS) ; do \
			mkdir -p work.d/splitted/$$w/$$g/ ;\
		done ;\
		for t in $(TARGETS); do \
			mkdir -p work.d/targets/$$t/$$w/ ;\
		done \
	done

ifdef MPLUS_FULLSET
SVGFILES=	svg.d/*/*.svg svg.d/*/*/*.svg
else
SVGFILES=	svg.d/*/*.svg svg.d/*/vert/*.svg
endif

split-svgs: dirs
	perl -I $(SCRIPTS) $(SCRIPTS)/split-svg.pl $(SPLIT_CONCURRENCY) ${SVGFILES}

clean:
	@rm -rf work.d/ release/mplus-* *~ 

clean-targets:
	@rm -rf work.d/targets/

rebuild-ttf:
	@($(MAKE) clean-targets ; $(MAKE) dirs ; $(MAKE) ttf)

release: ttf
	@(cd release ; $(MAKE) )
