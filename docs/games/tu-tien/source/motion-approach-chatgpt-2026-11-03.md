https://chatgpt.com/c/6ae8fb24-93f4-83ec-bb68-9b486683fc2e

ChatGPT said:

Your procedural system is not fundamentally wrong. The problem is that it is currently being asked to invent acting from unsuitable source motion and an unsuitable silhouette. A fourth round of amplitude/turn-rate/spring tuning on the hooded stand-in is unlikely to move the judges much.

The better architecture is:

authored camera-readable key poses → input-driven pose progression → immediate release event → procedural responsiveness/IK/secondary motion → VFX that reinforces the authored motion.

That is much closer to how strong shipped games solve this problem.

1. What shipped games are actually doing

There are fewer published numeric rules than you might expect. Studios discuss silhouette, anticipation, timing and VFX hierarchy much more often than “extend the arm 32°.” Where I give exact pose numbers later, I will mark them as our lab targets, not pretend they came from Genshin or Hades.

Game / source	What is relevant to your problem	Lesson for Tu Tien Thu Ai
Hades	Supergiant built characters as 3D animations rendered into 2D sprites. They give one remarkable example: the standard bow attack is a 104-frame animation rendered from 32 angles = 3,328 rendered frames for one attack. They explicitly pursued the crisp responsiveness of 2D despite producing enormous quantities of character frames. Later patch notes also mention revising combat VFX specifically to make frenetic fights easier to parse. 
Steam Community
+2
	They did not try to make one generic animation mathematically work from every angle. They spent content on camera/direction-specific authored reads.
Diablo IV	Blizzard says character design, shapes and detail are made “in service to our isometric point of view”; assets are repeatedly evaluated from the gameplay camera. They deliberately use larger shapes and simplify detail that harms readability. Their VFX team describes a hierarchy where visually loud effects are reserved for powerful skills, and attack “payloads” are animated/synchronized to weapon and VFX motion. 
Blizzard News
+1
	Judge the pose at 50 px, not in Blender close-up. Weapon path, target area and effect must agree.
Path of Exile	GGG explicitly changed melee attacks so the initial wind-up is slower and the strike itself faster. They also changed trails/effects so attack range was accurately communicated. 
Path of Exile
	Your typing phase should be readable, progressively loaded anticipation; the final key should unleash a disproportionately fast release.
Genshin Impact	HoYoverse has described using optical mocap for natural movement, then manually adjusting combat movement, including individual bones and clothing, because fantastical combat cannot simply be captured physically. They emphasize adding exaggeration and keeping important poses visually strong. 
Genshin Impact
	Mocap/video-to-motion is a starting point, not your final casting animation. Hand-authored exaggeration still wins.
League of Legends	Riot calls silhouette the single most important factor in champion recognition. In Lee Sin's update, Riot specifically replaced vague, floaty “two-pose” attacks with stronger timing and spacing that highlight important poses. Riot's animation teaching similarly emphasizes that animation quality begins with the strength of individual poses. 
League of Legends
+2
	This is extremely close to your actual failure. You do not have a transition-quality problem; you have a pose-design problem.
Lost Ark	A developer interview describes combat impact as a combination of effects, speed and animation, including a very brief pause on weapon contact to increase visceral impact. 
GameGrin
	Impact can momentarily interrupt motion, but only after your immediate typing release. Never let hit-stop compromise the 50 ms input contract.

Tale of Immortal is actually less useful as your benchmark. Interviews around its development describe a small-team, cost-constrained production with substantial reliance on purchased effects and limited character animation directions. That proves xianxia combat can survive on strong VFX, but it is not the route to your 9/10 against Genshin / Star Rail / Wuthering Waves target. 
智象出海

The Hades screenshots also illustrate the scale relationship that matters: the directional attack shape often occupies several times the screen area of the tiny character, while the character pose still establishes where the action originated.

