# Full Code Review — Shared Learning / Smart Review

Date: 2026-09-25  
Mode: **REVIEW ONLY — no implementation fix is retained**  
Parent repository: `sinhvienaiti/typing-game`  
Review baseline: `main@6cc291a78986ac034d0eb9eca2c040a9b73660da`

## 1. Scope

This review was reconstructed directly from GitHub and covers the active parent implementation plus the exact child revisions pinned by the parent baseline:

- Parent platform: `sinhvienaiti/typing-game@6cc291a78986ac034d0eb9eca2c040a9b73660da`
- Monkeytype: `01cca03b6f38c054f1fdd41ed5150160a6f3cd00`
- Recall Typing: `59c1d6043a09c23108e2390a2e259bb1be23e83d`
- Vocabulary Shooter: `b1721c43be075836a293fa6ba10ba908f4d06c22`
- Space Typing: `a50dcfcb29d7ff27a365a8ebf093836aeae97d2b`
- Karaoke Typing: `f2bd7ae55143d98cd270535d6e6c06d87a8742ec`

Reviewed areas:

- Shared Learning event parsing, normalization, aggregation, mastery, review priority, next-review timestamps
- IndexedDB persistence and batching
- Parent/child `postMessage` contract
- Smart Review Dashboard, Builder, Session, Mixed Review and Adaptive Mix
- Review datasets for Monkeytype, Recall Typing, Vocabulary Shooter, Space Typing and Karaoke Typing
- Import / Export / selective reset / reset all
- Browser route / reload / stale-session behavior
- Large-profile performance paths
- UI/UX and keyboard recovery in Smart Review
- Security boundaries for imported JSON and cross-frame messaging
- Static Play/build dependency logic and current tests
- Child-game runtime lifecycle: timers, requestAnimationFrame loops, event listeners, audio/TTS and media cleanup
- Child backup/import and per-game local persistence boundaries
- Project launchers, Play-mode stale-build detection and Platform CI coverage
- Project-owned/custom Monkeytype translation, speech, typing-text and learning modules

The review used six passes:

1. Correctness, cross-game contracts and data integrity.
2. Performance, lifecycle/recovery, UI/UX and security.
3. Regression review of the initial findings and proposed solutions.
4. Child-game runtime review across Recall, Shooter, Space and Karaoke.
5. Project-owned/custom Monkeytype plus launcher/build/CI review.
6. Final cross-check for overlapping findings, severity inflation and source-only suspicions.

For Monkeytype, the review targets this project's custom/fork-specific code and integration surfaces. It does not claim a fresh line-by-line audit of unrelated upstream Monkeytype code.

## 2. Baseline CI state

The review started from parent HEAD:

`6cc291a78986ac034d0eb9eca2c040a9b73660da`

Latest Platform CI for that exact HEAD:

- Workflow: Platform CI
- Run: `36029563264`
- Result: PASS

The baseline child checkpoints documented by the parent also had passing CI:

- Monkeytype: Custom EN-VN CI `36016126490` — PASS
- Recall Typing: CI `36017329739` — PASS
- Vocabulary Shooter: CI `36019201874` — PASS
- Space Typing: CI `36022862848` — PASS
- Karaoke Typing: CI `36024029825` — PASS

Important: CI PASS is not treated as proof that the implementation has no bugs. The findings below are code-path issues not fully covered by the existing baseline test suite.

The review-only report commit that restored the active tree to baseline code plus this document was also verified:

- Parent report-only HEAD before this continuation: `949065314b98a1fbfe8c5dc13586ad1839285c6f`
- Platform CI run: `36034579893`
- Result: PASS

That later PASS confirms the review-only repository state builds/tests under the current Platform CI, not that the findings below are fixed.

---

# 3. Confirmed Findings

## F01 — Out-of-order Learning Events can roll live learning state backward

**Severity:** High  
**File:** `shared/learning/core.mjs`  
**Function/module:** `applyLearningEvent()`, `applyLearningEvents()`

### Problem

Learning Events are applied in receive/order-of-processing order. The implementation directly assigns:

- `lastSeenAt = event.occurredAt`
- `lastCorrectAt = event.occurredAt` for correct events
- `lastWrongAt = event.occurredAt` for wrong events
- `updatedAt = event.occurredAt`
- `correctStreak` according to the event currently being processed

There is no protection against an older event arriving after a newer event.

### Condition

A delayed event can occur when:

- multiple events are batched;
- an iframe or browser task is delayed;
- multiple tabs emit events;
- events are queued before a query/flush;
- a child posts an event with a valid timestamp older than the latest persisted record.

### Impact

A late older event can make:

- `lastSeenAt` move backward;
- `lastCorrectAt` or `lastWrongAt` move backward;
- `profile.updatedAt` move backward;
- `correctStreak` describe processing order rather than chronological learning order;
- mastery / review priority / next review time be calculated from stale time state.

This can change Smart Review ordering and due calculations.

### Root cause

Event chronology is not separated from event arrival order.

### Reproduce / evidence

For one vocabulary item:

1. Apply correct event at 10:10.
2. Apply wrong event at 10:05.
3. The baseline implementation writes `lastSeenAt = 10:05` even though 10:10 was already persisted.

The same issue exists when a delayed event is applied after an already-current record.

### Proposed fix

- Parse the batch first.
- Apply batch events in stable `occurredAt` order.
- Never decrease `lastSeenAt`, `lastCorrectAt`, `lastWrongAt` or profile `updatedAt`.
- Keep bounded mistake/answer histories chronologically ordered.
- Recalculate mastery/review timing using the newest live timestamp.
- Add regression tests for unordered batches and late historical events.

---

## F02 — Batched Learning Events deep-clone the complete profile repeatedly

