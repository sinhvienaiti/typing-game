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


---

# 46. Offline-first core gameplay rule

Core gameplay for every game in this platform must remain playable offline after the project has been installed/built locally.

Permanent rule:

~~~text
core gameplay
→ must work offline

online services
→ optional enhancement only
→ must not be required to start or finish the main learning/game loop
~~~

Current implications:

~~~text
Portal
→ local nginx/static files

Vocabulary Shooter
→ local static frontend
→ IndexedDB/localStorage
→ procedural local audio/SFX
→ browser/system SpeechSynthesis

Monkeytype custom local typing
→ local frontend/static build
→ custom EN-VN settings in localStorage
~~~

Some original Monkeytype account/cloud/leaderboard features can still require network access. Those are not allowed to become dependencies of the local custom typing workflow.

For pronunciation, prefer a voice already installed in the browser/operating system so SpeechSynthesis remains available offline.

---

# 47. Vocabulary Shooter multi-mode implementation baseline

The multi-mode Shooter design is no longer only a proposal. An initial implementation now exists in:

~~~text
sinhvienaiti/vocab-shooter
branch main
~~~

Verified child revision:

~~~text
8b1bebe8fc0b1f3e0392e2fd32039f29d317d39c
~~~

The implementation includes:

~~~text
Classic Survival
Bounce / Relax
Time Attack
Target Rush
~~~

It also includes:

- per-mode settings with migration from the earlier settings shape,
- configurable Tab/Escape quick restart,
- common results screen,
- Target Rush dedicated top VN/IPA Learning Panel,
- immediate Target Rush pronunciation at spotlight activation,
- fixed spotlight cadence and danger-dive behavior,
- late-save feedback,
- offline procedural background/danger audio and SFX,
- water/bubble-style hit particles and expanding ring,
- performance/balanced/quality particle/DPR budgets,
- hidden-tab RAF pause and audio suspension,
- dense Target Rush board rendering that draws dormant items first and active/danger targets above them,
- larger readable active/danger Target Rush cards without making every dormant card expensive.

Shooter CI runs:

~~~text
pnpm build
→ tsc --noEmit
→ vite build
~~~

The latest implementation/review revision above passed that CI.

The procedural background audio is an offline-safe first implementation, not the final music-content polish. A later pass may replace/improve the musical composition with licensed local assets while keeping the same performance and offline rules.

---

# 48. Monkeytype corrected-error accuracy option

Monkeytype now has an additional optional input setting:

~~~text
forgiveCorrectedErrors
~~~

UI label:

~~~text
forgive corrected errors
~~~

Default:

~~~text
false
~~~

It only changes behavior when:

~~~text
stop on error != off
~~~

The original Monkeytype scoring behavior remains unchanged when the option is disabled.

## Letter stop-on-error behavior

With:

~~~text
stop on error = letter
forgive corrected errors = on
~~~

the first wrong attempt at a blocked character can be recorded, but additional wrong attempts at that same blocked character do not keep reducing accuracy.

When the correct character is finally entered, the previous blocked error is forgiven for accuracy.

Concept:

~~~text
target: hello

x
→ first blocked error

y
→ still blocked at the same character
→ no additional accuracy penalty

h
→ blocked character corrected
→ previous blocked accuracy penalty is removed
~~~

## Word stop-on-error behavior

With:

~~~text
stop on error = word
forgive corrected errors = on
~~~

the first error in the currently blocked word can count, but further errors while that same word remains incorrect do not repeatedly reduce accuracy.

Once the word is corrected, the prior error for that blocked word is forgiven.

Correction is detected both when:

- normal correct typing makes the word text correct again, and
- a deletion/backspace removes the bad input and leaves the current word exactly correct.

This directly addresses the case where Stop on Error prevents advancing to the next word but extra keystrokes intended for later words would otherwise keep lowering accuracy.

## Implementation

Input events can carry:

~~~text
accuracyIgnored: true
~~~

Forgiven/repeated blocked errors remain in the event history for reproducibility/debugging but are excluded from accuracy calculations.

The live accuracy cache is adjusted incrementally instead of rescanning the complete event history after each correction.

Final accuracy and accuracy-related error history also ignore forgiven events.

Main changed areas:

~~~text
packages/schemas/src/configs.ts
frontend/src/ts/constants/default-config.ts
frontend/src/ts/config/metadata.tsx
frontend/src/ts/input/handlers/insert-text.ts
frontend/src/ts/input/handlers/delete.ts
frontend/src/ts/test/events/types.ts
frontend/src/ts/test/events/data.ts
frontend/src/ts/test/events/live-cache.ts
frontend/src/ts/test/events/stats.ts
frontend/__tests__/input/handlers/insert-text.spec.ts
frontend/__tests__/test/events/stats.spec.ts
~~~

Current Monkeytype child revision:

~~~text
9ba873ac06411802979ac9fdf48b435db82eb071
~~~

Targeted unit tests were added for:

- repeated blocked attempts,
- restoring live/final accuracy after correction,
- preserving original behavior when disabled,
- word-level blocked-error forgiveness,
- direct accuracy-stat handling of forgiven events.

The fork's existing Monkey CI is configured for master and non-draft/forced pull-request CI. The code/tests are present in the feature branch; do not claim a full Monkeytype CI pass unless an actual workflow run or local test output confirms it.

Detailed design/behavior is documented in:

~~~text
docs/design/MONKEYTYPE_CORRECTED_ERROR_ACCURACY.md
~~~

---

# 49. Current pinned child revisions

After the 2026-09-19 feature implementation/review work, the platform pins:

~~~text
games/vocab-shooter
→ 8b1bebe8fc0b1f3e0392e2fd32039f29d317d39c

games/monkeytype
→ 9ba873ac06411802979ac9fdf48b435db82eb071

games/recall-typing
→ 99d05c7cd72b47deae0f7700d7e168d529ebcc49
~~~

Use the parent repository plus:

~~~bash
git pull
git submodule update --init --recursive
~~~

to reproduce those versions.


---

# 50. Recall Typing becomes a separate game

The hidden-word / recall-spelling idea is now treated as a **new game**, not as another Monkeytype setting or Monkeytype mode.

Reason:

- it has a different learning goal from normal speed typing,
- it needs its own hint area and interaction model,
- it should be directly selectable from the platform Game Library,
- it avoids overloading Monkeytype with unrelated game behavior,
- it follows the platform rule that distinct learning experiences should become separate game repositories.

Working game name:

~~~text
Recall Typing
~~~

A better final product name can be chosen later without changing the architecture.

Implemented public route:

~~~text
https://typing-game.local/recall-typing
~~~

Internal origin:

~~~text
https://recall.typing-game.local
~~~

Repository model:

~~~text
sinhvienaiti/recall-typing
→ independent game repository

