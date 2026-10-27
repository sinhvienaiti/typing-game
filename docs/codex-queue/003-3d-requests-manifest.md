# Phiếu 003 · Danh sách ảnh 2D cần dựng 3D (mọi game), nhóm theo face limit và cách rig

**Mục tiêu:** chủ dự án sẽ tự dựng 3D trong Tripo từ ảnh 2D. Họ cần **một file** gom mọi ảnh 2D cần lên 3D, chia nhóm sẵn để làm một lượt:
- theo **face limit**;
- theo **cách rig**: Tripo tự rig (20 credit mỗi rig), tự rig trong Blender, hay không rig.

**Ghi vào:** `docs/games/3D_REQUESTS.md` (file mới, tiếng Việt). Thư mục làm việc: gốc repo `D:\typing-game`. Không sửa file nào khác. Không chạy git.

## Nguồn phải đọc

- **Rồng Giữ Ải:** `docs/games/dragon-lane/art-requests/m0/README.md` (§2 thứ tự, §3 thiết lập Tripo, §3.2 bảng face limit, rig, clip của 24 model) và các file `01`–`05` cùng thư mục. Ảnh 2D nằm ở `games/dragon-hold/art-src/` (Codex đang tạo ở phiếu 001, 002; ảnh nào chưa có thì ghi "chờ ảnh").
- **Lời Gọi:** `games/typing-defense/art-src/3d/SOURCES.json` (model đã có và nguồn), `games/typing-defense/scripts/models/README.md`, `games/typing-defense/docs/changelog/2026-10-24-models-*.md`, `games/space-typing/docs/art-requests/td/README.md` và `01-tripo-characters-enemies.md`, `02-tripo-buildings-props.md` (danh sách model TD và mục còn thiếu).
- **Tuyến Cuối:** `games/typing-survival/docs/` (tìm phần model và hình của S1). Game này dùng model của Space qua `/assets/space-typing/models/`. Chỉ ghi model **còn thiếu**.
- **Tu Tiên Thủ Ải** (`games/immortality-cultivation`): canon đang viết ở `docs/games/tu-tien/00-canon.md`. Có thì đọc phần mỹ thuật và M0b; chưa có thì để một mục "chờ canon".
- **Công cụ tự rig đã có trong repo:**
  - `games/typing-defense/scripts/models/blender/td_rig_*.py` (rig người, rig sinh vật không phải người, clip bằng script);
  - `games/space-typing/scripts/models/blender/space_typing_model_tools.py` (`make_dragon_clips`, `make_guide_clips`, `rigid_islands`, đo độ giãn lưới);
  - `scripts/models/blender/static_model_tools.py` (model tĩnh).

## Luật chọn cách rig (áp cho từng model, ghi lý do một dòng)

1. **Tripo rig** (Biped hoặc Quadruped, 20 credit): người hoặc quái hai chân đúng dáng chữ A, tỉ lệ thường, và preset clip của Tripo đủ dùng (Idle, Walk/Run, Attack, Death). Hợp với quái bầy: rẻ, nhanh, đủ tốt.
2. **Tự rig trong Blender** (0 credit, đẹp hơn với dáng lạ). Áp khi có ít nhất một điều sau:
   - dáng không chuẩn: côn trùng nhiều chân, có cánh, rắn hay Thuồng Luồng, cây yêu như Mộc Tinh;
   - Tripo không có preset clip cần dùng (cắn, vồ, húc, bay);
   - sinh vật chữ ký hoặc boss: chủ dự án chê chuyển động cứng và muốn chuyển động chồng lớp toàn thân;
   - vật có bộ phận cử động (bẫy, cổng);
   - Tripo rig đã hỏng với model đó.
   Trong Tripo vẫn bấm tạo model, **không bấm rig**: tải GLB không xương rồi giao Claude rig.
3. **Không rig:** prop, nhà, đá, cây, ô đất (gió và lay động làm bằng shader).
4. **Rig lai:** Tripo rig thân, Blender thêm xương phụ (đuôi, cánh, áo) và clip. Ghi rõ phần nào làm ở đâu.

## Nội dung file `docs/games/3D_REQUESTS.md`

1. **Tóm tắt.** Tổng số model theo game. Số model mỗi nhóm rig. Credit rig ước tính: số model Tripo rig × 20. Giá tạo model của Tripo thì ghi "theo gói" nếu tài liệu không nêu.
2. **Thiết lập Tripo chung**, chép đúng từ README §3 của Rồng Giữ Ải: Multiview khi có 2 góc, tách nền, Texture HD, PBR, lưới tam giác, Smart Low Poly tắt, tải GLB.
3. **Bảng nhóm:**
   - mỗi nhóm là một cặp (face limit, cách rig), ví dụ "6000 · Tripo Biped" hay "5000 · tự rig Blender";
   - mỗi dòng gồm: game, id, tên, ô ảnh Multiview (Front/Back/Left…) với đường dẫn ảnh 2D đầy đủ, face limit, rig, clip cần có, lý do chọn rig, nơi lưu GLB, trạng thái ảnh 2D (có / chờ ảnh).
4. **Thứ tự làm đề xuất:** mẫu duyệt trước (Rồng: E09, E18, E01), rồi theo nhóm để làm một lượt cùng thiết lập.
5. **Việc sau khi có GLB:** chép vào `art-src/3d/...` đúng tên, `pnpm models:index --root games/<game>`, `pnpm media:push`. Model tự rig thì báo Claude.

**Xong khi:** file liệt kê đủ model của Rồng Giữ Ải M0 (24) và mục còn thiếu của Lời Gọi và Tuyến Cuối, có mục Tu Tiên (đủ hoặc "chờ canon"), mọi model có lý do rig. Báo cáo cuối nêu số liệu tổng và những chỗ tài liệu nguồn mâu thuẫn.
