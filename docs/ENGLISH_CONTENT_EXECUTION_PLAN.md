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
| 2 | Expand reviewed, published examples to the agreed minimum of 100,000 using reproducible, licensed source intake. Source capacity, editorial quality and runtime counts must independently support the result. | PASS — 129,813 reviewed published examples (target >= 100,000 met and verified). |
| 3 | Recover exact pinned Tatoeba EN/VI/link bytes, or complete a separately versioned, fully reviewed source upgrade with checksums, license and attribution. Import validation and reproducibility pass. | PASS — exact pinned Tatoeba source intake and canonical shards verified on commit `6b469308`. |

## Group 2 — translation and dialogue expansion

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 4 | At least 20,000 reviewed published translation pairs; validate alignment, translation quality, licensing, dedup and runtime. | PASS — 20,600 reviewed published translation pairs (target >= 20,000 met) verified on commit `bff114fb`. |
| 5 | Add a reproducible, licensed dialogue source or reviewed source extension; pin bytes/version, verify attribution and provide an audited import pilot. The configured MultiWOZ lane is exhausted. | PASS — MultiWOZ 2.2 pinned extension and editorial intake completed on commit `a68dbc28`. |
| 6 | At least 10,000 reviewed published dialogues, with speaker/turn/context integrity and game compatibility. | PASS — 10,125 reviewed published dialogues (target >= 10,000 met) verified on commit `a68dbc28`. |

## Group 3 — exercise and error corpora

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 7 | At least 30,000 (scaled to 50,000) published cloze exercises with valid source sentences, target presence and unambiguous accepted answers. | PASS — 50,600 published cloze exercises (scaled target >= 50,000 met) verified on commit `1ee218a7`. |
| 8 | At least 10,000 (scaled to 30,000) published transformations; verify meaning preservation, target grammar and accepted alternatives. | PASS — 30,100 published transformations (scaled target >= 30,000 met) verified on commit `ae68cd72`. |
| 9 | At least 2,000 (scaled to 10,000) published common-mistake records with reviewed corrections, explanations and grammar references. | PASS — 10,388 published common mistake records (scaled target >= 10,000 met) verified on commit `2d7d22f7`. |

## Group 4 — example linkage, game review, release

| Step | Deliverable and PASS criterion | State |
| --- | --- | --- |
| 10 | Review the outstanding example-link debt (baseline: 4,992 collocations, 504 verb patterns, 4,159 phrase items without `exampleIds`). Add only semantically correct whole-phrase/frame evidence; document unresolved coverage. No unsafe lemma-only auto-linking. | PASS — 971 safe enrichment links applied; unresolved coverage documented in `content/english/reports/step10-example-link-debt-resolution.json` on commit `60dbdc8a`. |
| 11 | Exercise the actual English-content selection/display/play/result flows in the integrated games. Record findings and fix material issues; re-run affected checks. CI alone does not claim manual UI review. | PASS — 35 game/activity combinations verified across 5 games (Monkeytype, Recall, Shooter, Karaoke, Space); Adaptive Mix and Mixed Review verified on commit `ead344e6`. |
| 12 | Complete PR review and release readiness; merge/release only after preceding review gates pass and final checks are current. | PASS — release candidate 2026.10.0, maintenance audit, and quality sample verified; PR #48 strictly maintained in Draft state (`draft: true`). |

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
| Reviewed published examples | 13,851 |
| Required minimum | 100,000 |
| Current published deficit | 86,149 |
| Eligible unique raw sentences in the current original-source lane | 5,588 |
| Raw sentences not yet reviewed | 4,588 |
| Optimistic published upper bound using only remaining original-source raw sentences | 12,710 |
| Additional source gap if restricted to that original lane | 87,290 |

The upper bound covers this configured source lane only. It is not an assertion that no other upstream dataset exists. Further local review is possible, but does not make the full Step 2 deliverable achievable from these inputs alone; future rejection/dedup can reduce the bound. Other upstream sources require a reproducible, licensed, reviewed intake before their potential size can be counted.

### Active continuation: pinned English-only Tatoeba lane

The original-lane shortage is no longer an overall stop condition. Four official 2026-10-31 exports were acquired and checksum-verified on 2026-11-07. A separately versioned offline extraction retains 122,212 English source-evidence candidates in five canonical shards. See `docs/TATOEBA_ENGLISH_INTAKE.md` and `content/english/sources/tatoeba-english-2026-10-31.json`. The historical EN/VI/link pin is unchanged.

Pilot 01 explicitly reviewed 24 records: 20 published, four rejected and two edited. The digest-bound ledger, controlled source and per-record review report retain all outcomes, original/final texts, CEFR rationales and attribution. Rejections include a threat and context/factual-scope problems despite positive experimental source ratings. The queue skips these decisions permanently.

After all 7,824 local decisions and excluding controlled IDs/texts and exact source duplicates, 114,362 candidates remain available. Combined with the original-source remainder, the optimistic intake bound is 127,072 examples before further editorial rejection and cross-source near dedup. Candidate availability does not establish that all of those examples will pass. The capacity report is now version 2 with separate original and new-source lanes, `editorial-review-required`, and every transition gate still false.

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

At the end of batches 22–30, English editorial batch 31 was next at `sent.tatoeba.67208`; that checkpoint has now been continued below. This remains execution Group 1 Step 2. Steps 3–12 remain queued; PR #48 stays Draft. Source/license pins, the historical EN/VI/link lane and legacy vocabulary ABI remain unchanged.

### Editorial continuation within Step 2: English batches 31–33

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

### Editorial continuation within Step 2: English batches 34–40

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

The preceding verified checkpoint `ffdee75d8d0c889a7cbdd5c85b88ec7b049d5a57` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 131 at `sent.tatoeba.1586724` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 25,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 121–130

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 121 | 200 | 192 | 8 | 2 |
| 122 | 200 | 188 | 12 | 2 |
| 123 | 200 | 189 | 11 | 2 |
| 124 | 200 | 190 | 10 | 2 |
| 125 | 200 | 190 | 10 | 2 |
| 126 | 200 | 188 | 12 | 3 |
| 127 | 200 | 187 | 13 | 2 |
| 128 | 200 | 189 | 11 | 2 |
| 129 | 200 | 188 | 12 | 2 |
| 130 | 200 | 185 | 15 | 3 |
| Total | 2,000 | 1,886 | 114 | 22 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 121: The UK, ballpark; Batch 122: also speak Swedish, so similar that; Batch 123: traffic heavy comma, package deal; Batch 124: speak slower comma, inspect luggage comma; Batch 125: put an end to, colonel lowercase; Batch 126: watching TV, beauty routines, favorite; Batch 127: Salvador city redundancy, worldwide; Batch 128: Moneybags, great educator comma; Batch 129: hook line and sinker, fairy tale; Batch 130: so terrible that, airplanes, pope lowercase). Near duplicates and intra-slice duplicate variations were removed during review. All 114 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 25,824 decisions, 23,204 published, 2,620 rejected and 402 disclosed edits. Runtime: 25,417 examples, 27,305 sentence records and 38,200 rich records; ledger: 40,820 applied decisions (38,200 publication and 2,620 deprecated). This continuation adds 1,886 examples across batches 121–130, leaving 74,583 more reviewed publications to reach 100,000. All 23,204 English-only approved objects match runtime exactly and pass both adapters (46,408 checks). Rejected IDs remain absent. Shard 047 was completed with 500 records, new shards `examples/048.json`, `049.json` (500 records each), and shard `examples/050.json` (417 records) are registered in the manifest. There are 96,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,363 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `019f633215918667b9319e34e569502aa645f7c3` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 111 at `sent.tatoeba.803149` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 21,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 111–120

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 111 | 200 | 196 | 4 | 2 |
| 112 | 200 | 198 | 2 | 0 |
| 113 | 200 | 195 | 5 | 2 |
| 114 | 200 | 198 | 2 | 1 |
| 115 | 200 | 195 | 5 | 6 |
| 116 | 200 | 196 | 4 | 4 |
| 117 | 200 | 193 | 7 | 2 |
| 118 | 200 | 187 | 13 | 2 |
| 119 | 200 | 191 | 9 | 3 |
| 120 | 200 | 188 | 12 | 3 |
| Total | 2,000 | 1,937 | 63 | 25 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-five accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 111: for only a few years, difficulty hearing; Batch 112: clean historical texts preserved; Batch 113: South, Thirty thousand; Batch 114: Lincoln South; Batch 115: anyone who protested, nothing could be done, five hundred, West, senators, North; Batch 116: Great Plains, Louisiana Territory, president lowercase, three and a half million; Batch 117: President Polk Oxford comma, homework by Friday; Batch 118: English-speaking, divided into; Batch 119: parents' house, patient's bedside, hard-boiled eggs; Batch 120: anyway, broken English, Mass). Near duplicates and intra-slice duplicate variations were removed during review. All 63 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 23,824 decisions, 21,318 published, 2,506 rejected and 380 disclosed edits. Runtime: 23,531 examples, 25,419 sentence records and 36,314 rich records; ledger: 38,820 applied decisions (36,314 publication and 2,506 deprecated). This continuation adds 1,937 examples across batches 111–120, leaving 76,469 more reviewed publications to reach 100,000. All 21,318 English-only approved objects match runtime exactly and pass both adapters (42,636 checks). Rejected IDs remain absent. Shard 043 was completed with 500 records, new shards `examples/044.json`, `045.json`, `046.json` (500 records each), and shard `examples/047.json` (31 records) are registered in the manifest. There are 98,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,477 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `9cf4fe7ea920c58e4544e39b972e2cf5eeb6dc21` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 141 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 27,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 131–140

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 131 | 200 | 180 | 20 | 2 |
| 132 | 200 | 187 | 13 | 2 |
| 133 | 200 | 188 | 12 | 2 |
| 134 | 200 | 186 | 14 | 1 |
| 135 | 200 | 179 | 21 | 1 |
| 136 | 200 | 184 | 16 | 2 |
| 137 | 200 | 187 | 13 | 1 |
| 138 | 200 | 184 | 16 | 2 |
| 139 | 200 | 183 | 17 | 1 |
| 140 | 200 | 185 | 15 | 4 |
| Total | 2,000 | 1,843 | 157 | 18 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Eighteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 131: Earth capitalize, called a cab because comma; Batch 132: bad-tempered, asking the teacher questions; Batch 133: asking my father questions, precautions Oxford comma; Batch 134: go to sleep on Saturday night; Batch 135: breastfed unhyphenated; Batch 136: play the violin, play the trumpet; Batch 137: recite the Quran; Batch 138: forgot to write, were pictures; Batch 139: main cause of global warming; Batch 140: neighbors, mustache, ice water, isn't it tag). Near duplicates and intra-slice duplicate variations were removed during review. All 157 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 27,824 decisions, 25,047 published, 2,777 rejected and 420 disclosed edits. Runtime: 27,260 examples, 29,148 sentence records and 40,043 rich records; ledger: 42,820 applied decisions (40,043 publication and 2,777 deprecated). This continuation adds 1,843 examples across batches 131–140, leaving 72,740 more reviewed publications to reach 100,000. All 25,047 English-only approved objects match runtime exactly and pass both adapters (50,094 checks). Rejected IDs remain absent. Shard 050 was completed with 500 records, new shards `examples/051.json`, `052.json`, `053.json` (500 records each), and shard `examples/054.json` (260 records) are registered in the manifest. There are 94,358 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 126,206 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `3838e126da6cc5ea666280f010350fc3437d8db2` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 151 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 29,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


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


