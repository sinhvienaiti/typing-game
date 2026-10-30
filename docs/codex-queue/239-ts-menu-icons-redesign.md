> **Chạy lại sau hạn mức (31/10, điều phối Claude):**
> - Lượt 02:56 dừng vì hết hạn mức. Nó chạy theo bản phiếu cũ, nên `next-stage` khi đó còn là chevron.
> - File đã có của lượt đó là file đã biết. Giữ nguyên, không xoá:
>   - `menu-journey.c2-try1..3`;
>   - `menu-armory.c2-try1`;
>   - `next-stage.c2-try1..2`.
> - `menu-journey` và `menu-armory`: làm tiếp từ các lượt đã có. `menu-journey` đã dùng đủ 3 lượt, nên chỉ chọn trong ba bản đó và chốt.
> - `next-stage`: hai bản `c2` theo ý tưởng chevron cũ **không tính lượt**. Ý tưởng mới (mũi tên xuyên cổng, mục Việc) đặt tên `next-stage.c3-try1..3`, tối đa 3 lượt.
> - Ghi đè `239-report.md` nếu lượt trước đã viết dở.

# Phiếu 239 · Last Line · Đổi ý tưởng ba icon menu của 151

**Nguồn:**
- Phiếu `docs/codex-queue/151-ts-ui-menu-results.md` và báo cáo `151-report.md`. Mọi luật của 151 vẫn áp dụng: phong cách, tham chiếu, hậu kỳ, kích thước, kiểm số, tờ xem. Phiếu này chỉ ghi chỗ khác.
- Claude chấm tờ `games/typing-survival/art-src/_review/151-sheet-20261031-v3.jpg` ngày 31/10:
  - **Nhận (từ 8):** `menu-play`, `menu-mode`, `menu-settings`, `menu-profile`, `star-lit`, `star-unlit`, `retry`, `stat-time`, `stat-accuracy`. **Không động tới chín icon này.**
  - **Chưa đạt:**
    - `menu-journey` 7: dải dọc ngoằn ngoèo; ở 24 px thành một sợi, không đọc ra "hành trình". Đã dùng 3 lượt.
    - `next-stage` 7,5: khung cổng; ở 20 px thành một ô vuông rỗng. Đã dùng 3 lượt.
    - `menu-armory` 7,5: ba ngạnh mảnh; ở 24 px mảnh. Trùng ý tháp đôi của `chapter-crest` (đã nhận ở 150).

**Báo cáo:** `docs/codex-queue/239-report.md` (tiếng Việt) và thư mục `docs/codex-queue/239/`. Model `gpt-6.1-sol`, mức `high`.

## Việc: ý tưởng mới, mỗi icon tối đa 3 lượt

Đây là **ý tưởng mới**, nên tính lượt lại từ đầu. Đặt tên `<tên>.c2-try1`, `c2-try2`, `c2-try3`. Giữ chất liệu kim loại trắng ngà viền vàng và lõi lam như chín icon đã nhận. Khung bao gần vuông (không quá 1,3:1). Không vẽ chữ.

- `menu-journey`: một tấm bản đồ sao nhỏ, có đường đi cong nối ba điểm mốc. Điểm cuối là một ghim định vị lam sáng.
- `next-stage`: một mũi tên dày, thân thẳng, chỉ sang phải, xuyên qua một vòng cổng tròn mở (cổng sang ải sau). Vòng cổng có lõi lam.
  - **Không dùng chevron.** `menu-play` là một chevron đơn; `streak` (đã nhận ở 237, 31/10) là hai chevron.
  - Kiểm bằng ô so sánh với cả hai icon đó.
- `menu-armory`: một giá súng nhìn thẳng, hai hoặc ba bóng súng dựng đứng trong khung giá dày. Hoặc một hòm vũ khí mở nắp có lõi sáng.
  - Phải khác `equipment` của 150 (hai súng bắt chéo). Kiểm bằng ô so sánh.

**Kiểm nhỏ (bắt buộc):**
- Ô 20 và 24 px trên nền tối và nền sáng.
- Ô so sánh: `next-stage` cạnh `menu-play` và `streak`; `menu-armory` cạnh `equipment` và `chapter-crest`.

**Giới hạn ảnh:** công cụ ảnh trả 429 hoặc báo thử lại sau thì dừng, giữ nguyên mọi file, và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM`.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/icons/{menu-journey,next-stage,menu-armory}.c2-try*.*` (mới).
- Bản chốt của **đúng ba tên này** (`.png`, `.64.png`, `.128.png`, `.256.png`, `.prompt.txt`).
  - Được ghi đè vì Claude chưa nhận chúng.
  - Trước khi ghi đè, chép bản cũ sang `art-src/_review/239/prev/`.
- `games/typing-survival/art-src/_review/239*`.
- `docs/codex-queue/239-report.md`, `docs/codex-queue/239/`.

## Cấm

- Sửa hay xoá file của chín icon đã nhận, hay của các ảnh 149 và 150.
- Sửa hay xoá mọi file `try*` cũ.
- Chép vào `public/`.
- Lệnh Git ghi.
- Tu Tiên; `.wt-*`.

## Nhận

- Claude chấm lại từ 8, có xét cỡ 20 và 24 px và các ô so sánh.
