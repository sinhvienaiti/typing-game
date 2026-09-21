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
- Commit the completed ten-level batch to GitHub immediately as one batch commit.
- Update this file in that same batch commit with the exact completed range, QA result, next level, and handoff notes. Report the resulting commit SHA after the commit is created.
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

Current batch: 061-070.

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
- Level 021: 15 passages, 4105 words, vocabulary coverage 63.0 percent, duplicate/similarity warnings 0, checkpoint `0ff8cb13b7b0d38abaf70c6fe7330dad5961ac2d`.
- Level 022: 15 passages, 3977 words, vocabulary coverage 72.9 percent, duplicate/similarity warnings 0, checkpoint `ce24aa5a161bb5c371b4b8c9fd34ef1ed5c8161b`.
- Level 023: 15 passages, 3814 words, vocabulary coverage 55.2 percent, duplicate/similarity warnings 0, checkpoint `d345ae13e85980519c1ed0693b31b5466664eb8b`.
- Level 024: 15 passages, 3963 words, vocabulary coverage 57.5 percent, duplicate/similarity warnings 0, checkpoint `b3fd1d3bc2e8b473bbf481ecdd9a08551655bf3b`.
- Level 025: 15 passages, 3813 words, vocabulary coverage 50.3 percent, duplicate/similarity warnings 0, checkpoint `806df72fdba6d0724c5eeeb179d9baa2327682dd`.
- Level 026: 15 passages, 3792 words, vocabulary coverage 45.9 percent, duplicate/similarity warnings 0, checkpoint `8f2b14e22daae8c6c94fb44a4e515f81ee5cdef5`.
- Level 027: 15 passages, 3868 words, vocabulary coverage 56.4 percent, duplicate/similarity warnings 0, checkpoint `2d47c215ca29c0d9cc1e141776f08e8531c3b1bc`.
- Levels 011-027 cross-check: 255 passages, 66173 words, duplicate/similarity warnings 0.
- Level 028: 15 passages, 3952 words, vocabulary coverage 54.1 percent, duplicate/similarity warnings 0, checkpoint `12113fb5650595d5f78c567ac1cb3d390bf76146`.
- Levels 011-028 cross-check: 270 passages, 70125 words, duplicate/similarity warnings 0.
- Level 029: 15 passages, 3809 words, vocabulary coverage 49.2 percent, duplicate/similarity warnings 0, checkpoint `1d3d5431c3e027ec884d9b44ae21c2c18262b59f`.
- Levels 011-029 cross-check: 285 passages, 73934 words, duplicate/similarity warnings 0.
- Level 030: 15 passages, 3810 words, duplicate/similarity warnings 0, checkpoint `30e5dfba55afe6796800e71c46b0696e18b29f2a`.
- Levels 011-030 cross-check: 300 passages, 77744 words, duplicate/similarity warnings 0.
- Level 031: 15 passages, 3885 words, duplicate/similarity warnings 0.
- Level 032: 15 passages, 3855 words, duplicate/similarity warnings 0.
- Level 033: 15 passages, 3930 words, duplicate/similarity warnings 0.
- Level 034: 15 passages, 3855 words, duplicate/similarity warnings 0.
- Level 035: 15 passages, 3804 words, duplicate/similarity warnings 0, checkpoint `8c1f2135ce6770035101ab2c6c1c607b8a90716d`.
- Level 036: 15 passages, 3843 words, duplicate/similarity warnings 0, checkpoint `6e081ef5f40bd18c3ed4cfb75831b92715635ea5`.
- Level 037: 15 passages, 3988 words, duplicate/similarity warnings 0, checkpoint `98db242806a555e73e9626877aafacc2c3ebceab`.
- Level 038: 15 passages, 4071 words, duplicate/similarity warnings 0, checkpoint `e5d277c72792a9a1f9e7214d4df1ffe66a20d85c`.
- Level 039: 15 passages, 4025 words, duplicate/similarity warnings 0, checkpoint `20be79964295953a64c8c4cf925f00240386ff8b`.
- Level 040: 15 passages, 3860 words, duplicate/similarity warnings 0, checkpoint `b6cc693c044675b57d4a77ac3b7de0366ec2181e`.
- Batch 031-040: complete on checkpoint branch.
- Level 041: 15 passages, 3982 words, duplicate/similarity warnings 0, checkpoint `54c6b0c7c2c6401bb6666b57457aadde9f3e071c`.
- Level 042: 15 passages, 3946 words, duplicate/similarity warnings 0, checkpoint `90a0663e539c76fb0820eec26308df56dbb96cdb`.
- Level 043: 15 passages, 3873 words, duplicate/similarity warnings 0, checkpoint `0accb77c67f5f23f8eaf627d086c2c06a89c8486`.
- Level 044: 15 passages, 3963 words, duplicate/similarity warnings 0, checkpoint `a4c49a3e16def9d552150c145329d35ddb66f67f`.
- Level 045: 15 passages, 3990 words, duplicate/similarity warnings 0, checkpoint `b434a0a56880570e66e64b3156917ca4d023e4b4`.
- Level 046: 15 passages, 3923 words, duplicate/similarity warnings 0, checkpoint `cab42debdfba3466e35ef64d5290f756cce73ff5`.
- Level 047: 15 passages, 3898 words, duplicate/similarity warnings 0, checkpoint `2b00d649dbd4bc239340a0f4a2ff72c1fe60e9f2`.
- Level 048: 15 passages, 3851 words, duplicate/similarity warnings 0, checkpoint `d2aa11ebe7fb7340101552d7efd9b9dd7ba694df`.
- Level 049: 15 passages, 3819 words, duplicate/similarity warnings 0, checkpoint `dadb8f42be23c72ff6e3da7e7d5ebe01013e66b5`.
- Level 050: 15 passages, 3826 words, duplicate/similarity warnings 0, checkpoint `f322785797799ea1366f24b40ebb2985220b2f85`.
- Batch 041-050: complete on checkpoint branch, batch QA PASS, 150 passages, 39071 words, duplicate/similarity warnings 0.
- Level 051: 15 passages, 3813 words, duplicate/similarity warnings 0, checkpoint `a41c616136b7cf5bccf129001f446ef4885ae8ce`.
- Level 052: 15 passages, 3916 words, duplicate/similarity warnings 0, checkpoint `7950cb0f4313d3af7c77c80ac1fa9515dc4f7940`.
- Level 053: 15 passages, 3977 words, duplicate/similarity warnings 0, checkpoint `72725263ed058daeb0cccc92cc6d3bc01a6060ed`.
- Level 054: 15 passages, 4051 words, per-level QA PASS, checkpoint `cfc83c03c33484607b10a534296d962ab6881ba1`.
- Level 055: 15 passages, 4110 words, per-level QA PASS, checkpoint `c9fd873259b581f22196bc6b909dc58e960cd1fb`.
- Level 056: 15 passages, 4017 words, per-level QA PASS, checkpoint `2349b327b24edc0677a565eab003c3ae20c42b9d`.
- Level 057: 15 passages, 4049 words, per-level QA PASS.
- Level 058: 15 passages, 3874 words, per-level QA PASS.
- Level 059: 15 passages, 3838 words, per-level QA PASS.
- Level 060: 15 passages, 3851 words, per-level QA PASS.
- Batch 051-060: complete on checkpoint branch, batch QA PASS, 150 passages, 39496 words, duplicate/similarity warnings 0.
- Levels 001-060 index: 60 levels, 900 passages, 234904 words.
- Next active level: 061.
- Main receives each completed 10-level batch: 001-010, 011-020, 021-030, and so on.