2. Your procedural layer is doing the wrong job

I would keep most of the technology you wrote.

I would stop letting it be the primary animator.

Your inertialization, IK, springs, motion probe, typing-progress parameter and procedural hit/aim offsets are valuable. But none of those systems can manufacture a great silhouette if the underlying key poses put both hands behind a hood at the actual camera.

The new division of responsibility should be:

Layer	Responsibility
Authored animation	Heroic silhouette, stance, arm placement, sword path, torso shape, hip level, anticipation, release pose, overshoot
Typing procedural layer	Move progressively through authored anticipation poses as letters arrive
Immediate gameplay layer	Spawn projectile / activate hitbox / sword formation on final correct key
Additive procedural	Aim adjustment, subtle continuing coil, hit direction, small recoil variation
IK	Preserve convincing foot contact after authored motion
Secondary	Robes, hair, ribbons, scabbard, accessories
VFX	Make direction, reach, velocity and impact unmistakable

There is also an important timing point in your current setup.

At 24 fps, one source-animation frame is about 41.7 ms. Your complete release budget is 50 ms.

That does not mean a 24 fps clip is unusable—three.js can interpolate continuously—but it means the gameplay release absolutely should not wait for a clip marker or the next meaningful source pose.

The heroine should already be fully loaded into a release-ready pose before the last character is typed. On the final key:

frame N: input accepted, gameplay skill fires immediately.
frame N or N+1: sword/VFX begins.
next ~50–100 ms: body traverses the authored release stroke.
afterward: overshoot → settle/recovery.

The animation is visually catching up to an action that the player's typing already caused.

That is exactly the responsiveness structure you want.

3. Pose rules I would use at your camera

These are proposed Tu Tien Thu Ai production targets, informed by the shipped-game principles above and by your judges' feedback. They are not published Genshin/Diablo measurements.

Property	Lab target
Key-pose silhouette width	1.5–2.0× idle width for important casts
Weapon/outer hand separation	Roughly 0.20–0.35 character heights outside the torso silhouette
At 30 px hero height	Aim for roughly 6–10 px clear exterior separation
At 50 px	Roughly 10–18 px
At 70 px	Roughly 14–24 px
Hip drop for powerful anticipation	Start at your judges' requested 20–25%
Progressive typing coil	25–35° total, accumulated over the word
Living hold motion	About 2–4° shoulder/torso circulation or 2–4 screen pixels of meaningful hand/sword motion
Head lead	Head/upper shoulder intent about 2–4 60-Hz frames before the torso catches up; exaggerate head relative to torso by ~10–20° when anatomically plausible
Main release	Visually explosive 50–100 ms
Smear accent	1–2 rendered frames
Bright sword trail	Start testing around 80–150 ms persistence
Ground directional mark	150–400 ms, skill dependent
Recovery	Usually 120–250 ms before returning toward locomotion, except deliberately heavy skills

The crucial variable is screen-space negative space.

At your rear 55° camera, do not pose arms “correctly” in anatomical space if that puts the forearm over the torso. Cheat them sideways or upward until there is visible sky/ground between ribs, elbow, forearm and sword.

At 50 px, nobody evaluates anatomical purity. They perceive:

wide / narrow
high / low
left / right
open / closed
coiled / released.

That is why your judges asking for 1.5–2× bigger poses is probably directionally correct.

Your existing “increase amplitude to 1.3×” did not solve this because multiplying a bad pose by 1.3 still leaves the important joints travelling along bad screen-space directions.

The hold should never actually hold

Your typing mechanic gives you something ordinary action games do not have: the player is literally feeding anticipation over time.

Use that.

If a word contains eight letters, do not interpolate from pose A to pose B and then sit there. Make it something like:

0–20%: shoulders open, weapon clears silhouette
20–55%: hips sink, torso coils
55–80%: sword/hand rises farther outside silhouette
80–100%: additional 10–15° compression and directional intention
100% / final key: instantaneous gameplay release

