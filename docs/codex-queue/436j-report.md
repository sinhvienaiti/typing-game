# Báo cáo 436j — Thân nền nữ chính v6

Ngày 18/11/2026. Đã dùng **4/4 lần image_gen**: hai mẫu, mỗi mẫu một lượt sửa. Mỗi lần đều truyền đúng hai ảnh nguồn trong phiếu; không dùng ảnh bên thứ ba. Đây là các phương án để owner chọn, **chưa xác nhận đạt để dựng Tripo**.

## Tệp đã làm

Thư mục ảnh: `games/immortality-cultivation/art-src/heroine/fashion/`.

| Mẫu | Ảnh | Prompt nguyên văn |
| --- | --- | --- |
| A1 | `base-body.v6A-turn.v1-try1.png` | `base-body.v6A-turn.v1-try1.prompt.txt` |
| A2 | `base-body.v6A-turn.v1-try2.png` | `base-body.v6A-turn.v1-try2.prompt.txt` |
| B1 | `base-body.v6B-turn.v1-try1.png` | `base-body.v6B-turn.v1-try1.prompt.txt` |
| B2 | `base-body.v6B-turn.v1-try2.png` | `base-body.v6B-turn.v1-try2.prompt.txt` |

Cả bốn PNG đều 1536×1024. Các tệp nguồn được giữ nguyên.

Bảng so sánh **v5B | A2 | B2**, kèm ô phóng to mặt trước và mặt nghiêng của từng bản:

- `/private/tmp/typing-game-436j/heroine-base-v6-436j.jpg` (2304×1056).
- `/private/tmp/typing-game-436j/ABOUT.md`.
- Hai bảng hỗ trợ đo mặt: `measurement-heads.jpg`, `measurement-heads-grid.jpg`.
- `heroine-base-v6-436j-layout-error.jpg`: bản ghép đầu có lỗi vị trí crop, giữ riêng; **không dùng để chọn mẫu**. Bảng đúng là tệp tên chính ở trên.

Dùng đường dẫn dự phòng theo phiếu vì sandbox chỉ cho ghi repo và thư mục tạm, không cho ghi thư mục review bên cạnh repo. Không cập nhật chỉ mục review bên ngoài phạm vi cho phép.

## Cách đo và độ chắc chắn

Đo trên ảnh gốc, kiểm tra lại mặt bằng ô phóng to có vạch tọa độ. Các mốc giải phẫu chọn thủ công; sai số khoảng ±4–6 px, góc khoảng ±3°. Tóc che đỉnh sọ nên số đầu chỉ là ước lượng, khoảng ±0,5 đầu, không phải chứng nhận chính xác tỷ lệ 9 đầu.

- Chiều cao hình: từ đỉnh búi tóc đến đáy bàn chân, theo từng góc trước / nghiêng / sau.
- Chiều cao giải phẫu: từ đỉnh sọ ước lượng, **không tính búi tóc**, đến đất.
- Số đầu = chiều cao giải phẫu / khoảng đỉnh sọ–cằm; không lấy phần cổ làm chiều cao đầu. Số đo sơ bộ trong quá trình làm có lẫn cổ, đã sửa bằng bảng mặt phóng to.
- Tỷ lệ chân chính = khoảng háng–đất / chiều cao giải phẫu. Có thêm tỷ lệ tính cả búi tóc để tránh nhầm quy ước.
- Góc tay: góc đoạn tâm vai–cổ tay so với trục dọc ảnh, ghi hai tay trong mỗi góc nhìn. Đây là **góc chiếu 2D**, không suy ra góc khớp 3D.
- Lề và khe: dò biên bằng chênh kênh màu trên nền xám, đối chiếu mắt. Các kết quả sát ngưỡng cần coi là chưa chắc đạt; không làm tròn lên để cho qua.

## Số đo từng ảnh

| Ảnh | Số đầu, xấp xỉ | Háng–đất / chiều cao giải phẫu | Háng–đất / chiều cao cả búi | Chiều cao hình trước / nghiêng / sau (px) | Lề nhỏ nhất (px) | Khe nhỏ nhất giữa hình (px) |
| --- | ---: | ---: | ---: | --- | ---: | ---: |
| A1 | 8,0 | 53,3% | 51,1% | 906 / 900 / 901 | ≈44 | ≈78 |
| A2 | 8,7 | 53,4% | 51,5% | 907 / 907 / 907 | ≈39 | ≈60 |
| B1 | 8,5 | 54,0% | 51,9% | 926 / 922 / 922 | ≈31 | ≈32 |
| B2 | 9,0 | 55,3% | 53,3% | 905 / 902 / ≈902 | ≈42 | ≈58 |

