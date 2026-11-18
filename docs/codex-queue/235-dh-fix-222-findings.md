# Phiếu 235 · Dragonhold · Sửa ba lỗi nặng mà kiểm lại 222 tìm ra (F2, F3, F4)

> **Chạy lại (30/10, 15:22, điều phối):**
> - Năm đường mà lượt 15:18 thấy lạ là của **phiếu 223** (bot giống người, DH-08). 223 chạy sau 222 trong cùng worktree; xem `223-report.md`. Năm đường đó:
>   - `scripts/balance/bot.ts`, `scripts/balance/run.ts` (sửa);
>   - `scripts/balance/human.ts`, `tests/sim/bot-human.test.ts`, `docs/changelog/2026-10-30-human-like-bot.md` (mới).
> - Chúng là file **đã biết**; không sửa. Tập đã biết nay là 51 đường của 222 cộng năm đường này.
> - Clone sạch ở mục Kiểm cũng chép năm file này.
> - Ghi đè `235/status-before.txt` và `235/preflight.json` của lượt dừng.

**Nguồn:**
- `docs/codex-queue/222-report.md` §5:
  - **F2 (major, 197):** lớp màn tựa ghi đè mọi tiêu đề giao diện;
  - **F3 (major, 197 tích hợp 195):** lỗi từ vựng mặc định làm mất đường Retry;
  - **F4 (major, 195):** test thường phụ thuộc dữ liệu ngoài repo mà Git bỏ qua.
- Phiếu gốc `195-dh-deck-notice-and-idle-speed.md`, `197-dh-title-screen.md` và báo cáo của chúng.
- `docs/games/DEPLOY_INDEPENDENCE.md` dòng 20: mỗi game build và test độc lập.
- Chủ dự án 30/10: Codex chạy ba làn, giao nhiều việc.

**Không trùng:**
- **F1** (SVG, icon và tranh gỗ CSS còn lại) chờ Claude chấm ảnh và quyết phạm vi. Không sửa.
- **F5** (đồng hồ âm/VFX) là ghi chú, chờ Claude nghe và xem. Không sửa.

**Báo cáo:** `docs/codex-queue/235-report.md` (tiếng Việt) và thư mục `docs/codex-queue/235/`. Model `gpt-6.1-sol`, mức `high`.

## Chỉ chạy khi

1. Có `222-report.md`.
2. `games/.wt-dh-codex` ở nhánh `dh-codex`.
3. `git -C games/.wt-dh-codex status --short -uall`:
   - chỉ có đường của 187, 194, 195, 197 mà 222 đã liệt kê. Đó là file đã biết, chưa commit.
   - Có đường lạ thì dừng, ghi vào báo cáo.
4. Lưu đầu ra vào `235/status-before.txt`.

## Nơi làm

- Worktree `games/.wt-dh-codex`, nhánh `dh-codex`. cwd của làn là repo cha (`.`); lệnh `pnpm` chạy trong worktree. Phiếu này **cho phép** và **bắt buộc** chạy `pnpm check`, build và toàn bộ test. Điều này thắng mọi luật chung kiểu "không chạy build hay toàn bộ test".
- Chỉ được sửa:
  - `src/ui/styles/title.css`, `src/ui/title.ts`, `src/ui/title-state.ts`;
  - `src/app/app.ts` (đoạn nối màn tựa với deck boot);
  - `src/app/deck-boot.ts` nếu cần;
  - `tests/app/idle-estimate.test.ts`, các file mới dưới `tests/fixtures/`, test mới cho F2 và F3;
  - một changelog mới trong `docs/changelog/` của worktree;
  - báo cáo và `235/` ở repo cha.
- Không sửa `src/sim/**`, `src/kit/**`, golden. Git chỉ đọc. Không dev server, trình duyệt, mạng.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn. Chữ người chơi thấy là tiếng Anh.

## Việc

1. **F2:**
   - màn tựa dùng lớp gốc riêng, ví dụ `.dh-title-screen`, và mọi selector của màn tựa đổi theo;
   - `.dh-title` trở lại chỉ là kiểu chữ như `dh.css:87–95`.
   - Thêm test đọc CSS thật: các tiêu đề ở `hud.ts:291`, `shop-strip.ts:177`, `wave-card.ts:145,161`, `results.ts:232,249` không nhận `position:absolute`, `inset:0`, `z-index:40`, nền, `pointer-events:auto`.
2. **F3:**
   - khi nạp bộ từ mặc định lỗi (mất mạng, bộ rỗng, chỉ 69 từ), màn tựa có nút **Retry**, dùng được bằng phím và chuột;
   - Retry gọi lại `buildDeck` qua đường phục hồi của 195 (`deck-boot.ts:73–89`): chỉ đặt lại nguồn từ, chặn khi đang bận, đã hủy hay đã nạp hai lần;
   - Start vẫn tắt tới khi bộ từ hợp lệ;
   - cổng cấu hình vẫn dùng được.
   - Test: lỗi rồi Retry thì nạp lại và Start bật; Retry hai lần liền chỉ chạy một lần nạp.
3. **F4:**
   - test thường dùng một fixture nhỏ, ổn định, nằm trong repo game, dưới `tests/fixtures/`, không đọc `../dragon-hold/tmp/...`;
   - phép đối chiếu với mẫu audit thật (nếu cần giữ) chuyển thành lệnh kiểm tùy chọn có tham số đường dẫn, mặc định bỏ qua khi thiếu file;
   - fixture không phải media, chỉ JSON nhỏ (dưới 50 KB).
4. **Đột biến:** tắt từng bản sửa F2, F3 thì test mới phải đỏ.

## Kiểm (bắt buộc, ghi số)

- `pnpm check`: số test trước và sau (222 ghi 593), kit, build.
- Golden 10/10 `same`. English UI 9/9 như 197.
- `pnpm deploy:pack` production: 0 lỗi.
- Clone sạch: chép `git ls-files` của worktree, cộng các file chưa commit đã biết, sang `games/dragon-hold/tmp/codex-235/clean` mà **không có** `tmp/map1-audit`; trong bản chép đó `pnpm test` phải xanh. Dựng như mục "Dựng bản chép" của `224-td-pack-recheck.md`, rồi xóa bản chép.
- `git status --short -uall` sau khi làm, lưu `235/status-after.txt`. Phần chênh chỉ nằm trong vùng ở mục "Nơi làm".

## Báo cáo

- Mỗi lỗi: test đỏ, bản sửa (tệp:dòng), test xanh, đột biến.
- Số của mục Kiểm.
- **Mục "Cần trình duyệt của Claude":** HUD, cửa hàng, thẻ đợt, kết quả, màn tựa ở 1280 và 1920; Retry khi tắt mạng.
