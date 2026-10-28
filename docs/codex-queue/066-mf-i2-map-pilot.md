# Phiếu 066 · Bản thử bản đồ Rồng L2-cau · MF-I2: Maple Tree dự phòng, hai sắc (pine-river)

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-I2. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/066-report.md`.

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

## MF-I2 · [codex-image] Maple Tree dự phòng, hai sắc (pine-river)

**Cần trước:** không. Chỉ dùng nếu cây tán tròn có sẵn nhuộm sắc ấm dưới 8 điểm (CL-05).

**Chỉ được ghi:** `games/dragon-hold/art-src/props/pine-river/{maple-tree-rust,maple-tree-copper}.*`, `_review/MF-I2*`.

**Việc:** một cây lá rộng mùa thu, thân lộ rõ từ góc 55° và 75°, tán thành 3–5 khối lá tròn mềm như các cây của bộ, cao 6 m, khổ 1024×1536. Hai bản: tán **gỉ sắt** và tán **đồng**. Dáng tán khác cây tròn và thông của bộ.

**Kiểm (bắt buộc):** KA1–KA3, KA5; thay KA4 bằng:
1. Mặt nạ tán (hue 0–60°, s > 0,25, trong vùng vật): hue trung vị 10–30°, s trung vị ≤ 0,70, v trung vị ≤ 0,70.
2. ΔE2000 của màu tán trung vị so với #FF4A4A, #FFB020, #FFC83A và vàng Héo #C8D24A, mỗi số ≥ 20. In bốn số.
3. Px ngoài tán: KA4 như thường.

**Xong khi:** hai ảnh đạt chung 1.1 và ba kiểm trên.
