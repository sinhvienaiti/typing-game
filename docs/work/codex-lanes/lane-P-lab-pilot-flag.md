# Phiếu lab · Cờ `?pilot=1`: nạp nguồn làm thử đè lên đúng các mục manifest

Bối cảnh: `docs/work/tasks/vfx-pilot-0711.md`. Cần so trước và sau cho 4 hiệu ứng trong cùng một bản lab, cùng camera và seed. Chỉ khác ở cờ URL.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/lanePilot-report.md` (tiếng Việt, ngắn). Một lần chạy, việc nhỏ.

## Yêu cầu
- Khi URL có `?pilot=1`, bộ nạp flipbook của lab đọc thêm manifest đè ở `art-src/lab/vfx-pilot-2026-11-07/<kit>/manifest.json` (cùng lược đồ manifest hiện có).
  - Mục nào có trong manifest đè thì thay **đúng mục cùng id** của kit đó. Mục khác giữ nguyên.
  - Không có thư mục, hoặc không có mục, thì không đổi gì và chỉ cảnh báo console một lần.
- Manifest đè có thể có thêm trường `envelope`: `{ durationS, scale: [[t, v]…], alpha: [[t, v]…], erosion: { start, end } }`, với t từ 0 đến 1. Trình phát flipbook dùng đường bao này nếu có, không có thì giữ cách cũ.
  - Chỉ thêm ở lớp lab. Nếu bắt buộc chạm `src/view/skills/flipbook.ts` thì chỉ ở mức tối thiểu và ghi lý do.
- Thêm `pilot` vào danh sách cờ của mục A/B (`src/lab/ab-flags.ts`), nhãn "Pilot sources".
- 4 kit cần chạy được: `boss`, `blood`, `fire`, `beast`.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Trước việc này: 125 file, 1.514 test.
- **Được ghi:**
  - file mới `src/lab/pilot-overrides.ts`;
  - chỗ nối trong `src/lab/skills-main.ts` và nơi nạp manifest trong `src/lab/`;
  - `src/lab/ab-flags.ts`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Không:** sửa media hay manifest đang có; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Đạt khi
- Có test node:
  - đè đúng id;
  - không cờ thì không đổi gì;
  - thiếu thư mục thì không lỗi;
  - đọc đúng `envelope`.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
