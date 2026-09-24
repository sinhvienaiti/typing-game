# Shared Learning System + Monkey Learning Expansion — Master Plan

## Status

**L02 COMPLETE / L03 NEXT**

Agreed on 2026-09-24.

This document is the source of truth for the next learning-system expansion across the local typing-game platform.

It covers **all newly confirmed scope**, not only Smart Review:

1. Shared Learning Profile / Learning Memory across games.
2. Smart Review Dashboard.
3. Smart Review Session / Review Builder.
4. Cross-game review execution.
5. Monkeytype Learning System.
6. Monkeytype Vietnamese IME-aware input/accuracy.
7. Monkeytype Sentence Builder / Word Order practice.
8. Grammar and sentence mastery tracking.
9. Pagination, search, filter and sort for review data.
10. Progressive rollout and validation rules.

Existing child-game behavior must not be removed merely to simplify this work.

---

# 1. Product goal

The platform should evolve from a collection of typing games into a connected English-learning system.

The user should be able to:

- learn vocabulary,
- recall meaning,
- listen and type,
- practice words in context,
- practice sentence order and grammar,
- automatically revisit weak material,
- review the same weak material through different games,
- inspect what is weak and why,
- see progress without being overwhelmed by statistics.

The platform must stay local-first, responsive and easy to understand.

The key product rule is:

~~~text
all games contribute to one learning profile
→ Smart Review decides what needs attention
→ the user can choose how and where to review it
~~~

---

# 2. Architecture principle

## 2.1 Shared learning intelligence belongs to the parent platform

Smart Review must not be independently implemented inside every child game.

The parent platform owns the canonical learning state and review logic.

Conceptually:

~~~text
typing-game
├── Shared Learning Profile
├── Smart Review Engine
├── Smart Review Dashboard
├── Review Builder
└── Review Session orchestration

child games
├── emit learning events
└── consume review datasets
~~~

This prevents different games from calculating mastery differently.

## 2.2 Child games remain independent repositories

Existing repository boundaries remain unchanged.

The parent coordinates shared learning contracts; game implementation stays inside the relevant child repository.

No child source should be copied into the parent.

## 2.3 Local-first

Do not introduce a cloud service merely for this feature.

The first implementation should use a local persistent store suitable for cross-subdomain access through the platform architecture.

The data layer must be abstracted so storage can evolve later without rewriting the learning logic or UI.

---

# 3. Shared Learning Profile

The shared profile is the canonical record of learning history.

It must support at least three learning entities:

~~~text
Vocabulary
Grammar
Sentence
~~~

## 3.1 Vocabulary record

Minimum fields:

~~~text
wordKey
attempts
correct
wrong
hints
replays
avgResponseMs
correctStreak
lastSeenAt
lastCorrectAt
lastWrongAt
mastery
recentMistakes[]
sourceGames[]
~~~

wordKey should use the same normalized key convention already used by the shared vocabulary library.

Do not duplicate EN/VI/IPA into the learning record when the canonical shared vocabulary source already owns those values.

## 3.2 Grammar record

Minimum fields:

~~~text
grammarId
attempts
correct
wrong
mastery
errorTypes{}
lastSeenAt
lastCorrectAt
lastWrongAt
sourceGames[]
~~~

Examples:

~~~text
present
past
future
present-perfect
articles
prepositions
word-order
questions
negatives
~~~

The user-facing curriculum can stay simplified while the internal identifier remains precise enough for review.

## 3.3 Sentence record

Minimum fields:

~~~text
sentenceId
attempts
correct
wrong
mastery
errorTypes{}
recentAnswers[]
lastSeenAt
lastWrongAt
~~~

Recent raw answers must be bounded.

Do not keep unlimited history.

## 3.4 Bounded mistake samples

The profile should retain aggregate statistics plus a small number of recent examples.

Recommended initial bound:

~~~text
5-10 recent mistake samples per item
~~~

Example:

~~~text
environment
→ enviroment
→ environmant
~~~

This is more useful than only showing a mistake count, while avoiding unbounded storage growth.

---

# 4. Shared learning events

Games should emit a common event contract rather than implementing Smart Review logic themselves.

Conceptual event:

~~~text
learningAttempt({
  entityType,
  entityId,
  gameId,
  activityType,
  result,
  responseMs,
  hintUsed,
  replayUsed,
  userAnswer,
  expectedAnswer,
  errorType,
  occurredAt
})
~~~

Supported entityType:

~~~text
vocabulary
grammar
sentence
~~~

Useful activityType examples:

~~~text
typing
recall
listening
sentence-builder
cloze
combat
shooter
karaoke
~~~

The shared engine updates mastery and review priority from these events.

---

# 5. Mastery model

Mastery is a learning indicator, not a literal percentage of knowledge.

User-facing label:

~~~text
Mastery
~~~

or:

~~~text
Learning strength
~~~

Do not label it as an exact measurement of knowledge.

Initial mastery inputs may include:

- correctness ratio,
- recent mistakes,
- correct streak,
- response speed,
- hint usage,
- replay usage,
- time since last successful recall,
- recent regression.

Suggested display bands:

~~~text
0-39   Needs Review
40-69  Learning
70-89  Improving
90-100 Mastered
~~~

The exact weighting should be deterministic, documented and testable.

Do not calculate mastery independently in each game.

---

# 6. Smart Review priority

The system must support more than fixed date ranges.

Primary review sets:

~~~text
Due Now
Today’s Mistakes
Recent 7 Days
Recent 30 Days
Weakest Items
At Risk / Forgotten
Custom
~~~

Due Now should be the default Smart Review set.

Date-based review remains available because it is intuitive, but it is not the core intelligence.

## 6.1 At Risk / Forgotten

This group identifies items that were previously strong but are now at risk because of:

- long time since review,
- recent mistakes after a strong period,
- declining response quality,
- broken correct streak.

## 6.2 Smart Priority

Default table sort and default review ordering should use a shared review-priority score.

It may consider:

- low mastery,
- recent failure,
- repeated failure,
- time since successful review,
- slow response,
- hint/replay dependence,
- current due status.

---

# 7. Smart Review Dashboard

Smart Review requires a dedicated parent-platform screen.

Its purpose is to answer:

1. What am I weak at?
2. Why is it considered weak?
3. What should I review next?

## 7.1 Summary area

Initial summary cards:

~~~text
Needs Review
Improving
Mastered
Review Today
~~~

Primary action:

~~~text
Start Smart Review
~~~

## 7.2 Main tabs

~~~text
Words
Grammar
Sentences
~~~

## 7.3 Main list/table

Desktop should use a clean modern data table.

Do not overload the list with every metric.

Recommended visible word columns:

~~~text
Word / meaning / IPA
Mastery
Mistakes
Last mistake
Source
~~~

Meaning and IPA can live under the word instead of separate columns.

Example:

~~~text
environment
môi trường
/ɪnˈvaɪrənmənt/

42% Needs Review | 5 mistakes | Today | Recall +2
~~~

Clicking the row opens details.

## 7.4 Pagination

Pagination is required from the beginning.

Default:

~~~text
25 items per page
~~~

User options:

~~~text
10
25
50
100
~~~

Display:

~~~text
Showing 1-25 of 1,438
Previous 1 2 3 4 5 ... 58 Next
~~~

Do not render the entire dataset at once.

The query contract should support:

~~~text
page
pageSize
search
filters
sort
~~~

and return:

~~~text
items
totalItems
totalPages
~~~

## 7.5 Search

Search should support practical lookup.

For vocabulary:

- English word/phrase,
- Vietnamese meaning.

For grammar:

- grammar label,
- related category.

For sentences:

- sentence text.

## 7.6 Filters

Primary visible filters:

~~~text
Status
Source Game
Last Seen / Last Mistake
Mastery
~~~

Advanced filters under More Filters:

~~~text
Mistake count
Hint count
Replay count
Response speed
Correct streak
Grammar category
Word type
Topic
Level
Custom date range
~~~

## 7.7 Quick filters

Useful chips:

~~~text
Needs Review
Missed Today
Slow Words
Used Hint
Not Seen 7d+
At Risk
~~~

## 7.8 Sorting

Required sorts:

~~~text
Smart Priority
Lowest Mastery
Most Mistakes
Most Recent Mistake
Oldest Review
Slowest Response
Most Attempts
A-Z
Z-A
~~~

