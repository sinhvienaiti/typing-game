# Review of "Dragonhold dragon fire VFX solution V3 (free only)"

Claude, 31/10/2026. Read in full; the four free sources were checked on their pages. Nothing has been downloaded yet. The earlier review of V2 is `VFX_SOLUTION_V2_REVIEW.md`; this note only says what changes.

## Free-only decision

**MODIFY.** The asset half is good: it finally names a free, hand-painted source. The runtime half repeats V2's over-engineering for this game.

## Existing repo systems

Unchanged since the V2 review:
- three.js 0.170, no particle library;
- our own flipbook runtime and five-phase STRONG hit;
- a mouth socket from the rig;
- quality tiers, no depth texture, flat terrain;
- **no continuous breath attack**: the dragon shoots a fireball per typed word, plus the Sky Fire ultimate.

## three.quarks

**REJECT for now**, same reason as in the V2 review. The repo already has what it would add. The art is the bottleneck, not the runtime.

## AD_FX FREE 01 review

https://ad-fx.itch.io/free

- **Best candidate in V3.** CC0. It is the first free source described as **hand-painted** and stylized, which matches Dragonhold's painted world better than the code-generated SCORCH and Pyroclast samples we already looked at.
- No generative AI, per the page.
- Transparent PNG sequences, 1024 x 1024.
- Download `Free.zip`, 3.5 MB.
- Unknown: the page does not list the effects. At 3.5 MB it is likely only a few animations, so it may hold no strong-hit explosion at all. It must be opened before any plan depends on it.

## Kenney review

- Particle Pack (80 files, 512 px) and Smoke Particles (70 files). CC0, a well-established source.
- Good **supporting** layers: sparks, glows, and smoke puffs tinted warm grey, normal blend, not emissive.
- They will not carry the main flame.

## Free scorch review

- Taproot Free Surface Decals: name-your-price with $0 allowed; commercial use, no attribution; no generative AI.
- `free-surface-decals-raw.zip`, 1.8 MB.
- Its Scorch Mark is described as "soot burn with blistered paint", a wall-style decal. It may look wrong on painted grass. Test B's own warm-brown scorch with a cooling ember edge is already free and in the repo. Compare the two on the bench and keep the better one.

## Dragon breath implementation

**Not needed.** Dragonhold has no continuous breath, so drop the BreathRibbon, the BreathController and the flame chunks. The release plume at the mouth already exists.

## Prototype plan (one day, stop rule)

1. Owner's OK to download the four free files above (about 6–10 MB in all).
2. Open them and make contact sheets over grass, sand and dark ground. Keep only effects that fit.
3. Build one STRONG impact on the existing bench (`?bench=fire`):
   - AD_FX main explosion, at 2.5–3x the foe, with a punch frame larger than the shot;
   - our procedural ground shockwave;
   - Kenney sparks and smoke;
   - the better of the two scorches.
4. Two fresh blind judges score it against round 10 (6.0 / 6.5), without the builder's report in their brief.
5. If both judges do not give 8 within a day, stop and keep round 10. Blender (installed, free) stays as the later path for our own stylized fire. It is option C of the diagnosis and costs real work.

## Performance risk

Low. A few 1024 px sheets and small Kenney sprites are well inside the High 1080 budget (round 10 runs at about 3.5 ms).

## Art quality risk

- Medium to high. One hand-painted free pack is a narrow base:
  - its style and colours may still clash with our palette;
  - every hit will look the same if it holds only one explosion;
  - its scale and timing were made for another game.
- Kenney's sprites are generic.

## Any free source better than these

None found yet. For the painted look, AD_FX is the only free hand-painted candidate named so far.

## Any paid dependency accidentally remaining

None. Blender is free, and EmberGen is correctly dropped.
