# Phiếu 073 · Bản thử bản đồ Rồng L2-cau · MF-C03: Đọc PNG bằng `node:zlib` và thu nhỏ hộp

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C03. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/073-report.md` **trong worktree** `/Users/toandx/htdocs/typing-game-wt/map-codex`.

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

## MF-C03 · [codex-code] Đọc PNG bằng `node:zlib` và thu nhỏ hộp

**Cần trước:** không.

**Chỉ được ghi:** `tools/map-factory/lib/png.mjs`, `tools/map-factory/test/png.test.mjs`, `tools/map-factory/test/fixtures/png/*` (PNG nhỏ do test tự sinh và ghi; ≤ 20 KB mỗi file).

**Việc:**
- `decodePng(buf)`: PNG 8 bit, RGB hoặc RGBA, không interlace, mọi bộ lọc dòng (0–4). Kiểu khác trả lỗi có mã (`png-unsupported-<kiểu>`).
- `boxDownscale(rgba, w, h, 384, 216)`: trung bình vùng (diện tích), ra RGB.
- `readRaw384(buf)`: đọc RGB thô 384×216 (định dạng file `.rgb` của script đo ảnh 28/10).

**Kiểm (bắt buộc):** KC1, KC3, KC4, và:
1. Bộ mã hóa PNG nhỏ trong test (zlib `deflateSync`) ghi ảnh đã biết với cả 5 bộ lọc; giải mã ra đúng từng byte.
2. Thu nhỏ ảnh 768×432 hai màu kẻ ô 2 px ra màu trung bình đúng ±1/255.
3. PNG 16 bit và interlace báo đúng mã lỗi.

**Xong khi:** ba kiểm đạt.
