# Monster rig test: reuse 3 monsters, Blender rig, walk / attack / hit (16/11/2026)

Owner, 16/11/2026: "chúng ta có thể sử dụng được 1 số hình ảnh 3d của quái từ các game đang có để lấy sang dùng thử và thiết kế blender cho nó khi thực hiện di chuyển, tấn công, và nhận sát thương được chứ? thử với vài con trước để test xem sao".

Status: **test only, not judged.** No blind judges ran, so nothing here claims the 8.5 bar (or 9 for character animation). Nothing committed; no media in Git.

## Picked monsters

These are the Wordwoven Tripo originals in `games/typing-defense/art-src/3d/enemies/`. Wordwoven's own rigs were not used. The 2D sources are `art-src/enemies/<id>.png`. I did not check whether their 2D sources passed review.

| id | Body | Tris (kept) | Why |
|---|---|---:|---|
| `troll` | heavy biped, back shield, fur skirt | 11,720 | inventory D1, heavy brute |
| `tanuki` | small biped, big belly, tail | 5,696 | inventory D12, has a tail for a tail chain |
| `nuppeppo` | blob with stub arms and feet | 5,910 | inventory D8, tests squash and stretch |

## Rig

- Blender 5.2, `--background --python`. Scripts live in `typing-game-review/owner-review/2026-11-16/tu-tien/monster-rig-test/blender-src/` (`build2.py`, `rigcfg.py`, `anim.py`, `params.json`, plus the checks `wcheck.py`, `wviz.py`, `stretch.py`, `rend_atk.py`).
- Bones use the canonical names: `pelvis`, `spine_01–03`, `neck_01`, `head`, `clavicle/upperarm/lowerarm/hand_l|r`, `thigh/calf/foot/ball_l|r`. The tanuki adds `tail_01–04`. The mesh is turned to face −Y in Blender (+Z in glTF and three.js). Tripo's auto rig was not used.

### Skin fix, 16/11 (owner: in `troll_side` the swinging arm stretched and melted into the ground)

Cause, as found:
1. **Joints placed wrong.** The joints had been read off renders by eye.
   - Troll and nuppeppo: the arm bones sat 0.07–0.15 inside the arms; the nuppeppo's were also 0.1–0.2 too far forward.
   - Tanuki: the bounding box included the tail, so the whole skeleton sat 0.04 to one side and 0.1 too far back.
   
   Fix: joints re-measured on 0.05-unit grid renders, with the arm joints checked against the mesh vertex means; left and right arms placed separately where the model is not symmetric. Proof: `attack-closeup/bones_on_grid.png`.
