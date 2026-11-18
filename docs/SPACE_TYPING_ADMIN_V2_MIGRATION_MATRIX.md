# Space Typing Admin V2 — A0 Migration Matrix

> Status: A0 CURRENT-STATE AUDIT / SOURCE OF TRUTH
>
> Parent branch audited: `feat/space-typing-admin-uiux`
>
> Parent HEAD at audit start: `571ccdcd34362548c29bfdc0a3d55bf7861bd3c0`
>
> Child Admin integration branch audited: `feat/admin-world-music-stage-policy`
>
> Child HEAD at audit start: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
>
> Review date: 2026-10-13
>
> Master plan: `docs/SPACE_TYPING_ADMINISTRATOR_ADMIN_V2_MASTER_PLAN.md`

This document is the concrete A0 migration inventory for Administrator-first Admin V2. It does not replace the Master Plan. It translates the Master Plan into an implementation map grounded in the current Phase B code and runtime ownership.

Every later Admin V2 worker must fetch current GitHub HEADs before using this matrix. If newer code changes ownership, persistence, APIs, or routes, update this matrix before implementing against stale assumptions.

---

# 1. A0 executive findings

## 1.1 Current Admin is technically complete Phase B, but not Administrator V2

The current production Admin has 30 explicitly mapped Phase B screens. Phase B correctly established runtime ownership boundaries, authenticated Admin APIs, immutable revision-backed authoring for several domains, compare-and-swap publish/rollback, canonical child preview bridges, and read-only diagnostics for unsupported authoring capabilities.

The problem is product orientation, not lack of engineering value. Current screens often expose source ownership, runtime contracts, persistence boundaries, canonical IDs, apply boundaries and unsupported capability evidence directly to the normal operator.

Admin V2 must preserve the trustworthy ownership/publish foundation and replace the primary presentation with administrator workflows.

## 1.2 Current mutation model is whole-config revision based

Current revision-backed edits clone the active config, mutate a namespace, and write a new immutable revision containing the entire Admin config. Publish then activates that entire revision using compare-and-swap semantics.

Therefore entity-level V2 editors must not imply that `Publish` affects only the currently visible entity unless A0.5 introduces explicit change-set/domain-scoped semantics. Until then, the UI must expose a complete review of the pending revision scope before publish.

## 1.3 Current deployment model is local authoring, not a production multi-admin control plane

Current Admin server binds to `127.0.0.1`, persists to local `.local/admin/space-typing` by default, and authenticates with one Admin token (`local-dev` fallback).

A0 decision for the current V2 implementation track:

> Treat Admin V2 as a **local authenticated authoring/control surface first**. Do not fabricate remote multi-user infrastructure, remote player management, centralized scheduler, or account directory that does not yet exist.

A0.5 must still add an explicit actor/permission/audit envelope suitable for local authoring so writes are attributable and future migration to a remote control plane remains possible.

## 1.4 Media ownership is inconsistent across types

Music already has a concrete writable authored-asset service with upload/delete/catalog rebuild behavior. Images, VFX, models and several other visual surfaces are currently source/code/runtime owned and read-only.

Therefore A3 must remain split:

- A3.0 — Media architecture gate;
- A3.1 — Media Library / Asset Picker implementation.

Do not build one generic writable Media CRUD surface until A3.0 defines canonical ownership per asset type.

## 1.5 Current UI validator freezes Phase B presentation

`validate-space-admin-ui.mjs` correctly protects several critical safety guarantees, but it also freezes exact Phase B route count, route labels, Phase B status strings and current presentation details.

A1/A2 must migrate those assertions instead of weakening validation.

## 1.6 One routing anomaly exists today

The production Phase B router has an internal route:

`/admin/space-typing/worlds-stages`

which renders the stage-focused surface, while the mapped/sidebar route `/admin/space-typing/stages` renders the world-focused surface. `/worlds-stages` is not one of the 30 mapped screens.

V2 must eliminate this ambiguity by defining explicit `Worlds` and `Stages` routes and treating the old helper route as a migration alias/internal transition only, not a new normal navigation item.

