# Agent guidance

## Game development skills

For broad Space Typing tasks, start with
[space-typing-director](.agents/skills/space-typing-director/SKILL.md).
For a focused task, load only the relevant project specialist and its references.
Project contracts and the current source take precedence over generic skill defaults;
plans and checkpoints must be checked against the current implementation.

Use installed OpenAI Game Studio and `threejs-*` specialists for engine, graphics,
assets, UI implementation, profiling and browser QA. Their scaffolds and release
checklists do not expand the user's task or replace existing project architecture.

Canonical project skills live in `.agents/skills`. Update those first; use
`bash scripts/sync-agent-skills.sh` for conflict-checked Claude copies.
Launch the agent from the parent project root; an independently opened Git
submodule does not inherit these parent skill folders.
See [setup and validation](docs/AGENT_SKILLS_SETUP.md) for commands and discovery.

## Skills by game

The project skills in `.agents/skills` are written for Space Typing. The games
split out of it ([split plan](docs/games/SPLIT_PLAN.md)) follow their own design
docs and use Game Studio and `threejs-*`; a Space skill is reference only there.

| Game | Skills | Design source |
| --- | --- | --- |
| Space Typing (`games/space-typing`) | `.agents/skills`, from `space-typing-director` | Space docs, `contracts/` |
| Rồng Giữ Ải (`games/dragon-hold`) | Game Studio, `threejs-*` | [`docs/games/dragon-lane`](docs/games/dragon-lane/DESIGN.md) |
| Lời Gọi (`games/typing-defense`) | Game Studio, `threejs-*` | the game's `docs/` (`docs/td` in Space until the split) |
| Tuyến Cuối (`games/typing-survival`) | Game Studio, `threejs-*` | the game's `docs/` (`docs/survival` in Space until the split) |
| Tu Tiên Thủ Ải (`games/immortality-cultivation`) | Game Studio, `threejs-*` | [`docs/games/tu-tien`](docs/games/tu-tien) |
| Portal, nginx, launch scripts | `game-ci-resumable` for CI/Git resumes | [split plan](docs/games/SPLIT_PLAN.md) §9–10 |

Combat VFX in Rồng Giữ Ải, Tuyến Cuối and Lời Gọi follow
[the layered VFX standard](docs/games/VFX_STANDARD.md) through the
`game-vfx-layered` skill. Every shot, skill, trap or enemy attack has five
phases (charge, release at the caster, travel, impact, aftermath), the caster
side first. Every VFX brief names the standard, the reference image, the
action class, the capture scenario and the acceptance numbers.

## In-game names (owner, 27/10/2026)

The games teach English, so the player sees game nouns in English: towers,
traps, houses, units and soldiers, enemy kinds, items, guns (for example
"Pine Bomb", not "Bom Hạt Thông"). Sentences, hints and menus stay Vietnamese
around those names, and a name's first showing (debut card, shop tooltip) may
add a short Vietnamese gloss. Unique characters keep their proper names (the
dragons, Draconis, named bosses). Any new or reworded player-facing text uses
English nouns; existing names change in a per-game naming pass, not in passing.