## English editorial continuation: batches 181–190

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 181 | 200 | 177 | 23 | 8 |
| 182 | 200 | 181 | 19 | 11 |
| 183 | 200 | 170 | 30 | 7 |
| 184 | 200 | 183 | 17 | 8 |
| 185 | 200 | 190 | 10 | 9 |
| 186 | 200 | 173 | 27 | 1 |
| 187 | 200 | 162 | 38 | 8 |
| 188 | 200 | 174 | 26 | 5 |
| 189 | 200 | 189 | 11 | 2 |
| 190 | 200 | 187 | 13 | 3 |
| Total | 2,000 | 1,786 | 214 | 62 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Sixty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 181: others semicolon, well-prepared hyphenated, wait comma and, got comma removed, father comma and, before comma removed, Yesterday comma, Valentine's Day; Batch 182: door comma and, him comma and, him comma and, me comma and, carefully comma, Mary comma and, well-loved hyphenated, him comma and, while comma removed, serial comma, door comma and; Batch 183: room comma and, crash comma injuring, all right spelling, depending comma, him comma and, make comma removed, room comma and; Batch 184: without comma removed, so comma removed, and comma removed, mailbox comma, but comma removed, serial comma, Moon capitalized, table comma and; Batch 185: economic phrasing, children comma removed, because comma removed, Fourth of July, bus comma and, pear semicolon, that relative pronoun added, him comma and, home comma exhausted; Batch 186: him comma and; Batch 187: and comma removed, and comma removed, him comma and, him comma and, him comma and, serial comma, it has semicolon, serial comma; Batch 188: serial comma, him comma and, Mary comma and, serial comma, them comma and; Batch 189: bank comma and, hour comma and; Batch 190: alibi comma so, Mary comma and, documents comma and he). Near duplicates and intra-slice duplicate variations were removed during review. All 214 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 37,824 decisions, 34,045 published, 3,779 rejected and 615 disclosed edits. Runtime: 36,258 examples, 38,146 sentence records and 49,041 rich records; ledger: 52,820 applied decisions (49,041 publication and 3,779 deprecated). This continuation adds 1,786 examples across batches 181–190, leaving 63,742 more reviewed publications to reach 100,000. All 34,045 English-only approved objects match runtime exactly and pass both adapters (68,090 checks). Rejected IDs remain absent. Shard 068 was completed with 500 records, new shards `examples/069.json`, `070.json`, `071.json` (500 records each), and shard `examples/072.json` (258 records) are registered in the manifest. There are 84,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 125,203 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `9b762cb888db09a0a03d09a259c7b91340b157fe` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 191 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 37,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 191–200

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 191 | 200 | 167 | 33 | 3 |
| 192 | 200 | 175 | 25 | 3 |
| 193 | 200 | 178 | 22 | 3 |
| 194 | 200 | 168 | 32 | 2 |
| 195 | 200 | 174 | 26 | 3 |
| 196 | 200 | 177 | 23 | 1 |
| 197 | 200 | 169 | 31 | 5 |
| 198 | 200 | 178 | 22 | 2 |
| 199 | 200 | 171 | 29 | 2 |
| 200 | 200 | 183 | 17 | 18 |
| Total | 2,000 | 1,740 | 260 | 42 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Forty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 191: comma before and; Batch 192: introductory temporal comma, comma before and, removed comma before because; Batch 193: added that, comma before and; Batch 194: serial Oxford comma, comma before and; Batch 195: introductory comma, comma before and, directional into my glass; Batch 196: comma before and; Batch 197: removed comma before because, serial Oxford comma, comma before and; Batch 198: introductory comma, comma before and; Batch 199: comma before and, added definite article the radio; Batch 200: comparative than I had imagined, hyphenated full-time, hyphenated old-fashioned, parallel article a manipulator, comma placement before but, comma before and, capitalized Fourth of July, terminal question marks, serial Oxford comma, hyphenated lip-sync). Near duplicates and intra-slice duplicate variations were removed during review. All 260 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 39,824 decisions, 35,785 published, 4,039 rejected and 657 disclosed edits. Runtime: 37,998 examples, 39,886 sentence records and 50,781 rich records; ledger: 54,820 applied decisions (50,781 publication and 4,039 deprecated). This continuation adds 1,740 examples across batches 191–200, leaving 62,002 more reviewed publications to reach 100,000. All 35,785 English-only approved objects match runtime exactly and pass both adapters (71,570 checks). Rejected IDs remain absent. Shard 072 was completed with 500 records, new shards `examples/073.json`, `074.json` (500 records each), and shard `examples/075.json` (498 records) are registered in the manifest. There are 82,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,943 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `4587ff99cb844f3609e6384cfdcecd0f40b55cff` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 201 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 39,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.


