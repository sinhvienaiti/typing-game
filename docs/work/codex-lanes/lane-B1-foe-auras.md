# Làn Codex B · Việc B1 · Hào quang tinh anh và boss trong lab

Bối cảnh (07/11 01:45):
- Làn 6 (`c93e2f3`, `src/lab/foe-flipbook-fx.ts`) đã cho quái chết, trúng đòn, choáng và trói dùng flipbook vẽ.
- Thư mục `art-src/lab/vfx/boss/` còn các vòng hào quang chưa dùng: `elite-aura-ironhide-loop`, `elite-aura-frenzy-loop`, `elite-aura-regen-loop`, `captain-aura-loop`, `captain-aura-ground-loop`, `boss-frenzy-aura-loop`, `boss-entrance-vortex`, `boss-entrance-fog`, `boss-phase-roar-shockwave`, `boss-phase-aura-flare`.
- Luật của anh: mọi quái mạnh phải có lớp hiện diện quanh thân. Lớp đó khoác lên model, không che hay thay model.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB1-report.md` (tiếng Việt, ngắn).

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Trước việc này: 116 file, 1.351 test.
- Dùng đúng `FoeFlipbookFx` và bể, bộ nạp của nó: nạp lười, giải phóng sau 20 s.
- **Được ghi:**
  - `src/lab/foe-flipbook-fx.ts`;
  - chỗ nối trong `src/lab/skills-main.ts` và `src/lab/events.ts`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Cấm:**
  - sửa `src/view/skills/*`, `src/sim/*`, `src/content/*`, `src/lab/sound*.ts`;
  - sửa file trong `art-src`: làn A đang thêm KTX2 vào manifest `boss/`, việc này chỉ đọc;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Bảng ghép (đã chốt)
| Quái | Lớp |
|---|---|
| Bậc 2 (`thiet-giap-tru`, tinh anh) | `elite-aura-ironhide-loop` quanh thân, lặp suốt đời quái |
| Boss `thiet-boi-lang-vuong` | `captain-aura-ground-loop` dưới chân luôn bật. Khi máu ≤ 50 % thêm `boss-frenzy-aura-loop` quanh thân, kèm một lần `boss-phase-roar-shockwave` + `boss-phase-aura-flare` đúng khung qua mốc 50 % |
| Boss xuất hiện (nếu lab có lúc sinh boss) | `boss-entrance-vortex` + `boss-entrance-fog` một lần tại chỗ sinh |

- Các vòng còn lại (`elite-aura-frenzy-loop`, `elite-aura-regen-loop`, `captain-aura-loop`) chỉ dùng nếu lab có đúng trạng thái đó (cuồng nộ, hồi máu, đội trưởng). Không có thì ghi "chờ tính năng" trong báo cáo.
- Lớp quanh thân nằm sau và quanh model. Chói tối đa 0,9 mỗi kênh, không che mặt hay chữ trên đầu quái.

## Danh sách việc
1. **Vòng hào quang:**
   - bật và tắt theo đời quái (chết, biến mất, đổi serial thì tắt ngay);
   - tối đa 8 vòng tinh anh cùng lúc, chọn gần giữa màn hình trước; boss luôn có chỗ;
   - không cấp phát mỗi khung khi bể đã ấm.
   - **Đạt khi:** có test node cho bật và tắt theo đời quái, giới hạn 8, mốc 50 % bắn đúng một lần.
2. **So sánh:** `?foeaura=0` tắt toàn bộ lớp của việc này.
   - **Đạt khi:**
     - có test;
     - `npx --no-install tsc --noEmit` sạch;
     - `npx --no-install vitest run --maxWorkers=4` qua toàn bộ. Ghi số test trước và sau.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
