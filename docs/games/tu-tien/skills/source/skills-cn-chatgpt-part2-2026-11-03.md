https://chatgpt.com/c/6ae8da12-8b08-83ec-83c7-5a34e441e0e1

Escalate each school from weapon technique to battlefield authority to mythic phenomenon, as you concluded.
Worked for 2m 21s
ChatGPT said:
PART 2 — Full redesign: Sword + Sabre

I kept the conclusion from Part 1 as the governing progression:

Sword: weapon technique → sword-intent geometry → sword-heart authority → all blades obey → heaven itself is cut open.
Sabre: decisive cut → mass/inertia → refusal to yield → execution pressure hunts across the battlefield → one sabre divides the world.

These are original skills. The sources below provide the design grammar, not copied names/choreography. In particular, Li Chungang's “剑来” is remembered for hundreds/thousands of swords answering one command; Han Li's Great Geng Sword Formation for organized lethal geometry; Tale of Immortal players explicitly pursue “万剑归宗 / full-screen clearing”; Naraka's tai-dao compresses many cuts and a redraw into an instant; and Where Winds Meet's modao builds its identity around large committed sweeps, toughness and counterplay. 
Bilibili
+4

Shared implementation rules

F0 = the last correct key, except Basic Auto where F0 means the auto-fire tick. One frame at 60 Hz is 16.67 ms. Every typed skill has a gameplay consequence at F0, so there is never an animation lock between typing and casting.

For ultimates, the sequence is deliberately:

last key → F0 mechanical hit/mark → pause game + typing timer → ~0.95 s anime cut-in → resume at F1.

So the cut-in does not violate the ≤50 ms response rule.

I would standardize screen effects as:

Tier	Treatment
T0	Local flash only; no camera displacement.
T1	0.3–0.5° camera punch; optional 1-frame hitstop on elite impact.
T2	1–1.5° punch, ~0.10 s shake, 2-frame elite hitstop, brief 0.90× time accent.
T3	~2° punch, 0.15–0.20 s shake, 3-frame heavy-hit stop, 0.80× accent for ~0.12 s, world darkens ~15%.
T4 Ultimate	~0.95 s paused cut-in; then 0.65–0.75× climax accent, 4-frame major hitstop, ~0.25 s shake, world darkening up to ~28%.

Word-tag protection: tags render after bloom/postprocessing; world-darkening never darkens them; a small screen-space exclusion halo suppresses high-luminance trails immediately behind the text. Do not make tags shake with the camera.

SCHOOL I — SWORD / KIẾM / 剑
School fantasy

The Sword cultivator starts as someone exceptionally skilled with a jian.

By slot 2, sword intent can occupy space.

By slot 4, the cultivator no longer attacks personally: weapons acknowledge an imperial-style command and conduct the battle independently.

The ultimate establishes the final claim:

The cultivator does not swing harder.
Their sword principle is strong enough to divide Heaven and Earth.

Visual palette: polished silver-white + very pale indigo/cyan sword-intent. Avoid elemental lightning/fire so Thunder and Fire later retain their own identities.

BASIC — Hàn Mang Điểm Phách

Code: SWD_A0_HANMANG

Name: Hàn Mang Điểm Phách — 寒芒点魄 — Hán Máng Diǎn Pò — “Cold Gleam Pierces the Spirit”

Source lesson: Where Winds Meet demonstrates sword qi as a readable ranged extension of swordsmanship rather than requiring the swordsman physically to reach every enemy. 
Gamersky

Fantasy: The cultivator barely moves; a needle-thin sword-intent flash picks a beast's vital point.

Area: Single target, 17 m acquisition; narrow 1.2 m continuation behind the target can clip one additional trash beast.

40-px silhouette: One crisp wrist/finger snap plus a single bright 2–3 px straight silver streak. No crescent, no particle cloud.

Timeline
F0 / 0.000 s: target receives damage immediately; tiny white rim flash.
F1 / 0.017 s: silver line becomes visible between sword tip and target.
F3 / 0.050 s: line snaps out.
F6 / 0.100 s: small wound-glint.
F12 / 0.200 s: completely clean again.
Five VFX phases

Charge: None; Basic Auto is not typed. Sword edge has only a faint permanent cold sheen.

Release: 8–12 cm of concentrated white sword-intent condenses at the tip.

Travel: Perceptually instantaneous straight streak; never a visible projectile travelling slowly.

Impact: Pinpoint four-ray star flash at the beast's center mass.

