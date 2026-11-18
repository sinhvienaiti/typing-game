# Rà soát hằng ngày lúc 23:00

Anh dặn (05/11/2026, khoảng 00:40): "bạn nhớ phải theo dõi kỹ việc sử dụng token và chất lượng ra 1 file để mỗi ngày sẽ review lại lúc 23h00 cho tôi để đưa ra phương án cải thiện".

Mỗi ngày Claude viết `review/<yyyy-mm-dd>.md` (tối đa khoảng 80 dòng) và gửi anh bản tóm tắt:
1. **Token:** tổng và theo khâu (`tools/agent-usage/usage.py`), so với hôm trước; khâu tốn nhất; mỗi lần hỏi Gemini/ChatGPT tốn bao nhiêu so với tự làm.
2. **Làm được gì:** phiếu đã gộp, mẫu anh duyệt, video đã gửi, số việc Firefly xong.
3. **Chất lượng:** số sự kiện theo loại trong `QUALITY.md` (anh chê, lỗi Claude, Codex dừng đúng, kiểm trượt, lỗi sau gộp) và ví dụ nặng nhất.
4. **Thời gian mất:** hết giới hạn phiên, Codex ngồi không, chờ duyệt.
4b. **Vi phạm luật:** chạy một agent Sonnet 5.5 effort low theo `docs/work/RULE_AUDIT.md` (chỉ đọc); ghi từng vi phạm và nhật ký `.local/codex-runs/gate-refusals.log` của ngày. Vi phạm lặp hai ngày thì đề xuất thành cổng chặn.
5. **3 phương án cải thiện** cho ngày mai, mỗi cái có mức tiết kiệm hoặc lợi ích ước tính. Luật nào đổi thì ghi vào skill `agent-orchestration`.

Lịch: CronCreate `55 22 * * *` trong phiên điều phối. Lịch chỉ sống trong phiên, nên khi chuyển phiên phải đặt lại (ghi ở BOARD).
