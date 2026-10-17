# Rich English content publication

`content/english/**` is authoring/review space. `shared/**` is runtime publication.

Run:

```bash
pnpm english-content:check
```

The publisher copies **only records whose `quality.state` is exactly `published`** into runtime shards.

Candidate, draft, validated and reviewed records remain authoring-only. This prevents imports or generated exercises from shipping merely because their JSON is structurally valid.

Current pilot data is intentionally candidate/draft, so the expected rich runtime counts remain zero until independent quality review is completed.
