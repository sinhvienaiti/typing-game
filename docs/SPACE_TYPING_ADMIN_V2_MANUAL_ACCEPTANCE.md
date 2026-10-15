# Space Typing Admin V2 — Manual Acceptance

> Task-based acceptance checklist for the Administrator-first Admin V2.
>
> **Policy:** automated evidence may prove architecture/safety invariants, but it does **not** replace visual/browser acceptance. Every A17 browser scenario remains `MANUAL: QUEUED` until a human executes it. A queued manual scenario does not block unrelated implementation work.

---

## Acceptance status legend

- `AUTOMATED: COVERED` — a validator/test protects the relevant invariant.
- `AUTOMATED: PARTIAL` — some safety/ownership behavior is automated; visual/browser behavior still needs manual verification.
- `MANUAL: QUEUED` — ready for human execution; not claimed as passed.
- `MANUAL: BLOCKED` — only for a genuine missing dependency, never simply because nobody has clicked through yet.

---

# Retained foundation acceptance — A1 / A2 / A3.1

These remain part of final acceptance and must be executed before PR #49 is marked Ready.

## A1 — Help, keyboard and shell

- `A1-M01` mouse/focus tooltip lifecycle and collision placement.
- `A1-M02` keyboard focus, Escape and accessible association.
- `A1-M03` click/tap info popover and outside-click close.
- `A1-M04` viewport-edge collision handling without horizontal overflow.
- `A1-M05` route teardown removes stale tooltip/listeners.
- `A1-M06` leaving Admin removes body-level overlays.
- `A1-M07` Help Drawer focus trap, Escape and focus restoration.
- `A1-M08` reduced-motion mode remains fully usable.
- `A1-M09` sidebar stays concise and administrator-first.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A2 — Dashboard, navigation and Developer Tools

- `A2-M01` Dashboard shows real state only.
- `A2-M02` loading/empty/error/retry states.
- `A2-M03` primary navigation excludes diagnostics-only routes.
- `A2-M04` restricted role cannot see/open Developer Tools.
- `A2-M05` Runtime/Contract/Validation/Asset/QA diagnostics are consolidated under Developer Tools.
- `A2-M06` command palette respects permission separation.
- `A2-M07` legacy diagnostic URLs remain canonical and safe when directly opened.
- `A2-M08` responsive shell remains usable at desktop/laptop/narrow widths.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A3.1 — Media Library / Asset Picker

- `A3.1-M01` inventory/search/type filters/archive visibility.
- `A3.1-M02` runtime/project-owned media remains read-only.
- `A3.1-M03` Admin upload creates media without changing gameplay revision.
- `A3.1-M04` replace creates a new immutable version.
- `A3.1-M05` archive/restore preserves historical versions/references.
- `A3.1-M06` usage graph and exact-version visibility.
- `A3.1-M07` Asset Picker returns exact `{asset, version}`.
- `A3.1-M08` picker keyboard/focus/Object-URL teardown.
- `A3.1-M09` responsive Media workflow.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

---

# A17 — Administrator end-to-end acceptance matrix

## A17-M01 — Change a real Shop product price

**Task:** Open Shop, select a canonical offer that exposes an Admin-owned price override, change the price, save a draft, inspect preview/change scope, then publish only if the current runtime owns that write seam.

**Expected:** gameplay consumes the same canonical owner; no disconnected product catalog or shadow price model is created. If the current offer is runtime-owned/read-only, the UI must say so instead of exposing a fake editor.

**Automated evidence:** Shop ownership/capability validators and runtime preview tests.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M02 — Discount badge / schedule only where supported

**Task:** Inspect Promotions/Discounts from Live Ops and Shop Offers.

**Expected:** badge/original-price fields work only when owned by Shop; start/end scheduling remains unavailable while canonical scheduling is absent. No fake calendar service appears.

**Automated evidence:** A11 Live Ops ownership boundary and Events/Shop validators.

Status: `AUTOMATED: COVERED` for fail-closed ownership · `MANUAL: QUEUED` for browser UX.

## A17-M03 — Replace a Ship image/model through Media

**Task:** Pick a Ship, replace an exact supported image/model asset version through Asset Picker, save draft and compare Draft vs Published preview.

**Expected:** no raw path entry; exact immutable `assetVersionId` is pinned; Media current-version movement does not silently change published gameplay.

**Automated evidence:** Media V2 exact-version tests, Ship media resolver/preview validators.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M04 — Change Ship weapon/projectile/VFX context

**Task:** Change only supported Ship projectile/effect relationships and preview Fire/Impact through production runtime.

