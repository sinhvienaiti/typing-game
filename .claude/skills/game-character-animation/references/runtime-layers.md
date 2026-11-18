# Runtime layers: order, springs and budgets

Numbers below come from the Tu Tien lab (`games/immortality-cultivation/src/lab/anim/`, tuned on Lam, a borrowed Tripo hero with 0.37 m legs) and from `docs/games/CHARACTER_ANIMATION.md` §5. They are starting values for a new character: tune them on its frame sheets and record the result in that game's doc.

## 1. Frame order (`animator.ts` `update`)

1. **Locomotion:** way-points, speed springs, the yaw follower (`locomotion.ts`).
2. **Acting:** its timeline drives the strike's clip section and may offset the shown root (a lunge, a step back). The logical position the sim and skill code read never moves (`acting.ts`).
3. **State:** charge, strike, dash, fidget or locomotion picks the base clip, its time and rate.
4. **Pose:** sample the base clip, or two gaits blended by nlerp, into flat arrays, with no mixer.
5. **Inertialization:** on a requested transition, store the per-bone offset and decay it (`inertial.ts`); then write the bones.
6. **Hit additive:** the Hit clip on upper-body bones only, at weight 0.3 (in 0.03 s, out 0.25 s).
7. **Root:** position, glide lift and yaw (Lam faces −z, so yaw + π: the profile records the front axis).
8. **Record the clip feet** before any layer moves them; these are the foot-lock targets.
9. **World layers** (`layers.ts`): lean into turns and starts, the acting's body pose (crouch with a hip hinge, twist, lean, side lean), recoil, breathing, look-at. Rotations are applied in world space, so the rig's local axes do not matter.
10. **Arm aims:** acting arm directions in the character frame, then a limit on held arm poses.
11. **Foot IK** (`foot-ik.ts`).
12. **Spring chains** (`springs.ts`).
13. **VFX read the sockets** (`FX_HAND_R`) after this, so a shot leaves the hand as drawn.

## 2. Transition half-lives (`HALFLIFE` in `animator.ts`)

| Transition | Half-life (s) |
|---|---|
| Into release | 0.04 |
| Into charge | 0.06 |
| To Idle | 0.09 |
| Skill end to Idle (about 0.22 s to 95 %) | 0.065 |
| Dash in / out | 0.04 / 0.08 |
| Hit | 0.03 |
| Idle to move / move to Idle / gait switch | 0.10 / 0.12 / 0.12 |
| Fidget | 0.15 |

- A transition samples the new pose one frame earlier too, so its velocity carries over. The largest remaining offset and its bone are exposed for checks.
- Yaw: a critically damped spring, half-life 0.06 s moving and 0.14 s turning in place. Its goal follows at limited speed and acceleration, and its per-frame turn is capped at 355°/s.
- Look-at: yaw and pitch springs at 0.09 s, split head 0.6, neck 0.4, spine_03 0.2; clamped at 20° (15° on the spine), because past about 25° Lam's hood rim stretches.
- Lean springs 0.12 s; breathing at 0.25 Hz with its weight on a 0.4 s spring; recoil an underdamped spring at 5 Hz, ζ 0.6.
- All springs are exact critically damped (or underdamped where the overshoot is the point) updates written by half-life (`math.ts`), so they are frame-rate independent and stay continuous when the goal jumps.

## 3. Strikes and acting

- **Charge:** clip time springs (half-life 0.1 s) to progress × (release − lead).
- **Release:** the strike runs on from release − lead at ×1.2 swing speed. The lead is 45 ms of swing, so the body reaches `release` within 50 ms of the last key; the lab measures 33 ms. A design brief allowed ×1.2–1.5; ×1.2 kept the swing within 1.5 × the clip's peak once the release inertialization adds its own speed.
- **After the swing:** the pose holds at a near-still rate (×0.05) through the acting's hold and settle. The strike hands over to Idle 0.1 s before the clip ends.
- **Release time from the clip:** at load, the hand speed at 60 Hz (smoothed over 5 frames, since 24 fps keys leave a saw-tooth) gives the striking hand, the wind-up end and the swing end around the authored `release`.
- **Acting phases** (`acting.ts`):
  - anticipation with the typing: the centre of mass drops 4–6 cm, the sword arm draws back, the torso counter-twists 10–15°;
  - a release that reaches about 85 % in 6 frames and all of it in about 8;
  - a hold of 18 frames, longer where the skill's own later strikes land, with a pulse on each beat;
  - an overshoot and settle over about 0.3 s, then a 0.5 s recovery while the clip cross-fades to Idle.
