# Phiếu 184 · Ba game · Tranh màn tải và mẹo chơi

**Trạng thái: chưa xong, bị chặn bởi hạn mức công cụ tạo ảnh. Có 0/12 ảnh; chưa có bản chọn, chưa tự chấm M/Q.**

## 1. Điểm chặn

Lời gọi `image_gen.imagegen` đầu tiên, cho `dragon-hold/loading`, trả lỗi HTTP **429**, loại **`usage_limit_reached`**, thông báo “The usage limit has been reached”. Công cụ không trả ảnh hoặc đường dẫn ảnh. Đây là lỗi hạn mức, không phải một bản sinh bị loại vì chất lượng. Không gọi tiếp 11 ảnh còn lại và không dùng CLI/API thay thế công cụ tích hợp mà chủ dự án yêu cầu.

Công cụ báo `resets_at = 1793364446`, tương ứng **19:47:26 ngày 30/10/2026, giờ Việt Nam**. Đây là thời điểm do phản hồi lỗi cung cấp, chưa xác minh hạn mức đã mở lại. Phản hồi lỗi được ghi ở [imagegen-error.json](../../games/typing-defense/art-src/_review/184/imagegen-error.json).

## 2. Những gì đã chuẩn bị

Đã đọc phiếu 176, phiếu 184, `ART_ACCEPTANCE.md` (đặc biệt §5), các khối STYLE trong `ART_DIRECTION_2026-10-28.md` và hướng dẫn của ba game. Dùng skill `imagegen`. Đã xem ảnh chủ đạo của từng game và ảnh tham chiếu thương mại của chủ dự án.

Mỗi thư mục dưới đây có tám tệp văn bản mới: `loading.prompt.txt`, `tip-1.prompt.txt`, `tip-2.prompt.txt`, `tip-3.prompt.txt` và bốn tệp tương ứng `.try1.prompt.txt`.

| Game | Thư mục | Ảnh tham chiếu đã chọn |
|---|---|---|
| Dragonhold | `games/dragon-hold/art-src/ui/loading/` | `games/dragon-hold/art-src/ui/title-epic/keyart.png` |
| Wordwoven | `games/typing-defense/art-src/ui/loading/` | `games/typing-defense/art-src/ui/title-epic/keyart.png` |
| Last Line | `games/typing-survival/art-src/ui/loading/` | `games/typing-survival/art-src/concepts/b-lightbearer-keyart.png` |

**Các tệp `.prompt.txt` là prompt đã chuẩn bị, không phải bằng chứng có ảnh hoặc đã chọn ảnh.** Chỉ prompt `dragon-hold/loading.try1.prompt.txt` đã được gửi vào công cụ; 11 prompt còn lại chưa gọi. Khi tiếp tục, không tính lỗi hạn mức này là một lượt ảnh đã sinh. Mỗi prompt bắt đầu bằng khối STYLE nguyên văn, chỉ định tham chiếu thế giới/nhân vật/màu, cấm chữ, và mô tả đúng thao tác của phiếu. Prompt màn tải yêu cầu dải dưới tối ngay từ bố cục và chiếu sáng gốc; không dự kiến phủ hộp tối khi hậu kỳ.

Bộ prompt cùng đường dẫn tham chiếu được lưu ở [generation-plan.json](../../games/typing-defense/art-src/_review/184/generation-plan.json). Đây là hồ sơ chuẩn bị, không phải nhật ký thành công của công cụ.

## 3. KA1 và phạm vi

Ba thư mục đích đều chưa tồn tại trước tác vụ. MD5 trước/sau được lưu tại `games/typing-defense/art-src/_review/184/`, với tên `<game>.md5-before.txt`, `<game>.md5-after.txt`; bản tổng hợp là [ka1-before.json](../../games/typing-defense/art-src/_review/184/ka1-before.json) và [ka1-after.json](../../games/typing-defense/art-src/_review/184/ka1-after.json).

| Game | Tệp trước | Tệp sau | Thêm | Đổi MD5 | Mất |
|---|---:|---:|---:|---:|---:|
| Dragonhold | 0 | 8 | 8 | 0 | 0 |
| Wordwoven | 0 | 8 | 8 | 0 | 0 |
| Last Line | 0 | 8 | 8 | 0 | 0 |

Chỉ thêm prompt trong ba thư mục đích, hồ sơ kiểm ở `_review/184/` và báo cáo này. Không sửa mã, tài liệu game, media có sẵn, Tu Tiên hoặc Audio Lab. Không chạy lệnh Git, build, test game, dev server, trình duyệt hay mạng ngoài lời gọi tạo ảnh.

## 4. Những mục chưa làm và việc cần xem

- **Chưa có 12 ảnh** `loading.png` (1920 × 1080) và `tip-1.png`–`tip-3.png` (1024 × 640), cũng chưa có ảnh `.tryN.png`: công cụ chưa trả ảnh.
- **Chưa hậu kỳ, chưa có tờ “bản sinh | bản hậu kỳ”** cho từng ảnh. Không có tranh để đổi cỡ hoặc đối chiếu.
- **Chưa có `games/typing-defense/art-src/_review/184-sheet.jpg`**: không ghép tranh tham chiếu thành tờ giao nhận để thay ảnh được yêu cầu.
- **Chưa kiểm** khổ ảnh thực, chữ thừa, WCAG ≥ 7 trên toàn dải dưới 20 %, độ rõ thao tác ở 320 × 200, hay KA5. M và Q của cả 12 ảnh đều **chưa chấm**, không ghi điểm đạt khi chưa có bản hậu kỳ để xem.
- Chủ dự án cần xem điểm chặn hạn mức ở mục 1. Khi công cụ dùng được, tiếp tục từ bộ prompt đã lưu, tạo từng ảnh kèm tham chiếu, giữ mọi lượt thử, kiểm và tự chấm trên bản giao; tối đa ba ảnh sinh mỗi tấm. Nếu số đo dải dưới mâu thuẫn với tranh đẹp, giữ tranh và ghi lại theo §5, không phủ hoặc san phẳng phần vẽ.

Phiếu **chưa đạt điều kiện hoàn thành** và chưa có ảnh nào để duyệt nhận.
