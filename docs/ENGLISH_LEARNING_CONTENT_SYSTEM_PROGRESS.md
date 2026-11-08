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
- New pinned intake: official Tatoeba 2026-10-31 English detailed sentences, self-reported language levels, experimental sentence reviews and action tags were acquired and SHA-256 verified. The separate English-only canonical snapshot contains 122,212 candidates; after controlled/exact exclusions and 11,824 decisions, 110,361 remain. It is reproducible offline and does not change the historical EN/VI/link pin.
- English-only editorial batches 01–300: 59,824 decisions, 55,187 published, 4,637 rejected and 246 disclosed edits. Batches 201–300 add 20,000 reviews, 18,805 publications, 1,195 rejections and 0 edits. Runtime: 57,400 examples, 59,288 sentence records and 70,183 rich records; ledger: 74,820 decisions (70,183 publication, 4,637 deprecated). Approved English-only objects match runtime exactly and pass both adapters (110,374 checks). Shard `examples/077.json` filled to 500, new shards `078.json` through `113.json` (500 records each), and `114.json` (400 records) are registered in the manifest.
- Step 2 capacity review is now `editorial-review-required`, with an optimistic combined candidate bound of 124,349 before further rejection/dedup. This is not publication or Step 2 sign-off. Continue bounded review; candidate counts never unlock Step 3.
- Next editorial packet: batch 301 at `sent.tatoeba.5738175`; 62,361 English-only candidates remain unreviewed. Published examples are 42,600 short of 100,000. Later steps remain closed.
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

## English editorial continuation: batches 71–80

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 71 | 200 | 194 | 6 | 0 |
| 72 | 200 | 193 | 7 | 0 |
| 73 | 200 | 185 | 15 | 0 |
| 74 | 200 | 191 | 9 | 0 |
| 75 | 200 | 190 | 10 | 0 |
| 76 | 200 | 190 | 10 | 0 |
| 77 | 200 | 191 | 9 | 0 |
| 78 | 200 | 189 | 11 | 0 |
| 79 | 200 | 191 | 9 | 0 |
| 80 | 200 | 193 | 7 | 0 |
| Total | 2,000 | 1,907 | 93 | 0 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Near duplicates and intra-slice duplicate variations were removed during review. All 93 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 15,824 decisions, 13,545 published, 2,279 rejected and 246 disclosed edits. Runtime: 15,758 examples, 17,646 sentence records and 28,541 rich records; ledger: 30,820 applied decisions (28,541 publication and 2,279 deprecated). This continuation adds 1,907 examples, leaving 84,242 more reviewed publications to reach 100,000. All 13,545 English-only approved objects match runtime exactly and pass both adapters (27,090 checks). Rejected IDs remain absent. Shard 027 was completed with 500 records, new shards `examples/028.json`, `examples/029.json`, `examples/030.json` (500 records each), and `examples/031.json` (258 records) are registered in the manifest. There are 106,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,707 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 81 at `sent.tatoeba.313724` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 15,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 81–90

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 81 | 200 | 188 | 12 | 0 |
| 82 | 200 | 195 | 5 | 0 |
| 83 | 200 | 188 | 12 | 0 |
| 84 | 200 | 192 | 8 | 0 |
| 85 | 200 | 192 | 8 | 0 |
| 86 | 200 | 190 | 10 | 0 |
| 87 | 200 | 194 | 6 | 0 |
| 88 | 200 | 193 | 7 | 0 |
| 89 | 200 | 194 | 6 | 0 |
| 90 | 200 | 195 | 5 | 0 |
| Total | 2,000 | 1,921 | 79 | 0 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Near duplicates and intra-slice duplicate variations were removed during review. All 79 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 17,824 decisions, 15,466 published, 2,358 rejected and 246 disclosed edits. Runtime: 17,679 examples, 19,567 sentence records and 30,462 rich records; ledger: 32,820 applied decisions (30,462 publication and 2,358 deprecated). This continuation adds 1,921 examples, leaving 82,321 more reviewed publications to reach 100,000. All 15,466 English-only approved objects match runtime exactly and pass both adapters (30,932 checks). Rejected IDs remain absent. Shard 031 was completed with 500 records, new shards `examples/032.json`, `examples/033.json`, `examples/034.json` (500 records each), and `examples/035.json` (179 records) are registered in the manifest. There are 104,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,628 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 91 at `sent.tatoeba.370950` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 17,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 91–110

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 91 | 200 | 194 | 6 | 0 |
| 92 | 200 | 195 | 5 | 0 |
| 93 | 200 | 189 | 11 | 0 |
| 94 | 200 | 191 | 9 | 0 |
| 95 | 200 | 189 | 11 | 0 |
| 96 | 200 | 199 | 1 | 0 |
| 97 | 200 | 199 | 1 | 0 |
| 98 | 200 | 200 | 0 | 0 |
| 99 | 200 | 198 | 2 | 0 |
| 100 | 200 | 198 | 2 | 0 |
| 101 | 200 | 198 | 2 | 0 |
| 102 | 200 | 199 | 1 | 0 |
| 103 | 200 | 200 | 0 | 0 |
| 104 | 200 | 199 | 1 | 0 |
| 105 | 200 | 199 | 1 | 0 |
| 106 | 200 | 189 | 11 | 0 |
| 107 | 200 | 195 | 5 | 0 |
| 108 | 200 | 198 | 2 | 0 |
| 109 | 200 | 198 | 2 | 0 |
| 110 | 200 | 197 | 3 | 0 |
| Total | 4,000 | 3,924 | 76 | 0 |

