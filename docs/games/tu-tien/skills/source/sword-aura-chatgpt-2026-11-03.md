# Sword aura research, ChatGPT (Chat, thinking High), 03/11/2026

- **Công cụ:** ChatGPT, chế độ Chat (không dùng Work hay agent), thinking effort High; tab riêng của Claude trong trình duyệt của ứng dụng.
- **Ngày:** 03/11/2026, khoảng 13:45–14:30.
- **Chat:** https://chatgpt.com/c/6ae9888a-825c-83ec-b9be-b62feb3210c1
- **Bối cảnh:** anh hỏi vì sao các thanh kiếm bay chưa có hiệu ứng quanh thân ("nhìn các thanh kiếm bay kiểu hơi thô, chưa đẹp cho lắm"). Đây là bước nghiên cứu thiết kế được yêu thích trước khi đưa anh ba hướng.
- **Đây là văn bản nghiên cứu chưa tin cậy.** Bảng kiểm nguồn của Claude ở phần E, đánh giá ở phần F.
- **Cách lấy văn bản:** chuyển DOM câu trả lời sang Markdown ngay trong trang rồi gửi về một bộ nhận cục bộ (127.0.0.1), nên chữ là nguyên văn. Mỗi chip trích dẫn giữ dạng `[Trang +N](url)`: trang chỉ có link của nguồn đầu, các nguồn "+N" không nằm trong DOM. Băng ảnh minh họa bị bỏ, còn lại dòng "55 images". Tham số `utm_source=chatgpt.com` giữ nguyên như ChatGPT ghi. Đầu mục của hai câu trả lời được hạ hai bậc (`#` thành `###`) để nằm dưới mục C và D; chữ không đổi.
- **Bố cục file:** A và B là hai tin nhắn đã gửi; C là câu trả lời cuối sau khi tự rà soát (dùng bản này); D là câu trả lời đầu, giữ lại vì bản tự rà soát đã dựng lại cả ba hướng theo trần của engine và bỏ vài trích dẫn; E là bảng kiểm nguồn; F là đánh giá của Claude.

## A. Tin nhắn 1 (đã gửi nguyên văn)

```text
I'm designing the flying-sword look for a xianxia typing-defense game (three.js, browser, far top-down 3/4 camera at about 55 degrees). Please do a thorough web search: many sources (official game pages and patch notes, developer talks and interviews, GDC or 80.lv breakdowns, ArtStation breakdowns, fan reaction threads and reviews), not one listicle. Put a URL behind each claim, and say when something is your own inference rather than sourced.

Context: our hero sword is a real 3D model we keep as-is, called Clear Wind: a slim silver jian blade, a white jade ring at the guard, a cloud-shaped guard, and a tassel. In skills it flies as a "river" of swords: about 6 full swords + 24 LOD swords + 64 impostor sprites. Right now they fly as bare metal props with only a thin white-hot edge line, a soft rim, a hit flash and a short trail, and they look crude. We need an aura layer that DRESSES the real sword: the blade, jade ring, cloud guard and tassel must stay readable; the aura wraps the sword, never hides or replaces it. The aura is a SHAPE layer; its MATERIAL comes from an element kit (Metal = silver-white/cyan qi; Fire; Water next; later Wood, Earth, Thunder). Our VFX rules: only thin HDR cores bloom; halos and rings stay at or below 0.9 per channel; a dark layer sits behind every bright layer; the core is at most 30% white; never use the enemy warning red #FF4A4A; the aura for the whole river must cost about +0.6 ms p95 at 1920x1080 in WebGL.

Please cover:

1) The most loved flying-sword / sword-qi / yu jian (御剑) and sword-aura looks in games and donghua/anime. For example: Genshin Impact (Xiao, Xianyun, Shenhe), Honkai: Star Rail (Jing Yuan's Lightning-Lord, Blade, Yanqing's flying swords), Wuthering Waves, Naraka: Bladepoint, Black Myth: Wukong, Tower of Fantasy, Moonlight Blade (Tian Ya Ming Yue Dao), Justice Online (Ni Shui Han), Swords of Legends, Where Winds Meet, Onmyoji; donghua such as A Record of a Mortal's Journey to Immortality (Fan Ren Xiu Xian Zhuan), Battle Through the Heavens, Soul Land, Jade Dynasty / Zhu Xian, Sword of Coming (Jian Lai), The Daily Life of the Immortal King; and the Myriad-Swords / sword-rain ultimates players love. Which ones do fans praise most, and WHY? Cite fan reaction or reviews where you can.

2) The LAYERS that make a flying sword read premium: blade-hugging qi sheath, edge light, afterimages/ghosts, ribbon or tassel streamers, light motes, runes, a tip star, distortion, a soft ground shadow-light, colour grading per element. How does the look change at launch, cruise, turn, strike and return? How does each layer read at a FAR top-down 3/4 camera (sword 35-130 px long on a 1080p screen) versus close-up? Which layers survive at 35 px and which become noise?

3) How those games keep many swords cheap (instancing, impostors, shell or fin meshes, ribbon trails, flowmaps, vertex-shader tricks), where known, with sources.

4) THREE original directions for our Clear Wind jian, each with an English name and: its layer list (each layer's role, rough brightness, which phase it shows in, and whether it survives at 35 px); how the element kit swaps its material (Metal, Fire and Water at least); what makes it captivating, luxurious and modern; and a rough cost estimate for about 94 swords. Do not copy any game's design; take principles, not looks.

End with a ranked table of the three directions and the 5 sources you trust most.
```

## B. Tin nhắn 2, tự rà soát (đã gửi nguyên văn)

Claude thêm vào đây trần số lượng của engine ở High (`docs/games/VFX_STANDARD.md`, bảng trần số lượng): 32 ribbon sống, 32 draw call VFX thêm, trung bình 3 lớp trong suốt chồng nhau mỗi điểm ảnh.

```text
Before I use this, please review your own answer with fresh eyes. Search again where you need to.

1) Reopen every link you cited (especially the Reddit threads, the Xiao developer insight, the Naraka Wuchen rework note, the RealTimeVFX sketchbook post, the Robbert Mouthaan ArtStation breakdown, the 80.lv articles, the GDC Vault entries, the Weibo and 17173 pages, the Riot page and the Kuro patch notes). Confirm each one exists and says what you claimed. Where you quote fans, give the exact phrase and the thread.

2) Mark each claim as verified, uncertain or unsupported. Correct or drop anything wrong (for example: check that Qingxiao really is a Wuthering Waves character with a Sword Flight state, and when she launched; check that the Riot page you linked is the right one).

3) Add strong examples or techniques you missed: other loved yu-jian, sword-formation and sword-rain scenes in donghua and games (for example Zhu Xian, Battle Through the Heavens, Soul Land, The Daily Life of the Immortal King, Swords of Legends, Chinese Paladin / Sword and Fairy), and real-time techniques for a blade-hugging aura (shell meshes, fresnel or depth-faded fins, signed-distance impostors, flowmapped ribbons), each with a URL.

4) Check that the three directions do not copy any specific game's signature look, and that each one fits our rules: only a thin HDR core blooms; halos and rings at or below 0.9 per channel; a dark layer behind every bright layer; core at most 30% white; never #FF4A4A; +0.6 ms p95 for the whole river. Note also our engine caps on High: about 32 live ribbons, about 32 extra VFX draw calls, and an average of 3 overlapping transparent layers per pixel on the field. So a separate ribbon per sword for all 94 swords is not available. Adjust the designs where needed.

5) Give the corrected final answer in full: the corrected loved-designs list with URLs, the layer hierarchy and what survives at 35 px, the cheapness techniques, and the three directions with their layer lists, element swaps (Metal, Fire, Water) and cost. End with a short list of what you changed and why.
```

## C. Câu trả lời cuối, sau khi tự rà soát (nguyên văn)

I re-audited the previous answer source by source, including the primary pages, the Reddit threads, the VFX breakdowns, and the technical references. Several parts survive intact, but I found a few places where I had promoted an inference into a sourced claim. I correct those below.

The most consequential correction is architectural: **the aura should not mean 94 independent transparent trail systems**. With your 32-ribbon cap and ~3-layer average transparency budget, the right structure is:

**6 hero swords = physical identity + luxury detail**
**24 LOD swords = instanced aura geometry + swept fins**
**64 impostors = one SDF quad/pass each**
**4–8 river-level ribbons = composition, not one ribbon per sword**

That is the basis of the revised three directions.

---

### 1. Source audit of my previous answer

Status meanings:

- **VERIFIED** — I reopened the source and it supports the claim.
- **UNCERTAIN** — source exists, but the stronger wording was partly my interpretation.
- **UNSUPPORTED** — the cited page does not substantiate that specific wording; I drop or replace it.
- Where the source is a Reddit post, the status means the quote/thread is verified, **not** that the fan opinion is objectively true.

