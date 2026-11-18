# Ngân sách hiệu năng Tu Tiên · thử tải 100 quái + map một đường + Ngũ Lôi (13/11/2026)

**Anh hỏi:** "100 quái cùng lúc trên màn hình, với đồ hoạ map đẹp, kỹ năng đẹp, thì liệu nó sẽ khiến fps của game như nào". Máy trung bình là máy anh (Mac mini M4); máy yếu vừa chưa có máy thật nên suy từ số đo công khai; máy cao chưa định nghĩa.

**Trả lời ngắn:**
- Trên máy anh, cảnh nặng nhất (100 quái + map + đỉnh Ngũ Lôi) ở 1920×1080 tốn **11 ms GPU trung vị, 18 ms ở p95**. Trung bình vẫn 60 khung/s; đỉnh tia thì rớt khung. Ở 1280×720 là 6 / 11 ms.
- CPU không phải nút cổ chai: p95 ≤ 2,2 ms mọi trường hợp.
- Máy yếu vừa (lớp Apple M1 hoặc Intel Iris Xe) **chưa giữ được 60 khung/s** với cảnh này dù đã hạ 720p. Cần ba việc ở mục 5 trước.
- Ba chi phí lớn nhất: chi phí cố định theo điểm ảnh (nền đất, ánh sáng, chuỗi hậu kỳ), lớp cộng sáng của Ngũ Lôi lúc đỉnh, và tam giác của bầy quái (mỗi con ~5 800, vẽ hai lần vì bản đồ bóng, gấp 2–6 lần ngân sách `TT_BUDGETS`).
- **Vòng 2 (giữ nguyên hình, mục 10):** nạp sẵn bỏ cú khựng 480 ms ở lần tung đầu (còn 45–55 ms); KTX2 giữ hình như PNG gốc (77,7 dB) mà bộ nhớ atlas Ngũ Lôi giảm 4 lần; chi phí lớn nhất trong scene là **ánh sáng của đất** (1,1 ms ở 1080p); lưới vừa khít cho thẻ hiệu ứng **không lợi** trên máy anh; LOD bầy lợi 9–14 % thời gian scene nhưng đổi hình ở cự ly gần.
- **Cách đo vòng 1 bi quan:** đồng bộ GPU sau mỗi khung làm GPU nghỉ và hạ xung, nên số "GPU" ở mục 2–3 cao hơn thực tế. Số đáng tin cho trải nghiệm là vòng rAF thật (khung trung vị 7,2–9,6 ms ở 1080p, mục 2) và các phép A/B của vòng 2.

## 1. Cảnh thử và cách đo

**Cảnh** (`games/.wt-ic-lab-all/stress.html`, `src/lab/stress.ts`; không đổi `skills-main.ts` hay `five-thunder.ts`):
- Bầy của lab ở chế độ đi (86 thú + Thú Vương) và 13 thú đi dọc đường: **100 quái sống**. Trên màn thấy 27–34 con ở góc sau lưng và nghiêng, 80–86 con ở góc trên.
- Map một đường (`MAP1_WIDE.md` §13): dải đất 6 m từ z −46 vào mép Kết Giới z −9, hai gờ đá, **200 vật trang trí instanced** (9 loại, đá, bụi, cỏ, đèn, cây; mượn kit pine-river của Dragonhold, 325 000 tam giác, 9 draw call).
- Ngũ Lôi (lab phím G, `five-thunder.ts` đang có, vòng 32–33) tung vào bầy; bloom và tone mapping là của game (`createRenderer`, `applyLook`, mức High).

**Đo** (`scripts/visual/scenarios/lab-perf-stress.mjs`, chạy qua `.local/bin/heavy.sh --perf`, Chrome headless trên **ANGLE Metal, Apple M4**, không phải phần mềm):
- Mỗi khung qua `__lab.perf(1)`: CPU = thời gian JS của `frame()`; tổng = tới khi `readPixels` 1 điểm ảnh trả về (GPU đã vẽ xong); **GPU ≈ tổng − CPU**. Số này hơi bi quan (gồm cả độ trễ IPC của Chrome, ~0,2–0,5 ms) vì khung không chồng lên nhau.
- `EXT_disjoint_timer_query_webgl2` không có trên ANGLE/Metal (macOS), nên không dùng.
- Đối chứng: vòng rAF thật, bỏ giới hạn khung (`--disable-gpu-vsync --disable-frame-rate-limit`), tung Ngũ Lôi mỗi 6 s.
- Hai độ phân giải, hai DPR (1 và 0,67 = render scale), bốn góc (Alt+1..4: top, behind, behind25, side), năm trường hợp: nền, chỉ quái, chỉ map, đỉnh Ngũ Lôi (1,0–3,6 s sau khi tung), tất cả. 120 khung mỗi ô; 156 khung với Ngũ Lôi.

