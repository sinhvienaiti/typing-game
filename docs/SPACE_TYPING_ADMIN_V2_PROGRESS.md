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
- A0.5 validated checkpoint: `fefa731922d59542aa9fc6293fa56fc029b999aa`
- A1 validated checkpoint: `f2f088b59a9ae418b8a26045b5544b46dfb48b73`
- A2 validated checkpoint: `9d3a94231d6c3168615c1675247cb443bd6b3b51`
- A3.0 validated checkpoint: `d707354b48432987c8794e2df304b55ea0214172`

Child:
- Repo: `sinhvienaiti/space-typing`
- Admin integration branch: `feat/admin-world-music-stage-policy`
- Integration branch HEAD: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
- Parent-pinned child SHA used by A2/A3.0 validation: `83f80b3d6f640ea1af46e158e25485bc57b31393`
- Parent-pinned child CI #1957: PASS.

The child integration branch trails the child commit pinned by the parent. Workers must treat the parent gitlink/pinned child SHA as source of truth and must not reset the parent submodule back to the older integration-branch HEAD.

Checkpoint SHAs are informational only. Every worker must fetch latest heads before editing and must never reset newer work back to these values.

## CURRENT PHASE

`A3.1 — Media Library + Asset Picker`

A0, A0.5, A1, A2 and A3.0 are complete. A3.1 is the first unfinished phase.

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
- audited all 30 mapped Admin routes and `/worlds-stages` routing anomaly;
- classified KEEP / REUSE / MOVE / REMOVE / BUILD NEW / SPLIT;
- inventoried Admin APIs/runtime preview boundaries;
- recorded whole-config publish-scope risk;
- locked local authenticated authoring deployment assumption;
- created Capability Gap Register and Validator Migration Map;
- locked child integration policy and Developer Tools destinations.

Deliverable: `docs/SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`

### A0.5 — Cross-cutting Architecture Gates
- local actor identity/request context;
- server-side permissions for draft/publish/rollback/media/audit/Developer Tools;
- JSONL audit sink with durable pre-mutation attempt and safe post-mutation degradation;
- whole-config change-scope/publish warning;
- actor/audit/change-scope endpoints;
- Music/revision permission + audit wiring;
- actor-based revision author attribution;
- tests and CI validation.

### A1 — Admin V2 design-system foundation
- reusable tooltip/info/help drawer/field help system;
- collision handling, hover/focus/tap, Escape/outside close, route teardown;
- Page Header, validation, empty/error/loading, search/filter, chips, table/card grid;
- draft lifecycle bar and confirm/destructive dialog;
- concise sidebar with tooltip-first contextual help;
- A1 validator and manual acceptance checklist.

### A2 — Administrator shell, Dashboard V2 and Developer Tools
- real-data-only Dashboard V2;
- capability-aware primary navigation;
- read-only diagnostics removed from administrator sidebar but retained as canonical direct routes;
- permission-gated Developer Tools hub/manifest;
- permission-aware command palette;
- A2 shell/main validator migration without weakening all 30 Phase B ownership checks;
- UI Assets/QA validators migrated to Developer Tools placement;
- A2 manual acceptance scenarios.

A2 checkpoint:
- Parent `9d3a94231d6c3168615c1675247cb443bd6b3b51`
- Admin CI #1002 PASS
- Platform CI #2233 PASS

### A3.0 — Media / Asset architecture gate

Architecture source of truth:
- `docs/SPACE_TYPING_ADMIN_V2_MEDIA_ARCHITECTURE.md`

Locked architecture:
- stable logical asset separated from immutable asset version;
- published/runtime definitions pin exact `assetVersionId`; no silent `follow latest`;
- multi-component bundle support for assets such as 3D ships;
- provenance: `admin-upload`, `generated-runtime`, `code-owned`, `external-reference`;
- storage classes: `admin-blob`, `runtime-reference`, `source-reference`, `external-reference`;
- explicit `usedBy` reference graph;
- replacement creates a new immutable version and never overwrites old bytes;
- archive is the normal removal path;
- hard delete is fail-closed for referenced/current/generated/code-owned versions;
- rollback retains exact referenced media versions;
- generated/code-owned bootstrap is metadata/reference-only and idempotent;
- procedural VFX definitions remain outside generic Media CRUD.

Canonical service:
- `admin/media-assets-v2.mjs`
- Admin metadata/blob store under Admin data root, not child source tree;
- atomic registry writes;
- content-addressed immutable Admin blobs;
- logical asset/version/reference listing and resolution;
- upload creates immutable versions;
- reference-only bundle registration;
- archive/unarchive;
- explicit reference add/remove/query;
- safe hard-delete guard;
- versioned Admin blob URL resolution.

