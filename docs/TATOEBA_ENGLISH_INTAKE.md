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

At the end of batches 13–15, English-only totals were: 2,824 decisions, 2,335 published, 489 rejected and 63 disclosed edits. Runtime: 4,548 examples, 6,436 sentence records and 17,331 rich records; ledger: 17,820 decisions. All 2,335 published English-only records match runtime exactly and pass both Monkeytype and Karaoke adapters (4,670 checks); rejected objects remain absent. There are 119,362 unreviewed English-only candidates and 95,452 more reviewed publications are needed. Continue English editorial batch 16 at `sent.tatoeba.41120` using `--limit 200`. This is still execution Step 2; Steps 3–12 remain unopened. The historical EN/VI/link pin, all source checksums and the legacy vocabulary ABI are unchanged.

## English batches 16–18: current Step 2 checkpoint

A further 600 candidates received individual decisions: batch 16 published 103/rejected 97/edited two; batch 17 published 151/rejected 49/edited three; batch 18 published 164/rejected 36/edited four. Total: 418 published, 182 rejected and nine disclosed edits. Reports preserve source/final wording, explicit accepted-record CEFR, rationale, attribution, intake/controlled digests and nearest-overlap evidence. Unspecified context was not invented. Semantic repeats were rejected even below the token threshold, including additional hearing-news/turning-pale variants. Edited final text was compared against all active canonical sources.

Current English-only totals: 3,424 decisions, 2,753 published, 671 rejected and 72 disclosed edits. Runtime: 4,966 examples, 6,854 sentence records and 17,749 rich records; ledger: 18,420 decisions. All 2,753 approved English-only records match runtime exactly and pass both Monkeytype and Karaoke adapters (5,506 checks). All rejected records remain absent. There are 118,762 unreviewed English-only candidates and 95,034 more reviewed publications are needed. Continue English editorial batch 19 at `sent.tatoeba.45621` using `--limit 200`. This is still execution Step 2, with Steps 3–12 queued. The historical EN/VI/link pin, all source checksums and the legacy vocabulary ABI are unchanged.
