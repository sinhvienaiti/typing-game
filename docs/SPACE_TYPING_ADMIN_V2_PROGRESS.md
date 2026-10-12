# Space Typing Admin V2 — Progress

> Execution tracker for `docs/SPACE_TYPING_ADMINISTRATOR_ADMIN_V2_MASTER_PLAN.md`.
>
> This file tracks implementation state only. The Master Plan remains the product/design source of truth and `SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md` is the A0 audit source of truth.

## CURRENT HEADS

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- A0 audit start HEAD: `571ccdcd34362548c29bfdc0a3d55bf7861bd3c0`
- A0 migration matrix commit: `46c8da14af8f268fd01f8186c88826fff930042b`
- A0.5 validated implementation checkpoint: `fefa731922d59542aa9fc6293fa56fc029b999aa`

Child:
- Repo: `sinhvienaiti/space-typing`
- Integration branch: `feat/admin-world-music-stage-policy`
- Audited HEAD: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`

Checkpoint SHAs are informational only. Every worker must fetch latest heads before editing and must never reset newer work back to these values.

## CURRENT PHASE

`A1 — Admin V2 design system foundation`

A0 and A0.5 are complete. A1 is the first unfinished phase.

## COMPLETED UNITS

### Master Plan review / hardening
- Administrator-first requirements locked.
- A0.5 architecture gate inserted before writable V2 domains.
- Roles/Permissions core moved earlier than full A13 management UI.
- Audit foundation moved earlier than full A14 Audit UI.
- Developer Tools scaffold moved to A2; A15 is cleanup/final migration.
- Media split into A3.0 architecture + A3.1 UI.
- Shop split into A4.0 architecture + A4.1 workflow.
- Validator migration made explicit.

### A0 — Current-state audit and migration inventory
- Fetched latest parent/child heads before audit.
- Reviewed Phase B completion/progress source.
- Audited all 30 mapped Admin routes.
- Recorded `/worlds-stages` unmapped routing anomaly.
- Classified each current screen into KEEP / REUSE / MOVE / REMOVE / BUILD NEW / SPLIT.
- Inventoried current Admin APIs and runtime preview boundaries.
- Recorded whole-config revision/publish scope risk.
- Locked current deployment assumption as local authenticated authoring first.
- Created Capability Gap Register.
- Created Validator Migration Map.
- Locked child integration branch policy.
- Defined Developer Tools destinations and prerequisite phases.

A0 deliverable:
- `docs/SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`

### A0.5 — Cross-cutting Architecture Gates

Implemented and validated:

- local Admin actor context with explicit actor ID/display name/auth method/request ID;
- explicit permission identifiers for draft/publish/rollback/media/audit/Developer Tools;
- server-side authorization hooks for current mutation routes;
- local audit JSONL sink with actor/action/domain/entity/change-scope/result metadata;
- durable pre-mutation audit attempt so a write cannot execute without an audit trail entry;
- safe post-mutation audit degradation behavior so a completed mutation is not falsely returned as failed solely because the final audit append degraded;
- generated revision ID resolution in successful audit events;
- whole-config revision change-scope calculation with changed domains/paths and an explicit complete-revision publish warning;
- authenticated actor/audit/change-scope API endpoints;
- Music upload/delete permission + audit wiring;
- revision create/publish/rollback permission + audit wiring;
- revision author attribution from actor context instead of implicit default;
- revision validation response includes change scope;
- focused unit tests and static wiring validator;
- Admin CI integration for the A0.5 validator/tests.

A0.5 keeps the current deployment assumption local-only and maps the existing authenticated local token to a backwards-compatible local Super Admin. It does not fabricate a remote IAM platform.

During A0.5 CI, legacy Phase B validators exposed formatting-coupled route assertions. Existing ownership semantics were preserved: current route formatting was kept compatible and the Shop validator was made whitespace-tolerant without opening any Shop write endpoint or weakening its runtime ownership boundary.

## IN PROGRESS

### A1 — Design system foundation

First safe implementation unit:

1. create reusable imperative-DOM `AdminTooltip` + `AdminInfoIcon` primitives;
2. create reusable `AdminHelpDrawer` foundation;
3. create reusable field/help wrapper foundation;
4. define explicit teardown/lifecycle behavior for document listeners, Escape/outside click, route navigation and stale tooltip nodes;
5. add Space Typing V2 visual tokens/styles without discarding the existing dark sci-fi identity;
6. add focused validator/tests for accessibility/lifecycle requirements;
7. then migrate the shell navigation away from permanent short descriptions and native `title`-only help.

Do not mass-rewrite all Phase B domain forms in the first A1 unit. Build the reusable primitives first and migrate shared shell/help behavior before domain-specific screen conversion.

## BLOCKERS

None for the A1 foundation unit.

Known future architecture gates remain tracked in `SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`, especially:
- generic Media ownership (A3.0);
- Shop canonical authoring model (A4.0);
- Ships/Weapons/Projectiles canonical expansion (A5);
- Live Ops scheduler (A11);
- remote player/backend absence (future capability).

## DEFERRED MANUAL TESTS

No manual UI test blocks A1 foundation development.

A1 will add/extend scenarios in:
- `docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

Manual acceptance must cover hover, keyboard focus, Escape, outside click, touch/click popover behavior, responsive placement and navigation teardown once the new help primitives are integrated into the shell.

## LATEST GREEN CI

A0.5 validated checkpoint `fefa731922d59542aa9fc6293fa56fc029b999aa`:
- Parent Space Typing Admin CI #920: PASS.
- Parent Platform CI #2193: PASS.
- Child integration checkpoint CI #1759: PASS on `8128a2a5a7713fff80cd1286b607de6a3e7190f7` (no child source changes were required for A0/A0.5).

Admin CI #920 covered:
- Admin V2 foundation validator;
- complete Phase B ownership validators;
- immutable revision/CAS + security/audit tests;
- all canonical preview bridges;
- boss/world/stage HTTP publish/runtime/rollback smoke tests;
- Space Typing tests and audits;
- Space Typing build;
- Portal build.

## NEXT EXACT ACTION

1. Re-fetch current parent HEAD before A1 source writes.
2. Inspect current shell/core CSS and imperative-DOM lifecycle patterns.
3. Add shared Admin V2 help primitives under a reusable `portal/src/admin/v2/` structure.
4. Add styles/tokens matching the current Space Typing admin visual identity.
5. Add A1 validator/test coverage for tooltip/accessibility/cleanup semantics.
6. Integrate the shared tooltip into shell navigation and remove permanent per-item short descriptions without losing contextual help.
7. Run Admin + Platform CI.
8. Continue the next unfinished A1 component unit after blockers are resolved.

## SAFETY RULES

- Do not mark PR #49 Ready or merge without explicit user instruction.
- Do not create fake remote users, fake scheduler services or fake player management.
- Do not weaken Phase B ownership validators simply to make V2 pass.
- Do not create Shop/Ships shadow models disconnected from runtime.
- Do not create unnecessary child branches; continue current Admin integration branch unless a real dependency requires otherwise.
