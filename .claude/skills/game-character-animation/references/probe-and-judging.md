# Motion probe, captures and judging

## 1. The probe's gates

The probe (`games/immortality-cultivation/src/lab/motion-probe.ts`) samples what was drawn, once per frame after the render. It reads the bones, root and feet, and every mesh of the FX layer, from their own attributes and uniforms; it never changes the clips or the VFX. Its per-frame path allocates nothing. Gates (`MOTION_GATES`, from CHARACTER_ANIMATION §5.11):

| Check | Gate |
|---|---|
| Bone angular speed in a transition | ≤ 1.5 × the active clips' peak |
| Foot speed while planted (lower foot under 4 cm) | ≤ 0.05 m/s |
| Loop seam | ≤ 1 cm |
| Ground penetration | ≤ 2 % of height |
| Clip event drift | ≤ 1 frame |
| Last key to body release | ≤ 50 ms |
| Charge silhouette against release (mean key-joint distance) | ≥ 15 % of height |
| A layer's alpha or size in one frame, outside a declared flash | ≤ 30 % change of its full level |
| Frames near the bind pose | none |
| Root turn / root speed | snap above 1,800°/s, teleport above 15 m/s |
| Blade direction / centre in one frame | snap above 30°, jump above 3 m |

- **Arms-out check** (`arm-check.ts`): a frame is flagged when both upper arms are abducted past 70° in the torso's plane. More than 3 flagged frames in a row, outside a pose the Animator declares intended, is a failure. It was built after both judges saw the arms held out after K5.
- **Fair pops:** a layer's rise is judged against the level it reaches within 0.25 s, so a slow fade-in never scores worse than an instant pop.
- **Peaks from the authored clip:** when the played clip is resampled, the reference peaks come from the 24 fps original.
- **Frame-rate check:** run once more at 120 Hz with metrics only. A true snap doubles its per-second rate at 120 Hz.
- Crowds add one more gate: fewer than 10 % of neighbour pairs in phase for over 1 s (CHARACTER_ANIMATION §5.11).

## 2. Captures

The lab's scenario (`games/immortality-cultivation/scripts/visual/scenarios/lab-motion.mjs`) runs on the fixed clock of the dev-only page (`?fixed=1`). Its sequence: idle, walk, run on an arc, stop, turns of 90° and 180°, strafe, dash, every skill typed at 45 WPM, a hit, back to Idle. It writes:
- `metrics.json`: the probe's report;
- transition sheets: 6 frames (f−2 … f+3) round each state change, close-up row over play-camera row;
- per-phase sheets: 12 frames per phase, snapped to clip changes, last keys, strikes and hits;
- a half-speed clip (every 1/60 s step encoded at 30 fps) and a real-time 60 fps clip;
- both at the play camera and a close-up (55°, 6 m), at 1280×720 and 1920×1080.

Delete the raw frames once the sheets and clips are made, through the prune tool.

## 3. Blind judging

- **Judge sheets print no metrics:** phase words only, no ratios, bone speeds or gate colours. Tu Tien round 2's transition sheets printed ratios and bone speeds on their headers; blind sheets must drop them.
- **Two independent judges,** not from the animation lane, score the eight categories 0–10 before they read any metric (SHARED_SYSTEMS_BAR §4): anticipation and follow-through, weight, transitions, hit reactions, deaths, walking and standing, crowds out of lockstep, legibility at the play camera. Each writes the five most concrete fixes when the bar is not met.
- **Beside commercial references** of the same genre and size, never beside our previous round.
- **Pass:** both ≥ 9 and no category under 8.5, in the built play host at the player's settings with no URL flags. The owner watches last, in the lab and in the game, before it spreads to other games.
- **Movement demo at 7** (MOTION_PLAN step 4): when both judges give 7 or more in every category, send the owner the demo. It is an MP4 at 1920×1080 and 60 fps plus a half-speed copy, the transition sheets and a metric summary, with two lists: what reached 7 (with before and after numbers), and what still blocks 8.5 (each judge's five fixes).
- **Three tries, then discuss:** after three reworks without a clear score gain, take the clips, the judges' notes and what was tried to ChatGPT, and agree on a different approach before trying again.
