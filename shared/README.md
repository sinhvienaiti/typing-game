# Shared

Only genuinely shared platform assets or contracts belong here.
Game-specific logic stays in each game repository.

## Vocabulary library

`shared/vocabulary/levels/*.json` is the single source of truth for the built-in learning library.

Every official entry must contain:

- `id`
- `en`
- `vi`
- `ipa`

Do not maintain a second giant vocabulary copy for Monkeytype.

Generated files:

- `shared/vocabulary/index.json` - available levels and counts
- `shared/vocabulary/lookup.json` - normalized English/phrase -> level lookup used by Monkeytype

Commands:

```bash
pnpm vocab:generate
pnpm vocab:validate
```

Shooter and Recall load one selected level. Monkeytype uses `lookup.json` to discover and cache only the level files needed by the current Custom Text.

## Shared Learning

`shared/learning/` owns the parent canonical Learning Event/Profile contracts, deterministic mastery/review-priority logic and parent IndexedDB persistence.

Commands:

```bash
pnpm learning:check
pnpm learning:test
```

Child games emit attempts; they do not own competing canonical mastery calculations.
