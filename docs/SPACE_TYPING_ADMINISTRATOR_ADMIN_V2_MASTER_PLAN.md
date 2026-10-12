# Space Typing Administrator Admin V2 — Master Plan

> Status: PLANNING SOURCE OF TRUTH — REVIEWED / HARDENED
>
> Scope: `sinhvienaiti/typing-game` + `sinhvienaiti/space-typing`
>
> Review date: 2026-10-13
>
> Parent working branch: `feat/space-typing-admin-uiux`
>
> Parent HEAD observed immediately before this review/update: `f45ba4aa1929e2bab8b3b73e1cbdb583ab8d84ed`
>
> Child Admin integration branch: `feat/admin-world-music-stage-policy`
>
> Child HEAD observed immediately before this review/update: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
>
> IMPORTANT: these SHAs are checkpoints only. Every implementation worker MUST fetch current GitHub HEADs first and use newer Git state as source of truth. Never reset a branch to the SHAs in this document.

---

# 0. Executive decision

The current Space Typing Admin Phase B established important engineering foundations: authenticated Admin APIs, runtime ownership audits, revision-backed configuration, validation, preview bridges, canonical child integration, publish/rollback infrastructure, and removal of legacy fake/mock production routing.

Those foundations remain valuable and must be preserved.

The current product surface, however, is still too developer-oriented. A normal administrator is currently exposed to runtime contracts, canonical IDs, source ownership, capability evidence, apply boundaries, child SHAs, persistence details and implementation language that should not be required for routine game management.

Admin V2 changes the primary product model from:

```text
Admin screen = runtime/config inspector with some editing
```

into:

```text
Administrator workflow
        ↓
Admin Domain API
        ↓
Admin Domain Service
        ↓
Domain validation + permissions + audit
        ↓
Canonical persisted definition / revision / change set
        ↓
Runtime adapter / generated artifact when required
        ↓
Space Typing runtime consumer
```

The existing technical information is not deleted. It is relocated to **Developer Tools / Diagnostics / Advanced details**.

## Hard product rule

> If a normal administrator must understand source code, JSON structure, filesystem paths, canonical runtime IDs, child SHAs, protocol versions, runtime evidence, persistence ownership or implementation boundaries to complete a routine task, that Admin V2 workflow is not finished.

This is a hard acceptance criterion.

---

# 1. Product-owner requirements locked by this plan

These requirements must survive every implementation decision.

## 1.1 Administrator orientation

The primary Admin product is for administrators and game operators, not developers.

## 1.2 Shop

Administrators must ultimately be able to manage real runtime-consumed product data, including applicable fields such as:

- product presentation;
- product name/label;
- price;
- sale price / discount;
- discount label/badge such as SALE / HOT / NEW / LIMITED;
- availability/schedule;
- media;
- purchase limits/stock semantics where runtime genuinely supports them;
- preview before publish.

The current Shop runtime-contract inspector is not considered a finished Shop admin screen.

## 1.3 Ships

Administrators must ultimately be able to manage applicable ship properties such as:

- image / authored visual asset;
- 3D model where supported;
- display name;
- description / class / rarity;
- weapon;
- projectile;
- VFX;
- SFX;
- unlock rule;
- related media;
- preview/test behavior.

No raw path editing should be required.

## 1.4 UI density

Permanent short descriptions and architecture-heavy subtitles must be removed substantially.

Help should use styled tooltips/info icons/help drawers and progressive disclosure.

## 1.5 Developer information

Runtime contracts, SHAs, protocol versions, source ownership, raw paths, registry evidence and similar technical information remain available, but under **Developer Tools / Advanced** rather than the normal administrator workflow.

---

# 2. Verified current-state constraints that shape V2

The following are not theoretical concerns. They were observed in the current implementation and must influence sequencing.

## 2.1 Current shell is still developer-heavy

Current navigation/page helpers render permanent descriptions and technical explanatory text. Admin V2 must replace this with concise labels, contextual help and task-oriented state messages.

## 2.2 Current UI construction is imperative DOM TypeScript

The existing admin is not a React component system. V2 shared components must therefore define lifecycle and cleanup explicitly instead of assuming framework-managed cleanup.

This is especially important for tooltips, dialogs, outside-click handlers, keyboard handlers, async loading and focus restoration.

## 2.3 Current Shop is runtime-backed read-only

The current Shop screen exposes a runtime contract, not a canonical administrator-authored commerce model.

Therefore:

> Do not add edit buttons to the existing Shop inspector until canonical Shop authoring architecture is decided and implemented.

## 2.4 Current Ships editor is a registry/config override editor

The existing Ships workflow has useful revision/preview foundations but exposes IDs, asset IDs, procedural settings and implementation boundaries more prominently than real administrator concepts.

It must evolve into an entity workflow, not merely receive cosmetic wording changes.

## 2.5 Current revision/publish model is whole-config oriented

Existing revisions contain complete config state and publish uses compare-and-swap against the active revision.

This means an entity editor cannot casually present `Publish` as if it were guaranteed to publish only that entity.

V2 must define change scope and publish semantics before writable entity workflows are considered complete.

## 2.6 Current authentication is minimal/local-oriented

The current server model is effectively a local Admin service with a shared token and no mature user/role identity model.

The plan may target roles, audit and multi-user-safe mutation, but implementation must not pretend those capabilities already exist.

## 2.7 Current generic Media architecture is incomplete

Music already has stronger upload/catalog behavior than several other asset types. Images, models, VFX and other media do not yet share a complete writable canonical Media service.

Therefore Media UI must follow a Media architecture gate rather than immediately creating generic upload/edit screens over inconsistent owners.

## 2.8 Existing validator freezes Phase B presentation details

Current Admin validation includes useful canonical/runtime safety checks, but also hardcodes old routes/labels/status text and other presentation details.

V2 must migrate those assertions deliberately. Do not weaken canonical safety checks simply to make the new UI pass.

---

# 3. Product principles

## P01 — Administrator-first language

Use domain language: Product, Price, Ship, Weapon, Boss, Reward, Event, Image, Music, Draft, Preview, Publish.

Implementation language belongs in Developer Tools.

## P02 — Progressive disclosure

Show only information needed for the current task.

