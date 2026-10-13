# Space Typing Admin V2 — Asset Tuning & Runtime Preview Plan

> Status: **DESIGN / IMPLEMENTATION SOURCE OF TRUTH FOR ASSET-TUNING UX**
>
> Scope: A5 Ships / Weapons / Projectiles first, then reusable adoption by A6 Skills / Equipment and other compatible domains.
>
> Parent: `sinhvienaiti/typing-game` · `feat/space-typing-admin-uiux`
>
> Child runtime source: `sinhvienaiti/space-typing` · current Admin/runtime integration line.
>
> This document refines, and does not replace:
> - `SPACE_TYPING_ADMINISTRATOR_ADMIN_V2_MASTER_PLAN.md`
> - `SPACE_TYPING_ADMIN_V2_MEDIA_ARCHITECTURE.md`
> - `SPACE_TYPING_ADMIN_V2_SHOP_ARCHITECTURE.md`
>
> Checkpoint SHAs are never implementation targets. Every worker must fetch latest parent/child HEAD before editing and preserve newer work.

---

## 1. Product decision

The target Admin experience is **not** “upload an arbitrary file and hope the game renders it correctly”.

The target is an administrator-facing **Asset Tuning Studio**:

```text
Select / Upload compatible asset
        ↓
Validate against the slot profile
        ↓
Tune only runtime-supported presentation parameters
        ↓
Preview in the real child renderer / presentation path
        ↓
Test states and effects
        ↓
Save Draft
        ↓
Validate + Review Changes
        ↓
Publish
```

The asset is only the source material. The administrator manages **how the canonical runtime uses that asset**.

Examples:

- Ship sprite: asset + scale + position + supported motion + weapon/effect bindings.
- Ship 3D presentation: model/bundle + supported transform + animation clip mapping + effect bindings.
- Skill: icon/effect references + supported presentation/timing controls.
- Projectile: visual asset/preset + supported scale/trail/impact bindings.
- Shop: product presentation only where the Shop runtime or the owning Item/Equipment domain canonically consumes those fields.

### Hard rule

> A control must not appear in normal Admin merely because it is easy to draw in the UI. It appears only when the production runtime has a canonical consumer for that value.

This is the main protection against a beautiful but fake settings screen.

---

## 2. Goals

1. Let administrators select/upload a compatible visual asset without editing source code or filesystem paths.
2. Let administrators tune its presentation with simple, game-language controls.
3. Let administrators immediately see the result in a live preview using the same child-owned rendering logic as production.
4. Let administrators preview movement, firing, skill use, VFX, hit, damage and death states when those states genuinely exist.
5. Keep the normal screen simple and visually calm while still allowing advanced tuning.
6. Keep Media ownership, immutable versions, revision/CAS safety and runtime ownership intact.
7. Make this system reusable without forcing every domain into one giant universal schema.

---

## 3. Non-goals

The first implementation does **not** attempt to become Blender, After Effects or a generic game engine editor.

Explicitly out of scope unless separately implemented by the child runtime:

- arbitrary rig creation;
- automatic skeleton repair;
- arbitrary GLB animation generation;
- arbitrary shader graph editing;
- node-based VFX authoring;
- frame-by-frame sprite animation authoring;
- Photoshop-style image editing;
- free-form JSON configuration;
- arbitrary filesystem path entry;
- making an unsupported upload type magically compatible;
- reimplementing production rendering logic inside Portal.

External tools may still create/prepare assets. Admin owns safe assignment, supported tuning, preview and publication.

---

## 4. Core UX principle — simple first, power on demand

The UI must follow:

> **Make the common task obvious; make the powerful task discoverable.**

A normal administrator should be able to complete this flow without understanding render engines, manifests, protocol versions or source paths:

```text
Choose image/model
→ adjust size and position
→ choose effect/preset
→ press Idle / Move / Fire / Skill
→ visually approve result
→ Save Draft
```

