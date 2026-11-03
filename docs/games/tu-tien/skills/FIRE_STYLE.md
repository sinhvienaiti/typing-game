# Fire style and skill radiance (Sword × Fire), 03/11/2026

Tài liệu thiết kế và nghiên cứu, chưa có mã. Mục đích: trả lời hai lời anh về lửa của phím 1 và về "hiệu ứng xung quanh" của mọi chiêu, đưa anh một bảng hình để chọn kiểu, rồi dựng 3–5 bản ứng viên trong lab theo kiểu anh chọn.

- **Bảng hình cho anh** (không vào Git, chỉ để anh xem): `games/immortality-cultivation/tmp/shots/fire-style/board/board-fire-all.jpg` (12 khung đánh số, kèm khung F88 của ta để so), `board-fire-brushfire.jpg`, `board-fire-starfire.jpg`, `board-fire-halo-seal.jpg`; nguồn từng khung trong `board-sources.md` cùng thư mục.
- **Nghiên cứu nguyên văn và bảng kiểm nguồn:** [`source/fire-style-chatgpt-2026-11-03.md`](source/fire-style-chatgpt-2026-11-03.md) (ChatGPT, Chat, thinking High, hai lượt: nghiên cứu rồi tự rà soát) và [`source/fire-style-gemini-2026-11-03.md`](source/fire-style-gemini-2026-11-03.md) (Gemini 4 Argon, mức Cao). Gemini chạy được: hộp thoại xin nối dữ liệu Google đã chặn lượt trước lúc 17:08 không còn khi Claude mở lại lúc 18:39 (Claude không bấm gì).
- **Phạm vi:** lửa va chạm, tia lửa và lớp hào quang quanh các hình của chiêu (tụ lực, chớp phóng, lửa, nhát chém, ấn, tia, vụ nổ, đất cháy). **Không** làm lại hào quang quanh kiếm bay: đó là [`SWORD_AURA.md`](SWORD_AURA.md). **Không** đụng việc lửa lưu lâu hơn (vòng 3, agent khác đang làm).
- **Kiểm từng chiêu, từng pha** (phím 0–7, Metal và Fire), xếp hạng chỗ thiếu và lớp dùng chung cho mọi hệ: [`SKILL_RADIANCE.md`](SKILL_RADIANCE.md). Tài liệu đó dùng lại `GlintPool`, vệt của `EmberPool` và vòng mảnh của §5.1.
- **Luật áp dụng:** `AGENTS.md` mục "Skill effects sparkle too"; skill `game-vfx-layered` bước 3 "Every shape sparkles"; chuẩn [`VFX_STANDARD.md`](../../VFX_STANDARD.md); trần 0,85 ms ở [`ELEMENT_LAYER.md`](ELEMENT_LAYER.md) §5.

## Quyết định của anh (03/11/2026, tối)

Anh trả lời "đồng ý trộn" cho đề xuất của Claude. Hướng là trộn ba phần:

- **Thân lửa theo A · Brushfire Calligraphy** (khung 1, 3):
  - 3 nét lửa lớn cong theo lực nhát kiếm, thêm 4–5 nét phụ và vài mẩu rời;
  - mép sắc trên lớp lót tối, dải màu theo bậc, lõi trắng ≤ 5 %;
  - tắt bằng cách các nét tách ra và tan từ đầu lưỡi.
- **Tia lửa và sao lấp lánh theo B · Starfire Jewel** (khung 6, 7, 8):
  - tia lửa là vệt mảnh, đầu trắng vàng, đuôi đỏ nguội, ba độ dài, bắn thành 2–3 chùm theo hướng đòn, rơi theo trọng lực, vài vệt nảy một lần;
  - mỗi đòn 1 sao bốn cánh lớn và 2 sao nhỏ lóe nối nhau ở camera chơi (mức vừa, §5.3); dư âm có bụi vàng lấp lánh.
- **Vòng hào quang theo C · Halo Seal** (khung 9, 10), **chỉ ở đòn lớn:** phát chiêu từ ấn, kiếm dẫn đầu phím 7 bổ xuống, nhát kết, tuyệt kỹ. Đòn thường không có vòng.

Claude giữ hai điểm, trừ khi anh muốn khác:
- lửa giữ tông cam đỏ (D54), không thêm màu ngọc bích "dị hỏa";
- hơi nóng méo hình chỉ bật ở cận cảnh, làm sau cùng Water.

Thứ tự làm:
1. Trong lúc hào quang kiếm đang dựng, làm clip Firefly Video (A1 thân lửa, B2 tia lửa, B3 sao lấp lánh, C3 vòng và tia) và gửi anh xem. Bước này không đụng mã.
2. Sau khi hào quang kiếm vào, dựng các mảnh dùng chung (§5.1), rồi làm 3–5 bản ứng viên trong lab: hai mức lấp lánh, hai dải màu, vòng ở mọi đòn hoặc chỉ đòn lớn.
3. Anh thử bằng link local và chọn một bản.

## 0. Hai lời anh (nguyên văn)

1. Về khung F88 của `stills-fixed-light-dark.jpg` (hoa sen lửa va chạm của phím 1 và các hạt tàn lửa tròn): "với cả k thể làm ngọn lửa đẹp hơn sao, nhìn nó hơi xấu, bao gồm cả tia lửa nhìn cũng khá là thô".
2. Về mọi chiêu: "như tôi đã nói, bạn luôn thiếu các hiệu ứng xung quanh, ví dụ trước đó đã nói về vũ khí, bây giờ là với kỹ năng, bạn cũng cần phải xử lý để nó lấp lánh, long lanh hào quang đẹp hơn chứ".

Trước đó cùng ngày anh nói lửa biến mất hơi nhanh ("hình như tôi thấy hiệu ứng bị biến mất hơi nhanh"); việc đó đang được làm ở vòng 3 và không thuộc tài liệu này.

## 1. Chẩn đoán: vì sao lửa xấu, tia lửa thô và thiếu hào quang

