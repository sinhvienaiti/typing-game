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


## F18 — Space Typing rejects valid v26 backup files even though v26 migration exists

**Severity:** High  
**Repository:** `sinhvienaiti/space-typing`  
**Files:** `src/persistence/backup.ts`, `src/persistence/player-save.ts`  
**Function/module:** `parsePlayerSaveJson()`, `migratePlayerSave()`

### Problem

The current player-save schema is v27 and `migratePlayerSave()` contains an explicit `raw.version === 26` migration path.

However, `parsePlayerSaveJson()` accepts versions 1–25 and the current `PLAYER_SAVE_VERSION` only. Because the current version is 27, v26 is omitted from the accepted-version condition and is rejected as unsupported before migration can run.

### Condition

A user has a legitimate Space Typing backup exported while the save schema was v26 and attempts to restore it after updating to the current v27 build.

### Impact

A valid recent backup cannot be restored through the supported import UI.

This directly weakens the backup/recovery path and can strand user progression even though the migration implementation required to recover it already exists.

### Root cause

Supported import versions are maintained as a long manual boolean chain separate from the migration switch. The two lists drifted when v27 was introduced.

### Proposed fix

Make backup-version acceptance and migration support share one source of truth.

At minimum:

- add v26 to the accepted backup versions;
- validate every v26 field required by `PlayerSaveV26`, including equipment, progression, currencies, checkpoint/recovery state, route/upgrades/relic/codex/ascension/hotbar;
- migrate it through the existing v26 → v27 path.

Prefer replacing the repeated `version === ...` chains with explicit schema/version descriptors so a newly added migration cannot silently be omitted from backup import.

Add regression tests that construct a valid v26 backup, import it, assert `ok: true`, assert `migrated: true`, and verify the resulting save is v27 with the original persistent state preserved.

---

## F19 — Space Typing backup validation has schema holes for v21 and v22

**Severity:** High  
**Repository:** `sinhvienaiti/space-typing`  
**Files:** `src/persistence/backup.ts`, `src/persistence/player-save.ts`

### Problem

The backup parser accepts v21 and v22, but the per-field validation chains do not consistently include those versions.

The mismatch is especially severe for v21:

- `PlayerSaveV21` contains inventory, equipment, support spells, characters, luck pity, hidden discovery, credits, progression, expansion currencies, campaign expansion, checkpoint, crash recovery, stage-entry snapshot, shops and route;
- the backup parser validates campaign and route for v21, while many of those other required fields are skipped.

v22 is better covered but still has holes; for example current equipment, progression, expansion currencies, campaign expansion and shops are not all validated in the same way as the surrounding save versions.

After those gaps, `migratePlayerSave()` sanitizes the raw values.

### Condition

A v21/v22 backup is syntactically valid JSON and has a valid campaign/required checked fields, but one of the skipped persistent-state fields is malformed or corrupted.

### Impact

Instead of rejecting the damaged backup before replacement, import can accept it and silently sanitize/reset part of the user's persistent state.

That creates a data-loss mode in the recovery feature itself.

### Root cause

Each field owns a hand-maintained list of schema versions. Version additions were not applied consistently across every validation branch.

### Proposed fix

Define validation by schema version rather than repeated ad-hoc version lists.

For each historical version:

1. validate exactly the fields that version declares;
2. reject malformed required fields;
3. only then migrate/sanitize known-valid legacy shape.

Add focused corruption fixtures for v21 and v22 covering at least inventory, equipment, support/characters, currencies/progression, checkpoint/recovery snapshots and shops. The expected result for malformed required data must be `ok: false`, not silent defaulting.

---

## F20 — Monkeytype dynamic word generation can erase an in-progress multi-word Learning Memory attempt

**Severity:** High  
**Repository:** `sinhvienaiti/monkeytype`  
**Files:** `frontend/src/ts/learning/learning-memory.ts`, `frontend/src/ts/input/helpers/word-navigation.ts`, `frontend/src/ts/test/test-logic.ts`

### Problem

`learning-memory.ts` caches dictionary matches by the current `TestWords.words.length`.

Whenever the word count changes, `rebuildMatchesIfNeeded()` rebuilds the maps **and resets `attemptStates` to a new empty Map**.

A multi-word learning match intentionally stores partial state after the first component word and emits only after the last component word.

