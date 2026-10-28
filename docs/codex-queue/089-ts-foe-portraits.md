# Phiếu 089 · Tuyến Cuối · Sáu chân dung quái cho bảng tin ải (map 1)

**Vì sao:** kiểm kê map 1 ngày 28/10 (TS-M1-09, P1, cổng G2) thấy bảng tin trước ải chỉ có chữ, không có hình quái. Người mới không biết con nào là Brute, con nào là Shield Guard trước khi vào trận. Claude sẽ gắn ảnh vào bảng tin (TS-M1-10).

**Báo cáo:** `docs/codex-queue/089-report.md`.

## Luật chung

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh ghi vào `games/typing-survival/art-src` (media, không vào Git).
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Chưa đạt thì sửa prompt đúng chỗ thiếu, tối đa 3 lượt mỗi ảnh.
- **Chỉ được ghi:**
  - `games/typing-survival/art-src/ui/foes/<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3);
  - bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`;
  - `games/typing-survival/art-src/_review/089-*.jpg` và `games/typing-survival/art-src/_review/089/`;
  - file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - ghi vào `games/space-typing` (chỉ được đọc ảnh mẫu ở đó);
  - mọi lệnh git;
  - sửa mã hay tài liệu;
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, khung thẻ hay nền vẽ sẵn trong ảnh.

## Quái trông thế nào trong game

Quái của Tuyến Cuối dùng hình của bộ quái "rainbow" bên Space Typing, phủ một lớp vật liệu chung tên "Bầy Hố Đen" (`games/typing-survival/src/view/crowd.ts`, chú thích trên `STATE_HEAD`, và bảng màu ngay trên `LOOK`):

- thân tối và mờ, gần như than chì; vẫn giữ khối và bóng của hình gốc, nhưng **bỏ hết màu cầu vồng** của bản gốc;
- các gân năng lượng chạy qua thân, sáng rực;
- viền ngoài đen hút sáng, ngay bên trong có một đường chỉ nóng mảnh, như ánh sáng bị bẻ quanh chân trời sự kiện;
- thân hơi méo, như bị trọng lực kéo.

Ảnh mẫu hình dáng (chỉ lấy khối và bóng, không lấy màu): `games/space-typing/art-src/enemies/rainbow-<mẫu>.png`.

## Sáu ảnh

Khổ 1024×1024, **alpha thật**. Góc ba phần tư nhìn từ trước, hơi từ trên xuống. Quái đứng giữa, chân ở 82–88 % chiều cao ảnh. Mọi ảnh cùng khung và cùng ánh sáng: đèn chính lạnh từ trên trái, ánh cam ấm hắt từ phía sau như từ hố đen.

| Tên file | Tên (tiếng Anh) | Ảnh mẫu | Màu gân | Ghi chú |
|---|---|---|---|---|
| `swarm` | Swarm | `rainbow-mine.png` | cam nóng | nhỏ, tròn gai; trong ảnh, thân chiếm ~55 % chiều rộng |
| `scout` | Scout | `rainbow-scout.png` | xanh điện | nhanh, thân thon nghiêng về trước |
| `brute` | Brute | `rainbow-tank.png` | vàng hổ phách đậm | to, nặng, đầu cúi; thân chiếm ~80 % chiều rộng |
| `shield-guard` | Shield Guard | `rainbow-shield.png` | xanh lam, đường chỉ xanh | đi khom sau tấm khiên; khiên có viền năng lượng xanh |
| `splitter` | Splitter | `rainbow-splitter.png` | cam đỏ | thân phập phồng, có rãnh như sắp tách đôi |
| `pack-leader` | Pack Leader | `rainbow-tank.png` | vàng kim sáng | cùng hình với Brute nhưng to hơn, đầu ngẩng; gân dày và sáng hơn hẳn Brute, để nhìn là biết con đầu đàn |

## Việc

1. Chạy KA1 "trước" (xem Kiểm).
2. Viết prompt cho từng quái: phong cách "stylized game art, strong large shapes and restrained detail", gọn và rõ khối như model 3D trong game, cộng mô tả vật liệu ở trên và dòng của bảng. **Không** vẽ như ảnh chụp, không bề mặt ướt, không vân chi tiết dày. `title-horizon.png` bị ghi là lệch phong cách game (`docs/games/ART_REPLACE_LATER.md`, dòng title-horizon), nên không dùng nó làm mẫu. Dùng ảnh mẫu tương ứng làm tham chiếu hình. Ghi `.tryN.prompt.txt` cạnh mỗi lượt.
3. Làm `brute` trước. Dùng nó làm tham chiếu chất liệu và ánh sáng cho năm ảnh còn lại.
4. Tự chấm từng lượt theo 5 tiêu chí của `ART_ACCEPTANCE.md` §2.2, ở cỡ đầy đủ và ở 96 px. Ở 96 px phải phân biệt được sáu con chỉ bằng hình và màu gân. Đạt từ 8 thì dừng; chưa đạt thì sửa prompt, tối đa 3 lượt.
5. Chép bản chọn thành `<tên>.png` và `<tên>.prompt.txt`.

## Kiểm (bắt buộc, ghi số đo vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `games/typing-survival/art-src/` (đệ quy) trước, lưu `_review/089/md5-before.txt`, và sau. `diff` chỉ được có dòng của file mới.
2. **Khổ:** `magick identify` ra 1024×1024 cho cả sáu bản chọn.
3. **Alpha:** min 0, max 255. Bốn dải 16 px sát mép có alpha 0 ở ≥ 99 % số px. Trên vùng alpha 1–254, luma trung bình ≤ 0,35 (không viền nền sáng).
4. **Khung đều:** đo hộp bao của alpha > 16 bằng `magick <ảnh> -alpha extract -threshold 6% -trim -format '%X %Y %w %h' info:`.
   - Lề mỗi phía ≥ 48 px.
   - Đáy hộp bao nằm ở y 840–900.
   - Ghi bảng số đo của sáu ảnh.
5. **Không còn màu cầu vồng:** trên px có alpha > 128, px có saturation > 0,5 chiếm ≤ 25 % (gân thì sáng, nhưng thân phải tối và mờ). Ghi tỉ lệ cho từng ảnh.
6. **Tờ xem nhanh:**
   - `_review/089-sheet.jpg`: hàng 1 là sáu bản chọn ở 512 px trên nền `#0B0E14`; hàng 2 là sáu ảnh mẫu `rainbow-*.png` tương ứng, cùng cỡ; có nhãn tên tiếng Anh.
   - `_review/089-small.jpg`: sáu bản chọn ở 96 px và 64 px trên nền `#0B0E14`.

## Báo cáo `docs/codex-queue/089-report.md`

- Bảng `| Quái | Lượt | Prompt thêm hay sửa | Điểm 5 tiêu chí | Tổng | Còn thiếu |`.
- Bản chọn của từng quái và lý do.
- Đầu ra của sáu mục Kiểm, có số.

**Xong khi:** cả sáu ảnh có lượt tự chấm từ 8 và qua mục Kiểm 1–5. Nếu đủ 3 lượt mà vẫn chưa tới 8, ghi bản tốt nhất kèm lý do. **Nhận** khi Claude chấm lại từ 8.