**Đã xem:** F88 sáng và tối (`tmp/shots/fire-style/diag/f88-light-crop.png`, `f88-dark-crop.png`, cắt từ `stills-fixed-light-dark.jpg`); khung rút bằng ffmpeg từ hai video anh xem (`diag/close-k1-seq.jpg`, `diag/pull/close-impact2-20fps.jpg`: va chạm thứ hai, 10 khung trong 0,5 s; `diag/pull/close-1.30.png`: ấn và vòng áp suất lúc phóng; `diag/close-seal-slash-ground.jpg`: ấn, nhát kết, đất cháy; `diag/play-k1-impact-zoom.png`: va chạm ở camera chơi); và mã: `src/view/skills/element-fire.ts`, `embers.ts`, `flipbook.ts`, atlas `art-src/lab/vfx/fire/fire-burst.json`, `fire-sparks.json`.

**Tỉ lệ để đọc số:** ở camera chơi 1080p, nhân vật cao ~1,7 m chiếm ~64 px, tức **~38 px/m**; ở cận cảnh, hoa sen va chạm cao ~2 m chiếm ~500 px, tức **~250 px/m**.

**Video anh xem quay trước vòng 3.** Vòng 3 (`000440d` … `10c6e93`) đã sửa quả cầu trắng (thành điểm lửa `fire-points.ts`), vòng có cấu trúc lửa, khung đồ họa, đất cháy, nhát chém lửa. Các điểm dưới đây vẫn đúng với mã hiện tại vì vòng 3 không đổi hình hoa sen, hình tàn lửa, và không thêm lớp hào quang nào.

### 1.1 Ngọn lửa (hoa sen `fire-burst`)

| Điểm | Thấy gì | Do đâu trong mã |
|---|---|---|
| Hình lưỡi lửa | 12–15 lưỡi gần bằng nhau, thẳng, xếp quạt đối xứng: đọc như một bông hoa cam hay vương miện, không phải lửa có hướng | atlas `fire-burst` (Firefly Video try2, 16 khung, ô 512×296): hình có sẵn trong clip; không có cấp lớn–vừa–nhỏ, không móc, không đường cong chữ S, không khoảng trống giữa các lưỡi |
| Mép | Mềm, như phun sơn; ở cận cảnh ô 512×296 bị phóng ~1,7 lần nên mép càng nhòe | `burst.softM = 0.3` (mềm theo đất), `setSharpen(0.06, 0.4)` chỉ làm mép xói gọn hơn khi tàn, không làm mép thân sắc |
| Dải màu và bậc sáng | Một thân cam vàng phẳng, chuyển màu mượt; không có bậc; không có lớp tối viền ngoài, nên trên đá sáng là sáng chồng sáng | màu lấy thẳng từ clip; `setGrade(LOTUS_GOLD, 0.9)` chỉ kéo phần trắng về vàng |
| Lõi trắng | Phần sáng nhất là một dải ngang rộng ở gốc, không phải vài gân mảnh; vẫn là chỗ "tiêu" độ tương phản lớn nhất vào một vệt không hình | gốc trắng của clip; vòng 3 đã đổi về vàng, nhưng diện tích vẫn rộng |
| Cấu trúc bên trong | Không có lưỡi trong khác nhiệt độ, không có lỗ hở; ruột phẳng | clip không có; shader chỉ tô lại |
| Lớp và chiều sâu | Một tấm quay mặt về camera, đặt **trước** con thú (`lift 0.7`): con thú biến mất sau một miếng dán cam | `lotus()` → `burst.spawn(...)`, một thẻ; không có lớp sau, lớp trước, bóng lửa tối phía sau |
| Chuyển động | Cả quạt phóng to (khung 0–6), giữ (5–9), rồi co về một lưỡi giữa (10–14): đổi kích thước chứ không đổi hình; các lưỡi không tách, không cuộn, không rời ra theo thứ tự | `LOTUS_PEAK = 7`, `rate 1.25`, `slowRate 0.48`: chỉ đổi tốc độ phát clip |
| Chỗ đứng trên đất và trên thú | Gốc là một đường cắt ngang thẳng; có vết cháy dưới (tốt) nhưng không có chớp tiếp xúc, không vòng sáng, không ánh hắt lên đất; số sát thương đè ngay lên thân lửa | flipbook đặt `ground 0`, không có decal sáng tạm thời |
| Ở camera chơi | Lửa va chạm chỉ ~70–110 px, chữ số "34" che gần hết; tia lửa không thấy | quy mô `2.0 × s` m |

### 1.2 Tia lửa và tàn lửa

| Điểm | Thấy gì | Do đâu trong mã |
|---|---|---|
| Hình | Đĩa tròn đặc mép gọn: "bong bóng cam", "bokeh" | `embers.ts` fragment: `cov = 1 − smoothstep(0.24, 0.38, r)` là một đồng xu; vệt kéo chỉ `stretch 0.03 s` × tốc độ (≤ ~4 m/s ⇒ ≤ 0,13 m) so với cỡ 0,08–0,28 m, nên gần như luôn tròn |
| Cỡ | Đều, to: cận cảnh 20–70 px, camera chơi 3–11 px | `emberBurst`: `size = 0.08 + 0.2·r³` m |
| Chấm phát sáng thêm | Chấm mờ tròn cộng sáng, như đèn bokeh | `ember()` dùng `SpritePool` với `T.glow` (vệt sáng tròn), 0,10–0,16 m, ×1,8–2,4 |
| Đường bay | Bắn ra rồi phanh gấp (cản 2,2–3,4 /s), rồi trôi lên (nổi 0,8–1,6 m/s²) và lắc lư: "bong bóng nổi" thay vì mảnh nóng bay vòng cung và rơi | `drag`, `rise`, `sway` của `emberBurst` và `risingEmbers` |
| Hướng | Tỏa đều 360° quanh điểm đánh; không có chùm theo hướng kiếm, không có tia dẫn đầu | `emberBurst`: góc ngẫu nhiên đều |
| Màu | Một dải hổ phách–cam đều; đầu và đuôi cùng màu | `ramp()` theo nhiệt độ của cả hạt, không theo dọc vệt |
| Nhấp nháy | Một nhịp mờ đều (hai sóng sin), không có "lóe" | `flicker` 0,25–0,5 |
| Số lượng ở một đòn phím 1 | ~18 tàn lửa tròn + 8–14 chấm sáng tròn, gần như cùng cỡ: ~30 vật tròn giống nhau | `emberBurst(…, 1.1·s)` + `ember()` × `8 + 6·power` |
| Tia kim | Một flipbook tia thẳng tỏa đều như nan bánh xe; cộng sáng màu vàng nên trên đá sáng gần như mất | `sparkRays` → atlas `fire-sparks` (14 khung, cộng sáng, nhuộm `SPARK_TINT`) |

