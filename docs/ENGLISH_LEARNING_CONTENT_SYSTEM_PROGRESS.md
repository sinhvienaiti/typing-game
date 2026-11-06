# English Learning Content System — Progress

Status: SCALE_UP_ACTIVE

## Current checkpoint

- Working branch: `feature/english-learning-content-system`
- Current HEAD: resolve the branch HEAD from GitHub at the start of every run. Do not hard-code the checkpoint file's own commit SHA because updating this file changes HEAD.
- Latest verified E11 typing-text checkpoint: editorial commit `1192fcb7eed7f93cd6606e20530c291ce2ea0bfb` — 24/24 Slice 22 sentences have digest-bound published review decisions; English Content Full Validation run `42264784597` passed, including runtime publication, smoke, E11 coverage, E12 and reproducibility. Its four bot-generated runtime/metadata commits ended at `240318b372f4975162247f5fa40266c613690aae`. Bot-authored PR runs may show `action_required`; do not misreport them as success on that SHA.
- Published Slice 22 runtime snapshot: 1,729 example sentences, 3,617 total sentence records, 14,512 published rich records, 14,512 applied editorial decisions, 900 dictionary records, 300 grammar records and 9,695 phrase records. See live `shared/sentences/manifest.json`, E10 ledger, E12 audit and acceptance report before using these numbers in later work.
- Historical MultiWOZ slice-51 editorial checkpoint: `a6b1844774cb9a9b1826f4a7ed348af507f67868` — English Content Full Validation #913 passed the complete MultiWOZ E11 slice-51 editorial decision set. Its registration and generated-metadata commits were `b9400e88f2c498b8524137aa2317d32ab87b0f81` and `9803698754f07d7023bde774b13c249eb8309d91`.
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
- E06 controlled sentence/exercise/dialogue/mistake pilots: complete — historical pre-E11 scale-up baseline was 1,513 examples; current runtime after E11 Slice 22 contains 1,729 examples + 1,400 exercises + 100 dialogues + 388 reviewed common mistakes
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

1. E04 scale-224 and its approved controlled phrase-family minimums remain complete. Do not create scale-225 merely to increase volume.
2. Translation-pair expansion is below its locked E11 target, but the historically pinned Tatoeba raw cache bytes are unavailable through the reproducible repo path. Keep import checksum gates strict; mutable weekly-export URLs are source-intake probes, not replacements for an approved pin.
3. The pinned MultiWOZ E11 lane is now `source-exhausted` in Full Validation run `42264784597`: 1,171 candidate dialogues, 547 rejected, 625 used, zero remaining and zero selected. It is not a justification to invent `test/dialogues_003.json`.
4. Reproducible E11 typing-text review is the bounded fallback lane. Slices 21 and 22 use project-original passages with explicit provenance and digest-bound editorial review; Slice 22 adds 24 published examples from six source shards and six decision shards, including three documented self-containment/punctuation edits. All generated publication/dedupe gates passed in Full Validation.
5. The deterministic next typing-text review packet from run `42264784597` is a **candidate only**, not published Slice 23: 1,000 queue candidates, 300 controlled, 516 reviewed decision IDs, 484 remaining before selection, 24 selected. Its selected range begins `sent.tt.l017-p001.011` and ends `sent.tt.l020-p001.012`. Regenerate against the newest HEAD before reviewing Slice 23.
6. Platform CI on the Slice 22 *editorial-only* commit `1192fcb7` failed the expected reproducibility diff because the generated `shared/sentences` runtime was not committed yet; Full Validation completed the regeneration and pushed the four metadata/runtime commits, ending at `240318b`. Do not disable the `git diff --exit-code` gate. Re-run the normal PR workflows from a human-authored checkpoint commit on top of synchronized artifacts.
7. Verify English Content Full Validation, Master Plan Acceptance and Platform CI with no stale generated artifacts before opening the next slice. Respect new HEADs, human-versus-bot PR event behavior, and the current source-update policy.

## Known non-blocking enrichment debt

Many E04 items still lack `exampleIds`. These are not errors and must not be auto-filled from unsafe lemma-only matches. Treat them as an evidence/review queue: link only when whole-phrase/frame evidence is valid and reviewable.

## Blockers

- Tatoeba next translation slice remains source-blocked until the exact pinned source bytes are recovered or a reviewed source upgrade is approved. Never silently update a checksum.
- The configured MultiWOZ lane is source-exhausted. No additional upstream-designed file should be fabricated.
- PR workflow runs triggered by bot-generated commits can show `action_required` with no jobs. Validate the synchronized runtime from a subsequent human-authored checkpoint commit instead of treating bot runs as green.

## Next actionable task

Verify all three required workflows from a new human-authored checkpoint commit on top of the synchronized Slice 22 runtime (generated HEAD `240318b372f4975162247f5fa40266c613690aae`). If checks pass and the branch remains coherent, regenerate the deterministic E11 typing-text next-review packet from the newest HEAD, audit source integrity/grammar/naturalness/CEFR/exact-and-near-duplicates/license, then review and publish only eligible Slice 23 records through digest-bound E10 decisions. Leave the already complete MultiWOZ and E04 lanes untouched.
