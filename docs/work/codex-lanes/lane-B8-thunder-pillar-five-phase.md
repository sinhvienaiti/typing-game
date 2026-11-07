# Làn Codex B · Việc B8 · Mẫu năm pha cho một chiêu phím 8: Cột Lôi (`pillar-thunder-single`)

Bối cảnh (07/11 09:15):
- Anh (06/11): các chiêu phím 8/9 làm từ video "vẫn cho tôi cảm giác đang chiếu video". Lý do: chiêu chỉ có hình chính, thiếu pha ở người tung và phản ứng trên quái.
- Chuẩn: `docs/games/VFX_STANDARD.md`, đủ 5 pha (tụ lực, phóng tại người tung, bay, chạm, dư âm), làm phía người tung trước. Mỗi pha có lớp hào quang: lấp lánh, hạt sáng, quầng mềm, vòng sáng ≤ 0,9 mỗi kênh.
- Mẫu đã làm cho Hỏa ở `src/lab/five-phase.ts` (sao băng và lưỡi liềm, `docs/work/tasks/skill-five-phase-samples.md`). Làm theo đúng cách đó.
- Đêm qua lab có thêm các phần dùng lại được:
  - phản ứng trên quái `src/lab/foe-flipbook-fx.ts` (trúng theo mức, choáng);
  - lớp tụ lực theo hệ `src/lab/charge-fill-fx.ts`;
  - hào quang người tung `src/lab/hero-presence-fx.ts`.

Việc này **chỉ làm một chiêu mẫu** để anh chấm, chưa áp cho các chiêu khác.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB8-report.md` (tiếng Việt, ngắn).

## Năm pha của Cột Lôi (đã chốt)
Hình lấy từ bộ hệ Lôi `art-src/lab/vfx/thunder/manifest.json` (các vai `charge`, `release`, `pillar`, `impact`, `groundImpact`, `groundMark`, `sparkle`, `hitAffliction`) và các thư mục quái. Không vẽ hình bằng mã.

1. **Tụ lực (0,15–0,25 s, ngay khi bấm phím 8):**
   - clip `charge` Lôi ở tay hoặc kiếm người tung, cùng `charge-fill` Lôi (dùng `charge-fill-fx`) chạy theo thời gian;
   - viền nhân vật sáng tím trắng;
   - vài `sparkle` hút vào.
   - Phím đến lúc phóng ≤ 50 ms vẫn giữ: tụ lực là lớp chồng, không giữ chiêu lại.
2. **Phóng tại người tung (khung đầu sáng đủ):**
   - clip `release` Lôi ở tay;
   - chớp sáng, giật camera nhẹ theo bậc có sẵn;
   - một vệt sáng mảnh bắn lên trời (vai `slash` hoặc `ribbon` dựng đứng), báo chiêu đi lên.
3. **Bay:** ấn `groundMark` dưới mục tiêu 0,15–0,25 s trước cú (đã có). Cột Lôi rơi đúng khung đỉnh như hiện tại.
4. **Chạm:**
   - `impact` và `groundImpact` Lôi tại mục tiêu;
   - quái dùng phản ứng của làn 6: hình trúng theo mức `heavy`, choáng bằng `stagger-stars-loop` đúng thời gian `status`;
   - số sát thương, hit-stop và rung theo bậc như cũ.
5. **Dư âm (1,5–2,5 s, tàn bằng erosion, không tắt nhanh):**
   - vết `groundMark` nằm lại;
   - `sparkle` Lôi lấp lánh thưa dần;
   - `hitAffliction` Lôi trên quái còn sống trong thời gian choáng.

- **Âm:** giữ âm có sẵn của chiêu. Pha nào có âm Firefly đúng nghĩa mà chưa gắn thì ghi vào báo cáo; không tự gắn.
- **So sánh:** `?fivephase=0` trả chiêu về bản cũ. Thêm cờ này vào danh sách `src/lab/ab-flags.ts` để hiện trong mục A/B của panel.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Trước việc này: 123 file, 1.494 test.
- **Được ghi:**
  - `src/lab/five-phase.ts`, hoặc file mới `src/lab/five-phase-clip.ts` nếu tách gọn hơn;
  - `src/lab/clip-skills.ts`, chỉ chỗ nối cho đúng mục `pillar-thunder-single`;
  - `src/lab/ab-flags.ts`;
  - chỗ nối trong `src/lab/skills-main.ts`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Cấm:**
  - đổi sát thương, thời gian cú trúng hay bảng 47 chiêu;
  - sửa `src/view/*`, `src/sim/*`, `src/content/*`, `src/lab/sound*.ts`;
  - sửa file trong `art-src`;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Đạt khi
- Có test node:
  - đủ 5 pha theo đúng thứ tự thời gian;
  - khung phóng sáng đủ ngay khung đầu;
  - tụ lực không làm chậm cú trúng;
  - dư âm tắt hết trong 2,5 s;
  - `?fivephase=0` về bản cũ;
  - không cấp phát mỗi khung khi đã ấm.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ.
- Báo cáo ghi những gì Claude cần quay để anh chấm.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
