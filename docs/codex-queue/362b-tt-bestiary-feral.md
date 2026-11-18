# Phiếu 362b · Tu Tiên · Bộ quái v3: hoang dại, hung ác, đáng sợ; boss to lớn

Anh (12/11 sau khi xem boss v2 của phiếu 362): "nên được vẽ dạng hoang dại, nhìn đáng sợ hơn, hung ác hơn, to lớn hơn với boss, chứ bạn vẽ như sói cún thế kia thì k đạt". Phiếu 362 đã dừng. Bản v2 đúng chuẩn bộ (sáng, góc, lề, hai góc khớp) nhưng **sai khí chất**: dáng đứng hiền, lông mượt sạch, mặt bình thản, đọc như chó cảnh khoác giáp.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 20 lần `image_gen`**, `view_image` tối đa 24. Báo cáo `docs/codex-queue/362b-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/kings/*.v3-*.png`, `A/beasts/*.v3-*.png`, `.prompt.txt`, tấm ghép `A/beasts/bestiary-362b-sheet.jpg`. Giữ nguyên mọi file v2 (thư viện). Cấm git ghi, sửa hay xoá file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
- **Chuẩn bộ giữ nguyên** (ánh sáng, góc, lề, nền, cặp góc khớp): `A/kings/thiet-boi-lang-vuong.v2-q-final.png`, `A/kings/thiet-boi-lang-vuong.v2-front-final.png`. **Chỉ lấy chuẩn kỹ thuật, bỏ khí chất.**
- Thiết kế loài: `A/kings/thiet-boi-lang-vuong.png`, `A/beasts/{hoa-nha,nham-vien,thach-thu,thiet-giap-tru}.png`; mô tả `docs/games/tu-tien/art-requests/m0b/02-five-families.md`, `05-beast-kings.md`; khối chuẩn §0 trong `docs/games/tu-tien/art-requests/demo1/README.md`.

## Khí chất mới (mọi con)
- **Dáng săn mồi hoặc lao tới:** thân hạ thấp, vai gồ, đầu chúi về trước, chân trước choãi bám đất, cơ bắp căng; không đứng thẳng thong thả.
- **Mặt hung:** mõm nhăn, nanh dài lộ hết, mắt nhỏ sâu có ánh trọc khí, tai ép ra sau; nước dãi hoặc hơi thở mực.
- **Hoang dại:** lông xù, bết, rối thành mảng; sẹo cũ, da rách, gai xương hoặc đá mọc xuyên da; trọc khí mực đen loang và vân linh thú phát sáng mờ (không vượt 0,9 mỗi kênh) đọc được ở cỡ nhỏ.
- **Tỉ lệ:** quái thường lớn hơn thú thật 1,3–1,5 lần, chi to, vuốt dài. **Boss Thiết Bối Lang Vương** khổng lồ: thân dày như tê giác, lưng là sống núi đá gai, đầu to với hàm nặng, xích đồng đứt dang dở trên cổ như vừa phá ấn; vẻ cổ xưa, vương giả và tàn bạo.
- Giữ cấm màu tín hiệu ở cường độ cao (đỏ tươi, cam, vàng kim, xanh ngọc). Không hào quang vẽ sẵn, không bóng đổ, không chữ.

## Thứ tự
1. **Boss** trước: `A/kings/thiet-boi-lang-vuong.v3-q-final.png` và `A/kings/thiet-boi-lang-vuong.v3-front-final.png`. Xong boss thì **dừng phiếu**, ghi báo cáo, để chủ dự án duyệt mẫu trước khi vẽ các loài khác (luật "mẫu trước khi làm cả lô").
2. Phiếu sau sẽ vẽ Hỏa Nha, Nham Viên, Thạch Thử, Thiết Giáp Trư theo chuẩn boss đã duyệt.

## Kiểm và tự chấm
Script: lề ≥ 8 %, hai góc lệch chiều cao vật ≤ 5 %, một khối liền, tách `#00FF00` không viền xanh. Tấm ghép: v2 | v3 cạnh nhau ở cùng cỡ và ô 66 px. Tự chấm theo mặt yếu nhất (đáng sợ ngay ở 66 px, hoang dại, to lớn, chuẩn bộ, dựng Tripo được: có đáy chân rõ, không lông mảnh rời); dưới 8 vẽ lại trong hạn lượt. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; hai ghi chú đã sửa)
