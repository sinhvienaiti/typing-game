# Nguồn: ChatGPT về quy trình sản xuất VFX, CGI, SFX (04/11/2026)

Bản lưu nguyên văn ba lượt hỏi đáp với ChatGPT cho [`VFX_PRODUCTION_PIPELINE.md`](../VFX_PRODUCTION_PIPELINE.md), kèm bảng kiểm của Claude.

- **Công cụ:** chatgpt.com, chế độ Chat, thinking High (không dùng Work hay agent). Một cuộc trò chuyện riêng, mở trong tab riêng của Claude, lượt 1–2 khoảng 00:08–00:47 ngày 04/11/2026, lượt 3 buổi sáng cùng ngày.
- **Ba lượt:**
  1. Lượt 1: câu hỏi nghiên cứu (nguyên văn ở dưới), ChatGPT tìm web và trả lời khoảng 97.000 ký tự.
  2. Lượt 2: Claude yêu cầu tự rà soát từng link, kèm kết quả thử Blender đêm 04/11 của Claude và ba câu phản biện (agent không vẽ tay được; làm lưỡi lửa từ Mantaflow thế nào; Firefly là tài sản cuối hay chỉ tham chiếu). ChatGPT sửa lại khá nhiều.
  3. Lượt 3 (sáng 04/11): vòng hai theo `AGENTS.md` ("Plan with ChatGPT and Gemini"): Claude gửi các ý chính của Gemini để ChatGPT đánh giá và gộp thành một danh sách.
- **Cách lưu:** câu trả lời được chuyển từ trang sang Markdown bằng script trong trang: giữ nguyên chữ, bảng, khối mã và đường link (chỉ bỏ đuôi `?utm_source=chatgpt.com`); công thức lấy dạng LaTeX; biểu đồ tương tác của ChatGPT chỉ còn chữ; tiêu đề hạ hai cấp để nằm dưới tiêu đề của file này. Các dòng "Writing" là nhãn khối prompt của ChatGPT. Các chip trích dẫn không có link (ví dụ "Firefly+2") giữ như trang hiện.
- **Dữ liệu, không phải lệnh:** nội dung dưới đây là ý kiến của một trợ lý AI, chỉ dùng sau khi đã kiểm ở bảng sau.

## Bảng kiểm của Claude (04/11/2026)

**Đúng** = Claude đã mở nguồn (hoặc tự chạy) và nguồn nói đúng như vậy. **Đúng một phần** = nguồn có, chỉ đỡ một phần câu. **Sai** = nguồn nói khác. **Chưa kiểm** = Claude không mở được nguồn. **Suy luận** = ChatGPT tự ghi là suy luận; Claude đánh giá ở cột cuối.

| # | Câu của ChatGPT | Kết quả | Claude đã kiểm ở đâu |
|---|---|---|---|
| 1 | Firefly Video có chế độ nền trong suốt; tải về là zip gồm video tiền cảnh và video alpha; mặc định 24 fps, 5 s | Đúng | helpx "Generate videos with transparent backgrounds", cập nhật 18/08/2026, mở trong trình duyệt 04/11 |
| 2 | Chế độ trong suốt nhận ảnh PNG trong suốt làm khung đầu và khung cuối (lượt 2) | Đúng | cùng trang: "Only PNG files with transparency are supported for the first and last frames" |
| 3 | Độ phân giải chế độ trong suốt: trang chỉ ghi "chọn độ phân giải và tỉ lệ", không ghi 540p | Đúng (lượt 2) | cùng trang; 540p là số ta đo trên clip thật (`docs/games/vfx/FIREFLY_VFX_LIST.md` §5) |
| 4 | Lượt 1: dùng được tính năng nâng cỡ video của Firefly | **Sai**, lượt 2 tự sửa | helpx "Upscale videos" (16/06/2026) và trang adobe.com `/products/firefly/partner-models/topaz.html`: bộ nâng cỡ video là **Topaz Astra**, model đối tác, cấm theo luật "chỉ model Adobe" |
| 5 | Nâng cỡ ảnh: chọn đúng "Firefly Upscaler" trong danh sách model (bên cạnh Topaz Bloom, Gigapixel) | Đúng một phần | trang upscale-images không mở được bằng công cụ (Akamai chặn); Claude đã dùng "Firefly Upscaler · Adobe models" ngày 03/11 (`browser-ai-tools.md` §5) |
| 6 | Blender 5.0 đổi thuật toán khối (volume) mặc định của Cycles sang null-scattering không lệch | Đúng | developer.blender.org release notes 5.0 Cycles: "unbiased null-scattering", bỏ step size, bật lại bằng Render → Volume → Biased |
| 7 | Pass Vector (Cycles, EEVEE) là chuyển động màn hình 4 thành phần, tắt khi bật Motion Blur | Đúng | Blender 5.2 manual, Render Passes |
| 8 | Lượt 1: pass Vector không cho chuyển động bên trong khối lửa, nên dùng optical flow từ ảnh | Suy luận đúng về pass Vector, **kết luận thực hành sai** | Claude thử 04/11: thuộc tính `velocity` của miền Mantaflow đọc được trong **Cycles** (EEVEE trả 0), cho vector giảm 18 % sai số so với hòa trộn thường; optical flow tự viết chỉ giảm 2 %. Lượt 2 ChatGPT nhận và đổi khuyến nghị |
| 9 | Volume Info có bốn đầu ra Color, Density, Flame, Temperature; `velocity` là lưới riêng, không phải đầu ra của nút | Đúng | Blender 5.2 manual, Volume Info Node; lưới `velocity` đọc được bằng nút Attribute trong Cycles (Claude tự chạy) |
| 10 | Vorticity cao thì nhiều xoáy nhỏ, thấp thì hình mượt; Reaction Speed cao thì lửa ngắn | Đúng | Blender 5.2 manual, Fluid Domain Settings (Gas, Fire) |
| 11 | Klemen Lozar: render vận tốc mô phỏng thành texture vector, không nén, tắt sRGB, bóp méo khung hiện tại và khung sau rồi trộn | Đúng | klemenlozar.com, "Frame Blending with Motion Vectors", 16/03/2015 |
| 12 | ffmpeg `minterpolate` `mi_mode=mci` là nội suy bù chuyển động | Đúng | `ffmpeg -h filter=minterpolate` trên máy |
| 13 | Rayane Saada (80.lv): tia lửa anime bằng lưới, texture cuộn, mặt nạ, xói, mờ mép theo màu đỉnh, khúc xạ | Đúng | 80.lv, 15/03/2024 |
| 14 | Flame Burst (80.lv): flipbook mô phỏng 8×4, rồi phải thêm cấu trúc tự dựng để sửa bố cục; tia lửa là ribbon có khúc xạ và nhiễu cuộn | Đúng | 80.lv, Kirill Anchikov, 20/01/2026 (mô phỏng bằng EmberGen) |
| 15 | RealTimeVFX "Block-ins and Timing": dựng thô bằng hình đơn giản, ảnh xám, shader tối thiểu để lộ lỗi nhịp và bố cục | Đúng | realtimevfx.com/t/29830, 28/10/2025 (bài có quảng cáo khóa học) |
| 16 | Simon Trümpler, "Stylized VFX in RiME": texture đơn giản, méo UV và lưới cho lửa cách điệu | Đúng | trang sự kiện Unreal Fest Europe 2018 (qua tìm kiếm) |
| 17 | Hazel Stagner: đĩa lưới đen đục dưới nhát chém sáng, tia lửa, va chạm vẽ tay | Chưa kiểm | ArtStation chặn công cụ tải; xem bảng của tài liệu chính |
| 18 | Johan Nydahl, Adam Gothard (ArtStation) | Chưa kiểm | như trên |
| 19 | Sheila Stipnieks: xói alpha cho lửa và khói; tác giả tự chê texture tàn lửa | Đúng | đã kiểm 03/11 cho `FIRE_STYLE.md` §2 |
| 20 | Unity Labs flipbook và JangaFX VDB miễn phí là CC0 | Đúng | đã kiểm 01/11 (`docs/games/FREE_ASSET_SOURCES.md` §7, `game-vfx-layered/references/flipbooks.md`) |
| 21 | Six-way lighting: nướng sáng sáu hướng vào hai texture RGBA; có add-on Blender | Đúng | Unity VFX Graph docs (six-way lighting) và blog Unity 20/01/2023 |
| 22 | Riot "Clarity in League" và bài VFX updates: thứ bậc, ít nhiễu, sức mạnh hình theo tầm quan trọng | Đúng | đã kiểm 03/11 (`FIRE_STYLE.md` §2) |
| 23 | MDN: `EXT_disjoint_timer_query` chỉ cho WebGL1, WebGL2 dùng `EXT_disjoint_timer_query_webgl2` (lượt 2) | Đúng | MDN |
| 24 | Adobe khuyên tạo từng âm riêng rồi chồng lớp; có "Voice to sound effects" để dẫn nhịp bằng giọng | Đúng một phần | hướng dẫn prompt âm đã kiểm 02/11 (`game-art-pipeline/references/audio.md` §5.6); trang voice-to-sound chỉ thấy qua kết quả tìm kiếm |
| 25 | Video nền trong suốt chưa được hỗ trợ đầy đủ trong trình biên tập video của Firefly (lượt 2) | Chưa kiểm | không ảnh hưởng: ta cắt và ghép ngoài Firefly |
| 26 | Mọi số giờ làm, ms GPU, MB, ngưỡng thang điểm | Suy luận | ChatGPT tự rút lại ở lượt 2 (mục 8, "What I am withdrawing"); dùng làm điểm xuất phát, phải đo |
| 27 | Lượt 1: Grease Pencil vẽ tay là bước "thiết yếu" | **Không dùng được cho ta**, lượt 2 tự rút | agent không có bút vẽ; lượt 2 thay bằng ảnh AI → mặt nạ → đường cong Blender |
| 28 | Lượt 2: thử ba bản A (clip Firefly đã thích), B (Mantaflow ba nguồn phát), C (hình ba lưỡi từ ảnh + chuyển động hữu cơ), đoán C thắng | Suy luận, Claude đồng ý làm phép thử | tài liệu chính §10 |
| 29 | Lượt 3: viền tối alpha 0,88 khắp viền dễ thành "miếng dán đen"; dùng 0,35–0,75, đứt khúc | Suy luận, Claude nhận | tính tay theo phương trình hòa trộn: nền trắng còn 0,14 ở alpha 0,88 |
| 30 | Lượt 3: lõi alpha thấp không hẳn là cộng sáng (vẫn che nền một phần) | Đúng | kiểm bằng phương trình hòa trộn premultiplied |
| 31 | Lượt 3: tách độ phủ khi xói khỏi alpha hòa trộn | Claude nhận | — |
| 32 | Lượt 3: không giữ khung 12–15 hình mỗi giây cho clip Firefly anh đã thích | Claude nhận | khớp lời anh "mượt, uyển chuyển" |
| 33 | Lượt 3: dải lửa từ Firefly Image không tự liền mạch; phải làm liền offline (dịch nửa ảnh, sửa mối nối, kiểm cột đầu cuối) | Claude nhận | — |
| 34 | Lượt 3: MSDF (`msdfgen`, giấy phép MIT) cho ký hiệu góc nhọn | Đúng một phần | Claude biết `msdfgen` dùng giấy phép MIT, chưa mở lại trang; ghi `THIRD_PARTY.md` khi dùng |
| 35 | Lượt 3: một đèn tiếp xúc dùng chung theo ưu tiên, không đổ bóng; đo chi phí trong cảnh thật | Claude nhận | three.js có `PointLight` |
| 36 | Lượt 3: khói bằng cụm khối cầu, pháp tuyến chuyển bằng Data Transfer | Đúng | Blender manual có modifier Data Transfer chép pháp tuyến |

**Claude không đồng ý ở đâu** (chi tiết ở tài liệu chính §9):
- Lượt 1 đẩy Firefly xuống "tham chiếu chuyển động"; anh đã thích một clip Firefly. Lượt 2 sửa: clip đạt thì là tài sản cuối. Claude theo lượt 2.
- Lượt 1 đề xuất "hai vòng nghiệm thu liên tiếp". Luật của anh là hai giám khảo mù ≥ 8,5 ở bản dựng chơi; không thêm vòng.
- Lượt 2 đề xuất "advect" mặt nạ hình bằng vận tốc mô phỏng (7.2): hay nhưng rủi ro méo hình cao; để sau phép thử A/B/C.

## Lượt 1: câu hỏi (nguyên văn)

```text
I need a deep, practical production analysis, not a pep talk. Please research thoroughly on the web (official docs, GDC/Unite/Blender Conference talks, 80.lv breakdowns, RealTimeVFX forum threads, ArtStation breakdowns by working VFX artists), put a URL behind every key claim, and mark each claim as "checked now", "from memory" or "my inference".

CONTEXT
- Game: a browser game in three.js (WebGL2), xianxia / cultivation theme. A hero commands flying swords; typing words fires skills. Elements: Metal and Fire today, Water and Thunder later. Camera: high three-quarter view. At the play camera a 1.7 m hero is about 64 px tall at 1080p (about 38 px per metre); in close-ups about 250 px per metre. Effects on screen are often only 40-200 px.
- Target look: anime / donghua / Chinese myth, at commercial level: Genshin Impact, Honkai: Star Rail, Wuthering Waves, Zenless Zone Zero, donghua like A Record of a Mortal's Journey to Immortality. Radiant, glistening, luxurious, captivating, with smooth graceful motion; flames "a bit realistic" in motion but stylized in shape and colour. Acceptance: two independent blind judges must both score 8.5/10 or higher, compared to those commercial references, in the real play build.
- Allowed tools only: Adobe Firefly (Firefly Video incl. transparent-background mode, Firefly Image, the Firefly Upscaler, Firefly Generate Sound Effects; Adobe models only, no partner models), Blender 5.x (Mantaflow fire and smoke, EEVEE and Cycles, Geometry Nodes, particles, Grease Pencil, compositor), free CC0 packs (Kenney particles, Unity Labs CC0 flipbooks, JangaFX free VDBs, ambientCG, Screaming Brain noise), images from ChatGPT and Gemini, and our own shader code. Hardware: one Mac mini M4 (no local AI models, no paid tools such as EmberGen, Houdini, Photoshop).
- Runtime budget: our fire layer has about 0.85 ms GPU per frame on a mid laptop; VFX textures per quality tier capped at 8/16/32/48 MB; we prefer at most 2 overlapping transparent layers per pixel inside one effect.
- What we did so far (the owner calls the result "garbage", under 6/10):
  1. Firefly Video clips (5 s, 24 fps, 540p, transparent background or black) cut into 14-16 frame atlases with 256-512 px cells, played at 12-24 fps with plain crossfade between frames. The fire impact is a symmetric "lotus" of 12-15 equal tongues that only scales up and down; edges soft like airbrush; flat orange gradient; wide white core; one camera-facing card in front of the enemy.
  2. Many shapes drawn analytically in shaders: 4-point stars as two crossed diamonds, rings as |length(uv)-r|, coin-shaped round embers that rise like bubbles, radial "wheel spoke" sparks, Voronoi cracks. The owner found the analytic tip star ugly and the shader-drawn sword aura crude, static, with no sparkle.
  3. Alpha taken from luminance on some clips (dim flame = see-through veil), no dark backing behind bright fire on bright stone, no glints, pastel colours to dodge the tone mapper, no bloom on the mid tier.
  4. One flame-trail flipbook made with Firefly Video (soft, smooth moving flame) the owner liked.

QUESTIONS
A. For each effect type below, give: the best tool chain for OUR toolset (which tool makes the source, which makes the motion, what the shader does at runtime), why it beats the alternatives, step-by-step pipeline, runtime representation in three.js (flipbook card, mesh with panning/scrolling textures and dissolve, ribbon/trail, GPU particles, decal, post pass), texture size and frame count, rough GPU cost, and the classic mistakes.
   1) fire impact burst; 2) flame band or sheath wrapping a flying sword blade; 3) sword qi slash and trail; 4) sparks and embers; 5) glints, 4-point stars, twinkles; 6) thin rings, halos, magic seals and sigils; 7) ground cracks, scorch marks, burning ground; 8) smoke; 9) heat distortion; 10) a dragon made of fire or qi that flies along a path.
B. How do studios get smooth motion from flipbooks? Cover: frame counts and playback rates, motion-vector (flow map) frame blending (how to render motion vectors from Blender, how to get them from a Firefly video, the shader math, encoding and pitfalls), sub-frame interpolation, erosion/dissolve over life instead of fading, combining a short flipbook with mesh motion, UV panning and noise distortion so it never looks like a looping GIF. When is a flipbook the wrong tool and a mesh with scrolling textures the right one (how much of Genshin/HSR VFX is mesh + panning texture vs flipbook)?
C. How do they keep a stylized anime look: stepped colour ramps / gradient maps, alpha clip thresholds for crisp edges, dark backing or outline layers behind bright fire, HDR core plus bloom, shape language (S-curves, negative space, big-medium-small), timing (anticipation, impact frame, hold, smear, animating on 2s vs smooth 60 fps), and how to turn a realistic Mantaflow sim or a Firefly clip into that look.
D. Blender recipe, concrete: Mantaflow fire to a seamless or one-shot flipbook. Domain resolution, frame range, flame and smoke settings, Principled Volume / blackbody vs toon ramp shading of density, flame and temperature, EEVEE vs Cycles for volumes, transparent film, orthographic camera at our play angle, render passes (motion vector pass, normal or 6-way lighting for smoke), packing into an atlas, and render times on an M-series Mac. Also: Grease Pencil for hand-drawn anime effects, and Geometry Nodes for stylized mesh fire.
E. Firefly recipe, concrete: what Firefly Video is good and bad at for VFX (consistency, edges, transparency, 5 s length, resolution), prompt patterns that work for game VFX elements, how to cut a clip into a flipbook (choosing frames, cropping, centering, alpha from the matte video, premultiply), whether and how to upscale, how to get a loop, and when to use Firefly Image (for painted masks, glints, seals, crack decals) instead.
F. Quality rubric: concrete, observable criteria that separate 4/10, 6/10, 7/10, 8.5/10 and 9.5/10 for a game VFX at the play camera (silhouette, value hierarchy, edge quality, motion smoothness, timing, colour, layering, sparkle, readability against busy ground, consistency with the game's art). What specific things make a judge say "cheap / mobile / procedural" vs "commercial anime game"?
G. Sound: how to make skill effects feel powerful (layering transient + body + tail, sweeteners, pitch and timing per hit, sync to the visual impact frame, loudness, ducking), and how to make those layers with Firefly Generate Sound Effects (prompt patterns), plus free CC0 sources.
H. Tell us bluntly what we are doing wrong and the order in which to fix it to reach 8.5. Disagree with our assumptions where needed.

FORMAT
- First a decision table: effect type | best tool and pipeline | why | cost (production hours, GPU ms, texture MB).
- Then sections A-H. Use numbers where you can (frame counts, resolutions, thresholds, timings in frames at 60 Hz).
- A source list with URLs, each marked checked now / from memory.
- Do not name or imitate a specific studio's IP in prompts; principles only.
```

## Lượt 1: trả lời của ChatGPT (nguyên văn)

### Production research: Commercial-grade anime / xianxia VFX in three.js

Research date: 4 November 2026 · Target: WebGL2, 60 FPS, approximately 38 px/m at gameplay camera · Metal / Fire now, Water / Thunder later

#### Executive decision table

Primary finding: Your problem is not that you use flipbooks, shaders, or procedural geometry. It is that you are asking each of them to solve the wrong part of the effect.

The strongest practical approach for your game is a hybrid authored-shape pipeline: hand-designed silhouettes and masks, simulated motion where appropriate, animated meshes for directional movement, shader-controlled erosion and colour, and selectively placed particles and glints.

This is supported by actual artist breakdowns. Hazel Stagner's sword-slash effect combines textured disc geometry, an opaque black contrast layer, directional sparks, smoke, and a hand-painted impact. Johan Nydahl's stylized fire uses authored flame shapes with tiling noise and colour variation. Neither relies on one animated card or complex shader mathematics alone. [Checked now] Stylized Sword Slashes+1

##### Recommended production approach

All production times, GPU milliseconds, and memory estimates in this table are my inference, not measured figures or published studio benchmarks. Times assume an experienced technical artist with your existing infrastructure, and exclude large-scale concept revisions.

GPU ranges are approximate incremental effect-rendering costs for a representative active effect on a midrange laptop at 1080p. They are planning envelopes, not guaranteed performance, and cannot simply be added across rows without accounting for overlap, shared passes and simultaneous instances.

| Effect type | Best tool and pipeline | Why | Production / GPU / texture |
| --- | --- | --- | --- |
| 1. Fire impact | Blender Grease Pencil shape design + Firefly Video or Mantaflow motion reference → hand-directed flipbook + mesh shockwave + particles | Strong authored silhouette, organic internal motion, controllable timing | 8–16 h; 0.08–0.22 ms; 4–8 MiB |
| 2. Sword flame sheath | Firefly Video motion reference + Blender blade-conforming mesh + painted scrolling masks | Fire stays attached to sword geometry and responds to movement | 6–12 h; 0.025–0.09 ms; 0.5–2 MiB |
| 3. Sword-qi slash/trail | Grease Pencil painted masks + Blender curved ribbon mesh → UV-scroll, dissolve, tip highlight | Preserves a graceful calligraphic arc rather than a flat glowing streak | 5–10 h; 0.02–0.08 ms; 0.5–2 MiB |
| 4. Sparks / embers | Firefly Image or hand-painted sprite sheet → instanced particles + ballistic motion | Individually controlled paths, scale hierarchy, hot heads and cooler tails | 3–6 h; 0.02–0.08 ms; 0.25–1 MiB |
| 5. Glints / twinkles | Painted 4/6-point sprite masks → timed, instanced screen-aligned particles | Beautiful small highlights without procedural diamond artifacts | 3–5 h; 0.01–0.04 ms; 0.25–1 MiB |
| 6. Rings / sigils | Firefly Image + Blender curve/mesh authoring → UV scrolling, masked reveal and segmented erosion | Precise visual design, sharp linework and repeatable symbols | 5–10 h; 0.015–0.06 ms; 0.5–2 MiB |
| 7. Ground marks | Firefly Image / original painting → packed decal maps + erosion and persistent material state | Designed cracks and scorch morphology rather than generic procedural splats | 6–12 h per family; 0.025–0.12 ms; 1–4 MiB |
| 8. Smoke | JangaFX CC0 VDB or Blender Mantaflow → stylized RGBA flipbook | Natural rolling, curling and dispersion at relatively low runtime cost | 5–10 h; 0.04–0.12 ms; 2–6 MiB |
| 9. Heat distortion | Painted/noise normal or vector field → one shared scene-colour distortion pass | Actual refraction rather than another glowing transparent sprite | 4–8 h infrastructure; 0.06–0.25 ms for a shared pass; 0.25–1 MiB texture |
| 10. Fire/qi dragon | Blender rigged/path-deformed mesh + stylized body textures + ribbons + particles | Coherent anatomy and directional flight; avoids AI-video shape instability | 20–40 h; 0.12–0.35 ms; 4–8 MiB |

