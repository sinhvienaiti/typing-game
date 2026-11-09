# English Learning Content System — Progress

Status: SCALE_UP_ACTIVE

## Current checkpoint

- Working branch: `feature/english-learning-content-system`
- Current HEAD: resolve the branch HEAD from GitHub at the start of every run. Do not hard-code the checkpoint file's own commit SHA because updating this file changes HEAD.
- Latest E11 typing-text work: Group 1 / Step 1 reviews all 316 candidates remaining after Slice 29 across Slices 30–43 (thirteen full 24-record slices and a final four-record slice). All 316 have explicit digest-bound publication decisions; 238 documented edits improve standalone context, naturalness, terminology or punctuation. CEFR: 6 A1 + 53 A2 + 176 B1 + 81 B2. Each decision records exact source-file SHA-256 and editorial rationale.
- Latest verified remote CI baseline: `30e2a514e26a4edcd6e971ea37fde79565ec1d3d`; Platform CI `42454527175`, Master Plan Acceptance `42454527087` and Full Validation `42454523482` all passed. Check PR #48 for current continuation-HEAD evidence.
- Published Slice 43 runtime snapshot: 2,213 example sentences, 4,101 total sentence records, 14,996 published rich records and 14,996 applied editorial decisions; dictionary 900, grammar 300 and phrases 9,695. The default 1,000-candidate typing-text queue is now source-exhausted. Refer to generated manifests/reports before reusing these counts.
- Historical MultiWOZ slice-51 editorial checkpoint: `a6b1844774cb9a9b1826f4a7ed348af507f67868` — English Content Full Validation #913 passed the complete MultiWOZ E11 slice-51 editorial decision set. Its registration and generated-metadata commits were `b9400e88f2c498b8524137aa2317d32ab87b0f81` and `9803698754f07d7023bde774b13c249eb8309d91`.
- MultiWOZ slice 51 is integrated: 22/22 candidates received explicit editorial decisions, with 9 edited records retained and 13 rejected. The registered runtime slice is `content/english/sentences/e11-multiwoz-dialogue-reviewed-slice-51.json`.
- The pinned MultiWOZ 2.2 source coverage now includes the complete configured source set at immutable upstream commit `fe0c8e65cfcd8462bd33c86e35f21addc84ca82b`: train `dialogues_001.json` through `dialogues_017.json`, dev `dialogues_001.json` and `dialogues_002.json`, and test `dialogues_001.json` and `dialogues_002.json`. There is no configured or upstream-designed `test/dialogues_003.json` lane; never invent one.
- E04 scale-224 publication is complete. Do not recreate scale-223/scale-224 artifacts or reopen the 2,000-chunk completion batch.
- Current phase: four sequential three-step groups are recorded in `docs/ENGLISH_CONTENT_EXECUTION_PLAN.md`. Group 1 Step 1 is PASS; Step 2 is IN PROGRESS with active new-source editorial intake. The original source shortage is not an overall stop condition. Group 1 is not complete and Steps 3–12 are not unlocked.
- New pinned intake: official Tatoeba 2026-10-31 English detailed sentences, self-reported language levels, experimental sentence reviews and action tags were acquired and SHA-256 verified. The separate English-only canonical snapshot contains 122,212 candidates; after controlled/exact exclusions and 17,824 decisions, 104,359 remain. It is reproducible offline and does not change the historical EN/VI/link pin.
- English-only editorial batches 01–190: 37,824 decisions, 34,045 published, 3,779 rejected and 615 disclosed edits. Batches 181–190 add 2,000 reviews, 1,786 publications, 214 rejections and 62 edits. Runtime: 36,258 examples, 38,146 sentence records and 49,041 rich records; ledger: 52,820 decisions. Approved English-only objects match runtime exactly and pass both adapters (68,090 checks). Shard `examples/068.json` filled to 500, new shards `069.json`, `070.json`, `071.json` (500 records each), and `072.json` (258 records) are registered in the manifest.
- Step 2 capacity review is now `editorial-review-required`, with an optimistic combined candidate bound of 125,203 before rejection/dedup. This is not publication or Step 2 sign-off. Continue bounded review; candidate counts never unlock Step 3.
- Next editorial packet: batch 191; 84,357 English-only candidates remain unreviewed. Published examples are 63,742 short of 100,000. Later steps remain closed.
- PR: #48 — open, draft, mergeable
- Published runtime release: `2026.10.0`

### Group 1 Step 1 — Slices 30–43

