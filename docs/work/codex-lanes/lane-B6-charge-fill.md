# Làn Codex B · Việc B6 · Lớp tụ lực theo hệ ở người tung chiêu khi đang gõ từ

Bối cảnh (07/11 02:50):
- Chuẩn VFX năm pha: tụ, bung tại người tung, bay, trúng, dư âm, và phía người tung làm trước.
- `art-src/lab/vfx/charge-fill/` có 14 flipbook `i2v-<hệ>-charge-fill` (vai `charge`, trường `element`), cắt ở làn 4, đã có KTX2 (A3).
- Phím 2–7 trong lab chưa có lớp tụ lực bằng tranh vẽ quanh người tung trong lúc gõ từ.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB6-report.md` (tiếng Việt, ngắn). Làm sau B5.

## Bảng (đã chốt)
- Khi đang gõ từ cho phím 2–7, flipbook `charge-fill` của hệ đang chọn hiện quanh người tung, ngang tay hoặc ngực, cỡ khoảng 1,2 lần bề ngang thân.
- **Chạy theo tiến độ gõ** (phần ký tự đã gõ đúng / độ dài từ), không theo giờ: gõ dừng thì clip đứng.
- Gõ xong thì tắt dần 0,12 s, đúng khung bung chiêu có sẵn. Không giữ lại chiêu: phím đến lúc bung vẫn ≤ 50 ms.
- Đổi từ hay bỏ dở thì tắt dần 0,2 s.
- Sáng tối đa 0,9 mỗi kênh. Sau model người tung, không che chữ đang gõ.
- `?chargefill=0` tắt lớp này.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:**
  - file mới `src/lab/charge-fill-fx.ts`;
  - chỗ nối trong `src/lab/skills-main.ts`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Cấm:**
  - đổi thời gian hay sự kiện của chiêu;
  - sửa `src/view/*`, `src/sim/*`, `src/content/*`, `src/lab/sound*.ts`;
  - sửa file trong `art-src`;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Đạt khi
- Có test node cho khung clip theo tiến độ gõ, tắt khi xong hay bỏ, đổi hệ, `?chargefill=0`, và không làm chậm khung bung chiêu.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
