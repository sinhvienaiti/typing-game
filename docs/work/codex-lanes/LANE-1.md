# LANE-1 · Lab: Cột Lôi vòng 2 từng bước nhỏ và sửa phép đo

Chạy bằng `lane-runner.md`. Thứ tự, việc phải xong trước và cổng ghi trong bảng. **Cổng:**
- **C (Claude):** Claude quay, đo khung hình, cho chấm mù, rồi ghi `✅` kèm điểm khi đạt (§7: điểm tăng, không trục nào tụt, trong ngân sách). Không đạt thì ghi `✖` và lý do.
- **A (anh):** anh duyệt.

| # | Việc | Phiếu | Mức | Cần xong trước | Cổng | Trạng thái | Đầu ra |
|---|---|---|---|---|---|---|---|
| 1 | R2-1 phía người tung (mã) | `lane-R2-1a-thunder-caster.md` | high | — | | done | `340bd97` |
| 2 | R2-1 kịch bản quay và đo | `lane-R2-1b-thunder-measure.md` | high | 1 | | done | `61d7f0e` (video=0) |
| 3 | ĐO R2-1 (Claude) | — | — | 2 | C | done | Hiệu năng ĐẠT (Δp95 0,000 ms); chấm mù TRƯỢT (+0,5 trục mục tiêu), `docs/work/consult/r2-step1-verdict.md` |
| 3a | R2-1 thử lại: chỉ đổi nhịp vòng ấn (đỉnh đúng khung phóng) | `lane-R2-1d-retry-timing.md` | high | 3 | | done | commit (Claude chạy đủ vitest 13:30) |
| 3b | ĐO lại R2-1 (Claude); trượt lần nữa thì dừng và nghĩ lại (§7) | — | — | 3a | C | done | ĐẠT: tụ lực +4,5/+4,0, phóng +1,0/+1,5, Δp95 0,1 ms (`docs/work/consult/r2-step1b-verdict.md`) |
| 4 | R2-2 bay và thân cột | `lane-R2-2-thunder.md` | high | 3b | ✅ 13:50 (#3b đạt) | done | `5c4bf30` (Claude chạy đủ vitest 14:30) |
| 5 | ĐO R2-2 (Claude) | — | — | 4 | C | done | ĐẠT: bay +1,5/+2,5, cột +1,5/+0,5; cả chiêu 5,5 → 6,5 ở góc chơi; p95 9,8 ms (`docs/work/consult/r2-step2-verdict.md`) |
| 6 | R2-3 chạm và phản ứng quái | `lane-R2-3-thunder.md` | high | 5 | ✅ 14:50 (#5 đạt) | done | commit (Claude chạy đủ vitest 15:00) |
| 7 | ĐO R2-3 (Claude) | — | — | 6 | C | done | ĐẠT ngưỡng bước (chạm +1,0 nhịp/lực); cả chiêu vẫn 6,5; phản ứng quái chưa thấy rõ; p95 8,7 ms (`docs/work/consult/r2-step3-verdict.md`) |
| 8 | R2-4 dư âm | `lane-R2-4-thunder.md` | high | 7 | ✅ 15:15 (#7 đạt) | done | commit (Claude chạy đủ vitest 15:30) |
| 9 | ĐO R2-4 và gửi anh (Claude) | — | — | 8 | C | done | Dư âm +1,5 nhịp/lực; cả chiêu 6,5 (không tăng từ bước 2); p95 8,4 ms; 3 nút thắt trong `docs/work/consult/r2-step4-verdict.md` |
| 10 | Sửa phép đo cổng boss, vòng Huyết, tia trúng đòn | `lane-L1-measure-fixes.md` | high | — | ✅ 12:20 (quay xong) | done | commit (Claude chạy đủ vitest 13:30) |
| 11 | Sửa vòng phản hồi Framebuffer (glError 1282) | `lane-L1-gl-feedback.md` | high | — | ✅ 12:20 (quay xong) | done | commit sửa screen-fx (Claude chạy đủ vitest) |

**Ghi chú cho runner:**
- Việc "(Claude)" thì runner **không làm**, coi như cổng.
- Việc 10 và 11 không chờ vòng 2; làm khi việc 4, 6, 8 còn bị cổng chặn.
- Hai việc mã lab không chạy cùng lúc: làn này chỉ có một runner.

**Kết thúc vòng 2 (15:50):** cả chiêu 5,5 → 6,5 sau bước 2, đứng yên qua bước 3 và 4. Dừng theo §7, chờ anh quyết vòng 3 (sửa lần lượt 3 nút thắt).

## Vòng 3 (anh duyệt 07/11 15:55: "Làm vòng 3"): sửa lần lượt 3 nút thắt, đo sau mỗi bước

| # | Việc | Phiếu | Mức | Cần xong trước | Cổng | Trạng thái | Đầu ra |
|---|---|---|---|---|---|---|---|
| 12 | R3-1 quái nhận đòn có lực | `lane-R3-1-foe-reaction.md` | high | 9 | ✅ 15:55 (anh duyệt) | done | `games/.wt-ic-lab-all`: phản ứng thân R3-1; 43 test đạt; chờ Claude đo/chấm #13; `docs/codex-queue/laneL1-report.md` |
| 13 | ĐO R3-1 (Claude): cả chiêu ở góc chơi phải tăng | — | — | 12 | C | done 16:55: TRƯỢT hai lần (bc6077c, e132c92). Bảng 3 giám khảo mù: K = T = P, cả chiêu 6 = 6; nghiêng có chạy (20°) nhưng bị đĩa sao, cột sáng và số sát thương che; quái cao khoảng 20 px. Hiệu năng đạt (Δp95 −0,7 ms). Claude chốt: dừng hướng nghiêng, qua bước 2 | `docs/work/consult/r3-step1b-panel.md`, `r3-step1-verdict.md` |
| 14 | R3-2 đường dẫn thành dải sét | `lane-R3-2-guide-strip.md` | high | 13 | ✅ 16:55 (Claude: #13 trượt hai lần, luật vòng 3 dừng khi hai bước liền không tăng) | done 16:43 | `games/.wt-ic-lab-all`: dải sét R3-2; 35 test + probe + TypeScript đạt; chờ Claude đo/chấm #15; `docs/codex-queue/laneL1-report.md` |
| 15 | ĐO R3-2 (Claude) | — | — | 14 | C | doing (Claude): hiệu năng ĐẠT (Δp95 −1,0 ms, p95 8,7 ms); Codex chấm mù trên bộ nhãn mới D/R/W từ 17:15 (`lane-R3-2c-judge.md`) | |
| 16 | R3-3 dấu Lôi nguội trên mặt đất | `lane-R3-3-ground-mark.md` | high | 15 | C: mở khi #15 đạt | todo | |
| 17 | ĐO R3-3 và gửi anh (Claude) | — | — | 16 | C | todo (Claude) | |

**Đạt** ở vòng 3 = pha được sửa tăng ≥ 1 ở trục mục tiêu **và cả chiêu ở góc chơi tăng**, không trục nào tụt, trong ngân sách. Cả chiêu không tăng qua hai bước liền thì dừng và báo anh.
