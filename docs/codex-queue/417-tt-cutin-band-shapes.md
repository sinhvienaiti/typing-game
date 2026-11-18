# Phiếu 417: 10 kiểu dáng dải cut-in, bản trung tính để tô màu bằng code


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Owner 16/11/2026 xem 14 dải phiếu 416 (`games/immortality-cultivation/art-src/concept/cutin-bands/cutin-bands-sheet-416.jpg`), cùng một bố cục hai dải lụa: "nên vẽ thêm khoảng 10 kiểu dáng, mỗi kiểu dáng lại nhiều màu sắc như kia để có thể thay đổi tuỳ ý và tạo nhiều hiệu ứng chồng sau này". Theo luật thành phần (owner 12/11): một kiểu dáng vẽ một lần ở dạng **trung tính** (trắng-xám sáng trên nền đen), code tô màu theo hệ và chồng lớp; như vậy mỗi kiểu có đủ 14 màu mà không phải vẽ 140 ảnh.

## Việc
`image_gen`, tối đa 16 lần, 1920×640, lưu `games/immortality-cultivation/art-src/concept/cutin-bands/shapes/cutin-shape-<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc mọi lần (ghi đường dẫn trong prompt): ảnh 416 của hệ gần nhất về chất liệu (vd. `cutin-metal.v1-try1.png`) để giữ độ chi tiết và ánh sáng.
1. **10 kiểu dáng khác hẳn nhau**, mỗi kiểu một ảnh trung tính: năng lượng trắng-bạc phát sáng, độ sáng có lớp (lõi sáng, viền mềm, hạt/lấp lánh), trên nền đen tuyệt đối, hai đầu mờ về đen, chừa vùng giữa-trái để đặt nhân vật và tên chiêu. Gợi ý 10 kiểu (được đổi nếu có ý tốt hơn): (a) xoáy cuộn một chiều, (b) tia chém chéo song song, (c) sóng dâng lớp lớp, (d) vụ nổ lan từ phải sang, (e) mảnh vỡ/tinh thể bay ngang, (f) vệt khói mực thư pháp, (g) vòng ấn/trận pháp nghiêng phẳng, (h) tia sét phân nhánh, (i) cánh/lông vũ năng lượng xòe, (j) dải sao/bụi tinh tú chảy.
2. **4 ảnh thử màu**: chọn 2 kiểu, mỗi kiểu tô 2 màu (vd. đỏ lửa, xanh băng) bằng chính `image_gen` để kiểm rằng bản trung tính tô màu vẫn đẹp; ghi trong báo cáo cách code nên tô (nhân màu, gradient map hai màu lõi/viền).
Phong cách: game tu tiên thương mại, sang trọng, điện ảnh, chân thật; không người, không sinh vật, không chữ, không watermark, không viền nét, không tô phẳng.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `cutin-shapes-sheet-417.jpg` (10 kiểu trung tính + 4 thử màu, có nhãn) trong `shapes/` và `docs/codex-queue/417-report.md`.
