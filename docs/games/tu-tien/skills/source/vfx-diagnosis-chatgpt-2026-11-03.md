https://chatgpt.com/c/6ae90a5c-7d00-83ec-b620-e2cf41e2b534

ChatGPT said:
Executive diagnosis

Round 2 failed because it was still fundamentally the Round-1 visual language with more post-processing and more layers. The judges asked for anime/donghua art direction; the implementation translated that into more bloom, more blur, more tint, more objects, more screen treatment.

That distinction matters. HoYoverse describes Genshin's rendering target explicitly as the opposite of “dirty, noisy, dark”: fresh, bright, clean, anime-like, and says technologies that look impressive in isolation are rejected when they do not fit the art style. 
Docswell
+1
 HoYoverse made essentially the same point about Star Rail in 2026: artistic direction comes first; technology exists to deliver it, while character performance, camera and staging matter more than simply maximizing graphics. 
JPGames Community

So I would not do a Round 3 that consists of another parameter-tuning pass. I would treat Round 3 as a small VFX art-direction reboot.

One important caveat: Genshin, HSR and Wuthering Waves do not publicly publish exact sprite counts, luminance values or proprietary layer stacks for individual attacks. I will distinguish documented techniques from what can reasonably be inferred visually, and the numeric targets below are my recommended numbers for your camera, not claimed internal HoYoverse/Kuro settings.

1. Why Round 2 scored worse
The primary problem is value hierarchy, not insufficient spectacle

Your Round-2 stack has several operations all pushing pixels toward the middle:

environment dim/desaturation,
large translucent mint/cyan objects,
broad bloom,
full-screen flash that is not actually white,
radial blur,
chromatic separation,
semi-transparent ribbons/pools/glitter.

That creates large areas of similar middle luminance.

A convincing anime “white-hot” attack does almost the opposite:

tiny white core → saturated narrow color → darker clean surrounding field.

The eye reads the contrast, not the number of luminous pixels.

Riot's public VFX guidance is useful here even though League has a different aesthetic: primary elements are distinguished through stronger silhouette, value range, contrast, opacity and motion; secondary information is quieter. Their VFX hiring guidance boils the fundamentals down to shape, value, colour and timing, and explicitly says the gameplay information should be the primary read. 
Riot Games
+1

Your 320 swords, ribbons, glitter, pools, four hues, screen wash and numbers are effectively saying:

Everything is primary.

Therefore nothing is primary.

The “milky flash” is exactly what I would expect from the current recipe

A flash value of (0.42, 0.19, 0.05) is not a white impact frame. Depending on the space in which you apply it and how it interacts with tone mapping, bloom and desaturation, it is a broad colored exposure lift.

Then you blur that result radially and separate RGB by 12 pixels.

Instead of:

BLACK → WHITE → CYAN → normal image

you get:

scene → tinted haze → blurred tinted haze → RGB-fringed haze.

The judges' description of “fog/render bug” is technically consistent with that.

There is also a three.js pipeline check I would make before touching the art. UnrealBloomPass selects contribution using a luminance threshold, and Three.js expects tone mapping to participate in the pipeline. OutputPass performs tone mapping and color-space conversion and normally belongs at the end. 
Three.js
+2

For r170, verify:

RenderPass → HDR VFX → bloom → linear-space screen effects that need HDR → OutputPass → only passes explicitly requiring display/sRGB input.

Do not merely assume the custom flash/chromatic pass is operating in the color space you think it is.

Also inspect the actual HDR values entering bloom. With threshold 1, a sword shader that visually looks cyan but never substantially exceeds 1.0 linear luminance cannot produce the same concentrated blooming core as an HDR emissive value several times brighter.

I would start testing sword cores around 4–8 linear emissive, not because that is a reference-game number, but because you need enough HDR separation for a thresholded bloom pipeline. Tune after tone mapping.

Additive blending is being asked to do jobs it is bad at

Additive is excellent for:

tiny energy cores,
sparks,
hot particles,
thin glints,
narrow halos.

It is poor for:

the body of a sword,
smoke,
clouds,
large impact shapes,
broad slash silhouettes,
anything whose silhouette must remain readable.

Stack enough soft additive mint cards and you inevitably get pastel fog.

For your style I would make each important effect two systems:

Graphic body

opaque / alpha / premultiplied-alpha
defined silhouette
hand-authored texture
relatively little bloom.

Energy layer

additive
very narrow
HDR
supplies the glow.

A flying sword therefore isn't “a transparent glowing sword.”

It is:

dark/cyan silhouette + white spine + cyan emission fringe + directional streak.

That is a major conceptual change.

Procedural sprites are exposing their procedural nature

Procedural gradients, circles, noise puffs, rings and smooth ribbons are mathematically clean. Anime VFX are usually designed shapes.

Industrial Light & Magic ran into almost exactly this issue while developing Ultraman: Rising. Their artists found that impact-frame treatment could not simply be automated: sometimes it needed two frames, sometimes three or four, depending on the action. They also built stylized explosions from modular, art-directable pieces and layered streaks, smears and ink-like elements rather than relying on physically correct simulation alone. 
Animation World Network
+1

That is closer to what your game is missing than another shader.

Your current particles probably have technically good movement but weak drawn shapes.

Your scale is hostile to detailed 3D swords

At 30–70 px character height, a flying sword might occupy 20–50 px in length and perhaps 1–4 pixels in width.

At that scale:

decorative guard shapes alias together,
the ring becomes disproportionately recognizable,
material roughness barely matters,
subtle engravings do nothing,
translucent mint occupies more visual area than the metal body,
a long thin GLB becomes a “toothpick.”

So the full Clear Wind GLB is the wrong representation for most flying swords.

This is analogous to how film/game effects production changes fidelity with viewing distance: the farther something is, the more important its broad designed read becomes relative to microdetail.

You need screen-space VFX representations, not merely LOD geometry.

Timing also regressed

Anime impact does not mean “temporarily apply more post FX.”

It means discontinuity.

The filmmakers of Ultraman: Rising specifically describe changing or inverting the picture for only a couple frames; they also deliberately removed conventional motion blur and used graphic smears instead. 
Yahoo
+1

Your 80 ms radial blur is roughly five 60-Hz frames. That softens the exact moment that is supposed to become sharper and more violent.

The ideal rhythm is closer to:

anticipation → acceleration → violent 1–3-frame graphic interruption → hard return → aftermath.

Not:

acceleration → blur → blur → flash/fog → chromatic blur → slowly settle.

2. What the references are actually doing
A. Impact frames

This is the highest-leverage change in your whole game.

The documented anime-derived approach is remarkably literal: Ultraman: Rising used inversions, contrast changes and alternate shading for two, three or sometimes four individual frames, each art-directed to the specific action. 
Animation World Network

For Tu Tien Thu Ai at 60 fps, I would build this sequence:

Frame	Treatment
−3 to −2	motion accelerates; background darkens slightly
−1	weapon/strike reaches near-white; speed lines converge
0	black/navy silhouette frame + white/cyan graphic strike
+1	nearly white frame with cyan contour / black silhouettes
+2	normal image returns immediately; very bright core remains
+3–6	debris, streaks and reactions expand
+7 onward	smoke/dissipation begins

Not every hit needs both impact frames. Basic hits may use one; ultimates can use 2–3.

Remove the full-screen radial blur from Frame 0/+1.

If you use RGB split at all, make it approximately 0–2 px, localized to the strike or previous acceleration frame. Twelve pixels reads as lens/error processing rather than anime drawing.

Create 3–5 reusable authored full-screen impact textures:

radial black ink rays,
white wedge burst,
cyan-black inverted slash,
sword-shaped radial streak field,
cracked black brush burst.

Rotate/scale/mirror them procedurally.

That gives you variation without generating the art procedurally.

B. Sword qi and flying swords at 20–60 px

Do not try to make every sword beautiful as a miniature GLB.

Make every sword legible.

I would use three representations.

Lead swords

Only 4–6 at once.

Screen target:

length: roughly 35–70 px
graphic blade width: 4–7 px
central white core: 2–3 px
cyan halo: another 3–6 px each side during maximum emission.

They can use simplified 3D Clear Wind geometry when close enough, but overlay a camera-readable luminous spine.

Palette:

white → pale cyan → deep cyan/navy

with gold reserved for the heroine's 2–4 command swords or the finisher.

No mint, teal, cyan, jade and gold all competing simultaneously.

Mid swords

Approximately 16–32 meaningful sword silhouettes.

Do not render detailed hilts.

Use a simplified mesh or oriented billboard:

white tapered spine,
cyan body,
narrow dark edge,
one short motion streak.

At 15–30 px, the viewer needs to read:

尖 / point → blade → movement direction.

Not guard construction.

Distant swarm

These should stop pretending to be literal swords.

Use directional sword streaks, perhaps 40–100 visible depending on density and performance.

They support scale.

They are not primary objects.

That gives you:

6 heroes + 24 readable swords + 80 atmospheric streaks

instead of 320 equally unimportant objects.

Wuthering Waves' own technical interview is useful philosophically here: Kuro says it unified the presentation of the entire combat loop, using a unified material controller plus Niagara rather than treating every effect as an unrelated feature. 
Unreal Engine

Build one Sword-Qi material grammar and reuse it everywhere.

C. High-3/4 ultimates

The ground vortex fundamentally fights your camera.

With a 55° downward view, circular ground graphics:

become visually compressed,
look like decals,
resemble RPG telegraphs/HUDs,
cannot imply celestial scale.

Your judges are therefore right that “Sword Galaxy” needs to move into vertical space.

The composition I recommend:

Sky gate

upper/central portion of screen,
roughly 35–55% screen width at peak,
dark celestial aperture rather than bright opaque disc,
luminous perimeter and internal sword silhouettes.

Heaven-earth link

3–7 vertical columns / shafts,
broken volumetric-looking segments,
provide parallax across near/mid/far depth.

Sword rain

hits distributed across 70–90% of the visible battlefield,
near/mid/far waves,
directional perspective,
strong screen-space downward streaks.

Ground contact

localized impact crowns,
dust/shock rings,
swords physically remaining embedded.

Aftermath

8–16 visible pinned swords,
scorched/slashed terrain marks,
beasts launched or dissolved,
residual falling motes.

Genshin's rendering talk contains an especially relevant lesson. Their team found that some desired god-ray visuals were not satisfactorily achieved by simply leaning on volumetric fog, because low resolution and dense fog could become visually dirty; they kept more controllable treatments where the art required them. The broader pipeline was explicitly shaped around art requirements rather than physical correctness. 
Docswell
+1

Do the same.

Do not solve your heavenly portal by filling the screen with more transparent fog.

Use hard graphic structures plus restrained atmospheric depth.

A recommended ultimate rhythm:

0–150 ms: sound drop + sky darkening
150–350 ms: gate tears open
350–650 ms: first sparse giant swords
650–1050 ms: dense rain in 2–3 waves
~1050 ms: hero command gesture / finisher
impact: 2–3-frame graphic cut
next 300–500 ms: launches/pins/deaths
0.6–1.2 s: readable aftermath

Those are design recommendations, not reference-game internal timings.

D. Crowd hit reactions

The mistake is making reactions physically plausible and uniformly distributed.

At this camera, a 30 cm reaction can be just a few pixels.

You need reaction tiers.

For one large cast:

Hero victims: 4–8 beasts

one-frame white/cyan silhouette,
10–25 px screen displacement,
actual launch,
exaggerated rotation,
sword pin,
big ground ring,
premium dissolve.

Secondary victims

smaller synchronized hop/stagger,
shared rim flash,
cheap displacement,
simple dissolve.

Background victims

no elaborate animation,
flash → disappear/dissolve.

The player's eye only needs several spectacular “proof points” to believe that the whole crowd was devastated.

Also synchronize:

impact texture + SFX transient + camera impulse + victim pose change

on the exact same simulation frame.

Five individually good effects starting 30–60 ms apart will feel softer than four mediocre effects perfectly synchronized.

