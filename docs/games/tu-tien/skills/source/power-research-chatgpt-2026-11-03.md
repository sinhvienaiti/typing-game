https://chatgpt.com/c/6ae8d7a8-cdfc-83ec-9522-f7cde2543fc9

Finish with which direction you recommend and why, and a short list of WebGL techniques with rough per-frame cost for 500 swords hunting foes across 40 m.
…
Show more
Worked for 5m 36s
ChatGPT said:
Research findings → design implications

I treated “most-loved” as high-signal references with strong community discussion, not as an objective ranking. I also weighted mechanics that transfer to your fixed 3/4 typing-game camera rather than simply copying impressive close-up ultimates.

One important caveat: I found solid verifiable material for Tale of Immortal, NARAKA, Wuthering Waves, Zhu Xian World, Vampire Survivors and A Record of a Mortal’s Journey. I did not find comparably reliable mechanical documentation for Immortal Taoists, so I would not use it as a hard design benchmark.

1. Field-wide flying swords: what actually creates the xianxia fantasy

Tale of Immortal is useful because the fantasy escalates through persistence. Its Sunset Sword literally summons a Rain of Swords over an area; Sword Slash stacks can extend that rain by one second each, and recasting while it remains active increases the number of falling swords. The broader Sword kit also supports very high-frequency cooldown loops. Player-review analysis is telling: people specifically enjoy the “growing storm of swords, fireballs and summons” when builds come together, but combat is also criticized for becoming repetitive or simply holding attack. 
Tale of Immortal
+1

NARAKA's Wuchen gives an even more relevant targeting lesson. His Blade Storm strikes a hit target with a series of spirit blades, or rains them into the impact area on a miss. More importantly, a 2025 update explicitly changed multi-blade tracking so simultaneous spirit blades prefer different enemies. An older Autotrack implementation automatically released blades as enemies approached, with subsequent blades at three-second intervals. That is almost exactly the targeting principle your “whole-map sword hunter” needs: spectacle comes partly from watching the formation intelligently divide itself among prey. 
Naraka: Bladepoint
+2

Wuthering Waves 3.7 gives a good modern version of persistent off-field threat. Kuro officially classifies Hsin around Main Damage, Coordinated Attacks and Resonance Skill damage; released gameplay shows her leave a golden field that persists after she swaps out and periodically calls swords/pillars down on enemies. The power fantasy is “I made a law of the battlefield,” rather than “I fired one projectile.” 
Wuthering Waves
+1

Zhu Xian World is structurally close to your Sword school. Qingyun's kit includes flying-sword, sword-array and burst attacks. One documented version of 寰宇千锋 sends multiple flying swords skyward and then lets later damage call swords back down; official 2026 balance notes even nerfed its multi-target behavior because it was too strong in multi-target combat. 
17173 News
+1

A Record of a Mortal's Journey gives the canonical cultivation-scale image: Han Li divides his spiritual sense into 72 parts to control 72 Azure Bamboo Cloudswarm Swords simultaneously. The impressive part isn't merely “72 projectiles”; it is that they act as a coordinated formation controlled by one cultivator. 
Wuxiaworld

Vampire Survivors gives the best pacing lesson. Victory Sword repeatedly attacks the closest enemies; Gorgeous Moon escalates in three phases: a glyph forms, 20 closest-target beams accelerate over roughly 9.1 seconds, then at 12.1 seconds comes a screen-wide erasure followed by vacuum. It demonstrates that a screen-clear feels larger when the player first sees the system hunting individuals, then escalating beyond individual targets. 
Vampire Survivors Wiki
+1

The downside is equally useful. Vampire Survivors players repeatedly complain that at extreme power levels the weapon effects make enemies, drops and terrain unreadable; damage-number removal helps only partly because the screen-wide VFX themselves remain the problem. 
Steam Community
+1

Design conclusion: your map-wide sword skill should not merely spawn 500 swords and explode. It should have four readable states:

Heaven changes → swords assemble → swords visibly choose prey → one decisive ending.

The player should be able to look at a beast and understand, “those six swords have chosen that beast.”

