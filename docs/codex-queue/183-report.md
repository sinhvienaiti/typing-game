# Phiếu 183 · Tranh thắng và thua cho ba game

**Trạng thái: chưa hoàn thành — công cụ tạo ảnh hết hạn mức.** Chưa có ảnh sinh, ảnh chọn hay điểm tự chấm M/Q. Không đánh dấu đạt khi chưa có tranh để kiểm.

## Đã làm

- Đọc phiếu 176, `ART_ACCEPTANCE.md` §5 và các khối STYLE của Wordwoven §2.2, Dragonhold §3.2, Last Line §4.3 hướng B trong `ART_DIRECTION_2026-10-28.md`.
- Xem ảnh chủ đạo của từng game và ảnh chuẩn thương mại của chủ dự án. Dự kiến giữ nhân vật, vật liệu và bảng màu; bố cục mới đặt hành động bên trái, để nửa phải yên ngay trong bản sinh.
- Ghi KA1 trước và sau trên ba thư mục `art-src/ui/results/` và thư mục tờ duyệt được giao. Tổng cộng **11.554 file có sẵn**, **0 file đổi MD5**, **0 file bị mất**.
- Gửi một yêu cầu sinh `Dragonhold / victory` bằng công cụ tích hợp `image_gen`, đính kèm `games/dragon-hold/art-src/ui/title-epic/keyart.png`. Prompt gửi nguyên văn từ `games/dragon-hold/art-src/ui/results/victory.try1.prompt.txt` có sẵn; không sửa hay ghi đè prompt đó.

## Điểm dừng

Công cụ trả HTTP **429**, loại lỗi **`usage_limit_reached`**, thông báo **`The usage limit has been reached`**. Lỗi xảy ra trước khi công cụ trả ảnh hoặc đường dẫn đầu ra. Phản hồi ghi `plan_type: plus`, `resets_at: 1793364445`, `resets_in_seconds: 63728` tại lúc gọi.

Thời điểm mở lại do công cụ cung cấp: **19:47:25 ngày 30/10/2026, giờ Việt Nam (UTC+7)**. Đây là mốc từ phản hồi lỗi, chưa xác nhận khả năng gọi sau mốc đó.

Không gọi lặp năm ảnh còn lại khi công cụ đã báo hết hạn mức; không dùng API, dịch vụ hay công cụ sinh khác thay thế. Yêu cầu đầu tiên thất bại, không có lượt sinh thành công.

## Bàn giao theo ảnh

| Game | Đích dưới `art-src/ui/results/` | Tình trạng |
|---|---|---|
| Dragonhold | `victory.png` | Yêu cầu đầu tiên bị chặn bởi hạn mức; chưa có ảnh |
| Dragonhold | `defeat.png` | Chưa gọi vì cùng hạn mức |
| Wordwoven | `victory.png` | Chưa gọi vì cùng hạn mức |
| Wordwoven | `defeat.png` | Chưa gọi vì cùng hạn mức |
| Last Line | `victory.png` | Chưa gọi vì cùng hạn mức |
| Last Line | `defeat.png` | Chưa gọi vì cùng hạn mức |

Ba thư mục đích đều đã có các file `victory.try1.prompt.txt` và `defeat.try1.prompt.txt` trước phiên này (sáu prompt trong ba thư mục). Phiên này giữ nguyên chúng. Chưa tạo bản chọn `.png` hoặc `.prompt.txt` của bản chọn.

## File tạo trong phiên

- `docs/codex-queue/183-report.md` — báo cáo này.
- `games/typing-defense/art-src/_review/183-ka1-before.json` — MD5 trước khi ghi file của phiếu.
- `games/typing-defense/art-src/_review/183-ka1-after.json` — MD5 sau yêu cầu sinh thất bại và đối chiếu file có sẵn. Bản kê sau không tự chứa MD5 của chính nó.

## Chưa thực hiện và việc cần xem

Chưa thể kiểm khổ 1600 × 900, độ lệch chuẩn luma hai nửa, khả năng đọc ở 480 × 270, tờ “bản sinh | bản hậu kỳ”, tờ tổng hợp `games/typing-defense/art-src/_review/183-sheet.jpg` hay KA5 M/Q vì chưa có ảnh. Không tạo tờ giả hoặc chấm điểm từ prompt.

Khi công cụ được cấp lại hạn mức, tiếp tục sinh và giữ `.tryN.*`, lưu prompt chính xác cạnh từng ảnh, chỉ đổi cỡ nếu cần, làm tờ so và tự chấm trên bản hậu kỳ. Nếu chỉ số luma mâu thuẫn với tranh đẹp, giữ tranh và ghi lại theo §5; không phủ mảng tối lên tranh.

Chủ dự án cần xem **điểm dừng hạn mức** trước; hiện chưa có tranh để duyệt. Không chạy lệnh Git, build, test, dev server, trình duyệt hoặc mạng ngoài công cụ tạo ảnh; không sửa mã và không chạm Tu Tiên.