But `goToNextWord()` calls `TestLogic.addWord()` between word completions. In long/custom-time tests the generator maintains the ahead buffer by appending words, which changes `TestWords.words.length`.

Therefore an in-progress phrase can be reset between its component words.

### Condition

A dictionary phrase spans multiple Monkeytype words and the dynamic word generator appends another future word after the first phrase component is completed but before the final component is completed.

### Impact

The emitted phrase Learning Event can lose state from the earlier component words:

- `userAnswer` can contain only the final component;
- an error on the first component can be forgotten and the phrase can be reported correct;
- hint/replay flags can be lost;
- `responseMs` can be lost because `presentedAt` was reset.

This pollutes Shared Learning mastery/review data while the existing unit test still passes because its mocked word list length stays static.

### Root cause

Match-cache invalidation and active-attempt lifetime are coupled. A harmless append to the future word buffer is treated like a full learning-session reset.

### Proposed fix

Separate these lifecycles:

- cache the parsed dictionary independently by dictionary raw text;
- when the word list grows, update/rebuild match maps without clearing active attempt state;
- preserve `AttemptState` for still-valid match keys;
- clear attempt state only on actual test restart, dictionary/source replacement, or a match that genuinely became invalid.

Add a regression test that:

1. starts a two-word phrase attempt;
2. records the first component with an error/hint/timestamp;
3. simulates appending an unrelated future word so `TestWords.words.length` changes;
4. completes the second component;
5. asserts one phrase event still contains both user parts, the wrong result, hint/replay state and original response timing.

---

## F21 — Monkeytype EN-VN matching performs repeated full rescans as the word buffer grows

**Severity:** Medium  
**Repository:** `sinhvienaiti/monkeytype`  
**Files:** `frontend/src/ts/test/test-ui.ts`, `frontend/src/ts/learning/learning-memory.ts`, `frontend/src/ts/custom/en-vn-translation/dictionary.ts`

### Problem

Two custom paths repeatedly rebuild phrase matching over the complete growing `TestWords.words` array:

- `getRecallTargetInfo()` reparses the active dictionary and calls `findDictionaryMatches()` over every generated word each time `TestUI.addWord()` renders an appended word;
- `rebuildMatchesIfNeeded()` does another full parse/full scan whenever `TestWords.words.length` changes.

`TestWords.words` only grows during a test; it is not truncated as old words leave the visible area.

### Condition

A long custom/time learning session keeps generating one or more future words while EN-VN learning/recall/listen behavior is active.

### Impact

Matching work grows with the total historical word count rather than the small active/ahead window.

Across a long run this becomes quadratic-style repeated work and unnecessary allocation/parsing, increasing the chance of typing/render stutter exactly in the modes that add translation/recall UI.

### Root cause

The implementation uses whole-test recomputation for an append-only stream even though only a small suffix can be affected by a newly appended word.

### Proposed fix

Use an incremental matcher:

- parse/cache the dictionary once per dictionary change;
- retain `maxWordCount`;
- when a word is appended, recompute only starts within the trailing `maxWordCount - 1` boundary plus the new word;
- update only affected match-map entries;
- if a newly completed multi-word phrase changes the classification of a previously rendered boundary word, retag that word instead of rebuilding the entire test.

Add a performance regression around several thousand appended words and assert dictionary parsing does not occur once per append and matching work stays bounded by the phrase-window size.

---

## F22 — Space Recall Bonus input is starved by the normal enemy target lock

**Severity:** Medium  
**Repository:** `sinhvienaiti/space-typing`  
**File:** `src/Game.ts`  
**Function/module:** `handleKey()`, `currentTarget()`, `typeRecallBonus()`

### Problem

`handleKey()` resolves `currentTarget()` before considering Recall Bonus.

If a normal enemy target is locked, every letter is sent to `typeTarget()` and the function returns immediately. A key that would correctly advance the Recall Bonus never reaches `typeRecallBonus()`.

Even when there is no current lock, normal target acquisition runs before the final first-letter Recall Bonus fallback, so an enemy sharing the same initial key can take the lock first.

Recall Bonus has a finite lifetime and can therefore expire while visible but practically unselectable.

### Condition

A Recall Bonus is active while:

