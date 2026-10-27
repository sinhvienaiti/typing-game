# Phiếu 012d · Sửa `tools/art-normalize` lần 3 theo phản biện 012c

**Bối cảnh:** 012c sửa được nhiều (15/23 lỗi của 012b đã sửa hẳn, 8 sửa một phần; hoa tím D2 đã về, phông không còn bị co giãn). **Nhưng chưa đạt phản biện lần 3** (Claude, 4 góc, 26/10/2026 trên Mac mini M4): **2 lỗi lớn, 19 lỗi nhỏ**. Đầy đủ, có bằng chứng, script và cách sửa đề xuất: `.local/codex-runs/012c-review.json` (khóa `merged.findings`, `merged.review012b_status`, `merged.notes`; bản từng góc ở `reviews`). Script và ảnh của người phản biện: `tools/art-normalize/.tmp/review-claude-3/`. Đọc hết trước khi sửa.

**Thư mục làm việc:** gốc repo. Chỉ được ghi vào:
- `tools/art-normalize/`;
- `games/dragon-hold/art-src/`: chỉ file dẫn xuất của 012–012d, không đụng ảnh gốc, không đụng `art-src/3d/`;
- `games/dragon-hold/art-src/2d/README-normalize.md`.

Không chạy git. `export ART_MAGICK=/opt/homebrew/bin/magick`.

## Phải sửa: 2 lỗi lớn

1. **Phông B1 lộ đường nối thẳng trong ô** (cột 118–124, lặp mỗi 1.351 px; dãy núi xa gãy khoảng 10 px ở hàng 410–480), mà `seam-check` vẫn cho qua, kể cả cắt cứng và cắt ở cột sai nhất.
   - Thay đường cắt thẳng bằng **đường nối sai số nhỏ nhất theo từng hàng** (quy hoạch động hoặc graph-cut) cộng vùng hòa 2–4 px, hoặc chỉ cắt ở cột ít chi tiết.
   - Ghi lại vị trí đường cắt. Dựng lại B1 và ảnh xem mép; đính kèm ảnh cắt 1:1 hàng 0–600 quanh đường cắt.
   - `seam-check`:
     - thêm tiêu chí gián đoạn qua đường cắt (bước nhảy 2r+2 cột qua đường cắt, và bước độ sáng theo dải hàng, so với p99 phần trong và với các cột nguồn được nối);
     - kiểm sọc hàng trên **cả** dải trộn;
     - `--reference` so cửa sổ theo **đúng cột nguồn**, không theo vị trí đã chuẩn hóa;
     - phép bù lệch so với cột nguồn tương ứng; bắt được gập gương hẹp (≤ 12 px).
2. **Test chưa ghim các phần vừa sửa.** Nhiều bản cố tình làm hỏng (mutant) vẫn qua `test.sh`.
   - **Ca phải trượt:**
     - cắt cứng;
     - cắt ở cột sai nhất;
     - sọc ở chỗ cắt;
     - sọc một bên;
     - sọc cỡ 8–10;
     - tụt chi tiết giữa dải 0,75–0,85 (ở cả hai chế độ);
     - bù lệch rộng 30;
     - gập gương chỉ thấy qua `reference_mirror`.
   - **Ca phải qua:** độ chi tiết khoảng 0,93.
   - **Bảo vệ phần trong lòng vật:**
     - kiểm toàn bộ phần trong, cộng một vành 4–10 px vào trong;
     - ranh khử răng cưa giữa hai màu sơn;
     - sơn cùng sắc với màu khóa, cách nền 4–8 px;
     - viền tối có khử răng cưa.
   - **Ca túi nền của ảnh Tripo:** vành mềm phải qua; túi ≥ 64 px phải trượt.
   - **Unit test:** `key_residue`, `preserve_interior`, định dạng chữ ký và khung, `--keep-size`, khóa báo cáo.
   - **Chạy lại bộ mutant của người phản biện** (`.tmp/review-claude-3/code/mutate3.py`, `.tmp/review-claude-3/docs-tests/mutate3*.py`) và ghi trung thực mutant nào còn sống vào `REVIEW-012d.md`.

## Phải sửa: lỗi nhỏ (chi tiết trong JSON)

- `key()`:
  - chỉ đổi màu điểm ảnh viền giải thích được bằng pha màu khóa; không làm sáng sơn tối không phải màu khóa; không hạ alpha của điểm ảnh đục không phải ứng viên;
  - kẹp dư màu khóa ở viền cho vật không có sắc màu khóa (đốm xanh ở D1);
  - ghi rõ và **đếm** cách xử lý sơn màu khóa bão hòa trong lòng vật thay vì loại khỏi phép kiểm;
  - D3: tùy chọn theo job, hoặc ghi trong README;
  - chốt sắc độ để không ăn mất highlight của ảnh Tripo (`bush-blossom`).
- **Ghi file:**
  - hàm ghi của thư viện chặn đường dẫn bắt đầu bằng `-`;
  - đọc ảnh bằng đúng định dạng đã kiểm (không để file bị tráo thành SVG);
  - quyền file công bố như file thường (không 0600);
  - tín hiệu lúc dọn không để lại `.partial`;
  - không cài bộ bắt SIGHUP khi chỉ `import`;
  - phase 1 của bước công bố từ chối symlink treo.
- **Test khóa runner** không bao giờ chạy build thật: dùng ART/STAGE tạm hoặc đường khóa riêng.
- **Khổ canvas Tripo:** không phóng to ảnh nguồn; chọn khổ theo tỉ lệ vật (đã chọn theo đề xuất ở 012c).
- **Tài liệu:**
  - REVIEW không dẫn tới `.tmp`;
  - wrapper 012 bị khóa trỏ đúng chỗ;
  - `--shard` dùng thật hoặc bỏ;
  - ví dụ xy trong README phải tự qua `seam-check`.

## Làm lại ảnh

- Dựng lại B1, 8 decal, và icon nếu `key()` đổi. Bản 012c đổi hậu tố `.rejected-012c` (kèm kiểm hash). Giữ nguyên `.rejected-012`, `.rejected-012b` và mọi ảnh gốc.
- Cập nhật README-normalize với số đo thật trước và sau.

**Xong khi:**
- `test.sh` đạt, kể cả mọi ca phải trượt mới;
- 2 lỗi lớn đã sửa, có ảnh 1:1 làm bằng chứng;
- lỗi nhỏ đã sửa hoặc ghi rõ lý do;
- README khớp mã.

Claude phản biện lần 4 trước khi commit.
