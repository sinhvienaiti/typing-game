# Space Typing Administrator Admin V2 — Master Plan

> Status: PLANNING SOURCE OF TRUTH FOR ADMINISTRATOR-FIRST REDESIGN
>
> Scope: `sinhvienaiti/typing-game` + `sinhvienaiti/space-typing`
>
> Parent working branch at plan creation: `feat/space-typing-admin-uiux`
>
> Parent HEAD observed before plan creation: `db53949ad89271e3ad6cd8232fa2331cd962b58f`
>
> Child Admin integration branch observed before plan creation: `feat/admin-world-music-stage-policy`
>
> Child HEAD observed before plan creation: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
>
> IMPORTANT: these SHAs are checkpoints only. Every implementation worker MUST fetch current GitHub HEADs first and use newer Git state as source of truth. Never reset a branch to the SHAs in this document.

---

## 0. Executive decision

The current Space Typing Admin Phase B successfully established many important engineering foundations: authenticated Admin APIs, runtime ownership audits, revision-backed configuration, validation, canonical child integration, publishing/rollback infrastructure, and removal of legacy fake/mock production routing.

However, the current product surface is not yet an administrator-oriented game management product. Too many screens expose runtime contracts, source ownership, canonical IDs, capability evidence, apply boundaries, child SHAs, unsupported runtime fields, and implementation terminology directly in the primary UI.

That approach is valuable for developers, but it is the wrong primary experience for game administrators.

Admin V2 therefore changes the primary product model from:

```text
Admin screen = runtime/config inspector with some editing
```

to:

```text
Admin screen = business/game-management workflow
                ↓
            domain service
                ↓
      validation + canonical model
                ↓
        Space Typing runtime
```

The existing Phase B technical work is NOT discarded. It becomes the foundation beneath V2 and, where appropriate, is surfaced under **Developer Tools / Diagnostics** rather than in administrator-facing workflows.

### Product rule

> If a normal administrator must understand source code, JSON structure, filesystem paths, canonical runtime IDs, child SHAs, runtime evidence, protocol versions, or implementation ownership in order to perform a routine game-management task, the Admin UX is not complete.

This rule is a hard acceptance criterion for Admin V2.

---

# 1. Why Admin V2 is required

## 1.1 Current problem: developer-first presentation

Representative current patterns include:

- Shop presenting runtime contract status, capability evidence, read-only boundaries, runtime source fields, persistence ownership and unsupported authoring states.
- Ships presenting canonical IDs, asset IDs, child registry terminology, override persistence terminology and apply-boundary details as primary content.
- Navigation items carrying long descriptions under almost every label.
- Page headers containing technical explanations that are always visible.
- Panels carrying subtitles that describe architecture instead of helping an administrator finish a task.
- Runtime diagnostics and administrator actions being mixed in the same hierarchy.

This produces a technically correct but operationally noisy product.

## 1.2 Administrator intent is different

An administrator thinks in tasks such as:

- “Change the price of this product.”
- “Add a SALE badge until Sunday.”
- “Replace the Vanguard ship image.”
- “Change its primary weapon and projectile effect.”
- “Disable this boss temporarily.”
- “Schedule a Halloween promotion.”
- “Upload a new BGM and assign it to World G05.”
- “Duplicate this ship and create a new variant.”
- “Preview this change before publishing.”
- “See who changed this value.”

The UI must be organized around these tasks.

---

# 2. Admin V2 product principles

## P01 — Administrator-first language

Use domain language: Product, Price, Ship, Weapon, Boss, Reward, Event, Image, Music, Publish.

Do not use implementation language in primary UI: runtime owner, protocol version, canonical source, child SHA, apply boundary, registry evidence, serialized override, JSON path.

Technical terms belong in Developer Tools or contextual troubleshooting details.

## P02 — Progressive disclosure

Show only information needed for the current task.

- Basic fields are visible.
- Advanced fields live in Advanced sections/drawers.
- Help is hidden behind tooltips/info icons.
- Diagnostics are hidden behind Developer Tools.
- Conditional fields appear only when their controlling option is selected.

## P03 — Tooltip-first help, not permanent short descriptions

The current repeated short descriptions must be removed from primary layouts wherever the label/control is self-explanatory.

Standard:

```text
Price                 ⓘ
[ 2,000              ]
```

Hover/focus/click on `ⓘ`:

```text
PRICE
Base purchase price before promotion discounts.
```

Do not render this text permanently below the field unless it is a validation message, warning, state explanation, or task-critical instruction.

## P04 — Visual management instead of path management

Administrators choose assets from a Media Library / Asset Picker.

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

## P05 — Safe content lifecycle

Routine mutation flow:

```text
Edit → Save Draft → Validate → Preview → Publish
```

A normal edit must not silently mutate production runtime immediately.

## P06 — Preserve one source of truth

Admin V2 must not create a shadow model that diverges from gameplay.

When runtime currently lacks an authorable domain, implementation must establish a real canonical owner/apply boundary before presenting an editable administrator workflow.

## P07 — Lists first, details second

Large domains use list/detail patterns:

- searchable table/grid
- filters
- sorting
- status
- bulk actions where appropriate
- create/duplicate/edit actions
- focused entity editor

Do not place an entire registry worth of forms on one page.

## P08 — Preview whenever the output is visual or experiential

Ships, projectiles, VFX, backgrounds, bosses, music, SFX, shop cards and events should have useful preview/test surfaces.

## P09 — Strong permissions

Developer-only controls and dangerous operations must be separated from normal administrator permissions.

## P10 — Preserve Space Typing visual identity

Admin must feel like part of Space Typing: dark sci-fi command interface, restrained cyan/violet accents, existing Exo 2 / Be Vietnam Pro typography, angular panels and high-contrast states.

The redesign should reduce noise without becoming a generic white SaaS dashboard.

---

# 3. Target users and roles

Admin V2 should be designed around explicit roles even if initial authentication remains simple.

## 3.1 Super Admin

Full access to all administrator domains, publishing, permissions and Developer Tools.

## 3.2 Game Designer

