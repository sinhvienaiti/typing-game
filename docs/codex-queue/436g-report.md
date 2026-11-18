# Phiếu 436g — thân nền nữ chính v4

Đã gọi công cụ `image_gen` 4/4 lần, tạo bốn PNG gốc 1536×1024, giữ nguyên dữ liệu ảnh công cụ trả về, không chỉnh sửa ảnh bằng mã. Mỗi PNG có prompt nguyên văn cạnh ảnh. Cả bốn lần đều đính kèm chân dung A và bảng thân v3; lần 4 đính kèm thêm bản v4 try2 làm đích sửa bố cục.

## Tệp đã làm

Trong `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/heroine/fashion/`:
- `base-body.v4-turn.v1-try1.png` và `base-body.v4-turn.v1-try1.prompt.txt`.
- `base-body.v4-turn.v1-try2.png` và `base-body.v4-turn.v1-try2.prompt.txt`.
- `base-body.v4-turn.v1-try3.png` và `base-body.v4-turn.v1-try3.prompt.txt`.
- `base-body.v4-turn.v1-try4.png` và `base-body.v4-turn.v1-try4.prompt.txt`.

Tờ so sánh v3 | v4 try2: `/private/tmp/typing-game-436g/heroine-base-v4-436g.jpg`.
Số đo: `/private/tmp/typing-game-436g/measurements.json`.

## Tự đo

Góc tay lấy theo hồi quy đường giữa vùng da cánh tay trên ở y=260–340, tính so với phương dọc. Khe gối đo phần nền ở y=650. Biên hình lấy chênh kênh RGB > 4, loại đốm rời dưới 50 pixel; sai số biên khoảng 1–2 px. Chiều cao gồm búi tóc và giày. Thứ tự góc tay: trước trái/phải, sau trái/phải. Chiều cao và lề trên: trước/nghiêng/sau. Khe gối: trước/sau. Góc nghiêng đúng 90° khiến tay và chân chồng theo phép chiếu; không ép góc tay và khe gối 2D giống mặt trước.

| Lần | Góc tay (°) | Khe gối (px) | Cao hình (px) | Lề trên (px) | Lề ngoài trái/phải (px) | Khe giữa hình (px) |
|---|---|---|---|---|---|---|
| 1 | 36.7 / 36.5 / 37.2 / 37.6 | 35 / 35 | 925 / 920 / 925 | 39 / 44 / 39 | 107 / 109 | 72 / 76 |
| 2 | 40.5 / 39.6 / 41.5 / 42.1 | 30 / 30 | 897 / 894 / 898 | 53 / 55 / 52 | 86 / 81 | 60 / 66 |
| 3 | 32.4 / 31.6 / 33.5 / 33.9 | 27 / 25 | 921 / 916 / 922 | 40 / 45 / 40 | 86 / 89 | 121 / 108 |
| 4 | 40.2 / 39.5 / 41.6 / 41.9 | 28 / 29 | 898 / 895 / 898 | 52 / 54 / 52 | 21 / 31 | 130 / 115 |

## Kết luận

**Đề xuất try2 để chủ dự án xem và chuyển chấm mù; chưa công nhận đạt 8.5.** Tay nằm trong dải 35–45°, khe gối rõ 30 px ở cả trước và sau, chiều cao xấp xỉ 900 px, lề trên/dưới và lề ngoài đủ. Khe giữa hình đo được 60/66 px, sát ngưỡng, nên cần lưu ý sai số biên. Biên cao ba hình còn chênh khoảng 4 px; đường chân chênh khoảng 1 px. Vì vậy chưa khẳng định đạt yêu cầu bằng nhau tuyệt đối. Mặt nghiêng là ngang, mặt sau có gáy và búi tóc; độ khớp nhận dạng mặt trước/nghiêng và mức hoàn thiện cần hai giám khảo độc lập xác nhận.

- Try1: góc tay đo ổn định đạt 36,5–37,6° (ước lượng ban đầu bằng mắt thấp hơn), nhưng lề trên trước/sau chỉ 39 px, loại.
- Try3: tăng khe giữa hình lên 121/108 px nhưng góc tay giảm xuống 31,6–33,9°, loại.
- Try4: giữ được tay 39,5–41,9° nhưng công cụ dịch nhiều hơn yêu cầu; lề ngoài chỉ 21/31 px, loại.

Đã dừng đúng giới hạn bốn lần, không sinh lần thứ năm. Không làm trang phục thời trang, Tripo, rig, sửa mã, chạy build/test hay thao tác Git. Không tự tổ chức chấm mù ngoài phạm vi phiếu này.

## Chủ dự án cần xem

Xem tờ so sánh và PNG try2 ở độ phân giải gốc, đặc biệt mặt nghiêng, tỷ lệ trưởng thành, khoảng cách hai chân và độ hoàn thiện da/mặt. Chưa có xác nhận hai giám khảo ≥8.5 nên chưa đưa sang Tripo.

Tờ so sánh và số đo được lưu tạm trong `/private/tmp/typing-game-436g/`: sandbox phiên này không có quyền ghi thư mục `/Volumes/SS990TPRO/htdocs/typing-game-review/`. Cần người điều phối sao chép sang thư mục review của chủ dự án và cập nhật chỉ mục. Không sửa chỉ mục khi chưa có tệp trong thư mục review.