Budget implication: Ten independently designed effects are not necessarily ten independent runtime effects. A good asset architecture shares a handful of shaders, masks, particle systems and post-processing infrastructure across the entire skill library.

For your existing 0.85 ms fire-layer GPU allowance, I would initially allocate:

Proposed GPU allocation — fire skill, 0.85 ms ceiling

Core fire + impact

0.28 ms

Sparks, glints, trails

0.16 ms

Smoke and ground mark

0.10 ms

Heat distortion

0.08 ms

Bloom / extra composition

0.13 ms

Safety reserve

0.10 ms

My inference. All shares are adjustable. Bloom and distortion are shared passes: account for them once, not once per effect. The reserve is deliberate.
A key constraint: if 0.85 ms is intended to cover all simultaneously visible fire effects, the hero's sword sheath, multiple impacts, burning ground and dragon cannot each consume their individual row allowance. They must use priority-based spawning and reduced LOD when overlapping.

[Checked now] Unity's documented rendering systems explicitly distinguish linear flipbook blending, motion-vector blending, ribbons, GPU particles and distortion. These are different techniques, not interchangeable ways to obtain a premium result. Unity's free flipbook library is explicitly CC0, and JangaFX's free VDB collection is explicitly CC0. Unity Docs+2

Important production correction: Adobe Firefly's transparent-background Video mode provides a foreground video and a separate alpha video. You should reconstruct alpha from the actual generated matte rather than luminance-keying the coloured foreground. Adobe confirms this export behaviour in its current documentation. [Checked now] Firefly+1

### A. Effect-by-effect production recipes

#### First: Shared technical standards

Before rebuilding any particular effect, establish an asset contract. Otherwise, ten different production methods will produce ten incompatible looks.

Recommended VFX texture standard — [My inference]

| Channel | Standard purpose |
| --- | --- |
| R | Primary silhouette / opacity or directional mask |
| G | Internal pattern / erosion variation |
| B | Secondary highlights / crack depth / special mask |
| A | Dedicated coverage or another specifically documented channel |

Do not force every effect into the same channel meanings. An animated RGBA flipbook may need all four channels for colour and alpha; a ground decal may instead use R = cracks, G = char, B = ember, A = coverage.

Maintain a machine-readable manifest for every asset specifying its channel semantics, colour space, frame layout, UV direction, premultiplication, blend mode and intended size.

Texture memory must be computed from the actual GPU format, not the PNG download size.

| Uncompressed atlas | RGBA8 VRAM | With full mip chain |
| --- | --- | --- |
| 4×4 cells, 128 px | 1 MiB | 1.33 MiB |
| 4×4 cells, 256 px | 4 MiB | 5.33 MiB |
| 8×4 cells, 256 px | 8 MiB | 10.67 MiB |
| 4×4 cells, 512 px | 16 MiB | 21.33 MiB |
| 8×4 cells, 512 px | 32 MiB | 42.67 MiB |

This is exact arithmetic for uncompressed RGBA8 allocations, with approximately one-third additional memory for a complete mip chain.

For mask-only textures, use single-channel storage where supported. Investigate KTX2/Basis Universal compression for larger atlases, but inspect alpha edges after transcoding. Three.js officially supports KTX2/Basis transcoding; actual GPU format depends on device capabilities. [Checked now] Three.js Docs+1

At your game camera, a 1-metre effect occupies about 38 pixels. Therefore:

- A 1.5-metre sword is only approximately 57 pixels long.
- A 0.1-metre detail occupies only 3.8 pixels.
- A 1-metre impact is about 38 pixels wide.
- A 4-metre ground effect is around 152 pixels wide.

[My inference] Designs must prioritize details that occupy at least a few pixels at final resolution. Extremely fine filigree can still be useful as sparse glints, but cannot carry the silhouette or meaning of the skill.

#### A1. Fire impact burst

