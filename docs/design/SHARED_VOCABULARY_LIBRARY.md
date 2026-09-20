# Shared Leveled Vocabulary Library

## Status

**Confirmed requirement and implemented baseline.**

The platform uses one shared English vocabulary library for Monkeytype, Vocabulary Shooter and Recall Typing.

There is no separate giant Monkeytype vocabulary file.

## Source of truth

The only editable source-of-truth data is:

~~~text
shared/vocabulary/levels/
  001.json
  002.json
  ...
  100.json
~~~

One level equals one JSON file.

The final library is expected to contain roughly 15,000-20,000 useful English words/phrases. The current committed dataset is the 450-entry reviewed foundation checkpoint, while the automated bulk pipeline is the approved path for expansion.

Current production batch:

~~~text
3 levels
150 entries per level
450 entries total
~~~

This is the first reviewed batch. The remaining levels must still be expanded gradually.

## Required entry shape

Every official library entry must have all four fields:

~~~json
{
  "id": "L003-025",
  "en": "cache",
  "vi": "bộ nhớ đệm",
  "ipa": "/kæʃ/"
}
~~~

Required:

~~~text
id
en
vi
ipa
~~~

An official level entry missing English, Vietnamese or IPA is invalid.

Phrases are supported as well as individual words.

Example:

~~~json
{
  "id": "L057-088",
  "en": "dependency injection",
  "vi": "tiêm phụ thuộc",
  "ipa": "/dɪˈpendənsi ɪnˈdʒekʃən/"
}
~~~

## Generated artifacts

The level files generate:

~~~text
shared/vocabulary/index.json
shared/vocabulary/lookup.json
~~~

These files are derived artifacts, not independent data sources.

### index.json

Contains:

- planned level count,
- currently available levels,
- total entries,
- level labels,
- file paths,
- entry counts.

Shooter and Recall use this file to build their level selector.

### lookup.json

Contains:

~~~text
normalized English word/phrase
→ level number
~~~

It also stores the maximum phrase word count.

Monkeytype uses this mapping to determine which level files are needed by the current Custom Text.

The lookup does not duplicate Vietnamese/IPA content.

## Generator and validator

Commands:

~~~bash
pnpm vocab:generate
pnpm vocab:validate
~~~

The validator rejects:

- invalid/missing level files within the populated level range,
- invalid level number,
- filename/level mismatch,
- duplicate level,
- empty level,
- missing id/en/vi/ipa,
- unsupported entry fields,
- malformed ID,
- ID prefix that does not belong to the current level,
- duplicate ID,
- duplicate normalized English word/phrase,
- IPA without /.../ delimiters,
- stale generated index/lookup artifacts.

CI also runs the generator and checks that it produces no Git diff.

## HTTP contract

The parent platform serves the shared files directly:

~~~text
https://typing-game.local/vocabulary/index.json
https://typing-game.local/vocabulary/lookup.json
https://typing-game.local/vocabulary/levels/001.json
...
~~~

Both Dev and Play nginx configurations expose the same contract.

CORS is enabled because the child games run on their own local subdomains.

The vocabulary data remains local/offline-first. No cloud vocabulary service is required.

## Vocabulary Shooter

Shooter now has:

~~~text
Vocabulary source

Class
Custom
~~~

### Class

~~~text
select Class
→ select a level
→ load only that level JSON
→ play with built-in vocabulary
~~~

The selected source and level are persisted locally.

Selecting Class applies that level immediately.

Changing the dropdown and pressing Use level applies the newly selected level.

### Custom

Custom keeps the existing IndexedDB vocabulary editor.

Switching between Class and Custom never overwrites the custom IndexedDB dataset.

Saving custom vocabulary switches the active source back to Custom.

## Recall Typing

Recall uses the same source model:

~~~text
Class
→ one selected shared level

Custom
→ existing IndexedDB vocabulary
~~~

The shared level entries already match Recall's canonical runtime shape:

~~~text
id
en
vi
ipa
~~~

Custom data is preserved when Class mode is used.

## Monkeytype

Monkeytype's EN-VN translation dictionary now has:

~~~text
Library
Custom
~~~

### Custom

Preserves the existing manually entered dictionary behavior.

### Library

The user does not select a level.

When the Custom Text form is submitted:

~~~text
current text
→ normalize English words/phrases
→ read lookup.json
→ determine required levels
→ fetch only those level files
→ cache a dictionary for the current text
→ existing EN-VN matching/Recall behavior uses that dictionary
~~~

