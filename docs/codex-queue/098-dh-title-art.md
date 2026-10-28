# Phiếu 098 · Rồng Giữ Ải · Huy hiệu và nền màn tựa (map 1)

**Vì sao:** kiểm kê map 1 ngày 28/10 (DH-14, P1, cổng G5). Rồng chưa có màn tựa. Mở game là gặp ngay câu hỏi tốc độ gõ: không có tên game, nút bắt đầu hay hình ảnh mở đầu. Claude dựng màn tựa (DH-13). Phiếu này vẽ hai ảnh cho màn đó.

**Không vẽ chữ vào ảnh.** Tên "Rồng Giữ Ải" có dấu tiếng Việt, và công cụ tạo ảnh hay vẽ sai dấu. Claude đặt chữ tên game bằng font của game, đè lên huy hiệu.

**Báo cáo:** `docs/codex-queue/098-report.md`.

## Luật chung

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh ghi vào `games/dragon-hold/art-src` (media, không vào Git).
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Tối đa 3 lượt tạo mỗi ảnh.
- **Chỉ được ghi:**
  - `games/dragon-hold/art-src/ui/title/<tên>.tryN.png` và `.tryN.prompt.txt` (N = 1, 2, 3);
  - bản chọn `<tên>.png` kèm `<tên>.prompt.txt`;
  - `games/dragon-hold/art-src/_review/098-*.jpg` và `_review/098/`;
  - file báo cáo.
- **Cấm:** ghi đè, đổi tên, xóa file có sẵn hay file `.try*`; mọi lệnh git; sửa mã hay tài liệu khác; dev server, trình duyệt, mạng ngoài công cụ tạo ảnh; đụng game khác; đọc hay ghi Tu Tiên; **chữ, số, logo chữ, ký tự** trong ảnh.

## Phong cách

- Dòng **House style** nguyên văn của bộ Rồng, ở `docs/games/dragon-lane/art-requests/m0/01-creatures.md` (dòng bắt đầu bằng `House style:`).
- Ảnh tham chiếu (chỉ đọc):
  - cảnh map và hai con Rồng trong game: `games/dragon-hold/tmp/map1-audit/sheets/sheet-01-first-time-flow-1920.jpg`, `sheet-03-keyboard-only-1920.jpg`;
  - bộ cây đá `pine-river`: `games/dragon-hold/art-src/props/pine-river/pine-tall.png`, `bridge-old.png`, `rock-boulder.png`.
- **Hai con Rồng:** Hỏa Long đỏ lửa và Bạch Long trắng ngọc trai. Giữ đúng màu và dáng như trong game.
- **Luật màu của Rồng:** đỏ, cam và vàng kim là màu tín hiệu. Ngoài thân Hỏa Long, ảnh không có mảng đỏ, cam hay vàng kim lớn; cảnh nền giữ rêu xanh, xanh thông, tím nhạt, kem ấm.

## Hai ảnh

| Tên file | Khổ | Nền | Nội dung |
|---|---|---|---|
| `title-emblem` | 1024×1024 | alpha thật | Huy hiệu: Hỏa Long và Bạch Long cuộn quanh một vòm cổng đá cổ phủ rêu (cái "Ải"), hai đầu Rồng chầu vào nhau phía trên vòm. Hình khối to, gọn, đọc được ở 256 px và 128 px. Phía dưới vòm chừa một dải trống ngang (cao khoảng 18 % ảnh) để Claude đặt chữ tên game. Không khung tròn, không chữ |
| `title-backdrop` | 1536×1024 | đặc | Cảnh thung lũng của map L2-cau buổi sớm có sương mỏng: suối và cây cầu gỗ cũ, rừng thông, ở giữa xa là Bệ Rồng (Dragon Dais) có hai con Rồng đang nằm canh. 40 % bên trái là vùng êm, tối vừa, ít chi tiết, để đặt huy hiệu và menu. Không quái, không người, không chữ |

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `games/dragon-hold/art-src/ui/` (đệ quy) trước (`_review/098/md5-before.txt`) và sau. `diff` chỉ có dòng của file mới.
2. **Khổ:** `magick identify` đúng khổ ở bảng.
3. **Huy hiệu:**
   - alpha min 0, max 255, bốn dải 16 px sát mép có alpha 0 ở ≥ 99 % số px;
   - trên vùng alpha 1–254, luma trung bình ≤ 0,45 (không viền nền sáng);
   - dải trống cho chữ: ở hàng y 74–92 % của ảnh, trong khoảng x 20–80 %, px có alpha > 128 chiếm ≤ 15 %.
4. **Nền tựa:**
   - vùng x 0–40 % có độ rối (trung bình `|L − box5×5(L)|`) ≤ 70 % độ rối của vùng x 40–100 %;
   - luma trung bình vùng trái trong 0,20–0,45.
5. **Màu tín hiệu:** đếm px có hue 0–50°, S > 0,55, V > 0,5.
   - Ở nền tựa, ngoài vùng thân Hỏa Long (ước bằng hộp bao, ghi tọa độ): ≤ 2 %.
   - Ở huy hiệu thì chỉ ghi số.
6. **Không chữ:** xem bằng mắt cả hai ảnh ở cỡ đầy đủ; ghi "không thấy chữ, số, ký tự" hay chỉ chỗ.
7. **Ảnh kiểm:**
   - `_review/098-sheet.jpg`: huy hiệu trên nền tựa (thu còn 40 % chiều cao, đặt ở vùng trái), huy hiệu ở 256 px và 128 px trên nền tối và nền sáng;
   - nền tựa cắt 16:9 (1536×864, giữa).
8. **KA5 tự chấm:** 5 tiêu chí của §2.2.

## Báo cáo `docs/codex-queue/098-report.md`

Tiếng Việt: bảng lượt và điểm; đầu ra tám mục Kiểm; bản chọn và lý do.

**Xong khi:** hai ảnh có bản chọn tự chấm từ 8 và qua mục Kiểm 1–6. **Nhận** khi Claude chấm lại từ 8.
