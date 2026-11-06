# B7 · Nút so sánh A/B trong panel lab

Đã làm trong `games/.wt-ic-lab-all`, nhánh `codex/lab-all`:
- Thêm `src/lab/ab-flags.ts`: một mảng khai báo đủ 9 cờ, nhãn và giá trị so sánh; thêm cờ mới bằng một dòng. Hàm đọc trạng thái và tạo URL thuần, không sửa URL đầu vào hay hành vi cờ hiện có.
- Nối mục gập **A/B** ở đầu panel trong `src/lab/skills-main.ts`, đóng mặc định; giữ chiều rộng 240 px và cuộn của panel. Mỗi lớp có một checkbox với nhãn tiếng Anh. Bấm nhãn hoặc ô sẽ tải lại trang, chỉ đổi cờ tương ứng; giữ các tham số khác, lựa chọn hệ/mục 8–9 đã có trên URL, tham số lặp và phần `#…`. Trạng thái lấy từ URL hiện tại; riêng Readability dimming bật bằng `readable=1`, các lớp còn lại mặc định bật.
- Thêm `tests/lab/ab-flags.test.ts`: 37 test Node cho đủ 9 cờ, mặc định/giá trị so sánh/giá trị lạ, bật và tắt, giữ lựa chọn và cờ khác, tham số lặp, thao tác lặp lại và không sửa URL đầu vào.

Kiểm tra: `npx --no-install tsc --noEmit` sạch; `npx --no-install vitest run --maxWorkers=4` qua **123 file / 1.494 test**; `git diff --check` sạch. Một số test cũ có cảnh báo manifest/WebGL trong môi trường Node nhưng không có test lỗi.

Không thêm phím tắt vì mục gập và checkbox đã hỗ trợ bàn phím sẵn, tránh trùng hotkey lab. Không build, mở cổng mạng, mở trình duyệt, sửa đường dẫn cấm hay chạy lệnh Git ghi. Chưa xác nhận hiển thị thực tế/video theo lệnh cấm trình duyệt. Chủ repo cần mở A/B, thử từng ô và xem panel có gọn, không che vùng chơi ở kích thước màn hình đang dùng.
