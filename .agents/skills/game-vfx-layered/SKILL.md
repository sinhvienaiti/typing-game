---
name: game-vfx-layered
description: "Build or review combat and skill VFX in any game of this repo (Dragonhold, Wordwoven, Last Line, Tu Tien and later games) as layered effects with all five phases: charge, release at the caster, travel, impact, aftermath. Use for any shot, skill or spell (xianxia sword arts, formations and talismans included), ultimate, trap, enemy attack, death or boss effect. Also use when building a skill demo or VFX lab for the owner to review before the effect goes into the game, when designing or redesigning a whole skill catalog or kit, when skills feel weak, small or unimpressive (screen effects, foe reactions, damage numbers, cut-ins, callouts), and for \"pale\", \"weak\" or \"plain\" feedback complaints. Not for a character's always-on glow (game-hero-presence-vfx), and not for making source images, textures or audio or judging art (game-art-pipeline)."
---

# Layered combat and skill VFX

**The standard:** [docs/games/VFX_STANDARD.md](../../../docs/games/VFX_STANDARD.md) (Vietnamese). Read §3 before building and §5.6 before claiming done.

**References:**
- The owner's reference for layering is `tmp/vfx/owner-reference-layered-vfx.webp` (ignored): nine simple layers composed into one effect.
- Lessons from the first three games: [LESSONS_FROM_THREE_GAMES.md](../../../docs/games/LESSONS_FROM_THREE_GAMES.md) §5 (VFX and light) and §6 (sound).

**Each game's own sources win over this skill for that game:**
- **Tu Tien:** the VFX list in five phases is `docs/games/tu-tien/ART_AUDIO_VFX_PLAN.md` §6, the canon is `docs/games/tu-tien/00-canon.md`, the texture list and budgets are in the same plan.
- **Last Line:** `games/typing-survival/docs/ALIVE_PLAN.md` (AL-08 guns).
- **Dragonhold:** `docs/games/dragon-lane/`.

## Style target

Spectacle, not realism (owner, 02/11/2026: "chúng ta k làm ra kiểu âm thanh như thật, hay hình ảnh hiệu ứng như thật… phải bùng nổ, đẹp, hào quang, thu hút của các phim anime hoặc các thần thoại, tiểu thuyết"). Skill and combat VFX aim at anime, donghua and mythic spectacle: explosive bursts, radiant halos and auras, luminous trails, glowing runes and sigils, sparkle and light shafts, bold shapes with strong colour accents, the way Genshin Impact, Honkai: Star Rail, Wuthering Waves and donghua such as Soul Land or Battle Through the Heavens stage a skill. Physically plausible but plain effects fail. The bloom and white-out limits below keep spectacle readable; they never justify a dull effect.

## Smooth motion

Owner, 02/11/2026: "đảm bảo animation của các chiêu thức phải mượt, và lưu ý về animation của nhân vật cũng vậy, từng cử chỉ, yển chuyển của chân tay, cơ thể, đầu cũng cần phải xử lý thật mượt". Every layer eases in and out (no sprite or ribbon pops on or off), blades and trails never snap between poses, motion is frame-rate independent, and a fixed-step sim is drawn with render interpolation. The caster's clips cross-fade or inertialize; turning and moving are damped, never instant. Check it on frame sheets and on a half-speed clip, and measure pops (a layer's alpha or size jumping more than 30 % in one frame outside an intended flash). When two judges score motion at 7 or more, send the owner a movement demo with what is done so far; keep going to 8.5.

## Method

1. **Trace the event.**
   - Find the sim event that starts the action and its timing: wind-up, release and strike ticks, and the delay to impact.
   - VFX lives in the view only. It never changes sim, content or goldens.
   - One sim tick emits the release or strike. The caster's body, every VFX layer, the sound, the camera and the hit-stop react on that same frame. No `setTimeout`. Clip markers align to the tick and never delay the sim ([game-character-animation events](../game-character-animation/references/events-and-sync.md)).
