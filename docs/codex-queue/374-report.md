# Phiếu 374 · Ba cơ quan v2

Đã tạo bằng `image_gen`: 6 final 2048 × 2048, 6 raw, 6 prompt kèm tham chiếu và nhật ký hậu xử lý.

Trong `games/immortality-cultivation/art-src/mechanisms/`:
- `{kiem-thung,loi-phu-tru,phong-an-vong}.v2-{q,front}-final.png`
- Cùng tên với hậu tố `-raw.png` và `-final.prompt.txt`.
- `mechanisms-374-sheet.jpg`: cũ | mới q | mới front | icon; bản thu tối đa 72 px; đối chiếu raw | final cho cả sáu ảnh.

Kiếm đã sửa mũi hướng lên, chuôi chàm nằm dưới. Trụ dùng bùa giấy quấn dày và ấn lôi văn vuông. Võng là khung ngang thấp, bản đồng đan chéo, bốn ngọc ngà. Đồng trầm, đá xám, vân mây và hồi văn thống nhất bộ.

| Kiểm bằng script/ImageMagick | Kết quả |
| --- | --- |
| Lề nhỏ nhất | 10,94%, đạt ≥ 8% |
| Chiều cao q/front: kiếm, trụ, võng | 1600/1600; 1600/1600; 534/534 px |
| Chênh chiều cao từng cặp | 0%, đạt ≤ 5% |
| Khối liền sau tách key | 1 khối/ảnh, cả 6 đạt |
| Nền và alpha final | #00FF00 đặc; alpha 255 toàn ảnh |

Tự chấm **cùng bộ / khớp icon / chất Á Đông / dựng Tripo**: kiếm **8,8/8,7/8,8/8,6**; trụ **8,8/8,5/8,8/8,6**; võng **8,7/8,6/8,7/8,5**. Điểm yếu nhất 8,5; đây là tự chấm ảnh nguồn, chưa phải duyệt độc lập trong game.

Đã dùng 9/16 lần image_gen, 10/18 lần view_image. Giữ ảnh cũ; không ghi Git, chạy build/test hay sửa mã. Không dựng Tripo/kiểm host vì ngoài phạm vi. Bản thu 72 px là mô phỏng; anh xem độ đọc lưới và dải bùa. Võng căn cùng chiều cao hai góc nên q có nền rộng hơn; raw giữ kích thước gốc.
