# Phiếu 271c · Tu Tiên · Code: Song Long chỉ giải khi có thú trong dải trúng

**Loại việc:** code nhỏ (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã chốt. Không thiết kế lại.

**Báo cáo:** tin nhắn cuối. Claude chép vào `docs/codex-queue/271c-report.md`.

**Đường duyệt:** đây là quyết định của Claude (người chốt), lúc 20:45 ngày 04/11, cho điểm "thiết kế mơ hồ" A1 mà phiếu 271b tìm ra. Phiếu là bản sửa một chỗ theo đúng chữ của §9.2 ("chiêu chỉ giải khi có thú nhận được sát thương"), nên bỏ bước phản biện.

## Bối cảnh
- Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide`, nhánh `codex/twin-pearl-fieldwide`, có thay đổi chưa commit của phiếu 271 và file test của 271b.
- Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/271/section9-design.md`:
  - §9.2 dòng 38: chỉ chụp thú ở dải đất (≤ 1,5 m) hoặc dải trời (2,5–6 m);
  - §9.2 dòng 42: chỉ giải khi có thú nhận được sát thương;
  - §9.6: thú ở giữa hai dải không bị khối nào trúng.
- Lỗi A1 (báo cáo 271b), ở `tests/sim/twin-pearl-sweep.test.ts` dòng khoảng 459, đang để `it.fails`:
  - hai thú sống, không miễn thương, ở độ cao 149.999 u và 90.001 u, tức giữa hai dải;
  - `resolveTwinPearl` vẫn giải (hồi chiêu 480 tick) mà không có đòn dương nào tới F102.
- Nguyên nhân: `resolveTwinPearl` trong `src/sim/twin-pearl.ts` (khoảng dòng 487) chỉ kiểm `alive && !damageImmune`.

## Việc (lời giải đã chốt)
1. Trong `resolveTwinPearl`, điều kiện giải đổi thành: có ít nhất một thú `alive && !damageImmune(world, beast)` **và** độ cao của nó thỏa `inGroundBand(y) || inSkyBand(y)`. Độ cao y lấy đúng như phần chụp ảnh F0 đang lấy (cùng hàm, cùng đơn vị u). Không có con nào như vậy thì trả `false`, Cast giữ nguyên như hôm nay khi không có thú. Sửa chú thích JSDoc của hàm cho khớp.
2. Nếu ảnh chụp F0 có một hàm lọc riêng, dùng chung một hàm cho cả hai chỗ, để không lệch nhau.
3. Trong `tests/sim/twin-pearl-sweep.test.ts`, đổi ca A1 từ `it.fails` sang `it`. Ca mới kiểm:
   - với hai thú ở giữa dải, `resolveTwinPearl` trả `false`, không có bản ghi lần tung mới, không tốn hồi chiêu;
   - thêm một thú vào dải đất thì giải được, và có đòn dương ở F0 hoặc F1.

   Bỏ chú thích "thiết kế mơ hồ" và ghi rằng Claude đã chốt theo §9.2.
4. Không đổi gì khác. Trạng thái khi cờ tắt không đổi: test băm `1a78a82` phải còn qua.

### Được ghi
- `src/sim/twin-pearl.ts`, chỉ `resolveTwinPearl` và hàm lọc dùng chung nếu cần;
- `tests/sim/twin-pearl-sweep.test.ts`.

### Cấm
- Sửa file khác; mọi lệnh git trừ `status`, `diff`, `log`, `show`; chạy Vitest hay Vite thiếu cờ `--no-cache --configLoader runner`.

## Kiểm bắt buộc (trong worktree)
1. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4 tests/sim/twin-pearl.test.ts tests/sim/twin-pearl-sweep.test.ts`: mọi test qua, không còn `it.fails`.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: chỉ còn hỏng đúng một test đã biết, `tests/lab/orbit-cutin.test.ts`, đã sửa trên `main`.
3. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
4. `git status --short` và `git diff --stat -- src/sim/twin-pearl.ts`: chỉ thêm thay đổi ở hai file được ghi.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
