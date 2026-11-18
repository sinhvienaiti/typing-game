# Phiếu 344 · Tu Tiên · Bộ bốn góc nhân vật chính · vòng 2

**Kết quả: đủ bộ file bàn giao; CHƯA ĐẠT nhận dạng và độ nhất quán.** Không dùng bộ này làm nguồn 3D đã duyệt. Tự chấm thấp nhất của bộ chọn: **7,3/10**. Đã vẽ lại bảng bốn góc yếu nhất một lần, đồng thời sửa riêng ảnh trước và ảnh sau; tổng cộng **8/8 lần image_gen**, **14/14 lần view_image**. Không có HTTP 429 hoặc thông báo thời điểm mở lại hạn mức.

## File bàn giao

Thư mục: `games/immortality-cultivation/art-src/heroine/` (viết qua đường dẫn `/Volumes/SS990TPRO/htdocs/typing-game`).

Năm tên `r2-*.v1-try1.png` mà phiếu yêu cầu đều có, kèm prompt chính xác. Giữ nguyên cả lượt đầu và lượt sửa. **Bộ dùng để xem/đo trong báo cáo là năm bản chuẩn hóa mới dưới đây**, không phải ảnh gốc chưa chỉnh lề:

| Vai trò | File chọn |
| --- | --- |
| Bảng trước, trái, sau, phải | `r2-turnaround.v1-try2-normalized.png` |
| Trước | `r2-view-front.v1-try2-normalized.png` |
| Sau | `r2-view-back.v1-try2-normalized.png` |
| Trái | `r2-view-left.v1-try1-normalized.png` |
| Góc chơi | `r2-view-play.v1-try1-normalized.png` |

Mỗi PNG/JPG đều có file cùng tên gốc và đuôi `.prompt.txt`. Prompt của 8 lượt AI đều có 11 chi tiết nhận dạng, đường dẫn tham chiếu và câu **“same face, same hair and diadem as the reference portrait”**. Prompt cạnh bản chuẩn hóa sao chép nguyên prompt AI; thao tác hậu kỳ được ghi riêng ở dưới và trong JSON.

- `r2-344-sheet.jpg`: bảng bốn góc, bốn ảnh đơn, tấm so mặt, ô 66 px nguyên cỡ và bản phóng 4× nearest-neighbour.
- `r2-344-face-compare.jpg`: chân dung gốc, ảnh trước lượt 1 và lượt 2 cạnh nhau, cùng cỡ khung mặt.
- `r2-344-back-66.png`, `r2-344-play-66.png`: đúng 66×66 px; nhân vật cao 62 px.
- `r2-344-checks.json`, `r2-344-measurements.json`: khổ ảnh, hộp bao, lề, nền và chiều cao từng cột.

Tổng cộng 17 PNG/JPG mới: 8 ảnh AI, 5 bản chuẩn hóa, 4 ảnh kiểm tra; 17 prompt và 2 JSON. Không thay ảnh, prompt hay mã có trước phiếu.

## Tham chiếu và cách làm

Mở chân dung `art-src/identity/kiem-tu-portrait.png` trước từng lần vẽ, đủ 8 lần; xem bốn ảnh vòng 1 được phiếu chỉ định. Chỉ đưa ảnh trong repo vào image_gen. Chân dung điều khiển mặt, tóc, diadem; vòng 1 chỉ cung cấp bố trí trang phục/phụ kiện. Ảnh trước đầu tiên của vòng 2 chỉ dùng chân dung làm đầu vào để giảm ảnh hưởng khuôn mặt sai ở vòng 1. Các lượt sau dùng thêm ảnh vòng 2 để giữ cấu tạo trang phục.

Áp dụng hướng dẫn `game-character-design`, `game-art-pipeline`, `imagegen`, `agent-orchestration` trong phạm vi phiếu ảnh đã chốt. Không mở hướng thiết kế mới, không nhờ thêm trợ lý, không tạo hào quang. Đọc rate_limits trước khi làm: còn 100% cửa sổ ngắn, 65% tuần.

