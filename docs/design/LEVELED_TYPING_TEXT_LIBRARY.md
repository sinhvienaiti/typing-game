# Leveled Typing Text Library and Random Practice Plan

## Status

**Approved design plan. Implementation has not started yet.**

This document is the source of truth for the next large learning-content phase of the local typing-game platform.

It covers four connected requirements:

1. Vocabulary Shooter must present vocabulary in randomized non-repeating order.
2. Recall Typing must present vocabulary in randomized non-repeating order.
3. Monkeytype must gain a level-based typing-text source built on the shared 100-level vocabulary library.
4. The platform must build and maintain a large reviewed English passage corpus for Levels 001-100.

The existing shared vocabulary library remains authoritative:

~~~text
100 levels
18,000 English entries
English + Vietnamese + IPA
shared/vocabulary/levels/*.json
~~~

This plan does not replace that library. It adds contextual typing material on top of it.

---

# 1. Goals

The same shared vocabulary should support three different learning styles:

~~~text
Vocabulary Shooter
-> fast recognition and active recall
-> randomized individual vocabulary targets

Recall Typing
-> recall English from learning cues
-> randomized individual vocabulary targets

Monkeytype
-> contextual reading and typing
-> randomized level-appropriate passages
~~~

The system must prioritize useful English, level-appropriate language, natural connected writing, broad topic diversity, strong vocabulary coverage, minimal repetition, deterministic validation, local/offline runtime, simple implementation and safe incremental Git delivery.

---

# 2. Non-goals

Do not turn this phase into:

- a cloud content service,
- an online article scraper at runtime,
- a backend database,
- an AI call required during gameplay,
- a replacement for the shared vocabulary library,
- one giant JSON file containing every passage,
- a copyright-sensitive collection of copied articles,
- a workflow that generates hundreds of files before QA.

Generation and research happen during content production. Gameplay must remain fully local after the content is committed.

---

# 3. Overall architecture

The platform will contain two shared datasets:

~~~text
shared/vocabulary/
-> individual vocabulary
-> English
-> Vietnamese
-> IPA
-> 100 levels

shared/typing-texts/
-> contextual English passages
-> built around shared vocabulary
-> 100 levels
~~~

Expected structure:

~~~text
shared/
  vocabulary/
    index.json
    lookup.json
    levels/
      001.json
      ...
      100.json

  typing-texts/
    index.json
    levels/
      001.json
      002.json
      ...
      100.json
~~~

No giant passage file is required.

---

# 4. Corpus size

Initial production target:

~~~text
100 level files
minimum 15 passages per level
250-300 English words per passage
20-30 target vocabulary entries per passage
~~~

Minimum corpus size:

~~~text
1,500 passages
375,000-450,000 English words
~~~

The initial production build should normally create exactly 15 reviewed passages per level. The schema must allow more passages later without changing the runtime contract.

---

# 5. Passage file contract

Example:

~~~json
{
  "version": 1,
  "level": 12,
  "cefr": "A2",
  "passages": [
    {
      "id": "L012-P001",
      "topic": "nature",
      "style": "narrative",
      "setting": "forest path",
      "tone": "calm",
      "targetWords": [
        "path",
        "quiet",
        "carry"
      ],
      "wordCount": 276,
      "text": "..."
    }
  ]
}
~~~

Required level fields:

~~~text
version
level
cefr
passages
~~~

Required passage fields:

~~~text
id
topic
style
setting
tone
targetWords
wordCount
text
~~~

The metadata exists for vocabulary coverage, diversity control, duplicate prevention and QA. Do not add metadata without a real use case.

---

# 6. Generated typing-text index

Generate:

~~~text
shared/typing-texts/index.json
~~~

The index should stay lightweight and contain:

~~~text
version
plannedLevels
availableLevels
totalPassages
totalWords
level number
CEFR
file path
passage count
~~~

Monkeytype reads the index to build the level selector, then fetches only the selected level file.

Do not fetch all 100 passage files at startup.

---

# 7. Relationship to vocabulary levels

Every typing-text level uses:

~~~text
shared/vocabulary/levels/NNN.json
~~~

as its vocabulary source.

Each passage selects 20-30 unique target vocabulary entries from the current level.

Rules:

- selected target words must actually appear naturally in the final passage,
- a target listed in metadata but absent from the text is invalid,
- a target not present in the corresponding vocabulary level is invalid,
- phrases may be used when they fit naturally,
- do not force an awkward word or phrase merely to satisfy coverage.

---

# 8. Vocabulary coverage strategy

Pure random selection is not sufficient during corpus creation.

Maintain a temporary usage counter for each level:

~~~text
word -> number of passages in which it has already been targeted
~~~

Selection rule:

~~~text
least-used vocabulary
+
controlled randomization
+
topic compatibility
~~~

Priority:

1. words never used as targets,
2. words used once,
3. words used twice,
4. heavily used words only when particularly natural.

The selection must still be randomized. It must not simply walk through the vocabulary file from top to bottom.

Initial level coverage goal:

- at least 90 percent of the level vocabulary appears as an explicit target in at least one passage,
- aim for near 100 percent when natural writing allows it,
- avoid using one target vocabulary item in more than four passages unless it is an ordinary high-frequency word,
- naturalness is more important than mathematically forcing 100 percent coverage.

The validator must produce a final coverage report for every level.

---

# 9. Level difficulty policy

Using 20-30 words from a level does not by itself make a passage level-appropriate.

Permanent principle:

~~~text
target vocabulary
-> current level

supporting vocabulary
-> mainly current level or easier

grammar and sentence structure
-> appropriate for the level CEFR profile
~~~

Avoid surrounding easy target vocabulary with much harder prose.

## A1

Prefer concrete everyday topics, short direct sentences, simple present or past structures, clear subjects and actions, common connectors, limited clause depth and little abstraction.

## A2

Prefer simple connected narratives, familiar situations, basic descriptions and explanations, simple cause and effect, and modest sentence variety.

## B1

Allow longer connected ideas, experiences and opinions, reasons and consequences, more descriptive detail and broader everyday or social topics.

## B2

Allow more detailed explanation, comparison, argument, broader technical or cultural subjects, richer sentence structures and more precise vocabulary.

## C1

Allow nuanced description, abstraction, analytical prose, varied sentence rhythm and complex relationships between ideas.

## C2 and Advanced

Allow highly varied syntax, subtle distinctions, specialized and abstract topics, and sophisticated but still natural prose.

Difficulty should rise gradually across the 100 levels. Adjacent levels should not feel like completely different courses.

---

# 10. Typing-text writing rules

These rules apply to the actual text value stored in every passage.

## 10.1 Language

- English only.
- Natural modern English.
- No Vietnamese inside the passage.
- No unexplained foreign-language phrases.

## 10.2 Narrative form

- One continuous coherent passage.
- No heading inside the text.
- No bullet list.
- No table.
- No Markdown.
- No code.
- No isolated sentence collection.
- No blank-line formatting inside the passage.
- Sentences must connect logically.

## 10.3 Character policy

Preferred allowed content:

~~~text
a-z
A-Z only where sentence capitalization requires it
space
comma
period
straight apostrophe
~~~

Do not use curly quotes, em dash, en dash, Unicode ellipsis, emoji, decorative symbols, bullets, brackets, parentheses, semicolons, colons or unusual Unicode characters in normal passage text.

Use commas and periods correctly rather than removing punctuation.

Straight apostrophes may be used for ordinary contractions or possessives when natural.

## 10.4 Capitalization policy

The corpus follows the strict typing convention:

- the first alphabetic character of a sentence is uppercase,
- ordinary words elsewhere remain lowercase,
- avoid content that requires internal capitalization,
- avoid proper names, brands, acronyms, titles and named places when practical,
- do not create unnatural lowercase versions of famous names merely to satisfy the rule, choose a different subject instead.

## 10.5 Punctuation

- periods define sentence boundaries,
- commas are used where grammatically useful,
- avoid comma-heavy artificial sentences,
- sentence rhythm must remain natural.

---

# 11. Content quality rule

A passage must not read like vocabulary filler.

Required qualities:

- a clear subject or situation,
- coherent development,
- meaningful links between sentences,
- natural transitions,
- enough detail to remain interesting,
- no obvious prompt-template language,
- no repeated generic moral ending,
- no robotic summary sentence added only to reach word count.

Target vocabulary must fit the passage rather than controlling every sentence.

---

# 12. Topic diversity

There is no narrow topic limit.

Topic families may include:

~~~text
daily life
home
family
friendship
food
cooking
shopping
school
work
hobbies
sports
travel
transportation
health habits
animals
plants
gardens
forests
rivers
oceans
weather
seasons
environment
simple science
technology
inventions
craft
design
history
culture
communities
public spaces
problem solving
personal experiences
observations
small adventures
fictional situations
practical situations
simple reports
explanations
reflections
social behavior
learning
memory
communication
cities
rural life
energy
space
engineering
art
music
books
games
research
ethics
economics
psychology
ecology
future scenarios
~~~

This list is deliberately open. Do not cycle through the same small set of themes every level.

---

# 13. Writing-style diversity

Changing only the topic is not enough.

Useful style families:

~~~text
short story
personal narrative
descriptive prose
explanatory article
practical situation
nature observation
small adventure
process explanation
reflective prose
factual article
problem and solution
comparison
cause and effect
day in the life
historical-style explanation
science explanation
social observation
scenario analysis
~~~

Do not enforce a rigid repeating passage template. Track style distribution and avoid clusters of near-identical structures.

---

# 14. Content signature

Each passage has a simple signature:

~~~text
topic
style
setting
tone
~~~

Before writing a new passage, inspect signatures in the same level, nearby levels and current batch.

Avoid repeatedly generating the same combination.

Keep the signature system simple. Its purpose is repetition control, not building a complex ontology.

---

# 15. Research and reference policy

Before and during each production batch, consult good-quality writing and factual references so the corpus does not collapse into repetitive AI-style prose.

Research purposes:

- discover varied topics,
- observe natural article and story organization,
- verify factual ideas,
- improve descriptive variety,
- avoid repeatedly inventing the same scenarios.

Permanent workflow:

~~~text
research
-> understand topic and structure
-> design an original passage
-> write for the requested level
-> review originality and quality
~~~

Research is not permission to copy.

Do not copy paragraphs, lightly paraphrase one article, preserve distinctive source phrasing, reproduce copyrighted stories or make a passage that is effectively a sentence-by-sentence summary of one copyrighted article.

Prefer reputable educational or reference sources, public-domain material when literary examples are useful, factually stable subjects and sources appropriate to the target level.

The committed corpus must not depend on external links at runtime.

---

# 16. Anti-repetition system

The corpus is too large to rely on human memory alone.

Use automated similarity checks plus editorial review.

## 16.1 Exact passage duplicate

Normalize whitespace and case for comparison.

Any exact duplicate passage is a hard failure.

## 16.2 Exact sentence duplicate

Repeated substantial normalized sentences across the corpus are a hard failure unless the sentence is an unavoidable short common construction.

Recommended first threshold:

~~~text
8 or more words
~~~

## 16.3 Long phrase reuse

Flag repeated long token sequences.

Recommended first review trigger:

~~~text
8-token contiguous sequence reused in another passage
~~~

## 16.4 Passage similarity

Use a simple maintainable metric.

Recommended first implementation:

~~~text
normalized 5-gram sets
-> Jaccard similarity
~~~

Initial review thresholds:

~~~text
same level similarity >= 0.25
global corpus similarity >= 0.35
~~~

These are starting thresholds and should be calibrated against real pilot passages before becoming hard gates.

## 16.5 Repeated openings and endings

Track common openings and formulaic endings.

Examples to monitor:

~~~text
one morning
one day
after a long day
in a small town
at first
in the end
~~~

Do not require every story to end with a lesson or summary.

---

# 17. Runtime randomization for Vocabulary Shooter

Vocabulary order must never follow file order.

Use a shuffle bag per active source and level.

Algorithm:

~~~text
load active vocabulary
-> copy entry IDs to bag
-> Fisher-Yates shuffle
-> consume entries from shuffled bag
-> do not repeat an entry until the bag is exhausted
-> when exhausted, create a new shuffled bag
-> first item of the new bag must not equal the previous emitted item
~~~

This provides random visible order without repeated independent random draws that can return the same word again and again.

Apply the same principle to Custom vocabulary when compatible.

Changing source, level or custom dataset rebuilds the relevant bag.

All Shooter modes must ultimately receive randomized targets or randomized pools rather than source-file order.

---

# 18. Runtime randomization for Recall Typing

Recall uses the same shuffle-bag contract:

~~~text
load selected Class level or Custom set
-> Fisher-Yates shuffle
-> consume without replacement
-> reshuffle only after cycle completion
~~~

Do not create a cross-repository package only for shuffle logic. A small game-local helper is sufficient.

---

# 19. Random progress persistence

Preferred behavior is to keep shuffle progress during the browser session and persist it in localStorage only if the implementation stays simple.

Useful minimal persisted state:

~~~text
source
level
remaining IDs
last emitted ID
dataset version
~~~

If the dataset changes, discard stale bag state and rebuild.

Correct random non-repeating behavior is more important than persistence complexity.

---

# 20. Monkeytype feature model

Do not mix the new passage source with the existing EN-VN dictionary source.

Existing setting:

~~~text
Dictionary source
- Library
- Custom
~~~

New independent setting:

~~~text
Typing text source
- Custom Text
- Level Passages
~~~

When Level Passages is selected, show:

~~~text
Level
001 ... 100

Passages per session
1 ... 15
~~~

Recommended default:

~~~text
Level = last selected level, otherwise 001
Passages per session = 1
~~~

Persist these settings locally.

The EN-VN dictionary source remains independently configurable.

---

# 21. Monkeytype passage loading

Runtime:

~~~text
open Level Passages
-> fetch /typing-texts/index.json
-> select level
-> fetch only /typing-texts/levels/NNN.json
-> select passages from level shuffle bag
-> combine requested number of passages
-> pass resulting text into existing Monkeytype pipeline
~~~

Do not build a new typing engine.

Reuse existing Monkeytype rendering, input, WPM, accuracy, errors, results, EN-VN layer, Recall mode and pronunciation features.

This feature is a text-source layer.

---

# 22. Monkeytype passage randomization

Each level uses a passage shuffle bag.

For 15 passages:

~~~text
shuffle all passage IDs
-> consume 1-N based on Passages per session
-> do not reuse a passage until all passages have been consumed
-> reshuffle for the next cycle
~~~

If the remaining bag contains fewer passages than the requested session count:

1. use the remaining passages,
2. reshuffle a new cycle,
3. continue filling the session,
4. do not repeat the previous cycle's last passage at the boundary.

Within one session, the same passage must never appear twice.

Persist per-level progress only if it stays simple.

---

# 23. Combining multiple passages

If the user selects three passages, combine them into one Monkeytype test.

Preferred initial separator:

~~~text
one normal space
~~~

Do not inject headings, passage IDs, bullets or decorative separators into the typing text.

This keeps the result compatible with the strict character rules and existing Monkeytype text pipeline.

---

# 24. Passage count setting

Initial allowed range:

~~~text
1-15 passages
~~~

Approximate resulting session sizes:

~~~text
1 passage  -> 250-300 words
2 passages -> 500-600 words
3 passages -> 750-900 words
8 passages -> 2,000-2,400 words
10 passages -> 2,500-3,000 words
15 passages -> 3,750-4,500 words
~~~

This supports both short and long typing practice.

Do not restrict the UI to only one, two or three passages.

---

# 25. Production workflow for one level

A level is never complete immediately after generation.

Required loop:

~~~text
read vocabulary level
-> read CEFR profile
-> inspect existing corpus signatures
-> select balanced target vocabulary
-> research suitable topic/reference material
-> draft passage
-> run automatic checks
-> editorial self-review
-> fix all issues
-> run automatic checks again
-> repeat until PASS
-> continue next passage
-> after 15 passages run whole-level QA
-> fix level issues
-> rerun whole-level QA
-> level PASS
-> only then move to next level file
~~~

Permanent rule:

**Do not generate many level files first and review them later.**

---

# 26. Automatic passage validation

Each passage needs deterministic checks for at least:

- valid JSON/schema,
- valid passage ID,
- ID belongs to current level,
- unique passage ID,
- 250-300 word count,
- metadata wordCount matches actual count,
- 20-30 unique target words,
- every target exists in the vocabulary level,
- every target appears in the text,
- no forbidden characters,
- no forbidden typography,
- valid sentence capitalization,
- no repeated whitespace,
- no blank-line content,
- no exact duplicate passage,
- no substantial duplicate sentence,
- long phrase reuse report,
- similarity report.

Hard-rule failures are rejected before editorial QA.

---

# 27. Difficulty validation

Difficulty validation uses automation plus editorial judgment.

Useful automated signals:

- current or lower-level vocabulary coverage,
- unknown token ratio,
- average sentence length,
- longest sentence length,
- linking-word density,
- target vocabulary usage,
- CEFR references where available.

For lower levels, unexpected advanced language must be especially strict.

Do not automatically rewrite good prose because one heuristic score is unusual. Final level appropriateness remains an editorial gate.

---

# 28. Grammar and coherence review

Every passage must be read as prose after mechanical validation.

Check:

- grammar,
- tense consistency,
- pronoun clarity,
- logical sequence,
- passage focus,
- transitions,
- natural collocations,
- target-word usage,
- factual plausibility,
- ending quality,
- sentence rhythm.

A passage can pass JSON validation and still fail because it sounds unnatural.

---

# 29. Naturalness review

Explicitly look for bulk-generation problems:

- repetitive sentence length,
- excessive however, therefore or moreover,
- generic moral endings,
- fake inspirational language,
- repeated one day openings,
- repeated person-goes-somewhere scenarios,
- every passage using the same mini-story structure,
- unnecessary explanation of obvious facts,
- target vocabulary visibly inserted for quota,
- excessive adjective pairs,
- empty conclusions,
- repeated this shows that language,
- repeated in today's world openings.

If a passage feels dry, robotic or obviously generated, rewrite it before PASS.

---

# 30. QA scoring

Hard-rule categories are binary and must be perfect.

Recommended level QA:

| Category | Requirement |
| --- | ---: |
| Schema and structure | 10/10 |
| Character rules | 10/10 |
| Capitalization | 10/10 |
| Word-count rules | 10/10 |
| Target vocabulary validity | 10/10 |
| Vocabulary coverage | >= 9/10 |
| Level suitability | >= 9/10 |
| Grammar | >= 9.5/10 |
| Coherence | >= 9/10 |
| Naturalness | >= 9/10 |
| Topic and style diversity | >= 9/10 |
| Repetition control | >= 9/10 |
| Typing quality | 10/10 |

A high average cannot hide a hard-rule failure.

---

# 31. Whole-level QA

After all passages individually pass, review the level as a set.

Check:

- at least 15 passages,
- target vocabulary coverage distribution,
- no target-word domination,
- topic diversity,
- style diversity,
- signature diversity,
- sentence-opening diversity,
- passage-opening diversity,
- ending diversity,
- duplicate and similarity report,
- total word count,
- level difficulty consistency.

A file is PASS only after both individual passage QA and whole-level QA pass.

---

# 32. Cross-corpus QA

After each 30-file batch, scan every corpus file created so far for:

- duplicate passages,
- duplicate substantial sentences,
- long phrase reuse,
- similarity clusters,
- repeated topics and signatures,
- repeated opening formulas,
- repeated ending formulas,
- vocabulary coverage anomalies,
- malformed IDs,
- missing levels,
- stale index.

After Level 100, run the same checks across the complete corpus.

---

# 33. Batch production rule

Production batches:

~~~text
Batch 1 -> Levels 001-030
Batch 2 -> Levels 031-060
Batch 3 -> Levels 061-090
Batch 4 -> Levels 091-100
~~~

Do not generate all 100 files before review.

Each level inside a batch follows the full generation and QA loop before the next level begins.

---

# 34. Git safety workflow

When working in a local clone:

~~~text
complete Level N
-> passage QA PASS
-> whole-level QA PASS
-> local Git checkpoint commit
-> continue Level N+1
~~~

After the 30-file batch passes:

~~~text
run batch-wide QA
-> fix all failures
-> rerun batch-wide QA
-> update generated index
-> run project validation
-> push batch to GitHub
-> verify remote commit and CI
-> report one concise status line
-> immediately continue next batch
~~~

Required status style:

~~~text
Đã hoàn tất và push batch Level 001-030, toàn bộ QA PASS. Tiếp tục Level 031-060.
~~~

Do not wait for confirmation between successful batches unless the user explicitly asks to stop.

---

# 35. Changelog during production

Do not create hundreds of noisy changelog entries.

For each pushed batch, record:

- level range,
- passage count,
- approximate total words,
- QA result,
- similarity result,
- vocabulary coverage summary,
- important validator or policy changes,
- Git commit.

The corpus itself remains the detailed source of truth.

---

# 36. Research cadence

Before each 30-level batch:

1. prepare a broad topic and style pool appropriate to the CEFR range,
2. consult varied high-quality reference material,
3. identify overused themes from prior batches,
4. suppress those themes or signatures where necessary,
5. generate and review passages one level at a time,
6. perform extra research whenever target vocabulary suggests a topic that needs factual grounding.

Do not research hundreds of passages once and then write from one undifferentiated idea list.

---

# 37. Copyright and originality gate

The default corpus is original educational prose.

Hard requirements:

- no copied article paragraph,
- no copied story paragraph,
- no close sentence-by-sentence paraphrase,
- no distinctive source phrasing,
- no lyrics,
- no copyrighted fiction excerpts.

Even when public-domain literature is consulted, prefer learning from structure and style and writing a new passage.

---

# 38. Factual-content policy

Prefer stable factual subjects:

- science,
- nature,
- history,
- common technology concepts,
- ordinary social and practical knowledge.

Be cautious with rapidly changing facts such as current prices, current political office holders, active conflicts, short-lived statistics and current software details.

Timeless prose makes the local corpus useful longer.

Specific factual claims should be verified during production.

---

# 39. Sensitive vocabulary coverage

The shared vocabulary library contains legitimate slang and adult terms because it is a general learning library.

Typing passages do not need to force every such term into general educational prose.

A target may be recorded as a coverage exception when it is highly sexual, abusive, graphic, hateful or otherwise unsuitable for a normal passage.

Do not damage passage quality merely to reach mathematical 100 percent coverage.

---

# 40. Implementation phases

## Phase A - Shooter and Recall randomization

Vocabulary Shooter:

- standardize shuffle-bag selection,
- verify every mode receives randomized entries or pools,
- test cycle boundaries,
- test source and level changes.

Recall Typing:

- standardize shuffle-bag selection,
- test Class and Custom,
- test cycle boundaries.

Complete this first because it is independent of passage generation.

## Phase B - Shared typing-text contract

Parent platform:

- create shared/typing-texts,
- define schema,
- create index generator,
- create validator,
- expose the HTTP route in Dev and Play nginx,
- add CI validation.

Use a tiny temporary fixture while developing the contract.

Do not begin mass content production until the contract is stable.

## Phase C - Monkeytype Level Passages

Monkeytype:

- add Typing text source selector,
- add level selector,
- add Passages per session,
- load shared typing-text index,
- lazy-load selected level,
- implement passage shuffle bag,
- feed combined text into existing typing engine,
- persist settings,
- verify EN-VN Library and Recall mode compatibility.

## Phase D - Pilot content

Before 30-file production, build representative pilot levels such as:

~~~text
001
020
050
080
100
~~~

Use them to calibrate schema, validator, word count, difficulty rules, similarity thresholds, writing rules and Monkeytype runtime.

Weak pilot content must not be kept merely because the scripts work.

## Phase E - Production corpus

~~~text
001-030
-> review
-> batch QA
-> push

031-060
-> review
-> batch QA
-> push

061-090
-> review
-> batch QA
-> push

091-100
-> review
-> final corpus QA
-> push
~~~

## Phase F - Final integration review

Verify all 100 level files, 1,500 or more passages, index totals, random selection, passage-count settings, Shooter, Recall, Monkeytype performance, Dev mode, Play mode, offline behavior, CI and documentation.

---

# 41. Recommended scripts

Keep the workflow simple and explicit.

Recommended commands:

~~~text
pnpm typing-texts:generate
pnpm typing-texts:validate
pnpm typing-texts:validate-level --level 001
pnpm typing-texts:report
~~~

Possible scripts:

~~~text
scripts/generate-typing-text-index.mjs
scripts/validate-typing-texts.mjs
scripts/report-typing-text-coverage.mjs
~~~

Plain Node scripts are sufficient unless a real limitation appears.

---

# 42. CI gate

Normal CI validates committed content. It does not generate hundreds of passages.

CI should run:

~~~text
typing-text schema validation
typing-text index generation
git diff check
duplicate hard checks
forbidden-character checks
word-count checks
target-vocabulary checks
existing platform integration/build tests
~~~

Editorial generation and web research do not belong in normal CI.

---

# 43. Performance rule

Expected runtime:

~~~text
Monkeytype
-> typing-text index
-> one selected typing-text level

Shooter
-> vocabulary index
-> one selected vocabulary level

Recall
-> vocabulary index
-> one selected vocabulary level
~~~

No game should download the full 18,000-entry vocabulary plus all 1,500 passages just to start one session.

Do not add compression, caches or extra abstractions until measurement shows they are needed.

---

# 44. Testing requirements

## Shooter

Test:

- first cycle contains every entry once,
- no duplicate before cycle exhaustion,
- next cycle reshuffles,
- cycle boundary does not immediately repeat the final previous word,
- level switch resets correctly,
- Custom source works,
- all modes still start and finish correctly.

## Recall

Test the same shuffle guarantees for Class, Custom and level changes.

## Monkeytype

Test:

- index loading,
- all available levels in selector,
- selected level lazy loading,
- one, two, three and fifteen-passage sessions,
- no duplicate passage within a session,
- no repeat before bag exhaustion,
- cycle boundary,
- persisted level and passage-count settings,
- EN-VN Library matching,
- Recall typing compatibility,
- restart and new-test behavior,
- very long combined text,
- Dev build,
- static Play build.

---

# 45. Acceptance criteria

## Random vocabulary

- Shooter Class vocabulary never intentionally follows source-file order.
- Recall Class vocabulary never intentionally follows source-file order.
- both use non-repeating shuffled cycles,
- Custom datasets use the same behavior where compatible.

## Shared typing corpus

- Levels 001-100 exist.
- every level has at least 15 reviewed passages.
- every passage has 250-300 words.
- every passage has 20-30 valid target words.
- target words occur naturally in the passage.
- strict character and capitalization rules pass.
- duplicate and similarity review passes.
- every level passes passage QA and whole-level QA.

## Monkeytype

- user can choose Level Passages,
- user can choose Level 001-100,
- user can choose 1-15 passages per session,
- passages are randomized without premature repetition,
- multiple passages combine into one typing test,
- existing typing and result engine remains authoritative,
- EN-VN Library and Recall behavior remain compatible.

## Delivery

- each level is reviewed before the next,
- every 30-file batch receives batch-wide QA,
- batch is pushed only after PASS,
- user receives the concise completed-range message,
- production then continues automatically,
- final corpus receives complete cross-corpus QA.

---

# 46. Permanent rules for future AI or developers

Read this file before modifying this feature.

1. Git is the source of truth.
2. Runtime stays local and offline-first.
3. Shooter and Recall vocabulary order is randomized with no repetition before cycle exhaustion.
4. Monkeytype passage order is randomized with no repetition before cycle exhaustion.
5. Passage generation uses the current level vocabulary and the corresponding CEFR difficulty.
6. Every passage is 250-300 words and targets 20-30 level vocabulary entries.
7. Writing must be coherent, natural and varied rather than vocabulary filler.
8. Strict typing character and capitalization rules apply to every passage.
9. Research improves writing, but researched text is not copied or closely paraphrased.
10. Similarity and repetition are checked automatically and editorially.
11. A level file must PASS before the next level file is produced.
12. Production is checkpointed locally and pushed in 30-file batches.
13. After a successful batch push, report the completed range and continue automatically.
14. Never generate the whole corpus first and promise to review it later.
15. Do not over-engineer runtime or validation scripts.
