# English content — four sequential execution groups

User instruction: execute the twelve agreed work items as four groups of three. Review each step before starting the next; complete and review a group before entering the following group. A blocked or partially completed step is never a PASS.

## Review rules

- PASS requires the stated deliverable, explicit editorial/source review, applicable executable gates and current evidence. Candidate counts and published counts are distinct.
- Every content promotion requires source/version/license/provenance verification, grammar/naturalness/CEFR review, exact/near dedup, a digest-bound decision and compatible game runtime output.
- Reproduce affected artifacts, reconcile E10/E11/E12, then verify Full Validation, Master Plan Acceptance and Platform CI on the resulting branch HEAD.
- When a step is blocked, record the exact missing input and evidence. Later steps stay queued. Do not relax a checksum, invent a source, mass-publish unchecked records, or redefine a long-term target as completed tooling work.
- Resume from the latest remote HEAD and this plan together with `ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md`. Preserve existing reviewed work.

## Group 1 — current queue, example corpus, translation source

| Step | Deliverable and PASS criterion | Current reviewed state |
| --- | --- | --- |
| 1 | Review all 316 candidates remaining after Slice 29; publish only eligible records. Verify the final four-record slice and an exhausted next-review queue without replaying old records. All content/runtime/report/CI gates pass. | PASS — all 316 reviewed/published; three workflows passed on `565659b` |
| 2 | Expand reviewed, published examples to the agreed minimum of 100,000 using reproducible, licensed source intake. Source capacity, editorial quality and runtime counts must independently support the result. | IN PROGRESS — new pinned English-only intake and thirty editorial batches integrated; 6,645 published examples. Candidate capacity is available; remaining editorial work is not approved. |
| 3 | Recover exact pinned Tatoeba EN/VI/link bytes, or complete a separately versioned, fully reviewed source upgrade with checksums, license and attribution. Import validation and reproducibility pass. | Queued behind Step 2; historical source bytes currently unavailable |

The default typing-text candidate queue is bounded at 1,000 candidates. Exhausting that queue is Step 1 completion, not exhaustion of all original passages and not completion of Step 2.

## Group 2 — translation and dialogue expansion

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 4 | At least 20,000 reviewed published translation pairs; validate alignment, translation quality, licensing, dedup and runtime. | Queued behind Group 1 |
| 5 | Add a reproducible, licensed dialogue source or reviewed source extension; pin bytes/version, verify attribution and provide an audited import pilot. The configured MultiWOZ lane is exhausted. | Queued behind Step 4 |
| 6 | At least 10,000 reviewed published dialogues, with speaker/turn/context integrity and game compatibility. | Queued behind Step 5 |

## Group 3 — exercise and error corpora

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 7 | At least 30,000 published cloze exercises with valid source sentences, target presence and unambiguous accepted answers. | Queued behind Group 2 |
| 8 | At least 10,000 published transformations; verify meaning preservation, target grammar and accepted alternatives. | Queued behind Step 7 |
| 9 | At least 2,000 published common-mistake records with reviewed corrections, explanations and grammar references. | Queued behind Step 8 |

## Group 4 — example linkage, game review, release

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 10 | Review the outstanding example-link debt (baseline: 4,992 collocations, 504 verb patterns, 4,159 phrase items without `exampleIds`). Add only semantically correct whole-phrase/frame evidence; document unresolved coverage. No unsafe lemma-only auto-linking. | Queued behind Group 3 |
| 11 | Exercise the actual English-content selection/display/play/result flows in the integrated games. Record findings and fix material issues; re-run affected checks. CI alone does not claim manual UI review. | Queued behind Step 10 |
| 12 | Complete PR review and release readiness; merge/release only after preceding review gates pass and final checks are current. | Queued behind Step 11; PR #48 remains Draft |

## Review evidence

Step 1 uses explicit decisions in `content/english/reviews/decisions.d/e06-typing-text-30-*.json` through `e06-typing-text-43-*.json`, authoring shards, generated runtime/manifests and E10/E11/E12 reports. The queue-tail fix is covered by `scripts/typing-text-review-core.test.mjs`, including CLI stale-packet replacement for partial and exhausted queues. Record final CI run links in PR #48; do not create a timestamp-only commit solely to move CI to another SHA.

## Step 1 sign-off and Step 2 capacity review

Step 1 passed on commit `565659b885ffe52e1abdcddfd93c97808e563334`:

- [Platform CI #3201](https://github.com/sinhvienaiti/typing-game/actions/runs/42333877164) — success.
- [Master Plan Acceptance #1312](https://github.com/sinhvienaiti/typing-game/actions/runs/42333877161) — success.
- [Full Validation #952](https://github.com/sinhvienaiti/typing-game/actions/runs/42333874055) — success.
- 90 content/tooling tests, 3 runtime-count tests, all 316 Monkeytype/Karaoke adapter checks, all 28 linked lexical references, exact/near dedup and deterministic artifact regeneration passed.

Step 2 was then assessed with `node scripts/audit-english-example-source-capacity.mjs`. The reproducible report is `content/english/reports/example-source-capacity.json`.

| Capacity measure | Count |
| --- | ---: |
| Reviewed published examples | 6,645 |
| Required minimum | 100,000 |
| Current published deficit | 93,355 |
| Eligible unique raw sentences in the current original-source lane | 5,588 |
| Raw sentences not yet reviewed | 4,588 |
| Optimistic published upper bound using only remaining original-source raw sentences | 11,233 |
| Additional source gap if restricted to that original lane | 88,767 |

The upper bound covers this configured source lane only. It is not an assertion that no other upstream dataset exists. Further local review is possible, but does not make the full Step 2 deliverable achievable from these inputs alone; future rejection/dedup can reduce the bound. Other upstream sources require a reproducible, licensed, reviewed intake before their potential size can be counted.

### Active continuation: pinned English-only Tatoeba lane

The original-lane shortage is no longer an overall stop condition. Four official 2026-10-31 exports were acquired and checksum-verified on 2026-11-07. A separately versioned offline extraction retains 122,212 English source-evidence candidates in five canonical shards. See `docs/TATOEBA_ENGLISH_INTAKE.md` and `content/english/sources/tatoeba-english-2026-10-31.json`. The historical EN/VI/link pin is unchanged.

Pilot 01 explicitly reviewed 24 records: 20 published, four rejected and two edited. The digest-bound ledger, controlled source and per-record review report retain all outcomes, original/final texts, CEFR rationales and attribution. Rejections include a threat and context/factual-scope problems despite positive experimental source ratings. The queue skips these decisions permanently.

After all 5,824 local decisions and excluding controlled IDs/texts and exact source duplicates, 116,362 candidates remain available. Combined with the original-source remainder, the optimistic intake bound is 127,595 examples before further editorial rejection and cross-source near dedup. Candidate availability does not establish that all of those examples will pass. The capacity report is now version 2 with separate original and new-source lanes, `editorial-review-required`, and every transition gate still false.

Local validation: 112 content/tooling tests plus three runtime-count tests; complete schema/source/review/license checks, E10, actual published-runtime smoke, E11 record coverage/reconciliation, E12 and master-plan audit. The source snapshot also reproduces byte-for-byte from all four pinned upstream inputs. Compare the resulting remote HEAD's three workflow runs in PR #48 before signing off that implementation batch.

Step 2 completion review is **not passed**. Group 1 is **not complete**. Steps 3–12 remain queued, following the user's strict transition rule. Continue bounded editorial review from `node scripts/prepare-tatoeba-english-review.mjs --limit 200`; do not stop merely because the original source lane is too small, and do not count the remaining candidate backlog as reviewed publication.

### Editorial continuation: batches 02 and 03

A further 400 candidates received individual editorial decisions: batch 02 accepted 181 and rejected 19; batch 03 accepted 176 and rejected 24. Eight accepted records have disclosed edits, including an ambiguous multiplicative comparison, place-name agreement, compound punctuation, a precise relative clause and an expanded physical-education abbreviation. The two reports retain every original/final text, rationale, CEFR and source digest.

After batches 02 and 03, the English-only lane had reviewed 424 records, published 377 and rejected 47; the runtime at that checkpoint contained 2,590 examples and 15,373 rich records. Exact/near lexical dedup also passes against the existing runtime and within the new batches. Pragmatic duplicates were explicitly rejected even when their token overlap was below the numerical threshold.

Self-review detected that readiness counted only the first explicitly configured English-only shard. E11 readiness and record coverage now discover every registered English-only batch from the manifest and apply the digest-bound review overlay. A regression checks each batch is counted exactly once and that deprecated/unapproved records do not increase its count. The redundant first-shard target entry was removed; locked targets are unchanged. E12 release snapshots must be refreshed before the final E11 readiness/runtime reconciliation, because readiness embeds release bytes.

The source integration checkpoint `bb0ce40898a6975f108760da91b5faed15f3670e` passed all three remote workflows: [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42357377757), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42357377770), [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42357372993). Verify the continuation commit's workflows separately before sign-off. Step 2 remains in progress; it has not met 100,000 published examples.

### Editorial continuation: batches 04–06

| Batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 04 | 200 | 179 | 21 | 4 |
| 05 | 200 | 172 | 28 | 8 |
| 06 | 200 | 180 | 20 | 6 |
| Total | 600 | 531 | 69 | 18 |

Every candidate has an individual rationale. Rejections include unsupported factual/medical/legal generalizations, insufficiently framed quotations, unsuitable standalone wording and lexical/pragmatic duplicates. An inverted counterfactual was rejected after exact Jaccard review found 0.9333 overlap with the selected non-inverted sentence. Eighteen accepted edits address collocations, punctuation, tense, comparison ambiguity and self-contained wording; source modification markers and decision digests were refreshed. Self-review simplified one initially overcomplicated responsibility paraphrase and reassessed its CEFR.

At the end of batches 04–06, the English-only lane had reviewed 1,024 candidates: 908 published and 116 rejected, with 28 disclosed edits. Runtime at that checkpoint: 3,121 examples, 5,009 sentence records and 15,904 rich records; ledger: 16,020 decisions. All 908 approved English-only records pass both Monkeytype and Karaoke adapters (1,816 checks). Rejected IDs remain excluded from runtime and future packets. Source/version/license pins and legacy vocabulary output are unchanged.

The prior continuation `e81e3e48def60bd04386f003fce509f300d42a0d` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42358545415), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42358545421) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42358540969). Record the new continuation HEAD's checks in PR #48 after publication. At that checkpoint the remaining reviewed-publication deficit was 96,879; Step 2 and Group 1 had not passed.

