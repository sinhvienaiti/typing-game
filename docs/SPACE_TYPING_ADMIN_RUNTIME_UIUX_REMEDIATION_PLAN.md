# Space Typing Admin — Runtime + UI/UX Remediation Master Plan

Updated: 2026-10-12

## 1. Purpose

This plan was created after a real manual browser review of the Space Typing Admin screens exposed two classes of problems that automated Phase B validation did not catch:

1. **production-like local Play-mode integration failures**: Admin API requests are misrouted or mishandled, producing HTML-as-JSON errors, HTTP 405 responses, false capability errors, undefined-property crashes and stale loading states;
2. **Admin UI/UX quality gaps**: navigation, scrolling, collapse/toggle behavior, contextual descriptions, status/error treatment, empty states, control feedback, spacing, responsive behavior and terminology are not yet at a production Admin standard.

This document supersedes any earlier statement that Space Typing Admin is technically complete. Existing Phase B ownership decisions remain valid unless a current defect proves otherwise, but the Admin surface is **not accepted** until the runtime defects and UX acceptance criteria below are closed.

The execution model is resumable and idempotent:

- always fetch the latest branch HEAD before editing;
- never reset/revert newer worker/tab work to the SHAs recorded here;
- current Git state wins over this checkpoint;
- fix shared/root causes before duplicating local work across 30 screens;
- after the shared substrate is stable, close screens sequentially in navigation order;
- every completed unit must have focused regression evidence and the branch must return to green Admin CI / Platform CI checkpoints;
- manual visual acceptance remains manual and is never fabricated from source inspection or CI.

## 2. Source of truth / baseline

Parent repository:

- repo: `sinhvienaiti/typing-game`
- working branch: `feat/space-typing-admin-uiux`
- parent HEAD when this plan was authored: `901a23fd693062bfb69cd29d972e891328e21191`
- latest observed commit: `test(admin): align Shop audit evidence with child repin`

Pinned child:

- repo: `sinhvienaiti/space-typing`
- integration branch: `feat/bgv-integration-current`
- parent submodule pin: `27cee3867462f60a58f404109a59b867b2234c16`
- child integration HEAD observed at plan creation: same `27cee3867462f60a58f404109a59b867b2234c16`

Important: the parent is already pinned to the current integration child. The observed capability messages are therefore **not evidence by themselves that the submodule pin is stale**.

## 3. Non-negotiable architecture rules

1. Do not invent a second gameplay/runtime owner merely to make Admin render something.
2. Read-only domains remain read-only when the child has no canonical authoring/apply boundary.
3. Do not add fake capabilities to contracts to silence UI errors.
4. Do not weaken validators/audits to make CI pass.
5. Do not expose synthetic analytics, fake remote scheduling, fake Ranked policy stores, fake cross-player data or fake VFX/background authoring.
6. Parent Admin must consume the child-owned canonical contracts/resolvers that already exist.
7. Pronunciation must not reintroduce BGM/music ducking; this remediation must not regress the current audio ownership decision.
8. `Save Draft` and `Publish` semantics remain revision-backed/CAS-gated where authoring genuinely exists.
9. Human-facing Admin UI must not display raw parser exceptions, JavaScript `TypeError`s, stack-like messages or implementation-only terminology as its primary error explanation.
10. A screen is not “fixed” merely because it no longer throws. It must expose a coherent loading / ready / empty / unsupported / error lifecycle.

---

# 4. Confirmed root causes

## RC-01 — Play-mode Nginx does not proxy Admin API requests — **CONFIRMED / P0**

### Evidence

`play.sh` correctly starts `admin/server.mjs` on `127.0.0.1:3199`, but `infra/nginx/typing-game.local.play.conf` serves the Portal as static files and currently has only:

- static aliases/assets;
- `location / { try_files $uri $uri/ /index.html; }`.

It does **not** proxy `/api/admin/...` to port 3199.

By contrast, development mode works through Vite, and `portal/vite.config.ts` explicitly proxies `/api/admin` to `http://127.0.0.1:3199`.

### Exact symptom mapping