**Expected:** production `PlayerShotSystem`/effect path is used; unsupported VFX policy remains read-only; no Admin renderer copy exists.

**Automated evidence:** A5/A10 production-preview bridge and VFX coverage validator.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M05 — Ship Draft vs Published production preview

**Task:** Create an unsaved/draft Ship presentation change and toggle preview source between Draft and Published.

**Expected:** same child production renderer is used for both sources; switching source does not mutate active runtime or PlayerSave.

**Automated evidence:** shared ProductionPreviewBridge source semantics/isolation validators.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M06 — Enemy/Boss combat preview

**Task:** Preview representative Enemy and Boss idle/hit/death, plus phase behavior where production supports it.

**Expected:** child production draw/VFX systems render the scenarios. Do not expect fabricated attack/fire scenarios where production has no isolated owner.

**Automated evidence:** Enemy/Boss production preview adapters and A10 coverage validator.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M07 — Skill cast through production runtime

**Task:** Select a Skill and run its supported isolated cast/runtime scenario.

**Expected:** `SkillEngine` owns activation, energy, cooldown/state transitions; Admin does not fabricate combat results.

**Automated evidence:** child `SkillEngine` runtime preview and parent Skill production runtime panel.

Status: `AUTOMATED: COVERED` for state simulation · `MANUAL: QUEUED` for presentation.

## A17-M08 — Equipment representative gameplay context

**Task:** Select Equipment, inspect before/after stats/perks and any supported visible context.

**Expected:** `resolveEquipmentPerks` owns resolved effects; numeric effect value `1` is not accidentally hidden; no fake visual effect is claimed for stat-only equipment.

**Automated evidence:** Equipment resolver runtime preview and correctness fix.

Status: `AUTOMATED: COVERED` for resolution · `MANUAL: QUEUED`.

## A17-M09 — World production environment preview

**Task:** Preview a World using Published and Draft candidate data.

**Expected:** real production background/environment/parallax/lighting composition path is used; preview remains isolated from progression.

**Automated evidence:** World production renderer adapter and A10.5 coverage validator.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M10 — Stage representative production composition

**Task:** Preview a Stage containing its World/background and current objective/enemy/typing context supported by runtime.

**Expected:** the child production Stage composition path is used; unsupported contextual pieces fail soft rather than being mocked.

**Automated evidence:** Stage production renderer adapter and A10.5 coverage validator.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M11 — Upload BGM and assign World/Stage music

**Task:** Upload a supported Admin-managed music asset, rebuild catalog, assign it to a World/Stage context, preview playback/loop, save draft and publish deliberately.

**Expected:** upload alone does not change gameplay; assignment uses canonical World Music policy; production `MusicController` resolves the published catalog/policy.

**Automated evidence:** Media/Music catalog builder, World Music preview bridge and runtime adapter validators.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M12 — Duplicate an entity safely

**Task:** Duplicate a supported entity from its editor.

**Expected:** a new immutable internal ID is generated, references are not silently redirected, result is a draft until explicitly published.

**Automated evidence:** entity/reference conventions where implemented.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M13 — Save Draft without changing active runtime

**Task:** Save a supported edit as Draft and refresh both Admin runtime state and game runtime before publishing.

**Expected:** active revision/generation and gameplay remain unchanged until Publish succeeds.

**Automated evidence:** immutable revision store/runtime envelope tests.

Status: `AUTOMATED: COVERED` · `MANUAL: QUEUED`.

## A17-M14 — Preview changes without mutating progression/wallet/ownership

**Task:** Exercise Ship/Enemy/Boss/World/Stage/VFX previews repeatedly while inspecting active revision and local gameplay progression.

**Expected:** preview candidate injection never writes PlayerSave, wallet, Shop ownership, progression or active revision.

**Automated evidence:** shared production-preview isolation contracts and simulated reward/economy policies.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M15 — Review exact publication scope

**Task:** Open History & Publish for a draft containing changes in one or more domains.

**Expected:** primary compare uses administrator language grouped by domain/entity/field with before → after values; raw paths/revision internals are available only under Advanced.

**Automated evidence:** A14 History validator and whole-config change-scope tests.

Status: `AUTOMATED: COVERED` for structure · `MANUAL: QUEUED`.

## A17-M16 — Publish safely with CAS

**Task:** Validate and publish a fresh draft. Separately create a stale draft by advancing active revision first.

**Expected:** fresh draft publishes; stale draft is rejected and cannot overwrite newer work.

**Automated evidence:** revision CAS/store tests and publish validation flow.