2. Camera and screen effects: power versus irritation

Squirrel Eiserloh's GDC camera work gives a very useful general recipe: accumulate a normalized trauma value, derive shake strength using trauma² or trauma³, and use coherent/Perlin noise rather than raw random offsets. That produces a large impact that rapidly becomes subtle instead of buzzing constantly. 
GDC Vault
+1

Jason de Heras documents Street Fighter V using 8/12/15 frames of hit pause for light/medium/heavy attacks—about 133/200/250 ms at 60 Hz. He also notes DMC5 reserves hit pause mostly for heavy attacks so ordinary slicing remains fluid. Another breakdown estimates Bayonetta's Witch Time transition slowdown around 0.25 s. 
Jason de Heras
+1

Those numbers are far too large for your routine hits. Your game simultaneously has continuous typing, dozens of targets and potentially hundreds of sword impacts. The useful lesson is the tiering, not the magnitude.

Monster Hunter is a particularly good warning: World received complaints that very strong hitstop interfered with play; when Wilds' beta reduced it too far, players then complained that hits had become weightless, and Capcom restored stronger hitstop plus impact sound. 
PC Gamer
+1

Full cinematic camera takeover has the same trade-off. Genshin players praise beautiful Burst cinematics but have repeatedly asked for ways to disable the forced close-up because it hides enemy positioning and breaks orientation. HSR has similarly received feedback around repeated flashy ultimate effects causing visual fatigue; HoYoverse even responded to complaints about excessive flashing in Seele's Ultimate. 
Reddit
+1

Microsoft and Steam's accessibility guidance therefore recommends making shake, blur and automatic camera movement adjustable or disableable. Microsoft specifically points to games exposing radial blur, screen shake and full-screen effects on 0–100 sliders. 
Microsoft Learn
+1

For Tu Tien Thu Ai

I would use:

camera punch, yes;
brief shake, yes;
short, rare combat-time freeze, yes;
slow motion, only skills/ultimate;
world darkening, strongly yes;
full-screen radial blur, almost never;
chromatic split, edge-only and <50 ms;
letterbox, only an ultimate and only if the gameplay rectangle does not change;
full character cut-in, sparingly;
word-tag/UI layer never receives bloom, blur, chromatic aberration or exposure changes.

The critical principle is: make the world react more than the camera reacts.

3. Enemy hit reaction: what survives a 3/4 camera and 100 enemies

DMC5 is valuable here because its reaction system explicitly prevents every hit from retriggering a full reaction. A second hit during an existing reaction can damage without restarting it, while repeated hits can eventually produce a stronger eject response. That avoids the visual mush of constantly resetting stagger animations. 
Jason de Heras

Wuthering Waves' own CBT feedback specifically called out “poor sound effects and hit feedback,” after which the team said it would revise weapon hits, skill sound, camera transitions and landing feedback. 
Wuthering Waves

For top-down/3/4 visibility, I rank reactions:

Best: 2–4 frame rim flash → directional spark/slash → tiny silhouette displacement → clear death transformation.

Useful selectively: stagger, launch, armor fragments, one or two spectral swords stuck into elites.

Poor for 100+ mobs: detailed wounds, tiny blood decals, one stuck sword per ordinary hit, complex per-monster secondary particles.

Your camera needs the reaction to change the enemy's silhouette, not just decorate its skin.

Sound should reinforce the same hierarchy. Monster Hunter's sound director describes hit sounds varying with monster-body hardness and weapon sharpness, but says the team deliberately revised overly literal parameter-driven sounds when they became unsatisfying. Their system also suppresses low-priority simultaneous sounds so important combat cues survive busy battles. 
the ESA

That strongly argues for impact batching in your 500-sword sequences rather than playing 500 independent sword samples.

4. Damage numbers: the lesson is “dopamine, then compilation”

There is a remarkably consistent pattern:

Reference	Useful idea
Genshin	Critical hits use a larger font than non-crits. 
Genshin Impact Wiki

ZZZ	Attribute-specific colors; crit numbers become more prominent and use an exclamation mark. Current settings also include Damage Compilation, consolidating combat numbers by skill/attribute. 
Zenless Zone Zero
+2

