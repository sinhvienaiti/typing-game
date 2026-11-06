# Phiếu 305 · Một lệnh đọc trạng thái làm việc

Đã tạo `tools/agent-status/status.py`, `tools/agent-status/test_status.py` và `tools/agent-status/README.md`. Script dùng thư viện chuẩn Python 3.9, tự tìm gốc repo từ vị trí file; chỉ GET tới `127.0.0.1`, timeout 2 giây, tắt proxy và chuyển hướng. Đọc đủ video, âm, lab, Codex, queue, swap và SSD; nguồn thiếu/hỏng hiện `down` hoặc `missing`, thoát 0.

**Kiểm tra:** `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tools/agent-status/test_status.py` qua **14 test**. Đã kiểm tra cổng đóng, đếm MP4, các trạng thái âm (kể cả `round 1 done`), thư mục mới nhất, giới hạn ba nhật ký, HTTP lỗi, chặn URL ngoài máy, timeout, proxy, chuyển hướng, ngưỡng cảnh báo và JSON đủ sáu khóa khi chạy từ thư mục khác. Cú pháp hai file Python tương thích 3.9. Không tạo `__pycache__`.

Chạy thật `python3 tools/agent-status/status.py`: **11 dòng, mã thoát 0**, kết quả:

```text
giờ: 08:57
video: down · missing việc xong · missing take · còn 142 · mới nhất earth-ribbon-loop 08:56
âm: down · 349 xong · 0 lỗi · 19 dở · 0 chờ · mới nhất tt-sfx-x-heaven-earth-titan-avatar 08:57
lab: down · HTTP missing
thư viện: down · HTTP missing
codex: 3 nhật ký trong 24 giờ
codex-lane-mac-305.out: 06/11 08:51 start 305-agent-status-script (gpt-6.1-sol, xhigh, workspace-write)
codex-lane-mac-304.out: 05/11 22:56 queue done
codex-lane-mac-303.out: 05/11 22:42 queue done
queue.sh: missing
máy: swap missing · SSD trống 1787.29 GB
```

**Giới hạn cần chủ xem:** trong phiên sandbox này các yêu cầu HTTP nội bộ không kết nối được; `ps` và `sysctl` không đọc được. Vì vậy chưa xác nhận được trạng thái dịch vụ, queue và swap ngoài sandbox; các mục trên thể hiện khả năng đọc của phiên này. Dữ liệu file và dung lượng SSD đọc được. Chủ có thể chạy lệnh trên trong Terminal để xem trạng thái máy đầy đủ.

Không bỏ hạng mục triển khai nào. Không sửa ngoài bốn đường dẫn được phép, không dùng lệnh Git ghi, không chạy build/test game, không mở cổng hoặc gửi dữ liệu ra ngoài máy.

