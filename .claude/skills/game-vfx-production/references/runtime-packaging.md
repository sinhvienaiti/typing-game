# Runtime packaging: the hybrid rule (video, flipbook, strip, particles, model)

**Owner, 06/11/2026:** "đồng ý về cách lai, tôi nghĩ nên thêm nó vào skill để xử lý sau này". The analysis behind it, with measurements and sources, is `docs/games/tu-tien/skills/SKILL_TECH_OVERVIEW_2026-11-06.md`.

**Status: direction under test, not final.** A few minutes later he added: "tôi cần xem demo trước khi chốt chắc chắn 1 trong 2 cách". Build the A/B demo (today's video path against the hybrid path, same seed and clock, side by side) and send it to him. Until he picks, do not convert existing video layers. New work may follow the table below where it changes nothing he has already approved.

The look still comes from Firefly, Blender or painted art (this skill's main rule). Packaging only decides **how that art plays at runtime**. Pick it per layer, not per skill: one skill usually mixes several rows below.

## Pick the packaging

| Layer | Packaging | Use for | Never for |
|---|---|---|---|
| A large moment, shown once, filling the screen | **Video texture** (the Firefly clip itself, additive on black) | Element ultimates, avatar and spirit-beast hero moments, cut-in material | Anything repeated, many at once, or aimed |
| A small effect repeated many times at once | **Flipbook atlas** cut from the Firefly clip, each instance on its own phase | Meteor bodies, impacts, hit afflictions, bursts, lotus blooms, scorch, orbs, rings | Full-screen hero moments (too blurry at the cell sizes that fit) |
| A shape that follows a direction or a length | **Strip or decal mesh** carrying a painted or Firefly texture; the shader only scrolls, erodes and tints | Crescents and melee slashes (plane of the swing), channel beams, trails, ground sigils, cracks, rifts | Shapes the shader would have to draw itself |
| Sparkle, embers, motes, rays | **Particles** from painted sprites, in the instanced pools | The radiance layer of every phase | Analytic stars or round code dots |
| A solid object seen close | **3D model** with clips | Real swords, the Song Long dragons when they are solid | Skill creatures that should read as energy (use strips and flipbooks) |
| Placement, timing, shake, numbers, erosion | **Code** | Everywhere | The shape or texture of anything |

## Settings

**Video**
- At most 3 playing at once (the lab's `MAX_VIDEOS = 3`). Load only the equipped skills' clips, ahead of the fight.
- Encode for size once the owner has picked a level from a side-by-side test (1080p CRF 18 today; CRF 23 or 720p are the candidates).
- No alpha: additive on black. Dark smoke needs its own white-on-black clip used as a darkening layer.
- Every instance of one video shows the same frame. That is why repeated things are flipbooks.
- Keep the stall fallback (an atlas takes over when the video does not start within 1.5 s).

**Flipbook**
- Size the cell to what the player sees: about 38 px per metre at 1080p on the play camera. The cell should be at least the on-screen size, capped at 768 px.
- 12–24 fps. At low fps use **motion-vector blending** between frames, not a cross-fade (cross-fades ghost).
- Give each instance its own start frame, so a salvo never looks stamped from one mould.
- Load atlases on first need and pre-warm the equipped set. Uncompressed PNG atlases cost about 39 MB of GPU memory each at 2560×2880 with mipmaps.
- Use **KTX2** once the tool exports it: UASTC for detailed art, ETC1S for soft smoke. Every compressed set is compared with the source video before it replaces anything.

**Strip, decal and particles**
- The texture is painted (Codex, Firefly Image) or cut from a Firefly clip. Channel-pack masks where one texture serves several layers.
- A shader may scroll, erode, tint, fade and add thin analytic rings or lines. Nothing more.

## Budgets (start values; measure per game)
- Videos at once: ≤ 3.
- First use of any skill: no visible hitch. Pre-warm what is equipped; a first-use hitch of 0.45–0.7 s was measured when a 4th skill fell back to an unloaded atlas.
- Frame time: 2–3 videos cost 5.3–6.5 ms a frame on the Mac mini M4 (Chrome). Re-measure on a weaker machine and in Safari before shipping.
- Texture memory: defer loading. The lab once reached 9.8 GB in Chrome from atlases it loaded but never used.

## Checks before a repackaged layer replaces the old one
1. The source clip and the new packaging play side by side in the lab, at the play camera, light and dark ground.
2. Send the owner the comparison video. He picks the level of sharpness.
3. Measure the frame time, GPU memory and first-use hitch, and write them in the changelog.
