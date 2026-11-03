# Kiếm khó nhìn khi thi triển chiêu: chẩn đoán (03/11/2026)

**Trạng thái:** chẩn đoán, chưa sửa mã game. Đo trên đúng bản lab anh đang thử: `games/immortality-cultivation` `9cb7bcd` (Sword × Fire vòng 3, cổng 3161), xuất bằng `git archive` ra thư mục riêng, chạy trên server riêng (không HMR), đồng hồ cố định 60 Hz. Hào quang kiếm (`SWORD_AURA.md`) đang được dựng ở checkout chính, **chưa có** trong bản đo này. Mọi thí nghiệm chỉ đổi trong trang (JavaScript trong tab của tôi), không sửa mã.

**Phản biện độc lập (§9):** nguyên nhân 1 đứng vững; nguyên nhân 2 đúng cơ chế nhưng không phải nguyên nhân riêng; nguyên nhân 3 đúng mức độ nhưng sai cơ chế, và cổng C1 đo sai chỗ. Hai đoạn "sửa mô phỏng" trong video không nên gửi như hiện tại.

**Lời anh (03/11, tối, thử lab trên Mac):** "tôi thấy đang gặp 1 vấn đề, là khó nhìn thấy được hình ảnh kiếm mỗi khi thi triển kỹ năng, tôi không rõ là do tốc độ kiếm nhanh quá, hay là do hình ảnh kiếm kém chất lượng bị mờ".

**Để xem** (ngoài Git, chỉ cho anh):
- Video: `games/immortality-cultivation/tmp/sword-readability/owner/sword-speed-compare.mp4`: phím 1 và phím 7 ở tốc độ thật, rồi 0,25×, rồi với hai cách sửa mô phỏng trong trang; chú thích tiếng Anh.
- Tấm cắt: `games/immortality-cultivation/tmp/sword-readability/owner/sword-crops.jpg`: thanh kiếm đúng cỡ trên màn, từng khung, qua phím 1 và một kiếm chủ phím 7, dưới mỗi ô là dài và tốc độ.
- Khung tham chiếu: `games/immortality-cultivation/tmp/sword-readability/owner/reference-frames.jpg` (khung từ video chính thức, chỉ để anh xem, không đưa vào công cụ AI nào).

## Quyết định của anh (03/11/2026, tối)

- **T3: có.** Anh trả lời "Có, cho khựng":
  - Thanh đầu phím 1 treo một nhịp, mũi chỉ vào đích, rồi mới lao.
  - Nhát trúng đầu lùi khoảng 0,2 s, từ +6 lên khoảng +18 khung.
  - Đây là đổi luật lối chơi (canon §12.1). Lượt sửa phải cập nhật canon, `src/content` và golden hash có chủ đích (`pnpm ic:golden:update`), rồi ghi lý do.
  - Cùng tinh thần cho phím 0 và phím 2 nếu số đo cho thấy cần, nhưng phải đo và báo trước khi đổi.
- **Làm sau khi hào quang kiếm vào**, vì cùng tệp (`sword-skills.ts`, `myriad-swords.ts`):
  - T1, T2, T4 như §6, với ngưỡng T4 chỉnh theo §9;
  - C1, C2 đo bằng ΔE trong ảnh cuối có VFX, theo §9;
  - R1: khử răng cưa rẻ ở High.
- **Lab:** vẫn đánh tức thì (D58). R2 (sàn độ phân giải khi ra chiêu) để sau, đo trên M4 trước.
- **Video gửi anh:** chỉ phần tốc độ thật và 0,25× (`owner/sword-speed-real-and-slow.mp4`). Phần "sửa mô phỏng" bị cắt theo §9.

## 0. Trả lời câu hỏi của anh

**Cả hai, nhưng không ngang nhau.** Nguyên nhân lớn nhất là **thời gian**: ở phím 0, 1 và 2 không có khung bay nào mà thanh kiếm vừa dài ≥ 40 px vừa chạy chậm hơn 12 px/khung. Phím 1 bay đúng 6 khung (0,1 s) với 42 px/khung (p90 58), ngắn hơn thời gian mắt kịp nhảy tới một vật mới (~0,2 s). Ở cận cảnh (phím Z) tốc độ lên 128 px/khung và kiếm ra khỏi khung hình sau 4 khung. Thanh đầu tiên còn đang lớn dần từ 5 lên 64 px **trong lúc bay**, nên chưa bao giờ hiện nguyên hình trước khi trúng.

Phần "mờ, kém chất lượng" **có thật, nhưng không nằm ở model hay ảnh kiếm**: lưới đủ, LOD và impostor được lấy mẫu đúng (~1 texel/px). Nó nằm ở ba chỗ:
- **Thân lưỡi Fire bị nung tối** (`char` 0,12): sáng gần bằng nền đá (Weber 0,5, Metal 3,2), và vỏ lửa phủ thêm 21–42 % lưỡi khi bay. Anh thử cả `?element=fire`.
- **Mức High không có khử răng cưa nào** (MSAA 0, không FXAA). Trên màn 4K của anh, đo thời gian thật: độ phân giải động vẽ ở tỉ lệ 1,0 trong 54–100 % số khung lúc chiêu chạy (phím 1: 99–100 %), tức vẽ 1080p rồi phóng × 2 (§3.3b). Lưỡi rộng 6 px vì thế vừa răng cưa vừa mềm. Ở Ultra, máy chỉ giữ được 33–41 khung/giây, kiếm còn nhảy gấp đôi.
- **Bloom** làm lưỡi dòng sông phím 7 dày từ 6 lên 9 px, viền nhòe ra.

Metal ở camera chơi, lúc kiếm đứng yên, đọc tốt: dài 77–80 px, Weber 3–4, 99 % điểm ảnh lưỡi thấy rõ. Nên với Metal gần như toàn bộ là tốc độ và thời gian; với Fire là tốc độ cộng độ tương phản.

**Nên sửa trước** (§6):
1. Cho kiếm thời gian trên màn: kiếm chờ cất cánh sớm hơn, nửa sau đường bay chậm lại; một luật "thời gian đọc tối thiểu" có số đo. Mỗi kiếm chủ cần ≥ 12 khung, dài ≥ 40 px, ≤ 12 px/khung trước khi trúng.
2. Trả độ tương phản cho lưỡi Fire, và đưa vỏ lửa ra ngoài viền lưỡi (trùng một phần với hào quang đang dựng).
3. Khử răng cưa rẻ ở High, và một sàn độ phân giải khi chiêu đang chạy, nếu ngân sách cho phép (§3.3b, §6).

## 1. Cách đo

**Bản đo:** `9cb7bcd` xuất bằng `git archive` vào `games/immortality-cultivation/tmp/sword-readability/app/` (node_modules, art-src, public là liên kết tới game), cấu hình Vite riêng (`hmr` tắt, `watch` null, `cacheDir` riêng), cổng 3171. Không chạm server 3161 và thư mục `owner-preview` của anh. Mọi lượt trình duyệt chạy qua `.local/bin/heavy.sh --gpu`; lượt đo thời gian thật qua `--perf`.