typing-game/games/recall-typing
→ Git submodule
~~~

Monkeytype keeps its existing custom EN-VN learning features and corrected-error accuracy option. Recall Typing should not be implemented inside Monkeytype.

Core Recall Typing behavior:

~~~text
word/phrase target exists internally

before typing:
→ unrevealed English letters are hidden

correct character:
→ reveal that character immediately

wrong character:
→ do not reveal the target character

new active word:
→ pronunciation cue can play
→ Vietnamese hint can be shown when available

spaces and punctuation:
→ remain structurally visible where useful

complete word:
→ full English word is visible
→ success feedback
→ continue to next target
~~~

Recommended learning panel:

~~~text
Vietnamese meaning
IPA
speaker / replay pronunciation
~~~

The main typing area remains focused on recalling the hidden English spelling.

This game should use the platform's offline-first rule and remain playable without Internet after local setup/build.

Detailed design lives in:

~~~text
docs/design/RECALL_TYPING_GAME.md
~~~


---

# 51. Recall Typing implementation baseline

Recall Typing has been implemented as its own repository and integrated into the platform.

Child repository:

~~~text
sinhvienaiti/recall-typing
branch main
~~~

Initial reviewed/CI revision:

~~~text
99d05c7cd72b47deae0f7700d7e168d529ebcc49
~~~

The child CI runs:

~~~text
pnpm install
pnpm test
→ 2 test files / 9 tests

pnpm build
→ tsc --noEmit
→ vite build
~~~

and passed for the revision above.

Implemented behavior:

- English answer is hidden before typing.
- Correct letters reveal immediately.
- Wrong letters do not reveal and do not advance.
- Spaces and structural punctuation remain visible.
- Vietnamese + IPA can be shown in a fixed hint panel.
- English pronunciation can auto-play when a new target starts.
- F2 replays pronunciation without stealing normal letter keys.
- Hint styles support full, audio-only and meaning-focused recall.
- Tab/Escape is configurable as quick restart.
- Vocabulary editor supports English / Vietnamese / IPA.
- Bulk import uses `English | Vietnamese | IPA`.
- Vocabulary is stored in IndexedDB.
- Settings are stored in localStorage.
- JSON backup/import is supported.
- Results include completed words, wrong attempts, accuracy, max streak, elapsed time and average word time.
- The implementation is DOM/CSS based with no permanent RAF/render loop.
- After review, hidden slots render as clean underline blanks without placeholder glyphs that could distract from recall.

Platform integration:

~~~text
Game Library route:
https://typing-game.local/recall-typing

internal app origin:
https://recall.typing-game.local

dev port:
3002
~~~

The platform scripts now include:

~~~text
pnpm dev:recall
pnpm build:recall
~~~

Full `pnpm dev`, `pnpm build:local`, bootstrap and static Play mode also include Recall Typing.

The nginx setup script now:

1. verifies every required typing-game hostname in /etc/hosts,
2. checks the shared certificate for every required SAN,
3. runs `mkcert -install` before certificate regeneration,
4. regenerates one certificate covering Portal, Monkeytype, Shooter and Recall Typing when needed.

Core Recall Typing remains offline-first.


---

# 52. Recall Typing review and cleanup baseline

After the first Recall Typing implementation, a dedicated self-review and verification pass was completed before treating the game as the baseline.

Final reviewed child revision:

~~~text
sinhvienaiti/recall-typing
main
99d05c7cd72b47deae0f7700d7e168d529ebcc49
~~~

## Review findings and fixes

The review found and fixed several real issues:

### Quick-restart transition race

A completed word schedules a short transition to the next target.

Without cleanup, pressing quick restart during that transition could allow the old timeout to fire inside the new run and advance the new session unexpectedly.

Fix:

~~~text
track transition timer
→ cancel it on restart / finish
→ clear old success/error classes before a new run
~~~

### Bulk editor changed live vocabulary before Save

The Bulk Import button originally assigned parsed entries directly to the live `vocabulary` variable before the user pressed Save.

That meant:

~~~text
Apply bulk
→ close dialog without Save
→ in-memory game vocabulary had already changed
~~~

Fix:

~~~text
Apply bulk
→ update editor table only

Save vocabulary
→ commit table rows to IndexedDB and live game state
~~~

The vocabulary editor is now transactional.

### Invalid recall targets

Entries containing no recallable letter/number could create a target that could never be completed.

Fix:

~~~text
shared validation
→ English must contain at least one recallable letter/number
→ invalid punctuation-only targets are rejected
~~~

The same validator is reused by session building and bulk import to avoid duplicate rules.

### Backup import robustness

Backup import previously assumed every array item had the expected object shape.

The review hardened it to:

- reject null/non-object entries safely,
- validate English/Vietnamese field types,
- normalize text,
- replace missing IDs,
- replace duplicate IDs,
- reject a backup with no usable vocabulary.

### Hidden-answer presentation

The initial hidden state used placeholder bullet glyphs.

Those were removed so unrevealed characters are clean underline blanks and do not provide unnecessary visual noise.

### Core logic extraction

Small reusable recall rules were extracted to:

~~~text
src/game/recall.ts
~~~

This keeps session construction, structural-character skipping, case matching and target validation out of the large UI file.

## Automated tests

Added:

~~~text
src/game/recall.spec.ts
src/ui/vocabulary-editor.spec.ts
~~~

Coverage includes:

- letters/numbers versus structural spaces and punctuation,
- skipping apostrophes, hyphens and phrase spaces,
- case-insensitive and exact-case matching,
- invalid punctuation-only targets,
- non-mutating session selection/shuffle,
- normal word/phrase bulk parsing,
- invalid bulk-row rejection,
- blank IPA round-trip.

Verified CI result:

~~~text
2 test files passed
9 tests passed
TypeScript passed
Vite production build passed
~~~

## Platform integration review

A Platform CI workflow was added to validate:

- shell script syntax,
- game registry JSON,
- submodule checkout,
- Recall Typing tests,
- Portal TypeScript/build,
- Recall Typing TypeScript/build.

The first Platform CI run exposed a pre-existing Portal TypeScript narrowing issue:

~~~text
portal/src/main.ts
'app' is possibly 'null'
~~~

That was corrected by keeping a verified non-null root element for render functions.

The reviewed platform integration then passed Platform CI.

The platform also hardened local environment setup so all four local hosts and all certificate SANs are checked instead of only the newly added Recall hostname.

Current reviewed parent code baseline before documentation-only commits:

~~~text
b18c8825905b2a4e5027634bd5595a32e867755c
→ Platform CI PASS
~~~

This does not claim that no future browser/runtime edge case can ever exist; it means the known review findings were fixed and the current unit, type, build and focused integration checks are clean.


---