**Severity:** Medium  
**File:** `shared/learning/core.mjs`  
**Function/module:** `migrateLearningProfile()`, `applyLearningEvent()`, `applyLearningEvents()`

### Problem

`applyLearningEvents()` reduces over the batch and calls `applyLearningEvent()` once per event.

Each call goes through profile migration/cloning and then clones the profile again before changing one record. Therefore a batch can repeatedly clone all vocabulary, grammar and sentence collections.

### Condition

The parent bridge can flush up to 32 events at once. The problem becomes increasingly expensive as the profile grows to thousands or tens of thousands of records.

### Impact

Unnecessary:

- CPU work;
- object allocations;
- garbage collection;
- latency before ACK;
- main-thread pressure.

At large profile sizes this makes the cost approximately proportional to:

`batch size × complete profile size`

rather than:

`one profile copy + batch updates`.

### Root cause

The single-event immutable-update helper is reused directly inside batch processing.

### Reproduce / evidence

Create a large Learning Profile and call `applyLearningEvents(profile, 32Events)`. Source inspection shows the full migration/clone path runs for every event.

### Proposed fix

- Migrate/clone the input profile once per batch.
- Parse all events once.
- Apply the parsed events to the one cloned working profile.
- Keep `applyLearningEvent()` as the single-event public API.
- Add an immutability regression test to ensure the original profile is still untouched.

---

## F03 — IndexedDB read-modify-write is not atomic across browser tabs

**Severity:** High  
**File:** `shared/learning/browser-store.mjs`  
**Function/module:** `BrowserLearningProfileStore.apply()`, `applyMany()`, `load()`, `persist()`

### Problem

The baseline write flow is:

`load() -> calculate next profile -> persist()`

The read and write happen in separate IndexedDB transactions.

The in-memory `operationChain` only serializes operations inside one `BrowserLearningProfileStore` instance. It does not serialize a second browser tab/window.

### Condition

Two parent tabs are open and both receive Learning Events close together.

Example:

1. Tab A loads profile version P.
2. Tab B loads the same profile version P.
3. A writes P+A.
4. B writes P+B.
5. A's update is lost.

### Impact

Silent Learning Event loss across tabs. This directly corrupts Shared Learning Memory and can change mastery/review selection.

### Root cause

The read-modify-write operation is split across transactions; the JavaScript promise chain is tab-local.

### Proposed fix

Perform the read and write in the same IndexedDB `readwrite` transaction:

- `get(profile)`
- derive updated profile inside that transaction callback
- `put(updated profile)`
- resolve only on transaction completion

IndexedDB then serializes competing readwrite transactions on the same store.

Add a store-level test or browser integration test modeling interleaved writers.

---

## F04 — Prototype-like entity IDs are unsafe in plain-object collections

**Severity:** High  
**File:** `shared/learning/core.mjs`  
**Function/module:** record lookup/write in `applyLearningEvent()`

### Problem

Learning collections are ordinary JavaScript objects and records are accessed with:

`collection[event.entityId]`

Vocabulary IDs can originate from child/user vocabulary input after normalization.

Keys such as:

- `__proto__`
- `constructor`

have special/inherited behavior on normal objects.

For example, `collection["constructor"]` can resolve an inherited property instead of "record missing", while assigning `__proto__` has prototype semantics.

### Condition

A vocabulary item or imported/event entity ID normalizes to a prototype-like property name.

### Impact

Possible:

- wrong record selected;
- runtime type failure;
- collection prototype mutation;
- data corruption;
- security boundary confusion for user/import supplied text.

### Root cause

Dictionary-like storage uses a normal object plus inherited-property lookup.

### Proposed fix

Keep valid vocabulary unchanged; do not ban legitimate words.

Use one of:

- own-property lookup via `Object.hasOwn()` plus `Object.defineProperty()`; or
- null-prototype dictionaries throughout the schema, with migration compatibility.

Add regression tests for `__proto__` and `constructor`.

---

## F05 — A post-persistence callback failure can be reported as `persist-failed`

**Severity:** Medium  
**File:** `portal/src/learning/bridge.ts`  
**Function/module:** `ParentLearningBridge.#drain()`

### Problem

The same `try/catch` contains:

1. IndexedDB persistence;
2. the `onApplied` orchestration callback;
3. child ACK posting.

If persistence succeeds but `onApplied` throws, control enters the catch block and the child receives a `persist-failed` error.

### Condition

A Mixed/Adaptive orchestration callback throws after the Learning Event was already committed to IndexedDB.

### Impact

The child receives false information: the event is persisted but the response says it was not.

This creates ambiguity and would become a duplicate-learning risk if a child later retries failed requests.

### Root cause

Persistence failure and post-persistence side effects share one error boundary.

### Proposed fix

- Keep persistence in its own `try/catch`.
- After persistence succeeds, invoke orchestration callback independently.
- ACK the child independently.
- Log callback/ACK delivery problems without reclassifying successful persistence as `persist-failed`.

Add a regression test with a deliberately throwing `onApplied`.

---

## F06 — Backup import accepts internally inconsistent Learning Profile records

**Severity:** High  
**File:** `shared/learning/profile-backup.mjs`  
**Function/module:** `validateLearningProfile()`, `validateRecord()`

### Problem

Baseline validation checks that several numeric fields are finite and non-negative, but does not fully enforce profile invariants.

Examples currently structurally acceptable include:

- fractional attempt/counter values;
- `correct + wrong != attempts`;
- `hints > attempts`;
- `replays > attempts`;
- `responseSamples > attempts`;
- `correctStreak > correct`;
- mastery/reviewPriority above 100;
- summed grammar/sentence `errorTypes` greater than total wrong attempts.

### Condition

User imports malformed, manually edited, old, or externally generated JSON.

### Impact

Invalid data can replace the canonical IndexedDB profile and then affect:

- mastery;
- review priority;
- dashboard display;
- filters;
- Adaptive Mix signals;
- export round trips.

