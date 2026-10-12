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
- A1 validated implementation checkpoint: `f2f088b59a9ae418b8a26045b5544b46dfb48b73`
- A2 validated implementation checkpoint: `9d3a94231d6c3168615c1675247cb443bd6b3b51`

Child:
- Repo: `sinhvienaiti/space-typing`
- Admin integration branch: `feat/admin-world-music-stage-policy`
- Integration branch HEAD: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
- Parent-pinned child SHA used by the validated A2 CI: `83f80b3d6f640ea1af46e158e25485bc57b31393`
- Parent-pinned child CI #1957: PASS.

The child integration branch currently trails the child commit pinned by the parent. Workers must treat the parent gitlink/pinned child SHA as the source of truth for parent validation and must not reset the parent submodule back to the older integration-branch HEAD.

Checkpoint SHAs are informational only. Every worker must fetch latest heads before editing and must never reset newer work back to these values.

## CURRENT PHASE

`A3.0 — Media / Asset architecture gate`

A0, A0.5, A1 and A2 are complete. A3.0 is the first unfinished phase.

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
- local Admin actor context with explicit actor ID/display name/auth method/request ID;
- explicit permission identifiers for draft/publish/rollback/media/audit/Developer Tools;
- server-side authorization hooks for current mutation routes;
- local audit JSONL sink with actor/action/domain/entity/change-scope/result metadata;
- durable pre-mutation audit attempt + safe post-mutation audit degradation behavior;
- generated revision ID resolution in successful audit events;
- whole-config revision change-scope calculation + complete-revision publish warning;
- authenticated actor/audit/change-scope API endpoints;
- Music upload/delete and revision create/publish/rollback permission + audit wiring;
- revision author attribution from actor context;
- focused tests and CI validation.

### A1 — Admin V2 design-system foundation

Implemented and validated:

- reusable imperative-DOM `AdminTooltip`;
- real-button `AdminInfoIcon`;
- `AdminHelpDrawer` with focus trap/restore;
- `AdminFieldShell` help/state wrapper;
- collision-aware tooltip placement;
- hover/focus/click/tap help behavior;
- Escape/outside-click dismissal;
- `AbortController` listener cleanup;
- route/portal teardown via `AdminHelpScope` + `MutationObserver`;
- Space Typing dark sci-fi tooltip/drawer/field styling;
- reusable Page Header;
- Validation Message;
- Empty/Error/Loading/Skeleton states;
- Search + Filter bar;
- Status chips;
- Entity Table;
- Card Grid;
- Draft lifecycle bar with `Review Changes` before Publish;
- Confirmation/Destructive dialog with async failure handling, focus trap and duplicate-submit guard;
- sidebar migrated away from permanent item/group short descriptions;
- browser-native `title` removed as the primary help mechanism;
- topbar technical Phase B milestone replaced by administrator-facing local Admin status + contextual info;
- A1 design-system validator and migrated main UI contract validator;
- task-based manual acceptance checklist created.

A1 deliberately does **not** claim every Phase B domain page is already Administrator V2. Technical page copy/contract inspectors remain scheduled for their A2+/domain-specific migration destination instead of being cosmetically relabeled.

### A2 — Administrator shell, Dashboard V2 and Developer Tools

Implemented and validated:

- real-data-only Dashboard V2 at `/admin/space-typing`;
- Dashboard sources only canonical Admin state, revision history, actor, audit activity and Music catalog summary;
- Dashboard live generation, publishable/stale draft counts, music count, signed-in actor, maintenance warning, recent activity and quick actions;
- loading, empty and error states with retry;
- capability-aware primary navigation focused on current administrator workflows;
- read-only/runtime diagnostic routes removed from the primary administrator sidebar without deleting their canonical direct routes;
- permission-gated Developer Tools hub using `developer.runtime-inspect`;
- server-owned Developer Tools manifest grouped into Runtime/Telemetry, Economy Diagnostics, Live Ops Diagnostics, PvP Diagnostics, Visual Diagnostics and QA/Test Lab;
- permission-aware command palette split between administrator commands and Developer Tools commands;
- legacy technical route breadcrumb/direct-route metadata retained during migration;
- A2 shell validator added;
- main Admin UI validator migrated from the old exact-30-primary-navigation assumption to behavior-based A2 checks while retaining all 30 canonical Phase B route/ownership checks;
- UI Assets and QA validators migrated to assert Developer Tools placement rather than primary-sidebar placement without weakening their runtime/read-only/test-lab safety boundaries;
- A2 manual acceptance scenarios appended for Dashboard, permission-aware navigation, Developer Tools, command palette, direct migration routes and responsive layout.

A2 validated checkpoint:
- Parent HEAD: `9d3a94231d6c3168615c1675247cb443bd6b3b51`
- Space Typing Admin CI #1002: PASS.
- Platform CI #2233: PASS.
- Parent-pinned child `83f80b3d6f640ea1af46e158e25485bc57b31393`: child CI #1957 PASS.