Can manage gameplay content:

- ships
- weapons
- projectiles
- skills
- equipment
- enemies
- bosses
- worlds
- stages
- objectives
- routes

## 3.3 Economy Manager

Can manage:

- shop
- products
- currencies where allowed
- rewards
- drop tables
- pricing
- promotions
- purchase limits

## 3.4 Content Manager

Can manage:

- world/stage presentation
- typing content assignments
- labels/descriptions
- images/media assignments

## 3.5 Live Ops Manager

Can manage:

- events
- promotions
- discounts
- announcements
- schedules
- feature activations that are explicitly live-ops safe

## 3.6 Media Manager

Can upload, replace, tag and manage assets without changing gameplay balance.

## 3.7 Support / Player Operations

Future/conditional role for player lookup, inventory/progress support and safe compensating operations if a real server-side player backend exists.

Do NOT fabricate player-management CRUD if the runtime is still browser/local-profile owned.

## 3.8 Developer

Can access:

- Runtime Inspector
- Contract Inspector
- Validation Diagnostics
- QA Sandbox / Test Lab
- raw technical metadata
- runtime ownership evidence
- protocol/version diagnostics

## 3.9 Viewer

Read-only access to permitted domains.

---

# 4. Target information architecture

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
├── Players             (only when canonical backend exists)
├── Progress            (only when canonical backend exists)
├── Inventory           (only when canonical backend exists)
└── Transactions        (only when canonical ledger exists)

SYSTEM
├── Game Settings
├── Roles & Permissions
├── Audit Log
├── History & Publish
└── Developer Tools
    ├── Runtime Inspector
    ├── Contract Inspector
    ├── Validation
    ├── Diagnostics
    └── QA Sandbox / Test Lab
```

### Navigation rule

Sidebar items should show only icon + concise label in normal state.

Current always-visible per-item descriptions should be removed.

Optional help behavior:

- collapsed sidebar: tooltip on icon hover
- expanded sidebar: label only
- group tooltip/info icon for less obvious groups

---

# 5. Global UI/UX specification

## 5.1 Visual density

Goal: information-dense but calm.

Avoid:

- stacked permanent notices
- repeated explanation paragraphs
- architecture text in page headers
- large technical subtitles under every panel title
- multiple status badges that all say similar things

Prefer:

- concise heading
- optional one-line task context only when necessary
- tooltip/info icon
- compact status chips
- drawers for advanced details
- warnings only when actionable

## 5.2 Standard page header

```text
Ships                                    [ + Create Ship ]
Fleet management                          [ Filter ] [ Search ]
```

The subtitle may be omitted when redundant.

No primary header should contain paragraphs describing runtime architecture.

## 5.3 Standard field

```text
Display Name                         ⓘ
[ Vanguard                           ]
```

Optional states:

- required marker
- invalid state
- warning state
- read-only lock icon

Never place a long helper paragraph beneath every field.

## 5.4 Tooltip component — hard requirement

Create a reusable first-class component, not browser-native `title` only.

Suggested API concept:

```ts
createAdminTooltip({
  title: "Sale price",
  content: "Temporary promotional price. Must be lower than base price.",
  placement: "auto",
});
```

### Visual style

- dark/translucent panel matching Space Typing
- thin cyan/violet border
- subtle glow only
- 8–10px angular corner treatment consistent with current shell
- Exo 2 title, Be Vietnam Pro body
- maximum width approximately 280–340px
- no excessive animation
- small fade + 2–4px scale/translate transition
- very high z-index within admin portal
- must not cover the focused input when an alternate placement exists

### Interaction

Desktop:

- hover info icon
- keyboard focus info icon
- Escape closes persistent/focus tooltip

Touch:

- tap info icon toggles tooltip/popover
- tap outside closes

Accessibility:

- tooltip trigger is a real button when interactive
- `aria-describedby` / appropriate tooltip semantics
- fully keyboard reachable
- not required to hover with a mouse

### Content rule

Normal tooltip length: 1–4 short lines.

For complex topics:

```text
Advanced pricing rule...
Learn more →
```

Open a help drawer rather than a 15-line tooltip.

## 5.5 Inline messages

Inline messages are reserved for state, not generic documentation.

Valid examples:

```text
⚠ Sale price must be lower than base price.
```

```text
✓ Draft validated successfully.
```

```text
⚠ This asset is used by 12 entities.
```

Invalid example:

```text
This field controls how the child runtime resolves ...
```

That belongs in a tooltip or Developer Tools.

## 5.6 Conditional fields

Example:

```text
Unlock Type
[ World Completion ▼ ]

