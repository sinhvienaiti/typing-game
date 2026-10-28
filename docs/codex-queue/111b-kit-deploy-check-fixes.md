# Phiếu 111b · Kit · Hai sửa nhỏ cho `check-pack.mjs` sau lần chạy thật

**Vì sao:** điều phối viên chạy bộ kiểm của phiếu 111 trên hai bản build thật (29/10) và gặp hai chỗ phải sửa.
1. **Báo nhầm:** `games/.wt-ts-codex/dist --game typing-survival` báo `missing-vocabulary` cho level 4–100. `vocabulary/index.json` (bản ghim nguyên văn từ repo cha) liệt kê đủ 100 level, nhưng Last Line chỉ mang level 1–3 theo `vocab.config.json` và `vocab-manifest.json`. Game chỉ tải level 1–3, nên các level còn lại không phải lỗi.
2. **Thiếu tùy chọn:** `games/.wt-dh-codex/dist --game dragon-hold` báo `local-host`. Đó là địa chỉ cổng mặc định `https://typing-game.local` trong `src/app/portal.ts`. Với bản demo chạy ở máy chủ dự án (nginx, `typing-game.local`), địa chỉ này đúng. Chỉ bản đưa lên mạng mới phải cấm.

**Báo cáo:** `docs/codex-queue/111b-report.md` (ghi ở repo cha).

## Luật chung (phiếu mã)

- **cwd và nơi làm:** repo cha `/Users/toandx/htdocs/typing-game`.
- **Chỉ được ghi:**
  - `shared/game-kit/tools/deploy/check-pack.mjs`, `check-pack.test.mjs`;
  - `shared/game-kit/DRIFT.md` (sửa dòng của 111 hoặc thêm một dòng);
  - báo cáo và `docs/codex-queue/111b/`.
- **Cấm:**
  - mọi lệnh git có ghi;
  - sửa file trong `games/**`;
  - `kit:sync`; dev server, trình duyệt; mạng;
  - đụng Tu Tiên.

## Việc

1. **`missing-vocabulary`:**
   - Có `vocabulary/vocab-manifest.json` thì chỉ các file trong manifest là bắt buộc, cùng sha256 khớp manifest.
   - Các `levels[].file` của `index.json` không có trong manifest và không có trong gói thì đưa vào `report.vocabularyNotShipped` (số lượng và 5 tên đầu), không phải lỗi.
   - Không có manifest thì giữ luật cũ.
2. **Cờ CLI `--allow-local-host`** và tùy chọn API `{ allowLocalHost: true }`. Khi bật, `typing-game.local` không là lỗi; số lần gặp được ghi vào `report.localHost`. Mặc định vẫn là lỗi.
3. **Test:**
   - gói có manifest chỉ 3 level, `index.json` 100 level → đạt, `vocabularyNotShipped` là 97;
   - manifest có một level mà gói thiếu → `missing-vocabulary`;
   - `typing-game.local` khi có cờ → đạt, có `report.localHost`; khi không có cờ → lỗi như cũ.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. `node --test shared/game-kit/tools/deploy/check-pack.test.mjs`: xanh; ghi số ca trước và sau.
2. Chạy lại trên hai bản build trên (chỉ đọc): Last Line đạt; Dragonhold có cờ thì đạt, không có cờ thì vẫn báo `local-host`. Ghi đầu ra.
3. **Đột biến:** bỏ việc dùng manifest thì ca "3 level" phải đỏ.
4. `git status --short -uall -- shared/game-kit`: chỉ các file trong "Chỉ được ghi".

**Xong khi:** bốn mục đạt.
