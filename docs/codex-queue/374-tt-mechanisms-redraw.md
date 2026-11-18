# Phiếu 374 · Tu Tiên · Ba cơ quan vẽ lại: Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng (ảnh nguồn 3D, M11)

`A/mechanisms/kiem-thung.png` 6,80, `loi-phu-tru.png` 6,80, `phong-an-vong.png` 7,10 (`docs/games/tu-tien/art-requests/demo1/JUDGING.md` A22–A24): không cùng bộ, kiếm kiểu châu Âu, sét zigzag phương Tây. Biểu tượng HUD của ba cơ quan đã có ở bộ giao diện jewel-crest anh duyệt: `A/ui/icons/hud-trap-{sword-stake,thunder-pillar,seal-net}-jewel-crest.v1-try1.png` (giữ nhận diện giống icon).

Lô: 6 ảnh (3 vật × 2 góc)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/ui-369-sheet.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 16 lần `image_gen`**, `view_image` tối đa 18. Báo cáo `docs/codex-queue/374-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/mechanisms/{kiem-thung,loi-phu-tru,phong-an-vong}.v2-{q,front}-final.png` (`q` = ba phần tư 32° từ trên, `front` = chính diện) (và `-raw`), một `.prompt.txt` cho mỗi ảnh final, tấm ghép `A/mechanisms/mechanisms-374-sheet.jpg`. Giữ nguyên file cũ. Cấm git ghi, sửa file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
Ba ảnh cũ trong `A/mechanisms/`, ba icon HUD jewel-crest ở trên, `A/kings/thiet-boi-lang-vuong.v7-q-final.png` (chuẩn ảnh).

## Hình
- **Kiếm Thung:** bệ đá thấp cắm ba thanh kiếm thẳng kiểu Á Đông (lưỡi hẹp thẳng, chuôi quấn dây chàm, đốc đồng), lưỡi chĩa lên xiên ra ngoài.
- **Lôi Phù Trụ:** trụ đá thấp quấn một dải bùa giấy lớn (khối dày, không giấy mỏng bay), đỉnh trụ là ấn đồng khắc lôi văn kiểu Á Đông (đường xoắn góc vuông), không ký hiệu tia sét zigzag.
- **Phong Ấn Võng:** khung đồng vuông nằm thấp trên bốn chân đá, giữa là lưới dây đồng đan chéo dày bản (không dây mảnh), bốn góc gắn ngọc trắng ngà.
Chuẩn ảnh chung (giữ đúng bộ quái đã duyệt): một nguồn sáng mềm trên phải 45°, painterly-realistic như `A/kings/thiet-boi-lang-vuong.v7-q-final.png`, góc ba phần tư 32° từ trên, nền `#00FF00` phẳng, lề ≥ 8 %, không bóng đổ, không chữ (không Hán, không Latinh), motif tiên hiệp Việt (vân mây, hồi văn, lôi văn), không Celtic, không triskelion, không sét zigzag phương Tây; cấm màu tín hiệu ở cường độ cao (đỏ tươi, cam, vàng kim, xanh ngọc); khối lớn, không chi tiết mảnh rời (để Tripo dựng).

## Kiểm và tự chấm
Script: lề, chiều cao vật giữa hai góc lệch ≤ 5 %, alpha sạch. Tấm ghép: cũ | mới | icon HUD, bản thu ở cỡ camera chơi. Tự chấm theo mặt yếu nhất (cùng bộ, khớp icon, chất Á Đông, dựng Tripo); dưới 8,5 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; lỗi phản biện nêu đã sửa)
