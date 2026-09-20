# Typing Game

Local platform for Monkeytype, Vocabulary Shooter, Recall Typing, Karaoke Typing and future learning games.

Each game is an independent Git repository mounted under `games/` as a submodule.

## Structure

```text
typing-game/
├── portal/
├── infra/nginx/
├── scripts/
├── shared/
└── games/
    ├── monkeytype/       -> sinhvienaiti/monkeytype
    ├── vocab-shooter/    -> sinhvienaiti/vocab-shooter
    └── recall-typing/    -> sinhvienaiti/recall-typing
```

## URLs

```text
https://typing-game.local/
https://typing-game.local/monkeytype
https://typing-game.local/vocab-shooter
https://typing-game.local/recall-typing
https://typing-game.local/karaoke-typing
```

Internal origins:

```text
https://monkeytype.typing-game.local
https://shooter.typing-game.local
https://recall.typing-game.local
https://karaoke.typing-game.local
```

## First setup

```bash
cd /Users/jokerit/htdocs
git clone --recurse-submodules https://github.com/sinhvienaiti/typing-game.git
cd typing-game
nvm use
pnpm bootstrap
pnpm setup:dev
```

`pnpm setup:dev` verifies all local platform hosts in `/etc/hosts`, ensures the mkcert local CA is installed, and regenerates the shared certificate whenever any required hostname is missing from the certificate.

## Development

Recommended launcher:

```bash
./dev.sh
```

No argument means `all`. The launcher performs the normal update/start flow automatically:

```text
git pull --ff-only
→ sync/update pinned submodules
→ install/update platform + required app dependencies
→ switch nginx to dev mode
→ start Portal + selected game(s)
```

Focused runs:

```bash
./dev.sh monkeytype
./dev.sh shooter
./dev.sh recall
./dev.sh karaoke
```

Explicit all:

```bash
./dev.sh all
```

Aliases `vocab-shooter`, `recall-typing` and `karaoke-typing` are also accepted.

The lower-level commands remain available when needed:

```bash
pnpm setup:dev
pnpm dev
pnpm dev:monkeytype
pnpm dev:shooter
pnpm dev:recall
pnpm dev:karaoke
```

## Daily / Play mode

Recommended launcher:

```bash
./play.sh
```

Play mode is intentionally local-only and does **not** pull Git, update submodules, or install dependencies.

It performs only the work needed to play:

```text
stop old typing-game dev servers
→ check static outputs
→ rebuild only apps whose local source is newer than their static build
→ switch nginx to static Play mode if needed
→ open https://typing-game.local
```

If every static build is already current, no Node/Vite development server is started and no rebuild is performed.

Lower-level commands remain available when needed:

```bash
pnpm build:local
pnpm setup:play
pnpm play
```

## Submodules

Sync to the versions pinned by this platform:

```bash
git pull
git submodule update --init --recursive
```

For Monkeytype development:

```bash
git -C games/monkeytype switch feature/en-vn-translation
```

## Project documentation

The persistent project handoff and engineering history live under docs:

- [Project context](./docs/PROJECT_CONTEXT.md)
- [Change log overview](./docs/changelog/README.md)
- [2026-09-19 detail](./docs/changelog/2026-09-19.md)
- [Recall Typing design](./docs/design/RECALL_TYPING_GAME.md)
- [Karaoke Typing design](./docs/design/KARAOKE_TYPING_GAME.md)

Meaningful implementation or infrastructure changes should update the current day's changelog and the project context in the same Git workflow.
