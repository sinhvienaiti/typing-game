# Input contracts and acceptance

## Current pipeline

| Surface | Source/tests | Boundary at skill creation |
| --- | --- | --- |
| 2D Campaign/Recall | [Main keydown](../../../../games/space-typing/src/main.ts), [controller](../../../../games/space-typing/src/input/input-controller.ts), [Game](../../../../games/space-typing/src/Game.ts), [priority tests](../../../../games/space-typing/tests/game-input-priority.test.ts) | Window keydown skips composing/Process; dialogs own input. Game scores English target letters. This is not a committed Vietnamese text field. |
| Campaign 3D | [Key helpers](../../../../games/space-typing/src/scene3d/keys.ts), [entry/trace](../../../../games/space-typing/src/campaign3d/main.ts), [tests](../../../../games/space-typing/tests/campaign3d-keys.test.ts) | ASCII a-z only; composition/Process/229 skipped; accented replacement keys cause an IME notice, not scoring. `__campaign3d.keyTrace(true)` captures received keys. |
| Duel | [Parser](../../../../games/space-typing/src/duel/typing.ts), [battle input](../../../../games/space-typing/src/duel/battle-ui.ts), [tests](../../../../games/space-typing/tests/duel-contracts.test.ts) | ASCII input skips composition/shortcuts/repeat and sends `TYPE_CHAR`. Authored-token normalization is separate from live input scoring. |
| Hybrid ownership | [Ownership](../../../../games/space-typing/src/input/target-ownership.ts), [tests](../../../../games/space-typing/tests/input-ownership.test.ts) | First accepted keyboard input owns that word/layer. Reset/correction must not reopen voice eligibility. |
| Separate Monkeytype integration | [Native acceptance matrix](../../../../games/monkeytype/docs/CUSTOM_VIETNAMESE_IME_ACCEPTANCE.md), [runtime enhancements](../../../../games/monkeytype/frontend/src/ts/custom/en-vn-translation/runtime-enhancements.ts) | Useful traces/correction evidence. Its editable-text/scoring options must not be silently imposed on combat. |

Browser/OS IMEs expose composition events; external UniKey/EVKey may swallow Telex modifier keys and emit deletion plus accented replacements. A key the page never received cannot be recovered from its `code`. Capture native traces before choosing a fix.

## Requirements for future Vietnamese support

These are requested acceptance requirements, not implemented Space Typing capabilities.

- Separate provisional composition from committed scorer state. Reconcile committed DOM text/selection and prevent `compositionend` plus following `input` from scoring twice.
- Validate NFC-equivalent text deliberately. Cover a/ă/â/e/ê/i/o/ô/ơ/u/ư/y, each with no tone plus grave, acute, hook, tilde and dot; lower/upper case and `đ/Đ`. Stripping accents is not Vietnamese correctness.
- Handle multiple-character rewrite (`uo` → `ươ`), tone replacement on an earlier vowel, selection replacement, middle insertion and logical caret position across reconciliation.
- Define accuracy for genuine wrong input, provisional rewrites, corrected errors and repeated blocked errors. Preserve current forgiveness/error policy unless explicitly changed; do not double-charge IME rewriting.

## Regression matrix

Run on Windows + UniKey + Chrome, macOS + EVKey + Chrome, English keyboard, and OS/browser Vietnamese keyboard. Record versions/input mode; do not assume universal event ordering.

| Case | Examples/checks |
| --- | --- |
| English regression | `raw software fast draw wax jazz`, `good is how`; preserve literal English letters. |
| Shape/tone matrix | `ă â ê ô ơ ư đ`, all tone combinations; `rằng tiếng người đường thường`; tone-before-shape and shape-before-tone. |
| Correction | Wrong → corrected; wrong tone → right tone; Backspace/retype; delayed delete after keyup; IME deletion without physical Backspace. |
| Boundaries | Space/punctuation before compositionend; final composed character; previous-word Backspace; next target/layer; completion during commit. |
| Caret | Selection replacement; left/right; insertion/deletion by composed grapheme; declare unsupported caret editing explicitly for combat. |
| Ownership/controls | Focused modal/input; hotbar; shortcut/repeat; stale key into next target; Hybrid typing A and speaking B. |

Capture event type, key/code/keyCode, `isComposing`, `inputType`, `data`, DOM value/selection, target/unit, accepted hits/misses and accuracy. Prefer bounded existing development traces.

From platform root: `pnpm --dir games/space-typing exec vitest run tests/campaign3d-keys.test.ts tests/duel-contracts.test.ts tests/game-input-priority.test.ts tests/input-ownership.test.ts`. Add native IME/browser checks with `space-typing-playtest` for input changes.