---

# 2. Classification legend

| Classification | Meaning |
|---|---|
| KEEP | Preserve as a technical foundation with minimal semantic change. |
| REUSE | Reuse data/service/preview behavior in a new Administrator V2 workflow. |
| MOVE | Move technical presentation to Developer Tools / Advanced diagnostics. |
| REMOVE | Remove from normal administrator presentation; do not remove required backend safety. |
| BUILD NEW | A legitimate operator workflow requires a canonical capability that does not yet exist. |
| SPLIT | Current screen contains multiple concerns that must migrate to separate V2 destinations. |

Write level values:

- `NONE` — no Admin mutation;
- `ASSET` — authored asset mutation outside revision store;
- `REVISION` — immutable whole-config revision mutation;
- `EPHEMERAL` — isolated QA/session-only mutation;
- `FUTURE` — intended workflow requires new canonical ownership first.

---

# 3. Current route migration matrix

| # | Current route | Current screen/domain | Current persistence / boundary | Write | Primary classification | Administrator V2 destination | Developer Tools destination | Missing capability / prerequisite | Planned phase | Risk |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | `/admin/space-typing` | Overview / telemetry | child session runtime + local-profile history; no apply boundary | NONE | SPLIT | Dashboard using real implemented signals only | Runtime Inspector / Telemetry Diagnostics | Real dashboard aggregation must be derived only from implemented sources | A2 | Medium |
| 2 | `/admin/space-typing/analytics` | Analytics / telemetry | child session runtime + local-profile history | NONE | MOVE / REUSE | Optional administrator analytics summary only where operationally useful | Runtime Inspector / Telemetry Diagnostics | No centralized historical analytics backend; do not fabricate one | A2 / later | Medium |
| 3 | `/admin/space-typing/audio` | Audio Defaults | immutable revision store; safe boundary | REVISION | REUSE | System / Game Settings / Audio Defaults | Raw config details in Validation/Runtime Inspector | A0.5 lifecycle/permission/audit foundation | A5/A9-compatible | Low |
| 4 | `/admin/space-typing/music-library` | Music Library | authored asset service; catalog rebuild | ASSET | KEEP / REUSE | Media / Music | Asset Diagnostics / provenance | General Media model must preserve Music-specific canonical service | A3.0 → A3.1 | Medium |
| 5 | `/admin/space-typing/world-music` | World / Stage Music | immutable revision store; next-track/state | REVISION | SPLIT / REUSE | World editor + Stage editor + Media/Music assignment | Raw fallback trace / policy diagnostics | Explicit Worlds/Stages routing + shared Asset Picker | A8/A9 | Medium |
| 6 | `/admin/space-typing/ships` | Ships | immutable revision store; new-session | REVISION | REUSE + BUILD NEW | Gameplay / Ships | Registry metadata / raw canonical IDs | Authored media model, Weapon/Projectile ownership, richer ship canonical model | A5 | High |
| 7 | `/admin/space-typing/equipment` | Equipment | immutable revision store; new-session | REVISION | REUSE + BUILD NEW | Gameplay / Equipment | Registry diagnostics | Structured perks/media/economy references as canonical fields | A6 | Medium |
| 8 | `/admin/space-typing/skills` | Skills | immutable revision store; new-session | REVISION | REUSE + BUILD NEW | Gameplay / Skills | Registry/formula diagnostics | Structured effects/media/audio references where real | A6 | Medium |
| 9 | `/admin/space-typing/enemies` | Enemies | immutable revision store; new-session | REVISION | REUSE + BUILD NEW | Gameplay / Enemies | Registry/admission diagnostics | Richer visual/combat/reward references only through real runtime owners | A7 | High |
| 10 | `/admin/space-typing/bosses` | Bosses | immutable revision store; new-session | REVISION | REUSE + BUILD NEW | Gameplay / Bosses | Registry/phase implementation diagnostics | Canonical phase/ability/media/reward authoring where supported | A7 | High |
| 11 | `/admin/space-typing/stages` | Current World-focused Worlds & Stages route | immutable revision store; new-session | REVISION | SPLIT / REUSE | Content / Worlds and Content / Stages | Raw registry diagnostics | Resolve current `/stages` vs `/worlds-stages` routing anomaly | A8 | High |
| 12 | `/admin/space-typing/typing-content` | Typing Content references | reference manifest; new-session | NONE | REUSE | Content / Typing Content assignment/browse | Reference diagnostics | Keep English Learning Content as source of truth; no duplicate authoring DB | A8 | Low |
| 13 | `/admin/space-typing/shop` | Shop runtime contract | child runtime state; no Admin apply boundary | NONE | MOVE + BUILD NEW | Economy / Shop + Products | Contract Inspector / Shop runtime diagnostics | A4.0 canonical Shop architecture decision mandatory before writes | A4.0 → A4.1 | Critical |
| 14 | `/admin/space-typing/currencies` | Currencies | child runtime state; no Admin apply boundary | NONE | REUSE / MOVE | Economy / Currencies, read-only or writable only where authority exists | Contract/runtime ownership diagnostics | Determine which fields are safe authored data vs code-owned behavior | A10 | High |
| 15 | `/admin/space-typing/rewards` | Rewards & Drops | child runtime policy | NONE | REUSE + BUILD NEW | Economy / Rewards + Drop Tables | Runtime policy diagnostics | Canonical reward/drop-table authoring model and reference integrity | A10 | High |
| 16 | `/admin/space-typing/warp` | Stamina / Warp | child runtime policy | NONE | REUSE / MOVE | Economy / Stamina-Warp only if operator workflow becomes canonical | Runtime policy diagnostics | Canonical authoring boundary currently absent | A10 | Medium |
| 17 | `/admin/space-typing/missions` | Missions | child player progression/session | NONE | SPLIT / MOVE | Content / Objectives / Challenges only for genuine authorable definitions | Runtime progression diagnostics | Separate authorable mission definitions from player-owned progress | A8/A11 | High |
| 18 | `/admin/space-typing/daily-weekly` | Daily / Weekly | browser-local expansion profile; Weekly absent | NONE | MOVE / BUILD NEW | Live Ops challenge scheduling only if canonical scheduler is added | Runtime Inspector / capability diagnostics | Weekly identity/reset/rewards/scheduler do not currently exist | A11 | Critical |
| 19 | `/admin/space-typing/expedition` | Expedition | browser-local resumable run | NONE | MOVE / REUSE | Modes / Expedition only for safe rule definitions if canonical | Runtime Inspector / save-boundary diagnostics | Player run state must remain outside Admin mutation | A12 | High |
| 20 | `/admin/space-typing/events` | Runtime Events | child stage/session runtime | NONE | MOVE + BUILD NEW | Live Ops / Events | Contract Inspector / runtime event diagnostics | Real authored event calendar/scheduler/consumption path | A11 | Critical |
| 21 | `/admin/space-typing/duel` | Duel Settings | child duel room/session runtime | NONE | REUSE / MOVE | PvP / Duel safe game rules only where authority exists | Runtime authority diagnostics | Define safe Admin authority boundary; do not override room ownership blindly | A12 | High |
| 22 | `/admin/space-typing/ranked` | Ranked | child duel server/profile store | NONE | REUSE / MOVE | PvP / Ranked only where real backend authority exists | Runtime/backend capability diagnostics | No fabricated ranked season management | A12 | Critical |
| 23 | `/admin/space-typing/alternative-modes` | Alternative Modes | child alternative-match snapshot / partial absence | NONE | MOVE / BUILD NEW | PvP / Alternative Modes when real definitions exist | Capability diagnostics | Preserve explicit absence until canonical mode owner exists | A12 | High |
| 24 | `/admin/space-typing/backgrounds` | Backgrounds | source-owned compositions/generated kit manifests | NONE | SPLIT / MOVE | Media / Images plus World/Stage Visuals assignments | Asset Diagnostics | A3.0 media ownership/version/reference semantics | A3/A8 | High |
| 25 | `/admin/space-typing/vfx` | VFX | code-owned runtime VFX | NONE | MOVE + BUILD NEW | Media / VFX presets/assets only when canonical definitions exist | Runtime/renderer diagnostics | Authored VFX preset model required before writable UI | A3/A9 | High |
| 26 | `/admin/space-typing/ui-assets` | UI Assets | code-owned runtime UI | NONE | MOVE / REUSE | Media / Images only for assets with real authored ownership | Asset Diagnostics | Determine which UI assets are authorable vs build-time/code-owned | A3 | Medium |
| 27 | `/admin/space-typing/settings` | General Settings | immutable revision store; new-session | REVISION | KEEP / REUSE | System / Game Settings | Raw config/schema diagnostics | A0.5 lifecycle/permission/audit foundation | A2/A13-compatible | Low |
| 28 | `/admin/space-typing/feature-gates` | Feature Gates | child browser-local storage/runtime ownership | NONE in current canonical Admin surface | SPLIT / MOVE | Safe Live Ops feature controls only where server/Admin authority is real | Developer Tools / experimental gates | Must separate operator-safe gates from developer/runtime-only gates | A11/A15 | High |
| 29 | `/admin/space-typing/history` | History & Publish | immutable revision store; CAS publish | REVISION | KEEP / REUSE | System / History & Publish | Raw JSON/revision details in Advanced/Developer Tools | A0.5 publish-scope semantics + human-readable change summary | A14 | High |
| 30 | `/admin/space-typing/qa` | QA Sandbox | isolated child test session/preset | EPHEMERAL | KEEP / MOVE | No normal administrator route by default | Developer Tools / QA Sandbox | Permission boundary; preserve campaign no-write isolation | A2/A15 | Low |

