# Phiếu 337 · Tấm A9 · 11/11/2026

Đã tạo đủ ba tấm bằng `image_gen`, mỗi tấm 1254 × 1254, nền đen gần thuần, trắng–ngà nhạt. Dùng đúng hai ảnh tham chiếu của phiếu, chỉ lấy kiểu hạt và độ hoàn thiện. Tổng cộng **3/6 lần gọi**, không vẽ lại; mở **6/8 ảnh bằng `view_image`**. Các PNG được chép bằng `cp -n`; không sửa tệp có sẵn.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`.

Tệp mới trong `S`: `a9-spark-streaks.v1-try1.png`, `a9-ember-flakes.v1-try1.png`, `a9-dust-motes.v1-try1.png`; mỗi ảnh có tệp cùng gốc tên `.prompt.txt` ghi công cụ, đường dẫn tham chiếu, prompt nguyên văn và khổ thật. Tấm ghép **`a9-337-sheet.jpg`** (1584 × 856) đặt ba ảnh cạnh nhau, có tên và hàng thu nhỏ đúng 256 × 256.

## Tự chấm

Điểm cuối là **điểm thấp nhất**, không lấy trung bình. Đã xem ảnh gốc và bản thu toàn tấm xuống 256 px.

| Tấm | Lưới, tách ô | Không đốm tròn | Độ dài/cỡ | Đọc ở 256 px | Đẹp, chất lửa tiên hiệp | Điểm cuối | Ô đạt | Nhận xét | Vẽ lại |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Spark streaks | 9,3 | 9,4 | 8,7 | 8,5 | 8,5 | **8,5** | **16/16** | Ba độ dài rõ; hàng cuối cong/chẻ; đầu nhọn, đuôi mảnh nhiều lớp. | Không |
| Ember flakes | 9,3 | 9,4 | 9,0 | 8,3 | 8,5 | **8,3** | **16/16** | Bốn cỡ rõ, viền sáng và lòng tối; một số chi tiết tro rách mất khi thu nhỏ. | Không |
| Dust motes | 9,3 | 9,2 | 8,2 | 8,1 | 8,3 | **8,1** | **16/16** | Cụm rải không đều, hạt thoi/que/sao mảnh; các hạt nhỏ nhất mờ đi ở 256 px. Cỡ ở đây là độ phủ cụm, không phải ba độ dài của tia. | Không |

## Kiểm bằng ImageMagick 7

Đọc RGB 8 bit bằng `/opt/homebrew/bin/magick`, lấy cực đại của cả ba kênh. Mỗi ô phải có pixel > 12/255; toàn dải 4% sát bốn mép ô phải ≤ 12/255. Dải mép được làm tròn lên, nên kiểm bảo thủ hơn 4%.

| Tấm | Cực đại bốn góc, mỗi góc 10 × 10 px | Cực đại mép ô | Đỉnh nội dung | Kết quả |
| --- | --- | --- | --- | --- |
| Spark streaks | 1; 1; 1; 1 /255 | Cả 16 ô: 1/255 | Cả 16 ô: 255/255 | 16/16 |
| Ember flakes | 1; 1; 1; 1 /255 | Ô 13–14: 2/255; còn lại: 1/255 | Cả 16 ô: 255/255 | 16/16 |
| Dust motes | 1; 1; 1; 1 /255 | Cả 16 ô: 1/255 | Cả 16 ô: 255/255 | 16/16 |

**Cần lưu ý khi tích hợp:** 1254 không chia hết cho 4 theo pixel nguyên (ô chuẩn hóa rộng 313,5 px). Để đo 16 ô bằng nhau, nhân đôi bằng nearest-neighbor trong bộ nhớ thành 2508 × 2508, rồi chia thành ô 627 × 627; không nội suy thêm sáng và không sửa PNG gốc. Phiếu tích hợp cần xử lý kích thước chia hết cho 4 nếu bộ cắt đòi pixel nguyên.

**Anh xem:** tấm ghép, đặc biệt hàng bụi ở 256 px và lưu ý kích thước trên. Đây là tự chấm nguồn ảnh theo phiếu; chưa đánh giá hiệu ứng ghép trong game. Không làm tích hợp, sửa mã, âm thanh, chạy build/test, mở cổng mạng hay dùng lệnh Git ghi vì ngoài phạm vi. Không gặp giới hạn công cụ.
