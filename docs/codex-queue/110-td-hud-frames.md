# Phiếu 110 · Lời Gọi · Khung HUD "Sách tranh" 9-slice: gỗ và giấy

**Vì sao:** kiểm kê map 1 (I6 và C12, cổng G2). Khi map 1 lên 3D, HUD của Lời Gọi vẫn là bảng CSS phẳng. Người kiểm kê đề xuất khung gỗ và giấy vẽ tay nếu HUD bị chấm dưới 8. Phiếu làm sẵn hai bộ khung, để Claude thử ngay khi dựng C12 thay vì chờ.

**Báo cáo:** `docs/codex-queue/110-report.md`.

## Luật chung (phiếu ảnh)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Tối đa 3 lượt sinh mỗi ảnh.
- **Chỉ được ghi:**
  - `games/typing-defense/art-src/ui/frames/<tên>.*`, theo mẫu `.tryN.png`, `.tryN.prompt.txt`, bản chọn `.png`, `.prompt.txt`, `.alpha.png`, `.json`;
  - `games/typing-defense/art-src/_review/110-*.jpg` và `_review/110/`;
  - file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu;
  - dev server, trình duyệt;
  - đụng game khác, Tu Tiên;
  - chữ, số, logo trong ảnh.

## Phong cách

- Mở đầu prompt bằng nguyên văn khối **STYLE**, ở `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md` §3.1. Dòng nền theo §3.8: gỗ và giấy không có xanh lá, nên dùng nền G `#00FF00`.
- Xem các icon có sẵn ở `games/typing-defense/art-src/ui/buildings/`, `resources/`, cùng `ui/title-dusk.png`, để khung hợp với icon: viền mực, màu gỗ tre nâu ấm, giấy kem.

## Hai khung, mỗi khung 1024 × 1024, vẽ thẳng mặt, phẳng

| Tên file | Nội dung |
|---|---|
| `frame-wood` | Khung gỗ tre: bốn góc có khớp buộc dây mây và đinh gỗ tròn, bốn cạnh là thanh tre thẳng đều để kéo giãn được. Lòng khung là giấy kem sẫm nhẹ, phẳng, ít vân. Viền mực đều |
| `frame-paper` | Tờ giấy dó kem mép xé mềm, hơi cong ở góc, một vệt mực nhỏ ở góc trên trái. Lòng giấy phẳng, vân rất nhẹ, để chữ đen đọc rõ |

## Việc

1. Tạo ảnh. Tách nền thành `.alpha.png` bằng `tools/art-normalize/key-alpha.sh` (đọc README của công cụ).
2. **Chia 9-slice:** chọn bốn đường cắt (trái, phải, trên, dưới, tính bằng px) sao cho cạnh giữa là phần lặp hay kéo giãn được, không có chi tiết riêng. Ghi vào `<tên>.json`: `{ "size": 1024, "slice": { "left": L, "right": R, "top": T, "bottom": B }, "fill": "#rrggbb" }`, trong đó `fill` là màu trung vị của lòng.
3. Làm thử bằng ImageMagick: dựng mỗi khung ở 3 cỡ (480 × 160, 320 × 320, 720 × 120) theo 9-slice, kéo giãn cạnh giữa, giữ nguyên góc.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/ui/` (đệ quy) trước (`_review/110/md5-before.txt`) và sau. `diff` chỉ có dòng của file mới.
2. **Alpha sạch:** min 0, max 255. Px alpha 0,05–0,95 không mang màu nền: G không trội hơn cả R lẫn B quá 40/255. Đốm rời nhỏ hơn 20 px: 0.
3. **Cạnh kéo được:**
   - trong dải cạnh giữa (giữa hai đường cắt), độ lệch chuẩn luma theo chiều kéo ≤ 0,05;
   - không có chi tiết riêng (đinh, nút buộc) nằm trong dải đó.
4. **Lòng đọc chữ được:** in thử chữ đen "Gỗ 120 · Lúa 40" cỡ 24 px lên lòng khung: tương phản WCAG ≥ 7.
5. **Tờ** `_review/110-sheet.jpg`:
   - hai khung gốc;
   - ba cỡ dựng thử của mỗi khung;
   - mỗi khung đặt trên `games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png`.
6. **KA5 tự chấm:** 5 tiêu chí của §2.2.

**Xong khi:** hai khung có bản chọn tự chấm từ 8 và qua mục Kiểm 1–4. **Nhận** khi Claude chấm lại từ 8.