---

# 4. Non-mapped current route anomaly

| Route | Current owner | Problem | V2 treatment |
|---|---|---|---|
| `/admin/space-typing/worlds-stages` | `renderPhaseBStages(...)` | Exists in router but not in 30-screen map/sidebar; naming overlaps `/stages` which currently renders the world-oriented surface | Replace with explicit canonical V2 `Worlds` and `Stages` routes. During migration, old helper route may redirect/alias but must not become an additional normal sidebar item. |

---

# 5. Reusable Phase B foundations inventory

## 5.1 KEEP without weakening

- authenticated `/api/admin/...` boundary;
- local-only host binding for the current deployment phase;
- canonical child/runtime ownership contracts;
- immutable revision files;
- compare-and-swap publish conflict protection;
- rollback eligibility rules;
- strict schema validation;
- preview bridges that invoke the same canonical child/runtime transformation where possible;
- Music authored asset service and canonical catalog rebuild path;
- exact child SHA/runtime ownership guards where they protect real integration;
- QA Sandbox isolation from Campaign/player progression;
- bundled font ownership and focus/reduced-motion accessibility guards;
- no legacy mock production routing.

## 5.2 REUSE through new V2 presentation

- active revision/state retrieval;
- revision list/history data;
- world music preview resolution;
- ship/equipment/skill/enemy/boss/world/stage preview bridges;
- Typing Content canonical catalog/reference lookup;
- Music library catalog/upload/delete capability;
- current canonical registries and IDs as internal references;
- runtime read-only data where useful as business-facing summaries.