| Slice | Published examples | A1 | A2 | B1 | B2 | Documented edits |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 30 | 24 | 1 | 7 | 12 | 4 | 17 |
| 31 | 24 | 1 | 3 | 12 | 8 | 16 |
| 32 | 24 | 1 | 4 | 16 | 3 | 18 |
| 33 | 24 | 0 | 3 | 16 | 5 | 17 |
| 34 | 24 | 0 | 6 | 11 | 7 | 17 |
| 35 | 24 | 0 | 4 | 15 | 5 | 15 |
| 36 | 24 | 0 | 5 | 14 | 5 | 21 |
| 37 | 24 | 0 | 3 | 12 | 9 | 19 |
| 38 | 24 | 0 | 4 | 14 | 6 | 20 |
| 39 | 24 | 0 | 4 | 14 | 6 | 21 |
| 40 | 24 | 1 | 5 | 13 | 5 | 19 |
| 41 | 24 | 1 | 2 | 12 | 9 | 18 |
| 42 | 24 | 1 | 3 | 12 | 8 | 16 |
| 43 | 4 | 0 | 0 | 3 | 1 | 4 |
| Total | 316 | 6 | 53 | 176 | 81 | 238 |

The scheduled/manual worker must always resolve the newest branch HEAD and its workflows directly from GitHub before doing work. If a newer commit exists, adopt it, inspect its changes, preserve completed work, and never reset/revert/overwrite/duplicate it.

## Completed mandatory milestones

- E00–E02 foundation/contracts: complete
- E03 controlled lexical pilot: complete — 300 lexemes + 300 linked primary senses + 300 usage sidecars
- E04 phrase/pattern architecture + current reviewed publication: complete — 9,695 published records after scale-224
- E05 grammar framework/runtime: complete — 300/300 topics (45 A1 + 50 A2 + 60 B1 + 60 B2 + 50 C1 + 35 C2)
- E06 controlled sentence/exercise/dialogue/mistake pilots: complete — historical pre-E11 baseline was 1,513 examples; current runtime after Slice 43 contains 2,213 examples + 1,400 exercises + 100 dialogues + 388 reviewed common mistakes
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
4. Group 1 Step 1 consumes the 316 remaining default-queue candidates through Slices 30–43. Source wording/ordinals, licensing, grammar, naturalness, CEFR and cross-authoring/runtime exact/near dedup were explicitly reviewed. Maximum new-record token-Jaccard overlap is 0.5, below the 0.86 review threshold. Original passages and source pins are unchanged.
5. The default next-review packet is now `source-exhausted`: 1,000 candidates, 1,000 reviewed IDs, zero remaining and zero selected. The selector explicitly handles final partial slices and empty queues. This exhausts the bounded queue, not all project passages and not the 100,000-example target.
6. The user authorized four groups of three steps with review before every transition. Step 1 is PASS on `565659b`. The original-lane capacity audit was followed by an offline pinned English-only intake. Step 2 is now in progress at 9,423 reviewed published examples; 112,962 English-only candidates and 4,588 project-original raw sentences remain unreviewed. The optimistic combined bound is 126,973 before rejection/dedup, not publication approval. Read the current capacity report rather than reusing the superseded source-shortage checkpoint.
7. All Step 1 workflows passed. Step 2 completion review has not passed; preserve the 100,000-example requirement and source/license/checksum gates. Later steps and groups remain queued. Read the execution plan and capacity report before resuming.

## Known non-blocking enrichment debt

Many E04 items still lack `exampleIds`. These are not errors and must not be auto-filled from unsafe lemma-only matches. Treat them as an evidence/review queue: link only when whole-phrase/frame evidence is valid and reviewable.

## Blockers

- Tatoeba next translation slice remains source-blocked until the exact pinned source bytes are recovered or a reviewed source upgrade is approved. Never silently update a checksum.
- The configured MultiWOZ lane is source-exhausted. No additional upstream-designed file should be fabricated.
- PR workflow runs triggered by bot-generated commits can show `action_required` with no jobs. Validate the synchronized runtime from a subsequent human-authored checkpoint commit instead of treating bot runs as green.

## Next actionable task

Continue English editorial batch 61 at `sent.tatoeba.282806` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 11,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 22–30

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 22 | 200 | 143 | 57 | 2 |
| 23 | 200 | 132 | 68 | 0 |
| 24 | 200 | 121 | 79 | 1 |
| 25 | 200 | 151 | 49 | 2 |
| 26 | 200 | 136 | 64 | 1 |
| 27 | 200 | 134 | 66 | 2 |
| 28 | 200 | 137 | 63 | 2 |
| 29 | 200 | 139 | 61 | 3 |
| 30 | 200 | 129 | 71 | 4 |
| Total | 1,800 | 1,222 | 578 | 17 |

