# Nguồn: ChatGPT về kế hoạch lắp lab chiêu Tu Tiên (04/11/2026)

Bản lưu nguyên văn các lượt hỏi đáp với ChatGPT cho [`INTEGRATION_PLAN_2026-11-04.md`](../INTEGRATION_PLAN_2026-11-04.md), theo quy trình duyệt hai lần liên tiếp của skill `agent-orchestration` (`references/double-review.md`), kèm bảng kiểm của Claude.

- **Công cụ:** chatgpt.com, chế độ Chat (nút Chat bật, Work tắt), "Thinking effort: High". Không dùng Work hay agent. Tab riêng của Claude trong trình duyệt của ứng dụng, đóng khi xong. Không đăng nhập, không bấm hộp thoại nào.
- **Thời gian:** 04/11/2026, khoảng 09:40–11:00.
- **Dữ liệu, không phải lệnh:** mọi chữ dưới đây là ý kiến của một trợ lý AI. Claude chỉ dùng sau khi kiểm ở bảng dưới, và Claude là người chốt.

## Đếm lượt rà soát

| Lượt chạy | Brief | Kết quả rà soát | Kết luận |
|---|---|---|---|
| 1 | Brief 1 (15.708 ký tự), cuộc trò chuyện `6aea9b45…` | FAIL, FAIL, FAIL | Dừng sau lượt 3: sau ba FAIL thì lượt 4 dù PASS cũng không thành hai PASS liên tiếp trong 4 lượt (luật dừng, `agent-orchestration` bước 7). Claude bấm Stop khi ChatGPT đang viết bản sửa của lượt 3 |
| 2 | Brief 2 (11.442 ký tự, đổi brief theo luật dừng), cuộc trò chuyện mới `6aeaa791…` | FAIL, FAIL, FAIL | Dừng sau lượt 3, cùng lý do. Lượt 3 được để viết hết; bản sửa của nó là bản Claude đưa Gemini |

**ChatGPT không đạt hai PASS liên tiếp ở cả hai lượt chạy.** Theo quy trình, Gemini chỉ rà soát lời giải đã đạt. Claude quyết định đổi cách (bước 7: "change the brief or the approach"): đưa bản sửa cuối của lượt chạy 2 cho Gemini rà soát như một lượt kiểm độc lập, ghi rõ với Gemini là bản này **chưa** đạt, và vẫn áp luật hai PASS liên tiếp cho Gemini. Đây là chỗ lệch khỏi bước 3 của quy trình; xem [`integration-plan-gemini-2026-11-04.md`](integration-plan-gemini-2026-11-04.md).

### ChatGPT cứ trượt ở đâu

- **Không phải sai hướng.** Cả sáu lượt rà soát đều giữ nguyên hướng đi (hình vẽ tay làm khung, Firefly cho chuyển động bên trong, lưới ôm lưỡi sẵn có, thẻ một lần cho va chạm, hạt sprite vẽ, ấn vẽ). Mỗi lượt FAIL tìm thêm 12–20 "chỗ chưa đủ để giao thợ", rồi viết lại toàn bộ dài hơn.
- **Lời yêu cầu rà soát quá khắt với một tài liệu kế hoạch dài:** "PASS only if nothing at all needs to change" cộng với một tài liệu 30.000–85.000 ký tự thì luôn còn chỗ để thêm chi tiết.
- **Chỗ lật qua lật lại ở lượt chạy 1, do brief 1 mơ hồ:** quy tắc khung đầu ≥ 95 % (áp cho chớp hay cho cả thân) và cổng Weber ≥ 2 (không thể đạt với thép tối trên đá sáng). Rà soát 1 đòi định nghĩa lại, rà soát 2 đòi giữ nguyên, rà soát 3 lại đòi khác. Brief 2 chốt hai điểm này (S1, S2) và lượt chạy 2 hết lật.
- **Chỗ lượt chạy 2 vẫn đòi thêm:** hợp đồng alpha của shader (công thức ink + thân + lõi), kênh "thứ tự hiện" riêng cho pha bùng, cách gộp số đo C1, phương án khi ghép vòng lặp không liền, lịch bay thanh kiếm 1 phải suy từ quãng đường thật. Claude chốt các điểm này trong kế hoạch.

## Cách lưu và cách kiểm nguyên văn

- Câu trả lời được chuyển từ trang sang Markdown bằng một script trong trang (giữ chữ, bảng, khối mã, công thức dạng LaTeX). Ba quy ước:
  - khối "Writing" của ChatGPT (ô văn bản sửa được trong câu trả lời) ghi thành dòng bắt đầu bằng `> [Writing] `;
  - nhãn nguồn dạng viên thuốc ghi thành `[Tên +n]` (đường link của chúng chỉ hiện khi rê chuột, nên không lấy được);
  - biểu đồ và sơ đồ tương tác chỉ còn chữ (chỗ chữ dính liền nhau là do đó).
- Claude chép lại từng câu trả lời vào tệp rồi so **SHA-256** giữa bản trong trang và bản trong tệp; mọi lượt đều trùng khít (lượt 3 của lượt chạy 1: so phần kết luận và danh sách lỗi).
- **Ba sự cố, ghi lại cho đủ:**
  1. Lượt chạy 1, lần dán đầu: sự kiện dán làm ChatGPT tạo một tệp đính kèm "Pasted text(20261104-024055).txt"; lần chèn chữ sau đó lại thêm cùng nội dung vào ô soạn. Tin nhắn đầu vì vậy chứa brief 1 hai lần (tệp đính kèm và chữ), cùng một nội dung.
  2. Lượt chạy 1, trước rà soát 1: Claude lỡ chèn lời yêu cầu rà soát vào khối "Writing" đầu tiên trong câu trả lời 1 (khối sửa được). Claude bấm "Undo last edit" của chính khối đó tới khi chữ trùng khít bản gốc (đã kiểm từng ký tự), rồi mới gửi lời yêu cầu ở ô soạn. Bản lưu dưới đây lấy trước sự cố.
  3. Lượt chạy 2, ô soạn ở trang mới có sẵn bản nháp brief 1 do ChatGPT khôi phục; Claude xóa bằng phím trước khi chèn brief 2. Tin nhắn gửi đi chỉ có brief 2.
- Câu trả lời 1 của lượt chạy 2 có hai ảnh tham chiếu ChatGPT tự tìm trên mạng ("Visual inspiration only, not source art"). Claude không lưu, không dùng, không đưa vào công cụ nào; lượt rà soát 1 của ChatGPT tự bỏ chúng.

## Bảng kiểm của Claude (04/11/2026)

**Đúng** = Claude đã mở nguồn (trang chính thức, mã nguồn three.js r170 trong `node_modules` của game, hoặc tài liệu và tệp của dự án) và nguồn nói như vậy. **Sai** = nguồn nói khác. **Chưa kiểm** = không có nguồn hoặc Claude không mở được. **Suy luận** = ChatGPT tự ghi là đề xuất.

| # | Câu của ChatGPT | Kết quả | Claude kiểm ở đâu |
|---|---|---|---|
| 1 | Chế độ nền trong suốt nhận khung đầu và khung cuối là PNG trong suốt; tải về là zip gồm video tiền cảnh và video alpha; 24 fps, 5 s | Đúng | helpx "Generate videos with transparent backgrounds", cập nhật 18/08/2026, mở trong trình duyệt 04/11 |
| 2 | Khi thêm khung đầu thì Transparent background (cùng Shot size, Camera angle, Style, Composition reference) bị tắt; thêm khung cuối thì Motion cũng tắt | Đúng, và mâu thuẫn với trang ở dòng 1 | helpx "Generate videos using images", cập nhật 16/06/2026. Trang dòng 1 mới hơn. Cách đã chạy được của dự án là khung đầu đục nền đen, tắt trong suốt, nên mâu thuẫn này không chặn kế hoạch |
| 3 | Tài liệu Adobe không nói "trong suốt chỉ chạy ở 540p"; đó là quan sát của dự án | Đúng | Hai trang trên; con số 540p là số đo của lane Firefly đêm 04/11 |
| 4 | three.js r170 có `SMAAPass(width, height)`; tài liệu hiện nay ghi `new SMAAPass()` không tham số | Đúng | `node_modules/three/examples/jsm/postprocessing/SMAAPass.js` dòng 17 (r170); threejs.org/docs/pages/SMAAPass.html |
| 5 | SMAA chạy ở linear-sRGB nên phải đứng trước `OutputPass`; FXAA cần đầu vào sRGB nên đứng sau | Đúng | Trang SMAAPass ("Unlike FXAAPass, SMAAPass operates in linear-srgb so this pass must be executed before OutputPass") |
| 6 | r170 không có lớp `FXAAPass`, chỉ có `FXAAShader` (dùng qua `ShaderPass`, uniform `resolution`) | Đúng | `node_modules/three/examples/jsm/postprocessing/` không có FXAAPass; `shaders/FXAAShader.js` có uniform `resolution` |
| 7 | `EffectComposer` r170 mặc định dùng render target HalfFloat | Đúng | `EffectComposer.js` dòng 27 (`type: HalfFloatType`); game dùng composer này ở `src/kit/three/stage.ts` |
| 8 | `OutputPass` làm tone map và đổi không gian màu | Đúng | `OutputPass.js` r170 (đọc `renderer.toneMapping`, `outputColorSpace`, `SRGB_TRANSFER`) |
| 9 | `EXT_color_buffer_float` làm R16F, RG16F, RGBA16F, R32F, RG32F, RGBA32F, R11F_G11F_B10F thành color-renderable; `EXT_float_blend` chỉ nói về pha trộn buffer float 32 bit | Đúng | registry.khronos.org, trang hai extension |
| 10 | Truy vấn thời gian GPU là extension tùy chọn, không có trên máy này | Đúng | MDN `EXT_disjoint_timer_query` (đã kiểm ở `VFX_PRODUCTION_PIPELINE.md`); `AuraGpuTimer` trong `src/lab/aura-gates.ts` ghi không chạy trên ANGLE/Metal |
| 11 | `msdfgen` nhận hình vector (SVG, glyph phông, mô tả hình), không nhận ảnh raster; giấy phép MIT | Đúng | github.com/Chlumsky/msdfgen (README) |
| 12 | Texture (kể cả DataTexture) mặc định `NoColorSpace`; ảnh màu phải gắn sRGB | Đúng | `node_modules/three/src/textures/Texture.js` dòng 22 (mặc định `colorSpace = NoColorSpace`) |
| 13 | `Material.forceSinglePass` có trong r170 | Đúng | `src/materials/Material.js` dòng 84 |
| 14 | Weber thông thường của thép tối trên đá sáng là số âm, trị tuyệt đối ≤ 1, nên "Weber ≥ 2" không đạt được | Đúng | Toán. Brief 2 đã bỏ Weber khỏi cổng (S2) |
| 15 | Atlas RGBA8: 1536×1024 = 6 MiB, 2304×1536 = 13,5 MiB, 3072×2048 = 24 MiB, mipmap thêm ⅓ | Đúng | Toán |
| 16 | `ff-f1-c4`, `ff-m1-c4` là 24 khung ở 12 fps, tức khoảng 2 s chuyển động gốc | Đúng | `art-src/lab/vfx/aura/manifest.json` |
| 17 | Lượt chạy 1: "không biết clip gốc 24 fps còn không" | Sai với thực tế dự án | Clip gốc của cả 26 ứng viên còn ở `~/VFXLab/inbox/firefly/immortality-cultivation/overnight/<id>/`; brief 2 đã ghi |
| 18 | "Camera ba phần tư nghiêng khoảng 55°" (lượt chạy 1, rà soát 2) | Chưa kiểm, không có nguồn | Brief không nói góc camera; ChatGPT tự đặt |
| 19 | Lời nhắc J-RING: "ba chi tiết ngọc xanh, đốc sen" | Sai | `WEAPON_DESIGN.md`: Clear Wind có lưỡi thẳng xuyên vòng ngọc rỗng có hai khuyết mây, đốc giọt ngọc. Lời nhắc này không dùng được nguyên văn |
| 20 | Cận cảnh "400–500 px/m" (lượt chạy 2, rà soát 1) | Sai đơn vị | Brief: 400–500 px trên màn |
| 21 | Phương trình trộn premultiplied `ONE, ONE_MINUS_SRC_ALPHA`: kết quả = nguồn + (1 − α)·đích; một fragment làm được cả viền tối (α cao, màu tối) lẫn lõi HDR | Đúng | Toán trên phương trình trộn; khớp `VFX_PRODUCTION_PIPELINE.md` §6.3; shader `rgba` của `flipbook.ts` đã premultiply một lần |
| 22 | `minterpolate` là nội suy bù chuyển động, khác trộn khung | Đúng | `ffmpeg -h filter=minterpolate` (kiểm ở `VFX_PRODUCTION_PIPELINE.md` §5.2) |
| 23 | Ngưỡng R_seam ≤ 1,2; ΔE 0,12 / 0,18 cho thân hiệu ứng; trần ink 0,25–0,55; 10–18 tia lửa mỗi đòn; nhịp va chạm 0–3 / 4–9 / 10–34 khung | Suy luận | ChatGPT tự ghi TRIAL; Claude chọn lại trong kế hoạch |
| 24 | Ink + thân + lõi: α = 1 − (1 − a_i)(1 − a_b)(1 − a_h); RGB = C_i·a_i·(1 − a_b)(1 − a_h) + C_b·a_b·(1 − a_h) + C_h·a_h | Đúng về toán (là phép "over" ba lớp, lõi trên cùng) | Toán; Claude dùng làm hợp đồng shader trong kế hoạch, lõi HDR chỉ ở vạch mảnh |


## Nguyên văn các lượt

Mỗi lượt bắt đầu bằng một dòng **[TURN · …]**. Brief và lời yêu cầu rà soát nằm trong khối chữ; câu trả lời của ChatGPT giữ nguyên Markdown của nó (tiêu đề của câu trả lời là tiêu đề của ChatGPT, không phải của tệp này).

---

**[TURN · Lượt chạy 1 · Brief 1 (Claude gửi, nguyên văn)]**

````text
Role: you are the analyst for a game project. Research, analyse and propose a concrete solution. Answer in English.

GOAL
Take the best Firefly Video candidates of last night (blind-judged 6.5-7) to the owner's bar of 8.5 and fix the open problems, as ONE ordered integration plan for the skills lab of "Tu Tien Thu Ai" (a browser typing game, three.js WebGL2, xianxia sword school, Metal and Fire elements). For each layer below give the most effective route to 8.5: the tool, the order of work, the risks, and how to measure and judge it. Layers:
1. Metal mantle around the flying sword ("Wind-Silk Mantle").
2. Fire sheath around the blade (flames licking around the dark hot-edged blade).
3. Tip star (a glint at the sword's point).
4. Key-1 Fire impact body (three brushstroke flame crescents), including its designed first and last frames for Firefly image-to-video.
5. Sparks.
6. Halo seal (thin rings, big blows only).
7. Dark backing so additive art reads on light stone.
8. Seamless loops without ghosting.
9. Burst-in for shapes that are complete at frame 0.
10. Slow decay ("fast attack, slow decay").

FACTS AND CURRENT STATE
Scale: play camera about 38 px/m. Swords on screen 60-130 px long; tip star 12-32 px; impacts 70-160 px; close-up 400-500 px. Grounds: light stone #d6d0c2, dark stone #2a2c30. Key 1 = three swords fly one after another to targets (hits at +6, +36, +66 ticks of 60 Hz). Key 7 = a river of 88 swords (6 lead swords drawn as full meshes, mid swords as LOD meshes, far swords as impostor quads).

Rejected by the owner: aura round 1 (a shader-drawn mantle: "crude, static, not sparkling"; an analytic 4-point tip star: "ugly"); the current Fire impact (a symmetric lotus flipbook: "looks like trash"); code-drawn cracks and scorch. A Blender Mantaflow route with flat stepped colour scored only 3.5-4.5 with both judges, so that route is stopped.

Overnight Firefly Video candidates (Adobe Firefly Video model; cut to flipbook atlases) and the two blind judges' scores (judge 1 / judge 2, 0-10, bar 8.5):
- ff-f1-c4 "aura-fire-flame-sheath": a card along the blade, soft slightly realistic flame licking both sides of a hot line, needle at the tip; black-background additive; loop 24 frames at 12 fps (the cut kept only 1 of 2 source frames). 7 / 7. Gaps: symmetric, does not sweep back with the flight; a big blob at the hilt end reads as a fire arrowhead; crossfade ghosting at frames 16-23; cream smear on light stone; no white-gold point or stars.
- ff-g1-c2 "tip-star-glint": white mask 4 long arms + 4 thin diagonal arms, tiny core, soft halo, grows, turns 45 deg, shrinks; 32 frames at 24 fps. 7 / 7. Gaps: core swells into a white blob at peak (32 % white), shape jitters at frames 8 and 18-19, a little stock-sparkle-like, 1.33 s too long for one flash, at 12 px only a dot.
- ff-m1-c4 "aura-metal-feather-mantle": silver feather plates with blue veins on both sides of a spine, blue silk threads meeting in a needle at the tip; loop 24 frames at 12 fps. 7 / 6.5. Gaps: solid and white, reads as an object (a feather or fern) not as qi, would hide the real blade, almost static silhouette, white block on light stone, one white streak at 60 px.
- ff-c3-c3 "fire-halo-seal-loop": hair-thin gold rings with breaks, slowly turning, small stars running on the rings; loop 32 frames. 7 / 6.5. Gaps: at 100 px the rings merge into one thick bangle; crossfade zone (frames 24-31) shows four stray bars like a "+"; rings slightly elliptical (w/h 0.93-0.96); generic light-painting rings, no engraved seal pattern; washes out on light stone.
- ff-a1-c5 "fire-crescent-sweep": image-to-video, the first frame was Firefly's own soft flame warped by a polar transform into three crescent strokes; Firefly kept the shape and gave smooth, slightly realistic fire that sweeps with the cut; 24 frames, straight alpha from a black background. 6.5 / 6.5. Gaps: the arc closes to about 300 deg and reads as a ring or a "C"; strokes even thickness (base-to-tip thickness ratio 0.81, no taper); no white-gold hot line (0 % white core); edges cut by the mask like a sticker, no glow beyond the edge; full shape at frame 0 (coverage 0.15 at f0 vs peak 0.19), no burst-in; it dies in 6 frames (0.25 s), against "fast attack, slow decay"; no sparkle layer.
- Also: ff-f1-c2 "aura-fire-ribbon" (soft rolling flame band that tiles in x, like a Dragonhold flame trail the owner praised) 6.5 / 6.5, too thick for a sheath, better as a sword trail; ff-g1-c3 "glint-gold-twinkle-set" (8 warm gold twinkles) 6.5 / 6.5, variants 5, 7, 8 bad (square blobs, a 5- or 6-point clip-art star, double flashes, pops at the end); ff-m1-c3 "aura-metal-windsilk" (fast thin silver qi streaks, tiles in x) 6 / 6, generic speed-line look; ff-b2-c2 spark spray 5.5 / 5.5 (grinder sparks: uniform orange, straight, zigzag mid-life, no white-gold heads, no gravity); ff-b2-c1 6 / 5 (jewel-like white-gold heads but a 360 deg firework); ff-b3-c3 gold dust 5.5 / 5 (stock glitter, bokeh-like).
- Judges' shared verdict: Firefly keeps the soft living fire the owner wants but lacks DESIGN: open arcs, tapered strokes, a thin white-gold hot core, a dark layer, "fast attack, hold, slow decay", and a sparkle layer. All additive art washes out or disappears on light stone. 8-frame crossfade loops ghost. At play size (60-110 px) details melt into one streak, so judging must happen at the real size in the play build.

Ticket 252 (a pilot, now stopped) painted three first frames for the key-1 impact (1536x1024, pure black, image model): v1 three nested crescents sweeping up-right from a strike point at lower left; v2 three strokes flicked from one root; v3 two long crescents plus a short counter-stroke. In Claude's look, v1 and v3 already show an open fan, a heavy base tapering to needles and a thin hot leading edge (unmeasured). Its rules: opaque 1080x1080 square on black (the mode that worked for ff-a1-c5), arc 120-180 deg, taper >= 3:1 measured at 20 % and 80 % of the centreline, white-gold hot line on the leading outer edge, last frame made in the image tool's EDIT mode from the chosen first frame (same strokes burned down to thin ember lines, 15-35 % of the first frame's bright area, >= 70 % inside the first frame's mask). Known risk: a painted first frame may carry a painterly look that Firefly keeps.

Runtime today (code facts):
- FlipbookPool: atlases stored with straight alpha, the shader premultiplies; blend One / OneMinusSrcAlpha; modes rgba, fire, smoke, heat; default frame blend is a crossfade of two frames and loops wrap to frame 0 (so loop seams are crossfaded); also a "stepped" mode and an rgba "hold and erode" mode (each pixel switches at its own noise-driven moment); per-instance erode and cool (burn-out by erosion); a slowFrom / slowRate time map; NO motion-vector support; NO per-instance dark backing (fire mode only has an "occlude" term that darkens the ground by luminance); the manifest has no rows/variants, frames run row-major.
- Aura round 1 drawer (WindSilkMantle): MantleSheath = instanced cards along the blade axis (analytic plates plus a greyscale streak texture), MantleHull = back-face shell on lead swords, SilkTail = ribbon, MantleHalo = analytic halo inside the far-sword impostor quad, TipStar = analytic 4-point star. All premultiplied, with an ink term already (Metal indigo ink alpha 0.35, Fire soot alpha 0.85). Flame tiers: tongues only on <= 14 swords per frame (6 lead + 8 mid), mids get an "ember mantle", far swords a broken ember rim.
- Fire kit today on key-1 impact: the lotus flipbook, a spark-ray atlas, analytic ember dots, analytic heat rings, an analytic ground seal, procedural scorch decals.
- Budgets: aura on Metal <= +0.6 ms p95 on key 7 (hunt), Fire over Metal <= 0.85 ms p95 on key 7 at High, no window above 11.5 ms; <= 2 transparent layers per pixel inside each sword's area; light bodies <= 0.85-0.9 per channel, only thin HDR cores bloom. Reserved colours that must stay distinct: enemy warning red #FF4A4A, typing teal #7FF5E0, money gold #FFC83A. Mac mini M4, WebGL2 through ANGLE/Metal (GPU timer queries are unavailable there, so GPU time is measured as frame-time deltas).
- Existing gates and tools: blade-keep (share of blade pixels whose colour stays within dE OKLab 0.04 of the aura-off frame: >= 90 % lead and mid swords, >= 85 % far; jade ring and guard >= 95 % every frame; no layer covers > 10 % of the blade); per-layer overlap; perf A/B scenarios; tools/vfx-flipbook (atlas, contact sheet, metrics from a clip); ffmpeg minterpolate (measured -26 % interpolation error vs plain crossfade on fire frames); numpy/scipy/Pillow.

Research already decided (VFX_PRODUCTION_PIPELINE, both of you reviewed it last night):
- Shape from a designed image; inner motion from Firefly Video; colour steps, dark rim and white core in the shader; placement, timing, direction and erosion in code. Code never draws the main shape.
- Anything attached to an object or following a path is a mesh or ribbon carrying a scrolling texture with erosion; flipbook cards only for short chaotic things (impact body, smoke).
- Glints and sparks are painted sprites on GPU particles (InstancedMesh), velocity-stretched, screen-size clamped; seals are a painted design turned into an SDF or MSDF; analytic rings only for hairlines.
- One premultiplied layer does both a dark rim (dark colour, high alpha, 0.35-0.75, broken, never a uniform black outline) and an HDR core (low alpha). Colour steps via a 1D LUT. Erosion, not fading.
- Never play a flipbook slower than its source rate without interpolation.

CONSTRAINTS
- Tools: Firefly (Adobe models only: Firefly Video, Firefly Image, Firefly Upscaler for images; NEVER partner models; the Firefly video upscaler is Topaz, banned). Firefly Video: 24 fps, 5 s; transparent background works only at 540p 16:9 (a 1080p transparent run fails silently); black backgrounds at 1080p (16:9 or 1:1); first frame and last frame inputs. 2D images (first frames, painted masks, a jade ring repaint) are painted by ChatGPT or Gemini after the design passes review. The local Codex CLI writes code, logic and sound only from a complete solution (model gpt-6.1-sol, effort xhigh or ultra for code). Claude coordinates, drives the browser, processes clips, measures and runs blind judges. No local AI models. Blender headless is available but its stepped-fire look failed.
- Acceptance: two independent blind judges BOTH >= 8.5 in the built play host at the player's settings, no URL flags; judged at the play camera and close, on light and dark stone, at real speed and 0.25x. When anything reaches 7, the owner gets a demo video. Three tries without a gain: stop and change the method.
- Measurable checks we want per package: first frame >= 95 % of peak brightness (flash and core drawn at age 0); white-out (luminance >= 0.95) <= 6 % of the field every frame; dE OKLab of the effect vs light stone and vs dark stone; GPU time per layer; loop seam (last-to-first difference vs the median frame-to-frame difference; no ghost bars).
- Lab: the skills lab stays instant-cast (no typing wait). Media never goes into Git.
- Do not name games, studios or characters in Firefly prompts; avoid "cinematic", "realistic", "volumetric", "lens flare", "bokeh", "depth of field"; prompts under 600 characters.
- No third-party reference images go into any AI tool; the repo's own candidate sheets are fine.

ALREADY DECIDED BY THE OWNER (do not reopen)
- Sword aura: direction A "Wind-Silk Mantle" (a tailored mantle of qi plates outside the blade edge, a 1 px ink gap between steel and mantle, two seams meeting in a needle past the tip, open collar around the jade ring, a silk tail) plus ONE layer of direction C: the tip star. Nothing else from B or C.
- Q3: the Fire blade is dark steel with hot edges; flames lick AROUND the blade, never paint the blade.
- Q4: the jade ring of the sword model (it renders chrome-silver today) is repainted white jade with a pale gold rim, "as in the approved image".
- Fire mix: body = A Brushfire Calligraphy (3 big flame strokes curving with the cut, 4-5 small counter-strokes and a few detached licks, sharp edges on a dark underlay, stepped colour, white core <= 5 %, dies by strokes tearing apart and eroding from the tips); sparks and glints = B Starfire Jewel (thin streaks, white-gold heads, cooling red tails, three lengths, 2-3 clumps along the blow, gravity, a few bounce once; per blow 1 big 4-point star and 2 small ones flashing in turn; gold dust in the aftermath); halo = C Halo Seal thin rings ONLY on big blows (cast from a seal, key 7's lead sword diving, the finisher, ultimates). Orange-red stays (no jade "strange fire"). Heat haze later, with Water.
- Readability (owner approved): key 1's first sword hangs a beat pointing at its target, then flies; its first hit moves from +6 to about +18 ticks (a deliberate gameplay change: canon, content data and golden hashes change on purpose). Fixes after the aura lands (same files): T1 swords 2 and 3 leave the shoulder 0.25-0.3 s before their hit tick and slow down, last 8-10 frames <= 12 px/frame; T4 a gate: every lead sword >= 12 frames at >= 40 px long and <= 12 px/frame between appearing and hitting (threshold tuned to the owner's eye); C1 the Fire blade contrast measured in the FINAL image against the real background including VFX: dE OKLab >= 0.25 and Weber >= 2, idle and in flight; C2 VFX over the blade <= 5 % in flight, counting the fan behind the shoulder and the trail; R1 cheap anti-aliasing (FXAA or SMAA) at High.
- Owner rules: fast attack, slow decay (hold the peak, burn down by erosion, never a quick fade); every shape sparkles, with no clip-art stars; anime, donghua and myth, radiant, luxurious, captivating, never realism as the goal; every item and skill object carries a presence layer.

TASTE
Anime/donghua and myth: radiant, haloed, luxurious, captivating, stylish and modern; rich layered detail, strong silhouettes, premium materials, light accents; never plain, never realistic as the goal.

DELIVER
1) Analysis: for each of the 10 layers, why the best candidate stops at 6.5-7 and what exactly must change (shape, motion, light, sparkle, backing, timing).
2) The solution as ordered work packages. For each: the layer; the source asset or candidate id to start from; the tool; the worker (ChatGPT/Gemini for images, Firefly, Codex for code, Claude for browser/processing/judging); the processing steps; the runtime approach (card flipbook vs mesh/ribbon with scrolling texture vs particles vs SDF), with numbers (frames, fps, cell size, alpha thresholds, erosion curve, hold times, backing alpha); the measurable checks with thresholds; the capture scenario and the blind-judge step. Say which packages can run in parallel and which must wait.
3) The new art needed, with complete prompts (Firefly Video prompts under 600 characters; image prompts for first and last frames and masks), and how many candidates per item.
4) Specific answers: (a) how to make loops seamless without crossfade ghosting; (b) how to reconcile "first frame >= 95 % of peak" with a burst-in for shapes complete at frame 0; (c) how to build a dark backing that reads on light stone without a black sticker outline and without breaking the 2-layer cap; (d) whether the sheath and mantle should use the card flipbooks as-is, or be rebuilt as scrolling textures on a blade-hugging mesh; (e) how to keep the real blade visible (blade-keep gate) with a mantle that judges called "solid white".
5) Risks and how to check each.
6) What you are not sure about.
Cite a source for every factual claim (official docs: three.js, Adobe helpx, Khronos, GDC or the maker's article). Mark guesses as guesses.
````


---

**[TURN · Lượt chạy 1 · Câu trả lời 1 của ChatGPT (nguyên văn, 65.050 ký tự)]**

# Tu Tien Thu Ai — VFX Production Plan: From 6.5–7 to 8.5+

Research and integration specification · November 4, 2026 · three.js / WebGL2 · Metal and Fire

## 1. Executive decision

Keep Firefly as the source of organic motion. Stop asking it to design the final effect. The best route to 8.5 is to preserve its strongest contribution—living flame and flowing light—while transferring control of silhouettes, timing, compositing and readability to authored artwork and the runtime.

The overnight candidates are not a failed technology experiment. They establish useful motion references, but most are not suitable as final assets.

| Component | Production decision |
| --- | --- |
| Metal mantle | Redesign as a sparse, blade-hugging mesh with scrolling painted qi textures. Preserve the Wind-Silk direction, not the solid feather silhouette. |
| Fire sheath | Reuse Firefly's flame motion on a shaped, blade-hugging mesh. Remove the hilt blob and introduce backward flow. |
| Tip star | Replace the full animation with a short, curated painted glint played through instanced sprites. |
| Key-1 impact | Prioritize Ticket 252 v1 and v3. Author the first and last frames, then use Firefly for motion inside the three open crescents. |
| Sparks | Abandon baked spark sprays. Use authored sprite shapes with GPU-instanced ballistic particles. |
| Halo seal | Replace the light-painting loop with an engraved, painted seal converted to SDF/MSDF; animate it in code. |
| Backing | Use one premultiplied shader layer for dark, broken ink and narrow luminous cores. |
| Loops | Eliminate the current eight-frame crossfade. Use seamless texture flow, verified cyclic clips, or non-looping effects. |
| Burst-in | Reveal a finished bright shape spatially rather than fading an already complete flipbook. |
| Slow decay | Hold designed shapes at full intensity, then erode them non-uniformly, preferably stroke by stroke. |

### What actually separates 7 from 8.5

The decisive improvements should be:

1. Recognizable authored shapes at 60–160 px. At this scale, cleaner silhouettes matter more than additional interior detail.
2. Directional motion. The mantle, sheath, strike and sparks must all agree on the sword's travel direction.
3. Controlled luminance. Thin hot lines and small stars create brilliance without turning the whole effect cream-white.
4. Deliberate contrast. Broken dark ink restores shape against light stone without making every effect look outlined.
5. Designed attack and decay. The visual event needs an immediate strike, a readable peak and a satisfying aftermath.
6. Integration at the actual play camera. A beautiful isolated flipbook is not evidence of a successful skill.

These are production hypotheses based on the supplied judge reports, not guaranteed score improvements.

### Three technical corrections before implementation

First: first-frame brightness and burst-in are compatible only if they describe different measurements or different moments. If a shape starts from zero visible coverage at age zero, its total visible brightness cannot also be at least 95% of its eventual peak. Apply the 95% rule to the hot contact flash at age zero; measure the complete decorative body's reveal separately. Alternatively, make the whole visual strike already complete at age zero and use a short pre-impact reveal during the preceding sword motion.

Second: the dark-backing approach needs correct premultiplied compositing. With `ONE / ONE_MINUS_SRC_ALPHA`, an output of premultiplied dark colour plus a controlled emissive contribution is mathematically possible in one pass. The emissive value must be managed separately from the opacity; low alpha alone does not produce brightness. This is consistent with the documented blend factors, but the exact result depends on the render-target and tone-mapping pipeline.  [MDN +2]

Third: the Fire blade's Weber contrast gate needs a precise definition. Using conventional Weber contrast, $C_W=(L_\text{blade}-L_\text{background})/L_\text{background}$, a dark blade against a brighter stone background has contrast between −1 and 0. Therefore, a requirement of Weber ≥ 2 cannot be met for that dark-on-light comparison. Preserve the owner's visibility objective, but implement separate signed dark-on-light contrast and a threshold appropriate to that sign. Keep OKLab ΔE ≥ 0.25 as the independent colour-distance gate.

One additional source qualification: Adobe documents 24 fps generation, first/last frames and transparent-background options, but I could not verify from its documentation that transparency universally works only at 540p 16:9. Treat the reported 1080p failure as a confirmed project-specific observation, not a universal Adobe limitation. The black-background 1080p path remains the recommended controlled production route.  [Firefly +1]

All numeric tuning values below are proposed acceptance targets, except the budgets and requirements explicitly fixed in the brief.

## 2. The ordered implementation schedule

The work should be organized into eleven packages. The first three establish the rendering and measurement foundation. The Fire impact is the first major art milestone; the aura and supporting effects follow.

| Order | Package | Dependencies and parallel work |
| --- | --- | --- |
| WP0 | Measurement and reference harness | First. Codex + Claude. |
| WP1 | Premultiplied compositor and dark backing | After WP0. Codex. Image design may start concurrently. |
| WP2 | Loop, atlas and timing infrastructure | Parallel with WP1. Codex + Claude. |
| WP3 | Key-1 Brushfire impact body | Artwork starts after shape review; runtime integration needs WP1–2. |
| WP4 | Metal Wind-Silk mantle | Art parallel with WP3; runtime after WP1–2. |
| WP5 | Fire blade sheath | Share WP4's mesh system; art parallel. |
| WP6 | Tip star and skill glints | Art parallel; integration after WP4–5. |
| WP7 | Starfire Jewel sparks and dust | Artwork parallel; final tuning after WP3 and WP6. |
| WP8 | Big-blow Halo Seal | Independent SDF artwork; integrate after WP1. |
| WP9 | Burst-in and slow-decay timing | Timing engine built with WP2; final profiles after art integration. |
| WP10 | Gameplay, performance and blind acceptance | After WP3–9; includes approved timing and readability fixes. |

Priority: WP3 is the most important artistic replacement because the current key-1 impact has an explicitly rejected silhouette. WP4 and WP5 should take the next substantial share of work because the sword occupies the screen continuously. WP8 is polish for selected large blows, not a prerequisite for the ordinary key-1 effect.

### WP0 — Establish the baseline and acceptance harness

Worker: Codex implements instrumentation; Claude captures, measures and coordinates judging.
Tools: Existing `tools/vfx-flipbook`, NumPy/SciPy/Pillow, deterministic scene replay, frame captures and A/B performance harness.

The harness should produce the following outputs for every candidate:

| Measurement | Proposed gate |
| --- | --- |
| Output play resolution | 1280 × 720 reference, plus the owner's actual display settings |
| Blade preservation | Existing ≥90% lead/mid, ≥85% far; guard/jade ≥95% |
| Direct VFX blade overlap | Existing ≤5% Fire in flight; no individual layer over 10% |
| White-out | ≤6% of the defined effect field, every frame |
| Tip-star white-core area | ≤4% of its sprite bounding region, initial target |
| Visible effect contrast | Proposed ΔE OKLab ≥0.12 for principal strokes on both backgrounds; ≥0.18 for the focal highlight |
| Loop seam | Difference ratio ≤1.2, with no visible double image |
| Metal key-7 overhead | ≤0.60 ms p95 frame-time delta |
| Fire overhead over Metal | ≤0.85 ms p95 frame-time delta |
| Frame-time ceiling | Existing 11.5 ms window requirement; define the exact window statistic before testing |
| Artistic acceptance | Both independent judges ≥8.5/10 |

The ΔE values are initial engineering targets, not externally established perceptual thresholds. Tune them against the two judges; don't optimize toward ΔE at the expense of appearance.

Measurement details:

- Calculate OKLab distance from linearized final rendered RGB, using locally sampled background pixels and identical exposure. Also record screenshots in display sRGB. Three.js explicitly distinguishes linear working colours from sRGB output; mixing them would invalidate comparisons.  [Three.js +1]
- Use a fixed effect region of interest, not the whole 1280 × 720 screen, for the 6% white-out test. Otherwise a small white blob could pass trivially.
- Count blade occlusion by projecting blade and guard masks from an aura-off render onto the final render. For ΔE, test each sword individually as well as all 88 together.
- Benchmark fixed replay paths with the same camera, particle seed, viewport, DPR, antialiasing and warm-up. Alternate runs A/B/B/A rather than comparing one isolated A run with one B run.
- Report rendered frame-time deltas, not GPU milliseconds. On this Mac, no timer-query result is available. WebGL GPU timer queries require the relevant extension; availability is not universal.  [MDN]
- Capture a layered debug sheet: bare scene, blade only, backing only, effect body, hot core, particles and final composite.

Required captures: Key 1 at its new first-hit tick, the following two hits, Key 7 with all 88 swords, both stone backgrounds, play and close camera, real speed and 0.25×.

Judge procedure: Claude randomizes labeled A/B videos, collects independent scores before showing implementation details, and logs the precise version/seed. When a candidate reaches 7, the owner receives the demo. The final score is evaluated in the unmodified play host, not the isolated VFX viewer.

### WP1 — One-layer backing, colour steps and thin HDR cores

Layer: 7, the dark backing.
Source: Existing Metal indigo ink, Fire soot and accepted mask art.
Worker/tool: Codex; GLSL material in three.js. Claude measures.

This should be implemented before judging any new Firefly artwork, because the background problem currently penalizes nearly every candidate.

Proposed shader structure

```glsl
 // Conceptual fragment-compositing core.
 // All colors and emission are in linear RGB.
 // Texture channels are authored data, not color-managed RGB.

float coverage = texture(effectMask, uv).a;
float coreMask = texture(effectMask, uv).r;
float inkMask  = texture(effectMask, uv).g;
float persist  = texture(effectMask, uv).b;

// Erosion and blade exclusion are evaluated before blending.
float bodyA = coverage * bodyOpacity * survival * bladeExclusion;
float inkA  = clamp(inkMask * inkStrength, 0.0, 0.75)
              * survival * bladeExclusion;

// Two conceptual surfaces combined into ONE fragment.
// Body in front of its dark backing.
float outA = bodyA + (1.0 - bodyA) * inkA;

vec3 premulRGB =
    bodyA * bodyColor
  + (1.0 - bodyA) * inkA * darkColor;

// Only a narrow hot mask emits extra HDR light.
vec3 emissive = coreMask * survival * hotIntensity * hotColor;
premulRGB += emissive;

outColor = vec4(premulRGB, outA);
// Material: CustomBlending, src=ONE,
// dst=ONE_MINUS_SRC_ALPHA.
```

This is a proposed implementation, not shader code from a published source. Its composition follows the documented blend equation.  [MDN +1]

Material settings: transparent true, depth test true, depth write false, one-sided or `forceSinglePass` where applicable, explicit render ordering where necessary. Verify with the project's three.js version and its actual rendering pipeline.  [Three.js Docs]

Starting parameter ranges

| Feature | Metal | Fire |
| --- | --- | --- |
| Dark ink colour | Deep indigo-grey | Soot/burgundy-brown |
| Dark ink alpha | 0.35–0.50 | 0.45–0.70 |
| Main body alpha | 0.10–0.35 | 0.25–0.55 |
| Hot core share of shape | 1–3% | 2–5% |
| Core thickness at play size | 1–1.5 px | 1–2 px |
| Background irregularity | 15–30% broken segments | 20–35% broken segments |
| Maximum body output | Existing 0.85–0.90/channel limit | Same |

The ink must follow the actual authored contour rather than an evenly dilated silhouette. On light stone it supplies visual structure; on dark stone the luminous body and core must remain readable even if the ink contributes little.

For overlapping dark and bright regions, the single-fragment equation must be verified against an explicit two-pass reference image. It will not automatically reproduce arbitrary two-layer ordering. This matters particularly for semi-transparent fire.

HDR check: Before relying on emissive values greater than 1, confirm a compatible floating-point render target and blending path. WebGL2 supports float-renderable formats through extensions, and three.js documents half-float output for HDR pipelines. If the actual compositor clamps emission before bloom, low-alpha HDR cores will not behave as intended.  [MDN +3]

Acceptance: A/B the same existing Firefly flame with old additive versus new backing on both stones. Require no sticker-like continuous border, no visible dark rectangle, and a measurable improvement on light stone without losing the soft living motion.

### WP2 — Repair loop handling and the atlas pipeline

Layer: 8, seamless loops.
Source: `ff-f1-c4`, `ff-m1-c4`, `ff-c3-c3` as failing test inputs.
Worker/tool: Codex modifies `FlipbookPool` and manifest; Claude processes with FFmpeg and NumPy.

Implement three explicit playback types:

| Type | Use | Rule |
| --- | --- | --- |
| `scroll_periodic` | Metal and Fire sheath interior, silk tail | Continuous UV scrolling with a truly tileable texture |
| `loop_discrete` | Only validated cyclic secondary motion | Loop frames with no automatic eight-frame crossfade |
| `oneshot_erode` | Impact, glints, sparks, seal entrances | No wrap; hold/end by spatial erosion |

Do not attempt to fix the old crossfade merely by making it shorter.

For a moving flame silhouette, blending unrelated frames combines both silhouettes. That is precisely the double-image problem reported at frames 16–23. The approved fix is a periodic source or a transition aligned by motion, not arbitrary blending.

Claude should calculate:

$$R_{\rm seam} =
\frac{\operatorname{MAE}(F_{N-1},F_0)}
{\operatorname{median}_{i=0}^{N-2}\operatorname{MAE}(F_i,F_{i+1})}$$

Use premultiplied RGB and alpha for the measurements. Require $R_{\rm seam}\leq1.2$ as an initial threshold. Report tiny denominators separately rather than treating a nearly static clip as a perfect loop.

Additional gates: no frame containing an isolated cross-shaped artifact, no doubled edges over 2 px at play size, and no abrupt silhouette shift.

Atlas standards:

- Sheath/mantle trial atlas: 24 frames, 6 × 4, 256 px slots, 240 px usable art with internal gutters; atlas 1536 × 1024.
- High-detail impact: 24 frames, 6 × 4, 512 px slots; atlas 3072 × 2048. Reduce to 384 px cells if memory or texture bandwidth becomes costly.
- Glint trial: 12 frames, 4 × 3, 128 px slots; atlas 512 × 384.
- Use 4–8 px edge-safe padding, explicit frame rectangles, and packed-channel manifests with versioned layout.
- Preserve texel padding through mipmap generation, and prevent sampling neighbouring atlas cells.

Three.js documents texture filtering, mipmaps and wrapping, including `RepeatWrapping`. Periodic textures should repeat only on the intended scrolling axis; packed atlases should use cell-bounded UV sampling rather than repeating the entire atlas.  [Three.js Docs +1]

Interpolation: Keep `ffmpeg minterpolate` as an offline option for genuinely intermediate motion frames, especially where your measured interpolation error improved by 26%. FFmpeg documents motion-compensated interpolation separately from simple frame blending. It is not a substitute for an actual periodic animation and should not be used to bridge a completely different last/first silhouette.  [FFmpeg]

Acceptance: Test every loop for at least ten repeats at 1× and 0.25×. A loop that is mathematically close but visibly freezes, reverses or pops fails.

## 3. Art-production packages

### WP3 — Key-1 Fire impact: Brushfire Calligraphy

Starting assets: Ticket 252 v1 and v3; `ff-a1-c5` is a motion reference only.

Workers: ChatGPT/Gemini paint the authored frames; Adobe Firefly Video animates them; Claude extracts and evaluates; Codex integrates the selected asset.

This is the largest opportunity for an immediate qualitative improvement.

Why 6.5: The current animation demonstrates good flame movement but has a nearly closed, uniform-width arc, no developed hot edge, and an abrupt disappearance. The 300° arc is particularly damaging: a player reads a circle before reading three sword-cut strokes.

Design:

- Three dominant crescent strokes, each covering approximately 120–180°.
- Four or five short counter-strokes, with two or three detached flame tongues.
- At least 60° of meaningful open space in the overall sweep; no connecting outer ring.
- Taper ≥3:1, measured between 20% and 80% of each principal stroke's centreline.
- Leading white-gold edge, ≤5% of the main luminous region.
- Dark broken backing; edges that feather into fine tongues without losing the three main silhouettes.
- Stroke directions must follow the sword strike, not rotate like a circular explosion.

Production route

1. Review Ticket 252 v1 and v3 at actual impact size. Select the stronger one, or make a minimal edit to fix one identifiable defect.
2. Prepare each selected first frame as an opaque 1080 × 1080 image on black, with no cropping or automatic recentering.
3. Create its last frame in image EDIT mode: same stroke positions, reduced to ember remnants. Require 15–35% of the initial bright area, and ≥70% of remaining bright pixels inside the original stroke masks.
4. Use Firefly Video with the first and last frames. Produce two motion candidates for each of the two designs—four video generations initially.
5. Extract 20–24 useful frames at 24 fps from the generated 5-second clips. Select by motion continuity and silhouette retention, not simply the first 24 frames.
6. Derive separate channels for body coverage, hot core, dark backing and erosion persistence. Hand-correct the masks where automatic extraction merges two strokes.
7. Feed the selected frames into `FlipbookPool` as `oneshot_erode`, with no loop or crossfade.

Adobe documents use of both first and last frames as transition guidance. However, it does not promise that the middle of the clip preserves exact painted topology. For that reason, every Firefly output must be checked for stroke mergers, spontaneous new shapes and geometry drift.  [Firefly]

Proposed timing

Key-1 Fire impact visual envelope

60 Hz ticks relative to contactProposed maximum visual lifetime; the bright main-body area should diminish substantially before the next key-1 hit. Exact hold and erosion speeds are adjustable after live judging.At contact, the compact hot strike is already bright. The large crescents complete their expansion over roughly 3–4 ticks. Their peak silhouette then holds for approximately 6–8 ticks before breaking and eroding over 20–28 ticks. A weaker ember residue can remain longer.

Measurements and acceptance:

| Criterion | Proposed threshold |
| --- | --- |
| Main stroke count | Exactly 3 readable at 70–160 px |
| Arc design | 120–180°; no closed ring |
| Taper | ≥3:1 |
| White-gold core | ≤5% |
| First-frame strike brightness | ≥95% of strike peak |
| Last-frame overlap | ≥70% with original shape |
| Last-frame bright area | 15–35% of first |
| Bright main-body erosion | At least 3× longer than attack |
| Close-up | No clipped masks or obvious pixelation at 400–500 px |

Judge: First the three-stroke shape on light/dark stone without supporting particles. Then judge again with sparks and glints. Never accept a weak impact body simply because particles make the finished effect busier.

Fallback after three unsuccessful tries: Stop Firefly shape generation. Keep the best authored static shape, use the existing flame movement only as an interior animated texture, and let runtime erosion create the temporal progression. This changes the method without returning to procedural main-shape drawing.

### WP4 — Metal Wind-Silk Mantle

Layer: 1.
Starting assets: `ff-m1-c4` for plate language and `ff-m1-c3` for moving silk threads. Neither is acceptable as a final full-card aura.

Workers: ChatGPT/Gemini paint two revised mask designs; Firefly Video supplies interior qi motion; Codex implements the geometry; Claude performs blade-keep and visual comparisons.

The current 7/6.5 mantle contains too much nearly opaque silver material. It looks like a second sword-shaped object rather than a field of qi.

Geometry and authored design:

- Retain the two tailored seams, an open collar, a needle past the tip and one trailing silk ribbon.
- Replace large feather plates with separated, irregular suggestions of plates: broken scalloped edges, gaps, tapered filaments and occasional luminous veins.
- Leave at least 60–70% of the mantle's projected rectangular envelope visually open.
- Begin the mantle outside the real steel edge, preserving the approved 1 px ink gap at play resolution.
- Extend the needle approximately 3–7 px beyond the visible sword tip on a 100 px reference sword.
- Keep the guard and jade ring visually open; do not add a luminous collar across them.
- Let the mantle envelope deform gently while fine internal threads travel from the hilt toward the tip or sweep backward along the outer seams.

Runtime choice: Blade-hugging UV mesh with scrolling painted qi textures, not a full-card Firefly flipbook.

Use a single batched geometry containing the two mantle side strips where possible. Drive per-sword variation with instance attributes and UV phase offsets. `BufferGeometry` supports custom vertex attributes; `InstancedMesh` reduces draw calls when multiple objects share geometry and material.  [Three.js Docs +2]

Initial runtime values

| Setting | Proposed value |
| --- | --- |
| Painted motion source | 24 fps, select a clean 24-frame segment |
| Actual runtime motion | Continuous scrolling, not indexed card playback |
| Texture atlas | Two 512 × 128 or 1024 × 128 seamless strip variants |
| Scroll rate | 0.6–1.2 texture repeats/sec |
| Envelope breathing | 2–5% width variation, ~0.4–0.7 Hz |
| Blade-side opening | ≥1 px in final play capture |
| Main qi body alpha | 0.10–0.35 |
| Indigo ink backing | 0.35–0.50, broken |
| Strong white coverage | ≤2% of mantle region |
| Readable tail | 8–20 px for a 100 px sword, adjusted for motion |

These are tuning hypotheses. The continuous scrolling source can be created by extracting and phase-matching a texture strip from Firefly, or by designing a naturally tileable painted strip and adding movement with UVs.

Critical blade-preservation method

Apply the blade exclusion before colour and emission:

$$M_{\rm final}=M_{\rm authored}\,(1-M_{\rm protectedBlade})$$

The protection mask should include the blade, the hilt collar and a conservative guard/jade region. The shape should already avoid these areas geometrically; the mask is a safety net, not the primary design.

Avoid an expensive full-screen blade mask for every sword unless profiling proves it necessary. Initially use a blade-local exclusion corridor and geometry that physically stays outside the blade. For the lead swords, the projected screen-space footprint can be compared against the blade-off screenshot to detect violations.

Measurement: Same sword at 60, 100 and 130 px; both grounds; stationary, flying and rotating. Require blade-keep, jade-ring keep and stable one-pixel separation. At 60 px the mantle must still read as two distinct luminous seams rather than one solid white streak.

Judge: Compare new Metal mantle against aura-off and `ff-m1-c4`, using identical sword motion. Score identity and luxury separately from blade readability.

### WP5 — Fire blade sheath

Layer: 2.
Starting assets: `ff-f1-c4` (primary motion); `ff-f1-c2` (secondary trailing ribbon motion).

Workers: ChatGPT/Gemini design the new asymmetric sheath mask; Firefly supplies the flame source; Codex reuses WP4 geometry; Claude tests both the blade and flame.

Why 7: The living flame is good, but the sheath is symmetrical, the hilt-end blob creates an unwanted arrowhead, and the entire effect lacks travel direction. The pale body becomes a cream streak on light stone.

The 8.5 route is to preserve the flame's softness while replacing the exterior silhouette.

Design rules:

- The steel remains dark and readable, with its own hot edges. The fire is outside the blade.
- Upper and lower flame tongues must not be mirror images. Start with a 65:35 visual-weight split.
- Tongues lean backward relative to sword velocity, with approximately 20–40° of trailing inclination.
- Remove the bulb at the hilt. A small fragmented ignition collar may exist behind the blade root, but not as a filled arrowhead.
- Retain fine, fast licks within a broader, slower outer shape.
- Let the pointed Fire sheath end in a needle, with the separate white-gold tip glint handling the sharpest highlight.

Runtime: A blade-hugging strip mesh with moving texture, sharing WP4's geometry and instance system. A narrow silk/flame tail may use a separate ribbon, but its projection must not exceed the two-transparent-layer cap inside the blade region.

| Parameter | Initial value |
| --- | --- |
| Firefly motion segment | 24 frames at 24 fps, for source extraction |
| Main texture | 512 × 128 strip, 2 alternatives |
| Flow | 0.8–1.5 repeats/sec, adjusted to velocity |
| Tongue length | 6–12 px on a 100 px sword |
| Blade gap | ≥1 px |
| Soot backing alpha | 0.45–0.70 |
| Flame body alpha | 0.25–0.55 |
| Thin hot edge | 1–2 px |
| Active full flame tier | Existing ≤14 swords/frame |
| Distant swords | Broken ember rim; no extra tongues |

Do not simply clamp the existing flame card into a narrow rectangle. That would preserve the arrowhead and symmetry inside a different container. The authored sheath mask must reshape the source flame, and the motion texture should be extracted where it provides interesting turbulence.

Accept: Fire blade final-image contrast on both grounds, all blade-keep gates, recognizably backward-sweeping flame in motion and no hilt-end bulb. Judge with the real sword model and the approved white-jade guard, never the flame alone.

### WP6 — Tip star and secondary glints

Layer: 3.
Source: `ff-g1-c2` for movement study; reject its swelling peak. `ff-g1-c3` is only a source of possible small glint variations.

Workers: ChatGPT/Gemini paint the star masks; Codex builds the particle-sprite atlas player; Claude removes unstable animation frames and judges.

The observed 7/7 star has a good underlying idea, but at the actual 12 px minimum it cannot sustain eight equally important arms. Its core is too large, and its 1.33-second animation is far too long for one decisive flash.

New specification:

- One primary four-point star with two dominant tapered arms and two subordinate arms.
- At 12–16 px, suppress the faint diagonal arms rather than allowing eight arms to merge.
- At 24–32 px, permit fine secondary diagonals, but keep them much dimmer than the main four.
- Compact core: roughly 1–2 px at normal play size.
- No large white central disc; hard-limit the bright core to ≤4% of sprite ROI.
- A faint, broken darker companion contour may help on light backgrounds.
- Add asymmetry through arm taper, length and the trailing glint, not by constructing a clip-art star.

Runtime: Instanced camera-facing sprite, 8–12 curated frames at 24 fps, one-shot. Main flash duration 0.12–0.22 seconds; faint twinkle tail can continue another 0.10–0.15 seconds without retaining a full-sized star. Optional small rotation should be subtle and monotonic.

For a sword tip, anchor the star just beyond the physical tip, approximately 1–3 screen pixels, rather than overpainting the steel. Use a 12–32 px screen-size clamp in the owner's play configuration.

For major impacts, reuse this design language: one large and two small stars, flashing consecutively rather than simultaneously.

Measurements: Track core radius and centroid frame to frame; reject sudden jumps over roughly 1 px at 24 px display size. No secondary flash at the end. At 12 px, the star must be distinguishable from an ordinary round particle in a frozen capture and at real speed.

Judge: First against the rejected analytic tip star, then attached to Metal and Fire swords. Reject if judges call it stock sparkle, coin-like or visually distracting during typing.

### WP7 — Starfire Jewel sparks and gold dust

Layer: 5.
Source: `ff-b2-c1`, `ff-b2-c2`, `ff-b3-c3` are negative examples and occasional shape references—not animation assets to keep.

Workers: ChatGPT/Gemini paint the particle sprites; Codex builds movement and batching; Claude judges and measures.

Why the previous sprays scored 5–6: The sparks lack hierarchy and physical direction. They behave either like uniform grinder sparks, a radial firework or generic floating glitter.

Firefly Video is the wrong place to solve their trajectories. The trajectories belong to the game's deterministic effect system.

Asset: One sprite sheet with three stretched-head lengths, compact white-gold heads, orange-red tapering tails, plus a separate sparse dust mask.

GPU movement:

- Spawn in 2–3 directionally coherent clumps along the sweep.
- Proposed ordinary key-1 hit: 14–22 sparks, not a full radial spray.
- Three starting length groups: roughly 4–7 px, 9–15 px and 16–25 px at play scale.
- Initial trajectories follow the sword-cut tangent plus controlled angular scatter.
- Apply downward screen-projected gravity, starting around 180–350 px/s² and tuning to the game camera.
- Lifetime ~0.15–0.45 seconds.
- Permit only a small minority to bounce once, with restitution approximately 0.25–0.40.
- Head colour evolves white-gold → amber/orange → red-dark ember; cooling belongs to colour and erosion, not uniform opacity fading.
- Spawn a few much smaller gold-dust motes in the later decay, not a persistent glitter cloud.

This is a stylized ballistic model, not a claim of physically accurate gravity at the game scale.

Use one instanced particle batch with per-instance age, velocity, seed, sprite variant and colour profile. Three.js `InstancedMesh` is specifically intended to reduce draw calls for multiple objects sharing geometry and material.  [Three.js Docs +1]

Checks: No 360° firework; no zigzag trajectory unless collision-driven; three readable sizes; no stock bokeh disc; no excessive yellow resembling the reserved money-gold UI colour. Test at every key-1 hit and on the key-7 lead sword dive.

Judge: Measure whether removing the sparks makes the blow less exciting, then whether adding them back reduces silhouette readability. The correct result is greater impact without losing the three crescents.

### WP8 — Halo Seal, big blows only

Layer: 6.
Source: `ff-c3-c3` for the general idea of small moving highlights. Discard its geometry, crossfade and generic rings.

Workers: ChatGPT/Gemini paint two seal designs; Codex traces/cleans the approved contours and generates an SDF/MSDF; Claude evaluates play-size readability.

Why 7/6.5: The rings collapse into a bangle at 100 px. The visible `+` artifacts are an integration defect, while the absence of distinctive engraved motifs is an art-direction defect.

New art:

- One principal thin outer ring, incomplete in 2–4 deliberately designed locations.
- One partial secondary arc, not several concentric equivalent rings.
- A small number of crafted geometric seal marks occupying distinct quadrants.
- A few moving star points attached to the path.
- No continuous bright circular band.
- No extra rings on ordinary key-1 hits.

Runtime: Camera-aligned seal graphic represented as MSDF/SDF, using the signed-distance field for antialiasing and revealing pre-authored segments. Analytic geometry may be used for simple hairlines only, never to invent the engraved design.

The original `msdfgen` author explains that multi-channel distance fields can preserve sharp corners in real-time rendering and documents shader-based reconstruction. For a delicate seal, test both MSDF and high-resolution ordinary alpha; MSDF is not guaranteed to win at 1-pixel lines.  [GitHub]

| Setting | Proposed value |
| --- | --- |
| Source design | 2 authored seal candidates |
| Source resolution | 1024 × 1024 for master, 256–512 px runtime |
| Projected diameter | 90–140 px for a large blow |
| Ring stroke | ~1–1.5 px at play size |
| Reveal | 0.10–0.17 s |
| Full-presence hold | 0.10–0.17 s |
| Eroding exit | 0.30–0.50 s |
| Bright ring area | ≤3% of seal region |
| Backing alpha | 0.35–0.50, broken |

Source geometry should be circular when viewed face-on. If the seal is intended to lie on the ground, an elliptical screen projection is expected from the camera and should not be mistaken for a source-art defect.

Acceptance: Recognizable engraved signature at 100 px; not a bangle; no bars or sudden cross shapes; distinct from the reserved gold UI; present only at cast, lead dive, finisher or ultimate events.

### WP9 — Burst-in and slow-decay scheduler

Layers: 9 and 10.
Source: Existing `FlipbookPool` erosion and `slowFrom/slowRate` functions.
Worker/tool: Codex implements profiles; Claude measures temporal envelopes and judges.

The existing runtime already has useful erosion tools. The missing work is a common effect-phase model controlling the visuals consistently across each asset family.

```TypeScript
type EffectPhase =
  | "prestrike"
  | "contact"
  | "reveal"
  | "hold"
  | "erode"
  | "residue"
  | "finished";

type EffectProfile = {
  contactFlashTicks: number;
  revealTicks: number;
  holdTicks: number;
  erodeTicks: number;
  residueTicks: number;
  initialBrightnessRatio: number;
  erosionMode: "tips-first" | "islands" | "along-stroke";
  sourcePlaybackFps: number;
  looping: boolean;
};
```

How the scheduler works:

At impact tick zero, trigger a bright contact point and narrow hot slash immediately. This satisfies the first-frame requirement for the strike.

Simultaneously, a directional reveal mask exposes the already-authored three large crescents. The exposed area grows quickly, while the surviving pixels maintain their designed luminosity.

The shape holds briefly. During decay, use a separate persistence map so tips and detached flame tongues disappear first, followed by broken mid-stroke islands and finally the heavy roots.

Do not apply the same global alpha fade to every pixel.

Proposed timing profiles

| Family | Attack/reveal | Hold | Erosion/residue |
| --- | --- | --- | --- |
| Key-1 Fire impact | 0–67 ms | 80–130 ms | 350–650 ms |
| Tip flash | Immediate | 50–100 ms | 100–200 ms |
| Large glint | Immediate | 65–120 ms | 150–250 ms |
| Halo seal | 100–170 ms | 100–170 ms | 300–500 ms |
| Permanent sword mantle | Enter over 50–100 ms | Continuous presence | 150–300 ms on dismissal |
| Fire sheath | Enter over 50–100 ms | Continuous presence | 180–350 ms on dismissal |
| Gold dust | Spawn after blow | No static hold | 400–900 ms, sparse |

For key 1, note that the first and second hits will be only ~300 ms apart after the first hit moves to +18 ticks. Do not let each blow leave its entire bright crescent fan intact for 650 ms. At the second hit, the first should predominantly be broken ember residue.

Erosion algorithm

Use a painted or derived persistence field $P(x,y)$, where tips have lower persistence and roots higher persistence. During decay:

$$A(x,y,t)=A_0(x,y)\,
\operatorname{smoothstep}\left(e(t),e(t)+w,P(x,y)\right)$$

Here $e(t)$ increases during the decay interval and $w$ provides a narrow transition. For repeated colour bands after erosion, renormalize a surviving ramp using:

$$r=\operatorname{clamp}
\left(\frac{P-e}{\max(1-e,\epsilon)},0,1\right).$$

Keep the persistence field separate from the authored coverage and core masks. Otherwise a single noise threshold can destroy fine hot lines too early.

This is a proposed implementation for the game's existing erosion model. The artistic gate is that each remaining stroke fragment still has a dark base, coloured body and small hot accent until it disappears.

Accept: Decay is visually slower than attack by at least 3:1; no sudden global darkening; no identical dissolve pattern across all three strokes; no static frozen flame during an extended hold.

### WP10 — Final sword readability, gameplay and host acceptance

Workers: Codex applies runtime/gameplay changes; Claude validates and coordinates judges.

Integrate the already-approved changes without reopening their design:

- Key-1 first sword points at its target before flying; first contact is approximately +18 ticks rather than +6.
- Swords 2 and 3 depart 0.25–0.30 seconds before contact and slow near their targets, with the final 8–10 frames at ≤12 px/frame.
- Every lead sword meets T4: at least 12 frames ≥40 px long and moving ≤12 px/frame before contact.
- The jade ring uses the approved white-jade material and pale-gold rim, not reflective chrome-silver.
- Fire sword contrast is measured on the completed render, including mantle, blade fire, particles and trails.
- Use the existing FXAA or SMAA option at High, whichever performs and reads better in the real host. Three.js documents both implementations; SMAA pass ordering must respect its linear colour-space requirement.  [Three.js Docs +1]
- Update gameplay canon, content and golden hashes intentionally for the approved key-1 change.
- Keep skills instant-cast; no typing delay. Keep generated media outside Git.

Final judge: The full Metal and Fire experience, including key 1 and key 7, must reach ≥8.5 from each blind judge. A package's isolated score is diagnostic, never final acceptance.

## 4. New art and complete generation prompts

All prompts below are original production instructions. They are not quotations from the cited references.

For Firefly Video, use the Adobe Firefly Video model only, not any partner model. Disable automatic prompt enhancement for controlled comparisons, and record model, seed, settings and first/last-frame IDs. Adobe documents the option to select the Firefly model, keyframes and 24 fps generation.  [Firefly]

### Candidate allocation

| Item | New image candidates | New Firefly Video runs | Reuse |
| --- | --- | --- | --- |
| Metal mantle | 2 masks | 2 | `ff-m1-c4`, `ff-m1-c3` |
| Fire sheath | 2 masks | 2 | `ff-f1-c4`, `ff-f1-c2` |
| Key-1 impact | 2 first + 2 last | 4 | Ticket 252 v1/v3, `ff-a1-c5` |
| Tip stars and skill glints | 3 masks | 0 initially | `ff-g1-c2`; optional 1 video fallback |
| Sparks | 2 sprite sheets | 0 | Old sprays for rejection comparison |
| Gold dust | 1 sprite sheet | 0 | No old motion retained |
| Halo seal | 2 designs | 0 | `ff-c3-c3` as rejection comparison |
| Jade ring | 1 approved-image repaint | 0 | Existing approved character/sword art |

Initial total: 17 image candidates/edits and 8 new Firefly Video generations. Do not run every possible variant immediately: make two or four, evaluate them, and only expand when the measured defect is specific.

### A. Metal mantle — authored mask

Image prompt M-IMAGE, two candidates

> [Writing] Create one premium xianxia sword-qi mantle design mask for a real-time game. Pure black background, a single long horizontal composition, hilt on the left and point on the right. No actual sword. Two separated, asymmetrical flowing seams made of fine silver-white silk filaments, broken feather-like qi plates, delicate etched threads and a narrow needle beyond the tip. Keep a wide central black corridor for the real steel blade, an open collar around the hilt, many elegant negative-space gaps, and a thin trailing silk tail. Luxurious hand-painted anime/donghua linework, sharp tapered ends, grayscale only. No solid feather, fern, smoke, fog, text, border or glow blob.

Produce one candidate with more angular, tailored plates and one with softer streaming silk. The mantle direction remains A in both; these are sub-variants, not alternative concepts.

Firefly Video M-VIDEO — 2 runs

> [Writing] A single long, thin horizontal band of flowing silver-white sword qi on pure black. Fine silk filaments race smoothly toward the right while small broken feather-shaped energy fragments ripple and separate. Preserve broad empty gaps and delicate tapered ends. The outer silhouette stays narrow and stable; motion lives inside the strands. Elegant hand-painted anime energy, subtle silver-blue accents, crisp ink-like edges, continuous directional flow. Static camera, no sword, no scenery, no large solid feather, no smoky haze, no bursts, no text.

Processing: Extract motion from the most stable strip of each clip. Correct the left/right texture boundaries offline so UV repetition has no visible seam. Use the painted M-IMAGE mask as the stationary exterior envelope; Firefly controls only moving interior texture.

### B. Fire sheath — authored mask

Image prompt F-IMAGE — 2 candidates

> [Writing] Design one asymmetrical fire sheath mask for a straight flying sword, horizontal with hilt left and tip right, pure black background. No sword. Flames exist OUTSIDE a central empty blade corridor, never inside it. Long soft tongues stream backward toward the left, with a few small fast licks and a thin tapered needle past the right tip. Upper and lower flame shapes differ strongly; no mirrored symmetry. The hilt is almost empty, without a large fire blob. Use elegant hand-painted flame shapes, rich taper, sharp small accents and generous black negative space. No arrowhead, no fireball, no smoke veil, no text.

Generate two variations: one with long directional tongues, one with shorter layered tongues. Both retain the same protected blade corridor.

Firefly Video F-VIDEO — 2 runs

> [Writing] A narrow horizontal sheath of soft living orange-red fire on pure black, flowing from right to left around an invisible straight blade. Asymmetrical flame tongues lick backward in layered waves, with tiny fast flickers and a restrained pale-gold hot line near the forward tip. The middle remains visibly open and dark. Motion is continuous, delicate and directional; the overall silhouette stays narrow and pointed. Rich stylized anime fire, soft inner movement with crisp small flame tips. Static camera, no sword, no fireball, no hilt blob, no smoke, no text.

Processing: Keep organic motion from `ff-f1-c4` where it outperforms the new video. Remove the hilt-end blob using an authored mask. Preserve the soft turbulent transitions rather than flattening them into a stepped-fire simulation.

### C. Key-1 impact — designed first frames

Image prompt I-FIRST-V1 — main candidate

> [Writing] Premium xianxia Fire sword-impact artwork, one isolated effect on a pure solid black 1080×1080 square. Three DIFFERENT sweeping flame crescents rise diagonally up-right from a strike point in the lower-left region. Each open crescent spans 120–180 degrees with a thick energetic root tapering to an extremely fine needle tip, thickness ratio at least 3:1. Arrange the three strokes as an OPEN fan, never as a circle or letter C. Add four or five small counter-strokes and a few detached licks. Rich orange-red flame, thin white-gold hot line along each outer leading edge, dark broken ink underlay. Luxurious hand-painted anime/donghua fire, sharp crafted shape, soft living interiors. No background scene, no sword, no lotus, no smoke, no text.

Image prompt I-FIRST-V3 — alternate

> [Writing] Create one isolated Fire sword-cut impact on pure black, 1080×1080 square. Two long dramatic flame-brush crescents sweep diagonally up-right from a lower-left strike point, followed by a distinct shorter third counter-stroke. Together they form three readable OPEN strokes, not a closed circle. Roots are bold and expressive, tips narrow to sharp fine needles, with thickness taper at least 3:1. Add four or five small detached flame accents. Saturated orange-red body with a very thin white-gold leading edge, broken dark ink beneath, soft organic fire movement suggested inside the strokes. Premium elegant anime/donghua calligraphy, no lotus, no circular ring, no sword, no scenery, no text.

Important: These prompts are initial generation specifications, not automatic approval. Claude must measure arc openness, taper and hot-line percentage before the image is allowed into video generation.

### D. Key-1 impact — designed last frame

Image EDIT prompt I-LAST — use once per approved first frame

> [Writing] EDIT THE ATTACHED FIRST FRAME. Keep exactly the same black canvas, framing, stroke roots, directions, relative positions and overall three-crescent layout. Do not redesign or reposition the effect. Transform the flame strokes into their late ember state: the same shapes have burned down to thin, broken dark-red and orange ember lines with a few tiny pale-gold hot points. Bright remaining area should be only 15–35% of the original. At least 70% of the remaining bright pixels must lie within the original stroke silhouettes. Tips have broken into small fragments, roots remain identifiable. No new strokes, no smoke, no new stars, no fade-to-empty black frame.

Do not generate the last frame from an independent text-only prompt; using the approved first image as the edit input is essential to retaining its identity.

Firefly Video I-VIDEO — 4 runs

> [Writing] Animate the supplied first and last images of three open flame-brush crescents. Preserve each stroke's position, direction, taper and separate identity. Soft living orange-red fire flows along the curved strokes from heavy roots toward fine tips. Tiny detached licks curl and break away; the thin pale-gold leading edges shimmer. After the strong initial appearance, the strokes gently fragment into their matching ember remnants. Luxurious stylized anime fire on pure black. Static camera, no rotation of the whole composition, no new rings, no lotus, no extra strokes, no smoke, no text.

Use two seeds for each of I-FIRST-V1 and I-FIRST-V3. The designed last frame should also be retained as a separate runtime decay reference.

The final frame being at the end of a 5-second Firefly video does not mean the game should play a five-second impact. Extract the useful motion and enforce the game timing independently. If the requested end state never appears during the selected segment, use the authored end-state mask to guide runtime erosion rather than stretching the generated clip.

### E. Tip star and glint sheet

Image prompt G-IMAGE — 3 candidates

> [Writing] Premium hand-painted sword-tip glint sprite sheet on pure black. Show three separated variations of the SAME elegant four-point white-gold star: a compact main star with two long razor-tapered arms and two shorter arms, a slender diagonal glint, and a tiny secondary star. Each has a very small bright nucleus, delicate uneven tapers, a faint fine halo and subtle darker edging. Refined anime/donghua jewel-like sharpness, not a generic stock sparkle. Generous black separation between sprites. No round white blobs, no six-point star, no squares, no bokeh, no text, no sword, no background.

Candidate variations should change arm proportions and outer contour, not invent new symbols. The animation should preferably be produced in code from stable painted masks, with a brief curated glint sequence reused only if it improves the result.

### F. Starfire sparks and dust

Image prompt S-SPARK — 2 candidates

> [Writing] A premium game-VFX sprite sheet of isolated fire sparks on pure black. Arrange three distinct spark lengths with several separated variations. Every spark has a tiny extremely bright white-gold hot head, a fine tapered amber-orange body and an even thinner cooling dark-red tail. Elegant sharp hand-painted anime/donghua energy, directional, slightly curved, refined and varied in thickness. No round explosion, no fireworks, no repeated equal-length rods, no zigzag shapes, no glitter particles, no smoke, no scene, no text. Wide black padding around every sprite.

Image prompt S-DUST — 1 candidate

> [Writing] A sparse premium ember-dust sprite sheet on pure black. Many individually separated tiny irregular warm-gold and red-orange flecks, needle glimmers, micro-streaks and a few asymmetric four-point twinkles. Each is sharp, delicate and different. Keep the total bright area low with generous black gaps. Designed for a quiet magical aftermath at small gameplay size. No circles of light, no lens artifacts, no floating coins, no glitter clouds, no hexagons, no large stars, no scenery, no text.

Movement is created by Codex in the particle system, not Firefly Video.

### G. Halo Seal

Image prompt H-SEAL — 2 candidates

> [Writing] Create one distinctive xianxia sword-school halo-seal design as clean, fine white artwork on a pure black square. Perfect circular source geometry, one hair-thin incomplete outer ring and one sparse broken inner arc. Add a small number of elegant engraved seal marks, short geometric inscriptions and deliberate gaps; make every mark feel crafted and symbolic. Keep generous negative space, strong separation between ring segments and no heavy solid areas. High-precision linework for conversion to a signed distance field. No thick bangle, no multiple equivalent rings, no generic magic circle, no glow, no stars, no scenery, no text labels.

The two designs should differ in the engraved structure. One may favour a sword-seal motif; the other a refined cloud-and-flame seal. Both remain recognizably part of the same sword-school visual language.

### H. Approved jade-ring repaint

Image EDIT prompt J-RING — one final candidate

> [Writing] EDIT the supplied game sword image using the approved sword-design reference. Change ONLY the hollow ring at the guard from chrome-silver to smooth translucent white jade with a narrow, restrained pale-antique-gold outer rim. Preserve the ring's exact position, shape, internal opening, three green-jade details, cloud carving and all sword geometry. Do not change the steel blade, hilt, lotus pommel, lighting direction, framing or background. The jade must read as premium polished white stone, not glowing plastic or reflective chrome. Keep the original game's anime/donghua material style.

Use the project's approved image and original sword asset as the references. Do not substitute unrelated online weapon art.

## 5. Answers to the five open technical questions

### A. How to make loops seamless without crossfade ghosting

The important distinction is between a looping animation and a periodically scrolling texture. They should not use the same implementation.

For the Metal mantle and Fire sheath:

1. Keep the exterior silhouette stable in the authored envelope.
2. Extract a long, thin moving texture from the Firefly footage.
3. Make its left and right spatial boundaries periodic, matching both colour and approximate edge direction.
4. Scroll it using `fract(u + speed * time + phase)` on the mesh.
5. Add a small, non-periodic secondary deformation if needed, but do not let it change the protected blade corridor.

There is no video-frame seam because the flame motion comes from a periodic spatial texture. Three.js supports repeating texture coordinates directly.  [Three.js]

For an animation that genuinely needs full-frame looping, select a segment with similar starting and ending silhouettes and consistent motion. Check the terminal transition in both directions, use motion-compensated interpolation only if it demonstrably improves intermediate frames, and reject clips that still create double shapes.

Recommended `FlipbookPool` change: The default should no longer be crossfade plus wrap. Each asset explicitly declares `loopMode: "periodic" | "validated-frames" | "none"`.

Glints and impacts should use `"none"`.

### B. First-frame brightness ≥95% versus a burst-in

Use two separate visual events:

Contact-relative timing

Illustrative, not to scale−3 to −1 ticks

Pre-impact

Optional qi preparation0 ticks

Contact

Hot flash ≥95%+1 to +4 ticks

Reveal

Crescents expand+5 onward

Hold/decay

Tear and erodeThe contact flash already has its maximum local brightness at age zero. The flame crescents can still expand after contact.

If the owner insists the 95% rule applies to total effect brightness across the entire region, rather than the contact flash, shift the reveal into the pre-impact sword motion. At contact, the crescents must already be substantially visible.

Do not artificially label a dim, partially transparent image as a full-brightness first frame. Log both instantaneous peak luminance and total integrated luminance.

### C. Dark backing without a black sticker or extra layer

One pass is achievable by composing the authored backing, body and emissive core inside the fragment shader, then using premultiplied-style blending.

A proposed output is:

$$\mathbf C_\text{out} =
\mathbf C_\text{body}\alpha_\text{body}
+
(1-\alpha_\text{body})\mathbf C_\text{ink}\alpha_\text{ink}
+
\mathbf E_\text{core}$$

$$\alpha_\text{out} =
\alpha_\text{body}
+
(1-\alpha_\text{body})\alpha_\text{ink}$$

The framebuffer then composites it against the destination.

Important implementation detail: Use a custom packed data format, not a conventional PNG whose alpha channel is assumed to mean the final transparency of every RGB channel.

A suitable raw packed texture is:

| Channel | Data |
| --- | --- |
| R | Narrow hot-core mask |
| G | Authored dark-ink mask |
| B | Erosion persistence |
| A | Body coverage |

Use `DataTexture` or another byte-preserving upload path, `NoColorSpace`, and explicitly controlled premultiplication. A normal image-decoding path can alter transparent pixels and corrupt data stored in channels that are not ordinary colour. Validate round-trip channel values before integration. Three.js distinguishes non-colour textures from sRGB colour textures.  [Three.js Docs +1]

The ink must be:

- Broken rather than a continuous perimeter.
- Different in Metal and Fire.
- Narrower and less opaque near fine hot accents.
- Displaced slightly outward from the brightest edge where useful.
- Protected against crossing the blade and jade guard.

The present Fire soot alpha of 0.85 should be treated as a candidate for reduction, not automatically retained. Start at 0.45–0.70.

An additional warning: adding emission to the fragment RGB while retaining lower alpha is a hybrid emissive-compositing technique. It is not a conventional premultiplied opaque colour. Verify its behaviour through HDR targets, tone mapping and bloom rather than assuming that it will behave identically on every render path.  [MDN +2]

### D. Cards or blade-hugging meshes?

Blade-hugging meshes for both sheath and mantle. This decision should not be reopened.

The old Firefly card is useful as a source of animated texture, not as the final spatial representation of something attached to a 3D sword.

A mesh enables the effect to follow blade length, orientation, movement, LOD and the protected blade corridor. It also avoids paying to redraw a large transparent rectangle around every sword.

Use card flipbooks for the Key-1 impact and short one-shot visual events. Use sprites for glints and sparks. Use SDF/MSDF for the designed seal.

The engine support for custom mesh attributes, UV mapping and instancing is documented by three.js; the expected visual and performance improvements are project-specific hypotheses to verify in WP0/WP10.  [Three.js Docs +2]

### E. How to preserve the blade when the Metal mantle looks solid white

Use five safeguards in combination:

1. Art correction: Replace contiguous feather masses with open, separated qi fragments. The blade should be visible through the space between the two mantle seams.
2. Geometry correction: Put the mantle outside the blade, not on top of it. Preserve the one-pixel separation at final display resolution.
3. Shader correction: Exclude protected blade/guard pixels before calculating body, backing and emission.
4. Brightness correction: Reduce the white fill; concentrate brightness in a small number of narrow lines.
5. Testing correction: Judge the finished sword at 60, 100 and 130 px in flight—not the close-up mantle by itself.

If the effect passes blade-keep numerically but the sword still looks like a feather, the problem is its silhouette identity, not merely occlusion. Return to the authored mask, not to the blending code.

## 6. Risk register and verification

| Risk | How to detect it | Action if it fails |
| --- | --- | --- |
| Firefly changes the three crescent shapes | Frame-by-frame stroke identity and mask overlap | Keep authored shape; use Firefly motion only inside it |
| First/last frame causes an undesirable 5-second interpolation | Inspect temporal contact sheets; measure time to useful motion | Extract a useful segment; construct runtime decay independently |
| Solid-white Metal mantle | Area/coverage analysis at 60 px; blind identity judgment | Redesign negative spaces and plates |
| Fire arrowhead reappears at the hilt | Mask and silhouette inspection | Explicit hilt exclusion; correct source strip |
| Bright cream on light stone | Local OKLab and luminance maps | Reduce body brightness, improve ink shape and core separation |
| Dark backing becomes a sticker | Backing-only capture on both stones | Break continuity, reduce alpha, vary edge widths |
| Firefly loop ghosting | Seam ratio, optical-flow diagnostics, ten-loop capture | Replace with periodic UV motion or reject loop |
| White point bloats into a blob | Core area, centroid and radius tracking | Replace peak frames; reduce mask rather than only brightness |
| Sparks resemble fireworks | Particle angle histogram and trajectory recording | Spawn directional clumps, remove radial emission |
| Impact decays too quickly | Area-versus-time curve and persistence maps | Extend controlled erosion and retained ember remnants |
| Too many effects overlap at +18/+36 ticks | Full key-1 capture with all three hits | Reduce early residue coverage; maintain the long but sparse tail |
| Halo looks like a bangle | Actual 100 px capture | Remove secondary rings; simplify engraved detail |
| HDR bloom destroys delicate edges | HDR input and final output comparison | Reduce core area/intensity and adjust bloom threshold |
| Atlas causes dark fringes or adjacent-cell bleeding | Atlas border test across mip levels | Repair padding, colour extension and sampling bounds |
| More than two transparent layers over the blade | Per-pixel overdraw debug output | Merge backing/body; exclude extra ribbons near steel |
| Frame-time budget exceeded | Fixed-replay A/B deltas on key 7 | Reduce far LOD work, sampling cost and particle count |
| FXAA/SMAA softens fine art | A/B capture at 60 px | Choose the cleaner method or adjust line thickness |
| Approved jade becomes silver again | Guard-only and final sword captures | Fix source material and verify texture colour space |
| Project files accidentally include generated media | Repository diff and asset-path audit | Keep media in external asset storage; commit manifests/code only |

For texture and shader correctness, WebGL's published best practices are particularly relevant to checking render-target support rather than assuming all floating-point configurations work.  [MDN]

## 7. Acceptance ladder

Use the same procedure after every package, not just at the end.

1. Asset validityCorrect source model, legal project-owned inputs, correct mask geometry, no unwanted components, correct frame dimensions and alpha/data-channel handling.
2. Temporal and technical validityNo ghost seam, no frame pops, correct first-frame brightness, intended erosion progression, valid render-target compositing and protected blade regions.
3. Play-size readabilityReview at 60–160 px for ordinary effects, 400–500 px close-up, both grounds, real speed and 0.25×. Compare against the last accepted candidate with identical scene settings.
4. Performance validityThe new package stays within its allocated share of the Metal/Fire frame-time budgets. No hidden overdraw regression on 88 swords.
5. Owner and blind evaluationAt 7 or higher, send the demo to the owner. At 8.5 or higher from both judges, mark the built-play-host candidate accepted. Three attempts without a measurable gain trigger a method change.

Each package should produce a small evidence bundle: candidate ID, source settings, atlas metadata, mask measurements, screenshots, real-speed video, 0.25× video, performance delta, both scores and disposition (accept / revise / replace method).

This makes acceptance reproducible rather than reliant on an isolated attractive screenshot.

## 8. Remaining uncertainties

These are material uncertainties that should be resolved by implementation tests, not presented as established facts.

| Unknown | Recommended test |
| --- | --- |
| Whether Ticket 252 v1 or v3 has the better visual rhythm | Compare actual source images at 70/100/160 px; only descriptions were supplied here |
| How much of the old Firefly flame can be salvaged as a seamless strip | Extract candidate strips, measure spatial periodicity and run ten-loop captures |
| Whether 512 px impact atlas cells justify their memory cost | Compare 384 vs 512 at both cameras, including sampling and frame-time deltas |
| Whether one-layer ink/emission preserves enough colour nuance | Compare against an explicit two-pass reference on both stones |
| Exact backing alphas that look premium rather than dirty | Blind A/B alpha sweep using the same design |
| Whether FXAA or SMAA best preserves these 1 px effects | Compare both with exact viewport/DPR and frame-time budget |
| Whether an MSDF improves the Halo Seal at 100 px | Compare MSDF, high-resolution alpha and possibly single-channel SDF |
| Whether Firefly first/last guidance retains hand-painted shape topology | Evaluate the four specified impact generations before further spending |
| True incremental GPU workload on the Mac mini M4 | No timer-query data in the supplied environment; use A/B frame-time proxies |
| The final owner-approved colour and softness balance | Cannot be inferred reliably from numeric metrics or overnight scores alone |

There is also an art-approval limitation: I have evaluated the descriptions, score reports and code facts in the brief, but not the original source clips, Ticket 252 frames or a running play build. Therefore I cannot truthfully claim that any candidate already passes the new measurements, or that the proposed settings will necessarily score 8.5.

## 9. Final production recommendation

The critical path is:

WP0–2: Establish the technical foundation

Measurement · premultiplied backing · validated loops and atlasesWP3: Impact

Ticket 252 v1/v3 → Firefly → mask → erosionWP4–5: Sword aura

Wind-Silk + Fire sheath → scrolling meshesWP6–9: Impact polish and timing

Glints · sparks · seal · burst-in · slow erosionWP10: Integrated play-host acceptance

Both judges ≥8.5 · blade-keep · performance · light/dark stoneDo not spend another generation cycle making `ff-m1-c4` brighter, `ff-f1-c4` larger, or `ff-a1-c5` more elaborate in its existing shape. Those interventions are unlikely to address the actual design defects.

Spend the next Firefly runs on motion constrained by the selected artwork; invest Codex time in accurate geometry, blending and temporal control; and spend Claude's judging time on the final visual at its true size.

The 8.5 target is more likely to be reached through controlled integration than through a single stronger generated clip. That is the central production decision.

### Verified technical references

The core recommendations are supported by these primary sources:

- [Adobe Firefly — Generate videos using images](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html)
- [Adobe Firefly — Generate videos with transparent backgrounds](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html)
- [three.js — InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html)
- [three.js — Texture and wrapping](https://threejs.org/docs/pages/Texture.html)
- [three.js — Colour Management](https://threejs.org/manual/pages/color-management.html)
- [MDN — WebGL best practices](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices)
- [Viktor Chlumský — MSDF generator and implementation](https://github.com/Chlumsky/msdfgen)
- [FFmpeg — Frame interpolation filters](https://ffmpeg.org/ffmpeg-filters.html)
- [Björn Ottosson — Original OKLab specification](https://bottosson.github.io/posts/oklab/)

These sources establish technical capabilities and algorithms; they do not certify the proposed artistic thresholds or guarantee a blind-judge score. Those remain game-specific decisions validated through the prescribed testing process.


---

**[TURN · Lượt chạy 1 · Lời yêu cầu tự rà soát (Claude gửi; dùng nguyên văn cho mọi lượt rà soát của cả hai lượt chạy)]**

````text
Review your latest full answer above against the brief, the facts and the constraints. Check: wrong facts or sources, steps that would not work, missing steps, contradictions with the constraints or the owner's decisions, vague parts that a worker could not execute.
Answer in exactly this form:
VERDICT: PASS or FAIL
If FAIL: list each problem, then give the corrected FULL analysis and solution (not a diff).
PASS only if nothing at all needs to change.
````


---

**[TURN · Lượt chạy 1 · Rà soát 1 của ChatGPT: FAIL (nguyên văn, 84.903 ký tự)]**

VERDICT: FAIL

The previous answer has the correct overall art direction, but it is not yet safe to hand to Codex and Claude as an executable production specification. It contains technical gaps, one mathematical contradiction with an owner-approved gate, incorrectly defined asset-processing steps, and several incomplete acceptance criteria.

## Problems found

### P01 — Firefly's first/last-frame workflow was not reconciled with the runtime duration

Adobe Firefly generates 5-second video by default at 24 fps and uses first/last images to guide the beginning and end. My instruction to extract 20–24 frames from that video did not explain how to preserve a designed last frame located approximately five seconds after the first.

Simply taking the first second may discard the ending. Compressing all five seconds into one second can make organic fire move unnaturally fast.

Correction: Separate the generated flame-motion interval from the authored decay. Use the first/last frames to constrain generation, evaluate the full 120-frame result, then construct the shorter gameplay envelope using selected motion plus controlled erosion.  [Firefly]

### P02 — The transparent-background rules were incomplete

Adobe's current documentation explicitly says that when transparent-background generation is selected, first and last frames must be PNG files containing transparency. It also says transparent downloads contain separate foreground and alpha videos.

My earlier answer did not distinguish that workflow from the project's successful opaque-black 1080 × 1080 workflow. It could cause a worker to upload an opaque black image while using the transparent mode.  [Firefly]

Correction: Use opaque black square images with transparent mode disabled for the proven impact workflow. Treat the 540p transparent workflow as a separate option requiring true RGBA input and explicit alpha-video reconstruction.

### P03 — Black-background footage was treated as if it contained reliable alpha

Black-background RGB does not uniquely determine the original foreground colour and opacity. A soft orange pixel could represent a dim opaque flame or a bright transparent one.

Automatic black removal can therefore produce dark fringes, clipped tongues and incorrect glow.

Correction: Extract approximate coverage from Firefly footage, constrain it with the authored masks, reconstruct alpha intentionally, and inspect the composite on both backgrounds. Never describe this as recovery of ground-truth alpha.

### P04 — The proposed scrolling texture was not enough to preserve living fire

A repeating spatial texture scrolling across a mesh solves an important seam problem, but it can look like repeating wallpaper.

My answer did not specify how soft turbulent movement would survive once a Firefly video became a texture strip.

Correction: Use a static authored exterior envelope with animated interior motion, preferably two decorrelated texture samples in the same shader. Measure both spatial repetition and temporal variation. Use validated cyclic animation only where scrolling cannot reproduce the desired motion.

### P05 — The packed-channel specification was incomplete

The proposed RGBA layout allocated all four channels to masks but failed to explain how Firefly's moving interior brightness and shapes would survive.

It also did not specify whether those channels represented one static image or an animated frame atlas.

Correction: Define separate authored-mask and animated-motion data, explicit channel meanings, colour-space settings, texture-upload rules, LUT sampling and atlas metadata.

### P06 — The shader example was not implementation-ready

The previous blending equations were conceptually useful, but the example omitted several essential conditions: actual three.js blend configuration, premultiplication rules, render-target behaviour, output colour conversion, depth and render ordering.

It also treated HDR emission too casually. Float colour-buffer renderability and floating-point blending are distinct capability checks.  [Three.js Docs +2]

Correction: Specify the exact compositing contract, shader inputs, render order and fallback if the required HDR path is unavailable.

### P07 — The proposed one-pixel blade gap could disappear after projection and antialiasing

A one-pixel gap in an authored image is not guaranteed to remain one pixel after rotating a 3D sword, scaling an instance, applying texture filtering and postprocessing.

My answer did not explain how the approved gap would be enforced in the final screen image.

Correction: Measure the actual projected silhouette, use conservative blade-local geometry and exclusion, and verify gaps through the final antialiased output.

### P08 — The two-transparent-layer cap was not enforced across the complete effect

I counted backing and luminous material inside one shader but did not provide a reliable way to account for overlapping mantle strips, flame ribbons, blade trails, glints and other transparent effects.

Correction: Count actual transparent fragment contributions inside each sword's screen-space region. Make mantle/backing/core one contribution where possible, and keep secondary layers outside the blade footprint.

### P09 — The 95%-first-frame rule was partially redefined

My answer correctly recognized the contradiction between an empty first frame and a completed bright burst, but then treated contact-flash brightness as the replacement for the stated requirement without making the acceptance distinction sufficiently explicit.

Correction: Define separate measurements for the immediate contact flash, the body reveal and total effect brightness. If the owner's original 95% requirement applies to the entire effect, place the body reveal before contact or require approval to change the criterion.

### P10 — The key-1 impact timing and overlap were under-specified

The previous answer suggested a long decay without fully separating the next hit at +36 ticks from the first hit moved to approximately +18 ticks.

Those hits are only 18 ticks, or 300 ms, apart. A lingering bright first impact could obscure the second.

Correction: Control decay by bright-body coverage, not just total lifetime. Allow sparse ember remnants to survive while removing most bright crescent coverage before the next impact.

### P11 — The Weber-contrast requirement is mathematically incompatible with a dark blade on light stone

I identified this contradiction but did not finish resolving its engineering and acceptance consequences.

For a dark blade against brighter stone, the conventional signed Weber contrast is negative and cannot reach +2. Nor can its absolute magnitude reach 2 when the blade luminance is nonnegative.

Correction: Preserve the owner's contrast objective while marking the precise C1 calculation as blocked pending a formally approved definition. Use separate dark-on-light and hot-edge-on-dark contrast measurements, while retaining ΔE OKLab ≥0.25.

### P12 — Source citations did not adequately separate facts from proposals

Several citations in the original answer were attached to broad technical or quality claims that the cited page could not establish. For example, documentation supporting instanced geometry does not establish that a particular aura mesh will achieve the target performance or visual score.

Some numerical thresholds were introduced without a sufficiently explicit distinction between owner-approved requirements and proposed tuning targets.

Correction: Cite documentation only for its actual claims. Mark project observations, mathematical deductions and proposed engineering thresholds separately.

### P13 — The spark implementation was not specific enough

I described GPU-instanced ballistic particles but did not say whether movement ran in a vertex shader or on the CPU. I also used screen-pixel gravity values without defining their relationship to the 3D ground plane and camera.

Correction: Use a deterministic world-space trajectory projected by the game camera, with per-instance launch data and an explicit bounce model.

### P14 — The atlas proposals lacked a memory, filtering and LOD decision

A 3072 × 2048 RGBA8 atlas consumes approximately 24 MiB before mipmaps. It is a substantial resource for one effect, especially if multiple independent data atlases are created.

The earlier answer did not budget total memory or guarantee safe sampling of adjacent cells.

Correction: Prototype smaller atlases first; specify per-frame padding, LOD sampling and mip behaviour. Promote to 512 px cells only if the close-up judge justifies the cost.

### P15 — The performance claims were too imprecise

Without GPU timer queries, the measured frame-time delta is not isolated GPU execution time. Vsync, CPU work, shader compilation, asset uploads and scheduling can affect it.

Correction: Report measured frame-time overhead, use matched A/B runs and warm-up, and distinguish it from true GPU timing. Define the window used for the 11.5 ms ceiling.

### P16 — Several owner-approved gameplay and art requirements were not fully integrated

The answer needed stronger coverage of the sword's first target-pointing hold, all three launch schedules, the T4 exposure gate, the final-scene Fire blade contrast, distributed micro-sparkles, and the precise LOD behaviour of the 88 swords.

It also failed to explicitly disable the rejected lotus, procedural scorch and code-drawn crack effects rather than merely replacing the foreground impact.

Correction: Include a final integration matrix tied to the approved gameplay changes and an explicit removal list.

### P17 — Some art prompts could produce invalid or hard-to-process assets

The image-generation prompts did not consistently require fixed safe margins, stable stroke topology, registered mask boundaries or exact sprite layouts. The previous Firefly prompts also lacked an explicit preflight character-count check.

The halo prompt said to add inscriptions but also prohibited text, leaving an unnecessary ambiguity.

Correction: Supply consistent layout constraints, a defined conversion pipeline and complete prompts of fewer than 600 characters for each Firefly Video request.

### P18 — The candidate plan and stop rules were not fully operational

The previous plan listed candidate counts but did not specify an unambiguous selection gate between image review, video generation and runtime integration. Nor did it define exactly what constitutes an unsuccessful attempt.

Correction: Use staged candidate generation, measurable defect logs, explicit acceptance per package and a method-change trigger after three attempts without improvement.

### P19 — The final 8.5 gate needed stronger controls

Blind judging was mentioned, but the protocol lacked enough detail about score independence, randomized presentation, fixed seeds, capture order, regression checks and the difference between an isolated visual pass and a full-host acceptance pass.

Correction: Make the two-judge acceptance procedure repeatable and require the integrated skill to pass all owner gates on the normal play host.

### P20 — The strongest existing assets were not prioritized precisely enough

The last plan correctly preserved `ff-f1-c4` and Ticket 252 v1/v3, but risked replacing useful organic fire unnecessarily. It also did not clearly distinguish reusable shape assets, reusable motion, rejected output and negative references for every candidate.

Correction: Salvage approved-quality components first; replace only the failed design dimensions. Do not spend new Firefly generations on glints, spark trajectories or seals unless the authored approach demonstrably fails.

# Corrected full analysis and solution

The following is the replacement production specification. It preserves all fixed owner decisions and treats new numeric recommendations as trial settings unless expressly identified as requirements.

## 1. Fixed production contract

The owner-approved art direction is immutable for this work.

| Area | Fixed decision |
| --- | --- |
| Sword aura | A — Wind-Silk Mantle: tailored external qi plates, two seams, 1 px ink gap, open jade-ring collar, needle tip and silk tail |
| Additional aura | Only the approved C-derived tip star; no other competing aura direction |
| Fire blade | Dark steel with hot edges; external flames must not repaint steel |
| Sword guard | White jade ring with pale-gold rim, matching the approved image |
| Key-1 Fire body | Three Brushfire Calligraphy crescents, 4–5 counter-strokes, detached licks, sharp edge, dark underlay and ≤5% white core |
| Sparks | Starfire Jewel: white-gold heads, red-cooling tails, three lengths, gravity, 2–3 directional clumps, occasional single bounce |
| Major-hit glints | One large four-point star and two smaller sequential glints |
| Halo | Engraved Halo Seal, restricted to big blows |
| Timing | Fast attack, readable hold, slow erosion; never a quick global fade |
| Existing rejected effects | No lotus, code-drawn cracks/scorch, analytic four-point star or rejected stepped-fire Mantaflow |
| Performance | Metal ≤+0.60 ms p95 on key 7; Fire incremental over Metal ≤+0.85 ms p95; 11.5 ms frame-time ceiling |
| Compositing | ≤2 transparent contributions per pixel within sword regions |
| Acceptance | Both independent blind judges ≥8.5 in the normal play host |

These are requirements, not optimization suggestions.

Roles remain fixed: ChatGPT/Gemini produce edited or authored images after approval of their design; Firefly Video supplies organic motion; Codex CLI implements code, logic and sound; Claude operates the browser, prepares assets, measures results and manages blind judging.

The lab remains instant-cast, and generated media remains outside Git.

## 2. Full diagnosis of all ten layers

| Layer | Why the current candidate stops at 6.5–7 | Required change |
| --- | --- | --- |
| 1. Metal mantle `ff-m1-c4` | Solid white feather plates conceal the sword; static silhouette; little sparkle; poor light-stone contrast | Separate tailored qi plates, broader negative space, two animated seams, exposed steel, thin moving veins, distributed micro-glints |
| 2. Fire sheath `ff-f1-c4` | Organic flame is attractive but symmetrical; hilt blob reads as arrowhead; no trailing airflow; pale smear; loop ghosts | Asymmetric, backward-sweeping tongues constrained to a blade-hugging envelope; preserve Firefly motion; thin hot edge, broken soot backing |
| 3. Tip star `ff-g1-c2` | Eight arms collapse at 12 px; white core grows to a blob; frame jitter; overlong flash | New stable four-point painted mask, tiny nucleus, size-dependent arm detail, 0.12–0.22 s bright event |
| 4. Key-1 impact `ff-a1-c5` | ~300° ring-like arc, weak taper, no core, sticker edges, full shape at first frame, 0.25 s disappearance | Ticket 252 open fan, ≥3:1 taper, authored first/last, hot leading edges, rapid directional reveal, stroke-specific erosion |
| 5. Sparks `ff-b2-c1/c2`, `ff-b3-c3` | Radial fireworks, grinder sparks and bokeh-like gold dust | Painted sprite hierarchy driven by directional world-space particles and deliberate cooling |
| 6. Halo `ff-c3-c3` | Generic luminous bangle, '+' ghosts, weak engraved identity, ring-merging at 100 px | Authored sparse seal, high-quality alpha or SDF/MSDF, segment reveals and sequential glints |
| 7. Backing existing shader terms | Light stone erases pale effects; strong soot can become a dirty sticker | One-fragment dark body/bright core composition with designed discontinuous ink |
| 8. Loops existing crossfade | Crossfade blends different shapes into doubled objects | Source-level periodicity or a verified cyclic segment; no automatic eight-frame crossfade |
| 9. Burst-in complete `ff-a1-c5` f0 | The body seems to appear fully formed rather than emerging from the strike | Immediate hot contact plus a fast spatial reveal, or pre-contact body reveal |
| 10. Slow decay rapid disappearance | Flame dies faster than the strike develops; no luxurious aftermath | Brief hold, persistence-controlled tip/root erosion, separated sparse ember tail |

The current candidates reveal three different failure classes.

Art-design failures require new image masks: solid feather mantle, circular impact, generic rings, poor star shape.

Motion failures require controlled animation and placement: fire flowing against flight, loop ghosting, static qi, incorrect particle paths.

Compositing/timing failures require runtime changes: cream washout, ink backing, hot-core control, instant contact and slow decay.

Applying only the third category to a rejected shape will not make that shape acceptable. Conversely, a superior painted image cannot solve a broken loop or poor blade preservation.

The score expectation is therefore a hypothesis: the integrated solution has a credible route toward 8.5, but no score improvement is guaranteed until both judges test it.

# 3. Ordered work packages

## WP0 — Freeze the baseline and build the measurement harness

Workers: Codex, Claude · Must complete before runtime integration · Artwork research may run in parallel

### Tools

Existing `tools/vfx-flipbook`, NumPy, SciPy, Pillow, FFmpeg, the performance A/B harness and the game's deterministic playback system.

### Execution

1. Record the exact Git commit, three.js version, renderer configuration, display resolution, DPR, bloom settings, tone mapping, antialiasing mode and LOD settings.
2. Save a normal-player-settings baseline for key 1 and key 7, without URL flags.
3. Create deterministic action replays with fixed random seeds.
4. Save screenshots and video of the existing effects, including `ff-f1-c4`, `ff-m1-c4`, `ff-g1-c2`, `ff-a1-c5` and `ff-c3-c3`.
5. Add diagnostic toggles only to the development harness, not the owner's acceptance build.
6. Capture scene-only, sword-only, ink-only, body-only, core-only, particle-only and final-composited images.
7. Establish the actual output colour pipeline and float-render-target capabilities before modifying blending.

### Required test matrix

Primary capture combinations

| Dimension | Values |
| --- | --- |
| Ground | Light `#d6d0c2`; dark `#2a2c30` |
| Sword length | 60, 100, 130 px; close-up 400–500 px |
| Impact size | 70, 110, 160 px |
| Speed | 1× and 0.25× review |
| Actions | Key-1 three hits; key-7 88-sword sequence; one major blow with seal |
| Render | Aura off, each effect separately, final composite |
| Camera | Actual play camera and available close-up camera |
| Display | Reference 1280 × 720 plus owner's actual settings |

### Measurement definitions

Blade-keep

For protected sword pixel $p$:

$$d_p=\lVert OKLab(C_{\rm final}(p))-OKLab(C_{\rm auraOff}(p))\rVert_2$$

A pixel is preserved when $d_p\leq0.04$.

Required preserved proportions:

- Lead/mid blade: ≥90%.
- Far sword: ≥85%.
- Jade ring and guard: ≥95% on every frame.

The blade and guard masks must come from the sword's projected geometry, not a rectangle around the sprite. The comparison uses matched frames and postprocessing settings.

Oklab is a defined perceptual colour representation; its conversion and formulation are published by its author.  [bottosson.github.io]

Visual contrast

Measure final-output Oklab distance using local background samples. Preserve the existing owner target of ΔE OKLab ≥0.25 for the Fire blade. For other effects, proposed initial targets are ≥0.12 for primary silhouettes and ≥0.18 for important highlights on both stones.

These are screening values, not universally validated perception thresholds.

White-out

Use display-referred output converted to linear RGB, then calculate relative luminance consistently. Count pixels with $Y\geq0.95$.

Preserve the owner's ≤6% threshold over the defined visible play field. Additionally report the effect's own ROI, because field-wide coverage alone can hide an oversized white core in a small effect.

For Fire calligraphy, separately enforce ≤5% hot-core coverage of the principal effect shape.

Performance

For matched sequences, measure:

$$\Delta T_{p95}=p95(T_{\rm enabled})-p95(T_{\rm disabled})$$

Use several warm, interleaved A/B/B/A runs with the same seeds and conditions. Record CPU-side rendering time, total frame time, number of draw calls, texture uploads and memory separately where possible.

A suggested measurement protocol is five 20-second runs per configuration, with shader compilation and asset loading completed before recording. The exact sample duration is a proposed testing procedure.

For the 11.5 ms limit, report both the whole-capture p95 and every rolling one-second p95 window. Treat an interval above 11.5 ms as a failed window pending the precise existing harness definition.

Do not label these deltas “GPU time.” GPU timer-query support is extension-dependent, and the supplied Mac mini M4 environment does not expose that measurement.  [Khronos Registry]

### Deliverable and gate

A baseline report containing effect metrics, fixed captures, reproducible seeds, the actual render configuration, current scores, and a list of technical defects.

WP1 and WP2 cannot pass until the baseline is reproducible.

## WP1 — Rendering foundation: dark ink, luminous body and HDR core

Layers: 7, shared by all effects · Worker: Codex · Measurement: Claude

### Source

Reuse the existing Metal indigo and Fire soot art-direction values. Do not reuse their current alpha strength blindly.

### Exact runtime approach

One fragment of a `ShaderMaterial` should combine:

- The dark ink backing.
- The translucent body.
- The narrow emissive hot core.

Use a custom blend configuration with RGB source factor `ONE` and destination factor `ONE_MINUS_SRC_ALPHA`. Three.js documents these configurable material blend factors.  [Three.js Docs]

The conceptual compositing contract is:

$$a_b=\text{body coverage}\times\text{body opacity}\times\text{survival}$$

$$a_i=\text{ink coverage}\times\text{ink opacity}\times\text{survival}$$

$$a=a_b+(1-a_b)a_i$$

$$RGB_{\rm src}
=a_b C_b+(1-a_b)a_i C_i+E_{\rm core}$$

Then:

$$RGB_{\rm final}=RGB_{\rm src}+(1-a)RGB_{\rm background}$$

All colour terms are linear RGB. `E_core` is an independently controlled emissive contribution, not an ordinary alpha-multiplied surface colour.

### Codex implementation

```TypeScript
const material = new THREE.ShaderMaterial({
  transparent: true,
  depthTest: true,
  depthWrite: false,
  blending: THREE.CustomBlending,
  blendEquation: THREE.AddEquation,
  blendSrc: THREE.OneFactor,
  blendDst: THREE.OneMinusSrcAlphaFactor,
  blendEquationAlpha: THREE.AddEquation,
  blendSrcAlpha: THREE.OneFactor,
  blendDstAlpha: THREE.OneMinusSrcAlphaFactor,
  premultipliedAlpha: false,
  side: THREE.FrontSide,
  uniforms,
  vertexShader,
  fragmentShader
});
```

`premultipliedAlpha: false` here means the input texture is not automatically premultiplied. The shader constructs its final RGB/alpha contribution explicitly. Codex must verify how the installed three.js version passes material options to WebGL and compare the output against a two-pass reference.

The exact material configuration above is a proposed implementation that requires validation; the documented basis is `ShaderMaterial` and `Material` custom blending.  [Three.js Docs +1]

### Data and shader contract

Use two inputs for the sheath/mantle family.

Texture A — Authored static RGBA mask

| Channel | Meaning |
| --- | --- |
| R | Main body coverage |
| G | Broken ink coverage |
| B | Hot-core coverage |
| A | Erosion persistence |

Texture B — Animated motion data

Contains motion-derived brightness and turbulence from Firefly, encoded as data channels or a selected animated atlas.

The shader samples Texture A to establish the silhouette and Texture B to modulate interior light and detail.

This preserves the authored exterior while retaining organic movement.

For impact cards, the authored design mask may be static while the Firefly-derived motion atlas changes per frame. A different packed layout is permitted only if the manifest explicitly declares it.

All masks use `NoColorSpace`, no automatic alpha premultiplication, and controlled byte values. Three.js documents both non-colour texture annotations and `DataTexture` construction from raw buffers.  [Three.js +2]

### Starting parameters

| Parameter | Metal | Fire |
| --- | --- | --- |
| Dark backing alpha | 0.35–0.50 | 0.45–0.70 |
| Main-body alpha | 0.10–0.35 | 0.25–0.55 |
| Main-body output ceiling | 0.85–0.90/channel | 0.85–0.90/channel |
| Hot-core area | 1–3% | ≤5% |
| Ink discontinuities | 15–30% | 20–35% |
| Core width at play camera | 1–1.5 px | 1–2 px |
| Body mask discard threshold | 2/255 initially | 2/255 initially |

Ink discontinuities mean intentionally missing segments along the designed backing path, not randomly removing the same proportion of important silhouette pixels.

The alpha ranges and thresholds are engineering starting points. Claude must adjust them against final-scene measurements.

### HDR verification

Codex must inspect the real renderer and test:

1. Whether the intermediate render target is `RGBA16F` or another compatible HDR format.
2. Whether `EXT_color_buffer_float` is available.
3. Whether emission survives blending, tone mapping and bloom.
4. Whether the actual target format supports the intended blending.
5. Whether a 1–2 px hot core remains narrow after postprocessing.

`EXT_color_buffer_float` permits defined float formats to be used as render targets. `EXT_float_blend` covers additional float blending capabilities, particularly 32-bit float attachments. Check the actual attachment format rather than assuming either extension alone guarantees the entire HDR path.  [Khronos Registry +1]

A practical fallback is an LDR-compatible core plus restrained bloom, but it is a fallback with potentially different visual quality and must be judged again.

Use the correct processing order: scene/HDR effects, bloom, tone mapping/output conversion, and FXAA when selected. SMAA's documented current three.js implementation runs in linear-sRGB before `OutputPass`; FXAA requiring sRGB input runs after it.  [Three.js Docs +2]

### Acceptance

The existing Firefly fire should become readable on light stone without a continuous black border, while retaining its soft movement on dark stone.

Compare both backgrounds, with and without bloom. Require one transparent contribution for the authored ink/body/core composition, and no unexpected render-order or depth artifacts.

## WP2 — Source processing, atlas metadata and loop engine

Layer: 8 · Workers: Codex and Claude · Runs parallel with WP1

### Source inputs

`ff-f1-c4`, `ff-m1-c4`, `ff-c3-c3` and the existing `FlipbookPool`.

### Four playback modes

| Mode | Behaviour | Used for |
| --- | --- | --- |
| `scroll-periodic` | Periodic spatial texture flow | Metal mantle, Fire sheath, silk tail |
| `cyclic-frames` | Validated first/last cyclic sequence | Only genuinely repeatable detail |
| `oneshot-frames` | One pass through selected source frames | Impact flame, occasional irregular glint |
| `hold-erode` | Frozen or slowly changing frame with spatial erosion | Late ember remnants, end states |

Remove automatic eight-frame wrapping crossfade from the production defaults.

### Spatially periodic texture workflow

For attached sword effects:

1. Choose a Firefly source region containing useful fine movement but little global silhouette drift.
2. Register its direction to blade-local UVs.
3. Extract grayscale or multichannel motion information.
4. Create two overlapping texture strips with different internal phase or features.
5. Make the horizontal boundaries tile seamlessly in value and preferably first derivative.
6. Sample both strips inside one shader and combine their modulation nonlinearly.
7. Use separate rates and phases per sword to prevent all 88 swords from repeating identically.
8. Retain the authored mask as the final silhouette limit.

Proposed runtime:

- Strip A: 512 × 128 or 1024 × 128.
- Strip B: 512 × 128, only if it materially improves movement.
- Flow A: 0.8–1.3 repeats/s.
- Flow B: 0.35–0.65 repeats/s.
- Interior detail modulation: roughly ±15–25% of local intensity.
- Envelope breathing: ≤5% width modulation.
- Keep the main shape and protected blade corridor stable.

This is a production hypothesis, not a promise that any scrolling texture will look like Firefly's original animation.

### Temporal cyclic workflow

If a complete animated cycle is necessary:

1. Find a source segment with similar first and last appearances.
2. Evaluate shape correspondence and direction of motion.
3. Measure last-to-first difference against ordinary frame-to-frame differences.
4. Reject unmatched silhouettes.
5. Use offline optical-flow interpolation only for gaps where it improves shape correspondence.
6. Disable the old eight-frame blend.

A useful diagnostic is:

$$R_{\rm seam}
=\frac{D(F_{N-1},F_0)}
{\operatorname{median}D(F_i,F_{i+1})}$$

Initial proposal: $R_{\rm seam}\leq1.2$, excluding near-static sequences where the denominator is too small. Require no visible doubled contours, bars, freezing or motion reversal.

FFmpeg documents `minterpolate` with motion-compensated interpolation as distinct from frame blending. Your measured 26% improvement is project evidence, not a universal expected improvement.  [FFmpeg]

### Atlas policy

Start with smaller assets:

| Cell size | 24-frame 6×4 atlas | Approx. RGBA8 storage |
| --- | --- | --- |
| 256 × 256 | 1536 × 1024 | 6 MiB |
| 384 × 384 | 2304 × 1536 | 13.5 MiB |
| 512 × 512 | 3072 × 2048 | 24 MiB |

With a complete mip chain, approximate storage rises by one-third. These calculations exclude other textures and duplicate buffers.

Use 256 px cells for initial play-size testing. Promote impacts to 384 px if the close-up warrants it, and to 512 only if both visual improvement and memory budget justify it.

Give cells 4–8 px safe borders, with the edge pixels extended appropriately. Never let UV interpolation sample an adjacent frame.

For code and manifest, implement fields equivalent to:

```JSON
{
  "id": "impact-fire-brush-v1",
  "sourceFps": 24,
  "frameCount": 16,
  "columns": 4,
  "rows": 4,
  "cellPx": 384,
  "paddingPx": 8,
  "loopMode": "oneshot-frames",
  "channelLayout": "body-ink-core-persistence",
  "colorSpace": "none",
  "sourceAlpha": "derived",
  "sourcePremultiplied": false,
  "variants": [
    {"name": "primary", "firstFrame": 0, "count": 16}
  ]
}
```

This requires an actual manifest and decoder update. The current implementation does not already support rows and variants.

Do not reduce playback from source 24 fps to 12 fps simply to lengthen the effect. A clip can be sampled at 12 fps while preserving real-time motion if alternate source frames are discarded appropriately, but slowing the original animation requires interpolation.

### Acceptance

All looping assets pass ten continuous cycles in the built host. One-shot effects never visibly wrap back to their initial frame.

## WP3 — Key-1 Fire impact body

Layer: 4, with layers 9–10 · Main art priority

Starting material: Ticket 252 v1 and v3. Keep `ff-a1-c5` as the organic-flame motion reference, not the final shape.

Workers: ChatGPT/Gemini for designed images; Firefly Video for organic motion; Claude for extraction and measurement; Codex for integration.

### Shape requirement

- Exactly three dominant readable crescents.
- Each open arc approximately 120–180°.
- No 300° ring or nearly closed letter C.
- At least 3:1 thickness taper between centreline positions 20% and 80%.
- Four or five short secondary strokes.
- A few separated flame tongues.
- Orange-red primary body.
- Thin white-gold hot line following the leading edges.
- Hot-core coverage ≤5%.
- Broken dark-ink backing.
- Erasure from tips and detached fragments toward heavier roots.

### Production sequence

Stage A — Design validation

Claude measures Ticket 252 v1 and v3 at 70, 110 and 160 px. Select at most two first-frame designs that pass openness, taper and distinct-three-stroke checks.

If the existing images are 1536 × 1024, recompose them into the approved 1080 × 1080 black square without stretching the original strokes. Preserve the impact origin and add safe margins.

Stage B — Last-frame design

Use the chosen first image as the direct EDIT input. Create matching late-ember remnants.

Require:

- Last bright area 15–35% of first-frame bright area.
- At least 70% of the remaining bright pixels inside the original stroke masks.
- Consistent roots and directions.
- No newly invented circles or separate strokes.
- No smoke or global fade.

Stage C — Video generation

Use Adobe Firefly Video, opaque black input, 1:1 1080p, transparent mode off, 24 fps, 5 seconds, supplied first and last frames.

Produce two attempts for each selected design, but only after its static design passes.

Inspect all 120 nominal video frames.

Stage D — Motion selection

Do not mechanically compress the entire five-second video.

Identify the best consecutive source interval with organic fire movement and tolerable topology drift. Prefer 12–24 source frames at 24 fps for the active flame body.

If the generated sequence does not present a good 0.5–1-second motion interval, reject that video rather than forcibly time-warping it.

The authored last frame controls the late runtime state; the clip does not need to reach it inside the gameplay interval.

Stage E — Mask reconstruction

Register the extracted motion to the authored first-frame geometry. Construct:

- Static authored crescent coverage.
- Firefly-derived moving interior intensity.
- Narrow authored hot-core paths.
- Broken ink coverage.
- Per-stroke erosion persistence.

With opaque black source footage, reconstruct approximate alpha under the design mask. Start with a low luminance threshold near 4/255 to exclude compression noise, then inspect soft edges at larger scale. Do not regard this threshold as universally correct.

Stage F — Runtime

Use one `FlipbookPool` impact body card and the single-pass compositor. Keep the main shape from the painted design, use selected video frames for living interior motion, and implement the reveal/decay scheduler from WP9.

### Proposed timeline for all three hits

| Event | Relative ticks at 60 Hz | Runtime design |
| --- | --- | --- |
| Contact | 0 | Narrow flash and contact core immediately bright |
| Spatial reveal | 0–4 | Three strokes rapidly open with sword-cut direction |
| Peak hold | 4–10 | Complete crafted silhouette remains prominent |
| Main erosion | 10–20 | Break tips and secondary strokes; remove most bright area |
| Ember aftermath | 20–42 | Sparse roots and fragments, no intact bright fan |

This is an initial 700 ms visual lifetime, with bright-body coverage decreasing substantially by tick 18.

The remaining sparse embers may survive beyond that point without obscuring the next strike.

The contact-to-peak period is around 67 ms; the main erosion lasts longer. Final timing is tuned after full three-hit playback.

### Measurements

| Gate | Required or proposed |
| --- | --- |
| Three visible dominant strokes | Required |
| 120–180° and ≥3:1 taper | Required |
| Hot-core area ≤5% | Required |
| Designed last-frame area 15–35% | Required pilot target |
| Last-frame overlap ≥70% | Required pilot target |
| Contact-core brightness at t=0 ≥95% of its peak | Proposed formal interpretation; see WP9 |
| Full-shape area at t=0 | Measured separately |
| No complete fan left at next contact | Required readability result |
| No clipped bright mask | Required |
| No symmetric lotus/ring appearance | Required |

### Judge

Compare Ticket 252 v1/v3 with `ff-a1-c5` in the same key-1 hit, on both stones.

First judge the body alone, then with sparks and glints.

After three iterations without a score gain, stop generating more crescent video. Use the best painted mask plus an internally animated texture and runtime erosion.

## WP4 — Metal Wind-Silk Mantle

Layer: 1 · Art can run parallel with WP3 · Runtime depends on WP1–2

Starting assets: `ff-m1-c4` for selected plate details, `ff-m1-c3` for streaming motion.

Tool: ChatGPT/Gemini painted masks; Firefly Video for internal qi movement; Codex for instanced mesh and shader; Claude for judging.

### Shape correction

The Wind-Silk Mantle must read as a field of tailored qi, not a white feather lying over the sword.

Implement:

- Two separated asymmetrical seams outside the steel.
- Small broken plate-shaped regions, not one continuous feather surface.
- Fine blue-silver moving veins.
- A clear central sword corridor.
- Open collar around the white-jade ring.
- A needle past the sword tip.
- One trailing silk ribbon.
- Small restrained sparkles along the seams and tip.

Proposed openness: 60–70% of the overall mantle envelope remains transparent or empty at play size.

### Runtime

Use a blade-hugging geometry whose placement derives from the sword's actual local orientation and dimensions.

For the six lead swords, the tailored geometry is fully enabled. For mid swords, simplify plate detail. For far impostors, embed a broken qi rim and needle in the existing impostor material instead of adding a separate card.

Three.js `InstancedMesh` supports drawing multiple objects sharing the same geometry/material with separate transforms; custom geometry attributes can carry additional UV and variation data.  [Three.js Docs +2]

### Proposed parameters

| Feature | Initial setting |
| --- | --- |
| Authored mask | 2 variants, 1024 × 256 master |
| Runtime mask | 512 × 128 or 1024 × 128 |
| Animated source | Firefly Video 24 fps; selected motion |
| Main qi flow | 0.8–1.3 texture cycles/s |
| Secondary flow | 0.35–0.65 cycles/s |
| Width breathing | ≤5% |
| Body alpha | 0.10–0.35 |
| Indigo ink alpha | 0.35–0.50 |
| Narrow hot highlights | ~1 px at play size |
| Main white coverage | ≤2% mantle ROI |
| Needle extension | 3–7 px on a 100 px sword, subject to blade-keep |

Do not implement an expensive whole-scene projected mask merely to cut out the steel. Place geometry correctly, apply an authored blade-local exclusion corridor, and verify the projected output.

### Presence and sparkle

A sword is not permitted to look completely inert between bursts. Use the moving veins and sparse glints to create presence.

The tip star remains the only imported C-direction aura element. Tiny vein highlights within the A mantle are material detail, not an additional competing aura design.

### Gate

At 60, 100 and 130 px, Metal still reads as a real sword with flowing qi outside it.

The mantle must not become a solid feather, white rectangular card or generic speed-line streak.

Run blade-keep and two-layer tests on key 7, then obtain blind scores for the real play build.

## WP5 — Fire blade sheath

Layer: 2 · Shares WP4 geometry system · Art parallel with WP3–4

Primary source: `ff-f1-c4`, the 7/7 living flame.

Secondary source: `ff-f1-c2`, useful for trailing ribbon motion.

The primary source has a valuable organic flame quality. Preserve it unless the new video clearly improves the result.

### Shape correction

Retain the dark steel blade and its hot edge.

Place flames around the outside with:

- Unequal upper and lower tongues.
- Approximately 65:35 upper/lower silhouette weight as a starting design.
- Tongues swept opposite the sword's direction of flight.
- A clean hilt end, without the fire-arrowhead blob.
- Stronger small licks toward the blade's trailing half.
- A narrow pointed fire needle beyond the sword tip.
- Open space around the jade-ring guard.

Use the designed envelope to reshape `ff-f1-c4`; do not rely on the video alone to maintain the contour.

### Runtime

Use the same blade-hugging mesh architecture as WP4, with Fire-specific masks and colour LUTs.

The Fire sheath replaces the principal Metal-looking body for the Fire presentation. Do not simply render the complete Metal mantle plus the complete Fire sheath on top of one another.

Suggested parameters:

| Parameter | Trial setting |
| --- | --- |
| Fire source | 24 fps |
| Main animated strip | 512 × 128 |
| Optional secondary strip | 512 × 128 |
| Main flow | 0.8–1.5 cycles/s |
| Body alpha | 0.25–0.55 |
| Soot backing | 0.45–0.70 |
| Hot edge | 1–2 px at play camera |
| External flame extent | 6–12 px on a 100 px sword |
| Full tongues | Existing limit ≤14 swords/frame |
| Mid/far | Ember mantle / broken ember rim |

Adapt flow to velocity without allowing every moving sword to change phase abruptly. A smooth change in texture rate is preferable to a sudden switch on launch.

### Gate

Compare the fire on stationary and flying swords against both stones, with and without the tip glint.

Require:

- No painted-over steel.
- No hilt blob.
- A backward flame direction in flight.
- Blade-keep pass.
- Final-scene contrast pass under the approved C1 objective, with the Weber-definition issue recorded.
- No cream smear after tone mapping.
- No visible loop repetition.

## WP6 — Tip star and glints

Layer: 3 · Worker: ChatGPT/Gemini for sprites, Codex for runtime, Claude for review

Reference: `ff-g1-c2`. Its jittering and oversized peak are not retained.

### Art

Produce three variations of one approved Starfire Jewel language:

- Four main tapered arms.
- Two dominant and two subordinate arms.
- Optional extremely faint diagonal detail at larger display sizes.
- Tiny white-gold core.
- Delicate asymmetry.
- No square pixels, spherical white blob, six-point emblem or stock sparkle.

### Animation

Default route: animate stable painted sprites in code.

A 12-frame source at 24 fps would last 0.5 seconds if played completely. Instead use selected 4–6 frames for the main flash, with additional low-intensity residual glint only if needed.

Proposed bright event:

- 0–2 ticks: near-maximum hot point.
- 2–6 ticks: extend/taper arms.
- 6–12 ticks: retract or break the star.
- Optional short afterglow, much dimmer.

No 1.33-second full-bright tip sparkle.

### Size-dependent detail

| Display size | Treatment |
| --- | --- |
| 12–16 px | Four simple tapered arms, 1 px centre |
| 17–24 px | More internal taper and soft secondary glimmer |
| 25–32 px | Optional faint diagonal accents, never equal to main arms |

Use a screen-size clamp, anchored slightly beyond the physical sword tip, with no significant coverage over the blade.

For major blows, use one large star and two smaller sequential flashes placed along the cut or impact.

### Measurement

Check core size, white-out, arm stability and absence of a second unintended peak.

Proposed centroid jitter limit: ≤1 px at a 24 px star. Verify stability across actual frame playback, not only source images.

### Gate

Both judges must recognize a sharp, crafted glint at 12–32 px. Reject anything that reads as a white dot, stock icon or floating coin.

## WP7 — Sparks and gold-dust aftermath

Layer: 5 · Worker: ChatGPT/Gemini for sprites, Codex for particles, Claude for testing

Negative references: `ff-b2-c2` grinder spray, `ff-b2-c1` radial firework, `ff-b3-c3` stock glitter.

### Asset

Paint three principal spark lengths with white-gold hot heads and narrow cooling tails. Use a separate restrained gold-dust atlas.

### Implementation

Use instanced camera-facing sprites with per-instance launch time, initial position, world-space velocity, sprite size, cooling rate and seed.

For a particle before collision:

$$\mathbf p(t)=\mathbf p_0+\mathbf v_0t+\frac12\mathbf gt^2$$

The gravity vector points toward the 3D ground plane. The camera projects the result into screen space.

For the occasional bounce, solve the contact time with the ground plane and reflect the normal velocity component using a low restitution coefficient. One bounce maximum.

The vertex shader can calculate deterministic age-dependent positions, while the CPU schedules particle emissions and supplies initial attributes. Collision events can be precomputed when the ground is a known plane.

### Initial parameters

| Feature | Trial value |
| --- | --- |
| Sparks per key-1 hit | 10–18 |
| Groups | 2–3 directional clumps |
| Sprite lengths | 4–7, 9–15, 16–25 px at play |
| Lifetime | 0.15–0.45 s |
| Single-bounce share | 10–20% |
| Restitution | 0.25–0.40 |
| Scatter | Suggested ±10–25° around cut direction |
| Dust aftermath | 4–10 small motes, staggered |
| Dust lifetime | 0.35–0.80 s |

These values are trial settings, not claims about real-world spark physics.

### Runtime layering

Sparks must not create uncontrolled extra coverage across the sword. Spawn mostly outside the blade footprint and within the impact's directional fan.

The sprite RGB, cooling gradient and silhouette come from authored assets and LUTs. Code may calculate particle trajectories and variation but may not invent the main spark artwork.

### Gate

At play size, sparks should show a clear size hierarchy, multiple phases of cooling and directional travel. No radial firework, uniform orange grinder shower, abrupt zigzag or bokeh-like dust.

Judge the key-1 impact once without particles and once with them. Particles pass only if they improve impact while preserving the crescent silhouette.

## WP8 — Halo Seal for large blows

Layer: 6 · Worker: ChatGPT/Gemini for design, Codex for vector/distance-field conversion, Claude for evaluation

Reference: `ff-c3-c3`, but only for the general idea of moving highlights. Do not preserve its bangle geometry or loop.

### Art

Paint two seal candidates containing:

- One principal engraved outer ring with designed breaks.
- One sparse inner partial arc.
- A few distinct carved sword-school motifs.
- Small star points moving along the seal.
- Substantial negative space.

Do not rely on generated fictional characters or unreadable writing to establish the seal's identity.

### Runtime

Convert the approved design into a clean high-resolution alpha atlas and test against a vector-derived SDF/MSDF.

MSDF is most useful when the geometry benefits from accurate sharp corners. The maker's documentation specifically addresses its ability to reproduce detailed vector shapes. Thin luminous lines may still benefit more from carefully authored alpha at the required pixel scale.  [GitHub]

### Initial values

| Feature | Trial |
| --- | --- |
| Art master | 1024 × 1024 |
| Runtime texture | 256 or 512 px |
| Large-blow screen diameter | 90–140 px |
| Thin line | 1–1.5 px |
| Reveal | 6–10 ticks |
| Hold | 6–10 ticks |
| Erosion | 18–30 ticks |
| Backing alpha | 0.35–0.50 |

The source artwork must be circular when rendered front-on. Ground-aligned seals may project elliptically because of the camera.

### Use restrictions

Show the seal only on big events: a major cast, key-7 lead-sword dive, finisher or ultimate.

Do not add it to every key-1 impact.

### Gate

At 100 px, judges must see an identifiable crafted seal, not a thick glowing ring or generic magic circle.

Require no `+` artifacts, no frame-jump and no excessive yellow competing with the reserved money colour.

## WP9 — Shared burst-in and slow-decay scheduler

Layers: 9–10 · Worker: Codex, validated by Claude · Runtime foundation may be built alongside WP2

### Timing data contract

```TypeScript
type PhaseProfile = {
  preContactTicks: number;
  contactTicks: number;
  revealTicks: number;
  holdTicks: number;
  erosionTicks: number;
  residueTicks: number;
  sourceFps: number;
  playbackMode:
    | "scroll-periodic"
    | "cyclic-frames"
    | "oneshot-frames"
    | "hold-erode";
  erosionProfile:
    | "tips-first"
    | "stroke-islands"
    | "root-to-tip";
};

type ImpactEvent = {
  castId: string;
  sourceSwordId: number;
  targetId: string;
  contactTick: number;
  seed: number;
  effectProfileId: string;
};
```

The effect phase is driven by gameplay ticks, not by an independent animation timer that may drift away from the hit.

### Immediate brightness versus reveal

The corrected rule is:

- At contact age zero, the hot contact flash or already-visible primary core must reach at least 95% of its own peak.
- The larger crescent body may reveal over the first few ticks only if the owner accepts the separate body criterion.
- If the existing 95% requirement applies to total effect brightness or total bright area, the reveal must occur before contact so the complete effect already meets the gate at contact.

This distinction must be included in the acceptance report. It is not permission to silently weaken the requirement.

### Erosion

Use a separate persistence field. Authored tips have lower survival; roots have higher survival.

For erosion progress $e(t)$, use:

$$S(x,y,t)=\operatorname{smoothstep}\left(e(t),e(t)+w,P(x,y)\right)$$

where $P$ is the authored persistence field. Use an initial transition width $w=0.06\text{–}0.12$ in normalized persistence units.

For surviving regions, a re-normalized ramp can maintain the full colour hierarchy:

$$r=\operatorname{clamp}
\left(\frac{P-e}{\max(1-e,\epsilon)},0,1\right)$$

Tune the ramp carefully near $e=1$, where the denominator becomes small.

Do not fade the entire sprite uniformly. Use the colour LUT to cool surviving fragments while allowing them to retain a small hot line until their own erosion boundary passes.

### Per-family trial envelope

| Family | Reveal | Hold | Main erosion | Residue |
| --- | --- | --- | --- | --- |
| Key-1 crescents | 0–4 ticks | 4–10 | 10–20 | 20–42 |
| Tip flash | Immediate | 2–6 | 6–12 | Minimal |
| Major-hit star | Immediate | 3–7 | 7–15 | Optional |
| Halo Seal | 6–10 | 6–10 | 18–30 | Minimal |
| Mantle entrance | 3–6 | Continuous | 9–18 on dismissal | No static fade |
| Fire sheath entrance | 3–6 | Continuous | 10–21 on dismissal | Small embers |

These are trial envelopes at 60 Hz. The final erosion duration may change with judge feedback, but the fast-attack/slow-decay principle remains fixed.

### Gate

Each effect must show a clear initial strike, short visual peak, substantially longer controlled breakup and no abrupt stop. Its last visible fragments must remain deliberately designed.

## WP10 — Gameplay, final contrast, antialiasing and 88-sword performance

Worker: Codex; Claude validates · Begins after the aura passes its own art checks

### Key-1 timeline

Maintain these absolute hit ticks relative to instant cast:

| Sword | Contact tick | Approx. contact time | Departure target |
| --- | --- | --- | --- |
| 1 | +18 | 0.30 s | After initial target-pointing hold |
| 2 | +36 | 0.60 s | +18 to +21 |
| 3 | +66 | 1.10 s | +48 to +51 |

For swords 2 and 3, departure 15–18 ticks before their contact matches the approved 0.25–0.30 seconds.

For sword 1, propose a short pointing hold during approximately ticks 0–5, then a visible flight during ticks 6–17 and contact at +18. This gives 12 flight frames before contact; the precise path is tuned to pass T4.

The approved tests remain:

- Every lead sword ≥12 frames at ≥40 px on screen.
- Flight velocity ≤12 px/frame in the designated readable interval.
- Swords 2 and 3 slow in their final 8–10 frames.
- The last 8–10 frames of those swords remain ≤12 px/frame.

Update canon timing, content definitions and golden hashes deliberately.

### Fire blade contrast

Maintain final-image ΔE OKLab ≥0.25 against both stones.

C1's Weber ≥2 criterion remains a specification blocker, because conventional positive Weber contrast cannot describe the required dark-on-light steel.

Recommended replacement for owner approval:

- Dark-on-light fractional luminance decrement: $(L_{bg}-L_{blade})/L_{bg}\geq0.65$.
- Hot-edge-on-dark positive Weber contrast ≥2 where applicable.
- ΔE OKLab ≥0.25 for the full blade comparison on both backgrounds.

Do not mark C1 PASS merely because the new proposed formulas pass. The original gate needs an explicitly approved definition.

### Antialiasing

Implement the already-approved High-setting comparison between FXAA and SMAA, respecting each pass's required colour-space order. Choose the option that preserves sword and VFX 1 px features at the real play camera within the performance budget.  [Three.js Docs +2]

### Key-7 LOD and overdraw

| Sword class | Representation | Presence detail |
| --- | --- | --- |
| 6 lead swords | Full mesh + tailored sheath/mantle | Full qi motion, small glints, occasional major-event seal |
| Up to 8 additional active mids | LOD mesh + simplified presence | Reduced Fire tongues / Metal moving seams |
| Remaining mid swords | Existing lower-detail mesh | Ember or qi edge; no independent full flame card |
| Far swords | Existing impostor quad | Broken rim and needle integrated into impostor material |

Keep the existing maximum of 14 full flame-tongue swords per frame.

Use the measured overdraw map to ensure the mantle, backing, tip star and optional ribbon do not exceed the two-contribution limit inside the protected sword region.

### Explicit removals

Disable the rejected key-1 lotus flipbook, old spark-ray spray, analytic tip star, old ground seal and procedural scorch/crack visuals from the production skill path when their replacements go live.

Do not let legacy assets remain invisibly active behind the new effects. Heat haze stays out of this package and is handled later with Water.

### Gate

Run key 7 with all 88 swords and compare against both the no-aura baseline and the Metal configuration.

Require:

- Metal ≤+0.60 ms p95.
- Fire incremental over Metal ≤+0.85 ms p95.
- No defined frame-time window over 11.5 ms.
- Blade-keep and guard gates.
- No more than two transparent contributions within sword regions.
- No unintended regression in enemy-warning, typing or money UI readability.

# 4. New art production: complete prompts and candidate counts

All prompts in this section are authored production prompts, not quotations from third-party material.

Only project-owned images may be supplied as references. No outside game screenshots, videos or third-party image references go into the image models or Firefly.

Use ChatGPT/Gemini to create and revise the 2D art after its design passes review. Use Adobe Firefly Video for the selected video generations. Firefly Image may be used for allowed image-only production if needed, but not partner models.

## 4.1 Candidate plan

| Asset | Candidates | Worker | Generation gate |
| --- | --- | --- | --- |
| Metal mantle mask | 2 | ChatGPT/Gemini | Both reviewed at real sword sizes |
| Metal motion | 2 videos | Firefly Video | Only after mantle silhouette passes |
| Fire sheath mask | 2 | ChatGPT/Gemini | Blade corridor and asymmetry measured |
| Fire motion | 2 videos | Firefly Video | First compare reprocessed `ff-f1-c4` |
| Key-1 first frame | 2 | Ticket 252 v1/v3, edited if needed | Openness and taper pass |
| Key-1 last frame | 2 | ChatGPT/Gemini EDIT | Registered against selected first frame |
| Key-1 videos | 4 | Firefly Video | Two seeds per accepted design |
| Tip-star masks | 3 | ChatGPT/Gemini | Compare at 12, 24, 32 px |
| Spark sheet | 2 | ChatGPT/Gemini | Three clear size classes |
| Dust sheet | 1 | ChatGPT/Gemini | No bokeh/glitter appearance |
| Halo Seal | 2 | ChatGPT/Gemini | Must read at 100 px |
| Jade repaint | 1 | ChatGPT/Gemini EDIT | Must match existing approved art |

Maximum initial generation allocation: 17 new image candidates/edits and 8 Firefly Video generations.

This is an allocation ceiling, not an instruction to generate everything unconditionally. If the existing `ff-f1-c4` motion processes successfully, the new Fire video runs can be deferred.

## 4.2 Common preflight rules

For every image, Claude must verify:

- Correct canvas dimensions and requested aspect ratio.
- Safe margins and no unintentionally clipped tips.
- No words, labels or unnecessary backgrounds.
- No unapproved extra objects.
- Clean separation of intended sub-shapes.
- Correct orientation of motion and sweep.
- No excessive solid white regions.
- No hidden black rectangle visible after alpha extraction.

For first/last impact images, the geometry must register in identical pixel coordinates.

For video generation, select Firefly Video, use the requested black-background mode, keep the camera static and record the settings. Disable prompt enhancement unless the experiment explicitly calls for testing it. Adobe documents first/last image inputs and the camera restrictions associated with using them.  [Firefly]

The following Firefly Video prompts are each under 600 characters.

## 4.3 Metal mantle

M-IMAGE — two authored design candidates

> [Writing] Create a premium xianxia Wind-Silk Mantle mask for a real-time flying sword, without drawing the sword itself. Wide horizontal canvas, pure black background, point to the right. Two asymmetrical tailored seams of fine silver-white qi thread sit outside a completely open central blade corridor. Small broken feather-like plates and flowing silk filaments form elegant fragments, never a solid feather or fern. Preserve generous black gaps, an open hilt collar, two seams meeting in a fine needle beyond the tip, and one trailing silk ribbon. Sharp hand-painted anime/donghua forms, grayscale mask, large safe margins. No smoke, scenery, text or large glow blobs.

Candidate M1 uses sharper geometric plate fragments; candidate M2 uses softer silk filaments. Do not change the approved mantle design family.

M-VIDEO — two Firefly runs

> [Writing] On pure black, one narrow horizontal band of living silver-white sword qi. Fine silk filaments flow continuously toward the right, while broken feather-like energy slivers ripple independently. Keep two separated seams, large dark gaps, sharply tapered ends, a stable narrow envelope, and delicate blue-silver highlights. The camera is fixed. Motion remains inside the authored shape. No sword, solid feather, fern, smoke, burst, scenery, text, or camera movement.

Use the result as interior-motion data, not as the final silhouette.

## 4.4 Fire sheath

F-IMAGE — two authored design candidates

> [Writing] Paint one asymmetric Fire sheath mask for a straight flying sword on pure black, wide horizontal canvas, tip to the right. Do not draw the sword. Keep a completely open central corridor for dark steel. Soft flame tongues emerge only outside the two blade edges and sweep backward toward the left, with a few small sharp detached licks. The upper and lower contours must differ strongly. The hilt area stays narrow and almost empty, without a bulb or arrowhead. A thin pointed flame needle extends beyond the tip. Premium hand-painted anime/donghua fire design, rich taper, generous black negative space and safe margins. No smoke cloud, ring, scenery or text.

One candidate uses longer flowing tongues, the other shorter layered tongues.

F-VIDEO — two Firefly runs if reuse fails

> [Writing] On pure black, a narrow asymmetric sheath of soft orange-red fire flows backward, right to left, around an invisible straight blade. Upper and lower flame tongues differ; small fast licks trail behind larger soft curls. Keep a clear dark centre, an almost empty hilt end, and a fine pointed tip. The external envelope stays slender. Fixed camera, living hand-painted flame movement. No sword, hilt blob, fireball, smoke cloud, ring, scenery, text, or camera movement.

First attempt to recover the best interior motion from `ff-f1-c4`; do not generate two new videos if the existing source already passes the interior-motion test.

## 4.5 Key-1 impact first-frame artwork

Both variants must be composed into opaque black 1080 × 1080 square images for the proven black-background Firefly workflow.

I-FIRST-V1 — open nested fan

> [Writing] Create the first frame of a premium xianxia Fire sword impact, opaque black 1080×1080 square. Three large distinct open flame-brush crescents sweep from a lower-left strike root toward the upper right. Each crescent spans 120–180 degrees, with a thick powerful base tapering into an extremely fine needle, thickness ratio at least 3:1 between centreline positions 20% and 80%. Preserve an open fan, not a circle or C. Include four or five short counter-strokes and a few detached flame tongues. Rich orange-red body, a hair-thin white-gold leading edge, broken dark-ink underlay, soft living interior flame. Elegant luxurious anime/donghua calligraphy. Generous safe margins. No sword, lotus, smoke, scenery or text.

I-FIRST-V3 — two long strokes and one counter-stroke

> [Writing] Create the first frame of an elegant xianxia Fire sword-cut impact on an opaque black 1080×1080 square. Two long unequal flame-brush crescents sweep from the lower-left strike root toward the upper right. A distinct short third crescent counters their motion. These must remain three separate OPEN strokes, never a closed ring. Every stroke has a heavy base and needle tip, at least 3:1 taper. Add four or five small counter-flicks and a few isolated licks. Saturated orange-red flame, a very thin white-gold hot leading edge, broken dark ink beneath, refined soft organic fire interior. Large margins. Premium hand-painted anime/donghua style. No lotus, sword, scenery, smoke or text.

### First-frame approval

Claude generates a mask report before any video run:

| Check | Acceptance |
| --- | --- |
| Dominant strokes | 3 |
| Arc range | 120–180° each |
| Base/tip taper | ≥3:1 |
| White-gold edge | ≤5% of main luminous region |
| Root position | Stable across intended sequence |
| Open overall shape | No unintended closed C/ring |
| Margins | No clipped needle or detached lick |

If neither passes, edit the existing designs rather than restarting from unrelated artwork.

## 4.6 Key-1 last frame

Use the approved first-frame image as the edit input.

I-LAST — run once for each approved first frame

> [Writing] EDIT the supplied first-frame image. Keep the canvas, strike root, three crescent paths, spacing, scale and directions exactly registered. Transform the SAME strokes into late ember remnants. The long flame bodies have burned down to thin broken red-orange lines, a few dark ember fragments and very small pale-gold hot points. Bright remaining area must be 15–35% of the first image. At least 70% of remaining bright pixels must lie inside the first-frame stroke masks. Tips are fragmented; original roots remain identifiable. Do not move, rotate, replace or invent strokes. Keep the same opaque pure-black background. No new circles, lotus, smoke or text.

Do not select the last frame by appearance alone. Quantitatively register it against the first.

## 4.7 Key-1 Firefly Video generation

I-VIDEO — two runs for each approved first/last pair

> [Writing] Animate the supplied first and last images as the same three open, tapered flame-brush crescents. Living orange-red fire flows from heavy roots along the curves toward fine tips; tiny detached licks flutter. Thin white-gold leading edges shimmer, then the original strokes tear into matching ember fragments. Preserve each stroke's position, open arc, direction and identity. Fixed camera, pure black. No new circles, lotus, extra strokes, smoke, scenery, text or camera movement.

Configuration: Firefly Video, 1080p, square, opaque black, transparent mode off, 24 fps, 5 seconds, both frames uploaded.

Selection: Produce a 120-frame contact sheet and numerical shape report. Reject spontaneous new arcs, large global rotation and asymmetric shape collapse. Extract a continuous period of valuable internal motion, then let the runtime implement the short actual skill event.

## 4.8 Tip star

G-IMAGE — three variations

> [Writing] Paint a premium sword-tip glint sprite sheet on pure black with three isolated variations of one elegant white-gold four-point star. Each star has two long sharp tapered arms, two shorter delicate arms, a tiny bright nucleus and faint irregular secondary light. At small scale the main four arms must remain recognizable. Make the three versions subtly different in arm length, taper and asymmetry, but clearly one design family. Clean luxurious anime/donghua jewel-like linework, crisp fine edges and large black spacing. No round white blob, square sparkle, six-point star, clip-art shape, lens effects, sword, scenery or text.

No new Firefly Video run initially. Animate stable painted shapes in code.

## 4.9 Sparks

S-SPARK — two sheets

> [Writing] Create a separated sprite sheet of premium xianxia fire sparks on pure black. Three length families: short sharp sparks, medium tapered streaks and long elegant needle trails. Every spark has a tiny brilliant white-gold hot head, slender orange body and very thin dark-red cooling tail. Vary curvature and taper subtly. The sheet is designed for directional GPU particles, so keep each spark isolated with generous black padding and no overlaps. Luxurious hand-painted anime/donghua energy. No firework bursts, circular sprays, equal-length rods, zigzags, glitter, bokeh, smoke, scenery or text.

S-DUST — one sheet

> [Writing] Create a sparse premium ember-dust sprite sheet on pure black. Isolated tiny irregular warm-gold flecks, red-orange cooling specks, delicate micro-streaks and a few miniature asymmetric four-point glimmers. Give every sprite its own large black margin. Designed to appear briefly after a magical sword blow, never as a continuous particle cloud. Sharp, elegant, restrained, hand-painted anime/donghua detail. No circular light discs, stock glitter, hexagons, large stars, scenery or text.

Movement is entirely runtime-controlled.

## 4.10 Halo Seal

H-SEAL — two designs

> [Writing] Design one premium xianxia sword-school Halo Seal as precise thin white lines on a pure black square. One incomplete circular outer ring, one sparse inner arc, deliberate breaks, and a small number of original engraved motifs derived from sword, cloud and flame geometry. Use clean distinct quadrants and abundant negative space. Every shape must remain legible as a designed seal when reduced to 100 pixels. Perfect circular geometry when viewed face-on. Suitable for vector tracing and SDF/MSDF conversion. No thick bangle, repeated concentric rings, invented written characters, generic magic circle, glow haze, stars, scenery or labels.

Use distinct engraving layouts for the two candidates, not two colour versions.

## 4.11 Jade-ring repaint

J-RING — one edit using the approved sword reference

> [Writing] EDIT the provided game sword using the approved project sword image as the identity and material reference. Change ONLY the existing hollow guard ring from chrome-silver to polished white jade with a narrow pale-antique-gold rim. Preserve the exact shape and opening of the ring, its green-jade beads, cloud carving, blade, grip, lotus pommel and all geometry. The new ring must read as premium white jade, not luminous plastic or mirror chrome. Keep the original lighting direction, framing, aspect ratio and anime/donghua material style. No changes to the background or any other sword component.

Important integration distinction: A beautiful edited reference image is not automatically a working 3D sword material. Codex must transfer the approved colours/texture characteristics to the actual sword mesh and validate the rendering under the real scene lighting.

If an atlas repaint is required, preserve the original UV layout and use an edit registered to the actual UV texture. Do not substitute the perspective concept image as a UV map.

# 5. Exact resolutions to the five technical questions

## A. Seamless loops without ghosts

Sheath/mantle: Use a spatially periodic interior-motion texture on a blade-hugging mesh. The authored exterior remains stable. Two different motion samples inside one shader add temporal richness without doubling geometry.

Impact: Do not loop. Play selected source motion once, then hold and erode.

Glints: Do not loop. Use curated one-shot sprites.

Seal: Do not loop its entire artwork. Animate selected segments and spark positions, then erode.

Validated cyclic animation: Allowed only if both the measured seam and visual continuity pass. The old eight-frame crossfade is removed.

A spatial tile must satisfy edge continuity not only for brightness but for visible filament and flame direction. A perfectly matched edge that reveals an obvious repeated motif every 0.7 seconds still fails the visual test.

## B. First-frame 95% versus burst-in

The two demands are mathematically incompatible for the same entire shape at the same moment if the shape begins invisible.

Implement one of two explicitly documented modes.

Mode 1 — Contact flash interpretation: The contact flash reaches ≥95% peak brightness immediately. The three-crescent body rapidly reveals after contact. Record total-body brightness and coverage separately.

Mode 2 — Strict whole-effect interpretation: Reveal the body during pre-contact motion. At the actual impact tick, it is already ≥95% of its eventual peak brightness.

The current project specification must choose which quantity the gate means. Codex must not silently substitute Mode 1 for a whole-effect requirement.

## C. Dark backing without a sticker or extra pass

Use the authored broken-ink mask, body coverage and hot-core mask within one fragment shader.

Dark ink has relatively high alpha and dark linear RGB; the core adds small bright RGB contribution. Ink and core must have separately controlled coverage, brightness and survival.

The effect is still one rendered transparent surface. However, this does not make overlapping separate ribbons or sprites free: those remain additional fragment contributions.

Judge the backing alone, then the final composite. A continuous black perimeter is an artistic failure even if it produces excellent numerical contrast.

## D. Card flipbooks or blade-hugging meshes?

Use the following fixed mapping.

| Effect | Runtime representation |
| --- | --- |
| Metal mantle | Blade-hugging mesh with scrolling motion texture |
| Fire sheath | Blade-hugging mesh with scrolling motion texture |
| Silk/flame tail | Path-following ribbon, preferably merged with existing aura geometry |
| Tip star | Painted camera-facing sprite |
| Key-1 crescents | One-shot flipbook/card with authored spatial mask |
| Sparks/dust | Instanced painted sprites |
| Halo Seal | Painted alpha or SDF/MSDF |
| Far-sword aura | Incorporated into existing impostor material |

Do not return to full-rectangle sheath/mantle cards merely because their source videos scored 7.

## E. Keeping the real blade visible

Use art, geometry and measurement simultaneously.

- The central corridor is truly empty in the authored mask.
- The blade-hugging geometry sits outside the steel.
- The one-pixel gap is measured after projection and antialiasing.
- The ring/guard region is explicitly protected.
- Glow and backing use the same blade exclusion.
- Tip glints sit beyond the blade tip.
- Trails and secondary effects are counted in the total overlap test.
- Final screenshots must pass the original blade-keep percentages and the Fire C2 ≤5% in-flight VFX-over-blade gate.

If the final 60 px sword looks white and feather-shaped despite numerical overlap passing, fail the art design and return to WP4.

# 6. Risk mitigation and verification matrix

| Risk | Detection | Required response |
| --- | --- | --- |
| Firefly ignores authored shape | Stroke correspondence, mask overlap, video contact sheet | Reject that clip; keep authored shape, reuse interior motion only |
| Last-frame design arrives too late | Full 5-second timeline inspection | Use runtime late-state mask; do not compress whole video automatically |
| Painterly static texture remains visible | 100 px and close-up footage | Increase useful internal motion, refine texture extraction, keep outer mask |
| Repeating texture looks mechanical | Ten-cycle moving sword capture | Change phase combination, select better motion, or use validated cyclic frames |
| Black-background matte creates fringes | Composite against both stones with enlarged edge crops | Correct coverage and edge colours under authored mask |
| Dark backing looks like a sticker | Backing-only and final captures | Break its contours, reduce coverage/alpha, avoid continuous outlines |
| HDR core clips or loses brightness | Pre/post-tone mapping and bloom comparison | Fix target/blending path or use judged LDR fallback |
| Solid Metal mantle hides sword | Projected mask/OKLab blade-keep and subjective identity test | Edit mantle silhouette, not just opacity |
| One-pixel gap collapses | Final post-AA 60/100/130 px captures | Adjust geometry, exclusion and final line widths |
| Fire hilt blob remains | Silhouette analysis in flight | Remask/reposition source motion; reject if persistent |
| Star becomes a white dot | Real 12 px output | Simplify and sharpen primary arms; keep tiny centre |
| Stars look like clip art | Independent style judging | Replace sprite geometry; do not add more bloom |
| Sparks become fireworks | Spawn-angle distribution and trajectories | Reduce spread, keep 2–3 coherent directional clumps |
| Gold dust becomes bokeh | Sprite sheet and final play capture | Replace round shapes with tiny authored flecks |
| Halo becomes a bangle | 100 px capture | Remove secondary arcs; widen important gaps |
| Main body dies too quickly | Bright area versus time | Adjust persistence/erosion, preserve short hold |
| First hit obscures second | Key-1 three-hit replay at real speed | Remove intact bright fan earlier; leave sparse ember residue |
| Multiple layers exceed cap | Per-pixel overdraw diagnostic | Merge appearance within one shader or move layers outside blade |
| Source texture memory exceeds budget | Atlas memory inventory, upload monitoring | Use smaller cells and fewer variants |
| High GPU cost is misattributed | Matched repeated A/B with CPU metrics | Report actual frame-time evidence; do not claim isolated GPU time |
| Changed hit timing breaks gameplay tests | Canon and golden-hash diff | Update intentionally and test all downstream events |
| Old rejected visuals remain active | Effect registry audit and layer captures | Disable unused effect paths before acceptance |
| White jade renders as chrome | Sword-model material inspection and final capture | Correct material/UV source, not merely an image overlay |

## 7. Work order, parallel execution and stopping rules

| Order | Work | Dependency / decision gate |
| --- | --- | --- |
| 0 | Measurement baseline | Must finish first |
| 1–2 | Compositor and asset/loop infrastructure | Run in parallel; both need WP0 |
| 3 | Impact first/last image approval | Parallel with WP1–2 |
| 4–5 | Metal and Fire sheath artwork | Parallel with WP3 art; reuse existing video first |
| 3 video | Firefly impact motion | Only after impact designs pass |
| 6–8 | Glints, particles and Halo Seal art | May start early; integrate after compositor |
| 9 | Common timing/erosion | Framework parallel with WP2; final tuning after assets |
| 10 | Gameplay timing, readability and full integration | After selected aura and impacts are integrated |
| Final | Blind acceptance and regression | Both judges ≥8.5 and all hard gates |

### Three-attempt rule

For each failing package, Claude records the targeted defect and current lower judge score.

An attempt counts as an improvement only when it produces a reproducible technical improvement without a new critical defect, or raises the lower blind-judge score. As an initial practical threshold, a score gain of 0.25 or greater is meaningful enough to continue exploring, but 0.25 is not a substitute for the owner's final 8.5 threshold.

After three attempts without useful improvement, stop that method.

Examples:

- Three failed impact generations: switch to an authored mask with interior animated fire instead of more image-to-video attempts.
- Three failed mantle-scroll integrations: change the internal animation strategy, not the owner-approved mantle design.
- Three failed MSDF seal tests: use the painted high-resolution alpha mask.
- Three failed particle visualizations: change the authored spark shapes or emission design, not just particle count.

No production acceptance is achieved through score averages. The lower of the two judge scores must be at least 8.5.

## 8. Blind judging and evidence package

For every package, Claude creates a review record with the following fields:

```JSON
{
  "candidateId": "wp3-impact-v1-attempt1",
  "sourceAssets": ["ticket252-v1", "ff-a1-c5"],
  "gitCommit": "record-current-commit",
  "renderProfile": "normal-high",
  "camera": "play",
  "ground": "light-and-dark",
  "playback": ["1x", "0.25x"],
  "captures": {
    "isolated": true,
    "fullSkill": true,
    "beforeAfter": true
  },
  "technicalGates": {
    "maskShape": "pending",
    "bladeKeep": "pending",
    "whiteOut": "pending",
    "loopOrOneShot": "pending",
    "performance": "pending"
  },
  "judges": {
    "judge1": null,
    "judge2": null
  },
  "decision": "pending"
}
```

This is an example of the required record structure, not an existing file or actual test result.

### Judge protocol

1. Capture the same deterministic event with the baseline and candidate.
2. Produce light-stone and dark-stone sequences, normal speed and 0.25×, plus approved close-ups.
3. Randomize candidate labels and presentation order.
4. Keep asset names, prompts, implementation method and prior scores hidden from judges.
5. Have the two judges score independently before seeing each other's comments.
6. Record scores and failure descriptions without changing their wording.
7. Run technical gates and performance tests independently of subjective scoring.
8. When a candidate reaches 7, provide the owner with the demo video.
9. When both judges reach 8.5, run the full unmodified host and regression tests.
10. Reopen acceptance if later changes degrade an already accepted layer.

The technical assessment is not permitted to override the two blind scores. Conversely, visual scores do not waive hard rendering, timing or performance requirements.

### Minimum package-specific captures

| Package | Mandatory capture |
| --- | --- |
| WP1 backing | Same `ff-f1-c4` source with backing off/on, on both stones |
| WP2 loop | Ten consecutive cycles at real speed and 0.25× |
| WP3 impact | Each of three key-1 hits isolated, followed by the complete sequence |
| WP4 Metal | Stationary, accelerating and flying swords at 60/100/130 px, plus key 7 |
| WP5 Fire | Dark steel with Fire on/off, moving and stationary, both stones |
| WP6 glints | 12/24/32 px tip star, plus sequential major-hit glints |
| WP7 sparks | Full strike with particles off/on, directional spawn and aftermath |
| WP8 seal | 100 px large blow and close-up, showing reveal/hold/erosion |
| WP9 scheduler | Brightness and area-over-time plots for impact and glint |
| WP10 integrated | Normal host, all 88 swords, both elements, gameplay timing and full UI |

## 9. Remaining uncertainties and decisions requiring evidence

The following cannot be certified from the supplied descriptions alone.

Art-source uncertainties: The actual Ticket 252 v1/v3 images, original Firefly footage, masks and atlas metrics are not available for direct frame inspection in this review. Whether v1 or v3 is superior remains unverified.

Motion uncertainties: It is not established that useful spatially tileable flame strips can be extracted from the existing videos without losing the organic motion judges preferred. This requires direct footage testing.

Rendering uncertainties: The exact intermediate render-target format, custom shader interactions, current postprocessing configuration, float blending capability and output colour treatment need inspection in the actual installed runtime.

Performance uncertainties: The project has no usable GPU timer-query measurements on the stated Mac mini M4 setup. Per-layer rendering cost can be estimated through repeated frame-time differences, but cannot truthfully be reported as measured GPU execution time.

Metric uncertainties: The owner-approved Weber ≥2 requirement has no conventional achievable interpretation for dark steel against brighter stone. The precise first-frame 95% definition also needs formal interpretation before marking that gate as passed.

Quality uncertainties: Neither ΔE thresholds nor attractive isolated art guarantee an 8.5 blind score. The proposed alpha, motion and timing values are informed starting points to be judged in context.

Asset-memory uncertainties: Whether 256 px or 384 px impact cells are sufficient for the 400–500 px close-up is an empirical decision. Increasing atlas size without visible benefit should not be accepted.

These uncertainties are explicitly listed as test tasks or acceptance blockers rather than treated as established facts.

## 10. Verified source basis

The following references were checked for this review. They support the relevant technical capabilities, not artistic scores or game-specific numeric thresholds.

| Source | What it supports |
| --- | --- |
| [Adobe — Generate videos using images](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html) | Firefly Video model selection, source image inputs, 24 fps and keyframe guidance |
| [Adobe — Transparent-background generation](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html) | Transparent PNG keyframe restrictions, foreground/alpha outputs, transparent workflow |
| [three.js — Material](https://threejs.org/docs/pages/Material.html) | Custom blending factors, depth, transparency and material properties |
| [three.js — ShaderMaterial](https://threejs.org/docs/pages/ShaderMaterial.html) | Custom GLSL shader implementation |
| [three.js — Colour Management](https://threejs.org/manual/pages/color-management.html) | Linear working space, output conversion and non-colour texture treatment |
| [three.js — DataTexture](https://threejs.org/docs/pages/DataTexture.html) | Uploading exact typed-array texture channels |
| [three.js — Texture](https://threejs.org/docs/pages/Texture.html) | Wrapping, mipmaps, filtering and premultiplication settings |
| [three.js — InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html) | Shared-geometry instanced rendering |
| [three.js — SMAAPass](https://threejs.org/docs/pages/SMAAPass.html) and [OutputPass](https://threejs.org/docs/pages/OutputPass.html) | Correct postprocessing order and colour-space constraints |
| [Khronos — EXT_color_buffer_float](https://registry.khronos.org/webgl/extensions/EXT_color_buffer_float/) | Floating-point render-target formats |
| [Khronos — EXT_float_blend](https://registry.khronos.org/webgl/extensions/EXT_float_blend/) | Floating-point blending capability requirements |
| [Khronos — GPU timer query extension](https://registry.khronos.org/webgl/extensions/EXT_disjoint_timer_query_webgl2/) | Optional GPU timing support |
| [FFmpeg — Filters documentation](https://ffmpeg.org/ffmpeg-filters.html) | Motion-compensated interpolation and its alternatives |
| [msdfgen — Author's implementation](https://github.com/Chlumsky/msdfgen) | SDF/MSDF generation for vector contours |
| [Björn Ottosson — Oklab](https://bottosson.github.io/posts/oklab/) | Oklab definition and conversion principles |

# 11. Final merged production decision

The execution order is now unambiguous:

1. Establish the real baseline and rendering capabilities.
2. Fix premultiplied compositing, mask data and atlas playback.
3. Select Ticket 252 v1/v3 as the designed Brushfire source and generate only the motion necessary to animate it.
4. Rebuild the Metal mantle and Fire sheath on blade-hugging geometry, salvaging existing Firefly motion.
5. Add painted tip glints, directional Starfire sparks and the restricted engraved Halo Seal.
6. Apply a common contact/reveal/hold/erosion scheduler.
7. Implement the already-approved key-1 gameplay timings, blade contrast, guard repaint, antialiasing and 88-sword LOD limits.
8. Run technical gates and both independent blind judges in the normal play host.

The critical design principle remains unchanged:

Paint the silhouette. Use Firefly for organic internal motion. Use shaders for colour, dark backing and luminous structure. Use geometry and code for placement, direction, timing and controlled decay.

The two unresolved specification issues—C1's Weber formulation and the exact scope of the first-frame 95% brightness requirement—must remain visible as acceptance blockers, not be silently reinterpreted by Codex.

Everything else in the corrected plan has a defined starting asset, responsible worker, processing route, runtime representation, trial parameter range, verification method and rejection path. That makes it suitable for implementation and experimentation, while leaving final artistic acceptance where the owner requires it: two independent judges, both ≥8.5, in the real game.


---

**[TURN · Lượt chạy 1 · Rà soát 2 của ChatGPT: FAIL (nguyên văn, 80.233 ký tự)]**

VERDICT: FAIL

## Problems found in the previous answer

The previous revision fixed several earlier problems, but another strict review against the original brief identifies 18 remaining issues. These are substantive enough to prevent a PASS.

| ID | Problem | Required correction |
| --- | --- | --- |
| P01 | The answer incorrectly left the first-frame 95% brightness gate unresolved. The brief already specifies “flash and core drawn at age 0.” There is no need to reopen the owner's decision. | Make the flash/core ≥95% bright at the first rendered impact frame. Apply burst-in to the larger shape separately, without delaying the flash. |
| P02 | The answer proposed replacing the owner's Weber ≥2 gate with different thresholds. That would change an approved decision. | Preserve Weber ≥2 and ΔE OKLab ≥0.25. Document the sign/reference problem for dark-on-light contrast, measure both polarity cases, and never substitute an unapproved threshold. |
| P03 | The cited Adobe documentation says that supplying both first and last frames disables the camera-motion controls. The previous instructions did not distinguish a fixed-camera prompt from a selectable camera setting.  [Firefly] | Use the fixed-camera prompt and static-source validation; do not instruct Claude to set a disabled control. |
| P04 | The 24 fps source footage and the existing 12 fps extracted candidates were treated too interchangeably. `ff-f1-c4` and `ff-m1-c4` contain 24 retained frames at 12 fps, representing approximately two seconds of the original movement. | Track original source rate, extraction rate and playback rate independently. Never reinterpret the retained 12 fps frames as 24 fps without intentionally changing speed. |
| P05 | The source-to-mask process was incomplete. A black-background video does not contain recoverable ground-truth alpha, and applying the authored mask alone may produce static flame silhouettes. | Use a maximum authored envelope, separate moving coverage/detail, controlled boundary deformation and manually verified antialiased alpha. |
| P06 | The proposed two-scrolling-texture method was assumed to preserve Firefly's living motion. It might instead produce moving wallpaper with an almost static outer contour—the exact defect the judges rejected. | Use scrolling textures as the first trial, with a measurable motion-quality gate and a defined fallback to registered, animated coverage on the same mesh. |
| P07 | The previous compositing code treated `premultipliedAlpha: false` as though it described only texture input. In three.js, texture upload premultiplication, material settings and the renderer's default-framebuffer configuration are separate concerns.  [Three.js Docs +2] | Define the RGB/alpha shader-output contract explicitly and test the blend equation against a reference image. |
| P08 | The colour-processing plan did not fully define LUT sampling, colour-space conversion, HDR rendering, bloom ordering and the effect of tone mapping on the hot-core measurements. | Specify separate data-mask and colour-LUT paths, linear RGB compositing, exact measurement stages and a tested HDR fallback. |
| P09 | The one-pixel gap and two-transparent-layer constraints still lacked an executable per-pixel coverage test. Counting draw calls or artist-intended layers is insufficient. | Use a separate overdraw diagnostic pass with the same depth tests and alpha-discard rules. Count contributions within the projected sword masks. |
| P10 | The proposed Key-1 impact remains too bright for too long relative to the revised first and second hits at +18 and +36 ticks. Only 300 ms separates those impacts. | Cap the surviving bright-body coverage before the next hit while retaining a longer, sparse ember aftermath. Test all three hits together. |
| P11 | The proposed particle system was still ambiguous about the actual ground plane, collision timing, instance data and how projected particle lengths would be clamped. | Define deterministic world-space trajectories, shader/CPU responsibilities, collision handling and size-dependent rendering. |
| P12 | The image/atlas specification mixed source dimensions, frame-cell dimensions and usable pixel dimensions without sufficiently defining cropping, gutters, UV bounds or mipmap behaviour. | Adopt one atlas contract, quantify memory, and use constrained UVs or separate texture layers where appropriate. |
| P13 | The Halo Seal instructions did not explain that MSDF generation requires suitable vector outlines; a painted raster cannot simply be passed to `msdfgen` as though it were an SVG.  [GitHub] | Use raster alpha as the first baseline; generate a single-channel SDF from the cleaned raster, or trace and repair actual vector paths before MSDF conversion. |
| P14 | The previous answer did not specify how non-Git media reaches the normal skills-lab build. This is an integration blocker because final acceptance cannot use URL flags or missing local assets. | Implement a versioned external-media manifest and normal asset-loading path, with checksums, preload, error handling and production-host verification. |
| P15 | The previous plan omitted an explicit sparkle allocation for every required shape and did not establish a clear hierarchy preventing a large Fire hit from becoming visually noisy. | Add an effect-wide sparkle budget, with separate rules for presence, tip glints, impacts, sparks and big-blow seals. |
| P16 | Some exact numeric settings were presented without sufficient visual or mathematical justification, particularly the impact timing, halo timing, arbitrary contrast thresholds and frame-time test windows. | Distinguish fixed requirements from trial parameters. Provide calculation methods and a tuning procedure rather than treating initial guesses as certified limits. |
| P17 | The release process did not adequately account for the final placement of a screen-designed impact in the three-dimensional 55° camera scene, sorting/depth issues, the approved jade-ring material or legacy-effect removal. | Add explicit anchor/orientation, transparency ordering, material conversion and old-effect-disable steps. |
| P18 | Several new art generations were still proposed before checking whether existing Firefly candidates could supply the necessary motion. The candidate counts also needed a staged stop/go procedure. | Reuse existing video wherever possible, approve authored silhouettes before video generation, and stop after three non-improving attempts on the same method. |

### Source-verification result

The relevant official documentation is available and supports the following narrower conclusions:

- Adobe Firefly Video supports first/last keyframes, and current documentation describes 24 fps generation. With both keyframes provided, camera-motion controls are disabled.  [Firefly]
- Adobe's transparent-background workflow requires transparent PNG keyframes and produces foreground and alpha videos. This is different from the project's opaque-black 1080p workflow; Adobe's documentation does not independently establish that every 1080p transparent generation must fail.  [Firefly]
- Three.js supports custom material blending, data textures and instanced rendering. Those features do not, by themselves, guarantee that the proposed shader will satisfy the game's appearance or performance budgets.  [Three.js Docs +2]
- Khronos distinguishes colour-renderable floating-point attachments from blending support and optional GPU timing extensions. The actual render-target configuration must be checked.  [Khronos Registry +2]
- Three.js documents different postprocessing orders for SMAA and FXAA relative to `OutputPass`.  [Three.js Docs +1]

The corrected specification follows. All numerical values explicitly described as trial values are implementation starting points, not newly imposed owner decisions.

# Corrected full analysis and production solution

Project: Tu Tien Thu Ai
Target: Both blind judges ≥8.5/10 in the normal play host
Engine: three.js / WebGL2, fixed three-quarter camera, approximately 55° tilt
Scope: Metal and Fire sword skills, especially Key 1 and Key 7
Source status: The artwork and runtime facts come from the project brief. The implementation recommendations below are engineering proposals; they have not yet been tested against the original media files or running project.

## 1. Non-negotiable design and integration contract

The solution must preserve these decisions, without reopening their artistic direction.

| System | Fixed requirement |
| --- | --- |
| Metal aura | Wind-Silk Mantle A: tailored external qi plates, two seams, 1 px steel gap, needle tip, open collar and silk tail |
| Fire aura | Dark steel with hot edges, asymmetric flames around the steel |
| Tip accent | One approved C-derived tip-star layer; no additional competing B/C sword-aura concepts |
| Sword identity | White-jade hollow ring with restrained pale-gold rim, matching approved reference |
| Key-1 body | Three open flame-brush crescents, 4–5 counter-strokes, detached tongues, thin white-gold core |
| Sparks | Starfire Jewel, directional clumps, three lengths, gravity, occasional single bounce |
| Halo | Engraved thin seal, only major events |
| Animation | Fast attack, designed peak, slow erosion; organic fire remains soft |
| Blade readability | Existing blade-keep, T1/T4, C1/C2 requirements |
| Compositing | No more than two transparent contributions per pixel inside any sword's screen region |
| Performance | Metal ≤+0.60 ms p95; Fire incremental ≤+0.85 ms p95; no defined frame-time window over 11.5 ms |
| Approval | Both independent blind judges ≥8.5 in normal player settings, without URL flags |

Other invariants: 38 px/m play-camera scale, 60–130 px swords, 12–32 px tip glints, 70–160 px impacts, and 400–500 px close-ups.

The approved reserved colours remain enemy warning red `#FF4A4A`, typing teal `#7FF5E0` and money gold `#FFC83A`. Fire remains orange-red. These reserved colours are checked in the final scene rather than merely against the artwork palette.

No partner AI models, local AI models, Firefly Video Topaz upscaling, third-party image inputs or rejected Blender stepped-fire pipeline.

The division of labour is:

- ChatGPT/Gemini: Generate/edit authored 2D image assets after their design is approved.
- Firefly Video: Generate living organic internal movement using the Adobe model.
- Codex CLI: Implement shader, geometry, game logic, integration, measurement code and sound where needed, using `gpt-6.1-sol` at xhigh/ultra according to the project's workflow.
- Claude: Coordinate, operate Firefly, process assets, run captures and metrics, organize independent blind judging and record decisions.

## 2. One consistent technical architecture

The new system consists of five visual representations, not ten unrelated custom effect engines.

| Representation | What it renders | Shared implementation |
| --- | --- | --- |
| Blade-attached mesh | Metal mantle, Fire sheath | One instanced, blade-local geometry/material system |
| Ribbon | Silk tail, Fire trailing band | Existing ribbon system, masked and constrained |
| One-shot effect card | Three-crescent impact body | Revised `FlipbookPool` |
| GPU-instanced sprite | Tip star, secondary glints, sparks, gold dust | One particle/sprite renderer with separate profiles |
| Authored seal | Halo engraving and its segments | High-quality alpha or SDF/MSDF material |

All five representations use the same colour-design vocabulary: dark broken ink, translucent coloured body, thin bright core, controlled sparkle and spatial decay.

The intended source-to-runtime pipeline is:

```Plain text
APPROVED ORIGINAL DESIGN
    |
    +-- Authored image (ChatGPT / Gemini)
    |       -> silhouette / ink / core / persistence masks
    |
    +-- Existing or new Firefly Video
    |       -> stabilized organic motion data
    |       -> verified sample fps
    |       -> motion atlas or periodic textures
    |
    +-- Offline processing (Claude)
    |       -> registration and matte reconstruction
    |       -> channel packing
    |       -> atlas and manifest
    |       -> contact sheets and metrics
    |
    +-- Runtime integration (Codex)
            -> mesh / card / sprite / seal
            -> material colour LUT
            -> blending and blade protection
            -> tick-synchronized timing
            -> deterministic LOD and particle rules
    |
    v
NORMAL SKILLS-LAB PLAY HOST
    -> technical gates
    -> two independent blind judges
    -> owner demo and acceptance
```

The primary artwork must never be invented by procedural geometry. Shader noise, flow sampling and erosion may animate or reveal authored artwork, but they cannot replace it with generic Voronoi, analytic feathers, lotus rings or generated crack patterns.

# 3. Dependency-ordered work packages

| Order | Package | Execution dependency |
| --- | --- | --- |
| WP0 | Baseline and technical gates | First |
| WP1 | External media and manifest | After WP0; parallel with WP2 |
| WP2 | Single-pass backing/HDR compositor | After WP0; parallel with WP1/WP3 |
| WP3 | Motion extraction, loops and flipbook engine | Parallel with WP1/WP2 |
| WP4 | Key-1 Brushfire impact | Image approval first; integration after WP2–3 |
| WP5 | Metal Wind-Silk Mantle | Artwork parallel with WP4; code after WP2–3 |
| WP6 | Fire blade sheath | Reuse WP5 geometry; art parallel |
| WP7 | Tip glints and sparkle hierarchy | Artwork parallel; integrate after aura |
| WP8 | Directional sparks and gold dust | Artwork parallel; tune with WP4/WP7 |
| WP9 | Major-hit Halo Seal | Independent artwork; integration after WP2 |
| WP10 | Burst, hold and erosion scheduler | Core code parallel with WP3; tune with WP4–9 |
| WP11 | Gameplay, sword materials, performance and acceptance | After selected visual components pass |

## WP0 — Reproducible baseline and measurement harness

Worker: Codex builds instrumentation; Claude captures and validates.

Tooling: Existing A/B harness, `tools/vfx-flipbook`, FFmpeg, NumPy, SciPy, Pillow and in-engine deterministic replay.

Codex must first inspect the actual versions and code paths rather than modifying the renderer based on assumptions about three.js.

### Required baseline records

Capture the project commit, renderer version, WebGL extensions, texture formats, render targets, tone mapping, colour space, bloom chain, antialiasing mode, device pixel ratio, output resolution, LOD configuration and asset-serving paths.

Use a fixed replay seed and the following captures:

| Scenario | Main measurement |
| --- | --- |
| Key-1 hit 1, 2 and 3 independently | Impact shape, first-frame core, spark timing |
| Complete Key-1 sequence | Successive-hit readability and residue overlap |
| Metal sword at 60/100/130 px | Mantle identity, blade-keep and tip detail |
| Fire sword stationary and flying | Hot-edge contrast and flame direction |
| Key 7 with 88 swords | Overdraw, LOD, p95 frame-time overhead |
| Major blow | Halo/glint interaction |
| Close-up at 400–500 px | Asset quality, jagged masking and detail |
| Both stone backgrounds | Light/dark contrast |
| 1× and 0.25× | Real-time quality and frame defects |

The normal play host remains instant-cast. Debug overlays may exist in a developer build but must not be required for final acceptance.

### Measurement functions

Blade-keep: Compare the aura-enabled frame against the same aura-off frame in OKLab. The protected blade pixels pass when their difference is ≤0.04.

The required proportions remain ≥90% for lead/mid, ≥85% for far, and ≥95% for jade ring/guard on every frame.

C2 blade overlap: Count effect-generated coverage on actual blade pixels, including the shoulder fan and trails. Require ≤5% in flight.

White-out: Calculate display-referred luminance after the final colour pipeline. For every frame, require the proportion of pixels with luminance ≥0.95 not to exceed 6% of the owner-defined field. Also report the local effect ROI so a small overbright star cannot hide behind a large denominator.

Contrast: Calculate OKLab distance between the final visible sword and a spatially adjacent background sample, with other VFX enabled. Preserve ΔE ≥0.25 for C1.

Performance: Record per-frame CPU/frame-time data over identical A/B replays. Report p95 enabled-minus-disabled deltas, confidence across repeated runs and rolling-window statistics. These are frame-time proxies, not isolated GPU timing.

The supplied M4 environment does not provide the required GPU timer queries. Khronos documents GPU timer queries as extension functionality rather than a universal WebGL2 guarantee.  [Khronos Registry]

Overdraw: Add a development-only counting pass using the same effect geometry, depth tests, clipping and alpha-discard rules. Render a fixed contribution into a diagnostic target for every actual effect fragment with coverage above a defined threshold, initially 0.02. Read back the count inside the projected sword masks.

A suggested implementation is an additive diagnostic buffer with one count unit per visible contribution. The counting pass must preserve depth testing and must not clear/reuse the buffer between individual effects. Validate its counts using synthetic overlapping quads before trusting real sword measurements.

Require ≤2 contributions per pixel in the protected region, including particles or ribbons where they overlap it.

This tests actual transparent overdraw, not draw-call count.

### Performance procedure

The test runs should complete asset preloading and shader warm-up before sampling. Use five interleaved A/B/B/A-style captures as an initial protocol.

Preserve the existing harness's definition of a performance “window.” If it has no recorded definition, implement and report both rolling 60-frame p95 and maximum frame time, without weakening the owner's 11.5 ms ceiling.

The owner budgets are absolute gates, not mere tuning goals.

WP0 deliverable: A baseline JSON/CSV report, deterministic captures and a clear statement of the original state. No VFX package may be called accepted without this reference.

## WP1 — External media, versioning and reliable loading

Worker: Codex implements; Claude manages source assets.

This package was missing from the previous plan and is necessary because the user explicitly requires media never to enter Git, while the normal play host must still load all the selected effects.

### Asset strategy

Keep source videos, generated images, processed masks and runtime atlases in a project-owned asset storage location outside Git. Use a build-time copy/sync procedure or a versioned static-media endpoint already supported by the host.

The repository may contain code, manifest schemas, configuration, asset IDs and hashes, but not generated visual-media binaries.

The loader must:

1. Resolve each asset by a stable manifest ID.
2. Preload the asset before the relevant skill can use it.
3. Verify its dimensions, format, frame count and checksum.
4. Load the correct version in the normal host without URL flags.
5. Report a clear error if media is missing or mismatched.
6. Avoid silently reverting to the rejected lotus or analytic star.
7. Avoid texture upload and shader compilation at the first cast.
8. Retain the exact media version for blind-review reproducibility.

### Manifest contract

```JSON
{
  "id": "key1-fire-brush-v1",
  "assetRevision": "001",
  "assetBase": "configured-external-vfx-root",
  "assetHash": "computed-during-packaging",
  "representation": "oneshot-card",
  "sourceModel": "adobe-firefly-video",
  "sourceFps": 24,
  "sampleFps": 24,
  "frameCount": 16,
  "columns": 4,
  "rows": 4,
  "cellPx": 384,
  "paddingPx": 8,
  "playbackMode": "oneshot",
  "channelLayout": "body-ink-core-persistence",
  "motionAtlas": "motion-atlas",
  "maskAtlas": "authored-mask-atlas",
  "colorSpace": "data-linear",
  "timingProfile": "key1-fire-brush"
}
```

The paths above are logical identifiers, not invented live URLs or actual filenames. Codex maps them to the existing asset-serving architecture.

The manifest must also support rows and variants rather than assuming every atlas uses the existing row-major, single-variant arrangement.

### Gate

Launch the normal host from a clean checkout with the external asset store configured. All effects must preload and render with the correct checksum. Confirm no generated media is tracked by Git.

## WP2 — Single-fragment dark backing and luminous core

Layer: 7, shared by the entire system.
Worker: Codex.
Sources: Existing Metal indigo ink, Fire soot, authored masks.

### Why it is foundational

The old candidates often disappear against `#d6d0c2` because their bright, low-contrast bodies lack a well-designed darker structure.

Simply increasing additive brightness raises white-out and produces cream smears. A separate opaque black backing would also increase overdraw and risk looking like a sticker.

The approved solution is one fragment shader with an authored broken-ink region, an independently controlled coloured body and a small bright core.

### Data contract

Use a static or per-frame authored mask texture:

| Channel | Contents |
| --- | --- |
| R | Designed body coverage |
| G | Broken ink coverage |
| B | Narrow hot-core coverage |
| A | Erosion persistence |

Use a separate motion texture or atlas for Firefly-derived brightness/turbulence.

This separation is essential: the four-channel authored mask cannot also contain arbitrary video motion unless there is an explicitly defined additional texture or frame layout.

Treat masks as data textures, not sRGB colour photographs. Three.js `DataTexture` supports raw typed-array data and defaults to `NoColorSpace`.  [Three.js Docs]

### Core blend contract

Let $a_b$ be coloured-body opacity, $a_i$ the dark-ink opacity, and $E$ the narrow emissive colour.

$$a=a_b+(1-a_b)a_i$$

$$RGB_{\rm premul}=
a_bC_{\rm body}
+(1-a_b)a_iC_{\rm ink}
+E_{\rm core}$$

With RGB blending factors `ONE` and `ONE_MINUS_SRC_ALPHA`:

$$RGB_{\rm result}
=RGB_{\rm premul}+(1-a)RGB_{\rm destination}$$

This is the intended premultiplied-output contract. Core emission is an additive term carried within the same fragment, not ordinary surface colour multiplied by the final alpha.

Use `ShaderMaterial` with custom blending and depth testing. The exact shader and materials must be verified against the installed three.js version. The official material documentation establishes the blend-factor support.  [Three.js Docs +1]

Do not casually change renderer-wide premultiplication settings. Distinguish `Texture.premultiplyAlpha`, `Material.premultipliedAlpha`, the fragment shader's actual output, and the renderer's framebuffer configuration.  [Three.js Docs +2]

### Trial ranges

| Property | Metal | Fire |
| --- | --- | --- |
| Dark backing alpha | 0.35–0.50 | 0.45–0.70 |
| Main body alpha | 0.10–0.35 | 0.25–0.55 |
| Bright body colour ceiling | 0.85–0.90/channel | 0.85–0.90/channel |
| White/hot core share | 1–3% | ≤5% |
| Core thickness | ~1 px | ~1–2 px |
| Backing continuity | Deliberately broken | Deliberately broken |
| Alpha discard start | 0.02 | 0.02 |

These are trial parameters. Measure their final results after tone mapping and postprocessing.

The white/hot core must stay narrow. Its body colour and emissive intensity are separately controlled; it must not turn the whole Fire stroke pale yellow.

### Required calibration tests

Codex creates four synthetic tests before integrating art:

1. A semi-transparent dark ink stroke over light and dark stone.
2. A thin emissive core in front of the ink stroke.
3. Two overlapping transparent effects to check colour and alpha composition.
4. A 1 px line through the actual bloom and AA pipeline.

Compare the single-fragment result against a reference implementation that composites the conceptual ink/body/core layers independently in known order.

Check for unexpected alpha darkening, halo fringes, clipping, missing HDR light and incorrect framebuffer alpha.

Use an HDR render target only after checking its format and blending support. Khronos lists `RGBA16F` as colour-renderable when `EXT_color_buffer_float` is enabled; additional float blending restrictions must be respected for the selected format.  [Khronos Registry +1]

### Colour processing

The authored colour LUT is sampled in linear RGB. Store the LUT with explicit colour-space metadata; do not accidentally apply sRGB decoding to coverage or persistence data.

For a custom `ShaderMaterial`, verify that the actual postprocessing chain performs tone mapping and output conversion once, not zero or twice. Three.js documents the linear working space and the role of `OutputPass`.  [Three.js +1]

### Gate

On both backgrounds, the final effect must retain its soft interior and distinct silhouette without a thick black outline, broad white smear or additional transparent backing pass.

## WP3 — Extract organic motion and repair loop playback

Layer: 8, shared infrastructure.
Workers: Claude for processing, Codex for runtime.

### Starting assets

- `ff-f1-c4`: Fire sheath, 24 retained frames at 12 fps.
- `ff-m1-c4`: Metal mantle, 24 retained frames at 12 fps.
- `ff-f1-c2`: Fire ribbon motion.
- `ff-m1-c3`: Metal streaming qi motion.
- `ff-c3-c3`: Halo only as a failing-loop diagnostic.
- `ff-a1-c5`: Fire impact motion reference.

### Preserve correct temporal metadata

The two 24-frame, 12 fps sheath/mantle samples represent approximately 2 seconds, not 1 second.

If the original 24 fps Firefly videos remain available, start with those. If only the retained atlases remain, record the extracted 12 fps sample rate accurately.

Never play content slower than its original effective motion rate without validated interpolation.

The project's measured 26% error improvement from FFmpeg `minterpolate` justifies testing it for missing intermediate frames, not using it indiscriminately. FFmpeg documents motion-compensated interpolation separately from frame blending.  [FFmpeg]

### Exact runtime modes

| Mode | Used for | Implementation |
| --- | --- | --- |
| `spatial-repeat` | Metal sheath, Fire sheath, silk motion | Authored envelope + scrolling motion data |
| `verified-cycle` | Rare naturally cyclic interior animations | Validated loop, no eight-frame crossfade |
| `oneshot` | Impact motion, glint motion | No wrap |
| `hold-erode` | Ember remnants, designed late state | Persistence-driven erosion |

### How to produce a spatial-repeat motion source

First try the simplest useful route:

1. Select a region from the original Firefly footage containing coherent, directional flame or qi movement.
2. Register the content to a fixed blade-local coordinate system.
3. Extract its internal luminance and structural detail without treating black pixels as perfect alpha.
4. Make one horizontal texture strip periodic in both value and visible feature direction.
5. Make a second independent strip only if it demonstrably improves motion.
6. Sample one or two strips at different speeds/phases inside the authored silhouette.
7. Introduce modest authored-boundary modulation so tongues and filaments are visibly alive.
8. Keep the protective blade corridor and approved mantle outline stable.

Initial scrolling rates: primary 0.8–1.3 cycles/s, secondary 0.35–0.65 cycles/s. These are trial values.

The second strip is not a second render pass. Both samples combine inside the same material.

### Motion-quality gate

A spatially seamless texture is not automatically a good effect.

Claude must verify:

- No obviously repeating motif during ten cycles.
- No static-looking outer feather or flame silhouette.
- No periodic brightness pulse.
- No backward travel inconsistent with sword flight.
- No visible tiling seam.
- The Fire sheath still looks organically alive compared with `ff-f1-c4`.

If two scrolling strips fail after three meaningful iterations, switch to a registered animated-coverage atlas on the same mesh. This preserves the blade-hugging geometry while using selected Firefly frames to modify the actual flame/qi boundary.

Do not fall back to an unprotected full rectangular card.

### Card flipbooks

For impact animations, use true one-shot playback.

A typical selected interior-motion sequence is 12–24 frames at 24 fps. At 60 Hz, sample it at correct timestamps. Avoid arbitrary slowing and uncontrolled adjacent-frame crossfades. If two frames produce double contours, use stepped display or a validated offline intermediate.

### Seam measurement

Calculate a last-to-first difference relative to median ordinary motion difference:

$$R_{\rm seam} =
\frac{D(F_{N-1},F_0)}
{\operatorname{median}_{i=0}^{N-2}D(F_i,F_{i+1})}$$

Proposed target: ≤1.2 for genuine frame cycles, with a separate visual test for direction and repetition.

For periodic texture strips, measure spatial left/right boundary agreement instead. Do not misuse a temporal seam metric for a scrolling texture.

### Atlas contract

Begin with these trial sizes:

| Use | Layout | Atlas size | Approx. RGBA8 memory |
| --- | --- | --- | --- |
| 24 frames, 256 px cells | 6 × 4 | 1536 × 1024 | 6 MiB |
| 16 frames, 384 px cells | 4 × 4 | 1536 × 1536 | 9 MiB |
| 24 frames, 384 px cells | 6 × 4 | 2304 × 1536 | 13.5 MiB |
| 24 frames, 512 px cells | 6 × 4 | 3072 × 2048 | 24 MiB |

These numbers exclude mipmaps, extra mask/motion textures, GPU overhead and retained source buffers.

Each cell size includes its padding. With 384 px cells and an 8 px inset on every side, the usable source region is 368 × 368 px.

Prefer controlled mipmaps and cell-bounded UVs. Do not let adjacent atlas frames bleed together at minified scale. Three.js documents filtering, wrapping and mipmap behaviour on textures.  [Three.js Docs]

Start with 256 px cells for ordinary play. Test 384 px for close-ups. Promote to 512 only if it visibly improves the 400–500 px capture and stays within resource budgets.

### Gate

The selected assets maintain organic motion at 1×, have no ghosts at the seam, and do not expose temporal jumps at 0.25×. The full motion pipeline must use correct source-rate metadata.

## WP4 — Key-1 Fire impact: Brushfire Calligraphy

Layer: 4, including burst and decay interaction.
Priority: Highest artistic replacement.

Starting assets: Ticket 252 v1 and v3. Use `ff-a1-c5` for its soft fire movement only.

Workers: ChatGPT/Gemini edit the artwork; Firefly Video supplies movement; Claude prepares/analyses the media; Codex integrates.

### Diagnosis

`ff-a1-c5` scored 6.5/6.5 because its 300° circular shape does not communicate three sword cuts. The strokes have only a 0.81 thickness ratio, lack the required white-gold leading line, and disappear too quickly.

Its organic movement remains useful. The shape and temporal presentation are the rejected parts.

### Source-art selection

Stage 1 uses only Ticket 252 v1/v3.

Choose the best two eligible designs after checking:

| Criterion | Gate |
| --- | --- |
| Main strokes | Exactly 3 distinguishable crescents |
| Individual arc | 120–180° |
| Thickness ratio | ≥3:1 between 20% and 80% of centreline |
| Secondary marks | 4–5 small counter-strokes, plus a few detached tongues |
| Overall shape | Open fan; not ring, lotus or letter C |
| Hot-core area | ≤5% |
| Leading hot line | Attached to appropriate outer edges |
| Margins | No tip or tongue cropped |
| Strike origin | Stable and identified in image coordinates |

An image model may generate a visually convincing taper without meeting the numeric requirement. Measure it from a cleaned binary/soft mask; do not rely solely on visual inspection.

### Designed first and last frames

For each approved first frame:

1. Produce a registered 1080 × 1080 opaque-black master.
2. Preserve the approved open-fan geometry.
3. Edit the same image into an ember last frame.
4. Keep 15–35% of the original bright area.
5. Require at least 70% of surviving bright pixels to overlap the original stroke mask.
6. Keep the main stroke roots recognizable.
7. Retain identical framing, scale and strike origin.

The pilot's first and last frames are design constraints, not a promise that Firefly will preserve every curve between them.

### Firefly Video

Use the Adobe Firefly Video model, black-background 1080p square mode, 24 fps, 5 seconds, first and last images.

With both keyframes supplied, camera-motion controls are unavailable; use the static-view instruction in the prompt. Adobe documents that behaviour.  [Firefly]

Run two variations per approved first/last pair, maximum four initial videos.

### Processing

Claude inspects the complete video before selecting motion.

The production pipeline should:

1. Identify the useful 12–24-frame organic-motion interval.
2. Stabilize the three stroke roots and outer silhouette.
3. Produce an animated interior-motion texture or atlas.
4. Preserve the authored crescent coverage as the primary form.
5. Build separately controlled hot-edge and ink masks.
6. Generate/paint a persistence field for the three different strokes.
7. Register the last-frame ember mask to the initial design.
8. Reject topology-changing video segments.

Black-background matte handling: Brightness does not uniquely identify alpha. Use the authored mask to define maximum coverage, then extract relative motion from the video. Where source RGB was composited against black, recover plausible colour/alpha only within the reliable authored matte, correcting edge colours manually when necessary.

Do not divide tiny RGB values by near-zero estimated alpha; that can create white or orange edge speckles.

### Runtime representation

Use a one-shot card with the authored shape and Firefly-driven movement.

The impact card must be anchored at the target contact point and oriented so that its intended up-right sweep corresponds to the projected sword-cut direction in the real camera.

Placement test: Compare a camera-facing impact plane against a ground-aligned effect plane at the 55° camera. The three crescents must remain open at play size and not clip through the target or environment. Select the representation that preserves the approved screen-space design while respecting appropriate depth occlusion.

Ground scorch and cracks are not part of this card. Keep the rejected procedural decals disabled; only a separately approved painted decal may be introduced.

### Proposed Key-1 temporal profile

| Age after contact | Phase | Visual behaviour |
| --- | --- | --- |
| 0 ticks | Contact | Flash and hot core appear at ≥95% of their respective peak brightness |
| 0–3 ticks | Reveal | Three completed source strokes become spatially visible from the cut direction |
| 3–6 ticks | Hold | Readably complete silhouette; organic fire moves inside |
| 6–19 ticks | Main erosion | Tips break, islands detach, roots remain; brightness comes from surviving local cores |
| 19–40 ticks | Ember residue | Sparse red-hot remnants only, not a full fan |

At age 18 ticks, corresponding to the next contact's arrival after the first hit, propose ≤15% of peak bright-body coverage remaining from the previous impact. The sparse ember residue may continue.

That 15% is a tuning target for avoiding overlap, not a new owner-approved global threshold.

The main erosion lasts about four times the three-tick reveal; the quieter residue lasts longer. This preserves fast attack and slow decay without obscuring the next hit.

### Gate and capture

Test each hit at 70, 110 and 160 px, then the full three-hit sequence.

Measure shape, taper, core percentage, the first-frame flash/core, bright-body coverage over time, overlap with the following hit, stone contrast, white-out and frame-time overhead.

Blind judges review body-only A/B against `ff-a1-c5`, then full impact with stars and sparks. Do not accept a weak core body just because the combined particle system looks busy.

Method-change trigger: After three unsuccessful Firefly motion attempts, retain the best painted crescent shape and animate its interior with the existing flame source and runtime erosion. Do not return to the lotus.

## WP5 — Metal Wind-Silk Mantle

Layer: 1.
Starting assets: `ff-m1-c4` and `ff-m1-c3`.

Workers: ChatGPT/Gemini for revised masks, Claude for existing-video extraction and judging, Codex for mesh integration. Firefly Video is only used for additional organic movement if the existing source is insufficient.

### Diagnosis

The current mantle reads as a nearly solid silver feather or fern. Its internal veins cannot rescue the silhouette when scaled to a 60 px sword.

The mantle must become a tailored presence field outside the real blade.

### Required structure

The approved A design consists of:

- Two asymmetric qi seams outside the steel.
- Discontinuous feather-like plate suggestions, not one filled feather.
- A clear central blade corridor and 1 px final projected ink gap.
- One open collar around the jade-ring guard.
- Two seams converging into a needle beyond the tip.
- One trailing silk tail.
- Small moving silver-blue filaments.
- Restrained micro-glints that sparkle without forming another aura direction.

### Geometry

Create a blade-local surface or narrow strip geometry that follows the real sword's dimensions. Preserve separate material/UV zones for the two external seams.

At runtime, calculate screen projection for the lead sword to verify that the corridor remains open after scaling, rotation and AA. The actual gap must be measured in output pixels.

Do not use a fixed 1 px border in a 1024 px master texture and assume it will survive projection.

Use batched instancing for swords sharing the same mantle geometry/material. Three.js documents `InstancedMesh` and its reduction of draw-call overhead for shared geometry.  [Three.js Docs]

### Motion architecture

The authored mask establishes the outer design.

Firefly motion provides internal flow, with limited variation along the feather fragments and silk seams. If scrolling movement makes the silhouette static, use the WP3 animated-coverage fallback.

The main body must have more than periodic brightness changes; at least some small filament and plate edges should move visibly without breaking the sword's protective corridor.

### Trial values

| Parameter | Starting range |
| --- | --- |
| Source mask master | 1024 × 256 |
| Runtime mask | 512 × 128 or 1024 × 128 |
| Motion source | Reprocessed `ff-m1-c4` / `ff-m1-c3` first |
| Flow speed | 0.6–1.2 cycles/s |
| Envelope variation | 2–5% outside protected corridor |
| Body alpha | 0.10–0.35 |
| Indigo backing alpha | 0.35–0.50 |
| Main bright detail | Thin filaments, approximately 1 px at play |
| White filled region | Minimized; initial target ≤2% mantle ROI |
| Needle extension | 3–7 px at a 100 px sword, subject to readability |
| Sword envelope negative space | Initial design target ≥60% |

The silhouette must remain luxurious and legible. Negative-space percentages are diagnostic aids, not a substitute for judge scores.

### LOD

For key 7:

- Six lead swords: full mantle.
- Mid swords: simplified seams and fewer plates.
- Far swords: a broken qi rim and needle incorporated into the existing impostor material.

Do not draw a separate full mantle card on every far sword.

### Gate

At 60 px, the mantle must still read as two external qi seams and a needle. At 130 px, it must show tailored detail rather than a solid feather.

Pass blade-keep, jade-ring keep, the projected gap test and key-7 frame-time measurement.

Blind judges review the actual sword in stationary, departure, flight and contact contexts on both grounds.

## WP6 — Fire sheath around the blade

Layer: 2.
Starting asset: `ff-f1-c4`, with `ff-f1-c2` as a trailing-ribbon motion reference.

### Diagnosis

The existing 7/7 flame has a desirable soft, organic quality. It fails as a finished sheath because of symmetry, the hilt blob, travel-direction mismatch and light-stone washout.

The correct route is to preserve its motion while replacing the envelope.

### Authored exterior

Use one asymmetric sheath mask with:

- A completely open steel corridor.
- Unequal upper and lower tongues.
- Longer tongues trailing backward relative to flight.
- No filled arrowhead at the hilt.
- Thin hot edging outside the steel.
- Small fast licks among larger slower curls.
- A fine tip continuation.
- An open guard/jade-ring region.

An initial 65:35 upper/lower silhouette balance is a design trial, not a fixed symmetry rule.

### Runtime

Use the WP5 blade-hugging mesh architecture with Fire-specific mask, motion and LUT.

The Fire presentation should not stack the complete Metal mantle and the complete Fire sheath as separate full-coverage effects.

A Fire-specific material kit may reuse the same tailored geometry while replacing the appearance.

### Trial values

| Feature | Proposed |
| --- | --- |
| Runtime motion | Existing source at correct rate, then periodic or registered motion |
| Main strip | 512 × 128 |
| Optional second detail strip | 512 × 128 |
| Texture flow | 0.8–1.5 cycles/s, adjusted smoothly with sword velocity |
| Main body alpha | 0.25–0.55 |
| Soot backing alpha | 0.45–0.70 |
| Hot edge | 1–2 px at play camera |
| External flame extent | 6–12 px at 100 px sword length |
| Full flame-tongue tier | Existing maximum 14 swords/frame |
| Mid/far tiers | Ember mantle / broken rim |

The most important moving visual is the backward-sweeping flame. Increasing sprite brightness is not an acceptable substitute for that shape.

### Blade protection

A local exclusion corridor is applied to body, ink and emissive masks.

The card/mesh must not paint the dark steel. The hot steel edges belong to the actual blade material or its already-approved treatment.

Use one transparent mantle/sheath contribution and keep additional ribbon coverage away from the protected blade.

### Gate

At normal play size, judges should see dark steel with fire licking around it—not a glowing cream sword or an arrow-shaped flame object.

Test idle, acceleration, full flight, slowing, light stone, dark stone and close-up. Apply C1/C2 on the final composited frame.

## WP7 — Tip star, secondary glints and sparkle hierarchy

Layer: 3, also supplying the small decorative glints that make the other shapes feel alive.

Source: `ff-g1-c2` is a motion/shape reference, not a final atlas. Reject the unstable swelling peak.

Workers: ChatGPT/Gemini paint masks; Codex animates sprites; Claude evaluates.

### Main tip-star design

Use a deliberately irregular four-point star:

- Two stronger tapered arms.
- Two shorter and finer arms.
- Very small white-gold centre.
- Optional weak diagonal detail only at larger sizes.
- Soft peripheral accent without a stock lens-like halo.

At 12 px, the four-arm silhouette must be recognizable. An eight-arm design is not required at that scale.

### Runtime

Use painted sprite masks in a GPU-instanced system.

Trial timing:

| Age | Behaviour |
| --- | --- |
| 0 | Tiny sharp hot centre already ≥95% peak |
| 1–3 ticks | Main arms extend and briefly dominate |
| 3–6 ticks | Smallest arms start disappearing |
| 6–12 ticks | Main arms retract/erode |
| After 12 | No persistent full-sized star |

The bright flash is short, while a subtle afterimage may be longer.

### Display-size detail

| Projected diameter | Detail |
| --- | --- |
| 12–16 px | Four principal arms, tiny nucleus |
| 17–24 px | Stronger taper and a faint outer glint |
| 25–32 px | Optional weak diagonal detail |

Limit the hot-white centre to an initial proposed ≤4% of the star's defined ROI. Track centroid stability; a jump of about 1 px at a 24 px sprite is a useful defect threshold.

### Sparkle allocation

The owner requires every shape to sparkle, but not every pixel to compete for attention.

Use this hierarchy:

| Shape/event | Sparkle design |
| --- | --- |
| Metal mantle | Sparse micro-highlights sliding along authored seams |
| Fire sheath | Occasional tiny hot points on flame tips |
| Sword tip | One main Starfire glint |
| Ordinary Key-1 impact | Main hot edge, a brief large glint and two smaller staggered glints, plus sparks |
| Key-7 ordinary distant swords | Internal rim shimmer, not individual large stars |
| Major blow / ultimate | Strong three-star sequence and the approved Halo Seal |
| Ember aftermath | Small intermittent flecks, no persistent glitter cloud |

These highlights must be staggered. Their maximum simultaneously visible brightness is constrained by the same global white-out gate.

No additional full C-direction aura is created around the swords.

### Gate

At 12, 24 and 32 px, the glint must look sharp and crafted rather than like a white dot or clip-art icon.

Both judges evaluate the tip with the real sword, not as an isolated enlarged star.

## WP8 — Starfire Jewel sparks and gold-dust aftermath

Layer: 5.
Sources: Use `ff-b2-c1`, `ff-b2-c2` and `ff-b3-c3` only as negative references.

Workers: ChatGPT/Gemini make sprite artwork; Codex implements deterministic GPU particles; Claude validates.

### Art

Create three spark length families:

- Short, sharp white-gold heads with small orange tails.
- Medium tapered streaks.
- Long, elegant needle streaks with curved cooling trails.

Gold dust is a separate, much smaller and sparser sprite family.

### Runtime data

For each spark, store:

| Attribute | Purpose |
| --- | --- |
| Launch position | Initial world-space origin |
| Launch tick | Deterministic synchronization |
| Initial velocity | Direction and speed |
| Gravity vector | Ground-plane movement |
| Lifetime | Individual survival |
| Sprite variant | Short/medium/long |
| Initial size | Screen-clamped appearance |
| Cooling phase | White-gold to red-dark |
| Bounce configuration | Whether this spark collides once |
| Seed | Stable variation |

The particle position before collision is:

$$\mathbf p(t)=\mathbf p_0+\mathbf v_0t+\tfrac12\mathbf g t^2$$

For the approved occasional bounce, calculate the first intersection with the actual ground plane. At collision, apply a reduced reflected normal velocity and continue movement. A second bounce is not allowed.

The CPU schedules the small number of emissions and, when useful, calculates the contact tick. The vertex shader calculates visual particle position, stretch and orientation each frame. This avoids per-frame CPU transformation of every spark.

### Trial parameters

| Property | Initial value |
| --- | --- |
| Sparks per Key-1 hit | 10–18 |
| Directional clumps | 2–3 |
| Short length | 4–7 px |
| Medium length | 9–15 px |
| Long length | 16–25 px |
| Launch spread | Approximately ±10–25° about the cut tangent |
| Lifetime | 0.15–0.45 s |
| Once-bouncing share | 10–20% |
| Bounce restitution | 0.25–0.40 |
| Dust after a hit | 4–10 small flecks |
| Dust lifetime | 0.35–0.80 s |

Lengths are projected screen lengths at the reference play camera, not fixed world-space dimensions.

A screen-size clamp must retain the short/medium/long hierarchy when the camera moves closer. Do not enlarge every spark to the same minimum size.

### Gate

The sparks must move in coherent, mostly curved paths along the hit direction. They must not resemble a grinder, firework, bokeh shower or stock glitter.

Judge the impact with sparks disabled and enabled. Require a stronger hit impression without obscuring the three main crescents.

## WP9 — Halo Seal for major blows

Layer: 6.
Source: `ff-c3-c3` only for limited highlight-motion reference.

Workers: ChatGPT/Gemini design the seal; Codex prepares its mask/SDF and runtime; Claude judges.

### Design

Create a recognizable engraved sword-school seal with:

- One thin outer ring with deliberate breaks.
- One partial secondary arc.
- Distinct carved sword/cloud/flame motifs.
- Large negative-space regions.
- A few moving star points.
- No generic multiple-ring magic circle.

At the 100 px target, the seal must not merge into a thick bangle.

### Asset conversion

Start with a clean, high-resolution alpha mask and test it directly.

If a distance field improves quality:

- For a regular SDF, derive signed distance from the cleaned raster using a distance transform.
- For MSDF, trace the design into valid vector contours, repair path intersections/corners and then process it with `msdfgen`.

Do not feed a bitmap directly into `msdfgen` while assuming it will infer accurate vector geometry.

The maker explains the sharp-corner benefits of multi-channel signed-distance fields; the method does not guarantee that a 1 px luminous ring will outperform ordinary alpha.  [GitHub]

### Runtime

Use one seal representation. Animate visibility along the authored paths and move small glints along those paths.

The engraving itself stays stable and is not generated by analytic concentric-circle shaders.

Trial parameters:

| Setting | Starting value |
| --- | --- |
| Master image | 1024 × 1024 |
| Runtime asset | 256–512 px |
| Projected diameter | 90–140 px for a big blow |
| Line width | Approximately 1–1.5 px at play camera |
| Reveal | 6–10 ticks |
| Hold | 6–10 ticks |
| Erosion | 18–30 ticks |
| Broken ink alpha | 0.35–0.50 |

These values apply only when a Halo Seal is appropriate.

### Activation policy

Activate only for approved big events: a major cast, Key-7 lead-sword dive, finisher or ultimate.

Do not use the Halo Seal on every ordinary Key-1 hit.

### Gate

At play size, the seal must remain distinct from a bangle, have no stray `+` bars or loop seam, and read as a crafted engraved design on both stones.

## WP10 — Immediate flash, spatial burst and slow erosion

Layers: 9 and 10.

Worker: Codex implements the shared scheduler; Claude verifies envelopes.

### Source

Reuse the existing `FlipbookPool` erosion/cooling and `slowFrom/slowRate` infrastructure where suitable.

Do not rewrite a functioning system unnecessarily. Extend the manifest and timeline only where the current code cannot express the approved profiles.

### Runtime timing contract

```TypeScript
type VfxPhase = {
  preContactTicks: number;
  revealTicks: number;
  holdTicks: number;
  erosionTicks: number;
  residueTicks: number;
  sourceFps: number;
  sampleFps: number;
  playbackMode:
    | "spatial-repeat"
    | "verified-cycle"
    | "oneshot"
    | "hold-erode";
  erosionProfile:
    | "tips-first"
    | "stroke-islands"
    | "edge-breakup";
};

type VfxEvent = {
  castId: string;
  swordId: number;
  targetId: string;
  contactTick: number;
  deterministicSeed: number;
  profileId: string;
};
```

The actual visual age comes from the skill's canonical event tick, not an independent unsynchronized animation clock.

### First-frame brightness

Use the original requirement exactly:

At the first rendered contact frame, the flash and hot core are already ≥95% of their respective peak brightness.

The authored large shape may have a directional spatial reveal over subsequent ticks.

This avoids the rejected impression of a completed static source shape suddenly pasted into the scene, while preserving immediate contact energy.

Measure peak brightness within the registered flash/core masks, rather than comparing the total number of bright pixels in the entire impact.

Also record total effect brightness and area as diagnostics, but do not replace the fixed flash/core gate with those values.

### Erosion

Prepare a persistence field $P(x,y)$ from the authored stroke design.

Tips, detached licks and selected outer fragments receive lower persistence. Main roots receive higher persistence.

During erosion:

$$S(x,y,t)=
\operatorname{smoothstep}
\left(e(t),e(t)+w,P(x,y)\right)$$

Use a proposed normalized transition width $w=0.06\text{–}0.12$.

The body, ink and hot line should have coordinated but not identical decay. The bright edge can remain on surviving islands, yet vanish immediately once its local fragment erodes.

For colour steps, remap the surviving persistence interval:

$$r=\operatorname{clamp}
\left(\frac{P-e}{\max(1-e,\epsilon)},0,1\right).$$

This prevents the remaining islands from becoming uniformly dull before disappearing.

The final visual should look like separate strokes tearing apart and cooling, not one image undergoing a global alpha fade.

### Per-family initial profiles

| Effect | Immediate attack/reveal | Hold | Slow breakup |
| --- | --- | --- | --- |
| Key-1 crescents | 0–3 ticks | 3–6 ticks | Main 6–19; ember 19–40 |
| Tip star | Hot point at age 0; arms 1–3 | 3–6 ticks | 6–12 |
| Major-hit glint | Hot point at age 0 | 3–7 ticks | 7–15 |
| Halo Seal | 6–10 tick engraved reveal | 6–10 additional ticks | 18–30 |
| Metal mantle entrance | 3–6 ticks | Continuous living presence | 9–18 on dismissal |
| Fire sheath entrance | 3–6 ticks | Continuous living presence | 10–21 on dismissal |

The Key-1 profile must be judged with the next hit only 18 ticks later. Adjust its bright-body coverage first, preserving the longer quiet ember tail wherever it remains readable.

### Gate

No quick global fade, no full-intensity crescent fan remaining when the next sword contacts, no frozen static flame during a long hold, and no source-clip wrap at the end.

## WP11 — Final gameplay integration, material correction and acceptance

Worker: Codex implements; Claude validates the complete host and coordinates blind judging.

### Key-1 gameplay schedule

The approved hit timings are preserved.

| Sword | Contact tick | Time at 60 Hz | Required movement |
| --- | --- | --- | --- |
| First | +18 | 0.30 s | Point at the target, visibly hold, then fly |
| Second | +36 | 0.60 s | Depart approximately +18 to +21; slow near target |
| Third | +66 | 1.10 s | Depart approximately +48 to +51; slow near target |

For the first sword, use ticks 0–5 as an initial pointing-hold trial, with flight during ticks 6–17. Tune the path while keeping the contact at +18.

The established T4 requirement remains: every lead sword must have at least 12 frames between appearance and impact during which it is ≥40 px long and moves ≤12 px/frame.

For the second and third swords, the final 8–10 frames must also meet the ≤12 px/frame slowdown.

Codex must update canon data, skill content, deterministic timelines and golden hashes intentionally. No artificial typing delay is added.

### Jade-ring correction

Use the approved image as the material reference, but apply the repaint to the actual sword asset.

Inspect the guard's mesh and UV allocation. Set the white-jade body as a non-metallic material and the narrow pale-gold rim as an appropriately metallic component, while retaining all original geometry.

Three.js `MeshStandardMaterial` exposes distinct metalness and roughness controls; the actual values must be tuned under game lighting rather than copied blindly from an illustration.  [Three.js Docs]

Test the ring on light and dark stone at 60/100/130 px. It must read as white jade rather than chrome, while the three small jade details and carved guard remain identifiable.

### C1 final contrast

Maintain the owner's two named requirements:

$$\Delta E_{\rm OKLab}\geq0.25$$

and

$$C_{\rm Weber}\geq2.$$

The Weber metric needs explicit sign/reference reporting. For conventional Weber contrast:

$$C_W=\frac{L_{\rm object}-L_{\rm background}}{L_{\rm background}}.$$

A dark blade against light stone has negative Weber contrast, and its absolute magnitude cannot exceed 1 when luminances are nonnegative.

To preserve the owner's intended strong dark-blade visibility without silently altering the target, the harness should output the conventional signed result and the alternative dark-reference ratio:

$$C_{\rm darkRef}
=\frac{L_{\rm light}-L_{\rm dark}}
{\max(L_{\rm dark},\epsilon)}.$$

The latter can reach 2, but it is not identical to conventional blade-against-background Weber contrast.

Do not declare C1 passed by renaming the second formula Weber. Retain the owner's number, provide both measurements, and flag the interpretation only if the original implementation does not already define it. No art-direction decision needs to be reopened.

### High-setting antialiasing

Test FXAA and SMAA with the actual renderer/postprocessing stack.

Three.js specifies that SMAA works in linear-sRGB before `OutputPass`, while an sRGB-dependent pass such as FXAA follows `OutputPass`.  [Three.js Docs +1]

Choose whichever preserves the narrow qi seams, thin stars, hot blade edges and 1 px gaps within budget.

### Explicit legacy-effect retirement

Disable the following on the production Key-1/Metal/Fire paths when the new components are integrated:

- Rejected symmetric lotus flipbook.
- Analytic four-point tip-star drawer.
- Old spark-ray atlas and generic analytic ember dots where replaced.
- Old analytic ground seal.
- Procedural scorch and code-drawn crack marks.
- Obsolete full-card aura rendering that duplicates the new blade-hugging representation.

Do not delete source assets before verifying the new package. But do not allow rejected layers to render invisibly under the replacements.

### Key-7 performance allocation

Use the following as an initial profiling allocation, not as a claim of measured individual GPU cost.

| Effect family | Trial incremental frame-time allocation |
| --- | --- |
| Metal mantle/ribbon | 0.45 ms |
| Metal tip glints | 0.08 ms |
| Shared Metal material/management reserve | 0.07 ms |
| Metal total | ≤0.60 ms |
| Additional Fire sheath work | 0.50 ms |
| Fire sparks and dust | 0.16 ms |
| Major-event seal, when active | 0.11 ms |
| Fire reserve | 0.08 ms |
| Fire increment over Metal | ≤0.85 ms |

Individual enabled-minus-disabled p95 differences are not necessarily additive. Measure each layer separately and the real combined configuration. The combined configuration is authoritative.

### Final acceptance

The candidate is accepted only after all technical gates pass and both independent judges assign at least 8.5 in the normal built play host.

# 4. New artwork and complete prompts

The production prompts below are ready for the assigned image or video worker. All Firefly Video prompts are below 600 characters and avoid prohibited names and terms.

## 4.1 Generation allocation and sequence

| Asset | Initial candidates | Generation sequence |
| --- | --- | --- |
| Metal silhouette | 2 images | Generate, measure, approve |
| Metal organic motion | 0–2 new videos | Reuse existing video first |
| Fire sheath silhouette | 2 images | Generate, measure, approve |
| Fire organic motion | 0–2 new videos | Reuse `ff-f1-c4` first |
| Impact first-frame design | 2 selected/edited images | Start from Ticket 252 v1/v3 |
| Impact registered last frames | 2 edits | After first-frame approval |
| Impact Firefly motion | Up to 4 videos | Two runs per approved image pair |
| Tip-star masks | 3 images | No video initially |
| Spark sprites | 2 images | No video |
| Gold dust | 1 image | No video |
| Halo Seal | 2 images | No video |
| Jade repaint | 1 image edit | Use approved project reference |

Maximum allocation: 17 image candidates/edits and eight new Firefly video runs. Actual spending should be lower when salvage succeeds.

Do not begin Firefly Video generation until the relevant source artwork passes its shape gate.

## 4.2 Metal silhouette — image prompt

> [Writing] Create one premium xianxia Wind-Silk Mantle mask for a straight flying sword, without drawing the sword. Wide horizontal composition, pure black background, tip pointing right, generous 10% safe margins. Two asymmetric tailored seams lie outside a wide empty blade corridor. Fine silver-white silk filaments, broken feather-like qi plates and delicate etched threads create a luxurious flowing presence. Keep much of the envelope black and open. Preserve a clear guard collar, one trailing silk tail and two seams meeting in a fine needle beyond the tip. Hand-painted anime/donghua mask artwork, grayscale only. No solid feather, fern, smoke, scenery, labels or thick glow.

Generate one sharper angular-plate version and one softer silk-filament version. Both are subdivisions of the approved Wind-Silk Mantle direction A.

## 4.3 Metal motion — Firefly Video

> [Writing] On pure black, a thin horizontal band of silver-white sword qi. Two separated flowing silk seams, tiny broken feather-like fragments and blue-silver filaments move steadily toward the right; the outer silhouette stays narrow and open, with a fine needle at the tip. Motion is delicate and continuous inside broad negative-space gaps. Hand-painted anime/donghua energy, fixed viewpoint. No sword, solid fern, smoke, explosions, text or scenery.

443 characters. Maximum two runs if existing motion cannot be salvaged.Use the motion as texture data constrained by the approved mask, not as an independent full-card aura.

## 4.4 Fire sheath — image prompt

> [Writing] Paint a premium asymmetric Fire sheath mask for a straight flying sword, without drawing the sword. Wide horizontal image on pure black, tip to the right, generous safe margins. The central steel corridor stays completely black and open. Unequal upper and lower orange-red flame tongues lick outside the blade and sweep backward toward the left. Mix long soft curls with tiny sharp detached licks. Keep the hilt nearly empty and the guard fully open. End in a fine pointed flame needle beyond the tip. Designed hand-painted anime/donghua fire with rich taper, thin hot-edge accents and dark negative space. No arrowhead blob, fireball, smoke, ring, scenery or text.

Generate two candidates: one long sweeping design and one shorter layered design.

## 4.5 Fire sheath motion — Firefly Video

> [Writing] On pure black, a narrow sheath of living orange-red fire around an invisible straight blade, tip right. Unequal flame tongues lick backward toward the left; fine fast licks move inside larger soft curling forms. The centre and hilt remain dark and open. Keep a slender pointed tip and crisp small accents, with soft flame motion. Hand-painted anime/donghua style, fixed viewpoint. No sword, arrowhead blob, smoke cloud, fireball, ring, text or scenery.

452 characters. Run only if processing ff-f1-c4 fails the motion-quality test.
## 4.6 Key-1 impact — first-frame image A

> [Writing] Create one premium xianxia Fire sword-impact first frame on an opaque pure-black 1080×1080 square. Three unequal OPEN flame-brush crescents rise diagonally from a lower-left strike point toward the upper right. Each curves 120–180 degrees and tapers from a heavy expressive root to a needle tip, with thickness ratio at least 3:1 between 20% and 80% along its centreline. Add four or five small counter-strokes and a few detached licks. The three main strokes form an open fan, never a circle or C. Use rich orange-red flame, a very thin white-gold leading edge occupying no more than 5% of the bright shape, and broken dark ink beneath. Elegant, luxurious hand-painted anime/donghua design, safe margins. No sword, lotus, smoke, scenery or text.

This is the Ticket 252 v1 direction.

## 4.7 Key-1 impact — first-frame image B

> [Writing] Create one premium xianxia Fire sword-impact first frame on opaque pure black, 1080×1080 square. Two long asymmetrical flame-brush crescents sweep diagonally up-right from a lower-left strike point. A shorter distinct third counter-stroke completes the OPEN three-stroke composition. No circle or C. Each stroke has a strong root and a razor-fine tapered tip, thickness ratio at least 3:1. Add four or five smaller counter-flicks and a few detached flame tongues. Rich orange-red living flame, thin white-gold leading edges covering at most 5% of the luminous shape, broken dark underlay, premium elegant hand-painted anime/donghua styling. Leave broad black gaps and safe margins. No sword, lotus, smoke, scenery or text.

This is the Ticket 252 v3 direction.

Use existing pilot artwork before creating a fresh replacement. The prompts are available for correction or controlled re-creation, not justification to restart the stopped pilot unnecessarily.

## 4.8 Registered late-ember frame — image EDIT prompt

> [Writing] EDIT the supplied approved first frame. Preserve the exact 1080×1080 canvas, black background, strike origin, three stroke paths, geometry, framing and directions. Turn the SAME strokes into their late ember state: thin broken red-orange lines, dark fragments and a few tiny pale-gold hot points. Remaining bright area must be 15–35% of the original. At least 70% of the remaining bright pixels must lie inside the original stroke mask. Let fine tips fragment first and keep the heavy roots identifiable. Do not move or redraw the composition. No new arcs, lotus, stars, smoke, scenery or text.

Run separately against each approved first frame, with image-edit mode and the first frame supplied as the source.

## 4.9 Key-1 organic motion — Firefly Video

> [Writing] Animate the supplied first and last frames as the same three open, tapered flame-brush crescents. Warm orange-red living fire runs along their curves from heavy roots to fine tips; small detached tongues flutter and thin white-gold leading edges shimmer. Gradually break the existing strokes into the matching ember remnants. Preserve the three separate paths, strike origin, open fan and framing. Pure black, fixed viewpoint. No new arcs, lotus, circles, smoke, text or scenery.

479 characters. Up to four runs, two per approved first/last pair.Settings: Adobe Firefly Video, 1080p square black-background workflow, 24 fps, 5 seconds, first and last images. Transparent-background mode disabled.

Do not use the Topaz video upscaler. Only image upscaling through allowed image tools may be considered if a close-up master genuinely needs more resolution, with mask registration revalidated afterward.

## 4.10 Tip-star sprite sheet

> [Writing] Create a clean hand-painted sprite sheet on pure black showing three variations of the same premium white-gold four-point sword glint. Each has two long razor-tapered arms, two shorter delicate arms, a tiny bright core and a faint asymmetrical peripheral shimmer. Keep all sprites separated with large black margins, stable centres and clearly distinct contours. Design for 12–32 pixel gameplay size, with beautiful fine anime/donghua energy and no solid white nucleus. No six-point icon, square blob, double star, glitter cloud, smoke, lens effect, sword, scenery or text.

Generate three related designs. Choose by the 12 px output first, not the 500 px enlarged appearance.

## 4.11 Spark sprite sheet

> [Writing] Create one premium xianxia Fire spark sprite sheet on pure black. Show isolated short, medium and long tapered spark shapes with generous margins. Each has a tiny intense white-gold head, slender orange-amber body and a fine cooling dark-red tail. Use subtle irregular curvature and three clearly distinct lengths. Crafted, sharp, elegant hand-painted anime/donghua VFX art suitable for GPU-instanced particles. Keep each sprite separate; no overlap. No fireworks, full radial sprays, zigzags, equal-length rods, glitter, bokeh, smoke, scenery or text.

Two candidates, one with straighter narrow heads and one with slightly curved flowing tails.

## 4.12 Gold-dust sheet

> [Writing] Create a sparse premium ember-dust sprite sheet on pure black. Tiny individually separated irregular gold flecks, red-orange embers, micro-streaks and a few miniature four-point glimmers. Every mark is crafted, sharp and different, with generous empty black spacing. Designed for a subtle magical sword-impact aftermath at gameplay size. No large stars, round light discs, stock glitter, bokeh, coins, haze, scenery or text.

One candidate initially.

## 4.13 Halo Seal

> [Writing] Design one refined xianxia sword-school Halo Seal as thin precise white artwork on a pure-black square. One broken circular outer ring, one sparse partial inner arc, generous gaps and a few original engraved motifs inspired by sword, cloud and flame geometry. Keep the artwork circular when face-on, with distinct quadrants and beautiful negative space. Every feature must remain recognizable at 100 pixels. Clean contours suitable for high-resolution alpha or vector tracing. No thick bangle, repeated equivalent rings, invented written characters, generic magic circle, bright haze, stars, scenery or labels.

Generate two different engraved arrangements, not different colour versions.

## 4.14 Jade-ring material reference edit

> [Writing] EDIT the supplied project sword image using its approved reference. Change ONLY the existing hollow guard ring from chrome-silver to polished white jade with a very thin pale-antique-gold rim. Keep the precise ring opening, white-jade form, three small green-jade details, cloud carving, blade, guard, grip and lotus pommel. Preserve camera angle, lighting, framing, proportions, colour palette and anime/donghua material style. The ring must look like premium white stone, not luminous plastic or reflective chrome. No changes to any other object or background.

The edited reference guides the actual 3D material or UV repaint. It must not be pasted onto the running game as a flat image.

# 5. Package-level measurement and judging matrix

Each work package needs a measurable result and an independent visual evaluation.

| Package | Principal automated checks | Judge capture |
| --- | --- | --- |
| WP0 baseline | Determinism, renderer metadata, reference pixel measurements | Existing 6.5–7 candidates reproduced |
| WP1 asset delivery | Hash, dimensions, frame count, preload, missing-asset behaviour | Normal host with all external media |
| WP2 compositor | Alpha math, colour-space calibration, ≤6% white-out, overdraw | Existing fire effect with old/new backing on both stones |
| WP3 loops | Seam ratio ≤1.2 trial, no adjacent-cell bleed, correct temporal rate | Ten-loop video at 1× and 0.25× |
| WP4 impact | Three strokes, ≥3:1 taper, ≤5% hot core, bright coverage before next hit | Each Key-1 hit and all three together |
| WP5 Metal mantle | Blade-keep, ≥1 px final gap, ≤2 layers, performance | Lead/mid/far swords at play and close |
| WP6 Fire sheath | Blade-keep, C1/C2, correct trailing motion, performance | Idle/flight on both stones |
| WP7 tip/glints | Stable centre, no white blob, 12–32 px clarity | Metal and Fire swords with glints |
| WP8 sparks | Directional distribution, size classes, deterministic paths, cost | Key-1 with particles off/on |
| WP9 Halo | Ring width, path registration, no merged bangle, cost | Major blow at 100 px and close |
| WP10 timing | Immediate flash, hold, erosion ratio, residue overlap | 1× and 0.25× complete skills |
| WP11 integration | T1/T4/C1/C2, AA, 88-sword budgets, no legacy layers | Final normal play host |

### Blind-review procedure

Claude creates matched before/after captures using the same camera, seed, ground, display settings and event timing.

Present candidates with randomized identities. The two judges score independently before seeing each other's results, prior scores or implementation method.

The review should evaluate five questions for each visual: silhouette/design, motion quality, material/light quality, readability and overall premium presentation. These category scores help diagnose failures; the independent overall scores determine acceptance.

Whenever a candidate reaches 7, provide the owner with its demonstration video. At ≥8.5 from both judges, proceed to integrated regression tests.

An isolated 8.5 effect is not accepted if the full skill drops below 8.5, loses blade readability or exceeds performance budgets.

### Three-attempt stop rule

Track attempts by method and targeted defect, not by the entire effect family.

For example, three failed periodic-texture improvements should stop that looping method, not cause the approved Fire sheath direction to be abandoned.

Record whether the lower judge score improved, whether a specific technical defect was eliminated, and whether a new critical regression appeared.

If three consecutive attempts provide no genuine improvement, stop and change the implementation method.

Do not repeatedly change glow intensity or particle count when the identified problem is a bad silhouette.

# 6. Remaining technical and production risks

| Risk | Verification | Fallback |
| --- | --- | --- |
| Original Firefly source no longer available | Asset inventory | Use retained 12 fps frames with honest temporal metadata |
| Firefly changes painted stroke geometry | Full contact sheet, registration and mask metrics | Preserve authored envelope; reuse only interior motion |
| Final keyframe appears only at 5 s | Inspect full clip | Drive late ember state through runtime persistence |
| Extracted flame alpha has black fringes | Both-stone edge composite | Rebuild matte and unpremultiply/re-premultiply carefully |
| Scrolling textures look static or repetitive | Ten-cycle real-speed test | Registered animated coverage on same blade mesh |
| Backing becomes a black sticker | Ink-only and final images | Break and soften authored ink, reduce coverage |
| Hot-core bloom becomes a cream smear | Pre/post-bloom and final captures | Narrow HDR area and adjust emission |
| One-pixel blade gap disappears | Projection/AA tests | Increase local exclusion or alter geometry width |
| Halo lines collapse at 100 px | Real-size mask comparison | Simplify engraving; use alpha instead of MSDF |
| Key-1 residue hides later hits | Full +18/+36/+66 replay | Decrease bright-body coverage; preserve only sparse embers |
| Particle motion becomes mechanical | Fixed-seed trajectory capture | Revise directional distribution and source sprites |
| Transparent overlap exceeds cap | Diagnostic per-pixel contribution count | Merge materials or move extra elements outside blade |
| Atlas memory or upload cost too high | Runtime memory and frame-time profiling | Smaller cells, reduced variants, deferred close-up data |
| HDR path unsupported or misconfigured | Extension/render-target/blending tests | Validated lower-intensity fallback, judged independently |
| Jade-ring repaint changes sword identity | Registered source comparison | Edit only original UV/material region |
| C1 Weber interpretation cannot pass conventionally | Report signed and dark-reference contrasts | Keep gate unresolved, not falsely passed |
| Generated media missing in play host | Clean deployment/preload test | Fix versioned external-media delivery |
| Old effects still render | Registry and per-layer screenshots | Remove obsolete effect registration |
| Performance varies between runs | Warm interleaved A/B tests | Report repeatability, do not claim precise GPU timing |

### License and provenance

All newly generated artwork should be recorded as project-owned generation outputs, with their source prompts and model details.

The optional `msdfgen` utility is MIT-licensed according to its repository license; if distributed or incorporated as software, follow the license notice requirements.  [GitHub]

No third-party artwork, game footage, commercial model asset, or external visual reference should be uploaded into the image/video generation workflow. Reuse the project's own candidate assets only.

Keep the generated media outside Git and retain license/provenance metadata in the manifest.

# 7. Remaining uncertainties

The following are genuine unknowns; this corrected plan does not pretend to have tested them.

Existing candidate fidelity. The actual frames from Ticket 252 v1/v3 and the overnight videos have not been visually inspected in this turn. The brief supports their qualitative strengths and defects, but not a new verified ranking of individual frames.

Firefly source recovery. It is unknown whether the original 24 fps footage still exists or only the retained 12 fps atlases remain. The extraction workflow changes depending on which is available.

Movement preservation. The periodic-texture approach is plausible, but its ability to retain the soft living flame must be proved. This is why the registered animated-coverage fallback is explicitly part of WP3.

Rendering implementation. The installed three.js version, current postprocessing stack, HDR target formats and shader configuration must be inspected. Official documentation establishes what APIs permit, not what the local renderer currently does.

Exact alpha reconstruction. Black-background footage cannot uniquely reveal foreground alpha. Any matte is an authored/estimated reconstruction requiring real-background review.

C1 measurement. The conventional Weber sign/reference issue is real. It must be made visible without silently changing the approved numeric gate.

Artistic tuning. Proposed opacity, texture flow, particle counts, erosion durations, brightness distributions and contrast screening values are trial settings. None is a guaranteed threshold for 8.5-quality appearance.

Close-up resolution. A 256 px impact cell may be adequate for 70–160 px play output but insufficient for 400–500 px close-ups. The actual source detail and sampling must determine the final choice.

Measured performance. The source gives budgets but not actual package overheads. The proposed allocation cannot be certified until the integrated host is profiled.

These are bounded test tasks, not missing artistic decisions.

# 8. Final production sequence

Gate A — Baseline and infrastructure

WP0–3: reproducible capture, media delivery, correct blending and loop handlingGate B1 — Key-1 impact

Ticket 252 v1/v3 → registered first/last frames → Firefly motion → erosionGate B2 — Sword presence

Metal mantle + Fire sheath → blade-hugging meshes → preserved steelGate C — Crafted highlights and timing

WP7–10: tip star, sparks, gold dust, major-hit seal, immediate flash and slow decayGate D — Integrated gameplay and performance

WP11: +18/+36/+66 timing, white jade, blade contrast, AA, all 88 swordsFinal acceptance

## Both judges ≥8.5

Normal play host, both grounds, real speed and 0.25×, no URL flags, all hard gates passing
## 9. Verified primary references

The technical claims in this review are based on these verified official or author-maintained sources:

- [Adobe Firefly — Video generation using first/last images](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html)
- [Adobe Firefly — Transparent-background generation](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-with-transparent-backgrounds.html)
- [three.js — ShaderMaterial](https://threejs.org/docs/pages/ShaderMaterial.html)
- [three.js — Blending and transparency](https://threejs.org/docs/pages/Material.html)
- [three.js — Raw data textures](https://threejs.org/docs/pages/DataTexture.html)
- [three.js — Texture filtering and wrapping](https://threejs.org/docs/pages/Texture.html)
- [three.js — Instanced rendering](https://threejs.org/docs/pages/InstancedMesh.html)
- [three.js — Colour Management](https://threejs.org/manual/pages/color-management.html)
- [three.js — OutputPass](https://threejs.org/docs/pages/OutputPass.html)
- [three.js — SMAAPass](https://threejs.org/docs/pages/SMAAPass.html)
- [Khronos — Floating-point colour attachments](https://registry.khronos.org/webgl/extensions/EXT_color_buffer_float/)
- [Khronos — Floating-point blending](https://registry.khronos.org/webgl/extensions/EXT_float_blend/)
- [Khronos — GPU timer queries](https://registry.khronos.org/webgl/extensions/EXT_disjoint_timer_query_webgl2/)
- [FFmpeg — Motion interpolation filters](https://ffmpeg.org/ffmpeg-filters.html)
- [Viktor Chlumský — MSDF generator](https://github.com/Chlumsky/msdfgen)
- [Björn Ottosson — Oklab colour space](https://bottosson.github.io/posts/oklab/)

The documentation supports the identified implementation capabilities and limitations. The visual scoring expectations, parameter ranges, timings and allocation budgets are project-specific engineering proposals.

Final decision: Preserve the current best Firefly fire movement, replace the rejected silhouettes with authored art, implement controlled mesh-based sword effects and one-shot painted impacts, and judge everything at the real play-camera scale. The corrected plan is an implementation specification, not a claim that the untested integration has already passed.


---

**[TURN · Lượt chạy 1 · Rà soát 3 của ChatGPT: FAIL (kết luận và danh sách lỗi nguyên văn; phần bản sửa bị dừng)]**

VERDICT: FAIL

## Problems found

The previous answer remains directionally sound, but it is not yet a fully executable implementation specification. I found 17 issues requiring correction, including errors in the rendering tests, unresolved asset-generation details, and specifications that could lead Codex to implement something different from the owner's approved design.

| ID | Problem | Required correction |
| --- | --- | --- |
| P01 | The Firefly documentation was oversimplified. Adobe's current image-to-video page says a first keyframe disables the transparent-background option in that workflow, while its dedicated transparency workflow describes using transparent PNG keyframes. The previous answer did not distinguish the two interfaces. | Use the project's proven opaque-black 1080p square workflow for the impact. Treat transparent 540p as an optional, separately validated workflow, not a fallback assumed to work with identical controls.  [Firefly +1] |
| P02 | The scrolling-texture pipeline had no reproducible method for constructing its source. Extracting a region of Firefly footage does not automatically create a spatially seamless texture, and translating it may lose the soft turbulent motion the owner likes. | Specify offline motion extraction, edge matching, temporal validation, UV phase control and a fallback to mesh-mapped animated coverage. |
| P03 | The shader had no final implementation-level data contract. It described body, ink, core and erosion but did not completely specify static versus animated texture channels, sampling, colour steps and alpha reconstruction. | Define exact static masks, motion data, shader equations and output format, including the treatment of straight-alpha source assets. |
| P04 | The proposed overdraw test could miscount layers. It did not distinguish transparent fragment contributions from final postprocessing, and its coverage cutoff could miss faint but extensive transparent sheets. | Use a dedicated contribution-count pass, separate union-of-blade-coverage measurement, and independently test final composited blade-keep. |
| P05 | The `11.5 ms` acceptance gate was weakened by introducing rolling p95 without resolving the meaning of “no window above 11.5 ms.” A rolling p95 can pass while individual frames exceed the threshold. | Report per-frame maxima, rolling-window statistics and the existing project's window definition. Do not certify the gate using a weaker statistic. |
| P06 | The timing profiles were not fully internally consistent. Some rows mixed absolute phase intervals with phase durations. The first hit's late embers could also overlap the next hit without a sufficiently precise spatial coverage rule. | Use one absolute-tick timeline, define peak-relative coverage at +18 ticks, and test the complete +18/+36/+66 sequence. |
| P07 | The proposed glint remained under-specified at 12 pixels. A four-arm painted image can still collapse into a dot after minification, mipmapping, bloom and FXAA/SMAA. | Create discrete small/medium/large glint assets or tested LOD masks, with explicit center-size and projected-arm gates. |
| P08 | The impact plane's world placement remained an open experiment rather than a default implementation. A ground-plane decal and camera-facing slash have different projection and depth behaviour. | Implement the impact primarily as a camera-facing slash plane anchored in world space, depth-tested against the environment; reserve ground decals for separately painted marks. |
| P09 | The particle specifications still mixed world-space physics and screen-space lengths without a clear conversion. They also did not define how collisions and velocity stretching remain deterministic. | Define the ground-plane coordinate system, tick-based trajectory, collision solution, camera projection and screen-size clamping. |
| P10 | The atlas specification failed to settle mipmap/filtering treatment for very narrow 1-pixel lines and packed data channels. Padding alone is insufficient. | Specify cell insets, a manual mip/LOD policy, mask filtering, motion-texture filtering and explicit tests for bleeding and disappearing cores. |
| P11 | The tip, sheath, silk tail and particle layers lacked a strict rendering/occlusion schedule. Transparent sorting and intersection with sword geometry can make external effects appear over the blade even when the source masks are correct. | Define render groups, depth testing, protected blade corridors, allowed overlaps and a sorting-regression capture. |
| P12 | The `C1` Weber discussion remained too open-ended. The mathematical conflict is real, but the previous answer effectively left a decision for the implementation worker despite the owner's instruction not to reopen the design. | Preserve both approved thresholds; make measurement diagnostic and mark the conventional dark-on-light Weber test mathematically infeasible rather than substituting another pass rule. |
| P13 | The previous answer still risked unnecessarily rebuilding `ff-f1-c4`. Its best qualities are the soft, living fire, and it scored 7/7. New Firefly generations may produce worse motion. | Salvage existing motion first, measure the corrected sheath in the host, and authorize new generations only when a specific motion defect remains. |
| P14 | Some artwork prompts did not fully specify extraction-friendly layouts. They lacked consistent registration marks in metadata, subject bounds, safe margins and masks for geometry that must stay empty. | Use a defined source-art coordinate system, transparent/blade-protection regions, pixel registration, shape IDs and automated mask QA. |
| P15 | The external-media package was incomplete operationally. A manifest alone does not establish where files are copied, how releases pin their versions or how normal-host loading is validated without URL flags. | Define an external source area, packaged runtime-media directory, immutable manifest revision, preload procedure and failure behaviour, adapting paths to the existing repository. |
| P16 | The 8.5 acceptance procedure could still permit a full-skill regression. Passing separate layers and one favorable composite is not enough when 88 swords, overlapping hits, bloom and the UI are present. | Require a fixed integrated regression matrix and both judges ≥8.5 on the final normal-host build, with re-judging after materially visible changes. |
| P17 | The performance and artistic fallback policies did not clearly separate reversible tuning from architecture changes. Three unsuccessful changes in opacity should not automatically trigger a new generation or a renderer rewrite. | Assign a measurable failure hypothesis to each attempt, keep the strongest accepted components, and change only the failing method after three non-improving tries. |

Several earlier concerns are now confirmed correctly rather than reopened: `ff-f1-c4` and `ff-m1-c4` contain 24 retained frames at 12 fps; the first contact moves to approximately +18 ticks; the Fire blade remains dark; the original 95% first-frame rule applies to the flash/core; and the existing owner budget and blade-keep requirements remain binding.

# Corrected full analysis and solution

[Claude: phần "Corrected full analysis and solution" của lượt rà soát 3 bị Claude bấm Stop khi ChatGPT mới viết được khoảng 19.000 ký tự (mục 1 tới đầu WP3), vì sau ba lượt FAIL liên tiếp thì không còn đường nào có hai PASS liên tiếp trong 4 lượt rà soát (luật dừng, `agent-orchestration` bước 7). Phần dở dang đó không chép lại ở đây; nội dung của nó lặp lại bản lượt 2 cộng các sửa đổi P01–P17 ở trên.]


---

**[TURN · Lượt chạy 2 · Brief 2 (Claude gửi, nguyên văn, cuộc trò chuyện mới)]**

````text
Role: you are the analyst for a game project. Research, analyse and propose a concrete solution. Answer in English.

This is a NEW run with a corrected brief. In an earlier chat a long answer failed three self-reviews in a row, mostly because my brief left some gates ambiguous and missed code facts, and because the answer grew too long to be checkable. This brief settles those points (section SETTLED) and asks for a COMPACT answer.

GOAL
One ordered integration plan that takes last night's best Firefly Video candidates (blind-judged 6.5-7) to the owner's bar of 8.5 for the Sword skills of "Tu Tien Thu Ai" (browser typing game, three.js r170 / WebGL2, xianxia, Metal and Fire elements). For each layer: the tool, the order of work, the risks, how to measure and judge. Layers: (1) Metal mantle around the flying sword ("Wind-Silk Mantle"); (2) Fire sheath around the dark hot-edged blade; (3) tip star; (4) key-1 Fire impact body (three brushstroke flame crescents) with its designed first and last frames for Firefly image-to-video; (5) sparks; (6) halo seal (big blows only); (7) dark backing so art reads on light stone; (8) seamless loops without ghosting; (9) burst-in for shapes complete at frame 0; (10) slow decay.

FACTS
Scale: play camera ~38 px/m; swords 60-130 px on screen; tip star 12-32 px; impacts 70-160 px; close-up 400-500 px. Grounds: light stone #d6d0c2, dark stone #2a2c30. Key 1 = three swords, hits at +6, +36, +66 ticks (60 Hz) today. Key 7 = 88 swords (6 lead full meshes, mid LOD meshes, far impostor quads).
Rejected by the owner: aura round 1 (shader-drawn mantle, analytic 4-point tip star), the current Fire impact (symmetric lotus flipbook), code-drawn cracks/scorch. Blender Mantaflow with flat stepped colour scored 3.5-4.5: stopped.

Best candidates (judge 1 / judge 2), all Firefly Video (Adobe model). Original 24 fps, 5 s source clips still exist for all 26 candidates; atlases were cut from them.
- ff-f1-c4 flame sheath card along the blade, 7/7. Soft living flame licking both sides of a hot line, needle at tip. Gaps: symmetric, does not sweep back with flight, blob at hilt end reads as an arrowhead, crossfade ghosting f16-23, cream smear on light stone (additive), no white-gold point or stars. Atlas kept 24 frames at 12 fps (every 2nd source frame).
- ff-g1-c2 tip star (white mask: 4 long + 4 thin diagonal arms, tiny core, soft halo; grows, turns 45 deg, shrinks), 7/7. Gaps: core swells to a white blob (32 % white at peak), jitter at f8 and f18-19, 1.33 s too long, a dot at 12 px, slightly stock-sparkle.
- ff-m1-c4 feather mantle card (silver plates with blue veins on both sides of a spine, blue silk threads meeting in a needle), 7/6.5. Gaps: solid and white, reads as a feather/fern object, would hide the blade, almost static silhouette, white block on light stone.
- ff-c3-c3 halo rings (hair-thin gold broken rings turning, stars running on them), 7/6.5. Gaps: rings merge into a bangle at 100 px, crossfade zone shows four stray bars, slightly elliptical, no engraved seal pattern, washes out on light stone.
- ff-a1-c5 crescent impact (image-to-video; first frame = Firefly's own flame warped into three crescents; opaque black 1:1 1080p), 6.5/6.5. Gaps: arc closes to ~300 deg (reads as a "C"), no taper (base/tip thickness 0.81), no white-gold hot line, sticker-cut edges, full shape at frame 0, dies in 6 frames, no sparkle.
- Others: ff-f1-c2 rolling flame ribbon 6.5/6.5 (too thick for a sheath; good trail); ff-g1-c3 gold twinkle set 6.5/6.5 (variants 5, 7, 8 bad); ff-m1-c3 fast silver qi streaks 6/6 (generic speed lines); sparks ff-b2-c2 5.5/5.5 (grinder sparks), ff-b2-c1 6/5 (jewel heads but 360 deg firework); gold dust ff-b3-c3 5.5/5 (stock glitter).
- Judges' shared verdict: the Firefly fire quality is what the owner wants, but it lacks design: open arcs, taper, a thin white-gold core, a dark layer, fast attack + hold + slow decay, and sparkle. Additive art washes out on light stone. 8-frame crossfade loops ghost. At 60-110 px details melt into one streak.
- Ticket 252 pilot painted three first frames (1536x1024 on black). I inspected them: v1 = three nested crescents sweeping up-right from a lower-left strike point, open fan, heavy roots tapering to needles, thin hot leading edge, a few glints and embers; v3 = two long crescents plus a short counter-stroke, similar quality; v2 = reads as a "V"/bird, weaker. Both v1 and v3 sit left of centre; they are not yet measured (arc, taper) and need recomposing into a 1080x1080 square.

CODE FACTS (current repo; you cannot see it, trust these)
- Post chain: EffectComposer (HalfFloat render targets by default in r170) -> RenderPass -> UnrealBloomPass (threshold 1.0) -> OutputPass. No AA at High today. r170 ships SMAAPass(width, height) and FXAAShader (no FXAAPass class).
- FlipbookPool: atlases stored straight-alpha, the shader premultiplies; blend One / OneMinusSrcAlpha; modes rgba/fire/smoke/heat; default crossfade of two frames and loops wrap to frame 0; also "stepped" and an rgba per-pixel "hold and erode" switch; per-instance erode and cool (burn-out by erosion); slowFrom/slowRate; no motion vectors; no per-instance ink; manifest has no rows/variants.
- Aura round 1 (WindSilkMantle): MantleSheath is ALREADY a blade-local instanced card mesh along the blade axis that reads a 96x1 blade half-width profile texture (so it knows the blade edge per slice) and a greyscale streak texture; MantleHull back-face shell on lead swords; SilkTail ribbon; MantleHalo analytic inside the far-sword impostor; TipStar analytic. All premultiplied with an ink term (Metal indigo alpha 0.35, Fire soot 0.85). Flame tongues on <= 14 swords per frame (6 lead + 8 mid), mids an ember mantle, far swords a broken ember rim. So "a blade-hugging mesh" exists; the look inside it is what must change.
- Key-1 Fire impact today: lotus flipbook card + spark-ray atlas + analytic ember dots + analytic heat rings + analytic ground seal + procedural scorch decal.
- Perf harness: each frame timed in page as CPU + a 1-pixel GPU readback (upper bound); windows = idle, key1, key7 hunt, key7 finish, K5; gate = each window p95 <= 11.5 ms; Fire over Metal <= 0.85 ms p95 at High 1920x1080 DPR 1; aura on Metal <= +0.6 ms p95 on key 7. GPU timer queries unavailable (ANGLE/Metal).
- Gates already in code: blade-keep (share of blade pixels within dE OKLab 0.04 of the aura-off frame: >= 90 % lead/mid, >= 85 % far; jade ring and guard >= 95 % every frame; no layer covers > 10 % of the blade), per-layer overlap.
- The skills live in a dev-only skills lab today (not yet in the game build). The owner reviews in a fixed snapshot of the lab at default flags; acceptance (two blind judges >= 8.5) is at the play camera with default settings, no URL flags. Art is served from art-src (media never in Git; synced to Drive).
- Tools: Firefly web (Firefly Video, Firefly Image, image Upscaler; Adobe models only; video upscaler is Topaz = banned). Firefly Video: 24 fps, 5 s; the proven image-to-video route is an opaque black 1:1 1080p first frame (transparent mode off). ChatGPT/Gemini paint 2D images (edit mode available). Codex CLI writes code from complete specs. Claude drives the browser, processes clips (numpy/scipy/Pillow, ffmpeg incl. minterpolate, tools/vfx-flipbook), measures and runs blind judges. No local AI.

SETTLED (decided by the coordinator; do not reopen, flag only a factual error)
S1. First-frame rule: the project's VFX standard applies "full brightness at age 0" to the contact flash and the impact light, not to the whole body. The body may reveal along the stroke direction over 2-4 frames, with the flash at >= 95 % of its peak at age 0.
S2. C1 (Fire blade readability): the owner approved measuring C1/C2 by dE OKLab in the FINAL image with VFX. Gate: dE OKLab >= 0.25 vs the local real background, idle and in flight. Luminance contrast is reported per polarity as a diagnostic only (the earlier "Weber >= 2" was a coordinator proposal and is dropped as a gate). C2: VFX over the blade <= 5 % in flight including the fan behind the shoulder and the trail.
S3. Runtime representations: mantle and sheath = the existing blade-local MantleSheath mesh with new art inside it (authored envelope mask + motion texture from Firefly), not full-rectangle cards; impact = one-shot card; glints/sparks = painted sprites on GPU instanced particles; seal = painted alpha (SDF only if it measurably helps).
S4. Owner decisions: aura direction A (Wind-Silk Mantle: qi plates outside the blade edge, 1 px ink gap, two seams meeting in a needle past the tip, open collar around the jade ring, silk tail) + ONE layer of C (the tip star). Fire blade = dark steel with hot edges, flames AROUND it. Jade ring = white jade with pale gold rim like the approved image. Fire mix = Brushfire body (3 big curved strokes, 4-5 counter-strokes, detached licks, dark underlay, stepped colour, white core <= 5 %, dies by strokes tearing apart from the tips) + Starfire sparks and glints (thin streaks, white-gold heads, cooling red tails, three lengths, 2-3 clumps along the blow, gravity, a few bounce once; per blow 1 big 4-point star and 2 small ones in turn; sparse gold dust in the aftermath) + Halo Seal thin rings on big blows only. Orange-red stays. Key 1: first sword hangs a beat pointing at the target; first hit +6 -> ~+18 (deliberate rule change; hits 2 and 3 stay +36 / +66). Readability fixes after the aura lands: T1 (swords 2-3 leave 0.25-0.3 s before hit, last 8-10 frames <= 12 px/frame), T4 (gate: each lead sword >= 12 frames at >= 40 px long and <= 12 px/frame; threshold tuned to the owner's eye), C1, C2, R1 (cheap AA at High). Lab stays instant-cast.
S5. Rules: fast attack, slow decay; every shape sparkles but no clip-art stars; anime/donghua/myth, radiant, luxurious, never realism as the goal; presence layer on every item and skill object. Bodies <= 0.85-0.9 per channel, only thin HDR cores bloom; <= 2 transparent layers per pixel inside each sword's area. Reserved colours: #FF4A4A, #7FF5E0, #FFC83A. Firefly prompts < 600 chars, no game/studio names, no "cinematic/realistic/volumetric/lens flare/bokeh/depth of field". No third-party images into AI tools. 2D images are painted by ChatGPT/Gemini; Codex only codes.

DELIVER (COMPACT: at most about 3,500 words; use tables; do not restate the brief; label every number as REQUIRED (from the brief) or TRIAL (yours))
1) Per layer: why it stops at 6.5-7 and the specific change (shape, motion, light, sparkle, backing, timing).
2) Ordered work packages: layer, source asset/candidate id, tool, worker, runtime approach, key TRIAL numbers, measurable checks, capture scenario, blind-judge step; which can run in parallel.
3) New art: the list and complete prompts (Firefly Video < 600 chars; image prompts for the impact first frame recompose/edit, the last frame edit, mantle/sheath envelope masks, star sheet, spark/dust sheets, seal); candidates per item.
4) Answers: (a) seamless loops without ghosting (for the mantle/sheath motion texture and for any frame loop); (b) burst-in under S1; (c) dark backing on light stone without a sticker outline inside the 2-layer cap; (d) keeping the blade visible with a mantle that judges called "solid white".
5) Top risks with checks. 6) What you are not sure about.
Cite a source for factual claims (official docs: three.js, Adobe helpx, Khronos, FFmpeg, maker's article); mark guesses as guesses.
````


---

**[TURN · Lượt chạy 2 · Câu trả lời 1 của ChatGPT (nguyên văn, 28.070 ký tự)]**

# Tu Tien Thu Ai — Sword VFX Integration Plan

Production recommendationDecision: Preserve Firefly's organic motion, but stop using its generated silhouettes as the final design. The path from the current 6.5–7 to the owner's 8.5 target is painted shape control + Firefly motion detail + blade-local rendering + deliberately staged animation.

Do not restart Blender simulations or rebuild the existing mantle geometry.

All numbers below are identified as R = REQUIRED (brief or settled decision) or T = TRIAL (proposed starting value, not yet validated). Candidate IDs and package identifiers are asset names, not measurement thresholds.

## 1. Layer-by-layer diagnosis and changes

| Layer | Why it stops at 6.5–7 | Required change |
| --- | --- | --- |
| Metal mantle | `ff-m1-c4` looks like an opaque feather or fern. It changes the sword's silhouette and hides the steel. | Retain Wind-Silk Mantle A. Paint separated silver-blue qi plates outside the blade, negative spaces, open jade collar, silk seams and needle tip. Reuse Firefly for internal moving threads, not the whole silhouette. |
| Fire sheath | `ff-f1-c4` has excellent flame motion but symmetrical lobes, a hilt arrowhead and washed-out additive colours. | Dark hot-edged steel stays visible. New asymmetrical envelope; Firefly flame flows toward the rear of flight, with a tapered needle and no root blob. Local soot backing and thin white-gold hot edges. |
| Tip star | `ff-g1-c2` is oversized, jittery, generic and too long. Small versions collapse into a dot. | Paint a controlled star family based on its best arm structure. Short needle glint, sharp peak, rotating unequal arms, small residual shimmer. |
| Fire impact | `ff-a1-c5` closes into a C, has almost constant stroke thickness, appears fully formed and disappears abruptly. | Ticket 252 v1/v3 composition, three open brushfire crescents, counter-strokes, thin hot edge, detached flame licks, directed reveal and tip-first disintegration. |
| Sparks | `ff-b2-c2` resembles grinder sparks; `ff-b2-c1` resembles a firework; dust resembles stock glitter. | Painted heads and thin tails, gravity-based trajectories, three size families, localized clumps, occasional bounce, deliberately timed glints and restrained residual dust. |
| Halo Seal | `ff-c3-c3` merges into a bangle and develops crossfade bars. There is no identifiable inscription. | Painted broken rings with sparse engraved segments, rotating without changing their overall geometry. Big blows only. |
| Dark backing | Additive colour loses its shape on light stone. Solid black edging would look like a sticker. | Integrate localized ink/soot into the same premultiplied material as the coloured effect. Avoid a separate opaque contour. |
| Loops | The existing crossfade blends different silhouettes and creates ghost images. | Use periodic texture advection or a verified matching frame transition. Never crossfade complete silhouettes simply to hide a seam. |
| Burst-in | Complete geometry at age zero eliminates anticipation and acceleration. | Keep the contact flash fully bright; directionally reveal the body afterwards. |
| Slow decay | Effects vanish or fade uniformly, losing their material identity. | After a rapid attack and short hold, dissolve individual tips, islands, embers and ring segments at different rates. |

### Recommended visual composition

Metal: separated energy strands, a readable steel blade and restrained silver-blue movement.Fire: calligraphic crescents, directional movement, contrasting dark and hot strokes. Visual inspiration only, not source art.The production artwork must remain original. Neither reference image should enter the AI generation pipeline as an input.

## 2. Ordered work packages

The implementation should use one shared integration branch and independent source-art tasks. W1, W2 and W3 can run in parallel after W0.

| Order | Asset and worker | Implementation / trial settings | Measurement, capture and review |
| --- | --- | --- | --- |
| W0 — Baseline | Codex: lab instrumentation. Claude: capture automation. Existing code. | Freeze default lab configuration, manifest and renderer settings. Add asset version, variant/row indexing, deterministic event replay and per-layer coverage diagnostics. | Capture both stone types, idle sword, key-1 impacts, key-7 hunt/finish and K5. Archive baseline frames and performance windows. No blind scoring yet. |
| W1 — Metal | ChatGPT/Gemini: painted envelope. Claude: extract `ff-m1-c4` motion. Codex: existing MantleSheath shader. | T: outer qi width 3–8 px for lead swords; T: moving silk 8–12 fps or continuous UV advection. Existing 96×1 blade profile remains. | Lead/mid/far blade masks; 60–130 px play view; compare against aura-off and round-1 mantle. Blind A/B after integration. |
| W2 — Fire blade | ChatGPT/Gemini: asymmetrical envelope. Claude: extract `ff-f1-c4`; `ff-f1-c2` for trailing motion. Codex: shader. | T: flame width 3–9 px; T: trailing bias increases with sword velocity; localized hot line approximately 1–2 px. | Idle, forward flight, shoulder fan, both stones. Verify C1, C2 and blade-keep before visual judging. |
| W3 — Painted secondary kit | ChatGPT/Gemini: star, spark, dust and seal sheets. Claude: atlas processing. Codex: instanced sprite integration. Sources: `ff-g1-c2`, `ff-g1-c3`, `ff-c3-c3`. | T: glint 8–16 frames; T: sparks 18–36 frames; T: seal 35–55 frames, subject to blow timing. | Test at R: 12–32 px stars and approximately 100 px seals; isolated and over crowded combat. Blind secondary-effects comparison. |
| W4 — Fire impact artwork | ChatGPT/Gemini: Ticket 252 v1/v3 first and last frames. Claude: Firefly Video, source processing. | R: 1080² black keyframes. T: test v1 with two generations and v3 with one generation; retain full source clips. | Measure arc opening, stroke taper, hot-core coverage, attachment to strike point and collapse behaviour. Review extracted frames before runtime. |
| W5 — Impact integration | Codex: one-shot FlipbookPool card, painted masks, particle events, replacing existing lotus/spark-ray look. | T: reveal 2–4 frames; attack 3–5; hold 4–7; decay 18–28 frames. R: first hit +18 ticks; other hits +36/+66. | Contact frame, peak, release, decay, overlapping hits. Firefly-only vs integrated A/B; two blind judges at milestone. |
| W6 — Readability and AA | Codex: T1/T4, C1/C2 and R1. Claude: replay verification. | R: swords 2–3 depart 0.25–0.3 s before impact; last 8–10 frames no faster than 12 px/frame. R: each lead meets the 12-frame visibility gate. Add trial SMAA at High. | Default snapshot, not URL flags. Check movement, final-image contrast, blade coverage and all performance windows. |
| W7 — Release candidate | Claude: captures, metrics and blind evaluation. Codex: fixes only for identified failures. | Lock assets and default settings before judging. Retain only candidates satisfying hard gates. | R: two blind judges each score at least 8.5; no averaging away a failing score. Capture play view first, close-ups afterward. |

Parallel execution: W1, W2, W3 and W4 may proceed concurrently. W5 needs W3/W4 outputs. W6 follows the integrated aura because the settled movement fixes must be judged with the final appearance.

### Shared measurement contract

Use the existing performance and blade-keep gates unchanged:

| Required gate | Value |
| --- | --- |
| Each performance-window p95 | R: ≤11.5 ms |
| Fire over Metal, High | R: ≤0.85 ms p95 |
| Metal aura on key-7 | R: ≤+0.6 ms p95 |
| Blade-keep lead/mid | R: ≥90% |
| Blade-keep far | R: ≥85% |
| Jade ring/guard | R: ≥95% |
| Legacy layer-over-blade ceiling | R: 10% |
| Stricter C2, flight | R: ≤5% including shoulder fan/trail |
| C1/C2 contrast | R: ΔE OKLab ≥0.25 against actual background |
| Transparent overlapping surfaces inside sword area | R: ≤2 |

For C1, capture the final rendered image and a corresponding background-only reference with identical camera, lighting and ground state. Compare corresponding blade-region pixels after display colour conversion. Use the original author's Oklab transformation; report the resulting distribution, including the minimum across the agreed test regions.  [bottosson.github.io]

C2 needs a separate VFX coverage/depth or ID-mask capture, not merely a screenshot colour difference. Report the affected blade-pixel share over the entire flight, including the shoulder fan and trails. Keep luminance contrast diagnostic only.

## 3. New-art production prompts

The following are complete prompts intended for ChatGPT/Gemini image editing or Adobe Firefly Video.

### A. Painted images

| Asset | Exact prompt |
| --- | --- |
| Impact first frame — v1 primary | Edit the attached Ticket 252 v1 image only. Recompose its three nested flame crescents into a centered 1080×1080 square on opaque pure black. The impact origin sits slightly below-left of center, leaving generous room for the arcs to sweep toward the upper-right. Preserve three unmistakably separate, OPEN curved brushstrokes: thick roots, long tapering needle tips, no C-shaped closure, no V/bird silhouette. Add four or five small opposing brushstrokes, detached flame licks, a thin white-gold leading edge, sparse glints, and a dark burnt-ink underside. Orange-red anime/donghua flame, painted stepped values, no haze. No text, scenery or ground. |
| Impact alternative — v3 | Edit the attached Ticket 252 v3 image only. Keep its two beautiful primary sweeps and short counter-stroke, but develop the composition into three clearly distinct major fire crescents. Recompose into a centered 1080×1080 square on opaque black, with the impact origin below-left of center. Keep generous gaps between arcs and long needle tips. Add four or five smaller counter-strokes and a few detached tongues. Preserve painterly irregularity, stepped orange-red colour, a thin white-gold hot edge and localized dark undersides. No closed ring, bird silhouette, sticker border or haze. |
| Impact last frame | Edit the approved first frame while preserving its exact square canvas, strike origin, arc family and orientation. Show the final fragments of the SAME fire strokes. Their outer needle tips have torn into irregular pieces; the thick roots are dimmer red-orange islands with disconnected ember seams. No new crescents, no expanding ring, no new bright flash. A few cooling particles remain near the original motion paths. Keep the underlying composition recognizable so the two keyframes guide one continuous event. Opaque pure black background, 1080×1080. |
| Metal mantle envelope | Paint a blade-local horizontal texture guide, wide aspect ratio, pure black background. The real sword is NOT included. Design two asymmetrical families of slim silver-blue qi plates and silk threads outside an invisible central steel blade, leaving an unpainted central channel and a narrow gap at each blade edge. Open collar at the hilt, two refined seams converge into a single needle beyond the tip. Deliberate gaps between plates, translucent indigo undersides, elegant thin highlights. No solid feather silhouette, fern, wings, white block or luminous fog. High-resolution clean mask art. |
| Fire sheath envelope | Paint a horizontal blade-local flame envelope on pure black, without depicting a sword. Two unequal flame banks cling outside an invisible dark blade, with clear central negative space. Their tongues bend backward toward the hilt as though travelling at speed; a few long tapered tongues trail behind. The tip extends as a fine hot needle. The hilt end remains slender, never an arrowhead. Orange-red body, dark soot beneath selected flame roots, extremely thin white-gold edges. Anime/donghua fire with stepped painted detail, no halo haze. |
| Tip-star sheet | Original clean 2D xianxia sword-tip glint sprite sheet on pure black, separated non-overlapping cells. Include a needle streak, an asymmetrical four-point glint, an eight-arm glint with four long and four very thin diagonal arms, a sharp tiny peak and a fragmented fading glint. White-gold highlights with extremely restrained pale-orange secondary accents; narrow dark backing close to the strokes. No round white blob, stock emoji sparkle, lens flare, decorative text or scenery. Each cell must remain recognizable when reduced to tiny gameplay size. |
| Spark and dust sheet | Original isolated hand-painted effect sprites on pure black. Provide three distinct spark lengths: compact bright-head needles, medium curved ember streaks and a few long fast streaks. Each has a narrow white-gold head, orange body and cooling dark-red tail. Separate clusters of three or four related strokes, plus small irregular ember fragments and very sparse fine gold dust. No radial fireworks, grinder shower, stock glitter, diamonds, smoke clouds or text. Keep ample spacing between atlas cells. |
| Halo Seal sheet | Original xianxia Fire halo seal artwork on pure black. Hair-thin, deliberately broken concentric gold-orange rings, each with unique gaps, three or four sparse engraved rune-like segments and refined needle glints at selected intersections. The structure remains circular, not elliptical, with no thick bangle shape. Use broad graphic spacing so the design reads when reduced. A little dark burnt-ink backing directly behind selected engraved lines. No full glowing disc, dense calligraphy, fog, lens flare or text labels. |

Claude must inspect and remap the generated images into their actual runtime formats. The image generator's resolution or alpha claims are not sufficient evidence that the texture is ready.

For the impact candidates, an additional automated contour report should calculate the largest connected arc, opening angle and root-to-tip thickness ratio.

Suggested targets: T: visible arc opening greater than 60°; T: tip/root thickness ratio ≤0.25. These are screening values, not established owner gates.

### B. Firefly Video prompts

Adobe documents both first/last-frame guidance and default Firefly Video generation at 24 fps and 5 seconds. The supplied frames guide composition but do not guarantee that every intermediate frame respects the intended shape.  [Firefly +1]

Use Adobe Firefly Video only. The existing black-background image-to-video workflow remains the default.

V1 — Fire sheath motion (fallback if `ff-f1-c4` extraction fails)

Firefly Video prompt · under R: 600 characters

> [Writing] Thin living orange-red flame flowing horizontally along an invisible sword blade, with unequal tongues on both sides and clear dark space through the centre. Flame tongues sweep backward from a needle-sharp leading tip, stretching into slender threads, curling and shortening in irregular rhythms. Rich hand-painted anime flame shapes, stepped warm colours, occasional hair-thin white-gold streaks. Fixed camera, pure black background, isolated effect. No sword, no smoke cloud, no radial explosion, no thick blob, no text.

V2 — Metal silk motion (fallback if `ff-m1-c4` cannot supply useful strands)

Firefly Video prompt · under R: 600 characters

> [Writing] Separated silver-blue silk-like energy threads flowing lengthwise along an invisible horizontal sword. Thin strands peel outward, curve gently backward and reconnect toward a sharp leading needle. Small pale silver accents travel along indigo filaments; delicate irregular motion with clear black gaps between every strand. Elegant hand-drawn xianxia energy, slender and light, not solid. Fixed camera and pure black background. No sword, feathers, wings, leaves, fern, thick white shapes, fog or text.

V3 — Fire impact body, with painted first and last frames

Firefly Video prompt · under R: 600 characters

> [Writing] Three powerful OPEN curved brushfire strokes explode from one lower-left strike origin, sweeping upward and right in a fan. Thick orange-red roots taper into long sharp needles; four or five smaller opposing strokes and detached tongues follow. A hair-thin white-gold edge races along each curve while dark burnt-ink undersides preserve the shape. Rapid attack, brief strong shape, then the flames tear apart from their tips into curling fragments and cooling embers. Fixed camera, pure black background. No closed circle, lotus, smoke veil or text.

Selection rule: Use the original source clips before requesting more generations. Trial priority: v1 first, v3 second, and fallback video only for motion missing from existing material.

## 4. Implementation decisions for the difficult technical problems

### A. Seamless loops without ghosting

Preferred solution for Metal and Fire sheath: do not loop complete Firefly silhouettes.

Extract moving highlights and internal irregularities from the source, then use a spatially tileable motion texture inside the painted blade envelope.

1. Claude extracts original frames, masks black backgrounds, removes obvious subject translation and builds a motion texture. Separate the retained organic texture detail from the approved, static silhouette.
2. Construct a horizontally periodic texture with verified matching left/right borders.
3. Codex scrolls the UV through the existing blade-local mesh. Spatial repetition provides continuous motion; the envelope never changes identity.
4. Drive motion along the blade axis, with optional instance phase offsets. Keep the tip and collar masks stationary.
5. Use a restrained second nonperiodic variation only when it does not create a visible seam or require a second surface.

The `RepeatWrapping` mechanism is part of three.js, but a texture does not become seam-free merely by enabling wrapping: its opposite boundaries must match visually.  [Three.js]

For assets that genuinely need looping flipbook frames, select a source interval whose final-to-initial transition matches both shape and motion direction. Disable the existing crossfade for those variants.

Trial seam gate: boundary frame difference ≤1.25× the median normal adjacent-frame difference, plus no greater than T: 1 px visible landmark jump at play scale. Inspect the transition over T: 20 repeated cycles. A loop that fails becomes a one-shot or a scrolling-motion texture, not an eight-frame ghosted blend.

FFmpeg's `minterpolate` supports motion-compensated frame interpolation, but it cannot guarantee coherent disappearing flame tips. Use it selectively after visual inspection, not as a seam-repair guarantee.  [FFmpeg]

### B. Burst-in under S1

The painted first frame can show the complete designed body for Firefly guidance without requiring that whole body to appear in runtime at age zero.

Implement two independently controlled signals:

- Contact flash: R: ≥95% of peak brightness at age zero. This can use the impact card's dedicated flash mask or a small instanced glint.
- Body: T: directionally reveal over 2–4 game frames. The reveal travels from the strike root along each curved stroke.

Use an authored path-progress mask rather than a radial wipe. This keeps the painted silhouette intact once revealed and avoids constructing another procedural crescent.

### C. Dark backing without a sticker outline

Reuse the existing premultiplied shader and blending mode.

For each fragment, conceptually combine the dark and bright contributions before blending:

$$C_{\text{out}}=C_{\text{src,premult}}+(1-\alpha_{\text{src}})C_{\text{background}}$$

One appropriately authored fragment can darken light stone through its alpha while carrying an HDR highlight in its source RGB. A separate black geometry layer is not intrinsically necessary. The three.js material system supports custom blending factors, including `OneFactor` and `OneMinusSrcAlphaFactor`.  [Three.js Docs]

Important limitation: A dark border generated by simply dilating the whole alpha mask will look like a sticker. Paint backing beneath selected roots, inner curves and stroke undersides, with deliberate broken gaps.

Suggested trial construction:

| Component | Trial treatment |
| --- | --- |
| Dark ink/soot | T: alpha 0.25–0.55 in narrow local regions |
| Main body | R: no body channel above 0.85–0.9 |
| Hot core | Narrow HDR emission above bloom threshold |
| Outer fade | Irregular, spatially broken |
| Blade interior | Keep transparent except permitted overlap |

The existing Metal indigo and Fire soot coefficients are starting points, not reasons to expand the backing across the entire silhouette.

Inside the sword area, keep the MantleSheath as the main transparent surface. Explicitly inspect overlap from MantleHull, SilkTail and the tip star. Disable or spatially separate an old layer where it would violate R: ≤2 overlapping surfaces.

### D. Preserve blade visibility

The mantle problem is primarily silhouette coverage, not insufficient transparency.

Use the existing blade half-width profile to place energy outside the metal edge. The authored central channel remains transparent, with the R: 1 px gap and open collar.

For Metal, do not retain the opaque plates from `ff-m1-c4` literally. Extract only useful silver-blue internal motion. For Fire, the hot rim belongs to the dark steel blade material, while the surrounding flames occupy the sheath mesh.

On key-7, retain the established LOD budget: full flame tongues only on the R: 6 lead and 8 mid swords; far impostors receive simplified baked appearance rather than full new effects.

At small screen sizes, use authored LOD variants rather than uniformly shrinking every detail. The jade ring and cloud guard remain visually unmodified.

## 5. Runtime timing and rendering

### Recommended key-1 Fire impact envelope

Trial animation timing · 60 Hz required simulation clock

This is a proposed first-hit envelope, not a measurement from an existing clip. Later overlapping blows require independent event ages and coverage checks.Keep source frame interpolation and runtime sequencing independent. The FlipbookPool already has the necessary slowFrom/slowRate and erosion concepts. Extend its variant/row manifest and provide an authored erosion-order channel so tips disappear before roots.

For erosion, rank pixels along each stroke, with additional irregular breaks. Preserve the thin hot edge while its supporting fragment survives; fade or cool the surviving fragments afterward. Avoid uniform alpha fading across the whole effect.

### Render pipeline

Use the existing High pipeline and test:

`RenderPass → UnrealBloomPass → SMAAPass → OutputPass`

Three.js r170 source confirms the `SMAAPass(width, height)` constructor and half-float render targets. The modern documentation uses a different constructor signature, so Codex must implement against the pinned r170 source.  [GitHub +1]

Keep bloom limited to thin HDR cores. `UnrealBloomPass.threshold` is a luminance threshold, not a selective-emissive object mask. Verify that background highlights and fat fire bodies do not unexpectedly contribute to bloom.  [Three.js Docs]

If SMAA causes the performance gate to fail, benchmark an FXAA ShaderPass fallback with the correct output-colour pipeline rather than introducing a nonexistent `FXAAPass` class.

## 6. Quality risks, tests and corrective action

| Risk | Detection | Response |
| --- | --- | --- |
| Firefly destroys painted open arcs | Contour tracking across extracted frames; inspect peak and decay | Use painted body masks and Firefly only for internal flame motion |
| Motion loops ghost or jump | Seam difference, landmark jump, repeated-loop capture | Switch to spatial advection or nonlooping one-shot |
| Fire disappears on light stone | Final-image C1 plus isolated body preview | Narrow localized soot backing; adjust opaque hot blade edges |
| Metal looks like a solid feather | Blade-keep and silhouette/negative-space inspection | Remove plate fill, shorten segments, enlarge transparent gaps |
| Star becomes clip art | Small-size A/B captures at R: 12–32 px | Reduce arms, remove halo, favor needle glints at minimum LOD |
| Effects overwhelm key-7 | Overlap heatmap and R: p95 performance windows | LOD simplification, fewer independent particles, stricter layer ownership |
| Impact looks good only in close-up | Default play-camera blind review | Repaint the silhouette for screen scale instead of increasing bloom |
| Slow decay creates clutter at the next hit | Three-hit deterministic replay | Lower residual opacity and particle count while retaining tip-first fragmentation |
| C1 conflicts with dark steel on dark ground | Idle/in-flight ΔE against both actual backgrounds | Modify opaque blade edge/material contrast before adding more sheath coverage |
| AA changes quality or performance unexpectedly | With/without AA captures and full-window timings | Choose the cheaper verified pass; never silently change the accepted default |

## 7. Required blind-judge protocol

At each relevant milestone Claude prepares anonymized baseline/candidate captures, including normal-speed gameplay video. Judges must not see candidate IDs, prompt history or which version is newer.

The owner acceptance is the default skills-lab snapshot at the play camera. Close-ups are diagnostic evidence only.

Each judge evaluates shape/design, animation timing, light/contrast, blade readability, xianxia identity and overall market-quality impression. Only the final score from each judge determines the R: ≥8.5 acceptance gate. Neither averaged scores nor superior close-up scores override a failure.

Before blind submission, the automated gates must pass. A visually exceptional version that breaches C2, blade-keep, the transparency cap or p95 is not a release candidate.

## 8. Remaining uncertainty

These are deliberately unresolved implementation or validation questions, not requests to reopen owner decisions.

| Uncertainty | How to resolve |
| --- | --- |
| How much of `ff-m1-c4` remains usable when isolated from its feather silhouette? | Extract blue filaments and silver highlights from the original source; compare against a freshly painted animated-thread version. |
| Does the painted impact maintain open arcs through Firefly's middle frames? | Inspect all source frames and score the contour before atlas construction. First/last guidance alone is insufficient. |
| Can `ff-f1-c4` provide convincing trailing motion after removing its symmetrical shape? | Compare UV-advection and extracted temporal-detail methods in the existing sheath mesh. |
| What exactly constitutes the minimum acceptable C1 sampling region? | Freeze the final-image blade region, background reference and pixel aggregation method in W0; do not tune them after seeing candidates. |
| Will SMAA fit the existing headroom on the target machine? | Measure all required windows using the current 1-pixel readback harness. |
| Can the completed combination genuinely reach 8.5? | Unknown until default-view blind judging. Individual 7/7 source clips do not establish that result. |

## 9. Final production decision

Prioritize the work in this sequence:

W0 measurement → W1/W2/W3/W4 parallel art → W5 integration → W6 readability/AA → W7 blind acceptance.

The critical production choices are:

- Keep: `ff-f1-c4` for Fire motion, `ff-m1-c4` for useful Metal filaments, `ff-g1-c2` for star shape reference, `ff-c3-c3` for selected ring details, and Ticket 252 v1/v3 for impact composition.
- Rebuild: authored blade envelopes, impact silhouette control, directional reveal, spark/glint sheets, backing masks and tip-first erosion.
- Remove from the accepted default: the symmetric lotus impact, stock-looking spark-ray presentation, ghosted loop crossfades, solid feather silhouettes and any extra old layers that compromise readability.
- Do not restart: the mantle geometry, the whole FlipbookPool, Mantaflow, or the existing performance harness.

The main improvement is not additional brightness, particle density or Firefly generations. It is making the energy look designed at the actual game camera, while retaining the organic motion that already scored well.

That is the recommended route to a testable R: 8.5 candidate—not a guarantee of acceptance, but a bounded plan with specific assets, workers, checks and failure exits.


---

**[TURN · Lượt chạy 2 · Rà soát 1: Claude gửi lời yêu cầu tự rà soát chuẩn (nguyên văn như ở lượt chạy 1)]**

````text
Review your latest full answer above against the brief, the facts and the constraints. Check: wrong facts or sources, steps that would not work, missing steps, contradictions with the constraints or the owner's decisions, vague parts that a worker could not execute.
Answer in exactly this form:
VERDICT: PASS or FAIL
If FAIL: list each problem, then give the corrected FULL analysis and solution (not a diff).
PASS only if nothing at all needs to change.
````


---

**[TURN · Lượt chạy 2 · Rà soát 1 của ChatGPT: FAIL (nguyên văn, 36.328 ký tự)]**

VERDICT: FAIL

## Problems found in the previous answer

After reviewing the settled decisions, implementation facts and official documentation, I found 15 issues. The overall direction was correct, but the answer was not sufficiently complete or executable to pass production review.

| # | Problem | Required correction |
| --- | --- | --- |
| 1 | The Firefly extraction workflow was underspecified. It did not explain how to separate organic motion from silhouettes or preserve dark artwork when extracting alpha from black backgrounds. | Define source processing, independent colour/alpha/control masks, texture packing and validation. |
| 2 | The seamless-loop solution was conceptual rather than executable. “Construct a periodic texture” is insufficient, and the suggested landmark-jump measurement was unsuitable for changing flame shapes. | Provide a concrete spatial-tiling algorithm, shader sampling method, temporal-loop fallback and appropriate seam metrics. |
| 3 | Impact timing was not fully coordinated with source frame rates. A 24-fps Firefly clip cannot simply supply a new painted body shape for every frame of a rapid 60-Hz attack. | Separate simulation-time reveal from flipbook-time internal animation. Specify the exact event schedule. |
| 4 | The impact first/last-frame workflow omitted key limitations. Adobe's first/last-frame guidance does not guarantee satisfactory intermediate shapes, and the fixed 5-second source duration can encourage slow motion. | Add source-frame inspection, action-window selection and rejection/fallback rules. |
| 5 | C1 measurement was insufficiently specified. The previous plan did not lock the blade sampling region, comparison image, colour conversion or aggregation before testing. | Define repeatable final-image OKLab measurement while preserving the owner's required ΔE threshold. |
| 6 | C2 coverage measurement was incomplete. A material/ID mask alone may miss bloom or other screen-space contributions over the blade. | Measure actual final-image VFX interference alongside layer attribution, while distinguishing native blade material from overlaid effects. |
| 7 | The dark-backing implementation was missing crucial alpha details. The compositing equation was broadly correct, but the asset and shader workflow could lose soot or double-premultiply colour. | Specify straight-alpha storage, premultiplication exactly once, linear colour and single-surface compositing. |
| 8 | The exact key-1 scheduling was not carried through to implementation. Changing the first hit from +6 to +18 ticks requires updating the projectile, hang, departure, VFX and damage events together. | Provide one deterministic timeline with hits 2 and 3 unchanged. |
| 9 | The settled sparkle and presence requirements were incomplete. There was no explicit plan for every item's presence treatment or the required large/small glint choreography. | Assign presence, ink, sparkle, particle timing and LOD behaviour to each applicable layer. |
| 10 | The halo and spark instructions were too vague. They lacked operational acceptance checks for small-size seal legibility, spark distribution, gravity and bounce. | Add measurable layout, animation and size-variant checks. |
| 11 | The FlipbookPool extension lacked a data contract. It proposed rows and variants but did not specify manifest fields, channel semantics or handling of legacy assets. | Define a backward-compatible manifest extension and separate authored masks from video imagery. |
| 12 | The High-AA fallback needed more precise version-specific instructions. Current three.js documentation includes APIs that differ from r170. FXAA also requires special handling of pass order and colour space. | Reference the pinned r170 source and provide correct SMAA/FXAA chains. |
| 13 | The production handoff was incomplete. It omitted explicit asset packaging, reproducibility, Drive/art-src boundaries, content hashes and an integration-ready definition of done. | Add deliverables for ChatGPT/Gemini, Claude and Codex, without committing media to Git. |
| 14 | The old-effect replacement policy was ambiguous. Removing the procedural scorch, heat rings and rejected lotus could leave inconsistent remnants or an ungrounded impact. | Identify which legacy layers are replaced, disabled or retained only after a dedicated comparison. |
| 15 | The acceptance procedure needed stricter isolation and source verification. Some citations had not been rechecked, and diagnostic close-ups, early blind comparisons and performance measurements were not clearly separated from final acceptance. | Cite verified official sources, distinguish required gates from trial metrics, use default-view blind judging and give explicit failure exits. |

The previous answer also included unnecessary external reference images. They are removed from the corrected plan; all production artwork remains original and is generated or edited using the approved tools.

# Corrected full analysis and solution

Notation: R = REQUIRED by the brief or settled decisions; T = TRIAL recommendation requiring validation. Asset IDs, skill names and package identifiers are names, not additional thresholds. All timings below refer to the game's simulation clock unless explicitly identified as Firefly source time.

## 1. Integration strategy and layer decisions

The highest-probability route remains a hybrid art-controlled pipeline:

- ChatGPT/Gemini determine the silhouettes and painted details.
- Firefly Video supplies organic internal motion, not authority over the final silhouettes.
- Claude extracts, measures, packs and evaluates assets.
- Codex integrates them using the existing blade-local mesh, FlipbookPool and instanced particle systems.

No Blender restart, no local AI, no replacement of the established runtime architecture.

| Layer / source | Specific improvement required | Runtime and visual timing |
| --- | --- | --- |
| Metal mantle `ff-m1-c4` | Remove opaque feather/fern silhouette. Paint separated silver-blue qi plates, negative gaps, outside-edge silk, open jade collar and forward needle. Extract blue filaments from Firefly. | Existing MantleSheath and 96×1 profile. T: 3–7 px exterior width at lead-sword play scale; moving internal threads with restrained irregularity. Small authored glints at seam intersections. |
| Fire sheath `ff-f1-c4`, `ff-f1-c2` | Preserve living flame but remove bilateral symmetry, hilt arrowhead and cream smear. Flame tongues trail backward. Dark steel and white-jade ring stay exposed. | MantleSheath with asymmetric envelope and moving internal flame. T: 3–9 px exterior width, small hot highlights and soot under selected roots. |
| Tip star `ff-g1-c2` | Preserve the recognizable four long/four diagonal-arm structure, but remove swollen core and jitter. Add a distinct needle-glint LOD. | Painted sprite family. T: primary attack 4–8 frames, secondary shimmer 6–12 frames. Each sprite follows the real tip, not an arbitrary screen offset. |
| Fire impact Ticket 252 v1/v3, `ff-a1-c5` | Three open tapered crescents, counter-strokes, detached licks, thin hot edge and painted underlay. Stop C-shaped closure and six-frame disappearance. | One-shot FlipbookPool card. R: flash ≥95% at age zero; body directional reveal over R: 2–4 frames; slow stroke fragmentation afterward. |
| Sparks and dust `ff-g1-c3`, `ff-b2-c1/c2` as references only | Replace grinder/firework shapes with thin streaks, white-gold heads, red-cooling tails and localized clumps. | Painted instanced sprites. R: three length families, 2–3 clumps per blow, one big four-point star and two small sequential glints, gravity, occasional single bounce and sparse aftermath dust. |
| Halo Seal `ff-c3-c3` | Replace bangle and stray crossfade bars with spaced broken rings, engraved marks and moving highlights. | Painted alpha sprite/mesh on big blows only; no default ring spam. T: independently timed segments and partial erosion. |
| Dark backing Existing ink shader | Replace broad additive wash with selective backing under roots, inner curves and bright strokes. No continuous black contour. | Same premultiplied fragment as the artwork; no extra transparent surface. |
| Loops Original 24-fps sources | Eliminate silhouette crossfades and discontinuous wrap. | Prefer spatially periodic internal motion. Use temporal one-shot or a genuinely matched loop where appropriate. |
| Burst and decay Painted impact masks | Fast root-origin attack, brief hold, tip-first tearing, delayed cooling. No uniform disappearance. | Independent flash, reveal, breakup and cooling parameters driven by event age. |

Critical art hierarchy: opaque blade and jade details first; exterior energy silhouette second; small hot accents third; secondary sparks last. Add a subtle, individually authored presence treatment to the sword, impact, glints, sparks and seal without adding a new geometry surface everywhere.

The appearance must survive R: 60–130 px swords, R: 12–32 px tip stars and R: 70–160 px impacts. Close-ups at R: 400–500 px/m are for diagnosing paint and texture defects, not for acceptance.

## 2. Ordered production work packages

| Order | Worker and source | Deliverable and implementation | Check / capture / judge |
| --- | --- | --- | --- |
| W0 — Freeze baseline | Codex + Claude. Existing lab. | Deterministic skill replay, fixed cameras, per-layer masks, source asset manifest, final-image captures and performance logs. Preserve default flags. | Capture idle, key1, key7 hunt/finish, K5, both stones and aura-off. No acceptance judging yet. |
| W1 — Metal | ChatGPT/Gemini paint; Claude extracts `ff-m1-c4`; Codex integrates. | Authored envelope/control map plus moving silver-blue detail in existing MantleSheath. Retain the profile texture and required gaps. | Blade-keep, collar, silhouette and small-size checks. Capture lead/mid/far in key7. Blind direction A/B. |
| W2 — Fire sheath | ChatGPT/Gemini paint; Claude extracts `ff-f1-c4`, tests `ff-f1-c2`; Codex integrates. | Asymmetric flame envelope, rearward motion, dark steel and hot edges, integrated soot. | C1/C2, blade-keep, flight direction, light/dark stone. Blind A/B. |
| W3 — Secondary kit | ChatGPT/Gemini paint; Claude packs; Codex uses instanced particles. | Tip-star variants, spark/dust sheet and engraved seal. Remove rejected analytic tip-star appearance. | R: 12–32 px tip tests, seal at play size, spark trajectory, density and big-blow gating. |
| W4 — Impact source | ChatGPT/Gemini edit Ticket 252 v1/v3; Claude operates Adobe Firefly Video. | Matched R: 1080×1080 first/last frames, source clips, selected action windows, independently painted control masks. | Arc/taper measurements, frame contact sheets, internal motion, source-quality review. |
| W5 — Impact runtime | Codex + Claude. `ff-a1-c5` as comparison. | One-shot card with painted body, separate flash mask, event-driven reveal/erosion, sparks and optional big-blow seal. | Key1 hit replay at R: +18/+36/+66 ticks, overlapping impacts, slow decay. Blind integrated A/B. |
| W6 — Readability | Codex. Existing movement/renderer. | Apply T1/T4, C1/C2 and R1 after aura integration. Test SMAA and fallback AA. | Final-image gates, projectile visibility, frame timing and default-view readability. |
| W7 — Acceptance | Claude coordinates two blind judges; owner approves. | Locked default snapshot, reports and reproducible asset package. | All R gates pass; both judges individually score R: ≥8.5. |

W1–W4 are parallel after W0. W5 depends on W3/W4. W6 depends on the integrated aura; W7 follows the complete implementation.

### Concrete asset/manifest contract

Add optional backward-compatible fields to FlipbookPool manifests:

```JSON
{
  "id": "fire-impact-brushfire-v1",
  "kind": "oneShot",
  "frames": 24,
  "fps": 12,
  "columns": 6,
  "rows": 4,
  "variants": 1,
  "playback": "stepped",
  "colourAtlas": "asset-id",
  "controlAtlas": "asset-id",
  "controlSchema": "coverage-ink-core-erosion-v1",
  "loop": false
}
```

The frame/row/column values above are T: illustrative trial values, not a specification to force onto the selected impact. Actual dimensions must come from inspected source frames.

Recommended T control-texture convention:

| Channel | Meaning |
| --- | --- |
| R | Painted body coverage |
| G | Local dark-ink contribution |
| B | Thin hot-core mask |
| A | Stroke survival order for erosion: outer tips fail before roots |

The control texture is data, not straight-alpha colour. Actual output alpha is computed from its coverage and constituent contributions.

Keep video colour imagery in a separate RGBA atlas. Existing manifests without the new fields must continue using their current shader paths.

Asset ownership: code and manifests go to Git. Videos, painted sources, processed atlases and reports live under `art-src`, synchronized to Drive. Each candidate gets an immutable asset ID, SHA-256 hash, prompt, source ID, dimensions, channel schema, processing script version and judge result. The default lab manifest must resolve these assets without URL flags.

## 3. Complete art-production prompts

### A. Image editing and creation

These prompts are for ChatGPT/Gemini 2D painting, not Codex. All numerical composition requirements from the brief are R; any suggested sheet arrangement is T.

Impact first frame — primary v1

> Edit the attached Ticket 252 v1 image, preserving its original painted flame character. Recompose into an opaque pure-black 1080×1080 square. Center the overall effect while keeping the strike origin below and left of the main arc fan. Three separate open flame crescents sweep toward the upper right: thick irregular roots taper into extremely fine needle tips, with clear negative gaps. Add four or five counter-strokes, detached licks, localized dark ink underneath and a thin white-gold leading edge occupying no more than 5% of the luminous design. Orange-red stepped anime/donghua painting. No closed C, V-shaped bird, lotus, smoke veil, sticker edging or scenery.

Impact alternative — v3

> Edit Ticket 252 v3 only. Preserve its two elegant sweeping crescents and shorter opposing stroke, but resolve the artwork into three major distinguishable open brushfire strokes. Recompose into a 1080×1080 square on opaque pure black, with the impact origin below-left of center and sufficient room for every long tapered tip. Add four or five small counter-strokes, detached flame tongues, narrow white-gold leading accents and selective dark brush backing. Maintain irregular calligraphic weight, orange-red stepped shading and clean spaces between strokes. No closed ring, bird silhouette, symmetrical petals, haze or text.

Impact last frame — matched edit

> Edit the selected approved first frame, not a new composition. Preserve its exact canvas, strike origin, stroke identities and directions. Show those SAME three fire crescents near extinction: needle tips torn apart into small irregular fragments, middle sections split into disconnected islands and surviving roots reduced to cooling red-orange patches. Retain a few dying embers along the original sweep paths. Almost all white-gold brightness has gone. The remaining shapes must still identify their parent strokes. Opaque pure-black 1080×1080 background. No new arcs, rings, explosions, smoke or scenery.

Metal Wind-Silk envelope

> Create original high-resolution horizontal blade-local VFX mask artwork on pure black. An invisible sword occupies the empty central channel; do not draw the sword. Along its outer edges, paint two unequal banks of separated silver-blue qi plates, thin indigo undersides and flowing silk strands. Leave narrow black gaps against the blade and between the plates. Keep the hilt collar completely open around the jade-ring area. Two elegant seams extend forward and meet in a single fine needle beyond the tip; a sparse silk tail trails backward. Strong graphic negative space, handcrafted xianxia design. No feather, fern, wings, solid white silhouette, fog or glow blanket.

Fire sheath envelope

> Create original horizontal blade-local flame envelope artwork on pure black, with an empty channel for an invisible dark-steel sword. Paint asymmetric orange-red flames hugging OUTSIDE both blade edges. The upper and lower banks must differ visibly. Flame tongues bend backward toward the hilt, some extending as long delicate trailing ribbons; the leading end becomes a sharp needle. Keep the hilt end narrow and open, never a triangular blob. Add selective dark burnt-ink undersides and exceptionally thin white-gold edge accents. Strong tapered motion, stepped anime flame design, no sword, no symmetrical wings, no solid glow slab, no smoke or scenery.

Tip star sheet

> Paint an original isolated xianxia sword-glint sprite sheet on pure black, with separated non-overlapping cells and generous gutters. Include a long needle glint, a four-point asymmetric star, an eight-arm star with four long and four extremely fine diagonal arms, a tiny sharply defined core, and fading fragmented variations. Include short and long forms designed for very small game rendering. Use restrained white-gold and pale-orange highlights, with thin localized dark backing. Avoid round glowing blobs, stock clip-art stars, diamonds, lens flares, glitter gradients, text and scenery. Keep every cell centered and individually extractable.

Spark/dust sheet

> Paint original isolated anime/donghua fire-spark sprites on pure black. Three families: short needle sparks, medium curved streaks and long fast streaks. Each spark has a very small white-gold head, an orange body and a tapering cooling red tail. Include separate clusters of related streaks, isolated ember fragments, a few irregular collision flecks and sparse tiny gold-dust marks. Keep ample black separation between sprites so they can be extracted independently. Energetic but deliberate shapes, not uniform radial emission. No grinder sparks, fireworks, stock glitter, round beads, smoke, scenery or text.

Halo Seal sheet

> Paint an original mystical Fire-element halo seal on pure black. Several extremely thin, deliberately broken concentric golden-orange rings with broad spacing and different gap positions. Add sparse engraved seal-like marks, tiny radial notches, short interrupted strokes and a few needle glints travelling visually along ring paths. The composition must remain identifiable when reduced to gameplay size, without merging into a thick bracelet. Use localized dark ink behind selected strokes, not a complete black outline. Clean graphic geometry with luxurious hand-crafted detail. No thick disc, elliptical bangle, dense writing, smoke, lens flare or text.

Optional painted ground contact mark — replaces rejected procedural scorch

> Paint an original small overhead fire-contact decal on a transparent background: an irregular dark-charred stone imprint with a few fine disconnected ember fissures following the direction of a curved sword strike. Concentrate the strongest burnt mark near the impact origin and let the outer edges break naturally into scattered irregular fragments. Preserve the ground-like texture and avoid radial star silhouettes, ink splats, oil puddles or glowing lightning cracks. No surrounding scenery, text or hard sticker outline.

This optional mark must undergo its own visual comparison. Do not enable it by default merely because it has been generated.

### B. Adobe Firefly Video

Use Adobe Firefly Video only, R: 24 fps and 5-second sources; start from the proven R: opaque-black square first-frame workflow. Adobe documents first/last-frame guidance, but these are guidance frames, not a guarantee of continuous in-between shapes. Using both keyframes also disables the camera Motion options in the current interface.  [Firefly]

Each prompt below is under R: 600 characters.

Fire sheath motion

> Thin living orange-red flames flowing along an invisible horizontal sword, with asymmetric tongues on either side and a clear dark central channel. Tongues stretch backward from a fine leading needle, curling, dividing and retracting in irregular rhythms. Beautiful hand-painted anime flame shapes, stepped warm colour, brief hair-thin white-gold accents, rich organic movement. Fixed view, pure black background, isolated energy effect. No sword, feathers, smoke cloud, radial burst, thick blob, symmetrical wings or text.

Metal mantle motion

> Delicate separated silver-blue silk energy strands moving lengthwise beside an invisible horizontal sword. Individual indigo threads peel outward, weave gently and reconnect toward a forward needle. Small silver accents race along the strands at different speeds, with graceful flowing motion and clear black gaps. Refined hand-drawn xianxia energy, slender and lightweight. Fixed view, pure black background. No sword, fern, feather, wings, solid white plates, smoke, fog or text.

Fire impact — painted first and last frame

> Three OPEN curved brushfire strokes erupt rapidly from one lower-left strike origin, sweeping upward and right. Thick irregular orange-red roots taper into needle tips; smaller opposing strokes and detached licks follow. Narrow white-gold heat traces race along the leading curves, with dark burnt-ink undersides. A sudden strong attack, brief held shape, then flame tips tear into irregular fragments that cool and separate. Fixed view, pure black background. No closed circle, lotus, bird shape, smoke veil or text.

Candidate policy: Trial two v1 impact generations and one v3 generation before deciding whether more Firefly work is justified. The original 26 source clips remain the first source of usable motion; do not regenerate merely because a pre-cut atlas looks poor.

## 4. Implementation specifications

### A. Seamless loops without ghosting

For Metal and Fire sheath motion, use the following spatial loop construction:

1. Claude selects the most useful original source frames, stabilizes their coordinate systems and extracts moving luminous details. Do not assume black-background extraction supplies accurate alpha for dark material.
2. Remove the generated overall silhouette. Retain only moving filaments, flame textures and local highlights within the approved painted envelope.
3. Construct a longitudinal tile from these details. Blend the opposite edges of the texture itself to form a periodic spatial signal, with T: approximately 10–15% boundary-working regions. Do not blend two complete flame silhouettes.
4. Verify opposite texture edges have matching colour, alpha and visually compatible gradients. Repeat the tile horizontally; do not repeat across its vertical edge.
5. In MantleSheath, advance the longitudinal texture coordinate continuously with simulation time:

$$u_{\mathrm{motion}}=\operatorname{fract}(u_{\mathrm{blade}}\cdot k-vt+\phi)$$

Here $k$ is T: tile density, $v$ is T: motion speed and $\phi$ is per-instance phase. The painted envelope remains fixed in blade-local space.

1. Let the authored envelope mask determine the maximum visible flame/qi shape. T: independent subtle lobe-opacity variation can introduce life without regenerating geometry.
2. Validate over T: 20 repeated cycles, including the exact wrap. Inspect both stone backgrounds and all LODs.

Three.js supports `RepeatWrapping`; it does not automatically make nonperiodic artwork seamless.  [Three.js]

Temporal flipbook fallback: find a genuinely matching internal-motion segment, remove duplicate endpoint frames, set stepped playback and wrap without crossfade. Check first/last transition against ordinary adjacent-frame transitions and inspect for motion-direction reversals. A failed loop becomes a one-shot, not an eight-frame crossfade.

FFmpeg `minterpolate` can generate motion-compensated intermediate frames, but it is not an alpha-aware flame-topology solver. It is optional and must pass frame inspection before use.  [FFmpeg]

### B. Burst-in and slow decay

Use one event timeline, separate from Firefly's source fps.

T: trial first-hit impact timing at R: 60 Hz

| Age | Action |
| --- | --- |
| 0 | R: contact flash already ≥95% peak; impact light appears. Body reveal begins. |
| +1 to +4 frames | R: 2–4-frame directed reveal along painted stroke paths. |
| +4 to +10 frames | T: body holds a strong open shape; thin internal flame motion continues. |
| +10 to +34 frames | T: outer tips tear first, then counter-strokes, then roots; cooling and scattered embers remain. |

Do not retime the entire Firefly 5-second clip into this event indiscriminately. Select useful internal-motion frames or use the continuously scrolling texture; let the shader's authored reveal and erosion masks control the fast animation at 60 Hz.

The existing hold/erode, cool and slowFrom/slowRate controls should be extended, not duplicated. Use painted stroke survival values so individual islands retain their internal artwork until their assigned breakup. Avoid a uniform alpha fade.

### C. Dark backing on light stone

Use one premultiplied surface with localized dark and bright contributions. The required blend setup is:

```Plain text
source = ONE
destination = ONE_MINUS_SRC_ALPHA
```

Khronos documents the corresponding premultiplied-alpha blend equation.  [OpenGL Wiki]

Operationally, Claude supplies a separate painted dark-ink mask. Codex combines ink, coloured body and hot-core contributions inside one shader, computes a final alpha, then outputs RGB already premultiplied exactly once.

Preserve straight-alpha colour-atlas storage. Never premultiply on extraction and then premultiply the same data again in the shader.

Use sRGB colour textures with the correct three.js colour-space annotation; treat packed masks as non-colour data. Perform colour composition in linear space.  [Three.js]

T: initial backing opacity 0.25–0.55, locally beneath flame roots and select curves only. Do not infer backing alpha from dark pixels in an opaque-black Firefly video; that would destroy the soot. Preserve the R: 0.85–0.9 per-channel body ceiling and reserve HDR bloom for narrow cores.

### D. Blade visibility and overlap

The existing MantleSheath remains the geometry authority. Do not overlay full rectangular Firefly sheath cards.

The real sword blade must remain visually dominant. Maintain the R: 1 px ink gap, open jade collar and outside-edge energy placement. The Fire blade material itself provides the dark steel/hot-edge treatment; surrounding flames belong to the sheath.

The established key7 budget stays intact: R: 6 lead full meshes, mid LOD meshes and far impostors; full flame tongues on at most R: 14 swords per frame. Convert rejected analytic far-aura presentation to simplified approved artwork rather than rendering full new mantle detail on all R: 88 swords.

Inside any sword region, count actual transparent surface overlap. Reuse existing shell/tail layers only when they contribute meaningfully and satisfy R: ≤2 surfaces per pixel. A tip glint should normally project beyond the blade tip, not blanket its guard.

### E. Event timing, glints and presence

Key1 hit schedule is exact:

| Sword | Required impact | Implementation |
| --- | --- | --- |
| First | R: +18 ticks | Hold initially pointing at the target. T: determine departure within approximately +4 to +8 ticks, adjusted for actual path length and capped arrival speed. |
| Second | R: +36 ticks | R: depart 15–18 ticks before impact, approximately +18 to +21. |
| Third | R: +66 ticks | R: depart 15–18 ticks before impact, approximately +48 to +51. |

Damage, sound, contact flash, painted impact and spark emission all use the same hit-event timestamp. No VFX may accidentally cause duplicate damage.

Apply the R: final 8–10 frames at ≤12 px/frame rule and the R: T4 visibility gate: every lead sword appears ≥40 px long at ≤12 px/frame for ≥12 frames. If a path cannot satisfy these values, adjust earlier departure or staging rather than teleporting the sword.

For each blow, arrange the required big and small glints in sequence, not simultaneously. Emit the required spark clumps near actual blade/contact motion, with gravity integration and a bounce cap of one for selected particles.

For presence, every visible object gets a restrained material-specific cue: sword qi movement, impact living edges, spark head/tail hierarchy, glint sharpness and seal engraving. This cue is authored within the object's existing visual representation; it is not an extra full-screen glow layer.

### F. R1 anti-aliasing in r170

Test:

`RenderPass → UnrealBloomPass → SMAAPass(width, height) → OutputPass`

The pinned r170 source confirms the SMAA constructor with width and height; `EffectComposer` creates half-float render targets by default.  [GitHub +2]

Use the actual composer render dimensions, update on resize and verify the pass's lookup textures have loaded before capture.

If SMAA exceeds the performance budget, test `ShaderPass(FXAAShader)` with its inverse-resolution uniform. For the FXAA alternative, place it after `OutputPass`, because it expects display-space/sRGB input; do not claim the nonexistent r170 `FXAAPass` class exists.  [GitHub +2]

Keep the existing R: bloom threshold 1.0 and verify that non-core effect bodies stay below the effective bloom contribution after blending.

## 5. Measurement and judging

### Hard gates

| Gate | Required measurement |
| --- | --- |
| C1 | R: final-image ΔE OKLab ≥0.25 against local real background in idle and flight, on both stone types. |
| C2 | R: overlaid VFX coverage on blade ≤5% in flight, including shoulder fan and trails. |
| Blade-keep | R: ≥90% lead/mid, ≥85% far, using existing ΔE OKLab 0.04 comparison to aura-off. |
| Jade ring/guard | R: ≥95% preserved every frame. |
| Other overlap | R: no effect layer covers >10% of blade; stricter C2 applies in flight. |
| Transparency | R: ≤2 overlapping transparent surfaces per pixel within each sword region. |
| Performance | R: every required window p95 ≤11.5 ms; Fire-over-Metal ≤0.85 ms; key7 Metal-aura overhead ≤0.6 ms. |
| Visual | R: two blind judges each ≥8.5 at the default play camera. |

C1 implementation: capture final postprocessed RGB, a background-only comparison and a stable blade-region mask. Convert display sRGB to linear RGB and then OKLab using Björn Ottosson's published transform.  [bottosson.github.io] Freeze the exact blade sampling regions, exclusions for partially covered edge pixels, and aggregation before testing candidates. Report regional results separately; do not invent a percentile that silently weakens the owner's threshold. Luminance contrast is diagnostic only.

C2 implementation: capture layer-attribution masks plus an aura-on/aura-off final-image difference. Include bloom spill and sprite trails that cross the blade. Exclude native blade-material changes from the overlay numerator but report the resulting visible blade separately under C1 and blade-keep.

Performance: use the existing CPU plus one-pixel GPU-readback upper-bound harness consistently. T: warm up for 120 frames and run five repeat captures per window, with fixed replay inputs. Record individual-window p95s and the comparison deltas. Do not describe the results as pure GPU timing; GPU timer queries are unavailable on the stated platform.

Blind judging: submit anonymized normal-speed clips plus still frames from the R: default lab snapshot. Show light/dark stone, idle, flight, impacts, crowded key7 and decay. Ask judges to score shape, motion, light, readability, xianxia style and overall premium quality. Close-ups are diagnostic only. Acceptance requires both individual overall scores to meet R: 8.5 after all hard gates pass.

## 6. Highest production risks

| Risk | Check | Failure exit |
| --- | --- | --- |
| Firefly closes or deforms painted crescents | Track open-arc shape, root/tip ratio and frame-to-frame identities | Keep painted silhouette authoritative; extract internal motion only |
| Black source destroys soot during alpha extraction | Compare control-mask and composited RGB on both stones | Use separate authored ink mask, not black-key alpha |
| Seamless motion becomes repetitive | Inspect R: play view and T: 20 cycles; detect periodic visual beats | Change tile length, phase and localized modulation; use one-shot if needed |
| Blade disappears under Metal/Fire | C1, C2, blade-keep and real-sword close-ups | Reduce exterior coverage and fix opaque blade contrast |
| Sparks become fireworks or noise | Count clumps, directions, glint timing and overlay density | Repaint isolated sprites; adjust event choreography, not bloom |
| Halo collapses at gameplay size | Capture at normal blow size with underlying combat visible | Reduce engraved detail and widen meaningful ring spacing |
| Impact decays too quickly or creates clutter | Inspect every replay frame through the following hit | Adjust erosion-order mask and retained fragments |
| AA or particles exceed budget | All performance windows with default flags | Simplify secondary sprites/LOD; compare SMAA with FXAA |
| Legacy effects remain simultaneously active | Layer-ID capture and event audit | Explicitly disable rejected lotus, spark rays, heat rings and procedural scorch in the accepted default |

## 7. What remains uncertain

The following require actual asset tests and cannot be established from documentation alone:

| Uncertainty | Resolution |
| --- | --- |
| Whether `ff-m1-c4` provides enough reusable movement after removing its feather-like silhouette | Inspect original frames and isolate useful threads; compare with new Firefly motion |
| Whether Ticket 252 v1 or v3 survives first/last-frame generation better | Produce limited candidate clips, inspect all source frames and compare actual play-size composites |
| Whether `ff-f1-c4` can create convincing rearward flow using spatial advection | Test against the existing flight path and blade profile |
| Whether the locked C1 sampling definition is both repeatable and representative | Validate against known readable/unreadable baseline frames before candidate scoring |
| Whether R1 fits the available High headroom | Run the full deterministic performance harness |
| Whether the integrated result achieves 8.5 | Only the two blind judges can establish acceptance |

## 8. Final decision list

The production order is W0 → W1/W2/W3/W4 in parallel → W5 → W6 → W7.

Preserve the strongest existing material: `ff-f1-c4` Fire motion, useful `ff-m1-c4` threads, `ff-g1-c2` glint structure, `ff-c3-c3` ring details and Ticket 252 v1/v3 impact designs.

Replace their weak silhouettes with painted envelopes, use source-derived internal motion, control burst and decay at simulation rate, integrate selective dark backing within the existing premultiplied materials, and replace rejected key1 effects without retaining their unwanted visual signatures.

Do not promote a candidate based on asset quality alone. Its final test is the default skills-lab play camera, with sword readability, all technical gates and both independent blind scores passing together.

### Verified primary references

The implementation claims above were checked against these sources:

- [three.js r170 — SMAAPass source](https://raw.githubusercontent.com/mrdoob/three.js/r170/examples/jsm/postprocessing/SMAAPass.js)
- [three.js r170 — EffectComposer source](https://raw.githubusercontent.com/mrdoob/three.js/r170/examples/jsm/postprocessing/EffectComposer.js)
- [three.js r170 — FXAAShader source](https://raw.githubusercontent.com/mrdoob/three.js/r170/examples/jsm/shaders/FXAAShader.js)
- [Adobe Firefly — generate videos using keyframe images](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html)
- [Khronos — blending and premultiplied alpha](https://wikis.khronos.org/opengl/Draw_Buffer_Blend)
- [FFmpeg — official filter documentation](https://ffmpeg.org/ffmpeg-filters.html)
- [Björn Ottosson — Oklab definition and conversion](https://bottosson.github.io/posts/oklab/)

Final self-review outcome: The corrected plan now specifies the asset pipeline, work dependencies, shader data contract, source-to-runtime timing, exact hit schedule, testing method, failure exits and acceptance procedure. The remaining uncertainties are explicitly identified as empirical tests, not presented as verified facts.


---

**[TURN · Lượt chạy 2 · Rà soát 2 (cùng lời yêu cầu) · câu trả lời của ChatGPT: FAIL (nguyên văn, 31.063 ký tự)]**

VERDICT: FAIL

## Problems found

The previous answer is substantially improved, but it still fails production-readiness review. I found 13 problems, including implementation gaps, incorrect classifications of required versus trial decisions, and several unverified assumptions.

| # | Problem | Correction |
| --- | --- | --- |
| 1 | The mantle motion extraction is not technically complete. Removing a Firefly-generated silhouette does not automatically leave a usable independent motion texture. | Specify registration, isolation, manual inspection, painted masks, texture reconstruction and fallback. |
| 2 | The proposed control atlas cannot fully describe the intended animation. Four channels were assigned to coverage, ink, core and erosion, leaving no directional reveal information. | Use a separate authored reveal map, or explicitly encode reveal and erosion in different control textures. |
| 3 | The premultiplied shader contract remains incomplete. Simply combining ink, colour and HDR before blending can produce incorrect alpha, double-premultiplication or dark halos. | Define alpha combination, linear-space colour contributions, texture sampling and transparent-edge handling. |
| 4 | Loop construction could still introduce visible ghosts. Blending opposite sides of an arbitrary Firefly image does not guarantee continuity of flame features or movement. | Match spatial features before tiling; validate both value and gradient continuity; provide a deterministic fallback. |
| 5 | The Firefly first/last-frame workflow still conflates source animation with runtime animation. A five-second transition toward a nearly extinguished last frame may not contain a usable fast attack. | Treat Firefly as a source of internal flame motion and organic breakup. Let the runtime control attack, hold and decay. |
| 6 | C1 was not operationally resolved. The answer still leaves the acceptance aggregation undefined and does not address possible conflict with blade-keep. | Freeze sampling and reference-generation rules; compare identical opaque blade materials for blade-keep; do not silently change the settled threshold. |
| 7 | C2 was not sufficiently separated from C1. A final-image difference can misclassify legitimate changes to the opaque Fire blade as an overlay. | Use render-layer attribution plus final-image bloom-spill inspection. Report opaque blade contrast separately. |
| 8 | The first-hit movement schedule was speculative. A proposed departure at +4 to +8 ticks was not validated against actual travel distance or the required 12 readable frames. | Make the first departure conditional on a measured trajectory and enforce T4 over the actual screen-space path. |
| 9 | A settled option was incorrectly labelled REQUIRED. S1 permits a 2–4-frame directional body reveal but does not require that precise reveal in every effect. | Classify the reveal duration as a settled permitted range, with the selected timing a trial. |
| 10 | The Firefly, image and shader asset interfaces were incomplete. Missing anchors, source-space transforms, colour/alpha conventions, atlas gutters, variant indexing and LOD mapping could make assets unusable. | Supply a concrete asset contract and validation procedure. |
| 11 | Presence and sparkle choreography were still too vague. “Subtle presence” did not specify behaviour for all applicable visual objects, and timing of the three required glints was undefined. | Give each layer an explicit motion/brightness/edge cue and specify per-blow glint events. |
| 12 | The performance and AA fallback policy was incomplete. Replacing SMAA with FXAA is acceptable only if FXAA itself meets the visual and performance requirements. | Test both on the pinned renderer; preserve R1 as a hard requirement, not an optional enhancement. |
| 13 | The handoff and final acceptance still lacked sufficient failure exits. Source inspection, atlas-level validation, lab defaults, rejected legacy layers and performance baselines were not all tied to explicit completion criteria. | Define a reproducible acceptance package and stop conditions for every work package. |

### Source-review findings

I reopened the relevant official documentation.

- Verified: three.js r170 provides `SMAAPass(width, height)` and `FXAAShader`; `EffectComposer` defaults to half-float render targets.  [GitHub +2]
- Verified: `OutputPass` performs tone mapping and colour-space conversion. FXAA belongs after it because FXAA expects sRGB input.  [Three.js Docs +1]
- Verified: Adobe accepts first/last-frame guidance, but disabling camera Motion controls when both frames are supplied does not guarantee that the generated effect will keep its geometry. The generated video defaults to 24 fps and five seconds.  [Firefly +1]
- Verified: the proposed premultiplied blend factors are correct, provided the shader outputs correctly premultiplied RGB and alpha.  [OpenGL Wiki]
- Verified: FFmpeg `minterpolate` can perform motion-compensated interpolation; it does not promise correct topology or seamless loops.  [FFmpeg]

The earlier recommendation to place FXAA after `OutputPass` is retained. It was not an error.

# Corrected full analysis and solution

## 1. Final integration architecture

Production decision: Use painted silhouettes as the geometric/artistic authority, Firefly Video as the source of organic movement, and the existing three.js systems for positioning, timing, rendering and LOD.

Do not regenerate a complete effect when only its silhouette is defective.

Notation: R = REQUIRED by the brief or a settled decision. T = TRIAL proposal. Numbers inside quoted asset IDs are identifiers; numeric design counts in the prompts inherit the owner's requirements.

### Layer plan

| Layer | Source | Specific change | Runtime | Measurement |
| --- | --- | --- | --- | --- |
| Metal mantle | `ff-m1-c4` | Remove opaque fern/feather shape. Preserve useful silver-blue filaments. Paint separated qi plates, open collar, negative spaces and needle tip. | Existing MantleSheath, blade profile and SilkTail. | Blade-keep, T: negative-space inspection, idle/flight and key7 LOD capture. |
| Fire sheath | `ff-f1-c4`; `ff-f1-c2` trail | Replace symmetric flame envelope and hilt arrowhead. Preserve living flame motion, trail backward and keep dark steel exposed. | Existing MantleSheath with painted envelope and moving detail. | C1/C2, blade-keep, both stones, idle/flight. |
| Tip star | `ff-g1-c2` | Fix swollen core, f8/f18–19 jitter and excessive duration. Paint distinct small/large glints. | Instanced painted sprites. | R: 12–32 px display, stable tip attachment and no blob. |
| Impact | Ticket 252 v1/v3 | Three open tapered crescents, counter-strokes, hot line, dark backing, directional reveal and tearing decay. | One-shot FlipbookPool card. | R: 70–160 px, arc/taper tracking, contact/peak/decay. |
| Sparks/dust | `ff-g1-c3`; `ff-b2-c1/c2` references | Replace radial fireworks and grinder sparks with painted streak families, glints and restrained dust. | GPU instanced sprites. | Distribution, trajectory, timing, count and play-size captures. |
| Halo Seal | `ff-c3-c3` | Paint broken engraved rings and eliminate bars/bangle. | Painted alpha, big blows only. | Legibility at T: approximately 100 px; big-blow eligibility. |
| Dark backing | Existing ink shader | Local ink under roots/inner curves, not an outer sticker border. | Combined in the effect's existing premultiplied material. | Light/dark stone composites, alpha inspection. |
| Loops | Original Firefly clips | No full-shape crossfade. Periodic internal motion or verified temporal loop. | Continuous UV motion or stepped flipbook. | Repeated-loop capture and boundary comparison. |
| Burst/decay | Painted control maps | Full-bright contact flash, separately revealed body, independent stroke erosion. | Simulation-time controls. | Frame-by-frame event capture. |

Keep the approved Metal Wind-Silk direction A and only the tip-star contribution from C.

Visual hierarchy: opaque blade and jade details → outside-edge energy → narrow hot accents → carefully placed glints and sparks.

## 2. Ordered work packages

| Order | Responsible worker | Deliverable | Exit gate |
| --- | --- | --- | --- |
| W0 — Baseline and contracts | Codex + Claude | Freeze default lab flags, asset IDs, render settings, fixed replays, C1/C2 masks, per-layer captures and old/new toggles. | Existing effects reproduce baseline results; logs identify exact assets and settings. |
| W1 — Metal mantle | ChatGPT/Gemini paint; Claude processes; Codex integrates. | Authored Metal envelope plus organic moving filaments using existing blade-local geometry. | Blade-keep, overlap and key7 performance pass; blind direction comparison. |
| W2 — Fire sheath | Same division. | Painted asymmetrical envelope and motion texture from `ff-f1-c4`, with optional `ff-f1-c2` rear trail. | C1/C2, blade-keep and flight-direction tests pass; blind comparison. |
| W3 — Secondary kit | ChatGPT/Gemini paint; Claude packs; Codex integrates. | Tip-star family, spark/dust sprites and engraved seal. | No blob stars, fireworks, unreadable seal or missing presence treatment. |
| W4 — Impact art | ChatGPT/Gemini edit Ticket 252; Claude runs Firefly. | Aligned first/last frames, source clips, contour report and independently authored masks. | Painted shape remains identifiable at every selected runtime frame. |
| W5 — Impact integration | Codex + Claude. | One-shot brushfire card, burst/reveal/erosion, glint/spark events and key1 schedule. | All three hits occur at correct ticks without duplicated damage or effects. |
| W6 — Readability and AA | Codex. | T1/T4 movement, C1/C2 evaluation, SMAA/FXAA implementation. | All required visibility and performance gates pass at default settings. |
| W7 — Acceptance | Claude coordinates judges; owner decides. | Locked snapshot, blind clips, metric reports and asset handoff. | Both judges independently R: ≥8.5; all hard gates pass. |

W1–W4 can run in parallel after W0. The secondary kit and approved impact art feed W5. W6 follows the integrated aura.

## 3. Source-art processing and runtime asset contract

Claude should not simply key black to alpha and use the result as the whole effect.

### Processing sequence

1. Decode: extract original R: 24-fps, five-second clips at native resolution. Keep originals immutable. Inspect original `ff-f1-c4` frames corresponding to the ghosted atlas region before reusing them.
2. Register: align the useful Firefly subject along the blade axis, or align the impact's common strike origin. Reject frames requiring substantial invented reconstruction.
3. Separate: paint envelope masks independently. Extract only usable moving flame/filament detail from Firefly; do not preserve its poor overall shape.
4. Pack: create straight-alpha colour atlases with independently authored control maps. Include gutters and bleed colour beneath transparent texels to avoid dark filtering seams.
5. Validate: view every source texture and its runtime composite on R: light stone `#d6d0c2` and dark stone `#2a2c30`.
6. Register coordinates: save blade-axis orientation, local origin/anchor, asset aspect ratio, atlas frame order and runtime size. Recompose Ticket 252 artwork by uniform scaling/translation, not nonuniform stretching.
7. LOD: independently author the lead, mid and far visual variants rather than assuming full-detail sprites will shrink cleanly.

T: control-map layout

| Map | Channels |
| --- | --- |
| Geometry/control A | R = painted coverage; G = dark ink; B = hot core; A = erosion survival order |
| Timing/control B | R = directed reveal order; G = local motion influence; B/A reserved for validated future use |

The timing map can be a separate low-resolution texture. Do not force it into the already occupied control A channels.

The manifest must be backward-compatible and record: asset ID, source hash, atlas grid, frame count, frame rate, row/variant map, alpha convention, colour space, anchor, size, loop policy, LOD and mask schema.

No unvalidated atlas dimension, duration or frame index should be silently hard-coded.

## 4. Complete new-art prompts

### Image prompts — ChatGPT/Gemini

Impact first frame, primary v1

> Edit the attached Ticket 252 v1 artwork only. Recompose into an opaque black 1080×1080 square without stretching the existing strokes. Center the overall effect but keep the strike origin below-left of the sweeping fan. Preserve three separate OPEN flame crescents, with heavy irregular roots tapering into fine needle tips and generous negative gaps. Add four or five smaller opposing brushstrokes, detached flame tongues, a narrow white-gold leading edge covering no more than 5% of the luminous design, small glints and selective dark burnt-ink undersides. Orange-red stepped anime/donghua painting. No closed C, bird/V shape, lotus, smoke, sticker contour or scenery.

Impact alternative v3

> Edit Ticket 252 v3 only. Retain its two beautiful primary sweeps and short opposing stroke, then refine the composition into three distinct major curved fire brushstrokes. Arrange them in an open fan sweeping upward and right from a lower-left impact origin, inside an opaque black 1080×1080 square. Preserve long tapered needle tips, uneven thick roots and clear gaps. Add four or five small counter-strokes, detached licks, tiny hot-edge highlights and localized dark backing. Luxurious irregular anime/donghua Fire, orange-red stepped colours, no closed ring, bird silhouette, symmetrical lotus, smoke or scenery.

Impact last frame

> Edit the APPROVED first frame, preserving its exact size, strike origin, directions and individual brushstroke identities. Show the same three open crescents near extinction, with the outer needle tips torn into fragments, the middle sections splitting into irregular islands, and the roots fading to dark orange-red patches. A few embers follow the original stroke paths. Almost all white-gold accents have disappeared. The shapes must remain recognizable as the remnants of the original painting. Opaque pure-black 1080×1080 canvas. No new arcs, rings, smoke, explosion or scenery.

Metal mantle envelope

> Create original horizontal xianxia sword-qi mask art on pure black. Leave an empty central channel for an invisible real sword. Paint two asymmetric banks of separated silver-blue qi plates outside the blade edges, with deliberate black gaps, slender indigo undersides and silk-like moving-strand designs. Leave the hilt and jade-ring collar open. Two delicate seams converge toward one sharp needle beyond the sword tip; a sparse silk tail extends backward. Hand-crafted elegant silver-blue energy, readable negative space, never a solid white object. No blade, fern, feather, wings, fog or bloom blanket.

Fire sheath envelope

> Create an original horizontal fire envelope on black for an invisible dark-steel sword. Preserve an empty central blade channel and narrow gaps beside its edges. Paint asymmetric orange-red living flame banks OUTSIDE the blade, with irregular tongues swept backward toward the hilt and several longer slender trailing ribbons. The leading tip narrows into a fine needle. Keep the hilt end light and open, not an arrowhead. Selective dark soot under the roots, stepped warm colour and very thin white-gold heat edges. Anime/donghua Fire, no sword, symmetrical wings, thick blob, smoke cloud, fog or text.

Tip-star sheet

> Original isolated painted xianxia sword-glint sprites on pure black, in distinct cells with wide gutters. Include needle streaks, unequal four-point glints, eight-arm variants with four long and four very thin diagonal arms, tiny sharp cores and fragmented fading versions. Shapes must survive reduction to small gameplay size. Restrained white-gold and pale-orange accents with selective dark backing. Sharp crafted brush detail, no swollen round core, stock clip-art star, emoji, diamond, lens flare, haze, scenery or text.

Spark and dust sheet

> Original hand-painted anime fire-spark sprites isolated on pure black with generous gutters. Three length families: short bright-head needles, medium curved streaks and long fast streaks. Each has a tiny white-gold head, narrow orange body and cooling red tapered tail. Add a few irregular ember fragments, small directional streak clumps, sparse fine gold dust and isolated collision flecks. Every sprite independently extractable. No uniform radial fireworks, metal-grinder sparks, stock glitter, round glowing beads, smoke, scenery or text.

Halo Seal

> Paint an original xianxia Fire halo-seal sheet on pure black. Thin broken golden-orange concentric circles with generous spacing, different gap positions, sparse rune-like engravings, short interrupted radial notches and selective tiny needle glints. Maintain a clearly circular silhouette, with readable open gaps at gameplay size. Include subtle dark burnt-ink backing beneath selected engraved strokes only. Elegant mythic calligraphy-like design, never a thick bangle, complete glowing disc, dense illegible symbols, fog, lens flare or text.

### Adobe Firefly Video prompts

All three prompts are under R: 600 characters. Use Adobe Firefly Video, not partner models, and retain the proven opaque-black first-frame workflow.

Fire motion

> Thin living orange-red flames moving along an invisible horizontal sword, with unequal tongues on both sides and a clear central dark channel. The tongues stretch backward from a needle-sharp leading tip, curling, splitting and shortening in irregular rhythms. Beautiful hand-painted anime flame, stepped warm colours, occasional thin white-gold heat streaks. Fixed view, isolated effect on pure black. No sword, symmetrical wings, thick blobs, radial explosion, smoke cloud, haze or text.

Metal motion

> Separated silver-blue silk energy strands flowing lengthwise beside an invisible horizontal sword. Fine indigo threads peel outward, weave gracefully and reconnect into a forward needle. Small pale silver accents travel along different strands at varied speeds, preserving clear black gaps. Elegant hand-drawn xianxia energy, delicate and lightweight. Fixed view, isolated on pure black. No sword, feather, fern, wings, solid white object, smoke, fog or text.

Impact motion — approved first/last frames

> Three powerful OPEN curved brushfire strokes sweep rapidly upward and right from one lower-left strike origin. Heavy orange-red roots taper into long needles; small opposing brushstrokes and detached tongues follow. Hair-thin white-gold edges race along the curves while dark ink preserves their shape. Sudden attack, brief strong hold, then the flame tips fragment into irregular curling islands and cooling embers. Fixed view, pure black background. No closed ring, lotus, bird silhouette, fog, smoke veil or text.

Candidate rule: T: test v1 twice and v3 once, then inspect all generated frames. If Firefly breaks the painted composition, use its texture movement only; preserve the painted silhouette in runtime.

## 5. Four critical technical solutions

### A. Seamless motion without ghosting

Preferred for Metal and Fire sheath: periodic spatial motion, not looping complete Firefly silhouettes.

Claude should isolate coherent moving details, align them longitudinally, select compatible edge features and create a periodic texture with matched opposite boundaries. If required, perform local boundary reconstruction on internal strands only—not a crossfade between complete flames.

Codex samples it as:

$$u_{\mathrm{motion}}=\operatorname{fract}(k u-vt+\phi)$$

where $k$, $v$ and $\phi$ are T: tuneable density, speed and instance phase.

The stationary painted envelope constrains the final energy silhouette. Flight direction controls backward sweep; velocity influences texture motion without altering the blade geometry.

Check opposite-edge colour, alpha and gradient continuity. Capture T: 20 cycles at play size. If a repeated motif is obvious, increase tile variety or use a nonlooping segment.

For temporal flipbooks, select a genuinely matching source transition and disable crossfade. Compare the wrap against ordinary adjacent-frame changes. If the transition fails visually, do not loop it.

### B. Burst-in under S1

The contact flash and impact light are fully present at age zero; the whole painted body need not be.

R: flash intensity ≥95% of its peak at age zero.

T: body progressively reveals along its painted brushstroke paths over a selected 2–4-game-frame interval, then holds briefly and decays more slowly.

Use a reveal-order mask authored from the painting. Keep this independent from both the source clip's 24-fps frame selection and the erosion-order mask.

Suggested T impact sequence at R: 60 Hz:

| Age | Effect |
| --- | --- |
| 0 | Contact flash, initial ember and strike origin |
| 1–4 frames | Directional body reveal |
| 4–10 frames | Strong open brushfire shape and thin moving hot edges |
| 10–34 frames | Tip-first fragmentation, cooling roots and sparse embers |

The selected runtime animation does not need to reproduce the Firefly clip's full five-second duration.

### C. Dark backing in one premultiplied surface

Keep the existing R: `ONE / ONE_MINUS_SRC_ALPHA` blending.

For a fragment, define independent linear-space ink, body and core contributions. An appropriate starting construction is:

$$\alpha=1-(1-a_i)(1-a_b)(1-a_c)$$

$$RGB_{\mathrm{premult}}
=C_i a_i+C_ba_b(1-a_i)+C_{\mathrm{HDR}}a_c$$

Here the last term is an intentionally added thin emissive contribution; the formula is a T: shader construction, not a general physical-lighting model. Clamp/shape masks as needed, keeping their final alpha coherent. Do not multiply the final RGB by alpha again.

Keep atlas colour stored straight-alpha; perform premultiplication once in shader. Author ink separately, because black source pixels cannot reliably distinguish dark soot from empty black background.

Use narrow, broken ink regions rather than a uniform dilated contour. Preserve the existing Fire soot and Metal indigo settings initially, then tune only after side-by-side captures. Respect R: body ≤0.85–0.9 per channel and reserve HDR bloom for thin cores.

### D. Blade preservation

Retain the existing MantleSheath and R: 96×1 blade profile. The authored central channel must remain empty; energy stays beyond the blade edge with the R: 1 px gap. Keep the jade ring open and the white-jade/pale-gold appearance unchanged.

Use opaque dark steel and its hot edges to establish Fire blade readability. Do not solve unreadable steel by placing more additive flame over it.

Respect R: ≤2 overlapping transparent surfaces inside each sword region. Audit MantleSheath, MantleHull, SilkTail, glints and impostor effects with a depth/coverage diagnostic.

On key7, preserve the existing R: 88-sword structure and full flame-tongue limit of R: 14 swords per frame. Use simplified authored appearances for distant impostors instead of adding full-detail quads.

## 6. Key1 timing, sparkle and presence

### Deterministic hit events

| Sword | Required hit | Movement specification |
| --- | --- | --- |
| First | R: +18 ticks | Begin in a visible target-pointing hold. Determine departure using the measured path; enforce T4 without compressing the final flight into an unreadable jump. |
| Second | R: +36 ticks | R: depart 15–18 ticks before hit, approximately +18 to +21. |
| Third | R: +66 ticks | R: depart 15–18 ticks before hit, approximately +48 to +51. |

All damage, contact flashes, body spawns, glints and spark emissions derive from the same per-sword impact event. Avoid duplicated callbacks when VFX instances are recycled.

R: for the final 8–10 flight frames, speed is ≤12 px/frame. T4 requires ≥12 readable frames per lead sword at ≥40 px displayed length and ≤12 px/frame. The first sword's held orientation may contribute to those readable frames, provided that matches the owner's intended visual gate; log held versus moving frames separately.

If a path cannot satisfy the gate, adjust staging or departure. Do not relax the gate.

### Secondary event choreography

For every blow, spawn the required painted glints and sparks in a controlled sequence:

- R: one large four-point glint and two smaller glints, separated in time. T: large at contact; small glints at +4 and +9 frames.
- R: three spark-length families in 2–3 localized clumps; gravity affects trajectories; selected particles bounce at most once.
- R: sparse gold dust remains in the aftermath.
- R: Halo Seal appears only on big blows, not automatically on every key1 contact.
- R: every applicable item/skill shape has a presence cue: moving qi seams, breathing flame edges, a sharp glint, spark cooling, or animated seal engraving.

Presence must remain local to each object and respect the transparency and readability budgets. Avoid adding a new generic glow layer.

## 7. Rendering and anti-aliasing

Test the pinned r170 chain:

`RenderPass → UnrealBloomPass → SMAAPass → OutputPass`

Use the actual drawing-buffer dimensions for SMAA, updating on resize and verifying its lookup textures have loaded. The r170 source confirms this constructor and the composer's half-float default.  [GitHub +1]

Fallback:

`RenderPass → UnrealBloomPass → OutputPass → ShaderPass(FXAAShader)`

Update FXAA inverse resolution to the final drawing-buffer size. Verify no double colour-space conversion or unintended extra tone mapping.  [Three.js Docs +1]

R1 requires cheap AA at High. If both approaches exceed budget, reduce secondary effect cost or optimize the pipeline. Do not silently leave High without AA.

Retain the R: UnrealBloomPass threshold 1.0. Inspect actual post-bloom contributions, since the threshold applies to luminance, not effect-object identity.  [GitHub]

## 8. Measurement and acceptance

### Hard technical gates

| Metric | Required |
| --- | --- |
| C1 | Final-image ΔE OKLab ≥0.25 against actual local background, idle and in flight |
| C2 | VFX blade overlay ≤5% in flight, including fan/trail |
| Blade-keep | ≥90% lead/mid; ≥85% far, ΔE OKLab 0.04 versus aura-off |
| Jade/guard preservation | ≥95% every frame |
| Other layer overlap | No effect layer covers >10% of blade |
| Transparent surfaces | ≤2 per pixel inside sword area |
| Performance windows | p95 ≤11.5 ms each |
| Fire over Metal | p95 ≤0.85 ms |
| Metal aura on key7 | p95 ≤+0.6 ms |
| Final visual | Two independent blind judges each ≥8.5 |

For C1, render paired images at the same replay tick: final scene with effects and a true background-only reference without the sword. Lock exposure, camera, renderer and scene state. Convert display RGB to OKLab using the published transform.  [bottosson.github.io]

Freeze the blade sampling mask, treatment of antialiased edge pixels and aggregation procedure in W0. Report minimum, lower-percentile and central values separately. The brief does not define the aggregation statistic, so that is an implementation uncertainty requiring a recorded coordinator decision—not permission to change the R: 0.25 threshold.

For blade-keep, compare the aura-on frame against an aura-off frame with the same opaque sword material, otherwise the approved Fire dark-steel change could be incorrectly counted as aura damage.

For C2, use render-layer attribution for actual VFX coverage and compare aura-on/aura-off final images to identify bloom spill. Do not count native opaque blade colouring as an overlay.

Use the existing CPU + one-pixel GPU-readback harness consistently. R: evaluate idle, key1, key7 hunt, key7 finish and K5 at 1920×1080 DPR 1 High. Because GPU timer queries are unavailable, label these timings as the harness's upper-bound measurements, not pure GPU time.

### Blind review

Before submission, freeze the default lab flags, atlas hashes, renderer, camera, replay input and VFX event schedule.

Provide normal-speed play-camera videos and stills for both stone types, sword idle, flight, key1 impacts, key7 crowding and decay. Keep diagnostic close-ups separate from acceptance captures.

Each blind judge independently evaluates overall market quality, silhouette/design, motion timing, readability, lighting/sparkle and xianxia identity. R: both overall scores must reach 8.5; averaging cannot rescue a failure.

## 9. Risks and failure exits

| Risk | Check | Failure action |
| --- | --- | --- |
| Firefly deforms open crescents | Contact sheets, contour tracking, play-size composite | Preserve painted body; reuse only internal motion |
| Black-key processing destroys soot | Alpha/ink diagnostic against both stones | Use independently painted ink masks |
| Metal hides steel | Blade-keep, centre-channel inspection | Reduce plate fill, restore negative gaps |
| Loop repeats or ghosts | Boundary checks, T: 20 cycles | Rebuild tile or use nonlooping motion |
| Impact looks like C or lotus | Arc/taper tracking across entire life | Reject silhouette and recompose |
| Stars collapse into blobs | R: 12–32 px capture | Switch to authored needle LOD |
| Sparks cause visual noise | Event/particle density capture | Reduce clump size and retime, not global brightness |
| Halo becomes bangle | Play-size seal capture | Widen gaps, simplify engraved strokes |
| Key1 movement violates T4 | Per-sword frame logs | Retune staging and flight |
| Old effects remain active | Layer-attribution capture | Disable rejected lotus, spark-ray, heat-ring and procedural-scorch defaults |
| AA exceeds headroom | Full performance windows | Benchmark alternate AA and optimize effects |
| Reserved colours conflict | Palette inspection | Avoid using R: `#FF4A4A`, `#7FF5E0`, `#FFC83A` as new effect colours |

## 10. Final handoff and unresolved uncertainty

Claude's acceptance package must include: source hashes, source-to-atlas processing records, prompts, painted first/last frames, mask/channel specifications, atlas dimensions and frame mapping, event replay, default flag manifest, all hard-gate reports, blind-judge captures and individual scores.

Media remains in `art-src` synchronized to Drive, not Git. Codex's code and lightweight manifests belong in the repository. The default snapshot must load without special URL flags; the lab remains instant-cast and is not yet represented as integrated into the actual game build.

Still uncertain—and requiring direct tests—are the salvageable motion quality of `ff-m1-c4`, whether Ticket 252 v1 or v3 generates better intermediate fire motion, the final C1 sampling aggregation, target-device SMAA headroom, and whether the composed result actually reaches the two-judge R: 8.5 bar.

Final ordered decision: freeze and measure W0; run W1–W4 in parallel; integrate W5; resolve readability and AA in W6; accept only through W7.

The correction is to make the painted silhouette, reveal map, erosion map, motion source and shader alpha contract independent, testable components. This preserves the Firefly fire quality the owner approved while preventing the shape, ghosting, readability and timing failures that kept the earlier candidates at 6.5–7.


---

**[TURN · Lượt chạy 2 · Rà soát 3 (cùng lời yêu cầu) · câu trả lời của ChatGPT: FAIL (nguyên văn, 30.696 ký tự). Bản sửa trong lượt này là bản Claude đưa Gemini rà soát]**

VERDICT: FAIL

## Problems found

The previous answer preserved the main owner decisions, but it still contained implementation errors and insufficiently defined production steps. I found 12 problems.

| # | Problem | Why it matters / correction |
| --- | --- | --- |
| 1 | Incorrect premultiplied shader specification. | The proposed RGB formula added an emissive term without fully defining its alpha relationship, potentially producing inconsistent transparency, excessive bloom or incorrect compositing. Replace it with a bounded, testable ink/body/core composition rule. |
| 2 | Firefly motion extraction was treated as more deterministic than it is. | An opaque-black video does not contain recoverable, independent alpha and colour information. Separating moving fire from its generated silhouette is an approximation. Use painted coverage masks and validated motion extraction, with explicit rejection criteria. |
| 3 | The loop-generation algorithm remained underspecified. | Matching the left and right edges of a texture does not guarantee coherent moving flame features. Define period construction, phase continuity, wrapping, rejection criteria and LOD behaviour. |
| 4 | The first/last-frame strategy could still waste generations. | A complete first frame and extinguished last frame across a R: 5-second clip can encourage an unwanted long decay. Provide a Firefly-specific decision tree separating useful motion from runtime-controlled attack/decay. |
| 5 | The key-1 first-sword schedule was not executable. | The previous solution correctly retained the R: +18-tick hit but did not derive movement from actual screen-space distance. Counting a stationary hold toward T4 could also create a misleading pass. Require trajectory validation and preserve a readable moving interval. |
| 6 | The atlas contract was incomplete. | Missing concrete sampling conventions, texture wrap modes, gutter handling, origins, frame indexing and event-to-variant mapping could produce wrong frames or visual seams. Specify these in a versioned manifest. |
| 7 | C1 remained undefined as a pass/fail algorithm. | Reporting several statistics does not establish which one satisfies R: ΔE OKLab ≥0.25. The code owner must implement a deterministic comparator and explicitly document the remaining interpretation ambiguity, without silently weakening the owner's threshold. |
| 8 | C2 lacked a definite final-image interference procedure. | Layer-ID masks alone miss postprocessed bloom; image differences alone confuse opaque blade changes with overlays. Use both and report their separate contributions. |
| 9 | The sparkle/presence system lacked a safe runtime budget. | Instanced particles alone do not prevent overdraw, especially during R: 88-sword key-7. Define event grouping, LOD, spawn priority and load tests without deleting required glints from key-1. |
| 10 | The effect-replacement matrix was incomplete. | The prior plan disabled rejected effects without clearly distinguishing their visual replacements from gameplay/event functionality. Preserve damage and timing; replace only rejected visual renderers. |
| 11 | Several measurements were proposed without calibration. | Shape-opening measurements, backing opacity, timing windows and particle sizes were sometimes framed as quality guarantees. Treat them as T: screening metrics, then calibrate at the actual play camera. |
| 12 | The art-to-code handoff still lacked exact acceptance artifacts. | Workers need a documented test scene, asset checksum/manifest, capture set, failure categories and promotion rule. Without those, blind scoring cannot reliably identify the asset version being judged. |

### Source verification

I rechecked official sources and found no reason to reverse the previous decisions on the pinned renderer APIs:

- Verified: r170 `SMAAPass(width, height)` exists; the r170 `EffectComposer` default render target uses `HalfFloatType`. The current online SMAA documentation has a different constructor signature, so implementation must follow the pinned source.  [GitHub +1]
- Verified: SMAA belongs before `OutputPass`; FXAA should follow `OutputPass` because it needs display-space input.  [Three.js Docs +1]
- Verified: Adobe supports first/last-frame guidance; both frames disable camera Motion controls. Generated frames are guidance-constrained, not guaranteed to preserve the intermediate shape.  [Firefly]
- Verified: the `ONE / ONE_MINUS_SRC_ALPHA` blend factors support premultiplied-alpha compositing. Correct source RGB and alpha are still the application's responsibility.  [OpenGL Wiki]
- Verified: three.js colour images and non-colour data maps require different colour-space treatment.  [Three.js]

The previous answer's basic artistic direction was correct. The corrections below concern reproducibility, shader correctness, timing and measurable acceptance.

# Corrected full analysis and solution

Notation throughout: R = REQUIRED by the supplied brief or settled owner decision; T = TRIAL engineering/art value, subject to measurement. Numbers appearing in candidate IDs, source filenames, tool versions and package identifiers are identifiers rather than numerical requirements.

## 1. Layer decisions: what to keep, what to change

| Layer / source | Why current quality stops around 6.5–7 | Corrected production treatment |
| --- | --- | --- |
| Metal mantle `ff-m1-c4` | Solid feather/fern silhouette, white block, minimal motion, hides steel. | Retain Wind-Silk A using the existing MantleSheath and blade-width profile. Paint separated qi plates outside the edge, an open jade collar, paired silk seams and forward needle. Reuse Firefly filaments only if they remain coherent after extraction. |
| Fire sheath `ff-f1-c4` | Symmetrical flame, arrowhead root, cream wash, crossfade ghosts, insufficient directional flight. | Painted asymmetric envelope plus organic moving flame. Dark steel and hot edges remain opaque and visible; tongues bend rearward. `ff-f1-c2` may provide separate trail movement. |
| Tip star `ff-g1-c2` | Swollen centre, frame jitter, generic sparkle and poor readability at small sizes. | Replace with painted asymmetric needle/four-point/eight-arm variants. Short event timing, exact tip attachment and size-specific LOD. |
| Fire impact Ticket 252 v1/v3; `ff-a1-c5` | Near-closed C, insufficient taper, no hot line, full body at age zero, abrupt extinction. | Three authored open crescents, counter-strokes, detached licks, selective ink, thin white-gold core, fast directed reveal, hold and tip-first breakup. |
| Sparks/dust `ff-g1-c3`, `ff-b2-c1/c2` | Grinder/firework movement and stock glitter. | Original painted streaks in three lengths, localized clumps, gravity, selected single bounces, timed sharp glints and restrained aftermath dust. |
| Halo Seal `ff-c3-c3` | Bangle silhouette, stray bars and insufficient engraving. | Painted broken rings with widely spaced authored marks. Only on designated big blows, not every key-1 hit. |
| Dark backing Existing ink system | Additive wash disappears on light stone; continuous black borders look like stickers. | Authored localized ink within the same premultiplied material, no extra backing card. |
| Loops, burst, decay Existing FlipbookPool | Ghosting, complete initial body and rapid disappearance. | Periodic internal motion, event-driven body reveal, separate contact flash and authored tip-first erosion. |

The owner-approved visual identity remains fixed: Metal Wind-Silk A plus the tip star from C; Fire has dark steel, hot edges, orange-red Brushfire and Starfire accents. White jade with pale-gold rim remains unchanged.

## 2. Ordered work packages

| Order | Workers and source | Deliverable and T settings | Measure, capture and review |
| --- | --- | --- | --- |
| W0 — Baseline | Codex instruments; Claude captures. | Fixed default lab replay, asset versioning, effect-layer masks, opaque-blade reference and performance baselines. | Both stone grounds, idle/flight, key1, key7 hunt/finish and K5. Verify existing gates before modification. |
| W1 — Metal | ChatGPT/Gemini paint; Claude processes `ff-m1-c4`; Codex integrates. | Authored mantle envelope, moving filaments and LOD variants. T: exterior qi width 3–7 px at lead-sword play scale. | R blade-keep and overlap; T negative-space/shape inspection. Capture lead/mid/far and blind A/B. |
| W2 — Fire blade | Same workers; `ff-f1-c4` primary, `ff-f1-c2` trail candidate. | Asymmetric envelope, velocity-directed motion, localized soot and thin hot edges. T: exterior flame width 3–9 px. | R C1/C2, blade preservation and full flight replay on both stones. Blind A/B. |
| W3 — Secondary art | ChatGPT/Gemini paint; Claude packs; Codex integrates. | Tip-star family, spark/dust sprites and seal. T: three screen-size LODs for relevant sprites. | R glint choreography, particle behaviours, big-blow-only seal; small-size blind comparison. |
| W4 — Impact art | ChatGPT/Gemini edit v1/v3; Claude runs Firefly Video and processing. | Matched R: 1080×1080 first/last frames, extracted organic movement and independent control maps. T: two v1 generations and one v3 generation. | Inspect every selected source frame, arc openness, taper, motion stability and decay shape. |
| W5 — Integration | Codex implements; Claude validates. | Impact card, reveal/erosion, sparks, glints, event scheduling; disable rejected visual layers. | R hits +18/+36/+66 ticks, no duplicate damage, overlap and frame-by-frame decay. Blind integrated A/B. |
| W6 — Readability/AA | Codex; Claude measures. | T1/T4 movement, C1/C2 comparator and R1 cheap AA at High. | Movement-frame logs, final-image gates, five performance windows and default snapshot. |
| W7 — Acceptance | Claude coordinates two blind judges; owner signs off. | Locked default version, metric files, captures, hashes and final manifest. | Both judges individually R: ≥8.5, plus every hard gate. |

Parallel dependency: W1–W4 run concurrently after W0. W5 consumes approved W3/W4 assets. W6 follows the integrated aura; W7 follows the complete default configuration.

## 3. New art — complete production prompts

All artwork is original. ChatGPT/Gemini handle painting and image edits; Codex does not generate images. Do not upload third-party reference images into AI tools.

### Painted images

Impact first frame — Ticket 252 v1, primary

> Edit the attached Ticket 252 v1 artwork. Preserve its three beautiful nested flame crescents and recompose them into an opaque pure-black 1080×1080 square without stretching. Center the overall composition, retaining a lower-left strike origin and an open upper-right sweeping fan. Three distinct strokes have thick irregular roots tapering to long needle tips, with generous gaps. Add four or five smaller opposing brushstrokes, detached licks, sparse glints, thin white-gold leading edges occupying no more than 5% of the luminous design, and localized burnt-ink undersides. Orange-red stepped anime/donghua painting. No C-shaped closure, V/bird, lotus, sticker edge, haze or scenery.

Impact alternative — Ticket 252 v3

> Edit the attached Ticket 252 v3 only. Preserve its two long elegant fire crescents and shorter counter-stroke, refining them into three unmistakably distinct open brushfire strokes. Recompose into an opaque-black 1080×1080 square, centered overall, with a lower-left impact origin. Keep long tapering tips, uneven heavy roots and large negative gaps. Add four or five smaller counter-strokes, detached flames, sparse glints, a very thin white-gold edge and dark ink underneath selected roots. Luxurious orange-red stepped anime/donghua flame. No closed ring, bird silhouette, symmetrical lotus, smoke or scenery.

Impact last frame — matched edit

> Edit the approved first frame, preserving the exact canvas, impact origin, stroke directions, identities and arrangement. Show the SAME fire crescents at the end of their life: needle tips torn into separated fragments, middle sections split into irregular islands and surviving thick roots cooling to dark orange-red. Only a few embers remain along the original motion paths. Nearly all white-gold brightness is gone. The remaining fragments must clearly belong to the original three strokes. Opaque pure-black 1080×1080. No new fire strokes, rings, explosions, smoke or scenery.

Metal mantle envelope

> Paint original horizontal xianxia sword-qi texture artwork on pure black. An invisible sword occupies the empty central channel; do not draw the sword. Two unequal banks of separated silver-blue qi plates hug OUTSIDE its edges with narrow black gaps. Paint fine indigo seams, delicate silk strands and open negative spaces. The hilt collar stays open around the white-jade ring. Two flowing seams converge beyond the tip into a sharp needle, with a sparse silk tail extending backward. Elegant layered anime/donghua energy, crafted and lightweight, not an opaque object. No feather, fern, wings, solid white blocks, fog or bloom blanket.

Fire sheath envelope

> Paint original horizontal sword-flame envelope artwork on pure black, leaving a clearly empty central channel for an invisible dark-steel sword. Unequal orange-red flame banks run outside the blade edges. Organic tongues sweep backward toward the hilt, with several slender trailing ribbons and a forward needle tip. Avoid symmetry and any triangular arrowhead at the hilt. Strong calligraphic taper, irregular licks, dark soot under selected roots and exceptionally thin white-gold hot edges. Stepped anime/donghua fire, rich handcrafted detail. No blade, flat glowing slab, symmetric wings, smoke, haze or scenery.

Tip-star sheet

> Paint isolated original xianxia sword-tip glints in separated sprite-sheet cells on pure black, with generous gutters. Include a slender needle streak, unequal four-point star, eight-arm star with four long and four extremely thin diagonal arms, sharp tiny cores and fragmented dying glints. Provide shapes suitable for small gameplay display, not simply scaled-down large stars. White-gold with restrained pale-orange detail and localized broken dark backing. No swollen core, stock emoji sparkle, symmetrical diamond, lens flare, glitter haze, scenery or text.

Spark/dust sheet

> Paint original isolated anime fire-spark sprites on pure black. Include short needle sparks, medium curved streaks and long fast streaks, all separated by wide gutters. Each has a tiny white-gold head, a narrow orange body and a cooling dark-red tapered tail. Include small directional clumps, irregular ember chips, a few impact-bounce fragments and very sparse gold-dust flecks. Shapes are sharp, lightweight and designed for moving trajectories. No radial firework, metal-grinder shower, stock glitter, round glowing beads, smoke or scenery.

Halo Seal

> Paint an original xianxia Fire halo seal on pure black. Several hair-thin broken golden-orange concentric rings with deliberate wide gaps and nonmatching break positions. Add sparse engraved rune-like segments, short radial notches and selective needle glints. Keep the ring structure circular and clearly separated when reduced to gameplay size. Place subtle burnt-ink backing beneath selected engravings, never around the entire circle. Luxurious mythic graphic design. No thick bangle, complete glowing disc, dense illegible text, smoke, lens flare or scenery.

### Adobe Firefly Video

All three prompts are below R: 600 characters. Generate with the Adobe model, using the proven R: opaque-black square image-to-video route. Keep original source clips for processing.

Fire sheath internal motion

> Thin living orange-red flames flowing along an invisible horizontal sword, with unequal tongues on both sides and a clear dark central channel. Tongues sweep backward from a needle-sharp leading tip, stretching, curling, splitting and retracting in irregular rhythms. Rich hand-painted anime flame motion, stepped warm colours and occasional hair-thin white-gold heat streaks. Fixed view, pure black background. No sword, symmetric wings, thick blob, radial burst, smoke cloud, haze or text.

Metal silk internal motion

> Separated silver-blue silk energy strands flowing lengthwise beside an invisible horizontal sword. Fine indigo threads peel outward, gently weave and reconnect toward a forward needle. Small silver highlights travel along individual strands at varied speeds, preserving clear black gaps. Graceful hand-painted xianxia energy, delicate and lightweight. Fixed view, pure black background. No sword, feather, fern, wings, solid white plates, smoke, haze or text.

Fire impact — first/last-frame guided

> Three OPEN curved brushfire strokes erupt rapidly from a lower-left strike origin and sweep upward and right. Heavy orange-red roots taper into long needles, followed by small opposing strokes and detached flame licks. Thin white-gold heat traces travel along leading edges while dark burnt ink preserves shape. A fast attack, brief strong shape, then tips tear into irregular curling fragments and cooling embers. Fixed view, pure black background. No closed circle, lotus, bird shape, smoke veil, haze or text.

Generation decision: inspect the original R: 24-fps, 5-second clips first. Use the Firefly output for internal motion only if it breaks the approved impact silhouette. Adobe's documented first/last-frame guidance does not establish intermediate geometric accuracy.  [Firefly]

## 4. Exact asset and shader contract

### A. Source processing

Claude performs these operations in order:

1. Preserve the original clips and hashes. Extract every source frame with FFmpeg; inspect the complete sequence before choosing an interval.
2. Register the sword's longitudinal axis or the impact's strike origin. Reject frames with large shape discontinuities.
3. Create the authoritative painted silhouette and separate coverage, ink, core, reveal and erosion maps.
4. Extract useful Firefly motion through masking and image analysis. Treat any alpha derived from opaque black as an approximation, never as recovered ground-truth transparency.
5. Pack colour and control textures separately, with gutters and transparent-edge RGB dilation.
6. Generate independent lead/mid/far variants. Composite each against both actual game stones.
7. Save source, processing parameters, anchors, atlas layout, colour-space flags, dimensions and hashes.

T: versioned manifest fields: `id`, `sourceHash`, `kind`, `frameCount`, `fps`, `columns`, `rows`, `variantMap`, `anchorUV`, `worldSize`, `colorAtlas`, `controlAtlas`, `timingAtlas`, `colorSpace`, `alphaMode`, `loopMode`, `lod`.

For old assets, missing fields must preserve current FlipbookPool behaviour. New approved variants explicitly override crossfade and loop settings.

The painted envelope and blade-profile textures use blade-local UVs. Atlases use clamped sampling with gutters; only verified periodic motion textures use longitudinal repeat. Do not enable `RepeatWrapping` on a multi-frame atlas.

### B. Packed channel conventions

| Texture | Channel interpretation |
| --- | --- |
| Colour atlas | Straight-alpha colour; RGB is display-authored sRGB, with preserved coverage alpha. |
| Control A | R: body coverage; G: localized ink; B: HDR-core coverage; A: erosion survival order. |
| Timing B | R: directional reveal order; G: motion influence; remaining channels unused unless validated. |
| Motion texture | Periodic longitudinal flame/silk variation; independent of the painted silhouette. |
| Existing blade profile | R: 96×1 half-width information, retained unchanged. |

Control-map channels are data, with `NoColorSpace`; colour images use `SRGBColorSpace` and are converted before linear-space composition.  [Three.js]

### C. Premultiplied composition — corrected

For a fragment, define effective ink, body and thin-core coverage $a_i,a_b,a_h$, each bounded to the valid alpha range, with colours $C_i,C_b,C_h$ in linear RGB.

One T: starting model for ink underneath body underneath the hot core is:

$$\alpha=1-(1-a_i)(1-a_b)(1-a_h)$$

$$RGB_p=C_i a_i(1-a_b)(1-a_h)+C_b a_b(1-a_h)+C_h a_h$$

Output $(RGB_p,\alpha)$ with the existing `ONE / ONE_MINUS_SRC_ALPHA` factors.

This is an ordered artistic composition, not a claim of physically simulated lighting. HDR $C_h$ is allowed above display range only in the approved thin-core region. Never premultiply the resulting RGB a second time.

T: localized ink alpha 0.25–0.5, under selected roots and inner curves. Do not generate a continuous outline. Preserve the R: body-channel ceiling 0.85–0.9 and existing Metal indigo / Fire soot treatment as starting settings.

Codex must render unit-test swatches against both stone backgrounds and compare GPU output with a CPU reference for zero, partial and full coverage. This is a hard implementation check, not a visual preference.

## 5. Loops, burst and decay

### Seamless motion

For the mantle/sheath, the approved envelope is stationary in blade coordinates; only internal detail moves.

Claude constructs a periodic spatial motion tile by selecting compatible strands, repositioning or repainting boundary-crossing details and matching opposite-edge values and slopes. Arbitrarily crossfading complete Firefly images is prohibited.

Codex advances sampling continuously:

$$u'=\operatorname{fract}(ku-vt+\phi)$$

Here $k,v,\phi$ are T: tuneable repeat density, velocity and per-sword phase.

The painted envelope constrains the final visible area. Trial validation: inspect T: 20 cycles, both stones, and screen sizes from R: 60–130 px. Reject visible seams, repeated static motifs or sudden shape jumps.

A genuinely matching temporal loop may use stepped playback with no crossfade. Otherwise treat the source as a one-shot. `minterpolate` is optional for limited motion interpolation, never a substitute for shape continuity.  [FFmpeg]

### Impact event timing

| Impact age, R: 60-Hz simulation | Behaviour |
| --- | --- |
| R: age 0 | Contact flash and impact light at ≥95% of peak. Body need not be complete. |
| T: frames 1–3 | Reveal the approved body along painted stroke directions. The R: permitted reveal window is 2–4 frames. |
| T: frames 4–9 | Strong open Brushfire shape; internal tongues continue moving. |
| T: frames 10–34 | Tips tear first, then counter-strokes, then roots; cooling and sparse embers persist. |

Reveal and erosion are separate authored scalar fields. For example, a fragment can appear when its reveal-order value is reached and disappear when its survival-order threshold is crossed. Its painted colour remains intact while surviving.

The runtime does not need to replay the full Firefly source duration. Slow decay is achieved through independently breaking strokes, not by uniformly reducing the whole card's opacity.

## 6. Key-1 movement, secondary effects and LOD

The hit scheduler, not VFX playback, owns damage and timing.

| Sword | R impact tick | Departure rule |
| --- | --- | --- |
| First | +18 | Hold pointing at the target, then begin a measured flight early enough to preserve readable moving frames. Choose departure from actual projected distance, not a guessed fixed tick. |
| Second | +36 | R: departure 0.25–0.3 s before impact, approximately +18 to +21 ticks. |
| Third | +66 | R: departure 0.25–0.3 s before impact, approximately +48 to +51 ticks. |

For every lead sword, R: ≥12 frames at ≥40 px displayed length and ≤12 px/frame. The final R: 8–10 flight frames must also remain ≤12 px/frame. Log held frames separately; T: require the readability check to pass using moving frames, preventing an artificial pass from a long stationary hold.

If the available projected travel distance makes the first sword impossible to stage within its new +18-tick window, adjust its initial placement, pose or path. Do not shift the settled hit tick.

At each impact, damage, contact flash, sound and effect spawns share one uniquely identified event. Event replay and recycling must not produce duplicate damage.

Sparkle choreography: R: one large four-point star and two smaller stars in sequence per blow; T: at contact, +4 frames and +9 frames. R: three spark lengths, 2–3 localized clumps, gravity, selected maximum-one-bounce particles and sparse residual dust. Avoid the reserved R: `#FF4A4A`, `#7FF5E0` and `#FFC83A` as new effect colours.

Presence cues must be specific: silk-thread motion for Metal, living flame edges for Fire, a sharp point/rotation for glints, cooling heads for sparks and moving engraved highlights for the seal. They should not all become the same glowing outline.

Keep R: key-7's 88 swords and existing full-tongue allocation of 6 lead plus 8 mid. Use simplified authored LODs for distant swords. Apply particle pooling and prioritize visible impact events and required key-1 glints before optional dust. Do not meet performance targets by deleting mandatory impact events.

The existing key-1 lotus card, rejected spark-ray look, analytic heat-ring visuals, procedural ground seal and code-drawn scorch should be disabled in the accepted default, while their gameplay/event responsibilities are preserved. A painted ground mark is a separate optional visual candidate, never an automatic replacement.

## 7. Anti-aliasing, measurements and blind judging

R1: test `RenderPass → UnrealBloomPass → SMAAPass(width,height) → OutputPass` against `RenderPass → UnrealBloomPass → OutputPass → ShaderPass(FXAAShader)`.

The r170 SMAA source confirms its constructor and resize behaviour; FXAA uses an inverse-resolution uniform. Use actual composer drawing-buffer dimensions.  [GitHub +1]

Do not combine both AA passes by default. Test actual play-camera quality and the complete performance envelope. The R: bloom threshold remains 1.0; only narrow HDR cores should contribute significantly.

### Measurement contract

| Hard gate | Implementation and report |
| --- | --- |
| C1 | R: final-image OKLab ΔE ≥0.25 against local real background, idle and flight. Freeze same-frame background-only reference, blade-interior sampling and colour conversion. T: use the lower-decile ΔE within each registered opaque-blade region as a conservative screening comparator; report min, median and region coverage too. This statistical choice is not an additional owner-approved rule. |
| C2 | R: aggregated VFX coverage ≤5% of blade in flight, including fan/trail. Combine overlay-attribution masks with final-image bloom-spill diagnostics; report separately. Do not count opaque Fire blade colouring as overlay. |
| Blade-keep | R: ≥90% lead/mid and ≥85% far within ΔE OKLab 0.04 of the aura-off image. Use the identical opaque blade material in both images. |
| Jade and guard | R: ≥95% preserved every frame, with no effect layer covering >10% of the blade. |
| Surface overlap | R: ≤2 transparent surfaces per pixel within each sword region; audit MantleSheath, Hull, Tail and crossing particles. |
| Performance | R: each window p95 ≤11.5 ms; Fire over Metal ≤0.85 ms p95; Metal aura on key-7 ≤+0.6 ms p95, at High R: 1920×1080 DPR 1. |
| Acceptance | R: both blind judges individually ≥8.5 at the default skills-lab play camera, without URL flags. |

For C1, use the published Oklab transform on final display-referred RGB; do not calculate Euclidean Oklab distance directly on gamma-encoded sRGB.  [bottosson.github.io]

The C1 lower-decile aggregation is a T implementation interpretation, because the brief specifies the threshold but not a statistic. Record it explicitly and report the complete distributions. Do not silently substitute a convenient average for the required threshold.

The performance harness is the existing CPU-plus-one-pixel-readback upper-bound measurement, not a pure GPU timer. Capture idle, key1, key7 hunt, key7 finish and K5 using identical deterministic replay inputs.

For final judging, prepare anonymized normal-speed video and stills on both grounds, plus a separate technical close-up set. Judges should not know which candidate is newer. Accept only after every hard gate passes; no averaging between the two judges.

## 8. Principal risks and failure exits

| Risk | Check | Exit |
| --- | --- | --- |
| Painted impact loses its open arcs in Firefly | Full-frame inspection and T arc/taper contour measurements | Keep painted silhouette; extract motion only. |
| Black source produces false alpha or loses dark soot | Composite checks against both stones, CPU/GPU swatches | Use authored coverage/ink rather than black-key alpha. |
| Sword disappears under the mantle | Blade-keep, C1/C2 and small-size captures | Reduce envelope coverage; adjust opaque steel contrast. |
| Loop ghosts or repeats visibly | Edge/gradient tests and T: 20-cycle capture | Rebuild periodic detail or use one-shot. |
| Seal becomes a bangle; star becomes a dot | Normal gameplay-size captures | Simplify LOD silhouette rather than increasing bloom. |
| Particles overwhelm crowded combat | Per-layer overlap, counts and all performance windows | Reduce optional residuals, simplify LOD and optimize instancing. |
| Key-1 misses movement-readability gates | Projected path/frame logs | Change staging and path, not hit ticks. |
| Current procedural effects accidentally remain | Visual-layer enable/disable audit | Disable rejected visual renderers while retaining events. |
| AA exceeds budget | Full High performance capture | Compare SMAA/FXAA; optimize effects before acceptance. |

## 9. Final deliverable and uncertainties

Claude's integration package must contain the immutable Firefly clips, painted artwork, extracted colour/motion atlases, channel schemas, prompts, processing commands, hashes, versioned manifest, deterministic replay data, hard-gate results, default-snapshot captures and individual blind-judge scores.

Media stays in `art-src` synchronized to Drive; only code and lightweight metadata belong in Git. The skills lab remains instant-cast, and promotion to the actual game build is outside this acceptance step.

The unresolved empirical questions are the usable filament content of `ff-m1-c4`, the quality of Ticket 252 v1 versus v3 intermediate Firefly motion, the visual suitability of periodic sheath motion, the performance cost of AA, and whether the combined effect reaches R: 8.5. The C1 aggregation convention also remains a documented methodological interpretation, not a change to the settled threshold.

Final production order: W0 baseline → W1/W2/W3/W4 in parallel → W5 integrated effects → W6 readability/AA → W7 locked two-judge acceptance.

The corrected plan keeps Firefly's already-approved organic fire quality while making the painted silhouette, motion, reveal, erosion, premultiplied backing, event timing and acceptance measurements independently testable.