- basic fields visible;
- advanced fields in Advanced sections/drawers;
- help behind tooltips/info icons;
- diagnostics under Developer Tools;
- conditional fields shown only when relevant.

## P03 — Tooltip-first help

Do not render permanent helper paragraphs where a label is self-explanatory.

Example:

```text
Price                                    ⓘ
[ 2,000                                  ]
```

Tooltip:

```text
PRICE
Base purchase price before promotion discounts.
```

Permanent inline copy is reserved for validation, warnings, state, destructive consequences or task-critical instructions.

## P04 — Visual management instead of path management

Wrong:

```text
/assets/ships/vanguard.png
```

Correct:

```text
Ship Image
[ preview ]
[ Replace ] [ Remove ]
```

## P05 — Safe lifecycle

Routine mutation flow:

```text
Edit → Save Draft → Validate → Preview → Review Change Scope → Publish
```

No routine edit silently mutates live gameplay.

## P06 — One source of truth

No shadow Admin database/config that gameplay does not consume canonically.

If a domain has no authorable owner, implement the owner first.

## P07 — Lists first, details second

Large domains use searchable/filterable list or card views followed by focused entity editors.

## P08 — Preview visual/experiential output

Ships, weapons, projectiles, bosses, VFX, backgrounds, music, SFX, shop cards, promotions and stages should provide meaningful preview/test surfaces where practical.

## P09 — Server-side permissions

UI hiding is not authorization. Every mutation/publish/destructive action must be permission-checked server-side once the permission foundation exists.

## P10 — Preserve Space Typing identity

Keep the dark sci-fi command interface, restrained cyan/violet accents, Exo 2 / Be Vietnam Pro typography, angular panels and high-contrast states.

Reduce noise; do not turn Admin into a generic white SaaS dashboard.

## P11 — Real-data-only UI

Do not invent dashboard counters, scheduled events, audit entries, player data or capabilities merely to make a screen look complete.

Unavailable capability should be represented honestly and quietly.

## P12 — Capability-aware navigation

The target IA is the final destination, not a requirement to render dozens of dead routes immediately.

Normal navigation should expose administrator workflows only when they are implemented or meaningfully usable.

---

# 4. Deployment model gate

Before first major writable V2 domain, A0 must record the intended deployment model.

## Current verified implementation assumption

Current Admin infrastructure is local-oriented and must be treated as such until architecture explicitly changes it.

## A0 decision required

Choose and document one of these directions for the current milestone:

### D1 — Local authoring/control plane

Admin runs locally for trusted operators/developers; published artifacts/config are later deployed through existing project flow.

### D2 — Remote production control plane

Admin is a networked multi-user service with production authentication, authorization, persistent identity, concurrency, durable storage, scheduling and security requirements.

### Rule

Do not partially design as D1 while implementing role/audit/scheduling assumptions as if D2 already exists.

A future migration from D1 to D2 is allowed, but the boundary must be explicit.

---

# 5. Target users, roles and permission model

Target roles remain:

- Super Admin
- Game Designer
- Economy Manager
- Content Manager
- Live Ops Manager
- Media Manager
- Support / Player Operations — only when real player backend exists
- Developer
- Viewer

Target permission format:

```text
resource.action
```

Examples:

```text
shop.read
shop.write
shop.publish
ships.write
media.upload
media.replace
events.publish
developer.runtime-inspect
```

## Critical sequencing change

The complete Roles & Permissions management UI remains a later phase, but **minimal permission infrastructure must exist before the first writable V2 domain ships**.

Minimum early foundation:

- current actor identity model;
- permission evaluation service;
- server-side mutation/publish authorization hook;
- Developer Tools permission boundary;
- test coverage proving UI hiding cannot bypass server authorization.

A13 later builds the administrator-facing role-template/granular-permission UI on top of this foundation.

---

# 6. Target information architecture

```text
SPACE TYPING ADMIN

Dashboard

CONTENT
├── Worlds
├── Stages
├── Routes
├── Objectives
├── Challenges
└── Typing Content

GAMEPLAY
├── Ships
├── Weapons
├── Projectiles
├── Skills
├── Equipment
├── Enemies
└── Bosses

ECONOMY
├── Shop
├── Products
├── Currencies
├── Rewards
├── Drop Tables
└── Unlock Rules

MEDIA
├── Images
├── 3D Models
├── Music
├── SFX
└── VFX

LIVE OPS
├── Events
├── Promotions
├── Discounts
└── Announcements

PVP / MODES
├── Duel
├── Ranked
└── Alternative Modes

PLAYERS
├── Players        (only when canonical backend exists)
├── Progress       (only when canonical backend exists)
├── Inventory      (only when canonical backend exists)
└── Transactions   (only when canonical ledger exists)

SYSTEM
├── Game Settings
├── Roles & Permissions
├── Audit Log
├── History & Publish
└── Developer Tools
    ├── Runtime Inspector
    ├── Contract Inspector
    ├── Validation
    ├── Asset Diagnostics
    └── QA Sandbox / Test Lab
```

## Navigation rules

- expanded sidebar: icon + concise label only;
- collapsed sidebar: icon + styled tooltip;
- no permanent per-item short descriptions;
- do not expose unavailable target routes merely because they exist in the target IA;
- Developer Tools is permission-gated;
- technical routes should migrate into Developer Tools incrementally as each V2 domain replaces its Phase B inspector.

---

# 7. Global UI/UX specification

## 7.1 Visual density

Prefer:

- concise headings;
- optional one-line task context only when necessary;
- tooltips/info icons;
- compact status chips;
- drawers/accordions for advanced details;
- warnings only when actionable.

Avoid:

- architecture paragraphs in page headers;
- source/owner subtitles under every panel;
- repeated permanent helper text;
- stacked notices saying the same thing;
- multiple technical badges in normal workflows.

## 7.2 Standard header

```text
Ships                                  [ + Create Ship ]
Fleet management                        [ Search ] [ Filter ]
```

Subtitle may be omitted when redundant.

## 7.3 Standard field

```text
Display Name                            ⓘ
[ Vanguard                              ]
```

Optional field states:

- required;
- invalid;
- warning;
- read-only lock;
- pending draft change.

## 7.4 Tooltip component — hard requirement

