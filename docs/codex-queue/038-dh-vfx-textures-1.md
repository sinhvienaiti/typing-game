# Phiếu 038 · Rồng Giữ Ải · Ảnh VFX lô 1: vết nứt, vết cháy, sợi khói, dải quét (không flipbook)

**Luật:** ảnh 2D phải đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Chưa đạt thì sửa prompt, tối đa 3 lượt mỗi ảnh. Chuẩn VFX là `docs/games/VFX_STANDARD.md` §4.4, bảng "Lô 1"; đọc §3.5–§3.6 về màu và độ dễ đọc.

**Bối cảnh:**
- Làn VFX của Rồng đang dựng Sky Fire (Thiên Hỏa) đủ 5 pha. Pha I và F cần vết nứt đất có khe đỏ nguội dần thành vết cháy tối; quái cần dải quét khi ra đòn; đạn và chiêu cần sợi khói tối đi sau lớp sáng.
- Hôm nay các mặt nạ này sinh bằng mã (nhiễu Voronoi). Ảnh đạt thì thay vào.
- Dạng ảnh: **ảnh xám có alpha**. Màu lấy từ ramp lúc chạy, nên ảnh không có màu.

**Được ghi** (`art-src` là media, không vào Git):
- `games/dragon-hold/art-src/vfx/<tên>.png`, `<tên>.prompt.txt` (bản chọn); `<tên>.tryN.png`, `.tryN.prompt.txt`; ảnh trung gian của `tools/art-normalize` trong `tools/art-normalize/.tmp/` (WORK của công cụ);
- `games/dragon-hold/art-src/_review/038-*.jpg`, `_review/038/`;
- `docs/codex-queue/038-report.md`.

**Cấm:**
- ghi đè, đổi tên, xóa file có sẵn;
- ghi vào `public/assets`, `media.md5`, `pnpm media:push`;
- chạy git; sửa mã hay tài liệu khác;
- dev server, trình duyệt;
- đụng game khác, đụng Tu Tiên.

## Sáu ảnh

| Tên | Cỡ | Nội dung | Kênh |
|---|---|---|---|
| `fissure-a` | 512×512 | Vết nứt đất nhìn thẳng từ trên xuống: một tâm vỡ, 5–7 khe chính tỏa ra, nhánh nhỏ dần, mép khe sắc | Xám có alpha; khe sáng nhất, mép khe xám vừa, ngoài khe trong suốt |
| `fissure-b` | 512×512 | Như A, nhưng dài và lệch một phía (vết đòn quét) | như trên |
| `fissure-c` | 512×512 | Như A, nhỏ hơn, ít nhánh (vết đòn nhẹ) | như trên |
| `scorch` | 512×512 | Vết cháy xém tròn méo trên đất, nhìn từ trên: lõi đậm, rìa vụn tro tan dần, vài vệt bắn ra | Xám có alpha; lõi đậm alpha cao, rìa tan về 0 |
| `smoke-strand` | 512×128 | Một dải sợi khói mảnh xoắn nằm ngang, liền mép trái phải | Xám có alpha; mép trên và dưới tan về 0 |
| `sweep-strip` | 512×128 | Một dải vệt quét như vết móng hay vệt chém nằm ngang, đầu dày đuôi mảnh, liền mép trái phải | như trên |

## Việc

1. **Prompt:** dùng phong cách tranh vẽ tay của bộ `pine-river` (đọc `docs/games/dragon-lane/art-requests/m0/04-2d-ground-decals-backdrop.md`, mục Decal), nhưng là **hình xám đơn sắc** trên nền đen phẳng `#000000`, nhìn thẳng từ trên xuống, không phối cảnh, không chữ, không khung. Vật sáng trên nền đen để tách alpha theo độ sáng.
2. **Tạo alpha:** chuyển ảnh sang xám rồi dùng độ sáng làm alpha (đen = trong suốt). Có thể dùng `tools/art-normalize` (`key-alpha.sh`, `pad-margin.sh`) hoặc `magick` trực tiếp. Ghi lệnh vào `.prompt.txt`.
3. **Hai dải `smoke-strand`, `sweep-strip`:** làm liền mép bằng `tools/art-normalize/seamless.sh … --axis x`. Kiểm bằng `seam-check.sh … --axis x --reference <ảnh trước seamless>`; `pass` phải là `true`.
4. **Tự chấm** theo 5 tiêu chí của `ART_ACCEPTANCE.md` §2.2, ở cỡ đầy đủ và ở 128 px trên nền đất của game (`games/dragon-hold/art-src/ground/pine-river/*.png`, nhân với một màu lửa cam để xem như lúc chạy). Đạt từ 8 thì dừng; tối đa 3 lượt.

## Kiểm (bắt buộc)

1. **md5:** chạy `md5 -r` cho mọi file trong `games/dragon-hold/art-src/vfx/` (nếu có) trước và sau. Chỉ có thêm file mới.
2. **Khổ và kênh:** `magick identify -format '%w %h %[channels]'` cho đúng khổ ở bảng, có alpha. Độ bão hòa trung bình ≤ 0,02 (ảnh xám).
3. **Mép alpha:**
   - Bốn ảnh vuông: viền 4 px quanh ảnh có alpha = 0 hoàn toàn.
   - Hai dải: mép trên và dưới 4 px có alpha = 0; hai mép trái phải liền nhau theo `seam-check` (`pass: true`).
4. **Độ phủ:** tỉ lệ px có alpha > 0,1. Vết nứt 6–25 %, vết cháy 25–55 %, hai dải 15–45 %. Ghi số; ngoài khoảng thì ghi lý do.
5. **Tờ xem nhanh** `_review/038-sheet.jpg`:
   - hàng 1: 6 ảnh trên nền ô bàn cờ;
   - hàng 2: 6 ảnh nhân màu (lửa cam cho nứt, cháy; tím mục cho quét, khói) đặt trên một ô đất `pine-river`;
   - có nhãn;
   - một bản nền tối.

## Báo cáo `docs/codex-queue/038-report.md`

- Bảng `| Ảnh | Lượt | Prompt thêm hay sửa | Điểm 5 tiêu chí | Tổng | Độ phủ | Còn thiếu |`.
- Lệnh tách alpha và seamless đã dùng.
- Đầu ra 5 kiểm.

**Xong khi:** cả 6 ảnh có lượt đạt từ 8, hoặc đủ 3 lượt và đã ghi bản tốt nhất kèm lý do.