- a normal enemy target is already locked; or
- no target is locked but an enemy competes for the same first key before the bonus starts.

### Impact

The bonus target can be displayed as an available learning/reward opportunity but the keyboard routing prevents the player from intentionally selecting it.

This matches the user-observed U08 behavior.

### Root cause

The input router is a priority-ordered chain with the persistent enemy lock at the top. Recall Bonus is modeled as an auxiliary target rather than participating in a deliberate target-arbitration policy.

### Proposed fix

Introduce explicit target arbitration instead of another one-off conditional.

The policy should preserve an already-valid typing sequence while making the bonus intentionally reachable. A safe direction is:

- keep an already-progressed target when the pressed key is its expected next key;
- otherwise allow an active special target whose expected next key matches to claim the key instead of recording an unrelated enemy miss;
- once the player has started the Recall Bonus, keep that special-target lock until completion/cancel/expiry;
- define deterministic tie behavior when two candidates expect the same key.

If ambiguity remains unacceptable, add an explicit special-target selection action rather than silently stealing input.

Add tests for locked enemy + bonus, shared first letter, bonus already partially typed, enemy expected-key precedence, bonus expiry, and no false enemy miss while intentionally typing the bonus.

---


## F23 — Monkeytype Vietnamese IME handling assumes composition payloads are append-only committed text

**Severity:** High  
**Repository:** `sinhvienaiti/monkeytype`  
**Files:** `frontend/src/ts/input/listeners/composition.ts`, `frontend/src/ts/input/listeners/input.ts`, `frontend/src/ts/input/handlers/insert-text.ts`, `frontend/src/ts/input/helpers/util.ts`

### Problem

The custom Vietnamese path normalizes `compositionend.data` and sends it directly through `onInsertText()` as though it were only the newly appended committed suffix.

That assumption is not guaranteed by browser/OS IME composition. An IME can replace the current composition range in the hidden input while `compositionend.data` represents the final composition string, and the input element may already contain that replacement.

The current multi-character branch then removes `options.data.length` characters from the end of the input and replays the payload character-by-character. This can remove an earlier committed prefix or replay characters against a different event-log position.

The existing Vietnamese unit tests call `onInsertText()` directly through a helper. They do **not** exercise real `compositionstart → compositionupdate/input → compositionend` DOM replacement semantics, so they cannot catch the user-observed sequence where a previously typed letter moves/disappears when `o + o` composes `ô`.

### Condition

A Vietnamese IME commits by replacing an active composition range rather than behaving as a simple appended character stream.

### Impact

Correct Vietnamese input can be scored as wrong, previously committed text can be visually displaced, and the hidden input/event log can diverge.

### Root cause

The custom implementation treats `CompositionEvent.data` as an insertion delta instead of deriving the committed delta from the input value and the composition range/snapshot.

### Proposed fix

Make the composition listener own an explicit snapshot:

1. on `compositionstart`, capture the normalized committed prefix/input state and active word/index;
2. during composition, do not score transient `insertCompositionText` updates;
3. on `compositionend`, read the **actual input element value**, normalize NFC when Vietnamese handling is enabled, and derive the committed replacement/delta relative to the captured pre-composition value;
4. reconcile the hidden input with the event-log-derived committed prefix before replaying only the true committed delta through the scorer;
5. use Unicode code points/grapheme-safe operations for the derived delta;
6. abort/restart safely if the active word changed during composition.

Add browser-shaped regression tests that set realistic input values across composition lifecycle events for at least:

- `T` then Vietnamese composition producing `ô`;
- decomposed `o + combining circumflex`;
- multi-character Vietnamese commits such as `ường`;
- backspace/cancel during composition;
- composition followed by separator/word commit.

---

## F24 — Space Typing still creates killed-enemy learning echo state but no longer renders it

**Severity:** Medium  
**Repository:** `sinhvienaiti/space-typing`  
**File:** `src/Game.ts`

### Problem

Typed enemy completion still assigns `this.learningEcho` with the killed enemy's vocabulary entry, world position and 1.1-second lifetime.

The update loop also continues moving/decrementing that state.

However, the render path has no corresponding draw call for `learningEcho`. The old killed-enemy-position feedback therefore became orphan state/dead rendering logic when the separate top learning strip was introduced.

### Impact