## 7.9 State persistence

Filter, sort, pagination and active tab should survive:

- opening/closing a detail drawer,
- browser refresh,
- Back/Forward navigation where practical.

A query-state URL is recommended, for example:

~~~text
/review?tab=words&status=weak&game=space&sort=mistakes&page=4
~~~

## 7.10 Mobile

Desktop: table.

Small screens: compact cards.

Do not squeeze the full desktop column layout onto mobile.

---

# 8. Smart Review detail drawer

Clicking an item opens a detail panel.

For vocabulary, show:

~~~text
word
IPA
Vietnamese meaning
mastery
attempts
correct
mistakes
hints
replays
average response
last seen
last mistake
next review
source games
recent mistakes
common mistake
why review
practice now
~~~

Example insight:

~~~text
Common mistake:
enviroment → environment
~~~

## 8.1 Why am I reviewing this?

The detail view must explain review priority in plain language.

Examples:

~~~text
Missed 2 of the last 3 attempts
Average response is slower than usual
Last successful recall was 6 days ago
~~~

This keeps Smart Review understandable rather than appearing random.

---

# 9. Smart Review Session

The Dashboard is for inspection.

A separate Review Session flow is required for actual practice.

## 9.1 Quick Review

Default entry point:

~~~text
Smart Review — 15 min
~~~

The engine chooses:

- due items,
- appropriate activity,
- ordering,
- amount of repetition.

This is the simplest path.

## 9.2 Custom Review Builder

The user may choose:

### Review set

~~~text
Due Now
Today
7 Days
30 Days
Weakest
At Risk
Custom
~~~

### Content

~~~text
Vocabulary
Grammar
Sentences
~~~

### Amount

~~~text
10
20
30
50
All
~~~

### Source filter

~~~text
All Games
Monkeytype
Recall Typing
Vocabulary Shooter
Space Typing
Karaoke Typing
~~~

### Review goal

~~~text
Remember words
Spelling
Listening
Grammar
Sentence building
Mixed
~~~

### Game

~~~text
Monkeytype
Recall Typing
Vocabulary Shooter
Space Typing
Karaoke Typing
Mixed Review
~~~

## 9.3 Capability matching

Not every game supports every review entity.

The review UI must only route compatible material.

Initial capability expectation:

~~~text
Monkeytype
- Vocabulary: yes
- Listening: yes
- Grammar: yes
- Sentences: yes

Recall Typing
- Vocabulary: yes
- Listening: yes
- Grammar: no/limited
- Sentences: no/limited

Vocabulary Shooter
- Vocabulary: yes
- Listening: optional/limited
- Grammar: no
- Sentences: no

Space Typing
- Vocabulary: yes
- Listening: optional/limited
- Grammar: no
- Sentences: no

Karaoke Typing
- Vocabulary: yes
- Listening: yes
- Grammar: limited
- Sentences/phrases: yes
~~~

If a selected game cannot review all chosen items, tell the user how many are compatible and preserve the remainder for another activity.

## 9.4 Mixed Review

Mixed Review lets the platform choose multiple activities/games in one review session.

Example:

~~~text
5 Recall
→ 5 Listening
→ 5 Space Typing
→ 5 Sentence Builder
~~~

The longer-term goal is to match activity to weakness:

~~~text
spelling problem
→ typing

listening problem
→ listen-and-type

slow recognition
→ shooter

long time not seen
→ contextual/game exposure

grammar problem
→ sentence builder / cloze
~~~

---

# 10. Review completion

After a review session, show a concise result:

~~~text
20 reviewed
16 correct
4 need more practice
Mastery improved: 61% → 68%
~~~

Also show:

~~~text
Strongest improvement
Still weak
~~~

Action:

~~~text
Review difficult items again
Finish
~~~

Review Again should target only items that remain weak in the current session.

Do not force the user to repeat indefinitely.

---

# 11. Monkeytype Learning System

Monkeytype becomes the first game to expose the full learning toolkit.

Normal Monkeytype typing remains intact.

New learning modes:

~~~text
Normal Typing
Learn
Recall
Listen
Sentence Builder
Context / Cloze
Smart Review
Adaptive Mix
~~~

## 11.1 Learn

Show:

- English,
- Vietnamese,
- IPA,
- pronunciation.

The learner types the English target.

Use mainly for new material.

## 11.2 Recall

Prompt with Vietnamese meaning and supporting learning cues.

The learner recalls and types English.

This should build on existing Monkeytype Recall behavior rather than reimplementing it from scratch.

## 11.3 Listen

Hide English.

Play pronunciation.

The learner types what they heard.

Support:

- replay,
- reveal letter,
- response-time tracking.

## 11.4 Context / Cloze

Use the existing shared typing-text/curriculum data where practical.

Example:

~~~text
I went to the ____ yesterday.
~~~

The user types the missing target.

This teaches use in context rather than isolated recall.

## 11.5 Adaptive Mix

Longer-term default learning experience.

A session may mix:

~~~text
new words
recall
listening
sentence building
context
smart review
~~~

The engine chooses based on current learning state.

---

# 12. Monkeytype Sentence Builder / Word Order

Sentence Builder is a confirmed learning mode.

Goal:

- practice word order,
- tense/time usage,
- grammar,
- phrase structure,
- memory.

Example shuffled prompt:

~~~text
nay / Tôi / với / chơi / đi / con / nay / hôm / gái
~~~

A valid answer may be:

~~~text
Tôi hôm nay đi chơi với con gái.
~~~

But the system must support more than one valid answer where language permits it.

Example:

~~~text
Tôi hôm nay đi chơi với con gái.
Hôm nay tôi đi chơi với con gái.
~~~

Both may be accepted.

## 12.1 Answer validation

Do not assume exactly one canonical string.

Each exercise may have:

~~~text
acceptedAnswers[]
~~~

Longer-term validation may normalize:

- punctuation,
- whitespace,
- capitalization where appropriate.

Do not accept grammatically invalid permutations merely because all words are present.

## 12.2 Difficulty

Suggested progression:

~~~text
Easy
- keep sentence-start cue
- keep punctuation
- fewer shuffled units

Normal
- shuffle all required words

Hard
- optional distractor words

Extreme
- show meaning/prompt and require free sentence production
~~~

## 12.3 Hints

Possible hints:

~~~text
Reveal next word
Grammar pattern
Reveal structure
~~~

Example:

~~~text
S + have/has + V3
~~~

## 12.4 Error classification

Sentence Builder should emit structured error types where reasonably detectable:

~~~text
word-order
wrong-tense
missing-word
extra-word
wrong-form
spelling
punctuation
~~~

This lets Smart Review identify grammar weakness even when vocabulary spelling is correct.

---

# 13. Grammar mastery

Smart Review must not treat every mistake as a vocabulary mistake.

Example:

~~~text
Expected:
I have lived here since 2020.

User:
I lived here since 2020.
~~~

The words may be correctly spelled, but the learning problem is grammar.

The event should be able to record:

~~~text
grammarId: present-perfect
errorType: tense
~~~

Dashboard example:

~~~text
Present Perfect
Mastery 41%
8 exercises
5 incorrect
Common issue: Past Simple used instead of Present Perfect
~~~

This is a core requirement for Sentence Builder and Context/Cloze.

---

# 14. Vietnamese input support in Monkeytype

Monkeytype currently evaluates English-style direct key input.

This causes incorrect accuracy penalties when typing Vietnamese through UniKey/macOS IME.

Example target:

~~~text
ấ
~~~

Telex physical input may be:

~~~text
a
a
s
~~~

The intermediate physical keys must not be treated as three incorrect target characters.

## 14.1 New input-language / accuracy behavior

Add a user-facing input mode such as:

~~~text
Input Language
- English
- Vietnamese
- Auto
~~~

or an equivalent design that clearly distinguishes direct key input from IME-composed text.

The exact UI wording may be refined during implementation.

## 14.2 IME-aware processing

Vietnamese mode must be composition-aware.

Relevant browser events include:

~~~text
compositionstart
compositionupdate
compositionend
beforeinput
input
~~~

While composition is active:

~~~text
event.isComposing === true
→ do not finalize correctness/accuracy from intermediate physical keys
~~~

Accuracy should be applied when the IME commits the resulting character/text.

## 14.3 Unicode normalization

Before correctness comparison, normalize both target and committed text using NFC.

