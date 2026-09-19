# Monkeytype - Optional Recall Typing Mode

## Status

Implemented and reviewed on:

~~~text
sinhvienaiti/monkeytype
branch feature/en-vn-translation
revision e1667b2aee0ee384a13e3c4189a96e9da4388dd7
~~~

This mode is an optional extension of the existing Custom Text EN-VN learning feature.

It is not a replacement for the independent Recall Typing game.

---

# 1. Goal

Normal Monkeytype remains visible-copy typing.

The optional Monkeytype Recall mode is for mixed practice where dictionary-matched vocabulary inside a longer Custom Text can become hidden recall targets while the rest of the text keeps normal Monkeytype behavior.

---

# 2. Activation

Setting:

~~~text
recallModeEnabled
~~~

Default:

~~~text
false
~~~

Required context:

~~~text
Config.mode === custom
EN-VN translation enabled
dictionary is not empty
~~~

Only text that matches the dictionary is hidden.

Non-matching words remain visible.

---

# 3. Dictionary matching

Matching uses the same normalized EN-VN dictionary parser as the normal learning feature.

A shared helper chooses the longest matching phrase.

Example:

~~~text
dependency = sự phụ thuộc
dependency injection = tiêm phụ thuộc
~~~

For:

~~~text
dependency injection
~~~

the two-word entry wins.

Do not duplicate phrase-matching logic in the renderer.

---

# 4. Hidden-answer behavior

Before typing:

- recallable English letters/numbers in a matched target are hidden,
- structural punctuation stays visible,
- the word still occupies its normal layout space.

While typing:

- correct/corrected characters reveal progressively,
- incorrect target characters remain hidden,
- standard Monkeytype input/statistics logic remains authoritative.

Recall classes are attached during normal word rendering, not after the first keypress.

This prevents a brief answer flash and avoids a layout jump at test start.

---

# 5. Learning cue timing

Normal EN-VN mode keeps its first-typed-character learning trigger.

Recall mode additionally presents the matching learning cue when the recall target becomes the active word.

This matters because the English answer is intentionally hidden before the user begins typing.

One occurrence is still de-duplicated so backspace/retype does not repeatedly replay the same cue.

---

# 6. Translation presentation

Existing display settings are reused:

~~~text
tooltip
top
both
~~~

Existing tooltip behaviors are reused:

~~~text
hold
float
~~~

In Recall mode the top display hides the English source and shows the Vietnamese learning information without leaking the answer.

Held tooltips continue to use dataset/classes + CSS pseudo-elements because Monkeytype rewrites word inner HTML during typing.

---

# 7. Pronunciation

Existing English pronunciation settings are reused.

The recall target can be pronounced through browser/system SpeechSynthesis.

No new audio asset pipeline was introduced.

---

# 8. Three-line viewport

The EN-VN learning extension must preserve Monkeytype's normal line-window behavior.

The wrapper keeps the core-computed height.

Translation UI is allowed extra clip space above/sides, while typing content below the viewport remains clipped.

Do not use an unrestricted overflow rule that exposes all generated Custom Text lines.

---

# 9. Persistence

The setting is stored inside:

~~~text
personalEnVnTranslationSettings
~~~

Older saved settings migrate with Recall mode disabled unless a valid stored value already exists.

---

# 10. Verification

The custom branch has a dedicated CI workflow that verifies:

~~~text
frontend lint
type-aware lint
test.scss stylelint
local-static production build
full frontend test suite
~~~

Final reviewed workflow result for revision 39b6112...:

~~~text
PASS
~~~

The review also fixed unrelated/pre-existing corrected-error test/type metadata issues found by the full branch checks rather than hiding or skipping them.

---

# 11. Overlapping phrase boundary guarantee

Recall target hiding and recall learning cues use the same greedy longest-match boundaries.

The render phase computes the recall phrase starts and marks only those start words.

The active/started-word cue path reads that rendered marker instead of independently treating every dictionary-matching word as a fresh phrase start.

This prevents a shorter entry inside a longer selected phrase from firing twice.

Regression example:

~~~text
dependency injection = tiêm phụ thuộc
injection = tiêm
~~~

For the text:

~~~text
dependency injection
~~~

only the two-word phrase starts a recall cue.

Final reviewed revision:

~~~text
e1667b2aee0ee384a13e3c4189a96e9da4388dd7
~~~

Dedicated Custom EN-VN CI is green at this revision.