Aftermath: One hair-thin silver line hangs for ~0.08 s and disappears.

Screen tier: T0.

Beast reaction: Small beast gives a sharp localized recoil; elites only twitch at the struck point. Killing hit produces a white line through the silhouette followed by rapid silver dust shedding from that point outward.

Callout: Wordless short “Hè!”

Sound layers: dry jian ring → microscopic air snap → needle-like impact tick → on death, very brief crystalline disintegration hiss.

WebGL difficulty: S.

SLOT 1 — Nhất Tự Kinh Phong

Code: SWD_S1_YIZI

Name: Nhất Tự Kinh Phong — 一字惊锋 — Yī Zì Jīng Fēng — “One-Word Startling Edge”

Gameplay requirement: One short English word. Spammable. No conventional cooldown beyond the next word selection / typing cadence.

Source lesson: The readable sword-qi attacks of Chinese action games: one clean gesture can carry the blade farther than its physical length. Naraka's long sword similarly relies on clearly legible horizontal/vertical sword qi rather than projectile clutter. 
Gamersky
+1

Fantasy: One word, one breath, one sword stroke—but the sword-intent is several times wider than the steel.

Area: 7.5 m long × 5 m wide shallow fan; ideal trash-clearing spammable strike.

40-px silhouette: Hero makes a very short diagonal cut; a fat white calligraphic stroke appears on the ground plane for only a few frames.

Timeline
While typing: edge glow climbs per correct letter.
F0 / 0.000 s: inner 3 m fan already damages.
F1 / 0.017 s: outer pressure front begins.
F3 / 0.050 s: entire 7.5 m fan has resolved.
F7 / 0.117 s: beasts finish recoil.
F14 / 0.233 s: effect gone.
Five VFX phases

Charge: Each typed letter adds one short glint along the blade ridge; no growing orb.

Release: Silver-white compression flash hugging the cutting edge.

Travel: Broad flat pressure stroke skims 10–20 cm above terrain.

Impact: Targets receive a hard white edge-light on the struck side.

Aftermath: Dust/grass is pushed away in the same diagonal direction, leaving a faint temporary brushed line.

Screen tier: T1.

Beast reaction: Trash beasts snap sideways roughly half a body width; elites rotate shoulders but retain position. Death: silhouette briefly becomes a black cut-paper shape with one silver diagonal slit, then collapses into wisps.

Callout: Wordless “Hè!”

Sound: blade draw → compressed “whup” → clustered cloth/armor cuts → short tonal jian tail → separate death whisper.

WebGL difficulty: S.

SLOT 2 — Thất Tinh Liệt Phong

Code: SWD_S2_QIXING

Name: Thất Tinh Liệt Phong — 七星列锋 — Qīxīng Liè Fēng — “Seven Stars Array the Edges”

Cooldown: 8 s

WIDE AREA

Source lesson: Han Li's Great Geng Sword Formation is memorable not because it merely contains many swords, but because numerous blades become a formation and therefore turn territory itself into the weapon. 
Bilibili
+1

Fantasy: Seven points of sword intent establish an execution geometry; everything between the points is suddenly inside a blade formation.

Area: 26 m × 14 m oriented rectangle/fan toward the densest enemy region. Covers roughly one quarter to one third of the map.

40-px silhouette: Seven large silver points appear in a recognizable zig-zag constellation, then connect into a razor-bright lattice. Readable even zoomed out.

Timeline
F0 / 0.000 s: nearest formation node detonates and deals first damage.
F2 / 0.033 s: all seven nodes lock into position.
F4 / 0.067 s: first three connecting cuts fire.
F7 / 0.117 s: full lattice exists.
F12 / 0.200 s: cross-cut pulse.
F22 / 0.367 s: lattice collapses inward.
F36 / 0.600 s: visual aftermath only.
F48 / 0.800 s: clear.
Five VFX phases

Charge: Seven tiny sword-star motes progressively appear behind the hero according to normalized typing progress. They never fire before completion.

Release: Hero points the jian once; the first star slams into the ground at F0.

Travel: Remaining points shoot to their positions as straight streaks, not arcing projectiles.

Impact: Lines joining the seven points flash in carefully sequenced groups, producing overlapping broad cuts.

Aftermath: Seven thin silver scars remain on terrain for ~1.2 s with tiny motes drifting upward.

Screen tier: T2.

Beast reaction: First line makes beasts turn/recoil along the line normal; cross-cuts produce a second stagger. Trash deaths unravel into 2–3 clean luminous fragments rather than gore. Elite receives one stronger stagger on the lattice-collapse pulse only.

