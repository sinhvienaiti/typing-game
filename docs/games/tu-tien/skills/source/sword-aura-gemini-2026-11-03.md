# Sword aura research, Gemini (4 Argon, thinking Cao), 03/11/2026

- **Công cụ:** Gemini (gemini.google.com), model 4 Argon, mức suy nghĩ "Cao"; cùng tab riêng của Claude, sau lượt ChatGPT. Đây là ý kiến thứ hai.
- **Ngày:** 03/11/2026, khoảng 14:35–14:45.
- **Chat:** https://gemini.google.com/app/37142c92c0d9fbff
- **Đây là văn bản nghiên cứu chưa tin cậy.** Bảng kiểm nguồn của Claude ở phần C, đánh giá ở phần D. Bản ChatGPT cùng đề bài: [`sword-aura-chatgpt-2026-11-03.md`](sword-aura-chatgpt-2026-11-03.md).
- **Nguyên văn, không phải bản tóm tắt.**
  - Claude chuyển DOM câu trả lời sang Markdown ngay trong trang.
  - Trang Gemini chặn mọi đường gửi về máy cục bộ: CSP `form-action` chặn form, `fetch` tới 127.0.0.1 thất bại. Vì vậy Claude chép bản Markdown đó ra thành bốn đoạn.
  - Claude so SHA-256 của từng đoạn với chính chuỗi trong trang: cả bốn đoạn và toàn bài (46.118 byte) đều khớp.
- **Phần bị bỏ:**
  - dòng tóm tắt suy nghĩ ("Analyzing visual preferences for sword auras");
  - các chip nguồn dạng băng chuyền.
  - Link trong bài là link Gemini tự gắn vào tên nguồn.

## A. Tin nhắn đã gửi (nguyên văn, một chat mới)

```text
Please use Google Search and give a URL behind each factual claim (official pages, patch notes, developer talks, GDC or 80.lv or ArtStation breakdowns, fan threads and reviews; many sources, not one listicle). Say clearly when something is your own opinion.

I am designing the flying-sword look for a xianxia typing-defense game (three.js, browser, far top-down 3/4 camera at about 55 degrees). Our hero sword is a real 3D model we keep as-is, Clear Wind: slim silver jian blade, white jade ring at the guard, cloud-shaped guard, tassel. A skill flies a river of about 6 full swords + 24 LOD swords + 64 impostor sprites. Today they fly as bare metal props (thin white-hot edge line, soft rim, hit flash, short trail) and look crude. We need an aura that DRESSES the real sword (blade, jade ring, cloud guard and tassel stay readable; the aura never hides or replaces the sword). The aura is a shape layer; its material comes from an element kit (Metal = silver-white/cyan qi; Fire; Water; later Wood, Earth, Thunder). Rules: only thin HDR cores bloom; halos and rings at most 0.9 per channel; a dark layer behind every bright layer; core at most 30% white; never the enemy warning red #FF4A4A; the whole river's aura must cost about +0.6 ms p95 at 1080p in WebGL; engine caps on High: about 32 live ribbons, about 32 extra VFX draw calls, average 3 overlapping transparent layers per pixel.

1) Which flying-sword / sword-qi / yu jian (御剑) and sword-aura looks do players and viewers love most, and why? Consider games (Genshin Impact, Honkai: Star Rail Yanqing and Jing Yuan, Wuthering Waves, Naraka: Bladepoint, Black Myth: Wukong, Tower of Fantasy, Moonlight Blade, Justice Online, Swords of Legends, Where Winds Meet, Onmyoji) and donghua (A Record of a Mortal's Journey to Immortality, Battle Through the Heavens, Soul Land, Jade Dynasty / Zhu Xian, Sword of Coming / Jian Lai, The Daily Life of the Immortal King), and the Myriad-Swords / sword-rain ultimates. Cite fan reaction or reviews where you can.

2) The layers that make a flying sword read premium (blade-hugging qi sheath, edge light, afterimages, ribbon or tassel streamers, motes, runes, tip star, distortion, ground light, colour grading per element), how the look changes at launch, cruise, turn, strike and return, and which layers survive when the sword is only 35-130 px long on a 1080p screen.

3) How games keep many swords cheap (instancing, impostors, shell or fin meshes, ribbon trails, flowmaps), with sources where known.

4) THREE original directions for Clear Wind, each with an English name, a layer list (role, rough brightness, phase, survives at 35 px or not), how Metal, Fire and Water swap its material, what makes it captivating, luxurious and modern, and a rough cost for about 94 swords. No copying of any game's design.

End with a ranked table of the three directions.
```

Gemini không có lượt tự rà soát như ChatGPT; việc kiểm nguồn nằm ở phần C.

## B. Câu trả lời của Gemini (nguyên văn)

### 1. Player-Favorite Flying-Sword (*Yu Jian* / 御剑) & Sword-Qi Looks Across Games and Donghua

#### A. Action RPGs, Gacha & Wuxia/Xianxia Games

