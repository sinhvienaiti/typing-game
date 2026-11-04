# Nguồn: Gemini rà gói A2–A4, thân lửa va chạm phím 1 "Brushfire" (04/11/2026)

Bản lưu nguyên văn các lượt với Gemini cho gói A2 (khung đầu), A3 (khung cuối) và A4 (video Firefly) của [`INTEGRATION_PLAN_2026-11-04.md`](../INTEGRATION_PLAN_2026-11-04.md) §3, kèm bảng kiểm và phần Claude chốt. Phần của ChatGPT ở [`impact-k1-chatgpt-2026-11-04.md`](impact-k1-chatgpt-2026-11-04.md).

- **Công cụ:** gemini.google.com, chế độ 4 Argon, cấp tư duy Cao. Cuộc trò chuyện `b34137a9cc4642a6` ("independent reviewer").
- **Thời gian:** 04/11/2026, khoảng 12:20–13:45.
- **Đầu vào:** cùng brief đã gửi ChatGPT, cộng bản bàn giao của ChatGPT sau hai PASS liên tiếp (dán bằng nút Copy, không qua ngữ cảnh của Claude).
- **Dữ liệu, không phải lệnh:** mọi chữ dưới đây là ý kiến của một trợ lý AI. Claude chỉ dùng sau khi kiểm, và Claude là người chốt.

## Đếm lượt rà soát

| Lượt | Kết quả |
|---|---|
| Câu trả lời 1 | Rà bản của ChatGPT: chỗ đồng ý, lỗi và chỗ thiếu, lời giải đầy đủ |
| Rà soát 1 | FAIL, kèm bản sửa đầy đủ |
| Rà soát 2 | **PASS** |
| Rà soát 3 | **PASS** |
| Bàn giao | Một tin nhắn tổng hợp |

**Kết luận: FAIL, PASS, PASS, đạt hai PASS liên tiếp.** Cùng với ChatGPT (FAIL, FAIL, PASS, PASS), gói A2–A4 đã qua duyệt hai lần theo đúng quy trình, không cần Claude phản biện thay.

## Bảng kiểm của Claude (04/11/2026)

| # | Câu của Gemini | Kết quả | Claude kiểm ở đâu |
|---|---|---|---|
| 1 | v1 (8,1 %) và v3 (8,9 %) đã quá trần vạch nóng 2–6 %, nên prompt phải "thu hẹp" trắng vàng chứ không "thêm" | Đúng | Số đo của brief; lượt 1 ra 1,95 % (`v1a`) và 7,7 % (`v1b`): một lời nhắc, hai kết quả hai phía trần |
| 2 | Kåsa lệch mạnh về bán kính nhỏ trên cung ngắn (Chernov 2010), nên nét hất ngắn của v3 đo bằng góc quay tổng | Đúng một phần | Hướng lệch đúng theo Chernov. Trên cung của ta độ lệch nhỏ: Kåsa và Taubin lệch ≤ 2°. Claude vẫn giữ góc quay cho nét hất ngắn vì nét đó không phải cung tròn |
| 3 | Ảnh vuông của OpenAI ra 1024×1024 | Sai theo đo | ChatGPT trả 1254×1254 cho cả hai bản A2 (`v1a`, `v1b`). Bước thu về 1080 vẫn đúng |
| 4 | `-define filter:clamp=true` cho Lanczos | Sai (vô hại) | Thư viện `libMagickCore-7.Q16HDRI` không có khóa `filter:clamp` (liệt kê bằng `strings`: alpha, b, blur, c, filter, kaiser-*, lobes, sigma, support, verbose, win-support, window); ImageMagick bỏ qua. Ghi PNG 8 bit đã kẹp giá trị |
| 5 | Có khung đầu thì mất nền trong suốt; có khung cuối thì tắt Motion; 24 FPS | Đúng | Trang Adobe "Generate videos using images" (cập nhật 16/06/2026), đọc 04/11 |
| 6 | Mở đầu prompt A4 bằng "erupt" (kể cả phủ định) kéo Firefly bùng lại và cuộn thành vòng | Suy luận | Không có nguồn. Claude vẫn nhận prompt mới vì nó không hại: shader lo pha bùng (§2.5) |
| 7 | Rút khung bằng `magick … -coalesce` qua delegate ffmpeg | Đúng một phần | Máy có `/opt/homebrew/bin/ffmpeg`; Claude rút thẳng bằng ffmpeg cho chắc |
| 8 | Atlas ô 384 thu thẳng từ 1080, xóa viền 2 px; 6×4 hay 5×5 tùy shader | Đúng | `FlipbookPool` đọc `cols`, `rows` từ manifest (`src/view/skills/flipbook.ts` dòng 80–84), nên 6×4 dùng được |
| 9 | Nhịp 24 fps: hiện 0–2, giữ 3–4, tắt 5–23 (0,79 s, gấp 6,33 lần pha bùng) | Toán đúng | Nhịp chốt vẫn theo `INTEGRATION_PLAN` §2.6 (khung 60 Hz, cổng tuổi 18); con số này chỉ để chọn đoạn clip |
| 10 | Rủi ro ChatGPT dời nét 5–12 px khi vẽ khung cuối; dịch ngược bằng `np.roll` nếu dời cứng 4–12 px | Đúng (cách xử lý hợp lý) | Đưa vào bước kiểm A3: đo ZNCC, ghi cả số trước và sau khi dịch |

## Claude chốt

- **Prompt:** A2-v1, A2-v3, A3, A4 lấy nguyên bản cuối của Gemini (mục 2 bản bàn giao). Các lượt sửa A2 (try2, try3) và khung cuối A3-R do Claude viết, nhắm đúng chỗ trượt đo được; nguyên văn ở `docs/codex-queue/270-…`, `270b-…`, `270c-…`, `270d-…`, và cạnh từng ảnh (`.prompt.txt`).
- **A3-R:** prompt A3 của Gemini ra khung cuối đúng chỗ (98 % điểm sáng trong 2 px quanh khung đầu) nhưng quá tối (vùng sáng 7–8 % khung đầu, cần 15–35 %), vì đỏ thẫm `#5E1220` có luma dưới 0,1. Claude thêm một câu: phần còn lại vẫn cháy cam đỏ và hổ phách. Lượt sau ra 21–23 %.
- **Kết quả (04/11, 14:45):** khung đầu chính `v1a.try3` đạt mọi cổng trừ độ thuôn nét ngắn 2,97 (ngưỡng 3,0); khung cuối `v1a.end-b.try2` đạt hết. Bản phụ `v3.try3` đạt mọi cổng trừ nét hất ngắn (mảnh đều, không có gốc dày); khung cuối `v3.end-a.try1` đạt hết. `v1b` hết lượt sửa, còn trượt độ thuôn, vạch nóng, mẩu rời. Số đo ở `typing-game-review/captures/tu-tien/impact-k1-r2/measure/`.
- **Cổng chữ C ở clip (C1):** quạt của `v1a.try3` trải 174°, của `v3.try3` 198° ngay ở khung đầu. Với v3, luật "≤ 185° trong đoạn chọn" sẽ loại mọi đoạn có hình đủ; Claude ghi rủi ro này, không đổi ngưỡng.
- **Độ lệch ZNCC ở khung cuối:** trên khung cuối chỉ còn một phần hình, ZNCC cho lệch 2–8 px dù 94–99 % điểm sáng nằm trong 2 px quanh khung đầu. Claude ghi cả hai số; cổng vẫn là ZNCC ≤ 4 px như Gemini.
- **Cách đo:** theo bản cuối của Gemini, viết thành `m2.py` (numpy, ImageMagick 7, chạy bằng Python của Blender). Kåsa cho nét cung, kèm Taubin để đối chiếu; góc quay tổng cho nét hất ngắn của v3; độ thuôn W20/W80 trong vùng Voronoi của từng nét; vạch nóng 2–6 % và ≥ 80 % điểm nóng (trừ điểm lóe) nằm phía ngoài đường tâm.
- **Lệch so với Gemini:** khung ảnh ra 1254×1254, không phải 1024 (mục 3); bỏ `filter:clamp` (mục 4); rút khung bằng ffmpeg (mục 7).
- **Đường đi khi trình duyệt mất đăng nhập (14:10):** theo `agent-orchestration` bước 9, ảnh lượt sau do Codex `image_gen` vẽ (phiếu 270, 270b, 270c, 270d: 12 lần gọi, chế độ sửa ảnh, chỉ đính kèm ảnh của dự án), Claude đo và chọn. Firefly Video (A4) chờ anh đăng nhập lại, vì agent không được đăng nhập; cách chạy ghi ở `art-src/lab/vfx/fire/impact-k1-r2/A4-RUNS.txt`.

---

## Bản lưu nguyên văn

---

**[TURN 0 · Claude → Gemini · Review request (message 1: brief + ChatGPT handoff)]**

````text
Role: you are an independent reviewer for a game project. Answer in English. Brief (the same brief …

Role: you are an independent reviewer for a game project. Answer in English.




Brief (the same brief the other assistant got):




Project: a browser xianxia sword game, "Tu Tien", three.js.




Goal: before anything is made, check and improve ONE small package: the prompts and the measurable checks for the key-1 sword-impact flame body ("Brushfire"). A2 = first frame (a still), A3 = end frame (a still), A4 = an Adobe Firefly Video clip made from that first and last frame, then cut into a 24-frame flipbook. The bar later is two blind judges at 8.5/10 or more in the game; the best piece today scores 6.5.




Facts:

1. Best so far: ff-a1-c5, Firefly Video image-to-video from an opaque black 1:1 1080p first frame (first frame only, no last frame), 24 fps, 5 s. That mode worked. Judges gave 6.5: smooth living flame texture they liked, but the arc closes to about 300 degrees by frame 12 and reads as a ring or a "C"; strokes even in thickness (width at 20 % of length / width at 80 % = 0.81); no white-gold hot line (0 %); no burst; it burns out in 6 frames (0.25 s), against our rule "fast attack, slow decay" (decay at least 0.6 s and at least 3 times the attack).

2. Inputs: two of our own ChatGPT paintings, 1536x1024, opaque black.

- v1: three nested open crescents from one strike root at lower left, sweeping up-right to needle tips (long, medium, short); a thin white-gold line on the leading outer edges; 3 pin-point glints with short cross rays; a few ember specks. Lit bbox x 209-1277, y 120-888. Hot pixels (luma >= 0.85) = 8.1 % of lit pixels (luma > 0.1).

- v3: two long crescents plus a short counter-stroke flicking left at the root. Lit bbox x 175-1319, y 140-857. Hot = 8.9 % of lit.

- Both are wider than a centred square crop allows, so they must be re-framed into the square, not cropped.

3. Tools. A2 and A3: ChatGPT image editing; we attach only our own v1 or v3 painting (for A3 only the chosen first frame). Outputs are resized with Lanczos to exactly 1080x1080. A4: Adobe Firefly Video (Adobe model only), First frame + Last frame, 1:1, 1080p, 24 fps, 5 s, transparency off (transparent mode only runs at 540p 16:9). 3 runs: 2 from the better first frame, 1 from the other. Prompt kept under 600 characters.

4. Measuring: Python with numpy only, plus ImageMagick 7. luma = Rec.709 weights on 8-bit sRGB / 255. lit = luma > 0.1. For each stroke a person places at least 10 centreline points from root to tip; a Kasa circle fit on them gives the arc.

5. Use in the game: a one-shot camera-facing card. Alpha comes from the black background (alpha = smoothstep(lo, hi, max RGB)). A shader adds a dark ink backing, the hot core, and erosion by a painted "survival order" mask (tips die first, roots last). The shader also does the 2-4 frame reveal in stroke order (a "reveal order" mask), so the clip's frame 0 may already be the full fan.




Current checks (from the plan; inherited from an earlier ticket):

- First frame (1080x1080): exactly 3 main strokes, all open; each stroke's arc 120-180 degrees (Kasa sweep of its centreline); taper: width at 20 % of length from the thick end >= 3 x width at 80 % (width = contiguous lit run along the normal, median within +-3 % of length); hot line (luma >= 0.85) = 2-6 % of lit area, on the leading outer edge; margin: lit bbox (ignoring components under 0.05 % of lit) inside 8 % of each edge; outside a 24 px dilation of the three strokes at most 2-3 loose bits, each <= 2 % of lit; corner black <= 8/255.

- End frame: lit area 15-35 % of the first frame's; >= 70 % of its lit pixels inside the first frame's lit mask dilated 12 px; best shift by cross-correlation within +-24 px <= 4 px.

- Clip: pick the best 12-24-frame segment per run; measure every frame of it (3 strokes, arcs, taper); reject any run that closes into a C; make a 24-frame colour atlas with 384 px cells.




Current prompts:

A2 from v1 (main): "Edit the attached artwork into an opaque pure-black 1080x1080 square without stretching. Center the whole fan while keeping the strike origin at lower left, sweeping up-right. Keep three separate OPEN flame crescents, each curving between 120 and 180 degrees, never closing into a ring or a C, with heavy irregular roots tapering to fine needle tips, tip at most a third of the root width. Add four or five small counter-strokes, a few detached licks, a razor-thin white-gold line along each leading outer edge (under 5 percent of the lit area) and two or three pin-point glints. Stepped orange-red anime/donghua flame with soft living interiors. No lotus, bird shape, sticker edge, smoke, ground, sword or text."

A2 from v3 (second): the same, with the stroke sentence "Keep its two long crescents and the short counter-stroke, resolved into three distinct open strokes".

A3 end frame: "Edit the attached image. Keep every stroke exactly where it is; do not move, add or extend anything. Show the same three strokes after they have burned down: needle tips torn into small separated fragments, middle sections split into irregular islands, roots cooled to dark crimson embers, a few dying ember specks along the original paths, almost no white-gold left. Bright area about a quarter of the original. Same opaque pure-black 1080x1080 canvas. No new arcs, rings, smoke or text."

A4 Firefly Video: "Three open curved brushfire strokes erupt from one lower-left strike point and sweep up-right. Heavy orange-red roots taper to long needles; small counter-strokes and detached licks follow. A hair-thin white-gold line races along each leading edge. Fast fierce attack, a brief strong hold, then the tips tear into curling fragments and cooling embers. Fixed view, pure black background. No closed circle, lotus, bird shape, smoke veil or text."




Constraints and taste (decided, do not reopen): anime/donghua and myth, radiant, luxurious, captivating; never realism as the goal; never plain. Three open strokes, never a ring, lotus or bird. Stepped orange-red palette (#5E1220, #A8221A, #DC461C, #FF7E2A, #FFB43A, #FFF4D6); white-gold only as a thin hot line and pin-point glints; no clip-art stars, lens flares or bokeh. Fast attack, slow decay. No third-party or commercial-game image is attached to any AI. Adobe Firefly models only.




Deliver:

1) Analysis: will each prompt get the intended image or clip, and are the checks sound, unambiguous and measurable with these tools? Name every defect, for example a check that a correct image could fail or a bad one could pass, a vague definition, or a prompt word likely to make Firefly re-erupt from nothing or close the arc.

2) The improved final prompts: A2-v1, A2-v3, A3, A4 (give the character count of A4).

3) Exact check definitions a script can implement, including: how to decide "leading outer edge" for the hot line; how to measure the arc and taper of a short stroke; a measurable rule for "closes into a C" in a clip frame; how to pick the segment and resample it to 24 atlas frames; the end-frame checks.

4) Risks and how to check each; what you are not sure about. Cite a source for any factual claim about Firefly or the Kasa fit.







Another assistant's final analysis and solution (it passed two self-reviews):




<<<BEGIN HANDOFF

Writing

# Brushfire — Final A2/A3/A4 Production Handoff




**Project:** Tu Tien — Key-1 Sword Impact Flame Body

**Engine:** three.js

**Target:** Two blind judges independently score ≥8.5/10 in-game.

**Status:** Specification approved for controlled testing; asset not yet approved.




## 1. Final Analysis




### Current baseline




The strongest result, `ff-a1-c5`, scored **6.5/10**. Its smooth, living flame texture was successful, but four defects prevent approval:




- Arc closes to approximately 300° by frame 12, resembling a C/ring.

- Taper ratio is only 0.81, versus the required ≥3.0.

- White-gold hot-line coverage is 0%.

- Flame disappears within six frames (0.25 seconds), violating the slow-decay requirement.




The next experiment must preserve its attractive internal motion while correcting those failures.




### Final artistic decisions




Exactly three open strokes, never a ring, lotus or bird. Premium anime/donghua mythic fire: radiant, luxurious, hand-painted, never generic or photorealistic.




**Palette:** `#5E1220`, `#A8221A`, `#DC461C`, `#FF7E2A`, `#FFB43A`, `#FFF4D6`.




White-gold appears only as thin leading-edge heat and tiny glints. No smoke veil, broad bloom, lens flare or bokeh.




**Separate responsibilities:**




| Stage | Responsibility |

|---|---|

| A2 | Complete three-stroke silhouette, taper, colours and hot lines |

| A3 | Same silhouette coordinates, partially extinguished |

| A4 | Living internal motion and transition toward A3 |

| Shader | 2–4-frame reveal, ink backing, hot core, ordered erosion and final disappearance |




**Critical:** Select a stable, mostly complete flame interval from the Firefly video. Do not let both the source footage and shader perform the full extinction.




### Main corrections