### 1.3 Thiếu gì "xung quanh"

Trong bộ chất Fire **không có một ngôi sao bốn cánh, một vòng mảnh, một tia sáng, hay một điểm sáng chạy** nào:

| Hình của pha | Hiện có | Không có |
|---|---|---|
| Tụ lực ở tay | flipbook `fire-charge`, tàn lửa hút vào, đất tối dưới chân | vòng sáng co lại, chớp sao trên kiếm hay chuôi |
| Chớp phóng | điểm lửa, vòng áp suất (`HeatRingPool`, một vành dày đều), hoa sen sau lưng | vài tia mảnh theo hướng phóng, một sao lóe 1–2 khung |
| Kiếm bay | vỏ lửa, dải lửa (phần của `SWORD_AURA.md`) | (ngoài phạm vi) |
| Va chạm | điểm lửa, hoa sen, tia kim, tàn lửa tròn | sao lớn và sao nhỏ lóe lệch nhịp, vòng mảnh nở, vài tia hẹp, ánh hắt lên đất |
| Nhát chém (`cut()`, nhát kết của phím 7) | trăng lưỡi liềm vật chất cam + vạch vàng 0,72; `FlameSlash` | mép trước sáng mảnh, ánh chạy dọc nhát, bụi lấp lánh rơi khỏi đuôi |
| Ấn trên đất | nét đỏ son trên lớp than, một vạch vàng giữa (≤ 0,9) | ánh chạy vòng quanh nét, sao lóe ở chỗ nét giao nhau, vòng mảnh ngoài, bụi sáng bay lên |
| Đất cháy | vết cháy, lửa thấp `fire-ground`, khói, tàn lửa tròn bay lên | vài lóe thưa trên vết nứt, khe nứt có ánh chạy |
| Tia `glint` của phím 7 | **một chấm tròn** `CORE × 2,4` | chính cái Metal gọi là "glint" thành chấm trong Fire |

**Tóm lại:** lửa có **một tần số thị giác** (lưỡi giống nhau, sáng giống nhau, mềm giống nhau, hạt tròn giống nhau); tia lửa là đồng xu nổi; và quanh mọi hình không có lớp lấp lánh nào. Cả ChatGPT và Gemini, đọc độc lập mô tả bằng chữ, đi tới cùng kết luận.

## 2. Nghiên cứu nói gì (đã kiểm)

Chi tiết và bảng kiểm từng câu ở hai file `source/`. Ở đây chỉ các điều dùng để dựng. **Đúng** = đã mở nguồn (hoặc đã tự chụp khung video) và nguồn nói đúng như vậy; **suy luận** = trợ lý tự ghi là suy luận của nó, Claude thấy hợp lý với camera của ta.

| Điều | Trạng thái | Nguồn |
|---|---|---|
| Độ gây chú ý theo tầm quan trọng; không "vặn mọi thứ lên 11" | Đúng | Riot "Clarity in League" (2021) |
| Mọi hiệu ứng có chuẩn bị và tan; phần kết là hiệu ứng phụ, thấp hơn về độ sáng, độ bão hòa, độ đục; trộn hình mềm và sắc, hình bóng rõ | Đúng | Riot VFX Style Guide (PDF 2017, bản lưu web.archive.org) |
| Lửa ảo khác nhau nhờ lõi nóng, chuyển màu, tia lửa và khói, không chỉ đổi màu một lửa chung | Đúng | Riot, Little Demon Tristana (2019, bản lưu) |
| Lửa cách điệu = vài mặt nạ đóng gói RGB cuộn khác tốc độ, dải trong có ngưỡng cắt riêng | Đúng | Soenke Seidel, 80.lv (2021) |
| Tụ lực: quả cầu Fresnel lớn dần, hạt hút vào tâm, vòng co lại; nhiễu đỉnh để thân sống | Đúng | Rayane Saada, 80.lv (2024) |
| Va chạm tách thành chớp chính + khói + tàn lửa + vết sáng + mảnh vụn | Đúng | David Gao, 80.lv |
| Tia lửa: đổi sang bản kéo dài khi nhanh, chỉ kéo phần giữa ("hotdog"), không kéo cả hình tròn | Đúng | ryangatts (Paragon), RealTimeVFX 2019 |
| Tia lửa bắt đầu dài, co dần thành chấm | Đúng | Guillermo Rossell, 80.lv |
| Không phun tia lửa hình cầu; bắn theo vài chùm hình nón; chớp gai 1–2 khung ở đầu | Đúng | cEssex, RealTimeVFX (chủ đề 29528) |
| Tàn lửa thiếu kết cấu riêng trông rất tệ khi lên video | Đúng | Sheila Stipnieks, ArtStation |
| Lửa đẹp = hạt sáng + dải cuộn + flipbook, không phải một clip | Đúng | Jonny Cadman, ArtStation |
| Ở pha thả, sao bốn cánh ba cỡ, vòng cung sáng mảnh và bụi lấp lánh bao quanh chiêu | Đúng (khung tự chụp) | Yoimiya demo 1:24–1:26 |
| Vòng mảnh nhiều lớp (một lớp ánh cầu vồng) quanh nhát kết, trụ lửa đứng trên vòng | Đúng (khung tự chụp) | Changli 2:31–2:32 |
| Ấn vẽ bằng một nét sáng mảnh, tia sáng hẹp, bụi tàn lửa | Đúng (khung tự chụp) | Jiaoqiu 0:53 |
| Ở camera game trên bê tông sáng: mỗi đòn lóe một sao bốn cánh gọn; vòng lửa quét quanh địch | Đúng (khung tự chụp) | Burnice Combat Intel 0:33, 0:35 |
| Tia lửa đẹp: đầu trắng nóng, đuôi dài đỏ cam nguội dần, đường cong | Đúng (khung tự chụp) | Firefly trailer 2:23 |
| Dựng hiệu ứng nền đen cho lửa và hạt; Firefly Video có nền trong suốt (video tiền cảnh + alpha), 5 s, 24 fps; quá bốn chủ thể làm Firefly rối | Đúng | Adobe helpx (06/2026, 08/2026) |
| Pack CC0: Kenney Particle (có `star_01–09`, `circle_01–05`, `spark_01–07`, `trace_*`), Screaming Brain noise (ghi không dùng AI tạo sinh), EffectTextureMaker (kết cấu tạo ra là CC0), ambientCG | Đúng | trang giấy phép của từng nơi; Kenney đã có bản tải |
| 3–5 lưỡi chính cong + 4–7 lưỡi phụ + 2–4 mẩu rời; 10–25 % khoảng trống; trắng thật chỉ 2–5 % diện tích lửa ở camera xa; lớp lót tối quanh 30–60 % viền trên đá sáng | Suy luận (ChatGPT; Gemini nói tương tự) | — |
| Kích thước ở camera chơi: vệt 1,25–2 px rộng, 7–18 px dài; sao nhỏ 4–7 px, lớn 8–12 px; vòng 1,5–2 px; sao sống 4–8 khung | Suy luận | — |
| Mỗi pha một họ hào quang chính; tiết kiệm ở mật độ, sang ở chỗ đặt | Suy luận (khớp với Riot "never up to 11") | — |

