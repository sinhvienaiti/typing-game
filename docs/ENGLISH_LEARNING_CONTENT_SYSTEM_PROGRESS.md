# English Learning Content System — Progress

Status: SCALE_UP_ACTIVE

## Current checkpoint

- Working branch: `feature/english-learning-content-system`
- Current HEAD: resolve the branch HEAD from GitHub at the start of every run. Do not hard-code the checkpoint file's own commit SHA because updating this file changes HEAD.
- Latest fully CI-verified hardening checkpoint before the current Tatoeba next-slice work: `f3e1dd43d5468c936cea8d5b0880ce3669da862c` — English Content Full Validation passed with E11 readiness freshness, exact runtime-count reconciliation, exact record-level runtime coverage, E12 maintenance, enrichment reporting and reproducibility checks.
- E04 scale-224 publication is complete. Do not recreate scale-223/scale-224 artifacts or reopen the 2,000-chunk completion batch.
- Current phase: mandatory E00–E12 implementation is complete; approved quality-first E11 corpus scale-up is the first unfinished workstream. E04 may continue only when new evidence-backed reviewed enrichment/content is actually available.
- PR: #48 — open, draft, mergeable
- Published runtime release: `2026.10.0`

The scheduled/manual worker must always resolve the newest branch HEAD and its workflows directly from GitHub before doing work. If a newer commit exists, adopt it, inspect its changes, preserve completed work, and never reset/revert/overwrite/duplicate it.

## Completed mandatory milestones

- E00–E02 foundation/contracts: complete
- E03 controlled lexical pilot: complete — 300 lexemes + 300 linked primary senses + 300 usage sidecars
- E04 phrase/pattern architecture + current reviewed publication: complete — 9,695 published records after scale-224
- E05 grammar framework/runtime: complete — 300/300 topics (45 A1 + 50 A2 + 60 B1 + 60 B2 + 50 C1 + 35 C2)
- E06 controlled sentence/exercise/dialogue/mistake pilots: complete — 1,513 examples + 1,400 exercises + 100 dialogues + 388 reviewed common mistakes
- E07–E09 parent runtime, `/english` launcher, and game capability integrations: complete
- E10 controlled batch/review pipeline: complete and enforced
- E11 readiness/reporting contracts: complete; corpus scale-up remains active work
- E12 release/audit/maintenance foundation: complete and enforced

## Published runtime snapshot after E04 scale-224 publication

- dictionary: 900 records
- grammar: 300 records
- sentences: 3,401 records
- phrases: 9,695 records
- total published rich records: 14,296
- attribution runtime: 4 source records
- editorial ledger: 14,296 decisions / 14,296 applied / 14,296 publish decisions
- E04 collocation frontier: `col.00005000`
- E04 phrasal-verb frontier: `pv.00001000`
- E04 chunk frontier: `chunk.00002000`
- E04 idiom frontier: `idiom.00001185`

## Current E11 readiness snapshot

Recalculate from live HEAD before every new batch; these values are a handoff snapshot, not a substitute for the generated readiness/runtime reports.

- grammar topics: 300
- verb patterns: 510
- collocations: 5,000
- phrasal verbs: 1,000
- idioms/chunks: 3,185
- common mistakes: 388
- example sentences: 1,513
- translation pairs: 600
- cloze exercises: 600
- sentence transformations: 100
- dialogue examples: 100
- legacy typing texts: 300; this runtime metric has no separate locked E11 long-term target

## Approved scale-up targets

Current repository/master-plan data always outranks these checkpoint numbers. Recalculate from HEAD before every new batch.

Priority order:

1. E04 evidence-backed example-link enrichment for existing collocations, verb patterns, phrasal verbs, idioms and chunks when valid reviewable evidence exists. Do not create enrichment merely to keep E04 active.
2. E04 long-term minimums are currently reached for the controlled phrase families:
   - verb patterns: 510, above the 500 minimum;
   - collocations: 5,000, minimum reached;
   - phrasal verbs: 1,000, minimum reached;
   - idioms/chunks: 3,185 combined, above the 2,000 minimum; chunk frontier is exactly 2,000.
3. E11 sentence/exercise corpus scale-up is now the first unfinished capacity work:
   - example sentences: 100,000+;
   - translation pairs: 20,000+;
   - cloze exercises: 30,000+;
   - transformations: 10,000+;
   - dialogues: 10,000+;
   - common mistakes: 2,000+.
4. Add source-specific importers only when source snapshot/version/checksum/license/provenance obligations are pinned and validation support exists.
5. Preserve the legacy `shared/vocabulary/levels/*.json` ABI unless a separately approved compatibility migration changes it.

These are scale targets, not permission to bulk-generate unchecked content. Quality gates remain mandatory for every promoted record.

## Mandatory anti-duplicate resume procedure

Before creating or modifying any scale-up batch, the worker MUST perform this sequence:

