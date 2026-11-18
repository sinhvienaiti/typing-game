# Phiếu 078 · Bản thử bản đồ Rồng L2-cau · MF-C22: Lint chiến thuật A: hình học làn và thời gian

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C22. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/078-report.md` ở repo cha.

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

## MF-C22 · [codex-code] Lint chiến thuật A: hình học làn và thời gian

**Cần trước:** MF-C20.

**Chỉ được ghi:** `scripts/maps/lint-map.ts`, `scripts/maps/metrics-lane.ts`, `package.json` (thêm `dh:map-lint`), `tests/maps/lint-lane.test.ts`.

**Việc:** dùng `compileLanes`, `alongAtRadius`, `inWordZone`, hằng số `rules.ts`. Tính: độ dài, bán kính cổng, độ quanh co, các khúc và góc, đơn điệu hướng tâm trong 26 m, điểm vào vòng, thời gian mỗi lớp quái (trước vùng, trong vùng, tổng; bị chặn bởi T_a hay vòng) ở hồ sơ tham chiếu (k = 1, biên 1,219), sàn Q, khoảng cách làn và chỗ cắt, phương vị đầu làn, nón 60° và đĩa 4 m, tỉ lệ nghẽn, thời gian lội. Luật cứng H1–H4, H12 (kế hoạch §2.2). Ra JSON.

**Kiểm (bắt buộc):** KR1–KR4, và trên L2-cau (±0,05 m, ±0,5°, ±0,1 s):
1. Độ dài 24,59 / 25,29 m; cổng r 30,22 / 30,81 m; độ quanh co 1,015 / 1,019.
2. Khúc Suối 21,2°; vào vòng ở 4,35 / 4,95 m; khoảng cách làn nhỏ nhất 9,15 m; phương vị đầu làn 4° / 266° (= −94°).
3. Cung bay 24,3 m, kết thúc ở r 7,5.
4. Tỉ lệ cầu 1,13 (H12 trượt, mã `choke-not-real`); lội ×1,43 trên 7,1 m.
5. E09: trước vùng 2,5 / 2,9 s, tổng 12,3 / 12,6 s; vùng chữ E09 bắt đầu ở 5,09 m dọc Đường Cầu.
6. Thời gian trước vùng của lint **bằng đúng** `zoneDelayMs` của `waves.ts` cho mọi làn × quái.
7. Bản đồ hỏng tổng hợp trượt đúng luật: làn 22 m (H1), làn đi ra rồi vào lại (H2), hai làn cách 6 m (H3).
Số nào lệch fixture: dừng và báo; Claude kiểm lại fixture trước khi bên nào đổi.

**Xong khi:** bảy kiểm đạt.
