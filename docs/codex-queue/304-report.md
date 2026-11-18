# Phiếu 304 · Các lớp bộ đếm mực vàng D60

Đã gọi **đúng 4 lần `image_gen`**, cả 4 bật `transparent_background: true`, dùng nguyên văn prompt A/A/B/C cùng hai ảnh tham chiếu `streak-ink-edict.v1-try1.png` và `streak-ink-edict.v1-try2.png`. Đã mở lại hai tham chiếu trước mỗi lần gọi. Lần đầu có alpha thật nên tiếp tục đủ bốn lần; không gặp hạn mức.

Đã thêm 4 PNG bằng `cp -n`, kèm 4 `.prompt.txt` cùng tên trong `games/immortality-cultivation/art-src/lab/ui/streak-counter/`. Không sửa hoặc xóa file có sẵn; ảnh chép nguyên bản, không hậu xử lý.

Đo bằng ImageMagick 7; alpha dưới đây trong khoảng 0–1, thứ tự góc: trên trái, trên phải, dưới trái, dưới phải. Cả bốn ảnh có kênh `srgba`, `opaque=False`.

| Tên ảnh (.png và .prompt.txt) | Khổ thật (px) | Alpha min–max | Alpha bốn góc |
| --- | --- | --- | --- |
| `streak-plates-row.v1-try1` | 2172 × 724 | 0–1 | 0, 0, 0, 0 |
| `streak-plates-row.v1-try2` | 2172 × 724 | 0–1 | 0, 0, 0, 0 |
| `streak-flakes-sheet.v1-try1` | 1536 × 1024 | 0.00392157–0.988235 | 0.00784314, 0.00784314, 0.0392157, 0.0117647 |
| `streak-ribbons-t4.v1-try1` | 1536 × 1024 | 0–0.992157 | 0, 0, 0, 0.00392157 |

Quan sát từng ảnh:
- `streak-plates-row.v1-try1`: không thấy chữ/số; năm hình mực phân biệt được, nhưng quầng sáng cấp cao sát/chạm nhau, cấp cuối sát mép phải, chưa bảo đảm tách sạch theo năm ô bằng nhau.
- `streak-plates-row.v1-try2`: không thấy chữ/số; năm hình mực phân biệt được, nhưng quầng sáng cấp 3–5 nối nhau rõ hơn, cấp cuối sát mép phải, chưa đạt yêu cầu mọi phần rời nhau.
- `streak-flakes-sheet.v1-try1`: không thấy chữ/số; đếm bằng mắt đủ 12 mảnh, 8 sao, 8 cụm chấm/vệt và 6 làn khói, hình chính rời nhau nhưng nền mờ phủ toàn tấm, không có pixel alpha=0.
- `streak-ribbons-t4.v1-try1`: không thấy chữ/số hoặc vệt mực; hai dải hình chính tách nhau quanh tâm trống, nhưng quầng nền mờ rộng và góc dưới phải còn alpha 1/255.

**Chưa đạt toàn bộ điều kiện ảnh tách lớp sạch:** ảnh mảnh vàng và dải sáng có kênh alpha nhưng nền chưa trong suốt sạch; hai hàng cấp cần chủ xem phần quầng sáng nối/sát nhau và mép phải. Đã gửi hiển thị hai mẫu hàng cấp trước khi tạo hai ảnh còn lại. Giữ đủ kết quả để chủ xem, không tự sửa hoặc gọi thêm theo giới hạn bốn lần. Chưa tích hợp, chưa chấm nghiệm thu trong game; không chạy build/test, không mở cổng mạng hoặc dùng lệnh Git ghi.
