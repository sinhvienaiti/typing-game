# Phiếu 080 · Bản thử bản đồ Rồng L2-cau · MF-C24: `prepare-ground` và `prepare-decals`

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C24. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/080-report.md` ở repo cha.

**Thay đổi ngày 28/10 (điều phối viên), thắng mọi chỗ khác trong phiếu:**
- Phiếu được chạy lại vì là cổng G7 của map 1 Rồng: bản build production không được đọc `/art-src/`. Hôm nay chỉ dev mới nạp được nét ô đất và decal.
- **Worktree là `games/.wt-dh-codex`** (nhánh `dh-codex` tách từ `main` 02fe9c7, `node_modules` đã cài, `public/assets` là symlink tới media của cây chính). Không dùng `games/.wt-dh-mapcodex`: worktree đó còn thay đổi chưa commit của phiếu 076 đang tạm dừng, và phiếu này **không được đụng** tới nó.
- Mọi chỗ trong phiếu ghi `.wt-dh-mapcodex` hay nhánh `map-codex` thì hiểu là `.wt-dh-codex` và nhánh `dh-codex`.
- Kiểm chung KR1–KR4 và KC1 ở `docs/tools/map-factory/TICKETS.md` §1.2–1.3.
- Được ghi thêm `dist/` và cache trong `node_modules/` (Git bỏ qua). Dùng `git status --short -uall` cho KR1.
- **Không ghi vào `public/assets/`** của worktree: đó là symlink tới media thật của cây chính. Hai script nhận thư mục vào và ra làm tham số (mặc định như phiếu), và test luôn truyền thư mục tạm.
- Test chạy trên ảnh tổng hợp trong thư mục tạm `$TMPDIR/dh-080/`; xóa thư mục đó khi xong (`rm -rf "$TMPDIR/dh-080"`, không có `/` cuối).

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
