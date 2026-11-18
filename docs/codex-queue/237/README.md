# Hồ sơ phiếu 237

Báo cáo chính: [237-report.md](../237-report.md). Prompt thực tế, đường dẫn nguồn công cụ, tham số nền trong suốt và ảnh tham chiếu: [generation-log.json](generation-log.json).

Bộ chọn:

| Tên | Bản sinh | Thư mục hậu kỳ trong `art-src/_review/237/` |
| --- | --- | --- |
| keyboard | try2 | `keyboard-try2/` |
| bay-full | try3 | `bay-full-try3-fill736/` |
| streak | try2 | `streak-try2/` |

Mỗi thư mục hậu kỳ giữ nguồn hình học, mask, alpha, gốc, ba bản thu trực tiếp và số đo. File gốc chưa hậu kỳ giữ nguyên trong `art-src/ui/icons/<tên>.tryN.png`; prompt thực tế ở ngay cạnh. Không sinh lại ảnh khi chỉ muốn tái lập hậu kỳ.

## Tái lập hậu kỳ trong hồ sơ mới

Chạy từ repo cha trên macOS, dùng `/opt/homebrew/bin/magick` và Arial hệ thống. Không chạy build hay test game. Thay `replay1` bằng nhãn chữ/số mới nếu thư mục đó đã tồn tại; script từ chối ghi đè.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 games/typing-survival/art-src/_review/237/process.py keyboard 2 716 replay1
PYTHONDONTWRITEBYTECODE=1 python3 games/typing-survival/art-src/_review/237/process.py bay-full 3 736 replay1
PYTHONDONTWRITEBYTECODE=1 python3 games/typing-survival/art-src/_review/237/process.py streak 2 716 replay1
```

Các thư mục mới có hậu tố `-replay1`. Đối chiếu pixel RGBA của `.png`, `.64.png`, `.128.png`, `.256.png` với thư mục bản chọn trong bảng; không đòi byte PNG giống nhau vì metadata thời gian có thể khác. Thu đều, căn tâm và alpha có tham số ghi trong `measurements.json` từng thư mục. Không sửa RGB, không làm nét.

`prepare-delivery.py` kiểm đủ bộ và dựng thư mục `delivery/`; `proofs.py` dựng sheet/cỡ nhỏ/bến. Hai script này từ chối ghi đè proof có sẵn, nên không chạy lại trong hồ sơ đã giao. Khi tái lập toàn bộ, cần đổi đích sang một thư mục mới nằm dưới `_review/237*` và giữ nguyên đường dẫn đọc helper 149; không sửa hồ sơ 149.

`install.py` đã chạy một lần: kiểm số, sao lưu đủ 15 file vào `prev/`, kiểm MD5 trước phiên, rồi thay đúng ba tên. Không chạy lại để tránh chạm bản chốt. `audit.py` có thể chạy lại để kiểm MD5 15 ngoại lệ, backup, try1 và các file giữ nguyên; không có lệnh Git.

Tờ cần Claude xem trước: `art-src/_review/237-sheet-delivery.jpg`, `237/keyboard-try2-small.jpg`, `237/bay-full-try3-fill736-small.jpg`, `237/streak-try2-small.jpg`. IoU cao nhất 0,7968 là cặp clock–bay-full, sát ngưỡng 0,80. Chưa tự ghi nhận thay Claude.
