> 31/10/2026 · Phân tích vì sao lửa rồng Dragonhold đi ngang quanh 8 điểm (workflow `dragon-fire-diagnosis`, `wf_67d78548-8a1`): đọc lại phiếu chấm vòng 4–10, soi code nhánh `dh-vfx`, đối chiếu cách game thương mại làm lửa. Bản tổng hợp dưới đây bằng tiếng Anh như báo cáo gốc; tóm tắt tiếng Việt nằm trong tin nhắn trả lời chủ dự án cùng ngày.

# Dragon fire (Hỏa Long): why the score is stuck near 8, and what to do instead

**Short answer:** The plateau comes mainly from our method. It is not judge bias and it is not lack of effort.

From round 8 to round 11 the lane turned each set of verdicts into about nine parameter or shader patches. The fire they were patching cannot reach 8.5:
- it is video fire whose transparency comes from its brightness;
- it is laid half-transparent over bright grass;
- the colour grade bleaches hot orange to peach;
- nothing glows on the judged High tier;
- the smoke is unlit.

Geometry defects were fixed in one or two rounds each. Material defects only changed form: olive, then rust lace, then mustard, and in round 11 a brown cut-out and a grey cardboard cloud. I checked the round-11 frames myself.

The judging setup adds about ±0.5 of noise and some unfair deductions, but it does not explain the gap. The aftermath and charge phases really are weak. Until this review, nobody tried a structural change.

## 1. Root causes

### RC1: Fire transparency comes from brightness (our approach; the biggest single cause)
- **How it works now:**
  - 10 of the 11 Firefly clips have `alpha:false` in `public/assets/dragon-hold/vfx/firefly/manifest.json`. Only `smoke-roll` has an alpha channel.
  - The shader sets `body = smoothstep(0.02, 0.45, lum)` and outputs `vec4(rgb*soft, body*vOcclude*soft)` (`src/view/flipbook.ts` around lines 355–365). Cooling then lowers `body` further.
  - So a dim or cooling flame becomes a see-through orange veil. Orange at alpha 0.25 over grass (125, 155, 85) gives (149, 146, 66). Judge B measured (150, 157, 90) at strong frame f080 in round 10. Over sand the same veil turns salmon or khaki.
- **History:** this defect was flagged in about 10 verdicts from round 6 to round 10. Each round tried a different parameter fix:

| Round | Fix tried |
|---|---|
| r7 | char colour |
| r8 | premultiplied alpha, occlude 0.85 |
| r9 | cooling ramp and erosion |
| r10 | cooling from 30 % of life, smoke drawn over the fire |
| r11 | violet-grey rims, noise cut-outs, `uSolid` |

- **What round 11 shows:** the round-11 gate shows the olive share falling from 0.56 to 0.0077. But frames c074–c078 of the round-11 strong clip show an opaque brown-red silhouette and black or violet flecks. Judges already marked that look down in round 9 as "rust lace" and "hard-edged red cut-outs." The fixes swing between two failures of the same model.
- **Where we were wrong:** for four rounds we treated a missing transparency channel as a colour-tuning problem.

### RC2: The colour and light pipeline cannot make fire read as hot light (our approach, partly an owner constraint)
- **Tone mapping:** the grade uses Khronos PBR Neutral with desaturation 0.15 (`mix(color, vec3(newPeak), g)`), followed by `uHighTint` (1.04, 1.01, 0.94) (`src/view/stage.ts` around lines 100–137). Orange at 4× brightness comes out as (255, 197, 150), which is peach, not yellow. A judge measured the Sky Fire core at (255, 237, 210).
- **No glow:**
  - High has no bloom (owner decision 29/10, `STAGE_QUALITY`).
  - Ultra's bloom threshold of 1.6 is never reached, because the 8-bit flipbooks peak at about 0.7 linear.
