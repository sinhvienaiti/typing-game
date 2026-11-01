# Worked examples

These examples only show how the procedure meets a real game. Check the current source before reusing any number; where an example and the source disagree, the source wins.

## Lessons that apply to every game

- **No light painted into the source art.** The third try at the Last Line heroine painted a light ring into the character image, and the owner found it odd (LESSONS §11). He asked for the right method, found with evidence, not an assumed one. So the geometry-or-VFX split of the radiance kit stays open until the research decides it ([pipeline decision](../../game-character-design/references/pipeline-decision.md)). What holds meanwhile: no painted glow, rays or rim light in a 3D source image, and one brief line per kit part with its socket.
- **Bloom is not a style.** The old Last Line bloom (strength 0.85, radius 0.3, threshold 1.0) with ACES widened shots 2.5–3.5× and whitened them at High and Ultra, so Ultra looked worse than Medium (`docs/games/QUALITY_RESCUE_2026-11-01.md` §2.3). Lowering the shared bloom to fix it also erased the typing marks (LESSONS §5). A presence layer adapts to the bloom rule; it never moves the global bloom.
- **Judge at the size the player sees.** Icons accepted on 256 px sheets scored 6.2 in game at 16–24 px. The Last Line heroine is 68–100 px tall in play; a Tu Tien cultivator has a floor of 64 px at 1080p. Presence is judged there, not on a close-up.
- **A URL flag is not the player's setting.** A layer that reads only with a flag (`?bloom=1`, `?debug=1`) has not been seen by the player. Judge with no flags.

## Last Line (`games/typing-survival`): Lightbearer and drone

- **What the camera sees.** Pitch 36°, FOV 42. A 2.6 m heroine is about 68 px tall at 720p and 100 px at 1080p, seen from behind and from 46° above (QUALITY_RESCUE §4.1). Her cyan visor faces the enemies, so the player never sees it. Presence lives on the back core (`FX_BACK_CORE`), the cape lines, a ring and the drone, not on the face.
- **Colours.** Gold is reserved for the Pack Leader (colour fix of 01/11, QUALITY_RESCUE §4.4). The heroine, drone and guns are ivory ceramic and graphite with thin cyan light; the cape is navy with very thin ivory lines; the drone carries one narrow cyan slit. A gold halo on her would read as an elite enemy.
- **Presence follows typing** (QUALITY_RESCUE §4.6):
  - the ring, cape and back core brighten with the typing chain;
  - on victory the drone circles her; on defeat it falls and its lights go out beside her as she kneels;
  - planned sockets (QUALITY_RESCUE §4.3): hero `FX_HAND_R/L`, `FX_CORE`, `FX_BACK_CORE`, `FX_VISOR`; drone `FX_EYE`, `FX_RING`, `FX_THRUST`. Check the GLB before relying on them.
- **Shared typing feedback.** Today finished words fly their letters into the ship's core (`games/typing-survival/src/view/type-fx.ts`). The hero plan routes them into the `FX_CORE` of the gun whose bay is being typed (QUALITY_RESCUE §4.7). Find the landing point in the current source, keep presence there dimmer than the arrival, and re-run the typing captures.
- **Bloom.** The owner approved the fix (O4). Check `games/typing-survival/src/view/scene.ts` before tuning: on 01/11 it still showed ACES and 0.85 / 0.3, so the fix had not landed. Tune presence against the fixed values on a branch, not against the old pass.
- **Plumbing.** New presence shaders compile at load in `games/typing-survival/src/view/warm.ts`. The motion switch is `motionReduced()` in `games/typing-survival/src/app/motion.ts`.

## Dragonhold (`games/dragon-hold`): Draconis

