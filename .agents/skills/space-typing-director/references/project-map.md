# Sources and routing

Re-read affected code on current HEAD. Links resolve from the installed skill.

| Source | Use |
| --- | --- |
| [Parent context](../../../../docs/PROJECT_CONTEXT.md) | Platform boundaries, shared learning and integration. |
| [Game context](../../../../games/space-typing/docs/PROJECT_CONTEXT.md) | Product contracts, typing combat and no manual movement. |
| [Parent scripts](../../../../package.json), [game scripts](../../../../games/space-typing/package.json), [submodules](../../../../.gitmodules) | Actual commands, dependencies and ownership. Run commands from the owning repository. |
| [Shared learning](../../../../shared/learning) | Parent owns mastery/review persistence; child emits evidence at committed activity boundaries, not each key. |
| [Shared voice](../../../../shared/voice) | Reusable ASR contracts; inspect adapters before gameplay changes. |
| [Admin V2 plan](../../../../docs/SPACE_TYPING_ADMINISTRATOR_ADMIN_V2_MASTER_PLAN.md), [admin implementation](../../../../admin) | Authoring goals versus actual validation, persistence and runtime capability. |
| [CI continuation policy](../../../../docs/SPACE_TYPING_CI_CONTINUATION_POLICY.md) | Resume rules, including missing historic CI logs. |
| [Claude handoff](../../../../games/space-typing/docs/CLAUDE_PROCESS_2026-10-17.md) | Prior decisions and pending work; Windows/WSL paths describe that host. Detect current host/tools. |
| [Defense V2](../../../../games/space-typing/docs/SPACE_TYPING_DEFENSE_PLAN_V2_2026-10-18.md) | Draft design. [Benchmark HTML](../../../../games/space-typing/defense-bench.html) and [source](../../../../games/space-typing/src/bench/defense-bench.ts) demonstrate render load, not Defense gameplay. |

## Generic implementation expertise

The project specialist owns product contracts; a generic specialist supplies
implementation technique when needed. For a focused task, one project skill may
suffice. Select one primary generic specialist for the current need, then load
another only for a concrete dependency or unresolved gap. Resolve paths from the
host catalog and read only relevant references. Once this project router has
assigned the work, continue with specialists; use a generic director only when
its broader design workflow adds something the task still needs.

| Current need | Project owner | Primary technique; alternative when useful |
| --- | --- | --- |
| Vanilla Three.js runtime | Gameplay or asset specialist by ownership | `game-studio:three-webgl-game`; Majid gameplay for new systems |
| GLB preparation/export | `game-asset-2d-to-3d` | `game-studio:web-3d-asset-pipeline`; a generation specialist only for actual generation |
| Art direction, lighting, materials, shaders | Asset or combat specialist | `threejs-aaa-graphics-builder` |
| HUD/menu implementation | `game-ui-ux-review` | Choose `game-studio:game-ui-frontend` or `threejs-game-ui-designer` for the task |
| Measured frame/runtime regression | `game-performance-quality` | `threejs-debug-profiler` |
| Browser evidence | `space-typing-playtest` | Choose `game-studio:game-playtest` or `threejs-qa-release` by available tooling |
| Sprite strips | Asset or combat specialist | `game-studio:sprite-pipeline` |
| Generated 2D, 3D or audio | Asset or combat specialist | Available imagegen or matching `threejs-*` generator; follow tool/authorization requirements |

IME, voice, Duel authority, economy and Admin authoring start with their project
specialists; a generic engine skill does not replace those contracts. For
Monkeytype work, follow [its own guidance](../../../../games/monkeytype/AGENTS.md)
and current source instead of applying Space Typing defaults.

Game Studio also includes `game-studio:game-studio`, `game-studio:web-game-foundations`, `game-studio:phaser-2d-game`
and `game-studio:react-three-fiber-game`. Space Typing currently uses vanilla Three.js; installing
the pack does not justify changing engine. Providers are optional. Prefer available
built-in image generation when appropriate; service access, licenses and expenditure
remain task-specific. See [setup](../../../../docs/AGENT_SKILLS_SETUP.md) for provenance.

## Compatibility before reusing recipes

Read the owning package manifest and lockfile, then identify the active renderer
from its consumer. The game pins Three.js and its types to `0.170.0` at this
checkpoint; this is a snapshot, not a requirement to keep that version forever.
Check imported API paths, shader chunks, color/tone-mapping behavior and loader
or post-processing assumptions against the installed version. WebGLRenderer
recipes and WebGPU/TSL recipes are not interchangeable. Adapt a recipe to the
existing renderer; upgrading dependencies or changing renderer needs its own
task scope. For Blender, follow the executable/version check in the
[asset preparation reference](../../game-asset-2d-to-3d/references/asset-map.md#preparation).
