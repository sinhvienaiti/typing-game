# Phiếu 362e · Tu Tiên · Bộ quái v5: yêu hoá riêng từng loài, boss vương giả, đọc ở 66 px

Anh (12/11 21:1x): "bộ quái sửa lại và tự chấm đi". Hai giám khảo mù chấm bộ v3/v4 được 7,0 và 7,3 (`docs/codex-queue/368-report.md`, `368b-report.md`); cả hai cùng nêu bốn lỗi, sửa đúng bốn lỗi này. Giữ chuẩn bộ (tiêu chí "cùng bộ" đã 8,2–8,6).

Lô: 10 ảnh (5 loài × 2 góc)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/bestiary-v4.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 26 lần `image_gen`**, `view_image` tối đa 30. Báo cáo `docs/codex-queue/362e-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/kings/thiet-boi-lang-vuong.v5-{q,front}-final.png`, `A/beasts/{hoa-nha,nham-vien,thach-thu,thiet-giap-tru}.v5-{q,front}-final.png` (và `-raw`), một `.prompt.txt` cho mỗi ảnh final (ghi đường dẫn tham chiếu), tấm ghép `A/beasts/bestiary-362e-sheet.jpg`. Giữ nguyên mọi bản cũ. Cấm git ghi, sửa hay xoá file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
Bản đã anh duyệt hướng: `A/kings/thiet-boi-lang-vuong.v3-{q,front}-final.png`, `A/beasts/{nham-vien,thiet-giap-tru}.v3-{q,front}-final.png`, `A/beasts/{hoa-nha,thach-thu}.v4-{q,front}-final.png`. Hai báo cáo giám khảo trên (đọc mục "Năm sửa cụ thể nhất").

## Bốn sửa
1. **Mỗi loài một kiểu yêu hoá riêng, mọc từ cơ thể**, bỏ công thức chung "giáp vai khắc vân + gai lưng" trên cả năm con. Giữ một dấu họ hàng chung nhỏ (vết nứt trọc khí tím mờ).
   - **Thiết Giáp Trư:** sống đá liền từ sọ qua vai tới lưng như dãy núi, nanh là đá mọc từ hàm.
   - **Nham Viên:** cẳng tay và khớp hoá đá nứt có vân dung nham nguội, bàn tay đá to.
   - **Thạch Thử:** thân phủ vảy đá xếp như mái ngói, răng cửa đá, đuôi là chuỗi đốt đá.
   - **Hỏa Nha:** lông cánh rìa hoá mực loang và cháy tàn, mắt và mỏ như sắt nung nguội.
   - **Thiết Bối Lang Vương:** xem sửa 2.
2. **Boss vương giả, tách hẳn quái thường:** đầu to, mõm dài rõ; bờm và vai dựng cao thành một vòng đá gai liền khối như vương miện; tư thế đứng thống trị (đầu cao hơn vai, ngực ưỡn), không chồm thấp như chó; to gấp 2,5 quái thường. Bỏ xích treo lủng lẳng: một vòng cổ đồng liền khối có ấn ngọc đứt.
3. **Đọc ở 66 px:** gom chi tiết nhỏ thành các mảng sáng tối lớn; mắt sáng rõ (một điểm sáng ấm-nhạt trong hốc tối), mõm hoặc mỏ há với khoảng tối miệng lớn; tách đầu khỏi thân bằng tương phản.
4. **Dựng Tripo:** gom lông cánh quạ thành ít bó dày có gốc nối; ngón và móng đủ thể tích, tách nhau; không vật treo, không sợi mảnh; đáy chân phẳng rõ. Hai góc mỗi loài dùng cùng sơ đồ vân, vết nứt, bên trái phải.
Chuẩn bộ giữ: ánh sáng, góc ba phần tư 32° từ trên và chính diện, nền `#00FF00`, lề ≥ 8 %, vật chiếm 70–80 % bề ngang (boss vẫn 70–80 % khung của nó), không bóng đổ, không chữ, cấm màu tín hiệu cường độ cao.

## Kiểm và tự chấm
Script: lề, hai góc lệch chiều cao ≤ 5 %, một khối liền, alpha sạch. Tấm ghép: v4 | v5 từng loài, và cả bộ v5 ở ô 66 px (thu nhỏ chính ảnh final bằng magick). **Tự chấm** theo đúng sáu tiêu chí của giám khảo 368 (a–f), điểm cuối là tiêu chí thấp nhất, ghi bảng điểm; dưới 8,5 ở tiêu chí nào thì vẽ lại loài đó trong hạn lượt. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; hai ghi chú đã sửa)