The earlier local-at-kill learning feedback disappears even though the game still pays the update-state cost and the user expects it to remain available.

This exactly explains the observed regression behind U02.

### Root cause

The top-strip feature was added as a replacement presentation while the old runtime state was retained but its render step was removed/not reconnected.

### Proposed fix

Do not simply restore an unconditional duplicate.

Add a persisted presentation mode:

- `off`;
- `top`;
- `kill-position`;
- `both`.

For `top`, keep the latest killed item's IPA/meaning visible until another typed kill replaces it; remove the forced auto-hide timer.

For `kill-position`/ `both`, restore a bounded Canvas draw for `learningEcho` at the kill location and keep its short fade lifetime.

Only **typed** word completions should create learning feedback. Skill/Nova kills must not fabricate typing/learning evidence.

Add tests for mode sanitization and source-level/runtime tests that typed kills populate the correct presentation paths while skill kills do not.

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

Confirmed integrity defects are F01, F03, F04, F06, F15, F18, F19 and F20.

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
- F16: a reentrant Karaoke restart can create multiple RAF loops;
- F21: Monkeytype EN-VN phrase matching repeatedly rescans the complete growing test buffer.

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
- F16: Karaoke restart reentrancy can create duplicate animation loops;
- F22: Recall Bonus can be starved by the normal enemy target lock.

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
- Space v26 backup import compatibility;
- Space v21/v22 malformed backup rejection;
- Monkeytype multi-word attempt state surviving dynamic word-buffer growth;
- bounded/incremental Monkeytype phrase matching for long custom-time runs;
- Space Recall Bonus target arbitration against an active enemy lock;
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
9. F18 + F19 Space backup version compatibility/validation.
10. F20 Monkeytype multi-word attempt-state preservation.
11. F13 Monkeytype Learning Memory target origin + F17 auxiliary message origins.
12. F15 Shooter backup import validation.
13. F16 Karaoke restart generation/RAF ownership.
14. F21 Monkeytype incremental phrase matching/performance.
15. F22 Space Recall Bonus target arbitration.
16. F10 + F14 Portal route/timer lifecycle.
17. F11 drawer keyboard/focus recovery.

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

Therefore the review contains **24 confirmed findings / 8 risks** after the exhaustive pass. The independent self-review verdict is recorded below.

Current GitHub source-of-truth checkpoint for this continued exhaustive pass:

- Parent: `b98a184ac661019f86965f681468ed6048945bc7`
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

**Classification:** likely already corrected in the current pinned code; manual browser verification remains.

The current `kill-translation.css` places the learning strip in a dedicated first CSS-grid row and the `.game-shell`/battlefield in the second row. The code comment explicitly states that the battlefield is resized when the learning row is enabled/disabled, rather than overlaying the Canvas.

Do not add another layout workaround unless current-browser verification still reproduces overlap. Verify desktop/mobile, bosses and bonus targets against the current pin.

## U02 — IPA display behavior must be configurable and persistent

**Classification:** confirmed product/UX gap, not a regression bug.

Current code has one top-strip queue with `enabled`, IPA/Vietnamese toggles, size and a forced 0.8–5.0 second duration. It does not provide killed-enemy-position / both modes and does not keep the last kill indefinitely.

Current desired modes:

- top banner;
- killed-enemy position;
- both;
- off.

The top banner should keep the latest killed target's IPA/meaning until another kill replaces it; it should not auto-hide after a few seconds.

The old killed-enemy-position feedback should remain available instead of being silently replaced by the new banner.

## U03 — Stage result / measured report is too small

**Classification:** current source has already been enlarged; keep as manual UX verification rather than a confirmed source bug.

The pinned CSS now uses `width: min(1040px, calc(100vw - 24px))` and `max-height: min(92vh, 900px)` for the measured result card, with responsive grids. Verify the current browser result before making it larger again.

If the current build still feels cramped, treat the next change as a UX sizing adjustment rather than a logic fix.

## U04 — Settings need explicit Save/Cancel and clear apply semantics

**Classification:** confirmed UX/product-flow gap.

Current settings controls are wired mostly as immediate `input`/`change` mutations that persist directly; the dialog does not provide a transactional draft with explicit Save/Cancel semantics.

**Observed/requested:**

