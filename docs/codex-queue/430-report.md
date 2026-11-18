# Phiếu 430 — Ảnh nguồn một kiếm Kim dày

Ngày thực hiện: 16/11/2026. Đã dùng **2/4 lần gọi `image_gen`**, một luồng, từ ảnh tham chiếu bắt buộc. Phiếu đã có phản biện PASS và miễn luật hạn mức của owner ngày 16/11.

## Tệp giao

Thư mục: `games/immortality-cultivation/art-src/concept/ult-metal/tripo-src/`.

- `ult-metal-sword.v1-try1.png` và `ult-metal-sword.v1-try1.prompt.txt`.
- `ult-metal-sword.v1-try2.png` và `ult-metal-sword.v1-try2.prompt.txt`.
- `ult-metal-sword-sheet-430.jpg` và `ult-metal-sword-sheet-430.prompt.txt`.

Ảnh ghép có hai hàng; mỗi hàng gồm ảnh tham chiếu, ảnh gốc công cụ và bản giao đã chuẩn hóa. Prompt cạnh mỗi PNG chứa nguyên văn prompt đã gửi, đường dẫn ảnh tham chiếu và nhật ký hậu kỳ tách riêng.

## Kiểm tra

Cả hai PNG giao đều **1024×1024**. Mỗi ảnh có một kiếm cắm mũi xuống khối đá nhỏ; lưỡi bạc bản rộng, sống và mặt vát nổi rõ, hoa văn mây, chắn kiếm và chuôi vàng chạm trổ. Không thấy kiếm phụ, vệt sáng, hạt, quầng, bloom, dây mảnh, chữ hay watermark. Nền xám, ánh sáng studio mềm.

| Bản giao | Lề trái | Lề trên | Lề phải | Lề dưới | Bề ngang / chiều dài lưỡi lộ ra, ước lượng thị giác |
| --- | ---: | ---: | ---: | ---: | --- |
| Mẫu 1 | 42,0% | 12,6% | 42,2% | 19,5% | Khoảng 1:5,5–1:6, lớn hơn 1:8 |
| Mẫu 2 | 42,5% | 15,7% | 42,7% | 19,1% | Khoảng 1:6–1:6,5, lớn hơn 1:8 |

Lề đo bằng ImageMagick trên mặt nạ phân biệt màu/độ sáng với nền xám, rồi đối chiếu ảnh ghép. Hộp bao lần lượt `(430,129)–(592,824)` và `(435,161)–(587,828)`; đây là phép đo ảnh 2D, không phải số đo mô hình 3D. Độ dày được thể hiện bằng sống và mặt vát; chưa có mô hình để đo độ dày thực.

Công cụ trả ảnh 1254×1254 dù prompt yêu cầu 1024×1024. Mẫu 1 được nới nền bằng pixel biên tới 1536×1536; mẫu 2 tới 1440×1440; sau đó thu đồng đều về 1024×1024 bằng Lanczos. Cách này bảo đảm lề ≥12% mà không cắt hoặc sửa vật thể. Ảnh gốc được giữ nguyên tại thư mục mặc định của công cụ; ảnh ghép chứng minh trước/sau.

## Owner cần xem

Mẫu 1 có bản lưỡi và chắn kiếm lớn hơn; mẫu 2 gọn hơn. Góc nhìn vẫn thiên về mặt rộng của kiếm; owner cần xem trực tiếp mặt vát và cảm giác dày trước khi chọn nguồn Tripo. Đây là hai ứng viên nguồn, chưa có hai đánh giá mù và chưa được công nhận đạt ngưỡng 8,5.

Dừng ở hai mẫu để owner so sánh trước khi tạo thêm. Không gọi Tripo, không tạo video, không tích hợp game vì ngoài phạm vi phiếu. Không sửa code, không chạy build/test, không xóa hoặc ghi đè ảnh có sẵn, không đổi nhánh và không thực hiện commit/push/reset/clean/stash. Ảnh ghép được đặt cạnh ảnh đúng yêu cầu riêng của phiếu 430; không ghi sang thư mục review ngoài phạm vi cho phép.
