# Phiếu 015b · Lời Gọi · làm nốt ảnh 2D còn thiếu (theo bản kiểm kê 015)

**Bối cảnh:** phiếu 015 (26/10/2026) kiểm kê ba game và làm 34 đích ảnh. Claude đã duyệt: đạt. Rồng Giữ Ải và Tuyến Cuối không còn thiếu ảnh nào. **Lời Gọi còn thiếu 248 ảnh**, liệt kê từng đích ở `docs/games/IMAGE_AUDIT_2026-10-25.md`:
- §6.2: 48 ảnh bậc P;
- §6.3: 200 ảnh VS dùng thẳng.

Phiếu này chạy nhiều lượt cho tới khi đủ, mỗi lượt tối đa 45 lần tạo.

**Thư mục làm việc:** gốc repo. Chỉ được ghi vào:
- `games/typing-defense/art-src/` (ảnh, prompt `.prompt.txt`, README giao nhận `README-015b.md`, ảnh xem nhanh `_review/015b-*.jpg`);
- `games/typing-defense/docs/art-requests/td/015b-delivery.md` (hàng chờ đã soạn prompt);
- §6.2, §6.3 và mục "Tổng" của `docs/games/IMAGE_AUDIT_2026-10-25.md`: chỉ đánh dấu đích đã xong.

Không chạy git, không sửa mã, không dùng `tools/art-normalize`. Không đụng Tu Tiên. Không ghi đè ảnh có sẵn: bản cũ đổi tên `.v1.png`.

## Việc
1. **Thứ tự:**
   - §6.2 bậc P trước, theo thứ tự bảng: cảnh S, phông F, chân dung C, đèn L, thẻ nhà U, nhịp U;
   - rồi §6.3 VS.
   - Mỗi lượt bỏ qua ảnh đã có, nên chạy lại là làm tiếp.
2. **Prompt:** ghép nguyên văn như 015 làm, theo bộ prompt `games/typing-defense/docs/art-requests/td/` (STYLE, phần riêng, biến thể, MATCH, nền). Không tự đổi phong cách.
   - Ghi trong README nếu thấy phong cách bộ prompt lệch rõ với ảnh 2D đã dùng trong game (ví dụ viền đen kiểu hoạt hình so với lối vẽ tô dày của công trình 005b). Chủ dự án quyết.
3. **Ảnh hỏng:**
   - ảnh hỏng rõ thì tạo lại tối đa 1 lần;
   - mỗi ảnh có `<tên>.prompt.txt`;
   - tự kiểm theo bảng kiểm của bộ prompt.
4. **Cuối mỗi lượt:**
   - cập nhật `README-015b.md`: bảng ảnh, lượt sinh, đạt hay chưa;
   - ghép một ảnh xem nhanh: ImageMagick `/opt/homebrew/bin/magick`, font `/System/Library/Fonts/Supplemental/Arial.ttf`;
   - đánh dấu đích đã xong trong IMAGE_AUDIT.

**Xong khi:** mọi đích §6.2 và §6.3 có ảnh, hoặc nằm trong danh sách còn lại có ghi lý do. Claude duyệt trước khi commit phần văn bản; ảnh đi Drive bằng `pnpm media:push`.
