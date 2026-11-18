# Vòng 3 · Bước 3 · Cột Lôi: dư âm có dấu Lôi nguội rõ trên mặt đất (sau `tp2=1`)

Nút thắt số 3 trong `docs/work/consult/r2-step4-verdict.md`: dư âm thiếu vết tích bám mặt đất (giây 1,80–2,97). Mặt đất nhanh trở về nền, kết thúc nhẹ và chung chung. Luật: `path-to-8.md` §7.

**Chỉ làm điểm này:**
- Một **dấu Lôi nguội** bám mặt đất tại điểm giáng:
  - dùng dấu vẽ có sẵn (`thunder-ground-mark` hoặc mặt nạ vết trong `art-src/lab/vfx/marks/`); **không vẽ vết bằng mã**;
  - hiện ra từ điểm chạm đúng lúc cột rút;
  - nền tối hơn mặt đá cho tương phản rõ, khe sáng tím mảnh nguội dần;
  - tan bằng ăn mòn từ mép vào trong 1,2–2,0 s.
- Tách hẳn khỏi điện dư: điện dư thưa và tắt trước, dấu nguội ở lại lâu hơn.
- Kiểm trên cả nền sáng và nền tối của sân.

**Ngân sách:** như bước 1. **Mức `high`.** Worktree như trên.
- **Được ghi:** `src/lab/thunder-aftermath-r2.ts`, chỗ nối, test, báo cáo.

**Đạt khi:**
- test node: hiện đúng lúc, nằm phẳng trên mặt đất, tan hết, tách khỏi điện dư, `tp2` tắt thì không đổi;
- chạy riêng các file test có liên quan.
