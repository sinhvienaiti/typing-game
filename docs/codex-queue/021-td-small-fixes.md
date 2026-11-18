# Phiếu 021 · Lời Gọi · 5 việc nhỏ còn mở sau đợt test 27/10

**Bối cảnh:** sau đợt test 27/10, agent sửa của Claude viết sẵn 5 việc nhỏ để giao Codex. Mỗi việc có file, cách sửa và cách kiểm. Changelog ở `games/typing-defense/docs/changelog/2026-10-27-test-pass.md`, mục "Còn mở". Phiếu chạy **sau phiếu 019** (lượt kiểm lại chỉ đọc) để không đổi mã khi 019 đang đo.

Chủ dự án (27/10) giao một phần việc nhỏ cho Codex và yêu cầu làm đúng, không sai sót. Mỗi việc phải qua kiểm của chính nó. Claude đọc diff, chạy lại kiểm rồi mới commit.

**Thư mục làm việc:** `games/typing-defense`.

**Ngân sách cứng:**
- gói "/" chỉ còn **0,19 kB** dưới trần 85 kB gzip;
- mã `.ts` đang **đúng trần 10.500 dòng** (BUILD_1B §16).

Sửa trong dòng có sẵn; việc nào cần thêm dòng thì phải bớt đúng số dòng đó ở chỗ khác trong cùng file. Gợi ý lấy chỗ ở `docs/td/BUILD_NOTES.md` §7.10.

**Cấm:**
- lệnh git có ghi (chỉ được `log`, `show`, `diff`, `status`). Claude commit;
- sửa sim (`src/sim/**`) hay file vàng;
- đụng media, game khác, Tu Tiên, `shared/game-kit`.

**Quyền chạy:** Codex chạy với sandbox `workspace-write`, thư mục gốc là repo cha (`cd games/typing-defense` trước khi làm). Sandbox có thể chặn mở cổng dev server hay Chrome. Gặp chặn thì ghi rõ lệnh nào, lỗi gì vào báo cáo, làm hết các phần còn lại (đọc mã, `pnpm check`, golden, bot Node). Claude sẽ chạy phần trình duyệt; không tìm cách vượt sandbox.

**Máy dùng chung:** lệnh nặng qua `../../.local/bin/heavy.sh` (`--gpu` cho trình duyệt). Dev server riêng ở cổng 4292, tắt khi xong.

## Việc

Làm đúng như mục "Còn mở" của changelog, tóm tắt dưới đây.

1. **Nhãn kho đè Draconis.**
   - **Sửa:** `src/view/debug-2d.ts`, ở dòng vẽ `T.left[t] + '/' + TREE.reserve`, thêm vào điều kiện `&& Math.abs(w.agents.x[0]! - x) + Math.abs(w.agents.z[0]! - z - TREE.radiusM - 2) > 3`. Đọc mã quanh đó để chắc agent 0 là Draconis và trục đúng.
   - **Kiểm:** `td-1b-wood` đạt ở hai cỡ. Ở Ngày 1 tại 1280×720, cho Draconis đứng cạnh cây đang chặt, chụp ảnh: không có nhãn "…/1000" nào trên đèn lồng của Draconis.
2. **Nhãn "Lời gọi Hoàn hảo" xuống dòng ở thẻ kết hai cột.**
   - **Sửa:** `src/ui/td.css`, trong khối `@media (max-height: 800px)`: thêm `.td-sheet dt { white-space: nowrap; }`, và cho `.td-sheet dl` của khối đó `gap: 3px 10px`.
   - **Kiểm:**
     - `td-1b-story` ở 1280×720, đọc ảnh `td-1b-story-won-1280x720.png`: nhãn nằm trên một dòng, thẻ nằm trong màn.
     - `sheet.scrollWidth <= clientWidth`.
     - `td-theme` vẫn đạt ở hai cỡ.
3. **Bấm "Chép số chơi thử" lần nữa lưu thêm file.**
   - **Sửa:** `src/main.ts`, ở dòng `if (action === "copy") (…)`: bỏ qua khi `lost?.text.startsWith("Đã lưu") && performance.now() < lost.until`.
   - **Kiểm:**
     - Ở hộp cát, làm thua (`__td.flood(220)`), bấm nút hai lần trong 10 s: chỉ có một file `loi-goi-choi-thu-*.json`.
     - `td-1b-tour` vẫn đạt `playtestFileReplays` ở hai cỡ.
4. **Cổng 5b (chỉ đo, không đổi mã).**
   - **Chạy:** `../../.local/bin/heavy.sh node --import tsx scripts/td/balance.ts --stage-seeds=12 --stage-sets=1 --seeds=20 --nights=4 --threads=4`.
   - **Ghi:** số 5b và riêng Ngày 4 vào báo cáo, **không** sửa BUILD_NOTES; Claude chép vào sau khi duyệt.
5. **Dải nghĩa lúc rời đi đè bảng HUD** (ảnh `tmp/mac-2026-10-27/test/verify-fix/final/scen/td-1b-tour-07-choang-1280x720.png`).
   - **Sửa:** `src/view/words/cards.ts`, chỗ đặt thẻ ở trạng thái `'mean'`: kẹp `card.x` để hộp của dải không chạm hộp nào trong `panels`. Giữ đúng số dòng `.ts`.
   - **Kiểm:** ảnh 07 của `td-1b-tour` ở hai cỡ; `td-1b-learn` ở hai cỡ (`cardsClean`).

## Kiểm chung (bắt buộc)

1. Sau mỗi việc có sửa mã: `../../.local/bin/heavy.sh pnpm check`. Ghi số test, gói "/" (kB gzip), số dòng `.ts`. Cả ba phải trong trần.
2. `pnpm td:golden:check`: hai file `same: true` (không việc nào được đổi sim).
3. Cuối cùng, `git diff --stat` và `git diff` đầy đủ, dán vào báo cáo.

## Báo cáo `docs/codex-queue/021-report.md` (repo cha)

Bảng `| # | Việc | File:dòng đã sửa | Kiểm (lệnh, kết quả, ảnh) | Gói "/" | Dòng .ts |`, kèm mục Kiểm chung. Việc nào không làm được trong ngân sách: ghi lý do, để nguyên mã.

**Xong khi:** 5 việc có kết quả, `pnpm check` và golden đạt trên cây cuối.
