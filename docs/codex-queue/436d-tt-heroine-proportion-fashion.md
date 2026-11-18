# Phiếu 436d: Nữ chính, sửa tỷ lệ cơ thể và vẽ lại thời trang theo dáng riêng

Phản biện: PASS (Sonnet, 17/11; vòng 1 chỉ lỗi cách đo tỷ lệ, đã sửa)

## Bối cảnh: owner chê ngày 17/11
- Trang phục: "sao bạn vẽ xấu vậy, không thể vẽ các dạng trang phục đẹp như này ak". Kèm bảng tham khảo trang phục game tu tiên đang hot. Claude chỉ phân tích bảng này bằng lời; **không đưa ảnh game khác vào công cụ**.
- Cơ thể: "cân bằng cơ thể của bạn nhìn rất xấu, nhìn lùn tịt vậy".

Claude phân tích các bản 436, 436b và 436c, thấy những lỗi sau:
- Đầu to, chân ngắn, khoảng 6,5 đầu.
- Cả ba bộ cùng một dáng áo dài suông, voan nhiều lớp, chỉ khác màu.
- Không có món nào tạo điểm nhấn.
- Ánh sáng phẳng, dáng chữ A, nên trông như catalogue.

Điều làm bảng tham khảo đẹp:
- Tỷ lệ cao ráo khoảng 8,5 đầu, chân dài hơn nửa chiều cao, eo cao, cổ thon dài.
- Mỗi bộ một dáng riêng hẳn: váy xẻ cao, áo ôm thân, quần short với tất đen, vạt lệch, khoét vai.
- Một món nổi bật: khăn hoặc mạng che mặt, băng tay giáp, hoa văn vẽ trên da.
- Một màu chính đậm, ví dụ đỏ trên đen hoặc trắng điểm đỏ.
- Chất liệu tương phản: ren, lụa, da, kim loại.
- Tư thế thời trang, ánh sáng sân khấu.

## Việc
Dùng công cụ `image_gen`, tối đa 8 lần.

Ảnh tham chiếu duy nhất được dùng (của dự án): `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`, chỉ để giữ khuôn mặt. Không dùng thân nền cũ vì sai tỷ lệ.

1. **Thân nền mới `base-body.v2`** (1 bảng 3 góc trước, nghiêng, sau, 1536×1024, dáng chữ A, nền xám trơn, ánh sáng đều):
   - cao 8,5 đầu;
   - cách đo: 1 đầu = từ đỉnh đầu (không tính búi tóc) đến cằm; chiều cao = đỉnh đầu đến lòng bàn chân (không tính đế giày). Đầu ≈ 11,8 % chiều cao (8,5 đầu);
   - đáy chậu (inseam) ở ≤ 50 % chiều cao tính từ đỉnh đầu, tức chân trong ≥ 50 %; khớp hông xuống đất ≥ 52 %;
   - vai ở khoảng 1,5 đầu, eo ở khoảng 3 đầu tính từ đỉnh đầu;
   - eo hẹp và cao, vai thon, cổ dài, đầu nhỏ;
   - đi giày đế mỏng hoặc gót thấp;
   - áo lót ôm trung tính;
   - **vẽ thêm vạch kẻ ngang mỏng chia 8,5 đầu ở mép phải** để kiểm tra.
   - **Dừng lại sau bước này** nếu tỷ lệ chưa đúng (tự đo theo vạch).
2. **Bốn bộ thời trang trên thân nền mới.** Mỗi bộ một ảnh "lookbook" 1024×1536: toàn thân, tư thế thời trang tự tin, ánh sáng sân khấu, nền tối đơn giản có điểm sáng. Mỗi bộ một dáng khác hẳn nhau:
   - **`crimson-bride`**: váy đỏ thẫm ôm thân xẻ đùi cao, áo ren đỏ khoét vai, mạng che mặt voan đỏ trên búi tóc, bao tay vàng, thêu phượng vàng.
   - **`moon-blade`**: áo trắng ngà ngắn ôm eo, quần short và tất đen mỏng, áo choàng xanh băng vạt lệch một bên vai, đai bạc, khăn bạc che mắt mỏng, kiếm bên hông.
   - **`jade-noble`**: áo dài xanh ngọc đậm cổ đứng, ôm thân trên, xẻ hai tà dài, quần lụa ngà bên trong, áo khoác lửng tay rộng, viền vàng, trâm ngọc và ngọc bội lớn làm điểm nhấn.
   - **`shadow-spider`**: áo đen ren và da ôm thân, hở eo nhẹ, váy xẻ nhiều dải đen–xanh rêu, băng tay giáp vàng, vương miện gai nhỏ, hoa văn mực vẽ trên tay.
   - Tỷ lệ màu ~60/30/10 mỗi bộ, chất liệu tương phản (ren, lụa, da, kim loại). Gợi cảm có chừng mực kiểu game thương mại, không hở quá mức.
3. Ghép tờ `heroine-lookbook-436d.jpg` gồm thân nền v2 và 4 bộ. Ghi bên dưới mỗi ảnh tỷ lệ đầu/chiều cao đo được.

Lưu ảnh ở `games/immortality-cultivation/art-src/heroine/fashion/<tên>.v1-try<k>.png` (thân nền là `base-body.v2-try<k>.png`), kèm prompt thật trong `.prompt.txt`. Nếu sandbox không cho ghi thư mục review thì để tờ ghép ở `/private/tmp/typing-game-436d/`.

Phong cách: nhân vật game tu tiên thương mại cao cấp, cuốn hút, thời trang, sang trọng, hiện đại. Không chữ, không watermark, không hào quang.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/436d-report.md`, gồm số đo tỷ lệ của từng ảnh.