Each additional letter should visibly increase potential energy.

Once near maximum compression, stop sinking further and use a circulating hold: tiny shoulder rotation, hand describing a small arc, robe tension, sword vibration/qi gathering. The pose looks alive without destroying readiness.

4. Which production approach wins?
Approach	What I would do
A. More procedural tuning on hooded stand-in	Stop. Keep it as an engineering regression test only. Its hood, ears, tail, short proportions and arm occlusion are actively teaching you the wrong silhouette.
B. Authored 60-Hz key-pose clips	Primary solution. This should become the base of signature casting. “60 fps” does not mean hand-key every frame; make excellent key poses and let curves/interpolation produce the intermediate frames.
C. Quaternius / Mesh2Motion	Excellent for locomotion, generic reactions, dodges, basic locomotor transitions and starting body mechanics. Do not expect a generic library to supply your signature immortal-sword casting language.
D. DeepMotion / Rokoko / Move One	Useful for reference and first-pass mechanics. Then exaggerate manually, as Genshin does with captured motion. I would not use video mocap as final cast animation untouched.
E. Build the heroine	Required before final scoring, but don't block tonight's experiment on production modeling. First make a human-proportioned proxy with approximate sleeves/robe mass. Once the pose language passes, build/rig the real heroine before producing the whole cast library.

The commercial-use situation also matters. I checked the current pages/terms on November 3, 2026.

Cascadeur: the Free tier prohibits commercial use. Indie supports commercial work subject to its sub-$100k annual revenue/funding eligibility; Pro removes that Indie business restriction. So use Indie if you qualify or Pro otherwise—not Free for this project. 
Cascadeur
+2

Quaternius UAL / UAL2: both pack pages explicitly identify the animation assets as CC0. Quaternius introduced a newer general asset licence in August 2026, but its licence page says changes apply to future releases rather than retroactively changing previously released assets. Keep a copy of the asset page/licence in your provenance folder. 
Quaternius
+2

Mesh2Motion: its project/assets are explicitly positioned for free personal and commercial use, with CC0 animation content and MIT code. 
Mesh2Motion

DeepMotion: Freemium output is non-commercial; paid-plan output receives a commercial-use licence suitable for integration into games/software, subject to their redistribution restrictions. 
DeepMotion
+1

Rokoko: its current Create/Vision material states generated motion clips may be used commercially under its terms; FBX export is supported, while some higher-end export options such as 60 fps depend on paid functionality. 
Rokoko
+1

Move One: its EULA grants a broad royalty-free, transferable/sublicensable licence to generated Output, but Move AI retains ownership language around Motion Data/Output. That is less clean to me than the DeepMotion/Rokoko formulation for a production asset pipeline; I would get explicit written confirmation for your intended shipped-game use before standardizing on it. 
Move AI
+2

For your project, I would rank the actual production choices:

Cascadeur/Blender authored animation > mocap-assisted authored animation > library-retargeted signature casts > procedural invention.

5. How much should VFX carry?

Not 0%. Not 100%.

I would use this design rule:

The body communicates verb + direction + phase.
VFX communicates trajectory + range + power + impact.

A body-only grayscale/silhouette recording should let a tester distinguish:

“charging”
“released”
“recovering”
and approximately where the attack is going.

It does not need to communicate “this is Heavenly Myriad Sword Formation rank III.” That is where VFX takes over.

As an internal production budget—not an industry statistic—I would target roughly 60–70% of basic semantic readability from body/weapon and 30–40% from VFX for ordinary skills.

An ultimate can be overwhelmingly VFX-heavy visually, but the starting pose should still clearly communicate its intent.

For your sword cultivator specifically, the best VFX readability devices are not random particles. They are geometry that extends the body:

hand → sword-light line → target
sword swing → matching arc
thrust → narrow directional streak
formation summon → expanding radial ground/screen-space arrangement
dash → one-frame character afterimage plus persistent travel line