## 5.3 MOVE to Developer Tools / Advanced

- protocol versions;
- child SHA evidence;
- source file paths;
- persistence-owner strings;
- apply-boundary implementation descriptions;
- capability manifests;
- raw runtime ownership matrices;
- unsupported-field matrices;
- raw fallback traces;
- raw contract payloads;
- renderer/runtime diagnostics.

## 5.4 REMOVE from normal administrator presentation

- permanent navigation short descriptions;
- permanent architecture paragraphs below page titles;
- panel subtitles whose primary purpose is explaining source ownership;
- `runtimeBacked`, `owner`, `source`, `protocolVersion` rows as normal content;
- raw asset path entry;
- raw JSON authoring for routine tasks;
- multiple notices explaining the same absent capability;
- Phase B milestone badges as product-facing success indicators.

---

# 6. Admin API / service inventory

## 6.1 Current authenticated core endpoints

Current server exposes a single-token authenticated Admin namespace and includes:

- Admin contract retrieval;
- state/history retrieval;
- active runtime config retrieval;
- revision validation;
- revision creation;
- CAS publish;
- rollback;
- Typing Content catalog query;
- Shop capability manifest;
- Currency capability manifest;
- Music library list/upload/delete;
- World Music preview;
- Ships/Equipment/Skills/Enemies/Bosses/Worlds/Stages previews;
- read-only contract endpoints for Events, Duel, Ranked, Alternative Modes, Backgrounds, VFX, UI Assets, QA, Telemetry, Expedition and Daily/Weekly.

