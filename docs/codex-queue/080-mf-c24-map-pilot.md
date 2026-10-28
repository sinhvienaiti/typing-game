# Phiếu 080 · Bản thử bản đồ Rồng L2-cau · MF-C24: `prepare-ground` và `prepare-decals`

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C24. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/080-report.md` ở repo cha.

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

## MF-C24 · [codex-code] `prepare-ground` và `prepare-decals`

**Cần trước:** không.

**Chỉ được ghi:** `scripts/assets/prepare-ground.mjs`, `scripts/assets/prepare-decals.mjs`, `package.json` (hai lệnh), `tests/assets/prepare-ground.test.mjs`, `src/view/ground-manifest.ts` (bộ đọc manifest, chưa nối vào phần vẽ).

**Việc:** từ `art-src/ground/<kit>/` và `art-src/decals/<kit>/` ra `public/assets/dragon-hold/{ground,decals}/<kit>/` theo mẫu `prepare-models` (cỡ, WebP), kèm manifest (tên, md5, byte). Test chạy trên ảnh tổng hợp trong thư mục tạm; **không chạy trên media thật** (Claude chạy).

**Kiểm (bắt buộc):** KR1–KR4, và:
1. Manifest tất định (hai lần cùng byte).
2. `git check-ignore` trả đường dẫn đầu ra (media không vào Git).
3. `grep -rn "/art-src/" src/` không in gì từ file mới.

**Xong khi:** ba kiểm đạt.
