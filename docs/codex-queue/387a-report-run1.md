# Báo cáo phiếu 387a · 16/11/2026

**Trạng thái: dừng ở bước đối chiếu phiếu; chưa sửa mã.** Hai điều kiện kiểm nhận mâu thuẫn với hình học và tốc độ đã chốt. Cần sửa lời giải trước khi triển khai, theo quy tắc Codex dừng khi gặp mâu thuẫn trong skill `agent-orchestration`.

## Đã kiểm tra

- Đọc phiếu 387a, `MAP1_WIDE.md` §13.3–13.4, script `lane-width.mjs`, hướng dẫn game và các tệp sim/view liên quan.
- Quota trong rollout mới nhất: đã dùng 6%, còn 94%; không bị giới hạn quota.
- Mã hiện tại xác nhận Hỏa Nha có `tier: "small"`, `flying: true`, `speedMm: 2000`; thú bay đi thẳng tới tim. Flow field kéo dây bằng `clearLine`, đi thẳng tới tim khi các ô trên đoạn đó mở.

## Hai mâu thuẫn cần chốt

### 1. Hỏa Nha không thể đạt 10–16 giây

Phiếu giữ tốc độ 2.000 mm/s và đặt lối trời tại (±24.000; −44.000) mm. Khoảng cách tới tâm là 50.119,856 mm; mép Kết Giới có bán kính 9.000 mm. Thời gian tới mép là:

`(50.119,856 − 9.000) / 2.000 = 20,560 giây`.

Đây là một loài Nhỏ, nên kiểm nhận 3(e) yêu cầu nó nằm trong 10–16 giây, nhưng các số bắt buộc ở mục 1.4 và 1.6 làm điều đó bất khả thi. Không thể sửa test cho xanh mà vẫn giữ đủ yêu cầu.

**Đề nghị sửa phiếu:** giữ cổng và tốc độ đã chốt, ghi ngoại lệ Hỏa Nha khoảng 20,56 giây. Nếu bắt buộc 10–16 giây, người chốt lời giải phải đổi tốc độ hoặc điểm sinh; worker chưa tự chọn.

### 2. `routeMm` theo đường gấp khúc không khớp flow field ±3%

Tái tính Catmull-Rom từ đúng sáu điểm điều khiển của phiếu, bước 0,1, làm tròn 10 mm và bỏ điểm trùng liền kề: tổng độ dài đường tới z −9 m, cộng 7 m tới mép tim r 2 m, là **44.159,463 mm**.

Với đường rộng 12 m và clearance 400 mm, flow field cho phép tâm ô cách đường tới **5.600 mm**. Kiểm tra các tâm ô trên đường thẳng từ ô cổng tới tim theo quy tắc chọn ô hiện tại và phép chiếu nguyên `mulDivSym`:

| Cổng | Tâm ô cổng (mm) | Khoảng cách lớn nhất của tâm ô tới đường | Độ dài flow tới mép tim |
| --- | --- | --- | --- |
| A | (−2.250; −43.250) | 2.464,485 mm | khoảng 41.308,486 mm |
| B | (2.250; −43.250) | 4.735,773 mm | khoảng 41.308,486 mm |

Cả hai đường thẳng đều nằm trong phần mở của lane; đoạn phía nam cũng không chạm hai trụ tại x ±7.600 mm. Vì vậy `buildFlow` chọn waypoint `HEART` ngay từ ô cổng, thay vì bám tâm đường chữ S. Sai lệch giữa `routeMm` theo polyline và flow field là **6,90%** so với flow, vượt ±3% của kiểm nhận 3(d). Làm tròn số nguyên không giải quyết được sai lệch này.

**Đề nghị sửa phiếu:** lấy `routeMm` theo độ dài flow field thực tế; giữ polyline làm biên hành lang. Nếu cần thú bắt buộc uốn theo tâm đường, cần lời giải điều hướng khác, vì chỉ chặn ngoài hành lang rộng 12 m không tạo ra hành vi đó.

## Tệp đã đổi và phần bỏ qua

- Chỉ tạo `docs/codex-queue/387a-report.md`.
- Chưa sửa sim, dữ liệu, camera, trượt mép hoặc test; chưa cập nhật golden, nên không có giá trị cũ → mới.
- Chưa chạy typecheck/test/build, chưa nướng impostor, chưa chụp hoặc ghép ảnh; chưa có số đo khung build. Các bước này đợi lời giải hết mâu thuẫn.
- Không sửa Ngũ Lôi, ảnh/mặt đất của 387b, số quái/liveCap của 387c, hay công việc có sẵn của agent khác. Không ghi Git.
- Khi tới bước capture, thư mục review nằm ngoài các writable roots của phiên này; cần môi trường cho phép ghi đúng đường dẫn review đã chỉ định. Không tạo ảnh vào nơi khác để thay thế.

Chủ dự án cần xem hai điều chỉnh kiểm nhận trên trước khi chạy tiếp 387a.
