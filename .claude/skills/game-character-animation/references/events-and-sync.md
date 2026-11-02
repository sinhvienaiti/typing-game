# Events and sync: one event, one frame

## 1. Who owns time

- **The sim owns gameplay.** It runs at a fixed 60 Hz, deterministic, with golden hashes. It decides damage, hits, deaths, stuns and knock-backs. Animation, VFX, sound and camera are views of its events.
- **Animation never delays the sim, and never moves a sim event.** A clip that is not ready is the clip's problem: it inertializes into the pose the event needs.
  - A typed strike: the wind-up follows the typing progress, and the last key releases the body within 50 ms.
  - A foe: the clip holds at `windup_end` until the sim's strike event, and never releases before it (CHARACTER_ANIMATION §5.5).
- **Clip markers drive view reactions only:** foot dust and footsteps on `foot_l` and `foot_r`, a whoosh on a swing, a thud on `fall_impact`, a camera nudge for a heavy body. They never start damage.

## 2. One event, every listener on the same frame

When a sim tick emits a release, a strike, a contact or a hit, these answer it in the frame that tick is drawn:
- the caster's body (the release clip and the acting);
- every VFX layer of that phase, with each burst written at age 0 so its first frame is fully bright;
- the sound of that phase;
- the camera kick or shake;
- the hit-stop.

No `setTimeout`, `setInterval` or promise delay schedules any of them: a timer started with the clip drifts from the body and the hit. Layer offsets (VFX layers 2–3 frames apart) are counted in frames from the event, on the same clock.

## 3. Order inside a frame

1. Sim steps for this frame.
2. Read their events into the view.
3. Update the animators (the release starts here).
4. Read the sockets.
5. Spawn the VFX from the sockets.
6. Start the sounds.
7. Kick the camera.
8. Render.

The Tu Tien lab does steps 3 to 5 in this order: keys and casts reach the VFX after the caster's update, so a shot leaves the hand as drawn (`games/immortality-cultivation/src/lab/skills-main.ts`).

## 4. Hit-stop

- Hit-stop scales world time for the view. It is counted to part frames, so a 30 ms stop is 30 ms at 60 or 120 Hz, and it eases back to full speed over 30 ms instead of snapping (`games/immortality-cultivation/src/lab/feel.ts` `HitStop`).
- **A new release cuts a stop still holding,** with no exit ramp: the player's input never waits on a stop. In the lab's stress run, a 50–83 ms stop held a release's body 100 ms after its last key, against a 50 ms gate.
- The kit's `BlowQueue` (`shared/game-kit/feedback/hitstop.ts`) works the other way: it may hold a finished word's blow while the world is stopped, up to `holdMaxMs` (70 ms in the kit's profiles). Where a game uses it, check the last key to body release with the probe.
- The animation clock reads the same scaled time as the VFX, so body and effects freeze and resume together.

## 5. Detecting clip markers

- **A marker fires when it lies between the clip time of the last frame and this one.** This stays right when the clip loops, changes rate, is scrubbed by the typing or jumps. Never compare against an exact time, and never use a timer started when the clip began.
- **Drift is at most 1 frame,** and the probe checks it.
- **Position comes from the nearest socket** (`FX_FOOT_L`, `FX_MOUTH`, `FX_WING_*`, `FX_TOOL`), read after the animator's update.
- **Crowds:** the CPU knows each instance's clip time, so crossing tests are cheap. Emit only for on-screen instances nearest the camera, capped per tier ([runtime layers](runtime-layers.md) §7: 2, 4, 6 or 8 sounding events per frame).
- **Event names** follow the clip contract (CHARACTER_ANIMATION §5.4, §5.8): `foot_*`, `wing_down`, `windup_end`, `release`, `recover`, `fall_impact`, plus a family's own (`breath_start`, `root_strike`).

## 6. What the probe checks

- **Markers:** the last key, the body release (the strike clip crossing its `release`), the VFX release (the first flash after the last key), and clip and state changes (`games/immortality-cultivation/src/lab/motion-probe.ts`).
- **Gates:** last key to body release ≤ 50 ms; clip event drift ≤ 1 frame. Run the scenario at 60 Hz and again at 120 Hz: an offset that changes with the frame rate comes from something tied to frames instead of time.
