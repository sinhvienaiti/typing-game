# Phiếu 271b · Tu Tiên · Test: kiểm độc lập mã Song Long của phiếu 271 theo thiết kế §9

**Loại việc:** test (`gpt-6.1-sol`, mức `xhigh`). Codex viết test và chạy, **không sửa mã**. Đây là bước kiểm độc lập trước khi Claude gộp phiếu 271: một model khác đọc thiết kế, viết test của riêng mình, rồi tìm chỗ mã lệch thiết kế.

**Báo cáo:** tin nhắn cuối (`.local/codex-runs/271b-tt-twin-pearl-test-sweep/last.md`). Claude chép vào `docs/codex-queue/271b-report.md`.

**Đường duyệt:** Claude viết lúc 20:50 ngày 04/11, khi làn Codex trống. Đặc tả là thiết kế đã duyệt (§9.0–§9.11, hai lượt PASS S3 và S4 cho phiếu 1). Không có quyết định thiết kế mới nào.

## Bối cảnh
- Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/271/section9-design.md` §9.2–§9.6 và §9.12 A–D.
- Mã cần kiểm: worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide`, nhánh `codex/twin-pearl-fieldwide`. Mã của phiếu 271 nằm ở đây, chưa commit: `src/content/data/twin-pearl.ts`, `src/sim/twin-pearl.ts`, `src/sim/combat.ts`, `src/lab/twin-pearl-greybox.ts`, `src/lab/skills-main.ts`. Test của phiếu 271 là `tests/sim/twin-pearl.test.ts`, 37 test đều qua.
- Lỗi đã biết, ngoài phạm vi: `tests/lab/orbit-cutin.test.ts` hỏng ở worktree này. Đã sửa trên `main` (`2381c7b`).

## Làm ở đâu (cwd là worktree trên)
### Được ghi
- `tests/sim/twin-pearl-sweep.test.ts` (tạo mới), chỉ file này.

### Cấm
- Sửa bất kỳ file nào khác, nhất là mã trong `src/` và `tests/sim/twin-pearl.test.ts`.
- Mọi lệnh git trừ `status`, `diff`, `log`, `show`.
- Chạy Vitest hay Vite thiếu cờ `--no-cache --configLoader runner`. Mở cổng mạng.

## Việc
1. **Tự đọc thiết kế** §9.2–§9.6 (chia hai bên, ngọc, neo, đường, năm pha và khung, khối trúng, trần, ngân sách). Lập danh sách các bất biến **kiểm được bằng số** mà `tests/sim/twin-pearl.test.ts` chưa kiểm, hoặc kiểm yếu hơn thiết kế. Ví dụ:
   - không đòn nào ngoài khung pha;
   - ngân sách mỗi bên và mỗi phần không âm và không vượt sau mọi tick;
   - mỗi thú tối đa 3 đòn, mỗi loại 1, cách nhau ≥ 20 tick;
   - đối xứng và tất định trên bố cục ngẫu nhiên có hạt giống cố định;
   - không có số thực trong trạng thái;
   - các mốc khung F0/F1/F3/F30/F49/F57/F77/F102 khớp bảng;
   - sát thương chỉ khi có thú nhận được.
2. **Viết test cho từng bất biến** trong `tests/sim/twin-pearl-sweep.test.ts`, dùng các hàm dựng thế giới đã có trong `tests/sim/twin-pearl.test.ts` (chép phần cần, không import file test). Thêm một vòng quét: 200 bố cục ngẫu nhiên, hạt giống 1–200, 10–60 thú trên sân tổng hợp 40 × 40 m của §9.12 D, mỗi bố cục một lần tung tới F102. Kiểm mọi bất biến ở mỗi tick.
3. **Chạy.** Một test hỏng thì **không sửa mã và không nới test** để qua. Ghi lại: bất biến nào, bố cục nào (hạt giống), tick nào, số đo được so với thiết kế, đoạn thiết kế (§ và dòng) mà mã lệch. Nếu chính thiết kế mơ hồ ở chỗ đó, ghi "thiết kế mơ hồ" kèm lý do. Để test hỏng ở dạng `it.fails` hoặc `it.skip`, kèm chú thích dẫn tới báo cáo, để bộ test vẫn chạy được.

## Kiểm bắt buộc
1. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4 tests/sim/twin-pearl-sweep.test.ts tests/sim/twin-pearl.test.ts`: chạy xong, có số test qua, hỏng và đánh dấu.
2. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
3. `git status --short`: chỉ có thêm `tests/sim/twin-pearl-sweep.test.ts`, ngoài các thay đổi sẵn có của phiếu 271.

## Báo cáo
- Danh sách bất biến kèm trạng thái (qua, hỏng, mơ hồ) và bằng chứng.
- Số test, thời gian chạy vòng quét.
- Ba lỗi nặng nhất, nếu có, xếp theo mức ảnh hưởng tới người chơi.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
