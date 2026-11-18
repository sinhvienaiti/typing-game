# Phiếu 350 · Tu Tiên · Ảnh 2D: bộ bốn góc nhân vật chính, vòng 4 (thứ bậc mảng cho 66 px, vai mềm, tấm lưng gắn vào áo)

Vòng 3 (phiếu 347) được hai giám khảo mù chấm 8,0 và 7,5 (ngưỡng 8,5): nhất quán 8,6, hướng 9+, dựng mesh 8,5–8,7 **đều đạt**; còn thiếu ở **sức hút (8,1–8,2)** và **đọc ở 66 px (8,0–8,1)**. Hai giám khảo cùng nêu: (1) ở 66 px lưng và vai còn bận bởi mây, hạc nhỏ rải đều; cần gom thành ít mảng lớn: lưng là **một mảng chàm yên**, viền ngà hoặc vàng cũ **bản rộng rõ**, một phượng lớn ít nét; (2) **vai vuông cứng như tấm giáp**, tay quá ôm: cần vai mềm hơn, tay áo có vài nếp lớn có kiểm soát, lớp áo khoác chàm rủ dọc thân; (3) **tấm tròn ở lưng lấn át** và trông như vật lạ: thu nhỏ, nối rõ vào áo và đai (là tấm thêu may liền vào áo khoác, không phải đĩa đeo); (4) diadem và búi tóc phải cùng một cấu tạo ở mọi góc (vòng ôm đầu, đỉnh, hai tua). Chỉ vẽ ảnh, không sửa mã. **Giữ nguyên mặt, tóc, màu và kiểu C** (anh đã chọn); không quay về váy dài.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần gọi `image_gen`.** `view_image` tối đa 14. Báo cáo: `docs/codex-queue/350-report.md`.

## Đường dẫn
`H = games/immortality-cultivation/art-src/heroine`. Chỉ thêm `H/r4-*` và báo cáo. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
`H/r3-view-front.v1-try1.png` (chuẩn mặt, tóc, diadem, màu; giữ y), `H/r3-view-back.v1-try1.png`, `H/r3-view-left.v1-try1.png`, `H/r3-view-play.v1-try2.png`, `H/r3-turnaround.v1-try1.png` (vòng 3, sửa lỗi dưới).

## Sửa bắt buộc
1. **Thứ bậc mảng cho 66 px:** áo khoác ngoài chàm lạnh là **một mảng yên**, bỏ mây hạc nhỏ rải trên lưng và vai; viền ngà và vàng cũ **bản rộng** (≥ 3 % chiều cao người) chạy quanh mép khoác, mép tà và tấm cổ; hoa văn mây hạc chỉ còn ở **một dải gấu** và trên tấm cổ, nét to; **ấn phượng lưng** giữ đường kính 25 % chiều cao người nhưng là **thêu phẳng trên áo khoác**, ít nét chính, vàng cũ trên chàm, nhìn từ 66 px vẫn ra một đốm vàng tròn lớn trên lưng chàm.
2. **Vai mềm:** tấm cổ Nhật Bình vẫn vuông nhưng mỏng, mép mềm theo vai; tay áo trong trắng có **2–3 nếp lớn** ở bắp tay, ống bó từ khuỷu; không giống giáp.
3. **Tấm lưng** không còn là đĩa nhô: bỏ lót dày; ấn thêu liền vào áo khoác; tấm cổ và đai là chỗ "gắn" tự nhiên.
4. **Diadem và búi tóc** một cấu tạo: vòng ôm đầu thanh, đỉnh ngọc trắng, hai tua dài treo hai bên; cùng hình và vị trí ở 4 góc.
5. Giữ mọi thứ khác của vòng 3: áo khoác xẻ hông và xẻ sau, quần suông, ủng có gót, ngọc bội trái, hai đuôi lưng, kiếm thấp ở xương cùng chuôi phải nghiêng 10° có đai treo, A-pose, nền `#00FF00`, lề ≥ 8 %, đèn trên phải 45°, không bóng, không hào quang, không chữ. Màu 60 ngà, 30 chàm lạnh, 10 vàng cũ; đầu, vai, thân trên sáng; quần tối.

## Bộ ảnh (cùng khổ 3:4 ảnh đơn, cùng chiều cao người chênh ≤ 3 %)
`H/r4-turnaround.v1-try1.png` (16:9), `H/r4-view-front.v1-try1.png`, `H/r4-view-back.v1-try1.png`, `H/r4-view-left.v1-try1.png`, `H/r4-view-play.v1-try1.png` (camera 55° nhìn xuống từ sau chếch 30°, dáng sẵn sàng, hai tay thấy). Mỗi prompt liệt kê 12 chi tiết nhận dạng và "same face, hair and diadem as the reference front view".

## Kiểm
Nền, lề, chênh chiều cao; bảng nhất quán 12 chi tiết × 4 góc; **ô 66 px của sau và góc chơi, phóng 4×**: tự ghi số mảng đọc được (mục tiêu: tóc đen, vai ngà, lưng chàm, đốm phượng vàng, quần tối, kiếm ngang = 6 mảng); tấm so mặt với `r3-view-front` (phải giống). Tự chấm theo mặt yếu nhất; dưới 8 vẽ lại ảnh yếu nhất, tối đa 3 lần.

## Xong khi
5 ảnh + prompt + `H/r4-350-sheet.jpg` + báo cáo có bảng.
