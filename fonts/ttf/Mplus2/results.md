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
<summary><b>[12] Mplus2-Black.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---

A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.

The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.

Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;


Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.

When in doubt, please choose OFL for new font projects.


</pre>

* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
" Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]

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
<summary>🔥 <b>FAIL:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---

There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.

For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright


</pre>

* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 13) has trailing spaces that must be removed: 'This Font [...]l.org/OFL
'

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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
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
	 periodcentered [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0305, U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

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
	 U+00B7 [code: non-mark-chars]

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
	* uni50C2: L<<455.0,355.0>--<510.0,355.0>> -> L<<510.0,355.0>--<535.0,355.0>>
	* uni5F85: L<<305.0,555.0>--<305.0,555.0>> -> L<<305.0,555.0>--<525.0,555.0>>
	* uni61B2: L<<465.0,235.0>--<525.0,235.0>> -> L<<525.0,235.0>--<535.0,235.0>>
	* uni69CC.jp04: L<<505.0,735.0>--<505.0,735.0>> -> L<<505.0,735.0>--<616.0,735.0>>
	* uni6A13: L<<475.0,355.0>--<535.0,355.0>> -> L<<535.0,355.0>--<555.0,355.0>>
	* uni6BB2: L<<221.0,585.0>--<350.0,585.0>> -> L<<350.0,585.0>--<381.0,585.0>>
	* uni6E38: L<<245.0,730.0>--<245.0,730.0>> -> L<<245.0,730.0>--<335.0,730.0>>
	* uni743A: L<<525.0,475.0>--<525.0,475.0>> -> L<<525.0,475.0>--<650.0,475.0>>
	* uni74CA: L<<530.0,250.0>--<531.0,250.0>> -> L<<531.0,250.0>--<775.0,250.0>>
	* uni85F7.jp04: L<<705.0,575.0>--<830.0,575.0>> -> L<<830.0,575.0>--<830.0,575.0>> and 29 more. [code: found-colinear-vectors]

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
	* uni2E96: L<<405.0,-100.0>--<405.0,568.0>>/B<<405.0,568.0>-<391.0,479.0>-<373.5,390.5>> = 8.939565003151522
	* uni2EDF: L<<525.0,155.0>--<665.0,190.0>>/L<<665.0,190.0>--<455.0,190.0>> = 14.036243467926484
	* uni2F71: B<<720.5,411.5>-<739.0,329.0>-<755.0,255.0>>/L<<755.0,255.0>--<755.0,580.0>> = 12.200468727380786
	* uni2F96: L<<205.0,215.0>--<345.0,250.0>>/L<<345.0,250.0>--<130.0,250.0>> = 14.036243467926484
	* uni2F98: L<<245.0,545.0>--<385.0,611.0>>/B<<385.0,611.0>-<303.0,595.0>-<215.0,580.0>> = 14.19958908446302
	* uni2F98: L<<525.0,610.0>--<659.0,673.0>>/B<<659.0,673.0>-<602.0,658.0>-<540.0,643.5>> = 10.436965633934038
	* uni2FB5: B<<255.0,635.0>-<461.0,642.0>-<670.0,665.0>>/L<<670.0,665.0>--<240.0,665.0>> = 6.280007125699772
	* uni2FBF: B<<558.5,244.0>-<689.0,266.0>-<817.0,295.0>>/L<<817.0,295.0>--<50.0,295.0>> = 12.765565781058607
	* uni2FC6: L<<595.0,320.0>--<439.0,320.0>>/L<<439.0,320.0>--<585.0,295.0>> = 9.716685817785114
	* uni2FC7: L<<330.0,-100.0>--<330.0,128.0>>/B<<330.0,128.0>-<307.0,25.0>-<275.0,-33.0>> = 12.587693381648771 and 1909 more. [code: found-jaggy-segments]

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
	* uni00B5: L<<249.0,520.0>--<250.0,240.0>>
	* uni3083.vert: L<<640.0,170.0>--<641.0,322.0>> and uni3083: L<<560.0,90.0>--<561.0,242.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[12] Mplus2-Bold.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---

A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.

The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.

Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;


Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.

When in doubt, please choose OFL for new font projects.


</pre>

* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
" Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]

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
<summary>🔥 <b>FAIL:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---

There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.

For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright


</pre>

* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 13) has trailing spaces that must be removed: 'This Font [...]l.org/OFL
'

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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
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
	 periodcentered [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0305, U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

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
	 U+00B7 [code: non-mark-chars]

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
	* OE: L<<511.0,730.0>--<511.0,730.0>> -> L<<511.0,730.0>--<1007.0,730.0>>
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
	* OE: L<<511.0,0.0>--<511.0,0.0>>/B<<511.0,0.0>-<465.0,-10.0>-<415.0,-10.0>> = 12.2647737278924
	* uni2E90: L<<520.0,43.0>--<520.0,451.0>>/B<<520.0,451.0>-<489.0,266.0>-<385.5,128.5>> = 9.51253760227898
	* uni2F2A: L<<520.0,43.0>--<520.0,451.0>>/B<<520.0,451.0>-<489.0,266.0>-<385.5,128.5>> = 9.51253760227898
	* uni2F87: B<<265.0,600.0>-<225.0,486.0>-<171.0,388.0>>/L<<171.0,388.0>--<244.0,481.0>> = 9.274346472069261
	* uni3052.BRACKET.500: B<<753.0,642.0>-<749.0,668.0>-<743.0,694.0>>/L<<743.0,694.0>--<743.0,589.0>> = 12.994616791916512
	* uni3091: L<<89.0,542.0>--<549.0,665.0>>/B<<549.0,665.0>-<444.0,658.0>-<345.5,655.0>> = 11.156097600053185
	* uni30F8.BRACKET.500: B<<753.0,642.0>-<750.0,659.0>-<747.0,675.0>>/L<<747.0,675.0>--<747.0,620.0>> = 10.61965527615514
	* uni3231: L<<232.0,-93.0>--<232.0,286.0>>/B<<232.0,286.0>-<221.0,232.0>-<207.0,185.5>> = 11.513831184487014
	* uni4EB3: B<<577.5,296.5>-<664.0,307.0>-<726.0,319.0>>/L<<726.0,319.0>--<177.0,319.0>> = 10.954062643398332
	* uni4F38: L<<295.0,80.0>--<295.0,686.0>>/B<<295.0,686.0>-<273.0,599.0>-<240.0,525.0>> = 14.19109654902398 and 1104 more. [code: found-jaggy-segments]

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
	* uni00B5: L<<200.0,520.0>--<201.0,227.0>>
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
<summary><b>[12] Mplus2-ExtraBold.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---

A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.

The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.

Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;


Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.

When in doubt, please choose OFL for new font projects.


</pre>

* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
" Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]

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
<summary>🔥 <b>FAIL:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---

There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.

For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright


</pre>

* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 13) has trailing spaces that must be removed: 'This Font [...]l.org/OFL
'

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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
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
	 periodcentered [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0305, U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

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
	 U+00B7 [code: non-mark-chars]

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
	* uni661C: L<<200.0,277.0>--<200.0,277.0>> -> L<<200.0,277.0>--<201.0,277.0>>
	* uni6BB2: L<<214.0,582.0>--<344.0,582.0>> -> L<<344.0,582.0>--<376.0,582.0>>
	* uni6FE0: L<<237.0,468.0>--<237.0,468.0>> -> L<<237.0,468.0>--<966.0,468.0>>
	* uni7B46: L<<582.0,587.0>--<582.0,587.0>> -> L<<582.0,587.0>--<890.0,587.0>>
	* uni7BED: L<<582.0,587.0>--<582.0,587.0>> -> L<<582.0,587.0>--<915.0,587.0>>
	* uni7DAC: L<<383.0,516.0>--<383.0,516.0>> -> L<<383.0,516.0>--<429.0,516.0>>
	* uni7E6D: L<<604.0,408.0>--<624.0,295.0>> -> L<<624.0,295.0>--<634.0,237.0>>
	* uni7E6D: L<<634.0,323.0>--<624.0,386.0>> -> L<<624.0,386.0>--<621.0,408.0>>
	* uni89B3: L<<406.0,47.0>--<483.0,47.0>> -> L<<483.0,47.0>--<483.0,47.0>>
	* uni92F2: L<<443.0,272.0>--<443.0,623.0>> -> L<<443.0,623.0>--<443.0,643.0>>
	* uni9444: L<<367.0,281.0>--<367.0,281.0>> -> L<<367.0,281.0>--<982.0,281.0>> and uni96E2: L<<383.0,619.0>--<383.0,619.0>> -> L<<383.0,619.0>--<495.0,619.0>> [code: found-colinear-vectors]

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
	* u2634C: L<<417.0,668.0>--<278.0,633.0>>/L<<278.0,633.0>--<577.0,633.0>> = 14.133190548862903
	* uni2F60: B<<705.0,273.0>-<713.0,243.0>-<721.0,214.0>>/B<<721.0,214.0>-<703.0,288.0>-<695.0,378.0>> = 1.750854186542861
	* uni2F60: B<<790.5,26.0>-<755.0,92.0>-<732.0,171.0>>/B<<732.0,171.0>-<747.0,111.0>-<761.5,50.0>> = 2.1961071932298095
	* uni2F87: B<<266.0,580.0>-<244.0,517.0>-<218.0,458.0>>/L<<218.0,458.0>--<237.0,483.0>> = 13.452803558353288
	* uni2F98: L<<526.0,618.0>--<658.0,680.0>>/B<<658.0,680.0>-<565.0,656.0>-<455.0,633.0>> = 10.689007815965782
	* uni2FC0: L<<727.0,43.0>--<666.0,43.0>>/B<<666.0,43.0>-<698.0,40.0>-<718.0,38.5>> = 5.355825042855143
	* uni2FC6: L<<582.0,328.0>--<427.0,328.0>>/L<<427.0,328.0>--<566.0,299.0>> = 11.78474850626279
	* uni2FCE: L<<256.0,87.0>--<122.0,43.0>>/B<<122.0,43.0>-<200.0,55.0>-<278.0,69.0>> = 9.431856535863268
	* uni2FCE: L<<477.0,223.0>--<349.0,223.0>>/L<<349.0,223.0>--<475.0,192.0>> = 13.822054635731691
	* uni2FD5: L<<683.0,-93.0>--<674.0,34.0>>/L<<674.0,34.0>--<674.0,-76.0>> = 4.053554231831338 and 1594 more. [code: found-jaggy-segments]

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
	* u27FB7: L<<767.0,139.0>--<768.0,5.0>>
	* uni2ECA: L<<767.0,139.0>--<768.0,5.0>>
	* uni3070.BRACKET.633: L<<542.0,769.0>--<699.0,768.0>>
	* uni3083.vert: L<<640.0,186.0>--<641.0,318.0>>
	* uni3083: L<<560.0,106.0>--<561.0,238.0>>
	* uni3084: L<<574.0,153.0>--<575.0,294.0>>
	* uni4E73: L<<577.0,257.0>--<578.0,132.0>>
	* uni4E9B: L<<511.0,477.0>--<512.0,352.0>>
	* uni4F5B: L<<382.0,139.0>--<258.0,140.0>>
	* uni5230: L<<577.0,118.0>--<578.0,-7.0>> and 77 more. [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[12] Mplus2-Light.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---

A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.

The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.

Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;


Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.

When in doubt, please choose OFL for new font projects.


</pre>

* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
" Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]

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
<summary>🔥 <b>FAIL:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---

There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.

For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright


</pre>

* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 13) has trailing spaces that must be removed: 'This Font [...]l.org/OFL
'

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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uni20A9	Contours detected: 6	Expected: 1, 3, 4 or 7
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uni20A9	Contours detected: 6	Expected: 1, 3, 4 or 7
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
	 periodcentered [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0305, U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

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
	 U+00B7 [code: non-mark-chars]

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
	* uni5099.BRACKET.620: L<<311.0,523.0>--<311.0,481.0>> -> L<<311.0,481.0>--<317.0,354.0>>
	* uni5436: L<<110.0,703.0>--<110.0,77.0>> -> L<<110.0,77.0>--<110.0,67.0>>
	* uni5436: L<<623.0,643.0>--<623.0,654.0>> -> L<<623.0,654.0>--<623.0,765.0>>
	* uni543B: L<<125.0,703.0>--<125.0,75.0>> -> L<<125.0,75.0>--<125.0,69.0>>
	* uni545F: L<<119.0,703.0>--<119.0,68.0>> -> L<<119.0,68.0>--<119.0,67.0>>
	* uni5471: L<<119.0,703.0>--<119.0,103.0>> -> L<<119.0,103.0>--<119.0,71.0>>
	* uni5475: L<<124.0,703.0>--<124.0,102.0>> -> L<<124.0,102.0>--<124.0,67.0>>
	* uni5477: L<<114.0,703.0>--<114.0,102.0>> -> L<<114.0,102.0>--<114.0,67.0>>
	* uni547B: L<<114.0,703.0>--<114.0,109.0>> -> L<<114.0,109.0>--<114.0,67.0>>
	* uni54AC.fude: L<<116.0,703.0>--<116.0,68.0>> -> L<<116.0,68.0>--<116.0,67.0>> and 9 more. [code: found-colinear-vectors]

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
	* uni3091: L<<855.0,711.0>--<420.0,568.0>>/B<<420.0,568.0>-<458.0,572.0>-<500.0,574.5>> = 12.188530773173335
	* uni3231: L<<226.0,-83.0>--<226.0,454.0>>/B<<226.0,454.0>-<192.0,291.0>-<130.0,146.0>> = 11.782325134462294
	* uni4E6D: B<<437.0,216.0>-<540.0,251.0>-<652.0,278.0>>/L<<652.0,278.0>--<109.0,278.0>> = 13.553764097731639
	* uni4E9F: L<<371.0,556.0>--<371.0,547.0>>/B<<371.0,547.0>-<378.0,589.0>-<385.0,634.0>> = 9.462322208025613
	* uni50FB: L<<270.0,-74.0>--<270.0,211.0>>/B<<270.0,211.0>-<261.0,148.0>-<245.5,90.5>> = 8.13010235415596
	* uni513A: L<<218.0,693.0>--<218.0,723.0>>/B<<218.0,723.0>-<205.0,668.0>-<188.5,617.5>> = 13.298570330494275
	* uni5275: L<<140.0,-79.0>--<140.0,202.0>>/B<<140.0,202.0>-<139.0,195.0>-<138.0,189.0>> = 8.13010235415596
	* uni5288: L<<128.0,286.0>--<128.0,465.0>>/B<<128.0,465.0>-<109.0,375.0>-<65.0,304.0>> = 11.920738539922306
	* uni56A2: L<<890.0,488.0>--<602.0,488.0>>/B<<602.0,488.0>-<679.0,472.0>-<747.5,453.5>> = 11.738571206722328
	* uni56C2: B<<303.0,149.5>-<254.0,134.0>-<196.0,121.0>>/L<<196.0,121.0>--<459.0,121.0>> = 12.633361935275003 and 197 more. [code: found-jaggy-segments]

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
	* uni5B54: L<<267.0,47.0>--<268.0,324.0>>
	* uni689D: L<<116.0,-83.0>--<115.0,439.0>>
	* uni7BC9: L<<784.0,560.0>--<535.0,559.0>>
	* uni8129: L<<116.0,-83.0>--<115.0,439.0>>
	* uni8FF9: L<<741.0,662.0>--<740.0,161.0>> and uni907D: L<<346.0,647.0>--<345.0,487.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[12] Mplus2-Medium.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---

A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.

The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.

Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;


Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.

When in doubt, please choose OFL for new font projects.


</pre>

* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
" Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]

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
<summary>🔥 <b>FAIL:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---

There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.

For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright


</pre>

* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 13) has trailing spaces that must be removed: 'This Font [...]l.org/OFL
'

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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
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
	 periodcentered [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0305, U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

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
	 U+00B7 [code: non-mark-chars]

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
	* uni2EF2: L<<758.0,598.0>--<565.0,598.0>> -> L<<565.0,598.0>--<542.0,598.0>>
	* uni4E80: L<<758.0,598.0>--<565.0,598.0>> -> L<<565.0,598.0>--<542.0,598.0>>
	* uni4FD8: L<<732.0,228.0>--<732.0,228.0>> -> L<<732.0,228.0>--<970.0,228.0>>
	* uni545F: L<<158.0,668.0>--<158.0,145.0>> -> L<<158.0,145.0>--<158.0,100.0>>
	* uni56AE: L<<335.0,698.0>--<335.0,698.0>> -> L<<335.0,698.0>--<645.0,698.0>>
	* uni58A8: L<<445.0,210.0>--<445.0,210.0>> -> L<<445.0,210.0>--<555.0,210.0>>
	* uni5C3E: L<<588.0,98.0>--<588.0,47.0>> -> L<<588.0,47.0>--<588.0,46.0>>
	* uni63AC: L<<225.0,642.0>--<300.0,642.0>> -> L<<300.0,642.0>--<300.0,642.0>>
	* uni6908: L<<240.0,645.0>--<335.0,645.0>> -> L<<335.0,645.0>--<335.0,645.0>>
	* uni6BEC: L<<440.0,8.0>--<670.0,8.0>> -> L<<670.0,8.0>--<675.0,8.0>> and 10 more. [code: found-colinear-vectors]

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
	* uni2F5E: L<<277.0,-36.0>--<277.0,-36.0>>/B<<277.0,-36.0>-<174.0,-42.0>-<75.0,-45.0>> = 3.3338506615365393
	* uni3091: L<<865.0,683.0>--<520.0,576.0>>/B<<520.0,576.0>-<563.0,580.0>-<615.0,580.0>> = 11.916465921030575
	* uni3091: L<<94.0,530.0>--<589.0,676.0>>/B<<589.0,676.0>-<472.0,669.0>-<366.0,666.0>> = 13.009525882790433
	* uni3231: L<<228.0,-90.0>--<228.0,313.0>>/B<<228.0,313.0>-<204.0,204.0>-<169.0,116.0>> = 12.417445790076274
	* uni4E7E: L<<465.0,122.0>--<465.0,65.0>>/B<<465.0,65.0>-<479.0,134.0>-<560.0,242.0>> = 11.469530332866904
	* uni4EB3: B<<593.5,293.5>-<682.0,305.0>-<747.0,318.0>>/L<<747.0,318.0>--<160.0,318.0>> = 11.309932474020195
	* uni4FEF: L<<272.0,475.0>--<272.0,722.0>>/B<<272.0,722.0>-<259.0,664.0>-<241.0,611.5>> = 12.633361935275003
	* uni4FF8: L<<275.0,670.0>--<275.0,735.0>>/B<<275.0,735.0>-<261.0,674.0>-<242.5,618.0>> = 12.92599912470594
	* uni5043: B<<709.0,115.0>-<600.0,54.0>-<434.0,32.0>>/L<<434.0,32.0>--<879.0,32.0>> = 7.549421768263246
	* uni504F: L<<358.0,-85.0>--<358.0,194.0>>/B<<358.0,194.0>-<347.0,117.0>-<324.5,52.5>> = 8.13010235415596 and 655 more. [code: found-jaggy-segments]

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
	* uni5B54: L<<242.0,70.0>--<243.0,285.0>>
	* uni5B54: L<<244.0,382.0>--<245.0,522.0>>
	* uni67C4: L<<247.0,348.0>--<248.0,-90.0>>
	* uni689D: L<<98.0,-90.0>--<96.0,334.0>>
	* uni6A2A: L<<247.0,358.0>--<248.0,-90.0>>
	* uni7BC9: L<<750.0,518.0>--<565.0,517.0>>
	* uni8129: L<<98.0,-90.0>--<96.0,334.0>> and uni8FF9: L<<771.0,489.0>--<770.0,192.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[12] Mplus2-Regular.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---

A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.

The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.

Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;


Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.

When in doubt, please choose OFL for new font projects.


</pre>

* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
" Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]

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
<summary>🔥 <b>FAIL:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---

There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.

For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright


</pre>

* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 13) has trailing spaces that must be removed: 'This Font [...]l.org/OFL
'

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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uni20A9	Contours detected: 6	Expected: 1, 3, 4 or 7
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: uni20A9	Contours detected: 6	Expected: 1, 3, 4 or 7
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
	 periodcentered [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0305, U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

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
	 U+00B7 [code: non-mark-chars]

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
	* uni2F46: L<<592.0,353.0>--<592.0,48.0>> -> L<<592.0,48.0>--<592.0,47.0>>
	* uni545F: L<<139.0,685.0>--<139.0,143.0>> -> L<<139.0,143.0>--<139.0,83.0>>
	* uni5475: L<<143.0,685.0>--<143.0,86.0>> -> L<<143.0,86.0>--<143.0,83.0>>
	* uni547B: L<<133.0,685.0>--<133.0,84.0>> -> L<<133.0,84.0>--<133.0,83.0>>
	* uni54AC.fude: L<<138.0,685.0>--<138.0,89.0>> -> L<<138.0,89.0>--<138.0,83.0>>
	* uni54FA: L<<133.0,685.0>--<133.0,87.0>> -> L<<133.0,87.0>--<133.0,83.0>>
	* uni5540: L<<139.0,685.0>--<139.0,100.0>> -> L<<139.0,100.0>--<139.0,93.0>>
	* uni559D: L<<502.0,146.0>--<502.0,115.0>> -> L<<502.0,115.0>--<502.0,114.0>>
	* uni55F9: L<<64.0,753.0>--<307.0,753.0>> -> L<<307.0,753.0>--<307.0,753.0>>
	* uni591C: L<<133.0,428.0>--<133.0,428.0>> -> L<<133.0,428.0>--<133.0,428.0>> and 23 more. [code: found-colinear-vectors]

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
	* uni01EA: B<<660.0,64.5>-<596.0,15.0>-<508.0,-2.0>>/L<<508.0,-2.0>--<508.0,-2.0>> = 10.933816785755795
	* uni01EA: L<<508.0,-2.0>--<508.0,-2.0>>/B<<508.0,-2.0>-<467.0,-11.0>-<441.0,-30.0>> = 12.380756928807159
	* uni2F5E: L<<258.0,-32.0>--<258.0,-32.0>>/B<<258.0,-32.0>-<165.0,-37.0>-<77.0,-40.0>> = 3.0774553994244176
	* uni2F7A: L<<406.0,673.0>--<398.0,671.0>>/L<<398.0,671.0>--<592.0,671.0>> = 14.036243467926484
	* uni2FAA: L<<369.0,182.0>--<356.0,169.0>>/B<<356.0,169.0>-<382.0,188.0>-<405.0,206.0>> = 8.84181456019167
	* uni2FC1: L<<877.0,298.0>--<735.0,298.0>>/L<<735.0,298.0>--<762.0,294.0>> = 8.426969021480678
	* uni2FCE: B<<441.0,-7.0>-<474.0,4.0>-<504.0,18.0>>/B<<504.0,18.0>-<420.0,-4.0>-<345.0,-20.0>> = 10.340500340650019
	* uni2FD2: L<<645.0,260.0>--<346.0,260.0>>/L<<346.0,260.0>--<398.0,247.0>> = 14.036243467926484
	* uni2FD2: L<<645.0,572.0>--<346.0,572.0>>/L<<346.0,572.0>--<398.0,559.0>> = 14.036243467926484
	* uni2FD2: L<<835.0,260.0>--<658.0,260.0>>/L<<658.0,260.0>--<712.0,247.0>> = 13.535856369134248 and 541 more. [code: found-jaggy-segments]

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
	* uni5B54: L<<255.0,58.0>--<256.0,305.0>>
	* uni5B54: L<<256.0,376.0>--<257.0,520.0>>
	* uni67C4: L<<233.0,416.0>--<234.0,-87.0>>
	* uni689D: L<<107.0,-87.0>--<105.0,385.0>>
	* uni6A2A: L<<233.0,420.0>--<234.0,-87.0>>
	* uni7BC9: L<<767.0,539.0>--<550.0,538.0>>
	* uni8129: L<<107.0,-87.0>--<105.0,385.0>> and uni8FF9: L<<756.0,648.0>--<755.0,176.0>> [code: found-semi-vertical]

</details>
<br>
</details>
<details>
<summary><b>[11] Mplus2-Thin.ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---

A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.

The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.

Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;


Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.

When in doubt, please choose OFL for new font projects.


</pre>

* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
" Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]

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
<summary>🔥 <b>FAIL:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---

There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.

For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright


</pre>

* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 13) has trailing spaces that must be removed: 'This Font [...]l.org/OFL
'

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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
Glyph name: uni1EF0	Contours detected: 3	Expected: 2
Glyph name: uni1EF1	Contours detected: 3	Expected: 2
Glyph name: Uhorn	Contours detected: 2	Expected: 1
Glyph name: aogonek	Contours detected: 3	Expected: 2
Glyph name: eogonek	Contours detected: 3	Expected: 2
Glyph name: ohorn	Contours detected: 3	Expected: 2
Glyph name: uhorn	Contours detected: 2	Expected: 1
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
Glyph name: uni1EEF	Contours detected: 3	Expected: 2
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
	 periodcentered [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0305, U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

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
	 U+00B7 [code: non-mark-chars]

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
	* uni4FEF: L<<395.0,448.0>--<395.0,448.0>> -> L<<395.0,448.0>--<395.0,448.0>>
	* uni5056: L<<370.0,345.0>--<370.0,345.0>> -> L<<370.0,345.0>--<370.0,345.0>>
	* uni5195: L<<175.0,370.0>--<175.0,370.0>> -> L<<175.0,370.0>--<175.0,370.0>>
	* uni5436: L<<90.0,720.0>--<90.0,77.0>> -> L<<90.0,77.0>--<90.0,50.0>>
	* uni543B: L<<105.0,720.0>--<105.0,83.0>> -> L<<105.0,83.0>--<105.0,50.0>>
	* uni545F: L<<100.0,720.0>--<100.0,97.0>> -> L<<100.0,97.0>--<100.0,50.0>>
	* uni5471: L<<100.0,720.0>--<100.0,82.0>> -> L<<100.0,82.0>--<100.0,50.0>>
	* uni5475: L<<105.0,720.0>--<105.0,88.0>> -> L<<105.0,88.0>--<105.0,50.0>>
	* uni5477: L<<95.0,720.0>--<95.0,90.0>> -> L<<95.0,90.0>--<95.0,50.0>>
	* uni547B: L<<95.0,720.0>--<95.0,95.0>> -> L<<95.0,95.0>--<95.0,50.0>> and 44 more. [code: found-colinear-vectors]

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
	* uni01EA: B<<663.0,67.0>-<600.0,17.0>-<515.0,-1.0>>/L<<515.0,-1.0>--<515.0,-1.0>> = 11.956584243149111
	* uni01EA: L<<515.0,-1.0>--<515.0,-1.0>>/B<<515.0,-1.0>-<452.0,-13.0>-<417.0,-36.5>> = 10.784297867562596
	* uni305D.002: B<<431.5,460.0>-<318.0,405.0>-<196.0,368.0>>/L<<196.0,368.0>--<900.0,433.0>> = 11.596294914960142
	* uni305D: B<<424.0,466.0>-<308.0,412.0>-<184.0,376.0>>/L<<184.0,376.0>--<900.0,420.0>> = 12.672658760691471
	* uni305E.BRACKET.499: B<<390.5,454.5>-<276.0,402.0>-<154.0,366.0>>/L<<154.0,366.0>--<870.0,410.0>> = 12.923832025344671
	* uni305E: B<<394.0,456.0>-<278.0,402.0>-<154.0,366.0>>/L<<154.0,366.0>--<870.0,410.0>> = 12.672658760691471
	* uni3069.BRACKET.766: B<<175.5,289.5>-<230.0,353.0>-<348.0,411.0>>/L<<348.0,411.0>--<336.0,407.0>> = 7.740341158837903
	* uni3086: B<<118.5,325.5>-<119.0,293.0>-<121.0,262.0>>/B<<121.0,262.0>-<136.0,348.0>-<176.5,421.5>> = 13.585306656186683
	* uni308A: B<<209.0,490.0>-<209.0,457.0>-<210.0,422.0>>/B<<210.0,422.0>-<227.0,514.0>-<275.0,583.0>> = 12.105751299328105
	* uni3091: B<<320.5,224.0>-<274.0,185.0>-<213.0,121.0>>/B<<213.0,121.0>-<265.0,155.0>-<306.0,165.0>> = 13.196323121176645 and 285 more. [code: found-jaggy-segments]

</details>
<br>
</details>
<details>
<summary><b>[8] Mplus2[wght].ttf</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---

A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.

The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.

Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;


Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.

When in doubt, please choose OFL for new font projects.


</pre>

* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
" Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]

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
<summary>🔥 <b>FAIL:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---

Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).


</pre>

* 🔥 **FAIL** Failed to lookup ligatures. This font file seems to be malformed. For more info, read: https://github.com/googlefonts/fontbakery/issues/1596 [code: malformed]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---

There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.

For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright


</pre>

* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 13) has trailing spaces that must be removed: 'This Font [...]l.org/OFL
'

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
	 periodcentered [code: spacing-mark-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---

Mark characters should be in the GDEF mark glyph class.


</pre>

* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 U+0305, U+030B, U+0324, U+032E, U+0331, U+3099 and U+309A [code: mark-chars]

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
	 U+00B7 [code: non-mark-chars]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 40 | 52 | 732 | 49 | 582 | 0 |
| 0% | 3% | 4% | 50% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