In static Play mode on `typing-game.local`:

- a GET such as `/api/admin/space-typing/telemetry/contract` falls through `try_files` and receives `portal/dist/index.html`;
- direct `response.json()` then throws `Unexpected token '<', "<!doctype "... is not valid JSON`;
- clients using `.json().catch(() => ({}))` silently convert that HTML response to `{}`, then produce false secondary errors such as “Pinned child contract does not expose rewards.read”;
- a POST preview request such as `/api/admin/space-typing/ships/preview` is handled by the static Nginx location instead of `admin/server.mjs`, producing HTTP `405`;
- the real Admin service already has the POST preview routes, so those 405s are routing failures, not missing preview implementations.

### Solution

Add an explicit Play-mode reverse proxy before the static fallback, scoped to the Space Typing Admin service:

`/api/admin/space-typing/` → `http://127.0.0.1:3199`.

Required proxy behavior:

- preserve request method/body;
- set Host and forwarded scheme;
- disable proxy caching;
- avoid any SPA fallback for this path;
- let `admin/server.mjs` own JSON status/error envelopes.

### Regression requirement

`validate-play-mode.mjs` (or a dedicated Play Admin routing validator) must fail if the Play Nginx config can route `/api/admin/space-typing/*` into `index.html`.

This is the first code fix after this plan is committed.

---

## RC-02 — Inconsistent JSON/error handling creates misleading secondary failures — **CONFIRMED / P0**

### Evidence

The Admin code currently uses at least three patterns:

1. direct `response.json()` — produces raw parser exceptions when HTML is returned;
2. `response.json().catch(() => ({}))` — hides invalid response bodies and later reports false contract/capability errors;
3. typed casts with no runtime shape validation — later crashes on properties such as `canonicalTotals.vocabulary`, `filter`, `slice` or `activeRevision`.

Examples observed in source:

- Telemetry calls `response.json()` directly;
- Rewards parses JSON with `.catch(() => ({}))` then reports missing `rewards.read`;
- Typing Content casts the parsed object to `CatalogPayload` and later dereferences nested fields;
- common `SpaceTypingAdminApi.request()` also suppresses parse failures to `{}`.

### Solution

Create/reuse one canonical Admin HTTP reader with these semantics:

- read response body once;
- inspect HTTP status and `Content-Type`;
- require JSON for Admin JSON endpoints;
- on HTML/text response, throw an `AdminApiError` with a stable error code such as `invalid-response-content-type` and a user-safe message;
- preserve method/path/status in diagnostic metadata, not in the main user-facing banner;
- validate minimum payload shape before returning typed data;
- never convert invalid JSON to `{}` and pretend it is a valid domain contract.

Screens may retain domain-specific validation, but all network parsing must use the shared transport/error layer.

### UX copy target

Instead of:

`Unexpected token '<', "<!doctype "... is not valid JSON`

show:

`Admin service is unavailable in the current local runtime. The request did not reach the Space Typing Admin API.`

Provide a secondary technical detail/retry affordance for developers, not raw parser text as the primary message.

---

## RC-03 — False capability errors caused by invalid/missing payloads — **CONFIRMED for main contract; VERIFY dedicated contracts after RC-01**

The exact pinned child main contract at `27cee386...` already contains:

- `rewards.read`
- `warp.read`
- `missions.read`
- `feature-gates.read`

Therefore screenshot messages claiming that the pinned main child “does not expose” those capabilities are false secondary symptoms, not reasons to mutate the child contract.

Dedicated contracts also have domain-specific shapes. For example Events uses singular:

`"capability": "events.read"`

not a general `capabilities[]` list.

### Solution

After RC-01:

1. re-run every contract screen against the real Admin service;
2. verify the current parser matches each canonical child contract shape;
3. fix only genuine parent contract-shape mismatches;
4. never add duplicate capabilities just to satisfy a stale frontend assumption;
5. add validators that assert the parent reads the actual child contract field shape.

---

## RC-04 — Loading/status lifecycle is incomplete — **CONFIRMED / P1**

### Evidence