Every candidate received an individual reading, explicit outcome and rationale. Review checked grammar, naturalness, standalone use, CEFR, canonical source evidence, attribution, exact/near matches and semantic repeats. Seventeen accepted edits preserve source meaning and disclose original/final wording, `modified: true`, an edit description and a recomputed controlled-source digest. Examples include the standard participle shaken, natural duration expressions, word order, collocations and clarified geographic/language scope. Edited final texts were checked against all active canonical sentence records as well as approved runtime/new-batch records; no exact collision was retained. Rejections remain in authoring, ledger and per-record editorial reports. Grammar that can be repaired without changing source meaning is edited and reviewed; duplication, missing factual context or an unsupported claim is not repaired by inventing new source content.

Local validation passes schema/source/review/license gates, E10 batch contracts and smoke, 112 content/tooling tests, 10 MultiWOZ handoff/decision tests, publication, dedup, published-runtime smoke, three runtime-count tests, E11 freshness and exact source/runtime coverage, capacity and master-plan reports. E12 release/maintenance snapshots are refreshed before final E11 readiness/runtime generation. Verify deterministic regeneration and commit every runtime shard referenced by the manifest before push. No engineering result satisfies the 100,000-example gate.

At the end of batches 22–30, English editorial batch 31 was next at `sent.tatoeba.67208`; that checkpoint has now been continued below. This remains execution Group 1 Step 2. Steps 3–12 remain queued; PR #48 stays Draft. Source/license pins, the historical EN/VI/link lane and legacy vocabulary ABI remain unchanged.

## English editorial continuation: batches 31–33

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 31 | 200 | 146 | 54 | 5 |
| 32 | 200 | 158 | 42 | 7 |
| 33 | 200 | 156 | 44 | 8 |
| Total | 600 | 460 | 140 | 20 |

Each of the 600 candidates received an individual reading, explicit outcome and rationale for grammar, naturalness, independent use, CEFR and source suitability. Canonical snapshot evidence, CC BY 2.0 France attribution and source digests were verified. Twenty accepted edits retain original/final wording, `modified: true`, a change description and recomputed digest. Repairs include neither-of-us agreement, goal-in-life wording, uncountable testimony, buttering-up collocation, compound punctuation and arithmetic-list wording. Edited final texts were compared against all canonical sentence records as well as retained runtime records. Self-review removed twelve additional semantic repeats below the lexical threshold, including wait-here, family-introduction, surprise-meeting and help-enabled-completion variants. All 140 rejections remain traceable in authoring, ledger and reports, without a CEFR or runtime object. Source authoring remains draft; only the exact digest-bound publication decision permits runtime publication.

Current English-only totals: 6,424 decisions, 4,892 published, 1,532 rejected and 118 disclosed edits. Full runtime: 7,105 examples, 8,993 sentence records and 19,888 rich records; ledger: 21,420 applied decisions (19,888 publication and 1,532 deprecated). The continuation adds 460 published examples; 92,895 more reviewed publications are needed to reach 100,000. All 4,892 English-only approved objects match runtime exactly and pass both Monkeytype and Karaoke adapters (9,784 checks). The example manifest includes `examples/014.json`; the final shard contains 105 records. There are 115,762 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 127,455 before further rejection/dedup and is not publication approval.

Local validation passes schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact record coverage, capacity and master-plan checks. E12 release/maintenance is regenerated before final E11 readiness/runtime. Deterministic regeneration and tracked manifest-shard coverage are mandatory before push. These engineering gates do not satisfy the Step 2 publication target.

The verified preceding checkpoint `cd323b28477c1562b54c22beae9118a9990de7e1` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42448870529), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42448870531) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42448867006). Verify all three workflows on the resulting continuation HEAD and record current evidence in PR #48; this file intentionally retains the preceding verified SHA to avoid a self-referential SHA-only commit.

At the end of batches 31–33, English batch 34 was next at `sent.tatoeba.72913`; the continuation is recorded below. All 6,424 reviewed English-only IDs are excluded from the next packet, which has no assigned CEFR. This remains execution Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI and completed E04/typing-text batches remain unchanged.

## English editorial continuation: batches 34–40

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 34 | 200 | 147 | 53 | 5 |
| 35 | 200 | 145 | 55 | 9 |
| 36 | 200 | 151 | 49 | 2 |
| 37 | 200 | 143 | 57 | 2 |
| 38 | 200 | 136 | 64 | 2 |
| 39 | 200 | 153 | 47 | 3 |
| 40 | 200 | 142 | 58 | 5 |
| Total | 1,400 | 1,017 | 383 | 28 |