Mandarin callout: “七星，列锋！” — Qīxīng, liè fēng!
“Seven stars—array the edges!”

Sound layers: seven pitched sword notes → one command snap → seven arrivals in rising pitch → layered planar cuts → bass formation collapse → quiet metallic residue.

WebGL difficulty: M.

SLOT 3 — Kiếm Tâm Bất Động

Code: SWD_S3_JIANXIN

Name: Kiếm Tâm Bất Động — 剑心不动 — Jiàn Xīn Bù Dòng — “Unmoving Sword Heart”

Type: Guard

Suggested cooldown: 10 s.

Source lesson: Chinese sword fantasy repeatedly treats mastery as composure and intent, while wuxia game parry systems such as Naraka make the opponent's committed attack the trigger for retaliation. 
Gamersky

Fantasy: The body does not defend itself. Sword intent becomes so still that incoming violence is split around it.

Area: Guard radius 2 m; successful counter affects an 8 m × 110° wedge toward attacker.

40-px silhouette: Hero becomes perfectly still beneath one tall translucent upright sword silhouette roughly 2.5× character height.

Timeline
F0 / 0.000 s: guard is active immediately.
F0–F24 / 0–0.400 s: perfect-guard window.
On successful guard:
Counter F0: attacker immediately takes chip/poise damage.
+F2 / +0.033 s: vertical sword silhouette flashes.
+F4 / +0.067 s: reverse cut reaches attacker.
+F9 / +0.150 s: secondary pressure fan.
If unused, stance dissolves by F30 / 0.500 s.
Five VFX phases

Charge: During typing the jian loses reflections rather than becoming brighter—its surface becomes eerily matte and still.

Release: At F0 a transparent sword-intent pillar snaps upright through the hero.

Travel: On parry, a razor-straight return line runs from the contact point back through the attacker.

Impact: Contact freezes sparks for one frame, then ejects them backward.

Aftermath: A circular dust gap around the hero emphasizes that nothing crossed the sword-heart boundary.

Screen tier: T1 normally; T2 on successful elite parry.

Beast reaction: Trash attacker is thrown backward; elite's weapon/limb violently deflects sideways followed by a clear stagger. Killing counter leaves the enemy frozen upright for ~0.12 s before dissolving along the returned sword line.

Mandarin callout: “不动。” — Bù dòng.
“Unmoving.”

Say it almost quietly.

Sound: typing charge gradually removes ambience → metallic contact → one unnaturally clean high-frequency “ting” → bass pressure crack → attacker death layer.

WebGL difficulty: M.

SLOT 4 — Vạn Phong Thính Chiếu

Code: SWD_S4_TINGZHAO

Name: Vạn Phong Thính Chiếu — 万锋听诏 — Wàn Fēng Tīng Zhào — “Myriad Edges Hear the Edict”

Cooldown: 12 s

FIELD-WIDE — SELF-HUNTING

This is the Sword school's owner-demo skill.

Source lesson: Li Chungang's famous “剑来” works because swords belonging to the surrounding world answer him; descriptions have hundreds of swords from Huishan and roughly a thousand peach-wood swords converging until they obscure the sky. Han Li's sword formations add disciplined geometry, while Tale of Immortal players deliberately build toward “万剑归宗 / full-screen clearing.” 
Bilibili
+2

Fantasy: The hero issues an edict. The battlefield's sky becomes a court of blades, and those blades independently sentence beasts to death.

Area: Entire 40 × 26 m field.

Hunting duration: ~5.0 s.

Target logic: independently hunts enemies across the map, prioritizing:

beasts not struck recently,
high-density clusters,
low-health kill opportunities,
elites when no trash target is optimal.

On kill, a blade immediately retargets.

40-px silhouette: Eight large suspended sword-gates/constellations around the outer field boundary form a visible octagonal crown; tiny swords move between them. The hero remains readable as the still commander at center.

Timeline
F0 / 0.000 s: six nearest valid beasts are instantly marked and struck by initial sword-intent pins. Hunting has begun.
F2 / 0.033 s: eight celestial sword-gates open around field perimeter.
F6 / 0.100 s: first hunting cohort launches.
F12 / 0.200 s: sustained autonomous hunt established.
F12–F300 / 0.2–5.0 s: blades continuously acquire → dive → strike → rise → retarget.
F300 / 5.0 s: gates close.
F330 / 5.5 s: last residual trails vanish.
Five VFX phases