Số liệu: `typing-game-review/captures/tu-tien/perf-stress/` (`grid-1920.json`, `grid-1280.json`, `cuts-1920.json`, `live-1920.json`, `tables.md` đủ 80 ô). Cho anh xem: `owner-review/2026-11-13/tu-tien/perf-stress/` (`perf-stress-gpu.png`, `perf-stress-scene-1280x720.mp4`, ảnh đỉnh).

## 2. Bảng đo (máy anh, góc xấu nhất mỗi ô, ms)

| Khung | Trường hợp | GPU trung vị | GPU p95 | CPU p95 | Draw call | Tam giác |
|---|---|---|---|---|---|---|
| 1920×1080 | nền (đất, sân, hậu kỳ) | 5,7 | 7,6 | 0,7 | 30 | 0 |
| 1920×1080 | chỉ quái (100) | 8,0 | 13,2 | 1,1 | 50 | 1,15 triệu |
| 1920×1080 | chỉ map (200 vật) | 6,4 | 12,3 | 0,9 | 41 | 0,32 triệu |
| 1920×1080 | đỉnh Ngũ Lôi | 9,2 | 12,8 | 1,0 | 52 | ~0 |
| 1920×1080 | **tất cả** | **11,0** | **17,8** | 1,9 | 85 | 1,47 triệu |
| 1920×1080, scale 0,67 | tất cả | 6,0 | 10,7 | 1,1 | 85 | 1,47 triệu |
| 1280×720 | nền | 2,7 | 3,4 | 0,6 | 30 | 0 |
| 1280×720 | **tất cả** | **6,0** | **11,3** | 1,2 | 85 | 1,47 triệu |
| 1280×720, scale 0,67 | tất cả | 4,4 | 9,1 | 2,2 | 85 | 1,47 triệu |

**Vòng thật, bỏ giới hạn khung** (1920×1080, DPR 1, tung Ngũ Lôi mỗi 6 s, 8 s mỗi góc):

| Góc | Khung/s trung bình | Khoảng khung trung vị | p95 | Khung > 16,7 ms |
|---|---|---|---|---|
| top | 126 | 7,2 | 11,5 | 12 / 1 008 |
| behind | 103 | 8,2 | 20,2 | 100 / 824 |
| behind25 | 95 | 9,6 | 19,1 | 78 / 763 |
| side | 122 | 7,5 | 14,1 | 2 / 974 |

**Khựng lần đầu:** khung đầu mỗi lần tung Ngũ Lôi kéo dài 200–450 ms (nạp texture và biên dịch shader lần đầu). Lab đã đẩy 1,9 GB texture lên GPU (mọi atlas phím 8, 9 và các hệ), 181 texture còn giữ. Đây là việc riêng, không tính vào p95 ở trên vì p95 bỏ qua một khung.

## 3. Thử cắt nhanh (1920×1080, góc sau lưng, "tất cả" trong cửa sổ đỉnh Ngũ Lôi)

| Thử | GPU trung vị | GPU p95 | Tiết kiệm (trung vị) |
|---|---|---|---|
| High như đo | 6,5 | 9,6 | — |
| Tắt bloom (q=medium) | 6,2 | 10,9 | 0,3 ms (5 %) |
| Render scale 0,67 | 4,2 | 6,1 | **2,3 ms (35 %)** |
| Tắt lớp hiệu ứng màn hình | 6,1 | 13,6 | 0,4 ms |
| Không có bầy (giá của 100 quái) | 5,0 | 12,6 | **1,5 ms** |
| Low: không bloom + scale 0,67 | 3,7 | 6,3 | **2,8 ms (43 %)** |

p95 trong các lượt này dao động mạnh giữa các lần chạy (máy còn chạy việc khác); trung vị ổn định hơn.

## 4. Máy yếu vừa: suy từ số đo công khai

Chưa có máy thật. Hệ số lấy từ 3DMark Wild Life Extreme (GPU thuần, đa nền tảng):

