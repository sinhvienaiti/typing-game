# Phiếu 431: Bảng phân cảnh 2D cho 7 tuyệt kỹ khả thi (để owner duyệt trước khi dựng)


Phản biện: PASS (Sonnet, 17/11)
**Owner miễn luật hạn mức 16/11 (nguyên văn):** "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau".

## Bối cảnh
Owner 17/11 chê các tuyệt kỹ "đều trồi lên từ mặt đất rồi vòng tròn lại", hỏi đã có ảnh 2D mẫu để duyệt chưa. Thiết kế trình diễn và đánh giá khả thi: `docs/games/tu-tien/ULT_CHOREOGRAPHY.md`. Làm phân cảnh cho 7 hệ được đánh dấu **Làm**: Kim, Tinh Tú, Lôi, Quang, Phong, Thổ, Băng.

## Việc
Dùng công cụ `image_gen`: **2 mẫu trước** (Kim và Lôi), ghép `ult-storyboard-samples-431.jpg`, dừng và ghi báo cáo để Claude gửi owner; chỉ khi được giao tiếp mới làm 5 hệ còn lại. Tổng tối đa 14 lần. Mỗi hệ **một ảnh 1536×1024 gồm 4 khung** xếp 2×2 (tụ lực · phát chiêu · trúng đòn · dư âm), lưu `games/immortality-cultivation/art-src/concept/ult-storyboards/<hệ>-storyboard.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc mọi lần (ghi đường dẫn): `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png` (góc camera 55°, nền sân đá, mật độ quái — chỉ lấy góc nhìn và sân, **không** lấy bố cục vòng tròn), và ảnh tham chiếu cùng hệ có sẵn trong `games/immortality-cultivation/art-src/concept/ult-<hệ>/` để lấy màu và chất liệu, nếu có (Lôi chưa có thư mục: dùng `games/immortality-cultivation/art-src/lab/vfx/thunder/thunder-big-burst.atlas.png`). Kim dùng thêm thanh kiếm đã duyệt `.../ult-metal/tripo-src/ult-metal-sword.v1-try1.png`.
Mỗi khung: nhìn chéo xuống ~55°, một người tung chiêu nhỏ ở dưới giữa (bóng dáng chung, quay lưng), đàn quái nhỏ trên làn đường đá phía trước; diễn đúng dòng của hệ đó trong bảng `ULT_CHOREOGRAPHY.md` (nguồn, chuyển động, điểm nhấn). **Không vẽ vòng tròn mọc từ đất** trừ khi bảng ghi (Kim có trận pháp **trên trời**). Không chữ, không watermark. Phong cách game tu tiên thương mại cao cấp, chân thật, ánh sáng điện ảnh.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/431-report.md`.
