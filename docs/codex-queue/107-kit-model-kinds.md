# Phiếu 107 · Kit · `ModelLibrary` nhận thêm loại model của từng game

**Vì sao:** bước 1C của Lời Gọi (làn L, C6) cần nạp nhà, bộ cấp và đạn từ manifest model của chính game. Hôm nay `shared/game-kit/three/model-loader.ts` (`parseEntry`) bỏ mọi mục có `kind` không nằm trong `MODEL_KINDS`, và danh sách đó chỉ có các loại của Space: ships, enemies, bosses, skills, items, heroes, guides, units, props. Vì vậy các mục `buildings`, `kits`, `projectiles` trong manifest của Lời Gọi bị bỏ âm thầm; chỉ `props` đọc được. Điều phối viên quyết ngày 28/10: thêm một tùy chọn, giữ tương thích ngược.

**Báo cáo:** `docs/codex-queue/107-report.md`, và thư mục `docs/codex-queue/107/`.

## Luật chung (phiếu mã)

- **cwd và nơi làm:** repo cha `/Users/toandx/htdocs/typing-game`, thư mục `shared/game-kit/three/`.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- **Cấm:**
  - sửa bản chép kit trong game (`games/*/src/kit/**`);
  - chạy `kit:sync` (Claude làm sau);
  - sửa file ngoài danh sách dưới đây;
  - dev server, trình duyệt; media;
  - đụng Tu Tiên.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn.

**Chỉ được ghi:**
- `shared/game-kit/three/model-loader.ts`, `model-contracts.ts`, `index.ts`;
- `shared/game-kit/three/models.test.ts`;
- `shared/game-kit/DRIFT.md`: thêm một mục ngắn, sửa gì so với bản nguồn của Space. Phiếu 102 có thể đã thêm một mục trước: giữ nguyên mục đó;
- báo cáo và `docs/codex-queue/107/`.

## Việc

1. **Tùy chọn mới của `ModelLibrary`:** `kinds?: readonly string[]`, các loại nhận **thêm** ngoài `MODEL_KINDS`.
   - Không truyền thì hành vi y như hôm nay.
   - Tên loại phải khớp `^[a-z][a-z0-9-]*$`. Tên sai thì constructor ném lỗi có nêu tên đó.
2. `parseModelManifest(raw, manifestUrl, extraKinds?)` và `parseEntry` nhận danh sách thêm đó. Giữ nguyên chữ ký cũ: tham số mới là tùy chọn.
3. **Kiểu:**
   - `ModelManifestEntry.kind` thành `string`;
   - `entry(kind, id)` và `url(kind, id, quality)` của `ModelLibrary` nhận `kind: string`;
   - giữ `ModelKind`, `MODEL_KINDS`, `isModelKind`, `MODEL_CONTRACTS` như cũ, vì hợp đồng socket và clip vẫn chỉ cho các loại của Space;
   - mọi chỗ khác trong kit đang dùng `entry.kind` như `ModelKind` (ví dụ tra `MODEL_CONTRACTS[entry.kind]`) phải xử lý được loại lạ: không có hợp đồng thì bỏ qua kiểm socket và clip, không ném lỗi. Tìm hết bằng `grep -rn "\.kind" shared/game-kit/three` và ghi vào báo cáo.
4. **Test** trong `models.test.ts`:
   - manifest có một mục `buildings/barracks`: không có `kinds` thì `entry("buildings", "barracks")` trả `null`; có `kinds: ["buildings"]` thì trả mục đó, đúng `tiers` và `size`;
   - mục `props` vẫn đọc được trong cả hai trường hợp;
   - `kinds: ["Bad Name"]` ném lỗi;
   - mọi test cũ vẫn xanh.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. `pnpm --dir shared/game-kit test` xanh; ghi số test trước và sau.
2. `pnpm --dir shared/game-kit typecheck` sạch.
3. **Tương thích:** chép tạm `shared/game-kit/three` đè vào `src/kit/three` của một bản chép **tạm** của mỗi game dùng kit three (`games/dragon-hold`, `games/typing-survival`), đặt ngoài repo cha (`$TMPDIR/kit107/<game>`, không có `node_modules`, `ln -s` tới `node_modules` của game). Ở đó chạy `./node_modules/.bin/tsc --noEmit`: sạch. Ghi kết quả, rồi xóa thư mục tạm bằng `rm -rf "$TMPDIR/kit107"`. Không sửa cây thật của game.
4. **Đột biến:** bỏ việc nhận `extraKinds` trong `parseEntry` thì test `buildings` phải đỏ; trả lại thì xanh.
5. `git status --short -uall -- shared/game-kit`: chỉ các file trong "Chỉ được ghi".

**Xong khi:** năm mục đạt. Sau đó Claude chạy `kit:sync` vào worktree `games/.wt-td-1c` (Lời Gọi, làn L), rồi kiểm C6 nạp được `buildings`.