2. **Pick the action class** (§3.3: key, basic shot, rapid fire, skill, ultimate, trap, enemy attack, death, boss) and take its required layers per phase.
3. **Give each action its own shape.** Every gun, skill or spell gets its own flash, projectile, hit and smoke shapes, not one sprite atlas recoloured.
   - Last Line's audit found five guns sharing one star, which the owner called plain.
   - In a xianxia game, a sword art, a formation, a talisman and a thunder strike each read as a different thing.
   - **Dress what travels** (owner, 03/11: "những hiệu ứng như vậy xung quanh vật phẩm, trang bị, kỹ năng là rất cần thiết, nó đem lại cái nhìn cho người chơi hứng thú hơn"). A flying sword, talisman, bullet or thrown relic carries an aura for its whole flight: a sheath in the element's material, afterimages, streamers, motes or a tip star, chosen from [game-hero-presence-vfx](../game-hero-presence-vfx/SKILL.md)'s layer menu.
     - A bare model in flight reads crude, even a good one.
     - On 03/11, Tu Tien swapped code-drawn swords for the real model and dropped every layer around the blade, and the owner found the flying swords crude.
     - Swapping in real art removes the stand-in, never the aura. The aura wraps the object and keeps it readable as itself.
   - **Every shape sparkles.** The owner, later on 03/11: "bạn luôn thiếu các hiệu ứng xung quanh… bây giờ là với kỹ năng, bạn cũng cần phải xử lý để nó lấp lánh, long lanh hào quang đẹp hơn".
     - The main shape of each phase carries a radiance layer around it: a charge, release flash, flame, slash, seal, beam, burst or burning ground.
     - The radiance layer is made of glints and star twinkles, fine motes and glitter, soft halos and light rings (≤ 0.9), shimmering rims and thin rays.
     - Brief it beside the shape, judge it with the shape, and keep it off word tags and foes.
     - Tu Tien's first Sword × Fire had flames, seals and slashes with no sparkle around them. The owner found them plain even after the colour fixes.
4. **Build the caster side first.**
   - A (charge) and R (release at the mouth, muzzle, hand or tower) come before I (impact). This was the owner's complaint of 28/10.
   - Key-to-release stays ≤ 50 ms. A clip follows typing progress; it never holds the shot back.
5. **Layers and timing** in frames at 60 Hz (§3.4):
   - A flash is fully bright on its first frame: write a new burst at age 0, never one frame late.
   - **Fast attack, slow decay.** Impact and aftermath linger: hold the peak a moment, then burn down by erosion and cooling, never a quick alpha fade.
     - The owner, 03/11/2026, on Tu Tien's fire: "hình như tôi thấy hiệu ứng bị biến mất hơi nhanh". The impact flame then lived about 0.6 s.
     - A slowed flipbook blends frames or holds and erodes; it never drops to a visibly lower frame rate.
     - In crowded skills, cap the lingering pieces so they never veil the field, word tags or foes. Grow pools so nothing is cut short.
   - Layers are offset 2–3 frames.
   - Put a dark layer behind bright ones.
   - The core is at most 30 % white.
   - Enemy colours never use our fire ramp. Hits carry the attacker's colour; a dying foe glows in its own faction's colour.
6. **Light and bloom** (LESSONS §5; verified in Last Line on 01/11):
   - Only thin HDR cores (3–6) bloom. Halos and rings stay at or below 0.9 per channel.
   - Bloom strength 0.4–0.5, radius 0.1–0.15; Neutral tone mapping.
   - Smoke is dark puffs with normal blending, never additive grey. A smoke shader that writes the floor's depth lies on the ground, so foes and characters stand over it.
   - Under MSAA an edge pixel is shaded past its triangle: clamp before `pow()`, or NaN black blocks spread through the bloom.
   - Never lower bloom globally to fix one effect. That killed the shared typing marks once.
7. **Budgets** (§3.7): stay inside the game's measured frame headroom per tier, measured before adding lights or bloom.
   - Dragonhold High had about 2 ms left (28/10).
   - Last Line High had about 0.7 ms left (02/11).
   - Measure a new game first.
   - When headroom is tight, add an overdraw count (transparent layers per pixel, against the §3.7 caps) to the lab capture's `meta.json`.
   - **Retina screens:**
     - On the M4 at 1920×1080 CSS, a fixed DPR 2 frame cost 3–6× the DPR 1 frame, and MSAA 4 added about 3 ms even at DPR 1 (Tu Tien, 03/11/2026).
     - Use dynamic resolution instead of a fixed ratio: `games/immortality-cultivation/src/view/dynamic-resolution.ts` with the renderer's `pinPixelRatio`.
     - Pin the ratio for captures and perf runs so numbers compare.
8. **Sound with every effect.**
   - Each phase that flashes also sounds, on the same frame.
   - Combat and skill sounds are layered, loud by tier, explosive and reverberant ([game-art-pipeline audio](../game-art-pipeline/references/audio.md) §5). The soft key-sound rules apply only to keys and light UI.
