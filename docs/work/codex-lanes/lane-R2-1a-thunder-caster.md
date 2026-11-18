# Vòng 2 · Bước 1a · Cột Lôi: chỉ phía người tung (tụ lực và phóng), sau cờ `tp2=1`

Bối cảnh:
- Kết luận làm thử vòng 1: `docs/work/consult/codex-pilot-verdict.md` §3–4. Lỗi lớn nhất ở cả hai hiệu ứng là "không đọc được người tung ở pha tụ lực và phóng".
- Anh (07/11 11:30): làm **từng phần nhỏ, đo sau mỗi phần**; đẹp và mượt là ưu tiên số một, nhưng **trong ngân sách hiệu năng, mã gọn**.
- Luật: `.agents/skills/game-vfx-production/references/path-to-8.md` §7. Đọc §7 trước.

Bước này **chỉ** làm pha tụ lực và phóng của `pillar-thunder-single`. Không đụng các pha bay, chạm, dư âm (bước sau).

**Model `gpt-6.1-sol`, mức `high`.** Một lần chạy. Báo cáo: `docs/codex-queue/laneR2-report.md` (tiếng Việt, ≤ 10 dòng).

## Nền hiện có
- Mẫu năm pha B8: `src/lab/five-phase-clip.ts`. Tụ lực 0,20 s ở tay bằng `thunder-charge`; phóng lấy khung đỉnh `thunder-release`; `?fivephase=0` về bản cũ.
- Bản mới bật bằng `tp2=1` và chồng **trên** B8. Tắt `tp2` thì B8 giữ nguyên từng khung.

## Lớp của bước này (nguồn có sẵn trong `art-src/lab/vfx/thunder/`)
| Pha | Lớp | Engine điều khiển |
|---|---|---|
| Tụ lực | `thunder-caster-seal`, ấn nằm phẳng dưới chân người tung | Hiện dần 0 → 1 trong lúc tụ, xoay chậm; giữ qua lúc phóng; tan bằng ăn mòn 0,3 s sau phóng |
| Tụ lực | `thunder-sparkle` dạng sprite, hút vào tay | Mật độ tăng theo thời gian tụ, tối đa khoảng 24 hạt; quầng ≤ 0,9 mỗi kênh |
| Phóng | `thunder-ring-burst` dưới chân | Đúng khung phóng: nở nhanh 0,15 s rồi mờ 0,25 s |
| Phóng | đèn điểm có sẵn của lab | Một nhịp sáng ngắn màu Lôi đúng khung phóng, rồi tắt; không thêm đèn mới nếu đã có |

- Không đổi thời gian, sát thương hay sự kiện của chiêu. Phím đến lúc phóng vẫn ≤ 50 ms.
- Âm phóng đã có; chỉ cần lớp mới trùng đúng khung đó.

## Ngân sách (bắt buộc, §7)
- Cả Cột Lôi khi bật `tp2`: thêm ≤ 1,0 ms p95 so với khi tắt; ≤ 12 draw call thêm; không cấp phát mỗi khung khi đã ấm; ≤ 64 MB texture thêm (dùng KTX2 đã có).
- **Mã gọn:** tái dùng `FlipbookLibrary`, `FlipbookPool`, `FlipbookPlayer`, `charge-fill-fx` và `five-phase-clip`. Bước này thêm khoảng ≤ 250 dòng (không tính test). Không thêm shader mới.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:**
  - `src/lab/five-phase-clip.ts`, hoặc file mới nhỏ `src/lab/thunder-caster-r2.ts`;
  - chỗ nối trong `src/lab/skills-main.ts`;
  - `src/lab/ab-flags.ts`, thêm `tp2` nhãn "Thunder Pillar round 2";
  - test trong `tests/lab/`;
  - báo cáo.
- **Không:** sửa media hay manifest; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Đạt khi
- Test node:
  - 4 lớp bật đúng khung, tắt đúng hạn;
  - `tp2` tắt thì không đổi gì;
  - không cấp phát mỗi khung;
  - số draw call thêm ≤ 12, đếm qua pool.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ.
- Báo cáo ghi số dòng mã thêm, và những gì Claude cần quay để đo.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
