# Phiếu 240 · Last Line · Làm lại ba icon của 152 và một mảnh của 153

**Nguồn:**
- Phiếu `152-ts-ui-settings.md`, `153-ts-ui-parts.md` và báo cáo của chúng. Mọi luật của hai phiếu vẫn áp dụng: phong cách, tham chiếu, hậu kỳ, kích thước, kiểm số, tờ xem. Phiếu này chỉ ghi chỗ khác.
- Claude chấm ngày 31/10:
  - **152** (tờ `_review/152-sheet-final.jpg`):
    - **Nhận:** `sfx`, `music`, `read-aloud`, `pace-director.v2`, `quality`, `stat-wpm.v2`, `stat-new-word`, `rift`. Sắc tím của `rift` là chủ ý, nhận. Hai bản `.v2` là bản chọn của `pace-director` và `stat-wpm`.
    - **Chưa đạt:**
      - `shake` 7: khung rỗng hai bên có răng cưa; ở 20 px chỉ còn một ô chữ nhật rỗng.
      - `reduced-motion` 7: khung rỗng có mỏ neo nhỏ; ở 20 px cũng thành ô rỗng.
      - `stat-evenness` 6,5: một thanh ngang mảnh; ở 24 px thành một vạch.
  - **153** (tờ `_review/153-sheet.jpg`):
    - **Nhận:** `keycap`, `keycap-active`, `led-on`, `led-off`, `mag-full`, `arrow`.
    - **Chưa đạt:** `mag-empty` 7,5: viền tối trên nền tối; ở 10 px gần như biến mất.

**Báo cáo:** `docs/codex-queue/240-report.md` (tiếng Việt) và thư mục `docs/codex-queue/240/`. Model `gpt-6.1-sol`, mức `high`.

## Việc

Mỗi ảnh tối đa 3 lượt. `shake` và `reduced-motion` đổi ý tưởng, nên đặt tên `<tên>.c2-tryN`. `stat-evenness` và `mag-empty` tiếp từ `try2`.

Giữ chất liệu và bảng màu của các ảnh đã nhận. Bóng hình phải **đặc**, không phải khung rỗng.
- `shake`: một khối thiết bị đặc (lõi lam sáng) có hai bóng mờ lệch hai bên và vạch rung dày. Đọc ra "rung" ở 20 px.
- `reduced-motion`: một quả cầu đặc có ba vệt tốc độ, các vệt bị một vòng kẹp giữ lại và mờ dần. Đọc ra "chuyển động dịu lại" ở 20 px.
  - Phải khác hẳn `shake` khi đặt cạnh nhau.
- `stat-evenness`: khung bao gần vuông, ba cột cao bằng nhau trên một bệ, lõi lam đều. Đọc ra "đều tay".
- `mag-empty`: cùng dáng với `mag-full` đã nhận. Viền vàng sáng và dày hơn; lòng rãnh tối có mép lam rất mờ. Ở 10 px trên nền tối vẫn thấy rõ một ô rỗng; đặt cạnh `mag-full` phải phân biệt ngay.

**Kiểm nhỏ (bắt buộc):**
- Ô 20, 24 px (icon) hoặc 10, 15 px (`mag-empty`) trên nền tối và nền sáng.
- Ô so sánh `shake` cạnh `reduced-motion`; `mag-empty` cạnh `mag-full`.

**Giới hạn ảnh:** công cụ ảnh trả 429 hoặc báo thử lại sau thì dừng, giữ nguyên mọi file, và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM`.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/icons/{shake,reduced-motion}.c2-try*.*` và `stat-evenness.try2.*`, `.try3.*` (mới).
- `games/typing-survival/art-src/ui/parts/mag-empty.try2.*`, `.try3.*` (mới).
- Bản chốt của **đúng bốn tên này**.
  - Được ghi đè vì Claude chưa nhận chúng.
  - Trước khi ghi đè, chép bản cũ sang `art-src/_review/240/prev/`.
- `games/typing-survival/art-src/_review/240*`.
- `docs/codex-queue/240-report.md`, `docs/codex-queue/240/`.

## Cấm

- Sửa hay xoá ảnh đã nhận và mọi file `try*` cũ.
- Chép vào `public/`.
- Lệnh Git ghi.
- Tu Tiên; `.wt-*`.

## Nhận

- Claude chấm lại từ 8, có xét cỡ nhỏ và các ô so sánh.
