# Shared English Content Runtime

This module is the parent-side read/query contract for the rich English-content runtime.

Current foundation support:

- load the 300-topic catalog lazily;
- load one CEFR curriculum file at a time;
- resolve one grammar topic by stable `gr.*` ID;
- list/search grammar topics without loading the future sentence corpus.

Future dictionary/sentence/phrase shard adapters should extend this module rather than making each child game scan large datasets independently.
