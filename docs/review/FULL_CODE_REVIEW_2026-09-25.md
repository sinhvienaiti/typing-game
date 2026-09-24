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

The review used three passes:

1. Correctness, cross-game contracts and data integrity.
2. Performance, lifecycle/recovery, UI/UX and security.
3. Regression review of the findings and proposed solutions.

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

The confirmed security inconsistency is specifically Monkeytype's *normal Learning Memory attempt sender* using wildcard target origin (F13).

## Mixed / Adaptive progress

The core parent design—advance only after persisted Learning Events and only for the launched concrete segment—is sound.

The confirmed reliability gap is stale/malformed persisted orchestration state (F09), not the normal happy-path segment-matching logic.

---

# 6. Data integrity review result

Confirmed integrity defects are F01, F03, F04 and F06.

Additional observations:

- vocabulary normalization uses NFKC + trim + collapsed whitespace + lowercase in the parent;
- event optional text is NFC-normalized;
- L18 already added stricter canonical backup-key validation;
- selective reset is scoped by entity group and preserves unselected collections;
- reset/import clear transient review queues to avoid running stale datasets against replaced profile state.

No additional confirmed silent-delete path was found in selective reset beyond the findings listed above.

---

# 7. Performance review result

Confirmed performance findings:

- F02: repeated full-profile cloning inside event batches;
- F12: deep cloning for read-only Dashboard/Builder operations.

The architecture still performs full collection filtering/sorting for many Dashboard operations. That is expected for the current local profile model and is not by itself classified as a bug.

For 5,000–10,000 records the existing approach is reasonable after removing duplicated cloning. Around 50,000 records, query/sort remains O(n log n) for sort-heavy views; pagination bounds returned DOM/data but does not avoid scanning the source collection.

**Recommendation:** first remove duplicate cloning. Do not add indexing/caching complexity unless real measurements after that still show an interactive latency problem.

---

# 8. UI / UX review result

Confirmed UI/UX issues:

- F10: stale debounced search callback after navigation;
- F11: incomplete drawer keyboard/focus recovery.

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

No additional confirmed broken-button or overflow defect was established from source evidence alone in this pass.

Visual responsive verification remains best done in a browser/E2E pass rather than labeling source-only suspicions as bugs.

---

# 9. Security / input-boundary review result

Confirmed boundary issues:

- F04: prototype-like collection keys;
- F06: insufficient backup invariants;
- F13: wildcard Monkeytype attempt target origin.

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
- multi-tab IndexedDB read-modify-write behavior.

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
9. F13 Monkeytype target origin.
10. F10 Dashboard debounce lifecycle.
11. F11 drawer keyboard/focus recovery.

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
