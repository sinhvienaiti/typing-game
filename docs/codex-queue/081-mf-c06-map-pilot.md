# Phiếu 081 · Bản thử bản đồ Rồng L2-cau · MF-C06: MapSpec v1: kiểu và chuyển từ v0

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C06. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/081-report.md` **trong worktree** `/Users/toandx/htdocs/typing-game-wt/map-codex`.

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

## MF-C06 · [codex-code] MapSpec v1: kiểu và chuyển từ v0

**Cần trước:** CL-02.

**Chỉ được ghi:** `shared/game-kit/map/spec.ts`, `shared/game-kit/map/spec.test.ts`, `shared/game-kit/map/spec-v1.ts` (nếu tách).

**Việc:** thêm các khối (kế hoạch §2.10): `gameplay {adapter, commit, simHash, viewHash}`; `brief` (enum và phương vị, không tọa độ); `lighting {preset, sunAzimuthDeg, sunElevDeg, hemiGround, exposurePermille, mistStartCm}`; `scene` (mỗi vật lớn là `"auto"` hoặc ghim: `cliff`, `pond`, `openSector`, `forestEdge`, `groves`, `accents`, `paths[]` với `tier` và `destination`, `landmarks`, `gates[]` với `source` và `telegraph`); `layers.life`; `critics` (ghi đè ngưỡng, bắt buộc có `reason`); `approved` (băm từng lớp). Viết `migrateV0toV1`.

**Kiểm (bắt buộc):** KC1–KC3, và:
1. Hai spec v0 mẫu chuyển sang v1 và hợp lệ.
2. Chuyển hai lần cho cùng byte.
3. Spec v1 tối thiểu (mọi vật lớn `auto`) hợp lệ.

**Xong khi:** ba kiểm đạt.
