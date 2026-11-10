# English content source update policy

External content is never refreshed silently.

1. **Pinned imports remain reproducible.** OEWN and MultiWOZ use immutable Git commits; Vietnamese Wiktionary and Tatoeba pilots use pinned content hashes/snapshots.
2. **A source refresh creates a new review batch.** Updating a commit, dump, checksum or weekly export never mutates already-published records in place.
3. **License is re-audited before every source bump.** A source whose redistribution terms are unresolved remains `publishAllowed: false`.
4. **Attribution travels with publication.** If a published record depends on an attribution-required source, the runtime attribution dataset must be non-empty and use the same `contentVersion`.
5. **Stale does not mean auto-upgrade.** Older pinned sources may continue to build reproducibly. A maintainer reviews freshness at release planning time and explicitly chooses whether to create a replacement batch.
6. **Deprecation is explicit.** Stable IDs are not silently reused. Replacements go through `content/english/migrations/deprecations.json`, which is cycle-checked by E12 audit.
7. **Quality samples are deterministic.** `pnpm english-content:e12:sample` chooses records by stable hash so reviewers cannot unconsciously cherry-pick easy examples.

## Source-intake probes versus published-content CI

Published-content CI validates committed source manifests, licenses, immutable authoring inputs, editorial decisions, source digests, runtime publication, deduplication and reproducibility. It must not depend on fetching the **current** bytes from mutable Tatoeba weekly-export or Kaikki dump URLs: these URLs can serve a different release while the existing published records remain unchanged.

Use `.github/workflows/english-content-source-probes.yml` (manual `workflow_dispatch`) when evaluating an upstream refresh or attempting to reproduce an approved source cache. The workflow retains the original Tatoeba EN-VI and Simple/Vietnamese Wiktionary import commands, checksum validation, candidate-generation steps and review-only artifacts. A mismatch or unavailable approved snapshot **must fail that source probe**; do not weaken an importer or rewrite a pin to make the probe pass.

To promote new externally derived records, provide the exact approved source bytes or a reviewed source upgrade, verify content hashes and licensing, inspect candidate diffs, then apply digest-bound editorial decisions. This separation does not mean that the current pinned Tatoeba raw data can be reconstructed from GitHub: if those bytes are unavailable, new Tatoeba imports remain source-blocked. The unchanged reviewed runtime is validated independently.