**Đầu dò trong trang** (`tmp/sword-readability/tools/probe.js`, chỉ JavaScript trong tab của tôi):
- Vá prototype của các module đã nạp (cùng URL Vite, cùng bản module) để thấy mọi `BladeSet` (kiếm chủ: lưới đủ; kiếm giữa: LOD), mọi `SwordImpostors` (kiếm xa, vòng cổng trời phím 6) và tư thế từng kiếm phím 7 (`MyriadSwordsFx.poseOf`, giữ danh tính từng thanh).
- Mỗi khung, mỗi kiếm: tầng, đốc và mũi chiếu lên màn, dài và rộng (px CSS), độ sâu.
- Tốc độ: tâm kiếm dời bao nhiêu px mỗi khung 60 Hz, chia thành dọc trục và ngang trục. Tốc độ góc trên màn tính bằng độ/khung.
- **Ảnh:** cùng một khung (không trôi thời gian) vẽ lại bốn lần: (a) đủ; (b) tắt kiếm; (c) tắt VFX trừ kiếm; (d) tắt cả hai. Đọc điểm ảnh từ bộ đệm vẽ ngay sau khi vẽ.
  - **Điểm ảnh lưỡi:** trong viên nang quanh trục kiếm, những điểm mà (c) khác (d).
  - **Tương phản:** độ chói tuyến tính của lưỡi (c) so với nền đá dưới nó (d). Weber = (Lưỡi − Nền) / Nền.
  - **Bị VFX phủ:** điểm lưỡi mà dấu của kiếm trong ảnh cuối (a − b) còn chưa tới nửa dấu của nó khi không có VFX (c − d).
  - **Vành 5 px quanh lưỡi:** ánh kiếm tràn ra ngoài viền (bloom).
  - **Răng cưa:** độ nhảy của tín hiệu lưỡi giữa các lát 1 px dọc trục, trên 70 % giữa thanh kiếm.
  - Mỗi lớp VFX (vệt, chớp/tia/sao, lửa, bloom) còn được tắt riêng để biết lớp nào phủ.
- **"Đọc được"** theo đề bài: kiếm dài ≥ 40 px và chạy < 12 px/khung. 12 px/khung là 720 px/s, khoảng 20°/s ở 60 cm trước màn 24–27 inch (~35 px CSS mỗi độ), trong vùng mắt bám theo được. 42 px/khung là ~70°/s.
- **"Khung sống":** từ lúc kiếm hiện tới khung trúng đầu tiên (hoặc tới lúc tắt nếu không trúng). **"Khung bay":** khung sống mà tâm kiếm dời ≥ 4 px, không phải chỉ vì kiếm lớn lên hay thu lại tại chỗ.

**Ma trận đo** (`tmp/sword-readability/data/*.json`):
- Phím 0–7, Metal và Fire, camera chơi và cận cảnh của người chơi (`__lab.zoom(1)`, phím Z), High 1920 × 1080, DPR 1.
- High DPR 2, phím 0, 1, 2, 7, Metal.
- Ultra (DPR 2, MSAA 4), mọi phím, Metal.
- Ba lượt thời gian thật trên màn DPR 2 (High Metal, High Fire, Ultra Fire) để xem độ phân giải động.
- Thí nghiệm trong trang (§2.4, §3): thời gian 0,5× và 0,25×; tắt vệt, chớp, lửa, bloom; MSAA 4 ở High; DPR 2 có và không MSAA; lưới đủ thay LOD và impostor; kiếm × 1,4; thân lưỡi Fire `steel` và `char` 0,4.

Hình học (dài, rộng, tốc độ theo px CSS) không đổi theo DPR hay tầng chất lượng; chỉ số kiếm phím 7 đổi (Ultra 6 + 32 + 80). Bốn lượt DPR 2 ít giá trị (cận cảnh Ultra Metal và Fire, Fire High DPR 2, Fire Ultra) bỏ để đỡ giờ GPU.

Phím 4 (Flowing-Light Step) không vẽ kiếm chiêu nào, nên không có trong bảng. Phím 6 có ảnh cut-in 1,7 s trước khi mưa kiếm rơi; ở cận cảnh, phím 6 và phím 7 tự lùi về toàn sân (`zoom.holdWide`), nên số cận cảnh của hai phím này bằng camera chơi.

## 2. Thời gian và tốc độ

### 2.1 Camera chơi, High, DPR 1

Mỗi dòng là trung vị theo kiếm. Cột "Bay đọc được" là số khung bay đạt ngưỡng đọc, kèm tỉ lệ trên mọi khung bay của tầng đó. "Bị VFX phủ" là trung vị trên khung bay.

**Metal**

| Phím | Tầng | Số kiếm | Khung sống | Khung bay | Bay đọc được | Dài khi bay (px) | Rộng (px) | Tốc độ bay (px/khung, trung vị / p90) | Bị VFX phủ | Weber |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | lưới đủ | 1 | 34 | 18 | 0 (0 %) | 80 | 5,9 | 15 / 19 | 2 % | 3,9 |
| 1 | lưới đủ | 3 | 37 | 6 | 0 (5 %) | 71 | 6,0 | 42 / 58 | 1 % | 3,2 |
| 2 | lưới đủ | 1 | 12 | 12 | 0 (0 %) | 77 | 5,8 | 35 / 60 | 78 % | 3,5 |
| 3 | lưới đủ | 3 | 299 | 17 | 5 (23 %) | 25 | 1,5 | 8 / 18 | 0 % | 3,2 |
| 5 | lưới đủ | 6 | 12 | 8 | 1 (17 %) | 67 | 6,4 | 20 / 33 | 0 % | 1,8 |
| 6 | lưới đủ | 18 | 82 | 13 | 3 (59 %) | 80 | 7,3 | 8 / 122 | 26 % | 2,3 |
| 6 | LOD | 153 | 12 | 11 | 2 (31 %) | 107 | 6,9 | 33 / 165 | 0 % | 3,3 |
| 6 | impostor | 16 | 40 | 21 | 13 (56 %) | 113 | 6,5 | 10 / 36 | 11 % | 10,9 |
| 7 | lưới đủ | 13 | 21 | 8 | 3 (29 %) | 103 | 7,2 | 19 / 35 | 3 % | 8,0 |
| 7 | LOD | 54 | 53 | 36 | 20 (66 %) | 101 | 6,2 | 6 / 30 | 0 % | 10,7 |
| 7 | impostor | 146 | 60 | 40 | 25 (71 %) | 95 | 5,7 | 5 / 25 | 0 % | 8,1 |

**Fire** (cùng hình học, nên khung và tốc độ trùng Metal; khác ở độ phủ và tương phản)

| Phím | Tầng | Bay đọc được | Bị VFX phủ | Weber | Lưỡi / nền (độ chói tuyến tính) |
|---|---|---|---|---|---|
| 0 | lưới đủ | 0 (0 %) | 21 % | 0,9 | 0,17 / 0,09 |
| 1 | lưới đủ | 0 (5 %) | 22 % | 0,5 | 0,14 / 0,10 |
| 2 | lưới đủ | 0 (0 %) | 27 % | 1,2 | 0,25 / 0,09 |
| 3 | lưới đủ | 5 (23 %) | 0 % | 0,5 | 0,14 / 0,10 |
| 5 | lưới đủ | 1 (17 %) | 0 % | −0,3 | 0,07 / 0,10 |
| 6 | lưới đủ | 3 (60 %) | 27 % | 0,6 | 0,12 / 0,07 |
| 7 | lưới đủ | 3 (29 %) | 42 % | 3,6 | 0,17 / 0,04 |
| 7 | LOD | 21 (63 %) | 0 % | 5,5 | 0,21 / 0,03 |
| 7 | impostor | 19 (64 %) | 0 % | 2,4 | 0,10 / 0,03 |

(Phím 5 Fire: lưỡi **tối hơn** nền.)

### 2.2 Cận cảnh của người chơi (Z), High, DPR 1

Kiếm to lên ~2,8 lần, nhưng tốc độ px cũng nhân lên đúng chừng ấy, nên thời gian đọc không tăng.

| Phím | Dài khi bay (px) | Rộng (px) | Tốc độ bay (px/khung, trung vị / p90) | Bay đọc được | Bị VFX phủ (Metal / Fire) |
|---|---|---|---|---|---|
| 0 | 216 | 19,7 | 46 / 56 | 2 / 20 | 5 % / 21 % |
| 1 | 199 | 22,5 | 128 / 138 | 0 / 6 | 4 % / 12 % |
| 2 | 137 | 16,5 | 58 / 162 | 0 / 14 | 92 % / 0 % |
| 5 | 382 | 20,8 | 114 / 161 | 0 / 8 | 0 % / 0 % |

