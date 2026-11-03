# Tool choice: which tool makes each effect most beautiful

Start from this table, then confirm with the VFX production pipeline research in docs/games (VFX_PRODUCTION_PIPELINE, written 04/11/2026). When the research or a judged test shows a better tool for an effect, update this table.

| Effect | First choice | Second choice | Code does |
|---|---|---|---|
| Fire burst or impact flame | Blender Mantaflow fire, rendered to a flipbook with a stylized colour ramp (crisp tongues, dark rim) | Firefly Video, transparent background | Spawn, scale, orient to the blow, erode, linger |
| Flame band around a blade, flame trail | Firefly Video or Blender, a seamless band that tiles along x; the Dragonhold flame-trail flipbook is the proven reference | Blender wind-blown fire on a strip | Map along the blade, scroll, clip at the edge, cool toward the tail |
| Qi, wind-silk, energy aura around an object | Firefly Video loop of flowing silk or qi (transparent background) | Blender smoke sim with an emission ramp, or Geometry Nodes ribbons rendered | Wrap the band round the object's profile, ink gap, fade by state |
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
- A photoreal sim is raw material, never the target. Push it to anime and myth with stepped ramps, a bold silhouette and a thin bright core.
- Never use the tool you know best by default. Use the one that makes the most beautiful result for this effect, and when unsure, test two.