Diablo IV	Normal white, crit yellow, overpower light blue, overpower+crit orange; later updates abbreviated large combat numbers such as 10000 → 10k. 
Wowhead
+1

Lost Ark	Officially added an “Abbreviated Damage Font” option. 
Lost Ark - Free to Play MMO Action RPG

PoE2	Goes the other way: essentially no normal floating damage numbers; discussion shows the split—some players value clean immersion, others feel they lose hit/progression feedback. 
Steam Community

HSR / WuWa	Current player requests increasingly ask for hiding or compiling multi-hit numbers because dense attacks can cover the animation itself. WuWa discussion specifically points to ZZZ-style cumulative damage as desirable. 
Reddit
+1

So I would not imitate the old “one number for every sword” approach.

For 300 sword impacts, the correct dopamine unit is the attack, not every collision.

5. Voice and sound: why a two-word bark can outperform a paragraph

HSR community discussions are remarkably focused on delivery: simple lines become memorable because of timing, timbre and personality, and players explicitly distinguish between powerful normal-speed deliveries and rushed 2× versions. Players also praise extremely short barks such as Kafka's “Boom” precisely because they are concise and inseparable from the action. 
Reddit
+1

The inverse is repetition fatigue: repeating the exact same animation/line hundreds of times eventually produces requests to skip or accelerate it. 
Reddit

For your game I would therefore record 3 variants per frequently used skill, not one:

one English localized line;
corresponding Mandarin delivery;
a wordless kiai/exhale.

The player selects the voice language; you do not play multiple languages together.

For sound structure, use four semantic layers rather than “one cool sword sound”:

summon/cast → flight → material impact → death/aftermath.

The ultimate then adds a fifth layer: world-state audio—music ducking, atmospheric pressure, silence or ritual tone.

The non-negotiable casting rule

This applies to all three directions:

The last correct keystroke IS the release trigger. There is never another charge animation after typing.

While the player types, you may accumulate light, sword ghosts, formation geometry, sound tension, breathing, runes, etc. On the final correct key:

t = 0 ms: game logic enters CAST;
damage/projectile scheduling is committed immediately;
first visible action appears on the next rendered frame, normally within 0–16.7 ms at 60 Hz;
the first damaging/hunting action must begin ≤50 ms after the key;
any spectacular “wind-up” happens after something has already fired, or was already happening during typing.

That single change should eliminate one of the owner's biggest complaints.

Direction A — Celestial Sword River
Core fantasy

The cultivator does not throw swords; he opens a river of swords in Heaven and diverts its current toward every beast on the battlefield.

This is the direction I think best fits Tu Tien Thu Ai.

New field-wide skill

Vạn Kiếm Triều Tông — 萬劍朝宗 — Wàn Jiàn Cháo Zōng
English: Ten-Thousand Sword Convergence

I would make this the powered-up/reworked Slot 4 rather than turning the ultimate into the only map-wide move.

Timeline
Time	Frames	Event
While typing	pre-cast	Each correct key adds faint sword silhouettes to a curved celestial stream above the hero. No gameplay delay.
0.000 s	F0	Last key. Eight real swords launch immediately from the hero toward nearby threats. Sharp metallic snap.
0.017–0.067	F1–4	World exposure drops ~8%. A pale-blue sword-river seam appears diagonally across the sky.
0.067–0.200	F4–12	64 sword seeds rise from the field and join the river.
0.200–0.500	F12–30	River broadens over almost the full 40 m field; 320 visible swords on High. Formation visibly rotates tips toward assigned enemies.
0.500–2.800	F30–168	Hunting phase. 24–36 swords peel off per 100 ms in curved dives. Instances recycle, producing roughly 700–900 perceived strikes without needing 900 meshes.
2.800–3.200	F168–192	Remaining swords climb, spiral once and line up along one enormous diagonal celestial stroke.
3.200	F192	Finisher: the stroke sweeps through the whole battlefield. Trash receives cleanup damage; elites/bosses receive the remaining allocated hits.
3.200–3.450	F192–207	Sword river folds into a thin point above the hero and disappears with one deep jade-bell tone.
Targeting

