# Phiếu 323 · Hai mẫu ấn Kim

Đã gọi `image_gen` 3 lần: 2 mẫu ban đầu và 1 lần vẽ lại lục giác do lề/mặt nạ dưới 8. Cả ba lần đều gửi đúng hai ảnh Kim được phiếu chỉ định, chỉ lấy chất liệu, nét và ánh sáng. Không dùng ảnh ngoài repo.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

Tệp mới trong `S`:
- `metal-sigil-hex.v1-try1.png` và `metal-sigil-hex.v1-try1.prompt.txt`.
- `metal-sigil-hex.v1-try2.png` và `metal-sigil-hex.v1-try2.prompt.txt` — bản chọn.
- `metal-sigil-line.v1-try1.png` và `metal-sigil-line.v1-try1.prompt.txt` — bản chọn.
- `metal-sigils-samples-sheet.jpg` — trái: hex try2; phải: line try1.

Mỗi PNG là bản sao nguyên gốc bằng `cp -n`, khổ thật **1672 × 941 px**, xấp xỉ 16:9; công cụ không trả đúng 1536 × 864 px yêu cầu trong prompt. Tấm ghép **3344 × 941 px**, ghép ngang bằng ImageMagick, không cắt ảnh. Đã mở các PNG và tấm ghép để kiểm tra.

Điểm tự chấm 0–10; điểm chung lấy tiêu chí yếu nhất, không phải kết quả chấm mù hay nghiệm thu runtime.

| Ảnh | Bản chọn | Đúng dáng | Đẹp, sang, cuốn hút | Nhìn thẳng / nền / không chữ | Mặt nạ / lề / không cắt | Điểm chung | Nhận xét |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| hex try1 | Không | 8,5 | 8,5 | 8 | 7,5 | 7,5 | Đủ sáu kiếm và tâm trống nhưng quầng sáng đỉnh trên chạm mép. |
| hex try2 | Có | 8,5 | 8,5 | 8 | 8,5 | 8 | Sáu kiếm rõ, viền bạc nhiều lớp; lề trên/dưới tốt hơn, tâm trống. |
| line try1 | Có | 8,5 | 8,5 | 8 | 8 | 8 | Dải ngang dài, hai biên song song và mũi phải rõ; trang trí đầu trái làm dải dày hơn phần thân. |

Lưu ý cần anh xem: nền nhìn đen nhưng **chưa đen tuyệt đối ở mọi pixel**; lấy mẫu góc có `(0,1,0)` trên thang 255. Giữ nguyên ảnh theo phạm vi phiếu, chưa làm sạch nền. Ở ngưỡng sáng 5%, hộp nét của hex try2 là `746×790+464+61`, của line try1 là `1641×185+15+371`: hình không bị cắt, nhưng lề hai đầu dải còn hẹp. Anh duyệt mức trang trí, tỷ lệ dải và sắc ánh sáng trên tấm ghép trước khi làm đủ bộ.

Chưa làm arcs, arrow, spiral, crack, rãnh mưa kiếm hoặc hệ khác: ngoài phiếu, chờ anh chọn mẫu. Chưa tích hợp game, chưa chấm mù trong play host; không chạy build/test, mở cổng, sửa/xóa tệp cũ hay chạy lệnh Git ghi. Không gặp giới hạn tạo ảnh.