| GPU giả định | Điểm | So với M4 10 nhân (~9 140) | Nguồn | Đã kiểm |
|---|---|---|---|---|
| Apple M4 10 nhân (máy anh) | ~9 140 trung bình (8 457–9 636) | 1 | Notebookcheck, trang GPU M4 10 nhân | Qua kết quả tìm kiếm; trang chặn tải trực tiếp (403) |
| Apple M1 8 nhân | ~4 700–4 970 | **÷ 1,9** | Notebookcheck (so Iris Xe), nanoreview | Như trên |
| Intel Iris Xe 96EU (laptop 2020–2023) | ~3 100–3 550 | **÷ 2,6–2,9**; dùng **÷ 3** vì trên Windows Chrome chạy ANGLE D3D11 và laptop hay tụt xung | Notebookcheck (trung bình 3 545), nanoreview (3 119); Geekbench GPU 14 437 vs 35 341 (÷ 2,45) | Như trên |

Muốn 60 khung/s (16,7 ms) ở máy đó, chừa 15 % cho CPU và trình duyệt, thì **trên máy anh** cảnh chỉ được tốn:
- lớp M1: 16,7 ÷ 1,9 × 0,85 ≈ **7,5 ms GPU**;
- lớp Iris Xe: 16,7 ÷ 3 × 0,85 ≈ **4,7 ms GPU**.

So với số đo: 1280×720 scale 0,67 "tất cả" là 4,4 ms trung vị, 9,1 ms p95. Vậy Iris Xe giữ được trung bình nhưng rớt mạnh lúc đỉnh tia; M1 ở 1280×720 thì vừa trung bình (6,0), rớt lúc đỉnh (11,3). **Cần việc ở mục 5 trước khi hứa 60 khung/s cho máy yếu vừa.**

## 5. Ba chi phí lớn nhất và cách cắt không thấy khác

1. **Chi phí cố định theo điểm ảnh** (đất và sân có ánh sáng, sương, chuỗi hậu kỳ): 5,7 ms ở 1080p khi sân trống, 2,7 ms ở 720p, tức ~2,7 ms mỗi megapixel. Bằng nửa khung "tất cả".
   - Render scale động (D57 đã có ở High/Ultra) là nút rẻ nhất: 0,67 tiết kiệm 35 % mà vẫn ra 1080p qua phóng lại.
   - Bloom không phải thủ phạm (0,3 ms). Giữ ở mọi mức trừ Thấp.
   - Việc cần đo tiếp: tách nền thành đất và hậu kỳ. Nếu đất đắt: nướng ánh sáng và bóng vào texture, shader đất đơn giản hơn.
2. **Ngũ Lôi lúc đỉnh** (nhiều lớp cộng sáng lớn chồng lên nhau, cột sáng toàn màn): +3,5 ms trung vị, +5 ms p95 so với nền ở 1080p; là nguyên nhân chính của các khung > 16,7 ms.
   - Trần lớp chồng theo `VFX_STANDARD.md` §3.7 (trung bình ≤ 3, đỉnh ≤ 8 trong ≤ 10 khung; Thấp ≤ 2 / ≤ 4).
   - Vẽ lớp cộng sáng vào bộ đệm nửa độ phân giải rồi ghép lại.
   - Ở Thấp: ít cột sáng cùng lúc hơn, chớp toàn màn ngắn hơn. Chưa thử vì phiên khác đang chỉnh Ngũ Lôi.
3. **Tam giác của bầy**: 1,15 triệu tam giác mỗi khung cho 100 quái: mỗi con ~5 800, vẽ hai lần (bản đồ bóng và màn), trong khi `TT_BUDGETS.lodTris` là 1 000 / 1 800 / 3 000. Bỏ bầy tiết kiệm 1,5 ms; nếu theo đúng ngân sách LOD thì bầy chỉ còn 0,2–0,6 triệu tam giác.
   - Quái đã instanced; thêm LOD theo ngân sách, ảnh phẳng (impostor) cho quái xa, hoạt ảnh nướng vào texture (VAT) đã có trong kế hoạch bench.
   - Ước tính tiết kiệm ~1 ms; chưa đo, cần mesh LOD.

Thêm:
- **Map:** 200 vật instanced chỉ thêm 0,7 ms trung vị ở 1080p. Map đẹp với vật instanced không đáng lo; cây ở xa có thể dùng LOD.
- **Khựng lần đầu:** nạp sẵn (prewarm) texture và shader của kỹ năng khi vào trận, và texture KTX2 nén (đã có cho flipbook lab) để giảm 1,9 GB.

