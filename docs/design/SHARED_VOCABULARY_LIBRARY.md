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

The final library is expected to grow to roughly 15,000-20,000 useful English words/phrases, but the current implementation intentionally contains only a small sample dataset while the pipeline is being validated.

Current sample:

~~~text
3 levels
30 entries per level
90 entries total
~~~

The sample is not the final vocabulary curriculum.

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