Các mốc phía trước dùng tính tỷ lệ, theo thứ tự **đỉnh sọ / cằm / háng / đất**, đơn vị px:

| Ảnh | Các mốc y |
| --- | --- |
| A1 | 80 / 188 / 486 / 949 |
| A2 | 74 / 174 / 481 / 948 |
| B1 | 65 / 170 / 475 / 956 |
| B2 | 75 / 172 / 465 / 947 |

| Ảnh | Tay góc trước | Tay góc nghiêng | Tay góc sau | Kết luận hình học |
| --- | --- | --- | --- | --- |
| A1 | ≈37° / 36° | ≈0°; tay còn lại khuất | ≈36° / 37° | Chưa đạt số đầu và tay nghiêng |
| A2 | ≈36° / 34° | ≈20° / 10° | ≈37° / 36° | Gần 9 đầu; tay nghiêng chưa đạt; lề sát dưới 40 px |
| B1 | ≈34° / 32° | ≈24° / 25° | ≈35° / 35° | Chưa đạt số đầu, tay nghiêng, lề và khe |
| B2 | ≈36° / 34° | ≈27° / 27° | ≈36° / 36° | Gần 9 đầu; tay nghiêng chưa đạt; khe khoảng 58 px, chưa đủ 60 px |

Lưu ý về tư thế: A-pose dạng tay sang hai bên khi xoay nhân vật đúng 90° sẽ bị thu ngắn trong hình chiếu. Để đáp ứng yêu cầu tay mở ngay trên ảnh nghiêng, prompt đã yêu cầu hai tay đưa chéo trước/sau; kết quả vẫn chưa tới 35–45°. Vì vậy chưa thể coi ba hình là một A-pose 3D thống nhất và đạt đủ góc yêu cầu.

## Kiểm tra hình và đề xuất

**Mẫu A — đề xuất A2.** Mặt dài và trưởng thành hơn A1, mắt bớt tròn, môi rõ hơn, dáng thanh lịch. Đồ liền thân vẫn kín và có bề mặt vải mờ. Nhược điểm: gò má còn mềm, ánh mắt còn hiền, tỷ lệ đầu mới gần mục tiêu; tay nghiêng và lề chưa đủ chắc. Phù hợp để owner cân nhắc hướng thanh lịch, chưa nên dùng ngay làm nguồn Tripo.

**Mẫu B — đề xuất B2.** Đầu nhỏ tương đối, cổ và chân cho cảm giác cao hơn; eo gọn và đường cong nghiêng rõ hơn v5B. Tỷ lệ gần 9 đầu và tỷ lệ chân là tốt nhất trong bốn ảnh. Nhược điểm: mức khác biệt về môi, ánh mắt và đường cong so với A2 còn nhẹ; chưa đạt rõ sắc thái “quyến rũ đậm hơn”. Tay nghiêng và khe giữa hình chưa đạt. Nếu chọn theo tỷ lệ thân, ưu tiên owner xem B2 trước.

Cả hai lượt sửa đều có đúng mặt trước, nghiêng và lưng; chân trần, hai chân trước/sau có khe, tóc búi gọn và trang phục giữ độ che phủ. Da hồng hơn nhưng mức trắng sứ và khối gò má vẫn cần owner xem ở ô phóng to. Các ngón tay thấy tách ở đa số bàn tay; chưa xác nhận giải phẫu từng ngón ở tay xa. Nền xám còn biến thiên sắc độ nhẹ, chưa hoàn toàn đồng nhất. Không có bóng đổ nền rõ hay điểm chói mạnh; vải chủ yếu là mờ.

**Owner cần xem:** A2 hay B2 phù hợp nét mặt và dáng mong muốn; B2 đã đủ khác A2 về độ quyến rũ hay chưa. Đây là lựa chọn hướng, chưa phải đề nghị bỏ qua các lỗi hình học.

## Phần không làm

- Không gọi lần thứ năm: đã hết số lượt mà phiếu cho phép; giữ đủ cả bốn ảnh và prompt.
- Không dựng Tripo, sửa code, làm video, chạy build/test, đổi nhánh hoặc thực hiện thao tác Git ghi dữ liệu.
- Không chấm điểm thay hai giám khảo độc lập; chưa có duyệt thẩm mỹ hay nghiệm thu trong play host.
- Không hậu kỳ kéo đầu/chân hoặc sửa giải phẫu bằng công cụ khác. ImageMagick chỉ ghép và phóng to bảng so sánh.