All 1,400 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-eight accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest. Repairs cover plural possessives, articles, collocations, agreement, prepositions, passive tense, clause wording and clearer reference. Seven additional semantic repeats were removed during self-review, below the lexical threshold. All 383 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 7,824 decisions, 5,909 published, 1,915 rejected and 146 disclosed edits. Runtime: 8,122 examples, 10,010 sentence records and 20,905 rich records; ledger: 22,820 applied decisions (20,905 publication and 1,915 deprecated). This continuation adds 1,017 examples, leaving 91,878 more reviewed publications to reach 100,000. All 5,909 English-only approved objects match runtime exactly and pass both adapters (11,818 checks). Rejected IDs remain absent. The example manifest includes new `examples/015.json` and `examples/016.json`; shard 016 has 122 records. There are 114,362 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 127,072 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `30e2a514e26a4edcd6e971ea37fde79565ec1d3d` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42454527175), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42454527087) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42454523482). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 41 at `sent.tatoeba.248058` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 7,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 41–47

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 41 | 200 | 183 | 17 | 7 |
| 42 | 200 | 186 | 14 | 6 |
| 43 | 200 | 173 | 27 | 7 |
| 44 | 200 | 194 | 6 | 8 |
| 45 | 200 | 193 | 7 | 7 |
| 46 | 200 | 190 | 10 | 7 |
| 47 | 200 | 182 | 18 | 12 |
| Total | 1,400 | 1,301 | 99 | 54 |

All 1,400 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fifty-four accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest. Repairs cover articles, collocations, agreement, prepositions, comma splices, coordination, clause wording and clearer standalone reference. Semantic repeats and near duplicates were removed during review. All 99 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 9,224 decisions, 7,210 published, 2,014 rejected and 200 disclosed edits. Runtime: 9,423 examples, 11,311 sentence records and 22,206 rich records; ledger: 24,220 applied decisions (22,206 publication and 2,014 deprecated). This continuation adds 1,301 examples, leaving 90,577 more reviewed publications to reach 100,000. All 7,210 English-only approved objects match runtime exactly and pass both adapters (14,420 checks). Rejected IDs remain absent. The example manifest includes new `examples/017.json` and `examples/018.json`; shard 018 has 423 records. There are 112,962 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,973 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 48 at `sent.tatoeba.264735` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 9,224 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 48–50

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 48 | 200 | 181 | 19 | 11 |
| 49 | 200 | 184 | 16 | 19 |
| 50 | 200 | 194 | 6 | 13 |
| Total | 600 | 559 | 41 | 43 |

All 600 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Forty-three accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest. Repairs cover articles, collocations, agreement, prepositions, comma splices, coordination, clause wording and clearer standalone reference. Semantic repeats and near duplicates (e.g. high-overlap variants of future prediction, delayed stopping of crying, headache bed-going, and neck hugs) were removed during review. All 41 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 9,824 decisions, 7,769 published, 2,055 rejected and 243 disclosed edits. Runtime: 9,982 examples, 11,870 sentence records and 22,765 rich records; ledger: 24,820 applied decisions (22,765 publication and 2,055 deprecated). This continuation adds 559 examples, leaving 90,018 more reviewed publications to reach 100,000. All 7,769 English-only approved objects match runtime exactly and pass both adapters (15,538 checks). Rejected IDs remain absent. Shard 018 was updated to its 500-record capacity and the example manifest includes new `examples/019.json`; shard 019 has 482 records. There are 112,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,931 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 51 at `sent.tatoeba.268742` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 9,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 51–60

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 51 | 200 | 194 | 6 | 1 |
| 52 | 200 | 191 | 9 | 0 |
| 53 | 200 | 195 | 5 | 0 |
| 54 | 200 | 196 | 4 | 0 |
| 55 | 200 | 196 | 4 | 0 |
| 56 | 200 | 194 | 6 | 0 |
| 57 | 200 | 195 | 5 | 1 |
| 58 | 200 | 196 | 4 | 0 |
| 59 | 200 | 192 | 8 | 0 |
| 60 | 200 | 195 | 5 | 0 |
| Total | 2,000 | 1,944 | 56 | 2 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (e.g. normalization of unhyphenated compound nouns and punctuation spacing). Near duplicates and intra-slice duplicate variations were removed during review. All 56 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 11,824 decisions, 9,713 published, 2,111 rejected and 245 disclosed edits. Runtime: 11,926 examples, 13,814 sentence records and 24,709 rich records; ledger: 26,820 applied decisions (24,709 publication and 2,111 deprecated). This continuation adds 1,944 examples, leaving 88,074 more reviewed publications to reach 100,000. All 9,713 English-only approved objects match runtime exactly and pass both adapters (19,426 checks). Rejected IDs remain absent. Shard 019 was completed with 500 records, new shards `examples/020.json`, `examples/021.json`, `examples/022.json` (500 records each), and `examples/023.json` (426 records) are registered in the manifest. There are 110,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,875 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 61 at `sent.tatoeba.282806` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 11,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 61–70

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 61 | 200 | 193 | 7 | 0 |
| 62 | 200 | 189 | 11 | 0 |
| 63 | 200 | 194 | 6 | 0 |
| 64 | 200 | 188 | 12 | 0 |
| 65 | 200 | 192 | 8 | 0 |
| 66 | 200 | 193 | 7 | 1 |
| 67 | 200 | 196 | 4 | 0 |
| 68 | 200 | 195 | 5 | 0 |
| 69 | 200 | 194 | 6 | 0 |
| 70 | 200 | 191 | 9 | 0 |
| Total | 2,000 | 1,925 | 75 | 1 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. One accepted edit preserves source meaning and discloses original/final text, modified provenance, the change description and a recomputed digest (e.g. normalization of spelling and punctuation). Near duplicates and intra-slice duplicate variations were removed during review. All 75 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 13,824 decisions, 11,638 published, 2,186 rejected and 246 disclosed edits. Runtime: 13,851 examples, 15,739 sentence records and 26,634 rich records; ledger: 28,820 applied decisions (26,634 publication and 2,186 deprecated). This continuation adds 1,925 examples, leaving 86,149 more reviewed publications to reach 100,000. All 11,638 English-only approved objects match runtime exactly and pass both adapters (23,276 checks). Rejected IDs remain absent. Shard 023 was completed with 500 records, new shards `examples/024.json`, `examples/025.json`, `examples/026.json` (500 records each), and `examples/027.json` (351 records) are registered in the manifest. There are 108,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,800 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 71 at `sent.tatoeba.297624` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 13,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 71–72

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 71 | 200 | 189 | 11 | 6 |
| 72 | 200 | 192 | 8 | 10 |
| Total | 400 | 381 | 19 | 16 |

