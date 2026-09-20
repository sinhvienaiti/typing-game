# Shared Typing Text Library

Status: infrastructure ready; production passage generation has not started.

Source of truth:

~~~text
shared/typing-texts/levels/001.json
...
shared/typing-texts/levels/100.json
~~~

Runtime index:

~~~text
shared/typing-texts/index.json
~~~

Commands:

~~~bash
pnpm typing-texts:validate
pnpm typing-texts:generate
pnpm typing-texts:report
~~~

Production requirements are defined in:

~~~text
docs/design/LEVELED_TYPING_TEXT_LIBRARY.md
~~~

A committed level file must contain at least 15 fully reviewed passages. Partial level files must not be pushed to main.

Current runtime state intentionally has zero production levels until Level 001 completes the full content QA gate.
