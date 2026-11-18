# Phiếu 431b: Phân cảnh 2D cho 5 tuyệt kỹ còn lại (Tinh Tú, Quang, Phong, Thổ, Băng)


Phản biện: PASS (Sonnet, 17/11)
## Bối cảnh
Tiếp phiếu 431 (`431-tt-ult-storyboards-batch1.md`): 2 mẫu Kim và Lôi đã gửi owner 17/11 (`games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`), owner cho làm tiếp ("bạn đang chờ tôi duyệt gì?"). Thiết kế: `docs/games/tu-tien/ULT_CHOREOGRAPHY.md`.

## Việc
Dùng công cụ `image_gen`, tối đa 10 lần (2 mỗi hệ). Mỗi hệ một ảnh 1536×1024 gồm 4 khung 2×2 (tụ lực · phát chiêu · trúng đòn · dư âm), lưu `games/immortality-cultivation/art-src/concept/ult-storyboards/<hệ>-storyboard.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc mọi lần (ghi đường dẫn): `ult-storyboard-samples-431.jpg` ở trên (giữ đúng phong cách, góc camera 55°, người tung chiêu áo trắng quay lưng, đàn quái, sân đá đã được owner chấp nhận) và ảnh cùng hệ trong `games/immortality-cultivation/art-src/concept/ult-<star|light|wind|earth|ice>/` (màu, chất liệu).
Diễn đúng dòng của hệ trong bảng `ULT_CHOREOGRAPHY.md`: Tinh Tú — vẽ chòm sao trên trời rồi sao băng rơi **chéo** bắn tỉa; Quang — người tung chiêu nâng thấu kính, tia sáng quét hình quạt từ người ra; Phong — lưỡi gió trăng khuyết chém ngang qua đường kéo quái; Thổ — vết nứt chạy **thẳng** từ người tung tới quái, gai đá phun nối tiếp theo đường (không vòng); Băng — bão mảnh băng rơi phủ vùng, quái đóng băng rồi vỡ. Không vòng tròn mọc từ đất. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `ult-storyboards-431b.jpg` (5 hệ) và `docs/codex-queue/431b-report.md`.
