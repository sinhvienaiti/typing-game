# Làn Codex B · Việc B3 · Âm cho các sự kiện mới của B1 và B2

Bối cảnh (07/11 02:25): B1 (`bb53ab2`) và B2 thêm vào lab nhiều sự kiện mới chưa có tiếng:
- boss xuất hiện;
- boss qua mốc 50 % máu: gầm cùng sóng xung kích;
- vòng hào quang tinh anh bật;
- hào quang tuyệt kỹ sẵn sàng bật;
- kim thân bật khi chặn B thành công.

Còn khoảng 413 việc âm Firefly chưa gắn (bảng kiểm kê ở `docs/codex-queue/lane5-report.md`). Làm đúng cách làn 5 (`docs/work/codex-lanes/lane-5-lab-sounds-2.md`):
- bảng `SPRINT_TAKES`;
- `FIREFLY_LEVELS` đo bằng ebur128;
- chọn take theo số đo cộng với prompt khớp `why`;
- bậc âm: boss T4 hoặc T5, tinh anh T3, hào quang nhân vật T2 khô hoặc vang nhẹ, không lấn tiếng đòn.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB3-report.md` (tiếng Việt, ngắn).

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Trước việc này: 118 file, 1.384 test.
- **Được ghi:**
  - `src/lab/sound.ts`, `src/lab/sound-tiers.ts`;
  - chỗ gọi âm trong `src/lab/foe-flipbook-fx.ts`, `src/lab/hero-presence-fx.ts`, `src/lab/skills-main.ts`;
  - test trong `tests/lab/`;
  - số đo vào `.local/laneB3-sounds/`;
  - báo cáo.
- **Cấm:**
  - đổi âm và mức đã gắn;
  - sửa file trong `firefly-sprint-2026-11-05/`;
  - tổng hợp âm bằng mã;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Việc
1. Với mỗi sự kiện mới, tìm việc âm hợp nhất trong số chưa gắn (đọc `group`, `why`, prompt trong `docs/work/tasks/firefly-sprint-sound.json`). Không có việc nào hợp thì ghi "chờ âm" và bỏ qua.
2. Gắn âm, đo mức, đặt điểm bắt đầu. Hào quang lặp thì chỉ phát tiếng lúc bật, không lặp tiếng suốt thời gian hào quang còn.
3. **Đạt khi:**
   - có test node: file có thật, mức có trong `FIREFLY_LEVELS`, mỗi sự kiện gọi đúng id, `?foeaura=0` và `?presence=0` thì không phát tiếng của lớp đó;
   - `npx --no-install tsc --noEmit` sạch;
   - `npx --no-install vitest run --maxWorkers=4` qua toàn bộ. Ghi số test trước và sau.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