Blizzard's “payload” philosophy is particularly relevant: the damaging region and the visible motion should agree rather than using spectacular effects that tell a different spatial story. 
Blizzard News

And keep bloom away from the exact regions you need to read. At 50 px, blowing out the hand, forearm and sword root destroys the pose you just paid to author.

6. Three-step recovery plan

Tonight: perform one body-only silhouette experiment, not another system-wide tuning round. Replace the hooded creature with any correctly proportioned humanoid proxy carrying a sword; give it crude robe/sleeve volumes so limb occlusion roughly resembles the future heroine. Pick one representative skill—I would use your fan-of-blades sweep because it requires both casting authority and directional release. Author only six strong poses: neutral/readiness → early anticipation → mid coil → maximum coil → release → overshoot/recovery. Do it directly in Blender or even through your existing runtime bone-pose format; there is no reason to install an elaborate mocap pipeline tonight. Drive the first four poses with typing progress and fire the gameplay event independently on the final key. Disable almost all procedural acting for this test; retain IK and perhaps tiny living-hold motion. Record the exact play camera at 30, 50 and 70 px, with plain materials and zero VFX. Measure key-to-effect ≤50 ms hard maximum and preferably same/next rendered frame; maximum silhouette width ≥1.5× idle; hips down ~20–25%; 25–35° progressive coil; weapon/hand clearly exterior to torso; no visually static interval longer than roughly 100 ms during continued typing. Then show randomized 50 px clips/stills to blind viewers and ask only “charging/releasing/recovering?” and “which direction?” I would require ≥80% correct phase identification and ≥90% direction identification without VFX. If this passes, I expect the single-skill judge impression to move from the current ~5.5 territory into roughly 6.5–7.2 immediately. If it does not, stop animation tuning and investigate camera/proportions/silhouette first.

Build the real animation foundation around the heroine. Once the proxy experiment proves the visual grammar, get the real heroine into 3D—or at minimum a near-final proportion/robe proxy—before authoring the full library. Make perhaps 6–8 signature casting families, each with deliberate camera-space anticipation/release poses. Use Blender or commercial Cascadeur. Quaternius/Mesh2Motion can fill locomotion, generic recovery/hits and reference material; DeepMotion/Rokoko can provide human mechanics where helpful. Your procedural layer now becomes the glue: letter-by-letter coil progression, aim/yaw offsets, slight pose exaggeration by camera distance, directional hit overlay, IK and secondary motion. Do not globally multiply every joint by 1.3×; create a screen-space exaggeration policy that mainly pushes hands, elbows, sword and shoulder line out of occlusion. At this stage I would target 7.5–8.3 blind-judge territory if the heroine silhouette and authored poses are strong.

Only then add the combat presentation layer and chase 9. Generate trails from the actual weapon path, sword-light from the casting hand, persistent directional ground cues, short afterimages, full-body directional hit reactions and selective impact pauses. Evaluate three renders of every signature skill: body only / VFX only / combined, each at 30, 50 and 70 px, with audio muted. Body-only should reach roughly 8/10 readability before VFX is allowed to rescue it. Combined should approach ~8.8+ internally before sending it to your blind judges. I would consider 8.5–9.0 a realistic first external result after this rebuild, with 9+ achievable through iteration; I would not expect a reliable 9 while the hooded stand-in remains the animation target.

The biggest change I would make tonight is therefore not another procedural parameter pass. It is one deliberately ugly, human-proportioned, no-VFX, six-pose prototype designed entirely around what survives at 50 pixels.

If that prototype suddenly looks powerful, you have proved that your animation technology was largely fine and the missing layer was authored pose direction. If it still looks weak, you have isolated the problem before spending weeks modeling and animating the real heroine.

ChatGPT can make mistakes. Check important info.
Latest response




Thinking effort
High