**Không kiểm được:** số điểm Reddit và các lời khen của fan (Reddit bị chặn trong trình duyệt của ứng dụng và sandbox); lời chê hiệu ứng Yoimiya nhạt (không có link); "Firefly hạng 1 bình chọn" (wiki fan); ArtStation của Pawel Margacz (lỗi chứng chỉ); câu "đèn hạt tốn, giả bằng tấm" (nguồn "+1" không có trong DOM). **Sai, đã loại:** quy tắc "70/20/10 của Riot" (không có trong nguồn nào), bài Simon Trümpler "về lửa lưới" (bài về RiME), mốc Burnice 1:19, và nhiều mốc video của cả hai trợ lý (ChatGPT lượt 2: 6 trên 13 mốc sai, 3 yếu; Gemini: 5 trên 24 mốc sai, 9 chỉ đúng một phần; bảng E2 và C2 trong `source/`). **Hai trợ lý không xem được khung video;** Gemini ghi "đã xem từng khung" nhưng 5 trên 24 mốc sai hẳn. Mọi khung trên bảng hình là Claude tự chụp ở kênh chính thức và tự nhìn.

**Chỗ nguồn ngược với anh:** Riot và VFX Apprentice khuyên hiệu ứng ngắn để đỡ rối. Anh muốn lửa lưu lâu hơn. Luật của anh thắng; cách dung hòa: thân lửa và đất cháy lưu (vòng 3), còn **lớp hào quang sống ngắn** (sao 4–12 khung, vòng 10–20 khung), chỉ ánh chạy trên ấn và vài lóe thưa là lưu.

## 3. Ba hướng (bảng hình)

Ba hướng khác nhau ở **ngữ pháp hình**, không chỉ ở màu: **nét** (A), **điểm** (B), **vòng** (C). Anh có thể trộn: lửa của A, tia lửa của B, hào quang của C.

| Hướng | Ý | Khung trên bảng | Lấy gì (nguyên lý) | Không lấy |
|---|---|---|---|---|
| **A · Brushfire Calligraphy** | Lửa là vài nét bút đi theo lực của kiếm: ít lưỡi, cong, có hướng, mép sắc trên lớp lót tối; tàn lửa là vảy nóng rời khỏi nét | 1 Changli 2:06 · 2 Rengoku 0:39 · 3 Phàm Nhân Tu Tiên 0:46,5 · 4 Arlecchino 1:00 | lưỡi lửa như nét lông vũ theo nhát chém (1); xoáy thư pháp móc đầu, vảy lửa nhiều cỡ (2); lửa liếm ngoài mép kiếm trên thân tối, đúng chất tu tiên (3); vệt lửa kéo trên đất, tàn lửa thon đầu nóng trên nền sáng vừa (4) | lông phượng, hình chim (Changli); đỏ thẫm đen của Arlecchino |
| **B · Starfire Jewel** | Vụ nổ dàn dựng như trang sức: một điểm → cánh lửa lệch → vòng nhỏ trễ 2–3 khung → bụi vàng; tia lửa vệt mảnh cao cấp; sao bốn cánh | 5 Yoimiya 1:26 · 6 Firefly 1:29 · 7 Firefly 2:23 · 8 Burnice Intel 0:33 | vòng cung sáng, bụi lấp lánh, sao ba cỡ quanh chiêu (5); vệt mảnh nhiều độ dài, lõi dày, sao ở vài đầu vệt (6); vệt cong đầu trắng đuôi đỏ nguội (7); sao lóe ở mỗi đòn ở camera game trên đá sáng (8) | pháo hoa hình cầu, cá vàng, lễ hội (Yoimiya) |
| **C · Halo Seal** | Lửa bị buộc vào hình học sáng: vòng mảnh, ấn, tia; lửa đứng lên từ ấn; nền tối để vòng mảnh đọc rõ. Đúng chữ "hào quang" và nối với ấn trên đất của ta | 9 Changli 2:32 · 10 Jiaoqiu 0:53 · 11 Mavuika 3:44 · 12 Burnice Intel 0:35 | nhiều vòng mảnh, một vòng ánh cầu vồng, trụ lửa trên vòng (9); ấn là một nét sáng mảnh, tia hẹp, bụi (10); khung "mặt trời" của tia và vòng sau đòn đánh (11, chỉ ý); vòng lửa quét quanh địch ở camera game trên nền sáng (12) | glyph mặt trời của Mavuika; lông phượng của Changli; con mắt và nhật thực của Arlecchino |

