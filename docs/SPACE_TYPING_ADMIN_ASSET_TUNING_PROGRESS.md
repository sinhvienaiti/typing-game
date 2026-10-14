# Space Typing Admin Asset Tuning — Progress / Handoff

Last updated: 2026-10-14

## Current status

- **A5.0 — Runtime Capability Matrix + Production Preview Harness: COMPLETE**
- **A5.1 — Shared Asset Tuning Studio shell: COMPLETE**
- **A5.2 — Ship exact-version 2D Media assignment: COMPLETE**
- **A5.3 — Ship projectile recipe / production SFX binding slice: COMPLETE**
- **A5.4 — Ship exact-version 3D relief bundle assignment + production preview lifecycle: COMPLETE**
- **A6.0 — Skills / Equipment canonical capability audit + executable matrix: COMPLETE**
- **A6.1 — Skills / Equipment shared capability-state UI adoption: COMPLETE**
- **First unfinished unit: A6.2 — shared V2 field/help ergonomics for canonical Skills / Equipment gameplay editors**

Manual visual acceptance remains intentionally non-blocking and is tracked separately. An unavailable historical CI log is also non-blocking under `docs/SPACE_TYPING_CI_CONTINUATION_POLICY.md`; use the next safe commit as the fresh diagnostic checkpoint instead of stopping implementation.

## Source of truth

### Parent Admin

- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- PR: `#49` — OPEN / DRAFT
- Parent gitlink pins child `0d8ed88a90b370e6547e9846cfca1c46ef2a342f`.
- Dedicated A6 Skills / Equipment CI run `38522696356` passed capability validation and Portal build on the A6.1 UI checkpoint.
- Latest full Admin / Platform runs must still be re-checked before a handoff claims the entire parent branch green; do not infer their conclusion from the dedicated A6 gate.

### Child runtime

- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/bgv-integration-current`
- Current A6 runtime/capability authority: `0d8ed88a90b370e6547e9846cfca1c46ef2a342f`.
- Child CI `#2038` / run `38521566489`: PASS, including tests, Admin audits, strict build and R01 browser QA.
- Previous A5.4 strict-build-stable runtime authority: `d4632067fbe2e0ba17324a75793c62088cbd6ceb`.
- Child CI `#2036` / run `38520846232`: PASS.

Always fetch latest parent + child HEAD before editing. Never reset to a SHA recorded here when GitHub has newer work.

---

## A5 runtime-authority rules

A writable presentation control is allowed only when the chain exists:

`persisted canonical field → validator → runtime materializer/resolver → production consumer → production-backed preview consumer → apply boundary`

Capability states remain exactly one of:

- `SUPPORTED NOW`
- `REQUIRES CANONICAL MIGRATION`
- `READ-ONLY REFERENCE`
- `DEFERRED / UNSUPPORTED`

Do not create a Portal-only renderer, raw path/URL field, generic VFX CRUD, fake Weapon entity or fake Media binding merely to satisfy UI design.

---

## A5.2 — Ship exact-version 2D Media assignment

Canonical field:

`ships.<id>.imageAssetVersionId`

Implemented chain:

Ships Admin → Media V2 Asset Picker → exact immutable `assetVersionId` → strict parent/child validation → revision-backed Ship config → published Ship runtime session → exact Ship media resolver → production renderer + production Admin preview.

Locked behavior:

- Choose / Change / Clear image through Media V2;
- image-only compatibility filtering;
- no arbitrary URL/filesystem path;
- no implicit `current` / `latest` lookup;
- bundled production art remains the safe fallback;
- Draft / Published / rollback semantics remain revision-backed;
- gameplay changes only after normal Publish and the new-session apply boundary.

---

## A5.3 — Projectile / effect binding slice

Canonical writable field:

`ships.<id>.projectileArchetype`

Supported production recipe identities:

`spear`, `heavy`, `electric`, `shadow`, `star`, `barrage`, `mystic`, `guard`, `slash`, `radiant`, `cosmic`.

Runtime chain:

