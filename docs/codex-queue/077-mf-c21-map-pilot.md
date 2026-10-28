# Phiếu 077 · Bản thử bản đồ Rồng L2-cau · MF-C21: Báo cáo cân bằng: cột theo làn, theo ô, theo Herb Hut

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C21. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/077-report.md` ở repo cha.

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

## MF-C21 · [codex-code] Báo cáo cân bằng: cột theo làn, theo ô, theo Herb Hut

**Cần trước:** MF-C20.

**Chỉ được ghi:** `scripts/balance/report.ts`, `scripts/balance/meter.ts` (chỉ thêm bộ đếm), `tests/balance/report-columns.test.ts` (mới).

**Việc:** chỉ báo cáo, không đụng sim:
- mỗi làn: tỉ phần sức ép đất, số giết, sát thương lên Rồng, số lọt;
- mỗi ô: tỉ lệ được đặt, tỉ phần giết;
- Herb Hut: số nhịp theo ô nhà;
- nền cho G14: tỉ phần món trong các bộ tốt nhất.

**Kiểm (bắt buộc):** KR1–KR4, và:
1. Trên 20 seed, tổng theo làn và theo ô bằng tổng hiện có.
2. Cùng seed, tỉ phần đợt 7 của Đường Cầu ra 58,2 % ±1 điểm (Phát hiện 40).

**Xong khi:** hai kiểm đạt.