### Root cause

Schema validation checks primitive shape but not cross-field invariants.

### Proposed fix

Validate before replacement:

- counters are non-negative integers;
- mastery and reviewPriority are integers in `0..100`;
- `correct + wrong === attempts`;
- dependent counters cannot exceed attempts/correct where applicable;
- error classification totals cannot exceed wrong attempts.

Add malformed-backup regression cases for each invariant.

---

## F07 — Persisted Smart Review plans are trusted after only shallow version checks

**Severity:** High  
**File:** `portal/src/review/session.ts`, `shared/learning/review-session.mjs`  
**Function/module:** `readSession()`; proposed `parseReviewPlan()`

### Problem

Baseline `readSession()` parses `sessionStorage` and accepts the plan when:

- wrapper `version === 1`
- `plan.version === 1`

Nested plan data is not validated before runtime use.

### Condition

Session data is:

- stale after a code/schema change;
- manually modified;
- partially written;
- corrupted;
- restored from an older browser session.

### Impact

Later code assumes valid:

- options;
- entity types;
- score fields;
- item arrays;
- counts;
- compatibility arrays.

Malformed state can crash Review Session or produce impossible routing state.

### Root cause

A persisted boundary is treated as a trusted in-memory TypeScript object after JSON parsing.

### Proposed fix

Create one canonical `parseReviewPlan(unknown)` validator and use it whenever a stored plan is loaded.

Validate:

- version and timestamps;
- options through existing `parseReviewPlanInput()`;
- every item;
- mastery/priority range;
- `compatibleGames`;
- counts and count relationships.

If invalid, delete the stale storage entry and show the existing "No active review session" recovery UI.

---

## F08 — A stored review item can be structurally valid but incompatible with its own plan

**Severity:** Medium  
**File:** `shared/learning/review-session.mjs`  
**Function/module:** persisted ReviewPlan validation / capability matrix

### Problem

Even after validating shapes, a stale plan can contain an item whose:

- `compatibleGames` is empty; or
- selected plan game/goal no longer supports that item's entity type.

This can happen after capability changes between versions.

### Condition

An old persisted plan survives while game capabilities or plan rules have changed.

### Impact

The parent can present a session that cannot be safely launched into the selected executor.

### Root cause

Structural validation and semantic compatibility validation are different checks; the baseline has neither persisted-plan validation nor a final compatibility invariant.

### Proposed fix

During stored-plan parsing require:

- each item has at least one concrete compatible game;
- the selected `options.game + options.goal` still supports the item;
- pseudo orchestration games are not accepted as concrete child compatibility entries.

Reject and clear stale incompatible plans.

---

## F09 — Mixed/Adaptive Review storage validation is too shallow

**Severity:** High  
**File:** `portal/src/review/mixed.ts`  
**Function/module:** `readMixedReview()`, `enrich()`, orchestration progress state

### Problem

Baseline validates only a few top-level version fields before casting parsed JSON to `StoredMixedReview`.

It does not validate:

- segments array shape;
- concrete segment game;
- segment item arrays;
- `selectedCount`;
- `activeSegmentIndex` bounds;
- `completedBySegment` shape;
- completion timestamp;
- launched segment id type.

### Condition

Malformed/stale `typingGameMixedReviewV1` exists in `sessionStorage`.

### Impact

Possible:

- runtime exceptions;
- wrong active segment;
- impossible progress state;
- inability to resume/cancel cleanly;
- broken navigation after refresh.

### Root cause

Persisted orchestration state is trusted as a TypeScript shape without runtime validation.

### Proposed fix

Add a strict `validStoredMixedReview()` boundary validator.

On invalid data:

- remove the storage key;
- return `null`;
- let the parent rebuild the orchestration state from the canonical ReviewPlan.

Validate concrete game IDs against `REVIEW_CAPABILITIES`.

---

## F10 — Debounced Dashboard search can fire after navigation and change route/state

**Severity:** Medium  
**File:** `portal/src/review/dashboard.ts`  
**Function/module:** Dashboard search `input` debounce

### Problem

Search schedules a timer (~280 ms) that calls the dashboard URL-state updater unconditionally.

The timer is not cancelled/guarded when the user leaves `/review`.

### Condition

1. Type in Dashboard search.
2. Navigate to another route before the debounce expires.
3. The old callback fires.

### Impact

The stale Dashboard callback can mutate URL parameters or navigate the user back into review-related state after they already left.

### Root cause

The debounced callback has no route/component liveness check.

### Proposed fix

Before applying the search update verify:

- the search element is still connected; and
- current normalized route is still exactly `/review`.

Longer term a route-scoped cleanup mechanism is also acceptable, but it is unnecessary if the small guard solves the current bug.

---

## F11 — Smart Review detail drawer lacks complete keyboard/focus recovery

**Severity:** Low  
**File:** `portal/src/review/dashboard.ts`  
**Function/module:** item detail drawer

### Problem

The drawer can be closed by button/backdrop, but baseline does not fully implement modal semantics and keyboard recovery.

Missing behavior includes:

- `role="dialog"`;
- `aria-modal="true"`;
- Escape-to-close;
- restoring focus to the element that opened the drawer.

### Condition

Keyboard-only or assistive-technology navigation.

### Impact

Reduced accessibility and a confusing keyboard position after closing item details.

### Root cause

The drawer is visually modal but not implemented as a complete modal interaction.

### Proposed fix

- Capture `document.activeElement` before opening.
- Add dialog semantics.
- Handle Escape.
- Use one `closeDrawer()` path for button, backdrop, Escape and action navigation.
- Restore focus when the previous control still exists.

A full focus trap can be evaluated separately; do not over-engineer it unless keyboard traversal demonstrates a real escape problem.

---