- explicit Save button;
- Cancel/close without accidental changes;
- successful-save feedback;
- dirty/unsaved state;
- clear distinction between immediate, next-stage and stage-reload settings.

Any difficulty/combat-pacing setting that cannot safely update mid-stage must warn the user on Save and, when accepted, reload/restart that stage with the newly saved configuration.

The exhaustive review must verify why current mid-game setting changes appear to have no runtime effect.

## U05 — Stage replay must preserve already-earned persistent progression

**Classification:** confirmed product/spec change; the current checkpoint rollback behavior is intentional code, not an accidental hidden bug.

Current death flow explicitly calls `ensureCheckpointRollback()`, restores `checkpointSnapshot`, rolls Campaign Expansion back to the checkpoint, and describes that behavior in the Game Over UI. `selectCompletedStageForReplay()` is also bounded by the existing checkpoint/progression ceiling.

Requested product rule:

- clearing a stage commits earned persistent progression/rewards;
- replaying an already-cleared stage must not roll back previously earned equipment, XP, loot, unlocks or other persistent progression;
- replay should be usable for farming XP/items;
- remove the old death behavior that sends the player back to checkpoint blocks such as 10/20/30;
- keep only the special in-stage diamond revive that resumes the current encounter after death.

The review must inspect current checkpoint/recovery/replay/reward code before proposing the migration plan.

## U06 — Rage / ship signature skill system needs a clearer model

**Classification:** confirmed product redesign plus a verified gameplay-consistency gap.

Current code already has a distinct ultimate branch for every ship, but every 100%-charge activation also runs the same shared `releaseNovaPulse()`. That shared pulse clears every regular/elite enemy regardless of remaining word layers, while only a subset of normal typed-kill reward/death-trait paths are executed.

The requested redesign should preserve the existing ship identities rather than replacing them: use five 20% Rage segments and make each ship's bound signature Rage ability usable from one filled segment, scaling with the number of segments consumed. At five segments it reaches that ship's full ultimate form. Remove the generic unconditional screen-clear from every ship.

Gameplay reward attribution should go through a shared kill-resolution primitive so score/kill/reward rules are explicit, while Shared Learning and typed-word metrics remain reserved for actual typing evidence.

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

**Classification:** confirmed UX issue.

The equipment renderer adds an `equipment-card-icon` class, but the pinned styles do not define it; the icon falls back to the generic `.local-item-icon` height of 42px. That explains the weak visual hierarchy against the card text.

Keep the current information layout direction, but give equipment cards a dedicated larger artwork slot with responsive sizing and clear containment.

## U08 — Recall bonus target cannot be selected while the normal enemy lock owns input

**Classification:** confirmed bug — promoted to F22.

Code verification shows `Game.handleKey()` routes to `currentTarget()` first and returns immediately, so a locked enemy starves Recall Bonus input. Even without a lock, normal enemy acquisition can win the bonus's first key.

Desired behavior remains: bonus targets must be intentionally typeable and should receive appropriate priority without corrupting an already-valid active typing sequence. See F22 for the proposed arbitration and regression-test plan.

## U09 — Recall hidden-letter cells should be simplified

**Classification:** already implemented in the current pinned source; manual visual verification only.

`recallBonusMask()` currently renders a space-separated character/underscore string such as `M _ _ _`, and `drawRecallBonus()` draws that string as one text line rather than one tiny box per hidden character.

Keep the current outer frame/art direction. Do not reimplement individual cells. If the current build still looks cramped, adjust only the containing mask plate/glow dimensions.

## U10 — Map/background system needs verification and a test selector

**Classification:** the code assumption that later worlds have no distinct background is not supported by the current pinned implementation; remaining work is manual visual verification.

Verified in code:

- the World registry contains distinct environment profiles;
- `Game.startStage()` resolves the world from the stage, replaces `worldEnvironment`, clears the cached background gradient and reseeds stars when the environment changes;
- Test Lab already exposes world/environment selection infrastructure.

Therefore this is not currently a confirmed missing-background bug. Keep it as a browser/manual QA item to verify that every registered environment is visually distinct and that the Test Lab selector exposes them correctly.

## U11 — Recall controls currently sit in the middle of gameplay

**Classification:** confirmed UX issue.

`recallAssistBar` reuses `.boss-hud`, which is absolutely positioned at horizontal center; its override only changes `top` and enables pointer events. It therefore occupies the central combat sightline.