- **Tia lửa cao cấp:** khung 2, 4, 6, 7. **Lấp lánh, sao, hào quang quanh chiêu:** khung 5, 8, 9, 10, 11.
- **Vì sao không có hướng "lửa tối" (Inkfire, Crimson Eclipse, Abyssal Blood-Sun):** cả hai trợ lý đề xuất, nhưng đó là một **tính chất** cả ba hướng đều cần trên đá sáng (lớp lót tối, khoảng trống), và bản nào cũng trượt về dấu ấn đỏ đen của Arlecchino. Nếu anh muốn lửa tối cho tuyệt kỹ hay boss, nó là một nhánh của A.

## 4. Bộ kit của từng hướng theo pha

Mọi số đo ở camera chơi (≈ 38 px/m), cận cảnh trong ngoặc; sao và tia có **kẹp cỡ trên màn hình** để cận cảnh không thành sao giao diện khổng lồ. Thời gian theo khung 60 Hz. Lõi HDR (3–6, chỉ vài px) là phần duy nhất được nở bloom; thân, vòng, cánh sao ≤ 0,9 mỗi kênh. Không màu nào dùng đỏ cảnh báo `#FF4A4A` của địch (D54).

### 4.1 Dải màu (sRGB)

| Bậc | A · Brushfire | B · Starfire | C · Halo Seal |
|---|---|---|---|
| Lót tối (mép, nền) | `#1E0A0C` mực rượu | `#2A0E08` than hồng | `#1A0C08` than |
| Đỏ thẫm | `#6E1414` | `#A8300E` | `#8C2A10` |
| Thân | `#D2401C` son | `#FF8A2A` cam (ORANGE hiện có) | `#E0561A` (SEAL_BODY hiện có) |
| Sáng | `#FF7A26` | `#FFB703` hổ phách (AMBER hiện có) | `#FFAE34` × 0,9 (SEAL_LIT hiện có) |
| Vàng | `#FFB43A` vạch mảnh | `#FFD866` | `#FFD38A` vạch vòng |
| Lõi (HDR, chỉ vài px) | `#FFF8E0` | `#FFF3C8` | `#FFE7A8` |

### 4.2 A · Brushfire Calligraphy

| Pha | Hình chính | Tia lửa | Hào quang quanh hình | Nhịp |
|---|---|---|---|---|
| Tụ lực | lửa cuộn thành nét quanh tay, siết theo phím gõ | 3–5 vảy nóng hút vào | 1 vòng nửa (cung 200–260°) co lại, 1,5 px; 1 sao nhỏ (5–7 px) trên chuôi mỗi phím | vòng co trong 8–12 khung mỗi phím |
| Phóng | một nét lửa quét theo hướng phóng | 3 vệt thon dẫn đầu theo hướng đó | 1 sao lớn (10–14 px) lóe ở tay, 2–3 tia hẹp (1–2 px) theo hướng | sao 1–2 khung lên, 3–4 khung xuống |
| Bay | (vỏ lửa và dải: `SWORD_AURA.md`) | vảy nóng rời khỏi vệt, thưa | một điểm sáng chạy dọc mép vệt | — |
| Va chạm | 3 nét lửa lớn cong theo lực kiếm + 4–5 nét phụ ngược + 2–3 mẩu rời; lót tối hiện ở 30–60 % viền; trắng ≤ 5 % | 4–7 vệt thon (1,5–2 px × 8–20 px; cận 3–5 × 40–120 px) trong 2–3 chùm theo tiếp tuyến nhát chém, 6–10 vảy nhỏ, 1–2 vệt nảy một lần | vòng lưỡi liềm vỡ (một cung) nở theo nhát; 1 sao lớn + 2 sao nhỏ lệch 2 khung; vết sáng hắt trên đất 5–12 khung | nét bung 3–5 khung, giữ, rồi từng nét tách và xói từ đầu lưỡi |
| Dư âm | đất cháy, lửa thấp thành vài nét nằm | vảy nóng bay lên thưa (3–5 mỗi giây), thon chứ không tròn | ánh chạy 90–180° dọc nét ấn; 0–2 lóe mỗi giây ở khe nứt | ánh chạy 0,6–1 s |

**Vì sao sang:** giàu ở đường cong và viền chồng lớp, không ở số lượng. Ở 64 px vẫn còn cử chỉ chính; ở 500 px thấy được nét trong, lót tối và mẩu rời.

### 4.3 B · Starfire Jewel

| Pha | Hình chính | Tia lửa | Hào quang quanh hình | Nhịp |
|---|---|---|---|---|
| Tụ lực | lửa nén về một điểm vàng trắng | 3–5 hạt sáng hút vào | 4–6 bụi vàng xoáy về tâm, sao nhỏ ở mỗi phím | — |
| Phóng | điểm nổ thành 4 tia cực mảnh | 1–2 vệt dài dẫn đầu | 1 sao lớn sáu cánh (tuyệt kỹ) hoặc bốn cánh | sao 4–6 khung |
| Bay | — | đôi khi một chùm 3 tia nhỏ khi đổi hướng | sao nhỏ lóe thưa ở đầu vệt | — |
| Va chạm | hoa sen lệch: 2 cánh lớn, 3 vừa, 3 nhỏ, đầu cánh tách, có khe; một cánh bắn ngang và rời sớm; một lần nở phụ trễ 2–3 khung | 6–10 vệt ba độ dài trong 2–3 cụm lệch, 1–2 vệt dài dẫn đầu, một chùm 3 tia nhỏ trễ; bụi vàng 1–2 px sau cùng | 1 sao lớn + 3–4 sao nhỏ lóe nối nhau ("ting ting"), 1 vòng mảnh nở trễ 2–3 khung | điểm → quạt → vòng → bụi |
| Dư âm | lửa thấp, vài cánh nhỏ cháy tàn | bụi vàng lấp lánh nổi lên, 6–10 hạt | sao nhỏ thỉnh thoảng hiện ở chỗ nét ấn giao nhau | bụi sống 0,5–1,2 s |

