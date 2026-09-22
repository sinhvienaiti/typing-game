# Typing Game - Change Log Overview

This folder is the chronological engineering history of the typing-game platform.

## Rules for future updates

- Create or update exactly one detail file per calendar day using YYYY-MM-DD.md.
- Do not create a new file for every small commit on the same day. Append work to that day's file.
- README.md is the compact index. Every meaningful engineering day gets one row.
- A daily detail file should explain:
  - what was requested,
  - decisions that were made,
  - repositories/files changed,
  - implementation details,
  - bugs and root causes,
  - fixes,
  - commands/setup changes,
  - verification/current status,
  - remaining caveats/follow-up.
- If a child game repo changes, record both the child change and the typing-game submodule pointer update.
- Git is the source of truth. Do not return to ZIP-based source delivery.
- docs/PROJECT_CONTEXT.md describes the current state; the daily changelog records how the state evolved.

## Daily index

| Date | Main work completed | Detail |
| --- | --- | --- |
| 2026-09-22 | Advanced Space Typing through the post-Step-68 checkpoint, refreshed the parent submodule pin, fixed Space-origin shared vocabulary/typing-text routing, and added a Platform CI integration contract that preserves existing game routes. | [2026-09-22](./2026-09-22.md) |
| 2026-09-21 | Fixed rapid consecutive pronunciation loss across Shooter, Recall and Monkeytype EN-VN by queueing browser speech instead of cancelling the active utterance before each word; added regression coverage and updated platform submodule pointers. | [2026-09-21](./2026-09-21.md) |
| 2026-09-20 | Added the shared EN-VN-IPA vocabulary architecture, expanded the reviewed foundation to 450 entries, then completed a validated 18,000-entry/100-level production library using pinned wordfreq ranking, SCOWL lexical filtering, CEFR anchoring and trusted EN-VN/IPA enrichment; also added source/license attribution, Library/Custom dictionary source for Monkeytype, Class/Custom level sources for Shooter and Recall, validator/schema hardening, plus the earlier EN-VN/Recall UI, Stop-on-Error, Shooter visual, restart and static Play-mode refinements; also documented the approved leveled typing-text corpus and random non-repeating practice plan for Shooter, Recall and Monkeytype; added the independent Karaoke Typing game with YouTube/local media, synchronized LRC gameplay, four modes and isolated platform integration. | [2026-09-20](./2026-09-20.md) |
| 2026-09-19 | Established the multi-game local platform and submodule architecture; fixed local nginx/Vite/Turbo setup; implemented and CI-reviewed Shooter Classic/Bounce/Time Attack/Target Rush; added offline-first rules and Monkeytype corrected-error accuracy forgiveness; separated Recall Typing into its own game and completed its review/test pass; added Platform CI; hardened stale dev-port cleanup; and added an executable `./dev.sh` launcher for pull/bootstrap/nginx/start with all or focused-game targets. | [2026-09-19](./2026-09-19.md) |

## Current repositories

~~~text
Platform:
sinhvienaiti/typing-game
branch main

Monkeytype:
sinhvienaiti/monkeytype
branch feature/en-vn-translation

Vocabulary Shooter:
sinhvienaiti/vocab-shooter
branch main

Recall Typing:
sinhvienaiti/recall-typing
branch main

Karaoke Typing:
sinhvienaiti/karaoke-typing
branch main

Space Typing:
sinhvienaiti/space-typing
branch main
~~~

## Current local root

~~~text
/Users/jokerit/htdocs/typing-game
~~~

## Current entry point

~~~text
https://typing-game.local
~~~
