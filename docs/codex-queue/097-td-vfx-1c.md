# Phiếu 097 · Lời Gọi · Ảnh VFX cho bộ đòn 3D của map 1: Ghost Flame, vết nứt rễ báo trước, dải bọt thác

**Vì sao:** kiểm kê map 1 ngày 28/10 (I4, I5, P1, cổng G3). Ở bước 1C, map 1 của Lời Gọi lên 3D. Ba hiệu ứng chưa có ảnh:
- **Ghost Flame** (ma trơi): không có model, chỉ là VFX. Prompt của tờ khung đã có, nhưng chưa có ảnh.
- **Đòn báo trước của boss Mộc Tinh** cần một decal vết nứt rễ trên mặt đất.
- **Thác Bạc** cần dải bọt chảy lặp được.

11 flipbook cũ đã được chấm lại ở phiếu 043, nên phiếu này không làm lại phần đó.

**Báo cáo:** `docs/codex-queue/097-report.md`.

## Luật chung

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh ghi vào `games/typing-defense/art-src/vfx/` (media, không vào Git).
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Tối đa 3 lượt tạo mỗi ảnh.
- **Chỉ được ghi:**
  - `games/typing-defense/art-src/vfx/{ma-troi-sheet,root-crack,falls-foam}.*` theo mẫu tên: `.tryN.png`, `.tryN.prompt.txt`, `.tryN.alpha.png`;
  - bản chọn `<tên>.png`, `<tên>.alpha.png`, `<tên>.prompt.txt`. Riêng `ma-troi-sheet.prompt.txt` **đã có**: không ghi đè; prompt dùng thật ghi ở `ma-troi-sheet.tryN.prompt.txt`;
  - `tools/art-normalize/.tmp/097/` (thư mục WORK của công cụ);
  - `games/typing-defense/art-src/_review/097-*.jpg` và `_review/097/`;
  - file báo cáo.
- **Cấm:** ghi đè, đổi tên, xóa file có sẵn hay file `.try*`; mọi lệnh git; sửa mã hay tài liệu khác; dev server, trình duyệt, mạng ngoài công cụ tạo ảnh; đụng game khác; đọc hay ghi Tu Tiên; chữ, số, logo trong ảnh.

## Chuẩn alpha

Như phiếu 043, §Việc 2 (`docs/codex-queue/043-td-vfx-images.md`):
- tách nền bằng `tools/art-normalize/key-alpha.sh` (đọc README công cụ);
- flipbook đưa về 1024×1024, lưới 4 × 4, ô 256, mỗi ô có viền 4 px alpha 0;
- px có alpha 0,05–0,95 không mang màu nền.

Đọc khối VFX §3.6 và dòng nền §3.8 ở `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md`. Đầu prompt là khối STYLE §3.1. Xem `ma-troi-wisp.alpha.png`, `ink-smoke.alpha.png`, `paper-burn.alpha.png` để giữ cùng bộ.

## Ba ảnh

| Tên | Loại | Nền khi tạo | Mô tả |
|---|---|---|---|
| `ma-troi-sheet` | FLIPBOOK lặp, 16 khung | K (đen, cộng màu) | Theo đúng `ma-troi-sheet.prompt.txt` có sẵn. Ngọn lửa ma xanh lam nhạt pha ngọc, lõi sáng, đuôi lửa uốn; khung 16 nối liền khung 1 |
| `root-crack` | ảnh đơn 1024×1024, nhìn thẳng từ trên | M hay B (vết có xanh rêu) | Vết nứt đất tỏa từ tâm theo 5–7 nhánh như rễ cây, mép nứt nâu đất, trong khe có ánh lục vàng (màu Mộc Tinh) phẳng, không tỏa sáng. Dùng làm vùng báo trước đòn: game sẽ phóng to dần nó trong 0,8–1,2 s. Tâm cách mép ảnh ≥ 15 %, nhánh không chạm mép |
| `falls-foam` | dải 512×1024, **liền mép trên và dưới**, alpha | G hay B | Bọt nước trắng bạc và vệt nước chảy dọc, chảy từ trên xuống, mảng bọt to gọn, mép mềm vẽ bằng hai ba dải tông, không mờ. Game cuộn dải này theo trục dọc |

Với `falls-foam`, sau khi tách alpha thì làm liền mép trên và dưới bằng cách của phiếu 095 ("Làm liền mép"), chỉ theo trục Y.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/vfx/` trước (`_review/097/md5-before.txt`) và sau. `diff` chỉ có dòng của file mới; `ma-troi-sheet.prompt.txt` giữ md5.
2. **Khổ và lưới:**
   - `ma-troi-sheet.alpha.png` 1024×1024, 16 ô 256, mỗi ô có viền 4 px alpha 0, hình cách mép ô ≥ 24 px ở bản gốc;
   - `root-crack.alpha.png` 1024×1024;
   - `falls-foam.alpha.png` 512×1024.
3. **Alpha sạch:** min 0, max 255; px alpha 0,05–0,95 không mang màu nền (ví dụ nền xanh lá: G không trội hơn cả R lẫn B quá 40/255); đốm rời nhỏ hơn 20 px: 0.
4. **Vòng lặp:**
   - `ma-troi-sheet`: độ lệch trung bình khung 16 → khung 1 ≤ độ lệch lớn nhất giữa hai khung liền kề bên trong (in cả hai số);
   - `falls-foam`: `E ≤ 1,25 · I` theo trục Y như phiếu 093.
5. **Ảnh kiểm:**
   - `_review/097-sheet.jpg`: ba bản chọn trên nền đen, trên nền ô vuông xám, và trên nền xanh cỏ `#7FA35B`;
   - `_review/097-loop.jpg`: Ghost Flame, 16 khung xếp một hàng cộng thêm khung 1 ở cuối; dải bọt lát 1 × 3 theo trục dọc.
6. **KA5 tự chấm:** 5 tiêu chí của §2.2, ở cỡ đầy đủ và ở cỡ trong game (một ô 64 px; vết nứt 256 px).

## Báo cáo `docs/codex-queue/097-report.md`

Tiếng Việt: bảng lượt và điểm; đầu ra sáu mục Kiểm; bản chọn và lý do.

**Xong khi:** ba ảnh có bản chọn tự chấm từ 8 và qua mục Kiểm 1–4. **Nhận** khi Claude chấm lại từ 8.
