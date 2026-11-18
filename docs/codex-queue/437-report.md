# Phiếu 437 — Trận pháp Kim nhìn thẳng từ trên xuống

Đã tạo một ảnh nguồn bằng công cụ `image_gen` tích hợp, dùng 1/4 lần gọi tối đa. Không gặp giới hạn công cụ.

## Tệp giao nộp

- Ảnh: [formation-topdown.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-topdown.v1-try1.png).
- Prompt gửi nguyên văn, kèm ghi chú hậu xử lý tách riêng: [formation-topdown.v1-try1.prompt.txt](../../games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-topdown.v1-try1.prompt.txt).
- Tham chiếu duy nhất đã nạp vào công cụ: `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-sky.v1-try1.png`. Chỉ lấy hoa văn mây, phù văn và màu vàng; chuyển góc nghiêng sang nhìn thẳng từ trên xuống.

## Kiểm tra ảnh nguồn

Đã mở và xem ảnh sau khi lưu. Đồ án có nhiều vòng đồng tâm, dải phù văn trang trí, tám cụm quẻ và hoa văn mây vàng; tâm rỗng đen. Nhìn trực diện mặt trận pháp, không còn ellipse phối cảnh hoặc các tia rủ của ảnh tham chiếu; không thấy cảnh nền, bóng đổ, chữ đọc được hay watermark.

- PNG RGB, đúng **1024×1024**.
- Hộp bao mọi pixel khác đen: từ **(92, 93)** đến **(931, 930)**, tính cả hai đầu; rộng **840**, cao **838** pixel. Chênh lệch hai chiều khoảng **0,24%**; đây là phép đo hộp bao cả hoa văn, không phải chứng nhận hình học từng vòng tròn.
- Tâm hộp bao **(511,5; 511,5)**, đúng tâm ảnh.
- Lề trái/phải **92 px (8,98%)**; trên/dưới **93 px (9,08%)**. Dải viền 62 px ở cả bốn phía được kiểm tra: mọi pixel đúng **RGB(0,0,0)**, vượt yêu cầu lề tối thiểu 6%.
- Công cụ trả bản gốc 1254×1254; ImageMagick làm sạch nền với ngưỡng đen 1%, cắt phần trống, thu đồng tỉ lệ và đặt giữa khung 1024×1024. Không vẽ thêm hình; bản gốc còn nguyên tại đường dẫn ghi trong tệp prompt.

## Phần không làm và owner cần xem

Không tạo try2–try4 vì try1 đã đáp ứng yêu cầu ảnh nguồn qua kiểm tra trực quan và số đo trên. Không sửa hay ghi đè ảnh có sẵn; không sửa code, tạo video, chạy build/test, đổi nhánh hoặc thực hiện thao tác Git.

Owner xem try1 để duyệt mức huyền bí, hoa văn và độ tròn trước khi dùng trên mặt phẳng 3D. Các quẻ/phù văn là trang trí cách điệu, chưa kiểm định tính chính xác của một đồ án bát quái truyền thống. Đây là bàn giao thành phần nguồn; chưa tích hợp hoặc chấm chất lượng hiệu ứng tổng hợp trong play host.
