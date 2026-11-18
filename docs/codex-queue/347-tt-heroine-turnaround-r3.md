# Phiếu 347 · Tu Tiên · Ảnh 2D: bộ bốn góc nhân vật chính, vòng 3 (sửa lỗi kỹ thuật và thêm lớp hoàng tộc)

Vòng 2 (phiếu 344) bị hai giám khảo mù chấm CHƯA (7,0 và 6,5). Anh đã chốt: **mặt donghua của vòng 2 được chấp nhận, giữ nguyên khuôn mặt đó**. Lỗi còn lại, cả hai giám khảo cùng nêu: (1) **mặt sau hai ủng ở ảnh sau vẽ sai**: mang hoạ tiết và mũi giày của mặt trước; (2) **góc camera chơi không đúng 55° nhìn xuống**; (3) ngọc bội và phụ kiện bất đối xứng không nhất quán giữa các góc; (4) thiếu khí chất hoàng tộc ở cấp hình khối: cần một lớp ngoài chàm có độ rủ và vai mềm hơn, một khối tà chính có bề dày, không chỉ thêm thêu; (5) tấm lưng chưa rõ là tấm cứng hay vải, chưa thấy bề dày và điểm gắn. Chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần gọi `image_gen`.** `view_image` tối đa 14. Báo cáo: `docs/codex-queue/347-report.md`.

## Đường dẫn
`H = games/immortality-cultivation/art-src/heroine`. Chỉ thêm `H/r3-*` và báo cáo. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
- `H/r2-view-front.v1-try2-normalized.png`: **chuẩn mặt, tóc, diadem và bộ đồ** của vòng 2; giữ y nguyên người này.
- `H/r2-view-back.v1-try2-normalized.png`, `H/r2-view-left.v1-try1-normalized.png`, `H/r2-turnaround.v1-try2-normalized.png`: vòng 2, sửa lỗi dưới.
- `games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png`: chỉ để lấy **độ rủ của lớp áo ngoài chàm và vai mềm** (khí chất hoàng tộc), không lấy váy dài.

## Sửa bắt buộc
1. **Thêm lớp áo khoác ngoài chàm lạnh** mở trước, không tay hoặc tay ngắn tới khuỷu, dài tới giữa đùi, **xẻ hai bên hông và xẻ sau**, mép có bề dày, rủ mềm; tấm cổ Nhật Bình (lõi chàm, rìa ngà rộng) nằm trên lớp này; vai mềm hơn, không hộp. Áo trong trắng ngà và quần suông giữ. Vẫn không váy dài, không ống tay rộng, không dải lụa.
2. **Tấm lưng:** quyết là tấm vải thêu có lót cứng, dày 1–2 cm, gắn ở hai vai và thắt lưng (thấy dây hoặc khuy gắn), ấn phượng trên đó; ở góc bên phải thấy cạnh có bề dày.
3. **Ngọc bội:** treo ở hông trái, móc vào thắt lưng, dài tới giữa đùi; ở góc sau thấy một phần bên trái, góc phải khuất; cùng dài ở mọi góc.
4. **Ủng góc sau:** gót, đế sau, đường ráp sau; không hoạ tiết mũi giày; chân sau đúng hướng; cùng ủng ở mọi góc.
5. **Góc camera chơi** (`r3-view-play`): camera nhìn xuống **55°**, từ sau chếch 30°, thấy mặt trên đầu, vai, lưng, thân chân bị rút ngắn; nhân vật đứng dáng sẵn sàng, đầu cùng hướng thân, hai tay thấy; không phải ba phần tư ngang.
6. Giữ: A-pose cho 4 góc, kiếm thấp ở xương cùng chuôi phải nghiêng 10° có đai treo, hai đuôi lưng, viền mây hạc, nền `#00FF00`, lề ≥ 8 %, đèn trên phải 45°, không bóng, không hào quang, không chữ. Màu 60 ngà, 30 chàm lạnh, 10 vàng cũ.

## Bộ ảnh (cùng khổ 3:4 cho ảnh đơn, cùng chiều cao người chênh ≤ 3 %)
`H/r3-turnaround.v1-try1.png` (16:9, trước, trái, sau, phải), `H/r3-view-front.v1-try1.png`, `H/r3-view-back.v1-try1.png`, `H/r3-view-left.v1-try1.png`, `H/r3-view-play.v1-try1.png`. Mỗi prompt liệt kê 12 chi tiết nhận dạng (thêm: áo khoác ngoài chàm xẻ, tấm lưng có lót) và "same face, hair and diadem as the reference front view".

## Kiểm
Nền, lề, chênh chiều cao; bảng nhất quán 12 chi tiết × 4 góc; **kiểm ủng sau** (ghi có/không gót và đế); tấm so mặt với `r2-view-front` (phải giống); ô 66 px cho sau và góc chơi. Tự chấm theo mặt yếu nhất; dưới 8 vẽ lại ảnh yếu nhất, tối đa 3 lần.

## Xong khi
5 ảnh + prompt + `H/r3-347-sheet.jpg` + báo cáo có bảng.