This avoids false mismatches between visually identical precomposed/decomposed Vietnamese Unicode sequences.

## 14.4 Vietnamese accuracy semantics

For Vietnamese IME mode:

- accuracy is based on committed grapheme/text,
- progress is based on committed grapheme/text,
- temporary composition keystrokes do not create accuracy penalties,
- composition-time backspace does not create false mistakes,
- raw physical keystrokes may be retained separately for diagnostic/statistical use,
- raw keystroke count must not be confused with committed character accuracy.

Example:

~~~text
target: ấ
physical keys: a a s
committed result: ấ

learning/typing result:
1 committed character
1 correct character
no false penalty
~~~

## 14.5 Do not implement a second Telex engine by default

Do not manually convert:

~~~text
aas → ấ
~~~

inside Monkeytype when the system IME/UniKey already performs composition.

A custom Telex engine would create unnecessary complexity and can conflict with the active IME.

A future explicit raw-Telex mode can be evaluated separately if required.

## 14.6 Compatibility

English/direct typing must preserve existing behavior.

Vietnamese IME support must be opt-in or safely auto-detected without changing normal English scoring.

---

# 15. Cross-game Smart Review integration

Smart Review should eventually cover all platform games.

Recommended integration order:

~~~text
1. Parent Shared Learning Profile + Dashboard foundation
2. Monkeytype full integration
3. Recall Typing
4. Vocabulary Shooter
5. Space Typing
6. Karaoke Typing
~~~

Every integration must:

- emit shared events,
- consume review datasets only through a documented contract,
- preserve existing game behavior outside Review mode,
- avoid repeated review spam,
- keep game performance stable.

---

# 16. Cross-subdomain persistence

The platform currently uses separate internal origins for child games.

Therefore child-local localStorage cannot be treated as a shared cross-game database.

A shared mechanism is required.

The exact implementation should be selected after inspecting the current Portal/game messaging architecture.

Acceptable local-first directions include:

- parent-owned persistent storage with iframe postMessage contracts,
- parent-owned IndexedDB accessed through a message API,
- another equally local architecture that preserves repository boundaries.

Do not duplicate a full learning profile independently in each child game.

---

# 17. Performance requirements

Learning telemetry must not create input lag or animation stutter.

Rules:

- no synchronous full-profile serialization after every keystroke,
- batch/debounce persistent writes,
- avoid rescanning full history during normal input,
- use aggregate counters,
- bound mistake samples,
- calculate heavy review queries outside frame-critical paths,
- paginate dashboard queries,
- do not load all detailed history merely to render a page.

Performance fixes must address incorrect processing, not remove learning features to hit budgets.

---

# 18. Privacy / local data

This is a local/private learning platform.

Learning history should remain local by default.

No remote analytics is required.

The user should eventually have clear controls for:

~~~text
Export learning profile
Import learning profile
Reset selected learning history
Reset all learning history
~~~

Destructive reset must require confirmation.

---

# 19. Implementation phases

## L00 — Reconstruct and contract audit

**Status: COMPLETE — 2026-09-24**

Audit findings:

- Parent `main` reconstructed from GitHub at `28f0cf60c3c820b6194373b444422ae366504f1a` before implementation work.
- Portal currently owns iframe lifecycle and already has a narrow cross-origin `postMessage` bridge for shared music state and child speech activity; Shared Learning must extend this existing parent-owned boundary instead of introducing a second competing bridge.
- Child origins are registry-driven and the Portal validates both `event.origin` and the active iframe `event.source`; L02 must preserve and extend that trust model with versioned payload validation.
- Shared vocabulary remains canonical in `shared/vocabulary/levels/*.json`; normalized vocabulary keys use NFKC + trimmed/collapsed whitespace + lowercase, matching `scripts/vocabulary-core.mjs#normalizeEnglish`.
- Curriculum/topic/POS/grammar metadata remains additive and references the same 18,000-word library rather than duplicating EN/VI/IPA values.
- Monkeytype Recall/EN-VN already has shared greedy longest-match phrase selection, Recall start markers, pronunciation hooks and local settings. Later learning modes must reuse those hooks instead of rebuilding Recall or dictionary matching.
- Vocabulary Shooter, Recall Typing and Space Typing already consume the shared curriculum/library contracts; Karaoke remains primarily lyric/audio driven.
- No existing parent Shared Learning Profile, mastery engine, Smart Review engine or learning-event persistence layer was found.