Bootstrap adapter:
- `admin/media-bootstrap.mjs`
- Music catalog indexed as reference-only;
- legacy `local-admin-upload` Music is imported as `external-reference` rather than falsely becoming a Media V2-owned blob;
- ship3D manifest indexed as generated multi-component bundles;
- ship bundle fingerprint uses actual bytes/hash/size of `color.webp`, `emissive.webp`, `height.bin`, `model.json`;
- incomplete bundles are skipped rather than fabricated;
- static SFX tree indexed as code-owned reference-only assets with hashes;
- importer never copies/moves/deletes/overwrites runtime binaries;
- bootstrap admissions are serialized after tests exposed a real read-modify-write lost-update race.

Automated coverage:
- `admin/media-assets-v2.test.mjs`
- `admin/media-bootstrap.test.mjs`
- `scripts/validate-space-admin-v2-media.mjs`
- runtime smoke test runs against the actual parent-pinned Space Typing tree, confirms current Music + all ship3D manifest bundles + SFX can be indexed, `media-v2/blobs` stays empty, and rerun creates zero duplicate versions.

A3.0 validated checkpoint:
- Parent HEAD: `d707354b48432987c8794e2df304b55ea0214172`
- Space Typing Admin CI #1034: PASS.
- Platform CI #2249: PASS.
- Parent-pinned child: `83f80b3d6f640ea1af46e158e25485bc57b31393`.

## IN PROGRESS

### A3.1 — Media Library + Asset Picker

Implementation order is backend-first:

1. instantiate canonical `MediaAssetStore` under existing Admin data root;
2. bootstrap current runtime references idempotently at service initialization;
3. expose narrow authenticated Media V2 read APIs;
4. expose Admin-owned upload/new-version/archive mutations with A0.5 permission + audit enforcement;
5. do not expose casual hard-delete in normal Media UI;
6. serve Admin-owned blobs through exact-version component URLs;
7. add Portal Media API types/client;
8. build Media Library using A1 primitives;
9. build reusable Asset Picker that returns exact `assetVersionId`;
10. add Media manual acceptance scenarios and CI/browser-contract validators.

Important A3.1 behavior:
- uploading media alone never changes Shop/Ships/Worlds/gameplay;
- generated/code-owned runtime assets are visible/searchable/referenceable but remain read-only ownership;
- replacement creates a new version; reference migration is explicit and belongs to the consuming domain draft;
- raw paths/provenance diagnostics are progressive disclosure, not normal primary workflow.

## BLOCKERS

No blocker for A3.1 backend/API implementation.

Later architecture gates remain tracked in `SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`, especially Shop A4.0, Ships/Weapons/Projectiles A5, Live Ops scheduler A11 and absent remote player backend.

## DEFERRED MANUAL TESTS

A1/A2 browser scenarios are recorded in:
- `docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

They remain non-blocking for safe foundation work. A3.1 Media scenarios must be appended before claiming browser UX acceptance.

## LATEST GREEN CI

A3.0 checkpoint `d707354b48432987c8794e2df304b55ea0214172`:
- Parent Space Typing Admin CI #1034: PASS.
- Parent Platform CI #2249: PASS.
- Parent-pinned child CI #1957: PASS on `83f80b3d6f640ea1af46e158e25485bc57b31393`.

## NEXT EXACT ACTION

1. Re-fetch parent HEAD before every A3.1 write.
2. Add Media V2 server adapter with minimal changes to `admin/server.mjs` so old formatting-sensitive Phase B validators remain stable.
3. Initialize `MediaAssetStore` and run idempotent reference bootstrap on startup.
4. Add authenticated Media read endpoints for assets/versions/references/component resolution.
5. Add `media.upload` mutations for new asset/new immutable version through `runAuthorizedAdminMutation`.
6. Add `media.delete` mutation for archive/unarchive; keep hard-delete out of normal A3.1 UI/API unless an explicitly restricted cleanup endpoint is separately justified/tested.
7. Serve only `admin-blob` component bytes from Media V2; reference-only runtime files keep their canonical runtime URLs.
8. Add HTTP/security tests before Portal UI.
9. Then add Portal client, Media Library and Asset Picker.

## SAFETY RULES

- Do not mark PR #49 Ready or merge without explicit user instruction.
- Do not create fake remote users, fake scheduler services or fake player management.
- Do not weaken Phase B ownership validators simply to make V2 pass.
- Do not create Shop/Ships shadow models disconnected from runtime.
- Do not expose generated runtime files as writable Media V2 blobs.
- Do not treat procedural VFX definitions as ordinary uploaded binary files.
- Do not let upload/replace implicitly mutate gameplay references.
- Do not create unnecessary child branches; continue from the parent-pinned child source of truth.
