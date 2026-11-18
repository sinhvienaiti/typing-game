# Phiếu 229 · Wordwoven · Sửa các phát hiện của kiểm lại 224 (phiếu 170 + 208)

**Nguồn:**
- `docs/codex-queue/224-report.md` §8 "Phát hiện": P1-01 (`vite.config.ts:48`), P1-02 (`scripts/deploy/prune.mjs:8`), P2-01 (`tests/deploy-prune.test.ts:94`), P2-02 (`tests/portal.test.ts:77`). Kết luận của 224: "commit được sau khi sửa các P0–P1".
- Phiếu gốc: `170-td-pack-and-kit.md`, `208-td-deploy-pack.md` và báo cáo của chúng.
- Chủ dự án 30/10: Codex chạy ba làn, giao nhiều việc.

**Không trùng:**
- 224 chỉ đọc. 199, 200, 202 làm ở worktree khác (`.wt-td-scenery`, `.wt-td-ui`).
- Mục "Cần trình duyệt của Claude" trong 224 vẫn là việc của Claude.

**Báo cáo:** `docs/codex-queue/229-report.md` (tiếng Việt) và thư mục `docs/codex-queue/229/`.

## Chỉ chạy khi

1. Có `224-report.md`, `170-report.md`, `208-report.md`.
2. `git -C games/.wt-td-codex branch --show-current` là `td-codex`.
3. `git -C games/.wt-td-codex status --short -uall`:
   - chỉ có các đường chưa commit của 170 và 208 mà 224 đã liệt kê (khoảng 28 đường) thì làm tiếp. Đó là file đã biết, chưa được commit.
   - Có file lạ thì dừng, ghi vào báo cáo.
4. Lưu đầu ra vào `229/status-before.txt`.

## Nơi làm

- Worktree `games/.wt-td-codex`, nhánh `td-codex`. cwd của làn là repo cha (`.`); lệnh `pnpm` chạy trong worktree.
- Chỉ được sửa:
  - `vite.config.ts`, `scripts/deploy/prune.mjs`, `tests/deploy-prune.test.ts`, `tests/portal.test.ts`;
  - `src/app/learning.ts` hoặc `portal.ts` nếu P2-02 cần;
  - một test mới trong `tests/` nếu cần;
  - một changelog mới trong `docs/changelog/` của worktree;
  - báo cáo và `229/` ở repo cha.
- Không sửa `src/kit/**`, kit cha, sim, golden. Git chỉ đọc. Không dev server, trình duyệt, mạng.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn.

## Việc

Mỗi phát hiện: viết test đỏ tái tạo đúng ca trong 224 rồi lưu đầu ra đỏ, sửa, xong chạy lại cho xanh.

1. **P1-01:** khi `VITE_PORTAL_URL` vắng, plugin thay nguồn portal trong `vite.config.ts` phải bắt cả các id có query (`?v=123`, `?import`) và đường qua symlink của `src/kit/learning/contract.ts`. Build không được ra chunk còn nguồn portal cũ. Chuẩn hóa id (bỏ query, `realpath`) trước khi so.
2. **P1-02:** `scripts/deploy/prune.mjs` phải xử lý symlink đứt ở mọi cấp mà 224 nêu (`assets`, `assets/typing-defense`, `models`, `models/keep/link`, `.vite`, `.vite/link`). Dùng `lstat`, không dùng `existsSync`. Symlink đứt thì xóa khỏi `dist` hoặc báo lỗi, theo đúng luật của 208; không được bỏ qua lặng lẽ.
3. **P2-01:** thêm test để đột biến M5 trong 224 (bỏ chặn symlink ở `dist` và tổ tiên, `prune.mjs:37`) làm test đỏ.
4. **P2-02:** thêm test để đột biến M6 trong 224 (`createPortalBridge()` chạy ngay khi import, `learning.ts:27`) làm test đỏ. Kiểm rằng bridge chỉ được tạo khi gọi lần đầu.

## Kiểm (bắt buộc; điều phối cho phép chạy build và toàn bộ test)

1. `pnpm check` trong worktree: số test trước và sau (224 ghi 40 file, 414 test); kit; build.
2. `pnpm deploy:pack` production và bản nhà: 0 lỗi như 208. Ghi byte.
3. Golden của Wordwoven không đổi: lệnh golden của 170 hoặc 208.
4. Chạy lại đột biến M5, M6 của 224 và đột biến cho P1-01, P1-02: test mới đều đỏ.
5. `git -C games/.wt-td-codex status --short -uall` sau khi làm, lưu `229/status-after.txt`. Phần chênh chỉ nằm trong vùng ở mục "Nơi làm".

## Báo cáo

Mỗi phát hiện: test đỏ, bản sửa (tệp:dòng), test xanh, đột biến. Kèm số của mục Kiểm.
