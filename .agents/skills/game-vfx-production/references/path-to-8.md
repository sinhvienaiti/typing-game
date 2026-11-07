# Path to 8.5: how a VFX reaches the bar

Agreed on 07/11/2026:
- the owner approved two-tier judging ("tôi đồng ý điều này, phải note lại để sau xử lý hình ảnh hay video còn làm theo");
- Codex reviewed the draft after reading 467 lane-C verdicts (`docs/work/consult/codex-path-to-8.md`; read its 300-word summary first);
- Claude settled the result below.

Applies to every game's VFX, CGI layers and their source media.

## Why this exists
- On 06–07/11, 467 raw Firefly clips were scored as if each were a finished effect: 0 reached 8, best 7.5.
- A prompt-only redo of 10 clips moved the average only from 5.60 to 5.95.
- Raw clips are layers. The score belongs to the composited effect.

## 1. Two tiers
- **Tier A, source layer** (clip, render, still, flipbook, sprite): PASS, FAIL or NOT-ENOUGH-EVIDENCE **for its declared role**. Five boxes, each with evidence:
  1. **role and shape:** right silhouette, colour, direction, identity marks; no parts growing or vanishing, no stray objects in the used segment. Progress layers follow typing, never the clip's brightness;
  2. **margin and stability:** core ≥ 5 % from every edge in every used frame; centre drift ≤ 2 % of the short side; size change ≤ 5 % while sustaining, unless designed. Full-screen rays and tiling strips check their seam or endpoints instead;
  3. **background and matte:** RGBA edge alpha ≤ 2/255 with no dark or white fringe on light and dark grounds. Additive on black: background p99 ≤ 4/255 per channel. Dark smoke or stone needs real alpha or its own mask;
  4. **time:** a one-shot ends at alpha ≤ 2/255 after the engine envelope; a sustain need not fade. A loop checks the last-to-first jump against neighbour frames (warn above 2×) plus colour, centre and shape, and plays 10 cycles at real speed;
  5. **sharpness and packaging:** checked at real pixel size and speed, with no stepping, ghosting, atlas bleed or compression smear. A burst has ≥ 24 frames, never by duplicating frames.
- A technically clean layer can still FAIL on role: a charge fill that sweeps instead of accumulating fails.
- A hero layer seen large must still look good alone. Compositing never excuses ugly material.
- **Tier B, composited effect** in the built play host, scored 1–10:
  - axes: appeal and style; shape, material and light; rhythm and force; interaction and role; readability;
  - each judge names the biggest flaw, with phase and time;
  - pass only when both blind judges reach ≥ 8.5 (shared systems ≥ 9); 8 is a progress mark, not a pass;
  - the gates of VFX_STANDARD still apply.

## 2. What fixes what
- **Engine owns macro timing:** start, path, direction, lifetime, envelope, reveal, erosion, light pulses.
- **The source owns internal motion:** a slash's leading edge, curling smoke, a wave crest, creature limbs. Scale and alpha curves cannot create these, and over-driving them makes the effect look more like a video.
- **Phase-offset flipbooks** only hide sync between instances; they never fix a seam inside one instance.
- **Diagnose before regenerating:**
  - still wrong → fix the still;
  - still right but fitted or cropped wrong → refit the same still;
  - model drifts later → keep the clean segment or redo image-to-video from the same still.
- **Design for separation:** stone base, emissive cracks, energy and particles are separate sources or masks, each with its own control. Do not bake them into one still and hope to fix them apart.
- **Radiance belongs to the composite's phases**, not to every source. A mask prompt describes only the mask; sparkle is its own painted layer.
- **HDR cores and bloom** only shape hierarchy. A burnt-white MP4 cannot be recovered by adding HDR.

## 3. Process for one effect
1. **Lock the effect and the real scenario:** action class, size at the play camera, approved internal references, instance count, input, release and hit events, light and dark ground, settings, budget. List the five phases and the radiance per phase, caster side first.
2. **Map the layers and who controls them:** for each layer write its role, source or still, blend, view, what the engine controls, the useful segment and the packaging. Use existing sources first.
3. **Triage before making anything new** (§4).
4. **Run tier A by role.** New sources start with two samples, which go to the owner before any batch.
5. **Build one five-phase sample in the lab:**
   - the engine drives the macro rhythm;
   - release, light, target reaction and sound meet on the event frame;
   - no sim or canon change to hide timing.
6. **Find the weak layer** by switching layers on and off with the same camera, seed, clock, ground and volume, and look at a muted pass too. Replace or reduce a layer rather than add more.
7. **Score tier B** in a loaded scene: one cast, many instances, cold and warm load, light and dark ground, reduced motion. Judge in the host's default settings; flags are only for diagnosis.
8. **Fix at the right place:**
   - timing → engine;
   - mask → processing;
   - broken material → source;
   - wrong shape → still.
   Then finish the sample, get the owner's before/after review, then scale. At most 3 tries of one method without progress, each try with a written hypothesis, then change method or ask the owner. There is never a best-of pass.