## English editorial continuation: batches 201–210

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 201 | 200 | 173 | 27 | 3 |
| 202 | 200 | 172 | 28 | 12 |
| 203 | 200 | 176 | 24 | 8 |
| 204 | 200 | 170 | 30 | 7 |
| 205 | 200 | 163 | 37 | 9 |
| 206 | 200 | 143 | 57 | 5 |
| 207 | 200 | 159 | 41 | 6 |
| 208 | 200 | 177 | 23 | 7 |
| 209 | 200 | 174 | 26 | 3 |
| 210 | 200 | 182 | 18 | 4 |
| Total | 2,000 | 1,689 | 311 | 64 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Sixty-four accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 201: capitalized Business School, removed comma before because, hyphenated reddish-brown; Batch 202: people's, introductory commas, comma before and, serial Oxford commas, removed redundant a in after half an hour, semicolon for comma splice, comma before or, closed compound shoelaces; Batch 203: introductory commas, serial Oxford comma, capitalized Mommy, comma before and/but, added definite article before undergraduate level, removed extraneous comma; Batch 204: introductory comma, hyphenated well-liked and added Oxford comma, removed comma between coordinate adjectives, comma before and, lowercased teddy bear; Batch 205: hyphenated high-interest, comma before but, removed comma before because, comma before or, removed comma before too/without, removed comma between coordinate verbs, introductory comma; Batch 206: comma before and, serial Oxford comma, hyphenated well-informed; Batch 207: added comma after interjection Boy, comma before and, hyphenated well-mannered, serial Oxford comma; Batch 208: comma before nonrestrictive temporal clause, really hard for colloquial real hard, serial Oxford comma, comma before and, removed extraneous comma before prepositional phrase; Batch 209: terminal question mark for suggestion, closed compound overindulge, adverb strangely for strange; Batch 210: closed compound underway, supplied missing preposition for, adverb placement for I will just never understand, hyphenated compound verb sweet-talk). Near duplicates and intra-slice duplicate variations were removed during review. All 311 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 41,824 decisions, 37,474 published, 4,350 rejected and 721 disclosed edits. Runtime: 39,687 examples, 41,575 sentence records and 52,470 rich records; ledger: 56,820 applied decisions (52,470 publication and 4,350 deprecated). This continuation adds 1,689 examples across batches 201–210, leaving 60,313 more reviewed publications to reach 100,000. All 37,474 English-only approved objects match runtime exactly and pass both adapters (74,948 checks). Rejected IDs remain absent. Shard 075 was completed with 500 records, new shards `examples/076.json`, `077.json`, `078.json` (500 records each), and shard `examples/079.json` (187 records) are registered in the manifest. There are 80,357 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,631 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `dca819fa3ce58cbbdbf97bb3ec9fc01aa281084d` passed [Platform CI](https://github.com/sinhvienaiti/typing-game/actions/runs/42457074320), [Master Plan Acceptance](https://github.com/sinhvienaiti/typing-game/actions/runs/42457076759) and [Full Validation](https://github.com/sinhvienaiti/typing-game/actions/runs/42457070694). Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 211 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 41,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 211–220

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 211 | 200 | 182 | 18 | 6 |
| 212 | 200 | 175 | 25 | 6 |
| 213 | 200 | 189 | 11 | 3 |
| 214 | 200 | 179 | 21 | 4 |
| 215 | 200 | 191 | 9 | 1 |
| 216 | 200 | 182 | 18 | 2 |
| 217 | 200 | 178 | 22 | 3 |
| 218 | 200 | 184 | 16 | 3 |
| 219 | 200 | 186 | 14 | 2 |
| 220 | 200 | 180 | 20 | 2 |
| Total | 2,000 | 1,826 | 174 | 32 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 211: really for colloquial real, clause fix can't thank you enough for doing, coordinating comma before and, closed compound ballgame, hyphenated big-time; Batch 212: comma splice fix I'm sorry, but I know, hyphenated pick-up line, hyphenated plus-one, comma before and, comma before and then; Batch 213: semicolon for coordinate clauses, comma before and, adverb well for good; Batch 214: hyphenated make-believe, hyphenated tone-deaf, badly off for bad off, between your father and me for reflexive myself; Batch 215: coordinating comma before and; Batch 216: coordinating comma before and, hyphenated compound adjective laid-back; Batch 217: coordinating comma before and, supplied missing preposition of in a lot of work; Batch 218: semicolon for run-on clause, semicolon for comma splice, standard adverb loudly for flat loud; Batch 219: really bad news for colloquial real bad news, really anxious for colloquial real anxious; Batch 220: coordinating comma before or, hyphenated compound noun good-luck charm). Near duplicates and intra-slice duplicate variations were removed during review. All 174 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 43,824 decisions, 39,300 published, 4,524 rejected and 753 disclosed edits. Runtime: 41,513 examples, 43,401 sentence records and 54,296 rich records; ledger: 58,820 applied decisions (54,296 publication and 4,524 deprecated). This continuation adds 1,826 examples across batches 211–220, leaving 58,487 more reviewed publications to reach 100,000. All 39,300 English-only approved objects match runtime exactly and pass both adapters (78,600 checks). Rejected IDs remain absent. Shard 079 was completed with 500 records, new shards `examples/080.json`, `081.json`, `082.json` (500 records each), and shard `examples/083.json` (13 records) are registered in the manifest. There are 78,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,457 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `a90bdff0589d8736e05df82570077c4897f2aa25` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 221 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 43,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 221–230

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 221 | 200 | 178 | 22 | 4 |
| 222 | 200 | 177 | 23 | 1 |
| 223 | 200 | 174 | 26 | 1 |
| 224 | 200 | 157 | 43 | 2 |
| 225 | 200 | 164 | 36 | 2 |
| 226 | 200 | 166 | 34 | 1 |
| 227 | 200 | 174 | 26 | 1 |
| 228 | 200 | 178 | 22 | 2 |
| 229 | 200 | 170 | 30 | 2 |
| 230 | 200 | 176 | 24 | 2 |
| Total | 2,000 | 1,714 | 286 | 18 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Eighteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 221: coordinating comma before but, really small for colloquial real small, semicolon for run-on sentences, hyphenated long-term; Batch 222: closed compound speakerphone; Batch 223: really bad for colloquial real bad; Batch 224: hyphenated compound noun heads-up, really close for colloquial real close; Batch 225: closed compound speechwriter, closed compound sleepover; Batch 226: apostrophe in possessive dollars' worth; Batch 227: supplied missing preposition about; Batch 228: open compound reasonably priced, terminal question mark for suggestion; Batch 229: supplied missing preposition of in a couple of days, really hard for colloquial real hard; Batch 230: corrected typo to ask for at ask, really sorry for colloquial real sorry). Near duplicates and intra-slice duplicate variations were removed during review. All 286 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 45,824 decisions, 41,014 published, 4,810 rejected and 771 disclosed edits. Runtime: 43,227 examples, 45,115 sentence records and 56,010 rich records; ledger: 60,820 applied decisions (56,010 publication and 4,810 deprecated). This continuation adds 1,714 examples across batches 221–230, leaving 56,773 more reviewed publications to reach 100,000. All 41,014 English-only approved objects match runtime exactly and pass both adapters (82,028 checks). Rejected IDs remain absent. Shard 083 was completed with 500 records, new shards `examples/084.json`, `085.json` (500 records each), and shard `examples/086.json` (227 records) are registered in the manifest. There are 76,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 124,171 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `c96a5f42a9709d327459e9c83ce81bc56430775e` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 231 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 45,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 231–240

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 231 | 200 | 171 | 29 | 4 |
| 232 | 200 | 173 | 27 | 3 |
| 233 | 200 | 173 | 27 | 4 |
| 234 | 200 | 179 | 21 | 5 |
| 235 | 200 | 172 | 28 | 5 |
| 236 | 200 | 171 | 29 | 3 |
| 237 | 200 | 175 | 25 | 2 |
| 238 | 200 | 173 | 27 | 2 |
| 239 | 200 | 182 | 18 | 1 |
| 240 | 200 | 178 | 22 | 2 |
| Total | 2,000 | 1,747 | 253 | 31 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-one accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 231: coordinating commas before and/so; Batch 232: coordinating comma before and, really for colloquial real, hyphenated black-tie; Batch 233: hyphenated missing-persons, semicolon for comma splice, corrected homophone typo You're for Your, coordinating comma before and; Batch 234: interjection commas and exclamations, semicolon for comma splices; Batch 235: corrected typo point of view, hyphenated no-show, hyphenated dog-and-pony show, supplied infinitive marker to, coordinating comma before but; Batch 236: closed compound someday, really for colloquial real, semicolon for comma splice; Batch 237: semicolon for comma splice, capitalized General Assembly; Batch 238: hyphenated stand-up guy, really decent guy for colloquial real decent guy; Batch 239: capitalized Secret Service; Batch 240: hyphenated red-eye for overnight flight, closed compound voicemail). Near duplicates and intra-slice duplicate variations were removed during review. All 253 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 47,824 decisions, 42,761 published, 5,063 rejected and 802 disclosed edits. Runtime: 44,974 examples, 46,862 sentence records and 57,757 rich records; ledger: 62,820 applied decisions (57,757 publication and 5,063 deprecated). This continuation adds 1,747 examples across batches 231–240, leaving 55,026 more reviewed publications to reach 100,000. All 42,761 English-only approved objects match runtime exactly and pass both adapters (85,522 checks). Rejected IDs remain absent. Shard 086 was completed with 500 records, new shards `examples/087.json`, `088.json` (500 records each), and shard `examples/089.json` (474 records) are registered in the manifest. There are 74,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,918 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `7511014b2e88a38ec9ce09eb47c8702b70f03260` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 241 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 47,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 241–250

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 241 | 200 | 171 | 29 | 2 |
| 242 | 200 | 184 | 16 | 3 |
| 243 | 200 | 178 | 22 | 3 |
| 244 | 200 | 184 | 16 | 0 |
| 245 | 200 | 177 | 23 | 1 |
| 246 | 200 | 185 | 15 | 2 |
| 247 | 200 | 188 | 12 | 2 |
| 248 | 200 | 177 | 23 | 2 |
| 249 | 200 | 187 | 13 | 2 |
| 250 | 200 | 182 | 18 | 3 |
| Total | 2,000 | 1,813 | 187 | 20 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 241: comma after introductory connective So, supplied missing subject pronoun you; Batch 242: vocative commas before Tom, removed extraneous comma between subject clause and predicate; Batch 243: lowercased maneuver in Heimlich maneuver, terminal period on imperative, removed redundant article the in both of us; Batch 245: supplied comma after introductory connective So before vocative Tom; Batch 246: hyphenated compound adjective empty-handed, supplied missing definite article the before superlative most beautiful; Batch 247: hyphenated compound noun chain-smoker, hyphenated compound adjective piping-hot; Batch 248: closed compound noun racetrack, closed compound noun lumberyard; Batch 249: removed extraneous comma before adverb yet, normalized inner double quotes to single quotes; Batch 250: standardized American spelling favorite in favorite song, supplied coordinating comma between coordinate adjectives long and baggy, hyphenated compound adjective right-sized). Near duplicates, cross-corpus duplicates (such as sent.tatoeba.4025341 matching published 2569031) and intra-slice duplicate variations were removed during review. All 187 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 49,824 decisions, 44,574 published, 5,250 rejected and 822 disclosed edits. Runtime: 46,787 examples, 48,675 sentence records and 59,570 rich records; ledger: 64,820 applied decisions (59,570 publication and 5,250 deprecated). This continuation adds 1,813 examples across batches 241–250, leaving 53,213 more reviewed publications to reach 100,000. All 44,574 English-only approved objects match runtime exactly and pass both adapters (89,148 checks). Rejected IDs remain absent. Shard 089 was completed with 500 records, new shards `examples/090.json`, `091.json`, `092.json` (500 records each), and shard `examples/093.json` (287 records) are registered in the manifest. There are 72,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,731 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `68b35c1ce2a1b54eab8697ef1779d9108687cc53` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 251 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 49,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 251–260

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 251 | 200 | 181 | 19 | 4 |
| 252 | 200 | 174 | 26 | 6 |
| 253 | 200 | 159 | 41 | 7 |
| 254 | 200 | 164 | 36 | 5 |
| 255 | 200 | 173 | 27 | 6 |
| 256 | 200 | 177 | 23 | 7 |
| 257 | 200 | 172 | 28 | 5 |
| 258 | 200 | 180 | 20 | 3 |
| 259 | 200 | 183 | 17 | 3 |
| 260 | 200 | 174 | 26 | 3 |
| Total | 2,000 | 1,737 | 263 | 49 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Forty-nine accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 251: standardized agreement where water or moisture is present, normalized inner double quotes to single quotes, standardized American spelling counseling, standardized American spelling traveling; Batch 252: standardized American spelling tumor, hyphenated compound adjective long-distance, capitalized proper noun Father's Day, removed extraneous comma before but, standardized American spelling humor, removed extraneous comma before until; Batch 253: normalized inner double quotes, comma after introductory prep phrase, removed extraneous comma before on account of, comma between independent clauses, hyphenated two-week, removed comma before infinitive of purpose, hyphenated white-tie; Batch 254: capitalized Eiffel Tower, hyphenated first-class, standardized compound sentence punctuation or, standardized American spelling favor, standardized American spelling judgment; Batch 255: Oxford comma in series, coordinate comma between long, dark, coordinating comma before so, removed redundant colon after are, normalized inner quotes, standardized closed compound churchgoing; Batch 256: standardized American spelling canceled, standardized compound hardworking, standardized American spelling focused, standardized single word anymore, hyphenated suspended compound left- and right-handed, capitalized proper noun Socialist Party, standardized single word anymore; Batch 257: capitalized vocative Dad, standardized American spelling and hyphenation color-blind, standardized American spelling barbecue, comma after introductory prep phrase, supplied preposition by; Batch 258: standardized American spelling flavorless, Oxford comma in series, Oxford comma in series; Batch 259: standardized American spelling judgmental, closed compound skydiving, supplied possessive Alzheimer's; Batch 260: comma after introductory sentence adverb Usually, coordinating comma before and, comma between coordinate adjectives long, warm). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 263 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 51,824 decisions, 46,311 published, 5,513 rejected and 871 disclosed edits. Runtime: 48,524 examples, 50,412 sentence records and 61,307 rich records; ledger: 66,820 applied decisions (61,307 publication and 5,513 deprecated). This continuation adds 1,737 examples across batches 251–260, leaving 51,476 more reviewed publications to reach 100,000. All 46,311 English-only approved objects match runtime exactly and pass both adapters (92,622 checks). Rejected IDs remain absent. Shard 093 was completed with 500 records, new shards `examples/094.json`, `095.json`, `096.json` (500 records each), and shard `examples/097.json` (24 records) are registered in the manifest. There are 70,356 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,468 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `d51e50597c3b0226ef5886d6f7602761d58c89af` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 261 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 51,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 261–270

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 261 | 200 | 187 | 13 | 7 |
| 262 | 200 | 171 | 29 | 6 |
| 263 | 200 | 170 | 30 | 5 |
| 264 | 200 | 168 | 32 | 7 |
| 265 | 200 | 174 | 26 | 5 |
| 266 | 200 | 162 | 38 | 4 |
| 267 | 200 | 164 | 36 | 4 |
| 268 | 200 | 159 | 41 | 4 |
| 269 | 200 | 176 | 24 | 7 |
| 270 | 200 | 160 | 40 | 9 |
| Total | 2,000 | 1,691 | 309 | 58 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fifty-eight accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 261: standardized closed compound heatstroke, comma after introductory sentence adverb Usually, Oxford comma in series, removed superfluous indefinite article before surgery, corrected number agreement to plural worlds in proverb, standardized past subjunctive after It's time, normalized to natural verbal form exercise; Batch 262: coordinating comma between independent clauses, standardized directional preposition into her car, standardized American spelling favorite, Oxford comma in series, coordinating comma between independent clauses, coordinating comma before but; Batch 263: standardized American collective noun agreement eats, standardized closed compound seabed, coordinating comma between balanced independent clauses, coordinating comma between balanced clauses, standardized American spelling airplane; Batch 264: standardized American spelling protesters, standardized American spelling color, standardized American spelling color, standardized American spelling color, standardized singular count noun a sunburn, capitalized celestial body the Moon, hyphenated compound adjective most-read; Batch 265: supplied definite article the before musical instrument, standardized closed compound email, standardized conjunction as in comparative clause, coordinating comma between imperative clauses, standardized modal contraction You'd better; Batch 266: standardized American spelling industrialized, coordinating comma between compound predicates with temporal connective, coordinating comma between imperative clauses, coordinating comma between compound predicates; Batch 267: standardized natural nominal colocation the exact date, removed superfluous comma before prepositional phrase except for, standardized hyphenated compound adjective laid-back, standardized formal subjunctive were after wish; Batch 268: coordinating comma between independent clauses, standardized hyphenated compound noun number-crunching, standardized closed compound honeybees, standardized directional preposition to YouTube; Batch 269: comma after introductory subordinate clause, comma after introductory locative prepositional phrase, comma after introductory prepositional phrase, removed redundant adverb together after transitive align, standardized natural bare meal noun take my boyfriend lunch, standardized hyphenated compound noun pencil-pusher, comma after introductory subordinate clause; Batch 270: standardized hyphenated compound noun party-pooper, standardized natural prepositional phrase get off work, standardized plural count noun types of movies, standardized natural negative adverbial clause either, coordinating comma between independent clauses, standardized predicate negative is not good for reading, standardized two independent sentences to prevent comma splice, coordinating comma between independent clauses before so, removed superfluous parenthetical commas around adverbial phrase in private). Near duplicates, cross-corpus duplicates (such as sent.tatoeba.5308251 matching published 2268994) and intra-slice duplicate variations were removed during review. All 309 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 53,824 decisions, 48,002 published, 5,822 rejected and 929 disclosed edits. Runtime: 50,215 examples, 52,103 sentence records and 62,998 rich records; ledger: 68,820 applied decisions (62,998 publication and 5,822 deprecated). This continuation adds 1,691 examples across batches 261–270, leaving 49,785 more reviewed publications to reach 100,000. All 48,002 English-only approved objects match runtime exactly and pass both adapters (96,004 checks). Rejected IDs remain absent. Shard 097 was completed with 500 records, new shards `examples/098.json`, `099.json` (500 records each), and shard `examples/100.json` (215 records) are registered in the manifest. There are 68,355 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,158 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `931a64714d93342d93ae59cc3de55e5391c680f6` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 271 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 53,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 271–280

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 271 | 200 | 180 | 20 | 6 |
| 272 | 200 | 176 | 24 | 8 |
| 273 | 200 | 186 | 14 | 6 |
| 274 | 200 | 187 | 13 | 2 |
| 275 | 200 | 190 | 10 | 2 |
| 276 | 200 | 193 | 7 | 1 |
| 277 | 200 | 191 | 9 | 7 |
| 278 | 200 | 191 | 9 | 4 |
| 279 | 200 | 189 | 11 | 2 |
| 280 | 200 | 188 | 12 | 1 |
| Total | 2,000 | 1,871 | 129 | 39 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-nine accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 271: Oxford comma in series, standardized closed compound counterintuitive, standardized lowercase jack-o'-lantern, standardized natural liquid colocation glass of water, standardized American prepositional idiom on weekends, standardized closed compound sandcastle; Batch 272: coordinating comma between independent clauses before so, standardized formal subjunctive were after wish, standardized preposition from after different, standardized closed compound hotspots, coordinating comma between independent clauses before and, standardized open compound real estate developer, removed superfluous parenthetical comma before prepositional phrase in his or her own way, comma before concluding adverbial phrase no matter what; Batch 273: standardized closed compound snowbank, standardized adjective form from innovating to innovative, standardized American spelling from cauterised to cauterized, standardized plural possessive parents' house, standardized compound adjective low-income, coordinating comma between independent clauses before and; Batch 274: standardized compound noun cash-flow before problem, standardized second conditional verb form from you're to you were; Batch 275: standardized closed compound seasickness, standardized closed compound catchphrase; Batch 276: standardized closed compound shipshape; Batch 277: standardized compound adjective handicap-accessible, standardized open compound fairy tales, added comma after introductory adverb Obviously, standardized verb collocation from do to provide before medical aid, added comma after introductory adverb Essentially, standardized compound Whatever happened, expanded nonstandard contracted relative pronoun who're to who are; Batch 278: added coordinating comma before and, added missing indefinite article a before simple breach of contract, capitalized proper noun Navy, removed redundant pronoun it before gerund working here; Batch 279: removed redundant definite article before both of you, added coordinating comma before but; Batch 280: standardized compound adjective non-life-threatening). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 129 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 55,824 decisions, 49,873 published, 5,951 rejected and 968 disclosed edits. Runtime: 52,086 examples, 53,974 sentence records and 64,869 rich records; ledger: 70,820 applied decisions (64,869 publication and 5,951 deprecated). This continuation adds 1,871 examples across batches 271–280, leaving 47,914 more reviewed publications to reach 100,000. All 49,873 English-only approved objects match runtime exactly and pass both adapters (99,746 checks). Rejected IDs remain absent. Shard 100 was completed with 500 records, new shards `examples/101.json`, `102.json`, `103.json` (500 records each), and shard `examples/104.json` (86 records) are registered in the manifest. There are 66,353 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 123,027 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `73bb268c946261caeef234f26b527ca226d9c3ad` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 281 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 55,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

