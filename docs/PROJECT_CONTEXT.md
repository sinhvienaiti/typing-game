# Typing Game Local Platform - Project Context and Handoff

## Purpose

This document is the persistent source of truth for the local typing-game platform.

It is intentionally written so that a new ChatGPT tab, another AI assistant, or a developer can read it and understand:

- why the project exists,
- which requirements have already been agreed,
- how the repositories are separated,
- how the local domains work,
- how development and daily Play mode work,
- what Monkeytype has been customized to do,
- what Vocabulary Shooter must do,
- which bugs have already been diagnosed,
- which implementation rules should not be changed without an explicit user request.

The chronological engineering history is kept separately under:

~~~text
docs/changelog/
~~~

The latest user confirmation on 2026-09-19 was that both Monkeytype and Vocabulary Shooter appeared to be working after the integration fixes.

---

# 1. User goal

The user wants a local platform containing multiple typing and English-learning games.

The main public local domain is:

~~~text
https://typing-game.local
~~~

Current public routes:

~~~text
https://typing-game.local/
https://typing-game.local/monkeytype
https://typing-game.local/vocab-shooter
~~~

The homepage is a styled Game Library.

Every game page must keep a small horizontal global navigation so the user can move between games easily.

Concept:

~~~text
[ Home ] [ Monkeytype ] [ Vocabulary Shooter ] [ future game ... ]
~~~

The navigation belongs to the Portal, not to each child game.

---

# 2. Core architecture rules

The architecture has been explicitly agreed.

## 2.1 One game equals one repository

Do not mix the source of different games together.

The parent platform repository must not become a giant monorepo containing the actual implementation of all games.

The permanent rule is:

~~~text
typing-game
= platform only

monkeytype
= game repository

vocab-shooter
= game repository

future game
= new independent repository
~~~

The platform connects game repositories with Git submodules.

## 2.2 Git is the source of truth

The initial bootstrap briefly used ZIP files, but the user explicitly rejected that as the long-term workflow.

Do not return to ZIP-based source delivery for normal development.

Normal workflow:

~~~text
child repo change
→ commit child repo
→ update submodule pointer in typing-game
→ commit typing-game
→ user pulls parent and updates submodules
~~~

## 2.3 Do not silently change the domain

The user explicitly wants .local.

Do not replace it with .test unless the user asks.

## 2.4 Keep the solution local-first

This project is for local use.

Do not introduce PHP, MariaDB, cloud storage, authentication services, or a backend merely to store local vocabulary/settings unless there is a real requirement.

## 2.5 Performance is a first-class requirement

The user explicitly wants the site and games to remain smooth.

For animation-heavy games, input responsiveness and stable frame time are more important than adding more visual effects.

---

# 3. Repositories

## 3.1 Platform

Repository:

~~~text
https://github.com/sinhvienaiti/typing-game
~~~

Branch:

~~~text
main
~~~

Local path:

~~~text
/Users/jokerit/htdocs/typing-game
~~~

Responsibilities:

- Portal homepage.
- Game Library.
- Global navigation.
- Browser-facing route management.
- Game registry.
- nginx dev configuration.
- nginx static Play configuration.
- bootstrap/setup scripts.
- Git submodule pointers.
- shared platform documentation.
- genuinely shared contracts/assets only when required.

## 3.2 Monkeytype

Repository:

~~~text
https://github.com/sinhvienaiti/monkeytype
~~~

Custom branch:

~~~text
feature/en-vn-translation
~~~

Monkeytype remains a fork because future synchronization with official Monkeytype may still matter.

Do not move Monkeytype's source into the platform repo.

## 3.3 Vocabulary Shooter

Repository:

~~~text
https://github.com/sinhvienaiti/vocab-shooter
~~~

Branch:

~~~text
main
~~~

Vocabulary Shooter is a standalone repository, not a fork.

TypeEmUp was used as an open-source reference/base for some ideas. Its MIT attribution is retained in the Shooter repository.

---

# 4. Parent repository layout

Expected structure:

~~~text
typing-game/
├── .git/
├── .gitmodules
├── .nvmrc
├── .gitignore
├── package.json
├── README.md
│
├── docs/
│   ├── PROJECT_CONTEXT.md
│   └── changelog/
│       ├── README.md
│       └── YYYY-MM-DD.md
│
├── portal/
│   ├── index.html
│   ├── package.json
│   ├── pnpm-workspace.yaml
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── public/
│   │   └── games.json
│   └── src/
│       ├── main.ts
│       └── styles.css
│
├── games/
│   ├── monkeytype/        -> Git submodule
│   └── vocab-shooter/     -> Git submodule
│
├── infra/
│   └── nginx/
│       ├── typing-game.local.dev.conf
│       └── typing-game.local.play.conf
│
├── scripts/
│   ├── bootstrap.sh
│   ├── setup-nginx.sh
│   └── play.sh
│
└── shared/
    └── README.md
~~~

---

# 5. Git submodules

Current mapping:

~~~text
games/monkeytype
→ https://github.com/sinhvienaiti/monkeytype.git
→ branch feature/en-vn-translation

games/vocab-shooter
→ https://github.com/sinhvienaiti/vocab-shooter.git
→ branch main
~~~

The parent stores an exact commit pointer for each game.

Correct fresh clone:

~~~bash
cd /Users/jokerit/htdocs

git clone --recurse-submodules   https://github.com/sinhvienaiti/typing-game.git

cd typing-game
~~~

If submodules were not cloned:

~~~bash
git submodule update --init --recursive
~~~

Normal update to the versions pinned by the parent:

~~~bash
git pull
git submodule update --init --recursive
~~~

Do not use submodule --remote automatically unless intentionally moving the platform to a newer child commit.

---

# 6. Local domains and routing

Public user-facing origin:

~~~text
https://typing-game.local
~~~

Internal app origins:

~~~text
https://monkeytype.typing-game.local
https://shooter.typing-game.local
~~~

Reason for internal subdomains:

Monkeytype expects to run from root and uses root-based assets/routes. Keeping Monkeytype on its own internal origin avoids invasive base-path rewrites and keeps upstream maintenance easier.

The user still sees:

~~~text
https://typing-game.local/monkeytype
~~~

The Portal hosts the global navigation and mounts the game in an iframe.

Only the currently selected game iframe should be mounted.

Do not keep all games loaded and hide inactive ones with CSS.

---

# 7. /etc/hosts

Expected local mapping:

~~~text
127.0.0.1 typing-game.local monkeytype.typing-game.local shooter.typing-game.local
~~~

Check:

~~~bash
grep typing-game.local /etc/hosts
~~~

---

# 8. Local HTTPS

mkcert is used.

Certificate paths:

~~~text
/usr/local/etc/nginx/ssl/typing-game.local/typing-game.local.pem
/usr/local/etc/nginx/ssl/typing-game.local/typing-game.local-key.pem
~~~

The certificate covers:

~~~text
typing-game.local
monkeytype.typing-game.local
shooter.typing-game.local
~~~

---

# 9. Portal

The Portal is intentionally lightweight.

Technology:

~~~text
Vite
TypeScript
HTML
CSS
~~~

No React/Vue was needed.

Responsibilities:

- Game Library.
- Game cards.
- Global navigation.
- routing.
- iframe lifecycle.
- reading game metadata.

Dev port:

~~~text
3100
~~~

The registry is stored at:

~~~text
portal/public/games.json
~~~

Current games:

~~~text
Monkeytype
Vocabulary Shooter
~~~

---

# 10. Development ports

Expected:

~~~text
3000 → Monkeytype
3001 → Vocabulary Shooter
3100 → Portal
~~~

Diagnostic:

~~~bash
lsof -nP   -iTCP:3000   -iTCP:3001   -iTCP:3100   -sTCP:LISTEN
~~~

The intended final binding is IPv4 localhost for all three services.

---

# 11. Development commands

Full integration development:

~~~bash
cd /Users/jokerit/htdocs/typing-game

pnpm setup:dev
pnpm dev
~~~

Portal + Monkeytype only:

~~~bash
pnpm setup:dev
pnpm dev:monkeytype
~~~

Portal + Shooter only:

~~~bash
pnpm setup:dev
pnpm dev:shooter
~~~

Use the smaller mode when only one game is being developed to reduce CPU/RAM/watchers.

---

# 12. Daily static Play mode

The user specifically does not want all Vite/Turbo development processes running just to study.

Build static outputs:

~~~bash
pnpm build:local
~~~

Outputs:

~~~text
portal/dist
games/vocab-shooter/dist
games/monkeytype/frontend/dist
~~~

Switch nginx to static Play mode:

~~~bash
pnpm setup:play
~~~

Open:

~~~bash
pnpm play
~~~

If nginx is already running, the user should be able to simply open:

~~~text
https://typing-game.local
~~~

