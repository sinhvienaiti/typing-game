# Presence layer menu

Pick layers from this menu; nobody counts them. As a starting point, a character 60–100 px tall at the play camera carries three to five layers well. A close-up, menu or intro pose can carry more. The names P1–P10 avoid a clash with L1–L18 in VFX_STANDARD §3.2.

## 1. What every layer module declares

| Field | Meaning |
|---|---|
| anchor | A socket name from the model contract (`FX_HALO`, `FX_CORE`, `FX_CAST_L/R`, `FX_WING_*`, `FX_TAIL`, `FX_FOOT_L/R`, or game sockets such as `FX_BACK_CORE`, `FX_RING`, `FX_THRUST`), plus the written fallback when it is missing |
| bloom class | `core`: a thin HDR line or dot, 3–6, may bloom. `glow`: at most 0.9 a channel before tone mapping, never blooms |
| tiers | On or off per tier (Low, Medium, High, Ultra), with counts per tier |
| budget | Measured ms at the default tier, 1080p, dpr 1 |
| reduced | `keep`, `soften` or `drop` (§5) |
| states | How idle, ready, action, hit, low health, victory and defeat drive it (§3) |
| protected | The masks it stays out of: word strip, learning frame, enemy telegraphs, HUD |

## 2. The layers

| # | Layer | Technique | Bloom class | Cost driver |
|---|---|---|---|---|
| P1 | Rim glow | Fresnel added to the character's own material | glow | Pixels of the character only |
| P2 | Emissive channels | The model's emissive map, animated by a mask | core where thin, else glow | Pixels of the character only |
| P3 | Halo or light ring | Signed-distance ring on a quad, or a thin torus | thin core line plus glow falloff | Quad size on screen |
| P4 | Orbiting motes | One instanced mesh, orbit computed in the vertex shader | glow, tiny core on the largest | Sprite size on screen × count |
| P5 | Light ribbons and trails | Kit ribbons on sockets | thin core plus glow body | Ribbon length and width |
| P6 | Aura pulse or energy shell | Fresnel capsule or column at low opacity | glow | Shell area on screen (overdraw) |
| P7 | Ground glow | Decal disc or ring under the feet | glow | Decal area |
| P8 | Character light | One pooled point light | n/a | Every lit pixel nearby, crowds included |
| P9 | Core, eye or emblem | Small HDR dot over a darker backing | core | Tiny |
| P10 | Heat haze, distortion, light shafts | Screen-space passes | n/a | Full-screen pass |

### P1 Rim glow

- Patch the model's own `MeshStandardMaterial` with `onBeforeCompile`. Add the rim to `totalEmissiveRadiance` and set `customProgramCacheKey` so the variant compiles once. Keep the base, normal and roughness maps (`docs/games/MODEL_QUALITY.md`); an unlit replacement material makes the model flat.
- Clamp before the power: `pow(max(1.0 - dot(n, v), 0.0), power)`. Under MSAA an edge pixel shades outside its triangle, so the interpolated normal can pass ±1. In Dragonhold's crowd rim (29/10) `pow()` of that negative base gave NaN, and Ultra's bloom spread one NaN pixel into a black box over the field.
- Bias the rim toward a light direction (a key rim) instead of an even outline: it sculpts the form. Mask skin and face with a vertex or texture mask.
- At play camera the rim is what separates the character from the ground. Check it on bright and dark ground.
- For instanced crowds, use one shared material with the rim strength as an instance attribute, and give it to elites only.

### P2 Emissive channels

- Prefer the model's own emissive map. Animate it with a UV-scrolling mask or a world-space band driven by `uTime`.
- Lines thinner than about 1.5 px at the play camera shimmer or vanish. Widen them, or accept that they read only in close-ups and menus, and do not count on them in play.

### P3 Halo or light ring

- If the radiance-kit decision puts the ring in the model (an accessory mesh or part of the body), this layer adds only the light: an emissive mask on that mesh plus a soft falloff quad behind it. The points below still apply.
- Otherwise, draw a quad with a signed-distance ring in the fragment shader. Antialias it with `fwidth`, so it stays clean at 1–3 px. Compute the soft falloff in the shader, so it reads without bloom. Only the thin core line may be HDR.
- Orientation: turn the quad toward the camera around the body's up axis (axis billboard). Or, if the ring is seen in 3D, lock it in world space behind the head as a thin torus. A fully camera-facing halo drifts off the head when the camera tilts.
- Anchor it at `FX_HALO`. Use depth test on, depth write off, and render it after the body. Set `toneMapped: false` only on the HDR core. That flag matters only on tiers that draw straight to the screen; with a composer, the grade or output pass tone maps everything at the end.
- Keep the ring line at least 1.5 px wide at the play camera, or it aliases. Give any texture mipmaps.
- Rotate rune detail slowly (period of 6 s or more). Idle brightness is flat or breathing, never flickering.

### P4 Orbiting motes

- Use one `InstancedMesh` (or `Points`) per character with per-instance attributes: radius, phase, speed, tilt, size and seed. Compute the orbit in the vertex shader from `uTime` and the anchor's matrix uniform, so the CPU does nothing per mote per frame.
- Vary the motes: two or three tilted bands, mixed radii and speeds, a few large and many tiny, and a twinkle with a low duty cycle. Even circles of identical dots read as cheap.
- Keep depth test on so motes pass behind the body. They are additive and in the glow class; only the few largest get a tiny HDR centre.
- Start from 12–40 motes per hero at play size. Overdraw grows with sprite size on screen, not with count alone.
- Seed the randomness so captures repeat.

