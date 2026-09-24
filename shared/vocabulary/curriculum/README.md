# Shared English Curriculum

This layer adds reusable learning metadata on top of the existing 18,000-entry
EN/VI/IPA vocabulary library.

## Source of truth

Lexical data remains:

`shared/vocabulary/levels/001.json ... 100.json`

Curriculum source data is:

`shared/vocabulary/curriculum/source.json`

Generated artifacts are:

- `shared/vocabulary/topics/catalog.json`
- `shared/vocabulary/topics/index.json`
- `shared/vocabulary/parts-of-speech/index.json`
- `shared/vocabulary/grammar/index.json`
- `shared/vocabulary/curriculum/coverage.json`

Run:

`pnpm curriculum:generate`
`pnpm curriculum:validate`

## Reference contract

Curriculum metadata references vocabulary by normalized English key plus level hint.
The level JSON remains authoritative for `id/en/vi/ipa`.

This avoids coupling curriculum metadata to positional `Lxxx-xxx` IDs that may change
when the trusted 18k library is rebuilt.

## Coverage gaps

A source token that is not present in the 18k lookup is retained in the coverage report.
It is never silently invented or promoted into the lexical library.

This is especially important for function words, phrasal verbs, collocations and fixed
phrases. Those gaps can later be enriched through the existing trusted vocabulary
pipeline when provenance and EN/VI/IPA quality are available.

## Loading rule

Games should fetch the compact topic/POS/grammar index first and only load the vocabulary
level files referenced by the selected curriculum item. Do not preload all 18k entries.