Play mode should not require Vite/Turbo/Node dev servers.

---

# 13. Bootstrap

Command:

~~~bash
nvm use
pnpm bootstrap
~~~

Node/pnpm baseline:

~~~text
Node 24.11.0
pnpm 11.21.0
~~~

Bootstrap responsibilities:

- initialize/update submodules,
- install platform dependencies,
- install Portal,
- install Shooter,
- install Monkeytype,
- create a local Monkeytype Firebase placeholder config if the ignored file is absent.

Successful bootstrap ends with:

~~~text
Bootstrap complete.
~~~

---

# 14. pnpm 11 and esbuild

A setup failure occurred because pnpm 11 blocked the esbuild install/build script.

Observed:

~~~text
ERR_PNPM_IGNORED_BUILDS
Ignored build scripts: esbuild@0.28.2
~~~

The first attempt used an old package.json setting and pnpm warned that it was no longer read there.

The repository was changed to the pnpm 11 workspace configuration using allowBuilds for esbuild.

The desired result is reproducible setup from Git without repeatedly asking the user to manually approve esbuild.

---

# 15. Monkeytype custom EN-VN learning module

The custom branch adds an EN-VN learning layer while preserving normal Monkeytype behavior.

Main module:

~~~text
frontend/src/ts/custom/en-vn-translation/
├── store.ts
├── dictionary.ts
├── index.ts
└── speech.ts
~~~

Feature scope:

~~~text
Config.mode === custom
~~~

The custom feature should not be expanded into a replacement for Monkeytype itself.

---

# 16. Monkeytype dictionary

User can enter mappings such as:

~~~text
cache = bộ nhớ đệm
parent block = block cha
dependency injection = tiêm phụ thuộc
~~~

Supported separators:

~~~text
=
=>
tab
~~~

Behavior:

- NFKC normalization.
- trim.
- English case-insensitive match.
- surrounding punctuation normalization.
- words and phrases.
- later duplicate wins.
- longest phrase support.

---

# 17. Monkeytype trigger rule

Monkeytype and Shooter intentionally use different learning timing.

Monkeytype:

~~~text
user starts typing target
→ reveal learning information immediately
~~~

The trigger is around the first actual typed character of the target.

It does not wait for the entire English target to be completed.

This supports learning while typing.

One occurrence should not repeatedly trigger if the user backspaces/retypes it during the same test attempt.

Restart clears trigger state and cancels speech.

---

# 18. Monkeytype display options

Display mode:

~~~text
tooltip
top
both
~~~

Tooltip behavior:

~~~text
hold
float
~~~

Top display shows the latest/current vocabulary in the space above the typing area.

Held tooltip must stay visually attached to its source word while that word remains visible.

---

# 19. Monkeytype held-tooltip implementation lesson

Appending a tooltip DOM child directly to a Monkeytype word failed because Monkeytype rewrites the word's inner HTML while typing.

Final design:

- keep data/class on the existing word element,
- store translation in dataset,
- render tooltip via CSS pseudo-elements.

This survives normal innerHTML replacement.

Do not revert to child-node tooltip rendering without understanding this issue.

---

# 20. Monkeytype pronunciation

Uses browser Web Speech API:

~~~text
SpeechSynthesis
SpeechSynthesisUtterance
~~~

Settings include:

- pronunciation enabled,
- en-US / en-GB,
- slow / normal / fast,
- volume.

Important rule:

~~~text
speech.cancel()
→ speech.speak(current English)
~~~

This prevents stale queued pronunciation.

Speak the English source, not Vietnamese and not the IPA string.

---

# 21. Monkeytype custom settings storage

LocalStorage key:

~~~text
personalEnVnTranslationSettings
~~~

Settings include:

- enabled,
- dictionary,
- duration,
- popup style,
- popup size,
- popup color,
- display mode,
- tooltip behavior,
- line spacing,
- pronunciation enable,
- pronunciation accent,
- pronunciation rate,
- pronunciation volume.

Standard Monkeytype config uses its own storage.

Storage is origin-specific.

The new Monkeytype origin is:

~~~text
https://monkeytype.typing-game.local
~~~

Settings from older origins do not automatically migrate.

---

# 22. Vocabulary Shooter core learning contract

This rule is mandatory.

Before success:

~~~text
enemy displays English only
~~~

Wrong/incomplete input:

~~~text
no Vietnamese
no IPA
no pronunciation
~~~

Only after the full English target is typed correctly:

~~~text
English pronunciation
→ shot
→ explosion
→ Vietnamese reveal
→ IPA reveal
~~~

Example:

~~~text
dependency injection
→ user completes correctly

then:
tiêm phụ thuộc
/dɪˈpen.dən.si ɪnˈdʒek.ʃən/
~~~

Do not reveal VN or IPA on spawn.

Do not pronounce the word on spawn.

---

# 23. Shooter vocabulary model

Current fields:

~~~text
id
en
vi
ipa
~~~

Example:

~~~text
en  = dependency injection
vi  = tiêm phụ thuộc
ipa = /dɪˈpen.dən.si ɪnˈdʒek.ʃən/
~~~

The UI supports an EN/VI/IPA editor and bulk import.

Bulk example:

~~~text
cache | bộ nhớ đệm | /kæʃ/
parent block | block cha | /ˈper.ənt blɑːk/
dependency injection | tiêm phụ thuộc | /dɪˈpen.dən.si ɪnˈdʒek.ʃən/
~~~

---

# 24. Shooter storage

Vocabulary:

~~~text
IndexedDB
database: typingGameVocabulary
store: entries
~~~

Settings:

~~~text
localStorage
key: vocabShooterSettings
~~~

No backend database is required.

Shooter also supports JSON backup/restore.

---

# 25. Shooter settings

Current concepts:

- pronunciation enabled,
- US/UK accent,
- speech rate,
- volume,
- difficulty,
- reveal duration,
- graphics quality.

Graphics:

~~~text
performance
balanced
quality
~~~

---

# 26. Shooter input behavior

Target selection:

~~~text
no active target
→ first matching typed character
→ lock one enemy
~~~

Then:

~~~text
correct character → advance
wrong character   → error feedback, no reveal
Backspace         → reduce typed progress
Esc               → unlock
~~~

Full completion triggers shot/TTS/reveal.

---

# 27. Shooter rendering/performance

Shooter uses one Canvas.

Main loop:

~~~text
requestAnimationFrame
→ update with clamped delta
→ draw
~~~

Performance measures:

- bounded star count,
- device-pixel-ratio cap,
- bounded particle count,
- graphics quality modes,
- delta clamp,
- hidden-tab pause,
- cancel speech when hidden,
- only one game iframe mounted.

Performance priority:

~~~text
1. responsive typing
2. stable frame rate
3. synchronized audio
4. clear gameplay
5. extra effects afterward
~~~

---

# 28. Shooter text-rendering bug already fixed

Observed problem:

Typing an English target made its visible text shift/disappear incorrectly.

Root cause:

Canvas textAlign state leaked from the idle overlay.

Fix:

- set enemy text rendering to left alignment explicitly,
- wrap idle overlay draw state with save/restore.

Do not remove that isolation casually.

---

# 29. Shooter header overflow bug already fixed

The button group could overflow on some iframe widths.

Fix included:

- flexible grid columns,
- min-width zero,
- flex wrapping for actions.

---

# 30. Shooter pronunciation

Uses browser SpeechSynthesis.

Only after full correct input:

~~~text
cancel previous speech
speak entry.en
~~~

Never pronounce the Vietnamese translation or IPA field.

---

# 31. Shooter third-party attribution

TypeEmUp is MIT-licensed reference material.

Shooter retains:

~~~text
THIRD_PARTY_NOTICES.md
third_party/TypeEmUp-LICENSE.txt
~~~

Do not remove required attribution if derived/copied code remains.

The user has not explicitly chosen a final license for all original Shooter code.

---

# 32. Monkeytype reverse-proxy issue history

Several integration failures were diagnosed.

## 32.1 502 from port binding mismatch

At one stage Monkeytype listened on IPv6:

~~~text
[::1]:3000
~~~

while nginx used IPv4:

~~~text
127.0.0.1:3000
~~~

The final target is deterministic IPv4 binding through DEV_HOST.

## 32.2 Vite host rejection

Observed:

~~~text
Blocked request.
This host ("monkeytype.typing-game.local") is not allowed.
~~~

Vite needs the custom host in server.allowedHosts.

## 32.3 Vite environment source

Vite config originally relied only on loadEnv.

The platform variables are supplied as shell environment variables.

The config was changed to merge loadEnv with process.env.

## 32.4 Turbo dropped DEV variables

This was the decisive final blocker.

Monkeytype's Turbo frontend dev task had an environment allowlist.

The platform passed:

