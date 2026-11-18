# Phiếu 377 · Tu Tiên · Map 1 rộng (D66): tranh ý tưởng vẽ đè greybox

> **TẠM DỪNG (13/11 09:5x):** anh đổi sang map một đường; không chạy phiếu này tới khi anh duyệt bản mới (`MAP1_WIDE.md` mục "Một đường").
>
> **Trạng thái cũ:** anh chọn B và đã xem greybox (13/11 09:4x). Điều phối chạy phản biện rồi chạy qua `tools/codex-run/run.sh`; là phiếu ảnh nên chạy được cả khi quota Codex < 15 %.

Lô: có — 3 ảnh (home, nw, overview), làm 2 mẫu trước rồi dừng chờ anh duyệt.
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-13/tu-tien/map1-wide/overview-B.png

Map 1 đổi theo D66: sân rộng 3 × 2 khung, camera giữ 55°/28°/52,8 m, rê chuột mép để xem xa. Đọc `docs/games/tu-tien/MAP1_WIDE.md` (bố cục §3, luật §1), `docs/games/tu-tien/MAP1_CONCEPT.md` §3–6 (ánh sáng, màu tín hiệu, chất liệu, sự sống — vẫn giữ), skill `game-map-concept`.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 9 lần `image_gen`**, `view_image` tối đa 14. Báo cáo `docs/codex-queue/377-report.md`.

## Đường dẫn
`G = games/immortality-cultivation`. Chỉ thêm `G/art-src/concept/map1-wide-{overview,home,nw}.v1-try*.png` kèm `.prompt.txt` (ghi đường dẫn ảnh tham chiếu trong mỗi prompt), tấm ghép `G/art-src/concept/map1-wide-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`, bắt buộc, không vẽ chỉ từ chữ)
- Greybox mới (nền bố cục, giữ đúng vị trí): `G/tmp/shots/map1-wide/overview-B.png` (nhìn từ trên, lưới 10 m, legend), `G/tmp/shots/map1-wide/incam-home.png`, `G/tmp/shots/map1-wide/incam-nw.png` (đúng camera chơi 1920 × 1080).
- Phong cách đã có: `G/art-src/concept/map1-camera.v1-try7.png` (tranh một khung, sương sớm — chất liệu, màu, độ chi tiết), `G/art-src/identity/thanh-thach-ai-55.png`.
- Không dùng ảnh bên thứ ba.

## Việc (thứ tự)
1. **Hai mẫu trước** (ít nhất 2 lần sinh): `home` (vẽ đè `incam-home.png`) và `nw` (vẽ đè `incam-nw.png`). Dừng, ghép tấm `map1-wide-sheet.jpg` (greybox | tranh | chồng 50 %), báo cáo; điều phối gửi anh xem. Chỉ làm bước 2 khi anh OK.
2. `overview` (vẽ đè `overview-B.png`, nhìn thẳng từ trên, bỏ chữ legend): bản đồ vẽ cả sân 140 × 66 m để dựng ô đất, decal và mốc.

## Nội dung tranh
- Giữ nguyên phối cảnh, hành lang (rộng 6 m, đá lát mòn sáng hơn xung quanh ≥ 1,3×), vị trí Trận Tâm, Trận Trụ, 6 ô, ải trong, cổng ngoài, Thiên Đàn, Vọng lâu, Thác Đông, tường bắc theo legend; lệch ≤ 20 px ở 1080p.
- Mỗi khung **một mốc nhấn**: khung nhà = Trận Tâm; khung tây bắc = Cổng ngoài A. Thiên Đàn: đài tế cổ nhiều tầng, vành chữ triện cổ khắc phát sáng nhẹ, bát quái/cánh sen (D64), không chữ Hán thật.
- Hấp dẫn và sang: lớp khối, chất liệu thật (đá vôi xanh xám có vân và rêu, ngói âm dương chàm, gỗ lim, ngọc trắng ngà), ánh nắng sớm đông bắc, sương chàm; viền vực và biển mây ở góc khung khi sát biên. Không để mảng đất trống một màu.
- Màu tín hiệu (`#FF4A4A`, `#FFB020`, `#FFC83A`, `#7FF5E0`) không dùng mạnh trong môi trường. Không vật nào che hành lang. Dải dưới y ≥ 930 (Bàn Quyết) vẽ đơn giản, tối.
- Không người, không quái, không chữ, không UI.

## Tự chấm (trong báo cáo)
Bảng: Camera khớp · Đọc đường · Hùng vĩ/hấp dẫn · Tiên hiệp Việt · Không che đường · Yếu nhất. Ghi các chỗ lệch so với legend bằng px.

## Kiểm tra của Claude sau khi nhận
Chồng 50 % lên greybox, đo lệch các mốc; anh xem; hai giám khảo mù ≥ 8,5 mới coi là chấp nhận.