## F12 — Read-only Dashboard and Review Builder paths deep-clone the entire profile

**Severity:** Medium  
**File:** `shared/learning/query.mjs`, `shared/learning/review-session.mjs`, `shared/learning/core.mjs`  
**Function/module:** `queryLearningProfile()`, `buildReviewPlan()`, `migrateLearningProfile()`

### Problem

Read-only operations call `migrateLearningProfile()`, which creates a fresh profile and deep-clones collections.

Dashboard interactions can trigger query/sort/filter repeatedly, while the Review Builder also clones the profile before merely reading it.

### Condition

Large Learning Profiles, especially 10,000–50,000 records.

### Impact

Unnecessary memory allocation and GC during:

- pagination;
- filter changes;
- search;
- sorting;
- review plan previews.

The query still needs O(n) scanning/sorting for these features, but the extra full deep clone is unnecessary duplicated work.

### Root cause

The same defensive migration helper is used for mutation and trusted read-only views.

### Proposed fix

Introduce a read-only validated view helper that:

- checks the profile version/top-level collections;
- does not deep clone;
- is used only by functions that never mutate input.

Keep cloning/migration for mutation boundaries.

Add a 50,000-record query regression to prevent accidental unbounded page output and to expose avoidable cloning regressions.

---

## F13 — Monkeytype Learning Memory posts events to wildcard origin

**Severity:** Medium  
**Repository:** `sinhvienaiti/monkeytype`  
**File:** `frontend/src/ts/learning/learning-memory.ts`  
**Function/module:** `postAttempt()`

### Problem

Monkeytype's normal Learning Memory event emission uses:

`window.parent.postMessage(message, "*")`

Other Smart Review child paths use the fixed trusted parent origin.

### Condition

Monkeytype is embedded by any parent page other than the intended local Portal.

### Impact

Learning event payloads can be disclosed to the embedding parent page.

In this local project the practical exposure is limited, but this is still an unnecessary trust-boundary inconsistency.

### Root cause

The older Learning Memory path kept wildcard target origin while newer child integrations use `https://typing-game.local`.

### Proposed fix

Use the same explicit trusted parent origin:

`https://typing-game.local`

Do not change the parent-side origin/source validation; both sides should remain strict.

Add a focused test or source-level contract assertion that the Learning Memory sender does not use wildcard origin.

---


## F14 — A stale Smart Review success timer can remove the next game's status UI

**Severity:** Medium  
**Repository:** `sinhvienaiti/typing-game`  
**File:** `portal/src/main.ts`  
**Function/module:** review-ready message handling / `currentReviewStatus`

### Problem

After a child reports `review-ready`, Portal schedules a 1.8-second timeout that later executes:

`currentReviewStatus?.remove(); currentReviewStatus = null;`

The callback reads the mutable global `currentReviewStatus` when it fires instead of retaining the status element that belonged to the game that scheduled the timeout.

### Condition

1. Game A reports Smart Review ready.
2. Portal schedules the success-status removal timer.
3. Before 1.8 seconds elapse, the user navigates to Game B.
4. `renderRoute()` clears globals and `renderGame(Game B)` assigns Game B's status element to `currentReviewStatus`.
5. Game A's old timeout fires.

### Impact

The stale timeout can remove Game B's current Smart Review status element and then null the global reference.

This is a UI lifecycle race and can hide useful "starting/ready/error" feedback for the newly opened game.

### Root cause

The timeout is bound to a mutable global rather than the route/game generation or the concrete status element that initiated it.

### Proposed fix

Capture the concrete element/token at scheduling time and only clear it if it is still current, for example:

- capture `const status = currentReviewStatus`;
- on timeout, remove `status`;
- set the global to null only when `currentReviewStatus === status`.

Alternatively use a route-generation token and invalidate route-owned timers on navigation.

Add a fake-timer regression:

- receive ready for Game A;
- navigate to Game B before 1.8 seconds;
- advance timers;
- assert Game B's status remains intact.

---

## F15 — Vocabulary Shooter backup import can silently persist fewer entries than it shows in memory

**Severity:** Medium  
**Repository:** `sinhvienaiti/vocab-shooter`  
**Files:** `src/main.ts`, `src/storage/db.ts`  
**Function/module:** backup import / `replaceVocabulary()`

### Problem

Shooter backup import accepts vocabulary rows when `en` and `vi` are merely strings and then keeps any existing non-empty `id` without checking uniqueness.

It does not apply the stricter usable-entry validation that Recall Typing already uses.

The IndexedDB store uses `keyPath: "id"` and persists entries with `put()`.

### Condition

A syntactically valid backup contains, for example:

- two different entries with the same non-empty `id`;
- English or Vietnamese values that are empty/whitespace strings;
- an empty vocabulary array.

### Impact

Duplicate IDs are both retained in the in-memory `customVocabulary` array, but later `put()` calls overwrite earlier rows with the same key in IndexedDB.

The running game can therefore see a different item count/content from the next reload.

Whitespace-only targets can also enter the runtime. An imported empty array clears the store; the next normal load then reseeds defaults, so the restored state is not stable across reload.

### Root cause

Backup import has its own weak parser instead of reusing one canonical vocabulary validator/normalizer and duplicate-ID policy.

### Proposed fix

Before replacing storage:

- require each row to be a plain object;
- trim/normalize `en`, `vi` and optional `ipa`;
- reject unusable rows;
- guarantee unique IDs, regenerating missing/duplicate IDs or rejecting duplicates consistently;
- reject a backup with zero valid vocabulary entries;
- only then call `replaceVocabulary()`.

Prefer one shared parser used by custom editor/bulk import/backup restore.

Add regression tests for:

- duplicate IDs;
- blank/whitespace text;
- malformed rows;
- empty vocabulary;
- import → IndexedDB reload preserving exact count/content.

---