Use threat-weighted target reservations, not pure nearest-neighbor.

priority = gateThreat × 2.0 + eliteWeight × 1.5 + proximity × 0.8 + lowHPFinish × 0.5 - reservedSwordPenalty

Rules:

trash: normally max 2 swords reserved simultaneously;
elite: 4–6;
boss: 8–12;
killed target → sword retargets within the next simulation tick;
15–20% of swords intentionally choose a different nearby target even if the mathematically optimal target is the same.

The visible effect should look intelligent, like spiritual sense controlling a sword formation.

Screen-effects recipe
Action	Shake	Hitstop	Slow	Screen state	Cut-in
Basic sword	1.5 px, 65 ms quadratic decay	12 ms target-local	none	white/cyan flash α0.06, 45 ms	No
Normal skill	3 px, 100 ms	24 ms primary impact; secondary hits 8–10 ms visual hold only	0.90× for 70 ms on finisher	darken α0.08/120 ms; flash α0.10/45 ms	No
Ultimate	7 px + ≤0.08° roll, 200 ms	55 ms combat freeze at climax	0.50× for 160 ms	darken α0.24/360 ms; silver flash α0.14/45 ms	No full cut-in. 160 ms calligraphy banner near top edge

If the 55 ms ultimate freeze occurs while another word is active, pause that word's typing timer for exactly those 55 ms. Input/UI rendering still updates.

Hit reactions

Small beasts: 2-frame cyan-white rim; 5–10 cm recoil in attack direction; one sharp slash streak; deaths unwrap into white-blue spirit threads plus 2–4 ink flecks.

Elites: 3-frame rim; 70–90 ms stagger only on major strikes; up to two translucent swords remain stuck for 0.3–0.5 s; death fractures into six luminous spirit shards.

Boss: never translate the root transform. Use 1–3° upper-body/head recoil, weak-point flash, directional slash scar and a brief sword-qi ripple through the body. No chain stagger.

Damage numbers

Thin, elegant sharp-serif / calligraphic hybrid numerals, but extremely legible.

normal: ivory;
sword-qi: ivory with pale-cyan lower stroke;
crit: 125% size, platinum-gold edge, tiny four-point slash spark;
multi-hit: accumulate per target for 150 ms;
display 12.8K × 6, not six overlapping values;
field-wide attack: maximum 2 number packets/target/sec;
5+ trash enemies struck in one screen cluster → one cluster total at their centroid.
Voice

Voice: 26–32, low clear tenor, calm and almost effortless during basics; ultimate progresses from near-whisper to absolute command.

Skill	English	Mandarin	Wordless
Basic Flying Sword	“Go.”	疾！ — Jí!	short “Hnh.”
Slot 1 — three swords	“Three blades. One intent.”	三剑一念！ — Sān jiàn yī niàn!	“Hah!”
Slot 2 — piercing line	“One sword pierces Heaven.”	一剑贯天！ — Yī jiàn guàn tiān!	sharp “HAA!”
Slot 3 — guard ring	“Sword wheel—guard.”	剑轮护身！ — Jiàn lún hù shēn!	controlled exhale
Slot 4	“Ten thousand swords—return.”	万剑归宗！ — Wàn jiàn guī zōng!	rising “Hè!”
Ultimate	“Milky Way overturned—ten thousand swords descend!”	星河倒悬，万剑天降！ — Xīnghé dàoxuán, wàn jiàn tiānjiàng!	inhale → sustained “HAAAH!”

Record at least three alternates for slots 1–4.

Slot 4 sound layers

Typing: each valid key quietly adds a pitched metal harmonic; never louder than the typing sound itself.

F0 cast: dry scabbard snap + high sword transient.

River opening: broad reversed metallic swell + high-altitude wind, mostly stereo rather than hundreds of objects.

Hunting: one continuous “blade swarm” texture whose density parameter follows active sword count; only the nearest 8–12 swords get actual spatial fly-bys.

