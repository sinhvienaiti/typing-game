# Space Typing Admin UI/UX Progress

## PROJECT STATE

STATUS: IN_PROGRESS

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- HEAD before this checkpoint: `1f5d49206df88d0c1ab126389d9f47514c50db38`

Child:
- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/admin-world-music-stage-policy`
- HEAD: `80f8e984b005e961746b1617347570b7741d8513`
- Parent child reference: still the previous B06.4 child revision; do not advance it until the B06.5 child slice is runtime-wired and validated.

Current milestone:
- **B06.5 — Bosses Admin → Runtime**

## COMPLETED MILESTONES

- **B06.1 — Ships Admin → Runtime** — DONE
- **B06.2 — Equipment Admin → Runtime** — DONE
- **B06.3 — Skills Admin → Runtime** — DONE
- **B06.4 — Enemies Admin → Runtime** — DONE

## COMPLETED TASKS OF CURRENT MILESTONE

- Audited canonical Boss identity/runtime model and real consumer path.
- Confirmed 26 canonical Boss IDs: 10 Galaxy Tyrants, 8 Wardens, 8 Lieutenants.
- Locked first safe authorable slice to `name` + `title`; HP/shield/armor/damage/speed/phase/reward fields remain unsupported until they have explicit canonical runtime consumers.
- Added child `src/admin/boss-runtime-policy.ts` with:
  - published runtime endpoint `/api/runtime/space-typing/bosses`
  - `new-session` apply boundary
  - strict canonical Boss ID allowlist
  - strict `name` / `title` field allowlist
  - normalization and deterministic bundled fallback
  - unknown-ID filtering and malformed-policy fallback
- Added `scripts/admin/boss-registry-preview.ts` and `pnpm bosses:admin-preview`.
- Added child unit coverage in `tests/boss-runtime-policy.test.ts` for valid overrides, unknown IDs, unsupported fields, malformed apply boundary, and fetch failure fallback.
- Child changes are committed/pushed through `80f8e984b005e961746b1617347570b7741d8513`.

## REMAINING TASKS

- Wire published Boss `name` / `title` overrides into the canonical identity/runtime consumer used by `bossIdentityForStage()` / `bossFullName()` / boss HUD state.
- Add Boss section/capabilities/route/apply-boundary metadata to child Admin contract.
- Add/extend child contract and identity integration tests.
- Run child targeted Boss tests, full tests, typecheck/build and child CI; fix any failures.
- Mirror Boss contract in parent.
- Add parent Boss validation, preview bridge, runtime envelope and `/api/admin/space-typing/bosses/preview` + `/api/runtime/space-typing/bosses` endpoints.
- Replace mock Boss Admin screen with revision-backed editor; unsupported master-plan fields must remain read-only with explicit explanation.
- Verify Draft -> Validate -> Publish -> runtime sees Boss identity change -> Rollback -> runtime returns prior identity.
- Update Phase B mapping and Admin CI gates.
- Only after child validation passes, update parent child reference to exact final B06.5 child SHA.
- Run parent Admin CI, Platform CI and runtime smoke.
- Then continue to the next mandatory milestone from the current master plan.

## CURRENT BLOCKER

- NONE

## NEXT ACTION

- Continue B06.5 directly by wiring `ACTIVE_BOSS_RUNTIME_SESSION` into the canonical Boss identity/name path, then update the child contract and tests. Do not repeat the completed audit or recreate the runtime loader/preview/test files.

## QUALITY GATES

- Unit: PARTIAL — Boss runtime policy tests added, execution not yet verified in this run.
- Integration: PENDING — identity consumer wiring not complete.
- Admin validation: PENDING for Boss.
- Runtime validation: PARTIAL — loader implemented; real identity consumer wiring pending.
- Contract tests: PENDING for Boss.
- Build: PENDING after B06.5 child wiring.
- Lint/typecheck: PENDING after B06.5 child wiring.
- Child CI: PENDING for child HEAD `80f8e984b005e961746b1617347570b7741d8513`.
- Parent Admin CI: previous B06.4 gate PASS; B06.5 pending.
- Platform CI: previous B06.4 gate PASS; B06.5 pending.
- Runtime smoke: PENDING for Boss.