- **We skipped our own rule:** `VFX_STANDARD.md` §3.5 rule 2 says the tier without bloom must still read through painted halos and dark layers. No halo sprites were ever built.
- **The workaround made it worse:** to dodge the tone mapper, the lane picked a pastel palette: `fire` #ff9e6b and `fireHot` #ffd9a0 (the reason is in a comment at `fx-palette.ts:13–16`).
- **Result:** colour/heat sub-scores of 7.0–7.5, and the judges' words "sticker", "clip-art star" and "not hot".

### RC3: The aftermath and charge are built from stand-ins, and they cap the total
- **The cap is arithmetic:**
  - Across all 12 verdicts, the word-attack aftermath (F) never scored above 7.5; rounds 9–10 gave 6.0–7.0.
  - No charge phase (A) ever scored above 8.0.
  - Even with release, travel and impact at 8.5, the five-phase mean is 8.2, and the "no phase below 8" rule still fails.
  - Most of the round 8–10 effort went into release, travel and impact, which cannot lift the total enough.
- **Smoke:**
  - The shader keeps only density (`d = sqrt(lum)`). It paints two constant colours plus a fake highlight and ignores `SUN_DIRECTION`.
  - It is drawn over the fire (render order 5.35 against 5.3) and appears 8–12 frames after it.
  - It is scaled to 1.7× the hit's mass, while §5.3 asks for a small grey smoke on a word shot.
  - In round 11 it is an opaque grey cloud larger than the blast. It covers the foe, the river and the "128" damage number for about 1 s (`r11-f-strong.jpg`, which I looked at).
- **Burn marks and cracks (decals):**
  - They are generated in code: a Voronoi crack mask and radial marks. Judges called them "pinwheel", "honeycomb" and "oval hole" from round 7 to round 10.
  - Meanwhile the painted `scorch.png`, `fissure-a/b/c.png` and `smoke-strand.png` from ticket 038 sit unused in `games/dragon-hold/art-src/vfx`. Nothing in `src` references them.
  - This also breaks the owner's rule against code-drawn stand-ins.
- **Charge:**
  - It is a flat 2D "galaxy" swirl, with no pull into the mouth and no light on the dragon.
  - Three requests were never attempted: a volumetric orb, the dragon glowing, and the Perfect trail made of the word's letters (§3.3, asked for in 6 verdicts).

### RC4: One symmetric source clip, retimed, serves every tier (our asset choice)
- **The clip:**
  - `impact-burst` is a symmetric gear shape with 6–8 lobes, in 256-px cells, 30 frames at 12 fps, blended by plain crossfade.
  - The strong hit plays frames 11–19 at ×1.8. Round-11 Sky Fire plays the same clip, frames 7–20.
  - Judges called it "gear-tooth lobes" and saw the shape hold still for about 20 frames (both round-10 judges, Sky f072–f092).
- **Sky Fire is not bigger:**
  - On screen it is about 170–210 px against about 180 px for the strong word hit, only 1.0–1.2×.
  - The dome or ring was flagged in 9 verdicts from round 6 to round 10. The radius metric reads 1.00, but the dome sits hidden under the explosion.
  - The order of tiers is inverted: the ultimate is no heavier than a word shot.
- **Style clash:** semi-photoreal video fire sits next to a cel-drawn meteor in a painterly world. It is judged against Kingdom Rush, Clash Royale, BTD6 and Orcs Must Die 3. Judge A flagged this in rounds 8 and 9, and it is still open in the round 9 and 10 changelogs.

### RC5: Process (our fault) and judging (an artifact, but a smaller one)
**Our process:**
- **Patching one symptom at a time with no test bench:** about 9 fixes per round, and new defects appeared each round.
- **Gates that measure the symptom, not the look:**
  - Every numeric check in §5.6 passed from round 5 to round 10.
  - Round 11's olive and straight-edge gates are satisfied by an opaque cut-out.