Charge: Typing progressively creates eight faint geometric “edict seals” around the sword hand. On the final few characters, distant weapons begin subtly vibrating—but none attack yet.

Release: Hero lifts only two fingers/sword tip. At F0 six silver pin-strikes hit immediately.

Travel: On High, up to ~144 visible instanced spirit blades circulate between the eight gates; gameplay can logically resolve more attacks than visible meshes. Blades fly mostly laterally and diagonally, never as generic vertical sword rain.

Impact: Each target gets a brief narrow sword-intent cross plus directional rim flash. Several simultaneous kills compile into one consolidated damage-number burst per cluster.

Aftermath: Dead beasts leave pale sword-shaped impressions in dust; the eight gates collapse inward into one tiny spark above the hero.

Screen tier: T3 on release, then T1 micro-punches are disabled during sustained hunting to avoid five seconds of camera vibration.

Beast reaction: Individual trash beasts are knocked in differing directions according to attack vector, making the field visibly “alive.” Elites receive only one full stagger every ~0.8 s to avoid stun-lock visual spam. Death: victim becomes a dark silhouette perforated by 2–4 silver seams, then dissolves upward like ash drawn toward the celestial gates.

Mandarin callout:
“万锋——听诏！” — Wàn fēng—tīng zhào!
“Myriad edges—heed the edict!”

Sound layers: low gathering chorus of distant unsheathing swords → command voice → eight gate booms → hundreds of quiet Doppler blade passes → spatialized hit ticks compiled by cluster → periodic deeper elite impacts → mass-death ash hiss.

Do not play 144 equally loud sword sounds.

WebGL difficulty: L.

Recommended implementation: InstancedMesh blades + GPU-computed/simple spline transforms; gameplay targeting stays CPU-side using a 5×4 or 8×5 spatial grid rather than pairwise searches.

SLOT 5 ULTIMATE — Nhất Tuyến Khai Càn Khôn

Code: SWD_U5_QIANKUN

Name: Nhất Tuyến Khai Càn Khôn — 一线开乾坤 — Yī Xiàn Kāi Qiánkūn — “One Line Opens Heaven and Earth”

ULTIMATE — Qi bar

FIELD-WIDE MYTHIC PHENOMENON

Source lesson: Li Chungang's sword mythology escalates all the way to “剑开天门”; Lu Xueqi's famous Divine Sword Commanding Thunder similarly works by making the cultivator's weapon a tiny axis through which the heavens answer. 
Bilibili
+1

This does not copy either attack. It takes the principle that final sword mastery should alter the cosmological scene.

Fantasy: The cultivator traces one impossibly thin sword line; sky and earth recognize it as a boundary and separate.

Area: Entire battlefield, with maximum damage in a 9 m-wide line passing through the densest enemy axis; secondary sword-law damage reaches everyone else.

40-px silhouette: Almost no clutter around the hero. The unmistakable image is a single silver line stretching from one screen edge into the sky, while the world on either side darkens differently.

F0 + cut-in contract
F0 / 0.000 s: every enemy receives a small “sword-law” impact immediately; nearest enemies recoil. A silver line appears through the battlefield.
Immediately after F0: game + typing timer pause for ~0.95 s real time.
Anime cut-in:
close crop of cultivator's eye;
reflected silver line crosses pupil;
cut to sword edge;
no elaborate attack animation.
Resume gameplay at F1.
Resume timeline
F1 / 0.017 gameplay s: clouds/upper darkness separate along the existing line.
F4 / 0.067 s: primary 9 m corridor receives catastrophic cut.
F8 / 0.133 s: secondary field-wide pressure pulse.
F13 / 0.217 s: complete silence for ~3 frames.
F16 / 0.267 s: all accumulated wounds “open” simultaneously.
F22 / 0.367 s: ground seam ignites silver-white.
F45 / 0.750 s: heaven scar begins closing.
F90 / 1.500 s: only terrain aftermath remains.
Five VFX phases

Charge: With typing progress, a razor-thin line behind the hero lengthens vertically through the sky. It never widens.

Release: F0: hero rotates the blade only a few degrees. The battlefield immediately receives the initial law-cut.

Travel: There is effectively no projectile. The line simply exists everywhere along its axis.

Impact: The two halves of the world's lighting shift apart for several frames; the main corridor flashes black → pure white → normal. Enemies then display simultaneous cut seams.

Aftermath: A glowing hairline fissure remains in terrain for 3–4 s; floating dust hangs on opposite sides of it moving in opposite directions.

