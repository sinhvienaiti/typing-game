# Làn Codex B · Việc B9 · Sửa glError 1282 khi làm ấm bản demo A/B (hybrid)

Bối cảnh (07/11 09:20): bản demo A/B giữa video và flipbook (`src/lab/hybrid-ab.ts`, phiếu 326, mở bằng `?ab=meteor` hoặc `?ab=azure-cloud-dragon`) chạy đúng. KTX2 UASTC sang ASTC đã kiểm. Nhưng console báo `glError 1282` (`GL_INVALID_OPERATION`) trong bước làm ấm (prewarm) texture hoặc shader. Anh sẽ xem bản demo này để chốt cách lai, nên cần sạch lỗi.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB9-report.md` (tiếng Việt, ngắn). Làm sau B8, cùng worktree.

## Việc
1. Đọc đường làm ấm trong `src/lab/hybrid-ab.ts` và chỗ nó gọi `src/view/skills/flipbook.ts`. Tìm lệnh GL có thể sai thứ tự. Các nghi vấn thường gặp:
   - `texSubImage` hoặc `compileAsync` trên texture nén trước khi texture được cấp phát;
   - cập nhật texture đã `dispose`;
   - gọi `renderer.initTexture` với định dạng KTX2 chưa có loader;
   - đổi `uniform` khi chương trình chưa liên kết.
2. Sửa ở `hybrid-ab.ts`. Nếu lỗi nằm ở `flipbook.ts` thì chỉ sửa đúng chỗ đó, tối thiểu, và ghi rõ trong báo cáo.
3. **Đạt khi:**
   - có test node tái hiện thứ tự gọi sai bằng một renderer giả và chứng minh thứ tự mới đúng;
   - `npx --no-install tsc --noEmit` sạch;
   - `npx --no-install vitest run --maxWorkers=4` qua toàn bộ;
   - báo cáo ghi điều Claude cần kiểm trong trình duyệt: console không còn 1282 khi mở hai trang `?ab=`.

## Ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:**
  - `src/lab/hybrid-ab.ts`;
  - `src/view/skills/flipbook.ts`, chỉ khi lỗi nằm ở đó;
  - test trong `tests/`;
  - báo cáo.
- **Cấm:**
  - đổi hình hay số đo của bản demo;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