All 4,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Near duplicates and intra-slice duplicate variations were removed during review. All 76 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 21,824 decisions, 19,390 published, 2,434 rejected and 246 disclosed edits. Runtime: 21,603 examples, 23,491 sentence records and 34,386 rich records; ledger: 36,820 applied decisions (34,386 publication and 2,434 deprecated). This continuation adds 3,924 examples, leaving 78,397 more reviewed publications to reach 100,000. All 19,390 English-only approved objects match runtime exactly and pass both adapters (38,780 checks). Rejected IDs remain absent. Shard 035 was completed with 500 records, new shards `examples/036.json`, `examples/037.json`, `examples/038.json`, `examples/039.json`, `examples/040.json`, `examples/041.json`, `examples/042.json` (500 records each), and `examples/043.json` (103 records) are registered in the manifest. There are 100,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,552 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 111 at `sent.tatoeba.803149` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 21,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 111–200

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 111 | 200 | 197 | 3 | 0 |
| 112 | 200 | 200 | 0 | 0 |
| 113 | 200 | 196 | 4 | 0 |
| 114 | 200 | 199 | 1 | 0 |
| 115 | 200 | 198 | 2 | 0 |
| 116 | 200 | 199 | 1 | 0 |
| 117 | 200 | 195 | 5 | 0 |
| 118 | 200 | 196 | 4 | 0 |
| 119 | 200 | 196 | 4 | 0 |
| 120 | 200 | 191 | 9 | 0 |
| 121 | 200 | 196 | 4 | 0 |
| 122 | 200 | 197 | 3 | 0 |
| 123 | 200 | 196 | 4 | 0 |
| 124 | 200 | 192 | 8 | 0 |
| 125 | 200 | 189 | 11 | 0 |
| 126 | 200 | 197 | 3 | 0 |
| 127 | 200 | 192 | 8 | 0 |
| 128 | 200 | 191 | 9 | 0 |
| 129 | 200 | 191 | 9 | 0 |
| 130 | 200 | 179 | 21 | 0 |
| 131 | 200 | 189 | 11 | 0 |
| 132 | 200 | 192 | 8 | 0 |
| 133 | 200 | 182 | 18 | 0 |
| 134 | 200 | 184 | 16 | 0 |
| 135 | 200 | 165 | 35 | 0 |
| 136 | 200 | 169 | 31 | 0 |
| 137 | 200 | 191 | 9 | 0 |
| 138 | 200 | 175 | 25 | 0 |
| 139 | 200 | 181 | 19 | 0 |
| 140 | 200 | 195 | 5 | 0 |
| 141 | 200 | 185 | 15 | 0 |
| 142 | 200 | 180 | 20 | 0 |
| 143 | 200 | 190 | 10 | 0 |
| 144 | 200 | 188 | 12 | 0 |
| 145 | 200 | 190 | 10 | 0 |
| 146 | 200 | 178 | 22 | 0 |
| 147 | 200 | 168 | 32 | 0 |
| 148 | 200 | 199 | 1 | 0 |
| 149 | 200 | 196 | 4 | 0 |
| 150 | 200 | 193 | 7 | 0 |
| 151 | 200 | 199 | 1 | 0 |
| 152 | 200 | 193 | 7 | 0 |
| 153 | 200 | 197 | 3 | 0 |
| 154 | 200 | 196 | 4 | 0 |
| 155 | 200 | 195 | 5 | 0 |
| 156 | 200 | 198 | 2 | 0 |
| 157 | 200 | 197 | 3 | 0 |
| 158 | 200 | 184 | 16 | 0 |
| 159 | 200 | 178 | 22 | 0 |
| 160 | 200 | 189 | 11 | 0 |
| 161 | 200 | 187 | 13 | 0 |
| 162 | 200 | 183 | 17 | 0 |
| 163 | 200 | 188 | 12 | 0 |
| 164 | 200 | 171 | 29 | 0 |
| 165 | 200 | 185 | 15 | 0 |
| 166 | 200 | 185 | 15 | 0 |
| 167 | 200 | 195 | 5 | 0 |
| 168 | 200 | 190 | 10 | 0 |
| 169 | 200 | 183 | 17 | 0 |
| 170 | 200 | 186 | 14 | 0 |
| 171 | 200 | 185 | 15 | 0 |
| 172 | 200 | 191 | 9 | 0 |
| 173 | 200 | 194 | 6 | 0 |
| 174 | 200 | 192 | 8 | 0 |
| 175 | 200 | 178 | 22 | 0 |
| 176 | 200 | 184 | 16 | 0 |
| 177 | 200 | 193 | 7 | 0 |
| 178 | 200 | 183 | 17 | 0 |
| 179 | 200 | 192 | 8 | 0 |
| 180 | 200 | 187 | 13 | 0 |
| 181 | 200 | 185 | 15 | 0 |
| 182 | 200 | 194 | 6 | 0 |
| 183 | 200 | 185 | 15 | 0 |
| 184 | 200 | 191 | 9 | 0 |
| 185 | 200 | 195 | 5 | 0 |
| 186 | 200 | 184 | 16 | 0 |
| 187 | 200 | 186 | 14 | 0 |
| 188 | 200 | 182 | 18 | 0 |
| 189 | 200 | 188 | 12 | 0 |
| 190 | 200 | 195 | 5 | 0 |
| 191 | 200 | 186 | 14 | 0 |
| 192 | 200 | 186 | 14 | 0 |
| 193 | 200 | 187 | 13 | 0 |
| 194 | 200 | 184 | 16 | 0 |
| 195 | 200 | 185 | 15 | 0 |
| 196 | 200 | 190 | 10 | 0 |
| 197 | 200 | 191 | 9 | 0 |
| 198 | 200 | 189 | 11 | 0 |
| 199 | 200 | 181 | 19 | 0 |
| 200 | 200 | 193 | 7 | 0 |
| Total | 18,000 | 16,992 | 1,008 | 0 |

