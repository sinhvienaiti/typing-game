# English Learning Content System — Progress

Status: SCALE_UP_ACTIVE

## Current checkpoint

- Working branch: `feature/english-learning-content-system`
- Current HEAD: resolve the branch HEAD from GitHub at the start of every run. Do not hard-code the checkpoint file's own commit SHA because updating this file changes HEAD.
- Latest bot publication commit: `0af400dcc97be0de6d99bb08ec84c92980ef1ba9` — `feat(content): publish E04 phrase scale 176`.
- Scale-176 publication has completed all apply-workflow gates; this single normal-user checkpoint must be verified by English Content Full Validation, English Content Master Plan Acceptance and Platform CI before the next E04 batch is opened.
- Current phase: mandatory E00–E12 implementation is complete; approved quality-first E04/E11 content scale-up is active.
- PR: #48 — open, draft, mergeable
- Published runtime release: `2026.10.0`

The scheduled/manual worker must always resolve the newest branch HEAD and its workflows directly from GitHub before doing work. If a newer commit exists, adopt it, inspect its changes, preserve completed work, and never reset/revert/overwrite/duplicate it.

## Completed mandatory milestones

- E00–E02 foundation/contracts: complete
- E03 controlled lexical pilot: complete — 300 lexemes + 300 linked primary senses + 300 usage sidecars
- E04 phrase/pattern architecture + current reviewed publication: complete — 7,790 published records after scale-176
- E05 grammar framework/runtime: complete — 300/300 topics (45 A1 + 50 A2 + 60 B1 + 60 B2 + 50 C1 + 35 C2)
- E06 controlled sentence/exercise/dialogue/mistake pilots: complete — 1,513 examples + 1,400 exercises + 100 dialogues + 388 reviewed common mistakes
- E07–E09 parent runtime, `/english` launcher, and game capability integrations: complete
- E10 controlled batch/review pipeline: complete and enforced
- E11 readiness/reporting contracts: complete; corpus scale-up remains active work
- E12 release/audit/maintenance foundation: complete and enforced

## Published runtime snapshot after E04 scale-176 publication

- dictionary: 900 records
- grammar: 300 records
- sentences: 3,401 records
- phrases: 7,790 records
- total published rich records: 12,391
- attribution runtime: 4 source records
- editorial ledger: 12,391 decisions / 12,391 applied / 12,391 publish decisions
- E04 collocation frontier: `col.00005000`
- E04 phrasal-verb frontier: `pv.00000720`
- E04 chunk frontier: `chunk.00000795`
- E04 idiom frontier: `idiom.00000765`

## Approved scale-up targets

Current repository/master-plan data always outranks these checkpoint numbers. Recalculate from HEAD before every new batch.

Priority order:

1. E04 evidence-backed example-link enrichment for existing collocations, verb patterns, phrasal verbs, idioms and chunks.
2. E04 scale-up toward long-term lexical-unit targets while preserving reviewed provenance/license gates:
   - verb patterns: 500–1,000 target range; current runtime already exceeds the 500 minimum at 510, so prioritize other under-target families unless valid reviewed evidence is ready;
   - collocations: 5,000+; current frontier is 5,000, so the minimum is met;
   - phrasal verbs: 1,000+; current frontier is 720, leaving a minimum deficit of 280;
   - idioms/chunks: 2,000+ long-term scale target; continue bounded reviewed idiom/chunk batches while the target remains unmet.
3. E11 sentence/exercise corpus scale-up:
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

`E04/E11 SCALE-UP ACTIVE`

Mandatory architecture/pilot implementation is complete. The active work is quality-first content expansion toward the approved long-term targets.

## Current first-unfinished workstream

1. Scale-176 bot publication is complete at `0af400dcc97be0de6d99bb08ec84c92980ef1ba9`; do not duplicate scale-176 artifacts.
2. Verify this single normal-user checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI.
3. After all three mandatory CI workflows PASS, recalculate deficits from the resulting HEAD and open the next bounded E04 unit (Scale-177) for under-target phrasal verbs, idioms and chunks unless safer reviewed enrichment has become available.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. Reuse the established scale-up workflow and keep the batch bounded; preserve exact/near-dedupe, provenance, review, deterministic publication and runtime gates.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.

## Known non-blocking enrichment debt

Many E04 items still lack `exampleIds`. These are not errors and must not be auto-filled from unsafe lemma-only matches. Treat them as an evidence/review queue: link only when whole-phrase/frame evidence is valid and reviewable.

## Blocker

None.

## Next actionable task

Verify this Scale-176 normal-user checkpoint against English Content Full Validation, English Content Master Plan Acceptance and Platform CI. Once all three PASS, continue immediately with Scale-177: recalculate live deficits from HEAD, use the next safe IDs after `pv.00000720`, `chunk.00000795` and `idiom.00000765`, generate one bounded reviewed batch, run exact/near dedupe before publication, and drive the full apply/publish/CI pipeline to completion.