All 400 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Sixteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 71: flatly rejected offer, poet and a statesman, prevented him from attending, quite a humble man, talk of the town, Newsweek magazine article drop; Batch 72: cozy little house, capable at his job, woman-hater, henpecked, angling for a promotion, into the crowd, a reputation, sharpshooter, his entire fortune, gives his work all he's got). Near duplicates and intra-slice duplicate variations were removed during review. All 19 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 14,224 decisions, 12,019 published, 2,205 rejected and 262 disclosed edits. Runtime: 14,232 examples, 16,120 sentence records and 27,015 rich records; ledger: 29,220 applied decisions (27,015 publication and 2,205 deprecated). This continuation adds 381 examples across batches 71–72, leaving 85,768 more reviewed publications to reach 100,000. All 12,019 English-only approved objects match runtime exactly and pass both adapters (24,038 checks). Rejected IDs remain absent. Shard 027 was completed with 500 records and shard `examples/028.json` now holds 232 records. There are 107,961 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,781 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 73 at `sent.tatoeba.300949` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 14,224 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 73–80

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 73 | 200 | 189 | 11 | 5 |
| 74 | 200 | 190 | 10 | 4 |
| 75 | 200 | 191 | 9 | 3 |
| 76 | 200 | 193 | 7 | 3 |
| 77 | 200 | 192 | 8 | 3 |
| 78 | 200 | 193 | 7 | 3 |
| 79 | 200 | 191 | 9 | 4 |
| 80 | 200 | 192 | 8 | 3 |
| Total | 1,600 | 1,531 | 69 | 28 |