## 6. Ngân sách theo hệ thống (GPU, ms, đo trên máy anh)

| Hệ thống | Vừa (máy anh, 1920×1080) | Thấp (cho máy yếu vừa, quy về máy anh) | Đo hiện nay, trung vị phần thêm so với nền (1080p / 720p scale 0,67) |
|---|---|---|---|
| Nền: đất, ánh sáng, hậu kỳ | ≤ 5,5 | ≤ 2,0 | 5,7 / 2,0 |
| Map: vật trang trí | ≤ 1,0 | ≤ 0,4 | 0,7 / 0,5 |
| 100 quái | ≤ 2,0 | ≤ 0,8 | 2,3 / 1,7 |
| Kỹ năng lúc đỉnh (phần thêm) | ≤ 4,0 | ≤ 1,3 | 3,5 (p95 5,2) / 1,3 (p95 2,0) |
| Chữ, số sát thương, UI 3D | ≤ 0,5 | ≤ 0,2 | chưa đo riêng |
| Dự trữ | 1,0 | — | — |
| **Tổng GPU p95** | **≤ 14** | **≤ 4,7** (p95 ≤ 6) | 17,8 / 9,1 |
| CPU p95 (canon `TT_BUDGETS`) | ≤ 6 | ≤ 6 | ≤ 2,2 |
| Draw call | ≤ 150 | ≤ 80 | 85 |

## 7. Thứ tự: giữ hình trước, hạ hình sau cùng

Anh (13/11): "không phải cứ giảm chất lượng hình ảnh … là tối ưu". Thứ tự làm và thứ tự tự hạ khi rớt khung:

1. **Không đổi hình, đã chứng minh:** nạp sẵn shader và texture khi vào trận; atlas KTX2 (đã dùng ở lab); bỏ pass thừa nếu có (ScreenPass đo 0 ms nên giữ).
2. **Không đổi hình, cần làm rồi chứng minh:** gộp các lớp tĩnh chồng nhau của kỹ năng thành một lần vẽ (mục 10.4); nướng phần ánh sáng tĩnh của đất vào texture và giữ đèn động, bóng động (mục 10.3).
3. **Đổi hình rất nhỏ, chỉ khi xa:** LOD cho quái cao dưới ~80 px trên màn (mục 10.2); cây và đá xa dùng LOD.
4. **Đổi hình, chỉ là mức Thấp cuối cùng cho máy yếu:** render scale động 0,67–0,85; tắt bloom; giảm số hạt và lớp chồng; quái ≤ 1 000 tam giác và ảnh phẳng khi xa.

| | **Thấp** (máy yếu vừa: M1, Iris Xe) | **Vừa** (máy anh, chuẩn) | **Cao** |
|---|---|---|---|
| Hình | hạ theo bước 4 khi bước 1–3 chưa đủ | giữ nguyên hình hiện nay (bước 1–3) | Để ngỏ: anh chưa định nghĩa máy cao |
| Khung ra | 1280×720 | 1920×1080, render scale 1 | |
| Bloom, hiệu ứng màn hình | tắt (cuối cùng) | bật | |
| Tam giác mỗi quái | ≤ 1 000, ảnh phẳng khi xa | gốc ở gần, LOD khi < ~80 px | |
| Lớp cộng sáng chồng | trung bình ≤ 2, đỉnh ≤ 4 | ≤ 3, đỉnh ≤ 8 (`VFX_STANDARD` §3.7) | |

## 8. Luật tự hạ chất lượng khi rớt khung

- Đo khoảng khung rAF, cửa sổ trượt 1 s; ngưỡng = 16,7 ms × 1,1.
- **Bước 1, chỉ ở mức Thấp, không tải lại trang:** p90 vượt ngưỡng 0,5 s liền thì hạ render scale 0,1, tới sàn 0,67. Hồi lại 0,05 mỗi 2 s khi p90 < 0,7 × ngưỡng (có trễ, tránh nhấp nháy). Ở mức Vừa không tự hạ độ phân giải: hình là ưu tiên, các khung vượt chỉ xảy ra vài khung lúc đỉnh kỹ năng.
- **Bước 2:** đã ở sàn mà vẫn vượt 3 s thì bật chế độ nhẹ trong trận: trần lớp cộng sáng của mức dưới, giảm hạt, kéo gần khoảng cách ảnh phẳng cho quái.
- **Bước 3:** không tự đổi mức giữa trận, vì đổi mức cần tải lại trang (`LESSONS_FROM_THREE_GAMES.md` §8). Sau trận gợi ý người chơi chọn mức thấp hơn trong Settings.
- Kỹ năng lớn được phép vượt tối đa 10 khung (khớp trần đỉnh của §3.7) mà không kích bước 2.

