# Phiếu 378 · Tu Tiên · Linh kiện: dòng cột sấm sét chảy thẳng (thay cột bện xoắn), 3 biến thể

Anh (13/11 10:1x): "phải thiết kế thêm 1 luồng cột sấm sét để dùng cho cột lôi, chứ hiện tại cột lôi của chúng ta khi toả ra nhìn như lốc xoáy hơn". Ba cột 367 là sợi bện xoắn quanh trục nên khi nhân 5 × 8 đọc thành lốc xoáy. Cần **một dòng sét đổ thẳng**: sét chảy từ mây xuống đất liên tục theo một trục thẳng, không xoắn.
Giữ luật anh 07/11 (`docs/work/tasks/five-thunder-lab.md`, mục "Anh nói gì"): cột chỉ là sét, không vỏ trụ, không ống sáng trơn.

Lô: 6 ảnh (3 cột + 3 lõi)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-13/tu-tien/codex-images/column-videos-sheet.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/378-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-stream-{a,b,c}.v1-try*.png`, `S/thunder-stream-{a,b,c}-core.v1-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `S/thunder-stream-378-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
`S/thunder-column-a.v1-try1.png` (khổ, chân, mây, bộ màu: giữ; **bỏ kiểu bện xoắn**), `S/thunder-single-bolt-a.v4-try9.png` (nét sét bạch kim đã duyệt), `S/thunder-five-cloud-ink.v4-try2.png` (mây mực). Bộ màu D65 trong `docs/games/tu-tien/00-canon.md`.

## Ba biến thể, khổ dọc 1024×1536, nền đen thuần, nhìn ngang hơi từ trên (30°)
- **Thân:** một **lõi sét thẳng đứng** sáng nhất ở giữa, quanh nó 4–8 tia sét **chạy song song từ trên xuống**, mỗi tia gấp khúc nhỏ kiểu sét thật (zigzag nhỏ, không uốn lượn sóng), **không quấn quanh nhau**; từ thân toả **nhánh điện ngang ngắn** ra hai bên ở nhiều độ cao như rễ cây nằm ngang; khe tối giữa các tia.
- **Cảm giác:** một thác sét đổ thẳng xuống, nặng và giận dữ; đọc là "cột sét", không phải lốc xoáy, không phải ống.
- **Chân:** vụ chạm đất, điện lan sát đất toả ngang, đá vụn bắn thấp; chân trên một hàng pixel.
- **Ngọn:** cắm vào một mảng mây mực nhỏ ở mép trên (lề ≥ 6 %), mây **nhỏ và gọn** (không phình).
- **Khác nhau:** a = lõi dày, ít tia; b = nhiều tia mảnh, thân rộng; c = hai lõi song song sát nhau.
- **Ảnh `-core`:** sửa từ chính ảnh đã chọn, chỉ giữ các lõi trắng mảnh trên nền đen, chồng khít.
Bạch kim D65 (trắng ngà, vàng nhạt); không xanh, tím, cam đậm. Không chữ.

## Kiểm và tự chấm
Script: lề, chân trên một hàng pixel (lệch ≤ 2 % chiều cao), core chồng khít, trắng thuần (> 245) ≤ 6 %. Tấm ghép: ba cột mới cạnh một cột 367 cũ, và bản thu cao 120 px; thêm một ô ghép thử 5 cột mới cạnh nhau như một chùm. Tự chấm theo mặt yếu nhất (đọc là cột sét đổ thẳng, không ra lốc xoáy, không ra ống; ba biến thể khác rõ); dưới 8 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 13/11)
