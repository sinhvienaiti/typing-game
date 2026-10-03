# Controlled English-content batches

`content/english/batches/manifest.json` is the machine-readable E10 release train.

Each record set declares:

- exact expected record count;
- whether it is generated during CI;
- allowed quality states;
- quality checks that must exist;
- game smoke tests that must consume the same parent-produced records.

A batch in `published` state is stricter than a record merely carrying
`quality.state = published`: every declared required check and every present
quality check must be `pass` or `not-applicable`.

Run after the external-source/import steps have produced review queues:

```bash
pnpm english-content:e10
```

The command writes `content/english/reports/e10-batch-report.json` for CI
coverage inspection. Review queues remain non-runtime data until the normal
publication gate promotes reviewed records.
