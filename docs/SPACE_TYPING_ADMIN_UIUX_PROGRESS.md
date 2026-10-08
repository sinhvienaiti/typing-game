# Space Typing Admin UI/UX Progress

## PROJECT STATE
STATUS: PHASE_B_COMPLETE_CANONICAL_CLEANUP_GREEN

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- Latest fully validated implementation HEAD before this metadata checkpoint: `f158945f20257fec8add85a71aba0e01f2c95b83`
- PR: #49 — OPEN, DRAFT, mergeable at latest review
- Space Typing Admin CI #596: PASS on `f158945f20257fec8add85a71aba0e01f2c95b83`.
- Platform CI #1575: PASS on `f158945f20257fec8add85a71aba0e01f2c95b83`.

Child:
- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/admin-world-music-stage-policy`
- Validated HEAD: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
- Child CI #1759: PASS.
- Parent `games/space-typing` is pinned to exactly that tested child SHA.

## COMPLETED MILESTONES
All 30 registered Phase B Admin screens have an explicit audited ownership/status mapping and production routing. Do not redo these unless a newer commit regresses them:
- Overview / Analytics telemetry — DONE
- Audio Defaults — DONE
- Music Library — DONE
- World / Stage Music — DONE
- Ships — DONE
- Equipment — DONE
- Skills — DONE
- Enemies — DONE
- Bosses — DONE
- Worlds & Stages — DONE
- Typing Content — DONE
- Shop — DONE
- Currencies — DONE
- Rewards & Drops — DONE
- Stamina / Warp — DONE
- Missions — DONE
- Daily / Weekly — DONE (Daily canonical; Weekly explicit runtime absence)
- Expedition — DONE
- Events — DONE
- Duel — DONE
- Ranked — DONE
- Alternative Modes — DONE as explicit runtime-absence diagnostic; no fake runtime introduced
- Backgrounds — DONE
- VFX — DONE
- UI Assets — DONE
- General Settings — DONE
- Feature Gates — DONE
- History & Publish — DONE
- QA Sandbox / Test Lab — DONE

## CANONICAL-ONLY LEGACY CLEANUP — CLOSED CHECKPOINT
A follow-up cleanup audit found that production routing had been made Phase-B-only, but some presentation dependencies were still owned indirectly by dead mock modules.

### Canonical style/font ownership
- Shared Phase B `.stx-*` layout/control styles moved from legacy `space-typing-extended.css` to canonical `portal/src/admin/space-typing-phase-b.css`.
- The production `space-typing.ts` shell now imports that stylesheet directly.
- The production shell also imports the bundled Exo 2 weights 600/700/800 and Be Vietnam Pro weights 400/500/600/700 directly; font loading no longer depends on a dead mock-data module side effect.
- `validate-space-admin-ui.mjs` now requires the canonical stylesheet, critical shared selectors and every bundled font import.

### Dead mock module removal
The following files were proven unreachable from the canonical production shell and removed:
- `portal/src/admin/space-typing-mock.ts`
- `portal/src/admin/space-typing-extended.ts`
- `portal/src/admin/space-typing-extended.css`
- `portal/src/admin/space-typing-daily-weekly.ts`
- `portal/src/admin/space-typing-dialogs.ts`
- `portal/src/admin/space-typing-dialogs.css`
- `portal/src/admin/space-typing-world-music-v2.ts`

`space-typing-world-music-v2.css` remains intentionally because the canonical Phase B World Music implementation still consumes those styles.

CI now explicitly fails if any of the seven removed legacy modules reappears.

### Missions / Daily-Weekly stale boundary cleanup
- Missions previously still labeled the Daily / Weekly navigation action as `UI mock` even after Daily/Weekly had been integrated as a canonical partial read-only runtime boundary.
- The stale label was removed.
- `validate-space-admin-missions.mjs` no longer reads the deleted mock renderer. It now validates `space-typing-daily-weekly-phase-b.ts`, the authenticated Daily/Weekly contract endpoint, Daily runtime ownership, explicit Weekly absence and the no-synthetic-authoring boundary.

## FINAL PR REGRESSION TRIAGE — CLOSED CHECKPOINT
The final PR review found real integration defects even though the earlier validator chain was green. These are fixed and permanently guarded.

### Production Admin shell routing
- The old shell previously intercepted `/admin/space-typing` before the Phase B router and rendered the legacy mock Overview (`UI MOCK DATA`).
- The production shell is now Phase-B-only: every registered route is delegated through `renderPhaseBAdminScreen`; unknown routes terminate at an explicit unknown-screen guard.
- Root Overview and Analytics resolve to the authenticated runtime telemetry owner instead of synthetic dashboard numbers.
- Music Library resolves to the authenticated runtime catalog/asset service instead of the mock upload/list screen.
- Daily/Weekly, World Music, Duel, Ranked, Alternative Modes, Events and all other registered domains no longer have a reachable legacy renderer fallback.
- Legacy `/admin/space-typing/flags` is normalized to canonical `/admin/space-typing/feature-gates`; navigation and command palette use `Feature Gates` directly.

### Play-mode Admin runtime bridge freshness
- `play.sh` previously reused any responsive process on port 3199, which could leave a newly built Portal talking to an old `admin/server.mjs` after source updates.
- Play startup now cleans project-owned port 3199 together with other local runtime ports, starts a fresh Admin bridge from current source, records its PID, verifies that the new PID remains alive and requires the runtime endpoint to respond before continuing.
- The existing `cleanup-dev-ports.sh --project-only` ownership check prevents this from killing unrelated processes outside the repository.

### Regression-validator hardening
- `validate-space-admin-ui.mjs` no longer protects mock milestone behavior. It requires all 30 mapped Phase B routes, canonical production routing, canonical style/font ownership and explicit runtime bindings.
- It fails if the production shell imports mock data, advertises `UI MOCK DATA`, calls legacy renderers, wires the old mock Music Library dialog, loses shared Phase B styles/fonts, or recreates deleted legacy modules.
- It also rejects unfinished Phase B map markers (`backend-foundation`, `ui-prototype-not-runtime-connected`, `mapped-awaiting-*`).
- Events, Duel, Ranked and Alternative Modes validators require the legacy fallback to be unreachable from the production shell.
- Runtime evidence, ownership, read-only/write boundaries and unsupported-field assertions were retained; validator semantics were strengthened rather than weakened.

## QA SANDBOX / TEST LAB
- Canonical isolated Test Lab contract backed by the real child game runtime.
- QA session state is isolated/ephemeral; Test Lab presets are browser-local only; production campaign persistence remains no-write.
- Parent exposes authenticated QA contract + launcher surface.
- No fake Admin spawn/grant/progression CRUD or production-save mutation bridge.

## OVERVIEW / ANALYTICS
- Child telemetry is stage/session runtime data only.
- No fabricated historical aggregation backend, cross-process live feed, remote player analytics store, or Admin write/publish capability.
- Both root Overview and Analytics route through the authenticated runtime-backed read-only telemetry screen.

## EXPEDITION
- Canonical runtime: browser-owned revisioned/resumable Expedition run, ruleset `expansion-v2-v1`, 8 encounters, deterministic draft/rest boundaries, writer ownership, replay/resume safeguards.
- Parent exposes authenticated read-only ownership surface.
- Admin cannot remotely read, create, resume, settle, clear, overwrite, or publish a player's Expedition run.

## DAILY / WEEKLY
- Daily is the canonical deterministic UTC-day Expedition challenge using runtime day-key/seed/identity logic.
- Personal Best and Personal Ghost are browser-local under `spaceTypingExpansionV2ProfileV1`.
- Weekly is explicitly unavailable because runtime has no canonical weekly challenge identity, seed/reset scheduler, reward track, or remote scheduler backend.
- No weekly scheduler, reward authoring, remote leaderboard, seed override, Save Draft, or Publish flow was fabricated.

## MUSIC LIBRARY — CLOSED CHECKPOINT
- Parent `MusicAssetService` is the canonical authored-asset mutation boundary for Local Admin uploads.
- Uploads are constrained to `games/space-typing/public/assets/audio/music`, validated for track/world IDs, supported audio extension/content type, duration and size (96 MiB max).
- Uploaded tracks receive provenance `local-admin-upload`; only that provenance is deletable from Admin.
- Successful upload/delete rebuilds canonical child `src/audio/world-music-catalog.json` using `pnpm music:catalog`.
- Child catalog builder walks authored manifests safely, rejects duplicate IDs/path or symlink escape, and computes deterministic SHA-256 `manifestRevision`.
- Production runtime ownership is proven: `world-music-runtime.ts` imports `world-music-catalog.json` as `BUNDLED_WORLD_MUSIC_CATALOG`; `MusicController` materializes runtime tracks from that catalog.
- Production `/admin/space-typing/music-library` reaches the Phase B runtime catalog surface; the legacy mock dialog has been removed.

## EXACT-CHILD-SHA GUARDS
- Every child pin advance was re-audited rather than bypassed.
- Shop, Currencies, Visuals, QA, Telemetry, Expedition and capability/test SHA expectations were refreshed only after confirming newer child commits did not change canonical ownership.
- Validator/test semantics were not weakened to make CI pass.

## PHASE B COMPLETION CHECK
Current `admin/space-typing-phase-b-map.v1.json` contains no `backend-foundation`, `mapped-awaiting-*`, or `ui-prototype-not-runtime-connected` status.

Intentional constrained states are closed, not unfinished:
- Daily / Weekly is `phase-b-ui-wired-runtime-partial-readonly` because Daily exists and Weekly does not.
- Alternative Modes is `phase-b-ui-wired-runtime-absence-diagnostic` because the audited runtime is absent and Admin must not fabricate it.

## CURRENT BLOCKER
NONE.

## NEXT EXACT ACTION
1. Fetch latest parent and child HEADs before any further edit; never reset to the SHA in this document if GitHub is newer.
2. Treat `f158945f20257fec8add85a71aba0e01f2c95b83` as the latest fully validated implementation checkpoint unless newer Git state supersedes it.
3. PR #49 can remain DRAFT for human acceptance; do not mark Ready or merge without explicit user instruction.
4. If continuing engineering work, only address concrete review/regression findings. Do not recreate removed legacy mock modules or invent new Phase B adapters now that all mapped screens are closed.
5. Any new product capability beyond current runtime contracts is a new scope/milestone and must first identify a real child owner/apply boundary.

## STATUS
`PHASE_B_COMPLETE_CANONICAL_CLEANUP_GREEN` — final regression triage and legacy cleanup are green. Admin CI #596 and Platform CI #1575 pass on `f158945f20257fec8add85a71aba0e01f2c95b83`; child CI #1759 passes on pinned child `8128a2a5a7713fff80cd1286b607de6a3e7190f7`.
