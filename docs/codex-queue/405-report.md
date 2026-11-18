# Phiếu 405 — Ảnh tham chiếu ba tuyệt kỹ Quang, Độc, Phong

Ngày 16/11/2026. Đã dùng **12/12 lần image_gen**, mỗi hệ 4 lần, tạo **12 PNG 1536×1024**, **12 prompt nguyên văn** và **3 ảnh ghép**. Giữ nguyên PNG công cụ trả về, không ghi đè ảnh có sẵn. Đây là bộ phương án để owner/Claude chọn, chưa phải nghiệm thu hiệu ứng trong game.

## File giao nộp

Mỗi thư mục dưới đây có bốn PNG, mỗi PNG có prompt cùng tên, đổi đuôi thành `.prompt.txt`:

| Hệ | Thư mục | Ảnh ghép |
| --- | --- | --- |
| Quang | `games/immortality-cultivation/art-src/concept/ult-light/` | [ult-light-sheet-405.jpg](../../games/immortality-cultivation/art-src/concept/ult-light/ult-light-sheet-405.jpg) |
| Độc | `games/immortality-cultivation/art-src/concept/ult-poison/` | [ult-poison-sheet-405.jpg](../../games/immortality-cultivation/art-src/concept/ult-poison/ult-poison-sheet-405.jpg) |
| Phong | `games/immortality-cultivation/art-src/concept/ult-wind/` | [ult-wind-sheet-405.jpg](../../games/immortality-cultivation/art-src/concept/ult-wind/ult-wind-sheet-405.jpg) |

Tên bốn PNG trong mỗi thư mục, thay `<hệ>` bằng `light`, `poison`, `wind`:

- `ult-<hệ>-moment-a.v1-try1.png`: khoảnh khắc A.
- `ult-<hệ>-moment-b.v1-try1.png`: khoảnh khắc B.
- `ult-<hệ>-components.v1-try1.png`: bảng thành phần đầu.
- `ult-<hệ>-components.v1-try2.png`: bảng thành phần đã thu nhỏ để tăng lề.

Ba ảnh ghép đều **1576×1112**: A ở trên trái, B ở trên phải, bảng try1 dưới trái, bảng try2 dưới phải. Chỉ ảnh ghép có nhãn tên file. Mỗi ảnh ghép có `.prompt.txt` ghi lệnh ImageMagick thực tế; đây là ghép cơ học, không tính thêm lượt AI.

Thứ tự gọi công cụ: Quang A → Quang thành phần 1 → Quang B → Độc A → Độc thành phần 1 → Độc B → Độc thành phần 2 → Phong A → Phong thành phần 1 → Phong thành phần 2 → Quang thành phần 2 → Phong B.

## Tham chiếu

Đã mở xem và truyền ảnh thật vào **mọi lần tạo**, không chỉ ghi tên trong prompt:

- Bố cục chung: `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png`.
- Clip Quang: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-light.jpg`.
- Clip Độc: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-poison.jpg`.
- Clip Phong: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-wind-firmament.jpg`.
- Atlas Quang: `games/immortality-cultivation/art-src/lab/vfx/light/light-column-loop-w2.atlas.png`.
- Atlas Độc: `games/immortality-cultivation/art-src/lab/vfx/poison/poison-vortex-loop.atlas.png`.
- Atlas Phong: `games/immortality-cultivation/art-src/lab/vfx/wind/wind-vortex-loop.atlas.png`.

Không thiếu tham chiếu nào. Từng prompt ghi đường dẫn tuyệt đối và vai trò: ảnh Băng cho bố cục/camera/mật độ; ảnh clip chỉ cho chất liệu và ánh sáng; atlas cùng hệ cho vật liệu thành phần. Ba lượt chỉnh bảng try2 nhận thêm bảng try1 tương ứng làm ảnh mục tiêu. Không dùng ảnh bên thứ ba. Hai mẫu Quang đã được xem và hiển thị cho owner trước các mẫu tiếp theo.

Dùng image_gen đúng phiếu đã có phản biện PASS của Sonnet. Khoảnh khắc toàn sân là tranh tham chiếu bố cục theo yêu cầu phiếu, không phải nguồn dùng thay cả chiêu khi dựng. Bảng thành phần dành cho các phần nhỏ có thể tái sử dụng.

## Gợi ý để owner/Claude chọn

**Quang: ưu tiên B và bảng thành phần try2.** B giữ trọn cột vàng trắng và các vòng trong khung, có một tâm sáng, nền đá tối đọc rõ giữa các lớp phù văn trừu tượng và tia mảnh. A rực hơn nhưng cột chính bị cắt ở mép trên. Bảng try1 giữ chi tiết lớn hơn; try2 có lề rộng hơn.

**Độc: ưu tiên B và bảng thành phần try2.** B dùng tâm vũng độc sủi bọt với sương thấp, xanh lục và tím phân lớp. A có dáng đài hoa ở tâm do ảnh clip kéo hình; không đề nghị dùng A làm mẫu dựng chính. Try1 có nhiều ô thiếu lề; try2 đã thu nhỏ và đặt lại từng cụm.

**Phong: ưu tiên B và bảng thành phần try2.** B giữ toàn bộ lốc và vòng sân, có lá cùng đường bụi xám nâu cuốn tròn giữa các dòng gió xanh ngọc. A dày, rực hơn nhưng vành gió sát mép ngang. B nhẹ hơn về mật độ, owner cần cân nhắc sức nặng cao trào khi chọn.

Cả ba bảng dùng lưới vô hình **4 cột × 2 hàng**. Bốn ô trên là bốn biến thể hình chính nhìn ngang; hàng dưới lần lượt là mảnh/lá/gai nhỏ, hạt/bụi/bọt, mặt đất nhìn trên, vòng trói phẳng nhìn trên. Vòng có tâm rỗng, không kèm chân/người và không bọc thân. Không thấy sinh vật, người, chữ hoặc watermark trong PNG; nền khoảnh khắc chỉ có đá lát và hiệu ứng, riêng Độc A có hình gợi hoa đã nêu trên.

Các gợi ý này không thay quyết định của owner/Claude, không tự chấm điểm 8,5 hoặc đánh dấu nghiệm thu.

## Kiểm tra và hạn chế

Đã kiểm đủ 12 PNG đúng 1536×1024, đủ prompt cạnh ảnh và đủ đường dẫn tham chiếu trong mỗi prompt. Đã xem ảnh công cụ và mở kiểm cả ba ảnh ghép. ImageMagick chỉ dùng để đọc kích thước/pixel và ghép ảnh, không tô lại, cắt hoặc chuẩn hóa PNG nguồn.

Đo hộp bao từng ô try2 theo pixel có kênh RGB lớn hơn **8/255** để bỏ nhiễu tối. Lề nhỏ nhất của ô 1–8:

| Hệ | Lề nhỏ nhất từng ô (%) |
| --- | --- |
| Quang | 21,68; 21,29; 21,68; 21,29; 24,80; 25,59; 25,98; 23,18 |
| Độc | 17,45; 26,82; 26,30; 16,67; 23,18; 26,82; 25,78; 23,18 |
| Phong | 26,30; 29,69; 28,39; 22,40; 29,69; 28,91; 26,56; 28,91 |

Tất cả ô try2 vượt 8% theo ngưỡng này; phép đo không tính halo hoặc nhiễu cực tối ≤8/255.

**Nền đen tuyệt đối chưa đạt.** Dù prompt chỉnh đã yêu cầu RGB(0,0,0), trong dải lề 8% của các ô try2 vẫn có pixel mức 1/255: Quang khoảng 9,78–11,13%, Độc 9,97–11,39%, Phong 9,56–11,68%. Kênh lớn nhất trong các dải này đều bằng 1/255. Giữ nguyên ảnh nguồn và ghi rõ phần chưa đạt, không gọi nền gần đen là đen tuyệt đối.

**Tile mặt đất là decal các cụm rời lặp trên nền đen**, không phải chất liệu liên tục xuyên cạnh. Đối chiếu nguyên ô 7 try2, vùng `x=768..1151, y=512..1023`, sai khác RGB trung bình giữa mép đối diện (đơn vị /255):

| Hệ | Trái–phải | Trên–dưới | Sai khác lớn nhất |
| --- | --- | --- | --- |
| Quang | 0,1087 | 0,1207 | 1/255 |
| Độc | 0,1191 | 0,0868 | 1/255 |
| Phong | 0,1074 | 0,0911 | 1/255 |

Hình tắt trước biên nên có thể bố trí lặp từng cụm; nhiễu nền khiến mép chưa trùng pixel tuyệt đối. Chưa xuất texture riêng, chưa kiểm nhịp lặp trong engine. Góc nhìn 50–55° và sân 30 m là chỉ dẫn cho công cụ; tranh chưa xác nhận được kích thước/góc bằng đo hình học.

## Phạm vi và phần bỏ qua

Chỉ tạo ảnh, prompt, ảnh ghép trong ba thư mục concept được phép và báo cáo này. Không sửa code, script, test, tài liệu Tu Tiên, atlas hoặc ảnh tham chiếu; không tạo video, không chạy build/test game, không đổi nhánh và không thực hiện commit/push/reset/clean/stash. Không tạo capture mới hoặc sửa thư mục review ngoài phạm vi phiếu.

Không tạo thêm sau 12 lượt theo mức trần của phiếu. Không có lỗi giới hạn dịch vụ hoặc yêu cầu chờ giờ. Chưa dựng chiêu, chưa tách nguồn thành phần, chưa chấm mù trong play host vì phiếu chỉ giao ảnh tham chiếu. Owner/Claude cần chọn phương án và quyết định bước xử lý nền/tile trước khi dùng làm nguồn dựng.

