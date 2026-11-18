# Phiếu 324b · Vẽ lại xoắn ốc và rãnh Kim

Đã gọi `image_gen` **đúng 2 lần**, không cần lượt vẽ lại: cả hai bản tự chấm đạt 8. Mỗi lần đều gửi hai mốc `metal-sigil-hex.v1-try2.png`, `metal-sigil-line.v1-try1.png` và bản cũ của đúng hình cần sửa. Không dùng ảnh ngoài repo.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

Đã thêm mới bằng `cp -n`:
- `S/metal-sigil-spiral.v1-try2.png` và `.prompt.txt` cùng tên.
- `S/metal-rift-groove.v1-try3.png` và `.prompt.txt` cùng tên.
- `S/metal-sigils-set-sheet-v2.jpg`.

Hai PNG đều **1672 × 941 px**, giữ nguyên ảnh công cụ trả về; SHA-256 khớp bản nguồn. Các tệp prompt ghi công cụ, đầy đủ đường dẫn tham chiếu và prompt nguyên văn.

Điểm 0–10, lấy **mặt yếu nhất** làm điểm chung; đây là tự chấm ảnh nguồn theo phiếu, chưa phải nghiệm thu runtime hay chấm mù.

| Ảnh được chọn | Đúng dáng | Đẹp, sang | Nhìn thẳng / nền / không chữ | Mặt nạ / lề / không cắt | Cùng phong cách | Chung | Nhận xét |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| spiral try2 | 8,5 | 8,5 | 8 | 8,5 | 9 | **8** | Giữ ba nhánh xoắn, tâm nhỏ và vòng ngoài; toàn trận khoảng 69% chiều cao, hai lề thoáng; tâm hơi cao hơn giữa khung. |
| groove try3 | 8,5 | 8,5 | 8 | 9 | 8,5 | **8** | Khe ánh thép mảnh, mép răng cưa và nhánh ngắn, hai đầu nhọn; không thấy phù văn, chữ hay trang trí. |

Đo bằng ImageMagick: chuyển ảnh sang thang xám, `-threshold 5%`, lấy hộp nét `%@`, cùng phương pháp tái hiện đúng số đo của phiếu 324.

| Ảnh | Hộp nét (rộng × cao + x + y) | Số đo yêu cầu | Kiểm tra bổ sung |
| --- | --- | --- | --- |
| spiral try2 | `620×649+525+120` | **Lề trên 120 px = 12,75%** chiều cao, đạt ≥12% | Lề dưới 172 px = 18,28%; hộp cao 68,97% khung. |
| groove try3 | `1520×65+77+432` | **Cao 65 px = 6,91%** khung, đạt ≤10% | Lề trái 77 px = 4,61%; phải 75 px = 4,49%, đều ≥3%. |

So với bản cũ: lề trên spiral tăng từ 6 lên 120 px; chiều cao groove giảm từ 176 xuống 65 px. Nền nhìn đen nhưng chưa đen tuyệt đối: góc dưới phải cả hai vẫn `RGB(0,1,0)`, góc trên trái groove `RGB(1,1,1)`. Giữ nguyên ảnh, không hậu kỳ.

Tấm ghép **2656 × 858 px**, lưới 4 cột × 2 hàng, nền đen, tên tiếng Anh. Đã mở bằng `view_image` kiểm đúng ô: trên **Hex · Line · Guard Arcs · Dash Arrow**; dưới **Galaxy Spiral (try2) · Star Crack · Sword Rift (try3)**, ô cuối trống. Năm ảnh còn lại giữ đúng bản chọn của phiếu 324.

**Anh cần xem:** độ đồng bộ trên tấm ghép, bố cục xoắn ốc và độ mảnh của rãnh mới. Không dùng lượt dự phòng vì không ảnh nào dưới 8. Không tích hợp game, chạy build/test, mở cổng, dùng Git ghi hoặc sửa/xóa tệp có sẵn. Không gặp giới hạn dịch vụ.
