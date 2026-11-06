# Phiếu 312 · Vẽ lại 7 sao băng

Đã gọi đúng **7 lần `image_gen`**, mỗi hệ một lần, không gọi thêm hay tự sửa ảnh. Theo yêu cầu cụ thể trong thân phiếu là 7 lần (tiêu đề ghi 8). Đủ 7 bộ `.png` và `.prompt.txt`, chỉ thêm file mới bằng `cp -n` vào:

`games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`

Mỗi prompt giữ nguyên văn, chỉ thay `<MATTER>`; kèm đúng ảnh lưỡi liềm của hệ và `fire-comet.v1-try1.png`, nền đen, `transparent_background=false`. File prompt ghi công cụ, hai đường dẫn tham chiếu, prompt đã gửi và khổ thật. Đã kiểm tra bản chép khớp SHA-256 với ảnh gốc và prompt lưu khớp prompt gửi.

| Tệp mới (kèm `.prompt.txt` cùng tên gốc) | Khổ thật | Quan sát ảnh |
| --- | --- | --- |
| `metal-comet.v1-try2.png` | 1672 × 941 px | Đầu tròn rõ, mảnh thép bạc và ánh vàng; đuôi thon dần, không thấy dáng lưỡi liềm hay chữ. |
| `earth-comet.v1-try2.png` | 1670 × 941 px | Đầu đá rõ với khe sáng hổ phách; đuôi thon dần, không thấy dáng lưỡi liềm hay chữ. |
| `dark-comet.v1-try2.png` | 1671 × 941 px | Đầu khói đen lớn, viền đỏ và lõi trắng sáng rõ; đuôi thon dần, không thấy dáng lưỡi liềm hay chữ, không thấy tím. |
| `wind-comet.v1-try2.png` | 1671 × 941 px | Đầu xoáy khí bạc hà sáng rõ; đuôi thon dần, không thấy dáng lưỡi liềm, chữ hay lá. |
| `poison-comet.v1-try2.png` | 1671 × 941 px | Đầu dịch xanh có bọt rõ, tím phụ; đuôi thon dần và nhỏ giọt, không thấy dáng lưỡi liềm hay chữ. |
| `blood-comet.v1-try2.png` | 1671 × 941 px | Đầu dịch đỏ có cục sẫm rõ; đuôi thon dần, có giọt và vài mảnh tinh thể, không thấy dáng lưỡi liềm hay chữ. |
| `void-comet.v1-try2.png` | 1672 × 941 px | Đầu xoáy có tâm tối rõ, các khe sáng chàm-tím; đuôi thon dần, không thấy dáng lưỡi liềm hay chữ. |

Anh cần xem: cả bộ nghiêng gần dáng mẫu Lửa, chưa sát góc 20° so với phương đứng; dải sáng Thổ còn gợi lửa; viền Ám đỏ khá sáng; Huyết còn mảnh tinh thể; Hư Không có viền trắng-vàng khá dày. Giữ nguyên các đầu ra theo phiếu, chờ chấm mù lại, chưa kết luận đạt trên 8.

Không bỏ sót ảnh nào. Không vẽ lại Mộc vì đã làm qua Gemini; không chạy build/test, không sửa file cũ hay mã game, không dùng ảnh ngoài.