### 4.1 No parameter wall

The screen must not show 20–40 sliders at once.

Rules:

- show at most about **5–7 primary controls per visible group**;
- one task-focused section is active at a time;
- advanced settings are collapsed by default;
- conditional controls appear only when relevant;
- technical diagnostics move to Developer Tools / Advanced Details;
- long explanatory paragraphs are replaced by styled tooltips/help drawer;
- warnings remain inline only when actionable.

### 4.2 Basic and Advanced modes

Every tunable asset slot should expose a small **Basic** set first.

Typical Basic controls:

- Asset / Model / Effect selection;
- Size / Scale;
- Position;
- Rotation only when useful;
- one or two domain-specific presets;
- core effect bindings;
- preview state.

Advanced may expose, only when supported:

- anchor/pivot;
- per-axis scale;
- depth/layer;
- opacity/blend mode;
- motion amplitude/speed;
- recoil timing;
- animation clip mapping;
- effect offsets;
- effect intensity/scale;
- easing/timing parameters.

`Advanced` is not a dumping ground for raw runtime config. Unsupported/internal-only values remain Developer Tools information.

---

## 5. Visual design direction

The studio must look like Space Typing Admin, not a generic form builder.

### 5.1 Visual hierarchy

Use mostly neutral dark surfaces with restrained cyan/violet accents.

- Preview canvas is the visual hero.
- Settings use low-noise flat sections, not boxes nested inside boxes.
- Glow is reserved for focus, selection, active preview state and meaningful status.
- Exo 2 is used for compact headings/labels where already defined by Admin V2; Be Vietnam Pro remains the readable body font.
- Status chips use text + icon, never color alone.
- Spacing is generous enough to scan quickly.
- Inputs line up vertically; labels remain short.

### 5.2 Responsive studio layout

#### Standard desktop / laptop

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Vanguard                                Draft    [⋯]                  │
│ [General] [Visual] [Motion] [Effects] [Unlock] [Preview]            │
├──────────────────────────────┬───────────────────────────────────────┤
│ SETTINGS                     │ LIVE PREVIEW                          │
│                              │                                       │
│ Main Visual                  │            production scene           │
│ [ thumbnail ] [Replace]      │                                       │
│                              │                                       │
│ Size        ─────●──  1.10   │ [Idle] [Move] [Fire] [Skill] [Hit]   │
│ Position X  ───●────  +8     │ [Low HP] [Death]                     │
│ Position Y  ──●─────  -12    │                                       │
│                              │ [Play] [Pause] [Reset] [Bounds]       │
│ ▸ Advanced                   │                                       │
└──────────────────────────────┴───────────────────────────────────────┘
│ Unsaved changes  [Discard] [Save Draft] [Validate] [Review] [Publish]│
└──────────────────────────────────────────────────────────────────────┘
```

Recommended proportion:

- settings: ~35–45% / 400–480 px practical width;
- preview: ~55–65%, flexible;
- lifecycle bar: sticky bottom;
- preview remains visible while tuning within the section.

#### Wide desktop

A narrow section rail may be added to the left only when space allows. It must not reduce the preview to a small card.

#### Narrow laptop / tablet

- section tabs remain at top;
- preview can move above settings or collapse into a resizable panel;
- one-column fields;
- complex 3D tuning may be review-only on very small screens.

### 5.3 Controls

For scalar visual tuning, prefer **slider + numeric input + Reset** together.

Example:

```text
Size  ⓘ
[──────●────] [1.10] [Reset]
```

This gives fast visual adjustment and precise values without exposing raw config.

For common motion/effect choices, prefer presets first:

```text
Idle Motion
[ Default ▼ ]