~~~text
DEV_HOST
DEV_ALLOWED_HOSTS
DEV_HMR_HOST
DEV_HMR_PROTOCOL
DEV_HMR_CLIENT_PORT
~~~

but Turbo did not forward them.

turbo.json was updated so the frontend dev task forwards all of them.

Current chain:

~~~text
typing-game command
→ Turbo
→ Vite
→ nginx
~~~

All layers must preserve the reverse-proxy configuration.

---

# 33. Current Monkeytype dev environment variables

The parent script passes:

~~~text
SERVER_OPEN=false
DEV_HOST=127.0.0.1
DEV_ALLOWED_HOSTS=monkeytype.typing-game.local
DEV_HMR_HOST=monkeytype.typing-game.local
DEV_HMR_PROTOCOL=wss
DEV_HMR_CLIENT_PORT=443
~~~

Expected result:

- Vite binds 127.0.0.1:3000.
- custom host is allowed.
- HMR uses the HTTPS/WSS public local hostname.

---

# 34. Firebase config issue already handled

Monkeytype ignores:

~~~text
frontend/src/ts/constants/firebase-config.ts
~~~

Fresh clones therefore lacked it and TypeScript complained.

Bootstrap now copies the example config into the ignored local file when necessary.

Do not commit real Firebase secrets.

---

# 35. Useful diagnostics

Ports:

~~~bash
lsof -nP   -iTCP:3000   -iTCP:3001   -iTCP:3100   -sTCP:LISTEN
~~~

Direct:

~~~bash
curl -I http://127.0.0.1:3000
curl -I http://127.0.0.1:3001
curl -I http://127.0.0.1:3100
~~~

Through nginx:

~~~bash
curl -kI https://typing-game.local
curl -kI https://monkeytype.typing-game.local
curl -kI https://shooter.typing-game.local
~~~

Debug order:

~~~text
1. process exists
2. correct port listener
3. direct HTTP
4. nginx upstream
5. Vite host allowlist
6. HMR
7. Turbo env forwarding
~~~

Do not jump directly to random nginx changes.

---

# 36. Local storage separation

Origins are separate, so storage is naturally isolated.

~~~text
typing-game.local
→ Portal storage

monkeytype.typing-game.local
→ Monkeytype storage

shooter.typing-game.local
→ Shooter IndexedDB/localStorage
~~~

This avoids collisions.

Tradeoff:

Vocabulary is not currently shared between Monkeytype and Shooter.

A future shared vocabulary service could be added through the Portal/postMessage if the user asks.

Do not over-engineer this before it is needed.

---

# 37. Adding a future game

Expected process:

~~~text
1. create a new repository
2. provide pnpm dev and pnpm build when practical
3. add it under games/ as a submodule
4. add registry entry
5. add internal local hostname if needed
6. add nginx dev mapping
7. add nginx static mapping
8. update orchestration scripts only if needed
9. commit parent submodule pointer
10. document the change in today's changelog
~~~

For new custom games, prefer static output at:

~~~text
dist/
~~~

Monkeytype remains an exception because upstream has its own command/layout conventions.

---

# 38. Git workflow for future AI/developers

If changing Shooter:

~~~text
commit sinhvienaiti/vocab-shooter main
→ update games/vocab-shooter gitlink in typing-game
→ commit typing-game
~~~

If changing Monkeytype:

~~~text
commit sinhvienaiti/monkeytype feature/en-vn-translation
→ update games/monkeytype gitlink in typing-game
→ commit typing-game
~~~

User local synchronization:

~~~bash
cd /Users/jokerit/htdocs/typing-game

git pull
git submodule update --init --recursive
~~~

Do not ask the user to manually copy files that can be committed through Git.

---

# 39. Changelog policy

The user explicitly requested a durable detailed engineering history.

Folder:

~~~text
docs/changelog/
~~~

Files:

~~~text
README.md
YYYY-MM-DD.md
~~~

Rules:

- one detail file per calendar day,
- append multiple changes from the same date into the same file,
- overview README has one row per meaningful day,
- daily detail should include requirements, design, repos/files, implementation, bugs/root causes, fixes, verification and follow-up,
- child repo work must also record the parent submodule pointer update,
- update docs in Git as part of the work, not as an external ZIP.

---

# 40. Coding style expected by the user

The user prefers:

- simple solutions,
- no unnecessary abstraction,
- no excessive defensive checks,
- verify function input/output before using it,
- reuse existing helpers before creating new ones,
- simple English names,
- consistent coding style,
- avoid over-engineering,
- identify root cause before stacking workarounds,
- verify behavior after changes.