**Vì sao sang:** nhịp như trang sức (điểm, quạt, vòng, bụi), gần nhất với chữ "lấp lánh, long lanh" của anh. **Rủi ro:** dễ thành rắc kim tuyến khắp nơi; cần trần số sao (mục 5.3).

### 4.4 C · Halo Seal

| Pha | Hình chính | Tia lửa | Hào quang quanh hình | Nhịp |
|---|---|---|---|---|
| Tụ lực | ấn dưới chân sáng dần theo phím gõ (đã có `GroundSigil`) | — | vòng mảnh ngoài ấn khép lại; một điểm sáng chạy quanh vòng mỗi phím | — |
| Phóng | ấn bừng sáng; lửa đứng lên ở 4–6 điểm trên vòng | tia lửa bắn từ vòng theo cung ngắn | 2–3 vòng mảnh đồng tâm nở (một vòng ánh cầu vồng nhẹ), 4–6 tia hẹp | vòng nở 10–16 khung |
| Bay | — | — | — | — |
| Va chạm | ấn nhỏ hiện dưới con thú; 4–6 trụ lửa ngắn đứng trên vòng, nghiêng ra; lõi vàng mảnh | vệt thon bắn ra khỏi vòng, rơi theo trọng lực | vòng mảnh 1,5–2 px nở; sao lóe ở chỗ vòng gặp nét ấn | trụ lửa bung 3–4 khung, cháy tàn |
| Dư âm | ấn còn lại trên đất cháy, nét nguội dần | 2–4 vảy nóng thưa | ánh chạy vòng quanh ấn, 0–3 sao lóe mỗi giây ở giao điểm; một gợn vòng rất mờ | 1–2 s |

**Vì sao sang:** hình học tinh, mảnh, sáng trên nền tối, đúng chất "pháp ấn" tu tiên; hào quang là chính hình, không phải lớp rắc thêm. **Rủi ro:** vòng lớn che đất và thẻ chữ; ≥ 65 % diện tích ấn phải dưới 0,15 độ đục, vòng không bao giờ thành màn.

## 5. Cách dựng trong lab và chi phí

### 5.1 Ba mảnh dùng chung (cho mọi hệ, dựng trước)

1. **`GlintPool`** (mới, kiểu `fire-points.ts`: tính trên GPU, instanced, một lệnh vẽ, không cấp phát mỗi khung): sao bốn cánh vẽ giải tích (hai hình thoi mảnh chéo nhau + lõi tròn tí hon), biến thể sáu cánh cho tuyệt kỹ; cánh ≤ 0,9, chỉ lõi 1–2 px là HDR 3–4; cỡ tính bằng px trên màn hình, có kẹp (nhỏ 5–8 px, lớn 10–14 px; cận cảnh 12–20 / 20–32 px); sống 4–8 khung (lên 1–2, đỉnh 0–1, xuống 3–5); lệch pha, xoay 0/45°, tỉ lệ cánh ngẫu nhiên. Sức chứa 256; trần phím 7 là 48 sao sống. Các sao bốn cánh trong Kenney `star_01–09` (CC0, đã có ở `~/VFXLab/packs/kenney-particles`) dùng để thử nhanh trước khi viết SDF.
2. **Chế độ vệt cho `EmberPool`** (sửa shader, cùng lệnh vẽ, **không tăng số hạt**): hình viên con nhộng "hotdog" (đầu tròn, chỉ kéo phần giữa); nhiệt dọc vệt (đầu trắng vàng → thân vàng → đuôi đỏ cam về 0); dài = kẹp(cơ bản + tốc độ × k); bề rộng tối thiểu 1,5 px trên màn hình; ba lớp cỡ (15 % vệt chính, 55 % vệt vừa, 30 % bụi 1–1,5 px); họ "vệt" ít cản (0,3–0,8 /s) với trọng lực −9,8, 10–20 % nảy một lần trên mặt đất y = 0 (tính giải tích trong shader); họ "vảy" bay lên chậm như cũ nhưng thon; vài hạt lóe 2 khung trước khi tắt; phát theo 2–4 chùm hình nón theo hướng đòn, không đều 360°. Thay cả `emberBurst` và chấm `ember()`; `sparkRays` (flipbook nan bánh xe) bỏ.
3. **Vòng mảnh** (mở rộng `HeatRingPool` / `GroundSigil`): vòng giải tích `d = |length(uv) − r|`, bề rộng tính bằng px qua `fwidth` (1,5–2 px ở camera chơi), cung vỡ bằng mặt nạ góc, một đoạn sáng chạy quanh, mặt đất hoặc mặt camera; ≤ 0,9. Cùng shader cho vòng tụ lực, vòng va chạm, vòng ấn, sóng xung kích của tuyệt kỹ, mọi hệ chỉ đổi màu và nhịp.
4. **Ánh chạy trong shader sẵn có** (ấn, nhát chém, vạch nứt của đất cháy): một uniform đẩy một đoạn sáng hẹp dọc toạ độ nét; **không thêm lệnh vẽ**. Chỗ nét giao nhau thì gọi `GlintPool`.
5. **Lớp lót đất tối tạm thời** dưới mỗi va chạm (đã có `GroundDecalPool`): 1,25 lần bán kính lửa, đục 0,55–0,7 trong 0,35 s đầu rồi thành vết cháy; giữ nền tối cho lửa và sao trên đá sáng.

### 5.2 Thân lửa theo hướng

