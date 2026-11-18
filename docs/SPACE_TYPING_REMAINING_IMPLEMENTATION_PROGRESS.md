# Space Typing Remaining Implementation Progress

> Cross-tab source of truth for **remaining engineering work after Admin Phase B**.
>
> This file exists so a new chat/tab/worker can resume from the first unfinished milestone without relying on conversation memory.

## 0. RESUME RULES — MANDATORY

Before changing any code:

1. Fetch the latest parent and child HEADs.
2. If GitHub contains commits newer than any SHA recorded here, read those commits first and use the newest Git state as source of truth.
3. Never reset/revert/overwrite newer work from another worker/tab.
4. Determine what is already complete from the current Git state before doing any work.
5. Do not redo a completed milestone.
6. Every implementation step must be resumable and idempotent.
7. Do not weaken validators, dedupe rules, audits, tests, runtime ownership checks, or persistence guarantees just to make CI pass.
8. After fixing one blocker, continue to the next unfinished unit instead of stopping at the first green fix.
9. Keep runtime ownership explicit. Do not fabricate fake Admin/runtime capabilities where no canonical child owner exists.
10. Do not mark a PR Ready and do not merge unless the user explicitly asks.
11. Update this file after each completed milestone/checkpoint with:
    - current HEAD(s)
    - completed scope
    - remaining first-unfinished scope
    - tests/CI status
    - blockers
    - exact next action

## 1. CURRENT VERIFIED BASELINES

### Parent repo

- Repo: `sinhvienaiti/typing-game`
- Admin branch: `feat/space-typing-admin-uiux`
- Current HEAD at time this handoff was created: `c608e94d33206a54a787bdb864ad58028b714041`
- PR #49: OPEN / DRAFT
- Phase B state: `PHASE_B_COMPLETE_CANONICAL_CLEANUP_GREEN`
- Latest current parent CI checkpoint seen before this file: Platform CI #1577 PASS on `c608e94d33206a54a787bdb864ad58028b714041`.

### Admin child branch

- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/admin-world-music-stage-policy`
- Validated HEAD: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
- Child CI #1759: PASS.

### Gameplay / expansion child branch

- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/bgv-integration-current`
- HEAD at time this handoff was created: `fa63c79bde068d2de07b67402158c93462adecd1`
- Tree at that commit: `c6f6b114bbb66ee413dca809da604cffd0962191`
- Latest commit message: `fix: harden offline voice runtime and warp charge UI`

**Important:** These SHAs are checkpoints, not reset targets. Always fetch latest Git state first.

## 2. CLOSED SCOPE — DO NOT REDO

### Admin Phase B

`docs/SPACE_TYPING_ADMIN_UIUX_PROGRESS.md` is the detailed source of truth.

All 30 registered Admin Phase B screens are closed with canonical runtime ownership, explicit read-only/absence boundaries, or revision-backed authoring where supported. Legacy production mock fallbacks were removed and CI is green.

Do not reopen Phase B merely because some product capability is absent. If the runtime capability itself does not exist, that is a **new product/runtime milestone**, not unfinished Admin Phase B.

### Boss Depth View / Reward Cards

Previously reviewed gameplay work indicates Boss Depth View and ARAM-style Reward Cards are already implemented enough that they are not the current first-unfinished scope. Re-audit current Git before touching them; do not recreate them from plan text alone.

### Warp Charge / Stamina foundation

Core Warp Charge/Stamina work has already been implemented in the gameplay branch. Future work may extend balancing/admin/runtime behavior, but do not recreate the base system.

## 3. ORDERED REMAINING IMPLEMENTATION ROADMAP

The order below is the default engineering priority unless newer Git/docs prove a milestone is already complete or the user explicitly changes priorities.

---

# R01 — Campaign Map & Rest Stop completion

**Status:** CURRENT / FIRST UNFINISHED ENGINEERING SCOPE

**Primary child:** `sinhvienaiti/space-typing`

**Expected working branch:** `feat/bgv-integration-current`, unless a newer dedicated branch has superseded it.

## R01.1 Audit existing ownership before edits

Before implementing:

- locate the canonical route/campaign state owner;
- locate existing Hidden Content registry;
- locate `discoveredHiddenShop` / related discovery state if still present;
- locate persistence normalization/sanitization;
- locate stage-complete / route-map lifecycle trigger;
- locate deterministic seed/RNG helpers already used by campaign content;
- inspect existing drought/pity and `lastRollStage` behavior;
- identify current tests covering hidden-content discovery.

Do **not** create a parallel route-state, RNG, storage key, or persistence subsystem.

## R01.2 Hidden Shop deterministic auto-discovery

Goal: make rare Hidden Shop discovery deterministic and replay/resume safe.

Requirements:

- replace direct nondeterministic `Math.random` use in canonical campaign discovery path with the existing deterministic seeded RNG abstraction;
- seed must derive only from stable campaign/run identity + discovery roll identity, not wall-clock time;
- same saved run/state + same stage must produce the same discovery result;
- repeated renders/resume calls for the same stage must not reroll;
- retain existing drought/pity semantics unless the current design/docs explicitly supersede them;
- discovery must persist through the existing save/profile lifecycle;
- invalid/legacy saved values must be sanitized safely;
- no duplicate discovery rewards/events after reload.

Acceptance tests should prove:

- deterministic same-seed result;
- different seed identity can produce different result;
- same stage cannot roll twice;
- persistence survives save/load;
- pity/drought increments/resets correctly;
- legacy save migration/sanitization is safe.

## R01.3 Hidden Station deterministic auto-discovery

Goal: add a canonical rare Hidden Station encounter using the same discovery system instead of a second subsystem.

Requirements:

- add Hidden Station to the canonical hidden-content/discovery registry;
- define explicit availability predicates and rarity/weight/pity behavior;
- use the same deterministic RNG path as Hidden Shop;
- persist discovery state in the same normalized save lifecycle;
- ensure Hidden Shop and Hidden Station cannot create invalid duplicate/conflicting route nodes;
- ensure stage replay/reload is idempotent;
- expose a stable discovery result the route map can render without rerolling.

Tests must cover:

- registry validity;
- deterministic station discovery;
- mutual/exclusive behavior if applicable;
- no duplicate node injection;
- persistence/resume;
- legacy save compatibility.

## R01.4 Route-map integration

After runtime discovery logic is green:

- render discovered Hidden Shop/Station as explicit secret route nodes;
- do not reveal undiscovered nodes prematurely;
- preserve keyboard/controller/navigation behavior;
- ensure route selection writes through the canonical campaign owner;
- no visual re-render may trigger a new discovery roll;
- test route-map state restoration after reload/resume.

## R01.5 Rest Stop / secret-node UX completion

Only after runtime/state tests pass:

- complete the Rest Stop/detail panel for discovered secret locations;
- provide concise explanation/help text;
- clearly distinguish normal Rest Stop, Hidden Shop, and Hidden Station;
- preserve existing visual hierarchy and combat/campaign performance constraints;
- avoid modal flows that can double-apply rewards/actions after reload.

## R01 exit criteria

R01 is DONE only when:

- runtime discovery is deterministic;
- persistence is idempotent and migration-safe;
- Hidden Shop + Hidden Station both use one canonical discovery owner;
- route map consumes persisted discovery results without rerolling;
- relevant unit/integration tests pass;
- child build passes;
- child CI passes;
- this progress file is updated with exact commit/CI checkpoint.

---

# R02 — Weekly runtime implementation

**Status:** PENDING AFTER R01

Current Admin behavior correctly reports Weekly as unavailable. Do not change Admin to pretend Weekly exists before canonical runtime exists.

Implement the child runtime first.

## R02.1 Canonical weekly identity

Define:

- UTC week key;
- deterministic weekly challenge ID;
- deterministic seed;
- explicit reset boundary;
- versioned ruleset identity.

The identity must remain stable across reload, timezone changes and client restart.

## R02.2 Weekly run lifecycle

Implement:

- start/resume/complete lifecycle;
- deterministic challenge generation;
- one canonical writer owner;
- safe persisted state;
- reset handling when week changes;
- abandoned/old-week run handling;
- replay protection where rewards are involved.

## R02.3 Rewards and personal results

Implement at minimum:

- reward eligibility;
- once-per-week settlement protection;
- Personal Best;
- optional Personal Ghost only if it fits existing Daily architecture cleanly;
- history/version fields needed for future migration.

Do not fabricate remote leaderboard/backend unless a real backend scope is explicitly started.

