# English Learning Content System — Progress

Status: SCALE_UP_ACTIVE

## Current checkpoint

- Working branch: `feature/english-learning-content-system`
- Current HEAD: resolve the branch HEAD from GitHub at the start of every run. Do not hard-code the checkpoint file's own commit SHA because updating this file changes HEAD.
- Latest fully CI-verified scale-up state before scale-210 publication: `0d1a0516ce86b29d82edf9ee7154d14e5449f03a` — scale-209 publication checkpoint verified by English Content Full Validation, English Content Master Plan Acceptance and Platform CI; scale-209 published output: `b746e173536e621996a74610bde1261babc89f60`.
- Scale-209 publication state at `0d1a0516ce86b29d82edf9ee7154d14e5449f03a` is fully verified; scale-210 is the active publication unit.
- Scale-210 source/apply publication is active; after bot publication create exactly one normal-user checkpoint before opening the next safe scale-up unit.
- Current phase: mandatory E00–E12 implementation is complete; approved quality-first E04/E11 content scale-up is active.
- PR: #48 — open, draft, mergeable
- Published runtime release: `2026.10.0`

The scheduled/manual worker must always resolve the newest branch HEAD and its workflows directly from GitHub before doing work. If a newer commit exists, adopt it, inspect its changes, preserve completed work, and never reset/revert/overwrite/duplicate it.

## Completed mandatory milestones

- E00–E02 foundation/contracts: complete
- E03 controlled lexical pilot: complete — 300 lexemes + 300 linked primary senses + 300 usage sidecars
- E04 phrase/pattern architecture + current reviewed publication: complete — 9,150 published records after scale-210
- E05 grammar framework/runtime: complete — 300/300 topics (45 A1 + 50 A2 + 60 B1 + 60 B2 + 50 C1 + 35 C2)
- E06 controlled sentence/exercise/dialogue/mistake pilots: complete — 1,513 examples + 1,400 exercises + 100 dialogues + 388 reviewed common mistakes
- E07–E09 parent runtime, `/english` launcher, and game capability integrations: complete
- E10 controlled batch/review pipeline: complete and enforced
- E11 readiness/reporting contracts: complete; corpus scale-up remains active work
- E12 release/audit/maintenance foundation: complete and enforced

## Published runtime snapshot after E04 scale-210 publication

- dictionary: 900 records
- grammar: 300 records
- sentences: 3,401 records
- phrases: 9,150 records
- total published rich records: 13,751
- attribution runtime: 4 source records
- editorial ledger: 13,751 decisions / 13,751 applied / 13,751 publish decisions
- E04 collocation frontier: `col.00005000`
- E04 phrasal-verb frontier: `pv.00001000`
- E04 chunk frontier: `chunk.00001455`
- E04 idiom frontier: `idiom.00001185`

## Approved scale-up targets

Current repository/master-plan data always outranks these checkpoint numbers. Recalculate from HEAD before every new batch.

Priority order:

1. E04 evidence-backed example-link enrichment for existing collocations, verb patterns, phrasal verbs, idioms and chunks.
2. E04 scale-up toward long-term lexical-unit targets while preserving reviewed provenance/license gates:
   - verb patterns: 500–1,000 target range; current runtime already exceeds the 500 minimum at 510, so prioritize other under-target families unless valid reviewed evidence is ready;
   - collocations: 5,000+; current frontier is 5,000, so the minimum is met;
   - phrasal verbs: 1,000+; current frontier is 1,000, so the minimum is met; prioritize other under-target families unless valid reviewed phrasal evidence is ready;
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

1. Scale-209 publication checkpoint `0d1a0516ce86b29d82edf9ee7154d14e5449f03a` is fully verified; do not duplicate scale-209 artifacts.
2. Scale-210 is the active publication unit; do not start the next scale-up unit until its bot publication, one normal-user checkpoint and all three mandatory CI gates complete.
3. Scale-210 adds a bounded 40-record chunk-only batch because the phrasal-verb and collocation minimums are already met while chunks remain under target, advancing the expected publication frontiers to `pv.00001000` / `chunk.00001455` / `idiom.00001185`; near-dedupe threshold remains `0.86`.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. Reuse the established scale-up workflow and preserve exact/near-dedupe, provenance, review, deterministic publication and runtime gates.
6. After scale-210 bot publication, create exactly one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.
7. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
8. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.

## Known non-blocking enrichment debt

Many E04 items still lack `exampleIds`. These are not errors and must not be auto-filled from unsafe lemma-only matches. Treat them as an evidence/review queue: link only when whole-phrase/frame evidence is valid and reviewable.

## Blocker

None.

## Next actionable task

Finish the active Scale-210 chunk-only apply/publish pipeline through deterministic verification and bot publication. Then create exactly one normal-user tree-identical checkpoint and verify English Content Full Validation + Master Plan Acceptance + Platform CI on that checkpoint. If all three PASS, recalculate live deficits and continue with the next safe E04 or E11 unit without changing the `0.86` threshold.