Screen tier: T4 Ultimate.

Beast reaction: F0 produces immediate recoil. Main corridor throws trash beasts backward as shadow fragments; outside corridor they stagger toward the line. Elites drop to one knee/forelimb where anatomy permits. Death is elegant: silhouette turns monochrome, one bright line crosses it, upper and lower shadow masses offset only slightly and dissolve into silver-black motes—avoid gore.

Mandarin chant:
“剑心所至，天地皆开！” — Jiàn xīn suǒ zhì, tiāndì jiē kāi!
“Where the sword-heart reaches, Heaven and Earth open!”

Sound layers: typed-key charge adds nearly subliminal harmonics → F0 impossibly sharp sword note → cut-in voice + low heartbeat → resume with near-silence → colossal sub-bass spatial split → delayed mass impact → stone fissure → many deaths compressed into one downward spectral choir.

WebGL difficulty: L, but cheaper than the slot-4 sword population: the challenge is full-field masks, lighting split and postprocessing rather than geometry count.

SCHOOL II — SABRE / ĐAO / 刀
School fantasy

Sword says:

“Obey.”

Sabre says:

“Get out of my way.”

The school therefore avoids celestial sword formations and floating arsenals.

Its power language is:

body momentum → pressure wake → battlefield-clearing sweep → unavoidable execution → reality itself continuing the cut.

Research supports that identity. Naraka describes 百裂斩 as an instant draw with multiple cuts and follows it with a redraw-pursuit attack; its rhythm is characterized as “狂风骤雨.” Where Winds Meet's heavy modao performs enormous charged double sweeps and can pull surrounding enemies into a finishing slash. Nangong Pushe's legend pushes sabre escalation even further: increasingly lethal “stops,” and the famous image of one sabre stirring the entire snowy sky. 
GamerSky
+4

Visual palette: dark steel, chalk-white pressure, restrained black ink/smoke and tiny dark-crimson wound accents. Not fire.

BASIC — Đoạn Trần

Code: SAB_A0_DUANCHEN

Name: Đoạn Trần — 断尘 — Duàn Chén — “Sever Dust”

Source lesson: Naraka's tai-dao works through fast, decisive attack rhythm rather than a prolonged magical projectile show. 
GamerSky

Fantasy: A compact sabre flick sends enough pressure through the air to cut a beast before the blade physically reaches it.

Area: Primary target within 13 m; 2.5 m shallow cleave around target.

40-px silhouette: One short black-steel movement followed by a thick white slash dash, noticeably broader than Sword's needle-like auto attack.

Timeline
F0: damage.
F1 / 0.017 s: pressure mark becomes visible.
F3 / 0.050 s: nearby cleave resolves.
F8 / 0.133 s: recoil complete.
F12 / 0.200 s: clear.
Five phases

Charge: None.

Release: Tiny dark compression puff at sabre edge.

Travel: Broad white pressure wedge, barely two frames long.

Impact: Short black-centered/white-edged slash spark.

Aftermath: Dirt kicks outward as one low horizontal puff.

Screen tier: T0.

Beast reaction: Stronger lateral jerk than Sword auto. Death creates a momentary horizontal black line across the silhouette followed by dusty fragmentation.

Callout: Wordless breath/grunt.

Sound: heavy steel flick → bass-heavy air split → meaty/armored cut → dust slap/death layer.

Difficulty: S.

SLOT 1 — Lược Ảnh

Code: SAB_S1_LUEYING

Name: Lược Ảnh — 掠影 — Lüè Yǐng — “Passing Shadow”

ONE-WORD SPAMMABLE

No conventional cooldown.

Source lesson: The appeal of Naraka's tai-dao lies partly in compressing draw, multiple cuts and pursuit into extremely short windows rather than lengthy committed animations. 
GamerSky
+1

Fantasy: The player types one short word; the enemy sees the cultivator's afterimage only after the edge has already passed.

Area: 7 m × 120° frontal sweep.

40-px silhouette: Hero's body makes only ~20° of visible rotation; a thick hook-shaped white-black stroke completes the attack for them.

Timeline
While typing: sheath/edge produces tiny intermittent sparks.
F0: inner 3.5 m sweep hits.
F2 / 0.033 s: full 7 m arc resolves.
F5 / 0.083 s: one afterimage briefly appears behind hero.
F10 / 0.167 s: afterimage collapses.
F15 / 0.250 s: clear.
Five phases