Status: `AUTOMATED: COVERED` · `MANUAL: QUEUED`.

## A17-M17 — Roll back safely

**Task:** Select an eligible published ancestor and roll back; attempt rollback to an ineligible/stale revision.

**Expected:** ancestor rollback succeeds using expected-active CAS; invalid target fails closed; History shows the action clearly.

**Automated evidence:** rollback/CAS tests and A14 History flow.

Status: `AUTOMATED: COVERED` · `MANUAL: QUEUED`.

## A17-M18 — Restricted role cannot mutate forbidden domains

**Task:** Run Admin with a restricted server-side role, attempt Save Draft/Publish/Rollback/Media mutations both from UI and direct API.

**Expected:** prohibited actions are hidden/disabled in UI and rejected server-side; browser headers cannot self-promote the actor.

**Automated evidence:** A13 role templates, effective permission evaluation, denied-mutation audit tests.

Status: `AUTOMATED: COVERED` for server enforcement · `MANUAL: QUEUED`.

## A17-M19 — Restricted role cannot access Developer Tools

**Task:** Run with a role lacking `developer.runtime-inspect`; inspect sidebar, command palette and direct Developer Tools endpoint/route.

**Expected:** navigation/commands fail closed and server endpoint returns permission denial.

**Automated evidence:** permission-gated manifest/navigation and A13 security tests.

Status: `AUTOMATED: COVERED` for permission contract · `MANUAL: QUEUED`.

## A17-M20 — Audit attribution for mutation / publish / rollback

**Task:** Create a draft, publish it, perform an eligible rollback, then open History.

**Expected:** activity identifies actor, action, entity/domain, timestamp and result; denied/error attempts are attributable; human-readable compare remains separate from raw diagnostics.

**Automated evidence:** durable pre-mutation audit tests + A14 History integration validator.

Status: `AUTOMATED: COVERED` · `MANUAL: QUEUED`.

## A17-M21 — Normal workflows require no raw path/JSON/SHA/protocol knowledge

**Task:** Complete representative Shop/Ship/World/Media/History workflows without opening Developer Tools.

**Expected:** normal controls use game/business language, selectors and Asset Picker; raw filesystem paths, JSON textareas, child SHAs and protocol versions are not required.

**Automated evidence:** V2 anti-pattern validators and Developer Tools separation.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M22 — Production preview teardown leaves no orphan resources

**Task:** Repeatedly open/switch/close production previews, enter/exit fullscreen, navigate away mid-load and replay/reset scenarios.

**Expected:** iframe/runtime/audio/RAF/listeners are disposed; no stale async result overwrites a newer selection; focus/status remain usable.

**Automated evidence:** ProductionPreviewBridge stale-generation/teardown logic + A16 preview UX validator.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

## A17-M23 — Live Ops truthfulness

**Task:** Open Events/Promotions/Discounts/Announcements.

**Expected:** Shop-owned merchandising controls link to the real owner; Gameplay Events stay read-only where appropriate; scheduling/announcements remain unavailable when no canonical service exists.

**Automated evidence:** A11 Live Ops control-plane validation.

Status: `AUTOMATED: COVERED` for capability boundary · `MANUAL: QUEUED`.

## A17-M24 — PvP / Ranked / Alternative Modes truthfulness

**Task:** Run Duel Room Scenario, then inspect Ranked and Alternative Modes.

**Expected:** Duel scenario uses production room validator/session simulation; Ranked does not invent season management; Alternative Modes keep Ranked admission fail-closed.

**Automated evidence:** A12 production Duel simulation and Ranked/Alternative Modes validators.

Status: `AUTOMATED: COVERED` for rule/authority boundary · `MANUAL: QUEUED`.

## A17-M25 — Responsive / keyboard / reduced-motion final sweep

**Task:** Repeat representative edit/preview/history/developer workflows at wide desktop, laptop and narrow viewport using mouse, keyboard and reduced-motion preference.

**Expected:** no critical horizontal overflow, visible focus, usable tooltips/dialogs, production preview actions accessible by keyboard, fullscreen exits cleanly.

**Automated evidence:** A1/A16 CSS/component validators.

Status: `AUTOMATED: PARTIAL` · `MANUAL: QUEUED`.

---

# Final acceptance rule

A17 implementation is considered **prepared** when all cases above have a real executable path or an explicit truthful fail-closed expectation and automated safety evidence is wired into CI.

A17 is considered **human accepted** only after the `MANUAL: QUEUED` cases required for release have actually been executed and recorded. Do not convert queued rows to PASS from code inspection alone.