Default
Gentle
Dynamic
Custom
```

Only `Custom` reveals fine-grained parameters.

### 5.4 Direct manipulation

For 2D assets, a later enhancement may allow dragging the preview object to change X/Y and handles to change size. It must write the same canonical draft fields as the numeric controls—never maintain a separate preview-only state.

Direct manipulation is not required for the first A5 slice; reliable renderer parity is more important.

---

## 6. Architecture boundary — Media vs domain tuning

Media V2 and domain configuration have different responsibilities.

### Media V2 owns

- logical asset identity;
- immutable asset versions;
- bytes/reference components;
- media type;
- provenance;
- metadata;
- usage references;
- archive/version lifecycle.

### Domain definitions own

- which exact asset version is assigned to an entity slot;
- scale/offset/rotation and other supported presentation tuning;
- motion presets/parameters;
- weapon/projectile relationships;
- VFX/SFX bindings;
- animation clip mapping where supported;
- entity-specific preview scenario defaults.

### Rule

> Do not add render tuning to the generic Media record simply because multiple domains can tune visuals.

The same immutable image may be used by two entities with different presentation tuning. Media stores the asset; each domain stores how it uses that asset.

Published definitions must continue pinning an exact immutable `assetVersionId`, never a floating `latest` alias.

---

## 7. Asset Slot Profile — the key abstraction

Every assignable slot has a child-owned or jointly-audited **Asset Slot Profile**.

Conceptually:

```ts
type AssetSlotProfile = {
  slotId: string;
  label: string;
  allowedMediaKinds: string[];
  requirements: {
    alpha?: "required" | "allowed" | "forbidden";
    aspectRatio?: { min: number; max: number };
    minWidth?: number;
    minHeight?: number;
    maxBytes?: number;
  };
  supportedControls: SupportedPresentationControls;
  previewStates: string[];
  processingProfile?: string;
};
```

This is conceptual, not permission to invent a universal runtime schema. Each real profile must be derived from actual child consumption.

Examples of slot identities:

```text
ship.mainVisual
ship.thumbnail
ship.model
ship.engineEffect
ship.damageEffect
ship.deathEffect
projectile.visual
projectile.trailEffect
projectile.impactEffect
skill.icon
skill.castEffect
skill.impactEffect
shop.promotionalVisual   // only after real Shop runtime consumption exists
```

### Profile-driven UI

The profile drives:

- which assets the Asset Picker shows;
- file validation on upload;
- which tuning controls appear;
- ranges/defaults/units;
- which preview state buttons appear;
- whether processing is required;
- whether the slot is read-only because runtime ownership has not migrated.

This prevents the Portal from becoming the hidden owner of gameplay presentation rules.

---

## 8. Capability-driven controls

The production runtime must be the authority for which tuning fields are meaningful.

Conceptual capability shape:

```ts
type SupportedPresentationControls = {
  uniformScale?: { min: number; max: number; step: number };
  offsetX?: { min: number; max: number; step: number; unit: "px" | "world" };
  offsetY?: { min: number; max: number; step: number; unit: "px" | "world" };
  rotation?: { min: number; max: number; step: number };
  opacity?: { min: number; max: number; step: number };
  idleMotionPreset?: string[];
  recoilPreset?: string[];
  effectScale?: { min: number; max: number; step: number };
};
```

### Hard invariant

Portal must not define a `glowIntensity`, `pitch`, `roll`, `recoil`, `blendMode`, etc. input unless the child production path consumes that exact authored concept.

A5.0 therefore starts with a runtime/render inventory before schema expansion.

---

## 9. Media import and processing pipeline

A safe flow is:

```text
RAW SOURCE
   ↓
Media V2 upload / reference admission
   ↓
Slot profile validation
   ↓
Optional non-destructive processor
   ↓
Immutable derived component/version metadata
   ↓
Exact assetVersionId
   ↓
Domain presentation config
   ↓
