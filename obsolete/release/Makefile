TESTFLIGHT_VER= 063a

RELEASE=	mplus-TESTFLIGHT-${TESTFLIGHT_VER}

FILES=	LICENSE_E LICENSE_J README_E README_J m++ipa.pe

FONTS=	../work.d/targets/mplus-1p/black/mplus-1p-black.ttf \
	../work.d/targets/mplus-1p/heavy/mplus-1p-heavy.ttf \
	../work.d/targets/mplus-1p/bold/mplus-1p-bold.ttf \
	../work.d/targets/mplus-1p/medium/mplus-1p-medium.ttf \
	../work.d/targets/mplus-1p/regular/mplus-1p-regular.ttf \
	../work.d/targets/mplus-1p/light/mplus-1p-light.ttf \
	../work.d/targets/mplus-1p/thin/mplus-1p-thin.ttf \
	../work.d/targets/mplus-2p/black/mplus-2p-black.ttf \
	../work.d/targets/mplus-2p/heavy/mplus-2p-heavy.ttf \
	../work.d/targets/mplus-2p/bold/mplus-2p-bold.ttf \
	../work.d/targets/mplus-2p/medium/mplus-2p-medium.ttf \
	../work.d/targets/mplus-2p/regular/mplus-2p-regular.ttf \
	../work.d/targets/mplus-2p/light/mplus-2p-light.ttf \
	../work.d/targets/mplus-2p/thin/mplus-2p-thin.ttf \
	../work.d/targets/mplus-1m/bold/mplus-1m-bold.ttf \
	../work.d/targets/mplus-1m/medium/mplus-1m-medium.ttf \
	../work.d/targets/mplus-1m/regular/mplus-1m-regular.ttf \
	../work.d/targets/mplus-1m/light/mplus-1m-light.ttf \
	../work.d/targets/mplus-1m/thin/mplus-1m-thin.ttf \
	../work.d/targets/mplus-2m/bold/mplus-2m-bold.ttf \
	../work.d/targets/mplus-2m/medium/mplus-2m-medium.ttf \
	../work.d/targets/mplus-2m/regular/mplus-2m-regular.ttf \
	../work.d/targets/mplus-2m/light/mplus-2m-light.ttf \
	../work.d/targets/mplus-2m/thin/mplus-2m-thin.ttf \
	../work.d/targets/mplus-1c/black/mplus-1c-black.ttf \
	../work.d/targets/mplus-1c/heavy/mplus-1c-heavy.ttf \
	../work.d/targets/mplus-1c/bold/mplus-1c-bold.ttf \
	../work.d/targets/mplus-1c/medium/mplus-1c-medium.ttf \
	../work.d/targets/mplus-1c/regular/mplus-1c-regular.ttf \
	../work.d/targets/mplus-1c/light/mplus-1c-light.ttf \
	../work.d/targets/mplus-1c/thin/mplus-1c-thin.ttf \
	../work.d/targets/mplus-2c/black/mplus-2c-black.ttf \
	../work.d/targets/mplus-2c/heavy/mplus-2c-heavy.ttf \
	../work.d/targets/mplus-2c/bold/mplus-2c-bold.ttf \
	../work.d/targets/mplus-2c/medium/mplus-2c-medium.ttf \
	../work.d/targets/mplus-2c/regular/mplus-2c-regular.ttf \
	../work.d/targets/mplus-2c/light/mplus-2c-light.ttf \
	../work.d/targets/mplus-2c/thin/mplus-2c-thin.ttf \
 	../work.d/targets/mplus-1mn/bold/mplus-1mn-bold.ttf \
 	../work.d/targets/mplus-1mn/medium/mplus-1mn-medium.ttf \
 	../work.d/targets/mplus-1mn/regular/mplus-1mn-regular.ttf \
 	../work.d/targets/mplus-1mn/light/mplus-1mn-light.ttf \
 	../work.d/targets/mplus-1mn/thin/mplus-1mn-thin.ttf
#	../work.d/targets/mplus-2mn/bold/mplus-2mn-bold.ttf \
#	../work.d/targets/mplus-2mn/medium/mplus-2mn-medium.ttf \
#	../work.d/targets/mplus-2mn/regular/mplus-2mn-regular.ttf \
#	../work.d/targets/mplus-2mn/light/mplus-2mn-light.ttf \
#	../work.d/targets/mplus-2mn/thin/mplus-2mn-thin.ttf

release: 
	mkdir -p ${RELEASE}
	cp -p $(FILES) ${RELEASE}
	cp -p $(FONTS) ${RELEASE}
#	tar cvfz ${RELEASE}.tar.gz ${RELEASE}/
	tar cf - ${RELEASE}/ | xz -9 -c > ${RELEASE}.tar.xz
	rm -rf ${RELEASE}

clean:
	rm -rf ${RELEASE} ${RELEASE}.tar.gz