1. Resolve current remote HEAD for `feature/english-learning-content-system` and read newest commits since the previous checkpoint/run.
2. Check workflows for that HEAD. If the same scope already has CI queued/in-progress, do not create duplicate work; only continue an independent safe unit.
3. Read this progress file and the relevant E04/E10/E11/E12 sections of `docs/ENGLISH_LEARNING_CONTENT_SYSTEM_MASTER_PLAN.md`.
4. Read the current controlled batch manifest, target/readiness report, source/review manifests and runtime manifests relevant to the intended record type. Do not trust numeric counts copied from old prompts.
5. Inspect the stable ID registry and existing source/candidate/review/runtime records for the intended scope.
6. Before assigning a batch ID, record ID, source key or normalized text, verify it does not already exist in active/superseded controlled batches, source/candidate files, review queues/decisions, published runtime, stable ID registry, and exact/near-dedupe reports.
7. Recalculate the actual current target deficit from HEAD. If the target/family is already complete, skip it and move to the next first-unfinished target.
8. Reuse existing generation/apply/publish tooling where available. Never recreate or regenerate unchanged completed slices merely to produce a new commit.
9. For third-party-derived content, verify pinned source/version/checksum/license/attribution/provenance before generation. License-uncertain data cannot be promoted.
10. Generate only a bounded next batch. Run schema/source/reference/exact-dedupe/near-dedupe validation before review.
11. Review/promote only digest-bound records. Candidate/generated content must never bypass editorial review into runtime.
12. Regenerate only affected runtime scope, then run publication reproducibility, runtime smoke, E10 batch validation, E11 readiness and E12 maintenance/audit gates.
13. Commit/push valid changes, verify remote HEAD, then verify English Content Full Validation, Master Plan Acceptance and Platform CI for the resulting HEAD.
14. If any gate fails, inspect the exact failed step/log, fix the source/generator/apply logic without weakening validators, and re-run.
15. Update this checkpoint only when real state changes: completed batch, changed runtime counts, new blocker, changed next target, or verified new milestone. Never make timestamp-only or self-referential CI-refresh commits.

## Current milestone

`E11 CORPUS SCALE-UP ACTIVE`

Mandatory architecture/pilot implementation is complete. The active work is quality-first content expansion toward the approved E11 long-term targets.

## Current first-unfinished workstream

1. E04 scale-224 is complete; all controlled E04 phrase-family minimums are met. Do not create scale-225 merely for volume.
2. Translation pairs are the current bounded E11 scale-up front: runtime is 600 against the locked 20,000 target, and the repository already has a pinned Tatoeba source/review pipeline.
3. The legacy Tatoeba E06 pilot selector uses `selectEvenly(candidates, limit)`. Increasing its limit is unsafe for scale-up because a new limit can reshuffle the previously selected 300 pairs. Keep that pilot behavior unchanged for reproducibility.
4. The E11 path now uses a separate source-ID-based, prefix-monotonic next-slice selector. It excludes Tatoeba pair identities already present in controlled batch-manifest record sets and never derives identity from editable English/Vietnamese text.
5. Use `pnpm english-content:e11:translation:next -- --limit=24` to prepare the default bounded next review packet when, and only when, the local `.cache/english-content/tatoeba/` files match the checksums in `content/english/sources/tatoeba-eng-vie-pilot.json`.
6. The Tatoeba URLs in the pin are moving export URLs. A newly downloaded current export is not automatically the pinned historical snapshot. Never update the pin or accept a checksum mismatch merely to make the command run.
7. The next-slice output is candidate-only. Do not add it to runtime or mark it published until a controlled E10 batch and digest-bound bilingual/naturalness/CEFR/license review have completed.
8. After a reviewed bounded Tatoeba slice is integrated, regenerate publication, E11 readiness/runtime/record-level coverage and E12 artifacts, then verify all mandatory CI gates before opening the following slice.

## Known non-blocking enrichment debt

Many E04 items still lack `exampleIds`. These are not errors and must not be auto-filled from unsafe lemma-only matches. Treat them as an evidence/review queue: link only when whole-phrase/frame evidence is valid and reviewable.

## Blocker

The next Tatoeba candidate slice requires access to the exact pinned source-cache bytes. This is a source-availability constraint, not permission to refresh/re-pin the moving upstream export. Core selector/preparer development and validation can continue without weakening this constraint.

## Next actionable task

With exact pinned Tatoeba cache bytes available, run the bounded E11 translation next-slice preparer (default 24 pairs), inspect the generated source IDs and candidate records, then create the controlled E10 batch/review artifacts for that slice. Keep every new record non-published until digest-bound bilingual, naturalness, CEFR and license review passes. If the pinned cache is unavailable, continue with another E11 family that has reproducible committed/pinned source material rather than fetching a newer Tatoeba export under the old pin.
