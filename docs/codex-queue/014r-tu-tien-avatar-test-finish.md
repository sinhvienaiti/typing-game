# Phiếu 014r · Tu Tiên Thủ Ải · làm nốt phiếu 014 (avatar vẽ tay)

**Vì sao có phiếu này:** lượt chạy phiếu 014 dừng giữa chừng lúc khoảng 15:53 ngày 25/10 (tiến trình Codex mất, không có báo cáo). Đã có 6 ảnh cuối (a01–a06). a07 và a08 mới có bản lượt đầu bị loại (`*-rejected-1.png`) và prompt lượt 2 đã viết sẵn. Chưa có ảnh xem nhanh và README.

**Đọc trước:** phiếu gốc [`014-tu-tien-face-direction-test.md`](014-tu-tien-face-direction-test.md): phong cách, khung avatar, luật D47, ảnh xem nhanh, README. Phiếu này chỉ làm phần còn thiếu.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `games/immortality-cultivation/art-src/avatar-test/` (chỉ tạo `a07-thieu-nien-phu-tu.png`, `a08-nam-hoa-tu.png`);
- `games/immortality-cultivation/art-src/_review/014-avatar-test.jpg`;
- `games/immortality-cultivation/art-src/README-014.md`.

Không chạy git. **Không sửa, không tạo lại, không xóa** a01–a06 và mọi tệp `*-rejected-1.*`.

## Việc

1. **Tạo a07 và a08**, mỗi ảnh đúng một lần:
   - dùng **nguyên văn** prompt lượt 2 đã có: `avatar-test/a07-thieu-nien-phu-tu.prompt.txt`, `avatar-test/a08-nam-hoa-tu.prompt.txt` (không sửa prompt);
   - không đính kèm ảnh tham chiếu nào;
   - lưu `avatar-test/a07-thieu-nien-phu-tu.png`, `avatar-test/a08-nam-hoa-tu.png`, đưa về 1024 × 1024 (Lanczos, như a01–a06).
   - Mỗi mẫu đã dùng hết một lượt tạo lại của phiếu 014. Ảnh lần này còn lỗi thì vẫn giữ, ghi rõ lỗi vào README; không tạo thêm.
2. **Ảnh xem nhanh** `_review/014-avatar-test.jpg` theo phiếu gốc, bước 3:
   - lưới 4 × 2 theo thứ tự a01–a08, nhãn tiếng Việt (vai, tuổi);
   - một hàng thu nhỏ 128 px của cả 8 ảnh;
   - ImageMagick trong WSL: `~/.local/bin/magick montage`, font `/mnt/c/Windows/Fonts/arial.ttf`.
3. **`README-014.md`** theo phiếu gốc, bước 4:
   - mỗi ảnh một dòng: đạt chưa, khác các ảnh khác ở đâu;
   - với a01, a03, a07, a08: bản lượt đầu bị loại vì sao, bản giữ sửa được gì;
   - nhận xét chung về phong cách (vẽ tay hay còn bóng bẩy; còn nét mặt idol AI không; nhận ra được ở 128 px không).

**Xong khi:** đủ 8 ảnh cuối, có ảnh xem nhanh và README.
