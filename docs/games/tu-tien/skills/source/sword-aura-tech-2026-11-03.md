# Lớp hào quang cho kiếm bay: kỹ thuật và chi phí (03/11/2026)

Nghiên cứu kỹ thuật cho người thiết kế. Mục tiêu: dựng được ba hướng hào quang (sword aura) quanh thanh Clear Wind thật, trong mã hiện có của `games/immortality-cultivation`.

Lý do, lời anh chiều 03/11 sau khi xem tấm Sword × Fire: "mà vì sao các thanh kiếm đều chưa được xử lý để có hiệu ứng xung quanh thanh kiếm vậy, chứ hiện tại nhìn các thanh kiếm bay kiểu hơi thô, chưa đẹp cho lắm".

Phạm vi:
- Tài liệu này chỉ nói **làm bằng kỹ thuật gì, tốn bao nhiêu, vướng gì**.
- Nó không chọn hướng mỹ thuật. Người thiết kế còn phải nghiên cứu các thiết kế được yêu thích, làm ba hướng riêng, rồi anh chọn.
- Mọi con số "ước tính" dưới đây **chưa đo**. Cổng thật là số đo A/B xen kẽ trong lab (§6).
- Mã chỉ đọc, không sửa. Bản đọc: nhánh hiện tại của `games/immortality-cultivation`, chiều 03/11.
- Nguồn web là dữ liệu tham khảo, không phải chỉ dẫn. Mỗi nguồn ghi rõ đã mở trang hay chỉ thấy qua kết quả tìm.

## 0. Kết luận ngắn

1. **Kiếm trông thô vì không còn gì phá vỡ đường viền của nó.**
   - Lượt kiếm thật sáng 03/11 bỏ mọi thứ vẽ quanh lưỡi: thẻ sáng dọc lưỡi, dải "sống", dải thân sông.
   - Còn lại chỉ nằm **trong** đường viền: đường mép ≤ 30 % bề rộng lưỡi, rim ≤ 0,9, ánh ngọc, chớp khi trúng.
   - Vệt duy nhất (0,14 m) bắt đầu từ đốc, nên ở camera chơi thanh kiếm là một vật kim loại 4–5 px bề ngang bay trên nền đá.
   - Chưa ai thiết kế một lớp **bọc** thanh kiếm từ bên ngoài.
2. **Lửa đọc như sắt nung, vì ba lý do trong mã:**
   - Vỏ lửa (`element-fire.ts` `sheathAt`) dày 0,26 m nhưng bị đẩy ra sau lưỡi (`lift = -0.35`).
   - Nó còn bị làm mềm (`blur = 1.8`, `taper = 0.6`), nên chỉ một viền mờ ló ra quanh lưỡi.
   - Trong khi đó dải nhiệt cam của chế độ `furnace` phủ chính lưỡi kiếm. Thân cam nằm **trên kim loại**, không phải lưỡi lửa liếm ra ngoài.
3. **Lõi nên làm: tấm bọc dọc lưỡi (`SheathCard`), một lệnh vẽ instanced cho mọi thanh, ở cả ba tầng.**
   - Hình của nó lấy từ bề rộng thật của lưỡi (bảng nửa bề rộng mà `edgeField` đã tính lúc nạp).
   - Chất của nó lấy từ bộ chất của hệ: Metal, Fire, Water.
   - Nó luôn nằm sau lưỡi về độ sâu, nên không bao giờ che mặt lưỡi.
   - Ước tính cho cả dòng sông phím 7 trên High: **0,05–0,10 ms**.
4. **Thêm theo tầng, mỗi lớp một công tắc:**
   - vỏ ngược (`AuraHull`) cho 6 kiếm chủ và thiên kiếm 20 m;
   - quầng trong shader impostor (`ImpostorHalo`) cho kiếm xa, không thêm lệnh vẽ;
   - bóng tàn ảnh (`GhostTrail`) vẽ bằng chính atlas impostor;
   - vệt GPU theo lịch sử vị trí (`src/view/trails.ts` đã có);
   - hạt quay (`OrbitMotes`), sao mũi (`TipStar`), tia rơi (`ShedSparks`);
   - pass méo dùng chung, sau cùng.
   Một bộ đầy đủ ước tính **0,35–0,55 ms** p95, vừa trần +0,6 ms nếu chọn kỹ (§5).
5. **Ba điều dễ làm sai:**
   - Kiếm bay mũi trước, nên vệt từ **mũi** nằm đè lên chính lưỡi. Mảng quét giữa hai khung (smear) gần như bằng 0 khi bay thẳng. Smear chỉ có ích khi lưỡi quét ngang (quay, bổ, rơi xoay).
   - Lớp glow ≤ 0,9 cộng lên nền đá sáng vẫn vượt ngưỡng bloom 1. Phải có lớp tối bên dưới (premultiplied), làm trong **cùng một** lệnh vẽ.
   - Trần của `VFX_STANDARD` §3.7 tính theo số **vật**: ≤ 32 ribbon sống và ≤ 8 vỏ lưới trên High. 94 vệt GPU hay 30 vỏ sẽ vượt trần chữ, dù chỉ tốn một lệnh vẽ. Cần anh hoặc chuẩn chốt lại cách đếm (§9).

## 1. Hiện trạng trong mã

### 1.1 Ba tầng hiển thị của kiếm chiêu

| Tầng | Vẽ bằng | Ở đâu | Số lượng |
|---|---|---|---|
| Kiếm chủ (hero) | GLB đủ, 14.728 tam giác, PBR của chính nó, đổ bóng | `blades.ts` `BladeSet` lưới 1 | Phím 7: 6 kiếm chủ. K0–K4: kiếm bay, kiếm chờ sau vai. Các thanh chủ của mưa K5. Thiên kiếm (bộ riêng, lượt trong suốt) |
| Kiếm giữa (mid) | LOD có texture, 3.200 tam giác | `BladeSet` lưới 2 | Phím 7: Low 10, Medium 16, High 24, Ultra 32 (`MYRIAD_SWORDS_PER_TIER`). Mưa K5, vầng 24 thanh khi gõ K5 |
| Kiếm xa (far) | Tấm impostor từ atlas 4 góc lăn, ô 512 × 128, kèm atlas mặt nạ (R mép, G lưỡi, A phủ) | `real-swords.ts` `SwordImpostors` | Phím 7: Low 24, Medium 40, High 64, Ultra 80. Vòng 16 kiếm cổng trời K5 |

- Phím 7 trên High có 94 thanh cùng lúc; Ultra 118, Low 40.
- Kích thước ở camera chơi, từ chuôi tới mũi, 1080p (`docs/changelog/2026-11-03-lab-real-swords.md`):
  - kiếm chủ: trung vị 97–130 px;
  - kiếm giữa: ~100 px;
  - kiếm xa: 88–98 px;
  - p10 khoảng 35 px.
- Lưỡi rộng chừng 4–5 px ở kích thước đó.
- Mọi thanh lưới đều quay mặt phẳng về camera (`FaceRoll`). Nhờ vậy bề ngang chiếu của lưỡi luôn gần bề ngang thật: điều kiện thuận cho tấm bọc ở §3.A1.

### 1.2 Những gì đang vẽ quanh kiếm

- **Trong vật liệu kiếm** (`sword-material.ts`, vá `onBeforeCompile`):
  - đường mép HDR `smoothstep(0.8, 0.95, aEdge)`, là phần duy nhất bloom;
  - rim fresnel (đã kẹp trước `pow`) ≤ 0,9;
  - ánh ngọc chỉ lấp phần còn trống dưới độ sáng 0,95;
  - chớp khi trúng; tan bằng nhiễu có `discard`;
  - chế độ `furnace` của Fire: thân ×0,12, dải nhiệt từ sống ra mép, ngọc thành than hồng.
  - Mỗi thanh có `iFx` (glow, flash, dissolve, seed) và `iRim`. Đồng phục chung `SWORD_LOOK` cho mọi kiếm và impostor.
- **Impostor:** cùng đường mép và `furnace` lấy từ atlas mặt nạ.
  - Shader **không `discard`**: phần trống của tấm (quanh lưỡi, trên dưới chuôi) vẫn được tô với alpha 0.
  - Nghĩa là thêm quầng vào chính shader này gần như không thêm diện tích tô.
- **Vệt:**
  - `RibbonPool` (`fxkit.ts`): đỉnh dựng trên CPU mỗi khung, một lệnh vẽ mỗi pool.
    - Kiểu sáng: cộng sáng, lõi `pow(s, 7)` trong quầng ≤ 0,9.
    - Kiểu lửa (`setFlame`): premultiplied, dải bồ hóng 0,85.
    - Phím 7: 6 vệt kiếm chủ, 46 điểm. `sword-skills.ts`: 64 vệt, 18 điểm, gồm cả dải lụa (`startSilk`, 0,11 m, màu tua).
  - Kiếm sông phím 7: một tia `BeamPool` một khung sau đốc.
    - Rộng 0,18 → 0,07 m; dài 0,45 × chiều dài kiếm (0,9 khi bổ xuống).
    - Thẳng, không cong theo đường bay.