# 53. Development port cleanup

A repeated local development start can leave old Vite listeners alive on the platform ports:

~~~text
3000 → Monkeytype
3001 → Vocabulary Shooter
3002 → Recall Typing
3100 → Portal
~~~

When that happened, Vite failed with messages such as:

~~~text
Port 3001 is already in use
Port 3100 is already in use
~~~

Because the top-level development command uses `concurrently -k`, one child failure caused the other game processes to receive SIGTERM even when those games had started correctly.

The platform now runs:

~~~text
scripts/cleanup-dev-ports.sh
~~~

before the full or focused development commands.

Safety rule:

- only listeners whose current working directory is inside the current `typing-game` repository may be stopped automatically,
- a listener from another project/application is never killed automatically,
- if an external listener owns a required port, startup stops and reports the PID/cwd so the conflict can be handled intentionally.

Current wrappers:

~~~text
pnpm dev
→ cleanup 3000 3001 3002 3100

pnpm dev:monkeytype
→ cleanup 3000 3100

pnpm dev:shooter
→ cleanup 3001 3100

pnpm dev:recall
→ cleanup 3002 3100
~~~

Platform CI shell validation includes the cleanup script.


---

# 54. One-command development launcher

Normal development startup is now centralized in the executable root script:

~~~text
./dev.sh
~~~

Default behavior:

~~~text
./dev.sh
→ same as ./dev.sh all
~~~

Supported targets:

~~~text
all
monkeytype
shooter
recall
~~~

Accepted convenience aliases:

~~~text
vocab-shooter
recall-typing
~~~

The launcher intentionally does not hard-code the user's local absolute path. It resolves the repository root from the location of `dev.sh`.

Flow:

~~~text
git pull --ff-only --recurse-submodules=no
→ re-run the post-pull version of dev.sh
→ bootstrap the selected scope
→ git submodule sync/update to the revisions pinned by typing-game
→ install/update platform + Portal dependencies
→ install/update only the requested game dependencies, or every game for all
→ pnpm setup:dev
→ start the matching pnpm dev command
~~~

The post-pull re-exec is intentional: if `dev.sh` itself changes in the pulled revision, the newly pulled script controls the rest of that startup instead of continuing with stale in-memory instructions.

Focused bootstrap is implemented in:

~~~text
scripts/bootstrap.sh [all|monkeytype|shooter|recall]
~~~

Common platform and Portal dependencies are always prepared because every browser-facing game route uses the Portal. A focused run prepares only its selected child game beyond those common dependencies.

The launcher uses the child revisions pinned by the platform repository. It does not use `git submodule update --remote`, because the parent repository remains the integration source of truth.

Examples:

~~~bash
./dev.sh
./dev.sh all
./dev.sh monkeytype
./dev.sh shooter
./dev.sh recall
~~~

---

# 55. Cross-game interaction refinement baseline - 2026-09-20

The current reviewed child revisions are:

~~~text
Monkeytype
feature/en-vn-translation
943b4d9dd60f6e4f870cba3588538b8b06745210

Vocabulary Shooter
main
7e23c1241360be8f08fce83b4733300dad12aa88

Recall Typing
main
3beb3ceea3d23688d027134d945b33b8daceb894
~~~

For new Shooter and Recall settings, Escape is now the default quick-restart key.

Migration must preserve an existing user-selected Tab/Escape value rather than silently replacing it.

The keyboard restart interaction for both games is:

~~~text
quick restart key
→ clean ready state
→ next normal key
→ 3-second countdown
→ start
~~~

The Start / Restart button may begin the countdown directly.

Restart must clear stale timers/transitions/speech and return keyboard focus to the game.

---

# 56. Monkeytype EN-VN three-line viewport rule

The EN-VN learning extension must not disable Monkeytype's normal line-window behavior.

Root cause of the 2026-09-20 expansion regression:

~~~text
core wrapper height was correct
+
custom learning overflow exposed content below that height
~~~

Current rule:

~~~text
Monkeytype core controls typing viewport height
translation UI may extend above / slightly outside horizontally
typing content below the viewport remains clipped
~~~

Current custom wrapper uses a clip path with extra top/side allowance for translation tooltips.

Do not restore a plain unrestricted overflow rule on the learning wrapper.

Comfortable/wide EN-VN line spacing is intentionally larger than normal spacing so held Vietnamese tooltips have room without covering adjacent text.

---

# 57. Monkeytype optional Recall Typing mode

The existing Custom Text EN-VN feature now has:

~~~text
recallModeEnabled
~~~

Default:

~~~text
false
~~~

Scope:

~~~text
Config.mode === custom
EN-VN feature enabled
dictionary contains a matching word/phrase
~~~

Behavior:

- dictionary-matched English letters are hidden before typing,
- non-matched text remains normal Monkeytype text,
- structural punctuation remains visible,
- correct/corrected letters progressively reveal,
- wrong target letters do not reveal the answer,
- the learning cue is presented when the recall target becomes active,
- top display hides the English source while Recall mode is enabled,
- English pronunciation still follows the existing pronunciation settings,
- restart clears shown-match and speech state.

Longest phrase matching is centralized in the dictionary helper.

Do not implement a second independent phrase matcher in the render/input code.

Recall-target classes are attached during normal word rendering so the answer does not flash before the first keypress.

---

# 58. Monkeytype Custom Text settings baseline

The custom text/EN-VN settings UI is intentionally compact.

The text and dictionary editors use bounded heights and internal scrolling.

Small question-mark help controls explain EN-VN display, tooltip, spacing and pronunciation options without permanently expanding the sidebar.

The Recall Typing control belongs to this EN-VN settings group and remains opt-in.

---

# 59. Vocabulary Shooter Target Rush presentation baseline

Target Rush currently uses text-first targets without rectangular word boxes.

Board rules:

~~~text
maximum rows = 4
extra targets increase the column count
font size adapts to cell width and phrase length
~~~

Dormant targets stay subdued.

Spotlight, danger, active and error states use glow/color to carry emphasis.

Dense/long phrases may use a small font rather than overlap neighboring cells.

The dedicated top Learning Panel remains the source of VN/IPA for the current spotlight target.

Do not move VN/IPA onto the target text itself.

---

# 60. Recall Typing responsive target presentation

Recall Typing calculates slot font size/gap from the available width and target length.

Short targets remain large.

Long phrases can wrap into compact rows without extreme letter gaps.

The scale is recalculated on viewport resize.

Structural spaces/punctuation remain visible while recallable English characters reveal progressively.

---

# 61. Portal game-loading rule

The Portal continues to mount only one selected game iframe.

Do not keep all games mounted merely to make navigation feel instant; that would increase memory/CPU usage and violate the existing platform performance rule.

The current compromise is:

