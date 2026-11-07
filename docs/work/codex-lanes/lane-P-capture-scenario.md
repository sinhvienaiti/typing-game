# Phiếu làm thử · Kịch bản quay trước và sau cho 4 hiệu ứng (`?pilot=1`)

Bối cảnh: `docs/work/tasks/vfx-pilot-0711.md`. Nguồn đã lắp ở `art-src/lab/vfx-pilot-2026-11-07/` (báo cáo `docs/codex-queue/lanePilot-report.md`). Cờ `?pilot=1` đã có (`src/lab/pilot-overrides.ts`, `1cbc94d`).

Cần một kịch bản quay tự động để Claude chạy ngoài sandbox. Sandbox của Codex không mở được trình duyệt hay cổng, nên Codex **chỉ viết** kịch bản và kiểm cú pháp, không chạy.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: thêm đoạn ≤ 8 dòng vào `docs/codex-queue/lanePilot-report.md`, có lệnh chạy chính xác.

## Viết `scripts/visual/scenarios/lab-pilot-ab.mjs`
Theo khuôn của `scripts/visual/scenarios/lab-hybrid-ab.mjs` và `lab-judge.mjs`:
- chạy qua `node src/kit/tools/cdp-run.mjs`;
- trang `skills-lab.html?fixed=1&ui=0`, đồng hồ cố định 60 Hz;
- dùng API `window.__lab` có sẵn: đọc `src/lab/skills-main.ts` để biết hàm tung chiêu, đổi hệ, sinh boss, camera.

**Mỗi hiệu ứng quay 2 lần, cùng seed, cùng camera chơi, 1920 × 1080:** lần A không có `pilot`, lần B có `pilot=1`.
- **P1 · boss xuất hiện** (`boss-entrance-vortex`): sinh boss như phím V của greybox, hoặc hàm sinh boss có sẵn.
- **P2 · vòng Huyết** (`blood-ring-burst`): chọn hệ Huyết (E hay ô Element), tung chiêu nào đang dùng vai trò `ringBurst` (tìm trong mã lab).
- **P3 · sao băng Hỏa** (`fire-comet`): hệ Hỏa, phím M.
- **P4 · tia trúng đòn** (`beast-hit-spark-burst`): đòn nhẹ (phím 0 hay 1) vào bầy quái.

**Đầu ra mỗi hiệu ứng**, vào `OUT_DIR` (mặc định `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/pilot-ab/`):
- 12 khung theo pha (tụ, phóng, bay, chạm, dư âm), ghép tấm 4 × 3 cho mỗi lần quay;
- **nhãn mù X và Y**, xáo theo seed, khoá ở file riêng `key.json` không nằm cạnh tấm;
- mỗi lần quay 1 MP4 khoảng 3 s ở 30 fps (ffmpeg từ khung, đúng đồng hồ cố định);
- 1 MP4 ghép đôi trái và phải có chữ "X | Y", cho anh xem.
- Xoá khung thô sau khi ghép (luật AGENTS.md "Test captures").

Chưa xác định được cách kích một hiệu ứng thì ghi rõ trong báo cáo và vẫn làm 3 cái còn lại.

## Ranh giới
- **Được ghi:** `scripts/visual/scenarios/lab-pilot-ab.mjs` trong worktree `games/.wt-ic-lab-all`; báo cáo.
- Không sửa mã lab khác; nếu cần một hàm `__lab` mới, ghi đề xuất vào báo cáo, không tự thêm.
- Không lệnh git ghi, không mở cổng mạng, không mở trình duyệt.

## Đạt khi
- `node --check` qua.
- Báo cáo có lệnh chạy đầy đủ (biến môi trường, URL dạng `http://127.0.0.1:3146/skills-lab.html`) và danh sách file ra.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