Reference: [Hazel Stagner — Stylized Sword Slashes](https://glairedaggers.artstation.com/projects/GaGnLQ)

Artist breakdown with contrast geometry, sparks and painted impact texture. [Checked now]

Recommended representation: a deliberately designed one-shot flipbook for the turbulent flame body, plus a fast mesh impact arc and batched sparks.

Do not generate an entire fully finished explosion in Firefly and ask the engine to scale the result. Firefly is better used to create organic internal combustion and interesting flame fragments.

Step-by-step pipeline — [My inference]:

1. Draw three alternative impact silhouettes in Grease Pencil: a lopsided forward explosion, a crescent-shaped impact and a fragmented flame crown.
2. Establish three primary lobes, two secondary lobes, and small independent fragments. The directions should reflect the incoming sword's velocity and contact angle.
3. Obtain organic turbulent motion with Firefly Video or a short Mantaflow simulation. Extract useful individual flames rather than preserving its whole composition.
4. Composite a 24- or 32-frame sequence. Animate the overall silhouette separately from the detailed turbulence.
5. Prepare a compact RGBA flipbook at 256 px per cell, usually 6×4 or 8×4. A 6×4 RGBA8 atlas is 6 MiB before mipmaps.
6. Add one curved mesh that expands rapidly along the ground or contact plane, with a hand-painted arc mask.
7. Spawn 8–20 directional sparks from the hit point, with a mixture of long streaks and smaller flecks.
8. Add an optional dark impact accent behind the core, then dissipate through breakup and outward movement.

Example timing at 60 Hz

| Frames | Event |
| --- | --- |
| −5 to −2 | Brief compression / convergence |
| −1 | Tight bright contact point |
| 0 | Peak impact: compact bright flash |
| 1–3 | Violent asymmetric expansion |
| 4–8 | Flame tongues bend, split and separate |
| 9–17 | Core collapses; outward-moving fragments remain |
| 18–30 | Darker smoke, embers and residue dissipate |

For a repeated typing attack, omit most anticipation and reduce the total duration to roughly 12–20 gameplay frames.

Main correction: the 12–15 equal radial tongues must go. Equal spacing and identical curvature make the effect resemble a decorative flower. The effect should instead contain a dominant directional impulse, obvious empty spaces, and unequal flame masses.

Classic mistakes: a single billboard placed directly in front of the enemy; uniform expansion; broad additive white centres; over-soft edges; excessive smoke hiding the target; sparks with no directional relation to the incoming sword.

The phased design aligns with artist breakdowns of stylized fire attacks and flame bursts. [Checked now] Fire Slash Unity VFX+2

#### A2. Flame band or sheath around a flying sword

Best solution: blade-conforming geometry with animated textures. Not a flipbook card.

A sword sheath must maintain continuity with the weapon even when its orientation changes. A camera-facing card can look correct from one angle but drift, detach or obscure the weapon when the sword turns.

Pipeline — [My inference]:

1. In Blender, make one or two narrow, asymmetrical flame meshes following the blade's length. Think elongated S-shaped sheets, not a cylindrical glowing tube.
2. UV-map the blade direction from hilt to tip. Add edge masks so the flame starts intermittently and breaks into thin tongues.
3. Use the Firefly flame-trail clip that your owner already liked as a reference for motion cadence, curvature and breakup.
4. Derive two seamless masks: one carries large moving flame shapes; another supplies smaller internal movement.
5. In the shader, scroll the masks at different speeds. Distort UVs subtly, then apply an artist-controlled boundary.
6. Tie the sheath's length to the sword rather than the camera. Add one short afterimage ribbon during acceleration.
7. At the exact sword tip, permit a rare 1–2-frame glint or thin hot filament.

Suggested textures: two 256² or 512² masks, perhaps packed together. No multi-frame atlas required.

Suggested animation: one primary flow speed and one slower variation, with gentle phase offsets per sword. Keep the blade visible and recognizably metallic.

Use alpha-clipped edges where appropriate, with a narrow antialias transition. Do not use large semi-transparent orange sheets.

An industry breakdown of character fire hair describes choosing authored alpha cards and panning internal colour rather than relying on expensive fire simulation. The author emphasizes controlling each flame shape and retaining the underlying silhouette. [Checked now] 80.lv+1

Common failure: the fire envelope becomes wider than the sword, so the weapon reads as an orange projectile rather than a magical flying jian.

#### A3. Sword qi slash and trail

Best solution: authored curved ribbon or arc mesh + painted qi mask + animated shader.

Do not rely on procedural rings, triangle fans or straight-line analytic streaks as the final silhouette.

A premium sword-qi attack needs a recognizable gesture. The slash should convey whether the sword cuts, sweeps, pierces, coils or releases a wave.

Pipeline — [My inference]:

1. Draw 3–5 long arc silhouettes in Grease Pencil, using a calligraphic stroke hierarchy: broad entry, thin acceleration region, tapered terminal point.
2. Export a painted grayscale mask with an irregular leading boundary and internal strand channels.
3. Construct a curved mesh from a spline in Blender or dynamically from sampled blade positions in three.js.
4. UV-map distance along the stroke to U and stroke width to V. Use accumulated arc length, not vertex index, so the texture does not stretch unevenly.
5. Scroll one texture along the stroke, distort its internal strands slightly and reveal the arc from one end to the other.
6. Use a dark backing stroke or underlayer just outside the luminous core. This can be a single co-designed material when transparency sorting permits.
7. Emit a small number of moving glints and short detached filaments near the fastest region.
8. Dissolve from the trailing end while the leading portion continues moving.

Recommended assets: two 512×128 or 1024×128 grayscale masks, with a separate 256² fragment sheet if needed. A true flipbook is optional, not central.

Timing recommendation: for a fast hit, form the major slash in 2–4 frames, let it travel for 3–7 frames, then dissolve over 5–10 frames. Longer arcs can extend to 20–30 frames overall.

A studio-level distinction is that the slash's geometry carries the gesture, while the shader carries internal motion.

An artist-produced anime-inspired fire beam breakdown documents mesh shapes, scrolling textures, directional mask reveals, dissolve and phase changes. [Checked now] 80.lv+1

#### A4. Sparks and embers

Reference study: [RealTimeVFX — Know Your Sparks](https://realtimevfx.com/t/know-your-sparks/834)

A thread collecting real-world spark references, useful for trajectory and appearance studies. [Checked now]

Best solution: small hand-painted elongated sprites, instanced particles, and physical or artist-directed trajectories.

Do not render an ember as a circle that moves vertically at constant speed.

Create at least three shapes: a thin hot streak, a teardrop with a clear head, and a tiny irregular cooling fragment.

Suggested particle distribution — [My inference]:

| Property | Primary sparks | Secondary sparks |
| --- | --- | --- |
| Count | 5–10 | 8–20 |
| Visible length | 5–18 px | 1–5 px |
| Lifetime | 5–13 frames | 10–30 frames |
| Behaviour | High initial velocity, deceleration/ballistic arc | Slow falling, curling or drifting |
| Brightness | Brief HDR hot head | Lower-energy yellow/orange/red |
| Trail | Short geometric streak | Usually none |

Spawn most sparks along the contact tangent, with some normal-direction scatter. Add gravity or stylized curvature and individual variation. Do not spawn a mathematically perfect 360-degree wheel.

For more than a few sparks, use a shared instanced geometry and shader. In WebGL2, GPU-driven rendering of particles is easy with instancing; an entirely GPU-resident particle simulation requires additional state-update techniques. Do not confuse WebGL2 particle instancing with Unity VFX Graph compute capabilities.

An efficient implementation stores per-particle birth time, life, initial position, velocity, acceleration, size, seed and colour selection, then derives the visible state from the current clock.

#### A5. Glints, four-point stars and twinkles

Best solution: authored sprite masks.

This is one of the clearest cases where a shader-generated analytic shape can be more work and look worse than a tiny painted image.

Create a glint atlas containing 6–10 variants:

- A fine four-point star with a long vertical axis and short horizontal axis.
- A diagonal asymmetric four-point star.
- A delicate six-point glint.
- A thin horizontal flare.
- An extremely small pinprick.
- A nearly invisible afterglow fragment.

These are shape variations, not copies of the same symmetrical diamond.

Animation — [My inference]: scale from approximately 0.6 to 1.0 to 0.7 across 3–8 frames; peak colour and brightness on one deliberate frame; use a slight rotation or anisotropic scale change. Spawn at curvature changes, blade tips, seal intersections and flame fragmentation points.

Suggested sprite atlas: 256² to 512² RGBA8, with a 2–4-pixel gutter around sprites.

At gameplay scale, most glints should occupy about 3–8 pixels. Hero moments can allow 10–16 pixels.

Do not create a permanent screen full of twinkles. Scarcity is what makes selected highlights feel intentional.

[My inference] A glint should indicate a material edge, energy concentration or meaningful action. Random glitter floating over the whole effect creates visual noise instead of perceived quality.

#### A6. Thin rings, halos, magic seals and sigils

Best solution: carefully authored graphic masks applied to a ground-aligned plane, narrow ring mesh or curved surface.

Analytic circles are acceptable as temporary layout geometry and distance masks. They are not enough to create a premium magical seal.

Pipeline — [My inference]:

1. Design the seal as an actual graphic composition in Firefly Image, your image-generation tools or Blender curves.
2. Separate the graphic into primary stroke, secondary markings and optional highlight channels.
3. Avoid fake written characters. Use a small, consistent set of intentional symbols inspired by your game's cultivation system.
4. Place the seal on a ground-aligned mesh or horizontal plane, with local height offset or depth-aware rendering.
5. Animate a progressive reveal, counter-rotating segments or arc-length travelling highlights.
6. Add limited glints at intersections, and a subtle depth or raised-line impression.
7. Remove sections through a broken-line dissolve, not simultaneous full-opacity fading.

Suggested texture: 512² for an ordinary seal, 1024² for a boss-scale seal or close-up.

At 40–100 px on screen, reduce symbol density aggressively. Four strong, readable structural features will beat 40 subpixel glyphs.

Common failures: perfect concentric circles; hundreds of tiny symbols; all lines glowing equally; repetitive rotation at constant angular velocity; bright seals that obscure enemies.

The staged use of dimensional runes and layered magic geometry is documented in an 80 Level artist breakdown. [Checked now] 80.lv+1

#### A7. Ground cracks, scorch marks and burning ground

Best solution: authored decal masks and a small amount of animated fire.

Do not use Voronoi as the final crack artwork. Use it for generating variations or for auxiliary erosion.

Each damage family needs its own physical logic:

| Ground effect | Visual logic | Required design cues |
| --- | --- | --- |
| Metal cut | A surface was sharply separated | Narrow continuous incision, branching chips, hard directional edges |
| Metal impact | A powerful concentrated blow struck the stone | Compressed centre, unequal radial fractures, lifted stone fragments |
| Fire scorch | Heat spread across and damaged the stone | Irregular burnt perimeter, varying char density, ember seams |
| Burning ground | Persistent flames occupy a damaged area | Charred substrate, separated flame anchors, glow concentrated in cracks |
| Rift | The ground opened along a larger path | Irregular dark interior, offset edges, occasional light from depth |

Pipeline — [My inference]:

1. Begin with an actual ground-damage drawing, not a procedural blob.
2. Produce independent channels for fracture, burned area, hot interior and coverage.
3. Keep the main structural marks wider than about 1 pixel at gameplay resolution; provide a slightly wider dark border around thin bright lines.
4. Align the decal with the ground or surface normals. Use projection only if the relevant depth and normal information is available.
5. At impact, reveal primary cracks quickly from the origin.
6. Let smaller branches propagate with a separate timing mask.
7. For Fire, briefly illuminate selected cracks, then cool to char.
8. Persist scorch or cuts at low visual priority until removed by the game's decal-management system.

Recommended packed texture: 512² RGBA8 per mark family, with a small atlas of variations.

For burning ground, add a separate low-profile flame ribbon or small number of animated cards above the decal. Do not attempt to make the decal itself look three-dimensional through excessive glow.

Adam Gothard's Fire Magic VFX set includes a documented ground-crack detail map with separate channels for cracks, depth and opacity. This is an especially relevant reference for your packed-mask workflow. [Checked now] Fire Magic VFX Set+1

The most important art correction: scorch is not synonymous with a black splat. Cut seams are not synonymous with dotted grey lines. Each ground mark needs its own designed physical form.

#### A8. Smoke

Best solution: a short smoke simulation rendered into an atlas, recoloured and eroded by the runtime shader.

Smoke is one of the relatively few effect types where fluid simulation is often worth the offline cost, because curling volume motion is difficult to reproduce convincingly with naive 2D noise.

Pipeline — [My inference]:

1. Start from one small Mantaflow smoke setup or a permitted CC0 VDB.
2. Choose a large, recognizable plume silhouette, not dense photographic microstructure.
3. Render 16–32 frames from the game-relative viewing direction.
4. Use a stylized grey ramp: dark contact area, medium-value smoke body and lighter edges where needed.
5. At runtime, allow modest expansion and drift while the atlas supplies internal swirling.
6. Erode unevenly through a second mask.
7. Spawn two or three plumes at staggered times only when needed; otherwise use one.

For an ordinary hit, 16 frames at 128–256 px per frame will generally be a better starting point than a large 512 px smoke atlas.

Avoid both excessively additive smoke and broad transparent veils. A good smoke puff generally has stronger opacity in selected body regions and breaks up at the boundary.

[Checked now] The JangaFX collection explicitly licenses its listed free VDB simulations as CC0, including fire plumes and smoke. This permits using those volumes as offline source material without installing or buying EmberGen. Real-Time VFX Simulations

#### A9. Heat distortion

Best solution: one shared, localized scene-colour distortion system.

Do not make heat haze a regular orange translucent card. Real distortion needs to displace samples of the already rendered background.

Pipeline — [My inference]:

1. Generate a small two-channel signed displacement field from packed noise or a stylized animated texture.
2. Render the opaque world, scene geometry and entities whose images should be refracted.
3. Capture or retain that scene-colour buffer.
4. Apply localized distortion through a half-resolution post-processing pass, or through a carefully managed refraction pass with access to the scene-colour buffer.
5. Composite non-refracted bright lines, glints and UI afterward where appropriate.
6. Exclude HUD and typing text.
7. Fade distortion through the effect's lifetime and reduce it aggressively when multiple fire attacks overlap.

Suggested displacement: about 0.5–2 screen pixels for subtle gameplay heat, occasionally 3–5 pixels for a large isolated blast. These values are starting estimates, not physical simulation units.

Design constraint: use a single shared source buffer. Do not copy the entire 1080p screen for each individual flame.

Common failures: excessive waviness, stretching characters, distorted UI, multiple screen-colour captures, and heat distortion that is stronger than the visible fire.

Artist breakdowns of fire beams and stylized fire attacks explicitly use UV distortion/refraction as a supporting effect rather than the entire visual. [Checked now] 80.lv+1

#### A10. Dragon made of fire or sword qi

Best solution: rigged/path-following mesh for the dragon body, with animated materials and selectively added flames, ribbons, whiskers and particles.

This should be treated as a hero asset, not as an enlarged particle sprite.

Pipeline — [My inference]:

1. Design a recognizable long Eastern-dragon silhouette with a distinct head, horns, whiskers, flowing mane and serpentine body.
2. Model or construct a low-poly control body in Blender.
3. Rig with bones or a curve-based deformation system.
4. Animate the head along a spline. Let the spine follow with measured delay, producing a travelling body wave.
5. Use authored masks and scrolling textures to suggest flame or qi moving along the body.
6. Add a controlled flame mane along the dorsal ridge and isolated detached fragments near the body bends.
7. Make the head and torso the primary visual masses. Do not cover the anatomy with turbulent fire.
8. Synchronize acceleration, turn, strike and dissolution with the skill's gameplay events.
9. At the strike, the dragon may separate into one strong directional impact and several flowing afterimages.
10. Dissolve tail-first or fragment into organized qi strands, rather than simply scaling the entire creature to zero.

A 20–40 h production estimate is reasonable only for a stylized gameplay dragon with a reusable path rig, not a cinematic creature with detailed facial animation.

At 38 px/m, size matters: a dragon roughly 5 metres long occupies only around 190 pixels if fully projected across the screen. The head silhouette may be just 20–35 pixels. At this scale, anatomical micro-detail is much less valuable than strong bends, head readability and a clean dark/light separation.

Do not give Firefly Video responsibility for maintaining a dragon's anatomy through arbitrary turns. Use Firefly for motion references and secondary flame details, not the main creature.

### B. How to make flipbooks move smoothly

#### B1. Why your current approach fails

Your current pipeline produces a 14–16-frame atlas from 24 FPS source footage, plays it at 12–24 FPS, and linearly crossfades neighbouring frames.

That is not inherently wrong. The problem is that crossfading two independently evolving flame images creates transparency ghosts, not new motion.

At a moving flame boundary, frame A and frame B may be in different places. A plain blend shows two partially transparent boundaries at once. When the original frames already have soft alpha, the resulting flame becomes even softer.

[Checked now] Unity's technical documentation distinguishes ordinary flipbook frame blending from motion-vector interpolation, and its learning templates explicitly cover optical flow as a way to achieve smoother texture animation. Unity Discussions+1

#### B2. Choose frame count by motion type

Recommended starting values — [My inference]

| Effect | Source frames | Playback | Lifetime | Interpolation |
| --- | --- | --- | --- | --- |
| Small flame impact | 16–24 | 24–30 FPS | 0.25–0.6 s | Linear or flow |
| Main impact turbulence | 24–32 | 24–30 FPS | 0.5–1.1 s | Flow useful |
| Sustained flames | 16–32 looping | 18–30 FPS | Variable | Flow preferred if high quality |
| Smoke puff | 16–32 | 16–24 FPS | 0.5–1.5 s | Linear / flow |
| Hand-drawn slash | 6–12 | 12–30 FPS | 0.15–0.5 s | Often no interpolation |
| Spark / glint | 1–8 | Shader-controlled | 0.05–0.3 s | Usually unnecessary |
| Animated seal | 1–8 or none | Shader-controlled | Variable | Usually unnecessary |

A particular number of frames does not establish quality. Good motion at 12 FPS can be better than badly authored motion at 60 FPS.

Also, distinguish the sampling rate of the recorded flipbook from the overall effect lifetime. A 24-frame flipbook played at 24 FPS lasts one second. If it plays for only 0.35 seconds, it must be retimed, clipped or sampled differently.

#### B3. Motion-vector frame interpolation

Motion-vector interpolation attempts to move the content of one frame toward the next before blending it.

The essential distinction is:

- Linear blending: fades pixel values between two locations.
- Flow-assisted blending: moves those pixel values through the estimated path of the flame.

##### Renderable motion-vector source from Blender

[Checked now] Blender 5.0 has a Vector render pass under View Layer → Passes → Data. It supplies screen-space motion relative to neighbouring frames and is disabled when render motion blur is enabled. Blender describes the pass as containing four components associated with previous and next frame motion. Blender 5.0 Manual

However, a critical qualification:

[My inference based on the pass definition] Blender's Vector pass should not be assumed to produce correct velocity data for the changing interior of Mantaflow flame or smoke. A fluid voxel pattern evolves even when the volume container is stationary. Object-motion vectors and internal fluid advection are different things.

Therefore:

For animated meshes: try Blender's Vector pass, checking which channels are forward and backward and converting its pixel-space displacement into the exact UV convention of your atlas.

For Mantaflow or Firefly flame video: derive apparent optical flow between consecutive rendered images, or omit motion-vector interpolation.

Blender's Vector pass does not automatically turn a generated Firefly clip into flow data.

##### Practical Firefly optical-flow pipeline

[My inference; OpenCV documents the underlying algorithm, not this specific game pipeline.]

1. Export consecutive RGB and alpha frames.
2. Premultiply or composite foreground colour over a stable neutral background for optical-flow estimation. Do not estimate motion from arbitrary changes in transparent RGB.
3. For each frame pair, estimate dense optical flow using the current and next image.
4. Estimate backward flow separately by reversing the image order. Negating forward flow is not an exact substitute near occlusions.
5. Store forward flow for frame A and backward flow for frame B, preferably in a texture atlas aligned with the colour atlas.
6. Normalize motion from frame-pixel displacement to cell UV displacement.
7. Test with a visualized direction field and a checkerboard. Correct the vertical axis convention before shipping.
8. Apply masks at low-alpha pixels and reduce unreliable vectors around newly appearing flames.
9. Clamp unreasonable displacement and use a safe fallback to simple blending where the vector estimates are untrustworthy.

The official OpenCV documentation describes dense optical flow using Farnebäck's algorithm and the resulting per-pixel two-component displacement field. You can implement the relevant estimation offline in permitted custom code if you do not wish to introduce an additional dependency. [Checked now] docs.opencv.org

##### Shader mathematics

Define:

- $C_0$: current colour frame.
- $C_1$: next colour frame.
- $F$: forward flow from frame 0 to frame 1.
- $B$: backward flow from frame 1 to frame 0.
- $t$: fractional interpolation time between 0 and 1.

Then use approximately:

$$ C(t,u) =
(1-t)\,C_0(u-tF(u))
+
t\,C_1(u-(1-t)B(u)) $$

The second term uses the backward flow, which points from the second frame toward the first. Signs must match the convention of the stored vector map.

A compact GLSL-style illustration:

```glsl
vec4 sampleFlowInterpolated(
    vec2 uv,
    float t,
    vec2 flowFwd,
    vec2 flowBack,
    vec4 colorA,
    vec4 colorB
) {
    // colorA and colorB shown here conceptually.
    // In production, resample atlas frames at warped UVs.
    return mix(colorA, colorB, t);
}

// Production sampling concept:
//
// vec2 warpedA = uv - t * flowFwd;
// vec2 warpedB = uv - (1.0 - t) * flowBack;
//
// vec4 A = sampleAtlas(frameA, warpedA);
// vec4 B = sampleAtlas(frameB, warpedB);
//
// vec4 result = mix(A, B, t);
```

This is intentionally a mathematical sketch, not a drop-in complete shader. Real implementation must handle warped sampling, forward/backward masks, image boundaries, alpha and atlas UV gutters.

For encoded 8-bit flow, one possible scheme is:

$$ R = 0.5 + \frac{dx}{2D},
\qquad
G = 0.5 + \frac{dy}{2D} $$

where $D$ is the maximum representable displacement in pixels per source frame. Decode with:

$$ dx = (2R-1)D,\qquad dy=(2G-1)D $$

Then divide by the source cell dimensions to obtain UV displacement.

[My inference] Start with a clamp around ±8–16 pixels per 256-pixel source cell, unless measured source motion requires more. Flow storage could use separate forward/backward RG pairs in RGBA8, but RGBA8 quantization can visibly damage small displacement estimates. Half-float encoding or another representation may be preferable after testing.

##### Where flow interpolation fails

It fails particularly at:

- Newly created flame tips with no corresponding content in the previous frame.
- Flame tongues that merge or divide.
- Strong opacity changes.
- Smoke crossing transparent foreground/background boundaries.
- Low-texture regions with ambiguous movement.
- Clips whose underlying geometry changes inconsistently between frames.

[My inference] You should test motion-vector interpolation on your favourite existing flame-trail clip first. If its flame boundaries become unstable or rubber-like, retain the original sequence and add movement through geometry and UV panning instead.

Do not introduce flow maps for every effect merely because they are technically more sophisticated.

#### B4. Frame interpolation is only one of four motion layers

A high-quality effect can combine four separate movements:

| Layer | Responsible for | Example |
| --- | --- | --- |
| Object / mesh animation | Overall trajectory | Sword moves 6 metres along an arc |
| Vertex / ribbon animation | Silhouette and deformation | Slash extends then curls |
| UV / shader animation | Internal flow | Flame streaks race along the blade |
| Flipbook animation | Complex local changes | Fire tongues split and fold |

[Checked now] These combinations are documented in working artists' pipelines, including stylized fire, Rime fire studies, and layered anime fire beams. VFX + Breakdown+2

#### B5. Erode instead of simply fading

A long uniform opacity fade makes a flame resemble a translucent image that disappears.

A useful shader formulation is:

$$ M = \operatorname{smoothstep}
\left(d-w,\ d+w,\ A-kN\right) $$

where $A$ is the authored shape mask, $N$ is erosion noise, $d$ is an animated threshold, $k$ controls breakup, and $w$ defines transition softness.

As lifetime progresses, increase $d$, causing the visible flame to break into smaller islands.

My suggested starting values are normalized $d=0.15$ to $0.85$, $k=0.15$ to $0.4$, and $w=0.02$ to $0.08$, adjusted for the underlying mask distribution.

These are [My inference], not universal thresholds.

Sheila Stipnieks' stylized fire breakdown explicitly presents an alpha-erosion material for fire and smoke. [Checked now] sheilastipnieks.artstation.com

Crucially, don't apply identical erosion to every effect. Metal qi may separate along flowing strands; Fire may fragment at flame tips; Smoke may soften and disperse without high-contrast holes.

#### B6. When not to use a flipbook

Use meshes with scrolling textures when the effect:

- Must adhere to a sword or character.
- Must stretch between arbitrary positions.
- Must change length dynamically.
- Must follow a curved path.
- Must face multiple camera angles.
- Must run for an indefinite lifetime.
- Has a recognizable geometric structure such as a seal, arc or energy sheath.

Use flipbooks when:

- The internal motion is chaotic, organic and hard to synthesize convincingly.
- The effect is short or naturally looping.
- The view angle is fixed or restricted.
- The rendered simulation provides useful complexity at small pixel sizes.
- Its shape need not respond to arbitrary deformations.

On Genshin Impact and Honkai: Star Rail: I cannot substantiate an exact percentage of mesh/scrolling-texture effects versus flipbooks from publicly verified engine data. I would not cite a claim such as “80% mesh VFX” without source files, tool documentation or a developer presentation establishing that figure.

What is documented is that commercial real-time VFX workflows routinely combine textured meshes, flipbooks, scrolling UVs, shaders and particles. [Checked now] 80.lv+2

For your own project, I would plan roughly 60–70% of reusable effect families around meshes, ribbons and shader-driven masks, 20–30% around flipbooks, and the remainder around decals and post effects. [My inference] That is an architecture proposal, not a measurement of another game's content.

### C. Achieving the stylized anime / donghua look

#### C1. Silhouette should be decided before shaders

[Checked now] In the RealTimeVFX discussion Block-ins and Timing, Jason Keyser describes deliberately using simple geometry, grayscale, uncomplicated textures and minimal shaders to expose problems in composition and timing. The point is to prevent visual polish from concealing an effect that is structurally weak. Real Time VFX

This is the correct order for your production.

An effect should first pass as an untextured moving black-and-white shape. If a fire impact looks like a flower at this stage, no expensive shader will fix it.

Use a shape hierarchy:

| Level | Function | Example for fire impact |
| --- | --- | --- |
| Big | Primary directional gesture | One dominant flame mass |
| Medium | Secondary rhythm | Two or three curved flame branches |
| Small | Energy and finish | Tiny flame fragments, sparks, pointed tears |
| Negative space | Separates forms | Visible gaps between major tongues |

[My inference] Design the dominant mass to occupy roughly 50–65% of the effect's visual emphasis, secondary masses 25–35%, and the remaining accents about 10–15%. These are composition guides rather than literal pixel-area requirements.

For xianxia specifically, I would favour long directional S-curves, thin tapered qi strands, asymmetric crowns and controlled ornamental details. Avoid overusing serrated explosion spikes, comic-style radial bursts and identical lobes.

#### C2. Use colour ramps, not flat orange gradients

A convincing stylized flame needs variation in both hue and luminance, plus a clear distinction between the bright core and the body.

Proposed Fire colour hierarchy — [My inference]

Dark outer edge / char
Thin hot energy core
The palette is a proposal, not a sampled commercial game's palette.

Map the underlying flame intensity or designed grayscale mask through a ramp. The relationship should not be a uniform fade across the sprite.

Possible implementation:

- Dark reddish-brown or near-charred colour for selected exterior regions.
- Saturated red-orange through the main flame body.
- Warm yellow-orange concentrated along travelling internal folds.
- Cream or near-white only for very thin energy concentrations and contact points.

Use a 1D lookup texture, perhaps 256×1 pixels, for a consistent shared colour ramp. That allows Metal, Fire, Water and Thunder to share much of the same motion architecture while preserving different visual identities.

Do not force everything into pastel colours just to survive tone mapping. Fix the HDR and tone-mapping pipeline.

#### C3. Edge quality: crisp does not mean binary

A premium stylized effect often contains several edge qualities within one shape:

| Edge treatment | Suitable use |
| --- | --- |
| Sharp, antialiased contour | Sword qi, fire tongue silhouette, graphic seal |
| Narrow soft edge | Internal fire transitions, secondary glow |
| Broken or eroded edge | Flame breakup, smoke dissipation, damaged ground |
| Tiny luminous filament | Very hot core, cutting edge |
| Dark outer accent | Separation against bright stone |

[My inference] For 40–200 px effects, begin with a soft-edge transition of approximately 0.5–1.5 output pixels for key graphic contours. Use derivative-aware antialiasing such as `fwidth()` for procedural thresholds when available.

For example:

```glsl
float threshold = 0.5;
float aa = max(fwidth(mask), 0.001);
float coverage = smoothstep(
    threshold - aa,
    threshold + aa,
    mask
);
```

This is preferable to a fully hard `discard` threshold for most small moving contours.

A narrow edge is different from a broad airbrush feather. The former preserves the shape; the latter destroys it.

#### C4. Dark backing behind luminous energy

Your effects lack dark backing on bright stone. That is a substantial visual-design problem, but the solution is not to add a black border around every flame.

[Checked now] Hazel Stagner's slash breakdown explicitly describes a black opaque disc mesh drawn beneath the bright slash geometry to create contrast. An artist's technique is being cited here, not a claim that it is universally appropriate. Stylized Sword Slashes+1

For your game, choose backing by effect type:

- Metal sword qi: narrow indigo/ink under-stroke, especially at the leading and outer edge.
- Fire: a broken dark red-brown edge, scorched inner gaps or darker trailing filaments.
- Glints: usually no opaque backing; create separation using local brightness and contrast.
- Ground cracks: a strong dark incision with a much thinner inner light.
- Smoke: larger low-value masses, without an obvious painted outline.

The dark backing should preserve the material or energy identity. A uniformly black cartoon border may be equally wrong for your art direction.

#### C5. HDR, bloom and tone mapping

[Checked now] Three.js documents `UnrealBloomPass` and its brightness threshold, and recommends `OutputPass` for final tone mapping and colour-space conversion in post-processing. It also documents that image colour textures and non-colour data textures require different colour-space treatment. Three.js Docs+2

Recommended architecture:

Scene + VFX in linear HDR

Bright core → bloom extraction

Preserved scene colour + shapes

Composite → tone map → sRGB output

[My inference] Start with a bright-emission threshold around 1.0–1.5 in linear HDR units, where 1.0 corresponds to reference display white, and tune to your actual scene exposure and tone mapper. There is no universal bloom threshold.

Treat luminance and saturation as separate design choices.

The flame body should not bloom heavily. Reserve the strongest bloom contribution for thin cores, impact contacts and a small number of glints.

If the mid tier cannot afford full bloom, a carefully constrained small blurred-core approximation may work. But it should not turn every large orange shape into a low-contrast translucent cloud.

Important: measure whether the complete HDR+bloom pipeline fits your 0.85 ms budget. A stock multi-mip bloom pass is not automatically inexpensive just because it is part of Three.js.

#### C6. Timing: animation on twos versus smooth 60 FPS

There is no requirement that every individual visual component update at the same temporal cadence.

A stylized attack may combine:

| Component | Recommended cadence |
| --- | --- |
| Sword trajectory | Smooth every frame at 60 FPS |
| Ribbon geometry | Smooth 60 FPS |
| Internal flame flow | 24–60 FPS equivalent |
| Hand-drawn slash silhouette | 12–24 distinct drawings per second |
| Sparks | 60 FPS trajectory |
| Glints | Deliberate 2–8-frame pulses |
| Impact flash | Often just 1–2 frames |
| Camera impulse | One short, controlled event |

[My inference] Use stepped drawings only where a held anime pose adds impact. A sword's actual position and collision timing should remain smooth and gameplay-consistent.

A particularly useful combination is a 12-drawing-per-second stylized slash texture carried by a smoothly moving ribbon. That creates an authored graphic cadence without making the sword movement stutter.

Blender Studio's Cowboi NPR production discusses the problem of ordinary 3D motion revealing 3D parallax in anime-style shots. Blender Conference talks likewise cover mixing 2D drawing, 3D geometry and controlled shading. These are artistic precedents for deliberate motion treatment, not direct evidence about a specific game engine. [Checked now] Blender Studio+2

#### C7. Turn realistic source motion into stylized motion

For Mantaflow or Firefly source, use this transformation:

Organic source: turbulence, curl and flow

Select recognizable large flame masses

Simplify detail and impose directional silhouettes

Quantize colour and concentrate highlights

Hand-correct timing and edge breakup

Bake texture data; animate geometry in engine

The output should not resemble a realistic fire video with an orange-to-red filter applied. Shape simplification and motion direction have to change as well.

[Checked now] Simon Trümpler's Unreal Fest presentation on stylized VFX explains the use of simple textures, UV distortion and geometry-based methods for fire, smoke and water. A 2026 80 Level report also describes an NPR fire workflow using Blender EEVEE, mesh work and painterly compositing while retaining selected realistic cues. Unreal Engine+1

### D. Concrete Blender 5.x production recipe

#### D1. When I would use Mantaflow

Use Mantaflow to produce organic reference motion for fire, smoke, plumes and some explosion interiors.

Do not choose Mantaflow as the default authoring tool for:

- Sword qi slashes.
- Decorative fire tongues attached to moving swords.
- Thin rings, sigils or star glints.
- Stylized geometric energy outlines.
- Coherent dragons.

Those are better authored with geometry and graphic masks.

Blender 5.0 still documents gas domains, fire/smoke flows, resolution divisions, adaptive domains, noise refinement and fire reaction settings. [Checked now] Blender 5.0 Manual+3

#### D2. Mantaflow fire flipbook: working starter configuration

All numeric settings below are proposed test values, not Blender defaults or official performance benchmarks.

| Setting | Prototype | Higher-quality candidate |
| --- | --- | --- |
| Domain dimensions | Approximately 3×3×3 m | Tight fit to intended plume |
| Resolution Divisions | 64 | 96–128 |
| Fluid type | Gas | Gas |
| Flow | Fire + Smoke or Fire | Depends on desired output |
| Cache | Modular | Modular |
| Simulation length | 48 frames | 72–96 frames |
| Simulation FPS | 24 | 24 |
| Noise refinement | Off initially | Enabled after base motion passes |
| Adaptive domain | On with safe margin | On unless cropping occurs |
| Render resolution | 256–512 square | 512–1024 for source |
| Rendered source frames | 24 | 24–48 |
| Runtime atlas frames | 16–24 | 24–32 |

##### Build procedure

1. Create a constrained emitter. Start with a small mesh shaped like the desired emission source. For impact fire, use an irregular cluster or directional arc, not a perfect sphere.

2. Create a Gas domain. Keep it only as large as necessary to contain the movement. The official manual explains that the domain's longest dimension determines voxel subdivision, so unnecessary volume dramatically wastes resolution. [Checked now] Blender 5.0 Manual

3. Configure the fire source. Use a brief burst of fuel, with initial velocity reflecting the intended impact direction. Blender's Flow documentation provides controls for fuel and initial velocity. [Checked now] Blender 5.0 Manual

4. Tune the simulation without rendering. First inspect overall motion at 64 divisions. Adjust emitter shape, force direction, temperature influence, vorticity and reaction speed.

5. Tune fire length. Blender's manual states that higher Reaction Speed produces shorter flames because fuel burns faster; lower values can produce longer flames. [Checked now] Blender 5.0 Manual

6. Enable adaptive domain carefully. Keep enough margin to avoid cropping rapidly moving flame tips. [Checked now] Blender 5.0 Manual

7. Bake base simulation, then enable gas noise refinement if the motion needs detail. Noise refinement adds finer structure without requiring the entire underlying base simulation to increase in resolution. [Checked now] Blender 5.1 Manual+1

8. Render the sequence as individual EXR or RGBA PNG frames. Do not render directly to a delivery video, because you need control over alpha, timing and the atlas.

9. Post-process the result into stylized shape and luminance masks.

10. Pack the chosen frames using Blender's compositor, Video Sequencer and Blender Python API.

#### D3. Shading flame, density and temperature

Blender's `Principled Volume` includes density, scattering, emission and blackbody controls. The `Volume Info` node also exposes flame and temperature information from a smoke domain. [Checked now] Blender 5.0 Manual+1

Produce at least two distinct candidate renders:

Candidate A — Realistic motion, stylized post-processing. Render flame with a controlled Principled Volume / blackbody setup. Extract a high-dynamic-range flame image, then simplify it with curves, thresholds, colour ramps and hand corrections in Blender's compositor.

Candidate B — Stylized masks directly. Use flame/density-related volume information to drive a limited set of brightness or colour regions, instead of aiming for physically accurate colour. This may require custom volume shading and is more involved than simply connecting `Volume Info.Flame` to a surface emission node.

For both variants, create an explicit alpha representation. Do not assume that emission brightness is equivalent to coverage.

A useful channel design for a flame atlas is:

| Channel | Interpretation |
| --- | --- |
| R | Flame body / colour-mask intensity |
| G | Hot core / concentrated emission |
| B | Small structural variation / erosion |
| A | Overall coverage |

Alternatively, if the RGB channels contain fully authored flame colours, store coverage in alpha and derive other shader controls from a separate packed map.

[My inference] For most 40–200 px gameplay effects, the carefully processed mask-based version is more likely to fit your visual style and runtime budget than a physically shaded volume replayed unchanged.

#### D4. EEVEE versus Cycles

| Requirement | EEVEE | Cycles |
| --- | --- | --- |
| Fast iteration | Prefer first | More expensive |
| Smoke/fire volume previews | Supported | Supported |
| Stable stylized graphic output | Good starting point | Possible, usually unnecessary |
| Complex volume lighting | Limited/approximate relative to path tracing | Stronger physically based option |
| Multiple realistic scattering effects | Less suitable | More suitable |
| Authoring small flipbook masks | Usually preferred | Often excessive |

[Checked now] Blender documents volumetric rendering in EEVEE and Cycles, with separate quality controls and limitations. Blender 5.0 also introduced an updated default volume-rendering algorithm in Cycles, so older tutorials describing only the previous ray-marching settings may be outdated. Blender 5.0 Manual+2

##### M4 render-time estimates

I have not benchmarked your Mac mini M4. The following are [My inference] as rough planning scenarios, not measurements:

| Task | Plausible early planning range |
| --- | --- |
| 64-division, short gas simulation | Several minutes to tens of minutes |
| 96–128-division simulation | Tens of minutes or longer |
| Simple 512² EEVEE volume render | Seconds to tens of seconds per frame |
| Complex 512² Cycles volume render | Tens of seconds to several minutes per frame |
| 32-frame production atlas | Minutes to hours, depending on scene and bake |

A simulation is a separate cost from rendering. Domain resolution, simulation forces, enabled noise, smoke complexity, volume quality and thermal throttling can move these estimates substantially.

At 16 GB unified memory, avoid using your maximum simulation resolution while simultaneously running multiple heavy development environments.

More important than the render estimate: a 128-division simulation does not automatically yield a better 128-pixel screen-space flame than a 64-division simulation. Judge the rendered, reduced image.

#### D5. Camera setup

Use an orthographic camera for standard flipbook extraction when you need stable sizing.

For a world-facing effect, orient the camera to match the game's actual three-quarter view. Avoid treating the user's stated camera pitch as an automatically correct camera Euler rotation; establish the game camera transform and reproduce it.

For camera-facing particles, a directly front-facing render may be better.

[My inference] Maintain two bake camera presets:

| Preset | Purpose |
| --- | --- |
| `VFX_PLAY_CAMERA` | Ground-plane and world-oriented effects |
| `VFX_BILLBOARD_CAMERA` | Smoke puffs, fire interiors and camera-facing sprites |

Keep the camera fixed throughout a flipbook. Do not introduce unnecessary camera motion into the source footage.

#### D6. Transparent film, passes and premultiplication

[Checked now] Blender has a transparent film setting and supports rendering sequences in RGBA PNG or OpenEXR. Blender's image documentation distinguishes straight alpha from premultiplied alpha. Blender 5.0 Manual+2

Recommended internal authoring format: linear EXR for high-quality intermediate frames.

Recommended delivery format: RGBA8 or appropriate packed masks, with a documented alpha convention.

For premultiplied colour:

$$ RGB_{\text{premult}} = RGB_{\text{straight}}\times\alpha $$

Compositing then uses:

$$ C_{\text{out}}=C_{\text{premult}}+(1-\alpha)C_{\text{background}} $$

Do not premultiply twice. Do not save premultiplied data and configure the runtime as though it were straight-alpha data.

For coloured fire against bright ground, test both straight and premultiplied workflows. Choose one consistent convention for the engine and ensure transparent texels have suitable edge colour to avoid filtering halos.

#### D7. Blender motion vectors and six-way lighting

##### Motion-vector export

Use View Layer → Passes → Data → Vector, with render motion blur disabled, for geometry where the pass is meaningful.

Save the vector data in multichannel EXR and inspect frame order, sign convention and units before atlas packing.

Do not treat the vector pass as guaranteed internal fluid flow. For a pure volumetric plume, test optical-flow estimation from rendered frames instead.

##### Six-way lighting for smoke

The idea is to bake how the same volume responds to illumination from different directions, then reconstruct approximate lighting in the runtime.

A custom Blender method:

1. Fix the simulation and camera.
2. Render six directional light configurations representing +X, −X, +Y, −Y, +Z and −Z in a documented local basis.
3. Keep exposure and other scene conditions identical.
4. Store the six responses in two RGB textures or another packed representation, plus opacity.
5. In the runtime shader, derive nonnegative directional weights from the local lighting vector.
6. Combine weighted responses to approximate lighting.

The Unity VFX Toolbox documents a Blender six-way lighting texture baker as part of its DCC tools. This is evidence of a real production technique, not a recommendation to install Unity, which is outside your permitted toolset. [Checked now] GitHub

For your project I would not introduce six-way smoke lighting initially. Six directional texture datasets increase memory and texture reads, and your smoke puffs are small. A prelit grayscale atlas with one or two stylized shading controls is a better baseline.

Reserve six-way lighting experiments for close-ups or large persistent smoke.

#### D8. Grease Pencil and Geometry Nodes recipes

Grease Pencil is essential for your style, even if you are not an experienced animator.

Blender officially documents frame-by-frame drawing, keyframed strokes and onion skinning. Blender Conference talks cover production workflows combining Grease Pencil and Geometry Nodes. [Checked now] Blender 5.0 Manual+2

Recommended production uses:

| Grease Pencil | Geometry Nodes |
| --- | --- |
| Author sword-qi contour | Generate ribbon mesh from curves |
| Draw important flame key shapes | Distribute controlled flame strips along sword |
| Make 4–8 slash key poses | Create procedural variations of authored geometry |
| Design hand-drawn sparks | Construct repeated seal geometry |
| Add frame-specific speed lines | Displace dragon/body ribbons along paths |
| Paint dark accent strokes | Assign attributes for shader control |

For a stylized flame, draw a graceful centreline, convert or recreate it as a curve, generate a tapered strip along it, assign UVs from distance along the curve and animate the material flow.

That gives you controlled geometry with fluid internal movement, without requiring a complete volumetric simulation.

### E. Adobe Firefly: practical production recipe

#### E1. What Firefly Video is good and bad at

[Checked now] Adobe documents the Firefly Video model with a default 5-second duration and 24 FPS, and documents selectable generation resolutions such as 540p, 720p and 1080p in relevant workflows. Transparent-background output is supported with the Firefly Video model. Firefly+2

| Good uses | Poor uses |
| --- | --- |
| Organic flame motion | Exact 16-frame animation designed to repeat |
| Fire trails and curling tongues | Precise topology or sword attachment |
| Smoke movement references | Perfect graphic seal linework |
| Organic turbulent fragments | Stable dragon anatomy and 3D orientation |
| Fast visual exploration | Accurate per-pixel flow vectors |
| Mood and broad shape exploration | Reliable 1–2-pixel opaque edges |

The failure modes in the right column are my inference, based on the needs of deterministic game assets, not Adobe's own claims about limitations.

#### E2. Prompt design for VFX assets

Your prompts should describe a source asset, not a whole cinematic scene.

##### Fire impact motion source

Writing
An isolated magical fire-impact burst for a real-time fantasy game VFX source sheet. One fast directional ignition from the centre, with three dominant asymmetric flame masses, two smaller curling flame tongues and a few detached burning fragments. Strong elegant S-curve motion, organic turbulent folding, sharp readable flame tips, saturated deep orange and warm red with very thin concentrated hot highlights. No symmetric radial flower, no identical petals, no circular wheel, no diffuse fog, no smoke cloud, no floating coins, no wide white core. Fixed camera, centred composition, clean separation from the background, complete effect visible within the frame, no scenery, no characters, no weapons, no text. A single ignition that expands, breaks apart and dissipates.

##### Flame-trail motion source

Writing
An isolated long, thin magical flame ribbon flowing horizontally from left to right, for use as a game VFX motion reference. Graceful continuous S-curve flow, several narrow trailing filaments, naturally curling flame tips, sparse detached hot fragments, organic turbulence inside the ribbon, a clear leading edge and gradual tail breakup. Rich orange-red fire, thin yellow-hot streaks, sharply designed silhouette with subtle organic motion. Fixed camera, no camera movement, no scenery, no characters, no weapons, no text, no large central fireball, no smoke veil. The ribbon remains slender and directionally coherent throughout.

##### Smoke motion source

Writing
An isolated small stylized impact-smoke plume for a real-time fantasy game. Dense charcoal-grey smoke rises from a compact irregular base, folds into two or three large rolling curls, expands asymmetrically and breaks into smaller wisps. Distinct readable masses, restrained internal turbulence, no photographic micro-detail, no fire, no sparks, no explosions, no ground, no background scenery, no objects, no text. Fixed camera and fixed scale, complete smoke plume visible throughout, clean foreground separation.

[My inference] Generate several candidates and select primarily for motion character. Do not choose the smoothest or brightest clip automatically.

#### E3. Recover true alpha from Firefly Video

Use the separate foreground and alpha video supplied by transparent-background generation.

[Checked now] Adobe explicitly states that the download ZIP contains a primary foreground video and an alpha video. Firefly

In Blender:

1. Import the foreground video and alpha video.
2. Match their frame rates, start frames and resolution.
3. Convert the alpha video to a grayscale mask if necessary.
4. Set foreground alpha from that mask using the compositor.
5. Inspect the result against black, white, grey and your actual stone courtyard.
6. Export an RGBA image sequence.
7. Check for edge contamination, matte flicker and incorrect premultiplication.

If using a black-background clip with no alpha, a luminance key is only a fallback. It cannot reliably reconstruct opacity for dark red or low-luminance flame edges.

Do not assume that every Firefly transparent output has perfect mattes. Inspect it frame by frame.

#### E4. Cut the footage into a flipbook

Your clip's 120 frames do not all belong in the atlas.

[My inference] Selection process:

1. Identify actual ignition, active expansion, breakup and decay.
2. Cut away long pre-roll and empty end footage.
3. Select a coherent sequence of 16–32 frames, maintaining consistent temporal spacing where possible.
4. If retiming substantially, process the sequence in Blender rather than picking arbitrary frames according to appearance.
5. Reframe around a stable effect origin, especially the point of impact.
6. Preserve natural large-scale movement. Do not align every frame by centring the brightest flame blob, because that can remove useful motion.
7. Reserve 4–8 pixels per cell as a starting gutter for a 256-pixel tile, using edge dilation or suitable padding.
8. Pack into the atlas, then generate mips and test cross-frame sampling.
9. Inspect the result at the exact runtime pixel size.

For a 24-frame sequence at 256², a 6×4 layout uses a 1536×1024 atlas. The result consumes about 6 MiB RGBA8 before mipmaps.

[My inference] Keep the origin fixed for an impact and let the silhouette move around it. For a looping flame, select a motion segment with relatively stable overall mass instead.

#### E5. How to make a loop

A Firefly-generated clip is not necessarily a seamless loop even when it has a fairly stable appearance.

Try three approaches in order:

First choice: use a one-shot whenever the effect has a defined beginning and end. Most impacts should not loop.

Second choice: use a stable 16–32-frame segment and move the internal material independently from its geometry.

Third choice: create an actual looping source by blending a short overlap region between the end and beginning, then hand-correcting the most visible seams.

Check for a matching silhouette, compatible motion direction, similar value distribution, and no sudden jump in the flame core.

Do not treat crossfading the last and first frames as sufficient proof of seamlessness.

#### E6. Upscaling: when it helps

[Checked now] Adobe documents a Firefly Upscaler for images with 2× and 4× scaling. Adobe separately provides video upscaling with 1080p and 4K targets and enhancement/detail controls. These are distinct features. Firefly+1

For your game:

- Do not upscale a 256-pixel source merely to generate a bigger atlas that will be rendered at 80 pixels.
- Upscale when you need to recover a clear contour before making a final painted mask.
- Use the least creative enhancement available when preserving an existing silhouette is important.
- Validate that an upscaled version has not changed the original flame identity or introduced shimmer.
- Do not upscale foreground and alpha independently without inspecting their correspondence.

[My inference] For source frames already around 540p, producing clean 128–256 px gameplay flipbook cells through careful cropping and processing is often a more useful investment than further generative upscaling.

#### E7. When to use Firefly Image instead

Use Firefly Image for assets where static graphic design matters more than temporal coherence: ground marks, glints, magic symbols, crack decals, qi strokes, ornamental energy motifs and flame silhouettes.

Recommended pattern: generate multiple grayscale or flat-colour candidates, select by silhouette, then manually clean or reconstruct the final asset using Blender, Grease Pencil or custom mask processing.

Do not expect a generated grayscale image to automatically be a production-ready mask. It may have inconsistent edges, faint halos, unwanted shadows and unintentional detail.

For cracks specifically, paint or refine the main branch structure by hand rather than accepting random branches simply because the image looks detailed.

### F. Quality rubric: what actually separates 4/10 from 9.5/10?

First, a critical distinction: a technically advanced effect is not necessarily an artistically successful effect.

An effect using motion vectors, HDR, six-way lighting, three scrolling masks and GPU particles can still look like a cheap asset-pack spell. Conversely, a carefully designed ribbon with one excellent texture and eight perfectly timed sparks can look commercially convincing.

[Checked now] Riot Games' published VFX principles explicitly emphasize conveying gameplay, preserving hierarchy and minimizing visual noise. Its VFX-update documentation also describes reducing unnecessary fine texture detail and matching perceived visual power to gameplay importance. League of Legends+1

#### F1. Observable quality levels

The following rubric is [My inference]. It is a proposed production review system, not an official grading scale from any commercial studio.

| Score | Observable appearance | Typical problems |
| --- | --- | --- |
| 4/10 | Clearly a particle, sprite or shader demonstration rather than a designed skill | Symmetry, featureless gradients, abrupt motion, bad alpha, simple geometric primitives |
| 6/10 | Recognizable and functional, sometimes attractive in isolation | Repetitive shapes, weak silhouette, flat colour, incomplete layering, poor fit to environment |
| 7/10 | Designed silhouette and reasonably polished motion | Some generic details, inconsistent sparkle, weak contact, insufficient art-direction coherence |
| 8.5/10 | Cohesive, deliberate and convincing at gameplay size; strong sense of energy and material | No major visual failure; timing, hierarchy, edges and secondary details cooperate |
| 9.5/10 | Exceptional composition and execution; strong identity; beautiful motion even under scrutiny | Very few visible weaknesses; nearly every component contributes to the effect's meaning |

The important threshold is between 7 and 8.5.

At 7/10, an evaluator can appreciate the effort and explain what the effect is trying to achieve. At 8.5/10, the design feels like a finished part of the game's visual language rather than an assemblage of techniques.

#### F2. Weighted evaluation

Proposed scorecard — [My inference]

Interactive VFX scoring worksheet

Adjust each category from 0 to 10

### 6.00/10

Below proposed score threshold

Silhouette and composition (20%)

6.0

Clear gesture, asymmetry, negative space, big-medium-small hierarchy
Motion and timing (20%)

6.0

Smooth spatial motion, powerful impact, graceful follow-through
Shape and edge quality (15%)

6.0

Designed contours, clean alpha, no airbrush mush or unwanted pixelation
Colour and value hierarchy (15%)

6.0

Rich controlled palette, readable hot core, no clipping or flat gradient
Layering and contact (10%)

6.0

Effect belongs to sword, target and ground; impact has physical consequence
Sparkle and secondary motion (10%)

6.0

Intentional glints, sparks, particles and small-scale variation
Gameplay readability (5%)

6.0

Readable target, action and direction during simultaneous effects
Art-direction consistency (5%)

6.0

Matches the xianxia world rather than looking like a generic fantasy asset
This weighted score is a useful diagnostic tool, but I would not let it override a critical failure. For example, an effect with 9/10 colour but 5/10 gameplay readability should fail your acceptance gate regardless of its calculated average.

#### F3. Cheap versus commercial: specific visual signatures

| Evaluator says | Likely underlying defect | What to examine |
| --- | --- | --- |
| “Looks like a mobile-game effect” | Flat billboard or generic particle-sheet composition | Silhouette, camera-facing card, lack of spatial interaction |
| “Looks procedural” | Perfect circles, repeated symmetry, analytic stars | Authored masks and geometric irregularity |
| “Looks blurry” | Weak alpha, excessive crossfade, large soft transitions | Source matte, contour width, frame blending |
| “Looks like a sticker” | No depth/contact relationship | Ground intersection, contact shadow, directional impulse |
| “Looks like an animation GIF” | Entire shape loops/scales identically | Independent mesh, UV and particle motion |
| “Looks like paint or ink” | Wrong shape morphology for fire/scorch | Flame contour, soot and fracture logic |
| “Not powerful” | Weak impact timing or no sonic weight | Peak frame, anticipation, sound transient |
| “Too chaotic” | Every element simultaneously competing | Hierarchy, peak separation, particle density |
| “Not luxurious” | No selective highlights, material character or visual rhythm | Concentrated glints, fine accents, contrast |
| “Looks pretty but doesn't fit the game” | Inconsistent artistic language | Character, sword, ground and environment integration |

These are my diagnostic inferences, not verified quotations from players or judges.

The RealTimeVFX fireball critique provides a useful real example: artists call out visual inconsistency between sharp and soft fire components, as well as an overly clean central silhouette compared with a more turbulent trail. [Checked now] Real Time VFX

#### F4. Formal acceptance protocol

You have two independent blind judges and require both to score at least 8.5/10. I recommend the following test protocol.

Production acceptance configuration — [My inference]

| Test | Conditions | Pass criterion |
| --- | --- | --- |
| Gameplay scale | Native 1080p, actual game camera | Primary skill readable without zoom |
| Bright background | Light stone courtyard | Bright and dark parts distinguishable |
| Dark background | Shadowed stone or darker area | Silhouette remains differentiated |
| Single effect | One target, no other effects | Form, timing and contact are clear |
| Crowd stress | 20–50 enemies and overlapping attacks | Target, skill direction and important UI readable |
| Motion | 60 FPS capture of real build | No distracting judder, frame ghost or edge shimmer |
| Contact accuracy | Compare VFX contact with registered hit | Preferably within ±1 frame, after accounting for intended anticipation |
| Texture quality | Actual low/mid/high asset settings | No obvious aliasing, matte fringe or atlas bleeding |
| GPU | Midrange laptop and chosen quality tier | Respect 0.85 ms fire budget in defined representative and stress conditions |
| Judge independence | Same anonymized video/build, no labels or coaching | Both judges independently score ≥8.5 |

A valid test must include both a controlled clip and the real gameplay build. A polished, isolated VFX turntable is not enough.

I would also require two consecutive acceptance rounds with both judges passing. If either judge fails, identify the failed dimension, revise the effect, and restart that consecutive-pass count.

Be careful about source-camera differences. A cinematic reference at 4K close-up is not a fair direct resolution comparison with a 60-pixel-tall character in a browser game. Compare composition, motion, colour and perceived quality at equivalent screen occupancy.

### G. Sound design: making skills feel powerful

#### G1. The three-part impact

A powerful hit rarely depends on one loud sound.

The useful structure is:

Suggested 60 FPS impact sound timeline — [My inference]

Illustrative timing diagram, not a measured audio waveform. Different skills need different envelopes.
Transient: the sharp 5–40 ms onset that communicates actual contact. This may be a metallic click, hard crack, snap or brief explosive pulse.

Body: approximately 60–250 ms of the event's material and mass. For fire, a rushing combustion burst; for Metal, a resonant blade-force impact.

Tail: roughly 100–700 ms of residual movement, decaying energy, scattering sparks or environment response.

These are practical starting values [My inference]. They should not all peak at the same moment.

#### G2. Firefly Generate Sound Effects production

[Checked now] Adobe recommends generating one sound at a time and layering separate sounds for greater control. Its Voice to sound effects feature can use a recorded performance to guide timing and energy. The updated Firefly audio tools also support arranging sound effects in timeline-based workflows. Firefly+2

For your game, generate three separate assets for a single skill.

##### Fire impact transient

Writing
A single very short, powerful fantasy fire-impact crack. Sharp dry ignition snap with a compact explosive attack and immediate decay. Dense close-up energy, controlled high-frequency detail, no sustained roar, no reverb, no echo, no music, no voices, no secondary impacts. One isolated transient, suitable for layering at the exact contact frame of a sword skill.

##### Fire impact body

Writing
One concentrated burst of rapidly expanding magical combustion. Deep forceful rushing flame with a textured turbulent body, strong initial pressure and controlled natural decay. A dense whoosh followed by a brief hot flame roar. No multiple explosions, no environmental ambience, no long echo, no music, no voices. One isolated game sound effect.

##### Fire tail / sparkle

Writing
A short scattering tail of fine hot sparks and tiny burning fragments cooling in the air. Delicate rapid crackles with a few brighter individual ticks, irregular natural timing, clear detailed transients, gradually fading. No hollow metallic resonance, no glass chimes, no large explosion, no background ambience, no reverb, no music, no voices.

For Metal sword qi, replace the fire body with a directional blade-pressure or compressed-air release, and the transient with a sharp metallic/energy contact.

Do not use the same explosion transient on every sword hit. Create several meaningful variation families.

#### G3. Audio runtime in a browser

The native Web Audio API is sufficient for your layering and voice-management requirements.

[Checked now] MDN documents sample playback, gain control, playback-rate changes, filters and dynamic compression through the Web Audio API. MDN+2

Recommended design:

| Bus | Content | Behaviour |
| --- | --- | --- |
| `typingBus` | Keyboard / command input | Highly consistent, low latency |
| `weaponBus` | Sword travel and launch | Directional and relatively restrained |
| `impactBus` | Contact transients | High priority, short duration |
| `elementBus` | Fire, Thunder, Metal, Water bodies | Element-specific character |
| `sweetenerBus` | Sparkle, qi glints, small resonance | Low volume, selectively triggered |
| `musicBus` | Music | Controlled ducking on major events |
| `masterBus` | Final output | Headroom and peak management |

[My inference] Use scheduled `AudioBufferSourceNode.start(when)` calls when event time can be predicted. For unpredictable typing hits, trigger the audio from the same authoritative gameplay event that activates the contact VFX, then measure audible latency in the browser/device.

Do not depend on a video frame export timestamp if that frame does not align with the actual combat hit.

##### Suggested audio mixing rules

- Maintain several dB of bus headroom before the master stage.
- For a major ultimate, try 3–6 dB of music ducking over a short attack/recovery envelope.
- For routine hits, reduce simultaneous voice count rather than making every sound loud.
- Try small pitch/playback-rate variation, perhaps ±3–6%, while avoiding obviously robotic or comically detuned effects.
- Cap simultaneous near-identical sweetener voices.
- Preserve the attack transient of the most important hit when many enemies are struck together.
- Use compression sparingly; a flattened waveform makes repeated hits tiring.

All settings here are [My inference] and need listening tests. There is no reliable universal loudness target for every short fantasy-game SFX.

For horde combat, aggregate collisions intelligently. One prominent impact transient and several quieter, spatially distributed secondary sounds can convey multiple kills better than ten identical full-volume explosions.

#### G4. Free CC0 sound libraries

| Source | Licence verified | Best use |
| --- | --- | --- |
| [Kenney Impact Sounds](https://kenney.nl/assets/impact-sounds) | CC0, checked now | Hard contacts, clicks, material hits |
| [Freesound](https://freesound.org/) | Individual files vary; use only verified CC0 uploads | Fire, whooshes, cracks, impacts |

Kenney's Impact Sounds page explicitly lists 130 files and CC0. Freesound's official FAQ explains its CC0, CC-BY and CC-BY-NC licensing distinctions, so the site itself must not be treated as entirely CC0. Kenney+1

The Sonniss GDC bundles are also worth distinguishing: they are freely downloadable and royalty-free, but not CC0. Under your strict CC0-only asset rule, I would exclude them unless that policy changes. [Checked now] SONNISS+1

For AI-generated sound effects, Adobe describes commercial use of released Firefly features as permitted under its guidelines. Keep the generation metadata and check the particular feature's current beta status and terms. [Checked now] Adobe Firefly+1

### H. What is wrong and what to fix first

#### H1. Diagnosis of the current fire pipeline

Based on your description, I agree that the existing result can plausibly fail a commercial-art comparison. I have not inspected the current build, so this is a diagnosis of the specified defects rather than an independent visual score.

1

The silhouette was never properly art-directed

Your symmetric lotus fire with equal tongues is fundamentally a weak combat-impact shape. It is decorative, not directional. This has greater impact on quality than whether the source uses 16 or 32 frames.

2

The fire is treated as an animated image rather than a constructed event

One billboard in front of the enemy cannot supply meaningful ground contact, direction, depth, residual damage and secondary motion.

3

Source alpha and colour handling are damaging the shape

Luminance-derived alpha makes darker flame colours look transparent. Soft footage plus frame crossfading makes the contour softer again.

4

Too much of the visual identity is mathematically generic

Perfect circles, diamond stars, evenly radial sparks and Voronoi cracks are useful mathematical ingredients but poor substitutes for authored shape language.

5

The colour and HDR hierarchy are not controlled

Pastel colours used to dodge the tone mapper, broad white centres and missing bloom remove the sense of concentrated hot energy.

6

Secondary events are missing or weak

The absence of purposeful glints, sparks, smoke and residual ground interaction makes impacts feel isolated and inexpensive.

7

Your testing seems concentrated on making individual assets rather than final gameplay compositions

An attractive flipbook preview or a high-resolution close-up does not establish that an effect looks commercial when the hero is 64 pixels tall.

#### H2. Assumptions I would reject

| Assumption | My assessment |
| --- | --- |
| “More frames will make Firefly effects premium” | Incorrect. Better motion sampling cannot repair bad shape design. |
| “Motion-vector blending is the main fix” | Incorrect priority. Useful after source shape and alpha are already good. |
| “Blender Mantaflow will automatically look more expensive” | Incorrect. Realistic turbulence can make an effect less stylized. |
| “A shader is cheaper and therefore should generate most shapes” | Often wrong. A sampled 256² authored mask may be simpler, cleaner and cheaper than elaborate fragment mathematics. |
| “Every flame needs a dark outline” | Wrong. Contrast support must match the material and visual direction. |
| “A large white core means a powerful explosion” | Usually wrong. Concentrated white contact can be powerful; broad clipped white regions lose shape. |
| “Commercial quality needs many simultaneous layers” | Wrong. It needs a strong hierarchy; two carefully composed overlapping transparent layers can outperform six. |
| “No bloom on mid tier is always necessary for performance” | Unproven. Measure a small shared half-resolution bloom solution first. |
| “Firefly Video should make the whole final VFX asset” | Wrong for many categories. It is usually more useful for organic motion than precise graphic design. |
| “All effects must be smooth at 60 FPS” | Wrong. Gameplay movement should be smooth, while selected hand-drawn components can use deliberately held frames. |

All assessments in this table are my inference, informed by the checked artist and official technical references throughout this report.

#### H3. Recommended implementation order

I would not attempt to rebuild all ten effect types simultaneously.

Production roadmap — [My inference]

| Priority | Work | Estimated effort | Required evidence before moving on |
| --- | --- | --- | --- |
| P0 | Save controlled baseline captures and profiling | 0.5–1 day | Current quality and cost recorded |
| P1 | Rebuild one fire impact silhouette and timing | 1–2 days | Silhouette accepted in grayscale |
| P2 | Correct alpha, premultiplication, colour handling | 0.5–1 day | No matte or tone-map defects |
| P3 | Add ground-contact geometry and dark contrast | 0.5–1 day | Reads on light and dark stone |
| P4 | Replace sparks and glints with authored sprites | 0.5–1 day | Clear hierarchy at gameplay scale |
| P5 | Add proper audio layers and synchronize contact | 0.5–1 day | Impact feels forceful with sound on |
| P6 | Optimize and test simultaneous effects | 1–2 days | GPU/VRAM/overdraw budget passes |
| P7 | Blind quality review | 0.5 day per round | Both independent judges ≥8.5 |
| P8 | Reuse approved systems for other VFX families | Per family | Art consistency and regression pass |

This is approximately 5–9 focused working days for one polished fire-impact family, assuming an experienced developer/artist and no major redesign of engine architecture. It is not a guaranteed delivery time.

If the silhouette fails at P1, do not advance to motion-vector blending, high-resolution simulation or complex post-processing.

#### H4. One experiment that can validate the whole approach

Make three deliberately different versions of the same fire impact, using the same source duration and the same performance budget.

| Candidate | Pipeline | What it tests |
| --- | --- | --- |
| A | Existing Firefly flipbook + corrected alpha, contrast and timing | Whether existing assets can be salvaged |
| B | Authored mesh/ribbon silhouette + scrolling masks + sparks | Whether mesh-led VFX is better suited to your game |
| C | Authored silhouette + short organic flipbook interior + mesh contact + sparks | Whether a hybrid approach is genuinely superior |

Use identical lighting, target, background, impact position and camera framing.

Do not label versions by implementation method when showing them to the judges.

##### What I expect

[My inference] Candidate C is most likely to reach the target for a major impact, while B may be equally good for repeated low-cost attacks. A may improve considerably but will probably continue showing the limitations of a single flat card.

That prediction must be tested; the expensive-looking option should not win automatically.

#### H5. Asset architecture for Claude to implement

I recommend separating artistic assets from their runtime presentation.

Skill event / gameplay contact

Effect Timeline Controller

Spawn, intensities, phase timings, priorities, LOD
Ribbon / mesh effects

Flipbook player

Instanced sparks / glints

Ground decal system

Shared distortion / bloom

Sound event mixer

Quality tier + GPU/VRAM budget manager

A skill definition should not hardcode a unique shader system for every ability.

A compact configuration might resemble:

```JSON
{
  "skillId": "fire_sword_impact",
  "element": "fire",
  "qualityPriority": "high",
  "durationMs": 480,
  "phases": [
    {
      "name": "contact",
      "atMs": 0,
      "emit": ["contact_flash", "impact_transient"]
    },
    {
      "name": "expansion",
      "atMs": 16,
      "emit": ["fire_core", "impact_arc", "sparks"]
    },
    {
      "name": "residue",
      "atMs": 115,
      "emit": ["smoke", "ground_scorch"]
    }
  ],
  "budgets": {
    "maxTransparentOverlap": 2,
    "allowSharedDistortion": true,
    "allowSharedBloom": true
  }
}
```

This is an architectural example, not a claim that such a file is already compatible with your existing engine.

The system should also record actual concurrent instance counts, texture residency and post-processing cost. A two-transparent-layer limit per pixel does not by itself guarantee low overdraw over the whole screen.

#### H6. Production quality tiers

The goal should not be to make a 48 MB tier look premium while the 8 MB tier remains crude. All tiers must share the same fundamental art direction.

Proposed texture residency allocation — [My inference]

| Resource family | 8 MiB | 16 MiB | 32 MiB | 48 MiB |
| --- | --- | --- | --- | --- |
| Fire/organic flipbooks | 4.0 | 7.0 | 14.0 | 21.0 |
| Sword trails/sheaths | 1.0 | 2.0 | 4.0 | 6.0 |
| Ground masks/decals | 1.0 | 2.0 | 4.0 | 6.0 |
| Sparks, glints and seals | 1.0 | 2.0 | 4.0 | 5.0 |
| Smoke/noise/shared masks | 1.0 | 3.0 | 6.0 | 10.0 |
| Total | 8.0 | 16.0 | 32.0 | 48.0 |

These are planning allocations for GPU texture residency, not file download sizes; actual textures need fitting, compression and mip budgeting to remain within each cap.

Tier differences should mostly affect secondary density, flipbook resolution, smoke quality and post-processing. They should not replace the approved silhouette with a substantially worse one.

### Verified sources and production references

The following URLs were opened or retrieved through web research during this response. Checked now means the retrieved page exists and contains the relevant documentation or description; it does not mean I ran the software, downloaded every asset, measured the performance or watched every minute of linked videos.

From memory: No external factual claims in the source inventory below are presented as memory-only. The proposed thresholds, hours, GPU costs, architecture, art choices and quality scores are independently identified as my inference throughout.

#### Official documentation and technical references

| Source | What it supports | Status |
| --- | --- | --- |
| [Adobe — Transparent video](https://helpx.adobe.com/firefly/mobile/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html) | Foreground + alpha export, model and controls | Checked now |
| [Adobe — Video transparency](https://helpx.adobe.com/ie/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html) | Default duration/FPS, alpha workflow | Checked now |
| [Adobe — Video upscaling](https://helpx.adobe.com/ca/firefly/web/work-with-audio-and-video/work-with-video/upscale-videos.html) | Upscale settings and targets | Checked now |
| [Adobe — Image upscaling](https://helpx.adobe.com/firefly/web/edit-images/prompt-to-edit/upscale-images.html) | Firefly Upscaler and 2×/4× options | Checked now |
| [Adobe — Sound prompt guide](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-audio/writing-effective-text-prompts-for-sound-effects-generation.html) | Isolated sound generation and layering | Checked now |
| [Adobe — Voice-to-sound effects](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-audio/voice-to-sound-effects.html) | Timing and intensity guidance | Checked now |
| [Adobe — Generative AI usage FAQ](https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html) | Commercial usage conditions | Checked now |
| [Blender 5.0 — Fluid domain](https://docs.blender.org/manual/en/5.0/physics/fluid/type/domain/settings.html) | Resolution, fire reaction, baking | Checked now |
| [Blender — Adaptive domain](https://docs.blender.org/manual/en/5.0/physics/fluid/type/domain/gas/adaptive_domain.html) | Domain adaptation | Checked now |
| [Blender — Render passes](https://docs.blender.org/manual/en/5.0/render/layers/passes.html) | Vector, normal, depth and volume passes | Checked now |
| [Blender — Principled Volume](https://docs.blender.org/manual/id/5.0/render/shader_nodes/shader/volume_principled.html) | Density, emission, blackbody controls | Checked now |
| [Blender — Cycles volumes](https://docs.blender.org/manual/en/5.0/render/cycles/render_settings/volumes.html) | Updated volume settings | Checked now |
| [Blender — Grease Pencil animation](https://docs.blender.org/manual/en/5.0/grease_pencil/animation/introduction.html) | Frame-by-frame animation | Checked now |
| [Three.js — UnrealBloomPass](https://threejs.org/docs/pages/UnrealBloomPass.html) | Bloom threshold and mip processing | Checked now |
| [Three.js — OutputPass](https://threejs.org/docs/pages/OutputPass.html) | Tone mapping and output transform | Checked now |
| [Three.js — Colour management](https://threejs.org/manual/pages/color-management.html) | Linear RGB, sRGB and HDR formats | Checked now |
| [Three.js — KTX2Loader](https://threejs.org/docs/pages/KTX2Loader.html) | GPU texture compression support | Checked now |
| [OpenCV — Optical flow](https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html) | Dense optical-flow principles | Checked now |
| [MDN — Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) | Browser audio implementation | Checked now |
| [MDN — GPU timer queries](https://developer.mozilla.org/en-US/docs/Web/API/EXT_disjoint_timer_query) | Asynchronous GPU timing principles | Checked now |

#### Working artists, developer presentations and breakdowns

| Source | Production insight | Status |
| --- | --- | --- |
| [Hazel Stagner — Sword Slashes](https://glairedaggers.artstation.com/projects/GaGnLQ) | Dark backing, textured discs, sparks, impact composition | Checked now |
| [Hazel Stagner — Electric Impact](https://glairedaggers.artstation.com/projects/Nx3qW1) | Hand-painted electricity, ribbons, painted crack SDF | Checked now |
| [Johan Nydahl — Stylized Fire](https://johannydahl.artstation.com/projects/GemQgW) | Dual tiling noise, shape masks, colour variation | Checked now |
| [Sheila Stipnieks — Stylized Fire](https://sheilastipnieks.artstation.com/projects/D5oPoA) | Smoke/fire texture and alpha-erosion breakdown | Checked now |
| [Adam Gothard — Fire Magic](https://agothard.artstation.com/projects/oAwa9w) | Packed ground-crack channels, cohesive effects | Checked now |
| [Unreal Fest — Stylized VFX in RiME](https://www.unrealengine.com/events/unreal-fest-europe-2018/stylized-vfx-in-rime?lang=es-ES) | UV distortion, simple texture/mesh approaches | Checked now |
| [Blender Conference — Stylized Visuals](https://conference.blender.org/2024/presentations/3870/) | Blender anime/NPR production talk | Checked now |
| [Blender Conference — Comic Style in 3D](https://conference.blender.org/2026/presentations/4146/) | Hand-drawn lines, Geometry Nodes, Grease Pencil | Checked now |
| [Blender Studio — Cowboi](https://studio.blender.org/blog/cowboi/) | NPR/anime camera and 2D/3D treatment | Checked now |
| [RealTimeVFX — Block-ins and Timing](https://realtimevfx.com/t/block-ins-and-timing/29830) | Grayscale, simplified timing validation | Checked now |
| [RealTimeVFX — Panning Fire](https://realtimevfx.com/t/campfire-using-panning-textures/20165) | Critique of shape, movement and noise scale | Checked now |
| [RealTimeVFX — Know Your Sparks](https://realtimevfx.com/t/know-your-sparks/834) | Spark motion reference collection | Checked now |
| [80 Level — From Realism to Stylization](https://80.lv/articles/from-realism-to-stylization-game-vfx-production) | Shape simplification, meshes, UV tricks | Checked now |
| [80 Level — Stylized Fire Beam](https://80.lv/articles/using-unreal-engine-to-make-an-anime-inspired-stylized-fire-beam-vfx) | Authored mesh, panning masks, phase staging | Checked now |
| [80 Level — Flame Burst](https://80.lv/articles/creating-a-flame-burst-effect-using-unreal-engine-5) | Ribbons, noise, refraction, secondary particles | Checked now |
| [Riot Games — Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/) | Readability, visual hierarchy, noise control | Checked now |
| [Riot Games — VFX Updates](https://www.leagueoflegends.com/en-us/news/dev/dev-behind-the-scenes-of-vfx-updates/) | Readability, thematic consistency and power hierarchy | Checked now |
| [GDC Vault — The VFX Toolkit](https://gdcvault.com/play/1029417/Visual-Effects-Summit-The-VFX) | GDC session covering composition and effects techniques; session overview verified, not the full presentation | Checked now |

#### Free asset sources and licences

| Source | Verified licence | Status |
| --- | --- | --- |
| [Unity Labs — Free flipbooks](https://unity.com/blog/engine-platform/free-vfx-image-sequences-flipbooks) | CC0 | Checked now |
| [JangaFX — Free VDBs](https://www.jangafx.com/software/embergen/download/free-vdb-animations) | CC0 for the listed free VDB simulations | Checked now |
| [Kenney — Particle Pack](https://kenney.nl/assets/particle-pack) | CC0 | Checked now |
| [Kenney — Impact Sounds](https://kenney.nl/assets/impact-sounds) | CC0 | Checked now |
| [ambientCG](https://ambientcg.com/) | CC0 | Checked now |
| [Screaming Brain Studios — Noise](https://screamingbrainstudios.itch.io/noise-texture-pack) | CC0 | Checked now |
| [Freesound — Licence FAQ](https://freesound.org/help/faq/) | Per-file; CC0 exists alongside other licences | Checked now |

For production, maintain a licence manifest with source URL, asset name, author, exact licence, date checked, original downloaded file and any modification notes. Do not assume an entire marketplace or artist portfolio is free because one individual asset is CC0.

#### Final production recommendation

The most important change is to stop organizing work around which tool can generate an impressive flame and start organizing it around which motion and graphic elements the final skill requires.

For your game, I would make the next fire impact from one authored main flame shape, one organically animated interior, one directional contact arc, a small set of deliberately designed sparks/glints, a ground response and synchronized three-layer sound. Keep the design within the two-overlapping-transparent-layers preference, sharing geometry and post passes where sensible.

Do not start by adding motion vectors, a 128-division simulation, six-way lighting or more HDR bloom. First make the impact beautiful in grayscale at 80–150 pixels wide. Then make its movement convincing, then its colour, then its sparkle and sound.

The decisive experiment is authored mesh versus improved flipbook versus hybrid, blind-rated in the actual game camera under the same GPU budget. That will tell you which production route is genuinely worth scaling across the remaining skills.

Nothing in the verified source material guarantees an 8.5/10. The process above is designed to make the quality problems visible, measurable and correctable instead of repeatedly generating assets and hoping one happens to look commercial.

## Lượt 2: câu hỏi tự rà soát (nguyên văn)

```text
Thank you. Before we use this, please self-review it carefully (search again where needed):

1. Reopen every link you cited and confirm it exists and says what you claim. Mark each one verified, partly verified, unsupported or wrong, and drop or correct anything that fails. In particular re-check: (a) the Firefly transparent-background mode's actual output resolution (we observe 540p, 16:9, 24 fps, 5 s), (b) whether Firefly's video upscaling runs on an Adobe Firefly model or on a partner model such as Topaz (we may only use Adobe models), (c) your claim that Blender 5.0 changed the default Cycles volume rendering, (d) the Volume Info node and the attribute names a Mantaflow domain exposes (density, flame, temperature, velocity?).

2. Challenge our results. We ran a small test tonight on the Mac mini M4 with Blender 5.2.2 headless:
   - Mantaflow fire burst, 128 divisions, 48 frames: bake plus render took 3.5-4.5 minutes in total. EEVEE renders of 256 px frames take about 0.2 s each.
   - We rendered data, not colour: pass 1 = emission-only volume (flame as grey heat), pass 2 = absorption-only volume (soot plus flame as coverage in alpha). A stepped 6-colour ramp and a crisp alpha threshold in post gave a clean dark-rimmed toon fire, but the shape is still a turbulent "explosion blob", not designed curved tongues.
   - Motion vectors: EEVEE does not expose the fluid "velocity" attribute (all zero), Cycles does. Rendering velocity projected to camera right/up as emission, divided by a weight pass, gave per-pixel vectors. Using every second frame as the flipbook and the frames in between as ground truth: Lozar-style MV blending cut the in-between error by 18% versus a plain crossfade (best scale found by search; wrong sign made it worse). A naive numpy Lucas-Kanade optical flow on the rendered frames gained only 2%. ffmpeg minterpolate (mi_mode=mci, offline in-betweens) cut the error by 26%.
   Do these results change any of your recommendations? You said the Vector pass cannot give fluid motion and suggested optical flow; the velocity-attribute route seems to work. What would you change?

3. Our producer is an AI agent, not a human artist. It cannot hand-draw in Grease Pencil with a tablet. Rewrite the parts of your pipeline that assume hand drawing (silhouettes, slash key poses, sigils, crack art) so they work with what the agent can actually do: Firefly Image, ChatGPT and Gemini images (masks and paintings), Firefly Video, Blender Python (curves, Geometry Nodes, Mantaflow, forces, renders), and shader code. Be concrete: how does the agent get a designed, beautiful flame silhouette with 3 curved tongues and negative space into a flipbook or a mesh?

4. How do we get anime flame TONGUES (not a turbulent blob) out of Mantaflow specifically: emitter shapes, guide forces, vorticity, coarse voxels, noise, dissolve, buoyancy, camera, and post (dilate, threshold, ramp)? Give a concrete parameter starting set.

5. The owner liked one Firefly Video flame-trail flipbook (soft, smooth, a bit realistic motion) and called our code-drawn shapes "garbage". You suggest Firefly mostly as motion reference. Reconcile: when is a Firefly clip the final asset, and when only a reference?

6. Add strong options you missed, then give a short corrected final list of decisions (effect type -> tool chain), marking what changed after this review.
```

## Lượt 2: trả lời của ChatGPT (nguyên văn)

### VFX production pipeline — critical self-review and corrections

Audit: 4 November 2026 · Blender 5.2.2 on Mac mini M4 · Adobe-only models inside Firefly · three.js/WebGL2

#### 1. Four critical findings

Your experiments change my recommendations substantially. In particular, my previous assessment of Blender's practical value, simulated-fire motion vectors and Firefly's role in producing finished assets was too conservative.

| Disputed claim | New verdict | Correction |
| --- | --- | --- |
| Firefly transparent video resolution and format | Partly verified | Adobe confirms Firefly Video, default 24 FPS, 5 seconds, separate foreground and alpha video. Your observed 540p, 16:9 output is valid evidence for your current workflow, but I have not found an official statement proving this is a universal maximum. |
| Adobe Firefly video upscaling | Wrong recommendation | Firefly's video upscaler uses Topaz Astra, a partner model. It is not permitted under your Adobe-model-only restriction. |
| Blender 5.0 changed default Cycles volume rendering | Verified | Blender 5.0 introduced unbiased null-scattering volume rendering as the default, with the previous biased ray-marching mode still selectable. |
| Blender Vector pass cannot provide fluid motion | Partly verified, but my practical conclusion was incomplete | The conventional render Vector pass should not be assumed to describe internal flame advection. However, your successful Cycles render of the Mantaflow `velocity` attribute supplies a separate, useful route to fluid motion vectors. |

##### Firefly: actual mode and limits

Adobe's transparent-background instructions explicitly state that the Firefly Video model must be selected, that unsupported settings are hidden when transparency is enabled, that the default frame rate is 24 FPS, and that the default duration is five seconds. It describes choosing resolution and aspect ratio but does not enumerate all combinations available in transparent mode. [Checked now] Firefly

Therefore the correct production assumption is:

Use 540p, 16:9, 24 FPS, 5 seconds as the verified configuration of your existing Firefly transparent clips, based on your actual test. Do not assume a 1080p transparent export is available merely because standard Firefly Video generation supports higher resolutions.

##### Firefly video upscaling: exclude it

Adobe's own [Topaz Astra information](https://www.adobe.com/products/firefly/partner-models/topaz.html) identifies Astra as the integrated video upscaler. Its [Video Quality Enhancer](https://www.adobe.com/products/firefly/features/video-quality-enhancer.html) explicitly identifies it as a partner model. [Checked now] Adobe+2

The distinction matters:

- Firefly Upscaler, specifically selected in the image upscaling model dropdown: allowed.
- Topaz Bloom / Gigapixel image upscaling: excluded.
- Topaz Astra video upscaling: excluded.
- Blender offline resampling and filtering: allowed.
- Firefly Video generation using the Adobe Firefly Video model: allowed.

Adobe separately lists Firefly Upscaler and the two Topaz options for image upscaling. [Checked now] Firefly

My previous answer should not have suggested Firefly video upscaling as an unrestricted production tool.

##### Blender 5.0 volume rendering: confirmed

Blender's [official Cycles 5.0 release notes](https://developer.blender.org/docs/release_notes/5.0/cycles/) explicitly confirms the new default null-scattering algorithm and the optional older biased ray-marching algorithm. [Checked now] Blender Developer Documentation+1

This statement was correct. What needs correction is the practical implication: for your asset production, it is the measured Blender 5.2.2 bake and render speed that matters, not general speculation about expensive volumetric rendering.

#### 2. Your Mac mini M4 results change the production priorities

These are your measured figures, not figures I independently benchmarked.

128-division simulation + render

### 3.5–4.5 min

48-frame burst
EEVEE

### 0.2 s

Per 256 px frame
MV versus crossfade

### −18%

Reconstruction error
Your reported interpolation comparison:

Reported in-between reconstruction error
Normalized: plain crossfade = 100. Lower is better. Measurements supplied by user, not independently reproduced.

0%
25%
50%
75%
100%
Crossfade
Lucas–Kanade
Fluid velocity MV
FFmpeg MCI
- Crossfade: Relative error 100%
- Lucas–Kanade: Relative error 98%
- Fluid velocity MV: Relative error 82%
- FFmpeg MCI: Relative error 74%

This is useful evidence, but one distinction is essential: lower frame reconstruction error is not equivalent to higher perceived VFX quality. A method can reduce pixel error while producing unstable edges, doubled tongues, unstable matte boundaries or softened details.

Nevertheless, your results support three changes immediately.

First: Blender simulation is now a strong default candidate for organic fire motion, not merely an expensive fallback. Your hardware makes rapid parameter searches practical.

Second: promote fluid-velocity-based motion-vector blending to the primary experimental route for Blender-simulated fire, provided the velocity data is correctly weighted, projected and aligned. Optical flow becomes a fallback or comparison method, rather than the preferred first option.

Third: use your FFmpeg interpolation as a leading baseline. It currently wins your reported in-between reconstruction test by 26%, versus 18% for velocity-based MV. Do not ignore that result merely because velocity maps are theoretically more physically meaningful.

The next decision is not “which interpolation algorithm sounds more advanced?” It is whether FFmpeg MCI, calibrated fluid MV or the original full-rate sequence looks best in motion at 40–200 pixels, and whether the resulting atlas fits the texture budget.

#### 3. Blender 5.2.2: confirmed volume data and the motion-vector correction

##### 3.1 Which data exists?

The [Blender 5.2 Volume Info documentation](https://docs.staging.blender.org/manual/en/latest/render/shader_nodes/input/volume_info.html) specifies four outputs. Blender's developer documentation separately describes the named volume grids, including `velocity`. [Checked now] Blender 5.2 LTS Manual+1

| Data | Access method | What it means | Verdict |
| --- | --- | --- | --- |
| `Density` | Volume Info output; `density` Attribute/grid | Smoke density | Verified |
| `Flame` | Volume Info output; `flame` Attribute/grid | Fire intensity/density | Verified |
| `Temperature` | Volume Info output; `temperature` Attribute/grid | Normalized temperature field | Verified |
| `Color` | Volume Info output; `color` Attribute/grid | Simulated smoke colour | Verified |
| `velocity` | Named vector volume grid through Attribute node or volume-data access | 3D simulated fluid velocity | Partly verified — documented grid, with successful Cycles access demonstrated by your test |
| Ordinary render Vector pass | Render-layer pass | Screen-space motion associated with rendered geometry | Verified, but not interchangeable with internal fluid velocity |

Correction: `velocity` is not a fifth output socket on the Volume Info node. It is a separate named vector grid.

The relevant distinction is not whether fluid velocity exists. It does. The distinction is whether the chosen renderer and shader node expose that grid in a useful way. Your test found that Cycles does, whereas your EEVEE shader returned zero.

The Blender developer documentation describes `density`, `temperature` and `velocity` as standard volume-grid names and distinguishes Cycles' NanoVDB-based volume rendering from EEVEE's dense-texture representation. That supports the possibility of different renderer behaviour, although it does not independently establish why EEVEE returned zero in Blender 5.2.2. Blender Developer Documentation

Revised production setup:

- EEVEE: render fast flame-emission and soot-coverage passes.
- Cycles: render the fluid-velocity diagnostic pass.
- Offline: project and normalize velocity, then evaluate interpolation.
- Runtime: choose either a compact motion-vector atlas or a pre-interpolated colour atlas, based on the measured tradeoff.

This is a practical hybrid of the two Blender render engines.

##### 3.2 Your technique is consistent with published motion-vector flipbook production

I located the original article by [Klemen Lozar — Frame Blending with Motion Vectors](https://www.klemenlozar.com/frame-blending-with-motion-vectors/).

[Checked now] Lozar describes rendering simulation velocity, converting it to encoded motion-vector textures, masking those vectors with alpha, expanding motion information beyond the simulated flame boundary, and warping the current and next flipbook frames toward one another. He also warns about vector direction, compression, colour-space settings and additional shader/memory cost. klemenlozar.com

That is much closer to your experimental setup than my earlier generic optical-flow recommendation.

##### 3.3 Important limitation: projected velocity is not automatically optical flow

A 3D fluid velocity vector tells you how the simulated material moves through space. It does not, by itself, provide a perfect mapping between image pixels in adjacent frames.

For an orthographic camera with right vector $R$, up vector $U$, image width $W$, height $H$, orthographic horizontal extent $S_x$ and vertical extent $S_y$, a first-order approximation is:

$$ d_x = \Delta t\frac{W}{S_x}(v\cdot R) $$

$$ d_y = -\Delta t\frac{H}{S_y}(v\cdot U) $$

The negative sign assumes image coordinates increase downward, unlike camera-space up.

For an orthographic Blender render, check the actual fitted sensor extent and output aspect ratio rather than assuming the same scale on both axes.

For a perspective camera, projected displacement depends on depth and the projection Jacobian; simple dot products are not sufficient.

Even with correct projection, velocity blending can fail at:

- Newly ignited or extinguished regions.
- Occlusion between flame structures at different depths.
- Lines of sight containing several distinct velocity values.
- Areas where the fire's intensity changes because fuel burns, rather than because visible material moves.
- Matte boundaries where the weighted average becomes unstable.

Your absorption-weighted velocity pass is a sensible approach because it approximates the visible region's movement. But I would test two weight definitions: flame-emission-weighted velocity and coverage-weighted velocity. They can give different results at bright tips and dark outer rims.

##### 3.4 What I would run next

[My inference] Use the existing 48 rendered frames and perform the following controlled evaluation before modifying simulation settings:

| Variant | Runtime texture strategy | Expected tradeoff |
| --- | --- | --- |
| A: full-rate source | 48 colour frames, no interpolation | Best direct record of original motion; larger atlas |
| B: half-rate crossfade | 24 colour frames | Small atlas, visible ghosting risk |
| C: half-rate fluid MV | 24 colour frames + vectors | Potentially smoother with extra texture reads |
| D: FFmpeg MCI in-betweens | 48 offline reconstructed colour frames | Additional processing, simpler runtime |
| E: mixed | Original half-rate frames + targeted offline MCI + mesh motion | Smaller deployment choices, extra asset preparation |

Measure reconstruction with masked MAE or RMSE, SSIM, edge error and temporal stability. Keep a separate visual ranking at actual gameplay resolution.

Also evaluate the result against a 256-frame or 96-frame higher-temporal-resolution source if practical. When you evaluate odd original frames against even originals, some of the ground truth is itself the output of a discrete-time simulation. That is useful, but it does not perfectly establish what the fluid would look like at arbitrary sub-frame times.

Revised recommendation: if FFmpeg MCI looks best and a 48-frame atlas fits the memory budget, deploy the precomputed frames. Runtime MV interpolation is valuable when it saves enough memory, when playback speed changes dynamically, or when cinematic slow motion makes its extra flexibility worthwhile.

FFmpeg's own `minterpolate` implementation documents `mi_mode=mci` as motion-compensated interpolation. [Checked now] GitHub

### 4. Replace human hand-drawing with an AI-agent production pipeline

This is the largest architectural correction.

My earlier directions repeatedly assumed that an artist could draw flame contours, slash key poses and polished decal masks in Grease Pencil. That is not a useful default when the producer is Claude operating Blender headlessly.

The agent needs a design → extraction → geometry → animation → validation pipeline with deterministic intermediate files.

[My inference] I recommend three complementary asset-generation methods, rather than using generative images for every individual animation frame.

| Method | What the AI generates | How it becomes a game asset | Best use |
| --- | --- | --- | --- |
| Image-to-mask | One designed high-contrast image | Extract mask, clean, pack, animate through shader | Glints, sigils, ground damage, decorative flame contours |
| Image-to-geometry | Silhouette or stroke reference | Trace contours and convert to Blender curves / ribbons | Sword qi, long flame tongues, seals |
| Guided simulation + graphic control | Three-tongue target shape plus simulated fire motion | Bake Mantaflow, mask/reform with target silhouette, export animated atlas | Fire impacts, stylized flames |

The third method is what I would prioritize for your fire impact.

#### 4.1 How the agent obtains three beautiful curved flame tongues

##### Stage 1 — Generate a design mask, not a complete effect

Generate four candidate high-resolution silhouettes using Firefly Image, ChatGPT image generation or Gemini image generation. These are separate permitted tools in your production setup.

The prompt should specify geometry rather than merely “premium anime fire.”

Writing
Create a clean black-and-white VFX shape-design mask for a fantasy fire-impact burst.

Pure black background, solid white flame silhouettes. Exactly THREE dominant curved flame tongues rising from a compact common ignition point. The central tongue is tallest and bends gracefully to the right in a long S-curve; the left tongue is medium-height and curves outward to the left; the right tongue is shorter, broader near the base and curls sharply inward at its pointed tip.

All three tongues must be unequal in width, height, curvature and angle. Preserve two large, clearly visible pure-black negative-space gaps between them. Strong tapered tips, graceful organic calligraphic curves, elegant asymmetric composition.

No radial lotus, no symmetrical flower, no repeated petals, no smoke, no particles, no stars, no colour, no gradients, no glow, no antialias-looking fuzzy fog, no background, no scenery, no lettering.

A graphic-design silhouette intended to remain readable when reduced to 80 pixels tall.

This is not intended to create a finished fire animation. It creates a target shape that the agent can enforce.

##### Stage 2 — Extract and validate the image automatically

Use Blender Python plus image processing to:

1. Convert the candidate to luminance.
2. Remove near-black background variation.
3. Produce a binary mask using a threshold; start around 0.5 but choose the final threshold from the image histogram.
4. Preserve the three primary flame tips.
5. Eliminate tiny disconnected artifacts and accidental grey haze.
6. Measure the silhouette's bounding box, overall fill percentage and key negative-space gaps.
7. Downsample to 64, 128 and 256 px and render over your actual game ground.
8. Reject candidates where the three tips merge into one blob or where the major gaps vanish at the target size.

[My inference] For an approximately 100-pixel-tall effect, I would require two recognizable gaps at least about 3 pixels wide across their important visible regions. This is a design check, not a universal antialiasing requirement.

The agent must not identify three flames solely by counting connected components. Three tongues commonly join at a common base and therefore constitute one connected region.

Use contour geometry, tip prominence, medial-axis structure or a supplied spline template to identify the individual tongues.

##### Stage 3 — Turn the image into controllable geometry

The image can be converted into Blender curves through contour extraction and spline fitting, but a contour alone does not tell the system which branch is which.

I would retain a procedural three-spine representation alongside the final image mask.

Here is a sample normalized design specification:

```JSON
{
  "asset": "fire_impact_tongues_v1",
  "coordinateSystem": "screen_normalized_xy",
  "tongues": [
    {
      "id": "main",
      "bezier": [
        [0.49, 0.12],
        [0.41, 0.42],
        [0.72, 0.67],
        [0.59, 0.96]
      ],
      "widthBase": 0.17,
      "widthTip": 0.0,
      "startFrame": 0
    },
    {
      "id": "left",
      "bezier": [
        [0.44, 0.15],
        [0.27, 0.31],
        [0.12, 0.55],
        [0.23, 0.72]
      ],
      "widthBase": 0.11,
      "widthTip": 0.0,
      "startFrame": 2
    },
    {
      "id": "right",
      "bezier": [
        [0.55, 0.16],
        [0.85, 0.27],
        [0.91, 0.52],
        [0.69, 0.60]
      ],
      "widthBase": 0.14,
      "widthTip": 0.0,
      "startFrame": 4
    }
  ]
}
```

These are example control points, not a claim that the resulting shape is already approved.

The agent should iterate the coordinates until the resulting geometry matches the chosen image design.

For a cubic Bézier centreline:

$$ B(t)=(1-t)^3P_0+3(1-t)^2tP_1+
3(1-t)t^2P_2+t^3P_3 $$

At each sampled point, calculate the tangent $T$, perpendicular normal $N$, and a tapered width $w(t)$. Construct two boundary vertices:

$$ P_\pm(t)=B(t)\pm w(t)N(t) $$

A suggested initial taper is:

$$ w(t)=w_0(1-t)^{1.4}
\left(0.75+0.25\sin(\pi t)\right) $$

This produces a simple pointed ribbon. To avoid mathematically perfect edges, perturb the width with a low-frequency authored mask or restrained correlated noise.

Critical distinction: this geometry is a controllable structural silhouette, not the final appearance of fire. The unwanted procedural look arises when the crude mathematical shape is rendered directly without organic motion, texture or artistic refinement.

##### Stage 4 — Introduce organic motion

There are three practical ways to use the silhouette.

Option A: silhouette-constrained Firefly footage

Map the liked Firefly fire-trail footage into the three authored flame shapes, or use it to derive interior motion textures. Animate the overall shapes as curves or meshes while the footage supplies moving folds and curling highlights.

Best for preserving the smooth, slightly realistic fire movement already approved by the owner.

Option B: silhouette-constrained Mantaflow

Bake organic fire separately. Render its intensity and velocity, then use the simulated motion within the three designed tongue regions. Warp the envelopes modestly using the simulation's motion.

Best for controlled shape plus physically coherent turbulence and fluid velocity.

Option C: three independent simulated tongues

Create separate directional emitters so the simulation itself starts with three different flame streams. Combine the resulting render with a less restrictive authored shape mask.

Best if the source simulation can naturally preserve the silhouette without looking artificially cut out.

The actual production pipeline should try C first, then B if the physics keeps merging the tongues. Option A can retain the liked Firefly motion and may outperform both.

##### Stage 5 — Compose into one asset

Do not necessarily render each tongue as a separate transparent runtime layer.

You can render three tongue components, blend their source images offline, then pack the result into one atlas with one final alpha channel.

The shape-design stage can be elaborate while the three.js representation remains one card or one curved mesh.

If the result looks like a flat sticker, move the primary energy body onto shaped geometry, add a separate contact response or reserve the flat atlas for internal flame turbulence only.

#### 4.2 Agent-generated slash key poses

Instead of asking Claude to draw eight slash images:

1. Generate one premium grayscale slash reference image.
2. Extract a centreline or manually specify a cubic Bézier through the major movement points.
3. Create a ribbon mesh in Blender Python.
4. Animate the visible arc length, stroke width, curvature and endpoint.
5. Generate 6–12 key poses through deterministic parameters.
6. Render the key poses to a compact texture sheet only if stepped artwork is desired.
7. Otherwise export the mesh and its masks for runtime animation.

Example pose design:

| Pose | Frame | Shape |
| --- | --- | --- |
| Compression | 0 | Short, thick, curved start |
| Release | 2 | Arc length grows rapidly |
| Sweep | 4 | Long tapered curve with strong leading edge |
| Follow-through | 6 | Main arc extended and slightly bent |
| Breakup | 9 | Rear section fragments and thins |
| Residue | 12 | Only selected qi filaments remain |

[My inference] Use the generated reference to constrain proportions, not to invent each key pose independently. Independent AI image generations will often drift in contour and stroke identity.

#### 4.3 Agent-generated sigils and seals

The agent can generate the ornamental design with Firefly Image or other allowed image generators, but construct the clean final linework in Blender Python.

Suggested workflow:

- Request a pure black-and-white symbol design with a limited number of concentric structures and large readable motifs.
- Extract contours or construct the main rings and arcs directly as curves.
- Use the image only for irregular ornaments, terminals and decorative insets.
- Render layers separately: outer circle, major symbols, central seal, highlight path.
- Animate their reveal, rotation, progression and erosion independently.

Do not use AI-generated pseudo-Chinese characters as meaningful text. If the design requires actual Chinese characters, create them from verified intended text and licensed font/vector assets, with manual language review.

#### 4.4 Agent-generated crack and scorch decals

For ground damage, generate the painted morphology first, then extract channels automatically.

Suggested workflow — [My inference]

| Source | Extraction | Runtime channels |
| --- | --- | --- |
| AI-painted Metal cut | Extract dark central incision and chipped stone edges | R = cut, G = chipped edge, B = highlight, A = coverage |
| AI-painted Metal impact | Extract unequal fracture branches and central contact | R = cracks, G = debris, B = inner light, A = coverage |
| AI-painted Fire scorch | Separate blackened stone, burnt boundary and hot seams | R = char, G = ember, B = surface damage, A = coverage |
| AI-painted rift | Extract interior darkness and raised fractured edges | R = deep void, G = fractured rim, B = energy, A = coverage |

Use generated images as source paintings but not automatically as production-ready decals.

Reject large muddy shapes and radial black stars. Evaluate at the correct ground projection before accepting them.

This workflow preserves the advantage of authored/painted appearance without requiring the AI agent to operate a drawing tablet.

### 5. Making anime fire tongues with Mantaflow specifically

The main lesson from your existing test is that a realistic simulation with a good toon ramp can still have a bad silhouette.

A stepped ramp does not change the underlying flow's topology. To get three graceful tongues, you need to control the emission structure and motion field before shading, then apply only as much silhouette correction as necessary afterward.

#### 5.1 Recommended starter scene

Parameter values below are [My inference]—a proposed Blender 5.2.2 experiment. The parameter meanings and API names are documented; their artistic results are not guaranteed.

Use a Z-up world and an approximately 2.4 × 1.4 × 3.2 m simulation domain.

| Domain parameter | Initial value | Why |
| --- | --- | --- |
| `resolution_max` | 128 | Already practical on your M4 |
| `cache_frame_end` | 48 | Matches existing experiment |
| `time_scale` | 1.0 | Stable baseline |
| `vorticity` | 0.08 | Suppress excessive global turbulence |
| `flame_vorticity` | 0.15 | Some local curling without a cauliflower look |
| `burning_rate` | 0.40 | Longer, less immediately consumed flames |
| `flame_smoke` | 0.08 | Keep soot mostly for the separate coverage pass |
| `alpha` | 0.10 | Low smoke-density buoyancy |
| `beta` | 0.40 | Controlled heat buoyancy |
| `flame_ignition` | 1.5 | Start near the documented default |
| `flame_max_temp` | 3.0 | Start near the documented default |
| `use_adaptive_domain` | True | Reduce wasted simulation space |
| `adapt_margin` | 6 | Protect fast-moving flame tips |
| `adapt_threshold` | 0.002 | Avoid aggressive cropping |
| `use_noise` | False | First solve large-scale shape |
| `use_dissolve_smoke` | False initially | Avoid changing the simulation during silhouette tuning |
| `use_guide` | False initially | Isolate emission/force behaviour before adding expensive guiding |

The official Blender 5.2 Python API documents these named controls, their ranges and, for several settings, their defaults. Blender Python API+1

##### Why reduce vorticity?

Blender's gas-domain documentation describes higher vorticity as producing more numerous small swirls, while lower values yield smoother shapes. [Checked now] Blender 5.2 LTS Manual

Your goal is three coherent tongues with secondary folding, not a highly turbulent blob.

I would run `vorticity` values 0.0, 0.08 and 0.20, combined with `flame_vorticity` values 0.05, 0.15 and 0.35. Do not assume more curling means better fire.

#### 5.2 Three emitters, not a spherical burst

Use three distinct mesh emitters generated by Blender Python.

Suggested emitter configuration — [My inference]

| Emitter | Start location (m) | Initial velocity (m/s) | Relative fuel |
| --- | --- | --- | --- |
| Main | (0.00, 0.00, 0.10) | (0.20, 0.00, 3.2) | 1.0 |
| Left | (−0.25, 0.00, 0.10) | (−0.80, 0.00, 2.4) | 0.7 |
| Right | (+0.26, 0.00, 0.10) | (+0.85, 0.00, 2.1) | 0.8 |

Use narrow elliptical or slightly irregular emission meshes with radii around 0.08–0.14 m.

Keep the emitter objects inside the domain, and make sure their dimensions and surface-emission regions are several voxels wide. Otherwise the simulation may not receive consistent fuel.

Important: if the three sources are close together, they can merge rapidly. Spread them slightly during block-in, then reduce spacing once their individual motions are recognizable.

Blender documents initial X/Y/Z flow velocity, flow fuel, geometry/inflow behaviour and emission from mesh sources. [Checked now] Blender 5.2 LTS Manual+1

#### 5.3 Animate the emitters along curved paths

This is probably the most important structural change.

Rather than emitting all fuel from one origin for the entire effect, give each emitter a short controlled path over the first few frames.

For example:

- Main emitter moves upward, slightly left, then right.
- Left emitter accelerates outward before curling toward the centre.
- Right emitter travels outward more quickly, then its fuel emission stops early.

In Blender Python, animate emitter transforms and optionally source velocity. Use keyframes or a cubic Bézier control curve.

A moving source can create an initial distribution of fuel along a curved trajectory. But it does not guarantee the resulting flame will follow the path exactly: the gas continues to advect and interact according to the simulation.

[My inference] Start by moving sources only for frames 1–6, with emission ceasing at different frames. Let the remaining 8–20 frames capture the deformation and breakup.

If the tongues immediately merge, shorten the emission period, increase initial spacing or reduce turbulence.

#### 5.4 Force fields: which ones are worth using?

There are two distinct Blender systems that should not be conflated.

Fluid Guides: Blender's domain-level fluid guiding feature. It can derive velocities from baked moving effectors or another fluid domain, and enables a more expensive guiding solve. [Checked now] Blender 5.2 LTS Manual

Curve Guide force field: Blender's documented curve-based force for particle-path following. Its documentation is explicitly about particles and does not establish that it will directly guide Mantaflow gas into a target silhouette. [Checked now] Blender 5.2 LTS Manual

I would therefore test forces in this order:

1. Directional initial velocity on each flow source.
2. Short emitter animation along separate curved paths.
3. A weak Wind field or local force, if the first two still lack directional flow.
4. A small Vortex field to introduce a specific curl.
5. Actual fluid guiding from moving effector objects or a baked guiding domain, only after simpler controls fail.

Do not enable fluid guides speculatively. Blender explicitly warns that guiding incurs extra solver cost even without useful guide sources. Blender 5.2 LTS Manual

#### 5.5 Noise, dissolve and buoyancy

Noise: keep it disabled while evaluating silhouette. Blender states that gas noise adds finer detail on top of base motion. That makes it a polish stage, not a primary shape-control mechanism. [Checked now] Blender 5.2 LTS Manual

If the base passes, test noise upres factor 2 with a restrained noise strength such as 0.15–0.35. Inspect whether the noise destroys the pointed tips at gameplay resolution.

Dissolve: Blender's gas dissolve is primarily a way of dissipating simulated gas/smoke over time. It is not a substitute for designing flame shape or controlling fuel combustion. [Checked now] Blender 5.2 LTS Manual

For the first three-tongue test, use a short period of actual fuel emission, then let the flame burn out. Add smoke dissolve only if soot persists too long.

Buoyancy: keep it moderate enough for the flame to remain in its intended attack direction. If the resulting effect is strongly vertical regardless of the incoming sword direction, the motion is likely dominated by buoyancy rather than the authored directional impulse.

#### 5.6 Camera orientation

Your current scene uses a high three-quarter camera. Simulate and render at the final intended relative angle, but make a separate front-facing diagnostic render.

The front view tells you whether the emitters are creating three streams at all. The gameplay view tells you whether those streams actually appear as three separate tongues after projection.

A gap visible in Blender's front view may disappear at the gameplay camera because the tongues overlap in depth.

For a camera-facing impact card, choose one stable baking camera and keep it fixed throughout the atlas. For a ground-anchored effect, maintain the actual world-space camera relationship.

#### 5.7 Post-processing your two-pass fire

Your emission-only and absorption-only approach is worth retaining.

Do not return to physically coloured blackbody output as the default simply because it is more physically based. Your data-first pipeline is more controllable for a stylized result.

Suggested processing:

Emission greyscale + absorption coverage

Normalize passes using fixed sequence-wide exposure

Shape correction / three-tongue target mask

Subpixel edge cleaning and minimal dilation

Six-colour stepped ramp

Dark rim + thin concentrated hot core

Straight/premultiplied alpha validation

48-frame animation test at gameplay scale

Use sequence-wide normalization. If each frame is normalized independently to its own maximum, brightness may pulse unnaturally as the flame expands and dissipates.

Suggested starting post controls — [My inference]:

| Operation | Initial approach | Failure to avoid |
| --- | --- | --- |
| Exposure normalization | One fixed high percentile from all frames | Per-frame brightness pumping |
| Coverage threshold | Begin around 0.30–0.45 after normalization | Clipping away thin flame tips |
| Edge transition | Approximately 0.5–1.5 output pixels | Broad airbrush edge |
| Morphological dilation | 1 px at final cell size, if necessary | Bulky flame lobes |
| Dark rim | Thin coverage-difference band | Thick cartoon border |
| Highlight | High emission percentile, narrow region | Wide featureless white core |
| Small breakup | Spatially correlated, flow-following variation | Random flicker or noisy pixels |

For the dark rim, derive a narrow perimeter band from coverage, then limit its colour contribution to selected regions. Do not create a uniformly heavy black outline.

##### The core limitation

Mantaflow is a fluid solver, not a flame-tongue composition engine.

If the three-tongue silhouette repeatedly fails despite emitter and velocity tuning, stop trying to obtain exact graphic topology exclusively from the simulation.

Keep the successful simulated internal motion and impose a controlled shape envelope in post or at runtime.

That is not “cheating.” It is separating the responsibilities of physical motion and graphic art direction.

#### 5.8 A small but meaningful parameter search

Your M4 bake speed makes a controlled parameter sweep practical.

I recommend this experiment matrix:

| Candidate | Emitter design | Vorticity | Flame vorticity | Guide | Intended test |
| --- | --- | --- | --- | --- | --- |
| M1 | Three stationary sources | 0.08 | 0.15 | Off | Baseline separation |
| M2 | Three animated sources | 0.08 | 0.15 | Off | Does motion form curved tongues? |
| M3 | Three animated sources | 0.00 | 0.05 | Off | Maximum silhouette coherence |
| M4 | Three animated sources | 0.20 | 0.35 | Off | More organic breakup |
| M5 | M2 plus local directional force | 0.08 | 0.15 | Off | Can curvature improve? |
| M6 | Best prior candidate with guided fluid | Best | Best | On | Does expensive guiding add value? |

Use the same camera, resolution, exposure and ramp for all six renders.

Score each version using specific observable metrics: recognizable tongue count, tip separation, negative-space retention, image-edge quality, attractive internal motion and comparison with the owner-approved Firefly flame.

Do not score only the final frame. Inspect at least the growing, peak and breakup phases.

### 6. Firefly Video: finished asset or motion reference?

I would change my earlier recommendation here.

The owner already approved one Firefly flame-trail animation. That is meaningful project-specific quality evidence. Replacing it with a procedural mesh simply because meshes are more controllable would be a mistake.

Firefly Video can absolutely be the final visual asset when its actual motion and silhouette pass the game's acceptance test.

The issue is not whether the footage was AI-generated. The issue is whether it gives you the required shape, duration, alpha, consistency and spatial behaviour.

#### 6.1 Revised decision rule

| Situation | Use Firefly as | Reason |
| --- | --- | --- |
| Flame trail looks good at gameplay size, loops or dissipates correctly, and follows the action | Final animated texture | No need to rebuild an approved motion |
| Firefly footage has excellent curling motion but a generic overall silhouette | Interior motion source | Preserve organic detail; impose an authored shape |
| Firefly generates a symmetric lotus impact | Reference only or reject | Its fundamental composition is wrong |
| Sword sheath needs exact blade attachment | Final texture on a blade-conforming mesh | The texture can be final even when geometry is not |
| Smoke has excellent organic movement and clean alpha | Final flipbook | The video already solves the difficult part |
| Magic seal needs precise linework and symbols | Not the primary source | Prefer an image mask and controlled shader |
| Dragon must maintain anatomy during arbitrary path turns | Secondary flame source | Rigged geometry carries the creature |
| Firefly impact has excellent silhouette, timing and alpha | Potentially final flipbook | Do not force additional complexity without evidence it helps |

This is my inference, explicitly incorporating your reported preference test.

##### The liked flame-trail asset

I would preserve its existing visual character, then conduct only targeted tests:

1. Inspect the original frames and matte.
2. Test at native 24 FPS and at the intended game playback rate.
3. Compare plain frame sampling, crossfade and offline MCI.
4. Test optional subtle shape confinement only if the trail has unwanted boundaries.
5. Put the texture onto a ribbon that follows sword movement if its spatial behaviour requires it.
6. Avoid changing the source's palette, turbulence or softness until there is a clearly observed defect.

Do not “toonify” an already liked clip through aggressive thresholds merely to make it resemble another effect.

Your direction explicitly permits slightly realistic flame motion with stylized shape and colour. The liked clip may be closer to that target than a fully graphic, hard-edged procedural flame.

#### 6.2 Using Firefly Image to control Firefly Video

There is a particularly useful option missing from my previous answer.

Adobe's transparent-video workflow allows PNG images with transparency to be provided as first and last frames. [Checked now] Firefly

Therefore an agent can attempt this sequence:

- Generate a high-quality three-tongue flame design with an allowed image generator.
- Create a version suitable as Firefly Video's starting frame.
- Use Adobe Firefly Video with transparency enabled.
- Prompt the flames to curl, flex, rise and separate while preserving their broad arrangement.
- Select the clip that retains the strongest geometry and motion.

This may improve consistency, but it is not equivalent to an exact topology constraint. Firefly can still change the shape during the video.

[My inference] Treat this as a useful candidate generator, not a guarantee of reproducible animation.

For precision, the agent-controlled mesh or mask remains the fallback.

#### 6.3 One more important Firefly limitation

Adobe's September 2026 documentation describes a limitation in which transparent-background-generated videos are not fully supported inside the Firefly video editor workflow. [Checked now] Firefly

That is another reason to perform final alpha composition, trimming, temporal processing and atlas packing offline in Blender or your scripts rather than relying on the Firefly editor.

#### 6.4 Avoid an unnecessary Firefly versus Blender competition

Your tools can be complementary:

Firefly is a candidate source of beautiful organic image motion.

Mantaflow is a source of reproducible physically coherent motion, separate emission/coverage data and useful fluid velocities.

Blender Python provides controllable geometry, composition, masking and exports.

three.js shaders provide timing, spatial movement, palette controls, erosion and runtime integration.

The choice of the final source should be driven by the actual visual result, not by a preference for AI generation, simulation or procedural code.

### 7. Strong production options missing from the original report

These are the additions I would prioritize after reviewing your measurements and the sources again.

#### 7.1 Precomputed temporal super-resolution

New recommendation — [My inference]

Because FFmpeg MCI already produced your lowest measured reconstruction error, offline temporal interpolation deserves to be a first-class asset-production method.

For one 24-frame, 256² RGBA8 atlas:

- Original colour atlas: 6 MiB, excluding mipmaps.
- 48-frame atlas after 2× temporal interpolation: 12 MiB.
- A 24-frame RG8 motion atlas at 128² per frame: approximately 0.75 MiB before mipmaps.

Those figures show why precomputed interpolation can be attractive in the 32/48 MiB tiers but expensive in the 8 MiB tier.

For constrained tiers, consider half-rate source colour plus a reduced-resolution velocity map. For higher tiers, a larger pre-interpolated colour atlas may produce simpler and cheaper runtime rendering.

FFmpeg MCI should operate on consistently prepared foreground/alpha data, with testing for edge contamination. Independently interpolating the colour video and alpha video can create boundary misalignment.

Quality warning: FFmpeg MCI may reduce reconstruction error but also create warped structures at newly forming flame tips. Reject those candidates during animation review.

#### 7.2 Velocity-driven 2D shape animation

New recommendation — [My inference]

Instead of only using Mantaflow velocity to interpolate its original frames, use the velocity field to advect a separate authored shape mask.

Conceptually:

$$ M_{t+\Delta t}(u)=M_t(u-\Delta t V(u)) $$

where $M$ is the authored mask and $V$ is the projected, appropriately scaled motion field.

This gives you another possible hybrid:

- Artistically designed initial three-tongue mask.
- Fluid-derived motion directions.
- Smooth, evolving shape boundaries.
- Organic interior texture from simulation.

The difficult part is preventing the transported mask from becoming distorted, smeared or fragmented.

Use regular regeneration or controlled shape constraints to preserve the intended structure.

I would consider this an advanced experiment after the simple silhouette-constrained approach.

#### 7.3 Offline synthesis of 2.5D fire from authored ribbons

New recommendation — [My inference]

You do not necessarily need Mantaflow to create every elegant flame tongue.

An agent could build a three-dimensional arrangement of tapered ribbons in Blender, using:

- Curved centreline geometry.
- Broad-to-narrow width progression.
- Controlled twist.
- Travelling deformation waves.
- Organic noise masks.
- Partial overlaps.
- A simulated fire texture moving through the surfaces.

Render those ribbons offline into a 24–48-frame atlas from the game's camera.

This could combine the controllability of geometry with the organic appearance of simulated textures.

It is a strong candidate for sword sheaths, elongated flame trails and directional impacts.

#### 7.4 Source segmentation before simulation compositing

New recommendation — [My inference]

You can preserve separately rendered primary flame masses rather than allowing the full simulation to merge them visually.

A robust setup is:

- Simulate or render the three main tongues separately.
- Keep their per-frame masks independent.
- Composite into a single atlas in the desired overlap order.
- Add a short shared contact flame at the base.
- Introduce one common turbulence layer, if required.

That avoids three overlapping transparent runtime cards while giving you per-tongue timing and shape control.

The limitation is that independent simulations may appear disconnected. The shared base and consistent turbulence direction are important.

#### 7.5 Simulation-based motion plus image-generated static art

Expanded recommendation — [My inference]

Use the expensive offline generation where it materially contributes.

A practical division is:

| Component | Preferred production source |
| --- | --- |
| Large beautiful flame silhouette | AI image + curve reconstruction |
| Internal rolling motion | Mantaflow or approved Firefly clip |
| Fine irregular edge | Authored mask plus restrained distortion |
| Crack morphology | AI-painted image |
| Spark trajectory | Lightweight deterministic motion |
| Glint shape | AI image/clean mask |
| Colour hierarchy | Shared authored ramp |
| Hit timing | Gameplay event timeline |
| Runtime performance | Shader and batching |

The final visual identity comes from the combination, not from one tool.

#### 7.6 Automated visual regression and acceptance

This becomes more important because your producer is an AI agent.

The agent should capture the same skill at the same camera, target position and animation frames after every meaningful revision.

[My inference] A useful automated quality report should include:

| Measurement | What it detects |
| --- | --- |
| Silhouette bounding-box changes | Unexpected scale drift |
| Negative-space area and connectivity | Tongues merging into blobs |
| Alpha histogram | Excessive transparency or clipping |
| Edge-gradient distribution | Airbrush softness or aliasing |
| Temporal edge difference | Flicker and interpolation artifacts |
| Saturated-white pixel percentage | Overexposed cores |
| Frame-to-frame centroid movement | Unexpected whole-sprite wobble |
| GPU timing and draw calls | Performance regressions |
| Texture residency | Tier-budget violations |

Do not let these metrics replace blind visual judgment. They are regression detectors, not aesthetic graders.

The AI agent can run two internal review passes before presenting a candidate to the owner. The two human or independent blind judges remain the final acceptance gate.

### 8. Full source audit of the previous report

I rechecked the URLs from the earlier source inventory, using direct page retrieval where available and indexed official documentation where a site blocked direct retrieval.

The labels mean:

- Verified: source exists and supports the technical or artistic claim made.
- Partly verified: source exists but only supports part of the claim, or the original page could not be retrieved directly and an equivalent official source was used.
- Unsupported: source exists but does not establish the claim as presented.
- Wrong: the earlier claim contradicts the verified evidence.

Where a source was only verified through search indexing, that limitation is reflected in the verdict. These are checked-now audit results, not memory-based assurances.

#### 8.1 Adobe sources

| Original URL | Verdict | Finding |
| --- | --- | --- |
| [Firefly mobile transparency](https://helpx.adobe.com/firefly/mobile/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html) | Verified | Firefly Video, transparent generation, foreground and alpha export |
| [Firefly web transparency](https://helpx.adobe.com/ie/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html) | Partly verified | Confirms default 5 s/24 FPS and output structure, but not an absolute 540p limit |
| [Firefly video upscale](https://helpx.adobe.com/ca/firefly/web/work-with-audio-and-video/work-with-video/upscale-videos.html) | Wrong as recommended | Feature exists, but Adobe identifies Topaz Astra as the underlying partner model |
| [Firefly image upscale](https://helpx.adobe.com/firefly/web/edit-images/prompt-to-edit/upscale-images.html) | Verified | Explicit model choices include Firefly Upscaler, Topaz Bloom and Topaz Gigapixel |
| [Sound prompt guide](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-audio/writing-effective-text-prompts-for-sound-effects-generation.html) | Verified | Supports sound-prompt construction and separate sound generation |
| [Voice-guided SFX](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-audio/voice-to-sound-effects.html) | Verified | Supports voice-guided timing/energy control |
| [Adobe generative credits FAQ](https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html) | Verified | Includes commercial-use FAQ; feature-specific conditions and terms still apply |

The model provenance correction is supported independently by [Adobe's Topaz Astra page](https://www.adobe.com/products/firefly/partner-models/topaz.html). Adobe

The commercial-use FAQ supports use of Firefly-generated content in commercial projects, including beta features unless otherwise specified. This is not a blanket guarantee that every generated image is non-infringing or that every third-party input has an acceptable licence. Creative Cloud+1

#### 8.2 Blender sources

| Original URL | Verdict | Finding |
| --- | --- | --- |
| [Blender domain settings](https://docs.blender.org/manual/en/5.0/physics/fluid/type/domain/settings.html) | Partly verified | Direct retrieval failed; current official 5.2 documentation confirms relevant controls |
| [Adaptive domain](https://docs.blender.org/manual/en/5.0/physics/fluid/type/domain/gas/adaptive_domain.html) | Partly verified | Confirmed through corresponding indexed 5.2 manual |
| [Blender render passes](https://docs.blender.org/manual/en/5.0/render/layers/passes.html) | Partly verified | Vector pass confirmed; does not itself establish internal fluid-flow correctness |
| [Principled Volume](https://docs.blender.org/manual/id/5.0/render/shader_nodes/shader/volume_principled.html) | Verified through indexed manual | Density, emission, blackbody and temperature controls confirmed |
| [Cycles volume rendering](https://docs.blender.org/manual/en/5.0/render/cycles/render_settings/volumes.html) | Verified | Blender 5.0 default null-scattering change confirmed |
| [Grease Pencil animation](https://docs.blender.org/manual/en/5.0/grease_pencil/animation/introduction.html) | Partly verified | Current manual confirms capability; unsuitable as a hand-drawing dependency for your agent |

Two important new verified sources should replace the earlier vague fluid-attribute statements:

- [Blender 5.2 FluidDomainSettings API](https://docs.blender.org/api/5.2/bpy.types.FluidDomainSettings.html)
- [Blender 5.2 Volume Info node](https://docs.staging.blender.org/manual/en/latest/render/shader_nodes/input/volume_info.html)

The first documents the actual simulation properties. The second distinguishes the four Volume Info outputs from separately accessible named volume grids. Blender Python API+1

#### 8.3 Three.js, OpenCV and MDN sources

| Original URL | Verdict | Finding |
| --- | --- | --- |
| [UnrealBloomPass](https://threejs.org/docs/pages/UnrealBloomPass.html) | Verified | Bloom controls and mip-chain implementation |
| [OutputPass](https://threejs.org/docs/pages/OutputPass.html) | Verified | Tone mapping and output colour-space conversion |
| [Three.js colour management](https://threejs.org/manual/pages/color-management.html) | Verified | Colour-space handling |
| [KTX2Loader](https://threejs.org/docs/pages/KTX2Loader.html) | Verified | Basis Universal texture transcoding |
| [OpenCV optical flow](https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html) | Verified | Optical-flow algorithms, but no guarantee they beat simulated fluid velocity |
| [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) | Verified | Browser sound processing and scheduling |
| [GPU timer query](https://developer.mozilla.org/en-US/docs/Web/API/EXT_disjoint_timer_query) | Partly verified | General timing concept valid, but this particular extension is for WebGL1; WebGL2 uses `EXT_disjoint_timer_query_webgl2` |

That final distinction is another correction for your three.js implementation. MDN explicitly distinguishes the two extension names. MDN

#### 8.4 ArtStation, 80 Level, RealTimeVFX and developer sources

| Original URL | Verdict | Finding |
| --- | --- | --- |
| [Hazel Stagner — Sword Slashes](https://glairedaggers.artstation.com/projects/GaGnLQ) | Verified | Explicit mesh, black backing, directional/omnidirectional sparks, hand-painted hit |
| [Hazel Stagner — Electric Impact](https://glairedaggers.artstation.com/projects/Nx3qW1) | Verified | Painted electric core and SDF-style ground crack from painting |
| [Johan Nydahl — Stylized Fire](https://johannydahl.artstation.com/projects/GemQgW) | Verified | Tiling noises, flame shape mask and colour mixing |
| [Sheila Stipnieks — Stylized Fire](https://sheilastipnieks.artstation.com/projects/D5oPoA) | Verified | Alpha erosion and particle breakdown; author also criticizes her own ember texture |
| [Adam Gothard — Fire Magic](https://agothard.artstation.com/projects/oAwa9w) | Verified | Packed crack detail map and gameplay consistency |
| [Simon Trümpler — Stylized VFX in RiME](https://www.unrealengine.com/events/unreal-fest-europe-2018/stylized-vfx-in-rime?lang=es-ES) | Verified | Official presentation overview specifically mentions textures, UV distortion and geometry |
| [Blender Conference 2024 — Stylized Visuals](https://conference.blender.org/2024/presentations/3870/) | Partly verified | Official session listing exists; not every technique in the full presentation was inspected |
| [Blender Conference 2026 — Comic Style](https://conference.blender.org/2026/presentations/4146/) | Partly verified | Official description covers shapes, shading and Grease Pencil; full presentation not independently inspected |
| [Blender Studio — Cowboi](https://studio.blender.org/blog/cowboi/) | Verified | Camera parallax and anime NPR workflow claims confirmed |
| [Block-ins and Timing](https://realtimevfx.com/t/block-ins-and-timing/29830) | Verified | Grayscale composition and timing workflow |
| [Campfire using panning textures](https://realtimevfx.com/t/campfire-using-panning-textures/20165) | Verified | Direct feedback concerning shape, noise scale, speed and silhouette |
| [Know Your Sparks](https://realtimevfx.com/t/know-your-sparks/834) | Verified | Collection of real-world spark references, not a formal spark-production algorithm |
| [From Realism to Stylization](https://80.lv/articles/from-realism-to-stylization-game-vfx-production) | Partly verified | Supports stylized shape simplification and texture principles; my previous characterization of specific workflow techniques was too broad |
| [Anime-Inspired Fire Beam](https://80.lv/articles/using-unreal-engine-to-make-an-anime-inspired-stylized-fire-beam-vfx) | Verified | Panning textures, masks, vertex fade, noise and refraction explicitly documented |
| [Flame Burst](https://80.lv/articles/creating-a-flame-burst-effect-using-unreal-engine-5) | Verified | Simulation-to-flipbook, composition iteration, refraction, ribbons and timing |
| [Riot — Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/) | Verified | Gameplay clarity, hierarchy and visual noise principles |
| [Riot — VFX Updates](https://www.leagueoflegends.com/en-us/news/dev/dev-behind-the-scenes-of-vfx-updates/) | Verified | Readability, thematic consistency and fine-detail reduction |
| [GDC — The VFX Toolkit](https://gdcvault.com/play/1029417/Visual-Effects-Summit-The-VFX) | Partly verified | Session and overview verified; full presentation content not audited |

The 80 Level Flame Burst breakdown is especially interesting after your Blender experiments. The artist explicitly describes an 8×4 simulated flipbook, then improving composition through additional authored structures. It is direct evidence that a professional artist can use simulation and still need to fix composition deliberately. 80 Level

#### 8.5 CC0 source audit

| Original URL | Verdict | Finding |
| --- | --- | --- |
| [Unity Labs flipbooks](https://unity.com/blog/engine-platform/free-vfx-image-sequences-flipbooks) | Verified | Official release explicitly CC0 |
| [JangaFX free VDBs](https://www.jangafx.com/software/embergen/download/free-vdb-animations) | Verified | Listed free VDB simulations explicitly CC0 |
| [Kenney Particle Pack](https://kenney.nl/assets/particle-pack) | Verified | CC0 stated on asset page |
| [Kenney Impact Sounds](https://kenney.nl/assets/impact-sounds) | Partly verified | Official indexed result confirms 130 files and CC0; direct retrieval blocked |
| [ambientCG](https://ambientcg.com/) | Verified | Official [licence page](https://docs.ambientcg.com/license/) confirms CC0 |
| [Screaming Brain noise](https://screamingbrainstudios.itch.io/noise-texture-pack) | Verified | CC0 explicitly shown on asset page |
| [Freesound FAQ](https://freesound.org/help/faq/) | Verified | Multiple licence types; only explicitly CC0 sounds meet your policy |

The CC0 status of Unity's flipbooks, JangaFX's VDBs, ambientCG's assets and Screaming Brain's noise pack is directly supported by those publishers. Unity+3

##### What I am withdrawing from the earlier report

The earlier numerical GPU-cost estimates, production-hour estimates and quality-rubric thresholds were my inference, not values established by the cited sources. They should remain planning hypotheses until you benchmark them. They are not verified production facts.

I am also withdrawing any implication that a simulated flipbook with good motion vectors automatically has commercially excellent artwork, that Blender fluids must be slow on your M4, or that AI-generated footage is primarily useful as reference.

Most importantly, I would no longer prescribe Grease Pencil hand-drawing as an essential step for your AI agent.

### 9. Corrected final production decisions

This is the list I would give Claude as the current architecture decision record.

All pipeline selections are my inference, informed by the checked sources and your new test results. “Changed” indicates a meaningful change from the earlier report.

| Effect type | Corrected preferred tool chain | Review outcome |
| --- | --- | --- |
| 1. Fire impact | AI-image-designed three-tongue silhouette + Blender Mantaflow organic motion and velocity + toon data passes + offline MCI/MV comparison + optional contact mesh | Changed substantially — Mantaflow promoted, AI-generated shape control replaces hand drawing |
| 2. Flying sword flame sheath | Owner-approved Firefly flame-trail footage or Blender-simulated motion + blade-conforming ribbon/mesh + controlled mask/UV movement | Changed — Firefly footage can be a final texture |
| 3. Sword qi slash and trail | AI-generated painted mask → Blender Python Bézier geometry → animated ribbon, reveal, breakup and selective glints | Changed — remove manual Grease Pencil dependency |
| 4. Sparks and embers | AI-designed/cleaned sprite masks or CC0 sprites + instanced, path-aware motion + controlled lifetime | Retained |
| 5. Glints and twinkles | AI-generated fine star/glint masks → cleaned small atlas → timed instanced sprites | Retained |
| 6. Magic seals and halos | AI image ornament design + Blender Python curves and clean structural geometry + shader reveal | Changed — image-to-vector / programmatic construction |
| 7. Ground cuts and scorch | AI-painted damage morphology → automatically cleaned packed masks → decals + shader-driven propagation | Changed — explicit agent-friendly extraction pipeline |
| 8. Smoke | Fast Blender Mantaflow or CC0 VDB → emission/coverage data → stylized flipbook; add interpolation only if beneficial | Changed — prioritize measured local Blender capability |
| 9. Heat distortion | Shared, low-resolution noise/displacement field + scene-colour refraction pass | Retained |
| 10. Fire/qi dragon | Blender Python curve/rigged body + AI-designed materials + Firefly/Mantaflow flame-motion assets + ribbons/particles | Retained, with Firefly more strongly considered for final secondary textures |

#### Immediate next production experiment

Rather than developing ten VFX systems, I would run one decisive three-way fire test:

| Test | Source | Main purpose |
| --- | --- | --- |
| A — Firefly final asset | The liked Firefly motion, with correct matte and contact treatment | Preserve what the owner already likes |
| B — Guided Mantaflow | Three directional emitters, low turbulence, six-colour ramp, velocity/MCI interpolation | Test whether simulation can create aesthetically useful tongues |
| C — Authored hybrid | AI-generated three-tongue mask/geometry + best Firefly or Mantaflow interior motion | Test whether deliberate shape plus organic movement wins |

Hold all three to the same duration, gameplay camera, visual scale and runtime budget. In the hybrid, don't overcorrect the organic fire into a cartoon graphic.

My predicted ranking is C first, A or B second depending on the shot. That is a hypothesis, not a conclusion.

I would make the deciding evidence a 60 FPS capture from the actual game with the hero approximately 64 pixels tall, alongside a close-up and a texture/GPU-cost report. Both independent judges must approve the real-play version, not just the isolated sprite.

The most important revised decision is this: your Mac mini M4 is already capable of producing useful simulated fire quickly, and your team has demonstrated a working fluid-velocity interpolation method. The remaining primary obstacle is visual composition—creating three beautiful curved tongues, preserving the negative spaces, and integrating the resulting flame into the sword impact without losing the organic motion the owner likes.

That is the problem I would instruct Claude to solve next, before investing in more simulation resolution, shader complexity or new VFX assets.

## Lượt 3: các ý chính của Gemini gửi ChatGPT (nguyên văn)

```text
Second round: we gave Gemini the same brief. Here are Gemini's key ideas that differ from or add to yours. Please evaluate each one (adopt, adapt or reject, with reasons and a source where you can), say what it adds to your corrected plan, and then give one merged decision list. Keep it under about 12,000 characters.

1. One premultiplied layer does both the dark rim and the glowing core: blend ONE, ONE_MINUS_SRC_ALPHA; at the flame edge output a dark colour with alpha about 0.88 (it darkens the stone behind), at the core output HDR colour with alpha about 0.05-0.25 (it adds light). So a dark backing costs no extra transparent layer.
2. Erosion with ramp re-normalization: alpha = smoothstep(e, e + w, M); ramp coordinate = (M - e) / (1 - e), so every surviving island keeps its dark rim, body and core until it vanishes.
3. Hybrid cadence: mesh transforms, ribbons, sparks and camera at 60 fps, while flipbook frame index and erosion phase are stepped at 12-15 fps (on 2s), with no crossfade, for hand-drawn or cel flipbooks.
4. For a typing game, put anticipation inside the first frame: frame 0 a star glint at the sword tip plus a click sound, frame 1 a one-frame high-contrast impact flash at about 125% scale, frames 2-4 hold the silhouette nearly still while the inside scrolls, frames 5-16 ease out while erosion rises.
5. Firefly Video is strong at continuous directional flows (trails, ribbons, rising auras, magma) and weak at one-shot radial bursts. Generate the hero frame in Firefly Image first and use it as the video's first frame.
6. Make horizontally tiling flame-lick bands in Firefly Image (upscaled), use them as a 1024x256 greyscale mask scrolled on a ribbon or blade sheath mesh: far less memory than a flipbook, true 60 fps.
7. Seals, glints and crack decals: Firefly Image black-and-white design, threshold, then a signed distance field via a Euclidean distance transform, so lines stay crisp at 38 and 250 px per metre with fwidth antialiasing.
8. Motion-vector atlas at one quarter of the colour atlas resolution, linear colour space, uncompressed; clamp warped UVs inside each cell.
9. A 120 ms transient point light on impact that lights the hero and ground; a heat refraction ring on big hits.
10. Smoke from a cluster of displaced spheres in Blender with normals transferred from a smooth proxy (anime cloud shading), or CC0 VDB with a 2-3 step ramp.
11. Gemini estimates 75-85% of commercial anime combat VFX are meshes with panning textures (its own inference, no source).
12. Things we already rejected from Gemini: a "70/20/10 rule from Riot" (not in Riot's guide), studio names in prompts, OpenCV optical flow (not installed; our measurements favour sim velocity and ffmpeg minterpolate), 7-11 s Mantaflow bakes (we measured minutes), the Blender Glare node for stars (lens-flare look), Voronoi-baked cracks.
```

## Lượt 3: trả lời của ChatGPT (nguyên văn)

### Round 3 — Gemini proposal audit and merged VFX decisions

Verdict: adopt 5, adapt 6, reject 1. Gemini adds useful production techniques, particularly single-layer HDR compositing, erosion-ramp normalization, tiled flame masks, distance fields and stylized mesh smoke. But several proposals need corrections before Claude implements them.

I checked the relevant Adobe, Blender, three.js, WebGL, Unity VFX and working-artist documentation. The recommendations below are my engineering judgments, not claims that commercial studios use these exact settings.

#### 1. Evaluation of all 12 proposals

| # | Proposal | Verdict | Priority |
| --- | --- | --- | --- |
| 1 | Single premultiplied dark-rim + HDR-core layer | Adapt | P0 |
| 2 | Erosion with ramp renormalization | Adopt | P0 |
| 3 | Hybrid 60 FPS / 12–15 FPS animation | Adapt | P2 |
| 4 | Immediate glint, flash, hold, erosion timing | Adapt | P1 |
| 5 | Firefly for directional flow + first-frame image | Adopt | P1 |
| 6 | Seamless flame-band masks on scrolling meshes | Adopt | P1 |
| 7 | SDF for seals, glints and cracks | Adapt | P1 |
| 8 | Quarter-resolution uncompressed motion-vector atlas | Adapt | P2 |
| 9 | Transient point light + heat-refraction ring | Adopt | P1 |
| 10 | Clustered spheres with transferred normals for smoke | Adopt | P2 |
| 11 | 75–85% of anime-game VFX use meshes | Reject as a quantitative claim | — |
| 12 | Previously rejected techniques and assumptions | Adopt the rejections, with qualifications | P0 |

#### 2. Technical review

##### 1. One layer for dark rim and luminous core — ADAPT

This is mathematically valid and particularly useful under your two-overlapping-transparent-layers preference.

With premultiplied alpha:

$$ C_{\mathrm{out}}=C_{\mathrm{src}}+(1-\alpha)C_{\mathrm{dst}} $$

where $C_{\mathrm{src}}=\alpha C_{\mathrm{HDR}}$.

Consider white stone with linear colour $C_{\mathrm{dst}}=1$:

| Region | Straight RGB | Alpha | Result |
| --- | --- | --- | --- |
| Dark rim | 0.02 | 0.88 | 0.1376 — strongly darkened |
| Orange body | 1.5 | 0.50 | 1.25 — brighter |
| Hot core | 10.0 | 0.10 | 1.90 — HDR brightening |

The same draw can darken at its edges and brighten near its centre.

But Gemini's explanation requires two corrections.

First, the core is not truly additive. Its alpha still attenuates the background. Strong HDR source values can make the resulting composite brighter, but that is not identical to additive blending or physical light illuminating the environment.

Second, alpha 0.88 at the flame rim risks producing a black sticker on light stone. Use strong opacity only in selected narrow regions, not around the entire contour.

I would start with a discontinuous dark backing at approximately 0.35–0.75 alpha and tune it visually. Keep the high-alpha option for concentrated contact regions.

For WebGL2, configure the material for premultiplied output:

```JavaScript
material.transparent = true;
material.blending = THREE.CustomBlending;
material.blendSrc = THREE.OneFactor;
material.blendDst = THREE.OneMinusSrcAlphaFactor;
material.depthWrite = false;
```

The shader must output premultiplied RGB exactly once, and the effect must be composited into a linear HDR buffer before tone mapping. Beware of automatic premultiplication settings elsewhere in the material pipeline.

Sources, checked: [WebGL blend factors](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/blendFunc); [three.js material blending](https://threejs.org/docs/pages/Material.html). MDN+2

What this adds: one combined fire material is worth testing before committing to separate dark-backing geometry and luminous-core cards.

##### 2. Erosion with ramp renormalization — ADOPT

This is one of Gemini's best contributions.

Ordinary erosion raises an opacity threshold. As the effect disappears, the remaining pixels can become uniformly bright or uniformly dark because the colour ramp is still evaluated against the original intensity distribution.

Renormalization preserves a complete colour range across the surviving values.

For an intensity mask $M\in[0,1]$:

$$ a=\operatorname{smoothstep}(e,e+w,M) $$

$$ q=\operatorname{clamp}\left(\frac{M-e}{1-e},0,1\right) $$

Sample the six-colour ramp using $q$, not raw $M$.

Use `max(1.0 - e, 0.001)` to avoid division instability. Limit $e$ below 1 and explicitly terminate the effect at its final lifetime.

One additional correction: don't automatically use `a` as the final blending alpha. In proposal 1, dark rims and bright cores require different alpha values. Treat `a` as an erosion coverage mask, then calculate actual compositing opacity independently.

For example:

```glsl
float surviving = smoothstep(e, e + width, M);
float q = clamp((M - e) / max(1.0 - e, 0.001), 0.0, 1.0);

vec3 rgb = texture(colorRamp, vec2(q, 0.5)).rgb;
float opacity = coverage * surviving * alphaProfile(q);

outColor = vec4(rgb * opacity, opacity);
```

`alphaProfile(q)` is an authored curve; it is not necessarily monotonic.

If every surviving island retains a dark border, orange body and hot interior, the fire should look more coherent throughout dissolution.

Source: Unity's documented VFX Graph supports gradient colour mapping and alpha thresholding, although this exact combined normalization equation is an implementation proposal, not an officially documented Unity method. [Unity VFX shared output settings](https://docs.unity.cn/Packages/com.unity.visualeffectgraph%4012.0/manual/Context-OutputSharedSettings.html). 12.0.0

##### 3. Hybrid cadence — ADAPT

The principle is correct; the specific default is wrong for your currently approved Firefly flame.

Keep mesh positions, sword motion, ribbon geometry, sparks and camera movement smoothly updated at 60 FPS. Use stepped flipbooks only when their artistic style benefits.

However:

- At 60 FPS, 12 FPS source animation means one drawing every 5 frames.
- At 60 FPS, 15 FPS means one drawing every 4 frames.
- Traditional animation “on twos” at 24 FPS means 12 drawings/second; on twos at 60 FPS would mean 30 drawings/second.

Do not equate these automatically.

For your effects:

| Component | Recommendation |
| --- | --- |
| Approved Firefly flame trail | Continuous 24 FPS sampling, with tested interpolation |
| Mantaflow flames | 24–48 effective FPS; preserve organic motion |
| Anime slash silhouettes | Try 12–15 discrete poses/second |
| Mesh and sword movement | Smooth 60 FPS |
| Erosion | Usually smooth; stepped only when visually intentional |
| Glint animation | 2–8-frame authored pulses |

My inference: freezing both the source frame and the erosion phase at 12 FPS is likely to make your currently liked flame trail worse, not better.

Use stepped cadence for selected graphic elements, never as a universal stylization filter.

##### 4. Immediate glint, click, impact flash and hold — ADAPT

This is a strong short-hit timing preset, but I would not make it the default for every skill.

For one fast flying-sword contact, try:

| Simulation frame | Event |
| --- | --- |
| 0 | Sword-tip glint or ignition cue; launch/cue sound |
| 1 | Very brief bright contact flash |
| 2–4 | Hold the primary impact silhouette, while its internal fire continues moving |
| 5–10 | Controlled expansion and secondary movement |
| 11–16 | Dissolution, sparks and residual energy |

A 125% flash scale is an experimental value, not a universal requirement. A large flash can hide the enemy or create an apparent hitbox bigger than the real collision.

More importantly, the impact sound transient should coincide with the registered visual contact, not necessarily with the preliminary sword-tip glint. The sword may have a launch click at frame 0 and a separate impact transient at frame 1.

For your typing game, anticipation can start from the input-progress animation or sword launch. It does not need to delay the player's completed-word action.

Keep this as a reusable `fastSwordHit` timeline preset. Large Fire abilities, heavy boss impacts and dragon attacks need different timing.

Relevant verified principle: Riot's official clarity guidance requires visual/audio feedback to communicate gameplay, preserve importance hierarchy and minimize noise. [Riot — Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/). leagueoflegends.com

##### 5. Firefly directional flow and image first frame — ADOPT

This agrees with your actual approval results.

Keep the owner-approved Firefly flame-trail clip as a legitimate final asset. Do not reduce it to a reference just because Blender can reproduce the physics.

Firefly is a strong candidate for flowing flame, rising auras, trailing combustion and secondary movement. For exact one-shot impacts, it requires closer supervision because the event silhouette and contact location must remain controlled.

Adobe officially documents transparent-video generation using a transparent PNG first/last frame, with foreground and alpha videos in the export. Checked. [Adobe Firefly transparent video](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html). Firefly

Use a generated VFX key image, not an entire hero/character image, as the first frame when building a flame-only texture.

Recommended procedure:

1. Generate a clean isolated three-tongue design.
2. Supply it as the transparent first frame.
3. Select the Adobe Firefly Video model explicitly.
4. Request continuous motion while preserving major shapes.
5. Inspect first-frame adherence, alpha stability, curvature and breakup.
6. Reject clips that collapse into a symmetrical flower or shapeless blob.

What this adds: generated-image conditioning becomes a direct way to improve Firefly's shape control, though it cannot guarantee topology consistency.

##### 6. Horizontally seamless flame-lick masks — ADOPT

This may be the best low-memory technique in Gemini's proposal for sword sheaths and sustained trails.

A 1024×256 texture occupies approximately:

| Format | GPU memory without mips |
| --- | --- |
| R8 | 0.25 MiB |
| RGBA8 | 1.0 MiB |

That is substantially smaller than a multi-frame atlas at comparable source resolution.

A ribbon or blade mesh can scroll the mask smoothly at 60 FPS without storing multiple animation frames.

However, Firefly Image cannot be assumed to produce mathematically seamless tiles merely because the prompt requests them.

Claude should enforce periodicity offline:

- Generate the flame band.
- Inspect its left and right boundaries.
- Offset the image by half its width.
- Repair the visible seam with a short transition or procedural blending.
- Verify the first and last columns and their local gradients match.
- Reject obvious repeated motifs after scrolling across a long ribbon.

Prefer a long authored flame-lick pattern plus a slower secondary mask rather than two identical repetitive waves.

What this adds: a clear replacement for flipbooks on attached, sustained fire. It does not replace simulated fire impacts, where irregular changes in topology are valuable.

##### 7. SDF for seals, glints and cracks — ADAPT

Good technique, but not universally appropriate.

A signed distance field (SDF) stores the distance to a shape boundary. This supports scale-aware antialiasing and adjustable edge widths. However, an SDF cannot recover details that were already lost when the image was thresholded.

Use it selectively:

| Asset | Preferred representation |
| --- | --- |
| Magic seals, circular inscriptions | SDF or vector geometry |
| Sharp angular symbols | MSDF, preferably from vector paths |
| Thin Metal cutting lines | SDF plus appropriate width controls |
| Hand-painted branching cracks | Painted masks; optional SDF for main incision |
| Four-point glints | Painted RGBA sprite or MSDF |
| Scorch marks | Painted masks, not primarily SDF |
| Smoke and organic fire | Normal masks/flipbooks |

At 38 px/m and 250 px/m, one SDF can help maintain consistent edge appearance. But tiny features still disappear under minification, while excessive magnification reveals inaccuracies in low-resolution source shapes.

For sharp corners, consider MSDF. Viktor Chlumský's MIT-licensed `msdfgen` documents the distinction between ordinary SDF and multichannel SDF, including improved reproduction of corners.

Checked: [msdfgen](https://github.com/Chlumsky/msdfgen); [Epic — SDF rendering](https://dev.epicgames.com/documentation/unreal-engine/using-signed-distance-field-text-rendering-in-unreal-engine). GitHub+1

What this adds: better scale consistency for precise graphic effects. It should not replace high-quality painted morphology.

##### 8. Quarter-resolution motion vectors — ADAPT

This has especially strong support.

Klemen Lozar explicitly describes substantially reducing motion-vector texture resolution, using an uncompressed vector map, disabling sRGB interpretation and addressing motion outside the simulation boundary.

His example uses a 512-pixel motion-vector texture with a 4096-pixel colour texture. [Lozar — Motion-vector blending](https://www.klemenlozar.com/frame-blending-with-motion-vectors/). klemenlozar.com

But “quarter resolution” needs a precise definition:

| Example: colour cell 256² | Vector cell | Pixel count |
| --- | --- | --- |
| Quarter linear resolution | 64² | 1/16 |
| Quarter pixel count | 128² | 1/4 |

Test both. Start with 128² velocity per 256² colour frame, then try 64² if quality remains acceptable.

Important implementation details:

- Store vector data in linear/non-colour space.
- Avoid lossy colour compression.
- Validate forward/backward encoding and vector scale.
- Pad cells and ensure UV warping cannot sample neighbouring atlas frames.
- Do not merely clamp every displaced sample to a constant edge pixel; that can produce stretched borders.
- Compare runtime MV with your existing FFmpeg MCI result.

Your measurements still favour FFmpeg MCI in reconstruction error: 26% improvement versus 18% for MV blending. That remains the baseline to beat.

What this adds: a realistic method of reducing MV memory enough for the 8/16 MiB tiers.

##### 9. Transient light and heat-refraction ring — ADOPT

This is worth adding because it creates environmental contact that an isolated flame card cannot.

I would test:

- One unshadowed warm point light near the impact.
- Attack over 1–2 frames.
- Fast decay over approximately 80–120 ms.
- A localized heat-distortion ring only for sufficiently large Fire hits.

However, a dynamic light must be measured in the actual scene. Its cost depends on material shaders, affected objects and rendering configuration. Shadow casting should be disabled for the baseline.

In horde combat, use a shared priority-controlled light rather than one point light per enemy hit. The same applies to heat distortion: one shared distortion/compositing system, not one full-screen copy per hit.

Checked: [Three.js PointLight](https://threejs.org/docs/pages/PointLight.html). Three.js Docs

What this adds: an important sense of the fire affecting nearby surfaces and the hero, rather than floating above the world.

##### 10. Clustered-sphere anime smoke — ADOPT

This is a useful missing alternative to fluid flipbooks, especially for stylized magical smoke and clouds.

Claude can build an irregular cluster of overlapping ellipsoids in Blender Python, combine or remesh the shape, then transfer smooth normals from a larger proxy. A stepped lighting ramp creates broad animated shading regions.

Blender documents copying mesh normals through its Data Transfer modifier. Checked: [Blender Data Transfer](https://docs.staging.blender.org/manual/en/latest/modeling/modifiers/modify/data_transfer.html). Blender 5.2 LTS Manual

Use the methods differently:

| Desired smoke | Best candidate |
| --- | --- |
| Graphic anime puff | Clustered mesh with smooth/proxy normals |
| Rapid turbulent impact smoke | Mantaflow flipbook |
| Large persistent magical cloud | Mesh, optionally with moving internal texture |
| Realistic rolling plume | CC0 VDB or Mantaflow with stylized shading |

The [JangaFX free VDB library](https://www.jangafx.com/software/embergen/download/free-vdb-animations) explicitly lists its free VDB simulations as CC0. Real-Time VFX Simulations

For mesh smoke, avoid visible intersections between sphere components. Render a unified silhouette, not a pile of shaded balls.

What this adds: a controllable anime-smoke style that does not require a simulation or flipbook.

##### 11. The 75–85% mesh-VFX estimate — REJECT

There is no verified public dataset supporting this percentage for the referenced commercial anime games.

It is entirely plausible that many combat effects use scrolling textures, ribbons and meshes. But a specific percentage cannot be inferred reliably from screenshots or gameplay videos.

Keep the architectural principle; reject the statistic.

Your own distribution should be determined by your effect families, runtime constraints and accepted visual results—not an invented studio benchmark.

##### 12. Previously rejected ideas — ADAPT

The rejections are mostly correct, with these qualifications:

- “Riot's 70/20/10 rule”: reject. Riot's published clarity principles do not establish that numerical rule.
- Studio IP in prompts: exclude.
- OpenCV optical flow: deprioritize based on your measurements; lack of installation alone does not invalidate the method.
- 7–11-second Mantaflow bake: reject as an estimate for your measured 128-division, 48-frame scene. Your observed 3.5–4.5 minutes is the relevant baseline.
- Blender Glare-node stars: reject as the primary glint design. A restrained glare may still be useful as a secondary post effect, if measured and visually approved.
- Voronoi cracks: reject as the final artwork. Procedural fracturing remains useful for controlled variation, but painted shapes should carry the design.

Correction to the opening table: #12 is more accurately Adapt, not an unconditional adoption. The resulting tally remains five Adopt, six Adapt, one Reject.

### 3. One merged production decision list

This is the consolidated version I would use as the implementation specification for Claude.

| Effect | Final preferred pipeline | Key decision |
| --- | --- | --- |
| 1. Fire impact | AI-designed three-tongue silhouette + guided Mantaflow (128 divisions) or approved Firefly source → emission/coverage masks → six-colour ramp, renormalized erosion, single premultiplied HDR material → contact light, sparks | Compare Firefly-final, Mantaflow and authored hybrid in the real play build |
| 2. Sword flame sheath | Owner-approved Firefly flame footage or seamless 1024×256 painted flame band → scrolling texture on blade-conforming ribbon | Mesh holds geometry; texture supplies beautiful motion |
| 3. Sword-qi slash/trail | AI-generated calligraphic mask → Blender Python Bézier ribbon → shader reveal, directional dissolve and glints | Continuous 60 FPS ribbon; optionally stepped graphic poses |
| 4. Sparks and embers | Painted small sprite atlas → instanced particles with directional initial velocities, ballistic movement and cooling | No round bubble embers, radial wheels or analytic diamond stars |
| 5. Glints/twinkles | AI-painted four/six-point masks, optionally MSDF → limited sprite pulses | Keep highlights rare, sharp and purposeful |
| 6. Rings/halos/seals | AI Image ornament design → Blender curves / SVG / SDF-MSDF → segmented shader reveal | Clean linework across zoom levels |
| 7. Ground cuts/scorch | AI-painted damage morphology → packed masks → decals with animated propagation and erosion | SDF only where useful for precise cuts; preserve painterly scorch |
| 8. Smoke | Two candidates: Mantaflow/CC0 VDB flipbook or clustered toon mesh with transferred normals | Choose based on the desired smoke language and actual gameplay scale |
| 9. Heat distortion | Shared localized refraction pass with animated displacement field; optional expanding distortion ring | Major Fire impacts only; profile before enabling on mid tier |
| 10. Fire/qi dragon | Blender Python path-rigged body + authored surface masks + Firefly/Mantaflow flame motion + trailing ribbons/particles | Coherent anatomy and movement come from mesh; textures carry organic energy |

#### 4. The next implementation sequence

I would organize Claude's work into four practical passes, not ten independent asset tasks.

1. Shader foundation: implement the single-layer premultiplied dark-rim/HDR-core material, renormalized erosion, colour ramp and reliable alpha handling. Verify that the output buffer retains HDR values and that alpha is not multiplied twice.
2. Two fire-source candidates: retain the approved Firefly clip; create one three-tongue Mantaflow candidate. For each, compare native source frames, FFmpeg MCI and reduced-resolution fluid MV. Do not assume interpolation improves perceived quality.
3. Spatial integration: add sword-following mesh support, authored spark/glint sprites, and one priority-controlled contact light. Test a heat-distortion ring separately because of its post-processing cost.
4. Blind acceptance: capture all variants at gameplay scale against light stone, dark ground and dense enemies. Record GPU time, texture residency and animation-quality findings, then submit the strongest candidates to both independent judges.

#### Final conclusion

Gemini's most valuable additions are single-layer HDR compositing, erosion-ramp renormalization and seamlessly scrolling flame-band masks. These improve your current architecture without requiring more transparent layers or high-resolution flipbooks.

Its most important conceptual contribution is separating frame cadence, internal motion and mesh movement. The result does not need to be uniformly animated at one rate.

The two ideas I would treat most cautiously are the nearly opaque dark fire rim and the universal 12–15 FPS stepped cadence. Either could actively damage the soft, flowing Firefly flame appearance the owner already approved.

The merged plan should therefore preserve organic fire motion, use designed silhouettes instead of generic procedural geometry, and concentrate technical complexity where it demonstrably improves the final 40–200-pixel effect.

Production rule: no technique is adopted solely because it is more advanced. It must improve the blind-rated real-play result while respecting the 0.85 ms GPU and 8/16/32/48 MiB texture budgets.
