# Phiếu 076 · Bản thử bản đồ Rồng L2-cau · MF-C20: Đợt quái theo bản đồ; test bản đồ chạy mọi bản đồ

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C20. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/076-report.md` ở repo cha.

## Luật chung: 1.3 Mọi phiếu mã Codex ở worktree Rồng

- **Thư mục làm việc:** `games/.wt-dh-mapcodex` (repo Rồng), nhánh `map-codex` tách từ `main` 02fe9c7, do Claude tạo ở CL-02. Phụ thuộc cài như các worktree `.wt-dh-*` khác.
- **Chỉ được ghi:** đúng các đường dẫn phiếu liệt kê **bên trong worktree này**, cộng file báo cáo ở repo cha `docs/codex-queue/<số>-report.md`.
- **Cấm:** như 1.2, cộng:
  - ghi vào checkout chính `games/dragon-hold` hay worktree khác (`.wt-dh-mappilot` là của Claude);
  - `pnpm media:push`, `pnpm media:pull`, `pnpm dev`, kịch bản trình duyệt (`scripts/visual/**`);
  - sửa `tests/golden/**` (golden chỉ Claude đổi, có chủ ý).
- **Kiểm chung, bắt buộc:**
  - **KR1 cây Git:** như KC1, trong worktree.
  - **KR2 golden:** `md5 -r tests/golden/*` trước và sau giống hệt; `pnpm test` đạt.
  - **KR3 check:** `pnpm check` (sha kit, test, tsc, vite build) đạt.
  - **KR4 tất định:** như KC4 với lệnh của phiếu.

## MF-C20 · [codex-code] Đợt quái theo bản đồ; test bản đồ chạy mọi bản đồ

**Cần trước:** CL-02.

**Chỉ được ghi:** `src/content/data/waves.ts`, `src/content/data/stages.ts` (chỉ nếu cần tra bản đồ theo ải), `tests/content/map.test.ts`, `tests/content/waves-map.test.ts` (mới).

**Việc:** `waves.ts` hôm nay import `MAP_L2_CAU` để tính `zoneDelayMs`. Đổi thành hàm nhận MapDef (ví dụ `wavePlanFor(map)`), bản đồ tra từ ải. `map.test.ts` lặp qua mọi mục của `MAPS`. Không đổi hành vi.

**Kiểm (bắt buộc):** KR1–KR4, và:
1. Bảng `zoneDelayMs` mọi làn × quái trên L2-cau bằng đúng giá trị cũ (test so bảng ghi trước khi sửa).
2. Một MapDef lật gương (x → −x) trong test cho cùng bảng.
3. `pnpm dh:balance --seeds=20 --json` cho cùng đầu ra trước và sau (in md5).

**Xong khi:** ba kiểm đạt.
