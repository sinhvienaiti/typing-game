# Phiếu 237 · Last Line · Làm lại ba icon HUD chưa đạt của 149

**Nguồn:**
- Phiếu `docs/codex-queue/149-ts-ui-hud.md` và báo cáo `149-report.md`. Mọi luật của 149 vẫn áp dụng: phong cách, tham chiếu, hậu kỳ, kích thước, kiểm số, tờ xem. Phiếu này chỉ ghi chỗ khác.
- Claude chấm tờ `games/typing-survival/art-src/_review/149-sheet-delivery.jpg` ngày 31/10:
  - **Nhận (từ 8):** `armour`, `clock`, `kills`, `surge`, `repair-pod`, `check`, `lock`. **Không động tới bảy icon này.**
  - **Chưa đạt:**
    - `keyboard` 7: dáng ngang rộng hơn 2:1, nên ở 16 và 24 px chỉ còn một vạch, không đọc ra bàn phím.
    - `bay-full` 7,5: dáng dọc 1:2, ở 16 px thành một sợi mảnh.
    - `streak` 7,5: ba ngôi sao nhỏ nối chéo, ở 16 px chỉ còn ba chấm mờ.

**Báo cáo:** `docs/codex-queue/237-report.md` (tiếng Việt) và thư mục `docs/codex-queue/237/`. Model `gpt-6.1-sol`, mức `high`.

## Việc

Làm lại đúng ba icon trên. Mỗi icon tối đa **2 lượt sinh mới** (`try2`, `try3`), vì `try1` đã dùng ở 149.

**Hướng sửa:** mục tiêu là đọc được ở 16 và 24 px. Giữ chất liệu kim loại trắng ngà viền vàng và lõi lam phát sáng như bảy icon đã nhận.
- `keyboard`: dáng gần vuông, tỷ lệ khung bao không quá 1,3:1. Ví dụ một cụm 2×2 phím lớn nhìn chéo 3/4, một phím sáng lam. Không vẽ chữ hay ký tự lên phím.
- `bay-full`: dáng gần vuông, không quá 1,3:1. Ví dụ một ổ nạp thấp và rộng, ba ô lam đầy đặt cạnh nhau, viền dày.
- `streak`: ít chi tiết, nét dày. Ví dụ hai hoặc ba mũi chevron lớn nối liền, hoặc một ngôi sao lớn kéo vệt. Bóng hình phải đọc được ở 16 px.

**Kiểm nhỏ (bắt buộc):**
- Mỗi lượt có thêm ô 16 px và 24 px trên nền tối và nền sáng, như tờ của 149.
- Không đạt ở 16 px thì sửa prompt rồi sinh lượt kế.

**Giới hạn ảnh:** công cụ ảnh trả 429 hoặc báo thử lại sau thì làm theo luật chung của bộ chạy: dừng, giữ nguyên mọi file, và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM`.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/icons/{keyboard,bay-full,streak}.try2.*`, `.try3.*` (mới).
- Bản chốt của **đúng ba tên này**: `{keyboard,bay-full,streak}.png`, `.64.png`, `.128.png`, `.256.png`, `.prompt.txt`.
  - Được ghi đè vì Claude chưa nhận chúng.
  - Trước khi ghi đè, chép bản cũ sang `art-src/_review/237/prev/` (thư mục mới).
- `games/typing-survival/art-src/_review/237*` (tờ xem mới).
- `docs/codex-queue/237-report.md`, `docs/codex-queue/237/`.

## Cấm

- Sửa hay xoá file của bảy icon đã nhận.
- Sửa hay xoá mọi file `try1`.
- Chép vào `public/`: Claude chép khi gắn.
- Lệnh Git ghi.
- Tu Tiên; `.wt-*`.

## Nhận

- Claude chấm lại từ 8, có xét cỡ 16 và 24 px.
- Tờ `237-sheet-delivery.jpg` đặt ba icon mới cạnh bảy icon đã nhận, cùng cỡ, để so phong cách.