Several editable screens initialize badges such as `ACTIVE · loading`. Their request `.catch()` changes an inline notice but does not transition the revision badge to an error/unavailable state. The screenshot therefore shows contradictory UI such as:

- red `Admin service unavailable...`
- while the header still says `ACTIVE · loading`.

### Solution

All async screen headers must use a common finite state model:

- `loading`
- `ready`
- `empty`
- `read-only`
- `unsupported`
- `error`
- optionally `saving` / `saved` for authoring screens.

When a request fails:

- remove loading animation/badge;
- mark service/revision status unavailable;
- disable actions that require the failed payload;
- show `Retry`;
- do not leave stale “loading” text indefinitely.

---

## RC-05 — No shared loading/error/empty-state design primitive — **CONFIRMED / P1**

Each Phase B screen currently creates its own `notice`, `panel`, async catch text and empty layout. This causes inconsistent behavior and huge blank canvases when content fails to load.

### Solution

Introduce a small shared Admin UI state layer instead of a risky full rewrite:

- `AdminPageState` / state-banner helper;
- consistent `Loading`, `Ready`, `Empty`, `Unsupported`, `Error` treatments;
- retry action;
- optional details disclosure for technical diagnostics;
- action disabling rules;
- consistent iconography and tone;
- minimum useful error/empty panel so the page never becomes an empty background with one line of red text.

Migration can be incremental screen-by-screen.

---

## RC-06 — Navigation information architecture is under-designed — **CONFIRMED / P1**

### Current issues

- very long sidebar requires excessive scrolling;
- group headings are not collapsible;
- no group toggle/chevron/expanded state;
- no menu tooltip;
- no short description explaining what a screen does;
- cryptic trailing `B` badge is implementation-centric and not useful to an Admin;
- sidebar does not provide a compact/collapsed mode;
- current scroll bar presentation is visually rough;
- brand/status area consumes vertical space while the long navigation competes below it;
- active item can be far from the visible navigation region;
- developer-centric labels (`Phase B`, `runtime-backed`) dominate the shell rather than task-oriented Admin language.

### Solution

Refactor `NAV_GROUPS` into a richer metadata model:

- stable group ID;
- label;
- optional group description;
- item label/path/icon;
- one-line item description;
- optional access mode (`view`, `edit`, `developer`) for UI hints.

Sidebar behavior:

- each group header becomes a button with chevron and `aria-expanded`;
- active route’s group is always expanded;
- user collapse preferences persist locally;
- optional full-sidebar compact toggle collapses to icons while keeping accessible labels/tooltips;
- sticky brand/top; only nav body scrolls;
- styled thin scrollbar with clear hover target;
- keyboard navigation/focus-visible states;
- tooltip/short description on hover/focus;
- remove/replace raw `B` item suffix with useful task status if needed;
- responsive width and text ellipsis with tooltip rather than hidden text.

---

## RC-07 — Developer/internal terminology and copy dominate operator UX — **CONFIRMED / P2**

Examples include repeated `PHASE B · RUNTIME`, `B06.x`, `runtime-backed`, `canonical`, `no fake ...`, and code ownership prose as primary page copy.

These concepts are useful diagnostics, but an Admin first needs:

- what this screen controls/inspects;
- whether it is editable or read-only;
- when changes take effect;
- what key risk or limitation exists.

### Solution

Keep technical ownership information in secondary help/details blocks, while primary headers use operational language.

Every menu item and page header should answer:

1. What can I do here?
2. Is it read-only or editable?
3. When does a change apply?
4. What is intentionally unavailable?

---

## RC-08 — CI validated ownership/source contracts but missed the real Play-mode request path — **CONFIRMED / P0**

Existing validators inspect source files, direct Admin server behavior and contract ownership. They did not catch the missing Nginx reverse proxy in static Play mode.

### Solution

Add integration protection for the deployment path itself:

- Play Nginx config must include Admin API proxy before SPA fallback;
- validator must check the target port and scope;
- Admin CI should run this validator;
- where practical, add a lightweight smoke test that proves a representative GET and POST route are reachable through the intended routing contract;
- retain existing direct server smoke tests.

