# Phiếu 370 · Tu Tiên · Boss Thiết Bối Lang Vương hướng A "Sói Núi Đá"

Anh chưa đạt boss v3–v5 ("ảnh boss vẫn chưa đạt", 12/11) và bảo nghiên cứu quái game tiên hiệp trước. Nghiên cứu: `docs/games/tu-tien/characters/BEAST_BOSS_RESEARCH_2026-11-12.md` (đọc mục 2, 3A, 3C, 4). Anh chọn **hướng A, mượn đôi mắt lệch của C** ("đồng ý, triển khai A cho tôi xem", 12/11 21:4x).

Lô: 2 ảnh (một boss × 2 góc)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/bestiary-v4-vs-v5.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/370-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/kings/thiet-boi-lang-vuong.v6-{q,front}-final.png` (và `-raw`), một `.prompt.txt` cho mỗi ảnh final (ghi đường dẫn tham chiếu), tấm ghép `A/kings/boss-370-sheet.jpg`. Giữ nguyên mọi bản cũ. Cấm git ghi, sửa hay xoá file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
- **Chuẩn ảnh và chất tả thực** (giữ đúng): `A/kings/thiet-boi-lang-vuong.v3-q-final.png`, `A/kings/thiet-boi-lang-vuong.v3-front-final.png`, `A/beasts/nham-vien.v3-q-final.png`.
- **Không theo** khí chất của `A/kings/thiet-boi-lang-vuong.v5-q-final.png` (tròn trịa, đọc như thú cưng). Không dùng ảnh nào ngoài repo.

## Hướng A, mô tả
- **Bóng:** sói khổng lồ bốn chân lực lưỡng, ngực ưỡn, đầu cao thẳng (không chồm thấp, không ngồi như chó); lưng nhô thành **một dãy 5–7 tảng đá tù xếp dọc sống lưng như dãy núi thu nhỏ**, tảng giữa cao nhất.
- **Tỉ lệ:** đầu khoảng 1/4 thân, cổ ngắn rất dày, vai cao hơn mông, chân trước to gấp rưỡi chân sau, móng đá lớn.
- **Vương miện:** một vòng sừng đá mọc từ xương trán, ba chóp lớn, liền khối với sọ. Bờm là các tấm vảy đá đặc chồng lớp quanh cổ, không lông xơ, không sợi.
- **Mặt (mượn C):** mõm dài, nanh lớn lộ, hàm dưới hơi lệch; **một mắt bị vảy đá đóng kín, mắt kia mở** với một điểm sáng trắng ngà trong hốc tối; mặt nhăn, dữ, không tròn đều.
- **Biến dị:** vết nứt chạy dọc sống lưng giữa các tảng đá, trong khe là mực than loãng; vài vết nứt tím rất mờ trên vai (dấu họ hàng chung với bộ quái).
- **Lông:** chỉ ở bụng, chân và đuôi, thành mảng dày bết, xám than; đuôi ngắn dày như khối đá phủ lông.
- **Màu:** nền xám than, tảng đá xám nhạt ấm, điểm nhấn duy nhất **trắng ngà ở mắt mở và ba chóp sừng**. Không đỏ tươi, cam, vàng kim, xanh ngọc. Không xích, không vòng cổ, không vật treo.
- Chuẩn bộ: ánh sáng như v3, góc ba phần tư 32° từ trên và chính diện, nền `#00FF00`, lề ≥ 8 %, vật chiếm 70–80 % bề ngang, không bóng đổ, không chữ, không hào quang vẽ sẵn.

## Kiểm và tự chấm
Script: lề, hai góc lệch chiều cao ≤ 5 %, một khối liền, alpha sạch. Tấm ghép: v3 | v6 hai góc, và v6 thu về ô 66 px nhìn từ trên (thu nhỏ chính ảnh final). Tự chấm sáu tiêu chí (a–f) trong `docs/codex-queue/368-tt-judge-bestiary.md` dòng 7, điểm cuối là tiêu chí thấp nhất; đặc biệt kiểm: ở 66 px có đọc ra dãy núi trên lưng, ba chóp sừng và điểm mắt sáng không; có còn đọc như chó cảnh không. Dưới 8,5 thì vẽ lại trong hạn lượt. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; thêm đường dẫn tiêu chí)