## Kiểm kỹ thuật

Ảnh AI gốc cùng khổ 1672×941; các ảnh đơn có lề trên/dưới quá nhỏ. Không ghi đè chúng. Tạo bản chuẩn hóa bằng ImageMagick 7: tách xanh với fuzz 30%, trim, thu/phóng **giữ tỷ lệ** vừa 2148×1152, đặt giữa canvas 2560×1440 trên `#00FF00`. Không vẽ lại, nắn mặt, đổi phụ kiện hoặc ghép thêm hình. Không dùng AI tăng chi tiết mặt.

| Bản chuẩn hóa | Khổ | Chiều cao hình, px | Lề trái / trên / phải / dưới |
| --- | --- | --- | --- |
| Turnaround lượt 2 | 2560×1440, 16:9 | 1149 toàn bảng | 8,047% / 10,069% / 8,047% / 10,139% |
| Trước lượt 2 | 2560×1440, 16:9 | 1152 | 36,992% / 10% / 37,031% / 10% |
| Sau lượt 2 | 2560×1440, 16:9 | 1152 | 36,719% / 10% / 36,719% / 10% |
| Trái lượt 1 | 2560×1440, 16:9 | 1152 | 37,734% / 10% / 37,734% / 10% |
| Góc chơi lượt 1 | 2560×1440, 16:9 | 1152 | 37,344% / 10% / 37,383% / 10% |

Bốn nhân vật trong turnaround cao lần lượt **1149 / 1147 / 1149 / 1147 px**. Chênh lớn nhất giữa tất cả hình được chọn: **0,4359%**, dưới 3%. Bốn dải lề ngoài 8% của cả năm bản chuẩn hóa đều chỉ có một màu **RGB(0,255,0)**. Kiểm bằng ImageMagick, không suy từ ảnh xem trước. Không thấy bóng sàn, hào quang hoặc chữ trong ảnh nguồn nhân vật. Nhãn chỉ xuất hiện trên tấm kiểm tra.

## Nhất quán 11 chi tiết × 4 góc

Bảng này xét bốn cột của `r2-turnaround.v1-try2-normalized.png`. “Khuất” là bị cơ thể che đúng góc nhìn, không được tính thành đã chứng minh đúng. Các sai lệch với ảnh đơn ghi sau bảng.