### Editorial continuation: batches 07–09

| Batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 07 | 200 | 160 | 40 | 3 |
| 08 | 200 | 171 | 29 | 5 |
| 09 | 200 | 169 | 31 | 4 |
| Total | 600 | 500 | 100 | 12 |

All 600 candidates received individual decisions and rationale. Review rejected unsupported biological universals, unscoped current economic/medical assertions, insufficiently framed quotations and pragmatic repeats. Twelve disclosed edits improve written-register wording, compound punctuation, fixed expressions and standalone questions while preserving source meaning. Exact source evidence and intake/controlled digests are retained; rejected IDs never re-enter the queue.

At the end of batches 07–09: 1,624 decisions, 1,408 published, 216 rejected and 40 disclosed edits. Runtime at that checkpoint: 3,621 examples, 5,509 sentence records and 16,404 rich records; ledger: 16,620 decisions. All 1,408 approved English-only records pass both adapters (2,816 checks). That checkpoint had 120,562 unreviewed candidates, not approved publications, and a remaining reviewed-publication deficit of 96,379. Step 2 remains IN PROGRESS; Steps 3–12 stay queued.

Prior checkpoint `88802d34bb7ea4049c23f6a4ca8f674f9ab35c47` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42364035182), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42364035316) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42364030575). Verify the new continuation's exact HEAD and record its workflow evidence in PR #48. Preserve the source pin, reviewed-only publication, deterministic generation and E12-before-final-E11 reconciliation order.

### Editorial continuation within Step 2: English batches 10–12

These batch numbers identify English-only editorial packets; they do not mean execution Steps 10–12 have opened.

| English batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 10 | 200 | 165 | 35 | 2 |
| 11 | 200 | 167 | 33 | 1 |
| 12 | 200 | 168 | 32 | 6 |
| Total | 600 | 500 | 100 | 9 |

All 600 candidates received explicit decisions and rationale. Review removed pragmatic repeats, unsupported historical/biological universals, unsafe unqualified medical/travel assertions and unsuitable standalone wording. Nine disclosed edits clarify fixed expressions, written punctuation, collocations and complete questions without inventing new source events. Self-review also checked edited final texts against active canonical sentence sources; no exact authoring collision was found. Source/controlled digests and modification disclosure remain intact.

At the end of twelve English-only batches: 2,224 decisions, 1,908 published, 316 rejected and 49 disclosed edits. Runtime: 4,121 examples, 6,009 sentence records and 16,904 rich records; ledger: 17,220 decisions. All 1,908 approved English-only examples pass both adapters (3,816 checks). That checkpoint had 119,962 unreviewed candidates and a reviewed-publication deficit of 95,879; Step 2 remains IN PROGRESS and execution Steps 3–12 remain queued.

Prior checkpoint `80b46dcd9ba8185ccf6a4850b6007e1b9e726219` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42367756978), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42367756974) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42367751864). Verify the continuation HEAD separately and record its workflows in PR #48. Source pins, locked targets, reviewed-only publication and sequential transition gates are unchanged.