Move Recall assist controls into a dedicated compact edge HUD (desktop top/right or side rail; responsive bottom/edge on narrow screens) instead of inheriting boss positioning.

## U12 — Monkeytype project-added settings need a visible Codex marker

**Classification:** confirmed UX/discoverability issue.

The custom settings currently use normal Monkeytype labels such as `keep first wrong letter`, `ignore repeated blocked errors`, `forgive corrected errors` and `input language`, with no project marker.

Add a consistent `— Codex` suffix (or equivalent small badge rendered by metadata) to every project-added setting, not just one item, while leaving upstream settings unchanged.

## U13 — Monkeytype Vietnamese composed input is broken

**Classification:** confirmed bug — promoted to F23.

The exhaustive input review confirmed that the custom composition path assumes `compositionend.data` is append-only committed text and its tests bypass the real browser composition lifecycle. That assumption can desynchronize the hidden input and event-log position when an IME replaces a composition range.

See F23 for the root cause, replacement/delta-based solution and browser-shaped regression tests.

---


# 15. Independent self-review verdict

A second pass challenged every confirmed finding against the pinned source instead of assuming that the first review was correct.

## Verdict by finding

- **F01 KEEP / High** — event application order can regress timestamps/streaks; fix must preserve monotonic live state without adding an unbounded event log.
- **F02 KEEP / Medium** — repeated full-profile cloning in one batch is real and avoidable; solve together with F12.
- **F03 KEEP / High** — per-tab JS serialization does not make IndexedDB read-modify-write atomic across tabs.
- **F04 KEEP / High** — plain-object entity collections are unsafe for prototype-like user keys; preserve legitimate vocabulary strings rather than banning them.
- **F05 KEEP / Medium** — persistence success and post-persist callback failure are currently conflated.
- **F06 KEEP / High** — structural backup checks omit important cross-field invariants.
- **F07 KEEP / High** — persisted ReviewPlan nested data is trusted after shallow version checks.
- **F08 KEEP / Medium** — structurally valid stale items can still violate the plan/game compatibility contract.
- **F09 KEEP / High** — Mixed/Adaptive persisted state validation is too shallow for its nested progress indices and segment data.
- **F10 KEEP / Medium** — the delayed Dashboard search callback has no route/liveness guard.
- **F11 KEEP / Low** — this is accessibility/UX rather than data correctness, but Escape/focus restoration and dialog semantics are still warranted.
- **F12 KEEP / Medium** — read-only paths clone the complete profile; merge the implementation work with F02.
- **F13 KEEP / Medium** — wildcard Learning Memory target origin exposes learning payloads to an unintended embedding parent. Severity remains above F17 because the payload is richer.
- **F14 KEEP / Medium** — the delayed success callback dereferences the global status element after navigation and can remove the next game's status element.
- **F15 KEEP / High** — Shooter can hold duplicate IDs in memory while IndexedDB `put()` collapses them, so visible/imported count can diverge from reloaded data.
- **F16 KEEP / Medium** — asynchronous restart has no generation guard; two unresolved `play()` calls can start two RAF chains.
- **F17 KEEP / Low** — auxiliary speech/shared-music origin handling is inconsistent. Fix is small and should ride with F13, not become a separate security subsystem.
- **F18 KEEP / High** — v26 migration exists but backup parser rejects v26 before migration.
- **F19 KEEP / High** — v21/v22 validation lists do not match their declared save schemas and can accept malformed required state that migration sanitizes.
- **F20 KEEP / High** — dynamic word-buffer growth resets active multi-word attempt state because match-cache invalidation clears `attemptStates`.
- **F21 KEEP / Medium** — full rescans on an append-only growing word list are real; implement incrementally while fixing F20.
- **F22 KEEP / Medium** — target-routing order demonstrably starves Recall Bonus behind a normal enemy lock.
- **F23 KEEP / High** — direct helper tests do not cover real IME replacement semantics; fix must derive a committed delta from composition snapshots rather than add more normalization patches.
- **F24 KEEP / Medium** — `learningEcho` is written and updated but never drawn; reconnect it only through the new presentation-mode contract.

## Items that should NOT be treated as bugs

The self-review explicitly rejected several tempting fixes:

- **U01:** current pinned CSS already reserves a separate grid row for the top learning strip; do not add another battlefield-offset hack unless current-browser QA still reproduces overlap.
- **U03:** current result card is already up to 1040px wide / 92vh; further enlargement is a UX preference after visual QA, not a confirmed logic defect.
- **U09:** current Recall Bonus mask already uses `M _ _ _` style text; do not rebuild per-letter cells.
- **U10:** multiple world environment profiles are wired into stage start and Test Lab; this remains visual QA, not a missing-background code bug.

## Product/spec changes to implement separately from bug fixes

- **U04:** transactional Settings Save/Cancel, dirty state, saved confirmation and stage-reload warning.
- **U05:** remove checkpoint rollback-on-death and legacy recovery consumables; keep only in-encounter diamond/Phoenix-style revive; cleared-stage replay must preserve/farm persistent progression.
- **U06:** five-segment Rage + ship-bound scalable Rage/ultimate behavior; remove the generic unconditional Nova clear and centralize non-learning kill rewards.
- **U07:** larger dedicated equipment artwork.
- **U11:** move Recall controls out of the central battlefield.
- **U12:** mark every project-added Monkeytype setting with Codex identity.

## Final review state

The exhaustive custom-code review and second-pass self-review are **COMPLETE** at this checkpoint.

Implementation may now start. The fix phase must preserve this distinction:

- correctness/security/data/performance findings F01–F24 receive regression coverage where practical;
- product changes U04/U05/U06/U07/U11/U12 receive behavior/UX tests appropriate to their scope;
- U01/U03/U09/U10 are not to be "fixed" blindly unless current-build visual QA still reproduces the problem.


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

No source implementation fix is included up to this review-finalization checkpoint. The following commits may begin implementation only after this report commit.


---

# 16. Post-review implementation completion

The implementation phase following this review is complete for the accepted review fixes and requested product corrections covered by this pass.

Validated integrated child revisions:

~~~text
Monkeytype      8e49127c1eb51000323bbda3b750d3a292fbf567
Vocabulary      4618f3bcdeb5f72bde8e28587ae23d3567bdb05d
Recall          27ded35809c1d2e37eabc1a91c34b907b95c2219
Karaoke         d88d64f01e66fd41ed1eef1a4cf743b76bb0bbe3
Space           d7ec4858a0c046799b49eb246f6fa7d875fc7b1b
~~~

Parent integration checkpoint before this documentation commit:

~~~text
2e921e38d38b0433f8cc54938fab17102ea92b4f
~~~

The implementation includes the confirmed correctness/security/data/performance fixes from the review batch and the verified user-requested corrections implemented during this phase, including U02/U04/U05/U06/U07/U08/U11/U12/U13.

U01/U03/U09/U10 were deliberately not changed merely because they appeared in the user-observed list: the independent review found the current source already contains the relevant layout/result/mask/background behavior, so they remain current-build manual visual QA items.

Important U05 compatibility rule:

- old `salvage-anchor` and `stage-revival-core` IDs remain readable for save/schema compatibility;
- they are no longer generated as current shop death-recovery stock and are no longer offered by the Game Over flow;
- Phoenix Core remains the generated in-encounter revive path;
- normal defeat/replay preserves persistent progression instead of rolling back to checkpoint blocks.

Important U06 rule:

- Rage has five 20% segments;
- SPACE spends the currently completed segments and scales the selected ship's signature Rage;
- a five-segment activation is the full ship ultimate;
- the generic unconditional Nova screen clear is no longer attached to every ship ultimate;
- Nova Bomb remains its own consumable;
- skill/consumable kills receive explicit gameplay reward attribution without being reported as typed Shared Learning success.

Validation:

- Space Typing standalone CI passed tests, TypeScript, Vite build, bundle budget and ship-art budget at `d7ec4858a0c046799b49eb246f6fa7d875fc7b1b`.
- CSS raw output was `59.99 KiB` against the existing `60.00 KiB` budget; the budget was not raised.
- Parent Platform CI passed at `2e921e38d38b0433f8cc54938fab17102ea92b4f`, including platform contracts, Recall tests/build, Space tests/build and Portal build.

Future review or implementation must start from the current parent `main` and pinned child gitlinks, not from the pre-fix review checkpoint.
