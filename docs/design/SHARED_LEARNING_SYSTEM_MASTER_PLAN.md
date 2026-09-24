# Shared Learning System + Monkey Learning Expansion — Master Plan

## Status

**L12 COMPLETE / L13 NEXT**

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

**Status: COMPLETE — 2026-09-24**

Implemented one canonical parent review planner and session shell:

- review sets: Due Now / Today’s Mistakes / Recent 7 Days / Recent 30 Days / Weakest / At Risk / Custom;
- content selection: Vocabulary / Grammar / Sentences;
- count selection: 10 / 20 / 30 / 50 / All;
- source-game filter;
- goals: remember words / spelling / listening / grammar / sentence building / mixed;
- compatible-game capability matrix;
- incompatible content is preserved/excluded instead of silently routed to an unsupported game;
- Quick Smart Review uses a 15-minute target, Due Now, mixed content/goal and the shared mixed-review planner;
- parent-only `/review/build` Review Builder;
- parent-only `/review/session` persisted session shell using sessionStorage;
- Dashboard Start Smart Review and item-level Practice Now now route into the Builder;
- exact-item Practice Now scopes the plan to that entity/item;
- shared At Risk logic is canonical in `review-session.mjs` and reused by the Dashboard;
- child game adapters intentionally remain in their own later milestones; the parent session does not fabricate child integration before those adapters exist.

Verification:

- planner/unit coverage for set semantics, amount/source filtering, capability matching, Quick Review and At Risk rules;
- a failing Recent-30-Days fixture was corrected because the roadmap defines date sets as recent **mistakes**, while the fixture had incorrectly created a successful attempt;
- Platform CI #292: PASS, including shared-learning tests, Portal TypeScript/Vite build, Recall tests/build and Space tests/build.


## L05 — Monkeytype Vietnamese IME

**Status: COMPLETE — 2026-09-24**

Implemented in `sinhvienaiti/monkeytype` on `feature/en-vn-translation`:

- user-facing Input Language option: Auto / English / Vietnamese;
- existing browser compositionstart / compositionupdate / compositionend flow remains authoritative, so intermediate Telex/IME physical keys are not scored as committed characters;
- Vietnamese committed text and target comparison use Unicode NFC without introducing a second Telex engine;
- multi-character commits are replayed through the normal scorer by Unicode code point rather than UTF-16 code unit;
- Auto enables Vietnamese IME normalization for Vietnamese test languages while English/direct input keeps existing behavior;
- composition quick-end comparison uses the same canonical committed/target form;
- regression coverage includes `ấ`, `ộ`, `ường`, `nghiêng`, decomposed Vietnamese targets, Auto mode and explicit English behavior.

Child checkpoint:

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation
dd700f3e4f0fd33c6ca1259d4987bdfcc4465305
~~~

Verification:

- Custom EN-VN CI run 35999852048: PASS;
- frontend lint PASS;
- changed-style lint PASS;
- local-static production build PASS;
- full frontend test suite PASS.

## L06 — Monkeytype Learning Memory integration

**Status: COMPLETE — 2026-09-24**

Monkeytype now emits the parent-owned shared learning contract for dictionary-backed learning attempts:

- one vocabulary event per completed learning item/phrase rather than per keypress;
- greedy multi-word dictionary matches stay one canonical vocabulary attempt;
- normal EN-VN learning typing emits `activityType=typing`;
- existing Recall mode emits `activityType=recall` without reimplementing Recall;
- response time is measured from learning-cue presentation to item completion;
- event output includes user answer, expected answer, correctness, hint/replay dependence flags and canonical Monkeytype game ID;
- helper hooks exist for explicit hint/replay actions; automatic pronunciation is not falsely counted as a user replay;
- matching is cached per test/dictionary and completion uses the current word snapshot, avoiding synchronous per-keystroke persistence/history rescans;
- child only posts the shared event; parent bridge remains the sole owner of validation, batching, persistence, mastery and review priority.

Child checkpoint:

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation
d4ffe3131153f93da8c1ee24a0161fed9c66c5ba
~~~

Verification:

- Custom EN-VN CI run 36000835083: PASS;
- frontend lint PASS;
- changed-style lint PASS;
- local-static production build PASS;
- full frontend test suite PASS, including single-word, greedy multi-word, Recall, hint/replay and non-learning-mode regression coverage.

Normal Monkeytype mode remains compatible.

## L07 — Monkey Learn + Listen

**Status: COMPLETE — 2026-09-24**

Implemented on the existing Monkeytype learning surface without replacing normal typing:

- explicit Normal / Learn / Recall / Listen modes;
- Learn presents English + Vietnamese + shared-library IPA and auto-pronounces the active vocabulary item;
- Recall keeps the existing hidden-English behavior rather than creating a second recall implementation;
- Listen hides the English target and IPA while using item-level pronunciation;
- Listen provides explicit Replay and Reveal Letter controls;
- Reveal Letter exposes a cumulative prefix cue without mutating Monkeytype's core per-character scorer;
- explicit replay/hint actions feed `replayUsed` / `hintUsed` into the shared Learning Event;
- learning attempts now identify `typing`, `learn`, `recall` and `listen` activity types;
- a bounded parent-review dataset input accepts 1–100 vocabulary items from `https://typing-game.local`, canonicalizes/deduplicates them and rejects non-vocabulary content;
- review datasets resolve through the shared 18k vocabulary source, keep parent ordering, construct one bounded Custom test and fail closed when any requested item cannot be resolved;
- review vocabulary is cached as a distinct source so Custom / Library / Topic / Word type / Grammar state remains intact;
- no child-side mastery, priority or Smart Review engine was introduced.

Child checkpoint:

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation
637f607a23a44a62c4c1392297b7526526b34f27
~~~

Verification:

- Custom EN-VN CI run 36004240518: PASS;
- frontend lint PASS;
- changed-style lint PASS;
- local-static production build PASS;
- full frontend test suite PASS;
- regression coverage includes Learn/Listen activity labels, review-dataset validation, multi-word review input, unresolved-item failure and shared IPA metadata.


## L08 — Sentence Builder V1

**Status: COMPLETE — 2026-09-24**

Implemented in Monkeytype as a dedicated learning surface rather than forcing sentence-order gameplay through the per-character typing scorer:

- shuffled word/unit builder with click-to-compose plus direct text input;
- `acceptedAnswers[]` supports multiple authored valid answers and records the actually matched valid answer;
- normalization covers NFC, whitespace, capitalization and punctuation spacing while preserving punctuation correctness;
- Easy / Normal / Hard / Extreme difficulty presets;
- Easy keeps a sentence-start cue, Normal shuffles required units, Hard adds optional distractors, Extreme uses free production;
- Reveal Next Word, Grammar Hint and Structure Hint controls;
- custom exercise authoring in Custom Text settings with sentence ID, optional grammar ID, prompt/context, multiple accepted answers, difficulty, distractors and grammar hint;
- optional authored mistake mappings use `answer => error-type` for reliable grammar cases such as wrong-tense;
- generic fallbacks classify word-order / missing-word / extra-word / spelling / punctuation / wrong-form;
- one sentence learning event is emitted per submission plus a grammar event when `grammarId` is present;
- hint use, response time, user answer, expected answer and error type flow into the parent shared Learning Event contract;
- normal Monkeytype word-learning UI is explicitly isolated from Sentence Builder mode;
- no child-side mastery/review engine was introduced.

Child checkpoint:

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation
7b939dec3b1c913e048c62a0876b489e4ba067ac
~~~

Verification:

- Custom EN-VN CI run 36008893127: PASS;
- type-aware frontend lint PASS;
- changed-style lint PASS;
- local-static production build PASS;
- full frontend test suite PASS;
- tests cover alternative valid answers, authored grammar error mappings, normalization, all four difficulty presets, hints and sentence+grammar event output.


## L09 — Context / Cloze

**Status: COMPLETE — 2026-09-24**

Implemented in Monkeytype from existing shared data only:

- dedicated Context/Cloze learning mode and test panel;
- selected shared Typing Text level + passage count is reused as the source context;
- passage access now exposes the same cached/shuffle-bag-backed passage records used by normal typing-text mode rather than copying passages;
- vocabulary cloze exercises are derived from each passage's existing `targetWords`;
- grammar cloze exercises are derived from the existing shared grammar module `signalTokens`;
- vocabulary and grammar exercises are interleaved in one bounded context session;
- masking respects whole words/phrases and preserves the original surrounding sentence;
- one submitted answer produces at most one learning event, preventing retry/event spam;
- vocabulary mistakes emit `spelling`; grammar mistakes emit `wrong-form`, while Present/Past/Future time-group misses emit `wrong-tense`;
- reveal-letter hint use and response timing are included in the shared Learning Event;
- Context/Cloze remains scoped to Custom learning mode and is isolated from normal Monkeytype word rendering;
- shared level JSON is cached for the session and grammar tokens are precomputed once per generated session;
- no separate context sentence/exercise corpus and no child Smart Review engine were introduced.

Child checkpoint:

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation
626b51766850f9de712ec0ae4c1fea2efaf7aba9
~~~

Verification:

- Custom EN-VN CI run 36010643624: PASS;
- type-aware frontend lint PASS;
- changed-style lint PASS;
- local-static production build PASS;
- full frontend test suite PASS;
- tests cover whole-phrase masking, shared passage reuse/shuffle progress, vocabulary + grammar derivation, spelling/wrong-tense classification, hints and cloze Learning Events.


## L10 — Monkey Smart Review

**Status: COMPLETE — 2026-09-24**

The parent remains the single Smart Review planner and Monkeytype now consumes its bounded review queue through the shared postMessage contract.

Implemented:

- parent Review Session builds a versioned Monkey dataset from the parent-owned Learning Profile;
- dataset carries goal, ordered items, mastery/review-priority display metadata, recent mistake context and remembered sentence accepted answers without copying mastery logic into Monkeytype;
- Portal queues the dataset in session storage, launches Monkeytype, posts only to the child origin and handles ready/error acknowledgement;
- child validates the parent `goal + items` contract and mirrors the same goal/entity compatibility boundary;
- one dedicated Smart Review coordinator sequences the parent queue while leaving selection/order/mastery/review priority parent-owned;
- remember/spelling/listening vocabulary items resolve through the shared 18k vocabulary library;
- mixed vocabulary routing is deterministic: previous listening weakness → Listening, spelling error → Spelling, otherwise Recall;
- Grammar review reuses recent expected-answer context when available and otherwise falls back to the existing shared grammar module signal tokens;
- Sentence review reuses Sentence Builder validation and the accepted answers retained in shared learning memory;
- Mixed Review inside Monkeytype can sequence vocabulary / grammar / sentence items without creating a child review-priority engine;
- explicit reveal/replay usage, response time and the activity-specific result are emitted back through the standard Learning Event contract;
- Smart Review uses a dedicated bounded UI surface and keeps normal Monkeytype / Learn / Recall / Listen / Sentence Builder / Context-Cloze behavior isolated.

Parent checkpoint includes the L10 dataset builder, compatibility rules, Portal adapter, launch/status flow and tests.

Child checkpoint:

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation
01cca03b6f38c054f1fdd41ed5150160a6f3cd00
~~~

Verification:

- parent Platform CI at pre-pin L10 HEAD `783bcb80010dae7d4007bd64147e8d0e1ed14e09`: PASS;
- Monkeytype Custom EN-VN CI run 36016126490: PASS;
- child type-aware lint PASS;
- changed-style lint PASS;
- local-static production build PASS;
- full frontend test suite PASS;
- tests cover goal/entity validation, mixed activity routing, shared vocabulary enrichment, grammar context/fallback, Sentence Builder accepted answers, event output and queue activation.

## L11 — Recall Typing integration

**Status: COMPLETE — 2026-09-24**

Implemented without replacing Recall Typing's existing local vocabulary/settings behavior:

- normal Recall sessions now emit one shared vocabulary Learning Event per completed word rather than per keypress;
- response time begins when each hidden word becomes active;
- a word completed after one or more wrong letter attempts is recorded as a wrong spelling attempt, while clean completion is recorded as correct;
- explicit F2/speaker replay is tracked as `replayUsed`; automatic pronunciation is not misclassified as replay;
- normal audio-only Recall sessions emit listening activity, normal meaning/full hint sessions emit recall activity, and explicit spelling review emits typing activity;
- child accepts only origin-checked parent review datasets from `https://typing-game.local`;
- compatible review goals are Remember Words / Spelling / Listening / Mixed and dataset items must be vocabulary;
- review words resolve from the existing shared 18k vocabulary library, preserve the parent queue order and fail closed when any requested key is missing;
- Listening review forces the existing audio-only hint style while preserving the user's stored setting for normal play;
- review runs consume the full selected parent queue instead of re-randomizing it through the normal Recall session bag;
- selecting Class / Topic / Word type / Grammar / Custom manually exits review mode cleanly;
- no child mastery / review-priority engine and no migration of Recall's existing local vocabulary storage were introduced;
- parent Portal now creates/stores/launches Recall review datasets, posts only to the child origin and handles ready/error acknowledgement.

Child checkpoint:

~~~text
sinhvienaiti/recall-typing
main
59c1d6043a09c23108e2390a2e259bb1be23e83d
~~~

Verification:

- Recall Typing CI run 36017329739: PASS;
- parent Platform CI run 36018360661: PASS;
- parent shared-learning tests/checks PASS;
- Recall tests PASS;
- Portal build PASS;
- Recall production build PASS.


## L12 — Vocabulary Shooter integration

**Status: COMPLETE — 2026-09-24**

Implemented while preserving the existing Shooter modes and vocabulary source workflow:

- gameplay emits one shared vocabulary Learning Event per resolved target, never per keypress;
- a target completed without wrong keys is recorded as correct;
- a target completed after corrected key errors is recorded as wrong with `spelling`;
- a target that escapes/impacts is recorded as wrong with `missed-word`;
- response timing is measured from target presentation/Target Rush spotlight activation;
- parent Smart Review accepts Shooter-compatible Remember Words / Spelling / Mixed vocabulary queues only;
- selected review keys resolve through the shared 18k library, preserve the parent-selected set and fail closed if a key is missing;
- review execution reuses the existing Target Rush gameplay as a bounded run with `targetCount` equal to the selected review set;
- the temporary review mode/settings are not persisted over the user's normal Shooter settings;
- manual mode or Class / Topic / Word type / Grammar / Custom selection exits review mode and restores normal settings;
- normal Class/Custom/curriculum modes remain intact;
- the parent remains the sole owner of weak/due selection, mastery and review priority.

Child checkpoint:

~~~text
sinhvienaiti/vocab-shooter
main
b1721c43be075836a293fa6ba10ba908f4d06c22
~~~

Verification:

- Vocabulary Shooter CI run 36019201874: PASS;
- child tests PASS;
- child TypeScript check + production build PASS;
- parent Platform CI run 36019549335: PASS;
- shared learning tests/checks, Portal build and platform integration checks PASS.


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