| Previous claim | Status | Audit result |
| --- | --- | --- |
| Qingxiao is a real Wuthering Waves character | **VERIFIED** | Kuro's Version 3.6 maintenance notes list her as a new **5-star Aero, Sword Resonator**. Version 3.6 maintenance ran on **August 20, 2026**. [Wuthering Waves](https://wutheringwaves.kurogames.com/es/main/news/detail/5272?utm_source=chatgpt.com) |
| Qingxiao has a “Sword Flight” state | **VERIFIED** | Kuro's 3.7 patch notes explicitly refer to Qingxiao being in the **“Sword Flight” state**, plus Sword Step and Ephemeral Transcendence. [Wuthering Waves](https://wutheringwaves.kurogames.com/en/main/news/detail/5571?utm_source=chatgpt.com) |
| Qingxiao's fantasy involves ten thousand flying blades | **VERIFIED** | Kuro's official Qingxiao media page describes her Heart Sword as splitting sword intent into **“ten thousand flying blades.”** [Notion](https://wutheringwaves.notion.site/Resonator-Videos-Qingxiao-42aef7f91e4b83e0989a01533d33f9b2?pvs=21&utm_source=chatgpt.com) |
| “Qingxiao is probably the strongest current benchmark” | **UNCERTAIN / inference** | That is my comparative judgement, not an objective sourced ranking. I retain her as **my #1 reference for your problem**, not “the objectively best.” |
| Fans strongly praised Qingxiao's presentation | **VERIFIED** | In *Qingxiao convene animation*: “**good lord this is art**,” “**Really, really good**,” and “**this is so beautiful ...**”. Another commenter praises combat, skills, ultimate, SFX, mobility and animation together. [Reddit](https://www.reddit.com/r/WutheringWaves/comments/1vhxs99/qingxiao_convene_animation/) |
| Fans notice her physical swords and detailed recovery | **VERIFIED** | *This little animation is top tier*: OP says the swords “**never clip through the floor**”; another calls out “**recovery animations after every single moves**”; another calls her invisible-stair animation “**so elegant**.” [Reddit](https://www.reddit.com/r/WutheringWaves/comments/1w7f6n1/this_little_animation_is_top_tier/) |
| Beta players asked for swords to be less VFX-like and more physical | **VERIFIED, but beta-source only** | *QINGXIAO MOVESET LEST GOO*: “**wish the swords persisted more in map and looked less VFX Y more phyiscal**.” [Reddit](https://www.reddit.com/r/Qingxiao/comments/1v69j6d/qingxiao_moveset_lest_goo/) |
| Qingxiao players complained transparent swords meld together | **VERIFIED, beta-source only** | *Can the swords be more opaque?*: OP says VFX feel “**less physical and very transparent and overdone, so they all meld together**,” and specifically asks for more physicality and intent. [Reddit](https://www.reddit.com/r/Qingxiao/comments/1v6x6sw/can_the_swords_be_more_opaque_moveset_discussion/) |
| V2 fans noticed additional swords, hitlag/screen-shake polish | **VERIFIED, but leak/beta thread** | The thread exists and is explicitly flagged by moderators as incomplete beta material. I should not have treated this as final-game evidence. [Reddit](https://www.reddit.com/r/WutheringWavesLeaks/comments/1vcki40/qingxiao_v2_animations_via_seele/) |
| Yanqing's official trailer climaxes with swords descending | **VERIFIED** | HoYoverse's official trailer is the correct source; its official metadata includes “Practice is over. **Swords, descend!**” The direct YouTube page was rate-limited on reopen, but the official video/result is valid. |
| Fans recognize Yanqing as the classic Chinese flying-sword trope | **VERIFIED as fan reaction** | In *Yanqing's ult is hilarious to me*: “**CN shows and games has told me that everybody who is competent rides on flying swords. (Also summon swords behind them.)**” [Reddit](https://www.reddit.com/r/HonkaiStarRail/comments/16jf4xw/) |
| Naraka Wuchen received Blade Storm / enduring sword rain | **VERIFIED** | Official Naraka notes say Tai Chi Teleport: Blade Storm strikes with a series of spirit blades and “**features an enduring sword rain**.” [narakathegame.com +1](https://www.narakathegame.com/news/update/20240719/33459_1168466.html) |
| Wuchen's sword-rain cadence alternates small and large swords | **VERIFIED as player observation** | *How do y'all feel about Wuchen's rework?* describes multiple small swords → big sword with a high-pitched cue → more small swords → final large swords. [Reddit](https://www.reddit.com/r/NarakaBladePoint/comments/1l1wis3) |
| Sword of Coming has praised stylized afterimages and energy-wave detail | **VERIFIED** | The review explicitly praises “**stylisation in the afterimage effects**” and the fine behaviour of wavy energy light. [Reddit](https://www.reddit.com/r/Donghua/comments/1nea5pb/sword_of_coming_review/) |
| Sword of Coming is therefore uniformly a great reference for huge sword swarms | **UNSUPPORTED / corrected** | The **same reviewer** says that at huge scale its energy effects get rougher and “**All those energy flying swords attacks ... [are] especially lacklustre.**” That negative evidence is actually very useful for your design. [Reddit](https://www.reddit.com/r/Donghua/comments/1nea5pb/sword_of_coming_review/) |
| RMJI gets unusually strong praise for production/visual quality | **VERIFIED as fan reaction** | Comments call its development quality “**unparalleled by others**,” praise “stunning visuals,” and repeatedly say it sets a very high bar. [Reddit](https://www.reddit.com/r/Donghua/comments/1o10etd/) |
| RMJI's “grounded cultivation presentation” was proven by that same thread | **UNSUPPORTED as attribution** | That phrasing was my visual interpretation. I now mark it explicitly as **my inference**. |
| Xiao's developer insight discusses jade, clouds, light/dark and movement language | **VERIFIED** | HoYoverse's official Xiao development article supports those design choices; my previous summary was fair. [Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com) |
| Genshin GDC article was about the game's deliberate anime art core/pipeline | **VERIFIED** | GDC says the talk covers anime-style art-core pillars, character/setting design, pipeline, and key features. [GDC Vault](https://www.gdcvault.com/play/1027540) |
| Riot says VFX artists must balance spectacle and readability | **VERIFIED** | This was the correct Riot page. It explicitly says artists carry a “**heavy burden of restraint**” so players can understand what is happening and balance satisfaction with gameplay clarity. [Riot Games](https://www.riotgames.com/vi/artedu/visual-effects) |
| RealTimeVFX example uses a sword-attached mesh aura with scrolling noise/mask | **VERIFIED** | Rensei explicitly describes a mesh aura, scrolling noise, circular mask, lifetime colour/alpha and attachment to the sword hierarchy. The same breakdown uses a black layer behind a glowing slash layer. [Real Time VFX](https://realtimevfx.com/t/renseis-sketchbook/20495/24?u=rensei) |
| Robbert Mouthaan provides phase-based melee VFX evidence | **VERIFIED with qualification** | It is a **self-study project**, not a shipped Zelda breakdown. It does use proxy-mesh sword glow, sparks, ribbon, hit effects and post-hit fade/erosion. [Robbert Mouthaan](https://robbertmouthaan.artstation.com/projects/L49NVk) |
| 80.lv Matt Schwartz article supports build-up → attack → dissipation and mesh/shader techniques | **VERIFIED** | It explicitly defines those three phases and shows shader-revealed mesh effects. [80.lv](https://80.lv/articles/from-realism-to-stylization-game-vfx-production) |
| The same 80.lv article explicitly said stylized VFX “simplify microdetail” | **UNSUPPORTED** | That was my paraphrase pushed too far. I drop it. |
| Jason Keyser describes painted textures + authored meshes + animated materials | **VERIFIED** | The article supports hand-authored shape/material workflows. [80.lv](https://80.lv/articles/jason-keyser-on-in-game-vfx-and-the-demand-for-fx-artists) |
| GDC VFX Bootcamp is about broadly applicable artistic/gameplay VFX principles | **VERIFIED** | That is exactly what its overview states; speakers were Hadidjah Chamberlain and Jason Keyser. [GDC Vault](https://www.gdcvault.com/play/1023943/Visual-Effects-Bootcamp-Artistic-Principles) |
| Rocksteady's Attention Overload talk is about directing attention amid dense feedback | **VERIFIED** | Its overview explicitly describes avoiding total screen chaos and using VFX to drive attention without overwhelming players. [GDC Vault](https://gdcvault.com/play/1034360/Attention-Overload-Creating-Readable-VFX) |
| Justice Online official Weibo supported 万剑归宗 / 御剑·极 | **VERIFIED from the indexed result, but page is dynamic** | The official Weibo result contained that June 2026 promotion; today's generic profile reopen no longer exposes that specific post text in its visible lines. I would classify this as **verified search-index evidence, weaker than a stable article URL**. |
| My second Justice Online claim about free sword-flight + camera optimisations | **UNSUPPORTED in this re-audit** | I could not re-establish that claim strongly enough. I drop it. |
| Where Winds Meet homepage supported “lightness and agility” sword-motion wording | **UNSUPPORTED** | The homepage exists, but not that specific claim. I drop it. |
| Where Winds Meet has current sword-energy mechanics | **VERIFIED elsewhere, not by that homepage** | Official patch material supports Nameless Sword/sword-energy changes. Treat it as a restrained wuxia reference, not a primary flying-sword reference. |
| Moonlight Blade's raid has lightning/fire/wind/ice sword mechanics | **VERIFIED, but secondary source** | 17173 explicitly lists 雷剑, 火剑, 风剑 and 冰剑 mechanics. [17173 News](https://news.17173.com/content/10282023/093214220.shtml) |
| Therefore Moonlight Blade proves a “shape/material separation” rendering architecture | **UNCERTAIN / my inference** | It demonstrates reusable elemental sword motifs, but not their shader architecture. |
| Onmyoji fans praised Susanoo's lightning visuals | **VERIFIED as fan reaction** | The cited thread exists. It is useful for lightning language, not as a flying-sword benchmark. [Reddit](https://www.reddit.com/r/Onmyoji/comments/x9puzz/) |
| Tower of Fantasy fans called particular weapon effects gorgeous | **VERIFIED but weak relevance** | The thread exists; this doesn't justify putting ToF near the top of your flying-sword research. I demote it. [Reddit](https://www.reddit.com/r/TowerofFantasy/comments/1mir21p/) |
| Black Myth is evidence for integrating surfaces, characters and VFX | **VERIFIED at a high level** | Epic's Game Science interview explicitly highlights environments, characters and VFX as part of its AAA visual presentation. [Unreal Engine](https://www.unrealengine.com/developer-interviews/black-myth-wukong-wows-with-ue5-early-access-visuals?lang=en-US) |
| Black Myth is a direct sword-aura reference | **UNSUPPORTED** | It isn't. I drop it from the core reference list. |
| Three.js instancing/batching reduces draw calls | **VERIFIED** | BatchedMesh explicitly exists for large numbers of objects sharing a material but varying geometry/transforms and says it reduces draw calls. [Three.js +1](https://threejs.org/docs/pages/BatchedMesh.html) |
| Transparent effects can become fill-rate/overdraw bound | **VERIFIED** | NVIDIA explicitly warns that screen-filling translucent effects can have effectively unbounded overdraw. [NVIDIA Developer](https://developer.nvidia.com/gpugems/gpugems3/part-iv-image-effects/chapter-23-high-speed-screen-particles) |
| Three.js transparency introduces sorting/depth complications | **VERIFIED** | The Three.js manual explains the depth/sorting issue directly. [Three.js](https://threejs.org/manual/pages/transparency.html) |
| EXT_disjoint_timer_query_webgl2 should be used for WebGL2 GPU timing | **VERIFIED, previous link was imprecise** | The MDN page I linked is titled for WebGL1 but explicitly states that WebGL2 uses EXT_disjoint_timer_query_webgl2; the underlying timing principle is correct. [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/EXT_disjoint_timer_query) |
| My +0.20–0.58 ms numbers were demonstrated measurements | **UNSUPPORTED if interpreted that way** | They were estimates. The corrected numbers below are explicitly **engineering budget estimates requiring profiling**. |

So: the previous answer's main design conclusion survives, but the sourcing is cleaner now.

---

### 2. Corrected reference set: what is actually worth studying

I would divide these into **direct yu-jian references** and **supporting art-language references**.

#### A. Direct flying-sword / sword-rain references

##### 1. Qingxiao — Wuthering Waves

**Status: VERIFIED primary reference + strong qualitative fan signal.**

Qingxiao was added with Wuthering Waves Version 3.6 on **August 20, 2026**, as a 5-star Aero Sword Resonator. Kuro explicitly describes her Heart Sword as turning sword intent into **ten thousand flying blades**, and subsequent 3.7 patch notes explicitly name her Sword Flight state. [Wuthering Waves +2](https://wutheringwaves.kurogames.com/es/main/news/detail/5272?utm_source=chatgpt.com)

The strongest lesson is not merely “lots of cyan swords.” It is **preserving swordness**. The positive fan response is substantial in the threads sampled, but equally useful is the criticism:

> “wish the swords persisted more in map and looked less VFX Y more phyiscal”

and:

> “very transparent and overdone, so they all meld together”

Those comments come from *QINGXIAO MOVESET LEST GOO* and *Can the swords be more opaque? Moveset discussion*. Both were beta-era discussions, so they are evidence of **audience taste**, not proof of a final-game flaw. [Reddit +1](https://www.reddit.com/r/Qingxiao/comments/1v69j6d/qingxiao_moveset_lest_goo/)

**What Clear Wind should take:** physical blade visibility, meaningful sword population, elegant recovery/secondary motion.

**What it should not take:** Qingxiao's exact cyan visual motifs, blade arrangements, animation poses, or named Heart Sword iconography.

---

##### 2. Yanqing — Honkai: Star Rail

**Status: VERIFIED direct trope reference.**

Yanqing is one of the clearest mainstream gacha executions of the classic “command floating swords / ride sword / rain swords down” fantasy. HoYoverse's official trailer uses the command **“Swords, descend!”** at the climax.

The fan thread *Yanqing's ult is hilarious to me* is particularly useful because viewers immediately identify the cultural shorthand:

> “everybody who is competent rides on flying swords. (Also summon swords behind them.)” [Reddit](https://www.reddit.com/r/HonkaiStarRail/comments/16jf4xw/)

**Lesson:** the silhouette and behaviour of an actual sword already communicate a large amount of xianxia fantasy. Don't bury that free semantic value under an energy blob.

---

##### 3. Wuchen — Naraka: Bladepoint

**Status: VERIFIED primary game source.**

NetEase changed Wuchen's ultimate into Tai Chi Teleport: Blade Storm. Its official notes explicitly call it an **“enduring sword rain”** and say targets or the impact region are struck by a series of spirit blades. [narakathegame.com +1](https://www.narakathegame.com/news/update/20240719/33459_1168466.html)

More valuable for your mass effect is player-described cadence:

small blades → distinct large sword → small blades → final large swords, with sound warning the important attacks. [Reddit](https://www.reddit.com/r/NarakaBladePoint/comments/1l1wis3)

**My inference:** a premium river needs **hierarchy in time as well as hierarchy in LOD**. Your six full Clear Winds should periodically become visible visual “beats” within the 88 support swords.

---

##### 4. Swords of Legends Online — Spellsword/Sword Artist

**Status: VERIFIED fan appeal; secondary for exact implementation.**

Players were explicitly attracted to the concept itself. In *Spellsword looks like a pretty unique class*:

> “Flinging magical swords at enemies sounds like an awesome concept.”

and another calls it “one of the cooler” classes. [Reddit](https://www.reddit.com/r/SwordsOfLegends/comments/ogk103)

A separate player describes liking how the Sword Artist's skills interact and the depth of longer combat. [Reddit](https://www.reddit.com/r/MMORPG/comments/p97dba)

**Lesson:** again, the fantasy is “magical swords,” not “energy projectiles vaguely shaped like swords.”

---

##### 5. Soul Land — Sword Douluo Chen Xin / *Soul Land: Sword Master*

**Status: VERIFIED official sword-centric reference; fan-love ranking uncertain.**

Tencent/WeTV now has a dedicated *Soul Land: Sword Master* film centred on Chen Xin, explicitly described as the **Sword Soul Master**, and Tencent released an official Sword Douluo Chen Xin PV. [WeTV +1](https://wetv.vip/en/play/89zj0dh7422ant5-Dunia_Roh_%3A_Master_Pedang)

This is a stronger addition than the generic Soul Land reference in my first answer because it provides a dedicated **sword-Dao hero visual vocabulary**.

**What to study:** how a single sword identity scales from physical weapon to supernatural authority.

**What I will not claim:** that a particular Chen Xin sequence is “the most loved sword rain” without stronger scene-specific audience evidence.

---

##### 6. Sword of Coming / Jian Lai

**Status: VERIFIED, with an especially useful warning.**

A detailed viewer review praises the show's stylized slash afterimages and the precise behaviour of smaller-scale energy waves. [Reddit](https://www.reddit.com/r/Donghua/comments/1nea5pb/sword_of_coming_review/)

But the same reviewer says the large-scale energy-flying-sword effects become rougher and calls those attacks “especially lacklustre.” [Reddit](https://www.reddit.com/r/Donghua/comments/1nea5pb/sword_of_coming_review/)

That contrast is almost a direct design lesson for you:

> **Small, authored sword-energy behaviour looks luxurious. Scaling the same glowing language indiscriminately to hundreds of objects can look cheaper, not richer.**

That sentence is **my inference** from the review.

---

#### B. Strong supporting sword/art-language references

##### Jade Dynasty / Zhu Xian

WeTV's official synopsis culminates with Gui Li wielding the **Zhu Xian Sword** against the Ghost King. [WeTV](https://wetv.vip/en/play/62e9ut2hxil9sgj-Jade_Dynasty?appid=coop_direct_msite_MY_bonusli)

Fan reaction to Season 2 describes it as a “visual spectacle,” while newer discussions repeatedly praise its animation/aesthetics. [Reddit +1](https://www.reddit.com/r/Donghua/comments/1clzmr2)

**Use it for:** divine-sword authority, environment/VFX contrast and making a sword feel like a mythical artefact.

**Do not use it as evidence for:** a specific mass-flying-sword rendering technique.

---

##### The Daily Life of the Immortal King

Bilibili's official listing has Season 3 Episode 5, **“You Are My Sword,”** and Crunchyroll describes Jingke reaching adolescence as a spiritual sword. [BiliBili +1](https://www.bilibili.tv/en/play/2067971/12619830?utm_source=chatgpt.com)

A sword-duel discussion contains:

> “I do love swords, especially Chinese swords. The Jian being my favorite sword of all.”

and praises the “insane end to the sword duel.” [Reddit](https://www.reddit.com/r/Animedubs/comments/zsyukf?utm_source=chatgpt.com)

**Use it for:** treating a sword as an identity-bearing supernatural being rather than disposable ammunition.

---

##### A Record of a Mortal's Journey to Immortality

The fan evidence strongly supports its visual reputation; comments describe its development quality as exceptional and praise the “stunning visuals.” [Reddit](https://www.reddit.com/r/Donghua/comments/1o10etd/)

**My visual inference:** RMJI is particularly useful for studying magical implements that continue to feel like physical objects while supernatural energy surrounds them. I cannot attribute that specific conclusion to the Reddit thread.

---

##### Genshin — Xiao, Shenhe, Xianyun

These are **not primary flying-sword references**, and I overstated their relevance before.

Xiao's official developer article is nevertheless extremely useful to Clear Wind because HoYoverse discusses jade jewellery, cloud motifs, dark/light contrast, hanging cloth elements and agile directional motion as deliberate parts of a Chinese-fantasy character language. [Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com)

Genshin's GDC talk likewise confirms that its anime appearance is based on deliberate art-core, character, environment and pipeline choices rather than simply adding glow. [GDC Vault](https://www.gdcvault.com/play/1027540)

**Use them for:** how jade, clouds, cloth/tassels, colour/value and movement cooperate.

---

##### Battle Through the Heavens

I would **not** now present BTTH as a primary yu-jian reference. I found better support for treating it as an **elemental supernatural-power benchmark**.

Recent donghua viewers praise its current battle animation quality, but this is qualitative fan evidence rather than a rendering breakdown.

**Use it for:** how supernatural elements are differentiated through movement, colour and scale.

**Don't cite it to justify:** your flying-sword geometry.

---

##### Moonlight Blade

A detailed 17173 raid breakdown documents lightning sword, fire sword, wind sword and ice sword mechanics. [17173 News](https://news.17173.com/content/10282023/093214220.shtml)

That is a useful conceptual precedent for:

**stable sword semantic shape + interchangeable elemental language**

but the architecture itself is **my inference**; the article doesn't describe the renderer.

---

##### Sword and Fairy 7 / Chinese Paladin

The official Steam listing describes real-time action, multiple skills and a deliberate “traditional oriental” aesthetic. [Steam Store](https://store.steampowered.com/app/1543030/STEAM?l=english&utm_source=chatgpt.com)

Players specifically praise its art direction and fluid/elaborate attack animations. [Reddit +1](https://www.reddit.com/r/JRPG/comments/1d1ggcx?utm_source=chatgpt.com)

I did **not** find enough reliable evidence to elevate a particular Sword and Fairy 7 flying-sword scene alongside Qingxiao/Yanqing/Wuchen. It belongs in the broader visual-reference folder.

---

##### Where Winds Meet

Keep it as the **restrained wuxia end of the spectrum**, not as a canonical flying-sword showcase. Players explicitly ask for flying swords in current discussions, which itself shows how recognizable/desirable that fantasy remains. [Reddit](https://www.reddit.com/r/wherewindsmeet_/comments/1qsvgr0/new_sword_martial_art_teased/)

---

#### My corrected “strongest references for Clear Wind”

Not an objective popularity ranking—this is **my ranking by usefulness to your exact task**:

| Rank | Reference | Why |
| --- | --- | --- |
| **1** | **Qingxiao** | Closest contemporary sword-cultivator + many-sword reference, plus unusually relevant fan feedback about physicality |
| **2** | **Yanqing** | Extremely clear, instantly legible yu-jian grammar |
| **3** | **Wuchen Blade Storm** | Excellent mass-sword cadence/hierarchy lesson |
| **4** | **Sword of Coming** | Strong small-scale energy/afterimage craft **and** strong warning against energy-soup at huge scale |
| **5** | **Swords of Legends Spellsword** | Pure “magical flying swords are cool” fantasy, without requiring giant energy replacement |
| **6** | **Soul Land: Sword Master / Chen Xin** | Strong sword-authority and divine-weapon reference |
| **7** | **RMJI** | Physical-magical artefact balance |
| **8** | **Jade Dynasty** | Mythic sword authority and spectacle/value composition |

That is much more defensible than my original list.

---

### 3. The professional principle underneath all of them

Riot's own VFX education page says the artist has to balance satisfaction with gameplay clarity and that every effect should clearly belong to a particular character/source. [Riot Games](https://www.riotgames.com/vi/artedu/visual-effects)

The 2017 Riot/Blizzard GDC VFX Bootcamp similarly frames VFX principles as both **artistic and gameplay** concerns, while Rocksteady's 2024 presentation explicitly tackles the problem of effects turning into information overload. [GDC Vault +1](https://www.gdcvault.com/play/1023943/Visual-Effects-Bootcamp-Artistic-Principles)

So for your typing game:

> **The aura's first job is not “make sword brighter.” Its first job is “make Clear Wind unmistakably magical while leaving the word tags, enemy silhouettes and sword itself understandable.”**

That's my design conclusion from those sources.

---

### 4. Corrected layer hierarchy

Your immutable rule should be:

**Opaque real sword → dark support shape → element aura → tiny HDR core.**

Not:

**sword → translucent glow → translucent glow → translucent glow → particles → ribbon → bloom.**

That latter stack would destroy both your readability and your ~3-layer transparency budget.

#### Recommended hierarchy

All brightness values below are **my art-direction recommendations**, not values taken from another game.

| Layer | Function | Output | 35 px | 70–130 px | Implementation |
| --- | --- | --- | --- | --- | --- |
| **Real Clear Wind** | Identity: silver blade, jade ring, cloud guard, tassel | PBR/opaque | **Critical** | **Critical** | Existing model |
| **Dark support lobe** | Separates aura from field/enemies | ~0.05–0.16 | **Critical** | Critical | Same aura shader/pass |
| **Element sheath** | Main magical shape hugging sword | ~0.40–0.82 | **Critical** | Critical | Same shell pass |
| **Thin elemental core** | Focus / controlled bloom | ~1.3–2.1 HDR | **Critical** | Critical | Same shader, tiny mask |
| **Tip needle/star** | Directionality | HDR, tiny | **Yes** | Yes | Same pass where possible |
| **Swept fin/tail** | Velocity read | ~0.2–0.55 | **Yes** | Yes | Instanced fin, not ribbon |
| **Hero jade-ring pulse** | Clear Wind signature | ≤0.80 | No | **Yes** | 6 swords only |
| **Hero tassel energy echo** | Organic secondary motion | ≤0.50 | No | **Yes** | 6 swords only |
| **Turn ghost** | Marks rapid trajectory change | ~0.15–0.30 | Only big turn | **Yes** | pooled sprite/fin |
| **River ribbon** | Gives swarm one coherent current | ≤0.35 | **Group-level** | Group-level | 4–8 total |
| **Motes** | Atmosphere | ≤0.55 | **No** | sparse heroes only | pooled/batched |
| **Distortion** | Strong hit accent | n/a | No | strike only | tiny shared region |
| **Ground shadow/light** | Connects airborne river to battlefield | ~0.08–0.30 | **Group-level** | Group-level | one/few field overlays |
| **Runes/glyphs** | Close glamour | ≤0.70 | **Kill** | 100 px+ only | optional hero pass |

##### Critical implementation rule

**Dark backing and bright aura should normally be encoded in the same surface/material pass.**

Your rule says every bright layer needs darkness behind it; that does **not** mean a second transparent mesh has to exist for every sword.

For example, one aura shell fragment shader can produce:

- outer dark zone,
- inner elemental body,
- tiny HDR spine.

Likewise, one impostor texture/SDF can encode all three zones.

That saves a huge amount of overdraw.

---

### 5. What survives at 35 px

At 35 pixels long, I'd preserve only six visual facts:

1. **there is physically a sword there;**
2. it has a dark outline/support field;
3. it has one elemental aura silhouette;
4. it has one very narrow bright direction line;
5. it has a clear tip;
6. its velocity has a readable rear shape.

The following become noise and should automatically LOD out:

- jade-ring ornament;
- cloud-shaped mini energy arcs;
- runes;
- tiny orbiting rings;
- multiple ghosts;
- individual motes;
- detailed water caustics;
- detailed fire tongues;
- tassel VFX;
- internal animated patterns narrower than ~2 px;
- multiple ribbon strands.

That isn't merely aesthetic conservatism. Transparent VFX can become fill-rate bound rapidly; NVIDIA specifically highlights overdraw as a common particle-system bottleneck, and Three.js's transparency documentation illustrates why transparent layers create depth/sorting complexity. [NVIDIA Developer +1](https://developer.nvidia.com/gpugems/gpugems3/part-iv-image-effects/chapter-23-high-speed-screen-particles)

##### My approximate screen-space art targets

At **35 px sword length**:

- dark backing extends ~1–1.5 px outside element body;
- element aura adds ~2–3 px to the sword silhouette;
- HDR core appears ~0.8–1.2 px;
- tip accent ~2 px;
- velocity tail ~6–12 px.

At **70 px**:

- sheath can widen;
- jade guard pulse becomes useful;
- one ghost can become readable.

At **100–130 px**:

- internal flow;
- guard-specific accents;
- tassel response;
- element-specific surface behaviour.

---

### 6. Correct phase behaviour

Matt Schwartz's breakdown explicitly separates an effect into **build-up, execution, dissipation**. [80.lv](https://80.lv/articles/from-realism-to-stylization-game-vfx-production)

Robbert Mouthaan's self-study similarly shows sword glow/trail before impact, hit effects at impact and erosion/fade afterwards. [Robbert Mouthaan](https://robbertmouthaan.artstation.com/projects/L49NVk)

For your typing release, I would adapt that into five phases.

#### Launch — 0 to roughly 3 frames

Because typing completion is the input, there should be no perceptible post-word charge delay.

- blade remains fully visible;
- sheath reveals **guard → tip**;
- jade ring gives one non-HDR pulse on the six hero swords;
- core lights immediately;
- tail starts compact;
- no shower of particles.

The shader reveal can do almost all of this without additional emitters.

---

#### Cruise

This should be the **lowest-noise state**.

Each 3D sword gets:

- physical model;
- one shell/material pass;
- one compact swept fin if needed.

The 64 impostors get only their single SDF quad.

Only **2–4 river ribbons** need to be visible in normal straight cruise.

---

#### Turn

Make **curvature**, not speed, the main richness driver.

On high angular velocity:

- fin widens on outer curve;
- hero aura asymmetrically stretches;
- at most 4–8 of the most visually important swords gain a temporary live ribbon;
- pooled turn ghosts appear behind a few leaders;
- physical tassel lags on the six hero swords.

This is an inference/design recommendation.

---

#### Strike

Don't turn the sword into a white explosion.

Sequence:

**sheath narrows → core spikes → physical sword contacts → tiny impact → residue spreads.**

Only the narrow core is >1.0.

Use a shared batched impact system. If distortion exists, restrict it to:

- hero sword hits;
- a few-frame lifetime;
- tiny screen footprint.

Never refract the whole river.

---

#### Return

Do not simply reverse launch.

Instead:

- tip core fades first;
- element flow rolls backward toward jade ring;
- hero guard gives one ≤0.9 closure pulse;
- river ribbons contract toward the formation;
- tassel catches up after direction change.

This gives controlled **御剑** behaviour rather than “homing missile despawn.”

---

### 7. Techniques for a real blade-hugging aura

Here are the techniques I would actually consider for your WebGL build.

#### A. Attached shell mesh

This has a direct real-time VFX precedent: Rensei's Sword Aura is literally a mesh attached to the sword hierarchy using scrolling noise and masks. [Real Time VFX](https://realtimevfx.com/t/renseis-sketchbook/20495/24?u=rensei)

For Clear Wind:

- create a very low-poly inflated silhouette around the blade;
- don't envelope the hilt completely;
- intentionally open the shell around the ring/cloud guard;
- vertex shader adjusts width according to LOD/phase.

For the 24 LOD swords, the same shell geometry can be instanced.

**Best use:** River-Silk and Meridian designs.

---

#### B. Fresnel as a secondary mask, not the aura itself

Epic's Fresnel documentation shows the standard view-normal falloff approach, including controlling how tightly it sits at silhouettes. [Epic Games Developers](https://dev.epicgames.com/documentation/unreal-engine/using-fresnel-in-your-unreal-engine-materials)

In GLSL the principle is simply based on dot(N,V).

For Clear Wind, use Fresnel to:

- bias sheath brightness toward its outer silhouette;
- strengthen the outer edge when the sword faces camera;
- prevent the aura from filling the entire blade face.

But don't let Fresnel replace authored shape: at 55° camera and rapidly varying sword orientations, a pure Fresnel aura would fluctuate too much.

That last sentence is **my inference**.

---

#### C. Depth-faded fins

Epic's DepthFade is explicitly intended to remove hard seams where translucent geometry intersects opaque surfaces. [Epic Games Developers](https://dev.epicgames.com/documentation/unreal-engine/depth-material-expressions-in-unreal-engine)

This is useful when:

- low-flying swords skim terrain;
- a velocity fin touches ground;
- river-level ground wisps intersect architecture.

For WebGL, reproduce the principle using your scene depth texture.

But it should **not** be enabled indiscriminately for 94 swords; that's an extra depth sample in a highly overdraw-sensitive effect.

---

#### D. Flowmapped ribbons / strips

A particularly credible example comes from Overwatch FX artist Rachel Day discussing Mercy's actual beam: its wispy particles use a **flow map**, and the original effect uses **two ribbons with subtle directional changes**. Blizzard separately identifies Rachel Day as an Overwatch FX artist. [Real Time VFX +1](https://realtimevfx.com/t/overwatch-vfx-mercy-healing-beam/699)

80.lv's Baltic VFX breakdown also describes texture-based caustics driven by a dedicated flow map rather than expensive fluid simulation. [80.lv](https://80.lv/articles/creating-vfx-for-baltic-vfx-content-pack)

For you:

- river ribbons: flowmapped;
- Water sheath: flowmapped;
- Fire: same geometry but different distortion field;
- Metal: almost straight directional UV flow.

---

#### E. Signed-distance impostors

Valve's classic distance-field work shows a low-resolution distance representation retaining smooth edges, sharp outlines and effects such as outlines/drop-shadows; it explicitly discusses use with image-based impostor-type content. [steamcdn-a.akamaihd.net](https://steamcdn-a.akamaihd.net/apps/valve/2007/SIGGRAPH2007_AlphaTestedMagnification.pdf)

This is ideal for your **64 impostor swords**.

Each quad stores something like:

- signed distance to physical sword silhouette;
- aura-distance band;
- optional guard blob/tip region;
- longitudinal coordinate.

Then one shader derives:

- opaque/dithered dark centre;
- element body;
- thin core;
- tip;
- velocity stretching.

No five-layer sprite stack.

At 35 px, SDF is particularly valuable because it lets you keep edge thickness screen-consistent.

---

#### F. Instanced fins instead of 24 ribbons

This is one of the biggest changes from my first answer.

A swept fin is simply a tiny camera/velocity-oriented mesh—say 2–6 triangles—whose rear vertices extend according to velocity.

It can:

- be part of one InstancedMesh;
- use per-instance speed, curvature, seed, element;
- UV-scroll;
- disappear at low velocity.

Three.js's batching APIs exist specifically to reduce draw-call overhead for large numbers of repeated objects, and NVIDIA's geometry-instancing analysis explains why many tiny independently submitted objects are expensive. [Three.js +1](https://threejs.org/docs/pages/BatchedMesh.html)

---

### 8. Correct cheap rendering architecture for 94 swords

#### The previous bad architecture

My earlier answer effectively left room for:

> 30-ish 3D swords × aura + wake ribbon
> 64 impostors × aura
> plus river treatment

That is too aggressive given your explicit cap.

#### Revised architecture

##### Tier 1 — six full Clear Winds

Each gets:

- existing opaque sword;
- instanced/pooled aura shell;
- shader core;
- hero guard/tassel accent;
- eligibility for a live ribbon.

But **not all six need ribbons continuously**.

Normal allocation: **2–4 hero ribbons**.
Sharp-turn allocation: **4–6**.

---

##### Tier 2 — 24 LOD Clear Winds

Each gets:

- simplified physical mesh;
- instanced shell;
- **instanced swept fin**, not a live ribbon.

All 24 fins can be a single draw if they share material.

No:

- particles;
- rings;
- distortion;
- individual ribbon simulation.

---

##### Tier 3 — 64 impostor swords

One instanced quad batch.

Each quad includes:

- sword silhouette;
- dark support;
- elemental aura;
- thin HDR line;
- tiny tip;
- speed-dependent tail.

One material, one pass.

---

##### River-level effects

Allocate the “expensive beauty” to the **formation**:

- 2–4 ribbons in ordinary cruise;
- up to 6–8 when the river makes a dramatic turn;
- 1 broad low-alpha ground current;
- one pooled mote system;
- one pooled impact system.

##### Total ribbon budget

Typical:

**4–10 live ribbons.**

Extreme turn/ultimate:

**12–16.**

Hard emergency ceiling:

**20.**

That leaves substantial margin under your ~32-engine cap for simultaneous unrelated gameplay FX.

---

### 9. Suggested draw-call budget

**My implementation estimate:**

| VFX batch | Approx. draws |
| --- | --- |
| 6 hero aura shells | 1 |
| 24 LOD aura shells | 1 |
| 24 swept fins | 1 |
| 64 SDF impostors | 1 |
| hero guard/tassel accents | 1 |
| dynamic ribbon pool | 1–2 |
| river-level motes | 1 |
| aggregate ground current | 1 |
| impact pool | 1–2 |
| optional distortion | 0–1 |

**Cruise: ~7–9 extra VFX draws.**
**Heavy strike: ~10–12.**

Even allowing implementation quirks, I would set the art team's hard internal limit at **16 aura-related draws**, not 32. The other 16 should remain reserve.

---

### 10. Transparency/overdraw budget

Your average ~3 overlapping transparent layers per field pixel is more restrictive than your draw-call limit.

Therefore:

##### One sword should normally contribute only **one translucent aura surface at a pixel**

Inside that one shader:

Plain text

`dark outer band
    ↓
element body
    ↓
thin HDR core`

are **regions**, not three separate transparent layers.

The physical sword itself remains opaque.

The swept fin begins mostly *behind* the shell rather than exactly on top of it.

The river ribbon should occupy gaps between sword clusters rather than coating the entire river.

##### Density-aware LOD

I strongly recommend one additional rule:

**When projected swarm density rises, reduce aura footprint automatically.**

For example:

- 1–2 nearby swords: normal sheath width;
- 3–5 projected overlaps: −20% sheath width and −25% fin alpha;
- dense convergence: impostors lose secondary halo entirely; only dark silhouette + core remain.

That is **my recommendation**, but it directly addresses the type of overdraw NVIDIA warns about. [NVIDIA Developer](https://developer.nvidia.com/gpugems/gpugems3/part-iv-image-effects/chapter-23-high-speed-screen-particles)

It should also help word-tag readability.

---

### 11. Global colour/value rules for all three directions

These make every design compliant with your constraints.

##### Non-HDR

All of these stay ≤0.9/channel:

- aura body;
- guard halo;
- rings;
- ribbons;
- motes;
- ground current;
- turn ghosts.

##### HDR

Only:

- central meridian/core;
- tiny tip point;
- single-frame contact needle.

##### White percentage

The core should be:

**≤30% neutral white contribution.**

Conceptually:

core = 0.70 × elementalCore + ≤0.30 × white

so Fire stays recognisably fire-coloured and Water stays water-coloured rather than all elements converging to white bloom.

##### Enemy warning colour

#FF4A4A is excluded completely.

For Fire, use:

- deep charcoal backing;
- burnt orange;
- amber;
- molten gold;
- pale warm-gold core.

Not warning red.

---

### 12. Direction A — **River-Silk Sheath**

#### Concept

Clear Wind looks as though an extremely thin piece of immortal qi silk has been tailored **around the real sword**.

The physical silver jian remains central.

The sheath:

- opens slightly around the white-jade ring;
- follows the cloud guard's curvature without covering it;
- narrows along the blade;
- becomes a restrained silk-like wake behind the sword.

It is a “garment,” not a substitute weapon.

#### Originality audit

**No signature match found in the references I surveyed.**

It borrows generic principles:

- blade-attached mesh;
- flowing cloth/qi;
- jade/cloud visual language;
- directional ribbons.

It does **not** use Qingxiao's specific sword arrangements, Yanqing's sword halo/ultimate composition, or Wuchen's sword-rain cadence.

##### Layers

| Layer | Role | Brightness | Phase | 35 px? | Cost form |
| --- | --- | --- | --- | --- | --- |
| Dark silk border | Separation | 0.06–0.15 | all | **Yes** | shell shader |
| Element silk body | Aura shape | 0.45–0.80 | all | **Yes** | same shell |
| Meridian core | controlled bloom | 1.35–1.9 HDR | launch/cruise/strike | **Yes** | same shell |
| Tip needle | direction | 1.6–2.1 HDR | cruise/strike | **Yes** | same pass |
| Jade-ring catch | Clear Wind identity | ≤0.75 | launch/return | No | hero only |
| Hero tassel echo | secondary motion | ≤0.45 | turn/return | No | hero only |
| Swept silk fin | velocity | 0.20–0.50 | cruise/turn | **Yes** | 24 instanced fins |
| Hero live ribbon | elegant extreme turn | ≤0.45 | turn | Yes | only 2–6 |
| River ribbons | group coherence | ≤0.30 | cruise/turn | group | 2–6 |
| Turn ghost | trajectory punctuation | ≤0.25 | high-curvature only | selective | pooled |

The 64 impostors bake all meaningful layers into a single SDF shader.

#### Metal material

Shape stays identical.

Material:

- blue-black/graphite dark support;
- pale silver-cyan silk;
- longitudinal brushed-qi streak;
- very narrow icy-cyan meridian;
- sparse pearl flash only on hero six.

Motion:

- precise;
- little wobble;
- fast, sharp guard→tip energy pulse.

It should feel **forged and controlled**.

---

#### Fire material

Same geometry.

- charcoal backing;
- amber → burnt orange → warm-gold sheath;
- pale-gold HDR core;
- rear edge receives pointed erosion;
- UV field pulls forms backward into small flame tongues;
- 0–2 ember particles per hero sword at a time.

No red warning language and specifically no #FF4A4A.

Motion:

- slight rear flicker;
- more irregular than Metal;
- still rigid near blade so the sword stays readable.

---

#### Water material

Same geometry.

- deep blue-black support;
- aqua-jade body;
- one or two broad flowmapped value bands;
- smooth rear contour;
- delayed lateral phase in swept fin;
- pale aqua core.

No normal-cruise refraction.

The 80.lv Baltic breakdown is good justification for cheap texture/flowmap-based water detail instead of fluid simulation. [80.lv](https://80.lv/articles/creating-vfx-for-baltic-vfx-content-pack)

---

#### Why it looks premium

The expensive-looking feature is **interaction with the actual Clear Wind design**:

- energy parts around the ring rather than covering it;
- cloud guard becomes visible inside negative space;
- physical tassel feeds naturally into the energy motion;
- real silver remains readable.

That's much more bespoke than adding a generic cyan trail.

#### Revised cost

**My engineering target estimate, not benchmark data:**

**+0.32–0.50 ms p95 at 1080p**

assuming:

- ≤14 live ribbons in heavy cases;
- ~8–11 VFX draw calls;
- tight shell bounds;
- one-pass impostors;
- existing bloom pass;
- no continuous refraction.

**Risk:** medium-low.

---

### 13. Direction B — **Calligraphy Wake**

This is still my strongest option for the **35 px end**.

#### Concept

The physical Clear Wind is the nib of a celestial brushstroke.

But I've changed the implementation substantially from the previous answer:

**there is not a ribbon attached to every sword.**

Instead:

- hero swords may generate short live brush ribbons;
- 24 LOD swords use camera/velocity-facing brush **fins**;
- 64 impostors contain their own short brush tail;
- only 4–8 broad calligraphic currents exist at river level.

The sword always sits **in front of** the stroke.

#### Originality audit

Ink/calligraphy itself is a broad Chinese art motif and cannot sensibly belong to one game.

To keep this direction clearly original, I would prohibit:

- Naraka-style character-surrounding ink clouds;
- copying a known game's brush glyphs;
- copying named calligraphic characters;
- giant circular ink splashes.

Your form is specifically:

**short longitudinal negative-space stroke + physical Clear Wind at its leading tip.**

No reference I surveyed uses this exact package.

##### Layers

| Layer | Role | Brightness | Phase | 35 px? | Implementation |
| --- | --- | --- | --- | --- | --- |
| Dark brush fin | silhouette/contrast | 0.04–0.14 | cruise/turn | **Excellent** | shell/fin/SDF |
| Element filament | magical body | 0.40–0.78 | cruise/turn | **Excellent** | same pass |
| Blade core | sword connection | 1.35–1.9 HDR | active | **Yes** | same shell |
| Tip mark | directional point | ≤2.0 HDR | launch/cruise | **Yes** | same pass |
| Jade “seal” pulse | Clear Wind identity | ≤0.70 | launch/return | No | hero |
| Turn brush ghost | turn punctuation | 0.15–0.27 | turn | **Yes if large** | pooled |
| Hero calligraphy ribbon | flourish | ≤0.38 | extreme turn | Yes | 2–6 only |
| River currents | composition | ≤0.28 | cruise/turn | **Yes group-level** | 4–8 total |

#### Metal

- near-black blue-grey brush body;
- silver-cyan inner filament;
- crisp dry-brush edge breaks;
- straight/ordered motion.

#### Fire

- soot-dark brush;
- amber/gold filament;
- tail edge develops angular burned gaps;
- tiny embers only at hero accents;
- no red.

#### Water

- blue-black brush;
- turquoise/aqua filament;
- brush edge becomes smoother and slightly bulbous;
- flowmap causes one filament to bifurcate and rejoin;
- no literal splash during cruise.

#### Why it works at far camera

A 35 px sword does not have enough pixels to communicate “luxurious jade mist with six little orbiting runes.”

It **does** have enough pixels to communicate:

> narrow physical sword + dark tapered stroke + bright elemental line.

The result should survive the far view extremely well.

#### Revised cost

**+0.24–0.40 ms p95 target estimate**

Typical:

- 6–9 additional VFX draws;
- 6–12 live ribbons;
- smallest transparent footprint of the three.

**Risk:** lowest.

---

### 14. Direction C — **Jade Meridian Lattice**

This is the most showcase-luxurious design, but I have simplified its renderer.

#### Old problem

My previous version proposed 2–4 visible meridian rails around every sword.

That risks:

- multiple transparent surfaces;
- aliasing at 35 px;
- unnecessary draw/fragment cost.

#### Corrected implementation

Use **one shell mesh**.

The fragment shader masks that shell into apparent “rails.”

So four apparent energy rails can still equal **one physical surface / one draw**, not four strips.

#### Concept

Clear Wind sits naked inside a delicate celestial framework.

At large screen size:

- rails originate around the jade ring;
- briefly echo the cloud guard;
- run along open space outside the silver blade;
- converge beyond the point.

Large amounts of negative space keep the sword exposed.

##### Layers

| Layer | Role | Brightness | Phase | 35 px? | Implementation |
| --- | --- | --- | --- | --- | --- |
| Dark cage field | contrast | 0.05–0.14 | all | **Yes** | one shell |
| Meridian rails | ceremonial framing | 0.50–0.80 | cruise | simplify | same shell |
| Central elemental core | focus | 1.3–1.85 HDR | active | **Yes** | same shell |
| Tip convergence | authority | ≤2.0 HDR | cruise/strike | **Yes** | same shell |
| Jade anchor | connects real guard to aura | ≤0.78 | heroes | No | shell/hero |
| Cloud echo | bespoke ornament | ≤0.58 | launch/turn | No | >80 px only |
| Swept fin | velocity | ≤0.40 | cruise/turn | **Yes** | instanced |
| River lattice threads | formation unity | ≤0.30 | high state | group | only 2–4 |

##### Screen-size LOD

**>90 px:** four apparent rails + cloud echo.

**55–90 px:** two rails.

**<55 px:** shader merges them into one sheath rim + central core.

That transition is essential.

---

#### Metal

- perfectly controlled silver-cyan rails;
- faint guard→tip travelling pulse;
- cool jade anchor;
- very low noise.

#### Fire

- same rails, but segmented by amber/gold erosion;
- energy pulse jumps between segments;
- charcoal support;
- no broad flame envelope.

This gives Fire a divine-forge appearance rather than turning the sword into a torch.

#### Water

- aqua rails;
- UV phase offset makes them appear to weave;
- broad flowmapped intensity change;
- smooth droplet-like tip convergence.

Geometry does not physically weave—only the material does.

#### Why it looks luxurious

It resembles energy **crafted specifically around a precious artefact**.

Negative space makes the jade ring, silver blade and cloud guard look more expensive rather than obscuring them.

#### Revised cost

**+0.36–0.54 ms p95 target estimate**

Typical:

- ~8–12 VFX draws;
- 6–10 live ribbons;
- more shader work than A/B.

**Risk:** highest. Still potentially under +0.6 ms, but I'd reject it if its measured p95 lands above ~+0.52 because you need safety margin.

---

### 15. Performance ranking under the new caps

| Rank | Direction | 35 px read | Clear Wind identity | Luxury close | Typical live ribbons | VFX draws target | Est. +GPU p95 | Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | **River-Silk Sheath** | 9/10 | **10/10** | **9.5/10** | 6–14 | 8–11 | **0.32–0.50 ms** | Low–Med |
| **2** | **Calligraphy Wake** | **10/10** | 8.5/10 | 8.5/10 | 6–12 | **6–9** | **0.24–0.40 ms** | **Lowest** |
| **3** | **Jade Meridian Lattice** | 8/10 after LOD | **10/10** | **10/10** | 6–10 | 8–12 | **0.36–0.54 ms** | Highest |

All three:

- keep the real sword exposed;
- bloom only a thin HDR core;
- keep halo/ring/body ≤0.9;
- put dark support behind every bright region;
- cap neutral-white core contribution at 30%;
- exclude #FF4A4A;
- stay far below 32 ribbons;
- target far below 32 VFX draws;
- are designed around roughly ≤3 transparent field overlaps.

But the GPU figures are **not yet verified performance facts**. They are budget estimates. The designs only pass when your actual WebGL profiler confirms them.

---

### 16. How I would actually measure acceptance

Use EXT_disjoint_timer_query_webgl2; MDN confirms that GPU timer queries measure command duration without stalling, and explicitly notes the WebGL2 extension name. [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/EXT_disjoint_timer_query)

Profile these separately:

| Test | Why |
| --- | --- |
| Aura entirely OFF | baseline |
| 94 straight cruise | steady-state cost |
| 94 swords hard 90° turn | maximum fin/ribbon load |
| tight swarm convergence | worst transparent overdraw |
| six heroes + 24 LOD + 64 impostors all on bright terrain | readability + fill-rate |
| all six hero strikes same frame | hit peak |
| Water material | extra flowmap sampling |
| Fire material | alpha/erosion stress |
| 60-second representative fight | real p95 |

Record:

**p50 / p95 / p99 / max GPU delta.**

My pass criterion would be:

- **p95 ≤ +0.50 ms:** comfortable PASS;
- **+0.50–0.60:** technically passes requirement, but optimisation recommended;
- **>+0.60:** FAIL.

If a direction fails, remove in this order:

**extra river ribbons → depth fade → hero particles → ground light → secondary texture octave**

before touching the core physical sword/sheath.

---

### 17. The most important art rule

After this re-audit, I would put one rule at the top of Claude's implementation spec:

> **At any instant during the river, the player must be able to identify at least a few objects as real Clear Wind swords, while the remainder may collapse into sword-shaped directional rhythm.**

That conclusion is **my synthesis**, but the strongest evidence behind it is surprisingly consistent:

- Qingxiao fans explicitly disliked swords becoming overly transparent/VFX-like. [Reddit +1](https://www.reddit.com/r/Qingxiao/comments/1v69j6d/qingxiao_moveset_lest_goo/)
- Yanqing demonstrates how much fantasy value comes simply from recognizable flying swords. [Reddit](https://www.reddit.com/r/HonkaiStarRail/comments/16jf4xw/)
- Wuchen shows that hierarchy between small and important swords improves a large sword-rain sequence. [Reddit +1](https://www.reddit.com/r/NarakaBladePoint/comments/1l1wis3)
- Sword of Coming's reviewer likes refined small-scale energy behaviour but specifically dislikes the huge energy-sword attacks when they lose refinement. [Reddit +1](https://www.reddit.com/r/Donghua/comments/1nea5pb/sword_of_coming_review/)
- Riot's own guidance says VFX should remain readable and clearly attributable to their source. [Riot Games](https://www.riotgames.com/vi/artedu/visual-effects)

That combination is more persuasive to me now than in the first answer.

---

### 18. Five sources I trust most for the build decision

| Rank | Source | Why |
| --- | --- | --- |
| **1** | **Kuro — Qingxiao / Wuthering Waves 3.6 + 3.7 official material** | Closest actual contemporary reference to your flying-sword fantasy, and confirms Sword Flight/ten-thousand-blade language. [Wuthering Waves +2](https://wutheringwaves.kurogames.com/es/main/news/detail/5272?utm_source=chatgpt.com) |
| **2** | **Riot — Visual Effects** | Very clear first-party statement of spectacle vs gameplay clarity and effect-source identity. [Riot Games](https://www.riotgames.com/vi/artedu/visual-effects) |
| **3** | **HoYoverse — Xiao Developer Insight** | Rare primary discussion of Chinese-fantasy visual language: jade, clouds, colour, hanging forms and motion. [Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com) |
| **4** | **GDC VFX Bootcamp + Rocksteady Attention Overload** | Strong professional foundation for timing, hierarchy and dense-combat readability. [GDC Vault +1](https://www.gdcvault.com/play/1023943/Visual-Effects-Bootcamp-Artistic-Principles) |
| **5** | **Three.js/NVIDIA/Valve technical sources** | Directly applicable to your browser renderer: batching, transparency/overdraw and SDF impostors. [Three.js +2](https://threejs.org/docs/pages/BatchedMesh.html) |

#### What I changed from my first answer

I corrected five meaningful things.

1. **Qingxiao survives the audit strongly.** She is real, launched with Wuthering Waves 3.6 on **August 20, 2026**, is an Aero Sword Resonator, and Kuro explicitly uses Sword Flight plus ten-thousand-flying-blade language. [Wuthering Waves +2](https://wutheringwaves.kurogames.com/es/main/news/detail/5272?utm_source=chatgpt.com)
2. **I removed unsupported attribution.** The Where Winds Meet homepage did not substantiate my “lightness/agility” wording; the Justice Online camera-optimisation claim could not be robustly reverified; the 80.lv article did not say what I attributed to it about micro-detail.
3. **I added the negative evidence.** Sword of Coming's reviewer praises refined energy work but explicitly dislikes huge energy-flying-sword effects when they get rough. Qingxiao beta fans likewise object to physical swords dissolving into transparent VFX. Those are directly relevant warnings. [Reddit +1](https://www.reddit.com/r/Donghua/comments/1nea5pb/sword_of_coming_review/)
4. **I demoted weak references and added better ones.** Soul Land: Sword Master/Chen Xin, Swords of Legends' flying-sword class, Jade Dynasty, Daily Life's spiritual-sword identity and Sword and Fairy's Chinese-fantasy combat are now placed according to what the sources actually establish—not all labelled “sword-rain benchmarks.”
5. **Most importantly, I rebuilt all three designs around your actual engine limits.** There are no longer 94 independent ribbons. The corrected system uses **shells + instanced fins + one-pass SDF impostors + roughly 4–8 river-level ribbons**, with ordinary heavy cases around 6–16 total live ribbons rather than approaching your 32-ribbon ceiling.

My preferred production order after this audit is **River-Silk Sheath first, Calligraphy Wake second as the performance/readability fallback, and Jade Meridian Lattice only after the first two are GPU-profiled**.

## D. Câu trả lời đầu, trước khi tự rà soát (nguyên văn)

I searched across primary game material, official patch notes, GDC/Riot material, 80.lv and ArtStation breakdowns, engine/GPU documentation, plus fan discussions. One important caveat: **I found no public HoYoverse/Kuro/NetEase rendering breakdown that says “Yanqing/Qingxiao/Wuchen uses technique X.”** So I will not invent one. When I discuss how *your* three.js version should reproduce the principle, I label it **My inference**.

Fan reaction is also qualitative sampling, not a popularity poll.

#### Executive conclusion

The best answer for Clear Wind is **not “more particles.”** It is a three-scale hierarchy:

**6 hero swords = jewellery. 24 LOD swords = shape. 64 impostors = rhythm.**

The six hero swords should visibly remain *Clear Wind*: silver blade, jade ring, cloud guard, tassel. The next 24 need only retain blade + guard silhouette plus the aura's major shape. The final 64 should intentionally cease being miniature detailed weapons and become sword-shaped directional marks—but the river must always contain enough clearly physical swords that the viewer's brain interprets those marks as more Clear Winds.

That direction is strongly supported by the reaction to Qingxiao. Players praise her sword-cultivator fantasy and spectacular animation, but some specifically ask for swords to remain visible longer and look “less VFX-y, more physical”; another discussion says the appeal is thousands of **swords** flying around rather than yet another generic giant energy strike. [Reddit +2](https://www.reddit.com/r/WutheringWaves/comments/1vhxs99/qingxiao_convene_animation/?utm_source=chatgpt.com)

And it agrees with professional VFX guidance: Riot explicitly says VFX artists need restraint so players understand the action, while stylized VFX specialists emphasize strong shape, colour, form and timing over small noisy detail. [Riot Games +2](https://www.riotgames.com/vi/artedu/visual-effects)

Here are useful visual references side by side. Look less at their exact ornament and more at **how much of a sword remains identifiable versus how much becomes a directional energy shape**:

55 images

---

### 1. Flying-sword / sword-qi looks that are actually worth studying

##### 1. Qingxiao — Wuthering Waves: probably the strongest current benchmark

For your specific problem, **Qingxiao is the most useful contemporary reference I found**. Kuro's current game actually gives her a Sword Flight state, and the official 3.7 patch notes still refer explicitly to Sword Flight, Sword Step and Ephemeral Transcendence. Her official combat material revolves around the sword-cultivator fantasy rather than merely giving a normal swordswoman blue attack trails. [Wuthering Waves +1](https://wutheringwaves.kurogames.com/en/main/news/detail/5571?utm_source=chatgpt.com)

The fan response to the presentation is unusually strong. Her convene animation thread includes reactions such as “this is art,” “really, really good,” and praise across combat, skills, ultimate, SFX and mobility; a separate animation thread reached 1,271 votes with repeated reactions calling it beautiful, cinematic and essentially a short movie. [Reddit +1](https://www.reddit.com/r/WutheringWaves/comments/1vhxs99/qingxiao_convene_animation/?utm_source=chatgpt.com)

More importantly for Clear Wind, players notice the *physical swords*. A Qingxiao animation discussion praises the fact that her swords don't clip into angled ground and highlights her detailed recovery animations. Earlier beta feedback explicitly asked for swords to persist longer and be “less VFX-y more physical.” [Reddit +1](https://www.reddit.com/r/WutheringWaves/comments/1w7f6n1/this_little_animation_is_top_tier/?utm_source=chatgpt.com)

And during animation revisions, players noticed seemingly small changes—additional swords, black cinematic accents, hitlag and shake—and said the attacks gained weight. [Reddit](https://www.reddit.com/r/WutheringWavesLeaks/comments/1vcki40/qingxiao_v2_animations_via_seele/?utm_source=chatgpt.com)

**My inference:** this is the clearest warning against turning Clear Wind into a cyan missile. You need a visible *sword population* inside the river, with the abstract streak population supporting it.

---

##### 2. Yanqing — Honkai: Star Rail: clearest iconic “御剑” read

Yanqing remains one of the most culturally legible pure yu-jian examples: hovering swords, riding a sword, then commanding swords downward. HoYoverse's own character trailer climaxes around the command for the swords to descend. [YouTube](https://www.youtube.com/watch?v=2TY_i3n-7jY&utm_source=chatgpt.com)

The reaction is interesting because players don't only praise graphical fidelity—they immediately recognize the trope. In one highly engaged HSR thread, users joke that Chinese fantasy has taught them that competent characters “ride on flying swords” and summon swords behind them. [Reddit](https://www.reddit.com/r/HonkaiStarRail/comments/16jf4xw)

That matters. **The prop/action itself carries fantasy value.** You therefore don't have to cover Clear Wind in enormous effects to communicate xianxia power.

**My inference:** Yanqing demonstrates why your jade ring, guard and sword silhouette are assets rather than obstacles. Letting a viewer actually see the sword increases the cultural read.

---

##### 3. Wuchen — Naraka: Bladepoint: best reference for sword-rain hierarchy

NetEase's official 2024 rework gave Wuchen **Tai Chi Teleport: Blade Storm**, with an aimed spell followed by a “series of spirit blades.” Their developer note calls Wuchen's skill design a team favourite and describes Blade Storm specifically as an “enduring sword rain.” [narakathegame.com](https://www.narakathegame.com/news/update/20240719/33459_1168466.html)

The gameplay structure is even more useful than the graphics. Players describe the storm as an ordered cadence: multiple small swords → a large sword with a distinctive high-pitched cue → more small swords → two final large swords. [Reddit](https://www.reddit.com/r/NarakaBladePoint/comments/1l1wis3)

That is a valuable antidote to visual soup.

**My inference:** don't make all 94 Clear Winds equally important. A beautiful swarm needs visual punctuation. Six hero swords should periodically become the commas/exclamation marks among the 88 supporting marks.

---

##### 4. Sword of Coming / Jian Lai: probably the strongest donghua reference for refined energy treatment

A detailed fan review praises its filmmaking and animation, but specifically calls out the stylised **afterimages in clashes and slashes**, the detailed treatment of magical objects, and unusually pristine behaviour of surrounding energy waves. The reviewer describes the episode-26 sword-granting sequence as an “out of body cinematic experience.” [Reddit](https://www.reddit.com/r/Donghua/comments/1nea5pb/sword_of_coming_review/)

This is particularly relevant because its appeal isn't just “lots of glowing stuff.” Fine behaviour of the energy shape and afterimage timing is noticed.

**My inference:** borrow the principle of *precise, elegant secondary movement*. For Clear Wind, one controlled ghost/afterimage on a direction change will look more expensive than twelve random motes.

---

##### 5. A Record of a Mortal's Journey to Immortality: strongest reference for keeping magical artefacts physical

RMJI receives repeated praise for its visual quality and more grounded cultivation presentation; one Donghua community discussion describes the production quality as unusually high and recommends it specifically to people looking for a similar visual style. [Reddit](https://www.reddit.com/r/Donghua/comments/1o10etd)

**Visual inference:** compared with more abstract gacha VFX, Han Li's magical weapons frequently retain a strong physical-object read inside their green/gold/cyan energy treatment. That is exactly the useful part for Clear Wind; I'm deriving this from the visual material, not from a published studio VFX breakdown.

---

##### 6. Genshin's Xiao / Shenhe / Xianyun: not a flying-sword benchmark, but an excellent *adeptus material-language* benchmark

HoYoverse's Xiao developer article is unusually valuable because it explains the actual art decisions. His palette combines white/green adeptal imagery with dark malevolent energy; attacks deliberately mix light and darkness; jade jewellery helps communicate mystery and longevity; cloud motifs and hanging streamers contribute antiquity and ethereality. The animation team also sought light, decisive movement, and described his skill's motion in terms of an arrow passing straight through the air. [Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642)

That is a better source for Clear Wind than simply copying a Genshin screenshot. Genshin's 2021 GDC presentation likewise describes the deliberate art-core/pipeline decisions behind its anime-styled rendering rather than treating “anime” as a post-process filter. [GDC Vault](https://www.gdcvault.com/play/1027540)

**My inference:** your **white jade ring + cloud guard + tassel** should actively participate in the VFX grammar. Right now they are probably passengers. A premium aura can originate at the jade ring, curve around the cloud guard, and pull the tassel into the wake.

---

##### 7. Justice Online / Ni Shui Han: useful current evidence that the sword-riding/myriad-sword fantasy remains desirable

The official Ni Shui Han account promoted its June 2026 “御剑·极” traversal effect with the phrase **万剑归宗** and sword-riding imagery. An earlier official update also describes a region where players unlock free sword flight, including camera/feel optimisation for diving and low-altitude movement. [Weibo +1](https://weibo.com/u/7460249375?index=183&tabtype=album&uid=7460249375&utm_source=chatgpt.com)

That doesn't tell us how to render your aura, but it reinforces that the fantasy is not an old niche effect.

---

##### 8. Where Winds Meet: useful because it is comparatively restrained wuxia

Its official site describes sword motion in terms of lightness and agility; recent patches explicitly adjust Nameless Sword's released **sword energy** and animation timing. [wherewindsmeetgame.com +1](https://www.wherewindsmeetgame.com/?from=AppAgg.com&utm_source=chatgpt.com)

Meanwhile, players repeatedly ask for more flying-sword abilities or actual sword riding, and one Strategic Sword thread describes the sword as particularly satisfying to use. [Reddit +2](https://www.reddit.com/r/wherewindsmeet_/comments/1qsvgr0/new_sword_martial_art_teased/?utm_source=chatgpt.com)

**My inference:** WWM is useful as the lower end of your intensity scale: how much of the fantasy remains when the underlying sword action is still dominant.

---

##### 9. Moonlight Blade: useful as evidence for separating sword SHAPE from elemental MATERIAL

One Moonlight Blade raid design repeatedly uses an identifiable sword motif and then changes the elemental treatment into **lightning sword, fire sword and wind sword** mechanics. [17173 News](https://news.17173.com/content/10282023/093214220.shtml?utm_source=chatgpt.com)

That isn't a studio VFX breakdown, so confidence is lower than the official sources above, but the conceptual separation is exactly your proposed architecture:

**Sword/aura geometry = semantic shape.
Element = material language.**

---

##### 10. Onmyoji / Tower of Fantasy / Black Myth

Onmyoji's Susanoo is a useful elemental-sword reference: players specifically reacted positively to his lightning visuals, although feedback also shows how strongly colour and silhouette influence character identity. [Reddit +1](https://www.reddit.com/r/Onmyoji/comments/x9puzz?utm_source=chatgpt.com)

Tower of Fantasy is less directly useful for Clear Wind, but current community discussion still calls out certain weapon effects specifically for being “gorgeous,” showing that weapon-VFX identity itself is a significant attraction. [Reddit](https://www.reddit.com/r/TowerofFantasy/comments/1mir21p?utm_source=chatgpt.com)

Black Myth: Wukong is **not** a flying-sword benchmark. I'd use it only as a reference for keeping real surfaces/materials visually convincing underneath supernatural effects. Game Science's own material confirms the importance of the real-time models, shaders, lighting and VFX working together; its art director's ArtStation page explicitly identifies those as separate production disciplines. [Unreal Engine +1](https://www.unrealengine.com/developer-interviews/black-myth-wukong-wows-with-ue5-early-access-visuals?lang=en-US)

##### So which are most useful / loved?

My synthesis from the fan evidence—not an objective poll—is:

1. **Qingxiao** — strongest current direct flying-sword spectacle.
2. **Sword of Coming** — strongest refined cinematic sword-energy treatment.
3. **Yanqing** — most immediately legible/iconic pure yu-jian fantasy.
4. **RMJI** — strongest physical-magical artefact balance.
5. **Wuchen** — strongest gameplay-readable sword-rain cadence.

---

### 2. What actually makes a flying sword look premium

Professional VFX sources converge on the same fundamentals. Riot describes the problem as balancing spectacle with clarity; 80.lv's Matt Schwartz says stylized effects deliberately simplify microdetail so shape, colour and form read quickly; the GDC VFX Bootcamp similarly centres artistic and gameplay fundamentals rather than particle quantity. [Riot Games +2](https://www.riotgames.com/vi/artedu/visual-effects)

An especially relevant RealTimeVFX breakdown literally builds a sword aura from an attached mesh with scrolling noise and a mask, and puts a dark “glow” behind a bright blink to make it stand out. [Real Time VFX](https://realtimevfx.com/t/renseis-sketchbook/20495/24?u=rensei)

#### Layer hierarchy for Clear Wind

The brightness figures below are **my design recommendation**, expressed relative to ordinary non-HDR material white ≈ 1.0 before your existing tonemapping/exposure. They are not numbers from the referenced games.

| Layer | Job | Suggested output | 35 px? | 70–130 px? |
| --- | --- | --- | --- | --- |
| **Dark under-sheath** | Separates sword/aura from ground, enemies and other swords | 0.05–0.18 | **Essential** | Essential |
| **Qi sheath** | Main aura silhouette hugging blade | 0.45–0.85, non-HDR | **Essential** | Essential |
| **Thin energy core** | Magical sharpness / controlled bloom | ~1.3–2.2 HDR, ≤30% white mix | **Yes** | Yes |
| **Physical blade specular** | Keeps actual silver sword alive | existing PBR | **Yes** | Yes |
| **Wake ribbon / fin** | Shows direction and speed | 0.25–0.70 | **Essential** | Essential |
| **Tip star** | Makes direction instantly readable | tiny HDR point | **Yes** | Yes |
| **1 ghost sword** | Turn/acceleration punctuation | 0.15–0.40 | Conditional | Excellent |
| **Jade-ring accent** | Makes Clear Wind uniquely Clear Wind | ≤0.75 | No | **Excellent** |
| **Tassel streamer** | Secondary organic motion | ≤0.55 | No | **Excellent** |
| **Rune/detail flow** | Luxury close-up material information | ≤0.55 | **No** | 100 px+ only |
| **Motes** | Atmosphere/energy shedding | ≤0.6 | Mostly no | Sparse only |
| **Distortion** | Strike power | N/A | No | strike only |
| **Ground light/shadow** | Anchors airborne swarm against terrain | 0.1–0.35 | **Group-level only** | Group + heroes |

The most important finding for your camera is:

> **At 35 px, decoration is almost irrelevant. Silhouette enlargement, value contrast, direction and timing are the luxury.**

That is consistent with the stylized-VFX advice to remove micro-detail in favour of readable large shapes. [80.lv](https://80.lv/articles/from-realism-to-stylization-game-vfx-production)

##### My proposed screen-space widths

At roughly 35 px sword length:

- physical sword: keep untouched;
- dark under-sheath: project **~1–1.5 px beyond** the coloured aura;
- coloured sheath: only **~2–3.5 px total expansion** around the sword;
- core: roughly **0.8–1.3 px apparent width**;
- tip star: **2–3 px**;
- useful wake: roughly **8–16 px**.

At 100–130 px, the sheath can become ~4–7 px wide and reveal its internal material pattern.

I would not use GL_LINES for this. **My inference:** use actual thin triangles/shell geometry or camera-facing fins so the screen thickness remains art-directable.

---

### Phase behaviour

A good sword aura should not simply remain “on.”

A professional melee VFX breakdown on ArtStation shows exactly this kind of temporal staging: glow before impact, ribbon and sparks during movement, a very short impact/distortion moment, followed by erosion/fade once the attack loses speed. [Robbert Mouthaan](https://robbertmouthaan.artstation.com/projects/L49NVk)

##### Launch

**Final typing key should trigger visible response immediately.** Don't spend 100 ms “charging” after the player finishes typing.

My design:

**0–1 frame:** jade ring catches a compact dark halo; tip core appears immediately.
**Next ~60–90 ms:** aura sheath draws from guard → tip.
**Then:** wake unfolds behind it.

The physical sword should remain fully visible during the whole process.

##### Cruise

This should actually be the **quietest phase**:

- stable narrow sheath;
- one narrow core;
- short directional wake;
- no per-sword explosion particles;
- no constant distortion;
- few or zero motes on LOD swords.

A river looks expensive when it is coherent, not when every component is independently screaming.

##### Turn

This is where the aura can earn its money:

- wake becomes wider on the outside of the curve;
- 1 ghost sword appears on high angular acceleration;
- tip star stretches slightly;
- tassel lags on six hero swords;
- sheath remains physically attached to blade.

**My inference:** curvature should drive VFX more strongly than raw velocity. A straight fast sword already reads fast; a sharp turn needs help showing its trajectory.

##### Strike

Collapse before explosion:

1. broad sheath contracts toward blade;
2. thin HDR core spikes;
3. sword remains readable for the contact frame;
4. tiny impact graphic;
5. optional distortion only around the six hero impacts;
6. trailing aura peels away afterwards.

That “narrow → sharp → broad decay” gives impact without needing a huge white blob.

##### Return

Don't simply play launch backward.

Use:

- tip brightness decays first;
- wake rolls back toward guard;
- jade ring gives one small closure pulse;
- tassel catches up last.

That produces the “controlled immortal weapon” feeling rather than “projectile despawn.”

---

### What survives at 35 px?

##### Keep

- sword silhouette;
- dark backing;
- coloured sheath;
- thin core;
- tip accent;
- one strong wake;
- formation rhythm;
- collective ground shadow/light;
- **large** turn ghost.

##### Kill

- glyphs;
- little orbiting runes;
- individual 1 px motes;
- multiple concentric guard rings;
- internal caustics on every sword;
- refractive distortion;
- several trails per sword;
- fancy tassel VFX on the 24/64 population.

This also protects your typing UI. Rocksteady's GDC presentation frames dense-combat VFX as an attention-management problem: effects should steer attention rather than simply add information. [GDC Vault](https://gdcvault.com/play/1034360/Attention-Overload-Creating-Readable-VFX)

---

### 3. How to make 94 swords cheap

Here I need to distinguish hard evidence from engineering recommendation.

##### What is documented

Three.js InstancedMesh exists specifically to draw large numbers of identical geometry/material instances with different transforms while reducing draw calls. [archive.threejs.org](https://archive.threejs.org/docs/api/en/objects/InstancedMesh.html)

BatchedMesh can similarly combine many instances/geometry variants under the same material and supports per-object sorting where required. [Three.js](https://threejs.org/docs/pages/BatchedMesh.html)

The underlying rationale is old and solid: submitting many tiny similar objects individually causes disproportionate API/CPU overhead, which is exactly the use case geometry instancing solves. [NVIDIA Developer](https://developer.nvidia.com/gpugems/gpugems2/part-i-geometric-complexity/chapter-3-inside-geometry-instancing)

The other major enemy is **transparent fill-rate**, not triangle count. NVIDIA's particle-performance discussion notes that overlapping translucent effects can create effectively unbounded overdraw and become expensive even in otherwise sophisticated games. [NVIDIA Developer](https://developer.nvidia.com/gpugems/gpugems3/part-iv-image-effects/chapter-23-high-speed-screen-particles)

Three.js's own documentation also warns that transparency is complicated because of depth/sorting interactions. [Three.js](https://threejs.org/manual/pages/transparency.html)

##### What is *not* documented

I found no credible public source saying:

- “Qingxiao uses GPU instancing,”
- “Yanqing's swords use X impostor technique,” or
- “Wuchen's Blade Storm uses ribbon implementation Y.”

So any claim like that would be speculation.

---

#### My recommended architecture for your 6 + 24 + 64

##### Six full swords: **jewellery tier**

Keep:

- real Clear Wind model;
- proper PBR;
- blade-hugging aura shell;
- jade-ring accent;
- actual tassel + VFX streamer if necessary;
- one short wake;
- turn ghost;
- strike-only distortion;
- optional guard-level ornament.

These six sell the fantasy.

##### 24 LOD swords: **shape tier**

Keep:

- simplified physical Clear Wind mesh;
- dark/colour aura silhouette;
- thin energy core;
- one wake fin;
- tip star.

Remove:

- tassel simulation;
- small guard detail;
- runes;
- individual motes;
- distortion.

##### 64 impostors: **rhythm tier**

One atlas/material should already contain:

- dark sword silhouette;
- physical silver central blade read;
- coloured aura;
- tiny bright core;
- tip accent.

So you don't render five transparent sprites to construct one impostor.

Velocity-stretch the billboard slightly, but **do not let it become a featureless laser**.

---

#### One more important optimisation: effects belong to the *river*, not every sword

Instead of:

> 94 swords × 5 decorative effects

use:

> 94 sword marks + **1 river-level atmospheric system**.

For example:

- one broad, extremely faint ground-space river shadow;
- one pooled stream of motes through the formation;
- perhaps two large flowing qi wisps through the entire swarm;
- shared impact dust when several blades land.

This makes the group visually richer while actually reducing repetition.

---

#### Draw-call target

**My proposed implementation:**

1. aura dark shell — 30 mesh instances;
2. colour sheath/core — same 30 instances;
3. wake fins — 30 instanced low-poly strips;
4. impostor batch — 64 sprites/quads;
5. one group-level ground ribbon;
6. optional strike extras for six hero swords.

You should be able to keep normal cruise at roughly **4–6 aura draw calls**, depending on how aggressively you combine materials.

Element should be an instance/material parameter, **not duplicated geometry**.

---

#### Shader animation instead of particle simulation

Use per-instance attributes such as:

- phase;
- speed;
- turnRate;
- seed;
- elementId;
- importanceLOD.

Then let the vertex/fragment shader control:

- sheath width;
- flow offset;
- wake length;
- alpha erosion;
- turn widening;
- pulse position.

That moves your richness from spawning objects into cheap deterministic variation.

This is conceptually consistent with professional hand-crafted VFX practice: Jason Keyser describes combining authored meshes and textures with animated materials so painted effects “dance” without requiring simulation-heavy solutions. [80.lv](https://80.lv/articles/jason-keyser-on-in-game-vfx-and-the-demand-for-fx-artists)

---

#### Distortion should be almost absent

Don't sample the scene through 94 refractive objects.

Use distortion only:

- six hero swords;
- strike phase;
- perhaps 1–2 frames;
- tight screen bounds.

Fire heat haze can share the same mechanism later.

Water should **not** require refraction during cruise. Fake water body movement with shape, UV flow and value change.

---

#### Bloom

Your existing rule is correct:

**only the core enters HDR bloom.**

Do not add an additional selective-bloom scene/pass solely for the aura if your current pipeline can already pick up HDR pixels. The extra rendering/compositing pass could cost more than the actual sword geometry.

---

#### Ground treatment

Do not cast real extra lights or real sword shadows for 94 swords.

**My inference:** create one or several low-opacity projected ribbon/decal shapes representing the *river's aggregate presence*. The six hero swords can optionally add tiny strike decals.

---

#### How I would validate the +0.6 ms target

Use GPU timing, not only JavaScript frame time. EXT_disjoint_timer_query_webgl2 is designed to measure elapsed GPU command time without synchronously stalling the rendering pipeline. [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/EXT_disjoint_timer_query)

Measure:

- aura off baseline;
- straight cruise;
- maximum curved turn;
- 94-sword convergence;
- all six hero impacts simultaneously;
- over a long enough sample to report **p50 / p95 / worst**.

Your failure mode will probably be **transparent pixel coverage**, not the 94 transforms.

---

### 4. Three original Clear Wind directions

None of these copies an existing game's exact design.

---

### Direction A — **River-Silk Sheath**

This is the one I would build first.

The fantasy is: **the sword is dressed in flowing immortal silk made of qi.** The silk hugs the weapon instead of creating a replacement weapon around it.

| Layer | Role | Brightness | Phase | 35 px |
| --- | --- | --- | --- | --- |
| Dark silk under-shell | Separates sword/aura | 0.08–0.16 | all | **Yes** |
| Main qi sheath | Soft aerodynamic sword silhouette | 0.5–0.82 | all except final fade | **Yes** |
| Meridian core | Sharp energy spine | HDR ~1.4–2.0 | launch/cruise/strike | **Yes** |
| Split silk wake | Gives flowing direction | 0.3–0.6 | cruise/turn/return | **Yes** |
| Jade-ring pulse | Makes Clear Wind unique | ≤0.7 | launch/return | No |
| Single turn ghost | Makes banking luxurious | 0.2–0.35 | sharp turn only | Medium |
| Tassel continuation | Joins physical tassel to energy wake | ≤0.5 | hero six only | No |
| Tip needle | Direction/focus | tiny HDR | cruise/strike | **Yes** |

##### Shape

Imagine a transparent silk sleeve only a few centimetres away from the blade. Near the guard it subtly splits around the jade ring/cloud guard; behind the sword it becomes two asymmetrical ribbon tails.

The aura does **not** cross the central 60–70% of the projected blade area. That leaves real silver visible.

##### Metal

- dark underlayer: very deep blue-grey;
- sheath: pale cyan/silver;
- internal movement: very subtle longitudinal brushed-qi texture;
- core: ~70% cyan-silver + maximum 30% neutral white;
- occasional pearl-like sparkle only on six heroes.

##### Fire

Keep identical geometry.

Swap material to:

- charcoal / extremely dark aubergine underlayer;
- amber → orange qi silk;
- narrow pale-gold core rather than white;
- flowmap introduces pointed trailing licks only toward the rear;
- a few embers shed only from hero six.

**No #FF4A4A and no generic saturated red outline.**

##### Water

Again, same geometry:

- dark navy/teal backing;
- aqua-jade translucent silk;
- one broad moving caustic band rather than fine noise;
- rear ribbon bends with slightly delayed sinusoidal motion;
- tip becomes a narrow droplet/needle shape.

No continuous screen refraction.

##### Why it looks expensive

The aura behaves like a custom-made garment for **this particular sword**. The jade ring and cloud guard remain visible and actually become structural anchors.

It should feel closer to jewellery/fashion design than a shooter projectile.

##### Cost estimate

**My engineering estimate, not a measured benchmark: ~+0.28–0.45 ms p95** at 1080p if:

- 30 mesh aura instances;
- 64 single-pass impostors;
- transparent footprints remain tight;
- distortion is impact-only;
- bloom already exists.

This gives the healthiest margin below your +0.6 ms ceiling.

---

### Direction B — **Calligraphy Wake**

This is the strongest far-camera solution.

The fantasy is: **the sword writes a piece of heavenly calligraphy through space.**

Crucially, the “ink” is behind the physical sword, not covering it.

| Layer | Role | Brightness | Phase | 35 px |
| --- | --- | --- | --- | --- |
| Dark brush wake | Primary graphic silhouette | 0.04–0.15 | cruise/turn | **Excellent** |
| Thin coloured filament | Magical energy through brush stroke | 0.55–0.85 | cruise | **Excellent** |
| Blade edge core | Connects wake back to physical blade | HDR | all active | **Yes** |
| Tip spark | Stroke's leading point | HDR | launch/cruise | **Yes** |
| Brush ghost | Direction-change punctuation | 0.15–0.30 | turns | **Yes** |
| Jade stamp-ring | Tiny “seal” accent | ≤0.75 | launch/return | No |
| Shared river wisps | Integrates swarm into one composition | ≤0.4 | cruise | Group-level |

##### Shape

The sword moves at the **leading edge of a dark tapered brush stroke**.

Inside the dark stroke is one narrow elemental streak.

This exploits your mandatory “dark behind bright” rule as an art feature rather than a technical precaution.

##### Metal

- ink: almost-black blue;
- filament: silver-cyan;
- edge breakup: occasional dry-brush gaps;
- tip: hard cyan-white needle.

##### Fire

- stroke: charcoal/soot;
- filament: amber/orange;
- rear edge breaks into small flame-shaped negative gaps;
- extremely sparse ember specks.

##### Water

- stroke: blue-black ink;
- filament: turquoise;
- edges become smoother and more rounded;
- filament gently bifurcates/rejoins like a stream.

##### Why it is captivating

At 35 px, it may actually read **better than Direction A** because it depends on one huge compositional idea: black brush + brilliant sword.

When 94 swords turn together, the strokes form a calligraphic current.

It also prevents the classic cyan-on-bright-ground disappearing problem.

##### Luxury/modernity risk

The risk is that if the brush shape becomes too long or chunky, Clear Wind feels like an icon moving in front of a 2D anime slash.

Keep cruise trails short and save dramatic brush expansion for turns/strikes.

##### Cost estimate

**My estimate: ~+0.20–0.34 ms p95.**

This should be the cheapest because most swords need only one dark/colour ribbon shape, while impostors can bake the entire identity into one sprite.

---

### Direction C — **Jade Meridian Lattice**

This is the most luxurious in close view and the riskiest at 35 px.

The fantasy is: **Clear Wind is a precious divine artefact held inside a floating energy setting, like a gemstone in fine celestial metalwork.**

| Layer | Role | Brightness | Phase | 35 px |
| --- | --- | --- | --- | --- |
| Thin dark sheath | Contrast foundation | ~0.1 | all | **Yes** |
| Two/four meridian rails | Open cage around sword | 0.55–0.85 | cruise | Merge to 1–2 lines |
| Jade anchor ring | Connects lattice to real guard | ≤0.8 | all heroes | No |
| Cloud-guard arcs | Echoes the physical cloud shape | ≤0.65 | launch/turn | No |
| Tip convergence | Rails meet at needle point | HDR | cruise/strike | **Yes** |
| Orbit filament | Adds ceremonial sophistication | ≤0.45 | hero six only | No |
| Snap ghost | Lattice separates briefly on acceleration | 0.2–0.35 | turn/strike | Medium |
| Wake | Very narrow | ≤0.55 | cruise | **Yes** |

##### Shape

Rather than a solid aura envelope, two to four lines run close to Clear Wind's sides without touching the blade.

They begin around the jade ring, travel longitudinally, and converge just beyond the point.

There is lots of negative space, so the sword remains exposed.

##### Metal

- geometric, almost perfectly straight cyan/silver rails;
- faint pulses travel guard → tip;
- ring gets a cold jade accent.

##### Fire

- rails become segmented molten-gold/amber energy;
- pulses hop across tiny gaps;
- dark shell becomes charcoal;
- no thick flame shell—the geometry itself stays elegant.

##### Water

- rails become flowing aqua threads;
- their phase is offset so they gently weave around the blade;
- convergence point stretches into a clear droplet-like taper.

##### Why it looks luxurious

This is the one that best showcases your expensive Clear Wind guard.

It creates the feeling that energy has been **engineered around the precious sword** rather than sprayed over it.

##### Why it is third place

At 35 px, four meridians become aliasing.

So LOD must deliberately collapse:

- > 90 px: four rails + guard arcs;
- 55–90 px: two rails;
- <55 px: one coloured sheath/core silhouette.

That means this design really has two or three representations.

##### Cost estimate

**My estimate: ~+0.38–0.58 ms p95.**

Still potentially inside budget, but it has the least safety margin because it encourages more transparent geometry and more hero-level detail.

---

### Element material system I would use

This lets all three aura designs share the same shape architecture.

| Property | **Metal** | **Fire** | **Water** |
| --- | --- | --- | --- |
| Dark support | blue-black / graphite | charcoal / dark plum-brown | navy / blue-black |
| Main body | silver-cyan | amber-orange | aqua-jade |
| HDR core | cyan-biased silver | pale gold | pale aqua |
| Internal movement | straight longitudinal flow | upward/rearward licking | smooth travelling bands |
| Edge language | sharp / crystalline | broken / pointed | rounded / flowing |
| Shed particles | almost none | sparse ember | sparse droplets/mist only close |
| Turn behaviour | crisp snap | tail stretches | tail phase-lags |
| Strike | needle flash | sharp ember fan | crescent/splash line |
| Noise character | brushed/striated | cellular breakup | broad caustic flow |

**My inference:** this is much stronger than making Metal = blue particles, Fire = orange particles, Water = blue particles.

The element should change the **motion law and edge shape**, not merely RGB.

That is consistent with professional stylized VFX thinking: shape, motion, colour and timing form the identity; changing colour alone is comparatively weak. [80.lv +1](https://80.lv/articles/from-realism-to-stylization-game-vfx-production)

---

### One production rule I would make non-negotiable

##### The six full swords must periodically “prove” that the river contains Clear Wind.

For example, every 120–220 ms during the swarm:

- one or two hero swords pass through a readable orientation;
- their silver blade catches light;
- jade ring flashes non-HDR;
- tassel visibly trails;
- then they disappear back into the mass.

Meanwhile the 24/64 population carries quantity and speed.

**My inference:** this gives your viewer repeated subconscious confirmation:

> “Those streaks are swords.”

rather than:

> “The hero fired 94 blue lasers.”

It directly addresses the Qingxiao fan criticism about attacks becoming too VFX-like. [Reddit](https://www.reddit.com/r/Qingxiao/comments/1v69j6d/qingxiao_moveset_lest_goo/)

---

### Final ranking

| Rank | Direction | Clear Wind identity | 35 px read | Luxury | Element flexibility | Performance risk | Estimated aura cost* | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | **River-Silk Sheath** | **10/10** | 9/10 | **9.5/10** | **10/10** | Low–medium | **+0.28–0.45 ms** | **Build this first** |
| **2** | **Calligraphy Wake** | 8.5/10 | **10/10** | 8.5/10 | 9.5/10 | **Low** | **+0.20–0.34 ms** | Best swarm/far-camera option |
| **3** | **Jade Meridian Lattice** | **10/10** | 7.5/10 | **10/10** | 9/10 | Medium–high | **+0.38–0.58 ms** | Gorgeous close-up, harder LOD problem |

*These are **my engineering estimates**, not benchmark results from the cited games. They assume tight transparent bounds, instanced geometry, 64 single-pass impostors, no extra full-screen bloom pass and strike-only distortion.

If I were implementing it, I'd choose **River-Silk Sheath**, but take one idea from Calligraphy Wake: a very subtle dark tapered wake behind each sword. I would **not** merge all three designs; that would put you straight back into VFX clutter.

#### 5 sources I trust most

| Rank | Source | Why I trust/use it |
| --- | --- | --- |
| **1** | HoYoverse — Xiao Developer Insight [Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642) | First-party explanation of actual Chinese-fantasy character/VFX/animation art decisions: jade, clouds, light/dark, motion language. |
| **2** | Kuro Games — Qingxiao official material + current Sword Flight patch notes [YouTube +1](https://www.youtube.com/watch?v=op22gIZneCk&utm_source=chatgpt.com) | Closest current production reference to your exact sword-cultivator/flying-sword problem. |
| **3** | Riot Games — Visual Effects Art Education [Riot Games](https://www.riotgames.com/vi/artedu/visual-effects) | First-party production guidance on spectacle versus gameplay readability. |
| **4** | GDC — *Visual Effects Bootcamp: Artistic Principles of VFX* [GDC Vault](https://gdcvault.com/play/1023943/Visual-Effects-Bootcamp-Artistic-Principles) | Riot/Blizzard professional VFX fundamentals applicable across styles. |
| **5** | three.js InstancedMesh / BatchedMesh documentation [archive.threejs.org +1](https://archive.threejs.org/docs/api/en/objects/InstancedMesh.html) | Primary technical source for the batching strategy I'd actually use in your WebGL implementation. |

## E. Claude kiểm nguồn (03/11/2026)

Claude tự mở lại các nguồn chính bằng WebFetch hoặc tab riêng trong trình duyệt của ứng dụng. Reddit bị chặn với cả hai đường (WebFetch: "unable to fetch from www.reddit.com"; trình duyệt: "not allowed due to safety restrictions"), nên mọi câu trích fan từ Reddit chỉ là lời ChatGPT, Claude chưa đọc được.

| Khẳng định | URL | Kết quả |
|---|---|---|
| Qingxiao là Resonator 5 sao, hệ Aero, dùng kiếm, ra ở bản 3.6 của Wuthering Waves | https://wutheringwaves.kurogames.com/es/main/news/detail/5272 | **Đúng.** Thông báo bảo trì 3.6 (đăng 26.08.13) ghi "Resonadora de 5 estrellas: Qingxiao (Aero, Espada)". Ngày bảo trì 20/08 Claude chưa thấy trong đoạn đã đọc. |
| Bản 3.7 nhắc trạng thái "Sword Flight", Sword Step và "Ephemeral Transcendence" của Qingxiao | https://wutheringwaves.kurogames.com/en/main/news/detail/5571 | **Đúng.** Ghi chú bản 3.7 (26.09.30), phần sửa lỗi, nhắc cả ba tên. |
| Trang media chính thức nói Heart Sword tách kiếm ý thành "ten thousand flying blades" | https://wutheringwaves.notion.site/Resonator-Videos-Qingxiao-42aef7f91e4b83e0989a01533d33f9b2 | **Chưa kiểm được.** Trang Notion trả về rỗng khi WebFetch đọc. |
| Wuchen (Naraka) được đổi tuyệt kỹ thành Tai Chi Teleport: Blade Storm, "enduring sword rain", đội phát triển rất thích bộ kỹ năng này | https://www.narakathegame.com/news/update/20240719/33459_1168466.html | **Đúng.** Ghi chú cập nhật ngày 01–02/08/2024 có đúng các câu "features an enduring sword rain" và "has always been a favorite among our team". |
| Bài Rensei trên RealTimeVFX: hào quang kiếm là một lưới gắn vào kiếm, nhiễu cuộn và mặt nạ tròn; một lớp "glow" tối đặt sau chớp sáng cho nổi | https://realtimevfx.com/t/renseis-sketchbook/20495/24 | **Đúng.** Bài số 24, 07/11/2022. |
| Riot: nghệ sĩ VFX mang "heavy burden of restraint", cân giữa sướng mắt và rõ lối chơi | https://www.riotgames.com/vi/artedu/visual-effects | **Đúng.** Bài tiếng Anh, khung trang tiếng Việt. |
| Developer Insight về Xiao: ngọc bích cho cảm giác trường thọ và bí ẩn; dải vải có hoa văn mây cho vẻ cổ xưa; thân trên trắng xanh, thân dưới tối cho sức mạnh tà; sáng tối đan nhau trong đòn đánh; kỹ năng như mũi tên bay thẳng | https://genshin.hoyoverse.com/en/news/detail/8642 (chuyển sang `/103849`) | **Đúng.** Developer Insight #4, đăng 10/02/2021; Claude đọc trong tab riêng. WebFetch không đọc được vì trang dựng bằng JS. |
| Bài GDC 2021 về phong cách anime của Genshin | https://www.gdcvault.com/play/1027540 | **Đúng.** Haoyu "Hugh" Cai, miHoYo. Bài nói về phong cách và quy trình, không nói về VFX kiếm. |
| GDC 2017 "Visual Effects Bootcamp: Artistic Principles of VFX" | https://gdcvault.com/play/1023943/Visual-Effects-Bootcamp-Artistic-Principles | **Đúng.** Hadidjah Chamberlain (Blizzard) và Jason Keyser (Riot). |
| GDC 2024 Rocksteady "Attention Overload": dẫn sự chú ý mà không làm ngộp | https://gdcvault.com/play/1034360/Attention-Overload-Creating-Readable-VFX | **Đúng.** Hanno Hinkelbein; phần mô tả có câu "drive player attention in the right direction without overwhelming them". |
| 80.lv, Matt Schwartz: ba pha build-up, execution, dissipation | https://80.lv/articles/from-realism-to-stylization-game-vfx-production | **Đúng** (06/02/2018). |
| ChatGPT tự rút lại câu "hiệu ứng stylized lược bớt chi tiết nhỏ" vì cho là không có trong bài này | như trên | **ChatGPT rút sai.** Bài có câu "stylized effects use fewer small details" và nói tập trung vào hình, màu, khối. Câu ở bản đầu là đúng. |
| Jason Keyser, 80.lv: lưới và kết cấu vẽ tay, vật liệu động cho kết cấu "dance" | https://80.lv/articles/jason-keyser-on-in-game-vfx-and-the-demand-for-fx-artists | **Đúng** (25/11/2022). Ý "không cần mô phỏng" chỉ **đúng một phần**: ông đặt mô phỏng ở đầu kia của phổ, không nói thẳng như vậy. |
| Raid Moonlight Blade có cơ chế kiếm sét, kiếm lửa, kiếm gió (và kiếm băng) | https://news.17173.com/content/10282023/093214220.shtml | **Đúng một phần.** Đây là bản di động 天涯明月刀手游, phó bản 10 người Tâm Kiếm 2.0, boss 公子羽, mở 28/10/2023; bốn cơ chế 剑意惊雷, 剑意如火, 剑意乘风, 剑意凛寒. Bài tả cơ chế, không tả cách dựng hình. |
| Mercy (Overwatch): hạt khói dùng flow map, tia gốc là hai ribbon đổi hướng nhẹ | https://realtimevfx.com/t/overwatch-vfx-mercy-healing-beam/699 | **Đúng.** Người trả lời là Rachel_Day, được gọi là "the original source"; chức danh không ghi trên trang này. |
| 80.lv, gói Baltic VFX: tụ quang (caustics) bằng kết cấu và một flowmap vẽ tay, không mô phỏng chất lỏng | https://80.lv/articles/creating-vfx-for-baltic-vfx-content-pack | **Đúng.** Perik Blivet, 19/10/2021. |
| Epic DepthFade che đường nối nơi vật trong suốt cắt vật đục | https://dev.epicgames.com/documentation/unreal-engine/depth-material-expressions-in-unreal-engine | **Đúng.** |
| GPU Gems 3 ch. 23: hạt phủ màn hình gây overdraw gần như không giới hạn; vẽ hạt ở bộ đệm nhỏ hơn | https://developer.nvidia.com/gpugems/gpugems3/part-iv-image-effects/chapter-23-high-speed-screen-particles | **Đúng.** "overdraw can be almost unbounded". |
| three.js BatchedMesh giảm draw call, có sắp xếp từng vật | https://threejs.org/docs/pages/BatchedMesh.html | **Đúng.** `sortObjects` mặc định bật; vật trong suốt vẽ từ xa tới gần. |
| Bài SDF của Valve (SIGGRAPH 2007) giữ mép sắc khi phóng to, có viền và bóng | https://steamcdn-a.akamaihd.net/apps/valve/2007/SIGGRAPH2007_AlphaTestedMagnification.pdf | **Chưa đọc được.** Máy chủ trên link lỗi chứng chỉ; bản trên `cdn.akamai.steamstatic.com` tải về nhưng máy này không có công cụ đọc chữ PDF. Đây là bài nổi tiếng của Chris Green; nội dung khớp hiểu biết chung, nhưng Claude chưa đọc lại. |
| Câu trích fan Reddit: Qingxiao ("less VFX Y more phyiscal", "very transparent and overdone, so they all meld together"), Yanqing ("rides on flying swords"), nhịp mưa kiếm của Wuchen, bài review Sword of Coming ("especially lacklustre"), RMJI, Swords of Legends, Jade Dynasty, Sword and Fairy 7 | các link `reddit.com` trong mục C | **Chưa kiểm được** (Reddit bị chặn). Là ý kiến fan, không phải số liệu. Dùng làm gợi ý, không dùng làm bằng chứng chính. |
| Bài ArtStation của Robbert Mouthaan; bài phỏng vấn Black Myth của Epic | https://robbertmouthaan.artstation.com/projects/L49NVk, https://www.unrealengine.com/developer-interviews/black-myth-wukong-wows-with-ue5-early-access-visuals | **Chưa kiểm được** (403). |
| Các mức sáng, bề rộng điểm ảnh, số draw call và mức +0,24–0,54 ms | — | **Là ước lượng của ChatGPT**, chính nó ghi rõ. Chưa đo trên máy mình. |

**Tóm lại:** Claude mở được 17 nguồn chính thức và kỹ thuật. 16 nguồn đúng như ChatGPT tả; nguồn 17173 chỉ đúng một phần (là bản di động). Một ý phụ về Keyser cũng chỉ đúng một phần. Một lần tự sửa của ChatGPT là sai: câu về 80.lv lẽ ra phải giữ. Phần "fan yêu nhất" dựa gần hết vào Reddit, nên vẫn chưa ai kiểm.

## F. Đánh giá của Claude

**Đồng ý:**
- **Giữ kiếm là kiếm.** Bài học chính trùng với luật của anh: thanh Clear Wind thật phải đọc ra được; hào quang chỉ mặc thêm cho kiếm. Ý "6 kiếm đầy đủ thỉnh thoảng phải chứng minh cả dòng là Clear Wind" (ngọc lóe, tua đuôi trễ) đáng ghi vào brief.
- **Mỗi tầng một cách vẽ.** 6 kiếm có vỏ lưới, viền ngọc, tua; 24 kiếm LOD có vỏ instanced và vây quét; 64 impostor chỉ một quad SDF. Phần đẹp tốn tiền đặt ở cấp cả dòng (4–8 ribbon, một dòng sáng trên đất), không đặt trên từng kiếm. Cách này hợp trần 32 ribbon và 3 lớp trong suốt.
- **Lớp tối, thân, lõi HDR nằm chung một shader**, thành một mặt trong suốt cho mỗi kiếm ở mỗi điểm ảnh. Đây là điểm kỹ thuật quan trọng nhất. Nó giữ luật "tối sau sáng" mà không nhân đôi overdraw.
- **Theo pha:**
  - độ cong của đường bay quyết định độ giàu, không phải tốc độ;
  - lúc chém thì vỏ co lại, lõi vọt lên, rồi mới loang ra;
  - lúc phóng thì sáng ngay khung 0 (khớp luật ≤ 50 ms);
  - lúc về không phát ngược lúc phóng.
- **Đo bằng `EXT_disjoint_timer_query_webgl2`** với chín cảnh thử, kể cả cảnh dòng kiếm hội tụ dày và cảnh nền sáng.

**Chỗ Claude không đồng ý hoặc thấy thiếu:**
- **Lửa vẫn có nguy cơ thành sắt nung.** Lỗi anh vừa chê là vỏ Fire đọc như sắt nung, không như lửa liếm. Hướng A tả Fire là "lụa hổ phách, mép sau bị bào nhọn, cứng gần lưỡi". Ở 35–130 px, như vậy dễ lặp lại đúng lỗi đó.
  - Lửa cần lưỡi lửa thoát ra khỏi đường viền: ít nhất 2–3 px ở 35 px, chạy ngược chiều bay, và nhấp nháy.
  - Clip lửa có sẵn (heat-field, 12 flipbook lửa của Dragonhold) nên được thử ngay trên vây và vỏ.
- **Hướng B (Calligraphy Wake) tối và hợp nhất.** Nét mực đen sau kiếm rất rõ ở xa. Nhưng:
  - trên nền đá tối nó có thể thành vệt bẩn;
  - nó dễ che chữ gõ và thú;
  - nó đi ngược khẩu vị "rực sáng, có hào quang" của anh.
  - Muốn dùng thì nét mực phải ngắn và chỉ là viền, không thành mảng.
- **Hướng C (Jade Meridian Lattice) đẹp nhất ở cận cảnh, nhưng camera mình hầu như không có cận cảnh.** Phần lớn thời gian kiếm chỉ 35–130 px, nên các "đường kinh mạch" gộp lại còn một viền. Nó hợp làm bản riêng cho 6 kiếm chính hơn là một hướng độc lập.
- **Chi phí là ước lượng.** Phím 7 đang ở p95 10,2–10,5 ms, trần 11,5 ms. Lớp Fire đã thêm tới +0,23 ms ở phím 7 (changelog 03/11).
  - Hào quang +0,6 ms cộng với chất Fire có thể chạm trần.
  - Cần chốt: +0,6 ms là cho riêng hào quang hay đã gồm chất của hệ.
- **Thiếu những thứ riêng của game mình:**
  - hào quang lớn dần theo chuỗi gõ (mức gõ đã điều khiển pha tụ ở Fire);
  - một vòng hay quầng nhỏ sau 6 kiếm chính lúc phóng, theo bộ radiance của anh (halo, motes, ribbon);
  - phép thử chữ gõ không bị khó đọc (tỉ lệ điểm ảnh gần trắng);
  - phép thử màu cam sau tone mapping.
- **Thiếu nguồn tiếng Trung.** Cả hai lượt đều chỉ tìm nguồn tiếng Anh. Các bài phân tích của họa sĩ VFX NetEase hay Tencent trên Bilibili, Zhihu, GameRes chưa được tìm.

So sánh với Gemini, những gì cả hai cùng thiếu và gợi ý ba hướng để làm mẫu cho anh: [`sword-aura-gemini-2026-11-03.md`](sword-aura-gemini-2026-11-03.md), mục D.
