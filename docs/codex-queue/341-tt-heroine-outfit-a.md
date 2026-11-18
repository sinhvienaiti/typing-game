# Phiếu 341 · Tu Tiên · Ảnh 2D: bộ trang phục thứ hai (A, bộ lễ) trên cùng thân chuẩn, để chứng minh đổi đồ

Canon D63 (4): bộ lễ A dựng ngay sau bộ đầu, trên **cùng thân chuẩn, cùng chiều cao, cùng A-pose** với phiếu 340. Phiếu này chỉ vẽ ảnh, không sửa mã. Chạy **sau khi phiếu 340 xong**; đọc `docs/codex-queue/340-report.md` và dùng bộ 340 làm thân chuẩn.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 7 lần gọi `image_gen`** (4 ảnh × 1, cộng tối đa 3 lần vẽ lại). Mở tối đa 14 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/341-report.md`.

## Đường dẫn
`H = games/immortality-cultivation/art-src/heroine`. **Được ghi:** chỉ thêm file mới `H/outfit-a-*` và báo cáo. **Cấm:** git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo; sửa mã.

## Tham chiếu (`view_image`)
- `H/turnaround.v1-try1.png`, `H/view-front.v1-try1.png`, `H/view-back.v1-try1.png`, `H/view-left.v1-try1.png` (phiếu 340): **thân chuẩn**. Giữ y nguyên: mặt, tóc búi cao, diadem, chiều cao, tỉ lệ, A-pose, đường chân, vị trí vai, eo, gối.
- `H/dir-a-front.v1-try2.png`, `H/dir-a-back.v1-try1.png`: thiết kế bộ lễ A.
- `games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png`: chân dung A, bảng màu và mô típ mây hạc.

## Bộ lễ A theo hợp đồng trang phục (D63)
- Áo ngũ thân trắng ngà dài tới bắp chân, **xẻ thành ba tấm** (trước, hai bên) từ hông xuống, hai tấm bên dính theo đùi; tấm sau rời, tới gối.
- Tấm cổ Nhật Bình chữ nhật lớn vắt vai: lõi chàm, rìa trắng ngà viền vàng cũ bản rộng, thêu phượng; vai vuông rộng hơn bộ C.
- Thắt lưng gấm chàm, ngọc bội trắng bên trái, hai đuôi lưng dài tới gối (đúng 2 xương lò xo).
- Ống tay bó từ khuỷu (giữ luật, không ống rộng); gấu áo viền mây hạc dày.
- Lớp sau lưng: **ấn phượng lớn** như C nhưng đặt trên tấm sau rời; kiếm Thanh Phong đeo thấp ngang xương cùng, chuôi nghiêng 10°, nằm trong vùng ổ vũ khí, không đâm xuyên tấm sau.
- Quần chàm bó cổ chân, giày cao cổ. Màu 60 ngà, 30 chàm, 10 vàng cũ; rìa vai và đầu sáng.
- Khác hẳn C ở lưng và vai: tấm sau rời dài và vai rộng (C: áo ngắn, lưng trống chỉ ấn).

## Bộ ảnh (nền `#00FF00`, lề ≥ 8 %, đèn trên phải 45°, không bóng, cùng khổ và **cùng chiều cao người với phiếu 340, chênh ≤ 3 %**)
`H/outfit-a-turnaround.v1-try1.png` (16:9, 4 cột trước, trái, sau, phải), `H/outfit-a-front.v1-try1.png`, `H/outfit-a-back.v1-try1.png`, `H/outfit-a-left.v1-try1.png` (3:4). Mỗi prompt liệt kê 10 chi tiết nhận dạng của bộ A và câu "same body, face, hair, diadem, height and A-pose as the reference turnaround".

## Kiểm
- `magick`: nền, lề, chiều cao người so với 340 (chênh ≤ 3 %); mốc vai, eo, gối so với 340 (chênh ≤ 3 % chiều cao).
- Bảng nhất quán 10 chi tiết × 4 góc; sau thật là sau.
- Ô 66 px từ góc sau: phân biệt được với bộ C ở lưng và vai (ghi có/không).
- Tự chấm theo mặt yếu nhất: cùng thân với 340; đúng hợp đồng (xẻ tấm, tay bó, không kéo lê); khác C ở lưng vai; sang, cuốn hút. Dưới 8: vẽ lại một lần ảnh yếu nhất.

## Xong khi
4 ảnh + prompt + `H/outfit-a-341-sheet.jpg` (so cạnh bộ C: trước và sau của cả hai, cùng tỉ lệ) + báo cáo có bảng.

## Hết hạn mức
Giữ file, báo cáo phần đã xong, dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
