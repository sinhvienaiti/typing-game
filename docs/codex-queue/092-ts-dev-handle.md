# Phiếu 092 · Tuyến Cuối · `window.__survival` chỉ có ở bản dev hoặc khi có `?debug=1`

**Vì sao:** kiểm kê map 1 ngày 28/10 (TS-M1-20, P2, cổng G7). Bản production vẫn cài `window.__survival`, gồm cả lệnh `flood`, `send`, `place`, `hold`: ai mở console cũng thả được bầy quái hay đặt quái. Các kịch bản trình duyệt (`scripts/visual/scenarios/survival-*.mjs`) chạy trên dev server nên vẫn cần nó; một lượt kiểm trên bản build thì bật bằng `?debug=1`.

**Báo cáo:** `docs/codex-queue/092-report.md`.

## Nơi làm

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (để ghi báo cáo).
- **Mã:** worktree `games/.wt-ts-codex` (nhánh `ts-codex`). Phiếu 090 có thể đã sửa worktree này trước (từ vựng): **giữ nguyên** thay đổi của 090, không hoàn lại.

**Chỉ được ghi:**
- `games/.wt-ts-codex/src/app/dev.ts`, `src/app/main.ts` (chỉ đoạn gọi `installDevHandle`, khoảng dòng 681);
- `games/.wt-ts-codex/tests/dev-handle.test.ts` (mới);
- `games/.wt-ts-codex/docs/changelog/2026-10-28-dev-handle.md` (mới, tiếng Việt);
- `docs/codex-queue/092-report.md`, `docs/codex-queue/092/`.

**Cấm:**
- mọi lệnh git có ghi. Được dùng `git diff`, `git status`;
- sửa `src/kit/**`, `src/sim/**`, `src/content/**` hay bất kỳ file nào ngoài danh sách trên;
- đổi nội dung của handle (các hàm, tên, thứ tự): chỉ đổi **khi nào** nó được cài;
- ghi vào `games/typing-survival` (cây chính), `games/.wt-ts-vfx`, game khác; đụng Tu Tiên;
- dev server, trình duyệt; media.

## Việc

1. Trong `src/app/dev.ts`, thêm hàm thuần, có chú thích tiếng Anh ngắn:
   ```ts
   export function devHandleWanted(dev: boolean, search: string): boolean
   ```
   Trả `true` khi `dev` là `true`, hoặc khi `new URLSearchParams(search)` có khóa `debug` với giá trị `"1"`. Trả `false` với mọi trường hợp khác, kể cả `?debug=0`, `?debug=`, `?debug=true`, `?nodebug=1`.
2. Trong `src/app/main.ts`, chỉ cài handle khi `devHandleWanted(import.meta.env.DEV, location.search)` trả `true`. Giữ nguyên đối tượng truyền vào `installDevHandle` từng ký tự; chỉ bọc lời gọi trong `if`. Sửa câu chú thích ở dòng khoảng 50 của `main.ts` ("window.__survival lets the browser …") để ghi điều kiện mới.
3. Nếu có kịch bản trong `scripts/` chạy trên bản build (không phải dev server) và đọc `__survival`, ghi tên nó vào báo cáo, **không sửa**. Claude sẽ thêm `?debug=1`.
4. **Test `tests/dev-handle.test.ts`** cho `devHandleWanted`, ít nhất 8 ca:
   - `(true, "")` → true; `(true, "?debug=0")` → true;
   - `(false, "")` → false; `(false, "?debug=1")` → true; `(false, "?card=1&debug=1")` → true;
   - `(false, "?debug=0")`, `(false, "?debug=")`, `(false, "?debug=true")`, `(false, "?nodebug=1")` → false.
5. **Changelog** `docs/changelog/2026-10-28-dev-handle.md`.

## Kiểm (bắt buộc, ghi đầu ra vào báo cáo)

1. `pnpm check` trong worktree: xanh; ghi số test trước và sau.
2. `node --import tsx scripts/chapter-hashes.ts`: không đổi so với trước khi sửa (chạy trước và sau, `diff` rỗng).
3. **Đột biến:** đổi `"1"` thành `"0"` trong `devHandleWanted` → `pnpm vitest run tests/dev-handle.test.ts` đỏ; trả lại → xanh.
4. `pnpm build`, rồi `grep -c "__survival" dist/assets/*.js`: chuỗi vẫn có (handle vẫn được build, chỉ không cài), ghi số. Không cần kiểm trình duyệt: Claude kiểm.
5. `git -C games/.wt-ts-codex diff --stat`: chỉ có file của phiếu này và của phiếu 090. Dán đầu ra.

## Báo cáo `docs/codex-queue/092-report.md`

Tiếng Việt: file đã đổi; đầu ra năm mục Kiểm; danh sách kịch bản ở việc 3.

**Xong khi:** năm mục Kiểm đạt. Claude kiểm trên trình duyệt (dev có handle; bản build không có handle, có handle khi thêm `?debug=1`), rồi commit.