Ship draft → strict enum validation → Ship runtime session → `playerProjectileProfile()` → `shotRecipeFor()` → production `PlayerShotSystem.fire()` → production-backed Fire preview.

Important boundaries:

- impact SFX is recipe-derived and reaches `Sfx.boltImpact()`;
- launch uses the generic production `Sfx.shot()` cue;
- no independent impact/launch SFX asset field exists;
- muzzle/trail/painted sprite/motion/impact geometry remain recipe-owned derived presentation;
- normal per-Ship miss authoring remains unsupported;
- no first-class Weapon Admin entity is invented;
- Skill Media/VFX binding remains migration-required.

---

## A5.4 — Ship exact-version 3D relief bundle assignment

A5.4 is complete. The current production 3D path remains the strict relief-bundle runtime rather than arbitrary GLB authoring.

Canonical field:

`ships.<id>.reliefAssetVersionId`

Production ownership:

- `src/admin/ship-runtime-policy.ts` — exact persisted assignment;
- `src/duel/relief-media-runtime.ts` — strict exact-version bundle resolution;
- `src/duel/relief-model.ts` — production relief loading;
- `src/duel/ship3d.ts` — production 3D Ship consumer;
- `src/duel/ship3d-lifecycle.ts` — explicit GPU resource ownership/disposal;
- `src/admin/ship-asset-preview.ts` + `asset-preview-main.ts` — isolated production-backed Admin preview.

Bundle requirements remain strict and immutable. Required component roles are the production relief roles, with same-origin runtime URLs and immutable hash/fingerprint metadata. Arbitrary GLB, animated GLB and semantic animation clip authoring remain deferred until a real production runtime owns them.

A5.4 Admin behavior:

- separate `Ship Image` and `3D Relief Bundle` controls;
- model-only Media picker plus strict relief compatibility predicate;
- exact immutable version persistence;
- explicit `Preview 3D` surface;
- bundled-default restore path;
- Draft vs Published isolation;
- candidate-owned 3D resources disposed on switch/supersede/unmount;
- production gameplay resolves the published assignment only at the new-session boundary.

### A5.4 CI blocker closure

The historical failed Build log was initially unavailable and was correctly treated as non-blocking. A later commit reproduced the issue with readable diagnostics.

Real strict-build fixes:

- `src/duel/ship3d-lifecycle.ts`: readonly material-array vs disposable-object narrowing made TypeScript strict-build safe without changing disposal semantics;
- `tests/admin-ship-relief-media-runtime.test.ts`: negative fixtures received explicit record typing without weakening resolver validation.

Child `d4632067...` then passed the complete CI chain, including strict build and R01 browser QA.

---

## A6.0 — Skills / Equipment capability audit

A6 starts from canonical runtime ownership, not from forms.

Child executable source of truth:

`src/admin/a6-skill-equipment-capabilities.ts`

### Skills

`skill.gameplay-policy` — **SUPPORTED NOW**

Canonical writable fields:

`skills.<id>.{name,description,energyCost,cooldown,charges,perStageLimit,typingCondition}`

Owner / runtime chain:

`src/admin/skill-runtime-policy.ts` → `sanitizeOverride()` → `applySkillRuntimeOverride()` → production Skill definitions/gameplay.

`skill.media-vfx-binding` — **REQUIRES CANONICAL MIGRATION**

Current production Skill effects remain code-owned by `Game.ts` / `src/vfx/skill-fx.ts`. No `effectPreset`, VFX asset, SFX asset or generic Media binding is canonical yet.

### Equipment

`equipment.gameplay-policy` — **SUPPORTED NOW**

Canonical writable fields:

`equipment.<id>.{name,description,stats,perk}`

Owner / runtime chain:

`src/admin/equipment-runtime-policy.ts` → `materializeEquipmentRuntimeSession()` / `activeEquipmentRuntimeOverride()` → canonical equipment registry/gameplay consumers.

`equipment.registry-icon` — **READ-ONLY REFERENCE**

The current icon is a child-owned glyph string in `EquipmentDefinition.icon`; it is not a Media V2 asset version.

