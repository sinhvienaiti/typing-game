# Phiếu 362 · Tu Tiên · Ảnh nguồn 3D bộ quái v2 (một bộ chuẩn), vẽ lại

Lần trước 26 ảnh trượt (cao nhất 7,45) vì **không phải một bộ**, chạm mép, cặp góc lệch tỉ lệ, thiếu chất tiên hiệp: `docs/games/tu-tien/art-requests/demo1/JUDGING.md` mục "Lỗi chung". Vẽ lại đúng theo `docs/games/tu-tien/art-requests/demo1/README.md`: **khối chuẩn §0** gắn vào mọi prompt, phần chủ thể theo §2.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 20 lần `image_gen`**, `view_image` tối đa 24. Báo cáo `docs/codex-queue/362-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/kings/*.v2-*.png`, `A/beasts/*.v2-*.png` và `.prompt.txt`, tấm ghép `A/beasts/bestiary-362-sheet.jpg`. Cấm git ghi, sửa hay xoá file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
Thiết kế đã duyệt giữ nguyên: `A/kings/thiet-boi-lang-vuong.png`, `A/beasts/{hoa-nha,nham-vien,thach-thu,thiet-giap-tru}.png` (chỉ lấy thiết kế, bỏ lối vẽ); `A/beasts/v2/phong-lang-q.v3-try*.png` (bản v2 gần nhất, để biết chuẩn đã đi tới đâu). Mô tả loài: `docs/games/tu-tien/art-requests/m0b/02-five-families.md`, `05-beast-kings.md`.

## Thứ tự (mỗi con 2 góc, cùng khổ 1:1, cùng tỉ lệ vật trong khung)
1. **Thiết Bối Lang Vương** `-q` và `-front` (§2.3). Vẽ trước, xem lại: nếu chưa ra chuẩn bộ thì sửa khối chuẩn rồi mới đi tiếp.
2. **Hỏa Nha** (quạ, đủ hai cánh, có chân và đáy để Tripo dựng), **Nham Viên**, **Thạch Thử**, **Thiết Giáp Trư**.
Mọi ảnh: một nguồn sáng trên phải 45°, painterly-realistic, ba phần tư 32° từ trên; nền `#00FF00` phẳng, lề ≥ 8 % mọi cạnh, không bóng đổ, không chữ; motif tiên hiệp (vân mây, hồi văn, lôi văn, vân linh thú, trọc khí mực), không Celtic, không động vật thật mặt hiền; Vương có dấu hiệu vương giả. Không hào quang vẽ sẵn. Màu cấm ở cường độ cao: đỏ tươi, cam, vàng kim, xanh ngọc.

## Kiểm và tự chấm
Đo bằng script: lề 4 cạnh ≥ 8 %, chiều cao vật giữa hai góc lệch ≤ 5 %, một khối liền. Tấm ghép: mười ảnh cạnh nhau cùng cỡ + ô 66 px từng con. Tự chấm theo mặt yếu nhất (một bộ, lề, tỉ lệ, chất tiên hiệp, dựng Tripo được); dưới 8 vẽ lại trong hạn lượt. Báo cáo ≤ 300 chữ, ghi lượt đã dùng.