Required World
[ G04 — Frozen Rift ▼ ]
```

Do not show controls for all possible unlock types simultaneously.

## 5.7 List screens

Every large entity domain should implement:

- search
- filters
- sort
- status chips
- pagination or virtualized/scalable list where required
- create
- edit
- duplicate
- archive/disable where appropriate
- bulk actions only where safe

## 5.8 Entity editor

Use tabs/sections for complex entities.

Example Ship editor:

```text
Vanguard
[ General ] [ Visuals ] [ Combat ] [ Effects ] [ Unlock ] [ Preview ]
```

## 5.9 Sticky lifecycle bar

For revision-backed entities:

```text
Unsaved changes
[ Discard ] [ Save Draft ] [ Preview ] [ Publish ]
```

Publishing may remain centralized in History & Publish if required by the existing revision architecture, but the entity editor must provide a clear workflow rather than forcing administrators to understand revision internals.

## 5.10 Empty states

Good empty state:

```text
No promotions yet.
Create a promotion to schedule a discount or featured campaign.
[ + Create Promotion ]
```

Bad empty state:

```text
Canonical runtime does not expose promotional authoring capability.
```

If the capability genuinely does not exist, the administrator-facing state should explain product availability plainly, while technical evidence belongs in Developer Tools.

---

# 6. Shared component/design-system work

Admin V2 should establish reusable components before rewriting every domain.

## A. Shell components

- `AdminSidebar`
- `AdminTopbar`
- `AdminBreadcrumbs`
- `AdminPageHeader`
- `AdminPageActions`
- `AdminCommandPalette`

## B. Data/list components

- `AdminEntityTable`
- `AdminCardGrid`
- `AdminSearchInput`
- `AdminFilterBar`
- `AdminSortMenu`
- `AdminPagination`
- `AdminStatusChip`
- `AdminBulkActionBar`

## C. Form components

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

## D. Help/state components

- `AdminInfoIcon`
- `AdminTooltip`
- `AdminHelpDrawer`
- `AdminValidationMessage`
- `AdminWarningBanner`
- `AdminEmptyState`
- `AdminErrorState`
- `AdminSkeleton`

## E. Media components

- `AdminAssetPicker`
- `AdminAssetCard`
- `AdminImagePreview`
- `AdminAudioPreview`
- `AdminModelPreview`
- `AdminVfxPreview`
- `AdminUploadDropzone`
- `AdminUsageReferences`

## F. Lifecycle components

- `AdminDraftBar`
- `AdminPublishDialog`
- `AdminRevisionBadge`
- `AdminChangeSummary`
- `AdminAuditTimeline`

## G. Dialogs/drawers

- confirmation dialog
- destructive confirmation
- duplicate entity dialog
- asset replacement dialog
- advanced settings drawer
- dependency/usage drawer

### Component acceptance rule

A screen should not create a new one-off form/list pattern if a shared Admin V2 component can satisfy it.

---

# 7. Domain architecture

## 7.1 Required layers

```text
Administrator UI
      ↓
Admin Domain API
      ↓
Admin Domain Service
      ↓
Domain Validation
      ↓
Canonical persisted definition / revision
      ↓
Runtime adapter / generated artifact if required
      ↓
Space Typing runtime consumer
```

## 7.2 Existing Phase B work to preserve

Keep and reuse where compatible:

- authenticated Admin service
- revision model
- compare-and-swap semantics
- validation pipeline
- publish/rollback
- runtime preview bridges
- canonical child registries
- existing asset/catalog builders that are true runtime owners
- CI contract validators

## 7.3 Existing Phase B work to relocate from primary UX

Move to Developer Tools or internal diagnostics:

- child SHA evidence
- runtime source paths
- protocol versions
- runtime ownership strings
- contract field tables
- unsupported field matrices
- raw capability manifests
- persistence-owner diagnostics
- exact apply-boundary implementation text
- raw evidence lists

## 7.4 Missing capability policy

Admin V2 must not fake authoring.

If an administrator requirement is valid but current runtime lacks a canonical authoring model, implementation should:

1. identify existing gameplay behavior;
2. define the canonical domain model;
3. implement the domain owner in child/runtime or parent where architecturally correct;
4. add validation;
5. expose Admin service API;
6. add Admin editor;
7. ensure runtime consumes the exact same canonical source;
8. add CI tests preventing divergence.

---

# 8. Media Library — foundation capability

Media management is a dependency for many administrator workflows and should be implemented early.

## 8.1 Media types

- Images
- 3D Models
- Music
- SFX
- VFX presets/assets

## 8.2 Media list

Each asset card/row should show:

- preview
- display name
- type
- tags/category
- dimensions/duration/model metadata where relevant
- status
- usage count

## 8.3 Asset detail

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

[ Replace File ] [ Download/View Source if allowed ]
```

Do not make the filesystem path the primary identity.

## 8.4 Upload

- drag/drop + file picker
- validate extension/MIME
- validate size/dimensions/duration
- safe generated filename/storage mapping
- duplicate detection where useful
- preview before save
- automatic metadata extraction
- tag/category assignment

## 8.5 Replace

Before replacing:

```text
This asset is currently used by 12 entities.
Replacing it will update those references after publish.
```

## 8.6 Delete

Deletion must be blocked or explicitly handled if references exist.

Use archive/unpublish where physical delete is unsafe.

## 8.7 Asset Picker

Any entity field that references an asset should launch the same reusable picker.

Example:

```text
Ship Image
[ vanguard-main ]
[ Replace ]
```

Picker:

- search
- type filter
- tags
- thumbnail grid
- upload new
- select

---

# 9. Screen-by-screen administrator specification

# 9.1 Dashboard

## Goal

Answer: “What needs my attention right now?”

## Primary content

- published content counts
- draft/unpublished changes
- scheduled events/promotions
- missing/broken asset references
- validation warnings
- recent admin activity
- service health only at a high level

Example:

```text
Live Content
12 Worlds · 184 Stages · 32 Ships · 58 Products

Needs Attention
3 unpublished changes
2 missing asset references
1 promotion awaiting review

Live Ops
Halloween Event        Active
Autumn Sale            Ends in 2 days

Recent Activity
Toan updated Vanguard
Admin published World G05
```

## Do not show by default

- child commit SHA
- raw runtime evidence
- capability manifests
- protocol versions

---

# 9.2 Shop

## Goal

Manage what players can purchase and how it is presented.

## Shop list/catalog

Columns/cards:

- image
- product name
- category
- effective price
- promotion/badge
- availability
- stock/limit summary
- status
- actions

Actions:

- Add Product
- Edit
- Duplicate
- Disable/Enable
- Preview
- Archive where appropriate

Filters:

- category
- currency
- status
- promotion
- availability window

## Product editor tabs

### General

- Display name
- Short label
- Description
- Category
- Status
- Sort order

### Media

- Thumbnail
- Main image
- optional card background
- optional icon

### Pricing

- Currency
- Base price
- Sale price
- Discount percentage derived/displayed where appropriate
- Discount label: SALE / HOT / NEW / LIMITED / custom approved label

### Availability

- Active/inactive
- Start datetime
- End datetime
- purchase limit
- stock model if canonical runtime supports it

### Unlock

- no requirement
- level requirement
- world requirement
- stage requirement
- prerequisite item/achievement only if canonical owner exists

### Preview

Render the actual shop card/presentation as close to gameplay as practical.

## Required architecture change

Current Shop runtime is effectively a deterministic/game-owned runtime contract and is not a complete administrator-authored commerce catalog.

