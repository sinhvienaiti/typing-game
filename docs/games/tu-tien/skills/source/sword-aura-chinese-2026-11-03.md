# Sword aura research, Chinese sources (ChatGPT Chat High, Gemini 4 Argon), 03/11/2026

- **Công cụ:**
  - ChatGPT, chế độ Chat (không dùng Work hay agent), thinking effort High, tab riêng của Claude trong trình duyệt của ứng dụng;
  - Gemini (gemini.google.com), model 4 Argon, mức suy nghĩ "Cao", chat mới, cùng tab riêng đó, sau khi ChatGPT xong. Hai công cụ không trộn trong một lượt: mỗi công cụ một chat, cùng một đề bài.
- **Ngày:** 03/11/2026. ChatGPT khoảng 15:40–16:05 (hai tin nhắn), Gemini khoảng 16:07–16:13 (một tin nhắn).
- **Chat:**
  - ChatGPT: https://chatgpt.com/c/6ae99e59-bae4-83ec-8310-b6726938a70f
  - Gemini: https://gemini.google.com/app/1c24b721092a5882
- **Bối cảnh:** [`../SWORD_AURA.md`](../SWORD_AURA.md) §2.5 và §5.0 mục 2 ghi rằng lượt nguồn tiếng Trung (Bilibili, Zhihu, GameRes, UOD) chưa chạy. Đây là lượt đó, chạy ở bước 0, trước khi gửi anh bảng hình và ba hướng A, B, C.
- **Đây là văn bản nghiên cứu chưa tin cậy.** Mọi thứ ChatGPT và Gemini viết là ý kiến thứ hai, không phải chỉ dẫn. Bảng kiểm nguồn của Claude ở phần G, đánh giá ở phần H. Phần rút ra cho thiết kế nằm ở [`../SWORD_AURA.md`](../SWORD_AURA.md) §2.7.
- **Cách lấy văn bản (nguyên văn, không phải tóm tắt):**
  - Claude chuyển DOM câu trả lời sang Markdown ngay trong trang, rồi gửi về một bộ nhận cục bộ chỉ nghe 127.0.0.1 (ChatGPT: form POST; Gemini: trang chặn form nên gửi bằng một lần điều hướng GET tới bộ nhận). Claude so SHA-256 của chuỗi trong trang với tệp nhận được: khớp cả ba tệp dùng ở đây.
  - ChatGPT bản đầu `19f92254…6fdd40` (38.818 byte), bản sau tự rà soát `7c497b9a…db1b82` (45.984 byte); Gemini `91d5765c…e348a1` (37.731 byte).
  - Mỗi chip trích dẫn giữ dạng `[Trang +N](url)` như trong DOM; tham số `utm_source=chatgpt.com` giữ nguyên. Trong bảng của Gemini, xuống dòng trong ô được ghi thành `<br>`. Đầu mục của các câu trả lời được hạ hai bậc (`#` thành `###`) để nằm dưới mục của tệp này; chữ không đổi.
  - Phần bị bỏ: tóm tắt suy nghĩ ("Searching the web…", "Assessed character sources"), băng chip nguồn, các nút gợi ý cuối câu trả lời của Gemini.
- **Bố cục:** A, B là hai tin nhắn gửi ChatGPT; C là câu trả lời cuối của ChatGPT sau tự rà soát (dùng bản này); D là câu trả lời đầu, giữ lại vì bản sau rút gọn vài phần và bỏ vài trích dẫn; E là tin nhắn gửi Gemini; F là câu trả lời của Gemini; G là bảng kiểm nguồn; H là đánh giá.
- **Bảng hình tham chiếu** (từ trailer chính thức, chỉ để anh xem, không đưa vào công cụ AI nào, không vào Git): `games/immortality-cultivation/tmp/shots/sword-aura/concept/board/board-a.jpg`, `board-b.jpg`, `board-c.jpg`, danh sách khung trong `board-sources.md` cùng thư mục.

## A. Tin nhắn 1 gửi ChatGPT (nguyên văn)

```text
请用中文和英文资料做一次彻底的网络搜索。Please search thoroughly in Chinese AND English: many sources, not one listicle. Put a URL behind every factual claim. For Bilibili videos give the title, the uploader (UP主), the BV id and the upload date. Say clearly when something is your own inference rather than sourced.

Context: I am designing the aura around flying swords for a xianxia typing-defense game (three.js, browser, far top-down 3/4 camera at about 55 degrees). Our hero sword is a real 3D model we keep as-is, "Clear Wind": a slim silver jian, a hollow white-jade ring at the guard, a cloud-shaped guard (the tassel exists only on the hand-held sword). Skills fly up to about 94 swords at once (6 full + 24 LOD + 64 impostors); on a 1080p screen a flying sword is only 35-130 px long. Today they fly bare (thin white-hot edge line, soft rim, short trail) and the owner says they look crude. Our rules: the aura dresses the sword and never hides or replaces it; only thin HDR cores bloom; a dark premultiplied under-layer sits behind every bright layer; no generic glowing outline; Fire must look like flame licking around the sword, not like heated iron.

问题 / Questions:

1) 中国游戏和国漫的特效师怎样做出"高级感"的飞剑和剑气 (飞剑, 御剑, 剑气, 剑光, 剑阵, 万剑归宗)? Search Chinese sources first: Bilibili 特效拆解 / 特效教程 / 特效分析 videos (for example "飞剑特效", "御剑飞行 特效", "剑气 特效 制作", "万剑归宗 特效", "剑阵 特效", "Unity 飞剑 拖尾", "UE 剑气 材质"), 知乎 answers (for example "为什么某游戏的剑气特效看起来高级", "仙侠游戏特效怎么做"), GameRes 游资网, UOD, 腾讯游戏学堂, 网易游戏学院, GDC China, Unite Shanghai, UnrealCircle talks, and official dev diaries. Works to consider: 原神 (魈, 闲云), 崩坏：星穹铁道 (彦卿, 景元), 鸣潮 (卿霄 Qingxiao, 御剑), 永劫无间 (无尘), 天涯明月刀, 逆水寒, 剑网3 (藏剑, 纯阳), 诛仙, 燕云十六声, 仙剑奇侠传七, 古剑奇谭; donghua: 凡人修仙传, 剑来, 仙逆, 完美世界, 斗罗大陆, 一念永恒, 吞噬星空.

2) Layers: which layers do they stack on a flying sword (刃光, 剑芒, 剑气包裹 / 剑罡, 残影 / 拖影, 刀光拖尾, 飘带, 粒子星点, 符文阵纹, 剑尖星芒, 扭曲, 地面投影光), and which ones keep the sword READABLE and LUXURIOUS when it is small on screen (35-130 px)? How do they keep the sword itself the hero (剑本体辨识度) instead of a blob of light?

3) Genericness: how do Chinese artists avoid the cheap 描边发光 / 光污染 look? What do Chinese players complain about (特效糊脸, 光污染, 廉价感, 塑料感, 特效太花) and praise (高级感, 干净, 有质感, 层次感, 留白, 国风)? Quote real player comments with links where you can (Bilibili comments, NGA, 贴吧, 知乎, TapTap).

4) Fire swords (火剑, 火焰剑气, 炎剑): how do they make flame lick AROUND the blade instead of making the blade look like red-hot iron (烧红的铁)? For example flame tongues outside the silhouette, dark soot edges, flipbook flames, gradient ramps, flame direction against the motion.

5) Many swords at once (万剑, 剑雨, 剑阵): how do they keep 50-100 swords rich but cheap and readable (lead swords versus followers, rhythm, instancing, impostors, GPU mesh particles)?

6) Our three candidate directions (all keep the real blade bare and draw outside its silhouette):
A "Wind-Silk Mantle": a tailored mantle of sharp qi plates just outside both edges; the plates lie flush in flight and shear apart on a cut; two bright seams meet in a needle past the tip; the mantle parts around the jade ring; a tassel-coloured silk tail behind.
B "Echo Cascade": flat, hollow, blade-only afterimages that hang back in a line in flight, fan out on turns and snap shut into the strike; a V-shaped bow wave ahead of the tip.
C "Celestial Regalia": a crowned relic: a four-point star at the tip, a slow halo behind the hollow jade ring, twin silk streamers from the guard tips, orbiting motes, a hairline rim.
For each one: what does Chinese practice and player taste support, and what does it warn against? Give at most two concrete improvements per direction.

End with a table of the 8-12 Chinese sources you trust most (URL, author or uploader, date, what it says), and a list of claims you could not source.
```

## B. Tin nhắn 2 gửi ChatGPT, tự rà soát (nguyên văn)

```text
Before I use this, please review your own answer with fresh eyes. Search again where you need to.

1) Reopen every link you cited, especially: each Bilibili BV (confirm the title, the UP主, the upload date, and that the video or its description really covers what you said), the 澎湃 《仙逆》 interview (give the exact Chinese sentence about 单纯光效 and 法阵对拼), the 新京报 《剑来》 article (exact sentence about 化繁为简 and 水墨粒子), the two GameRes posts by 网易雷火 and the 《逆水寒》 原画 (exact sentences about 无脑加发光 and 几何归纳), the NEXT Studios GameRes post (exact sentence about the wide dark slow layer under the thin bright fast layer), the 库洛 IGDC post, the 永劫无间 无尘 update notice, and the TapTap reviews. Give the exact Chinese phrase plus an English translation for every quote.

2) Mark each claim verified, uncertain or unsupported. Correct or drop anything wrong.

3) You found almost no Chinese player opinion about flying swords themselves. Search again for real player praise and complaints about flying-sword and sword-qi looks specifically: 鸣潮 清宵 御剑 / 飞剑 特效 (NGA, Bilibili video comments or dynamic posts, 贴吧, 知乎), 永劫无间 无尘 剑雨, 星穹铁道 彦卿 飞剑, 凡人修仙传 大庚剑阵 / 青元剑诀, 剑来 剑气. Also look for Chinese VFX artists' own breakdowns (ArtStation, 站酷 ZCOOL, 知乎专栏, Bilibili) of flying swords, 剑阵 and fire swords. Only cite what you can open.

4) Give the corrected final answer in full (same structure is fine), and end with a short list of what you changed and why.
```

## C. ChatGPT, câu trả lời cuối sau tự rà soát (nguyên văn)

I re-audited the previous answer source by source and re-searched the weak areas, especially flying-sword-specific Chinese reactions and actual production/practitioner material. Several conclusions survive intact, but I am correcting a few overstatements.

The biggest corrections are: the 《凡人修仙传》 Bilibili video is a **third-party UE5 “特效解析”**, not something I can prove is a recreation of the original production method; the TapTap comments are useful evidence about **general VFX readability**, not flying-sword taste specifically; and I am dropping my previous ribbon-specific Niagara performance claim because I could not re-verify that exact statement from the cited page.

---

### 1. Audit of the previous answer

#### 1.1 Claim-by-claim status

