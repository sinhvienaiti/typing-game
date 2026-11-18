# Phiếu 339 · Ba hướng Kiếm tu nữ · 12/11/2026

Đã tạo **6 góc ảnh, 3 bản vẽ lại, 9 prompt nguyên văn**, tấm ghép và số đo tại `games/immortality-cultivation/art-src/heroine/`. Dùng đúng **9/9 lần image_gen**, **12/12 ảnh view_image**. Chỉ thêm file mới trong thư mục được phép và báo cáo này; không sửa mã, không chạy build/test, không dùng Git ghi.

**Chưa đạt trọn yêu cầu kỹ thuật:** B sau vẫn ra 1055×1491, khác 3:4 và khác khổ ảnh trước, dù đã vẽ lại. Nền cả bộ gần xanh lục nhưng không thuần #00FF00. Giữ nguyên mọi đầu ra; không ghi đè, kéo méo hoặc sửa màu để che sai lệch. Hết ngân sách 9 lượt nên dừng vẽ tại đây.

Xem [tấm ghép](../../games/immortality-cultivation/art-src/heroine/directions-339-sheet.jpg). Bảng dùng **A trước try2 / A sau try1; B trước try2 / B sau try2; C trước/sau try1**, trước ở trên, sau ở dưới.

## Số đo và tự chấm

Đo bằng ImageMagick 7: điểm nền khi R≤32, G≥223, B≤32 (thang 255); hộp bao lấy **tất cả điểm còn lại**, gồm kiếm và dải lụa. Lề theo thứ tự **trái/phải/trên/dưới (%)**. ΔH = |H_sau−H_trước|/H_trước; dùng chiều cao hộp bao bằng pixel. B khác khổ nên ghi thêm ΔH chuẩn hóa theo chiều cao canvas: **1,30%**. Số đo gốc và RGB bốn góc: [measurements-339.json](../../games/immortality-cultivation/art-src/heroine/measurements-339.json).

Điểm 0–10, theo thứ tự **bản sắc / đúng hướng / hai tay / lưng thật / gom khối mesh / sức hút thương mại**. Điểm chung là số thấp nhất; “—” là không áp dụng cho ảnh trước. Đây là **tự chấm phương án**, không thay chấm mù hoặc nghiệm thu trong game; ảnh sau chỉ đối chiếu tóc, gáy, diadem và tỷ lệ, không xác minh khuôn mặt.

| Ảnh (`dir-…png`) | Lề T/P/Tr/D (%) | H (px); ΔH cặp | Điểm từng tiêu chí | Thấp nhất | Nhận xét; vẽ lại |
| --- | --- | --- | --- | --- | --- |
| a-front.v1-try1 | 25,97/29,01/3,66/4,01 | 1337; 17,35% với A sau | 8,7/8,4/9/—/8,5/8,6 | 8,4 | Lề trên/dưới trượt; đã vẽ try2. |
| a-front.v1-try2 | 31,77/32,60/13,88/12,98 | 1059; **4,34%** | 8,6/8,4/9/—/8,5/8,5 | 8,4 | Chọn ghép; cổ chữ nhật, hai tay cầm kiếm rõ. |
| a-back.v1-try1 | 29,19/33,52/12,22/11,46 | 1105; **4,34%** | 8,4/8,0/8,5/9/8,5/8,4 | 8,0 | Lưng thật, cổ/phượng rõ; vị trí nắm kiếm khác trước, ngọc bội đổi phía nhìn. Không vẽ lại. |
| b-front.v1-try1 | 12,34/12,25/12,57/7,32 | 1160; 10,09% với B sau try1 | 8,6/8,5/9/—/8,2/8,6 | 8,2 | Lề dưới trượt; đã vẽ try2. |
| b-front.v1-try2 | 18,14/17,03/16,92/14,09 | 999; **4,30%** | 8,5/8,5/9/—/8,2/8,5 | 8,2 | Chọn ghép; hai dải S, sen/lá đề, kiếm không phát sáng. |
| b-back.v1-try1 | 16,97/13,65/17,04/13,01 | 1043; 4,40% với B trước try2 | 8,4/7,5/9/8,7/8,2/8,5 | **7,5** | Sai khổ; gáy thật nhưng còn viền bên đầu. Đã vẽ try2. |
| b-back.v1-try2 | 16,97/13,74/17,04/13,08 | 1042; **4,30%** | 8,4/7,5/9/8,7/8,2/8,5 | **7,5** | Chọn ghép để so hướng; vẫn sai khổ, chưa đạt. Không còn lượt. |
| c-front.v1-try1 | 25,41/26,34/14,02/11,40 | 1080; **0,09%** | 8,6/8,4/9/—/8,7/8,6 | 8,4 | Áo ngắn, tay bó, thế sẵn sàng; tay nắm chuôi rõ. Không vẽ lại. |
| c-back.v1-try1 | 21,82/27,35/13,88/11,60 | 1079; **0,09%** | 8,4/8,3/9/9/8,7/8,6 | 8,3 | Ấn phượng tròn và kiếm ngang lưng rõ; ngọc bội lệch bên so trước. Không vẽ lại. |

Các ảnh A/C và B trước đều **1086×1448 (3:4)**; cả hai B sau **1055×1491**. Sáu bản chọn đều đạt lề ≥8% và ΔH≤5%. Bốn góc cả 9 ảnh có R=13–22, G=235–244, B=9–24; sai số kênh lớn nhất so #00FF00 là **24/255**, đạt cách hiểu “gần” ở ngưỡng 32 nhưng **không đạt nền thuần**. Không thấy bóng nền rõ bằng mắt; phép đo trên không chứng minh nền phẳng tuyệt đối.

## Anh cần xem

**A:** dấu hoàng tộc và cổ phượng sau rõ nhất, còn dáng lễ phục. **B:** hai dải lụa cuốn hút nhưng cần sửa khổ trước khi dùng làm nguồn. **C:** tư thế chiến đấu và khối áo/quần dễ đọc nhất; ấn phượng sau rõ. Anh chọn hướng và đối chiếu lại mặt với chân dung A; đặc biệt xem cách nắm kiếm A và vị trí ngọc bội A/C.

Đã đọc brief §1/4/5/6 và hai ảnh chỉ định. Chỉ gửi chân dung duyệt cùng các ảnh mới của phiếu làm tham chiếu; bản 25/10 trượt chỉ xem để tránh. Mỗi prompt sau liệt kê đủ 8 chi tiết liên tục. Không làm bốn góc, 3D, tích hợp hoặc chấm mù vì ngoài phiếu. Không có âm thanh cần làm. Chưa có ảnh nào được tuyên bố nghiệm thu ≥8,5.
