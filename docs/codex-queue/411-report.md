# Phiếu 411 — Ảnh tham chiếu 10 thủ ấn tu tiên

Ngày 16/11/2026. Đã dùng **8/8 lượt image_gen tích hợp**, tạo đủ hai bảng nửa thân (mỗi bảng năm ấn) và một bảng cận **10 cặp tay**, nhãn tiếng Anh S0–S9. Mọi PNG đều **1536×1024**; giữ toàn bộ tám lượt và prompt thật cạnh ảnh. Không gặp HTTP 429 hoặc giờ bắt buộc chờ. Hạn mức Codex đầu phiếu: đã dùng 61%, còn 39%.

## Tệp giao và cách đọc

Thư mục chung: [hand-seals](../../games/immortality-cultivation/art-src/concept/hand-seals/).

| Tệp được chọn | Nội dung |
|---|---|
| [seals-front-s0-s4.v1-try3.png](../../games/immortality-cultivation/art-src/concept/hand-seals/seals-front-s0-s4.v1-try3.png) | S0 Origin Rest; S1 Sword Fingers; S2 Sprouting Branches; S3 Guiding Flow; S4 Hidden Ember |
| [seals-front-s5-s9.v1-try2.png](../../games/immortality-cultivation/art-src/concept/hand-seals/seals-front-s5-s9.v1-try2.png) | S5 Mountain Ward; S6 Thunder Command; S7 Crystal Closure; S8 Guiding Wind; S9 Opening Heaven |
| [seals-hands-s0-s9.v1-try3.png](../../games/immortality-cultivation/art-src/concept/hand-seals/seals-hands-s0-s9.v1-try3.png) | Mười cặp tay chính diện, lưới 5×2, để xem ngón |
| [seals-sheet-411.jpg](../../games/immortality-cultivation/art-src/concept/hand-seals/seals-sheet-411.jpg) | Ghép dọc ba tấm trên, **1536×3072**, JPEG khoảng 0,98 MB |

Mỗi ảnh có `<tên>.prompt.txt`. Riêng prompt của ảnh ghép ghi nguồn và argv ImageMagick 7 thực tế; đây là phép ghép cơ học, không phải lượt tạo thứ chín. Không cắt, tô lại hoặc đổi kích thước nguồn. Các bản cũ `front-s0-s4` try1–2, `front-s5-s9` try1 và `hands-s0-s9` try1–2 vẫn nguyên vẹn, không dùng trong ảnh ghép.

## Căn cứ và lựa chọn phạm vi

Mỗi lượt đều đính kèm [ảnh 403](../../../typing-game-review/owner-review/2026-11-16/tu-tien/hero-anim-r2/run-IpDPoU/403-seals-front-10-sheet.jpg), chỉ làm căn cứ nhận biết lỗi ma-nơ-canh. Mỗi prompt ghi đường dẫn đầy đủ của ảnh đó và [393-report.md §4](393-report.md#4-bộ-10-thủ-ấn-đề-xuất), chép cấu hình từng ngón cho các ô cần vẽ. Các lượt sau có thêm ảnh do chính phiếu này tạo làm căn cứ nhất quán; không dùng ảnh bên thứ ba. Hai mẫu nửa thân đầu đã hiển thị cho owner trước bảng cận.

Có hai điểm cần diễn giải theo bảng chi tiết: §4 quy định S2 không đan, S7 có khe 4–8 cm; cả bộ không chỉ định ngoại phược/nội phược. Vì vậy **không tự thay mười ấn bằng các ấn đan ngón mới**. S0 ở bụng dưới, S3 quanh rốn, tay phụ S5/S8 ở eo đúng §4, thay vì đưa tất cả lên ngực/mặt. S4 và S6 minh họa pha gồng; không trộn tay nắm và tay nhả trong cùng một ô. Tu sĩ là mẫu trung tính, áo đơn giản để đọc tay, không thiết kế nhân vật hoặc bộ hào quang mới.

## Các lượt sửa và kiểm tra

Thứ tự gọi: A1 → B1 → cận1 → A2 → B2 → cận2 → A3 → cận3. A là S0–S4, B là S5–S9. Sửa đầu cái S0 hướng gần nhau; S8 từ ngón gập kín sang gập nửa; làm rõ tay đỡ S9. S3 ban đầu bị công cụ mặc định thành tay trên úp/tay dưới ngửa; lượt cuối đổi rõ thành **tay phải trên ngửa, tay trái dưới úp**. Độ nghiêng được nhấn mạnh hơn chữ “hơi” trong §4 để nhìn ra hướng xoay cổ tay; khi dựng phải trả về độ nghiêng mềm theo bảng gốc.

Đã xem tám kết quả và ảnh ghép; kiểm đủ kích thước PNG, đủ tám prompt và ảnh ghép đọc được bằng ImageMagick. Không có tay bị cắt khỏi mép; các ô cận có hai tay, không có mặt/thân. Tên tiếng Anh và thứ tự đủ S0–S9.

Tự đánh giá nguồn, theo thứ tự **sức hút / đúng brief / dễ đọc / sạch hình** (thang 10; không phải chấm mù hoặc nghiệm thu game):

| Nhóm | try1 | try2 | try3 |
|---|---|---|---|
| A | 8,5 / 7,5 / 8,5 / 9 | 8,5 / 8 / 8,5 / 9 | 8,5 / 8,5 / 9 / 9 |
| B | 8,5 / 8 / 8,5 / 9 | 8,5 / 8,3 / 9 / 9 | — |
| Cận | 8,5 / 7,5 / 9 / 9 | 8,5 / 8 / 9 / 9 | 8,5 / 8,4 / 9 / 9 |

**Owner cần xem:** S3 đã nhấn mạnh độ xoay; S9 chỗ tay trái đỡ vẫn gần nếp cổ tay hơn giữa gót lòng tay, nhất là trên bảng nửa thân. Vài ngón gập bị ngón cái che theo góc nhìn chính diện; ảnh không xác định được mọi đốt ở mặt khuất. Dùng ảnh cùng §4 khi dựng, không lấy ảnh làm bằng chứng tiếp xúc hoặc giải phẫu tuyệt đối. Chưa có chấm mù, chưa tuyên bố đạt chuẩn chuyển động dùng chung 9 hoặc nghiệm thu trong bản chơi.

## Phần không thực hiện

Không sửa code, rig, animation, scripts/tests hoặc docs của Tu Tiên; không chạy build/test/game, không làm video/âm thanh, không đổi nhánh hoặc chạy các lệnh Git bị cấm. Không ghi thư mục review bên ngoài: phiếu chỉ cho phép thư mục concept và báo cáo này. Không sửa bảng 393 để hợp thức hóa hình. Không xóa/ghi đè ảnh có sẵn. Đã đủ sản phẩm yêu cầu; dừng ở trần tám lượt, không có tác vụ tạo ảnh đang chờ hạn mức.
