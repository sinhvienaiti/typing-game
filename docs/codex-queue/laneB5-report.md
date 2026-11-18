# B5 · Lớp không khí trên sân lab

Đã làm trong `games/.wt-ic-lab-all`, nhánh `codex/lab-all`:
- Thêm `src/lab/ambient-fx.ts`: 3 tấm sương nằm sát sân ở mép xa và hai bên, chừa giữa sân; 1 tấm bụi đứng phía xa; 1 tấm tia sáng chéo ở góc trên xa.
- Nối trong `src/lab/skills-main.ts`: cập nhật bằng thời gian thực, bật KTX2 mặc định cho ambient. Nạp lười đúng 3 atlas qua `FlipbookLibrary`/`FlipbookPlayer`/`FlipbookPool`, giữ vòng lặp liên tục và tái dùng bộ đệm; không phát lại sprite hoặc tạo pool mỗi khung.
- Cường độ từng kênh tối đa lần lượt 0,25 / 0,20 / 0,18; alpha 0,50 / 0,45 / 0,40, vào dần trong 1 giây. Nhóm và mesh có `renderOrder=-100`, kiểm tra chiều sâu và không ghi chiều sâu: nằm dưới các lớp chiêu trong suốt, bị quái đặc che; thẻ chữ DOM vẫn ở trên canvas. Không đổi đèn, sương mù cảnh, tone mapping hoặc bloom.
- `?ambient=0` tắt toàn bộ lớp và không nạp manifest/atlas. Có API bật/tắt, thu hồi tài nguyên; giữ PNG dự phòng của thư viện khi KTX2 lỗi.
- Thêm `tests/lab/ambient-fx.test.ts`: 10 test cho bật/tắt, cờ URL, nạp lười KTX2, PNG dự phòng, vị trí, độ sáng, thứ tự nền/chiều sâu, vòng lặp, tái dùng bộ đệm và nạp xong khi đang tắt.

Kiểm tra: `npx --no-install tsc --noEmit` sạch; `npx --no-install vitest run --maxWorkers=4` qua **121 file / 1.438 test**; `git diff --check` sạch.

Không tạo ảnh/âm thanh mới; dùng nguyên atlas đã có. Không chạy build, mở trình duyệt hoặc cổng mạng theo ranh giới ticket, nên chưa có xác nhận hình ảnh hay video. Chủ repo cần xem độ mờ, vùng giữa sân và khả năng đọc chữ khi quái/chiêu hoạt động, đối chiếu với `?ambient=0`. Không sửa các đường dẫn cấm và không chạy lệnh Git ghi.
