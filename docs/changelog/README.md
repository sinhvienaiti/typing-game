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
| 2026-09-20 | Refined Monkeytype EN-VN/Recall UI and local text reading, added flexible Stop-on-Error scoring/retained-error options, polished Shooter with a border-free VN reveal and animated red active-target marker, improved Shooter/Recall restart UX, added static `./play.sh`, fixed macOS Bash 3.2 cleanup, and completed multi-pass review/CI. | [2026-09-20](./2026-09-20.md) |
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
~~~

## Current local root

~~~text
/Users/jokerit/htdocs/typing-game
~~~

## Current entry point

~~~text
https://typing-game.local
~~~