## 6.2 Current runtime endpoints

Current server also exposes runtime envelopes for:

- Ships;
- Equipment;
- Skills;
- Enemies;
- Bosses;
- Worlds;
- Stages.

These are reusable integration evidence, not Administrator V2 screen designs.

## 6.3 A0.5 service prerequisites before new writable V2 domains

The current token check is authentication only. Before A4.1/A5 writable V2 domains are considered complete, introduce:

- actor extraction/context;
- permission evaluation;
- server-side authorization for mutation/publish/rollback/destructive actions;
- audit event emission;
- publish-scope/change-summary contract;
- tests proving direct endpoint calls cannot bypass permissions.

---

# 7. Capability Gap Register

| ID | Gap | Current evidence | Why it matters | Required decision/capability | Gate | Severity |
|---|---|---|---|---|---|---|
| CG-001 | Publish scope is whole-config revision | Editors clone active config; revision stores full config | Entity editor `Publish` can be misleading | Lock R1 whole-revision review semantics or implement R2 scoped change sets | A0.5 | Critical |
| CG-002 | No explicit actor identity | Revision create defaults to `local-admin` | Audit cannot reliably answer who changed data | Define local actor envelope and request propagation | A0.5 | High |
| CG-003 | Authentication is one shared token; no authorization model | `authorized()` compares token only | UI hiding alone cannot protect dangerous writes | Permission service + server-side checks | A0.5 | Critical |
| CG-004 | No minimal audit event stream | Revision metadata is coarse and asset mutations are separate | Asset/domain actions need attributable history | Audit event envelope and durable local audit sink | A0.5 | High |
| CG-005 | Deployment target not production multi-user | `127.0.0.1`, local filesystem, `local-dev` fallback | Remote roles/scheduling/player ops would be fake if assumed now | Lock local-authoring phase; design future-compatible interfaces | A0/A0.5 | High |
| CG-006 | Generic Media ownership absent | Music writable; Images/VFX/Models mostly source/code owned | Shop/Ships need visual asset pickers | Define asset identity/version/storage/reference/replace/archive semantics per type | A3.0 | Critical |
| CG-007 | Shop has no canonical Admin write owner | Current Shop is runtime-backed read-only | Product price/badge edits cannot be safely implemented | Choose authored catalog vs merchandising-layer architecture | A4.0 | Critical |
| CG-008 | Ships model does not cover desired authored media/combat relationships | Current overrides focus metadata/stats/procedural visual profile | Product owner expects image/model/weapon/projectile/effects management | Expand canonical child/runtime model deliberately | A5 | Critical |
| CG-009 | Weapons/Projectiles are not yet established first-class Admin domains | No current mapped screens/services | Ship editor depends on reusable combat references | Identify/create canonical owners and preview contracts | A5 | High |
| CG-010 | Live Ops scheduler/event calendar absent | Events screen is runtime read-only | Scheduling promotions/events would otherwise be fake | Build genuine event/schedule owner before authoring UI | A11 | Critical |
| CG-011 | Player management backend absent | Several systems are browser/local-profile owned | Player CRUD/grants would violate ownership | Keep Players hidden until canonical backend/ledger exists | Future | Critical |
| CG-012 | Dashboard has no unified operational summary API | Current Overview is telemetry diagnostics | Dashboard must not fabricate numbers | Compose only real available sources; expand API incrementally | A2 | Medium |
| CG-013 | Phase B validator freezes presentation | Exact route count/labels/status strings asserted | A1/A2 would fail for correct V2 changes | Migrate to behavioral/safety invariants | A0/A1 | High |
| CG-014 | Developer Tools is not yet a first-class V2 shell destination | QA only appears under Developer group; technical data spread across screens | Technical surfaces need a safe home during incremental migration | Create Developer Tools scaffold in A2 | A2 | High |
| CG-015 | `/stages` and `/worlds-stages` semantics are ambiguous | Router contains both, map only one | V2 split could inherit confusing routing | Introduce explicit Worlds and Stages routes/aliases | A2/A8 | Medium |
| CG-016 | Feature gates mix runtime ownership and future Live Ops concepts | Current screen is read-only boundary diagnostics | Operators should not see experimental/runtime-only controls | Classify safe live-ops gates vs developer gates | A11/A15 | High |