Admin V2 must define whether Shop should become:

A. a canonical authored product catalog consumed by runtime; or
B. an authored merchandising layer over canonical gameplay items with runtime price/stock generators.

This decision must be made explicitly before enabling writes.

Do not simply add form fields that write a second disconnected catalog.

---

# 9.3 Products

Products should be a reusable commerce entity if Shop presentation and item ownership justify separating product definitions from shop placement.

Potential fields:

- product ID (internal/read-only after creation)
- display name
- description
- item type
- referenced gameplay entity
- images
- default price
- tags
- lifecycle status

Use this separation only if it reduces duplication and aligns with runtime.

---

# 9.4 Currencies

Administrator UI should focus on usable economy semantics:

- Display Name
- Icon
- Symbol
- Enabled
- Cap if applicable
- Display formatting
- acquisition/source summary
- spend/sink summary

Advanced/system-only:

- immutable internal ID
- persistence key
- runtime technical owner

If currency behavior is intentionally fixed in code, normal administrators should see it as read-only business data, while developers can inspect technical ownership separately.

---

# 9.5 Rewards & Drop Tables

## Rewards

Editable/admin-manageable where canonical runtime supports:

- reward name/type
- amount/value
- currency/item reference
- source context
- enabled

## Drop Table editor

```text
Drop Table: Elite Sector G04

Reward                Weight/Chance
Credits               55%
Crystal               25%
Equipment Rare        15%
Legendary Fragment     5%
```

Features:

- add row
- entity picker
- probability validation
- normalize/weight mode depending runtime model
- simulation/preview button if deterministic enough

Do not expose raw nested reward JSON.

---

# 9.6 Unlock Rules

Provide reusable conditions instead of duplicating raw unlock fields across every entity.

Possible condition types:

- World completed
- Stage completed
- Player level
- Achievement/mission if canonical
- Currency purchase where appropriate
- Always unlocked

UI should dynamically show fields for the selected rule type.

---

# 9.7 Ships

## Fleet list

Show:

- visual thumbnail/model
- display name
- rarity/class
- primary weapon
- unlock summary
- status
- actions

Do not show raw asset IDs in the default list.

## Ship editor

Tabs:

```text
General | Visuals | Combat | Effects | Unlock | Shop | Preview
```

### General

- Display Name
- Description
- Role/Class
- Rarity
- Enabled
- Sort order

Advanced drawer:

- internal immutable ID
- technical registry metadata

### Visuals

- Thumbnail
- Main ship image
- 3D model if supported
- alternate skin/assets
- engine glow asset/preset
- damage-state visuals
- destroyed-state visual
- display scale
- offsets only when needed

Existing procedural silhouette/colors may remain available under an Advanced procedural fallback section, not as the dominant visual management method when authored assets exist.

### Combat

- Primary Weapon
- Secondary Weapon if runtime supports
- base stat adjustments
- fire rate/modifiers
- defense/shield characteristics

Use game-language labels and units.

### Effects

- engine VFX
- muzzle/fire VFX
- projectile trail
- hit VFX
- shield VFX
- low-HP smoke/fire
- death explosion
- SFX references

### Unlock

- unlock rule
- progression display milestone
- shop availability if relevant

### Preview

Interactive preview/test:

- ship render
- rotate/model preview if 3D
- engine effect
- fire primary weapon
- hit target
- death effect

## Duplicate ship

`Duplicate Vanguard` → creates draft entity/variant with generated internal ID workflow and copied editable fields.

---

# 9.8 Weapons

Weapon should be a first-class entity if multiple ships/enemies can reuse it.

Fields:

- Name
- Description
- Weapon Type
- Damage
- Fire Rate
- Cooldown
- Projectile reference
- Muzzle VFX
- Fire SFX
- Hit behavior
- Enabled

Preview/Test:

- fire weapon in isolated preview scene
- show projectile travel
- show hit VFX/SFX

Internal formulas and engine keys stay in Advanced/Developer Tools.

---

# 9.9 Projectiles

Fields:

- Name
- Image/Model
- Trail VFX
- Impact VFX
- Impact SFX
- Speed
- Scale
- lifetime/range if gameplay owns it
- behavior type if canonical
- enabled

Preview:

`▶ Test Projectile`

The administrator should not type asset paths.

---

# 9.10 Skills

List:

- icon
- name
- category/type
- cooldown
- status

Editor:

- General
- Icon/Media
- Gameplay Parameters
- Effects
- Audio
- Unlock
- Preview

Descriptions of formulas belong in tooltips/help drawers, not always-visible panel subtitles.

---

# 9.11 Equipment

List:

- icon
- name
- slot/type
- rarity
- key bonus
- status

Editor:

- General
- Visual
- Stats
- Perks
- Economy/Unlock
- Preview

Use structured perk editing instead of raw serialized config.

---

# 9.12 Enemies

List:

- image/model
- name
- family/archetype
- difficulty/tier
- worlds/stages usage
- status

Editor:

- General
- Visuals
- Combat
- AI/admission parameters that are genuinely configurable
- Weapons/Projectiles
- Effects
- Audio
- Rewards
- Stage Usage
- Preview

Where AI behavior is code-only, show selected behavior profile as read-only/business-friendly information rather than exposing implementation evidence.

---

# 9.13 Bosses

Boss editor should be substantially richer than current identity-focused overrides.

Tabs:

```text
General | Appearance | Combat | Phases | Abilities | Audio | Rewards | Stages | Preview
```

### General

- name
- title/subtitle
- description
- enabled
- difficulty/tier

### Appearance

- portrait
- battle image/model
- scale
- position offset
- aura/effect preset

### Phases

Visual phase editor:

```text
Phase 1   HP 100% → 70%
Phase 2   HP 70%  → 30%
Phase 3   HP < 30%
```

Each phase can reference abilities/effects and supported parameters.

Do not make administrators author phase JSON.

### Rewards

Entity-based reward picker/drop table.

### Preview

Boss preview scene, animation/effect preview, phase switching.

---

# 9.14 Worlds

World list:

- hero/background thumbnail
- world name
- stage count
- progression status
- publish status

World editor:

```text
General | Stages | Visuals | Music | Rewards | Routes | Unlock | Preview
```

### General

- Display Name
- Description
- Order
- Enabled

### Visuals

- hero/background
- parallax set
- overlay FX
- lighting/theme preset

### Music

- default BGM
- boss BGM
- volume/default mix override only if needed

### Routes

visual route/stage relationship editor rather than raw IDs where feasible.

---

# 9.15 Stages

Stage list under world or global searchable list.

Editor:

```text
General | Enemies | Objective | Words/Typing | Visuals | Music | Rewards | Unlock | Preview
```

### Enemies

Use entity selector / roster editor.

### Objective

Select supported objective type and show only relevant parameters.

### Words/Typing

Reference canonical content sets through searchable selectors.

### Preview

Launch isolated stage preview/test where architecture permits.

---

# 9.16 Routes / Objectives / Challenges

These should become explicit administrator concepts if they are real gameplay domains.

Avoid hiding them inside generic stage configuration when operators need to manage them repeatedly.

Each editor must use domain-specific controls rather than JSON.

---

# 9.17 Typing Content

Primary administrator tasks:

- browse content
- search/filter by CEFR/topic/type
- preview assignments
- assign content pool to stages/worlds
- inspect validation issues

Do not duplicate the English Learning Content source of truth.

If content authoring remains owned by the parent English Learning Content System, Space Typing Admin should manage assignment/reference, not create a second authoring database.

---

# 9.18 Music

Music Library should become an actual media-management screen rather than a runtime evidence page.

List:

- track name
- duration
- category
- usage
- status
- play button

Actions:

- Upload
- Preview/play
- Rename display metadata where safe
- Tag
- Replace file
- Delete only when provenance/usage rules permit

World/stage assignment belongs in World/Stage editors as well as dedicated music assignment management when helpful.

---

# 9.19 SFX

First-class library for:

- weapon shots
- impacts
- UI sounds
- boss sounds
- announcer sounds
- pickups
- explosions

Features:

- audio preview
- tags/categories
- usage references
- replace/upload

---

# 9.20 VFX

Current visual ownership inspection should evolve into manageable presets/assets where runtime can consume authored definitions.

List/grid:

- animated/static preview
- name
- category
- usage count

Editor where canonical:

- asset/preset selection
- intensity
- scale
- duration
- color theme
- particle profile

Avoid exposing renderer internals directly to normal admins.

---

# 9.21 Events

Live Ops Event editor:

- Event name
- status
- start/end
- timezone policy
- banner/media
- applicable worlds/stages/modes
- rewards
- promotions
- feature toggles explicitly approved for Live Ops
- preview

Schedule visualization is required.

If current runtime has no canonical remote event calendar, implementing this screen as editable requires first building the genuine event definition owner. Until then, present a business-friendly unavailable/read-only state and retain technical evidence only in Developer Tools.

---

# 9.22 Promotions / Discounts

Promotion editor:

- Name
- Product selection
- Discount type
- Discount value
- Badge label
- Start/end
- purchase limit overrides if supported
- priority/conflict rules
- preview

Conflict validation:

- overlapping promotions
- invalid sale price
- expired schedule
- product unavailable during promotion

---

# 9.23 Announcements

Only implement if a canonical player-facing announcement surface exists or is explicitly added.

Fields:

- title
- message
- image
- schedule
- target scope
- status

No fake Admin-only data that gameplay never reads.

---

# 9.24 PvP / Duel / Ranked

Administrator-facing screen should show supported game rules with normal labels and controls.

Developer diagnostics about room ownership, server/client authority and absent backend capabilities move to Developer Tools.

Editable settings require a real safe authority boundary.

Ranked season management must not be fabricated if the backend/service does not exist.

---

# 9.25 Players

Do not present fake player management when profile state is local/browser-owned.

When a real server-side player/account backend exists, target features include:

- search player
- view progression
- view inventory
- safe support actions
- transaction/audit history

Any destructive or grant action requires strong permission + audit log.

Until then, hide Players from normal navigation or clearly mark unavailable product capability without technical clutter.

---

# 9.26 Game Settings

Keep truly global administrator settings only.

Examples:

- maintenance mode
- default gameplay settings intended for server/admin ownership
- environment-safe feature availability

Do not turn this page into a dump of all runtime constants.

---

# 9.27 Roles & Permissions

Target permission model:

```text
resource.action
```

Examples:

- `shop.read`
- `shop.write`
- `shop.publish`
- `ships.write`
- `media.upload`
- `events.publish`
- `developer.runtime-inspect`

UI should provide role templates plus granular override if necessary.

Dangerous permissions are visually distinguished.

---

# 9.28 Audit Log

Audit entries should answer:

- who
- what entity
- what changed
- when
- draft/publish action
- previous/new values where appropriate

Example:

```text
13 Oct 01:14
Toan
Vanguard · Price
1,800 → 2,000
```

Technical revision IDs can be accessible in detail, not primary list content.

---

# 9.29 History & Publish

Existing immutable revision infrastructure remains valuable.

V2 should translate it into administrator language:

- Drafts
- Pending Changes
- Published Version
- Compare Changes
- Publish
- Roll Back

Raw JSON diff may remain available under Advanced/Developer detail, while normal compare view should group human-readable entity changes.

---

# 9.30 Developer Tools

This is where much of current Phase B UI logic belongs.

Suggested sections:

## Runtime Inspector

- current runtime ownership
- active registry data
- apply boundaries
- runtime-generated values

## Contract Inspector

- protocol versions
- capability manifests
- server/child ownership contracts

## Validation

- raw validation results
- canonical IDs
- schema/version diagnostics

## Asset Diagnostics

- raw paths
- missing files
- generated catalog revision
- provenance

## QA Sandbox

- existing isolated Test Lab

Developer Tools must be permission-gated and visually separate from normal administrator management.

---

# 10. Draft / Preview / Publish lifecycle

## 10.1 Draft