Versioning contract fixed for implementation:

~~~text
Learning Event schema version: 1
Learning Profile schema version: 1
Parent learning database: typingGameLearning
Parent profile store: state
Canonical profile key: profile
Recent sample bound: 8 per item
Reserved learning message namespace for L02: typing-game:learning:v1
~~~

Learning Event v1 requires:

~~~text
version
entityType: vocabulary | grammar | sentence
entityId
gameId
activityType
result: correct | wrong
occurredAt
~~~

Optional event fields:

~~~text
responseMs
hintUsed
replayUsed
userAnswer
expectedAnswer
errorType
~~~

For `entityType=vocabulary`, `entityId` is normalized using the same canonical vocabulary key rule above. Grammar and sentence IDs remain stable authored identifiers.

The parent remains the only canonical calculator of mastery/review priority. Child games emit events; they must not persist divergent mastery scores of their own.

## L01 — Shared Learning Core

**Status: COMPLETE — 2026-09-24**

Implemented in parent:

- `shared/learning/core.mjs` as the canonical Learning Event/Profile v1 engine;
- shared vocabulary-key normalization matching the existing 18k library contract;
- vocabulary / grammar / sentence aggregate records;
- deterministic mastery v1 and review-priority v1 calculations;
- deterministic next-review timestamps;
- bounded mistake and sentence-answer histories (8 samples per item);
- parent-owned IndexedDB persistence in `shared/learning/browser-store.mjs`;
- serialized store writes so concurrent operations cannot overwrite one another;
- root `learning:check` / `learning:test` scripts;
- Platform CI learning-core gate;
- focused Node tests for validation, normalization, aggregates, bounded history, grammar classification and priority ordering.

Local verification before push: 7/7 tests PASS.

The core records completed learning attempts, not physical keystrokes, so it does not introduce per-key synchronous profile serialization.


## L02 — Parent messaging bridge

**Status: COMPLETE — 2026-09-24**

Implemented cross-origin communication between parent and child games:

- versioned `typing-game:learning:v1` message namespace;
- validated Attempt and Query requests plus Ack / Query Result / Error responses;
- exact active iframe source + child origin validation;
- Attempt `gameId` must match the active registry game;
- bounded request IDs, strings, page sizes and filter ranges;
- parent batching at up to 32 events with a short 150 ms persistence debounce;
- atomic serialized `applyMany()` persistence so concurrent batches cannot overwrite one another;
- read-after-write consistency by flushing pending attempts before a query;
- bounded parent query API with page/pageSize/search/filter/sort;
- TypeScript declarations for the shared ESM contracts;
- Portal integration that preserves the existing shared music/speech bridge behavior;
- page-hide best-effort flush without introducing per-keystroke persistence.

Verification:

- learning contract/query tests PASS;
- Platform CI #264 PASS, including Portal TypeScript/Vite build with the production bridge;
- Platform CI #265 passed the expanded Shared Learning validation step after `learning:check` and `learning:test` were widened to all current shared-learning modules.


## L03 — Smart Review Dashboard V1

Implement:

- summary cards,
- Words/Grammar/Sentences tabs,
- search,
- filters,
- sort,
- pagination,
- detail drawer,
- Why Review explanations,
- responsive/mobile layout.

## L04 — Smart Review Builder + Session Core

Implement:

- Due Now,
- Today,
- 7 Days,
- 30 Days,
- Weakest,
- At Risk,
- Custom,
- content selection,
- count selection,
- goal selection,
- compatible-game selection,
- Quick Review.

## L05 — Monkeytype Vietnamese IME

Implement and test:

- input language option,
- composition-aware input,
- NFC normalization,
- committed-character accuracy,
- English regression behavior,
- Vietnamese test cases.

Minimum Vietnamese regression examples should include characters/words such as:

~~~text
ấ
ộ
ường
nghiêng
Việt Nam
~~~

## L06 — Monkeytype Learning Memory integration

Monkey emits shared events for:

- normal learning typing,
- existing recall mode,
- pronunciation/replay where relevant,
- hints where relevant,
- response timing.

