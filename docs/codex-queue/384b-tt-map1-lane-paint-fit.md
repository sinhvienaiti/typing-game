# Phiếu 384b · Tu Tiên · Map 1 một đường: vẽ lại bám sát vị trí greybox

Tranh mẫu 384 (`games/immortality-cultivation/art-src/concept/map1-lane.v1-try2.png`) đẹp và đúng chất (đường đá chữ S, nắng sớm, biển mây, cổng đá, tùng, hai Trận Trụ, Trận Tâm) nhưng **chưa khớp bố cục**: chồng 50 % lên greybox thì đường, trụ, cổng lệch vị trí thật; ảnh ra 1672×941 thay vì 1920×1080. Anh (15/11): cứ làm theo đề xuất; điều phối đề xuất vẽ lại một lần, ép bám greybox, giữ phong cách try2.

Lô: 1 ảnh
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-15/tu-tien/codex-images/map1-lane-try2.jpg

**Model `gpt-6.1-sol`, mức `high`. Dùng công cụ `image_gen` ở chế độ sửa ảnh, tối đa 4 lần.** `view_image` tối đa 8. Báo cáo `docs/codex-queue/384b-report.md` (Codex tự viết).

## Đường dẫn
`G = games/immortality-cultivation`. Chỉ thêm `G/art-src/concept/map1-lane.v2-try*.png` kèm `.prompt.txt` (ghi đường dẫn mọi ảnh tham chiếu), tấm ghép `G/art-src/concept/map1-lane-384b-sheet.jpg`. Giữ nguyên bản cũ. Cấm git ghi, sửa file có sẵn, mã.

## Cách làm
- **Đưa greybox vào làm ảnh gốc để sửa** (`G/tmp/shots/map1-wide/lane-B-final.png`, 1920×1080, camera chơi 42°): vẽ đè lên chính ảnh đó, giữ đúng vị trí đường, Trận Tâm, hai Trận Trụ, ô cơ quan, cổng, biên sân; chỉ thay bề mặt bằng chất liệu và ánh sáng.
- **Phong cách theo `G/art-src/concept/map1-lane.v1-try2.png`** (đưa làm ảnh tham chiếu thứ hai): đá cổ xám xanh, nắng sớm vàng nhạt, biển mây, tùng, cổng đá kiểu Việt.
- Ô đất tham chiếu: `G/art-src/ground/thanh-thach/lane-paving.v2.png`, `court-paving.v2.png`.
- Nếu ảnh ra không đúng 1920×1080: đổi cỡ về đúng khung (giữ tỉ lệ 16:9, không cắt mép có đồ vật) trước khi chồng đo.
Không chữ, không giao diện, không người; không dùng đỏ, cam, vàng kim, xanh ngọc mạnh trên môi trường.

## Kiểm và tự chấm
Chồng 50 % lên greybox. Toạ độ gốc đọc trên greybox bằng màu legend của nó (Trận Tâm khối trắng, Trận Trụ khối tím, đường đi dải be): ghi px tâm Trận Tâm, tâm hai Trận Trụ, và tâm dải đường ở ba hàng y = 300, 550, 800. Toạ độ trên tranh mới đọc ở cùng các vật đó (tâm đài Trận Tâm, tâm chân trụ, giữa mặt đường ở cùng ba hàng y). Mỗi điểm lệch ≤ 20 px ở 1920×1080; ghi bảng px gốc, px mới, độ lệch. Tấm ghép: greybox | tranh mới | chồng 50 % | try2 cũ. Tự chấm theo mặt yếu nhất (khớp vị trí, đẹp như try2, đọc rõ đường quái từ xa, không lấn quái); dưới 8 làm lại trong hạn lượt. Báo cáo ≤ 150 chữ, kèm bảng độ lệch.

Phản biện: PASS (Sonnet, 15/11; ghi rõ cách đo vị trí)