An administrator can save incomplete but structurally valid work without changing live gameplay.

## 10.2 Validation

Validation should occur:

- while editing for field-level constraints
- on Save Draft for domain constraints
- before Preview/Publish for full canonical validation

## 10.3 Preview

Preview should use the same canonical transformation/runtime adapters that Publish uses wherever possible.

Do not create a separate approximate preview model that can disagree with production.

## 10.4 Publish

Publishing should:

- use compare-and-swap protection
- fail safely if active revision changed
- show conflict/change summary
- record actor/time/message
- activate only validated canonical state

## 10.5 Rollback

Rollback should be clearly labeled and permission-gated.

The UI should show what will change before confirming.

---

# 11. Validation UX

## Field validation

Example:

```text
Sale Price
[ 2200 ]
⚠ Sale price must be lower than base price (2000).
```

## Cross-field validation

Show near related section.

## Cross-entity validation

Example:

```text
Cannot archive Plasma Cannon.
Used by 4 active ships.
[ View usages ]
```

## Publish validation summary

Group issues:

- Errors — block publish
- Warnings — allow with explicit review if safe
- Information — non-blocking

Do not dump raw stack traces in normal UI.

Raw diagnostics can be expanded in Developer Tools.

---

# 12. Search, filters and command palette

The existing command palette can be retained and evolved.

Search should index administrator concepts:

- entity names
- categories
- labels
- IDs as secondary advanced matches

Examples:

```text
Vanguard
Halloween
G04
Plasma Cannon
```

Do not require exact canonical IDs.

---

# 13. Responsive behavior

Primary target remains desktop administration, but layouts must degrade cleanly.

Breakpoints:

- desktop wide: sidebar + multi-column editor
- laptop: sidebar + narrower editor
- tablet: collapsible sidebar, single-column complex forms
- small mobile: basic review/light edits only; previews may be limited

Tooltip must remain usable on touch through click/tap popover behavior.

---

# 14. Accessibility

Hard requirements:

- keyboard navigable
- visible focus state
- tooltip help accessible without hover
- buttons are real buttons
- correct labels for inputs
- dialogs trap focus appropriately
- Escape closes dialogs/tooltips where applicable
- color is not the only status indicator
- reasonable contrast on dark UI
- tables/cards have accessible names
- audio controls have labels

---

# 15. Performance requirements

- avoid loading all media thumbnails at once
- lazy-load image/model previews
- virtualize very large lists if needed
- cancel/ignore stale async loads
- avoid full page rerender on every keystroke when not necessary
- cache reference catalogs carefully with revision invalidation
- debounce search
- avoid fetching technical manifests for screens that do not display them

---

# 16. Security and mutation safety

- authenticated endpoints only
- permission check server-side, never only in UI
- validate all filenames/uploads
- path traversal protection
- content type + extension validation
- size limits
- CAS/revision checks for writes
- destructive operations require confirmation
- audit actor and timestamp
- no arbitrary filesystem paths from administrator input
- no arbitrary JSON injection endpoints for normal admins
- no secret/token exposure in UI

---

# 17. Migration strategy from current Phase B

The migration must be incremental and resumable.

Do not perform a destructive rewrite of all screens at once.

## Migration classification

For every existing screen, classify current functionality into:

### KEEP AS FOUNDATION

- authenticated endpoint
- validated canonical model
- runtime preview
- revision/publish logic

### REUSE IN ADMINISTRATOR UI

- useful domain data
- entity registry
- safe write operation
- preview capability

### MOVE TO DEVELOPER TOOLS

- contract/evidence/source metadata
- SHA/protocol/apply-boundary diagnostics

### REMOVE FROM PRIMARY UI

- permanent explanatory short descriptions
- architecture-heavy subtitles
- redundant notice stacks
- raw paths/IDs when asset/entity pickers can replace them

### BUILD NEW DOMAIN CAPABILITY

Where administrator requirements are legitimate but runtime has no authorable owner.

---

# 18. Current screen migration map

## Overview / Analytics

Current: runtime/session diagnostics.

V2:

- Administrator Dashboard becomes operational/product summary.
- Runtime telemetry detail moves to Developer Tools / Analytics detail where appropriate.

## Audio Defaults

Current technical configuration can be simplified to administrator controls with tooltips.

## Music Library

Keep upload/catalog foundation.

Rebuild presentation as true media library.

## World / Stage Music

Keep canonical assignment/publish foundation.

Integrate music selection into World and Stage editors; retain dedicated assignment view if useful.

## Ships

Keep canonical preview + revision validation.

Rebuild list/detail editor; add Media/Combat/Effects workflows and hide override internals.

## Equipment / Skills

Keep domain validation where valid; rebuild administrator editors.

## Enemies / Bosses

Keep registry integration; expand domain models only through real runtime ownership.

## Worlds & Stages

Keep revision/runtime integration; split administrator workflows for Worlds and Stages.

## Typing Content

Keep canonical content ownership; make assignment/browse UX administrator-friendly.

## Shop

Major redesign and likely domain architecture expansion. Current runtime-contract screen moves to Developer Tools.

## Currencies / Rewards / Warp

Keep real runtime semantics. Present business concepts; technical ownership moves to Developer Tools.

## Missions / Daily / Weekly / Expedition / Events

Separate actual administrator-manageable capabilities from runtime diagnostics. Do not imply authoring where no canonical owner exists.

## Duel / Ranked / Alternative Modes

Same principle: administrator settings only where real authority exists; diagnostics move down.

## Backgrounds / VFX / UI Assets

Consolidate into Media / Visual management patterns with reusable Asset Picker.

## Feature Gates

Normal safe Live Ops gates may remain administrator-facing. Developer/experimental gates belong in Developer Tools.

## History & Publish

Keep foundation, redesign language/presentation.

## QA Sandbox

Move under Developer Tools.

---

# 19. Detailed implementation phases

The phase IDs below become the execution order unless current Git state proves a dependency should be adjusted.

## A0 — Current-state audit and migration inventory

### Tasks

