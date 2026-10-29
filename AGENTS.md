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

## Language, names and art level (owner, 28/10/2026, night)

These are English games. Everything the player reads is in English:
- titles, menus, buttons, hints, briefings, results, tooltips;
- game nouns (towers, traps, houses, units, enemy kinds, items, guns).

Vietnamese stays only where the game teaches it: the meaning of the word being learned (for example "thank · cảm ơn"), and optional glosses inside learning panels.

The games are named **Dragonhold** (was Rồng Giữ Ải), **Wordwoven** (was Lời Gọi) and **Last Line** (was Tuyến Cuối). Unique characters keep their proper names (the dragons, Draconis, named bosses).

The 27/10 rule (English nouns inside Vietnamese sentences) is replaced. Convert the existing text in a per-game language pass, not in passing.

Art must reach commercial-game level. Backgrounds, title screens, key art, map scenes and skies are scored against a board of commercial-game references (epic, majestic, cinematic light), not against our own style guide. Nothing the player sees is a code-drawn stand-in for art: no SVG or canvas scenery, no CSS-shape icons, no emoji, no fallback paintings. Shaders and VFX that meet the VFX standard are fine. Every UI detail carries real art, not text alone. Sound is real audio files made through `docs/games/AUDIO_PIPELINE.md`, not synthesized placeholders.

3D models favour detail over weight (owner, 29/10/2026): no model a player sees up close goes under 2,000 triangles; keep the Tripo originals' face count, normal and roughness maps where the floors in `docs/games/MODEL_QUALITY.md` say so; cut only when measured frame time breaks the budget, in the order that doc gives. Existing models stay as they are until the owner asks.

## Test captures (owner, 28/10/2026)

Browser and render captures go under the game's own `tmp/` (or the
worktree's), never into `art-src`, `public` or `docs`. Raw frames filled the
disk on 28/10: 77 GB of PNG and JPG in `tmp/`. So when a capture step ends,
the agent that took the frames keeps only what the report needs (contact
sheets, compare shots, images a doc links, numbers as JSON or Markdown) and
deletes its own raw frames with
`node tools/capture-prune/prune.mjs <its capture folder> --apply` (run it
without `--apply` first to see the list). It never deletes files it did not
create.
`.local/bin/heavy.sh --gpu` makes a browser run wait while less than 10 GB is
free, then gives up with exit 75.
