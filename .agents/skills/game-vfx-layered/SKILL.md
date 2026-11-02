---
name: game-vfx-layered
description: "Build or review combat and skill VFX in any game of this repo (Dragonhold, Wordwoven, Last Line, Tu Tien and later games) as layered effects with all five phases: charge, release at the caster, travel, impact, aftermath. Use for any shot, skill or spell (xianxia sword arts, formations and talismans included), ultimate, trap, enemy attack, death or boss effect. Also use when building a skill demo or VFX lab for the owner to review before the effect goes into the game, and for \"pale\", \"weak\" or \"plain\" feedback complaints. Not for a character's always-on glow (game-hero-presence-vfx), and not for making source images, textures or audio or judging art (game-art-pipeline)."
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

## Method

1. **Trace the event.**
   - Find the sim event that starts the action and its timing: wind-up, release and strike ticks, and the delay to impact.
   - VFX lives in the view only. It never changes sim, content or goldens.
2. **Pick the action class** (§3.3: key, basic shot, rapid fire, skill, ultimate, trap, enemy attack, death, boss) and take its required layers per phase.
3. **Give each action its own shape.** Every gun, skill or spell gets its own flash, projectile, hit and smoke shapes, not one sprite atlas recoloured.
   - Last Line's audit found five guns sharing one star, which the owner called plain.
   - In a xianxia game, a sword art, a formation, a talisman and a thunder strike each read as a different thing.
4. **Build the caster side first.**
   - A (charge) and R (release at the mouth, muzzle, hand or tower) come before I (impact). This was the owner's complaint of 28/10.
   - Key-to-release stays ≤ 50 ms. A clip follows typing progress; it never holds the shot back.
5. **Layers and timing** in frames at 60 Hz (§3.4):
   - A flash is fully bright on its first frame: write a new burst at age 0, never one frame late.
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
8. **Sound with every effect.**
   - Each phase that flashes also sounds, on the same frame.
   - Combat and skill sounds are layered, loud by tier, explosive and reverberant ([game-art-pipeline audio](../game-art-pipeline/references/audio.md) §5). The soft key-sound rules apply only to keys and light UI.
9. **Textures and flipbooks:**
   - Firefly Video flipbooks (Adobe models only) and CC0 packs (Unity Labs, Kenney, ambientCG, JangaFX free sets) through game-art-pipeline.
   - Record every source in the game's THIRD_PARTY list.

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

## Techniques beyond this repo

Claude reads these files directly; they are not loaded as skills here:
- `~/.agents/skills/threejs-aaa-graphics-builder/references/{technical-art,shader-cookbook,visual-scorecard}.md`
- `~/.agents/skills/threejs-gameplay-systems/references/game-feel.md`

Space Typing's [combat-vfx-audio](../combat-vfx-audio/SKILL.md) is reference only for the split games.
