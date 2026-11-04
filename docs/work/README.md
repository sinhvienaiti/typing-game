# Hệ thống file làm việc (từ 05/11/2026)

Anh dặn (05/11, khoảng 00:30): "nên thiết kế 1 hệ thống đơn giản các file md để xử lý, giao việc, ghi lại thông tin, các phần phân tích trao đổi để tránh việc phải đọc lại quá nhiều".

Mục đích: mỗi người làm (Claude, agent, Codex, Gemini, ChatGPT) **chỉ đọc đúng file nhỏ của việc mình**, không đọc lại lịch sử chat hay tài liệu dài.

## Các file

| File | Là gì | Ai ghi | Giới hạn |
|---|---|---|---|
| `BOARD.md` | Bảng việc: tối đa 3 việc đang làm, hàng chờ Codex, việc chờ anh, việc xong hôm nay | Claude điều phối | ≤ 60 dòng |
| `DECISIONS.md` | Mỗi quyết định của anh một dòng: ngày, việc, quyết định, câu gốc | Claude | thêm dòng, không sửa dòng cũ |
| `tasks/<id>.md` | Một việc một file: mục tiêu, cách đã chốt, số nghiệm thu, nhật ký trạng thái, đường dẫn | Claude tạo; agent và Codex ghi thêm vào nhật ký | ≤ 150 dòng |
| `consult/<id>-<gemini\|chatgpt>.md` | Một lần hỏi Gemini hoặc ChatGPT: đề bài gửi đi, **TÓM TẮT ≤ 300 chữ ở đầu**, câu trả lời đầy đủ ở dưới | agent hỏi (trang tự lưu câu trả lời) | người đọc chỉ đọc TÓM TẮT |
| `USAGE.md` | Chi phí token theo ngày và theo lần hỏi trợ lý | Claude (chạy `tools/agent-usage/usage.py`) | thêm dòng |
| `QUALITY.md` | Sổ chất lượng: anh duyệt hoặc chê, lỗi Claude, Codex dừng đúng, kiểm trượt, thời gian mất | Claude, ngay khi có sự kiện | thêm dòng |
| `review/<ngày>.md` | Rà soát 23:00 mỗi ngày: token, làm được gì, chất lượng, thời gian mất, 3 phương án cải thiện | Claude (lịch tự chạy) | khoảng 80 dòng |
| `archive/` | File cũ, chỉ mở khi cần tra | — | — |

Phiếu Codex vẫn nằm ở `docs/codex-queue/`; file việc trỏ tới chúng. Ảnh, video và số đo vẫn ở `typing-game-review/`.

## Luật dùng
1. **Mở phiên hay giao việc:** đọc `BOARD.md` rồi đúng file `tasks/<id>.md` của việc mình. Không đọc file lưu trữ, trừ khi file việc trỏ tới một dòng cụ thể.
2. **Giao agent:** chỉ đưa đường dẫn file việc và một câu nhiệm vụ. Agent ghi kết quả vào nhật ký của file việc (một dòng một sự kiện) và trả về tối đa 10 dòng.
3. **Giao Codex:** phiếu ngắn (≤ 1.500 chữ) ở `docs/codex-queue/`, link trong file việc. Kết quả Codex ghi ở `docs/codex-queue/<n>-report.md`; Claude ghi một dòng tóm tắt vào nhật ký.
4. **Hỏi trợ lý** (Gemini 4 Argon High trước, ChatGPT khi Gemini hết hạn mức):
   - đề bài ≤ 1.500 chữ, ghi ở đầu file `consult/`;
   - trang tự lưu câu trả lời vào file;
   - agent chỉ đọc TÓM TẮT;
   - ghi chi phí (số bước, token) vào `USAGE.md`.
5. **Báo anh khi trợ lý làm tốn hơn:** nếu một lần hỏi tốn hơn mức Claude tự làm (ước tính), hoặc hơn 1,5 triệu token, Claude **báo anh ngay** cùng số liệu để anh quyết cách xử lý. Anh dặn 05/11: "tôi đưa chatgpt và gemini vào để giúp bạn giảm token, chứ nếu việc đưa nó vào khiến token bị tốn nhiều hơn thì phải báo tôi".
6. **Cập nhật `BOARD.md` ở mốc,** không phải mỗi vài phút. Việc xong thì chuyển xuống "Xong hôm nay"; sang ngày thì xóa phần đó (đã có trong git).
