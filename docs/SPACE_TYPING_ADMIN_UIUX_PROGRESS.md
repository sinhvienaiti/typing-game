# Space Typing Admin UI/UX Progress

## PROJECT STATE
STATUS: IN_PROGRESS

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- Validated implementation HEAD before this metadata checkpoint: `cb21a187a12169a03c0dd0b8f8003791833d696c`
- PR: #49 — OPEN, DRAFT
- Space Typing Admin CI run `37729417681` (#481): PASS on `cb21a187a12169a03c0dd0b8f8003791833d696c`.
- Platform CI run `37729417655` (#1390): PASS on `cb21a187a12169a03c0dd0b8f8003791833d696c`.

Child:
- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/admin-world-music-stage-policy`
- Validated HEAD: `ac8014537a0b56e964175e7b31f92c97fa0f5afa`
- Child CI run `37728734859` (#1751): PASS.
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

## BACKGROUNDS — CLOSED CHECKPOINT
- Child owns the runtime-backed Backgrounds contract, runtime loader integration, contract test, and audit.
- The old audit false assumption was corrected by following the real call chain `stage.ts -> fetchKit() -> parseKit()` rather than adding fake production imports/calls.
- Child canonical CI is green on `ac8014537a0b56e964175e7b31f92c97fa0f5afa`; `pnpm build` passes together with all contract audits.
- Parent pins exactly that child SHA.
- Parent Backgrounds mapping/runtime validation, capability tests, Space Typing tests/build, Portal tests/build, Admin CI and Platform CI all pass on `cb21a187a12169a03c0dd0b8f8003791833d696c`.
- Re-audited Shop/Currencies SHA guards after the child pin because the child commit changed while those runtime domains did not. Validation was not weakened.

## QUALITY GATES AT BACKGROUNDS CLOSE
Child:
- Test: PASS.
- Warp economy audit: PASS.
- Missions audit: PASS.
- Feature Gates audit: PASS.
- Events audit: PASS.
- Duel audit: PASS.
- Ranked audit: PASS.
- Alternative Modes audit: PASS.
- Backgrounds audit: PASS.
- Canonical `pnpm build`: PASS.
- CI: `37728734859` (#1751) — PASS.

Parent:
- Admin contract/integration validations: PASS.
- B06.x capability tests: PASS.
- Shop/Currencies/Rewards/Warp/Missions/Feature Gates/Events/Duel/Ranked/Alternative Modes/Backgrounds capability tests: PASS.
- Backgrounds mapping/runtime validator: PASS.
- Space Typing tests/build: PASS.
- Portal tests/build: PASS.
- Space Typing Admin CI: `37729417681` (#481) — PASS.
- Platform CI: `37729417655` (#1390) — PASS.

## CURRENT MILESTONE
**VFX** — runtime ownership/consumer audit and smallest truthful end-to-end Admin slice.

## VFX AUDIT — CONFIRMED STARTING EVIDENCE
Current child runtime already has real VFX consumers and must remain the source of truth. Confirmed examples include:
- `src/vfx/combat-fx.ts` — `CombatFxSystem` for combat hit/death/layer/cast/boss effects.
- `src/vfx/enemy-fx.ts` — enemy/status/vengeance effects.
- `src/vfx/combat-vfx-sprites.ts` — combat VFX sprite runtime.
- `src/vfx/animation-player.ts` and `src/vfx/skill-fx.ts` — skill animation/effect runtime.
- `src/vfx/credit-crystal-fx.ts`, `credit-crystal-pickups.ts`, `credit-crystal-renderer.ts` — credit-crystal visual/pickup runtime.
- `src/vfx/bonus-sprites.ts` and `src/vfx/victory-celebration.ts` — bonus/victory effects.
- `src/vfx/flight-field.ts` — flight-field visual runtime.
- `src/Game.ts` imports/uses these runtime systems and also owns visual-quality resolution/budgets.

This is evidence for audit only. It is **not** permission to invent a new authoring schema. Authorable fields and publish/apply boundaries must be derived from actual ownership and consumers.

## CURRENT BLOCKER
NONE for Backgrounds. VFX schema/authorability is intentionally undecided until the runtime audit is complete.

## NEXT EXACT ACTION
1. Fetch latest parent and child HEADs again before edits.
2. Finish tracing VFX call sites and canonical owners: combat hit/death/boss/layer/cast, projectiles/explosions, skill effects, status effects, screen/bonus/victory effects, credit-crystal effects and quality-tier behavior.
3. Classify every candidate field as runtime-backed authorable, runtime-backed read-only/diagnostic, or unsupported. Do not duplicate source-owned constants/config.
4. Identify the smallest valid apply/publish boundary and persistence owner.
5. Implement the smallest end-to-end VFX slice only after that audit: Admin UI -> API -> validated canonical config -> apply/publish -> child loader/consumer -> actual gameplay behavior.
6. Add contract/audit proving the gameplay consumer really reads the canonical VFX config.
7. Run full child tests/audits/TypeScript/build. Only pin a fully green child SHA.
8. Run full parent Admin + Platform validation, then update this checkpoint and continue the next mandatory master-plan milestone without waiting for user confirmation.

## STATUS
`IN_PROGRESS` — Backgrounds is CLOSED/DONE; VFX is the active milestone.
