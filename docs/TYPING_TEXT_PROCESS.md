# Typing Text Corpus Production Process

## Purpose

This file is the source of truth for continuing the leveled typing-text corpus work across chat sessions. Read this file before changing `shared/typing-texts/`.

## Goal

Build production typing passages for Monkeytype Level Passages using the existing shared vocabulary library.

- Levels: 001-100.
- Minimum passages per level: 15.
- Passage length: 250-300 English words.
- Each passage should naturally use roughly 20-30 vocabulary entries from its own level when possible.
- A passage does not need to cover every word in a level.
- Natural readable prose is more important than forcing difficult, sensitive, slang, proper-name, or badly-leveled vocabulary into a passage.
- Topics may cover daily life, nature, school, work, travel, science, culture, community, technology, public services, history, practical situations, stories, and other varied subjects.
- Lower levels should use simpler sentence structure and explanation. Higher levels may become more complex gradually.

## Typing text rules

- Plain English prose only inside `text`.
- Use normal letters, spaces, apostrophes, commas, and periods.
- No headings, bullets, markdown, brackets, slashes, colons, semicolons, dashes, quotation marks, symbols, or decorative characters inside passage text.
- Capitalize sentence starts. Avoid unnecessary capitalization inside sentences.
- Use periods and commas naturally.
- Sentences must connect logically and form one coherent passage.
- Avoid repetitive AI-style openings, conclusions, plots, sentence patterns, and topic structures.
- Avoid copying source text. External reading material is for style/topic reference only.
- Avoid forcing unsuitable vocabulary only to improve a coverage percentage.

## File format

Production files live at:

`shared/typing-texts/levels/NNN.json`

Each level document:

- version: 1
- level: numeric level
- cefr: level band
- passages: 15 or more passage objects

Each passage:

- id: `LNNN-PNNN`
- topic
- style
- setting
- tone
- targetWords
- wordCount
- text

## QA gates per passage

Before a passage is accepted:

1. Word count must be 250-300.
2. `targetWords` must contain at least 20 and at most 30 entries whenever the level naturally supports this.
3. Every target word must belong to that level vocabulary.
4. Every target word must actually occur in the passage.
5. Text must contain only allowed typing characters.
6. Passage must end with a period.
7. Capitalization rule must pass.
8. Readability and topic coherence must be reviewed.
9. No obvious copied or templated sentence sequence.

If a passage fails, fix it and run QA again before moving on.

## QA gates per level

After all passages in one level pass:

1. Validate unique passage ids.
2. Detect duplicate sentences.
3. Detect repeated 8-word phrases.
4. Run 5-gram similarity checks.
5. Review topic/style/setting/tone variety.
6. Calculate target-vocabulary coverage as information, not an absolute pass threshold.
7. Prefer natural writing over artificially maximizing coverage.

## Batch workflow

- Production batch size: 10 level files.
- Batches: 001-010, 011-020, 021-030, 031-040, 041-050, 051-060, 061-070, 071-080, 081-090, 091-100.
- Work level by level.
- Review and repair each level before starting the next.
- After a batch is complete, run batch-wide validation and similarity checks.
- Push the completed batch to GitHub immediately.
- Update this file in the same push with exact completed range, QA result, commit SHA, next level, and handoff notes.
- Report completion to the user, then continue automatically to the next batch unless explicitly told to stop.

## Runtime features already completed

Vocabulary Shooter:

- Random shuffle-bag selection is mandatory.
- Avoid immediate repeat at cycle boundaries.
- Avoid duplicate entries inside one target pool.
- Current reviewed child commit: `d8cc524b746501b77cf95f848ef09c002ed08939`.

Recall Typing:

- Random shuffle-bag selection is mandatory.
- Avoid immediate repeat at cycle boundaries.
- Avoid duplicate words inside one run.
- Current reviewed child commit: `af5eee4416273ec2e7ffd2dca6764a1e5fc5b01d`.

Monkeytype:

- Custom Text and Level Passages are separate sources.
- Level Passages supports level selection and 1-15 passages per session.
- Selected passages use a non-repeating shuffle bag with per-level progress stored locally.
- Only the selected level file is loaded.
- Generated passage sessions keep sentence order and are isolated from Custom Text shuffle and pipe settings.
- Current reviewed child commit: `fb8e59c9425bdc69641190e9da87a1240067b9b6`.

Parent integration commit before corpus production: `189479a457b40ae80090697cd54865df3f92be81`.
Platform CI for that integration passed.

## Corpus production status

Current batch: 001-030.

Completed and self-reviewed but not yet committed as production files at the time this process file was first created:

- Level 001: 15 passages, 3854 words, vocabulary coverage 99.3 percent, duplicate/similarity warnings 0.
- Level 002: 15 passages, 3829 words, vocabulary coverage 99.3 percent, duplicate/similarity warnings 0.
- Level 003: 15 passages, 3786 words, vocabulary coverage 100 percent, duplicate/similarity warnings 0.
- Level 004: 15 passages, 3838 words, safe/natural target coverage 65.7 percent, duplicate/similarity warnings 0.
- Level 005: 15 passages, 3857 words, vocabulary coverage 67.4 percent, duplicate/similarity warnings 0.

Batch size: 10 level files.

Production status on main:

- Batch 001-010: complete and reviewed.
- Level 001: 15 passages.
- Level 002: 15 passages, 3829 words, vocabulary coverage 99.3 percent, duplicate/similarity warnings 0.
- Level 003: 15 passages, 3786 words, vocabulary coverage 100 percent, duplicate/similarity warnings 0.
- Level 004: 15 passages, 3838 words, safe/natural target coverage 65.7 percent, duplicate/similarity warnings 0.
- Level 005: 15 passages, 3857 words, vocabulary coverage 67.4 percent, duplicate/similarity warnings 0.
- Level 006: 15 passages, 3829 words, vocabulary coverage 74.0 percent, duplicate/similarity warnings 0.
- Level 007: 15 passages, 4312 words, vocabulary coverage 65.7 percent, duplicate/similarity warnings 0.
- Level 008: 15 passages, 3987 words, vocabulary coverage 59.7 percent, duplicate/similarity warnings 0.
- Level 009: 15 passages, 4275 words, vocabulary coverage 58.6 percent, duplicate/similarity warnings 0.
- Level 010: 15 passages, 3910 words, vocabulary coverage 56.4 percent, duplicate/similarity warnings 0.

Batch 011-020 production result:

- Production commit: `344dae0235f5d0e6cf4fb53765c7a87566cc6b10`.
- Batch QA: 150 passages, 38841 words, duplicate/similarity warnings 0.
- Level 011: 15 passages, 3870 words, vocabulary coverage 56.4 percent, duplicate/similarity warnings 0.
- Level 012: 15 passages, 3832 words, vocabulary coverage 52.5 percent, duplicate/similarity warnings 0.
- Level 013: 15 passages, 3799 words, vocabulary coverage 65.2 percent, duplicate/similarity warnings 0.
- Level 014: 15 passages, 3846 words, vocabulary coverage 58.6 percent, duplicate/similarity warnings 0.
- Level 015: 15 passages, 3835 words, vocabulary coverage 68.0 percent, duplicate/similarity warnings 0.
- Level 016: 15 passages, 3778 words, vocabulary coverage 68.5 percent, duplicate/similarity warnings 0.
- Level 017: 15 passages, 4099 words, vocabulary coverage 49.7 percent, duplicate/similarity warnings 0.
- Level 018: 15 passages, 3980 words, vocabulary coverage 58.0 percent, duplicate/similarity warnings 0.
- Level 019: 15 passages, 3833 words, vocabulary coverage 61.3 percent, duplicate/similarity warnings 0.
- Level 020: 15 passages, 3969 words, vocabulary coverage 72.9 percent, duplicate/similarity warnings 0.
- Index after Batch 011-020: 20 levels, 300 passages, 78318 words.

Checkpoint branch: `feature/typing-text-corpus`.

- Levels 011-020 are complete and reviewed.
- Next active level: 021.
- Main receives each completed 10-level batch: 001-010, 011-020, 021-030, and so on.

If continuing after interruption, trust committed production files on main first, then committed checkpoint files on the corpus branch, then this status file.

## Handoff instructions

When continuing this work in another chat:

1. Read this file first.
2. Read `docs/design/TYPING_TEXT_CORPUS_PLAN.md`.
3. Read `scripts/typing-text-core.mjs`, `scripts/validate-typing-texts.mjs`, and `scripts/generate-typing-text-index.mjs`.
4. Check the current `main` HEAD and latest Platform CI.
5. Check which `shared/typing-texts/levels/*.json` files are actually committed. Those files override any stale status line in this document.
6. Resume from the first missing or failing level.
7. Do not regenerate already committed passing levels unless QA finds a real defect.
8. Keep the 10-level batch rule and update this file in every completed batch push.
9. After each completed 10-level batch push, report the exact range and immediately continue with the next batch.

## Next action

Continue Batch 021-030 without stopping, starting exactly from Level 021.

For each level:

1. Create or repair only the current missing or failing level.
2. Run passage and per-level QA before moving on.
3. Commit the passing level to `feature/typing-text-corpus` as a checkpoint.
4. Update this process file often enough that the next active level is unambiguous.

After Levels 021-030 all pass per-level and batch-wide QA:

1. Push Batch 021-030 to main.
2. Update the typing-text index.
3. Update this process file with the production commit and QA totals.
4. Report one concise line that Batch 021-030 is complete.
5. Immediately continue with Batch 031-040.

The permanent batch size is 10 files to reduce loss risk during long runs.