Create a reusable first-class component, not browser-native `title` only.

Conceptual API:

```ts
createAdminTooltip({
  title: "Sale price",
  content: "Temporary promotional price. Must be lower than base price.",
  placement: "auto",
});
```

### Visual

- dark/translucent Space Typing panel;
- thin cyan/violet border;
- subtle glow;
- angular corner treatment consistent with shell;
- Exo 2 title / Be Vietnam Pro body;
- ~280–340px max width;
- restrained fade/translate transition;
- high z-index;
- collision-aware placement.

### Interaction

Desktop:

- hover;
- keyboard focus;
- Escape closes persistent/focus state.

Touch:

- tap toggles;
- outside tap closes.

### Accessibility

- interactive trigger is a real button;
- keyboard reachable;
- `aria-describedby` / appropriate semantics;
- help never requires mouse-only hover.

### Imperative DOM lifecycle requirement

Because current Admin is imperative DOM TypeScript, tooltip implementation must explicitly define:

- unique IDs;
- event listener cleanup;
- outside-click cleanup;
- Escape handler cleanup;
- focus restoration where applicable;
- viewport collision/flip behavior;
- stale tooltip removal during route/screen teardown;
- no orphan document-level listeners after rerender/navigation.

## 7.5 Help Drawer

Tooltip: 1–4 short lines.

Longer explanation uses:

```text
Learn more →
```

and opens `AdminHelpDrawer`.

## 7.6 Inline state messages

Valid:

```text
⚠ Sale price must be lower than base price.
✓ Draft validated successfully.
⚠ This asset is used by 12 entities.
```

Invalid as permanent inline documentation:

```text
This field controls how the child runtime resolves ...
```

## 7.7 Conditional fields

Show fields only for selected rule types.

Example:

```text
Unlock Type
[ World Completion ▼ ]

Required World
[ G04 — Frozen Rift ▼ ]
```

## 7.8 Lists

Large entity domains should support applicable combinations of:

- search;
- filters;
- sort;
- status chips;
- pagination/virtualization where required;
- create;
- edit;
- duplicate;
- archive/disable;
- preview;
- safe bulk actions only when appropriate.

## 7.9 Entity editors

Complex entities use tabs/sections.

Example:

```text
Vanguard
[ General ] [ Visuals ] [ Combat ] [ Effects ] [ Unlock ] [ Preview ]
```

## 7.10 Sticky lifecycle bar

```text
Unsaved changes
[ Discard ] [ Save Draft ] [ Preview ] [ Review Changes ] [ Publish ]
```

The button label and behavior must reflect actual revision/change-set semantics described later in this plan.

---

# 8. Shared Admin V2 component system

Create reusable primitives before mass domain migration.

## Shell

- `AdminSidebar`
- `AdminTopbar`
- `AdminBreadcrumbs`
- `AdminPageHeader`
- `AdminPageActions`
- `AdminCommandPalette`

## Lists/data

- `AdminEntityTable`
- `AdminCardGrid`
- `AdminSearchInput`
- `AdminFilterBar`
- `AdminSortMenu`
- `AdminPagination`
- `AdminStatusChip`
- `AdminBulkActionBar`

## Forms

- `AdminField`
- `AdminTextInput`
- `AdminNumberInput`
- `AdminTextarea`
- `AdminSelect`
- `AdminMultiSelect`
- `AdminToggle`
- `AdminSegmentedControl`
- `AdminDateTime`
- `AdminDateRange`
- `AdminSlider`
- `AdminColorPicker`
- `AdminTagInput`
- `AdminEntityPicker`

## Help/state

- `AdminInfoIcon`
- `AdminTooltip`
- `AdminHelpDrawer`
- `AdminValidationMessage`
- `AdminWarningBanner`
- `AdminEmptyState`
- `AdminErrorState`
- `AdminSkeleton`

## Media

- `AdminAssetPicker`
- `AdminAssetCard`
- `AdminImagePreview`
- `AdminAudioPreview`
- `AdminModelPreview`
- `AdminVfxPreview`
- `AdminUploadDropzone`
- `AdminUsageReferences`

## Lifecycle

- `AdminDraftBar`
- `AdminPublishDialog`
- `AdminRevisionBadge`
- `AdminChangeSummary`
- `AdminAuditTimeline`

## Dialogs/drawers

- confirmation dialog;
- destructive confirmation;
- duplicate entity dialog;
- asset replacement dialog;
- advanced settings drawer;
- dependency/usage drawer.

### Component rule

A domain must not create a new one-off form/list/help/lifecycle pattern when a shared V2 component can satisfy the need.

---

# 9. Domain architecture and canonical ownership

## Required layers

```text
Administrator UI
      ↓
Admin Domain API
      ↓
Admin Domain Service
      ↓
Authorization + validation + audit
      ↓
Canonical persisted definition / revision / change set
      ↓
Runtime adapter / generated artifact if required
      ↓
Space Typing runtime consumer
```

## Preserve from Phase B

Keep where compatible:

- authenticated Admin service;
- revision model;
- CAS semantics;
- validation pipeline;
- publish/rollback;
- runtime preview bridges;
- canonical child registries;
- real asset/catalog builders;
- CI ownership/contract validators.

## Move out of primary UI

Move to Developer Tools/Advanced:

- child SHA evidence;
- runtime source paths;
- protocol versions;
- runtime ownership strings;
- raw contract tables;
- unsupported field matrices;
- raw capability manifests;
- persistence-owner diagnostics;
- exact apply-boundary implementation text;
- raw evidence lists.

## Missing capability policy

If a valid administrator requirement lacks a canonical owner:

1. identify current gameplay behavior;
2. define canonical domain model;
3. choose real owner in parent/child/service;
4. implement persistence/revision behavior;
5. implement validation;
6. implement runtime consumption;
7. expose Admin Domain API;
8. add Admin editor;
9. add preview using the same transform/runtime adapter;
10. add CI tests preventing divergence.

Never fabricate authoring with a disconnected Admin-only config.

---

# 10. Draft / change-set / publish architecture gate

This is a new mandatory gate before the first major writable V2 entity domain.

## Current risk

Current revisions are whole-config snapshots. Multiple entity/domain edits may coexist in one draft revision lineage.

