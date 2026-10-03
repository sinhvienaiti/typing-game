# English content source update policy

External content is never refreshed silently.

1. **Pinned imports remain reproducible.** OEWN and MultiWOZ use immutable Git commits; Vietnamese Wiktionary and Tatoeba pilots use pinned content hashes/snapshots.
2. **A source refresh creates a new review batch.** Updating a commit, dump, checksum or weekly export never mutates already-published records in place.
3. **License is re-audited before every source bump.** A source whose redistribution terms are unresolved remains `publishAllowed: false`.
4. **Attribution travels with publication.** If a published record depends on an attribution-required source, the runtime attribution dataset must be non-empty and use the same `contentVersion`.
5. **Stale does not mean auto-upgrade.** Older pinned sources may continue to build reproducibly. A maintainer reviews freshness at release planning time and explicitly chooses whether to create a replacement batch.
6. **Deprecation is explicit.** Stable IDs are not silently reused. Replacements go through `content/english/migrations/deprecations.json`, which is cycle-checked by E12 audit.
7. **Quality samples are deterministic.** `pnpm english-content:e12:sample` chooses records by stable hash so reviewers cannot unconsciously cherry-pick easy examples.
