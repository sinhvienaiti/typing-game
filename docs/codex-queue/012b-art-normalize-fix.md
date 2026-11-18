# Phiếu 012b · Sửa `tools/art-normalize` theo phản biện của Claude

**Bối cảnh:** phiếu 012 làm xong phần lớn nhưng **chưa đạt phản biện**. Ba góc phản biện: mã, an toàn, chất lượng ảnh. Kết quả có 1 lỗi chặn, 13 lỗi lớn, 19 lỗi nhỏ, đầy đủ ở `D:\typing-game\.local\codex-runs\012-review.json`. Đọc hết trước khi sửa. Ảnh gốc không bị hỏng.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `tools/art-normalize/`;
- `games/dragon-hold/art-src/`: chỉ file dẫn xuất của phiếu 012, không đụng ảnh gốc;
- `games/dragon-hold/art-src/2d/README-normalize.md`.

Không chạy git.

## Phải sửa

1. **Lỗi chặn: chốt không ghi đè.** Từ chối đường dẫn có `%`, `[`, hoặc tiền tố định dạng kiểu `png:`. Ghi kết quả bằng tạo-độc-quyền (`open(dst, 'xb')` hoặc `os.link` từ thư mục tạm). Thêm ca test cho từng trường hợp.
2. **`seamless`:** thay phép gập gương bằng phép trộn quấn vòng thật (roll nửa ảnh rồi hòa mép bằng mặt nạ mềm, hoặc cách tương đương).
   - `seam-check` và `test.sh` phải đo: hiệu cột đầu và cột cuối, so với trung vị hiệu hai cột kề; cộng một chốt chống ảnh đối xứng gương.
   - Bỏ phép thử `MAE == 0` vì nó luôn đúng.
3. **`key-alpha`:**
   - Không bỏ qua bước tách nền chỉ vì có 1 điểm ảnh alpha < 255. Chỉ coi là đã tách khi alpha có ý nghĩa thật, hoặc khi có cờ `--keep-alpha`.
   - Tách mềm theo khoảng cách màu, không ăn mòn mặc định; khử màu loang bằng phép tách màu nền.
   - Nét 2 px phải còn sau khi tách.
4. **`flat-bg` và `key-alpha`:** xử lý cả túi nền kín bên trong vật, ví dụ khoảng giữa cung và dây. Kiểm từng ảnh: đếm điểm ảnh gần màu nền mà chưa đúng `#E6E6E6`.
5. **Lỗi lớn và nhỏ còn lại** trong `012-review.json`, gồm:
   - `+repage` trong `fit()` và khi cắt 2×2;
   - lỗi `$WORK`;
   - các câu README không khớp mã.
6. **Dọn thư mục:**
   - `tools/art-normalize/.gitignore` cho `.tmp/`, `__pycache__/`, ảnh;
   - dời script chạy một lần cho Rồng (`normalize_dragon.py`, `finalize_dragon.py`, `refine*.sh`, `review_labels.sh`, các `*-dragon.sh`) vào `tools/art-normalize/jobs/dragon-hold-012/`.
7. **Làm lại ảnh của Rồng bằng công cụ đã sửa.** Ghi bản đạt vào đúng tên phiếu 012 quy định (`<tên>.alpha.png`, `pine-river-far.seamless.png`, `_review/pine-river-far.seam.png`). Bản cũ đổi hậu tố `.rejected-012`. Cập nhật README-normalize: số đo trước và sau, ảnh nào vẫn chưa đạt.

**Xong khi:**
- `test.sh` đạt với các ca mới;
- mọi lỗi chặn và lỗi lớn đã sửa, hoặc ghi rõ lý do không sửa;
- README khớp mã.

Claude sẽ phản biện lại trước khi commit.
