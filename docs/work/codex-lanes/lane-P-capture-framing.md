# Phiếu làm thử · Kịch bản quay phải đặt máy quay để thấy hiệu ứng

Bối cảnh: `docs/work/tasks/vfx-pilot-0711.md`. Lần quay 10:40 (`8f46b03`) đã chạy hết: `pilotStatus` xác nhận nguồn làm thử được thay đúng (`override: true`, URL `vfx-pilot-2026-11-07`). **Nhưng không dùng được để chấm:**
- P1 ở cả X và Y chỉ thấy sân trống nhìn từ xa (bằng chứng `framing: { wanted: 0, shown: 0 }`, `distanceM ≈ 53,5`). Không thấy cổng boss.
- Kịch bản không báo lỗi dù hiệu ứng không nằm trong khung.
- Ffmpeg trên máy **không có `drawtext`**, nên bước ghép X|Y lỗi. Claude đã tự ghép, không cần sửa bước này nữa; bỏ hẳn bước ghép trong kịch bản.

Thư mục bằng chứng: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/pilot-ab-fix/` (đã có `X-sheet.jpg` của P1).

**Model `gpt-6.1-sol`, mức `high`.** Một lần chạy. Báo cáo: thêm ≤ 8 dòng vào `docs/codex-queue/lanePilot-report.md`.

## Việc (chỉ sửa `scripts/visual/scenarios/lab-pilot-ab.mjs`; cần hàm `__lab` mới thì thêm tối thiểu vào `src/lab/skills-main.ts`)
1. **Đặt máy quay theo vị trí hiệu ứng**, dùng cách đặt camera cận cảnh theo chiêu như `lab-judge.mjs`:
   - P1: chỗ boss sinh ra;
   - P3: vùng sao băng rơi;
   - P4: con quái bị đánh.
   Mỗi hiệu ứng quay 2 góc: (a) camera chơi nhưng đặt tâm vào hiệu ứng, (b) cận cảnh sao cho hình chính chiếm khoảng 35–60 % chiều cao khung. Hai lần X và Y dùng đúng cùng tư thế camera.
2. **Kiểm khung thật:** đo số điểm ảnh của hiệu ứng trong khung (so khung có hiệu ứng với khung ngay trước khi kích, vùng chênh sáng > 8/255). Nếu vùng này < 0,5 % khung ở thời điểm đỉnh thì **ném lỗi**; ghi số đo vào `evidence.json`.
3. Bỏ bước ghép X|Y (không có `drawtext`).
4. **Đạt khi:**
   - `node --check` qua;
   - có test node nhỏ cho hàm đo vùng chênh (ảnh tổng hợp);
   - nếu có sửa `skills-main.ts` thì `npx --no-install tsc --noEmit` sạch và `npx --no-install vitest run --maxWorkers=4` qua;
   - báo cáo ghi lệnh chạy lại vào thư mục mới `pilot-ab-v3`.

## Ranh giới
Worktree `games/.wt-ic-lab-all`. Không sửa media; không lệnh git ghi; không mở cổng mạng; không mở trình duyệt.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
