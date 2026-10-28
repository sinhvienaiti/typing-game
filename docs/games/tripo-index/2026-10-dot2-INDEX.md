# Ảnh gửi Tripo · đợt 2 (26/10/2026)

92 ảnh của 87 model Lời Gọi (bậc VS từ Codex 005a/005b, Draconis mới, Trại Lính). Cần gửi 86 model: Trại Lính không làm lại (mục "Không gửi Tripo"). Cùng cách làm đợt 1: tên thư mục là face limit, có rig hay không, 1 ảnh hay nhiều góc. Thiết lập chung: tách nền BẬT, texture HD + PBR BẬT, lưới tam giác.

- Tải GLB về `_GLB tải về/`. Không cần đổi tên: Claude tự ghép như đợt 1.
- "KHÔNG bấm rig (Claude rig sau)": tạo model, không bấm rig. "không rig": đồ vật, công trình, không cần xương.
- Cột "Ảnh" ghi tên file chính xác. Riêng ba model multiview (`loigoi_draconis_*`, `loigoi_dai-bang-tinh_*`, `loigoi_tre_*`) mỗi model có nhiều ảnh góc.
- **Không đưa thư mục này vào Git.** `.gitignore` của repo cha chưa loại `typing-game-handoff-2026-10-25/` (lúc kiểm 26/10: chưa track, có 420 PNG, 55 GLB). Đừng chạy `git add -A` hay `git add .`; nên thêm thư mục này vào `.gitignore`.

| Thư mục | Model |
|---|---:|
| face 10000 - KHÔNG bấm rig (Claude rig sau) - 1 ảnh | 2 |
| face 10000 - không rig - 1 ảnh | 21 |
| face 2000 - không rig - 1 ảnh | 20 |
| face 20000 - KHÔNG bấm rig (Claude rig sau) - multiview | 1 |
| face 30000 - KHÔNG bấm rig (Claude rig sau) - multiview | 2 |
| face 4000 - không rig - 1 ảnh | 23 |
| face 8000 - không rig - 1 ảnh | 17 |

**27/10, 23:05 (Claude):** đã kiểm lại cả 92 ảnh. Không thiếu file. Nền đều phẳng (lệch tối đa 5/255). Không vật nào chạm mép ảnh (sát nhất 7 px). Ảnh Trại Lính `loigoi_barracks.png` (không gửi) đã chuyển vào `_cu-khong-gui/`: mọi ảnh còn trong các thư mục `face …` đều gửi được.

## Ưu tiên (26/10/2026)

Xếp theo [luật duyệt ảnh và model](../../docs/games/ART_ACCEPTANCE.md) §3: làm P1 trước, rồi P2; P3 chờ kinh phí. Trong mỗi bảng, làm theo cột #.