~~~text
preconnect child origin
→ lightweight Loading game overlay
→ iframe load
→ fade game in
→ remove loader
~~~

This improves perceived loading without keeping inactive game runtimes alive.

---

# 62. Monkeytype full-text reader

The Monkeytype Custom Text settings now include a full-text reader.

Technology:

~~~text
browser/system SpeechSynthesis
SpeechSynthesisUtterance
~~~

No external TTS library or remote/cloud audio pipeline is part of the feature.

Settings persisted in `personalEnVnTranslationSettings`:

~~~text
textReaderEnabled
textReaderLanguage
textReaderVoiceURI
textReaderRate
textReaderVolume
~~~

Language options:

~~~text
auto
en-US
vi-VN
~~~

Auto detects Vietnamese-specific marks and otherwise uses English.

Voice rule:

~~~text
only SpeechSynthesisVoice entries with localService === true
~~~

If no matching local voice exists, reading does not silently fall back to remote speech.

Rate:

~~~text
0.5x → 2.0x
~~~

Volume:

~~~text
0 → 100
~~~

Runtime controls:

~~~text
Play / Restart
Pause / Resume
Stop
~~~

Long text is chunked before playback; oversized unbroken tokens are also bounded.

The full-text reader and existing EN-VN word pronunciation intentionally share one browser speech queue. Starting word pronunciation stops the full-text reader and updates reader state before speaking the word.

The modal stops full-text reading when it closes.

Current reviewed Monkeytype revision:

~~~text
943b4d9dd60f6e4f870cba3588538b8b06745210
~~~

Verification:

~~~text
Custom EN-VN CI
→ lint PASS
→ stylelint PASS
→ local-static production build PASS
→ full frontend tests PASS
~~~

---

# 63. Verification baseline - 2026-09-20

Automated review status before the final parent integration commit:

~~~text
Monkeytype custom branch
→ lint PASS
→ stylelint PASS
→ local-static production build PASS
→ full frontend tests PASS

Vocabulary Shooter
→ TypeScript PASS
→ Vite build PASS

Recall Typing
→ 2 test files / 9 tests PASS
→ TypeScript PASS
→ Vite build PASS

Portal parent revision 2fbf31d...
→ Platform CI PASS
~~~

The final parent commit pins the reviewed child revisions and must itself pass Platform CI before this baseline is treated as closed.

---

# 64. Second-pass phrase/cell edge-case fixes

Before the 2026-09-20 baseline was finally pinned, a second logic review found two additional edge cases.

## Monkeytype overlapping phrases

Recall rendering and recall learning cues must use the same greedy longest-match boundaries.

Current implementation:

~~~text
dictionary scan during word rendering
→ target indices + phrase-start indices
→ phrase-start marker on rendered word
→ active/started-word cue checks the marker
~~~

This prevents a shorter dictionary entry inside a longer phrase from becoming a second recall cue.

Example:

~~~text
dependency injection = tiêm phụ thuộc
injection = tiêm
~~~

The second word must not trigger a separate "injection" learning cue when it belongs to the already selected two-word phrase.

Current reviewed Monkeytype revision:

~~~text
943b4d9dd60f6e4f870cba3588538b8b06745210
~~~

## Target Rush ultra-dense width

Target Rush target width must not keep a minimum that is larger than the real grid cell on narrow/dense boards.

The current renderer uses the actual cell-derived target width for text fitting and a smaller safe drawing floor.

Current reviewed Shooter revision:

~~~text
7e23c1241360be8f08fce83b4733300dad12aa88
~~~

Both child CI workflows are green at these revisions.

---

# 65. Root Play launcher

Normal study/play startup is:

~~~bash
./play.sh
~~~

Play mode is deliberately separate from development mode.

It must not:

- run `git pull`,
- update submodules,
- install dependencies,
- start Vite/Turbo watchers.

Those responsibilities belong to `./dev.sh`.

Play mode may rebuild a static app when its current local source is newer than its existing static output. This is a local compilation step, not a source update.

Current flow:

~~~text
stop project-owned dev listeners
→ selectively refresh stale static builds
→ switch nginx to Play config if needed
→ open https://typing-game.local
~~~

The four development ports are not required in Play mode:

~~~text
3000
3001
3002
3100
~~~

Any old typing-game listeners on those ports are stopped before play so they do not keep consuming resources.

The cleanup helper's `--project-only` option must never terminate or block on an unrelated application's listener.

Build freshness is checked independently per app so changing Recall does not force a Monkeytype rebuild, and vice versa.

Once all static builds are current, repeated `./play.sh` runs should not invoke pnpm builds.

The Portal still mounts only the selected game iframe. In Play mode, child apps are served as prebuilt static assets by nginx rather than Vite dev servers.



---

# 66. macOS Bash 3.2 empty cleanup compatibility

Observed local failure:

~~~text
scripts/cleanup-dev-ports.sh: line 56: targets[0]: unbound variable
~~~

This occurred when `./dev.sh all` reached port cleanup and there were no old project-owned listeners to stop.

The project uses:

~~~text
set -euo pipefail
~~~

macOS Bash 3.2 can treat an empty array expansion under nounset differently from the newer Bash used by CI.

Portable rule:

~~~text
do not expand targets[@] when there are zero targets
~~~

Implementation uses a separate scalar:

~~~text
target_count
~~~

The array is expanded only when `target_count > 0`.

Do not replace this with an unconditional empty-array loop merely because it works on a newer Bash.

Platform CI also executes an empty project-only cleanup smoke test.

---

# 67. Current Monkeytype reader baseline

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation
943b4d9dd60f6e4f870cba3588538b8b06745210
~~~

This baseline includes:

- EN-VN tooltip/top learning,
- optional Monkeytype Recall mode,
- English word/phrase pronunciation,
- full Custom Text reader,
- Auto/English/Vietnamese reader language,
- local system voice selection,
- rate and volume controls,
- Play/Restart/Pause/Resume/Stop,
- chunked long-text speech,
- shared speech-queue coordination.

No remote TTS dependency was added.


---

# 68. Monkeytype post-test visual/reader/settings fixes

A browser review on 2026-09-20 found four remaining Monkeytype issues.

## Held tooltip collision

Symptoms:

- first-line held tooltips could cover mini live stats,
- second-line held tooltips could overlap text from the previous typing line.

Fix:

~~~text
compact tooltip bubble
+
safe vertical line margins for normal/comfortable/wide
+
2.15rem learning lane above #wordsWrapper
~~~

The wrapper lane separates first-line bubbles from Monkeytype's h-0/negative-margin mini statistics.

The top EN-VN panel was moved slightly higher.

## Custom Text modal empty space

Root cause:

~~~text
left editor column shared the row height of the much taller settings sidebar
+
its internal grid used normal stretch behavior
~~~