Therefore the UI must not imply:

```text
Publish Vanguard
```

if the operation may also publish unrelated pending Shop/World/etc. changes.

## A0.5 decision required

Explicitly choose and document one model:

### Model R1 — Whole-config revision remains canonical

If retained:

- entity `Save Draft` may create/update a whole-config revision;
- `Review Changes` must show all pending changes included in publication;
- `Publish` copy must describe the real scope;
- unrelated pending changes must never be silently published;
- centralized History & Publish may remain the actual publication surface;
- entity editor may link/hand off to centralized publication.

### Model R2 — Change sets / domain-scoped drafts

If implemented:

- change set owns explicit entity/domain scope;
- merge/validation into canonical whole state is defined;
- conflict behavior is defined;
- publish/rollback remains auditable and deterministic.

### Hard acceptance

No writable V2 domain is complete until an administrator can clearly answer:

> “Exactly what changes will go live when I press Publish?”

---

# 11. Actor identity, permissions and audit foundation

## 11.1 Actor identity

Remove reliance on a generic default such as `local-admin` as the long-term audit identity.

A0.5 defines the minimal actor envelope appropriate for the chosen deployment model.

Example conceptual fields:

```text
actorId
actorDisplayName
authMethod
requestId
```

Do not overbuild production identity while the deployment model is local-only, but do not lose the ability to attribute mutations.

## 11.2 Permission foundation

Before first writable V2 domain:

- authorization service exists;
- server mutation routes call it;
- publish/rollback/destructive operations have explicit permissions;
- Developer Tools has explicit permission boundary;
- tests prove denied operations remain denied even when called directly.

## 11.3 Minimal audit event envelope

Every meaningful mutation/publish operation should be able to record:

```text
actor
action
domain
entity type
entity ID/reference
change scope
revision/change-set reference
timestamp
result
```

Human-readable field-level diff UI may come later in A14.

### Sequencing rule

A14 is the **full Audit Log UX**, not the first time audit exists.

---

# 12. Media architecture gate

Media management is a dependency for Shop, Ships, Bosses, Worlds, VFX and more.

Do not build a generic Media Library UI over inconsistent storage contracts first.

## A3.0 must define

For each asset type:

- canonical asset identity;
- display metadata;
- storage owner/location;
- immutable vs replaceable fields;
- file/hash/version semantics;
- MIME/type/dimension/duration/model validation;
- generated filename policy;
- duplicate detection policy;
- usage/reference lookup;
- replace semantics;
- archive/delete semantics;
- cache invalidation;
- preview URL/source behavior;
- revision/publish relationship;
- rollback expectations;
- provenance/source metadata where relevant.

## Media entity principle

Filesystem path is an implementation detail, not the administrator-facing identity.

Target asset detail:

```text
Vanguard Main Ship

[ Preview ]

Type        PNG
Dimensions  1024 × 1024
Used by     3 entities

Usage
• Ship: Vanguard
• Shop Product: Vanguard
• Ship Selection Card: Vanguard

[ Replace File ] [ Archive ]
```

## Asset Picker

All entity references should use one reusable picker with:

- search;
- type filter;
- tags;
- preview grid/list;
- upload new when permitted;
- select;
- usage context.

---

# 13. Administrator screen/domain specification

The following defines product intent. A route should become visible only when the underlying capability is real enough to support its workflow.

## 13.1 Dashboard

Goal: answer **“What needs my attention now?”**

Show only real data available from implemented domains, such as:

- drafts/unpublished changes;
- validation issues;
- broken/missing references;
- scheduled events/promotions when canonical scheduling exists;
- recent audit activity when audit source exists;
- high-level service health.

Do not fabricate counts or cards for future domains.

Do not show SHAs/protocols/raw capability evidence by default.

## 13.2 Shop / Products

Target catalog list/cards:

- image;
- product name;
- category;
- effective price;
- promotion/badge;
- availability;
- stock/limit summary when canonical;
- status;
- actions.

Product editor sections:

```text
General | Media | Pricing | Availability | Unlock | Preview
```

General:

- display name;
- short label;
- description;
- category;
- status;
- sort order.

Media:

- thumbnail;
- main image;
- optional card/background/icon.

Pricing:

- currency;
- base price;
- sale price;
- derived discount where appropriate;
- SALE/HOT/NEW/LIMITED/custom approved badge.

Availability:

- active/inactive;
- start/end;
- purchase limit;
- stock semantics only if canonical runtime supports them.

Preview should render the actual/near-actual gameplay shop presentation using canonical transforms.

### Mandatory architecture decision before write UI

Choose explicitly:

A. authored canonical product catalog consumed by runtime; or

B. authored merchandising layer over canonical gameplay items with runtime-owned price/stock generation.

Do not create a second disconnected catalog.

## 13.3 Currencies

Administrator concepts:

- display name;
- icon;
- symbol;
- enabled;
- cap if applicable;
- formatting;
- acquisition/source summary;
- spend/sink summary.

Internal ID/persistence owner belong in Advanced/Developer Tools.

## 13.4 Rewards / Drop Tables / Unlock Rules

Use entity/reference pickers and structured conditions instead of raw JSON.

Drop tables should support validation/simulation appropriate to the real runtime model.

Unlock rule types may include only genuinely supported conditions such as:

- always unlocked;
- world completed;
- stage completed;
- player level;
- purchase/currency requirement;
- achievement/mission only when canonical.

## 13.5 Ships

Fleet list:

- visual preview;
- display name;
- class/rarity;
- primary weapon;
- unlock summary;
- status.

Editor:

```text
General | Visuals | Combat | Effects | Unlock | Shop | Preview
```

General:

- name;
- description;
- role/class;
- rarity;
- enabled;
- sort order.

Visuals:

- thumbnail;
- main image;
- 3D model where supported;
- skins/alternate assets;
- engine glow;
- damage/destroyed visual;
- scale/offsets only when needed.

Existing procedural silhouette/color controls may remain under Advanced fallback, not dominate the normal workflow when authored assets exist.

Combat:

- primary weapon;
- secondary weapon when real;
- supported stat adjustments;
- fire/cooldown/defense/shield values exposed in game language.

Effects:

