## Fontbakery report

Fontbakery version: 0.7.34

<details>
<summary><b>[1] Family checks</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Is the command `ftxvalidator` (Apple Font Tool Suite) available?</summary>

* [com.google.fonts/check/ftxvalidator_is_available](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ftxvalidator_is_available)
<pre>--- Rationale ---

There&#x27;s no reasonable (and legal) way to run the command `ftxvalidator` of the
Apple Font Tool Suite on a non-macOS machine. I.e. on GNU+Linux or Windows etc.

If Font Bakery is not running on an OSX machine, the machine running Font
Bakery could access `ftxvalidator` on OSX, e.g. via ssh or a remote procedure
call (rpc).

There&#x27;s an ssh example implementation at:
https://github.com/googlefonts/fontbakery/blob/master/prebuilt/workarounds
/ftxvalidator/ssh-implementation/ftxvalidator


</pre>

* ⚠ **WARN** Could not find ftxvalidator.

</details>
<br>
</details>
<details>
<summary><b>[12] MplusCode-Bold.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Mplus Code" but got "MplusCode". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FULL_FONT_NAME entries.</summary>

* [com.google.fonts/check/name/fullfontname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/fullfontname)

* 🔥 **FAIL** Entry [FULL_FONT_NAME(4):WINDOWS(3)] on the "name" table: Expected "Mplus Code Bold"  but got "MplusCode Bold". [code: bad-entry]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---

There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)

Requirements for monospace fonts:

* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm

* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm

* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2

* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397

Also we should report an error for glyphs not of average width.

Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave
a font a monospace flag in Panose, Microsoft Word would ignore the actual
advance widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140


</pre>

* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** On monospaced fonts, the value of OS/2.panose.bProportion must be set to 9 (proportion: monospaced), but got 0 instead. [code: mono-bad-panose-proportion]
* ⚠ **WARN** Font is monospaced but 553 glyphs (8.46%) have a different width. You should check the widths of: ['A', 'Aacute', 'Abreve', 'uni1EAE', 'uni1EB6', 'uni1EB0', 'uni1EB2', 'uni1EB4', 'Acircumflex', 'uni1EA4', 'uni1EAC', 'uni1EA6', 'uni1EA8', 'uni1EAA', 'uni0200', 'Adieresis', 'uni0226', 'uni1EA0', 'Agrave', 'uni1EA2', 'uni0202', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde', 'AE', 'AEacute', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'uni01C4', 'Eth', 'Dcaron', 'Dcroat', 'uni01C5', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'uni1EBE', 'uni1EC6', 'uni1EC0', 'uni1EC2', 'uni1EC4', 'uni0204', 'Edieresis', 'Edotaccent', 'uni1EB8', 'Egrave', 'uni1EBA', 'uni0206', 'Emacron', 'Eogonek', 'uni1EBC', 'F', 'G', 'Gbreve', 'Gcaron', 'Gcircumflex', 'uni0122', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'I', 'Iacute', 'Ibreve', 'Icircumflex', 'uni0208', 'Idieresis', 'Idotaccent', 'uni1ECA', 'Igrave', 'uni1EC8', 'uni020A', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'uni0136', 'L', 'uni01C7', 'Lacute', 'Lcaron', 'uni013B', 'Ldot', 'uni01C8', 'Lslash', 'M', 'N', 'uni01CA', 'Nacute', 'Ncaron', 'uni0145', 'Eng', 'uni01CB', 'Ntilde', 'O', 'Oacute', 'Obreve', 'Ocircumflex', 'uni1ED0', 'uni1ED8', 'uni1ED2', 'uni1ED4', 'uni1ED6', 'uni020C', 'Odieresis', 'uni022A', 'uni022E', 'uni0230', 'uni1ECC', 'Ograve', 'uni1ECE', 'Ohorn', 'uni1EDA', 'uni1EE2', 'uni1EDC', 'uni1EDE', 'uni1EE0', 'Ohungarumlaut', 'uni020E', 'Omacron', 'uni01EA', 'Oslash', 'Oslashacute', 'Otilde', 'uni022C', 'OE', 'P', 'Thorn', 'Q', 'R', 'Racute', 'Rcaron', 'uni0156', 'uni0210', 'uni0212', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'uni0218', 'uni1E9E', 'uni018F', 'T', 'Tbar', 'Tcaron', 'uni0162', 'uni021A', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'uni0214', 'Udieresis', 'uni1EE4', 'Ugrave', 'uni1EE6', 'Uhorn', 'uni1EE8', 'uni1EF0', 'uni1EEA', 'uni1EEC', 'uni1EEE', 'Uhungarumlaut', 'uni0216', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'uni1EF4', 'Ygrave', 'uni1EF6', 'uni0232', 'uni1EF8', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'a', 'aacute', 'abreve', 'uni1EAF', 'uni1EB7', 'uni1EB1', 'uni1EB3', 'uni1EB5', 'acircumflex', 'uni1EA5', 'uni1EAD', 'uni1EA7', 'uni1EA9', 'uni1EAB', 'uni0201', 'adieresis', 'uni0227', 'uni1EA1', 'agrave', 'uni1EA3', 'uni0203', 'amacron', 'aogonek', 'aring', 'aringacute', 'atilde', 'ae', 'aeacute', 'b', 'c', 'cacute', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'd', 'eth', 'dcaron', 'dcroat', 'uni01C6', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'uni1EBF', 'uni1EC7', 'uni1EC1', 'uni1EC3', 'uni1EC5', 'uni0205', 'edieresis', 'edotaccent', 'uni1EB9', 'egrave', 'uni1EBB', 'uni0207', 'emacron', 'eogonek', 'uni1EBD', 'uni0259', 'f', 'g', 'gbreve', 'gcaron', 'gcircumflex', 'uni0123', 'gdotaccent', 'h', 'hbar', 'hcircumflex', 'i', 'dotlessi', 'iacute', 'ibreve', 'icircumflex', 'uni0209', 'idieresis', 'i.loclTRK', 'uni1ECB', 'igrave', 'uni1EC9', 'uni020B', 'imacron', 'iogonek', 'itilde', 'j', 'uni0237', 'jcircumflex', 'k', 'uni0137', 'kgreenlandic', 'l', 'lacute', 'lcaron', 'uni013C', 'ldot', 'uni01C9', 'lslash', 'm', 'n', 'nacute', 'ncaron', 'uni0146', 'eng', 'uni01CC', 'ntilde', 'o', 'oacute', 'obreve', 'ocircumflex', 'uni1ED1', 'uni1ED9', 'uni1ED3', 'uni1ED5', 'uni1ED7', 'uni020D', 'odieresis', 'uni022B', 'uni022F', 'uni0231', 'uni1ECD', 'ograve', 'uni1ECF', 'ohorn', 'uni1EDB', 'uni1EE3', 'uni1EDD', 'uni1EDF', 'uni1EE1', 'ohungarumlaut', 'uni020F', 'omacron', 'uni01EB', 'oslash', 'oslashacute', 'otilde', 'uni022D', 'oe', 'p', 'thorn', 'q', 'r', 'racute', 'rcaron', 'uni0157', 'uni0211', 'uni0213', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'uni0219', 'germandbls', 't', 'tbar', 'tcaron', 'uni0163', 'uni021B', 'u', 'uacute', 'ubreve', 'ucircumflex', 'uni0215', 'udieresis', 'uni1EE5', 'ugrave', 'uni1EE7', 'uhorn', 'uni1EE9', 'uni1EF1', 'uni1EEB', 'uni1EED', 'uni1EEF', 'uhungarumlaut', 'uni0217', 'umacron', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'uni1EF5', 'ygrave', 'uni1EF7', 'uni0233', 'uni1EF9', 'z', 'zacute', 'zcaron', 'zdotaccent', 'm_p_l_u_s_f_o_n_t_s', 'ordfeminine', 'ordmasculine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.lf', 'one.lf', 'two.lf', 'three.lf', 'four.lf', 'five.lf', 'six.lf', 'seven.lf', 'eight.lf', 'nine.lf', 'uni2070', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'periodcentered.loclCAT', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'hyphen', 'uni00AD', 'endash', 'emdash', 'underscore', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'space', 'uni00A0', 'uni20B5', 'cent', 'colonmonetary', 'currency', 'dollar', 'dong', 'Euro', 'florin', 'franc', 'uni20B2', 'uni20AD', 'lira', 'uni20BA', 'uni20BC', 'uni20A6', 'peseta', 'uni20B1', 'uni20BD', 'uni20B9', 'sterling', 'uni20A9', 'yen', 'uni2219', 'uni2215', 'plus', 'minus', 'multiply', 'divide', 'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal', 'plusminus', 'approxequal', 'logicalnot', 'asciitilde', 'asciicircum', 'uni00B5', 'percent', 'perthousand', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'trademark', 'degree', 'bar', 'brokenbar', 'dagger', 'daggerdbl', 'uni2116', 'uni02BC', 'uni02C9', 'dieresis', 'dotaccent', 'grave', 'acute', 'hungarumlaut', 'circumflex', 'caron', 'breve', 'ring', 'tilde', 'macron', 'cedilla', 'ogonek', 'uni20B5.BRACKET.499', 'cent.BRACKET.499', 'colonmonetary.BRACKET.234', 'dollar.BRACKET.499', 'uni20B2.BRACKET.499', 'uni20A6.BRACKET.234', 'uni20B1.BRACKET.367', 'uni20A9.BRACKET.234'] [code: mono-outliers]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni01CC	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni01CC	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class)</summary>

* [com.google.fonts/check/gdef_spacing_marks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class should be non-spacing.
Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
positioning that was only intended for building composite glyphs during design.


</pre>

* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 Ccedilla, Uogonek, ccedilla, periodcentered, uni0163 and uni01EB [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7, U+00C7, U+00E7, U+0163, U+0172 and U+01EB [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---

This test looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.

This test is not run for variable fonts, as they may legitimately have colinear
vectors.


</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* colonmonetary.BRACKET.234: L<<236.0,139.0>--<260.0,365.0>> -> L<<260.0,365.0>--<286.0,614.0>>
	* colonmonetary.BRACKET.234: L<<384.0,460.0>--<374.0,365.0>> -> L<<374.0,365.0>--<348.0,118.0>>
	* uni50CF: L<<407.0,467.0>--<550.0,467.0>> -> L<<550.0,467.0>--<552.0,467.0>>
	* uni57FA: L<<332.0,370.0>--<652.0,370.0>> -> L<<652.0,370.0>--<668.0,370.0>>
	* uni6962.jp04: L<<259.0,647.0>--<320.0,647.0>> -> L<<320.0,647.0>--<320.0,647.0>>
	* uni6BEC: L<<438.0,19.0>--<665.0,19.0>> -> L<<665.0,19.0>--<670.0,19.0>>
	* uni76EA: L<<370.0,405.0>--<370.0,405.0>> -> L<<370.0,405.0>--<371.0,405.0>>
	* uni900F: L<<304.0,622.0>--<304.0,622.0>> -> L<<304.0,622.0>--<552.0,622.0>> and uni92F2: L<<452.0,258.0>--<452.0,635.0>> -> L<<452.0,635.0>--<452.0,654.0>> [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* dollar.BRACKET.499: B<<311.0,185.0>-<311.0,192.0>-<310.0,198.0>>/L<<310.0,198.0>--<310.0,173.0>> = 9.462322208025613
	* dollar.BRACKET.499: L<<310.0,198.0>--<310.0,173.0>>/B<<310.0,173.0>-<311.0,179.0>-<311.0,185.0>> = 9.462322208025613
	* uni01CC: B<<258.0,509.0>-<293.0,488.0>-<305.0,433.0>>/L<<305.0,433.0>--<305.0,520.0>> = 12.308015817427924
	* uni20B5.BRACKET.499: B<<180.0,345.0>-<180.0,272.0>-<190.0,226.0>>/L<<190.0,226.0>--<190.0,498.0>> = 12.2647737278924
	* uni20B5.BRACKET.499: L<<190.0,226.0>--<190.0,498.0>>/B<<190.0,498.0>-<180.0,451.0>-<180.0,385.0>> = 12.01147838636543
	* uni2E90: L<<520.0,43.0>--<520.0,451.0>>/B<<520.0,451.0>-<489.0,266.0>-<385.5,128.5>> = 9.51253760227898
	* uni2F2A: L<<520.0,43.0>--<520.0,451.0>>/B<<520.0,451.0>-<489.0,266.0>-<385.5,128.5>> = 9.51253760227898
	* uni2F87: B<<265.0,600.0>-<225.0,486.0>-<171.0,388.0>>/L<<171.0,388.0>--<244.0,481.0>> = 9.274346472069261
	* uni3231: L<<232.0,-93.0>--<232.0,286.0>>/B<<232.0,286.0>-<221.0,232.0>-<207.0,185.5>> = 11.513831184487014
	* uni4EB3: B<<577.5,296.5>-<664.0,307.0>-<726.0,319.0>>/L<<726.0,319.0>--<177.0,319.0>> = 10.954062643398332 and 1105 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* uni01CA: L<<201.0,520.0>--<202.0,730.0>>
	* uni01CB: L<<201.0,520.0>--<202.0,730.0>>
	* uni5B54: L<<231.0,78.0>--<232.0,267.0>>
	* uni5B54: L<<232.0,386.0>--<233.0,525.0>>
	* uni67C4: L<<258.0,319.0>--<259.0,-93.0>>
	* uni689D: L<<94.0,-93.0>--<93.0,320.0>>
	* uni6A2A: L<<258.0,326.0>--<259.0,-93.0>>
	* uni6B05: L<<642.0,462.0>--<643.0,600.0>>
	* uni8129: L<<94.0,-93.0>--<93.0,320.0>>
	* uni8977: L<<649.0,462.0>--<650.0,600.0>> and uni8FF9: L<<779.0,460.0>--<777.0,208.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[13] MplusCode-Light.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Mplus Code Light" but got "MplusCode Light". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FULL_FONT_NAME entries.</summary>

* [com.google.fonts/check/name/fullfontname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/fullfontname)

* 🔥 **FAIL** Entry [FULL_FONT_NAME(4):WINDOWS(3)] on the "name" table: Expected "Mplus Code Light"  but got "MplusCode Light". [code: bad-entry]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicfamilyname)

* 🔥 **FAIL** Entry [TYPOGRAPHIC_FAMILY_NAME(16):WINDOWS(3)] on the "name" table: Expected "Mplus Code" but got "MplusCode". [code: non-ribbi-bad-value]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---

There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)

Requirements for monospace fonts:

* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm

* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm

* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2

* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397

Also we should report an error for glyphs not of average width.

Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave
a font a monospace flag in Panose, Microsoft Word would ignore the actual
advance widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140


</pre>

* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** On monospaced fonts, the value of OS/2.panose.bProportion must be set to 9 (proportion: monospaced), but got 0 instead. [code: mono-bad-panose-proportion]
* ⚠ **WARN** Font is monospaced but 553 glyphs (8.46%) have a different width. You should check the widths of: ['A', 'Aacute', 'Abreve', 'uni1EAE', 'uni1EB6', 'uni1EB0', 'uni1EB2', 'uni1EB4', 'Acircumflex', 'uni1EA4', 'uni1EAC', 'uni1EA6', 'uni1EA8', 'uni1EAA', 'uni0200', 'Adieresis', 'uni0226', 'uni1EA0', 'Agrave', 'uni1EA2', 'uni0202', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde', 'AE', 'AEacute', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'uni01C4', 'Eth', 'Dcaron', 'Dcroat', 'uni01C5', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'uni1EBE', 'uni1EC6', 'uni1EC0', 'uni1EC2', 'uni1EC4', 'uni0204', 'Edieresis', 'Edotaccent', 'uni1EB8', 'Egrave', 'uni1EBA', 'uni0206', 'Emacron', 'Eogonek', 'uni1EBC', 'F', 'G', 'Gbreve', 'Gcaron', 'Gcircumflex', 'uni0122', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'I', 'Iacute', 'Ibreve', 'Icircumflex', 'uni0208', 'Idieresis', 'Idotaccent', 'uni1ECA', 'Igrave', 'uni1EC8', 'uni020A', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'uni0136', 'L', 'uni01C7', 'Lacute', 'Lcaron', 'uni013B', 'Ldot', 'uni01C8', 'Lslash', 'M', 'N', 'uni01CA', 'Nacute', 'Ncaron', 'uni0145', 'Eng', 'uni01CB', 'Ntilde', 'O', 'Oacute', 'Obreve', 'Ocircumflex', 'uni1ED0', 'uni1ED8', 'uni1ED2', 'uni1ED4', 'uni1ED6', 'uni020C', 'Odieresis', 'uni022A', 'uni022E', 'uni0230', 'uni1ECC', 'Ograve', 'uni1ECE', 'Ohorn', 'uni1EDA', 'uni1EE2', 'uni1EDC', 'uni1EDE', 'uni1EE0', 'Ohungarumlaut', 'uni020E', 'Omacron', 'uni01EA', 'Oslash', 'Oslashacute', 'Otilde', 'uni022C', 'OE', 'P', 'Thorn', 'Q', 'R', 'Racute', 'Rcaron', 'uni0156', 'uni0210', 'uni0212', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'uni0218', 'uni1E9E', 'uni018F', 'T', 'Tbar', 'Tcaron', 'uni0162', 'uni021A', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'uni0214', 'Udieresis', 'uni1EE4', 'Ugrave', 'uni1EE6', 'Uhorn', 'uni1EE8', 'uni1EF0', 'uni1EEA', 'uni1EEC', 'uni1EEE', 'Uhungarumlaut', 'uni0216', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'uni1EF4', 'Ygrave', 'uni1EF6', 'uni0232', 'uni1EF8', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'a', 'aacute', 'abreve', 'uni1EAF', 'uni1EB7', 'uni1EB1', 'uni1EB3', 'uni1EB5', 'acircumflex', 'uni1EA5', 'uni1EAD', 'uni1EA7', 'uni1EA9', 'uni1EAB', 'uni0201', 'adieresis', 'uni0227', 'uni1EA1', 'agrave', 'uni1EA3', 'uni0203', 'amacron', 'aogonek', 'aring', 'aringacute', 'atilde', 'ae', 'aeacute', 'b', 'c', 'cacute', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'd', 'eth', 'dcaron', 'dcroat', 'uni01C6', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'uni1EBF', 'uni1EC7', 'uni1EC1', 'uni1EC3', 'uni1EC5', 'uni0205', 'edieresis', 'edotaccent', 'uni1EB9', 'egrave', 'uni1EBB', 'uni0207', 'emacron', 'eogonek', 'uni1EBD', 'uni0259', 'f', 'g', 'gbreve', 'gcaron', 'gcircumflex', 'uni0123', 'gdotaccent', 'h', 'hbar', 'hcircumflex', 'i', 'dotlessi', 'iacute', 'ibreve', 'icircumflex', 'uni0209', 'idieresis', 'i.loclTRK', 'uni1ECB', 'igrave', 'uni1EC9', 'uni020B', 'imacron', 'iogonek', 'itilde', 'j', 'uni0237', 'jcircumflex', 'k', 'uni0137', 'kgreenlandic', 'l', 'lacute', 'lcaron', 'uni013C', 'ldot', 'uni01C9', 'lslash', 'm', 'n', 'nacute', 'ncaron', 'uni0146', 'eng', 'uni01CC', 'ntilde', 'o', 'oacute', 'obreve', 'ocircumflex', 'uni1ED1', 'uni1ED9', 'uni1ED3', 'uni1ED5', 'uni1ED7', 'uni020D', 'odieresis', 'uni022B', 'uni022F', 'uni0231', 'uni1ECD', 'ograve', 'uni1ECF', 'ohorn', 'uni1EDB', 'uni1EE3', 'uni1EDD', 'uni1EDF', 'uni1EE1', 'ohungarumlaut', 'uni020F', 'omacron', 'uni01EB', 'oslash', 'oslashacute', 'otilde', 'uni022D', 'oe', 'p', 'thorn', 'q', 'r', 'racute', 'rcaron', 'uni0157', 'uni0211', 'uni0213', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'uni0219', 'germandbls', 't', 'tbar', 'tcaron', 'uni0163', 'uni021B', 'u', 'uacute', 'ubreve', 'ucircumflex', 'uni0215', 'udieresis', 'uni1EE5', 'ugrave', 'uni1EE7', 'uhorn', 'uni1EE9', 'uni1EF1', 'uni1EEB', 'uni1EED', 'uni1EEF', 'uhungarumlaut', 'uni0217', 'umacron', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'uni1EF5', 'ygrave', 'uni1EF7', 'uni0233', 'uni1EF9', 'z', 'zacute', 'zcaron', 'zdotaccent', 'm_p_l_u_s_f_o_n_t_s', 'ordfeminine', 'ordmasculine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.lf', 'one.lf', 'two.lf', 'three.lf', 'four.lf', 'five.lf', 'six.lf', 'seven.lf', 'eight.lf', 'nine.lf', 'uni2070', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'periodcentered.loclCAT', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'hyphen', 'uni00AD', 'endash', 'emdash', 'underscore', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'space', 'uni00A0', 'uni20B5', 'cent', 'colonmonetary', 'currency', 'dollar', 'dong', 'Euro', 'florin', 'franc', 'uni20B2', 'uni20AD', 'lira', 'uni20BA', 'uni20BC', 'uni20A6', 'peseta', 'uni20B1', 'uni20BD', 'uni20B9', 'sterling', 'uni20A9', 'yen', 'uni2219', 'uni2215', 'plus', 'minus', 'multiply', 'divide', 'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal', 'plusminus', 'approxequal', 'logicalnot', 'asciitilde', 'asciicircum', 'uni00B5', 'percent', 'perthousand', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'trademark', 'degree', 'bar', 'brokenbar', 'dagger', 'daggerdbl', 'uni2116', 'uni02BC', 'uni02C9', 'dieresis', 'dotaccent', 'grave', 'acute', 'hungarumlaut', 'circumflex', 'caron', 'breve', 'ring', 'tilde', 'macron', 'cedilla', 'ogonek', 'uni20B5.BRACKET.499', 'cent.BRACKET.499', 'colonmonetary.BRACKET.234', 'dollar.BRACKET.499', 'uni20B2.BRACKET.499', 'uni20A6.BRACKET.234', 'uni20B1.BRACKET.367', 'uni20A9.BRACKET.234'] [code: mono-outliers]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class)</summary>

* [com.google.fonts/check/gdef_spacing_marks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class should be non-spacing.
Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
positioning that was only intended for building composite glyphs during design.


</pre>

* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 Ccedilla, Uogonek, ccedilla, periodcentered, uni0163 and uni01EB [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7, U+00C7, U+00E7, U+0163, U+0172 and U+01EB [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---

This test looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.

This test is not run for variable fonts, as they may legitimately have colinear
vectors.


</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* colonmonetary: L<<144.0,129.0>--<169.0,365.0>> -> L<<169.0,365.0>--<201.0,668.0>>
	* colonmonetary: L<<248.0,688.0>--<214.0,365.0>> -> L<<214.0,365.0>--<184.0,80.0>>
	* colonmonetary: L<<362.0,684.0>--<329.0,365.0>> -> L<<329.0,365.0>--<295.0,37.0>>
	* uni4F0E: L<<143.0,549.0>--<143.0,549.0>> -> L<<143.0,549.0>--<143.0,549.0>>
	* uni4F11: L<<143.0,549.0>--<143.0,549.0>> -> L<<143.0,549.0>--<143.0,549.0>>
	* uni5099.BRACKET.620: L<<312.0,523.0>--<312.0,491.0>> -> L<<312.0,491.0>--<316.0,354.0>>
	* uni5436: L<<111.0,703.0>--<111.0,69.0>> -> L<<111.0,69.0>--<111.0,67.0>>
	* uni5436: L<<623.0,643.0>--<623.0,647.0>> -> L<<623.0,647.0>--<623.0,765.0>>
	* uni545F: L<<119.0,703.0>--<119.0,134.0>> -> L<<119.0,134.0>--<119.0,67.0>>
	* uni5471: L<<119.0,703.0>--<119.0,92.0>> -> L<<119.0,92.0>--<119.0,72.0>> and 19 more. [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* sohira: B<<469.5,471.0>-<368.0,422.0>-<261.0,388.0>>/L<<261.0,388.0>--<903.0,441.0>> = 12.908695661948286
	* trademark: L<<316.0,445.0>--<270.0,659.0>>/L<<270.0,659.0>--<273.0,375.0>> = 11.526106469387715
	* trademark: L<<396.0,375.0>--<399.0,660.0>>/L<<399.0,660.0>--<352.0,445.0>> = 11.728048271607536
	* uni2FC6: L<<475.0,700.0>--<265.0,700.0>>/L<<265.0,700.0>--<311.0,694.0>> = 7.431407971172489
	* uni3231: L<<225.0,-83.0>--<225.0,450.0>>/B<<225.0,450.0>-<192.0,290.0>-<130.0,146.0>> = 11.653840585834315
	* uni4E6D: B<<437.0,216.0>-<540.0,251.0>-<652.0,278.0>>/L<<652.0,278.0>--<109.0,278.0>> = 13.553764097731639
	* uni4E9F: L<<371.0,556.0>--<371.0,545.0>>/B<<371.0,545.0>-<379.0,588.0>-<385.5,633.0>> = 10.539183728628242
	* uni50FB: L<<270.0,-74.0>--<270.0,209.0>>/B<<270.0,209.0>-<260.0,147.0>-<245.0,90.0>> = 9.162347045721706
	* uni513A: L<<216.0,693.0>--<216.0,714.0>>/B<<216.0,714.0>-<191.0,612.0>-<153.0,520.0>> = 13.771599717082417
	* uni51DD: B<<321.0,482.0>-<301.0,482.0>-<285.0,483.0>>/L<<285.0,483.0>--<316.0,473.0>> = 14.302362220843962 and 206 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* M: L<<406.0,0.0>--<407.0,659.0>>
	* M: L<<93.0,659.0>--<94.0,0.0>>
	* asterisk: L<<229.0,568.0>--<228.0,753.0>>
	* asterisk: L<<272.0,753.0>--<271.0,568.0>>
	* uni5B54: L<<267.0,47.0>--<268.0,324.0>>
	* uni6643: L<<361.0,214.0>--<70.0,215.0>>
	* uni689D: L<<116.0,-83.0>--<115.0,440.0>>
	* uni8129: L<<116.0,-83.0>--<115.0,440.0>>
	* uni8FF9: L<<741.0,662.0>--<740.0,160.0>>
	* uni966A: L<<130.0,734.0>--<132.0,-75.0>> and 3 more. [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[13] MplusCode-Medium.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Mplus Code Medium" but got "MplusCode Medium". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FULL_FONT_NAME entries.</summary>

* [com.google.fonts/check/name/fullfontname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/fullfontname)

* 🔥 **FAIL** Entry [FULL_FONT_NAME(4):WINDOWS(3)] on the "name" table: Expected "Mplus Code Medium"  but got "MplusCode Medium". [code: bad-entry]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicfamilyname)

* 🔥 **FAIL** Entry [TYPOGRAPHIC_FAMILY_NAME(16):WINDOWS(3)] on the "name" table: Expected "Mplus Code" but got "MplusCode". [code: non-ribbi-bad-value]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---

There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)

Requirements for monospace fonts:

* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm

* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm

* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2

* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397

Also we should report an error for glyphs not of average width.

Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave
a font a monospace flag in Panose, Microsoft Word would ignore the actual
advance widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140


</pre>

* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** On monospaced fonts, the value of OS/2.panose.bProportion must be set to 9 (proportion: monospaced), but got 0 instead. [code: mono-bad-panose-proportion]
* ⚠ **WARN** Font is monospaced but 553 glyphs (8.46%) have a different width. You should check the widths of: ['A', 'Aacute', 'Abreve', 'uni1EAE', 'uni1EB6', 'uni1EB0', 'uni1EB2', 'uni1EB4', 'Acircumflex', 'uni1EA4', 'uni1EAC', 'uni1EA6', 'uni1EA8', 'uni1EAA', 'uni0200', 'Adieresis', 'uni0226', 'uni1EA0', 'Agrave', 'uni1EA2', 'uni0202', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde', 'AE', 'AEacute', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'uni01C4', 'Eth', 'Dcaron', 'Dcroat', 'uni01C5', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'uni1EBE', 'uni1EC6', 'uni1EC0', 'uni1EC2', 'uni1EC4', 'uni0204', 'Edieresis', 'Edotaccent', 'uni1EB8', 'Egrave', 'uni1EBA', 'uni0206', 'Emacron', 'Eogonek', 'uni1EBC', 'F', 'G', 'Gbreve', 'Gcaron', 'Gcircumflex', 'uni0122', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'I', 'Iacute', 'Ibreve', 'Icircumflex', 'uni0208', 'Idieresis', 'Idotaccent', 'uni1ECA', 'Igrave', 'uni1EC8', 'uni020A', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'uni0136', 'L', 'uni01C7', 'Lacute', 'Lcaron', 'uni013B', 'Ldot', 'uni01C8', 'Lslash', 'M', 'N', 'uni01CA', 'Nacute', 'Ncaron', 'uni0145', 'Eng', 'uni01CB', 'Ntilde', 'O', 'Oacute', 'Obreve', 'Ocircumflex', 'uni1ED0', 'uni1ED8', 'uni1ED2', 'uni1ED4', 'uni1ED6', 'uni020C', 'Odieresis', 'uni022A', 'uni022E', 'uni0230', 'uni1ECC', 'Ograve', 'uni1ECE', 'Ohorn', 'uni1EDA', 'uni1EE2', 'uni1EDC', 'uni1EDE', 'uni1EE0', 'Ohungarumlaut', 'uni020E', 'Omacron', 'uni01EA', 'Oslash', 'Oslashacute', 'Otilde', 'uni022C', 'OE', 'P', 'Thorn', 'Q', 'R', 'Racute', 'Rcaron', 'uni0156', 'uni0210', 'uni0212', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'uni0218', 'uni1E9E', 'uni018F', 'T', 'Tbar', 'Tcaron', 'uni0162', 'uni021A', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'uni0214', 'Udieresis', 'uni1EE4', 'Ugrave', 'uni1EE6', 'Uhorn', 'uni1EE8', 'uni1EF0', 'uni1EEA', 'uni1EEC', 'uni1EEE', 'Uhungarumlaut', 'uni0216', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'uni1EF4', 'Ygrave', 'uni1EF6', 'uni0232', 'uni1EF8', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'a', 'aacute', 'abreve', 'uni1EAF', 'uni1EB7', 'uni1EB1', 'uni1EB3', 'uni1EB5', 'acircumflex', 'uni1EA5', 'uni1EAD', 'uni1EA7', 'uni1EA9', 'uni1EAB', 'uni0201', 'adieresis', 'uni0227', 'uni1EA1', 'agrave', 'uni1EA3', 'uni0203', 'amacron', 'aogonek', 'aring', 'aringacute', 'atilde', 'ae', 'aeacute', 'b', 'c', 'cacute', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'd', 'eth', 'dcaron', 'dcroat', 'uni01C6', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'uni1EBF', 'uni1EC7', 'uni1EC1', 'uni1EC3', 'uni1EC5', 'uni0205', 'edieresis', 'edotaccent', 'uni1EB9', 'egrave', 'uni1EBB', 'uni0207', 'emacron', 'eogonek', 'uni1EBD', 'uni0259', 'f', 'g', 'gbreve', 'gcaron', 'gcircumflex', 'uni0123', 'gdotaccent', 'h', 'hbar', 'hcircumflex', 'i', 'dotlessi', 'iacute', 'ibreve', 'icircumflex', 'uni0209', 'idieresis', 'i.loclTRK', 'uni1ECB', 'igrave', 'uni1EC9', 'uni020B', 'imacron', 'iogonek', 'itilde', 'j', 'uni0237', 'jcircumflex', 'k', 'uni0137', 'kgreenlandic', 'l', 'lacute', 'lcaron', 'uni013C', 'ldot', 'uni01C9', 'lslash', 'm', 'n', 'nacute', 'ncaron', 'uni0146', 'eng', 'uni01CC', 'ntilde', 'o', 'oacute', 'obreve', 'ocircumflex', 'uni1ED1', 'uni1ED9', 'uni1ED3', 'uni1ED5', 'uni1ED7', 'uni020D', 'odieresis', 'uni022B', 'uni022F', 'uni0231', 'uni1ECD', 'ograve', 'uni1ECF', 'ohorn', 'uni1EDB', 'uni1EE3', 'uni1EDD', 'uni1EDF', 'uni1EE1', 'ohungarumlaut', 'uni020F', 'omacron', 'uni01EB', 'oslash', 'oslashacute', 'otilde', 'uni022D', 'oe', 'p', 'thorn', 'q', 'r', 'racute', 'rcaron', 'uni0157', 'uni0211', 'uni0213', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'uni0219', 'germandbls', 't', 'tbar', 'tcaron', 'uni0163', 'uni021B', 'u', 'uacute', 'ubreve', 'ucircumflex', 'uni0215', 'udieresis', 'uni1EE5', 'ugrave', 'uni1EE7', 'uhorn', 'uni1EE9', 'uni1EF1', 'uni1EEB', 'uni1EED', 'uni1EEF', 'uhungarumlaut', 'uni0217', 'umacron', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'uni1EF5', 'ygrave', 'uni1EF7', 'uni0233', 'uni1EF9', 'z', 'zacute', 'zcaron', 'zdotaccent', 'm_p_l_u_s_f_o_n_t_s', 'ordfeminine', 'ordmasculine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.lf', 'one.lf', 'two.lf', 'three.lf', 'four.lf', 'five.lf', 'six.lf', 'seven.lf', 'eight.lf', 'nine.lf', 'uni2070', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'periodcentered.loclCAT', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'hyphen', 'uni00AD', 'endash', 'emdash', 'underscore', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'space', 'uni00A0', 'uni20B5', 'cent', 'colonmonetary', 'currency', 'dollar', 'dong', 'Euro', 'florin', 'franc', 'uni20B2', 'uni20AD', 'lira', 'uni20BA', 'uni20BC', 'uni20A6', 'peseta', 'uni20B1', 'uni20BD', 'uni20B9', 'sterling', 'uni20A9', 'yen', 'uni2219', 'uni2215', 'plus', 'minus', 'multiply', 'divide', 'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal', 'plusminus', 'approxequal', 'logicalnot', 'asciitilde', 'asciicircum', 'uni00B5', 'percent', 'perthousand', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'trademark', 'degree', 'bar', 'brokenbar', 'dagger', 'daggerdbl', 'uni2116', 'uni02BC', 'uni02C9', 'dieresis', 'dotaccent', 'grave', 'acute', 'hungarumlaut', 'circumflex', 'caron', 'breve', 'ring', 'tilde', 'macron', 'cedilla', 'ogonek', 'uni20B5.BRACKET.499', 'cent.BRACKET.499', 'colonmonetary.BRACKET.234', 'dollar.BRACKET.499', 'uni20B2.BRACKET.499', 'uni20A6.BRACKET.234', 'uni20B1.BRACKET.367', 'uni20A9.BRACKET.234'] [code: mono-outliers]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class)</summary>

* [com.google.fonts/check/gdef_spacing_marks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class should be non-spacing.
Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
positioning that was only intended for building composite glyphs during design.


</pre>

* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 Ccedilla, Uogonek, ccedilla, periodcentered, uni0163 and uni01EB [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7, U+00C7, U+00E7, U+0163, U+0172 and U+01EB [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---

This test looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.

This test is not run for variable fonts, as they may legitimately have colinear
vectors.


</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* colonmonetary.BRACKET.234: L<<240.0,106.0>--<267.0,365.0>> -> L<<267.0,365.0>--<296.0,641.0>>
	* colonmonetary.BRACKET.234: L<<259.0,636.0>--<231.0,365.0>> -> L<<231.0,365.0>--<207.0,132.0>>
	* colonmonetary.BRACKET.234: L<<369.0,465.0>--<359.0,365.0>> -> L<<359.0,365.0>--<330.0,89.0>>
	* uni2F46: L<<610.0,340.0>--<610.0,60.0>> -> L<<610.0,60.0>--<610.0,59.0>>
	* uni5099.BRACKET.620: L<<367.0,492.0>--<367.0,404.0>> -> L<<367.0,404.0>--<371.0,362.0>>
	* uni5429: L<<155.0,16.0>--<156.0,6.0>> -> L<<156.0,6.0>--<156.0,-44.0>>
	* uni545F: L<<152.0,670.0>--<152.0,112.0>> -> L<<152.0,112.0>--<152.0,99.0>>
	* uni5BC7: L<<427.0,311.0>--<427.0,51.0>> -> L<<427.0,51.0>--<427.0,50.0>>
	* uni6173: L<<544.0,370.0>--<620.0,370.0>> -> L<<620.0,370.0>--<620.0,370.0>>
	* uni65E0: L<<610.0,340.0>--<610.0,60.0>> -> L<<610.0,60.0>--<610.0,59.0>> and 7 more. [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* gehira: B<<768.0,648.0>-<762.0,685.0>-<754.0,717.0>>/L<<754.0,717.0>--<754.0,578.0>> = 14.036243467926484
	* pahira: B<<727.0,622.0>-<725.0,626.0>-<724.0,631.0>>/L<<724.0,631.0>--<724.0,622.0>> = 11.309932474020195
	* uni2FC9: L<<411.0,164.0>--<377.0,134.0>>/B<<377.0,134.0>-<378.0,135.0>-<380.0,136.0>> = 3.5763343749973706
	* uni2FD2: L<<628.0,251.0>--<400.0,251.0>>/L<<400.0,251.0>--<416.0,247.0>> = 14.036243467926484
	* uni2FD2: L<<628.0,558.0>--<396.0,558.0>>/L<<396.0,558.0>--<416.0,553.0>> = 14.036243467926484
	* uni2FD2: L<<819.0,251.0>--<700.0,251.0>>/L<<700.0,251.0>--<717.0,247.0>> = 13.24051991518721
	* uni2FD2: L<<945.0,558.0>--<697.0,558.0>>/L<<697.0,558.0>--<717.0,553.0>> = 14.036243467926484
	* uni3231: L<<229.0,-90.0>--<229.0,331.0>>/B<<229.0,331.0>-<204.0,211.0>-<164.0,116.0>> = 11.768288932020628
	* uni4EB3: B<<622.0,301.0>-<716.0,314.0>-<781.0,329.0>>/L<<781.0,329.0>--<158.0,329.0>> = 12.994616791916512
	* uni4F8B: B<<411.0,494.0>-<388.0,416.0>-<356.0,347.0>>/L<<356.0,347.0>--<381.0,392.0>> = 4.1742372398952705 and 828 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* uni5B54: L<<243.0,69.0>--<244.0,286.0>>
	* uni5B54: L<<244.0,382.0>--<245.0,523.0>>
	* uni6212: L<<264.0,570.0>--<263.0,400.0>>
	* uni6643: L<<324.0,195.0>--<60.0,196.0>>
	* uni67C4: L<<246.0,366.0>--<247.0,-90.0>>
	* uni689D: L<<101.0,-90.0>--<100.0,352.0>>
	* uni6A2A: L<<246.0,371.0>--<247.0,-90.0>>
	* uni8129: L<<101.0,-90.0>--<100.0,352.0>>
	* uni8FF9: L<<768.0,518.0>--<766.0,192.0>>
	* uni907D: L<<395.0,624.0>--<394.0,460.0>>
	* uni966A: L<<167.0,704.0>--<169.0,-85.0>> and uni966A: L<<72.0,-85.0>--<70.0,785.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[12] MplusCode-Regular.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Mplus Code" but got "MplusCode". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FULL_FONT_NAME entries.</summary>

* [com.google.fonts/check/name/fullfontname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/fullfontname)

* 🔥 **FAIL** Entry [FULL_FONT_NAME(4):WINDOWS(3)] on the "name" table: Expected "Mplus Code Regular"  but got "MplusCode Regular". [code: bad-entry]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---

There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)

Requirements for monospace fonts:

* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm

* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm

* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2

* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397

Also we should report an error for glyphs not of average width.

Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave
a font a monospace flag in Panose, Microsoft Word would ignore the actual
advance widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140


</pre>

* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** On monospaced fonts, the value of OS/2.panose.bProportion must be set to 9 (proportion: monospaced), but got 0 instead. [code: mono-bad-panose-proportion]
* ⚠ **WARN** Font is monospaced but 553 glyphs (8.46%) have a different width. You should check the widths of: ['A', 'Aacute', 'Abreve', 'uni1EAE', 'uni1EB6', 'uni1EB0', 'uni1EB2', 'uni1EB4', 'Acircumflex', 'uni1EA4', 'uni1EAC', 'uni1EA6', 'uni1EA8', 'uni1EAA', 'uni0200', 'Adieresis', 'uni0226', 'uni1EA0', 'Agrave', 'uni1EA2', 'uni0202', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde', 'AE', 'AEacute', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'uni01C4', 'Eth', 'Dcaron', 'Dcroat', 'uni01C5', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'uni1EBE', 'uni1EC6', 'uni1EC0', 'uni1EC2', 'uni1EC4', 'uni0204', 'Edieresis', 'Edotaccent', 'uni1EB8', 'Egrave', 'uni1EBA', 'uni0206', 'Emacron', 'Eogonek', 'uni1EBC', 'F', 'G', 'Gbreve', 'Gcaron', 'Gcircumflex', 'uni0122', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'I', 'Iacute', 'Ibreve', 'Icircumflex', 'uni0208', 'Idieresis', 'Idotaccent', 'uni1ECA', 'Igrave', 'uni1EC8', 'uni020A', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'uni0136', 'L', 'uni01C7', 'Lacute', 'Lcaron', 'uni013B', 'Ldot', 'uni01C8', 'Lslash', 'M', 'N', 'uni01CA', 'Nacute', 'Ncaron', 'uni0145', 'Eng', 'uni01CB', 'Ntilde', 'O', 'Oacute', 'Obreve', 'Ocircumflex', 'uni1ED0', 'uni1ED8', 'uni1ED2', 'uni1ED4', 'uni1ED6', 'uni020C', 'Odieresis', 'uni022A', 'uni022E', 'uni0230', 'uni1ECC', 'Ograve', 'uni1ECE', 'Ohorn', 'uni1EDA', 'uni1EE2', 'uni1EDC', 'uni1EDE', 'uni1EE0', 'Ohungarumlaut', 'uni020E', 'Omacron', 'uni01EA', 'Oslash', 'Oslashacute', 'Otilde', 'uni022C', 'OE', 'P', 'Thorn', 'Q', 'R', 'Racute', 'Rcaron', 'uni0156', 'uni0210', 'uni0212', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'uni0218', 'uni1E9E', 'uni018F', 'T', 'Tbar', 'Tcaron', 'uni0162', 'uni021A', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'uni0214', 'Udieresis', 'uni1EE4', 'Ugrave', 'uni1EE6', 'Uhorn', 'uni1EE8', 'uni1EF0', 'uni1EEA', 'uni1EEC', 'uni1EEE', 'Uhungarumlaut', 'uni0216', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'uni1EF4', 'Ygrave', 'uni1EF6', 'uni0232', 'uni1EF8', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'a', 'aacute', 'abreve', 'uni1EAF', 'uni1EB7', 'uni1EB1', 'uni1EB3', 'uni1EB5', 'acircumflex', 'uni1EA5', 'uni1EAD', 'uni1EA7', 'uni1EA9', 'uni1EAB', 'uni0201', 'adieresis', 'uni0227', 'uni1EA1', 'agrave', 'uni1EA3', 'uni0203', 'amacron', 'aogonek', 'aring', 'aringacute', 'atilde', 'ae', 'aeacute', 'b', 'c', 'cacute', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'd', 'eth', 'dcaron', 'dcroat', 'uni01C6', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'uni1EBF', 'uni1EC7', 'uni1EC1', 'uni1EC3', 'uni1EC5', 'uni0205', 'edieresis', 'edotaccent', 'uni1EB9', 'egrave', 'uni1EBB', 'uni0207', 'emacron', 'eogonek', 'uni1EBD', 'uni0259', 'f', 'g', 'gbreve', 'gcaron', 'gcircumflex', 'uni0123', 'gdotaccent', 'h', 'hbar', 'hcircumflex', 'i', 'dotlessi', 'iacute', 'ibreve', 'icircumflex', 'uni0209', 'idieresis', 'i.loclTRK', 'uni1ECB', 'igrave', 'uni1EC9', 'uni020B', 'imacron', 'iogonek', 'itilde', 'j', 'uni0237', 'jcircumflex', 'k', 'uni0137', 'kgreenlandic', 'l', 'lacute', 'lcaron', 'uni013C', 'ldot', 'uni01C9', 'lslash', 'm', 'n', 'nacute', 'ncaron', 'uni0146', 'eng', 'uni01CC', 'ntilde', 'o', 'oacute', 'obreve', 'ocircumflex', 'uni1ED1', 'uni1ED9', 'uni1ED3', 'uni1ED5', 'uni1ED7', 'uni020D', 'odieresis', 'uni022B', 'uni022F', 'uni0231', 'uni1ECD', 'ograve', 'uni1ECF', 'ohorn', 'uni1EDB', 'uni1EE3', 'uni1EDD', 'uni1EDF', 'uni1EE1', 'ohungarumlaut', 'uni020F', 'omacron', 'uni01EB', 'oslash', 'oslashacute', 'otilde', 'uni022D', 'oe', 'p', 'thorn', 'q', 'r', 'racute', 'rcaron', 'uni0157', 'uni0211', 'uni0213', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'uni0219', 'germandbls', 't', 'tbar', 'tcaron', 'uni0163', 'uni021B', 'u', 'uacute', 'ubreve', 'ucircumflex', 'uni0215', 'udieresis', 'uni1EE5', 'ugrave', 'uni1EE7', 'uhorn', 'uni1EE9', 'uni1EF1', 'uni1EEB', 'uni1EED', 'uni1EEF', 'uhungarumlaut', 'uni0217', 'umacron', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'uni1EF5', 'ygrave', 'uni1EF7', 'uni0233', 'uni1EF9', 'z', 'zacute', 'zcaron', 'zdotaccent', 'm_p_l_u_s_f_o_n_t_s', 'ordfeminine', 'ordmasculine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.lf', 'one.lf', 'two.lf', 'three.lf', 'four.lf', 'five.lf', 'six.lf', 'seven.lf', 'eight.lf', 'nine.lf', 'uni2070', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'periodcentered.loclCAT', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'hyphen', 'uni00AD', 'endash', 'emdash', 'underscore', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'space', 'uni00A0', 'uni20B5', 'cent', 'colonmonetary', 'currency', 'dollar', 'dong', 'Euro', 'florin', 'franc', 'uni20B2', 'uni20AD', 'lira', 'uni20BA', 'uni20BC', 'uni20A6', 'peseta', 'uni20B1', 'uni20BD', 'uni20B9', 'sterling', 'uni20A9', 'yen', 'uni2219', 'uni2215', 'plus', 'minus', 'multiply', 'divide', 'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal', 'plusminus', 'approxequal', 'logicalnot', 'asciitilde', 'asciicircum', 'uni00B5', 'percent', 'perthousand', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'trademark', 'degree', 'bar', 'brokenbar', 'dagger', 'daggerdbl', 'uni2116', 'uni02BC', 'uni02C9', 'dieresis', 'dotaccent', 'grave', 'acute', 'hungarumlaut', 'circumflex', 'caron', 'breve', 'ring', 'tilde', 'macron', 'cedilla', 'ogonek', 'uni20B5.BRACKET.499', 'cent.BRACKET.499', 'colonmonetary.BRACKET.234', 'dollar.BRACKET.499', 'uni20B2.BRACKET.499', 'uni20A6.BRACKET.234', 'uni20B1.BRACKET.367', 'uni20A9.BRACKET.234'] [code: mono-outliers]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class)</summary>

* [com.google.fonts/check/gdef_spacing_marks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class should be non-spacing.
Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
positioning that was only intended for building composite glyphs during design.


</pre>

* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 Ccedilla, Uogonek, ccedilla, periodcentered, uni0163 and uni01EB [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7, U+00C7, U+00E7, U+0163, U+0172 and U+01EB [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---

This test looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.

This test is not run for variable fonts, as they may legitimately have colinear
vectors.


</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* colonmonetary.BRACKET.234: L<<146.0,194.0>--<164.0,365.0>> -> L<<164.0,365.0>--<191.0,624.0>>
	* colonmonetary.BRACKET.234: L<<244.0,75.0>--<274.0,365.0>> -> L<<274.0,365.0>--<306.0,668.0>>
	* colonmonetary.BRACKET.234: L<<265.0,665.0>--<234.0,365.0>> -> L<<234.0,365.0>--<206.0,96.0>>
	* colonmonetary.BRACKET.234: L<<355.0,470.0>--<344.0,365.0>> -> L<<344.0,365.0>--<312.0,62.0>>
	* uni4EAB: L<<552.0,179.0>--<552.0,179.0>> -> L<<552.0,179.0>--<957.0,179.0>>
	* uni5099.BRACKET.620: L<<339.0,505.0>--<339.0,441.0>> -> L<<339.0,441.0>--<347.0,358.0>>
	* uni545F: L<<139.0,685.0>--<139.0,130.0>> -> L<<139.0,130.0>--<139.0,84.0>>
	* uni559D: L<<503.0,146.0>--<503.0,115.0>> -> L<<503.0,115.0>--<503.0,114.0>>
	* uni56CE: L<<775.0,603.0>--<775.0,439.0>> -> L<<775.0,439.0>--<775.0,399.0>>
	* uni5BC7: L<<412.0,330.0>--<412.0,43.0>> -> L<<412.0,43.0>--<412.0,42.0>> and 7 more. [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* uni2FAA: L<<359.0,186.0>--<317.0,143.0>>/B<<317.0,143.0>-<365.0,175.0>-<404.0,206.0>> = 11.983969372004685
	* uni2FB6: L<<889.0,493.0>--<911.0,486.0>>/B<<911.0,486.0>-<836.0,532.0>-<737.0,573.0>> = 13.872053026828576
	* uni2FB6: L<<903.0,96.0>--<914.0,93.0>>/B<<914.0,93.0>-<879.0,111.0>-<837.0,129.5>> = 11.960992854249666
	* uni2FC1: L<<877.0,298.0>--<731.0,298.0>>/L<<731.0,298.0>--<763.0,293.0>> = 8.880659150520234
	* uni2FD2: L<<645.0,260.0>--<347.0,260.0>>/L<<347.0,260.0>--<400.0,248.0>> = 12.757532160876671
	* uni2FD2: L<<645.0,572.0>--<346.0,572.0>>/L<<346.0,572.0>--<400.0,559.0>> = 13.535856369134248
	* uni2FD2: L<<835.0,260.0>--<659.0,260.0>>/L<<659.0,260.0>--<713.0,248.0>> = 12.52880770915152
	* uni2FD2: L<<940.0,572.0>--<659.0,572.0>>/L<<659.0,572.0>--<713.0,559.0>> = 13.535856369134248
	* uni3231: L<<226.0,-87.0>--<226.0,375.0>>/B<<226.0,375.0>-<197.0,240.0>-<150.0,131.0>> = 12.123738247789403
	* uni4FA1: L<<272.0,703.0>--<272.0,770.0>>/B<<272.0,770.0>-<260.0,709.0>-<242.5,652.5>> = 11.129189289611167 and 481 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* uni5B54: L<<254.0,59.0>--<255.0,304.0>>
	* uni5B54: L<<255.0,376.0>--<256.0,520.0>>
	* uni6643: L<<342.0,204.0>--<65.0,205.0>>
	* uni6643: L<<572.0,203.0>--<419.0,204.0>>
	* uni67C4: L<<233.0,414.0>--<234.0,-87.0>>
	* uni689D: L<<107.0,-87.0>--<105.0,385.0>>
	* uni6A2A: L<<233.0,418.0>--<234.0,-87.0>>
	* uni8129: L<<107.0,-87.0>--<105.0,385.0>>
	* uni8FF9: L<<757.0,648.0>--<755.0,176.0>>
	* uni907D: L<<373.0,635.0>--<372.0,473.0>>
	* uni966A: L<<150.0,718.0>--<154.0,-80.0>> and uni966A: L<<80.0,-80.0>--<76.0,780.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[13] MplusCode-Thin.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---

Checks that the family name infered from the font filename matches the string
at nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise
checks that nameID 1 is the family name + the style name.


</pre>

* 🔥 **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the "name" table: Expected "Mplus Code Thin" but got "MplusCode Thin". [code: mismatch]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FULL_FONT_NAME entries.</summary>

* [com.google.fonts/check/name/fullfontname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/fullfontname)

* 🔥 **FAIL** Entry [FULL_FONT_NAME(4):WINDOWS(3)] on the "name" table: Expected "Mplus Code Thin"  but got "MplusCode Thin". [code: bad-entry]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicfamilyname)

* 🔥 **FAIL** Entry [TYPOGRAPHIC_FAMILY_NAME(16):WINDOWS(3)] on the "name" table: Expected "Mplus Code" but got "MplusCode". [code: non-ribbi-bad-value]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---

There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)

Requirements for monospace fonts:

* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm

* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm

* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2

* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397

Also we should report an error for glyphs not of average width.

Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave
a font a monospace flag in Panose, Microsoft Word would ignore the actual
advance widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140


</pre>

* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** On monospaced fonts, the value of OS/2.panose.bProportion must be set to 9 (proportion: monospaced), but got 0 instead. [code: mono-bad-panose-proportion]
* ⚠ **WARN** Font is monospaced but 553 glyphs (8.46%) have a different width. You should check the widths of: ['A', 'Aacute', 'Abreve', 'uni1EAE', 'uni1EB6', 'uni1EB0', 'uni1EB2', 'uni1EB4', 'Acircumflex', 'uni1EA4', 'uni1EAC', 'uni1EA6', 'uni1EA8', 'uni1EAA', 'uni0200', 'Adieresis', 'uni0226', 'uni1EA0', 'Agrave', 'uni1EA2', 'uni0202', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde', 'AE', 'AEacute', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'uni01C4', 'Eth', 'Dcaron', 'Dcroat', 'uni01C5', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'uni1EBE', 'uni1EC6', 'uni1EC0', 'uni1EC2', 'uni1EC4', 'uni0204', 'Edieresis', 'Edotaccent', 'uni1EB8', 'Egrave', 'uni1EBA', 'uni0206', 'Emacron', 'Eogonek', 'uni1EBC', 'F', 'G', 'Gbreve', 'Gcaron', 'Gcircumflex', 'uni0122', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'I', 'Iacute', 'Ibreve', 'Icircumflex', 'uni0208', 'Idieresis', 'Idotaccent', 'uni1ECA', 'Igrave', 'uni1EC8', 'uni020A', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'uni0136', 'L', 'uni01C7', 'Lacute', 'Lcaron', 'uni013B', 'Ldot', 'uni01C8', 'Lslash', 'M', 'N', 'uni01CA', 'Nacute', 'Ncaron', 'uni0145', 'Eng', 'uni01CB', 'Ntilde', 'O', 'Oacute', 'Obreve', 'Ocircumflex', 'uni1ED0', 'uni1ED8', 'uni1ED2', 'uni1ED4', 'uni1ED6', 'uni020C', 'Odieresis', 'uni022A', 'uni022E', 'uni0230', 'uni1ECC', 'Ograve', 'uni1ECE', 'Ohorn', 'uni1EDA', 'uni1EE2', 'uni1EDC', 'uni1EDE', 'uni1EE0', 'Ohungarumlaut', 'uni020E', 'Omacron', 'uni01EA', 'Oslash', 'Oslashacute', 'Otilde', 'uni022C', 'OE', 'P', 'Thorn', 'Q', 'R', 'Racute', 'Rcaron', 'uni0156', 'uni0210', 'uni0212', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'uni0218', 'uni1E9E', 'uni018F', 'T', 'Tbar', 'Tcaron', 'uni0162', 'uni021A', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'uni0214', 'Udieresis', 'uni1EE4', 'Ugrave', 'uni1EE6', 'Uhorn', 'uni1EE8', 'uni1EF0', 'uni1EEA', 'uni1EEC', 'uni1EEE', 'Uhungarumlaut', 'uni0216', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'uni1EF4', 'Ygrave', 'uni1EF6', 'uni0232', 'uni1EF8', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'a', 'aacute', 'abreve', 'uni1EAF', 'uni1EB7', 'uni1EB1', 'uni1EB3', 'uni1EB5', 'acircumflex', 'uni1EA5', 'uni1EAD', 'uni1EA7', 'uni1EA9', 'uni1EAB', 'uni0201', 'adieresis', 'uni0227', 'uni1EA1', 'agrave', 'uni1EA3', 'uni0203', 'amacron', 'aogonek', 'aring', 'aringacute', 'atilde', 'ae', 'aeacute', 'b', 'c', 'cacute', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'd', 'eth', 'dcaron', 'dcroat', 'uni01C6', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'uni1EBF', 'uni1EC7', 'uni1EC1', 'uni1EC3', 'uni1EC5', 'uni0205', 'edieresis', 'edotaccent', 'uni1EB9', 'egrave', 'uni1EBB', 'uni0207', 'emacron', 'eogonek', 'uni1EBD', 'uni0259', 'f', 'g', 'gbreve', 'gcaron', 'gcircumflex', 'uni0123', 'gdotaccent', 'h', 'hbar', 'hcircumflex', 'i', 'dotlessi', 'iacute', 'ibreve', 'icircumflex', 'uni0209', 'idieresis', 'i.loclTRK', 'uni1ECB', 'igrave', 'uni1EC9', 'uni020B', 'imacron', 'iogonek', 'itilde', 'j', 'uni0237', 'jcircumflex', 'k', 'uni0137', 'kgreenlandic', 'l', 'lacute', 'lcaron', 'uni013C', 'ldot', 'uni01C9', 'lslash', 'm', 'n', 'nacute', 'ncaron', 'uni0146', 'eng', 'uni01CC', 'ntilde', 'o', 'oacute', 'obreve', 'ocircumflex', 'uni1ED1', 'uni1ED9', 'uni1ED3', 'uni1ED5', 'uni1ED7', 'uni020D', 'odieresis', 'uni022B', 'uni022F', 'uni0231', 'uni1ECD', 'ograve', 'uni1ECF', 'ohorn', 'uni1EDB', 'uni1EE3', 'uni1EDD', 'uni1EDF', 'uni1EE1', 'ohungarumlaut', 'uni020F', 'omacron', 'uni01EB', 'oslash', 'oslashacute', 'otilde', 'uni022D', 'oe', 'p', 'thorn', 'q', 'r', 'racute', 'rcaron', 'uni0157', 'uni0211', 'uni0213', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'uni0219', 'germandbls', 't', 'tbar', 'tcaron', 'uni0163', 'uni021B', 'u', 'uacute', 'ubreve', 'ucircumflex', 'uni0215', 'udieresis', 'uni1EE5', 'ugrave', 'uni1EE7', 'uhorn', 'uni1EE9', 'uni1EF1', 'uni1EEB', 'uni1EED', 'uni1EEF', 'uhungarumlaut', 'uni0217', 'umacron', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'uni1EF5', 'ygrave', 'uni1EF7', 'uni0233', 'uni1EF9', 'z', 'zacute', 'zcaron', 'zdotaccent', 'm_p_l_u_s_f_o_n_t_s', 'ordfeminine', 'ordmasculine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.lf', 'one.lf', 'two.lf', 'three.lf', 'four.lf', 'five.lf', 'six.lf', 'seven.lf', 'eight.lf', 'nine.lf', 'uni2070', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'periodcentered.loclCAT', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'hyphen', 'uni00AD', 'endash', 'emdash', 'underscore', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'space', 'uni00A0', 'uni20B5', 'cent', 'colonmonetary', 'currency', 'dollar', 'dong', 'Euro', 'florin', 'franc', 'uni20B2', 'uni20AD', 'lira', 'uni20BA', 'uni20BC', 'uni20A6', 'peseta', 'uni20B1', 'uni20BD', 'uni20B9', 'sterling', 'uni20A9', 'yen', 'uni2219', 'uni2215', 'plus', 'minus', 'multiply', 'divide', 'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal', 'plusminus', 'approxequal', 'logicalnot', 'asciitilde', 'asciicircum', 'uni00B5', 'percent', 'perthousand', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'trademark', 'degree', 'bar', 'brokenbar', 'dagger', 'daggerdbl', 'uni2116', 'uni02BC', 'uni02C9', 'dieresis', 'dotaccent', 'grave', 'acute', 'hungarumlaut', 'circumflex', 'caron', 'breve', 'ring', 'tilde', 'macron', 'cedilla', 'ogonek', 'uni20B5.BRACKET.499', 'cent.BRACKET.499', 'colonmonetary.BRACKET.234', 'dollar.BRACKET.499', 'uni20B2.BRACKET.499', 'uni20A6.BRACKET.234', 'uni20B1.BRACKET.367', 'uni20A9.BRACKET.234'] [code: mono-outliers]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---

Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will
only differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.

However, a quotedbl should have 2 contours, unless the font belongs to a
display family.

This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.


</pre>

* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: daggerdbl	Contours detected: 2	Expected: 1 or 3
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: trademark	Contours detected: 1	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
Glyph name: uni01CA	Contours detected: 1	Expected: 2
Glyph name: uni01CB	Contours detected: 2	Expected: 3
Glyph name: uni1EDB	Contours detected: 4	Expected: 3
Glyph name: uni1EDD	Contours detected: 4	Expected: 3
Glyph name: uni1EDF	Contours detected: 4	Expected: 3
Glyph name: uni1EE1	Contours detected: 4	Expected: 3
Glyph name: uni1EE3	Contours detected: 4	Expected: 3
Glyph name: uni1EE8	Contours detected: 3	Expected: 2
Glyph name: uni1EE9	Contours detected: 3	Expected: 2
Glyph name: uni1EEA	Contours detected: 3	Expected: 2
Glyph name: uni1EEB	Contours detected: 3	Expected: 2
Glyph name: uni1EEC	Contours detected: 3	Expected: 2
Glyph name: uni1EED	Contours detected: 3	Expected: 2
Glyph name: uni1EEE	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uogonek	Contours detected: 2	Expected: 1 [code: contour-count]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class)</summary>

* [com.google.fonts/check/gdef_spacing_marks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class should be non-spacing.
Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
positioning that was only intended for building composite glyphs during design.


</pre>

* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 Ccedilla, Uogonek, ccedilla, periodcentered, uni0163 and uni01EB [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7, U+00C7, U+00E7, U+0163, U+0172 and U+01EB [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---

This test looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.

This test is not run for variable fonts, as they may legitimately have colinear
vectors.


</pre>

* ⚠ **WARN** The following glyphs have colinear vectors:
	* colonmonetary: L<<145.0,83.0>--<174.0,365.0>> -> L<<174.0,365.0>--<209.0,703.0>>
	* colonmonetary: L<<230.0,711.0>--<194.0,365.0>> -> L<<194.0,365.0>--<163.0,64.0>>
	* colonmonetary: L<<258.0,16.0>--<294.0,365.0>> -> L<<294.0,365.0>--<331.0,718.0>>
	* colonmonetary: L<<350.0,715.0>--<314.0,365.0>> -> L<<314.0,365.0>--<277.0,13.0>>
	* uni4FEF: L<<395.0,448.0>--<395.0,448.0>> -> L<<395.0,448.0>--<395.0,448.0>>
	* uni5056: L<<370.0,345.0>--<370.0,345.0>> -> L<<370.0,345.0>--<370.0,345.0>>
	* uni5195: L<<175.0,370.0>--<175.0,370.0>> -> L<<175.0,370.0>--<175.0,370.0>>
	* uni5436: L<<90.0,720.0>--<90.0,77.0>> -> L<<90.0,77.0>--<90.0,50.0>>
	* uni543B: L<<105.0,720.0>--<105.0,83.0>> -> L<<105.0,83.0>--<105.0,50.0>>
	* uni545F: L<<100.0,720.0>--<100.0,97.0>> -> L<<100.0,97.0>--<100.0,50.0>> and 49 more. [code: found-colinear-vectors]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---

This test heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed
up by manual inspection.


</pre>

* ⚠ **WARN** The following glyphs have jaggy segments:
	* sohira: B<<428.0,466.0>-<315.0,414.0>-<193.0,378.0>>/L<<193.0,378.0>--<899.0,437.0>> = 11.663305459962674
	* uni3231: L<<225.0,-80.0>--<225.0,523.0>>/B<<225.0,523.0>-<187.0,338.0>-<111.0,161.0>> = 11.60741567579494
	* uni4E6D: B<<560.5,247.5>-<656.0,275.0>-<751.0,295.0>>/L<<751.0,295.0>--<115.0,295.0>> = 11.888658039627968
	* uni4FDF: L<<358.0,578.0>--<358.0,578.0>>/B<<358.0,578.0>-<303.0,576.0>-<250.0,575.0>> = 2.082565279730795
	* uni50FB: L<<260.0,-70.0>--<260.0,278.0>>/B<<260.0,278.0>-<251.0,197.0>-<233.5,123.5>> = 6.340191745909908
	* uni5288: L<<125.0,295.0>--<125.0,500.0>>/B<<125.0,500.0>-<116.0,452.0>-<98.0,406.0>> = 10.61965527615514
	* uni56C2: B<<274.5,148.5>-<215.0,130.0>-<146.0,115.0>>/L<<146.0,115.0>--<455.0,115.0>> = 12.2647737278924
	* uni56C2: L<<830.0,200.0>--<654.0,200.0>>/B<<654.0,200.0>-<734.0,182.0>-<805.5,161.0>> = 12.680383491819796
	* uni58C1: L<<125.0,250.0>--<125.0,475.0>>/B<<125.0,475.0>-<107.0,371.0>-<54.0,281.0>> = 9.819300638757893
	* uni5F6C: L<<185.0,-80.0>--<185.0,563.0>>/B<<185.0,563.0>-<136.0,356.0>-<29.0,160.0>> = 13.31763397294935 and 278 more. [code: found-jaggy-segments]

</details>
<details>
<summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---

This test detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.

This test is disabled for italic styles, which often contain nearly-upright
lines.


</pre>

* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:
	* M: L<<430.0,0.0>--<431.0,691.0>> and M: L<<69.0,691.0>--<70.0,0.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[6] MplusCode[wght].ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---

All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.

If using GlyphsApp, ligature carets can be set directly on canvas by accessing
the `Glyph -&gt; Set Anchors` menu option or by pressing the `Cmd+U` keyboard
shortcut.

If designing with UFOs, (as of Oct 2020) ligature carets are not yet compiled
by ufo2ft, and therefore will not build via FontMake. See
googlefonts/ufo2ft/issues/329


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---

There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)

Requirements for monospace fonts:

* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm

* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm

* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2

* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397

Also we should report an error for glyphs not of average width.

Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave
a font a monospace flag in Panose, Microsoft Word would ignore the actual
advance widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140


</pre>

* 🔥 **FAIL** On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead. [code: mono-bad-post-isFixedPitch]
* 🔥 **FAIL** On monospaced fonts, the value of OS/2.panose.bProportion must be set to 9 (proportion: monospaced), but got 0 instead. [code: mono-bad-panose-proportion]
* ⚠ **WARN** Font is monospaced but 553 glyphs (8.46%) have a different width. You should check the widths of: ['A', 'Aacute', 'Abreve', 'uni1EAE', 'uni1EB6', 'uni1EB0', 'uni1EB2', 'uni1EB4', 'Acircumflex', 'uni1EA4', 'uni1EAC', 'uni1EA6', 'uni1EA8', 'uni1EAA', 'uni0200', 'Adieresis', 'uni0226', 'uni1EA0', 'Agrave', 'uni1EA2', 'uni0202', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde', 'AE', 'AEacute', 'B', 'C', 'Cacute', 'Ccaron', 'Ccedilla', 'Ccircumflex', 'Cdotaccent', 'D', 'uni01C4', 'Eth', 'Dcaron', 'Dcroat', 'uni01C5', 'E', 'Eacute', 'Ebreve', 'Ecaron', 'Ecircumflex', 'uni1EBE', 'uni1EC6', 'uni1EC0', 'uni1EC2', 'uni1EC4', 'uni0204', 'Edieresis', 'Edotaccent', 'uni1EB8', 'Egrave', 'uni1EBA', 'uni0206', 'Emacron', 'Eogonek', 'uni1EBC', 'F', 'G', 'Gbreve', 'Gcaron', 'Gcircumflex', 'uni0122', 'Gdotaccent', 'H', 'Hbar', 'Hcircumflex', 'I', 'Iacute', 'Ibreve', 'Icircumflex', 'uni0208', 'Idieresis', 'Idotaccent', 'uni1ECA', 'Igrave', 'uni1EC8', 'uni020A', 'Imacron', 'Iogonek', 'Itilde', 'J', 'Jcircumflex', 'K', 'uni0136', 'L', 'uni01C7', 'Lacute', 'Lcaron', 'uni013B', 'Ldot', 'uni01C8', 'Lslash', 'M', 'N', 'uni01CA', 'Nacute', 'Ncaron', 'uni0145', 'Eng', 'uni01CB', 'Ntilde', 'O', 'Oacute', 'Obreve', 'Ocircumflex', 'uni1ED0', 'uni1ED8', 'uni1ED2', 'uni1ED4', 'uni1ED6', 'uni020C', 'Odieresis', 'uni022A', 'uni022E', 'uni0230', 'uni1ECC', 'Ograve', 'uni1ECE', 'Ohorn', 'uni1EDA', 'uni1EE2', 'uni1EDC', 'uni1EDE', 'uni1EE0', 'Ohungarumlaut', 'uni020E', 'Omacron', 'uni01EA', 'Oslash', 'Oslashacute', 'Otilde', 'uni022C', 'OE', 'P', 'Thorn', 'Q', 'R', 'Racute', 'Rcaron', 'uni0156', 'uni0210', 'uni0212', 'S', 'Sacute', 'Scaron', 'Scedilla', 'Scircumflex', 'uni0218', 'uni1E9E', 'uni018F', 'T', 'Tbar', 'Tcaron', 'uni0162', 'uni021A', 'U', 'Uacute', 'Ubreve', 'Ucircumflex', 'uni0214', 'Udieresis', 'uni1EE4', 'Ugrave', 'uni1EE6', 'Uhorn', 'uni1EE8', 'uni1EF0', 'uni1EEA', 'uni1EEC', 'uni1EEE', 'Uhungarumlaut', 'uni0216', 'Umacron', 'Uogonek', 'Uring', 'Utilde', 'V', 'W', 'Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave', 'X', 'Y', 'Yacute', 'Ycircumflex', 'Ydieresis', 'uni1EF4', 'Ygrave', 'uni1EF6', 'uni0232', 'uni1EF8', 'Z', 'Zacute', 'Zcaron', 'Zdotaccent', 'a', 'aacute', 'abreve', 'uni1EAF', 'uni1EB7', 'uni1EB1', 'uni1EB3', 'uni1EB5', 'acircumflex', 'uni1EA5', 'uni1EAD', 'uni1EA7', 'uni1EA9', 'uni1EAB', 'uni0201', 'adieresis', 'uni0227', 'uni1EA1', 'agrave', 'uni1EA3', 'uni0203', 'amacron', 'aogonek', 'aring', 'aringacute', 'atilde', 'ae', 'aeacute', 'b', 'c', 'cacute', 'ccaron', 'ccedilla', 'ccircumflex', 'cdotaccent', 'd', 'eth', 'dcaron', 'dcroat', 'uni01C6', 'e', 'eacute', 'ebreve', 'ecaron', 'ecircumflex', 'uni1EBF', 'uni1EC7', 'uni1EC1', 'uni1EC3', 'uni1EC5', 'uni0205', 'edieresis', 'edotaccent', 'uni1EB9', 'egrave', 'uni1EBB', 'uni0207', 'emacron', 'eogonek', 'uni1EBD', 'uni0259', 'f', 'g', 'gbreve', 'gcaron', 'gcircumflex', 'uni0123', 'gdotaccent', 'h', 'hbar', 'hcircumflex', 'i', 'dotlessi', 'iacute', 'ibreve', 'icircumflex', 'uni0209', 'idieresis', 'i.loclTRK', 'uni1ECB', 'igrave', 'uni1EC9', 'uni020B', 'imacron', 'iogonek', 'itilde', 'j', 'uni0237', 'jcircumflex', 'k', 'uni0137', 'kgreenlandic', 'l', 'lacute', 'lcaron', 'uni013C', 'ldot', 'uni01C9', 'lslash', 'm', 'n', 'nacute', 'ncaron', 'uni0146', 'eng', 'uni01CC', 'ntilde', 'o', 'oacute', 'obreve', 'ocircumflex', 'uni1ED1', 'uni1ED9', 'uni1ED3', 'uni1ED5', 'uni1ED7', 'uni020D', 'odieresis', 'uni022B', 'uni022F', 'uni0231', 'uni1ECD', 'ograve', 'uni1ECF', 'ohorn', 'uni1EDB', 'uni1EE3', 'uni1EDD', 'uni1EDF', 'uni1EE1', 'ohungarumlaut', 'uni020F', 'omacron', 'uni01EB', 'oslash', 'oslashacute', 'otilde', 'uni022D', 'oe', 'p', 'thorn', 'q', 'r', 'racute', 'rcaron', 'uni0157', 'uni0211', 'uni0213', 's', 'sacute', 'scaron', 'scedilla', 'scircumflex', 'uni0219', 'germandbls', 't', 'tbar', 'tcaron', 'uni0163', 'uni021B', 'u', 'uacute', 'ubreve', 'ucircumflex', 'uni0215', 'udieresis', 'uni1EE5', 'ugrave', 'uni1EE7', 'uhorn', 'uni1EE9', 'uni1EF1', 'uni1EEB', 'uni1EED', 'uni1EEF', 'uhungarumlaut', 'uni0217', 'umacron', 'uogonek', 'uring', 'utilde', 'v', 'w', 'wacute', 'wcircumflex', 'wdieresis', 'wgrave', 'x', 'y', 'yacute', 'ycircumflex', 'ydieresis', 'uni1EF5', 'ygrave', 'uni1EF7', 'uni0233', 'uni1EF9', 'z', 'zacute', 'zcaron', 'zdotaccent', 'm_p_l_u_s_f_o_n_t_s', 'ordfeminine', 'ordmasculine', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero.lf', 'one.lf', 'two.lf', 'three.lf', 'four.lf', 'five.lf', 'six.lf', 'seven.lf', 'eight.lf', 'nine.lf', 'uni2070', 'uni00B9', 'uni00B2', 'uni00B3', 'uni2074', 'fraction', 'onehalf', 'onequarter', 'threequarters', 'period', 'comma', 'colon', 'semicolon', 'ellipsis', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'bullet', 'asterisk', 'numbersign', 'slash', 'backslash', 'periodcentered.loclCAT', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'hyphen', 'uni00AD', 'endash', 'emdash', 'underscore', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemotleft', 'guillemotright', 'guilsinglleft', 'guilsinglright', 'quotedbl', 'quotesingle', 'space', 'uni00A0', 'uni20B5', 'cent', 'colonmonetary', 'currency', 'dollar', 'dong', 'Euro', 'florin', 'franc', 'uni20B2', 'uni20AD', 'lira', 'uni20BA', 'uni20BC', 'uni20A6', 'peseta', 'uni20B1', 'uni20BD', 'uni20B9', 'sterling', 'uni20A9', 'yen', 'uni2219', 'uni2215', 'plus', 'minus', 'multiply', 'divide', 'equal', 'notequal', 'greater', 'less', 'greaterequal', 'lessequal', 'plusminus', 'approxequal', 'logicalnot', 'asciitilde', 'asciicircum', 'uni00B5', 'percent', 'perthousand', 'at', 'ampersand', 'paragraph', 'section', 'copyright', 'registered', 'trademark', 'degree', 'bar', 'brokenbar', 'dagger', 'daggerdbl', 'uni2116', 'uni02BC', 'uni02C9', 'dieresis', 'dotaccent', 'grave', 'acute', 'hungarumlaut', 'circumflex', 'caron', 'breve', 'ring', 'tilde', 'macron', 'cedilla', 'ogonek', 'uni20B5.BRACKET.499', 'cent.BRACKET.499', 'colonmonetary.BRACKET.234', 'dollar.BRACKET.499', 'uni20B2.BRACKET.499', 'uni20A6.BRACKET.234', 'uni20B1.BRACKET.367', 'uni20A9.BRACKET.234'] [code: mono-outliers]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class)</summary>

* [com.google.fonts/check/gdef_spacing_marks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class should be non-spacing.
Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
positioning that was only intended for building composite glyphs during design.


</pre>

* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 Ccedilla, Uogonek, ccedilla, periodcentered, uni0163 and uni01EB [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---

Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.


</pre>

* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7, U+00C7, U+00E7, U+0163, U+0172 and U+01EB [code: non-mark-chars]

</details>
<details>
<summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 25 | 45 | 548 | 37 | 440 | 0 |
| 0% | 2% | 4% | 50% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
