# Space Typing Admin V2 — Progress

> Execution tracker for `docs/SPACE_TYPING_ADMINISTRATOR_ADMIN_V2_MASTER_PLAN.md`.
>
> This file tracks implementation state only. The Master Plan remains the product/design source of truth, `SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md` is the A0 audit source of truth, and `SPACE_TYPING_ADMIN_ASSET_TUNING_PREVIEW_PLAN.md` is the implementation source of truth for A5 presentation/preview work.

## CURRENT HEADS / SOURCE-OF-TRUTH POLICY

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- A0 audit start HEAD: `571ccdcd34362548c29bfdc0a3d55bf7861bd3c0`
- A0 migration matrix commit: `46c8da14af8f268fd01f8186c88826fff930042b`
- A0.5 validated checkpoint: `fefa731922d59542aa9fc6293fa56fc029b999aa`
- A1 validated checkpoint: `f2f088b59a9ae418b8a26045b5544b46dfb48b73`
- A2 validated checkpoint: `9d3a94231d6c3168615c1675247cb443bd6b3b51`
- A3.0 validated checkpoint: `d707354b48432987c8794e2df304b55ea0214172`
- A3.1 validated checkpoint: `98bfa8712286c6b2c7e4ebbcbcbc8c05374a783f`
- Asset Tuning / Runtime Preview initial plan checkpoint: `49470623f7fdc8cc96720a5896a124628d1698ab`
- A5 architecture hardening commit: `067d330c360a5ade2daf9eca2a18940be6df33ac`

Child:
- Repo: `sinhvienaiti/space-typing`
- Current runtime/integration branch used by the A5 review: `feat/bgv-integration-current`
- Reviewed runtime checkpoint: `dbd7348daf23a7e8ef3d804c23205e22f82407f1`
- Historical Admin integration branch: `feat/admin-world-music-stage-policy`

### Child branch reconciliation rule

The historical `feat/admin-world-music-stage-policy` branch and current `feat/bgv-integration-current` branch have diverged. Workers must **not** reset the current runtime branch to the historical Admin branch and must **not** merge/revert either branch automatically just because an older document names it.

Before any A5 implementation that depends on child runtime:

1. fetch latest child HEAD;
2. use the latest approved integration/runtime source as source of truth;
3. compare any required historical Admin/runtime work against the current branch;
4. classify differences as already superseded / still required / obsolete;
5. preserve all newer work.

Checkpoint SHAs are informational only. Every worker must fetch latest heads before editing and must never reset newer work back to these values.

---

## CURRENT PHASE TRACKING

Historical execution tracker before the A5 architecture review still recorded:

`A4.0 — Shop Architecture Decision`

Do not infer from this historical label that A5 UI may start immediately. The current A5 plan adds a mandatory architecture gate:

```text
A5.0 runtime authority + production preview gate
→ only then A5.1 Studio UI
```

Workers continuing Shop work should follow the latest Shop architecture/progress state at current HEAD. Workers beginning A5 must follow the A5 lock below even if older progress text appears to imply Ships/Weapons/Projectiles are already ready for UI authoring.

---

## COMPLETED FOUNDATION UNITS

### Master Plan review / hardening
- Administrator-first requirements locked.
- A0.5 architecture gate inserted before writable V2 domains.
- Roles/Permissions core moved earlier than full A13 management UI.
- Audit foundation moved earlier than full A14 Audit UI.
- Developer Tools scaffold moved to A2; A15 is cleanup/final migration.
- Media split into A3.0 architecture + A3.1 Media Library/Asset Picker.
- Shop split into A4.0 architecture + A4.1 workflow.
- Validator migration made explicit.

### A0 — Current-state audit and migration inventory
- audited mapped Admin routes and ownership boundaries;
- classified KEEP / REUSE / MOVE / REMOVE / BUILD NEW / SPLIT;
- inventoried Admin APIs/runtime preview boundaries;
- recorded whole-config publish-scope risk;
- locked local authenticated authoring deployment assumption;
- created Capability Gap Register and Validator Migration Map;
- locked Developer Tools destinations.

Deliverable: `docs/SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`

### A0.5 — Cross-cutting Architecture Gates
- local actor identity/request context;
- server-side permissions for draft/publish/rollback/media/audit/Developer Tools;
- JSONL audit sink with durable pre-mutation attempt and safe post-mutation degradation;
- whole-config change-scope/publish warning;
- actor/audit/change-scope endpoints;
- revision permission/audit wiring;
- actor-based revision author attribution;
- tests and CI validation.