- engine VFX;
- muzzle VFX;
- projectile trail;
- impact VFX;
- shield VFX;
- low-HP smoke/fire;
- death explosion;
- SFX references.

Preview:

- render ship;
- model rotate if 3D;
- engine effect;
- fire weapon;
- projectile/hit effect;
- damage/death effect.

Duplicate creates a new draft entity/variant with safe ID generation.

## 13.6 Weapons

First-class entity when reuse/runtime ownership justifies it.

Fields may include:

- name;
- description;
- type;
- damage;
- fire rate/cooldown;
- projectile reference;
- muzzle VFX;
- fire SFX;
- hit behavior;
- enabled.

Preview/Test should exercise real canonical transform/behavior where practical.

## 13.7 Projectiles

Fields may include:

- name;
- image/model;
- trail VFX;
- impact VFX;
- impact SFX;
- speed;
- scale;
- lifetime/range where canonical;
- behavior type;
- enabled.

No path text boxes.

## 13.8 Skills / Equipment

Use shared list/detail/media/entity-picker patterns.

Skills:

```text
General | Media | Gameplay Parameters | Effects | Audio | Unlock | Preview
```

Equipment:

```text
General | Visual | Stats | Perks | Economy/Unlock | Preview
```

Use structured perk editing; no serialized config editing.

## 13.9 Enemies / Bosses

Enemies should expose real business/game concepts: visuals, combat, weapon/projectile relationships, effects, audio, rewards, stage usage and behavior profile where configurable.

Bosses:

```text
General | Appearance | Combat | Phases | Abilities | Audio | Rewards | Stages | Preview
```

Boss phase authoring should be visual/structured, never raw JSON.

## 13.10 Worlds / Stages / Routes / Objectives / Challenges

World editor:

```text
General | Stages | Visuals | Music | Rewards | Routes | Unlock | Preview
```

Stage editor:

```text
General | Enemies | Objective | Words/Typing | Visuals | Music | Rewards | Unlock | Preview
```

Use entity selectors for enemies/rewards/media/content pools.

Routes/Objectives/Challenges should be first-class administrator concepts only if they are genuine gameplay domains.

## 13.11 Typing Content

Space Typing Admin should manage browsing/assignment/reference to canonical English Learning Content, not create a second authoring database.

Target tasks:

- search/filter by CEFR/topic/type;
- preview content;
- assign content sets/pools to world/stage;
- inspect validation/reference issues.

## 13.12 Music / SFX / VFX / Models / Images

These become real Media workflows only after A3.0 establishes canonical ownership.

Common features:

- preview;
- searchable metadata/tags;
- usage references;
- upload/replace when supported;
- archive/delete policy;
- assignment through Asset Picker.

## 13.13 Events / Promotions / Discounts / Announcements

Only implement editable Live Ops when real canonical scheduling/consumption exists.

Event target fields may include:

- name;
- status;
- start/end;
- timezone policy;
- media;
- applicable worlds/stages/modes;
- rewards;
- promotions;
- approved feature toggles;
- preview.

Promotion target fields:

- product selection;
- discount type/value;
- badge;
- start/end;
- limit overrides if supported;
- priority/conflict behavior;
- preview.

Validation must catch overlap/conflict/expiry/product availability issues.

Announcements are only implemented if gameplay has a player-facing announcement consumer.

## 13.14 PvP / Duel / Ranked / Modes

Expose safe game-rule controls only where a real authority boundary exists.

Room authority, server/client ownership and unsupported backend diagnostics belong in Developer Tools.

Do not fabricate ranked season management.

## 13.15 Players

Hide normal Players navigation until a real canonical server-side player/account backend exists.

Future support operations require strong permission and audit.

## 13.16 Game Settings

Keep truly global administrator-owned settings only.

Do not turn this page into a dump of runtime constants.

## 13.17 History & Publish

Translate technical revision infrastructure into administrator language:

- Drafts;
- Pending Changes;
- Published Version;
- Compare Changes;
- Publish;
- Roll Back.

Normal compare should be human-readable by entity/domain. Raw JSON diff may exist under Advanced/Developer Tools.

## 13.18 Developer Tools

Developer Tools hosts technical Phase B surfaces:

### Runtime Inspector

- runtime ownership;
- active registry data;
- apply boundaries;
- generated values.

### Contract Inspector

- protocol versions;
- capability manifests;
- parent/child ownership contracts.

### Validation

- raw validation diagnostics;
- canonical IDs;
- schema/version detail.

### Asset Diagnostics

- raw paths;
- missing files;
- generated catalog revisions;
- provenance.

### QA Sandbox / Test Lab

Retain isolated technical preview/test capabilities.

Developer Tools is permission-gated and visually separated from normal administrator workflows.

---

# 14. Search, responsive, accessibility and performance

## Search

Search administrator concepts first:

- entity names;
- categories;
- labels;
- IDs only as secondary/advanced matches.

## Responsive

Primary target remains desktop administration.

- wide desktop: sidebar + multi-column editor;
- laptop: narrower editor;
- tablet: collapsible sidebar, single-column complex forms;
- small mobile: basic review/light edits only; complex previews may be limited.

## Accessibility

Hard requirements:

- keyboard navigation;
- visible focus;
- help accessible without hover;
- real buttons;
- proper input labels;
- focus-trapped dialogs;
- Escape behavior where appropriate;
- color not the only state signal;
- dark-theme contrast;
- accessible table/card/audio names.

## Performance

- lazy-load media/model previews;
- virtualize large lists when needed;
- debounce search;
- cancel/ignore stale async work;
- cache reference catalogs with revision invalidation;
- avoid loading technical manifests on normal screens;
- avoid whole-page rerender per keystroke where unnecessary.

---

# 15. Security and mutation safety

- authenticated endpoints only;
- server-side permission checks;
- filename/path traversal protection;
- MIME/type/extension/size validation;
- CAS/revision conflict checks;
- destructive confirmation;
- actor/timestamp/audit event;
- no arbitrary filesystem path input;
- no arbitrary JSON mutation endpoint for normal admins;
- no secret/token exposure;
- preview must not mutate active runtime;
- publish must activate only validated canonical state.

---

# 16. A0 migration inventory specification

A0 is more than a list of pages. It creates the architecture map used by every later worker.

