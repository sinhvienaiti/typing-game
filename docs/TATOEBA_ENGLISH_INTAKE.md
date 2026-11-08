# Tatoeba English-only intake

This lane resumes Group 1 Step 2. It is separate from the historical English–Vietnamese translation pilot. It does not recover or replace the old EN/VI/link pin, unlock Step 3, or claim that the 100,000 published-example target has passed.

## Approved source observation

The four official weekly exports were downloaded on 2026-11-07; their Last-Modified headers identify 2026-10-31 exports. `content/english/sources/tatoeba-english-2026-10-31.json` records their URLs, byte lengths and SHA-256 hashes. Weekly URLs are mutable: later bytes must not be substituted for these approved inputs.

The extraction contains 122,212 source-evidence candidates from 2,040,024 English rows. Owners and independent positive reviewers self-report English level 5 in the same observed language export. Positive ratings must be at least as recent as the sentence modification. Any fresh negative rating or configured action/problem tag excludes a record. The typing subset uses 5–30 words, at most 300 ASCII characters, initial capitals and final sentence punctuation; it excludes digits, URLs and markup delimiters. These structural filters are not an exhaustive assessment of grammar, bias, factual accuracy or suitability. Some historical creation timestamps are unknown (`\N`); modification timestamps must be known to check rating freshness.

Tatoeba documents sentence reviews as experimental. The 623 records with at least two independent positive ratings receive queue priority; even these records require local editorial decisions. Self-reported language levels do not establish professional/native-speaker certification. A rating is not a CEFR assessment.

## Offline pin and reproduction

The five committed `.jsonl.gz.b64` shards contain the canonical extraction, including sentence IDs/texts, current owners, modification times, self-reported language levels and qualifying ratings. They retain no user profile descriptions. Base64 keeps the compressed snapshot transportable through the GitHub text-file API. Decode base64 before comparing the compressed hash; decompressed JSONL has its own byte length and hash. Files and rows are ordered deterministically. This extraction, rather than a promise that a mutable upstream URL will remain available, is the offline pin.

To verify and reconstruct the extraction from the **exact four original files** in `.cache/english-content/tatoeba-english-intake`:

```sh
python scripts/build-tatoeba-english-snapshot.py
```

The builder refuses mismatched upstream hashes or changed canonical descriptors. `--write` only restores bytes that already match the approved pin; it cannot approve a new source version. Bzip2/tar parsing uses Python's standard library and reads named members without extracting archive paths. CI does not fetch the mutable weekly URLs.

To validate the pinned archive and prepare the next editorial packet:

```sh
node scripts/prepare-tatoeba-english-review.mjs --limit 24
```

This works offline from the committed snapshot. It reserves every controlled sentence ID/text, skips previous positive and negative local decisions, deduplicates source text, returns a partial/exhausted packet truthfully, and never reuses an older Tatoeba ID for changed content. Source records remain `candidate`; grammar, naturalness, standalone suitability, CEFR, exact/near dedup and license review remain pending. Every packet includes original evidence and a source digest. Editing text, assigning CEFR or changing provenance requires a new controlled-source digest before a decision can apply.

## Editorial pilot and publication

Pilot 01 reviewed all 24 selected records: 20 accepted, four rejected, two accepted with disclosed edits. The rejected records include a generalized regulatory claim, a violent threat and two context-dependent discourse prompts. Positive upstream ratings were insufficient for those cases. `content/english/reports/tatoeba-english-editorial-pilot-01.json` records each original/final text, rationale, source digests and cross-runtime token-overlap score. Two edits simplify an unnatural phrase and expand “contact” to “contact lens.” All accepted records have explicit A2/B1/B2 editorial levels; no unreviewed records receive a default CEFR label.

Authoring records remain draft. The E10 manifest and digest-bound ledger decide which records may enter runtime. Rejected records are retained with deprecated decisions so they cannot return as new work. The publisher, schema/source validator, E11 counts/coverage and runtime smoke include this lane. Runtime verification compares approved objects exactly and asserts rejected objects are absent. The historical 300 Tatoeba sentences and 300 translation exercises retain their original source snapshots and counts.

Near-duplicate checks retain the existing exact token-Jaccard definition and threshold. A global token-order prefix index replaces repeated all-pairs tokenization. Every candidate match still receives a full set-intersection calculation, and regression tests compare the complete ordered results against brute force across random corpora, boundary thresholds, punctuation, empty sets and Unicode. It is not an approximate dedup filter.

## License and attribution

