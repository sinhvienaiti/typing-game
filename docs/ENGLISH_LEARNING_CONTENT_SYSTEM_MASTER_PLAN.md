# English Learning Content System — Master Plan

Status: FINAL PLAN v1 — architecture/taxonomy phase  
Repository: sinhvienaiti/typing-game  
Plan branch: feature/english-learning-content-system  
Baseline inspected: parent main 9edbba00bae3c66dca51e29a821f35c9c9a9c06c  
Date: 2026-10-02

## 0. Purpose and source-of-truth rules

This document is the implementation source of truth for expanding typing-game from a vocabulary-first typing platform into a reusable English-learning content platform covering vocabulary senses/usage, lexical patterns, grammar/usage, phrases, sentence corpora, exercises, translation and listening-oriented practice.

This plan supersedes the narrow grammar/content scope in docs/design/ENGLISH_TOPIC_CURRICULUM_PLAN.md only for the new rich learning-content architecture and the ~300-topic grammar/usage curriculum. The existing topic/POS/grammar indexes remain supported compatibility views until an explicit migration removes them.

Repository reality at the inspected baseline differs from older planning notes:

- there is no root PROCESS.md on current main;
- there is no shared/words/ tree;
- shared/vocabulary/levels/*.json is the current canonical 18,000-entry EN/VI/IPA library;
- the vocabulary level schema is version 1 and has additionalProperties=false, so rich fields MUST NOT be injected into those entries;
- shared/typing-texts/ already owns level-based long typing passages;
- shared/learning/ already owns parent-level mastery/review contracts for vocabulary, grammar and sentence entities;
- all five games are Git submodules and game-specific implementation stays in each child repository.

If future code/documents conflict with this file, prefer committed runtime contracts and newer explicitly marked source-of-truth docs, then update this plan in the same change. Conversation history is never a source of truth.

## 1. Goals

The system must:

1. preserve 100% backward compatibility with shared/vocabulary/levels/*.json v1 and existing consumers;
2. add sense-level meaning, POS, morphology, usage, register, word forms, preposition patterns and semantic relations without bloating the legacy vocabulary record;
3. support 300 high-quality grammar/usage learning topics across A1-C2, each with a distinct learning objective;
4. scale toward 500-1,000 verb patterns, 5,000+ collocations, 1,000+ phrasal verbs, 2,000+ idioms/chunks, 2,000+ common mistakes, 100,000+ example sentences, 20,000+ translation pairs, 30,000+ cloze exercises, 10,000+ transformations and 10,000+ dialogue examples;
5. let multiple games consume the same canonical content without maintaining competing copies;
6. separate rich authoring records from compact runtime views;
7. keep provenance/license metadata attached through import, normalization, derivation and publication;
8. make quality measurable and block publication when required checks fail;
9. support automation and batch generation without treating generated quantity as published quality;
10. remain local-first and efficient for static Play mode.

## 2. Non-goals for this phase

This phase does NOT:

- generate hundreds of thousands of final records;
- redesign the existing 18k vocabulary levels;
- copy proprietary Cambridge English Profile datasets into the repository;
- assume every child game must support every exercise type;
- move canonical mastery logic into child games;
- add a cloud database merely to host content;
- accept AI-generated sentences directly into published datasets without validation;
- use license-uncertain data just because it is technically downloadable;
- use a single giant JSON file for 100k+ sentence records;
- treat CEFR as an exact scientific score for every sentence.

## 3. Current-state analysis

### 3.1 Existing vocabulary

Current canonical runtime contract:

~~~
shared/vocabulary/
├── levels/001.json ... 100.json
├── schema.json
├── index.json
├── lookup.json
├── curriculum/
├── topics/
├── parts-of-speech/
├── grammar/
└── ATTRIBUTION.md
~~~

The 100 level files contain 18,000 total entries. Each official entry is deliberately small:

~~~json
{
  "id": "L001-001",
  "en": "good",
  "vi": "tốt; hay",
  "ipa": "/ɡʊd/"
}
~~~

This record is a typing target, not a dictionary lexeme. It cannot represent polysemy, multiple parts of speech, register, morphology or usage safely.

The existing curriculum/POS/grammar files are generated selection views over the vocabulary library. The current grammar index is a small signal-token taxonomy such as time.present, time.past, time.future, grammar.articles and grammar.prepositions. It is useful for selecting vocabulary, but it is not a full grammar-learning corpus.

### 3.2 Existing typing texts

shared/typing-texts/ already supplies leveled long passages. Existing consumers expect passage records with:

- id;
- topic;
- style;
- setting;
- tone;
- targetWords;
- wordCount;
- text.

This remains valuable for long-form typing and contextual exposure. New sentence/exercise corpora must reference or complement it, not replace it.

### 3.3 Existing shared learning system

The parent already owns:

- canonical Learning Profile;
- vocabulary/grammar/sentence learning entities;
- Smart Review;
- review priority/mastery;
- bounded review datasets;
- local IndexedDB persistence;
- cross-game event contracts.

This is the correct foundation. New content IDs must plug into it; the new content system must not create a second mastery engine.

### 3.4 Current child-game consumption

Monkeytype:
- loads shared vocabulary lazily by index/lookup/level;
- supports custom EN-VN dictionary display;
- has Learn, Recall and Listen paths;
- has Context/Cloze logic that currently derives exercises from typing passages and broad grammar signal tokens;
- already has a reusable SentenceBuilderExercise v1 with accepted answers, difficulty, distractors, hints and classified error answers;
- can emit vocabulary, grammar and sentence learning events;
- is the best first consumer for rich grammar/sentence activities.

Vocabulary Shooter:
- supports class/topic/word-type/grammar/custom vocabulary sources;
- grammar mode currently selects vocabulary around a broad grammar module, not true grammar exercises;
- emits vocabulary attempts only;
- is a good consumer for words, collocations, phrasal verbs and short chunks.

Recall Typing:
- consumes shared vocabulary;
- emits vocabulary attempts for typing/recall/listening;
- is a good consumer for headwords, phrases, collocations, phrasal verbs, short translations and listening recall.

Karaoke Typing:
- accepts vocabulary and sentence review items;
- emits word and sentence events;
- can become a strong sentence/listening/dialogue consumer;
- legacy sentence events may use sentence text as entityId, so authored shared content needs stable sentence IDs while retaining legacy-text compatibility.

Space Typing:
- consumes shared vocabulary and typing-text data;
- emits vocabulary typing/recall attempts;
- combat should stay fast, so grammar-heavy activities belong in bounded events, boss/challenge phases or contextual side activities rather than every enemy.

### 3.5 Exact inspected child-repository pins

These are the child commits actually referenced by the parent baseline inspected for this plan:

| Game | Commit |
|---|---|
| Monkeytype fork | 236f64ebf10c45d2859028aee71d12d2df407f4e |
| Vocabulary Shooter | 4618f3bcdeb5f72bde8e28587ae23d3567bdb05d |
| Recall Typing | 27ded35809c1d2e37eabc1a91c34b907b95c2219 |
| Karaoke Typing | d88d64f01e66fd41ed1eef1a4cf743b76bb0bbe3 |
| Space Typing | 0583b34552d00194012068ca4cbce497291e509e |

Future implementation sessions MUST re-read parent gitlinks before modifying a child. These pins are a review snapshot, not permanent branch names.

## 4. Architecture principles

### 4.1 Preserve the legacy vocabulary ABI

shared/vocabulary/levels/*.json v1 is an ABI-like contract. Do not add rich fields to it. Do not rename id/en/vi/ipa. Do not require child games to understand a new schema just to keep current modes working.

Rich data is joined by normalized headword/phrase keys and stable new content IDs.

### 4.2 Sidecar content graph, not one mega-record

A headword may map to many senses; a sense may map to many examples; a collocation can involve several lexemes; a sentence can exercise several grammar topics. Therefore the normalized model is relational/graph-like even though the runtime distribution uses static JSON.

The canonical relationships are IDs/references, not duplicated nested copies.

### 4.3 Authoring model and runtime model are different

Authoring records may be verbose and provenance-rich. Runtime files should be compact, sharded and purpose-specific.

Pipeline:

~~~
upstream/raw source
→ normalized candidates
→ authored/enriched records
→ validation/review
→ published canonical records
→ generated compact runtime indexes/shards
→ child-game adapters
~~~

### 4.4 Stable IDs are independent of display text and level files

Never use a level position such as L053-177 as the only identity of a sense or sentence. Level IDs can change if the trusted vocabulary is rebuilt.

New IDs are immutable once published. Text corrections increment revision/contentVersion rather than changing the ID.

Recommended namespaces:

- lexeme: lex.en.<stable-id>
- sense: sense.<source-or-project>.<stable-id>
- grammar: gr.<cefr>.<slug>
- pattern: pat.<stable-id>
- collocation: col.<stable-id>
- phrasal verb: pv.<stable-id>
- idiom: idiom.<stable-id>
- chunk: chunk.<stable-id>
- sentence: sent.<stable-id>
- dialogue: dlg.<stable-id>
- exercise: ex.<type>.<stable-id>
- mistake: err.<stable-id>

IDs are allocated once by tooling. Do not derive the primary ID from the full text hash because editing a typo must not create a new learning entity.

### 4.5 Canonical normalization

For compatibility with existing learning keys:

- Unicode normalize NFKC for lookup keys;
- trim;
- collapse whitespace;
- lowercase with en-US semantics for English lookup;
- preserve original display text separately;
- do not remove meaningful apostrophes/hyphens from canonical lexical identity;
- sentence text uses NFC for presentation and a separate normalized dedup key.

## 5. Proposed repository layout

The current shared/vocabulary and shared/typing-texts trees stay in place.

Target architecture:

~~~
shared/
├── vocabulary/                     # EXISTING; unchanged v1 ABI
│   ├── levels/
│   ├── curriculum/
│   ├── topics/
│   ├── parts-of-speech/
│   └── grammar/
├── typing-texts/                   # EXISTING long-form passages
├── dictionary/                     # NEW lexical enrichment sidecars
│   ├── manifest.json
│   ├── senses/
│   ├── morphology/
│   ├── usage/
│   ├── relations/
│   ├── collocations/
│   ├── verb-patterns/
│   └── prepositions/
├── phrases/                        # NEW multiword lexical units
│   ├── manifest.json
│   ├── phrasal-verbs/
│   ├── idioms/
│   └── chunks/
├── grammar/                        # NEW real learning curriculum/content
│   ├── manifest.json
│   ├── topics/
│   ├── patterns/
│   └── examples/
├── sentences/                      # NEW reusable sentence/exercise corpus
│   ├── manifest.json
│   ├── examples/
│   ├── translation/
│   ├── dialogues/
│   ├── cloze/
│   ├── correction/
│   ├── transformation/
│   ├── building/
│   └── listening/
├── curriculum/                     # NEW A1-C2 learning sequences
│   ├── manifest.json
│   ├── a1.json
│   ├── a2.json
│   ├── b1.json
│   ├── b2.json
│   ├── c1.json
│   └── c2.json
├── schemas/                        # shared JSON schemas/common definitions
│   └── english-content/
└── attribution/                    # generated human/machine attribution views
    └── english-content/

content/
└── english/                        # NEW authoring/import workspace
    ├── sources/                    # manifests/checksums; raw bulk downloads ignored
    ├── dictionary/
    ├── phrases/
    ├── grammar/
    ├── sentences/
    └── review-queues/
~~~

Rules:

- content/english is canonical authoring material and source manifests.
- Large third-party raw downloads are NOT committed unless explicitly justified; source URL/version/checksum/import recipe is committed.
- shared/* contains validated publishable runtime artifacts.
- generated indexes are deterministic and reproducible.
- no child repo gets its own giant copy.

## 6. Sharding and scale

100k+ sentences must not be a single JSON file.

Recommended default:

- sentence shards: CEFR/type + deterministic bucket, roughly 500-1,000 records per shard;
- dictionary sidecars: 256 deterministic hash-prefix buckets or equivalent indexed shards;
- phrases/collocations: type + CEFR + deterministic shard;
- grammar topics: one topic file is acceptable because there are only ~300 topics, but examples/exercises are referenced in sentence shards;
- every dataset has a compact manifest with version, counts, shard paths, checksums and license mix.

Runtime manifest example:

~~~json
{
  "schemaVersion": 1,
  "contentVersion": "2026.10.0",
  "dataset": "sentences.examples",
  "count": 12540,
  "shards": [
    {
      "id": "a2-00",
      "path": "examples/a2/00.json",
      "count": 742,
      "bytes": 683421,
      "sha256": "..."
    }
  ]
}
~~~

Target shard guideline: normally 0.5-2 MB uncompressed. Measure actual browser/network performance before locking a hard limit.

## 7. Core schemas


### 7.0 Schema catalog and contract rules

Phase E01 must implement JSON Schema Draft 2020-12 contracts, not ad-hoc TypeScript-only validation.

Planned schema files:

~~~
shared/schemas/english-content/
├── common.schema.json
├── provenance.schema.json
├── source-manifest.schema.json
├── lexeme.schema.json
├── sense.schema.json
├── morphology.schema.json
├── usage.schema.json
├── collocation.schema.json
├── verb-pattern.schema.json
├── phrase.schema.json
├── grammar-topic.schema.json
├── sentence.schema.json
├── translation-pair.schema.json
├── dialogue.schema.json
├── exercise.schema.json
├── common-mistake.schema.json
├── curriculum.schema.json
└── runtime-manifest.schema.json
~~~

Contract rules:

- schemas use Draft 2020-12 and stable $id values under the project namespace;
- published canonical records use additionalProperties=false unless a deliberately open metadata extension object is defined;
- draft/import records may carry a dedicated extensions/raw object rather than leaking unknown fields into published records;
- all IDs validate against type-specific patterns;
- all CEFR values use one enum: A1, A2, B1, B2, C1, C2;
- license identifiers use SPDX-style IDs where a suitable identifier exists, plus a controlled LicenseRef value for project-original/uncleared material;
- provenance is required for imported/derived content;
- quality state is required for anything entering the publication pipeline;
- cross-file references are validated semantically after JSON Schema validation;
- schema files define structure; business rules such as "a cloze blank must resolve to its target" belong in semantic validators;
- runtime compact views may have separate schemas from canonical authoring records, but the generator is the only supported bridge between them.

This plan intentionally specifies record contracts rather than freezing every final JSON property before E01 pilots. E01 must convert these contracts into executable schemas before any large batch is generated.

### 7.1 Provenance object

Every imported/derived record that contains third-party facts/text must retain provenance.

~~~json
{
  "source": {
    "dataset": "oewn",
    "sourceId": "oewn-...",
    "sourceUrl": "https://en-word.net/",
    "snapshot": "YYYY-MM-DD",
    "license": "CC-BY-4.0",
    "attribution": "Open English WordNet contributors",
    "modified": true
  }
}
~~~

For composite records, use sources[] and field-level provenance when fields have materially different origins.

### 7.2 Lexeme/sense record

~~~json
{
  "schemaVersion": 1,
  "id": "lex.en.00012345",
  "headword": "run",
  "headwordKey": "run",
  "legacyVocabularyRefs": ["run"],
  "partsOfSpeech": ["verb", "noun"],
  "senseIds": ["sense.oewn...."],
  "forms": ["runs", "running", "ran"],
  "cefr": {
    "overall": "A2",
    "method": "curated-reference",
    "confidence": 0.86
  },
  "usageRefs": ["usage.0001"],
  "quality": {
    "state": "published",
    "checks": {}
  }
}
~~~

Sense records separately carry:

- sense ID;
- lexeme/headword reference;
- POS;
- concise English definition;
- Vietnamese gloss/explanation;
- semantic relations;
- usage labels;
- register;
- region;
- sense-level CEFR when available/curated;
- examples by ID;
- provenance.

Do not pretend a single Vietnamese string covers all senses.

### 7.3 Morphology record

Fields:

- lemma/headwordKey;
- POS;
- inflected forms;
- irregularity;
- comparative/superlative where relevant;
- countability/plural;
- verb forms;
- derivational family references;
- pronunciation variants only if source/license supports them;
- source/provenance.

### 7.4 Usage record

Fields:

- id;
- target lexeme/sense/phrase;
- register: neutral/formal/informal/spoken/written/academic/business/etc.;
- region if material;
- construction/pattern;
- Vietnamese explanation;
- positive guidance;
- avoid/mistake notes;
- contrast refs;
- example refs;
- source/provenance;
- quality.

### 7.5 Collocation record

~~~json
{
  "schemaVersion": 1,
  "id": "col.00001234",
  "text": "make a decision",
  "headwordKeys": ["make", "decision"],
  "pattern": "V + DET + N",
  "meaningVi": "đưa ra quyết định",
  "cefr": "B1",
  "register": ["neutral"],
  "exampleIds": ["sent.000..."],
  "evidence": {
    "kind": "curated",
    "score": null
  }
}
~~~

Do not manufacture a numeric frequency score unless it comes from a documented corpus/calculation. Keep "curated", "source-attested" and "frequency-measured" distinct.

### 7.6 Verb-pattern record

Fields:

- id;
- lemma;
- senseRef when pattern is sense-dependent;
- frame: V + to-inf, V + -ing, V + object + to-inf, V + that-clause, etc.;
- argument roles when source supports them;
- restrictions;
- meaning difference;
- Vietnamese explanation;
- contrast patterns;
- examples;
- CEFR;
- provenance.

VerbNet classes/frames can inform candidates, but published records require licensing clearance and pedagogical normalization.

### 7.7 Phrase record

Common base for phrasal verbs, idioms and chunks:

- id/type;
- canonical text;
- normalized key;
- headword/particle references;
- meanings as separate senses;
- separability/transitivity for phrasal verbs;
- literal/idiomatic flag;
- register;
- CEFR;
- Vietnamese explanation;
- examples;
- common mistakes;
- variants;
- provenance;
- quality.

### 7.8 Grammar topic record

Every published grammar/usage topic must support the requested lesson dimensions, but fields can be optional during draft state.

~~~json
{
  "schemaVersion": 1,
  "id": "gr.a2.present-perfect-experience",
  "cefr": "A2",
  "title": "Present Perfect: life experience",
  "objective": "Talk about experience without a finished past time.",
  "concept": {
    "en": "...",
    "vi": "..."
  },
  "formulae": [],
  "whenToUse": [],
  "forms": {
    "positive": [],
    "negative": [],
    "question": []
  },
  "variations": [],
  "relatedCollocationIds": [],
  "exampleIds": [],
  "commonMistakeIds": [],
  "contrastTopicIds": [],
  "dialogueIds": [],
  "contextExampleIds": {
    "dailyLife": [],
    "work": [],
    "travel": []
  },
  "exerciseRefs": {
    "cloze": [],
    "correction": [],
    "building": [],
    "translation": [],
    "transformation": []
  },
  "prerequisiteIds": [],
  "quality": {}
}
~~~

### 7.9 Sentence record

A sentence is reusable content, not an exercise by itself.

Fields:

- immutable sentenceId;
- English text;
- optional Vietnamese translation refs;
- CEFR;
- context/domain;
- register;
- target grammar IDs;
- target lexeme/sense/phrase IDs;
- tokens/annotations generated at build time;
- attribution/provenance;
- quality;
- revision.

Keep source sentence and project-authored adaptation as separate records when license/provenance differs.

### 7.10 Translation-pair record

Fields:

- id;
- sourceLanguage/targetLanguage;
- sourceText/targetText;
- acceptedAlternatives[];
- literalHint optional;
- grammar/lexical targets;
- direction permissions;
- CEFR;
- register;
- provenance;
- quality.

For VI→EN exercises, acceptedAlternatives are important. Do not mark a natural equivalent wrong merely because it differs from one reference sentence.

### 7.11 Exercise record

Use a common envelope plus type-specific payload.

Types:

- cloze;
- error-correction;
- sentence-building;
- translation;
- transformation;
- listening-typing;
- contextual-usage;
- collocation;
- grammar-typing.

Common fields:

- exerciseId;
- type;
- prompt;
- target entity IDs;
- source sentence/dialogue IDs;
- accepted answers;
- classified common wrong answers when known;
- hint policy;
- difficulty;
- CEFR;
- explanation refs;
- quality.

Monkeytype SentenceBuilderExercise v1 should be adapted from this canonical record rather than becoming the canonical storage schema itself.

### 7.12 Common mistake record

Fields:

- id;
- incorrect pattern/example;
- corrected form(s);
- Vietnamese explanation;
- grammar/lexical target refs;
- error type;
- scope;
- evidence type: pedagogical | source-attested | observed-local;
- frequency only when measured;
- examples;
- quality.

Never invent learner-frequency claims. "Common mistake" can mean pedagogically high-risk even when no numeric corpus frequency is available, but the evidence type must say so.

## 8. Quality metadata and publication states

Do not use five booleans that imply more certainty than the process can provide.

Recommended:

~~~json
{
  "quality": {
    "state": "reviewed",
    "checks": {
      "schema": {"status": "pass", "method": "validator-v1"},
      "grammar": {"status": "pass", "method": "rules+review"},
      "translation": {"status": "pass", "method": "bilingual-review"},
      "exactDuplicate": {"status": "pass", "method": "canonical-hash-v1"},
      "nearDuplicate": {"status": "pass", "method": "minhash-v1"},
      "naturalness": {"status": "pass", "method": "review"},
      "cefr": {"status": "pass", "method": "heuristic+review"},
      "targetPresence": {"status": "pass", "method": "structure-detector-v1"}
    }
  }
}
~~~

Lifecycle:

candidate → draft → validated → reviewed → published → deprecated

Only published content ships in normal game manifests. Draft/review queues never silently leak into runtime.

## 9. Source and license strategy

This section is an engineering strategy, not legal advice. Every importer must pin the exact upstream terms/snapshot used.


### 9.0 Source-to-content coverage and publication policy

| Source | Primary use | Can directly publish derived data? | Required handling |
|---|---|---|---|
| Open English WordNet | senses, definitions, POS, semantic relations | Yes, subject to CC BY 4.0 | attribution, source IDs, modification notice |
| Wiktionary via Wiktextract/Kaikki | IPA, forms, morphology, usage, phrases | Yes only under applicable Wiktionary terms | preserve CC BY-SA/GFDL provenance; isolate license-aware derivatives |
| Tatoeba | supplementary sentences/translation pairs | Yes when record license permits | retain sentence/source attribution; filter quality; treat audio separately |
| VerbNet | verb classes/frames/pattern discovery | NO by default in this plan | publication gate stays closed until exact version rights are verified |
| Cambridge EGP/EVP | taxonomy/CEFR reference | No copying into repo | reference manually; do not scrape/redistribute proprietary entries/examples |
| Current shared vocabulary | legacy EN/VI/IPA targets | Already published under existing attribution | do not change its license or schema through this project |
| Project-authored content | Vietnamese explanation, lessons, controlled examples, exercises | Yes after owner/license policy + QA | mark PROJECT-ORIGINAL/LicenseRef until explicit distribution license is chosen |

Coverage gaps are expected. No external source above provides the whole requested system. In particular, high-quality Vietnamese explanations, controlled grammar lessons, common mistakes, accepted-answer sets, transformations, sentence-building tasks and game-specific contextual practice are primarily project-authored datasets.


### 9.1 Open English WordNet

Use for:

- senses;
- definitions;
- synonyms;
- semantic relations;
- POS;
- lexical network structure.

Current official site states Open English WordNet is CC BY 4.0:
https://en-word.net/

Requirements:

- retain attribution and source IDs;
- mark modifications;
- do not collapse several synsets into one Vietnamese sense without review.

### 9.2 Wiktionary / Wiktextract / Kaikki

Wiktextract software is MIT, but that is NOT the license of extracted Wiktionary content. English Wiktionary text is distributed under CC BY-SA 4.0 and GFDL terms. Kaikki/Wiktextract extracts inherit the source-content obligations.

Use for:

- IPA/pronunciation metadata;
- morphology/forms;
- POS;
- usage/register labels;
- phrase and phrasal-verb candidates;
- linguistic notes.

Requirements:

- isolate source-derived data in provenance-aware records;
- preserve attribution and ShareAlike obligations for redistributed derivatives;
- do not mix license metadata away during normalization;
- separately review media/audio licenses; dictionary text license does not automatically cover every media asset.

References:
https://github.com/tatuylonen/wiktextract
https://en.wiktionary.org/wiki/Wiktionary:Copyrights
https://kaikki.org/

### 9.3 Tatoeba

Use as supplementary examples/translation pairs, not as the only quality source.

Tatoeba text downloads are generally CC BY 2.0 FR, while a subset is CC0. Translations and audio can have additional derivative/license constraints.

Requirements:

- retain sentence ID, author/attribution data when required, license and source;
- prefer CC0 records when they satisfy the task and quality target;
- exclude records marked with licensing issues;
- do not assume audio has the same license as sentence text;
- filter unnatural, incorrect, archaic or context-poor examples;
- avoid importing merely because a pair exists.

References:
https://tatoeba.org/en/downloads
https://en.wiki.tatoeba.org/articles/show/using-the-tatoeba-corpus

### 9.4 VerbNet

Use for:

- verb-class candidates;
- syntax frames;
- argument structures;
- pattern discovery.

Important license gate: current common distributions describe VerbNet as "distributed with permission of the author", which is not enough to assume unrestricted redistribution of derived bulk data. The University of Colorado repository does not currently expose a simple root open-data license.

Therefore:

- do not bulk-copy VerbNet frames into published shared data until exact redistribution terms for the chosen version are verified;
- it may be used as a development/reference input where permitted;
- independently authored pedagogical verb-pattern records can be created from linguistic analysis without copying protected expression, but provenance and derivation must be reviewed;
- importer must have a hard ALLOW_PUBLISH flag controlled by a source manifest.

References:
https://github.com/cu-clear/verbnet
https://verbs.colorado.edu/verbnet/

### 9.5 Cambridge English Grammar Profile / English Vocabulary Profile

Reference only.

Use for:

- taxonomy sanity checks;
- CEFR calibration concepts;
- coverage-gap review.

Do NOT:

- scrape/copy the proprietary database into the repo;
- copy Cambridge definitions/examples/entries;
- advertise the project as officially "English Profile informed" without permission;
- treat free online access as redistribution permission.

References:
https://englishprofile.org/?menu=english-grammar-profile
https://englishprofile.org/?menu=english-vocabulary-profile
and their Terms of Use.

### 9.6 Existing vocabulary sources

shared/vocabulary/ATTRIBUTION.md remains authoritative for the current 18k dataset, which is distributed as a CC BY-SA 4.0 derived dataset.

The new content system must not weaken or hide that attribution.

### 9.7 Project-authored content

Original Vietnamese explanations, controlled examples, lesson text, exercises and corrections must be marked PROJECT-ORIGINAL with authoring/review metadata until the repository owner explicitly chooses a redistribution license for that dataset.

If an open content license is chosen later, store it per dataset manifest. Do not infer a license merely because the GitHub repo is public.

### 9.8 License partitions

Each runtime shard declares its license mix. Prefer homogeneous-license shards where practical.

A build must fail if:

- a source-required attribution is missing;
- license is unknown;
- a record is marked nonredistributable;
- a ShareAlike-derived record is placed in a manifest claiming incompatible terms;
- a Tatoeba sentence requiring attribution has lost its source identity.

## 10. Vocabulary enrichment architecture

The existing level entry remains the simple learning target. Rich lookup works as:

~~~
legacy word/phrase key
→ dictionary index bucket
→ lexeme record
→ sense(s)
→ morphology / usage / collocations / verb patterns
→ example sentence IDs
→ exercise IDs
~~~

Key decisions:

- lexeme != sense;
- phrase != arbitrary multiword vocabulary level entry;
- POS belongs at lexeme/sense level, not as a single guessed field on the old entry;
- Vietnamese meanings are sense-specific in the new layer;
- current vi stays as the compact legacy gloss;
- current ipa stays compatibility pronunciation; richer pronunciation variants live in sidecars;
- joins use normalized key plus explicit IDs, never array position.

## 11. Collocations

Long-term target: 5,000+ validated records.

Categories include:

- adjective + noun;
- noun + noun;
- verb + noun;
- noun + verb;
- adverb + adjective;
- verb + adverb;
- adjective + preposition;
- noun + preposition;
- verb + preposition;
- light-verb collocations;
- fixed grammatical collocations.

Generation strategy:

1. collect source-attested candidates where licensing permits;
2. generate candidate combinations only as a proposal stage;
3. verify idiomatic naturalness;
4. verify meaning/register;
5. attach at least one natural example before publication;
6. deduplicate morphological variants when the learning target is the same;
7. keep meaningful variants when syntax/register differs.

Never publish "possible English combinations" as collocations without evidence/review.

## 12. Verb patterns and prepositions

Long-term target: 500-1,000 verb-pattern records.

Pattern taxonomy:

- V + to-inf;
- V + -ing;
- V + object + to-inf;
- V + object + bare infinitive;
- V + that-clause;
- V + wh-clause;
- V + whether/if-clause;
- V + preposition + noun/-ing;
- V + object + preposition + noun/-ing;
- linking/resultative/causative patterns;
- passive-compatible variants;
- sense-dependent alternations.

Each pattern should answer:

- what structure is licensed;
- what it means;
- whether object is required;
- whether passive is possible;
- common preposition;
- meaning changes vs another pattern;
- one or more natural examples;
- one high-value learner error where applicable.

## 13. Phrasal verbs

Long-term target: 1,000+.

Metadata must include:

- verb + particle(s);
- sense-specific meaning;
- transitive/intransitive;
- separable/inseparable;
- pronoun object rule;
- register;
- literal vs idiomatic;
- CEFR estimate;
- examples and Vietnamese explanation.

"take off" as aircraft departure and "take off" as remove clothing are different senses, even though the phrase key is identical.

## 14. Idioms and chunks

Long-term target: 2,000+.

Chunks include:

- conversational frames;
- discourse chunks;
- formulaic requests;
- academic/work chunks;
- travel/service chunks;
- stance frames;
- fixed/semi-fixed sequences.

Do not teach rare colorful idioms ahead of high-frequency functional chunks merely to increase count.

## 15. Sentence corpus

### 15.1 Long-term targets

- examples: 100,000+;
- translation pairs: 20,000+;
- dialogues: 10,000+;
- cloze: 30,000+;
- transformations: 10,000+;
- plus correction/building/listening records as coverage requires.

### 15.2 Sentence design requirements

Each published controlled example should:

- sound like plausible modern English;
- contain the claimed target structure;
- stay within the intended CEFR vocabulary/syntax envelope where possible;
- avoid bizarre named entities and unnecessary cultural assumptions;
- have enough context for ambiguous grammar/sense;
- avoid templates that produce robotic repetitive wording;
- represent daily life, work, travel and general communication across the corpus;
- carry register/context labels.

### 15.3 Dialogues

A dialogue record is a sequence of turns, not concatenated independent sentences.

Fields include:

- dialogue ID;
- scenario;
- speakers with neutral labels;
- turns;
- target grammar/lexical IDs;
- CEFR;
- register;
- optional audio/TTS plan;
- translation refs;
- quality/provenance.

### 15.4 Listening

Phase 1 listening can use browser/system TTS for project-authored text where existing game architecture permits. TTS voice metadata is runtime configuration, not a license claim about source audio.

If third-party audio is added later:

- store audio license per asset;
- link audio to exact sentence revision;
- do not assume Tatoeba audio is reusable because the text is reusable;
- validate duration, clipping, pronunciation and transcript match.

## 16. Exercise system

### 16.1 Cloze

Cloze can be authored or derived, but derived records must pass target-presence and ambiguity checks.

A blank must have:

- a pedagogical target;
- sufficient context;
- accepted alternatives when more than one answer is natural;
- a reason why distractors are wrong.

Current Monkeytype auto-cloze from broad signal tokens is useful as a fallback/pilot, not the final 30k curated corpus.

### 16.2 Error correction

Record:

- incorrect sentence;
- corrected answers;
- error span;
- error taxonomy;
- explanation in Vietnamese;
- target topic;
- optional plausible distractor reasoning.

Avoid errors that native speakers would accept as a legitimate dialect/register variant.

### 16.3 Sentence transformation

Types:

- tense/aspect rewrite;
- active/passive;
- direct/reported speech;
- conditional/wish;
- relative/reduced clause;
- comparison;
- modality;
- register rewrite;
- emphasis/cleft;
- clause-to-phrase/phrase-to-clause.

Require meaning-preservation metadata and accepted alternatives.

### 16.4 Sentence building

Reuse Monkeytype's successful concepts:

- acceptedAnswers;
- difficulty;
- distractors;
- grammarHint;
- classifiedAnswers.

Canonical shared records should be game-neutral. Monkey adapter converts to SentenceBuilderExercise v1.

### 16.5 Translation

Primary practice direction for this project:

Vietnamese prompt → English production.

Also support English → Vietnamese comprehension where useful.

Do not grade VI→EN with exact string equality only. Normalize punctuation/case where appropriate and allow curated equivalents.

### 16.6 Contextual usage

Give a mini-scenario and require the learner to choose/type an expression that matches:

- meaning;
- register;
- grammar;
- collocation;
- social context.

This is essential at B2-C2, where "grammatically possible" is not enough.

## 17. CEFR model

CEFR is stored at several levels:

- curriculum topic level;
- lexeme/sense/phrase estimate;
- sentence estimate;
- exercise difficulty;
- vocabulary legacy level mapping.

Do not collapse them into one global score.

CEFR assignment inputs may include:

- existing project vocabulary level mapping;
- CEFR-J reference already used by the vocabulary pipeline;
- Cambridge EGP/EVP as non-copied reference;
- structure prerequisites;
- sentence length/embedding/clause complexity;
- lexical coverage;
- manual pedagogical review.

Store method/confidence. A heuristic estimate is not the same as an externally validated CEFR label.

## 18. Full 300-topic grammar/usage curriculum

Rules:

- exact target: 300 topics;
- distribution: A1 45, A2 50, B1 60, B2 60, C1 50, C2 35;
- each topic below has its own learning objective;
- related topics may share examples but must not duplicate the same objective;
- IDs remain stable after publication;
- topic content must later satisfy the lesson dimensions in section 7.8.

### A1 — 45 topics

| ID | Topic | Learning objective |
|---|---|---|
| gr.a1.be-identification-description | Be: identification and description | Use am/is/are to identify people/things and give simple descriptions. |
| gr.a1.be-negative | Be: negatives | Make negative statements with am not/isn't/aren't. |
| gr.a1.be-questions-short-answers | Be: yes/no questions and short answers | Ask and answer basic yes/no questions with be. |
| gr.a1.subject-pronouns | Subject pronouns | Choose I/you/he/she/it/we/they correctly as subjects. |
| gr.a1.possessive-adjectives | Possessive adjectives | Use my/your/his/her/its/our/their before nouns. |
| gr.a1.demonstratives | This/that/these/those | Choose demonstratives for singular/plural and near/far reference. |
| gr.a1.there-is-are | There is / there are | Introduce the existence and location of people and things. |
| gr.a1.articles-a-an | A/an for classification and first mention | Use a/an with singular count nouns for non-specific reference. |
| gr.a1.article-the-basic | The for basic specific reference | Use the when speaker and listener can identify the referent. |
| gr.a1.noun-number | Singular and plural nouns | Form regular plurals and high-frequency irregular plurals. |
| gr.a1.countability-basic | Countable and uncountable nouns: basics | Distinguish common count and mass nouns in simple contexts. |
| gr.a1.some-any-basic | Some and any: basics | Use some and any in simple affirmative, negative and question contexts. |
| gr.a1.have-possession | Have/has for possession | Express possession and basic relationships with have/has. |
| gr.a1.possessive-s | Possessive 's | Show ownership and relationships with noun + 's. |
| gr.a1.present-simple-routines | Present Simple: habits and routines | Describe repeated everyday actions and routines. |
| gr.a1.present-simple-facts-states | Present Simple: facts and states | Describe general truths, stable situations and common states. |
| gr.a1.present-simple-third-person | Present Simple: third-person -s | Form he/she/it verb forms accurately. |
| gr.a1.present-simple-negative | Present Simple: negatives | Use don't/doesn't + base verb. |
| gr.a1.present-simple-questions | Present Simple: yes/no questions | Form Do/Does questions and short answers. |
| gr.a1.wh-questions-present | Present Simple: wh- questions | Ask for basic information with who/what/where/when/why/how. |
| gr.a1.frequency-adverbs | Adverbs of frequency | Place always/usually/often/sometimes/never naturally. |
| gr.a1.can-ability | Can/can't: ability | Talk about present ability and inability. |
| gr.a1.can-permission-requests | Can: permission and simple requests | Ask for permission and make simple requests with can. |
| gr.a1.imperatives | Imperatives and instructions | Give simple commands, directions and instructions. |
| gr.a1.object-pronouns | Object pronouns | Use me/you/him/her/it/us/them after verbs and prepositions. |
| gr.a1.likes-gerund-noun | Like/love/hate + noun or -ing | Express preferences with nouns and common -ing forms. |
| gr.a1.want-need-infinitive | Want/need + noun or to-infinitive | Express wants and needs with common complement patterns. |
| gr.a1.time-prepositions | At/on/in for time | Choose basic time prepositions for clock times, days and periods. |
| gr.a1.place-prepositions | At/in/on for place | Choose basic place prepositions for points, spaces and surfaces. |
| gr.a1.movement-prepositions | Basic movement prepositions | Use to/from/into/out of/across for simple movement. |
| gr.a1.adjective-position | Basic adjective position | Use adjectives before nouns and after be. |
| gr.a1.degree-very-really | Very/really + adjective | Modify basic adjectives with common degree adverbs. |
| gr.a1.coordinators | And, but and or | Join words and simple clauses with basic coordinators. |
| gr.a1.because-basic | Because for simple reasons | Give a direct reason with because. |
| gr.a1.present-continuous-now | Present Continuous: actions happening now | Describe actions in progress at the speaking moment. |
| gr.a1.present-continuous-temporary | Present Continuous: temporary situations | Describe short-term situations around now. |
| gr.a1.present-simple-vs-continuous | Present Simple vs Present Continuous: basic contrast | Choose routine/state vs action-in-progress meanings. |
| gr.a1.past-be | Was/were | Describe past states, identity and location. |
| gr.a1.past-simple-regular | Past Simple: regular verbs | Form and use regular past verbs for finished events. |
| gr.a1.past-simple-irregular | Past Simple: common irregular verbs | Use high-frequency irregular past forms in finished events. |
| gr.a1.past-simple-negative-question | Past Simple: negatives and questions | Use didn't + base verb and Did...? |
| gr.a1.going-to-intentions | Be going to: intentions and plans | Talk about plans and intentions already decided. |
| gr.a1.will-basic | Will: simple predictions and immediate decisions | Use will for basic predictions and decisions made at the moment. |
| gr.a1.would-like | Would like: wants, offers and invitations | Use would like for polite wants and simple offers/invitations. |
| gr.a1.basic-word-order | Basic English sentence order | Build clear SVO clauses and place basic time/place information naturally. |

### A2 — 50 topics

| ID | Topic | Learning objective |
|---|---|---|
| gr.a2.past-simple-finished-time | Past Simple with finished time | Link completed past events to finished time expressions. |
| gr.a2.past-continuous-background | Past Continuous: background actions | Set the scene with actions in progress at a past time. |
| gr.a2.past-continuous-interruption | Past Continuous + Past Simple: interruption | Describe an action in progress interrupted by a shorter event. |
| gr.a2.past-simple-vs-continuous | Past Simple vs Past Continuous | Choose completed events vs background/in-progress past actions. |
| gr.a2.used-to | Used to: past habits and states | Describe past habits/states that are no longer true. |
| gr.a2.present-perfect-experience | Present Perfect: life experience | Talk about experience without stating a finished past time. |
| gr.a2.present-perfect-recent-result | Present Perfect: recent events and present result | Connect a recent past event to a current result. |
| gr.a2.present-perfect-ever-never | Present Perfect with ever/never | Ask and answer about experience with ever and never. |
| gr.a2.present-perfect-already-yet | Present Perfect with already/yet | Express earlier-than-expected completion and pending completion. |
| gr.a2.present-perfect-just | Present Perfect with just | Describe very recent completed events. |
| gr.a2.present-perfect-since-for | Present Perfect with since/for | Express duration from a starting point or over a period. |
| gr.a2.present-perfect-vs-past-simple | Present Perfect vs Past Simple: basic contrast | Choose unspecified/current relevance vs finished past time. |
| gr.a2.quantifiers-much-many-lot | Much, many and a lot of | Choose quantity expressions for countable and uncountable nouns. |
| gr.a2.few-little | A few/few and a little/little | Express positive or insufficient small quantities. |
| gr.a2.indefinite-pronouns | Some/any/no/every compounds | Use someone/anything/nothing/everywhere and related forms. |
| gr.a2.comparatives | Comparative adjectives and adverbs | Compare two people, things or actions. |
| gr.a2.superlatives | Superlatives | Identify the highest/lowest degree in a group. |
| gr.a2.as-as | As...as and not as...as | Express equality and inequality. |
| gr.a2.too-enough-adjective | Too and enough with adjectives/adverbs | Express excess and sufficiency. |
| gr.a2.too-much-many-enough-noun | Too much/too many/enough + noun | Express excess or sufficiency with nouns. |
| gr.a2.will-predictions | Will: predictions | Make neutral predictions about the future. |
| gr.a2.going-to-evidence | Going to: evidence-based predictions | Predict a near future result based on present evidence. |
| gr.a2.present-continuous-arrangements | Present Continuous: future arrangements | Talk about personal arrangements already organized. |
| gr.a2.present-simple-schedules | Present Simple: timetables and schedules | Use present simple for fixed future schedules. |
| gr.a2.future-forms-basic-contrast | Future forms: plans, arrangements, schedules and predictions | Choose among going to, present continuous, present simple and will. |
| gr.a2.could-past-ability | Can/could: present and past ability | Contrast present ability with general past ability. |
| gr.a2.must-have-to | Must and have to: obligation | Express internal/external obligation in common contexts. |
| gr.a2.mustnt-vs-dont-have-to | Mustn't vs don't have to | Distinguish prohibition from lack of necessity. |
| gr.a2.should-advice | Should/shouldn't: advice | Give and ask for everyday advice. |
| gr.a2.may-might-possibility | May/might: possibility | Express uncertain present or future possibilities. |
| gr.a2.polite-requests-permission | Could/may: polite requests and permission | Make more polite requests and ask/give permission. |
| gr.a2.first-conditional | First Conditional | Describe realistic future conditions and likely results. |
| gr.a2.zero-conditional | Zero Conditional | Describe general truths, rules and repeated cause-effect. |
| gr.a2.future-time-clauses | Future time clauses with when/as soon as/until | Use present forms after future time conjunctions. |
| gr.a2.infinitive-purpose | To-infinitive for purpose | Explain why someone does something using to + verb. |
| gr.a2.verb-to-infinitive-common | Common verb + to-infinitive patterns | Use want/hope/plan/decide/need and similar verbs with to-infinitives. |
| gr.a2.verb-ing-common | Common verb + -ing patterns | Use enjoy/finish/avoid/mind and similar verbs with -ing. |
| gr.a2.adjective-to-infinitive | Adjective + to-infinitive | Use common adjective complements such as happy to/helpful to/easy to. |
| gr.a2.preposition-ing | Preposition + -ing | Use gerunds after common prepositions. |
| gr.a2.phrasal-verbs-object-position | Basic phrasal verbs and object position | Place noun/pronoun objects correctly with common separable phrasal verbs. |
| gr.a2.defining-relatives-basic | Defining relative clauses: who/which/that | Add essential information about people and things. |
| gr.a2.relative-where | Relative clauses with where | Describe places with where clauses. |
| gr.a2.articles-generic-specific | Articles: generic vs specific reference | Choose a/an, the or plural reference in common generic/specific contexts. |
| gr.a2.zero-article-generic | Zero article with plural and uncountable nouns | Make generic statements without an article where appropriate. |
| gr.a2.one-ones | One/ones as substitutes | Avoid repetition by substituting one/ones for count nouns. |
| gr.a2.reflexive-pronouns | Reflexive pronouns | Use myself/yourself/etc. when subject and object refer to the same participant. |
| gr.a2.adverbs-manner | Adverbs of manner | Describe how actions happen and form common -ly adverbs. |
| gr.a2.adjective-vs-adverb | Adjective vs adverb | Choose the correct form to modify nouns, verbs and adjectives. |
| gr.a2.basic-subordination | Because, so, although and while | Connect clauses for reason, result, contrast and simultaneous situations. |
| gr.a2.question-tags-basic | Basic question tags | Use common positive/negative tag patterns to check information. |

### B1 — 60 topics

| ID | Topic | Learning objective |
|---|---|---|
| gr.b1.present-perfect-unfinished-time | Present Perfect: unfinished time periods | Talk about events within time periods that continue to now. |
| gr.b1.present-perfect-repeated-events | Present Perfect: repeated events up to now | Describe repeated actions whose time frame includes the present. |
| gr.b1.present-perfect-result-vs-event | Present Perfect: result focus vs event focus | Choose wording based on whether the current result or occurrence matters. |
| gr.b1.been-vs-gone | Been vs gone | Distinguish returned experience/location from still-being-away meaning. |
| gr.b1.have-had-duration | Have had and other state verbs over time | Use present perfect with possession and long-running states. |
| gr.b1.present-perfect-continuous-duration | Present Perfect Continuous: duration | Emphasize ongoing/recent activity over a period leading to now. |
| gr.b1.present-perfect-simple-vs-continuous | Present Perfect Simple vs Continuous | Choose result/completion/count vs duration/activity focus. |
| gr.b1.past-perfect-earlier-past | Past Perfect: earlier past | Mark an event as earlier than another past reference point. |
| gr.b1.past-perfect-vs-past-simple | Past Perfect vs Past Simple | Use past perfect only when earlier-past ordering needs marking. |
| gr.b1.narrative-tenses | Narrative tenses | Combine past simple, continuous and perfect to tell coherent stories. |
| gr.b1.used-to-vs-would | Used to vs would for past habits | Choose forms for repeated past actions and past states. |
| gr.b1.future-continuous | Future Continuous | Describe actions expected to be in progress at a future time. |
| gr.b1.will-vs-going-to | Will vs going to: intention and prediction nuance | Choose between spontaneous/neutral future meaning and prior intention/evidence. |
| gr.b1.present-future-forms-detail | Present forms for future events | Distinguish arrangements from fixed schedules in realistic planning. |
| gr.b1.first-conditional-variants | First Conditional: modal and imperative results | Use can/may/might/should or imperatives in realistic result clauses. |
| gr.b1.second-conditional | Second Conditional | Describe unlikely or hypothetical present/future situations. |
| gr.b1.conditional-alternatives | Unless, as long as and provided that | Express conditions without relying only on if. |
| gr.b1.wish-present | Wish + past: present wishes | Express dissatisfaction with a present situation. |
| gr.b1.hope-vs-wish | Hope vs wish | Choose realistic desired outcomes vs counterfactual/regret meanings. |
| gr.b1.deduction-present | Must/might/can't: present deduction | Infer present situations with different confidence levels. |
| gr.b1.possibility-modals | May/might/could: degrees and contexts of possibility | Express uncertain possibilities with natural modal choices. |
| gr.b1.obligation-need | Have to, must and need to | Distinguish sources and strengths of obligation/necessity. |
| gr.b1.advice-strength | Should, ought to and had better | Adjust the strength and consequence implied by advice. |
| gr.b1.permission-allowed | Can/could/be allowed to | Express permission across present, past and more formal contexts. |
| gr.b1.gerund-infinitive-similar | Gerund vs infinitive after verbs with little meaning change | Use common verbs that accept both patterns naturally. |
| gr.b1.remember-forget-gerund-infinitive | Remember/forget + -ing vs to-infinitive | Distinguish memory of past action from remembering a duty. |
| gr.b1.stop-try-gerund-infinitive | Stop/try + -ing vs to-infinitive | Distinguish ending an activity, purpose, experiment and effort meanings. |
| gr.b1.verb-object-to-infinitive | Verb + object + to-infinitive | Use tell/ask/want/allow/encourage patterns. |
| gr.b1.make-let-help | Make/let/help + object + verb | Use causative/permission patterns with bare infinitives appropriately. |
| gr.b1.passive-present-past | Passive Voice: present and past simple | Shift focus from doer to action/result. |
| gr.b1.passive-modals | Passive with modal verbs | Form modal + be + past participle for rules, possibility and obligation. |
| gr.b1.passive-agent-choice | Passive agents and when to omit them | Decide whether a by-agent is useful, obvious or irrelevant. |
| gr.b1.defining-relative-clauses | Defining relative clauses | Add essential identifying information accurately. |
| gr.b1.nondefining-relative-clauses | Non-defining relative clauses | Add extra information with commas and appropriate pronouns. |
| gr.b1.relative-pronoun-omission | Omitting relative pronouns | Omit object relative pronouns when grammar allows it. |
| gr.b1.relative-whose | Relative clauses with whose | Express possession inside defining and non-defining relative clauses. |
| gr.b1.reported-statements | Reported statements | Report speech with pronoun/time changes and basic backshift. |
| gr.b1.reported-questions | Reported questions | Use statement word order in reported yes/no and wh-questions. |
| gr.b1.reported-requests-commands | Reported requests and commands | Report instructions using tell/ask + object + to-infinitive. |
| gr.b1.reported-speech-backshift | Reported speech: backshift vs unchanged truth | Choose when backshift is natural and when it is unnecessary. |
| gr.b1.indirect-questions | Indirect questions | Use polite question frames with statement word order. |
| gr.b1.question-tags | Question tags: agreement and intonation meaning | Form tags and understand checking vs confirmation functions. |
| gr.b1.embedded-questions | Embedded wh-clauses | Use wh-clauses after verbs such as know, wonder and explain. |
| gr.b1.comparative-modifiers | Comparative modifiers | Use much/far/a lot/a bit/slightly with comparatives. |
| gr.b1.comparison-relations | Same as, different from and similar to | Express comparison relationships with correct prepositions. |
| gr.b1.too-enough-nuance | Too/enough: consequence and implication | Use too/enough to imply whether an action/result is possible. |
| gr.b1.so-such | So and such | Intensify adjective/adverb vs noun phrases correctly. |
| gr.b1.articles-institutions | Articles with institutions and activities | Distinguish school/work/home/bed as activities vs specific places. |
| gr.b1.articles-geography | Articles with geographical names | Use the/zero article with countries, rivers, seas, mountains and regions. |
| gr.b1.both-either-neither | Both/either/neither | Refer to two people or things with correct agreement and meaning. |
| gr.b1.each-every-all | Each, every and all | Choose distributive vs group reference. |
| gr.b1.other-forms | Another/other/others/the other | Refer to additional and remaining people/things accurately. |
| gr.b1.quantifiers-most-enough-plenty | Most, enough and plenty of | Express broad proportions and sufficiency naturally. |
| gr.b1.adjective-preposition-patterns | Common adjective + preposition patterns | Use patterns such as interested in, good at and responsible for. |
| gr.b1.noun-preposition-patterns | Common noun + preposition patterns | Use patterns such as reason for, solution to and increase in. |
| gr.b1.verb-preposition-patterns | Common verb + preposition patterns | Use depend on, belong to, apply for and similar combinations. |
| gr.b1.phrasal-verb-separability | Phrasal verbs: separable vs inseparable | Place objects correctly and identify particle/preposition behavior. |
| gr.b1.concession-linkers | Although, despite and in spite of | Express concession with correct clause or noun/-ing complements. |
| gr.b1.reason-result-linkers | Because of, therefore and as a result | Connect causes and consequences across sentence structures. |
| gr.b1.narrative-linkers | Narrative sequencing and discourse markers | Organize spoken/written stories with before, after, then, eventually and meanwhile. |

### B2 — 60 topics

| ID | Topic | Learning objective |
|---|---|---|
| gr.b2.perfect-aspect-nuance | Present perfect simple/continuous: nuanced aspect choice | Choose completion, result, repetition, temporary activity or duration focus. |
| gr.b2.past-perfect-continuous | Past Perfect Continuous | Show duration/activity leading up to a past reference point. |
| gr.b2.future-perfect | Future Perfect | Describe actions completed by a future deadline/reference point. |
| gr.b2.future-continuous-expectation | Future Continuous: expected course and polite inquiry | Describe expected ongoing events and ask about plans neutrally. |
| gr.b2.future-in-the-past | Future in the past | Use would/was going to/was about to for future viewed from a past point. |
| gr.b2.future-forms-planning | Advanced future form choice in plans | Coordinate intentions, arrangements, schedules, predictions and deadlines. |
| gr.b2.second-conditional-modals | Second Conditional with could/might | Express hypothetical ability and uncertain hypothetical results. |
| gr.b2.third-conditional | Third Conditional | Describe unreal past conditions and imagined past results. |
| gr.b2.mixed-conditional-past-present | Mixed Conditional: past condition → present result | Connect a counterfactual past event to a present consequence. |
| gr.b2.mixed-conditional-present-past | Mixed Conditional: present state → past result | Connect an unreal present/general condition to a past consequence. |
| gr.b2.wish-past-regret | Wish/if only + past perfect | Express regret about past events. |
| gr.b2.wish-would-annoyance | Wish/if only + would | Express desired change or annoyance about controllable behavior. |
| gr.b2.would-rather | Would rather / would sooner | Express preferences about one's own or another person's actions. |
| gr.b2.unreal-past-time-as-if | Unreal past after It's time / as if / as though | Use past forms for remoteness, criticism or unreal comparison. |
| gr.b2.deduction-past | Must have/might have/can't have | Make deductions about past events with graded certainty. |
| gr.b2.modal-perfect-criticism | Should have/ought to have | Express criticism, regret and unfulfilled expectation. |
| gr.b2.modal-perfect-possibility | Could have/might have | Express unrealized options and uncertain past possibilities. |
| gr.b2.neednt-vs-didnt-need | Needn't have vs didn't need to | Distinguish unnecessary action performed vs no necessity. |
| gr.b2.passive-continuous-perfect | Continuous and perfect passives | Use is being done/has been done/had been done appropriately. |
| gr.b2.get-passive | Get-passive | Use get + past participle in natural informal/eventive contexts. |
| gr.b2.reporting-passive | Reporting passives | Use It is said that... and subject + is believed to... patterns. |
| gr.b2.causative-have-get | Have/get something done | Describe arranging for another person to perform a service/action. |
| gr.b2.reporting-verbs-patterns | Reporting verbs and complement patterns | Use admit/deny/suggest/accuse/remind/warn with correct structures. |
| gr.b2.reported-speech-advanced | Reported speech: time, place and viewpoint shifts | Adjust deictic words and viewpoint beyond simple tense backshift. |
| gr.b2.reporting-infinitive-gerund | Reporting with infinitive and gerund patterns | Choose structures after advise, promise, recommend, apologize and similar verbs. |
| gr.b2.relative-prepositions | Relative clauses with prepositions | Use formal preposition + whom/which and natural stranded-preposition alternatives. |
| gr.b2.participle-clauses-ing | Present participle clauses | Reduce clauses when subjects align and simultaneous/cause meanings are clear. |
| gr.b2.participle-clauses-ed | Past participle clauses | Use reduced passive/result clauses accurately. |
| gr.b2.reduced-relative-clauses | Reduced relative clauses | Condense active/passive relative clauses without ambiguity. |
| gr.b2.emphatic-do | Emphatic do | Add contrastive emphasis to affirmative present/past statements. |
| gr.b2.noun-clauses-that-whether-wh | Noun clauses with that, whether/if and wh-words | Use clauses as objects/complements with correct word order. |
| gr.b2.wh-ever-clauses | Whoever/whatever/wherever clauses | Express free-choice or unknown reference with -ever forms. |
| gr.b2.gerund-clauses-subject | Gerund clauses as subjects and complements | Use -ing clauses as noun-like units in formal and everyday English. |
| gr.b2.infinitive-clauses | Infinitive clauses after nouns/adjectives and as complements | Build compact to-infinitive clause structures with clear understood subjects. |
| gr.b2.complex-noun-phrases | Complex noun phrases with postmodification | Build noun phrases using prepositional, relative and non-finite modifiers. |
| gr.b2.articles-abstract-nouns | Articles with abstract nouns | Choose zero/a/the as abstract ideas become general, instances or specified concepts. |
| gr.b2.articles-modified-reference | Articles with modifiers and unique reference | Use article choice when restrictive modifiers make reference identifiable. |
| gr.b2.generic-reference | Generic reference with a/an, the and zero article | Choose among three generic patterns based on noun type and style. |
| gr.b2.less-fewer-number-amount | Less/fewer, number/amount and quantity precision | Match quantifiers and measure nouns to countability. |
| gr.b2.advanced-quantifiers | A great deal of, hardly any, a large number/amount of | Use formal and nuanced quantity expressions. |
| gr.b2.correlative-comparison | The more..., the more... | Express linked changes with correlative comparatives. |
| gr.b2.superlative-present-perfect | Superlative + present perfect experience | Use patterns such as the best ... I've ever ... naturally. |
| gr.b2.adjective-order | Adjective order | Order opinion, size, age, shape, color, origin, material and purpose adjectives naturally. |
| gr.b2.gradable-intensifiers | Gradable vs non-gradable adjectives and intensifiers | Choose very, absolutely, completely, highly, deeply and similar modifiers naturally. |
| gr.b2.stance-adverbs | Stance adverbs | Use apparently, obviously, fortunately, arguably and similar items to mark speaker stance. |
| gr.b2.focus-adverbs | Focus adverbs: even, only, just, also | Place focus adverbs to control what part of a sentence is emphasized. |
| gr.b2.fixed-prepositional-phrases | Fixed prepositional phrases | Use common multiword patterns such as in charge of, on behalf of and in response to. |
| gr.b2.dependent-prepositions-adjectives | Advanced adjective + preposition patterns | Master less predictable adjective complement choices and meaning changes. |
| gr.b2.dependent-prepositions-verbs | Advanced verb + preposition patterns | Master verb-preposition combinations whose meaning depends on the preposition. |
| gr.b2.multiword-verbs | Phrasal-prepositional and multiword verbs | Distinguish particle, preposition and three-word verb patterns. |
| gr.b2.lexical-collocation-core | High-value make/do/take/have collocations | Choose natural light-verb collocations rather than literal alternatives. |
| gr.b2.concession-discourse | Whereas, while, nevertheless and despite | Express contrast/concession with appropriate syntax and register. |
| gr.b2.cause-effect-formal | Due to, owing to, consequently and as a result | Express cause/effect in neutral and formal registers. |
| gr.b2.purpose-result-clauses | In order to, so as to and so that | Express purpose while controlling subject and clause structure. |
| gr.b2.discourse-reference | This/that/such as discourse reference | Refer back to propositions and situations coherently. |
| gr.b2.substitution-ellipsis | Substitution and ellipsis with do/so/neither/nor | Avoid repetition while preserving grammatical meaning. |
| gr.b2.formal-informal-requests | Formal vs informal requests and hedging | Adjust modal, question and softening choices to social context. |
| gr.b2.spoken-ellipsis-tags | Spoken ellipsis, response forms and conversational tags | Use natural omissions and short follow-up structures in conversation. |
| gr.b2.word-order-adverbials | Adverbial position and information flow | Place manner/place/time and sentence adverbials for clarity and emphasis. |
| gr.b2.preposition-choice-meaning | Preposition choice and meaning contrasts | Distinguish near-synonymous prepositions in time, place, cause and method contexts. |

### C1 — 50 topics

| ID | Topic | Learning objective |
|---|---|---|
| gr.c1.negative-inversion | Inversion after negative and restrictive adverbials | Use Never/Rarely/Only then/Not until + auxiliary inversion for marked emphasis. |
| gr.c1.conditional-inversion | Conditional inversion with had/were/should | Form formal conditionals without if. |
| gr.c1.fronting-topicalization | Fronting and topicalization | Move constituents to the front to establish topic or contrast without losing clarity. |
| gr.c1.it-clefts | It-clefts for focused emphasis | Use It was X that/who... to focus a constituent. |
| gr.c1.wh-clefts | Wh-clefts and reversed clefts | Use What...is... and related patterns to organize information and emphasis. |
| gr.c1.perfect-participle-clauses | Perfect participle clauses | Use having + past participle for earlier non-finite events. |
| gr.c1.participle-clause-control | Participle clauses and subject control | Avoid dangling or ambiguous participle clauses. |
| gr.c1.nominalisation | Nominalisation in formal writing | Convert processes/qualities into noun phrases without producing dense unnatural prose. |
| gr.c1.complex-reporting-passives | Complex reporting passives | Use passive reporting with perfect/continuous infinitives and appropriate evidential distance. |
| gr.c1.mandative-subjunctive | Mandative subjunctive | Use base-form subjunctives after recommendations, demands and necessity expressions. |
| gr.c1.mandative-should | Mandative should | Use should in formal recommendation/necessity clauses where natural. |
| gr.c1.modal-remoteness | Modal remoteness and tentative meaning | Use past/modal forms to soften stance, proposals and interpersonal claims. |
| gr.c1.epistemic-hedging | Epistemic hedging | Calibrate certainty with seem, appear, tend to, may, arguably and related patterns. |
| gr.c1.stance-positioning | Stance adverbials and writer positioning | Signal confidence, evaluation and viewpoint in formal discourse. |
| gr.c1.advanced-concession | Advanced concession: even if/even though/much as | Choose concessive structures based on fact vs hypothesis and register. |
| gr.c1.free-choice-concession | No matter and wh-ever concession | Express unrestricted conditions such as no matter how/whatever happens. |
| gr.c1.sentential-relative-which | Sentential which clauses | Use which to comment on a preceding clause or proposition. |
| gr.c1.advanced-reduced-relatives | Advanced non-finite relative reduction | Reduce relative clauses with participles/infinitives while preserving meaning. |
| gr.c1.appositive-that-clauses | Appositive that-clauses | Use clauses after nouns such as fact, idea, claim and possibility. |
| gr.c1.noun-complement-clauses | Noun complement patterns | Choose that/of -ing/to-infinitive/preposition complements after abstract nouns. |
| gr.c1.preposition-wh-clauses | Prepositions + wh-clauses | Use structures such as about what, on whether and by how naturally. |
| gr.c1.future-perfect-continuous | Future Perfect Continuous | Emphasize duration of activity up to a future point. |
| gr.c1.be-to-formal-future | Be to for official plans and instructions | Use be to for formal schedules, requirements and planned events. |
| gr.c1.future-periphrases | Be due/about/bound/likely to | Express imminence, schedule and probability with nuanced future periphrases. |
| gr.c1.modal-perfect-continuous | Modal perfect continuous | Reason about past ongoing activity with must/might/could have been + -ing. |
| gr.c1.counterfactual-modal-nuance | Counterfactual modal nuance | Distinguish would/could/might have in unreal past results. |
| gr.c1.advanced-unreal-preferences | Unreal past in preferences and criticism | Use would rather/sooner, would prefer and It's time with correct subject/time reference. |
| gr.c1.advanced-condition-markers | Supposing, provided, but for and otherwise | Express formal, hypothetical and exception conditions compactly. |
| gr.c1.mixed-conditionals-nuance | Mixed conditionals: time and causality nuance | Build cross-time counterfactuals only when the causal relationship is coherent. |
| gr.c1.auxiliary-ellipsis | Ellipsis after auxiliaries | Omit repeated verb phrases after auxiliaries while preserving tense/modal meaning. |
| gr.c1.advanced-substitution | One/ones, that/those, former/latter and do so | Choose substitution devices by noun type, register and discourse relation. |
| gr.c1.articles-shared-knowledge | Articles and shared situational knowledge | Use the when identifiability comes from shared context rather than prior mention. |
| gr.c1.institution-metonymy-articles | Institutional/metonymic article shifts | Distinguish activity, institution, building and service meanings through article choice. |
| gr.c1.partitives-proportions | Partitives and proportions | Use a proportion/share/majority/minority/percentage of with correct agreement and countability. |
| gr.c1.complex-subject-agreement | Agreement with complex subjects | Handle intervening phrases, either/or, neither/nor and quantified noun phrases. |
| gr.c1.notional-agreement | Notional and proximity agreement | Choose singular/plural agreement with collective and coordinated meanings by dialect/register. |
| gr.c1.adjective-complementation | Advanced adjective complementation | Choose adjective + that-clause/to-infinitive/preposition patterns and understood subjects. |
| gr.c1.verb-complementation-advanced | Advanced verb complementation | Control complex patterns after perception, causative, reporting and attitude verbs. |
| gr.c1.resultative-constructions | Resultative constructions | Use patterns such as wipe it clean/paint it red where English licenses result states. |
| gr.c1.causative-ergative-alternation | Causative and ergative alternation | Distinguish verbs used transitively for causing change vs intransitively for change. |
| gr.c1.formal-discourse-markers | Formal discourse markers | Organize arguments with moreover, nonetheless, conversely, hence and related markers. |
| gr.c1.cohesion-reference-chains | Cohesion and reference chains | Maintain clear pronoun, demonstrative and lexical reference across paragraphs. |
| gr.c1.given-new-information | Given/new information and clause ordering | Order information so known material leads naturally to new/focal material. |
| gr.c1.parallelism | Grammatical parallelism | Keep coordinated lists, comparisons and paired structures grammatically parallel. |
| gr.c1.impersonal-formal-style | Impersonal constructions in formal writing | Use passive, anticipatory it and impersonal reporting without obscuring responsibility. |
| gr.c1.spoken-headers-tails | Spoken headers and tails | Recognize/use conversational topic frames such as That car, is it yours? and It's nice, that place. |
| gr.c1.vague-language | Vague language and approximators | Use kind of, roughly, or so, and things like that appropriately by register. |
| gr.c1.politeness-mitigation | Politeness and mitigation | Use distancing, softeners and indirect forms to manage face-sensitive requests/disagreement. |
| gr.c1.boosters-downtoners | Boosters and downtoners | Control emphasis with highly, strongly, rather, somewhat and related stance choices. |
| gr.c1.advanced-preposition-choice | Advanced preposition choice | Resolve idiomatic and abstract preposition contrasts that cannot be predicted from literal meaning alone. |

### C2 — 35 topics

| ID | Topic | Learning objective |
|---|---|---|
| gr.c2.narrative-viewpoint-aspect | Tense/aspect viewpoint shifts in narrative | Manipulate temporal viewpoint across scenes while keeping reference time coherent. |
| gr.c2.historical-present | Historical present and stylistic tense shift | Use present forms for vivid narration without accidental tense inconsistency. |
| gr.c2.sequence-of-tenses | Sequence of tenses and deliberate non-backshift | Manage tense relationships in complex reporting across multiple time frames. |
| gr.c2.modal-ambiguity | Epistemic vs deontic modal readings | Disambiguate probability, obligation, permission and volition from context. |
| gr.c2.layered-counterfactuals | Layered counterfactual reasoning | Express multi-stage unreal causes/results across past and present time frames. |
| gr.c2.implicit-conditionals | Implied and elliptical conditionals | Recognize and produce conditional meaning without an explicit if-clause. |
| gr.c2.so-such-inversion | Inversion after so/such | Use formal/literary So + adjective... and Such was... patterns accurately. |
| gr.c2.locative-inversion | Locative and directional inversion | Use marked place/direction-first inversion in descriptive/literary contexts. |
| gr.c2.formulaic-subjunctive | Formulaic and irrealis subjunctive | Use fixed expressions and were-subjunctive forms with appropriate register. |
| gr.c2.gapping-complex-ellipsis | Gapping and complex ellipsis | Omit repeated material across coordinated clauses without ambiguity. |
| gr.c2.comparative-clause-ellipsis | Ellipsis in comparative clauses | Interpret and produce reduced clauses after than/as. |
| gr.c2.free-relatives | Free/fused relative clauses | Use what/where/how constructions that function as complete noun phrases. |
| gr.c2.nominal-wh-ever-relatives | Nominal whoever/whatever/whichever clauses | Use -ever relatives as noun phrases distinct from concessive clauses. |
| gr.c2.extraposition-anticipatory-it | Extraposition and anticipatory it | Move heavy clauses rightward with it while preserving information structure. |
| gr.c2.raising-vs-control | Raising vs control patterns in advanced usage | Distinguish surface subjects from understood semantic subjects in seem/appear/expect/try-type structures. |
| gr.c2.tough-constructions | Tough constructions | Use patterns such as This problem is difficult to solve with correct understood object relations. |
| gr.c2.supplementive-clauses | Supplementive participial clauses | Use detached non-finite clauses to add circumstance/comment without dangling reference. |
| gr.c2.absolute-clauses | Absolute clauses | Use noun + participle/adjective/preposition supplements independently of main-clause subject. |
| gr.c2.verbless-clauses | Verbless clauses | Use compact subordinate/supplement clauses such as when necessary/though difficult appropriately. |
| gr.c2.pp-attachment-ambiguity | Prepositional phrase attachment and ambiguity | Detect and rewrite structures where a prepositional phrase has multiple plausible attachments. |
| gr.c2.proper-name-articles | Articles with proper names and institutional titles | Handle marked article use with newspapers, organizations, families, landmarks and renamed entities. |
| gr.c2.countability-coercion | Countability shifts and coercion | Use mass nouns as countable instances/types and count nouns as substances/activities when context licenses it. |
| gr.c2.word-class-conversion | Word-class conversion | Recognize and use noun↔verb/adjective shifts without overt morphology in contemporary English. |
| gr.c2.pragmatic-tense-modal | Pragmatic meanings of tense and modality | Use tense/modal choices for politeness, distancing, tentativeness and interpersonal stance. |
| gr.c2.evidential-distancing | Evidential and reporting distance | Attribute claims and manage commitment through reportedly, be said to, seem and related grammar. |
| gr.c2.concessive-inversion | Concessive inversion with adjective/adverb + though/as | Use patterns such as Difficult though it was... in formal/literary style. |
| gr.c2.formal-conditional-register | Formal and legal-style conditional constructions | Interpret and produce subject to/provided that/in the event that/should structures without overusing them. |
| gr.c2.dense-noun-phrases | Dense noun phrases and noun stacks | Parse and edit long premodification chains for clarity in technical/academic prose. |
| gr.c2.construction-register-selection | Construction choice and register constraints | Choose among grammatically possible constructions based on genre, formality and idiomatic frequency. |
| gr.c2.idiomatic-prepositions-c2 | Idiomatic preposition selection at advanced level | Resolve low-predictability preposition choices through collocational evidence and context. |
| gr.c2.advanced-punctuation-grammar | Punctuation as grammatical signaling | Use colon, semicolon, dash and comma choices to mark clause relations without run-ons or comma splices. |
| gr.c2.spoken-written-register-shift | Spoken vs written grammar at C2 | Recast headers, ellipsis, contractions and dense nominal style appropriately across registers. |
| gr.c2.marked-word-order-rhetoric | Marked word order for rhetorical effect | Use fronting, inversion and end-focus intentionally rather than accidentally. |
| gr.c2.ambiguity-reference-editing | Syntactic ambiguity and reference repair | Diagnose ambiguous modification/pronoun scope and rewrite for a single intended reading. |
| gr.c2.advanced-editing-consistency | Advanced grammatical editing | Repair subtle agreement, parallelism, tense/aspect and complement-pattern inconsistencies in long text. |

## 19. Curriculum sequencing and overlap policy

The list is a knowledge framework, not 300 isolated mini-courses.

A topic can depend on another topic. Example:

- A2 present-perfect-experience introduces indefinite life experience;
- A2 since/for introduces basic duration;
- B1 unfinished-time/repeated-events/result-focus deepen aspect choices;
- B1 simple-vs-continuous adds activity/result contrast;
- B2 perfect-aspect-nuance integrates the system in harder discourse.

This is progressive depth, not artificial duplication.

Every topic file must declare prerequisites and contrastTopicIds. Validation flags suspicious same-level overlap by normalized title/objective similarity.

## 20. Topic lesson coverage contract

A fully publishable grammar/usage topic should normally include:

1. concept/meaning;
2. Vietnamese explanation;
3. formula/structure;
4. when to use;
5. positive form where applicable;
6. negative form where applicable;
7. question form where applicable;
8. variations;
9. related collocations;
10. natural examples;
11. common mistakes;
12. contrast with similar structures;
13. short dialogues;
14. daily-life examples;
15. work examples;
16. travel examples;
17. cloze exercises;
18. error correction;
19. sentence building;
20. translation exercises.

Important: positive/negative/question are NOT mandatory conceptual subdivisions for topics where they make no pedagogical sense, such as adjective order or discourse cohesion. The schema supports them; the lesson validator should apply topic-type-specific requirements.

Initial quality floor for a fully authored topic:

- 20+ validated natural examples across contexts;
- 30+ validated exercises across at least three exercise families;
- at least 3 common mistakes when the topic has predictable learner errors;
- at least 1 contrast link where confusion with another structure is material;
- dialogue coverage when the structure is genuinely conversational;
- no forced daily/work/travel example if the scenario would be unnatural; corpus-wide context coverage is more important than mechanical per-topic templating.

## 21. Content-generation pipeline

### Stage 0 — source manifest

For every upstream dataset record:

- source name;
- version/snapshot;
- URL;
- expected checksum;
- license;
- attribution;
- redistributionAllowed;
- transformationAllowed;
- notes.

### Stage 1 — fetch/raw cache

Raw bulk files live outside committed runtime data by default.

Requirements:

- deterministic download command;
- checksum validation;
- no silent "latest" in production;
- cache can be regenerated.

### Stage 2 — normalization

Convert upstream formats to internal candidate schemas.

No pedagogical rewriting yet.

### Stage 3 — alignment

Align candidates to:

- legacy vocabulary keys;
- lexeme IDs;
- sense IDs;
- CEFR candidates;
- grammar topics;
- phrase IDs.

Unmatched candidates go to a review queue, not silent deletion unless the filter is documented.

### Stage 4 — authoring/enrichment

Create project-authored:

- Vietnamese explanations;
- controlled examples;
- contrasts;
- mistakes;
- exercises;
- accepted alternatives.

Bulk AI/model generation is allowed only as candidate production. It never directly sets state=published.

### Stage 5 — automated validation

Run schema, quality, license, target-presence, dedup and consistency checks.

### Stage 6 — review

Review can be:

- deterministic rule review;
- second-model review;
- bilingual/editor review;
- sampled human QA for large batches;
- targeted full human review for high-risk categories.

The method must be recorded. A "checked" flag without method is not enough.

### Stage 7 — publication

Only reviewed/published records are sharded into shared runtime data.

### Stage 8 — regression/game checks

Generate runtime views and run parent + affected child tests/builds.

## 22. Validation pipeline

Planned commands:

~~~
pnpm english-content:generate
pnpm english-content:validate
pnpm english-content:test
pnpm english-content:coverage
pnpm english-content:licenses
pnpm english-content:dedupe
~~~

Suggested modules:

- scripts/english-content/schema.mjs
- scripts/english-content/normalize.mjs
- scripts/english-content/provenance.mjs
- scripts/english-content/license-check.mjs
- scripts/english-content/dedupe.mjs
- scripts/english-content/cefr.mjs
- scripts/english-content/target-detect.mjs
- scripts/english-content/publish.mjs

### 22.1 Required validation categories

Schema:
- valid JSON;
- exact schema version;
- no unknown required-contract fields where schema is closed;
- unique IDs.

Grammar:
- sentence-level parse/rules where deterministic;
- accepted-answer consistency;
- structure-specific checks.

Translation:
- both sides non-empty;
- normalized duplicates;
- punctuation/placeholder integrity;
- bilingual quality state present;
- accepted alternatives not contradictory.

Target presence:
- sentence actually contains the lexeme/phrase/structure it claims to teach;
- transformations actually transform the requested feature;
- cloze target actually occupies the blank;
- mistake record correction actually repairs the classified error.

Naturalness:
- reject broken templates;
- detect excessive repeated n-grams;
- review awkward collocations;
- flag improbable punctuation/casing.

CEFR:
- check target topic level;
- calculate vocabulary coverage against current levels;
- flag sentences with excessive above-level vocabulary;
- use syntax heuristics;
- do not auto-reject legitimate higher-level proper terms without context review.

Length:
- mode-specific limits, not one universal sentence limit.

License:
- every imported record must resolve to a known source manifest and allowed runtime license.

## 23. Deduplication

### 23.1 Exact dedup

Canonical sentence key:

- NFC;
- trim/collapse spaces;
- normalized punctuation variants where safe;
- case-fold only for duplicate comparison, not stored text.

Store an exact content fingerprint.

### 23.2 Near-duplicate detection

Use a combination of:

- token Jaccard;
- character/token n-grams;
- MinHash or SimHash;
- edit-distance for short sentences;
- optional local semantic embedding only as a review signal.

Near-duplicate detection creates a review queue. It must not blindly delete semantically different minimal pairs such as:

"I have lived here for five years."
"I lived here for five years."

Those can be pedagogically valuable contrasts.

### 23.3 Template-family detection

Detect excessive shells such as:

"I usually X in the morning."
"I usually Y in the morning."
"I usually Z in the morning."

Some patterned drills are valid, but the published example corpus must not be dominated by them. Mark drill/template records separately from natural-example records.

## 24. Vietnamese translation quality

Vietnamese quality rules:

- preserve intended sense, not just headword gloss;
- prefer natural Vietnamese over word-for-word structure;
- preserve register;
- avoid adding a subject/pronoun that changes meaning when context is neutral;
- keep technical terms consistent;
- distinguish explanation from translation;
- avoid unnatural machine-translation punctuation;
- ensure English accepted alternatives map to the same intended Vietnamese prompt.

Recommended review flow:

1. generation/import candidate;
2. independent translation check;
3. semantic equivalence check;
4. terminology consistency check;
5. sampled bilingual human audit per batch;
6. escalate low-confidence/high-ambiguity items.

Back-translation may be used as a weak diagnostic signal only; it is not proof of correctness.

## 25. Common-mistake quality

Sources of mistakes are distinct:

- pedagogical: deliberately authored based on known grammar contrast;
- source-attested: backed by a licensed learner/error source;
- observed-local: derived from the user's own local Learning Profile.

Never upload or aggregate private local learner answers into the shared repo automatically.

When a local recurring error becomes useful for practice, use it only inside the local profile/review engine unless the user deliberately authors a generic public example.

## 26. Runtime content query layer

Introduce one parent-owned library module rather than five independent fetch implementations.

Conceptual API:

~~~
EnglishContent.getGrammarTopic(id)
EnglishContent.getLexeme(key)
EnglishContent.getSenses(key)
EnglishContent.getExamples(query)
EnglishContent.getExercises(query)
EnglishContent.getPhrase(id)
EnglishContent.resolveReviewItem(item, capability)
~~~

Queries support:

- IDs;
- CEFR;
- target grammar;
- target lexical IDs;
- activity type;
- domain/context;
- register;
- maximum length;
- source/license filters where needed.

The parent produces bounded datasets. Child games do not scan 100k records.

## 27. Learning-event compatibility

Do not force a Learning Event v2 just to launch content.

Initial mapping:

- word/collocation/phrasal verb/idiom/chunk practice can continue using entityType=vocabulary where the canonical normalized phrase key is sufficient for existing mastery;
- grammar activities use entityType=grammar with stable gr.* IDs;
- sentence/translation/building/listening sentence activities use entityType=sentence with stable sent.* IDs;
- exercise IDs can be recorded as activity metadata in a backward-compatible extension only after the shared event schema explicitly permits it.

If analytics later require independent mastery for phrase senses, collocations or transformations, design Learning Event v2 as a deliberate migration. Do not overload v1 inconsistently across children.

## 28. Game integration matrix

Legend: P1 = first rich-content integration, P2 = later integration, existing = already substantially supported.

| Content/activity | Monkeytype | Shooter | Recall | Karaoke | Space |
|---|---|---|---|---|---|
| Legacy vocabulary | existing | existing | existing | existing | existing |
| Sense/usage display | P1 | P2 | P1 | P2 | P2 |
| Example typing | P1 | optional | P2 | P1 | P2 |
| Grammar typing | P1 | no initial | no initial | P2 | challenge-only |
| Collocation typing | P1 | P1 | P1 | P2 | P1 |
| Phrasal verbs/chunks | P1 | P1 | P1 | P2 | P1 |
| Cloze | existing prototype → P1 corpus | later micro-cloze | later | P2 | challenge-only |
| Error correction | P1 | no initial | no initial | later | challenge-only |
| Sentence building | existing engine → P1 corpus | no initial | later short | P2 | event-only |
| VI→EN translation | P1 | later short | P1 | P2 | challenge-only |
| Transformation | P1 | no initial | no initial | later | event-only |
| Listening typing | existing/P1 corpus | optional | existing/P1 | P1 | optional |
| Contextual usage | P1 | later | P2 | P1 | P2 |

### 28.1 Monkeytype

First rich-content executor because it already has:

- dictionary display;
- learning modes;
- Context/Cloze;
- Sentence Builder;
- Smart Review;
- sentence/grammar event support.

Implementation order:

1. parent rich-content query adapter;
2. authored grammar topic/example display;
3. canonical sentence-builder adapter;
4. corpus-backed cloze;
5. translation;
6. correction/transformation;
7. contextual usage;
8. listening from canonical sentence IDs.

Vietnamese IME-safe mode remains isolated; new activities must reuse its tested input contract rather than bypass it.

### 28.2 Vocabulary Shooter

Keep combat readable.

Best targets:

- single words;
- collocations;
- short phrasal verbs;
- short chunks.

A short context line may be shown outside the typed target. Do not turn every enemy into a paragraph.

### 28.3 Recall Typing

Best targets:

- words;
- phrases/chunks;
- collocations;
- phrasal verbs;
- short VI→EN production;
- audio→English recall.

Hint generation must understand phrase token boundaries rather than assuming one word.

### 28.4 Karaoke Typing

Best targets:

- sentence listening/typing;
- dialogues;
- phrase rhythm/chunk exposure;
- sentence review.

Do not import copyrighted song lyrics into the canonical learning corpus merely because the game is named Karaoke. Canonical learning content should be project-authored or properly licensed.

### 28.5 Space Typing

Best targets:

- vocabulary;
- collocations;
- chunks;
- phrasal verbs;
- short contextual choices during combat;
- sentence/grammar objectives in dedicated challenge/boss/event phases.

Long rich explanations belong before/after combat, not over enemies.

## 29. Parent curriculum model

shared/curriculum/a1.json ... c2.json define sequence and prerequisites, not duplicate lesson bodies.

Conceptual record:

~~~json
{
  "schemaVersion": 1,
  "cefr": "A2",
  "units": [
    {
      "id": "a2.perfect-intro",
      "topicIds": [
        "gr.a2.present-perfect-experience",
        "gr.a2.present-perfect-ever-never"
      ],
      "recommendedActivities": [
        "example-typing",
        "cloze",
        "translation"
      ]
    }
  ]
}
~~~

Curriculum supports:

- prerequisite order;
- recommended review mix;
- context rotation;
- coverage dashboards;
- game capability routing.

It does not hardcode mastery; shared/learning remains authoritative for progress.

## 30. Versioning

Each dataset has:

- schemaVersion: structural compatibility;
- contentVersion: content release;
- generatedAt only in generated manifests where reproducibility permits;
- source snapshot versions;
- generator version.

Rules:

- schema-breaking change increments schemaVersion;
- text correction can increment contentVersion/revision without changing stable ID;
- deprecated IDs remain resolvable for Learning Profile migration;
- generated artifacts include generator/source fingerprints;
- child adapters declare supported schema ranges.

## 31. Attribution output

Generate both machine and human views.

Machine:

~~~
shared/attribution/english-content/manifest.json
~~~

Human:

~~~
shared/attribution/english-content/README.md
~~~

Include:

- dataset;
- source URL;
- snapshot/version;
- license;
- attribution text;
- modification notice;
- affected shards/record counts;
- special obligations.

Do not rely on one global README if record-level licenses differ materially.

## 32. Performance

Requirements:

- no preload of 18k legacy lookup when a compact reference already gives key+level;
- no preload of 100k sentence corpus;
- fetch manifest first, then only relevant shards;
- parent caches resolved shards with bounded memory;
- static Play mode paths must work without a development API;
- generate small topic→shard and entity→shard indexes;
- cache invalidation keyed by contentVersion;
- gzip/brotli from web server where available;
- measure mobile/older-device behavior;
- do not solve performance by deleting learning features.

Large local review/profile lists remain paginated as already implemented in Shared Learning.

## 33. Test strategy

### 33.1 Schema tests

For every dataset:

- valid fixture;
- missing required field;
- unknown enum;
- duplicate ID;
- invalid reference;
- unsupported schemaVersion.

### 33.2 Referential integrity

CI verifies:

- grammar topic refs exist;
- sentence target refs exist;
- exercise source sentence refs exist;
- curriculum prerequisites exist;
- no prerequisite cycles;
- phrase/example refs resolve;
- deprecated IDs have migration aliases where required.

### 33.3 Content invariants

Examples:

- every published grammar topic has unique objective;
- every published cloze target is present exactly where expected;
- sentence-building accepted answers are non-empty and normalized-unique;
- translation pair has at least one accepted target;
- separable phrasal verb metadata is internally consistent;
- no published record has unknown provenance/license.

### 33.4 Compatibility tests

Freeze legacy fixtures for:

- vocabulary level v1;
- vocabulary index/lookup;
- current topic/POS/grammar compatibility views;
- child loader behavior.

New generator changes must not alter legacy content unless a separate reviewed vocabulary change explicitly intends it.

### 33.5 Game tests

Monkeytype:
- adapter parsing;
- accepted answers;
- grammar/sentence event IDs;
- Vietnamese IME regression;
- no normal typing regression.

Shooter/Recall/Space:
- phrase targets;
- bounded review datasets;
- old vocabulary modes unchanged.

Karaoke:
- stable sentence IDs;
- legacy text-ID fallback;
- listening/replay event compatibility.

### 33.6 Scale tests

Synthetic tests:

- 100k sentence manifest;
- thousands of phrase records;
- random-access shard lookup;
- bounded memory/cache;
- no full-corpus browser parse on startup.

## 34. Coverage dashboards

Generated coverage report should show:

- topics by CEFR;
- examples/topic;
- exercises/topic/type;
- contexts per topic;
- grammar targets with no sentence;
- lexemes with no senses;
- senses with no Vietnamese explanation;
- phrasal verbs without separability metadata;
- collocations without examples;
- records by quality state;
- records by source/license;
- duplicate/near-duplicate queue;
- CEFR outlier queue.

Targets are not acceptance by raw count alone.

## 35. Migration compatibility

### 35.1 Legacy vocabulary

No migration required for current games.

shared/vocabulary stays authoritative for EN/VI/IPA targets.

### 35.2 Existing broad grammar index

Keep current shared/vocabulary/grammar/index.json for old selectors.

Later, generate a compatibility view mapping broad modules to new grammar topic IDs/lexical signals. Do not change current child parsers until their adapters support the new manifest.

### 35.3 Existing learning profile

Existing vocabulary entity IDs remain normalized phrase keys.

Existing grammar IDs such as time.present remain valid historical IDs. New detailed gr.* IDs are added, not retroactively substituted into old attempts.

Optional migration/aliasing can group old broad records into reporting categories, but must not fabricate attempts for detailed topics the user never practiced.

### 35.4 Existing sentence IDs

Where legacy games emitted sentence text as ID, keep those records readable. New canonical shared sentences use sent.* IDs.

Do not silently merge two different sentences because normalized text happens to match if provenance/context or revision semantics matter.

## 36. Implementation phases and milestones

### Phase E00 — Master plan

Deliverable:
- this document;
- exact 300-topic taxonomy;
- architecture/license/compatibility decisions.

Exit:
- self-review passes;
- no bulk content generation started.

### Phase E01 — Contracts and scaffolding

Create:
- directory skeleton;
- JSON schemas;
- ID allocator;
- manifests;
- source-manifest schema;
- common normalization library;
- pnpm command stubs.

Exit:
- fixtures validate;
- legacy vocabulary unchanged.

### Phase E02 — Validation and license gates

Implement:
- schema validator;
- provenance/license validator;
- exact/near dedup;
- reference integrity;
- quality-state rules;
- coverage report.

Exit:
- CI can reject unpublishable records before large generation begins.

### Phase E03 — Lexical enrichment pilot

Pilot 300-500 carefully selected legacy keys across A1-B2.

Include:
- multiple senses;
- POS;
- morphology;
- usage;
- Vietnamese sense explanations;
- examples.

Purpose: prove joins and UI needs, not maximize count.

### Phase E04 — Phrase/pattern pilot

Pilot:
- 100 collocations;
- 50 verb patterns;
- 50 phrasal verbs;
- 50 chunks/idioms;
- common prepositions.

Exit:
- metadata supports separability/register/sense differences;
- at least Monkey/Recall can resolve phrase targets.

### Phase E05 — Grammar topic contract pilot

Fully author 2-3 representative topics per CEFR, including:
- easy form-heavy A1/A2;
- aspect contrast B1/B2;
- discourse/register C1/C2.

Do not author all 300 until lesson schema proves usable.

### Phase E06 — Sentence/exercise pilot

Generate and review a manageable pilot, e.g.:
- 1,000 examples;
- 300 translations;
- 300 cloze;
- 100 corrections;
- 100 transformations;
- 100 dialogues.

Use this to tune validation thresholds and shard sizes.

### Phase E07 — Parent content library and adapters

Implement:
- manifests;
- shard loader/cache;
- query API;
- capability routing;
- review-item resolver.

### Phase E08 — Monkeytype rich-content integration

Ship:
- grammar lesson entry;
- corpus-backed cloze;
- sentence builder adapter;
- translation;
- correction/transformation;
- listening sentence mode;
- learning-event IDs.

### Phase E09 — Recall/Shooter/Karaoke/Space integrations

Add only activity types that fit each game's UX. Reuse parent-produced datasets.

### Phase E10 — Controlled scale-up

Batch by CEFR/category.

Each batch:
1. generate/import candidates;
2. validate;
3. review;
4. publish;
5. coverage report;
6. game smoke tests.

No "generate 100k then clean later".

### Phase E11 — Full corpus targets

Scale toward the long-term counts only after acceptance metrics remain stable.

### Phase E12 — Audit and maintenance

- license audit;
- attribution audit;
- stale source update policy;
- quality sampling;
- deprecated record migration;
- contentVersion release notes.

## 37. Acceptance criteria

Architecture is accepted when:

1. all current vocabulary level files remain byte-for-byte unchanged unless separately approved;
2. rich dictionary content can join to legacy targets without positional IDs;
3. schema/version/provenance/license rules are machine-validated;
4. 300 grammar/usage IDs are unique and distribution is exactly 45/50/60/60/50/35;
5. every topic has a distinct stated objective;
6. sentence storage demonstrably scales without a monolithic 100k JSON;
7. game adapters can request bounded datasets;
8. current Shared Learning remains the only canonical mastery engine;
9. no proprietary Cambridge content is copied;
10. VerbNet publication is license-gated;
11. Wiktionary/Tatoeba attribution cannot be dropped silently;
12. quality state prevents raw generated candidates from shipping;
13. exact and near-duplicate checks exist;
14. Vietnamese translation review method is recorded;
15. target-structure validation exists;
16. legacy child modes continue passing tests/builds.

A scaled dataset is accepted only when:

- published records pass required checks;
- random QA meets an agreed error threshold;
- coverage targets are met without template spam;
- attribution manifests are complete;
- performance remains acceptable in static Play mode.

## 38. Self-review of this plan


### 38.0 Mechanical audit performed after the first plan commit

The committed plan was re-read from GitHub and mechanically audited before finalization:

- curriculum rows found: 300;
- A1/A2/B1/B2/C1/C2 counts: 45/50/60/60/50/35;
- duplicate topic IDs: 0;
- duplicate normalized titles: 0;
- duplicate normalized learning objectives: 0;
- required master-plan sections from the task: all present.

Similarity review deliberately examined expected close pairs such as:

- B1 Present Perfect Simple vs Continuous vs B2 nuanced perfect aspect;
- A2 basic defining relatives vs B1 fuller defining relatives;
- A2 basic phrasal object position vs B1 separability;
- A2 may/might possibility vs B1 graded modal possibility.

These are retained because the learning decisions differ and the later topics deepen the earlier objectives. During authoring, prerequisite/contrast metadata and example overlap reports must prove that progression remains real rather than becoming duplicated content.

### 38.1 Missing categories

Reviewed categories:

- senses/definitions/relations;
- POS/morphology/forms;
- usage/register/context;
- collocations;
- verb patterns/prepositions;
- phrasal verbs;
- idioms/chunks;
- grammar/sentence structures;
- mistakes;
- examples/dialogues;
- translation;
- cloze;
- correction;
- transformation;
- building;
- listening;
- attribution/versioning/quality.

No major requested category is intentionally omitted.

### 38.2 Artificial topic splitting

Review result: acceptable with one explicit exception policy.

A1 necessarily separates some positive/negative/question mechanics because these are independent beginner production objectives. At higher levels, topics are split by meaning/use/contrast rather than merely sentence polarity.

Present Perfect is deliberately distributed by objective: experience, recent result, ever/never, already/yet, just, since/for, past-simple contrast, unfinished time, repetition, simple-vs-continuous and higher-level aspect nuance. Each changes the learner's decision, not merely the heading.

### 38.3 Overlap

Expected overlaps are encoded as prerequisites/contrasts.

Potential overlap clusters requiring extra authoring discipline:

- articles across A1-A2-B1-B2-C1-C2;
- future forms across A1-C1;
- conditionals B1-C2;
- participle/reduced clauses B2-C2;
- prepositions/collocations B1-C2;
- spoken/formal register B2-C2.

Validator should report title/objective similarity and authors must explain intentional progression.

### 38.4 CEFR plausibility

The distribution intentionally introduces concrete forms early and moves toward aspect nuance, information structure, register and ambiguity at C levels.

CEFR is not claimed to exactly reproduce Cambridge EGP. Cambridge is a reference only. Pilot authoring must recalibrate individual topics if controlled examples show the level is unrealistic.

### 38.5 Scale

The schema scales to 100k+ sentences because:
- sentences/exercises are separate from grammar topic bodies;
- records are sharded;
- manifests/indexes enable bounded fetch;
- rich authoring and compact runtime views are separated.

### 38.6 Legacy impact

No legacy vocabulary schema change is required. Existing loaders can continue unchanged while new consumers are introduced incrementally.

### 38.7 License risk

Highest risks:
- ShareAlike/GFDL obligations for Wiktionary-derived content;
- per-record attribution for Tatoeba;
- audio license differences;
- VerbNet redistribution uncertainty;
- Cambridge proprietary terms.

Mitigation: source manifests + publish gates + homogeneous shards where practical + generated attribution.

### 38.8 Shared use across games

Yes. The parent owns canonical content querying/routing; games implement capability adapters. No content corpus is copied into child repos.

## 39. Decisions locked by this plan

1. Keep shared/vocabulary/levels/*.json v1 unchanged.
2. Add rich content as sidecar datasets, not fields on old entries.
3. Use exactly 300 curriculum topics initially.
4. Stable content IDs are independent of text and level positions.
5. Parent owns content query/routing and shared mastery.
6. Child games consume bounded activity-specific datasets.
7. Rich sentence/exercise data is sharded.
8. Candidate generation never equals publication.
9. Provenance/license is first-class data.
10. Cambridge EGP/EVP is reference-only.
11. VerbNet-derived publishing stays disabled until redistribution rights for the chosen source/version are verified.
12. New stable sentence IDs coexist with legacy text-based sentence events.
13. Quality checks store method/status, not misleading booleans alone.
14. Bulk scale-up begins only after schemas and validators pass pilots.

## 40. Current continuation order

The original E01/E02 bootstrap described in earlier revisions is complete. New sessions must **not** restart scaffolding or bulk-generate records merely to increase totals.

Continue in this order:

1. keep the committed schemas, stable-ID registry, provenance/license gates and validation pipeline as the contract;
2. finish editorial alignment/review for candidate E03/E04/E06 batches;
3. promote only digest-bound reviewed slices through the publication ledger;
4. use the `/english` parent launcher and game capability matrix to smoke-test each newly published activity in the child game whose UX fits it;
5. extend E10 controlled batches by CEFR/category only after validation, review, publish and runtime smoke all pass;
6. monitor E11 long-term readiness without treating target counts as completed records;
7. run E12 license/attribution/staleness/sample audits on every release;
8. keep legacy `shared/vocabulary/levels/*.json` unchanged unless a separate compatibility migration is explicitly approved.

The implementation is therefore in **controlled content production/editorial promotion**, not architecture bootstrap.

## 41. Definition of success

The project succeeds when the learner can move from:

"good = tốt; /ɡʊd/"

to a connected learning experience:

- which sense is intended;
- what word class/form is used;
- which words naturally combine with it;
- which grammar pattern fits;
- what mistakes to avoid;
- how it appears in daily/work/travel context;
- how to recognize it in listening;
- how to produce it from Vietnamese;
- how to build/correct/transform a sentence with it;
- and how performance feeds one shared Smart Review profile across the games.

The platform should gain depth without sacrificing the fast typing/game experience or breaking the current 18k library.


---

## 42. Historical implementation checkpoint — early 2026-10-03

Branch: `feature/english-learning-content-system`

Implemented after the original master-plan commit:

- **E00 COMPLETE** — final master plan and exact 300-topic framework.
- **E01 COMPLETE** — executable Draft 2020-12 schema catalog, source/provenance contracts, stable ID registry/allocator, runtime manifests and directory architecture.
- **E02 COMPLETE** — validation, source/license gates, referential integrity, exact/near duplicate infrastructure, semantic cloze/translation source checks, CI integration and reviewed-only publication gate.
- **Machine-readable curriculum COMPLETE** — `content/english/grammar/topic-catalog.json` plus generated `shared/curriculum/a1.json ... c2.json`, exactly 45/50/60/60/50/35.
- **Lexical pilot foundation COMPLETE** — 300 legacy-compatible lexeme seeds with stable `lex.en.*` IDs, all kept in `candidate` state; no invented senses/POS.
- **OEWN import foundation COMPLETE** — official lemma-API importer, review-queue schema and a guard that marks live-API output as unpinned/non-publishable. Pinned 2025 release remains the publication-grade source.
- **E05 pilot authored** — 12 grammar topics, exactly 2 per CEFR, with EN/VI concepts, formulae, usage, examples, prerequisites/contrasts and exercise refs. State remains `draft`.
- **E06 pilot authored** — 36 controlled example sentences + 24 cloze/VI→EN exercises with reference and semantic validation. State remains `draft`.
- **E07 foundation COMPLETE** — parent-side `shared/english-content/query.mjs` lazily loads the 300-topic catalog and one CEFR curriculum at a time.
- **Runtime publication gate COMPLETE** — `pnpm english-content:publish` emits only records whose quality state is exactly `published`. Candidate/draft/reviewed data cannot accidentally ship.

Verification:

- Platform CI #501: PASS after the initial foundation/query work.
- Platform CI #503 correctly rejected five pilot exercises whose source-sentence references did not contain their accepted answers.
- The five data references were corrected; the validator was not weakened.
- Platform CI #504 rich-content and syntax stages passed after the correction; full run status is tracked on draft PR #48.

At that checkpoint, intentionally unfinished work was:

- populate/review the OEWN 300-word enrichment using a release-grade pinned source;
- Wiktionary/Wiktextract morphology/usage import;
- phrase/collocation/verb-pattern pilots;
- promote the 12 grammar/36 sentence/24 exercise pilot records only after grammar, bilingual, naturalness and CEFR review;
- full Monkeytype rich-content UI/executor integration, then suitable integrations for Recall/Shooter/Karaoke/Space;
- controlled batch scale-up toward the long-term corpus targets.

These items are not blockers waiting for architecture decisions. They are the subsequent content-production/integration phases and must use the now-implemented gates rather than bypassing them.


---

## 43. Current implementation checkpoint — 2026-10-03

Branch: `feature/english-learning-content-system`

This section supersedes the historical checkpoint above.

### 43.1 Foundation and contracts

- **E00 COMPLETE** — master plan and exact 300-topic curriculum framework.
- **E01 COMPLETE** — Draft 2020-12 schema catalog, stable IDs, provenance/source contracts, runtime manifests and directory architecture.
- **E02 COMPLETE** — schema/reference validation, license gates, exact/near dedup infrastructure, semantic exercise checks and reviewed-only publication gate.
- **Curriculum framework COMPLETE** — exactly 300 machine-readable topics with distribution A1/A2/B1/B2/C1/C2 = 45/50/60/60/50/35.
- Legacy `shared/vocabulary/levels/*.json` remains the compatibility ABI; rich content is sidecar data.

### 43.2 E03 lexical enrichment pilot

Pipeline status: **IMPLEMENTED; EDITORIAL ALIGNMENT PENDING**.

- 300/300 lexeme seeds map to pinned Open English WordNet.
- 3,334 OEWN senses imported; 3,334/3,334 have English definitions.
- 294/300 pilot lexemes also map to pinned Vietnamese Wiktionary English entries.
- Vietnamese Wiktionary pilot contains 2,779 candidate Vietnamese sense glosses and 274/300 records with IPA.
- Simple English Wiktionary/Wiktextract morphology/usage pilot maps 300/300 lexemes: 522 POS entries, 1,512 forms, 1,151 senses, 290/300 with forms, 193/300 with usage labels and 298/300 with IPA. The raw source is pinned by SHA-256 `ea4342525a35eb32e70f5d9945398f06d4f6160af25b0c340fc84662d27efcdf`.
- Bilingual sense-alignment packet contains 300 records; 294 have both sources and POS overlap.
- OEWN uses immutable Git commit `dc343f2683279ecbb13fab4e2fd778d7b162d287`.
- Vietnamese Wiktionary source bytes are pinned by SHA-256.
- Sense alignment, bilingual wording, naturalness and CEFR decisions remain `pending`; no source importer is allowed to invent those reviews.

### 43.3 E04 phrase / pattern pilot

Pilot status: **FIRST REVIEWED PHRASE SLICE PUBLISHED**.

- 100 collocations.
- 50 verb patterns.
- 50 phrasal verbs.
- 50 idiom/chunk records.
- All 250 records were reviewed for English form/pattern, Vietnamese meaning/explanation, naturalness, pilot CEFR placement and project-original provenance.
- Review decisions are digest-bound in the shared editorial ledger; source authoring records remain `draft`, while only the reviewed overlay is runtime-published.
- Published phrase runtime now unlocks compatible Collocation/Phrasal/Chunk activities in Recall, Shooter and Space without pretending phrase IDs are vocabulary IDs.

### 43.4 E05 grammar-topic pilot

Pilot status: **FIRST REVIEWED VERTICAL SLICE PUBLISHED**.

- Source authoring files remain `draft` so the original authored records and editorial workflow stay auditable.
- A digest-bound review ledger overlays 72 accepted records and promotes only those reviewed records at publication time.
- Published E05 runtime currently contains 12 rich grammar topics, 36 controlled example sentences and 24 exercises.
- The 12 grammar topics remain exactly 2 per CEFR level and include EN/VI concepts, formulae, forms, contrasts/prerequisites, examples and exercise references.
- All 72 publication decisions have completed grammar/naturalness/target/CEFR/license checks; translation is either `pass` or explicitly `not-applicable`.
- The full 300-topic framework is still the curriculum/taxonomy; only the reviewed 12-topic body slice is runtime-published.

### 43.5 E06 sentence / exercise pilot

Pipeline status: **TARGET PILOT COUNTS IMPLEMENTED; REVIEW PENDING**.

Current deterministic/reproducible candidate outputs:

- 1,000 example sentences derived from existing project typing texts.
- 300 cloze exercises.
- 300 EN↔VI Tatoeba translation exercises from 16,267 filtered source candidates; all three source files are checksum-pinned.
- 100 controlled error-correction exercises.
- 100 controlled sentence-transformation exercises.
- 100 MultiWOZ 2.2 human-human dialogues selected from 124 candidates after quality filters; both source blobs are pinned.
- 100 common-mistake candidates derived from the controlled correction pilot rather than from random artificial errors.

Candidate/draft records are not runtime-published.

### 43.6 E07 parent runtime

Status: **COMPLETE FOR CURRENT ARCHITECTURE**.

- bounded runtime routes under `/english-content/{curriculum,dictionary,grammar,sentences,phrases,attribution}`;
- shard loader/cache;
- curriculum/query API;
- capability routing;
- review-item resolver;
- published-record adapters;
- parent-to-child rich activity dataset contract.

The entire `shared/` tree is not publicly exposed.

The first published runtime slice is now non-empty: `shared/grammar` contains 12 topics and `shared/sentences` contains 36 examples + 24 exercises. Dictionary runtime remains empty until lexical sense alignment passes its editorial gate. Phrase runtime is now non-empty after the reviewed E04 promotion.

### 43.7 E08 Monkeytype

Status: **INTEGRATED AND CHILD CI GREEN**.

Implemented modes/adapters:

- grammar lesson;
- corpus-backed Context Cloze with legacy fallback;
- Sentence Builder with published-content fallback;
- Vietnamese → English translation;
- error correction;
- sentence transformation;
- sentence listening;
- stable grammar/sentence learning events feeding Shared Learning.

The integration was repeatedly rebased/synced with the Vietnamese IME fixes so English-content work does not overwrite the separate IME workstream.

### 43.8 E09 Recall / Shooter / Karaoke / Space

Status: **END-TO-END INTEGRATED; CHILD/PARENT CI VERIFIED**.

The parent emits bounded `typing-game:english-content:v1:activity-dataset` messages and now owns the complete runtime launch path:

- `shared/english-content/activity-source.mjs` maps activity types to bounded **published-only** runtime shards;
- `shared/english-content/game-adapters.mjs` converts canonical records into game-safe activity items;
- the portal exposes an **English Practice** route at `/english`;
- the route reports published availability, disables empty/unreviewed activities, lets the learner choose 5/10/20/40/100 items and posts the dataset to the selected child iframe;
- ready/error acknowledgements use the existing parent/child lifecycle; candidate/draft data is never substituted when an activity has zero published records.

Capability routing remains game-specific:

- Recall: vocabulary, collocation, phrasal verb, chunk, listening typing, contextual usage.
- Vocabulary Shooter: vocabulary, collocation, phrasal verb, chunk, contextual usage.
- Karaoke: example typing, dialogue, listening typing, translation.
- Space: vocabulary, collocation, phrasal verb, chunk, grammar challenge, contextual usage.

Recall, Shooter and Karaoke are pinned to their rich-activity child commits. Space is applied on a **clean branch based on the exact parent gitlink** so unrelated Duel/BGV work is not pulled into this content integration.

Results still write only the canonical Shared Learning entity families `vocabulary | grammar | sentence`; child games do not own separate mastery engines.

### 43.9 E10 controlled scale-up

Status: **FOUNDATION COMPLETE; CI VERIFIED**.

`content/english/batches/manifest.json` now enforces per batch:

1. exact expected counts;
2. generated vs committed record sets;
3. allowed quality states;
4. required quality-check presence;
5. publication readiness;
6. cross-game smoke tests.

A batch marked `published` cannot contain non-published records or unfinished `pending/fail` checks. Mixed record sets can declare a smoke `recordType`, so cloze/translation samples are selected from the compatible exercise subtype rather than arbitrary file order.

The current controlled E03-E06 manifest accounts for 3,522 authoring/candidate records: 3,200 candidate + 322 draft. E05 publication is represented by the review ledger/runtime overlay rather than mutating the authoring source state.

### 43.10 E11 long-term readiness

Status: **TARGET CONTRACT + READINESS REPORT COMPLETE; BULK CORPUS NOT CLAIMED COMPLETE**.

Locked readiness measurements before the common-mistake addition:

- grammar topics: 300 / minimum 300 (framework target reached);
- verb patterns: 50 / 500 minimum;
- collocations: 100 / 5,000 minimum;
- phrasal verbs: 50 / 1,000 minimum;
- idioms/chunks: 50 / 2,000 minimum;
- common mistakes: 0 / 2,000 minimum (now an additional 100-record candidate pilot is implemented);
- example sentences: 1,000 / 100,000 minimum;
- translation pairs: 300 / 20,000 minimum;
- cloze exercises: 300 / 30,000 minimum;
- transformations: 100 / 10,000 minimum;
- dialogues: 100 / 10,000 minimum.

These numbers intentionally expose what is not yet scaled. E11 does not allow target counts to be treated as completed work.

### 43.11 E12 audit and maintenance

Status: **FOUNDATION COMPLETE; CI VERIFIED**.

Implemented:

- centralized `contentVersion`;
- generated release note contract;
- source/license/attribution maintenance audit;
- explicit deprecation/replacement map with cycle detection;
- source update policy forbidding silent refreshes;
- deterministic hash-based QA sample queue;
- runtime/attribution version consistency checks.

The rich runtime now contains the reviewed E05 and E04 slices: 12 grammar records + 60 sentence/exercise records + 250 phrase/pattern records = 322 published rich records. Dictionary runtime remains zero while E03 lexical sense alignment is pending. The attribution runtime remains zero because every currently published E05 record is `project-original`; the E12 audit now derives attribution requirements from provenance of the records actually published, not merely from the existence of third-party sources in the source catalog.

### 43.12 Verified CI checkpoints

Important green platform runs:

- #530 — full E03/E06 source pipelines and validation after MultiWOZ fixture correction.
- #533 — E09 parent + all pinned child integrations.
- #534 — E10 controlled batches and cross-game smoke tests.
- #535 — E11 readiness target/report pipeline.
- #536 — E12 release/audit/sample maintenance pipeline.
- #548 — E10 typed smoke filtering, editorial review ledger, rich-content validation and E12 maintenance gates all passed together before first publication.
- #549 — attribution audit based on actual published provenance passed before the E05 promotion.
- #554 — E04 publication-license gate plus the current E03-E12 pipeline passed together.
- #555 — published activity-source routing and adapter tests passed.
- #556 — English Practice portal launcher, runtime routing, full content pipelines and Portal build passed together.

Child repositories also passed their relevant CI after E09 integration, including the Monkeytype branch after synchronization with later Vietnamese IME fixes. A dedicated committed-runtime smoke now verifies the first published E05 shards and cross-game adapters in CI.

### 43.13 What remains intentionally unfinished

The architecture, parent launcher and child integrations are no longer waiting for design decisions. Remaining work is primarily **content production and editorial promotion**:

- review/align OEWN ↔ Vietnamese Wiktionary senses for the 300 lexical pilot;
- independently review grammar, Vietnamese wording, naturalness and CEFR for E04 phrase/pattern records and E06 candidate corpora;
- continue promotion in small reviewed slices; E05 has completed the first 72-record `reviewed → published` vertical slice;
- expand E10 batches gradually by CEFR/category;
- grow the E11 counts toward the long-term targets only while QA error rates and game smoke tests remain stable;
- add further source-specific importers only after license/provenance rules are pinned.

The project must not bulk-generate 100k records merely to raise readiness percentages.
