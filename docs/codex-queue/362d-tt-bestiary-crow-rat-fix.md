# Phiếu 362d · Tu Tiên · Bộ quái v3: vẽ lại Hỏa Nha và Thạch Thử

Anh xem bộ v3 (12/11 19:5x): "về quái thì cũng tạm được". Luật anh 01/11: không có mức dùng tạm, phải 8,5. Hai con yếu nhất ở ô 66 px: **Hỏa Nha** mặt quá nhỏ, đọc như đại bàng; **Thạch Thử** tai hồng, lông sáng, giống chuột thường, chưa hung. Ba con còn lại (boss, Nham Viên, Thiết Giáp Trư) giữ nguyên.

Lô: 4 ảnh (2 loài × 2 góc)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/bestiary-v3.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/362d-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/beasts/{hoa-nha,thach-thu}.v4-{q,front}-final.png` (và `-raw`), một `.prompt.txt` cho mỗi ảnh final (ghi đường dẫn tham chiếu), tấm ghép `A/beasts/bestiary-362d-sheet.jpg`. Giữ nguyên mọi file v2, v3. Cấm git ghi, sửa hay xoá file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
Chuẩn bộ đã duyệt: `A/kings/thiet-boi-lang-vuong.v3-q-final.png`, `A/beasts/nham-vien.v3-q-final.png`, `A/beasts/thiet-giap-tru.v3-q-final.png`. Bản cần sửa: `A/beasts/hoa-nha.v3-q-final.png`, `A/beasts/hoa-nha.v3-front-final.png`, `A/beasts/thach-thu.v3-q-final.png`, `A/beasts/thach-thu.v3-front-final.png`. Khí chất: `docs/codex-queue/362b-tt-bestiary-feral.md` mục "Khí chất mới".

## Sửa
- **Hỏa Nha:** quạ yêu, không phải đại bàng: đầu và mặt to hơn (đầu khoảng 1/5 sải cánh), mỏ đen dày cong móc kiểu quạ, há mỏ kêu, mắt nhỏ ánh than đỏ sẫm (không đỏ tươi), lông cổ dựng xù như bờm, lông đen ánh dầu với rìa cháy xám tro, cánh rách như mực xé; chân và móng rõ, có đáy.
- **Thạch Thử:** bỏ tai hồng và lông sáng; da xám đá nứt và lông tro bết thành mảng, tai rách mép sẫm, mõm nhăn, răng cửa dài vàng ố, mắt nhỏ ánh trọc khí, lưng gù với gai đá to, đuôi trụi vảy đá; cỡ chó lớn, dáng chồm.
Giữ đúng chuẩn bộ: cùng ánh sáng, góc ba phần tư 32° từ trên và góc trước, nền `#00FF00`, lề ≥ 8 %, vật chiếm 70–80 % bề ngang, không bóng đổ, không chữ, cấm màu tín hiệu ở cường độ cao.

## Kiểm và tự chấm
Script: lề, hai góc lệch chiều cao ≤ 5 %, một khối liền, tách nền không viền xanh. Tấm ghép: v3 | v4 của hai loài, và cả bộ năm con ở ô 66 px. Tự chấm theo mặt yếu nhất (đọc ra quạ yêu và chuột đá hung ở 66 px, cùng bộ); dưới 8 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11)
