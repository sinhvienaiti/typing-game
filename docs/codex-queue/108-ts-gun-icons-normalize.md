# Phiếu 108 · Tuyến Cuối · Chuẩn hóa 6 icon súng bằng công cụ (không tạo ảnh mới)

**Vì sao:** kiểm kê map 1 (TS-M1-09, P1, cổng G2). Thẻ súng ở màn nạp súng, kho súng và đầu bến hôm nay chỉ có chữ. Claude sẽ gắn icon vào (TS-M1-10). Sáu icon có sẵn (8–8,5 điểm, `docs/games/ART_REPLACE_LATER.md`) đều 1254 × 1254, lề chỉ 1,6–3,9 %; ghi chú cũ là "co và đệm bằng công cụ khi lắp". Phiếu này làm phần đó.

**Báo cáo:** `docs/codex-queue/108-report.md`.

## Luật chung (phiếu ảnh, chỉ dùng công cụ)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Không gọi công cụ tạo ảnh.** Chỉ dùng ImageMagick 7, hoặc Node hay Python viết riêng (lưu script vào `_review/108/`).
- **Chỉ được ghi:**
  - `games/typing-survival/art-src/ui/icons/<tên>.norm.png`, `<tên>.norm.256.png`, `<tên>.norm.128.png`, `<tên>.norm.64.png`;
  - `games/typing-survival/art-src/_review/108-*.jpg` và `_review/108/`;
  - file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn;
  - mọi lệnh git; sửa mã hay tài liệu;
  - dev server, trình duyệt;
  - đụng game khác, Tu Tiên.

## Sáu icon

`gun-xung` (Pulse Gun), `gun-tia` (Heat Beam), `gun-tan` (Scatter Gun), `gun-ray` (Rail Gun), `gun-phao-sao` (Star Mortar), `nova`. Nguồn là `games/typing-survival/art-src/ui/icons/<tên>.png`; bản `.v1.png` không dùng.

## Việc

1. Cắt sát hộp bao của alpha > 16.
2. Đặt hình vào giữa canvas vuông trong suốt, sao cho lề mỗi phía đúng 15 % cạnh. Cạnh dài của hình bằng 70 % canvas; giữ nguyên tỉ lệ hình.
3. Thu về 1024 × 1024 bằng Lanczos → `<tên>.norm.png`. Từ bản 1024 làm thêm `.norm.256.png`, `.norm.128.png`, `.norm.64.png`.
4. Không đổi màu, không làm nét. Riêng bản 64 px được `-unsharp 0x0.6+0.6+0` một lần nếu thấy nhòe; ghi rõ vào báo cáo.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `art-src/ui/icons/` trước (`_review/108/md5-before.txt`) và sau. `diff` chỉ có dòng của file mới.
2. **Khổ:** đúng 1024, 256, 128, 64.
3. **Lề:** ở bản 1024, hộp bao alpha > 16 cách mỗi mép 148–160 px; hình không bị cắt. Ghi bảng 4 lề × 6 icon.
4. **Alpha sạch:** alpha min 0, max 255; vùng alpha 1–254 có luma trung bình lệch ≤ 0,08 so với luma vùng alpha 255 sát bên, để không có viền sáng hay tối lạ.
5. **Tờ xem** `_review/108-sheet.jpg`:
   - hàng 1: sáu icon 1024 thu về 256 trên nền `#0e1116` (màu bảng HUD tối);
   - hàng 2: sáu icon ở 64 px và 32 px trên cùng nền;
   - hàng 3: sáu icon 64 px trên nền màu thẻ súng `#1a1f27`, có viền 1 px màu súng (xanh, cam), để xem có lẫn viền không.
   Ghi vào báo cáo icon nào khó nhận ở 32 px (ghi chú cũ: viên của Tán dính thành cụm, Pháo Sao mảnh).

**Xong khi:** mục Kiểm 1–4 đạt cho cả 24 file. Claude xem tờ rồi gắn vào thẻ súng.