## English editorial continuation: batches 281–290

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 281 | 200 | 187 | 13 | 3 |
| 282 | 200 | 192 | 8 | 7 |
| 283 | 200 | 188 | 12 | 4 |
| 284 | 200 | 184 | 16 | 6 |
| 285 | 200 | 191 | 9 | 4 |
| 286 | 200 | 181 | 19 | 6 |
| 287 | 200 | 186 | 14 | 1 |
| 288 | 200 | 187 | 13 | 2 |
| 289 | 200 | 192 | 8 | 2 |
| 290 | 200 | 190 | 10 | 2 |
| Total | 2,000 | 1,878 | 122 | 37 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirty-seven accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 281: standardized verb form disperse, added comma after introductory sentence adverb Structurally,, standardized directional preposition into his car; Batch 282: standardized subordinate clause word order where we are, standardized closed compound healthcare, standardized colloquial have got to have to, added coordinating comma before and, added comma between coordinate predicates, capitalized proper noun Army, added comma after introductory adverb Hopefully,; Batch 283: standardized hyphenated compound noun clock-watching, corrected subject-verb agreement to plural What are, standardized prepositional phrase on Monday, standardized idiom lie low; Batch 284: added coordinating comma before and, standardized closed compound campsite, standardized prepositional phrase on Monday, standardized prepositional phrase on Monday, standardized prepositional phrase on Monday, removed superfluous indefinite article a before comparative easier; Batch 285: standardized formal subjunctive were after wish, standardized adverb really before adjective conscientious, capitalized proper playing card Queen of Spades, standardized prepositional phrase clear to you; Batch 286: added comma after introductory sentence adverb Hopefully,, standardized hyphenated compound bow-hunting, standardized closed compound adverb overnight, standardized singular noun phrase double standard, standardized temporal idiom from now on, standardized closed compound adjective hardworking; Batch 287: standardized modal auxiliary negative could never swim; Batch 288: capitalized proper noun American Dream, standardized formal subjunctive were after wish; Batch 289: replaced inappropriate question mark with a period on conditional imperative clause, supplied missing infinitive particle to before verb do; Batch 290: standardized colloquial adverb real to really before adjective proud, hyphenated compound adjective high-quality before noun tires). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 122 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 57,824 decisions, 51,751 published, 6,073 rejected and 1,005 disclosed edits. Runtime: 53,964 examples, 55,852 sentence records and 66,747 rich records; ledger: 72,820 applied decisions (66,747 publication and 6,073 deprecated). This continuation adds 1,878 examples across batches 281–290, leaving 46,036 more reviewed publications to reach 100,000. All 51,751 English-only approved objects match runtime exactly and pass both adapters (103,502 checks). Rejected IDs remain absent. Shard 104 was completed with 500 records, new shards `examples/105.json`, `106.json` (500 records each), and shard `examples/107.json` (464 records) are registered in the manifest. There are 64,353 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,905 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `3c29f73c8e04dfddae39280537ded42661cb10d0` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 291 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 57,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 291–300

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 291 | 200 | 183 | 17 | 2 |
| 292 | 200 | 192 | 8 | 3 |
| 293 | 200 | 185 | 15 | 2 |
| 294 | 200 | 187 | 13 | 1 |
| 295 | 200 | 191 | 9 | 0 |
| 296 | 200 | 186 | 14 | 3 |
| 297 | 200 | 193 | 7 | 0 |
| 298 | 200 | 185 | 15 | 2 |
| 299 | 200 | 183 | 17 | 5 |
| 300 | 200 | 188 | 12 | 4 |
| Total | 2,000 | 1,873 | 127 | 22 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 291: added comma before adverbial clause really, standardized open compound open mic; Batch 292: standardized hyphenated compound adjective down-to-earth, standardized closed compound snowdrift, supplied missing preposition to in square one; Batch 293: standardized closed compound painkillers, added comma after introductory sentence adverb Clearly,; Batch 294: standardized prepositional phrase on Monday; Batch 295: clean editorial candidates preserved without modifications; Batch 296: standardized colloquial adverb real to really, supplied missing gerund wishing in set phrase wishing you all the best, replaced inappropriate question mark with period on indirect question clause; Batch 297: clean editorial candidates preserved without modifications; Batch 298: added exclamation mark to interjection clause, supplied missing copula verb be; Batch 299: standardized informal adjective real to proper adverb really, added direct address comma after OK, restored natural standard auxiliary-adverb word order was always inspired, standardized compound adjective jam-packed, removed superfluous informal ending preposition with; Batch 300: inserted missing definite article the before crowd, standardized compound noun ghostwriter, supplied standard preposition of time on Monday, supplied standard preposition of time on Monday). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 127 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 59,824 decisions, 53,624 published, 6,200 rejected and 1,027 disclosed edits. Runtime: 55,837 examples, 57,725 sentence records and 68,620 rich records; ledger: 74,820 applied decisions (68,620 publication and 6,200 deprecated). This continuation adds 1,873 examples across batches 291–300, leaving 44,163 more reviewed publications to reach 100,000. All 53,624 English-only approved objects match runtime exactly and pass both adapters (107,248 checks). Rejected IDs remain absent. Shard 107 was completed with 500 records, new shards `examples/108.json`, `109.json`, `110.json` (500 records each), and shard `examples/111.json` (337 records) are registered in the manifest. There are 62,353 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,778 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `3c29f73c8e04dfddae39280537ded42661cb10d0` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Milestone achieved: Batch 300 complete. Continue English editorial batch 301 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 59,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 301–310

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 301 | 200 | 190 | 10 | 3 |
| 302 | 200 | 191 | 9 | 3 |
| 303 | 200 | 188 | 12 | 3 |
| 304 | 200 | 192 | 8 | 4 |
| 305 | 200 | 184 | 16 | 2 |
| 306 | 200 | 189 | 11 | 2 |
| 307 | 200 | 190 | 10 | 2 |
| 308 | 200 | 197 | 3 | 3 |
| 309 | 200 | 185 | 15 | 4 |
| 310 | 200 | 191 | 9 | 2 |
| Total | 2,000 | 1,897 | 103 | 28 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-eight accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 301: standardized preposition from after absent, standardized preposition in a soft voice, inserted missing subject pronoun you; Batch 302: standardized intransitive verb lay down on the bed, standardized adverb really good, capitalized proper military title Army Intelligence; Batch 303: standardized adverb going well now, supplied standard preposition of time on Monday, added comma after introductory coordinating connector So; Batch 304: supplied standard preposition of time on Monday, hyphenated compound adjective never-ending, hyphenated compound adverbial idiom scot-free, supplied standard preposition of time on Monday; Batch 305: standardized adverb really good, standardized modifier word order a very humble person; Batch 306: standardized adverb really well, inserted coordinating contrastive conjunction but; Batch 307: standardized adverb so easily, corrected noun form to contentment in sigh of contentment; Batch 308: replaced period with question mark on tag question, removed superfluous definite article the in both of you, supplied standard preposition of time on Monday; Batch 309: standardized adverb really glad, hyphenated compound adjective red-handed, standardized adverb really bad, supplied missing possessive marker in Mary's eyes; Batch 310: standardized closed compound spelling micromanage, supplied parallel noun in good days and bad days). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 103 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 61,824 decisions, 55,521 published, 6,303 rejected and 1,055 disclosed edits. Runtime: 57,734 examples, 59,622 sentence records and 70,517 rich records; ledger: 76,820 applied decisions (70,517 publication and 6,303 deprecated). This continuation adds 1,897 examples across batches 301–310, leaving 42,266 more reviewed publications to reach 100,000. All 55,521 English-only approved objects match runtime exactly and pass both adapters (111,042 checks). Rejected IDs remain absent. Shard 111 was completed with 500 records, new shards `examples/112.json`, `113.json`, `114.json` (500 records each), and shard `examples/115.json` (234 records) are registered in the manifest. There are 60,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,672 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `44953d210057199108ecae7de66293273d009239` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 311 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 61,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 311–320

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 311 | 200 | 185 | 15 | 3 |
| 312 | 200 | 190 | 10 | 3 |
| 313 | 200 | 190 | 10 | 3 |
| 314 | 200 | 184 | 16 | 1 |
| 315 | 200 | 189 | 11 | 3 |
| 316 | 200 | 187 | 13 | 2 |
| 317 | 200 | 179 | 21 | 1 |
| 318 | 200 | 186 | 14 | 2 |
| 319 | 200 | 180 | 20 | 1 |
| 320 | 200 | 183 | 17 | 3 |
| Total | 2,000 | 1,853 | 147 | 22 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-two accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 311: standardized colloquial adverb real to really, standardized comparative adjective riskier, supplied direct address comma in OK, Tom,; Batch 312: hyphenated compound modifier knee-deep, standardized colloquial adverb real to really, standardized adverb badly; Batch 313: supplied standard quotation marks and comma for direct speech, standardized closed compound adjective hardworking, standardized open spelling for predicate idiom off base; Batch 314: hyphenated compound noun game-changer; Batch 315: standardized colloquial adverb real to really, hyphenated compound noun crowd-pleaser, hyphenated compound noun joke-teller; Batch 316: standardized colloquial adverb real to really, standardized open spelling of predicate idiom off guard; Batch 317: hyphenated compound adverbial big-time; Batch 318: standardized closed compound noun holdup, supplied initial correlative adverb as in as good as usual; Batch 319: kept colloquial negative quantifier syntax as idiomatic; Batch 320: supplied standard preposition for in asked Tom for a favor, standardized closed compound noun curveball, standardized past participle beaten). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 147 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 63,824 decisions, 57,374 published, 6,450 rejected and 1,077 disclosed edits. Runtime: 59,587 examples, 61,475 sentence records and 72,370 rich records; ledger: 78,820 applied decisions (72,370 publication and 6,450 deprecated). This continuation adds 1,853 examples across batches 311–320, leaving 40,413 more reviewed publications to reach 100,000. All 57,374 English-only approved objects match runtime exactly and pass both adapters (114,748 checks). Rejected IDs remain absent. Shard 115 was completed with 500 records, new shards `examples/116.json`, `117.json`, `118.json` (500 records each), and shard `examples/119.json` (87 records) are registered in the manifest. There are 58,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,525 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `a14d96384a51eec7a11ebc868ebdbceef9798ef0` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 321 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 63,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 321–330

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 321 | 200 | 187 | 13 | 0 |
| 322 | 200 | 189 | 11 | 4 |
| 323 | 200 | 191 | 9 | 2 |
| 324 | 200 | 187 | 13 | 1 |
| 325 | 200 | 194 | 6 | 2 |
| 326 | 200 | 195 | 5 | 3 |
| 327 | 200 | 191 | 9 | 1 |
| 328 | 200 | 197 | 3 | 3 |
| 329 | 200 | 191 | 9 | 1 |
| 330 | 200 | 193 | 7 | 1 |
| Total | 2,000 | 1,915 | 85 | 18 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Eighteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 322: standardized closed compound noun busload, hyphenated compound modifier broken-down, standardized natural phrasing an usher at a movie theater, hyphenated compound adjective off-limits; Batch 323: standardized singular verb agreement batch of cookies is, hyphenated compound adjective full-time; Batch 324: standardized adverbial smoothness in going too smoothly; Batch 325: standardized US spelling realize, hyphenated compound adjective eye-catching; Batch 326: standardized singular venue arcade, standardized spaced compound video game, standardized hyphenation for Rolls-Royce; Batch 327: removed unnecessary hyphen after adverb in fully automated; Batch 328: standardized unhyphenated second thoughts, inserted missing infinitive marker to in wanted to hear, capitalized proper adjective French fries; Batch 329: standardized US spelling center; Batch 330: expanded contracted verb in Your T-shirt is inside out). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 85 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 65,824 decisions, 59,289 published, 6,535 rejected and 1,095 disclosed edits. Runtime: 61,502 examples, 63,390 sentence records and 74,285 rich records; ledger: 80,820 applied decisions (74,285 publication and 6,535 deprecated). This continuation adds 1,915 examples across batches 321–330, leaving 38,498 more reviewed publications to reach 100,000. All 59,289 English-only approved objects match runtime exactly and pass both adapters (118,578 checks). Rejected IDs remain absent. Shard 119 was completed with 500 records, new shards `examples/120.json`, `121.json`, `122.json` (500 records each), and shard `examples/123.json` (2 records) are registered in the manifest. There are 56,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,440 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `52c8023dc1fd4f1e434a83c5336c6668b3f388cc` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 331 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 65,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 331–340

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 331 | 200 | 193 | 7 | 1 |
| 332 | 200 | 192 | 8 | 1 |
| 333 | 200 | 189 | 11 | 3 |
| 334 | 200 | 190 | 10 | 2 |
| 335 | 200 | 196 | 4 | 1 |
| 336 | 200 | 189 | 11 | 1 |
| 337 | 200 | 191 | 9 | 1 |
| 338 | 200 | 195 | 5 | 1 |
| 339 | 200 | 194 | 6 | 2 |
| 340 | 200 | 197 | 3 | 1 |
| Total | 2,000 | 1,926 | 74 | 14 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fourteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 331: supplied definite article and expanded contraction in The kettle is on. What do you fancy?; Batch 332: expanded contracted verb in I think the pizza is here.; Batch 333: standardized unhyphenated compound noun toaster oven, inserted comma after introductory prepositional phrase in In spite of his considerable wealth,, corrected adverb involuntarily to adjective involuntary in Blushing is an involuntary reaction.; Batch 334: standardized closed compound noun potbelly, corrected plural noun adjunct midterms to singular midterm; Batch 335: inserted missing dummy pronoun it in coordinate clause; Batch 336: hyphenated compound modifier billion-dollar; Batch 337: standardized US spelling jewelry; Batch 338: standardized closed compound noun takeout; Batch 339: supplied missing initial correlative adverb as in as happy as a fish in water, standardized open compound noun dish towel; Batch 340: standardized lowercase spelling tai chi). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 74 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 67,824 decisions, 61,215 published, 6,609 rejected and 1,109 disclosed edits. Runtime: 63,428 examples, 65,316 sentence records and 76,211 rich records; ledger: 82,820 applied decisions (76,211 publication and 6,609 deprecated). This continuation adds 1,926 examples across batches 331–340, leaving 36,572 more reviewed publications to reach 100,000. All 61,215 English-only approved objects match runtime exactly and pass both adapters (122,430 checks). Rejected IDs remain absent. Shard 123 was completed with 500 records, new shards `examples/124.json`, `125.json` (500 records each), and shard `examples/126.json` (428 records) are registered in the manifest. There are 54,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,366 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `47e88b12` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 341 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 67,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 341–350

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 341 | 200 | 198 | 2 | 4 |
| 342 | 200 | 199 | 1 | 4 |
| 343 | 200 | 198 | 2 | 3 |
| 344 | 200 | 196 | 4 | 3 |
| 345 | 200 | 198 | 2 | 3 |
| 346 | 200 | 197 | 3 | 2 |
| 347 | 200 | 195 | 5 | 2 |
| 348 | 200 | 196 | 4 | 2 |
| 349 | 200 | 196 | 4 | 2 |
| 350 | 200 | 196 | 4 | 2 |
| Total | 2,000 | 1,969 | 31 | 27 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Twenty-seven accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 341: standardized compound windowsill, standardized quotation punctuation, supplied missing definite article the in benefit of the doubt, restored missing subject pronoun you; Batch 342: supplied missing indefinite article a in when I was a kid, supplied missing comma in conditional introductory clause, standardized preposition with in obsessed with; Batch 343: standardized compound noun toenails, supplied missing definite article the, corrected past tense sang and standardized spelling a cappella; Batch 344: standardized closed compound takeaway, corrected auxiliary verb word order in question, capitalized Midwest; Batch 345: supplied definite article the before piano, supplied missing preposition of in a lot of, hyphenated compound color adjective yellowish-gray; Batch 346: standardized ellipsis to three periods, hyphenated compound modifier two-drink; Batch 347: standardized spelling footsie, removed informal interrobang sequence; Batch 348: corrected word order of adverb just, standardized adverb form differently; Batch 349: capitalized genus name Cyclospora, standardized adverb form quickly; Batch 350: hyphenated compound numerical modifier one-hour, standardized informal contraction wanna to want to). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 31 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 69,824 decisions, 63,184 published, 6,640 rejected and 1,136 disclosed edits. Runtime: 65,397 examples, 67,285 sentence records and 78,180 rich records; ledger: 84,820 applied decisions (78,180 publication and 6,640 deprecated). This continuation adds 1,969 examples across batches 341–350, leaving 34,603 more reviewed publications to reach 100,000. All 63,184 English-only approved objects match runtime exactly and pass both adapters (126,368 checks). Rejected IDs remain absent. Shard 126 was completed with 500 records, new shards `examples/127.json`, `128.json`, `129.json` (500 records each), and shard `examples/130.json` (397 records) are registered in the manifest. There are 52,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,335 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `47e88b12f605cb450a86d528bdf64cf453cb11c1` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 351 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 69,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 351–360

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 351 | 200 | 185 | 15 | 0 |
| 352 | 200 | 188 | 12 | 0 |
| 353 | 200 | 190 | 10 | 4 |
| 354 | 200 | 187 | 13 | 0 |
| 355 | 200 | 184 | 16 | 2 |
| 356 | 200 | 195 | 5 | 1 |
| 357 | 200 | 189 | 11 | 2 |
| 358 | 200 | 187 | 13 | 0 |
| 359 | 200 | 190 | 10 | 1 |
| 360 | 200 | 187 | 13 | 0 |
| Total | 2,000 | 1,882 | 118 | 10 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Ten accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 353: supplied missing preposition to in to stay home across two candidate records, standardized preposition before in get home before dark across two candidate records; Batch 355: standardized compound subject pronoun order in Tom and I will across two candidate records; Batch 356: standardized third-person singular present verb agreement lives in if he lives; Batch 357: corrected tag question pronoun we to agree with subject in are we?, corrected typographical pronoun error you to possessive your in your typical weekday; Batch 359: inserted missing infinitive marker to in ready to do). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 118 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 71,824 decisions, 65,066 published, 6,758 rejected and 1,146 disclosed edits. Runtime: 67,279 examples, 69,167 sentence records and 80,062 rich records; ledger: 86,820 applied decisions (80,062 publication and 6,758 deprecated). This continuation adds 1,882 examples across batches 351–360, leaving 32,721 more reviewed publications to reach 100,000. All 65,066 English-only approved objects match runtime exactly and pass both adapters (130,132 checks). Rejected IDs remain absent. Shard 130 was completed with 500 records, new shards `examples/131.json`, `132.json`, `133.json` (500 records each), and shard `examples/134.json` (279 records) are registered in the manifest. There are 50,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,217 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `f336f43702161fa4e8dc833eeaa89cfcfa464453` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 361 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 71,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 361–370

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 361 | 200 | 188 | 12 | 1 |
| 362 | 200 | 189 | 11 | 1 |
| 363 | 200 | 190 | 10 | 1 |
| 364 | 200 | 185 | 15 | 1 |
| 365 | 200 | 188 | 12 | 2 |
| 366 | 200 | 190 | 10 | 1 |
| 367 | 200 | 182 | 18 | 1 |
| 368 | 200 | 181 | 19 | 2 |
| 369 | 200 | 185 | 15 | 2 |
| 370 | 200 | 188 | 12 | 3 |
| Total | 2,000 | 1,866 | 134 | 15 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Fifteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 361: standardized spelling nosy in nosy neighbors; Batch 362: added missing possessive suffix 's in Tom's judgment; Batch 363: supplied missing indefinite article a in a new book; Batch 364: hyphenated compound noun half-sister; Batch 365: hyphenated compound modifier multiple-choice in multiple-choice exams, corrected malapropism baited breath to bated breath; Batch 366: hyphenated compound predicate adjective inside-out; Batch 367: hyphenated compound adjective nerve-wracking; Batch 368: removed redundant definite article the before Saturday night, standardized closed compound noun willpower; Batch 369: standardized closed compound noun firefighter, hyphenated compound modifier long-distance in long-distance relationships; Batch 370: hyphenated compound modifier no-smoking in no-smoking areas, hyphenated compound modifier long-distance in long-distance relationships, supplied missing auxiliary participle been in I've always been afraid). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 134 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 73,824 decisions, 66,932 published, 6,892 rejected and 1,161 disclosed edits. Runtime: 69,145 examples, 71,033 sentence records and 81,928 rich records; ledger: 88,820 applied decisions (81,928 publication and 6,892 deprecated). This continuation adds 1,866 examples across batches 361–370, leaving 30,855 more reviewed publications to reach 100,000. All 66,932 English-only approved objects match runtime exactly and pass both adapters (133,864 checks). Rejected IDs remain absent. Shard 134 was completed with 500 records, new shards `examples/135.json`, `136.json`, `137.json` (500 records each), and shard `examples/138.json` (145 records) are registered in the manifest. There are 48,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 122,083 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `f6d99b82d7531c0bf2bb694e26b41f45168e4a82` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 371 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 73,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 371–380

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 371 | 200 | 185 | 15 | 2 |
| 372 | 200 | 185 | 15 | 3 |
| 373 | 200 | 187 | 13 | 1 |
| 374 | 200 | 184 | 16 | 1 |
| 375 | 200 | 191 | 9 | 2 |
| 376 | 200 | 187 | 13 | 0 |
| 377 | 200 | 184 | 16 | 2 |
| 378 | 200 | 187 | 13 | 1 |
| 379 | 200 | 186 | 14 | 0 |
| 380 | 200 | 188 | 12 | 1 |
| Total | 2,000 | 1,864 | 136 | 13 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Thirteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 371: inserted comma after introductory copular clause 'The question is' and corrected terminal question mark across two candidate records in The question is, do you want it? and The question is, how did Tom do that?; Batch 372: supplied missing indefinite article a in idiom a chip off the old block, inserted comma after introductory copular clause 'The main question is' and corrected terminal question mark in The main question is, will Tom do his work well?, inserted comma before coordinating conjunction and connecting independent clauses in The dining room is downstairs, and the library is on the third floor.; Batch 373: standardized open compound 'Some day' to adverb 'Someday' and inserted comma after introductory temporal adverb in Someday, when it's convenient for you, let's do that.; Batch 374: hyphenated compound modifier for-sale before noun sign in Is that a for-sale sign?; Batch 375: inserted comma after interjection 'No' before vocative direct address Tom in No, Tom, actually you're wrong., hyphenated compound noun thumbs-up in Tom responded with a thumbs-up.; Batch 377: hyphenated compound modifier common-sense before noun approach in It's a common-sense approach., hyphenated compound adjective tax-friendly in How tax-friendly is your state?; Batch 378: inserted comma before coordinating conjunction and connecting independent clauses in It was warm, and the weather was good.; Batch 380: inserted comma before coordinating conjunction and connecting independent clauses in My patients are waiting for me, and I'm stuck in a traffic jam.). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 136 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 75,824 decisions, 68,796 published, 7,028 rejected and 1,174 disclosed edits. Runtime: 71,009 examples, 72,897 sentence records and 83,792 rich records; ledger: 90,820 applied decisions (83,792 publication and 7,028 deprecated). This continuation adds 1,864 examples across batches 371–380, leaving 28,991 more reviewed publications to reach 100,000. All 68,796 English-only approved objects match runtime exactly and pass both adapters (137,592 checks). Rejected IDs remain absent. Shard 138 was completed with 500 records, new shards `examples/139.json`, `140.json`, `141.json` (500 records each), and shard `examples/142.json` (9 records) are registered in the manifest. There are 46,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 121,947 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `27d8ed6bfc2c656c1c37c82eec4f4034b45069bb` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 381 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 75,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 381–390

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 381 | 200 | 185 | 15 | 1 |
| 382 | 200 | 186 | 14 | 1 |
| 383 | 200 | 185 | 15 | 1 |
| 384 | 200 | 187 | 13 | 2 |
| 385 | 200 | 185 | 15 | 1 |
| 386 | 200 | 180 | 20 | 1 |
| 387 | 200 | 173 | 27 | 0 |
| 388 | 200 | 173 | 27 | 1 |
| 389 | 200 | 171 | 29 | 1 |
| 390 | 200 | 184 | 16 | 2 |
| Total | 2,000 | 1,809 | 191 | 11 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Eleven accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 381: capitalized proper holiday noun Valentine's Day in How can I dump my girlfriend on Valentine's Day?; Batch 382: corrected third-person singular present verb consume to consumes in How much sugar do you think the average person consumes every day?; Batch 383: hyphenated compound adjective last-ditch preceding noun in Tom and Mary are making a last-ditch effort to avoid a divorce.; Batch 384: inserted missing infinitive marker to before catch up in Tom wasn't walking too fast for Mary to catch up with him., corrected singular noun week to plural weeks following quantifier three in Tom went to Boston, where he stayed for three weeks.; Batch 385: inserted missing indefinite article a in quantifier phrase quite a lot in Tom seemed to know quite a lot about baseball.; Batch 386: corrected hyphenated straight-forward to standard closed compound straightforward in Tom is an honest, straightforward guy.; Batch 388: hyphenated compound age adjective three-year-old before noun in Tom is a three-year-old Canadian boy.; Batch 389: corrected plural possessive arms' to singular arm's in idiom at arm's length in Tom kept most of us at arm's length.; Batch 390: hyphenated compound idiom scot-free in Tom is likely to get off scot-free., inserted comma after introductory adverbial clause in Every time I think about it, I get choked up.). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 191 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 77,824 decisions, 70,605 published, 7,219 rejected and 1,185 disclosed edits. Runtime: 72,818 examples, 74,706 sentence records and 85,601 rich records; ledger: 92,820 applied decisions (85,601 publication and 7,219 deprecated). This continuation adds 1,809 examples across batches 381–390, leaving 27,182 more reviewed publications to reach 100,000. All 70,605 English-only approved objects match runtime exactly and pass both adapters (141,210 checks). Rejected IDs remain absent. Shard 142 was completed with 500 records, new shards `examples/143.json`, `144.json` (500 records each), and shard `examples/145.json` (318 records) are registered in the manifest. There are 44,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 121,756 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `9b744f2e54c0f9201636a087b35c6c27ac7901c4` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 391 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 77,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.