---

# 5. Cross-screen UI/UX standards

Every screen closed by this plan must satisfy the following shared acceptance rules.

## 5.1 Async lifecycle

- Loading state is visible and bounded.
- Loading state transitions to exactly one stable terminal state.
- Error never leaves `ACTIVE · loading` or equivalent stale text behind.
- Retry is available for recoverable local-service/network errors.
- Buttons dependent on missing state are disabled.

## 5.2 Error presentation

Primary UI must never show raw:

- `Unexpected token '<'`
- JavaScript `TypeError`
- `Cannot read properties of undefined`
- stack-like implementation errors.

Admin-facing text explains the operational problem. A collapsible/details area may retain safe technical diagnostics such as endpoint/status/error code.

## 5.3 Empty / unsupported states

A read-only or unavailable domain must not render as a nearly empty galaxy background. It must include a structured state card explaining:

- what data/feature was expected;
- whether the feature is intentionally unsupported or temporarily unavailable;
- what Admin can still do;
- related navigation if helpful.

## 5.4 Controls

Buttons, toggles, selects, inputs, tabs and segmented controls require:

- default;
- hover;
- focus-visible;
- active/pressed;
- disabled;
- loading/busy where applicable;
- error/invalid where applicable.

Toggle controls must expose `aria-pressed` or native checkbox semantics and a visible text label.

## 5.5 Tooltips/help

- every navigation item receives a concise description;
- icon-only/compact navigation always has accessible tooltip/label;
- ambiguous badges and destructive/publish-sensitive actions receive contextual help;
- tooltips are supplemental, not the only place critical information exists.

## 5.6 Responsive / clipping

Verify at minimum:

- 1365×768 class viewport;
- 1920×1080 class viewport.

Requirements:

- no hidden/truncated critical labels without a discoverable tooltip;
- no horizontal page overflow for normal Admin content;
- sticky bars do not obscure content;
- tables may use controlled horizontal scrolling inside their own container;
- sidebar remains usable with long menu content.

## 5.7 Read-only vs editable visual distinction

Read-only screens should not visually imply an editable draft workflow.

Editable screens must clearly distinguish:

- active published revision;
- local draft state;
- save draft;
- validate;
- publish boundary.

---

# 6. Screen-by-screen defect matrix and solutions

The screen order below is also the implementation order after shared P0/P1 fixes.

## A01 — Overview

Observed: raw `Unexpected token '<' ... not valid JSON` and otherwise empty page.

Root cause:

- RC-01 confirmed: telemetry contract GET receives Portal HTML in Play mode;
- RC-02 confirmed: direct `response.json()` exposes parser text;
- RC-05 causes poor empty/error presentation.

Owner files:

- `portal/src/admin/space-typing-telemetry-phase-b.ts`
- shared Admin API/state helper introduced by this remediation.

Solution:

- route to real Admin service;
- migrate contract fetch to canonical JSON reader;
- structured error state with Retry;
- use operator-first overview copy;
- retain local-profile/no-central-backend constraint as a secondary ownership card;
- add meaningful overview summary cards once real contract data loads; do not fabricate unavailable live metrics.

Exit:

- no parser text;
- contract loads in Play mode;
- status resolves from loading;
- useful content appears;
- failure state is structured and retryable.

## A02 — Analytics

Same transport failure as Overview because it shares Telemetry contract loading.

Additional UX:

- clearly separate persisted local-profile history from unavailable central/cross-player analytics;
- avoid implying live fleet-wide analytics;
- responsive cards/tables.

Exit: same as A01 plus no ambiguous synthetic analytics language.

## A03 — Audio Defaults

Observed: `Cannot read properties of undefined (reading 'activeRevision')`, stale `ACTIVE · loading` badge.

Root cause:

- RC-01/RC-02 likely yields invalid state payload;
- renderer dereferences `payload.state.activeRevision` without a validated envelope;
- RC-04 leaves loading badge stale after failure.

Solution:

- validated Admin state envelope;
- header state transition on success/failure;
- disable Save Draft when active revision unavailable;
- preserve current real child-owned audio fields and read-only runtime mix boundary;
- present pronunciation focus policy in operator language without changing audio semantics.

