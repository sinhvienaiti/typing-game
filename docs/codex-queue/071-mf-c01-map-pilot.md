# Phiếu 071 · Bản thử bản đồ Rồng L2-cau · MF-C01: Kit sync không làm hỏng Vite với `map/tsconfig.json`

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C01. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/071-report.md` **trong worktree** `/Users/toandx/htdocs/typing-game-wt/map-codex`.

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

## MF-C01 · [codex-code] Kit sync không làm hỏng Vite với `map/tsconfig.json`

**Cần trước:** CL-02 (lõi đã gộp).

**Chỉ được ghi:** `scripts/sync-game-kit.mjs`, `shared/game-kit/map/tsconfig.json`, `scripts/test/sync-game-kit.test.mjs` (tạo mới nếu chưa có).

**Việc:** `map/tsconfig.json` hiện `extends: "../tsconfig.json"`; khi chép vào `games/<id>/src/kit/map/` thì Vite báo `failed to resolve "extends"`. Chọn một: kit sync bỏ qua `map/tsconfig.json`; hoặc tsconfig của map tự đứng (chép các tùy chọn cần, giữ `erasableSyntaxOnly`). Ghi lý do chọn.

**Kiểm (bắt buộc):** KC1–KC3, và:
1. Test tạo một game mẫu trong thư mục tạm (`os.tmpdir()`), chạy sync, rồi `vite build` (Vite của `shared/game-kit` hoặc của game mẫu nếu có sẵn, không cài): thành công.
2. `verify-kit` (sha256) đạt trên game mẫu.
3. Mọi module kit khác chép ra giống hệt từng byte trước và sau sửa.
4. Lint 027 vẫn bắt `enum` và `namespace` khi dịch trong RAM với tùy chọn của map.

**Xong khi:** bốn kiểm đạt; diff chỉ ở ba file trên.
