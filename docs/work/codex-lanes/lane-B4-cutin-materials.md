# Làn Codex B · Việc B4 · Chất liệu vẽ cho cut-in phím 5 và phím 7

Bối cảnh (07/11 02:25):
- Lab có cut-in cho phím 5 và phím 7 (`src/lab/cutin.ts`). Làn 5 đã gắn âm vào các mốc: mở, khung hô, ấn dấu, thoát.
- `art-src/lab/vfx/cutin-mat/` có 8 chất liệu vẽ từ Firefly, cắt ở làn 4 và A2:
  - `cutin-ink-wash-sweep`, `cutin-cloud-wipe`: lau mở;
  - `cutin-speed-lines-loop`: tia tốc độ, lặp;
  - `cutin-gold-rays`: tia vàng;
  - `cutin-ember-drift`: tro lửa bay;
  - `cutin-light-petals-drift`: cánh hoa sáng bay;
  - `cutin-ink-bloom`: mực nở;
  - `cutin-seal-stamp-splash`: mực bắn ở ấn.
- Luật của anh: không vẽ hình bằng mã. Mỗi chi tiết thấy được dùng tranh vẽ.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB4-report.md` (tiếng Việt, ngắn).

## Bảng ghép (đã chốt)
| Mốc cut-in | Lớp |
|---|---|
| Mở | `cutin-ink-wash-sweep` (mặc định); `cutin-cloud-wipe` cho hệ water, wind, light, ice |
| Suốt khung hô, sau chân dung | `cutin-speed-lines-loop` |
| Cao trào khung hô | `cutin-gold-rays` cho light, star, metal; các hệ khác bỏ lớp này |
| Lớp bay suốt cut-in | `cutin-ember-drift` cho fire, metal, thunder, blood; `cutin-light-petals-drift` cho wood, light, water, wind; các hệ còn lại bỏ |
| Ấn dấu | **chưa dùng** `cutin-seal-stamp-splash`, vì clip có cán con dấu lộ ra và đang chờ làm lại. Ghi "chờ clip" |
| Thoát | `cutin-ink-bloom` |

- Lớp nằm trong khung cut-in, theo thứ tự lớp có sẵn: sau chân dung, trước nền.
- Sáng tối đa 0,9 mỗi kênh. Không che chữ, chân dung hay khuôn mặt.
- Dùng `FlipbookLibrary`, `FlipbookPool`, `FlipbookPlayer` có sẵn, nạp lười.
- `?cutinmat=0` trả về cut-in cũ để so A/B.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Làm sau B3.
- **Được ghi:**
  - `src/lab/cutin.ts`;
  - file mới `src/lab/cutin-materials.ts`;
  - chỗ nối trong `src/lab/skills-main.ts`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Cấm:**
  - đổi thời gian hay mốc âm của cut-in;
  - sửa `src/view/skills/*`, `src/sim/*`, `src/content/*`, `src/lab/sound*.ts`;
  - sửa file trong `art-src`;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Đạt khi
- Có test node cho chọn lớp theo hệ và mốc, `?cutinmat=0`, mỗi lớp tắt khi cut-in kết thúc hay bị huỷ, không cấp phát mỗi khung khi đã ấm.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ. Ghi số test trước và sau.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
