# Phiếu 436i: Nữ chính, thân nền v5B, chỉ sửa tay và ngón

Phản biện: PASS (Sonnet, 18/11; vòng 1 vượt phạm vi, đã bỏ mục sức hút)

## Bối cảnh
Owner 18/11 chọn mẫu v5B (dịu dàng, quyến rũ). Hai giám khảo chấm mù (`docs/work/tasks/blind-judging-v5b-relic.md`) cho 7.6–8.8 và chỉ ra ba lỗi:
- ở góc nghiêng, tay đưa ra phía trước thay vì mở chữ A như góc trước và góc sau;
- các ngón tay dính vào nhau;
- sức hút còn giống ma-nơ-canh CG.

Owner chọn "Sửa tay và ngón rồi Tripo": giữ nguyên mặt và dáng đã chọn.

## Việc
Dùng công cụ `image_gen`, tối đa 2 lần.

Ảnh đầu vào là ảnh của dự án, dùng làm ảnh để sửa (edit) và ghi đường dẫn vào prompt: `games/immortality-cultivation/art-src/heroine/fashion/base-body.v5B-turn.v1-try2.png`.

Giữ nguyên mặt, tóc, thân, tỷ lệ, đồ lót, nền, ánh sáng và vị trí ba hình. Chỉ sửa những điểm sau:
1. **Góc nghiêng:** tay nằm trong mặt phẳng hai bên thân và mở xuống theo dáng chữ A, giống góc trước và góc sau. Nhìn ngang thì tay che một phần hông, không đưa ra phía trước.
2. **Ngón tay:** ở cả ba góc, năm ngón hơi tách nhau và duỗi tự nhiên, thấy rõ khe giữa các ngón.

Sau mỗi lần sửa, tự đo góc mở tay ở cả ba góc, chiều cao hình (px) và lề nhỏ nhất (px).

Lưu ở `games/immortality-cultivation/art-src/heroine/fashion/base-body.v5B-turn.v2-try<k>.png`, mỗi ảnh kèm `.prompt.txt`. Ghép tờ so sánh v1 | v2 tên `heroine-base-v5b-436i.jpg`; nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-436i/`.

## Ràng buộc
- Không đưa ảnh của game khác vào công cụ.
- Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/436i-report.md`, gồm danh sách ảnh và số đo của từng ảnh.
