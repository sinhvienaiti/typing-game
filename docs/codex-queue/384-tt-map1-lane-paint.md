# Phiếu 384 · Tu Tiên · Map 1 một đường (camera B 42°): tranh ý tưởng vẽ đè greybox

> **Trạng thái:** map một đường, camera B chốt 15/11 theo đề xuất (anh xem sau). Điều phối chạy phản biện rồi chạy qua `tools/codex-run/run.sh`. Đây là phiếu ảnh nên chạy được cả khi quota Codex < 15 %. Thay phiếu 377 (hai đường, tạm dừng).

Lô: có — 3 ảnh (tranh trong camera, ánh sáng sớm và chiều, rồi ghép tấm so sánh); làm 1 mẫu trước, dừng chờ anh duyệt rồi mới làm tiếp.
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-15/tu-tien/map1-wide/lane-B-final.png

Đọc `docs/games/tu-tien/MAP1_WIDE.md` §13 (bố cục, camera, toạ độ), `docs/games/tu-tien/MAP1_CONCEPT.md` §3–6 (ánh sáng, màu tín hiệu, chất liệu, sự sống — vẫn giữ), skill `game-map-concept`.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/384-report.md`.

## Đường dẫn
`G = games/immortality-cultivation`. Chỉ thêm `G/art-src/concept/map1-lane.v1-try*.png` kèm `.prompt.txt` (ghi đường dẫn mọi ảnh tham chiếu trong mỗi prompt), tấm ghép `G/art-src/concept/map1-lane-384-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`, bắt buộc; không vẽ chỉ từ chữ)
- **Nền bố cục và camera:** `G/tmp/shots/map1-wide/lane-B-final.png` (1920 × 1080, đúng camera chơi 42°, lưới 10 m, legend). Giữ phối cảnh và vị trí; lệch ≤ 20 px.
- **Phong cách map cũ:** `G/art-src/concept/map1-camera.v1-try6.png` (chất liệu, màu, độ chi tiết, ánh vàng nhạt).
- **Ô đất đã có:** `G/art-src/ground/thanh-thach/lane-paving.png` (mặt đường), `court-paving.png`, `court-cracked.png` (sân quanh), `formation-worn.png` (đá trận quanh Trận Tâm). Mặt đất trong tranh phải đọc ra đúng các chất liệu này.
- Không dùng ảnh bên thứ ba.

## Việc (thứ tự)
1. **Mẫu 1** (≤ 2 lần sinh): vẽ đè `lane-B-final.png`, ánh nắng sớm đông bắc. Ghép tấm `map1-lane-384-sheet.jpg` (greybox | tranh | chồng 50 %). Dừng, báo cáo; điều phối gửi anh xem.
2. Chỉ khi anh OK: bản ánh chiều vàng nhạt (theo try6) và bản cuối đã sửa theo góp ý.

## Nội dung tranh
- **Một** con đường đá lát rộng 6 m, uốn mềm từ mép trên khung (z −31) xuống Kết Giới; mòn bóng, **sáng hơn đất quanh ≥ 1,3 lần**, mép có rãnh rêu. Đường là thứ đọc rõ nhất sau Trận Tâm.
- Giữ chỗ: Trận Tâm (đĩa đá, lõi ngọc trắng ngà), vòng Kết Giới r 9 m (khảm ngọc mảnh), hai Trận Trụ 4,5 m, 6 ổ cơ quan chìm H1–H6 dọc đường theo legend, Tâm nhãn (không vẽ người).
- Mốc: Vọng lâu đá đổ nát (−15; −21) ≤ 6 m bên trái; tùng cổ và tảng đá vôi (15; −25) bên phải; cổng ải nằm **ngoài khung** phía trên — chỉ gợi bằng sương và ánh đèn đá ở mép trên. Ngoài x ±22: mép vực rơi xuống biển mây, tùng bám vách. Không thấy trời.
- Một điểm nhấn chính (Trận Tâm), nhì là đường; mốc phụ trầm. Hấp dẫn, sang, nhiều lớp: đá có vân và rêu, ngói chàm, gỗ lim, ngọc trắng ngà, sương chàm, ánh sáng điện ảnh một nguồn. Không mảng đất trống một màu.
- Màu tín hiệu (`#FF4A4A`, `#FFB020`, `#FFC83A`, `#7FF5E0`) không dùng mạnh trong môi trường. Không vật nào che đường. Dải y ≥ 930 (Bàn Quyết) vẽ tối, đơn giản.
- Không người, không quái, không chữ, không UI, không legend.

## Tự chấm (trong báo cáo)
Bảng: Camera khớp · Đọc đường · Hùng vĩ/hấp dẫn · Tiên hiệp Việt · Không che đường · Yếu nhất; ghi độ lệch các mốc so với legend bằng px.

## Claude kiểm sau khi nhận
Chồng 50 % lên greybox, đo lệch; anh xem; hai giám khảo mù ≥ 8,5 mới chấp nhận.

Phản biện: PASS (Sonnet, 15/11)