## R02.4 Admin integration

Only after child runtime exists:

- expose a read-only canonical Weekly contract first;
- update Daily/Weekly Admin screen to show real weekly identity/state;
- preserve explicit absence for capabilities still not implemented;
- add authoring/write capability only if there is a real revision/apply boundary.

## R02 exit criteria

- deterministic UTC weekly identity tested;
- reset/resume/reward idempotency tested;
- child CI green;
- Admin contract/validator updated without synthetic fields;
- parent Admin CI + Platform CI green.

---

# R03 — Alternative Modes canonical runtime

**Status:** PENDING AFTER R02

Admin Phase B currently provides an explicit runtime-absence diagnostic. That is correct until a real child owner exists.

## R03.1 Mode registry

Create a versioned canonical registry describing only real modes.

Each mode should define:

- stable ID;
- availability/unlock predicate;
- runtime owner;
- ruleset/version;
- session lifecycle;
- persistence requirements;
- telemetry ownership.

## R03.2 Runtime implementations

Implement Alternative Modes incrementally instead of shipping a fake generic shell.

For each mode:

- real gameplay rules;
- deterministic/replay-safe state where relevant;
- input pipeline compatibility;
- performance budget;
- test coverage;
- explicit unsupported features.

## R03.3 Admin boundary

After real runtime owners exist:

- replace absence diagnostic with runtime-backed read surfaces;
- introduce editing only when an apply/publish owner exists;
- never expose controls that mutate nonexistent runtime fields.

## R03 exit criteria

- at least the approved Alternative Modes have real child runtime ownership;
- registry + runtime tests pass;
- Admin reflects only real capabilities;
- child/parent CI green.

---

# R04 — Voice / Hybrid final acceptance and hardening

**Status:** ENGINEERING FOUNDATION EXISTS; HARDWARE/REAL-LOAD ACCEPTANCE PENDING

Do not redo the Voice platform from scratch.

Known architecture already includes Typing / Voice / Hybrid work and offline Voice hardening. Re-audit latest Git before editing.

## R04.1 Real combat-load profiling

Measure on supported hardware/browser:

- audio capture → main-thread dispatch delay;
- decoder ACK turnaround;
- pending/backlog high-water mark;
- overflow count;
- event-loop lag;
- combat FPS/frame pacing;
- CPU and memory trend during long sessions;
- behavior during heavy VFX/boss combat;
- recovery after overload.

Synthetic E2E timing alone is not sufficient to mark the feature accepted.

## R04.2 Recognition acceptance

Validate real microphone behavior for:

- Typing-only mode unaffected;
- Voice-only mode;
- Hybrid mode;
- permission denial/recovery;
- mic disconnect/reconnect;
- slow/fast speech;
- repeated words;
- wrong recognition/noise;
- pause/resume/tab visibility transitions;
- long combat session.

## R04.3 Performance fixes only from measured evidence

If profiling exposes a bottleneck, fix the measured owner first:

- capture/worklet;
- main-thread dispatch;
- decoder worker;
- queue/backpressure;
- rendering contention;
- audio mixing.

Do not arbitrarily increase queue/TTL thresholds to hide overload.

## R04 exit criteria

- real hardware acceptance evidence recorded;
- no input regression in Typing mode;
- Voice/Hybrid stable under combat load;
- relevant tests/build/CI green;
- explicit ACCEPTED checkpoint written to this file.

---

# R05 — Historical Analytics backend

**Status:** FUTURE BACKEND SCOPE

Current Admin analytics is intentionally session/runtime telemetry only. Do not treat the absence of historical analytics as an Admin bug.

## R05.1 Data model first

Define a versioned event/aggregate schema for approved metrics such as:

- sessions;
- stage attempts/completions;
- WPM/accuracy distributions;
- deaths/failures;
- retention-like aggregates if identity/privacy architecture supports them;
- mode usage;
- economy/progression aggregates where appropriate.

Define retention, privacy, aggregation boundaries and migration strategy before UI.

## R05.2 Storage/ingestion

Implement a real backend or approved storage owner.

Requirements:

- idempotent ingestion;
- schema/version validation;
- bounded payloads;
- no fabricated history from browser-local session state;
- no cross-player claims unless the backend truly has multi-player data.

## R05.3 Admin historical surfaces

