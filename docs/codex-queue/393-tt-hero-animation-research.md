# Phiếu 393: Nghiên cứu hoạt ảnh nhân vật khi gõ chữ và tung chiêu (báo cáo, chưa dựng)


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Owner 16/11/2026: "khi typing, nhân vật sẽ có những animation nào, khi sử dụng các kỹ năng, hành động, cử chỉ, tung chiêu sẽ có những animation, rig như nào để mềm mượt đẹp và đa dạng, các dạng thủ ấn, cử động chân tay phải như nào để hợp với kỹ năng… giao thêm 1 agent cho codex xử lý thêm về animation của nhân vật".
Hoạt ảnh nhân vật là hệ thống dùng chung, chuẩn 9 điểm (`docs/games/SHARED_SYSTEMS_BAR.md`). Lối chơi gõ chữ đang được chốt ở phiếu 392/392b và bản phân tích Gemini `docs/games/tu-tien/source/gemini-typing-gameplay-ui-2026-11-16.md` (gợi ý: phi kiếm tự đánh, gõ từ trên quái tiền tuyến, 5 kỹ năng mỗi kỹ năng một từ, tuyệt kỹ gõ chuỗi từ rồi ấn Space theo vòng tụ linh). Đọc để biết các khoảnh khắc cần hoạt ảnh, không cần chờ kết quả 392.

## Đọc trước
- Skill `.agents/skills/game-character-animation/SKILL.md` và `docs/games/CHARACTER_ANIMATION.md` (hợp đồng clip, sự kiện, máy trạng thái, lớp thủ tục, IK).
- `docs/games/tu-tien/MOTION_PLAN.md`, `docs/games/tu-tien/00-canon.md` (nhân vật, ngũ hành, kỹ năng).
- Rig và clip hiện có của nhân vật chính trong `games/immortality-cultivation/` (tìm file `.glb`, bảng clip, code animation). Liệt kê xương, clip đang có, clip còn thiếu.

## Việc
1. **Bản đồ khoảnh khắc → hoạt ảnh**, theo từng trạng thái: chờ (thở, áo bay), bắt đầu gõ (tụ khí), mỗi phím đúng (nhịp tay nhỏ, không lặp đơn điệu), phím sai, gõ xong từ (phát chiêu nhỏ), kỹ năng của từng hệ (Kim, Mộc, Thủy, Hỏa, Thổ, Lôi, Băng…), tuyệt kỹ (gõ chuỗi, vòng tụ linh, Space khai ấn: Phàm/Linh/Tiên Ấn), bị đánh, thắng, thua.
2. **Thủ ấn (hand seals):** đề xuất bộ 6–10 thủ ấn gắn với ngũ hành và kiếm quyết, mỗi ấn mô tả tư thế hai bàn tay (ngón nào duỗi/gập), vị trí tay so với thân, nhịp chuyển. Ghi nguồn văn hoá nếu có (kiếm chỉ, ấn Phật giáo/Đạo giáo), không có web thì ghi "từ trí nhớ, chưa kiểm chứng", không bịa URL.
3. **Chân tay theo kỹ năng:** thế đứng, bước, xoay hông, nhịp tụ lực → phát chiêu → thu thế cho từng loại chiêu (kiếm chém, chưởng, triệu hồi trụ, kết trận dưới đất, tuyệt kỹ toàn sân). Thời gian theo khung 60 Hz; phím đến lúc phát chiêu ≤ 50 ms (luật VFX), nên phần tụ lực phải chạy song song khi gõ, không giữ chiêu lại.
4. **Rig và kỹ thuật để mềm mượt, đa dạng:** xương ngón tay có đủ cho thủ ấn không; lớp thủ tục (nghiêng, nhìn, thở, giật lùi), chuyển trạng thái mượt (inertialization), lò xo cho áo, tóc, dải lụa; biến thể ngẫu nhiên để không lặp; sự kiện clip cho VFX, âm thanh, camera cùng khung. Nguồn clip khả thi theo luật repo (không Mixamo cho AI đám mây, không auto-rig của Tripo; xem skill), ước lượng số clip cần làm.
5. **Đề xuất kế hoạch dựng theo đợt** (đợt 1 nhỏ nhất để owner thử trong lab), rủi ro, và một bài kiểm tra trong lab.

## Ràng buộc
Không sửa code, không tạo ảnh, video hay clip, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/393-report.md`, mở đầu tóm tắt tiếng Việt ≤ 300 từ cho owner; bảng thủ ấn và bảng khoảnh khắc ở dạng bảng Markdown.