- **Fire** (`element-fire.ts`):
  - vỏ lửa: `FlipbookPool` chế độ `heat`, clip `dragonhold-flame-trail`, trải dọc lưỡi (`span` = 1,45 × chiều dài lưỡi), dày 0,24–0,3 m, `lift = -0.35` (sau lưỡi), `taper 0.6`, `blur 1.8`;
  - tàn lửa rơi 40 cái/s mỗi thanh bay;
  - phím 7: chỉ 6 kiếm chủ có vỏ, vì "~90 tấm lửa trên sân đọc thành tấm ván cháy" (changelog Fire).
- **Đã có sẵn để dùng lại:**
  - `src/view/trails.ts`: vệt GPU. Lịch sử mũi kiếm nằm trong một `DataTexture` vòng, mỗi kiếm một hàng, mỗi mẫu 1/60 s; một lệnh vẽ instanced dựng dải trong vertex shader (`texelFetch`), 16 B mỗi mẫu. Game dùng nó cho bầy kiếm, lab chưa dùng.
  - `src/lab/blade-smear.ts`: tấm quét một khung giữa đường lưỡi cũ và mới (dải 3 hàng × 2 mép).
  - `FlipbookPool`: `span` co theo góc nhìn, `lift` chỉ đổi độ sâu, hạt mềm giải tích với mặt đất (`vxSoftGround`), chế độ `heat`.
  - `SpritePool` (`stretch`, `crop`, `groundFade`), `BeamPool`.
  - Các công thức P1, P4, P5, P6, P10 của skill `game-hero-presence-vfx`.

### 1.3 Chuỗi hậu kỳ (High, Ultra)

Theo `src/lab/skills-main.ts` và `src/view/renderer.ts`:
- **Bước 1, RenderPass:** cảnh HDR tuyến tính vào đích half-float. MSAA chỉ có ở Ultra (4 mẫu; `TT_MSAA` High 0).
- **Bước 2, UnrealBloomPass:** ngưỡng 1. Game: strength 0,55, radius 0,4. Lab: bloom 0,45.
- **Bước 3, ScreenPass:** làm tối, vignette, giảm bão hòa, vẫn ở HDR tuyến tính.
- **Bước 4, OutputPass:** exposure (game 1, lab 0,72), tone map Neutral, sRGB.
- **Bước 5, sau Output:** khung đồ họa.
- Chưa có pass méo nào.
- DPR của High và Ultra trôi trong khoảng 1–2 theo nhịp khung (`TT_DYNAMIC_RES`). Mọi số đo dưới đây là DPR ghim 1.

### 1.4 Ngân sách và số đo gốc

Trên M4, High 1920×1080, DPR 1:
- **Phím 7, lúc săn:** p95 10,2–10,5 ms; trần 11,5. Còn **~0,6 ms** cho cả dòng sông.
  - 54 lệnh vẽ.
  - 1,39 triệu tam giác mỗi khung.
- **Giá đỉnh, suy từ số đo của mình:**
  - Gom thanh hiện làm K5 giảm từ 3,17 xuống 1,37 triệu tam giác, p95 từ 13,1 xuống 10,0 ms.
  - Các thanh ẩn bị thu về 0, nên phần tam giác này gần như chỉ tốn vertex shader.
  - Vậy giá đỉnh của shader PBR instanced cỡ **~1,7 ms mỗi triệu tam giác**.
  - Số này nhiễu ±1–2 ms, nên khoảng tin cậy rộng: 1,2–2,2.
- **Fire so với Metal:** thêm +0,2 ms p95 ở phím 7 lúc săn. Phần thêm gồm 6 vỏ lửa, tàn lửa và vệt lửa. Đây là mốc cho một bộ lớp cỡ tương tự.
- **Nhiễu đo:** cùng một bản lệch ~1,5 ms giữa hai vòng. Lớp nào dưới 0,2 ms chỉ thấy được bằng nhiều vòng xen kẽ (§6).

## 2. Luật chung cho mọi lớp hào quang

1. **Hình của vũ khí, chất của hệ (D59).**
   - Lớp hào quang là một lớp **hình**: các module kiếm (`sword-skills.ts`, `myriad-swords.ts`) giữ hình học, tư thế, nhịp, số lượng.
   - **Chất** đến từ bộ chất: dải màu, kiểu dòng chảy, độ cứng mép, lớp tối, phần méo.
   - Đổi hệ là đổi đồng phục hoặc define, không thêm tấm.
   - Fire hiện vẽ vỏ lửa bằng móc `travel` riêng. Khi có lớp hào quang, vỏ đó phải **trở thành** chất Fire của lớp hào quang, không vẽ thêm bên cạnh (thay, không chồng).
2. **Kiếm thật luôn đọc được.**
   - Không lớp nào cộng sáng lên mặt lưỡi. Hào quang nằm ngoài đường viền hoặc sau lưỡi về độ sâu.
   - Hai cách:
     - đẩy độ sâu ra sau (như `lift` âm của flipbook);
     - vỏ ngược: chỉ vẽ mặt sau của vỏ phồng, nên lưỡi đục che phần trong.
   - Anh đã từ chối "ống sáng" (lưỡi bị bloom trùm thành ống trắng). Lớp hào quang không được dựng lại lỗi đó.
3. **Ánh sáng (LESSONS §5, VFX_STANDARD §3.5):**
   - Chỉ lõi mảnh HDR 3–6 được bloom; mọi quầng ≤ 0,9 mỗi kênh.
   - Lõi trắng ≤ 30 % bề ngang hiệu ứng. Không dùng đỏ cảnh báo `#FF4A4A`.
   - Chú ý: ngưỡng bloom so với **tổng** điểm ảnh. Quầng 0,5 trên đá sáng ~0,65 tuyến tính thành 1,15 và bloom. Vì vậy mỗi lớp glow có lớp tối bên dưới (luật 4) và đo phần điểm ảnh > 1 bằng `__lab.bright` / HdrProbe.
