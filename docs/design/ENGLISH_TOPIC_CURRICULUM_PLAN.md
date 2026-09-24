# English Topic Curriculum Plan

Status: **ACTIVE IMPLEMENTATION — EXPLICIT USER OVERRIDE 2026-09-24**

## 1. Goal

Build one reusable English-learning curriculum layer on top of the existing validated 18,000-entry shared vocabulary library.

Do not fork or duplicate the 18,000 EN/VI/IPA records. Topic, grammar and part-of-speech data reference the existing vocabulary entries so Monkeytype, Vocabulary Shooter, Recall Typing, Karaoke Typing and Space Typing can consume the same learning metadata.

## 2. Existing source of truth

Keep:

`shared/vocabulary/levels/001.json ... 100.json`

as the authoritative lexical data.

Each official entry keeps the current shape:

- id
- en
- vi
- ipa

The existing pipeline remains authoritative for lexical quality:
- thichhoc-dict enrichment
- CMUdict pronunciation chain
- WordNet / Wiktionary lexical provenance
- wordfreq ranking
- ESDB/SCOWL whitelist
- CEFR-J difficulty reference

## 3. Curriculum-source references

Use public/reliable educational references to design coverage and progression rather than blindly copying proprietary word lists.

### British Council LearnEnglish

Reference topics and learner progression such as:
- daily routine
- clothes
- body
- food
- holidays
- hotels
- jobs
- money
- nature
- town
- restaurants
- shopping
- transport
- weather

Source:
https://learnenglish.britishcouncil.org/free-resources/vocabulary

### Cambridge English / English Profile

Use for:
- CEFR-oriented topic progression
- meaning-level vocabulary analysis
- part-of-speech and grammar framing
- communicative learner context

Sources:
https://www.cambridgeenglish.org/learning-english/
https://englishprofile.org/

### Oxford learner-word-list methodology

Use as a benchmark for frequency/usefulness/core-word coverage, not as a data dump.

Source:
https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000

### New General Service List

Use as a public high-frequency coverage reference, plus relevant specialized lists for business/academic coverage.

Source:
https://www.newgeneralservicelist.com/

## 4. Data architecture

New metadata lives beside, not inside, the 18k level records:

`shared/vocabulary/topics/`
`shared/vocabulary/parts-of-speech/`
`shared/vocabulary/grammar/`
`shared/vocabulary/curriculum/`

Generated curriculum references use the existing normalized English lookup key plus its level hint, for example `{ "key": "airport", "level": 12 }`.

This is intentionally more stable than persisting positional `Lxxx-xxx` IDs in curriculum metadata: a trusted full-library rebuild may rebalance entries across levels and therefore change positional IDs, while the normalized English key is already the canonical key used by `lookup.json`.

The referenced level file remains authoritative for the actual `id/en/vi/ipa` record. Curriculum files never duplicate Vietnamese meanings or IPA.

A single word may belong to multiple topics and may have different sense/POS uses.

Do not assume one English spelling means one learning category.

## 5. Topic taxonomy

Initial top-level curriculum groups:

1. Everyday Life
   - greetings
   - daily routine
   - time and dates
   - household tasks
   - personal belongings

2. People & Relationships
   - family
   - friends
   - appearance
   - personality
   - emotions
   - relationships

3. Home & Living
   - rooms
   - furniture
   - appliances
   - renting
   - repairs
   - neighborhood

4. Food & Drink
   - ingredients
   - meals
   - cooking
   - restaurants
   - ordering
   - taste and texture
   - nutrition

5. Health & Body
   - body
   - symptoms
   - healthcare
   - exercise
   - sleep
   - wellbeing

6. Education
   - school
   - classroom
   - university
   - study skills
   - exams
   - research

7. Work & Business
   - jobs
   - workplace
   - meetings
   - email
   - projects
   - management
   - sales
   - finance
   - customer service
   - interviews

8. Travel & Tourism
   - planning
   - airport
   - flights
   - immigration
   - hotels
   - sightseeing
   - emergencies
   - directions

9. Transport
   - road
   - public transport
   - driving
   - rail
   - air
   - sea

10. Shopping & Money
    - stores
    - products
    - prices
    - payments
    - banking
    - budgeting
    - online shopping

11. Technology
    - computers
    - internet
    - software
    - phones
    - cybersecurity
    - AI
    - programming
    - devices