Exit: real state loads; no undefined crash; draft actions only enabled when revision baseline is valid.

## A04 — Music Library

Observed: HTML-as-JSON parser error.

Root cause: RC-01/RC-02.

Solution:

- canonical transport;
- clear loading/catalog-empty/service-error states;
- upload form field help, validation feedback and progress;
- clarify accepted formats/size and that upload rebuilds canonical catalog;
- after upload/delete, refresh catalog and surface result without raw implementation output.

Exit: catalog loads in Play mode and upload UI is understandable even before a file is selected.

## A05 — World / Stage Music

Observed: `activeRevision` undefined, preview unavailable, stale `ACTIVE · loading`.

Solution:

- validated state + preview responses;
- keep current Global → Galaxy → World → Stage canonical authoring model;
- ensure state/preview errors transition badges/actions correctly;
- explain scope inheritance with concise help/tooltips;
- disable Validate/Save until baseline and canonical preview are available;
- do not change the already-approved resolver semantics.

## A06 — Ships

Observed: POST preview `405`.

Root cause: RC-01 confirmed; server already exposes POST `/ships/preview`.

Solution:

- Play proxy fix should remove 405;
- then verify canonical fleet list and editor load;
- replace generic “Admin unavailable” banner with shared state UX;
- improve selection/override affordance and field descriptions;
- clear apply boundary/new-session semantics.

## A07 — Equipment

Observed: preview `405`.

Same routing class as Ships.

Per-screen follow-up:

- ensure list/filter/editor render after route repair;
- clear immutable fields vs authorable overrides;
- avoid empty two-column shells when preview fails.

## A08 — Skills

Observed: preview `405`.

Same routing class.

Per-screen UX:

- explain category/energy/cooldown/typing condition fields;
- preserve immutable canonical skill identity;
- responsive editor layout.

## A09 — Enemies

Observed: preview `405`, empty filters.

Same routing class.

Per-screen UX:

- label filter selects;
- explain that only supported admission/min-stage boundary is authorable;
- show useful empty/error state.

## A10 — Bosses

Observed: preview `405`.

Same routing class.

Per-screen UX:

- explain name/title-only override boundary;
- show canonical identities when loaded;
- no blank editor shell on error.

## A11 — Worlds & Stages

Observed: Worlds preview `405`; large blank page; some text visually weak/clipped.

Same routing class plus layout quality issue.

Solution:

- restore preview transport;
- make World/Stage relationship obvious;
- clear navigation between World roster and Stage overrides;
- structured table/list and selected-detail states;
- controlled overflow for dense data;
- preserve only verified authoring fields.

## A12 — Typing Content

Observed: `Cannot read properties of undefined (reading 'vocabulary')`.

Root cause:

- RC-01 returns HTML;
- `.json().catch(() => ({}))` masks transport failure;
- typed cast later dereferences `canonicalTotals.vocabulary`.

Solution:

- shared validated transport;
- validate `protocolVersion`, `mode`, `canonicalTotals`, `tabs` and `items` before render;
- useful failure/empty state;
- retain canonical read-only English Learning Content ownership;
- improve tab/filter/table help and overflow behavior.

## A13 — Shop

Observed: `Cannot read properties of undefined (reading 'filter')`.

Likely root cause:

- invalid capability payload due RC-01, followed by unsafe array operations.

Solution:

- canonical transport + manifest validation;
- guard arrays/required fields;
- read-only Shop UI should explain transaction model/currencies/stock instead of showing a blank page on missing data;
- no fake price authoring.

## A14 — Currencies

Observed: `Cannot read properties of undefined (reading 'slice')`.

Likely same invalid payload → unsafe collection operation.

Solution:

- validated capability manifest;
- guard collection rendering;
- show canonical currency caps/sources/sinks read-only;
- no fabricated economy analytics.

## A15 — Rewards & Drops

Observed: `Pinned child contract does not expose rewards.read`.

Confirmed fact: exact pinned child main contract **does include** `rewards.read` and the `rewards` block.

