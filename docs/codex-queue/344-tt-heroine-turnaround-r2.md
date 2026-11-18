# Phiếu 344 · Tu Tiên · Ảnh 2D: bộ bốn góc nhân vật chính, vòng 2 theo hai giám khảo mù

Vòng 1 (phiếu 340) bị hai giám khảo mù chấm **CHƯA** (thấp nhất 7,2 và 7,4; báo cáo `docs/codex-queue/343-report.md`, `343b-report.md`, không cần đọc hết). Hai giám khảo cùng nêu: (1) **mặt không còn là người trong chân dung**: mắt to, mặt ngắn, như búp bê, thiếu độ trưởng thành; (2) **tóc và diadem** thành búi dựng đứng và vòng hoa chung, mất cấu trúc vương miện thanh, cao, chạm rỗng của chân dung; (3) **hình bóng vai hộp + quần phồng đọc như đồng phục quân**, thiếu thanh thoát và lớp lang của nữ chính hoàng tộc; (4) góc trái tay chồng lên thân, hai chân chồng nhau; (5) chuôi, vỏ kiếm và giá treo chưa rõ cấu tạo; vật liệu: chàm phải lạnh hơn, ngà bớt hồng, tách rõ tóc bóng, vải mềm, kim loại, ngọc. Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần gọi `image_gen`** (5 ảnh, tối đa 3 vẽ lại). `view_image` tối đa 14. Báo cáo: `docs/codex-queue/344-report.md`.

## Đường dẫn
`H = games/immortality-cultivation/art-src/heroine`. Chỉ thêm file mới `H/r2-*` và báo cáo. Cấm git ghi, sửa hay xóa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
- `games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png`: **chuẩn mặt, tóc, diadem**. Mở trước mỗi ảnh. Mặt phải giữ đúng tỷ lệ mắt, mũi, miệng, chiều dài mặt, đường hàm và vẻ trưởng thành 24 tuổi của ảnh này; chỉ làm da mịn kiểu donghua, không đổi khuôn mặt. Tóc búi gọn ôm đầu như ảnh này (không dựng cao); diadem ngọc trắng và vàng cũ **thanh, cao, chạm rỗng** đúng hình trong ảnh, có hai tua dài hai bên.
- `H/view-front.v1-try1.png`, `H/view-back.v1-try2.png`, `H/view-left.v1-try1.png`, `H/turnaround.v1-try2.png`: vòng 1, giữ bộ đồ và cách đặt phụ kiện, **sửa các lỗi dưới**.

## Sửa bắt buộc so với vòng 1
1. **Mặt, tóc, diadem khớp chân dung** (xem trên); dùng cùng một khuôn mặt cho mọi góc.
2. **Hình bóng thanh thoát hơn, bớt quân phục:** vai tấm cổ Nhật Bình vẫn vuông nhưng **mỏng và sát vai hơn** (không hộp dày); quần ống rộng **thu bớt độ phồng** thành ống suông rơi mềm, bó ở cổ chân; áo dài tới giữa đùi với **vạt hò chéo rõ và tà xẻ hai bên hông** để thấy lớp lang; thêm một lớp áo trong trắng lộ ở cổ và cổ tay. Vẫn không váy dài, không ống tay rộng, không dải lụa.
3. **Vật liệu theo chân dung:** chàm lạnh (xanh chàm ngả lam), ngà bớt hồng, vàng cũ nhạt; tóc có độ bóng, lụa mềm, kim loại và ngọc rõ chất.
4. **Góc trái:** tay mở 30° rõ khoảng hở với hông, hai chân hơi tách để thấy cả hai; kiếm đeo thấp ngang xương cùng phải thấy chuôi nhô ra phía sau.
5. **Kiếm và giá treo nhất quán ở 4 góc:** vỏ sơn mài chàm, chuôi bên phải nghiêng 10°, đai treo vòng qua thắt lưng, nhìn thấy điểm gắn; ấn phượng lưng cùng đường kính (25 % chiều cao người) và cùng độ nhô ở mọi góc.
6. Giữ: lõi chàm rìa ngà ở tấm cổ (rìa ≥ 4 % chiều cao người), ngọc bội trái, hai đuôi lưng ngắn, giày cao cổ, viền mây hạc, A-pose, nền `#00FF00`, lề ≥ 8 %, đèn trên phải 45°, không bóng, không hào quang, không chữ.

## Bộ ảnh (cùng khổ, cùng chiều cao người, chênh ≤ 3 %)
`H/r2-turnaround.v1-try1.png` (16:9, 4 cột trước, trái, sau, phải), `H/r2-view-front.v1-try1.png`, `H/r2-view-back.v1-try1.png`, `H/r2-view-left.v1-try1.png`, `H/r2-view-play.v1-try1.png` (ba phần tư từ trên 30°, nhìn từ sau chếch, dáng sẵn sàng; **hai tay đều thấy**). Mỗi prompt liệt kê 11 chi tiết nhận dạng và câu "same face, same hair and diadem as the reference portrait".

## Kiểm
Nền, lề, chênh chiều cao; bảng nhất quán 11 chi tiết × 4 góc; **tấm so mặt**: cắt mặt chân dung và mặt `r2-view-front` cạnh nhau cùng cỡ, ghi nhận giống hay khác ở mắt, mũi, miệng, hàm; ô 66 px cho sau và góc chơi. Tự chấm theo mặt yếu nhất; dưới 8 vẽ lại ảnh yếu nhất một lần.

## Xong khi
5 ảnh + prompt + `H/r2-344-sheet.jpg` (turnaround, 4 ảnh, tấm so mặt, ô 66 px) + báo cáo có bảng.

## Hết hạn mức
Giữ file, báo cáo phần đã xong, dòng cuối `CODEX-WAIT-UNTIL: HH:MM`.