## 9. Thứ tự tối ưu nên làm trước (sau vòng 2)

1. **Nạp sẵn khi vào trận** (đã chứng minh: khựng 480 → 45–55 ms, hình như cũ). Tìm nốt phần còn khựng 45–55 ms (thứ Ngũ Lôi tạo lúc tung).
2. **Texture đất — đã làm ở vòng 4** (`look.ts`, mục 10.7; vòng 3, mục 11): gộp AO và roughness vào một texture (giống hệt từng bit, −0,3 ms) rồi nén màu, normal và map gộp sang KTX2 UASTC (56–58 dB, −0,5–0,7 ms). Nướng ánh sáng **không** lợi: phần đắt của đất là phản xạ trời qua normal map và bóng, không nướng được mà giữ hình.
3. **Lớp trận pháp của Ngũ Lôi** (6 thẻ, 1,3 ms lúc tia rơi): tỉa shader không lợi; gộp thành một shader còn để ngỏ (mục 11.2).
4. **LOD bầy theo cỡ trên màn, từng con:** chỉ con cao < ~80 px; dùng bộ giản lược giữ đường nối uv (meshoptimizer) để bỏ vệt sáng tối trên thân như ảnh hiệu ở mục 10.2.
5. **KTX2 cho mọi atlas và texture model** (hình như PNG, bộ nhớ ÷ 4).
6. Bỏ hướng "lưới vừa khít cho thẻ": đo 0–0,4 % trên M4. Chỉ xem lại khi có máy yếu thật mà số đo cho thấy tô màu thẻ là nút thắt.
7. Đo lại sau mỗi bước bằng `lab-perf-stress.mjs` (PART=opt); khi có máy yếu thật, đo trên đó.

## 10. Vòng 2: tối ưu giữ nguyên hình (13/11, chiều)

**Cách chứng minh và đo** (`src/lab/stress-opt.ts`, `PART=opt`; mọi tối ưu là công tắc lúc chạy trong cảnh thử, không sửa tệp lab dùng chung hay Ngũ Lôi):
- **Hình:** vẽ thẳng scene vào render target số thực (`renderer.render`, không gọi `frame()`, nên không lớp nào sinh thêm, không gì trôi). Hai lần vẽ cùng trạng thái giống hệt 100 % từng điểm ảnh, nên mọi khác biệt là do thay đổi đang thử. Bản vẽ qua `frame()` thì không dùng được: Ngũ Lôi sinh thẻ mới ở mỗi lần vẽ và vài lớp ánh sáng dịu dần theo lần vẽ.
- **Chi phí:** A/B xen kẽ 7 vòng, mỗi vòng 40 lần vẽ liền nhau và một lần đồng bộ, lấy trung vị. Phép A/A lệch 0,6 %. Chi phí hậu kỳ đo trên cả khung, cùng cách (5 vòng × 60 khung).
- Ảnh trước/sau: `owner-review/2026-11-13/tu-tien/perf-stress/round2-compare.jpg`; số: `captures/tu-tien/perf-stress/opt/opt.json`.