- Ở cận cảnh, đích của phím 1 và phím 5 nằm **ngoài khung**. Thanh đầu phím 1 ra khỏi màn ở khung 5; thanh thứ hai ở khung 36, tức 4 khung sau khi cất cánh.
- Phím 2 ở cận cảnh: 92 % lưỡi Metal bị vạch và chớp của chính nó phủ.

### 2.3 Phím 1 từng thanh (Metal, camera chơi)

| Thanh | Hiện | Chờ sau vai | Bay | Trúng | Sau khi trúng |
|---|---|---|---|---|---|
| 1 | f1, lớn dần 5 → 64 px **trong lúc bay** | không có | f1–f6, 30–60 px/khung, đi ~200 px | f7 | Cắm ở đích f7–f16, bị chớp va chạm phủ 48–83 %; thu lại f17–f26 |
| 2 | f1, lớn tới 77 px trong 7 khung | f7–f31, dài 77 px, Weber 3,2, đứng yên | f32–f37, 35–63 px/khung | f38 | Bị phủ 40–79 % trong 8 khung; mờ đi f48–f57 |
| 3 | f1, lớn tới 80 px | f7–f60 | f61–f66 | f67 | Bị phủ 65–80 % trong 10 khung |

- Kiếm đọc rất rõ **lúc chờ** sau vai, rồi biến mất trong 6 khung.
- Lab đang ở chế độ đánh tức thì (không gõ chữ), nên thanh 1 cất cánh ngay khung phóng. Trong game, khi gõ từ, ba thanh hiện sau vai lúc gõ được 15 %, 45 % và 75 % của từ (`K1_SHOW`). Thanh 1 vì thế chờ được gần cả thời gian gõ (~1 s ở 45 WPM). Bản lab anh thử cho thấy trường hợp xấu nhất của thanh 1.
- **Chuyến bay thì như nhau ở cả hai chế độ**: 6 khung, trúng ở tick canon +6, +36, +66 (§12.1).

### 2.4 Thí nghiệm thời gian (tốc độ trên mỗi khung hiển thị, Metal)

| Phím | Thật (1×) | 0,5× | 0,25× |
|---|---|---|---|
| 0: khung bay, đọc được, tốc độ | 18 khung, 0 đọc được, 15 px/khung | 36, 30 (83 %), 8 | 29, 28 (97 %), 4,5 |
| 1 | 6, 0, 42 | 13, 1, 21 | 25, 16 (47 %), 11 |
| 2 | 12, 0, 35 | 24, 7, 18 | 41, 24 (59 %), 10,5 |
| 7 kiếm chủ trước nhát đầu | 8, 3, 19 | 12, 6, 11 | 8 đọc được / 8, 7,6 |

- **Phím 1 phải chậm khoảng 4 lần thì gần nửa chuyến bay mới đọc được.** Phím 0 chỉ cần chậm 2 lần.
- Clip 0,25× trong video cho thấy cùng thanh kiếm ấy là kiếm thật rõ ràng: viền lưỡi, vòng ngọc, chắn.
- Vậy đúng là **tốc độ, không phải ảnh**: chậm lại thì cùng model ấy đọc ra.

## 3. Chất lượng ảnh

### 3.1 Độ tương phản lưỡi trên nền

- **Metal:** lưỡi sáng ~0,42 trên nền đá ~0,10 (Weber 3–4) ở phím 0, 1, 2. Phím 7 trên nền tối của tuyệt kỹ: Weber 8–11. Đây không phải vấn đề.
- **Fire ở `9cb7bcd`:** lưỡi ở chế độ `furnace`, `char` 0,12 (thân sắt nhân 0,12, cộng một dải nhiệt cam).
  - Phím 1: lưỡi 0,14 trên nền 0,10, Weber 0,49. Tín hiệu của lưỡi trên mỗi px chiều dài chỉ còn 518, so với 853 của Metal (−40 %).
  - Lúc bay, có khung thanh đầu chỉ còn Weber 0,04: một vệt sắt tối trên đá tối.
  - Thí nghiệm trong trang, cùng VFX Fire:

| Thân lưỡi Fire | Weber phím 1 | Phím 0 | Phím 7 kiếm chủ | Phím 7 impostor |
|---|---|---|---|---|
| `char` 0,12 (bản đo) | 0,49 | 0,93 | 3,6 | 2,4 |
| `char` 0,4 (gần giá trị khởi điểm của lưỡi Fire mới ở HEAD, SWORD_AURA Q3) | 1,55 | 2,14 | 5,2 | 4,6 |
| thép Metal dưới VFX Fire (`steel`) | 2,99 | 3,79 | 7,5 | 8,0 |
| Metal | 3,16 | 3,92 | 8,0 | 8,1 |

- **Lưỡi Fire mới ở HEAD** (thép tối mép nóng, `dfc1aa9`) chưa đo ở đây. Ước theo `char` 0,4, nó vẫn chỉ đạt khoảng nửa độ tương phản của Metal. Phần còn lại phải do lớp áo khí và khe mực của hào quang gánh. Phải đo lại bằng chính đầu dò này khi hào quang vào.

### 3.2 VFX phủ lưỡi

| Chỗ | Bị phủ | Lớp nào (tắt riêng từng lớp) |
|---|---|---|
| Fire phím 0, 1 khi bay | 21–23 % | **Vỏ lửa** (flipbook): tắt lửa thì còn 1 %; vệt và chớp không đổi |
| Fire phím 7 kiếm chủ | 25 % cả đời, **42 %** khi bay tới nhát đầu | Vỏ lửa: tắt lửa thì còn 3 % |
| Phím 2 Metal | 78 % (cận cảnh 92 %), 41 % lưỡi bị đẩy lên trắng | Mọi lớp cộng lại: tắt vệt còn 55 %, tắt chớp/tia/sao còn 67 %, tắt bloom còn 50 % |
| Phím 1, 0 sau khi trúng (kiếm cắm ở đích ~10 khung) | 48–83 % | Chớp va chạm, vết chém, tia lửa. Ngoài ra **số sát thương** ("34") nằm đúng chỗ kiếm cắm từ khung thứ 7 sau khi trúng. Số được vẽ chồng lên khung đã xong (`addOverlay`), nên con số % không tính nó; tấm cắt cho thấy nó che gần hết kiếm |
| Fire phím 1, kiếm chờ sau vai | 11–17 % | Quạt lửa lúc phóng sau lưng người |
| Phím 6 kiếm trời | 26 % | Cổng trời, cột sáng |
| Phím 1, 0, 7 Metal khi bay | 1–3 % | Không đáng kể; vệt bắt đầu sau đốc 0,14 m nên không đè lưỡi |

### 3.3 Độ phân giải, khử răng cưa, độ phân giải động

**Đo trên đồng hồ cố định**, độ nhảy răng cưa trên 70 % giữa lưỡi, khi bay. Thấp hơn là mượt hơn.

| Cấu hình | Phím 1 | Phím 7 kiếm chủ | Phím 7 LOD | Phím 7 impostor |
|---|---|---|---|---|
| High, DPR 1 (MSAA 0, không FXAA) | 0,244 | 0,182 | 0,151 | 0,138 |
| High, DPR 1, MSAA 4 (thí nghiệm) | 0,205 | 0,157 | 0,137 | 0,137 |
| High, DPR 2 | 0,115 | 0,083 | 0,076 | 0,077 |
| High, DPR 2, MSAA 4 (thí nghiệm) | 0,114 | 0,082 | 0,073 | 0,077 |
| Ultra (DPR 2, MSAA 4) | 0,108 | 0,081 | 0,071 | 0,074 |