### Editorial continuation within Step 2: English batches 13–15

| English batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 13 | 200 | 143 | 57 | 6 |
| 14 | 200 | 143 | 57 | 2 |
| 15 | 200 | 141 | 59 | 6 |
| Total | 600 | 427 | 173 | 14 |

Every candidate was read and given an individual decision. Review rejected unscoped current, scientific and health assertions, ambiguous or context-only wording, unsuitable general-learning material and pragmatic repeats. Cross-corpus review removed further paraphrases even below the numerical near-duplicate threshold, including the different cookie-crumbles/ball-bounces metaphors for the same acceptance sentiment. Fourteen disclosed edits repair tense consistency, fixed expressions, punctuation, collocations and explicit weather-forecast attribution while preserving source meaning. All final accepted texts were checked against active canonical records; no exact collision was found. Original/final text, rationale, source evidence, CEFR and digest-bound decisions remain traceable in the three per-record reports.

At the end of batches 13–15, English-only totals were: 2,824 decisions, 2,335 published, 489 rejected and 63 disclosed edits. Full runtime: 4,548 examples, 6,436 sentence records and 17,331 rich records. Ledger: 17,820 decisions. All 2,335 approved English-only examples pass both adapters (4,670 checks), match runtime objects exactly and exclude rejected IDs. That checkpoint queue skipped every reviewed ID and had 119,362 unreviewed candidates, beginning at `sent.tatoeba.41120`; English editorial batch 16 followed. The published deficit at that checkpoint was 95,452. Step 2 is IN PROGRESS; Steps 3–12 stay queued and PR #48 stays Draft.

Local verification passed 112 configured content/tooling tests, ten additional MultiWOZ handoff/decision tests and three runtime-count tests, plus schema/source/review/license/E10, publication, exact/near dedup, published-runtime smoke, E12, E11 count freshness/ID coverage, capacity and master-plan reconciliation. Release/maintenance was refreshed before final E11 readiness/runtime generation. Regeneration and shard tracking are verified before pushing; record the final HEAD's three workflow results in PR #48.

The verified preceding checkpoint `0d88f8272cbf868733cd6faa5f877d1867345ef8` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42379829061), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42379829041) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42379823439). Source/license pins, legacy vocabulary ABI and the historical translation lane remain unchanged. No CI result or candidate capacity count satisfies the 100,000-example requirement.

### Editorial continuation within Step 2: English batches 16–18

| English batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 16 | 200 | 103 | 97 | 2 |
| 17 | 200 | 151 | 49 | 3 |
| 18 | 200 | 164 | 36 | 4 |
| Total | 600 | 418 | 182 | 9 |

Every candidate received an individual reading, decision and rationale. Batch 16 had substantial context-only material; unspecified referents, unbounded assertions and unsuitable wording were rejected rather than supplied with invented contexts. Cross-corpus review also rejected semantic repeats below the numerical token-overlap threshold. Examples include repeated hearing-news/turning-pale scenes and a paraphrase of the published millionaire acquiring a masterpiece regardless of cost. Nine disclosed edits address conditional wording, natural collocations, a role term, compound punctuation, photo background wording and an empty-dish completion expression without adding source events. Edited final texts were checked against all active canonical sentence sources; no exact collision was found.

At the end of batches 16–18, English-only totals were: 3,424 decisions, 2,753 published, 671 rejected and 72 disclosed edits. Full runtime: 4,966 examples, 6,854 sentence records and 17,749 rich records; ledger: 18,420 applied decisions. All 2,753 published English-only records match the approved controlled objects and pass both adapters (5,506 checks). Rejected records remain absent from runtime and future packets. That checkpoint queue skipped every reviewed ID, contained 118,762 unreviewed candidates and begins at `sent.tatoeba.45621`; English editorial batch 19 followed. That checkpoint target deficit was 95,034 reviewed publications.

Local checks passed 112 configured content/tooling tests, ten additional MultiWOZ handoff/decision tests and three runtime-count tests, alongside schema/source/review/license/E10, publication, exact/near dedup, published-runtime smoke, E12, E11 freshness/exact ID coverage, capacity and master-plan reconciliation. E12 release/maintenance precedes final E11 readiness/runtime regeneration. Verify deterministic artifacts and tracked manifest shards before pushing, then record the final HEAD's three workflows in PR #48.