| Việc | Trước → sau (1920×1080, góc sau lưng) | Hình | Kết luận |
|---|---|---|---|
| 10.1 Lưới vừa khít cho thẻ (16×16 ô theo phần có điểm sáng của mọi khung, nới 1 ô) | scene 3,3–7,1 ms: tiết kiệm 0–0,4 % ở 5 thời điểm của Ngũ Lôi | Giống hệt ở các pool dùng được; 18 pool đọc mẫu ngoài ô (trận pháp, mây, tia B, nổ, vòng…) nên bị loại tự động | **Không lợi trên M4** (GPU kiểu tile bỏ qua phần trong suốt rẻ). Bỏ |
| 10.2 LOD bầy (giản lược, giữ thuộc tính từng con) | 5 800 → 3 200–3 450 tam giác: −0,31 ms (−8,9 % scene); → 2 000–2 300: −0,47 ms (−13,8 %) | 94 % / 93 % điểm ảnh giống hệt; 3,8–5 % điểm ảnh đổi, nhất là bóng đổ trên thân ở con gần (thú cao 34–247 px) | Lợi vừa, **đổi hình ở gần**: chỉ dùng cho con < ~80 px, bộ giản lược tốt hơn |
| 10.3 Tách nền (sân trống) | scene 1,9 ms: ánh sáng đất 1,1 ms (58 %), đất cả thảy 1,24 ms, bản đồ bóng 0,16 ms; hậu kỳ (bloom và ghép) 1,3 ms trên cả khung; ScreenPass 0 ms | — | **Đất là chỗ đáng làm nhất** (nướng ánh sáng tĩnh); bloom 1,3 ms: giữ |
| 10.3 Như trên, khi có bầy, map, hiệu ứng | ánh sáng đất 1,08 ms (31 % scene), bóng 0,09 ms, hậu kỳ 0,56 ms | — | như trên |
| 10.5 Atlas KTX2 so với PNG gốc (34 atlas Ngũ Lôi) | cùng thời gian (0 %) | 77,7 dB, sai khác lớn nhất 0,024; 0,006 % điểm ảnh lệch > 2/255 | **Giữ KTX2**: bộ nhớ GPU 235 MB thay vì 940 MB |
| 10.6 Nạp sẵn (biên dịch 184 shader, đẩy 160 texture, nạp atlas Ngũ Lôi; 1,5–1,7 s lúc vào trận) | khung đầu sau khi tung: 480–492 ms → 45–55 ms | Như cũ (chỉ làm sớm việc lần tung sẽ làm) | **Làm ngay** |

**10.4 Ngũ Lôi, chỉ đề xuất** (đo lớp từng lớp bằng cách ẩn, ở 1,2 / 1,8 / 2,5 / 3,4 s sau khi tung; tổng các lớp 2,0 / 2,6 / 4,1 / 3,7 ms scene ở 1080p):
- **Chồng lớp:** trung bình 2,6–3,0 lớp trên mỗi điểm ảnh có hiệu ứng, đỉnh 12–17 lớp; 60–80 nghìn điểm ảnh (3–4 % màn) có ≥ 9 lớp, vượt trần "đỉnh ≤ 8" của `VFX_STANDARD.md` §3.7.
- **Lớp phủ rộng nhất:** `formationShade` (2 thẻ, 0,9 triệu điểm ảnh, ~45 % màn), `formationRim` (3 thẻ, 0,6–0,7 triệu), `formation` (1 thẻ, 0,54 triệu), `dim` (22 thẻ màu đặc, 0,95 triệu), `cloud` (0,64 triệu). Ba lớp trận pháp tốn 0,6–1,1 ms cộng lại.
- **Đắt theo số lượng:** `motes` (68–92 thẻ, 0,3–0,45 ms), `embers` (78–179 thẻ, 0,2–0,5 ms), `smoke` (6–18, 0,1–0,6 ms), `scarHot` (0,6 ms ở 3,4 s).
- **Đề xuất không đổi hình:**
  1. Gộp `formationShade` + `formation` + `formationRim` thành một thẻ, một shader đọc ba texture theo đúng thứ tự trộn hiện nay (nhân tối rồi cộng sáng). Cùng phép tính ở mỗi điểm ảnh, một lần tô thay ba: ước tính tiết kiệm 0,4–0,7 ms.
  2. Thay 22 thẻ `dim` màu đặc bằng một tham số làm tối trong ScreenPass, nếu chúng chỉ là một lớp tối phủ màn.
  3. Gộp `motes` và `embers` (cùng kiểu hạt cộng sáng) vào một pool: ít draw call hơn; thời gian tô không đổi.
  4. Giữ đỉnh ≤ 8 lớp bằng cách lệch thời điểm các lớp sáng lớn nhất (cột, nổ, vết cháy), không bỏ lớp.

**Còn bao nhiêu ms so với ngân sách** (máy anh, 1080p, 60 khung/s = 16,7 ms):
- Vòng thật hiện nay: khung trung vị 7,2–9,6 ms, còn **7–9,5 ms** trung vị. p95 ở góc sau lưng 19–20 ms, vượt ~3,5 ms trong vài khung lúc đỉnh Ngũ Lôi.
- Các việc giữ hình ở mục 9 (đất 1,1 ms, gộp trận pháp 0,4–0,7 ms, LOD con xa ~0,3 ms) cộng ~2 ms. Đủ kéo trung vị xuống ~6–7,5 ms; p95 lúc đỉnh còn vượt ~1–1,5 ms, cần đề xuất 10.4.4.
- Máy yếu vừa (hệ số mục 4, áp lên vòng thật): lớp M1 ~14–18 ms trung vị ở 1080p, vừa chạm 60 khung/s, nên cần bước 1–3 rồi mới tới bước 4. Iris Xe ~22–29 ms: cần 720p và bước 4.