Root cause:

- RC-01 + `.json().catch(() => ({}))` creates a false capability error.

Solution:

- fix proxy and canonical parser;
- report true contract mismatch only when valid JSON was received and semantically validated;
- retain read-only runtime ownership and no synthetic RNG preview.

## A16 — Stamina / Warp

Observed: false `warp.read` missing message.

Confirmed fact: exact pinned main contract contains `warp.read`.

Solution: same transport/capability correction as Rewards, then screen-specific layout/help for current/reserve/refuel policy and persistence boundary.

## A17 — Missions

Observed: false `missions.read` missing message.

Confirmed fact: exact pinned main contract contains `missions.read`.

Solution: same canonical transport correction; then present mission/objective ownership and intentional non-authoring boundaries clearly.

## A18 — Daily / Weekly

Observed: HTML-as-JSON parser error.

Solution:

- route dedicated contract endpoint correctly;
- canonical parser;
- distinguish Daily runtime-backed behavior from any intentionally unavailable Weekly capability using a deliberate `unsupported` state rather than a failure-looking blank page;
- do not invent Weekly scheduler/reward authoring.

## A19 — Expedition

Observed: HTML-as-JSON parser error.

Solution:

- route dedicated Expedition contract;
- safe parser;
- structured browser-owned/read-only state explanation;
- no remote run mutation controls.

## A20 — Events

Observed: `Pinned child Events contract does not expose events.read`.

Exact child dedicated Events contract uses:

`capability: "events.read"`.

Current frontend also expects that singular field, so the screenshot error is consistent with invalid/missing payload rather than a proven schema disagreement.

Solution:

- fix routing first;
- then validate singular `capability` contract shape;
- present “runtime event systems” vs “no calendar service” as intentional capability information, not as an error.

## A21 — Duel Settings

Observed: `duel.read` missing message.

Solution:

- route and validate dedicated Duel contract;
- distinguish room-owner configuration from global Admin authoring;
- no fake global Duel policy store;
- task-oriented read-only explanation.

## A22 — Ranked

Observed: `ranked.read` missing message.

Solution:

- route/validate dedicated Ranked contract;
- preserve fail-closed semantics where no season/Admin authority exists;
- intentional “no season service” is an unsupported capability state, not a red runtime failure.

## A23 — Alternative Modes

Observed: `alternative-modes.read` missing message.

Solution:

- route/validate dedicated contract;
- present runtime-backed modes and unavailable Ranked admission clearly;
- retain fail-closed behavior; no fake Admin authoring.

## A24 — Backgrounds

Observed: `backgrounds.read` missing message and no gallery content.

Solution:

- route dedicated Backgrounds contract;
- ensure real gallery preview appears when contract loads;
- preserve code/art-pipeline ownership and read-only boundary;
- gallery cards need consistent image sizing, lazy-loading/error placeholders and responsive layout.

## A25 — VFX

Observed: `vfx.read` missing message.

Solution:

- route dedicated VFX contract;
- present real VFX ownership/budgets/domains;
- intentional lack of fake profile becomes an informational boundary state, not a broken page.

## A26 — UI Assets

Observed: HTML-as-JSON parser error.

Solution:

- canonical route/parser;
- show production HUD/component ownership information with structured preview/reference cards where real data exists;
- no fake CRUD.

## A27 — General Settings

Observed: `activeRevision` undefined while fields render defaults, plus stale `ACTIVE · loading`.

Risk: showing editable defaults while the authoritative active revision failed to load can mislead the user into believing the values are current.

Solution:

- do not present fallback defaults as authoritative editable values when state request fails;
- differentiate “schema defaults” from “active revision values”;
- disable Save Draft until authoritative baseline loads;
- fully transition header/status state;
- improve toggles, field help and maintenance risk callout.

## A28 — Feature Gates

Observed: false `feature-gates.read` missing message.

Confirmed fact: main contract contains `feature-gates.read`.

Solution:

- route + valid payload parser;
- clearly state current real runtime-owned gate scope;
- no fabricated remote percentage rollout when runtime has no such service;
- remove stale/duplicate legacy Phase B flag authoring paths if current router no longer uses them.

