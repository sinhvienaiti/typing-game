# Phiếu 370b · Tu Tiên · Boss "Sói Núi Đá" bản 7: dãy núi cao, vương miện lớn, mõm sói, mặt gầm

Bản 6 (phiếu 370) đúng hướng A nhưng điều phối tự chấm khoảng 6,5: dãy núi trên lưng chỉ là gờ vảy thấp; sừng ba chóp nhỏ; góc chính diện đọc như gấu hay khỉ đột (đầu tròn, mõm ngắn, thân vuông); mặt bình thản, mất vẻ gầm dữ của bản 3. Anh để điều phối tự quyết sửa (12/11 22:3x).

Lô: 2 ảnh (một boss × 2 góc)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/boss-v3-vs-v6.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/370b-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/kings/thiet-boi-lang-vuong.v7-{q,front}-final.png` (và `-raw`), một `.prompt.txt` cho mỗi ảnh final (ghi đường dẫn tham chiếu), tấm ghép `A/kings/boss-370b-sheet.jpg`. Giữ nguyên mọi bản cũ. Cấm git ghi, sửa hay xoá file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
`A/kings/thiet-boi-lang-vuong.v6-q-final.png` và `-front-final.png` (giữ vảy đá, không xích, chuẩn ảnh); `A/kings/thiet-boi-lang-vuong.v3-q-final.png` và `-front-final.png` (lấy **khuôn mặt gầm, mõm dài, nanh lộ**). Hướng: `docs/games/tu-tien/characters/BEAST_BOSS_RESEARCH_2026-11-12.md` mục 3A.

## Sửa
1. **Dãy núi trên lưng:** 5–7 tảng đá tù **nhô cao rõ**, tảng giữa cao bằng khoảng 40 % chiều cao vai, tảng đầu và cuối thấp dần, xếp dọc sống lưng như dãy núi; khe giữa các tảng có vết nứt mực than. Nhìn từ trên đọc ra ngay.
2. **Vương miện:** sừng đá ba chóp mọc từ trán, **to gấp đôi bản 6**, chóp giữa cao nhất, liền khối với sọ, đầu chóp ánh trắng ngà.
3. **Đầu sói:** mõm dài và nhọn rõ ở **cả góc chính diện** (nhìn thẳng vẫn thấy mõm nhô ra trước, tai nhọn dựng), không đầu tròn như gấu; thân thuôn từ vai rộng xuống hông hẹp, chân dài hơn bản 6.
4. **Mặt gầm như bản 3:** mõm nhăn, há rộng, nanh dài lộ hết, một mắt bị vảy đá đóng, mắt kia sáng trắng ngà trong hốc tối.
Giữ: chuẩn bộ (ánh sáng, góc ba phần tư 32° và chính diện, nền `#00FF00`, lề ≥ 8 %, vật 70–80 % bề ngang), không xích, không vòng cổ, không lông sợi mảnh, cấm màu tín hiệu cường độ cao.

## Kiểm và tự chấm
Script: lề, hai góc lệch chiều cao ≤ 5 %, một khối liền, alpha sạch. Tấm ghép: v6 | v7 hai góc, và v7 ở ô 66 px. Tự chấm sáu tiêu chí (a–f) trong `docs/codex-queue/368-tt-judge-bestiary.md` dòng 7, thêm hai câu hỏi: góc chính diện có đọc ra sói (không phải gấu) không; ở 66 px có thấy dãy núi và vương miện không. Dưới 8,5 thì vẽ lại trong hạn lượt. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11)
