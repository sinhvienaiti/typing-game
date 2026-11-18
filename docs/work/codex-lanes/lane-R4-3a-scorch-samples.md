# Vòng 4 · Bước 3a · Vẽ mẫu vết sét cháy trên nền đá (2 bản cho anh duyệt)

Giám khảo bước R3-3 (`docs/work/consult/r3-step3-verdict.md`): vết hiện tại là nét tím phẳng, không giống đá bị sét đánh cháy rồi nguội, khó đọc ở góc chơi. Đề xuất của giám khảo: **dấu cháy có chất liệu nền đá, lõi tối, khe sáng mảnh cùng vị trí; khe sáng nguội dần, mép bị xói từ ngoài vào** (engine lo phần nguội và xói). Kho chỉ có `thunder-ground-mark` (đang dùng), nên phải vẽ mới. Luật ảnh: `.agents/skills/game-vfx-production/references/path-to-8.md` §5 và tầng A ở §1; luật dự án: ảnh tham chiếu của ta, không bao giờ chỉ prompt.

**Model `gpt-6.1-sol`, mức `high`.** Một lần chạy, tối đa 12 ảnh xem. Báo cáo: thêm ≤ 8 dòng vào `docs/codex-queue/laneL1-report.md`.

## Ảnh tham chiếu (bắt buộc đưa vào image_gen, ghi đường dẫn vào `.prompt.txt`)
- `.local/r4/refs/current-thunder-ground-mark-frame20.png`: bố cục nhánh sét tỏa từ tâm của vết đang dùng; giữ tinh thần hình, đổi chất liệu.
- `.local/r4/refs/lab-floor-before-cast.png` và `lab-floor-with-current-mark-2.10s.png`: nền đá sân và cỡ vết ở góc chơi (vết cần đọc được ở cỡ này).
- Kiểu ánh sáng đã được anh duyệt: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/blood-ring-burst-still.v1-try2.png` (lõi sáng mảnh, quầng mềm, đốm sáng nhỏ).
- Không dùng ảnh bên thứ ba.

## Việc
- Vẽ **2 bản** (`try1`, `try2`) của một vết sét đánh xuống nền đá, nhìn **thẳng từ trên xuống** (trực giao, không phối cảnh), vuông 1024 px, lề ≥ 8 % mỗi cạnh, không đổ bóng, nền đen thuần:
  - **lớp nền** `<tên>-base`: đá cháy sém tối (than, muội, vài mảnh đá vỡ nhỏ, rạn tỏa từ tâm), mép không đều, mờ dần ra ngoài; không phát sáng;
  - **lớp khe** `<tên>-cracks`: chỉ các khe sáng mảnh nằm **đúng vị trí** các rạn của lớp nền, màu tím–trắng, lõi khe mảnh và sáng nhất, quầng ≤ 0,9 mỗi kênh, vài đốm lửa sét nhỏ;
  - hai lớp phải khớp từng điểm ảnh khi chồng lên nhau. Cách dễ nhất: vẽ lớp nền trước, rồi lấy chính nó làm ảnh nguồn để vẽ lớp khe.
- Đặt tên: `thunder-scorch-base.v1-try<k>.png`, `thunder-scorch-cracks.v1-try<k>.png`, mỗi ảnh một `.prompt.txt`. Thư mục: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/scorch/thunder-scorch/`.
- Tự chấm mỗi bản theo 5 ô tầng A (§1) cộng sức hút (1–10); ghi bản đề xuất.
- **Tấm duyệt** `.local/r4/scorch-samples.jpg`: mỗi bản một hàng gồm lớp nền, lớp khe, hai lớp chồng nhau trên `lab-floor-before-cast.png` ở cỡ gần cỡ vết thật ở góc chơi, và một ô phóng to. Claude gửi anh tấm này. **Chưa lắp vào lab** cho tới khi anh duyệt.

## Ranh giới
- **Chỉ ghi:** thư mục `scorch/thunder-scorch/` ở trên, `.local/r4/`, báo cáo.
- **Không:** sửa mã, manifest hay media khác; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Hết hạn mức
Khi image_gen báo hết lượt, giữ file đã có và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