---

# 8. Validator Migration Map

## 8.1 Preserve these guarantees

The following current validator intent must remain or become stronger:

- production Admin shell never falls back to legacy mock renderers;
- canonical runtime owners remain the source of truth;
- no synthetic backend/capability is introduced for unsupported domains;
- immutable revision validation remains strict;
- publish retains compare-and-swap conflict protection;
- canonical child/runtime preview bridges remain connected;
- deleted mock modules do not reappear in production routing;
- Admin bundled fonts remain locally owned;
- `:focus-visible` accessibility remains protected;
- reduced-motion behavior remains protected;
- command palette keyboard/focus cleanup remains protected;
- QA Sandbox remains isolated from Campaign/player persistence;
- child/runtime contract tests continue to fail closed when ownership changes.

## 8.2 Replace Phase B presentation locks

The following assertions must be migrated when A1/A2 implement V2. They must not simply be deleted without replacement:

| Current assertion pattern | Why it must change | V2 replacement |
|---|---|---|
| Exactly 30 registered screens | Target navigation is capability-aware and may temporarily expose fewer primary routes | Assert every exposed V2 route has a real capability/owner and every legacy route has an explicit migration/alias destination |
| Exact Phase B labels in sidebar | V2 IA changes labels/groups and splits Worlds/Stages | Assert required administrator concepts are discoverable and no technical-only route leaks into primary nav |
| `PHASE B · RUNTIME INTEGRATED` shell text | Milestone wording is not product functionality | Assert connected/error/service status behavior without freezing milestone text |
| Permanent nav description strings | V2 explicitly removes them | Assert `.st-admin-nav-description`/equivalent permanent helper copy is absent from normal nav and tooltip help is available where required |
| Telemetry phrases such as `RUNTIME-BACKED · READ ONLY` | Technical evidence moves to Developer Tools | Assert telemetry diagnostics remain reachable in Developer Tools while normal Dashboard avoids runtime-contract jargon |
| Current Feature Gates route label/presentation | Safe Live Ops and developer gates will split | Assert authority/permission classification, not one legacy label |
| Current router exact strings | A2/A8 will introduce explicit V2 routes | Assert normalized aliases resolve safely and unknown routes still fail closed |

## 8.3 Add V2 validator coverage

A1/A2 onward should add automated checks for:

- no permanent per-item navigation descriptions in primary sidebar;
- first-class `AdminTooltip` / `AdminInfoIcon` usage and cleanup behavior;
- no browser-native `title` as the sole help mechanism for key controls;
- capability-aware navigation;
- Developer Tools permission gating;
- no raw asset path text fields in migrated Media-dependent screens;
- no raw JSON editors for routine administrator workflows;
- real-data-only Dashboard cards;
- permission checks on server mutation endpoints;
- audit event emission for meaningful writes;
- publish review exposes complete change scope;
- Media references use canonical asset identity;
- Shop write workflow is blocked until A4.0 owner is canonical;
- V2 screen Definition of Done tests per domain.