**10.7 Vòng 4 (15/11): texture đất mới trong `look.ts`.** `buildField` dựng đất bằng màu và normal cùng **AO + roughness gộp một texture** (`lookdev/<id>/ORM.png`), rồi đổi sang **KTX2** (`Color`, `NormalGL`, `ORM` `.uastc.ktx2`) khi nạp xong. Nếu KTX2 lỗi thì giữ bản gộp. `?groundTex=jpg|orm|ktx2` chọn bộ, mặc định ktx2; `useGroundTextures()` đổi lúc chạy. `pbr()` không đổi (trang lookdev, vật khác). Số: `captures/tu-tien/perf-stress/r4/` (`r4-proof.json`, `r4.json`); ảnh: `owner-review/2026-11-13/tu-tien/perf-stress/round4-ground.jpg`.

| | Góc 1 (top) | Góc 2b (behind 25°) |
|---|---|---|
| Gộp AO + roughness so 4 JPG (vẽ thẳng) | **giống hệt 100 %** | **giống hệt 100 %** |
| KTX2 so 4 JPG (vẽ thẳng) | 53,7 dB, 1,2 % điểm ảnh lệch > 2/255 | 55,8 dB, 0,7 % |
| KTX2 so 4 JPG (cả khung, có hậu kỳ) | 48,0 dB | 51,0 dB |
| Scene, A/B xen kẽ: JPG → gộp → KTX2 | 3,05 → (−7 %) → 2,63 ms (−14 %) | 4,09 → (−9 %) → 3,21 ms (−21 %) |
| Cả khung, A/B | 4,74 → 4,35 ms (−8 %) | 5,75 → 4,90 ms (−15 %) |

**Vòng thật, máy rảnh** (Codex không chạy, không trình duyệt khác; macOS đang lập chỉ mục ở nền; 1920×1080, bỏ giới hạn khung, Ngũ Lôi mỗi 6 s). Mỗi lượt là một trang mới, 8 s; JPG và KTX2 chạy xen kẽ; đối chứng là các lượt JPG với nhau:

| Góc | JPG (4 lượt) p50 / p95 / trung bình | KTX2 (2 lượt) p50 / p95 / trung bình | Độ lệch giữa các lượt JPG (p95) |
|---|---|---|---|
| 1 (top) | 7,3–7,5 / 10,6–12,6 / 7,95–8,21 ms | 7,0–7,3 / 8,7–10,9 / 7,76–8,06 ms | 2,0 ms |
| 2b | 8,4–8,7 / 12,3–14,2 / 9,44–11,03 ms | 8,3 / 12,4 / 9,03–9,05 ms | 1,9 ms |

- Trung vị và trung bình của KTX2 thấp hơn mọi lượt JPG ở góc 2b (khung trung bình 9,0 so với 9,4–11,0 ms).
- p95 cũng thấp hơn ở góc 1 (trung bình 9,8 so với 11,6 ms), nhưng chênh lệch nằm trong độ lệch giữa các lượt JPG (~2 ms). Nên nói được: **trung bình nhanh hơn, p95 không xấu đi; chưa đủ chắc để nói p95 tốt lên.**
- Bộ nhớ GPU: hai bộ đất từ 8 texture RGBA8 1024² (~43 MB có mip) xuống 6 texture ASTC 4×4 (~8 MB).

## 11. Vòng 3: nướng ánh sáng đất, lớp trận pháp (15/11)

Cách đo như vòng 2 (vẽ thẳng, A/B xen kẽ; phép A/A giống hệt 100 %). Số: `captures/tu-tien/perf-stress/r3/r3.json`; ảnh: `owner-review/2026-11-13/tu-tien/perf-stress/round3-ground.jpg`. Mã: `src/lab/ground-bake.ts`, `src/lab/stress-opt.ts` (công tắc trong cảnh thử, không đổi đất của lab).