| Chi tiết | Trước | Trái | Sau | Phải |
| --- | --- | --- | --- | --- |
| 1. Mặt đúng chân dung 24 tuổi | CHƯA: mắt/mũi/môi/hàm khác | Trưởng thành hơn vòng 1 nhưng chưa chứng minh cùng người | Khuất | Profile khá gần góc trái; chưa khớp chân dung |
| 2. Tóc bóng, búi gọn ôm đầu | Bớt dựng cao | Búi thấp/gọn hơn | Búi tròn sát đầu | Cấu trúc búi vẫn hơi khác bên trái |
| 3. Diadem thanh, cao, chạm rỗng, hai tua | Có ngọc/vàng/tua; vẫn thành vòng hoa thấp | Có crest và tua; chạm rỗng chưa đúng | Có hai tua; crest giống mặt trước đặt ra sau | Vẫn thiên vòng hoa; tua xa bị khuất |
| 4. Cổ Nhật Bình lõi chàm, rìa ngà rộng ≥4% H | Lõi/rìa có; rìa chưa đủ bề rộng | Mỏng hơn vòng 1; rìa chưa đủ | Có lõi/rìa, vẫn hơi cứng | Có lõi/rìa; chưa đủ bề rộng |
| 5. Áo giữa đùi, hò chéo, xẻ hông, lớp trong | Có hò chéo, cổ/tay trắng, tà ngắn | Thấy lớp và khe hông | Tà giữa đùi; mặt trước khuất | Có lớp và khe hông |
| 6. Quần suông mềm bó cổ chân, giày cao | Có; hai chân rõ | Có; hai chân rõ | Có; hai chân rõ | Có; hai chân rõ |
| 7. Đai chàm, vàng cũ, khóa ngọc | Khóa rõ | Thấy một phần khóa | Khóa/hoa văn lưng tự phát sinh | Cấu tạo bên phải chưa đối xứng hoàn toàn |
| 8. Ngọc bội bên trái | Đúng bên trái nhân vật | Thấy ngọc và tua | Lệch gần cạnh trái, một phần bị kiếm/tà che | Khuất hợp góc; không thể kiểm chắc |
| 9. Ấn phượng 25% H, cùng độ nhô | Khuất | Có cạnh; độ dài vẫn nhỏ hơn cột sau | Lớn hơn lượt 1; vẫn chưa đúng 25% | Có cạnh; tương tự góc trái nhưng chưa đồng nhất đường kính |
| 10. Kiếm thấp ngang xương cùng, chuôi phải 10°, đai treo | Phần lớn khuất | Chuôi nhô sau, có vòng treo | Phân biệt chuôi/vỏ, hai vòng/đai rõ; góc nghiêng gần yêu cầu | Vòng treo và kiếm có nhưng hilt/chape chưa đối ứng hoàn toàn |
| 11. Hai đuôi lưng ngắn, viền mây hạc | Có tà ngắn và mây hạc | Tà ngắn; hoa văn có | Hai đuôi và mây hạc rõ | Tà ngắn; mô-típ còn đổi nét |

Các lỗi còn lại đáng kể:

1. **Mặt chưa khớp**, dù không còn ngắn như vòng 1. Ảnh trước lượt sửa không tạo được cải thiện chắc chắn về nhận dạng.
2. **Diadem chưa giữ kiến trúc cao, thanh, chạm rỗng của chân dung**. Búi đã bớt dựng nhưng một số góc vẫn có khối tròn rõ.
3. **Rìa ngà tấm cổ chưa đạt 4% chiều cao người**; nhìn khoảng 1–2% theo bề rộng dải ở ảnh trước, là ước lượng thị giác, không phải số đo chính xác.
4. **Ấn không đồng nhất giữa bộ ảnh đơn và bảng**. Ảnh sau sửa lớn lên rõ, đường kính nhìn khoảng 23% H; bảng sau khoảng 21–22% H; ảnh chơi và ảnh trái riêng vẫn nhỏ hơn đáng kể. Đây là ước lượng từ hình chiếu; góc nghiêng không đủ để khôi phục chính xác đường kính 3D.
5. Vải chàm bớt tím nhưng vẫn hơi xám/tím ở quần; ngà còn ấm, vàng hơi hồng ở vài nét. Chất tóc, lụa, kim loại, ngọc đã tách được ở cỡ lớn.
6. Góc chơi thấy cả hai tay, hai chân; camera nhìn từ sau chếch có nâng cao nhưng **chưa xác minh đúng 30°**. Chưa nhận làm chuẩn camera.
7. Ảnh trái riêng và hai cột bên đã sửa được tay dính hông/chân chồng nhau. Đó là cải thiện rõ nhất của vòng này.

## Tấm so mặt và ô 66 px

Cắt mặt chân dung ở `240x264+348+100`, mặt hai ảnh trước ở `100x110+786+70`; mỗi ô lên 300×330, giữ tỷ lệ khung. Chân dung góc 3/4, ảnh mới chính diện nên không dùng tỷ số pixel thô để kết luận nhận dạng. Chi tiết ảnh trước gốc ít hơn, bản so có nội suy thông thường và không bù chi tiết bằng AI.