## F16 — Karaoke Typing restart is not reentrancy-safe and can create multiple RAF loops

**Severity:** Medium  
**Repository:** `sinhvienaiti/karaoke-typing`  
**File:** `src/main.ts`  
**Function/module:** `restartGame()`, `tick()`

### Problem

`restartGame()` cancels the currently stored frame, resets shared game state, then awaits `controller.play()` before starting a new `requestAnimationFrame(tick)`.

Restart buttons call it with `void restartGame()` and are not guarded/disabled while that asynchronous restart is pending.

### Condition

With local media, two restart actions can enter `restartGame()` before the first `HTMLMediaElement.play()` promise resolves.

Both invocations cancel the same old frame and then await. When both promises resolve, each schedules a new RAF callback. Only the most recently assigned RAF id remains in the single `frameId` variable.

### Impact

Two independent `tick()` chains can run against the same engine/controller state.

That can cause duplicate rendering/timeline work, racey line transitions and unnecessary CPU use. Later cancellation by one stored `frameId` is not sufficient to identify every already-created loop.

### Root cause

The async restart path has no generation token, in-flight guard or stale-continuation check after `await controller.play()`.

### Proposed fix

Use a restart/loop generation token:

- increment generation at the start of every restart/return;
- capture the generation locally;
- after every async boundary, abort if the captured generation is stale;
- schedule `tick(generation)` only for the active generation;
- have `tick` stop immediately when its generation is stale.

Optionally disable Restart controls while restart is in flight for UX clarity, but the generation guard should remain the correctness mechanism.

Add a test with a deferred fake media `play()` promise, invoke restart twice, resolve both promises, and assert only one active RAF chain remains.

---

## F17 — Auxiliary cross-frame media messages do not consistently use the trusted parent origin

**Severity:** Low  
**Repositories:** Monkeytype, Recall Typing, Vocabulary Shooter, Space Typing  
**Files:** child speech/audio-focus modules and Shooter `src/main.ts`

### Problem

The main Shared Learning / Smart Review contracts use the fixed parent origin `https://typing-game.local`, but auxiliary media coordination is less strict:

- Monkeytype `audio-focus.ts` posts `typing-game:speech` with target origin `"*"`;
- Recall `src/audio/speech.ts` does the same;
- Shooter `src/audio/speech.ts` does the same;
- Space `src/speech.ts` does the same;
- Shooter accepts `typing-game:shared-music` from `window.parent` without also checking `event.origin === PARENT_ORIGIN`.

### Condition

A game is embedded by an unintended parent origin rather than the local Portal.

### Impact

The outgoing wildcard messages disclose only speech-active state, not vocabulary/event payloads, so the confidentiality impact is small.

For Shooter, an unintended embedding parent can also toggle the internal "shared music is playing" state and affect its built-in music behavior.

This is lower impact than F13, but it is a real trust-boundary inconsistency.

### Root cause

Auxiliary audio coordination predates or bypasses the stricter origin contract used by Shared Learning.

### Proposed fix

Use the same explicit `PARENT_ORIGIN` for outgoing speech messages.

For Shooter's incoming shared-music message, require both:

- `event.source === window.parent`;
- `event.origin === PARENT_ORIGIN`.

Add lightweight contract tests/source assertions for these auxiliary message paths.

---

# 4. Risks — not confirmed bugs

These are intentionally not labeled as confirmed defects.

## R01 — Learning request IDs are not durable idempotency keys

Current child implementations emit an attempt once and do not retry on missing/failed ACK, so no current duplicate-delivery path was confirmed.

However, the parent does not persist processed `requestId` values. If retry semantics are added later, the same Learning Event could be counted twice.

**Recommendation:** define idempotency semantics before adding child retries. Do not add a large dedupe subsystem now without a retry requirement.

## R02 — Import has no explicit file-byte limit

Import validates JSON after `file.text()`, but there is no explicit file-size cap before reading/parsing.

A very large user-selected file could cause memory/parse pressure.

**Recommendation:** if large-file behavior becomes a real local problem, add a simple file-size guard before `file.text()`. Choose the limit from expected backup sizes rather than an arbitrary tiny threshold.

## R03 — Exact historical streak reconstruction needs more history than the aggregate stores

Preventing old events from rolling live timestamps/streak backward is feasible.

But if a very old event arrives after several newer events, the aggregate alone cannot always reconstruct the mathematically exact historical chronological streak because the full ordered event log is intentionally not stored.

**Recommendation:** keep bounded aggregate semantics. Do not introduce an unbounded event log solely for exact retrospective streak reconstruction unless that becomes a product requirement.

## R04 — No true browser E2E test kills/reloads multiple tabs and iframes

The current coverage is strong at unit/integration/build level, but there is no browser harness that actually:

- opens two parent tabs;
- kills/reloads an iframe mid-review;
- reloads the parent while an event/ACK is in flight;
- verifies IndexedDB + sessionStorage recovery end-to-end.

**Recommendation:** add a small Playwright-style lifecycle suite only if the project is ready to maintain browser E2E infrastructure. Until then, keep focused deterministic tests around storage and lifecycle boundaries.


## R05 — Space page-lifecycle recovery begins with an unguarded noncritical localStorage write

`persistPageLifecycleRecovery()` calls `saveRecallMemory()` before its guarded player-recovery write. `saveRecallMemory()` directly calls `localStorage.setItem()`.

If that first write throws because storage is unavailable/quota-limited, execution can exit before the more important player recovery mirror and queued autosave are attempted.

No normal-path failure was reproduced from source alone, so this remains a reliability risk rather than a confirmed user-visible defect.

**Recommendation:** isolate the recall-memory write in its own try/catch so a failure cannot prevent player recovery. Add a test with a throwing storage adapter/window stub.

## R06 — Space keeps a full RAF draw loop active outside active gameplay