## 16.1 Required migration matrix

Create/update:

`docs/SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`

Each current route/domain should record at minimum:

```text
Current route
Current UI module
Target V2 route/domain
Administrator task
Current Admin API
Parent service/owner
Child/runtime owner
Persistence/revision owner
Runtime apply boundary
Current write level: none/read-only/draft/publish
Preview capability
Current classification
Target classification
Missing canonical capability
Required prerequisite phase
Developer Tools destination if applicable
Current tests/validators
Validator migration required?
Migration risk
Manual acceptance scenario
Notes/blockers
```

## 16.2 Classification values

- KEEP AS FOUNDATION
- REUSE IN ADMINISTRATOR UI
- MOVE TO DEVELOPER TOOLS
- REMOVE FROM PRIMARY UI
- BUILD NEW DOMAIN CAPABILITY

## 16.3 Capability Gap Register

A0 must also produce a dedicated section/table listing missing capabilities such as:

```text
Capability
Requested admin workflow
Why current runtime cannot support it
Canonical owner needed
Parent/child impact
Persistence model
Preview need
Security/permission impact
Dependency phase
Decision/status
```

This prevents UI workers from improvising shadow models.

## 16.4 Deployment decision

A0 records D1 vs D2 from Section 4.

## 16.5 Branch/integration policy

A0 records the exact parent/child branch strategy from Section 18.

## 16.6 Validator Migration Map

A0 records every validator/assertion that freezes legacy presentation or route structure and separates it from safety-critical canonical invariants.

---

# 17. Validator migration strategy

The current validator must evolve with V2.

## Preserve safety invariants

Do not weaken checks for:

- canonical runtime ownership;
- no legacy mock production routing;
- child/runtime consumption;
- immutable revision/CAS safety;
- no fabricated backend/capability;
- upload/path safety;
- reference integrity.

## Replace brittle presentation assertions

Legacy assertions such as exact Phase B route counts, old labels, old status banners or technical presentation text should be replaced with behavioral V2 invariants.

Examples of V2 invariants:

- primary nav does not render permanent developer descriptions;
- unavailable target routes are not exposed as fake management pages;
- Developer Tools is permission-separated;
- tooltip/help component is accessible;
- raw paths are not normal asset-edit controls;
- write screens use canonical domain APIs;
- preview does not mutate active runtime;
- publish is CAS protected;
- server rejects unauthorized mutation;
- administrator workflows do not require JSON editing.

### Rule

Validator migration is not validator weakening.

---

# 18. Branch and multi-worker integration policy

Past work has shown that domain-specific child branches can become stranded or forgotten.

Admin V2 should minimize branch fragmentation.

## Parent

Primary Admin V2 work continues on:

`feat/space-typing-admin-uiux`

unless current Git state clearly requires another integration strategy.

## Child

Prefer one explicit Admin V2 child integration branch rather than creating a new child branch for every domain.

The current candidate integration branch is:

`feat/admin-world-music-stage-policy`

A0 must confirm whether to continue this branch or supersede it with one clearly documented integration branch.

## Rules

- do not create a new child branch casually;
- every child commit used by Admin V2 must have a documented integration destination;
- migration/progress docs must state which child branch contains canonical work;
- workers must inspect newer commits before changing child ownership;
- no reset/revert of newer worker code;
- no domain branch may be considered complete while its code is unintegrated/stranded unless explicitly marked as such.

---

# 19. Revised implementation roadmap

The original A0–A17 product goals remain, but sequencing is hardened so foundational safety is not implemented after writable domains.

## A0 — Current-state audit + migration inventory

Deliverables:

- `docs/SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`;
- `docs/SPACE_TYPING_ADMIN_V2_PROGRESS.md`;
- Capability Gap Register;
- Validator Migration Map;
- deployment-model decision;
- parent/child integration policy;
- current API/service/owner map.

Exit criteria:

- every existing route has a migration destination;
- every requested write workflow has a known canonical owner or explicit gap;
- no implementation assumption relies only on an old checkpoint.

---

## A0.5 — Cross-cutting architecture gates

This phase is mandatory before the first large writable V2 domain.

Resolve/implement minimum foundation for:

### A0.5.1 Draft/change-set/publish semantics

- whole-config vs domain/change-set model;
- exact publication scope;
- conflict behavior;
- entity editor lifecycle contract.

### A0.5.2 Actor identity

- current actor envelope appropriate to deployment model.

### A0.5.3 Minimal permissions

- permission service;
- server-side mutation/publish checks;
- Developer Tools permission boundary.

### A0.5.4 Minimal audit event infrastructure

- mutation/publish actor/action/entity/scope/revision/timestamp/result.

### A0.5.5 Entity/reference conventions

- immutable internal IDs;
- display identity;
- safe reference pickers;
- archive/disable/delete conventions;
- duplicate/new-ID behavior.

Exit criteria:

A writable domain can be implemented without inventing security, publication or identity semantics locally.

---

## A1 — Admin V2 design system foundation

Build shared:

- Tooltip;
- Info Icon;
- Help Drawer;
- Field wrapper;
- Validation message;
- Page Header;
- Search/Filter primitives;
- Entity table/card;
- Empty/Error/Loading state;
- Drawer/Dialog;
- Draft lifecycle bar;
- common status chips.

Mandatory cleanup:

- stop rendering nav short descriptions by default;
- remove generic permanent technical helper paragraphs where tooltip/help replaces them;
- establish lower-noise spacing/type tokens;
- keep task-critical warnings visible.

Tooltip tests must cover:

- hover;
- focus;
- touch toggle;
- Escape;
- outside click;
- cleanup after screen teardown;
- collision placement;
- keyboard/a11y semantics.

---

## A2 — Shell + capability-aware navigation + Dashboard + Developer Tools scaffold

Tasks:

- implement concise target IA incrementally;
- capability-aware/permission-aware nav;
- do not add dead placeholder routes;
- administrator Dashboard using real data only;
- create Developer Tools scaffold now;
- move technical surfaces into Developer Tools incrementally as V2 replacements appear;
- preserve command palette.

Exit criteria:

Normal administrator navigation is understandable without runtime terminology.

### Important change

A15 is no longer the first Developer Tools migration phase. A2 creates the destination; later phases move technical content continuously.