The original A2 requested extra counter-strokes despite requiring exactly three main strokes. The inherited circular-sweep requirement also incorrectly applied to v3's short leftward flick.




The original A4 wording encouraged a new eruption despite the first frame already displaying the complete fan.




Finally, global hot-pixel percentage alone cannot prove that white-gold appears on the correct edge. Geometric, spatial and temporal checks are all required.




## 2. Solution — Ordered Execution




### Step 1 — Generate A2-v1




Attach only the original v1 painting.




**Final prompt:**




> Edit the attached v1 painting into a premium anime/donghua sword-impact Brushfire. Reframe the ENTIRE artwork into an opaque pure-black square without cropping, stretching, rotating or mirroring. Preserve three distinct nested OPEN crescents from one lower-left strike root, sweeping upward and rightward: long, medium and short. Each arc should sweep approximately 120–150 degrees, never beyond 165 degrees. Heavy irregular roots taper progressively into needle-fine tips, with at least 3:1 width reduction between 20% and 80% of length. Layer sculpted orange-red flames with angular tongues and soft living interiors. Add a razor-thin, partly interrupted #FFF4D6 hot line on each convex outer edge and two or three tiny attached pinpoint glints. At most two detached ember licks. No extra main strokes, C, ring, lotus, bird, smoke, haze, decorative stars, lens flare, bokeh, ground, sword or text.




### Step 2 — Generate A2-v3




Attach only the original v3 painting.




**Final prompt:**




> Edit the attached v3 painting into a premium anime/donghua sword-impact Brushfire. Reframe the ENTIRE artwork into an opaque pure-black square without cropping, stretching, rotating or mirroring. Preserve EXACTLY THREE open strokes from one lower-left strike root: TWO long crescents sweeping upward and rightward, plus ONE SHORT counter-stroke flicking LEFT. The long crescents sweep approximately 120–150 degrees, never beyond 165 degrees. Do not lengthen the short flick into another crescent. Give all strokes heavy irregular roots, dramatic progressive taper and sharp needle tips. Use layered orange-red hand-painted flame with angular tongues and soft living interiors. Add thin, partly interrupted #FFF4D6 heat along each convex outer edge and two or three tiny attached glints. At most two detached ember licks. No fourth stroke, C, ring, lotus, bird, smoke, haze, stars, flares, bokeh, scenery, sword or text.




Both prompts use the approved six-colour palette.




### Step 3 — Normalize and validate A2




Resize both images to exactly **1080×1080** using Lanczos, preserving proportions and adding black padding as necessary.




Use:




[

Y=(0.2126R+0.7152G+0.0722B)/255

]




Define `lit = Y > 0.1` and `hot = Y ≥ 0.85`.




Annotate at least ten ordered centreline points per stroke, the common root, each tip, and the intended outer-edge side.




**Acceptance:**




| Test | Requirement |

|---|---|

| Main strokes | Exactly three, all open |

| Long-arc sweep | 120–165° |

| v3 short flick | Leftward, net turn ≤120° |

| Taper (W_{20}/W_{80}) | ≥3.0 for crescents; ≥2.5 for short flick |

| Hot-pixel fraction | Target 2–6%; hard range 1–10% |

| Hot-edge continuity | ≥50% for long strokes; ≥35% for short |

| Hot-pixel placement | ≥80% on approved outer edges, excluding glints |

| Margins | Main flame within coordinates 86–993 |

| Black corners | Every RGB channel ≤8 |

| Detached licks | Maximum two |




Use the Kasa least-squares circle fit for long strokes. Calculate sweep from unwrapped angles along the ordered centreline, not endpoint angles alone.




Treat fits with normalized radial error above 0.08 as unreliable. Use smoothed tangent turning for the short flick or unreliable fits. Disagreement above 20° requires annotation review.




**Reject C/ring formations:** reliably measured sweep above 175°, endpoint-to-path-length ratio below 0.55, unintended stroke reconnection, or a visibly closed combined silhouette. Check whole-fan topology, not individual arcs alone.




### Step 4 — Generate A3 for both candidates




Use the approved A2 as the only image attachment. Generate a matching A3 for each candidate entering A4.




**Final prompt:**




> Edit ONLY the attached approved Brushfire first frame into its late-decay endpoint. Preserve the exact opaque-black square, root, scale, orientation and three original stroke paths. Extinguish the SAME flames IN PLACE. Needle tips disappear first, middle sections break into irregular fading islands, and heavy roots survive longest as dark crimson and muted orange embers. Keep approximately 25% of the original visible flame area, concentrated near the roots. Almost all white-gold heat and glints disappear. No movement, extension, reconnection, new eruption, extra arcs, ring, bird, lotus, smoke, haze or text.




**A3 acceptance:**




- Lit area = 15–35% of corresponding A2.

- ≥85% of remaining lit pixels fall inside the A2 lit mask dilated by 12 px; target ≥90%.

- Persistent root landmarks move ≤4 px.

- Root survival exceeds middle survival; middle survival is at least tip survival.

- Hot pixels ≤0.5% of remaining lit area.

- No new major stroke geometry.




Do not force fragmented A3 strokes to pass intact A2 arc/taper requirements.




### Step 5 — Generate A4




Use Adobe Firefly Video only.




**Settings:** First + Last frame, 1:1, 1080p, 24 FPS, five seconds, transparency off, prompt enhancement off.




**Final A4 prompt — 523 characters:**




> The first image already shows the full three-stroke Brushfire; do not erupt again. Keep the lower-left root, three separate OPEN curved paths, tips, framing and camera fixed. For the first half, animate living orange-red tongues and a hair-thin white-gold edge flicker without reshaping the fan. Across the second half, erode slowly toward the supplied last image: tips first, middles next, crimson roots last. Opaque pure black. No new strokes, joining arcs, C-shape, ring, lotus, bird, smoke, haze, flashes, zoom or text.




**Three runs:** Two from the stronger A2/A3 pair, one from the alternative.




### Step 6 — Extract and measure video




Preflight ImageMagick 7 MP4 decoding. Confirm its decoder delegate is available; NumPy alone cannot decode MP4.




Verify actual frame count, dimensions, order and timing. If decoding fails, obtain an ordered, timestamp-verified image sequence before continuing.




Measure every extracted frame automatically. For shortlisted segments, validate actual centrelines, geometry and temporal behavior frame by frame.




A selected source window must retain:




- At least 85% occupancy for long strokes.

- At least 80% for v1 medium/short crescents.

- At least 75% for v3's short flick.

- Root displacement ≤4 px; median centreline displacement ≤8 px.

- No C/ring, fourth main stroke or unacceptable contour change.

- Lit area within 80–115% of the window's first-frame area.

- No six-frame interval losing more than 15% of its starting lit area.




Use interior frame differences to rank living motion, but reject static-looking or violently flickering results visually.




### Step 7 — Select segment and build atlas




Enumerate all contiguous 12–24-frame windows.




Reject any violating hard checks. Among survivors, select deterministically by longest duration, least geometric contamination, least displacement, most stable area, then strongest acceptable internal movement.




Resample to exactly 24 frames:




[

i_k=s+\left\lfloor k(N-1)/23+0.5\right\rfloor

]




where (s) is the selected start index, (N) its frame count and (k=0,\ldots,23).




Create a **1920×1920 atlas**: 5×5 cells, each 384×384. Resize each source frame to 376×376, add 4 px black padding, and leave the final cell empty.




Validate the atlas at actual gameplay size.




### Step 8 — Runtime and approval




Use the atlas as living colour texture. The shader controls the final attack:




| Phase | Frames | Duration |

|---|---|---|

| Reveal | 0–2 | 0.125 s |

| Peak | 3–4 | 0.083 s |

| Decay | 5–23 | 0.792 s |




Decay/attack ratio ≈6.33, exceeding both timing requirements.




Check final composited frames for tip-first erosion, readable flame, thin hot lines, dark backing without a rectangular sticker, and clean disappearance.




**Approval requires both blind judges independently scoring ≥8.5/10 in-game.** Passing numerical checks alone does not approve the asset.




## 3. Sources




1. [Adobe — Generate videos using images](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html). Documents first/last-frame guidance, video settings and disabled Motion controls with a last frame.

2. [Adobe — Generate video with Firefly models](https://helpx.adobe.com/firefly/web/firefly-video-editor/generate-videos/generate-video-using-firefly-models.html). Documents Firefly Video settings and the default five-second, 24 FPS workflow.

3. [Chernov — Error Analysis for Circle Fitting Algorithms](https://people.cas.uab.edu/~mosya/cl/AC1c.pdf). Explains the Kasa algebraic fit and its bias on incomplete arcs.

4. [ImageMagick — Command-line options](https://imagemagick.org/command-line-options/). Documents Lanczos filtering, resize, extent and image-processing operations.




## 4. Open Questions and Risks




- **Geometry calibration:** The actual edited v1/v3 pixels have not been measured. Validate the proposed numeric bounds against the artwork before locking them.

- **Firefly consistency:** First/last keyframes guide generation but do not guarantee every intermediate contour remains fixed.

- **Temporal quality:** A 12-frame source stretched to 24 atlas frames may look stepped; 24 distinct passing frames are preferred.

- **Decoder availability:** MP4 extraction depends on the installed decoding capability. Block analysis if frame order or timing cannot be verified.

- **Visual quality:** A perfectly measured flame may still look generic, muddy, or sticker-like on the game court. The final blind rating is decisive.




**Handoff decision:** Proceed with the three-run controlled experiment. Reject structurally failing outputs rather than relaxing acceptance thresholds to force a winner.




Adobe's documented workflow and Chernov's analysis support the stated tool behavior and mathematical limitations. The proposed numeric acceptance thresholds are project-specific engineering criteria, not claims established by those sources. Firefly+3




END HANDOFF>>>




Review it: is it correct, accurate and complete for the brief? Correct errors, fill gaps, replace weak parts with better ideas, and cite a source for every factual claim.

Deliver: 1) what you agree with, 2) each error or gap with the fix, 3) your full reviewed solution, including the final prompts A2-v1, A2-v3, A3 and A4 written out in full (with the A4 character count), 4) what you are not sure about.
````

**[TURN 0 · Gemini answer]**

### 1. What We Agree With in the Handoff (and Why)

The previous assistant's handoff correctly identified several structural problems in the inherited brief and prompts:

- **Separation of animation vs. shader responsibilities:** Because the Three.js shader already performs the 2–4 frame stroke-order reveal (`reveal_order` mask) and the late tip-to-root alpha erosion (`survival_order` mask), the First Frame (A2) should already show the complete three-stroke fan, and the 24-frame atlas extracted from Firefly (A4) should prioritize living internal flame motion on intact strokes rather than letting both the video clip and the shader extinguish the flame twice.
- **Removing the extra counter-stroke contradiction in A2:** The original A2 prompt asked ChatGPT to *"Add four or five small counter-strokes, a few detached licks"*, which directly conflicts with the check requiring *"exactly 3 main strokes"* and *"outside a 24 px dilation of the three strokes at most 2–3 loose bits"*.
- **Recognizing the `v3` short counter-stroke geometry:** `v3` consists of two long crescents and one short counter-stroke flicking left at the root. Forcing that short root flick to pass a `120–180°` Kåsa circle sweep is geometrically invalid; as shown by Chernov (2010), the algebraic Kåsa fit is heavily biased toward artificially small radii (and inflated sweep angles) on short, noisy arcs.
- **Eliminating "erupt" as a primary action in A4:** Starting the Firefly prompt with *"Three open curved brushfire strokes erupt from one lower-left strike point..."* when Frame 0 already contains the full fan encourages Firefly to either fade down and re-erupt or push the tips outward until they curl into a 300° ring.
- **Spatial verification of the hot line:** Checking only the global percentage of hot pixels (`Y ≥ 0.85` at `2–6%` of lit area) cannot verify whether those hot pixels sit on the leading convex outer edge versus pooling inside the stroke core.
- **Preflighting MP4 decoding:** Python with `numpy` alone cannot decode an `.mp4` container, and ImageMagick 7 relies on an external `ffmpeg` delegate to read video files.

### 2. Errors and Gaps (in Both the Original Plan and the Handoff) — With Fixes

#### A. Prompt Defects

| Defect Location | Error / Gap | Exact Fix |
|---|---|---|
| **Original A2 & Handoff A2 prompts** | **Telling ChatGPT to "Add" white-gold when `v1` and `v3` already exceed the hot-pixel limit:** Fact 2 states `v1` has **8.1%** hot pixels (`Y ≥ 0.85`) and `v3` has **8.9%**, whereas the check requires **2–6%**. Asking the editor to *"Add a razor-thin... hot line"* keeps or increases hot area above 6%. (The handoff hid this by relaxing the hard check to `1–10%` instead of fixing the prompt.) | Instruct ChatGPT to **narrow and pare back** the existing white-gold highlights into a discontinuous razor-thin rim along the convex outer edges (targeting ~3–4% of lit area) and shift interior bright spots down into warm amber/orange so `Y ≥ 0.85` drops into the required `2–6%` range. |
| **Handoff A2 prompts** | **Literal hex code `#FFF4D6` inside an image-editing prompt:** Passing raw hex strings like `#FFF4D6` to ChatGPT (`gpt-image-1`) frequently causes the model to render literal text labels, color swatch bars, or harsh posterized borders. | Replace `#FFF4D6` in the prompt text with visual color descriptors (*"pale ivory white-gold"* over *"stepped deep crimson, vermilion, tangerine, and warm amber"*), and enforce the exact 6-color palette quantizer/distance check in the Python script. |
| **Original A2 prompts** | **Asking ChatGPT for `"1080x1080"` in prompt text:** OpenAI's image model natively generates square images at `1024×1024` (which Fact 3 then resizes via Lanczos to `1080×1080`). Specifying `"1080x1080"` in text does not change output dimensions and leaves no margin target. | Specify a `1:1` square composition with at least a **10% pure-black margin** on all four sides (giving safety buffer for the 8% margin check after Lanczos resize to `1080×1080`). |
| **Handoff A4 prompt** | **Negative token `"do not erupt again"` in sentence 1 + fractional timeline syntax:** Video diffusion text encoders weight early nouns/verbs heavily and process inline negation weakly; putting `"erupt"` in the first clause still activates eruption motion priors. Additionally, `"For the first half... Across the second half..."` is poorly followed by single-prompt video models, which apply text conditioning globally across latent frames. | Open with a positive steady-state anchor (*"Already-ignited three-stroke anime brushfire fan burning in place..."*) with zero occurrences of `"erupt"`, and express temporal progression via natural cause-and-effect motion (*"Hold peak intensity briefly, then slowly erode from needle tips to middle islands down to the final frame's dark crimson root embers"*). |
| **Handoff Step 5** | **Non-existent UI setting `"prompt enhancement off"`:** Adobe Firefly Video's web `Generate Video` panel does not expose a "prompt enhancement off" toggle (unlike text-to-image tools in some third-party wrappers). | Stick strictly to the brief's verified Firefly Video controls: model `Firefly Video`, `1:1`, `1080p`, `24 fps`, `5 s`, `First frame + Last frame` uploaded, `Transparent background` off, camera motion `Static / None`. |

#### B. Measurement, Check, and Pipeline Defects

