# Hồ sơ phiếu 242

Bộ được giao nằm trong ui/icons, danh sách `delivered.json`. Nguồn và prompt nguyên văn cạnh nhau. `assets.json` chứa nhãn/cỡ/cặp; `selection-delivery.json` là lựa chọn cuối.

Tái lập hậu kỳ, số đo và các ô bằng ImageMagick 7, Python 3 chuẩn (không mạng/phụ thuộc Python ngoài):

```sh
python3 docs/codex-queue/242/process-final.py docs/codex-queue/242/replay-01 docs/codex-queue/242/selection-delivery.json
python3 docs/codex-queue/242/audit.py replay-01
```

Mỗi lệnh yêu cầu tên thư mục chưa có và từ chối ghi đè. So ảnh trong replay-01 với final-delivery để kiểm pixel. `process.py`, process-v2/v3 và các candidates/final cũ giữ quá trình sửa, không phải bộ chọn. `proofs-v3.py` tạo tờ duyệt cuối; đầu ra cố định đã có nên script sẽ từ chối ghi đè. Nếu tái dựng tờ, tạo bản script mới trong thư mục này và đổi hậu tố đầu ra 242 cùng thư mục proof. `deliver-selected.py` cũng chỉ chạy một lần để không ghi đè tài sản.

`process-final.py` dùng alpha >128 cho opening/coverage/IoU, đo thêm IoU >16 và mép ≥128. Matte chỉ đổi alpha tối đa 16/255 ngoài biên 3 px, RGB giữ nguyên. Bản thu không threshold hay sharpen. Mọi phép thu trực tiếp từ master; báo cáo ghi ngoại lệ Lanczos.

Tờ đầu có nhãn dài bị cắt, v2 nới chiều rộng, v3 dùng chiều cao chữ bitmap đúng 60%; sheets-v4.py cắt vùng phóng theo cỡ từng icon. Dùng `art-src/_review/242-sheet-v4.jpg`, không dùng hai tờ cũ để chấm. Không có capture runtime trong hồ sơ.