4. **Một lệnh vẽ cho cả tối lẫn sáng: premultiplied với `ONE, ONE_MINUS_SRC_ALPHA`.**
   - Phần tối xuất `rgb = tối × a` với `a > 0`: phủ nền như trộn thường.
   - Phần sáng xuất `rgb = sáng` với `a = 0`: cộng như additive.
   - Cả hai nằm trong cùng một điểm ảnh, cùng một shader.
   - Nguồn: [dtrebilco/PreMulAlpha](https://github.com/dtrebilco/PreMulAlpha) (chỉ thấy qua kết quả tìm) và [jvm-gaming, "Pre-multiplied alpha for drawing particles in one pass"](https://jvm-gaming.org/t/pre-multiplied-alpha-for-drawing-particles-in-one-pass/39549) (chỉ thấy qua kết quả tìm). Cả hai dẫn về bài "Premultiplied alpha" của Tom Forsyth ([blog wiki](https://tomforsyth1000.github.io/blog.wiki.html), chưa mở).
   - Trong repo, `RibbonPool.setFlame` và `FlipbookPool` chế độ `heat`, `rgba` đã dùng đúng phép trộn này.
5. **Thứ tự vẽ.** Kiếm đục (lượt đục) trước, rồi theo `renderOrder`:
   - lớp tối và vỏ lửa (11);
   - hào quang (11–12);
   - vệt, tia (11–13);
   - lõi và sao (13–15).
   Pool một mesh nằm ở gốc tọa độ, nên three chỉ xếp theo `renderOrder`, không theo khoảng cách. Hai lớp premultiplied có lớp tối chồng nhau thì thứ tự instance bên trong một lệnh vẽ là tùy ý. Giữ lớp tối mỏng để sai thứ tự không thấy được.
6. **Bề ngang tối thiểu theo điểm ảnh.**
   - Ở 35–130 px, một hào quang 0,1 m chỉ còn 2–4 px.
   - Mỗi lớp tính nửa bề ngang = max(bề ngang thế giới, N px quy về thế giới ở độ sâu của nó). Cách tính `halfPx` của `SwordImpostors` dùng lại được.
   - Mốc từ chẩn đoán ChatGPT 03/11 (`source/vfx-diagnosis-chatgpt-2026-11-03.md` §B): quầng thêm 3–6 px mỗi bên lúc mạnh nhất.
7. **Theo thời gian thế giới, không theo khung.**
   - Lịch sử tư thế (bóng tàn ảnh, vệt) lấy mẫu mỗi 1/60 s thời gian thế giới, như `RIBBON_SAMPLE_S`.
   - Nhờ vậy 60 Hz và 120 Hz giống nhau, và mọi thứ đứng yên khi dừng hình.
8. **Không cấp phát mỗi khung. Biên dịch trước.**
   - Shader mới vào `prewarm` của lab, để lần tung đầu không biên dịch giữa trận. Lần tung đầu hiện tại khung chậm nhất 46 ms.
   - Mỗi hệ một define: một chương trình mỗi hệ, biên dịch lúc nạp.
9. **Hai đường xuất màu.**
   - Low và (theo chú thích của lab) Medium vẽ thẳng ra màn, không qua composer.
   - Shader mới phải gọi `#include <tonemapping_fragment>` và `#include <colorspace_fragment>` như `real-swords.ts`, để hai đường cùng một màu.
10. **Chồng lớp.**
    - `ELEMENT_LAYER` §5: tối đa 2 lớp trong mờ chồng nhau ở một điểm ảnh. `VFX_STANDARD` §3.7: trung bình ≤ 3, đỉnh ≤ 8 trên High.
    - Vì vậy các lớp phải **thay chỗ nhau theo vùng**. Ví dụ bóng tàn ảnh thay tia một khung sau đốc của kiếm sông, không vẽ cả hai.

## 3. Từng lớp

### A. Vỏ khí bọc lưỡi (blade-hugging qi sheath)

Ba kỹ thuật, mỗi cái hợp một tầng; cùng một hàm chất (`auraMaterial`) cho cả ba.

#### A1. `SheathCard`: tấm bọc quay về camera dọc lưỡi (mọi tầng)

**Cách dựng:**
- Một `InstancedBufferGeometry` hình chữ nhật, mỗi thanh một instance: điểm đầu lưỡi (sau vòng chắn), mũi, độ sáng, độ tan, seed, lớp.
- Vertex shader dựng tấm theo trục lưỡi trên màn như `BeamPool` / `SwordImpostors`:
  - dài từ chắn tay tới quá mũi ~10–20 %;
  - rộng = bề ngang lưỡi + 2 × nửa bề ngang hào quang, có mức tối thiểu theo px (luật 6).
- **Hình bám lưỡi, không phải chữ nhật:**
  - Fragment đọc một kết cấu 1D 96 mẫu: nửa bề ngang lưỡi theo chiều cao. Đó chính là mảng `half[]` mà `edgeField` tính lúc nạp; hiện nó bị bỏ đi, chỉ cần giữ lại.
  - Từ đó tính khoảng cách tới mép lưỡi: `d = |x| − w(y)`.
  - Hào quang = hàm của `d` cộng nhiễu: mép mềm hoặc mép cứng tùy hệ.
  - Đây là thứ tránh được bài học "tấm ván cháy": tấm chữ nhật mềm mép đọc thành ván; hình thon theo lưỡi đọc thành lưỡi đang cháy hay đang tỏa khí.
- **Dòng chảy từ mũi về đốc:**
  - Nhiễu cuộn theo `y`: `noise(vec2(x·k1, y·k2 + t·v))`, hai quãng tám tốc độ khác nhau cho chiều sâu.
  - `v` tăng theo tốc độ bay thật của thanh (khí bị gió bạt về sau).
  - Khi kiếm đứng chờ, dòng chậm và theo luật của hệ: lửa bốc lên theo trục **thế giới**, không theo trục lưỡi.
  - Muốn có xoáy cuộn (Water) thì dùng flow map hai pha lệch nửa chu kỳ, theo [Vlachos, "Water Flow in Portal 2", SIGGRAPH 2010](https://www.advances.realtimerendering.com/s2010/Vlachos-Waterflow(SIGGRAPH%202010%20Advanced%20RealTime%20Rendering%20Course).pdf) (đã mở qua kết quả tìm và bản trình chiếu: hai lớp lệch pha giấu lặp lại, nhiễu giấu nhịp đập).
  - Dòng thẳng một chiều thì cuộn UV là đủ.
- **Độ sâu:**
  - Đẩy tấm ra sau lưỡi chỉ ở độ sâu (như `iLift` của `flipbook.ts`), để lưỡi đục luôn che phần nằm trên mặt lưỡi.
  - Không đẩy thì tấm cắt qua mặt phẳng lưỡi và nhấp nháy z.
  - Đẩy quá thì một con thú phía sau lọt lên trước hào quang. Giữ khoảng đẩy ≤ nửa bề ngang thú, ~0,3 m.
- **Mặt đất:** hạt mềm giải tích với mặt phẳng y = 0 (`vxSoftGround`), để kiếm cắm đất không bị cắt một đường thẳng.

**Tham khảo đã mở:** dự án [IRCSS/Stylized-Sword-Aura](https://github.com/IRCSS/Stylized-Sword-Aura) (Shahriar Shahrabi, 2020, MIT; [shader](https://raw.githubusercontent.com/IRCSS/Stylized-Sword-Aura/master/Assets/Shaders/Resources/SwordAura.shader)). Nó làm đúng loại này:
- một mặt phẳng đặt dọc lưỡi, UV từ chuôi tới mũi;
- nhiễu cuộn ngược chiều ở hai nửa trên dưới (lệch 0,5 để không soi gương);
- sóng tổng 9 hài lấy trọng số mạnh ở giữa lưỡi;
- mép sắc ở mũi, mềm ở chuôi;
- trộn alpha thường, `ZWrite Off`, `Cull Off`.
- Bài viết giải thích trên Medium không mở được (lỗi chứng chỉ).
- Học ý tưởng, tự viết mã. MIT cho phép chép, nhưng shader Unity đó không vừa với ràng buộc ≤ 0,9 và lớp tối của mình.

**Theo tầng:**

| Tầng | Cách | Ghi chú |
|---|---|---|
| Kiếm chủ | `SheathCard` + có thể thêm A2 | Ở cận cảnh, tấm phẳng lộ ra khi kiếm chĩa vào camera. Khi đó tấm co theo trục (như `span`) và A2 gánh phần nổi khối |
| Kiếm giữa | `SheathCard` | Lớp chính |
| Kiếm xa | A3 trong shader impostor, hoặc `SheathCard` chung lệnh vẽ | A3 không thêm lệnh vẽ |

**Chi phí, ước tính (High, DPR 1, phím 7 lúc săn):**
- **Lệnh vẽ:** +1 cho mọi thanh. Đỉnh: 94 × 4, không đáng kể.
- **Diện tích:** mỗi thanh ~100 × 16–24 px, khoảng 1,6–2,4 nghìn px. 94 thanh là ~150–230 nghìn px, ~7–11 % khung 1080p, với 1 lần đọc bảng bề ngang và 2–3 lần đọc nhiễu.
- **Ước tính tổng:** **0,05–0,10 ms**.
- **Cận cảnh** (zoom D57, kiếm chủ ~600 px): tấm ~600 × 120 = 72 nghìn px mỗi thanh. 6 kiếm chủ là ~0,4 triệu px, vẫn dưới một phần năm khung.
- **DPR 2:** diện tích ×4. Lớp này nhẹ, nhưng cộng với B và C thì góp phần làm độ phân giải động tụt bậc (§7).
- **CPU:** ghi 94 instance mỗi khung, nằm trong vòng `drawSwords` sẵn có: ~0,01–0,02 ms.

#### A2. `AuraHull`: vỏ ngược phồng theo pháp tuyến (kiếm chủ, thiên kiếm)

**Cách dựng:**
- Một `InstancedMesh` thứ hai dùng hình học khác hình kiếm:
  - hoặc LOD 3.200 tam giác;
  - hoặc tốt hơn, một vỏ thấp đa giác chỉ bọc lưỡi và vòng chắn, ~200–600 tam giác, nướng một lần bằng Blender: làm mượt, phồng sẵn.
- Vertex shader đẩy đỉnh theo **pháp tuyến đã làm mượt**: N px trong không gian clip cộng một phần mét thế giới.
- Vẽ **mặt sau** (`side: BackSide`), `depthWrite: false`, sau lượt đục.
- Phần vỏ nằm sau lưỡi bị lưỡi che bằng phép thử độ sâu. Chỉ dải ngoài đường viền hiện ra: một viền hào quang ôm đúng khối 3D, kể cả vòng ngọc và mây cuộn ở chắn tay.
- Fragment: fresnel của mặt sau (`1 − |n·v|`, kẹp trước `pow`) làm độ mềm ra ngoài; nhiễu dòng chảy theo `y` của kiếm đơn vị (`vSwP.y`, có sẵn trong quy ước jian) như A1.

**Nguồn:**
- Kỹ thuật vỏ ngược là cách viền kiểu toon kinh điển: vẽ một bản sao lưới, lật và phóng to một chút. Xem [bộ slide của Arc System Works về viền toon Guilty Gear](https://docswell.com/s/ASW_Academy/5LVY67-GG-Toonline-Eng) (chỉ thấy qua kết quả tìm) và buổi nói GDC 2015 "Guilty Gear Xrd's Art Style" ([GDC Vault](https://www.gdcvault.com/play/1022031/), có trả phí).
- Bề ngang theo từng đỉnh lưu trong màu đỉnh là kinh nghiệm cộng đồng ([polycount](https://polycount.com/discussion/comment/2169865), chưa mở).
- Skill `game-hero-presence-vfx` P6 khuyên tránh vỏ phồng của **lưới có xương** vì gấp đôi skinning. Kiếm không có xương, nên lý do đó không áp ở đây.

**Chi phí, ước tính:**
- **Đỉnh, theo dốc ~1,7 ms mỗi triệu tam giác:**
  - vỏ bằng LOD cho 30 thanh (chủ và giữa): 96 nghìn tam giác, **~0,10–0,2 ms**, không đáng;
  - vỏ thấp đa giác 400 tam giác cho 6 kiếm chủ: 2,4 nghìn tam giác, ~0,005 ms.
- **Diện tích:** chỉ dải viền và phần bị che sớm. ~1–1,5 nghìn px mỗi thanh ở camera chơi.
- **Ước tính tổng** cho 6 kiếm chủ: **0,01–0,03 ms**.
- **Trần:** `VFX_STANDARD` §3.7 cho ≤ 8 vỏ lưới cùng lúc trên High. Chỉ dùng cho kiếm chủ, thiên kiếm và kiếm chờ K1. Kiếm giữa và xa dùng A1, A3.

**Bẫy:**
- **Pháp tuyến tách ở đường may UV:**
  - `bladeFromObject` hàn đỉnh giữ UV, nên pháp tuyến tách ở đường may (Clear Wind LOD có 2.067 cạnh đường may).
  - Đẩy theo pháp tuyến tách thì vỏ rách thành khe.
  - Phải có thuộc tính pháp tuyến mượt riêng (`aSmoothNormal`), tính lúc nạp từ vị trí đã hàn bỏ UV, hoặc nướng sẵn trong vỏ thấp đa giác.
- **NaN dưới MSAA (Ultra):** điểm mẫu ở mép tam giác có thể nằm ngoài tam giác, nên pháp tuyến nội suy vượt ±1.
  - Luôn `pow(clamp(x, 0.0, 1.0), p)` và `normalize` có chặn dưới.
  - Có thể dùng `centroid` cho biến nội suy nhạy giá trị. Đổi lại, đạo hàm kém chính xác hơn.
  - Nguồn: [OpenGL Pipeline Newsletter vol. 3](https://www.opengl.org/pipeline/article/vol003_6/), [Khronos `interpolateAtCentroid`](https://registry.khronos.org/OpenGL-Refpages/es3/html/interpolateAtCentroid.xhtml) (cả hai chỉ thấy qua kết quả tìm).
  - Trong nhà: Dragonhold 29/10, một NaN thành ô đen qua bloom (skill hero-presence, P1).
  - `sword-material.ts` đã kẹp đúng cách. Vỏ mới phải giữ như vậy.
- **Ánh sáng:** vỏ không đổ bóng (`castShadow = false`) và không nhận `SWORD_LIGHT`: nó là phát sáng, không phải bề mặt được chiếu.

#### A3. `ImpostorHalo`: quầng trong shader impostor (kiếm xa, vòng kiếm cổng trời)

**Cách dựng:**
- Tấm impostor đã rộng 0,25 × chiều dài ô (`uCell.z`), nghĩa là có khoảng trống quanh lưỡi, và shader không `discard`.
- Thêm quầng vào chính shader:
  - **(a) Rẻ nhất:** đọc lại alpha của atlas ở mip mờ hơn (`texture2D(tLit, uv, 2.0–3.0).a`), lấy `blur·(1 − a)` làm quầng. Mip của alpha premultiplied cho sẵn một bóng mờ không cần nướng thêm. Hàng ô cao 128 px, nên ở mip 3 (16 px) bóng chưa lan sang hàng góc lăn kế bên.
  - **(b) Đẹp hơn:** nướng thêm một kết cấu khoảng cách có dấu (SDF ±16 px) trong `bake_sword_impostor.py`, rồi lấy ngưỡng SDF + nhiễu. Đây là cách cổ điển cho lưỡi lửa toon có mép cứng.
- **Không đặt SDF vào kênh B của atlas mặt nạ.** Mặt nạ được nạp `premultiplyAlpha = true`, nên B bị nhân với A và mất sạch ngoài đường viền. Phải là một tệp riêng (`-aura.png`), tuyến tính, không premultiply.
- Quầng là phát sáng: **không** nhân `SWORD_LIGHT` và `uGain`. Hiện impostor nhân `SWORD_LIGHT` dù ảnh nướng không bị làm tối (nợ mở trong changelog kiếm thật).

**Chi phí:**
- Thêm 1–2 lần đọc kết cấu trên diện tích **đã được tô**. Không lệnh vẽ, không diện tích mới.
- 64 thanh × ~2,5 nghìn px = 160 nghìn px → **~0,01–0,03 ms**.

**Chất theo hệ cho cả A1–A3** (đồng phục `AURA_LOOK` chung như `SWORD_LOOK`, đặt bởi `applyAuraLook(kit.aura)`):

| | Metal (align → shear) | Fire (compress → burst) | Water (flow → engulf) |
|---|---|---|---|
| Hình | Mảnh, thẳng, song song lưỡi: các vạch khí dài chạy từ mũi về đốc. Mép cứng. Tránh "đũa nhựa phát sáng" (ELEMENT_LAYER §2) | Lưỡi lửa **vượt ra ngoài** đường viền 1–2 lần bề ngang lưỡi, đầu lưỡi lửa bị bào sắc (không `blur`), nghiêng theo −vận tốc + lực nổi lên trên | Khối nước liền chảy chữ S quanh lưỡi, vượt quá mũi rồi cuộn lại; thân đặc, mép bọt cứng |
| Màu (tuyến tính) | Lõi trắng lam ≤ 30 % (đã có ở đường mép), thân lam ≤ 0,9 (`METAL_STREAM.halo`), viền mực chàm alpha 0,3–0,5 ở ngoài cùng trên nền sáng | Dải `heat` sẵn có: bồ hóng → son → hổ phách → lõi trắng vàng (chỉ lõi > 1). Bồ hóng alpha 0,85 ở mép ngoài | Thân chàm gần đen, alpha thật 0,9; bọt trắng mép cứng; vân sáng ≤ 0,9 |
| Trộn | Premultiplied: mực (a > 0) + khí (a = 0) | Premultiplied như `heat` | Premultiplied, alpha thật; không bao giờ lấy độ sáng làm alpha |
| Méo (§E) | Rất nhẹ, áp suất dọc mép (tùy chọn) | Hơi nóng phía trên vỏ | Khúc xạ trong thân nước |
| Lưỡi kiếm | `steel` (giữ nguyên) | Đề nghị bớt dải nhiệt `furnace` trên mặt lưỡi (để lại mép trắng vàng và than ngọc), dời phần cam ra lớp hào quang: thép tối tương phản với lửa liếm quanh | `steel` hoặc một chế độ "ướt" sau |

Các mã màu Fire là của `element-fire.ts` hiện tại. Màu Water là của ELEMENT_LAYER §2, chưa có bộ chất.

### B. Bóng tàn ảnh (afterimages) và mảng quét (smear)

**Nhận xét hình học trước:**
- Kiếm bay **mũi trước** trên đường gần thẳng: đường lưỡi trượt dọc chính nó, nên diện tích quét giữa hai khung ≈ 0.
  - Smear kiểu `BladeSmear` chỉ có nghĩa khi lưỡi quét **ngang**: K2 quét, kiếm rơi xoay K4, lúc kiếm chủ đổi hướng bổ xuống, kiếm chờ K1 lắc.
- Bóng tàn ảnh dọc đường bay nằm nối đuôi sau đốc. Nếu cách nhau 0,5–0,8 chiều dài kiếm, chúng đọc thành một chuỗi "kiếm quang" kiểu donghua, không thành một vệt mềm.

#### B1. `GhostTrail` bằng impostor (đề nghị)

**Cách dựng:**
- Mỗi thanh giữ một vòng K tư thế cũ (đốc, mũi, góc lăn), lấy mẫu theo thời gian thế giới mỗi Δ.
- Δ chọn theo tốc độ để khoảng cách bóng ≈ 0,6 chiều dài kiếm. Ở 15–25 m/s với kiếm 2,5 m, Δ ≈ 0,06–0,1 s.
- Vẽ K bóng mỗi thanh bằng **chính atlas impostor**, một `SwordImpostors` thứ hai ở chế độ "ghost":
  - không ánh sáng kim loại, chỉ một màu khí phẳng của hệ;
  - viền từ trường mép (R của mặt nạ);
  - alpha giảm theo tuổi; lõi không vượt 0,9 (bóng không bloom).
- Bóng phải **khác** thanh kiếm (bóng màu, phẳng, mờ dần). Một bản sao được chiếu sáng đọc thành ba thanh kiếm thay vì một, tức là rác.
- Áp cho mọi tầng, kể cả kiếm chủ: ở cận cảnh ô 512 px vẫn đủ nét cho một bóng phẳng.
- Góc lăn của bóng lấy theo góc lăn đã lưu (4 hàng atlas).

**Nguồn:**
- Kỹ thuật bản sao mờ dần theo vị trí cũ là kinh nghiệm phổ biến. Ví dụ [bài kỹ thuật "afterimage" của chocola-mint trên itch.io](https://chocola-mint.itch.io/touhou-ice-hockey-festival/devlog/483653/tech-blog-how-i-did-the-afterimage-effect) (chỉ thấy qua kết quả tìm: chép từng renderer, trộn nhân để bóng tối dần).
- Không tìm được bản phân tích của game 3D lớn về bóng tàn ảnh của vũ khí bay. Phần áp vào atlas impostor là đề xuất của mình.

**Chi phí, ước tính:**
- +1 lệnh vẽ cho mọi bóng.
- Diện tích: K = 2–3 cho kiếm chủ và giữa (30 × 3 × 2,5 nghìn px ≈ 225 nghìn px), K = 1 cho kiếm xa (≈ 160 nghìn px). Tổng ~0,4 triệu px với 4 lần đọc kết cấu.
- **~0,05–0,10 ms.**
- CPU: vòng K × 8 số mỗi thanh, ~0,01 ms.
- **Thay, không chồng:** bóng thay tia một khung sau đốc của kiếm sông (`drawSwords`), để mỗi điểm ảnh ≤ 2 lớp trong mờ.

#### B2. Bóng bằng lưới LOD (không đề nghị cho dòng sông)

- 90 bóng × 3.200 tam giác = 288 nghìn tam giác, **~0,5 ms** chỉ riêng phần đỉnh.
- Đúng khối 3D hơn, nhưng ăn gần hết ngân sách. Chỉ hợp cho 1–3 thanh cận cảnh: thiên kiếm, kiếm bay K0.

#### B3. `SweepSmear`: mảng quét một khung, instanced

**Cách dựng:**
- Tổng quát `BladeSmear` của lab thành instanced: 4 góc (đốc và mũi cũ, đốc và mũi mới).
- Một tấm 4 tam giác mỗi thanh: sáng ở mép trước và mũi, tắt dần ở mép sau.
- Chỉ phát khi tốc độ góc của lưỡi vượt ngưỡng.
- **Nguồn:**
  - smear frame trong hoạt hình: [bài "SMEAR: Stylized Motion Exaggeration with ARt-direction" (2024)](https://hal-iogs.archives-ouvertes.fr/hal-04576817v1) (chỉ thấy qua kết quả tìm);
  - cách làm trong game bằng lưới quét dọc vệt: [RealtimeVFX "Weapon Swipe"](https://realtimevfx.com/t/limeslushie-sketch-42-weapon-swipe/16890) (chỉ thấy qua kết quả tìm).

**Chi phí:** +1 lệnh vẽ. Diện tích chỉ khi quét. **< 0,02 ms.**

#### B4. Smear trên đỉnh của lưới thật (đánh dấu rủi ro)

**Cách dựng:**
- Truyền ma trận khung trước cho mỗi instance (`iPrev`, 64 B).
- Vertex shader kéo các đỉnh nằm phía sau chuyển động về phía tư thế cũ.
- **Nguồn:** [gist "object smearing" của dorodo95](https://gist.github.com/dorodo95/d8da68df38335153b4a7599026d2b0fd) (chỉ thấy qua kết quả tìm: đệm vị trí đỉnh khung trước, lấy hiệu làm độ dời).

**Chi phí:** không thêm lệnh vẽ.

**Rủi ro:** nó **biến dạng chính thanh kiếm đã duyệt**. Chỉ cho 1–2 khung lúc trúng hay lúc quét mạnh, và phải hỏi anh trước.

### C. Vệt ribbon: từ mũi và từ tua

**Nhận xét:**
- Vệt từ **mũi** của một thanh bay mũi trước nằm đúng trên lưỡi của nó. Mã hiện tại cố ý bắt đầu vệt ở đốc ("never over the sword").
- Vệt mũi chỉ dùng khi thanh quay hoặc bay cung gắt (K4 rơi xoay, K2, kiếm chờ). Hoặc đặt điểm phát lệch ngang khỏi trục lưỡi, ví dụ hai vệt mảnh ở hai mép như hai sợi khí.
- Vệt **tua** (dải lụa từ đốc) là phần nhận diện của Clear Wind (thanh tua lụa xanh nhạt), và mã đã có (`startSilk`). Nó chỉ cần đẹp hơn: rung theo sóng, rộng thay đổi, màu theo hệ.

**Cách dựng cho cả dòng sông: vệt GPU theo lịch sử (`src/view/trails.ts`)**
- Kiến trúc: vòng `DataTexture` mỗi thanh một hàng, 1 lệnh vẽ instanced dựng dải trong vertex shader, bề ngang thon theo tuổi.
- Thêm vào nó những gì `RibbonPool` có:
  - đường cong bề ngang (phồng nhanh rồi lắng, rồi thon);
  - cuộn UV chậm;
  - ăn mòn bằng nhiễu theo tuổi;
  - dải nguội (lõi → thân → bồ hóng);
  - chế độ lửa (đã có trong `FLAME_RIBBON_FRAGMENT`).
- Thay `AdditiveBlending` của `trails.ts` bằng premultiplied như luật 4. Hiện nó nhân alpha hai lần (`uColour·a` rồi `SrcAlpha`).
- Vệt cong theo làn bện của dòng sông. Tia `BeamPool` một khung hiện tại thì thẳng, nên mất cảm giác "chảy".
- **Kinh nghiệm cộng đồng:**
  - căn vệt kiếm theo hai điểm (gốc, mũi) để dải nằm theo lưỡi ([RealtimeVFX, Niagara ribbon mini tutorial, trang 2](https://realtimevfx.com/t/niagara-4-25-ribbon-trail-mini-tutorial/13043?page=2), đã mở);
  - co giãn bề ngang theo tuổi ([RealtimeVFX, vệt Battlerite](https://realtimevfx.com/t/how-to-do-this-trail-battlerite/2943?page=2), đã mở);
  - tăng bề ngang làm kết cấu bị kéo giãn, nên đưa bề ngang vào vật liệu để bù ([diễn đàn Unreal](https://forums.unrealengine.com/t/how-to-get-a-thick-paint-trail-effect/2311217), đã mở);
  - kiểu UV mép "SmoothTransition" theo tuổi chuẩn hóa ([Epic, `ENiagaraRibbonUVEdgeMode`](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/Niagara/ENiagaraRibbonUVEdgeMode), chỉ thấy qua kết quả tìm).
  - [TrailRendererJS](https://github.com/mkkellogg/TrailRendererJS) là thư viện three.js cũ (2015), ít cập nhật. Không dùng; `trails.ts` của mình đã tốt hơn cho nhiều vệt.

**Chi phí, ước tính:**
- 94 thanh × 24 mẫu: 4,5 nghìn tam giác. Tải lên 94 × 24 × 16 B ≈ 36 KB mỗi khung (72 KB nếu thêm vệt tua).
- Diện tích: ~0,5–1,5 nghìn px mỗi thanh, tổng ~50–140 nghìn px.
- **~0,03–0,06 ms**, 1–2 lệnh vẽ.
- CPU: ghi đầu vệt, ~0,01 ms. So với `RibbonPool` CPU: 94 vệt × 46 điểm × tích có hướng, khoảng 0,1–0,2 ms CPU và ~380 KB tải lên mỗi khung.
- **Trần:** `VFX_STANDARD` §3.7 "ribbon sống ≤ 32 trên High" được viết cho vệt CPU. 94 vệt GPU trong một lệnh vẽ vượt trần chữ. Cần chốt lại cách đếm (§9).

### D. Hạt quay, ký tự, sao mũi, tia rơi

1. **`OrbitMotes`** (skill hero-presence P4):
   - Một `InstancedMesh` hoặc một `SpritePool`. Quỹ đạo tính trong vertex shader từ `uTime` và tư thế thanh.
   - Tư thế thanh có thể đọc từ một `DataTexture` nhỏ (94 × 2 texel) để CPU không làm gì mỗi hạt.
   - Lệch quỹ đạo theo 2–3 dải nghiêng, bán kính và tốc độ khác nhau, vài hạt to, nhiều hạt nhỏ, nhấp nháy với chu kỳ làm việc thấp.
   - Chỉ cho kiếm chủ, kiếm chờ K1, vầng K5: 8–16 hạt mỗi thanh.
   - Ký tự (rune) dùng atlas ký tự có sẵn của kit (`runes`). Quay chậm, chu kỳ ≥ 6 s (P3).
   - Chi phí: 6 × 12 hạt × (6 px)², không đáng. **~0,01–0,02 ms.** Gộp vào pool glow sẵn có thì không thêm lệnh vẽ.
2. **`TipStar`:**
   - Một sao bốn cánh nhỏ ở mũi, lõi HDR ≤ 2–3 px.
   - Chỉ cho kiếm chủ, kiếm đang bổ xuống và kiếm ở đỉnh sóng sáng. 94 sao HDR cùng lúc thành bầu trời sao rối mắt và nhiều điểm bloom.
   - Dùng pool `stars` của phím 7. Chi phí ~0.
3. **`ShedSparks`:**
   - Đã có (móc `glint`, tàn lửa của Fire). Chỉ đổi chất theo hệ: Metal tia thép trắng lam ngắn, Fire tàn lửa, Water giọt và bụi nước.
   - Trần hạt sinh mỗi khung của High là 260 (`VFX_STANDARD` §3.7).

### E. Méo không khí (pass dùng chung)

**Cách dựng, theo ELEMENT_LAYER §3:**
- Một RT dùng chung 480 × 270.
- Các lớp ghi vector lệch kiểu normal map, cộng dồn.
- Một lần ghép đọc cảnh với UV lệch. Nên **gộp vào `ScreenPass`**, vốn đã đọc ảnh cảnh, để không thêm một pass toàn màn.
- Nó nằm trước bloom, nên bloom thấy ảnh đã méo.

**Nguồn đã mở:** [Froyok (Léna Piquet), "Refracting Pixels", 12/2024](https://www.froyok.fr/blog/2024-12-refraction). Bài so hai họ cách làm:
- **Chép màu cảnh** trước mỗi vật khúc xạ (Half-Life 2, F.E.A.R., Crysis 3): mỗi lần chép là một lần đổi framebuffer.
- **Cộng dồn méo vào một bộ đệm rồi một pass:**
  - Jericho: BGRA8, hạt ghi hướng vào RGB, độ đục vào A.
  - Batman Arkham Knight: BGRA8, trước vật trong suốt.
  - **Dishonored 2: cộng vào bộ đệm vận tốc RGBA16F ở nửa độ phân giải.**
  - Quantum Break: RG16F, lật gương UV ở mép màn.
  - DOOM: RGBA8, áp trong pass tone map.
- Cái giá của cách cộng dồn: méo không đan xen được với vật trong suốt, luôn nằm trước hoặc sau.
- Lỗi rò từ vật phía trước (Batman) bài viết không nêu cách sửa.

**Rò tiền cảnh:** ở 1/16 diện tích, mặt nạ méo lem sang thú đứng trước kiếm. Hai cách chặn:
- tắt dần méo khi sâu cảnh < sâu của lớp ghi (cần một kết cấu độ sâu nhỏ, hiện composer chưa có);
- hoặc giữ biên độ méo nhỏ quanh kiếm và chấp nhận lem.

**Chi phí:**
- Ghi vào RT nhỏ: không đáng.
- Ghép trong `ScreenPass`: thêm 1 lần đọc RT nhỏ và 1 lần đọc phụ thuộc trên 2,07 triệu px.
- Ước tính **0,08–0,15 ms**; ELEMENT_LAYER §5 cho trần 0,15 ms.
- +1 lệnh vẽ (lớp ghi) và 1 lần đổi đích.
- Medium yếu hơn, Low tắt, bản giảm chuyển động tắt (`VFX_STANDARD` §3.8).

**Thứ tự:** dựng một lần cùng Water, như changelog Fire đã định.

### F. Bloom đối xử từng lớp thế nào

| Lớp | Lớp sáng | Được vượt 1 không |
|---|---|---|
| Đường mép lưỡi (đã có) | lõi | Có, × glow. Nhưng ở cận cảnh nó đã trùm thành vầng trắng (nợ mở): cân nhắc giảm theo kích thước màn (`fwidth`) mạnh hơn |
| `SheathCard`, `AuraHull`, `ImpostorHalo` | glow | Không. Mép trong sát lưỡi có thể có một sợi lõi mảnh ≤ 1 px khi kiếm sáng nhất, như "sống" của khí |
| `GhostTrail` | glow | Không bao giờ |
| Vệt (`trails.ts`) | lõi mảnh + glow | Chỉ lõi `pow(s, 7)` |
| `OrbitMotes` | glow, vài hạt to có lõi bé | Chỉ ≤ 10 % số hạt |
| `TipStar` | lõi | Có, chỉ ở kiếm được chọn |
| Méo | — | — |

- **Không đổi bloom chung** (strength, radius, threshold), theo skill hero-presence.
- **Selective bloom** kiểu ví dụ three.js ([`webgl_postprocessing_unreal_bloom_selective`](https://threejs.org/examples/#webgl_postprocessing_unreal_bloom_selective)) cần vẽ cảnh hai lần, các vật không bloom tô đen ([diễn đàn three.js](https://discourse.threejs.org/t/selective-unrealbloompass-issues/9331), chỉ thấy qua kết quả tìm). Quá đắt ở đây; luật giá trị (lõi > 1, quầng ≤ 0,9) làm đúng việc đó không tốn thêm pass.
- **Hòa trộn MAX** (`THREE.MaxEquation`) giữ chồng hào quang không vượt mức của từng cái, nên không bao giờ bloom. Nhưng trên nền đá sáng hơn mức hào quang, nó biến mất. Chỉ hợp cho phần sông kiếm trên nền đã bị làm tối lúc phím 7.
- **Đo:** phần điểm ảnh > 1 do lớp mới gây ra (`__lab.bright`, HdrProbe), trên nền giữa, sáng `#d6d0c2`, tối `#2a2c30`, như cách đo Fire.

## 4. Ráp theo pha, trạng thái và bản giảm chuyển động

| Trạng thái | Hào quang làm gì | Bản giảm chuyển động |
|---|---|---|
| Chờ, gõ (K1 sau vai, vầng K5) | Lớn dần theo tiến độ gõ (thông tin), dòng chậm, hạt quay | **Giữ** mức theo tiến độ gõ (một độ sáng đứng yên); dòng × 0,3, không nhấp nháy |
| Phát chiêu (f0) | Vỏ và tấm bừng sáng ngay khung 0 (luật 5 §3.1), rồi lắng 150–300 ms | Đỉnh × 0,6 |
| Bay | Dòng theo tốc độ, bóng tàn ảnh, vệt tua; sông kiếm: sóng sáng chạy dọc dòng (`brightAt`) kéo theo hào quang | Bóng tàn ảnh: 1 bóng đứng hoặc tắt; vệt ngắn lại, không rung |
| Bổ xuống | Hào quang dài ra, bóng dày hơn, sao mũi | Như trên |
| Trúng | Vỏ chớp 2–3 khung, hạt tung, smear nếu đang quét | Chớp × 0,6; smear tắt |
| Tan vào ánh sáng | Hào quang tan **trước** lưỡi, cùng ngưỡng nhiễu với `iFx.z`, mép sáng theo hệ | Giữ |

- Hệ thống giảm chuyển động của game chưa có, chỉ có `screen.intensity`. Mỗi lớp mới khai báo `keep | soften | drop` theo `VFX_STANDARD` §3.8.
- **Theo tầng đồ họa:**
  - Low: chỉ A1 cho kiếm chủ và giữa, A3 (miễn phí), vệt tua cho kiếm chủ; không bóng, không méo, không hạt quay.
  - Medium: thêm bóng K = 1, vệt GPU.
  - High: đủ bộ trong ngân sách.
  - Ultra: K = 3, hạt nhiều hơn, méo nửa độ phân giải.

## 5. Ba gói kỹ thuật cho ba hướng (để người thiết kế ghép, không phải hướng mỹ thuật)

Ước tính p95 cộng thêm cho phím 7 lúc săn, High, DPR 1. Ngân sách ~0,6 ms.

| Gói | Thành phần | Lệnh vẽ thêm | Ước tính |
|---|---|---|---|
| G1 "Vỏ khí + tàn ảnh" | A1 mọi thanh, A2 cho 6 kiếm chủ, A3, B1 (K 3/3/1), vệt tua cho kiếm chủ | +3 | 0,15–0,25 ms |
| G2 "Dòng chảy + hạt" | A1, A3, vệt GPU cho mọi thanh (thay tia một khung), hạt quay và ký tự cho kiếm chủ, sao mũi chọn lọc | +2–3 | 0,10–0,20 ms |
| G3 "Áp suất + méo" | A1, A2, A3, `ShedSparks` theo hệ, pass méo dùng chung (gộp vào `ScreenPass`) | +2 và 1 lần đổi đích | 0,20–0,35 ms |
| Mọi thứ | A1 + A2 + A3 + B1 + vệt GPU + hạt + méo | +6–7 | 0,35–0,55 ms |

Chú thích:
- 54 lệnh vẽ + 7 vẫn dưới trần +32 của `VFX_STANDARD` §3.7.
- Dải ước tính đã gồm sai số của dốc đỉnh. Ở DPR 2, phần diện tích nhân 4: gói "mọi thứ" có thể lên ~1 ms và đẩy độ phân giải động tụt bậc.
- Fire hiện thêm +0,2 ms. Nếu lớp hào quang **thay** vỏ lửa và tia một khung (thay, không chồng), phần đó được trả lại một phần.

## 6. Cách đo trước khi tin số nào

- **Mỗi lớp một công tắc** trong lab: `enabled`, `intensity`, đếm lệnh vẽ, như skill hero-presence bước 4.
- **A/B xen kẽ,** như phần 2 của changelog Fire: 7 vòng, mỗi vòng 3–5 lượt, xen bật và tắt trên cùng máy, `lab-element-perf.mjs`.
  - Báo trung vị và trung bình p95.
  - Trên DPR ghim 1, và một lượt DPR 2 cho phần diện tích.
  - Chạy qua `.local/bin/heavy.sh --perf`, một lượt GPU mỗi lúc.
- **Các cửa sổ:** phím 7 lúc săn và nhát kết, phím 1, K5. Cận cảnh phím 7 (zoom gần) cho phần diện tích.
- **Kiểm ánh sáng:**
  - phần điểm ảnh > 1 do lớp mới gây ra;
  - điểm ảnh độ sáng ≥ 0,95 ≤ 6 % sân;
  - NaN/Inf trong bộ đệm bloom ở Ultra (MSAA 4) và High;
  - ba nền: giữa, sáng, tối.
- **Kiểm đọc được:**
  - ảnh xám ở 40–100 px: còn thấy lưỡi, vòng ngọc, chắn tay, tua;
  - so cùng khung bật và tắt hào quang.
- **Chụp:** vào `tmp/` của game. Tỉa khung thô bằng `tools/capture-prune/prune.mjs` sau khi chấm.

## 7. Bẫy, gom lại

1. **Che lưỡi.** Mọi lớp cộng sáng trên mặt lưỡi làm lưỡi mất (lỗi "ống sáng" đã bị từ chối). Hào quang phải nằm sau lưỡi về độ sâu, hoặc ngoài đường viền (vỏ ngược).
2. **Sắp xếp với clip lửa trong suốt.**
   - Lớp cộng sáng vẽ **sau** thân lửa `heat` hoặc `rgba` sẽ cộng sáng lên lớp bồ hóng, làm mất lớp tối.
   - Lớp premultiplied vẽ **trước** thì bị thân lửa phủ 0,85–0,95.
   - Với Fire, hào quang **là** vỏ lửa (một lớp). Với các hệ khác, ghi thứ tự `renderOrder` trong một bảng duy nhất.
   - Instance bên trong một lệnh vẽ không được sắp xếp.
3. **NaN trước `pow` dưới MSAA** (Ultra): kẹp trước `pow`, chặn `normalize(0)`, cân nhắc `centroid` (§A2).
4. **Độ sâu với mặt đất.** Tấm và vỏ cắm đất bị cắt thẳng: dùng hạt mềm giải tích với y = 0 (`vxSoftGround`). Theo [bài Soft Particles của NVIDIA, 2007](https://developer.download.nvidia.com/whitepapers/2007/SDK10/SoftParticles_hi.pdf) (tệp PDF mở được nhưng không đọc được chữ; ý chính qua kết quả tìm): đổi phép thử độ sâu có-hoặc-không thành một vùng chuyển tiếp. Mặt đất ở đây phẳng, nên không cần kết cấu độ sâu.
5. **Màn che trên nền sáng.**
   - Cộng sáng trên đá `#d6d0c2` bạc màu, như vòng áp suất của Fire đo được (18 % "thân nhạt").
   - Cách chữa:
     - lớp tối premultiplied trong cùng shader (luật 4);
     - kênh trong suốt luôn tách khỏi màu;
     - không lấy độ sáng làm alpha (DRAGON_FIRE_DIAGNOSIS).
6. **Pháp tuyến tách ở đường may UV** làm vỏ phồng rách (§A2).
7. **SDF trong atlas premultiplied bị xóa ngoài đường viền** (§A3).
8. **`discard`.**
   - Trên kiến trúc tile như GPU Apple, `discard` và alpha-test cản bước loại bỏ bề mặt khuất. PowerVR khuyên vẽ theo thứ tự đục → alpha-test → trộn, và tránh `discard` ([Imagination, "Do Not Use Discard"](https://docs.imgtec.com/starter-guides/powervr-architecture/html/topics/rules/do-not-use-discard.html), đã mở).
   - Apple chỉ nói chung về giảm vẽ chồng trên TBDR ([WWDC20 10632](https://developer.apple.com/videos/play/wwdc2020/10632), chỉ thấy qua kết quả tìm). Chưa có số cho M4: phải đo.
   - Áp vào đây: các lớp trộn **không cần** `discard` để đúng hình, chỉ để bớt tô. Đo cả hai.
   - Phần tan của vật liệu kiếm (đục, có `discard`) là thứ đã có, không đổi.
9. **Lưới dither thay trong mờ:** mẹo trong bài Unreal của Rayane Saada trên [80.lv](https://80.lv/articles/a-detailed-tutorial-on-how-to-create-enhanced-holy-vfx-effect-in-ue5) (đã mở). Nó cần TAA để mịn; mình không có TAA, nên sẽ lộ lỗ chấm. Không dùng.
10. **Trần đếm theo vật** (ribbon ≤ 32, vỏ lưới ≤ 8 trên High) không khớp với vệt và vỏ instanced (§9).
11. **Impostor nhân `SWORD_LIGHT`:** quầng impostor không được nhân, nếu không nó sáng gấp 1/k khi màn tối (nợ mở của changelog kiếm thật).
12. **Lần biên dịch đầu:** mỗi hệ một chương trình. Biên dịch sẵn trong `prewarm`, đo lại khung chậm nhất của lần tung đầu (hiện 46 ms, cổng 50).
13. **Độ phân giải động:** lớp nặng diện tích không làm vượt ngân sách một cách ồn ào. Chúng làm DPR tụt và ảnh mờ đi. Đọc cả DPR trung bình trong số đo.

## 8. Đề xuất hợp đồng cho bộ chất (để bàn, chưa sửa mã)

Thêm vào `ElementKit` một mục `aura`, cùng kiểu với `blade` và `trail`. Lớp hình trong các module kiếm đọc nó; móc theo pha không phát tấm riêng cho từng thanh.

```ts
interface AuraLook {
  readonly mode: "qi" | "flame" | "water";   // shader define, one program per kit
  readonly ramp: ElementRamp;                // core, edge, body, soot (linear)
  readonly widthM: number;                   // half width outside the blade edge
  readonly minPx: number;                    // screen floor for that half width
  readonly flow: { readonly speed: number; readonly scale: number; readonly buoyancy: number };
  readonly edge: number;                     // 0 soft … 1 hard (eroded tongues, foam lines)
  readonly darkUnder: number;                // premultiplied dark layer alpha (light ground)
  readonly ghosts: { readonly count: number; readonly spacing: number; readonly tint: Rgb };
  readonly motes: { readonly count: number; readonly tint: Rgb } | null;
  readonly distortion: number;               // share of the shared pass (0 none)
}
```

- Metal giữ bộ hiện tại và thêm `aura` mới. Mọi khung Metal sẽ đổi, nên phải chụp lại tấm trước/sau và để anh duyệt.
- Fire chuyển `sheathAt` vào `aura.mode = "flame"`.

## 9. Câu hỏi còn mở

1. **Cách đếm trần.** Vệt và vỏ instanced (94 vệt trong một lệnh vẽ, vỏ trên > 8 thanh) có tính theo **lệnh vẽ và diện tích** thay cho số vật ở `VFX_STANDARD` §3.7 không? Đề nghị: có, cổng là thời gian khung và độ chồng điểm ảnh.
2. **Lưỡi Fire.** Có bớt dải nhiệt cam trên mặt lưỡi (`furnace`), để lửa nằm **quanh** lưỡi và lưỡi là thép tối nóng mép không? Hướng này cần anh duyệt vì nó đổi hình lưỡi đã chụp.
3. **Smear trên lưới thật** (B4) có được phép 1–2 khung lúc quét mạnh không, hay thanh kiếm đã duyệt không bao giờ được biến dạng?
4. **Vỏ thấp đa giác** (A2): có được dựng một vỏ bọc lưỡi trong Blender không? Nó là hình học vô hình mang ánh sáng, không phải kiếm thay thế. Hay chỉ dùng LOD sẵn có?
5. **Đổi Metal.** Thêm hào quang cho Metal phá lời hứa "Metal không đổi" của lớp hệ. Cần một lượt chụp trước/sau mới và anh xem.
6. **Pass méo.** Dựng cùng Water như đã định, hay sớm hơn cho Fire (hơi nóng) nếu hướng anh chọn cần nó?
7. **Bản giảm chuyển động.** Game chưa có công tắc riêng (chỉ có `screen.intensity`). Lớp hào quang nên đọc công tắc nào?

## 10. Bảng tổng: lớp × tầng × chi phí

Ước tính, chưa đo; High, 1080p, DPR 1, phím 7 lúc săn (6 kiếm chủ, 24 kiếm giữa, 64 kiếm xa).

| Lớp | Kiếm chủ (lưới đủ) | Kiếm giữa (LOD) | Kiếm xa (impostor) | Lệnh vẽ thêm | Diện tích tô thêm | p95 ước tính | Giảm chuyển động |
|---|---|---|---|---|---|---|---|
| A1 `SheathCard` | có | có | tùy (hoặc A3) | 1 | 150–230 nghìn px (7–11 %) | 0,05–0,10 ms | dòng × 0,3 |
| A2 `AuraHull` | có (vỏ thấp đa giác) | không (trần 8 vỏ) | không | 1 | dải viền, ~10 nghìn px | 0,01–0,03 ms (LOD cho 30 thanh: 0,10–0,2) | giữ, không nhịp |
| A3 `ImpostorHalo` | — | — | có | 0 | 0 (trên diện tích sẵn có) | 0,01–0,03 ms | giữ |
| B1 `GhostTrail` | K 2–3 | K 2–3 | K 1 | 1 | ~0,4 triệu px | 0,05–0,10 ms | 1 bóng hoặc tắt |
| B2 bóng bằng lưới LOD | chỉ cận cảnh | không | không | 1 | — | ~0,5 ms cho 90 bóng | tắt |
| B3 `SweepSmear` | khi quét | khi quét | không | 1 | chỉ khi quét | < 0,02 ms | tắt |
| B4 smear trên đỉnh | hỏi anh | không | không | 0 | 0 | ~0 | tắt |
| C vệt GPU (mũi lệch, tua) | có | có | có (ngắn) | 1–2 | 50–140 nghìn px | 0,03–0,06 ms | ngắn lại |
| D `OrbitMotes` | có | không | không | 0–1 | rất nhỏ | 0,01–0,02 ms | × 0,3, không nhấp nháy |
| D `TipStar` | có | chọn lọc | chọn lọc | 0 | rất nhỏ | ~0 | giữ, × 0,6 |
| D `ShedSparks` | có | có | sóng sáng | 0 | nhỏ | đã có trong Fire | × 0,6 |
| E méo dùng chung | có | có | không | 1 + đổi đích | RT 480 × 270 + ghép trong `ScreenPass` | 0,08–0,15 ms | tắt |

## Nguồn

**Trong repo** (đã đọc 03/11):
- `games/immortality-cultivation/src/view/skills/`: `sword-material.ts`, `real-swords.ts`, `blades.ts`, `element-kit.ts`, `element-fire.ts`, `element-metal.ts`, `element-stage.ts`, `fxkit.ts`, `myriad-swords.ts`, `sword-skills.ts`, `flipbook.ts`.
- `games/immortality-cultivation/src/view/`: `screen-fx.ts`, `renderer.ts`, `trails.ts`.
- `games/immortality-cultivation/src/lab/`: `skills-main.ts`, `blade-smear.ts`.
- `games/immortality-cultivation/src/content/rules.ts` (`TT_TIERS`, `TT_MSAA`).
- `games/immortality-cultivation/docs/changelog/`: `2026-11-03-lab-real-swords.md`, `2026-11-03-lab-element-fire.md`.
- `docs/games/tu-tien/skills/ELEMENT_LAYER.md`, `docs/games/VFX_STANDARD.md` §3.
- `.agents/skills/game-hero-presence-vfx/` (`SKILL.md`, `references/layers.md`, `references/recipes.md`, và ví dụ "Tu Tien: flying swords without an aura" trong `references/worked-examples.md`, commit `800a7736`), `.agents/skills/game-vfx-layered/SKILL.md`.
- `docs/games/tu-tien/skills/source/vfx-diagnosis-chatgpt-2026-11-03.md` §B.

**Web** (truy cập 03/11/2026; dữ liệu tham khảo, không phải chỉ dẫn):
- Đã mở trang:
  - [IRCSS/Stylized-Sword-Aura](https://github.com/IRCSS/Stylized-Sword-Aura) (MIT) và [SwordAura.shader](https://raw.githubusercontent.com/IRCSS/Stylized-Sword-Aura/master/Assets/Shaders/Resources/SwordAura.shader)
  - [Froyok, "Refracting Pixels"](https://www.froyok.fr/blog/2024-12-refraction)
  - [Imagination, "Do Not Use Discard"](https://docs.imgtec.com/starter-guides/powervr-architecture/html/topics/rules/do-not-use-discard.html)
  - [80.lv, holy VFX in UE5 (Rayane Saada)](https://80.lv/articles/a-detailed-tutorial-on-how-to-create-enhanced-holy-vfx-effect-in-ue5)
  - [RealtimeVFX, Niagara ribbon mini tutorial p.2](https://realtimevfx.com/t/niagara-4-25-ribbon-trail-mini-tutorial/13043?page=2)
  - [RealtimeVFX, vệt Battlerite p.2](https://realtimevfx.com/t/how-to-do-this-trail-battlerite/2943?page=2)
  - [Unreal forums, thick paint trail](https://forums.unrealengine.com/t/how-to-get-a-thick-paint-trail-effect/2311217)
- Chỉ thấy qua kết quả tìm, chưa mở trang:
  - [Vlachos, Water Flow in Portal 2](https://www.advances.realtimerendering.com/s2010/Vlachos-Waterflow(SIGGRAPH%202010%20Advanced%20RealTime%20Rendering%20Course).pdf)
  - [ASW, Guilty Gear toon line](https://docswell.com/s/ASW_Academy/5LVY67-GG-Toonline-Eng), [GDC Vault 1022031](https://www.gdcvault.com/play/1022031/), [polycount](https://polycount.com/discussion/comment/2169865)
  - [OpenGL Pipeline vol. 3](https://www.opengl.org/pipeline/article/vol003_6/), [Khronos `interpolateAtCentroid`](https://registry.khronos.org/OpenGL-Refpages/es3/html/interpolateAtCentroid.xhtml)
  - [NVIDIA Soft Particles](https://developer.download.nvidia.com/whitepapers/2007/SDK10/SoftParticles_hi.pdf)
  - [dtrebilco/PreMulAlpha](https://github.com/dtrebilco/PreMulAlpha), [jvm-gaming premultiplied one pass](https://jvm-gaming.org/t/pre-multiplied-alpha-for-drawing-particles-in-one-pass/39549), [Tom Forsyth blog wiki](https://tomforsyth1000.github.io/blog.wiki.html)
  - [chocola-mint afterimage](https://chocola-mint.itch.io/touhou-ice-hockey-festival/devlog/483653/tech-blog-how-i-did-the-afterimage-effect), [dorodo95 smear gist](https://gist.github.com/dorodo95/d8da68df38335153b4a7599026d2b0fd), [SMEAR (2024)](https://hal-iogs.archives-ouvertes.fr/hal-04576817v1), [RealtimeVFX weapon swipe](https://realtimevfx.com/t/limeslushie-sketch-42-weapon-swipe/16890)
  - [Epic `ENiagaraRibbonUVEdgeMode`](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/Niagara/ENiagaraRibbonUVEdgeMode)
  - [TrailRendererJS](https://github.com/mkkellogg/TrailRendererJS)
  - [three.js selective bloom example](https://threejs.org/examples/#webgl_postprocessing_unreal_bloom_selective), [three.js forum](https://discourse.threejs.org/t/selective-unrealbloompass-issues/9331)
  - [WWDC20 10632](https://developer.apple.com/videos/play/wwdc2020/10632)