Normal Monkeytype mode remains compatible.

## L07 — Monkey Learn + Listen

Implement:

- Learn mode,
- Listen mode,
- replay/reveal behavior,
- shared learning event output,
- review dataset input.

## L08 — Sentence Builder V1

Implement:

- shuffled word units,
- acceptedAnswers[],
- basic normalization,
- difficulty presets,
- hints,
- scoring,
- grammar/sentence events.

## L09 — Context / Cloze

Integrate shared typing text/curriculum data.

Implement contextual vocabulary and grammar exercises without duplicating source data.

## L10 — Monkey Smart Review

Monkey consumes parent-provided review datasets.

Support review goals:

- remember,
- spelling,
- listening,
- grammar,
- sentence building,
- mixed.

## L11 — Recall Typing integration

Emit learning events and accept compatible vocabulary/listening review datasets.

Avoid duplicating the existing Recall-specific local memory logic without an explicit migration plan.

## L12 — Vocabulary Shooter integration

Emit shared vocabulary events.

Support review runs using selected weak/due words while preserving normal Class/Custom modes.

## L13 — Space Typing integration

Emit shared vocabulary learning signals.

Allow Smart Review vocabulary runs while keeping Campaign/gameplay systems intact.

Do not cause spawn repetition that harms gameplay readability.

## L14 — Karaoke Typing integration

Capture vocabulary/phrase/context mistakes where reliable.

Support compatible contextual review datasets.

## L15 — Mixed Review

Implement multi-activity/multi-game session orchestration.

The parent should track session progress across transitions.

## L16 — Adaptive Mix

Use learning state to choose the activity best suited to the weakness.

Keep the algorithm transparent and deterministic enough to test.

## L17 — Export / Import / Reset

Add local profile backup and maintenance controls.

## L18 — Final cross-game review

Review:

- correctness,
- persistence,
- migration,
- UI/UX,
- accessibility,
- performance,
- cross-game consistency,
- stale-data behavior,
- long-profile behavior,
- browser refresh/navigation,
- offline/static Play mode.

Fix confirmed issues rather than merely documenting them.

---

# 20. UI design principles

The new learning UI should be:

~~~text
simple
modern
information-dense only when needed
easy to scan
not admin-like
not visually noisy
~~~

Use progressive disclosure:

~~~text
summary
→ list
→ detail drawer
~~~

and:

~~~text
Quick Review
→ Customize only when wanted
~~~

Do not put every statistic in the main table.

Use labels plus visual indicators; do not rely on color alone.

---

# 21. Testing requirements

Every phase needs targeted tests.

Core test areas:

- mastery determinism,
- priority determinism,
- bounded histories,
- profile migrations,
- cross-origin message validation,
- paging/filter/sort correctness,
- URL/view-state restoration,
- accepted sentence alternatives,
- sentence error classification,
- Vietnamese IME composition,
- Unicode normalization,
- English regression behavior,
- review dataset compatibility per game,
- no feature regression in normal game modes,
- large-profile performance.

CI failures must be fixed at the root cause.

Do not weaken tests or raise performance thresholds merely to make CI green.

---

# 22. Documentation requirements

As implementation proceeds:

- update this master plan milestone status,
- update docs/PROJECT_CONTEXT.md at meaningful checkpoints,
- update affected child-repo design docs,
- record integration contracts,
- record storage/profile schema versions,
- keep GitHub as the only handoff source of truth.

Do not rely on conversation state for future continuation.

---

# 23. Definition of completion

This expansion is complete when:

1. one shared local Learning Profile exists,
2. all supported games can contribute compatible learning events,
3. Smart Review Dashboard clearly shows weak vocabulary/grammar/sentences,
4. pagination/search/filter/sort are complete,
5. Review Session supports Quick and Custom flows,
6. compatible review data can launch into selected games,
7. Monkey supports Learn / Recall / Listen / Sentence Builder / Context / Smart Review,
8. Vietnamese IME input does not receive false accuracy penalties,
9. grammar mistakes are tracked separately from spelling mistakes,
10. Mixed Review works across compatible activities,
11. persistence/export/reset behavior is documented and tested,
12. normal game modes remain stable and performant,
13. parent and child CI/build checks pass.
