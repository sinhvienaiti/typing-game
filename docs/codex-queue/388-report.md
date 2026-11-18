# Phiếu 388 — Duyệt bố cục nữ kiếm tu

Đã xem [chân dung A](../../../typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png), [tờ vòng 4](../../../typing-game-review/owner-review/2026-11-12/tu-tien/heroine/codex-350-r4.jpg) và đọc [brief gốc](/private/tmp/claude-501/-Volumes-SS990TPRO-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/gemini-heroine-prompt.txt). Đây là tư vấn thay Gemini, chưa phải chấm mù hay duyệt đạt 8,5 trong game.

1. **Ba nguyên nhân gốc** (suy luận từ ảnh, chưa có biên bản hai giám khảo):
   - **Chuyển sai thứ bậc thị giác:** chân dung sang nhờ lớp vải, chàm–ngà và vật liệu; vòng 4 dồn chú ý vào viền sáng, đai, chim ở gấu và ấn lưng. Ô 66 px biến chúng thành nhiều vệt sáng ngang cạnh tranh.
   - **Hình bóng thiếu chữ ký chiến đấu:** cổ vai hiện bo như áo choàng ngắn, chưa thành vai vuông của brief; thân áo xòe đều, quần khá hẹp. Kiếm ngang eo nhỏ khó gánh vai trò kiếm tu.
   - **Danh sách chi tiết lấn át thiết kế:** lưng chàm chiếm ưu thế, cảm giác khác tỷ lệ 60 ngà/30 chàm; mặt vòng 4 trẻ, tròn hơn chân dung. Thêm thêu không khôi phục được khí chất trưởng thành và cấu trúc trang phục.

2. **Năm mảng lưng–vai đề xuất:** (a) cổ vai chàm hình chữ nhật, viền ngà rõ; (b) tay trái ngà; (c) tay phải ngà; (d) ô lưng chàm mang phượng, có khoảng ngà cách cổ vai; (e) đai chàm ngang, cách ô phượng bằng dải ngà. Hai tay tạo khung sáng, phượng làm tiêu điểm; hoa văn phụ chìm hơn. Đây là mục tiêu bố cục, cần kiểm tra ở đúng 66 px, camera 55°, trên sân đá; nền xanh hiện tại chưa chứng minh độ nổi.

3. **Một sửa hình bóng:** thay mép vai rủ cong bằng hai bậc vai vuông ngắn, mỗi bên rộng thêm khoảng 1 px trong hình chiếu 66 px. Giữ mép trên cơ delta, tay nâng được; không kéo thành cánh hay áo choàng.

4. **Tấm ấn phượng:** giữ kích thước khoảng 25% chiều cao toàn nhân vật theo brief, trên ô chàm giữa lưng. Gom đầu–cánh–đuôi thành dấu lớn có khoảng âm, vàng cũ dịu; giảm vòng tròn bao và nét lông li ti. Là thêu trên vải, không biến thành đĩa giáp nổi. Chừa khoảng với búi tóc, đai và kiếm. Ở 66 px cần đọc được dấu phượng; nét tinh dành cho zoom 250 px.

5. **Ba quy tắc prompt vòng sau:**
   - Đính đúng hai ảnh trên: A khóa danh tính, nét trưởng thành, vật liệu; vòng 4 khóa cấu tạo cần giữ. Chân dung/cut-in giữ mặt tả thực; 3D giữ mặt donghua sạch theo hướng C.
   - Mở đầu bằng năm mảng và vai vuông; giữ lụa ngà, chàm, vàng cũ, độ giàu vật liệu ở mảng chính. Chỉ định thứ bậc sáng tối; giữ màu tín hiệu ở cường độ thấp.
   - Khóa một thiết kế qua các góc, A-pose và mốc trang phục; yêu cầu góc chơi cùng ô 66 px. Tách nguồn dựng Tripo khỏi tờ trình bày; hào quang và dải lụa thi triển thuộc VFX riêng.

6. **Câu 1 — Hoàng tộc và kiếm tu?** Có nền hoàng tộc nhờ diadem, ngọc, cổ cao; kiếm tu mới đạt một phần. Cần vai có cấu trúc, tay linh hoạt, kiếm dễ nhận và cách rút hợp lý. Chất Việt là ý định trong brief; ảnh này chưa đủ xác nhận tính đúng lịch sử.

7. **Câu 2 — Lưng vai đủ riêng ở 66 px?** Chưa; nhận ra bảng màu và búi tóc nhiều hơn trang phục. Thử đúng thay đổi ở mục 3 trước khi thêm đồ.

8. **Câu 3 — Lỗi rig/Tripo/clip dự kiến?** Tua, ngọc sát thân/vạt dễ dính khi dựng; kiếm ngang eo có nguy cơ xuyên khuỷu; cổ vai dễ méo khi Cast_Heavy. Tách phụ kiện, xác định socket và kiểm tra rút/cất kiếm; thử Run, Cast_Heavy, Dash, Down. Đây là rủi ro, chưa phải lỗi đã đo trên model.

9. **Câu 4 — Hợp đồng thiếu gì?** Khóa đơn vị, tỷ lệ, bind pose, tên xương, socket, đường nối ổ đồ, vùng che thân và phần thân ẩn; quy định quyền sở hữu phụ kiện, giới hạn vạt/xương phụ, khoảng hở theo clip. Bộ lễ A phải chứng minh đổi đồ cùng skeleton trước khi mở rộng.

10. **Câu 5 — Ba rủi ro lớn nhất/cách tránh:** mất nhận diện ở xa → duyệt bố cục 66 px trước thêu; lệch mặt/cấu tạo giữa góc → khóa mốc và đối chiếu từng góc; đồ đẹp nhưng va xuyên → thử bộ chiến và bộ lễ trên cùng toàn bộ clip trước sản xuất hàng loạt.

11. **Nhật ký tự rà:**
   - Lần 1 — **FAIL**: “A khóa mặt” dễ kéo model về tả thực, trái hướng C; “chiều cao thân người” mơ hồ. Đã sửa mục 4–5; làm rõ vị trí tua ở mục 8. Chuỗi PASS: 0.
   - Lần 2 — **PASS**: đối chiếu ảnh và brief; giữ hướng C, trang phục ngắn, thêu phượng và VFX riêng. Đủ năm câu hỏi; rủi ro model được ghi là dự kiến. Chuỗi PASS: 1.
   - Lần 3 — **PASS**: rà tính nhất quán và phạm vi; đủ 3 nguyên nhân, 5 mảng, 1 sửa hình bóng, xử lý phượng, 3 quy tắc. Không suy diễn thành kết quả trong game; dưới 900 chữ. Chuỗi PASS: 2.
