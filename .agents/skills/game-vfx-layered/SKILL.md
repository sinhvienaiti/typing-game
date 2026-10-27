---
name: game-vfx-layered
description: Build or review combat VFX in Rồng Giữ Ải, Tuyến Cuối or Lời Gọi as layered effects with all five phases (charge, release at the caster, travel, impact, aftermath). Use for any shot, skill, ultimate, trap, enemy attack, death or boss effect, and for "pale" or "weak" feedback complaints.
---

# Layered VFX for the split games

The standard is [docs/games/VFX_STANDARD.md](../../../docs/games/VFX_STANDARD.md) (Vietnamese). Read §3 before building and §5.6 before claiming done. The owner's reference is `tmp/vfx/owner-reference-layered-vfx.webp` (ignored): nine simple layers composed into one effect.

1. **Trace the event.** Find the sim event that starts the action and its timing: wind-up, release and strike ticks, delay to impact. VFX lives in the view only. It never changes sim, content or goldens.
2. **Pick the action class** (§3.3: key, basic shot, rapid fire, skill, ultimate, trap, enemy attack, death, boss). Take its required layers per phase.
3. **Build the caster side first.**
   - A (charge) and R (release at the mouth, muzzle or tower) come before I (impact). This was the owner's complaint of 28/10.
   - Key-to-release stays ≤ 50 ms. A clip follows typing progress; it never holds the shot back.
4. **Layers and timing** in frames at 60 Hz (§3.4):
   - A flash is full bright on its first frame.
   - Layers are offset 2–3 frames.
   - Add a dark layer behind bright ones.
   - The core is at most 30 % white.
   - Enemy colours never use our fire ramp.
5. **Budgets** (§3.7): stay inside the game's measured frame headroom per tier. Rồng Giữ Ải High has about 2 ms left, bloom included. Measure before adding lights or bloom.
6. **Capture, measure, score** (§4.5, §5.6):
   - Frame sheets at 1280×720 and 1920×1080, play camera and close-up, light and dark backgrounds, beside the reference.
   - First frame ≥ 95 % of peak; white-out ≤ 6 %; word-tag contrast ≥ 7:1.
   - Score ≥ 8/10, with a second scorer for 7.5–8.5.
   - Give the owner a short clip.
7. Write the game's changelog. Keep reduced-motion versions.

Techniques beyond this repo (Claude reads these files directly; they are not loaded as skills here): `~/.agents/skills/threejs-aaa-graphics-builder/references/{technical-art,shader-cookbook,visual-scorecard}.md` and `~/.agents/skills/threejs-gameplay-systems/references/game-feel.md`.

Space Typing's [combat-vfx-audio](../combat-vfx-audio/SKILL.md) is reference only for the split games.
