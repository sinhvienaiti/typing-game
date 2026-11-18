# Wordwoven

Chạy `pnpm deploy:pack` để dựng game rồi kiểm thư mục `dist` bằng bộ kiểm gói của kit, với mã game `typing-defense`; lệnh dừng nếu build hoặc kiểm gói lỗi. Dùng `pnpm deploy:pack:local` cho bản demo ở nhà: chỉ miễn lỗi nguồn `typing-game.local`, các kiểm tra khác giữ nguyên. Đây là bước dựng và kiểm `dist`, chưa chép sang `.deploy/` hay đưa lên máy chủ; gói production phải qua kiểm trước khi triển khai.
