# Phiếu 278 · Tu Tiên · Code: làm nốt 277, sửa hai cổng trượt của 264

**Loại việc:** code phần nhìn (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/278-report.md`.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, nền `ee3ee97` (đã có 264). Làm tiếp trên các thay đổi **chưa commit** của 277 trong cùng worktree, như 259b từng làm tiếp 259. Đọc `docs/codex-queue/277-report.md` trước.

## A. Làm nốt 277: Claude gỡ hai chỗ phiếu 277 viết sai
1. **Được sửa 6 test cũ** mà báo cáo 277 nêu là mâu thuẫn với đường mặc định mới.
   - Các test đó kiểm đường cũ (`FirePointPool`, `HeatRingPool`), nên đặt cờ `fxcode` trong phần dựng của chúng để chúng tiếp tục kiểm đúng đường cũ.
   - Không nới hay xóa phép kiểm nào.
   - Nếu một ca thật sự kiểm hành vi của đường mặc định, chuyển nó sang kiểm đường art mới với cùng mức chặt.
   - Ghi trong báo cáo từng ca: tên ca, sửa gì, vì sao.
2. **Lệnh build:** dùng bộ bọc mà phiếu 274 và 264 đã dùng, không gọi CLI Vite với `--no-cache`:
   ```sh
   IC_VITE_CACHE_DIR=/private/tmp/codex-278-dist/.vite-cache node /Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/274-out/build-no-cache.mjs --no-cache --configLoader runner --outDir /private/tmp/codex-278-dist
   ```
   Grep bundle không thấy `fxcode`, rồi xóa thư mục build.

## B. Sửa hai cổng lab trượt của 264
Số đo nằm ở `typing-game-review/captures/tu-tien/impact-k1-v2/gates.json`, ghi ở `docs/work/tasks/key1-fire.md` (05/11 02:40).

1. **Chớp ở khung đầu.**
   - Đo được `E(tuổi 0) / max(E tuổi 0–12)` là 0,76–0,91; cả 6 ca đều có tuổi 1 sáng hơn tuổi 0. Ngưỡng là ≥ 0,95.
   - Phản biện 264 đã chỉ ra: chớp `fx-fire-flash` được vẽ lần đầu khi đã già một khung (`fxkit.ts:451`).
   - Sửa để đỉnh rơi đúng tuổi 0 cho chớp của brush impact (`BRUSH.flash` trong `element-fire.ts`).
   - **Ưu tiên sửa cục bộ trong `element-fire.ts`.** Chỉ khi buộc phải sửa `SpritePool` trong `fxkit.ts` thì thêm tùy chọn theo pool, mặc định tắt, để không pool nào khác đổi hành vi.
2. **Biên dịch lần đầu.**
   - Khung trúng đầu tiên mất 96 ms, ngưỡng 11,5 ms.
   - Làm ấm lúc nạp lab: chương trình `FlipbookPool` v2 và vật liệu của brush impact, cùng các pool mới của 277. Theo cách đã có ở `skills-main.ts` khoảng dòng 1601–1613 (`screen.prewarm`, `swordAura.prewarm`, `fx.prewarmAura`): thêm một hàm prewarm cho phần lửa và gọi nó cùng chỗ đó.
   - Không đổi hình hay số.
3. **`ageTicks`** (`skills-main.ts` khoảng dòng 1787): trả `Math.round(...) + 0` để không ra `-0`. CDP đọc `-0` thành `undefined`, làm kịch bản chụp lấy trùng khung.

### Được ghi
- `src/view/skills/element-fire.ts`, `src/view/skills/element-stage.ts`;
- `src/lab/skills-main.ts`: chỉ phần prewarm và `ageTicks`;
- `src/view/skills/fxkit.ts`: chỉ khi buộc phải, theo mục B1;
- 6 test cũ ở mục A1 và `tests/view/fire-lot1-art.test.ts`;
- một test mới `tests/view/key1-flash-age0.test.ts` (chớp brush ở tuổi 0 bằng đỉnh, dùng clip giả);
- `docs/changelog/2026-11-05-fire-lot1-art.md`;
- `docs/codex-queue/278-report.md` ở repo cha.

### Cấm
Lệnh git ghi; sửa kit, sim, nội dung, `art-src`; nới phép kiểm; mở cổng mạng; tạo ảnh hay âm.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua. Mốc ở `ee3ee97` là 985 test.
3. Build như mục A2: thoát 0, grep không thấy `fxcode`, đã xóa thư mục build.
4. `git status --short` chỉ có các tệp được ghi, cộng `?? node_modules` và `?? art-src` (link của Claude, không đụng).

## Claude làm sau
- Chạy lại 7 cổng lab của 264 và parity ONLY lô 1, cùng perf.
- Quay video trước/sau, gửi anh, cho giám khảo mù chấm.
- Commit cả 264, 277 và 278, rồi gộp vào `main` sau 275.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
