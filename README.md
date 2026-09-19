# Typing Game

Local platform for Monkeytype, Vocabulary Shooter and future learning games.

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
    └── vocab-shooter/    -> sinhvienaiti/vocab-shooter
```

## URLs

```text
https://typing-game.local/
https://typing-game.local/monkeytype
https://typing-game.local/vocab-shooter
```

Internal origins:

```text
https://monkeytype.typing-game.local
https://shooter.typing-game.local
```

## First setup

```bash
cd /Users/jokerit/htdocs
git clone --recurse-submodules https://github.com/sinhvienaiti/typing-game.git
cd typing-game
nvm use
pnpm bootstrap
```

Add to `/etc/hosts`:

```text
127.0.0.1 typing-game.local monkeytype.typing-game.local shooter.typing-game.local
```

Create one mkcert certificate for all three hosts, then use `pnpm setup:dev` or `pnpm setup:play`.

## Development

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

- [Project context](./docs/PROJECT_CONTEXT.md) - current architecture, requirements, repositories, runtime modes, important implementation rules, and known technical decisions.
- [Change log overview](./docs/changelog/README.md) - chronological index by day.
- [2026-09-19 detail](./docs/changelog/2026-09-19.md) - detailed initial platform integration history.

For future work, meaningful implementation or infrastructure changes should update the current day's change-log file and the change-log overview in the same Git workflow.
