# Shared Learning Core

This folder owns the parent-platform learning contract and deterministic learning calculations.

## Versioning

- Learning Event: v1
- Learning Profile: v1
- IndexedDB database: `typingGameLearning`
- object store: `state`
- canonical profile key: `profile`
- recent mistake/answer bound: 8 samples per item

Child games must emit learning attempts. They must not independently calculate a competing canonical mastery score.

## Vocabulary identity

Vocabulary IDs use the same canonical rule as the shared vocabulary library:

```text
NFKC
-> trim
-> collapse whitespace
-> lowercase
```

EN/VI/IPA stay in `shared/vocabulary`; learning records store only the normalized key and aggregate history.

## Profile entities

The profile has three maps:

- `vocabulary`
- `grammar`
- `sentences`

Common aggregates include attempts, correct/wrong counts, hint/replay counts, average response time, correct streak, last-seen/correct/wrong timestamps, mastery, review priority, next-review time and source games.

Grammar/sentence records also keep bounded error classifications. Sentence records keep bounded recent answers.

## Mastery v1

Mastery is deterministic and clamped to 0-100. It is a learning-strength indicator, not a literal percentage of knowledge.

Weights:

- correctness: 55
- correct streak: 20
- response speed: 10
- independence from hints/replays: 10
- recent successful recall: 5

## Review priority v1

Review priority is deterministic and clamped to 0-100.

Signals:

- low mastery: up to 55
- accumulated failures: up to 20
- staleness since successful recall: up to 15
- slow response: up to 5
- hint/replay dependence: up to 5

Initial next-review intervals are intentionally simple and deterministic:

- mastery 0-39: due now
- 40-69: +1 day
- 70-89: +3 days
- 90-100: +7 days

Later milestones may evolve the formula only through an explicit profile/event versioned migration.

## Persistence

`browser-store.mjs` persists the canonical parent profile in IndexedDB.

Writes are serialized so concurrent parent operations do not overwrite one another. Learning is recorded per completed attempt/event, not per physical keystroke.

L02 adds the cross-origin messaging bridge and batching/query API.

## Verification

Run:

```bash
pnpm learning:check
pnpm learning:test
```

The tests cover event validation, vocabulary key normalization, deterministic aggregates, bounded history, grammar error classification, sentence answer history and review-priority ordering.
