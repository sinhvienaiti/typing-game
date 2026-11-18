# Recipes to research

Status, 01/11/2026: no recipe is verified yet. This file lists where to look, how to record what is found, and (§4) the verified recipes themselves. A recipe verified in any game is written here, in reusable form, so the next game finds it; the game's changelog keeps its captures and numbers.

## 1. How to record a recipe

For each recipe, write down:
- the layer (P1–P10 in [the layer menu](layers.md));
- the source link;
- the licence, quoted from the source page or its LICENSE file;
- the technique, in our own words;
- port notes for the game's renderer: three version, and WebGL2 GLSL (`ShaderMaterial`, `onBeforeCompile`) or WebGPU with TSL;
- the cost measured in the lab;
- a verdict after opening the source (correct, partly correct, unsupported);
- a capture that shows it.

## 2. Licences

- The allowed and banned lists, and how to verify a licence on its page, are in [game-art-pipeline's licences](../../game-art-pipeline/references/licences.md) (rule text: `docs/games/SHARED_SYSTEMS_BAR.md` §5). Do not keep a second copy here.
- For effects in particular:
  - shader code on Shadertoy is CC BY-NC-SA 3.0 unless its header says otherwise: study only;
  - sample content bound to another engine (Unity, Unreal) is study only;
  - a study-only source teaches the idea; we write our own code from it and cite the link.
- Record every library or asset used in `docs/games/THIRD_PARTY.md`.

## 3. Where to look

| Source | Licence (check at source) | What to learn | How we may use it |
|---|---|---|---|
| three.js examples and addons | MIT | Selective bloom (`webgl_postprocessing_unreal_bloom_selective`), material patches (`webgl_materials_modified`), instancing (`webgl_buffergeometry_instancing`), point sprites, pixel-width lines for thin rings (`webgl_lines_fat`), the outline pass | Adapt code, keeping the notice |
| three.quarks | MIT | The emitter and behaviour model (trails, mesh particles, soft particles, sub-emitters) and its JSON presets | Study for now. VFX_STANDARD §4.3 decided not to use it: versions are tied to three (the last for three 0.170 was 0.16.0), its editor exports JSON only when paid, and its CPU simulation is no better than ours. Revisit on three 0.182 or later |
| three-nebula | MIT | CPU emitters and behaviours | Study |
| pmndrs postprocessing | Zlib | Selective bloom, mipmap-blur bloom, merged effect passes | Candidate when the game's bloom costs too much; measure first |
| drei | MIT | `Sparkles` (instanced motes), `Trail`, `Billboard`, `Outlines`, `Float` | Bound to React; port the shader idea to plain three |
| TSL (three.js) | MIT | Node recipes for fresnel, glow and noise | Needs the WebGPU renderer; reference only until a game moves to it |
| Shadertoy | CC BY-NC-SA 3.0 by default, unless the author states otherwise | Signed-distance rings, glow falloffs, noise, sparkle | Study only, unless the shader's header grants a permissive licence |
| The Book of Shaders | Check the licence of the text and of the code | Shapes (rings), noise, patterns, easing | Study; reimplement |
| Inigo Quilez's articles | Check per article and snippet | Distance functions, smooth falloffs, colour palettes | Study; reimplement |
| Unity VFX Graph samples | Bound to Unity | How auras, halos and trails are split into layers; timing; emitter structure | Study only |
| Unreal Niagara content examples | Bound to Unreal Engine | The same | Study only |
| Studio talks and breakdowns | Not applicable | GDC Vault VFX talks, Real-Time VFX community breakdowns, studio art blogs on hero readability | Ideas and rules of thumb, cited with a link |
| Commercial games (look only) | Not applicable | How heroes, companions and bosses carry radiance at the play camera | The judges' reference board |

## 4. Questions the research should answer

- For each layer: geometry, texture, shader or particles, and why. This feeds the geometry-or-VFX decision.
- How commercial games keep a radiant character readable at small sizes: rim, halo or ground glow.
- The cost of selective bloom against falloffs baked into shaders, on WebGL2, at our tiers.
- Idle timing: breathing periods and twinkle duty cycles that read as alive without flicker.
- Thin rings that do not shimmer at 1–3 px.
- Presence that scales with progress (streak, charge) in a way players can read.
- Reduced-motion practice in commercial games for effects that are always on.

## 4. Verified recipes

A recipe enters this table once it has a source verdict, a measured lab cost and a capture. Write the technique so another game can use it; keep game-specific numbers in that game's docs and link them. The last column says where the recipe is part of a presence two blind judges accepted at 8.5, or "lab only".

| Layer | Recipe, in our words | Source and licence | Renderer and port notes | Cost (game, tier, dpr) | Evidence (changelog, sheet) | Accepted in |
|---|---|---|---|---|---|---|

No row yet (01/11/2026).
