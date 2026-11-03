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

Cross-game project skills (01/11/2026; reusable know-how lives in skills, docs are for handoff and records): `game-art-pipeline` (making art and media with AI tools, blind judging at 8.5, Tripo, licences), `game-map-concept` (a map concept from the real play camera before building), `game-character-design` (research-first character design, the appeal checklist, four consistent views), `game-hero-presence-vfx` (halos, motes, rim glow and other presence layers, built and judged one by one). They apply to every game in this repo, Space Typing included.

Making any VFX, CGI or SFX starts with the `game-vfx-production` skill (owner, 04/11/2026: "luôn ưu tiên dùng blender hoặc fire[fly] nếu 2 thứ này làm tốt hơn bạn"). The look comes from the best art tool (Firefly Video or Image, Blender sims rendered to flipbooks, painted masks), and code only places, times and animates it. Code-drawn flames, auras, stars, cracks and scorch were rejected as crude, "under 6". `game-vfx-layered` and `game-hero-presence-vfx` follow it for phases and always-on layers.

Three companion skills the owner supplied (04/11/2026) apply after it:
- `game-vfx`: readability, hierarchy, performance, licence and the VFX scorecard, with two consecutive passes;
- `game-cgi`: cut-ins, cinematics, character beauty and continuity;
- `game-sfx`: sound design, Web Audio runtime and the combat mix.

Where they differ from the owner's rules in this file, these rules win.

Combat and skill VFX in every game (Dragonhold, Last Line, Wordwoven,
Tu Tiên Thủ Ải and later games) follow
[the layered VFX standard](docs/games/VFX_STANDARD.md) through the
`game-vfx-layered` skill; skills the owner reviews first are built in a
dev-only lab before they go into the game. Every shot, skill, trap or enemy attack has five
phases (charge, release at the caster, travel, impact, aftermath), the caster
side first. Every VFX brief names the standard, the reference image, the
action class, the capture scenario and the acceptance numbers.

## Plan with ChatGPT and Gemini (owner, 04/11/2026)

"trước khi triển khai gì, nên tham khảo ý kiến của cả chatgpt và gemini để bổ sung ý tưởng cho nhau để đưa ra 1 plan tốt nhất, tối ưu nhất".

Before building any feature, effect, art, system or rework:
1. Give ChatGPT (Chat mode, thinking High, never Work) and Gemini (4 Argon, High) the same brief.
2. Send each the other's key ideas for a second round, so they complement each other.
3. Verify their key claims at the sources.
4. Merge everything into one plan that says what each contributed and where you disagree. Only then implement.

Save their answers verbatim with a check table in the game's docs `source/` folder.

Only purely mechanical work skips this step: a typo, a one-line bug fix, re-running a measurement, moving files.

## Language, names and art level (owner, 28/10/2026, night)

These are English games. Everything the player reads is in English:
- titles, menus, buttons, hints, briefings, results, tooltips;
- game nouns (towers, traps, houses, units, enemy kinds, items, guns).

Vietnamese stays only where the game teaches it: the meaning of the word being learned (for example "thank · cảm ơn"), and optional glosses inside learning panels.

The games are named **Dragonhold** (was Rồng Giữ Ải), **Wordwoven** (was Lời Gọi) and **Last Line** (was Tuyến Cuối). Unique characters keep their proper names (the dragons, Draconis, named bosses).

The 27/10 rule (English nouns inside Vietnamese sentences) is replaced. Convert the existing text in a per-game language pass, not in passing.

Art must reach commercial-game level. Backgrounds, title screens, key art, map scenes and skies are scored against a board of commercial-game references (epic, majestic, cinematic light), not against our own style guide. Nothing the player sees is a code-drawn stand-in for art: no SVG or canvas scenery, no CSS-shape icons, no emoji, no fallback paintings. Shaders and VFX that meet the VFX standard are fine. Every UI detail carries real art, not text alone. Sound is real audio files made through `docs/games/AUDIO_PIPELINE.md`, not synthesized placeholders.

3D models favour detail over weight (owner, 29/10/2026): no model a player sees up close goes under 2,000 triangles; keep the Tripo originals' face count, normal and roughness maps where the floors in `docs/games/MODEL_QUALITY.md` say so; cut only when measured frame time breaks the budget, in the order that doc gives. Existing models stay as they are until the owner asks.