### A1 — Admin V2 design-system foundation
- reusable tooltip/info/help drawer/field help system;
- collision handling, hover/focus/tap, Escape/outside close, route teardown;
- Page Header, validation, empty/error/loading, search/filter, chips, table/card grid;
- draft lifecycle bar and confirm/destructive dialog;
- concise sidebar with tooltip-first contextual help;
- A1 validator/manual acceptance coverage.

### A2 — Administrator shell, Dashboard V2 and Developer Tools
- real-data-only Dashboard V2;
- capability-aware primary navigation;
- read-only diagnostics removed from administrator sidebar but retained as canonical direct routes;
- permission-gated Developer Tools hub/manifest;
- permission-aware command palette;
- shell/main validator migration without weakening Phase B ownership checks;
- UI Assets/QA validators migrated to Developer Tools placement.

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
- multi-component bundle support;
- explicit provenance/storage classes;
- explicit usage reference graph;
- replacement creates new immutable version and never overwrites old bytes;
- archive is normal removal;
- hard delete is fail-closed for referenced/current/generated/code-owned versions;
- rollback retains exact referenced media versions;
- generated/code-owned bootstrap is metadata/reference-only and idempotent;
- procedural VFX definitions remain outside generic Media CRUD.

Canonical service:
- `admin/media-assets-v2.mjs`
- Admin metadata/blob store under Admin data root;
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
- generated Ship 3D bundles indexed as multi-component reference assets;
- incomplete bundles skipped rather than fabricated;
- static SFX tree indexed as code-owned reference-only assets;
- importer never copies/moves/deletes/overwrites runtime binaries;
- bootstrap admissions serialized to avoid read-modify-write lost updates.

### A3.1 — Media Library + Asset Picker

Backend/API:
- canonical `MediaAssetStore` initialized under Admin data root;
- authenticated Media V2 read APIs expose logical assets, versions, references and exact-version components;
- Admin-owned Media mutations use A0.5 permission/audit enforcement;
- normal Media UI does not expose hard-delete;
- generated/code-owned/external assets remain reference-only;
- Media mutations declare `changesGameplay: false`.

Portal workflow:
- typed Media API client;
- authenticated Admin-blob preview uses Object URLs;
- Media Library route/search/filter/details/version history;
- usage graph;
- ownership-aware Replace/Archive;
- reusable Asset Picker returns exact `{asset, version}`;
- current/historical version selection;
- keyboard focus trap, Escape/outside close and focus restoration;
- technical IDs/paths progressive-disclosed rather than primary UI.

A3.1 validated checkpoint:
- Parent HEAD: `98bfa8712286c6b2c7e4ebbcbcbc8c05374a783f`
- Space Typing Admin CI #1074 PASS
- Platform CI #2269 PASS

Manual A1/A2/A3.1 browser QA remains deferred/non-blocking for independent architecture work but must be completed before final acceptance or before a later phase depends on an unproven interaction.

---

## SHOP ARCHITECTURE SAFETY — RETAINED

Shop must remain runtime-owned rather than becoming a disconnected CRUD product catalog.

Important locked rules remain:

- Shop inventory/instances are runtime-derived/persisted state, not a static shadow catalog;
- Item/Equipment identity stays with owning registries;
- Shop-specific authoring must model real runtime policy;
- service-shop costs remain a separate policy family from ordinary stock pricing;
- unsupported promotions/schedules/bundles must not be fabricated;
- existing persisted `PlayerSave.shopState` behavior must be explicitly defined when policy revisions change;
- Shop preview/simulation must reuse canonical runtime generation/pricing logic;
- media upload alone must not mutate gameplay Shop state.

Architecture source of truth:
- `docs/SPACE_TYPING_ADMIN_V2_SHOP_ARCHITECTURE.md`

---

## A5 ARCHITECTURE REVIEW LOCK — MANDATORY

Architecture source of truth:
- `docs/SPACE_TYPING_ADMIN_ASSET_TUNING_PREVIEW_PLAN.md`

Review verdict: **GO WITH CHANGES**.

### A5.1 is blocked until A5.0 exits

Do not build the Asset Tuning Studio form first.

A5.0 must first prove:

1. every writable field has a persisted domain owner;
2. validator/materializer/resolver/production consumer are explicit;
3. current Ship visual policy actually reaches the production renderer, or the authority gap is repaired;
4. per-entity exact Media versions are resolved through a canonical production resolver before Asset Picker assignment becomes gameplay-writable;
5. existing Ship 3D is treated as the current strict generated relief-bundle representation, not arbitrary GLB;
6. arbitrary GLB / animated GLB / semantic clip mapping remain deferred until production supports them;
7. current procedural VFX remains read-only until a canonical writable effect contract exists;
8. Ship motion values such as aim/recoil/roll/pitch/yaw remain preview scenario state unless a real persisted consumer is introduced;
9. the Child Admin Visual Preview Harness uses production renderer/presentation modules rather than Portal copies;
10. preview does not mutate active revision, PlayerSave, persisted ShopInstance, published definitions or Media current-version pointers;
11. resource lifecycle cleanup is proven for RAF/audio/Object URLs/WebGL/geometry/material/texture/fetch/listeners;
12. branch/source-of-truth reconciliation is documented.

### Baseline capability classification from reviewed child checkpoint

- Ship metadata: `SUPPORTED NOW`.
- Ship procedural visual authoring: `REQUIRES CANONICAL MIGRATION` until production consumption is proven.
- Per-Ship 2D image assignment: `REQUIRES CANONICAL MIGRATION`.
- persisted scale/offset/rotation/pivot: `REQUIRES CANONICAL MIGRATION`.
- idle/aim/recoil and 3D roll/pitch/yaw: `READ-ONLY REFERENCE` / preview scenario state.
- Engine/Muzzle/Trail/Impact/Low-HP/Death VFX: `READ-ONLY REFERENCE` until effect ownership migrates.
- current projectile recipes: code-owned; authoring requires canonical migration.
- existing generated relief 3D bundle: `READ-ONLY REFERENCE` first; writable exact-version assignment requires migration.
- arbitrary GLB / animated GLB / animation clips: `DEFERRED / UNSUPPORTED`.
- generic writable VFX: `DEFERRED / UNSUPPORTED` under current contract.
- first-class Weapon Admin entity: conditional; do not invent one if runtime ownership does not justify it.

### A5.0 exact execution order

1. Re-fetch parent/child heads and audit authority chain.
2. Repair/prove current Ship visual runtime consumption.
3. Lock minimal Ship presentation schema only for real consumers.
4. Decide shared sprite-sheet vs per-Ship exact-version 2D migration.
5. Lock strict current relief 3D profile.
6. Decide derived-Media lineage; prefer validation-only until explicit provenance exists.
7. Build Child Admin Visual Preview Harness from production modules.
8. Add isolated domain candidate adapter for unsaved preview.
9. Harden postMessage/security/lifecycle/stale cancellation.
10. Add Draft vs Published sourcing through the same harness.
11. Only then start A5.1 Studio UI.

### A5 tests that must not be skipped

- production consumer parity for every writable field;
- exact `assetVersionId` pin test (`A` stays active after Media `B` becomes current);
- upload-is-not-gameplay test;
- preview mutation-isolation test;
- production/harness authority parity test;
- strict 3D profile rejection tests;
- postMessage origin/source/protocol/stale request tests if iframe is used;
- repeated preview mount/switch/unmount resource cleanup test;
- CAS conflict test;
- VFX unknown/non-authorable fields continue failing closed.

---

## DEFERRED MANUAL TESTS

Existing Admin V2 browser scenarios are recorded in:
- `docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

For A5 additionally require:

- common laptop/desktop anti-clutter review;
- keyboard-only core editing flow;
- slider numeric alternative/no drag-only verification;
- normal Admin has no raw paths/child SHA/protocol/manifests;
- production gameplay vs preview comparison for hull/motion/muzzle/projectile/trail/impact identity;
- repeated 3D preview switching/hide/show/navigation stress test.

---

## SAFETY RULES

- Do not mark PR #49 Ready or merge without explicit user instruction.
- Fetch latest parent and child source of truth before every new implementation unit.
- Do not reset/revert/overwrite newer worker/runtime work.
- Do not merge divergent child branches automatically merely to make documentation line up.
- Do not create fake remote users, fake scheduler services or fake player management.
- Do not weaken validators merely to make Admin V2 pass.
- Do not create Shop/Ships/Weapon shadow models disconnected from runtime.
- Do not expose generated runtime files as writable Media blobs without an explicit ownership migration.
- Do not treat procedural VFX definitions as ordinary uploaded binary files.
- Do not let upload/replace implicitly mutate gameplay references.
- Do not treat a renderer function parameter as an authorable setting without a persisted domain field + production consumer.
- Do not copy renderer/VFX logic into Portal.
- Do not treat current registry/data preview helpers as the production visual Preview Harness.
- Do not claim arbitrary GLB/animation support while production still uses the generated relief-bundle path.
- Do not start A5.1 until the A5.0 exit gate in the Asset Tuning plan is satisfied.