All 18,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Near duplicates and intra-slice duplicate variations were removed during review. All 1,008 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 39,824 decisions, 36,382 published, 3,442 rejected and 246 disclosed edits. Runtime: 38,595 examples, 40,483 sentence records and 51,378 rich records; ledger: 54,820 applied decisions (51,378 publication and 3,442 deprecated). This continuation adds 16,992 examples, leaving 61,405 more reviewed publications to reach 100,000. All 36,382 English-only approved objects match runtime exactly and pass both adapters (72,764 checks). Rejected IDs remain absent. Shard 043 was completed with 500 records, new shards `examples/044.json` through `examples/076.json` (500 records each), and `examples/077.json` (95 records) are registered in the manifest. There are 82,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,544 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 201 at `sent.tatoeba.3597719` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 39,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 201–300

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 201 | 200 | 190 | 10 | 0 |
| 202 | 200 | 193 | 7 | 0 |
| 203 | 200 | 189 | 11 | 0 |
| 204 | 200 | 186 | 14 | 0 |
| 205 | 200 | 191 | 9 | 0 |
| 206 | 200 | 195 | 5 | 0 |
| 207 | 200 | 198 | 2 | 0 |
| 208 | 200 | 191 | 9 | 0 |
| 209 | 200 | 188 | 12 | 0 |
| 210 | 200 | 191 | 9 | 0 |
| 211 | 200 | 185 | 15 | 0 |
| 212 | 200 | 185 | 15 | 0 |
| 213 | 200 | 193 | 7 | 0 |
| 214 | 200 | 189 | 11 | 0 |
| 215 | 200 | 192 | 8 | 0 |
| 216 | 200 | 187 | 13 | 0 |
| 217 | 200 | 182 | 18 | 0 |
| 218 | 200 | 189 | 11 | 0 |
| 219 | 200 | 192 | 8 | 0 |
| 220 | 200 | 186 | 14 | 0 |
| 221 | 200 | 190 | 10 | 0 |
| 222 | 200 | 194 | 6 | 0 |
| 223 | 200 | 193 | 7 | 0 |
| 224 | 200 | 189 | 11 | 0 |
| 225 | 200 | 181 | 19 | 0 |
| 226 | 200 | 190 | 10 | 0 |
| 227 | 200 | 186 | 14 | 0 |
| 228 | 200 | 192 | 8 | 0 |
| 229 | 200 | 195 | 5 | 0 |
| 230 | 200 | 177 | 23 | 0 |
| 231 | 200 | 184 | 16 | 0 |
| 232 | 200 | 184 | 16 | 0 |
| 233 | 200 | 187 | 13 | 0 |
| 234 | 200 | 179 | 21 | 0 |
| 235 | 200 | 178 | 22 | 0 |
| 236 | 200 | 181 | 19 | 0 |
| 237 | 200 | 191 | 9 | 0 |
| 238 | 200 | 186 | 14 | 0 |
| 239 | 200 | 194 | 6 | 0 |
| 240 | 200 | 181 | 19 | 0 |
| 241 | 200 | 181 | 19 | 0 |
| 242 | 200 | 188 | 12 | 0 |
| 243 | 200 | 178 | 22 | 0 |
| 244 | 200 | 185 | 15 | 0 |
| 245 | 200 | 183 | 17 | 0 |
| 246 | 200 | 190 | 10 | 0 |
| 247 | 200 | 188 | 12 | 0 |
| 248 | 200 | 190 | 10 | 0 |
| 249 | 200 | 187 | 13 | 0 |
| 250 | 200 | 185 | 15 | 0 |
| 251 | 200 | 188 | 12 | 0 |
| 252 | 200 | 192 | 8 | 0 |
| 253 | 200 | 193 | 7 | 0 |
| 254 | 200 | 178 | 22 | 0 |
| 255 | 200 | 194 | 6 | 0 |
| 256 | 200 | 194 | 6 | 0 |
| 257 | 200 | 184 | 16 | 0 |
| 258 | 200 | 185 | 15 | 0 |
| 259 | 200 | 186 | 14 | 0 |
| 260 | 200 | 185 | 15 | 0 |
| 261 | 200 | 192 | 8 | 0 |
| 262 | 200 | 181 | 19 | 0 |
| 263 | 200 | 184 | 16 | 0 |
| 264 | 200 | 187 | 13 | 0 |
| 265 | 200 | 179 | 21 | 0 |
| 266 | 200 | 185 | 15 | 0 |
| 267 | 200 | 175 | 25 | 0 |
| 268 | 200 | 180 | 20 | 0 |
| 269 | 200 | 186 | 14 | 0 |
| 270 | 200 | 166 | 34 | 0 |
| 271 | 200 | 177 | 23 | 0 |
| 272 | 200 | 182 | 18 | 0 |
| 273 | 200 | 191 | 9 | 0 |
| 274 | 200 | 194 | 6 | 0 |
| 275 | 200 | 196 | 4 | 0 |
| 276 | 200 | 194 | 6 | 0 |
| 277 | 200 | 197 | 3 | 0 |
| 278 | 200 | 199 | 1 | 0 |
| 279 | 200 | 197 | 3 | 0 |
| 280 | 200 | 192 | 8 | 0 |
| 281 | 200 | 199 | 1 | 0 |
| 282 | 200 | 192 | 8 | 0 |
| 283 | 200 | 189 | 11 | 0 |
| 284 | 200 | 198 | 2 | 0 |
| 285 | 200 | 189 | 11 | 0 |
| 286 | 200 | 190 | 10 | 0 |
| 287 | 200 | 194 | 6 | 0 |
| 288 | 200 | 194 | 6 | 0 |
| 289 | 200 | 187 | 13 | 0 |
| 290 | 200 | 190 | 10 | 0 |
| 291 | 200 | 191 | 9 | 0 |
| 292 | 200 | 189 | 11 | 0 |
| 293 | 200 | 189 | 11 | 0 |
| 294 | 200 | 188 | 12 | 0 |
| 295 | 200 | 194 | 6 | 0 |
| 296 | 200 | 192 | 8 | 0 |
| 297 | 200 | 179 | 21 | 0 |
| 298 | 200 | 186 | 14 | 0 |
| 299 | 200 | 191 | 9 | 0 |
| 300 | 200 | 192 | 8 | 0 |
| Total | 20,000 | 18,805 | 1,195 | 0 |

All 20,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Near duplicates and intra-slice duplicate variations were removed during review. All 1,195 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 59,824 decisions, 55,187 published, 4,637 rejected and 246 disclosed edits. Runtime: 57,400 examples, 59,288 sentence records and 70,183 rich records; ledger: 74,820 applied decisions (70,183 publication and 4,637 deprecated). This continuation adds 18,805 examples, leaving 42,600 more reviewed publications to reach 100,000. All 55,187 English-only approved objects match runtime exactly and pass both adapters (110,374 checks). Rejected IDs remain absent. Shard 077 was completed with 500 records, new shards `examples/078.json` through `examples/113.json` (500 records each), and `examples/114.json` (400 records) are registered in the manifest. There are 62,361 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,349 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `258069e4e7f10c8c45591fc2e66920d2af9179da` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 301 at `sent.tatoeba.5738175` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 59,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.