Charge: Blade reflection narrows as if disappearing into shadow.

Release: Single hard draw flash.

Travel: Hook-shaped pressure arc, not an actual projectile.

Impact: Broad side-rim flash across every struck beast.

Aftermath: One black afterimage of the cultivator finishes the swing a fraction later.

Screen tier: T1.

Beast reaction: Trash beasts are knocked outward around the arc; elite feet stay planted but upper torso snaps sideways. Death: afterimage appears briefly on the far side of the beast, then beast collapses into smoke fragments.

Callout: Wordless sharp “Hah!”

Sound: scabbard/steel scrape → crack → simultaneous clustered cuts → one low “thoom” for multiple kills.

Difficulty: S.

SLOT 2 — Thiên Quân Thoái

Code: SAB_S2_QIANJUN

Name: Thiên Quân Thoái — 千军退 — Qiān Jūn Tuì — “Ten Thousand Foes Recoil”

Cooldown: 8 s

WIDE AREA

Source lesson: Where Winds Meet's modao performs broad charged double sweeps with toughness and large-area control, while Nangong Pushe's legendary sabre is remembered as being capable of stirring an entire sky of snow with one cut. 
Gamersky
+1

Fantasy: One grounded cut carries so much momentum that an entire advancing wave physically folds backward.

Area: 20 m radius, 210° frontal sector.

This is intentionally enormous for an 8-second main skill.

40-px silhouette: A single huge ground-hugging white semicircle expands from the hero; very little vertical clutter.

Timeline
F0: 5 m inner shock ring damages and checks the advancing wave.
F2 / 0.033 s: main swing begins visibly.
F4 / 0.067 s: pressure front reaches 10 m.
F7 / 0.117 s: reaches full 20 m.
F10 / 0.167 s: second pressure wake catches surviving beasts.
F18 / 0.300 s: dust wall peaks.
F36 / 0.600 s: dust falling.
F60 / 1.000 s: terrain cut remains only.
Five phases

Charge: Each correct key adds dark pressure ribbons around the cultivator's ankles, always below the tag plane.

Release: F0 foot-stomp sends a local pressure ring before the weapon has visibly completed its swing.

Travel: A massive low white/grey compression front sweeps outward.

Impact: Beasts receive broad directional rim light and physically lean away as a group.

Aftermath: Terrain shows one 20 m curved gouge and a fan of dragged dust.

Screen tier: T2, bordering T3 when it hits a large elite pack.

Beast reaction: The key spectacle is population motion: dozens of beasts simultaneously slide/recoil away from the pass. Small beasts can tumble once. Elites dig feet/claws into terrain, leaving drag marks. Death: body turns to a compressed dark silhouette and bursts horizontally into smoky strips.

Mandarin callout:
“退！” — Tuì!
“Yield!”

Sound layers: foot impact → heavy sabre windup → enormous low pressure roar → dozens of impacts compiled into two layers rather than per-beast spam → gravel drag → death gust.

Difficulty: M.

SLOT 3 — Trấn Quan

Code: SAB_S3_ZHENGUAN

Name: Trấn Quan — 镇关 — Zhèn Guān — “Hold the Pass”

Type: Guard / counter

Suggested cooldown: 10 s.

Source lesson: Where Winds Meet's modao school combines large committed offense with shielding/toughness; player builds explicitly exploit guard and counter interactions rather than treating the heavy blade as pure DPS. 
Gamersky
+1

Fantasy: The cultivator plants the sabre across the pass and becomes, for one instant, a gate no beast can cross.

Area: Self guard; successful counter: 10 m × 150° frontal counter wave.

40-px silhouette: Sabre becomes an unmistakable horizontal dark bar across the hero's body, followed by a V-shaped pressure rebound.

Timeline
F0: guard active.
F0–F27 / 0–0.450 s: guard window.
On successful block:
Counter F0: attacker immediately takes poise damage.
+F2 / 0.033 s: guard shock.
+F5 / 0.083 s: 10 m counter arc.
+F10 / 0.167 s: ground wake.
Failure/unused: stance ends around F32 / 0.533 s.
Five phases

Charge: Typing draws low dust toward the hero rather than away, implying compression.

Release: F0 sabre locks horizontally; dark rectangular pressure plane briefly appears.

Travel: Successful block converts the incoming force into a V-shaped ground shock.

Impact: Enemy's attack sparks backward toward itself rather than toward the player.

Aftermath: Two short trenches form from the hero toward the sides of the counter cone.

