# Space Typing Admin UI/UX Progress

## PROJECT STATE
STATUS: IN_PROGRESS

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- Validated implementation HEAD before this metadata checkpoint: `844c1ae0e40868b4b81b1e568875c1daab1a8df3`
- PR: #49 — OPEN, DRAFT
- Space Typing Admin CI #507: PASS on `844c1ae0e40868b4b81b1e568875c1daab1a8df3`.
- Platform CI #1465: PASS on `844c1ae0e40868b4b81b1e568875c1daab1a8df3`.

Child:
- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/admin-world-music-stage-policy`
- Validated HEAD: `712cc80c401ababc00ed0b77b5f24952befc0e82`
- Child CI #1755: PASS.
- Parent `games/space-typing` is pinned to exactly that tested child SHA.

## COMPLETED MILESTONES
The following slices are confirmed present by current Git state and the full Admin/Platform validation chain; do not redo them unless a later commit regresses them:
- B06.1 Ships — DONE
- B06.2 Equipment — DONE
- B06.3 Skills — DONE
- B06.4 Enemies — DONE
- B06.5 Bosses — DONE
- B06.6 Worlds & Stages — DONE
- Mandatory Typing Content — DONE
- Shop / economy runtime ownership slice — DONE
- Currencies — DONE
- Rewards & Drops runtime contract slice — DONE
- Warp economy — DONE
- Missions — DONE
- Feature Gates — DONE
- Events — DONE
- Duel — DONE
- Ranked — DONE
- Alternative Modes — DONE
- Backgrounds — DONE
- VFX — DONE
- UI Assets — DONE

## BACKGROUNDS — CLOSED CHECKPOINT
- Child owns the runtime-backed Backgrounds contract, runtime loader integration, contract test, and audit.
- The audit follows the real call chain `stage.ts -> fetchKit() -> parseKit()` rather than adding fake production imports/calls.
- The parent integration gap discovered during VFX work is closed: `/admin/space-typing/backgrounds` routes to the Phase B runtime-backed screen and `/api/admin/space-typing/backgrounds/contract` is exposed through the authenticated Admin service.
- Backgrounds remains runtime-backed/read-only because no truthful Admin write/apply boundary exists.

## VFX — CLOSED CHECKPOINT
- Child commit `c444b5f1d2bf873a1e6ad368746c095f11cf3c24` added the runtime-backed VFX contract; `3435ca12b447ee11c28d3cbe8f8d63d885d8cbf9` fixed the canonical quality mapping audit.
- Canonical VFX ownership is `Game.ts` plus production VFX systems (`CombatFxSystem`, `SkillFxSystem`, player/enemy projectile systems and related screen feedback) with visual-quality budgets owned by `src/performance/quality.ts`.
- There is no standalone runtime-consumed VFX authoring manifest, persistence seam, or safe apply boundary. Admin is intentionally `runtime-derived-readonly`; no fake profile CRUD, sliders, Save Draft, Publish, or write endpoint was added.
- Parent exposes authenticated `/api/admin/space-typing/vfx/contract`, routes `/admin/space-typing/vfx` to the runtime-backed Phase B screen, and validates the exact child SHA plus the no-write boundary.

## UI ASSETS — CLOSED CHECKPOINT
- Child commit `a4830c93ebd9d9781fde1eb7cb41bd0d2ea96ebe` introduced the UI Assets ownership contract/audit/test/CI wiring; `712cc80c401ababc00ed0b77b5f24952befc0e82` stabilized the audit against runtime identifiers instead of brittle HTML/CSS formatting.
- Child CI #1755 is green on `712cc80c401ababc00ed0b77b5f24952befc0e82`.
- The audit found no standalone Admin-authorable UI asset repository, loader/apply seam, or safe mutation boundary. Production UI ownership is code/DOM/CSS/runtime-backed, including shared UI components/HUD, Duel battle UI, and Ranked reuse.
- The canonical contract is therefore `runtime-derived-readonly` with `ui-assets.read`, `writeCapability=false`, `previewWriteCapability=false`, `authorableFields=[]`, and `applyBoundary=none`.
- Parent pins the exact green child SHA and exposes authenticated `GET /api/admin/space-typing/ui-assets/contract` plus `/admin/space-typing/ui-assets`.
- Parent CI now runs `validate-space-admin-ui-assets.mjs`, syntax-checks it, and runs child `ui-assets:audit`; the Phase B map is closed as `phase-b-ui-wired-runtime-backed-readonly` with `code-owned-runtime-ui` persistence ownership.
- Advancing the child pin only changed UI Assets contract/audit/test/CI/package files. Existing Backgrounds/VFX and Shop/Currencies exact-child-SHA guards were re-audited against the diff and refreshed without weakening their assertions.
- Parent Admin CI #507 and Platform CI #1465 are green on `844c1ae0e40868b4b81b1e568875c1daab1a8df3`.

## CURRENT MILESTONE
**QA Sandbox / Test Lab capability** — isolated QA capability after closing the B10 Visuals chain.

## QA / TEST LAB STARTING RULES
The current Phase B map calls `/admin/space-typing/qa` an `ephemeral-sandbox` with a `new-qa-run` boundary. That is a planning assumption only; it is not proof that the child runtime exposes a safe sandbox mutation seam.

Before implementation:
- trace real production diagnostics, preview/test-lab controllers, debug hooks, performance diagnostics, and scenario/fixture entry points;
- separate production runtime capability from test-only helpers and unit-test fixtures;
- identify whether any real isolated QA session can be created without mutating campaign/player production state;
- determine whether preview actions have explicit lifecycle/reset boundaries;
- classify each requested control as executable QA action, read-only diagnostic, or unsupported;
- do not expose spawn/grant/unlock/damage/currency/state mutation unless the child already owns an isolated safe execution boundary.

If no genuine QA sandbox exists, replace the aspirational `ephemeral-sandbox` map with a truthful diagnostics/read-only or runtime-absence contract. Do not build a mock Test Lab that behaves differently from the game.

## CURRENT BLOCKER
NONE. UI Assets is closed and green. QA/Test Lab runtime ownership audit is next.

## NEXT EXACT ACTION
1. Fetch latest parent and child HEADs before every edit; preserve newer worker commits.
2. Audit child production sources for Test Lab / QA / debug / diagnostics / performance / preview / scenario seams and distinguish them from test-only code.
3. Decide whether the canonical QA capability is an isolated executable sandbox, read-only diagnostics, or an explicit unsupported/absence diagnostic.
4. Implement the smallest truthful child contract/audit/test and CI gate.
5. Require full child CI green before advancing the parent submodule pin.
6. Pin parent to the exact green child commit; wire authenticated API + Phase B QA UI + validator/map only for proven capabilities.
7. Re-audit exact-child-SHA guards after any child pin without weakening them.
8. Run full Parent Admin CI + Platform CI, update this checkpoint, then continue to Overview/Analytics telemetry adapters and remaining safe adapters.

## STATUS
`IN_PROGRESS` — Backgrounds, VFX, and UI Assets are CLOSED/DONE; QA Sandbox/Test Lab is the active milestone.
