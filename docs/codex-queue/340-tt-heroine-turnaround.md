# Phiếu 340 · Tu Tiên · Ảnh 2D: bộ bốn góc nhân vật chính (hướng C mượn cổ A), ảnh nguồn cho Tripo

Anh (12/11 00:3x): "thử triển khai theo hướng này". Brief: `docs/games/tu-tien/characters/HEROINE_TURNAROUND_BRIEF.md` (đọc hết, nhất là phần Thiết kế và Bộ ảnh). Canon D63. Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần gọi `image_gen`** (5 ảnh × 1, cộng tối đa 3 lần vẽ lại). Mở tối đa 14 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/340-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`H = games/immortality-cultivation/art-src/heroine`. **Được ghi:** chỉ thêm file mới vào `H` và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu; sửa mã.

## Tham chiếu (mở bằng `view_image`)
- `games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png`: chân dung A đã duyệt, **cùng người** (mặt, tóc, diadem, màu). Model 3D dùng mặt sạch kiểu donghua cao cấp, không tả thực ảnh, nhưng vẫn là người này: diadem, chân tóc, lông mày giữ y nguyên.
- `H/dir-c-front.v1-try1.png`, `H/dir-c-back.v1-try1.png`: hướng C đã chọn (thân, dáng, quần, giày, thắt lưng, kiếm).
- `H/dir-a-back.v1-try1.png`: chỉ lấy **tấm cổ Nhật Bình vắt vai** để mượn.

## Thiết kế (theo brief; khác C cũ ở 5 chỗ)
1. Tấm cổ Nhật Bình chữ nhật vắt qua hai vai: **lõi chàm, rìa ngoài trắng ngà viền vàng cũ bản rộng** (≥ 4 % chiều cao người), vai vuông.
2. Búi tóc cao hơn khoảng 30 % so với chân dung, một khối đặc; diadem ngọc trắng và vàng cũ dày bản, không thành mão.
3. Viền gấu áo và tấm cổ dùng **mây và hạc** như chân dung A; ấn tròn **phượng** thêu vàng cũ giữa lưng (đường kính 25 % chiều cao người); vạt hò chéo và đường tà ngũ thân rõ.
4. Kiếm Thanh Phong trong vỏ sơn mài chàm đeo ngang **thấp ở xương cùng, ngay dưới ấn phượng**, chuôi bên phải nghiêng 10°.
5. Không dải lụa, không áo choàng, không váy, không hào quang, không ánh sáng phép, không vật bay.
Còn lại giữ C: áo lụa trắng ngà cổ cao dài tới giữa đùi, ống tay bó từ khuỷu, thắt lưng gấm chàm rộng có tấm hộ eo, ngọc bội trắng đục bên trái, hai đuôi lưng ngắn tới gối, quần ống rộng chàm thẫm bó cổ chân, giày cao cổ chàm viền vàng cũ. Màu 60 trắng ngà, 30 chàm, 10 vàng cũ. Sáng ở đầu, vai, thân trên; tối ở quần.

## Bộ ảnh (cùng khổ, cùng chiều cao người, nền `#00FF00`, lề ≥ 8 %, đèn mềm một nguồn trên phải 45°, không bóng đổ, chân phẳng)
| Tên tệp | Ảnh | Khổ |
|---|---|---|
| `H/turnaround.v1-try1.png` | Tờ 4 cột trước, trái, sau, phải; **A-pose** (tay hở thân 30°, lòng bàn tay úp), cùng chiều cao từng cột, cùng đường chân | 16:9 ngang |
| `H/view-front.v1-try1.png` | Trước, A-pose | 3:4 |
| `H/view-back.v1-try1.png` | Sau, A-pose: gáy, búi tóc, tấm cổ, ấn phượng, kiếm thấp, đuôi lưng; **không thấy mặt** | 3:4 |
| `H/view-left.v1-try1.png` | Trái (vai trái về phía người xem), A-pose | 3:4 |
| `H/view-play.v1-try1.png` | Ba phần tư từ trên 30°, nhìn từ sau chếch, dáng sẵn sàng, một tay nắm chuôi; chỉ để kiểm camera chơi | 3:4 |

Mỗi prompt sau tờ turnaround liệt kê đủ 11 chi tiết nhận dạng: diadem, búi tóc cao, tấm cổ lõi chàm rìa ngà, ấn phượng lưng, thắt lưng và tấm hộ eo, ngọc bội trái, hai đuôi lưng, ống tay bó, quần ống rộng, giày cao cổ, kiếm thấp ngang xương cùng. Thêm: "clean high-end donghua face, same person as the reference portrait, smooth skin, no photoreal pores", "large clean colour masses, few thin folds, mesh-ready", "no text, no logo, no watermark".

## Kiểm
- `magick`: nền 4 góc gần `#00FF00`; lề ≥ 8 % mỗi cạnh; chiều cao người của 4 ảnh góc chênh ≤ 3 %; ghi số.
- Bảng nhất quán: 11 chi tiết × 4 góc, có/không. Lưng thật là lưng.
- Ô kiểm 66 px: thu `view-back` và `view-play` xuống cao 66 px, phóng 4× cạnh ảnh gốc trong tấm ghép; tự ghi 3 khối còn đọc được không.
- Tự chấm 0–10 theo mặt yếu nhất: cùng người với chân dung A; nhất quán 4 góc; gom khối dựng mesh; sang, cuốn hút; đọc ở 66 px. Dưới 8: vẽ lại một lần ảnh yếu nhất.

## Xong khi
- 5 ảnh + `.prompt.txt` + tấm ghép `H/turnaround-340-sheet.jpg` (turnaround trên, 4 ảnh dưới, ô 66 px) + báo cáo có bảng nhất quán, lề, chênh chiều cao, điểm, vẽ lại.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