If continuing after interruption, trust committed production files on main first, then committed checkpoint files on the corpus branch, then this status file.

## Handoff instructions

When continuing this work in another chat:

1. Read this file first.
2. Read `scripts/typing-text-core.mjs` and `scripts/validate-typing-texts.mjs`.
3. Check the current `main` HEAD and latest Platform CI.
4. Check which `shared/typing-texts/levels/*.json` files are actually committed. Those files override any stale status line in this document.
5. Resume from the first missing or failing level.
6. Do not regenerate already committed passing levels unless QA finds a real defect.
7. Keep the 10-level batch rule. Do not commit individual level files. Prepare and QA all ten levels, then commit the ten level files together with the index and this process file in one batch commit.
8. After each completed 10-level batch commit, report the exact range and immediately continue with the next batch.

## Next action

Batch 051-060 is complete on the checkpoint branch. Continue without stopping from Level 061 in Batch 061-070.

For each level:

1. Create or repair only the current missing or failing level.
2. Run passage and per-level QA before moving on.
3. Do not create a commit for an individual passing level.
4. Keep completed level content prepared for the current ten-level batch.
5. After all ten levels pass, run batch-wide QA and create one batch commit containing all ten level files, the updated index, and this process file.

After all ten levels in the current batch pass per-level and batch-wide QA:

1. Update the typing-text index.
2. Update this process file with the completed range and QA totals.
3. Create one commit for the entire ten-level batch. Do not create per-level commits.
4. Report one concise batch completion status with the commit SHA.
5. Immediately continue with the next ten-level batch.

The permanent batch size is 10 files to reduce loss risk during long runs.
