# Phiếu 398 — Ảnh tham chiếu tuyệt kỹ Hư Không, Huyết, Tinh Tú

Ngày 16/11/2026. Đã dùng **12/12 lần image_gen**, bốn lần mỗi hệ, tạo **12 PNG 1536×1024**, ba ảnh ghép và lưu prompt thật cạnh từng ảnh. Giữ nguyên PNG công cụ trả về. Đây là các phương án để owner/Claude chọn, chưa phải nghiệm thu hiệu ứng trong game.

## File giao nộp

| Hệ | Thư mục nguồn | Ảnh ghép |
| --- | --- | --- |
| Hư Không | `games/immortality-cultivation/art-src/concept/ult-void/` | [ult-void-sheet-398.jpg](../../games/immortality-cultivation/art-src/concept/ult-void/ult-void-sheet-398.jpg) |
| Huyết | `games/immortality-cultivation/art-src/concept/ult-blood/` | [ult-blood-sheet-398.jpg](../../games/immortality-cultivation/art-src/concept/ult-blood/ult-blood-sheet-398.jpg) |
| Tinh Tú | `games/immortality-cultivation/art-src/concept/ult-star/` | [ult-star-sheet-398.jpg](../../games/immortality-cultivation/art-src/concept/ult-star/ult-star-sheet-398.jpg) |

Trong mỗi thư mục, thay `<hệ>` bằng `void`, `blood` hoặc `star`, có đủ bốn ảnh:

- `ult-<hệ>-moment-a.v1-try1.png`: phương án khoảnh khắc A.
- `ult-<hệ>-moment-b.v1-try1.png`: phương án khoảnh khắc B.
- `ult-<hệ>-components.v1-try1.png`: bảng thành phần ban đầu, giữ lại để xem chi tiết lớn.
- `ult-<hệ>-components.v1-try2.png`: bảng thành phần đã thu gọn, tăng lề; Tinh Tú chuyển sang vàng trắng.

Mỗi PNG có `.prompt.txt` cùng tên gốc, ghi nguyên văn prompt đã gửi, đường dẫn và vai trò từng ảnh đầu vào. Mỗi ảnh ghép **1576×1114** có `ult-<hệ>-sheet-398.prompt.txt` ghi đúng lệnh ImageMagick, không phải prompt AI. Trong ảnh ghép: A/B ở hàng trên, components try1/try2 ở hàng dưới. Chỉ ảnh ghép có nhãn tên file; các PNG nguồn không có chữ hoặc watermark quan sát được.

## Tham chiếu và cách làm

Đã mở xem và truyền đủ ba ảnh bắt buộc vào **mọi lần tạo**:

- Bố cục, camera, nền đá và mật độ: `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png`.
- Chất liệu và ánh sáng: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-void.jpg`, `ult__ult-blood.jpg`, `ult__ult-star.jpg`, đúng hệ tương ứng. Prompt yêu cầu bỏ toàn bộ sinh vật và cảnh của ảnh audit.
- Atlas cùng hệ, dưới `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/vfx/`: `void/void-ground-impact.atlas.png`, `blood/blood-caster-seal.atlas.png`, `star/star-comet.atlas.png`.

Không thiếu tham chiếu nào; không dùng ảnh bên thứ ba. Mỗi lượt components try2 nhận thêm chính ảnh components try1 cùng hệ làm mục tiêu chỉnh sửa. Prompt ghi cả đường dẫn này. Hai mẫu khoảnh khắc Hư Không đã hiển thị trước khi tiếp tục các bảng thành phần; mọi ảnh sau cũng hiển thị ngay khi công cụ trả về.

Thực hiện đúng phiếu đã có phản biện PASS, không mở thêm thiết kế chiêu hoặc nghiên cứu ngoài. Khoảnh khắc chỉ là tranh tham chiếu bố cục theo yêu cầu, không phải ảnh đóng sẵn toàn bộ hiệu ứng để đưa vào runtime. Bảng thành phần là nguồn hướng hình cho các phần có thể tách, đặt, xoay và nhân bản khi dựng sau.

## Gợi ý cho owner/Claude

**Hư Không: ưu tiên moment-b và components try2.** B giữ tâm hút rõ, nhiều khoảng đá tối hơn A; có khe nứt tím đen, mảnh kính lơ lửng và luồng hạt hướng tâm. Tâm trong cả A/B đọc thành xoáy rách không gian nằm thấp, chưa phải một khe dựng đứng rõ như thành phần hàng trên. Owner cần chọn có giữ hướng xoáy này hay dùng khe đứng từ bảng thành phần khi dựng.

**Huyết: ưu tiên moment-b và components try2.** B có tâm hoa văn thấp, bớt khối tinh thể lớn so với A; gai huyết tinh và sương đỏ tách được trên đá tối. Cả A/B đều diễn giải nút hoa văn ở tâm thành hình hoa nhiều cánh; không thấy sinh vật, người hoặc bộ phận cơ thể. Owner cần xem mô típ hoa này có hợp tuyệt kỹ Huyết hay cần đổi hướng ở bước tiếp theo.

**Tinh Tú: ưu tiên moment-b và components try2.** B chuyển rõ sang vàng trắng: mạng chòm sao nối tia trên mặt đất, sao băng nhỏ và bụi sao. A và components try1 còn nhiều tím từ tham chiếu, giữ để so sánh, không phải gợi ý màu chính.

Trong cả ba bảng, thứ tự bốn cột × hai hàng: hàng trên là bốn biến thể hình chính nhìn ngang; hàng dưới là mảnh/hạt rời, luồng hạt hoặc sương/bụi, mặt đất nhìn trên, vòng trói nhìn trên. Vòng là decal phẳng, tâm rỗng, không có cấu trúc bọc thân. Bốn hình chính tương ứng là khe nứt, gai huyết tinh và sao băng.

Đây là gợi ý của Codex; owner/Claude quyết định. Không tự chấm điểm 8,5 hoặc đánh dấu nghiệm thu.

## Kiểm tra và phần chưa đạt

Đã kiểm đủ 12 PNG đúng **1536×1024**, có prompt tương ứng; đã xem từng kết quả và cả ba ảnh ghép. PNG nguồn không bị cắt, đổi kích thước, tô lại hoặc xử lý nền. ImageMagick chỉ đọc kích thước/pixel và ghép bản xem.

Đo từng ô **384×512** ở components try2, lấy hộp bao pixel có ít nhất một kênh RGB **>8/255**, bỏ nhiễu cực tối. Lề nhỏ nhất của từng ô 1–8:

| Hệ | Lề nhỏ nhất của ô 1–8 (%) |
| --- | --- |
| Hư Không | 25,00; 25,20; 25,20; 22,92; 20,05; 23,63; 21,09; 17,19 |
| Huyết | 21,88; 25,00; 25,39; 20,31; 22,66; 26,95; 23,18; 17,97 |
| Tinh Tú | 18,75; 22,40; 24,22; 18,23; 24,22; 22,92; 23,70; 21,09 |

Cả 24 ô try2 vượt 8% theo ngưỡng này. Try1 có một số đầu hình, đuôi, sương hoặc vòng dưới 8%, nên không gợi ý làm bản đủ lề. Halo và nhiễu ≤8/255 không nằm trong phép đo hộp bao.

**Nền đen tuyệt đối chưa đạt.** Dù try2 yêu cầu lại RGB(0,0,0), dải lề 8% từng ô vẫn có pixel gần đen với kênh lớn nhất **1/255**: Hư Không 10,85–13,20% pixel trong dải; Huyết 9,15–10,68%; Tinh Tú 9,50–11,49%. Giữ nguyên nguồn và ghi rõ thiếu sót, không coi yêu cầu đen tuyệt đối đã hoàn tất. Đã dùng hết 12 lượt phiếu cho phép, không tạo lượt thứ 13.

**Mặt đất lặp theo cụm rời.** Ô 7 try2, vùng `x=768..1151, y=512..1023`, có mô típ tắt trước biên. Sai khác RGB trung bình trái–phải / trên–dưới, theo thang 0–255: Hư Không **0,1263 / 0,0998**; Huyết **0,1139 / 0,0512**; Tinh Tú **0,1159 / 0,1328**. Sai khác lớn nhất đều **1/255**, do nhiễu gần đen. Có thể bố trí như các mảng decal lặp rời; chưa phải mạng khe/hoa văn/chòm sao nối liên tục xuyên mép, và chưa có xác nhận seamless trong engine. Chưa xuất texture cắt riêng.

Camera 50°/55° và sân 30 m là chỉ dẫn trong prompt, chưa xác nhận bằng đo hình học. Một số vành và chi tiết ngoài của khoảnh khắc vẫn sát mép ngang, chưa giữ trọn dải đá rộng quanh toàn bộ hiệu ứng. Không thấy sinh vật, kiến trúc, bầu trời hoặc phong cảnh vẽ sẵn trong 12 kết quả đã xem.

## Phạm vi và phần bỏ qua

Chỉ ghi ảnh, prompt, ảnh ghép trong ba thư mục concept được giao và báo cáo này. Không sửa code, scripts, tests hoặc docs Tu Tiên; không tạo video/âm thanh, chạy build/bộ test game, đổi nhánh, stage, commit, push, xóa hoặc ghi đè ảnh có sẵn. Không ghi sang thư mục review hoặc sửa chỉ mục vì ngoài phạm vi phiếu.

Không bỏ hệ hoặc loại ảnh nào. Phần còn thiếu kỹ thuật là nền đen tuyệt đối, tính lặp được xác nhận trong engine và đo camera/quy mô; không dựng lab hoặc tích hợp vì ngoài phiếu. Không có lỗi HTTP 429 hay thời gian chờ từ công cụ. Owner cần xem ba ảnh ghép, chọn A/B và hình chính, đặc biệt tâm xoáy Hư Không và mô típ hoa Huyết, trước khi làm nguồn dựng tiếp.