| Defect Location | Error / Gap | Exact Fix |
|---|---|---|
| **Handoff Step 3 (Margin coordinates)** | **Off-by-one boundary error (`86–993`):** At `1080×1080`, 8% of 1080 is `86.4 px`. In 0-indexed coordinates `0..1079`, pixel index `86` is only `86 / 1080 = 7.96%` from the top/left edge, and `993` leaves `1079 - 993 = 86 px` (`7.96%`) on the right/bottom edge—failing a strict `≥ 8%` check. | Require `xmin ≥ 87`, `ymin ≥ 87`, `xmax ≤ 992`, `ymax ≤ 992` in 0-indexed coordinates (leaving at least `87 px = 8.055%` of pure unlit margin on all four edges). |
| **Handoff Step 3 ("Leading outer edge" check)** | **Unimplementable / circular definition:** The handoff tells a human to *"annotate... the intended outer-edge side"* and checks *"≥ 80% on approved outer edges, excluding glints"* without defining how the script constructs the outer-edge zone or separates glints. | Define the **convex outer normal** N out 	​  (s) mathematically from the ordered centerline itself using the chord-bulge sign (no extra side annotation needed), define the **outer rim band** as the outer 40% of local outer half-width (or within `4 px` of the outer lit boundary), and isolate pinpoint glints by morphological top-hat / local prominence (`area ≤ 36 px²` with four-ray cross profile). |
| **Brief & Handoff (Taper check W 20 	​  /W 80 	​ )** | **Two script-breaking edge cases:** (1) Near the common lower-left strike root (s=0.20L), normal rays from adjacent strokes cross into neighboring strokes if their roots touch, inflating W 20 	​ . (2) If a stroke tip vanishes early (W 80 	​  =0), W 20 	​  /W 80 	​  =∞, passing a broken stroke. | (1) Partition the lit mask into 3 stroke territories via **geodesic / Voronoi nearest-centerline assignment** before marching along the normal, stopping when leaving stroke k's territory. (2) Require non-zero tip width W 80 	​  ≥1.5 px (via subpixel bilinear normal sampling) and lit occupancy past s=0.95L. |
| **Handoff Step 3 ("Closes into a C" thresholds)** | **Internal mathematical contradiction:** For a circular arc of sweep θ, the exact chord-to-arc ratio is θ 2sin(θ/2) 	​ . At θ=175 ∘, chord/arc=0.654; at θ=180 ∘, chord/arc=0.637. The handoff set max sweep at 175 ∘ while setting the minimum chord-to-path ratio at `0.55` (which allows a **204 ∘** C-arc!). | Align both metrics to the brief's `180°` ceiling: require per-stroke Kåsa sweep θ k 	​  ≤180 ∘, chord-to-arc ratio ∥P tip 	​  −P root 	​  ∥/L k 	​  ≥0.60, AND add an automated **whole-fan polar wrap check** (Θ fan 	​  ≤185 ∘ around the fan's Kåsa center) plus a **zero interior cavity check**. |
| **Brief & Handoff (A3 cross-correlation shift check)** | **Raw luma cross-correlation fails on in-place burn-down:** In A2, peak luma (`Y ≥ 0.85`) sits at the root and outer edge; in A3, roots have cooled to dark crimson (`Y ≈ 0.2–0.35`) while middle islands may be brighter (`Y ≈ 0.5`). Unmasked luma cross-correlation slides A3's middle islands onto A2's bright root, reporting a false shift up to `15–24 px`. (The handoff quietly dropped cross-correlation for manual "root landmarks".) | Keep the brief's automated `±24 px` cross-correlation check, but compute **Zero-Mean Normalized Cross-Correlation (ZNCC) on the binary/soft-clipped lit masks min(Y/0.15,1.0) restricted to the 12 px-dilated support of A3**. Inside A3's dilated footprint, both frames share the same active strokes without A2's vanished tips biasing the correlation peak. |
| **Handoff Step 6 & Step 7 (Window selection vs. decay)** | **Rejecting natural Firefly decay windows:** Because Firefly interpolates from A2 (100% area) to A3 (~25% area) over 120 frames, its best 12–24 frame motion window often exhibits gentle early tip decay (e.g., `100% → 70%` area). The handoff's rule (*"Lit area within 80–115%"*) can reject all 3 runs if Firefly begins smooth decay early. | Allow the selected 12–24 frame segment to retain `65–110%` of its starting frame's lit area **provided** that: (a) no 6-frame sub-window loses more than `18%` of area (preventing the 6-frame burnout of `ff-a1-c5`), and (b) all 3 strokes remain present and pass arc (`120–180°` long) and taper (`≥ 2.5×` dynamic) on every frame of the segment. |
| **Handoff Step 7 (Atlas cell scaling `376×376` + `4 px` pad)** | **UV misregistration against shader masks:** Shrinking each frame from `384×384` to `376×376` (97.9% scale) shifts the flame inward by up to `11 px` (at 1080p scale) relative to the static `reveal_order` and `survival_order` masks painted over the `1080×1080` A2 reference! Furthermore, an `87 px` margin at `1080p` already equals **`30.9 px` of pure black margin** after scaling directly to `384×384`. | Resize each `1080×1080` frame **directly to `384×384`** (`-filter Lanczos -resize 384x384!`) to maintain 1:1 UV registration with the shader masks, and zero out the outer `2 px` border of each `384×384` cell in place (`cell[:2,:]=0`, etc.) to prevent Lanczos ringing or bilinear bleed. |

### 3. Full Reviewed Solution

#### Part A — Final Prompts

##### 1. A2-v1 (First Frame from `v1` painting)

Attach only the original `v1` (`1536×1024`) painting in ChatGPT image editing (`1:1` square output):

> Edit the attached painting into a 1:1 square opaque pure-black canvas by reframing the entire flame fan inward so at least 10 percent pure-black margin surrounds all four sides, without cropping, stretching, rotating or mirroring. Keep the lower-left strike root and exactly three separate OPEN flame crescents sweeping up-right (long, medium, short), each curving between 120 and 160 degrees and never closing into a C or ring. Give every stroke a heavy irregular root that tapers smoothly to a needle-fine tip at most one-third of its root width. Use a stepped anime/donghua fire palette of deep crimson, vermilion, bright tangerine and warm amber with soft living interior tongues. Narrow the existing pale ivory white-gold highlights into a razor-thin, slightly broken line strictly hugging each convex leading outer edge (covering only 3 to 4 percent of the flame area) plus two or three tiny pinpoint glints. Include at most two small detached ember specks near the tips; absorb any extra root flicks into the three main roots. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.

##### 2. A2-v3 (First Frame from `v3` painting)

Attach only the original `v3` (`1536×1024`) painting in ChatGPT image editing (`1:1` square output):

> Edit the attached painting into a 1:1 square opaque pure-black canvas by reframing the entire flame fan inward so at least 10 percent pure-black margin surrounds all four sides, without cropping, stretching, rotating or mirroring. Keep the lower-left strike root and resolve the flame into exactly three separate OPEN strokes: two long crescents sweeping up-right (curving between 120 and 160 degrees, never closing into a C or ring) and one short counter-stroke flicking sharply left at the root. Do not lengthen the short left flick into a third crescent. Give all three strokes heavy irregular roots that taper smoothly to needle-fine tips at most one-third of their root width. Use a stepped anime/donghua fire palette of deep crimson, vermilion, bright tangerine and warm amber with soft living interior tongues. Narrow the existing pale ivory white-gold highlights into a razor-thin, slightly broken line strictly hugging each convex leading outer edge (covering only 3 to 4 percent of the flame area) plus two or three tiny pinpoint glints. Include at most two small detached ember specks; merge any other loose bits into the three strokes. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.

##### 3. A3 (End Frame from the chosen `1080×1080` A2 frame)

Attach only the normalized `1080×1080` A2 image (generate a matching A3 for each A2 candidate entering A4):

> Edit the attached image in place on the exact same opaque pure-black 1:1 canvas. Keep the lower-left root and all three stroke paths locked at their exact pixel coordinates; do not shift, scale, rotate, extend or reconnect anything. Show the same three strokes late in their burn-down: needle tips completely vanished, middle sections broken into small separated orange-red islands, and thick roots cooled into dark crimson and muted ember cores, with two or three tiny dying ember specks along the original paths. Total lit flame area must be about one-quarter of the attached image, with almost no white-gold remaining. No new flames, arcs, C-shape, ring, lotus, bird, smoke, glow haze or text.

##### 4. A4 (Adobe Firefly Video — **537 characters** including spaces)

Settings: **Adobe Firefly Video**, **First frame** = normalized `1080×1080` A2, **Last frame** = normalized `1080×1080` A3, aspect ratio **1:1**, resolution **1080p**, frame rate **24 fps**, duration **5 s**, transparency **Off**, camera motion **Static / None**.

> Already-ignited three-stroke anime brushfire fan burning in place on a fixed pure-black canvas. Keep the lower-left strike root, three separate open curved paths, and sharp needle tips locked in position. Stepped orange-red flame tongues surge along each stroke with a hair-thin white-gold shimmer hugging the convex outer edges. Hold peak intensity briefly, then slowly erode from needle tips to middle islands down to the final frame's dark crimson root embers. Static camera. No closing C-arc, ring, lotus, bird, smoke, bloom or text.

*(Character count verification: 537 characters, well below the 600-character limit.)*

#### Part B — Exact Script-Ready Check Definitions (Python + NumPy + ImageMagick 7)

##### Step 0: Image Normalization & MP4 Frame Extraction (ImageMagick 7)

1. **Normalize A2 and A3 to `1080×1080` 8-bit sRGB PNG** (clamping negative Lanczos lobes and stripping any alpha channel):Bash`magick input.png -alpha off -colorspace sRGB -filter Lanczos -define filter:clamp=true -resize 1080x1080! -depth 8 PNG24:output_1080.png
`
  *(Check before running: `identify -format "%wx%h" input.png` must be `1:1`, e.g., `1024x1024`. If ChatGPT returned `1536x1024`, reject and re-run in `1:1` mode rather than stretching with `!`.)*
2. **Extract Firefly A4 MP4 to 120 numbered PNG frames** (after verifying `magick -list delegate | grep -i ffmpeg`):Bash`magick ff_run1.mp4 -alpha off -colorspace sRGB -coalesce -depth 8 PNG24:frames/frame_%03d.png
`
  Verify that `frames/` contains `120` frames (`frame_000.png` to `frame_119.png`), each `1080×1080`.

##### Step 1: Base Pixel Masks and Connected Components (NumPy)

Given an RGB image array `img` of shape `(1080, 1080, 3)` with `uint8` values in `[0, 255]`:

- **Luma:**
  $$
Y = \frac{0.2126\,R + 0.7152\,G + 0.0722\,B}{255.0}
$$
- **Masks:** `lit = (Y > 0.10)` and `hot = (Y >= 0.85)`. Let $N_{\text{lit}} = \sum \text{lit}$.
- **8-connected components (pure NumPy + ImageMagick or BFS in Python):** Either label 8-connected components of `lit` in Python using a standard queue-based breadth-first search over `np.argwhere(lit)` or via ImageMagick `magick frame.png -fx "0.2126*r+0.7152*g+0.0722*b" -threshold 10% -define connected-components:connectivity=8 -connected-components 8 -auto-level PNG16:labels.png`.
- **24 px morphological dilation in pure NumPy:** Let $D_{r}$ be a binary disk mask of radius $r$ (`dx**2 + dy**2 <= r**2`). Dilate any binary mask $M$ via FFT convolution:Python`def dilate_disk(mask: np.ndarray, radius: int) -> np.ndarray:
    y, x = np.ogrid[-radius:radius+1, -radius:radius+1]
    kernel = (x*x + y*y <= radius*radius).astype(np.float64)
    H, W = mask.shape
    kh, kw = kernel.shape
    f_mask = np.fft.rfft2(mask.astype(np.float64), s=(H + kh - 1, W + kw - 1))
    f_kern = np.fft.rfft2(kernel, s=(H + kh - 1, W + kw - 1))
    conv = np.fft.irfft2(f_mask * f_kern, s=(H + kh - 1, W + kw - 1))
    sy, sx = radius, radius
    return conv[sy:sy+H, sx:sx+W] > 0.5
`

##### Step 2: Centerline Parameterization, Kåsa Fit, and Short-Stroke Turning Angle

For each stroke $k \in \{1, 2, 3\}$, a human annotates $M \ge 10$ ordered points $P_0, P_1, \dots, P_{M-1}$ from root ($P_0$) to tip ($P_{M-1}$) in pixel coordinates $(x, y)$.

1. **Arc-length resampling:** Compute cumulative chord lengths along $P_0 \dots P_{M-1}$ with total length $L_k$. Linearly interpolate $(x(s), y(s))$ at uniform arc-length stations $s_j = j\,\Delta s$ with $\Delta s = 1.0\text{ px}$ for $j = 0, \dots, \lfloor L_k \rfloor$. Smooth $(x(s), y(s))$ with a 1D Savitzky–Golay or Gaussian kernel ($\sigma = 3\text{ px}$, keeping endpoints fixed) to remove click jitter, yielding curve $C_k(s)$ and unit tangent $\mathbf{T}_k(s) = (T_x(s), T_y(s))$.
2. **Distinguishing long crescents vs. `v3` short counter-stroke:**
  - A stroke is classified as the **`v3` short counter-stroke** if $L_k \le 260\text{ px}$ and $x_{\text{tip}} < x_{\text{root}}$ (flicks leftward from the strike root). All other main strokes must have $L_k > 260\text{ px}$ and $x_{\text{tip}} > x_{\text{root}},\, y_{\text{tip}} < y_{\text{root}}$ (sweeping up-right).
3. **Kåsa circle fit & unwrapped sweep (for long crescents):**
Given points $(x_j, y_j)_{j=0}^n$ along $C_k(s)$, solve the linear least-squares system:
  $$
\begin{bmatrix} x_0 & y_0 & 1 \\ \vdots & \vdots & \vdots \\ x_n & y_n & 1 \end{bmatrix} \begin{bmatrix} a \\ b \\ c \end{bmatrix} \approx -\begin{bmatrix} x_0^2 + y_0^2 \\ \vdots \\ x_n^2 + y_n^2 \end{bmatrix}
$$
  via `np.linalg.lstsq`. Then center $(x_c, y_c) = (-a/2, -b/2)$ and radius $R = \sqrt{x_c^2 + y_c^2 - c}$.
Compute radial angles $\phi_j = \text{atan2}(y_j - y_c, x_j - x_c)$, unwrap via `phi_unwrapped = np.unwrap(phi)`, and compute sweep in degrees:
  $$
\theta_{\text{Kasa}, k} = \frac{180^\circ}{\pi} \bigl|\phi_{\text{unwrapped}}[-1] - \phi_{\text{unwrapped}}[0]\bigr|
$$
  Also compute the normalized radial RMSE: $\epsilon_{\text{rad}} = \frac{1}{R}\sqrt{\frac{1}{n+1}\sum_{j=0}^n \bigl(\|(x_j - x_c, y_j - y_c)\| - R\bigr)^2}$.
  - **Pass requirement (long crescents):** $120^\circ \le \theta_{\text{Kasa}, k} \le 180^\circ$ AND chord-to-arc ratio $\frac{\Vert{}P_{M-1} - P_0\Vert{}}{L_k} \ge 0.60$.
4. **Arc / turning measurement for the `v3` short counter-stroke:**
Because Kåsa is biased on short arcs (Chernov 2010), compute the **total signed tangent turning angle** using secant tangents with baseline $\delta = \max(0.08 L_k, 8\text{ px})$:
  $$
\Delta \theta_{\text{turn}, k} = \frac{180^\circ}{\pi} \left| \sum_{j} \text{atan2}\bigl(T_x(s_j) T_y(s_{j+1}) - T_y(s_j) T_x(s_{j+1}),\; \mathbf{T}(s_j)\cdot\mathbf{T}(s_{j+1})\bigr) \right|
$$
  - **Pass requirement (`v3` short counter-stroke):** $x_{\text{tip}} < x_{\text{root}}$, $80\text{ px} \le L_k \le 260\text{ px}$, $15^\circ \le \Delta \theta_{\text{turn}, k} \le 110^\circ$, and chord-to-arc ratio $\frac{\Vert{}P_{M-1} - P_0\Vert{}}{L_k} \ge 0.72$.

##### Step 3: Exact Taper Check ($W_{20} / W_{80}$) with Stroke-Territory Clamping

