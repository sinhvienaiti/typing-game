# Danh sách ảnh 2D cần dựng 3D — mọi game (25/10/2026)

> **Phiếu 003 · Dành cho:** chủ dự án dựng model trong Tripo; Claude nhận GLB để chuẩn cỡ, rig và làm clip trong Blender.
> **Phạm vi:** Rồng Giữ Ải M0; phần Lời Gọi chưa có bản gốc hoặc cần làm lại, gồm bậc P và VS; bản gốc còn thiếu cho Tuyến Cuối S1; Tu Tiên Thủ Ải chờ canon.
> **Đường dẫn:** mọi đường dẫn đầy đủ trong bảng tính từ gốc `D:\typing-game`. Trạng thái “có” chỉ xác nhận file ảnh hiện diện trên máy, chưa thay cho duyệt mỹ thuật. Ảnh của phiếu 001–002 đang được bổ sung; đã kiểm tồn tại ảnh lúc 25/10/2026 04:14:12 +07:00.

## 1. Tóm tắt

**143 lượt dựng/làm lại**, gồm **142 model chưa có GLB gốc** và **1 bản làm lại Trại Lính** (giữ cùng id `barracks`). Không tính góc phụ thành model riêng; không dựng lại model đã có chỉ vì còn thiếu rig hoặc clip.

| Game / đợt | Tổng danh mục đối chiếu | Đưa vào lượt dựng này | Tripo Biped | Tripo Quadruped | Tự rig Blender | Không rig | Rig lai |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rồng Giữ Ải · M0 | 24 | 24 | 3 | 0 | 7 | 14 | 0 |
| Lời Gọi · P | 42, đã có 41 GLB gốc | 2: Draconis mới + Trại Lính làm lại | 0 | 0 | 2 | 0 | 0 |
| Lời Gọi · VS, đợt sau | 115, chưa có GLB gốc trong danh mục hiện tại | 115 | 0 | 0 | 16 | 99 | 0 |
| Tuyến Cuối · S1 | Dùng chung thư viện Space; chỉ đếm 2 bản gốc thiếu | 2 | 0 | 0 | 0 | 2 | 0 |
| Tu Tiên Thủ Ải | Chờ canon | Chưa chốt, không cộng | — | — | — | — | — |
| **Cộng lượt dựng** | | **143** | **3** | **0** | **25** | **115** | **0** |

- **Credit rig ước tính:** `3 × 20 = 60 credit`. Biped và Quadruped đều 20 credit/lần rig theo phiếu; Blender và không rig: 0 credit rig. Không có model rig lai trong lượt này. Nếu dùng rig lai về sau: Tripo rig thân (20 credit), Blender thêm xương đuôi/cánh/áo và clip; tính model đó vào số lần rig trả phí.
- **Giá tạo model Tripo:** **theo gói**; các nguồn không nêu giá cố định. 60 credit trên chỉ là rig, chưa gồm tạo model, làm lại hay tăng chất lượng.
- **Lời Gọi:** 157 model đã định danh = 42 P + 115 VS (45 model nhân vật/đồ gắn + 70 công trình/prop). 41 GLB P đang có đều hiện diện trên máy; không lấy `notMadeYet: {}` trong `SOURCES.json` làm bằng chứng rằng toàn bộ thiết kế đã đủ.
- **Tuyến Cuối:** hai ảnh Rainbow đã có, thiếu GLB gốc riêng. `rainbow-tank` còn dùng cho Đầu Đàn; không phát sinh model thứ ba. Tổ dùng `rainbow-carrier`, boss dùng `warden-rainbow`; cả hai đã có GLB gốc, không đưa vào lượt dựng.
- **Chưa định danh:** các thế giới sau, trang phục và nhóm “Sau” của TD mới là danh sách ý tưởng; chưa đủ id/ảnh/face limit để đưa vào thao tác Tripo. Xem §6.

### 1.1. Quy tắc rig của lượt này

1. **Tripo Biped:** chỉ E09, E11, U1 có dáng người tư thế A và bộ clip cơ bản phù hợp. Chọn preset theo hành động trong bảng; E11 cần đúng động tác bắn cung. Nếu thư viện không có clip đủ dùng hoặc rig hỏng: tải GLB không xương, chuyển cho Claude; không thử trả phí rig nhiều lần.
2. **Tự rig Blender:** trong Tripo vẫn tạo model nhưng **không bấm rig**, tải **GLB không xương**. Áp cho dáng lạ, cánh, nhiều chân, cắn/vồ/húc, nhân vật chữ ký/boss, clip riêng, hoặc bộ phận có khớp cử động. Nhân vật TD chibi và clip nghề/chiêu riêng được đưa sang pipeline Blender đã có.
3. **Không rig:** đồ tĩnh, đồ cầm gắn socket, đạn, cảnh. Di chuyển cả vật, gió, nhún, co giãn và VFX làm bằng runtime/shader. Hai quái Rainbow giữ cách vẽ instanced của S1, không thêm xương cho đám đông.
4. Face limit là mức **tạo ở Tripo**. Giảm tam giác khi chuẩn bị bản chạy trong game là bước sau. Riêng 6000 cho hai Rainbow là **đề xuất cho lượt dựng**, dựa vào `triangles: 6000` của preset Space, không phải thiết lập Tripo được đặc tả trong S1.

## 2. Thiết lập Tripo chung

