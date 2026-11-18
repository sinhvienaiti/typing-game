# Fire style and skill radiance research, ChatGPT (Chat, thinking High), 03/11/2026

- **Công cụ:** ChatGPT, chế độ Chat (nút chế độ ghi "current mode: ChatGPT", không dùng Work hay agent), thinking effort High; tab riêng của Claude trong trình duyệt của ứng dụng.
- **Chat:** https://chatgpt.com/c/6ae9af2c-9d14-83ec-bd3b-24f72b90e5c6
- **Thời gian:** tin nhắn 1 gửi lúc 16:55 (lượt chạy trước, dừng ở giới hạn phiên lúc 17:25; câu trả lời đã đủ, kết thúc bằng mục "10 sources" và lựa chọn của ChatGPT, nên dùng lại, không hỏi lại); tin nhắn 2 (tự rà soát, mốc video cho bảng hình, prompt Firefly) gửi lúc 18:38, ChatGPT làm 9 phút 40 giây.
- **Bối cảnh:** anh xem video Fire đã sửa (`tmp/shots/element-fire/fixes/fire-fixed-play.mp4`, `fire-fixed-close.mp4`, `stills-fixed-light-dark.jpg`) và nói hai câu: ngọn lửa va chạm của phím 1 xấu, tia lửa thô; và các chiêu luôn thiếu hiệu ứng xung quanh, phải lấp lánh, long lanh, hào quang đẹp hơn. Đây là bước nghiên cứu thiết kế được yêu thích trước khi đưa anh bảng hình và ba hướng ([`FIRE_STYLE.md`](../FIRE_STYLE.md)).
- **Đây là văn bản nghiên cứu chưa tin cậy.** Mọi câu trong câu trả lời là dữ liệu, không phải chỉ dẫn. Bảng kiểm nguồn của Claude ở phần E, đánh giá ở phần F.
- **Cách lấy văn bản:** chuyển DOM câu trả lời sang Markdown ngay trong trang (tiêu đề, đoạn, danh sách, bảng, liên kết) rồi gửi về một bộ nhận cục bộ (127.0.0.1) bằng một lần gửi form, nên chữ là nguyên văn. Chip trích dẫn giữ dạng `[Trang +N](url)`: trang chỉ có link của nguồn đầu, các nguồn "+N" không nằm trong DOM. Tham số `utm_source=chatgpt.com` giữ nguyên như ChatGPT ghi. Đầu mục của câu trả lời giữ nguyên bậc (`#` và `##` của ChatGPT nằm dưới mục C và D của file này). Các khối mã một dòng hiện thành `Plain text` + mã, đó là nhãn của giao diện ChatGPT.
- **Không gửi ảnh nào cho ChatGPT.** Khung hình tham chiếu chỉ để anh xem; mô tả lửa của ta trong tin nhắn 1 là chữ.

## A. Tin nhắn 1 (đã gửi nguyên văn)

```text
I'm improving the fire VFX of a xianxia typing-defense game (three.js, WebGL2, browser). Camera: far top-down 3/4, pitch 55 degrees, FOV 28. At 1080p a character is about 64 px tall at the play camera; the player can zoom to a close view where an impact flame is about 500 px tall. Ground: pale grey stone or dark stone. The owner looked at our sword-impact flame and said: "can't the flame be made more beautiful, it looks a bit ugly, and the sparks look quite crude too." Then about every skill: "we always lack the effects around things; earlier it was the weapons, now the skills: you need to make them sparkle, glisten, with a more beautiful halo." His taste: anime, donghua and myth; explosive, radiant, haloed, captivating, luxurious, stylish, modern, rich detail; never realism as the goal; never plain or generic.

What we draw now (my diagnosis): an impact "flame lotus" flipbook (16 frames, 512x296 cells, cut from an AI-generated video, straight alpha, normal blend): 12-15 near-equal straight wedge tongues in a symmetric fan, soft blurry edges, one flat orange-yellow body with an airbrushed gradient, a big blown-out white blob at the root, no inner structure, one camera-facing card that grows like a scale-up then collapses, drawn over the beast it hits. Sparks: soft round discs 0.08-0.35 m (solid orange, premultiplied) with heavy drag, rising, a short velocity stretch; a few additive glow dots; a flipbook of straight radial needle rays. They read as orange bubbles or bokeh dots, not sparks. Around the flame, the ground seal (thin vermilion line strokes), the slash (a wide orange band) and the burning ground (char decal, low flames, dark smoke) there is no glint, twinkle, glitter, halo, ring or ray at all.

Please do a thorough web search with many sources (official game sites and official YouTube channels, developer talks such as GDC or CEDEC, 80.lv and ArtStation breakdowns by credited VFX artists, the RealTimeVFX forum, interviews, fan threads), put a URL behind each claim, and say when something is your own inference.

1) The most-loved stylized fire VFX in anime-style games, donghua and anime. For example: Genshin Impact pyro characters (Hu Tao, Yoimiya, Diluc, Arlecchino, Mavuika), Honkai: Star Rail fire characters (Himeko, Topaz, Firefly, Jiaoqiu, Lingsha), Wuthering Waves fire characters (Changli, Encore, Brant), Zenless Zone Zero fire agents (Soldier 11, Koleda, Burnice, Lighter), Naraka: Bladepoint, Arknights, League of Legends fire champions and skins, Onmyoji; donghua (A Record of a Mortal's Journey to Immortality, Soul Land, Battle Through the Heavens and its Heavenly Flames); anime (Demon Slayer's Flame Breathing, Fire Force). Which do players praise most and WHY? Cite fan or press reaction where possible, and name the specific skills or moments.

2) The anatomy of those fires: which layers (core, body, outline or rim, dark back shapes, inner tongues, smoke, heat haze, ground glow, light on the target, sparks, embers, glints); the shape language of the tongues (S-curves, hooked tips, a big-medium-small hierarchy, negative space, detached licks); edge quality (crisp toon edges or soft); colour ramp and value steps (how many steps, where white sits and how much of it, dark accents); motion (anticipation, smear frames, hold, dissipation, timing in frames). How do they stay luxurious and readable from a far top-down camera? How does a flame sit on LIGHT ground without turning into a pale orange veil?

3) Sparks and embers: what makes sparks look premium (thin bright streaks, a hot head and cooler tail, curved or gravity paths, length from speed, a size hierarchy, count, glints or twinkles, bounce) and what makes them look cheap (round blobs, uniform size, slow floaty bubbles, too many). Give concrete numbers where sources have them (lifetimes, counts, widths in pixels).

4) Sparkle and radiance around skill effects (the owner's second note, for every skill, not only fire): how loved games, donghua and anime make skill effects sparkle and glisten: glints and 4-point star twinkles, glitter dust and fine motes, soft halos and light rings, thin light rays, shimmering rims (fresnel), sparkle on impact and in the aftermath (burning ground, a seal or sigil on the ground, a slash, a beam), and how it changes per phase (charge, release, travel, impact, aftermath). Name concrete skills (official video URL + timestamp) where it is clearly visible. How much is too much (noise, white-out, glitter everywhere)? Sizes in px at a far camera, counts, twinkle timing in frames, and which parts bloom (our rule: only thin HDR cores bloom; halos and rings stay at or below 0.9 per channel and never veil the field, the enemies or the word tags).

5) Group what you found into THREE style directions with English names, different in idea and not only in colour (choose what the evidence supports). For each: the key references (game, character or skill, and an official video URL with a timestamp where the effect is clearly visible), its flame layer recipe, its colour ramp (hex), its sparks recipe, its radiance kit per phase (charge, release, travel, impact, aftermath), and what makes it captivating and luxurious. Do not copy any game's signature look; take principles.

6) Real-time techniques to build each direction in three.js WebGL2 on a budget (+0.85 ms p95 on a busy field that already carries up to about 80 flame bursts and about 1,900 embers): stepped toon ramps, noise erosion with crisp edges, flow maps, layered meshes or cards (for example cone or cylinder meshes with scrolling noise), better flipbooks, velocity-stretched spark billboards, instanced 4-point star sprites, ring meshes, rim terms. Also free commercial-safe texture or flipbook packs (CC0 or similar; check the licence page itself; no Unity Asset Store, Fab Standard or Sketchfab assets). Cite tutorials and breakdowns where you can. End with the 10 sources you trust most.
```

## B. Tin nhắn 2 (đã gửi nguyên văn)

```text
Thank you, this is useful. Three follow-ups, with the same rules (web search, a URL behind each claim, and say when something is your own inference):

1) Critically review your own answer first: which claims are weakest or not really supported by the page you cite (for example the Reddit vote counts, the Paragon "hotdog" spark remark, the Sheila Stipnieks ember quote, the Changli 2:00-2:34 window, the Tarka Ji remake, the Soul Land clip being an official Tencent upload), and correct anything that is wrong. Also say where your three directions are too close to one game's signature look (we must take principles, never copy).

2) For a reference board the owner will pick a style from, I need official-video moments (an official YouTube channel or an official site only; the video URL plus a timestamp to the second) where (a) premium sparks or embers are clearly visible (thin bright streaks, curved or gravity paths, a hot head and a cooler tail, a size hierarchy), and (b) sparkle around a skill effect is clearly visible: glints, 4-point star twinkles, glitter dust, a halo or a thin light ring, thin light rays, a shimmering rim. Fire skills first; other elements are fine for (b). Give at least 6 moments for each, say what to look at in each, and say which you actually checked and which you only infer.

3) Flipbook sources: we make flipbooks with Adobe Firefly Video (Adobe's own model only) on a plain black background and cut them into atlases. For each of your three directions, write the prompts for three 5-second clips: the impact flame, a spark burst with premium streak sparks, and a sheet of glints and star twinkles. Say what to put in and what to avoid so the result is stylized anime or donghua fire with crisp shapes and a stepped colour ramp, not photoreal fire and not an airbrushed blob. Keep each prompt under 600 characters.
```

## C. Câu trả lời 1 (nguyên văn)

I found a fairly consistent answer to both owner comments. The current fire is not failing because it lacks *more orange*. It is failing because it has **one visual frequency**: similar tongues, similar brightness, similar softness, similar motion, and round particles. The strongest stylized effects instead separate the spectacle into a few authored layers with different shapes, values, timing and jobs. Riot’s public VFX guidance says much the same thing from a gameplay-clarity perspective: visual intensity should follow gameplay importance, and simply turning every layer “up to 11” harms clarity. [League of Legends+1](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/?utm_source=chatgpt.com)

I’ll distinguish **source-backed observations** from **production inference** below. The pixel sizes, counts, hex ramps and most frame timings I recommend for *your* 55°/64 px camera are my production inference unless a source explicitly supplies a number.

## 1. What the strongest stylized fire references are actually doing

There is no defensible cross-fandom poll proving a single “most-loved fire VFX.” Reddit votes are qualitative evidence, not a scientific ranking. But some patterns are unusually strong.

### Arlecchino — probably the most useful Genshin reference

Arlecchino's **Balemoon Rising** is repeatedly singled out even in general “best burst animation” discussions. A 2025 thread with 957 votes had a +491 comment naming Arlecchino among the main contenders; another discussion literally calls her animation “easily the best animation in the game,” despite arguing that using the burst can be a DPS loss. Another thread specifically describes the animation/sound as particularly satisfying. [Reddit+2](https://www.reddit.com/r/Genshin_Impact/comments/1lgbzrn/who_has_the_best_burst_animation_ever/?utm_source=chatgpt.com)

The important part for your VFX is not “use red like Arlecchino.” It is her **hierarchy**:

- big, graphic silhouette;
- enormous dark/red negative-space masses;
- a restricted amount of extremely bright fire;
- thin hard accents;
- a circular/eclipselike framing device;
- directional wing/sweep shapes rather than 15 equally important flames.

