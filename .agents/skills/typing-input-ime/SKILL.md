---
name: typing-input-ime
description: Diagnose or change Space Typing keyboard, correction, accuracy and Vietnamese IME behavior; use for composing text, Backspace, caret, word boundaries or English input regressions.
---

Read [the input map and acceptance matrix](references/input-contracts.md). Distinguish English combat safely ignoring composition from an actual Vietnamese text-entry pipeline; current Space Typing does not implement the latter.

1. Identify the surface and scoring contract: 2D combat, Campaign 3D, Duel, editable UI field, or separate Monkeytype integration. Capture the smallest failing sequence and expected result.
2. Trace `keydown`, `beforeinput`, `input`, `compositionstart`, `compositionupdate` and `compositionend` as available. Keep committed DOM text, caret/selection, composition state, physical Backspace intent, target identity and scoring separate.
3. Never treat composition as ordinary keydown input or score provisional characters. Reconcile committed replacements/deletions once. An IME-generated `deleteContentBackward` alone does not prove a user deletion.
4. Preserve English behavior and target/word ownership. Do not add speculative Telex reversal or accent stripping to English combat without traces and an explicit scoped requirement. Future Vietnamese support needs the full regression matrix.
5. Add a focused regression for changed behavior, run neighboring ownership/scoring tests, and track real Windows/UniKey and macOS/EVKey checks separately. Synthetic events do not certify native IMEs.

Use `voice-typing-runtime` for speech and `realtime-duel-pvp` for fairness/authority. Keep the current correction policy unless the task changes it.
