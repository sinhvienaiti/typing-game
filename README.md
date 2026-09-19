# Typing Game

Local platform for Monkeytype, Vocabulary Shooter, Recall Typing and future learning games.

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
```

Internal origins:

```text
https://monkeytype.typing-game.local
https://shooter.typing-game.local
https://recall.typing-game.local
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

All games:

```bash
pnpm setup:dev
pnpm dev
```

Only Portal + Monkeytype:

```bash
pnpm dev:monkeytype
```

Only Portal + Shooter:

```bash
pnpm dev:shooter
```

Only Portal + Recall Typing:

```bash
pnpm dev:recall
```

## Daily / Play mode

```bash
pnpm build:local
pnpm setup:play
```

After a static build exists, normal use only needs nginx and the browser:

```bash
pnpm play
```

or simply open `https://typing-game.local` if nginx is already running.

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

Meaningful implementation or infrastructure changes should update the current day's changelog and the project context in the same Git workflow.
