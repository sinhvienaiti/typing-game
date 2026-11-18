# Phiếu 362c · Tu Tiên · Bộ quái v3: bốn loài theo chuẩn boss đã duyệt

Anh duyệt boss v3 (12/11 18:2x: "Đạt, vẽ tiếp"). Vẽ bốn loài còn lại theo **đúng chuẩn và khí chất** của boss v3 (phiếu 362b, `docs/codex-queue/362b-tt-bestiary-feral.md` mục "Khí chất mới").

Lô: 8 ảnh (4 loài × 2 góc)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/boss-v2-vs-v3.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 16 lần `image_gen`**, `view_image` tối đa 20. Báo cáo `docs/codex-queue/362c-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/beasts/<loài>.v3-q-final.png`, `A/beasts/<loài>.v3-front-final.png` (và bản `-raw`), một `.prompt.txt` cho mỗi ảnh final (ghi đường dẫn tham chiếu), tấm ghép `A/beasts/bestiary-362c-sheet.jpg`. Giữ nguyên mọi file v2. Cấm git ghi, sửa hay xoá file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
- **Chuẩn và khí chất đã duyệt:** `A/kings/thiet-boi-lang-vuong.v3-q-final.png`, `A/kings/thiet-boi-lang-vuong.v3-front-final.png`.
- Thiết kế loài (chỉ lấy thiết kế): `A/beasts/hoa-nha.png`, `A/beasts/nham-vien.png`, `A/beasts/thach-thu.png`, `A/beasts/thiet-giap-tru.png`; mô tả `docs/games/tu-tien/art-requests/m0b/02-five-families.md`.

## Bốn loài (`<loài>` = `hoa-nha`, `nham-vien`, `thach-thu`, `thiet-giap-tru`)
Mỗi loài lớn hơn thú thật 1,3–1,5 lần, dáng săn mồi hoặc lao tới, mặt hung lộ nanh hoặc mỏ, lông/da bết rách, sẹo, gai đá hoặc xương xuyên da, trọc khí mực đen loang và vân linh thú mờ; cùng ánh sáng, góc ba phần tư 32° từ trên, nền `#00FF00`, lề ≥ 8 %, không bóng đổ, không chữ, không hào quang vẽ sẵn, cấm màu tín hiệu ở cường độ cao.
- **Hỏa Nha:** quạ lớn đang sà xuống, hai cánh dang đủ, lông cánh rách như mực xé, mỏ nhọn há, mắt ánh than; có chân và móng rõ (Tripo cần đáy).
- **Nham Viên:** vượn đá đứng chồm, hai tay dài chống đất, vai và lưng mọc khối đá gồ ghề, hàm nanh lớn.
- **Thạch Thử:** chuột đá cỡ chó lớn, lưng gù gai đá, răng cửa dài, đuôi trụi có vảy đá.
- **Thiết Giáp Trư:** lợn rừng to như bò non, giáp sắt-đá tự nhiên trên lưng, nanh cong dài, đầu cúi lao húc.
Thứ tự: một loài xong cả hai góc rồi mới sang loài sau; cỡ vật trong khung theo bề rộng cơ thể, cùng mức với boss (vật chiếm 70–80 % bề ngang khung).

## Kiểm và tự chấm
Script: lề ≥ 8 %, hai góc lệch chiều cao vật ≤ 5 %, một khối liền, tách `#00FF00` không viền xanh. Tấm ghép: boss v3 + bốn loài v3 cùng cỡ, và ô 66 px. Tự chấm theo mặt yếu nhất (đáng sợ ở 66 px, cùng bộ với boss, dựng Tripo được); dưới 8 vẽ lại trong hạn lượt. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; ghi chú prompt.txt đã sửa)
