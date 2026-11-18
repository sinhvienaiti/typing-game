# Phiếu 320 · Hai mẫu VFX Thú Vương

Ngày 06/11/2026. Đã gọi `image_gen` **4 lần**: 2 mẫu đầu và 1 lần vẽ lại cho mỗi mẫu dưới 8. Đã mở toàn bộ ảnh tham chiếu và cả 4 kết quả bằng `view_image`. Chỉ dùng các ảnh của repo được phiếu chỉ định.

Đặt `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

| Ảnh trong S | Đọc đúng đòn/ai | Cuốn hút, uy lực | Màu, nền, không chữ | Khung video | Điểm yếu nhất | Nhận xét; vẽ lại |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `foe-boss-rend-claw.v1-try1.png` | 7 | 8,5 | 8 | 8 | **7** | Có năm vệt chính thay vì bốn; đã vẽ lại. |
| `foe-boss-rend-claw.v1-try2.png` | 8,5 | 8,5 | 8 | 8 | **8** | Đúng bốn vệt, bàn vuốt giáp mờ, quạt mở về trước; lề trên còn vừa phải; chọn bản này. |
| `foe-boss-entrance-wolf-head.v1-try1.png` | 9 | 8,5 | 8 | 7,5 | **7,5** | Dáng sói và giáp rõ, nhưng lề trên/dưới hẹp; đã vẽ lại. |
| `foe-boss-entrance-wolf-head.v1-try2.png` | 9 | 8,5 | 8 | 9 | **8** | Thu nhỏ toàn bộ đầu và xoáy, lề rộng, chân khói tan; mặt và giáp vẫn khá đặc; chọn bản này. |

Đây là **tự chấm ảnh mẫu**, chưa phải nghiệm thu trong game hoặc chấm mù độc lập.

Tệp mới: bốn PNG trong bảng, mỗi ảnh có `.prompt.txt` cùng tên chứa công cụ, hai đường dẫn tham chiếu, prompt nguyên văn và khổ thật. Tấm ghép `S/foe-boss-samples-sheet.jpg` đặt hai bản **try2** cạnh nhau (Vồ Xé trái, đầu sói phải), nền/viền đen, khổ 3392×989; có tệp `.prompt.txt` ghi lệnh ghép ImageMagick.

**Lưu ý kỹ thuật:** cả bốn PNG gốc là **1672×941**, gần 16:9 nhưng chưa đúng tuyệt đối (sai lệch tỷ lệ khoảng 0,053%). Nền nhìn đen; kiểm tra bốn góc thấy vài kênh ở mức 1/255, nên chưa phải đen RGB 0 tuyệt đối. Giữ nguyên ảnh công cụ xuất, không cắt hay chỉnh màu; cần chuẩn hóa khổ và mức đen trước bước video nếu yêu cầu đầu vào nghiêm ngặt. Không thấy chữ, máu hoặc mảng cam/vàng/tím trong hình.

**Anh xem:** tấm ghép, độ mở hình nón và độ mờ bàn vuốt ở mẫu trái; độ trong suốt của đầu/giáp và sắc thái đe dọa ở mẫu phải. Hai bản try1 được giữ để đối chiếu, không ghi đè.

**Không làm:** cả bộ còn lại, video Firefly và tích hợp runtime vì phiếu chỉ yêu cầu hai mẫu chờ anh duyệt. Không chạy build/test, mở cổng, dùng ảnh bên thứ ba, sửa/xóa tệp có sẵn hoặc chạy lệnh Git ghi. Không gặp giới hạn công cụ.
