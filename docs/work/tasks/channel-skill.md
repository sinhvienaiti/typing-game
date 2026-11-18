# Chiêu duy trì theo nhịp gõ (canon D61)

**Mục tiêu (≤ 3 dòng):** một kiểu chiêu mới, luồng chảy liên tục vào đích; mỗi từ đúng nối thêm khoảng 0,8–1 s và một nhịp đập, gõ sai thì luồng tàn chậm.
**Cách đã chốt:** anh duyệt 05/11 22:20 ("Duyệt cả 3"); canon D61. Học từ `REF_VIDEO_LESSONS_2026-11-05.md` bài 10. Ô nào, phái hay hệ nào, thông số sát thương: chốt sau vòng Gemini (`docs/work/consult/streak-channel-gemini.md`), Claude kiểm với canon §6.5, §7 rồi viết lời giải, một phản biện Claude PASS rồi mới phiếu Codex.
**Nghiệm thu (số):** luồng hẹp ≤ 1 m, ≤ 60 % đục trên quái, chữ luôn trên cùng; từ đúng đến nhịp đập ≤ 50 ms; tàn bằng erosion ≥ 0,6 s; hai giám khảo mù ≥ 8,5 trong bản chơi.
**Phiếu, báo cáo, ảnh:** (chưa có)

## Nhật ký (mỗi dòng một sự kiện: ngày giờ · ai · việc · kết quả)
- 05/11 22:22 · Claude · tạo việc sau khi anh duyệt · chờ vòng Gemini
- 05/11 22:35 · Gemini · vòng hỏi xong, `consult/streak-channel-gemini.md` · Claude chốt: dựng thử trong lab bằng phím riêng (chưa chiếm ô 3); từ nào cũng nuôi luồng; 1 nhịp + 4 tick mỗi từ; chỉ đứt khi từ SLOPPY hoặc dừng > max(2,5 s, 2 × nhịp phím); hình từ clip ribbon/charge/release/impact có sẵn; tổng sát thương bằng ngân sách ô · kế tiếp: lời giải + một phản biện Claude, rồi phiếu Codex (mai)
- 06/11 04:45 · Claude (lab-element-kits) · dựng thử trong lab, commit `39f066f`, phím **C** (chưa chiếm ô 3): C mở luồng vào con gần nhất; từ nào gõ xong (phím 0–7 theo hạng, hoặc C) cũng nuôi luồng, 1 nhịp ngay khung của từ + 4 tick trong 0,9 s, nhân hạng; chỉ đứt khi SLOPPY (Shift+C) hoặc dừng > max(2,5 s, 2 × nhịp phím); giữa hai từ là sợi 0,3 m không sát thương; quái chết thì quét sang con gần nhất trong 6 m; luồng từ clip ribbon của hệ (không có thì dải lưỡi liềm), 0,85 m, sáng ≤ 0,6, tan erosion 0,7 s; nhịp dùng impact của bộ chất, mở dùng release. 4310 (Thủy): 5 từ, 5 nhịp, 20 tick, 0 lỗi. Chưa: ngân sách sát thương thật và ô ở vòng cân bằng; luồng Hỏa/Ám mảnh (ribbon mảnh); chưa chấm mù.
