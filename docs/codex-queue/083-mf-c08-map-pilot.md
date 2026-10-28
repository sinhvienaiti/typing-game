# Phiếu 083 · Bản thử bản đồ Rồng L2-cau · MF-C08: Khung camera trên mặt đất (`frame.ts`)

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C08. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/083-report.md` **trong worktree** `/Users/toandx/htdocs/typing-game-wt/map-codex`.

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

## MF-C08 · [codex-code] Khung camera trên mặt đất (`frame.ts`)

**Cần trước:** CL-02.

**Chỉ được ghi:** `shared/game-kit/map/frame.ts`, `frame.test.ts`.

**Việc:** từ yaw, pitch, khoảng cách, `lookM`, fov dọc, tỉ lệ khung và danh sách chữ nhật HUD (px ở 1280×720 và 1920×1080), tính đa giác khung trên mặt đất (y = 0) và đa giác "khung trừ HUD". Hàm `insideShare(polygon, frame)` (tỉ lệ diện tích, ‰). Lượng giác bằng bảng tra số nguyên theo độ (‰); thử với `Math` chỉ trong test.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Camera mặc định L2-cau (yaw 0, pitch 55, khoảng cách 95, `lookM` [0, −4], fov dọc 30°, 16:9; Claude xác nhận với `stage.ts` khi xếp): đáy khung z ≈ +22,2 m, đỉnh z ≈ −42,2 m, nửa bề ngang ở z = 0 ≈ 44,2 m, mỗi số ±0,3 m. (Ảnh đo được: x ±43, đáy +23.)
2. So với cách tính số thực trong test: lệch ≤ 10 cm ở mọi đỉnh trên 50 camera ngẫu nhiên.
3. `insideShare` của một đĩa nằm trọn trong khung = 1000 ‰; nằm trên mép = 500 ‰ ±10.

**Xong khi:** ba kiểm đạt.