| Hướng | Cách dựng | Nguồn chất |
|---|---|---|
| A | 3 nét chính + 4–5 nét phụ là dải lưới (kiểu `RibbonPool` / `FlameSlash`) uốn theo hướng đòn, đuôi nhọn; shader đọc mặt nạ đóng gói (R nét ngoài, G vùng nóng trong, B nhiễu vỡ), dải màu 5 bậc có khử răng cưa bằng `fwidth`, xói từ đầu lưỡi; mẩu rời là thẻ nhỏ. Cận cảnh thêm nhiễu đỉnh | clip Firefly Video A1 (nền trong suốt) làm mặt nạ nét, hoặc vẽ tay; nhiễu Screaming Brain (CC0) |
| B | giữ ô `fire-burst` của `FlipbookPool`, thay atlas: hoa sen lệch 2/3/3 cánh, nở phụ trễ; dải màu bậc thay cho `setGrade`; vòng và sao do 5.1 lo | clip Firefly Video B1 (nền trong suốt) |
| C | ấn + vòng (5.1) là thân; 4–6 trụ lửa ngắn là thẻ đứng trên vòng (dùng lại `line` / `ground` pools); tia hẹp bằng `BeamPool` | clip Firefly Video C1 cho trụ lửa; vòng và ấn vẽ giải tích |

Ở camera chơi (lửa 70–110 px) một thẻ đúng góc với hình bóng tốt vẫn đủ; lưới cánh hay dải 3D chỉ cho va chạm lớn và cận cảnh (cấp chi tiết theo cỡ trên màn hình: < 60 px chỉ thân, lõi, 3–6 vệt, tối đa 1 sao; 60–180 px thêm mẩu rời và sao thứ hai; > 180 px thêm nét trong, bụi, hơi nóng nếu anh cho).

### 5.3 Số đếm và trần

| | Đòn thường phím 1 (camera chơi) | Cận cảnh | Dòng sông phím 7 (mỗi đòn) | Kiếm dẫn đầu phím 7 |
|---|---|---|---|---|
| Vệt tia lửa | 4–7 | 6–10 | 2–3 | như phím 1 |
| Vảy, bụi | 6–10 | 10–14 | 0–2 | 4–6 |
| Sao | 1 lớn + 2 nhỏ | 1 lớn + 3–5 nhỏ | 0–1 (theo trần chung 48) | 1 lớn + 1 nhỏ |
| Vòng | 1 | 1–2 | 0 | 1 |

Tổng không vượt 1.900 hạt hiện có; 48 sao sống ở phím 7; 24 vòng sống; ánh chạy không tốn hạt.

### 5.4 Chi phí (ước lượng, phải đo)

Fire hiện chỉ hơn Metal ~+0,1–0,2 ms p95 (trung vị) trên phím 7 ở High (changelog Fire phần 5), nên còn ~0,65 ms trong trần 0,85 ms.

| Phần | Lệnh vẽ thêm | Ước lượng p95 phím 7 High |
|---|---|---|
| `GlintPool` (48 sao, quad nhỏ) | +1 | 0,03–0,08 ms |
| Vệt trong `EmberPool` | 0 | ±0,05 ms (vệt mảnh tô ít điểm ảnh hơn đĩa tròn) |
| Vòng mảnh (24 sống; quad lớn nhưng loại sớm) | 0–1 | 0,05–0,12 ms |
| Ánh chạy trong shader | 0 | < 0,02 ms |
| Thân lửa A / B / C | 0–2 | A 0,10–0,25; B 0,05–0,15; C 0,10–0,20 ms |
| **Cộng thêm so với Fire hiện tại** | | **A ~0,2–0,5; B ~0,15–0,4; C ~0,2–0,45 ms** |

Chừa 0,15–0,2 ms an toàn. Đo bằng `scripts/visual/scenarios/lab-element-perf.mjs` như các phần trước (Fire − Metal, 6 vòng xen kẽ, `RUNS=2`), qua `../../.local/bin/heavy.sh --gpu` trên server không HMR. Số đếm chồng lớp trong suốt ghi vào `meta.json` (≤ 2 lớp ở một điểm ảnh, ELEMENT_LAYER §5).

### 5.5 Prompt Firefly Video (chỉ model Firefly Video của Adobe)

Luật chung: camera Static; một hiệu ứng ở giữa, chiếm ≤ 65–75 % khung; thân lửa dùng **Transparent background** (alpha thật, giữ được mép tối trên đá sáng); tia lửa và sao dùng **nền đen phẳng** rồi cộng sáng (Adobe khuyên nền đen cho lửa và hạt). Không gọi tên game, nhân vật, studio ("ufotable style" của Gemini bị loại). Không ghi "cinematic", "realistic", "volumetric", "lens flare", "bokeh", "depth of field". Dưới 600 ký tự mỗi prompt, ≤ 4 chủ thể.