Admin CI #1002 covered all A0.5/A1/A2 validators, every retained Phase B ownership validator, revision/CAS/security tests, domain validation/runtime/lifecycle tests, all canonical preview bridges, boss/world/stage HTTP publish/runtime/rollback smoke tests, Space Typing tests and audits, Space Typing build and Portal TypeScript/Vite build.

## IN PROGRESS

### A3.0 — Media / Asset architecture gate

First audit findings already locked:

1. `admin/music-assets.mjs` is the only current generic-style writable media service. It writes uploaded tracks into the child `public/assets/audio/music/...` tree, writes `track.json`, rebuilds `src/audio/world-music-catalog.json`, and only deletes tracks whose provenance is `local-admin-upload`.
2. Current Music replacement behavior is destructive/manual (`delete then upload replacement`) and therefore is not yet a versioned general Media architecture.
3. Child `art-src/README.md` explicitly defines `art-src/**` as heavy local source art that is intentionally not committed. Runtime pipelines such as `art:prepare`, `bg:prepare`, `sprites:prepare`, `ship3d:prepare`, `combat-vfx:prepare`, etc. generate committed/runtime assets into `public/assets/space-typing/` or `src/assets/`.
4. Therefore Admin Media must not silently treat generated runtime files as editable source originals, and must not overwrite generated output without retaining source/provenance/version semantics.
5. Backgrounds are currently `runtime-derived-readonly`, persisted as `code-owned-runtime-art`, and explicitly reject a parallel Admin shadow registry.
6. UI Assets are currently `runtime-derived-readonly`, persisted as `code-owned-static-and-inline-svg`, with no generic upload/replace/delete/publish capability.
7. VFX is currently `runtime-derived-readonly`, persisted as `code-owned-runtime-vfx`; much of it is procedural/config-owned rather than a simple file asset. VFX definitions must not be collapsed into generic file CRUD.
8. A3.0 must define stable logical asset identity, immutable versions, hashes, storage/provenance, reference/usage tracking, safe replacement/archive/delete, cache/versioned URLs, rollback semantics and import/bootstrap behavior before A3.1 exposes generic Media editing.

## BLOCKERS

No blocker for architecture/design implementation of A3.0.

A3.1 writable Media UI is intentionally blocked until A3.0 establishes a canonical persistence owner and safe reference/version semantics for non-Music assets.

Known later architecture gates remain tracked in `SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`, especially:
- Shop canonical authoring model (A4.0);
- Ships/Weapons/Projectiles canonical expansion (A5);
- Live Ops scheduler (A11);
- remote player/backend absence (future capability).

## DEFERRED MANUAL TESTS

A1 and A2 browser/manual scenarios are recorded in:
- `docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

They remain non-blocking for safe architecture/foundation work. Manual validation should be requested before claiming browser UX acceptance, but it must not block architecture units that can be proven through contracts/tests/CI.

## LATEST GREEN CI

A2 checkpoint `9d3a94231d6c3168615c1675247cb443bd6b3b51`:
- Parent Space Typing Admin CI #1002: PASS.
- Parent Platform CI #2233: PASS.
- Parent-pinned child CI #1957: PASS on `83f80b3d6f640ea1af46e158e25485bc57b31393`.

## NEXT EXACT ACTION

1. Re-fetch parent HEAD before every A3.0 write.
2. Finish media ownership inventory for Music, source art pipelines, runtime images, ship/model art, SFX and procedural VFX.
3. Define the canonical Media Asset model: logical asset ID, immutable version ID, SHA-256/hash, kind, MIME/format, dimensions/duration, source provenance, storage class/path, created actor/time and lifecycle status.
4. Define references/`usedBy` records and the integration boundary between Media assets and revision-backed game definitions.
5. Define replacement as new immutable asset version + explicit reference migration; never silent in-place overwrite.
6. Define archive/delete safety: referenced versions cannot be hard-deleted; archive is the normal removal path; hard delete is restricted to safe unreferenced local uploads/generated failures.
7. Define versioned/cache-safe URLs and rollback semantics so an old game revision can still resolve the asset version it referenced.
8. Define bootstrap/import of existing runtime-generated/code-owned assets as read/reference assets without duplicating binaries or pretending Admin owns their original source files.
9. Keep procedural VFX definitions separate from generic binary assets; Media may reference VFX media, but VFX authoring remains its own canonical domain capability.
10. Implement and test the A3.0 canonical Media service only after the architecture contract is documented and validator-ready.
11. Move to A3.1 Media Library/Asset Picker only when the A3.0 service is canonical and green.

## SAFETY RULES

- Do not mark PR #49 Ready or merge without explicit user instruction.
- Do not create fake remote users, fake scheduler services or fake player management.
- Do not weaken Phase B ownership validators simply to make V2 pass.
- Do not create Shop/Ships shadow models disconnected from runtime.
- Do not create a generic Media CRUD layer on top of generated runtime files without canonical source/provenance/version/reference semantics.
- Do not treat procedural VFX definitions as if they were ordinary uploaded binary files.
- Do not create unnecessary child branches; continue from the parent-pinned child source of truth and reconcile the older Admin integration branch only when a real child change requires it.