- fetch latest parent and child HEADs
- inspect every registered Admin screen
- classify each piece as KEEP / REUSE / MOVE / REMOVE / BUILD NEW
- inventory existing APIs/domain services/tests
- identify administrator-required capabilities missing from runtime
- produce a machine-readable or Markdown migration matrix

### Deliverable

`docs/SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`

### Exit criteria

Every current screen has an explicit migration destination.

No coding assumptions based on old Phase B checkpoint only.

---

## A1 — Admin V2 design system foundation

### Tasks

Build shared:

- Tooltip
- Info Icon
- Help Drawer
- Field wrapper
- Validation message
- Page header
- Filter/search bar
- Entity table/card
- Empty/error/loading states
- Drawer/dialog primitives
- Draft lifecycle bar

### Mandatory cleanup

- stop rendering navigation short descriptions by default
- remove always-visible technical page descriptions where replaced by tooltip/help
- establish spacing/type tokens for lower-noise UI

### Tooltip acceptance

- mouse hover works
- keyboard focus works
- touch click works
- Escape/outside-click behavior works
- Space Typing style
- accessible semantics

### Tests

- component behavior tests
- keyboard/accessibility checks
- responsive screenshots/manual QA checklist

---

## A2 — Shell, navigation and Dashboard V2

### Tasks

- implement new information architecture
- concise sidebar labels
- role-aware Developer Tools section
- administrator Dashboard
- move technical diagnostics out of Dashboard
- preserve command palette

### Exit criteria

A normal administrator can navigate without seeing runtime terminology in the primary shell.

---

## A3 — Media Library + Asset Picker

### Tasks

- unified media browsing model
- Images
- Music
- SFX
- VFX
- 3D Models where supported
- upload
- replace
- usage references
- safe delete/archive
- reusable asset picker

### Exit criteria

Subsequent entity editors do not require administrators to type asset paths.

---

## A4 — Economy V2: Shop / Products / Pricing / Promotions foundation

### First requirement

Resolve canonical Shop authoring architecture. Current read-only runtime contract cannot simply be decorated with edit buttons.

### Tasks

- define canonical product/merchandising model
- runtime consumption path
- pricing
- availability
- badges/discount labels
- media references
- limits
- drafts
- preview
- publish

### Exit criteria

Administrator can change a real product’s presentation/price/availability and gameplay consumes the published canonical result.

---

## A5 — Gameplay V2: Ships / Weapons / Projectiles

### Tasks

- fleet list/detail
- media assignment
- ship naming/description
- stats
- primary weapon assignment
- projectile entity
- VFX/SFX assignment
- unlock rules
- duplicate
- preview/test

### Exit criteria

Administrator can perform the core workflow requested by product owner: replace ship image/model, change name, choose weapon/projectile/effects, preview, draft and publish without code/path editing.

---

## A6 — Skills / Equipment

Rebuild with shared list/detail/entity-picker/media patterns.

---

## A7 — Enemies / Bosses

Implement rich entity workflows including visuals, combat relationships, effects, rewards, stage usage and boss phases where canonical runtime can support them.

---

## A8 — Worlds / Stages / Routes / Objectives

Split current combined technical management into content workflows.

Integrate media/music/reward/content assignment.

---

## A9 — Audio / SFX / VFX management completion

Consolidate dedicated media workflows and usages after gameplay/world editors exercise them.

---

## A10 — Economy completion: Currencies / Rewards / Drop Tables / Unlock Rules / Warp

Convert remaining economy diagnostics into administrator workflows where safe.

---

## A11 — Live Ops: Events / Promotions / Discounts / Announcements

Build real scheduling only where canonical runtime/backend owners exist or are intentionally added.

---

## A12 — PvP / Modes administrator controls

Separate safe game-rule controls from diagnostics.

Do not fabricate ranked season backend.

---

## A13 — Roles & Permissions

Add role-aware navigation and server-side authorization for mutations.

---

## A14 — Audit Log + human-readable History / Publish

Keep immutable revision safety while adding entity-oriented change summaries.

---

## A15 — Developer Tools migration

Move remaining Phase B technical surfaces into:

- Runtime Inspector
- Contract Inspector
- Validation
- Asset Diagnostics
- QA Sandbox

Normal administrator navigation must no longer expose these details by default.

---

## A16 — UX polish / accessibility / responsive / performance

Full pass:

- remove stale helper paragraphs
- tooltip consistency
- empty/loading/error states
- keyboard navigation
- responsive layouts
- list scalability
- preview performance

---

## A17 — Administrator acceptance testing

Create a manual acceptance file with task-based scenarios.

Examples:

1. Change product price.
2. Add discount badge and schedule.
3. Replace ship image.
4. Change ship weapon/projectile/VFX.
5. Upload BGM and assign it to a world.
6. Duplicate an entity.
7. Save a draft without affecting runtime.
8. Preview changes.
9. Publish.
10. Roll back.
11. Confirm restricted role cannot access Developer Tools.
12. Complete all above without using raw path/JSON/source-code concepts.

---

# 20. First implementation sequence after this plan

The next worker should NOT jump directly into Shop or Ships without foundation work.

Start with:

```text
A0 → A1 → A2 → A3 → A4 → A5 ...
```

Reason:

- A0 prevents duplicating/replacing working Phase B infrastructure incorrectly.
- A1 establishes shared UX patterns, especially tooltip/help behavior required by product owner.
- A2 fixes the developer-first navigation/shell globally.
- A3 provides asset management required by Ships, Shop, Bosses, Worlds and VFX.
- A4 and A5 then build high-value administrator workflows on correct foundations.

---

# 21. Suggested file/module direction

Exact files may change after A0 audit, but target organization should avoid another collection of giant one-off Phase B renderers.

Possible structure:

```text
portal/src/admin/
  v2/
    shell/
    components/
      tooltip.ts
      field.ts
      entity-table.ts
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

This is a direction, not a requirement to create a parallel framework blindly. A0 must determine how best to evolve current modules without dangerous churn.

Backend/domain files should similarly be grouped by real domain instead of adding arbitrary generic JSON mutation endpoints.

---

# 22. CI and automated test strategy

## 22.1 Keep existing critical guarantees

Do not weaken current validators simply to make V2 pass.

Preserve:

- exact runtime ownership where relevant
- no legacy mock production routing
- canonical child/runtime consumption
- immutable revision semantics
- safe publishing
- no synthetic unsupported backend

## 22.2 Add V2 UI contract checks carefully

Tests should protect behavior, not freeze incidental text/CSS too aggressively.

Test important requirements:

- normal nav does not show developer descriptions
- Developer Tools permission separation
- tooltip component exists and is used for help
- Shop uses administrator entity workflow once writable
- asset picker replaces raw path editing
- draft/publish lifecycle is preserved

## 22.3 Domain tests

For each writable entity:

- schema validation
- cross-field validation
- reference integrity
- missing asset rejection
- duplicate ID protection
- CAS conflict
- preview matches canonical transform
- publish activates expected runtime state
- rollback

## 22.4 Upload tests

- MIME/extension
- max size
- unsafe filenames
- path traversal
- duplicates
- usage protection

---

# 23. Manual QA strategy

Each phase should add its scenarios to:

`docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md`

Manual testing should not block unrelated implementation units unless the result is required to establish correctness of the next dependency.

Record deferred manual scenarios and continue safe automated work where possible.

---

# 24. Definition of Done for an Administrator V2 screen

A screen is NOT done because it renders runtime data.

It is done only when all applicable criteria are met:

- administrator task is explicit
- list/search/filter works where needed
- entity can be opened/edited if product requirement says it is manageable
- labels use game/business language
- no raw filesystem path is required
- no JSON editing is required
- no source-code knowledge is required
- no child SHA/protocol evidence is in primary workflow
- help uses tooltip/info/help drawer instead of permanent clutter
- validation messages are actionable
- Draft workflow is clear
- Preview exists where visual/behavioral preview is meaningful
- Publish is safe
- permissions are respected
- audit history is recorded where required
- runtime consumes the same canonical source
- automated tests cover critical paths
- manual acceptance scenario exists

---

# 25. Explicit anti-patterns forbidden in V2

Do NOT reintroduce these patterns in primary administrator screens:

1. Page title followed by a paragraph explaining runtime architecture.
2. Panel title followed by a permanent subtitle describing source files/owners.
3. Rows such as `runtimeBacked`, `source`, `owner`, `protocolVersion` as normal administrator content.
4. Asset text boxes that require `/assets/...` paths.
5. JSON textareas for routine content authoring.
6. Displaying child SHA as a normal success metric.
7. “Capability evidence” panels in primary workflows.
8. Multiple warning/info boxes that merely explain that a feature is technically absent.
9. A read-only developer inspector being presented as if it were a finished administrator management page.
10. Adding edit buttons that write a shadow config not consumed canonically by gameplay.

---

# 26. Resumability / multi-worker protocol

Every implementation worker must follow this sequence:

1. Fetch latest parent branch HEAD.
2. Fetch latest child branch/submodule state relevant to the task.
3. Read this Master Plan.
4. Read latest `docs/SPACE_TYPING_ADMIN_UIUX_PROGRESS.md` and any new Admin V2 progress file.
5. Inspect commits newer than any checkpoint in the handoff.
6. Determine first unfinished Admin V2 phase/unit from Git state.
7. Never reset to a SHA in a prompt/plan.
8. Never revert or overwrite newer work from another worker.
9. Make changes idempotent/resumable.
10. After fixing a blocker, continue the first unfinished safe unit rather than stopping automatically.
11. Do not weaken validators or runtime ownership checks to force CI green.
12. Do not fabricate missing runtime capabilities.
13. Update progress/checkpoint docs after meaningful completion.

---

# 27. Progress file to create when implementation begins

Create:

`docs/SPACE_TYPING_ADMIN_V2_PROGRESS.md`

Minimum structure:

```text
CURRENT HEADS
CURRENT PHASE
COMPLETED UNITS
IN PROGRESS
BLOCKERS
DEFERRED MANUAL TESTS
LATEST GREEN CI
NEXT EXACT ACTION
```

This Master Plan remains the design/product source of truth; Progress tracks execution state.

---

# 28. Product-owner requirements locked by this plan

The following requirements are explicit and must not be lost during implementation:

## Administrator orientation

The primary Admin is for administrators, not developers.

## Shop

Administrators must ultimately be able to manage applicable product data such as:

- product presentation
- price
- discount label/badge
- availability
- media

through a canonical runtime-consumed model.

## Ships

Administrators must ultimately be able to manage applicable ship properties such as:

- image/model
- name
- weapon
- projectile
- effects
- related media

without raw source/path editing.

## UI density

Permanent short descriptions must be reduced substantially.

## Tooltips

Hover/focus/tap help must use styled Space Typing tooltips/info icons.

## Developer information

Technical/runtime details remain available but move under Developer Tools/Advanced surfaces.

---

# 29. Success metric

Admin V2 succeeds when a non-developer administrator can perform normal game operations by recognizing game concepts on screen, without needing a developer to explain the runtime architecture.

A practical acceptance question for every page:

> “Could an administrator who understands Space Typing but has never seen this repository confidently use this page?”

If the answer is no, the screen is not finished.

---

# 30. Immediate next action

The next implementation tab/worker should begin **A0 — Current-state audit and migration inventory**.

Do not begin by cosmetically rewriting all current screens.

The first concrete deliverables are:

1. fetch latest Git state;
2. audit all current Admin routes/modules/APIs;
3. create `docs/SPACE_TYPING_ADMIN_V2_MIGRATION_MATRIX.md`;
4. create `docs/SPACE_TYPING_ADMIN_V2_PROGRESS.md`;
5. identify reusable Phase B foundations;
6. identify technical surfaces to move to Developer Tools;
7. identify first missing canonical domain needed for administrator workflows;
8. then implement **A1 Design System Foundation**, starting with Tooltip/Info Icon and removal of always-visible navigation short descriptions.

Do not mark PR #49 ready or merge it unless the user explicitly requests that action.
