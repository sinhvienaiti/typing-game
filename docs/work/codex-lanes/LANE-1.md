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
| 5 | ĐO R2-2 (Claude) | — | — | 4 | C | doing (Claude): quay và đo từ 14:32 | |
| 6 | R2-3 chạm và phản ứng quái | `lane-R2-3-thunder.md` | high | 5 | C: mở khi #5 đạt | todo | |
| 7 | ĐO R2-3 (Claude) | — | — | 6 | C | todo (Claude) | |
| 8 | R2-4 dư âm | `lane-R2-4-thunder.md` | high | 7 | C: mở khi #7 đạt | todo | |
| 9 | ĐO R2-4 và gửi anh (Claude) | — | — | 8 | C | todo (Claude) | |
| 10 | Sửa phép đo cổng boss, vòng Huyết, tia trúng đòn | `lane-L1-measure-fixes.md` | high | — | ✅ 12:20 (quay xong) | done | commit (Claude chạy đủ vitest 13:30) |
| 11 | Sửa vòng phản hồi Framebuffer (glError 1282) | `lane-L1-gl-feedback.md` | high | — | ✅ 12:20 (quay xong) | done | commit sửa screen-fx (Claude chạy đủ vitest) |

**Ghi chú cho runner:**
- Việc "(Claude)" thì runner **không làm**, coi như cổng.
- Việc 10 và 11 không chờ vòng 2; làm khi việc 4, 6, 8 còn bị cổng chặn.
- Hai việc mã lab không chạy cùng lúc: làn này chỉ có một runner.
