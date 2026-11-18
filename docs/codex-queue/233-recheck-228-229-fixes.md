# Phiếu 233 · Kiểm lại độc lập các bản sửa 228 (repo cha) và 229 (Wordwoven `td-codex`)

**Nguồn:**
- `docs/codex-queue/228-report.md`, `229-report.md` cùng phiếu `228-parent-fix-227-findings.md`, `229-td-fix-224-findings.md`.
- Phát hiện gốc: `227-report.md` (F2–F5, F7) và `224-report.md` §8 (P1-01, P1-02, P2-01, P2-02).
- Chủ dự án 30/10: Codex chạy ba làn, giao nhiều việc. Claude duyệt trước khi commit.

**Không trùng:** phiếu này **chỉ đọc**, không sửa. 227 và 224 đã kiểm bản trước khi sửa; phiếu này kiểm bản sau khi sửa.

**Báo cáo:** `docs/codex-queue/233-report.md` (tiếng Việt) và thư mục `docs/codex-queue/233/`. Model `gpt-6.1-sol`, mức `xhigh`.

## Chỉ chạy khi

1. Có `228-report.md` và `229-report.md`.
2. Repo cha ở nhánh `feat/space-typing-admin-uiux`.
3. `games/.wt-td-codex` ở nhánh `td-codex`.
4. Chưa có `233/`, `233-report.md`, `games/typing-defense/tmp/codex-233/`. Đã có thì dừng.

## Luật chung

- **Repo cha:** chỉ đọc. Được chạy test node của `portal/tests`, `shared/learning` và `scripts/validate-play-mode.test.mjs` ngay trong repo cha, vì các test đó không ghi file. Kiểm bằng `git status` trước và sau: không được có thay đổi mới. Nếu một lệnh build của portal ghi ra `dist`, chạy nó trong bản chép ở `tmp/codex-233-portal/` của repo cha, rồi xóa.
- **`.wt-td-codex`:** chỉ đọc. Lệnh `pnpm` chạy trong bản chép `games/typing-defense/tmp/codex-233/tree`, dựng như mục "Dựng bản chép" của `224-td-pack-recheck.md`.
- Phiếu này **cho phép** chạy build và bộ test trong bản chép. Điều này thắng dòng "do not run the games' builds or test suites" mà runner chèn vào.
- Git chỉ đọc.
- Chỉ ghi: các thư mục `tmp/codex-233*` (xóa khi xong), `233-report.md`, `233/`.
- Cấm:
  - ghi vào worktree hay vào mã của repo cha;
  - `pnpm install`, `kit:sync`, `media:*`;
  - dev server, trình duyệt, mạng;
  - Tu Tiên.

## Việc

1. **Mỗi phát hiện F2–F5 và P1-01, P1-02, P2-01, P2-02:**
   - tái tạo ca gốc theo cách 227 và 224 mô tả, trên mã **sau khi sửa**: ca đó không còn xảy ra;
   - thử thêm ít nhất một biến thể mà bản sửa có thể bỏ sót, ví dụ:
     - F5: mã hóa ba lần, chữ hoa thường `%2f`, dấu `\` thô;
     - P1-01: id có cả query lẫn hash, đường qua hai cấp symlink;
     - P1-02: symlink đứt trỏ ra ngoài `dist`;
   - chạy lại đột biến mà 228 và 229 ghi: test mới đỏ khi tắt bản sửa.
2. **F7** mà 228 không sửa: ghi rõ file và dòng, để Claude sửa khi commit.
3. **Hồi quy:**
   - toàn bộ test portal và `shared/learning`;
   - `pnpm check`, `pnpm deploy:pack` (bản production và bản nhà) và golden của Wordwoven trong bản chép;
   - so số với 228 và 229.
4. **Phạm vi:** diff của 228 chỉ nằm trong vùng phiếu 228 cho phép, và của 229 chỉ trong vùng phiếu 229.
5. **Kết luận:** mỗi phát hiện đã sửa đúng, sửa thiếu hay chưa sửa; mỗi phiếu commit được hay chưa.

## Kiểm (ghi số)

- Số test và gói, so với số của 228 và 229.
- `git status` của repo cha và của `.wt-td-codex` trước và sau phiếu: không có thay đổi mới.
- Dọn các thư mục `tmp/` xong thì ghi lại.

## Báo cáo

- **Bảng:** phát hiện, đã sửa đúng hay chưa, biến thể đã thử, đột biến.
- Phát hiện mới, nếu có: P0, P1, P2, kèm tệp:dòng và đề xuất sửa.
