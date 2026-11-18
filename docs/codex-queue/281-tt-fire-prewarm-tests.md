# Phiếu 281 · Tu Tiên · Test: cập nhật hai ca prewarm cũ sau phiếu 280

**Loại việc:** test (`gpt-6.1-sol`, mức `xhigh`). Phiếu rất ngắn, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/281-report.md`.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`. Làm tiếp trên các thay đổi chưa commit của 277, 278 và 280.

## Việc
Claude cho phép sửa đúng hai ca mà `docs/codex-queue/280-report.md` mục "Hai test cũ cần mở phạm vi" nêu, đều trong `tests/view/fire-lot1-art.test.ts`:
- `loads the v2 strip through the fire library from the existing art URL`;
- `prewarms the final masked brush, flash and lot-1 programs without changing live effects`.

Làm đúng như báo cáo 280 đề xuất:
- renderer giả có thêm `initTexture`;
- phép kiểm chuyển từ `compile(pool.mesh, camera)` sang một lần `compile` theo cả cảnh;
- duyệt các mesh con để giữ đủ các phép kiểm cũ: shader, mặt nạ, đặt dải, visibility, target, dữ liệu thẻ đang sống.

Không nới hay bỏ phép kiểm nào. Không sửa mã chạy.

### Được ghi
`tests/view/fire-lot1-art.test.ts` (chỉ hai ca trên) và `docs/codex-queue/281-report.md`.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): 1000/1000.
3. `git status --short` không thêm tệp nào ngoài danh sách của 277, 278, 280 và tệp test này.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
