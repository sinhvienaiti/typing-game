# Làn Codex B · Việc B7 · Nút so sánh A/B trong panel lab

Bối cảnh (07/11 03:25): đêm nay lab có thêm nhiều lớp mới, mỗi lớp tắt được bằng cờ URL:
- `?deathfx=old` (làn 6);
- `?foeaura=0` (B1), `?presence=0` (B2), `?cutinmat=0` (B4), `?ambient=0` (B5), `?chargefill=0` (B6);
- `?video=0`, `?sigil=code`, `?readable=1` (có từ trước).

Anh xem lab trên máy, không gõ cờ URL. Cần một mục "So sánh A/B" trong panel gọn để bật hoặc tắt từng lớp bằng một cú bấm.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB7-report.md` (tiếng Việt, ngắn).

## Yêu cầu
- Một mục gập được "A/B" trong panel gọn có sẵn (giữ cỡ gọn, không che màn chơi). Mỗi cờ trên là một ô bật/tắt, nhãn tiếng Anh ngắn, ví dụ "Painted foe deaths", "Foe auras", "Hero presence", "Cut-in materials", "Ambient", "Charge layer".
- Bấm thì nạp lại trang với cờ tương ứng, giữ nguyên các cờ khác và các lựa chọn đang có trên URL (hệ, mục 8/9).
- Trạng thái ô lấy từ URL hiện tại. Phím tắt không trùng phím có sẵn của lab; không có thì bỏ.
- Danh sách cờ khai báo một chỗ (một mảng), để thêm cờ sau này chỉ sửa một dòng.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Trước việc này: 122 file, 1.457 test.
- **Được ghi:**
  - các file panel lab hiện có (tìm nơi dựng panel gọn của phiếu 329);
  - file mới `src/lab/ab-flags.ts`;
  - chỗ nối trong `src/lab/skills-main.ts`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Cấm:**
  - đổi hành vi của các cờ;
  - sửa `src/view/*`, `src/sim/*`, `src/content/*`, `src/lab/sound*.ts`;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Đạt khi
- Có test node: tạo URL đúng khi bật hoặc tắt từng cờ, giữ cờ khác, đọc trạng thái từ URL.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