## A29 — History & Publish

Observed: `activeRevision` undefined; revisions area empty; stale loading badge.

Solution:

- validated state envelope;
- header terminal states;
- publish/rollback controls disabled unless a valid revision relation is loaded;
- clear immutable revision history layout;
- explicit validation/publish errors without raw exceptions;
- responsive revision diff/detail area.

## A30 — QA Sandbox

Observed: HTML-as-JSON parser error.

Solution:

- route dedicated QA contract;
- safe parser;
- clearly present isolated Test Lab launch action and no-write campaign guarantee;
- do not create a second QA state owner;
- structured error state with Retry if local Test Lab bridge is unavailable.

---

# 7. Shared shell / navigation remediation

This work is global and should be completed before or alongside A01/A02 so every later screen benefits from it.

## Sidebar

Required:

- collapsible groups with chevrons;
- `aria-expanded` and keyboard operation;
- active group auto-open;
- local persistence of collapsed state;
- compact sidebar toggle if layout remains usable;
- item tooltip and one-line description;
- sticky brand/header area;
- isolated scrollable nav region;
- styled scrollbar and no horizontal sidebar overflow;
- active item automatically remains discoverable;
- eliminate raw trailing `B` suffix unless replaced with meaningful status;
- long labels must not become silently hidden.

## Topbar

Required:

- keep command palette but improve focus/hover treatment;
- replace dominant implementation-only `PHASE B · RUNTIME` copy with user-relevant environment/service status;
- preserve an optional technical diagnostics badge/details area for developers;
- responsive wrapping without hiding the command action.

## Page headers

Standardize:

- eyebrow/domain;
- task title;
- short Admin-oriented description;
- one clear access-mode badge (`Editable`, `Read only`, `Developer/Test`);
- secondary ownership/limitations in help/details;
- no contradictory statuses.

---

# 8. Execution order

## R0 — Repair real Play-mode request path

1. Add `/api/admin/space-typing/` reverse proxy to static Play Nginx config.
2. Add validator coverage so the route can never fall into SPA `index.html` again.
3. Check exact Play startup assumptions (`play.sh` starts fresh Admin service before Nginx switch).
4. Run focused validation, Admin CI, Platform CI.

Expected immediate effect: most HTML-parser, 405 and false missing-capability screenshot errors disappear together.

## R1 — Canonical Admin transport/error layer

1. Refactor `SpaceTypingAdminApi` into the shared safe JSON transport.
2. Migrate direct screen fetchers incrementally.
3. Add transport tests for:
   - valid JSON 2xx;
   - JSON 4xx/5xx;
   - HTML 200/404 fallback;
   - empty response;
   - malformed JSON;
   - authentication error.
4. User-safe error mapper + developer details.

## R2 — Shared page-state UI

Create reusable loading/error/empty/unsupported/retry components and status badge lifecycle.

## R3 — Sidebar/topbar/navigation UX

Implement collapse, descriptions, tooltips, scroll behavior, keyboard focus, responsive shell and terminology cleanup.

## R4 — Sequential screens

Close A01 → A30 in the order documented above. Shared fixes may resolve the runtime failure early, but each screen still requires its own UX/contract/acceptance review before being marked DONE.

## R5 — Final responsive/accessibility pass

- desktop viewport checks;
- keyboard/focus;
- scrolling/overflow;
- sticky bars;
- tooltip accessibility;
- read-only/editable distinction.

## R6 — Final CI + manual acceptance handoff

- focused validators green;
- Space Typing Admin CI green on exact SHA;
- Platform CI green on exact SHA;
- browser manual retest checklist generated from A01–A30;
- user manually verifies visual quality on the actual local Play build.

---

# 9. CI / regression strategy

## Required new coverage

### Play-mode routing guard

CI must assert that static Play mode sends `/api/admin/space-typing/*` to port 3199 and does not let that prefix enter the SPA fallback.

### Transport tests

The shared Admin client must have explicit tests for HTML/malformed bodies. This prevents future raw JSON parser errors from reaching screens.