Chép nguyên văn bảng §3.1 của [README Rồng Giữ Ải](dragon-lane/art-requests/m0/README.md#31-chung-giống-bộ-td):

| Mục | Chọn |
|---|---|
| Chế độ | Có 2 góc: **Multiview to 3D** theo cột "Ô ảnh" ở 3.2. Một ảnh: **Image to 3D** |
| Tách nền | Bật (nền xám nhạt `#E6E6E6`) |
| Texture | Bật, HD cao nhất của gói. **PBR** bật |
| Lưới | Tam giác (Quad tắt). Smart Low Poly tắt |
| Face limit | Theo bảng 3.2. Blender giảm số tam giác chạy trong game sau (quái đám đông 1.500–3.000, prop 800–3.000) |
| Rig | Theo bảng 3.2 |
| Clip Tripo | Quái thường: đúng **4 clip** Idle, Move, Attack, Death, chọn preset gần nghĩa nhất trong thư viện Tripo. Thiếu preset (cắn, vồ, húc, bay) thì bỏ trống: Blender làm (02 §7.2). Tướng G01: thêm Cast, Hit, Intro nếu có preset |
| Tải về | **GLB** (bản có xương nếu đã rig). Đổi tên đúng id |

Các số mục “3.2”, “02 §7.2” trong bản chép trên là số mục **của tài liệu nguồn**. Khi thao tác lượt này, lấy face limit, rig và clip từ từng dòng §3 dưới đây; luật chọn rig của phiếu thay cho cột rig cũ.

- Ảnh TD cũ dùng nền khóa màu; vẫn bật tách nền theo ảnh đã có, không đổi nền ảnh chỉ để giống Rồng. Màu nền `#E6E6E6` là quy định của bộ ảnh Rồng.
- Nhiều ảnh: mỗi ảnh vào một ô Front / Back / Left riêng, không ghép các góc vào một tấm. Ảnh phụ tùy chọn chỉ dùng khi đã có và khớp ảnh chính; không bắt buộc chờ nó để dùng Image to 3D.
- Bảng dùng tên clip runtime khi nguồn đã quy định. Các tên “Chờ / Kích / Thu gai / Ngắm / Bắn / Hồi / Lật sách” là **đề xuất giao Blender**, cần chốt khi tích hợp, không phải tên preset có sẵn trong Tripo.
- Rồng thông thường đủ bốn vai Idle, Move, Attack, Death; Walk/Run/Crawl/Fly là Move tương ứng. Ong Gai có thể dùng Hover cho Idle. G01 thêm Cast, Hit, Intro.
- Gai Chông và Lưới Phóng: chọn Blender theo luật bẫy có bộ phận cử động của phiếu; nguồn M0 cũ dùng shader/cả model. Đây là lựa chọn chuẩn bị asset, chưa thay đổi runtime. Bom Hạt Thông giữ shader vì không có khớp cơ khí.

## 3. Bảng nhóm theo face limit và cách rig

**Cách đọc:** cột ảnh ghi đầy đủ từng file; “chờ ảnh” không có nghĩa là đã gửi yêu cầu tạo ảnh mới. Bậc **VS** là đợt sau, làm sau P; mã `01-VS/…`, `02-VS/…` chỉ rõ file nguồn để tránh trùng mã. Cùng một id chỉ có một GLB đích.

### 3.1. 2000 · Tự rig Blender (2 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Lời Gọi · VS | 01-VS/VS2 · `chuon-chuon-tre` | Chuồn Chuồn Tre, bạn đồng hành của Tre | Image = `games/typing-defense/art-src/animals/chuon-chuon-tre.png` | 2000 | Tự rig Blender | Helper_Idle, Helper_Walk, Helper_Assist.craft, Helper_Cheer | Côn trùng có cánh; Blender làm bay lơ lửng và nhịp cánh. | `games/typing-defense/art-src/3d/animals/chuon-chuon-tre.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS14a · `helper-book` | Sách nhỏ Thư Đồng lật ở nhà hỗ trợ | Image = `games/typing-defense/art-src/helpers/helper-book.png` | 2000 | Tự rig Blender | Lật sách theo Helper_Assist.support (tên clip riêng đề xuất) | Sách có hai khối trang mở theo gáy; Blender thêm khớp, không mua rig Tripo. | `games/typing-defense/art-src/3d/helpers/helper-book.glb` | chờ ảnh |

### 3.2. 2000 · Không rig (38 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Lời Gọi · VS | 01-VS/VS1b · `tre-mallet` | Búa gỗ to của Tre | Image = `games/typing-defense/art-src/heroes/tre-mallet.png` | 2000 | Không rig | — | Đồ cầm/gắn cứng vào socket của nhân vật; không cần rig riêng. | `games/typing-defense/art-src/3d/heroes/tre-mallet.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS1c · `tre-slingshot` | Ná tre của Tre | Image = `games/typing-defense/art-src/heroes/tre-slingshot.png` | 2000 | Không rig | — | Đồ cầm/gắn cứng vào socket của nhân vật; không cần rig riêng. | `games/typing-defense/art-src/3d/heroes/tre-slingshot.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS3b · `linh-khien-shield` | Khiên đồng | Image = `games/typing-defense/art-src/units/linh-khien-shield.png` | 2000 | Không rig | — | Đồ cầm/gắn cứng vào socket của nhân vật; không cần rig riêng. | `games/typing-defense/art-src/3d/units/linh-khien-shield.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS4b · `linh-giao-dai-spear` | Giáo dài | Image = `games/typing-defense/art-src/units/linh-giao-dai-spear.png` | 2000 | Không rig | — | Đồ cầm/gắn cứng vào socket của nhân vật; không cần rig riêng. | `games/typing-defense/art-src/3d/units/linh-giao-dai-spear.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS6b · `oni-club` | Chùy sắt của Oni | Image = `games/typing-defense/art-src/enemies/oni-club.png` | 2000 | Không rig | — | Đồ cầm/gắn cứng vào socket của nhân vật; không cần rig riêng. | `games/typing-defense/art-src/3d/enemies/oni-club.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS9b · `dokkaebi-club` | Gậy của Dokkaebi | Image = `games/typing-defense/art-src/enemies/dokkaebi-club.png` | 2000 | Không rig | — | Đồ cầm/gắn cứng vào socket của nhân vật; không cần rig riêng. | `games/typing-defense/art-src/3d/enemies/dokkaebi-club.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS14b · `helper-fan` | Quạt nan Thư Đồng quạt nồi ở nhà hỗ trợ | Image = `games/typing-defense/art-src/helpers/helper-fan.png` | 2000 | Không rig | — | Quạt cứng gắn tay Thư Đồng; động tác quạt nằm trong clip thân. | `games/typing-defense/art-src/3d/helpers/helper-fan.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K01 · `worker-kit-gatekeeper-head` | Mũ sắt tròn + râu bạc dài, lông mày rậm · Lão Gác Cổng (Lũy Chữ) | Image = `games/typing-defense/art-src/workers/worker-kit-gatekeeper-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-gatekeeper-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K02 · `worker-kit-gatekeeper-crossbow` | Nỏ gỗ to · Lão Gác Cổng | Image = `games/typing-defense/art-src/workers/worker-kit-gatekeeper-crossbow.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-gatekeeper-crossbow.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K03 · `worker-kit-en-head` | Tóc búi, nơ đuôi én · Chị Én (Tháp Cung) | Image = `games/typing-defense/art-src/workers/worker-kit-en-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-en-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K04 · `worker-kit-en-bow` | Cung ngắn · Chị Én | Image = `games/typing-defense/art-src/workers/worker-kit-en-bow.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-en-bow.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K05 · `worker-kit-se-head` | Tóc tròn, chỏm như mào sẻ · Em Sẻ (Tháp Cung) | Image = `games/typing-defense/art-src/workers/worker-kit-se-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-se-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K06 · `worker-kit-se-quiver` | Ống tên · Em Sẻ | Image = `games/typing-defense/art-src/workers/worker-kit-se-quiver.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-se-quiver.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K07 · `worker-kit-dong-head` | Kính đồng đẩy lên trán + ria xám dày · Bác Đồng (Tháp Pháo) | Image = `games/typing-defense/art-src/workers/worker-kit-dong-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-dong-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K08 · `worker-kit-dong-rammer` | Cây thông nòng · Bác Đồng | Image = `games/typing-defense/art-src/workers/worker-kit-dong-rammer.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-dong-rammer.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K09 · `worker-kit-lua-head` | Tóc dựng + băng đô · Cậu Lửa (Tháp Pháo) | Image = `games/typing-defense/art-src/workers/worker-kit-lua-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-lua-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K10 · `worker-kit-lua-shot` | Quả đạn vằn xanh ngọc · Cậu Lửa | Image = `games/typing-defense/art-src/workers/worker-kit-lua-shot.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-lua-shot.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K11 · `worker-kit-scholar-head` | Mũ mềm đen + râu dê trắng · Thầy Đồ Mực (Tháp Thư Pháp) | Image = `games/typing-defense/art-src/workers/worker-kit-scholar-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-scholar-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K12 · `worker-kit-sam-head` | Băng đô xanh đậm + ria đen to · Đội trưởng Sấm (Trại Lính) | Image = `games/typing-defense/art-src/workers/worker-kit-sam-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-sam-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K13 · `worker-kit-sam-drumstick` | Dùi trống to (Blender nhân đôi) · Đội trưởng Sấm | Image = `games/typing-defense/art-src/workers/worker-kit-sam-drumstick.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-sam-drumstick.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K14 · `worker-kit-miner-head` | Mũ vải có đèn dầu nhỏ (không lửa) · Ba anh em thợ mỏ (Mỏ Vàng) | Image = `games/typing-defense/art-src/workers/worker-kit-miner-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-miner-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K15 · `worker-kit-miner-pickaxe` | Cuốc chim · Ba anh em thợ mỏ | Image = `games/typing-defense/art-src/workers/worker-kit-miner-pickaxe.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-miner-pickaxe.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K16 · `worker-kit-ma-head` | Nón lá + bím tóc · Cô Mạ (Ruộng Lúa) | Image = `games/typing-defense/art-src/workers/worker-kit-ma-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-ma-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K17 · `worker-kit-ma-seedlings` | Bó mạ xanh · Cô Mạ | Image = `games/typing-defense/art-src/workers/worker-kit-ma-seedlings.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-ma-seedlings.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K18 · `worker-kit-tieu-head` | Khăn ô nâu kem + râu đen ngắn · Chú Tiều (Trại Gỗ) | Image = `games/typing-defense/art-src/workers/worker-kit-tieu-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-tieu-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K19 · `worker-kit-tieu-axe` | Rìu · Chú Tiều | Image = `games/typing-defense/art-src/workers/worker-kit-tieu-axe.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-tieu-axe.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K20 · `worker-kit-tro-head` | Tóc búi nhỏ buộc dây xám xanh · Trò Mực (Đài Ấn) | Image = `games/typing-defense/art-src/workers/worker-kit-tro-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-tro-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K21 · `worker-kit-tro-scroll` | Cuộn giấy trắng · Trò Mực | Image = `games/typing-defense/art-src/workers/worker-kit-tro-scroll.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-tro-scroll.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K22 · `worker-kit-lang-head` | Búi tóc bạc · Bà Lang Thơm (Nhà Thuốc) | Image = `games/typing-defense/art-src/workers/worker-kit-lang-head.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-lang-head.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K23 · `worker-kit-lang-basket` | Giỏ thảo dược · Bà Lang Thơm | Image = `games/typing-defense/art-src/workers/worker-kit-lang-basket.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-lang-basket.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/K24 · `worker-kit-sam-vest` | Áo giáp lá tre · Đội trưởng Sấm | Image = `games/typing-defense/art-src/workers/worker-kit-sam-vest.png` | 2000 | Không rig | — | Bộ gắn cứng vào xương/socket của thân thợ; không có khớp riêng. | `games/typing-defense/art-src/3d/workers/worker-kit-sam-vest.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V13 · `cannon-barrel-l3` | Tháp Pháo cấp 3: nòng vằn | Image = `games/typing-defense/art-src/kits/cannon-barrel-l3.png` | 2000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/cannon-barrel-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V65 · `go-lan` | Gỗ Lăn | Image = `games/typing-defense/art-src/props/go-lan.png` | 2000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/props/go-lan.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V66 · `pebble` | Viên ná của Tre | Image = `games/typing-defense/art-src/projectiles/pebble.png` | 2000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Đạn cứng; quỹ đạo và xoay do runtime điều khiển. | `games/typing-defense/art-src/3d/projectiles/pebble.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V67 · `meteor` | Đá lửa (Mưa Đá Lửa) | Image = `games/typing-defense/art-src/projectiles/meteor.png` | 2000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Đạn cứng; quỹ đạo và xoay do runtime điều khiển. | `games/typing-defense/art-src/3d/projectiles/meteor.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V68 · `quill` | Lông Đại Bàng Tinh | Image = `games/typing-defense/art-src/projectiles/quill.png` | 2000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Đạn cứng; quỹ đạo và xoay do runtime điều khiển. | `games/typing-defense/art-src/3d/projectiles/quill.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V69 · `seed-drop` | Hạt Mộc Tinh | Image = `games/typing-defense/art-src/projectiles/seed-drop.png` | 2000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Đạn cứng; quỹ đạo và xoay do runtime điều khiển. | `games/typing-defense/art-src/3d/projectiles/seed-drop.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V70 · `fire-feather` | Lông lửa Draconis | Image = `games/typing-defense/art-src/projectiles/fire-feather.png` | 2000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Đạn cứng; quỹ đạo và xoay do runtime điều khiển. | `games/typing-defense/art-src/3d/projectiles/fire-feather.glb` | chờ ảnh |

### 3.3. 4000 · Tự rig Blender (2 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | E25 · `thorn-ant` | Kiến Gai | Left = `games/dragon-hold/art-src/enemies/thorn-ant.png`<br>Front = `games/dragon-hold/art-src/enemies/thorn-ant-front.png` | 4000 | Tự rig Blender | Idle, Crawl (Move), Attack (cắn), Death | Sáu chân và hàm cắn; cần chu kỳ chân riêng, không thử rig Hexapod trả phí. | `games/dragon-hold/art-src/3d/enemies/thorn-ant.glb` | có |
| Rồng Giữ Ải | TR1 · `spikes` | Gai Chông | Image = `games/dragon-hold/art-src/traps/spikes.png` | 4000 | Tự rig Blender | Chờ, Kích (gai trồi), Thu gai (tên clip đề xuất) | Bẫy có khối gai cử động: theo luật phiếu, Blender gắn xương cứng cho phần gai. | `games/dragon-hold/art-src/3d/traps/spikes.glb` | có |

### 3.4. 4000 · Không rig (29 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | TR2 · `pine-bomb` | Bom Hạt Thông | Image = `games/dragon-hold/art-src/traps/pine-bomb.png` | 4000 | Không rig | — (thở/nổ bằng shader và VFX) | Không khớp cơ khí; co giãn cả quả bằng shader, vụn nổ là VFX. | `games/dragon-hold/art-src/3d/traps/pine-bomb.glb` | có |
| Rồng Giữ Ải | K07 · `rock-boulder` | Đá tảng rêu | Image = `games/dragon-hold/art-src/props/pine-river/rock-boulder.png` | 4000 | Không rig | — | Prop tĩnh, không có bộ phận cần khớp. | `games/dragon-hold/art-src/3d/props/pine-river/rock-boulder.glb` | chờ ảnh |
| Rồng Giữ Ải | K08 · `rock-slab` | Gờ đá phiến | Image = `games/dragon-hold/art-src/props/pine-river/rock-slab.png` | 4000 | Không rig | — | Prop tĩnh, không có bộ phận cần khớp. | `games/dragon-hold/art-src/3d/props/pine-river/rock-slab.glb` | chờ ảnh |
| Rồng Giữ Ải | K09 · `river-stones` | Đá kê suối | Image = `games/dragon-hold/art-src/props/pine-river/river-stones.png` | 4000 | Không rig | — | Prop tĩnh, không có bộ phận cần khớp. | `games/dragon-hold/art-src/3d/props/pine-river/river-stones.glb` | chờ ảnh |
| Rồng Giữ Ải | K10 · `stump` | Gốc thông | Image = `games/dragon-hold/art-src/props/pine-river/stump.png` | 4000 | Không rig | — | Prop tĩnh, không có bộ phận cần khớp. | `games/dragon-hold/art-src/3d/props/pine-river/stump.glb` | chờ ảnh |
| Rồng Giữ Ải | K11 · `log` | Khúc gỗ đổ | Image = `games/dragon-hold/art-src/props/pine-river/log.png` | 4000 | Không rig | — | Prop tĩnh, không có bộ phận cần khớp. | `games/dragon-hold/art-src/3d/props/pine-river/log.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V7 · `keep-kit-l3` | Lũy cấp 3 | Image = `games/typing-defense/art-src/kits/keep-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/keep-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V8 · `keep-kit-l4` | Lũy cấp 4 | Image = `games/typing-defense/art-src/kits/keep-kit-l4.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/keep-kit-l4.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V9 · `archer-kit-l2` | Tháp Cung cấp 2 | Image = `games/typing-defense/art-src/kits/archer-kit-l2.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/archer-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V10 · `archer-kit-l3` | Tháp Cung cấp 3 | Image = `games/typing-defense/art-src/kits/archer-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/archer-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V11 · `cannon-kit-l2` | Tháp Pháo cấp 2 | Image = `games/typing-defense/art-src/kits/cannon-kit-l2.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/cannon-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V12 · `cannon-kit-l3` | Tháp Pháo cấp 3: cờ | Image = `games/typing-defense/art-src/kits/cannon-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/cannon-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V14 · `barracks-kit-l2` | Trại Lính cấp 2 | Image = `games/typing-defense/art-src/kits/barracks-kit-l2.png` | 4000 | Không rig | — (hiệu ứng nâng cấp do runtime) | Bộ mái/sàn canh gắn lên nhà; không gồm cánh cổng cần khớp riêng. | `games/typing-defense/art-src/3d/kits/barracks-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V15 · `barracks-kit-l3` | Trại Lính cấp 3 | Image = `games/typing-defense/art-src/kits/barracks-kit-l3.png` | 4000 | Không rig | — (hiệu ứng nâng cấp do runtime) | Bộ mái/sàn canh gắn lên nhà; không gồm cánh cổng cần khớp riêng. | `games/typing-defense/art-src/3d/kits/barracks-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V16 · `gold-mine-kit-l2` | Mỏ Vàng cấp 2 | Image = `games/typing-defense/art-src/kits/gold-mine-kit-l2.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/gold-mine-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V17 · `gold-mine-kit-l3` | Mỏ Vàng cấp 3 | Image = `games/typing-defense/art-src/kits/gold-mine-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/gold-mine-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V18 · `farm-kit-l2` | Ruộng Lúa cấp 2 | Image = `games/typing-defense/art-src/kits/farm-kit-l2.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/farm-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V19 · `farm-kit-l3` | Ruộng Lúa cấp 3 | Image = `games/typing-defense/art-src/kits/farm-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/farm-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V20 · `seal-dais-kit-l2` | Đài Ấn cấp 2 | Image = `games/typing-defense/art-src/kits/seal-dais-kit-l2.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/seal-dais-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V21 · `seal-dais-kit-l3` | Đài Ấn cấp 3 | Image = `games/typing-defense/art-src/kits/seal-dais-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/seal-dais-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V22 · `scribe-kit-l2` | Tháp Thư Pháp cấp 2 | Image = `games/typing-defense/art-src/kits/scribe-kit-l2.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/scribe-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V23 · `scribe-kit-l3` | Tháp Thư Pháp cấp 3: cọ lơ lửng | Image = `games/typing-defense/art-src/kits/scribe-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/scribe-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V24 · `infirmary-kit-l2` | Nhà Thuốc cấp 2 | Image = `games/typing-defense/art-src/kits/infirmary-kit-l2.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/infirmary-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V25 · `infirmary-kit-l3` | Nhà Thuốc cấp 3 | Image = `games/typing-defense/art-src/kits/infirmary-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/infirmary-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V26 · `lumber-kit-l2` | Trại Gỗ cấp 2 | Image = `games/typing-defense/art-src/kits/lumber-kit-l2.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/lumber-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V27 · `lumber-kit-l3` | Trại Gỗ cấp 3 | Image = `games/typing-defense/art-src/kits/lumber-kit-l3.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/lumber-kit-l3.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V62 · `scaffold-bamboo` | Giàn tre | Image = `games/typing-defense/art-src/props/scaffold-bamboo.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/props/scaffold-bamboo.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V63 · `rao-tre` | Rào Tre | Image = `games/typing-defense/art-src/props/rao-tre.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/props/rao-tre.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V64 · `cau-tre` | Cầu Tre | Image = `games/typing-defense/art-src/props/cau-tre.png` | 4000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/props/cau-tre.glb` | chờ ảnh |

### 3.5. 5000 · Tự rig Blender (4 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | E01 · `thorn-wasp` | Ong Gai | Front = `games/dragon-hold/art-src/enemies/thorn-wasp.png`<br>Left = `games/dragon-hold/art-src/enemies/thorn-wasp-side.png` | 5000 | Tự rig Blender | Idle/Hover, Fly (Move), Attack (chổng bụng bắn ngòi), Death | Côn trùng có cánh; cần bay và xoay bụng, không dùng rig Avian của Tripo. | `games/dragon-hold/art-src/3d/enemies/thorn-wasp.glb` | chờ ảnh (có Front; thiếu Left) |
| Lời Gọi · VS | 01-VS/VS3a · `linh-khien` | Lính Khiên (nhánh Khiên Đồng) | Image = `games/typing-defense/art-src/units/linh-khien.png` | 5000 | Tự rig Blender | Unit_Idle, Unit_Walk, Unit_Attack, Unit_Hit, Unit_Death, Unit_Cheer, Unit_Skill; nên có Unit_Charge | Lính chibi và clip Khiên Tường riêng; Blender giữ chân, tay khiên và giáo. | `games/typing-defense/art-src/3d/units/linh-khien.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS4a · `linh-giao-dai` | Lính Giáo Dài (nhánh Giáo Dài) | Image = `games/typing-defense/art-src/units/linh-giao-dai.png` | 5000 | Tự rig Blender | Unit_Idle, Unit_Walk, Unit_Attack, Unit_Hit, Unit_Death, Unit_Cheer; nên có Unit_Charge | Lính chibi, đâm giáo dài xuyên hai mục tiêu; dùng pipeline Lính Giáo để giữ tay và chân. | `games/typing-defense/art-src/3d/units/linh-giao-dai.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS5a · `worker-base` | Thân thợ chung của 10 tổ thợ | Image = `games/typing-defense/art-src/workers/worker-base.png` | 5000 | Tự rig Blender | Worker_Idle, Worker_Walk, Worker_Work, Worker_Strike; nên có Worker_Cheer | Thân chibi 2,25 đầu, dùng chung 10 tổ; động tác nghề theo nhịp chữ cần clip riêng. | `games/typing-defense/art-src/3d/workers/worker-base.glb` | chờ ảnh |

### 3.6. 5000 · Không rig (2 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | K05 · `bush-moss` | Bụi rêu | Image = `games/dragon-hold/art-src/props/pine-river/bush-moss.png` | 5000 | Không rig | — | Cây/bụi tĩnh; gió và lay tán làm bằng shader. | `games/dragon-hold/art-src/3d/props/pine-river/bush-moss.glb` | chờ ảnh |
| Rồng Giữ Ải | K06 · `bush-blossom` | Bụi hoa kem, tím | Image = `games/dragon-hold/art-src/props/pine-river/bush-blossom.png` | 5000 | Không rig | — | Cây/bụi tĩnh; gió và lay tán làm bằng shader. | `games/dragon-hold/art-src/3d/props/pine-river/bush-blossom.glb` | chờ ảnh |

### 3.7. 6000 · Tripo Biped (3 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | E09 · `moss-grunt` | Yêu Rêu Lính | Front = `games/dragon-hold/art-src/enemies/moss-grunt.png`<br>Back = `games/dragon-hold/art-src/enemies/moss-grunt-back.png` | 6000 | Tripo Biped | Idle, Walk, Attack (chém), Death | Hai chân tư thế A; bốn preset cơ bản đủ cho quái bầy. | `games/dragon-hold/art-src/3d/enemies/moss-grunt.glb` | chờ ảnh (có Front; thiếu Back) |
| Rồng Giữ Ải | E11 · `moss-archer` | Yêu Rêu Cung | Front = `games/dragon-hold/art-src/enemies/moss-archer.png`<br>Back = `games/dragon-hold/art-src/enemies/moss-archer-back.png` | 6000 | Tripo Biped | Idle, Walk, Attack (bắn cung), Death | Hai chân tư thế A; dùng preset Attack bắn cung, kiểm tay và dây cung khi duyệt. | `games/dragon-hold/art-src/3d/enemies/moss-archer.glb` | có |
| Rồng Giữ Ải | U1 · `moss-warden` | Vệ Binh Rêu | Front = `games/dragon-hold/art-src/units/moss-warden.png`<br>Back = `games/dragon-hold/art-src/units/moss-warden-back.png` | 6000 | Tripo Biped | Idle, Walk, Attack (quét chày/đỡ khiên), Death | Dáng người tư thế A, tay chân tách rõ; preset cơ bản đủ, nụ hồi sinh là VFX. | `games/dragon-hold/art-src/3d/units/moss-warden.glb` | chờ ảnh |

### 3.8. 6000 · Tự rig Blender (8 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | E18 · `blight-wolf` | Sói Mục | Left = `games/dragon-hold/art-src/enemies/blight-wolf.png`<br>Front = `games/dragon-hold/art-src/enemies/blight-wolf-front.png` | 6000 | Tự rig Blender | Idle, Run, Attack (cắn/vồ), Death | Cắn và vồ cần clip riêng, đuôi và thân chồng lớp; tải GLB không xương. | `games/dragon-hold/art-src/3d/enemies/blight-wolf.glb` | có |
| Rồng Giữ Ải | TR3 · `net-launcher` | Lưới Phóng | Image = `games/dragon-hold/art-src/traps/net-launcher.png` | 6000 | Tự rig Blender | Chờ, Ngắm, Bắn, Hồi (tên clip đề xuất) | Bẫy có đầu phóng cử động: theo luật phiếu, Blender làm khớp đầu phóng; lưới bung là VFX. | `games/dragon-hold/art-src/3d/traps/net-launcher.glb` | có |
| Lời Gọi · VS | 01-VS/VS7 · `tat-phuong` | Tất Phương, chim một chân tự nổ | Image = `games/typing-defense/art-src/enemies/tat-phuong.png` | 6000 | Tự rig Blender | Enemy_Idle, Enemy_Move, Enemy_Attack, Enemy_Hit, Enemy_Skill, Enemy_Death | Chim một chân, lò cò và báo nổ; dáng không chuẩn cho Biped/Quadruped. | `games/typing-defense/art-src/3d/enemies/tat-phuong.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS8 · `ma-da` | Ma Da, hồn nước tàng hình | Image = `games/typing-defense/art-src/enemies/ma-da.png` | 6000 | Tự rig Blender | Enemy_Idle, Enemy_Move, Enemy_Attack, Enemy_Hit, Enemy_Death | Hồn nước không thấy chân, trôi và Kéo Chân; không có dáng người chuẩn để auto rig. | `games/typing-defense/art-src/3d/enemies/ma-da.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS9a · `dokkaebi` | Yêu Tinh Dokkaebi, gọi Ma Trơi | Image = `games/typing-defense/art-src/enemies/dokkaebi.png` | 6000 | Tự rig Blender | Enemy_Idle, Enemy_Move, Enemy_Attack, Enemy_Hit, Enemy_Skill, Enemy_Death | Chibi có động tác Phong Gậy/gọi Ma Trơi riêng; cần clip và đồ gắn theo đòn. | `games/typing-defense/art-src/3d/enemies/dokkaebi.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS10 · `kamaitachi` | Chồn Liềm, bay thấp trên lốc | Image = `games/typing-defense/art-src/enemies/kamaitachi.png` | 6000 | Tự rig Blender | Enemy_Idle, Enemy_Move, Enemy_Attack, Enemy_Hit, Enemy_Death | Chồn bay thấp, chạy quanh lốc; cần phối hợp thân/đuôi, không chỉ preset Run. | `games/typing-defense/art-src/3d/enemies/kamaitachi.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS12 · `trau` | Trâu (trâu Mộng của Ruộng Lúa) | Left = `games/typing-defense/art-src/animals/trau.png`<br>Front (tùy chọn) = `games/typing-defense/art-src/animals/trau-front.png` | 6000 | Tự rig Blender | Worker_Work, Worker_Strike, Worker_Cheer, Unit_Charge; Idle, Walk/Run | Trâu Mộng cần kéo cày và húc riêng; Blender kiểm chân trụ và động tác đầu/sừng. | `games/typing-defense/art-src/3d/animals/trau.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS13 · `piggy` | Heo Đất Vàng | Image = `games/typing-defense/art-src/animals/piggy.png` | 6000 | Tự rig Blender | Enemy_Move, Enemy_Idle, Enemy_Hit, Enemy_Death | Heo gốm chân ngắn, thân tròn; Blender làm bước chạy và phản ứng, vỡ gốm là VFX. | `games/typing-defense/art-src/3d/animals/piggy.glb` | chờ ảnh |

### 3.9. 6000 · Không rig (3 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | K03 · `pine-young` | Thông non | Image = `games/dragon-hold/art-src/props/pine-river/pine-young.png` | 6000 | Không rig | — | Cây/bụi tĩnh; gió và lay tán làm bằng shader. | `games/dragon-hold/art-src/3d/props/pine-river/pine-young.glb` | chờ ảnh |
| Tuyến Cuối · dùng chung Space | S1 · `rainbow-scout` | Lính họ Rainbow | Image = `games/space-typing/art-src/enemies/rainbow-scout.png` | 6000 | Không rig | Enemy_Idle (Blender); di chuyển/trúng/hạ bằng shader instanced | Thiếu GLB gốc riêng; quái đám đông S1 chuyển động bằng shader, không cần xương. | `games/space-typing/art-src/3d/enemies/rainbow-scout.glb` | có |
| Tuyến Cuối · dùng chung Space | S1 · `rainbow-tank` | Trâu / Đầu Đàn họ Rainbow | Image = `games/space-typing/art-src/enemies/rainbow-tank.png` | 6000 | Không rig | Enemy_Idle (Blender); di chuyển/trúng/hạ bằng shader instanced | Thiếu GLB gốc riêng; quái đám đông S1 chuyển động bằng shader, không cần xương. | `games/space-typing/art-src/3d/enemies/rainbow-tank.glb` | có |

### 3.10. 8000 · Tự rig Blender (1 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | E19 · `tusk-boar` | Heo Nanh Đá | Left = `games/dragon-hold/art-src/enemies/tusk-boar.png`<br>Front = `games/dragon-hold/art-src/enemies/tusk-boar-front.png` | 8000 | Tự rig Blender | Idle, Walk, Attack (cào đất/húc), Death | Húc có lấy đà và trượt theo đà cần clip riêng toàn thân. | `games/dragon-hold/art-src/3d/enemies/tusk-boar.glb` | có |

### 3.11. 8000 · Không rig (17 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Lời Gọi · VS | 02-VS/V6 · `keep-kit-l2` | Lũy cấp 2 | Image = `games/typing-defense/art-src/kits/keep-kit-l2.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Bộ cấp gắn lên nhà bằng socket; hiệu ứng nâng cấp không cần xương. | `games/typing-defense/art-src/3d/kits/keep-kit-l2.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V46 · `ruin-s` | Đổ nát cỡ S | Image = `games/typing-defense/art-src/ruins/ruin-s.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/ruins/ruin-s.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V47 · `ruin-m` | Đổ nát cỡ M | Image = `games/typing-defense/art-src/ruins/ruin-m.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/ruins/ruin-m.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V48 · `ruin-l` | Đổ nát cỡ L | Image = `games/typing-defense/art-src/ruins/ruin-l.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/ruins/ruin-l.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V49 · `ruin-xl` | Đổ nát cỡ XL | Image = `games/typing-defense/art-src/ruins/ruin-xl.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/ruins/ruin-xl.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V50 · `vach-thac-bac` | Vách Thác Bạc | Image = `games/typing-defense/art-src/landmarks/vach-thac-bac.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/vach-thac-bac.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V51 · `cau-go` | Cầu gỗ | Image = `games/typing-defense/art-src/landmarks/cau-go.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/cau-go.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V52 · `choi-canh-doi` | Chòi canh trên đồi | Image = `games/typing-defense/art-src/landmarks/choi-canh-doi.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/choi-canh-doi.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V53 · `hai-dang` | Hải đăng | Image = `games/typing-defense/art-src/landmarks/hai-dang.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/hai-dang.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V54 · `cau-tau` | Cầu tàu | Image = `games/typing-defense/art-src/landmarks/cau-tau.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/cau-tau.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V55 · `nha-rai-da` | Nhà Rái Đá trên cọc | Image = `games/typing-defense/art-src/landmarks/nha-rai-da.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/nha-rai-da.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V56 · `them-da-trang` | Thềm Đá Trắng | Image = `games/typing-defense/art-src/landmarks/them-da-trang.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/them-da-trang.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V57 · `goc-da-rong` | Gốc đa rỗng | Image = `games/typing-defense/art-src/landmarks/goc-da-rong.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/goc-da-rong.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V58 · `cau-do` | Cầu Đỏ | Image = `games/typing-defense/art-src/landmarks/cau-do.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/cau-do.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V59 · `da-ke` | Đá Kê | Image = `games/typing-defense/art-src/landmarks/da-ke.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/da-ke.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V60 · `re-vom` | Rễ khổng lồ uốn qua đường | Image = `games/typing-defense/art-src/landmarks/re-vom.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/re-vom.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V61 · `thac-ho-sut` | Thác đổ vào Hố Sụt | Image = `games/typing-defense/art-src/landmarks/thac-ho-sut.png` | 8000 | Không rig | — (chuyển động cả vật/socket hoặc shader khi cần) | Prop/mốc cảnh tĩnh; VFX, gió hoặc di chuyển cả vật không cần rig. | `games/typing-defense/art-src/3d/landmarks/thac-ho-sut.glb` | chờ ảnh |

### 3.12. 9000 · Tự rig Blender (1 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Lời Gọi · VS | 01-VS/VS6a · `oni` | Quỷ Oni, phá nhà | Image = `games/typing-defense/art-src/enemies/oni.png` | 9000 | Tự rig Blender | Enemy_Idle, Enemy_Move, Enemy_Attack, Enemy_Hit, Enemy_Death | Quái chibi to, đập chùy có lấy đà và thả chùy; Blender làm chuyển động có trọng lượng. | `games/typing-defense/art-src/3d/enemies/oni.glb` | chờ ảnh |

### 3.13. 10000 · Tự rig Blender (4 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | G01 · `moss-banner` | Yêu Rêu Cầm Cờ | Front = `games/dragon-hold/art-src/generals/moss-banner.png`<br>Back = `games/dragon-hold/art-src/generals/moss-banner-back.png` | 10000 | Tự rig Blender | Idle, Walk, Attack, Cast, Hit, Death, Intro | Tướng có cắm/phất cờ, cờ và thân chuyển động chồng lớp; preset cơ bản chưa đủ. | `games/dragon-hold/art-src/3d/generals/moss-banner.glb` | có |
| Lời Gọi · P | 02/P5 · `barracks` | Trại Lính, bản làm lại cao hơn | Image = `games/typing-defense/art-src/buildings/barracks-v2.png` | 10000 | Tự rig Blender | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin; mở/đóng cổng (Blender) | Thay model tạm 1,8 m; nhà giữ cứng, chỉ gắn xương cánh cổng theo luật vật có phần cử động. | `games/typing-defense/art-src/3d/buildings/barracks.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V34 · `barracks-khien-dong` | Trại Lính, nhánh Khiên Đồng | Image = `games/typing-defense/art-src/branches/barracks-khien-dong.png` | 10000 | Tự rig Blender | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin; mở/đóng cổng (Blender) | Nhánh Trại Lính giữ nhà cứng, Blender gắn xương cánh cổng cử động. | `games/typing-defense/art-src/3d/branches/barracks-khien-dong.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V35 · `barracks-giao-dai` | Trại Lính, nhánh Giáo Dài | Image = `games/typing-defense/art-src/branches/barracks-giao-dai.png` | 10000 | Tự rig Blender | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin; mở/đóng cổng (Blender) | Nhánh Trại Lính giữ nhà cứng, Blender gắn xương cánh cổng cử động. | `games/typing-defense/art-src/3d/branches/barracks-giao-dai.glb` | chờ ảnh |

### 3.14. 10000 · Không rig (26 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Rồng Giữ Ải | H1 · `herb-hut` | Nhà Thuốc Lá | Image = `games/dragon-hold/art-src/houses/herb-hut.png` | 10000 | Không rig | — | Nhà tĩnh; giọt sáng và vòng hồi máu là VFX. | `games/dragon-hold/art-src/3d/houses/herb-hut.glb` | chờ ảnh |
| Rồng Giữ Ải | K01 · `pine-tall` | Thông cao | Image = `games/dragon-hold/art-src/props/pine-river/pine-tall.png` | 10000 | Không rig | — | Cây/bụi tĩnh; gió và lay tán làm bằng shader. | `games/dragon-hold/art-src/3d/props/pine-river/pine-tall.glb` | chờ ảnh |
| Rồng Giữ Ải | K02 · `pine-round` | Thông dù già | Image = `games/dragon-hold/art-src/props/pine-river/pine-round.png` | 10000 | Không rig | — | Cây/bụi tĩnh; gió và lay tán làm bằng shader. | `games/dragon-hold/art-src/3d/props/pine-river/pine-round.glb` | chờ ảnh |
| Rồng Giữ Ải | K04 · `tree-violet` | Cây tán tím | Image = `games/dragon-hold/art-src/props/pine-river/tree-violet.png` | 10000 | Không rig | — | Cây/bụi tĩnh; gió và lay tán làm bằng shader. | `games/dragon-hold/art-src/3d/props/pine-river/tree-violet.glb` | chờ ảnh |
| Rồng Giữ Ải | K12 · `bridge-old` | Cầu gỗ cũ | Image = `games/dragon-hold/art-src/props/pine-river/bridge-old.png` | 10000 | Không rig | — | Prop tĩnh, không có bộ phận cần khớp. | `games/dragon-hold/art-src/3d/props/pine-river/bridge-old.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V1 · `scribe` | Tháp Thư Pháp cấp 1 | Image = `games/typing-defense/art-src/buildings/scribe.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/buildings/scribe.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V2 · `infirmary` | Nhà Thuốc cấp 1 | Image = `games/typing-defense/art-src/buildings/infirmary.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/buildings/infirmary.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V3 · `lumber` | Trại Gỗ cấp 1 | Image = `games/typing-defense/art-src/buildings/lumber.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/buildings/lumber.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V4 · `farm-ao-ca` | Ruộng, skin Ao Cá | Image = `games/typing-defense/art-src/buildings/farm-ao-ca.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/buildings/farm-ao-ca.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V5 · `farm-nuong` | Ruộng, skin Nương | Image = `games/typing-defense/art-src/buildings/farm-nuong.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/buildings/farm-nuong.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V28 · `archer-en-bao` | Cung, nhánh Én Bão | Image = `games/typing-defense/art-src/branches/archer-en-bao.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/archer-en-bao.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V29 · `archer-than-tien` | Cung, nhánh Thần Tiễn | Image = `games/typing-defense/art-src/branches/archer-than-tien.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/archer-than-tien.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V30 · `cannon-coi-lon` | Pháo, nhánh Cối Lớn | Image = `games/typing-defense/art-src/branches/cannon-coi-lon.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/cannon-coi-lon.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V31 · `cannon-vac-lua` | Pháo, nhánh Vạc Lửa | Image = `games/typing-defense/art-src/branches/cannon-vac-lua.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/cannon-vac-lua.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V32 · `scribe-but-loi` | Thư Pháp, nhánh Bút Lôi | Image = `games/typing-defense/art-src/branches/scribe-but-loi.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/scribe-but-loi.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V33 · `scribe-muc-bang` | Thư Pháp, nhánh Mực Băng | Image = `games/typing-defense/art-src/branches/scribe-muc-bang.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/scribe-muc-bang.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V36 · `gold-mine-ham-sau` | Mỏ, nhánh Hầm Sâu | Image = `games/typing-defense/art-src/branches/gold-mine-ham-sau.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/gold-mine-ham-sau.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V37 · `gold-mine-lo-duc-tien` | Mỏ, nhánh Lò Đúc Tiền | Image = `games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/gold-mine-lo-duc-tien.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V38 · `farm-bac-thang` | Ruộng, nhánh Bậc Thang | Image = `games/typing-defense/art-src/branches/farm-bac-thang.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/farm-bac-thang.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V39 · `farm-chuong-trau` | Ruộng, nhánh Chuồng Trâu | Image = `games/typing-defense/art-src/branches/farm-chuong-trau.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/farm-chuong-trau.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V40 · `lumber-xuong-cua` | Trại Gỗ, nhánh Xưởng Cưa | Image = `games/typing-defense/art-src/branches/lumber-xuong-cua.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/lumber-xuong-cua.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V41 · `lumber-xuong-rao` | Trại Gỗ, nhánh Xưởng Rào | Image = `games/typing-defense/art-src/branches/lumber-xuong-rao.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/lumber-xuong-rao.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V42 · `seal-dais-phong-an` | Đài Ấn, nhánh Phong Ấn | Image = `games/typing-defense/art-src/branches/seal-dais-phong-an.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/seal-dais-phong-an.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V43 · `seal-dais-vang-am` | Đài Ấn, nhánh Vang Âm | Image = `games/typing-defense/art-src/branches/seal-dais-vang-am.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/seal-dais-vang-am.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V44 · `infirmary-vuon-thao-duoc` | Nhà Thuốc, nhánh Vườn Thảo Dược | Image = `games/typing-defense/art-src/branches/infirmary-vuon-thao-duoc.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/infirmary-vuon-thao-duoc.glb` | chờ ảnh |
| Lời Gọi · VS | 02-VS/V45 · `infirmary-tram-cuu-thuong` | Nhà Thuốc, nhánh Trạm Cứu Thương | Image = `games/typing-defense/art-src/branches/infirmary-tram-cuu-thuong.png` | 10000 | Không rig | Building_Idle, Building_Fire; nên có Building_Work, Building_Hit, Building_Ruin (shader/cả khối) | Công trình tĩnh; VFX và chuyển động cả khối/socket làm trong runtime. | `games/typing-defense/art-src/3d/branches/infirmary-tram-cuu-thuong.glb` | chờ ảnh |

### 3.15. 20000 · Tự rig Blender (1 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Lời Gọi · VS | 01-VS/VS1a · `tre` | Tướng Tre, cô thợ mộc tre | Front = `games/typing-defense/art-src/heroes/tre.png`<br>Left = `games/typing-defense/art-src/heroes/tre-side.png`<br>Back = `games/typing-defense/art-src/heroes/tre-back.png` | 20000 | Tự rig Blender | Hero_Idle, Hero_Run, Hero_Attack, Hero_Skill1, Hero_Skill2, Hero_Ult, Hero_Assist, Hero_Hit, Hero_Death, Hero_Respawn, Hero_Victory | Tướng chữ ký, chibi, cần bắn ná, sửa nhà, dựng cầu và lớp phụ kiện. | `games/typing-defense/art-src/3d/heroes/tre.glb` | chờ ảnh |

### 3.16. 30000 · Tự rig Blender (2 model)

| Game | Mã · id | Tên | Ô ảnh Tripo · đường dẫn ảnh 2D | Face limit | Rig | Clip cần có | Lý do chọn rig | Nơi lưu GLB gốc | Trạng thái ảnh 2D |
|---|---|---|---|---:|---|---|---|---|---|
| Lời Gọi · P | 01/P18 · `draconis` | Draconis Phượng Long | Front = `games/typing-defense/art-src/heroes/draconis.png`<br>Left = `games/typing-defense/art-src/heroes/draconis-side.png`<br>Back = `games/typing-defense/art-src/heroes/draconis-back.png` | 30000 | Tự rig Blender | Hero_Fly, Hero_Idle_Hover, Hero_Boost, Hero_Attack_L, Hero_Attack_R, Hero_Attack_Both, Hero_Cast, Hero_Hit, Hero_Death, Hero_Victory, Hero_Intro; Hero_Skill1, Hero_Skill2, Hero_Ult, Hero_Takeoff, Hero_Land, Hero_Perch_Assist | Rồng chữ ký có cánh; rig Tripo ngăn build_winged_rig, cần clip bay và chồng lớp toàn thân. | `games/typing-defense/art-src/3d/heroes/draconis.glb` | chờ ảnh |
| Lời Gọi · VS | 01-VS/VS11 · `dai-bang-tinh` | Boss Đại Bàng Tinh | Left = `games/typing-defense/art-src/bosses/dai-bang-tinh.png`<br>Front = `games/typing-defense/art-src/bosses/dai-bang-tinh-front.png` | 30000 | Tự rig Blender | Boss_Intro, Boss_Idle, Boss_Move, Boss_Attack, Boss_Skill.snatch, Boss_Skill.gale, Boss_Skill.quill, Boss_Skill.steal, Boss_Channel, Boss_Stun, Boss_Hit, Boss_Phase, Boss_Death | Boss có cánh, sà cắp và bão cánh; cần clip bay và chồng lớp toàn thân. | `games/typing-defense/art-src/3d/bosses/dai-bang-tinh.glb` | chờ ảnh |

## 4. Thứ tự làm đề xuất

1. **Duyệt mẫu Rồng trước: E09 → E18 → E01.** Chốt dấu Héo A/B và ảnh chính/phụ theo README §2; HT-A/HT-B chỉ là ảnh thử, không gửi Tripo. E09 dùng nhóm 6000 · Tripo Biped; E18 dùng 6000 · tự rig Blender; E01 dùng 5000 · tự rig Blender. Chủ dự án duyệt hình model, Claude làm clip mẫu rồi duyệt chuyển động trước khi dựng hàng loạt sinh vật còn lại.
2. **Sau cổng mẫu, làm hết P đang thiếu:** Draconis 30000 · Blender, Trại Lính 10000 · Blender; hai Rainbow 6000 · không rig có thể làm cùng đợt vì đã có ảnh. Trại Lính chờ đưa ảnh `barracks-v2.png` từ máy Mac về đường dẫn trong bảng.
3. **Gom theo từng cặp thiết lập §3:** 6000 · Tripo Biped (E11, U1 sau E09); các nhóm Blender theo face limit tăng dần; các nhóm không rig 2000 → 4000 → 5000 → 6000 → 8000 → 10000. Đổi face limit hoặc cách rig thì sang nhóm mới. Prop Rồng không phụ thuộc dấu Héo, có thể làm trong lúc chờ duyệt sinh vật.
4. **Bậc VS làm sau P**, vẫn theo đúng các cặp face limit/rig đã gom chung. Cùng nhóm có cả Rồng và TD thì giữ riêng ảnh tham chiếu/phong cách, không dùng ảnh game này làm tham chiếu cho game kia.
5. **Tu Tiên:** chỉ xếp lịch sau khi có canon mỹ thuật và danh sách M0b. Không chi credit dựa trên tài liệu đánh giá cũ.

## 5. Việc sau khi có GLB

Đây là hướng dẫn cho lượt nhận model sau; phiếu này chỉ lập danh sách, chưa tạo ảnh, model, rig hay đẩy media.

1. Đổi tên và chép GLB gốc vào đúng cột **Nơi lưu GLB gốc** (`art-src/3d/…`). Không đặt vào `public/assets/…` hoặc dùng file đã giảm mặt làm bản gốc. Trại Lính mới vẫn đích `games/typing-defense/art-src/3d/buildings/barracks.glb`: giữ bản cũ riêng trước khi thay theo changelog; không tạo thêm id runtime `barracks-v2`.
2. Trong **WSL Ubuntu**, tại gốc repo `/mnt/d/typing-game`, cập nhật danh mục của game vừa nhận GLB, rồi sao lưu:

   ```bash
   pnpm models:index --root games/dragon-hold
   pnpm models:index --root games/typing-defense
   # Hai Rainbow được dùng chung từ Space:
   pnpm models:index --root games/space-typing
   pnpm media:push
   ```

   Chỉ chạy dòng index tương ứng game có GLB mới; mẫu tổng quát là `pnpm models:index --root games/<game>`. Không index hai Rainbow dưới `games/typing-survival`: game đó dùng `/assets/space-typing/models/`. Cấu hình hiện tại `media/media.config.json` đã liệt kê cả bốn game; lời nhắc cũ “media chỉ quét Space” đã lỗi thời.
3. **Model tự rig: báo Claude** game, id, GLB gốc, ảnh chính/phụ, clip theo bảng, và “GLB chưa có xương”. Claude đo lại lưới rồi làm preset riêng, không coi preset của loài khác là đã tương thích. Bản xử lý xuất riêng vào `art-src/models/…`, giữ nguyên GLB Tripo.
4. Với Tripo Biped, báo đã có rig và các clip thực tế xuất được. Blender ánh xạ tên clip, thêm socket, chuẩn hướng/cỡ/gốc, khóa chuyển động gốc nếu trượt; rig hỏng thì dùng bản không xương. Với model không rig, chạy pipeline tĩnh; các clip co giãn/cả vật của S1 không cần thêm xương.
5. Duyệt ảnh model và chuỗi khung clip trong góc camera game trước khi đưa vào manifest. Kiểm chân trụ, giãn lưới, vùng dính tay/thân, cánh, socket và nhịp đòn. Việc index/sao lưu không thay cho chuẩn bị và tích hợp runtime.

### 5.1. Công cụ Blender đã có

| Công cụ | Dùng cho lượt nhận GLB |
|---|---|
| `games/typing-defense/scripts/models/blender/td_rig_tools.py` | Nhập model không xương, chuẩn hướng/cỡ, xương, vùng trọng lượng, socket; dùng xương Mesh2Motion và xích phụ theo preset. |
| `games/typing-defense/scripts/models/blender/td_rig_clips.py`, `td_rig_creatures.py`, `td_rig_post.py`, `td_rig_attach.py` | Chuyển clip người CC0, clip theo khóa, rắn/khối mềm, lớp chuyển động, IK, lò xo đuôi/tai/áo, đồ cầm. Cần thêm preset/clip cho loài mới. |
| `games/typing-defense/scripts/models/blender/td_rig_review.py`, `td_rig_compare.py` | Đo giãn cạnh, tam giác sập, trượt chân, đầu cứng và mối nối vòng lặp; ảnh camera game và thử tư thế khó. |
| `games/space-typing/scripts/models/blender/space_typing_model_tools.py` | `build_winged_rig`, `make_flight_clips`, `make_dragon_clips`, `make_guide_clips`; `rigid_islands` trong cấu hình vùng tách giúp các mảnh gai/vảy/lông rời theo một xương, tránh kéo giãn thành mảnh dài. Không phải rig dùng được ngay cho mọi côn trùng. |
| `scripts/models/blender/static_model_tools.py` | Model tĩnh: nhập gộp đỉnh ở đường nối UV, hướng/cỡ/gốc, giảm mặt, vật liệu, socket, xuất bản xử lý; không nhận model đã có armature. |

### 5.2. Có GLB rồi, không gửi Tripo tạo lại

Các mục dưới đây là việc **rig/clip/duyệt**, không nằm trong 143 lượt và không cộng credit rig Tripo:

| Model / nhóm | Hiện trạng và việc tiếp theo | Cách rig / lý do |
|---|---|---|
| Lam `heroes/lam` | Có GLB gốc, đã có rig/clip Blender và bản sửa duyệt 24/10. | Blender: rig Tripo cũ gắn 14.071/14.132 đỉnh cứng vào Hips, không dùng lại. |
| Cương Thi, Lính Giáo, Tanuki, Troll | Có GLB gốc; đã có pipeline rig, còn các mục chủ dự án duyệt bằng mắt trong README công cụ. | Blender: nhảy cứng, tay đồ cầm, đuôi/lá/váy và clip đặc thù đã có; không mua lại rig. |
| Nuppeppō, Thuồng Luồng, Mầm Gỗ, Thư Đồng | Có GLB gốc và preset/clip; changelog ghi kiểm lô sinh vật, một số kiểm chỉ ở chế độ xương hoặc không xuất. | Blender: khối mềm, rắn chuỗi, cây và cánh cần dáng riêng; không coi kết quả kiểm xương là đã duyệt mọi clip. |
| Alicanto `enemies/alicanto` | Có GLB gốc; tiếp tục rig cánh/clip nếu bản chạy chưa đủ. | Blender: chim bay, cần vỗ cánh và clip riêng; không tạo lại chỉ vì thiếu animation. |
| Mộc Tinh `bosses/moc-tinh` | Có `games/typing-defense/art-src/3d/bosses/moc-tinh.glb`. Changelog 24/10 mới có Boss_Idle, chưa có bản xuất hoàn chỉnh. Tiếp tục Rễ Trồi, Quật cành, choáng, rút lui và kiểm bản xuất. | Blender: boss cây yêu, tán/rễ chuyển động chồng lớp; GLB gốc đã có. |
| Xe goòng `props/gold-mine-cart`, Rễ Trồi `projectiles/root-burst` | Cả hai có tên trong SOURCES và có GLB thật trên máy. Không yêu cầu dựng lại. | Không rig riêng: goòng chạy cả vật trên ray; rễ trồi/rút cả model theo runtime. |
| Lũy/các nhà hiện có, rương và đồ gắn | Giữ model đã có; tách cánh cổng Lũy, nắp rương và làm clip theo bước Blender còn thiếu của README. | Blender cho khớp cổng/nắp rương; phần nhà/đồ tĩnh không rig. Đây là xử lý GLB hiện có, không phải lượt tạo model mới. |

## 6. Tu Tiên Thủ Ải và những mục chưa chốt

**Chờ canon.** Tại thời điểm lập file, `docs/games/tu-tien/00-canon.md` chưa tồn tại. Chưa có phần mỹ thuật/M0b tại nguồn được chỉ định để chốt model, ảnh, face limit, rig, clip hay đích GLB cho `games/immortality-cultivation`. Không suy danh sách model từ `DANH_GIA_2026-10-24.md`, tài liệu phân tích hoặc mã giữ chỗ; không cộng một con số giả vào tổng.

Bậc “Sau” của TD (§12 file 01, §7 file 02): các thế giới 2–5, bộ Trợ Thủ/thợ mới, trang phục, bộ skin thế giới và CGI dựng sẵn chưa có bộ id/ảnh đầy đủ. CGI dùng lại model, Bà Cú Mực và người đón ở Thư Thành dùng tranh 2D. Chỉ VS đã định danh đủ 115 model được đưa vào bảng; không biến các nhóm ý tưởng thành model mới tự đặt tên.

Rồng M0 không gồm Bệ Rồng, Hỏa Long mới hay 5 prop M2. Bệ dùng khối tạm theo README §7; 8 ô đất, 4 tấm decal, phông xa, 20 icon, HT-A/HT-B là ảnh dùng thẳng/thử dáng, không gửi Tripo. Vì vậy 67 ảnh của bộ M0 không đồng nghĩa 67 model.

## 7. Nguồn và các chỗ mâu thuẫn

### 7.1. Nguồn đối chiếu

- Rồng: [README §2–3](dragon-lane/art-requests/m0/README.md), [01 sinh vật](dragon-lane/art-requests/m0/01-creatures.md), [02 phe ta](dragon-lane/art-requests/m0/02-allies-traps.md), [03 prop](dragon-lane/art-requests/m0/03-pine-river-props.md), [04 đất/decal/phông](dragon-lane/art-requests/m0/04-2d-ground-decals-backdrop.md), [05 icon](dragon-lane/art-requests/m0/05-icons.md).
- Lời Gọi: [SOURCES hiện tại](../../games/typing-defense/art-src/3d/SOURCES.json), [README công cụ model](../../games/typing-defense/scripts/models/README.md), [changelog rig sinh vật](../../games/typing-defense/docs/changelog/2026-10-24-models-creature-rigs.md), [changelog sửa rig và Trại Lính](../../games/typing-defense/docs/changelog/2026-10-24-models-rig-fixes.md).
- Bộ yêu cầu TD trước khi tách game: [README](../../games/space-typing/docs/art-requests/td/README.md), [01 P](../../games/space-typing/docs/art-requests/td/01-tripo-characters-enemies.md), [02 P](../../games/space-typing/docs/art-requests/td/02-tripo-buildings-props.md), cùng [01 VS](../../games/space-typing/docs/art-requests/td/01-tripo-characters-enemies-vs.md), [02 VS](../../games/space-typing/docs/art-requests/td/02-tripo-buildings-props-vs.md) được hai file P dẫn tới.
- Tuyến Cuối: [BUILD_S1 §1.1, §6, §12](../../games/typing-survival/docs/BUILD_S1.md), [BUILD_S0](../../games/typing-survival/docs/BUILD_S0.md), [kế hoạch](../../games/typing-survival/docs/SURVIVAL_MODE_PLAN.md), [BUILD_NOTES](../../games/typing-survival/docs/BUILD_NOTES.md), [preset model Space](../../games/space-typing/scripts/models/presets/campaign3d-models.json), [SOURCES Space](../../games/space-typing/art-src/3d/SOURCES.json), cùng `games/typing-survival/src/view/crowd.ts` để xác nhận id đang dùng.
- Công cụ rig/tĩnh: các file §5.1; sao lưu: `media/media.config.json`. Canon Tu Tiên chờ đúng đường dẫn §6.

### 7.2. Cách xử lý mâu thuẫn / thông tin cũ

| Chỗ lệch | Kết luận dùng trong phiếu này |
|---|---|
| README Rồng §1 ghi “24 model (2 + 7 sinh vật, 5 phe ta, 12 prop)” | Hai ảnh thử Héo không phải model. Đếm đúng 24 dòng §3.2 = 7 địch (6 quái + G01) + 5 phe ta (U1, H1, TR1–TR3) + 12 prop. Không cộng thêm 2. |
| README Rồng §2–3.2 từng chọn E18/E19 Quadruped, E01 Avian, E25 Hexapod, G01 Biped | Face limit và ảnh giữ nguyên. Luật phiếu này ưu tiên Blender cho cắn/vồ/húc, côn trùng/cánh và tướng có clip riêng. E09/E11/U1 giữ Tripo Biped. |
| File 02 Rồng nói bẫy không rig, trồi gai bằng shader, quay cả trụ bằng mã | Phiếu này phân TR1/TR3 sang Blender để có khớp cử động theo luật bẫy; TR2 vẫn không rig. Tên clip/khớp là đề xuất cần Claude làm khi nhận GLB; runtime chưa đổi. |
| README Rồng §4 nói thư mục game chưa có, ảnh ở Downloads, media chỉ quét Space | `games/dragon-hold/art-src/` đã có trên máy; bảng kiểm đúng các đường dẫn trong game. `media/media.config.json` đã có cả dragon-hold, typing-defense, typing-survival. Không dùng đường Downloads làm đích hiện tại. |
| README công cụ TD và `SOURCES.history` còn nói xe goòng chưa có; file 01/02 P nói Rễ Trồi chưa có | Bảng `SOURCES.files` hiện có **41** GLB, gồm goòng và Rễ Trồi, đã đối chiếu tồn tại thật. Hai mục này không nằm trong lượt dựng. |
| SOURCES TD có `notMadeYet: {}`, nhưng P18 và VS chưa có | SOURCES là kiểm kê file đã nhập, không phải danh mục thiết kế. Đối chiếu 42 P và 115 VS: thiếu Draconis P18 và toàn bộ VS; Trại Lính cũ có nhưng phải làm lại theo changelog. |
| Prompt TD cũ dùng `games/space-typing/art-src/td/…`, manifest `/assets/td/…` và nhiều rig Tripo | Theo nguồn game đã tách, ảnh TD dùng `games/typing-defense/art-src/…`, GLB dùng `art-src/3d/…`; rig theo luật phiếu và công cụ mới. Không giữ đoạn `td/` thừa, không chép đè media của Space. |
| Trại Lính cũ 1,8 m; ảnh mới chỉ được ghi ở `~/Downloads/td-tripo-2d/buildings/barracks-v2.png` trên Mac | Ghi “chờ ảnh” tại đích repo; không lấy `barracks.png` cũ thay ảnh làm lại. Model đích vẫn `barracks.glb`, face limit 10000. Rig cổng Blender là lựa chọn của phiếu, không phải yêu cầu bấm auto rig nhà trong Tripo. |
| Changelog TD ghi Mộc Tinh chưa có GLB đã rig; SOURCES lại có GLB | Hai loại file khác nhau: gốc `art-src/3d/bosses/moc-tinh.glb` đã có; bản rig `art-src/models/…` và clip hoàn chỉnh là việc Blender. Không yêu cầu tạo lại. |
| S1 nói scout/tank đã sẵn, đồng thời gọi chúng là bản sao tạm của Prism | Manifest có bản chạy giữ chỗ; GLB gốc `enemies/rainbow-scout.glb`, `enemies/rainbow-tank.glb` chưa có. Chỉ hai bản gốc thiếu được đưa vào bảng. Preset còn chỉ rõ tank tạm lấy **prism-scout**, không suy thành prism-tank. |
| S1 không quy định face limit Tripo cho hai Rainbow; phần lớn chỉ có Idle | Đề xuất 6000 theo ngân sách preset Space, đánh dấu rõ ở §1.1. Không rig vì chuyển động S1 là shader instanced; không tự thêm yêu cầu rig boss/Tổ đã có. |
| Mức chung TD nói phần nhánh 4000; bảng VS có nhánh 10000 và `keep-kit-l2` 8000 | File VS ghi rõ nhánh là công trình trọn, nên theo mức riêng từng dòng: 10000; vòng tường Lũy L2 là 8000. Không hạ tất cả về 4000. |

**Chủ dự án cần xem:** ba model mẫu Rồng và dấu Héo A/B; ảnh Trại Lính mới cần đưa về máy này; các lựa chọn khớp bẫy/cổng và clip đặc thù giao Blender; face limit đề xuất 6000 cho Rainbow. Tu Tiên tiếp tục chờ canon.