Fix:

~~~text
content-start
self-start
~~~

are now applied to the editor/settings grids, with slightly smaller settings gaps.

This keeps the text editor, dictionary editor and OK button grouped near the top instead of being stretched down the full sidebar height.

## Full-text reader gameplay start

The settings button is now labeled:

~~~text
Preview
~~~

because it is only a configuration preview.

When enabled, real gameplay automatically starts reading on the first actual typing key.

Source:

~~~text
current generated TestWords
~~~

rather than stale modal text.

Only one automatic reader start occurs per test; restart resets it.

While the reader is playing or paused, dictionary learning tooltips/top cues still appear but per-word pronunciation is suppressed so it cannot cancel the full-text narration.

## Corrected-error setting visibility

The existing:

~~~text
forgiveCorrectedErrors
~~~

logic and tests were already present.

The Settings page had accidentally omitted:

~~~text
<SearchableAutoSetting key="forgiveCorrectedErrors" />
~~~

It is now visible directly after Stop on Error in Settings -> Input.

Current behavior remains:

~~~text
Stop on Error = letter
→ first wrong blocked attempt may count
→ repeated wrong attempts at same blocked position do not add accuracy penalties
→ correcting the character forgives the blocked accuracy error

Stop on Error = word
→ first error in the blocked word may count
→ later wrong attempts in that same unresolved word do not add accuracy penalties
→ correcting the word forgives the blocked accuracy error
~~~

Final reviewed Monkeytype revision:

~~~text
943b4d9dd60f6e4f870cba3588538b8b06745210
~~~

Custom EN-VN CI:

~~~text
lint PASS
stylelint PASS
local-static production build PASS
full frontend tests PASS
~~~


---

# 69. Monkeytype flexible Stop on Error policies

Monkeytype now exposes three distinct accuracy/input behaviors around Stop on Error.

## Original behavior

With the new accuracy options disabled, original Monkeytype scoring remains authoritative.

## Ignore repeated blocked errors

~~~text
ignoreRepeatedBlockedErrors = true
~~~

Behavior:

~~~text
first blocked error
→ remains an accuracy penalty

later wrong attempts at the same blocked character/word
→ no additional accuracy penalty

eventual correction
→ original first penalty remains
~~~

This is the preferred mode for the user's fast-typing case where several extra keys may be pressed after a Stop on Error block is already active.

## Forgive corrected errors

~~~text
forgiveCorrectedErrors = true
~~~

Behavior:

~~~text
first blocked error
→ may count initially

later repeated blocked attempts
→ no additional accuracy penalty

eventual correction
→ original blocked accuracy penalty is forgiven
~~~

This existing feature remains available.

The Settings UI makes these two scoring modes mutually exclusive.

## Keep first wrong letter

~~~text
stopOnErrorKeepFirstError = true
~~~

With:

~~~text
stop on error = letter
~~~

the first wrong character remains visibly incorrect/red instead of being immediately removed.

Further insertions are blocked until the wrong character is deleted.

Backspace/delete behavior remains native Monkeytype behavior.

UI location:

~~~text
Settings
→ Input
→ stop on error
→ keep first wrong letter
→ ignore repeated blocked errors
→ forgive corrected errors
~~~

All three custom options default to off.

Final reviewed Monkeytype child revision:

~~~text
9ca8c976d3883688705e58bb0e3f1626db7eae1b
~~~

Verification:

~~~text
Custom EN-VN CI
→ lint PASS
→ stylelint PASS
→ local-static production build PASS
→ full frontend tests PASS
~~~

The final review also added the two new config keys to command-line metadata after CI correctly reported the missing exhaustive entries.

---

# 70. Shooter active-target visual baseline

Vocabulary Shooter now uses a red animated downward marker above the currently locked typing target.

The marker:

- is Canvas vector art,
- has no external asset dependency,
- uses rounded/chubby geometry,
- has red glow/gradient,
- bobs smoothly,
- has subtle sway,
- uses horizontal scale animation for a lightweight rotating-game-marker feel,
- exists only for the active locked target.

The post-success Vietnamese/IPA display no longer draws a rectangular border/card over the game field.

Vietnamese is now heavier:

~~~text
font weight = 900
~~~

and uses a soft glow for readability.

IPA remains secondary.

The Target Rush fixed top Learning Panel remains separate and unchanged.

Final reviewed Shooter revision:

~~~text
0e07b54171ac2d192178b0bcef65ebe9407bf36a
~~~

Shooter CI:

~~~text
TypeScript PASS
Vite build PASS
~~~


---

# 71. Shared leveled vocabulary library

The platform now has one canonical built-in vocabulary library shared by Monkeytype, Vocabulary Shooter and Recall Typing.

Source of truth:

~~~text
shared/vocabulary/levels/*.json
~~~

There is intentionally no second giant 15k-20k Monkeytype vocabulary copy.

Every official entry requires:

~~~text
id
en
vi
ipa
~~~

Example:

~~~json
{
  "id": "L003-025",
  "en": "cache",
  "vi": "bộ nhớ đệm",
  "ipa": "/kæʃ/"
}
~~~

Current implementation is only a pipeline/sample baseline:

~~~text
001.json → 30 entries
002.json → 30 entries
003.json → 30 entries

90 sample entries total
planned levels → 100
final target → roughly 15k-20k useful words/phrases
~~~

The 90 sample entries are not the final vocabulary curriculum.

Generated artifacts:

~~~text
shared/vocabulary/index.json
shared/vocabulary/lookup.json
~~~

They are generated/validated from the level files and must not become a second hand-maintained source of truth.

Commands:

~~~bash
pnpm vocab:generate
pnpm vocab:validate
~~~

Platform CI validates the dataset, runs the generator and verifies that generated index/lookup files produce no Git diff.

Local HTTP contract:

~~~text
https://typing-game.local/vocabulary/index.json
https://typing-game.local/vocabulary/lookup.json
https://typing-game.local/vocabulary/levels/NNN.json
~~~

Dev and Play nginx both expose the same files with CORS for child subdomains.

Shooter:

~~~text
Vocabulary
→ Class / Custom

Class
→ select one available level
→ load that level only

Custom
→ existing IndexedDB vocabulary
~~~

Recall:

~~~text
Vocabulary
→ Class / Custom

Class
→ select one available level
→ load that level only

Custom
→ existing IndexedDB vocabulary
~~~

Class mode never overwrites the user's Custom dataset.

Monkeytype Custom Text EN-VN dictionary:

~~~text
Library / Custom
~~~

Library mode does not expose a level selector.

It uses `lookup.json` against the current Custom Text, discovers the referenced levels, loads only those level files, and feeds the resulting entries into the existing dictionary/longest-phrase matching pipeline.

Final child revisions for this feature:

~~~text
Monkeytype
fede711b4316f8abe2d04ecc45c9bbf6a1e0c99a

Vocabulary Shooter
0f4e114fa003fffc67b72de9cb5ab3943c877087

Recall Typing
7e03fafe040814cd0e7cfd3f1a0033202133b996
~~~

Verification before parent pin:

~~~text
Monkeytype Custom EN-VN CI → PASS
Shooter CI                 → PASS
Recall CI                  → PASS
Platform vocabulary CI     → PASS
~~~

Detailed contract:

~~~text
docs/design/SHARED_VOCABULARY_LIBRARY.md
~~~


---

# 72. First production shared-vocabulary batch

The sample vocabulary dataset was replaced with the first production batch.

Current shared library:

~~~text
Level 001 -> 150 reviewed foundation entries
Level 002 -> 150 reviewed foundation entries
Level 003 -> 150 reviewed foundation entries

total -> 450
~~~

The entries are source-backed and manually selected for usefulness rather than bulk-generated.

The production data policy is now explicit:

~~~text
frequency
+ CEFR reference
+ usefulness
+ spelling difficulty
+ pronunciation difficulty
+ abstractness
+ technical/general balance
-> manual final level review
~~~

IPA convention:

~~~text
General American
~~~

The initial review found real heteronym problems in source pronunciations, including
`read`, `live` and `close`, so pronunciation must remain POS/meaning-aware.

A scalable review-only candidate tool was added:

~~~bash
pnpm vocab:candidates
~~~

It reads local cached open datasets and writes:

~~~text
.cache/vocabulary-candidates.json
~~~

It never writes `shared/vocabulary/levels/*.json`.

Approved source strategy and license/attribution details are documented in:

~~~text
docs/design/SHARED_VOCABULARY_LIBRARY.md
shared/vocabulary/ATTRIBUTION.md
~~~

The Portal includes a visible link to the vocabulary attribution.

The JSON Schema ID regex was also corrected and validator/schema drift is now checked explicitly.


---

# 73. Production vocabulary QA polish

A second manual QA pass refined learner-facing meanings and pronunciation in the first 300-entry production batch.

Corrections include:

~~~text
dirty      -> bẩn; dơ
show       -> cho thấy; chỉ ra
first name -> tên
card       -> thẻ
create     -> /kɹiˈeɪt/
outside    -> /aʊtˈsaɪd/
~~~

The pronunciation corrections were checked against English pronunciation references instead of trusting the source conversion blindly.

Platform CI now also syntax-checks:

~~~text
scripts/prepare-vocabulary-candidates.mjs
~~~

This keeps the review-only candidate pipeline from silently breaking even though CI does not download third-party source datasets.


---

# 74. Foundation vocabulary expanded to 450 entries

After the 300-entry batch passed manual QA and Platform CI, the same three foundation levels were expanded instead of creating Level 004 too early.

Current density:

~~~text
001.json -> 150 entries
002.json -> 150 entries
003.json -> 150 entries

total -> 450 unique English words/phrases
~~~

The additional 150 entries were selected from the same source-backed candidate pool:

~~~text
50 -> Level 001
50 -> Level 002
50 -> Level 003
~~~

Each promoted entry keeps the required:

~~~text
English
Vietnamese
General American IPA
~~~

The expansion remains intentionally incremental. The next levels should continue in reviewed batches rather than jumping directly to thousands of generated entries.

---

# 75. Automated trusted-source vocabulary expansion

The vocabulary production policy was changed after confirming that manual review of
15,000-20,000 entries is not a scalable requirement.

This section supersedes any earlier wording that implies every ordinary vocabulary entry
must be manually reviewed before it can enter the official level files.

The approved workflow is:

~~~text
pinned trusted source revisions
-> prepare normalized candidates
-> automatic provenance/exception filtering
-> automatic difficulty ordering
-> preserve reviewed Levels 001-003
-> automatically build Levels 004-100
-> regenerate index/lookup
-> validate everything
-> manually inspect only exceptions and samples
~~~

Normal command:

~~~bash
pnpm vocab:refresh
~~~

Subcommands:

~~~text
pnpm vocab:sources
pnpm vocab:candidates
pnpm vocab:build-library
pnpm vocab:validate
~~~

Default library target:

~~~text
18,000 total entries
minimum trusted total = 15,000
100 levels
~~~

The builder never generates filler just to reach a number.

Automatic promotion requires source provenance containing:

~~~text
CMUdict
+
WordNet or Wiktionary
~~~

Candidates with multiple trusted pronunciations are treated as exceptions and skipped from
the automatic bulk build. The existing reviewed entries in Levels 001-003 are preserved,
including previously resolved heteronyms.

Pinned source revisions:

~~~text
thichhoc-org/thichhoc-dict
4d6e92e8bcf8e3e762410c2b0a9f98fea8e62e5b

openlanguageprofiles/olp-en-cefrj
d4e45b75b38f27b30dfc5c44d8c571aec7e7092f
~~~

CEFR remains a difficulty anchor. When a candidate has no CEFR match, the bulk builder uses
frequency plus spelling/pronunciation complexity to estimate relative difficulty rather than
requiring manual placement.

The generated local report is:

~~~text
.cache/vocabulary-build-report.json
~~~

The committed level files remain the runtime source of truth for all three games.
The bulk pipeline is the reproducible way to rebuild/expand those files from approved sources.

---

# 76. Production 18k vocabulary library completed

The shared vocabulary expansion is now complete at the requested production scale.

Current committed dataset:

~~~text
100 levels
18,000 total entries
450 reviewed entries preserved in Levels 001-003
17,550 automatically generated entries in Levels 004-100
average 180 entries/level
~~~

Final generated-data commit:

~~~text
e18fbcae8713afaa0a0b5f2cf2df53a41c3f18e4
~~~

The automatic pipeline is no longer a dictionary-wide bulk import.

Final source/selection order:

~~~text
wordfreq 3.1.1
-> common-English usefulness/ranking

ESDB / SCOWL size 70, American English
-> lexical whitelist
-> abbreviations/special categories excluded
-> lowercase alphabetic headwords only

thichhoc-dict
-> Vietnamese meanings
-> IPA/pronunciation metadata
-> CMUdict + WordNet/Wiktionary provenance

CEFR-J
-> difficulty anchor where available
-> CEFR/POS mismatch protection
~~~

Pinned source revisions:

~~~text
thichhoc-org/thichhoc-dict
4d6e92e8bcf8e3e762410c2b0a9f98fea8e62e5b

openlanguageprofiles/olp-en-cefrj
d4e45b75b38f27b30dfc5c44d8c571aec7e7092f

en-wl/wordlist
1e5b7d3a72f47a71da5d28686c1dd4b397178485

wordfreq package
3.1.1
~~~

Final production build statistics:

~~~text
normalized candidates        = 83,617
wordfreq ranking headwords   = 57,449
SCOWL words                  = 126,423
trusted common candidates    = 23,474
selected automatic entries   = 17,550
selected maximum source rank = 35,609
final total                  = 18,000
~~~

Quality fixes made during full-build review:

~~~text
dictionary-wide phrases/proper names
-> replaced with wordfreq + SCOWL selection

proper-name-like Vietnamese sense chunks
-> skipped when a normal learner meaning is available

multiple trusted pronunciations
-> excluded from automatic promotion

CEFR headword/POS mismatch
-> review-only

unknown-CEFR level placement
-> normalized against the selected 18k library
   instead of the entire upstream frequency list
~~~

This last change prevents useful but clearly intermediate words from drifting into A1 only
because they are common relative to the complete upstream corpus.

Platform integration PASS and full vocabulary build PASS.

Runtime remains unchanged:

~~~text
shared/vocabulary/levels/*.json
-> source of truth

index.json / lookup.json
-> generated artifacts
~~~

Monkeytype, Vocabulary Shooter and Recall Typing continue to consume the same shared library.


---

# 77. Leveled typing-text library and random practice plan

The next major learning-content phase has been designed and approved.

Authoritative design document:

~~~text
docs/design/LEVELED_TYPING_TEXT_LIBRARY.md
~~~

The scope is:

~~~text
Vocabulary Shooter
-> randomized non-repeating vocabulary cycles

Recall Typing
-> randomized non-repeating vocabulary cycles

Monkeytype
-> new Level Passages text source
-> Level 001-100 selector
-> 1-15 passages per session
-> randomized non-repeating passage cycles

shared typing-text corpus
-> 100 level files
-> at least 15 passages per level
-> 250-300 words per passage
-> 20-30 target vocabulary entries per passage
-> at least 1,500 passages total
-> approximately 375,000-450,000 English words
~~~

The corpus must use the existing 18,000-entry shared vocabulary library rather than creating a second independent vocabulary system.

Content production is explicitly quality-gated:

~~~text
one level
-> generate passages
-> automatic validation
-> editorial self-review
-> fix
-> revalidate
-> whole-level QA
-> PASS
-> only then continue to next level
~~~

Production batches are:

~~~text
001-030
031-060
061-090
091-100
~~~

Each completed level should be checkpointed locally. A batch is pushed only after batch-wide QA passes. After each successful push, report the completed level range to the user and continue automatically.

The corpus uses strict typing rules, CEFR-aware difficulty, coverage-aware target vocabulary selection, topic/style diversity, research for better writing quality, originality protection, automated similarity checks and editorial anti-repetition review.

This section is only the implementation handoff summary. The detailed rules in docs/design/LEVELED_TYPING_TEXT_LIBRARY.md are authoritative.


---

# 78. Karaoke Typing game

A fourth independent game has been added:

~~~text
sinhvienaiti/karaoke-typing
~~~

Platform integration:

~~~text
games/karaoke-typing
-> Git submodule
-> branch main

public route
-> https://typing-game.local/karaoke-typing

internal origin
-> https://karaoke.typing-game.local

dev port
-> 3003
~~~

Karaoke Typing is a clean TypeScript/Vite implementation inspired by the gameplay model of TypingMania NEO. It does not copy TypingMania source code and does not modify Monkeytype, Vocabulary Shooter or Recall Typing source.

Current media sources:

~~~text
YouTube URL / video ID
local browser-supported audio
local browser-supported video
~~~

Local media uses browser object URLs and is never uploaded by the game.

Lyrics:

~~~text
standard LRC
enhanced LRC word timing
runtime offset -5s to +5s
~~~

Current gameplay modes:

~~~text
Normal
Easy
Blind
Blank
~~~

The game includes score, combo, normal/typing accuracy, completed/skipped lines, skipped characters, result screen and restart.

Child verification is owned by the Karaoke Typing repository:

~~~text
pnpm test
pnpm build
~~~

Important CI caveat:

~~~text
karaoke-typing is currently private
existing Monkeytype / Shooter / Recall repositories are public
~~~

The parent GitHub Actions token is not assumed to have access to a private sibling repository. Parent CI therefore leaves the private Karaoke gitlink uninitialized, verifies that the gitlink exists, and continues initializing/testing the existing public Recall submodule. Karaoke source correctness is enforced by its own child CI.

Authoritative design:

~~~text
docs/design/KARAOKE_TYPING_GAME.md
~~~


---

# 79. Rapid pronunciation queue

Browser TTS pronunciation for the vocabulary-based games must preserve rapid consecutive words.

Affected child games:

~~~text
Vocabulary Shooter
Recall Typing
Monkeytype EN-VN per-word pronunciation
~~~

Required behavior:

~~~text
first word is still speaking
-> second completed word is queued
-> first finishes
-> second is spoken
~~~

Per-word speech must not call `speechSynthesis.cancel()` before every `speak()`.

Explicit lifecycle cleanup is different and must continue cancelling speech when leaving/resetting a run so old queued words do not leak into a new session.

Current reviewed child revisions:

~~~text
monkeytype
9e4090b6212b71479e78f06d6c5bc2497a4343fb

vocab-shooter
71e2db77f5ec5229caf2501e8b0d48a8fe6c2650

recall-typing
277607d75972c776985e910c475eb8da4b9223b2
~~~

Karaoke Typing is not part of this TTS rule because its audio source is the song/media player rather than per-word browser speech.


---

# 80. Vocabulary source confirmation UX

Vocabulary Shooter's Vocabulary dialog separates browsing from applying a source.

~~~text
Class tab
-> choose a level
-> Use level
-> Applying…
-> load succeeds
-> source is persisted
-> game vocabulary is replaced
-> dialog closes
-> game returns to ready
-> "Level NNN applied · X words" notice
~~~

Switching between the Class and Custom tabs does not itself change the active vocabulary source.

Custom vocabulary becomes active only when Save vocabulary succeeds, and it also shows a success notice.

The Class level select uses the same Shooter form-control colors, border, radius and focus treatment as the existing settings controls while retaining native select appearance/keyboard/accessibility behavior.

Current reviewed Vocabulary Shooter revision:

~~~text
879104e875d571d5111d3c4a60c7a93e4f5fb572
~~~


---

# 81. Immediate Shooter learning feedback

For Classic, Bounce and Time Attack, Vietnamese + IPA learning feedback starts at the exact gameplay event where the English target becomes complete.

It must not wait for the visual projectile to reach the target.

~~~text
correct final key
-> reveal VI + IPA immediately
-> queue pronunciation
-> projectile/explosion continue as visual feedback only
~~~

This keeps learning feedback readable for fast typists and prevents target distance on the canvas from adding an artificial delay.

Reveal duration remains controlled by the existing Shooter setting.

Projectile animation must remain visible but responsive. Current rule:

~~~text
SHOT_MIN_SPEED = 1800 px/s
SHOT_MAX_TRAVEL_SECONDS = 0.22
~~~

Shot speed scales with target distance so distant targets do not create a long visual delay.

Current reviewed Vocabulary Shooter revision:

~~~text
9f8afde6b1c1fdf6748928e8937c0d5e6f0d1917
~~~


---

# 82. Shared background music

Background music is a parent Portal responsibility, not a per-game feature.

Persistent ownership:

~~~text
typing-game Portal
└── SharedMusicPlayer
    ├── Local audio
    └── YouTube

route content
├── Monkeytype iframe
├── Shooter iframe
├── Recall iframe
└── Karaoke iframe
~~~

The Portal shell is persistent while route content changes. Shared music therefore continues from the same timestamp when navigating between non-Karaoke games.

Local library:

~~~text
shared/music/
pnpm music:index
-> shared/music/index.local.json
~~~

The local index is generated and ignored by Git. Audio files in `shared/music/` are ignored by Git. The tracked `shared/music/index.json` is the empty/fallback manifest.

Supported indexed extensions:

~~~text
.mp3
.m4a
.aac
.wav
.ogg
.webm
~~~

YouTube tracks are stored as metadata in Portal localStorage and played through the YouTube IFrame Player API.

Playback modes:

~~~text
auto-next
repeat-one
~~~

Auto-next is the default and wraps at the end of the combined Local + YouTube list.

Music settings:

~~~text
music volume
playback mode
pronunciation ducking enabled/disabled
pronunciation music level
~~~

Default audio-balance policy:

~~~text
normal music volume = 0.32
ducking enabled = true
ducked multiplier = 0.18
duck attack = 55ms
speech release debounce = 160ms
restore fade = 220ms
~~~

Child speech events use:

~~~text
postMessage({
  type: "typing-game:speech",
  active: true|false
})
~~~

The Portal validates the sender against the registered current game iframe before applying ducking.

Shooter, Recall and Monkeytype EN-VN pronunciation send speech focus. Monkeytype Text Reader also signals playing/paused/idle state.

Karaoke rule:

~~~text
enter Karaoke
-> pause shared background music

leave Karaoke
-> resume only if shared music was active before Karaoke
~~~

Shooter rule:

~~~text
shared music active
-> mute Shooter procedural BGM
-> keep Shooter SFX
-> keep pronunciation

shared music inactive
-> Shooter procedural BGM may run if its Fallback music setting is enabled
~~~

Current reviewed child revisions:

~~~text
games/monkeytype
6227c28425b8f640e65b20b5f9371dc891369d03

games/vocab-shooter
15a5f4616acade800fc524fbd27b18ef70117387

games/recall-typing
4e007393e3fc61ce431392c70791015c5e3695cc
~~~


---

# 83. Portal full-height iframe contract

The persistent Portal shell introduced for shared background music must keep a definite height chain from the Portal grid row to every child game iframe.

Required contract:

~~~text
.portal-shell
height: 100%
grid-template-rows: 48px minmax(0, 1fr)

.route-host
height: 100%
min-height: 0

.game-stage
height: 100%
min-height: 0
overflow: hidden

.game-frame
position: absolute
inset: 0
width: 100%
height: 100%
~~~

Without this contract browsers may fall back to the default iframe height (about 150px), causing every game to appear clipped at the top with the remaining Portal area blank.

Validation:

~~~text
node scripts/validate-portal-layout.mjs
~~~

Platform CI runs this validation before builds.


---

# 84. Recall vocabulary source confirmation UX

Recall Typing uses the same Vocabulary source interaction contract as Vocabulary Shooter.

~~~text
Class tab
-> choose a level
-> Use level
-> Applying…
-> load succeeds
-> persist Class source
-> replace Recall vocabulary
-> dialog closes
-> Recall returns to ready
-> success notice

Custom tab
-> edit/save vocabulary
-> persist Custom source
-> dialog closes
-> Recall returns to ready
-> success notice
~~~

Switching Class/Custom tabs alone never changes the active vocabulary source.

Current reviewed Recall revision:

~~~text
c62a3ee9927fce9b27d7526df1972e1913866a83
~~~


---

# 85. Shared music Shuffle mode

Shared background music supports:

~~~text
shuffle
auto-next
repeat-one
~~~

Shuffle is the default playback mode.

Shuffle uses a bag instead of choosing a completely independent random track every time.

Rules:

~~~text
playlist size = 0
-> no playback

playlist size = 1
-> the only track may repeat

playlist size >= 2
-> do not immediately choose the current track
-> play each shuffled remaining track before refilling the bag
-> refill with all tracks except the current track
~~~

The bag contains the merged Local + YouTube music library.

If Shuffle is active and no track is selected, Play automatically chooses a random first track.

Legacy Music state created before Shuffle is migrated once from the old default `auto-next` to `shuffle`. A version marker preserves explicit future choices of Auto next.

The Music transport button shows `Shuffle →` in Shuffle mode.


---

# 86. Space Typing platform integration

Space Typing is now integrated as an independent child repository.

Repository and submodule:

~~~text
sinhvienaiti/space-typing
games/space-typing
branch: main
~~~

Platform route and internal origin:

~~~text
https://typing-game.local/space-typing
https://space.typing-game.local
~~~

Development port:

~~~text
3004
~~~

Focused development command:

~~~bash
./dev.sh space
~~~

Normal Play mode includes Space Typing and rebuilds it when its static output is missing or stale:

~~~bash
./play.sh
~~~

The child game's authoritative product/design/implementation source of truth is:

~~~text
games/space-typing/docs/PROJECT_CONTEXT.md
~~~

When reviewing Space Typing, do not infer requirements from Monkeytype, Vocabulary Shooter,
Recall Typing or Karaoke Typing except where the Space Typing context explicitly references a
shared parent-platform contract such as vocabulary, typing texts, shared music or Portal routing.

The parent pins a tested child commit through the normal Git submodule workflow.

Current reviewed child gameplay checkpoint after Review Pass #1 and Review Pass #2:

~~~text
9b9367479b0d47216cb7a13a859a5c38f0511dc6
~~~

Child push CI #131 passed on this exact checkpoint before the final parent pin update.

Space Typing requires these shared-data routes on its own internal origin in both Dev and Play nginx modes:

~~~text
/vocabulary/             -> shared/vocabulary/
/shared/typing-texts/    -> shared/typing-texts/
~~~

Platform CI runs `pnpm validate:space-integration` to protect all existing game routes/origins while validating the Space Typing integration contract.
