# Phiếu 339 · Tu Tiên · Ảnh 2D: 3 hướng thiết kế nhân vật chính (Kiếm tu nữ), mỗi hướng một cặp trước và sau

Anh (11/11 23:5x): nhân vật chính là việc ảnh đầu tiên. Nghiên cứu và brief: `docs/games/tu-tien/characters/HEROINE_RESEARCH_2026-11-11.md` (đọc §1, §4, §5, §6 trước khi vẽ). Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 9 lần gọi `image_gen`** (3 hướng × 2 góc, cộng tối đa 3 lần vẽ lại). Mở tối đa 12 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/339-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`H = games/immortality-cultivation/art-src/heroine` (tạo mới). **Được ghi:** chỉ thêm file mới vào `H` và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu; sửa mã.

## Tham chiếu (mở bằng `view_image` trước mỗi ảnh)
- `games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png`: **chân dung bản sắc A đã duyệt**. Giữ đúng người này: mặt, tóc búi đen cao, diadem ngọc trắng và vàng cũ, bảng màu trắng ngà, chàm, vàng cũ, kiếm Thanh Phong vỏ sơn mài chàm. Ba hướng là ba cách mặc và đứng của **cùng một người**.
- `games/immortality-cultivation/art-src/cultivators/kiem-tu.png`: bản 25/10 **đã trượt** (không cầm kiếm, vải mảnh nhiều lớp, đọc như tiểu thư). Chỉ xem để tránh.

## Ba hướng (mỗi hướng 2 ảnh: `H/dir-<a|b|c>-front.v1-try1.png` ba phần tư trước, `H/dir-<a|b|c>-back.v1-try1.png` ba phần tư sau)
| Hướng | Mặc và đứng (dịch đủ sang tiếng Anh) |
|---|---|
| A · Royal Nhật Bình | Áo ngũ thân trắng ngà dài tới bắp chân, **tấm cổ chữ nhật lớn kiểu Nhật Bình màu chàm viền vàng cũ vắt qua hai vai** (thấy rõ từ sau), thêu phượng và sóng nước, thắt lưng gấm chàm có ngọc bội trắng; đứng thẳng, kiếm Thanh Phong cầm thẳng đứng trước ngực bằng cả hai tay |
| B · Dunhuang Sword Immortal | Áo ngũ thân trắng ngà, cổ cao kín, **hai dải lụa chàm rất dài** vắt qua hai cánh tay và bay thành chữ S sau lưng, hoa văn lá đề và sen thêu vàng cũ; đứng nghiêng nhẹ, một tay mở 30°, kiếm Thanh Phong tuốt trần bay lơ lửng cạnh người (lưỡi thép xanh nhạt, không phát sáng) |
| C · Lý Silk Warrior | Áo ngắn tới đùi trên quần ống rộng, **ống tay bó từ khuỷu**, thắt lưng gấm chàm rộng có tấm hộ eo thêu phượng, dải lưng ngắn, giày cao cổ; **ấn phượng tròn thêu chàm giữa lưng**; dáng sẵn sàng, chân mở, một tay nắm chuôi kiếm đeo ngang lưng, tay kia mở |

Chung cho cả 6 ảnh (đặt sau câu tả hình, dịch đủ): cùng một người với chân dung tham chiếu; **cả hai tay đều thấy**; không sừng, không che mặt; lớp vải gom thành khối lớn, ít nếp mảnh (để dựng mesh); không hào quang, không ánh sáng phép, không vật bay ngoài kiếm (hướng B); không chữ, không logo; **nền phẳng xanh lục thuần `#00FF00`**, không bóng đổ xuống nền; **cả người lọt khung, lề trống ≥ 8 % mỗi cạnh**, chân phẳng; ánh sáng mềm **một đèn trên phải 45°**; phong cách painterly-realistic như game thương mại tiên hiệp cao cấp (sắc nét, chất liệu thật, không anime phẳng, không tả thực ảnh); cuốn hút, sang, thời trang, hiện đại, chi tiết nhiều lớp. Khổ **3:4 dọc**, cùng khổ và cùng chiều cao người cho cặp trước/sau. Ảnh sau: thấy gáy, búi tóc, lưng, dải lụa, vỏ kiếm; **không thấy mặt**.

## Cách làm
1. `view_image` hai ảnh tham chiếu. Vẽ trước cặp A, rồi B, rồi C; cặp sau của mỗi hướng tả lại đúng chi tiết của cặp trước (liệt kê 8 chi tiết nhận dạng trong prompt: diadem, kiểu cổ, thắt lưng, ngọc bội, dải lụa, kiếm, giày, hoa văn).
2. `cp -n` vào `H/`, ghi `.prompt.txt` cùng tên: công cụ, tham chiếu, prompt nguyên văn, khổ thật.
3. Kiểm bằng `magick`: nền 4 góc gần `#00FF00`; lề ≥ 8 % mỗi cạnh (đo hộp bao các điểm không phải xanh lục); chiều cao người của cặp trước/sau chênh ≤ 5 %. Ghi số.
4. **Tự chấm** 0–10 theo mặt yếu nhất: cùng người với chân dung A; đúng hướng đã tả; hai tay thấy; lưng là lưng thật; gom khối dựng mesh được; sang, cuốn hút, ngang game thương mại. Dưới 8: vẽ lại một lần (`-try2`).
5. Tấm ghép `H/directions-339-sheet.jpg`: 3 cột A, B, C; mỗi cột trước trên, sau dưới; có nhãn.

## Xong khi
- 6 ảnh + prompt + tấm ghép + báo cáo có bảng (ảnh, lề, chênh chiều cao, điểm từng tiêu chí, nhận xét, vẽ lại không).

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
