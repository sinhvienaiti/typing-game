# Phiếu 324 · Đủ bộ ấn Kim

Đã gọi `image_gen` **8 lần: 5 ảnh đầu + 3 lần vẽ lại** (arcs, arrow, groove). Mọi lần đều gửi hai mốc đã duyệt: `metal-sigil-hex.v1-try2.png` và `metal-sigil-line.v1-try1.png`; đã mở cả hai trước lượt đầu. Không dùng ảnh ngoài repo.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

Đã thêm vào `S` tám PNG trong bảng dưới, mỗi ảnh kèm `<tên không đuôi>.prompt.txt` ghi công cụ, hai đường dẫn tham chiếu, prompt nguyên văn và khổ thật. PNG đều **1672 × 941 px**, xấp xỉ 16:9, được chép bằng `cp -n`; đã đối chiếu SHA-256 với bản công cụ trả về, không hậu kỳ.

Điểm 0–10, lấy **mặt yếu nhất** làm điểm chung. Đây là tự chấm ảnh nguồn theo phiếu, chưa phải chấm mù hay nghiệm thu runtime.

| Ảnh | Bản chọn | Đúng dáng | Đẹp, sang | Nhìn thẳng / nền / không chữ | Mặt nạ / lề / không cắt | Cùng phong cách | Chung | Nhận xét |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| metal-sigil-arcs.v1-try1.png | Không | 7 | 8,5 | 8 | 8 | 9 | 7 | Nét bạc đúng mốc nhưng chỉ có ba vòng gần kín. |
| metal-sigil-arcs.v1-try2.png | Có | 8 | 8,5 | 8 | 8 | 9 | 8 | Bốn cung tách đoạn, bốn mũi kiếm tiếp tuyến và tâm trống; bán kính các cung ngoài còn gần nhau. |
| metal-sigil-arrow.v1-try1.png | Không | 7,5 | 8,5 | 8 | 8 | 9 | 7,5 | Còn giống dải ấn mốc, ba vệt lướt chưa rõ. |
| metal-sigil-arrow.v1-try2.png | Có | 8,5 | 8,5 | 8 | 8 | 9 | 8 | Ba vệt song song rõ, có nhịp bước và một đầu kiếm chỉ phải. |
| metal-sigil-spiral.v1-try1.png | Có, cần xem lại lề | 8 | 8,5 | 8 | 7,5 | 9 | 7,5 | Đủ ba nhánh xoắn và tâm sáng nhỏ; vòng ngoài hơi dày, quầng sáng trên sát mép. |
| metal-crack-star.v1-try1.png | Có | 8 | 8,5 | 8 | 8,5 | 9 | 8 | Tâm thủng nhỏ, tám nhánh và nứt phụ; hoa văn còn đậm tính trang trí. |
| metal-rift-groove.v1-try1.png | Không | 7 | 8,5 | 8 | 8 | 9 | 7 | Dải còn giống khung vũ khí hơn khe nứt. |
| metal-rift-groove.v1-try2.png | Có, cần xem lại tỷ lệ | 7,5 | 8 | 8 | 8 | 8,5 | 7,5 | Khe giữa và nhánh nứt rõ hơn; vẫn có phù văn và toàn dải còn dày hơn khoảng 1/8 khung. |

Tấm ghép: `S/metal-sigils-set-sheet.jpg`, **2656 × 826 px**, nền đen, lưới 4 cột × 2 hàng. Đã mở bằng `view_image` kiểm đúng ô: hàng trên **Hex · Line · Guard Arcs · Dash Arrow**; hàng dưới **Galaxy Spiral · Star Crack · Sword Rift**, ô cuối trống.

Kiểm cơ học ở ngưỡng sáng 5%: hộp nét của arcs try2 `816×863+419+29`; arrow try2 `1595×168+43+382`; spiral `839×879+416+6`; crack `1169×817+249+52`; groove try2 `1598×176+37+376`. Không bị cắt ở ngưỡng này; spiral chỉ còn lề trên **6 px**, groove gồm quầng/nhánh cao khoảng **19%** khung. Nền nhìn đen nhưng góc dưới phải của cả tám ảnh là `RGB(0,1,0)`, chưa đen tuyệt đối.

**Anh cần xem:** sự đồng bộ cả bộ trên tấm ghép; lề spiral; độ dày groove; hoa văn trên crack. Spiral và groove còn dưới 8 sau kiểm cơ học cuối; giữ nguyên, không gọi thêm vì đã đủ trần ba lượt vẽ lại. Không coi hai bản này là đạt.

Không tích hợp game, làm sạch nền hoặc sửa/xóa tệp cũ vì ngoài phạm vi. Không chạy build/test, mở cổng hay dùng lệnh Git ghi. Không gặp giới hạn dịch vụ tạo ảnh.
