# Sổ chất lượng (mỗi dòng một sự kiện, chỉ thêm dòng)

Ghi khi có sự kiện đáng kể. Bản rà soát 23:00 mỗi ngày (`review/<ngày>.md`) đọc từ đây.

Loại sự kiện:
- `anh duyệt`, `anh chê`;
- `lỗi Claude` (đặc tả sai, báo sai, xếp sai);
- `Codex dừng đúng` (phiếu sai, Codex bắt được);
- `Codex làm lại`;
- `phản biện FAIL`;
- `kiểm trượt`, `lỗi sau gộp`;
- `mất thời gian` (hết giới hạn phiên, Codex ngồi không, chờ duyệt).

| Ngày giờ | Việc | Loại | Chi tiết |
|---|---|---|---|
| 04/11 00:00–07:00 | toàn bộ | mất thời gian | Agent chờ duyệt ghi file khoảng 7 giờ, vì đi qua đường symlink |
| 04/11 ~14:10 | A4 Firefly | lỗi Claude | Agent báo nhầm Firefly mất đăng nhập; anh: "firefly đâu có tự logout" |
| 04/11 17:05–18:20 | toàn bộ | mất thời gian | Claude hết giới hạn phiên |
| 04/11 18:24–18:44 | A4 Firefly | lỗi Claude | Bị chặn 20 phút mà không báo anh; anh: "tại sao fire bị tắc nhưng bạn không hề thông báo" |
| 04/11 ~18:40 | Codex | mất thời gian | Codex ngồi không vì lượt phản biện cuối của 258 bị xếp sau A4; anh hỏi lần 1 |
| 04/11 18:56 | 258 | anh duyệt | Codex 14 phút; 907/907 test; gộp sau khi kiểm GPU |
| 04/11 19:1x | 258b | Codex dừng đúng | Đặc tả của Claude đòi số HDR nằm trong [0,1] |
| 04/11 ~19:50 | Codex | mất thời gian | Codex ngồi không khoảng 25 phút; phiếu Song Long đã đủ 2 PASS mà chưa được giao; anh hỏi lần 2 |
| 04/11 20:20 | C3 | lỗi Claude | Đổi ảnh mà không chạy test, làm hỏng `orbit-cutin.test`; Codex 271 bắt được |
| 04/11 21:02 | 273 | Codex dừng đúng | Đặc tả mặt nạ B của Claude tự mâu thuẫn |
| 04/11 21:13 | 273 | kiểm trượt | Lửa tắt vụt ở tick 12; Claude bắt được trước khi gửi anh, sửa ở 273b |
| 04/11 21:50–23:20 | toàn bộ | mất thời gian | Claude hết giới hạn phiên lần 2 |
| 04/11 ~22:00 | 273b | anh duyệt | Nhịp cháy lửa phím 1 |
| 04/11 23:31 | 274 | Codex dừng đúng | Công thức nguội của Claude kéo than xuống màu muội |
| 04/11 23:37 | Codex | lỗi Claude | Báo giờ mở hạn mức Codex là 00:03 (thật là 00:52); anh bắt được |
| 04/11 23:50 | nhát chém phím 7 | anh chê | Lửa gai nhọn vẽ bằng mã: "nhìn thực sự rất xấu" |
| 04/11 23:55 | 269 | anh duyệt | Gộp âm theo bậc |
| 05/11 00:05 | 259 | kiểm trượt | Kiểm 8, 9, 10 trượt; ở hệ Kim đĩa ngọc phẳng, xám |
| 04/11 cả ngày | phiếu 258, 259, 269, 272 | phản biện FAIL | 3, 4, 3 và 5 vòng FAIL trước khi có PASS |
| 05/11 00:27 | Firefly sprint | mất thời gian | Firefly tính credit (âm 10 credit/lần, còn 7.540/10.000), không phải "không tốn credit" như bộ nhớ cũ ghi; phải chia credit giữa video và âm |
| 05/11 00:40 | Firefly sprint | mất thời gian | Hai bộ chạy ở hai tab; tab nằm nền chạy chậm hơn (trình duyệt hạ nhịp tab nền) |