- **A1 · flame (Transparent):** `Stylized anime xianxia fire impact, isolated, static camera, centered, whole shape in frame. Three long sweeping brushstroke flame tongues curving one way like a sword's follow-through, four smaller counter-curves and two detached licks that peel off. Crisp clean edges, flat stepped colours: dark wine edge, crimson, vermilion, orange, a thin gold line inside, tiny ivory hot cores. Fast strike, short hold, strokes tear apart from the tips. No ground, no smoke cloud, no blur, no soft glow, no white blob, not photoreal.`
- **A2 · sparks (black):** `Stylized anime spark burst on a pure black background, static camera, centered. Sparse thin tapered streak sparks in two or three clumps flying one way, three sizes, each with a tiny white-gold head and a vermilion tail that thins to nothing; curved paths that bend down with gravity, two sparks bounce once. Crisp and fast, then the streaks shrink to dots and wink out. No round dots, no bokeh, no floating bubbles, no smoke, no lens flare, not photoreal.`
- **A3 · glints (black):** `Sheet of separate small 4-point star glints on a pure black background, static camera. Each star has razor-thin long arms and a tiny bright centre, warm gold arms, ivory centre, three sizes, widely spaced so none overlap. Each flashes on in one or two frames, holds briefly, shrinks away; a few turn slightly. Clean anime effect sheet. No lens flare, no bokeh, no haze, no glow cloud, no text, no objects.`
- **B1 · flame (Transparent):** `Stylized anime fire burst shaped like an opening lotus, isolated, static camera, centered. Asymmetric petals: two large, three medium, three small, each curved with a split tip and gaps between them; one petal fires sideways and breaks away early, a second smaller pop opens a moment later. Crisp edges, stepped colours: dark ember-red edge, red-orange, orange, amber, gold, a small pale-gold centre. No symmetry, no firework sphere, no smoke, no blur, no white blob, not photoreal.`
- **B2 · sparks (black):** `Stylized anime jewel-like spark burst on a pure black background, static camera. Six to ten crisp thin streaks in three lengths, white-gold heads, gold bodies, orange tails that cool and thin; launched in two or three uneven clusters along curved gravity arcs, one long leading streak, then a tiny delayed second burst of three sparks and a few fine gold glitter specks that twinkle out. No round dots, no bokeh, no fountain, no smoke, not photoreal.`
- **B3 · glints (black):** `Sheet of separate radiant twinkles on a pure black background, static camera: 4-point stars, a few 6-point stars, tiny diamond sparkles and one thin broken light ring, warm gold with ivory centres, three sizes, staggered so they flash one after another, each lasting a few frames. Crisp anime jewellery sparkle, lots of empty black space. No lens flare, no bokeh, no haze, no overlapping shapes, no text.`
- **C1 · flame pillars (Transparent):** `Stylized anime xianxia seal of fire, isolated, seen from a high three-quarter angle, static camera. A thin glowing ring with a few fine inner line marks; five short crisp flame pillars rise from points on the ring and lean outward, dark red edges, orange bodies, thin gold cores; the ring flares, the pillars burn down and break into a few embers. Crisp clean shapes, stepped colours. No ground texture, no smoke, no blur, no white blob, not photoreal.`
- **C2 · sparks (black):** `Stylized anime spark spray on a pure black background, static camera. Thin tapered sparks fly outward from a circle in a few short arcs, white-gold heads and orange-red tails, then fall with gravity; a few small hot flakes drift up and wink out. Sparse, crisp, graphic. No round dots, no bokeh, no uniform radial burst, no smoke, no lens flare, not photoreal.`
- **C3 · rings and rays (black):** `Effect sheet on a pure black background, static camera: separate thin light rings that expand and fade, some broken into arcs, a bright point running along one ring, short thin light rays fanning out, and small 4-point star glints where lines cross. Warm gold and pale orange, hairline-thin, crisp. No lens flare, no bokeh, no thick glow, no overlapping shapes, no text.`

Cắt atlas: thân lửa từ cặp video tiền cảnh và alpha của Firefly (alpha thật, nhân trước); tia và sao từ nền đen, alpha = smoothstep(0,06; 0,22; max(R,G,B)) rồi nhân trước (mẹo của Gemini, khớp bài học `DRAGON_FIRE_DIAGNOSIS`). Các nguồn CC0 khác chỉ để thử nhanh và làm nhiễu; ghi vào `docs/games/THIRD_PARTY.md` khi dùng.

## 6. Kế hoạch

1. **Anh chọn trên bảng hình** `board-fire-all.jpg`: trả lời bằng số ("tôi thích 2, 6, 9"), có thể trộn hướng. Nếu anh muốn xem thêm mẫu trong kiểu đã chọn trước khi chốt, Claude đưa thêm 9 khung trở lên từ kênh chính thức.
2. **Lab, chưa vào game:** sau khi vòng 3 (lửa lưu lâu) xong, dựng ba mảnh dùng chung (5.1) trước, rồi **3–5 bản ứng viên cùng lúc** theo kiểu anh chọn (ví dụ: hướng chọn ở ba mật độ lấp lánh, hai dải màu, có và không có vòng), chuyển bằng cờ lab và phím, Metal không đổi từng bit.
3. **Video và ảnh cho anh:** phím 1 cận cảnh và camera chơi, đá sáng và tối, phím 7 săn và nhát kết; khung tương đương F88 cho mỗi ứng viên; tấm khung theo pha 720p và 1080p; đo: khung đầu ≥ 95 % đỉnh, trắng xóa ≤ 6 %, phần nhạt ≤ 15 % ở khung va chạm, tương phản thẻ chữ, Fire − Metal p95 ≤ 0,85 ms trên phím 7 High. Khi giám khảo chấm ≥ 7 thì gửi anh video ngay.
4. **Anh chọn một ứng viên** → dựng đủ năm pha cho phím 1 đến 7 → hai giám khảo mù độc lập ≥ 8,5 ở bản dựng chơi, không cờ URL. Ba lượt không lên điểm thì dừng và bàn với ChatGPT trước lượt thứ tư.
5. Ba mảnh dùng chung dùng lại cho các hệ sau (Water, Thunder…) và cho Metal nếu anh muốn Metal cũng lấp lánh hơn.

## 7. Câu hỏi cho anh

1. Anh thích những khung nào trên bảng (số)? Một hướng, hay trộn (ví dụ lửa A, tia lửa B, hào quang C)?
2. Độ lấp lánh ở camera chơi: tiết chế (1 sao lớn + 2 nhỏ mỗi đòn) hay dày hơn (như khung 5)?
3. Vòng hào quang: ở mọi đòn, hay chỉ đòn lớn, kiếm dẫn đầu và tuyệt kỹ?
4. Giữ lửa cam đỏ thật (D54), hay cho một chút màu nhấn ngọc bích kiểu "dị hỏa" ở tuyệt kỹ (gợi ý của Gemini)?
5. Ở cận cảnh, có cho hơi nóng méo hình quanh 4–8 hiệu ứng gần nhất không (ở camera chơi luôn tắt)?
6. Với hướng A: lửa nên nằm theo nhát chém (nét bay ngang theo kiếm), hay vẫn đứng lên như ngọn lửa trên đất?