This allows Monkeytype to treat all levels as one logical library without downloading every level file.

The existing greedy/longest phrase matching remains authoritative.

Pipe-delimited Custom Text is normalized before lookup as well.

## Performance rule

Do not fetch all 100 level files when only one or a few are needed.

~~~text
Shooter / Recall
→ index + selected level

Monkeytype
→ lookup + only levels referenced by current text
~~~

Level files can therefore grow independently while keeping normal game startup small.

## Data expansion rule

Before expanding to the final 15k-20k library:

1. keep the current schema stable,
2. populate level files in difficulty order,
3. require English + Vietnamese + IPA for every official entry,
4. run `pnpm vocab:generate`,
5. run `pnpm vocab:validate`,
6. resolve duplicates/invalid entries before commit.

Do not manually edit `index.json` or `lookup.json` as primary data.


---

## Production vocabulary policy

The 90-entry sample has now been replaced by the first production-quality batch:

~~~text
Level 001 -> 150 entries
Level 002 -> 150 entries
Level 003 -> 150 entries

450 entries total
~~~

These are the first reviewed foundation levels, not a signal to bulk-generate the remaining library.

### Difficulty model

Final level placement is not based on word length alone.

The review order is:

1. frequency in real English,
2. CEFR reference where available,
3. usefulness for a Vietnamese English learner,
4. spelling difficulty,
5. pronunciation difficulty,
6. abstractness,
7. technical/general usefulness and balance.

CEFR is a reference, not a one-to-one mapping to a single level.

The intended broad bands are:

~~~text
001-012  -> A1-heavy foundation
013-028  -> A2-heavy foundation
029-046  -> B1-heavy intermediate
047-065  -> B2-heavy upper intermediate
066-082  -> C1-heavy advanced
083-094  -> C2-heavy advanced
095-100  -> manually selected very advanced / abstract / technical / rare-but-useful
~~~

Frequency and usefulness can move an item earlier than its nominal CEFR band.
Spelling/pronunciation difficulty, abstractness and ambiguity can move it later.

Technical vocabulary is allowed, but it must be useful and balanced against general English.
It must not be used as filler.

### Pronunciation convention

Official library IPA is normalized around **General American** pronunciation.

The source pipeline primarily obtains pronunciations from CMUdict through the
thichhoc-dict dataset. A pronunciation is not accepted only because it exists.

Heteronyms require the intended part of speech/meaning to match the IPA.

The first production batch already needed manual corrections for cases such as:

~~~text
read  -> /rid/  for the verb "đọc"
live  -> /lɪv/  for the verb "sống"
close -> /kloʊz/ for the verb "đóng"
~~~

This is why bulk IPA import without review is prohibited.

## Approved source strategy

### English-Vietnamese + IPA + frequency candidates

Primary enrichment/candidate source:

~~~text
thichhoc-org/thichhoc-dict
~~~

Its data license is CC BY-SA 4.0.

Its own source chain includes WordNet 3.1, CMUdict, Wiktionary and wordfreq.
The project explicitly warns that not every Vietnamese sense has been human-reviewed,
therefore this platform treats it as a candidate source rather than unquestioned truth.

### CEFR reference

Difficulty reference:

~~~text
openlanguageprofiles/olp-en-cefrj
CEFR-J Vocabulary Profile 1.5
Octanove C1/C2 profile when advanced coverage is needed
~~~

CEFR-J permits research/commercial use with citation according to its published terms.
The Octanove C1/C2 profile is CC BY-SA 4.0.

### Attribution

User-readable attribution is stored at:

~~~text
shared/vocabulary/ATTRIBUTION.md
~~~

The Portal exposes a visible link to it.

The derived vocabulary dataset is distributed under CC BY-SA 4.0.
Application source code remains separately licensed.

## Scalable candidate workflow

Raw third-party source data is not committed into the platform repository.

Use a local ignored cache:

~~~text
.cache/vocabulary-sources/
~~~

Recommended source checkout:

~~~bash
mkdir -p .cache/vocabulary-sources

git clone --depth 1 \
  https://github.com/thichhoc-org/thichhoc-dict.git \
  .cache/vocabulary-sources/thichhoc-dict

git clone --depth 1 \
  https://github.com/openlanguageprofiles/olp-en-cefrj.git \
  .cache/vocabulary-sources/olp-en-cefrj
~~~

Then prepare review candidates:

~~~bash
pnpm vocab:candidates
~~~

Pipeline:

~~~text
source datasets
-> normalize English
-> group senses/POS/pronunciations
-> attach CEFR/frequency
-> calculate spelling/pronunciation heuristics
-> propose a rough level
-> output .cache/vocabulary-candidates.json
-> filter trusted provenance and pronunciation exceptions
-> pnpm vocab:build-library
-> pnpm vocab:validate
~~~

Important:

~~~text
vocab:candidates
NEVER writes official level files.
~~~

The candidate file is temporary review material only.

Unknown CEFR items do not receive a CEFR-derived final level in the candidate artifact.
The bulk builder estimates their relative placement from frequency plus spelling/pronunciation complexity.

## Schema hardening

The JSON Schema ID pattern was corrected so it now represents the same contract
as the JavaScript validator:

~~~text
Lxxx-xxx
~~~

The validator now also checks the critical schema contract itself so a broken
escaped regex cannot silently drift away from runtime validation again.

English entry text is additionally checked for NFKC/whitespace normalization.


### Candidate-tool CI guard

Platform CI syntax-checks the review-only candidate tool with:

~~~bash
node --check scripts/prepare-vocabulary-candidates.mjs
~~~

CI intentionally does not download or vendor the third-party source datasets.
Actual candidate generation remains an explicit local data-preparation step.


## Foundation density checkpoint

After the initial 300-entry review passed, Levels 001-003 were expanded to 150 entries each.

~~~text
Level 001 -> 150
Level 002 -> 150
Level 003 -> 150
total     -> 450
~~~

This density is closer to the long-term 15,000-20,000 / 100-level target while still keeping each change small enough for manual learner-quality review.

---

## Automated full-library production policy

The project no longer requires manual review of every vocabulary entry before promotion.
That approach does not scale to the intended 15,000-20,000 entry library.

The approved production flow is now:

~~~text
pinned trusted source revisions
-> normalize and join source records
-> reject weak provenance
-> flag pronunciation/heteronym exceptions
-> rank by frequency + CEFR + spelling/pronunciation difficulty
-> preserve the already-reviewed Levels 001-003
-> automatically distribute the remaining trusted entries across Levels 004-100
-> generate index.json + lookup.json
-> run structural validation
-> spot-check exceptions only
~~~

One command performs the full refresh:

~~~bash
pnpm vocab:refresh
~~~

It runs:

~~~text
vocab:sources
-> vocab:candidates
-> vocab:build-library
-> vocab:validate
~~~

Default target:

~~~text
18,000 entries
minimum acceptable trusted total: 15,000
planned levels: 100
~~~

The builder must never invent filler to hit the target. If the pinned sources cannot provide
at least the configured minimum after provenance/exception filtering, the build fails.

### Trusted automatic-promotion rule

An automatically promoted dictionary option must contain provenance for:

~~~text
CMUdict
+
WordNet or Wiktionary
~~~

CMUdict supplies the pronunciation chain. WordNet/Wiktionary supply lexical evidence.
Entries without this provenance are not automatically promoted.

Candidates with more than one trusted pronunciation are treated as heteronym/pronunciation
exceptions and skipped by the bulk builder. They can be handled separately when useful.
This keeps cases such as `read`, `live`, `close` and similar words from forcing manual review
of thousands of ordinary entries.

### Source revisions

`pnpm vocab:sources` checks out fixed upstream revisions under the ignored local cache:

~~~text
thichhoc-org/thichhoc-dict
4d6e92e8bcf8e3e762410c2b0a9f98fea8e62e5b

openlanguageprofiles/olp-en-cefrj
d4e45b75b38f27b30dfc5c44d8c571aec7e7092f
~~~

Pinning revisions makes the bulk build reproducible instead of silently changing when an
upstream repository changes.

### Level assignment

CEFR remains an anchor, not a requirement for every word.

- Candidates with CEFR data keep the existing proposed CEFR-band level.
- Candidates without CEFR are ranked automatically from frequency and spelling/pronunciation complexity.
- The trusted selected set is then ordered by estimated learning difficulty and distributed across Levels 004-100.
- Levels 001-003 remain preserved as the already-reviewed foundation checkpoint.

The default 18,000-entry target therefore produces roughly 180 entries per level overall,
while keeping the current 450 reviewed entries intact.

The automatic builder writes a local ignored report at:

~~~text
.cache/vocabulary-build-report.json
~~~

Manual QA is now exception-oriented and statistical/spot-check based, not a mandatory
word-by-word gate for the complete library.