`Game.frame()` continuously advances effects and draws the scene on every animation frame, including non-playing phases. Adaptive render-scale observation is only applied while the phase is `playing`.

This can be intentional for animated title/menus, and source inspection alone cannot prove unacceptable CPU/GPU cost.

**Recommendation:** profile title, pause and stage-clear screens on the target Mac hardware. If idle cost is meaningful, reduce non-gameplay draw cadence or suspend expensive layers without removing visual features.

## R07 — Parent Platform CI is not a full five-game build/test gate

The parent Platform CI currently:

- initializes Monkeytype, Shooter, Recall and Space submodules;
- validates the Karaoke gitlink but does not initialize/build/test Karaoke;
- tests Recall and Space;
- builds Portal, Recall and Space;
- does not parent-build/test Shooter;
- does not parent-build Monkeytype, although a Play-mode environment validator runs.

Each reviewed child revision has its own passing checkpoint CI, so this is not evidence of a current broken build.

**Recommendation:** add a pragmatic parent integration matrix: initialize all pinned children and at minimum build/test Shooter + Karaoke, plus a bounded Monkeytype custom/integration smoke check if full upstream build cost is too high.

## R08 — Space Typing's two largest runtime files carry high change-risk

At the reviewed revision, `src/main.ts` is roughly 8.4k lines and `src/Game.ts` roughly 9.2k lines.

The test suite is extensive, which reduces risk, but very large orchestration/runtime files make lifecycle ownership, listener/timer review and safe refactoring harder.

**Recommendation:** do not refactor solely for line count. When future features touch stable boundaries, extract cohesive subsystems (route/UI orchestration, review integration, persistence coordination, rendering layers) with tests preserved before and after extraction.

---

# 5. Cross-game review result

## Parent → child review dataset contract

The five concrete adapters are aligned with the parent capability matrix at the reviewed revisions:

- Monkeytype: vocabulary, grammar, sentence
- Recall Typing: vocabulary
- Vocabulary Shooter: vocabulary
- Space Typing: vocabulary
- Karaoke Typing: vocabulary + sentence

No confirmed schema mismatch was found in the current pinned happy-path dataset formats.

## Child → parent Learning Event contract

Reviewed child builders normalize vocabulary keys consistently enough for the current parent canonical vocabulary key contract.

No confirmed duplicate-per-keypress regression was found in the currently pinned child implementations; events are emitted at learning-unit boundaries as intended.

## Review-ready / review-error flow

Current child listeners validate parent source/origin before accepting review datasets in Recall, Shooter, Space and Karaoke. Monkeytype Smart Review dataset intake also uses the fixed parent origin.

The higher-impact confirmed security inconsistency is Monkeytype's *normal Learning Memory attempt sender* using wildcard target origin (F13).

Auxiliary speech/music coordination also has weaker origin handling across several children (F17), although those messages carry much less sensitive state.

## Mixed / Adaptive progress

The core parent design—advance only after persisted Learning Events and only for the launched concrete segment—is sound.

The confirmed reliability gap is stale/malformed persisted orchestration state (F09), not the normal happy-path segment-matching logic.

---

# 6. Data integrity review result

Confirmed integrity defects are F01, F03, F04, F06 and F15.

Additional observations:

- vocabulary normalization uses NFKC + trim + collapsed whitespace + lowercase in the parent;
- event optional text is NFC-normalized;
- L18 already added stricter canonical backup-key validation;
- selective reset is scoped by entity group and preserves unselected collections;
- reset/import clear transient review queues to avoid running stale datasets against replaced profile state.

No additional confirmed silent-delete path was found in selective reset beyond the findings listed above.

Outside Shared Learning, Vocabulary Shooter backup restore has a separate duplicate-ID persistence mismatch (F15).

---

# 7. Performance review result

Confirmed performance/lifecycle findings:

- F02: repeated full-profile cloning inside event batches;
- F12: deep cloning for read-only Dashboard/Builder operations;
- F16: a reentrant Karaoke restart can create multiple RAF loops.

Space Typing's always-on non-gameplay RAF rendering is recorded as profiling risk R06 rather than a confirmed performance defect.

The architecture still performs full collection filtering/sorting for many Dashboard operations. That is expected for the current local profile model and is not by itself classified as a bug.

For 5,000–10,000 records the existing approach is reasonable after removing duplicated cloning. Around 50,000 records, query/sort remains O(n log n) for sort-heavy views; pagination bounds returned DOM/data but does not avoid scanning the source collection.

**Recommendation:** first remove duplicate cloning. Do not add indexing/caching complexity unless real measurements after that still show an interactive latency problem.

---

# 8. UI / UX review result

Confirmed UI/UX issues:

- F10: stale debounced search callback after navigation;
- F11: incomplete drawer keyboard/focus recovery;
- F14: stale Smart Review success timer can remove the next game's status;
- F16: Karaoke restart reentrancy can create duplicate animation loops.

Other reviewed Smart Review states include:

- loading;
- empty;
- error;
- disabled start state;
- paging;
- sorting;
- filtering;
- search;
- destructive confirmation;
- review session resume messaging.

No additional confirmed broken-button or overflow defect was established from source evidence alone in these passes.

Visual responsive verification remains best done in a browser/E2E pass rather than labeling source-only suspicions as bugs.

---

# 9. Security / input-boundary review result

Confirmed boundary issues:

- F04: prototype-like collection keys;
- F06: insufficient backup invariants;
- F13: wildcard Monkeytype attempt target origin;
- F17: weaker origin handling in auxiliary speech/shared-music messages.

Positive existing controls:

- parent validates active iframe window;
- parent validates exact child origin;
- parent validates matching `gameId`;
- review dataset item counts are bounded;
- request IDs use a restricted format;
- user-visible DOM in reviewed Smart Review code generally uses `textContent`/DOM nodes rather than injecting external text through `innerHTML`;
- backup import does not replace IndexedDB until validation succeeds.

