# Phiếu 352 · Tu Tiên · Ảnh 2D: trận pháp lôi bản nhạt (lớp nền, không tranh với tia sét)

Anh (12/11 10:0x) về phiếu 348: "sao k dùng màu nhạt hơn, vì tia lôi điện đã đậm r… cái nào cần nhấn mạnh, chứ có phải cái nào cũng đậm màu hết". Canon D64 (thứ bậc nhìn): trận pháp là lớp nền, tia sét là điểm nhấn. Chỉ vẽ ảnh, không sửa mã. Chạy sau các phiếu đang có trong hàng.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 5 lần gọi `image_gen`** (A nhạt, B nhạt, vành rời nhạt, tối đa 2 vẽ lại). `view_image` tối đa 8. Báo cáo: `docs/codex-queue/352-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-array-pale-*.v1-try*.png`, `.prompt.txt`, tấm ghép. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
`S/thunder-array-a.v1-try2.png` (bố cục A: bát quái, chữ triện, giữ nguyên bố cục), `S/thunder-array-b.v1-try2.png` (bố cục B), `S/thunder-array-ring.v1-try1.png` (vành rời), `S/thunder-five-strike.v2-try9.png` (tia sét sẽ nằm đè lên: trận phải nhạt hơn hẳn tia này).

## Màu mới (bắt buộc)
- Giữ **đúng bố cục và chi tiết** của A, B, vành rời; chỉ đổi màu và độ mạnh.
- Nét: **ngà nhạt ngả đồng cổ** (khoảng `#D9C9A8` tới `#B89F74`), độ bão hoà thấp, **không** ánh vàng đậm, không hổ phách rực; lõi và nút sét sáng vừa (trắng ngà), không chói.
- Độ sáng tổng của trận thấp hơn tia sét rõ rệt: vùng sáng nhất của trận ≤ 70 % giá trị sáng của lõi tia trong ảnh tham chiếu; nét mảnh; quầng mềm rất nhẹ; hạt sáng thưa.
- Tâm vẫn thoáng. Nền đen thuần, lề ≥ 10 %, tròn hoàn hảo, 1:1.

## Ba ảnh
`S/thunder-array-pale-a.v1-try1.png`, `S/thunder-array-pale-b.v1-try1.png`, `S/thunder-array-pale-ring.v1-try1.png`.

## Kiểm và tự chấm
Nền, lề, tròn; **đo độ sáng**: trung vị độ sáng (V) của các điểm sáng (V > 0,15) của trận và của tia tham chiếu, ghi tỉ lệ, phải ≤ 0,7; độ bão hoà trung vị của trận ≤ 0,45; vàng kim sáng 0 %. Tự chấm theo mặt yếu nhất: nhạt và lùi về nền nhưng vẫn đọc ra trận lôi huyền bí; giữ bố cục; tâm thoáng; sang. Dưới 8 vẽ lại một lần.

## Xong khi
3 ảnh + prompt + `S/thunder-array-352-sheet.jpg` (mỗi cột: bản đậm 348 trên, bản nhạt dưới, và một ô ghép thử tia sét `thunder-five-strike.v2-try9` thu nhỏ đè lên bản nhạt để thấy thứ bậc) + báo cáo có bảng số.
