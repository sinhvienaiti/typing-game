# English content authoring workspace

Canonical authoring/source-control inputs for the rich English learning system.

- Keep `shared/vocabulary/levels/*.json` v1 unchanged.
- Raw third-party bulk downloads are not committed by default.
- Pin upstream snapshot/checksum before enabling an importer.
- Generated candidates never become published runtime content automatically.
- Source/license/provenance gates must pass before publication.
- `grammar/topic-catalog.json` is the source for the machine-readable 300-topic framework.
- Run `pnpm english-content:generate` after curriculum-source changes.
- Run `pnpm english-content:check` before committing rich-content changes.
