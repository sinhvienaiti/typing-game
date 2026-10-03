# Shared English Content Runtime

This module is the parent-side read/query contract for the rich English-content runtime.

Current foundation support:

- load the 300-topic catalog lazily;
- load one CEFR curriculum file at a time;
- resolve one grammar topic by stable `gr.*` ID;
- list/search grammar topics without loading the future sentence corpus.

Future dictionary/sentence/phrase shard adapters should extend this module rather than making each child game scan large datasets independently.

## Cross-game rich activities

`activity-dataset.mjs` defines the bounded parent-to-child E09 contract.
`game-adapters.mjs` converts published rich-content records into that contract.

Runtime adapters reject draft/candidate records by default. Review/CI tools may opt in
with `allowUnpublished: true`, but child games must not treat those records as shipped
learning content.

Activity results still use the existing Shared Learning entity types
(`vocabulary`, `grammar`, `sentence`) so no child game owns a second mastery engine.