1. **Stroke territory assignment:** For every lit pixel $\mathbf{p} = (x, y)$, compute its Euclidean distance $d_k(\mathbf{p}) = \min_s \|\mathbf{p} - C_k(s)\|$ to each of the 3 centerlines. Assign pixel $\mathbf{p}$ to stroke $k^*(\mathbf{p}) = \arg\min_{k \in \{1,2,3\}} d_k(\mathbf{p})$ if $d_{k^*}(\mathbf{p}) \le 24\text{ px}$ (pixels beyond $24\text{ px}$ belong to detached bits).
  - *Openness / 3-stroke separation check:* For $s \in [0.25 L_k, 1.0 L_k]$ (past the shared lower-left root), the minimum centerline-to-centerline distance between any two strokes $k \neq m$ must be greater than the sum of their local half-widths plus $3\text{ px}$ (or a minimum `lit == False` gap of at least $2\text{ px}$ along the shortest line segment connecting $C_k(s)$ and $C_m(s')$).
2. **Normal width $w_k(s)$ at station $s$:**
Let $\mathbf{N}_k(s) = (-T_y(s), T_x(s))$ be the unit normal at $C_k(s)$. Sample the indicator mask $I_k(\mathbf{x}) = \mathbb{1}[\text{lit}(\mathbf{x}) \text{ and } k^*(\mathbf{x}) = k]$ along the ray $C_k(s) + u\,\mathbf{N}_k(s)$ at step $\Delta u = 0.25\text{ px}$ using bilinear interpolation of $Y$ ($Y > 0.10$) gated by nearest-pixel territory $k^* = k$.
March outward in $+u \ge 0$ until $I_k = 0$ at $u = r_{+}(s)$, and in $-u \le 0$ until $I_k = 0$ at $u = -r_{-}(s)$. (If $C_k(s)$ sits in a small interior flicker gap up to $2\text{ px}$ from lit pixels, start the contiguous run from the nearest lit pixel within $|u| \le 2\text{ px}$.) Then:
  $$
w_k(s) = r_{+}(s) + r_{-}(s)
$$
3. **Windowed medians $W_{20}$ and $W_{80}$:**
Let $\Delta_w = \max(0.03 L_k, 5\text{ px})$.
  - For long crescents: $W_{20, k} = \text{median}\{w_k(s) : s \in [0.20 L_k - \Delta_w, 0.20 L_k + \Delta_w]\}$ and $W_{80, k} = \text{median}\{w_k(s) : s \in [0.80 L_k - \Delta_w, 0.80 L_k + \Delta_w]\}$.
  - For the `v3` short counter-stroke (to avoid root junction overlap at $0.20 L_k$): allow $W_{20, k}$ to be measured at $s = 0.25 L_k \pm 5\text{ px}$ if $s = 0.20 L_k$ touches the main crescent root.
  - **Pass requirement:** $W_{80, k} \ge 1.5\text{ px}$, lit stroke reaches at least $s = 0.95 L_k$, and $\frac{W_{20, k}}{W_{80, k}} \ge 3.0$ for long crescents ($\ge 2.5$ for the `v3` short counter-stroke).

##### Step 4: Exact "Leading Outer Edge" Decision Rule for the Hot Line

1. **Automatic orientation of the outward (convex) normal $\mathbf{N}_{\text{out}, k}(s)$:**
Let $\mathbf{U}_k = \frac{P_{M-1} - P_0}{\|P_{M-1} - P_0\|}$ be the unit root-to-tip chord vector and $\mathbf{N}_{\perp, k} = (-U_{k,y}, U_{k,x})$. Compute the signed midpoint bulge away from the chord:
  $$
b_k = \bigl(C_k(0.5 L_k) - P_0\bigr) \cdot \mathbf{N}_{\perp, k}, \qquad \sigma_k = \text{sign}(b_k) \in \{-1, +1\}
$$
  Because any simple open arc bulges away from its chord toward its **convex (outer)** side, the outward unit normal at every station $s$ is unambiguously:
  $$
\mathbf{N}_{\text{out}, k}(s) = \sigma_k \, \bigl(-T_{k,y}(s),\, T_{k,x}(s)\bigr)
$$
2. **Separating pinpoint glints from the hot line:**
Label 8-connected components of `hot` ($Y \ge 0.85$). A hot component $G$ is classified as a **pinpoint glint** if its area is $1 \le |G| \le 36\text{ px}^2$ (`<= 6x6 px` core) and its bounding-box aspect ratio is in $[0.5, 2.0]$. Require between `1 and 4` pinpoint glints total across the fan.
3. **Leading-outer-edge placement and continuity check:**
For every remaining hot pixel $\mathbf{p} \in \text{hot} \setminus \text{glints}$ assigned to stroke $k$ with nearest centerline station $s^*(\mathbf{p})$, compute its signed normal offset:
  $$
d_{\text{out}}(\mathbf{p}) = \bigl(\mathbf{p} - C_k(s^*)\bigr) \cdot \mathbf{N}_{\text{out}, k}(s^*)
$$
  Compare $d_{\text{out}}(\mathbf{p})$ against the local outer boundary radius $r_{\text{out}, k}(s^*)$ (the distance along $+\mathbf{N}_{\text{out}, k}(s^*)$ from $C_k(s^*)$ to the outer edge of the `lit` mask).
Pixel $\mathbf{p}$ is on the **leading outer edge** if:
  $$
d_{\text{out}}(\mathbf{p}) > 0 \quad \text{AND} \quad d_{\text{out}}(\mathbf{p}) \ge \max\bigl(0.50\, r_{\text{out}, k}(s^*),\; r_{\text{out}, k}(s^*) - 4.0\text{ px}\bigr)
$$
  - **Pass requirements for hot pixels:**
    1. **Total hot area fraction:** $0.02 \le \frac{N_{\text{hot}}}{N_{\text{lit}}} \le 0.06$ (strictly `2.0% to 6.0%`).
    2. **Outer-edge concentration:** At least **80%** of non-glint hot pixels satisfy the leading-outer-edge equation above, and at least **90%** satisfy $d_{\text{out}}(\mathbf{p}) > 0$ (convex half of the stroke).
    3. **Edge continuity:** Along $s \in [0.15 L_k, 0.85 L_k]$, at least **40%** of arc-length stations on each long crescent ($\ge 25\%$ on the short flick) have at least one hot pixel in the leading-outer-edge band within $\pm 2\text{ px}$ of station $s$.

##### Step 5: Margins, Detached Loose Bits, and Corner Black (A2)

- **8% Margin check:** Filter out tiny connected components of `lit` with area under $0.0005 \times N_{\text{lit}}$ ($0.05\%$). For the union of all remaining `lit` pixels, require `87 <= x <= 992` and `87 <= y <= 992` (0-indexed).
- **Loose bits outside 24 px stroke dilation:** Let $M_{\text{strokes}}$ be the union of the 3 main stroke masks, and let $M_{24} = \text{dilate\_disk}(M_{\text{strokes}}, 24)$. Find all 8-connected components of `lit & (~M_24)` with area $\ge 4\text{ px}^2$ (ignoring 1–3 px quantization dust). Require **at most 3 components**, and require each component's area to be $\le 0.02 \times N_{\text{lit}}$.
- **Corner black:** In the four $16 \times 16$ corner patches (`[0:16, 0:16]`, `[0:16, 1064:1080]`, `[1064:1080, 0:16]`, `[1064:1080, 1064:1080]`), require `max(R, G, B) <= 8` for every pixel.

##### Step 6: End-Frame (A3) Checks

Given $Y_{\text{A2}}, \text{lit}_{\text{A2}}$ and $Y_{\text{A3}}, \text{lit}_{\text{A3}}$:

1. **Lit area ratio:** $0.15 \le \frac{\sum \text{lit}_{\text{A3}}}{\sum \text{lit}_{\text{A2}}} \le 0.35$.
2. **Spatial containment:** Let $D_{12} = \text{dilate\_disk}(\text{lit}_{\text{A2}}, 12)$. Require $\frac{\sum (\text{lit}_{\text{A3}} \land D_{12})}{\sum \text{lit}_{\text{A3}}} \ge 0.70$ (target $\ge 0.85$).
3. **Shift check via masked Zero-Mean Normalized Cross-Correlation (ZNCC):**
To prevent A2's vanished bright tips from pulling the correlation peak along the stroke tangent, define the soft-clipped masks $S_{\text{A2}} = \min(Y_{\text{A2}} / 0.15, 1.0)$ and $S_{\text{A3}} = \min(Y_{\text{A3}} / 0.15, 1.0)$, and restrict the reference window to the active region $W_{\text{support}} = \text{dilate\_disk}(\text{lit}_{\text{A3}}, 12)$.
For every integer shift $(\Delta x, \Delta y) \in [-24, 24]^2$, shift $S_{\text{A3}}$ by $(\Delta x, \Delta y)$ (zero-padded) and evaluate ZNCC against $S_{\text{A2}}$ inside $W_{\text{support}}$:
  $$
\text{ZNCC}(\Delta x, \Delta y) = \frac{\sum_{\mathbf{p} \in W_{\text{support}}} \bigl(S_{\text{A2}}(\mathbf{p}) - \bar{S}_{\text{A2}}\bigr)\bigl(S_{\text{A3}}(\mathbf{p} - \boldsymbol{\Delta}) - \bar{S}_{\text{A3},\boldsymbol{\Delta}}\bigr)}{\sqrt{\sum_{\mathbf{p} \in W_{\text{support}}} \bigl(S_{\text{A2}}(\mathbf{p}) - \bar{S}_{\text{A2}}\bigr)^2 \sum_{\mathbf{p} \in W_{\text{support}}} \bigl(S_{\text{A3}}(\mathbf{p} - \boldsymbol{\Delta}) - \bar{S}_{\text{A3},\boldsymbol{\Delta}}\bigr)^2}}
$$
  Let $(\Delta x^*, \Delta y^*) = \arg\max_{\Delta x, \Delta y \in [-24, 24]} \text{ZNCC}(\Delta x, \Delta y)$.
  - **Pass requirement:** $\sqrt{(\Delta x^*)^2 + (\Delta y^*)^2} \le 4.0\text{ px}$.
4. **Tip-to-root survival gradient & hot burnout:** Partition $\text{lit}_{\text{A2}}$ into Root ($s \in [0, 0.33 L_k]$), Middle ($s \in (0.33 L_k, 0.67 L_k]$), and Tip ($s \in (0.67 L_k, 1.0 L_k]$) zones. Require survival fractions in A3 to satisfy $f_{\text{root}} > f_{\text{mid}} > f_{\text{tip}}$ with $f_{\text{tip}} \le 0.10$, and require $\frac{\sum \text{hot}_{\text{A3}}}{\sum \text{lit}_{\text{A3}}} \le 0.005$ ($\le 0.5\%$).

##### Step 7: Measurable Rule for "Closes into a C" & Segment Selection in A4 (120 Frames)

1. **Automated per-frame "Closes into a C" rejection rule (run on all 120 frames $t = 0 \dots 119$):**
A frame $t$ **closes into a C or ring** if ANY of the following three conditions holds:
  - **Condition C1 (Whole-fan polar angular wrap $> 190^\circ$):** Let $(x_c, y_c)$ be the Kåsa circle center of the longest crescent in Frame 0. Compute polar angles $\phi(\mathbf{p}) = \text{atan2}(y - y_c, x - x_c) \in [-\pi, \pi)$ for all $\mathbf{p} \in \text{lit}_t$. Bin into 360 $1^\circ$ sectors; mark sector $b$ occupied if it contains $\ge 10$ lit pixels. Let $\Delta \phi_{\text{empty}}(t)$ be the largest contiguous run of unoccupied sectors (wrapping around $\pm 180^\circ$). The fan's angular wrap is $\Theta_{\text{fan}}(t) = 360^\circ - \Delta \phi_{\text{empty}}(t)$. Reject if $\Theta_{\text{fan}}(t) > 190^\circ$ (inside the selected window, require $\Theta_{\text{fan}}(t) \le 185^\circ$).
  - **Condition C2 (Topological loop / enclosed cavity):** Compute $M_{\text{closed}}(t) = \text{dilate\_disk}(\text{lit}_t, 12)$. Flood-fill the unlit background (`~M_closed(t)`) starting from the four image corners. If any unreached interior unlit component has area $\ge 1{,}000\text{ px}^2$, the fan has formed a closed ring/loop.
  - **Condition C3 (Single-stroke C-curl):** Any individual stroke centerline in frame $t$ has Kåsa sweep $\theta_{\text{Kasa}, k}(t) > 180^\circ$ or chord-to-arc ratio $\frac{\Vert{}P_{\text{tip}}(t) - P_{\text{root}}(t)\Vert{}}{L_k(t)} < 0.60$.
  - **Run-level vs. window-level rule:** Reject the entire 120-frame run if Condition C1 or C2 triggers during the active flame phase ($\sum \text{lit}_t \ge 0.35 \sum \text{lit}_0$).
2. **Selecting the best 12–24 frame segment $[s, s + N - 1]$ ($12 \le N \le 24$):**
  - **Automated pre-filter over all candidate windows $[s, s+N-1]$:**
    1. Every frame $t \in [s, s+N-1]$ passes Conditions C1 and C2 ($\Theta_{\text{fan}}(t) \le 185^\circ$, zero interior cavities), margins `[87, 992]`, and corner black `<= 8`.
    2. **Anti-fast-burnout check:** For every frame $t \in [s, s+N-1]$, $\sum \text{lit}_t \in [0.65 \sum \text{lit}_s,\, 1.15 \sum \text{lit}_s]$, and no 6-frame sub-interval $[t, t+5]$ loses more than $15\%$ of $\sum \text{lit}_t$.
    3. **Stroke occupancy:** The 3 stroke territories from Frame 0 (dilated by $12\text{ px}$) each retain at least $75\%$ of their Frame-$s$ lit pixel count in every frame of the window, with ZNCC shift against Frame 0 $\le 4\text{ px}$.
  - **Per-frame geometry verification on the top candidate window:** Extract the 3 stroke centerlines on each of the $N$ frames (seeded from the annotated Frame-0 centerlines via medial-axis ridge tracking within each stroke's $16\text{ px}$ corridor, verified visually by the reviewer) and confirm all $N$ frames pass the 3-stroke openness, arc ($120–180^\circ$ long crescents; $15–110^\circ$ `v3` flick), and taper ($\ge 2.5\times$ dynamic, $\ge 3.0\times$ window median) checks.
  - **Deterministic ranking score $J(s, N)$:** Among passing windows, maximize:
    $$
J(s, N) = 2.0\,\frac{N}{24} + 1.5\,\text{mean}_{t}\bigl(\text{internal\_luma\_diff}(t, t+1)\bigr) - 2.0\,\text{max}_{t}\bigl(\text{boundary\_leak}(t)\bigr) - 1.0\,\text{std}_{t}\left(\frac{\sum \text{lit}_t}{\sum \text{lit}_s}\right)
$$
    where `internal_luma_diff(t, t+1)` is the mean $|Y_{t+1} - Y_t|$ inside the core of `lit_0` (capped at `0.18` so violent strobe flicker is penalized) and `boundary_leak(t)` is the fraction of `lit_t` outside `dilate_disk(lit_0, 12)`.

##### Step 8: Resampling to 24 Frames and Building the `384×384` Cell Colour Atlas

1. **Temporal resampling ($N \in [12, 24] \to 24$ frames):**
  - If $N = 24$, copy frames $s, s+1, \dots, s+23$ directly (1:1, preferred).
  - If $12 \le N \le 23$, map output frame $k \in \{0, \dots, 23\}$ to continuous source coordinate $\tau_k = s + \frac{k(N - 1)}{23.0}$. Notice that nearest-neighbor rounding $\lfloor \tau_k + 0.5 \rfloor$ duplicates frames when $N < 24$, creating visible `12 fps` stutter in a `24 fps` flipbook! Instead, use **gamma-correct linear frame blending** between $i_0 = \lfloor \tau_k \rfloor$ and $i_1 = \min(i_0 + 1, s + N - 1)$ with weight $\alpha = \tau_k - i_0$ whenever $|\alpha - 0.5| < 0.35$ and the per-pixel luma change is smooth, or select $N = 24$ whenever a 24-frame window passes.
2. **Downscaling to `384×384` cells without breaking UV registration:**
  - Resize each of the 24 `1080×1080` frames **directly to `384×384`** (`magick frame_k.png -filter Lanczos -define filter:clamp=true -resize 384x384! cell_k.png`), then zero out the outer `2 px` border of `cell_k` (`cell[:2, :] = 0; cell[-2:, :] = 0; cell[:, :2] = 0; cell[:, -2:] = 0`). Because A2 already has an $\ge 87\text{ px}$ black margin at `1080p` ($\ge 30.9\text{ px}$ at `384×384`), zeroing the outer `2 px` never touches a flame pixel while keeping exact 1:1 UV alignment with the `1080×1080` `reveal_order` and `survival_order` shader masks.
3. **Tiling the 24 cells:**
  - Tile into the exact grid layout expected by the Three.js flipbook shader (`6×4` = `2304×1536` with zero empty cells, or `5×5` = `1920×1920` with cell 24 black; pass `--grid 6x4` or `--grid 5x5` to match the existing `ff-a1-c5` material uniform):Bash`magick montage cell_*.png -tile 6x4 -geometry 384x384+0+0 -background "#000000" -depth 8 PNG24:brushfire_atlas_24f.png
`

### 4. Risks, Verification Checks, Uncertainties, and Cited Sources

#### Risks and How to Check Each

1. **ChatGPT altering stroke positions during A3 editing:** Even with strict "in place" instructions, `gpt-image-1` re-synthesizes the entire image rather than editing only masked pixels, which can shift strokes by `5–15 px`.
  - *How to check & mitigate:* Run the Step 6 masked ZNCC shift check immediately (`shift <= 4.0 px`). If ChatGPT shifts A3 by `5–12 px` globally, either apply the opposite integer translation $(-\Delta x^*, -\Delta y^*)$ in ImageMagick (`-roll`) and re-verify containment ($\ge 85\%$ inside `dilate_disk(lit_A2, 12)`), or supply an explicit inpainting mask in ChatGPT's selection tool over the tips and middle sections while leaving the lower-left root unmasked.
2. **Firefly Video interpolating a global fade instead of tip-to-root erosion:** Firefly's `First frame + Last frame` conditioning guides the start and end states but can linearly cross-dissolve or swirl between them mid-clip.
  - *How to check:* Plot $\sum \text{lit}_t$ and the tip-vs-root ratio $f_{\text{tip}}(t) / f_{\text{root}}(t)$ across all 120 frames. Because the in-game shader applies its own painted `survival_order` erosion mask during frames `5..23` (`0.792 s` decay vs `0.125 s` 3-frame attack, giving a `6.33×` decay-to-attack ratio), selecting an intact 24-frame living-flame window from the first half of the Firefly clip insulates the final game effect from late-clip Firefly cross-dissolve artifacts.
3. **Black background compression noise from Firefly MP4 (`H.264` YUV420p):** Video compression often lifts pure black `(0,0,0)` to `(1..4, 1..4, 1..4)` in macroblocks around bright flames.
  - *How to check:* Confirm corner black `<= 8/255` and ensure the Three.js shader's `alpha = smoothstep(lo, hi, max_RGB)` sets `lo >= 0.04` (`~10/255`) so H.264 black-level quantization noise is completely transparent and never shows a rectangular card edge ("sticker edge").

#### What We Are Not Sure About (Requires Verification Against the Repo / Assets)

1. **Exact atlas grid dimensions (`6×4` vs `5×5` vs `4×6`):** The brief specifies *"a 24-frame colour atlas with 384 px cells"* but does not state the row×column layout hardcoded in the Three.js shader for `ff-a1-c5`. Check the shader's flipbook UV divisor uniform before exporting the final PNG.
2. **Actual centerline coordinates of raw `v1` and `v3`:** We have their bounding boxes (`209..1277, 120..888` and `175..1319, 140..857`) and hot-pixel percentages (`8.1%` and `8.9%`), but not the pixel rasters themselves. If `v1`'s shortest inner crescent is already around `110–115°` in the original painting, the A2 check's lower bound (`120°`) will either force ChatGPT to slightly lengthen that inner crescent or require calibrating the inner-crescent lower bound to `110°`.

#### Cited Sources

1. **Adobe Firefly Video — First & Last Frame, Resolution, FPS, and Transparent Background Constraints:** Adobe HelpX, *"Generate videos using images (First and Last Frame)"* and *"Generate video using Firefly models"* ([helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html)). Confirms `1080p`, `24 fps`, `5 s` duration, First + Last keyframe conditioning, and that transparent background video output is restricted to `540p` `16:9`.
2. **Kåsa Algebraic Circle Fit & Small-Arc Bias:** Kåsa, I. (1976), *"A circle fitting procedure and its error analysis"*, IEEE Transactions on Instrumentation and Measurement, 25(1), 8–14; and Chernov, N. (2010), *Circular and Linear Regression: Fitting Circles and Lines by Least Squares*, Chapman & Hall/CRC, Chapter 5 ([people.cas.uab.edu/~mosya/cl/AC1c.pdf](https://people.cas.uab.edu/~mosya/cl/AC1c.pdf)). Proves that the algebraic Kåsa fit is fast and closed-form on wide arcs ($120–180^\circ$) but suffers from severe small-radius bias on short arcs ($\ll 120^\circ$), justifying the secant turning-angle metric for `v3`'s short counter-stroke.
3. **OpenAI Image Generation (`gpt-image-1` / ChatGPT) Native Square Resolution:** OpenAI Platform Documentation, *"Image generation — Sizes and quality"* ([platform.openai.com/docs/guides/image-generation](https://platform.openai.com/docs/guides/image-generation)). Documents that square generations output at `1024×1024` (requiring the downstream Lanczos resize to `1080×1080`).
4. **ITU-R BT.709 Luma Weights:** International Telecommunication Union, *Recommendation ITU-R BT.709-6: Parameter values for the HDTV standards for production and international programme exchange* ([itu.int/rec/R-REC-BT.709](https://www.google.com/search?q=https://www.itu.int/rec/R-REC-BT.709)). Defines the standard coefficients $Y = 0.2126 R + 0.7152 G + 0.0722 B$.
5. **ImageMagick 7 Resampling, Clamping, and Video Delegates:** ImageMagick Studio LLC, *"Command-line Options (`-filter Lanczos`, `-define filter:clamp=true`, `-connected-components`)"* and *"Resampling Filters — Ringing Artifacts"* ([imagemagick.org/script/command-line-options.php](https://imagemagick.org/script/command-line-options.php)). Documents Lanczos negative-lobe ringing and clamping behavior.

Want the complete runnable Python + NumPy validation and atlas-packing script?

---

**[TURN 1 · Claude → Gemini · Self-review 1]**

````text
Review your latest full answer above against the brief, the facts and the constraints. It FAILS only…

Review your latest full answer above against the brief, the facts and the constraints. It FAILS only for a real defect: a wrong fact or source, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a worker to execute. Wording, style and optional extra ideas are not defects.

If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)

Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff).
````

**[TURN 1 · Gemini answer]**

VERDICT: FAIL

### Defects in the Previous Answer

1. **Broken ImageMagick 7 connected-components command (Part B, Step 1):** The command `magick frame.png -fx "0.2126*r+0.7152*g+0.0722*b" -threshold 10% -define connected-components:connectivity=8 -connected-components 8 -auto-level PNG16:labels.png` does not output integer component IDs. By default in ImageMagick 7, `-connected-components` colors each region with its mean input color (which on a thresholded binary image paints every foreground component white, `65535`), and `-auto-level` rescales values rather than preserving discrete labels. A pure-NumPy/Python 8-connected breadth-first search (BFS) labeler must be specified directly.
2. **Non-NumPy dependencies and vague centerline tracking (Part B, Steps 2 and 7):** Step 2 referenced a "Savitzky–Golay" filter (which requires `scipy.signal`, violating Fact 4: *"Python with numpy only, plus ImageMagick 7"*), and Step 7 specified *"medial-axis ridge tracking within each stroke's 16 px corridor"* without giving an executable pure-NumPy algorithm.
3. **Destructive frame blending during temporal resampling (Part B, Step 8):** Blending adjacent frames linearly when resampling $N \in [12, 23]$ frames to 24 frames blurs the stepped anime/donghua edges and averages out the `1–3 px` white-gold hot line (`Y >= 0.85`), causing hot pixels to drop below the `0.85` threshold and creating double-edge ghosting. Nearest-neighbor integer frame indexing (preferring $N=24$) must be used to preserve crisp stepped cel boundaries.
4. **Stretching risk in the A2/A3 normalization command (Part B, Step 0):** Using `-resize 1080x1080!` with the exclamation mark forces an aspect-ratio stretch if an input image is not already strictly `1:1`. Replacing `-resize 1080x1080!` with `-resize 1080x1080 -background "#000000" -gravity center -extent 1080x1080` guarantees aspect-preserving scaling with pure-black padding.
5. **Unstable chord-bulge sign on nearly straight short counter-strokes (Part B, Step 4):** Using only the midpoint chord-bulge sign $\sigma_k = \text{sign}(b_k)$ to orient the outward normal $\mathbf{N}_{\text{out}, k}(s)$ can flip on `v3`'s short leftward counter-stroke if its midpoint lies within `1–2 px` of its root-to-tip chord. The outward normal needs a deterministic fallback pointing away from the Kåsa circle center (for curved strokes) and away from the fan's interior centroid (for low-curvature short flicks).

### Corrected Full Analysis and Solution

#### 1. Review of the Inherited Brief and the Previous Assistant's Handoff

##### 1.1 What We Agree With in the Handoff

- **Division of labor between the Firefly clip and the Three.js shader:** Fact 5 states that the in-game shader performs the 2–4 frame stroke-order reveal (`reveal_order` mask) and the tip-to-root erosion (`survival_order` mask). Therefore, A2 (Frame 0) should already show the complete three-stroke fan, A3 provides the late-decay target so Firefly generates directional tip-to-root motion rather than closing the arc, and the 24-frame atlas extracted from A4 should capture a living, mostly intact flame window so the clip and shader do not extinguish the flame twice.
- **Removing the A2 counter-stroke contradiction:** The inherited A2 prompt asked to *"Add four or five small counter-strokes, a few detached licks"*, which violates the inherited check requiring *"exactly 3 main strokes"* and *"outside a 24 px dilation of the three strokes at most 2–3 loose bits"*.
- **Exempting `v3`'s short leftward root flick from the `120–180°` Kåsa circle sweep:** In `v3`, the third stroke is a short counter-stroke flicking left at the root. As proven by Chernov (2010), the algebraic Kåsa circle fit is strongly biased toward small radii and inflated sweep angles on short, noisy arcs. Measuring the short flick via total tangent turning angle is mathematically sound.
- **Removing "erupt" from A4's opening:** Asking Firefly to *"erupt from one lower-left strike point"* when Frame 0 already shows the full fan encourages the model to either fade out and re-erupt or push the tips forward into a 300° C-ring.
- **Adding spatial checks for the white-gold hot line:** Checking only whether global hot pixels (`Y >= 0.85`) equal `2–6%` of lit pixels cannot verify whether the white-gold sits on the leading outer edge or pools inside the stroke interior.
- **Preflighting MP4 decoding:** `numpy` cannot read `.mp4` streams natively; ImageMagick 7 requires its `ffmpeg` delegate installed on the host machine.

##### 1.2 Every Error and Gap (in Both the Inherited Plan and the Handoff) — With Fixes

| Source | Error or Gap | Fix |
|---|---|---|
| **Original A2 & Handoff A2 prompts** | **Asking ChatGPT to "Add" white-gold when `v1` (8.1%) and `v3` (8.9%) already exceed the `2–6%` hot-pixel ceiling:** Telling the model to *"Add a razor-thin... hot line"* leaves existing interior hot regions intact, failing the `2–6%` check. (The handoff masked this defect by widening the hard check to `1–10%` instead of fixing the prompt.) | Instruct ChatGPT to **narrow and pare back** the existing white-gold highlights into a discontinuous razor-thin line strictly along the convex leading outer edges (`3–4%` of lit area) and shift interior bright spots down to warm amber/orange so `Y >= 0.85` lands inside `2–6%`. |
| **Handoff A2 prompts** | **Raw hex string `#FFF4D6` inside the image prompt:** Image generation models (`gpt-image-1`) often render literal hex strings as text artifacts or color swatch blocks. | Replace `#FFF4D6` in the prompt with descriptive color terms (*"pale ivory white-gold"* over *"stepped deep crimson, vermilion, bright tangerine and warm amber"*). |
| **Original A2 prompts** | **Requesting `"1080x1080"` in text without a margin buffer:** ChatGPT (`gpt-image-1`) outputs square images at `1024×1024` before downstream Lanczos scaling to `1080×1080`, and `"Center the whole fan"` often leaves less than 8% margin near the tips. | Ask for a `1:1` square reframing with at least a **10% pure-black margin** around all four borders so the flame stays comfortably inside the 8% (`87 px`) margin after scaling. |
| **Handoff A4 prompt** | **Negative verb `"do not erupt again"` in sentence 1 + `"first half / second half"` timeline syntax:** Diffusion text encoders weight early verbs heavily and handle negation poorly; `"erupt"` in clause 1 still triggers eruption motion priors. Single-prompt video diffusion also struggles with fractional timeline instructions. | Start with a positive state description (*"Already-ignited three-stroke anime brushfire fan burning in place..."*) with zero occurrences of `"erupt"`, and describe natural physical progression (*"Hold peak intensity briefly, then slowly erode from needle tips to middle islands down to the final frame's dark crimson root embers"*). |
| **Handoff Step 5** | **Non-existent Firefly UI toggle `"prompt enhancement off"`:** The Adobe Firefly Video web interface does not have a "prompt enhancement off" setting. | Use only verified Adobe Firefly Video settings: `Firefly Video` model, `First frame + Last frame`, `1:1`, `1080p`, `24 fps`, `5 s`, `Transparent background` off, camera motion `Static / None`. |
| **Handoff Step 3 (Margin check)** | **Off-by-one boundary error (`86–993`):** At `1080×1080`, 8%×1080=86.4 px. In 0-indexed coordinates `0..1079`, index `86` leaves `86 px` (7.96%) on the top/left and `993` leaves `1079 - 993 = 86 px` (7.96%) on the right/bottom, failing a strict ≥8% margin check. | Require `87 <= x <= 992` and `87 <= y <= 992` in 0-indexed pixel coordinates (≥87 px=8.055% margin on every edge). |
| **Handoff Step 3 ("Leading outer edge")** | **Vague human-dependent definition:** The handoff asks a person to *"annotate... the intended outer-edge side"* and checks *"≥ 80% on approved outer edges, excluding glints"* without giving a mathematical formula for the outer-edge zone or glint isolation. | Compute the outward unit normal N out,k 	​  (s) automatically from the Kåsa circle center (with fan-centroid fallback for straight flicks), isolate pinpoint glints by connected-component area (`1 to 36 px²`) and aspect ratio (`0.5 to 2.0`), and require ≥80% of remaining hot pixels to lie in the outer rim band. |
| **Brief & Handoff (Taper W 20 	​  /W 80 	​ )** | **Root-merging and zero-tip-width failure modes:** Near the shared lower-left strike root (s=0.20L k 	​ ), normal rays from one stroke can cross into an adjacent stroke, inflating W 20 	​ . Conversely, if a tip erodes early (W 80 	​  =0), W 20 	​  /W 80 	​  =∞, passing a broken stroke. | Partition the `lit` mask into 3 Voronoi stroke territories by minimum Euclidean distance to the 3 centerlines before marching along normals, and require W 80 	​  ≥1.5 px and lit coverage to at least s=0.95L k 	​ . |
| **Handoff Step 3 ("Closes into a C")** | **Contradictory thresholds (`175°` max sweep vs `0.55` chord-to-arc ratio):** For a circular arc of sweep θ, chord/arc= θ 2sin(θ/2) 	​ , which equals `0.654` at 175 ∘ and `0.637` at 180 ∘. A ratio of `0.55` permits a **204 ∘** C-arc. | Align per-stroke sweep (≤180 ∘) with chord-to-arc ratio (≥0.60), and add two automated whole-fan checks: polar angular wrap Θ fan 	​  ≤185 ∘ around the longest crescent's Kåsa center, and zero enclosed interior cavities after a `12 px` disk dilation. |
| **Brief & Handoff (A3 shift check)** | **Unmasked luma cross-correlation fails on in-place burn-down:** When tips vanish and roots cool to dark crimson (`Y ~ 0.25`) while middle islands stay brighter (`Y ~ 0.50`), raw luma cross-correlation drags A3's middle islands toward A2's bright root, reporting a false `10–24 px` shift. | Compute **Zero-Mean Normalized Cross-Correlation (ZNCC)** on soft-clipped masks S=min(Y/0.15,1.0) restricted to the `12 px`-dilated footprint of A3 (`dilate_disk(lit_A3, 12)`), over shifts (Δx,Δy)∈[−24,24] 2. |
| **Handoff Step 7 (Atlas cell scaling)** | **Scaling cells to `376×376` with `4 px` padding breaks shader mask registration:** Shrinking frames to `376 / 384 = 97.9%` shifts the flame inward by up to `11 px` (at `1080p` scale) relative to the static `reveal_order` and `survival_order` masks painted over A2. | Resize each `1080×1080` frame directly to `384×384` (since the `87 px` margin at `1080p` already provides `30.9 px` of pure-black margin at `384×384`), and zero out the outer `2 px` border in place (`cell[:2,:]=0`, etc.) to block Lanczos ringing or bilinear bleed without shifting UVs. |

#### 2. Final Prompts (Written Out in Full)

##### A2-v1 (First Frame from `v1` painting)

Attach only the original `v1` (`1536×1024`) painting in ChatGPT image editing (`1:1` square output):

> Edit the attached painting into a 1:1 square opaque pure-black canvas by reframing the entire flame fan inward so at least 10 percent pure-black margin surrounds all four sides, without cropping, stretching, rotating or mirroring. Keep the lower-left strike root and exactly three separate OPEN flame crescents sweeping up-right (long, medium, short), each curving between 120 and 160 degrees and never closing into a C or ring. Give every stroke a heavy irregular root that tapers smoothly to a needle-fine tip at most one-third of its root width. Use a stepped anime/donghua fire palette of deep crimson, vermilion, bright tangerine and warm amber with soft living interior tongues. Narrow the existing pale ivory white-gold highlights into a razor-thin, slightly broken line strictly hugging each convex leading outer edge (covering only 3 to 4 percent of the flame area) plus two or three tiny pinpoint glints. Include at most two small detached ember specks near the tips; absorb any extra root flicks into the three main roots. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.

##### A2-v3 (First Frame from `v3` painting)

Attach only the original `v3` (`1536×1024`) painting in ChatGPT image editing (`1:1` square output):

> Edit the attached painting into a 1:1 square opaque pure-black canvas by reframing the entire flame fan inward so at least 10 percent pure-black margin surrounds all four sides, without cropping, stretching, rotating or mirroring. Keep the lower-left strike root and resolve the flame into exactly three separate OPEN strokes: two long crescents sweeping up-right (curving between 120 and 160 degrees, never closing into a C or ring) and one short counter-stroke flicking sharply left at the root. Do not lengthen the short left flick into a third crescent. Give all three strokes heavy irregular roots that taper smoothly to needle-fine tips at most one-third of their root width. Use a stepped anime/donghua fire palette of deep crimson, vermilion, bright tangerine and warm amber with soft living interior tongues. Narrow the existing pale ivory white-gold highlights into a razor-thin, slightly broken line strictly hugging each convex leading outer edge (covering only 3 to 4 percent of the flame area) plus two or three tiny pinpoint glints. Include at most two small detached ember specks; merge any other loose bits into the three strokes. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.

##### A3 (End Frame from the chosen `1080×1080` A2 frame)

Attach only the normalized `1080×1080` A2 image (generate a matching A3 for each A2 candidate entering A4):

> Edit the attached image in place on the exact same opaque pure-black 1:1 canvas. Keep the lower-left root and all three stroke paths locked at their exact pixel coordinates; do not shift, scale, rotate, extend or reconnect anything. Show the same three strokes late in their burn-down: needle tips completely vanished, middle sections broken into small separated orange-red islands, and thick roots cooled into dark crimson and muted ember cores, with two or three tiny dying ember specks along the original paths. Total lit flame area must be about one-quarter of the attached image, with almost no white-gold remaining. No new flames, arcs, C-shape, ring, lotus, bird, smoke, glow haze or text.

##### A4 (Adobe Firefly Video — **537 characters** including spaces)

Settings: **Adobe Firefly Video**, **First frame** = normalized `1080×1080` A2, **Last frame** = normalized `1080×1080` A3, aspect ratio **1:1**, resolution **1080p**, frame rate **24 fps**, duration **5 s**, transparency **Off**, camera motion **Static / None**.

> Already-ignited three-stroke anime brushfire fan burning in place on a fixed pure-black canvas. Keep the lower-left strike root, three separate open curved paths, and sharp needle tips locked in position. Stepped orange-red flame tongues surge along each stroke with a hair-thin white-gold shimmer hugging the convex outer edges. Hold peak intensity briefly, then slowly erode from needle tips to middle islands down to the final frame's dark crimson root embers. Static camera. No closing C-arc, ring, lotus, bird, smoke, bloom or text.

*(Character count: exactly 537 characters, under the 600-character limit.)*

#### 3. Exact Script-Ready Check Definitions (Python + NumPy + ImageMagick 7 Only)

##### 3.1 Normalization and Frame Extraction (ImageMagick 7)

1. **Normalize A2 and A3 to `1080×1080` 8-bit sRGB PNG (aspect-ratio preserving, no stretching, clamped Lanczos lobes):**Bash`magick input.png -alpha off -colorspace sRGB -filter Lanczos -define filter:clamp=true -resize 1080x1080 -background "#000000" -gravity center -extent 1080x1080 -depth 8 PNG24:output_1080.png
`
2. **Preflight and extract Firefly MP4 runs (`ff_run1..3.mp4`) to 120 PNG frames:**
Verify `magick -list delegate | grep -i ffmpeg` returns a valid `ffmpeg` delegate, then run:Bash`magick ff_run1.mp4 -alpha off -colorspace sRGB -coalesce -depth 8 PNG24:frames/frame_%03d.png
`
  Confirm `120` frames (`frame_000.png` .. `frame_119.png`) of shape `(1080, 1080, 3)` exist. Load PNGs into NumPy via a lightweight `magick frame.png -depth 8 RGB:-` pipe (`np.frombuffer(raw_bytes, dtype=np.uint8).reshape(1080, 1080, 3)`), requiring zero third-party Python imaging libraries.

##### 3.2 Base Masks, Pure-NumPy Connected Components, and Disk Dilation

Python```
from collections import deque
import numpy as np

def compute_luma_and_masks(img_u8: np.ndarray):
  rgb = img_u8.astype(np.float64) / 255.0
  Y = 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]
  lit = Y > 0.10
  hot = Y >= 0.85
  return Y, lit, hot

def dilate_disk(mask: np.ndarray, radius: int) -> np.ndarray:
  y, x = np.ogrid[-radius : radius + 1, -radius : radius + 1]
  kernel = (x * x + y * y <= radius * radius).astype(np.float64)
  H, W = mask.shape
  kh, kw = kernel.shape
  f_m = np.fft.rfft2(mask.astype(np.float64), s=(H + kh - 1, W + kw - 1))
  f_k = np.fft.rfft2(kernel, s=(H + kh - 1, W + kw - 1))
  conv = np.fft.irfft2(f_m * f_k, s=(H + kh - 1, W + kw - 1))
  return conv[radius : radius + H, radius : radius + W] > 0.5

def label_connected_components_8(mask: np.ndarray):
  H, W = mask.shape
  labels = np.zeros((H, W), dtype=np.int32)
  sizes = {}
  comp_id = 0
  nbrs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  ys, xs = np.nonzero(mask)
  for y0, x0 in zip(ys, xs):
    if labels[y0, x0] != 0:
      continue
    comp_id += 1
    labels[y0, x0] = comp_id
    q = deque([(y0, x0)])
    cnt = 0
    while q:
      cy, cx = q.popleft()
      cnt += 1
      for dy, dx in nbrs:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and labels[ny, nx] == 0:
          labels[ny, nx] = comp_id
          q.append((ny, nx))
    sizes[comp_id] = cnt
  return labels, sizes
```

##### 3.3 Centerline Parameterization, Long-Crescent Kåsa Sweep, and Short-Stroke Turning Angle

For each stroke $k \in \{1, 2, 3\}$, a human records $M \ge 10$ ordered centerline points $P_0, P_1, \dots, P_{M-1}$ in $(x, y)$ pixel coordinates from root ($P_0$) to tip ($P_{M-1}$).

1. **Pure-NumPy arc-length resampling & Gaussian smoothing:**
Compute cumulative chord distances along $P_0 \dots P_{M-1}$ with total length $L_k$. Interpolate via `np.interp` at $1.0\text{ px}$ steps $s_j = j$ for $j = 0, \dots, n$ ($n = \lfloor L_k \rfloor$). Smooth interior points with a 1D Gaussian kernel `g = np.exp(-0.5 * (np.arange(-9, 10) / 3.0)**2); g /= g.sum()` using endpoint padding (`np.pad(..., mode='edge')`) while pinning $C_k(0) = P_0$ and $C_k(L_k) = P_{M-1}$. Compute unit tangents $\mathbf{T}_k(s_j)$ via central differences normalized to unit length.
2. **Stroke classification:**
  - A stroke is the **`v3` short counter-stroke** iff $L_k \le 260\text{ px}$ and $x_{\text{tip}} \lt x_{\text{root}}$ (flicks left from the root).
  - Every other main stroke is a **crescent** and must have $L_k \gt 260\text{ px}$, $x_{\text{tip}} \gt x_{\text{root}}$, and $y_{\text{tip}} \lt y_{\text{root}}$ (sweeping up-right).
  - In `v1`, all 3 strokes must be crescents (`long, medium, short` with $L_1 \gt L_2 \gt L_3 \gt 260\text{ px}$). In `v3`, exactly 2 strokes are crescents and 1 is the short leftward counter-stroke.
3. **Kåsa circle fit & unwrapped sweep (for all crescents):**
Solve the linear least-squares system $A \mathbf{w} \approx \mathbf{b}$ via `np.linalg.lstsq(A, b, rcond=None)` where row $j$ of $A$ is $[x_j, y_j, 1]$ and $b_j = -(x_j^2 + y_j^2)$. The fitted circle center and radius are:
  $$
x_{c,k} = -\frac{w_0}{2}, \qquad y_{c,k} = -\frac{w_1}{2}, \qquad R_k = \sqrt{x_{c,k}^2 + y_{c,k}^2 - w_2}
$$
  Compute polar angles $\phi_j = \text{atan2}(y_j - y_{c,k},\; x_j - x_{c,k})$, unwrap along the ordered centerline via `phi_u = np.unwrap(phi)`, and compute:
  $$
\theta_{\text{Kasa}, k} = \frac{180^\circ}{\pi} \bigl|\phi_u[-1] - \phi_u[0]\bigr|
$$
  - **Pass requirement (crescents):** $120^\circ \le \theta_{\text{Kasa}, k} \le 180^\circ$ AND chord-to-arc ratio $\frac{\Vert{}P_{M-1} - P_0\Vert{}}{L_k} \ge 0.60$.
4. **Arc / turning measurement for the `v3` short counter-stroke:**
Because the algebraic Kåsa fit underestimates radius and inflates angle on short arcs (Chernov 2010), subsample the smoothed centerline $C_k(s)$ at step $\delta = \max(0.08 L_k, 8.0\text{ px})$ to get unit secant vectors $\mathbf{u}_m$, and sum the signed turning increments:
  $$
\Delta\theta_{\text{turn}, k} = \frac{180^\circ}{\pi} \left|\sum_{m} \text{atan2}\bigl(u_{m,x} u_{m+1,y} - u_{m,y} u_{m+1,x},\; \mathbf{u}_m \cdot \mathbf{u}_{m+1}\bigr)\right|
$$
  - **Pass requirement (`v3` short counter-stroke):** $x_{\text{tip}} \lt x_{\text{root}}$, $80\text{ px} \le L_k \le 260\text{ px}$, $15^\circ \le \Delta\theta_{\text{turn}, k} \le 110^\circ$, and chord-to-arc ratio $\frac{\Vert{}P_{M-1} - P_0\Vert{}}{L_k} \ge 0.72$.

##### 3.4 Stroke Territory Partition, 3-Stroke Separation, and Taper ($W_{20} / W_{80}$)

1. **Voronoi stroke territory assignment:**
For every pixel $\mathbf{p} = (x, y)$ with `lit[y, x] == True`, compute its distance $d_k(\mathbf{p}) = \min_{j} \|\mathbf{p} - C_k(s_j)\|$ to each of the 3 centerlines. Assign $\mathbf{p}$ to stroke $k^*(\mathbf{p}) = \arg\min_{k \in \{1,2,3\}} d_k(\mathbf{p})$ if $d_{k^*}(\mathbf{p}) \le 24.0\text{ px}$. Pixels with $\min_k d_k(\mathbf{p}) \gt 24.0\text{ px}$ are outside the 24 px stroke dilation (loose bits).
2. **Openness / separation between the 3 strokes:**
For all stations $s \in [0.25 L_k, 1.0 L_k]$ past the shared lower-left strike root, verify that along the line segment connecting any point $C_k(s)$ on stroke $k$ to its nearest point $C_m(s')$ on any other stroke $m \neq k$, there are at least `2` contiguous unlit pixels (`Y <= 0.10`), confirming the strokes do not merge or close into a loop.
3. **Normal width $w_k(s_j)$ and taper ratio $W_{20,k} / W_{80,k}$:**
At station $s_j$, let $\mathbf{N}_k(s_j) = (-T_{k,y}(s_j), T_{k,x}(s_j))$ be the unit normal. Sample the territory-gated lit mask $I_k(x, y) = \mathbb{1}[\text{lit}(x, y) \land (k^*(x, y) == k)]$ along $C_k(s_j) + u\,\mathbf{N}_k(s_j)$ at step $\Delta u = 0.25\text{ px}$ using bilinear interpolation of $Y$ ($Y \gt 0.10$) and nearest-integer lookup of $k^*$.
March outward in $+u \ge 0$ until $I_k = 0$ at $u = r_{+,k}(s_j)$ and in $-u \le 0$ until $I_k = 0$ at $u = -r_{-,k}(s_j)$ (if $C_k(s_j)$ falls in a `<= 2 px` interior tongue gap, start the contiguous run at the nearest lit sample within $|u| \le 2.0\text{ px}$). Set $w_k(s_j) = r_{+,k}(s_j) + r_{-,k}(s_j)$.
With half-window $\Delta_w = \max(0.03 L_k, 5.0\text{ px})$:
  $$
W_{20, k} = \text{median}\bigl\{w_k(s_j) : |s_j - 0.20 L_k| \le \Delta_w\bigr\}, \qquad W_{80, k} = \text{median}\bigl\{w_k(s_j) : |s_j - 0.80 L_k| \le \Delta_w\bigr\}
$$
  *(For `v3`'s short counter-stroke, if $s = 0.20 L_k$ lies inside the shared root radius of stroke 1, evaluate $W_{20,k}$ at $s = 0.25 L_k \pm 5.0\text{ px}$.)*
  - **Pass requirement:** $W_{80,k} \ge 1.5\text{ px}$, lit stroke coverage reaches at least $s = 0.95 L_k$, and $\frac{W_{20,k}}{W_{80,k}} \ge 3.0$ for all crescents ($\ge 2.5$ for the `v3` short counter-stroke).

##### 3.5 Exact "Leading Outer Edge" Decision Rule for the Hot Line

1. **Unambiguous outward normal $\mathbf{N}_{\text{out}, k}(s_j)$:**
  - **For crescents ($L_k \gt 260\text{ px}$):** The vector from the Kåsa circle center $\mathbf{O}_k = (x_{c,k}, y_{c,k})$ to $C_k(s_j)$ always points toward the **convex outer edge**. Define the sign $\sigma_k \in \{-1, +1\}$ by the median dot product along the stroke:
    $$
\sigma_k = \text{sign}\!\left(\text{median}_{j}\Bigl[\bigl(C_k(s_j) - \mathbf{O}_k\bigr) \cdot \mathbf{N}_k(s_j)\Bigr]\right)
$$
  - **For `v3`'s short counter-stroke ($L_k \le 260\text{ px}$):** Compute the midpoint chord bulge $b_k = \bigl(C_k(0.5 L_k) - P_0\bigr) \cdot \mathbf{N}_{\perp, k}$ where $\mathbf{N}_{\perp, k}$ is the left unit normal of the chord $P_{M-1} - P_0$. If $\vert{}b_k\vert{} \ge 3.0\text{ px}$, set $\sigma_k = \text{sign}\bigl(\text{median}_j[\mathbf{N}_k(s_j) \cdot (b_k \mathbf{N}_{\perp, k})]\bigr)$. Otherwise (nearly straight flick), orient $\sigma_k$ so $\mathbf{N}_{\text{out}, k}$ points away from the mean centroid of the two main crescents (the outer leading side of the counter-slash).
  - In both cases, $\mathbf{N}_{\text{out}, k}(s_j) = \sigma_k\,\mathbf{N}_k(s_j)$, and the local outer half-width to the boundary of `lit` is $r_{\text{out}, k}(s_j) = r_{+,k}(s_j)$ if $\sigma_k = +1$ else $r_{-,k}(s_j)$.
2. **Isolating pinpoint glints:**
Run `label_connected_components_8(hot)`. Any 8-connected component of `hot` ($Y \ge 0.85$) with area between `1` and `36 px²` and bounding-box aspect ratio in `[0.5, 2.0]` is classified as a **pinpoint glint** (require `1 to 4` such glints in A2).
3. **Leading-outer-edge test on remaining hot pixels:**
For every non-glint hot pixel $\mathbf{p}$ assigned to stroke $k$ with nearest centerline station $s^*(\mathbf{p})$, compute its outward normal coordinate:
  $$
d_{\text{out}}(\mathbf{p}) = \bigl(\mathbf{p} - C_k(s^*)\bigr) \cdot \mathbf{N}_{\text{out}, k}(s^*)
$$
  Pixel $\mathbf{p}$ lies on the **leading outer edge** iff:
  $$
d_{\text{out}}(\mathbf{p}) \gt 0 \quad \text{AND} \quad d_{\text{out}}(\mathbf{p}) \ge \max\bigl(0.50\,r_{\text{out}, k}(s^*),\; r_{\text{out}, k}(s^*) - 4.0\text{ px}\bigr)
$$
  - **Pass requirements:**
    1. Global hot fraction: $0.02 \le \frac{\sum \text{hot}}{\sum \text{lit}} \le 0.06$ (`2.0% to 6.0%`).
    2. Outer-edge placement: $\ge 80\%$ of non-glint hot pixels satisfy the leading-outer-edge condition above, and $\ge 90\%$ satisfy $d_{\text{out}}(\mathbf{p}) \gt 0$.
    3. Outer-edge continuity: Across $s \in [0.15 L_k, 0.85 L_k]$, at least $40\%$ of stations on each crescent ($\ge 25\%$ on the short flick) have a leading-outer-edge hot pixel within $\pm 2.0\text{ px}$ of station $s$.

##### 3.6 Margins, Loose Bits, and Corner Black (A2)

- **8% Margin check:** Using `label_connected_components_8(lit)`, discard components with area $\lt 0.0005 \times \sum \text{lit}$ ($0.05\%$). All remaining `lit` pixels must satisfy `87 <= x <= 992` and `87 <= y <= 992` (0-indexed).
- **Loose bits outside 24 px stroke dilation:** Let $M_{\text{strokes}}$ be the union of pixels with $\min_k d_k(\mathbf{p}) \le 24.0\text{ px}$. Run `label_connected_components_8(lit & (~M_strokes))`. Ignore 1–3 px quantization specks (`area < 4 px²`). Require **at most 3 components**, each with area $\le 0.02 \times \sum \text{lit}$.
- **Corner black:** In all four $16 \times 16$ corner regions (`img[:16, :16]`, `img[:16, -16:]`, `img[-16:, :16]`, `img[-16:, -16:]`), require `img_u8.max() <= 8`.

##### 3.7 End-Frame (A3) Checks

1. **Lit area ratio:** $0.15 \le \frac{\sum \text{lit}_{\text{A3}}}{\sum \text{lit}_{\text{A2}}} \le 0.35$.
2. **Containment inside 12 px dilated A2 mask:** Let $D_{12} = \text{dilate\_disk}(\text{lit}_{\text{A2}}, 12)$. Require $\frac{\sum (\text{lit}_{\text{A3}} \land D_{12})}{\sum \text{lit}_{\text{A3}}} \ge 0.70$ (target $\ge 0.85$).
3. **Shift $\le 4\text{ px}$ by masked cross-correlation within $\pm 24\text{ px}$:**
Compute soft-clipped occupancy maps $S_{\text{A2}} = \min(Y_{\text{A2}} / 0.15, 1.0)$ and $S_{\text{A3}} = \min(Y_{\text{A3}} / 0.15, 1.0)$, and restrict the evaluation domain to $W = \text{dilate\_disk}(\text{lit}_{\text{A3}}, 12)$ so A2's extinguished tips do not bias the correlation peak. For every integer shift $(\Delta x, \Delta y) \in [-24, 24]^2$, evaluate the Zero-Mean Normalized Cross-Correlation $\text{ZNCC}(\Delta x, \Delta y)$ between $S_{\text{A2}}$ and shifted $S_{\text{A3}}$ inside $W$. The best shift $(\Delta x^*, \Delta y^*) = \arg\max \text{ZNCC}(\Delta x, \Delta y)$ must satisfy $\sqrt{(\Delta x^*)^2 + (\Delta y^*)^2} \le 4.0\text{ px}$.
4. **Survival order & hot burnout:** Partition $\text{lit}_{\text{A2}}$ into Root ($s \in [0, 0.33 L_k]$), Middle ($s \in (0.33 L_k, 0.67 L_k]$), and Tip ($s \in (0.67 L_k, 1.0 L_k]$) zones. Require A3 survival fractions to obey $f_{\text{root}} \gt f_{\text{mid}} \gt f_{\text{tip}}$ with $f_{\text{tip}} \le 0.10$, and require $\frac{\sum \text{hot}_{\text{A3}}}{\sum \text{lit}_{\text{A3}}} \le 0.005$.

##### 3.8 Measurable Rule for "Closes into a C", Segment Selection, and 24-Frame Atlas Generation (A4)

1. **Measurable rule for "Closes into a C" (evaluated on every frame $t \in \{0, \dots, 119\}$):**
Frame $t$ closes into a C or ring if ANY of the following holds:
  - **C1 (Whole-fan polar angular wrap $\gt 190^\circ$):** Around the Kåsa center $(x_{c,1}, y_{c,1})$ of the longest crescent in Frame 0, compute polar angles $\phi(\mathbf{p}) \in [-180^\circ, 180^\circ)$ for all $\mathbf{p} \in \text{lit}_t$. Bin into 360 $1^\circ$ bins; mark bin $b$ occupied if it contains $\ge 10$ lit pixels. Let $\Delta\phi_{\text{gap}}(t)$ be the longest contiguous cyclic run of empty bins. The fan's angular span is $\Theta_{\text{fan}}(t) = 360^\circ - \Delta\phi_{\text{gap}}(t)$. Reject the run if $\Theta_{\text{fan}}(t) \gt 190^\circ$ on any active frame ($\sum \text{lit}_t \ge 0.35 \sum \text{lit}_0$), and require $\Theta_{\text{fan}}(t) \le 185^\circ$ on every frame of the chosen segment.
  - **C2 (Enclosed interior cavity):** Compute $M_{\text{closed}}(t) = \text{dilate\_disk}(\text{lit}_t, 12)$ and label 8-connected components of `~M_closed(t)`. If any non-border background component has area $\ge 1{,}000\text{ px}^2$, reject the run.
  - **C3 (Single-stroke C-curl):** Any crescent centerline in frame $t$ has $\theta_{\text{Kasa}, k}(t) \gt 180^\circ$ or chord-to-arc ratio $\lt 0.60$.
2. **Pure-NumPy per-frame centerline propagation (with human verification on the winning segment):**
To measure all 3 strokes on every frame $t$ of a candidate 12–24 frame segment:
  - Seed frame $t$'s control points from frame $t-1$'s smoothed centerline stations $C_k^{(t-1)}(s_m)$ at $M = 15$ uniformly spaced stations $s_m \in [0, L_k]$.
  - At each station $m$, sample $Y_t$ along the normal ray $C_k^{(t-1)}(s_m) + u\,\mathbf{N}_k^{(t-1)}(s_m)$ for $u \in [-12.0, +12.0]\text{ px}$ (gated to stroke $k$'s Voronoi territory). Update the station position to the luma-weighted centroid:
    $$
C_k^{(t)}(s_m) = C_k^{(t-1)}(s_m) + \frac{\sum_{u: Y_t(u) \gt 0.10} u \, Y_t(u)}{\sum_{u: Y_t(u) \gt 0.10} Y_t(u)} \, \mathbf{N}_k^{(t-1)}(s_m)
$$
  - Re-run the Step 3.3–3.4 arc, separation, and taper checks on $C_k^{(t)}$ for every frame in the window, and have the reviewer visually confirm the overlaid polylines on the winning 12–24 frames.
3. **Picking the best 12–24 frame segment $[s, s + N - 1]$ ($12 \le N \le 24$):**
  - **Hard filter:** Every frame $t \in [s, s+N-1]$ must pass C1–C3 (no C/ring), margins (`87..992`), corner black (`<= 8`), 3 open strokes, crescent Kåsa sweep `120–180°` (`v3` short flick turning `15–110°`), dynamic taper $W_{20}/W_{80} \ge 2.5$ on every individual frame and $\text{median}_{t}(W_{20}/W_{80}) \ge 3.0$ across the window, ZNCC shift vs. Frame 0 $\le 4.0\text{ px}$, total lit area $\sum \text{lit}_t \in [0.65 \sum \text{lit}_s,\, 1.15 \sum \text{lit}_s]$, and no 6-frame sub-interval $[t, t+5]$ losing more than $15\%$ of $\sum \text{lit}_t$.
  - **Ranking score:** Among passing windows, pick the one maximizing:
    $$
J(s, N) = 2.0\,\frac{N}{24} + 1.5\,\text{mean}_{t}\bigl(\min(\text{core\_diff}(t, t+1), 0.18)\bigr) - 2.0\,\text{max}_{t}\bigl(\text{leak}(t)\bigr) - 1.0\,\text{std}_{t}\!\left(\frac{\sum \text{lit}_t}{\sum \text{lit}_s}\right)
$$
    where `core_diff(t, t+1)` is the mean $|Y_{t+1} - Y_t|$ inside `lit_0` and `leak(t)` is the fraction of `lit_t` outside `dilate_disk(lit_0, 12)`.
4. **Resampling to 24 frames and packing the `384×384` cell atlas:**
  - Select the 24 frame indices via crisp nearest-neighbor indexing (preserving stepped anime edges and hot-line luma without blending blur):
    $$
i_k = s + \left\lfloor \frac{k(N - 1)}{23.0} + 0.5 \right\rfloor, \qquad k = 0, 1, \dots, 23
$$
  - Resize each selected `1080×1080` frame directly to `384×384` (maintaining 1:1 UV alignment with the `1080×1080` shader masks):Bash`magick frame_ik.png -alpha off -colorspace sRGB -filter Lanczos -define filter:clamp=true -resize 384x384! -depth 8 PNG24:cell_k.png
`
  - Zero out the outer `2 px` border of each `384×384` cell in NumPy (`cell[:2,:]=0; cell[-2:,:]=0; cell[:,:2]=0; cell[:,-2:]=0`) to prevent edge bleed, then tile into a 24-frame atlas (`6×4` = `2304×1536`, or `5×5` = `1920×1920` with cell 25 black, matching the shader's UV grid uniform):Bash`magick montage cell_00.png ... cell_23.png -tile 6x4 -geometry 384x384+0+0 -background "#000000" -depth 8 PNG24:brushfire_atlas_24f.png
`

#### 4. Risks, Verification Checks, Uncertainties, and Cited Sources

##### Risks and How to Check Each

- **ChatGPT shifting stroke coordinates when generating A3:** Because `gpt-image-1` re-renders the whole canvas, A3 strokes can drift by `5–15 px`.
  - *Check & fix:* Run the Step 3.7 masked ZNCC check immediately. If $4.0\text{ px} \lt \text{shift} \le 12.0\text{ px}$ is a pure rigid translation, shift A3 back by $(-\Delta x^*, -\Delta y^*)$ using `np.roll` (zero-filling edges) and re-verify `>= 70%` containment inside `dilate_disk(lit_A2, 12)`; otherwise regenerate A3 using ChatGPT's inpainting brush masked strictly over the outer 75% of the three strokes so the lower-left root pixels remain untouched.
- **Firefly cross-dissolving instead of eroding tips-first:** Firefly's `First + Last frame` mode can linearly fade luma mid-clip.
  - *Check & fix:* The Step 3.8 window filter rejects any 6-frame drop exceeding `15%` and extracts the healthiest 12–24 frame living-flame interval from the first half of the 5-second clip, while the Three.js shader's `survival_order` mask guarantees clean tip-to-root erosion over the final `0.79 s` in-game.
- **H.264 macroblock noise lifting corner/background black above zero:**
  - *Check & fix:* Enforce the `corner black <= 8/255` check on every frame and set the shader's `smoothstep(lo, hi, max_RGB)` lower bound `lo >= 0.04` (`~10/255`) so dark compression noise never produces a visible rectangular card edge.

##### What We Are Not Sure About

1. **Exact row×column layout (`6×4` vs `5×5`) expected by the Three.js flipbook shader:** The brief specifies *"a 24-frame colour atlas with 384 px cells"* without stating the grid dimensions used by `ff-a1-c5`. Check the shader uniform before running `magick montage`.
2. **Exact inner-crescent sweep of the unedited `v1` painting:** We have the bounding boxes and hot-pixel percentages of `v1` and `v3`, but not the raw pixel files. If `v1`'s shortest inner crescent was painted with a sweep of `110–118°`, measure A2-v1 first and either let ChatGPT slightly curve the tip to `>= 120°` or set the inner-crescent lower bound to `110°`.

##### Cited Sources

1. **Adobe Firefly Video — First & Last Frame Keyframes, Resolution, Frame Rate, and Transparent Background Limits:** Adobe HelpX, *"Generate videos using images"* and *"Generate video using Firefly models"* ([helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html)). Confirms `1:1` `1080p` at `24 fps` for `5 s` with First and Last frames, and confirms that transparent background mode is restricted to `540p` `16:9`.
2. **Kåsa Circle Fit and Small-Arc Bias:** Kåsa, I. (1976), *"A circle fitting procedure and its error analysis"*, IEEE Transactions on Instrumentation and Measurement, 25(1), 8–14; and Chernov, N. (2010), *Circular and Linear Regression: Fitting Circles and Lines by Least Squares*, Chapman & Hall/CRC, Chapter 5 ([people.cas.uab.edu/~mosya/cl/AC1c.pdf](https://people.cas.uab.edu/~mosya/cl/AC1c.pdf)). Proves the closed-form linear least-squares formulation and its bias toward small radii on short arcs ($\ll 120^\circ$).
3. **OpenAI Image Editing (`gpt-image-1`) Square Output Resolution:** OpenAI Platform Documentation, *"Image generation — Sizes and quality"* ([platform.openai.com/docs/guides/image-generation](https://platform.openai.com/docs/guides/image-generation)). Confirms square image outputs are `1024×1024`.
4. **ITU-R BT.709 Luma Coefficients:** International Telecommunication Union, *Recommendation ITU-R BT.709-6* ([itu.int/rec/R-REC-BT.709](https://www.google.com/search?q=https://www.itu.int/rec/R-REC-BT.709)). Defines $Y = 0.2126 R + 0.7152 G + 0.0722 B$.
5. **ImageMagick 7 Resampling, Clamping, and Connected Components:** ImageMagick Studio LLC, *"Command-line Options (`-filter Lanczos`, `-define filter:clamp=true`, `-extent`, `-connected-components`)"* ([imagemagick.org/script/command-line-options.php](https://imagemagick.org/script/command-line-options.php)). Documents Lanczos lobe clamping, aspect-preserving `-resize` + `-extent`, and default mean-color rendering of `-connected-components`.

---

**[TURN 2 · Claude → Gemini · Self-review 2]**

````text
Review your latest full answer above against the brief, the facts and the constraints. It FAILS only…

Review your latest full answer above against the brief, the facts and the constraints. It FAILS only for a real defect: a wrong fact or source, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a worker to execute. Wording, style and optional extra ideas are not defects.

If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)

Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff).
````

**[TURN 2 · Gemini answer]**

VERDICT: PASS
Optional: When running `magick montage` for the 24-frame atlas, pass `-define png:color-type=2` alongside `PNG24:` so ImageMagick never auto-quantizes a low-color cell or atlas into an 8-bit indexed palette PNG.

---

**[TURN 3 · Claude → Gemini · Self-review 3]**

````text
Review your latest full answer above against the brief, the facts and the constraints. It FAILS only…

Review your latest full answer above against the brief, the facts and the constraints. It FAILS only for a real defect: a wrong fact or source, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a worker to execute. Wording, style and optional extra ideas are not defects.

If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)

Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff).
````

**[TURN 3 · Gemini answer]**

VERDICT: PASS
Optional: In the Python centerline-propagation step (Step 3.8.2), clamp each station's per-frame normal update to `[-4.0, +4.0]` pixels before re-smoothing along arc length so a detached ember passing through the 12 px search corridor cannot pull a centerline station off the stroke core.

---

**[TURN 4 · Claude → Gemini · Handoff request]**

````text
Write the final handoff in one message, at most about 1,500 words: 1) the final analysis, 2) the sol…

Write the final handoff in one message, at most about 1,500 words: 1) the final analysis, 2) the solution as ordered steps, 3) sources, 4) open questions and risks. No preamble. Include the final prompts A2-v1, A2-v3, A3 and A4 written out in full (with the A4 character count) and the exact numeric checks.
````

**[TURN 4 · Gemini answer]**

## 1. Final Analysis

The current baseline clip, `ff-a1-c5`, scored **6.5/10**: judges praised its living internal flame texture, but rejected it for four measurable defects:

1. The arc closes to roughly $300^\circ$ by frame 12 (reading as a C or ring).
2. Strokes lack taper ($W_{20}/W_{80} = 0.81$ versus the required ratio of at least $3.0$).
3. White-gold hot-line coverage is $0\%$.
4. The flame burns out in 6 frames ($0.25\text{ s}$), violating the fast-attack, slow-decay rule (decay at least $0.6\text{ s}$ and at least $3\times$ attack).

### Division of Responsibilities

In Three.js, the camera-facing card shader already executes the 2–4 frame stroke-order reveal (`reveal_order` mask), dark ink backing, hot core, and ordered tip-to-root erosion (`survival_order` mask). Consequently:

- **A2 (First Frame):** Establishes the complete, open three-stroke fan silhouette, progressive $3:1$ taper, stepped six-color anime palette (`#5E1220`, `#A8221A`, `#DC461C`, `#FF7E2A`, `#FFB43A`, `#FFF4D6`), and outer-edge white-gold hot line.
- **A3 (End Frame):** Holds the exact A2 stroke coordinates at roughly $25\%$ lit area (tips vanished, middles fragmented, roots cooled to dark crimson) so Firefly Video interpolates directional tip-to-root decay rather than curling the tips into a ring.
- **A4 (Firefly Video Clip & 24-Frame Atlas):** Supplies living internal flame motion across a selected 12–24 frame window where the three strokes remain open and intact, preventing the video and the shader from extinguishing the flame twice.

### Key Corrections to Prompts and Checks

1. **Paring back white-gold in A2:** Unedited `v1` ($8.1\%$ hot) and `v3` ($8.9\%$ hot) already exceed the $2\text{--}6\%$ hot-pixel limit. Asking ChatGPT to "add" white-gold keeps hot area too high. The revised A2 prompts instruct ChatGPT to *narrow* existing white-gold into a razor-thin outer-edge rim ($3\text{--}4\%$ of lit area) and avoid raw hex strings (`#FFF4D6`) that trigger text/swatch artifacts.
2. **Eliminating eruption priors in A4:** Opening the A4 prompt with "erupt" (even negated as "do not erupt") triggers diffusion motion priors that re-erupt or curl the tips into a $300^\circ$ loop. The revised A4 prompt anchors the fan as already ignited and burning in place.
3. **Handling `v3`'s short leftward counter-stroke:** Applying a $120\text{--}180^\circ$ algebraic Kåsa circle fit to `v3`'s short root flick is mathematically invalid because Kåsa is strongly biased toward small radii on short arcs (Chernov 2010). Long crescents use the Kåsa sweep; the short flick uses total signed secant turning angle.
4. **Preventing root bleed, correlation drift, and UV shifts:** Normal widths ($W_{20}$) are gated by Voronoi centerline territories so adjacent roots do not merge; A3 alignment uses Zero-Mean Normalized Cross-Correlation (ZNCC) masked to A3's dilated footprint so vanished tips do not bias the shift; and atlas cells scale directly from $1080\times 1080$ to $384\times 384$ (zeroing a $2\text{ px}$ border in place) to preserve $1:1$ UV alignment with the shader masks.

## 2. Solution — Ordered Execution

### Step 1 — Generate A2 Candidates (ChatGPT Image Editing)

Attach only the original $1536\times 1024$ painting (`v1` or `v3`) in $1:1$ square mode.

**Final Prompt A2-v1:**

Plaintext```
Edit the attached painting into a 1:1 square opaque pure-black canvas by reframing the entire flame fan inward so at least 10 percent pure-black margin surrounds all four sides, without cropping, stretching, rotating or mirroring. Keep the lower-left strike root and exactly three separate OPEN flame crescents sweeping up-right (long, medium, short), each curving between 120 and 160 degrees and never closing into a C or ring. Give every stroke a heavy irregular root that tapers smoothly to a needle-fine tip at most one-third of its root width. Use a stepped anime/donghua fire palette of deep crimson, vermilion, bright tangerine and warm amber with soft living interior tongues. Narrow the existing pale ivory white-gold highlights into a razor-thin, slightly broken line strictly hugging each convex leading outer edge (covering only 3 to 4 percent of the flame area) plus two or three tiny pinpoint glints. Include at most two small detached ember specks near the tips; absorb any extra root flicks into the three main roots. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

**Final Prompt A2-v3:**

Plaintext```
Edit the attached painting into a 1:1 square opaque pure-black canvas by reframing the entire flame fan inward so at least 10 percent pure-black margin surrounds all four sides, without cropping, stretching, rotating or mirroring. Keep the lower-left strike root and resolve the flame into exactly three separate OPEN strokes: two long crescents sweeping up-right (curving between 120 and 160 degrees, never closing into a C or ring) and one short counter-stroke flicking sharply left at the root. Do not lengthen the short left flick into a third crescent. Give all three strokes heavy irregular roots that taper smoothly to needle-fine tips at most one-third of their root width. Use a stepped anime/donghua fire palette of deep crimson, vermilion, bright tangerine and warm amber with soft living interior tongues. Narrow the existing pale ivory white-gold highlights into a razor-thin, slightly broken line strictly hugging each convex leading outer edge (covering only 3 to 4 percent of the flame area) plus two or three tiny pinpoint glints. Include at most two small detached ember specks; merge any other loose bits into the three strokes. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

### Step 2 — Normalize and Validate A2 (Python + NumPy + ImageMagick 7)

Normalize to an exact $1080\times 1080$ 8-bit sRGB PNG without stretching:

Bash```
magick input.png -alpha off -colorspace sRGB -filter Lanczos -define filter:clamp=true -resize 1080x1080 -background "#000000" -gravity center -extent 1080x1080 -depth 8 PNG24:a2_1080.png
```

In Python (`numpy` only), compute Rec.709 luma $Y = (0.2126 R + 0.7152 G + 0.0722 B)/255.0$, `lit = (Y > 0.10)`, and `hot = (Y >= 0.85)`. Implement 8-connected component labeling via a standard queue-based breadth-first search (`label_cc8(mask)`) and morphological disk dilation of radius $r$ via 2D FFT convolution (`dilate_disk(mask, r)` using `np.fft.rfft2`/`irfft2` with disk kernel $x^2 + y^2 \le r^2$).

For each stroke $k \in \{1,2,3\}$, a person records $M \ge 10$ ordered centerline points $P_0 \dots P_{M-1}$ from root to tip. Resample linearly via `np.interp` at $1.0\text{ px}$ arc-length steps $s_j \in [0, L_k]$ and smooth interior coordinates with a 1D Gaussian kernel ($\sigma = 3.0\text{ px}$, endpoints pinned) to obtain curve $C_k(s_j)$, unit tangent $\mathbf{T}_k(s_j)$, and unit normal $\mathbf{N}_k(s_j) = (-T_{k,y}(s_j), T_{k,x}(s_j))$.

- **Stroke Classification & Arc Check:**
  - *Crescents* ($L_k \gt 260\text{ px}$, $x_{\text{tip}} \gt x_{\text{root}}$, $y_{\text{tip}} \lt y_{\text{root}}$; all 3 strokes in `v1`, 2 in `v3`): Fit the algebraic Kåsa circle via `np.linalg.lstsq` on $A_j = [x_j, y_j, 1]$, $b_j = -(x_j^2 + y_j^2)$, giving center $\mathbf{O}_k = (-w_0/2, -w_1/2)$ and radius $R_k = \sqrt{x_{c,k}^2 + y_{c,k}^2 - w_2}$. Unwrap polar angles $\phi_j = \text{atan2}(y_j - y_{c,k}, x_j - x_{c,k})$ via `np.unwrap`. Require sweep $\theta_{\text{Kasa}, k} = \frac{180^\circ}{\pi}\vert{}\phi_{\text{unwrap}}[-1] - \phi_{\text{unwrap}}[0]\vert{} \in [120.0^\circ, 180.0^\circ]$ and chord-to-arc ratio $\Vert{}P_{M-1} - P_0\Vert{} / L_k \ge 0.60$.
  - *Short leftward counter-stroke in `v3`* ($80\text{ px} \le L_k \le 260\text{ px}$, $x_{\text{tip}} \lt x_{\text{root}}$): Subsample $C_k(s)$ at step $\delta = \max(0.08 L_k, 8.0\text{ px})$ to form unit secants $\mathbf{u}_m$. Require total turning angle $\Delta\theta_{\text{turn}, k} = \frac{180^\circ}{\pi}\bigl\vert{}\sum_m \text{atan2}(u_{m,x} u_{m+1,y} - u_{m,y} u_{m+1,x},\, \mathbf{u}_m \cdot \mathbf{u}_{m+1})\bigr\vert{} \in [15.0^\circ, 110.0^\circ]$ and chord-to-arc ratio $\ge 0.72$.
- **Voronoi Stroke Territories, Openness & Taper ($W_{20}/W_{80}$):**
  - Assign every `lit` pixel $\mathbf{p}$ within $24.0\text{ px}$ of the centerlines to its closest centerline $k^*(\mathbf{p}) = \arg\min_k \min_j \Vert{}\mathbf{p} - C_k(s_j)\Vert{}$. For all $s \in [0.25 L_k, L_k]$, require at least $2$ contiguous unlit pixels (`Y <= 0.10`) along the shortest line segment between $C_k(s)$ and any other stroke's centerline.
  - March along $C_k(s_j) + u\,\mathbf{N}_k(s_j)$ in $\Delta u = 0.25\text{ px}$ steps (bilinear $Y \gt 0.10$, gated by nearest-pixel $k^* == k$) to find contiguous lit half-widths $r_{+,k}(s_j), r_{-,k}(s_j)$ and width $w_k(s_j) = r_{+,k}(s_j) + r_{-,k}(s_j)$.
  - Using median half-window $\Delta_w = \max(0.03 L_k, 5.0\text{ px})$ around $0.20 L_k$ and $0.80 L_k$ (or $0.25 L_k \pm 5\text{ px}$ for `v3`'s short flick if $0.20 L_k$ touches the shared root), require $W_{80,k} \ge 1.5\text{ px}$, lit coverage to at least $0.95 L_k$, and $W_{20,k}/W_{80,k} \ge 3.0$ for crescents ($\ge 2.5$ for the short flick).
- **Leading Outer Edge & Hot Line:**
  - Orient the outward unit normal $\mathbf{N}_{\text{out}, k}(s_j) = \sigma_k \mathbf{N}_k(s_j)$ using $\sigma_k = \text{sign}\bigl(\text{median}_j[(C_k(s_j) - \mathbf{O}_k)\cdot\mathbf{N}_k(s_j)]\bigr)$ for crescents. For the short flick, orient $\sigma_k$ along the midpoint chord bulge if $\vert{}b_k\vert{} \ge 3.0\text{ px}$, else away from the mean centroid of the two crescents. Let $r_{\text{out}, k}(s_j)$ be the outer half-width along $+\mathbf{N}_{\text{out}, k}(s_j)$.
  - Classify 8-connected `hot` components with area $1\text{--}36\text{ px}^2$ and bbox aspect ratio $0.5\text{--}2.0$ as pinpoint glints (require $1\text{--}4$ glints).
  - Require total hot area $\sum \text{hot} / \sum \text{lit} \in [0.02, 0.06]$ ($2.0\text{--}6.0\%$). For non-glint hot pixels, outward projection $d_{\text{out}}(\mathbf{p}) = (\mathbf{p} - C_k(s^*))\cdot\mathbf{N}_{\text{out}, k}(s^*)$ must satisfy $d_{\text{out}}(\mathbf{p}) \gt 0$ and $d_{\text{out}}(\mathbf{p}) \ge \max(0.50\,r_{\text{out}, k}(s^*),\, r_{\text{out}, k}(s^*) - 4.0\text{ px})$ for at least $80\%$ of pixels ($\ge 90\%$ with $d_{\text{out}} \gt 0$), covering at least $40\%$ of stations on $s \in [0.15 L_k, 0.85 L_k]$ for crescents ($\ge 25\%$ for the short flick).
- **Margins, Loose Bits & Corners:**
  - Ignore `lit` components under $0.05\%$ of $\sum \text{lit}$; remaining `lit` bbox must lie within `87 <= x, y <= 992` (0-indexed, $\ge 8.05\%$ margin).
  - Outside `dilate_disk(M_strokes, 24)`, allow at most $3$ components of area $\ge 4\text{ px}^2$, each $\le 2.0\%$ of $\sum \text{lit}$.
  - All four $16\times 16$ image corners must have `max(R, G, B) <= 8`.

### Step 3 — Generate and Validate A3 (End Frame)

Attach only the validated $1080\times 1080$ A2 image in ChatGPT image editing.

**Final Prompt A3:**

Plaintext```
Edit the attached image in place on the exact same opaque pure-black 1:1 canvas. Keep the lower-left root and all three stroke paths locked at their exact pixel coordinates; do not shift, scale, rotate, extend or reconnect anything. Show the same three strokes late in their burn-down: needle tips completely vanished, middle sections broken into small separated orange-red islands, and thick roots cooled into dark crimson and muted ember cores, with two or three tiny dying ember specks along the original paths. Total lit flame area must be about one-quarter of the attached image, with almost no white-gold remaining. No new flames, arcs, C-shape, ring, lotus, bird, smoke, glow haze or text.
```

Normalize A3 to $1080\times 1080$ as in Step 2 and verify:

1. **Lit area:** $0.15 \le \sum \text{lit}_{\text{A3}} / \sum \text{lit}_{\text{A2}} \le 0.35$.
2. **Containment:** At least $70\%$ (target $\ge 85\%$) of $\text{lit}_{\text{A3}}$ lies inside `dilate_disk(lit_A2, 12)`.
3. **Shift via Masked ZNCC:** Compute soft-clipped masks $S_{\text{A2}} = \min(Y_{\text{A2}}/0.15, 1.0)$ and $S_{\text{A3}} = \min(Y_{\text{A3}}/0.15, 1.0)$. Evaluate Zero-Mean Normalized Cross-Correlation between $S_{\text{A2}}$ and shifted $S_{\text{A3}}$ restricted to the active mask $W = \text{dilate\_disk}(\text{lit}_{\text{A3}}, 12)$ for all integer shifts $(\Delta x, \Delta y) \in [-24, 24]^2$. Require peak shift $\sqrt{(\Delta x^*)^2 + (\Delta y^*)^2} \le 4.0\text{ px}$.
4. **Burn-down order:** Partition $\text{lit}_{\text{A2}}$ into Root ($[0, 0.33 L_k]$), Middle ($(0.33 L_k, 0.67 L_k]$), and Tip ($(0.67 L_k, L_k]$); require A3 survival fractions $f_{\text{root}} \gt f_{\text{mid}} \gt f_{\text{tip}}$ with $f_{\text{tip}} \le 0.10$, and $\sum \text{hot}_{\text{A3}} / \sum \text{lit}_{\text{A3}} \le 0.005$.

### Step 4 — Generate A4 Clips (Adobe Firefly Video)

Use **Adobe Firefly Video** (`Firefly Video` model), **First frame** = normalized A2, **Last frame** = normalized A3, **1:1**, **1080p**, **24 fps**, **5 s**, **Transparency Off**, camera motion **Static / None**. Run 3 generations (2 from the stronger A2/A3 pair, 1 from the second).

**Final Prompt A4 (537 characters including spaces):**

Plaintext```
Already-ignited three-stroke anime brushfire fan burning in place on a fixed pure-black canvas. Keep the lower-left strike root, three separate open curved paths, and sharp needle tips locked in position. Stepped orange-red flame tongues surge along each stroke with a hair-thin white-gold shimmer hugging the convex outer edges. Hold peak intensity briefly, then slowly erode from needle tips to middle islands down to the final frame's dark crimson root embers. Static camera. No closing C-arc, ring, lotus, bird, smoke, bloom or text.
```

### Step 5 — Extract Video, Filter C-Shapes, Select Segment & Build 24-Frame Atlas

Verify ImageMagick's `ffmpeg` delegate (`magick -list delegate | grep -i ffmpeg`) and extract 120 PNG frames:

Bash```
magick ff_run1.mp4 -alpha off -colorspace sRGB -coalesce -depth 8 PNG24:frames/frame_%03d.png
```

- **Measurable "Closes into a C" Rule (evaluated on all 120 frames):**
Frame $t$ fails if ANY of C1–C3 holds:
  - **C1 (Polar wrap):** Around Frame-0 longest crescent's Kåsa center $\mathbf{O}_1$, bin all $\mathbf{p} \in \text{lit}_t$ into 360 $1^\circ$ polar sectors (sector occupied if $\ge 10$ lit pixels). With $\Delta\phi_{\text{gap}}(t)$ the longest contiguous cyclic run of empty sectors, fan wrap is $\Theta_{\text{fan}}(t) = 360^\circ - \Delta\phi_{\text{gap}}(t)$. Reject the entire run if $\Theta_{\text{fan}}(t) \gt 190^\circ$ while $\sum \text{lit}_t \ge 0.35 \sum \text{lit}_0$; require $\Theta_{\text{fan}}(t) \le 185^\circ$ across the selected window.
  - **C2 (Enclosed cavity):** Any non-border 8-connected background component of `~dilate_disk(lit_t, 12)` has area $\ge 1{,}000\text{ px}^2$.
  - **C3 (Single-stroke curl):** Any crescent has $\theta_{\text{Kasa}, k}(t) \gt 180^\circ$ or chord-to-arc ratio $\lt 0.60$.
- **Per-Frame Centerline Tracking & Segment Selection ($N \in [12, 24]$):**
  - Propagate 15 stations per stroke from frame $t-1$ to $t$ by sampling $Y_t$ along normal rays $u \in [-12, +12]\text{ px}$ within stroke $k$'s territory, shifting each station to the luma-weighted centroid clamped to $[-4.0, +4.0]\text{ px}$, and Gaussian-smoothing along arc length (visually verified on the winning window).
  - Candidate windows $[s, s+N-1]$ must pass C1–C3, margins `87..992`, corner black `<= 8`, 3 separated strokes, arc bounds, dynamic taper $W_{20}/W_{80} \ge 2.5$ on every frame (window median $\ge 3.0$), ZNCC shift $\le 4.0\text{ px}$ vs Frame 0, $\sum \text{lit}_t \in [0.65 \sum \text{lit}_s, 1.15 \sum \text{lit}_s]$, and lose at most $15\%$ of `lit` area over any 6-frame sub-interval.
  - Among passing windows, maximize $J(s, N) = 2.0(N/24) + 1.5\,\text{mean}_t(\min(\text{core\_diff}(t,t+1), 0.18)) - 2.0\,\text{max}_t(\text{leak}(t)) - 1.0\,\text{std}_t(\sum \text{lit}_t / \sum \text{lit}_s)$.
- **Resampling to 24 Frames & Packing `384x384` Cells:**Bash`magick montage cell_00.png ... cell_23.png -tile 6x4 -geometry 384x384+0+0 -background "#000000" -define png:color-type=2 -depth 8 PNG24:brushfire_atlas_24f.png
`
  - Sample 24 frame indices via nearest-neighbor $i_k = s + \lfloor k(N-1)/23.0 + 0.5 \rfloor$ ($k = 0 \dots 23$) to preserve crisp stepped cel edges and hot-line luma.
  - Resize each selected $1080\times 1080$ frame directly to $384\times 384$ (`-filter Lanczos -define filter:clamp=true -resize 384x384!`), zero out the outer $2\text{ px}$ border in NumPy (`cell[:2,:]=0; cell[-2:,:]=0; cell[:,:2]=0; cell[:,-2:]=0`) so shader mask UVs stay $1:1$, and tile (`6x4` or `5x5` to match the shader uniform):
- **Runtime Timing:** The shader drives Reveal on frames 0–2 ($0.125\text{ s}$), Peak on frames 3–4 ($0.083\text{ s}$), and Decay via `survival_order` erosion on frames 5–23 ($0.792\text{ s}$, decay/attack ratio $= 6.33\times$). Final sign-off requires two blind judges scoring $\ge 8.5/10$ in-game.

## 3. Sources

1. **Adobe Firefly Video Workflow & Constraints:** Adobe HelpX, *Generate videos using images* ([helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html)). Confirms First/Last frame conditioning, $1:1$ $1080\text{p}$ at $24\text{ fps}$ for $5\text{ s}$, and that transparent output is limited to $540\text{p}$ $16:9$.
2. **Kåsa Circle Fit & Small-Arc Bias:** Kåsa, I. (1976), *IEEE Trans. Instrum. Meas.*, 25(1), 8–14; Chernov, N. (2010), *Circular and Linear Regression*, Chap. 5 ([people.cas.uab.edu/~mosya/cl/AC1c.pdf](https://people.cas.uab.edu/~mosya/cl/AC1c.pdf)). Proves Kåsa's algebraic formulation and its small-radius bias on short arcs ($\ll 120^\circ$).
3. **OpenAI Square Image Resolution:** OpenAI Platform Docs, *Image generation* ([platform.openai.com/docs/guides/image-generation](https://platform.openai.com/docs/guides/image-generation)). Confirms square outputs generate at $1024\times 1024$.
4. **Rec.709 Luma:** ITU-R Recommendation BT.709-6 ([itu.int/rec/R-REC-BT.709](https://www.google.com/search?q=https://www.itu.int/rec/R-REC-BT.709)).
5. **ImageMagick 7 Processing:** ImageMagick Command-Line Options ([imagemagick.org/script/command-line-options.php](https://imagemagick.org/script/command-line-options.php)).

## 4. Open Questions and Risks

- **ChatGPT stroke drift in A3:** Whole-canvas re-synthesis can shift strokes by $5\text{--}12\text{ px}$. *Mitigation:* If the Step 3 ZNCC check detects a pure rigid shift between $4.0$ and $12.0\text{ px}$, translate A3 back by $(-\Delta x^*, -\Delta y^*)$ via `np.roll` and re-verify $\ge 70\%$ containment; otherwise use ChatGPT's inpainting selection over the outer $75\%$ of the strokes so the root pixels remain untouched.
- **Firefly linear cross-dissolve:** Firefly may cross-fade luma rather than eroding tips first. *Mitigation:* Extracting an intact 12–24 frame window from the first half of the clip lets the Three.js shader's `survival_order` mask execute clean tip-to-root erosion.
- **H.264 black-level lift:** Compression noise can raise black to $1\text{--}4/255$. *Mitigation:* Enforce corner black $\le 8/255$ and keep the shader's `smoothstep(lo, hi, max_RGB)` threshold `lo >= 0.04` ($\approx 10/255$).
- **Repo items to confirm before running:** Check the Three.js shader uniform for `ff-a1-c5` to confirm whether the 24-frame montage grid is `6x4` or `5x5`, and measure unedited `v1`'s shortest inner crescent first in case its painted sweep is $110\text{--}118^\circ$.

