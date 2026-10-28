# Phiếu 082 · Bản thử bản đồ Rồng L2-cau · MF-C07: MapSpec v1: mã lỗi và mẫu hỏng

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C07. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/082-report.md` **trong worktree** `/Users/toandx/htdocs/typing-game-wt/map-codex`.

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

## MF-C07 · [codex-code] MapSpec v1: mã lỗi và mẫu hỏng

**Cần trước:** MF-C06.

**Chỉ được ghi:** `shared/game-kit/map/spec.ts`, `spec.test.ts`, `tools/map-factory/test/fixtures/bad-spec/v1-*.json`, `tools/map-factory/cli.mjs` (`validate` đọc v1).

**Việc:** `validateSpec` cho v1 với mã lỗi.

**Kiểm (bắt buộc):** KC1–KC3, và 10 spec hỏng thoát 1 với đúng mã: preset ánh sáng lạ; `sunElevDeg` ngoài 30–70; số thùy quầng ngoài 3–5; `rimCm` ngoài 15–25; `accent.minLaneGapCm` < 900; `grove.gapCm` < 800; số sự sống quá ngân sách; thiếu `simHash`; tọa độ trong `brief`; lối mòn không có `destination`.

**Xong khi:** 10 mẫu hỏng đúng mã, 2 mẫu tốt thoát 0.
