# Phiếu 176 · Ảnh bìa cổng game

**Trạng thái: chưa hoàn thành — công cụ tạo ảnh hết hạn mức.** Ngày 30/10/2026, múi giờ Asia/Ho_Chi_Minh. Chưa có ảnh sinh, bản chọn hoặc điểm nhận.

## Đã chuẩn bị

Đã đọc `ART_DIRECTION_2026-10-28.md` §1.3, §2.2, §3.2, §4.3 và `ART_ACCEPTANCE.md`, gồm luật hậu kỳ §5. Đã xem ảnh mẫu của chủ dự án và ba tranh tham chiếu:

- Dragonhold: `games/dragon-hold/art-src/ui/title-epic/keyart.png` của phiếu 119 đã có; dùng tranh này.
- Wordwoven: `games/typing-defense/art-src/ui/title-epic/keyart.png`.
- Last Line: `games/typing-survival/art-src/concepts/b-lightbearer-keyart.png`, hướng B.

Đã tạo ba thư mục đích mới:

- `games/dragon-hold/art-src/ui/cover/`
- `games/typing-defense/art-src/ui/cover/`
- `games/typing-survival/art-src/ui/cover/`

Mỗi thư mục có `cover-wide.prompt.txt`, `cover-wide.try1.prompt.txt`, `cover-square.prompt.txt`, `cover-square.try1.prompt.txt`. Đây là sáu prompt đầy đủ, với bản sao dành cho lượt một: mở bằng khối STYLE nguyên văn, có đúng câu chỉ dẫn tham chiếu, quy cách 1600 × 900 hoặc 1024 × 1024, bố cục mới và vùng yên trong một phần ba dưới. Các tệp `.try1.prompt.txt` chỉ lưu prompt dự kiến; chúng không phải bằng chứng đã sinh được ảnh.

## Trở ngại và phần bỏ qua

Đã gọi công cụ tích hợp `image_gen` một lần cho **Dragonhold · cover-wide**, đính kèm đường dẫn tuyệt đối của tranh 119 sau khi xem ảnh. Công cụ từ chối trước khi trả ảnh:

```text
http 429 Too Many Requests
error.type: usage_limit_reached
error.message: The usage limit has been reached
plan_type: plus
resets_at: 1793364445
resets_in_seconds: 63232
```

Thời điểm đặt lại do công cụ cung cấp: **30/10/2026, 19:47:25 (UTC+7)**. Đây là thông tin tại lần gọi, không phải bảo đảm lần sau sẽ sinh được.

Không gọi năm ảnh còn lại vì cùng công cụ đã hết hạn mức. Không dùng API, dịch vụ khác, ảnh có sẵn hoặc tranh vẽ bằng mã để thay sáu ảnh yêu cầu. Không có tệp ảnh đầu ra do công cụ trả về; không có ảnh `.try1.png` hay bản chọn `.png`.

| Game | Ảnh | Lượt gọi công cụ | Bản chọn | M | Q |
|---|---|---:|---|---|---|
| Dragonhold | cover-wide | 1, bị từ chối 429 | Chưa có | Chưa chấm | Chưa chấm |
| Dragonhold | cover-square | 0 | Chưa có | Chưa chấm | Chưa chấm |
| Wordwoven | cover-wide | 0 | Chưa có | Chưa chấm | Chưa chấm |
| Wordwoven | cover-square | 0 | Chưa có | Chưa chấm | Chưa chấm |
| Last Line | cover-wide | 0 | Chưa có | Chưa chấm | Chưa chấm |
| Last Line | cover-square | 0 | Chưa có | Chưa chấm | Chưa chấm |

Vì chưa có tranh, chưa thực hiện hậu kỳ, tờ “bản sinh | bản hậu kỳ”, đo khổ và độ lệch chuẩn luma, kiểm không chữ, kiểm đọc ở 320 × 180 hoặc KA5. Chưa tạo `games/typing-defense/art-src/_review/176-portal.jpg` 1280 × 720. Không có xung đột giữa ngưỡng số và tranh để kết luận. **Số ảnh đủ điều kiện nhận: 0/6.**

## KA1 · Bảo toàn tệp

Kiểm kê MD5 từng thư mục đích trước và sau được lưu tại:

- `games/typing-defense/art-src/ui/cover/176-md5-before.json`
- `games/typing-defense/art-src/ui/cover/176-md5-after.json`

Bản trước bao gồm ba thư mục cover (đều chưa tồn tại), thư mục `_review` của Wordwoven và `docs/codex-queue`; bản sau liệt kê từng tệp cùng MD5. Manifest sau loại chính nó khỏi kiểm kê để tránh tự băm. Các biến động của tệp đã có được ghi trong manifest sau; đây là so sánh trạng thái, không quy kết tác giả vì có tác vụ khác chạy đồng thời.

Đối chiếu ngay trước khi viết báo cáo: 0 tệp đã có đổi MD5, 0 tệp đã có không còn ở vị trí cũ. Tác vụ này chỉ tạo tệp mới ở ba thư mục cover và báo cáo này. Không chạy lệnh Git, build, test, máy chủ, trình duyệt hoặc mạng ngoài lần gọi tạo ảnh; không chạm Tu Tiên.

## Chủ dự án cần xem

Chưa có tranh để duyệt. Sau khi hạn mức được đặt lại, tiếp tục từ sáu prompt đã lưu, đính kèm đúng tranh tham chiếu; giữ từng lượt sinh, tối đa ba lượt mỗi ảnh. Khi có ảnh, chỉ hậu kỳ được phép theo §5; nếu đo luma đòi phá tranh thì giữ tranh và ghi mâu thuẫn. Chỉ đánh dấu xong sau khi đủ sáu bản chọn, sáu tờ trước/sau, tờ cổng có ảnh mẫu và số đo cùng điểm M ≥ 8, Q ≥ 8 trên bản hậu kỳ.