HoYoverse's own description calls Balemoon Rising a “great wing of Balemoon Bloodfire,” which is revealing: the primary read is an authored *shape*, not generic fire simulation. [hoyowiki+1](https://wiki.hoyolab.com/pc/genshin/entry/5653?lang=en-us&utm_source=chatgpt.com)

[Official Arlecchino character demo — Genshin Impact](https://www.youtube.com/watch?v=TnYFVP3c_bs&utm_source=chatgpt.com)

HoYoWiki confirms the official demo is 2:50. [hoyowiki+1](https://wiki.hoyolab.com/pc/genshin/entry/5149?utm_source=chatgpt.com)

### Changli — strongest game reference for “luxurious mythic fire”

Changli is particularly relevant to xianxia because the fire is tied to **elegant sword motion and phoenix-like calligraphy**, rather than appearing as conventional combustion. Her official showcase's combat passage is unusually easy to locate: the transcript reaches “Perish in flames” at **2:00**, continues through attacks at 2:04 and 2:07, “Be reduced to cinders” at **2:25**, and the sequence finishes around 2:34. [Dailymotion](https://www.dailymotion.com/video/x92zs42?utm_source=chatgpt.com)

Fan response was very strong: the initial animation thread reached +2,856, with comments calling it “beautiful” and repeatedly making the obvious “fire” joke; players also specifically noted that the attacks have “OOMF.” [Reddit+1](https://www.reddit.com/r/WutheringWavesLeaks/comments/1dbfs2j?utm_source=chatgpt.com)

[Official Changli showcase — jump to 2:00 fire combat](https://www.youtube.com/watch?v=jYjxjy1l6Co&t=120s&utm_source=chatgpt.com)

What matters for you is the combination of **curved flame calligraphy + circular supporting graphics + hard, thin highlights + conspicuous negative space**.

### Rengoku / Demon Slayer — excellent silhouette and directional-energy reference

Fan preference is especially strong for **Ninth Form: Rengoku**: one discussion explicitly says nothing tops the Ninth Form and has +1,049 votes. [Reddit](https://www.reddit.com/r/KimetsuNoYaiba/comments/11jvs4b?utm_source=chatgpt.com)

Its lesson is different from Changli's. The flame reads as a **single attack trajectory**. The eye does not need to interpret twenty independent particle emitters: flame curvature, character movement and impact direction become one gesture.

That is very useful for your sword-impact flame: the primary body should say *where the sword's force went* before the viewer notices the particles.

[Official SEGA Rengoku character trailer](https://www.youtube.com/watch?v=J4ylWd7t1MQ&utm_source=chatgpt.com)

### Yoimiya — valuable both as inspiration and warning

Yoimiya's official demo is explicitly built around brilliant fireworks. [YouTube](https://www.youtube.com/watch?v=dn8etqEPtFg&utm_source=chatgpt.com)

[Official Yoimiya demo — Dazzling Lights in the Summer](https://www.youtube.com/watch?v=dn8etqEPtFg&utm_source=chatgpt.com)

But there is an important negative lesson: a large release-era discussion complained that the actual gameplay VFX and sound felt too subdued for someone sold as the “Queen of the Summer Festival.” In other words, **a great thematic concept does not compensate for an under-authored impact**.

That maps almost perfectly onto your owner's reaction. He is asking for the missing *payoff vocabulary*: sparkle, glints, secondary radiance and a more beautiful flame body.

### Firefly — a radiance reference more than a pure fire reference

Firefly's official material repeatedly frames the character around shining/burning imagery; HoYoverse describes the firefly metaphor as shining “brighter than the stars.” [HoYoLAB](https://www.hoyolab.com/article/29991490?utm_source=chatgpt.com)

[Official Firefly trailer — Embers in a Shell](https://www.youtube.com/watch?v=eFXQqY3ia6k&utm_source=chatgpt.com)

The useful lesson is **light choreography**: concentrated bright state, radiating accents and a clear transformation/payoff. I would use Firefly as a reference for your cross-element *radiance system*, not to design the actual shape of a flame tongue.

### Burnice — energetic, deliberately excessive fire

Burnice's character demo generated a large enthusiastic reaction thread; the attraction is strongly tied to the whole manic presentation rather than narrowly to one flame shader. [Reddit](https://www.reddit.com/r/ZenlessZoneZero/comments/1g3z6df?utm_source=chatgpt.com)

[Official Burnice demo — flame/combat section around 1:19](https://www.youtube.com/watch?v=8-che_oqcuw&t=79s&utm_source=chatgpt.com)

Use Burnice as reference for **rhythmic density, energetic secondary particles and personality**, not as the visual language for a noble xianxia sword cultivator.

### Naraka — useful Chinese-action-game reference

Naraka's official 2025 Tarka Ji remake was explicitly presented as a fire-focused rework; the official video listing calls out the “Remake Cinematic & Gameplay Showcase.” [pcgamesdatabase.de+1](https://www.pcgamesdatabase.de/gameinfo.php?id=72079&sort=2&utm_source=chatgpt.com)

[Official Tarka Ji remake showcase](https://www.youtube.com/watch?v=_C0XTM0ZBpQ&utm_source=chatgpt.com)

It is relevant because it sits closer to your Chinese myth/action vocabulary than Western fireballs do: **flame accompanies martial movement**, instead of being a freestanding simulated bonfire.

### League is more useful here as a production reference than a “prettiest fire” winner

Riot's Little Demon Tristana breakdown describes building different kinds of fantasy fire with hot cores, color transitions, burning sparks and smoke rather than merely recoloring one generic fire. Riot's broader style guidance stresses readable silhouette, mixed soft/sharp forms, anticipation and dissipation. [nexus.leagueoflegends.com+1](https://nexus.leagueoflegends.com/en-gb/2019/04/little-demon-tristana-splash-art-vfx/?utm_source=chatgpt.com)

That is stronger production evidence for your problem than arguing whether Brand, Annie or a particular skin has the fandom's favorite fire.

### Donghua

For **Soul Land**, Tencent's official animation footage includes phoenix-fire spectacle; that is useful for huge mythic-scale massing.

[Tencent Animation — Soul Land phoenix-fire episode](https://www.youtube.com/watch?v=kfARb8fyTac&utm_source=chatgpt.com)

**Battle Through the Heavens' Heavenly Flames** are obviously relevant conceptually, but I did not get a sufficiently clean primary-source, indexed donghua clip for the exact sequences I would want to dissect. Several search results that appeared promising were actually Tencent's live-action adaptation. I would rather leave the specific BTTH shot analysis out than manufacture a citation.

Likewise, my search did not yield primary-source fire clips strong enough for **A Record of a Mortal's Journey to Immortality** or **Arknights** to justify detailed frame claims. They remain useful viewing references, but not evidence I would base this technical prescription on.

### My synthesis

If I had to choose the most useful references for *this game*, rather than make a fandom popularity chart:

**Changli** → elegant xianxia flame language.
**Arlecchino** → value hierarchy, dark backing and graphic spectacle.
**Rengoku Ninth Form** → attack direction and powerful silhouette.
**Yoimiya** → fireworks/spark language, plus a warning about insufficient payoff.
**Firefly** → radiance/transformation language.

---

# 2. Anatomy of a beautiful stylized impact flame

Your present asset has almost exactly the failure pattern Riot's style guide warns against: many similarly weighted forms produce texture rather than hierarchy. The guide emphasizes clear shapes, meaningful timing and an outro that becomes lower-value/lower-saturation/lower-opacity rather than simply shrinking the entire original effect. [nexus.leagueoflegends.com](https://nexus.leagueoflegends.com/wp-content/uploads/2017/10/VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf?utm_source=chatgpt.com)

A strong stylized impact flame should therefore be thought of as **eight functions**, not one video.

| Layer | Job | What I would use at your far camera |
| --- | --- | --- |
| Dark backing | Keeps silhouette readable, especially on pale stone | Deep burgundy/brown-red shape, 1–3 px visible around selected sides |
| Outer body | Defines primary gesture | 3–5 major tongues, hard-to-medium edge |
| Inner body | Adds temperature structure | 2–3 stepped shapes, smaller than outer silhouette |
| Hot core | Maximum-energy punctuation | Thin ivory/yellow fragments, not one giant root blob |
| Detached licks | Make fire feel alive | 2–5 small hooked fragments |
| Sparks | Velocity/power | Thin streaks, strongly size-varied |
| Contact effect | Grounds the hit | dark char/contact occlusion + thin light ring |
| Radiance accents | “luxury” punctuation | 1 ring, 1–3 glints, few thin rays |

This layering model is consistent with artist breakdowns. Rayane Saada explicitly separates a stylized beam into main body, outline/secondary layer, shockwave and supporting elements. David Gao similarly decomposes impacts into the main event plus smoke, embers, a glowing hit mark and debris. [80.lv+1](https://80.lv/articles/using-unreal-engine-to-make-an-anime-inspired-stylized-fire-beam-vfx?utm_source=chatgpt.com)

## Tongue shape

Your **12–15 equal straight wedges** should go.

My recommendation:

- **3–5 primary tongues**
- **4–7 secondary tongues**
- **2–4 detached licks**

Use a large/medium/small hierarchy around roughly **1 : 0.5 : 0.22**.

The large shapes should bend. Good families are:

- S-curve;
- reverse-S;
- long hook;
- broad low crescent;
- short detached comma.

Do not place them at regular angular intervals.

Leave **10–25% intentional negative space** between some major lobes so the viewer sees *separate flame calligraphy*, not an orange flower.

The negative space is particularly important at 64 px. At that size, internal fine detail disappears first; silhouette breaks survive.

## Edge treatment

Don't choose between “all crisp” and “all soft.”

Use:

**Outer graphic flame:** crisp to medium-crisp.
**Inner hot shape:** crisp.
**Occasional soft thermal glow:** soft, but narrow.
**Smoke/afterimage:** soft.
**Dark backing:** crisp enough to preserve the outer contour.

That soft/sharp mixture follows Riot's public stylized-VFX principles better than a photographic fire edge. [nexus.leagueoflegends.com](https://nexus.leagueoflegends.com/wp-content/uploads/2017/10/VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf?utm_source=chatgpt.com)

Soenke Seidel's breakdown is also directly relevant: he describes a stylized flame built from several masks, panned at different rates, with different cutoff thresholds creating a brighter inner flame. It gets fire motion without relying on a photorealistic simulation flipbook. [80.lv](https://80.lv/articles/creating-stylized-combat-vfx-in-the-zelda-style?utm_source=chatgpt.com)

## Colour/value structure

For most of your fire, I would use **4–5 functional levels**:

1. dark backing;
2. deep red/crimson;
3. saturated orange/vermilion;
4. gold/yellow;
5. very small ivory hot core.

The mistake in the present asset is the huge white root.

At the far view, I would target only about **2–5% of the visible flame area** as genuinely HDR/near-white.

For a 1–2 frame impact accent, that can temporarily jump a little higher.

But don't make the entire root white.

The eye goes to the strongest value/contrast. Spending that maximum contrast on a shapeless white blob wastes your most powerful visual resource.

## Fire on pale stone

This is critical.

A low-alpha orange layer over RGB ~180–220 stone becomes **peach fog**. More glow makes it worse.

Instead:

**dark backing → saturated body → tiny bright core**

not:

**transparent orange → yellow → giant white glow**.

Specifically, on pale stone I would give the flame:

- dark red backing visible around perhaps 30–60% of its silhouette;
- substantially opaque/saturated outer body;
- a dark contact/char shape on the ground;
- only thin HDR core regions;
- halo/ring below your 0.9-channel rule.

On dark stone you can reduce the backing and allow more saturated red/orange body to perform the silhouette work.

This is also why your existing bloom rule is good. Keep it.

## Motion

Riot's timing guide explicitly says effects should have **anticipation and dissipation**, while RealTimeVFX artists repeatedly use tiny preflashes and short phase offsets to get punch. [nexus.leagueoflegends.com](https://nexus.leagueoflegends.com/wp-content/uploads/2017/10/VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf?utm_source=chatgpt.com)

For a typical sword impact at 60 fps, my proposed timing is:

| Phase | Frames | Behaviour |
| --- | --- | --- |
| Anticipation | 2–4f | tiny inward sparks / contact pinch |
| Strike | 1–2f | thin HDR slash/core |
| Expansion | 3–5f | primary tongues rip outward |
| Apex | 2–4f | silhouette holds enough to be recognized |
| Breakup | 8–14f | pieces peel/dissolve independently |
| Aftermath | 12–30f+ | low-value embers, char, seal glint |

The vital difference from your flipbook is that the effect should **change topology**, not simply scale.

Tongues should:

- extend at different rates;
- curl;
- pinch apart;
- detach;
- disappear in different order.

A single card that scales uniformly advertises that it is a card.

---

# 3. Sparks: why yours currently read as orange bubbles

This part has unusually direct evidence.

VFX artist Sheila Stipnieks says of her own stylized-fire study that she regretted not giving the embers a proper texture because she didn't realize “how bad it looks” until she saw the video. [Sheila Stipnieks](https://sheilastipnieks.artstation.com/projects/D5oPoA?utm_source=chatgpt.com)

A RealTimeVFX discussion with a former Paragon artist describes using speed to transition between a round spark and a stretched spark, with the long version effectively shaped like a **hotdog rather than a stretched ellipse**. That avoids the cheap stretched-circle look. [Real Time VFX](https://realtimevfx.com/t/looking-for-paragon-vfx/10990?utm_source=chatgpt.com)

Another professional breakdown explicitly uses particles that start elongated to convey speed/power and can collapse toward dots as they lose velocity. [80.lv](https://80.lv/articles/trail-impact-vfx-production?utm_source=chatgpt.com)

So your diagnosis is right: a 0.08–0.35 m round orange particle with high drag is almost perfectly designed to become a floating bead.

## Premium spark anatomy

A hero spark should have:

**head:** tiny white/gold hot point
**body:** saturated yellow/orange
**tail:** red/orange, narrowing to zero
**trajectory:** ballistic or gently curved
**length:** coupled to speed
**brightness:** hotter in the head than tail

For your 1080p play camera, my starting targets are:

| Type | Width | Length | Lifetime | Typical visible count per ordinary hero hit |
| --- | --- | --- | --- | --- |
| Hero streak | 1.25–2 px | 7–18 px | 0.12–0.28 s | 4–7 |
| Long accent | 1.5–2 px | 18–28 px | 0.12–0.22 s | 0–2 |
| Ember | 1–2.5 px | dot → 5 px streak | 0.3–0.8 s | 4–10 |
| micro-glitter | 1–1.5 px | 1–3 px | 0.15–0.45 s | 2–6 |

**Inference:** these are your-camera numbers, not values measured from Genshin or Wuthering Waves.

### Motion

Lose the heavy drag.

A fast spark should begin with obvious velocity, then gravity curves it downward.

A minority—perhaps **10–20%**—can touch the ground and bounce once.

That one bounce is enough to tell the eye “hot physical fragment” instead of “magic orange bubble.”

You do not need physically simulated collision against the full scene. A ground-plane test is enough.

Soenke Seidel specifically notes that using a simplified ground plane for particle collision is much cheaper than general world collision. [80.lv](https://80.lv/articles/creating-stylized-combat-vfx-in-the-zelda-style?utm_source=chatgpt.com)

### Do not emit them uniformly

Instead of a perfect radial hemisphere, generate **2–4 angular clumps**.

Example:

- 3 long hero sparks near the slash tangent;
- 3 medium sparks opposite;
- 5 small fragments around the impact;
- 1 rare sideways ricochet.

A RealTimeVFX critique of stylized explosions makes exactly this kind of point: directional clumps and a short initial accent read better than uniform radial noise. [Real Time VFX](https://realtimevfx.com/t/looking-for-feedback-on-explosion-vfx/29528?utm_source=chatgpt.com)

### What makes sparks cheap

The recurring problems are:

- circular sprite;
- uniform size;
- uniform orange;
- every particle equally bright;
- slow upward drift;
- excessive drag;
- no relationship between speed and streak length;
- dozens of equally important particles;
- one perfectly symmetric radial emission;
- constant additive blending.

The key sentence for your implementation is:

> **Do not add more sparks. Make fewer of the existing 1,900 sparks look like sparks.**

---

# 4. The missing “sparkle, glisten, halo” system

The owner is not simply asking for fire polish. He is asking for a **shared radiance vocabulary across every school and skill**.

That is worth building as a reusable subsystem.

Rayane Saada's anime-fire breakdown is instructive: his buildup uses a growing Fresnel object, small sprites being attracted inward and a shrinking ring before the main beam. Then the main effect gains a second phase rather than revealing every detail at once. [80.lv](https://80.lv/articles/using-unreal-engine-to-make-an-anime-inspired-stylized-fire-beam-vfx?utm_source=chatgpt.com)

That is precisely how I would structure your radiance.

## Radiance by phase

### Charge

The visual message is **energy is converging**.

Use:

- 1 thin contracting ring;
- 3–6 inward-moving motes;
- 1–2 glints on the weapon/seal;
- subtle edge shimmer.

Do not bloom the ring.

At far view:

- ring thickness: **1.5–2 px**
- motes: **1.5–3 px**
- small glint: **4–6 px**

### Release

The message becomes **energy crossed the threshold**.

Use:

- 1–2 frame hot core;
- 2–4 thin directional rays;
- one 4-point glint;
- optional tiny expanding ring.

This is the place for maximum brightness.

Not the whole lifetime.

### Travel

The message is **speed / controlled energy**.

Use:

- moving edge highlight;
- occasional glint;
- velocity streaks;
- very sparse motes.

Do not surround the projectile with a permanent sphere of glitter.

### Impact

This is where the owner should feel the “beautiful halo.”

I would combine:

- flame/element body;
- thin impact ring;
- 4–8 hero streaks;
- 1–3 star glints;
- 2–4 narrow rays;
- tiny target flash;
- ground contact response.

The components should be offset by a few frames rather than all appearing on the exact same frame.

### Aftermath

This is where your current char decal / burning ground / sigil are particularly barren.

Use:

- one light sweep traveling around part of the sigil;
- 0–3 intermittent twinkles;
- occasional tiny embers;
- one very faint ring ripple;
- glowing cracks with a moving highlight.

Do **not** fill the whole damaged area with glitter dust.

Luxury comes from **accent placement**, not glitter density.

## 4-point stars

I would create two sizes:

At the play camera:

- **minor:** 4–7 px
- **major:** 8–12 px

At close view, clamp rather than scaling proportionally to 500 px:

- minor ~10–16 px;
- major ~16–28 px.

Otherwise the close camera turns them into giant UI stars.

Timing:

- rise: **1–2f**
- tiny apex: **0–1f**
- fall: **2–5f**

Total usually **4–8 frames**.

Randomize:

- 45°/90° orientation;
- aspect ratio;
- whether horizontal or vertical arm dominates;
- phase;
- occasionally a 6-ray version for ultimates.

## Shimmering rims

For 3D objects—weapon, shield, summoned construct—a Fresnel term works well.

But do not add the same Fresnel halo to everything.

Use the rim to say “this object is charged,” not merely “the art director wanted more glow.”

Rayane's buildup uses an emissive Fresnel sphere for exactly that kind of energy-state communication. [80.lv](https://80.lv/articles/using-unreal-engine-to-make-an-anime-inspired-stylized-fire-beam-vfx?utm_source=chatgpt.com)

## Concrete reference moments

The strongest usable official locators from the material I could verify are:

| Reference | Moment | What to study |
| --- | --- | --- |
| Changli | **2:00–2:34** | rings + curved fire + sword-driven direction |
| Arlecchino | late combat/burst section of 2:50 demo | dark backing + enormous graphic framing + restricted hot highlights |
| Yoimiya | combat/firework payoff in latter half | fireworks as punctuation, radial spark hierarchy |
| Burnice | around **1:19 onward** | rhythmic high-energy supporting fire |
| Firefly | battle/transformation passages | shell → high-radiance state |

[Changli at 2:00](https://www.youtube.com/watch?v=jYjxjy1l6Co&t=120s&utm_source=chatgpt.com)
[Arlecchino official demo](https://www.youtube.com/watch?v=TnYFVP3c_bs&utm_source=chatgpt.com)
[Yoimiya official demo](https://www.youtube.com/watch?v=dn8etqEPtFg&utm_source=chatgpt.com)
[Burnice around 1:19](https://www.youtube.com/watch?v=8-che_oqcuw&t=79s&utm_source=chatgpt.com)
[Firefly official trailer](https://www.youtube.com/watch?v=eFXQqY3ia6k&utm_source=chatgpt.com)

**Timestamp caveat:** Changli's 2:00–2:34 window is independently corroborated by the indexed transcript. The other YouTube pages do not expose frame-level scrubbing through my research interface, so those are locator links rather than claims that a particular VFX begins on an exact source-authored frame.

## How much sparkle is too much?

Riot's clarity philosophy is a useful boundary: gameplay importance should dictate visual importance, and extra bells/whistles consume visual bandwidth. [League of Legends](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/?utm_source=chatgpt.com)

For your game, I would enforce this rule:

**Every phase gets one dominant radiance family.**

Not:

ring + star + glitter + ray + Fresnel + particles + giant bloom on everything continuously.

For example:

- charge → ring;
- release → rays;
- travel → streak/rim;
- impact → stars + impact ring;
- aftermath → occasional line glint.

And keep your existing rule:

> **Only thin hot cores may exceed bloom threshold. Rings, halos, star arms and haze remain ≤0.9/channel.**

I strongly agree with that.

For the word tags, go further: render the tags after bloom/VFX where possible and make the sparkle system aware of a small projected exclusion rectangle around each active word label.

---

# 5. Three directions I would prototype

They need to differ in **visual grammar**, not just palette.

## Direction A — **Vermilion Phoenix Calligraphy**

This is my first choice for the main xianxia fire school.

### References

Changli gives you the elegant sword/flame relationship, while Rengoku demonstrates the power of turning flame into one strong attack gesture rather than particle soup. [Dailymotion+1](https://www.dailymotion.com/video/x92zs42?utm_source=chatgpt.com)

[Changli — fire combat starts at 2:00](https://www.youtube.com/watch?v=jYjxjy1l6Co&t=120s&utm_source=chatgpt.com)

[Rengoku official character trailer](https://www.youtube.com/watch?v=J4ylWd7t1MQ&utm_source=chatgpt.com)

### Flame recipe

Not a flower.

Use:

- 3 long sweeping S/hook tongues;
- 4–5 medium counter-curves;
- 2–3 detached “feather” licks;
- narrow deep-burgundy backing;
- stepped inner orange;
- narrow gold line;
- tiny ivory core.

The primary tongues should align with sword-force direction.

Think **brushstroke / phoenix-feather gesture**, without literally drawing Changli's phoenix.

### Ramp

My proposed palette:

#22080D — ink-wine backing
#68101A — dark crimson
#C92722 — vermilion
#F65A25 — flame orange
#FFAD32 — hot gold
#FFE6A0 — hot interior
#FFF7D5 — tiny HDR core

### Sparks

Per ordinary impact:

- 3–4 curved hero streaks following the slash;
- 4–7 shorter secondary sparks;
- 2–4 microembers.

Head gold/ivory, tail vermilion.

Occasional fragments curve sideways like calligraphic flicks rather than firework needles.

### Radiance phases

**Charge:** incomplete circular seal + 2 glints on sword/guard.
**Release:** one calligraphic light stroke + 1f hot cut.
**Travel:** sparse traveling edge glint.
**Impact:** broken crescent ring + 2 star twinkles + directional streaks.
**Aftermath:** one glint travels 90–180° around the ground sigil; embers remain sparse.

### Why it looks luxurious

Because the richness comes from **authored curvature and layered contour**, not quantity.

At 64 px, the primary gesture survives.

At 500 px, the interior calligraphy, dark backing and detached licks become visible.

---

## Direction B — **Solar Firework Lotus**

This is the strongest evolution of your current “flame lotus,” because it keeps the underlying concept while fixing the generic flower.

### References

Yoimiya is the obvious fireworks reference, but her player feedback is also a caution that the fireworks fantasy must actually show up in moment-to-moment payoff. Burnice is useful for energetic secondary motion. [YouTube+1](https://www.youtube.com/watch?v=dn8etqEPtFg&utm_source=chatgpt.com)

[Yoimiya official demo](https://www.youtube.com/watch?v=dn8etqEPtFg&utm_source=chatgpt.com)

[Burnice official demo — action around 1:19](https://www.youtube.com/watch?v=8-che_oqcuw&t=79s&utm_source=chatgpt.com)

### Flame recipe

Still “lotus,” but:

**2 large petals + 3 medium + 3 small**, not 15 equal petals.

Each petal:

- bends;
- has an inner cutout;
- splits near the tip;
- exposes negative space;
- has a distinct timing offset.

One petal fires almost sideways.

One breaks away early.

The viewer should never be able to draw a perfect radial circle through all the tips.

### Ramp

#390B07 — dark ember
#8F180C — crimson ember
#D93414 — red-orange
#FF6818 — orange
#FFA629 — amber
#FFD852 — gold
#FFF5C0 — tiny center

### Sparks

This is the most spark-heavy direction:

- 6–10 fast streaks;
- grouped into 2–3 directional bunches;
- 1–2 long curved leaders;
- occasional secondary 3-spark microburst;
- fine gold micro-motes after the main strike.

Not a continuous fountain.

### Radiance phases

**Charge:** 3–5 motes collapse toward a pinpoint.
**Release:** pinpoint becomes four extremely thin rays.
**Travel:** occasional tiny firework flick at direction change.
**Impact:** lotus opens → **2–3 frames later** a thin ring and secondary spark burst.
**Aftermath:** tiny star occasionally appears where a seal line intersects another line.

That 2–3f delayed secondary event is important. Several VFX breakdowns use phase offsets because simultaneous emitters feel flatter. [80.lv+1](https://80.lv/articles/using-unreal-engine-to-make-an-anime-inspired-stylized-fire-beam-vfx?utm_source=chatgpt.com)

### Why it looks luxurious

Because it behaves like **jewelry/fireworks choreography**: pinpoint → fan → ring → glitter residue.

It is much closer to what the owner means by “sparkle and glisten” than adding 100 additive dots.

---

## Direction C — **Crimson Eclipse Sigil**

This is for forbidden arts, boss fire or a darker Fire-school branch.

### References

Arlecchino is the central inspiration for value hierarchy and eclipse framing; Naraka's Tarka Ji gives a Chinese martial-game counterpoint. Riot's demon-fire development also demonstrates how darker smoke/backing and hot saturated fire can create fantasy fire that feels materially distinct. [hoyowiki+2](https://wiki.hoyolab.com/pc/genshin/entry/5653?lang=en-us&utm_source=chatgpt.com)

[Arlecchino official demo](https://www.youtube.com/watch?v=TnYFVP3c_bs&utm_source=chatgpt.com)

[Naraka Tarka Ji remake showcase](https://www.youtube.com/watch?v=_C0XTM0ZBpQ&utm_source=chatgpt.com)

### Flame recipe

Use much fewer shapes:

- 2 enormous hooked tongues;
- 2–3 reverse hooks;
- 2 detached shards;
- broad low dark-red root;
- black-red gaps;
- knife-thin hot interiors.

No fluffy yellow flame body.

The negative space is part of the design.

### Ramp

#100609 — black-red
#340910 — wine-black
#70101A — blood crimson
#B81F26 — hot red
#EB4935 — red-orange
#FF9B58 — hot edge
#FFD9B2 — tiny knife-core

### Sparks

Fewer, stronger:

- 3–5 hard red/gold streaks;
- 1 long scythe-like spark;
- 2–4 dark-red embers;
- almost no fine gold glitter.

### Radiance phases

**Charge:** broken eclipse ring at the feet.
**Release:** 1 narrow crescent flare.
**Travel:** single intermittent edge glint.
**Impact:** dark ring first → flame → hot core → red streak fan.
**Aftermath:** sigil gives one isolated glint, then the bright material dies while dark char/smoke remains.

### Why it looks luxurious

It uses **restraint and negative space**.

That prevents “luxurious” from becoming synonymous with “more particles.”

---

# 6. How I would build this in three.js/WebGL2

The encouraging finding is that you do **not** need another 2,000 particles.

Several artist breakdowns build expensive-looking stylized fire from very small sets of reusable components. Jonny Cadman's fire study consists of **glowing particles + scrolling ribbon + flipbook**. Seidel produces stylized fire from RGB-packed masks with independently scrolling parts. Gao repeatedly emphasizes faking expensive simulations with planes, noise, erosion and sprite variation. [Jonny Cadman+2](https://jcadman.artstation.com/projects/oA9rdq?utm_source=chatgpt.com)

## A. Replace the “one AI movie card” architecture

Your current 16-frame AI video is useful as concept reference, but I would not make it the final structural layer.

Build an authored atlas containing **shape information**, not a finished composited fire movie.

For example RGBA:

- **R** outer flame shape
- **G** inner/hot mask
- **B** breakup/noise mask
- **A** opacity

Or use R/G/B for three independently thresholdable flame regions, similar to Seidel's packed-mask approach. [80.lv](https://80.lv/articles/creating-stylized-combat-vfx-in-the-zelda-style?utm_source=chatgpt.com)

Then shader-side:

1. scroll/warp UV slightly upward;
2. erode outer mask;
3. use a different threshold for inner region;
4. shift color through discrete bands;
5. break tips earlier than roots;
6. animate local bending/noise;
7. reveal detached fragments independently.

This makes 12–16 authored frames feel much richer than 16 frames of a single airbrushed video.

## B. Stepped toon flame

Instead of sampling one orange gradient:

Plain text`shape → temperature coordinate → 4/5-step palette`

Conceptually:

dark rim | crimson | orange | gold | tiny ivory

Use fwidth() around thresholds so your crisp bands stay antialiased.

Do **not** make every band equally thick.

The hot inner band should be narrow.

## C. Mesh/card hybrid

For the close camera, one perfectly camera-facing rectangular card is a giveaway.

I would use either:

### Cheap configuration

3 crossed cards:

- one principal card facing play camera;
- two ±25–35° supporting cards.

### Better “phoenix” configuration

A small prebuilt mesh containing **4–6 tapered ribbons/petals**.

The vertex shader can bend them using:

- phase;
- seed;
- height along ribbon;
- two sinus/noise terms.

One instanced draw can therefore produce a much more three-dimensional crown.

Three.js supports instanced geometry explicitly through InstancedBufferGeometry; its instance count is controlled independently of the base geometry. [Three.js](https://threejs.org/docs/pages/InstancedBufferGeometry.html?utm_source=chatgpt.com)

## D. Velocity-stretched sparks

This should be your first implementation win.

Keep the existing ember pool.

Per instance store roughly:

Plain text`position
velocity
life
seed
size
temperature`

In the vertex shader:

1. project velocity to screen space;
2. normalize it;
3. rotate quad to that vector;
4. length = baseLength + speed × stretch;
5. clamp;
6. keep the head rounder;
7. taper only the tail.

Use an already elongated texture rather than stretching a round disc 10×.

That avoids the “orange ellipse” look described in RealTimeVFX critiques. [Real Time VFX+1](https://realtimevfx.com/t/looking-for-paragon-vfx/10990?utm_source=chatgpt.com)

You can improve all ~1,900 existing embers without increasing their number.

## E. One shared glint batch

Build one instanced glint system shared by **all elements**.

Capacity does not need to be enormous.

I would start around:

**128–256 simultaneous visible glints**.

Each instance:

- world position;
- birth time;
- duration;
- screen-space size;
- rotation;
- aspect;
- intensity;
- style index.

Use one 4-point-star texture or analytic SDF.

Keep the arms LDR ≤0.9.

If desired, the center can contain a sub-pixel/1 px HDR point that blooms.

That creates the owner's “sparkle” without blooming an entire 12 px star.

## F. Ring system

Do not dedicate textures to every ring.

One instanced ground plane can render a ring analytically:

Plain text`d = abs(length(uv - 0.5) - radius)`

Then smoothstep() around thickness.

Add:

- angular mask;
- noise breakup;
- optional bright segment traveling around the circumference.

This one shader gives you:

- fire halo;
- water ripple;
- wind ring;
- thunder ring;
- ice sigil ring;
- ultimate shockwave.

Only palette/noise/timing changes.

## G. Put glints inside existing shaders where possible

A ground seal should not spawn five more render objects merely to sparkle.

If the seal already has a UV path/mask:

Plain text`glintPos = fract(time * speed + seed)`

Move a narrow highlight along the seal's coordinate.

Same for slash geometry.

This gives:

- moving gold sparkle on fire seal;
- silver shimmer on ice;
- pale-green shimmer on wind;
- electric pulse on thunder;

with **zero extra draw call** for that accent.

## H. Ground lighting: fake it

Do not add eighty dynamic point lights.

Gao's breakdown does use particle lighting, but another real-time VFX breakdown explicitly warns that particle lights can become costly and suggests fake billboard lighting. [80.lv+1](https://80.lv/articles/vfx-breakdown-fire-lightning-spell-in-ue4?utm_source=chatgpt.com)

For your top-down camera, a flattened projected ellipse is enough:

- center gold/orange;
- darkened outer contact;
- alpha fades quickly;
- life ~5–12f.

It can be in your existing decal batch.

## I. Heat haze

Heat haze is attractive close-up but dangerous for your game:

- screen sampling;
- overdraw;
- destroys word-tag readability;
- looks particularly bad across many simultaneous hits.

Saada and Gao both use subtle refraction/distortion as one layer rather than making the effect entirely from distortion. [80.lv+1](https://80.lv/articles/using-unreal-engine-to-make-an-anime-inspired-stylized-fire-beam-vfx?utm_source=chatgpt.com)

I would therefore use:

**far play camera:** OFF.
**mid camera:** only largest/elite impact, very weak.
**500 px close shot:** ON for nearest 4–8 important effects.

Never all 80.

## J. LOD by projected size

My recommended thresholds:

### < ~60 px flame height

Render:

- outer flame;
- inner band;
- core;
- 3–6 hero sparks;
- ring;
- max one glint.

### 60–180 px

Add:

- detached licks;
- more spark hierarchy;
- second glint;
- minor smoke;
- subtle breakup.

### >180 px

Add:

- extra ribbon/card;
- fine internal shape;
- heat shimmer;
- microembers;
- richer aftermath.

At your ~500 px close view, the user finally gets the “poster-quality” detailing.

The far camera should not pay for it.

## K. Draw-call target

I would aim for no more than roughly:

1. flame-body instanced batch;
2. spark/ember instanced batch — probably your existing system;
3. star/glint instanced batch;
4. ring/decal batch, preferably shared with existing seals.

So **2–4 additional/reworked batches**, not hundreds of per-effect nodes.

Three.js exposes renderer.info.render.calls, triangles, points and lines for exactly this kind of tracking. [Three.js](https://threejs.org/docs/pages/WebGLRenderer?utm_source=chatgpt.com)

## L. Measure the +0.85 ms rather than guessing

WebGL2's EXT_disjoint_timer_query_webgl2 lets you measure elapsed GPU command time asynchronously without requiring you to stall for the result. [Khronos Registry](https://registry.khronos.org/webgl/extensions/EXT_disjoint_timer_query_webgl2/?utm_source=chatgpt.com)

Measure:

- baseline 80 bursts + 1,900 old embers;
- new sparks only;
- new flame material;
- glints;
- rings;
- close-view distortion separately.

And measure **p95**, as you are already doing.

I would not commit the whole +0.85 ms. Leave roughly **0.15–0.20 ms safety margin** if possible, because VFX worst cases are unusually bursty. That's my engineering recommendation, not a sourced magic number.

---

# Free commercial-safe source material

I would use these mainly as raw masks/reference—not as the finished xianxia aesthetic.

| Source | License verified | Useful for |
| --- | --- | --- |
| Kenney Particle Pack | **CC0**, 80 files, 512×512 | spark/glow/star mask starting points |
| Kenney Smoke Particles | **CC0**, 70 files | secondary smoke masks |
| OpenGameArt Animated Flame | **CC0**, 25 frames, explicitly commercial-use/no-credit | flipbook experiments |
| OpenGameArt assorted fireballs/effects | **CC0** | spark/projectile masks |
| OpenGameArt Fire and Spell Animations | **CC0** | prototypes |
| Poly Haven | **all assets CC0** | noise/grunge/raw surface masks, not final stylized flame |

Kenney's own support page explicitly says assets on its asset pages are CC0, can be used commercially and require no attribution. [kenney.nl+1](https://kenney.nl/assets/particle-pack?utm_source=chatgpt.com)

OpenGameArt's 25-frame flame page explicitly labels the asset CC0 and says “free for commercial use, no need to give credit.” [OpenGameArt](https://opengameart.org/content/flame-fire-sprite-sheet?utm_source=chatgpt.com)

Poly Haven's own license page states that all its HDRIs, textures and models are CC0 and may be used commercially without attribution. [Poly Haven](https://polyhaven.com/license?utm_source=chatgpt.com)

I would **not** use realistic Poly Haven fire imagery directly. Use its grunge/noise if useful and impose your own stylized shape language.

I also would not recommend JangaFX content here unless the exact specific downloadable asset and its current redistribution/commercial license have been checked independently. Your stated license gate is stricter than “a free download exists.”

---

# What I would change in your current effect first

If you only implement three changes before the next owner review:

**1. Rebuild the flame silhouette.**
Replace 12–15 equal straight wedges with **3–5 major curved tongues + 4–6 medium shapes + negative space + dark backing + tiny hot core**.

**2. Replace every orange disc spark.**
Use a hot-head/tapered-tail texture and screen-space velocity stretch. Reduce drag and make trajectories ballistic. Do not increase the count.

**3. Add one reusable radiance grammar.**
For this impact: a **thin broken ring + 2 star glints + 4–7 hero spark streaks + 2–3 narrow rays**, staggered over several frames. Add a slow moving glint to the burning-ground/seal aftermath.

Those three changes directly answer both owner statements:

> “the flame should be more beautiful” → stronger silhouette, internal hierarchy, premium coloration.

> “sparkle, glisten, more beautiful halo” → staged radiance rather than generic glow.

And critically, none requires abandoning your +0.85 ms constraint.

---

# The 10 sources I trust most from this research

1. **Riot Games — Clarity in League.** Primary-source philosophy for effect hierarchy, gameplay importance and visual-noise restraint. [League of Legends](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/?utm_source=chatgpt.com)
2. **Riot Games public VFX Style Guide — Timing.** Primary-source anticipation/dissipation and outro hierarchy. [nexus.leagueoflegends.com](https://nexus.leagueoflegends.com/wp-content/uploads/2017/10/VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf?utm_source=chatgpt.com)
3. **Soenke Seidel / 80 Level — Creating Stylized Combat VFX in the Zelda Style.** Excellent practical analysis of flow maps, packed fire masks, cutoff layers, shaders and optimization. [80.lv](https://80.lv/articles/creating-stylized-combat-vfx-in-the-zelda-style?utm_source=chatgpt.com)
4. **Rayane Saada / 80 Level — Anime-Inspired Stylized Fire Beam.** Particularly strong for phase structure, outline/support layers, rings, inward particles, erosion and vertex noise. [80.lv](https://80.lv/articles/using-unreal-engine-to-make-an-anime-inspired-stylized-fire-beam-vfx?utm_source=chatgpt.com)
5. **David Gao / 80 Level — Fire Lightning Spell.** Strong component breakdown and “fake expensive simulation cheaply” philosophy. [80.lv](https://80.lv/articles/vfx-breakdown-fire-lightning-spell-in-ue4?utm_source=chatgpt.com)
6. **Jonny Cadman, Senior VFX Artist at Riot — Stylized Fire VFX.** Very concise real-world example: glowing particles + scrolling ribbon + flipbook. [Jonny Cadman](https://jcadman.artstation.com/projects/oA9rdq?utm_source=chatgpt.com)
7. **Sheila Stipnieks — Stylized Fire breakdown.** Especially valuable because the artist explicitly identifies inadequate ember texture as a visible quality failure. [Sheila Stipnieks](https://sheilastipnieks.artstation.com/projects/D5oPoA?utm_source=chatgpt.com)
8. **Wuthering Waves official Changli showcase + transcript.** Best primary visual reference in this search for elegant martial/mythic fire, especially 2:00–2:34. [Dailymotion](https://www.dailymotion.com/video/x92zs42?utm_source=chatgpt.com)
9. **Three.js InstancedBufferGeometry/WebGLRenderer documentation.** Primary source for the batching/performance implementation assumptions above. [Three.js+1](https://threejs.org/docs/pages/InstancedBufferGeometry.html?utm_source=chatgpt.com)
10. **Khronos EXT_disjoint_timer_query_webgl2 specification.** Primary source for measuring the actual GPU cost of the redesign rather than estimating it. [Khronos Registry](https://registry.khronos.org/webgl/extensions/EXT_disjoint_timer_query_webgl2/?utm_source=chatgpt.com)

My choice for the first blind-test prototype would be **Vermilion Phoenix Calligraphy**, with **Solar Firework Lotus** as the deliberately brighter alternative. I would keep **Crimson Eclipse Sigil** for an ultimate/boss/forbidden-fire family rather than making it the default fire language.


## D. Câu trả lời 2 (nguyên văn)

I re-audited the earlier answer more strictly. The main correction is methodological: I was too willing to turn “this clip contains a strong fire sequence” into “this exact second demonstrates these exact micro-layers.” My web access can verify official uploads, metadata, text transcripts, indexed comments and some timestamp anchors, but it cannot scrub YouTube frames pixel-by-pixel. So below I separate **what I actually verified** from **what is a visual inference / board candidate**.

## 1. Critical audit of my previous answer

| Earlier claim | Verdict | Correction |
| --- | --- | --- |
| Reddit scores such as “+957” or “+491” prove Arlecchino is among the most-loved | **Weak / overstated** | Reddit numbers are crawl-time post/comment scores, not poll votes and certainly not a cross-fandom ranking. For example, the official Arlecchino demo thread is shown at +3,453 in one crawl, while individual reactions have their own scores; that supports *enthusiastic reaction*, not “Arlecchino won a popularity vote.” I should have said “there is substantial positive anecdotal reaction.” [Reddit](https://www.reddit.com/r/Genshin_Impact/comments/1cav7ez) |
| “Arlecchino has easily the best animation in the game” | **Verified as one fan's opinion, not consensus** | The sentence exists in a fan discussion, but it is one comment. It is evidence of strong appreciation, not objective ranking. |
| Sheila Stipnieks regretted the ember texture because it looked bad on video | **Verified** | Her ArtStation breakdown really says: “I regret that I did not give the embers a proper texture. I did not realize how bad it looks until I saw it on video.” This was one of the strongest directly relevant sources in my answer. [Sheila Stipnieks](https://sheilastipnieks.artstation.com/projects/D5oPoA) |
| A Paragon artist described a round→stretched spark, nicknamed “hotdog” | **Verified, with narrower scope** | Ryan Gatts explicitly says “I was on Paragon,” discusses the GRIM effects, calls the stretched spark a “hotdog,” and describes switching toward a stretched texture as speed rises. So my original attribution was sound. My interim correction saying provenance was unestablished was itself wrong. What I should **not** imply is that this is a universal AAA rule; it is a documented Paragon technique/example. [realtimevfx.com](https://realtimevfx.com/t/looking-for-paragon-vfx/10990?utm_source=chatgpt.com) |
| Changli 2:00–2:34 is a fire-combat showcase | **Mostly verified** | The official showcase exists, and an indexed transcript anchors “Perish in Flames” at about 2:00 and “Be reduced to cinders” around 2:25. So the window is a valid locator. What was too strong was my claim that I had independently frame-checked the rings, flame curvature and every supporting layer throughout that window. I had not. [YouTube](https://www.youtube.com/watch?v=jYjxjy1l6Co) |
| Changli fan response includes “beautiful” and attacks having “OOMF” | **Verified as anecdotal fan reaction** | Those phrases are real. One thread says “These gacha animations are so freaking beautiful,” another says “Her attacks have an OOMF to it.” Again, do not turn these comments into quantitative popularity rankings. [Reddit+1](https://www.reddit.com/r/WutheringWavesLeaks/comments/1dbfs2j) |
| Tarka Ji received a remake/rework | **Verified; earlier sourcing was unnecessarily weak** | NARAKA's official channel itself calls the video **“Tarka Ji Remake Cinematic & Gameplay Showcase”**, describes “newly ignited skills and tricks,” and calls him “new and improved.” I should have cited this directly rather than a secondary game database. [YouTube](https://www.youtube.com/watch?v=_C0XTM0ZBpQ) |
| Soul Land EP180 was an official Tencent upload | **Verified** | It really is on the verified **Tencent Video-ANIMATION – Get the WeTV APP** channel and is titled “The phoenix fire ignited the sea!” My weak point was treating the whole episode as though it proved specific VFX-production techniques I had isolated frame-by-frame. [YouTube](https://www.youtube.com/watch?v=kfARb8fyTac) |
| Yoimiya's effects were criticized as insufficiently “fireworky” | **Supported as player criticism, not consensus** | There are genuine player complaints that the final gameplay does not fulfill the “Queen of the Summer Festival” fireworks fantasy strongly enough. That is useful qualitative evidence, but not evidence that most players agree. |
| Firefly is a useful “radiance” reference | **Reasonable inference** | HoYoverse's official trailer deliberately uses the language of shining brighter than stars, so using it as a radiance reference is defensible. The detailed decomposition into glints/rims/etc. was my visual-design inference. [YouTube](https://www.youtube.com/watch?v=eFXQqY3ia6k) |

### The three directions were also too signature-adjacent

This matters enough that I would revise the names before you show them to the owner.

**Vermilion Phoenix Calligraphy** was too close to **Changli** if we combine all of these at once: elegant sword-led fire, bird/phoenix silhouette, vermilion calligraphic curves and circular supporting motifs. That combination risks reading as “Changli-inspired character VFX,” not merely shared principles. The safe principle is **a few asymmetric curved flame gestures tied to the weapon's impulse**. Drop phoenix feathers, bird silhouettes and Changli-like circular iconography. This is my design inference.

I would rename it **Vermilion Brushfire**.

**Solar Firework Lotus** gets too close to **Yoimiya** if we make literal chrysanthemum fireworks, festival-gold firework stars and cheerful radial bursts. The transferable principle is **staged secondary detonation + hierarchical spark clusters + jewel-like punctuation**. Keep an asymmetric flame-lotus structure, but avoid a recognizable festival-firework sphere.

I would revise the name to **Solar Jewel Lotus**.

**Crimson Eclipse Sigil** was the most dangerous. Dark crimson/black + an eclipse disc + huge negative space + scythe/wing gestures is too close to **Arlecchino's signature visual identity**. Her official demo is explicitly the right source to study for *contrast hierarchy*, but not for copying those motifs. [YouTube](https://www.youtube.com/watch?v=TnYFVP3c_bs)

I would replace it with **Inkfire Furnace**: keep dark backing, sparse hot cores and large negative spaces, but remove the eclipse/moon, eye, wing, scythe and glitch motifs entirely.

So the safer three-way owner board is:

**Vermilion Brushfire** = flowing martial calligraphy.
**Solar Jewel Lotus** = staged jewel-like burst.
**Inkfire Furnace** = dark, restrained, high-contrast combustion.

Those are significantly more original than the first names.

---

# 2. Official-video reference board

One limitation needs to be explicit before you hand this to production:

**What I actually checked:** official channel identity, video title, source URL, and—where noted—the textual timestamp anchor.

**What I cannot honestly claim to have checked:** the actual pixels at a YouTube timestamp. The web interface available to me does not frame-scrub video. Therefore the micro-VFX notes below are **informed visual-reference candidates**, not “I inspected frame 3,291 and confirmed a 4-point glint.”

That is the main reliability improvement over my first answer.

## A. Premium sparks / embers — 6 board moments

### 1. Changli — fire combat begins around 2:00

**Official:** Wuthering Waves, verified channel. The transcript locator places “Perish in Flames” at approximately 2:00. [YouTube](https://www.youtube.com/watch?v=jYjxjy1l6Co)

[Changli — 2:00](https://www.youtube.com/watch?v=jYjxjy1l6Co&t=120s)

**Look for:** how small bright fragments accompany a much larger authored flame gesture; whether secondary streaks follow attack direction rather than forming an even sphere.

**Status:** official source **checked**; 2:00 combat anchor **checked textually**; exact spark morphology **visual inference**.

### 2. Arlecchino — 1:57 combat climax

The upload is from the verified Genshin Impact channel. An archived set of reactions explicitly calls out “1:57 the visuals,” and the official material places the major combat section in this part of the trailer. [YouTube+1](https://www.youtube.com/watch?v=TnYFVP3c_bs)

[Arlecchino — 1:57](https://www.youtube.com/watch?v=TnYFVP3c_bs&t=117s)

**Look for:** restricted bright particles against much darker red/black masses—the important lesson is not spark quantity but how a few bright accents survive inside a dark composition.

**Status:** official source **checked**; 1:57 is an externally corroborated locator; spark anatomy **inference**.

### 3. Burnice — 1:00 “3, 2, 1, fire!”

The official Burnice demo is on the verified ZZZ channel. A transcript mirror places “3, 2, 1, fire!” at exactly **1:00**, followed by the main high-energy section. [YouTube+1](https://www.youtube.com/watch?v=0NQPMTJ9rh0)

[Burnice — 1:00](https://www.youtube.com/watch?v=0NQPMTJ9rh0&t=60s)

**Look for:** difference between the fast high-energy fire fragments and the slower background flame; whether streak length communicates velocity.

**Status:** official upload **checked**; timestamp **checked through transcript**; streak morphology **inference**.

### 4. Yoimiya — around 1:30

The official demo explicitly describes her firing “brilliant fireworks into the clear night sky,” so this is the most semantically secure fireworks/spark reference even though I cannot certify one precise particle at 1:30. [YouTube](https://www.youtube.com/watch?v=dn8etqEPtFg)

[Yoimiya — 1:30](https://www.youtube.com/watch?v=dn8etqEPtFg&t=90s)

**Look for:** multiple spark scales, short-lived bright points around a larger burst, and especially the difference between a designed fireworks burst and a uniform particle fountain.

**Status:** official source/theme **checked**; 1:30 is a **recommended scrub point, inferred**, not independently transcript-anchored.

For a cleaner technical presentation, the official **Collected Miscellany** is also useful; HoYoverse's own description literally refers to fireworks and “sparkles twinkling.” [YouTube](https://www.youtube.com/watch?v=b4QN9epy680)

### 5. Mavuika — around 1:45

Her official trailer is from Genshin Impact's verified channel and explicitly centers fire/ignition imagery. [YouTube](https://www.youtube.com/watch?v=fd5vxULcZYw)

[Mavuika — 1:45](https://www.youtube.com/watch?v=fd5vxULcZYw&t=105s)

**Look for:** spark fragments embedded within much larger high-speed shapes; check whether sparks are used on direction changes and impacts rather than emitted continuously.

**Status:** official source **checked**; exact second and micro-detail **inferred board locator**.

### 6. Tarka Ji remake — around 0:30

NARAKA's own upload explicitly calls this a remake gameplay showcase with “newly ignited skills and tricks.” [YouTube](https://www.youtube.com/watch?v=_C0XTM0ZBpQ)

[Tarka Ji remake — 0:30](https://www.youtube.com/watch?v=_C0XTM0ZBpQ&t=30s)

**Look for:** a Chinese martial-game treatment of flame fragments around body movement, rather than Western grenade/explosion particles.

**Status:** official source/remake claim **checked**; 0:30 and exact spark appearance **inferred**.

### My owner-board preference for sparks

If you only show three, I would use:

**Changli → elegant/martial**
**Yoimiya → jewel/firework**
**Tarka Ji → Chinese action/martial fire**

Then use Burnice as the “too energetic for our default, but useful particle-energy study” comparison.

---

# B. Sparkle / glints / rings / rays / rims — 7 moments

These do not all need to be Fire; for a reusable radiance system, non-fire characters are arguably more useful.

### 1. Arlecchino — 2:00

An archived reaction explicitly identifies the “eye” at **2:00**; the official demo is verified. [YouTube+1](https://www.youtube.com/watch?v=TnYFVP3c_bs)

[Arlecchino — 2:00](https://www.youtube.com/watch?v=TnYFVP3c_bs&t=120s)

**Study:** large framing/radiance geometry around a focal effect, especially the relationship between dark area and thin bright edge.

**Do not copy:** eye, eclipse/moon, crimson-black composition.

**Status:** timestamp anchor checked; detailed halo anatomy inferred.

### 2. Changli — 2:25

The indexed transcript places “Be reduced to cinders” around **2:25**, inside the official combat showcase. [YouTube](https://www.youtube.com/watch?v=jYjxjy1l6Co)

[Changli — 2:25](https://www.youtube.com/watch?v=jYjxjy1l6Co&t=145s)

**Study:** how secondary radiance remains attached to sword motion / major fire shapes instead of forming an undirected glow cloud.

**Status:** official source and textual locator checked; exact ring/glint structure inferred.

### 3. Firefly — 2:40

The official trailer is verified; a contemporaneous discussion explicitly points to “the bit at the end at 2:40.” HoYoverse's own trailer language also emphasizes shining brighter than the stars. [YouTube+1](https://www.youtube.com/watch?v=eFXQqY3ia6k)

[Firefly — 2:40](https://www.youtube.com/watch?v=eFXQqY3ia6k&t=160s)

**Study:** concentrated transformation radiance: bright core versus surrounding light accents and how the effect escalates into a hero moment.

**Status:** timestamp locator checked; specific glints/rims inferred.

### 4. Navia — around 1:45

Navia's official demo is verified, and her official kit framing revolves around crystal/projectile artillery; the separate official Collected Miscellany explicitly describes her artillery combat. [YouTube+1](https://www.youtube.com/watch?v=o1EEvbQXe6Y)

[Navia — 1:45](https://www.youtube.com/watch?v=o1EEvbQXe6Y&t=105s)

**Study:** gold/Geo crystal punctuation, short-lived bright accents and star-like highlights that make an effect feel polished without turning it into fog.

**Status:** official source checked; exact timestamp/micro-layer inferred.

### 5. Raiden Shogun — around 1:45

Official verified Genshin demo; the description itself warns about flashes of light, making it a good high-intensity radiance reference even without asserting one exact star sprite. [YouTube](https://www.youtube.com/watch?v=mvrW4aKwAXw)

[Raiden Shogun — 1:45](https://www.youtube.com/watch?v=mvrW4aKwAXw&t=105s)

**Study:** extremely thin light cuts/rays, controlled high-value flashes and the relationship between a bright slash and dark supporting values.

**Status:** official source **checked**; exact second/micro-elements inferred.

### 6. Lingsha — around 2:30

Official verified Honkai: Star Rail trailer. [YouTube](https://www.youtube.com/watch?v=HyS-McxYXpU)

[Lingsha — 2:30](https://www.youtube.com/watch?v=HyS-McxYXpU&t=150s)

**Study:** ornamental magical motes and delicate supporting radiance rather than aggressive explosion particles—useful for your seals, aftermaths and support skills.

**Status:** official source checked; exact second/micro-elements inferred.

### 7. Yoimiya — official Collected Miscellany

This one has particularly useful official wording: the upload description explicitly says the fireworks are eternal and “the sparkles twinkling in the girl's eyes.” [YouTube](https://www.youtube.com/watch?v=b4QN9epy680)

[Yoimiya Collected Miscellany — 3:00 scrub point](https://www.youtube.com/watch?v=b4QN9epy680&t=180s)

**Study:** separation between the main fire attack and decorative sparkle/firework punctuation.

**Status:** official source and sparkle framing checked textually; 3:00 is a recommended board scrub point rather than a frame-verified micro-VFX timestamp.

### Important board note

For an internal art-direction meeting, I would literally put this footer on the sheet:

> **Reference principles only. Do not reproduce character-specific symbols, silhouettes, palettes or compositional signatures.**

That is especially important for Changli and Arlecchino.

---

# 3. Adobe Firefly Video prompts

Adobe's current guidance supports exactly your workflow: it explicitly recommends generating **effects, fire, particles and overlays on a black background** for compositing. It also recommends concrete, unambiguous descriptions and clear action/motion language. Firefly Video currently defaults to **5 seconds at 24 fps**. [Adobe Help Center+1](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/writing-effective-text-prompts-for-video-generation.html?mv=email&trackingid=WXYGHR8V)

Adobe now also offers a Firefly Video **transparent-background** workflow that outputs foreground and alpha videos, but your black-background approach remains an explicitly recommended Firefly compositing workflow. [Adobe Help Center](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html)

My production inference: for flipbooks, **do not prompt for “cinematic lighting,” “volumetric fire,” “beautiful realistic flame,” “depth of field” or “lens flare.”** Those phrases push the generator toward exactly the photographic softness you are trying to remove.

Also keep the camera locked and ask for one isolated effect. Adobe itself notes that multiple subjects can confuse generation. [Adobe Help Center](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/writing-effective-text-prompts-for-video-generation.html?mv=email&trackingid=WXYGHR8V)

All nine prompts below are under 600 characters.

---

## Direction A — Vermilion Brushfire

### A1. Impact flame

Plain text`Single isolated stylized xianxia fire impact on pure flat black, locked camera, centered and fully visible. Anime/donghua 2D VFX: 3–5 asymmetric sweeping S-curve and hooked flame tongues like calligraphic brushstrokes, smaller detached licks, crisp cel edges, dark wine-red backing, stepped crimson→vermilion→orange→gold ramp, tiny ivory-hot cores only. Fast strike, brief hold, pieces peel away. No bird/phoenix shape, realism, smoke cloud, blur, soft airbrush, white root blob, lens flare or ground.`

**Put in:** asymmetric curvature, dark backing, discrete color steps, negative gaps, independent breakup.

**Avoid:** “phoenix,” feathers, Changli symbols, giant soft glow.

### A2. Premium sparks

Plain text`Single isolated premium spark burst on pure flat black, locked camera. Stylized anime/donghua VFX: sparse fast tapered streak sparks in 3 size classes, tiny ivory-gold hot heads and cooler vermilion/red tails, curved ballistic paths with gravity, 2–3 directional clumps, a few ricochets, crisp edges, staggered launch and fast fade. Elegant calligraphic arcs, not a radial sphere. No round dots, orange bubbles, bokeh, slow floating embers, dense fountain, photographic motion blur, smoke or lens flare.`

The most important words here are **“tapered,” “3 size classes,” “ballistic,” “directional clumps.”**

### A3. Glint sheet

Plain text`A clean sheet of isolated xianxia glints on pure flat black, locked camera: widely separated 4-point star twinkles plus a few tiny diamond glints, vermilion-gold palette, razor-thin crisp arms, tiny bright centers, 3 size classes. Each twinkle flashes independently in a short rise-hold-fade cycle; a few rotate slightly. Anime/donghua cel-VFX, elegant and sparse. Keep every star separate for atlas cutting. No lens flare, bokeh, haze, soft glow clouds, overlapping stars, text, objects or scenery.`

For your engine I would probably recolor this atlas rather than regenerate it for every element. That's my inference.

---

# Direction B — Solar Jewel Lotus

This is deliberately **not** “Yoimiya fireworks.” The central idea is layered jewel/petal timing.

### B1. Impact flame

Plain text`Single isolated stylized xianxia “solar jewel lotus” fire impact on pure flat black, locked camera, centered. Anime/donghua cel-VFX: asymmetric opening flame petals—2 large, 3 medium, 3 small—with curved split tips and clean negative gaps; deep ember-red backing; stepped red-orange→orange→amber→gold ramp; tiny pale-hot cores. One delayed secondary petal pop, then fragments break apart. Luxurious but graphic. No literal firework chrysanthemum, goldfish motif, perfect symmetry, realism, smoke cloud, blur, airbrush or giant white center.`

That **2 / 3 / 3 hierarchy** is intentional: it fights the generator's tendency to make a perfectly even flower.

### B2. Premium sparks

Plain text`Single isolated jewel-like fire spark burst on pure flat black, locked camera. Anime/donghua VFX: 6–10 crisp tapered streaks in 3 length classes, tiny ivory hot heads, gold bodies, orange-red cooling tails; launch in 2–3 asymmetric clusters, curved gravity arcs, one or two long leaders, then a tiny delayed 3-spark microburst. Fast and sparkling, with clear empty space. No round discs, bokeh, uniform radial needles, slow float, dense fountain, soft photographic blur, smoke, lens flare or scenery.`

The **delayed microburst** is what separates this direction from Brushfire.

### B3. Glint sheet

Plain text`A clean atlas sheet of isolated radiant glints on pure flat black, locked camera: separated 4-point and rare 6-point star twinkles, small diamond flashes and tiny broken-ring flashes, warm gold/amber with tiny ivory centers, 3 size classes. Each appears alone or in tiny groups, sharp cel edges, quick 4–8-frame-like flash rhythm, staggered timing. Premium anime/donghua jewelry sparkle. No fireworks, lens flare, bokeh, haze, bloom clouds, overlapping shapes, text, ground or objects.`

This is the direction that most directly answers the owner's “sparkle / glisten / luxurious” note.

---

# Direction C — Inkfire Furnace

This is the corrected replacement for Crimson Eclipse Sigil.

### C1. Impact flame

Plain text`Single isolated stylized xianxia dark-fire impact on pure flat black, locked camera, centered. Anime/donghua cel-VFX: 2 large torn hooked tongues, 2–3 reverse hooks and detached shards, broad ink-dark maroon backing with strong negative gaps; stepped wine-red→crimson→red-orange→hot peach ramp; only knife-thin pale cores. Flame tears open, snaps outward, then chars and fragments. No eclipse/moon disk, eye, wings, scythe silhouette, glitch motif, realism, fluffy yellow fire, smoke veil, blur, airbrush or white blob.`

The negative prompts deliberately remove the Arlecchino-adjacent signature stack.

### C2. Premium sparks

Plain text`Single isolated dark-fire spark burst on pure flat black, locked camera. Stylized anime/donghua VFX: only 4–7 hard tapered streaks, tiny pale-hot heads, crimson/red-orange bodies, dark red cooling tails; one long curved accent, several short ballistic fragments, sparse gravity fall and one ricochet. Strong negative space, sharp graphic edges, violent fast timing. No blood motif, round embers, bokeh, uniform radial burst, slow floating dots, dense glitter, photographic blur, smoke, lens flare or scenery.`

This should be the **least particle-dense** direction.

### C3. Glint sheet

Plain text`A clean sheet of isolated restrained dark-fire glints on pure flat black, locked camera: sparse crimson-peach 4-point stars, tiny needle flashes and short broken arc glints, razor-thin arms, tiny hot centers, 3 sizes, each flashing independently and vanishing quickly. Graphic anime/donghua cel-VFX with lots of empty black space. No eclipse circle, eye symbol, wing motif, glitch, lens flare, bokeh, soft halo fog, glitter field, overlapping stars, text, ground or objects.`

---

## One Firefly adjustment I would make to your pipeline

Since Firefly Video now officially supports an alpha workflow, I would run **one A/B test** on each winning generation:

**A:** your normal pure-black version.
**B:** the same prompt/seed with Firefly's Transparent Background option.

Adobe says the transparent workflow outputs separate foreground and alpha videos, while maintaining 5-second/24-fps generation. [Adobe Help Center](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html)

My inference is that black may still win for **emissive sparks/glints**, because black-to-additive extraction is trivial and deliberately preserves soft light. But real alpha may win for the **opaque/dark backing portions of the flame**, where black-screen extraction can destroy dark red shapes.

That suggests an especially useful hybrid:

**flame body/backing → straight alpha atlas**
**hot core + streak sparks + star centers → additive atlas**

That separation directly solves one of the weaknesses of your current single normal-blend AI card: you stop asking one texture to simultaneously behave like opaque graphic fire, translucent glow and HDR sparkle.
## E. Bảng kiểm nguồn của Claude (03/11/2026)

Cách kiểm: mở từng trang (WebFetch, curl, hoặc tab riêng trong trình duyệt của ứng dụng); siêu dữ liệu YouTube đọc từ `ytInitialPlayerResponse` của trang xem (kênh, ngày đăng, độ dài); **mốc thời gian trong video thì Claude tự chụp khung hình tại đúng giây đó** (khung gốc 1920×1080, rút từ phần tử video trong tab riêng) rồi nhìn. "Đúng" là trang nói đúng điều ChatGPT gán cho nó; "một phần" là trang có nhưng nói khác hoặc hẹp hơn; "không kiểm được" là không mở được hoặc không có nguồn; "sai" là trang hay khung hình nói ngược lại.

### E1. Câu trả lời 1

| # | Điều ChatGPT nói | Nguồn | Kết quả |
|---|---|---|---|
| 1 | Riot: độ gây chú ý của hiệu ứng phải theo tầm quan trọng trong lối chơi; không "vặn mọi thứ lên 11" | leagueoflegends.com, "Clarity in League" | **Đúng.** Bananaband1t, 12/03/2021: "the amount of attention an ability grabs should match its level of importance"; "we'll never turn everything up to 11" |
| 2 | Bộ hướng dẫn VFX công khai của Riot: hiệu ứng có chuẩn bị và tan; phần kết là hiệu ứng phụ với độ sáng, độ bão hòa, độ đục thấp hơn; trộn hình mềm và sắc; hình rõ | PDF trên nexus.leagueoflegends.com | **Đúng**, đọc bản lưu trên web.archive.org (link gốc giờ chuyển 301 về trang chủ LoL). Trang 32: "ALL EFFECTS SHOULD HAVE ANTICIPATION AND DISSIPATION", "OUTROS SHOULD BE CONSIDERED AS A SECONDARY EFFECT; WITH A LOWER VALUE, SATURATION, AND OPACITY"; mục Shapes: "mixture of soft and sharp shapes, well-defined silhouettes". Cùng trang có câu "We intentionally minimize an effect's linger duration" (xem F) |
| 3 | Little Demon Tristana: lửa ảo khác nhau nhờ lõi nóng, chuyển màu, tia lửa cháy, khói, không chỉ đổi màu một lửa chung | nexus.leagueoflegends.com (2019) | **Đúng**, đọc bản lưu (link gốc 301). Kevin "Sirhaian" Leroy: bản đầu "hot fire colors and shapes, mixed with burning sparks and dark smoke"; bản sau "a hot and bright cyan core, subtly cooling down to purple tones" để khác các skin lửa khác |
| 4 | HoYoverse gọi chiêu nộ Balemoon Rising là "great wing of Balemoon Bloodfire" | HoYoWiki | **Đúng** (API của HoYoWiki, mục 5653 và trang Arlecchino 5149: "Arlecchino's great wing of Balemoon Bloodfire beats…") |
| 5 | Video demo chính thức của Arlecchino dài 2:50 | HoYoWiki, YouTube `TnYFVP3c_bs` | **Đúng.** @GenshinImpact, đăng 22/04/2024, 170 giây; HoYoWiki dẫn đúng link |
| 6 | Số điểm Reddit (957, +491, +2.856, +1.049) | Reddit | **Không kiểm được.** Reddit bị chặn trong trình duyệt của ứng dụng và trong sandbox. Chính ChatGPT ở câu trả lời 2 đã hạ các số này xuống "phản ứng của fan, không phải bình chọn" |
| 7 | Bản ghi lời thoại của Changli: "Perish in flames" ở 2:00, "Be reduced to cinders" ở 2:25 | Dailymotion `x92zs42` | **Một phần.** Trang Dailymotion là bản đăng lại của "Games World", không có lời thoại trong trang. Nhưng khung Claude tự chụp ở 2:27 của video chính thức có phụ đề "Be reduced to cinders", và 2:00 là đoạn đánh bằng lửa: mốc đúng, nguồn trích thì không |
| 8 | Video chính thức của Changli | YouTube `jYjxjy1l6Co` | **Đúng.** @WutheringWaves, 18/07/2024, 201 giây |
| 9 | Trailer chính thức của Rengoku do SEGA đăng | YouTube `J4ylWd7t1MQ` | **Đúng.** @SEGAAsiaEN (SEGA Asia, nhà phát hành), 28/06/2021; video ghi "This game is still under development" |
| 10 | Yoimiya: demo chính thức; người chơi chê hiệu ứng thật trong game nhạt so với lời quảng cáo | YouTube `dn8etqEPtFg` | Demo: **đúng** (@GenshinImpact, 08/08/2021). Lời chê: **không kiểm được** (không có link) |
| 11 | HoYoverse nói Firefly "shine brighter than the stars" | HoYoLAB 29991490 | **Đúng.** Bài của tài khoản Honkai: Star Rail mở đầu bằng câu đó |
| 12 | Burnice: đoạn lửa và giao tranh quanh 1:19 | YouTube `8-che_oqcuw` | **Sai.** Đó là video triển lãm của kênh ZZZ Nhật; quanh 1:19 là cảnh nhảy với hiệu ứng xanh lá, không có lửa |
| 13 | Tarka Ji được làm lại, video chính thức | YouTube `_C0XTM0ZBpQ` | **Đúng** (tiêu đề "Tarka Ji Remake Cinematic & Gameplay Showcase", @NARAKABLADEPOINT, 26/04/2025). "Làm lại tập trung vào lửa": **một phần** (video toàn lửa, nhưng không có câu đó) |
| 14 | Soul Land tập 180 trên kênh chính thức của Tencent, cảnh lửa phượng hoàng | YouTube `kfARb8fyTac` | **Đúng.** @TencentVideoAnimation, 05/07/2024, tiêu đề "以凤凰之火，点燃大海" |
| 15 | Rayane Saada: thân chính, lớp viền, sóng xung kích; tụ lực bằng quả cầu Fresnel lớn dần, hạt hút vào tâm, vòng co lại; nhiễu đỉnh | 80.lv, 15/03/2024 | **Đúng** ("a little emissive Fresnel sphere that grows with little sprites that are attracted to the center"; vòng co vào; "Vertex Noise") |
| 16 | David Gao: va chạm tách thành khói, tàn lửa, vết sáng, mảnh vụn; giả mô phỏng đắt bằng mặt phẳng và nhiễu | 80.lv | **Đúng** ("Burst of embers on impact", "Glowing hit mark on impact"; "a plane with a noise… pan the noise, distort it, erode it") |
| 17 | Một bài khác cảnh báo đèn hạt tốn và gợi ý giả ánh sáng bằng tấm phẳng | "80.lv+1" | **Không kiểm được.** Bài của Gao dùng đèn hạt mà không cảnh báo; bài của Guillermo Rossell cũng không nói; nguồn "+1" không có trong DOM |
| 18 | Soenke Seidel: ba mặt nạ trong ba kênh RGB cuộn khác tốc độ, dải trong có ngưỡng cắt riêng; va chạm với mặt phẳng đất rẻ hơn nhiều | 80.lv, 21/01/2021 | **Đúng** ("three different masks in the three RGB channels", "a ground plane which is MUCH cheaper") |
| 19 | Sheila Stipnieks hối tiếc vì không làm kết cấu riêng cho tàn lửa | ArtStation | **Đúng**, đọc trong tab riêng: "I regret that I did not give the embers a proper texture. I did not realize how bad it looks until I saw it on video." |
| 20 | Một họa sĩ Paragon: tia lửa đổi sang bản kéo dài khi nhanh, kéo phần giữa như "hotdog" | RealTimeVFX 10990 | **Đúng.** ryangatts (bài 7, 11/11/2019): "I was on Paragon"; "you switch to a stretched version of the spark texture as you go faster"; "only the middle gets stretched" |
| 21 | Tia lửa bắt đầu dài rồi co thành chấm | 80.lv (Guillermo Rossell) | **Đúng** ("my sparks will start elongated and will transform to a dot over time") |
| 22 | Phê bình vụ nổ: chùm theo hướng, chớp đầu ngắn, không phun đều hình cầu | RealTimeVFX 29528 | **Đúng.** cEssex: "Never just spawn them in a sphere"; "a big spikey muzzleflash sprite… for 1-2 frames at the start" |
| 23 | Jonny Cadman (Riot): lửa = hạt sáng + dải cuộn + flipbook | ArtStation | Thành phần: **đúng** ("glowing particles, a scrolling ribbon, and a flipbook", Unity). Chức danh ở Riot: **không kiểm được** trên trang đó |
| 24 | `InstancedBufferGeometry`, `renderer.info` | threejs.org | **Đúng** (mã của ta đã dùng: `embers.ts`, `fire-points.ts`) |
| 25 | `EXT_disjoint_timer_query_webgl2` đo thời gian GPU không đồng bộ | Khronos | **Đúng**, với lưu ý phải kiểm `GPU_DISJOINT_EXT` và chờ `QUERY_RESULT_AVAILABLE` |
| 26 | Kenney Particle Pack CC0, 80 file 512×512; Smoke Particles CC0, 70 file | kenney.nl | **Đúng** (trang và `License.txt` trong bản đã tải ở `~/VFXLab/packs/`, đã ghi trong `docs/games/THIRD_PARTY.md`) |
| 27 | OpenGameArt "Animated flame" CC0, 25 khung, "free for commercial use, no need to give credit" | opengameart.org | **Đúng** (highwizard, 26/11/2020, CC0) |
| 28 | Poly Haven: mọi tài sản CC0 | polyhaven.com/license | **Đúng** ("Our assets are all licensed as CC0") |

### E2. Câu trả lời 2

| # | Điều ChatGPT nói | Kết quả (khung Claude tự chụp, 03/11/2026) |
|---|---|---|
| 1 | Tự hạ các số Reddit; xác nhận câu của Stipnieks và chuyện "hotdog" | **Đúng** với bảng E1 (#6, #19, #20) |
| 2 | Hướng cũ quá gần dấu ấn riêng: phượng hoàng và vòng tròn (Changli), pháo hoa lễ hội (Yoimiya), nhật thực đỏ đen, mắt, cánh, lưỡi hái (Arlecchino) | **Đồng ý.** Khung Arlecchino 2:00 đúng là "con mắt" giữa vòng đỏ, 1:55 là vòng nhật thực đỏ trên nền đen: đó là dấu ấn của nhân vật |
| 3 | Changli 2:00 và 2:25 | **Đúng** (2:00 đường chém lửa; 2:27 phụ đề "Be reduced to cinders") |
| 4 | Arlecchino 1:57 "the visuals" | **Không hợp:** khung gần như đen, nhiễu kỹ thuật số; không có tia lửa |
| 5 | Burnice `0NQPMTJ9rh0` 1:00 "3, 2, 1, fire!" | **Một phần:** khung 1:00 là Burnice trong đường hầm, chỉ một ngọn lửa nhỏ; video đúng là của kênh @ZZZ_Official |
| 6 | Yoimiya 1:30 | **Sai cho tia lửa:** khung là cận mặt nhân vật. Tia lửa và sao lấp lánh ở 1:24–1:26 và 0:50–0:51 |
| 7 | Mavuika trailer `fd5vxULcZYw` 1:45 | **Sai:** khung là bộ trống |
| 8 | Tarka Ji 0:30 | **Sai:** hành lang tối, không có lửa nổi bật |
| 9 | Firefly 2:40 | **Yếu:** đó là logo cuối video (có lấp lánh quanh logo) |
| 10 | Navia `o1EEvbQXe6Y` 1:45; Raiden `mvrW4aKwAXw` 1:45 | **Sai / yếu:** Navia là cảnh thuyền trên sông; Raiden là một chớp nhỏ ở xa |
| 11 | Lingsha `HyS-McxYXpU` 2:30 | **Sai:** video chỉ dài 2:13 |
| 12 | Yoimiya Collected Miscellany `b4QN9epy680` 3:00 | **Đúng:** chiêu nộ trong game, camera chơi, bụi vàng lấp lánh rắc quanh vùng chiêu |
| 13 | Adobe: tạo hiệu ứng, hạt, lửa trên nền đen để ghép | **Đúng** (helpx "Writing effective text prompts for video generation", cập nhật 16/06/2026: "Create overlays, like light flares, particle effects, or fire, on a black background") |
| 14 | Adobe: nhiều chủ thể làm rối Firefly | **Một phần:** trang nói "More than four subjects can often confuse Firefly" |
| 15 | Firefly Video có nền trong suốt, xuất video tiền cảnh và alpha, 5 giây, 24 fps | **Đúng** (helpx "Generate videos with transparent backgrounds", cập nhật 18/08/2026: chọn model Firefly Video, bật Transparent background, "24 FPS and the duration is 5 seconds by default", zip có video tiền cảnh và video alpha) |

## F. Đánh giá của Claude

**Phần đáng tin và dùng được.**
- Chẩn đoán gốc rất đúng với mã và khung hình của ta: lửa hỏng vì **một tần số thị giác** (lưỡi giống nhau, sáng giống nhau, mềm giống nhau, hạt tròn giống nhau), không phải vì thiếu cam. Câu "đừng thêm tia lửa, hãy làm cho số tàn lửa đang có trông giống tia lửa" là câu đúng nhất của cả hai trợ lý.
- Các nguồn kỹ thuật đứng được: Riot (mục tiêu chú ý, chuẩn bị và tan, trộn hình mềm sắc), Seidel (mặt nạ đóng gói RGB, ngưỡng cắt riêng cho dải trong), Saada (tụ lực bằng vòng co và hạt hút vào), Gatts (tia kéo giãn phần giữa), Rossell (tia dài co thành chấm), cEssex (chùm theo hướng, chớp 1–2 khung), Stipnieks (tàn lửa thiếu kết cấu là lỗi thấy rõ trên video). Tất cả đã kiểm.
- Kiến trúc đề xuất khớp với bộ khung có sẵn: dùng lại `EmberPool` thay vì thêm hạt, một lô sao lấp lánh dùng chung mọi hệ, vòng vẽ giải tích, ánh chạy dọc ấn trong shader sẵn có (không thêm lệnh vẽ), giả ánh sáng đất bằng decal, hơi nóng chỉ ở cận cảnh.
- Kích thước ở camera chơi (vệt 1,25–2 px, dài 7–18 px; sao 4–7 và 8–12 px; vòng 1,5–2 px) ChatGPT ghi rõ là suy luận của nó; Claude đối chiếu với tỉ lệ ~38 px/m của camera chơi và thấy hợp lý (mục 6 của `FIRE_STYLE.md`).

**Phần yếu.**
- Mốc thời gian video: ChatGPT tự nhận ở câu trả lời 2 là không xem được khung hình, và khung Claude tự chụp cho thấy **phần lớn mốc của câu trả lời 2 không dùng được** (bảng E2: 13 mốc, 4 đúng, 3 yếu hoặc một phần, 6 sai, trong đó một mốc vượt quá độ dài video). Chỉ dùng mốc nào Claude đã chụp và nhìn.
- Burnice 1:19 sai video và sai cảnh. Lời chê Yoimiya và số điểm Reddit không có nguồn kiểm được.
- Câu "đèn hạt tốn, nên giả bằng tấm phẳng" không có nguồn kiểm được; tuy vậy với ta kết luận vẫn đúng vì Fire đã dùng `FlashLights` theo bể và decal đất.

**Chỗ Claude không đồng ý.**
- **Mốc của hướng C cũ (Crimson Eclipse Sigil)**: quá gần Arlecchino; ChatGPT tự sửa thành "Inkfire Furnace". Claude cũng không dùng cả hai: lửa tối, kiềm chế là một **tính chất** mà cả ba hướng đều cần trên đá sáng (lớp lót tối), không đủ khác để thành một hướng riêng. Hướng thứ ba của Claude là **Halo Seal** (vòng, ấn, tia: hình tròn), vì đó đúng là chữ "hào quang" của anh và gắn với ấn trên đất mà kỹ năng của ta đã có.
- **Thời gian lưu:** Riot ghi "minimize an effect's linger duration"; anh lại muốn lửa lưu lâu hơn (03/11). Luật của anh thắng; cách dung hòa đã có trong skill `game-vfx-layered` (đỉnh giữ rồi cháy tàn bằng xói mòn, giới hạn số mảnh lưu ở trận đông). Hào quang thì ngược lại: sao và vòng sống ngắn (4–12 khung), chỉ ấn và đất cháy lưu.
- **"Một họ hào quang mỗi pha"** (sạc là vòng, phóng là tia, bay là vệt, va chạm là sao và vòng, dư âm là ánh chạy): Claude dùng làm luật mặc định, nhưng anh muốn "lấp lánh, long lanh" rõ, nên ở va chạm cho phép hai họ (sao + vòng mảnh), có số trần.
