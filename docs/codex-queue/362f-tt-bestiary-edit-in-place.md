# Phiếu 362f · Tu Tiên · Bốn loài thường: sửa trên chính ảnh đã duyệt, yêu hoá riêng từng loài

Hai giám khảo mù chấm bộ quái với boss v7 được 7,2 và 7,4 (`docs/codex-queue/371-report.md`, `371b-report.md`); tiêu chí thấp nhất ở cả hai là **(e) chất tiên hiệp và độc đáo**: bốn loài thường chung một công thức "thú + mảng đá vai khắc vân". Lần vẽ lại từ đầu (phiếu 362e, bản 5) trôi thành tròn trịa kiểu đồ chơi nên bị loại. Lần này **sửa trên chính ảnh đã duyệt** (image edit), giữ nguyên dáng, lông, ánh sáng, khuôn mặt, khung, lề; chỉ đổi phần được nêu. Anh để điều phối tự làm theo đề xuất (12/11 22:3x).

Lô: 8 ảnh (4 loài × 2 góc)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/bestiary-v4-vs-v5.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 20 lần `image_gen`** (chế độ sửa ảnh, đưa ảnh gốc vào), `view_image` tối đa 24. Báo cáo `docs/codex-queue/362f-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/beasts/{hoa-nha,nham-vien,thach-thu,thiet-giap-tru}.v6-{q,front}-final.png` (và `-raw`), một `.prompt.txt` cho mỗi ảnh final (ghi ảnh gốc đã sửa), tấm ghép `A/beasts/bestiary-362f-sheet.jpg`. Giữ nguyên mọi bản cũ. Cấm git ghi, sửa hay xoá file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Ảnh gốc để sửa (đưa vào image_gen) và đúng một thay đổi mỗi loài
| Loài | Ảnh gốc | Đổi gì (chỉ chỗ này) |
|---|---|---|
| Thiết Giáp Trư | `A/beasts/thiet-giap-tru.v3-q-final.png`, `.v3-front-final.png` | bỏ mảng giáp vai khắc vân; thay bằng **một sống đá liền khối mọc từ sọ chạy qua gáy, vai tới giữa lưng như dãy núi nhỏ**, đá nứt có khe trọc khí tím rất mờ; nanh hoá đá nối liền với sống đá ở hàm |
| Nham Viên | `A/beasts/nham-vien.v3-q-final.png`, `.v3-front-final.png` | bỏ mảng giáp vai khắc vân; thay bằng **hai cẳng tay và nắm tay hoá đá nứt** (đá mọc ra từ da, mép đá lẫn vào lông), vân dung nham nguội xám tro trong khe nứt; trên vai một **vân linh thú lớn** (giám khảo 371b nêu) khắc chìm vào da lông, không phải mảng giáp |
| Thạch Thử | `A/beasts/thach-thu.v4-q-final.png`, `.v4-front-final.png` | bỏ mảng giáp vai; thay bằng **vảy đá xếp như mái ngói chạy từ gáy tới đuôi** liền với da, gai lưng nhỏ lại; răng cửa đá to rõ |
| Hỏa Nha | `A/beasts/hoa-nha.v4-q-final.png`, `.v4-front-final.png` | bỏ mảng giáp vai khắc vân trên cánh; thay bằng **gốc cánh đá phân lớp** (giám khảo 371 nêu: các phiến đá xếp lớp mọc liền ở gốc cánh và vai) và **rìa lông cánh hoá mực loang, cháy tàn xám** (gom thành vài bó dày có gốc nối chắc, không sợi mảnh); mỏ và mắt như sắt nung nguội; mặt tách khỏi ngực bằng một mảng sáng tối rõ |
Giữ đúng cho mọi ảnh: tư thế, khuôn mặt, lông, ánh sáng, nền `#00FF00`, khung, lề ≥ 8 %, cỡ vật trong khung. Hai góc mỗi loài dùng cùng thay đổi, cùng bên. Không chữ, không bóng đổ, cấm màu tín hiệu cường độ cao.

## Kiểm và tự chấm
Script: lề, hai góc lệch chiều cao ≤ 5 %, một khối liền, alpha sạch; so ảnh mới với ảnh gốc ở vùng ngoài thay đổi (khác biệt trung bình nhỏ, để chứng minh không vẽ lại cả con). Tấm ghép: gốc | mới từng loài, và cả bộ (boss `A/kings/thiet-boi-lang-vuong.v7-q-final.png` + bốn loài mới) ở ô 66 px. Tự chấm sáu tiêu chí (a–f) trong `docs/codex-queue/368-tt-judge-bestiary.md` dòng 7; nếu ảnh mới trông như vẽ lại khác chất ảnh gốc thì làm lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; sửa Hỏa Nha và Nham Viên theo đúng hai báo cáo)