`equipment.media-binding` — **REQUIRES CANONICAL MIGRATION**

A future image/icon Media picker requires a persisted exact-version field and production resolver first.

`equipment.vfx-sfx-binding` — **DEFERRED / UNSUPPORTED**

No generic per-Equipment VFX/SFX authoring contract exists.

A6 tests fail closed if a `SUPPORTED NOW` capability lacks persistence, validator, runtime resolver, production consumer, preview consumer or a `new-session` boundary.

---

## A6.1 — Shared capability-state UI adoption

Skills and Equipment retain their existing canonical registry/data-preview and immutable Draft lifecycle. A6.1 does **not** relabel those previews as a production visual renderer.

The pages now reuse `createAssetTuningCapabilityState()` from the shared V2 Asset Tuning primitives.

### Skills operator-facing states

- `Gameplay Policy` — `AVAILABLE`
- `Media / VFX` — `REQUIRES CANONICAL MIGRATION`

The previous long developer-centric warning about hypothetical damage/radius/projectile/VFX/SFX fields is removed.

### Equipment operator-facing states

- `Gameplay Policy` — `AVAILABLE`
- `Registry Icon` — `READ-ONLY REFERENCE`
- `Media Binding` — `REQUIRES CANONICAL MIGRATION`
- `VFX / SFX` — `DEFERRED / UNSUPPORTED`

The previous long future-fields warning is removed.

Lifecycle remains:

canonical child preview validation → immutable Draft revision → shared History / Publish activation → new-session runtime apply.

Skills / Equipment editors do not call `api.publish()` directly.

Dedicated A6 CI protects:

- child capability matrix identities/statuses;
- canonical authorable allow-lists;
- absence of fake Media/VFX/SFX fields;
- child-preview-before-Draft lifecycle;
- History-owned activation boundary;
- shared capability-state UI adoption;
- Portal build.

---

## Re-audited exact child SHA guards

After pinning `0d8ed88...`, unrelated domain guards were advanced only after confirming the A5/A6 diff does not touch their canonical owners:

- Visuals / Backgrounds / VFX;
- Shop;
- QA / Test Lab;
- Telemetry;
- Expedition;
- Daily / Weekly.

Their assertions were retained. The SHA guards were not removed or relaxed.

---

## Current capability summary

### Supported now

- Ship procedural visual profile;
- per-Ship exact immutable 2D image assignment;
- per-Ship exact immutable 3D relief bundle assignment;
- Ship → production projectile recipe binding;
- Skill canonical gameplay policy;
- Equipment canonical gameplay policy.

### Read-only / derived reference

- aim/recoil/boost scenario state;
- projectile recipe internals and recipe-derived impact SFX;
- generic production projectile launch cue;
- Equipment registry glyph icon;
- production Skill VFX/SFX without a typed writable binding.

### Requires canonical migration

- persistent Ship presentation offset/rotation/pivot fields;
- exact-version projectile painted-art bundle assignment;
- Skill Media/VFX binding;
- Equipment Media binding.

### Deferred / unsupported

- arbitrary GLB / animated GLB semantic clips;
- generic VFX CRUD;
- normal Ship per-Ship miss authoring;
- fake Weapon Admin entity;
- generic per-Equipment VFX/SFX authoring.

---

## First unfinished unit — A6.2

**A6.2 — shared V2 field/help ergonomics for canonical Skills / Equipment gameplay editors**

Goals:

1. retain the current canonical authorable field sets exactly;
2. migrate operator-facing field guidance to shared Admin help/tooltip primitives where useful;
3. reduce permanent implementation-heavy descriptions while keeping critical apply/publish boundaries visible;
4. keep immutable fields visibly read-only;
5. retain registry/data preview semantics without calling it production visual preview;
6. preserve child-preview validation before Draft creation and History-owned Publish;
7. do not introduce any Media picker, effect preset or VFX/SFX control unless a future child migration first establishes a complete production authority chain.

Manual UI review remains non-blocking for implementation; record it separately and fix concrete visual defects when reported.