Impacts: material bus—flesh/chitin, stone/armor, spirit/shield—with attack clusters merged into ~30–50 ms event buckets.

Ending: 40 ms near-silence → enormous clean slash → low bell → long air tail.

Ultimate audio
BGM ducks ~5 dB over 120 ms.
Ambient insects/wind vanish.
Low sub-pressure swell.
Heavenly formation produces a distant 72-sword metallic chorus.
Three volleys get three progressively lower transient clusters.
Before final impact: 60 ms vacuum.
Final impact = sword crack + low thunder + body-material layer.
Music restores over ~350 ms.

No 500 individual sword one-shots.

Word-tag safety

This direction is ideal for readability because its spectacle is mostly above and between targets.

tags rendered in a separate pass after tone mapping/bloom;
world darkening never darkens tags;
2–3 px dark outline + ~70% black translucent backing;
VFX beneath a tag's screen rectangle receives ~50% opacity suppression;
damage numbers prefer below-right of a beast; word tags own the above-head zone;
calligraphy banner occupies top 15% only and remains behind the tag layer.
Direction B — Heaven-Hunt Execution Array
Core fantasy

Every finished word is a death warrant; the sword array marks beasts, hunts them from impossible angles and executes the battlefield.

More frightening, less graceful than A.

Field-wide skill

Thiên Kiếm Liệp Sát Trận — 天劍獵殺陣 — Tiān Jiàn Liè Shā Zhèn
English: Heaven-Hunt Sword Array

Timeline
Time	Frames	Event
While typing	pre	Thin black-red seals appear under currently dangerous enemies.
0.000	F0	Final key: 12 swords instantly rip outward from black cracks around hero.
0.000–0.100	F0–6	Saturation −12%; dark circular “heaven seal” becomes visible above field.
0.100–0.350	F6–21	400 swords manifest around field perimeter and high sky; every sword visibly turns toward a victim.
0.350–2.350	F21–141	Execution salvos every 6 frames. Swords accelerate, disappear into short black streaks, rematerialize 1–2 m before impact.
2.350–2.700	F141–162	Surviving/pinned swords vibrate. Array sigil contracts.
2.700–2.900	F162–174	All spectral swords pull backward through their victims in one synchronized recall.
2.900–3.050	F174–183	Giant black-red seal closes with a dry thunderclap.
Targeting

This one deliberately feels predatory:

beasts closest to mountain-pass failure line;
dangerous caster/ranged enemies;
elites;
wounded trash likely to die from one sword;
boss.

Sword reservation:

trash 1;
ranged/dangerous trash 2;
elites 3–5;
boss 10.

When a sword kills early, it immediately picks another target rather than returning.

Screen recipe
Action	Shake	Hitstop	Slow	Screen	Cut-in
Basic	2 px / 75 ms	16 ms local	none	white flash α0.05/40 ms	No
Skill	4.5 px / 130 ms	30 ms main impact	0.82× / 90 ms	dark α0.14/180 ms	No
Ultimate	9 px / 240 ms	70 ms global climax	0.35× / 200 ms	dark α0.33/520 ms + vermilion flash α0.12/40 ms	Yes: 240 ms ink-silhouette cut-in

The cut-in starts after F0 cast logic has already fired. If it freezes combat for 240 ms, all typing countdowns freeze for those 240 ms too.

Reactions/deaths

Trash: hard 0.25–0.35 m directional snap on major hits; black rim with vermilion inner edge; death becomes an ink silhouette for 3 frames, then tears apart into crimson spirit dust.

Elite: reaction immunity window of ~120 ms after a stagger so 20 swords cannot repeatedly restart it. 2–4 spectral swords may remain embedded.

Boss: absolutely no launch. Each major hit creates a localized armor/body compression pose plus a red sword-seal fracture. Ultimate adds one enormous cross-field wound ripple.

Numbers

Angular, seal-inspired forms.

normal = pale bone-white;
crit = vermilion/orange-white;
crit 135% size with a square “seal stamp” behind it for ~70 ms;
packet window = 120 ms;
killing blow may show one larger number;
everything else aggressively compiled.
Voice

