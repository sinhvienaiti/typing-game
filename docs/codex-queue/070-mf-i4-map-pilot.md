# Phiếu 070 · Bản thử bản đồ Rồng L2-cau · MF-I4: Sprite sự sống B: lá rơi, khói, đom đóm, bóng mây

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-I4. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/070-report.md`.

## Luật chung: 1.1 Mọi phiếu ảnh Codex

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh ghi vào `art-src` của game (media, không vào Git).
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Chưa đạt thì sửa prompt, tối đa 3 lượt mỗi ảnh. Ảnh nguồn Tripo không nướng ánh sáng hay vùng phát sáng.
- **Chỉ được ghi:** đúng các file phiếu liệt kê; mỗi lượt thử là `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3); bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`; `art-src/_review/<mã phiếu>-*.jpg` và `art-src/_review/<mã phiếu>/`; file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git;
  - sửa mã hay tài liệu;
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - đụng game khác ngoài game của phiếu; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, logo, người, thần, nơi thờ trong ảnh.
- **Kiểm chung, bắt buộc:**
  - **KA1 md5:** `md5 -r` mọi file trong thư mục đích trước (`_review/<mã>/md5-before.txt`) và sau; `diff` chỉ có dòng của file mới.
  - **KA2 khổ và nền:** `magick identify` đúng khổ; với ảnh nguồn Tripo, 10 px mép bốn phía có độ lệch chuẩn ≤ 6/255 và màu trung bình gần `#E6E6E6` (mỗi kênh lệch ≤ 8); với sprite và decal, alpha sạch (không viền nền).
  - **KA3 lề:** ảnh nguồn Tripo cắt nền bằng `magick <ảnh> -fuzz 12% -trim -format '%X %Y %w %h' info:`; vật cách mép ≥ 24 px.
  - **KA4 màu giữ riêng:** tỉ lệ px có hue 0–50° hoặc 165–190°, saturation > 0,55, value > 0,5 phải ≤ 2 % (trừ khi phiếu cho phép rõ, như cây tán ấm có dải riêng).
  - **KA5 tự chấm:** 5 tiêu chí của §2.2, ở cỡ đầy đủ và ở 128 px; ghi điểm từng lượt.
- **Báo cáo:** tiếng Việt; file tạo ra; số đo từng kiểm; điểm từng lượt; lượt chọn và lý do.
- **Xong khi (chung):** KA1–KA5 đạt và bản chọn tự chấm ≥ 8. **Nhận** khi Claude chấm lại ≥ 8.

## MF-I4 · [codex-image] Sprite sự sống B: lá rơi, khói, đom đóm, bóng mây

**Cần trước:** không.

**Chỉ được ghi:** `games/dragon-hold/art-src/fx/life/{leaf-fall,smoke-puff,firefly,cloud-shadow}.*` và `.json`, `_review/MF-I4*`.

**Việc:**
- `leaf-fall.png`: 4 biến thể lá (2 xanh, 2 gỉ sắt cùng dải MF-I2), mỗi cái 4 khung xoay; ô 32 px.
- `smoke-puff.png`: 6 khung làn khói xám mềm, ô 128 px, alpha mềm.
- `firefly.png`: một chấm sáng mềm vàng xanh nhạt, 32 px (không vàng kim #FFC83A).
- `cloud-shadow.png`: ô xám 512² liền mép, nhiễu mây thấp tần, chỉ kênh độ sáng.

**Kiểm (bắt buộc):** KA1, KA5; alpha sạch; đúng lưới theo JSON; `cloud-shadow` lệch mép khi lát nửa ô ≤ 2 % (in số); mỗi tờ ≤ 256 KB; KA4 = 0 % trừ lá gỉ (in tỉ lệ).

**Xong khi:** các kiểm đạt, tự chấm ≥ 8.