## 4. Triage labels (unit = job + role + used segment)
- **KEEP-TUNE:** a clean segment exists for the role. What remains is trim, retime, envelope, reveal, erosion, grade, fit, alpha, or one independent extra layer. Record in/out frames and every operation.
- **REDO-IMAGE:** a shaped layer with no segment that passes tier A. Mark the image as one of:
  - keep (redo image-to-video from it);
  - fix (repair the measured fault);
  - new (owner picks it).
  A still shared by several jobs gets one fix; the other jobs depend on it.
- **REDO-BLENDER:** a pure-material layer that fails on motion, volume, dissolve or alpha. Two samples must beat Firefly in a composite before any batch. Blender can also be an extra layer over a good Firefly clip.
- **DROP:** duplicate, superseded with evidence, or wrong for every role. Keep the files and the reason; a score under 8 is never a reason to drop.
- Missing metadata (use, prompt, still, hash) is a **NOT-ENOUGH-EVIDENCE** status to trace, not a fifth label.

**Priority:**
1. layers already called in the lab with visible faults;
2. assets reused many times;
3. the five-phase sample the owner will judge;
4. unwired sources.

Within one level, fix shape, crop and missing caster side first, then timing, matte and radiance.

## 5. Stills for image-to-video
- Match the target aspect and the contain fit, and preview frame 0.
- Start an isolated, blooming shape at 60–70 % of the usable width or height, halo included. Check `g·w + 2·d + 2·m ≤ W`, where `g` is the expected growth, `w` the shape width, `d` the drift and `m` the margin; the same for height.
- Light shapes go on even black. Dark smoke or stone needs alpha or a mask. No floors, shadows or third-party images.
- Use a clear pose at the play camera. Flying things stay in place in the source; the engine moves them. Creatures are energy forms with even detail.
- Colour in the body, thin bright cores, no baked white block or thick bloom.
- One main motion task per source. Dissolve comes from the engine (erosion or a tail layer), never from the still.
- Write prompts as positive task statements: subject, axis, what moves, rhythm or sustain, envelope, camera, background.

## 6. Who does what
- **Codex streams**, each owning its own output folder:
  1. KEEP-TUNE (derived assets and recipes);
  2. REDO-IMAGE (stills and image-to-video inputs);
  3. REDO-BLENDER (render recipes and RGBA).
- Only the integrator (Claude, or one lab lane) edits manifests and lab call sites.
- Codex cannot drive Firefly: Claude runs image-to-video from approved stills. The driver refuses text-to-video unless the job says `"material": true`.

## 7. Small measured steps and the performance budget (owner, 07/11/2026)
The owner said, after round 1 of the pilot: "nên chia nhỏ ra, thử làm 1 vài phần nhỏ trước để kiểm tra xem solution làm có thực sự hiệu quả không, có khả thi đạt trên 8 điểm hay k … đẹp, mượt là sự ưu tiên hàng đầu, nhưng k thể bất chấp … chúng ta chấp nhận đánh đổi hiệu năng để làm cho nó đẹp và mượt, nhưng ở 1 mức nào đó mà thôi, k thể cứ viết 1 đống code phình to, hoặc ném nguyên toàn bộ r làm nó giật lag".

**One small step at a time:**
- Each step changes one phase or one group of layers, behind a flag, and is measured before the next step starts.
- **Measure** with a framed before/after capture at the play camera (plus a close-up if needed), a blind tier-B score of the phase changed and of the whole effect, and the frame-time delta.
- **Continue** only if the step raises its target axes, with no axis dropping and the budget kept. After two steps without a real gain, stop and rethink. Never build the whole effect and judge it only at the end.

**Performance budget per effect:**
- Measured on the M4 lab: 1920×1080, DPR 1, quality High, median of runs, with `scripts/visual/scenarios/lab-element-perf.mjs` or the same method.
- **Frame time:** at most **+1.0 ms p95** over the same scene without the effect, and frame p95 stays **≤ 11.5 ms**.
- **Memory:** extra GPU texture ≤ **64 MB**, with KTX2 when available. Atlases load lazily and free when unused.
- **Draw calls and video:** ≤ **12 extra draw calls** per instance, pooled; **≤ 3 videos** at once.
- **No allocation per frame** once warm.
- **Code stays lean:**
  - reuse the shared flipbook library, pools, players and the existing phase runners;
  - one small module per pattern, not per skill;
  - a step adds about **≤ 250 lines** unless the report justifies more;
  - no new shader unless a measured A/B shows it is needed.
- **Prefer the cheapest layer that looks the same:**
  - a sprite or decal over a full-screen flipbook;
  - a shorter or smaller atlas when the difference cannot be seen at play size.
- **Over budget:** cut or merge the weakest layer, or lower its resolution or frame rate where the eye cannot tell. Never let the effect stutter.