No confirmed XSS path was found in the reviewed Shared Learning / Smart Review boundaries.

---

# 10. Test gaps

The current baseline tests do not fully cover the confirmed findings above.

Regression tests recommended together with the eventual fixes:

- unordered/late Learning Events;
- batch immutability with one profile clone path;
- prototype-like entity IDs;
- malformed backup cross-field invariants;
- stale persisted ReviewPlan shape;
- stale plan compatibility;
- malformed Mixed/Adaptive storage;
- callback throw after successful persistence;
- 50,000-record read-only query;
- route change before Dashboard debounce fires;
- drawer Escape + focus restoration;
- Monkeytype trusted target origin;
- multi-tab IndexedDB read-modify-write behavior;
- stale Smart Review success timer across route/game navigation;
- Shooter backup import with duplicate IDs, blank rows and empty vocabulary;
- Karaoke double restart with deferred media play;
- auxiliary speech/shared-music origin checks;
- Space pagehide recovery when a noncritical localStorage write throws;
- parent CI matrix coverage for Shooter/Karaoke and bounded Monkeytype integration.

---

# 11. Proposed implementation order

This is a recommended fix order, not implementation done by this review.

1. F03 multi-tab atomic persistence.
2. F01 event chronology.
3. F04 prototype-like keys.
4. F06 backup invariants.
5. F07 + F08 persisted ReviewPlan validation.
6. F09 Mixed/Adaptive persisted-state validation.
7. F05 bridge error-boundary correctness.
8. F02 + F12 duplicate profile cloning/performance.
9. F13 Monkeytype Learning Memory target origin + F17 auxiliary message origins.
10. F15 Shooter backup import validation.
11. F16 Karaoke restart generation/RAF ownership.
12. F10 + F14 Portal route/timer lifecycle.
13. F11 drawer keyboard/focus recovery.

After each group:

- add regression test first where practical;
- fix root cause;
- run Shared Learning tests;
- run Portal TypeScript/build;
- run affected child tests/build;
- run Platform CI;
- continue to the next group instead of treating one green CI run as proof the remaining findings are resolved.

---

# 12. Review-only repository state

The review initially used temporary verification patches/regression tests to prove several findings and proposed fixes. Those implementation changes are **not retained** in the active parent/child code after the user's review-only clarification.

The intended active code baseline after publishing this report is functionally the same as:

`sinhvienaiti/typing-game@6cc291a78986ac034d0eb9eca2c040a9b73660da`

plus this review document only.

Monkeytype's active reviewed implementation remains the original parent-pinned revision:

`01cca03b6f38c054f1fdd41ed5150160a6f3cd00`

The temporary verification history remains visible in Git history for audit evidence, but the fixes listed in this report must be treated as **proposed work**, not completed work.

## Review status — REOPENED for exhaustive custom-code coverage

The earlier review completed the planned Shared Learning / runtime passes, but the completion criterion has now been tightened:

> Review is not complete until every project-owned/custom-added/custom-modified code surface has been inventoried and reviewed. No implementation fix starts before that exhaustive pass and a final self-review of both findings and proposed solutions.

Therefore the previous **17 confirmed findings / 8 risks** remain valid review output, but they are **not the final total**.

Current GitHub source-of-truth checkpoint when this exhaustive pass was reopened:

- Parent: `ead7641bb35ae01d1507adcf5aef3cc0fcce5904`
- Monkeytype pin: `01cca03b6f38c054f1fdd41ed5150160a6f3cd00`
- Recall Typing pin: `59c1d6043a09c23108e2390a2e259bb1be23e83d`
- Vocabulary Shooter pin: `b1721c43be075836a293fa6ba10ba908f4d06c22`
- Space Typing pin: `a50dcfcb29d7ff27a365a8ebf093836aeae97d2b`
- Karaoke Typing pin: `f2bd7ae55143d98cd270535d6e6c06d87a8742ec`

### Custom-code inventory gate

The following inventory now defines the review boundary:

- Parent platform: **68 source-like files**, about **375 KB**, covering Portal, Shared Learning/data code, scripts, launchers and CI.
- Recall Typing: **17 source-like files**; the game is project-owned, so its full runtime/storage/audio/UI/test surface is in scope.
- Vocabulary Shooter: **22 source-like files**; the full game runtime/storage/audio/UI/test surface is in scope.
- Karaoke Typing: **13 source-like files**; the full game runtime/media/LRC/learning/UI/test surface is in scope.
- Space Typing: **320 source-like/test files**, about **2.15 MB**, including **164 `src` files** and **150 tests**. This is the largest remaining exhaustive-review surface.
- Monkeytype: compare of project fork baseline `master@91bd24bb8513785c7364cbea29296ff7adafac41` to the parent-pinned custom revision `01cca03b6f38c054f1fdd41ed5150160a6f3cd00` identifies exactly **58 changed/added files**, **10,492 additions** and **98 deletions**. These 58 files are the exhaustive Monkeytype custom review scope, including:
  - 10 custom modules;
  - 9 learning modules;
  - 7 input-pipeline modifications;
  - 14 related frontend tests;
  - upstream UI/config integration changes;
  - test-runtime hooks;
  - schema/build/CI changes.

The review remains **REVIEW ONLY**. Source code and submodule pins must not be changed while this gate is open.

---

# 13. User-observed issues and requested product corrections — backlog for verification

These observations are recorded now so they are not lost, but they do **not** automatically become confirmed code findings until the exhaustive code pass verifies the relevant implementation path.

## U01 — Space top IPA/Vietnamese banner overlaps combat space

**Observed:** the fixed IPA/Vietnamese display occupies the same visual region enemies can enter, making target identification difficult.

