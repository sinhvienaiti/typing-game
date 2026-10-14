# Space Typing Admin Asset Tuning — Progress / Handoff

Last updated: 2026-10-14

## Current status

- **A5.0 — Runtime Capability Matrix + Production Preview Harness: COMPLETE**
- **A5.1 — Shared Asset Tuning Studio shell: COMPLETE**
- **A5.2 — Ship 2D Authoring / exact Media V2 image assignment: COMPLETE (automated implementation)**
- **A5.3 — Projectile / Effect Binding Migration: COMPLETE for the production-backed capability slice; non-canonical effect domains remain deliberately closed**
- **First unfinished unit: A5.4 — Current 3D bundle authoring / exact-version relief-bundle audit and migration**

Manual acceptance remains intentionally non-blocking and is tracked in `docs/SPACE_TYPING_ADMIN_ASSET_TUNING_MANUAL_ACCEPTANCE.md`.

## Source of truth

### Parent Admin

- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- PR: `#49`
- Last verified A5.3 implementation baseline before this progress-document update: `b3bdb1f25b6e289d26b649db07cb60499b4207ce`

### Child runtime

- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/bgv-integration-current`
- A5.3 runtime authority: `7dd950bd59dc51255558ebf3a211d1eff8d0df3f`
- Child CI `#2012`: PASS, including unit tests, Admin smoke/audits, strict build and R01 browser QA.

The parent gitlink now pins the same child A5.3 runtime authority. Do not reset either repository to an older checkpoint from a handoff prompt.

## A5.0 — Runtime capability matrix / production preview

Child executable matrix: `src/admin/asset-tuning-capabilities.ts`.

Every candidate capability is classified as exactly one of:

- `SUPPORTED NOW`
- `REQUIRES CANONICAL MIGRATION`
- `READ-ONLY REFERENCE`
- `DEFERRED / UNSUPPORTED`

`SUPPORTED NOW` requires a complete named chain:

persisted canonical field → validator → runtime materializer/resolver → production consumer → preview consumer using the production path → defined apply boundary.

The child `/admin-preview.html` harness uses production `drawCharacterShip()` and `PlayerShotSystem`. The parent bridge uses exact origin/source/session/nonce validation and preserves Draft vs Published isolation. No Portal-only Ship/projectile renderer exists.

## A5.1 — Shared Asset Tuning Studio

The Ships page uses the shared A5 Studio shell and common field/capability primitives rather than a developer-style diagnostic form.

The Studio keeps:

- Draft / Published source switch;
- Idle / Move / Fire production scenarios;
- Basic / Advanced disclosure;
- shared scalar controls with reset semantics;
- standard Admin tooltip/help presentation;
- existing Save Draft / Revision / History / Publish lifecycle.

Capability states remain visible instead of being converted into fake writable controls.

## A5.2 — Ship exact-version 2D Media assignment

Canonical field:

`ships.<id>.imageAssetVersionId`

Implemented chain:

Ships Admin → existing Media V2 Asset Picker → exact immutable `assetVersionId` → strict parent/child validation → revision-backed Ship config → published Ship runtime policy → child exact-version Ship media resolver → production renderer / production Admin preview.

A5.2 guarantees:

- Choose image / Change image / Clear;
- image-only Media picker filtering;
- exact immutable version persistence;
- no raw filesystem path or arbitrary URL;
- no implicit `current` / `latest` resolution;
- fallback to bundled Ship art when no override exists or a runtime resource cannot be used;
- upload alone does not change gameplay;
- Draft/Published/rollback semantics remain revision-backed.

## A5.3 — Projectile / Effect Binding Migration

### Runtime ownership audit

The production normal-Ship projectile path is owned by:

- `src/characters/projectiles.ts` — per-Ship semantic projectile profile;
- `src/vfx/player-shots.ts` — production `ShotRecipe` and `PlayerShotSystem`;
- `src/vfx/player-shot-sprites.ts` — strict painted projectile sprite bundles;
- `src/audio/Sfx.ts` — production launch/impact audio implementation;
- `src/Game.ts` — production impact/audio gameplay consumption.

The runtime does **not** expose a first-class writable Weapon entity.

### Supported canonical authoring: Ship → projectile recipe

Canonical field:

`ships.<id>.projectileArchetype`

Allowed production recipe identities:

`spear`, `heavy`, `electric`, `shadow`, `star`, `barrage`, `mystic`, `guard`, `slash`, `radiant`, `cosmic`.

Implemented chain:

Ship draft field → strict enum validation → Ship runtime session → `playerProjectileProfile()` → `shotRecipeFor()` → production `PlayerShotSystem.fire()` → Fire preview using the same production system → `new-session` apply boundary.

Changing a recipe in Admin immediately changes Draft Fire preview. Saving still creates a Draft revision only; runtime changes after normal Publish and a new session.

### Impact audio is recipe-derived, not a second writable field

A5.3 found a real typed production impact identity (`PlayerImpactVariant`) already consumed by `Game.applyShotImpact()` → `Sfx.boltImpact()`.

