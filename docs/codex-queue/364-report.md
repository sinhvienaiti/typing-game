# Phiếu 364 · D01–D05 · 12/11/2026

Đã tạo bằng **image_gen: 7/12 lượt**, xem ảnh **14/14 lượt**; chỉ dùng ảnh tham chiếu của phiếu. Tách kênh, mặt nạ và nối mép bằng ImageMagick; không vẽ hình bằng mã.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

| Việc | Tệp chọn trong S | Tự chấm theo mặt yếu nhất |
| --- | --- | --- |
| D01 | `fire-ground-mark-{rock,glow}.v1-try3.png` | 8,2 · đường viền còn hơi dài |
| D02 | `water-ground-mark-{rock,glow}.v1-try3.png` | 8,1 · nước mảnh, cần kiểm ở cỡ chơi |
| D03 | `ult-ice-crystal.v1-try1.png`, `ult-ice-crystal-mask.v1-try1.png` | 8,5 · chân cụm hơi dày |
| D04 | `ult-thunder-cloud-dark.v1-try2.png` | 8,2 · khối mây còn khá đều |
| D05 | `metal-rift-groove.v2-try2.png` | 8,0 · vùng nối hơi dày |

Mỗi PNG có `.prompt.txt` cùng tên gốc, chứa nguyên prompt, đường dẫn tham chiếu và lệnh xử lý tái lập.

**Kiểm bằng script:** cặp đá/sáng cùng khung 1536², cùng tọa độ nguồn; sai số độ chói khi cộng lại tối đa Hỏa 1,47/255, Thủy 1,39/255. Lề Hỏa/Thủy ≥168 px. Băng 1024²: lề nhỏ nhất 112 px (10,94%); mặt nạ chỉ 0/255, sai hình bóng **0 pixel**. Mây 1536×1024: lề trên 279 px, không cắt đỉnh; xám mực, viền ngà vàng nhạt. Kim đúng **2048×128**, lề dọc 14 px; cột đầu/cuối lệch **0/255**. Các lớp sáng và mây đạt đỉnh **229/255 = 0,898**; viền ngoài đen thuần.

Giữ 10 bản thử không chọn: D01/D02 try1 còn lẫn đá; try2 vượt đỉnh sáng; mây/Kim try1 lỗi chuẩn hóa hoặc nối mép. Không sửa ảnh có trước phiên, mã hoặc tài liệu game; không chạy build/test game.

Anh xem `S/vfx-364-sheet.jpg` trước/sau. Đây là tự kiểm nguồn; chưa nghiệm thu hiệu ứng ghép trong host ở mức 8,5.
