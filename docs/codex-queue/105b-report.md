# Phiếu 105b · Rồng Giữ Ải · Về cổng game

## Kết quả

Đã làm phần mã và kiểm tự động của DH-24, cổng G5. Worktree
`games/.wt-dh-codex`, nhánh `dh-codex`, HEAD nền `50fbeab`; ban đầu sạch.
Mọi đường dẫn bên dưới tính từ worktree này.

Màn thắng/thua thêm liên kết “Về cổng game” cạnh nút chơi lại. Liên kết là
thẻ `<a>`, lấy `href` từ
`portalHome(import.meta.env.VITE_PORTAL_ORIGINS)`, có `target="_top"` và
nhãn phím lấy từ `keyLabel("enter")`. Enter gọi `.click()` trên phần tử
đang chọn nên liên kết dùng điều hướng gốc của trình duyệt.

Khi bảng đã mở, trái và phải đổi lựa chọn giữa hai nút, Enter kích hoạt
lựa chọn đó; mặc định là chơi lại mỗi lần mở. Tiêu điểm được thể hiện bằng
viền `is-focused`, theo cách UI giữ phím ở bộ định tuyến cửa sổ. Di chuột
vào nút cũng đổi lựa chọn. Kiểm mã nền: trái/phải chưa có tác vụ riêng trong
màn này; handler kết quả đứng trước handler camera và đã chặn các phím đó.

Esc và Enter giữ việc mở bảng ngay trong đoạn chờ thắng 2.600 ms. Trong
bảng, Esc tiếp tục bị chặn, lên/xuống chọn từ, Tab nghe từ. Nút và phím
chơi lại mức dễ hơn khi thua hai lần vẫn giữ nguyên.

## File đã làm

- `src/ui/results.ts`: liên kết, lựa chọn nút và gợi ý phím.
- `src/ui/styles/dh.css`: chỉ vùng CSS màn kết quả; hai nút cùng kiểu,
  cùng kích thước, viền lựa chọn và bố trí phần chân bảng.
- `tests/ui/results-screen.test.ts`: 10 test mới, dùng DOM giả trong Node;
  không sửa các test cũ hay bộ nhớ golden.
- `docs/changelog/2026-10-29-results-portal.md`: ghi thay đổi bằng tiếng Việt.
- Báo cáo này và thư mục `docs/codex-queue/105b/`: nhật ký và bằng chứng kiểm.

## Khung 1280×720

Hai nút vẫn nằm cùng một hàng, chia hai cột bằng nhau. Hàng gợi ý phím và
nút chơi mức dễ hơn (nếu xuất hiện) chuyển xuống dưới. Không cần chuyển
cặp nút sang hai hàng. Sổ Từ Ải vẫn là hàng riêng trong grid của bảng;
phần chân bảng không dùng định vị tuyệt đối để đè lên sổ.

Đối chiếu CSS tại 1280×720: `--ui = 0,8`, bảng rộng 608 px, giới hạn cao
688 px; nhóm hai nút rộng 352 px, cách nhau 9,6 px, mỗi cột rộng 171,2 px.
Danh sách từ giữ giới hạn cao 184 px và cuộn. Đây là kiểm cấu trúc và kích
thước khai báo, **chưa phải nghiệm thu hình ảnh**: test Node không đo dàn
trang, cắt chữ hay hành vi điều hướng thật của khung portal.

## Bốn mục kiểm bắt buộc

| Mục | Kết quả thực chạy | Bằng chứng trong `105b/` |
| --- | --- | --- |
| `pnpm check` trước sửa | Mã thoát 0; 53/53 file, 465/465 test; 6,08 s phần Vitest | `check-before.txt` |
| Test trước mã | Mã thoát 1; 10/10 test mới đỏ vì chưa có liên kết và lựa chọn nút | `tests-red.txt` |
| Test kết quả sau mã | Mã thoát 0; 2/2 file, 14/14 test | `tests-green.txt` |
| `pnpm check` sau sửa lần đầu | Mã thoát 1; 53 file xanh, 1 file đỏ; 474 test xanh, 1 đỏ; chỉ `tags-bodies` trượt ngân sách | `check-after.txt` |
| `tags-bodies` chạy riêng lần 1 | Mã thoát 0; 21/21 test, 230 ms phần test, tổng 1,19 s | `tags-bodies-retry-1.txt` |
| `tags-bodies` chạy riêng lần 2 | Mã thoát 0; 21/21 test, 140 ms phần test, tổng 1,14 s | `tags-bodies-retry-2.txt` |
| `tags-bodies` chạy riêng lần 3 | Mã thoát 0; 21/21 test, 147 ms phần test, tổng 0,99 s | `tags-bodies-retry-3.txt` |
| `pnpm check` cuối, sau khôi phục đột biến | Mã thoát 0; 54/54 file, 475/475 test; 7,14 s phần Vitest; kit, TypeScript, build xanh | `check-final.txt` |
| Golden giữ nguyên | `git -C games/.wt-dh-codex diff --stat -- tests/golden` rỗng, mã thoát 0 | `golden-stat.txt` (0 byte) |
| Đột biến bỏ riêng phím phải | Mã thoát 1; 4 test đỏ, 6 xanh; đã khôi phục trước lượt kiểm cuối | `mutation.patch`, `mutation-red.txt` |
| Phạm vi thay đổi | `git -C games/.wt-dh-codex status --short -uall` chỉ có đường dẫn được phép; không đổi HEAD | `status.txt`, `scope.json` |

Test ngân sách trượt ở 1,304696875 ms cho một lần bố trí, ngưỡng yêu cầu
dưới 1 ms. Không sửa test đó hoặc nới ngân sách; cả ba lần chạy riêng và
lượt kiểm cuối đều đạt. Tổng số test tăng **465 → 475** (+10).

Các test mới kiểm nguồn portal mặc định, rỗng và có nhiều origin; thẻ A và
`target`; click không chặn điều hướng gốc; phải rồi Enter; trái rồi Enter;
lên/xuống và nghe từ độc lập với lựa chọn nút; Esc/Enter bỏ qua chờ thắng;
hết thời gian tự mở bảng; lượt mới đặt lại lựa chọn; phím mức dễ hơn.
Đột biến chỉ xóa nhánh nhận `rotate-right`, không đụng phím trái, vì vậy
test thực sự bắt mất chức năng phím phải. Mã đột biến không còn trong nguồn.

## Phần chưa làm và bàn giao

Không chạy dev server, trình duyệt hoặc tạo media theo giới hạn phiếu.
Không chạy cập nhật golden; không dùng lệnh Git ghi; không sửa cây chính,
worktree khác, Tu Tiên, kit, sim, content hoặc typing. `pnpm check` có bước
build theo đúng kiểm bắt buộc của phiếu; không chạy thêm bộ build/test của
game nào khác.

Claude cần kiểm thắng và thua tại 1280×720, 1920×1080, cả khi mở trực tiếp
và trong portal: viền lựa chọn, nhãn phím theo máy, hai nút bằng nhau,
không tràn/đè Sổ Từ Ải, trường hợp có nút mức dễ hơn; dùng trái/phải/Enter
về đúng cổng ở toàn trang; Esc bỏ chờ thắng, lên/xuống và Tab vẫn dùng sổ.
G5 còn bước nghiệm thu trực quan và điều hướng thật này.