Voice: 32–40, dry low baritone, extremely restrained. Basics sound almost contemptuous; only the ultimate reaches a shout.

Skill	English	Mandarin	Wordless
Basic	“Marked.”	定！ — Dìng!	tongue click / breath
Slot 1	“Three blades. Sentence passed.”	三剑定罪！ — Sān jiàn dìng zuì!	“Tch—hah!”
Slot 2	“No wall stops this.”	一线破关！ — Yī xiàn pò guān!	“HA!”
Slot 3	“Enter the array. Be cut.”	入阵者，斩！ — Rù zhèn zhě, zhǎn!	low “Hng.”
Slot 4	“The array has chosen you.”	剑阵锁命——诛！ — Jiàn zhèn suǒ mìng—zhū!	whisper → “HAA!”
Ultimate	“Heaven has no mercy. Ten thousand swords—erase them.”	天道无情，万剑诛灭！ — Tiāndào wúqíng, wàn jiàn zhūmiè!	quiet inhale → roar
Slot 4 audio

Typing adds faint brush/seal scratches rather than musical tones.

Cast gets a dry sword-snap plus one low “lock” transient.

Target-selection is communicated with grouped tonal ticks: one for ordinary prey, lower one for elite acquisition—not a tick for 100 enemies.

Hunt uses knife-like air slices and occasional close pass-bys.

Impacts have dry blade transient + material layer + small low-frequency body hit.

Ink death gets a paper-rip/ash sound rather than gore.

Ultimate

Music low-passes and ducks; a distant ritual drone enters. Three volley impacts become progressively wider and lower. Before the last recall, remove virtually everything for ~60 ms, then hit with a massive metal shear and sub impact.

Tag protection

This direction poses the greatest readability danger, so:

black/red VFX are forced below 0.55 luminance around word-tag regions;
no red damage numbers within the tag rectangle;
cut-in is behind live tag UI;
tags gain 80% black backing during the ultimate;
chromatic separation affects only the outer 18% of the viewport, never the central enemy/tag region.
Direction C — Galactic Constellation Arsenal
Core fantasy

Every typed word completes a constellation node, turning the hero into the commander of a celestial weapons platform.

This is the brightest, most anime/Honkai/WuWa-adjacent direction—but still original in mechanic.

Field skill

Tinh Hà Kiếm Vực — 星河劍域 — Xīnghé Jiànyù
English: Galactic Sword Domain

Timeline
Time	Frames	Event
While typing	pre	Correct letters illuminate constellation nodes orbiting hero.
0.000	F0	Final node completes; 16 swords fire instantly.
0.000–0.150	F0–9	Camera performs tiny 2.5% punch-in then begins returning. Indigo vignette appears.
0.150–0.450	F9–27	Huge circular star formation opens overhead.
0.450–3.000	F27–180	Up to 500 sword instances: ~300 active hunters + ~200 cheaper formation/background swords. They travel along graceful constellation arcs.
3.000–3.200	F180–192	Active swords snap upward into eight radial spokes.
3.200–3.450	F192–207	All spokes point downward.
3.450	F207	One all-field constellation pulse causes the final hit.
3.450–3.850	F207–231	Formation collapses into star motes that fall around hero.
Targeting

Use the uniform spatial grid to score cells, not only individual enemies.

60% of swords → densest cells;
25% → elites/high threat;
15% → enemies nearest the gate.

Within a chosen cell, pick the target with the lowest current sword-reservation count.

This produces obvious sweeping patterns instead of 500 independent bees.

Screen effects
Action	Shake	Hitstop	Slow	Screen	Cut-in
Basic	1 px / 50 ms	8–10 ms	none	α0.04/35 ms	No
Skill	2.5 px / 90 ms	20 ms	0.92× / 60 ms	dark α0.05/90 ms; flash α0.08/40 ms	No
Ultimate	6 px / 170 ms + 1.8% zoom punch	45 ms	0.55× / 120 ms	dark α0.20/280 ms; white-gold α0.12/35 ms	180 ms side-card only