- **Genshin Impact (Xingqiu, Chongyun, Alhaitham):**
   - **Factual Mechanics & Visuals:** Xingqiu’s *Guhua Sword: Fatal Rainscreen* and *Raincutter* summon 3 to 4 orbital *Rain Swords* around the active character and fire consecutive homing hydro sword-rain volleys ([HoYoWiki: Xingqiu](https://wiki.hoyolab.com/pc/genshin/entry/39/); [Genshin Impact Wiki: Raincutter](https://genshin-impact.fandom.com/wiki/Guhua_Sword:_Raincutter)). Players and theorycrafters praise Xingqiu’s Rain Swords for their unmistakable state readability—orbiting translucent turquoise blades framed by dark-blue water silhouettes and crisp white tip glints that clearly telegraph damage reduction and off-field hydro application ([Reddit r/GenshinImpactTips KQM Guide](https://www.reddit.com/r/GenshinImpactTips/comments/173vn0q/kqm_xingqiu_extended_guide/)). Chongyun’s *Spirit Blade: Chonghua’s Layered Frost* drops giant talisman-ringed cryo greatswords into the ground ([Heroes Wiki: Chongyun](https://hero.fandom.com/wiki/Chongyun); [Genshin Impact Wiki: Chongyun Profile](https://genshin-impact.fandom.com/wiki/Chongyun/Profile)), while Alhaitham’s *Chisel-Light Mirrors* float beside him as sharp emerald crystal-blade shards that project geometric sword-rain cages during *Particular Binding Field* ([Genshin Impact Wiki: Debate](https://genshin-impact.fandom.com/wiki/Debate); [Fextralife: Alhaitham 3.4 Overview](https://fextralife.com/genshin-impact-alhaithams-5-star-weapon-is-coming-in-version-3-4/)).
   - **My Opinion / Design Analysis:** *Genshin* succeeds because it pairs every glowing elemental blade with a dark ink-like outline or deep-value backing shell, preventing the blades from washing out against bright daytime terrain. However, because Xingqiu’s and Alhaitham’s constructs are pure energy projections rather than dressed physical weapons, copying them directly would hide *Clear Wind*’s silver blade and jade ring.
- **Honkai: Star Rail (Yanqing & Jing Yuan):**
   - **Factual Mechanics & Visuals:** Cloud Knight Lieutenant Yanqing is an ice-element prodigy who commands a formation of floating swords via *Soulsteel Sync*, riding a giant ice-forged sword through the clouds in his Ultimate (*Amidst the Raining Bliss* / *Cascading Laceration*) while swallow and cloud motifs trail behind ([Honkai: Star Rail Wiki: Yanqing Story](https://honkai-star-rail.fandom.com/wiki/Yanqing/Story); [Heroes Wiki: Yanqing](https://hero.fandom.com/wiki/Yanqing)). Community discussions frequently highlight the contrast between Yanqing’s agile, swallow-like flying sword arrays and General Jing Yuan’s *Lightning-Lord* (*Lightbringer* / *Command Talisman*), which manifests a titanic golden-lightning spirit glaive that sweeps the battlefield after accumulating talisman stacks ([Reddit r/HonkaiStarRail Yanqing Analysis](https://www.reddit.com/r/HonkaiStarRail/comments/1bk4902/an_exploration_into_yanqings_character_explained/); [HoYoWiki: Jing Yuan](https://wiki.hoyolab.com/pc/hsr/entry/26?lang=en-us); [VS Battles Wiki: Jing Yuan](https://vsbattles.fandom.com/wiki/Jing_Yuan)).
   - **My Opinion / Design Analysis:** Yanqing’s sword formation is the gold standard for **preserving real weapon hardware inside an aura**: each flying sword retains its metallic guard, fuller, and pommel tassel, while the ice-cyan *jianqi* hugs the bevel as a translucent sheath and trails a swallow-tail ribbon.
- **Wuthering Waves (Jinhsi, Changli, Jiyan):**
   - **Factual Mechanics & Visuals:** *Wuthering Waves* leans into high-contrast frequency/waveform VFX: Jiyan conjures a teal wind *Qingloong* around his broadblade ([Wuthering Waves Wiki: Jiyan](https://wutheringwaves.fandom.com/wiki/Jiyan/Backstory)), Jinhsi channels Spectro light and the Sentinel *Jué* with black-and-white/gold dragon motifs and floating sword-like frequency scales ([Wuthering Waves Wiki: Jinhsi](https://wuthering-waves.fandom.com/th/wiki/Jinhsi); [Reddit r/WutheringWaves Story & Visuals Thread](https://www.reddit.com/r/WutheringWaves/comments/1jpe6z9/what_made_22_so_powerful_is_exactly_what_makes_me/)), and Changli dresses her metallic sword in layered vermilion phoenix-feather flames that fans praised for delivering a true high-contrast flame sword without turning the blade into a cartoon club ([Reddit r/WutheringWavesLeaks Changli Discussion](https://www.reddit.com/r/WutheringWavesLeaks/comments/1d8km2i/changli_weapon_type/); [Reddit Signature Weapons Thread](https://www.reddit.com/r/WutheringWavesLeaks/comments/1d8q7nn/jinhsi_and_changli_signature_weapons_via_gura/)).Players also actively discuss the dedicated *Sword Flight* stamina mechanics introduced in later patches ([Reddit r/wherewindsmeet_ Cross-Reference on WuWa 3.5 Sword Flight](https://www.reddit.com/r/wherewindsmeet_/comments/1oz9lq0/flying_swords_in_wwm/)).
   - **My Opinion / Design Analysis:** Kuro Games’ signature look comes from **chromatic ink-wash darks (sumi-e black/charcoal edges)** combined with razor-thin HDR metallic specular lines. Even when Jinhsi’s or Changli’s effects peak, the dark frequency wave behind the bright core prevents screen-whiteout.
- **Naraka: Bladepoint:**
   - **Factual Mechanics & Visuals:** In *Naraka: Bladepoint*, the Longsword is famous for launching ranged horizontal and vertical *Sword Energy* waves on charged Blue Focus strikes, alongside Flying Knives (*Pierce the Sun* multi-blade volleys) and hero skills from Yoto Hime, Kurumi, and Takeda ([Naraka: Bladepoint Official Weapon Guide](https://www.narakathegame.com/guide/weapon/); [Naraka: Bladepoint Wiki](https://narakabladepoint.fandom.com/wiki/Naraka:_Bladepoint_Wiki)).
   - **My Opinion / Design Analysis:** Because *Naraka* is a competitive PvP melee game where Blue Focus vs. Red Parry states dictate survival, its sword qi never floods the screen with soft bloom; instead, it uses a **sharp crescent leading edge backed by a smoky dark wake**, keeping combat states instantly readable.
- **Black Myth: Wukong (Erlang Shen):**
   - **Factual Mechanics & Visuals:** In the secret Mount Mei boss encounter against Erlang, the Sacred Divinity (*Erlang Shen*), he fights with a three-pointed double-edged spear, a giant axe, and a telekinetically commanded **River of Swords**—floating in mid-air to rain dozens of glowing celestial blades before executing a lethal red-lightning finisher ([Black Myth: Wukong Wiki: Erlang Shen](https://blackmythwukong.fandom.com/wiki/Erlang_Shen); [Reddit r/BlackMythWukong Erlang Shen Guide](https://www.reddit.com/r/BlackMythWukong/comments/1szcpi4/erlang_shen/); [Reddit r/BlackMythWukong "ERLANG THE G.O.A.T."](https://www.reddit.com/r/BlackMythWukong/comments/1wf0h0l/erlang_the_goat/)). Players consistently rank Erlang’s River of Swords and phase transitions among the most cinematic spectacles in the game ([Reddit r/BlackMythWukong Boss Discussion](https://www.reddit.com/r/BlackMythWukong/comments/1fcjscp/at_what_point_are_you_supposed_to_fight_erlang/); [Reddit Lore & Fight Appreciation](https://www.reddit.com/r/BlackMythWukong/comments/1h6j6wg/i_realized_the_true_meaning_of_the_erlang_shen/)).
   - **My Opinion / Design Analysis:** Erlang’s sword river feels terrifying because each sword is **physically grounded first** (cold steel reflection + dark atmospheric dust) and **divine second** (a tight golden-white star at the guard/tip and a thin wake), avoiding the "neon laser" look.
- **Tower of Fantasy (Saki Fuwa, Alyss, Lin):**
   - **Factual Mechanics & Visuals:** Saki Fuwa’s dual-katana weapon *Heartstream* (and *Super Flow* Matrix set) uses floating frost-blade phantoms (*Surge* / *Flowing Springs*) that fire synchronized phantom cuts ([Tower of Fantasy Wiki: Saki Fuwa](https://toweroffantasy.fandom.com/wiki/Saki_Fuwa); [Tower of Fantasy Wiki: Saki Fuwa Matrix Set](https://toweroffantasy.fandom.com/wiki/Saki_Fuwa_(Matrix_Set))), while Lin’s *Shadoweave* teleports between floating epiphyllum-flower blades ([Reddit r/TowerofFantasy Lin & Animation Discussions](https://www.reddit.com/r/TowerofFantasy/comments/wufk2e/tower_of_fantasy_resource_wiki_site_launch/); [Reddit 2.0 Animation Thread](https://www.reddit.com/r/TowerofFantasy/comments/wmm4f5/for_people_complaining_about_the_animation_this/)).
   - **My Opinion / Design Analysis:** While *Tower of Fantasy*’s geometric blade formations are snappy, later weapons suffered from excessive additive overdraw where overlapping cyan/magenta halos turned multiplayer boss fights into unreadable white blobs—a cautionary tale that validates your strict `0.9` halo cap and `3.0` overdraw limit.
- **Classic & Modern Wuxia/Xianxia MMOs (Moonlight Blade, Justice Online / Sword of Justice, Swords of Legends Online, Where Winds Meet) & Onmyoji:**
   - **Factual Mechanics & Visuals:**
      - *Moonlight Blade* contrasts *Taibai* (ultra-fast snow-mountain one-handed sword bursts with crisp silver-white air-slits) against *Zhenwu* (Wudang-inspired twin-sword *Yin/Yang* shadow-clone projections that mirror the player’s sword forms) and *Tangmen* puppetry ([Moonlight Blade Wiki: Classes](https://moonlight-blade.fandom.com/wiki/Classes)).
      - *Swords of Legends Online* (*Gujian Qitan*) features the archetypal *Spellsword* (御剑 / *Yu Jian*), which splits into ranged flying-sword formations (*Sword Artist*) and close-quarters phantom sword storms (*Bladestorm*) ([Swords of Legends Online Wiki: Spellsword](https://swords-of-legend-online.fandom.com/wiki/Spellsword)).
      - *Justice Online* / *Sword of Justice* (*Nishuihan*) builds its *Shenxiang* and *Longyin* sword-qi visuals around the Five Elements cycle (*Jin, Mu, Shui, Huo, Tu*), earning praise from MMO players for its fluid martial animations and elemental inner-power synergies ([Reddit r/MMORPG Sword of Justice Review](https://www.reddit.com/r/MMORPG/comments/1ox7jkf/pleasantly_surprised_by_sword_of_justice_long/); [Sword of Justice Inner Power & Five Elements Guide](https://www.youtube.com/watch?v=4JtPpLjp1qc)).
      - *Where Winds Meet* emphasizes grounded *Strategic Sword* and *Nameless Sword* *jianqi* waves alongside the *World of Sword* mystic skill, though players on Reddit actively campaign for even more xianxia-style *yu jian* sword-flight ([Reddit r/wherewindsmeet_ Flying Swords Thread](https://www.reddit.com/r/wherewindsmeet_/comments/1oz9lq0/flying_swords_in_wwm/); [Reddit r/WhereWindsMeet Best Sword Weapon Thread](https://www.reddit.com/r/WhereWindsMeet/comments/1s87hcy/best_sword_weapon_and_new_weapons_release/)).
      - *Onmyoji*’s Susanoo commands the *6 Divine Swords: Ama no Habakiri*, which hover behind his back like a golden-thunder halo and launch individually as sky-piercing lightning spears that leave *Thunder Tombs* ([Onmyoji Wiki: Susanoo](https://onmyoji.fandom.com/wiki/Susanoo)).
   - **My Opinion / Design Analysis:** Across all five titles, players consistently prefer **structured formations** (lotus rings, dorsal fans, river streams) where each sword’s hilt, guard ring, and tassel remain crisp, rather than chaotic particle swarms.

#### B. Donghua Benchmarks & *Myriad-Swords* (万剑归宗) Ultimates

- **A Record of a Mortal's Journey to Immortality (*Fanren Xiuxian Zhuan* / 凡人修仙传):**
   - **Factual Lore & Visuals:** Han Li’s life-bound magic treasure is his set of 36 to 72 *Azure Bamboo Cloudswarm Swords* (青竹蜂云剑), which are carved like emerald-jade bamboo and infused with golden Divine Devilbane Lightning ([WebNovel Q&A: Azure Bamboo Cloudswarm Swords](https://www.webnovel.com/ask/q335986158218265); [Wikipedia: A Record of a Mortal's Journey to Immortality](https://en.wikipedia.org/wiki/A_Record_of_Mortal%27s_Journey_to_Immortality)). Fans on r/Donghua rave about how the donghua animates the *Great Geng Sword Array*—showing individual emerald blades humming with fine golden-arc threads that merge into a disciplined river or giant sword formation, pushing the series past 7 billion views ([Reddit r/Donghua Han Li Sword Array Discussion](https://www.reddit.com/r/Donghua/comments/1gq661l/a_mortals_journey_to_immortality_question/)).
- **Sword of Coming (*Jian Lai* / 剑来):**
   - **Factual Lore & Visuals:** *Sword of Coming* has been hailed by donghua viewers for its breathtaking sword fights—such as Ning Yao vs. Qi Jingchun and the episode 26 sword awakening—which blend poetic calligraphy, ink-wash atmospheric depth, and razor-sharp golden/cyan *jianqi* ([Reddit r/Donghua Sword of Coming Review](https://www.reddit.com/r/Donghua/comments/1nea5pb/sword_of_coming_review/); [Reddit r/Donghua Worth the Watch Thread](https://www.reddit.com/r/Donghua/comments/1pph898/is_sword_of_coming_worth_the_watch/)).
- **Jade Dynasty (*Zhu Xian* / 诛仙):**
   - **Factual Lore & Visuals:** Lu Xueqi wields the spiritual sword *Tianya* (天琊剑), famous for its clear azure-blue blade glow and the *Mighty Sword of Thunder* (*Nine Heavens Profound Lightning*) technique ([Zhu Xian Wiki: Lu Xueqi](https://zhu-xian.fandom.com/wiki/Lu_Xueqi); [Wikipedia: Zhu Xian](https://en.wikipedia.org/wiki/Zhu_Xian_(novel)); [Reddit r/Donghua Jade Dynasty vs Sword of Coming](https://www.reddit.com/r/Donghua/comments/1i1ow3p/jade_dynasty_or_sword_of_coming/)).
- **Soul Land (*Douluo Dalu*) & Battle Through the Heavens (*Doupo Cangqiong*):**
   - **Factual Lore & Visuals:** In *Soul Land*, Sword Douluo Chen Xin’s *Seven Kill Sword* (七杀剑) is described as a clear crystal-blue longsword inlaid with nine stars; its 7th and 9th Spirit Ring ultimates (*Edge Hidden in Thousands of Swords*) split into sword-streams that carve the black spatial character *Kill* (杀) in mid-air ([STARD Wiki: Chen Xin](https://stard.fandom.com/wiki/Chen_Xin); [Soul Land Wiki: Chen Xin Discussion](https://soulland.fandom.com/f/t/Chen%20Xin); [Reddit r/Donghua Sword Dao Chen Xin Movie](https://www.reddit.com/r/Donghua/comments/1kwc2v5/movie_soul_land_sword_dao_chen_xin_%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%E4%B9%8B%E5%89%91%E9%81%93%E5%B0%98%E5%BF%83/)). In *Battle Through the Heavens*, Yun Yun’s *Wind’s Extreme: Falling Day* and Misty Cloud Sect sword arrays weave cyan wind ribbons tightly around ornate silver-and-jade blades ([Battle Through the Heavens Wiki: Yun Yun](https://battle-through-the-heavens.fandom.com/wiki/Yun_Yun); [Reddit r/Donghua Yun Yun Character Design Appreciation](https://www.reddit.com/r/Donghua/comments/1jq7vaz/btth_yun_yun_x_xiao_yan/)).
- **The Daily Life of the Immortal King (*Xian Wang de Richang Shenghuo*):**
   - **Factual Lore & Visuals:** Wang Ling’s sentient wooden spirit-sword *Jingke* (惊柯) is beloved for looking like an unassuming, unadorned wooden prop until it unleashes relativistic, space-warping sword-qi streams ([The Daily Life of the Immortal King Wiki: Jingke](https://the-daily-life-of-the-immortal-king.fandom.com/wiki/Jingke); [VS Battles Wiki: Jingke](https://vsbattles.fandom.com/wiki/Jingke_(Donghua))).
- **My Opinion — Why Players Love These & What Fails:**
   1. **The "Dressed Relic" Principle:** Viewers hate when a named treasure sword turns into an anonymous glowing popsicle stick. In *RMJI* (Han Li’s bamboo-jointed blades) and *HSR* (Yanqing’s Cloud Knight swords), the aura acts like **tailored silk and cold mist around sharp metal**.
   2. **Hydrodynamic Flock Cohesion:** In *Myriad-Swords* (*Wan Jian Gui Zong*) rivers, players love seeing **tiered hierarchy**—a few "leader" swords with full guard/ring/tassel detail flanked by schooling follower blades that bank in unison like silver-scaled fish cutting through dark water.

### 2. Anatomy of a Premium Flying Sword: Layers, Phase Transitions & 35–130 px Survival

In professional top-down VFX design—codified in Riot Games' *League of Legends VFX Style Guide* and GDC VFX Bootcamps—every readable effect separates **Primary Elements** (sharp silhouette, localized illuminationspike at the focal point) from **Secondary Elements** (lower-value, lower-opacity thematic flavor), and avoids 100% pure white washout by anchoring bright cores against dark value contrast ([VFX Apprentice: 10 League of Legends VFX Design Tips](https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips); [ResearchGate: Artistic Principles of Visual Effects in Video Games](https://www.researchgate.net/publication/407219916_Artistic_Principles_of_Visual_Effects_in_Video_Games)).

#### A. The 10 Premium Layers (Opinion & Technical Specification for *Clear Wind*)

To keep *Clear Wind*’s slim silver jian blade, white jade ring, cloud-shaped guard, and tassel 100% readable while respecting your engine rules (**only thin HDR cores bloom; halos/rings ≤ 0.9 per channel; dark layer behind every bright layer; core ≤ 30% white; never `#FF4A4A`**), here is how each layer must be built:

1. **Dark Backing / Ink Cushion (Mandatory Underlay):**
   - **Role:** A slightly expanded inverted-hull or camera-facing fin silhouette behind the sword and behind the trail core (RGB `0.03–0.12`, alpha `0.55–0.75`, premultiplied alpha blend). It creates an immediate dark "trench" around the silver blade and white jade ring so that even over bright stone or snow passes, *Clear Wind* pops with razor contrast.
2. **Blade-Hugging Qi Sheath (Translucent Shell / Cross-Fin):**
   - **Role:** A tight, form-fitting shell mesh offset `1.5–3.0 cm` from the blade bevel, tapering to a needle point `15%` past the physical tip, with a **cutout window around the cloud guard and white jade ring** so the aura flows *around* the ring rather than burying it. Capped at ≤ `0.85` per channel so it never blooms.
3. **Edge Light (Thin HDR Ridge & Bevel Core):**
   - **Role:** The **only** blooming geometry on the sword body (`1.4–2.2` HDR luminance, ≤ `30%` white saturation mix, `1–2 px` wide in screen space). Placed strictly along the diamond central ridge (*ji*) and the leading cutting bevels of the silver blade, plus a micro-rim on the inner aperture of the white jade ring.
4. **Tip Star & Guard Aperture Glint:**
   - **Role:** An anisotropic 4-point diamond glint (stretched 3:1 along the flight vector) pinned to the sword tip, and a tiny circular halo (`≤ 0.9` per channel) framing the white jade ring at the guard. In top-down 3/4 view, this creates a two-point "constellation" (Tip + Jade Ring) that immediately tells the eye which way the sword is pointing.
5. **Runes / Talismans (Jade-Ring Collar Sigils):**
   - **Role:** Tiny Daoist cloud-seal scripts orbiting or stamped along the flat plane of the white jade ring or trailing immediately behind the cloud guard. Kept at `0.75–0.90` brightness over a dark `0.08` backing stroke.
6. **Ribbon & Tassel Streamers:**
   - **Role:** Extends the physical pommel tassel into a flowing qi streamer, paired with two hair-thin winglet threads peeling off the cloud-guard tips ([RealTimeVFX Sketch #14 Sword Trail](https://realtimevfx.com/t/ofiicial-vfx-sketch-14-sword-trail/5060)). As veteran VFX artists note on RealTimeVFX, a great trail is bolder/brighter at the leading striking edge and tapers with textured erosion along the wake ([RealTimeVFX Sketch #14](https://realtimevfx.com/t/ofiicial-vfx-sketch-14-sword-trail/5060); [Create Sword Trail Slash UE5 Breakdown](https://www.youtube.com/watch?v=ixvBQWsZreo)).
7. **Afterimages (Stepped Motion Echoes):**
   - **Role:** During high-acceleration turns and strikes, 2 to 3 discrete, non-blooming (`0.55–0.75` channel max) silhouette echoes of *Clear Wind* spawn at fixed time intervals (`40 ms` apart) and dissolve via noise erosion. Discrete stepped echoes feel much more "high-cultivation martial arts" than a smeared motion blur.
8. **Motes (Sparse Elemental Flecks):**
   - **Role:** Very sparse, crisp geometric flecks (bamboo-leaf diamonds, embers, or dew beads depending on element) shed from the cloud guard during turns. Drawn as instanced GPU quads with dark rims, never soft fuzzy smoke.
9. **Distortion (Refractive Air-Cut Wake):**
   - **Role:** In a 55° top-down WebGL game, full screen-space grab-pass refraction on 94 swords is too expensive and muddies the sword model. Instead, use **UV-offset normal distortion inside the qi-sheath shader itself** (or a single screen-space shock-slit only on the 6 hero swords during Strike impact) ([RealTimeVFX UE4/DMC5 Sword Trail Refraction Thread](https://realtimevfx.com/t/ue4-sword-trail-material-shader-help/17009)).
10. **Ground Light (Projected Pass-Floor Faux-Light):**
   - **Role:** Instead of real dynamic point lights, project **3 to 5 instanced additive/modulated ground decals** underneath the river’s center of mass (`≤ 0.45` brightness). Moving ground light anchors the flying river in 3D space above the pass floor.
11. **Element Colour Grading (Gradient Map / 1D LUT Ramp):**
   - **Role:** The aura geometry outputs a normalized `[0..1]` energy density value (`vEnergy`). A tiny `32×1` per-element LUT texture maps `[0.0–0.35]` to the **Dark Backing**, `[0.35–0.80]` to the **Saturated Element Body (≤ 0.9)**, and `[0.80–1.0]` to the **HDR Core (≤ 30% white)** ([Create Sword Trail Slash Gradient Mapping](https://www.youtube.com/watch?v=ixvBQWsZreo)). All fire/thunder reds are shifted to **Solar Gold (`#FFB830`), Cinnabar Amber (`#FF6E1A`), or Imperial Plum-Crimson (`#B81D58`)**, strictly avoiding enemy warning red `#FF4A4A`.

#### B. Phase State Machine: Launch → Cruise → Turn → Strike → Return (My Design Opinion)

- **1. Launch (Sword Call / *Qi Jian* — 0 to 150 ms):**
   - **Visual Shift:** The white jade ring at the guard flares first (`0.9` ring halo + brief `1.8` HDR inner-aperture spark) accompanied by a single Daoist rune collar stamp. The qi sheath unzips from guard to tip over `80 ms` (UV wipe), and the pommel tassel snaps taut.
- **2. Cruise (River Flight / *Yu Jian*):**
   - **Visual Shift:** Streamlined laminar flow. The dark backing shell hugs close (`1.2×` blade width). The HDR ridge line is steady (`1.5` luminance). The cloud guard trails two thin, calm laminar threads while the tassel streamer undulates with a low-amplitude sine wave.
- **3. Turn (Bank & Carve):**
   - **Visual Shift:** The sword rolls on its longitudinal axis (`45°–70°` bank) so the flat of the silver blade and the face of the white jade ring flash toward the 55° camera! Centrifugal force widens the outer cloud-guard streamer into a crescent fin (`0.85` brightness over `0.08` dark backing), spawns 1–2 stepped afterimage echoes on the outside of the curve, and sheds 2–3 crisp elemental motes.
- **4. Strike (Pierce / Slash Impact — 60 to 120 ms):**
   - **Visual Shift:** As the sword spears a beast, forward velocity spikes: the qi sheath stretches forward (`1.4×` length) into a needle-sharp *jianqi* lance; the tip star elongates into a high-HDR cross-slit (`2.2` luminance, 30% white + 70% element hue); a dark ink-slash cross-mark (`0.05` RGB) stamps behind the bright impact flash so the hit reads instantly without obscuring the beast.
- **5. Return (Recall & Sheathe Orbit):**
   - **Visual Shift:** HDR core drops to `1.1`, ribbon trails shorten by `60%` and fade into dotted calligraphy strokes, leaving the silver blade, jade ring, and tassel cleanly visible as the swords arc back toward the cultivator.

#### C. Screen-Space Readability Audit: What Survives at 35–130 px (1080p, 55° Camera)

*(My Technical Opinion based on Nyquist sampling limits at 1080p)*:

| Screen Size Tier | Role in Your River | Layers That SURVIVE Cleanly | Layers That DIE / Alias (Must Strip or Clamp) |
| --- | --- | --- | --- |
| **100–130 px** | **6 Full Hero Swords** (Lead formation) | All layers: physical silver blade, cloud guard silhouette, **white jade ring hole**, tassel, dark backing, qi sheath, 1.5 px HDR ridge core, guard runes, tip star, ribbon trail. | Ultra-fine internal rune strokes `< 2 px` thick will shimmer unless mip-biased (`lodBias = +0.5`). |
| **55–95 px** | **24 LOD Swords** (Flanking stream) | Physical blade + guard silhouette, **jade ring reads as a bright `3–4 px` O-dot**, dark backing cushion, qi sheath, HDR ridge core, tip star, simplified 1-strip tassel ribbon (on 20 of 24 swords). | Individual rune text characters, dual winglet threads (merge into main ribbon), internal normal refraction. |
| **35–50 px** | **64 Impostor Sprites** (Dense river body) | **Only 4 macro signals survive:** (1) Dark backing silhouette (`6–8 px` wide), (2) Silver blade body + **1–2 px HDR spine line**, (3) **High-contrast guard dot** (representing the white jade ring + cloud guard), (4) **Baked short tail taper** (`12–18 px` long) with tip glint. | Fine cloud-guard scrolls, separate tassel geometry, multi-layered shells, motes, and runes all collapse into sub-pixel noise and must be baked or culled. |

### 3. How Games Keep 90+ Flying Swords Cheap (+0.6 ms Budget Breakdown)

To render ~94 dressed swords (6 Full + 24 LOD + 64 Impostors) within **+0.6 ms p95 at 1080p in WebGL**, **≤ 32 live ribbons**, **≤ 32 extra VFX draw calls**, and **≤ 3 overlapping transparent layers per pixel**, modern engines combine five proven techniques:

1. **Single-Pass `InstancedMesh` & `BatchedMesh` Collapse:**
   - **How Games Do It:** In Three.js, every separate `Mesh` costs at least one WebGL draw call and CPU state validation; collapsing repeated geometry into `THREE.InstancedMesh` (or `THREE.BatchedMesh` in r159+/r170+) draws hundreds of transforms in a single call ([Hon Tran: Three.js Performance Optimization Guide](https://www.hontran.dev/blog/three-js-performance-optimization); [Three.js Performance Optimization Checklist](https://github.com/freshtechbro/claudedesignskills/blob/main/plugins/bundles/core-3d-animation/skills/threejs-webgl/references/optimization_checklist.md); [three.ez/instanced-mesh](https://threejsresources.com/tool/three-ez-instanced-mesh)).
   - **Application to Clear Wind (Opinion):** Pack a single `InstancedBufferAttribute` (`vec4 aSwordState`: `x = phase [0..4]`, `y = bankAngle`, `z = speedNorm`, `w = randomSeed`). Render all **6 Full + 24 LOD aura shells** in **1 single `InstancedMesh` draw call** (30 instances total).
2. **Multi-Channel Angle-Atlas / Hemi-Octahedral Impostors:**
   - **How Games Do It:** Pioneered by Ryan Brucks at Epic Games (*Fortnite* Battle Royale) and widely adopted for dense swarms, **Octahedral / Hemi-Octahedral Impostors** capture a 3D mesh from a hemisphere of view angles into a 2D texture atlas and reconstruct the nearest frame(s) in the vertex/fragment shader using L1-norm math with zero trig functions ([Ryan Brucks / ShaderBits: Octahedral Impostors](https://shaderbits.com/blog/octahedral-impostors); [Yummers.dev: Hemi-Octahedral Impostors Implementation](https://www.yummers.dev/hemi-octahedral-impostors.html); [Medium: Octahedral Imposters Guide](https://madarapremawardana.medium.com/the-only-imposter-who-come-in-handy-octahedral-imposters-e2b002379a98)).
   - **Application to Clear Wind (Opinion):** Because your camera is fixed at a **55° top-down 3/4 pitch**, you don't even need a full 3D sphere! Bake a **1D/2D Pitch-Locked Yaw+Roll Atlas** (`16 yaw angles × 4 roll angles = 64 tiles` on a single `1024×1024` texture) of *Clear Wind*. Crucially, instead of baking static RGB colors, pack **4 semantic channels into one RGBA texture**:
      - `R` = Lit Silver Blade + Cloud Guard + White Jade Ring grayscale luminance (so the real sword stays 100% visible!)
      - `G` = Qi Sheath + Short Wake mask (`[0..1]` density, capped at `0.9` output)
      - `B` = Thin HDR Core + Tip Star + Jade Ring Highlight mask (`> 1.0` HDR multiplier)
      - `A` = Combined Silhouette Alpha (where `A > 0` and `R+G == 0` automatically renders the **Dark Backing Cushion**!)
      - **Result:** All **64 Impostor Swords + their dressed aura + their short wake** render in **1 single `InstancedMesh` draw call** (`128 triangles` total) and dynamically swap between Metal, Fire, and Water using the exact same element kit LUT!
3. **Merged Shell / Cross-Fin Meshes with Premultiplied Alpha (Zero Extra Overdraw):**
   - **How Games Do It:** Instead of stacking separate meshes for the dark backing, mid-halo, and bright core (which would instantly hit 3–4 layers of overdraw per sword), AAA stylized VFX combine the **dark backing and bright core into a single shader pass** using **Premultiplied Alpha blending** (`gl.ONE, gl.ONE_MINUS_SRC_ALPHA`).
   - **Application to Clear Wind (Opinion):** When `rgb < alpha`, the shader darkens the background (acting as your mandatory dark backing layer); when `rgb > alpha` (up to `1.8` on the thin spine), the exact same pixel adds HDR bloom! This gives you **Dark Backing + Element Halo (≤0.9) + HDR Core in 1 transparent layer of overdraw** instead of 3.
4. **GPU Ring-Buffer Ribbon Pool (Capped at 26–32 Live Ribbons):**
   - **How Games Do It:** Updating ribbon geometry on the CPU every frame causes GC stalls and buffer-upload bottlenecks in WebGL. Instead, games allocate a single merged ribbon mesh for `N` ribbons (e.g., `26 ribbons × 10 segments = 520 triangles`) and store the last `10` positions of those 26 swords in a tiny `26×10` `RGBA16F` DataTexture (or uniform array) updated once per frame ([GDC Vault: Making Magic with Textures in the Vertex Shader](http://gdcvault.com/play/1024616/The-Illusion-of-Motion-Making)).
   - **Application to Clear Wind (Opinion):** Attach live ribbons only to the **6 Full Swords + 20 outer/leading LOD Swords = 26 live ribbons** (safely under your 32 ribbon cap). The remaining 4 interior LOD swords and 64 impostors use **vertex-stretched short tail fins** baked into their mesh/impostor card (`0` extra ribbons).
5. **Flowmaps & Vertex Shader Motion (VAT):**
   - **How Games Do It:** Rather than spawning hundreds of short-lived particles for fire flames, water ripples, or wind wisps, VFX artists pan a 2-channel RG flowmap across the aura shell and use vertex-shader displacement / Vertex Animation Textures (VAT) for organic undulation ([80 Level: Physics-Based Flowmap Painter](https://80.lv/articles/physics-based-flowmap-painter-for-unreal); [SideFX Houdini: Vertex Animation Textures for Realtime FX](https://www.sidefx.com/docs/houdini//nodes/out/labs--vertex_animation_textures-3.1.html); [LuosArts RealtimeVFX Flowmap Resources](http://luosarts.com/links/)).

### 4. Three Original Aura Directions for *Clear Wind*

*(Note: All three directions below are original visual designs tailored specifically to Clear Wind’s silver blade, white jade ring, cloud guard, and tassel, and represent my own design work and performance estimates.)*

#### Direction 1: **"Jade-Aperture Calligraphic Slipstream"** (*Qingfeng Mo-Yun* / 清风墨韵)

- **Core Concept:** Inspired by high-cultivation scholar-swordsmen. The aura treats *Clear Wind*’s **white jade ring as the "eye" of a Daoist ink-and-qi brush**. The physical silver blade remains completely uncovered along its central flat so the metal gleams cleanly; the aura hugs only the outer bevels like a razor-thin calligraphic stroke backed by sumi-ink shadow, while the cloud guard channels two crisp silk-scroll slipstreams that braid with the physical tassel.
- **Layer Breakdown:**

| Layer | Visual Role on *Clear Wind* | Rough Brightness (RGB / HDR) | Phase Behavior (Launch / Cruise / Turn / Strike / Return) | Survives at 35 px? |
| --- | --- | --- | --- | --- |
| **1. Sumi-Ink Cushion** | Tight inverted-hull/card backing around blade & wake | `0.04–0.10` RGB, `0.70` Alpha | Expands `1.3×` on **Turn** and **Strike** to frame the bright flash; thins on **Return**. | **Yes** (Forms the `7 px` high-contrast outer hull). |
| **2. Jade-Ring Collar Halo** | Toroidal qi ring hugging the white jade guard ring + 3 rotating seal ticks | `0.75–0.88` max per channel (No bloom) | Snaps inward on **Launch**; spins faster on **Turn**; flares on **Strike**. | **Yes** (Reads as a crisp `3–4 px` bright O-dot at the hilt). |
| **3. Bevel Calligraphic Sheath** | Split twin-fin sheath hugging only the left/right cutting edges, leaving the silver fuller bare | `0.60–0.85` max per channel (No bloom) | Laminar in **Cruise**; outer bevel widens into a crescent wing on **Turn**; projects `20%` past tip on **Strike**. | **Yes** (Merges with blade silhouette at 35 px). |
| **4. Razor Spine & Tip Star** | `1.5 px` HDR line along the central diamond ridge + 4-point needle star at tip | `1.65` HDR Cruise → `2.2` HDR Strike (`≤25%` white) | Ignites guard-to-tip on **Launch**; steady in **Cruise**; elongates into a lance slit on **Strike**. | **Yes** (Primary 1–2 px directional read at 35 px). |
| **5. Split-Brush Tassel Ribbon** | Single GPU ribbon extending the pommel tassel with dry-brush alpha erosion at the tail | Head: `0.85`, Wake: `0.45` over `0.06` dark edge | Smooth sine wave in **Cruise**; whips wide with 2 stepped afterimage ticks on **Turn**. | **Partial** (26 swords use live ribbons; 64 impostors use baked `14 px` dry-brush tail). |
| **6. Pass-Floor Light Wash** | 4 shared instanced ground decals beneath the river | `0.35` max per channel (Modulated additive) | Tracks river centroid; pulses `0.50` when lead swords **Strike**. | **N/A** (Shared river-level layer). |

- **Element Kit Material Swaps (Same Geometry & Shader, Swapped `32×1` LUT + Flowmap):**
   - **Metal (Default):** Deep Slate-Ink backing (`#0B131E`) → Celadon-Cyan & Silver-Frost sheath (`<= 0.88`) → Ice-Cyan/Silver HDR core (`[1.3, 1.75, 1.85]`, 25% white). Flowmap uses straight, high-speed laminar wind streaks.
   - **Fire:** Charred Obsidian-Soot backing (`#1A0D08`) → Imperial Amber (`#E07A16`) & Vermilion-Gold (`#E59824`) sheath (strictly zero `#FF4A4A` red; warmest accent is deep Cinnabar-Plum `#9E1946`) → Solar White-Gold HDR core (`[1.9, 1.55, 0.85]`). Flowmap switches to upward-curlingphoenix-feather tongues.
   - **Water:** Abyssal Indigo backing (`#061024`) → Deep Sea-Teal (`#127896`) & Jade-Foam (`#68D8D6`) sheath → Moonlight Aqua HDR core (`[1.1, 1.65, 1.85]`). Flowmap switches to curling wave-crest ripples.
   - *(Future Hooks: **Wood** = Pine-Ink backing + Emerald/Bamboo-Jade sheath; **Earth** = Basalt-Umber backing + Ochre/Topaz-Gold crystalline facets; **Thunder** = Storm-Violet backing + Indigo/Electric-Lilac jagged stepped UV offsets).*
- **Why It Is Captivating, Luxurious & Modern (My Opinion):** It turns 94 flying swords into a **living 3D Chinese ink-and-gold scroll painting** (*Guofeng* aesthetic popularized by *Sword of Coming* and *Wuthering Waves*). Because the center of the blade is left bare, players clearly see the silver metal flashing inside the dark-ink-and-cyan frame.
- **Rough Cost for ~94 Swords (1080p WebGL, High):**
   - **Extra VFX Draw Calls:** **4 draw calls** (`1` InstancedMesh for 30 aura shells + `1` merged GPU Ribbon mesh for 26 ribbons + `1` InstancedMesh for 64 dressed impostors + `1` InstancedMesh for 4 ground decals).
   - **Live Ribbons:** **26** (6 Full + 20 outer LODs).
   - **Avg Transparent Overdraw:** **~1.8 layers/pixel** (Premultiplied single-pass shell + ribbon).
   - **Estimated GPU Time (p95 at 1080p):** **~0.38 ms** (well under your +0.6 ms cap).

#### Direction 2: **"Astral Cloud-Loom & Sovereign Halos"** (*Xingyun Jianzhen* / 星云剑阵)

- **Core Concept:** Inspired by celestial *Xianzhou* / *Jade Dynasty* immortal arrays. Instead of wrapping the entire blade in a continuous sleeve, this direction **dresses the architecture of Clear Wind in three discrete jewelry-like stations**: (1) a needle-sharp *Star-Tip Crown*, (2) a *Cloud-Guard Winglet Halo* that interlocks with the white jade ring, and (3) a *Twin-Swallow Tail* streaming from the tassel. The silver blade between the guard and tip stays 85% exposed, bridged only by an ultra-thin HDR meridian wire.
- **Layer Breakdown:**

| Layer | Visual Role on *Clear Wind* | Rough Brightness (RGB / HDR) | Phase Behavior (Launch / Cruise / Turn / Strike / Return) | Survives at 35 px? |
| --- | --- | --- | --- | --- |
| **1. Eclipse Backing Diamond** | Elongated diamond dark card behind the guard and tip | `0.05–0.12` RGB, `0.65` Alpha | Pulses outward at **Launch**; locks tight in **Cruise**; stretches on **Strike**. | **Yes** (Creates a distinct broad-shouldered dagger silhouette at 35 px). |
| **2. Cloud-Guard Interlocking Halo** | Crescent constellation arc framing the cloud guard + white jade ring without touching it | `0.80–0.90` max per channel (No bloom) | Rotates `90°` into lock position on **Launch**; banks sharply with the sword on **Turn**. | **Yes** (The crescent guard arc makes the hilt end unmistakable at 35 px). |
| **3. Meridian Thread & Tip Star** | `1 px` HDR wire running through the white jade ring Hole to the tip + 6-point asymmetric star | `1.75` HDR Cruise → `2.4` HDR Strike (`≤30%` white) | Thread shoots from ring to tip on **Launch**; star flares into a cross-burst on **Strike**. | **Yes** (Sharpest point-and-spine read of all three directions). |
| **4. Stepped Afterimage Phantoms** | 2 instanced ghost copies of the blade+guard silhouette spawned only during high angular velocity | `0.55–0.70` over `0.08` dark rim (No bloom) | `0` in **Cruise** (zero cost); spawns 2 stepped echoes on **Turn** and **Strike**. | **No** (Culled on the 64 impostors; active only on the 6 Full + 24 LOD swords). |
| **5. Swallow-Tail Tassel Streamer** | Forked two-prong ribbon trailing from the tassel and cloud-guard tips | `0.85` head → `0.30` tail over `0.07` dark backing | Parallel twin lines in **Cruise**; crosses into a double-helix braid on **Turn**. | **Partial** (26 live ribbons; baked forked tail on 64 impostors). |
| **6. Constellation Mote Buffer** | 48 shared instanced star-diamond flecks shed across the whole river | `0.90` edge + `1.4` 1-px center | Emits along the outer curve of the river during **Turn** and **Strike**. | **Yes** (Individual `3–4 px` diamond glints read cleanly at river scale). |

- **Element Kit Material Swaps:**
   - **Metal:** Midnight-Indigo backing → Platinum-Silver & Cyan-Jade guard crescent (`≤ 0.90`) → White-Cyan Astral Wire (`1.8` HDR). Motes are 4-point silver-cyan stars.
   - **Fire:** Smoked-Bronze backing → Burnished Sun-Gold (`#F2A922`) & Deep Copper-Orange (`#D95B16`) solar ring → Blazing Champagne-Gold HDR wire (`2.0` HDR, zero `#FF4A4A`). Motes are crisp diamond sparks.
   - **Water:** Deep Abyssal-Teal backing → Pearl-Turquoise & Sapphire-Blue crescent → Glacial Cyan-White HDR wire. Motes are crisp hexagonal ice-dew prisms.
- **Why It Is Captivating, Luxurious & Modern (My Opinion):** It feels **architectural, aristocratic, and precision-engineered**—like a high-tier 5-star signature weapon reveal. By concentrating the aura around the cloud guard/jade ring and the sword tip while leaving the mid-blade bare except for a `1 px` HDR meridian wire, *Clear Wind*’s real 3D model is showcased better than in any conventional sheath aura.
- **Rough Cost for ~94 Swords (1080p WebGL, High):**
   - **Extra VFX Draw Calls:** **6 draw calls** (`1` InstancedMesh for 30 guard/tip shells + `1` InstancedMesh for conditional turn afterimages + `1` merged GPU Ribbon mesh for 26 ribbons + `1` InstancedMesh for 48 shared motes + `1` InstancedMesh for 64 impostors + `1` InstancedMesh for ground decals).
   - **Live Ribbons:** **26**.
   - **Avg Transparent Overdraw:** **~2.1 layers/pixel** (up to ~2.6 during sharp turns when afterimages spawn).
   - **Estimated GPU Time (p95 at 1080p):** **~0.49 ms**.

#### Direction 3: **"Hydrodynamic Dragon-Scale Wake"** (*Canglong Yujian* / 沧龙御剑)

- **Core Concept:** Designed specifically to maximize the **"River of 94 Swords"** (*Myriad-Swords*) fantasy from Han Li’s *Azure Bamboo Cloudswarm* and Erlang Shen’s *River of Swords*. Each sword wears a sleek, swept-back **chevron pressure wave** (*mach cone*) that starts *behind* the tip so the silver point pierces clean air first, flows back over the bevels in overlapping translucent chevron scales, and parts around the white jade ring like water around a smooth river stone.
- **Layer Breakdown:**

| Layer | Visual Role on *Clear Wind* | Rough Brightness (RGB / HDR) | Phase Behavior (Launch / Cruise / Turn / Strike / Return) | Survives at 35 px? |
| --- | --- | --- | --- | --- |
| **1. Abyssal Wake Trench** | V-shaped dark trough behind the cutting bevels and tassel | `0.03–0.09` RGB, `0.75` Alpha | Widens into a V-wake on **Turn**; narrows into a needle dart on **Strike**. | **Yes** (Gives every 35 px sword a sharp arrowhead contrast shadow). |
| **2. Swept Chevron Qi Fin** | Swept-back winglet shell (`25°` sweep angle) with scrolling chevron-scale alpha bands | `0.65–0.88` max per channel (No bloom) | Chevron bands scroll backward at `2×` speed during **Strike**; bank fins flare on **Turn**. | **Yes** (2–3 macro chevron bands remain visible at 55–130 px; merges to a crisp V-fin at 35 px). |
| **3. Leading-Edge Mach Slit** | Ultra-thin HDR compression line hugging only the front `40%` of the blade edges + jade ring inner rim | `1.70` HDR Cruise → `2.3` HDR Strike (`≤30%` white) | Concentrates all HDR energy at the piercing front `40%` of the sword + jade ring. | **Yes** (Creates an unmistakable bright arrowhead + guard dot at 35 px). |
| **4. Vortex Tassel Ribbon** | Single tapered ribbon using a 2D sine-displacement vertex shader so the wake ripples like a swimming dragon tail | `0.85` head → `0.25` tail over `0.05` dark border | Synchronized phase offset across the river so adjacent ribbons ripple in unison. | **Partial** (28 live ribbons; 64 impostors use vertex-waving 4-segment quad strips). |
| **5. River Current Ground Streaks** | 5 elongated flow-streaks projected onto the pass floor underneath the sword river | `0.40` max per channel | Scrolls along the river’s spline path to sell ground-relative velocity. | **N/A** (Shared river-level layer). |

- **Element Kit Material Swaps:**
   - **Metal:** Deep Iron-Blue trench → Silver-Teal & Pale Cyan chevron fins (`≤ 0.88`) → White-Silver Mach Slit (`1.8` HDR).
   - **Fire:** Volcanic Basalt trench → Molten Gold (`#F5B027`) & Sunset Amber-Orange (`#E86A17`) magma-scale chevrons (no `#FF4A4A`) → White-Gold Mach Slit (`2.1` HDR).
   - **Water:** Midnight Trench-Blue → Pelagic Cerulean & Seafoam-Jade chevrons → Bioluminescent Cyan-White Mach Slit (`1.75` HDR).
- **Why It Is Captivating, Luxurious & Modern (My Opinion):** When 94 swords fly together in a 55° top-down view, synchronized phase-offset chevron wakes make the entire swarm read as **one cohesive, terrifyingly fast super-organism made of 94 distinct silver-and-jade blades**.
- **Rough Cost for ~94 Swords (1080p WebGL, High):**
   - **Extra VFX Draw Calls:** **4 draw calls** (`1` InstancedMesh for 30 chevron shells + `1` merged GPU Ribbon mesh for 28 ribbons + `1` InstancedMesh for 64 4-segment impostor strips + `1` InstancedMesh for 5 ground streaks).
   - **Live Ribbons:** **28** (6 Full + 22 LODs).
   - **Avg Transparent Overdraw:** **~2.2 layers/pixel**.
   - **Estimated GPU Time (p95 at 1080p):** **~0.44 ms**.

### 5. Ranked Comparison Table of the Three Directions

*(My Overall Recommendation & Ranking for Clear Wind)*:

| Rank | Direction Name | *Clear Wind* Hardware Readability (Blade, Jade Ring, Cloud Guard, Tassel) | 35 px Impostor Readability (1080p @ 55° Tilt) | Element Kit Versatility (Metal, Fire, Water + Wood/Earth/Thunder) | Extra VFX Draw Calls (Cap: 32) | Live Ribbons (Cap: 32) | Avg Overdraw Layers/px (Cap: 3.0) | Est. p95 GPU Cost @ 1080p (Budget: +0.6 ms) | Why It Ranks Here |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **#1 (Best All-Round)** | **Direction 1: Jade-Aperture Calligraphic Slipstream** | **10 / 10** — Central silver blade flat is 100% bare; white jade ring is framed by a dedicated non-blooming collar halo. | **9.5 / 10** — Sumi-ink cushion + bright jade-ring O-dot + 1.5 px HDR spine reads instantly over any map tile. | **10 / 10** — Dry-brush + flowmap LUT swaps effortlessly across all 6 Five-Element kits. | **4** | **26** | **~1.8** | **~0.38 ms** | Best balance of **Guofeng luxury, zero model obstruction, and lowest GPU cost** (+0.22 ms headroom to spare). |
| **#2 (Most Luxurious Hero Detail)** | **Direction 2: Astral Cloud-Loom & Sovereign Halos** | **9.5 / 10** — Mid-blade is 85% bare; jewelry-like crescent halo turns the cloud guard & jade ring into the centerpiece. | **9.0 / 10** — Broad guard-crescent + tip star creates a super-crisp dagger-constellation silhouette. | **9.0 / 10** — Excels on Metal, Thunder, Water, and Solar-Fire; slightly more geometric for Wood. | **6** | **26** | **~2.1** | **~0.49 ms** | Highest **"5-star gacha signature weapon"** prestige on the 6 Full + 24 LOD swords; turn-afterimages add huge flair. |
| **#3 (Best Swarm / River Feel)** | **Direction 3: Hydrodynamic Dragon-Scale Wake** | **8.5 / 10** — Tip and jade ring are crisp, though swept chevron fins cover ~35% of the outer blade bevels. | **9.0 / 10** — V-shaped Mach slit + dark trench makes the 64 impostors look like a schooling predator swarm. | **9.0 / 10** — Incredible for Water, Wind/Metal, and Fire; chevron scales feel more fluid than solid Earth. | **4** | **28** | **~2.2** | **~0.44 ms** | Unbeatable **kinetic flow and swarm cohesion** for the 94-sword river, at the cost of slightly more blade coverage. |

For a practical visual walkthrough of how sword trail textures, ribbon renderers, and gradient-mapped materials are assembled in a modern real-time shader pipeline, check out this [Create Sword Trail Slash - Unreal Engine 5 Detailed Tutorial](https://www.youtube.com/watch?v=ixvBQWsZreo). It demonstrates how a grayscale trail mask is paired with a color-grading ramp and dynamic ribbon UVs—the exact same workflow used to swap *Clear Wind*’s aura between Metal, Fire, and Water in Three.js.

## C. Claude kiểm nguồn (03/11/2026)

Gemini dẫn nhiều link, nhưng phần lớn là wiki fandom và Reddit:
- **Fandom** trả về 402 với WebFetch;
- **Reddit** bị chặn cả với WebFetch lẫn trình duyệt của ứng dụng.

Vì vậy Claude kiểm bằng nguồn khác khi có thể.

| Khẳng định | URL | Kết quả |
|---|---|---|
| Hướng dẫn VFX của League: phần chính có giá trị cao, viền rõ, đục, có tiêu điểm; phần phụ tối hơn, mờ hơn; tránh trắng 100 % | https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips | **Đúng.** Bài ghi "avoid absolute extremes (0% pure black or 100% pure white)" và dành đỉnh sáng cho chớp chính. Bài dẫn style guide của Riot (Jin Ho Yang). |
| Bài "Artistic Principles of Visual Effects in Video Games" trên ResearchGate | https://www.researchgate.net/publication/407219916_Artistic_Principles_of_Visual_Effects_in_Video_Games | **Chưa kiểm được** (403). |
| Erlang Shen (Black Myth) là boss bí mật ở núi Mi, triệu cả trường kiếm bay rồi trút mưa kiếm | https://blackmythwukong.fandom.com/wiki/Erlang_Shen | **Đúng phần chính**, kiểm qua hướng dẫn của maxroll.gg và keengamer (fandom trả 402): "summon a field of flying swords", "rain a storm of swords". Tên "River of Swords" và đòn kết "red-lightning" chưa thấy. |
| Yanqing (HSR) điều khiển trận kiếm "via Soulsteel Sync"; tuyệt kỹ "Amidst the Raining Bliss / Cascading Laceration" | https://honkai-star-rail.fandom.com/wiki/Yanqing/Story | **Đúng một phần.** Tuyệt kỹ đúng là Amidst the Raining Bliss. Nhưng Soulsteel Sync là trạng thái buff do kỹ năng Darting Ironthorn bật, không phải cơ chế điều khiển kiếm (Mobalytics, Prydwen). "Cascading Laceration" không thấy nguồn. |
| Han Li có 36–72 thanh Thanh Trúc Phong Vân Kiếm; donghua vượt 7 tỷ lượt xem | https://en.wikipedia.org/wiki/A_Record_of_Mortal%27s_Journey_to_Immortality | **Không có trong nguồn dẫn.** Wikipedia không nhắc tên hai món kiếm và không nhắc 7 tỷ lượt xem; nó chỉ ghi lượt click của bản tiểu thuyết. Con số này chỉ dựa vào một chuỗi Reddit mà Claude không mở được. |
| Wuthering Waves có cơ chế "Sword Flight" có thanh sức bền, ra ở bản sau (3.5) | https://www.reddit.com/r/wherewindsmeet_/comments/1oz9lq0/flying_swords_in_wwm/ | **Sai nguồn, sai bản.** Gemini dẫn một chuỗi Reddit của game khác. Ghi chú chính thức của Kuro gắn Sword Flight với Qingxiao, ra ở bản 3.6 (Claude đã đọc bản 3.6 và 3.7, xem file ChatGPT). Gemini cũng bỏ sót Qingxiao, tham chiếu sát nhất năm 2026. |
| Ryan Brucks (Epic) mở đầu impostor bát diện cho Fortnite | https://shaderbits.com/blog/octahedral-impostors | **Đúng một phần.** WebFetch chỉ đọc được khung trang. Diễn đàn three.js dẫn "the great blog post by Ryan Brucks on impostors in Fortnite/Unreal", và 80.lv có bài về plugin Impostor Baker của ông. |
| GDC "The Illusion of Motion: Making Magic with Textures in the Vertex Shader" làm nguồn cho vòng ribbon trên GPU | http://gdcvault.com/play/1024616/The-Illusion-of-Motion-Making | **Đúng một phần.** Bài có thật: Mario Palmero, Tequila Works, GDC 2017, về kết cấu đọc trong vertex shader và hoạt ảnh không qua CPU. Bài không nói về ribbon; cách dựng vòng ribbon là suy luận của Gemini. |
| Susanoo (Onmyoji) có 6 thanh kiếm thần lơ lửng sau lưng như vầng sấm vàng | https://onmyoji.fandom.com/wiki/Susanoo | **Chưa kiểm được.** Fandom trả 402; tìm kiếm không ra mô tả kỹ năng. |
| Jingke của Wang Ling là kiếm gỗ có linh tính, xé được không gian | https://the-daily-life-of-the-immortal-king.fandom.com/wiki/Jingke | **Đúng một phần.** Tóm tắt mùa 2 có đoạn Jingke xé rách không gian. Chi tiết "kiếm gỗ đào" chỉ thấy ở trang hồ sơ không chính thức. |
| Kiếm dài Naraka phóng sóng kiếm khí khi đánh tích lực | https://www.narakathegame.com/guide/weapon/ | **Chưa kiểm được** (trang dựng bằng JS). |
| Câu nói về fan: Xingqiu, Changli, Yanqing, Erlang, RMJI, Sword of Coming, Yun Yun, Tower of Fantasy "white blobs" | các link `reddit.com` | **Chưa kiểm được** (Reddit bị chặn). Câu Tower of Fantasy và câu "dấu ấn sumi-e của Kuro" không có nguồn nào kèm; đó là ý kiến của Gemini. |
| Số draw call (4–6), số ribbon (26–28), lớp chồng (1,8–2,2) và chi phí (0,38–0,49 ms) | — | **Là ước lượng của Gemini**, chưa đo. |

**Nguồn yếu cần biết:**
- Một "Three.js Performance Optimization Checklist" nằm trong một repo kỹ năng cho tác tử AI trên GitHub (`claudedesignskills`).
- Blog cá nhân hontran.dev.
- Các wiki VS Battles và Heroes Wiki.
- Những nguồn này không đủ để dẫn khi ra quyết định.

**Tóm lại:** Gemini mạnh ở phần kỹ thuật dựng hình. Phần "fan yêu nhất" yếu hơn ChatGPT: nhiều câu dựa vào wiki fandom, có một nguồn sai bản, và Gemini thiếu Qingxiao.

## D. Đánh giá của Claude

**Đồng ý (hai bên tự đi tới cùng một kết luận, nên tin được hơn):**
- **"Dressed relic", kiếm vẫn là kiếm.** Fan ghét thanh kiếm có tên biến thành que phát sáng vô danh. Ý này trùng với luật của anh và với ChatGPT.
- **Có thứ bậc trong dòng kiếm:** vài kiếm "dẫn đầu" đủ chi tiết, phần còn lại bơi theo như đàn cá.
- **Một lớp trong suốt cho mỗi kiếm:** premultiplied alpha, `rgb < alpha` làm tối nền, `rgb > alpha` cộng sáng. Lớp tối, thân và lõi HDR nằm trong một lần vẽ. ChatGPT nói cùng ý.
- **Dải màu theo hệ là LUT 32×1**, trùng với "Element ramp atlas" trong `ELEMENT_LAYER.md` §3.

**Ý hay riêng của Gemini, nên lấy:**
- **Atlas impostor theo kênh ngữ nghĩa:**
  - R là độ sáng của kiếm thật;
  - G là mặt nạ vỏ và vệt ngắn;
  - B là mặt nạ lõi HDR và sao mũi;
  - A là bóng dáng.
  - Một atlas phục vụ mọi hệ. Atlas impostor hiện tại nung sẵn màu nên phải nung lại theo kênh.
  - Camera mình cố định 55°, nên atlas chỉ cần các góc yaw và roll, đúng như Gemini nói.
- **Liệng nghiêng khi rẽ:** kiếm lật 45–70° khi rẽ để mặt lưỡi và mặt ngọc lóe về phía camera. Rẻ, đẹp, và là chuyển động của vũ khí, nên thuộc lớp hình.
- **Chòm hai điểm:** sao mũi kiếm và chấm "O" sáng ở vòng ngọc chỉ hướng kiếm ngay ở 35 px.
- **Hướng 2, Astral Cloud-Loom & Sovereign Halos:** đặt ánh sáng thành ba "trạm trang sức" (mũi, vòng ngọc với cung trăng quanh chắn mây, tua én đôi), để 85 % thân lưỡi trần. Đây là hướng gần nhất với khẩu vị "rực rỡ, có hào quang, sang" của anh và với bộ radiance.

**Không đồng ý:**
- **26–28 ribbon sống gần chạm trần 32,** chẳng còn chỗ cho va chạm, đất, thú. Cách của ChatGPT tốt hơn: 4–10 ribbon cấp dòng, vây instanced cho 24 kiếm LOD.
- **Hướng 1 (Calligraphic Slipstream) gần như trùng Calligraphy Wake của ChatGPT.** Cả hai cùng nghĩ tới mực tàu, vì đây là motif quá phổ biến (Sword of Coming, nhiều game "guofeng"). Muốn có bản sắc riêng thì không nên lấy mực làm ý chính, chỉ dùng như lớp tối mảnh.
- **Hướng 3 (Dragon-Scale Wake) che khoảng 35 % mép lưỡi,** trái luật "không che kiếm". Vệt chữ V đồng pha lại rất hay cho cả dòng, nên dùng làm lớp cấp dòng thay vì lớp trên từng kiếm.
- **Bùa văn trên vòng ngọc ở độ sáng 0,75–0,9 không đọc được dưới khoảng 100 px.** Chỉ để cho 6 kiếm chính.

**Cả hai cùng thiếu:**
- **Lửa phải liếm, không như sắt nung.** Cả hai chỉ viết "flowmap cho lưỡi lửa cong lên". Đúng lỗi anh vừa chê thì chưa ai giải.
  - Cần lưỡi lửa thật sự vượt khỏi viền kiếm (≥ 2–3 px ở 35 px), chạy ngược chiều bay và tách mảnh.
  - Cần thử clip heat-field và flipbook lửa có sẵn trên vỏ và vây trước khi vẽ mới.
- **Gắn với việc gõ.** Hào quang có thể dày lên theo chuỗi gõ đúng, và mỗi từ hoàn hảo cho một nhịp lóe ở vòng ngọc. Đây là móc riêng của game, chưa ai nghĩ tới.
- **Giữ chữ gõ đọc được.** Hào quang không được đi qua ô chữ. Phải đo tỉ lệ điểm ảnh gần trắng quanh chữ như phép thử Fire đã làm.
- **Thiếu nguồn tiếng Trung:** các bài phân tích của họa sĩ VFX NetEase, Tencent, miHoYo trên Bilibili, Zhihu, GameRes, UOD và GDC China.
- **Cách anh duyệt.** Ba hướng phải thành ảnh hoặc clip ở đúng camera chơi, 35, 70 và 130 px, trên nền sáng lẫn tối, kèm ảnh xám, để anh chọn.

**Gợi ý ba hướng để làm mẫu cho anh** (gộp từ hai nguồn, chưa ai duyệt):
1. **River-Silk Sheath** (ChatGPT A): vỏ lụa khí bám kiếm, hở ở vòng ngọc, lớp tối, thân và lõi trong một lần vẽ. Thêm chòm hai điểm và cú liệng nghiêng của Gemini.
2. **Sovereign Halos** (Gemini 2): ba trạm trang sức với cung trăng quanh chắn mây, dây kinh mạch 1 px, tua én đôi. Gần bộ radiance nhất.
3. **Dragon-Scale Current** (Gemini 3 chuyển thành lớp cấp dòng, cộng vây instanced của ChatGPT): mỗi kiếm chỉ có lớp tối, lõi và sao mũi. Vẻ đẹp nằm ở dòng chảy chung của 94 thanh.

Cả ba dùng cùng hai bộ chất Metal và Fire hiện có để so. Mức +0,6 ms cần chốt là riêng hào quang hay đã gồm chất của hệ, vì Fire đã thêm +0,23 ms ở phím 7.
