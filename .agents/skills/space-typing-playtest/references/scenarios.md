# Browser tooling and scenarios

## Current tooling

Read [visual guide](../../../../games/space-typing/docs/VISUAL_TESTING.md), [shot.mjs](../../../../games/space-typing/scripts/visual/shot.mjs) and [package scripts](../../../../games/space-typing/package.json) for current flags. Historical machine paths/process-cleanup examples in the guide are not instructions to kill unrelated services; use the detected checkout and your own process handle.

`visual:shot` launches isolated Chrome via CDP, captures PNG and prints JSON with evaluation, warnings/errors and exceptions. It requires compatible Node and Chrome; override `CHROME_PATH` if detection is wrong. A physical CDP click counts as a gesture; its hidden-element `el.click()` fallback is not proof of pointer interaction. Inspect diagnostics and the image, not just exit status.

From repo root, against a verified server:

```bash
pnpm --dir games/space-typing -s visual:shot "http://127.0.0.1:3098/" .visual/game.png --width=1642 --height=799 --dpr=2 --click=#startButton --wait=20000 --eval-file=scripts/visual/evals/game-assets.js
```

Port 3098 is an example, not a discovery guarantee. Package-relative paths resolve inside `games/space-typing`; put artifacts in its ignored `.visual/` or task temp directory. The documented 1642×799 DPR 2 is a desktop reference; also inspect the actual user surface and a narrower supported viewport for layout changes.

Root `dev:space` cleans fixed ports: inspect [root scripts](../../../../package.json) before using it in a shared session. An isolated Vite process on an unused port with `--strictPort` avoids disruption. Play mode needs a current build; a healthy static nginx page does not prove Admin/account/duel backends are live.

| Scope | Exercise and evidence |
| --- | --- |
| 2D typing/combat | Start representative stage; acquire/complete word, wrong then corrected input, word boundary, skill; inspect visibility, projectile arrival, threat feedback and results |
| IME | Native English/Vietnamese, Windows UniKey + Chrome, macOS EVKey + Chrome when available; follow typing-input-ime. DOM-dispatched composition is not OS input and one headless browser does not prove cross-platform acceptance |
| Test Lab | [Direct launch](../../../../games/space-typing/src/test-lab/direct-launch.ts) supports `?testLab=1` when the button is exposed. Check [testing policy](../../../../games/space-typing/src/admin/game-testing-policy.ts); verify effective character/stats/scene after apply/restart rather than form values |
| Duel | Correct input through spawn/travel/confirmed impact/damage, HP/lives, low-HP/victory feedback, missile/bomb and announcer; use two clients for online sync and label bot/local tests |
| Campaign 3D | Inspect [visual scenarios](../../../../games/space-typing/scripts/visual/scenarios/) and [isolation tests](../../../../games/space-typing/tests/mode-isolation.test.ts); check camera, labels, turn/input, animation and storage separation |
| Admin | Select entity/media, edit supported value, preview, invalid input/request failure, save/publish only within authorization, check apply boundary, candidate isolation and teardown |
| VFX/audio | Normal-speed plus slow-frame inspection, typing readability, overlap, fallback, mute/pause/restart and gesture; offline metrics/fake microphone do not prove listening/live capture quality |
| Performance | Matched baseline/candidate viewport/DPR/quality; [Batch F procedure](../../../../games/space-typing/docs/UI_UX_BATCH_F_BROWSER_QA.md), frame reports and repeated transitions |
| Portal/responsive | Actual iframe plus standalone child, supported narrower viewport, modals/focus/HUD; choose correct frame/context for cross-origin input, and report embed coverage separately |
| Rift Defense | [V2 plan](../../../../games/space-typing/docs/SPACE_TYPING_DEFENSE_PLAN_V2_2026-10-18.md) is a draft; [benchmark](../../../../games/space-typing/defense-bench.html) measures rendering, not a playable Defense mode |

## Support and limits

- [R01 QA](../../../../games/space-typing/scripts/visual/r01-campaign-qa.mjs) captures a specific map at port 3098. Inspect scope/port before running; it is not a full playtest.
- [Evaluation scripts](../../../../games/space-typing/scripts/visual/evals/) probe assets/FX/performance. Confirm dev hooks exist before using them against Play; label state injection.
- [M22 matrix](../../../../games/space-typing/docs/M22_MANUAL_PLAYTEST_MATRIX.md) and [visual/audio hardening](../../../../games/space-typing/docs/RUNTIME_VISUAL_AUDIO_TEST_LAB_HARDENING_PLAN.md) provide historical cases. Reconcile with current source; do not reuse old completion claims as current evidence.
- A screenshot proves one visible frame; timed frames/video can prove animation; interaction traces demonstrate behavior; unit tests protect contracts. Identify evidence for each claim.
