# English Learning Content System — Progress

Status: SCALE_UP_ACTIVE

## Current checkpoint

- Working branch: `feature/english-learning-content-system`
- Current HEAD: resolve the branch HEAD from GitHub at the start of every run. Do not hard-code the checkpoint file's own commit SHA because updating this file changes HEAD.
- Latest fully verified E11 editorial checkpoint: `a6b1844774cb9a9b1826f4a7ed348af507f67868` — English Content Full Validation #913 passed the complete MultiWOZ E11 slice-51 editorial decision set. That run applied the decisions and registered the reviewed slice; the workflow then created registration commit `b9400e88f2c498b8524137aa2317d32ab87b0f81`, followed by generated-metadata commit `9803698754f07d7023bde774b13c249eb8309d91`.
- MultiWOZ slice 51 is integrated: 22/22 candidates received explicit editorial decisions, with 9 edited records retained and 13 rejected. The registered runtime slice is `content/english/sentences/e11-multiwoz-dialogue-reviewed-slice-51.json`.
- The pinned MultiWOZ 2.2 source coverage now includes the complete configured source set at immutable upstream commit `fe0c8e65cfcd8462bd33c86e35f21addc84ca82b`: train `dialogues_001.json` through `dialogues_017.json`, dev `dialogues_001.json` and `dialogues_002.json`, and test `dialogues_001.json` and `dialogues_002.json`. There is no configured or upstream-designed `test/dialogues_003.json` lane; never invent one.
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

## Historical runtime snapshot after E04 scale-224 publication

These values are the scale-224 baseline only. MultiWOZ E11 reviewed slices have subsequently changed sentence/dialogue-related runtime state. Recalculate current counts from live generated manifests/reports before planning any new batch; do not use these historical values as the current runtime total.

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

## Historical E11 readiness baseline

Recalculate from live HEAD before every new batch; these values predate the later MultiWOZ reviewed slices and are a handoff baseline, not a substitute for generated readiness/runtime reports.

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
2. Translation pairs remain the largest preferred bounded E11 scale-up front because runtime is far below the locked 20,000 target and a Tatoeba source/review pipeline exists. However, the exact pinned Tatoeba cache bytes are not currently available through the reproducible repository/CI path, so this lane remains source-blocked rather than license/review-blocked.
3. Keep the legacy Tatoeba E06 pilot selector unchanged. The E11 Tatoeba path uses the separate source-ID-based, prefix-monotonic selector and must reject checksum drift instead of silently refreshing moving export URLs.
4. MultiWOZ dialogue scale-up remains the current reproducible fallback lane. The pipeline has progressed through 51 reviewed slices using immutable source identity, explicit editorial decisions, digest-bound review, normal E10 publication gates and bot registration/metadata refreshes.
5. The configured MultiWOZ source has been extended through the last designed file currently pinned for this lane: train 001–017, dev 001–002 and test 001–002. Source pin, blob SHA1s, license and attribution remain immutable/reproducible at the pinned upstream commit.
6. Full Validation #913 verified slice 51 and registered it, but its next-review packet was prepared before the workflow-created registration/metadata commits. Therefore #913's packet must not be reused to decide slice 52.
7. A fresh English Content Full Validation must run on a HEAD containing the registered slice-51 state. If it emits another bounded MultiWOZ review packet, that packet becomes slice 52 and must go through the same complete editorial/dedupe/digest-bound review path.
8. If the fresh run reports `source-exhausted` / no next packet, treat the configured MultiWOZ lane as exhausted. Do not invent `test/dialogues_003.json`; instead inspect the current roadmap/source-coverage contracts and move only to the next explicitly designed E11 source/record-type lane.
9. After any reviewed bounded slice is integrated, regenerate publication, E11 readiness/runtime/record-level coverage and E12 artifacts, then verify the relevant English Content Full Validation before opening the following slice. Platform CI failures outside this content lane are not a reason to replay old completed content work.

## Known non-blocking enrichment debt

Many E04 items still lack `exampleIds`. These are not errors and must not be auto-filled from unsafe lemma-only matches. Treat them as an evidence/review queue: link only when whole-phrase/frame evidence is valid and reviewable.

## Blockers

- Tatoeba translation next-slice: requires the exact pinned source-cache bytes. The moving upstream export URL must not be downloaded and accepted under the old pin merely because the historical cache is unavailable.
- MultiWOZ is not currently source-cache blocked. The immediate requirement is a fresh Full Validation after slice-51 registration so the deterministic selector can prove either a real next packet or `source-exhausted` against the final configured source set.

## Next actionable task

Run English Content Full Validation from the newest live HEAD that contains the registered slice-51 state. Use only the fresh review/intake/editorial-handoff artifacts from that run. If a non-empty packet exists, review the complete bounded packet as slice 52 with exact/near-dedupe checks, grammar/naturalness/CEFR/license review, explicit edit/reject reasons and exact digest binding, then commit it atomically and let the normal apply/register pipeline run. If the fresh run reports `source-exhausted` or produces no next MultiWOZ packet, do not add `test/dialogues_003.json`; inspect the current E11 roadmap/source coverage and continue with the next explicitly designed lane.