**11.1 Đất.** Đất là `MeshStandardMaterial` với màu, normal, roughness, AO (JPG 1024², lặp 6× và 24×), chịu đèn bán cầu, đèn chính, đèn viền, IBL, mặt trời có bóng và 3 đèn điểm. Đo từng phần: normal map 0,39 ms, nhận bóng 0,19 ms, phần còn lại là đèn và PBR.

| Cách | Sân trống: trước → sau (ms scene) | Có bầy, map, hiệu ứng | Hình | Kết luận |
|---|---|---|---|---|
| Nướng phần khuếch tán tĩnh (bán cầu, đèn chính, đèn viền, IBL khuếch tán; bằng chính vật liệu đất vẽ trong không gian UV), giữ mặt trời, đèn điểm, phản xạ | 2,15 → 2,61 (chậm hơn) | 4,26 → 4,23 (0 %) | 33–46 dB | **Bỏ**: phần nướng được vốn rẻ (vài phép tính), còn rẻ hơn một lần đọc texture; bản nướng half-float còn chậm hơn 0,9 ms |
| Nướng lite (Lambert: khuếch tán tĩnh + mặt trời nướng × bóng thật + đèn điểm, bỏ phản xạ) | 2,20 → 1,71 (−22 %) | 3,63 → 2,91 (−20 %) | 22–24 dB: **mất ánh phản xạ trời**, chiếm ~40 % ánh sáng của đất | Chỉ cho mức Thấp |
| AO + roughness trong một texture (R = AO, G = roughness) | 1,95 → 1,69 (−0,27 ms) | 3,47 → 3,14 (−0,33 ms) | **Giống hệt từng bit** | **Làm** |
| Màu, normal, AO+roughness nén KTX2 UASTC (ASTC 4×4 trên M4) | 1,96 → 1,30 (−0,67 ms) | 3,31 → 2,79 (−0,52 ms) | 56–58 dB (mắt không phân biệt) | **Làm** (cùng việc gộp ở trên) |

Tệp đã mã hoá: `art-src/lab/models/stress-props/ground/` (PavingStones128, Rock035). Đưa vào game: `look.ts` `pbr()` đọc map gộp và KTX2 thay cho bốn JPG.

**11.2 Lớp trận pháp Ngũ Lôi.** Ba lớp là 6 thẻ (bóng mực, viền tối, bóng tiếp xúc, trận, vòng chữ, vòng nhỏ), cao 1,5–3 cm so với đất. Lúc tia rơi chúng tốn **1,32 ms** (vòng chữ 0,73, bóng 0,57), tất cả là phần tô từng điểm ảnh.
- Phép trộn của pool là premultiplied "over", có tính kết hợp, nên gộp sáu thẻ vào một shader **về toán là đúng thứ tự trộn**.
- Đã thử trước cách rẻ hơn, giữ y hệt: chỉ tính noise khi có nhánh dùng và đọc texture một lần cho ảnh tĩnh một khung. Hình giống hệt từng bit nhưng **không nhanh hơn** (−0,08 đến +0,27 ms, trong nhiễu). Trình biên dịch GPU đã tự bỏ phần đó, nên đã gỡ khỏi `five-thunder.ts` (tệp trở lại như trước vòng 3).
- Phần còn lại là chi phí cố định mỗi lần tô (dựng tam giác, nội suy, trộn) nhân 6. Gộp một shader sẽ cắt phần đó: ước tính tiết kiệm 0,6–0,9 ms. Nhưng phải chép lại phần đỉnh (đặt phẳng, nghiêng theo góc nhìn) và phần tô của pool cho ba texture trong `five-thunder.ts`, đúng lúc tệp đang được phiên khác chỉnh. **Để ngỏ**, làm khi Ngũ Lôi đã chốt hình.

## Nguồn

- [Notebookcheck: Apple M4 10-core GPU](https://www.notebookcheck.net/Apple-M4-10-core-GPU-Benchmarks-and-Specs.835807.0.html)
- [Notebookcheck: Iris Xe G7 96EUs vs M1 8-Core GPU](https://www.notebookcheck.net/Iris-Xe-G7-96EUs-vs-M1-8-Core-GPU_10364_10552.247598.0.html)
- [nanoreview: Iris Xe G7 96EU vs Apple M1 GPU 8-core](https://nanoreview.net/en/gpu-compare/intel-iris-xe-graphics-g7-96eu-vs-apple-m1-gpu-8-core)
- [Geekbench 6 GPU: Mac16,12 vs Dell Inspiron 16 5630](https://browser.geekbench.com/v6/compute/4758217)