- **High không có khử răng cưa**, dù canon D57 và `AGENTS.md` của game ghi "hậu kỳ có khử răng cưa" cho High và Ultra. `TT_MSAA.high` là 0, và trong chuỗi hậu kỳ không có FXAA hay SMAA (`RenderPass`, `UnrealBloomPass`, `ScreenPass`, `OutputPass`). Chỉ Ultra có MSAA 4.
- Ở DPR 1, một lưỡi rộng 6 px nghiêng bị bậc thang, và khi bay thì bậc thang ấy bò dọc lưỡi.
- DPR 2 giảm răng cưa còn một nửa. MSAA 4 ở DPR 1 chỉ giảm ~16 %, ở DPR 2 không thêm gì, và không tác dụng lên impostor (impostor là ảnh đã lọc, không có cạnh hình học).

### 3.3b Thời gian thật trên màn DPR 2 (độ phân giải động)

Màn chính của anh là LG UltraFine 4K "trông như 1920 × 1080", tức `devicePixelRatio` 2. Lượt đo dùng rAF thật, không ghim DPR, không đồng hồ cố định, đúng như bản lab mặc định. Chạy trong Chrome headless trên chính máy M4, qua `heavy.sh --perf`, không trình duyệt nào khác chạy cùng. Kịch bản: nghỉ 12 s, rồi lần lượt phím 1, 0, 2, 7, 6, 5, nghỉ xen giữa.

| Lượt | Tỉ lệ điểm ảnh vẽ trong lúc chiêu chạy | Khung/giây khi chiêu chạy | Khung trễ (> 21,7 ms) |
|---|---|---|---|
| High, Fire | **1,0** ở 54–100 % số khung (phím 1, 2: 100 %; phím 6, 7: 89 %; phím 5: 84 %; phím 0: 54 %), 1,25 ở phần còn lại | 49–59 | 1–13 % |
| High, Metal | 1,0 ở 68–99 % (phím 1: 99 %; phím 2: 94 %; phím 6: 90 %; phím 7: 82 %; phím 0: 68 %) | 49–57 | 2–15 % |
| Ultra, Fire | 1,0 ở 100 % (đã chạm sàn) | **33–41** | 40–63 % |

- **Trên màn 4K, High vẽ kiếm ở 1920 × 1080 rồi trình duyệt phóng 2 lần lên.** Bộ điều tốc bắt đầu ở 1,5 rồi hạ xuống 1,0 trong vài giây đầu, vì ở 1,5 máy không giữ được 60 khung. Trong lúc chiêu chạy, nó gần như nằm luôn ở 1,0.
- Một lưỡi rộng 6 px CSS vì thế thành 6 điểm ảnh vẽ, phóng lên 12 điểm ảnh màn, không khử răng cưa. Bậc thang to gấp đôi, viền mềm đi vì phép phóng song tuyến.
- Đây là phần "mờ" mà mắt anh thấy được trên màn này. Ở màn 1080p (DPR 1), phần này không có.
- **Ultra trên M4 không giữ được 60 khung** ngay cả ở sàn DPR 1: khoảng một nửa số khung là 33 ms. Mỗi khung hiển thị, kiếm nhảy gấp đôi quãng (phím 1: ~84 px). Nếu anh thử ở Ultra, kiếm còn khó nhìn hơn.
- Các khung trễ 33 ms ở High (1–15 %) cũng làm kiếm nhảy đôi đúng lúc chiêu nặng nhất (phím 6, phím 7).
- Lượt headless có thể khác Chrome có cửa sổ đôi chút, nhưng cùng GPU M4 và cùng bản lab.

### 3.4 Bloom

| Phím | Vành 5 px quanh lưỡi, bloom bật → tắt | Bề dày thấy được của lưỡi (px), bật → tắt | Bề rộng hình học (px) |
|---|---|---|---|
| 1 | 14,0 → 11,5 | 5,9 → 5,8 | 6,0 |
| 7 kiếm chủ | 48,8 → 32,0 | 9,2 → 7,2 | 7,2 |
| 7 LOD (dòng sông) | 64,5 → 26,4 | 9,0 → 6,0 | 6,2 |
| 7 impostor | 37,7 → 26,6 | 7,9 → 7,2 | 5,7 |

- Đường mép trắng nóng (`EDGE_HOT` 3,6, HDR) đi qua bloom. Ở dòng sông phím 7, nó làm lưỡi dày thêm ~50 % và quầng quanh lưỡi tăng 2,4 lần, nên viền nhòe.
- Ở phím 1 bloom gần như không đáng kể.

### 3.5 Tầng (lưới đủ, LOD, impostor), mip, lọc

- **Impostor phím 7:** dài trung vị 94 px. Ở mip 0, atlas có 5,2 texel mỗi px dọc lưỡi và 4,9 texel mỗi px ngang lưỡi. GPU vì thế lấy ở mip ~2,3, tức ~1 texel mỗi px: đúng mức, không thiếu chi tiết, không bị lọc quá.
  - Thu nhỏ đều theo hai chiều (tỉ lệ 1,06), nên anisotropy 4 không đổi gì.
  - Vòng cổng trời phím 6: mip ~1,9.
- **Thí nghiệm "lưới đủ thay mọi tầng"** (phím 6, phím 7: kiếm giữa sang lưới đủ, impostor vẽ bằng lưới đủ cùng chỗ):
  - Weber kiếm xa 8,1 → 9,9.
  - Răng cưa kiếm xa **tăng** 0,138 → 0,207: impostor là ảnh đã lọc nên mượt hơn lưới ở High không khử răng cưa.
  - Độ nháy giữa các khung 0,034 → 0,037.
- **Kết luận:** tầng không làm kiếm mờ. Không cần tăng độ phân giải impostor, đổi khoảng cách LOD hay anisotropy.

### 3.6 Kích thước

- Ở camera chơi, lưỡi rộng 5,7–7,4 px, dài 70–120 px. Vòng ngọc và hai rãnh chỉ 1–2 px, nên ở cỡ này kiếm đọc như "một cây kim bạc có chấm".
- Thí nghiệm kiếm × 1,4: phím 1 dài 71 → 99 px, rộng 6,0 → 8,3 px. Tốc độ px không đổi (42 px/khung, vì chuyển động tính theo mét), nên số khung bay đọc được **vẫn là 0**.
- Kích thước giúp nhận ra chi tiết lúc kiếm chậm, không giúp lúc kiếm bay.

## 4. So với game tham chiếu

Video chính thức trong `games/immortality-cultivation/tmp/shots/sword-aura/concept/board/board-sources.md`. Khung lấy trong tab trình duyệt của tôi, bước 1/30 s (Wuchen là 60 fps nên lấy cách một khung), đo bằng mắt trên khung đủ cỡ. Không đưa lên công cụ AI nào; khung thô đã xóa, chỉ giữ tấm `reference-frames.jpg`. Cửa sổ 1:43.5 của Qingxiao combat là cảnh hội thoại, không có kiếm, nên không dùng.

| Nguồn | Cỡ kiếm (px ở 1080p) | Trên màn bao lâu | Giữ, treo | Giữ nét khi chuyển động thế nào |
|---|---|---|---|---|
| Naraka Wuchen, camera trong game (Skill Updates 0:04–0:15) | Kiếm xa ~110, gần 300–550 | **Nhiều giây**: năm phi kiếm bay quanh người 12 s | Lượn quanh người rồi mới phóng | Lưỡi tự phát sáng lam trắng, chuôi tối có vòng ngọc. Lao rất nhanh (~60 px mỗi khung 60 Hz), nhưng mắt đã biết kiếm ở đâu |
| Wuchen Skill Preview 2:03–2:06 | ~250–500 | ~2 s | Quạt năm lưỡi **treo ~1 s** cạnh người trước khi phóng | Như trên; vệt dài thẳng sau mỗi lưỡi |
| A Record of a Mortal's Journey, 24 phi kiếm (0:15–0:18.5) | ~150–185 (khung dọc 1080 rộng) | ~3 s | Bay vào 0,2 s, rồi **treo ~1 s** thành trận quanh người, rồi cận cảnh trượt chậm ~1 s | Lưỡi xanh tối, vòng ngọc sáng, khí xanh và sét bao quanh |
| Wuthering Waves Qingxiao, combat showcase 0:30–0:33 | ~700–1500 | ~1,7 s | Trượt dưới chân, **~0,02 chiều dài mỗi khung** | Lõi lam sáng, viền trắng mảnh; nền nhòe chuyển động, kiếm thì nét |
| Qingxiao, ult 0:08–0:12 | 300–1500 | Nhiều giây | Tư thế giữ 2–3 khung (vẽ "on twos/threes") | Hình phẳng sáng, viền rõ |
| Honkai: Star Rail Yanqing trailer 0:35–0:38 | Vệt dài cả trăm px | ~1 s mỗi lượt | Không treo | Kiếm đọc thành **vệt sáng** dọc làn, sao ở mũi |