E. Damage numbers

I would stop using HSR as the target here.

HSR itself can display individual multi-hit values plus totals, and players have publicly complained about large damage-number presentations obscuring the battle. 
HoYoLAB

Your typing game has a stronger reason to suppress them because it already reserves screen space for words.

I recommend the hard invariant:

Never more than eight combat-number objects visible.

Prefer:

1 skill running total,
1–4 notable victim numbers,
1–2 crit/elite values,
optional status indicator.

All microhits aggregate.

Batch same-skill damage for approximately 100–150 ms before displaying it.

A sword rain doing 47 hits should therefore look like:

7,431 → 12,892 → 19,240 → 31,881

on the running headline, not 47 little floating numbers.

Also:

clamp labels at least 5% inside screen bounds,
no number may overlap the typing word,
fade old victim values immediately when the next batch arrives,
tiny damage under perhaps 10–15% of the skill's meaningful hit magnitude is total-only.
3. Yes—switch important VFX away from pure procedural sprites

But do not switch everything to flipbooks.

The correct answer is a hybrid.

Effect	Best representation
Smoke / dust / cloud bursts	Authored flipbook
Impact explosion body	Authored flipbook + mesh flash
Ink death wisps	Authored flipbook
Stylized debris cloud	Flipbook + a few real particles
Sword slash	Authored textured mesh/ribbon
Sword qi projectile	Mesh/ribbon + authored texture
Flying sword core	simplified geometry/billboard + shader
Sword trails	Procedural ribbon geometry with authored masks
Sky portal	Mesh layers + authored textures + shader motion
Shock ring	Mesh/decal with authored texture
Speed lines	Authored graphic texture, procedurally transformed
Sparks	Procedural
Spawn positions	Procedural
Sword trajectories	Procedural
Target reservation	Procedural
Reaction selection	Procedural
Dissolve threshold	Procedural shader
Camera / hit-stop / timing	Procedural/control code
Number aggregation	Code

This is much closer to professional stylized-effects practice: the computer handles motion, variation and orchestration while artists control the important shapes.

Riot explicitly describes its own effects as generally hand-drawn/painterly. 
Riot Games
 And ILM's stylized-effects work similarly combined procedural tools with manually controllable modular shapes rather than expecting simulation alone to deliver the desired illustration. 
Post Magazine
+1

Firefly Video is genuinely useful here

Adobe now supports transparent-background Firefly Video generation. It defaults to 24 fps / 5 seconds, and exported transparent generations contain separate foreground and alpha video data. 
Adobe Help Center

But I would not ship the raw AI video.

Use it as raw VFX photography:

Generate one isolated explosion/cloud/ink burst.
Select the best 8–20 frames.
Remove unstable frames.
Threshold/posterize values.
Repaint/clean important silhouettes.
Force your cyan/white/black palette.
Produce a clean flipbook.
Test on black, white and actual gameplay backgrounds.

A 16-frame 4×4 atlas with 256×256 cells gives you a 1024² texture and is enough for many impacts.

For dust/smoke, the free Unity Labs sequences are explicitly CC0 and were created as raw image sequences or assembled flipbooks. 
Unity
 JangaFX's free EmberGen VDB simulations are also explicitly CC0 and include explosions, smoke, shock waves and clouds. 
JangaFX

I would use:

Unity/JangaFX → physical movement reference/base → stylize heavily.

Not photoreal smoke pasted unchanged into a donghua game.

4. Round-3 plan

The order matters much more than adding another 20 effects.

