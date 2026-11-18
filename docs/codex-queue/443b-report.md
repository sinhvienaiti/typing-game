# Phiếu 443b — Trận pháp trên trời một lớp

Ngày 17/11/2026. Đã làm đủ ba mẫu và tờ so sánh trong lab; chờ owner chọn. Mặc định vẫn tải `formation-topdown`.

## Sản phẩm

- Tờ ghép: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/sky-formation-443b.jpg`. Ba hàng A/B/C; mỗi hàng có ảnh nhìn thẳng và bốn khung Alt+1/Alt+2 ở 0,8/1,4 giây. Đã thêm đúng một dòng vào `ABOUT.md` cùng thư mục.
- Ảnh và prompt chính xác: `games/immortality-cultivation/art-src/concept/ult-metal/sky-formation/sky-formation-simple-a.v1-try1.png`, `sky-formation-simple-b.v1-try1.png`, `sky-formation-simple-c.v1-try1.png`, mỗi ảnh có `.prompt.txt` cùng tên.
- Atlas: `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/formation-simple-a.atlas.png`, `formation-simple-b.atlas.png`, `formation-simple-c.atlas.png`, mỗi atlas có `.json` tương ứng, định dạng 1 cột × 1 hàng, 1 khung, fps 1 như atlas cũ.
- Mã lab: `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`; kịch bản chụp và đo: `games/.wt-ic-lab-all/src/lab/metal-ult-formation-review.mjs`.
- Số đo: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/sky-formation-443b/measure.json`; có `ABOUT.md` và nhật ký dọn ảnh trong cùng thư mục.

## Ảnh và cách dựng

Dùng 3/6 lượt `image_gen`, mỗi mẫu một lượt: A kiếm hướng tâm, B bát quái, C sen. Cả ba dùng duy nhất ảnh tham chiếu repo `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-topdown.v1-try1.png`. Hai mẫu A/B đã được hiển thị trước khi làm mẫu C. Không dùng ảnh bên thứ ba; không ghi đè sáu ảnh của phiếu 443.

Công cụ trả ảnh 1254²; ImageMagick thu gọn vùng tranh, đặt giữa khung đen 1024². Vùng sáng ở ngưỡng 1%: A 900×891, B 900×900, C 900×889; lề nhỏ nhất 62 px, tương đương 6,05%. Giữ màu và hoạ tiết gốc, chỉ chuẩn hoá kích thước/lề.

Theo `VFX_STANDARD`, đây là thành phần trận trong chiêu ultimate hiện có. Thành phần còn thiếu là ba mặt trận một lớp; tia rủ, kiếm, tác động, dư âm và âm thanh dùng lại thư viện hiện có. Công cụ tạo hình là `image_gen` theo phiếu; mã chỉ đặt, xoay UV, hiện chữ, điều biến sáng và làm mờ ảnh có sẵn.

`?formation=a|b|c` thay ảnh trên đúng một mesh XZ nằm ngang, cao 8 m, đường kính mặt phẳng 18 m. Vành xoay 0,10 rad/s, tâm đứng yên; chữ hiện theo góc trong 0,4 giây đầu và sáng theo nhịp. Mặt dưới dùng chính ảnh trận lấy mẫu mờ, không thêm mặt trận chồng tầng. Vệt sáng đất lấy tâm flare ô 9 của `metal-ult.atlas.png`, làm mờ và che mép mềm thành vùng sáng đặc, không dùng vòng. Giữ 20 tia rủ, đặt chân tia trong vành tranh. Fragment giới hạn mỗi kênh ở 0,9. Trận tan ở 1,9–2,45 giây để kiếm lớn giữ điểm nhấn ở cao trào 2,4 giây.

Neo cuối cố định giữa hai góc: x −0,3933 / y 8 / z −10,5423 m, phía sau tâm nhóm mục tiêu trong cảnh chuẩn. Góc chơi được hướng sâu thêm vào cụm trận. Góc sau lưng giữ vị trí máy ở tầm mắt, ngước nhẹ về trời và mở FOV 66°; thay đổi chỉ áp dụng khi chọn một mẫu mới, có chuyển vào/ra. Không nghiêng mặt phẳng về camera.

## Kiểm chứng

| Hạng mục | Kết quả |
| --- | --- |
| TypeScript strict cho rain, layered, skills-main và khai báo stress | 0 lỗi |
| Cảnh chuẩn | 1280×720, DPR 1, nền `#353a40`, 100 quái |
| A — p95 CPU + chờ GPU | 6,20 ms — đạt |
| B — p95 CPU + chờ GPU | 6,30 ms — đạt |
| C — p95 CPU + chờ GPU | 6,50 ms — đạt |
| GPU | ANGLE Metal, Apple M4; không dùng GPU phần mềm |
| Mẫu đo mỗi phương án | 208 khung hoạt động, sau một lượt làm nóng |
| Phần tranh ở Alt+1 | Rộng 39,21% khung; mép trên 169,04 px |
| Phần tranh ở Alt+2 | Rộng 34,63% khung; mép trên 219,96 px |
| Toàn mặt phẳng ở Alt+1 | Rộng 44,75% khung; mép trên 149,86 px |
| Trận và tia rủ | Trong khung ở cả 12 ảnh; cùng một neo thế giới |
| Kết thúc chiêu | Trả đủ 49 vị trí kiếm; chiêu ngừng hoạt động |
| Tài nguyên riêng của chiêu / ngoại lệ JS | Nạp đủ / 0 ngoại lệ |

Đo cùng phương pháp phiếu 433d: `__lab.perf(1)`, CPU và chờ `readPixels`, lấy p95 khi clock từ 0,6 tới dưới 4 giây. Kịch bản có cổng chặn p95 >16,7 ms, sai texture, sai kích thước hoặc ảnh vượt mép. Phần tranh tính theo đĩa 900/1024 của nguồn, tách khỏi mép đen của mặt phẳng.

Đã kiểm riêng nhánh không có tham số: nạp `formation-topdown.atlas.png`, đường kính cũ 12 m, không vẽ vệt sáng đất mới. Lab còn cảnh báo chung `KTX2Loader` và hai flipbook cũ `metal-crescent-sym`/`metal-slash-arc`; chúng cũng xuất hiện ở lượt kiểm mặc định, nằm ngoài phạm vi phiếu.

Xem trực tiếp góc chơi: `http://127.0.0.1:3148/stress.html?formation=a&ground=%23353a40`; đổi `a` thành `b` hoặc `c`, chọn chiêu Kim. Góc sau lưng dùng thêm `&ultCam=0` rồi Alt+2 để tránh camera đẩy vào của chiêu giữ góc chơi.

## Dọn và phần giữ lại

Đã chạy `capture-prune` ở chế độ xem danh sách rồi `--apply`: xoá 66 ảnh của riêng phiếu, khoảng 55,226 MB; không còn PNG thô trong thư mục capture. Đã đóng Chrome headless và xoá profile tạm bằng driver; giữ nguyên server localhost:3148. Không commit, không chạy build hoặc bộ test game, không sửa nguồn game chính hay tài liệu Tu Tiên.

Không dùng ba lượt tạo ảnh còn lại vì ba nguồn đầu đủ hình và đúng vai trò để so trong camera. Không thay mặc định, không chuyển sang game chính và không tuyên bố nghiệm thu mỹ thuật 8,5: owner cần xem tờ ghép và chọn A/B/C. Chỉ mục review tổng không ghi lại vì nằm ngoài danh sách đường dẫn được ghi của phiếu.