**Rút ra:**
1. Tham chiếu không làm kiếm chậm hẳn khi lao. Wuchen lao ~60 px mỗi khung, nhanh hơn phím 1 của ta. Nhưng **trước cú lao luôn có thời gian trên màn**: lượn quanh người, treo thành trận ~1 s, hoặc trượt chậm.
2. Trong tham chiếu, khoảnh khắc nhanh nhất **không phải lần đầu mắt thấy kiếm**. Ở phím 1 của ta thì là.
3. Lưỡi tự phát sáng, chuôi tối, nên bóng kiếm nổi trên mọi nền.
4. Vệt sau kiếm thẳng và còn lại vài khung, nên đường bay vẫn đọc được sau khi kiếm đã qua.
5. Phim hoạt hình giữ tư thế 2–3 khung, nên mỗi hình kiếm sống đủ lâu.
6. Cỡ: kiếm xa trong game Wuchen (~110 px) gần bằng kiếm phím 7 của ta ở camera chơi (94–122 px). **Cỡ không phải chỗ thua chính.**

## 5. Xếp hạng nguyên nhân

| Hạng | Nguyên nhân | Loại | Bằng chứng | Ảnh hưởng tới |
|---|---|---|---|---|
| 1 | **Chuyến bay quá ngắn, quá nhanh, và là lần đầu mắt thấy kiếm** | Tốc độ, thời gian | Phím 1: 6 khung bay, 42/58 px/khung, 0 khung bay đọc được; cận cảnh 128 px/khung, rời khung sau 4 khung. Phím 2: 12 khung, 35/60. Phím 0: 18 khung, 15/19. Phím 5: 8 khung, 20/33. Mưa kiếm phím 6: 33/165. Ở 0,25× phím 1 đọc được 16/25 khung bay | Mọi hệ, mọi tầng, mọi DPR |
| 2 | **Kiếm lớn dần trong lúc bay** | Thời gian | Thanh 1 phím 1 và phím 2 đi từ 5 px lên 64–78 px đúng trong 6 khung bay (`BLADE_IN_S` 0,12 s) | Phím 0, 1, 2 |
| 3 | **Lưỡi Fire tối, sát độ chói nền** | Ảnh: tương phản | Weber 0,5 (Metal 3,2); tín hiệu −40 %; `steel` trả về 3,0, `char` 0,4 được 1,55 | Fire, mọi phím; phím 5 lưỡi tối hơn nền |
| 4 | **VFX phủ lưỡi** | Ảnh: phủ | Vỏ lửa 21–42 % (Fire); phím 2: 78–92 %; kiếm cắm ở đích bị chớp phủ 48–83 % trong ~10 khung; kiếm trời phím 6: 26 % | Phím 2 mọi hệ; Fire phím 0, 1, 7; khoảnh khắc sau khi trúng |
| 5 | **Không khử răng cưa ở High, và độ phân giải động nằm ở 1,0 trên màn 4K** | Ảnh: độ phân giải, răng cưa | Thời gian thật trên màn DPR 2: tỉ lệ 1,0 ở 54–100 % khung chiêu (§3.3b), tức vẽ 1080p rồi phóng × 2. Răng cưa DPR 1 gấp đôi DPR 2 (0,244 so với 0,115). High MSAA 0, không FXAA. Ultra chỉ 33–41 khung/giây | High và Ultra trên màn DPR 2 |
| 6 | **Bloom làm dày, nhòe viền** | Ảnh: bloom | Dòng sông phím 7: dày 6 → 9 px, quầng × 2,4 | Phím 7 (cả Fire ít hơn) |
| 7 | **Lưỡi mảnh** ở camera chơi | Cỡ | Rộng 5,7–7,4 px; chi tiết 1–2 px | Nhận dạng "Clear Wind" lúc chậm |
| – | Tầng impostor/LOD, mip, anisotropy | Không phải nguyên nhân | §3.5 | – |

**Chúng cộng lại thế nào:** để thấy một thanh kiếm, mắt cần ba thứ theo thứ tự.
1. **Thời gian** để tìm ra kiếm: ~0,2 s để nhảy tới, rồi bám theo được nếu kiếm chạy dưới ~20°/s, tức ~12 px/khung.
2. **Tương phản** để tách kiếm khỏi nền.
3. **Một bóng sạch** để nhận ra đó là kiếm.

Metal hỏng ở bước 1. Fire hỏng ở bước 1 và 2. Độ phân giải động, răng cưa và bloom làm bước 3 kém đi, nhất là trên màn 4K. Chớp va chạm xóa bóng kiếm đúng lúc nó vừa dừng lại, tức khoảnh khắc duy nhất kiếm đứng yên sau chuyến bay. Nên **chỉ tăng độ nét thì không cứu được**: một thanh kiếm nét hoàn hảo bay 6 khung vẫn không ai thấy, và một thanh kiếm chậm nhưng tối như nền vẫn khó thấy.

## 6. Cách sửa

Mỗi cách theo đúng nguyên nhân của nó. Chi phí là ước tính, phải đo bằng đầu dò này và cổng hiệu năng của ELEMENT_LAYER. "Trùng hào quang" là phần lượt dựng hào quang kiếm (A Wind-Silk Mantle + TipStar) đang làm hoặc nên gánh.

