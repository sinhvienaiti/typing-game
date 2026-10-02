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