To prevent invalid visual/sound combinations, the selected projectile recipe now derives its matching impact sound identity. For example, an `electric` recipe derives the production `storm` impact sound; a `heavy` recipe derives `heavy`.

There is intentionally **no** separate Admin `impactSfxAssetVersionId` or free-form impact-SFX field.

The Fire preview now uses production audio:

- launch: `Sfx.shot()`;
- impact: recipe-derived `Sfx.boltImpact()`.

Launch audio remains read-only because `Sfx.shot()` is a generic production cue shared by multiple gameplay flows and has no canonical per-Ship semantic binding.

### Recipe-owned projectile presentation remains read-only

Muzzle placement, trail geometry/mode, painted projectile sprites, motion and impact geometry are owned by the selected production `ShotRecipe`.

The painted art runtime is a strict multi-component bundle (`bolt`, `finisher`, `impact`, `muzzle`) with manifest/hash semantics. A single `projectileImageAssetVersionId` would be structurally incorrect, so A5.3 does not invent one.

Future exact-version projectile-art authoring requires a canonical immutable **bundle** resolver, not a single-image shortcut.

### Skill → effect binding remains migration-required

Current Skill Admin policy persists gameplay fields such as metadata, energy cost, cooldown, charges and typing condition.

Production VFX/SFX selection is still hard-wired by skill ID through `Game.ts` and `SkillFxSystem`. There is no canonical persisted `effectPreset` / exact-version effect binding with validator + production resolver + production preview chain.

Classification: **REQUIRES CANONICAL MIGRATION**.

Do not create generic VFX CRUD or a fake writable `effectPreset` merely to satisfy the Admin UI.

### Unsupported / deferred boundaries retained

- normal Ship per-Ship miss presentation: `DEFERRED / UNSUPPORTED`;
- generic VFX CRUD: `DEFERRED / UNSUPPORTED`;
- first-class Weapon Admin entity: `DEFERRED / UNSUPPORTED`;
- arbitrary GLB / animated GLB semantic clips: `DEFERRED / UNSUPPORTED` until a real production runtime exists.

## A5.3 automated evidence

### Child

Runtime authority `7dd950bd59dc51255558ebf3a211d1eff8d0df3f` passed child CI `#2012`.

Tests/audits cover:

- strict projectile recipe materialization;
- production recipe resolution;
- recipe-derived impact identity;
- scoped Admin Fire preview without mutating active Ship runtime;
- launch/impact production SFX preview;
- capability classification that keeps recipe internals and unsupported domains closed.

### Parent

A5.3 parent integration includes:

- parent Ship validator support for `projectileArchetype`;
- server validation tests;
- exact child contract snapshot sync;
- typed preview bridge forwarding;
- Shared Studio `Projectile Recipe` control;
- child source assertions in the dedicated A5 preview CI;
- no arbitrary projectile URL/path;
- explicit assertions that no independent launch/impact SFX asset field was introduced;
- parent child-gitlink pin to `7dd950bd...`;
- re-audited unrelated domain SHA guards without removing their assertions.

At the last implementation checkpoint, fresh parent A5 Preview, Admin and Platform workflows for the latest branch were running. Re-check current workflow conclusions before claiming all parent CI green in a handoff.

## Current capability summary

### Supported now

- Ship procedural visual profile;
- per-Ship exact immutable 2D image assignment;
- Ship → production projectile recipe binding;
- existing Skill gameplay policy (independent of effect/media authoring).

### Read-only / derived production reference

- aim/recoil/boost scenario state;
- current relief 3D runtime;
- projectile muzzle/trail/sprite/motion/impact geometry owned by recipe;
- recipe-derived projectile impact SFX;
- generic production projectile launch cue;
- current production VFX/SFX where no canonical writable binding exists.

### Requires canonical migration

- persistent Ship presentation offset/rotation/pivot fields;
- exact-version relief 3D bundle assignment;
- exact-version projectile painted-art bundle assignment;
- Skill Media/VFX binding.

### Deferred / unsupported

- arbitrary GLB;
- animated GLB semantic clips without a production animation runtime;
- generic VFX CRUD;
- normal Ship per-Ship miss authoring;
- fake Weapon Admin entity.

## First unfinished unit — A5.4

**A5.4 — Current 3D bundle authoring / exact-version relief bundle migration**

Start with audit, not a form:

1. fetch latest parent + child HEAD and CI;
2. inspect `src/duel/relief-model.ts`, `src/duel/ship3d.ts` and all relevant bundle manifests/loaders;
3. inspect Media V2 kinds/component-role semantics and whether an immutable asset version can represent the complete relief bundle;
4. prove disposal/cache lifecycle for repeated Admin preview mount/switch/unmount;
5. identify persisted canonical assignment field, validator, exact-version bundle resolver, production consumer, production-backed preview consumer and apply boundary;
6. only then expose a compatible bundle picker in the Shared Asset Tuning Studio.

If exact-version bundle resolution or lifecycle ownership is incomplete, implement the canonical migration first. Do not fall back to raw GLB/path/URL authoring and do not build a Portal-only 3D renderer.
