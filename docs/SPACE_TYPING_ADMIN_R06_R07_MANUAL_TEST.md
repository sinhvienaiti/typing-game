# Space Typing Admin — R06/R07 Manual Acceptance Checklist

Updated: 2026-10-12

## Status

**MANUAL ACCEPTANCE: NOT TESTED**

This checklist intentionally remains `NOT TESTED` until the user runs the checks on the real local Play build. Automated CI, source review, screenshots from old runs, and static analysis must never be used to mark these items `PASS`.

Manual acceptance is a release/merge gate, not a blocker for independent technical implementation. If a later code change touches a tested area, mark that evidence `STALE` and re-run the affected item.

## Test setup

Use the latest `feat/space-typing-admin-uiux` parent branch with its current `games/space-typing` pin. Build and launch the normal local Play flow. Test at least one desktop viewport around 1920×1080 and one narrower desktop viewport around 1365×768.

For each item record one of: `PASS`, `FAIL`, `STALE`, `N/A`. Keep the default as `NOT TESTED` until actually exercised.

## M01 — Admin control plane and runtime service

Status: `NOT TESTED`

- Open `/admin/space-typing` through the normal local Play entry point.
- Confirm the shell renders operator-facing connection state rather than raw implementation milestone copy.
- Visit representative read-only and editable screens.
- Confirm real Admin API responses are used; no HTML-as-JSON/parser error is shown.
- Confirm a temporarily unavailable service resolves to a bounded error state with useful recovery guidance rather than an endless loading state.
- Confirm Retry works where offered.

## M02 — Navigation, command search, keyboard and focus

Status: `NOT TESTED`

- Expand/collapse sidebar groups and confirm the active route remains discoverable.
- Use keyboard only to traverse sidebar/group controls and page actions.
- Open command search with Cmd+K on macOS or Ctrl+K on Windows/Linux.
- In command search, verify Arrow Up/Down, Home, End, Tab/Shift+Tab and Escape.
- Confirm focus is restored to the previous control after closing the palette.
- Confirm visible focus states are clear.
- With a screen reader if available, confirm command result count/no-result updates are announced and result labels are understandable.

## M03 — Responsive/layout acceptance

Status: `NOT TESTED`

- At roughly 1920×1080, confirm sidebar/topbar/content spacing is stable and no critical content is clipped.
- At roughly 1365×768, confirm navigation remains usable without page-level horizontal overflow.
- Confirm long labels remain understandable and tables/panels scroll only inside intended containers.
- Confirm sticky regions do not cover controls or page content.
- Confirm narrow layouts do not hide the command-search affordance or active route context.

## M04 — Audio defaults, voice capability and mode boundaries

Status: `NOT TESTED`

- Open Audio Defaults and relevant voice/capability diagnostics.
- Confirm displayed capability/mode state matches the running child runtime.
- Confirm unsupported capability is explained as unsupported, not fabricated as editable.
- Confirm changing Admin-owned audio defaults does not overwrite player-owned preferences unexpectedly.
- Confirm pronunciation does not reintroduce unwanted BGM ducking.

## M05 — World/Stage music and fallback behavior

Status: `NOT TESTED`

- Inspect Global/Galaxy/World/Stage assignments and canonical preview.
- Confirm effective precedence/fallback shown by Admin matches the game runtime.
- Confirm random-normal behavior does not incorrectly inherit Stage/World/Galaxy normal overrides.
- Exercise at least one missing/invalid candidate and confirm fallback is safe and diagnostics remain understandable.

## M06 — Duel/PvP event matrix and six-life behavior

Status: `NOT TESTED`

- Open Duel/Ranked/Alternative Modes diagnostics and confirm ownership/read-only boundaries are clear.
- In actual PvP/Duel gameplay, verify the intended six-life rule.
- Verify representative event/announcer transitions and projectile/damage timing remain coherent.
- Confirm unavailable alternative-mode authority is not presented as a fake editable Admin setting.

## M07 — Economy defaults, expansion currency, rewards and stamina

Status: `NOT TESTED`

- Inspect Shop, Currencies, Rewards & Drops and Stamina/Warp.
- Confirm displayed default currency/player-life/economy values match actual runtime behavior.
- Confirm expansion currency symbol/value presentation is correct.
- Confirm reward/drop and stamina values do not imply an Admin mutation boundary where only runtime read ownership exists.
- Exercise one normal stamina consumption/regeneration path in game and compare with Admin diagnostics.

## M08 — Safe-zone, fallback and stale-state behavior

Status: `NOT TESTED`

- Exercise a safe-zone/rest/fallback path that is visible to the Admin/runtime contracts.
- Confirm stale or missing runtime data produces a bounded fallback/error state rather than stale success text.
- Confirm actions depending on unavailable state are disabled or withheld.
- Confirm technical details remain secondary to operator-facing copy.

## M09 — Child runtime loader and pinned-child coherence

Status: `NOT TESTED`

- Start from a clean Play launch so the Admin bridge and child runtime are freshly loaded.
- Confirm the child game starts from the parent-pinned revision without stale-process reuse.
- Visit representative contract-backed Admin screens and confirm they match current game behavior.
- Confirm no older child branch semantics appear after restart.

## M10 — Error, empty, unsupported and read-only presentation

Status: `NOT TESTED`

- Exercise at least one loading, empty, unsupported and recoverable-error state.
- Confirm no raw `TypeError`, stack-like text, `Unexpected token '<'`, or implementation-only exception appears as the primary message.
- Confirm read-only screens do not visually imply Save Draft/Publish authority.
- Confirm editable screens clearly distinguish active/published state from draft/validation/publish actions.

## M11 — QA Sandbox isolation

Status: `NOT TESTED`

- Launch QA Sandbox/Test Lab from Admin.
- Confirm the test session uses real runtime systems but does not mutate Campaign progression or production profile state.
- Exit and reopen normal Campaign; verify progression/resources were not changed by QA-only actions.

## M12 — Final smoke across A01–A30

Status: `NOT TESTED`

- Open every registered Admin screen once.
- Confirm no blank page, uncaught exception, endless loading state, broken navigation target or obviously stale implementation copy.
- For each screen, confirm the primary UI makes clear what can be inspected/changed and whether it is read-only or editable.

## Result recording

When manual testing is performed, append date, environment/browser, tested parent HEAD, tested child SHA, and per-item result below. Do not replace historical failures; add a new result block so regressions remain traceable.

### Result block

- Date: `NOT TESTED`
- Parent HEAD: `NOT TESTED`
- Child SHA: `NOT TESTED`
- Browser/OS: `NOT TESTED`
- Overall result: `NOT TESTED`
- Failed items / notes: `NOT TESTED`
