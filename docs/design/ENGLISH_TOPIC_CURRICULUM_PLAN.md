# English Topic Curriculum Plan

Status: **PLAN COMPLETE / CONTENT IMPLEMENTATION DEFERRED UNTIL SPACE TYPING M22-M24 IS COMPLETE**

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

Topic documents reference vocabulary IDs.

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
      "vocabularyId": "Lxxx-xxx",
      "roles": ["noun"],
      "priority": "core"
    }
  ]
}
```

Do not copy EN/VI/IPA into topic files.

Generated indexes provide reverse lookup:

- vocabulary ID -> topics
- topic -> vocabulary IDs
- POS -> vocabulary IDs
- grammar module -> vocabulary/topic references

## 10. Coverage workflow

1. Load all 18,000 current entries.
2. Build normalized word/ID indexes.
3. Seed topic concepts from the educational references.
4. Match existing vocabulary first.
5. Measure topic coverage.
6. Identify useful missing headwords/phrases.
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

### Monkeytype
Allow:
- Library
- Topic
- Custom

Topic mode selects one or more topic lists and builds the existing EN-VN dictionary/typing input from referenced shared entries.

### Vocabulary Shooter
Allow:
- Class/Level
- Topic
- Custom

### Recall Typing
Allow:
- Class/Level
- Topic
- Custom

### Space Typing
Later allow topic-aware campaign/practice presets without changing Campaign progression semantics.

### Karaoke Typing
Use topics primarily for learning metadata / optional practice content rather than forcing lyrics to a topic.

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

The curriculum plan is approved now, but bulk topic-content implementation starts only after the current Space Typing acceptance roadmap reaches its existing M22-M24 completion condition, unless explicitly overridden later.

This prevents the shared corpus project from hiding unresolved Space Typing audio/browser acceptance work.
