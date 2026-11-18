# Phiếu 363 · Khung mẫu và icon HUD

Đã dùng **16/18 lượt image_gen**, tham chiếu của repo; hậu tố `.v1-try1`.

Đường dẫn dưới đây tính từ `games/immortality-cultivation/art-src/`:

- `ui/frames/ban-quyet-{ink-gold,jewel-crest}.v1-try1.png`: hai khung Bàn Quyết 1024×768; nền ngoài đã tách xanh, giữa chàm trơn, góc mây hồi văn. Gợi ý inset 9-slice: trái/phải 288 px, trên/dưới 256 px; chưa kiểm runtime.
- `lab/ui/skill-icons/ult-dark-{ink-gold,jewel-crest}.v1-try1.png`: hai tuyệt kỹ Ám, cùng khung tròn mẫu Huyết; hướng jewel thêm mặt cắt và nạm thạch anh.
- `ui/icons/hud-*.v1-try1.png`: đủ 12 tên trong phiếu.
- Cả 14 icon có bản 256/48/32 px. Mỗi PNG có `.prompt.txt` ghi prompt, tham chiếu và hậu xử lý.
- `ui/ui-363-sheet.jpg`: hai khung và toàn bộ icon ở ba cỡ; có tệp mô tả cách ghép.

Đã kiểm 44 PNG: đúng kích thước, alpha; lề ảnh chính ≥8%. Đã nhìn bản 32 px; không thấy chữ.

Tự chấm theo **mặt yếu nhất**, không lấy trung bình:

| Mẫu | Điểm |
|---|---:|
| Khung ink / jewel | 8,6 / 8,6 |
| Ám ink / jewel | 8,4 / 8,2 |
| Phù hồi khí / hộ thân / tốc hành | 8,3 / 8,5 / 8,3 |
| Kiếm Thung / Lôi Trụ / Võng | 8,1 / 8,5 / 8,6 |
| Linh thạch / ngọc / công đức | 8,7 / 8,8 / 8,6 |
| Settings / sound / muted | 8,3 / 8,5 / 8,5 |

Mặt yếu nhất: icon đọc ở 32 px; khung đồng bộ. Không mẫu dưới 8 nên không vẽ lại. Chưa làm tám khung: chờ anh chọn hướng. Chưa tích hợp, build/test hoặc nghiệm thu độc lập; chỉ tự chấm nguồn. Anh xem hai khung và Kiếm Thung trong tấm ghép.
