# Phiếu 413 — Hoàn thiện sau 406b

Ngày: 16/11/2026. Đã sửa mã và kiểm tra tự động; còn kiểm tra hình ảnh trong bản chơi.

## Đã làm

Các đường dẫn dưới đây tương đối với `games/immortality-cultivation/`:

- `tests/ui/word-fx.test.ts`: thay so sánh trần tuyệt đối bằng dung sai `Number.EPSILON × max(1, limit) × 8`, chỉ bù sai số dấu phẩy động. Không đổi giới hạn bay/rơi trong mã. Kiểm tra thêm số hạt 6–10 và kích thước khi bay.
- `src/ui/word-fx.ts`, `src/ui/styles/word-fx-css.ts`: giữ 8 hạt/từ và ảnh `art-src/lab/vfx/ice-ult/glint.png`; tăng kích thước gốc 28 → 36 px, hệ số kích thước 0,85–1,2 → 1–1,3. Màu từ `(229,221,183)` thành `(229,229,206)`; mỗi kênh tối đa 229/255 ≈ 0,898. Opacity vẫn tối đa 0,9, theo đường tắt dần của chữ và bằng 0 tại 640 ms; reduced motion vẫn tắt hạt.
- `tests/ui/word-flight.test.ts`: kiểm tra hạt vẽ trên canvas có kích thước ít nhất 36 px, vẫn nằm trong viewport và hết cùng chữ.
- `tests/ui/word-fx-capture.mjs`: bổ sung `travelPx.attack` và `travelPx.defence` vào JSON của từng độ phân giải. Mỗi mục có đỉnh biên độ từng chữ, min/max, số mẫu, thời điểm vẽ và khoảng mục tiêu 80–110 / 50–80 px. Probe lấy tâm chữ thực từ ma trận canvas, sau kẹp viewport, đổi về CSS px theo DPR; chỉ tính mẫu opacity ≥ 0,5. Không lấy lại số danh định từ `WordFx.travel`. Thiếu mẫu được ghi vào `failures`. Phiếu 413 cũng xuất bảng khung hình như 406b.
- `tests/ui/word-fx-capture.test.ts`: 3 ca kiểm tra probe với DPR 2, bỏ mẫu gần trong suốt, báo đúng trường hợp rơi bị kẹp còn 12 px và không bịa số khi thiếu mẫu.
- `src/view/hitfx.ts`: chỉ đổi comment `HOÀN HẢO` thành `PERFECT`.
- `tests/ui/english-panels.test.ts`: kiểm tra literal giao diện trong `results.ts` và `review-card.ts`, bỏ qua comment. Cả hai đã dùng tiếng Anh; nghĩa tiếng Việt tiếp tục lấy từ dữ liệu từ học, không bị thay đổi.

## Kiểm tra

- `pnpm test --maxWorkers=2 --minWorkers=1`: **104/104 file, 1.054/1.054 test đạt**, 18,21 giây. Chạy theo mục nghiệm thu cụ thể của phiếu 413.
- `pnpm exec tsc --noEmit`: đạt.
- `node --check tests/ui/word-fx-capture.mjs`: đạt.
- Nhóm 6 file test liên quan: 27/27 đạt trước lượt kiểm tra toàn bộ.
- Không còn `HOÀN HẢO` trong `src/view/hitfx.ts` và `src/view/feedback-profile.ts`; profile cục bộ đã có `PERFECT` từ trước.

## Bỏ qua và phần cần xem

- Không chạy build. Không đổi nhánh, commit hoặc sửa kit, sim, lab; giữ nguyên các thay đổi có sẵn của agent khác.
- Không tạo ảnh hay âm thanh mới. Không sửa `results.ts`, `review-card.ts`, `feedback-profile.ts` vì nội dung cần kiểm đã đúng.
- Không chạy Chrome/Vite hoặc ghi capture ngoài vùng được phép của sandbox. Vì vậy chưa có JSON/video mới từ bản chơi, chưa xác nhận trực quan hạt ở 1280×720 và chưa tuyên bố đạt chấm mù.
- Claude chạy script với host 3008 đã phục vụ, từ thư mục game: `WORD_FX_TICKET=413 WORD_FX_TOPIC=word-fx-413 node tests/ui/word-fx-capture.mjs`. Kết quả vào `typing-game-review/owner-review/2026-11-16/tu-tien/word-fx-413/`; script giữ quy trình ABOUT, dọn khung hình và cập nhật index có sẵn.
- Anh cần xem clip/bảng khung hình ở 1280×720; đối chiếu `travelPx` với các khoảng mục tiêu. Đây là đỉnh tâm chữ quan sát được sau kẹp viewport, trước cắt vùng bảo vệ, không phải phép đo pixel mực còn nhìn thấy. Lấy mẫu theo khung hình có thể hụt nhẹ đỉnh rơi; nếu viewport làm rơi ngắn, JSON ghi số thực thay vì ép về 50–80 px.
