# Phiếu 079 · Bản thử bản đồ Rồng L2-cau · MF-C23: Lint chiến thuật B: ô, ô nhà, cung bay

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C23. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/079-report.md` ở repo cha.

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

## MF-C23 · [codex-code] Lint chiến thuật B: ô, ô nhà, cung bay

**Cần trước:** MF-C22.

**Chỉ được ghi:** `scripts/maps/lint-map.ts`, `scripts/maps/metrics-slots.ts`, `tests/maps/lint-slots.test.ts`.

**Việc:** luật H5–H11 và số mềm S4–S9: ô bẫy (số, khoảng cách, ≥ 8 m, không trong lội, r ≤ 25,5 m trừ `hold`), phần bẫy trong vùng chữ E09 (hồ sơ tham chiếu), điểm chặn, vai trò ô nhà và độ phủ ở 6–16 m, ô chung, ô chết, độ lộ với chỗ đứng của E11 (12 m) và E01 (10 m), tầm với tới đầu cung bay (Net Launcher 10 m, Owl Hunter 12 m, Watchtower 16 m), số ô so với vàng (in để bot kiểm G13b). Vai trò đọc từ trường `role` nếu có; không có thì suy và báo `role-missing`.

**Kiểm (bắt buộc):** KR1–KR4, và trên L2-cau (±0,05 m):
1. `cau-t1` ở r 26,32: H5 trượt, mã `trap-outside-ring`; dời trong RAM sang 5 m: r 25,35, đạt.
2. Ở 10 m: `h-nw` 7,4 m Cầu và 6,1 m Suối (ô chung duy nhất); `h-se` 0 m (`pad-no-lane`); `h-e` 12,9 m Cầu; `h-w` 18,3 m Suối.
3. Net Launcher tới đầu cung bay chỉ từ `cau-t4` (9,4 m).
4. Đúng năm phát hiện của kế hoạch §3.4 cổng D, không thêm không bớt.
5. Bản đồ hỏng tổng hợp trượt đúng H5, H6, H7, H8.

**Xong khi:** năm kiểm đạt.