Acceptance bar 8.5, no provisional passes (owner, 01/11/2026): "tôi không muốn dùng tạm được nữa, tôi muốn phải đạt trên 8.5 trở lên". Every piece the player sees is accepted only when two independent blind judges both score it 8.5 or higher in the built play host at the player's settings, with no URL flags. This covers art, 3D models, maps, VFX, UI and audio, 2D and 3D alike. There is no "best of 3 tries" and no "better than before" pass. Anything already wired below 8.5 (marked provisional) is an open debt to redo to 8.5, not done work. Shared systems keep their bar of 9.

Appeal is the goal (owner, 01/11/2026, evening): "phần hình ảnh chúng ta phải làm nó thật đẹp, nhìn cuốn hút, phong cách, sang trọng, thời trang, hiện đại… đừng làm hình ảnh của game trở nên nhàm chán, đơn giản, thiếu đi sự hấp dẫn". Visuals and effects are the focus. Every visual brief (art, models, maps, VFX, UI) asks for captivating, stylish, luxurious, fashionable, modern design with rich detail: layered forms, premium materials, light accents, strong silhouettes. Judges score appeal next to market level, and a piece that is technically clean but plain, simple or generic fails the 8.5 bar. For subjective designs (heroes, title art, key UI), show the owner options before building on one.

Effects around objects are essential (owner, 03/11/2026): "những hiệu ứng như vậy xung quanh vật phẩm, trang bị, kỹ năng là rất cần thiết, nó đem lại cái nhìn cho người chơi hứng thú hơn". Every item, piece of equipment, weapon and skill object the player sees carries a planned presence layer around it: a flying sword, talisman, relic, drop, shop item or equipment card gets an aura or sheath, motes, streamers, afterimages or a rarity glow. It is planned in the first brief, not added later as polish. The layer dresses the real model or art and never hides or replaces it. Swapping a code-drawn stand-in for real art removes the stand-in, not the aura. Skills: `game-hero-presence-vfx` (objects), `game-vfx-layered` (what travels).

Skill effects sparkle too (owner, 03/11/2026, later the same day): "bạn luôn thiếu các hiệu ứng xung quanh… bây giờ là với kỹ năng, bạn cũng cần phải xử lý để nó lấp lánh, long lanh hào quang đẹp hơn".
- Every phase of a skill carries a radiance layer around its main shape. The phases are charge, release, travel, impact and aftermath; the main shape is the flame, slash, seal, burst, beam or field.
- The radiance layer is made of glints and star twinkles, fine light motes and glitter, soft halos and light rings (at most 0.9 a channel), shimmering rims and thin light rays.
- No main shape ships bare. Its radiance is designed in the first brief, beside the shape, and judged with it. Skill: `game-vfx-layered`, method step 3.

Research before any character design (owner, 01/11/2026, evening): before briefing a hero, companion, dragon, boss or named character, research myth and legend, xianxia, royal and warrior references and run the character appeal checklist (skill `game-character-design`). Every character gets a radiance kit (a halo or mandorla, emissive channels, light motes or orbiting ornaments, a cape or ribbons in motion). Which parts are model geometry and which are engine VFX follows the researched pipeline decision in that skill (`references/pipeline-decision.md`), not a guess. Show the owner a few directions before building one.

Reuse monsters before making new ones (owner, 01/11/2026): every game already has 3D foes, and many of them have rigs and clips. Before any new monster model or monster image, search `docs/games/MONSTER_MODEL_INVENTORY.md` and reuse across games first: retexture, recolour, rescale, re-rig. A ticket for a new monster says why nothing in the inventory fits.

Shared systems need 9 or more (owner, 29/10/2026): the typing feedback (focus strip and letter effects), the Audio Lab keyboard sound profiles and character animation are reused across games, so each is accepted only when two independent judges both score it 9 or higher, compared with the references in `docs/games/SHARED_SYSTEMS_BAR.md`; the owner signs off last.

Every game has a Settings gear and a Sound speaker in play (owner, 29/10/2026), opening overlay panels for general and audio settings without leaving the game; one kit component, spec in `docs/games/IN_GAME_SETTINGS.md`.

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