Production preview
```

### 9.1 What can be automated for 2D

Where useful and architecture-approved:

- dimension validation;
- aspect-ratio validation;
- alpha-channel validation;
- safe file-size limits;
- thumbnail generation;
- optional immutable WebP/runtime variant generation;
- transparent-bound analysis;
- safe-area warnings.

The processor must never silently overwrite uploaded bytes.

If Media V2 does not yet model derived variants, A5 must extend it explicitly with provenance such as:

```text
sourceAssetVersionId
processorId
processorVersion
derivedAt
```

rather than mutating an existing immutable version.

### 9.2 Do not over-process artwork

Automatic crop/trim is dangerous for assets whose composition/anchor depends on transparent margins. Prefer warnings + preview unless the slot profile explicitly declares a deterministic processor.

### 9.3 3D

Current/generated ship 3D bundles and future GLB assets must be treated according to their actual runtime consumer.

Do not assume that uploading a `.glb` automatically makes it production-compatible.

A future/imported 3D profile may validate:

- accepted container format;
- bounds and scale;
- origin/pivot;
- material/texture constraints;
- triangle/texture budgets;
- named animation clips;
- required/optional clips;
- static vs animated model support.

The first 3D implementation must support only profiles that the child renderer can actually load.

---

## 10. 2D, VFX and 3D capability tiers

### Tier 1 — direct administrator tuning

Best fit for first implementation:

- icon;
- thumbnail;
- portrait/card art;
- 2D ship sprite where runtime supports authored sprite assignment;
- 2D projectile visual where runtime supports it.

Typical flow:

```text
select/upload → validate → size/position → preview → publish
```

### Tier 2 — profile + runtime effect binding

Examples:

- projectile trail;
- muzzle effect;
- impact effect;
- engine glow;
- low-HP smoke/fire;
- explosion.

Important: procedural VFX remains gameplay/runtime-owned. Media V2 must not pretend a procedural effect definition is an uploaded image asset.

Admin may select a canonical effect/preset and tune only explicitly supported parameters.

### Tier 3 — strict model/animation support

Examples:

- ship 3D model/bundle;
- animated boss model;
- skeletal animation clips.

Admin may eventually:

- assign a validated compatible model/bundle;
- adjust runtime-supported transform;
- map existing clips to semantic states;
- preview clips;
- tune supported transition/timing parameters.

Admin does not rig or create missing animation data.

---

## 11. Preview architecture — production parity first

Preview is the most important technical invariant of this plan.

### 11.1 Forbidden

```text
Portal-only fake renderer
Portal-only movement formula
Portal-only VFX approximation presented as canonical
hardcoded preview animation that gameplay does not use
```

### 11.2 Preferred architecture

The child owns an isolated **Admin Preview Harness** built from production renderer/presentation modules.

Conceptual flow:

```text
Portal Asset Tuning Studio
        │
        │ validated draft preview message / request
        ▼
Child Admin Preview Harness
        │
        ├─ production asset resolver
        ├─ production ship/skill/projectile renderer
        ├─ production effect bindings
        └─ production motion/state logic where safe
        ▼