Priority	Change	Acceptance gate before moving on
P0	Fix/verify HDR + post chain	OutputPass placement verified; screenshot before/after tone mapping available; no unexplained mid-grey wash
P1	Create 3 static “golden frames” before coding	Basic, sword-rain and ultimate climax must each look ≥8/10 as still images at actual gameplay camera
P2	Replace climax treatment	1–3 graphic frames; zero 80ms climax radial blur; chroma ≤2 px or off
P3	Rebuild sword visual grammar	only white/cyan + hero gold; 4–6 leads; leads ≥35 px long; white spine ≥2 px
P4	Rebuild Sword Galaxy vertically	sky event + columns + rain across ≥70% of visible field
P5	Replace hero impacts/smoke with authored assets	no default soft-circle/noise puff visible in hero effects
P6	Exaggerate selected victim reactions	4–8 premium victims visibly launch/pin; reaction visible at 25% screenshot scale
P7	Hard-cap damage UI	≤8 number objects under every automated stress test
P8	Rebuild basic attack	release burst + visible projectile body + trail + target-centred authored hit
P9	Redo cut-in composition	action pose + weapon + active VFX; title/seal rectangles have zero overlap
P10	Performance gate	≤11.5 ms p95 at 1080p High on M4, leaving ~0.5 ms safety below your 12 ms target
Add measurable image-quality gates

For every major skill, capture the climax and inspect it in grayscale.

I would require:

Primary value separation

white core vs adjacent background: luminance difference roughly ≥0.4
halo clearly subordinate to core,
black/dark shapes still exist during the climax.

No haze

no large uniform middle-grey overlay,
the whole frame must not become one value band.

Palette

one principal hue,
one supporting hue,
gold accent limited to roughly ≤10% of luminous-effect area.

For Sword school that means effectively:

white + cyan + tiny hero-gold.

Screen-space coverage

For the ultimate:

portal: ~35–55% frame width,
rain footprint: ≥70% of battlefield area,
at least 3 obvious depth zones,
at least 12 simultaneously recognizable downward trajectories during peak,
aftermath remains visible for 0.6–1.2 s.

The effect should still look huge in a 1280×720 screenshot reduced to 640×360.

That is an important test for your camera.

Sword readability gate

Turn bloom completely off.

If the flying swords disappear without bloom, they are badly designed.

A lead sword should still read from:

silhouette,
hard central spine,
taper,
motion direction.

Then turn bloom back on as enhancement.

Bloom must never be the object.

The single biggest process change I recommend

Before programmers build Round 3, make six Photoshop-style target frames:

Basic release.
Basic impact.
Sword rain anticipation.
Sword rain peak.
Ultimate impact frame.
Ultimate aftermath.

Paint them without caring whether the engine can currently reproduce them.

That becomes the contract.

Then ask:

“What combination of mesh, flipbook, shader and camera reproduces this image?”

instead of:

“What other procedural feature can we add?”

This mirrors the production philosophy visible in both HoYoverse's art-first statements and high-end stylized film pipelines: technology is solving toward an authored target, not generating the target by accumulation. 
JPGames Community
+1

What I would delete immediately

From Round 2 I would remove the 12 px full-screen chromatic fringe, 80 ms climax radial blur, broad green-grey flash, four-hue sword palette, hundreds of literal tiny sword models, ground-dial-as-main-ultimate, and >8 simultaneous damage labels.

None needs tuning.

They are taking you in the wrong visual direction.

Keep the good engineering underneath: instancing, reservation targeting, trajectories, camera trauma, hit-stop infrastructure, damage aggregation, dissolve shader, performance tiers and the cut-in system itself.

Replace the art payload carried by those systems.

Expected score

If you do another procedural polish/tuning round on the existing assets, I would expect roughly 5.5–6.5. The two rounds have already shown that the approach has plateaued.

If Round 3 genuinely changes to:

authored impact shapes + hard value hierarchy + fewer/larger swords + vertical ultimate composition + exaggerated selected reactions + ≤8 numbers + action cut-in, I would expect approximately 7.8–8.4, with ~8.1 as my realistic central estimate.

I would not promise 8.5 in this single pass. An 8.5 blind score is plausible, but once the structural problems are gone, the remaining gap will probably be asset craftsmanship—exact sword silhouettes, flipbook quality, cut-in art, timing and sound—not another shader feature.

The encouraging part is that your current 8.6–11 ms frame time does not require more GPU spectacle. Most of my recommendations actually reduce simultaneous geometry and full-screen processing. You can spend the saved budget on better pixels rather than more pixels.

ChatGPT can make mistakes. Check important info.
Latest response




Thinking effort
High