**Required direction:**

- reserve HUD space outside the combat spawn/movement area;
- enemies must not spawn/travel behind the learning banner;
- verify responsive layouts and all enemy/boss/bonus spawn paths.

## U02 — IPA display behavior must be configurable and persistent

Current desired modes:

- top banner;
- killed-enemy position;
- both;
- off.

The top banner should keep the latest killed target's IPA/meaning until another kill replaces it; it should not auto-hide after a few seconds.

The old killed-enemy-position feedback should remain available instead of being silently replaced by the new banner.

## U03 — Stage result / measured report is too small

**Required direction:** desktop result UI should become a large near-fullscreen report with enough width/height for combat, typing, learning and reward sections without cramped nested scrolling.

## U04 — Settings need explicit Save/Cancel and clear apply semantics

**Observed/requested:**

- explicit Save button;
- Cancel/close without accidental changes;
- successful-save feedback;
- dirty/unsaved state;
- clear distinction between immediate, next-stage and stage-reload settings.

Any difficulty/combat-pacing setting that cannot safely update mid-stage must warn the user on Save and, when accepted, reload/restart that stage with the newly saved configuration.

The exhaustive review must verify why current mid-game setting changes appear to have no runtime effect.

## U05 — Stage replay must preserve already-earned persistent progression

Requested product rule:

- clearing a stage commits earned persistent progression/rewards;
- replaying an already-cleared stage must not roll back previously earned equipment, XP, loot, unlocks or other persistent progression;
- replay should be usable for farming XP/items;
- remove the old death behavior that sends the player back to checkpoint blocks such as 10/20/30;
- keep only the special in-stage diamond revive that resumes the current encounter after death.

The review must inspect current checkpoint/recovery/replay/reward code before proposing the migration plan.

## U06 — Rage / ship signature skill system needs a clearer model

Requested product direction:

- rage meter split into five visible segments;
- each usable segment can power a rage action according to the final design;
- full/usable rage must have a strong glow/burning visual state;
- each ship has signature rage/ultimate behavior bound to that ship, not replaceable equipment;
- rage/ultimate kills should grant appropriate gameplay kill/score/reward credit;
- however Shared Learning credit must only claim a typing success when actual typing evidence exists;
- multi-layer enemy armor/HP must obey the final rage-skill rules rather than being unconditionally deleted by a generic screen clear.

The exhaustive pass must first inventory the current per-ship ultimate/rage implementation and kill/reward attribution paths.

## U07 — Equipment artwork is visually undersized

Keep the current information layout direction, but enlarge and clarify equipment imagery/iconography so the visual hierarchy is balanced against item name/description text.

## U08 — Recall bonus target cannot be selected while the normal enemy lock owns input

The review must inspect target acquisition/input dispatch precedence.

Desired behavior: bonus targets must be intentionally typeable and should receive appropriate priority without corrupting an already-valid active typing sequence.

## U09 — Recall hidden-letter cells should be simplified

Keep the current outer frame/art direction, but replace the cramped small internal boxes with a simpler letter/underscore presentation such as `M _ _ _`, plus a readable glow/border state.

## U10 — Map/background system needs verification and a test selector

The exhaustive review must establish:

- whether later maps/worlds already have distinct backgrounds;
- whether the simple current background is intentionally only the early-map look;
- whether every world/background is wired correctly.

If multiple backgrounds exist, add a dev/test-lab selector to preview them after review; do not alter production progression rules solely for testing.

## U11 — Recall controls currently sit in the middle of gameplay

`Recall clues`, `Replay` and `Reveal letter` should be moved into a dedicated HUD/control cluster at an edge/corner rather than obscuring the combat field.

## U12 — Monkeytype project-added settings need a visible Codex marker

Because upstream Monkeytype already has a very large settings surface, settings introduced by this project should be easy to identify, e.g. `Forgive corrected errors — Codex`.

The exhaustive Monkeytype pass must inventory every project-added setting so labeling is consistent rather than applied to only one option.

## U13 — Monkeytype Vietnamese composed input is broken

Observed reproduction includes Vietnamese composition where typing sequences that should form characters such as `ô` cause earlier text to move/replace incorrectly and produce false error state.

This is a **high-priority verification target** in the seven modified Monkeytype input-pipeline files.

Likely solution family to validate against the actual code:

- IME/composition-aware input handling;
- `beforeinput` / `input` / composition lifecycle correctness;
- NFC normalization of expected and committed text;
- grapheme-safe cursor/delete/validation behavior.

Do not implement the solution until the actual modified input code and its tests prove the root cause.

---

# 14. Exhaustive review completion criteria

No fix phase may start until all of the following are complete:

1. Inventory every parent custom source/config/script and mark it reviewed.
2. Review the complete project-owned Recall Typing source/test surface.
3. Review the complete project-owned Vocabulary Shooter source/test surface.
4. Review the complete project-owned Karaoke Typing source/test surface.
5. Review all Space Typing modules by subsystem, including gameplay, enemy/boss, recall, skills/rage, rewards, progression, replay/checkpoint/revive, persistence, UI, audio, backgrounds/test-lab and performance hot paths.
6. Review all 58 Monkeytype files changed from the fork baseline, with special attention to the seven input-pipeline modifications and every project-added setting.
7. Cross-check parent↔child contracts after the per-game reviews.
8. Verify each user-observed U01–U13 item against code and classify it as:
   - confirmed bug;
   - confirmed UX issue;
   - product/spec change;
   - risk;
   - not reproducible / incorrect assumption.
9. For every confirmed item, write root cause, impact, concrete solution and regression-test plan.
10. Perform a second independent pass over the completed findings to remove duplicates, correct severity, and challenge the proposed solution for unintended regressions.
11. Only after this report is final and internally self-reviewed may implementation begin.

No source implementation fix is included in this report update.
