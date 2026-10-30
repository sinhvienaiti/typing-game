# Phiếu 238 · Last Line · Làm lại ba ảnh chưa đạt của 150

**Nguồn:**
- Phiếu `docs/codex-queue/150-ts-ui-stage-loadout.md` và báo cáo `150-report.md`. Mọi luật của 150 vẫn áp dụng: phong cách, tham chiếu, hậu kỳ, kích thước, kiểm số, tờ xem. Phiếu này chỉ ghi chỗ khác.
- Claude chấm tờ `games/typing-survival/art-src/_review/150-sheet.jpg` ngày 31/10:
  - **Nhận (từ 8):** `hazard`, `learning-rule`, `equipment`, `warning`, `new-badge`, `chapter-crest`, `load-guns`, `back`. **Không động tới tám ảnh này.**
  - **Chưa đạt:**
    - `objective` 7,5: lá cờ nhỏ nằm trong khung ngoặc vuông; ở 20 px khung lấn cả lá cờ, rối.
    - `station-crest` 7,5: ở 20 px tháp và vòng hố đen dính thành một khối như đĩa bay.
    - `shard` 7,5: tinh thể tối trên nền tối thiếu tương phản (chính báo cáo 150 cũng nêu).

**Báo cáo:** `docs/codex-queue/238-report.md` (tiếng Việt) và thư mục `docs/codex-queue/238/`. Model `gpt-6.1-sol`, mức `high`.

## Việc

Làm lại đúng ba ảnh trên. Mỗi ảnh tối đa **2 lượt sinh mới** (`try2`, `try3`).

**Hướng sửa:** giữ chất liệu và bảng màu của tám ảnh đã nhận.
- `objective`: bỏ khung ngoặc. Lá cờ lớn chiếm phần lớn khung, cán và cờ rõ, lõi lam sáng.
- `station-crest`: một bóng hình rõ ở 20 px. Ví dụ tháp đứng thẳng, cao gấp đôi chiều rộng, vòng hố đen nhỏ và tách hẳn khỏi thân tháp.
- `shard`: viền sáng (ánh vàng hay cam rực) bao quanh bóng hình, lõi cam sáng hơn, để đọc được trên nền `#11161d`. Giữ dáng tinh thể của bản cũ.
  - Chân dung `shard` ở `ui/foes/` (thẻ ải 40 và 60 px) phải khớp với icon mới. Làm lại cả chân dung nếu icon đổi dáng.

**Kiểm nhỏ (bắt buộc):**
- Mỗi lượt có ô 20 px và 30 px trên nền tối và nền sáng.
- `shard` có thêm ô 40 và 60 px như tờ của 150.

**Giới hạn ảnh:** công cụ ảnh trả 429 hoặc báo thử lại sau thì dừng, giữ nguyên mọi file, và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM`.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/icons/{objective,station-crest,shard}.try2.*`, `.try3.*` (mới).
- `games/typing-survival/art-src/ui/foes/shard.try2.*`, `.try3.*` (mới).
- Bản chốt của **đúng ba tên này** ở `ui/icons/` (`.png`, `.64.png`, `.128.png`, `.256.png`, `.prompt.txt`) và bản chốt `shard` ở `ui/foes/`.
  - Được ghi đè vì Claude chưa nhận chúng.
  - Trước khi ghi đè, chép bản cũ sang `art-src/_review/238/prev/` (thư mục mới).
- `games/typing-survival/art-src/_review/238*`.
- `docs/codex-queue/238-report.md`, `docs/codex-queue/238/`.

## Cấm

- Sửa hay xoá file của tám ảnh đã nhận.
- Sửa hay xoá mọi file `try1`.
- Ghi đè sáu chân dung có sẵn khác ở `ui/foes/`.
- Chép vào `public/`.
- Lệnh Git ghi.
- Tu Tiên; `.wt-*`.

## Nhận

- Claude chấm lại từ 8, có xét cỡ 20 px.
- Tờ `238-sheet-delivery.jpg` đặt ba ảnh mới cạnh tám ảnh đã nhận, cùng cỡ.