### P5 Light ribbons and trails

- Use the kit's `Ribbon`, `FlameTrail` and `LightTrail` (`shared/game-kit/three/particles.ts`) on sockets: wing tips, tail, hands, thruster. The kit `Hero` already finds trail sockets (`shared/game-kit/three/hero.ts`).
- A trail driven by motion dies when the character stands still. For idle, drive a drift ribbon from a procedural path around the socket (slow sine plus noise), so it flows without travel.
- Taper it, scroll the UVs and erode with noise. Keep a thin HDR core and a glow-class body; never the default white core.
- Capes and sashes on bones are character animation, not this layer.

### P6 Aura pulse or energy shell

- Use a fresnel capsule or cylinder around the body at low opacity, or a gradient column rising from the ground. Avoid an inflated copy of a skinned mesh: it doubles skinning and overdraw.
- Pulse on events (word complete, streak tier reached, ready) with ease-out. The idle breathing period is 2–4 s, with a small amplitude.
- The shell is the first layer to wash out a character. Check the silhouette with it on.

### P7 Ground glow

- Put a decal disc or ring under the feet: `polygonOffset` on flat ground, a terrain-hugging mesh on uneven ground. It grounds the character and stands in for a light on tiers without lights.
- It must not look like an area marker or an enemy telegraph: use a different shape language, never red, and a soft edge.

### P8 Character light

- Take one point light from the game's pool, created at load and left at intensity 0 when unused. The light count is part of the shader key, so adding or removing a light at runtime recompiles shaders.
- A light costs on every lit pixel near it, crowds included (VFX_STANDARD §3.7). Measure it before keeping it.

### P9 Core, eye or emblem

- Put a small HDR core over a darker backing at `FX_CORE`, a back core or an eye socket.
- When typed letters fly into this point (shared typing feedback), keep the idle core dimmer than the arrival flash. Re-run the typing measurements.

### P10 Heat haze, distortion, light shafts

Rarely worth it for presence. Use only on a tier where measurement allows, and drop it in reduced motion.

## 3. States

| State | Presence does | Note |
|---|---|---|
| Idle | Slow breathing; motes drift; ribbons drift | Nothing flickers; at most one bright accent every 2 s |
| Ready or charging | Grows with typing progress or streak tiers, in steps the player can read | Information: kept in reduced motion as a steady level |
| Action | Swells into the release phase of the combat effect, then settles in 150–300 ms | The release flash itself belongs to game-vfx-layered |
| Hit | One dip or flicker of at most 100 ms | Any tint is the attacker's colour (the impact carries its source's colour, VFX_STANDARD §3.6), never a new colour |
| Low health | Dims, desaturates, slows | No flashing alarm; the HUD carries the alarm |
| Victory | Crescendo: motes spiral in, the halo brightens | May pass the idle caps for a peak of at most 3 frames |
| Defeat | Lights go out in sequence | |

Ease state transitions over 150 ms or more, except hit and action.

## 4. Restraint

These are starting caps. The game's own doc wins once it has measured.

- **Hierarchy:** background < idle presence < ready < combat feedback < word tags and learning frame.
- **White-out:** with presence alone at the play camera, pixels with luma of 0.95 or more stay at or under 1 % of the field. The 6 % in VFX_STANDARD §3.6 is for combat peaks, and presence is on all the time.
- **Protected masks:** presence adds at most 10 % luminance inside the word strip, learning frame, enemy telegraphs and HUD. Near the word strip, cut additive presence by 60 %, the calm-mask rule of VFX_STANDARD §3.6.
- **Word-tag contrast:** at least 7:1 at p99 with presence on.
- **Silhouette:** edge contrast against the ground is higher with presence on than off, on light and on dark ground.
- **Colours:** nothing from the game's reserved signal set (enemy, elite, telegraph, loot, typing power). Write the reserved set into the brief.
- **Signals are not presence:** an aura that carries a rule (an elite marker, a leader's buff radius) stays in reduced motion and follows the game's rules. Our presence borrows neither its colour nor its shape.
- **No screen tint:** no full-screen tint, vignette or grade change for a character. That is the stage's job.
- **Flashes:** at most 2 per second across the screen (VFX_STANDARD §3.6).
- **No cover-up:** glow never covers for a weak model or texture.

## 5. Reduced motion

| Layer | Class | Reduced version |
|---|---|---|
| P1 rim | keep | Static strength, no pulse |
| P2 channels | soften | No scrolling; steady glow |
| P3 halo | keep | No rotation |
| P4 motes | soften | Speed × 0.3, no twinkle; dropped on Low |
| P5 ribbons | soften | Shorter, no flutter |
| P6 aura pulse | soften | Steady shell at the mean level |
| P7 ground glow | keep | Static |
| P8 light | soften | No flicker |
| P9 core | keep | Steady; arrival flash × 0.6 |
| P10 distortion | drop | |

The ready or streak level always stays, as a steady brightness, because it carries information.

## 6. Tiers

| Tier | Starting set |
|---|---|
| Low | P1, P3 (static), P7, P9; no bloom, no light |
| Medium | Adds P2 and a few P4 motes |
| High | Adds P5 and P6; P8 only if measured |
| Ultra | More motes, soft particles, P8. It must differ from High for real, not only be brighter |

Low must pass on its own. The soft falloffs live in the shaders, not in bloom.