Rendered preview frame
```

Because parent and child are separate applications, an isolated child preview route/frame is preferable to copying renderer logic into Portal.

A possible host contract:

```ts
type AdminPreviewRequest = {
  protocolVersion: 1;
  entityType: "ship" | "projectile" | "skill" | "shop-presentation";
  entityId: string;
  draftDefinition: unknown;
  previewState: string;
  scenario?: unknown;
};
```

The concrete schema must be domain-specific and validated; `unknown` above only indicates this document is not defining runtime payload fields ahead of the child audit.

### 11.3 Same-origin isolated frame option

A practical implementation option is a child-owned preview route embedded by the Portal in a sandboxed/same-origin frame and controlled through a versioned `postMessage` contract.

Required safety:

- strict origin check;
- strict protocol/schema validation;
- no arbitrary script/file path in messages;
- no PlayerSave mutation;
- no active revision mutation;
- explicit teardown on route change;
- stale request IDs ignored;
- preview errors returned as structured warnings.

If direct shared-module import is later proven cleaner, it is acceptable only when it still executes the same production code path.

### 11.4 Preview states

The UI exposes only states supported by the entity/runtime:

```text
Idle
Move
Fire
Skill
Hit
Low HP
Death
```

Not every entity has every state.

### 11.5 Preview toolbar

Keep the toolbar compact:

```text
[Play/Pause] [Reset] [Background] [Bounds] [Grid] [Zoom]
```

Developer-only overlays such as raw anchors/hitboxes may be behind `Advanced` or Developer Tools.

### 11.6 Draft vs Published

Where practical, allow a quick comparison:

```text
[ Draft ] [ Published ]
```

or a split/toggle view.

This comparison must use two real definitions, not visual guessing.

---

## 12. Ship settings — target A5 experience

### General

Administrator-facing fields only when canonical:

- display name;
- description;
- class/role;
- rarity;
- enabled/status;
- sort/order where runtime supports it.

### Visual

Primary visible controls:

- Main Visual / Model picker;
- Thumbnail picker;
- Size;
- Position X/Y;
- Rotation only if meaningful;
- Preview background.

Advanced, only if supported:

- pivot/anchor;
- per-axis transform;
- layer/depth;
- opacity;
- model scale/origin correction.

### Motion

Prefer presets before raw parameters:

```text
Idle Motion     [Default ▼]
Movement Feel   [Default ▼]
Recoil          [Default ▼]
```

`Custom` reveals only child-supported controls such as amplitude, speed, tilt, recoil distance or recovery time.

For 3D, roll/pitch/yaw tuning is shown only if the production 3D movement renderer consumes those values.

### Effects

Use typed reference pickers:

- Engine VFX;
- Muzzle VFX;
- Projectile;
- Trail VFX;
- Impact VFX;
- Low HP effect;
- Death explosion;
- Fire/impact/death SFX.

Each effect row shows a tiny preview/status and an Edit/Replace action, not raw IDs.

### Preview

State chips:

```text
Idle | Move | Fire | Skill | Hit | Low HP | Death
```

The right preview stays visible while changing Visual/Motion/Effects.

### 3D clip mapping

If the runtime supports model clips, expose semantic mapping instead of raw animation systems:

```text
Idle            [ idle_loop ▼ ]
Attack          [ attack_primary ▼ ]
Skill Cast      [ cast_skill ▼ ]
Hit             [ hit_react ▼ ]
Death           [ death ▼ ]
```

Missing required clips produce an actionable validation warning. The Admin does not fabricate missing clips.

---

## 13. Weapon and projectile settings

A5 must not bury projectile/effect configuration inside dozens of Ship fields when the runtime treats them as reusable definitions.

### Weapon

Show only canonical fields such as:

- name;
- weapon type;
- fire/cooldown properties;
- projectile reference;
- muzzle VFX;
- fire SFX;
- supported hit behavior.

### Projectile

Visual section:

- image/model/preset;
- size;
- supported offset/orientation;
- trail VFX;
- impact VFX;
- impact SFX.

Behavior fields such as speed/lifetime/range appear only where canonical runtime ownership exists.

Preview actions should include:

```text
Fire once
Loop fire
Hit target
Miss target
```

where those scenarios are safe and deterministic.

---

## 14. Skills / Equipment adoption in A6

The same studio primitives can be reused, but Skill/Equipment keep domain-specific schemas.

### Skill

Potential supported slots:

- icon;
- cast effect;
- projectile effect;
- trail;
- impact;
- area effect;
- activation SFX.

Potential presentation tuning, only when consumed:

- effect scale;
- local offset;
- spawn delay;
- lifetime;
- intensity/tint if the effect system supports authoring them;
- semantic animation/state binding.

Preview may offer:

```text
Icon | Cast | Travel | Impact | Full Sequence
```

### Equipment

Focus on visual/icon and effect references where real. Stats/perks remain Equipment-domain data, not Media fields.

---

## 15. Shop adoption — preserve Shop ownership rules

Shop requires extra care because A4 already established that generated `ShopInstance` values are runtime policy outputs and Item/Equipment identity stays with its owning registry.

Therefore:

- generic Item/Equipment artwork should be authored by the owning Item/Equipment presentation domain and consumed by Shop;
- Shop must not duplicate names/images into a shadow product record;
- a Shop-specific promotional/card asset may become authorable only after the child Shop UI consumes a canonical Shop presentation field;
- compare-at price/badge remains Shop policy data as already implemented;
- persisted Shop instances must never be silently re-rendered/repriced with incompatible semantics merely because a new Admin revision is published.

The Asset Tuning Studio may be reused for Shop **only after** that presentation ownership exists.

Until then the UI may preview product imagery from its canonical Item/Equipment owner but must not show a fake writable Shop image field.

---

## 16. Settings information architecture

The normal entity editor should use a small number of task tabs:

```text
General | Visual | Motion | Effects | Unlock | Preview
```

Domain-specific tabs may replace irrelevant ones.

### Visual tab

One primary asset at top, then only the most common transform controls.

### Motion tab

Preset selection first. Custom parameters progressively disclosed.

### Effects tab

Reference cards/pickers grouped by event:

```text
On Fire
On Travel
On Hit
On Damage
On Death
```

This is easier to understand than grouping by technical implementation type.

### Preview tab

Larger scene, scenario controls, Draft/Published comparison and validation warnings.

The right live preview remains available in Visual/Motion/Effects, so the dedicated Preview tab is for deeper testing rather than the only place preview exists.

---

## 17. Field interaction patterns

### Asset field

```text
Main Visual                                            ⓘ
┌──────────┐  Vanguard Sprite
│ preview  │  PNG · 1024×1024 · Transparent
└──────────┘  [Replace] [Open in Media]
```

Do not show the filesystem path.

### Reference field

```text
Projectile
[ Plasma Bolt                                  ▾ ]
```

Picker shows visual preview and administrator-facing name first. Canonical ID is Advanced detail.

### Preset field

```text
Idle Motion
[ Gentle                                       ▾ ]
```

### Tuning field

```text
Size                                                   ⓘ
[────────●────] [1.10] [↺]
```

### Dirty state

Only changed controls receive subtle draft markers. Avoid highlighting the whole screen.

### Reset semantics

`Reset` returns to the domain/profile default, not an arbitrary UI constant.

---

## 18. Validation UX

Validation should happen at three levels.

### Immediate field validation

Examples:

- unsupported file type;
- scale outside allowed range;
- missing required reference.

### Asset compatibility validation

Examples:

- image too small;
- alpha required;
- model profile incompatible;
- missing required animation clip;
- referenced effect cannot be used by this slot.

### Publish validation

Examples:

- missing canonical asset version;
- archived referenced asset;
- invalid cross-entity reference;
- preview/runtime contract mismatch;
- revision conflict.

Errors should say what the administrator can do next.

Bad:

```text
E_ASSET_17 invalid schema path
```

Good:

```text
Attack animation is missing.
Choose one of the animation clips available in this model before publishing.
```

Raw codes may remain in Advanced diagnostics.

---

## 19. Accessibility

Hard requirements:

- every control has a real label;
- tooltip/help is keyboard/touch accessible;
- visible focus ring;
- slider always has a numeric input equivalent;
- no drag-only operation;
- preview state controls are buttons;
- play/pause state is announced;
- dialogs/pickers trap and restore focus correctly;
- Escape closes temporary overlays;
- color is never the only dirty/error/status indicator;
- preview canvas has a textual state summary for non-visual operation.

---

## 20. Performance and lifecycle

The studio can become expensive, especially with 3D/VFX.

Requirements:

- lazy-load preview runtime only when needed;
- do not reload model/assets on every numeric keystroke when a transform update is enough;
- debounce high-frequency form updates where necessary;
- use request IDs and ignore stale async preview results;
- cancel/teardown listeners/workers/animation loops on route change;
- release Object URLs and GPU resources;
- pause preview when hidden;
- cache immutable asset metadata by version ID;
- never cache draft state as if it were published state.

---

## 21. Draft / preview / publish semantics

The existing Admin V2 lifecycle remains authoritative:

```text
Edit
→ Save Draft
→ Validate
→ Preview
→ Review Change Scope
→ Publish
```

### Preview never publishes

Preview receives a draft definition and must not mutate:

- active runtime config;
- PlayerSave;
- Shop instances;
- Media logical version pointers;
- published entity definitions.

### Upload does not publish

Uploading or creating a Media version alone remains `changesGameplay: false`.

Gameplay changes only when a domain draft references the exact version and that revision is published.

### CAS remains whole-revision aware

The lifecycle bar must not imply that publishing a Ship guarantees only that Ship changes. Review Changes must show the actual revision/change scope defined by A0.5.

---

## 22. Runtime ownership audit required before implementation

A5.0 must inventory actual child ownership before adding fields.

For Ships / Weapons / Projectiles record:

```text
Current definition owner
Current visual source
Current renderer
Current transform parameters
Current movement parameters
Current projectile owner
Current VFX owner
Current SFX owner
Current 2D/3D capability
Current animation representation
Current preview/test hooks
Current runtime apply boundary
Persistence implications
```

Every proposed control is then classified:

```text
SUPPORTED NOW
REQUIRES CANONICAL MIGRATION
READ-ONLY REFERENCE
DEFERRED / UNSUPPORTED
```

This audit is mandatory because this plan intentionally describes the desired administrator experience without pretending all controls already exist.

---

## 23. Proposed implementation slices

### A5.0 — Renderer / presentation ownership gate

- fetch newest parent/child heads;
- audit real Ship/Weapon/Projectile renderer and definition owners;
- document 2D/3D paths actually used by production;
- define slot profiles from real runtime capability;
- decide child preview harness integration;
- define domain presentation schema only for consumed fields;
- lock preview parity tests before UI implementation.

Exit: no proposed writable control lacks a canonical runtime consumer.

### A5.1 — Shared Asset Tuning Studio shell

Parent UI:

- responsive Settings + Live Preview layout;
- shared Asset field;
- slider + numeric + reset control;
- Basic/Advanced disclosure;
- state chips;
- compact preview toolbar;
- loading/error/compatibility states;
- lifecycle integration.

Child:

- isolated preview harness/protocol using production presentation modules;
- no mutation;
- teardown and schema validation tests.

Exit: one audited fixture can be tuned and previewed without duplicated render logic.

### A5.2 — Ship 2D administrator workflow

- main visual assignment;
- supported transform tuning;
- supported idle/move/recoil presets/parameters;
- typed projectile/VFX/SFX references;
- Idle/Move/Fire/Hit/Low HP/Death preview where production supports them;
- draft/validate/publish path.

Exit: administrator can make a real visual adjustment and see the published gameplay consume it.

### A5.3 — Weapon / Projectile / VFX binding workflow

- reusable weapon/projectile entity/reference UX where canonical;
- projectile visual tuning;
- muzzle/trail/impact/death effect binding;
- production preview scenarios;
- cross-reference validation.

### A5.4 — Strict 3D model / animation support

Only after the current 3D production path is audited.

- compatible model/bundle picker;
- validated transform;
- available clip discovery;
- semantic clip mapping;
- clip/state preview;
- resource cleanup/performance tests.

Do not promise arbitrary GLB compatibility.

### A6 adoption — Skills / Equipment

Reuse studio primitives while defining Skill/Equipment-owned schemas and preview scenarios.

### Later Shop presentation adoption

Only after Shop-specific visual fields are canonical runtime-consumed; otherwise Shop reads canonical Item/Equipment presentation.

---

## 24. Automated verification strategy

At minimum:

### Contract tests

- slot profiles match child runtime capabilities;
- allowed asset kinds/ranges do not drift silently;
- unknown tuning fields fail closed.

### Preview parity tests

For representative definitions:

- draft preview and production renderer resolve the same asset version;
- same transform/preset produces the same resolved presentation values;
- same effect references resolve identically;
- preview has no write side effects.

### UI tests

- Basic does not expose Advanced controls;
- selecting `Custom` reveals only supported controls;
- Replace uses typed Asset Picker filters;
- no raw path input exists;
- keyboard-accessible preview controls;
- route teardown removes listeners/preview sessions;
- stale async responses do not overwrite newer draft state.

### Lifecycle tests

- upload alone does not change gameplay;
- draft tuning does not change active runtime;
- preview does not publish;
- publish activates validated exact asset versions/config;
- rollback resolves previous exact versions/config;
- CAS conflict is surfaced rather than overwritten.

---

## 25. Manual acceptance scenarios

A5 is not accepted only because the form saves.

Required administrator scenarios:

1. Open a Ship without seeing filesystem paths, child SHA or raw config.
2. Replace/select a compatible visual through Asset Picker.
3. Adjust size and position and immediately see the live preview update.
4. Reset a changed field to canonical default.
5. Switch Idle → Move → Fire → Hit and visually verify supported motion/effects.
6. Replace a projectile/effect reference and preview it.
7. Open Advanced and tune an actually supported parameter.
8. Attempt an incompatible asset and receive a clear compatibility error.
9. Save Draft and verify active gameplay remains unchanged.
10. Preview the draft through the production child path.
11. Review human-readable change scope.
12. Publish and verify a fresh runtime/session consumes the new presentation.
13. Roll back and verify the previous exact asset/config returns.
14. Navigate away during preview and verify no orphan animation/audio/listener continues.
15. Complete the normal task without raw IDs/paths/JSON/runtime terminology.

---

## 26. UX acceptance criteria — anti-clutter gate

A page fails the design gate if any of these are true:

- preview is visually secondary to a wall of controls;
- more than roughly 7 unrelated primary controls are visible in one group;
- Basic view requires understanding anchor math, manifests or renderer internals;
- permanent paragraphs explain concepts that belong in tooltip/help;
- nested cards/panels create unclear hierarchy;
- cyan/violet glow is used as decoration everywhere;
- raw IDs/paths dominate labels;
- unsupported settings are displayed disabled merely to look complete;
- every motion value is exposed instead of using sensible presets;
- the user must switch to a separate page after every small adjustment to see the result.

A page passes when an administrator can answer three questions immediately:

1. **What asset/effect am I editing?**
2. **What will it look/do like with these settings?**
3. **Is this Draft or Published?**

---

## 27. Key decisions to ask reviewers to challenge

Reviewers should specifically challenge:

1. Whether a child-owned preview harness/frame is the best parity boundary for the current codebase.
2. Whether any proposed tuning primitive is too generic for the existing runtime.
3. Whether Media V2 needs derived-variant metadata before automatic 2D processing.
4. Whether current Ship 3D production assets can share a profile with future GLB assets or must remain separate profiles.
5. Whether motion presets should resolve in child policy/runtime instead of being persisted as raw parameter sets.
6. Whether any Shop visual tuning would violate Item/Equipment ownership established by A4.
7. Whether the two-column Studio remains usable at current Admin breakpoints and with long translated labels.
8. Whether preview parity can be asserted strongly enough without introducing a second renderer.

---

## 28. Final architecture invariant

The finished system should feel simple to an administrator because complexity is absorbed by profiles, presets, validation and the production preview—not because the system hides a fake second implementation.

The desired end state is:

```text
Administrator chooses a compatible asset
        ↓
Admin shows only relevant controls
        ↓
Administrator tunes visually
        ↓
Production renderer shows the result immediately
        ↓
Draft is validated and published safely
```

That is the standard A5/A6 and future presentation-heavy domains must follow.