Only after data is real:

- time-range filters;
- aggregate trends;
- stage/world/mode breakdowns;
- empty/unavailable states;
- no write controls unless there is a real data-management requirement.

## R05 exit criteria

- schema + ingestion + storage owner are real;
- historical queries tested;
- Admin uses authenticated backend data;
- privacy/retention constraints documented;
- CI green.

---

# R06 — Expand intentionally read-only Admin controls only when justified

**Status:** OPTIONAL / CAPABILITY-DRIVEN

Several Admin surfaces are intentionally read-only because runtime ownership or safe mutation boundaries do not exist.

For any future write feature, require this chain:

`editor → validation → revision → publish/apply owner → runtime consumer → audit/history → rollback/test`

Do not add an Edit/Save button first and invent persistence afterward.

Each proposed write capability must answer:

1. Who owns the canonical value?
2. What schema/version validates it?
3. How is concurrent editing handled?
4. What is the immutable revision identity?
5. What applies/publishes it?
6. What runtime actually consumes it?
7. How is rollback performed?
8. What tests prove the runtime changed as intended?

---

## 4. FIRST-UNFINISHED POINTER

At creation of this file:

`FIRST_UNFINISHED = R01 — Campaign Map & Rest Stop completion`

More specifically:

`NEXT EXACT UNIT = R01.1/R01.2 — audit canonical hidden-content owner, then implement deterministic Hidden Shop auto-discovery through the existing RNG/persistence lifecycle.`

After R01.2 is completed and green, continue automatically to R01.3 Hidden Station instead of stopping.

## 5. CROSS-TAB STARTUP PROCEDURE

When a new chat/tab receives a request such as **"tiếp tục Space Typing"**, it should do the following without asking the user to repeat old context:

1. Read this file first.
2. Read `docs/SPACE_TYPING_ADMIN_UIUX_PROGRESS.md` to avoid reopening completed Phase B work.
3. Fetch latest GitHub HEADs for the relevant parent and child branches.
4. Compare current Git state with the checkpoints recorded here.
5. Read commits newer than the checkpoints.
6. Update the first-unfinished pointer mentally from actual Git state.
7. Continue the first unfinished unit.
8. Run focused tests, then broader build/CI gates.
9. Fix blockers and continue within the same milestone.
10. Update this file before ending the work session.

## 6. HANDOFF TEMPLATE TO KEEP UPDATED

After each implementation checkpoint, append/update this section:

### Latest checkpoint

- Date:
- Parent branch / HEAD:
- Child branch / HEAD:
- Completed milestone/unit:
- Files changed:
- Focused tests:
- Child CI:
- Parent Admin CI:
- Platform CI:
- Blockers:
- First unfinished unit:
- Exact next action:

## 7. CURRENT CHECKPOINT AT FILE CREATION

- Date: 2026-10-09 (Asia/Ho_Chi_Minh)
- Parent `feat/space-typing-admin-uiux`: `c608e94d33206a54a787bdb864ad58028b714041`
- Child Admin `feat/admin-world-music-stage-policy`: `8128a2a5a7713fff80cd1286b607de6a3e7190f7`
- Child gameplay `feat/bgv-integration-current`: `fa63c79bde068d2de07b67402158c93462adecd1`
- Admin Phase B: COMPLETE / canonical cleanup green
- Current engineering scope: R01 Campaign Map & Rest Stop
- First unfinished unit: deterministic Hidden Shop discovery via existing hidden-content RNG/persistence owner
- Following unit: deterministic Hidden Station discovery
- Current blocker: NONE known; implementation must begin with a fresh Git audit

## 8. SHORT PROMPT FOR A NEW TAB

Use this when opening a new chat if desired:

> Continue `sinhvienaiti/typing-game` / `sinhvienaiti/space-typing` from `docs/SPACE_TYPING_REMAINING_IMPLEMENTATION_PROGRESS.md`. The task is resumable and idempotent. Fetch latest parent/child HEADs first, read newer commits, do not reset/revert/overwrite newer work, determine what is already complete from current Git state, then continue from the first unfinished milestone. Do not stop after fixing one blocker; continue until the current milestone is complete or there is a genuine external/hardware blocker. Never weaken validators/tests to make CI pass. Do not mark PR Ready or merge unless I explicitly ask.
