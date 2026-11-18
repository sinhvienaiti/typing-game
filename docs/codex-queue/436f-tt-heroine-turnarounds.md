# Phiếu 436f: Nữ chính, bảng 3 góc cho dựng 3D (thân nền v3 và 4 bộ)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Ngày 17/11 owner duyệt thân nền v3 và 4 ảnh thời trang của phiếu 436e: "tôi thấy đạt r". Việc tiếp theo là làm nguồn cho Tripo và rig. Mỗi bộ cần một bảng 3 góc (trước, nghiêng, sau) ở dáng chữ A, và khuôn mặt phải giống hệt nhau ở mọi bảng. Ở 436e mặt còn hơi khác nhau giữa các bộ.

## Việc
Dùng công cụ `image_gen`, tối đa 8 lần (mỗi bảng 1 lần; nếu bảng nào lệch mặt hoặc lệch bộ thì được sửa 1 lần, tổng 3 lần sửa).

Mỗi bảng có kích thước 1536×1024. Mỗi lần gọi công cụ dùng các ảnh đầu vào sau:
- (a) Mặt: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`.
- (b) Thân, dáng và tỷ lệ: ảnh `base-body.v3` mới nhất trong `games/immortality-cultivation/art-src/heroine/fashion/`.
- (c) Thiết kế bộ đồ: ảnh lookbook 436e của đúng bộ đó, cùng thư mục.

Có 5 bảng:
1. `base-body.v3-turn`: chỉ làm nếu ảnh v3 hiện có chưa phải bảng 3 góc sạch.
2. `crimson-bride-turn`
3. `moon-blade-turn`
4. `jade-noble-turn`
5. `shadow-spider-turn`

Quy tắc chung cho mọi bảng:
- Dáng chữ A, tay rời thân khoảng 30°, chân hơi tách.
- Nhìn thẳng ở góc trước, nhìn ngang ở góc nghiêng, góc sau thấy đúng lưng.
- Nền xám trơn, ánh sáng đều, không bóng đổ, không hiệu ứng sáng, không chữ, không watermark.
- Giữ đúng chi tiết bộ đồ trong ảnh lookbook: màu, chất liệu, trang sức, đường xẻ. Mạng che mặt và khăn che mắt vẽ rõ ranh giới để sau tách thành mô hình riêng.
- Mặt ở mọi bảng phải giống ảnh (a).

Ghép tất cả thành `heroine-turnarounds-436f.jpg`. Nếu sandbox không cho ghi thư mục review thì để ở `/private/tmp/typing-game-436f/`.

Đặt tên file `<tên>.v1-try<k>.png`, kèm prompt thật trong `.prompt.txt` cùng tên.

## Ràng buộc
- Không đưa ảnh của game khác vào công cụ.
- Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/436f-report.md`, gồm:
- danh sách ảnh;
- nhận xét độ giống mặt giữa các bảng;
- các ô trang phục thấy được trong từng bảng (tóc, đầu, áo, đai, giày, phụ kiện), để chuẩn bị tách mô hình.