- **Hit stagger:** directional (torso 18°, head 25°, about 0.3 s) with a 0.15 m step back on the shown root, the Hit clip underneath at 0.3.
- Arm directions spring along great circles, so an arm swung from behind to the front keeps an even angular speed.

## 4. Locomotion

- Forward gaits (walk, jog, run) blend in log speed within a ×1.25 band round the geometric mean of two neighbours' speeds.
- Stride matching: cycles per second = speed ÷ stride, both measured from the clip at load (`gait.ts`).
- In-place clips are stabilized at load: a small pelvis surge makes the planted foot move back at one constant speed, so foot lock can hold it.
- Side and back steps are picked by their measured ground direction, not their names (Mesh2Motion's `Strafe_left` steps to the character's right).
- Turn in place past 60° with the feet stepping; idle fidgets every 4–9 s at random; a stop sways on and settles.

## 5. Foot lock (`foot-ik.ts`)

- A foot locks when its clip ankle or ball comes within 4.5 cm of its Idle height while the clip is not swinging it, and unlocks past 6 cm. Moving, a foot going forward faster than 1.6 × the body counts as swinging.
- The lock pivots on the ankle while the heel is down, on the ball after toe-off.
- Moving, a lock more than 18 cm off the clip foot lets go and fades on a spring (half-life 0.07 s) that starts at the foot's own speed.
- Standing, a foot that drifts 10 cm or twists past 35° steps (0.3 s, one foot at a time).
- Soft IK: the reach eases out past 97 % of the leg, and the pelvis lowers up to 4 cm so the knees bend instead of locking straight. A lock the leg cannot hold lets go. No foot is solved under the ground.
- The knee's bend axis comes from the clip's knee, blended to the facing as the leg straightens, so the knee never flips.

## 6. Springs (`springs.ts`)

- Fixed 60 Hz steps (at most 4 per frame), each joint drawn between its last two steps.
- Tips live in the character root's frame, so a dash or a turn does not whip the chain; a share (`trail`) of the root's own motion still trails them.
- Per joint: frequency, damping ratio, gravity, trail share, a cone limit and a turn-rate limit round the animated direction; sphere and capsule colliders on pelvis and thighs.
- Lab settings: tail 2.4 Hz at the base to 1.4 Hz at the tip, ζ 0.55, cone 22–32°, 360°/s; ears 4 Hz, ζ 0.7; bag 2.2 Hz, ζ 0.5. The trail boost rises to 2.5 during a dash and eases back after landing.

## 7. Tiers and budgets (CHARACTER_ANIMATION §5.1, §5.9)

- **H, main characters:** CPU skinning with every layer above.
- **C, skinned crowds:** bone textures baked per model, skinning in the instanced shader, with the CPU choosing clip and time; transitions blend a frozen old clip in the shader.
- **R, rigid swarms:** per-instance matrices plus shader deformation.

Starting caps per tier (Low / Medium / High / Ultra), measured at 1920×1080 on the heaviest scene of the game:

| Item | Low | Medium | High | Ultra |
|---|---|---|---|---|
| H characters updated per frame | 0 | 6 | 8 | 12 |
| Spring joints | 0 | 16 | 48 | 96 |
| Foot IK | off | off | H | H |
| C skinned on screen | 0 | 220 | 320 | 400 |
| Sounding events per frame | 2 | 4 | 6 | 8 |
| Animation CPU p95 (ms) | ≤ 0.2 | ≤ 0.5 | ≤ 0.8 | ≤ 1.2 |
| Extra GPU over rigid bodies (ms) | — | ≤ 0.4 | ≤ 0.6 | ≤ 0.9 |

Measure the animation CPU time on its own (p95) through `.local/bin/heavy.sh --perf`, and keep the game's own measured headroom as the real gate.
