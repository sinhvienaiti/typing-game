---
name: game-map-concept
description: Design a battle map, stage, arena or play scene from the game's real play camera before building or reworking it - measure the frame, make a base image and legend, write the concept, get it reviewed and painted over the base, judge it blind, then turn it into build steps. Use for any game in this repo or a later one (lane or tower defence, arena, survival, top-down or three-quarter view, 3D or 2D) when a map or stage, or its ground, water, light or dressing, looks plain, empty, flat or toy-like; before building, rebuilding or relighting a map; and when writing a map concept, a base image and legend, a ChatGPT review or painting brief for a map, or judging a map painting or a built map. Not for title, results or key art alone (game-art-pipeline), characters (game-character-design) or single combat effects (game-vfx-layered).
---

# Map concepts from the real camera

Owner, 01/11/2026, on the maps of all three games then in work: "việc thiết kế map của bạn đang có vấn đề rất lớn ... không chấp nhận nổi". We built maps before we had an idea of them, so they came out as toy parks: one-colour lawns, canal water, repeated trees, no landmark. We also painted the epic where the camera never looks. The fix is one accepted picture of "done" per stage, drawn for the camera the player uses, and then a build matched to it.

This method is for every game. Dragonhold, Wordwoven, Last Line and Tu Tiên appear only as examples; each game's own design docs, its sim and the owner's decisions win over this skill. Concepts change only what the player sees: lanes, slots, spawns, collisions and golden hashes stay.

1. **Read the live rules and the game.** Read `AGENTS.md` (bar 8.5 from two blind judges, appeal, market references, no code-drawn stand-ins, English text). Then read the game's design source and its accepted key art and stage cards, because the fight must show the world the menus promise. Take the camera from source code, not from a doc: every view and tilt or zoom the player can reach, as the play build ships it.
2. **Measure the frame before drawing anything.** Mirror the camera in [`frame-budget.mjs`](scripts/frame-budget.mjs). Check it against the engine's own projection: ≤ 2 px, at four or more points that span the frame. From it, write down:
   - whether any sky shows;
   - the height budget per screen row;
   - what would stand in front of play or lean into the HUD;
   - the ground each HUD box hides;
   - px per metre and the ground texel need.

   The epic has to live inside that frame. Anything the frame cannot show goes to the title, results or intro camera. For a 2D or fixed-screen game the frame is the canvas: skip the projection and read the rows, HUD boxes and play zone straight from the play build. See [camera-and-base](references/camera-and-base.md).
3. **Make the base image and legend.** Capture the battle camera on the play build, canvas only. Draw a translucent block for every planned piece at its projected place and height. Grey out the HUD. Write a legend with world and screen coordinates. See [camera-and-base](references/camera-and-base.md).
4. **Write the concept per stage**, in English, layout and camera fixed. Cover:
   - one story beat and one hero landmark;
   - the read order;
   - what carries the scale within the height budget;
   - depth bands, a light budget and a value table;
   - reserved signal colours and material families;
   - life before polish, and dressing only for what the frame shows;
   - sources, and what is wrong today.

   See [composition](references/composition.md) and the doc skeleton in [concept-doc](references/concept-doc.md).
5. **Review and paint with ChatGPT.** Use Chat mode at High, never Work, in your own tab ([game-art-pipeline browser tools](../game-art-pipeline/references/browser-ai-tools.md) has the tab, sign-in and file rules). Fall back to Gemini, or to Firefly Image 5 with the base as the composition reference.
   - The owner attaches the base image. Without it the painting drifts: layout scored 5.5–7.5 without a base and 8.3–8.5 with one.
   - Fold the review into the concept. Use ChatGPT's own prompt.
   - Retry with the judges' numbers and exact pixel boxes. Keep a sidecar file for every message.

   See [chatgpt-review](references/chatgpt-review.md).
6. **Judge the painting blind.** Two independent judges score market level, appeal, layout fidelity and readability, each 8.5 or more, then apply the reject list. Never pass a painting on "best of three" or "better than before". See [judging](references/judging.md).
7. **Turn the accepted painting into build steps.**
   - Make a kit table ordered by share of the battle frame.
   - Build in this order: life first, then ground, water and light, then landmarks, then dressing.
   - Use real PBR materials, free commercial-safe sources with licences recorded, reused monsters, and VFX to the standard.
   - Respect the budgets per quality tier.

   See [build-from-concept](references/build-from-concept.md).
8. **Judge the build in the play host.** Use the player's default settings with no URL flags, plus High and Ultra, at 1280×720 and 1920×1080. Put each shot beside the accepted painting and the reference board. Both judges must give 8.5 or more. See [judging](references/judging.md).

Before you send a concept, a prompt or a build for judging, run through [failures](references/failures.md). It lists what went wrong the hard way: empty fields, repeated tiles, flat water, finger-smear roads, foes sinking into the ground, too many focal points and gold glowing everywhere. [worked-examples](references/worked-examples.md) has the camera numbers, decisions and scores of four games with different cameras and genres.

Living sources of numbers (read them, do not copy them here):
- [VFX_STANDARD](../../../docs/games/VFX_STANDARD.md) for fire, water, ink, rifts, falls and bloom;
- [MODEL_QUALITY](../../../docs/games/MODEL_QUALITY.md) for triangle and texture floors;
- [PATH_QUALITY](../../../docs/games/PATH_QUALITY.md) for roads and lanes;
- [ART_DIRECTION §1.3](../../../docs/games/ART_DIRECTION_2026-10-28.md) for the market-level scale;
- [ART_ACCEPTANCE](../../../docs/games/ART_ACCEPTANCE.md) for the bar and appeal;
- [SHARED_SYSTEMS_BAR §5](../../../docs/games/SHARED_SYSTEMS_BAR.md), [FREE_ASSET_SOURCES](../../../docs/games/FREE_ASSET_SOURCES.md) and [THIRD_PARTY](../../../docs/games/THIRD_PARTY.md) for licences;
- [MONSTER_MODEL_INVENTORY](../../../docs/games/MONSTER_MODEL_INVENTORY.md) for monster reuse.

Related skills: [game-art-pipeline](../game-art-pipeline/SKILL.md) for tools, blind-round setup, licences and Tripo; [game-vfx-layered](../game-vfx-layered/SKILL.md) for every effect on the map; [game-character-design](../game-character-design/SKILL.md) for a hero creature or boss the map needs; and the installed `threejs-*` skills for rendering techniques. Captures, the base image included, go under the game's `tmp/` and raw frames are pruned after use (`AGENTS.md`). Base images and paintings are media and never go into Git.