| # | Cách sửa | Nguyên nhân | Chi phí, rủi ro | Trùng hào quang? |
|---|---|---|---|---|
| T1 | **Kiếm chờ cất cánh sớm hơn, nửa sau chậm lại:** thanh 2 và 3 phím 1 rời vai 0,25–0,3 s trước tick trúng (nay 0,1 s). Đường bay nhanh lúc đầu, 8–10 khung cuối ≤ 12 px/khung ở camera chơi. Tick trúng giữ nguyên | 1 | ~0 ms. Chỉ là view; cần chỉnh đường cong và thời điểm vệt | Không |
| T2 | **Lớn đủ rồi mới bay:** `BLADE_IN_S` xong trước khi kiếm dời chỗ (thanh 1 phím 1, phím 0, phím 2) | 2 | 0 ms. Thanh 1 phím 1 không còn chỗ (trúng ở +6) nếu không có T3 | Không |
| T3 | **Treo trước khi phóng cho thanh rời ngay lúc phóng:** treo 8–12 khung, mũi chỉ vào đích. Hoặc để lab mặc định gõ chữ (`?typed=1`) cho anh thấy đúng như người chơi | 1, 2 | Muốn treo thì phải dời tick trúng canon §12.1 (phím 1 +6 → ~+18), là luật lối chơi, **anh quyết** | Không |
| T4 | **Cổng "thời gian đọc tối thiểu":** mỗi kiếm chủ ≥ 12 khung dài ≥ 40 px và ≤ 12 px/khung giữa lúc hiện và lúc trúng, đo bằng `probe.js` ở camera chơi và cận cảnh | 1 | Một kịch bản đo (đã có công cụ) | Không |
| T5 | **Cận cảnh khi chiêu bay:** giữ đích trong khung (như phím 6 và 7 đã lùi về toàn sân), hoặc lùi một phần. Tốc độ px ở cận cảnh gấp 3 lần | 1 | Đổi cảm giác camera, cần anh xem | Không |
| T6 | **Vệt đường bay còn lại 8–12 khung** sau khi kiếm qua, thẳng, mảnh, như tham chiếu | 1 | +ít ms (ribbon có sẵn) | **Có**: đuôi `SilkTail`/needle của áo khí; phải ở ngoài viền lưỡi |
| C1 | **Lưỡi Fire phải đạt Weber ≥ 2 trên nền đá:** sống và mép sáng, thân không dưới `char` ~0,5; hoặc để áo khí và khe mực của hào quang tách lưỡi khỏi nền | 3 | Cổng: Weber ≥ 2 lúc chờ và lúc bay | **Có**: khe mực 1 px và áo khí là đúng chỗ này; đo lại sau khi hào quang vào |
| C2 | **Vỏ lửa ra ngoài viền lưỡi**, không đè lên (phủ 21–42 % → ≤ 5 %) | 4 | Đổi chỗ vẽ, ~0 ms | **Có**: luật "hào quang ở ngoài viền" của SWORD_AURA |
| C3 | **Phím 2: lưỡi vẽ trên vạch của nó**, vạch và chớp tối đi dưới lưỡi (phủ 78–92 % → ≤ 20 %) | 4 | Thứ tự vẽ, ~0 ms | Một phần (khe mực) |
| C4 | **Chớp va chạm và số sát thương không đè kiếm vừa cắm:** chớp sau lưỡi, hoặc lưỡi sáng lên trong 3–4 khung đầu; số sát thương bật lên lệch khỏi chuôi kiếm | 4 | ~0 ms; giữ sức nặng cú đánh. Chỗ đặt số là luật UI chung (`hitfx`), cần anh xem | Không |
| R1 | **Khử răng cưa rẻ ở High:** FXAA hoặc SMAA trong chuỗi hậu kỳ (~0,3–0,6 ms ở 1080p, chưa đo) | 5 | Hơi mềm ảnh; rẻ hơn MSAA 4 nhiều (D57: +3 ms) | Không |
| R2 | **Sàn độ phân giải khi chiêu chạy:** không hạ tỉ lệ dưới 1,25–1,5 trong lúc chiêu bay, hạ sau chiêu (§3.3b: nay nằm ở 1,0) | 5 | **Rủi ro cao trên M4:** D57 đo DPR 1,5 là 16–17 ms ở đỉnh K5, và lượt thời gian thật cho thấy ở 1,25 máy đã trễ khung. Có thể đổi nét lấy giật. Phải đo, có thể chỉ cho kiếm chủ (vẽ riêng ở độ phân giải cao hơn là việc lớn) | Không |
| R3 | **Ultra không nên là mức mặc định trên M4** cho tới khi giữ được 60 khung (nay 33–41) | 5 | Không chi phí; chỉ là mặc định | Không |
| B1 | **Bloom nhẹ tay trên lưỡi sông phím 7:** mép HDR 3,6 → ~2 ở kiếm giữa và kiếm xa, giữ ở kiếm chủ | 6 | ~0 ms; lưỡi bớt "phát sáng" | **Có**: ngân sách bloom của TipStar và áo khí |
| S1 | **Kiếm chủ to hơn × 1,3–1,4** ở phím 0, 1, 2 | 7 | Rối sân; không sửa tốc độ (§3.6) | Không |
| – | Tăng độ phân giải impostor, đổi khoảng cách LOD, anisotropy | – | Không cần (§3.5) | – |

**Làm trước:** T1 + T2 + T4 (rẻ, view-only, sửa nguyên nhân 1–2 cho mọi hệ), rồi C1 + C2 cùng lượt hào quang, rồi R1. T3 và R2 cần anh quyết.

**Mô phỏng trong video:** hai cách cho hai nguyên nhân đứng đầu (thời gian, tương phản Fire), làm trong trang, không sửa mã.
- **Thời gian:** "world time 0.35× while a lead sword flies faster than 12 px/frame" (phím 7: chỉ 0,5 s đầu, chuyến bay đầu của kiếm chủ). Đây là kiểu chậm phản ứng: khung bay đầu tiên vẫn ở tốc độ thật. Nó làm chậm cả VFX xung quanh; bản sửa thật chỉ đổi đường bay của kiếm.
- **Tương phản:** lưỡi Fire giữ thép sáng (`steel`).

## 7. Câu hỏi cho anh

1. **Lab mặc định gõ chữ hay đánh tức thì?** Ở chế độ tức thì (bản anh thử), thanh đầu phím 1 rời ngay lúc phóng và không có lúc chờ. Trong game, nó chờ sau vai trong lúc anh gõ. Anh muốn lab mặc định `?typed=1` để thấy đúng như người chơi, hay muốn chiêu đánh tức thì cũng phải có một nhịp treo?
2. **Phím 1 có được dời tick trúng đầu (+6 → khoảng +18) để thanh đầu treo 8–12 khung rồi mới lao?** Đây là luật lối chơi (canon §12.1). Không dời thì thanh đầu chỉ là một "đòn chớp" có vệt.
3. **Lưỡi Fire:** anh muốn thân lưỡi sáng hơn (sống, mép thép sáng, `char` ~0,5 trở lên), hay giữ thép tối và để áo khí cùng khe mực của hào quang tách lưỡi khỏi nền?
4. **Trên màn 4K:** anh chọn ảnh nét hơn khi chiêu chạy (sàn độ phân giải, có thể rớt khung), hay giữ khung mượt và thêm khử răng cưa rẻ (FXAA/SMAA) ở High?
5. **Kiếm chủ phím 0, 1, 2 to hơn 30–40 %?**

## 8. Tệp, công cụ, đo lại

Tất cả ở `games/immortality-cultivation/tmp/sword-readability/` (ngoài Git):
- `owner/`: `sword-speed-compare.mp4`, `sword-crops.jpg`, `reference-frames.jpg`.
- `data/`: mỗi lượt đo một `*.json.gz` (mỗi kiếm mỗi khung; giải nén trước khi chạy `analyze.mjs`). `data/digest.json` là bảng tóm tắt, `data/dynres-*.json` là các lượt thời gian thật. `clips/*/clip.json` là vị trí kiếm từng khung của các clip; khung ảnh thô đã xóa.
- `tools/`: công cụ đo, dùng lại được.
  - `probe.js`: đầu dò trong trang.
  - `experiments.js`: các thí nghiệm, gồm `notrail`, `noflash`, `noflame`, `nobloom`, `big<k>`, `fullmesh`, `msaa<n>`, `steel`, `char<k>`.
  - `measure.mjs`: kịch bản CDP.
  - `analyze.mjs`, `tables.mjs`, `pixstats.mjs`, `brief.mjs`: tóm tắt.
  - `dynres.mjs`, `dynres-sum.mjs`: thời gian thật.
  - `clip.mjs`, `crops.mjs`, `make-video.sh`, `make-crops.sh`: video và tấm cắt.
  - `batch1.sh` … `batch5.sh`: các ma trận đã chạy; `data/tables.md`: bảng của mọi lượt.
  - `refs.mjs`: khung video tham chiếu.
- Đo lại sau khi hào quang vào: chạy `measure.mjs` với `PIX=1` trên bản mới. Cổng đề xuất: T4, Weber ≥ 2 (C1), phủ ≤ 5 % khi bay (C2), phím 2 phủ ≤ 20 % (C3).

## 9. Phản biện (03/11/2026)