2. **Distance weights with a radius cap.** Arm vertices more than 0.14 from the arm segment (the outside of the troll's fist and forearm) went to the torso, so they stayed behind when the arm swung.
   - Before the fix, the troll had 536 vertices in the arm zone owned by the torso or legs, 454 arm vertices carrying more than 5 % torso weight, and 48 arm vertices carrying leg weight.

New skin pipeline (`build2.py`):
1. Copy the mesh and voxel-remesh the copy into a watertight proxy (4 mm voxels). Bind the proxy with Blender's heat weights, then transfer them to the real mesh (Data Transfer, nearest face interpolated).
2. **Arm guards:**
   - An arm vertex lies inside a tube around its own side's upperarm–forearm–hand chain, farther from the body midline than a set minimum, above the ankles, and closer to an arm bone than to any torso or leg bone (or the heat already gave it mostly arm weight).
   - Behind the arm the tube is only as thick as the arm (`r_back`), so the troll's back shield is not caught.
   - Arm vertices get no leg, pelvis or low-spine weight. Past the shoulder, the arm hands over from torso to arm bones over a smooth ramp.
   - Leg vertices get no arm weight. Leg weights are not allowed above the hip, or for the nuppeppo above the stubby legs, so its fat belly no longer folds with the thighs.
   - Vertices below the ankle listen only to the leg bones.
3. Laplacian smoothing over mesh edges for the shoulder and hip groups, then the guards again.
4. At most 4 influences per vertex, normalised. Vertices at the same position on UV seams get the same weights. Vertices left with no weight (2 on the troll, which pulled a sliver from the hand back to the hip) copy the nearest weighted vertex.

Checks after the fix:
- `wcheck.py`: no vertex with no weight, at most 4 influences, everything normalised. Arm vertices with any leg or low-spine weight: troll 2, tanuki 7, nuppeppo 0 (small weights from averaging seam vertices). Leg vertices with arm weight: 0.
- Weight map: `attack-closeup/weights_arm-red_leg-green_core-blue.png`.
- `stretch.py` counts edges more than 3× and more than 4 cm longer than at rest, during the attack:
  - troll: 240–350 before, now 9–61. What is left is the back of the shoulder when the arm goes up 150°, already blended between clavicle and upper arm.
  - tanuki: 0–9.
  - nuppeppo: 0–12.
- **Close-ups of every attack frame** (Blender, side and 3/4), and I looked at every one: `attack-closeup/<id>_attack_*.png` and `<id>_attack_closeup.mp4`.
  - Through wind-up, overhead hold, slam and recovery, the troll's arm and fist keep their volume. No spikes, no melting to the ground.
  - The tanuki's swipe and lunge and the nuppeppo's body slam are clean; the belly tear is gone.
  - I also checked lab frames 99–162 of `troll_side`, the stretch the owner pointed at.
- **Not done:**
  - no twist bones;
  - no corrective shapes for the shoulder when the arm goes overhead: the skin stretches over the shoulder blade, which a pose-space corrective would improve;
  - the troll's shield moves with `spine_03` and the clavicles, with no bone of its own.

## Clips (30 fps, sampled every frame)

| id | Idle | Move (cycle) | Attack: windup_end / release = `hit` / end | Hit: peak / end |
|---|---|---|---|---|
| troll | 2.0 s | 1.47 s | f20 (0.67 s) / f27 (0.90 s) / f62 (2.07 s) | f4 / 1.0 s |
| tanuki | 2.0 s | 1.0 s | f15 (0.50 s) / f21 (0.70 s) / f48 (1.6 s) | f3 / 0.87 s |
| nuppeppo | 2.0 s | 1.13 s | f17 (0.57 s) / f23 (0.77 s) / f50 (1.67 s) | f3 / 0.93 s |

- **Attack:** anticipation (lean back, raise or cock the arms, crouch), a hold at `windup_end`, a fast release over 6–7 frames, an overshoot hold, then an eased recovery. Per monster:
  - troll: two-arm overhead smash;
  - tanuki: right-arm swipe with a lunge and a tail whip;
  - nuppeppo: squash, then a stretched body-slam.
- **Hit:** recoil back with the head snapping, an overshoot forward, then settle. The nuppeppo also squashes.
- **Events** are in `glb/<id>.meta.json` (`windup_end`, `release`, `hit`, `recovery_end`, `impact_peak`). The lab fires them on the frame the clip time crosses them. On `hit`, a gold ring flashes on the ground; it is a placeholder, not VFX.
- **Walk:** a sine walk on plain FK slid badly. The stance-foot speed's standard deviation was larger than its mean. I replaced it with analytic two-bone leg IK on planned foot paths: the stance foot moves backward at constant speed, and the swing foot follows an arc. A three-pass correction lands the foot on target.

  Measured stance-foot speed (model units/s at scale 1; frames within 1.2 cm of the ground):

  | id | mean | sd |
  |---|---:|---:|
  | troll | 0.276 | 0.111 |
  | tanuki | 0.322 | 0.048 |
  | nuppeppo | 0.156 | 0.035 |

  The sd mostly comes from the first and last swing frames that fall inside the window. The lab moves each monster at mean × scale.

## Lab (dev-only, new files only)

- `games/.wt-ic-lab-all/monster-rig-test.html`, `src/lab/monster-rig-main.ts`. Not in `vite.config.ts` build inputs.
- `games/.wt-ic-lab-all/public/monster-rig-test` is a **symlink** to `…/monster-rig-test/glb/` in the review folder. Do not commit it, and delete it before deleting the review folder.
- **Scene (redo, 16/11, after the owner rejected the framing):** the game's own renderer (`createRenderer`, High, Neutral tone mapping, bloom), the lab look (`applyLook`: misty_pines HDRI, north-east sun, soft shadows) and the paved field (`buildField`), the same calls `skills-lab` uses. No flat green plane.
  - The KTX2 transcoder returns 403 from this worktree, so the field uses the packed ORM JPGs (`look.ts` falls back on its own). They are the same pictures.
- **Camera:** the play tilt (55°, `CAMERA.defaultTiltDeg`) and FOV 28° (`VIEW.fovDeg`). It follows the monster, as the game's close zoom follows the hero.
  - Framing: the rest mesh fills 60 % of the frame height, and every skinned pose of every clip stays inside 80 % of the width and height, so the margins are 10 % on every side.
  - The pose envelope is measured at load by skinning about 200 vertices through every frame of every clip. Bone boxes alone missed the tanuki's big head during the lunge.
  - The target follows the root exactly; only the distance is smoothed.
- **Close side view:** FOV 28°, 25° above the ground, from the monster's left, centred, with the rest mesh at 60 % of the frame height.
- URL: `http://127.0.0.1:3150/monster-rig-test.html`.
  - `?mon=troll|tanuki|nuppeppo`: one monster alone.
  - `?cam=side`: the close side view.
  - `?hud=0`: hide the HUD.
  - `?fixed=1`: step frames by hand with `window.__rig.advance(dt)`; `__rig.frameShare()` returns the framing numbers.
- Keys: `1`/`2`/`3` pick a monster; `W` walk, `A` attack, `H` hit, `I` idle; `Space` runs the automatic loop; `C` switches between the play camera and the side camera.
- It uses plain `AnimationMixer` crossfades (0.12–0.18 s). The `anim/` Animator is not wired in.

## Outputs

`typing-game-review/owner-review/2026-11-16/tu-tien/monster-rig-test/` (overwritten 16/11 after the framing redo):
- `clips/`: `<id>_play.mp4` and `<id>_side.mp4` for each monster, plus `all_play.mp4`. All are 1280×720, 30 fps.
- `sheet_<clip>.jpg`: frame grids (every 17th frame, 4×3), used for the framing check.
- `framing.json`: the measured framing numbers, below.
- `glb/`: the GLBs and meta files.
- `attack-closeup/`: every attack frame as close-ups and grids, the weight map, and the bones drawn on the grid renders.
- `blender-src/`: the scripts and `.blend` files.
- `ABOUT.md`.

Measured framing (re-captured after the skin fix; troll 0.46, tanuki 0.52, nuppeppo 0.54 of the frame height at the play camera) (NDC, the frame spans ±1; extent over every pose):

| Clip | Width (±) | Height (±) | Rest mesh, share of frame height |
|---|---:|---:|---:|
| troll_play | 0.40 | 0.80 | 0.47 |
| troll_side | 0.34 | 0.70 | 0.60 |
| tanuki_play | 0.39 | 0.80 | 0.52 |
| tanuki_side | 0.35 | 0.64 | 0.60 |
| nuppeppo_play | 0.41 | 0.80 | 0.54 |
| nuppeppo_side | 0.32 | 0.63 | 0.60 |
| all_play | 0.80 | 0.77 | 0.44–0.60 |

- The troll at the play camera is about 47 % of the frame height. Its overhead smash takes the 80 % room, so it is a little under the 50 % asked for.
- In the group view the width is the limit: three monsters side by side in 16:9.
- The `hit` ring is a placeholder, now small and at the feet; in the earlier run it spilled past the frame edge.

## What worked, what did not

**Worked:**
- An existing Tripo mesh plus our own scripted rig and clips loads and plays in three.js without errors.
- Canonical names are in place, so the clips could later be retargeted or moved onto the lab Animator.
- Attack events land on exact frames.
- After the IK walk, sliding is small.
- The nuppeppo's squash and stretch reads well.

**Weak or not working:**
- **Rig quality is test level.**
  - ~~When the troll raises its arms overhead, they thin out and stretch~~: fixed on 16/11 (see "Skin fix"). The skin still stretches a little over the shoulder blade when the arm goes overhead; there are no corrective shapes or twist bones yet.
  - The shield and fur skirt have no bones of their own: the shield follows `spine_03` and the clavicles, the skirt follows the hips and thighs.
  - The nuppeppo's arms are short and fused into its body, so arm motion reads less than body motion.
- **Foot sliding:** small, but not zero. It is not foot-locked in the game, and the 0.18 s crossfades between Move and Attack slide the feet.
- **Weight:**
  - the troll's crouch and smash have weight, but its walk looks stiff and squats a lot;
  - the tanuki's tail moves on a sine, not on springs;
  - none of them have secondary motion (springs) or a body reaction to the hit beyond the clip.
- **Readability at the play camera:** at about 55° from above with small monsters, the walk reads mostly through the arms and the bob. The attack anticipation reads clearly; the hit react is short and reads less well.
- Not scored. Next, if the owner wants this approach:
  1. Wire it into the `anim/` Animator, which adds inertialization, `foot-ik`, and springs for the tail and skirt.
  2. Add skirt and shield bones and paint corrective weights.
  3. Two blind judges.

**Lessons for the Blender scripts:**
- Tripo GLBs import with a parent node. Use `parent_clear(CLEAR_KEEP_TRANSFORM)`. Then rotate with `mesh.data.transform(...)`, because setting `rotation_euler` and applying it did nothing.
- In pose scale on Blender bones, the bone axis is local Y, and scale compounds down the chain.
