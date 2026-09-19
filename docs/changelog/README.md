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
| 2026-09-19 | Established the multi-game local platform; created the parent/submodule Git structure; implemented Portal, .local routing, dev/play modes and Shooter MVP; documented Monkeytype EN-VN behavior; fixed pnpm 11/esbuild, Shooter Canvas text/header issues, and Monkeytype nginx/Vite/Turbo reverse-proxy problems. | [2026-09-19](./2026-09-19.md) |

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
~~~

## Current local root

~~~text
/Users/jokerit/htdocs/typing-game
~~~

## Current entry point

~~~text
https://typing-game.local
~~~
