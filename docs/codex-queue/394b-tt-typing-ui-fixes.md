# Phiếu 394b: Sửa các lỗi UI sau khi chụp kiểm phiếu 394


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Agent Claude chụp và đo bản 394 trong Chrome thật (16/11): che màn lúc đánh đạt (13,6 % ở 1280×720, 9,7 % ở 1920×1080), nhưng còn lỗi. Ảnh: `typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-build/` (`after-1920x1080-combat-stress.png`, `after-1280x720-prep.png`). Bản chốt: `docs/games/tu-tien/TYPING_GAMEPLAY_DECISION.md` mục "Owner chốt". Chạy sau phiếu 400 trong cùng làn (đọc lại `ban-quyet.ts` hiện tại, giữ phần của 400).

## Việc (trong `games/immortality-cultivation/`)
1. Khung Health/Energy ở góc trên trái đè ô trụ 0 (~2.057 px² ở cả 4 trạng thái); lúc chuẩn bị ở 1280×720 ngăn cửa hàng đè ô trụ 5. Sửa để UI không đè lõi, cổng hay ô trụ nào, ở 1280×720 và 1920×1080 (dùng `screen-zones.ts` hoặc dời/thu gọn khung).
2. Năng lượng 100/100 mà ô Ultimate vẫn ghi "Waiting for slot": sửa để hiện từ tuyệt kỹ khi đầy, và sau khi gõ xong hiện "Ultimate ready · Space" như luật phiếu 394. Thêm test.
3. "Wave 1/6" hiện hai lần ở góc trên phải: chỉ giữ một.
4. Thanh máu: thêm test và kiểm chứng rằng quái đầy máu không có thanh (ảnh chụp có cả quái đầy máu lẫn quái bị thương).
5. Icon tinh anh/boss: chưa có art được duyệt. Không vẽ bằng CSS/emoji. Liệt kê chính xác icon cần (kích thước, số lượng) trong báo cáo để làm phiếu ảnh; để chỗ cắm sẵn trong code.

## Nghiệm thu
- `pnpm test` và typecheck sạch.
- Đo lại che màn bằng `getBoundingClientRect` ở 4 trạng thái, có giao cắt với ô trụ/lõi/cổng = 0; ghi số trong báo cáo. Nếu sandbox chặn trình duyệt, để lệnh chụp cho Claude.
- Chỉ sửa `src/ui/`, `src/view/health-bars.ts`, `src/app/app.ts` nếu cần, và test. Không đụng `src/lab/`, bản đồ. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/394b-report.md`.
