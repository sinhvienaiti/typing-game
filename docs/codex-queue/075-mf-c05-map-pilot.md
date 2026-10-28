# Phiếu 075 · Bản thử bản đồ Rồng L2-cau · MF-C05: Metadata kit, `captureBands` và `check-kit`

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C05. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/075-report.md` **trong worktree** `/Users/toandx/htdocs/typing-game-wt/map-codex`.

## Luật chung: 1.2 Mọi phiếu mã Codex ở repo cha

- **Thư mục làm việc:** worktree `/Users/toandx/htdocs/typing-game-wt/map-codex`, nhánh `map-factory` (MAP_FACTORY §9.4).
- **Chỉ được ghi:** đúng các đường dẫn phiếu liệt kê, cộng file báo cáo.
- **Cấm:**
  - lệnh git có ghi (`add`, `commit`, `checkout`, `stash`, `reset`, `clean`…); `git status`, `git diff`, `git archive` được phép;
  - mạng, trình duyệt, dev server, server bất kỳ;
  - ghi dưới `games/**` (chỉ đọc; bộ đọc lấy nội dung game bằng `git archive` ở commit ghim);
  - cài gói npm hay pip; chỉ Node 24 có sẵn và `node_modules` của `shared/game-kit` (TypeScript 6.0.3, vitest);
  - đọc hay ghi Tu Tiên;
  - `Math.sin/cos/tan/atan2/pow/hypot/exp/log/cbrt/random`, `Date`, `performance`, `**` trong `shared/game-kit/map/` (ngoài `*.test.ts`); số lẻ ở đầu ra lõi (đơn vị cm, ‰, độ nguyên).
- **Kiểm chung, bắt buộc:**
  - **KC1 cây Git:** lưu `git status --short --untracked-files=all` lúc đầu; lúc cuối chỉ được **thêm hoặc sửa** đường dẫn cho phép; không dòng ` M`, ` D` mới ngoài phạm vi.
  - **KC2 lint tất định:** test lint của 027 đạt trên mọi file mới trong `map/`.
  - **KC3 test:** `pnpm --dir shared/game-kit exec vitest run map` và `node --test tools/map-factory/test/*.test.mjs` đạt; `tsc -p shared/game-kit/map/tsconfig.json` đạt.
  - **KC4 tất định:** chạy hai lần (hai tiến trình Node) cho cùng từng byte; in băm.
- **Quá một giờ:** dừng ở phần đã xong, ghi phần còn lại vào báo cáo.
- **Báo cáo:** tiếng Việt; file tạo hay sửa; kết quả từng kiểm kèm số in ra; thời gian chạy.

## MF-C05 · [codex-code] Metadata kit, `captureBands` và `check-kit`

**Cần trước:** MF-C04.

**Chỉ được ghi:** `tools/map-factory/registry/kits/{pine-river,meadow}.json`, `tools/map-factory/lib/kit.mjs`, `tools/map-factory/cli.mjs` (lệnh `check-kit`), `tools/map-factory/test/kit.test.mjs`, `tools/map-factory/test/fixtures/kits/*.json`.

**Việc:**
- Mỗi proto: `role` (enum: `tree`, `bush`, `rock`, `log`, `landmark`, `path-prop`, `cliff`, `water-edge`, `set-piece`, `tuft`), `nominalHeightCm`, `footprintCm`, `clearanceCm`, `hueClass` (`green`, `violet`, `warm`, `neutral`; không có `signal-*`), `castsShadow`, `tintable`, `lodClass`, `maxTris`. Giá trị lấy từ bảng Claude ghi trong phiếu.
- Mỗi kit: `palette`, `captureBands` (pine-river theo kế hoạch §2.9 Q5), `lighting` mặc định, tham số bố cục.
- `check-kit <kit>`: kiểm đủ trường, enum, dải.

**Kiểm (bắt buộc):** KC1, KC3, và:
1. `check-kit` thoát 0 với hai kit.
2. Fixture thiếu trường, `role` lạ, `hueClass: "signal-red"` thoát 1 với đúng mã.
3. Mọi GLB trong sổ 025 của `public/assets/dragon-hold/models/m0b/props` có mục; chiều cao bao (đọc từ đầu ra sổ 025, không mở GLB) lệch `nominalHeightCm` ≤ 20 %, hoặc được in ra.

**Xong khi:** ba kiểm đạt.