All 1,600 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-eight accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 73: natural gerund, proper prepositional idiom, pronoun clarity; Batch 74: adjective order, idiomatic noun complement; Batch 75: article usage, modern collocation; Batch 76: preposition correction, natural gerund complement; Batch 77: talent for dancing, eye for beauty, same design as; Batch 78: take her place, different from, too short notice; Batch 79: plays the piano, natural for the part, which one I should buy, eye for a good bargain; Batch 80: closed housekeeping, coming into contact, lowercase ill). Near duplicates and intra-slice duplicate variations were removed during review. All 69 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 15,824 decisions, 13,550 published, 2,274 rejected and 290 disclosed edits. Runtime: 15,763 examples, 17,651 sentence records and 28,546 rich records; ledger: 30,820 applied decisions (28,546 publication and 2,274 deprecated). This continuation adds 1,531 examples across batches 73–80, leaving 84,237 more reviewed publications to reach 100,000. All 13,550 English-only approved objects match runtime exactly and pass both adapters (27,100 checks). Rejected IDs remain absent. Shard 028 was completed with 500 records, new shards `examples/029.json` and `examples/030.json` (500 records each), and shard `examples/031.json` (263 records) are registered in the manifest. There are 106,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,712 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 81 at `sent.tatoeba.313724` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 15,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 81–90

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 81 | 200 | 189 | 11 | 2 |
| 82 | 200 | 193 | 7 | 3 |
| 83 | 200 | 191 | 9 | 3 |
| 84 | 200 | 193 | 7 | 3 |
| 85 | 200 | 194 | 6 | 3 |
| 86 | 200 | 192 | 8 | 3 |
| 87 | 200 | 193 | 7 | 3 |
| 88 | 200 | 193 | 7 | 3 |
| 89 | 200 | 193 | 7 | 2 |
| 90 | 200 | 191 | 9 | 2 |
| Total | 2,000 | 1,922 | 78 | 27 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-seven accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 81: burned her left hand, express her feelings; Batch 82: clear-headed, all to herself, in a soft voice; Batch 83: Breakfast is included, using too much praise, When the manager gives a plan; Batch 84: for misconduct, stretched his legs, into the sky; Batch 85: Reading literature, United States,, exchange it for; Batch 86: cop-out, customer is always right principle, interfere with my affairs; Batch 87: want to press you, girls' school, Do you want to go; Batch 88: just in case, entered a war, Neither of my parents is alive; Batch 89: it is important to clearly distinguish, halfway; Batch 90: why he was so sad, custom-made). Near duplicates and intra-slice duplicate variations were removed during review. All 78 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 17,824 decisions, 15,472 published, 2,352 rejected and 317 disclosed edits. Runtime: 17,685 examples, 19,573 sentence records and 30,468 rich records; ledger: 32,820 applied decisions (30,468 publication and 2,352 deprecated). This continuation adds 1,922 examples across batches 81–90, leaving 82,315 more reviewed publications to reach 100,000. All 15,472 English-only approved objects match runtime exactly and pass both adapters (30,944 checks). Rejected IDs remain absent. Shard 031 was completed with 500 records, new shards `examples/032.json`, `033.json`, `034.json` (500 records each), and shard `examples/035.json` (185 records) are registered in the manifest. There are 104,359 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,632 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `23b60c9ec791a4afe06b9d8a66c3bceb7bf76a7a` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 91 at `sent.tatoeba.370950` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 17,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 91–100

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 91 | 200 | 193 | 7 | 1 |
| 92 | 200 | 195 | 5 | 2 |
| 93 | 200 | 189 | 11 | 2 |
| 94 | 200 | 194 | 6 | 3 |
| 95 | 200 | 190 | 10 | 2 |
| 96 | 200 | 198 | 2 | 2 |
| 97 | 200 | 199 | 1 | 2 |
| 98 | 200 | 198 | 2 | 2 |
| 99 | 200 | 199 | 1 | 3 |
| 100 | 200 | 198 | 2 | 2 |
| Total | 2,000 | 1,953 | 47 | 21 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-one accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 91: ask for help; Batch 92: Why is it that you can write, heard afterward; Batch 93: One has to protect one's family, The president abolished slavery; Batch 94: which is why, going to, near the station; Batch 95: conditional comma, causing problems; Batch 96: good at science, work and home life; Batch 97: onto your computer, debating health care; Batch 98: with computers, whitewater; Batch 99: flooring is hardwood, conditional comma, Washington, D.C.; Batch 100: windowsill, gives off light). Near duplicates and intra-slice duplicate variations were removed during review. All 47 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 19,824 decisions, 17,425 published, 2,399 rejected and 338 disclosed edits. Runtime: 19,638 examples, 21,526 sentence records and 32,421 rich records; ledger: 34,820 applied decisions (32,421 publication and 2,399 deprecated). This continuation adds 1,953 examples across batches 91–100, leaving 80,362 more reviewed publications to reach 100,000. All 17,425 English-only approved objects match runtime exactly and pass both adapters (34,850 checks). Rejected IDs remain absent. Shard 035 was completed with 500 records, new shards `examples/036.json`, `037.json`, `038.json` (500 records each), and shard `examples/039.json` (138 records) are registered in the manifest. There are 102,359 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,584 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `dd962a51f93f6c8d4df7140e69882f05a91798ac` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 101 at `sent.tatoeba.681375` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 19,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 101–110

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 101 | 200 | 198 | 2 | 1 |
| 102 | 200 | 198 | 2 | 1 |
| 103 | 200 | 198 | 2 | 4 |
| 104 | 200 | 197 | 3 | 2 |
| 105 | 200 | 198 | 2 | 2 |
| 106 | 200 | 192 | 8 | 1 |
| 107 | 200 | 183 | 17 | 3 |
| 108 | 200 | 196 | 4 | 0 |
| 109 | 200 | 198 | 2 | 2 |
| 110 | 200 | 198 | 2 | 1 |
| Total | 2,000 | 1,956 | 44 | 17 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Seventeen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 101: kids' favorite meal; Batch 102: push-ups; Batch 103: reason for being late, French fries, three-year sentence, Chickenpox; Batch 104: modern structure, backyard; Batch 105: Venice, Italy,, Band-Aid; Batch 106: send word; Batch 107: time heals all wounds, buy me some saffron, make my son eat; Batch 108: clean historical narratives preserved; Batch 109: repay, last resort; Batch 110: Rio Grande). Near duplicates and intra-slice duplicate variations were removed during review. All 44 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 21,824 decisions, 19,381 published, 2,443 rejected and 355 disclosed edits. Runtime: 21,594 examples, 23,482 sentence records and 34,377 rich records; ledger: 36,820 applied decisions (34,377 publication and 2,443 deprecated). This continuation adds 1,956 examples across batches 101–110, leaving 78,406 more reviewed publications to reach 100,000. All 19,381 English-only approved objects match runtime exactly and pass both adapters (38,762 checks). Rejected IDs remain absent. Shard 039 was completed with 500 records, new shards `examples/040.json`, `041.json`, `042.json` (500 records each), and shard `examples/043.json` (94 records) are registered in the manifest. There are 100,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,540 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `da55ebabeb4b0453303d2e07172fe4ff872e42b2` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 111 at `sent.tatoeba.803149` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 21,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 141–150

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 141 | 200 | 183 | 17 | 1 |
| 142 | 200 | 173 | 27 | 1 |
| 143 | 200 | 192 | 8 | 1 |
| 144 | 200 | 188 | 12 | 1 |
| 145 | 200 | 187 | 13 | 1 |
| 146 | 200 | 178 | 22 | 2 |
| 147 | 200 | 176 | 24 | 1 |
| 148 | 200 | 196 | 4 | 4 |
| 149 | 200 | 192 | 8 | 1 |
| 150 | 200 | 195 | 5 | 1 |
| Total | 2,000 | 1,860 | 140 | 14 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fourteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 141: With social media comma; Batch 142: Out of all my children comma; Batch 143: chickenpox closed compound; Batch 144: Hey, guys comma; Batch 145: show-off hyphenated; Batch 146: short-order cook, snowstorm; Batch 147: feet than to live comma removed; Batch 148: forced open, freshwater, mayor lowercase, For an old man comma; Batch 149: sweater is small, and; Batch 150: businessman closed compound). Near duplicates and intra-slice duplicate variations were removed during review. All 140 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 29,824 decisions, 26,907 published, 2,917 rejected and 434 disclosed edits. Runtime: 29,120 examples, 31,008 sentence records and 41,903 rich records; ledger: 44,820 applied decisions (41,903 publication and 2,917 deprecated). This continuation adds 1,860 examples across batches 141–150, leaving 70,880 more reviewed publications to reach 100,000. All 26,907 English-only approved objects match runtime exactly and pass both adapters (53,814 checks). Rejected IDs remain absent. Shard 054 was completed with 500 records, new shards `examples/055.json`, `056.json`, `057.json` (500 records each), and shard `examples/058.json` (120 records) are registered in the manifest. There are 92,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,066 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `559305537ef4f30ad8a4176465377f0a996f014e` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 151 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 29,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 151–160

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 151 | 200 | 190 | 10 | 2 |
| 152 | 200 | 178 | 22 | 4 |
| 153 | 200 | 177 | 23 | 4 |
| 154 | 200 | 189 | 11 | 3 |
| 155 | 200 | 192 | 8 | 2 |
| 156 | 200 | 195 | 5 | 3 |
| 157 | 200 | 188 | 12 | 4 |
| 158 | 200 | 181 | 19 | 5 |
| 159 | 200 | 166 | 34 | 2 |
| 160 | 200 | 175 | 25 | 5 |
| Total | 2,000 | 1,831 | 169 | 34 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-four accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 151: leftovers, eighty kilometers comma; Batch 152: Tidy up comma, streetcar, Oval Office, last-minute; Batch 153: Bullfighting, anymore, Western civilization, broke his arm comma; Batch 154: half a dozen, Hurry up comma, high interest; Batch 155: in favor of going comma, on the whole; Batch 156: timetable, scolded them comma, dining room serial comma; Batch 157: run-down, streetlights, passkey, tax-free; Batch 158: shop will be closed comma, take a walk comma, Yesterday comma, Once comma, fool than comparative; Batch 159: passport photo comma, once-in-a-lifetime; Batch 160: smoke semicolon he drinks, Mass, busy today semicolon otherwise, platinum-blonde, barbed-wire). Near duplicates and intra-slice duplicate variations were removed during review. All 169 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 31,824 decisions, 28,738 published, 3,086 rejected and 468 disclosed edits. Runtime: 30,951 examples, 32,839 sentence records and 43,734 rich records; ledger: 46,820 applied decisions (43,734 publication and 3,086 deprecated). This continuation adds 1,831 examples across batches 151–160, leaving 69,049 more reviewed publications to reach 100,000. All 28,738 English-only approved objects match runtime exactly and pass both adapters (57,476 checks). Rejected IDs remain absent. Shard 058 was completed with 500 records, new shards `examples/059.json`, `060.json` (500 records each), and shard `examples/061.json` (451 records) are registered in the manifest. There are 90,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,897 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `ca5d5d11f70903fc467425f4f36e785c345bc02e` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 161 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 31,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 161–170

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 161 | 200 | 178 | 22 | 2 |
| 162 | 200 | 177 | 23 | 2 |
| 163 | 200 | 170 | 30 | 2 |
| 164 | 200 | 161 | 39 | 2 |
| 165 | 200 | 171 | 29 | 4 |
| 166 | 200 | 177 | 23 | 2 |
| 167 | 200 | 175 | 25 | 6 |
| 168 | 200 | 182 | 18 | 5 |
| 169 | 200 | 173 | 27 | 5 |
| 170 | 200 | 174 | 26 | 5 |
| Total | 2,000 | 1,738 | 262 | 35 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-five accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 161: uppercuts, Last week comma; Batch 162: a couple of minutes, legwarmers; Batch 163: sandcastle, okay; Batch 164: windchimes, Recently comma; Batch 165: streetlamp, okay, soccer and, PIN; Batch 166: mousepad, do it too comma removed; Batch 167: you too comma removed, favor, lawnmower, whitewater, savor, Last Sunday comma; Batch 168: motorhome, On Saturdays comma, Every once in a while comma, everything and, Earth; Batch 169: Tom and I'm, playing too comma removed, Two years ago comma, shoehorn, at home too comma removed; Batch 170: okay, dog and his, King-size, Mary and they, Tonight comma). Near duplicates and intra-slice duplicate variations were removed during review. All 262 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 33,824 decisions, 30,476 published, 3,348 rejected and 503 disclosed edits. Runtime: 32,689 examples, 34,577 sentence records and 45,472 rich records; ledger: 48,820 applied decisions (45,472 publication and 3,348 deprecated). This continuation adds 1,738 examples across batches 161–170, leaving 67,311 more reviewed publications to reach 100,000. All 30,476 English-only approved objects match runtime exactly and pass both adapters (60,952 checks). Rejected IDs remain absent. Shard 061 was completed with 500 records, new shards `examples/062.json`, `063.json`, `064.json` (500 records each), and shard `examples/065.json` (189 records) are registered in the manifest. There are 88,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,634 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `f19aae1a89d8cc3397332e159d47a4e2de7dce7c` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 171 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 33,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 171–180

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 171 | 200 | 177 | 23 | 10 |
| 172 | 200 | 178 | 22 | 3 |
| 173 | 200 | 185 | 15 | 6 |
| 174 | 200 | 183 | 17 | 3 |
| 175 | 200 | 170 | 30 | 5 |
| 176 | 200 | 179 | 21 | 5 |
| 177 | 200 | 176 | 24 | 4 |
| 178 | 200 | 175 | 25 | 3 |
| 179 | 200 | 185 | 15 | 4 |
| 180 | 200 | 175 | 25 | 7 |
| Total | 2,000 | 1,783 | 217 | 50 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fifty accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 171: spent on Christmas presents, First comma, serial comma, otherwise semicolon, snored comma and, checkbook closed compound, workload closed compound, fell into pool, at the postgraduate level, wasn't only fined semicolon; Batch 172: joke soon comma removed, rich comma or, shorts-and-T-shirt hyphenated; Batch 173: Saltwater closed compound, crow comma but, in the hospital, wise man semicolon, serial comma, teaching comma and; Batch 174: brand-new hyphenated, stove comma and, Yesterday morning comma; Batch 175: strong that result clause, like you comma and, Earth capitalized, drinking poison and comma removed, In many ways comma; Batch 176: each other comma and, Christmas Day capitalized and comma, reliable comma and, terse comma and, volatile comma and; Batch 177: hooky spelling, sensitive child comma and, weaned comma they, Last night comma; Batch 178: now is wrong comma removed, treehouse closed compound, serial comma; Batch 179: inquiries American spelling, quarreled American spelling, top-secret hyphenated, appreciate it if; Batch 180: really close comma and, steady rain comma and, completely blank comma and, serial comma, sandcastle closed compound, evils I prefer redundant then removed, receives it poorer comma removed). Near duplicates and intra-slice duplicate variations were removed during review. All 217 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 35,824 decisions, 32,259 published, 3,565 rejected and 553 disclosed edits. Runtime: 34,472 examples, 36,360 sentence records and 47,255 rich records; ledger: 50,820 applied decisions (47,255 publication and 3,565 deprecated). This continuation adds 1,783 examples across batches 171–180, leaving 65,528 more reviewed publications to reach 100,000. All 32,259 English-only approved objects match runtime exactly and pass both adapters (64,518 checks). Rejected IDs remain absent. Shard 065 was completed with 500 records, new shards `examples/066.json`, `067.json` (500 records each), and shard `examples/068.json` (472 records) are registered in the manifest. There are 86,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,417 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `f19aae1a89d8cc3397332e159d47a4e2de7dce7c` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 181 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 35,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.