The official text export is distributed under CC BY 2.0 France. Each record retains the Tatoeba Project name, sentence URL, current owner, snapshot and license; the URL provides contributor history. Current owner is not represented as the original or sole author. Local edits set `modified: true` and explain the change. Audio is not imported. No source pin, community rating or successful technical test constitutes approval of the remaining editorial backlog.

Primary references: [Downloads](https://tatoeba.org/en/downloads), [Terms of use](https://tatoeba.org/en/terms_of_use), [Attribution FAQ](https://en.wiki.tatoeba.org/articles/show/faq).

## Reviewed continuation batches

Batches 02 and 03 each inspected 200 candidates. Batch 02 published 181, rejected 19 and disclosed four edits. Batch 03 published 176, rejected 24 and disclosed four edits. At that checkpoint, the three batches contained 424 decisions publishing 377 English-only examples and retaining 47 rejections. The full corpus then had 2,590 published examples; 121,764 source candidates remained unreviewed.

The per-record reports `tatoeba-english-editorial-pilot-02.json` and `tatoeba-english-editorial-pilot-03.json` contain individual rationales, original/final wording, explicit CEFR for accepted records, intake/controlled source digests and nearest token-overlap evidence. Rejections include unframed factual claims, outdated present-tense office-holder assertions, universal stereotypes, unsafe unqualified medical/food-storage advice and pragmatic repeats. Rejected candidates retain their original evidence and cannot re-enter the review queue.

E11 readiness and exact runtime record coverage discover registered English-only batches directly from the E10 manifest. Source authoring remains draft; only digest-bound publication decisions count. After release/maintenance refresh, regenerate E11 readiness and runtime reports again so embedded release snapshots are current. The existing runtime smoke checks every accepted object exactly and every rejected object's absence; all accepted continuation records are also exercised through Monkeytype and Karaoke adapters.

## Batches 04–06 and current continuation

Three further 200-record batches reviewed 600 candidates: 531 accepted, 69 rejected and 18 disclosed edits. Batch 04 accepted 179; batch 05 accepted 172; batch 06 accepted 180. Their individual reports use the same original/final wording, rationale, explicit CEFR, source-digest and nearest-overlap evidence as earlier batches. One inverted raincoat conditional was rejected at 0.9333 token overlap; pragmatic repeats were also removed below that threshold.

At the end of batches 04–06, all six batches contained 1,024 explicit decisions: 908 published English-only records and 116 rejected records, with 28 documented edits. The full corpus then contained 3,121 examples, with a target deficit of 96,879 and 121,162 unreviewed English-only candidates. These counts do not approve Step 2 or unlock translations.

Local checks exercise all 908 approved English-only records through both game adapters (1,816 checks), verify exact approved runtime objects and rejected-object absence, and reconcile E10/E11/E12 plus the capacity report. Regenerate the release snapshot before final E11 freshness checks. Verify the resulting remote HEAD's three workflows in PR #48.

## Batches 07–09

Three further 200-record batches explicitly reviewed 600 candidates: 500 published, 100 rejected and 12 edited. Batch 07 published 160; batch 08 published 171; batch 09 published 169. Rejection rationales cover unsupported universals, insufficiently scoped medical/economic/historical assertions, unclear standalone wording and pragmatic repeats. The per-record reports preserve every original/final text, rationale, CEFR assignment and source digest.

At the end of batches 07–09, 1,624 decisions published 1,408 English-only examples and retained 216 rejections. Forty accepted records had disclosed edits. Runtime then contained 3,621 examples, with a target deficit of 96,379 and 120,562 unreviewed candidates. All 1,408 approved English-only records pass both game adapters (2,816 checks). Rejected IDs stay out of both runtime and future review packets. Candidate inventory and successful engineering checks do not approve Step 2 or unlock later steps.

## English batches 10–12: still execution Step 2

A further 600 records received explicit review: batch 10 published 165, batch 11 published 167 and batch 12 published 168. Total: 500 published, 100 rejected and nine disclosed edits. Individual reports retain source/final wording, rationale, CEFR for accepted records, digest evidence and nearest-overlap results. Edited final texts were also checked against active canonical sentence sources for exact collisions.

At the end of batches 10–12, English-only totals were: 2,224 decisions, 1,908 published, 316 rejected and 49 disclosed edits. Full runtime contains 4,121 examples, 6,009 sentence records and 16,904 rich records; the ledger has 17,220 decisions. All 1,908 approved English-only records pass both adapters (3,816 checks). The queue has 119,962 unreviewed candidates; 95,879 more approved publications are needed. These engineering checks and packet labels do not open execution Steps 3–12. Source/license pins and the historical translation lane are unchanged.

## English batches 13–15: preceding Step 2 checkpoint

All 600 new candidates received explicit individual decisions: batch 13 published 143/rejected 57/edited six; batch 14 published 143/rejected 57/edited two; batch 15 published 141/rejected 59/edited six. Total: 427 published, 173 rejected and 14 disclosed edits. Reports retain every original/final text, editorial rationale, explicit accepted-record CEFR, source digests and nearest-overlap evidence. Self-review removed additional semantic repeats below the token threshold; edited final texts were also checked against active canonical sentence sources. Source authoring remains draft and publication requires the exact digest-bound ledger overlay.

At the end of batches 13–15, English-only totals were: 2,824 decisions, 2,335 published, 489 rejected and 63 disclosed edits. Runtime: 4,548 examples, 6,436 sentence records and 17,331 rich records; ledger: 17,820 decisions. All 2,335 published English-only records match runtime exactly and pass both Monkeytype and Karaoke adapters (4,670 checks); rejected objects remain absent. There are 119,362 unreviewed English-only candidates and 95,452 more reviewed publications are needed. English editorial batch 16 followed at `sent.tatoeba.41120`. This is still execution Step 2; Steps 3–12 remain unopened. The historical EN/VI/link pin, all source checksums and the legacy vocabulary ABI are unchanged.

## English batches 16–18: preceding Step 2 checkpoint

A further 600 candidates received individual decisions: batch 16 published 103/rejected 97/edited two; batch 17 published 151/rejected 49/edited three; batch 18 published 164/rejected 36/edited four. Total: 418 published, 182 rejected and nine disclosed edits. Reports preserve source/final wording, explicit accepted-record CEFR, rationale, attribution, intake/controlled digests and nearest-overlap evidence. Unspecified context was not invented. Semantic repeats were rejected even below the token threshold, including additional hearing-news/turning-pale variants. Edited final text was compared against all active canonical sources.

At the end of batches 16–18, English-only totals were: 3,424 decisions, 2,753 published, 671 rejected and 72 disclosed edits. Runtime: 4,966 examples, 6,854 sentence records and 17,749 rich records; ledger: 18,420 decisions. All 2,753 approved English-only records match runtime exactly and pass both Monkeytype and Karaoke adapters (5,506 checks). All rejected records remain absent. There are 118,762 unreviewed English-only candidates and 95,034 more reviewed publications are needed. English editorial batch 19 followed at `sent.tatoeba.45621`. This is still execution Step 2, with Steps 3–12 queued. The historical EN/VI/link pin, all source checksums and the legacy vocabulary ABI are unchanged.

## English batches 19–21: preceding Step 2 checkpoint

All 600 candidates received individual decisions: batch 19 published 159/rejected 41/edited six; batch 20 published 156/rejected 44/edited one; batch 21 published 142/rejected 58/edited two. Total: 457 published, 143 rejected and nine disclosed edits. Original/final wording, editorial rationale, explicit accepted-record CEFR, attribution, source evidence and digests remain in the three reports. Cross-corpus review rejected additional semantic repeats, including accident-cause paraphrases and a fifteen-member committee sentence whose wording differed from the existing record. Edited final text was also checked against all active canonical sources.

At the end of batches 19–21, English-only totals were: 4,024 decisions, 3,210 published, 814 rejected and 81 disclosed edits. Runtime: 5,423 examples, 7,311 sentence records and 18,206 rich records; ledger: 19,020 decisions. All 3,210 approved English-only records match runtime exactly and pass both adapters (6,420 checks); rejected objects remain absent. The example manifest includes `examples/010.json`. There were 118,162 unreviewed English-only candidates and 94,577 more reviewed publications were needed. English editorial batch 22 followed at `sent.tatoeba.49931` using `--limit 200`. This remains execution Step 2; Steps 3–12 stay queued. The historical EN/VI/link pin, source checksums and legacy vocabulary ABI are unchanged.

## English batches 22–30: preceding Step 2 checkpoint

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

At the end of batches 22–30, English editorial batch 31 was next at `sent.tatoeba.67208`; that checkpoint has now been continued below. This remains execution Group 1 Step 2. Steps 3–12 remain queued; PR #48 stays Draft. Source/license pins, the historical EN/VI/link lane and legacy vocabulary ABI remain unchanged.

## English batches 31–33: preceding Step 2 checkpoint

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

## English batches 34–40: current Step 2 checkpoint

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