- **"Done" fixes nobody could see at the play camera:** rune strokes are 1–2 px at 720; the judges saw no meteor ground shadow in rounds 9–10; the dome is hidden.
- **Capture errors:**
  - There was no PLAIN clip in rounds 8 and 9.
  - In round 10, the PLAIN clip was actually the PERFECT "128" shot: both judges measured about 1 % difference from the strong clip.
  - In round 9, the Sky 720 dark capture was covered by a pause overlay.
  - In round 10, the WebGL context was lost and the Sky pass recaptured.

**Judging artifacts:**
- **Noise is as large as a round's gain:** STRONG travel went from 8.5/8.5 in round 9 to 7.5/7.5 in round 10 on nearly identical frames.
- **A conjunctive gate:** about 30 judgments must each reach 8, and since round 9 smoke is scored three times.
- **Silent clips stepped frame by frame at 2–3× zoom:** each 2–3-frame transient costs 0.5–1 point.
- **One scenario:** a river ford, so the aftermath always lands on water, bank and bright grass.
- **The reference image is holy light on a dark background, not fire.** No commercial clip was ever scored under the same protocol, so "9" has no anchor.

My estimate: the judging artifacts explain about 0.3–0.5 points of the gap and most of the swings between rounds. The rest is real.

## 2. Options

