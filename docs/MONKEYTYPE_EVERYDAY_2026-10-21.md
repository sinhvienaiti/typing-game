# Monkeytype Everyday — 2026-10-21

Everyday is available under **custom → change → Everyday** on the local Monkeytype site. Select an Adobe Commerce lesson and **passages per session**, then press **ok**. The typing screen shows muted, theme-aware **prev / next** controls and the current lesson and passage range. The completed result screen has a separate, centered **prev / replay / next** footer below the chart, statistics and existing result controls. Replay restores the same original passage range without advancing progress.

## Content and navigation

- Source: `games/monkeytype/adobe_commerce_lessons_1_180_package/02_Typing_Files`. Learning guides are excluded. Source files are unchanged.
- One nonempty physical line is one authored passage. Both blank-line-separated files and files with consecutive paragraph lines are supported; BOM and CRLF are handled.
- The package currently contains 180 files, representing **178 unique lessons and 2,293 passages**. Unnumbered `full_page_caching_typing.md` and `partial_caching_typing.md` duplicate lessons `00` and `01` byte for byte. Numbered IDs are preserved, including existing gaps at 41, 49 and 59.
- Text loads one lesson at a time. The complete corpus is not included in the initial application bundle.
- A session contains up to the selected number of complete passages in their original order. A final short group stays within its lesson; next moves to the following available lesson. The final lesson does not wrap to the beginning.
- Progress stores the original starting passage and the actual ending passage, plus previous starting positions. Changing the session size keeps the current starting passage; next starts at the current ending passage. Returning to a lesson and reloading preserve its position.
- Progress is committed after preparation succeeds. Failed dictionary loads keep the previous text and Everyday progress. Navigation is guarded against repeated clicks, concurrent settings changes, restarting/results and the existing no-quit rule.

## Existing learning features

Everyday uses the existing custom-text engine, finite word limits and restart event. Existing dictionary, translation, popup, pronunciation, accent, rate, volume and text-reader preferences are retained. Library dictionaries refresh for the newly selected text; custom/topic/word-type/grammar choices are retained.

Normal, Learn, Recall and Listen keep their existing behavior. IPA is visible in Learn/Recall where a shared vocabulary entry supplies it; Normal and Listen retain their existing IPA visibility rules. Valid metadata for the cached dictionaries now survives reload, so IPA does not disappear after refreshing the page. Sentence Builder, Context/Cloze and Smart Review retain their separate exercise sources; Everyday prompts for a compatible mode before applying a lesson.

## Verification

From `games/monkeytype/frontend`, the installed local executables were used to avoid the package manager attempting a dependency reinstall:

```sh
../node_modules/.bin/oxlint --format agent --type-aware --type-check <changed source and test files>
../node_modules/.bin/vitest run __tests__/custom/everyday-lessons.spec.ts __tests__/custom/everyday-sessions.spec.ts __tests__/custom/everyday-runtime.spec.ts __tests__/custom/typing-text-library.spec.ts __tests__/custom/en-vn-translation/library.spec.ts __tests__/custom/en-vn-translation/speech.spec.ts __tests__/custom/en-vn-translation/text-reader.spec.ts __tests__/custom/en-vn-translation/dictionary.spec.ts
LOCAL_STATIC=true ./node_modules/.bin/vite build
```

Result: **67 tests passed across 8 files**, scoped type-aware lint/type checking passed, the local production build passed, and **12 browser checks passed**.

The browser pass uses headless installed Chrome against the actual nginx-served production build at `https://monkeytype.typing-game.local`, with fresh browser profiles. It exercises the visible source selector, themed lesson dropdown, session count, Prev/Next, count changes `3 → 1 → 3`, reload, final partial groups, lesson boundaries, disabled final Next, translation, native English speech dispatch, Learn/Recall/Listen, IPA after reload, dictionary network failure, and a 390px viewport. Persisted typing words are compared against the original lesson text at each navigation step. Mobile controls have 44px targets. Desktop and mobile screenshots were inspected.

Evidence is saved locally in `.local/monkeytype-everyday-qa/`:

- `report.json`
- `desktop-modal.png`, `desktop-typing.png`, `mobile-typing.png`
- `desktop-translation.png`, `desktop-translation-ipa.png`, `desktop-ipa-after-reload.png`

The browser test is scoped to the changed typing and navigation flows; no 3D/canvas harness or runtime test hooks were added. Existing local backend requests to `localhost:5005` fail in this environment and are recorded separately from feature errors. Speech dispatch was verified; headless execution does not establish perceptual audio quality. Synthetic typing does not establish native macOS/Windows IME acceptance.

## Follow-up: fixed tabs, live build and completion controls

The earlier browser check did not follow `docs/VISUAL_TESTING.md` and did not finish an entire typing session. The follow-up uses that document's **1642×799, DPR 2** viewport, isolated Chrome profiles, the installed GPU-enabled Chrome, direct Play-mode URL, before/after captures and enlarged detail crops.

The old default/custom tab bar was sticky inside the content that scrolled behind it. The desktop modal now has separate left and right scroll areas; the right header stays outside its content scroller. Both tabs are exercised using real mouse wheel input, including the long custom settings panel. The header remains at the same position and content is clipped below it.

The standalone URL `https://monkeytype.typing-game.local` serves `games/monkeytype/frontend/dist`; Portal embeds that same host. The served HTML and main JS were compared byte for byte with the rebuilt files. The browser's pre-existing cache was not inspected. Use **Cmd+Shift+R** on that host and reopen the modal to request the new assets; no learning data reset is needed.

The Monkeytype-only build was run with its existing installed tools, including Madge and Vite:

```sh
LOCAL_STATIC=true npm --prefix games/monkeytype/frontend run build
```

For later changes, the repository entrypoint is `pnpm build:monkeytype`. Merely opening `play.sh` does not rebuild the game.

The official visual runner and crop tool were used:

```sh
node games/space-typing/scripts/visual/shot.mjs https://monkeytype.typing-game.local games/space-typing/.visual/monkeytype-everyday/after-modal-scroll.png --wait=1000 --ready="!!document.querySelector('.pageTest button')" --eval-file=scripts/visual/evals/monkeytype-custom-scroll.js
node games/space-typing/scripts/visual/crop.mjs games/space-typing/.visual/monkeytype-everyday/after-modal-scroll.png games/space-typing/.visual/monkeytype-everyday/after-tabs-detail.jpg --rect=2100,100,710,360 --width=1000
```

`after-shot.json` reports `1642x799@2`, a `3284x1598` PNG, `tabTopBefore=64`, `tabTopAfter=64`, a static header with its own content scroller, and `exceptions=[]`. Its Firebase configuration log is an existing local-environment warning.

The completion browser scenario types all original characters with trusted browser input and verifies 100% accuracy. It measures the new footer below the result wrapper and centered in the viewport, then uses Replay, Next and Prev from actual completed sessions. The existing Everyday browser regression checks are also rerun.

Follow-up screenshots and diagnostic reports live in `games/space-typing/.visual/monkeytype-everyday/`, alongside the visual runner's ignored artifacts. Delivery hashes are saved in `.local/monkeytype-everyday-qa/delivery-followup.json`. No visual-runner or Space Typing source was changed.

Scoped type-aware lint/type checking and **74 tests across 9 files** passed. The **12 existing Everyday browser checks** and **7 follow-up browser checks** passed. Three full typing runs reached the real result screen with **100% accuracy**, exercising Replay, Next and Prev. The 390px completion layout keeps all three controls visible with 44px targets.

Final visual evidence includes `desktop-complete.png`, `desktop-complete-replayed.png`, `desktop-complete-next.png`, `mobile-complete.png`, `desktop-default-scroll.png`, `desktop-custom-scroll.png`, and three detail crops. `followup-report.json` records the flow checks; the pre-existing local backend configuration exception is listed separately from new feature errors. No new feature JavaScript errors were observed.

## Typing controls below the mascot

Typing navigation now aligns to the bottom of the playing area. When the monkey option is enabled, its navigation reserves space below the original 200px mascot before typing starts; the first keystroke does not change that reserved space. Short screens can scroll naturally to the controls. Completion navigation retains its existing placement.