- **Sockets.** `FX_MOUTH`, `FX_CAST_L/R`, `FX_WING_L/L2/R/R2`, `FX_TAIL`, `FX_FOOT_L/R`, `FX_CORE`, `FX_HALO` (`docs/games/MONSTER_MODEL_INVENTORY.md`). The halo and core layers already have anchors.
- **No bloom at the player's settings.** The owner decided on 29/10: no bloom on High and below. Ultra builds a bloom pass (0.32 / 0.5 / threshold 1.6), but it is off at start and only `?bloom=1` turns it on, so a judged build has no bloom on any tier. The grade pass tone maps with Neutral; MSAA 4× is on Ultra only, and High uses FXAA at dpr 1.25 (`STAGE_QUALITY` in `games/dragon-hold/src/view/stage.ts`). Presence must read with no bloom: falloffs in the shaders, HDR cores over a dark backing.
- **Little headroom.** About 2 ms at High when the machine is idle and about 0 when busy; bloom alone cost 2.2 ms on the bare field (VFX_STANDARD §3.7). Each light costs on lit ground and on 220 skinned enemies.
- **Rim.** The crowd rim's NaN black box (29/10) came from `pow()` of a negative base under MSAA; `games/dragon-hold/src/view/crowd.ts` now clamps the rim. A presence rim clamps the same way.
- **Colours.** Ours are fire orange-gold, with teal for Flash and Perfect. Enemies are moss, purple and crimson, never our fire ramp.
- **Bar.** Fire on the dragon aims for 9 and accepts 8.5 from both judges.
- **Reuse.** The VFX lane's dragon already carries wing-tip fire ribbons (`docs/games/CHARACTER_ANIMATION.md` §2.2); presence ribbons reuse them.
- **Plumbing.** The lab extends `runFxShowcase` in `games/dragon-hold/src/view/bench.ts`. The motion option is `reducedMotion` in `games/dragon-hold/src/view/camera.ts`.

## Tu Tien Thủ Ải (`games/immortality-cultivation`)

- **Split, as the requests stand today.** The M0b source requests (`docs/games/tu-tien/art-requests/m0b/`, for example `03-elites.md`) leave out aura, emissive light, particles and trails; auras, seals (Ấn) and healing are runtime effects. Recheck this against the radiance-kit decision once it exists.
- **Camera and size.** Pitch 55°, vertical FOV 28° (`docs/games/tu-tien/ART_AUDIO_VFX_PLAN.md` §2), so the camera looks down steeply and never sees the sky. A ring behind the head is seen from high above; compare it with a shoulder or ground ring in the lab. The player has a floor of 64 px at 1080p (canon §21.1).
- **Look.** Neutral tone map and the bloom rule (`ART_AUDIO_VFX_PLAN.md` §6). Our side is ivory, indigo and pale gold trim, with ivory spirit light: noble and restrained. Typed words become jade calligraphy strokes that fly into the hand in 0.15 s, so the hand is a typing-feedback landing point.
- **Reserved colours** (canon §21.1): red `#FF4A4A` for enemy danger, orange `#FFB020` for urgency, gold `#FFC83A` for money and drops, turquoise `#7FF5E0` for typing power. Presence stays off all four at high intensity; a bright gold halo would read as loot.
- **Signal auras, not presence.** Elites are drawn at ×1.25 with an aura ring; the beast general (Lang Đầu Đàn) at ×1.4 with an aura tint and its 6 m aura ring, which speeds nearby wolves (canon §10.3–10.4, `src/view/actors.ts`). These carry rules: they stay in reduced motion, and our presence must differ from them in shape as well as colour. Realm quality adds a halo colour on our side (`docs/games/tu-tien/analysis/01-tu-luyen-canh-gioi.md`).
- **Lab.** `lookdev.html` (the material standard in the game's renderer) and `bench.html` in the game.
- **Bar.** The owner wants every category at 8.5 or more in the demo before rollout.

## Wordwoven (`games/typing-defense`)

- **Main is 2D Canvas.** No bloom. Additive light uses `globalCompositeOperation = "lighter"` (VFX_STANDARD §3.5). Presence is pre-rendered sprite layers drawn in that mode. The per-layer switches, the lab, the protected masks and the judging all apply the same way.
- **A 3D view is on unmerged branches** (for example `td-3d-default`, on 01/11): three.js on Medium and High, Low stays 2D, a grade pass with Neutral tone, and a bloom pass that is built but off until measured. Check which view the play host builds; the 3D one brings in the three.js rules.
- **Motion.** On those branches the Settings motion row sets `td-still` on the page root (`src/app/quick.ts`), and the 3D words also read the system query. Use the game's setting, not the media query alone (VFX_STANDARD §3.8).
