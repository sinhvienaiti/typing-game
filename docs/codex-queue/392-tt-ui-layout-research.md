# Phiếu 392: Nghiên cứu lối chơi gõ chữ trước, rồi bố cục UI/UX cho Tu Tiên Thủ Ải (chỉ báo cáo, không sửa code)


Phản biện: PASS (Sonnet, 16/11, vòng 3, sau khi owner bổ sung lối chơi)

## Bối cảnh
Owner 16/11/2026, xem ảnh màn chơi hiện tại (`typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-research/owner-screenshot-current-ui.webp`): "phần UI/UX đang thực sự rất kém… từ góc nhìn người chơi, nó che sạch, không còn một cái gì, vậy bài toán để xử lý việc này sẽ là gì? phải thiết kế như nào để UI/UX thân thiện, phù hợp cho cả việc typing và nhìn game 1 cách đầy đủ?"
Trong ảnh: thẻ "Học trước" ở giữa màn, bảng Cửa hàng, thanh kỹ năng, khung đợt, sinh lực và Linh Sa cùng lúc phủ gần hết sân đấu.

Owner bổ sung cùng ngày: "phải giải quyết được bài toán, lối chơi sẽ như thế nào trước, typing theo từ, cụm từ, danh sách từ, nó sẽ như nào… bản đồ thì không sai, cái đang sai là việc hiển thị UI/UX… không khiến việc typing khó khăn nhưng vẫn có thể xem đầy đủ mọi thứ đang diễn ra của game". Bản đồ giữ nguyên, không đề xuất đổi bản đồ.

## Việc
0. **Lối chơi gõ chữ (làm trước, là phần chính của báo cáo).** Đọc luật hiện tại (`games/immortality-cultivation/src/`, `docs/games/tu-tien/00-canon.md` và các tài liệu thiết kế trong `docs/games/tu-tien/`): người chơi gõ gì để làm gì (đánh quái, tung kỹ năng, mua, đặt trụ, học từ). So sánh ít nhất 3 mô hình, mỗi mô hình nêu cách hiển thị chữ, cách chọn mục tiêu, tải nhận thức, và hợp với việc học từ vựng tiếng Anh đến đâu:
   - từ gắn trên từng quái (gõ từ nào trúng quái đó);
   - cụm từ hoặc câu ngắn cho kỹ năng, tuyệt kỹ;
   - danh sách từ / hàng đợi từ ở một dải gõ cố định;
   - kết hợp (ví dụ quái thường gõ từ, kỹ năng gõ cụm, mua sắm bằng phím tắt khi nghỉ đợt).
   Chốt mô hình khuyên dùng, kèm luồng chơi một đợt từ đầu đến cuối (trước đợt, trong đợt, nghỉ giữa đợt) và quy tắc phím (phím nào là gõ chữ, phím nào là lệnh, cách chuyển chế độ). Bố cục UI ở các bước dưới phải phục vụ mô hình này.
1. Đọc code UI/HUD hiện tại trong `games/immortality-cultivation/src/` (tìm các panel: học trước, cửa hàng, thanh kỹ năng, đợt, sinh lực, ô tháp/trụ), liệt kê từng thành phần: vị trí, kích thước % màn hình ở 1280×720 và 1920×1080, lúc nào hiện, có chặn chuột/bàn phím không. Đo tỉ lệ sân đấu bị che.
2. Nghiên cứu (có dẫn nguồn URL, chỉ lấy nguyên tắc, không chép ảnh) cách các game cùng thể loại giữ sân đấu thoáng mà vẫn gõ chữ tốt: game gõ chữ (Typing of the Dead, Epistory, Nanotale, ZType), thủ thành/tower defense (Kingdom Rush, Bloons TD 6, Defense Grid), MOBA/ARPG HUD, và nguyên tắc HUD (diegetic, vùng an toàn, ẩn theo ngữ cảnh, mật độ thông tin).
   Nếu không có truy cập web: ghi rõ "từ trí nhớ, chưa kiểm chứng" cho từng nhận định, không bịa URL; Claude sẽ kiểm chứng sau.
3. Đề xuất 2–3 phương án bố cục cho Tu Tiên, mỗi phương án có:
   - sơ đồ khung dây ASCII hoặc SVG ở 16:9 (không phải ảnh vẽ AI), ghi % diện tích sân bị che lúc chơi, lúc mua sắm, lúc học từ;
   - chỗ đặt ô gõ chữ/từ đang gõ sao cho mắt không phải rời khỏi quái (ví dụ chữ gắn trên quái, dải gõ thấp mỏng);
   - cách xử lý thẻ "Học trước" (trước trận, lúc nghỉ giữa đợt, hay thu gọn), cửa hàng (mở bằng phím, ngăn kéo cạnh, chỉ giữa đợt), thanh kỹ năng (thu gọn, icon), thông tin đợt/sinh lực (góc, mờ khi không đổi);
   - luồng bàn phím: không xung đột giữa gõ từ và phím tắt.
4. Chọn một phương án Codex khuyên dùng, lý do, rủi ro, và danh sách việc dựng (chưa làm).

## Ràng buộc
Không sửa code, không tạo ảnh hay video, không commit, không đổi nhánh. Chữ người chơi đọc là tiếng Anh (luật AGENTS.md); ghi chú nếu UI hiện tại còn tiếng Việt.

## Giao nộp
Báo cáo `docs/codex-queue/392-report.md`, mở đầu bằng tóm tắt ≤ 300 từ bằng tiếng Việt cho owner; sơ đồ đặt trong `typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-research/` kèm `ABOUT.md` (purpose, made-by, doc, delete-when).