Screen tier: T1; T2 on successful elite counter.

Beast reaction: Trash attacker rebounds dramatically; nearby trash gets swept aside. Elite takes a large backward upper-body stagger and visible foot skid. Death: black pressure outline compresses inward, then bursts back toward the beast.

Mandarin callout:
“此关，不退！” — Cǐ guān, bù tuì!
“This pass does not yield!”

Sound: muted inhale → guard clang with very deep body → one frame of near-silence → reversed pressure boom → gravel scrape → death layer.

Difficulty: M.

SLOT 4 — Thập Phương Vô Đào

Code: SAB_S4_WUTAO

Name: Thập Phương Vô Đào — 十方无逃 — Shí Fāng Wú Táo — “No Escape in Ten Directions”

Cooldown: 12 s

FIELD-WIDE — SELF-HUNTING

Sword's hunter dispatches actual celestial weapons.

Sabre's hunter must feel completely different.

There are no floating sabres.

Instead, the cultivator has imposed a roaming law of execution on the battlefield.

Source lesson: Naraka's 百裂斩 sells the fantasy of numerous cuts compressed into an instant, while Nangong Pushe's 十九停 concept turns consecutive “stops” into escalating lethality; descriptions place increasingly extraordinary opponents beneath successive thresholds. 
GamerSky
+1

Fantasy: After one draw, invisible killing pressure roams from pack to pack by itself. No enemy knows where the next cut will appear.

Area: Entire 40 × 26 m field.

Duration: ~4.0 s.

Hunter logic: Divide map into a cheap spatial grid. Every ~0.25–0.30 s, choose the highest-value cluster according to:

enemy density,
unhit priority,
kill probability,
elite weight.

A 9–12 m × 3 m execution plane orients itself through that cluster.

Gameplay target selection is autonomous.

40-px silhouette: The hero sheathes/lowers the weapon and barely moves. Across the map, huge white-black calligraphy cuts appear one after another in different orientations.

That still reads spectacularly with the player only 40 px high.

Timeline
F0: densest enemy cluster immediately receives Cut #1.
F2 / 0.033 s: a dark ring appears under hero, establishing the technique.
F12 / 0.200 s: Cut #2 hunts a new cluster.
Then approximately one logical execution every 15–18 frames.
F240 / 4.0 s: final cut.
F270 / 4.5 s: remaining suspended slash scars dissolve.
Five phases

Charge: While typing, short black-white cutting strokes accumulate behind the cultivator like unfinished calligraphy.

Release: F0: the first distant pack is already cut even though the hero has scarcely moved.

Travel: There is no travelling blade. A thin line appears at the chosen pack and expands into a local execution plane in 1–2 frames.

Impact: Broad white edge, black center, then violently displaced dust/beasts.

Aftermath: Every strike leaves a fading floating brushstroke in space. After several seconds, the map looks briefly like it has been written over by a furious immortal calligrapher.

Screen tier: T3 on F0 only; later executions use local impacts without camera shake.

Beast reaction: This skill must make the wave look terrified: nearby beasts snap their heads toward a previous cut just before another pack elsewhere is hit. Trash is swept sideways. Elites stagger every second or third selection rather than every cut. Death: beast silhouette becomes one rough black brush mark, then tears into drifting ink fragments.

Mandarin callout:
“十方之内——无处可逃！” — Shí fāng zhī nèi—wú chù kě táo!
“Within the ten directions—there is nowhere to flee!”

Sound layers: sheath click → distant first cut immediately → successive directional air fractures that move around the stereo field → heavy clustered impacts → occasional silence gaps → ink/dust decay.

The player's blade itself should become almost silent after F0, emphasizing that the battlefield is now doing the cutting.

Difficulty: M.

This is much cheaper than Sword S4: no persistent weapon population, only cluster selection + temporary cut planes.

SLOT 5 ULTIMATE — Thiên Khuynh Đoạn Giới

Code: SAB_U5_DUANJIE

Name: Thiên Khuynh Đoạn Giới — 天倾断界 — Tiān Qīng Duàn Jiè — “Heaven-Tilting World Sever”

ULTIMATE — Qi bar

MYTHIC WIDE-AREA

Source lesson: Nangong Pushe's sabre mythology is built around escalation toward overwhelming first-strike supremacy, while even an earlier feat is described as one blade stirring the entire snowy sky. The lesson is that peak sabre power should make one committed cut feel categorically more final than twenty ordinary cuts. 
Baidu Knows
+1