**Cách kiểm.** Một lượt độc lập, không dùng `probe.js` hay số của lượt đầu:
- **Bản đo:** `9cb7bcd` xuất riêng bằng `git archive` vào `games/immortality-cultivation/tmp/sword-readability/verify/app/`. Cấu hình Vite riêng (cổng 3187, `cacheDir` riêng, không HMR, không theo dõi tệp).
- **Điều kiện:** High 1920 × 1080, DPR 1, đồng hồ cố định 60 Hz, camera chơi; thêm cận cảnh và 0,25× cho phím 1.
- **Đầu dò riêng** (`verify/tools/vprobe.js`):
  - Hình học đọc thẳng từ `BladeSet`: đốc, mũi, tâm chiếu lên màn.
  - Ảnh: cùng một khung vẽ lại sáu lần. Kiếm được ẩn bằng `colorWrite = false`, nên bóng kiếm vẫn còn (lượt đầu dùng `visible = false`, bóng mất theo). Mặt nạ lưỡi lấy từ hai lần vẽ có bloom 0.
  - Kiểm vẽ lại: khung vẽ lại và khung sau khi trả mọi thứ về đều trùng khung gốc từng byte.
  - Ngoài Weber trung bình, đầu dò còn đo:
    - tỉ lệ điểm ảnh lưỡi lệch độ chói nền ≥ 50 %;
    - phân vị p10 và p90 của độ lệch ấy;
    - ΔE OKLab so với nền đá, và so với nền thật trong ảnh cuối (có VFX);
    - phần lưỡi nằm trên VFX.
- **Bản anh đang mở:** thư mục `owner-preview` nay khác `9cb7bcd` ở camera xoay quanh của lab (phím O) và các ảnh cut-in thử (`orbit.ts`, `cutin.ts`, `skills-main.ts`). Mã kiếm giống hệt, nên chẩn đoán vẫn áp dụng. Server của anh nay ở cổng 3160.

### 9.1 Nguyên nhân 1, chuyến bay ngắn và nhanh: xác nhận, nhưng nói quá ở ba chỗ

Số đo khớp:

| | Lượt đầu | Đo lại |
|---|---|---|
| Phím 1, mỗi thanh | 6 khung bay, 42 / 58 px/khung | 5–6 khung. Thanh 1: 35, 39, 44, 50, 58. Thanh 2, 3: 39, 39, 42, 47, 54, 63 |
| Phím 1 cận cảnh | 128 / 138, rời khung sau 4 khung | 122–153 px/khung; thanh 2 cất cánh ở f32, ra khỏi mép trên ở f35–36 |
| Phím 2 | 12 khung, 35 / 60 | 12 khung, giảm dần 66 → 9 px/khung |
| Phím 0 | 18 khung, 15 / 19 | 17 khung, 13–21 px/khung (trung vị 16) |
| Phím 1 ở 0,25× | 16 / 25 khung đọc được | Thanh 2, 3: 16 / 25 ở ngưỡng 12 px/khung, 25 / 25 ở ngưỡng 20 |

Ba chỗ nói quá:
1. **Ngưỡng 12 px/khung quyết định kết quả ở phím 0 và phím 5.**
   - Phím 0 bay 17 khung, dài 77–98 px từ khung thứ 3, chạy 13–21 px/khung (~23–37°/s, vẫn trong vùng mắt bám theo được). Ở ngưỡng 12 nó có 0 khung đọc được; ở ngưỡng 20 có 13 / 17.
   - Phím 5 (Lạc Kiếm Trận): mỗi kiếm có 0–4 khung đạt ngưỡng 12, và 1–7 khung đạt ngưỡng 20, trên 9–10 khung bay.
   - Phím 1 thì vẫn 0 khung ở cả ngưỡng 20 lẫn 30.
   - Phím 2 đạt 3 / 12 ở ngưỡng 20 và 6 / 12 ở ngưỡng 30. Nửa đầu nhanh (f2–f8, 66 → 29 px/khung) bị vạch và chớp phủ 66–84 % (Metal); ba khung chậm cuối (f10–f12, 20 → 12 px/khung) thì sạch, chỉ bị phủ 5–20 %.
   - Vậy chỉ phím 1 và nửa đầu phím 2 chắc chắn hỏng vì tốc độ. Phím 0 và phím 5 ở ranh giới, không nên xếp chung nhóm "0 khung đọc được".
2. **"Mọi hệ, mọi tầng"** (bảng §5) trái với bảng §2.1 của chính tài liệu này: kiếm giữa và kiếm xa phím 7 có 63–71 % khung bay đạt ngưỡng. Ở phím 7, tốc độ không phải nguyên nhân chính.
3. **Clip "sửa mô phỏng" không đạt cổng T4 mà tài liệu đề xuất.** Trong lúc làm chậm, kiếm vẫn chạy 13–23 px/khung (`clips/k1-fire-fix/clip.json`), trên ngưỡng 12.
   - Nếu anh thấy clip ấy đã đọc được, thì ngưỡng 12 chặt hơn mức cần.
   - Ngưỡng của T4 nên chỉnh theo mắt anh trên clip, không cố định ở 12 từ đầu.

### 9.2 Nguyên nhân 2, kiếm lớn dần khi bay: cơ chế đúng, nhưng không phải nguyên nhân riêng

- **Cơ chế đúng.** `BLADE_IN_S` 0,12 s = 7,2 khung, dài hơn 6 khung bay.
  - Thanh 1 phím 1 dài 17, 32, 46, 57, 64 px trong 5 khung bay; khi đứng yên nó dài 69 px, thanh 2 và 3 dài 77–87 px.
  - Phím 2: 18, 35, 52, 68 px, rồi 78–82 px.
  - Phím 0: 20, 40 px, rồi 61–98 px.
- **Không thêm khung đọc được nào.** Mọi khung "chưa đủ lớn" cũng là khung nhanh: phím 1 chạy 35–50 px/khung, phím 2 chạy 66–48, phím 0 chạy 15–16.
  - Nếu kiếm đủ lớn ngay từ đầu (chỉ làm T2), theo đúng luật "đọc được" của tài liệu này vẫn có **0 khung đọc được** thêm.
  - T2 chỉ có giá trị khi đi cùng T1 hoặc T3.
- **Phần lớn là chuyện của lab.** Theo D58 (1), pha gồng hiện trong lúc gõ: ba thanh phím 1 hiện ở 15, 45 và 75 % của từ, kiếm phím 2 hiện ở tay. Trong game, phím 1 và phím 2 không lớn dần khi bay. Phím 0 (không có từ) thì vẫn lớn dần, nhưng chỉ ở 2 khung đầu.
- **Đề nghị:** gộp vào nguyên nhân 1 như một chi tiết. Với bản Fire anh đang thử, lưỡi Fire (§9.3) nên đứng hạng 2.

### 9.3 Nguyên nhân 3, lưỡi Fire tối: đúng mức độ, sai cơ chế, cổng C1 đo sai chỗ

Cùng VFX Fire, ba kiểu lưỡi: Metal, Fire (`furnace`, `char` 0,12) và Fire với thép sáng của Metal (`steel`). Mỗi ô là trung vị theo khung, ghi theo thứ tự Metal / Fire / Fire `steel`.

| Pha | Weber trung bình so với đá | Điểm ảnh lệch nền ≥ 50 % | ΔE OKLab so với đá (× 100) | ΔE trong ảnh cuối (× 100) | Phần lưỡi nằm trên VFX |
|---|---|---|---|---|---|
| Phím 1, chờ sau vai (thanh 2, 3; f12–30) | 5,19 / 0,52 / 5,19 | 93 / 83 / 93 % | 39 / 23 / 39 | 34 / 20 / 33 | 26 / 62 / 62 % |
| Phím 1, bay (≥ 20 px/khung) | 3,81 / 0,50 / 3,81 | 94 / 76 / 95 % | 30 / 18 / 30 | 28 / 14,5 / 29 | 13 / 80 / 80 % |
| Phím 0, bay | 4,05 / 0,67 / 3,99 | 94 / 75 / 94 % | 31 / 18 / 31 | 30 / 15 / 29 | 14 / 78 / 78 % |

