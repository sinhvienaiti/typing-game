# Phiếu 177 · Biểu tượng ứng dụng và favicon ba game

**Trạng thái: chưa hoàn thành — công cụ tạo ảnh hết hạn mức.** Ngày 30/10/2026, múi giờ Asia/Ho_Chi_Minh. Số bộ đủ điều kiện nhận: **0/3**. Chưa có ảnh sinh hoặc bản chọn; chưa có điểm M, Q.

## Đã chuẩn bị

Đã đọc phiếu 176, phiếu 177, `ART_ACCEPTANCE.md` §5 và thang M trong `ART_DIRECTION_2026-10-28.md` §1.3–1.4. Đã xem ảnh mẫu thương mại của chủ dự án và ba ảnh gốc:

- Dragonhold: `games/dragon-hold/art-src/ui/title-epic/keyart.png`, giữ nhận diện rồng lửa, màu cam than hồng và vật liệu hoa cương, vàng búa.
- Wordwoven: `games/typing-defense/art-src/ui/title-epic/emblem.png`, huy hiệu đã nhận; prompt giữ thiết kế mặt trời, rồng, chim và mây, đổi nền khóa màu hồng sang ngọc sẫm.
- Last Line: `games/typing-survival/art-src/models-src/lightbearer-front.png`, giữ dáng mũ, giáp trắng vàng, mặt than chì và khe sáng lam của Lightbearer.

Đã tạo ba thư mục mới, mỗi thư mục có `app-icon.prompt.txt` và `app-icon.try1.prompt.txt`:

- `games/dragon-hold/art-src/ui/app-icon/`
- `games/typing-defense/art-src/ui/app-icon/`
- `games/typing-survival/art-src/ui/app-icon/`

Prompt mở bằng khối STYLE-UI của đúng game, yêu cầu 1024 × 1024, nền đặc, góc vuông, không chữ và khối chính đọc được ở 32/16 px. Hai prompt Wordwoven và Last Line là **prompt dự kiến, chưa gọi**; đuôi `.try1.prompt.txt` không phải bằng chứng có ảnh sinh.

## Trở ngại

Đã gọi công cụ tích hợp `image_gen` đúng một lần cho **Dragonhold · app-icon**, đính kèm ảnh chủ đạo sau khi xem ảnh. Công cụ từ chối trước khi trả ảnh:

```text
http 429 Too Many Requests
error.type: usage_limit_reached
error.message: The usage limit has been reached
plan_type: plus
resets_at: 1793364445
resets_in_seconds: 63077
```

Thời điểm đặt lại do công cụ cung cấp: **30/10/2026, 19:47:25 (UTC+7)**. Đây là thông tin tại lần gọi, không phải bảo đảm lần gọi sau thành công. Bản ghi lỗi: `games/typing-defense/art-src/ui/app-icon/177-generation-status.json`.

Không gọi Wordwoven hoặc Last Line tiếp vì cùng công cụ đã hết hạn mức. Không dùng dịch vụ hay API khác để thay công cụ được giao. Không tạo ảnh giả bằng mã hoặc coi ảnh tham chiếu là ảnh giao.

## Kiểm và phần bỏ qua

| Game | Lượt gọi | Ảnh 1024 | Bản thu 512/192/180/64/32/16 | M1024 / Q1024 | M32 / Q32 |
|---|---:|---|---|---|---|
| Dragonhold | 1, lỗi 429 | Chưa có | 0/6 | Chưa chấm / Chưa chấm | Chưa chấm / Chưa chấm |
| Wordwoven | 0 | Chưa có | 0/6 | Chưa chấm / Chưa chấm | Chưa chấm / Chưa chấm |
| Last Line | 0 | Chưa có | 0/6 | Chưa chấm / Chưa chấm | Chưa chấm / Chưa chấm |

- **Kiểm 1:** chưa đo khổ, độ đặc của nền và kiểm không chữ vì chưa có ảnh. Tổng bản chọn và bản thu: **0/21**.
- **Kiểm 2:** chưa kiểm nhận diện ba dáng ở 32/16 px trên nền tab sáng và tối; chưa có căn cứ quyết định cần `app-icon-small` hay không.
- **KA5:** chưa chấm M/Q; không gán điểm 0 cho ảnh chưa tồn tại và không tuyên bố đạt ngưỡng 8.
- **Hậu kỳ §5:** chưa có hậu kỳ hay tờ “bản sinh | bản hậu kỳ”. Chưa tạo `games/typing-defense/art-src/_review/177-icons.jpg`; không tạo tờ trống để giả bằng chứng. Chưa có mâu thuẫn giữa số đo và tranh để kết luận.

## KA1 · Bảo toàn tệp

Kiểm kê MD5 trước/sau lưu tại:

- `games/typing-defense/art-src/ui/app-icon/177-md5-before.json`
- `games/typing-defense/art-src/ui/app-icon/177-md5-after.json`

Bản trước kiểm kê riêng ba thư mục đích (đều chưa tồn tại), thư mục `_review` của Wordwoven và đường dẫn báo cáo (chưa tồn tại). Bản sau giữ cùng phạm vi, loại chính manifest sau để tránh tự băm. Đối chiếu ngay trước khi viết báo cáo: **0 tệp đã có đổi MD5, 0 tệp đã có không còn ở vị trí cũ**. Các biến động nếu có chỉ là quan sát trạng thái vì tác vụ khác chạy đồng thời.

Tác vụ chỉ tạo tệp mới trong ba thư mục `app-icon/` và báo cáo này. Không ghi đè, đổi tên hoặc xóa tệp đã có; không chạy lệnh Git, build, test, máy chủ, trình duyệt hay mạng ngoài công cụ tạo ảnh; không chạm Tu Tiên.

## Chủ dự án cần xem

Chưa có tranh để duyệt. Sau khi hạn mức được đặt lại, tiếp tục từ các prompt đã lưu và đính kèm đúng ảnh gốc. Giữ từng lượt sinh, tối đa ba lượt cho mỗi ảnh. Khi có bản 1024, thu Lanczos đủ sáu cỡ và lưu prompt cạnh từng ảnh; xem bản thật ở 32/16 trên hai nền tab. Chỉ sinh riêng `app-icon-small` 256 × 256 khi bản thu không đọc được. Làm đủ tờ trước/sau và tờ tổng hợp có ảnh mẫu, rồi chấm M/Q trên bản hậu kỳ ở 1024 và 32. Phiếu chỉ xong khi đủ ba bộ và đạt toàn bộ điều kiện nhận.