| Bộ phận | Nhận xét sau khi xem cạnh nhau |
| --- | --- |
| Mắt | Cùng nhóm mắt hạnh nhân nhưng mắt mới tròn/mở hơn, đường mí và đuôi mắt khác; chưa cùng khuôn mặt |
| Mũi | Mũi mới nhỏ và ngắn hơn, đầu mũi khác; mất độ dài/thể tích của chân dung |
| Miệng | Môi mới đậm và đối xứng hơn; dáng môi, khóe và khoảng cách mũi–miệng khác |
| Hàm | Cằm/hàm mới gọn nhọn hơn; phần má và đường hàm thiếu nét trưởng thành của chân dung |

Ở **66×66 px**, đường nét tóc, tấm cổ, khối ấn và kiếm vẫn phân biệt được; ngón tay, cấu tạo giá treo và hoa văn nhỏ không còn đọc rõ. Cả hai tay vẫn thấy ở góc chơi. Ấn góc chơi nhỏ hơn ấn ảnh sau nên vẫn nhận ra lệch tỷ lệ khi đặt cạnh nhau.

## Tự chấm theo mặt yếu nhất

Điểm tự chấm phục vụ phiếu này, **không phải điểm của hai giám khảo mù**. Mỗi dòng lấy giá trị thấp nhất trong bốn tiêu chí, không lấy trung bình.

| Ảnh AI | Hấp dẫn | Đúng phiếu / nhận dạng | Đọc ở cỡ chơi | Sạch hình | Thấp nhất |
| --- | --- | --- | --- | --- | --- |
| Turnaround lượt 1 | 8,0 | 6,8 | 7,6 | 8,5 | **6,8** |
| Trước lượt 1 | 8,2 | 7,4 | 8,0 | 8,5 | **7,4** |
| Sau lượt 1 | 8,1 | 7,3 | 8,0 | 8,5 | **7,3** |
| Trái lượt 1 | 8,1 | 7,8 | 8,0 | 8,5 | **7,8** |
| Góc chơi lượt 1 | 8,1 | 7,4 | 8,0 | 8,5 | **7,4** |
| Trước lượt 2 | 8,2 | 7,3 | 8,0 | 8,5 | **7,3** |
| Sau lượt 2 | 8,1 | 7,8 | 8,1 | 8,5 | **7,8** |
| Turnaround lượt 2 | 8,1 | 7,3 | 8,0 | 8,4 | **7,3** |

Lượt 6 sửa mặt/diadem và rút ngắn tà của ảnh trước; lượt 7 tăng ấn và chỉnh treo kiếm ảnh sau; lượt 8 vẽ lại turnaround yếu nhất, ưu tiên tay/chân hai cột bên và ấn lớn. Đã chạm trần 8 lần gọi của phiếu, không gọi lần 9. Không có thời gian reset từ công cụ vì không gặp giới hạn dịch vụ. Các bản chuẩn hóa chỉ giải quyết khổ, nền, lề và chiều cao, **không nâng điểm nhận dạng**.

## Phần không làm và việc chủ nhân cần xem

Không sửa mã, không chạy build/test của game, không mở cổng; không chạy lệnh Git ghi. Không chỉnh file có trước, không viết vào src/scripts/tests/docs của Tu Tiên, không tạo bản sao trong thư mục review ngoài phạm vi phiếu. Chỉ thêm `H/r2-*` và báo cáo này.

Không gọi giám khảo mới, không đưa sang Tripo, không tích hợp vào game; phiếu chỉ giao ảnh và tự kiểm. Không vẽ thêm sau 8/8 lượt.

Chủ nhân nên mở **`r2-344-sheet.jpg`** trước, rồi **`r2-344-face-compare.jpg`** ở cỡ thật. Điểm cần quyết định ở vòng tiếp theo là khóa nhận dạng mặt/diadem từ một ảnh cận mặt đủ lớn trước khi sinh toàn thân; bộ hiện tại giữ để đối chiếu, **không đánh dấu đã duyệt**.

