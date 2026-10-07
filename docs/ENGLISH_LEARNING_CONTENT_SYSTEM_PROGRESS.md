# English Learning Content System — Progress

Status: SCALE_UP_ACTIVE

## Current checkpoint

- Working branch: `feature/english-learning-content-system`
- Current HEAD: resolve the branch HEAD from GitHub at the start of every run. Do not hard-code the checkpoint file's own commit SHA because updating this file changes HEAD.
- Latest fully CI-verified scale-up checkpoint before scale-37 publication: `3e0741ca8684a9e0d8f98f9150a31dbeaa52632c` — scale-36 publication state verified by English Content Master Plan Acceptance #78, English Content Full Validation #86 and Platform CI #1121; published output: `ebcc481a41fc89499f566140aee0b69227070aef`.
- Latest published scale-up HEAD before this checkpoint: `d76454a30225b0dc1c4c85238b834e24afaa1b35` — `feat(content): publish E04 collocation scale 37`.
- Latest scale-37 pre-publication HEAD: `bbfaa70835fbc7532b74a3299fb32fe3141cc910` — Apply English E04 Scale 37 #2 passed preflight, source apply, review/E10/license, generate/publish, full quality gates, converge, deterministic replay and bot commit/push. Run #1 stopped at preflight on three exact duplicates; those candidates were replaced without weakening the 0.86 threshold or applying partial content state.
- Current phase: mandatory E00–E12 implementation is complete; approved quality-first E04/E11 content scale-up is now active.
- PR: #48 — open, draft, mergeable
- Published runtime release: `2026.10.0`
- Scale-37 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #81 and Platform CI #1124 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the mandatory CI from a normal branch write without regenerating scale-37 content or weakening any gate.

The scheduled/manual worker must always resolve the newest branch HEAD and its workflows directly from GitHub before doing work. If a newer commit exists, adopt it, inspect its changes, preserve completed work, and never reset/revert/overwrite/duplicate it.

## Completed mandatory milestones

- E00–E02 foundation/contracts: complete
- E03 controlled lexical pilot: complete — 300 lexemes + 300 linked primary senses + 300 usage sidecars
- E04 phrase/pattern architecture + current reviewed publication: complete — 2,230 published records after scale-37
- E05 grammar framework/runtime: complete — 300/300 topics (45 A1 + 50 A2 + 60 B1 + 60 B2 + 50 C1 + 35 C2)
- E06 controlled sentence/exercise/dialogue/mistake pilots: complete — 1,513 examples + 1,400 exercises + 100 dialogues + 388 reviewed common mistakes
- E07–E09 parent runtime, `/english` launcher, and game capability integrations: complete
- E10 controlled batch/review pipeline: complete and enforced
- E11 readiness/reporting contracts: complete; corpus scale-up remains active work
- E12 release/audit/maintenance foundation: complete and enforced

## Published runtime snapshot after E04 scale-37 publication

- dictionary: 900 records
- grammar: 300 records
- sentences: 3,401 records
- phrases: 2,230 records
- total published rich records: 6,831
- attribution runtime: 4 source records
- editorial ledger: 6,831 decisions / 6,831 applied / 6,831 publish decisions
- E04 collocation frontier: `col.00001120`

## Approved scale-up targets

Current repository/master-plan data always outranks these checkpoint numbers. Recalculate from HEAD before every new batch.

Priority order:

1. E04 evidence-backed example-link enrichment for existing collocations, verb patterns, phrasal verbs, idioms and chunks.
2. E04 scale-up toward long-term lexical-unit targets while preserving reviewed provenance/license gates:
   - verb patterns: 500–1,000 target range; current runtime already exceeds the 500 minimum at 510, so prioritize other under-target families unless valid reviewed evidence is ready;
   - collocations: 5,000+;
   - phrasal verbs: 1,000+;
   - idioms/chunks: 2,000+ long-term scale target.
3. E11 sentence/exercise corpus scale-up:
   - example sentences: 100,000+;
   - translation pairs: 20,000+;
   - cloze exercises: 30,000+;
   - transformations: 10,000+;
   - dialogues: 10,000+;
   - common mistakes: 2,000+.
4. Add source-specific importers only when source snapshot/version/license/provenance obligations are pinned and validation support exists.
5. Preserve the legacy `shared/vocabulary/levels/*.json` ABI unless a separately approved compatibility migration changes it.

These are scale targets, not permission to bulk-generate unchecked content. Quality gates remain mandatory for every promoted record.

## Mandatory anti-duplicate resume procedure

Before creating or modifying any scale-up batch, the worker MUST perform this sequence:

1. Resolve current remote HEAD for `feature/english-learning-content-system` and read newest commits since the previous checkpoint/run.
2. Check workflows for that HEAD. If the same scope already has CI queued/in-progress, do not create duplicate work; only continue an independent safe unit.
3. Read this progress file and the relevant E04/E10/E11/E12 sections of `docs/ENGLISH_LEARNING_CONTENT_SYSTEM_MASTER_PLAN.md`.
4. Read the current controlled batch manifest, target/readiness report, source/review manifests and runtime manifests relevant to the intended record type. Do not trust numeric counts copied from old prompts.
5. Inspect the stable ID registry and existing source/candidate/review/runtime records for the intended scope.
6. Before assigning a batch ID, record ID, source key or normalized text, verify it does not already exist in:
   - active/superseded controlled batches;
   - source/candidate authoring files;
   - review queues and digest-bound review decisions;
   - published `shared/**` runtime;
   - stable ID registry;
   - exact/near-dedupe reports.
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

Start with E04 because it has the smallest, safest incremental units and already has controlled generators/review/runtime gates.

1. Verify scale-37 publication state through this normal-user checkpoint CI; do not duplicate scale-37 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-37 checkpoint CI passes and no newer worker has claimed the next scope, create scale-38 as the next bounded collocation batch from frontier `col.00001120`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.

## Known non-blocking enrichment debt

Many E04 items still lack `exampleIds`. These are not errors and must not be auto-filled from unsafe lemma-only matches. Treat them as an evidence/review queue: link only when whole-phrase/frame evidence is valid and reviewable.

## Blocker

No content/data blocker. Scale-37 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content.

## Next actionable task

Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-37 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001120` (expected scale-38 range `col.00001121` through `col.00001160` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.