### Per-screen source validators

Existing `validate-space-admin-*.mjs` files remain valuable, but should additionally verify the new shared state/error conventions where relevant.

### Real server smoke

Keep direct `admin/server.mjs` smoke tests for GET/POST routes. Extend representative checks if gaps are discovered, especially one GET contract route and one POST preview route.

### Build

Portal TypeScript/build must remain green after each cluster.

## Checkpoint policy

A unit is marked DONE only when:

- latest branch HEAD was re-fetched before the change;
- focused tests/validator pass;
- change is committed;
- exact-SHA CI is inspected;
- no newer worker commit was overwritten.

---

# 10. Status tracker

Legend: `TODO`, `IN PROGRESS`, `DONE`, `BLOCKED`, `MANUAL RETEST`.

Shared:

- R0 Play-mode Admin API routing: `TODO`
- R1 canonical transport/error layer: `TODO`
- R2 shared page states: `TODO`
- R3 sidebar/topbar/navigation UX: `TODO`
- R5 responsive/accessibility pass: `TODO`
- R6 final CI/manual handoff: `TODO`

Screens:

- A01 Overview: `TODO`
- A02 Analytics: `TODO`
- A03 Audio Defaults: `TODO`
- A04 Music Library: `TODO`
- A05 World / Stage Music: `TODO`
- A06 Ships: `TODO`
- A07 Equipment: `TODO`
- A08 Skills: `TODO`
- A09 Enemies: `TODO`
- A10 Bosses: `TODO`
- A11 Worlds & Stages: `TODO`
- A12 Typing Content: `TODO`
- A13 Shop: `TODO`
- A14 Currencies: `TODO`
- A15 Rewards & Drops: `TODO`
- A16 Stamina / Warp: `TODO`
- A17 Missions: `TODO`
- A18 Daily / Weekly: `TODO`
- A19 Expedition: `TODO`
- A20 Events: `TODO`
- A21 Duel Settings: `TODO`
- A22 Ranked: `TODO`
- A23 Alternative Modes: `TODO`
- A24 Backgrounds: `TODO`
- A25 VFX: `TODO`
- A26 UI Assets: `TODO`
- A27 General Settings: `TODO`
- A28 Feature Gates: `TODO`
- A29 History & Publish: `TODO`
- A30 QA Sandbox: `TODO`

Every completion update should append the exact commit SHA and CI evidence beside the relevant item rather than rewriting history ambiguously.

---

# 11. Definition of Done

Space Typing Admin remediation is complete only when all of the following are true:

1. Play mode routes every Space Typing Admin API request to the real Admin service.
2. No reviewed screen displays raw JSON parser errors or JavaScript undefined-property errors.
3. No reviewed screen falsely reports a missing child capability because an invalid response was silently converted to `{}`.
4. Preview POST requests no longer receive Nginx/static 405 responses.
5. All 30 screens have stable loading/ready/empty/unsupported/error behavior.
6. Editable screens disable write actions until authoritative revision state is loaded.
7. Read-only screens clearly communicate what is inspectable and why authoring is unavailable.
8. Sidebar groups collapse/expand cleanly, scrolling is usable, menu items have descriptions/tooltips and keyboard focus is visible.
9. Buttons/toggles/tabs/selects expose coherent interaction states.
10. Critical text is not clipped/hidden at supported desktop viewports.
11. Developer-only implementation wording is secondary to Admin task-oriented copy.
12. Existing canonical runtime ownership is preserved; no fake backend or duplicate owner was introduced.
13. Focused validators/tests, Space Typing Admin CI and Platform CI are green on the final exact SHA.
14. The user performs a final browser visual retest of the actual local Play build and any remaining perceptual issues are recorded as explicit follow-up defects rather than silently accepted.

## Immediate next action

The first unfinished technical unit is **R0 — repair Play-mode Admin API routing**, because it is a confirmed shared root cause for a large portion of the manual screenshot failures. After R0 is green, continue directly into R1/R2 and then close A01–A30 sequentially; do not stop merely because the first root cause is fixed.