Fantasy: The cultivator makes one complete cut. Clouds, battlefield lighting and the enemy horde all appear to slide onto opposite sides of the edge.

Area: Dynamic diagonal execution corridor approximately 36 × 20 m, aligned through the greatest enemy population. It normally covers 70–85% of the battlefield without simply becoming another global AoE.

40-px silhouette: A colossal black-white diagonal boundary traverses almost the entire screen; clouds above it visibly shear in opposite directions.

F0 + cut-in
F0 / 0.000 s: 6 m pressure burst damages nearby beasts and every beast inside the final corridor receives a tiny immediate execution tick/rim flash.
Then freeze game + typing timer for ~0.95 s.
Anime cut-in

0.00–0.25 s: extreme close-up of hand around sabre grip.

0.25–0.50 s: one eye opens; all music drops.

0.50–0.72 s: sabre edge moves perhaps one centimeter from its resting position.

0.72–0.95 s: screen becomes white except for one black diagonal stroke.

Then gameplay resumes.

Gameplay resume
F1 / 0.017 s: world returns, nearly silent.
F3 / 0.050 s: cloud layer shears along corridor.
F5 / 0.083 s: main cut reaches entire 36 m span.
F8 / 0.133 s: dust on opposite sides accelerates in opposite directions.
F11 / 0.183 s: three-frame silence.
F14 / 0.233 s: all beasts reveal cut seams simultaneously.
F18 / 0.300 s: catastrophic compiled damage resolves.
F24 / 0.400 s: surviving elites receive second kneeling/stagger reaction.
F45 / 0.750 s: atmospheric movement resumes.
F120 / 2.0 s: terrain scar still remains.
Five VFX phases

Charge: As typing progresses, atmospheric particles begin drifting sideways toward an invisible diagonal plane. No giant glow.

Release: F0 pressure burst + immediate execution mark.

Travel: After cut-in, there is still no visible projectile—the gigantic boundary appears simultaneously along its entire length.

Impact: Sky/cloud mass visibly offsets by a few pixels/degrees; terrain dust splits; every victim flashes white on one side and black on the other.

Aftermath: A diagonal ground scar smokes faintly. For ~2 s, loose debris on the two sides drifts away from the divide.

Screen tier: T4 Ultimate.

Beast reaction: Nearby F0 victims recoil instantly. Main cut lifts light beasts sideways before they disappear into torn shadow strips. Medium beasts collapse in the cut direction. Elites violently brace, then drop to knee/forelimb at F24. Killed elites remain as dark statues for ~0.25 s with the diagonal seam visible before breaking into heavy black fragments.

Mandarin chant:
“此刀落——天地分！” — Cǐ dāo luò—tiāndì fēn!
“When this sabre falls—Heaven and Earth part!”

Sound layers: compressed low-frequency typing rumble → F0 shock → cut-in scabbard leather/metal detail + heartbeat → total music drop → tiny edge whisper → enormous broadband world-split crack → silence → delayed sub-bass body impact → mass death layer → distant stone collapse.

Difficulty: L because the visual sells itself through full-field atmosphere, cloud displacement, masks and postprocess timing rather than raw mesh count.

The two kits side by side
Slot	Sword	Sabre
Basic	寒芒点魄 — pinpoint sword intent	断尘 — blunt pressure cut
1, one word	一字惊锋 — fast fan of sword qi	掠影 — compressed draw-cut
2, 8 s	七星列锋 — WIDE geometric formation	千军退 — WIDE army-repelling sweep
3	剑心不动 — stillness/parry	镇关 — heavy guard/counter
4, 12 s	万锋听诏 — FIELD-WIDE SELF-HUNTER, autonomous celestial blades	十方无逃 — FIELD-WIDE SELF-HUNTER, autonomous roaming execution cuts
5	一线开乾坤 — heaven divided by sword law	天倾断界 — world divided by one sabre

The critical differentiation is that Sword S4 and Sabre S4 solve the same gameplay requirement without sharing the same fantasy.

Sword gives the player the owner's desired image of a sky full of independently hunting cultivation weapons.

Sabre makes the absence of a projectile frightening: the player sheaths the weapon, yet giant cuts keep materializing wherever the beasts gather.

And their ultimates deliberately finish on opposite emotional notes:

Sword: calm, celestial, precise — one impossibly thin line establishes cosmic authority.

Sabre: violent, final, physical — one cut carries enough intent that the world appears to slide apart.

ChatGPT can make mistakes. Check important info.
Latest response




Thinking effort
High