---

# 41. Current baseline

As of the end of 2026-09-19 integration work, the user said both games appeared stable.

Treat the current Git state as the baseline.

If a later regression appears, first inspect the current commits/configuration before reintroducing previously rejected approaches.

---

# 42. Quick prompt for a new chat

A user can attach or point to this document and say:

~~~text
Read docs/PROJECT_CONTEXT.md and the latest files in docs/changelog before changing anything.

Git is the source of truth.
Do not use ZIP updates.
typing-game is the platform repository.
Every game is an independent repository mounted as a submodule.

If you modify a child game, commit the child repo first and then update the submodule pointer in typing-game.

Keep .local.
Keep the Shooter learning rules:
- Classic/Bounce/Time Attack: English only before success; VN + IPA + English TTS after full correct English.
- Target Rush: when the spotlight activates, immediately show VN + IPA in the dedicated top Learning Panel and pronounce the English target. Do not attach VN/IPA to the glowing target itself.

Prefer simple maintainable solutions and protect input responsiveness/performance.
~~~


---

# 43. Cross-game engagement and performance rule

On 2026-09-19 the user expanded the product requirement beyond merely making game mechanics functional.

For Vocabulary Shooter and future games, the expected design process is:

~~~text
learning goal
→ analyze comparable game patterns
→ improve the raw idea
→ add purposeful audio/visual feedback
→ preserve keyboard-first flow
→ define results/metrics
→ define a performance budget
→ implement
~~~

The game must not feel visually flat or mechanically robotic.

At the same time, attractive effects must never be allowed to materially damage typing latency or frame stability.

The permanent cross-game principle is:

~~~text
engaging + attractive + smooth + performant
~~~

Background music, danger feedback and rewarding success effects are now considered part of the desired game experience when appropriate.

Real audio assets must have a clear compatible license and attribution when required.

---

# 44. Vocabulary Shooter multi-mode direction

Vocabulary Shooter is now planned as a multi-mode game.

Confirmed modes/mechanics:

~~~text
Classic Survival
→ current lives/falling-word gameplay becomes one explicit mode

Bounce / Relax
→ words move continuously by velocity
→ wall impact reflects the velocity like billiards
→ no random self-steering during motion
→ configurable maximum active word count
→ exceeding the cap loses the run

Time Attack
→ configurable fixed duration, including 100s
→ no early lives-based game over
→ missed words are counted
→ final results show how many were correct/missed during the window

Target Rush
→ preselect a configurable pool such as 70 words
→ highlight targets on a fixed cadence
→ next target activates even when the old word is unfinished
→ example timing: 3s spotlight + 2s dive
→ unfinished old target dives toward the player during the extra 2s
→ it remains typable during the dive
→ impact with the player ends the run
~~~

Learning timing is mode-specific:

~~~text
Classic Survival / Bounce / Time Attack
→ VN + IPA + English pronunciation only after full correct English

Target Rush
→ when the spotlight target activates:
   show VN large in a dedicated top Learning Panel
   show IPA below it
   pronounce the English target immediately
→ the glowing target itself remains English-only
→ the panel follows the newest spotlight target, not older danger targets
~~~

Shooter also requires a configurable keyboard quick-restart action using Tab or Escape.

Detailed mode behavior, recommended settings, audio design, effects, performance budgets and implementation order are documented in:

~~~text
docs/design/VOCAB_SHOOTER_GAME_MODES.md
~~~

The design document distinguishes confirmed requirements from recommendations that can still be tuned before code implementation.


---

# 45. Target Rush dedicated learning panel

Target Rush intentionally differs from the other Shooter modes.

When a word becomes the active spotlight target:

~~~text
spotlight target activates
→ dedicated top Learning Panel updates
→ Vietnamese meaning is shown large and clear
→ IPA is shown directly below
→ English pronunciation plays immediately
~~~

The Learning Panel must occupy a reserved area above the target field.

It must **not** behave like Monkeytype's per-word tooltip and must **not** place VN/IPA directly on the yellow/glowing target.

The active board target remains English-focused.

When the next target activates, the panel switches immediately to the new word and previous speech is cancelled before speaking the new target.

If the old word enters the danger/dive state, it may remain typable, but it must not take over the top Learning Panel from the new spotlight target.

For Target Rush, success effects should normally not replay the pronunciation because it was already played at spotlight activation.
