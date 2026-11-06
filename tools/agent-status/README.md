# Trạng thái điều phối trong một lệnh

Chạy từ gốc repo, Python 3.9 trở lên, không cần cài thêm thư viện:

```sh
python3 tools/agent-status/status.py
python3 tools/agent-status/status.py --json
```

Script tự tìm gốc repo từ vị trí file, nên cũng chạy được bằng đường dẫn script từ thư mục khác. Chỉ đọc file, chạy `ps`/`sysctl` và gửi GET tới `127.0.0.1`, timeout 2 giây mỗi yêu cầu; tắt proxy và không theo chuyển hướng. Không mở cổng, không sửa dữ liệu. Thiếu nguồn hoặc nguồn hỏng hiện `down`/`missing`, giá trị JSON không đọc được là `null`; mã thoát luôn 0.

- `giờ`: giờ máy theo HH:MM.
- `video`: receiver `/done`, số việc và tổng take của receiver; số việc trong danh sách chưa có file `*.mp4` trực tiếp trong thư mục mang tên `id`; tên và giờ sửa của thư mục đầu ra mới nhất. Hai cách đếm độc lập, không buộc khớp nhau.
- `âm`: receiver `/ping` phải trả `ok`; đếm `done` là xong, có `failed` là lỗi, có `round` là dở, còn lại là chờ. `failed` được xét trước `round`; `round 1 done` vẫn là dở. Cuối dòng là thư mục âm mới nhất và giờ sửa.
- `lab`, `thư viện`: trạng thái và mã HTTP của Skills Lab cổng 4310 và gallery cổng 4330; mã ngoài 2xx hiện `down`.
- `codex`: tối đa ba file `.local/codex-lane-mac-*.out` mới nhất có sửa trong 24 giờ, kèm dòng cuối không rỗng. Không có file gần đây hiện 0; không đọc được hiện `missing`.
- `queue.sh`: `chạy` khi `ps` chứa `tools/codex-run/queue.sh`, `không chạy` khi không thấy; `missing` khi không đọc được tiến trình.
- `máy`: swap đã dùng từ `sysctl vm.swapusage`, dung lượng trống của `/Volumes/SS990TPRO`. GB tính theo 1024³ byte. `RAM!` khi swap > 12 GB; `ĐĨA!` khi trống < 10 GB.

Dạng chữ tối đa 11 dòng. `--json` chứa cùng dữ liệu trong sáu khóa `time`, `video`, `sound`, `lab`, `codex`, `machine`, kèm trạng thái từng nguồn. Các hàm `read_*` nhận gốc repo và đường dẫn/URL/lệnh hệ thống tương ứng để kiểm tra bằng dữ liệu tạm.

Kiểm tra riêng công cụ, không chạy game hoặc mở máy chủ:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tools/agent-status/test_status.py
```

Biến môi trường trên tránh tạo `__pycache__` ngoài danh sách file của phiếu 305.
