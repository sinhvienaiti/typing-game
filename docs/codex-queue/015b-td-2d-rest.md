# Phiếu 015b · Lời Gọi · làm nốt ảnh 2D còn thiếu (theo bản kiểm kê 015)

**Bối cảnh:** phiếu 015 (26/10/2026) kiểm kê ba game và làm 34 đích ảnh. Claude đã duyệt: đạt. Rồng Giữ Ải và Tuyến Cuối không còn thiếu ảnh nào. **Lời Gọi còn thiếu 248 ảnh lúc kiểm (25/10)**, liệt kê từng đích ở `docs/games/IMAGE_AUDIT_2026-10-25.md`:
- §6.2: 48 ảnh bậc P;
- §6.3: 200 ảnh VS dùng thẳng.

**Cập nhật 26/10 tối:** đã có 32 đích (lượt 1 và 2). Theo luật mới chỉ làm các đích mức **P1, P2** trong `games/typing-defense/docs/art-requests/td/015b-priority.md` (60 đích lúc xếp; bỏ qua đích đã có). 166 đích P3 chờ kinh phí. Lượt 2 đã lỡ làm 6 ảnh núm nhịp U8–U13 (P3, game đã bỏ núm nhịp từ 1A.6): giữ file, không làm thêm.

Phiếu này chạy nhiều lượt cho tới khi đủ, mỗi lượt tối đa 45 lần tạo.

**Thư mục làm việc:** gốc repo. Chỉ được ghi vào:
- `games/typing-defense/art-src/` (ảnh, prompt `.prompt.txt`, README giao nhận `README-015b.md`, ảnh xem nhanh `_review/015b-*.jpg`);
- `games/typing-defense/docs/art-requests/td/015b-delivery.md` (hàng chờ đã soạn prompt);
- §6.2, §6.3 và mục "Tổng" của `docs/games/IMAGE_AUDIT_2026-10-25.md`: chỉ đánh dấu đích đã xong.

Không chạy git, không sửa mã, không dùng `tools/art-normalize`. Không đụng Tu Tiên. Không ghi đè ảnh có sẵn: bản cũ đổi tên `.v1.png`.

## Luật duyệt mới (chủ dự án, 26/10/2026): đọc trước khi làm

Đọc `docs/games/ART_ACCEPTANCE.md`. Tóm tắt:
- chi phí ảnh rất đắt: ảnh từ 7/10 điểm là nhận, **không tạo lại**;
- chỉ tạo lại khi sai quá, không sửa được (sai đề, giải phẫu sai lớn, lệch hẳn phong cách); lỗi khung, lề, nền, khổ là lỗi sửa được bằng công cụ, Claude sửa sau;
- số lượng chi tiết lệch nhẹ so với prompt (7 thân thay vì 9) không phải lỗi;
- ưu tiên ảnh cần thiết.

Luật này thay mọi câu "chưa đạt" khắt khe hơn trong bộ prompt và trong README-015b lượt 1.

## Việc
1. **Thứ tự:** mọi đích của §6.2 và §6.3 làm theo **thứ tự P1 rồi P2 của `games/typing-defense/docs/art-requests/td/015b-priority.md`** (một danh sách chung; C23, C21 của §6.3 đi trước U7, U14–U28 của §6.2).
   - Đích P3 không làm, kể cả U8–U13 và X12 của §6.2.
   - Đọc mục "Cách dùng" và "Phong cách" của file đó trước.
   - Mỗi lượt bỏ qua ảnh đã có, nên chạy lại là làm tiếp.
2. **Prompt:** ghép nguyên văn như 015 làm, theo bộ prompt `games/typing-defense/docs/art-requests/td/` (STYLE, phần riêng, biến thể, MATCH, nền). Không tự đổi phong cách.
   - Ghi trong README nếu thấy phong cách bộ prompt lệch rõ với ảnh 2D đã dùng trong game (ví dụ viền đen kiểu hoạt hình so với lối vẽ tô dày của công trình 005b). Chủ dự án quyết.
3. **Chấm và tạo lại:**
   - tự chấm từng ảnh theo thang 10 điểm của `ART_ACCEPTANCE.md`; dùng bảng kiểm của bộ prompt làm gợi ý, không phải điều kiện đạt;
   - từ 7 điểm: nhận. Dưới 9 thì ghi "tạm chấp nhận" kèm thiếu gì;
   - dưới 7 mà lỗi sửa được bằng công cụ: không tạo lại, ghi "cần sửa: <việc>";
   - chỉ tạo lại khi dưới 7 và không sửa được, tối đa 1 lần; giữ cả hai bản;
   - mỗi ảnh có `<tên>.prompt.txt`.
4. **Cuối mỗi lượt:**
   - cập nhật `README-015b.md`: bảng ảnh, lượt sinh, **điểm, mức** (Đạt / Tạm chấp nhận / Sửa / Tạo lại) và thiếu gì;
   - ghép một ảnh xem nhanh: ImageMagick `/opt/homebrew/bin/magick`, font `/System/Library/Fonts/Supplemental/Arial.ttf`;
   - đánh dấu đích đã xong trong IMAGE_AUDIT.

**Xong khi:** mọi đích P1, P2 trong `015b-priority.md` có ảnh từ 5 điểm trở lên, hoặc nằm trong danh sách còn lại có ghi lý do. Claude duyệt trước khi commit phần văn bản; ảnh đi Drive bằng `pnpm media:push`.