---

# 9. A0 deployment assumption

## Decision D-A0-DEPLOYMENT-01

For this Admin V2 implementation branch, the current system remains a **local authenticated authoring tool**.

Implications:

- preserve loopback binding unless a separately approved milestone changes deployment;
- preserve local filesystem revision storage for this phase;
- do not add fake remote users/players/scheduler services;
- A0.5 may add local actor identity and role/permission semantics without pretending to be a complete remote IAM platform;
- interfaces should be future-compatible so actor/permission/audit data can later come from a remote identity system.

Any transition to LAN/Internet-accessible Admin is a separate security/deployment milestone and requires explicit threat-model review before changing host binding or trust assumptions.

---

# 10. Child branch / integration policy

## Decision D-A0-BRANCH-01

Use `feat/admin-world-music-stage-policy` as the current child Admin integration branch unless Git state later proves a strong technical reason to replace it.

Rules:

1. Do not create a new child branch for every Admin V2 domain by default.
2. Before changing child code, fetch the latest child integration HEAD.
3. Never reset to the checkpoint SHA in this document.
4. If parallel workers need temporary branches, the handoff must explicitly record which commits are not yet integrated.
5. Parent submodule/pin advances only after child tests and ownership review pass.
6. A child capability is not considered available to Admin V2 until its integration commit is reachable from the tracked integration branch and the parent pin/contract points at the tested state.

This policy is intended to prevent hidden unmerged Admin capability branches from accumulating again.

---

# 11. A0 target route direction

The target information architecture remains the Master Plan destination, but A2 must introduce routes incrementally and capability-aware.

Recommended eventual route families:

```text
/admin/space-typing

/content/worlds
/content/stages
/content/routes
/content/objectives
/content/challenges
/content/typing-content

/gameplay/ships
/gameplay/weapons
/gameplay/projectiles
/gameplay/skills
/gameplay/equipment
/gameplay/enemies
/gameplay/bosses

/economy/shop
/economy/products
/economy/currencies
/economy/rewards
/economy/drop-tables
/economy/unlock-rules

/media/images
/media/models
/media/music
/media/sfx
/media/vfx

/live-ops/events
/live-ops/promotions
/live-ops/discounts
/live-ops/announcements

/modes/duel
/modes/ranked
/modes/alternative

/system/settings
/system/roles
/system/audit
/system/history
/system/developer-tools/...
```

Exact route strings may be adjusted during A2, but route naming must express administrator concepts rather than Phase B implementation history.

Legacy routes should be normalized/aliased during migration instead of breaking bookmarks without reason.

---

# 12. A0 completion checklist

- [x] Latest parent HEAD fetched before audit.
- [x] Latest child integration HEAD fetched before audit.
- [x] Existing Phase B progress source reviewed.
- [x] All 30 mapped Phase B screens classified.
- [x] Non-mapped `/worlds-stages` router anomaly recorded.
- [x] Current API/service ownership inventoried.
- [x] Whole-config revision/publish semantic risk recorded.
- [x] Deployment assumption locked for current V2 phase.
- [x] Capability Gap Register created.
- [x] Validator Migration Map created.
- [x] Child integration branch policy locked.
- [x] Developer Tools migration destinations identified.
- [x] Missing canonical capabilities assigned prerequisite phases.

## A0 exit decision

**A0 is complete enough to begin A0.5.**

The first A0.5 implementation target should be the smallest cross-cutting foundation that does not alter domain behavior:

1. define actor context contract;
2. define permission identifiers and authorization service contract;
3. define audit event envelope/sink;
4. define publish/change-scope contract for current whole-revision model;
5. cover the above with focused tests;
6. only then allow A1/A2 UI work to depend on those contracts.

No Shop or Ships write expansion should begin before these gates are in place.