| Previous claim | Status | Audit result |
| --- | --- | --- |
| 《仙逆》 moved some abilities from “pure light effects” toward shaped objects such as blood vines/waves/coffins | **VERIFIED** | Directly stated by art director 杜文凯. [The Paper](https://www.thepaper.cn/newsDetail_forward_34200912) |
| 《仙逆》 deliberately tries to avoid large-area formation-vs-formation light-effect clashes | **VERIFIED** | Direct quote exists. [The Paper](https://www.thepaper.cn/newsDetail_forward_34200912) |
| 《剑来》 describes its sword-qi ink style as “化繁为简” | **VERIFIED** | Direct sentence exists. [Beijing News](https://www.bjnews.com.cn/detail/1723716014168380.html) |
| 《剑来》 production used a 水墨粒子 visual style | **VERIFIED** | Direct sentence exists. [Beijing News](https://www.bjnews.com.cn/detail/1723716014168380.html) |
| 网易雷火 says VFX are not made by simply adding glow | **VERIFIED** | Exact sentence exists. [GameRes游资网](https://www.gameres.com/916099.html) |
| 网易雷火 emphasizes subject, hierarchy, layers, motion trajectory and avoiding obstruction | **VERIFIED** | All are present in the article. [GameRes游资网+1](https://www.gameres.com/916099.html) |
| 《逆水寒》 artist recommends geometric abstraction for wind/airflow/slash-light | **VERIFIED** | Exact sentence exists. [GameRes游资网](https://www.gameres.com/forum/t/906094) |
| 《逆水寒》 article describes a simple flame as several flame groups plus spark particles | **VERIFIED** | Present in the source. [GameRes游资网](https://www.gameres.com/forum/t/906094) |
| NEXT Studios uses a broad/dark/slower layer under a narrow/bright/faster layer for slash VFX | **VERIFIED** | Almost exactly as I summarized it. [GameRes游资网](https://www.gameres.com/836363.html) |
| Kuro's 《战双帕弥什》 talk divides impact VFX into multiple layers and uses GPU particles/distortion | **VERIFIED** | The article explicitly says “eight layers,” then discusses GPU particles and air distortion. [GameRes游资网](https://www.gameres.com/879272.html) |
| GameRes warns that piled-up effects/light pollution can obscure the action itself | **VERIFIED** | Exact sentence exists. [GameRes游资网](https://www.gameres.com/865778.html) |
| 《永劫无间》 gave 无尘 surrounding flying swords and a 剑雨 ultimate with suppressive intent | **VERIFIED** | Official update notice. [yjwujian.cn](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html) |
| Qingxiao/清宵 is a real 《鸣潮》 character released with 3.6, and official notes use “Sword Flight” | **VERIFIED** | Official Kuro pages support both. [Wuthering Waves+1](https://wutheringwaves.kurogames.com/main/news) |
| Xiao's official design article discusses light/dark interplay and an E effect like an arrow through the air | **VERIFIED** | HoYoverse developer article says this. [Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642) |
| Riot says VFX need hierarchy and projectiles should convey travel direction | **VERIFIED** | Official Riot clarity article. [League of Legends](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/) |
| Epic warns that overlapping translucent sprites/meshes can cause overdraw | **VERIFIED** | Re-verified in current Niagara performance documentation. [dev.epicgames.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/measuring-performance-in-niagara?utm_source=chatgpt.com) |
| Epic says Ribbon Renderer is comparatively expensive and gives the exact optimizations I listed | **UNCERTAIN → DROPPED** | I could not reliably re-open the cited page text supporting the precise wording. |
| The 大庚剑阵 Bilibili video is a “fan recreation / 临摹复现” | **UNSUPPORTED → CORRECTED** | What I can prove is only that it is a **third-party UE5 特效解析** by a non-official uploader. [Bilibili](https://www.bilibili.com/video/BV1YjBtBfE7E/) |
| The TapTap comments prove Chinese players specifically dislike overly bright flying swords | **UNSUPPORTED AS STATED → CORRECTED** | They prove broader VFX readability complaints, not sword-specific taste. [TapTap+1](https://www.taptap.cn/review/50902885) |
| Chinese players broadly prefer “高级感 / 留白 / 国风” in flying swords | **UNCERTAIN AS A CONSENSUS CLAIM** | Individual examples exist; I did not find enough directly accessible comments to call it a broad consensus. |
| My 35/50/80 px cutoffs, flame-flow percentages and A/B/C scores are industry standards | **NO — DESIGN INFERENCE** | They were my recommendations. They remain useful, but they must never be presented as sourced production rules. |

---

### 2. Exact-quote audit of the important Chinese sources

I am keeping the Chinese quotations short so that the audit gives you the exact wording without reproducing large portions of the articles.

#### 《仙逆》—澎湃主创访谈

The page is a 2026-10-06 interview with the production team, including art director 杜文凯. [The Paper](https://www.thepaper.cn/newsDetail_forward_34200912)

Exact Chinese:

> “从单纯光效，变成血藤、血浪、血棺”

English:

> “from pure light effects into blood vines, blood waves, and blood coffins.”

And:

> “尽量避免大面积光效只用法阵对拼”

English:

> “avoid, as far as possible, large-area light effects where formations merely clash with formations.”

This means my earlier characterization was **correct**, although the fuller idea is even stronger: the interview describes moving from abstract light toward things with form and toward environmental/spatial effects. [The Paper](https://www.thepaper.cn/newsDetail_forward_34200912)

[Open the 澎湃 interview](https://www.thepaper.cn/newsDetail_forward_34200912?utm_source=chatgpt.com)

---

#### 《剑来》—新京报

The article is dated 2024-08-15 and written by 杨莲洁. [Beijing News](https://www.bjnews.com.cn/detail/1723716014168380.html)

Exact Chinese:

> “用剑气水墨风来呈现一个宏大的仙侠世界，是一种化繁为简的方式。”

English:

> “Presenting a grand xianxia world through an ink-wash sword-qi style is a way of simplifying complexity.”

The article also says:

> “采用了独特的水墨粒子画风”

English:

> “adopted a distinctive ink-wash particle visual style.”

So my previous statement that 《剑来》 consciously contrasts a reduced ink-sword language with more conventional visually complex spectacle is **verified in substance**. [Beijing News](https://www.bjnews.com.cn/detail/1723716014168380.html)

[Open the 新京报 article](https://www.bjnews.com.cn/detail/1723716014168380.html?utm_source=chatgpt.com)

---

#### 网易雷火—顾清寒特效原画

The article is 《以顾清寒的特效挂饰为例，谈谈特效原画师的自我修养》, by 己凹米 / 网易雷火艺术中心. The page displays “01-12”; I will **not infer a year from that display alone**. [GameRes游资网+1](https://www.gameres.com/916099.html)

Exact Chinese:

> “特效并不是无脑加一些发光的效果就可以。”

English:

> “VFX are not something you can make simply by mindlessly adding glowing effects.”

The article then explicitly discusses strong subject focus, clear climax hierarchy, rich layering, designed motion trajectories, color hierarchy, three-dimensionality, and avoiding large effects that block the view. [GameRes游资网+1](https://www.gameres.com/916099.html)

It also rejects the notion that stronger VFX simply mean larger, brighter and flashier effects. That supports the previous conclusion, but I am paraphrasing that point rather than adding another long quotation. [GameRes游资网](https://www.gameres.com/916099.html)

[Open the 网易雷火/GameRes article](https://www.gameres.com/916099.html?utm_source=chatgpt.com)

---

#### 《逆水寒》角色原画—GameRes

The article is 《特效不达预期？可能是你在原画阶段就没做好》, by 对子, identified as a 《逆水寒》 character concept artist, published 2024-05-30. [GameRes游资网](https://www.gameres.com/forum/t/906094)

Exact Chinese:

> “经过几何归纳的风、气流、刀光等元素会更加出效果。”

English:

> “Wind, airflow, slash-light and similar elements become more effective after geometric abstraction.”

The article also says an effect should preferably possess a contour, direction and some geometric form; it contrasts scattered fine particles with more organized ribbon-like forms. [GameRes游资网](https://www.gameres.com/forum/t/906094)

For fire, the same article describes a simple flame as multiple flame groups supplemented by a spark-particle group, establishing that even a relatively simple fire effect is considered layered rather than one glowing surface. [GameRes游资网](https://www.gameres.com/forum/t/906094)

[Open the 《逆水寒》 GameRes article](https://www.gameres.com/forum/t/906094?utm_source=chatgpt.com)

---

#### NEXT Studios—slash-light layering

The GameRes article is sourced from 腾讯游戏学院 and dated 2019-01-30. [GameRes游资网](https://www.gameres.com/836363.html)

The key original wording is:

> “较宽较暗的淡出时间稍长的底图…加上一个较细较明亮更快消失的刀光”

English:

> “a wider, darker base that fades more slowly … plus a thinner, brighter slash-light that disappears faster.”

The same passage explains why the bright layer should not remain too long: otherwise it loses the sharp/dangerous quality and interferes with later hit feedback. [GameRes游资网](https://www.gameres.com/836363.html)

This is the strongest direct Chinese support I found for your existing rule:

**dark under-layer + thin HDR core.**

[Open the NEXT/GameRes article](https://www.gameres.com/836363.html?utm_source=chatgpt.com)

---

#### 库洛 IGDC / 《战双帕弥什》

The article is 《库洛游戏首次公开分享：《战双帕弥什》的动作打击感是怎么做出来的》, published 2021-01-08 and based on technical director 林晨晨's IGDC presentation. [GameRes游资网](https://www.gameres.com/879272.html)

Exact Chinese:

> “我们的特效主要分为八个层次。”

English:

> “Our effects are mainly divided into eight layers.”

The article subsequently discusses attack/reaction animation, scene and character lighting, ordinary effects, radial blur, GPU particles, air distortion and scene-color changes; it says moving particle computation from CPU toward GPU enabled much larger particle quantities. [GameRes游资网](https://www.gameres.com/879272.html)

So my previous general lesson—**commercial spectacle is built from coordinated layers, not one magic glow shader**—is valid, but the article is about action-impact production generally, not flying swords specifically. [GameRes游资网](https://www.gameres.com/879272.html)

[Open the Kuro/GameRes article](https://www.gameres.com/879272.html?utm_source=chatgpt.com)

---

#### GameRes—light pollution warning

The 2020-04-17 article 《动作游戏打击感到底从何而来？（下）》 explicitly separates effects into stages such as casting, flight and hit. [GameRes游资网](https://www.gameres.com/865778.html)

Exact Chinese:

> “各种特效堆叠，光污染严重，反而忽略了动作本身。”

English:

> “Effects pile up until light pollution becomes severe, and the action itself is neglected instead.”

That supports using **different intensity at cruise, turn, commitment and impact** rather than keeping every sword permanently at maximum spectacle. The specific curves I recommend later are my inference, however. [GameRes游资网](https://www.gameres.com/865778.html)

[Open the GameRes article](https://www.gameres.com/865778.html?utm_source=chatgpt.com)

---

#### 《永劫无间》无尘 official update

The official 2024-07-31 notice for the August 2 update states:

> “在周身生成飞剑。”

English:

> “Generate flying swords around the body.”

For the reworked ultimate:

> “其连绵的剑雨拥有极强的压制力。”

English:

> “Its continuous sword rain has extremely strong suppressive power.”

The notice therefore verifies both a surrounding-sword identity and a sustained sword-rain gameplay role. It does **not** contain an artist breakdown of shader/material construction. [yjwujian.cn](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html)

[Open the official Naraka update](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html?utm_source=chatgpt.com)

---

### 3. Bilibili audit: every BV I cited previously

One caveat: direct automated opening of some Bilibili pages returned HTTP 412. I count metadata as verified only when Bilibili's indexed result itself exposed the title, uploader and timestamp; I am not pretending I watched unavailable frames.

| BV | Verified title | UP主 | Upload date | What the accessible page actually supports | Audit |
| --- | --- | --- | --- | --- | --- |
| **BV13b7a6sEas** | 《Unity特效教程.05 刀光基础制作(全流程)》 | 做个特笑吧 | 2026-06-25 | Its series index includes 刀光构成和节奏, model/texture/UV, 蓄力节奏 and 火焰元素表达. [Bilibili](https://www.bilibili.com/video/BV13b7a6sEas/) | **Verified** |
| **BV1xq536mETu** | 《〖unity特效〗刀光贴图解析》 | 阿瑞教你做特效 | 2026-05-13 | This exact video is specifically slash-light texture analysis. [Bilibili](https://www.bilibili.com/video/BV1xq536mETu/) | **Verified**, but I should not assign methods not visible in this individual video |
| **BV1XGQpY9ENV** | 《05-案例：剑气 \| UE5.5无痛入门教程 \| 特效篇 \| UE5&Niagara》 | 年糕爸爸历险记 | 2025-03-12 | A UE5/Niagara 剑气 case; description exposes resource/project links. [Bilibili](https://www.bilibili.com/video/BV1XGQpY9ENV/) | **Verified** |
| **BV1MVzNB4EF5** | 《Unity游戏特效教程_红色飞行剑》 | 石青刺客 | 2026-01-23 | Explicit flying-sword VFX tutorial; source-file link in description. [Bilibili](https://www.bilibili.com/video/BV1MVzNB4EF5/) | **Verified** |
| **BV1cAB8B7Ek1** | 《Unity游戏特效教程_剑影刀光》 | 石青刺客 | 2025-12-23 | Explicit 剑影/刀光 tutorial; source file referenced. [Bilibili](https://www.bilibili.com/video/BV1cAB8B7Ek1/) | **Verified** |
| **BV1Us411172g** | 《CGJOY 喜子 U3D（Unity3d）游戏特效教程》 | CGjoy动画特效课堂 | 2015-09-17 | 26-part series visibly includes 武器特效、刀光、箭雨、火焰气波、万剑术上下、水墨. [Bilibili](https://www.bilibili.com/video/BV1Us411172g/) | **Verified** |
| **BV1YjBtBfE7E** | 《凡人修仙韩老魔大庚剑阵特效解析…》 | 乐悠小椰子 | 2025-12-22 | Third-party UE5 “特效解析.” [Bilibili](https://www.bilibili.com/video/BV1YjBtBfE7E/) | **Verified title; previous “recreation/临摹” wording dropped** |
| **BV1JJ411T71T** | 《[UnrealCircle]Epic Asher \| Niagara制作实时特效的新思路》 | 虚幻引擎官方 | 2019-09-27 | Official UnrealCircle Niagara presentation; description links the PPT. [Bilibili](https://www.bilibili.com/video/BV1JJ411T71T/) | **Verified; not sword-specific** |
| **BV1Th411C7ex** | 《原神》角色演示-「魈：历劫祓恶」 | 原神官方账号 | 2021-02-02 | Official visual reference. [Bilibili+1](https://www.bilibili.com/video/BV1Th411C7ex/) | **Verified; not a VFX breakdown** |

Three additional Chinese practitioner/training sources survived the second search:

- **BV1Z54y1e77w**, 《万剑归宗_3DS MAX_PF粒子特效_完整版》, UP **YD特效达人**, 2020-09-02; description identifies Particle Flow and includes an analysis/tutorial portion. [Bilibili](https://www.bilibili.com/video/BV1Z54y1e77w/)
- **BV1cX4y137nB**, 《Niagara特效之万剑归宗教程已发布》, UP **麦田老湿**, 2021-04-11; explicitly a Niagara sword-array tutorial linked to an AboutCG course. [Bilibili](https://www.bilibili.com/video/BV1cX4y137nB)
- These sources prove that **flying-sword/sword-array effects are explicitly taught with Unity particles, UE Niagara and 3ds Max Particle Flow in Chinese VFX education/practice**. They do **not** prove that 《鸣潮》《原神》 or another commercial game uses precisely those implementations. [Bilibili+2](https://www.bilibili.com/video/BV1MVzNB4EF5/)

That distinction was not sharp enough in my first answer.

---

### 4. What Chinese players/creators actually say about flying swords

This second search improved the evidence, but it also shows why we should be cautious about claiming a universal Chinese-player consensus.

#### Qingxiao / 清宵

First, the factual base is solid: Kuro's official news index published Qingxiao's character profile on 2026-08-18 around the Version 3.6 release, and later official patch notes explicitly use the English state name **“Sword Flight.”** [Wuthering Waves+1](https://wutheringwaves.kurogames.com/main/news)

There are accessible Bilibili creator reactions specifically praising sword-flight/sword-array visuals:

**BV1fjbf6qEjE**  
《清宵与漂泊者双飞（御剑飞行）实机展示，太帅了！》  
UP: **番茄酱不知**  
Date: **2026-08-20**. [Bilibili](https://www.bilibili.com/video/BV1fjbf6qEjE/)

The title's actual judgment is:

> “御剑飞行…太帅了！”

English:

> “Sword flight… looks so cool!”

Another is **BV1JWNj68EGF**, 《〖鸣潮〗清宵登场！剑阵太帅了！》, UP **爱弥斯的猫-**, 2026-07-10. [Bilibili](https://www.bilibili.com/video/BV1JWNj68EGF/)

Exact phrase:

> “剑阵太帅了！”

English:

> “The sword array looks so cool!”

These are **individual uploader reactions**, not scientific evidence of player consensus.

I also found NGA search-result snippets containing criticism of flying swords moving so fast that their form becomes hard to perceive, but the actual NGA pages returned 403 when opened. Because you explicitly said **only cite what you can open**, I excluded those comments from the evidence set.

---

#### 无尘 / 剑雨

One accessible creator reaction is **BV1UW4JzQETW**, 《永劫无间：无尘的奥义特效展示，剑仙变牌皇》, UP **松子姐**, 2025-10-10. [Bilibili](https://www.bilibili.com/video/BV1UW4JzQETW/)

The short judgment:

> “剑仙变牌皇”

English:

> “The sword immortal turns into a card master.”

That is valuable not as consensus, but as a concrete warning: changing a sword-immortal's visual motif too far can make viewers feel the **fantasy identity itself has shifted**. That design lesson is **my inference from the reaction**, not something the uploader formally theorized.

---

#### 《剑来》 sword qi

A Bilibili dynamic/post by **神猪说动漫**, dated 2024-08-16, describes the opening with:

> “特效拉满，水墨风好绝”

English:

> “The effects are turned all the way up; the ink-wash style is fantastic.” [Bilibili](https://www.bilibili.com/opus/966118387506741266)

Again, this is one creator's reaction. The stronger evidence for the actual artistic intent remains the New Beijing News production article describing the water-ink sword-qi style and “化繁为简.” [Beijing News](https://www.bjnews.com.cn/detail/1723716014168380.html)

---

#### 《凡人修仙传》大庚剑阵

I found accessible Bilibili material around the 大庚剑阵, including **BV1F3aizeEE3**, 《〖凡人修仙传159集〗大庚剑阵真的就是在炫技!!!》, UP **桑心嗄**, 2025-09-06. [Bilibili](https://www.bilibili.com/video/BV1F3aizeEE3/)

But “炫技” can be admiration, criticism, or playful exaggeration depending on context. I therefore **will not classify it as either praise or complaint** from the title alone.

More useful for the general problem of “万剑” is a People's Daily-affiliated report about creator 范十三's physical ten-thousand-sword presentation. One audience criticism quoted in the report was:

> “所有的剑都像排队，没有灵动感。”

English:

> “All the swords look as if they're standing in a queue; there's no liveliness.”

The creator acknowledged the limitation of the suspended-sword approach. [People's Daily](https://sc.people.com.cn/n2/2025/0902/c345167-41340002.html)

Although that is a physical performance rather than a videogame, it is remarkably relevant to your problem: **large sword count is not impressive merely because there are many swords; uniformity can destroy the feeling of 御剑 / 万剑.**

---

#### 彦卿

I found official Yanqing material and ordinary reaction videos, but I did **not** find a directly accessible source cleanly saying something like “彦卿的飞剑特效高级 because X” or criticizing its specific flying-sword treatment.

So the corrected conclusion is:

**No reliable, directly open Yanqing-flying-sword aesthetic opinion was found in this pass.**

I would rather leave a hole than convert generic “this fight is cool” reactions into fake evidence about sword VFX.

---

### 5. One particularly valuable real Chinese “万剑归宗” production breakdown

The second search found something better than most game tutorials: a 2009 interview with 《风云Ⅱ》 VFX director **吴炫辉** discussing the production of “万剑归宗.”

The team used a particle system plus an internally developed control rig to manage the huge sword population. The interview specifically describes controlling different swords' individual speed, direction and sense of weight. [动画创作家园 - 专业的动画创作交流平台](https://chinavid.com/interview/2009-12-14/0912143300773_2.htm)

The useful exact fragment is:

> “各自的流通速度、方向、重量感等”

English:

> “their individual flow speed, direction, sense of weight, and so on.”

This is film VFX rather than realtime game VFX, but it is genuine Chinese production evidence for something extremely relevant:

> **The richness of 万剑 comes partly from controlled variation among individual swords, not merely duplicating one sword 100 times.**

The application to your 94-sword browser game is **my inference**, but it is much better grounded than “just add randomized particles.”

[Open the 《风云Ⅱ》 VFX interview](https://www.chinavid.com/2009/1214/100709.shtml)

---

### 6. Corrected answer: what actually creates “高级感” in flying swords

With the audit complete, I would reduce the Chinese evidence to five robust principles.

#### Principle 1 — Give qi a designed shape, not merely brightness

Three independent Chinese sources point in this direction:

《仙逆》 explicitly talks about moving from pure light effects toward shaped objects and environmental phenomena. [The Paper](https://www.thepaper.cn/newsDetail_forward_34200912)

《剑来》 describes its sword-qi ink language as **化繁为简**, and uses ink-particle styling rather than merely more saturated CG light. [Beijing News](https://www.bjnews.com.cn/detail/1723716014168380.html)

The 《逆水寒》 concept-art article explicitly recommends **几何归纳** for wind, airflow and slash-light. [GameRes游资网](https://www.gameres.com/forum/t/906094)

##### My inference for Clear Wind

Your present system:

**silver sword + hot white edge + soft rim + short trail**

contains good rendering ingredients but almost no **designed secondary silhouette**.

At 35–130 px it says:

**“sword with emissive treatment.”**

A more premium system should say:

**“Clear Wind sword, wrapped in a recognizable Clear-Wind qi geometry.”**

That is why direction A is fundamentally stronger than merely improving the glow shader.

---

### 7. Layer stack for a 35–130 px flying sword

The professional evidence supports layered construction and hierarchy, but the following exact screen-space allocation is **my design recommendation**, not an industry standard.

| Layer | 80–130 px | 50–79 px | 35–49 px | Role |
| --- | --- | --- | --- | --- |
| Real silver sword | Always | Always | Always as main axis | Identity |
| Dark qi silhouette/under-layer | Yes | Yes | Yes, simplified | Shape + contrast |
| Thin HDR seam/core | 1–2 seams | 1 seam | 1 hairline cue | Sharp energy |
| Tip needle/glint | Yes | Yes | Yes | Direction |
| Short wake | Yes | Yes | Yes | Velocity |
| Hollow blade afterimage | Turn/cut only | Usually max 1 | Usually none | Motion grammar |
| Jade-ring motif | Yes | Minimal | No | Premium identity |
| Silk streamer | Max 1–2 | Max 1 | No | Luxury/motion |
| Individual motes | Sparse | Hero swords only | No | Tertiary detail |
| Rune/formation graphics | Event only | Lead sword only | No | State/read |
| Distortion | Commit/hit | Commit/hit | No | Impact |
| Ground light/projection | Skill event | Skill event | Not tied to each sword | Environmental response |

The strongest direct production analogy is the NEXT structure of a **wider/darker/slower base** plus a **thinner/brighter/faster upper layer**. [GameRes游资网](https://www.gameres.com/836363.html)

That maps extremely well onto your rule:

**premultiplied dark under-layer → shaped qi body → hairline HDR seam.**

---

### 8. How the sword itself remains the hero

The Chinese sources repeatedly emphasize subject hierarchy and avoiding obstruction; Riot's formal clarity guidance similarly says visual noise accumulates quickly and important elements need a clear hierarchy. [GameRes游资网+1](https://www.gameres.com/916099.html)

So for Clear Wind:

##### The aura should not trace the complete sword silhouette.

A complete equal-width cyan border is still a generic outline, even if the shader is technically sophisticated.

##### Instead, leave deliberate absences.

For example:

- qi plate starts 5–10% after the tip;
- breaks beside the jade ring;
- leaves short gaps along the blade;
- one edge can temporarily carry more energy than the other;
- the dark layer can extend farther than the HDR seam.

Those percentages and placements are **my design proposal**.

The result is visually important: the eye gets enough uninterrupted silver to keep recognizing a **physical jian**, instead of seeing a luminous projectile with a sword hidden inside.

---

### 9. What “cheap glow / 光污染” evidence really says

The strongest Chinese professional statement is still 网易雷火:

> “特效并不是无脑加一些发光的效果就可以。”

“VFX are not made simply by mindlessly adding glow.” [GameRes游资网](https://www.gameres.com/916099.html)

《仙逆》 adds the production-side warning against large-area luminous formation clashes. [The Paper](https://www.thepaper.cn/newsDetail_forward_34200912)

The action-VFX GameRes article adds the readability side:

> “各种特效堆叠，光污染严重，反而忽略了动作本身。”

“When effects pile up into severe light pollution, the action itself gets neglected.” [GameRes游资网](https://www.gameres.com/865778.html)

And Chinese player feedback about other combat games demonstrates what happens when that hierarchy fails:

TapTap user **猫.酒.闲人**, 2026-10-27:

> “特效太花，组队打着打着就找不到人在哪了。”

English:

> “The effects are too busy; while playing co-op you lose track of where people are.” [TapTap](https://www.taptap.cn/review/50902885)

TapTap user **Asspe**, 2026-10-31:

> “特效太多，容易看不清自己人在哪里。”

English:

> “There are too many effects; it's easy to lose sight of your teammates.” [TapTap](https://www.taptap.cn/review/50965248)

A different TapTap user complained about warning colors being obscured by skill effects, but explicitly added:

> “但是又不想关闭特效影响爽感”

English:

> “But I also don't want to turn the effects off and hurt the spectacle.” [TapTap](https://www.taptap.cn/moment/843207845351524095)

That last comment is especially useful.

##### My inference

Players are not necessarily asking for **less spectacle**.

They are asking for:

**spectacle without losing information hierarchy.**

For a typing game, your word labels make that requirement even stricter than in a conventional action game.

---

### 10. Fire swords: flame around the sword, not incandescent steel

The directly sourced technical evidence is narrower than my previous answer implied.

The 《逆水寒》 article says even a simple fire effect can consist of several flame groups plus spark particles. [GameRes游资网](https://www.gameres.com/forum/t/906094)

Epic's realtime fire tutorial uses animated **SubUV/flipbook** flames and supports velocity alignment, while Niagara's Flipbook Baker can bake complex simulations into sprite sequences for cheaper playback. [Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642)

For the Epic fire material specifically, the documentation supports animated sprite sequencing and velocity-aligned presentation. The practical implication below is mine.

##### My proposed Clear Wind fire construction

Keep the actual silver blade substantially unchanged.

Then place four exterior layers:

**1. Dark flame skirt**  
Near-black/red-brown lobes outside the metal silhouette.

**2. Animated flame tongues**  
Unequal fire tongues born along the two exterior edges, using flipbook or procedural flow.

**3. Small hot cores**  
White/yellow HDR only at a few flame roots, never across the whole blade.

**4. Detached sparks/embers**  
Sparse and delayed behind the sword.

That visually says:

**“fire is consuming / wrapping the air around a silver sword.”**

A blade whose whole metal body gradients red → orange → white instead communicates **incandescent metal**. That semantic distinction is **my visual inference**, not a quoted Chinese production rule.

For flight direction, I would shear most tongues generally opposite the sword's relative motion but preserve some curling, detachment and local turbulence. I am intentionally dropping my previous **70–80%** number: it was an authoring heuristic, not something I sourced.

---

### 11. 50–100 swords: richness comes from hierarchy and differentiated motion

Three kinds of evidence now line up unusually well.

The old 《风云Ⅱ》 “万剑归宗” production used particle control to differentiate sword speed, direction and weight. [动画创作家园 - 专业的动画创作交流平台](https://chinavid.com/interview/2009-12-14/0912143300773_2.htm)

Audience criticism of a later physical “万剑” spectacle was precisely:

> “所有的剑都像排队，没有灵动感。”

“All the swords look like they're standing in a queue; there's no liveliness.” [People's Daily](https://sc.people.com.cn/n2/2025/0902/c345167-41340002.html)

On the engineering side, current Epic Niagara documentation explicitly warns that overlapping translucent sprites and meshes are a common source of overdraw, recommending fewer particles, less overlap and less screen coverage where possible. [dev.epicgames.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/measuring-performance-in-niagara?utm_source=chatgpt.com)

Three.js `InstancedMesh` is expressly intended for many objects sharing geometry/material but using different transforms, reducing draw calls. [archive.threejs.org](https://archive.threejs.org/docs/api/en/objects/InstancedMesh.html)

##### My recommendation for your exact 6 + 24 + 64 architecture

| Tier | Count | Visual treatment |
| --- | --- | --- |
| **Lead / hero swords** | 6 | Full real sword + dark mantle + bright seams + tip + short trail + turn echoes + rare jade/ceremonial detail |
| **Mid swords** | 24 | Real/LOD sword + one simplified mantle form + tip + short trail |
| **Mass followers** | 64 | Impostor/silhouette + dark exterior shape + one directional bright accent; no individual motes, rings or multiple echoes |

The key concept is:

> **Do not make 94 small hero effects. Make a six-sword aristocracy commanding an army.**

That sentence is my design interpretation.

---

#### Movement should also have hierarchy

Rather than:

**94 swords × independent noise**

I would compose them into phrases:

**scouts → main wave → gap → second wave → six finishers**

or:

**outer ring drifts → inner six tighten → entire array pauses → needles collapse inward → launch**

That structure is my design proposal, but it responds directly to the documented “all swords look like they're queueing” problem and to professional emphasis on VFX rhythm/hierarchy. [People's Daily+1](https://sc.people.com.cn/n2/2025/0902/c345167-41340002.html)

A useful rule is:

> **variation inside structure, not randomness instead of structure.**

---

### 12. Direction A — Wind-Silk Mantle

#### What Chinese practice supports

This is the best-supported of your three ideas.

The 《逆水寒》 article specifically favors geometric abstraction of wind/airflow/slash light and discusses how additional VFX geometry can reshape or reinforce a weapon's design emphasis. [GameRes游资网](https://www.gameres.com/forum/t/906094)

NEXT's broad-dark + thin-bright layered slash construction maps naturally onto an exterior qi mantle. [GameRes游资网](https://www.gameres.com/836363.html)

网易雷火's emphasis on theme, subject hierarchy, layering and designed motion also supports giving Clear Wind a signature form rather than a generic border. [GameRes游资网](https://www.gameres.com/916099.html)

##### Warning — my inference

If both sides become continuous, equally thick cyan strips, A degenerates into:

**generic glowing outline, except wider.**

##### Two improvements only

**1. Build each side from 2–3 unequal qi plates separated by negative-space cuts.**  
They sit close during cruise, offset on turns, and shear open during a cut.

**2. Make the rear “silk” a qi-memory of the handheld tassel, not an actual second tassel.**  
Borrow its color relationship but remove knot, tassel head and cloth construction.

##### Verdict

**Best permanent Clear Wind identity.**

---

### 13. Direction B — Echo Cascade

GameRes describes weapon/action trails as a way to make attack trajectory more obvious, while Riot explicitly says projectiles should communicate travel direction even in a still frame and notes tail treatment as one method. [League of Legends](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/)

Chinese VFX training also has dedicated 剑影/刀光 treatments, e.g. 石青刺客's **BV1cAB8B7Ek1**. [Bilibili](https://www.bilibili.com/video/BV1cAB8B7Ek1/)

##### Warning

The artistic problem is repetition; the technical problem is transparency overlap. Epic explicitly warns about overlapping translucent VFX and overdraw. [dev.epicgames.com](https://dev.epicgames.com/documentation/en-us/unreal-engine/measuring-performance-in-niagara?utm_source=chatgpt.com)

So:

**94 swords × four persistent echoes**

is the opposite of what I recommend.

##### Two improvements only

**1. Make echo count depend on screen size and meaningful angular change.**  
Straight flight: none or one. Strong turn: one or two. Strike: brief two or three. Most 64 impostors: zero.

**2. Make the V-shaped bow wave an event, not a costume.**  
Appear only during acceleration, turn-in or final commitment, then collapse within roughly a few frames.

The exact counts/timing are my proposal.

##### Verdict

**Excellent motion grammar; weaker as a permanent aura.**

---

### 14. Direction C — Celestial Regalia

There is solid general support for using specific cultural/character motifs rather than generic particles. HoYoverse's Xiao developer article explicitly discusses jade, light/dark symbolism and culturally meaningful visual design. [Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642)

网易雷火 similarly discusses building recognizable thematic motifs instead of superficial effect decoration. [GameRes游资网](https://www.gameres.com/916099.html)

##### Warning — my inference

Your C currently contains:

**tip star + halo + two streamers + motes + rim + real jade ring + real blade.**

On one 130 px sword, that can be luxurious.

On 94 swords, it becomes iconography noise.

The slow halo is particularly dangerous because Clear Wind already owns a **real hollow jade ring**. A luminous circle immediately behind it can destroy the very physical detail you're trying to celebrate.

##### Two improvements only

**1. Reserve Regalia for the six lead swords, formation anchors and ultimate states.**

**2. Replace the complete halo/star language with a broken jade-ring echo plus an axial needle glint.**

The ring echo should contain obvious missing sectors so the real guard still wins.

##### Verdict

**Strong ceremonial/rank language; poor choice as a universal 94-sword costume.**

---

### 15. The strongest final system is A + B + C, but with different jobs

This is my design conclusion, not a sourced industry formula.

##### A = identity

Every important Clear Wind sword gets **Wind-Silk Mantle**.

##### B = motion grammar

**Echo Cascade** appears only when something physically interesting happens:

turn, acceleration, convergence, cut.

##### C = rank/ceremony

**Celestial Regalia** tells the player:

this is a lead sword, formation anchor, charged state or ultimate.

That yields a much cleaner system than asking all three designs to compete as permanent alternatives.

A normal sword in cruise becomes:

**silver jian → broken dark qi mantle → one/two hairline seams → needle tip → restrained wake**

A hard turn becomes:

**outer mantle separates → one/two hollow echoes fan out → short bow wave**

A cut becomes:

**echoes collapse → seam peaks for 1–2 frames → mantle shears → hit effect takes over**

A formation leader becomes:

**broken jade echo awakens → axial tip glint → restrained silk streamers**

---

### 16. Screen-space rules I would actually build

These are explicitly **my production thresholds**, not sourced Chinese standards.

##### 35–49 px

Keep only:

**physical sword axis + dark mantle silhouette + one directional bright cue**

No individual motes, runes, halos or streamers.

##### 50–79 px

Add:

**broken seam detail + at most one turn echo**

Do not use an aura halo if the real jade ring is still perceptible.

##### 80–130 px

Enable:

**separate qi plates + ring-parting geometry + one streamer + sparse motes on lead swords**

##### Six lead swords

Allow selective C/Regalia elements.

The artistic principle behind these thresholds is:

> From farther away, Clear Wind should become more like calligraphy: **fewer marks, but each mark carries more meaning.**

That sentence is my design interpretation, but it is consistent with the Chinese sources' emphasis on geometric abstraction, hierarchy and 化繁为简. [GameRes游资网+1](https://www.gameres.com/forum/t/906094)

---

### 17. Chinese sources I now trust most

| Source | Author / uploader | Date | Why I trust/use it |
| --- | --- | --- | --- |
| [澎湃《仙逆》主创访谈](https://www.thepaper.cn/newsDetail_forward_34200912?utm_source=chatgpt.com) | Interview includes 美术导演 杜文凯 | 2026-10-06 | Direct production-team explanation of moving beyond pure light and avoiding large formation-light clashes. [The Paper](https://www.thepaper.cn/newsDetail_forward_34200912) |
| [新京报《剑来》动画开播](https://www.bjnews.com.cn/detail/1723716014168380.html?utm_source=chatgpt.com) | 杨莲洁 | 2024-08-15 | Explicit “剑气水墨 / 化繁为简 / 水墨粒子.” [Beijing News](https://www.bjnews.com.cn/detail/1723716014168380.html) |
| [网易雷火：顾清寒特效原画](https://www.gameres.com/916099.html?utm_source=chatgpt.com) | 己凹米 / 网易雷火艺术中心 | page displays 01-12 | Direct professional discussion of subject hierarchy, layers, trajectories, obstruction and “not mindlessly adding glow.” [GameRes游资网+1](https://www.gameres.com/916099.html) |
| [《逆水寒》原画：特效不达预期？](https://www.gameres.com/forum/t/906094?utm_source=chatgpt.com) | 对子 | 2024-05-30 | Geometric abstraction, effect geometry, layer construction and fire components. [GameRes游资网](https://www.gameres.com/forum/t/906094) |
| [NEXT Studios / 腾讯游戏学院](https://www.gameres.com/836363.html?utm_source=chatgpt.com) | NEXT / 腾讯游戏学院 | 2019-01-30 | Excellent concrete dark-wide-slow + bright-thin-fast slash layering rule. [GameRes游资网](https://www.gameres.com/836363.html) |
| [库洛《战双帕弥什》IGDC 技术分享](https://www.gameres.com/879272.html?utm_source=chatgpt.com) | 林晨晨 / Kuro | 2021-01-08 publication | Commercial action-game layering, GPU particles, distortion and presentation stack. [GameRes游资网](https://www.gameres.com/879272.html) |
| [《永劫无间》8月2日官方更新](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html?utm_source=chatgpt.com) | 24 Entertainment / official | 2024-07-31 | Direct official reference for 无尘 flying swords and sustained sword rain. [yjwujian.cn](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html) |
| [《风云Ⅱ》特效制作总监访谈](https://www.chinavid.com/2009/1214/100709.shtml) | 吴炫辉 interview | 2009-12-14 | Rare real Chinese production explanation of managing mass swords' speed, direction and weight. [动画创作家园 - 专业的动画创作交流平台](https://chinavid.com/interview/2009-12-14/0912143300773_2.htm) |
| Bilibili **BV13b7a6sEas** | 做个特笑吧 | 2026-06-25 | Current Chinese training covering slash composition/rhythm and related effect production. [Bilibili](https://www.bilibili.com/video/BV13b7a6sEas/) |
| Bilibili **BV1XGQpY9ENV** | 年糕爸爸历险记 | 2025-03-12 | Direct UE5/Niagara 剑气 case tutorial. [Bilibili](https://www.bilibili.com/video/BV1XGQpY9ENV/) |
| Bilibili **BV1Z54y1e77w** | YD特效达人 | 2020-09-02 | Particle Flow 万剑归宗 example with analysis/tutorial material. [Bilibili](https://www.bilibili.com/video/BV1Z54y1e77w/) |
| Bilibili **BV1cX4y137nB** | 麦田老湿 | 2021-04-11 | Explicit Niagara 万剑归宗 teaching material. [Bilibili](https://www.bilibili.com/video/BV1cX4y137nB) |

---

### 18. Claims I still cannot source responsibly

I still found **no official production breakdown** that tells us the actual shader/mesh/particle stack used for Qingxiao's flying swords in 《鸣潮》. Qingxiao and her Sword Flight state are verified; the rendering implementation is not. [Wuthering Waves+1](https://wutheringwaves.kurogames.com/main/news)

I found no directly accessible official VFX breakdown of Yanqing's flying swords or Jing Yuan's relevant effects in 《崩坏：星穹铁道》.

I found no original 《凡人修仙传》 studio technical breakdown for 大庚剑阵/青元剑诀 comparable to the 《仙逆》 production interview. The Bilibili UE5 material is third-party analysis. [Bilibili](https://www.bilibili.com/video/BV1YjBtBfE7E/)

I found no sufficiently strong directly open source set to claim that Chinese players **as a group** prefer “留白” or specifically hate glowing outlines on flying swords. I found individual reactions, broader combat-readability complaints, and professional-art guidance; those are different kinds of evidence.

NGA produced potentially useful search snippets about Qingxiao/flying-sword readability, but the pages themselves returned access errors. Per your instruction, I excluded the quotes.

I did not find a strong native-Chinese professional breakdown specifically explaining **how to make fire lick around a sword rather than heat the blade**. My fire solution combines sourced generic flame construction with my own visual-direction recommendation.

And the exact thresholds **35–49 / 50–79 / 80–130 px**, echo counts, A/B/C ratings, and movement choreography are my recommendations for your game, not externally sourced “Chinese industry standards.”

---

#### What I changed from the previous answer

I made six material changes:

1. **Corrected the 大庚剑阵 Bilibili description** from “fan recreation” to the defensible “third-party UE5 特效解析.”
2. **Downgraded the TapTap evidence** from flying-sword-player taste to general combat-VFX readability evidence.
3. **Removed the unverified Niagara ribbon-performance claim.**
4. **Added a genuine Chinese 万剑 production case** from 《风云Ⅱ》 showing individual sword speed/direction/weight control, plus the very relevant “像排队，没有灵动感” audience criticism. [动画创作家园 - 专业的动画创作交流平台+1](https://chinavid.com/interview/2009-12-14/0912143300773_2.htm)
5. **Added sword-specific Qingxiao, Wuchen and Jianlai reactions**, but labeled them correctly as individual uploader/creator opinions rather than consensus. [Bilibili+2](https://www.bilibili.com/video/BV1fjbf6qEjE/)
6. **Separated evidence from design inference much more aggressively.** The core recommendation survives: **A should be Clear Wind's identity, B its movement language, C its rank/ultimate language**—but that conclusion is mine, built from the audited evidence rather than something any one source says.

## D. ChatGPT, câu trả lời đầu, trước khi tự rà soát (nguyên văn)

可以。下面这版我把“**能直接查到的事实**”“**业内/教程做法**”“**玩家反馈**”和“**针对 Clear Wind 的推断**”严格分开。凡是我声称某个团队、教程或玩家真的说过/做过什么，我都在该段后放可点击来源；标成 **【我的推断】** 的部分，是我把这些证据映射到你这个 55°、35–130 px、最多 94 把剑的具体场景。

#### 先给结论

最重要的结论不是“给剑再套一圈更漂亮的 glow”，而是：

> **高级飞剑 = 本体剪影 + 有设计的外部形状语言 + 明暗层级 + 运动方向 + 短时爆点。**

中文资料对此异常一致。《剑来》公开宣传明确把“剑气水墨”描述为一种**化繁为简**：没有跟随“复杂颜色 + 高饱和打光”的方向，而是用水墨粒子把剑风、剑气做成有文化辨识度的形状。[bjnews.com.cn](https://www.bjnews.com.cn/detail/1723716014168380.html) [新京报：《剑来》动画开播，国风美学诠释中式哲思](https://www.bjnews.com.cn/detail/1723716014168380.html?utm_source=chatgpt.com)

《仙逆》美术导演杜文凯的说法更加直接：他们把技能从“单纯光效”升级为血藤、血浪、血棺等**有造型、有生命的东西**，把特效从抽象光效升级成空间/物理环境变化，并明确表示要“尽量避免大面积光效只用法阵对拼”。[The Paper](https://www.thepaper.cn/newsDetail_forward_34200912) [澎湃：《仙逆》主创访谈](https://www.thepaper.cn/newsDetail_forward_34200912?utm_source=chatgpt.com)

网易雷火的特效原画师总结得更接近你的问题：好特效不是“无脑加一些发光”，而要**主体明确、主次明确、层次丰富、运行轨迹有造型、颜色有主次、具有立体感**；他们还展示了因为树枝特效太粗会遮挡视线而把它减细的真实迭代。[GameRes游资网](https://www.gameres.com/916099.html) [GameRes / 网易雷火：以顾清寒的特效挂饰为例，谈特效原画](https://www.gameres.com/916099.html?utm_source=chatgpt.com)

这跟你的规则——**剑本体必须仍然是 hero，aura 只能 dress it**——基本完全一致。

---

### 1. 中国游戏/国漫里“高级感”的核心到底是什么？

##### 1.1 第一原则不是亮，而是“造型”

《逆水寒》角色原画分享指出，风、气流、刀光一类东西应该先做**几何归纳**，让它有轮廓、有方向、有明确几何形态；单纯细碎粒子往往不容易出效果。文章还直接拿《逆水寒》早期金粉效果举反例：未归纳的细碎粒子不强，把金沙归纳成条带后表现明显增强。[GameRes游资网](https://www.gameres.com/forum/t/906094) [GameRes：《特效不达预期？可能是你在原画阶段就没做好》](https://www.gameres.com/forum/t/906094?utm_source=chatgpt.com)

同一篇还指出，一个完整实时特效通常由多层组合；简单火焰本身就可以拆成若干火苗层 + 火星粒子，而武器附魔可以借助额外特效 mesh 改造外轮廓/设计重点，而不是只铺 glow。[GameRes游资网](https://www.gameres.com/forum/t/906094) [GameRes：特效分层、模型与贴图](https://www.gameres.com/forum/t/906094?utm_source=chatgpt.com)

**【我的推断】**  
所以对 Clear Wind 来说，你缺的并不是“现在的白边亮度不够”，而是：

**目前只有光学处理，没有第二套设计语言。**

现在的：

`silver sword + white edge + soft rim + short trail`

从 35–130 px 看就是：

`剑 + generic emissive treatment`

而高等级版本应该更像：

`剑 + Clear-Wind-specific qi geometry + motion behaviour`

这正是 A 比“普通白 glow”强很多的原因。

---

##### 1.2 暗层和亮层必须一起存在

米哈游关于魈的官方 Developer Insight 明确解释，他的攻击动画有 light/dark interplay：暗色代表战斗的破坏力量，而光碎片/光球代表仙人属性；设计团队还通过玉石、云纹等文化元素强化角色身份，而不是只靠亮度。[Genshin Impact+1](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com) [HoYoverse Developer Insight：Vigilant Yaksha Xiao](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com)

官方还明确说，魈 E 技能的 visual effect 被设计得像“一支直线穿过空气的箭”，说明**方向性本身就是 VFX 设计的一部分**，而不是运动代码完成后再贴一团光。[Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com) [HoYoverse：Xiao animation/VFX breakdown](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com)

**【我的推断】**  
这非常支持你已经规定的：

**dark premultiplied under-layer + thin HDR core**

而且我会更进一步：

> 不要把 dark layer 当“防 bloom 技术层”；把它当 aura 造型真正的外缘。

也就是先让玩家看到**深青/墨蓝的 qi plate / soot edge / shadow wake 的形状**，再让 1–2 px 的亮核告诉眼睛“这里很锋利”。

这样即使 bloom 被关闭，特效仍然应该好看。

---

##### 1.3 “高级”高度依赖节奏，而不是所有层一直开着

GameRes 的动作游戏分析把技能 VFX 分为 casting、flight、hit 等阶段，并明确说各阶段的轻重缓急都会影响打击表现；同一篇也直接警告“各种特效堆叠，光污染严重”会反过来盖掉动作本身。[GameRes游资网](https://www.gameres.com/865778.html) [GameRes：动作游戏打击感到底从何而来？](https://www.gameres.com/865778.html?utm_source=chatgpt.com)

库洛游戏技术总监林晨晨在 IGDC 分享《战双帕弥什》时，把打击演出拆成多层：动作/受击、场景灯、角色灯、普通特效、径向模糊、大量 GPU 粒子、空气扭曲、场景变色等；关键在于这些是**不同层级的反馈手段**，而不是全部塞进每一个普通攻击。[GameRes游资网](https://www.gameres.com/forum/t/879272) [GameRes：库洛《战双帕弥什》动作打击感技术分享](https://www.gameres.com/forum/t/879272?utm_source=chatgpt.com)

**【我的推断】**  
你的 flying state 应该是最安静的。

建议能量等级：

**Cruise 25% → turn 40% → commit 65% → cut/contact 100% → immediately collapse**

不要让一把剑从出生到消失都处于“SSR weapon preview”状态。

---

### 2. Bilibili 中文技术资料：我实际核验到什么？

下面这些不是“我从标题猜”；BV、UP、日期都能从 B 站索引页核验。

| 视频 | UP主 | BV | 上传日期 | 有用点 |
| --- | --- | --- | --- | --- |
| 《Unity特效教程.05 刀光基础制作(全流程)》 | 做个特笑吧 | **BV13b7a6sEas** | **2026-06-25** | 同系列专门拆“刀光的构成和节奏”“刀光模型/贴图/UV”“蓄力节奏”“火焰元素表达”。[Bilibili](https://www.bilibili.com/video/BV13b7a6sEas/?utm_source=chatgpt.com) [Bilibili 视频](https://www.bilibili.com/video/BV13b7a6sEas/?utm_source=chatgpt.com) |
| 《〖unity特效〗刀光贴图解析》 | 阿瑞教你做特效 | **BV1xq536mETu** | **2026-05-13** | 同系列还有火焰制作、空气扭曲 Shader、蓄力条带等，正好覆盖 sword aura 所需基础组件。[Bilibili](https://www.bilibili.com/video/BV1xq536mETu/?utm_source=chatgpt.com) [Bilibili 视频](https://www.bilibili.com/video/BV1xq536mETu/?utm_source=chatgpt.com) |
| 《05-案例：剑气 \| UE5.5无痛入门教程》 | 年糕爸爸历险记 | **BV1XGQpY9ENV** | **2025-03-12** | Niagara 剑气案例，有项目/材质资源链接。[Bilibili](https://www.bilibili.com/video/BV1XGQpY9ENV/?utm_source=chatgpt.com) [Bilibili 视频](https://www.bilibili.com/video/BV1XGQpY9ENV/?utm_source=chatgpt.com) |
| 《Unity游戏特效教程_红色飞行剑》 | 石青刺客 | **BV1MVzNB4EF5** | **2026-01-23** | 直接针对飞行剑特效。[Bilibili](https://www.bilibili.com/video/BV1MVzNB4EF5/?utm_source=chatgpt.com) [Bilibili 视频](https://www.bilibili.com/video/BV1MVzNB4EF5/?utm_source=chatgpt.com) |
| 《Unity游戏特效教程_剑影刀光》 | 石青刺客 | **BV1cAB8B7Ek1** | **2025-12-23** | 剑影 + 刀光方向的案例。[Bilibili](https://www.bilibili.com/video/BV1cAB8B7Ek1/?utm_source=chatgpt.com) [Bilibili 视频](https://www.bilibili.com/video/BV1cAB8B7Ek1/?utm_source=chatgpt.com) |
| 《CGJOY 喜子 U3D 游戏特效教程》 | CGjoy动画特效课堂 | **BV1Us411172g** | **2015-09-17** | 26 节中包含武器特效、刀光、箭雨、**万剑术上下**、水墨、火焰气波等。[Bilibili](https://www.bilibili.com/video/BV1Us411172g/?utm_source=chatgpt.com) [Bilibili 视频](https://www.bilibili.com/video/BV1Us411172g/?utm_source=chatgpt.com) |
| 《凡人修仙韩老魔大庚剑阵特效解析…UE5》 | 乐悠小椰子 | **BV1YjBtBfE7E** | **2025-12-22** | 直接针对《凡人修仙传》大庚剑阵的 UE5 临摹/拆解；**注意：这是个人复现，不是官方制作组 breakdown。** [Bilibili](https://www.bilibili.com/video/BV1YjBtBfE7E/?utm_source=chatgpt.com) [Bilibili 视频](https://www.bilibili.com/video/BV1YjBtBfE7E/?utm_source=chatgpt.com) |
| 《[UnrealCircle] Epic Asher \| Niagara制作实时特效的新思路》 | 虚幻引擎官方 | **BV1JJ411T71T** | **2019-09-27** | 官方 UnrealCircle / Niagara 实时特效技术分享。[Bilibili](https://www.bilibili.com/video/BV1JJ411T71T/?utm_source=chatgpt.com) [Bilibili 视频](https://www.bilibili.com/video/BV1JJ411T71T/?utm_source=chatgpt.com) |

另外，《原神》魈的官方角色演示 B 站 BV 为 **BV1Th411C7ex**，日期是 2021-02-02，官方账号为“原神”；我把它当 visual reference，而真正用于分析设计意图的是上面的 HoYoverse Developer Insight。[Gamer Forum](https://forum.gamer.com.tw/Co.php?bsn=36730&sn=56469&utm_source=chatgpt.com) [Bilibili：魈「历劫祓恶」](https://www.bilibili.com/video/BV1Th411C7ex/?utm_source=chatgpt.com)

**这里有个重要限制：**上面绝大多数 B 站教程告诉我们“国内实时特效师会使用哪些构件和工作流”，但不能拿它们证明《原神》《鸣潮》《凡人修仙传》的官方团队具体就是这样制作的。后者我只在有官方/制作组资料时才这样表述。

---

### 3. Flying sword 应该堆哪些层？

一个非常有价值的中文制作经验来自 NEXT Studios 的动作游戏分享：刀光建议至少有**宽、暗、消失较慢的底层**来传达范围，再叠**细、亮、消失更快的锋利上层**；明亮层不能持续太久，否则会盖住其他反馈。[GameRes游资网](https://www.gameres.com/836363.html?utm_source=chatgpt.com) [GameRes：NEXT 工作室动作游戏特效拆解](https://www.gameres.com/836363.html?utm_source=chatgpt.com)

这几乎就是你规定的 dark under-layer + thin HDR core 的行业对应物。

##### 针对 35–130 px，我会这样分级

| Layer | 130 px | 70 px | 35 px | 判断 |
| --- | --- | --- | --- | --- |
| **真实剑本体** | 必须 | 必须 | 必须形成主轴 | 第一识别物 |
| **暗色 aura silhouette / 剑罡底层** | ✓ | ✓ | ✓ 极简 | 非常重要 |
| **细 HDR 刃光 / seam** | ✓ | ✓ | 1 条即可 | 非常重要 |
| **tip needle / 剑尖星芒** | ✓ | ✓ | ✓ | 给方向感 |
| **短拖影 / residual wake** | ✓ | ✓ | ✓ | 给速度感 |
| **blade-only afterimage** | 1–3 | 1 | 条件触发 | 转向/斩击很好 |
| **guard / jade motif** | ✓ | 极简 | × | 近处 luxury |
| **飘带** | ✓ | 1 条 | × | 容易乱 |
| **motes / sparks** | 稀疏 | lead only | × | tertiary |
| **rune / 法阵** | 特殊状态 | lead only | × | 不能常驻 |
| **distortion** | strike only | strike only | × | 非轮廓层 |
| **ground projection** | event layer | event layer | × | 不属于剑自身 |

Riot 的 clarity 规则与此高度一致：silhouette 是角色识别最重要的视觉信息；VFX 要有 hierarchy；视觉噪音会快速累积；projectile 即使静止截图也应该传达运动方向，官方举出的常见手段就是把尾端做模糊/拖尾。[League of Legends+1](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/) [Riot：Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/?utm_source=chatgpt.com)

Riot 的 VFX 更新团队还明确把 **readability、降低 fine-detail visual noise、避免技能过亮**列为正式目标。[League of Legends+1](https://www.leagueoflegends.com/en-us/news/dev/dev-behind-the-scenes-of-vfx-updates/?linkId=100000122221585) [Riot：Behind the Scenes of VFX Updates](https://www.leagueoflegends.com/en-us/news/dev/dev-behind-the-scenes-of-vfx-updates/?utm_source=chatgpt.com)

##### 【我的推断】Clear Wind 的优先顺序

在你的镜头上，我认为视觉预算应该固定为：

**1. sword axis / blade → 2. tip → 3. exterior qi shape → 4. motion wake → 5. decorative identity**

而不是：

**halo → particles → glow → rune → sword somewhere inside.**

尤其在 35 px 时，玩家需要读到的是：

> **“一把极细的剑，正朝这个方向飞。”**

而不是：

> “一个 cyan particle projectile。”

---

### 4. 怎么避免“廉价描边发光 / 光污染”？

中文专业资料其实说得非常直接。

网易雷火说好的特效必须有“主体性”“爆点主次”“层次丰富”，并明确写了“特效并不是无脑加一些发光的效果就可以”。[GameRes游资网](https://www.gameres.com/916099.html) [网易雷火/GameRes 原文](https://www.gameres.com/916099.html?utm_source=chatgpt.com)

《逆水寒》相关制作分享则强调：没有几何归纳、只有细碎粒子的效果容易散；需要通过造型、贴图、层次重建视觉重点。[GameRes游资网](https://www.gameres.com/forum/t/906094) [GameRes：《特效不达预期？》](https://www.gameres.com/forum/t/906094?utm_source=chatgpt.com)

《剑来》的“剑气水墨”也是同一个方向：它把“中国风”放在介质、边缘、颗粒和运动语言里，而不是给普通 CG 光效换成青色。[bjnews.com.cn](https://www.bjnews.com.cn/detail/1723716014168380.html) [新京报：《剑来》剑气水墨](https://www.bjnews.com.cn/detail/1723716014168380.html?utm_source=chatgpt.com)

---

#### 玩家实际在骂什么？

这里比“业内理论”更有说服力。

TapTap 上《失落城堡2》玩家直接写：

> “特效太花，组队打着打着就找不到人在哪了……二阶段都找不到boss。”

[TapTap](https://www.taptap.cn/review/50902885) [TapTap 原评论，2026-10-27](https://www.taptap.cn/review/50902885?utm_source=chatgpt.com)

另一名玩家写后期 Boss 战“特效太多，容易看不清自己人在哪里”，联机时装特效则“特别花里胡哨，根本看不清自己人在哪，甚至敌人在哪都不晓得”。[TapTap](https://www.taptap.cn/review/50965248) [TapTap 原评论](https://www.taptap.cn/review/50965248?utm_source=chatgpt.com)

《幻想九霄》玩家玩了 200 多小时后提出：

> “能不能把特效改改，出个特效透明模式什么的，眼睛都要晃瞎了。”

[TapTap](https://www.taptap.cn/moment/845609340168569997) [TapTap：《光污染太严重了》](https://www.taptap.cn/moment/845609340168569997?utm_source=chatgpt.com)

更值得注意的是另一条反馈：玩家说技能特效和预警颜色重复导致看不清，但他又**“不想关闭特效影响爽感”**，希望能自定义预警颜色。[TapTap](https://www.taptap.cn/moment/843207845351524095) [TapTap：特效和预警提示颜色重复](https://www.taptap.cn/moment/843207845351524095?utm_source=chatgpt.com)

正面的反例也存在。《极简塔防》的玩家明确赞扬“没有花里胡哨特效”“干净清爽”“不容易视觉疲劳”。[TapTap](https://www.taptap.cn/app/431173/review) [TapTap：《极简塔防》评价](https://www.taptap.cn/app/431173/review?utm_source=chatgpt.com)

##### 【我的推断】

玩家实际上不是在说：

> “我讨厌华丽特效。”

他们说的是：

> **“我愿意要爽，但别让我失去信息层级。”**

所以 Clear Wind 的 aura 可以很贵、很华丽，但 richness 应来自：

- shape;
- timing;
- material contrast;
- negative space;
- uniquely recognisable motion;

而不是来自**屏幕覆盖面积**。

---

### 5. Fire Sword：怎样做“火焰舔着剑”，而不是“烧红的铁”？

中文实时特效教程本身把“火焰元素表达”当作独立课题；例如“做个特笑吧”的 Unity 系列有 25:48 的《火焰元素的特效表达》，阿瑞的课程也有独立 42:34 火焰制作章节。[Bilibili+1](https://www.bilibili.com/video/BV13b7a6sEas/?utm_source=chatgpt.com) [Unity 刀光/火焰系列](https://www.bilibili.com/video/BV13b7a6sEas/?utm_source=chatgpt.com)

Epic 官方实时火焰教程使用 animated SubUV/flipbook sprite，并让 sprite **velocity-aligned**，说明实时游戏中让火苗本身拥有时间变化与方向性，而不是简单给实体表面改成红色，是标准可行路径。[Epic Games Developers](https://dev.epicgames.com/documentation/en-us/unreal-engine/at12-adding-visual-effects-to-your-game?utm_source=chatgpt.com) [Epic：Create a Fire Effect / SubUV](https://dev.epicgames.com/documentation/en-us/unreal-engine/at12-adding-visual-effects-to-your-game?utm_source=chatgpt.com)

Epic 的 Niagara Flipbook Baker 也明确支持把模拟/动画结果 bake 为 sprite flipbook 再由 Sprite Renderer 播放。[Epic Games Developers](https://dev.epicgames.com/documentation/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?lang=en-US&utm_source=chatgpt.com) [Epic：Niagara Flipbook Baker](https://dev.epicgames.com/documentation/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine?utm_source=chatgpt.com)

##### 【我的推断】正确的 Fire Clear Wind

**绝对不要：**

`silver blade → orange → red → white centre`

这会读成：

**metal is incandescent.**

应该是：

```
       separate flame tongues
       /\      /\
------/--\----/--\-------   ← silver blade remains visibly silver
    dark-red / soot skirt
   orange body
 tiny white-yellow flame cores
```

我会给它四层：

1. **Silver blade unchanged**  
  银剑本体绝不大面积乘红/橙。
2. **Dark flame-body underlayer**  
  深红褐/近黑 scalloped flame mass，主要待在 blade silhouette **之外**。
3. **Animated tongues**  
  两侧 3–5 个不对称火舌，用 flipbook/flow UV；不断出生、断裂、再贴回剑边。
4. **Tiny high-temperature cores**  
  只在少数火舌根部有短白黄 HDR 核；你的 bloom 规则仍成立。

##### 火舌方向

**【我的推断】**匀速高速飞行时，绝大多数火舌应该被 relative airflow 往**运动反方向**拉；但如果所有火舌都变成完全平行 backward streak，它就会重新退化成“普通火焰拖尾”。

所以建议：

- 70–80% backward shear；
- 20–30% local curling / lifting / separation；
- 转弯外侧火焰被甩长；
- 切击瞬间火焰突然向 blade normal 裂开。

这样看起来才是：

**fire attached to the sword**

而不是：

**a rocket trail behind the sword**。

这一具体比例是我的设计判断，不是我查到的中国行业标准。

---

### 6. 50–100 把剑怎么既富、又不糊、还便宜？

先说工程侧事实。Three.js 官方 `InstancedMesh` 就是为“同 geometry/material、大量不同 transform”的对象设计，并明确说明其作用是减少 draw calls。[archive.threejs.org](https://archive.threejs.org/docs/api/en/objects/InstancedMesh.html?utm_source=chatgpt.com) [Three.js InstancedMesh documentation](https://archive.threejs.org/docs/api/en/objects/InstancedMesh.html?utm_source=chatgpt.com)

Epic 的当前 Niagara 性能文档强调，大量相互覆盖的 translucent sprites/meshes 很容易造成 overdraw；减少粒子数量、减少重叠、减少屏幕占用、按 scalability 缩 spawn count 都是官方建议。[Epic Games Developers+1](https://dev.epicgames.com/documentation/en-us/unreal-engine/measuring-performance-in-niagara?utm_source=chatgpt.com) [Epic：Measuring Performance in Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/measuring-performance-in-niagara?utm_source=chatgpt.com)

Epic 还特别指出 Ribbon Renderer 相对昂贵，可以通过关闭不必要 tessellation、distance culling、cutout texture 等方式控制开销。[Epic Games Developers](https://dev.epicgames.com/community/learning/courses/qXe/unreal-engine-niagara-examples-pack/L7aY/unreal-engine-niagara-example-pack-best-practices?locale=ru-ru&utm_source=chatgpt.com) [Epic Niagara Best Practices](https://dev.epicgames.com/community/learning/courses/qXe/unreal-engine-niagara-examples-pack/L7aY/unreal-engine-niagara-example-pack-best-practices?utm_source=chatgpt.com)

中国侧，库洛早在《战双》公开技术分享里就明确提到把粒子计算从 CPU 移到 GPU，以达到过去做不到的粒子规模。[GameRes游资网](https://www.gameres.com/forum/t/879272) [库洛技术分享](https://www.gameres.com/forum/t/879272?utm_source=chatgpt.com)

《永劫无间》无尘的官方重做则很有“万剑编排”参考价值：2024 重做加入周身飞剑与持续降落的剑雨；开发者把剑雨定位为持续压制手段。[yjwujian.cn](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html) [《永劫无间》2024-08-02 官方更新公告](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html?utm_source=chatgpt.com)

##### 【我的推断】你的 6 + 24 + 64 分级其实非常适合做“视觉等级制”

不要让 94 把剑都有同一套 full aura。

我建议：

| Tier | 数量 | Aura budget |
| --- | --- | --- |
| **Hero / lead** | 6 | sword + dark mantle + bright seams + tip + trail + occasional ring motif/motes |
| **Mid LOD** | 24 | sword + single mantle shape + tip + short trail |
| **Mass followers** | 64 | sword/impostor silhouette + one dark shape + one bright directional accent |

关键不是让后 64 把“低质量”。

而是让观众自动理解：

**6 把是将领，88 把是军势。**

---

#### 万剑真正需要的是“节奏簇”，不是 94 个随机个体

**【我的推断】**

不要：

`94 swords × independent random noise × independent particles`

而要：

`6 visual phrases × 10–18 swords`

例如剑雨：

**front scouts → dense main curtain → breathing gap → second curtain → 6 hero finishers**

剑阵：

**outer ring quiet → inner six brighten → radial collapse → needle launch**

这样你减少了同时处于 peak brightness 的剑数量，却会让整体显得**更大**，因为出现了“起承转合”。

这也吻合 Riot 的 hierarchy 原则：重要事件应该获得更高视觉注意力，不能所有东西都同时 “11/10”。[League of Legends](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/) [Riot Clarity principles](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/?utm_source=chatgpt.com)

---

### 7. Qingxiao / 清宵：先纠正一个可能的资料坑

这次我特地重新核了。

**Qingxiao / 清宵确实是《鸣潮》角色，不是网上误传角色。**《鸣潮》官方新闻索引在 **2026-08-18** 发布“档案公开｜天地弦心剑——清宵”，3.6 版于 **2026-08-20** 更新，并将清宵列为新角色。[Wuthering Waves+1](https://wutheringwaves.kurogames.com/zh-tw/main/news/detail/5289?utm_source=chatgpt.com) [鸣潮官方 3.6 版本资讯](https://wutheringwaves.kurogames.com/zh-tw/main/news/detail/5289?utm_source=chatgpt.com)

官方 3.7 Patch Notes 还明确使用了 Qingxiao 的 **“Sword Flight” state** 一词。[Wuthering Waves](https://wutheringwaves.kurogames.com/en/main/news/detail/5571?utm_source=chatgpt.com) [Wuthering Waves official 3.7 patch notes](https://wutheringwaves.kurogames.com/en/main/news/detail/5571?utm_source=chatgpt.com)

但：

**我没有找到库洛官方公开的“清宵飞剑 VFX 分层制作 breakdown”。**

所以任何“清宵用了某种具体 shader / 某三层 sword aura”的说法，我都不会冒充官方事实。

---

### 8. 对三个方案的逐项判断

#### A. Wind-Silk Mantle

##### 中国实践支持什么？

最支持 A。

它把 aura 本身做成**有轮廓、有方向的几何造型**，符合《逆水寒》制作分享强调的 geometrical abstraction；同时又保留真实剑体，而不是把它包成发光棒。[GameRes游资网](https://www.gameres.com/forum/t/906094) [GameRes：《逆水寒》特效设计经验](https://www.gameres.com/forum/t/906094?utm_source=chatgpt.com)

“围绕主题做独特视觉 motif、保留原本辨识度再提高价值感”也正是网易雷火顾清寒案例明确描述的设计路径。[GameRes游资网](https://www.gameres.com/916099.html) [网易雷火特效原画案例](https://www.gameres.com/916099.html?utm_source=chatgpt.com)

##### 警告

**【我的推断】**最大风险是 qi plate 最后被美术做成：

`constant-width symmetric cyan casing`

那它就重新变成“描边 glow，只不过比较厚”。

##### 我只改两点

**1. 每边不要连续包边，而是 2–3 片 unequal qi plates，中间必须留负空间。**  
飞行时贴身；转向时外侧先错位；斩击时像剪开丝绸一样 shear。

**2. 尾部“silk”一定要读成 qi，不要读成一条真实第二流苏。**  
用跟手持剑 tassel 相同的色彩记忆，但不要结、穗头或实体布料结构。

##### 我的评分

**9/10，应该作为 Clear Wind 的 permanent identity layer。**

---

### 9. B. Echo Cascade

##### 实践支持什么？

残影/拖尾本身非常成熟。GameRes 把 weapon/action trail 明确归类为能强化攻击轨迹的信息层；Riot 则明确建议 projectile 可以通过 tail treatment 让静态轮廓也表现运动方向。[GameRes游资网+1](https://www.gameres.com/889570.html?utm_source=chatgpt.com) [GameRes：动作游戏提高打击感](https://www.gameres.com/889570.html?utm_source=chatgpt.com) [Riot：Projectile direction/readability](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/?utm_source=chatgpt.com)

石青刺客的中文案例库也同时存在“剑影刀光”与“飞行剑”案例，说明这种组合在中文实时特效工作流中完全正常。[Bilibili+1](https://www.bilibili.com/video/BV1MVzNB4EF5/?utm_source=chatgpt.com) [Bilibili：剑影刀光](https://www.bilibili.com/video/BV1cAB8B7Ek1/?utm_source=chatgpt.com)

##### 警告

你的问题不是单剑。

如果：

**94 swords × 4 echoes = 376 translucent sword cards**

视觉和 fill-rate 都会开始恶化；Epic 明确提醒重叠透明层会快速造成 overdraw。[Epic Games Developers](https://dev.epicgames.com/documentation/unreal-engine/measuring-performance-in-niagara?lang=en-US) [Epic Niagara overdraw guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/measuring-performance-in-niagara?utm_source=chatgpt.com)

##### 我只改两点

**1. Echo count 必须由 screen-space + angular velocity 驱动。**

我的建议：

- straight flight：0–1；
- meaningful turn：2；
- strike：2–3；
- 64 impostors：绝大多数 0。

**2. V bow wave 不常驻。**  
只在 accelerate / commit / turn-in 时出现 80–150 ms，然后收掉；V 的尖端必须和实际 sword tip 重合。

##### 我的评分

**8.5/10 作为 motion system；6.5/10 如果把它当 permanent aura。**

---

### 10. C. Celestial Regalia

##### 实践支持什么？

文化/主题 motif 的确能提高“价值感”。魈官方设计通过 jade、cloud motif 和 light/dark symbolism 把超自然力量和角色身份绑在一起。[Genshin Impact](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com) [HoYoverse Xiao Developer Insight](https://genshin.hoyoverse.com/en/news/detail/8642?utm_source=chatgpt.com)

网易雷火案例也通过寒梅、水墨枝、特定色彩而不是 generic particles 来做主题区别。[GameRes游资网](https://www.gameres.com/916099.html) [网易雷火：顾清寒 VFX concept](https://www.gameres.com/916099.html?utm_source=chatgpt.com)

##### 但是 C 风险最大

**【我的推断】**

你现在同时有：

- four-point star；
- halo；
- twin streamers；
- motes；
- rim；
- real sword；
- jade ring。

单把 130 px 能漂亮。

94 把一起就是：

**94 个“五星武器抽卡预览 UI”。**

而且那个 halo 很容易把最有辨识度的**真实 hollow jade ring**反而变成一团圆光。

##### 我只改两点

**1. Celestial Regalia 只给 6 lead swords / ultimate / formation captain。**  
24 LOD 最多保留一个 broken jade halo；64 个完全取消。

**2. 四角星改成与剑轴绑定的 needle glint，而不是稳定十字 icon。**  
halo 也不要完整圆，应是带缺口的“jade-ring echo”，中间必须透明。

##### 我的评分

**7/10 常驻；9/10 作为 rare ceremonial state。**

---

### 11. 我最终会怎么组合三个方案

**【我的设计结论】**

不是 A、B、C 三选一。

我会做：

#### **A = 身份**

Wind-Silk Mantle 是 Clear Wind 每次飞出来都拥有的 signature。

#### **B = 动作语法**

Echo Cascade 只在 turn / acceleration / cut 时展开。

#### **C = 等级语法**

Celestial Regalia 只出现在：

- 6 lead swords；
- sword-array anchors；
- ultimate；
- exceptionally charged sword。

所以正常飞行：

> **real silver jian → broken dark qi mantle → two hairline seams → needle tip → tiny silk wake**

高速转弯：

> **mantle outside edge shears → 2 hollow echoes fan → tip bow-wave appears**

命中：

> **echo snaps together → seam goes white-hot for 1–2 frames → mantle cuts apart → impact layer takes over**

大阵主剑：

> **broken jade halo wakes → restrained glint → two qi streamers**

这会比三个方向任选其一成熟得多。

---

### 12. 一个特别适合你项目的 screen-space rule

下面完全是 **【我的推断 / implementation proposal】**，不是外部资料里的标准数字。

##### 35–49 px

只允许三件东西：

**blade axis + dark mantle silhouette + tip/wake directional cue**

没有 motes，没有 rune，没有 halo，没有双飘带。

##### 50–79 px

加：

**broken seams + one echo on turns**

jade ring 本身如果还能采样出 2–3 px，就不要用 halo 抢它。

##### 80–130 px

才打开：

**individual qi plates + jade-ring parting + one streamer + optional motes**

##### Hero lead

再允许 C 的 ceremonial layer。

这套设计的核心不是“低 LOD 特效变差”，而是：

> **距离越远，视觉语言越接近书法——少笔，但每一笔都更重要。**

这恰恰比把 full effect 缩小 4 倍更像中国仙侠。

---

### 13. 我最信任的 11 个中文来源

| 来源 | 作者/UP | 日期 | 我信它的原因 / 它实际告诉我们什么 |
| --- | --- | --- | --- |
| [《仙逆》主创访谈](https://www.thepaper.cn/newsDetail_forward_34200912?utm_source=chatgpt.com) | 导演王建鑫、美术导演杜文凯访谈；澎湃刊发 | 2026-10-06 | **最重要。** 制作组直接说功法从单纯光效→具体造型/环境变化，并避免大面积法阵光效对拼。[The Paper](https://www.thepaper.cn/newsDetail_forward_34200912) |
| [《剑来》动画开播，国风美学诠释中式哲思](https://www.bjnews.com.cn/detail/1723716014168380.html?utm_source=chatgpt.com) | 新京报记者 杨莲洁 | 2024-08-15 | 剑气水墨、化繁为简、水墨粒子，与“高饱和复杂打光”形成明确对照。[bjnews.com.cn](https://www.bjnews.com.cn/detail/1723716014168380.html) |
| [网易雷火：顾清寒特效原画](https://www.gameres.com/916099.html?utm_source=chatgpt.com) | 己凹米 / 网易雷火艺术中心 | 页面标 01-12 | 主体性、主次、层次、运行轨迹、辨识度、遮挡控制、主题 motif。[GameRes游资网](https://www.gameres.com/916099.html) |
| [《逆水寒》原画：特效不达预期？](https://www.gameres.com/forum/t/906094?utm_source=chatgpt.com) | 对子，《逆水寒》角色原画 | 2024-05-30 | 几何归纳、模型+贴图、分层、火苗+火星；细碎粒子不如有造型的条带。[GameRes游资网](https://www.gameres.com/forum/t/906094) |
| [库洛：《战双》动作打击感技术分享](https://www.gameres.com/forum/t/879272?utm_source=chatgpt.com) | 库洛技术总监 林晨晨 / IGDC 分享整理 | 2021-01-08 | 多层演出、GPU particles、distortion 等真实生产思路。[GameRes游资网+1](https://www.gameres.com/forum/t/879272) |
| [GameRes：动作游戏打击感下篇](https://www.gameres.com/865778.html?utm_source=chatgpt.com) | nagatsuki | 2020-04-17 | VFX 有 casting/flight/hit rhythm；明确警告堆特效、光污染会压过动作。[GameRes游资网](https://www.gameres.com/865778.html) |
| [《永劫无间》无尘重做官方公告](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html?utm_source=chatgpt.com) | 24 Entertainment / 网易官方 | 2024-07-31 | 周身飞剑、连续剑雨、剑雨作为压制手段，是可靠的官方“御剑/剑雨”设计参考。[yjwujian.cn](https://www.yjwujian.cn/news/update/20240731/33456_1171206.html) |
| [Bilibili：Unity 刀光基础制作](https://www.bilibili.com/video/BV13b7a6sEas/?utm_source=chatgpt.com) | 做个特笑吧 | 2026-06-25 | BV13b7a6sEas；课程显式拆刀光构成/节奏/贴图/UV/火焰表达。[Bilibili](https://www.bilibili.com/video/BV13b7a6sEas/?utm_source=chatgpt.com) |
| [Bilibili：刀光贴图解析](https://www.bilibili.com/video/BV1xq536mETu/?utm_source=chatgpt.com) | 阿瑞教你做特效 | 2026-05-13 | BV1xq536mETu；同系列覆盖刀光、火焰、空气扭曲、条带等。[Bilibili](https://www.bilibili.com/video/BV1xq536mETu/?utm_source=chatgpt.com) |
| [Bilibili：CGJOY Unity 游戏特效教程](https://www.bilibili.com/video/BV1Us411172g/?utm_source=chatgpt.com) | CGjoy动画特效课堂 | 2015-09-17 | BV1Us411172g；虽然旧，但直接有武器、刀光、箭雨、万剑术上下、水墨等完整传统中文 VFX curriculum。[Bilibili](https://www.bilibili.com/video/BV1Us411172g/?utm_source=chatgpt.com) |
| [Bilibili：凡人大庚剑阵 UE5 解析/复现](https://www.bilibili.com/video/BV1YjBtBfE7E/?utm_source=chatgpt.com) | 乐悠小椰子 | 2025-12-22 | BV1YjBtBfE7E；对万剑场景很有参考价值，但必须记住它是 fan reproduction，不是《凡人》制作组官方 breakdown。[Bilibili](https://www.bilibili.com/video/BV1YjBtBfE7E/?utm_source=chatgpt.com) |

---

### 14. 英文资料给中文结论做了哪些交叉验证？

英文资料没有推翻上面的中国经验，反而把它技术化了。

Riot 的正式 VFX philosophy 明确要求：**readability > extra decoration；降低 unnecessary fine detail；技能不能过亮；视觉注意力必须有 hierarchy。** [League of Legends+1](https://www.leagueoflegends.com/en-us/news/dev/dev-behind-the-scenes-of-vfx-updates/?linkId=100000122221585) [Riot VFX Updates](https://www.leagueoflegends.com/en-us/news/dev/dev-behind-the-scenes-of-vfx-updates/?utm_source=chatgpt.com)

他们甚至在 fantasy weapon icon 的讨论里说，需要通过 rendering pass 让武器少一点“plastic”、更像 powerful fantasy weapon；这说明所谓“塑料感”并不是单靠增加 bloom 能解决，而涉及材质和视觉组织。[League of Legends](https://www.leagueoflegends.com/en-us/news/dev/quick-gameplay-thoughts-nov-20/) [Riot：Quick Gameplay Thoughts – Item Rendering](https://www.leagueoflegends.com/en-us/news/dev/quick-gameplay-thoughts-nov-20/?utm_source=chatgpt.com)

Epic 则从工程侧确认：透明层越多、重叠越多，overdraw 越危险；distance culling、particle-count scaling、cutout、减少 ribbon 成本都应该成为大型群体 VFX 的基本预算手段。[Epic Games Developers+1](https://dev.epicgames.com/community/learning/courses/qXe/unreal-engine-niagara-examples-pack/L7aY/unreal-engine-niagara-example-pack-best-practices?locale=ru-ru&utm_source=chatgpt.com) [Epic Niagara Performance](https://dev.epicgames.com/documentation/en-us/unreal-engine/measuring-performance-in-niagara?utm_source=chatgpt.com)

---

### 15. 我没有找到可靠来源、因此没有当成事实写的东西

这部分很重要。

我**没有找到**《崩坏：星穹铁道》彦卿/景元官方 VFX 制作团队公开解释“飞剑具体由哪些 shader/particle layer 组成”的资料，所以我没有把画面观察包装成官方制作方法。

我**没有找到**《鸣潮》清宵官方的飞剑 VFX layer breakdown；能核实的是她确实存在、3.6 于 2026-08-20 上线，以及官方后续 patch notes 明确存在 “Sword Flight” 状态。[Wuthering Waves+1](https://wutheringwaves.kurogames.com/en/main/news/detail/5571?utm_source=chatgpt.com) [鸣潮 3.6 官方版本资讯](https://wutheringwaves.kurogames.com/zh-tw/main/news/detail/5289?utm_source=chatgpt.com)

我没有找到可信的一手技术 breakdown 能证明《天涯明月刀》《剑网3》藏剑/纯阳、《诛仙》《仙剑奇侠传七》《古剑奇谭》《完美世界》《斗罗大陆》《一念永恒》《吞噬星空》的某个具体剑招“就是用 X 层 mesh + Y shader + Z flipbook 制作”；能找到很多视觉视频，但那只能用作观察参考，不能反推制作管线。

我找到的《凡人修仙传》大庚剑阵 B 站 UE5 视频是**第三方临摹拆解**，不是原动画工作室公开技术资料。[Bilibili](https://www.bilibili.com/video/BV1YjBtBfE7E/?utm_source=chatgpt.com) [该 Bilibili 视频](https://www.bilibili.com/video/BV1YjBtBfE7E/?utm_source=chatgpt.com)

我没有获得足够可靠的 Bilibili 评论区正文来逐条引用，所以玩家审美部分主要使用了**可直接读取原文的 TapTap 评论**，而没有伪造“B站网友说”。

“火舌 70–80% 逆速度拉伸”“35/50/80 px 对应哪些层”“6 lead + 24 mid + 64 mass 各自具体保留什么”“A+B+C 的组合方式”全部都是**我针对你这个游戏的工程/美术推断**，不是某个中国厂商公开过的标准。

---

如果现在要直接交给 Claude 开做，我认为不用再继续宽泛研究了。下一步最有价值的是把这份研究压成一份 **Clear Wind Flying-Sword Aura Production Spec**：精确到 A+B+C 每一层的 mesh/texture/shader、screen-space LOD、颜色/value、宽度占 blade width 百分比、动画曲线、94 剑 budget，以及 Fire/Wind/Water/Thunder 等元素如何共享同一个 aura framework。

## E. Tin nhắn gửi Gemini (nguyên văn, một chat mới)

Giống tin nhắn 1 gửi ChatGPT, trừ đoạn đầu (yêu cầu dùng Google Search) và câu cuối của mục 3 (thêm "especially about flying swords and sword qi").

```text
Please use Google Search, in Chinese AND English, and give a URL behind every factual claim: many sources, not one listicle. For Bilibili videos give the title, the uploader (UP主), the BV id and the upload date. Say clearly when something is your own opinion or inference.

Context: I am designing the aura around flying swords for a xianxia typing-defense game (three.js, browser, far top-down 3/4 camera at about 55 degrees). Our hero sword is a real 3D model we keep as-is, "Clear Wind": a slim silver jian, a hollow white-jade ring at the guard, a cloud-shaped guard (the tassel exists only on the hand-held sword). Skills fly up to about 94 swords at once (6 full + 24 LOD + 64 impostors); on a 1080p screen a flying sword is only 35-130 px long. Today they fly bare (thin white-hot edge line, soft rim, short trail) and the owner says they look crude. Our rules: the aura dresses the sword and never hides or replaces it; only thin HDR cores bloom; a dark premultiplied under-layer sits behind every bright layer; no generic glowing outline; Fire must look like flame licking around the sword, not like heated iron.

问题 / Questions:

1) 中国游戏和国漫的特效师怎样做出"高级感"的飞剑和剑气 (飞剑, 御剑, 剑气, 剑光, 剑阵, 万剑归宗)? Search Chinese sources first: Bilibili 特效拆解 / 特效教程 / 特效分析 videos (for example "飞剑特效", "御剑飞行 特效", "剑气 特效 制作", "万剑归宗 特效", "剑阵 特效", "Unity 飞剑 拖尾", "UE 剑气 材质"), 知乎 answers (for example "为什么某游戏的剑气特效看起来高级", "仙侠游戏特效怎么做"), GameRes 游资网, UOD, 腾讯游戏学堂, 网易游戏学院, GDC China, Unite Shanghai, UnrealCircle talks, and official dev diaries. Works to consider: 原神 (魈, 闲云), 崩坏：星穹铁道 (彦卿, 景元), 鸣潮 (卿霄 Qingxiao, 御剑), 永劫无间 (无尘), 天涯明月刀, 逆水寒, 剑网3 (藏剑, 纯阳), 诛仙, 燕云十六声, 仙剑奇侠传七, 古剑奇谭; donghua: 凡人修仙传, 剑来, 仙逆, 完美世界, 斗罗大陆, 一念永恒, 吞噬星空.

2) Layers: which layers do they stack on a flying sword (刃光, 剑芒, 剑气包裹 / 剑罡, 残影 / 拖影, 刀光拖尾, 飘带, 粒子星点, 符文阵纹, 剑尖星芒, 扭曲, 地面投影光), and which ones keep the sword READABLE and LUXURIOUS when it is small on screen (35-130 px)? How do they keep the sword itself the hero (剑本体辨识度) instead of a blob of light?

3) Genericness: how do Chinese artists avoid the cheap 描边发光 / 光污染 look? What do Chinese players complain about (特效糊脸, 光污染, 廉价感, 塑料感, 特效太花) and praise (高级感, 干净, 有质感, 层次感, 留白, 国风)? Quote real player comments with links where you can (Bilibili comments, NGA, 贴吧, 知乎, TapTap), especially about flying swords and sword qi.

4) Fire swords (火剑, 火焰剑气, 炎剑): how do they make flame lick AROUND the blade instead of making the blade look like red-hot iron (烧红的铁)? For example flame tongues outside the silhouette, dark soot edges, flipbook flames, gradient ramps, flame direction against the motion.

5) Many swords at once (万剑, 剑雨, 剑阵): how do they keep 50-100 swords rich but cheap and readable (lead swords versus followers, rhythm, instancing, impostors, GPU mesh particles)?

6) Our three candidate directions (all keep the real blade bare and draw outside its silhouette):
A "Wind-Silk Mantle": a tailored mantle of sharp qi plates just outside both edges; the plates lie flush in flight and shear apart on a cut; two bright seams meet in a needle past the tip; the mantle parts around the jade ring; a tassel-coloured silk tail behind.
B "Echo Cascade": flat, hollow, blade-only afterimages that hang back in a line in flight, fan out on turns and snap shut into the strike; a V-shaped bow wave ahead of the tip.
C "Celestial Regalia": a crowned relic: a four-point star at the tip, a slow halo behind the hollow jade ring, twin silk streamers from the guard tips, orbiting motes, a hairline rim.
For each one: what does Chinese practice and player taste support, and what does it warn against? Give at most two concrete improvements per direction.

End with a table of the 8-12 Chinese sources you trust most (URL, author or uploader, date, what it says), and a list of claims you could not source.
```

## F. Gemini, câu trả lời (nguyên văn)

##### 1. 中国游戏与国漫特效师如何做出“高级感”的飞剑与剑气

在中国游戏与国漫的特效制作体系中，“高级感”并非来自堆砌发光粒子，而是建立在层次感（Layering）、节奏感（Timing/Rhythm）、明度与饱和度克制（Value & Saturation Control）以及动作对帧（Frame-Accurate Alignment）四大支柱之上：

- **节奏感高于一切，且建立在层次感之上：** 网易游戏学堂在《如何理解特效和判定一个特效的品质标准？》（[https://game.academy.163.com/course/careerArticle?course=84](https://game.academy.163.com/course/careerArticle?course=84)）中明确指出，节奏感是高质量特效的第一标准；无论创意多好、颜色多好看、细节多细腻，只要动态节奏感达不到，品质就会大打折扣。GameRes游资网的《角色设计中，如何让角色具有张力、层次感和节奏感？》（[https://www.gameres.com/868130.html](https://www.gameres.com/868130.html)）进一步拆解了二者的递进关系：必须先在黑白色阶（明度）和材质质感上区分开各个层次，再按主次重要程度交错排列，才能形成节奏感。
- **三层递进消散（亮部快闪、暗部滞留）：** 在具体的刀光与剑气制作中，中国特效师普遍采用“三层异步消散”法则。在《学习 - 游戏特效（刀光）》（[https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html](https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html)）与Magesbox《刀光贴图制作AE》（[https://www.magesbox.com/article/detail/id/2116](https://www.magesbox.com/article/detail/id/2116)）中，标准做法是将刀光/剑气拆分为**亮色/高光层、中间色主体层、暗色底层**三层，分别调节粗糙边缘演进值与阶梯渐变；在动态节奏上，**最亮的高光层节奏最快，几乎一闪即逝，而暗色/黑色底层最后消失**，最外沿再配上一道极细的锐利“刀痕/剑痕”。
- **严苛的“对帧”与结构先行：** Bilibili专栏《刀光特效参考图集｜1031张素材一键直达》（[http://www.bilibili.com/read/cv53517098/](http://www.bilibili.com/read/cv53517098/)）总结道，剑气与刀光必须与动作严格“对帧”（慢放到0.25倍速逐帧对齐），错一帧就会出现“刀没到光先到”的廉价割裂感；制作流程必须“先搭大结构，再补细节”，用UE5 Niagara（如Bilibili视频《虚幻5，手把手教你做刀光，保姆级教程》，BV号：`BV11w411c7y8`，上传日期：2023-10-15，UP主名称在Google索引摘要中截断为“UP主更多”，[https://www.bilibili.com/video/BV11w411c7y8/](https://www.bilibili.com/video/BV11w411c7y8/)）或Unity粒子系统构建从蓄力闪光、主剑气到受击残影的完整时序。
- **仙侠作品中的“剑阵”与“剑影分光”：**
  - **《凡人修仙传》与《剑网3》联动：** 在《盘点〈凡人修仙传〉里那些特色强烈的十种法术》（[https://www.sohu.com/a/815792306_568249](https://www.sohu.com/a/815792306_568249)）及17173对《剑网3》×《凡人修仙传》联动的报道（[https://news.17173.com/content/09092026/171555998.shtml](https://news.17173.com/content/09092026/171555998.shtml)）中，韩立的“青元剑诀”与本命法宝“青竹蜂云剑”被拆解为递进的视觉形态：**青元剑芒**（凝练的丈许剑芒）→ **剑影分光术**（借助飞剑法宝的剑光幻化出与飞剑本体一致的剑影，虚实交错）→ **大庚剑阵 / 青竹蜂云剑**（青芒绽开，掺入庚精的剑丝无坚不摧，飞剑密如蜂群飞舞，剑阵灿若云海翻涌）。
  - **《剑来》的本命飞剑差异化：** CSDN《〈剑来〉深度解析》（[https://blog.csdn.net/weixin_42593549/article/details/164534695](https://blog.csdn.net/weixin_42593549/article/details/164534695)）指出，陈平安的本命飞剑“初一”、“十五”等每把剑都有独立的脾气与运动轨迹，剑气表现强调意境与神韵而非单纯的炫光特效。
  - **《崩坏：星穹铁道》（彦卿）与《暗黑破坏神：不朽》×《仙剑奇侠传》：** 米游社《彦卿-崩坏:星穹铁道WIKI》（[https://bbs.mihoyo.com/sr/wiki/content/565/detail?bbs_presentation_style=no_header](https://bbs.mihoyo.com/sr/wiki/content/565/detail?bbs_presentation_style=no_header)）中，彦卿的飞剑围绕“素刃”、“智剑连心”、“霜厉”设计，突出冰晶锐度与寒芒；而网易《暗黑破坏神：不朽》×《仙剑奇侠传》御剑飞行联动（[https://game.163.com/news/2024/04/22/18467_1150949.html](https://game.163.com/news/2024/04/22/18467_1150949.html)）则采用“沉稳威严的剑身 + 周身星芒剑气包裹 + 身后北斗七星天象阵纹浮现”的组合，用阵纹与星芒衬托飞剑本体。

##### 2. 飞剑特效图层拆解（Layers）与小尺寸（35–130 px）下的“剑本体辨识度”

根据CSDN《游戏特效教程：刀光特效制作全流程详解，从建模到粒子实战》（[https://blog.csdn.net/weixin_29504571/article/details/166712652](https://blog.csdn.net/weixin_29504571/article/details/166712652)）、《Unity刀光拖尾特效的一些总结》（[https://blog.csdn.net/weixin_36050664/article/details/112612892](https://blog.csdn.net/weixin_36050664/article/details/112612892)）以及ParticleFX Studio《剑气：免费剑斩特效、GIF 和精灵图》（[https://particlefx.studio/zh/effects/sword-beam](https://particlefx.studio/zh/effects/sword-beam)），完整的飞剑/剑气特效通常由以下图层叠加构成：

| 图层名称 (Layer) | 行业标准做法与混合模式 (源自检索文献) | 35–130 px 远景俯视角下的可读性与取舍 **[个人观点 / 技术推断]** |
| --- | --- | --- |
| **1. 核心高光层 / 刃光 / 最外沿刀痕** | 刀刃轨迹上最窄、最亮、最白的那条线（HDR Bloom），负责“砍中/破空”的确定性；闪烁最快（[https://blog.csdn.net/weixin_29504571/article/details/166712652](https://blog.csdn.net/weixin_29504571/article/details/166712652), [https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html](https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html)）。 | **必留（核心锚点）：** 在35–130 px下，1–2 px宽的锐利HDR高光边缘/剑芒尖端是定义飞剑剪影和朝向的唯一高频信息。 |
| **2. 暗色衬底层 (Dark Under-layer)** | 能量较低、速度较慢的元素使用较暗、接近黑色的明度值，为高亮核心提供对比度，且最后消失（[https://hao.shenyecg.com/Article/948118](https://hao.shenyecg.com/Article/948118), [https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html](https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html)）。 | **必留（防光污染核心）：** 你们规则中的 Premultiplied Dark Under-layer 完全契合这一原理，能在浅色地面或密集剑群中把银色剑身“抠”出来。 |
| **3. 渐变光带层 / 剑气包裹 (剑罡)** | 刀光主体（Beam/Mantle），采用半透明与较低饱和度的过渡色，前端粗后端细（[http://www.bilibili.com/read/cv53517098/](http://www.bilibili.com/read/cv53517098/), [https://hao.shenyecg.com/Article/948118](https://hao.shenyecg.com/Article/948118)）。 | **必须镂空剑身：** 若包裹层覆盖在35–130 px的剑模上方，哪怕只有30%不透明度也会把银剑糊成光棒；必须做剑身外扩偏移（Offset Outside Silhouette）。 |
| **4. 残影 / 拖影 (Afterimages)** | 动作或飞行路径上短暂停留的几何弧线或剑影，滞后于主体（[https://particlefx.studio/zh/effects/sword-beam](https://particlefx.studio/zh/effects/sword-beam), [http://www.bilibili.com/read/cv53517098/](http://www.bilibili.com/read/cv53517098/)）。 | **高价值（尤适转向与斩击）：** 离散的镂空残影不会遮挡剑本体，且能把35 px小剑的运动轨迹放大数倍。 |
| **5. 刀光拖尾 / 飘带 (Trail / Streamer)** | 使用 `TrailRenderer`、带状粒子或无贴图 `MeshLine` 沿路径生成，降低 `Min Vertex Distance` 防止折角，前粗后细（[https://developer.unity.cn/ask/question/63fef8a7edbc2a501197ce54](https://developer.unity.cn/ask/question/63fef8a7edbc2a501197ce54), [https://developer.unity.cn/ask/question/66fe757dedbc2a530fb1c192](https://developer.unity.cn/ask/question/66fe757dedbc2a530fb1c192), [https://juejin.cn/post/7643753392239280128](https://juejin.cn/post/7643753392239280128)）。 | **需严格限宽：** 拖尾起点必须挂在剑格白玉环或剑尾之后，绝不能从剑尖开始拉宽带，否则会吞没剑身。 |
| **6. 剑尖星芒 (Launch/Tip Glint)** | 0.08秒级爆发膨胀再缩小的十字/四角星芒，介于白色与浅金色之间（[https://particlefx.studio/zh/effects/sword-beam](https://particlefx.studio/zh/effects/sword-beam)）。 | **仅限关键帧触发：** 若常驻在35 px飞剑尖端会喧宾夺主，建议仅在出剑（Launch）、急停转向、命中（Impact）瞬间闪现。 |
| **7. 粒子星点 (Motes / Sparks)** | 沿运动方向拉伸的微粒或柔光，随时间缩小并受阻力减速（[https://particlefx.studio/zh/effects/sword-beam](https://particlefx.studio/zh/effects/sword-beam)）。 | **极少而精：** 小尺寸下密集粒子会变成噪点（Noise），每把领头剑最多2–4颗沿轨迹飘散的微粒。 |
| **8. 符文阵纹 (Rune / Array)** | 飞剑出鞘或御剑身后浮现的星象/阵图（[https://game.163.com/news/2024/04/22/18467_1150949.html](https://game.163.com/news/2024/04/22/18467_1150949.html)）。 | **仅限发射源/母剑：** 35–130 px的飞行单剑上画复杂符文会因Mipmap采样变成糊斑，应放在发射母阵或白玉环背后的极简光环上。 |
| **9. 空间热扭曲 (Screen-space Distortion)** | 在Shader中抓取背景颜色缓冲（如Unity `GrabPass`），用噪声图偏移UV实现武器挥动/飞行的空气扭曲（[https://blog.csdn.net/2401_84048161/article/details/137214013](https://blog.csdn.net/2401_84048161/article/details/137214013), [https://blog.51cto.com/u_14691/11063877](https://blog.51cto.com/u_14691/11063877)）。 | **慎用：** 远景下对单把小剑做折射扭曲会扭曲下方的打字UI或地面文字，仅适合大招斩击波或领头剑周围极弱的边缘折光。 |

**如何保持“剑本体辨识度”（Sword Model as Hero）：**

1. **灰度与能量分层（明度反差）：** 深夜学院《揭秘游戏特效的色彩魔法》（[https://hao.shenyecg.com/Article/948118](https://hao.shenyecg.com/Article/948118)）指出，设计特效时应先在灰度模式（无色模式）下检视明度对比；每个元素必须与周围元素形成明度反差，次要颜色必须降低饱和度、变暗并保持半透明。**[个人观点 / 技术推断]：** 既然“清风”（Clear Wind）剑身是亮银色金属与白玉环，环绕剑身的第一圈底色必须是**低明度、冷色调的暗部衬底（Dark Premultiplied Under-layer）**，用“暗气衬亮剑”，而不是“亮气包亮剑”。
2. **几何留白（Silhouette Cutout）：** **[个人观点 / 技术推断]：** 剑气模型（Mesh）或Billboard必须避开剑脊中心线——将剑气片分布在剑刃两侧外沿（距离剑刃外侧 1–2 px 处）以及白玉环后方，让银色剑脊、云纹剑格与中空白玉环直接暴露在摄像机前，不被任何 Additive 图层覆盖。

##### 3. 如何避免“描边发光 / 光污染 / 廉价感”及中国玩家真实评价

###### 行业如何避免“光污染”与“廉价感”

1. **严控色彩种类与饱和度：** 网易游戏学堂在《如何理解特效和判定一个特效的品质标准》（[https://game.academy.163.com/library/2016/02/04/17715_597546.html](https://game.academy.163.com/library/2016/02/04/17715_597546.html)）中警告：“颜色上的表现在于丰富多变，而颜色的丰富多变不在于颜色的多样化，这样会导致特效五颜六色，显得非常花，看久了会视觉疲劳。” 站酷《UI色彩总结》（[https://www.zcool.com.cn/article/ZMTI3OTAxNg==.html](https://www.zcool.com.cn/article/ZMTI3OTAxNg==.html)）同样强调要用主色、辅助色、中性色拉开层次，避免颜色细碎导致“花”。
2. **拒绝全高饱和度叠加：** 深夜学院（[https://hao.shenyecg.com/Article/948118](https://hao.shenyecg.com/Article/948118)）指出：“很多新的视觉特效艺术家都喜欢在特效中添加过多的饱和度，所以请记住，即使在你的主要颜色中，也不要让饱和度级别过高。” 即使使用单色调色板，也应靠**明度和饱和度的微妙渐变**（如白金核心 → 低饱和青蓝中层 → 深黛墨色底衬）来塑造高级感，而非靠外发光描边。

###### 中国玩家的真实吐槽与赞美（附社区原帖链接）

- **玩家对“光污染 / 廉价感”的尖锐批评：**
  - 在NGA玩家社区热帖《[破事氵] 为什么3d二游都喜欢光污染啊》（[https://bbs.nga.cn/read.php?tid=46205232](https://bbs.nga.cn/read.php?tid=46205232)，2026-02-14）中，高赞评论一针见血地讽刺道：“特效是最便宜又没技术含量又会让看的人觉得很nb的东西。至于玩的人怎么想不重要，策划又不玩。”
  - 在巴哈姆特《誅仙世界》哈啦板玩家评测《從視覺、美術、系統與營運模式談為什麼我不會入坑》（[https://forum.gamer.com.tw/C.php?bsn=29299&snA=537](https://forum.gamer.com.tw/C.php?bsn=29299&snA=537)，2025-06-11）中，玩家批评国产仙侠网游滥用大面积光效却缺乏骨骼动作与节奏支撑：“屬於偏慢節奏、視覺大但打擊感不強的設計。光影做得漂亮，但實際戰鬥中的節奏與打擊回饋都比較薄弱。沒有像《黑沙》那種俐落與重量感。”
  - 在233乐园玩家社区对比《天涯明月刀》《逆水寒》《燕云十六声》的实测帖（[https://www.233leyuan.com/post-detail/2061327426197557248](https://www.233leyuan.com/post-detail/2061327426197557248)，2026-06-01）中，玩家“稻葵”与实测评论指出，部分仙侠/武侠游戏虽然堆砌外观与画面，但“打击感实在太差，操作起来不够爽快”，相比之下玩家更认可干净利落、反馈清晰的战斗表现。
- **玩家对“高级感 / 暗部细节 / 国风剑意”的赞美：**
  - 在Bilibili视频《【天涯明月刀手游】场景堪比史诗大片！全局光照技术效果初探》（BV号：`BV1VC4y1p7rb`，上传日期：2020-05-28，[https://www.bilibili.com/video/BV1VC4y1p7rb/](https://www.bilibili.com/video/BV1VC4y1p7rb/)）中，官方与技术解析总结了高级光影的标准：“**高动态全局光照保证了暗部不失真，亮部曝光到位**”——这直接印证了你们“暗部衬底 + 仅极细HDR核心发光”的设计原则。
  - 在网易云游戏《永劫无间侠风赛季新皮肤特效详评》（[https://cg.163.com/static/content/690c144e7f4d7ffa38fd72d5](https://cg.163.com/static/content/690c144e7f4d7ffa38fd72d5)，2025-11-05）与《蓝梦与新挂件特效解析》（[https://cg.163.com/static/content/68949769a7771b4b2cfa393e](https://cg.163.com/static/content/68949769a7771b4b2cfa393e)，2025-08-06）中，玩家高度评价李寻欢飞刀、链剑、折扇等武器的特效，同时对过于高频刺耳的音效与杂乱元素提出警告（“叮叮作响的声音频繁出现，稍嫌喧闹，让人有些不适”），说明无论视效还是音效，“留白与克制”都是防疲劳的关键。

##### 4. 火焰飞剑（火剑 / 火焰剑气）：如何做出“火舌缠绕剑身”而非“烧红的铁”

要让火剑看起来是“灵火/剑气包裹着寒光凛冽的银剑”，而不是一把通体发红的烙铁，需结合中国特效师的噪声溶解（Noise Dissolve）**与**能量色阶分离（Energy-Value Separation）技法：

1. **核心、火舌与黑烟的能量明度分层（黑烟外缘 / 暗色衬底）：** 深夜学院《揭秘游戏特效的色彩魔法》（[https://hao.shenyecg.com/Article/948118](https://hao.shenyecg.com/Article/948118)）给出了火属性特效的标准色阶逻辑：“燃烧的炽热核心应该最亮，飞溅的火花亮度中等，因为能量正在减弱，而从底部冒出的烟雾则应该较暗，因为几乎没有能量参与。” 同样，《学习 - 游戏特效（刀光）》（[https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html](https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html)）在制作黑红色系刀光时，专门将3层分别设为**亮色（极快闪现）、中间色（红橙主体）、暗色（黑红/焦黑底层，最后消失）**。
2. **Shader 噪声溶解（Noise Dissolve）塑造撕裂火舌：** 根据CSDN《Unity Shader 使用Noise 图制作Shader 溶解效果》（[https://blog.csdn.net/mxwin/article/details/159240536](https://blog.csdn.net/mxwin/article/details/159240536)）与Unity社区《粒子拖尾特效怎么制作》（[https://developer.unity.cn/ask/question/63fef8a7edbc2a501197ce54](https://developer.unity.cn/ask/question/63fef8a7edbc2a501197ce54)），动态火焰拖尾与火舌是通过将 `Time × Speed` 叠加到UV偏移上采样噪声贴图（Noise Texture），并结合溶解阈值（Dissolve Threshold）与边缘颜色（Edge Color）实时裁切出来的。
3. **针对你们 35–130 px“清风”剑的具体工程落地 **[个人观点 / 技术推断]**：**
  - **绝对不要修改剑模本体的 PBR 材质色相：** 保持“清风”剑身原本的冷银色高光与白玉环材质不变（或者仅在剑刃法线朝外处给极微弱的暖色环境光反射），一旦给剑身加上橙红色自发光（Emission），在 50 px 尺度下立刻会变成“烧红的铁条”。
  - **轮廓外火舌片（Offset Flame Ribbons）：** 在剑刃两侧外沿各放置一条略宽于剑身的交叉弧面网格（Ribbon Mesh），UV 沿剑尖向剑柄方向高速流动（逆运动方向滚动 `UV.x += time * speed`）。使用双通道 Noise 贴图做硬边 Alpha Clip / Dissolve：内侧紧贴剑刃处留出 1–2 px 的**深炭黑/暗紫红烟气底衬（Premultiplied Dark Soot）**，往外跃出亮金黄色的纤细火芯与朱红火舌，火舌末端通过溶解断裂成离散的火星（Sparks）。这样冷银色的剑脊镶嵌在深色烟衬与金红火舌中央，冷暖对比强烈，火焰是“舔舐”在剑外的。

##### 5. 万剑归宗 / 剑雨 / 剑阵（50–100 把同屏）：如何兼顾丰富度、性能与可读性

在同屏 50–100 把甚至上万把飞剑的“万剑归宗”场景中，中国开发者主要从**渲染管线批处理**与主次视觉编排（Lead vs. Followers）两方面解决性能与杂乱问题：

1. **Three.js 与 UE5 中的“万剑归宗”工程架构：**
  - 在掘金技术文《用three.js + WebGPU + R3F 做一套「可玩」的3D 技能特效实验室》（[https://juejin.cn/post/7643753392239280128](https://juejin.cn/post/7643753392239280128)，2026-05-25）中，作者分享了浏览器端 Three.js 实现“万剑归宗”与“刀光”的轻量化方案：飞剑在平面/空间内随机排布并沿指定方向齐飞，飞行拖尾采用无贴图的 `MeshLine`（金橙或纯色渐变几何带）代替昂贵的多层重度粒子，并在碰撞点结合场景贴花（Decal 剑痕）完成反馈。
  - 在CSDN《UE5大规模技能特效实战：从SSS材质到Niagara粒子性能优化》（[https://blog.csdn.net/weixin_27676369/article/details/164408374](https://blog.csdn.net/weixin_27676369/article/details/164408374)，2026-09-05）与AboutCG《Unreal Engine4 Niagara粒子特效高级案例教学之万剑归宗》（[https://www.aboutcg.org/courseDetails/1219/introduce](https://www.aboutcg.org/courseDetails/1219/introduce)）中，针对海量剑型粒子从分散聚集、旋转、追踪到爆发的全流程，核心要求是控制单把剑的可见度、自阴影与着色开销，避免半透明 Overdraw 堆爆显卡。Bilibili《刀光特效参考图集》（[http://www.bilibili.com/read/cv53517098/](http://www.bilibili.com/read/cv53517098/)）也强调移动端/轻量化场景必须“以质感换算力”，用序列帧或合并网格层代替重度实时粒子解算。
2. **主次分层（Lead Swords vs. Followers）与编队节奏：**
  - 经典国漫与武侠作品中（如Bilibili《难得见到的满血无名，满血万剑归宗》，BV号：`BV1rw411a7CL`，上传日期：2023-10-05，[https://www.bilibili.com/video/BV1rw411a7CL/](https://www.bilibili.com/video/BV1rw411a7CL/)；以及《凡人修仙传》青竹蜂云剑“剑影分光术”，[https://www.sohu.com/a/815792306_568249](https://www.sohu.com/a/815792306_568249)），万剑齐发讲究“众星捧月”与“杀招主剑”。
  - **针对你们 94 把飞剑（6 Full + 24 LOD + 64 Impostors）的分级光环方案 **[个人观点 / 技术推断]**：**
    - **6 把主剑（Full 3D Models，70–130 px）：** 拥有完整的三层剑气（暗部底衬 + 剑刃外扩剑罡/残影 + 1 px HDR 核心刃光 + 剑格飘带拖尾），承担视觉焦点与打字锁定的核心反馈。
    - **24 把次级剑（LOD Models，50–70 px）：** 砍掉飘带、星芒和独立粒子，仅保留“暗色底衬 + 单层流线型外扩剑芒 + 极短 `MeshLine` 拖尾”，明度压低至主剑的 65%，不触发高阈值 HDR Bloom。
    - **64 把远景/伴飞剑（Impostors，35–50 px）：** 相当于《凡人修仙传》中的“剑影分光”——直接将“暗底 + 银剑剪影 + 锐利剑芒线”烘焙进同一张带 Premultiplied Alpha 的 Impostor 贴图中，配合 `InstancedBufferGeometry` 仅用 1 个 Draw Call 渲染，不挂任何实时 Trail 组件（而是通过在 Shader 中按速度矢量拉伸 Impostor 尾端顶点来模拟微短拖影）。这样 94 把剑同屏既像蜂群云海，又绝不会糊成一片白光。

##### 6. 三个候选方向（A / B / C）的中式审美评估与具体改进建议

以下评估结合前述中国特效界的**层次/节奏理论**（[https://game.academy.163.com/course/careerArticle?course=84](https://game.academy.163.com/course/careerArticle?course=84), [https://blog.csdn.net/weixin_29504571/article/details/166712652](https://blog.csdn.net/weixin_29504571/article/details/166712652)）与针对你们 35–130 px 俯视角尺度的[个人观点 / 技术推断]：

###### 方向 A：“Wind-Silk Mantle（风丝剑罡 / 剑衣）”

- **中式实践与审美支持点：**
  - 极度契合仙侠经典中的“剑罡 / 剑芒护体”与“剑丝”设定（如《凡人修仙传》大庚剑阵的庚精剑丝，[https://www.sohu.com/a/815792306_568249](https://www.sohu.com/a/815792306_568249)）。
  - 剑刃外侧的两道高亮细缝（Bright Seams）在剑尖前方交汇成针尖，完全符合中国特效教程中“最亮、最窄的核心高光层负责破空与砍中确定性”（[https://blog.csdn.net/weixin_29504571/article/details/166712652](https://blog.csdn.net/weixin_29504571/article/details/166712652)）的做法。
  - 剑衣在白玉环处分开、尾部延续剑穗色彩的丝绸拖尾，既有国风器物感，又保护了“清风”剑最具辨识度的中空白玉环。
- **中式实践警告的风险点：**
  - 在 35–60 px 的小尺寸下，如果两侧的“剑气甲片（Qi Plates）”造型过于均质对称、没有纵向明暗渐变和边缘破损，在 55° 俯视角下很容易让原本修长的银剑看起来像一把**变粗的扁平阔剑或塑料发光尺**，失去“清风”的纤细灵动感。
- **最多两项具体改进建议 **[个人观点 / 技术推断]**：**
  1. **纵向“前实后虚”阶梯渐变与错落消散：** 遵循《刀光贴图制作AE》（[https://www.magesbox.com/article/detail/id/2116](https://www.magesbox.com/article/detail/id/2116)）与《游戏特效（刀光）》（[https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html](https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html)）的法则，让剑尖交汇针芒保持 100% 锐利亮白，但两侧剑衣从剑身中段向剑格方向迅速做阶梯式透明度衰减与流线抽丝（像风吹散的丝缕而非实心板片），斩击裂开时亮缝 0.08 秒先闪灭，暗色底衬慢 0.15 秒消散。
  2. **白玉环与剑身内沿镶嵌 1.5 px 墨色暗衬槽（Premultiplied Ink Gap）：** 在银色剑刃与外侧剑气甲片之间、以及白玉环内孔边缘，强制留出一条深色预乘暗槽，确保任何背景下剑本体与剑衣之间都有清晰的物理空气感。

###### 方向 B：“Echo Cascade（剑影分光 / 残影叠浪）”

- **中式实践与审美支持点：**
  - 直接对应修真鼻祖级的“剑影分光术”（[https://www.sohu.com/a/815792306_568249](https://www.sohu.com/a/815792306_568249)）以及刀光特效中的“残影（Afterimages）”核心层（[https://particlefx.studio/zh/effects/sword-beam](https://particlefx.studio/zh/effects/sword-beam), [http://www.bilibili.com/read/cv53517098/](http://www.bilibili.com/read/cv53517098/)）。
  - **35–130 px 下可读性最高：** 因为剑身本体两侧几乎没有常驻包裹物，银剑本体在飞行中 100% 裸露清晰；转向时扇形展开、斩击时瞬间收拢合一（Snap shut into the strike），完美体现了网易游戏学堂所强调的“动态节奏感与张力”（[https://game.academy.163.com/course/careerArticle?course=84](https://game.academy.163.com/course/careerArticle?course=84)）。
- **中式实践警告的风险点：**
  - 直线匀速飞行时，如果镂空残影只是呆板地排在剑后一条直线上，由于没有横向面积展开，35–50 px 的飞剑会显得单薄（跟现在老板批评的“光秃秃的短拖尾”拉不开质变差距）；此外，当 30+ 把飞剑同时带多个离散残影时，残影容易与后方另一把真剑混淆，造成视觉杂乱。
- **最多两项具体改进建议 **[个人观点 / 技术推断]**：**
  1. **给残影序列做“色相/明度冷暖递减”以区分真剑与幻影：** 参照深夜学院的色彩过渡原则（[https://hao.shenyecg.com/Article/948118](https://hao.shenyecg.com/Article/948118)），第 1 道残影带极细亮青白边，第 2、3 道残影迅速降低明度与饱和度，转为半透明深青/黛蓝并压在暗色底衬上，让玩家一眼分清哪把是实体的“清风”真剑、哪些是滞后的残影。
  2. **将剑尖前方的 V 形破空波（Bow Wave）贴合到剑尖并向两侧拉出微弧翼：** 不要让 V 形波脱节悬浮在剑尖正前方（否则像科幻战机的激波锥），而是让 V 形破空芒的顶点紧咬剑尖，两翼贴着剑刃外侧向后掠过前 1/3 剑身，既有破空速度感，又能解决直线飞行时剑身偏瘦的问题。

###### 方向 C：“Celestial Regalia（天罡仪轨 / 仙器瑞相）”

- **中式实践与审美支持点：**
  - 非常契合高品阶仙家法宝的“灵宝瑞相”审美（如《暗黑破坏神：不朽》×《仙剑奇侠传》中星辰剑气配身后七星天象，[https://game.163.com/news/2024/04/22/18467_1150949.html](https://game.163.com/news/2024/04/22/18467_1150949.html)）。白玉环背后的慢旋光环（Slow Halo）与剑格双飘带（Twin Silk Streamers）极具古风仪式感，非常适合静态悬停、蓄力待发或主剑特写。
- **中式实践警告的风险点：**
  - **小尺寸与多剑同屏下的“花 / 碎”大忌：** 网易游戏学堂（[https://game.academy.163.com/library/2016/02/04/17715_597546.html](https://game.academy.163.com/library/2016/02/04/17715_597546.html)）与站酷色彩总结（[https://www.zcool.com.cn/article/ZMTI3OTAxNg==.html](https://www.zcool.com.cn/article/ZMTI3OTAxNg==.html)）均警告过元素细碎会导致画面“非常花，看久了视觉疲劳”。在一把仅 35–130 px 长的飞剑上同时塞入“剑尖四角星芒 + 白玉环光环 + 双丝绸飘带 + 环绕星点（Orbiting Motes）+ 极细轮廓边”五种不同几何形态的元素，高速飞行时环绕星点和常驻四角星芒会闪烁成一团像素噪点，完全夺走剑本体的视线。
- **最多两项具体改进建议 **[个人观点 / 技术推断]**：**
  1. **将方向 C 拆分为“悬停/主剑态”与“高速飞行态”（按速度动态收敛）：** 当飞剑在角色身周悬停待命或作为仅有的 1–6 把领头主剑（Full Model）时，展示白玉环慢旋光环与环绕微粒；一旦高速射出，立刻收起环绕微粒与常驻四角星芒（星芒仅在出剑和命中瞬间闪现 0.08 秒，参照 [https://particlefx.studio/zh/effects/sword-beam](https://particlefx.studio/zh/effects/sword-beam)），飞行中只保留白玉环微光与双丝绸飘带。
  2. **双飘带在高速飞行时收束交汇（Converging Twin Streamers）：** 剑格两端引出的双飘带在低速转向时可分叉飘舞，但在高速直线突刺时应受气流牵引向剑尾中心线收束贴合，形成一道修长利落的燕尾剑穗，避免两条宽飘带在 50 px 尺度下遮挡后方飞剑。

> **综合建议 **[个人观点 / 技术推断]**：** 将 **A（风丝剑衣的剑刃外扩剪影）** 与 **B（转向/斩击时的镂空残影叠浪）** 结合用于高速飞行与战斗，而将 **C（白玉环光环与双飘带）** 留给悬停待命态与 6 把 Full LOD 领头主剑，既能彻底解决“裸剑简陋感”，又能在 94 剑齐飞时保持极致的国风高级感与帧率。

##### 7. 最具参考价值的 12 篇中文技术与行业资料汇总表

| 序号 | 标题与 URL | 作者 / 上传者 (UP主) | 日期 | 核心内容摘要 |
| --- | --- | --- | --- | --- |
| 1 | **如何理解特效和判定一个特效的品质标准？**<br>[https://game.academy.163.com/course/careerArticle?course=84](https://game.academy.163.com/course/careerArticle?course=84)<br>及同系列文：<br>[https://game.academy.163.com/library/2016/02/04/17715_597546.html](https://game.academy.163.com/library/2016/02/04/17715_597546.html) | 网易游戏学堂 | 2023-01-02 / 2016-02-04 | 确立特效品质第一标准是动态**节奏感**；指出色彩丰富不等于颜色多样化，五颜六色会导致特效显得“花”并引发视觉疲劳。 |
| 2 | **游戏特效教程：刀光特效制作全流程详解，从建模到粒子实战**<br>[https://blog.csdn.net/weixin_29504571/article/details/166712652](https://blog.csdn.net/weixin_29504571/article/details/166712652) | CSDN博主 `weixin_29504571` | 2026-09-26 | 将完整刀光拆解为三层：**核心高光层**（最窄最白，负责砍中确定性）、**渐变光带层**（主体过渡）、**辅助粒子层**。 |
| 3 | **揭秘游戏特效的色彩魔法**<br>[https://hao.shenyecg.com/Article/948118](https://hao.shenyecg.com/Article/948118) | 深夜学院 (CG导航) | 2024-11-06 | 提出用**灰度模式（明度）**和**能量值**设计特效色阶：高能核心最亮，低能烟雾/底衬接近黑色；警告新手切勿添加过多饱和度。 |
| 4 | **刀光特效参考图集｜1031张素材一键直达**<br>[http://www.bilibili.com/read/cv53517098/](http://www.bilibili.com/read/cv53517098/) | Bilibili专栏作者（Google摘要未显示昵称） | 检索自 Bilibili 专栏 | 拆解刀光的**拖尾（前粗后细）、残留、斩击**三态；强调0.25倍速逐帧“对帧”（防刀没到光先到）以及移动端“以质感换算力”原则。 |
| 5 | **用three.js + WebGPU + R3F 做一套「可玩」的3D 技能特效实验室**<br>[https://juejin.cn/post/7643753392239280128](https://juejin.cn/post/7643753392239280128) | 掘金社区开发者 | 2026-05-25 | 直接针对 **Three.js** 的技能特效实战：涵盖 Slash Mesh 刀光、无贴图 `MeshLine` 拖尾，以及多把剑随机排布齐飞的**万剑归宗**实现。 |
| 6 | **UE5大规模技能特效实战：从SSS材质到Niagara粒子性能优化**<br>[https://blog.csdn.net/weixin_27676369/article/details/164408374](https://blog.csdn.net/weixin_27676369/article/details/164408374) | CSDN博主 `weixin_27676369` | 2026-09-05 | 拆解“**万剑归宗**”大规模剑型粒子从分散、聚集、旋转、追踪到爆发的可见度控制与 Niagara 性能优化。 |
| 7 | **学习 - 游戏特效（刀光）**<br>[https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html](https://seicing.com/html/study/%E6%B8%B8%E6%88%8F%E7%89%B9%E6%95%88%EF%BC%88%E5%88%80%E5%85%89%EF%BC%89.html) | 肥猫的秘密基地 (`seicing.com`) | 站点常驻教程 | 详解三层刀光复制法（亮色、中间色、暗色）与粗糙边缘演进：指出**最亮层节奏最快一闪即逝，黑色暗部最后消失**，外沿加锐利刀痕。 |
| 8 | **剑气：免费剑斩特效、GIF 和精灵图**<br>[https://particlefx.studio/zh/effects/sword-beam](https://particlefx.studio/zh/effects/sword-beam) | ParticleFX Studio | 站点常驻文档 | 逐层列出剑气的 9 个发射器参数与时序：包括 0.08s `Launch Glint`（起手星芒）、0.14s `Sword Beam`、`Beam Trail`、`Afterimages`、`Gold Motes` 等。 |
| 9 | **虚幻5，手把手教你做刀光，保姆级教程** (BV号：`BV11w411c7y8`)<br>[https://www.bilibili.com/video/BV11w411c7y8/](https://www.bilibili.com/video/BV11w411c7y8/) | Bilibili UP主（摘要截断为“UP主更多”） | 2023-10-15 | 共 9 集 UE5 刀光保姆级教程，涵盖基础场景、Sequencer 定序器、刀光网格模型创建及核心材质节点制作。 |
| 10 | **角色设计中，如何让角色具有张力、层次感和节奏感？**<br>[https://www.gameres.com/868130.html](https://www.gameres.com/868130.html) | GameRes游资网 | 2020-05-26 | 用黑白色阶图论证“节奏感建立在层次感之上”，演示如何通过明度、色彩对比度和材质质感的交错排列突出视觉中心。 |
| 11 | **Unity刀光拖尾特效的一些总结** & **Unity 武器拖尾效果**<br>[https://blog.csdn.net/weixin_36050664/article/details/112612892](https://blog.csdn.net/weixin_36050664/article/details/112612892)<br>[https://blog.csdn.net/2401_84048161/article/details/137214013](https://blog.csdn.net/2401_84048161/article/details/137214013) | CSDN博主 `weixin_36050664` / `2401_84048161` | 2021-01-12 / 2024-04-01 | 总结刀光拖尾的三层结构（带辉光的最亮高光、主体、残影拖尾）及使用 `GrabPass` + 噪声图 UV 偏移实现武器热扭曲拖尾。 |
| 12 | **[破事氵] 为什么3d二游都喜欢光污染啊**<br>[https://bbs.nga.cn/read.php?tid=46205232](https://bbs.nga.cn/read.php?tid=46205232) | NGA玩家社区 | 2026-02-14 | 反映中国核心玩家对滥用廉价发光特效（“光污染”）的反感，指出堆砌发光是最廉价且无视操作者视觉体验的做法。 |

##### 8. 未能通过 Google Search 直接检索到原始出处的声明与原因说明 (Unsourced / Unindexed Claims)

为严格遵守你的要求（不虚构任何链接或B站UP主信息，明确区分检索事实与未能检索到的内容），以下内容在本次 Google Search 中未能获取到直接的网页索引：

1. **知乎（Zhihu.com）原帖直链：** 由于知乎近年来在 `robots.txt` 中全面禁止了 Google 爬虫抓取（`site:zhihu.com` 在 Google Search 中返回为空），因此无法直接提供知乎回答的原始 URL，相关行业共识已改由网易游戏学堂、GameRes、CSDN 与深夜学院等可公开检索的技术文章提供 URL 支撑。
2. **部分 Bilibili 视频的 UP主昵称字段：** 虽然通过 Google 成功检索到了 Bilibili 视频标题、BV号与精确上传日期（如 `BV11w411c7y8` 上传于 2023-10-15、`BV1VC4y1p7rb` 上传于 2020-05-28、`BV1rw411a7CL` 上传于 2023-10-05、`BV1Nz421z7AS` 上传于 2024-06-20），但部分视频页面在 Google 索引摘要（Snippet）中将作者栏截断为“UP主更多”而未暴露具体昵称字符串，故未做猜测或编造。
3. **特定作品（如《鸣潮》卿霄、《永劫无间》无尘、《原神》闲云、《仙逆》/《完美世界》动画）的官方内部特效工程拆解文档：** 公开搜索引擎中关于上述具体角色的页面多为技能倍率图鉴（如米游社/HoYoWiki 彦卿词条 [https://wiki.hoyolab.com/pc/hsr/entry/28?lang=zh-cn](https://wiki.hoyolab.com/pc/hsr/entry/28?lang=zh-cn)）或剧情解析，腾讯游戏学堂/UOD/UnrealCircle 针对单一飞剑角色的内部 Shader 拆解未在公开 Google 索引中检出全文。
4. **35–130 px 像素级参数（如 1.5 px 暗槽宽度、LOD 三级明度百分比 65% 等）：** 公开特效文章定性阐述了“三层结构、亮快暗慢、灰度对比”，但未针对“55度俯视角、35–130 px 飞剑”给出具体像素数值，文中所有针对该尺寸的像素数值与 Three.js 分级方案均为基于上述文献原理推导的[个人观点 / 技术推断]。

如果你需要把这些设计方案直接转化为 Three.js 代码或材质参数，我们可以继续深入：

## G. Claude kiểm nguồn (03/11/2026)

Claude tự mở các nguồn bằng WebFetch hoặc tab riêng trong trình duyệt của ứng dụng (trang Bilibili, trang của NetEase và bài đọc trên Bilibili đọc bằng tab; tên, UP主 và ngày của video Bilibili đọc từ API công khai `x/web-interface/view` của chính Bilibili, giờ Bắc Kinh). Video Bilibili chỉ được kiểm tiêu đề, người đăng, ngày và mô tả; Claude không xem hết nội dung video, nên mọi câu "video này dạy X" ngoài tiêu đề và mô tả đều ghi là chưa kiểm. Không có ảnh hay khung nào từ các nguồn này được gửi cho công cụ AI.

**Nguồn ChatGPT đưa:**

| Khẳng định | URL | Kết quả |
|---|---|---|
| Đạo diễn mỹ thuật 杜文凯 của 《仙逆》 (phim hoạt hình) nói chiêu thức đi từ "quang hiệu đơn thuần" sang vật có hình (dây máu, sóng máu, quan tài máu) và cố tránh "đại diện tích quang hiệu chỉ dùng pháp trận đối nhau" | https://www.thepaper.cn/newsDetail_forward_34200912 | **Đúng.** 澎湃号·湃客, 06/10/2026, không có tên tác giả riêng. Có nguyên câu "从单纯光效，变成血藤、血浪、血棺" và "尽量避免大面积光效只用法阵对拼的情况，更多招式转为与环境结合"; thêm câu "把特效从抽象光效，升级成空间物理环境变化的体系化制作". |
| 《剑来》 dùng "剑气水墨风" như một cách 化繁为简, chọn ngược với lối "màu phức tạp + đánh sáng bão hòa cao", dùng "水墨粒子画风" | https://www.bjnews.com.cn/detail/1723716014168380.html | **Đúng.** 新京报, 15/08/2024, phóng viên 杨莲洁. Đây là bài báo về phim, không phải bài kỹ thuật. |
| 网易雷火 (己凹米): "特效并不是无脑加一些发光的效果就可以"; cần chủ thể rõ, chủ thứ của điểm bùng, nhiều tầng, quỹ đạo có hình; hiệu ứng to quá che tầm nhìn; cành mai làm mảnh lại | https://www.gameres.com/916099.html | **Đúng.** Có các câu "很强的主体性", "拉开爆点主次", "设计运行轨迹的造型美感", "可能还会遮挡玩家的视线", "更加纤细的梅花枝干". Trang ghi ngày 01-12, không ghi năm. |
| Họa sĩ nguyên họa 《逆水寒》 (对子): gió, khí, đao quang qua "几何归纳" thì ra hiệu quả hơn; hạt vụn khó thể hiện; cát vàng gom thành dải mạnh hơn nhiều; một ngọn lửa đơn giản = vài nhóm lưỡi lửa + một nhóm tia lửa; vũ khí phụ ma thêm "模型 hiệu ứng" để đổi bóng dáng | https://www.gameres.com/forum/t/906094 | **Đúng.** 30/05/2024, nguồn 网易雷火艺术中心. Bài không dùng chữ "mesh"; câu gốc là "增加额外特效模型，通过特效重塑设计重点". |
| NEXT Studios (腾讯游戏学院): đao quang cần một lớp đáy "较宽较暗的淡出时间稍长" cộng một lớp "较细较明亮更快消失" ở mép trên; lớp sáng không được tồn tại lâu | https://www.gameres.com/836363.html | **Đúng.** 30/01/2019, bài tái đăng từ 腾讯游戏学院. Đây là nguồn tiếng Trung khớp nhất với luật "mực dưới, lõi mảnh" của mình. |
| Kuro (林晨晨, IGDC): đòn đánh có tám tầng biểu hiện (động tác, đèn cảnh, đèn nhân vật, hiệu ứng thường, mờ xuyên tâm, hạt GPU, méo không khí, đổi màu cảnh); chuyển hạt từ CPU sang GPU | https://www.gameres.com/forum/t/879272 | **Đúng.** 08/01/2021 (tái đăng từ 手游那点事). Bài nói "八个层次" nhưng liệt kê bảy mục. Có câu "空气扭曲，效果可以让人物的剑好像把空气划开了一样". Về 《战双帕弥什》, không về kiếm bay. |
| GameRes (nagatsuki): hiệu ứng kỹ năng có ba pha thi pháp, bay, trúng; "各种特效堆叠，光污染严重，反而忽略了动作本身" | https://www.gameres.com/865778.html | **Đúng.** 17/04/2020. |
| 《永劫无间》 làm lại 无尘: sinh phi kiếm quanh thân; tuyệt kỹ 剑雨 có sức áp chế mạnh; bộ kỹ năng là bộ đội phát triển thích nhất | https://www.yjwujian.cn/news/update/20240731/33456_1171206.html | **Đúng.** Đăng 31/07/2024, cập nhật 02/08. Có "在周身生成飞剑", "其连绵的剑雨拥有极强的压制力", "是开发者内部最喜欢的". Thông báo luật chơi, không nói cách dựng hình. |
| TapTap, 《失落城堡2》: "特效太花，组队打着打着就找不到人在哪了…二阶段都找不到boss"; người khác: "特效太多，容易看不清自己人在哪里", hiệu ứng trang phục "特别花里胡哨" | https://www.taptap.cn/review/50902885, https://www.taptap.cn/review/50965248 | **Đúng.** 27/10/2026 và 31/10/2026. Lời chê hiệu ứng chung, không riêng kiếm bay. |
| TapTap, 《幻想九霄》: "光污染太严重了… 出个特效透明模式"; "特效和预警颜色重复… 但是又不想关闭特效影响爽感" | https://www.taptap.cn/moment/845609340168569997, https://www.taptap.cn/moment/843207845351524095 | **Đúng.** 06/09/2026 và 30/08/2026. Không riêng kiếm bay. |
| Riot "Clarity in League": bóng dáng là thông tin quan trọng nhất; độ thu hút phải khớp tầm quan trọng; nhiễu thị giác cộng dồn nhanh; vật bay phải cho biết hướng cả khi đứng hình | https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/ | **Đúng.** 12/03/2021, bananaband1t. |
| Riot "Behind the Scenes of VFX Updates": dễ đọc, bớt chi tiết vụn, chiêu không được quá sáng | https://www.leagueoflegends.com/en-us/news/dev/dev-behind-the-scenes-of-vfx-updates/ | **Đúng.** 25/04/2022. |
| Chín video Bilibili ở bảng mục 2 và mục 3 (BV13b7a6sEas, BV1xq536mETu, BV1XGQpY9ENV, BV1MVzNB4EF5, BV1cAB8B7Ek1, BV1Us411172g, BV1YjBtBfE7E, BV1JJ411T71T, BV1Th411C7ex): tiêu đề, UP主, ngày | https://www.bilibili.com/video/BV… | **Đúng** cả chín về tiêu đề và người đăng. Ngày đúng, trừ BV1XGQpY9ENV: Bilibili ghi 13/03/2025 giờ Bắc Kinh, ChatGPT ghi 12/03. BV1Us411172g có 26 phần, trong đó có "万剑术（上）/（下）". BV1YjBtBfE7E là bản "特效解析" UE5 của người ngoài (891 lượt xem), không phải của xưởng làm phim. Các câu về nội dung bên trong video (ví dụ "同系列…火焰元素表达 25:48") **chưa kiểm**. |
| Thêm ở bản 2: BV1Z54y1e77w (万剑归宗, 3ds Max Particle Flow, YD特效达人, 02/09/2020), BV1cX4y137nB (Niagara 万剑归宗, 麦田老湿, 11/04/2021, quảng cáo khóa học AboutCG) | như trên | **Đúng** (tiêu đề, người đăng, ngày, mô tả). |
| Phản ứng của người xem với Qingxiao: BV1fjbf6qEjE "清宵与漂泊者双飞（御剑飞行）实机展示，太帅了！" (番茄酱不知, 20/08/2026); BV1JWNj68EGF "【鸣潮】清宵登场！剑阵太帅了！" (爱弥斯的猫-, 10/07/2026, 1.756 lượt thích) | như trên | **Đúng** (tiêu đề). BV1JWNj68EGF đăng trước ngày ra bản 3.6, nên có thể là cảnh xem trước. Các bình luận được thích nhiều nhất dưới hai video không nói về hình kiếm. |
| BV1UW4JzQETW "永劫无间：无尘的奥义特效展示，剑仙变牌皇" (松子姐, 10/10/2025) | như trên | **Đúng.** Bình luận được thích dưới video chê da không đổi động tác và giọng ("皮肤再好看也很违和"). |
| BV1F3aizeEE3 "【凡人修仙传159集】大庚剑阵真的就是在炫技!!!" (桑心嗄, 06/09/2025) | như trên | **Đúng** (tiêu đề). ChatGPT không xếp là khen hay chê, Claude đồng ý. Một bình luận (0 lượt thích) nói 大庚剑阵 "存在感一般". |
| Bài Bilibili của 神猪说动漫: "特效拉满，水墨风好绝" về 《剑来》 | https://www.bilibili.com/opus/966118387506741266 | **Chưa kiểm.** |
| Báo 人民网 về màn "vạn kiếm" của 范十三; khán giả chê "所有的剑都像排队，没有灵动感" | https://sc.people.com.cn/n2/2025/0902/c345167-41340002.html | **Không kiểm được:** chứng chỉ của máy chủ sai tên miền khi WebFetch đọc. Chỉ dùng làm gợi ý. |
| Phỏng vấn 吴炫辉, tổng giám hiệu ứng phim 《风云Ⅱ》: cảnh 万剑归宗 dùng hệ hạt cộng "Particle Control Rig" tự viết để nắm "各自的流通速度、方向、重量感" của từng thanh kiếm | https://chinavid.com/interview/2009-12-14/0912143300773_2.htm | **Đúng.** 14/12/2009, tái đăng từ 火星时代. Hiệu ứng phim, không phải thời gian thực. |
| Bài hướng dẫn lửa của Epic dùng flipbook SubUV và sprite theo vận tốc | (bản 2 gắn link trang Xiao của Genshin) | **Trích dẫn sai link ở bản 2.** Bản 1 gắn link Epic; Claude không mở lại. Đây là kiến thức chung, không phải nguồn tiếng Trung. |
| Qingxiao là nhân vật bản 3.6, bản 3.7 có trạng thái "Sword Flight" | trang Kuro | **Đúng**, đã kiểm ở [`sword-aura-chatgpt-2026-11-03.md`](sword-aura-chatgpt-2026-11-03.md) mục E. |

**Nguồn Gemini đưa:**

| Khẳng định | URL | Kết quả |
|---|---|---|
| 网易游戏学堂 (蛋蛋): "特效的节奏感是高质量效果保证的第一选择"; màu nhiều loại làm hiệu ứng "五颜六色，显得非常花，看久了会视觉疲劳" | https://game.academy.163.com/course/careerArticle?course=84, https://game.academy.163.com/library/2016/02/04/17715_597546.html | **Đúng.** Bản trên course ghi 03/01/2023; bản trong thư viện không ghi ngày. Nguyên câu: "颜色上的表现在于丰富多变，而颜色的丰富多变不在于颜色的多样化，这样会导致特效五颜六色，显得非常花，看久了会视觉疲劳". |
| GameRes (画画的黄翰杰): "节奏感是建立在层次感之上的", minh họa bằng thang đen trắng | https://www.gameres.com/868130.html | **Đúng**, nhưng là bài về vẽ nhân vật, không về hiệu ứng. Gemini dùng nó như nguyên tắc hiệu ứng. |
| Đao quang chia ba lớp sáng, giữa, tối (tông đen đỏ); "最亮的一层肯定是节奏最快的，几乎一闪就消失了，黑色部分最后消失"; thêm lớp vết đao ngoài cùng cho sắc | https://seicing.com/html/study/… (肥猫的秘密基地) | **Đúng** về nội dung. Đây là một blog học tập, không ghi tác giả và ngày. Câu của Gemini "中国特效师普遍采用" là **suy rộng**: một blog không chứng minh "phổ biến". |
| Bài 深夜学院 trên Bilibili: đao quang phải "对帧" với động tác, lệch một khung là "刀没到光先到"; "先搭大结构，再补细节"; vệt "前端粗后端细"; di động "以质感换算力" | https://www.bilibili.com/read/cv53517098/ | **Đúng.** Bài ngày 20/10/2026 của 深夜学院, một trang tập hợp ảnh tham khảo. Câu 0,25× là lời khuyên xem chậm ảnh tham khảo. |
| 深夜学院 "揭秘游戏特效的色彩魔法": kiểm độ sáng ở ảnh xám; lõi cháy sáng nhất, tia lửa vừa, khói tối; đừng để độ bão hòa quá cao | https://hao.shenyecg.com/Article/948118 | **Không kiểm được.** Trang chỉ hiện khung điều hướng, không có bài, cả qua WebFetch lẫn tab. Lời trích có vẻ dịch từ một bài tiếng Anh; chưa rõ nguồn gốc. |
| ParticleFX Studio "剑气": chín emitter, Launch Glint 0,08 s, Sword Beam 0,14 s, Afterimages, Gold Motes | https://particlefx.studio/zh/effects/sword-beam | **Đúng một phần.** Đây là trang tài sản hiệu ứng thương mại của Explain AI Ltd. (nhiều ngôn ngữ), không phải tư liệu của họa sĩ Trung Quốc. 0,14 s là của Beam Trail, không phải Sword Beam. |
| Bài 掘金 làm "万剑归宗" bằng three.js: kiếm xếp ngẫu nhiên, bay cùng hướng, vệt `MeshLine` không texture, decal vết kiếm | https://juejin.cn/post/7643753392239280128 | **Đúng một phần.** 26/05/2026, 前端繁华如梦. Có "多把 Katana 在平面内随机排布，沿指定方向齐飞" và decal; **`MeshLine` là của chiêu rồng**, không phải của 万剑归宗. |
| Sohu: trong 《凡人修仙传》, 青元剑芒 → 剑影分光术 "借助飞剑法宝的剑光幻化出和飞剑一样的剑影" → 大庚剑阵 với "剑丝无坚不摧" | https://www.sohu.com/a/815792306_568249 | **Đúng.** 14/10/2024, bài của người hâm mộ về các pháp thuật trong truyện và phim. Bài ghi 青竹**峰**云剑. |
| 17173: vật phẩm hiệu ứng liên kết 《剑网3》×《凡人修仙传》: "天地变色，青芒绽开，四方飞剑俱听号令，飞剑密如蜂群飞舞，剑阵灿若云海翻涌" | https://news.17173.com/content/09092026/171555998.shtml | **Đúng.** 09/09/2026. Lời quảng cáo. |
| NetEase: liên kết 《暗黑破坏神：不朽》×《仙剑奇侠传》 "御剑飞行": "沉稳威严的剑身 + 周身星芒剑气包裹 + 身后北斗七星天象阵纹浮现" | https://game.163.com/news/2024/04/22/18467_1150949.html | **Đúng một phần.** 22/04/2024. Trang ghi "剑身铸有七星天象" (bảy sao **đúc trên thân kiếm**, không phải trận đồ hiện sau lưng), "沉稳威严的金光剑身与璀璨华丽的金色剑气相互映衬", "运星芒为周身剑气". Lời quảng cáo, tông vàng. |
| NGA "[破事氵] 为什么3d二游都喜欢光污染啊" (14/02/2026): "特效是最便宜又没技术含量又会让看的人觉得很nb的东西…" | https://bbs.nga.cn/read.php?tid=46205232 | **Không kiểm được** (403). |
| 巴哈姆特, 《誅仙世界》: "視覺大但打擊感不強…光影做得漂亮，但實際戰鬥中的節奏與打擊回饋都比較薄弱" | https://forum.gamer.com.tw/C.php?bsn=29299&snA=537 | **Không kiểm được** (403). |
| 233乐园: người chơi so 《天涯明月刀》《逆水寒》《燕云十六声》, chê "打击感实在太差" | https://www.233leyuan.com/post-detail/2061327426197557248 | **Chưa kiểm.** |
| 网易云游戏, bài của người chơi về da 《永劫无间》: khen hiệu ứng phi đao, kiếm xích; chê "叮叮作响的声音频繁出现，稍嫌喧闹，让人有些不适" | https://cg.163.com/static/content/690c144e7f4d7ffa38fd72d5, https://cg.163.com/static/content/68949769a7771b4b2cfa393e | **Đúng một phần.** Bài 05/11/2025 (người chơi 双余Xn) có lời khen; câu "叮叮作响" nằm ở bài **khác** (07/08/2025, người chơi) và nói về **tiếng** của hiệu ứng mới, không phải hình. |
| Video chính thức 《天涯明月刀手游》: "高动态全局光照保证了暗部不失真，亮部曝光到位" | https://www.bilibili.com/video/BV1VC4y1p7rb/ | **Đúng** (mô tả video của tài khoản chính thức, 28/05/2020). Nói về chiếu sáng cảnh; Gemini dùng nó như chuẩn của hiệu ứng là **suy rộng**. |
| BV11w411c7y8 "虚幻5，手把手教你做刀光，保姆级教程" (15/10/2023, 9 phần) | như trên | **Đúng.** Người đăng là Event_Orez (Gemini không đọc được tên). |
| BV1rw411a7CL (恬氏漫语, 05/10/2023), BV1Nz421z7AS (影视巡un, 21/06/2024; Gemini ghi 20/06) | như trên | **Đúng** (tiêu đề, người đăng). Là đoạn cắt phim của người hâm mộ, không phải tư liệu làm hiệu ứng. |
| Các bài CSDN (166712652, 112612892, 137214013, 159240536, 164408374, 164534695), trang Unity China, ZCOOL, AboutCG, magesbox | — | **Chưa kiểm** (166712652 trả HTTP 521). Toàn là blog kỹ thuật chung về đao quang, vệt, tan rã bằng nhiễu; không đổi kết luận. |
| Zhihu chặn Google nên không có link Zhihu | — | **Không kiểm.** Cả hai công cụ không đưa được câu trả lời Zhihu nào. |

**Claude tự thêm:**

| Khẳng định | URL | Kết quả |
|---|---|---|
| Trang tin người hâm mộ trên 17173 (漂泊者之家, 10/06/2026): "清宵其实热度极高，因为都想着御剑飞行" | https://news.17173.com/content/06102026/141404114.shtml | **Đúng.** Bài viết trước khi ra mắt, dựa trên tin đồn. Cho thấy người chơi rất muốn "ngự kiếm", không nói gì về hình hiệu ứng. |

**Tóm lại:**
- Đếm theo dòng của hai bảng:
  - nguồn ChatGPT, 22 dòng: 19 đúng, 1 gắn sai link, 1 không kiểm được, 1 chưa kiểm;
  - nguồn Gemini, 19 dòng: 7 đúng, 6 đúng một phần (phần lớn do suy rộng hoặc gắn nhầm bài), 3 không kiểm được (403, trang trống), 3 chưa kiểm (khoảng mười bài blog kỹ thuật chung).
- ChatGPT chính xác hơn rõ rệt, nhất là sau lượt tự rà soát. Gemini đưa nhiều nguồn mới nhưng hay đẩy một bài lẻ thành "ngành làm vậy".
- Nguồn tiếng Trung **chắc nhất** là năm bài của người làm nghề: NEXT (lớp tối rộng chậm dưới lớp sáng mảnh nhanh), 逆水寒 (quy về hình học), 网易雷火 (không vô não thêm phát sáng), 网易游戏学堂 (nhịp là chuẩn số một; màu không phải nhiều loại), và lời đạo diễn mỹ thuật 《仙逆》.
- **Chưa ai tìm được** một bài phân tích chính thức về cách dựng kiếm bay của Qingxiao, Yanqing hay 大庚剑阵, và chưa có lời người chơi Trung Quốc kiểm được nói riêng về hình kiếm bay (khen hay chê). Lời chê "光污染" kiểm được đều là chê hiệu ứng chung.

## H. Đánh giá của Claude

**Nguồn tiếng Trung thêm gì:**
- **Hình trước, sáng sau.** Bốn nguồn độc lập nói cùng một điều: 《仙逆》 bỏ "quang hiệu đơn thuần" để chiêu có hình; 逆水寒 bảo gió, khí, đao quang phải quy về hình học có đường viền và hướng; 网易雷火 nói hiệu ứng không phải là thêm phát sáng; 《剑来》 chọn 化繁为简. Đây là bằng chứng mạnh nhất cho luật "không viền phát sáng chung chung" của §1.2, và nghiêng về A (áo có hình) hơn là một viền sáng đều.
- **Thứ tự tắt của lớp tối và lớp sáng.** NEXT và blog seicing cùng nói lớp sáng mảnh tắt nhanh nhất, lớp tối rộng tắt sau cùng. Tài liệu mình đã có lớp mực trong cùng shader, nhưng chưa ghi lớp mực **ở lại lâu hơn** lõi sáng khi tan. Đây là chi tiết nhịp nên thêm cho cả ba hướng.
- **Nhịp là chuẩn số một.** 网易游戏学堂 đặt nhịp lên trên cả ý tưởng và màu; GameRes chia thi pháp, bay, trúng; lời chê 光污染 là chê sự chồng chất. Cả hai công cụ suy ra: bay đều phải là pha yên nhất, sự kiện (phóng, rẽ, bổ) mới sáng. Tài liệu đã có ý này ở §2.3; nguồn tiếng Trung củng cố, không đổi.
- **Vạn kiếm cần khác nhau từng thanh.** Phim 《风云Ⅱ》 điều khiển tốc độ, hướng, cảm giác nặng của từng thanh kiếm. Dòng sông 94 thanh của mình bay theo năm làn bện; nguồn này gợi ý lệch pha nhỏ theo từng thanh trong nhịp hào quang (thở, lấp lánh, độ dài vệt), để dòng không "xếp hàng". Câu chê "像排队" của 人民网 chưa kiểm, chỉ là gợi ý.
- **Người chơi muốn đã mắt nhưng đọc được.** Lời người chơi kiểm được ("不想关闭特效影响爽感") cho thấy họ không đòi ít hiệu ứng hơn; họ đòi thứ bậc. Điều này khớp với cổng "chữ gõ đọc được" và "kiếm đọc được" của §6.
- **Tên gọi văn hóa.** "剑影分光术" trong 《凡人修仙传》 là kiếm quang hóa thành bóng kiếm giống hệt phi kiếm; "剑丝" của 大庚剑阵; "剑罡". Đây là cái neo văn hóa cho B và A khi trình bày với anh. Nhưng trong truyện, bóng **giống hệt** kiếm, còn luật của B là bóng **chỉ là lưỡi** để không đọc thành "thêm kiếm". Claude giữ luật của B: ở camera chơi, đọc được quan trọng hơn chép đúng truyện.
- **Lời quảng cáo chính thức** (NetEase, 剑网3) tả cặp đôi "thân kiếm trầm, uy nghiêm" với "kiếm khí rực rỡ" làm nền cho nhau. Đó đúng là quan hệ thép trần và hào quang ngoài viền của mình. Lưu ý: cả hai dùng tông vàng, trong khi Metal của mình không có vàng và vàng là màu tiền (canon §21.1).

**Chỗ Claude không đồng ý:**
- **Gemini suy rộng:** "三层异步消散是中国特效师普遍采用" dựa trên một blog; "官方总结高级光影标准" dựa trên một câu quảng cáo về chiếu sáng cảnh; ParticleFX Studio là trang tài sản thương mại, không phải thực hành Trung Quốc; `MeshLine` của bài 掘金 thuộc chiêu rồng. Phần thiết kế của Gemini vẫn đáng đọc, nhưng các câu "theo ngành" của nó phải đọc là ý kiến.
- **Cả hai công cụ đều đề nghị ghép A, B, C** (A là nhận diện, B là ngữ pháp chuyển động, C là thứ bậc). Hai công cụ cùng nói không phải bằng chứng: đề bài liệt kê sẵn ba hướng, và đây là suy luận của chúng (ChatGPT tự ghi "my design conclusion"). Hướng ghép này gần với ghi chú §3.D "mượn **một** lớp của hướng khác **sau khi** A đạt". Claude giữ nguyên quy trình: anh chọn một hướng; việc mượn lớp chỉ bàn sau khi hướng đó đạt cổng, mỗi lần một lớp, có số đo chồng lớp.
- **Điểm số** (ChatGPT cho A 9/10, B 8,5/6,5, C 7/9) là ý kiến, không vào bảng so sánh.
- **Gemini muốn tia lóe mũi chỉ ở khung phóng và trúng** (0,08 s). Với C, bỏ hẳn sao thường trực làm C còn trần hơn ở dòng sông, đúng rủi ro chính của C. Claude chỉ nhận một nửa: sao của kiếm chủ thành sao trục kim, không lấp lánh liên tục; đỉnh sáng ở phóng và trúng (xem §2.7).
- **Gemini đề nghị nướng quầng vào atlas impostor và kéo đỉnh impostor theo vận tốc.** Tài liệu đã chọn tính quầng bằng giải tích (§7, câu tự quyết), lý do vẫn đứng.

**Còn thiếu sau lượt này:**
- Chưa có lời người chơi Trung Quốc kiểm được nói riêng về hình kiếm bay. NGA và 巴哈姆特 bị chặn; Zhihu không có trong chỉ mục của Google. Muốn có, cần một người đọc được NGA hoặc Zhihu khi đăng nhập, hoặc anh cho phép đọc bình luận Bilibili theo từ khóa.
- Chưa có bài phân tích chính thức nào của Kuro, HoYoverse hay xưởng phim 凡人 về cách dựng kiếm bay; hai công cụ đều nói vậy, Claude cũng không tìm thấy.
- Chưa có nguồn tiếng Trung riêng cho "lửa liếm quanh lưỡi, không như sắt nung". Phần lửa của ba hướng vẫn dựa trên luật lửa chung (vài nhóm lưỡi lửa, tia lửa, lớp tối tắt sau cùng) và chẩn đoán của chính mình.
