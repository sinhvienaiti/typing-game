# Tool choice: which tool makes each effect most beautiful

Start from this table, then confirm with the VFX production pipeline research in docs/games (VFX_PRODUCTION_PIPELINE, written 04/11/2026). When the research or a judged test shows a better tool for an effect, update this table.

| Effect | First choice | Second choice | Code does |
|---|---|---|---|
| Fire burst or impact flame | A painted shape (first and last frame, opaque black 1:1 1080p) moved by Firefly Video image-to-video; the clip is the final asset when it passes | Firefly Video alone when its shape is right; the painted shape plus the inner motion of a liked clip | Spawn, scale, orient to the blow, reveal in stroke order, ink/body/core, erode, linger |
| Flame band around a blade, flame trail | A painted sheath mask for the silhouette plus an x-seamless scrolling strip cut from a Firefly Video flame clip (recipes §2); the Dragonhold flame-trail flipbook is the proven reference | Blender wind-blown fire on a strip | Map along the blade, scroll backward, clip at the edge, cool toward the tail |
| Qi, wind-silk, energy aura around an object | A painted mantle mask plus an x-seamless strip of flowing silk streaks from Firefly Video (recipes §2) | Firefly Video loop of flowing silk or qi; Geometry Nodes ribbons rendered | Wrap the band round the object's profile, ink gap, fade by state |
| Sparks, embers | Firefly Video spark burst on black, or Blender particles rendered with motion blur (streaks) | CC0 spark sheets (Kenney) as a test only | Emit in clumps along the blow, gravity, lifetime |
| Glints, star twinkles, glitter | Firefly Video glint sheet on black; a painted 4- or 6-point star with a soft halo | CC0 star sprites as a test only | Place on tips, seams and crossings; flash timing; screen-size clamp |
| Thin rings, seals, sigils | A painted seal (ChatGPT or Firefly Image) for a sigil; analytic thin rings in code are fine | Firefly Video ring burst on black | Expand, rotate, run a light along the ring |
| Ground cracks, scorch, cut seams, rifts | Painted masks: ChatGPT or Firefly Image, 4–8 variants, channel-packed (shape, growth gradient, hot lines, alpha) | Blender displacement or crack generator, rendered top-down | Reveal from the impact, glow, cool, erode; random rotation |
| Smoke, dust, steam | Blender smoke sim → flipbook (dark, readable) | Firefly Video on black | Spawn, drift, fade by erosion |
| Water, splashes, flow | Blender fluid or Firefly Video | Painted flow maps | Flow-map scrolling, foam masks |
| Lightning, thunder | Firefly Video bolts on black; painted bolt sheets | Blender Geometry Nodes branches rendered | Branch placement, flicker timing |
| A creature made of an element (fire dragon, qi dragon) | Firefly Video for the motion study and the flipbook; Blender sim along a spline (smoke or fire following the body) | A Tripo or rigged model with an element shader, only if the owner approves | Path, timing, glints, aftermath |
| Cut-in art, key art | ChatGPT or Gemini painting, Firefly Upscaler | Firefly Image | Framing, punch, shake, flash |
| Skill sound | Firefly sound effects (Adobe model), layered | Licence-checked CC0 libraries | Mixing, loudness tiers, reverb send, timing to the frame |

Notes:
- **Each effect has three sources** (INTEGRATION_PLAN_2026-11-04, 04/11/2026):
  - a painting decides the shape;
  - Firefly Video gives the motion inside it;
  - the shader and code give colour, the dark backing, the hot core, timing and erosion.

  Code never draws the main shape. Blender's stepped-ramp painting of brush-fire impacts was stopped after blind judges scored it 3.5–4.5; keep Blender for data and for shapes a simulation really makes (recipes §3).
- **A Firefly clip is the final asset when it passes** at play size (recipes §1 step 1). Otherwise it is a source of motion, never a reason to keep a weak shape.
- **No video upscaling.** Firefly's video upscaler (Topaz) is a partner model. Images go through the Firefly Upscaler, Adobe's own model (recipes §1 step 9).
- A photoreal sim is raw material, never the target. Push it to anime and myth with stepped ramps, a bold silhouette and a thin bright core.
- Never use the tool you know best by default. Use the one that makes the most beautiful result for this effect, and when unsure, test two.
