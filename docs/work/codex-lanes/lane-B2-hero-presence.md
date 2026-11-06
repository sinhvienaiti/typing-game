# Làn Codex B · Việc B2 · Lớp hiện diện quanh nhân vật chính trong lab

Bối cảnh (07/11 01:45):
- Luật của anh (03/11): nhân vật và vật phẩm phải có lớp hào quang quanh thân (vòng sáng, đốm khí, quầng), không để model trần.
- Làn 4 đã cắt các vòng lặp cho anh hùng vào `art-src/lab/vfx/meta/`: `hero-presence-ring-loop`, `hero-qi-motes-idle-loop`, `hero-golden-body-shell-loop`, `hero-ultimate-ready-aura-loop`, `hero-pill-heal-swell`.
- Hai vòng `hero-halo-ring-loop` và `hero-down-qi-scatter` đang được làm lại vì clip lỗi. Thiếu trong manifest thì bỏ qua và ghi vào báo cáo; không tự cắt.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB2-report.md` (tiếng Việt, ngắn). Làm sau B1, cùng worktree.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- Dùng `FlipbookLibrary`, `FlipbookPool`, `FlipbookPlayer` có sẵn: nạp lười, giải phóng sau 20 s. Có thể tái dùng phần bể của `src/lab/foe-flipbook-fx.ts`.
- **Được ghi:**
  - file mới `src/lab/hero-presence-fx.ts`;
  - chỗ nối trong `src/lab/skills-main.ts` và `src/lab/events.ts`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Cấm:**
  - sửa `src/view/skills/*`, `src/sim/*`, `src/content/*`, `src/lab/sound*.ts`;
  - sửa file trong `art-src`;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Bảng ghép (đã chốt)
| Trạng thái của nhân vật chính trong lab | Lớp |
|---|---|
| Luôn bật | `hero-presence-ring-loop` dưới chân, chói ≤ 0,6 mỗi kênh |
| Đứng yên: không gõ phím ≥ 1,5 s | thêm `hero-qi-motes-idle-loop` quanh thân; tắt dần 0,3 s khi gõ lại |
| Tuyệt kỹ phím 8 hoặc 9 sẵn sàng (theo hồi chiêu hay thanh lực có sẵn trong lab; không có thì khi mục 8/9 đang chọn và không hồi chiêu) | thêm `hero-ultimate-ready-aura-loop` quanh thân |
| Hộ kiếm B đang bật (nhánh `fx.block` thành công) | thêm `hero-golden-body-shell-loop` bọc thân trong thời gian chặn |
| Hồi máu, nếu lab có sự kiện này | `hero-pill-heal-swell` một lần |

- Lớp nằm sau và quanh model, không che mặt nhân vật hay chữ đang gõ.
- Mọi quầng và vòng ≤ 0,9 mỗi kênh. Lõi sáng chỉ ở viền mảnh.

## Danh sách việc
1. **`HeroPresenceFx`:** bật, tắt và chuyển trạng thái đúng bảng, có chuyển dần; không cấp phát mỗi khung.
   - **Đạt khi:** có test node cho từng trạng thái, chuyển dần khi gõ lại, B bật rồi tắt, ult sẵn sàng.
2. **So sánh:** `?presence=0` tắt toàn bộ lớp của việc này.
   - **Đạt khi:**
     - có test;
     - `npx --no-install tsc --noEmit` sạch;
     - `npx --no-install vitest run --maxWorkers=4` qua toàn bộ. Ghi số test trước và sau.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
