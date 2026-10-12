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
- A3.1 validated checkpoint: `98bfa8712286c6b2c7e4ebbcbcbc8c05374a783f`

Child:
- Repo: `sinhvienaiti/space-typing`
- Admin integration branch: `feat/admin-world-music-stage-policy`
- Integration branch HEAD: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
- Parent-pinned child SHA used by A2/A3 validation: `83f80b3d6f640ea1af46e158e25485bc57b31393`
- Parent-pinned child CI #1957: PASS.

The child integration branch trails the child commit pinned by the parent. Workers must treat the parent gitlink/pinned child SHA as source of truth and must not reset the parent submodule back to the older integration-branch HEAD.

Checkpoint SHAs are informational only. Every worker must fetch latest heads before editing and must never reset newer work back to these values.

## CURRENT PHASE

`A4.0 — Shop Architecture Decision`

A0, A0.5, A1, A2, A3.0 and A3.1 are complete. A4.0 is the first unfinished phase.

## COMPLETED UNITS

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

A3.0 validated checkpoint:
- Parent HEAD: `d707354b48432987c8794e2df304b55ea0214172`
- Space Typing Admin CI #1034: PASS.
- Platform CI #2249: PASS.
- Parent-pinned child: `83f80b3d6f640ea1af46e158e25485bc57b31393`.

### A3.1 — Media Library + Asset Picker

Backend / API:
- canonical `MediaAssetStore` initialized under the existing Admin data root;
- runtime Music/ship3D/SFX reference bootstrap runs idempotently on Admin service startup;
- authenticated Media V2 read APIs expose logical assets, versions, references and exact-version components;
- Admin-owned upload/new-version/archive mutations use A0.5 permission + audit enforcement;
- normal Media API/UI does not expose hard-delete;
- Media HTTP mutations are serialized so concurrent read-modify-write operations cannot lose registry admissions;
- exact Admin-owned blobs are served only through authenticated version/component endpoints;
- generated/code-owned/external-reference assets remain reference-only ownership and reject Replace/Archive with `read-only-owner` instead of creating a shadow Admin version;
- Media mutations declare `changesGameplay: false`: upload/version/archive alone never change a Ship/Shop/World/runtime revision.

Portal / administrator workflow:
- typed `MediaAdminApi` client;
- authenticated Admin-blob preview fetch uses Object URLs; runtime-reference media keeps canonical runtime URLs;
- primary `/admin/space-typing/media` Media Library route plus command-palette entry;
- administrator-first search/type/archive filters and entity table;
- upload panel with explicit no-gameplay-mutation copy;
- ownership-aware details, preview, usage graph and immutable version history;
- technical IDs/source paths are progressive disclosure rather than primary UI;
- Replace/Archive controls appear only for Admin-owned media and only when actor permissions allow them;
- reusable Asset Picker returns exact `{asset, version}` rather than raw path or moving `latest` reference;
- Asset Picker supports allowed media types, current/historical version selection, preview, keyboard focus trap, Escape/outside close and focus restoration;
- responsive Media Library/Picker styling preserves the Space Typing dark sci-fi visual language.

Automated coverage:
- `admin/media-http.test.mjs`
- `admin/media-http-server-smoke.test.mjs`
- `admin/media-http-ownership.test.mjs`
- `admin/media-assets-v2.test.mjs`
- `admin/media-bootstrap.test.mjs`
- `scripts/validate-space-admin-v2-media.mjs`
- full Portal build and Space Typing build in Admin CI;
- A3.1 manual scenarios recorded in `docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`.

A3.1 validated checkpoint:
- Parent HEAD: `98bfa8712286c6b2c7e4ebbcbcbc8c05374a783f`
- Space Typing Admin CI #1074: PASS.
- Platform CI #2269: PASS.
- Parent-pinned child: `83f80b3d6f640ea1af46e158e25485bc57b31393`.

Manual A3.1 browser QA remains explicitly deferred/non-blocking for independent architecture work. It must be executed before final Admin V2 acceptance or before a later domain depends on an unproven browser interaction.

## IN PROGRESS

### A4.0 — Shop Architecture Decision

Current audit findings against parent-pinned child `83f80b3d6f640ea1af46e158e25485bc57b31393`:

