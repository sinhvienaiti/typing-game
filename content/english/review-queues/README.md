# English content review queues

Files here are **candidate/review inputs**, not runtime content.

Rules:

- importers may write normalized source candidates here;
- imported records must retain source IDs, source URL/snapshot and license;
- no file in this directory is published merely because import succeeded;
- candidates must pass schema, semantic, translation, naturalness, CEFR and license gates before conversion into canonical `shared/*` records;
- large raw downloads and transient API responses belong in `.cache/english-content/` (already ignored by Git), not in the repository.

## OEWN pilot

Run:

```bash
pnpm english-content:import:oewn:live -- --limit=300
```

The importer reads `content/english/dictionary/lexeme-seed-pilot.json`, calls the official OEWN **live** lemma API, and writes:

`content/english/review-queues/oewn-pilot.json`

Because the lemma API is live rather than release-versioned, the queue is explicitly stamped `live-api-unpinned` and can never be treated as the pinned 2025 release. For release-grade publishing, use the pinned OEWN 2025 JSON release and verify its checksum first.

The result contains source synset/sense IDs, POS, English definitions, source examples and pronunciations. It does **not** invent Vietnamese translations and does not mark anything as published.


## Pinned OEWN 2025 E03 pilot

Publication-grade source extraction uses the immutable OEWN source commit:

`dc343f2683279ecbb13fab4e2fd778d7b162d287`

With that checkout available locally:

```bash
pnpm english-content:import:oewn:pinned -- --source-dir=.cache/english-content/oewn
pnpm english-content:e03 -- --require-mapped=0.98
```

The generated `oewn-2025-pilot.json` contains source POS, morphology, pronunciations, sense IDs, synset definitions and source examples. It deliberately leaves `explanationVi` null and remains `candidate`; Vietnamese sense explanations require a separate bilingual authoring/review stage.

## E11 transient review packets

E11 review helpers generate bounded, deterministic local packets that are intentionally ignored by Git:

```bash
pnpm english-content:derive:typing-texts
node scripts/prepare-typing-text-e11-review-slice.mjs --limit 24
node scripts/prepare-english-content-e11-review-queue.mjs --per-target-limit 12
```

`typing-text-e11-next-review.json` advances through typing-text candidates after excluding controlled records and existing review decisions. Controlled record IDs must never be reintroduced into an E11 editorial slice to fill a packet; always regenerate the packet from the current controlled source and review ledger after a repair or concurrent branch advance.

`e11-sentence-gap-next-review.json` reads the current E11 readiness report, follows its exact sentence-source paths, overlays the review ledger, and selects unreviewed records only for sentence targets that are still below their locked minimum. Each selected record includes `batchId`, `recordSetId` and `sourceDigest` so a later review decision can be tied to the exact source revision.

Generating either packet does **not** mutate review decisions, source quality states, or published runtime content. A filename under `review-queues/` is never publication evidence; normal review, quality, license, dedupe, and publish gates still apply.