---

## A3.0 — Media architecture gate

Define/implement the canonical Media model from Section 12.

Exit criteria:

Images/Music/SFX/VFX/Models have documented ownership/reference/replace/archive/version rules appropriate to their capabilities.

---

## A3.1 — Media Library + Asset Picker

Build real supported workflows:

- browse/search/filter;
- preview;
- upload where supported;
- metadata;
- usage references;
- replace;
- safe archive/delete;
- reusable Asset Picker.

Exit criteria:

Later entity editors no longer require administrators to type asset paths.

---

## A4.0 — Shop architecture decision + canonical owner

Resolve Shop model A vs B from Section 13.2.

Implement missing canonical model/service/runtime consumption before enabling normal write UI.

Exit criteria:

There is one real Shop/product source of truth and a tested runtime path.

---

## A4.1 — Economy V2: Shop / Products / Pricing / Promotion foundation

Implement administrator workflows for:

- catalog/list;
- product editor;
- price/sale/badge;
- availability;
- media;
- safe limits;
- draft;
- preview;
- review change scope;
- publish handoff/operation according to A0.5 semantics.

Exit criteria:

Administrator can change a real product’s applicable presentation/price/availability and the published canonical result is what gameplay consumes.

---

## A5 — Ships / Weapons / Projectiles

Implement:

- fleet list/detail;
- authored media/model assignment;
- naming/description/class/rarity where canonical;
- weapon assignment;
- projectile entity/reference;
- VFX/SFX;
- unlock;
- duplicate;
- preview/test;
- safe draft/publish flow.

Exit criteria:

Administrator can replace ship image/model, change name, select weapon/projectile/effects and preview/publish without code/path editing.

---

## A6 — Skills / Equipment

Rebuild with shared V2 patterns and canonical owners.

---

## A7 — Enemies / Bosses

Implement rich entity workflows, relationships, effects, rewards, stage usage and structured boss phases only where runtime can support them canonically.

---

## A8 — Worlds / Stages / Routes / Objectives / Challenges / Typing assignment

Split current technical management into administrator content workflows and integrate Media/Music/Reward/Typing assignment.

---

## A9 — Audio / SFX / VFX management completion

Complete specialized Media workflows after gameplay/world domains exercise them.

---

## A10 — Economy completion

Currencies / Rewards / Drop Tables / Unlock Rules / Warp and related semantics become administrator workflows only where authority is real.

---

## A11 — Live Ops

Events / Promotions / Discounts / Announcements with real scheduling only when canonical runtime/backend owners exist.

---

## A12 — PvP / Modes

Expose safe rule controls; keep authority diagnostics in Developer Tools; do not fabricate ranked backend.

---

## A13 — Full Roles & Permissions UX

Build on A0.5 permission foundation:

- role templates;
- granular overrides where needed;
- dangerous-permission emphasis;
- role-aware nav/editor actions;
- permission audit/testing.

A13 is not allowed to be the first server-side authorization implementation.

---

## A14 — Full Audit Log + human-readable History / Publish UX

Build on the earlier audit event foundation:

- who;
- what entity;
- what changed;
- when;
- draft/publish action;
- previous/new value summaries;
- human-readable compare;
- rollback visibility.

A14 is not allowed to be the first time mutations are attributable.

---

## A15 — Developer Tools migration cleanup

By A15 most technical surfaces should already have moved incrementally.

A15 performs the final cleanup/consolidation:

- Runtime Inspector;
- Contract Inspector;
- Validation;
- Asset Diagnostics;
- QA Sandbox;
- removal of stale duplicate technical surfaces from normal Admin routes.

---

## A16 — UX / accessibility / responsive / performance polish

Full consistency pass:

- remove stale helper paragraphs;
- tooltip consistency;
- empty/loading/error states;
- keyboard navigation;
- responsive layout;
- list scalability;
- async cleanup;
- preview performance;
- visual hierarchy/noise reduction.

---

## A17 — Administrator acceptance testing

Maintain:

`docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

Task-based acceptance should include at least:

1. Change a real product price.
2. Add a discount badge/schedule where supported.
3. Replace a ship image/model.
4. Change ship weapon/projectile/VFX.
5. Upload supported BGM and assign it to a world/stage.
6. Duplicate an entity.
7. Save draft without changing active runtime.
8. Preview canonical changes.
9. Review exactly what will be published.
10. Publish safely.
11. Roll back safely.
12. Confirm restricted role cannot mutate forbidden domains.
13. Confirm restricted role cannot access Developer Tools.
14. Confirm audit attribution for mutation/publish.
15. Complete normal workflows without raw path/JSON/source-code concepts.

---

# 20. Required execution order

The next implementation should follow:

```text
A0
 ↓
A0.5
 ↓
A1
 ↓
A2
 ↓
A3.0
 ↓
A3.1
 ↓
A4.0
 ↓
A4.1
 ↓
A5 → A6 → ... → A17
```

Why:

- A0 prevents incorrect duplication/removal of Phase B foundations.
- A0.5 prevents permissions/audit/publish semantics from being retrofitted after writes exist.
- A1 establishes shared UX primitives.
- A2 fixes global navigation and creates the Developer Tools destination early.
- A3.0 prevents a fake generic Media UI.
- A3.1 enables asset-based workflows without paths.
- A4.0 prevents shadow Shop authoring.
- A4.1/A5 then deliver the high-value administrator workflows requested by the product owner.

---

# 21. Suggested module direction

Exact files are decided after A0, but new V2 work should avoid another set of giant one-off Phase B renderers.

Possible direction:

```text
portal/src/admin/
  v2/
    shell/
    components/
      tooltip.ts
      help-drawer.ts
      field.ts
      entity-table.ts
      entity-picker.ts
      asset-picker.ts
      draft-bar.ts
      dialogs.ts
    domains/
      dashboard/
      media/
      shop/
      ships/
      weapons/
      projectiles/
      skills/
      equipment/
      enemies/
      bosses/
      worlds/
      stages/
      live-ops/
      system/
      developer-tools/
    styles/
      tokens.css
      components.css
      shell.css
      domains.css
