# Phiếu làm thử · Sửa: bật `?pilot=1` nhưng nguồn làm thử không được tải

Bối cảnh: `docs/work/tasks/vfx-pilot-0711.md`. Claude chạy `scripts/visual/scenarios/lab-pilot-ab.mjs` lúc 10:30.

**Bằng chứng:**
- Lần không cờ (baseline) của P1 và P4 quay được.
- Lần có `?pilot=1` thì kịch bản ném lỗi "Thiếu nguồn/nguồn pilot/12 khung": không thấy request nào tới `/art-src/lab/vfx-pilot-2026-11-07/<kit>/` ngoài `manifest.json`. Bằng chứng ở `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/pilot-ab/_private/evidence.json`.
- Thử tay trong trình duyệt (URL như kịch bản, có `pilot=1`, gọi `__lab.twinPearl.boss()`, bước 90 khung): `performance.getEntriesByType('resource')` không có file nào chứa `boss-entrance` hay `vfx-pilot`. Nghĩa là hoặc cổng boss không được phát, hoặc phát bằng nguồn đã nạp sẵn mà không qua lớp đè.
- `manifest.json` đè trả 200 (`curl`).
- P3 lỗi "Video chưa giải mã": Chrome headless có thể không giải H.264, nên kịch bản nên dùng `?video=0` để đi đường atlas. Lớp đè cũng nằm ở đường này.

**Model `gpt-6.1-sol`, mức `high`.** Một lần chạy. Báo cáo: thêm đoạn ≤ 8 dòng vào `docs/codex-queue/lanePilot-report.md`.

## Việc
1. **Tìm vì sao lớp đè không có hiệu lực** với thư viện flipbook của:
   - `src/lab/foe-flipbook-fx.ts` (`clip("boss", "boss-entrance-vortex")`, `beast-hit-spark-burst`);
   - đường sao băng phím M (`comet-head.ts`, khoá `fire-comet`).
   Nghi vấn: thư viện được tạo hoặc nạp sẵn trước khi lớp đè đăng ký; lớp đè chỉ đè metadata mà không đổi URL atlas hay KTX2; hoặc cổng boss không phát với boss của greybox.
2. **Sửa:**
   - với `?pilot=1`, mọi đường nạp 4 id này dùng atlas và KTX2 trong `vfx-pilot-2026-11-07`;
   - thêm `window.__lab.pilotStatus()`, trả về với mỗi id: có manifest đè hay không, URL atlas thực dùng, đã nạp hay chưa, số lần phát.
3. **Kịch bản `lab-pilot-ab.mjs`:**
   - thêm `video=0` cho cả hai lần quay;
   - dùng `__lab.pilotStatus()` thay cho dò `performance` để kiểm nguồn làm thử;
   - nếu P1 cần một cách sinh boss khác để cổng phát, sửa trigger (đọc lab để biết).
4. **Đạt khi:**
   - có test node: lớp đè có hiệu lực cả khi thư viện tạo trước; `pilotStatus` đúng;
   - `npx --no-install tsc --noEmit` sạch;
   - `npx --no-install vitest run --maxWorkers=4` qua toàn bộ;
   - `node --check` kịch bản qua;
   - báo cáo ghi lệnh chạy lại.

## Ghi chú thêm (không sửa trong phiếu này)
Console có `GL_INVALID_OPERATION: glDrawArrays: Feedback loop formed between Framebuffer and active Texture`. Đây là nguồn của glError 1282 mà B9 chưa tìm ra. Ghi vào báo cáo nếu thấy chỗ gây ra, để làm phiếu riêng.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:**
  - `src/lab/pilot-overrides.ts`, `src/lab/foe-flipbook-fx.ts`, `src/lab/comet-head.ts`, `src/lab/skills-main.ts`;
  - `src/view/skills/flipbook.ts`, tối thiểu, có lý do;
  - `scripts/visual/scenarios/lab-pilot-ab.mjs`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Không:** sửa media; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