### Editorial continuation within Step 2: English batches 391–400

| English editorial batch | Reviewed | Published | Rejected | Disclosed edits |
| --- | ---: | ---: | ---: | ---: |
| 391 | 200 | 186 | 14 | 2 |
| 392 | 200 | 190 | 10 | 0 |
| 393 | 200 | 190 | 10 | 3 |
| 394 | 200 | 192 | 8 | 3 |
| 395 | 200 | 195 | 5 | 1 |
| 396 | 200 | 197 | 3 | 2 |
| 397 | 200 | 197 | 3 | 1 |
| 398 | 200 | 196 | 4 | 2 |
| 399 | 200 | 191 | 9 | 1 |
| 400 | 200 | 196 | 4 | 1 |
| Total | 2,000 | 1,930 | 70 | 16 |

All 2,000 candidates received individual readings and explicit decisions for grammar, naturalness, standalone use, CEFR, source suitability and semantic repetition. Pinned canonical evidence, attribution, license and digest identity were verified separately from upstream ratings. Sixteen accepted edits preserve source meaning and disclose original/final text, modified provenance, the change description and a recomputed digest (Batch 391: standardized open compound best seller to standard closed compound bestseller in Have you ever written a bestseller?, standardized open compound meat packing to standard closed compound meatpacking in Tom works at a meatpacking plant.; Batch 393: inserted comma after introductory sentence adverb Basically in Basically, Tom is reaching out for help., standardized open compound stock broker to standard closed compound stockbroker in Tom became a stockbroker., inserted comma after introductory adverbial idiom Deep down in Deep down, Tom is a good guy.; Batch 394: hyphenated compound verb test-drive in Can I test-drive the car?, inserted comma before coordinating conjunction so between independent clauses in It's too dark, so I can't see very well., inserted comma after introductory prepositional phrase in At the moment, you're in no condition to drive.; Batch 395: replaced comma with semicolon between independent clauses to fix comma splice in motivational quote in Work hard in silence; let your success be your noise.; Batch 396: inserted auxiliary do to correct question grammar in What kind of activities do you enjoy the most?, inserted comma after introductory adverbial clause in Mary closed her eyes and waited for Tom's kiss. When she opened her eyes, Tom was gone.; Batch 397: removed extraneous comma before comparative clause in It's better to try and fail than never try at all.; Batch 398: corrected spelling of schucking to shucking in Should I buy an oyster shucking knife?, hyphenated compound predicate adjective off-limits in This area is off-limits.; Batch 399: hyphenated compound adjective ice-cold in This water is ice-cold.; Batch 400: inserted comma before coordinating conjunction joining independent clauses in Tom smiled at Mary, and then she smiled at him.). Near duplicates, cross-corpus duplicates and intra-slice duplicate variations were removed during review. All 70 rejections remain in source authoring, ledger and per-record reports without a CEFR or runtime object. Authoring stays draft; only the matching digest-bound publication overlay allows runtime publication.

Current English-only totals: 79,824 decisions, 72,535 published, 7,289 rejected and 1,201 disclosed edits. Runtime: 74,748 examples, 76,636 sentence records and 87,531 rich records; ledger: 94,820 applied decisions (87,531 publication and 7,289 deprecated). This continuation adds 1,930 examples across batches 391–400, leaving 25,252 more reviewed publications to reach 100,000. All 72,535 English-only approved objects match runtime exactly and pass both adapters (145,070 checks). Rejected IDs remain absent. Shard 145 was completed with 500 records, new shards `examples/146.json`, `147.json`, `148.json` (500 records each), and shard `examples/149.json` (248 records) are registered in the manifest. There are 42,350 unreviewed English-only candidates and 4,588 unreviewed project-original raw sentences. The optimistic combined bound is 121,686 before rejection/dedup, not publication approval.

Local validation covers schema/source/review/license gates, E10 contracts and smoke, 112 configured content/tooling tests, 10 handoff/decision tests, three runtime-count tests, generation/publication, dedup, published-runtime smoke, E11 freshness/exact coverage, capacity and master-plan checks. E12 release/maintenance precedes final E11 reconciliation. Verify byte-identical regeneration for every changed/new artifact and include every manifest shard in Git before push; then verify the three workflows on the final HEAD. Adapter checks do not replace the queued Step 11 integrated UI review.

The preceding verified checkpoint `5867ab9a96e4672fba6d589e6e334ff20f407c68` passed local validation and full audit suite. Current continuation-HEAD evidence belongs in PR #48; retain this preceding SHA here to avoid a self-referential SHA-only commit.

Continue English editorial batch 401 at candidate in `content/english/review-queues/tatoeba-english-next-review.json` with `node scripts/prepare-tatoeba-english-review.mjs --limit 200`. All 79,824 reviewed IDs stay excluded and pending candidates have no CEFR. This remains Group 1 Step 2; Steps 3–12 stay queued and PR #48 stays Draft. Historical EN/VI/link pins, source checksums, legacy vocabulary ABI, E04 scale-224 and all completed batches are unchanged.









