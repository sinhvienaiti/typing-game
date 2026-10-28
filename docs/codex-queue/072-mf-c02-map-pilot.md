# Phiếu 072 · Bản thử bản đồ Rồng L2-cau · MF-C02: Bộ đọc `dragon-hold@2`: tách `simHash` và `viewHash`

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C02. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/072-report.md` **trong worktree** `/Users/toandx/htdocs/typing-game-wt/map-codex`.

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

## MF-C02 · [codex-code] Bộ đọc `dragon-hold@2`: tách `simHash` và `viewHash`

**Cần trước:** không.

**Chỉ được ghi:** `tools/map-factory/adapters/dragon-hold*.mjs`, `tools/map-factory/test/adapters.test.mjs`, `tools/map-factory/test/fixtures/gameplay/dragon-hold*.json`.

**Việc:**
- `simHash` = băm JSON chuẩn của: bệ, làn đã biên dịch (`compileLanes`, u), bề rộng, đoạn cầu và lội, cung bay, ô.
- `viewHash` = băm của: `river` (điểm, bề rộng, nông), `terrain`, `camera`.
- Giữ `@1` đọc được (băm cũ đổi tên `hashLegacy`) cho spec cũ một phiên bản.

**Kiểm (bắt buộc):** KC1, KC3, KC4, và:
1. Sửa một bề rộng sông trong RAM: chỉ `viewHash` đổi.
2. Sửa `atM` của một ô trong RAM: chỉ `simHash` đổi.
3. `simHash` của L2-cau ở commit 83da970 và 02fe9c7: in cả hai; nếu khác, in trường khác nhau (dữ liệu làn và ô không đổi thì phải bằng).
4. `git status --porcelain` của checkout chính `games/dragon-hold` trước và sau giống hệt.
5. `canonicalJson` cho cùng đầu ra như trước với các trường không đổi.

**Xong khi:** năm kiểm đạt.