| | What changes | Expected ceiling | Agent cost | Owner time | Risk |
|---|---|---|---|---|---|
| **Baseline: a 12th round of patches** | more parameters on the same model | about 8.2 (the arithmetic cap; the fixes keep swinging) | 1–2 days per round | none | it keeps failing |
| **A. Rebuild the fire material and layer stack, keep the Firefly sources** (recommended) | listed below | **8.5–8.8** | 6–8 days | 1 Firefly session (4–6 Sky Fire clips, about 1 h) plus the decisions below | medium-low |
| **B. A plus stylized (cel or anime) fire sources** | same shader; impact, trail and smoke from hand-drawn or cel Firefly clips (or painted keyframes via Firefly Image); stepped erosion; smoke in 2–3 toon bands | **9+ if the clips stay coherent** | A plus 3–4 days | 10–15 clips over 2 sessions, plus retries (rate limit about 10 per burst) | high |
| **C. A plus simulated sources** | CC0 Unity Labs Houdini flipbooks with temperature channels, or Blender Mantaflow renders with separate density, temperature and emission passes plus motion vectors | 8.5–8.7 | A plus 3–5 days | none (check each CC0 asset's licence) | medium |

**What A changes:**
1. **One fire material.** The flipbook tool re-exports the atlases with a real coverage channel. It comes from the tool's existing `luma_matte` path, widened 2–3 px and taking the maximum over neighbouring frames. The shader colours the fire through a colour ramp (char, dark red, orange, yellow, near-white). The fire disappears by erosion, an alpha threshold that rises over its life, with a burnt dark-red edge, and its glow erodes faster than its coverage. It is composited as a dark body blended normally plus an additive glow. This removes both the olive and the cut-out failures.
2. **Lit smoke under the fire.** It starts on frames 0–3 and outlives the fire. It keeps the clip's own shading, lit by the sun direction (or uses CC0 six-way lightmaps). It is drawn as 3–5 smaller sprites, no larger than the blast on a word shot.
3. **Painted textures.** Use the 038 scorch, fissure and smoke-strand images. Add Firefly Image stills for the halos, the flare and the charge streaks.
4. **Glow on High.** Painted halo sprites, as §3.5.2 already requires. Half-resolution bloom is a measured option for the owner.
5. **A grade shoulder that moves hot, saturated values toward yellow.**
6. **Sky Fire gets its own asset.** An asymmetric column or mushroom explosion in 512-px cells, 48–64 frames, with a vertical dome or dust ring outside the blast, 1.5–2× the strong hit on screen.
7. **A new charge.** Ember streaks pulled into the mouth, plus mouth light on the head.

**Why A tops out at 8.5–8.8:** it removes the lowest sub-scores: the aftermath, colour/heat, and light ground at 720. Getting the charge to 8.5 also needs the dragon to glow or its attack clip to charge with typing progress, which needs kit mixer access. A score of 9 is unlikely while the clip shapes stay semi-photoreal.

**Risks of A:** the matte may still leave a halo around the fire, and the grade change affects the whole map, so the owner has to check the map.

**Why B could reach 9+:** it matches the judges' references, the cel meteor and the painterly world. It needs A's shader anyway. The risk is that Firefly has never proven it can keep 2D fire consistent from frame to frame; the earlier "flat cartoon" fireball v2 was rejected, though under the old brightness-keyed shader.

**Why C stays at 8.5–8.7:** it gives clean coverage and motion vectors, but the style clash gets worse. The 2016 assets may be low resolution.

**Recommendation: A.** Once the one-day slice below proves the shader, run B as a half-day style test: 3–5 cel clips through the same material, scored blind against A. Use C only if Firefly matting fails the slice.

**Fix the judging protocol before the next judged round, and keep the bar at 8.5 from both judges:**
- the judges first score 2–3 commercial clips blind (Kingdom Rush Rain of Fire, Clash Royale Fireball, BTD6 Dragon's Breath) to anchor what 9 looks like;
- the score comes from real-speed playback at the play camera; stepping frame by frame is only for writing up defects;
- use three grounds: the ford, open grass and dark ground;
- check that the PLAIN clip really is a plain shot;
- add sound if the fire sound effects exist;
- score smoke once.

## 3. One-day test: the strong hit only

**Scope:**
- The STRONG word hit, impact and aftermath phases only, plus a halo at release.
- Release, travel, timing, hit-stop and the damage number stay frozen at round 10.
- Start from `ca64509` (round 10), not from round 11. Port only `scripts/visual/vfx-gates.mjs` and the plain-shot check.
- A test-bench scenario puts the same foe on three grounds: the ford, the dais or sand, and dark ground. Capture at the play camera at 1280×720 and at 1920×1080.

**Steps (one agent-day, no Firefly credits):**
1. Re-export `impact-burst` and `smoke-mask` with the tool as RGBA, coverage from `luma_matte`, widened and maxed over neighbouring frames. About 1.5 h.
2. Build the fire material path in `flipbook.ts`: colour ramp, erosion, burnt edge, separate glow, normal-blended body plus additive glow. About 3 h.
3. Put smoke under the fire: starts at f+2, 3–4 sprites, shaded by the clip times the sun, no larger than the blast, 45–80 frames with an ease-out. About 1.5 h.
4. Swap in `scorch.png` for the procedural mark, and add a halo behind the body made offline from a blurred copy of the clip's peak frame. About 1 h.
5. Add a test-bench-only toggle between the current grade and the yellow shoulder, and capture both. About 0.5 h.
6. Capture, run the gates, send to judges. About 1.5 h.

**Measured acceptance (every ground × both resolutions):**
- **Neither failure mode:**
  - olive or mustard share in the fade frames ≤ 0.02 (the existing gate);
  - **and** brown-silhouette share ≤ 0.03 from f+15 onward (hue 0–30°, saturation ≥ 0.5, value ≤ 0.35, inside the effect mask).
- **Edges:** no straight edge over 20 px at 1080.
- **Value ladder at the peak, in greyscale:**
  - rim ≤ 0.30;
  - body ≥ ground + 0.15;
  - core ≥ 0.90, with the white core within 30 % of the effect's radius (§3.5.3);
  - white ≤ 6 % of the field.
- **Colour at 1080:**
  - core hue 35–55°;
  - peach or salmon pixels (hue 10–30°, saturation ≤ 0.45, value ≥ 0.85) ≤ 2 % of the effect.
- **Smoke:**
  - at its largest, no bigger than the fire's peak area;
  - covers the foe or the number for ≤ 10 frames;
  - lit side minus shaded side ≥ 0.12 in brightness;
  - coverage never drops by more than 25 % in one frame.
- **No frozen shape:** the fire's outline overlaps itself 4 frames later by no more than 0.85 (IoU), from f+0 to f+20.
- **The existing checks still pass:**
  - first flash frame ≥ 95 % of the peak;
  - word tag contrast ≥ 7:1 at p99;
  - `dh-perf` High 1080 mean ≤ 8 ms and p95 ≤ 12 ms (expect about 4).

**Judges:**
- Two new judges see the clips at real speed and stepped, in blind order, next to the round-10 STRONG clip and one commercial clip.
- Pass:
  - both judges give the aftermath **≥ 8.0** (it has never passed 7.5);
  - colour/heat ≥ 8.0;
  - impact ≥ 8.0;
  - no other phase falls below its round-10 score.

**Stop rule:** if either judge gives the aftermath below 7.5, or the two colour checks cannot both pass on at least two grounds, the Firefly matte is the limit. Then change the source (C or B) instead of tuning parameters.

## 4. What to keep from rounds 1–10

**Freeze these phases, already at 8.5–9:**
- STRONG release: 8.5 from both round-10 judges.
- Sky Fire travel arc: 8.0–9.0, with at least 90 % of the arc in frame.
- Sky Fire release: 8.5 in three of the four round 9–10 verdicts.
- STRONG travel as it was in round 9: 8.5/8.5.

**Keep these fixes:**
- the cone hard cut (round 7);
- the damage-number position (round 9);
- removing the pink wash on the dais (round 9);
- the Sky release core and fan (round 9);
- the meteor draw order (round 10);
- removing the sticker star (round 10);
- hit-stop and camera kick;
- the timing table in §3.4.

**Keep the tooling:**
- `tools/vfx-flipbook`, including `luma_matte`, `grade` and `timing`;
- the flipbook pools and instancing;
- the `dh-vfx-word` and `dh-vfx-skyfire` capture scenarios;
- round 11's `vfx-gates.mjs` and plain-shot check, as regression gates only, not as acceptance;
- the `dh-perf` data: about 4 ms of headroom on High.

**Keep these assets:**
- the Firefly clips, used as density sources;
- the painted 038 textures, which still need to be wired in.

**Drop:**
- using brightness as transparency;
- the two-colour smoke shader;
- the Voronoi cracks and radial marks;
- the galaxy charge orb and the star flare;
- the pastel palette;
- round 11's opaque noise cut-outs, `uSolid` and `PUFF_SOLID`;
- the oversized word-shot smoke;
- reusing `impact-burst` for Sky Fire.

**Do not send round 11 to the judges as it is.** It is uncommitted and shows the cut-out failure.

**Decisions for the owner:**
1. Approve approach A and the one-day test.
2. Glow on High: painted halos (the default, per the standard), or measured half-resolution bloom (about 1–2 ms, and it reverses the 29/10 decision).
3. Allow the grade shoulder change, which affects how the whole map looks.
4. Approve the judging-protocol change, with the 8.5 bar unchanged.
5. After the test passes, one Firefly session for the Sky Fire column explosion, plus 3–5 cel clips for the B style test.

Contact sheets backing this report:
- /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/f97baf5f-4f81-4f84-8ec0-79083d7e3ba9/scratchpad/audit-fire/r11-f-strong.jpg
- /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/f97baf5f-4f81-4f84-8ec0-79083d7e3ba9/scratchpad/audit-fire/r11-g-sky.jpg
- /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/f97baf5f-4f81-4f84-8ec0-79083d7e3ba9/scratchpad/audit-fire/impact-burst.jpg
- /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/f97baf5f-4f81-4f84-8ec0-79083d7e3ba9/scratchpad/tcmp/decals.jpg
- the colour calculations: /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/f97baf5f-4f81-4f84-8ec0-79083d7e3ba9/scratchpad/audit-fire/tm.mjs

Nothing in the repo or the worktree was modified.
