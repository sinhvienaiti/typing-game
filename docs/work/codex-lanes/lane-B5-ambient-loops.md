# Làn Codex B · Việc B5 · Lớp không khí mờ trên sân lab

Bối cảnh (07/11 02:50): `art-src/lab/vfx/world/` có các vòng lặp không khí cắt từ Firefly, đã có KTX2 (A3):
- `world-mist-loop`: sương thấp;
- `world-dust-motes-loop`: bụi sáng;
- `world-light-shafts-loop`: tia nắng.

Sân lab hiện trống không khí. Làn này thêm các lớp đó **rất mờ, nằm sau quái**, để sân có chiều sâu mà không che chiêu hay chữ.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneB5-report.md` (tiếng Việt, ngắn).

## Bảng (đã chốt)
| Lớp | Vị trí | Sáng tối đa mỗi kênh |
|---|---|---|
| `world-mist-loop` | 2–3 tấm nằm gần mặt sân ở mép xa và hai bên, không phủ giữa sân | 0,25 |
| `world-dust-motes-loop` | 1 tấm đứng phía sau đàn quái, phủ ngang sân | 0,2 |
| `world-light-shafts-loop` | 1 tấm chéo từ góc trên xa | 0,18 |

- Thứ tự vẽ: sau quái và sau mọi hiệu ứng chiêu; không bao giờ trên thẻ chữ của quái.
- Không đổi đèn, sương mù cảnh, tone mapping hay bloom.
- Nạp lười, dùng `FlipbookLibrary`, `FlipbookPool`, `FlipbookPlayer` có sẵn. Vòng lặp chạy liên tục, không cấp phát mỗi khung.
- `?ambient=0` tắt toàn bộ lớp này.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:**
  - file mới `src/lab/ambient-fx.ts`;
  - chỗ nối trong `src/lab/skills-main.ts`;
  - test trong `tests/lab/`;
  - báo cáo.
- **Cấm:**
  - sửa `src/view/*`, `src/sim/*`, `src/content/*`, `src/lab/sound*.ts`;
  - sửa file trong `art-src`;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Đạt khi
- Có test node cho bật, tắt, `?ambient=0`, thứ tự vẽ sau quái và không cấp phát mỗi khung.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ (trước: 120 file, 1.428 test).

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
