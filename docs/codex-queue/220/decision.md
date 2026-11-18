# Quyết định đo · Phiếu 220

## Bốn ứng viên cố định

Ghi cấu hình trong `variants.json` trước đợt A/B. Mỗi bản thêm đúng một núm trên chuỗi V6; mỗi bản đủ 100 seed ở hai bộ, không có lượt thử ngắn. F1 là `extra=1`, F2 là `spill=1`, F3 là `boost=0.15`, F4 là `boost=0.3`.

Chưa chốt ứng viên bốn ải ở mục này; quyết định có giờ UTC sẽ được bổ sung sau khi có đủ số f1–f4.

## Chốt trước khi chạy bốn ải

Giờ UTC: `2026-10-30T06:43:05.401789+00:00`.

Không mở F5/F6. Bốn ứng viên cố định đã tách được ba cơ chế; R1/R2 còn I Khá 12,6–17,8 %, R3 đã hạ xuống 1,1–1,3 %. Phần còn trượt là S/thắng quá cao của Chậm chắc và S Chuẩn tắt nhịp, không còn là thiếu từ hữu ích cho Khá/Nhanh. F3→F4 không đơn điệu: S Chậm chắc 72,5→74 % ở bộ đầu nhưng 71→67 % ở bộ sau; không có bằng chứng đủ để chọn thêm mức boost hay ghép luật nhằm đóng đồng thời hai cổng. Dừng ở 4 biến thể, không có lượt thử ngắn.

| Hạng | Bản | Điều kiện trượt cộng hai bộ | I Khá lớn nhất | Ô B1 lệch cộng hai bộ |
|---|---|---|---|---|
| 1 | F4 | 4 | 1.3 % | 4 |
| 2 | F3 | 5 | 1.2 % | 4 |
| 3 | F1 | 6 | 12.7 % | 12 |
| 4 | F2 | 7 | 17.8 % | 12 |

**Chọn F4: `FULL_BAY.boost=0.3` trên nền V6**, ít điều kiện bắt buộc trượt nhất: 2 + 2 = 4 (B1, B7 ở mỗi bộ). F3 còn 5, F1 còn 6, F2 còn 7. Chưa bản nào đạt. F4: I Khá 1,2/1,3 %, Nhanh 0,7/0,7 %; B6 CB +11/+14, TT +34/+23 điểm; TT Nhanh − Mới +7/+2, G3c kém/tốt 67/96 và 68/91 %. B1 còn Chậm chắc ở cả hai bộ nên không miễn sát mép; B7 S 68/66,5 %, cả hai bộ đều lệch nên không miễn.

Chạy đúng 6 báo cáo: x-v0, x-v6, x-f4; mỗi cấu hình đủ hai bộ seed, mỗi báo cáo c1-s1,c1-s2,c1-s3,c1-s4. Giữ nguyên mọi mặc định. Đây là chọn bản để xem tiếp, không phải duyệt áp luật.

## Sau khi đủ bốn ải

Giờ UTC: `2026-10-30T07:15:08.302463+00:00`.

Giữ F4 là bản đứng đầu theo luật chọn ở c1-s1, nhưng **chưa khuyến nghị áp luật nào**. B6 CB ải 2: F4 +8/+8 so V0/V6 +10/+10; B6 TT bộ sau +9 so V0 +19, dù cao hơn V6 +1. Ải 4 bộ sau Nhanh − Mới −8 điểm, trượt luật không đảo. B6 gộp bốn ải của F4 vẫn đạt: CB +11/+11,5, TT +27,25/+21; không lẫn số gộp đạt với suy giảm cục bộ.

C1-s1 của cả sáu báo cáo bốn ải khớp mốc tương ứng: 0/216 ô, 0 trường summary lệch. 16/16 lệnh đo exit 0. Ngoại lệ tài nguyên: tải tăng >10 sau khi đợt C đã mở 4 báo cáo; sandbox từ chối SIGSTOP, ghi riêng trong load-rise.json. Giữ nguyên dữ liệu và số lệnh, không chạy lại hay đổi biến thể.
