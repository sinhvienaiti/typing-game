# Phiếu 373 · Trận Tâm và Trận Trụ v2

Hoàn tất **4/4 ảnh nguồn** bằng **image_gen 5/12 lượt**; **view_image 7/14 lượt**. Chỉ dùng bốn tham chiếu nội bộ được phiếu chỉ định và ảnh mới của chính bộ này.

Trong `games/immortality-cultivation/art-src/props/`:
- `{tran-tam,tran-tru}.v2-{q,front}-final.png`: bốn góc nguồn 1024².
- Bốn bản `-raw.png` và bốn `-final.prompt.txt`: prompt nguyên văn, tham chiếu, hậu kỳ; prompt Trận Tâm chính diện ghi cả lượt bị loại.
- `formation-373-sheet.jpg`: cũ | mới, bản cao 90/66 px, raw | final.

Trận Tâm có vòng triện giả, bát quái, sen và ngọc ngà; Trận Trụ dùng cùng đá bạc tím xám, vân mây–lôi văn, chân hai tầng và ngọc trên đài sen.

**Kiểm script ImageMagick:** thu đồng dạng, khử tràn xanh, căn giữa; không kéo méo. Matte Trận Tâm q/front rộng **768/768**, cao **641/640 px**, lệch cao **0,16%**. Trận Trụ cao **768/768 px**, lệch **0%** sau chuẩn hóa; rộng khác nhau do góc nhìn. Lề nhỏ nhất **12,5%**. Mỗi matte một khối liền, không mảnh rời. Final nền `#00FF00`, alpha **255** toàn ảnh theo v7, không phải PNG trong suốt.

| Tiêu chí tự chấm nguồn | Tâm | Trụ |
| --- | ---: | ---: |
| Huyền bí tu tiên | 8,7 | 8,6 |
| Cùng bộ | 8,8 | 8,8 |
| Đẹp từ trên | 8,8 | 8,6 |
| Phù hợp Tripo | 8,7 | 8,7 |

Loại lượt chính diện Trận Tâm đầu vì góc quá dốc; không bỏ vật nào. Giữ nguyên ảnh cũ; không ghi Git, chạy build/test hay dựng Tripo. Bản thu nhỏ chưa chứng minh camera runtime hoặc góc 3D đúng 32°. Anh xem tấm ghép, nhất là đỉnh ngọc và hoa văn ở 66 px; cần chấm mù độc lập trước nghiệm thu.