**Phần đứng vững:**
- Số Weber của lượt đầu lặp lại đúng: Fire 0,50, Metal 3,81.
- Thép sáng dưới đúng VFX Fire đưa ảnh cuối về mức Metal (ΔE 29–33).
- Lưỡi Fire là nguyên nhân thật và lớn của bản Fire: trong ảnh cuối, nó chỉ tách nền khoảng một nửa so với Metal.

**Phần sai: cơ chế.** Lưỡi Fire **không** "sáng gần bằng nền đá", và cũng không phải "một vệt sắt tối trên đá tối".
- 75–83 % điểm ảnh của lưỡi lệch nền từ 50 % trở lên. Khi bay, p10 là −0,82: chuôi, chắn và phần than tối hơn nền 82 %. P90 là +3,2: dải nhiệt và mép nóng màu cam sáng gấp ~4 lần nền.
- Weber trung bình chỉ còn ~0,5 vì hai phần sáng và tối triệt tiêu nhau.
- Ở cỡ thật trên màn (tấm `verify/sheets/k1-metal-fire-3x.jpg`, phóng × 3), kiếm Fire đọc như một lưỡi cam có chuôi đen, không hòa vào đá.
- Khi kiếm bay ~40 px/khung, mắt gộp sáng và tối lại, nên Weber trung bình là thước đúng lúc bay. Lúc kiếm đứng chờ sau vai, mắt thấy được cấu trúc đen và cam, nên con số "Weber 0,5" làm kiếm chờ trông tệ hơn thực tế.

**Phần tài liệu bỏ sót:**
- 62 % (lúc chờ) đến 80 % (lúc bay) diện tích lưỡi Fire nằm trên chính VFX Fire: quạt lửa sau vai, vỏ lửa, vệt cam. Ở Metal con số này là 13–26 %.
- Cột "Bị VFX phủ" (21–42 %) chỉ đếm VFX vẽ **đè lên** lưỡi, không đếm VFX nằm **sau** lưỡi.
- Trên nền lửa, lưỡi Fire chỉ tách nền ΔE 15–20, ngang mức trên đá. Lưỡi thép trên cùng nền lửa tách ΔE 30–36.

**Phím 5 Fire.** "Lưỡi tối hơn nền" (Weber −0,3) đúng cho pha kiếm đã cắm xuống đất (f14–200: −0,34). Lúc bay (f1–13), Weber là +0,65. Bảng §2.1 trộn hai pha này. Ẩn kiếm kiểu lượt đầu (mất cả bóng) chỉ làm Weber lệch 0,05–0,07, nên chỗ khác biệt này không đến từ bóng.

**Hệ quả cho cách sửa:**
- Cổng C1 "Weber ≥ 2 so với đá" đo sai chỗ và có thể lách: một lưỡi hai tông có thể có Weber ~0 mà vẫn nổi, hoặc đạt Weber 2 so với đá mà vẫn chìm trong lửa của chính nó.
- Đề nghị đo trong ảnh cuối, so với nền thật có VFX, cả lúc chờ lẫn lúc bay: ΔE OKLab ≥ 0,25 (Metal đạt 0,28–0,34), kèm Weber trong ảnh cuối ≥ 2.
- C2 phải tính cả quạt lửa sau vai và vệt sau kiếm, không chỉ vỏ lửa.

### 9.4 Video cho anh (`owner/sword-speed-compare.mp4`)

**Phần đúng:**
- **Tốc độ thật (0–7,5 s):** khung trong video trùng khung tôi vẽ lại độc lập ở cùng thời điểm: cùng vị trí, PSNR 31–34 dB ở vùng kiếm (`verify/sheets/source-vs-owner-video.jpg`). Nén chỉ làm ảnh mềm đi một chút, không làm mất kiếm.
- **Đoạn 0,25×:** đúng như chú thích (kiếm chạy 8–17 px/khung, trung vị ~11), nhưng nó làm chậm cả lửa, chớp và thú.

**Phần cần sửa:**
- **Chú thích đoạn Fire tốc độ thật**, "almost as dark as the stone", sai vì lý do ở §9.3. Nên ghi: lưỡi đen và cam, trung bình bằng nền đá, 80 % lưỡi nằm trên lửa của chính nó.
- **Hai đoạn "TWO FIXES SIMULATED"** chưa công bằng:
  1. Đoạn này làm chậm cả thế giới, nên các đòn trúng muộn dần, tới ~29 khung (~0,5 s) ở thanh thứ ba phím 1. T1 thì giữ nguyên tick trúng. Riêng thanh 1 phím 1, cảnh này chính là T3 (dời tick trúng canon), việc anh chưa quyết.
  2. Kiếm vẫn chạy 13–23 px/khung, không phải đường bay ≤ 12 px/khung mà T1 và T4 đề xuất.
  3. Thanh 1 vẫn lớn dần trong lúc bay (17 → 66 px), tức T2 không được mô phỏng.
  4. Tốc độ và lưỡi thép bị gộp làm một, nên không biết cái nào có tác dụng. Ở phím 7, phần làm chậm chỉ có 0,5 s đầu (58 khung); phần còn lại chỉ khác ở lưỡi thép. Vậy chỗ trông tốt hơn ở phím 7 là do lưỡi, không phải do tốc độ (tấm `verify/sheets/k7-metal-fire-steel-f70.jpg`).
  5. "Bright steel" là thép sáng của Metal, trái với lựa chọn của anh tối 03/11 (SWORD_AURA Q3: lưỡi Fire là thép tối, mép nóng). Nó chỉ là vật thử độ tương phản, không phải đề xuất ngoại hình, nhưng chú thích không nói rõ điều đó.

**Kết luận:**
- Gửi được phần tốc độ thật và phần 0,25×, sau khi sửa chú thích Fire.
- Không gửi hai đoạn mô phỏng như hiện tại. Thay bằng hai đoạn tách riêng: (a) chỉ đổi tốc độ, giữ lưỡi Fire và giữ tick trúng; (b) chỉ đổi lưỡi, chạy tốc độ thật.
- Nên thêm một đoạn Metal ở 0,25× để anh thấy riêng tác dụng của tốc độ, không lẫn với màu lửa.

### 9.5 Xếp hạng sau phản biện

1. **Thời gian bay:** phím 1 và nửa đầu phím 2; phím 0 và phím 5 ở ranh giới.
2. **Lưỡi Fire:** sáng và tối triệt tiêu nhau, và lưỡi nằm trên lửa của chính nó. Hạng 2 cho bản Fire.
3. **VFX phủ:** phím 2, và kiếm vừa cắm sau khi trúng.
4. **Kiếm lớn dần khi bay:** gộp vào nguyên nhân 1; phần lớn do lab đánh tức thì.

Các nguyên nhân 5–7 chưa được kiểm lại trong lượt này. Riêng thí nghiệm "kiếm × 1,4 vẫn 0 khung đọc được" (§3.6) không chứng minh được gì: luật "đọc được" chỉ xét tốc độ tính bằng px, mà phóng to kiếm không đổi tốc độ, nên kết quả 0 là tất nhiên.

**Thứ tự sửa:**
- T1 + T4, với ngưỡng T4 chỉnh theo mắt anh.
- C1 + C2, đo bằng cổng mới trong ảnh cuối.
- R1.
- T2 chỉ làm cùng T1 hoặc T3.

### 9.6 Tệp

Tất cả ở `games/immortality-cultivation/tmp/sword-readability/verify/` (ngoài Git):
- `tools/`: `vprobe.js` (đầu dò), `vmeasure.mjs` (kịch bản CDP, biến `STEEL=1` và `HIDEVIS=1`), `vanalyze.mjs` và `vphase.mjs` (tóm tắt), `vcrops.mjs` (cắt khung).
- `data/*.json.gz`: Metal, Fire, Fire `steel`, cận cảnh, 0,25×, ẩn kiếm bằng `visible`.
- `sheets/`: năm tấm so sánh.

Khung thô đã xóa; server 3187 đã tắt.
