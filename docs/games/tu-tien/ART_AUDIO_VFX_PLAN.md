# Tu Tiên Thủ Ải — Kế hoạch gốc: hình, âm thanh, VFX, model 3D (01/11/2026)

> **Trạng thái:** bản đánh giá giải pháp, **chờ chủ dự án duyệt**. Chưa tạo ảnh, chưa tiêu credit Tripo, chưa đổi mã game. Theo lời chủ dự án 01/11 (trong phiên này): làm **một bản demo trước** để anh chấm từng chi tiết hình, âm, hiệu ứng; **đánh giá giải pháp trước khi triển khai** để không đi sai hướng; **gốc phải thật đúng** (bối cảnh tu tiên, hiệu ứng, hình, âm, hệ skill, nhân vật, quái ≥ 8,5) rồi mới triển khai rộng.
> **Nguồn thắng:** [`00-canon.md`](00-canon.md) (D03, D27, D47–D49, §8, §10, §12, §20–22), [`../LESSONS_FROM_THREE_GAMES.md`](../LESSONS_FROM_THREE_GAMES.md), `AGENTS.md` repo cha (mục Language, Art, 8,5), [`../VFX_STANDARD.md`](../VFX_STANDARD.md), [`../AUDIO_PIPELINE.md`](../AUDIO_PIPELINE.md), [`../MODEL_QUALITY.md`](../MODEL_QUALITY.md), [`../MONSTER_MODEL_INVENTORY.md`](../MONSTER_MODEL_INVENTORY.md), [`../TRIPO_TODO.md`](../TRIPO_TODO.md), [`../FREE_ASSET_SOURCES.md`](../FREE_ASSET_SOURCES.md), [`../IN_GAME_SETTINGS.md`](../IN_GAME_SETTINGS.md), [`../SHARED_SYSTEMS_BAR.md`](../SHARED_SYSTEMS_BAR.md).
> **Ảnh đo:** `games/immortality-cultivation/tmp/plan-2026-11-01/` (không vào Git): `greybox-{prep,wave}-{720,1080}.png`, `legend-{prep,wave}-{720,1080}.png` (có lưới tọa độ), `capture.mjs` (kịch bản chụp qua Chrome thật), `capture-*.log` (số đo).

## 0. Đánh giá giải pháp (đọc trước)

### 0.1 Kết luận

**Hướng đi là đúng, thứ tự làm mới là chỗ dễ sai.** 3D một renderer, camera 3/4 cố định thấy cả sân (D03, D48), thú theo trường hướng, chữ trên Bàn Quyết: đều hợp với gameplay và không cần đổi. Ba game trước trông "như đồ chơi" không phải vì hướng 3D mà vì: ánh sáng phòng studio giả (`RoomEnvironment`), model bị cắt còn 2–4k mặt và mất map, đất phẳng một màu, map dựng trước khi có ý tưởng, chấm trên bản dev có cờ. Tu Tiên tránh được nếu làm **đúng thứ tự: chuẩn ánh sáng và chất liệu → một mẫu mỗi loại đạt 8,5 → rồi mới nhân rộng.**

Bảy phát hiện đổi cách làm (số đo ở §2):

| # | Phát hiện | Hệ quả |
|---|---|---|
| 1 | **Camera không bao giờ thấy trời.** Nghiêng 55°, FOV dọc 28° → mép trên khung ở 41° dưới chân trời. **Mặt sân chiếm ~85 % khung**; viền ngoài sân chỉ là dải 84 px trên cùng và hai tam giác bên (rộng nhất 261 px ở mép xa, 39 px ở mép gần, tại 1080p). | "Epic, hùng vĩ" **không** đến từ phông núi mây (ảnh bản sắc `thanh-thach-ai-55.png` vẽ nhiều núi quanh sân, trong game chỉ còn một viền mỏng). Nó phải đến từ: **mặt đất** (đá lát, rêu, vết trận, decal), **ánh sáng điện ảnh** (một nguồn chính xiên, sương thấp, bloom đúng luật), **kiến trúc trong sân** (cổng, trụ, Trận Tâm) và **VFX**. Ý tưởng map 1 và mọi prompt Firefly viết theo điều này: viền vẽ như **nhìn từ trên xuống** (biển mây, đỉnh vách, tán tùng), không vẽ đường chân trời. |
| 2 | **Ngân sách chiều cao ở mép xa ≈ 2,5 m.** Cột 2,5 m dựng ở cổng (z −18) vừa lọt khung; 5 m và 8 m bị cắt (ảnh `legend-prep-1080.png`). Ở 55°, chiều cao chiếu lên màn chỉ còn cos 55° = 0,57 × tỉ lệ. | Cổng ải 6 m kiểu ảnh bản sắc **sẽ bị cắt mất mái**. Chọn một trong ba: (a) cổng thấp ≤ 2,5 m (yếu); **(b) tăng `headroomM` của view từ 2,5 lên ~5,5 m** (sân nhỏ đi ~8 %, chỉ sửa view, không sửa sim); (c) đặt phần cao của cổng ra ngoài sân về hai bên. Đề xuất **(b)** và thiết kế cổng **rộng, thấp, mái nhìn từ trên đẹp** (ngói, đỉnh mái, lan can), vì ở 55° camera nhìn thấy **mặt trên** của mọi vật: ngói, đỉnh trụ, mặt đĩa Trận Tâm, lưng thú. Ảnh nguồn Tripo phải chăm mặt trên. |
| 3 | **Cỡ vẽ hiện dưới sàn canon §21.1** ở 1080p: người chơi 41 px (sàn 64), thú Nhỏ ~27 px (sàn 36), bầy 18 px (sàn 20), thú Vừa 56 px (sàn 48, đạt). | Demo phải **phóng cỡ vẽ ở view** (canon cho phép): người ×1,6, thú Nhỏ ×1,4, bầy ×1,15; hitbox không đổi. Việc này kéo ngược với (2b): chốt cùng lúc, đo lại bằng `__ic.foeSizes()` và `ic-camera-frame`. |
| 4 | **53 ảnh nguồn Codex (25/10) chưa qua giám khảo.** Nhìn bằng mắt: prop và cơ quan là góc ba phần tư từ trên, một khối, nền xám phẳng (hợp Tripo); thú, tướng, Vương là cặp **ngang + trước** (hợp `multiview-to-model`), kiểu vẽ "minh họa khá" nhưng chưa phải mức thương mại; chân dung và cảnh ải đã được anh duyệt về **thiết kế**, không phải về mức 8,5 thị trường. | **Chấm mù trước** (hai giám khảo, mức thị trường và mức hợp Tripo). Dự đoán 7–8: phần lớn sẽ **vẽ lại bằng Firefly Image 5 theo một chuẩn chất liệu chung** (§4.1), giữ nguyên thiết kế đã duyệt (D47, D49). Không tiêu credit cho ảnh dưới 8,5 (chủ dự án 01/11). |
| 5 | **Dùng lại quái:** kho 195 model không có game tu tiên nào, nhưng có 3 ứng viên dáng đúng: `blight-wolf` (DH, sói) → Phong Lang; `tusk-boar` (DH, lợn rừng nanh đá) → Thiết Giáp Trư; `kamaitachi` (WW, chồn dài thấp) → Thạch Thử. Hỏa Nha ← `dai-bang-tinh` (đại bàng 35k mặt) gượng; Nham Viên, Lang Đầu Đàn, Thú Vương: không có. | Chạy **một ngày thử** cho 3 ứng viên: build lại từ bản gốc Tripo (5,6–5,9k mặt, giữ map), đổi texture sang bảng màu Tu Tiên, đặt cạnh một model Tripo mới dưới cùng ánh sáng, chấm mù. Rủi ro thật: kiểu Warcraft "khối" của DH lệch với vẻ quý phái thủy mặc; nếu < 8,5 thì dựng mới từ ảnh (đã có thiết kế), ghi lý do vào phiếu như luật. |
| 6 | **Máy Mac này chưa có Blender** (`blender not found`); Tripo API có bước `rig` (v3.0) và retarget. | Cần Blender cho VAT, impostor, dọn lưới, đổi texture (công cụ GPL, không ảnh hưởng giấy phép game). **Xin anh cho cài** `brew install --cask blender`. Thử `rig` của Tripo trên model mẫu đầu tiên để biết có thay được rig tay hay không. |
| 7 | **HN0 chưa bao giờ đo trên GPU thật** (bảng §20.4 toàn "chưa đo"). Hôm nay bản preview trên M4 ở Medium: 16,8 ms trung bình, bị vsync khóa, 56 draw call, 11,9k tam giác, grey box. | Trước khi cam kết HDRI + PBR + bloom + 60 thú VAT, chạy `ic-bench` trên Mac này (một giờ) để biết khoảng trống thật ở Low/Medium/High (§20.2). Không đo thì không hứa bậc nào. |