12. Communication & Media
    - conversation
    - phone
    - messaging
    - email
    - news
    - social media
    - presentations

13. Nature & Environment
    - weather
    - animals
    - plants
    - geography
    - climate
    - environment

14. Society & Culture
    - community
    - customs
    - entertainment
    - arts
    - sports
    - public services

15. Academic & Abstract English
    - argument
    - cause/effect
    - comparison
    - data
    - evidence
    - trends
    - analysis

The detailed catalog should target roughly 100-150 reusable subtopics.

## 6. Part-of-speech learning views

POS is a cross-cutting classification, not a topic.

Provide reusable views for:
- noun
- verb
- adjective
- adverb
- pronoun
- preposition
- conjunction
- determiner
- modal/auxiliary
- phrasal verb
- collocation
- fixed phrase

A vocabulary item can appear in several views when its intended learner senses support them.

## 7. Simplified time/tense curriculum

Learner-facing grammar uses exactly three primary time groups:

### Present
Focus:
- current state
- habits/routines
- facts
- actions happening now

### Past
Focus:
- completed events
- previous states
- stories/background
- past experience

### Future
Focus:
- plans
- intentions
- predictions
- schedules

Do not expose a giant 12/16-tense selector as the primary curriculum UI.

Internally, grammar examples may still use accurate constructions such as simple, continuous, perfect, modals or future forms. They are grouped under the three learner-facing time concepts.

## 8. Additional grammar-learning themes

After the three time groups:
- questions
- negatives
- articles
- countable/uncountable nouns
- comparatives/superlatives
- quantity
- modal meaning
- condition/basic if
- passive recognition
- relative clauses
- linking words
- word order
- common preposition patterns

Keep grammar tied to practical topic examples where possible.

## 9. Topic record contract

Proposed topic document:

```json
{
  "version": 1,
  "id": "travel.airport",
  "label": "Airport",
  "group": "travel",
  "levels": ["A1", "A2", "B1"],
  "entries": [
    {
      "key": "airport",
      "level": 12,
      "roles": ["noun"],
      "priority": "core"
    }
  ]
}
```

Do not copy EN/VI/IPA into topic files.

Generated indexes provide reverse lookup:

- normalized vocabulary key -> topics
- topic -> normalized vocabulary references + level hints
- POS -> normalized vocabulary references + level hints
- grammar module -> vocabulary/topic references

## 10. Coverage workflow

1. Load all 18,000 current entries.
2. Build normalized word/ID indexes.
3. Seed topic concepts from the educational references.
4. Match existing vocabulary first.
5. Measure topic coverage.
6. Identify useful missing headwords/phrases in a deterministic coverage-gap report.
7. Only then run missing candidates through the existing trusted EN/VI/IPA/provenance pipeline.
8. Never invent filler merely to make topic counts equal.
9. Run validation and statistical spot checks.

## 11. Quality rules

- avoid duplicate normalized English;
- do not invent Vietnamese meanings or IPA;
- preserve General American IPA policy;
- ambiguous heteronyms require sense/POS handling;
- topic assignment must be semantically plausible;
- do not classify a word only from spelling;
- core beginner topics prioritize common/useful vocabulary;
- specialized vocabulary is additive, not filler;
- generated metadata must be deterministic.

## 12. Game integration

The learning selectors must expose all three curriculum dimensions, not only Topic:

- Topic — practical life/work/travel/technology/etc. groups;
- Word type — noun, verb, adjective, adverb and the additional POS/phrase views;
- Grammar — Present / Past / Future first, then the supporting practical grammar modules.

All modes resolve back to the same authoritative 18k EN/VI/IPA records and lazy-load only referenced level files.

### Monkeytype
Allow:
- Library
- Topic
- Word type
- Grammar
- Custom

Each curriculum mode builds the existing EN-VN dictionary for the selected practice set without replacing Custom data.

### Vocabulary Shooter
Allow:
- Class/Level
- Topic
- Word type
- Grammar
- Custom

### Recall Typing
Allow:
- Class/Level
- Topic
- Word type
- Grammar
- Custom

### Space Typing
Allow:
- Class/Level
- Topic
- Word type
- Grammar
- Custom

Curriculum selection changes the vocabulary pool only; Campaign progression, enemy budgets, rewards and stage semantics remain unchanged.

### Karaoke Typing
Keep curriculum optional. Lyrics/audio remain authoritative; curriculum metadata may be used later for tagging or optional practice extraction, but must not force songs into an artificial vocabulary mode.

