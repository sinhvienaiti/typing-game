# English Topic Curriculum Plan

Status: **T16 CROSS-GAME REVIEW COMPLETE / POST-T16 SPACE TYPING HUD + ACTION-RACE REVIEWS COMPLETE / AUTOMATED CI GREEN**

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

T15 curriculum integration is now feature-complete for the active games:

- Monkeytype: Library / Topic / Word type / Grammar / Custom;
- Vocabulary Shooter: Class / Topic / Word type / Grammar / Custom;
- Recall Typing: Class / Topic / Word type / Grammar / Custom;
- Space Typing: Class / Topic / Word type / Grammar / Custom;
- Present / Past / Future are the primary Grammar choices, followed by practical modules;
- Grammar practice combines its real signal vocabulary with linked practical-topic context;
- known zero-coverage POS/phrase views remain visible as gaps and are disabled rather than filled with invented data;
- existing Custom data and persisted source choices remain intact;
- all curriculum modes resolve back to the same 18k EN/VI/IPA source records.

Reviewed child checkpoints for this integration:

- Monkeytype: `30fca754d43ff23a03a920a2f6e20cde0440950b`;
- Vocabulary Shooter: `bf813d0abe9ceb1d83156e0f71764a915d037809`;
- Recall Typing: `9eed1f4a40bd1f4edf3162de4f939b05985d3504`;
- Space Typing: `b633276f58587040153951ed26b63ad528cb3b50`.

Next active work is T16 plus the explicitly requested second review pass:

- run full parent cross-game Platform CI on the four reviewed gitlinks;
- review UI/UX clarity and responsive behavior;
- review source-mode persistence and failure recovery;
- review lazy request behavior and remove redundant curriculum-index requests;
- review Space Typing gameplay/retry/route state transitions;
- review render/update hot paths for avoidable work without deleting visuals or mechanics;
- fix every confirmed issue and repeat child + parent CI.


## 19. T16 second review checkpoint — 2026-09-24

The explicitly requested second review pass was run after Topic / Word type / Grammar integration.

### Confirmed cross-game findings and fixes

#### Space Typing

- fixed eager loading of all four shared curriculum indexes when opening the Vocabulary dialog;
- isolated source-load failures to the selected source instead of writing one failure across all panels;
- added session caching for referenced vocabulary level JSON documents with failed-promise eviction for retry;
- deduplicated Grammar + linked-topic references before deriving the representative difficulty level;
- balanced the five source tabs responsively and exposed `aria-pressed`;
- moved repeated particle exponential damping calculation out of the per-particle loop without reducing particle count;
- prewarmed the complete bounded sampled-SFX pools before combat so first use no longer allocates new `Audio` elements during combat.

Reviewed child: `7e7a81769675911d2418682cc5c52e60ae505ea2`.
Child CI #638: PASS.

#### Vocabulary Shooter

- Vocabulary dialog now loads only the active curriculum source instead of all indexes together;
- shared level documents are session-cached and failed loads remain retryable;
- source tabs expose `aria-pressed`.

Reviewed child: `71c77330a3d54ac0a09bb7de9d88923850387ff0`.
Child CI #57: PASS.

#### Recall Typing

- Vocabulary dialog now loads only the active curriculum source instead of all indexes together;
- shared level documents are session-cached and failed loads remain retryable;
- source tabs expose `aria-pressed`.

Reviewed child: `7f4b1b2b676a0eb302e512393b8092847a275a93`.
Child CI #40: PASS.

#### Monkeytype

- existing active-source index loading was already lazy and was retained;
- shared level documents are now session-cached across Library / Topic / Word type / Grammar preparation;
- failed level promises are evicted so retry remains possible;
- Custom dictionary persistence remains unchanged.

Reviewed child: `610fbb8c03697b3c86ca61470f11d2b56484d715`.
Custom EN-VN CI #74: PASS (lint, local static build and frontend tests).

### Review conclusions

Confirmed inefficiencies were fixed by removing redundant work, not by removing learning/gameplay features.

The review did **not** reduce:

- the 18,000-word lexical library;
- Topic / Word type / Grammar choices;
- particles, enemies, projectiles or visual quality modes;
- Space Typing sampled/synthesized SFX;
- Campaign logic, rewards or difficulty.

Space Typing retry/checkpoint/route source flow was re-read during this pass. The current rollback path restores the committed frontier, exits Game's stale game-over phase before navigation, and intentionally opens Sector Briefing when a frontier route choice is required. No additional source-level retry defect was confirmed in this pass; real-browser interaction remains part of M22.

Parent Platform CI is the final automated integration gate for this T16 checkpoint. Real-device Space Typing M22 audio/visual/performance acceptance remains separate and pending.


## 20. Post-T16 Space Typing HUD follow-up — 2026-09-24

After the T16 cross-game review was merged and Parent Platform CI #231 passed, a further Space Typing source review found additional avoidable HUD/main-thread work and one Route Map clarity issue.

Reviewed child: `073bc02cb964876b3cfb451ff804017bfae7fec6`.

Child CI #643: PASS.

Confirmed fixes:

- Combat Hotbar DOM nodes are cached instead of re-querying all slots and descendants on the 150 ms skill/status cadence.
- Unchanged Hotbar slot states skip text/class/title/disabled DOM writes.
- Boss stagger no longer emits boss-HUD callbacks every simulation frame; Canvas stagger presentation remains live and the DOM HUD updates on state transitions.
- Boss HUD uses guarded text/width/class writes.
- Route Map separates optional Shop/Station services from primary encounter navigation and names the target Stage directly.

No gameplay, visual, enemy, projectile, particle, audio or curriculum feature was removed or reduced.

The parent gitlink is updated to this reviewed child. Parent Platform CI #233 passed the complete integration pipeline. Space Typing M22 real-browser/audio/performance acceptance remains separate and pending.


## 21. Post-T16 async-action race follow-up — 2026-09-24

A further interaction lifecycle review after the HUD hot-path pass found two confirmed race conditions in Space Typing.

Reviewed child: `d28ccd927166dfa2fb98fb3f67e7916a6b89dad4`.

Child CI #646: PASS.

Confirmed fixes:

- Campaign Map Start/Replay now owns an async action gate while the Stage selection autosave is in flight, preventing double-click save/navigation overlap.
- Campaign Map selection controls are frozen for the duration of that transaction so the saved Stage cannot change underneath the pending action.
- Checkpoint navigation and all game-over recovery-item actions share one mutually exclusive gate.
- Salvage Anchor and Stage Revival Core can no longer consume multiple copies from rapid repeated clicks while persistence is pending.
- failed or incomplete game-over transactions re-render the current valid recovery choices instead of leaving stale disabled/enabled controls.
- Phoenix Core uses the same action gate so all death-resolution paths have one consistent lifecycle.

The implementation changes transaction control only. Recovery effects, item costs, Campaign progression, checkpoint semantics, audio, visuals and difficulty are unchanged.

The parent gitlink is updated to this child. Parent Platform CI #236 passed the complete integration pipeline.


## 22. Space Typing M25 parent integration — 2026-09-24

Space Typing expansion Reviews #1/#2 and Recall follow-ups have been integrated back into the parent platform.

Pinned child:
- Space Typing: `7030ed539aeb3972ce5e6c3b5e8a46cc9c09ad21`;
- child M24 final CI #680: PASS;
- 149 test files / 752 tests;
- JS/CSS, audio asset and Ship V3 guards remain within unchanged limits.

Parent integration validation:
- PR #43 changes only `games/space-typing`;
- Platform CI #239: PASS;
- existing Monkeytype play-mode contract: PASS;
- shared vocabulary / curriculum / typing-text / music validation: PASS;
- Portal layout and game registry validation: PASS;
- Space Typing platform integration contract: PASS;
- Recall Typing tests/build: PASS;
- Space Typing tests/build: PASS;
- Portal build: PASS.

No other child gitlink, route, launcher or shared learning-data contract was changed by this integration.
