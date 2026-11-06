# B6 · Lớp tụ lực theo hệ khi gõ từ

Đã làm sau B5 trong `games/.wt-ic-lab-all`, nhánh `codex/lab-all`:
- Thêm `src/lab/charge-fill-fx.ts`: dùng nguyên 14 atlas `charge-fill` đã có, khung phân số chạy theo số ký tự đúng / độ dài từ; dừng gõ thì giữ khung, sửa lùi thì lùi khung. Hỗ trợ các slot của phím 2–7; bỏ qua phím 0/1 và M.
- Nối trong `src/lab/skills-main.ts`: đọc từ trước/sau cập nhật gõ và ngay ký tự cuối. Hoàn tất tắt dần 0,12 giây; bỏ từ, thay từ hoặc đổi hệ tắt lớp cũ trong 0,2 giây. Nạp trước riêng atlas hệ được chọn, không đợi atlas trong đường bung chiêu; KTX2 mặc định, PNG dự phòng. `?chargefill=0` không nạp manifest/atlas và không vẽ lớp này.
- Tấm tranh ở khoảng 62% chiều cao người tung, rộng 1,2 lần bề ngang thân ước lượng bằng 35% chiều cao. Kiểm tra chiều sâu, dịch chiều sâu về sau thân, không ghi chiều sâu; giữ mặt nạ chữ có sẵn. Tổng đóng góp RGB của các lớp tụ lực chồng nhau tối đa 0,9 mỗi kênh. Tái dùng pool/bộ đệm, tối đa 8 lớp chuyển tiếp; đầy pool thì bỏ lớp hình mới, không giữ chiêu.
- Thêm `tests/lab/charge-fill-fx.test.ts` (19 test); cập nhật một kỳ vọng trong `tests/lab/ambient-fx.test.ts` cho điều kiện bật KTX2 chung. Kiểm tra tiến độ, dừng/sửa gõ, hoàn tất/bỏ/đổi từ, đổi hệ, cờ URL, vị trí/chiều sâu/chữ/độ sáng, nạp trễ và PNG dự phòng. Chạy chính hàm gõ/flush của lab trong Node: ký tự cuối vẫn bung/cast trong cùng lượt xử lý khi atlas chưa nạp; phím 7 vẫn tung ngay.

Kiểm tra: `npx --no-install tsc --noEmit` sạch; `npx --no-install vitest run --maxWorkers=4` qua **122 file / 1.457 test**. `git diff --check` và kiểm tra khoảng trắng hai file mới sạch. Manifest có đủ 14 mục đúng vai/hệ/tên và đủ 14 file KTX2.

Giới hạn có sẵn được giữ nguyên theo lệnh cấm đổi thời gian/sự kiện: phím 7 luôn tung ngay, kể cả chế độ gõ, nên hiện không có quãng gõ để hiện tụ lực; phím 6 vẫn vào cut-in rồi mới bung. B6 không thêm độ trễ, nhưng không thể xác nhận mọi phím bung trong ≤50 ms do luồng cut-in có sẵn và chưa đo trên trình duyệt.

Không tạo ảnh/âm thanh, không sửa `art-src`, `src/view`, `src/sim`, `src/content` hay sound; không build, mở cổng, mở trình duyệt hoặc chạy lệnh Git ghi. Chưa nghiệm thu hình ảnh/8,5 điểm hay có video. Chủ repo cần xem cỡ/vị trí lớp quanh thân, các khung cuối nguồn tranh, khả năng đọc chữ và fade khi đổi hệ trong lab; so sánh bằng `?chargefill=0`, đo độ trễ thực tế và quyết định riêng về luồng gõ phím 7/cut-in phím 6 nếu muốn thay đổi.
