# Review of "Dragonhold dragon fire VFX solution V2"

Claude, 31/10/2026, after reading the whole document and checking the Dragonhold repo and the three suggested packs.

## Decision

**ACCEPT WITH CHANGES.** The core idea is right and matches what our tests showed: the weak point is the authored art, so use licensed, authored flipbooks assembled as layers, and keep gameplay independent of the packs. Most of the proposed runtime already exists in Dragonhold. The three.quarks spike, the breath ribbon and soft particles are not needed for the problem we have now.

## Existing repo systems (answers to the checklist that matter)

- three.js **0.170.0**. No particle library installed.
- A custom **flipbook runtime** already exists (`src/view/flipbook.ts`, about 950 lines on the VFX branch): atlases with JSON (cols, rows, fps, loop, blend, pivot), normal and additive blend, a coverage-alpha fire material, smoke and decal modes. A flipbook tool turns Firefly clips or alpha video into atlases (`tools/vfx-flipbook`).
- The STRONG word hit is already a **composite in five phases** (charge, release, travel, impact, aftermath) in `src/view/fx.ts`: halos, ribbon trail, smoke, scorch decals, embers, hit-stop and damage numbers.
- **Mouth socket** from the dragon rig (`fire.sockets.mouth` in `heroes.ts`).
- **Quality tiers** (Low, Medium, High, Ultra) in `stage.ts`. Bloom only on Ultra, through `EffectComposer` + `UnrealBloomPass`. **No depth texture** is produced today.
- **Camera shake**: trauma-based, from the shared kit's feedback module. **Impact light**: one pooled `PointLight` plus a mouth light per tier.
- **Terrain**: a flat lane map with painted ground; flat decal quads are enough.
- **Gameplay**: the dragon attack is a typed word: a fireball shot from the mouth, then an impact. Sky Fire is the ultimate. **There is no continuous breath attack.**
- Measurement and judging are already in place: a three-ground test bench (`?bench=fire`), measured gates (olive, brown, value ladder, core hue, peach, smoke cover, perf), and two fresh blind judges against commercial anchors.

## three.quarks decision

**REJECT for now.** Dragonhold already has the flipbook runtime and composite this layer would provide. A second particle system means more bundle size and code without fixing what failed (the art). Reconsider only if embers, trails or soft particles become the bottleneck, after a one-day spike. three.quarks is MIT and should work with three 0.170, but I could not reach npm from here to confirm the peer range.

## Architecture modifications

- Keep the existing flipbook runtime and the five-phase STRONG hit. Add only what is missing:
  - a **semantic layer table** (TypeScript, the repo's convention) mapping `dragon_fire_impact_strong` and similar to atlas layers with delay, scale, orientation, blend and tier;
  - a **PNG sprite-sheet ingest** path for packs (our tool takes video today), reading each pack's own metadata (`effects.json`, per-animation JSON).
- **Drop the BreathRibbon** until the game has a continuous breath attack. The release phase (mouth plume) already exists.
- **Defer soft particles.** No depth pass exists, and hard intersections were not among the judges' defects.

## Minimal implementation plan

1. Owner's OK to download the **free demos** of SCORCH and Pyroclast (no purchase yet).
2. Ingest the demo sheets and build one STRONG impact on the existing bench:
   - Pyroclast Fireball Burst (512 px) as the main body;
   - Pyroclast Shockwave Ring on the ground;
   - Ember Puff;
   - a SCORCH scorch decal;
   - pack smoke.
   - Peak size **2.5–3× the foe** with a punch frame bigger than the shot head. Test B failed at 1.8×.
3. Capture on the three grounds at 720p and 1080p. Run the existing gates. Two fresh blind judges score it against round 10 (current best, 6.0/6.5) **without the builder's report in their brief** (it leaked the key in test B).
4. Stop rule: if the pack hit does not reach **8 from both judges** within a day, stop. Otherwise the owner buys the full packs (about $10 at today's prices) and we roll it out to the PLAIN hit and Sky Fire.

## Files to modify / add (Dragonhold, after the merge of round 10 into main)

- Modify:
  - `src/view/fx.ts` (STRONG impact layers read from the table);
  - `src/view/flipbook.ts` (sprite-sheet atlases with pack metadata, straight and premultiplied alpha);
  - `scripts/visual/scenarios/dh-fire-bench.mjs` (pack variant).
- Add:
  - `src/view/vfx-layers.ts` (semantic layer table);
  - `scripts/assets/prepare-pack-vfx.mjs` (pack sheets to runtime atlases, kept out of Git);
  - `docs/games/THIRD_PARTY.md` rows (product, author, URL, date, licence).

## Asset recommendation

- **Pyroclast** (seamproof, $7.49 on sale, free demo):
  - **First pick for the STRONG hit.** It has 512 px cells, straight alpha, white-hot core, smoke and dust layers, and a ground shockwave.
  - Only 8 effects (one colour today).
  - Licence: commercial use, attribution optional, no resale of the files.
- **SCORCH** (godboyhappy, $2.49 on sale, free 8-effect sampler):
  - **Second pick, for breadth**: 48 effects, including scorch and burn-away, embers, jets and ground fire.
  - Only 256 px cells. Straight-alpha and premultiplied sheets plus `effects.json`.
  - Licence: commercial use, no credit, no resale of the files.
- **Fire & Explosions Vol. 1** (Taproot, $2.99): **not recommended.** Its alpha comes from brightness and it is drawn on black for additive blending. That is exactly what turned our fire olive and mustard over green grass in rounds 1–10.
- **Style risk:** all three packs are procedurally generated by code (each says "no generative AI"), not hand-painted. Dragonhold's world is painted. Only the bench and the blind judges can tell whether they match; preview videos cannot.

## Performance risks

- 512 px cells mean 2048–4096 px atlases. Pyroclast's 4096 sheets are too heavy: use its 2048 sheets or 256 px sequences on Medium.
- Additive layers over large areas cost fill rate. Keep the measured High 1080 budget (mean ≤ 8 ms, p95 ≤ 12 ms; round 10 runs at about 3.5 ms).

## Transparency and depth risks

- Normal-blend fire over light grass is what fixed olive in test B. Keep pack fire in normal blend with a separate additive glow.
- Check straight or premultiplied alpha per sheet (both packs say which) to avoid dark fringes.
- Depth stays as it is: flat decals with a small Y offset.

## Dragon breath risks

None for now: Dragonhold has no continuous breath attack.

## Prototype acceptance criteria

Reuse the test-A/B gates and judging protocol:
- both judges give impact, aftermath and colour/heat 8 or more;
- the foe is readable within 6 frames;
- the dragons are never covered;
- nothing remains at 2.5 s except a fading scorch;
- perf is within budget.

## Anything over-engineered in this V2

For Dragonhold today:
- the three.quarks adapter and spike;
- the BreathRibbon with flame chunks, pooling and its LOD;
- soft particles and depth integration;
- temporary-light prioritisation (one pooled light exists);
- WebGPU and heat-distortion notes;
- the full folder restructure.

## Anything missing

- What failed in our tests and why:
  - test A: flat material;
  - test B: right look but 1.8× size, so no punch.
  
  The plan must set the size and punch explicitly.
- The judging protocol: blind codes, real speed first, commercial anchors, and no builder text in the brief.
- That all suggested packs are code-generated, so the style test comes before any rollout.
- The cost-free first step: the free demos of both packs.