- current Shop capability is intentionally `runtime-backed-readonly`; no canonical Admin-authored Shop policy is consumed by gameplay yet;
- runtime owner is primarily `src/shops/state.ts`, with service pricing in `src/shops/service-shop.ts` and currency ownership in `src/economy/*`;
- Shop inventory is not a simple static catalog: `ShopInstance` stock is deterministically generated and persisted in `PlayerSave.shopState`;
- generation inputs include shop type, world/stage/sector, luck, progression and hidden discovery state;
- supported shop types are `normal`, `station`, `traveling`, `black-market`, `hidden`, `event`, `service`;
- stock currently includes item and equipment entries with remaining quantity and multi-currency price;
- item pools differ by shop type; equipment availability depends on tier and grade rules;
- equipment grades use shop-type/stage probability policy;
- normal Shop pricing is derived from item/equipment grade, equipment tier and shop-type modifiers, then expressed across Credits/Alloy/Star Crystal/Quantum Core;
- hidden/event/black-market/traveling availability is runtime policy, not a simple Enabled boolean;
- Shop instances refresh at the sector-instance boundary and are persisted once generated, so changing pricing/generation policy must define what happens to already-created PlayerSave instances;
- `src/shops/service-shop.ts` owns a separate family of service costs (repair, enhancement, evolution, affix/reroll, skill/attribute upgrade, etc.) and must not be accidentally collapsed into ordinary stock pricing;
- Master Plan concepts such as Original Price, Discount, Daily/Weekly Limit, Featured, Sort Order, schedules and bundles do not currently exist natively in this runtime and must not be fabricated by Admin UI.

A4.0 must therefore define a real runtime-consumed canonical policy/adapter before A4.1 exposes Shop editing. A CRUD table that writes only to parent Admin state without child runtime consumption is forbidden.

## BLOCKERS

No blocker for A4.0 architecture/audit work.

A4.1 write UI is blocked until A4.0 resolves at minimum:
- canonical Shop policy owner/schema;
- child runtime adapter/consumer seam;
- preview/simulation contract using the same runtime generator/pricing logic;
- existing persisted `PlayerSave.shopState` behavior when policy changes;
- separation between generated stock policy, stock/catalog eligibility, pricing policy, availability policy and service-shop costs;
- explicit decision on unsupported promotion/schedule/bundle concepts rather than synthetic fields.

Later architecture gates remain tracked in `SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`, especially Ships/Weapons/Projectiles A5, Live Ops scheduler A11 and absent remote player backend.

## DEFERRED MANUAL TESTS

A1/A2/A3.1 browser scenarios are recorded in:
- `docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

They remain non-blocking for independent safe architecture/foundation work. They must be completed before final acceptance and before any later phase treats an untested browser interaction as a proven dependency.

## LATEST GREEN CI

A3.1 checkpoint `98bfa8712286c6b2c7e4ebbcbcbc8c05374a783f`:
- Parent Space Typing Admin CI #1074: PASS.
- Parent Platform CI #2269: PASS.
- Parent-pinned child CI #1957: PASS on `83f80b3d6f640ea1af46e158e25485bc57b31393`.

## NEXT EXACT ACTION

1. Re-fetch parent HEAD before every A4.0 write.
2. Finish Shop runtime-owner audit: item registry, equipment registry, presentation metadata/assets, pricing/availability/purchase paths and service-shop cost families.
3. Write `docs/SPACE_TYPING_ADMIN_V2_SHOP_ARCHITECTURE.md` before implementing Shop write UI.
4. Define a canonical Shop policy that models real runtime policy rather than generated player-instance state.
5. Define migration/compatibility behavior for existing `PlayerSave.shopState` instances when a policy revision changes.
6. Define runtime preview/simulation API that calls the same generator/pricing logic as gameplay, with explicit scenario inputs (shop type/stage/world/luck/progression/discovery) and no second generator.
7. Define which requested administrator fields are truly authorable in A4.1 and which remain unavailable until real Live Ops/promotion capabilities exist.
8. Only after the architecture is validated should child runtime policy consumption and parent Admin authoring be implemented.
9. Do not build a Shop CRUD screen first.

## SAFETY RULES

- Do not mark PR #49 Ready or merge without explicit user instruction.
- Do not create fake remote users, fake scheduler services or fake player management.
- Do not weaken Phase B ownership validators simply to make V2 pass.
- Do not create Shop/Ships shadow models disconnected from runtime.
- Do not expose generated runtime files as writable Media V2 blobs.
- Do not treat procedural VFX definitions as ordinary uploaded binary files.
- Do not let upload/replace implicitly mutate gameplay references.
- Do not create unnecessary child branches; continue from the parent-pinned child source of truth.
