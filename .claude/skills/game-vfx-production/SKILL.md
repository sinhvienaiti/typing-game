---
name: game-vfx-production
description: "Make the LOOK of any VFX, CGI or SFX truly beautiful in any game of this repo (Tu Tien, Dragonhold, Last Line, Wordwoven, Space Typing and later games): fire, flames around a blade, auras and sheaths, sparks and embers, glints and stars, rings and seals, ground cracks and scorch, smoke, qi, water, lightning, dragons and other creatures made of an element, cut-in art, skill sounds. Use FIRST, before writing any shader or effect code, whenever an effect has to be created, redone or judged, and whenever the owner calls one ugly, crude, plain, static, not smooth, not sparkling or code-drawn. Decides the tool (Firefly Video or Image, Blender, CC0 packs, code), runs research, candidates, owner review and blind judging, and gives the recipes and the quality rubric. game-vfx-layered then owns phases and timing, game-hero-presence-vfx the always-on layers, game-art-pipeline the tools' browser recipes and licences."
---

# VFX, CGI and SFX production: art first, code animates

**Why this skill exists.** The owner had to repeat it night after night:
- On 03/11/2026: "việc bạn tự style ra những cái đó nó chưa được đẹp lắm" (code-drawn cracks), and "hào quang… thô… không có chút chuyển động, mượt mà, lấp lánh" (a shader-drawn sword aura).
- On 03/11/2026 too: "sao 4 cánh… thực sự không đẹp" (an analytic tip star).
- On 04/11/2026: "luôn ưu tiên dùng blender hoặc fire[fly] nếu 2 thứ này làm tốt hơn bạn… cách bạn đang làm… chưa đạt đến 6 điểm… ngọn lửa bạn làm ra, nhìn như rác".

What he liked came from real art: a Firefly Video flame flipbook ("rực cháy khá mềm mượt và nhìn khá chân thật"), and ChatGPT and Firefly paintings. What he rejected was drawn by code.

**The rule.** The goal is beauty at 8.5, not a favourite tool.
- The owner asked for Firefly and Blender because effects made in code kept failing his bar: "ưu tiên… nếu 2 thứ này làm tốt hơn bạn".
- So the look of an effect (its shape, texture, motion and sparkle) comes from whichever tool makes it most beautiful. Today that is Firefly, Blender or painted art. Code places, sizes, times, colours, erodes and blends that art.
- Code may make the look only if a blind A/B against Firefly or Blender versions shows code wins.

## Procedure (every effect, every time)

1. **Pick the tool from the table** in [tool-choice](references/tool-choice.md) before any code.
   - Write the choice and the reason in the brief.
   - If code is chosen for anything beyond noise, erosion, thin rings, placement or timing, stop and justify it in writing.
2. **Research loved designs first, with both assistants** (AGENTS.md "Plan with ChatGPT and Gemini").
   - Run the double review of [agent-orchestration](../agent-orchestration/SKILL.md): ChatGPT analyses and passes its own review twice in a row, then Gemini reviews and passes twice in a row, then Claude decides.
   - Verify their claims at the source, write down where they disagree, and merge everything into one plan before any making.
   - Build a numbered reference board of 9–12 frames from official footage, for the owner's eyes only.
   - Name what makes the loved ones beautiful: shape, motion, layers, light, sparkle.
3. **Make 3–5 candidates at once,** in the chosen tools and in the same set standard. For example: several Firefly Video takes, Blender sims with different shapes, two colour ramps.
   - Never improve one candidate in a loop.
   - Three tries without a gain: stop, and discuss a better method with ChatGPT and Gemini.
4. **Process into game-ready art,** following [recipes](references/recipes.md):
   - flipbook atlases with enough frames for smooth motion, clean straight alpha, crisp edges and a dark backing;
   - seamless loops where the effect loops;
   - channel-packed masks for marks.
5. **Self-check against the rubric** in [quality-rubric](references/quality-rubric.md), at the size the player sees (play camera and close), on light and dark ground, in motion.
   - If it would not stand next to official Genshin, Star Rail, Wuthering Waves or Naraka footage, do not show it as a result. Show it as a sample with its gaps named.
6. **Owner review.** Send the samples (sheets and short videos, or a local link to a fixed snapshot when he is at the Mac). His pick is final before anything is wired.
7. **Wire with code** through the game's pools: flipbooks, ribbons, decals, sprites.
   - Then [game-vfx-layered](../game-vfx-layered/SKILL.md) for phases and timing, and [game-hero-presence-vfx](../game-hero-presence-vfx/SKILL.md) for always-on layers.
8. **Two blind judges ≥ 8.5** in the built play host. At 7 or more, send the owner a demo video, then keep going.

## Hard rules

- **No code-drawn look without a won A/B.** Flame bodies, auras, stars and glints, cracks, scorch and seams drawn in code scored under 6 every time (03-04/11/2026). Ship one only after two blind judges prefer it over Firefly or Blender versions. Allowed in code: noise and erosion masks, analytic thin rings and lines, placement, motion curves, colour grading, alpha thresholds, blending.
- **Tools.**
  - **Firefly:** Adobe models only (Firefly Video, Firefly Image, the Upscaler, sound effects); never partner models; never sign in or click consent for the owner.
  - **Blender:** `/Applications/Blender.app`, run headless. It is not local AI. Heavy sims and renders go through `.local/bin/heavy.sh --cores=N`.
  - **No local AI models** (no Stable Diffusion, FLUX or ComfyUI).
- **Motion must be smooth.**
  - Enough frames (≥ 24 for a burst, a seamless loop for a band).
  - Frame blending or hold-and-erode, never a visible step.
  - Fast attack, slow decay. No pops.
- **Sparkle is part of the look.** Every effect carries glints, twinkles and fine motes from real art, not from analytic stars ([game-vfx-layered](../game-vfx-layered/SKILL.md) step 3).
- **Light.** Only thin HDR cores bloom, bodies stay ≤ 0.9, and a dark backing sits behind bright layers. Every game's reserved signal colours stay clear.
- **Media.** Never in Git. Art goes to the game's `art-src/` with a manifest entry and the exact prompt or script beside it. Captures go to `tmp/`.

## References

- **Companion skills** (owner-provided, 04/11/2026):
  - [game-vfx](../game-vfx/SKILL.md): readability, hierarchy, performance, licence and the VFX scorecard and gates;
  - [game-cgi](../game-cgi/SKILL.md): cut-ins, cinematics, shot and character beauty, continuity;
  - [game-sfx](../game-sfx/SKILL.md): sound design, Web Audio runtime, combat mix.

- [tool-choice](references/tool-choice.md): which tool makes which effect most beautiful, and why.
- [recipes](references/recipes.md): Firefly Video → flipbook, Blender fire and smoke → flipbook, glint sheets, painted marks, smooth motion, sound.
- [quality-rubric](references/quality-rubric.md): what separates 6/10 from 8.5/10, checked on frames and in motion.
- The research behind this skill: the VFX production pipeline research in docs/games (VFX_PRODUCTION_PIPELINE, written 04/11/2026) (ChatGPT and Gemini, checked).
- Existing tools and know-how:
  - `tools/vfx-flipbook` (atlas, contact sheet, metrics from a clip);
  - `.local/ff-bridge` (the receiver for browser downloads);
  - [game-art-pipeline browser tools](../game-art-pipeline/references/browser-ai-tools.md) §5 (Firefly recipes);
  - [flipbooks](../game-vfx-layered/references/flipbooks.md) (sources, atlas, budget).
