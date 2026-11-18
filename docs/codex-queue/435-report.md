# Phiếu 435 — Hai ảnh thành phần Kim mưa kiếm

Ngày: 17/11/2026. Trạng thái: **đã tạo hai mẫu a/b, dừng để Claude gửi owner xem; chưa làm c**.

## Đã làm

Thư mục: `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/`.

| Tệp | Nội dung |
|---|---|
| `sword-fall-streak.v1-try1.png` | Một kiếm bạc chạm mây, chuôi vàng, mũi xuống; vệt vàng nhiều sợi mềm phía trên và ánh sáng ôm cạnh kiếm. |
| `formation-sky.v1-try1.png` | Một trận pháp vàng nằm ngang theo phối cảnh bầu dục, nhiều vòng và họa tiết cổ, tia sáng rủ xuống. |
| Hai tệp cùng tên `.prompt.txt` | Nguyên văn prompt đã gửi công cụ; phần hậu xử lý được tách riêng cuối tệp, có đường dẫn bản sinh gốc. |
| `metal-rain-comp-samples-435.jpg` | Bảng 1328×1386: hàng trên a, hàng dưới b; cột trái bản sinh, cột phải PNG giao nộp sau chuẩn hóa. Chỉ có hai mẫu, không phải bốn phương án. |
| `metal-rain-comp-samples-435.prompt.txt` | Nguồn bảng, cách đọc và lệnh ghép thực tế; không có lượt sinh AI cho bảng. |

Công cụ: **image_gen tích hợp, 2 lần gọi / tối đa 6**, mỗi lần sinh đúng một thành phần. Không gọi công cụ ảnh khác hoặc dùng ảnh bên thứ ba.

## Tham chiếu thực sự đã đưa vào cả hai lần

- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg` — chỉ nửa trái: Kim; khung 2 cho kiếm rơi và khung 1 cho trận pháp, sắc vàng và chất kim loại.
- `games/immortality-cultivation/art-src/concept/ult-metal/tripo-src/ult-metal-sword.v1-try1.png` — hình kiếm đã duyệt: bạc chạm mây, chuôi và chắn tay vàng.

Đã xem cả hai trước khi sinh; truyền cả hai đường dẫn qua `referenced_image_paths` trong từng lần gọi. Phiếu đã chỉ định hướng hình và có phản biện PASS Sonnet; lượt này thực hiện hai mẫu đã giao, không mở thêm hướng thiết kế hay giao việc cho agent khác.

## Kiểm tra và chuẩn hóa

Công cụ trả hai bản gốc **1254×1254**, dù prompt yêu cầu 1024×1024; nền gốc có nhiễu mức rất thấp (ví dụ góc mẫu a là RGB 1,0,0). Dùng ImageMagick 7: đưa mức kênh ≤1% về đen, bỏ phần viền đen dư, thu đồng tỷ lệ vào 768×768 rồi đặt giữa nền RGB 0,0,0 ở 1024×1024. Không vẽ thêm, không bẻ phối cảnh, không cắt vào hình. Bản sinh gốc còn nguyên ở thư mục mặc định của công cụ; bảng có đối chiếu trước/sau.

| Mẫu | PNG giao nộp | Hộp mọi pixel khác đen, x/y từ 0 | Lề trái / trên / phải / dưới |
|---|---|---|---|
| a | 1024×1024, RGB | x=416..607, y=128..895 | 40,62% / 12,50% / 40,62% / 12,50% |
| b | 1024×1024, RGB | x=128..895, y=255..768 | 12,50% / 24,90% / 12,50% / 24,90% |

Đếm trực tiếp dữ liệu RGB 8-bit: mọi pixel ngoài các hộp trên là đen tuyệt đối; cả hai đạt lề ≥12%. Đã xem bảng ghép: mỗi ảnh một thành phần, không người/quái, không cảnh nền, không chữ đọc được hoặc watermark nhìn thấy. Không nghiệm thu 8,5 hay chuyển động chỉ từ ảnh nguồn.

## Owner cần xem

- **a:** chất liệu và họa tiết bám kiếm đã duyệt, vệt mềm; góc kiếm vẫn gần chính diện hơn yêu cầu hơi chéo từ trên xuống. Đoạn vệt trên chuôi còn ngắn so với chiều dài thân kiếm; owner xem có cần kéo dài và nhấn hướng rơi ở lượt sửa.
- **b:** phối cảnh bầu dục rõ, vòng và tia đều nằm trọn khung; họa tiết mây và hình học nổi hơn phù văn. Owner xem mật độ vòng, nét cổ và độ mềm của các tia rủ có đúng hướng mong muốn.
- Đây là **mẫu chờ chọn**, chưa phải ảnh đã duyệt để dùng làm video hoặc tích hợp.

## Đã dừng đúng phạm vi

Chưa tạo `ground-cracks-gold` (c), chưa tạo thêm biến thể: phiếu yêu cầu dừng sau a/b và chỉ làm tiếp khi được giao. Không tạo video, sửa code, chạy build/bộ kiểm thử, sửa tài liệu thiết kế game, ghi đè/xóa ảnh có sẵn hoặc thực hiện thao tác Git.

Claude gửi bảng mẫu cho owner trước khi giao bước tiếp. Không gặp giới hạn công cụ trong lượt này.
