# Phiếu 103 · Lời Gọi · Thẻ kết và dải nghĩa lúc rời đi

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 103). Phiếu 100 của lô (từ vựng Rồng) là phiếu **094** trong hàng; mọi chỗ ghi "phiếu 100" ở đây đã đổi thành 094.

**Báo cáo:** `docs/codex-queue/103-report.md`.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (để ghi báo cáo). Mã nằm trong worktree nêu ở từng phiếu; mọi đường dẫn mã tính từ worktree đó.
- **Được dùng git chỉ đọc:** `show`, `log`, `diff`, `status`, `ls-tree`. **Cấm** mọi lệnh git có ghi (`add`, `commit`, `checkout`, `reset`, `stash`, `worktree`…).
- **Cấm:**
  - sửa `src/kit/**` của game (bản chép từ kit, có kiểm sha256);
  - sửa file golden hay chạy lệnh cập nhật golden (`dh:golden:update`, `td:golden:update`…);
  - ghi vào cây chính của game (`games/<id>`), worktree khác, game khác; đụng Tu Tiên;
  - sửa file ở repo cha (nginx, `scripts/`, `shared/`), trừ khi phiếu cho phép;
  - dev server, trình duyệt (sandbox không mở được cổng); media (ảnh, âm, GLB).
- **Cách làm:** test trước, mã sau. Chú thích trong mã bằng tiếng Anh, ngắn. Chuỗi người chơi thấy: câu tiếng Việt, danh từ game tiếng Anh (`docs/games/NAMES_EN.md`).
- **Mỗi phiếu có changelog** `docs/changelog/2026-10-29-<tên>.md` trong worktree, tiếng Việt: làm gì, vì sao, số đo.
- **Báo cáo** `docs/codex-queue/<số>-report.md` và thư mục `docs/codex-queue/<số>/` (log, số đo): file đã đổi; đầu ra của từng mục Kiểm, có số; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chạy lại kiểm, đọc diff, kiểm trên trình duyệt ở 1280 và 1920 khi phiếu đụng giao diện, rồi commit trên nhánh của worktree và gộp.

## Phiếu

**Vì sao:** kiểm kê map 1 (A6, A8, P2).
- **A6:** thẻ kết ghi "Knowledge 0" cả khi không chơi chế độ Học (`src/ui/sheets.ts:96`).
- **A8:** dải nghĩa lúc thẻ rời đi đè lên thẻ kế ("kind · loại, hạng, kiểu" dưới "walk", Đêm 3, 1280). Bước tách cột chưa tính hộp của dải nghĩa (trạng thái `mean`, `src/view/words/cards.ts`).

**Nơi làm:** worktree `games/.wt-td-codex` (nhánh `td-codex`), **sau phiếu 091**. Giữ nguyên mọi thay đổi của 091.

**Chỉ được ghi:**
- `src/ui/sheets.ts`;
- `src/view/words/cards.ts`, `src/view/words/lanes.ts`;
- test mới hoặc sửa trong `tests/` cho hai việc này;
- `docs/changelog/2026-10-29-sheet-cards.md` (mới);
- `docs/codex-queue/103-report.md`, `docs/codex-queue/103/`.

**Trần cứng (Lời Gọi đang sát trần):**
- gói `/` gzip hôm nay 84,91 kB, trần 85,00 kB: sau phiếu không được vượt trần;
- mã `.ts` 10.499 / 10.500 dòng: sau phiếu không được vượt 10.500. Nếu phải thêm dòng, rút gọn trong cùng file mà không đổi hành vi. Không làm được thì dừng ở A6 và báo phần A8.

**Việc:**
1. **A6:** chỉ hiện dòng "Knowledge" khi ván ở chế độ `learn` hoặc `w.knowledge > 0`. Lấy chế độ từ chỗ đang dựng thẻ kết (kiểu `Mode`, xem `src/app/retry.ts`). Ghi vào báo cáo cách lấy chế độ.
2. **A8:** đưa hộp của dải nghĩa (thẻ ở trạng thái `mean`, kéo dài `MS.mean` = 1000 ms) vào bước tách cột, để thẻ kế không nằm đè lên dải nghĩa. Không đổi thời gian, màu, chữ của thẻ.
3. **Test:**
   - A6: thẻ kết ngoài chế độ Học với `knowledge = 0` không có chữ "Knowledge"; chế độ Học có; ngoài Học mà `knowledge = 3` có.
   - A8: nếu bước tách cột là hàm thuần thì thêm ca: hai thẻ cùng cột, thẻ trên đang `mean`, thẻ dưới không chồng lên hộp dải nghĩa. Nếu chưa thuần, tách phần tính hộp ra hàm thuần nhỏ và test hàm đó.

**Kiểm (bắt buộc):**
1. `pnpm test`: số đạt sau = trước + ca mới; `tsc` sạch.
2. `pnpm td:golden:check` giống hệt.
3. `pnpm build`: ghi cỡ gzip của gói `/` trước và sau.
4. Đếm dòng `.ts` theo cách của repo (tìm script hay test trần dòng trong `tests/`, ghi tên): trước và sau.
5. **Đột biến:** bỏ điều kiện chế độ của A6; bỏ hộp dải nghĩa khỏi bước tách cột. Mỗi cái phải làm test đỏ.
6. `git -C games/.wt-td-codex status --short -uall`: chỉ các file trong "Chỉ được ghi" và file của 091.

**Xong khi:** sáu mục đạt và hai trần giữ. Sau đó Claude chạy `td-1b-story`, `td-theme` và cảnh Đêm 3 ở 1280 và 1920.
