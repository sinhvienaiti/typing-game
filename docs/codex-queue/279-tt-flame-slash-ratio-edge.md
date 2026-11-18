# Phiếu 279 · Tu Tiên · Code: nhát chém kết phím 7 Hỏa, sửa tỉ lệ dải và mép cắt thẳng (sau 275)

**Loại việc:** code phần nhìn (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/279-report.md`.

**Worktree:** `games/.wt-ic-flame-slash`, nhánh `codex/flame-slash-strip`, HEAD `f3e7029` (phiếu 275 đã commit). `git status --short` lúc giao chỉ có `?? node_modules`. Nếu có `art-src` hay `public` là link của Claude thì không đụng.

**Nguồn:**
- Phiếu `docs/codex-queue/275-tt-flame-slash-strip.md`, nhất là dòng 62 về `uStripK`.
- Nhật ký kiểm của Claude ở `docs/work/tasks/flame-slash.md` (05/11 02:32). Hai lỗi:
  1. **Dải bị kéo dài:** với `k = 3`, dải lửa trông dài gấp khoảng 1,5–2 lần tỉ lệ tự nhiên 2:1, nên giống mảng dung nham hơn là lưỡi lửa liếm.
  2. **Mép cắt thẳng:** khoảng khung 200–215 có một mép cắt dọc, thẳng ở đầu chạy, do `float behind = step(s, uHead + 0.02);` là hàm bậc. Mép này có từ trước, nhưng dải rộng làm nó lộ hơn.

## Việc
1. **Tỉ lệ dải:** làm đúng như phiếu 275 dòng 62.
   - `uStripK` tính trong `set(...)`, từ chiều dài cung trên màn và bề rộng dải, sao cho mỗi chu kỳ dải giữ tỉ lệ tự nhiên 2:1 của ảnh dải (đọc kích thước từ `.json` của dải).
   - Chỉ khi không đo được mới dùng số dự phòng; đổi số dự phòng từ 3 thành 5.
   - Thêm cờ lab `?stripK=<số>` để Claude chỉnh tay, không dùng ở bản chơi.
   - Ghi công thức trong báo cáo.
2. **Mép đầu mềm:** thay `step(s, uHead + 0.02)` bằng một dải chuyển mềm theo chiều dài nhát chém, khoảng 6–8 % chiều dài, `smoothstep` từ đầu chạy về sau. Biên của dải chuyển rách theo nhiễu sẵn có của dải (cùng `n` đang dùng), để đầu nhát chém tan như lửa chứ không thành đường thẳng. Đỉnh sáng khung đầu không đổi.
3. **Không đổi gì khác:** nhịp, màu, `?slash=tongues` (đường cũ), hệ Kim.

### Được ghi
`src/view/skills/flame-slash.ts`, `src/view/skills/element-fire.ts` (chỉ chỗ gọi `set`), `src/lab/skills-main.ts` (chỉ cờ `stripK`), `tests/view/flame-slash.test.ts` (cập nhật chuỗi shader và các ca `uStripK` cho đúng logic mới, không nới phép kiểm), `docs/changelog/2026-11-05-flame-slash-strip.md`, và `docs/codex-queue/279-report.md` ở repo cha.

### Cấm
Lệnh git ghi; sửa file khác; mở cổng mạng; tạo ảnh hay âm.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua. Mốc là 979 test ở `f3e7029`.
3. Test mới:
   - (a) `uStripK` đổi theo chiều dài cung và giữ tỉ lệ 2:1 ±10 % trên ba bộ số tổng hợp;
   - (b) dự phòng là 5;
   - (c) chuỗi shader không còn `step(s, uHead`.
4. Build tạm bằng bộ bọc của 274:
   ```sh
   IC_VITE_CACHE_DIR=/private/tmp/codex-279-dist/.vite-cache node /Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/274-out/build-no-cache.mjs --no-cache --configLoader runner --outDir /private/tmp/codex-279-dist
   ```
   Grep bundle không thấy `stripK`; xóa thư mục build.
5. `git status --short` chỉ có các tệp được ghi.

## Claude làm sau
Quay lại video trước/sau ở camera chơi, kiểm hệ Kim trùng khít, gửi anh, rồi gộp.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