No full-screen freeze. The anime portrait/calligraphy card takes at most ~24% of screen width.

Reactions

Trash: 1–2 frame platinum rim; slight body lean; bright directional star slash; deaths unfold into geometric constellation motes.

Elite: short stagger, one armor shard, optional 0.2 m upward pop on the final hit only.

Boss: limb/torso recoil and bright weak-point ring. No displacement.

Damage numbers

Rounded-bold modern anime font with one sharp diagonal cut.

neutral sword = white;
qi = pale cyan;
crit = 120% + star spark;
accumulate over 100 ms;
short 10–12 px upward arc;
cluster hits on 5+ trash become one 36.4K × 8.

This direction should borrow ZZZ's Damage Compilation philosophy rather than HSR-style clouds of individual values. 
Zenless Zone Zero
+1

Voice

Voice: 20–26, bright mid-tenor/alto, energetic and clean rather than screaming constantly.

Skill	English	Mandarin	Wordless
Basic	“Fly!”	飞剑，去！ — Fēijiàn, qù!	“Ya!”
Slot 1	“Constellation—three points!”	三星成锋！ — Sān xīng chéng fēng!	“Hya!”
Slot 2	“One stroke draws the sky!”	一剑画天！ — Yī jiàn huà tiān!	“Hya—!”
Slot 3	“Orbit—protect!”	剑轮，护！ — Jiàn lún, hù!	“Heh!”
Slot 4	“Galactic Sword Domain—open!”	星河剑域——开！ — Xīnghé Jiànyù—kāi!	rising “HAA!”
Ultimate	“Milky Way, answer me—swords like rain!”	星河应我，万剑如雨！ — Xīnghé yìng wǒ, wàn jiàn rú yǔ!	heroic “YAAAH!”
Slot 4 audio

Every completed constellation node contributes a high, short metal/stone chime.

F0 is a bright resonant snap.

Formation opening uses widening stereo harmonics.

Sword travel uses one swarm layer plus limited hero-near fly-bys.

Impact sounds are grouped in musically pleasing 1/8-note-density waves without quantizing actual gameplay damage.

Ultimate audio

Constellation rings produce octave chimes; music ducks 4 dB; a low choir-like synth enters beneath three volleys. Last volley gets 45 ms silence, deep impact, enormous high-frequency sword shimmer, then a single resonant star-bell.

Tag readability

This direction has the brightest VFX, so:

bloom threshold deliberately excludes tag luminance;
formation lines are never drawn through projected tag rectangles at full intensity;
side-card avoids the active enemy cluster;
damage compilation is mandatory during map-wide attacks;
white tags get a dark navy/black backing during the ultimate.
My recommendation: Direction A — Celestial Sword River

I would choose Direction A.

Direction B is more terrifying, but its darkness, cut-in and execution language push the game toward “demonic assassin” rather than elegant sword immortal.

Direction C is extremely marketable and probably very satisfying, but it risks reading as generic modern anime/gacha spectacle.

A has the strongest xianxia identity because the ultimate fantasy is not merely “lots of swords”: it is one cultivator possessing enough spiritual control to turn the entire sky into a sword formation. That is exactly what references like Han Li's 72-sword control and Qingyun-style sword arrays evoke. 
Wuxiaworld
+1

I would still steal two systems from the other directions:

Direction B's brutal enemy hit/death response;
Direction C's Damage Compilation.

So the production target becomes:

A's celestial grandeur + B's impact violence + C's UI discipline.

That directly answers every part of the owner's 6/10 verdict without sacrificing the actual typing game.

One universal word-tag architecture I strongly recommend

Do not treat word tags as ordinary world sprites.

Render:

3D world → combat VFX → bloom/post → tone mapping → WORD TAG PASS → damage-number pass → HUD

Word tags should therefore never inherit:

bloom;
radial blur;
zoom blur;
chromatic aberration;
world exposure;
color grading;
full-screen flashes.

Project each enemy anchor using the final shaken camera matrix, then draw the tag crisp in screen space. That keeps it attached to the beast while remaining perfectly sharp.

Give each tag:

2–3 px outline;
4–6 px internal padding;
adaptive 65–85% dark backing depending on luminance underneath;
highest combat-text z-order.

Also maintain screen rectangles for all visible tags. Pass those rectangles into the VFX compositor as a low-resolution readability mask and reduce underlying bloom/particles by ~40–60%.

Damage-number placement then treats those rectangles as forbidden zones.

That is how you can make an ultimate absurdly large without ever compromising the primary mechanic.

500 hunting swords in three.js/WebGL2

These are engineering budget targets, not measured benchmarks. Actual cost needs profiling on your M4 and RTX 3050 Ti at your shipping resolution.

Three.js explicitly recommends InstancedMesh for many copies of the same geometry/material because it reduces draw calls. InstancedBufferAttribute gives you custom per-instance data, and BufferAttribute.addUpdateRange() can restrict GPU uploads to modified ranges. 
Three.js
+2

System	Approach	Rough budget
Enemy spatial index	2 m uniform grid over 40×26 m; rebuild 10–20 Hz	0.03–0.10 ms CPU avg
Target assignment	Reservation-count system; retarget only dead/out-of-range swords; stagger updates	0.05–0.18 ms CPU
500 sword steering	Structure-of-arrays Float32Array; analytic seek/curved path, no per-sword objects	0.03–0.15 ms CPU
Instance transforms	Custom position + orientation/phase attributes instead of allocating 500 Matrix4s	0.04–0.18 ms CPU/upload
Sword bodies	One low-poly InstancedMesh, ideally 1 material / 1 draw	~0.05–0.25 ms GPU
Trails	One instanced camera-facing tail card per sword; no 500 dynamic ribbon meshes	~0.10–0.45 ms GPU
Hit VFX	pooled/instanced; cap simultaneous visible bursts around 60–100	~0.10–0.35 ms GPU
Sword-specific bloom contribution	high-threshold emissive, tightly controlled screen coverage	~0.2–0.8 ms incremental
Likely sword-system total	excluding your existing scene	roughly 0.2–0.6 ms CPU + 0.5–1.8 ms GPU

UnrealBloomPass already uses a reduced-resolution mip chain to keep large-radius bloom reasonably efficient, but it is still a full-screen post effect, so it deserves its own GPU budget rather than assuming 500 glowing swords are free. 
Three.js
+1

A few implementation choices matter disproportionately:

Do not search every foe from every sword every frame. With 500 swords × 150 monsters × 60 Hz, even simple math becomes pointless work. Assign a target and keep it until something meaningful changes.

Do not create 500 JS Sword objects. Keep posX[], posY[], posZ[], velX[], targetId[], phase[], etc. in typed arrays.

Do not make 500 real ribbon trails. One stretched shader quad behind each sword will communicate motion perfectly at your camera distance.

Recycle swords. The eye cannot distinguish 320 unique swords producing 900 attacks from 900 permanently alive meshes.

Do not recompute InstancedMesh bounds every frame. Three.js notes transformed instances can require updated bounds; because your complete 40×26 m combat field is already visible, give the sword system a conservative battlefield-sized bound once, or deliberately handle its culling strategy yourself. 
Three.js
+1

Stay with normal WebGL2 instancing for r170. Three's newer StorageInstancedBufferAttribute is WebGPU-only, so it is not appropriate for this implementation. 
Three.js

With that architecture, 500 visible swords are not the scary part. The danger is translucent overdraw, bloom, trails, particles and 500 independent target/audio/text events. The sword geometry itself should be cheap.

Primary reference links

Tale of Immortal — Sword mechanics and Rain of Swords · NARAKA official Wuchen Blade Storm update · NARAKA 2025 multi-target tracking update · Wuthering Waves 3.7 official notes · Zhu Xian World 2026 Qingyun balance notes · GDC: Juicing Your Cameras With Math · Jason de Heras — combat/hit feel breakdown · Microsoft camera/motion accessibility guidance · Monster Hunter Wilds sound-design interview · Three.js InstancedMesh documentation

ChatGPT can make mistakes. Check important info.
Latest response




Thinking effort
High