The preceding checkpoint `754c83d9e0201e8038e62069c97cf36c9573fdf9` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42382049497), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42382049519) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42382044706). Source pins, legacy vocabulary ABI, locked targets and sequential gates are unchanged. Step 2 remains IN PROGRESS; Group 1 is incomplete, Steps 3–12 remain queued and PR #48 stays Draft. Candidate capacity and CI success are not completion of the 100,000-example deliverable.

### Preceding editorial checkpoint within Step 2: English batches 19–21

| English batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 19 | 200 | 159 | 41 | 6 |
| 20 | 200 | 156 | 44 | 1 |
| 21 | 200 | 142 | 58 | 2 |
| Total | 600 | 457 | 143 | 9 |

All 600 candidates received an individual reading, decision and rationale. Review rejected unsupported current legal/health/geographic assertions, unsuitable standalone material, missing contexts and exact or semantic repeats. Identified repeats include multiple careless-driving accident causes, the fifteen-member committee, a company's gold-watch recognition gift and a house burning to the ground. Token overlap alone did not determine these editorial rejections. Nine disclosed edits clarify a British one-and-a-half-times comparison, natural collocations, a beverage article, a missing incident article, temporal wording and a past-tense verb. Source meaning, original/final wording, attribution and intake/controlled digests remain traceable; edited final text was checked against all active canonical sentence sources.

At the end of batches 19–21, English-only totals were: 4,024 decisions, 3,210 published, 814 rejected and 81 disclosed edits. Runtime then contained 5,423 examples, 7,311 sentence records and 18,206 rich records; ledger: 19,020 applied decisions. All 3,210 approved English-only records exactly match runtime and pass both adapters (6,420 checks); rejected IDs remain absent. The example manifest now references the new `examples/010.json` shard. That checkpoint queue skipped all reviewed IDs, contained 118,162 unreviewed candidates and began at `sent.tatoeba.49931`; English editorial batch 22 followed. That checkpoint publication deficit was 94,577.

Local verification passed 112 configured content/tooling tests, ten additional handoff/decision tests and three runtime-count tests, with schema/source/review/license/E10, publication, exact/near dedup, runtime smoke, E12, E11 freshness/exact ID coverage, capacity and master-plan checks. E12 release/maintenance precedes the final E11 regeneration. Verify deterministic artifacts and every referenced shard, including the new shard, before pushing and recording exact-HEAD workflow results in PR #48.

The preceding checkpoint `686d4dd7371d00be0247ef7014d4177449f40894` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42383982367), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42383982357) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42383978080). Source pins, legacy vocabulary ABI, locked targets and sequential gates are unchanged. Step 2 remains IN PROGRESS; Group 1 is incomplete, Steps 3–12 remain queued and PR #48 stays Draft. No candidate count or engineering-check result completes the 100,000-example target.

### Editorial continuation within Step 2: English batches 22–30

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

Current English-only totals: 5,824 decisions, 4,432 published, 1,392 rejected and 98 disclosed edits. Full runtime: 6,645 examples, 8,533 sentence records and 19,428 rich records; ledger: 20,820 applied decisions (19,428 publication and 1,392 deprecated). All 4,432 approved English-only records match runtime exactly and pass Monkeytype and Karaoke adapters (8,864 checks). Rejected IDs remain absent from runtime and future review packets. The example manifest now includes `examples/011.json`, `examples/012.json` and `examples/013.json`; the last shard contains 145 records. There are 116,362 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 127,595 before further rejection/dedup; none of this candidate capacity counts as publication. The reviewed-publication deficit is 93,355.

Local validation passes schema/source/review/license gates, E10 batch contracts and smoke, 112 content/tooling tests, 10 MultiWOZ handoff/decision tests, publication, dedup, published-runtime smoke, three runtime-count tests, E11 freshness and exact source/runtime coverage, capacity and master-plan reports. E12 release/maintenance snapshots are refreshed before final E11 readiness/runtime generation. Verify deterministic regeneration and commit every runtime shard referenced by the manifest before push. No engineering result satisfies the 100,000-example gate.

The verified preceding checkpoint `ae519d789235eddf44e397a603c7a4b5e04f5bab` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42387866884), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42387866873) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42387862671). Verify the resulting continuation HEAD separately and record those workflow links in PR #48; this file intentionally names the previously verified SHA to avoid a self-referential SHA-only commit.

Continue English editorial batch 31 at `sent.tatoeba.67208` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. This remains execution Group 1 Step 2. Steps 3–12 remain queued; PR #48 stays Draft. Source/license pins, the historical EN/VI/link lane and legacy vocabulary ABI remain unchanged.