- Game đang là bản vẽ 2D (1B, bản đồ 1 Đồng Cỏ Thác Bạc). Mốc kế tiếp là 1C: cảnh 3D của chính bản đồ này. **P1** là thứ game đang có, 1C phải vẽ, mà chưa có GLB: thiếu thì hiện hình tạm.
- **P2** là các bước sau 1C trong lộ trình (TK §26.2): cấp 2–3 và nhánh của 6 nhà bản đồ 1, tổ thợ, Tre, Đại Bàng Tinh, Mộc Tinh đầy đủ, ba nhà VS cấp 1. Ở 1C, cờ cấp `level-pennant` là dấu cấp duy nhất trên nhà, nên bộ cấp ở P2.
- **P3** là biến thể, trang trí, món của bản đồ 2–3 và món luật hiện tại không dùng.
- Mức ở đây khớp lượt chấm lại 26/10: mười hai ảnh nguồn đã chấm nằm ở P2 (K04, K10, K13, V18, V36, V37, V68, V69 = #14–16, #10, #26, #27, #36, #37; V14, V15, V34, V35 = #38–41) cũng ghi P2 ở `docs/games/ART_REPLACE_LATER.md`, `ART_FIX_QUEUE.md` và IMAGE_AUDIT §7.

| Mức | Model | Credit (30 mỗi model, chưa tính rig) |
|---|---:|---:|
| P1 | 7 | 210 |
| P2 | 41 | 1.230 |
| P3 | 38 | 1.140 |
| **Cộng** | **86** | **2.580** |

### P1: làm ngay

| # | Ảnh | Món | Lý do |
|---|---|---|---|
| 1 | `face 30000 - KHÔNG bấm rig (Claude rig sau) - multiview/loigoi_draconis_*.png` | Draconis Phượng Long | Tướng duy nhất của game; chưa có GLB nào. |
| 2 | `face 2000 - không rig - 1 ảnh/loigoi_fire-feather.png` | Lông lửa Draconis | Tối Thượng có trong truyện từ Ngày 3. |
| 3 | `face 4000 - không rig - 1 ảnh/loigoi_scaffold-bamboo.png` | Giàn tre | Mọi nhà đặt xuống là công trường do thợ xây làm, nâng cấp cũng vậy (TK 23: công trường là giàn tre). |
| 4 | `face 8000 - không rig - 1 ảnh/loigoi_cau-go.png` | Cầu gỗ | Bản đồ có suối và 2 cầu; người đi bộ chỉ qua suối ở đó. |
| 5 | `face 8000 - không rig - 1 ảnh/loigoi_vach-thac-bac.png` | Vách Thác Bạc | Khe Nứt (−10, −46): quái ra và Mộc Tinh trồi lên ở đây. |
| 6 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-tieu-axe.png` | Rìu · Chú Tiều | Dân chặt cây (luật gỗ 26/10); thiếu rìu thì không đọc ra việc chặt. |
| 7 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-ma-head.png` | Nón lá + bím tóc · Cô Mạ | Nông dân của Ruộng có từ Ngày 1. Thân thợ chung đã có; nón lá tách nông dân khỏi thợ xây khi nhìn từ camera cao. |

### P2: sau P1

| # | Ảnh | Món | Lý do |
|---|---|---|---|
| 1 | `face 8000 - không rig - 1 ảnh/loigoi_keep-kit-l2.png` | Lũy cấp 2 | Lũy cấp 2 mở Ngày 3. |
| 2 | `face 4000 - không rig - 1 ảnh/loigoi_keep-kit-l3.png` | Lũy cấp 3 | Lũy cấp 3 mở Ngày 5 (truyện tối đa cấp 3). |
| 3 | `face 4000 - không rig - 1 ảnh/loigoi_archer-kit-l2.png` | Tháp Cung cấp 2 | Nâng nhà mở Ngày 4; 1C chỉ có cờ cấp. |
| 4 | `face 4000 - không rig - 1 ảnh/loigoi_archer-kit-l3.png` | Tháp Cung cấp 3 | Như trên. |
| 5 | `face 4000 - không rig - 1 ảnh/loigoi_cannon-kit-l2.png` | Tháp Pháo cấp 2 | Như trên. |
| 6 | `face 4000 - không rig - 1 ảnh/loigoi_cannon-kit-l3.png` | Tháp Pháo cấp 3: cờ | Như trên. |
| 7 | `face 2000 - không rig - 1 ảnh/loigoi_cannon-barrel-l3.png` | Tháp Pháo cấp 3: nòng vằn | Như trên; nòng là model riêng. |
| 8 | `face 4000 - không rig - 1 ảnh/loigoi_gold-mine-kit-l2.png` | Mỏ Vàng cấp 2 | Như trên. |
| 9 | `face 4000 - không rig - 1 ảnh/loigoi_gold-mine-kit-l3.png` | Mỏ Vàng cấp 3 | Như trên. |
| 10 | `face 4000 - không rig - 1 ảnh/loigoi_farm-kit-l2.alpha.png` | Ruộng Lúa cấp 2 | Như trên. **Đã sửa 27/10 (Codex 017, Claude duyệt 8,5): gửi bản `.alpha.png` này.** |
| 11 | `face 4000 - không rig - 1 ảnh/loigoi_farm-kit-l3.png` | Ruộng Lúa cấp 3 | Như trên. |
| 12 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-tieu-head.png` | Khăn ô + râu · Chú Tiều | Đầu cho dân chặt cây; rìu (P1) đã đủ để đọc việc. |
| 13 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-ma-seedlings.png` | Bó mạ · Cô Mạ | Đồ nghề nông dân; nón lá (P1) đã đủ để nhận ra. |
| 14 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-en-bow.png` | Cung ngắn · Chị Én | Tổ thợ Tháp Cung; đầu đã có GLB từ đợt 1. Tổ thợ có thoại ở bước 2 "Sống". |
| 15 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-lua-shot.png` | Quả đạn · Cậu Lửa | Tổ thợ Tháp Pháo; đầu đã có. |
| 16 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-sam-drumstick.png` | Dùi trống · Đội trưởng Sấm | Tổ thợ Trại Lính; đầu đã có. |
| 17 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-sam-vest.png` | Áo giáp lá tre · Đội trưởng Sấm | Như trên. |
| 18 | `face 2000 - không rig - 1 ảnh/loigoi_linh-giao-dai-spear.png` | Giáo dài | Thân Lính Giáo Dài có từ đợt 1, còn thiếu giáo (GLB duy nhất đợt 1 chưa có). |
| 19 | `face 20000 - KHÔNG bấm rig (Claude rig sau) - multiview/loigoi_tre_*.png` | Tướng Tre | Tướng thứ hai (VS); búa và ná của Tre đã có GLB từ đợt 1. |
| 20 | `face 2000 - không rig - 1 ảnh/loigoi_pebble.png` | Viên ná của Tre | Đạn của Tre. |
| 21 | `face 4000 - không rig - 1 ảnh/loigoi_rao-tre.png` | Rào Tre | Kỹ năng của Tre; nhánh Xưởng Rào dùng chung. |
| 22 | `face 10000 - không rig - 1 ảnh/loigoi_archer-en-bao.png` | Cung, nhánh Én Bão | Nhánh (bước 4); bản vẽ đầu tiên, thưởng Mộc Tinh bản đồ 1. |
| 23 | `face 10000 - không rig - 1 ảnh/loigoi_archer-than-tien.png` | Cung, nhánh Thần Tiễn | Như trên. |
| 24 | `face 10000 - không rig - 1 ảnh/loigoi_farm-bac-thang.png` | Ruộng, nhánh Bậc Thang | Nhánh nhà bản đồ 1 (thưởng 100 từ đã thuộc). |
| 25 | `face 10000 - không rig - 1 ảnh/loigoi_farm-chuong-trau.png` | Ruộng, nhánh Chuồng Trâu | Như trên; trâu đã có GLB. |
| 26 | `face 10000 - không rig - 1 ảnh/loigoi_gold-mine-ham-sau.png` | Mỏ, nhánh Hầm Sâu | Nhánh nhà bản đồ 1 (thưởng 100 từ đã thuộc). Ảnh tạm chấp nhận 8 (V36), gửi như hiện có. |
| 27 | `face 10000 - không rig - 1 ảnh/loigoi_gold-mine-lo-duc-tien.png` | Mỏ, nhánh Lò Đúc Tiền | Như trên. **Đã vẽ lại 27/10 (Codex 020c, lượt 3): lò nguội, thỏi vàng lì, không vùng phát sáng; Codex 8,5, Claude 8,5. Gửi được.** Ảnh lò còn sáng ở `_cu-khong-gui/`. |
| 28 | `face 10000 - không rig - 1 ảnh/loigoi_cannon-coi-lon.png` | Pháo, nhánh Cối Lớn | Nhánh nhà bản đồ 1 (thưởng 12 Sao). |
| 29 | `face 10000 - không rig - 1 ảnh/loigoi_cannon-vac-lua.png` | Pháo, nhánh Vạc Lửa | Như trên. |
| 30 | `face 10000 - không rig - 1 ảnh/loigoi_lumber.png` | Trại Gỗ cấp 1 | Nhà VS; game đã có Gỗ và dân chặt cây. |
| 31 | `face 10000 - không rig - 1 ảnh/loigoi_scribe.png` | Tháp Thư Pháp cấp 1 | Nhà VS, tháp thứ ba. |
| 32 | `face 10000 - không rig - 1 ảnh/loigoi_infirmary.png` | Nhà Thuốc cấp 1 | Nhà VS. |
| 33 | `face 8000 - không rig - 1 ảnh/loigoi_choi-canh-doi.png` | Chòi canh trên đồi | Đồi Cầu Vồng của bản đồ 1 (+10 % tầm); bản đồ hiện tại chưa có đồi. |
| 34 | `face 8000 - không rig - 1 ảnh/loigoi_ruin-m.png` | Đổ nát cỡ M | Một mesh co giãn cho mọi cỡ tới khi có S, L, XL. Chỉ cần khi quái phá được nhà (1B chưa có). |
| 35 | `face 30000 - KHÔNG bấm rig (Claude rig sau) - multiview/loigoi_dai-bang-tinh_*.png` | Boss Đại Bàng Tinh | Boss bản đồ 2 (VS). |
| 36 | `face 2000 - không rig - 1 ảnh/loigoi_quill.png` | Lông Đại Bàng Tinh | Đòn pha 3 của Đại Bàng Tinh. |
| 37 | `face 2000 - không rig - 1 ảnh/loigoi_seed-drop.flat.png` | Hạt Mộc Tinh | Đòn pha 3 của Mộc Tinh đầy đủ (VS); Mộc Tinh nhỏ của 1B không dùng. **Đã sửa 27/10 (Codex 017, Claude duyệt 8,5): gửi bản `.flat.png` này.** |
| 38 | `face 4000 - không rig - 1 ảnh/loigoi_barracks-kit-l2.png` | Trại Lính cấp 2 | Như bộ cấp khác. Ảnh tạm chấp nhận 8 (V14): gửi như hiện có, nắn trong Blender sau (ghi chú dưới bảng). |
| 39 | `face 4000 - không rig - 1 ảnh/loigoi_barracks-kit-l3.png` | Trại Lính cấp 3 | Như trên. Ảnh tạm chấp nhận 8 (V15): gửi như hiện có, nắn trong Blender sau. |
| 40 | `face 10000 - KHÔNG bấm rig (Claude rig sau) - 1 ảnh/loigoi_barracks-khien-dong.png` | Trại Lính, nhánh Khiên Đồng | **Đã vẽ lại 27/10 (Codex 015c): 8, tạm chấp nhận. Gửi được.** Tháp hai tầng như Trại Lính đang dùng, mái ngói, rào ốp khiên đồng. Bản cũ (6,5) chuyển vào `_cu-khong-gui/`. |
| 41 | `face 10000 - KHÔNG bấm rig (Claude rig sau) - 1 ảnh/loigoi_barracks-giao-dai.png` | Trại Lính, nhánh Giáo Dài | **Đã vẽ lại 27/10 (Codex 020, lượt 2): cao 98 % tháp v2, bó giáo kín; Codex 8,5, Claude 8,5. Gửi được.** Bản 015c (7,5) ở `_cu-khong-gui/`. Tháp hai tầng, rào cọc cao, giá giáo, sàn tập. Bản cũ (5,5) chuyển vào `_cu-khong-gui/`. |

**Sửa trước khi gửi (P2 #10, #27, #37).** Ba ảnh này là ảnh Tạm chấp nhận (ART_REPLACE_LATER.md). Làm bước dưới đây theo `docs/games/ART_FIX_QUEUE.md` §5.1, ra file mới trong `games/typing-defense/art-src`, rồi gửi file mới đó thay cho ảnh trong thư mục này. Không sửa ảnh trong thư mục này.
- #10 V18 `kits/farm-kit-l2.png`: `key-alpha` khóa toàn ảnh (`--mode global --fuzz 25%`) để giữ viền cỏ trên đế; gửi bản `.alpha.png`.
- #27 V37 `branches/gold-mine-lo-duc-tien.png`: tô miệng lò và dòng vàng chảy màu than đỏ sẫm, không sáng (luật không ánh sáng).
- #37 V69 `projectiles/seed-drop.png`: `flat-bg` làm phẳng nền xanh; gửi bản `.flat.png`.

Các ảnh P2 gửi như hiện có (#40, #41 đã vẽ lại 27/10, ghi chú dưới); Tripo tự tách nền. K04, K10, K13, V68 (#14–16, #36) đạt 9–9,5; V36 (#26) tạm chấp nhận 8, không có cách sửa miễn phí; V14, V15 (#38, #39) tạm chấp nhận 8, nắn trong Blender sau khi có GLB.

**Bốn món Trại Lính (P2 #38–41): đã chấm 26/10.** Cả bốn ảnh vẽ theo `barracks.png` cũ: nhà dài thấp, model 1,8 m. Trại Lính đang dùng là bản cao (ảnh `barracks-v2.png`). Mái ngói cấp 3 làm cho mái dài cũ, chòi cấp 2 đứng ở sân sau mà rào mới không còn, hai nhánh thấp như nhà cũ. Theo ART_ACCEPTANCE §4, hai người chấm độc lập (thêm người thứ ba cho #39–41), so với `barracks-v2.png` và render `barracks.glb`:
- #38 V14 `kits/barracks-kit-l2.png`: **8, Tạm chấp nhận.** Gửi như hiện có (`flat-bg` trước là tùy chọn). Sau khi có GLB: thu nhỏ đều, đặt chòi vào dải sân phải trong rào `barracks.glb`, render ba góc rồi chấm lại (ART_FIX_QUEUE.md §5.2).
- #39 V15 `kits/barracks-kit-l3.png`: **8, Tạm chấp nhận.** Gửi như hiện có. Sau khi có GLB: chỉnh tỉ lệ từng trục cho mái ngói chụp kín mái rơm `barracks.glb` (nâng Z khoảng 15–25 %), khoét đáy nếu lộ, render ba góc rồi chấm lại (ART_FIX_QUEUE.md §5.1).
- #40 V34 và #41 V35, hai nhánh Trại Lính: bản 26/10 (6,5 và 5,5) vẽ theo nhà dài thấp cũ, chỉ cao khoảng nửa tháp đang dùng, nên đã vẽ lại một lần (Codex 015c, 27/10). Bản mới cao gần bằng tháp (79 % và 77 % cùng bề ngang chân): 8 và 7,5, tạm chấp nhận, ghi ở `docs/games/ART_REPLACE_LATER.md`. Ảnh trong thư mục này là bản mới.

### P3: chờ kinh phí

| # | Ảnh | Món | Lý do |
|---|---|---|---|
| 1 | `face 10000 - không rig - 1 ảnh/loigoi_farm-ao-ca.png` | Ruộng, skin Ao Cá | Skin bản đồ 2. |
| 2 | `face 10000 - không rig - 1 ảnh/loigoi_farm-nuong.png` | Ruộng, skin Nương | Skin bản đồ 3. |
| 3 | `face 4000 - không rig - 1 ảnh/loigoi_keep-kit-l4.png` | Lũy cấp 4 | Chỉ có ở hộp cát; truyện tối đa cấp 3. |
| 4 | `face 4000 - không rig - 1 ảnh/loigoi_lumber-kit-l2.png` | Trại Gỗ cấp 2 | Bộ cấp nhà VS; cờ cấp thay tạm. |
| 5 | `face 4000 - không rig - 1 ảnh/loigoi_lumber-kit-l3.png` | Trại Gỗ cấp 3 | Như trên. |
| 6 | `face 4000 - không rig - 1 ảnh/loigoi_scribe-kit-l2.png` | Tháp Thư Pháp cấp 2 | Như trên. |
| 7 | `face 4000 - không rig - 1 ảnh/loigoi_scribe-kit-l3.png` | Tháp Thư Pháp cấp 3: cọ lơ lửng | Như trên. |
| 8 | `face 4000 - không rig - 1 ảnh/loigoi_infirmary-kit-l2.png` | Nhà Thuốc cấp 2 | Như trên. |
| 9 | `face 4000 - không rig - 1 ảnh/loigoi_infirmary-kit-l3.png` | Nhà Thuốc cấp 3 | Như trên. |
| 10 | `face 4000 - không rig - 1 ảnh/loigoi_seal-dais-kit-l2.png` | Đài Ấn cấp 2 | Đài Ấn để VS bản đồ 2; GLB cấp 1 đã có. |
| 11 | `face 4000 - không rig - 1 ảnh/loigoi_seal-dais-kit-l3.png` | Đài Ấn cấp 3 | Như trên. |
| 12 | `face 10000 - không rig - 1 ảnh/loigoi_lumber-xuong-cua.png` | Trại Gỗ, nhánh Xưởng Cưa | Nhánh nhà VS, mở sau Thế giới 1 (thưởng Mộc Tinh bản đồ 3). |
| 13 | `face 10000 - không rig - 1 ảnh/loigoi_lumber-xuong-rao.png` | Trại Gỗ, nhánh Xưởng Rào | Như trên. |
| 14 | `face 10000 - không rig - 1 ảnh/loigoi_infirmary-vuon-thao-duoc.png` | Nhà Thuốc, nhánh Vườn Thảo Dược | Như trên. |
| 15 | `face 10000 - không rig - 1 ảnh/loigoi_infirmary-tram-cuu-thuong.png` | Nhà Thuốc, nhánh Trạm Cứu Thương | Như trên. |
| 16 | `face 10000 - không rig - 1 ảnh/loigoi_scribe-but-loi.png` | Thư Pháp, nhánh Bút Lôi | Nhánh nhà VS (thưởng Đại Bàng Tinh). |
| 17 | `face 10000 - không rig - 1 ảnh/loigoi_scribe-muc-bang.png` | Thư Pháp, nhánh Mực Băng | Như trên. |
| 18 | `face 10000 - không rig - 1 ảnh/loigoi_seal-dais-phong-an.png` | Đài Ấn, nhánh Phong Ấn | Như trên. |
| 19 | `face 10000 - không rig - 1 ảnh/loigoi_seal-dais-vang-am.png` | Đài Ấn, nhánh Vang Âm | Như trên. |
| 20 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-lang-head.png` | Búi tóc bạc · Bà Lang Thơm | Tổ thợ Nhà Thuốc; nhà chưa vào game. |
| 21 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-lang-basket.png` | Giỏ thảo dược · Bà Lang Thơm | Như trên. |
| 22 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-tro-head.png` | Tóc búi · Trò Mực | Tổ thợ Đài Ấn; nhà chưa vào game. |
| 23 | `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-tro-scroll.png` | Cuộn giấy · Trò Mực | Như trên. |
| 24 | `face 8000 - không rig - 1 ảnh/loigoi_ruin-s.png` | Đổ nát cỡ S | Cỡ thêm; `ruin-m` co giãn thay tạm. |
| 25 | `face 8000 - không rig - 1 ảnh/loigoi_ruin-l.png` | Đổ nát cỡ L | Như trên. |
| 26 | `face 8000 - không rig - 1 ảnh/loigoi_ruin-xl.png` | Đổ nát cỡ XL | Như trên (đổ nát riêng của Ruộng). |
| 27 | `face 8000 - không rig - 1 ảnh/loigoi_hai-dang.png` | Hải đăng | Mốc cảnh bản đồ 2. |
| 28 | `face 8000 - không rig - 1 ảnh/loigoi_cau-tau.png` | Cầu tàu | Như trên. |
| 29 | `face 8000 - không rig - 1 ảnh/loigoi_nha-rai-da.png` | Nhà Rái Đá trên cọc | Như trên. |
| 30 | `face 8000 - không rig - 1 ảnh/loigoi_them-da-trang.png` | Thềm Đá Trắng | Như trên. |
| 31 | `face 8000 - không rig - 1 ảnh/loigoi_cau-do.png` | Cầu Đỏ | Mốc cảnh bản đồ 3. |
| 32 | `face 8000 - không rig - 1 ảnh/loigoi_da-ke.png` | Đá Kê | Như trên. |
| 33 | `face 8000 - không rig - 1 ảnh/loigoi_goc-da-rong.png` | Gốc đa rỗng | Như trên. |
| 34 | `face 8000 - không rig - 1 ảnh/loigoi_re-vom.png` | Rễ khổng lồ uốn qua đường | Như trên. |
| 35 | `face 8000 - không rig - 1 ảnh/loigoi_thac-ho-sut.png` | Thác đổ vào Hố Sụt | Như trên. |
| 36 | `face 4000 - không rig - 1 ảnh/loigoi_cau-tre.png` | Cầu Tre | Tre chỉ bắc ở điểm đánh dấu bản đồ 3; bản đồ 1–2 không có lối tắt. |
| 37 | `face 2000 - không rig - 1 ảnh/loigoi_meteor.png` | Đá lửa (Mưa Đá Lửa) | Phép Chỉ huy (TK 16); chưa có trong kế hoạch dựng. |
| 38 | `face 2000 - không rig - 1 ảnh/loigoi_go-lan.png` | Gỗ Lăn | Dùng cho Bùng Nổ Trại Gỗ, mà Bùng Nổ đã bỏ từ 1A.6. |

### Không gửi Tripo

| Ảnh | Món | Lý do |
|---|---|---|
| `_cu-khong-gui/loigoi_barracks.png` | Trại Lính, bản cao (`barracks-v2.png`) | **Không làm lại.** GLB hiện có dựng từ chính ảnh này và đạt 9,5. |

**Trại Lính.** `games/typing-defense/art-src/3d/buildings/barracks.glb` đang có đã là bản Tripo dựng từ chính ảnh này (`loigoi_barracks.png` trùng md5 với `barracks-v2.png`). File tải về là `~/Downloads/td-tripo-2d/3D/wooden+fortress+3d+model2410.glb` (24/10, 08:50): cùng cỡ, chỉ khác 174 byte.

Chấm lại 26/10 (`docs/games/ART_ACCEPTANCE.md`): hai người chấm 9,5 và 9, **điểm 9,5/10, Đạt**, mức cần P2 (1C cần 6 nhà bậc P). Đạt thì dùng: không làm lại, không ghi danh sách thay sau. Nhận xét theo tiêu chí:

| Tiêu chí | Ghi chú |
|---|---|
| Đúng đề | Nhà trại hai tầng có sàn canh, rào ôm sát, trống trận, khiên, cổng, bục, như ảnh. |
| Đọc được trong game | Ở góc camera game và khi thu còn 1/4: mái rơm, vòng rào, trống đỏ vẫn rõ. |
| Hợp bộ | Cùng nét Văn Điền với Tháp Cung, Ruộng, Lũy. |
| Hình khối | Gọn, không vỡ. Sàn canh tầng 2 bị lấp kín thay vì để trống như ảnh, không phải lỗi. |
| Dùng được cho bước sau | 27.847 tam giác (giới hạn 10.000: preset giảm); cánh cổng dính rào (Blender tách nếu làm clip mở cổng); cao khoảng 4,2–4,9 m tùy cách đo vòng, chỉnh preset cho khớp đích 4,5–5 m. Lượt ưu tiên Tripo trước đó chấm 9 và trừ 1 điểm ở tiêu chí này. |

Việc còn lại không tốn credit, là của Claude (`docs/games/ART_FIX_QUEUE.md` §1): chạy lại preset `buildings/barracks` (bản trong `public/` vẫn là nhà thấp 1,8 m, dựng lúc 02:57 ngày 24/10, trước khi có GLB mới), sửa ảnh nguồn và `downloadedAs` trong `SOURCES.json` (còn ghi `barracks.png` và `thatched+hut+3d+model (1).glb`).

## Danh sách

| Ảnh | Món | Ghi chú |
|---|---|---|
| `_cu-khong-gui/loigoi_barracks.png` | Trại Lính, bản cao | không làm lại: GLB hiện có đạt 9,5; không gửi |
| `face 10000 - KHÔNG bấm rig (Claude rig sau) - 1 ảnh/loigoi_barracks-giao-dai.png` | Trại Lính, nhánh Giáo Dài | Vẽ lại lần 2 ngày 27/10 (Codex 020): 8,5, gửi được (P2 #41) |
| `face 10000 - KHÔNG bấm rig (Claude rig sau) - 1 ảnh/loigoi_barracks-khien-dong.png` | Trại Lính, nhánh Khiên Đồng | Vẽ lại 27/10: 8, gửi được (P2 #40) |
| `face 10000 - không rig - 1 ảnh/loigoi_archer-en-bao.png` | Cung, nhánh Én Bão |  |
| `face 10000 - không rig - 1 ảnh/loigoi_archer-than-tien.png` | Cung, nhánh Thần Tiễn |  |
| `face 10000 - không rig - 1 ảnh/loigoi_cannon-coi-lon.png` | Pháo, nhánh Cối Lớn |  |
| `face 10000 - không rig - 1 ảnh/loigoi_cannon-vac-lua.png` | Pháo, nhánh Vạc Lửa |  |
| `face 10000 - không rig - 1 ảnh/loigoi_farm-ao-ca.png` | Ruộng, skin Ao Cá |  |
| `face 10000 - không rig - 1 ảnh/loigoi_farm-bac-thang.png` | Ruộng, nhánh Bậc Thang |  |
| `face 10000 - không rig - 1 ảnh/loigoi_farm-chuong-trau.png` | Ruộng, nhánh Chuồng Trâu |  |
| `face 10000 - không rig - 1 ảnh/loigoi_farm-nuong.png` | Ruộng, skin Nương |  |
| `face 10000 - không rig - 1 ảnh/loigoi_gold-mine-ham-sau.png` | Mỏ, nhánh Hầm Sâu |  |
| `face 10000 - không rig - 1 ảnh/loigoi_gold-mine-lo-duc-tien.png` | Mỏ, nhánh Lò Đúc Tiền | vẽ lại lò nguội 27/10 (020c), gửi được |
| `face 10000 - không rig - 1 ảnh/loigoi_infirmary.png` | Nhà Thuốc cấp 1 |  |
| `face 10000 - không rig - 1 ảnh/loigoi_infirmary-tram-cuu-thuong.png` | Nhà Thuốc, nhánh Trạm Cứu Thương |  |
| `face 10000 - không rig - 1 ảnh/loigoi_infirmary-vuon-thao-duoc.png` | Nhà Thuốc, nhánh Vườn Thảo Dược |  |
| `face 10000 - không rig - 1 ảnh/loigoi_lumber.png` | Trại Gỗ cấp 1 |  |
| `face 10000 - không rig - 1 ảnh/loigoi_lumber-xuong-cua.png` | Trại Gỗ, nhánh Xưởng Cưa |  |
| `face 10000 - không rig - 1 ảnh/loigoi_lumber-xuong-rao.png` | Trại Gỗ, nhánh Xưởng Rào |  |
| `face 10000 - không rig - 1 ảnh/loigoi_scribe.png` | Tháp Thư Pháp cấp 1 |  |
| `face 10000 - không rig - 1 ảnh/loigoi_scribe-but-loi.png` | Thư Pháp, nhánh Bút Lôi |  |
| `face 10000 - không rig - 1 ảnh/loigoi_scribe-muc-bang.png` | Thư Pháp, nhánh Mực Băng |  |
| `face 10000 - không rig - 1 ảnh/loigoi_seal-dais-phong-an.png` | Đài Ấn, nhánh Phong Ấn |  |
| `face 10000 - không rig - 1 ảnh/loigoi_seal-dais-vang-am.png` | Đài Ấn, nhánh Vang Âm |  |
| `face 2000 - không rig - 1 ảnh/loigoi_cannon-barrel-l3.png` | Tháp Pháo cấp 3: nòng vằn |  |
| `face 2000 - không rig - 1 ảnh/loigoi_fire-feather.png` | Lông lửa Draconis |  |
| `face 2000 - không rig - 1 ảnh/loigoi_go-lan.png` | Gỗ Lăn |  |
| `face 2000 - không rig - 1 ảnh/loigoi_linh-giao-dai-spear.png` | Giáo dài |  |
| `face 2000 - không rig - 1 ảnh/loigoi_meteor.png` | Đá lửa (Mưa Đá Lửa) |  |
| `face 2000 - không rig - 1 ảnh/loigoi_pebble.png` | Viên ná của Tre |  |
| `face 2000 - không rig - 1 ảnh/loigoi_quill.png` | Lông Đại Bàng Tinh |  |
| `face 2000 - không rig - 1 ảnh/loigoi_seed-drop.flat.png` | Hạt Mộc Tinh | đã sửa 27/10, gửi được |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-en-bow.png` | Cung ngắn · Chị Én |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-lang-basket.png` | Giỏ thảo dược · Bà Lang Thơm |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-lang-head.png` | Búi tóc bạc · Bà Lang Thơm (Nhà Thuốc) |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-lua-shot.png` | Quả đạn vằn xanh ngọc · Cậu Lửa |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-ma-head.png` | Nón lá + bím tóc · Cô Mạ (Ruộng Lúa) |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-ma-seedlings.png` | Bó mạ xanh · Cô Mạ |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-sam-drumstick.png` | Dùi trống to (Blender nhân đôi) · Đội trưởng Sấm |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-sam-vest.png` | Áo giáp lá tre · Đội trưởng Sấm |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-tieu-axe.png` | Rìu · Chú Tiều |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-tieu-head.png` | Khăn ô nâu kem + râu đen ngắn · Chú Tiều (Trại Gỗ) |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-tro-head.png` | Tóc búi nhỏ buộc dây xám xanh · Trò Mực (Đài Ấn) |  |
| `face 2000 - không rig - 1 ảnh/loigoi_worker-kit-tro-scroll.png` | Cuộn giấy trắng · Trò Mực |  |
| `face 20000 - KHÔNG bấm rig (Claude rig sau) - multiview/loigoi_tre_*.png` | Tướng Tre, cô thợ mộc tre |  |
| `face 30000 - KHÔNG bấm rig (Claude rig sau) - multiview/loigoi_dai-bang-tinh_*.png` | Boss Đại Bàng Tinh |  |
| `face 30000 - KHÔNG bấm rig (Claude rig sau) - multiview/loigoi_draconis_*.png` | Draconis Phượng Long |  |
| `face 4000 - không rig - 1 ảnh/loigoi_archer-kit-l2.png` | Tháp Cung cấp 2 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_archer-kit-l3.png` | Tháp Cung cấp 3 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_barracks-kit-l2.png` | Trại Lính cấp 2 | Tạm chấp nhận 8: gửi như hiện có (P2 #38) |
| `face 4000 - không rig - 1 ảnh/loigoi_barracks-kit-l3.png` | Trại Lính cấp 3 | Tạm chấp nhận 8: gửi như hiện có (P2 #39) |
| `face 4000 - không rig - 1 ảnh/loigoi_cannon-kit-l2.png` | Tháp Pháo cấp 2 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_cannon-kit-l3.png` | Tháp Pháo cấp 3: cờ |  |
| `face 4000 - không rig - 1 ảnh/loigoi_cau-tre.png` | Cầu Tre |  |
| `face 4000 - không rig - 1 ảnh/loigoi_farm-kit-l2.alpha.png` | Ruộng Lúa cấp 2 | đã sửa 27/10, gửi được |
| `face 4000 - không rig - 1 ảnh/loigoi_farm-kit-l3.png` | Ruộng Lúa cấp 3 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_gold-mine-kit-l2.png` | Mỏ Vàng cấp 2 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_gold-mine-kit-l3.png` | Mỏ Vàng cấp 3 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_infirmary-kit-l2.png` | Nhà Thuốc cấp 2 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_infirmary-kit-l3.png` | Nhà Thuốc cấp 3 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_keep-kit-l3.png` | Lũy cấp 3 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_keep-kit-l4.png` | Lũy cấp 4 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_lumber-kit-l2.png` | Trại Gỗ cấp 2 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_lumber-kit-l3.png` | Trại Gỗ cấp 3 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_rao-tre.png` | Rào Tre |  |
| `face 4000 - không rig - 1 ảnh/loigoi_scaffold-bamboo.png` | Giàn tre |  |
| `face 4000 - không rig - 1 ảnh/loigoi_scribe-kit-l2.png` | Tháp Thư Pháp cấp 2 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_scribe-kit-l3.png` | Tháp Thư Pháp cấp 3: cọ lơ lửng |  |
| `face 4000 - không rig - 1 ảnh/loigoi_seal-dais-kit-l2.png` | Đài Ấn cấp 2 |  |
| `face 4000 - không rig - 1 ảnh/loigoi_seal-dais-kit-l3.png` | Đài Ấn cấp 3 |  |
| `face 8000 - không rig - 1 ảnh/loigoi_cau-do.png` | Cầu Đỏ |  |
| `face 8000 - không rig - 1 ảnh/loigoi_cau-go.png` | Cầu gỗ |  |
| `face 8000 - không rig - 1 ảnh/loigoi_cau-tau.png` | Cầu tàu |  |
| `face 8000 - không rig - 1 ảnh/loigoi_choi-canh-doi.png` | Chòi canh trên đồi |  |
| `face 8000 - không rig - 1 ảnh/loigoi_da-ke.png` | Đá Kê |  |
| `face 8000 - không rig - 1 ảnh/loigoi_goc-da-rong.png` | Gốc đa rỗng |  |
| `face 8000 - không rig - 1 ảnh/loigoi_hai-dang.png` | Hải đăng |  |
| `face 8000 - không rig - 1 ảnh/loigoi_keep-kit-l2.png` | Lũy cấp 2 |  |
| `face 8000 - không rig - 1 ảnh/loigoi_nha-rai-da.png` | Nhà Rái Đá trên cọc |  |
| `face 8000 - không rig - 1 ảnh/loigoi_re-vom.png` | Rễ khổng lồ uốn qua đường |  |
| `face 8000 - không rig - 1 ảnh/loigoi_ruin-l.png` | Đổ nát cỡ L |  |
| `face 8000 - không rig - 1 ảnh/loigoi_ruin-m.png` | Đổ nát cỡ M |  |
| `face 8000 - không rig - 1 ảnh/loigoi_ruin-s.png` | Đổ nát cỡ S |  |
| `face 8000 - không rig - 1 ảnh/loigoi_ruin-xl.png` | Đổ nát cỡ XL |  |
| `face 8000 - không rig - 1 ảnh/loigoi_thac-ho-sut.png` | Thác đổ vào Hố Sụt |  |
| `face 8000 - không rig - 1 ảnh/loigoi_them-da-trang.png` | Thềm Đá Trắng |  |
| `face 8000 - không rig - 1 ảnh/loigoi_vach-thac-bac.png` | Vách Thác Bạc |  |