## 13. Performance

Do not load all topic files at startup.

Use:
- compact topic index
- lazy selected-topic fetch
- generated reverse lookup only where needed
- browser caching
- no duplication of 18k lexical payload

## 14. Validation

Add:
- JSON schemas
- duplicate topic ID checks
- referenced vocabulary ID existence checks
- POS enum checks
- grammar module checks
- deterministic generated-index checks
- coverage reports
- orphan/empty topic checks
- minimum core-topic sanity checks without enforcing equal counts

## 15. Delivery phases

T00 — schemas + folder contracts
T01 — taxonomy/index
T02 — POS metadata
T03 — Everyday Life / People / Home
T04 — Food / Health / Education
T05 — Work / Business
T06 — Travel / Transport
T07 — Shopping / Money
T08 — Technology / Communication
T09 — Nature / Society / Culture
T10 — Academic/Abstract
T11 — Present/Past/Future grammar groups
T12 — remaining practical grammar modules
T13 — 18k coverage-gap report
T14 — trusted missing-word enrichment only where justified
T15 — game integrations
T16 — cross-game QA + docs

## 16. Sequencing rule

The earlier defer-until-M22-M24 rule was explicitly overridden on 2026-09-24.

Implementation may now proceed in parallel with the remaining real-browser/audio Space Typing acceptance work, with these safeguards:

- Space Typing M22-M24 status must not be falsely marked complete because curriculum work progressed;
- the 18,000-entry EN/VI/IPA library remains unchanged unless a later coverage-gap review justifies trusted additions;
- topic/POS/grammar metadata must be additive and reusable across games;
- every generated curriculum artifact must be reproducible and validated in parent CI;
- game integrations must lazy-load selected curriculum data rather than loading the entire curriculum at startup.

## 17. Active implementation contract

The implementation target for this pass is:

1. T00 schemas/folder contracts;
2. T01 complete top-level taxonomy with roughly 100 practical subtopics;
3. T02 curated cross-cutting POS views;
4. T03-T10 broad practical topic coverage from the existing 18k library;
5. T11 Present/Past/Future learner-facing grammar groups;
6. T12 practical supporting grammar modules;
7. T13 deterministic coverage-gap reporting;
8. parent CI generation/validation guards;
9. T15 game integrations after the shared contract is stable;
10. post-implementation review for UI/UX, logic and performance.

The first pass must prefer exact normalized headword/phrase references already present in the 18k library. Missing terms are reported, not invented.

## 18. Implementation checkpoint — shared curriculum foundation

Implemented in the first active pass:

- 15 practical top-level groups;
- 101 learner-facing subtopics;
- deterministic exact-key mapping against the existing 18k `lookup.json`;
- 835 unique existing vocabulary keys referenced by topic metadata;
- 98.7% exact match across requested topic references;
- core noun / verb / adjective / adverb learning views;
- additional function-word / phrase POS views with explicit gap reporting;
- Present / Past / Future primary learner-facing grammar modules;
- 13 supporting practical grammar modules;
- generated reverse topic lookup for cross-game reuse;
- deterministic coverage-gap report instead of fabricated lexical entries;
- JSON schemas, generator, validator and parent CI drift guard.

Known lexical gaps intentionally remain visible for later trusted enrichment, especially:

- articles/pronouns/function words excluded from the current 18k production selection;
- common phrasal verbs;
- common collocations;
- fixed phrases.

These gaps do not block topic browsing. Grammar modules retain the real grammar tokens even
when those tokens are not yet standalone EN/VI/IPA vocabulary records.

T15 status after the first integration slice:

- Topic selection is implemented in Monkeytype, Vocabulary Shooter, Recall Typing and Space Typing;
- topic loading is lookup-free through embedded key/level hints;
- Topic selectors are grouped by curriculum area;
- parent Platform CI #228 is green on the reviewed Topic integration.

Remaining T15 work in the active pass:

- expose Word type selection from `parts-of-speech/index.json`;
- expose Grammar selection from `grammar/index.json`, with Present / Past / Future visually first;
- reuse one generic lazy key+level resolver per game instead of duplicating loaders;
- preserve each game's existing Custom/Class/Library behavior and persisted selection;
- keep Topic/POS/Grammar data lazy and do not preload all 18k entries;
- complete cross-game QA, then run the requested second UI/UX + logic + performance review and fix confirmed findings.