The local production build was rebuilt. Native typing with the monkey enabled was captured at 1642×799 DPR 2, 1366×650 DPR 2, and 390×844 DPR 2. At all three sizes, the visible mascot ends **28px above** the navigation, and navigation ends **44px above** the footer. Next/Prev retained the two-passage boundaries. The five navigation component tests, scoped type-aware lint and diff checks passed.

Evidence: `games/space-typing/.visual/monkeytype-everyday/monkey-nav-desktop.png`, `monkey-nav-short.png`, `monkey-nav-mobile.png`, and `monkey-nav-metrics.json`; before captures have the `monkey-nav-before-` prefix.

## Learning settings and translation position — 2026-10-22

Learning-mode buttons now size their columns to the sidebar instead of forcing six columns at the viewport's small breakpoint. Help labels use a shared Solid component: their descriptions render in the dialog outside its clipped scroll panes, stay inside the viewport, support hover and keyboard focus, and dismiss on Escape, scroll or resize.

Under EN-VN translation, `display` chooses `tooltip`, `panel` or `both`; the existing stored `top` display-mode value still means panel. The new `position` chooses `top` or `bottom` for both word bubbles and the learning panel. Existing settings migrate to `top`. Bottom panels have a reserved minimum-height lane before typing begins, below the words and above the mascot. Test initialization and typing now share the same appearance function, including after reload. Held labels follow visible words, pack adjacent labels without covering each other, wrap long meanings and clear on restart/completion. English/Vietnamese panel text wraps rather than being ellipsized. Pronunciation, IPA and Recall/Listen visibility are preserved.

The Monkeytype-only Madge/Vite production build passed and was exercised on `https://monkeytype.typing-game.local`. Scoped type-aware lint, stylelint and diff checks passed; **38 tests across 7 translation/help files** passed. Native browser interactions covered desktop 1642×799 DPR 2, tablet 1024×768, mobile 390×844, all six learning-mode labels, complete help text, keyboard dismissal, position selection, reload, eight Normal/Learn/Recall/Listen position/behavior cases, unchanged first-word position on the first keystroke, non-overlapping held labels, English speech dispatch, IPA, long Vietnamese meanings and disabling translation. A full 230-word source session reached completion, and Replay cleared the held labels. This accelerated automated run was marked invalid for WPM by the existing scoring rules; completion controls and tooltip cleanup were verified, not score eligibility.

The documented visual runner was used on the final build:

```sh
node games/space-typing/scripts/visual/shot.mjs https://monkeytype.typing-game.local games/space-typing/.visual/monkeytype-learning/official-settings.png --wait=1000 --ready="!!document.querySelector('#words .word')" --eval-file=scripts/visual/evals/monkeytype-learning-settings.js
```

`official-settings.json` reports 1642×799 DPR 2, six fitting labels, the complete help description outside the scroll pane, both position choices and `exceptions=[]`. The existing Firebase configuration log remains. Longer runtime checks record the pre-existing unavailable `localhost:5005` configuration request separately; no new feature exceptions were observed. Speech requests were inspected; perceptual audio and native operating-system IME were not revalidated by this UI change.

Before/after screenshots, full typing/completion captures and JSON reports are in `games/space-typing/.visual/monkeytype-learning/`. Inspected detail crops include `settings-detail.jpg` and `bottom-detail.jpg`; `after-help-mobile.png` shows the complete mobile help description. The temporary dev server on port 3097 was stopped.

## Git delivery validation

Before committing, all changed Monkeytype source/test files were formatted with the installed formatter. The complete frontend suite passed **1,393 tests across 72 files**; full frontend type-aware lint, changed-style lint, the local-static production build and the parent Play-build configuration validator passed. Only the complete-corpus test has a 30-second timeout: it imports all 178 raw modules and exceeded the default five seconds under simultaneous full-suite/build/lint load; every content assertion is unchanged.

Delivery includes all 180 files in `02_Typing_Files`, including the two duplicate aliases required by corpus checks. The 181 unreferenced authoring guides in `01_Learning_Files` remain local. One authored typing file has eight CRLF lines mixed with LF and no trailing spaces; its original bytes are preserved, with the staged whitespace check using `core.whitespace=cr-at-eol`.