```

Do not create a parallel framework blindly. Reuse safe current utilities where they fit, and migrate incrementally.

Backend/domain logic should be grouped by real domain, not generic arbitrary-JSON mutation endpoints.

---

# 22. Automated test strategy

## Preserve existing guarantees

Keep tests for:

- canonical ownership;
- no legacy fake routing;
- real child/runtime consumption;
- CAS/revision safety;
- preview isolation;
- no fabricated unsupported backend.

## Shared component tests

At minimum:

- tooltip lifecycle/accessibility;
- dialogs/focus;
- validation state;
- stale async cancellation;
- route teardown cleanup.

## Writable domain tests

For every writable entity:

- schema validation;
- cross-field validation;
- reference integrity;
- missing asset rejection;
- duplicate ID protection;
- authorization denial/allow;
- audit event creation;
- CAS conflict;
- preview uses canonical transform;
- preview does not mutate live state;
- publish activates expected runtime state;
- rollback behavior;
- publication scope/change summary correctness.

## Media/upload tests

- MIME/extension;
- size;
- unsafe filename;
- traversal;
- duplicate/hash behavior where relevant;
- usage protection;
- replace/version semantics;
- archive/delete policy.

---

# 23. Manual QA policy

Manual testing should not block unrelated implementation units unless a manual result is necessary to prove a dependency for the next unit.

Deferred manual scenarios are recorded in:

`docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

and progress docs.

Fix confirmed defects as they are found, but do not stop the entire roadmap merely because a later manual visual pass is pending.

---

# 24. Definition of Done for a V2 administrator screen

A screen is not done merely because it renders runtime data.

It is done only when all applicable criteria are met:

- administrator task is explicit;
- route is exposed only if capability is real/useful;
- list/search/filter is appropriate for domain size;
- entity can be safely edited when product requirement says it is manageable;
- labels use game/business language;
- raw filesystem paths are not required;
- JSON editing is not required;
- source-code knowledge is not required;
- SHAs/protocol/evidence are not in primary workflow;
- help uses tooltip/info/help drawer rather than permanent clutter;
- validation messages are actionable;
- Draft workflow is clear;
- Preview exists when meaningful;
- administrator can understand publication scope;
- publish is CAS-safe;
- server permissions are enforced;
- audit attribution exists for meaningful mutation;
- runtime consumes the same canonical source;
- automated tests cover critical paths;
- manual acceptance scenario exists.

---

# 25. Explicit anti-patterns forbidden in V2

Do not reintroduce in primary administrator screens:

1. Page title followed by a paragraph explaining runtime architecture.
2. Panel subtitle permanently describing source files/owners.
3. `runtimeBacked`, `source`, `owner`, `protocolVersion` as normal business fields.
4. Asset text boxes requiring `/assets/...` paths.
5. JSON textareas for routine authoring.
6. Child SHA as a normal success metric.
7. Capability-evidence panels in normal workflows.
8. Large warning stacks that only explain technical absence.
9. A read-only developer inspector presented as finished administrator management.
10. Edit buttons writing a shadow config gameplay does not consume.
11. Entity-level `Publish` that silently publishes unrelated changes.
12. Permission checks implemented only in the browser/UI.
13. Audit added only after high-risk write domains already exist.
14. Generic Media upload UI without defined asset/reference/version semantics.
15. Dead target-IA routes exposed as fake management pages.
16. New per-domain child branches without a documented integration destination.
17. Weakening canonical validators merely to satisfy redesigned UI assertions.

---

# 26. Resumability / multi-worker protocol

Every worker must:

1. fetch latest parent branch HEAD;
2. fetch latest child integration branch HEAD;
3. read this Master Plan;
4. read `docs/SPACE_TYPING_ADMIN_UIUX_PROGRESS.md` and `docs/SPACE_TYPING_ADMIN_V2_PROGRESS.md` when present;
5. inspect commits newer than handoff/checkpoint;
6. determine first unfinished V2 phase/unit from current Git state;
7. never reset to a SHA in a prompt/plan;
8. never revert/overwrite newer worker work;
9. make changes idempotent/resumable;
10. after fixing a blocker, continue the first unfinished safe unit;
11. never weaken canonical validators to force green CI;
12. never fabricate missing runtime capabilities;
13. update progress/checkpoint docs after meaningful completion;
14. document any child-domain work and its integration destination;
15. keep PR #49 draft/not-ready unless the user explicitly asks otherwise.

---

# 27. Progress file

Create/update when implementation begins:

`docs/SPACE_TYPING_ADMIN_V2_PROGRESS.md`

Minimum structure:

```text
CURRENT PARENT HEAD
CURRENT CHILD HEAD
CURRENT PHASE / UNIT
COMPLETED UNITS
IN PROGRESS
ARCHITECTURE DECISIONS
CAPABILITY GAPS
BLOCKERS
DEFERRED MANUAL TESTS
LATEST GREEN CI
NEXT EXACT ACTION
```

This Master Plan is the design/product/architecture source of truth. Progress tracks execution state.

---

# 28. Immediate next action

The next implementation worker must begin **A0 — Current-state audit + migration inventory**, not Shop/Ships coding.

First concrete actions:

1. fetch latest parent and child HEADs;
2. audit all current Admin routes/modules/APIs/services/validators;
3. create `docs/SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md` with all fields from Section 16;
4. create/update `docs/SPACE_TYPING_ADMIN_V2_PROGRESS.md`;
5. create Capability Gap Register;
6. create Validator Migration Map;
7. lock deployment model for the current milestone;
8. lock child integration branch policy;
9. execute A0.5 architecture decisions for publish scope, actor, minimal permissions, audit and entity/reference conventions;
10. only then implement A1 Design System Foundation.

The first visible UI change after foundations should be the shared Tooltip/Info Icon/help behavior plus removal of always-visible navigation short descriptions — while preserving task-critical warnings and state messages.

Do not mark PR #49 ready or merge it unless the user explicitly requests that action.

---

# 29. Success metric

Admin V2 succeeds when a non-developer administrator who understands Space Typing can confidently perform normal game operations without needing a developer to explain repository architecture.

Acceptance question for every page:

> “Could an administrator who understands Space Typing but has never seen this repository confidently use this page, understand what their change affects, preview it, and know exactly what will be published?”

If the answer is no, the screen is not finished.