9. **Textures and flipbooks:**
   - Firefly Video flipbooks (Adobe models only) and CC0 packs (Unity Labs, Kenney, ambientCG, JangaFX free sets) through game-art-pipeline.
   - Record every source in the game's THIRD_PARTY list.
   - Sources, render, atlas, VRAM and judging for flipbooks: [flipbooks](references/flipbooks.md).
   - **Designed marks come from painted images; the shader only animates them.** This covers cracks, scorch, cut seams, rifts, sigils, runes and impact decals.
     - The owner, 03/11/2026, on Tu Tien's code-drawn element cracks and char: "việc bạn tự style ra những cái đó nó chưa được đẹp lắm".
     - Paint a set with one set standard and 4–8 variants.
     - Pack the channels: shape, a growth or age gradient, hot lines, alpha. The shader reveals, glows, cools, erodes and adds glints from those channels.
     - Rotate, scale and flip the variants against repetition.
     - Procedural code is for noise, erosion and analytic thin rings, not for the mark's look.
     - Stars, glints and auras with motion also come from painted or Firefly Video art. On 03/11 the owner found Tu Tien's analytic tip star "thực sự không đẹp", and the shader-only sword mantle crude and static.
     - A pack image that fails (Kenney's scorch star read as ink) is replaced by a better image, never by code.

## Techniques by layer

Reuse these building blocks before writing a new pool. Short names in the table:
- **fxkit:** `games/immortality-cultivation/src/view/skills/fxkit.ts`: `SpritePool`, `RibbonPool`, `BeamPool`, `GroundSigil`, and helpers (`approach`, `lifeFade`, `pulse`, `Rand`, easings). Preallocated, no allocation per frame.
- **kit:** `shared/game-kit/three/particles.ts` (`ParticlePool`, `Ribbon`, `FlameTrail`, `LightTrail`) and the fresnel shaders in `shared/game-kit/three/materials.ts` (beam, shield, pillar).
- **DH:** `games/dragon-hold/src/view/vfx-layers.ts` (`Streak`, `ShellPool`, `StreakSparks`, `FissurePool`, `RuneCircle`) and `games/dragon-hold/src/view/flipbook.ts`.
- **feel:** `games/immortality-cultivation/src/lab/feel.ts` (`CameraKick`, `CameraShake`, `HitStop`, `FlashLights`).

| Layer | Technique | Start from |
|---|---|---|
| Ribbon trail | Camera-facing strip sampled by world time (same length at any frame rate, still in a hit-stop), UV scroll, noise, alpha shaping | fxkit `RibbonPool`; kit `Ribbon`, `FlameTrail`, `LightTrail`; DH `Streak` |
| Beam | Strip with a thin HDR core, a halo and energy ripples; soft ends | fxkit `BeamPool`; kit beam shader |
| Fresnel shell | Dome, cone, shield or shockwave mesh, bright at the rim, eroding as it fades | kit shield and pillar shaders; DH `ShellPool` |
| Ground sigil or decal | Ground plane with a procedural shader that reveals with the typing progress; cracks, scorch, runes | fxkit `GroundSigil`; DH `FissurePool`, `RuneCircle` |
| Velocity-stretched sprite | Instanced billboard stretched along its velocity; additive light or normal-blended ink; camera- or ground-facing | fxkit `SpritePool` (`stretch`); DH `StreakSparks`; kit `ParticlePool` (round points only) |
| Flipbook | Atlas frames blended in time, a pivot, soft against the ground, fire and smoke blends | DH `flipbook.ts`; `tools/vfx-flipbook`; [flipbooks](references/flipbooks.md) |
| Light | Pooled point lights built at load (idle at 0); a flash far from a lit light takes the dimmest, so no lit spot jumps | feel `FlashLights`; tier caps in VFX_STANDARD §3.7 |
| Camera | Kick on a damped spring fed impulses; shake that dies fast; hit-stop counted to part frames, easing out | feel `CameraKick`, `CameraShake`, `HitStop`; kit `shared/game-kit/feedback/hitstop.ts` |

Every layer keeps the light rule of step 6: thin HDR cores at 3–6, halos and rings at or below 0.9 a channel.

**Library decisions:**
- **three.quarks: not used.** Its current version needs three ≥ 0.182, and the kit and every game pin three 0.170.0 (their `package.json`). Its emitter and behaviour model is reading only (VFX_STANDARD §4.3).
- **pmndrs `postprocessing`: a lab A/B benchmark only,** when a tier is over budget. Adopting it needs a kit and boundary change, and a re-judge of the shared typing marks at 9. The owner decides.
- **Wawa VFX and Three-VFX: not used.**
- **WebGPU and TSL: later.** The games stay on WebGL2 with GLSL (VFX_STANDARD §4.1).

**A shared kit `vfx/` module** is extracted only when Tu Tien's first effect passes 8.5 and a second game needs the same pieces.

## Power layer: what makes a skill feel strong

An effect alone is not a skill. The owner scored a lab of good-looking blades about 6/10 because nothing around them reacted: "quá nhiều chiêu phải tích 1 lúc mới thi triển, nó không hề có hiệu ứng màn ảnh, quá thiếu đi sự khủng bố của tu tiên" (Tu Tien canon D58, 03/11/2026). Every skill ships with all of these (recipe and numbers: `docs/games/tu-tien/skills/POWER_RESEARCH.md`; building blocks in `games/immortality-cultivation/`):

- **Instant cast.** The last correct key is the release frame. The charge shows only while typing, and a new release cuts any running hit-stop. Building blocks: `src/lab/skills-main.ts`, `src/lab/feel.ts`.
- **Screen effects by tier** (basic, skill, ultimate), in `src/view/screen-fx.ts`:
  - shake from trauma squared on smooth noise, plus a FOV punch;
  - hit-stop per tier, and slow motion as a world-time scale;
  - darkening, flash and an edge-only chromatic split in one pass before the OutputPass. It never touches DOM text, word tags or the number overlay.
  - One intensity setting governs all of them.
- **Foe reactions** that change the silhouette, in `src/lab/herd.ts` and `src/lab/death-fx.ts`:
  - a 2–4 frame rim flash in the attacker's colour, and a 5–30 cm recoil along the blow;
  - a stagger only on elites and big strikes, with an immunity window so it is never restarted; the boss never moves at the root;
  - deaths that transform: a burst, wisps, ink, shards.
- **Compiled damage numbers**, in `src/view/hitfx.ts` (`SkillNumberField`) and `src/view/damage-compile.ts`:
  - per target over about 150 ms (500 ms for field-wide skills), with one cluster total when 5 or more small foes are hit;
  - crits at 120–135 % with a gold edge, placed below-right of the foe and never over word tags.
- **An ultimate cut-in** of about 1 s, after F0 has already hit. It pauses the sim and the typing timer, and uses owner-approved art only.
- **A sound bus** on the same frame, in `src/lab/sound.ts` and `src/lab/events.ts`:
  - impacts grouped per material in 30–50 ms buckets, never one sound per hit;
  - fly-bys only for the nearest 8–12 objects;
  - world-change events (open, hush, climax, close), and the callout.
- **Wide and field-wide skills.** A self-hunting field skill, in `src/view/skills/van-kiem.ts`, needs four readable states: the sky changes, the weapons gather, they visibly choose prey, and one decisive end.
  - Targeting reserves foes (by size 2, 5 or 10 weapons; retarget on death; 15–20 % scatter) and recycles instanced weapons.
- **Designing a whole skill kit:** [skill-kit design](references/skill-kit-design.md).

## Demo or lab first, then the game

When the owner wants to review skills before they ship (Tu Tien 02/11; Last Line's presence, style and typing-feedback labs), build a dev-only lab page first:
- **The game's real parts:** stage, play camera, lights, tone mapping and bloom chain, the real caster and foe models.
- **A trigger per skill:** a button and a key for each skill, plus each skill on a dummy group of foes.
- **A fixed-step clock**, so every capture of a skill shows the same frames.
- **A capture scenario** that writes frame sheets per phase at 1280×720 and 1920×1080 (play camera and close-up, light and dark ground), a short clip per skill, and the measurements below.
- **Out of the player build:** `vite build` must not ship the lab page (prove it with a grep of `dist`).

Show the owner the clips and sheets, take his notes, and wire a skill into the game only after it passes the lab.

## Acceptance

- **Measured:** the first frame reaches ≥ 95 % of peak; white-out ≤ 6 %; word-tag contrast ≥ 7:1; inside the frame budget per tier; reduced-motion versions kept (`reduced: keep | soften | drop`).
- **Judged:** two independent blind judges both score ≥ 8.5 in the built play host at the player's settings with no URL flags, beside commercial references ([game-art-pipeline judging](../game-art-pipeline/references/judging.md)). There is no best-of-three and no "better than before" pass.
  - Shared systems (typing feedback, key sounds, character animation) need ≥ 9.
  - Dragon fire in Dragonhold aims at 9.
- **Records:** write the game's changelog with before/after frame sheets at 720p and 1080p, and give the owner a short clip.
- **Three tries, then discuss** (owner, 02/11): when an effect or a motion has been reworked three times without a clear gain in the judges' scores, stop and work out a different approach with ChatGPT (show it the clips or sheets, the judges' notes and what was tried) before the fourth try. Sheets for blind judges never print metrics.

## Techniques beyond this repo

Claude reads these files directly; they are not loaded as skills here:
- `~/.agents/skills/threejs-aaa-graphics-builder/references/{technical-art,shader-cookbook,visual-scorecard}.md`
- `~/.agents/skills/threejs-gameplay-systems/references/game-feel.md`

Space Typing's [combat-vfx-audio](../combat-vfx-audio/SKILL.md) is reference only for the split games.
