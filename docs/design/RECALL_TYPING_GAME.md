# Recall Typing - Hidden Word / Spelling Game

## Status

~~~text
Architecture decision confirmed on 2026-09-19.
Design baseline defined.
Implementation has not started yet.
~~~

## 1. Product decision

Recall Typing is a separate game.

It is not a Monkeytype mode.

The platform should expose it alongside the other games:

~~~text
Home
Monkeytype
Vocabulary Shooter
Recall Typing
~~~

Planned route:

~~~text
https://typing-game.local/recall-typing
~~~

Planned internal origin:

~~~text
https://recall.typing-game.local
~~~

Planned repository:

~~~text
sinhvienaiti/recall-typing
~~~

The parent platform will mount it as:

~~~text
games/recall-typing
~~~

using a Git submodule.

---

# 2. Learning goal

The game trains active recall of English spelling.

The player should not simply copy visible English text.

Instead:

~~~text
meaning / pronunciation / IPA
→ recall the English word
→ type it
→ correct characters reveal progressively
~~~

This makes the game closer to spelling/dictation/recall exercises than to ordinary speed typing.

---

# 3. Core interaction

Example target:

~~~text
dependency
~~~

Initial display:

~~~text
_ _ _ _ _ _ _ _ _ _
~~~

Correct input:

~~~text
d
→ d _ _ _ _ _ _ _ _ _

e
→ d e _ _ _ _ _ _ _ _
~~~

Wrong input:

~~~text
x
→ target character stays hidden
→ error feedback
→ typing position does not advance
~~~

Once the whole word is correct:

~~~text
dependency
→ full word visible
→ success effect
→ next target
~~~

---

# 4. Phrase behavior

For a phrase:

~~~text
dependency injection
~~~

The spacing must remain structurally clear:

~~~text
_ _ _ _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _
~~~

Do not merge everything into one continuous unknown string.

Punctuation that provides useful structure should remain visible.

Examples:

~~~text
don't
→ _ _ _ ' _

end-to-end
→ _ _ _ - _ _ - _ _ _
~~~

The goal is spelling recall, not guessing punctuation layout.

---

# 5. Hint panel

A dedicated hint panel should sit above the typing area.

Recommended content:

~~~text
Vietnamese meaning
IPA
speaker button
~~~

Example:

~~~text
        sự phụ thuộc
        /dɪˈpen.dən.si/
             🔊

        _ _ _ _ _ _ _ _ _ _
~~~

This panel is separate from the word itself.

Do not use Monkeytype-style per-word translation bubbles here.

---

# 6. Pronunciation

When a new target becomes active:

~~~text
cancel old speech
→ pronounce the English target
~~~

A speaker button allows replay.

Pronunciation should use browser/system SpeechSynthesis and prefer installed voices so the core game remains offline-capable.

---

# 7. Vocabulary source

The game should use the same conceptual vocabulary model as Vocabulary Shooter:

~~~text
English
Vietnamese
IPA
~~~

Example:

~~~text
dependency | sự phụ thuộc | /dɪˈpen.dən.si/
~~~

The first implementation can keep its own local IndexedDB/storage to avoid premature shared-data architecture.

A future platform-level shared vocabulary library can synchronize multiple games when that becomes a real need.

---

# 8. Accuracy behavior

Recommended default:

~~~text
wrong character
→ one visible error pulse
→ do not advance
→ do not reveal the target character
~~~

Repeated wrong attempts at the same position should not produce noisy stacking animation/audio.

A scoring model can count:

~~~text
wrong attempts
first-try accuracy
corrected accuracy
word completion time
streak
~~~

The game does not need to reuse Monkeytype's internal result engine.

It should implement only the metrics useful for recall learning.

---

# 9. Recommended modes inside Recall Typing

The game itself can later support a small number of clearly related variants.

Recommended future variants:

~~~text
Recall
→ VN + IPA + audio hint

Listening
→ audio-first, VN optional

Hard Recall
→ VN hint only, pronunciation manual

Review Mistakes
→ prioritize words previously failed/slow
~~~

These all belong to the same recall/spelling learning family, so they can remain modes inside this game.

This is different from placing Recall inside Monkeytype, where the learning goal is too different.

---

# 10. Keyboard-first controls

The game should support:

~~~text
Tab or Escape
→ configurable quick restart

R or speaker shortcut
→ optional pronunciation replay
~~~

Exact shortcut selection can be tuned during implementation.

The player should be able to complete normal sessions without using the mouse.

---

# 11. Visual design

The visual style should feel like a learning game, not a plain form.

Recommended:

- large readable hidden slots,
- smooth reveal animation for correct letters,
- small error shake/pulse without revealing the answer,
- satisfying word-complete animation,
- subtle streak feedback,
- clean fixed hint panel,
- no layout jumping as words change length.

Avoid:

- heavy blur on every letter,
- per-character particle explosions,
- constant large transforms,
- anything that makes the spelling slots harder to read.

---

# 12. Performance rule

The game does not need Canvas unless later visual design truly benefits from it.

A DOM-based implementation is likely simpler and cheaper because:

- the main content is text,
- letter reveal is easy with classes,
- accessibility is better,
- no animation loop is required.

Performance goal:

~~~text
no permanent requestAnimationFrame loop
minimal DOM updates
CSS transitions only where useful
local/offline storage
local/system pronunciation
~~~

---

# 13. Offline-first rule

Core game must work offline after local setup/build.

Allowed local dependencies:

~~~text
static assets
IndexedDB
localStorage
browser/system SpeechSynthesis
~~~

Online services may be added only as optional features.

---

# 14. Proposed first implementation scope

Phase 1:

~~~text
independent Vite + TypeScript repo
game registry entry
submodule
nginx dev/play routes
vocabulary editor/import
hint panel
hidden letters
progressive reveal
wrong-character feedback
pronunciation/replay
quick restart
basic results
offline persistence
~~~

Phase 2:

~~~text
mistake history
review mode
streak/score polish
visual/audio polish
shared vocabulary integration if still needed
~~~

---

# 15. Why separate from Monkeytype

The architectural boundary is intentional:

~~~text
Monkeytype
→ visible-copy typing speed/accuracy platform

Recall Typing
→ hidden-answer recall/spelling game
~~~

A separate game gives the user one-click selection from the Game Library and keeps each codebase focused.

This decision also reduces custom divergence in the Monkeytype fork.