Hai việc **P0 ngoài mỹ thuật** phát hiện khi chạy bản build: (a) `vite preview` không phục vụ `/vocabulary/` (console: "vocabulary did not load; using the fallback set") → host chơi (nginx `tutien.typing-game.local`) phải phục vụ được, nếu không demo chạy bằng bộ từ dự phòng (lỗi kiểu "dev-only gap" = P0 theo luật 01/11); (b) trận demo hôm nay thua ở đợt 1 vì không ai gõ: bình thường, nhưng bot "Đứng yên" (D46) vẫn còn phát hiện 1 của changelog tích hợp (Nham Viên ngoài tầm) chưa ai giải.

### 0.2 Sáu quyết định nền (anh chốt trước khi tôi tạo bất cứ gì)

| # | Câu hỏi | Đề xuất của tôi | Vì sao cần sớm |
|---|---|---|---|
| Q1 | **Ngôn ngữ.** `AGENTS.md` repo cha (28/10): game tiếng Anh. Canon và toàn bộ UI hiện tại tiếng Việt (Trận Lực, Bàn Quyết, Thu Hoạch…). | Tiếng Anh cho UI, tên chiêu, tên thú, tên cơ quan như ba game kia; tên riêng giữ Hán-Việt (Thanh Thạch Ải, Thiết Bối Lang Vương, Kiếm tu Thanh Phong). Nghĩa tiếng Việt chỉ ở phần dạy từ. | Khung UI, độ dài nhãn, icon có chữ, màn tựa: làm tiếng nào thì vẽ tiếng đó. |
| Q2 | **Ai dựng model.** `games/immortality-cultivation/AGENTS.md`: "Real models come from the owner as GLB" (D27). Lời anh 01/11: Claude dựng qua Tripo API. | Đổi luật: Claude dựng qua API theo [`../TRIPO_TODO.md`](../TRIPO_TODO.md) (chỉ khi ảnh ≥ 8,5 từ hai giám khảo, `--dry-run`, một model trước, ghi credit). Model CC0/QAL của bên thứ ba cũng được (mở rộng 01/11 của SHARED_SYSTEMS_BAR §5). | Sửa `AGENTS.md` game và D27 sau khi anh xác nhận. |
| Q3 | **Tên game** (canon §0: tạm, chốt cùng ảnh bản sắc). | Nếu Q1 = tiếng Anh: cần tên Anh cho màn tựa (ví dụ *Thanh Thach Pass* / *Ascendant Pass*); anh chọn hoặc giữ "Tu Tiên Thủ Ải". `gameId` không đổi. | Tranh màn tựa và logo vẽ theo tên. |
| Q4 | **Chuẩn hình chung** (§4.1): "painterly-realistic" như hướng O1 của Dragonhold (vật liệu PBR thật, vẽ tay ở lớp màu, viền mực chỉ cho nhân vật, tinh anh, tướng, Vương), **không** hoàn toàn thủy mặc phẳng như canon §21.1 mô tả. | Chọn hướng này, vì mốc so là game thương mại (bảng tham chiếu, không phải style guide). Thủy mặc giữ ở: khói mực khi chết, vệt mực khi trúng, decal mực, nét thư pháp "chữ thành chiêu", sương. | Mọi prompt Firefly và ảnh nguồn Tripo viết theo một chuẩn. Đổi sau là vẽ lại cả bộ. |
| Q5 | **Camera:** tăng headroom lên ~5,5 m và phóng cỡ vẽ (0.1 #2, #3). | Làm, đo lại, anh xem ảnh trước/sau ở 720 và 1080. | Quyết định cỡ cổng, cỡ thú trong ảnh nguồn. |
| Q6 | **Bảng tham chiếu thương mại cho Tu Tiên** (mốc 9). Hiện chỉ có `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` (fantasy phương Tây). | Anh đưa 2–3 ảnh game tu tiên thương mại anh thấy "đúng" (cảnh từ trên xuống, nhân vật, quái, một ảnh VFX kiếm). Tôi để ở `art-src/_refs/` của game, giám khảo chấm so với bộ này. | Không có mốc tu tiên thì giám khảo chấm lệch. |

Trả lời "làm theo đề xuất" cho Q1–Q6 là đủ để tôi bắt đầu §3.

### 0.3 Khác gì ba game trước (chống lặp lỗi)

- Ý tưởng map viết theo **camera thật có số** (§2) trước khi vẽ; ChatGPT duyệt ở Chat mode, thinking High; ảnh nền có lưới tọa độ đã chụp sẵn để anh đính kèm.
- Một chuẩn chất liệu, một hướng sáng, một nền khóa, góc ba phần tư 30–35° cho **cả bộ** ảnh nguồn; kiểm khung bằng script (lề, một khối, bóng) trước khi chấm.
- **Chấm trong bản build trên host chơi, không cờ URL**, đúng cỡ, hai giám khảo mù; icon chấm ở 28–32 px trong Bàn Quyết, không trên tờ 256 px.
- Bloom chỉ lõi HDR mảnh; khói trộn thường; MSAA/SMAA ở High và Ultra; Ultra khác High thật.
- Model giữ mặt và map của bản gốc; `face_limit` theo loại (§7), không tối đa, không 2–4k.
- Âm là file thật, qua pipeline; tiếng phím dùng bộ Audio Lab chung (mức 9), không làm lại.
- Ảnh chụp thô dọn sau khi chấm (`node tools/capture-prune/prune.mjs <thư mục> --apply`).

## 1. Hiện trạng: cái gì còn là hộp xám (đo 01/11, bản build `pnpm build` tại `8093dcb`)

| Phần | Hiện tại | Ghi chú |
|---|---|---|
| Mặt sân 40 × 26 m | Mặt phẳng be `#b3ab95`, hành lang sáng hơn `#cdc5ab`, lưới mờ, ~30 vết mực xám thủ tục, viền đen; vùng ngoài sân xanh rêu phẳng `#7f8781` | Toàn bộ là đất thủ tục (`src/view/ground.ts`) |
| Cổng A, B | Hai cột hộp + xà ngang nâu (`GATE_M` 1,9 m) | Khối tạm |
| Trận Trụ T, P | Hai trụ tròn xám, viền mực | Khối tạm |
| Trận Tâm, Tâm nhãn | Đĩa đá + vòng rune sáng; chấm tròn xanh ngọc | Khối tạm |
| Kết Giới r 9 m | Một vòng tròn trắng mỏng | Chỉ là đường |
| 6 ô cơ quan, cơ quan đã đặt | Dải/vòng trắng mỏng; cơ quan là hộp màu | Khối tạm |
| Đường trời | Hai đường đứt từ góc trên | Gợi ý |
| Người chơi | Viên nang sáng | Khối tạm |
| Thú (5 họ, tinh anh, tướng, Vương) | Hộp, trụ, cụm hộp một màu theo họ (xanh lam, nâu) | Khối tạm, chế độ `procedural`; VAT và impostor có mã nhưng chưa có GLB |
| Kiếm, ô 1 và "vạn kiếm" | Que sáng trắng có vệt (`swords.ts`, 150/300/500) | Hình có, chưa là phi kiếm Thanh Phong |
| Báo đòn, trúng, chết | Vòng trên đất; lóe, tia, khói mực thủ tục | Khung VFX có, chưa đủ 5 pha, chưa có texture |
| HUD, Bàn Quyết, thẻ đợt, cửa hàng, Thu Hoạch, menu, thẻ tốc độ | DOM nền đen trong, chữ Be Vietnam Pro, không khung ảnh, không icon | Toàn bộ chữ trần |
| Màn tựa | Không có (vào thẳng thẻ tốc độ) | |
| Settings, Sound trong trận | Chưa có (kit `shared/game-kit/ui/quick-settings` đã tồn tại; M0a cấm đụng kit, bản chép `src/kit` chưa có) | Theo `IN_GAME_SETTINGS.md` |
| Âm | 71 id trong `src/audio/catalog.ts`, tất cả `silent: true`; phát âm từ bằng giọng trình duyệt | Không có file âm nào |
| Hiệu năng | M4, Medium, 1080p grey box: 16,8 ms TB (vsync), 56–62 draw call, 11,9k tam giác, CPU 1,4 ms | Chưa phải số đo (vsync); HN0 chưa chạy |

## 2. Camera thật: số liệu cho ý tưởng map

Camera nhìn về bắc từ phía nam, nghiêng **55°** dưới chân trời, FOV dọc **28°**, khung 40 × 26 m, `marginNdc` 0,03, `headroomM` 2,5 (`src/view/renderer.ts` `VIEW`, `rules.ts` `CAMERA`). Số từ `window.__ic.frame()` trên bản build:

| | 1280 × 720 | 1920 × 1080 |
|---|---|---|
| Mép xa sân (z −18) | y 56; x 174 → 1106 (932 px = 23,3 px/m) | y 84; x 261 → 1659 (1398 px = 35,0 px/m) |
| Trận Tâm (0; 0) | (640; 407) | (960; 611) |
| Mép gần (z +8) | y 613; x 26 → 1254 (30,7 px/m) | y 920; x 39 → 1881 (46,1 px/m) |
| Dải trên ngoài sân | 56 px | 84 px |
| Tam giác bên, rộng nhất ở mép xa | 174 px | 261 px (= 7,5 m đất ở tỉ lệ xa) |
| Bàn Quyết (DOM) che từ | y ≈ 620 | y ≈ 930 |
| Phép chiếu 1D theo z | y = (18,91 z + 407,4) / (1 − 0,01111 z) | y = (28,37 z + 611,1) / (1 − 0,01111 z) |

- **Trời:** mép trên khung ở 55° − 14° = **41° dưới chân trời**. Không có khung hình nào thấy trời. Ánh sáng "trời" chỉ hiện qua màu và bóng trên đất, sương, và viền ngoài sân.
- **Chiều cao bị cắt:** một vật cao h đặt ở z = −18 chiếm h × 0,57 × 35 px ở 1080p; dải trên trừ lề còn ~52 px → **h ≤ ~2,6 m** mới trọn. Ở z = −10 còn ~5,5 m, ở z = 0 không giới hạn thực tế.
- **Vật không được che:** đường đi từ hai cổng vào (hành lang đọc được), 6 ô cơ quan, vòng Kết Giới, Tâm nhãn (0; +3) phía nam Trận Tâm (gần người chơi, gần Bàn Quyết).
- **Thứ bậc độ sáng (đề xuất, đo sau khi có tranh):** hành lang thú đi sáng hơn đất quanh ≥ 1,3 lần độ chói; vùng Kết Giới và quanh Trận Tâm tối, yên hơn để thẻ chữ và số sát thương nổi; viền ngoài sân tối nhất; điểm sáng nhất là Trận Tâm (nguồn linh quang) rồi tới cổng (đèn lồng).
- **Màu dành cho tín hiệu (chốt từ đầu, canon §21.1):** đỏ `#FF4A4A` chỉ đòn địch; cam `#FFB020` khẩn; vàng kim `#FFC83A` tiền; xanh ngọc `#7FF5E0` sức gõ, Hộ thân, Kết Giới. Môi trường không dùng bốn màu này ở cường độ cao: đất và đá xám xanh, rêu xanh lục xám, gỗ nâu, ngói xám chàm; linh quang trắng ngà; đỏ son chỉ ở triện UI nhỏ.
- **Ánh sáng (một nguồn chính):** nắng xiên từ đông bắc (trên phải), thấp buổi sớm, ấm nhẹ; bóng đổ dài về tây nam để trụ và cổng có khối; sương lạnh xanh chàm ở viền và lớp thấp ngoài Kết Giới; linh quang Trận Tâm là nguồn phụ lạnh. Không nhiều điểm sáng rải.
- **Ảnh nền cho ChatGPT:** `legend-prep-1080.png` (lưới 5 m, cổng, trụ, ô, Kết Giới, cột 2,5 m). Trình duyệt trong app không đính kèm được: **anh đính kèm** khi tôi gửi brief.

## 3. Demo 1: bộ gốc (mỗi loại một mẫu, 8,5 rồi mới nhân rộng)

Mục tiêu: một trận Thanh Thạch Ải chơi được trên host chơi, không cờ URL, để anh chấm **từng chi tiết**: cảnh, nhân vật, quái, 5 chiêu + đánh nền, âm, UI. Không thêm hệ mới, không đổi luật sim (golden giữ nguyên).

### 3.1 Thứ tự (mỗi bước có cổng, bước sau chỉ chạy khi bước trước đạt)

| Bước | Làm gì | Cổng | Credit Tripo |
|---|---|---|---|
| 0 | Anh chốt Q1–Q6; cài Blender; chạy `ic-bench` trên Mac (HN0 thật); sửa host phục vụ `/vocabulary/` | Số đo HN0 ghi vào canon §20.4; bậc mặc định có cơ sở | 0 |
| 1 | **Bảng tham chiếu và tờ chuẩn chất liệu**: 1 ảnh "material sheet" (đá lát, rêu, gỗ, ngói, lụa, thép kiếm, linh quang) + 1 ảnh **ý tưởng map 1** theo camera thật (ChatGPT duyệt, Firefly vẽ đè ảnh nền có lưới) | Hai giám khảo ≥ 8,5 cho tờ chuẩn và ý tưởng map | 0 |
| 2 | **Ba model mẫu** (canon §21.2): Kiếm tu nữ, Phong Lang, Thiết Bối Lang Vương. Ảnh nguồn Firefly theo tờ chuẩn (hoặc ảnh Codex nếu qua chấm) → chấm ≥ 8,5 → `--dry-run` → dựng **một** (Phong Lang, rẻ nhất để kiểm quy trình, thử `rig` Tripo) → kiểm tam giác, map, vòng quay → hai model còn lại. Song song: thử dùng lại `blight-wolf`, `tusk-boar`, `kamaitachi` (một ngày) | Anh duyệt dáng và chuyển động của 3 mẫu (không chuyển động cứng); giám khảo ≥ 8,5 trong bản build | 3 × 40 = 120 (+ rig nếu Tripo tính riêng; sẽ dry-run và báo trước) |
| 3 | **Map 1**: đất nướng từ ô PBR (ambientCG CC0) + lớp vẽ Firefly, 8 decal, viền ngoài sân 3 lớp vẽ từ trên xuống, HDRI Poly Haven cho IBL (không thấy trời nên chỉ lấy ánh sáng), sương, hậu kỳ theo luật bloom; cổng, Trận Tâm, Trận Trụ, 3 cơ quan, phi kiếm qua Tripo | Giám khảo ≥ 8,5 ở 720 và 1080 trên host chơi; `ic-camera-frame` đủ 4 góc, 2 cổng, đường trời | 8 × 40 = 320 (cổng, Trận Tâm, Trận Trụ, Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng, phi kiếm Thanh Phong, đá vôi) |
| 4 | **Bốn họ thú còn lại + Lang Đầu Đàn** (hoặc bản dùng lại nếu bước 2 đạt), tinh anh bằng cỡ và chất liệu, không model mới | ≥ 8,5 ở cỡ chơi; bầy đọc thành khối ≥ 60 px | tối đa 4 × 40 = 160 (tướng dùng GLB sói, cỡ và hào quang) |
| 5 | **VFX** 5 chiêu + đánh nền + báo đòn + trúng, chết + Trận Tâm, Kết Giới, Hộ thân (§6), tờ khung trước/sau 720 và 1080 | ≥ 8,5; "chữ thành chiêu" và hiệu ứng gõ (hệ chung) ≥ 9 | 0 |
| 6 | **Âm** 26 id của demo (§5) qua Firefly SFX hoặc Audio Lab, chấm L1–L6, Bảng Nghe của anh; nhạc giữ ải 1 bản 4 lớp | Anh nghe mù ≥ 8,5; tiếng phím dùng bộ chung (≥ 9 đã có) | 0 |
| 7 | **UI**: màn tựa, khung Bàn Quyết, HUD, thẻ đợt, cửa hàng, Thu Hoạch, menu, bánh răng và loa (kit quick-settings, chép qua sync kit ở M0b) | ≥ 8,5 chấm trong game, icon ở 28–32 px | 0 |
| 8 | Chấm toàn bộ trong bản build, changelog, `media:push` (báo session điều phối trước) | Hai giám khảo ≥ 8,5 mọi phần; anh chơi thử | — |

Tổng credit demo: **≤ 600** của 970 (còn ~370 cho làm lại). Trước lần tiêu đầu tiên tôi gửi anh danh sách và tổng như luật.

### 3.2 Bối cảnh tu tiên phải "đúng" (để giám khảo và prompt cùng hiểu)

- **Thanh Thạch Ải**: sân đá vôi lát phẳng trên một vai núi, giữa hẻm đá vôi dựng đứng, biển mây dưới chân; sơn môn ở phía nam (sau lưng camera, chỉ thấy bậc đá và lan can ở mép gần). Chất Việt: đá vôi xám xanh kiểu Ninh Bình – Hà Giang, tùng cổ, sương chàm, lụa và giấy dó, hoa văn mây – hạc; **không** cầu chữ Hán, không đèn lồng đỏ kiểu phố, không ngói vàng cung đình.
- **Phe ta**: trắng ngà, lam chàm, vàng nhạt viền; linh quang trắng ngà; kiếm Thanh Phong thép xanh nhạt. Cao quý, kín đáo (D47).
- **Phe địch**: linh thú nhiễm trọc khí: lông xám tro, da đá, vân mực đen loang, mắt sáng xám tím; tinh anh thêm chất liệu (đá, thép, ngọc lục) và hào quang; Vương giáp đá đen thép bối. Trúng đòn là vệt mực, chết là khói mực và đốm linh quang, **không máu**.
- **Chiêu Kiếm (hệ Kim)**: thép sáng lạnh, vệt trắng xanh, viền vàng kim rất mảnh; "chữ thành chiêu" là nét thư pháp xanh ngọc bay vào tay. Đòn địch đỏ. Lôi Phù Trụ tím chàm điện; Phong Ấn Võng vòng triện vàng nhạt; Kiếm Thung thép xám mọc từ đất.

## 4. Danh sách 2D (Firefly Image 5; chỉ model Adobe)

### 4.1 Chuẩn chung cho mọi prompt (viết một lần, dán vào mọi prompt)

- Kiểu: painterly-realistic, vật liệu thật (PBR nhìn thấy: đá có vân và rêu, gỗ có thớ, ngói có lớp, lụa có bóng mềm), ánh sáng chính từ trên phải 45°, không bóng đổ xuống nền, **nền khóa phẳng một màu** (`#00FF00` cho vật, ảnh cảnh thì không), lề ≥ 8 %, một khối liền, chân phẳng, góc ba phần tư 30–35° nhìn từ trên 30° (vật đứng dùng khung dọc 3:4). Bảng màu §3.2. Prompt ≤ 1024 ký tự. Không chữ, không logo, không hiệu ứng trong ảnh nguồn 3D.
- Sau khi tạo: script kiểm khung (lề, một khối, bóng), nới nền nếu thiếu lề, khử ám xanh chỉ trên vật; đặt tên `<id>.v<n>-try<k>.png`, giữ prompt cạnh ảnh.
- Chấm: hai giám khảo mù, nhãn A/B/C, mức thị trường + mức hợp Tripo; icon và khung UI chấm ở cỡ thật trong game.

### 4.2 Demo 1

| Id | Món | Khổ | Chấm ở | Ghi chú |
|---|---|---|---|---|
| `refs/material-sheet` | Tờ chuẩn chất liệu (đá lát, rêu, gỗ, ngói, lụa, thép, linh quang) | 2048² | tờ | Bước 1; mọi ảnh sau trích chuẩn từ đây |
| `concept/map1-camera` | Ý tưởng map 1 vẽ đè ảnh nền có lưới (ChatGPT duyệt) | 1920 × 1080 | tờ | Bước 1 |
| `ground/thanh-thach/{lat-da,lat-reu,soi,co-nui,da-voi,bac-da}` | 6 ô đất lặp liền mép; nền từ ambientCG, Firefly chỉ vẽ lớp phủ vết trận và rêu | 2048² | trong game 720/1080 | 46 px/m gần, 35 px/m xa → 2048 px cho 8 m là dư |
| `decals/thanh-thach/{muc-loang,nut,reu-dom,la-tung,vong-tran,vet-cao,hoa-dai,suong}` | 8 decal nền trong | 1024² | trong game | Phá lặp |
| `backdrops/rim-{far,mid,near}` | 3 lớp viền ngoài sân **nhìn từ trên**: biển mây, đỉnh vách đá vôi và tùng, sương gần | 4096 × 1024, liền mép | trong game | Chỉ hiện ở dải 84 px và hai tam giác bên |
| `foliage/{co-nui,duong-xi,truc,hoa-dai,tung-non,reu-da}` | 6 thẻ cỏ bụi nền trong | 1024² | trong game | Tiền cảnh thưa ở mép gần và hai bên |
| `ui/title-key-art` | Tranh màn tựa (tên theo Q3) | 1920 × 1080 | màn tựa | Chuẩn D47; Kiếm tu trước Thanh Thạch Ải |
| `ui/frames/{ban-quyet,hud-bars,wave-card,shop,results,menu,panel-settings,panel-sound}` | 8 khung 9-slice có alpha, lụa và giấy dó viền chàm, triện đỏ son nhỏ | 512–1024 | trong game 720/1080 | Không chữ trong ảnh |
| `ui/icons/skills/{phi-kiem,ngu-kiem-quyet,nhat-tuyen,hoi-kiem-ho-than,luu-quang-bo,lac-kiem-tran,thien-ha-kiem-vu,kiem-tam,tich-kiem}` | 9 icon chiêu | 256², đọc ở 28–32 px | Bàn Quyết 28–32 px | Bóng đậm, 1 ý một icon |
| `ui/icons/{dan-phu ×3, co-quan ×3, tien ×3, settings, sound, sound-muted}` | 12 icon | 256² | HUD 24–32 px | Vàng kim chỉ cho tiền |
| `vfx/tex/*` | 14 kết cấu (§6) | 512²/1024², alpha | trong game | Firefly + Unity Labs CC0 (khói, lửa) |

### 4.3 Ảnh nguồn 3D cho demo (gửi Tripo; theo §7)

Kiếm tu nữ (trước, sau; tay mở 30°, chi tiết gom), Phong Lang (ba phần tư + trước), Thiết Bối Lang Vương (ba phần tư + trước), Thạch Thử, Hỏa Nha (trên và ba phần tư, cánh mở), Nham Viên, Thiết Giáp Trư, cổng ải, Trận Tâm, Trận Trụ, Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng, phi kiếm Thanh Phong (trên, cạnh), đá vôi. Ảnh Codex hiện có của cùng món đi chấm cùng lô; cái nào đạt thì dùng.

### 4.4 Sau demo (chỉ khi demo đạt)

Thổ thể nam/nữ và trượng đá, bot Đạo Đồng, tinh anh (không model mới), Đằng Thử, Khê Viên, Mê Vụ Trận, tùng cổ, Hậu Thổ Ấn, 7 icon Thổ thể, 6 icon Đạo Quả, 2 icon cảnh giới, Sơn Môn 1 nền + 4 điểm, Tĩnh Tu 10 ảnh, 8 nhân vật roster còn lại (D49). Danh sách gốc: [`art-requests/IMAGE_LIST.md`](art-requests/IMAGE_LIST.md).

## 5. Danh sách âm thanh (theo `AUDIO_PIPELINE.md`, canon §22, Q6)

Nguồn: **Firefly Generate Sound Effects** (model Adobe, prompt + nhịp giọng) cho tiếng hành động; **Audio Lab** (Stable Audio 3, anh đã có điều kiện dùng) và mẫu CC0 (VCSL: đàn tranh, sáo, trống khung; VSCO-2-CE: cello) cho nhạc và lớp nền; Freesound CC0 (đọc giấy phép từng trang) cho tiếng thật (gió núi, đá lăn, sói). Mọi id: 4 phần chuẩn bị – phát – thân – đuôi vang hẻm núi; cỡ âm theo cỡ hành động; cấm pop, thump trần, đồ chơi. Bus và ưu tiên theo canon §22. Tiếng phím: **bộ Audio Lab chung** (5 hồ sơ, mức 9), không tạo mới. Giọng đọc từ: giữ TTS trình duyệt ở demo (luật §6.2 đuôi thấp áp cho âm sau từ).

### 5.1 Demo 1 (26 id)

| Nhóm | Id | Cỡ | Ghi chú |
|---|---|---|---|
| Gõ (3) | `type.word-lock` (chốt từ, nét thư pháp bay), `type.word-fizzle` (Cast hụt), `type.word-flash` (Chớp) | nhỏ | âm sau từ ~1,5 s một lần: đuôi dưới 1 kHz |
| Kiếm (8) | `kiem.auto` (phi kiếm rời tay), `kiem.volley` (băng 3 kiếm), `kiem.line` (Nhất Tuyến), `kiem.ward-up`, `kiem.ward-block`, `kiem.zone-loop` (Lạc Kiếm Trận, vòng lặp 5 s), `kiem.ultimate-charge`, `kiem.ultimate-rain` (3 loạt) | vừa → lớn | thép lạnh, gió xé; ultimate có trọng lượng |
| Trúng, chết (4) | `hit.ink-small`, `hit.ink-medium`, `death.ink-puff` (gộp theo bầy, chuỗi "tan khói"), `death.elite` | nhỏ → vừa | không mỗi con một tiếng |
| Thú (5) | `beast.rat-skitter-loop` (lớp triều 3 tầng), `beast.wolf-howl` (Tru Đàn), `beast.crow-dive`, `beast.ape-throw`, `beast.boar-charge` (báo + húc) | vừa | báo đòn có âm riêng trước 1,2 s |
| Trận pháp (3) | `form.heart-hum-loop` (Trận Tâm), `form.heart-hit` (Trận Lực mất), `form.barrier-pulse` (Kết Giới chậm thú) | vừa | Trận Lực < 30 % có lớp khẩn |
| UI (3) | `ui.wave-start` (thẻ đợt, không chuông chùa), `ui.panel`, `ui.buy` | nhỏ | |
| Nhạc (1 bản, 4 lớp) | `music.hold` (nền – đợt – đông – nguy; cùng BPM, đàn tranh, sáo trúc, trống, cello) | | không tụng, không nhạc cụ Trung, Nhật dán nhãn Việt |

### 5.2 Sau demo

Thú Vương 6 id (gầm chuyển pha, Vồ Xé, Thiết Bối Xung nạp và húc, Gọi Đàn, chết), Lôi Phù Trụ, Phong Ấn Võng, Kiếm Thung (3), đan phù (3), Thu Hoạch và Sổ Từ (2), Thẻ Ôn (2), nhạc Vương 3 stem, Tĩnh Tu 5 + nhạc nền; đủ ~55 id của canon §22 và 3 bản nhạc. Danh sách chính thức ghi vào `games/immortality-cultivation/docs/audio/SOUND_LIST.md` khi bắt đầu bước 6.

## 6. Danh sách VFX (năm pha theo `VFX_STANDARD.md` §3; chỉ ở view, không đổi tick sim)

| Hành động | Bậc | A gồng | R ở người ra đòn | T bay | I trúng | F dư âm |
|---|---|---|---|---|---|---|
| Phím gõ (hệ chung, ≥ 9) | T0 | — | chữ nảy ở Bàn Quyết, đốm linh quang ở tay | đốm bay thẻ → tay | — | mức nạp ở tay lớn dần |
| Chữ thành chiêu (chốt từ) | T0–T1 | — | nét thư pháp xanh ngọc bật khỏi thẻ, bay 0,15 s vào tay (≤ 50 ms sau phím cuối) | nét bay | lóe ở tay | — |
| Phi Kiếm (đánh nền) | T1 | quầng tụ nhỏ ở tay | lóe tuổi 0, giật tay | kiếm 3D + ribbon mảnh | lóe, vệt mực, 2 tia | — |
| Ngự Kiếm Quyết (ô 1, băng 3 kiếm, tick +6/+36/+66) | T1–T2 | 3 kiếm hiện quanh vai theo chữ | lóe, nhún vai | 3 ribbon, lõi HDR mảnh | lóe, vệt mực, phản ứng thân, số | khói mực nhỏ |
| Nhất Tuyến Xuyên Vân (ô 2, đường 14 × 1,2 m, +12) | T3 | vòng phép dưới chân, than hút vào | nón fresnel, camera kick nhỏ | một lưỡi dài, vệt trắng xanh viền vàng mảnh | lóe theo tuyến, vệt mực từng thú, dừng hình 35 ms | decal rãnh mực 4 s |
| Hồi Kiếm Hộ Thân (ô 3, `ward` r 2 m, 5 s, 3 lần đỡ) | T3 | — | vòng triện dựng, 3 kiếm quay | — | mỗi lần đỡ: vòm nửa cầu lóe, tia | vòng mờ dần, kiếm rơi tan |
| Lạc Kiếm Trận (ô 4, vùng r 3 m, 5 s) | T3 | vòng phép tại đích | kiếm cắm từ trời xuống | mưa kiếm thưa | mỗi nhịp 30 tick: lóe nhỏ, vệt mực | decal vòng kiếm cắm 4 s, khói |
| Thiên Hà Kiếm Vũ (ô 5, 3 loạt +30/+75/+120, 150/300/500 kiếm) | T5 | viền màn ám xanh ngọc ≤ 20 %, kiếm tụ quanh người | cột sáng, vòng đất, camera, biến hình nhẹ | "vạn kiếm" 3D instanced hội về vùng r 6 m | vòm, đá vụn, tia, đèn, dừng hình 70 ms, chớp ≤ 3 khung | decal lớn 7 s, khói mực, than |
| Đòn thú (cắn, bổ nhào, ném, húc) | — | báo đỏ trên đất ≥ 1,2 s, ánh tụ ở thú | vệt quét hoặc lóe đỏ | đá ném, vệt bổ nhào | ở nạn nhân: lóe đỏ, rung nhỏ, Trận Lực lóe | — |
| Thú chết | T2 (thường), T3 (tinh anh), T4 (tướng, Vương) | — | — | — | thân lóe, tan theo nhiễu có viền | khói mực, đốm linh quang bay về HUD |
| Trận Tâm, Kết Giới, Tâm nhãn | nền | — | — | — | — | hơi thở linh quang; vòng Kết Giới shader; Trận Lực < 30 % đổi cam khẩn |
| Cơ quan (Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng) | T2–T3 | trạng thái sẵn sàng (rune mờ thở) | vừa kích: lóe, nhún | xích sét, lưới triện | lóe, tia theo chất liệu | dấu nạp lại (vòng đồng hồ) |

Luật bloom (bài học §5): chỉ lõi HDR 3–6 mảnh được bloom, quầng ≤ 0,9; strength 0,4–0,5, radius 0,1–0,15; tone map Neutral (canon §21.1). Khói trộn thường, làm tối. Mỗi hiệu ứng khai `reduced: keep | soften | drop`. Kết cấu: vệt kiếm, quầng, lá kiếm sprite, vết chém, khói mực (Unity Labs CC0 làm gốc), bắn mực, tia, bụi, sét xích, vòng triện, vòng Kết Giới, vạch báo đỏ sọc, nét thư pháp, xoáy Chân Nguyên: **14** cho demo (sau demo: sương mê, sét Thiên Kiếp, hào quang tinh anh, Lôi Kiếp).

## 7. Danh sách model 3D (Tripo API; chỉ khi ảnh nguồn ≥ 8,5 từ hai giám khảo)

Lệnh đã kiểm `--dry-run` (không tốn credit): `tripo make <ảnh> --for game-pc --then rig --dry-run` → chuỗi `image-to-model` (v3.1-20260211, texture, pbr, `texture_quality=detailed`) + `rig` (v3.0-20260909), đầu ra FBX + GLTF. Dựng thật: `tripo make <ảnh> --model v3.1-20260211 -p texture_quality=detailed -p pbr=true -p face_limit=<bảng> -o <thư mục tạm> --name <tên>` (thêm `--then rig` cho nhân vật và thú nếu bước 2 cho thấy rig Tripo dùng được). ~40 credit một model; geometry `standard` (detailed +20 chỉ cho Kiếm tu nếu lần đầu chưa đạt). Ghi mỗi lần tiêu vào [`../TRIPO_TODO.md`](../TRIPO_TODO.md), mục Tu Tiên riêng.

Ảnh nguồn (luật chung): một khối liền, chân phẳng, góc ba phần tư 30–35° nhìn từ trên 30°, nền khóa phẳng, không bóng, lề ≥ 6–8 %, cùng chuẩn §4.1; mặt trên chăm kỹ (camera 55°). Thú và nhân vật thêm góc trước cho `multiview-to-model` (2–4 ảnh).

| # | Model | Loại | `face_limit` | Kho sẵn có? | Ảnh nguồn | Demo | Ghi chú |
|---|---|---|---|---|---|---|---|
| 1 | Kiếm tu nữ (nhân vật chính) | nhân vật, rig biped, clip Idle, Run, Cast_Short, Cast_Heavy, Hit, Down | 50.000 | Không (hero kit là rồng bay) | Firefly theo chân dung A, trước + sau, tay mở 30° | ✔ bước 2 | Clip: rig Tripo hoặc Mesh2Motion người 66 xương (CC0), chấm theo mức 9 |
| 2 | Phong Lang (sói, Nhỏ) | quái, VAT | 30.000 | **`blight-wolf` DH** (gốc 5.637 mặt, B/N/MR 2048, không rig): thử đổi texture trước | ảnh Codex `beasts/phong-lang*.png` đi chấm; Firefly nếu trượt | ✔ bước 2 | Tinh anh Cuồng, Hồi Nguyên: cùng GLB ×1,25, chất liệu, hào quang |
| 3 | Thiết Bối Lang Vương (Thú Vương) | boss, rig, 8–10 clip | 50.000 | Không có boss sói nào | Codex `kings/*` đi chấm; Firefly | ✔ bước 2 | ≤ 45k tam giác theo canon §21.3 → đặt 45.000 |
| 4 | Thạch Thử (chuột đá, bầy) | quái, VAT, LOD | 25.000 | **`kamaitachi` WW** (chồn, 5.873) thử | Codex `beasts/thach-thu*` | ✔ bước 4 | Bầy ≥ 20 px, cụm ≥ 60 px; impostor nếu HN0 bắt |
| 5 | Hỏa Nha (quạ, bay) | quái, VAT | 25.000 | `dai-bang-tinh` WW (đại bàng 35k) gượng: không dùng | Codex `beasts/hoa-nha*` (góc ngang chưa đạt) → Firefly | ✔ bước 4 | Cánh mở, nhìn từ trên là chính |
| 6 | Nham Viên (vượn đá, Vừa) | quái, VAT | 30.000 | Không (troll WW là người khổng lồ, dáng khác) | Codex `beasts/nham-vien*` | ✔ bước 4 | |
| 7 | Thiết Giáp Trư (lợn giáp, Vừa) | quái, VAT | 30.000 | **`tusk-boar` DH** (5.812) thử: thêm giáp bằng texture | Codex `beasts/thiet-giap-tru*` | ✔ bước 4 | Tinh anh Thiết Bì cùng GLB |
| 8 | Lang Đầu Đàn (thú tướng) | dùng GLB sói ×1,4, hào quang | — | = #2 | — | ✔ bước 4 | Không model mới (canon §21.2) |
| 9 | Cổng ải (×2 dùng chung) | công trình | 40.000 | Không | Codex `props/cong-ai.png` đi chấm (hiện cao, sẽ bị cắt: vẽ lại rộng, thấp, mái đẹp từ trên) | ✔ bước 3 | Phụ thuộc Q5 |
| 10 | Trận Tâm | công trình | 30.000 | Không | Codex `props/tran-tam.png` đi chấm | ✔ bước 3 | Mặt đĩa là mặt chính |
| 11 | Trận Trụ (×2) | công trình | 25.000 | Không | Codex `props/tran-tru.png` | ✔ bước 3 | Bản nứt bằng texture thứ hai |
| 12 | Kiếm Thung | cơ quan | 15.000 | Không | Codex `mechanisms/kiem-thung.png` | ✔ bước 3 | |
| 13 | Lôi Phù Trụ | cơ quan | 15.000 | Không | Codex `mechanisms/loi-phu-tru.png` | ✔ bước 3 | |
| 14 | Phong Ấn Võng | cơ quan | 15.000 | Không | Codex `mechanisms/phong-an-vong.png` | ✔ bước 3 | |
| 15 | Phi kiếm Thanh Phong (đánh nền, ô 1, vạn kiếm) | vật nhỏ | 12.000 (LOD 600 cho 500 kiếm instanced) | Không | Codex `treasures/thanh-phong-kiem*.png` | ✔ bước 3 | |
| 16 | Đá vôi (rải viền) | vật nhỏ | 12.000 | Poly Haven CC0 (quét thật) thay được | Codex `props/da-voi.png` | ✔ bước 3 | Ưu tiên CC0 nếu hợp chuẩn |
| 17 | Tùng cổ | prop lớn | 30.000 | Quaternius (QAL) hay Poly Haven thử trước | Codex `props/tung-co.png` | sau demo | |
| 18–21 | Thổ thể nam, nữ, trượng đá, bot Đạo Đồng | nhân vật | 50.000 | Không | phiếu 013 | sau demo | M1 |
| 22–24 | Mê Vụ Trận, Hậu Thổ Ấn, Đằng Thử (biến chủng: không model mới) | cơ quan, pháp bảo | 15.000 | — | Codex đã có | sau demo | |

Credit demo: #1–#16 trừ #8 và các bản dùng lại đạt → **tối đa 15 × 40 = 600**; nếu 3 bản dùng lại đạt: 480.

## 8. Câu hỏi gửi chủ dự án

1. Q1–Q6 ở §0.2 (ngôn ngữ, ai dựng model, tên game, chuẩn hình, camera, bảng tham chiếu).
2. Cho cài Blender trên Mac này (`brew install --cask blender`, ~300 MB, GPL, công cụ ngoài game).
3. Firefly: anh xác nhận trong tab Firefly có **Generate Sound Effects** và **Generate Soundtrack** (đều model Adobe) để tôi dùng cho §5; nếu không có Soundtrack thì nhạc đi Audio Lab + mẫu CC0.
4. Hai điểm canon tôi đề nghị sửa khi anh duyệt: D27 ("anh tạo model") → Claude qua Tripo API; §21.1 "vẻ thủy mặc" → chuẩn Q4 (thủy mặc giữ ở VFX và decal).

## 9. Việc tôi làm ngay sau khi anh chốt (không chờ thêm)

Bước 0 của §3.1: `ic-bench` trên Mac, kiểm host `/vocabulary/`, brief ChatGPT cho map 1 (kèm ảnh `legend-prep-1080.png` để anh đính kèm), tờ chuẩn chất liệu trên Firefly, bộ chấm mù cho 53 ảnh Codex.

## 10. Nguồn

- Số đo camera và cỡ thú: `games/immortality-cultivation/tmp/plan-2026-11-01/capture-{720,1080}.log` (từ `window.__ic.frame()`, `foeSizes()`, `perf()` trên bản build qua `src/kit/tools/cdp-run.mjs`, Chrome Mac, GPU "ANGLE Metal, Apple M4").
- Kho quái: [`../MONSTER_MODEL_INVENTORY.md`](../MONSTER_MODEL_INVENTORY.md) §3–4, §7; bản gốc ở `games/dragon-hold/art-src/3d/enemies/` và `games/typing-defense/art-src/3d/enemies/`.
- Nguồn miễn phí: [`../FREE_ASSET_SOURCES.md`](../FREE_ASSET_SOURCES.md) §3–8 (Poly Haven, ambientCG CC0; Unity Labs flipbook CC0; Quaternius QAL; three r170 `Sky`, `GroundedSkybox`, `SMAAPass`, `GTAOPass`; `three-custom-shader-material` MIT).
- Tripo: `tripo balance` = 970 (01/11 12:30), dry-run chuỗi `image-to-model` + `rig` ở trên.
- Ảnh nguồn hiện có: `games/immortality-cultivation/art-src/` (53 ảnh Codex 25/10, [`art-requests/IMAGE_LIST.md`](art-requests/IMAGE_LIST.md), nhận xét từng ảnh ở `art-src/README-m0b.md`).
