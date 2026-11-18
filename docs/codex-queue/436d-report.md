# Phiếu 436d — Dừng tại cổng tỷ lệ thân nền

Ngày thực hiện: 17/11/2026. Đã dùng **1/8 lượt `image_gen`**. **Thân nền chưa đạt; dừng sau bước 1** theo yêu cầu của phiếu. Không chuyển sang vẽ trang phục trên thân này.

## Đã tạo

- `games/immortality-cultivation/art-src/heroine/fashion/base-body.v2-try1.png` — ảnh PNG 1536 × 1024, ba góc trước, nghiêng và sau; dáng chữ A, trang phục ôm trung tính, nền xám, có thước bên phải.
- `games/immortality-cultivation/art-src/heroine/fashion/base-body.v2-try1.prompt.txt` — nguyên văn prompt đã gửi công cụ, gồm đường dẫn tham chiếu và các mốc tỷ lệ yêu cầu.
- `/private/tmp/typing-game-436d/base-heads-measure.png` — phần đầu góc trước và nghiêng phóng to để kiểm tra; chỉ là ảnh cắt phục vụ đo, không phải ảnh nguồn mới.

Tham chiếu duy nhất gửi công cụ: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`, chỉ giữ khuôn mặt. Không gửi ảnh của trò chơi khác hoặc thân nền cũ.

## Số đo và kết luận

Đo trên ảnh gốc 1536 × 1024; tọa độ y tính từ mép trên. Một đầu là đỉnh sọ đến cằm, bỏ búi tóc; chiều cao đến lòng bàn chân, bỏ đế giày. Đỉnh sọ và lòng bàn chân bị tóc/giày che nên đây là **ước lượng theo ảnh**, không phải số đo giải phẫu chính xác. Sai số mốc khoảng 4–6 px; không lấy độ dài vạch kẻ thay cho chiều dài đầu thật.

| Ảnh / góc dùng làm cổng kiểm tra | Đỉnh sọ y | Cằm y | Lòng bàn chân y | Đầu | Chiều cao | Chiều cao / đầu | Đầu / chiều cao |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `base-body.v2-try1.png`, chính diện | ≈60 | ≈173 | ≈954 | ≈113 px | ≈894 px | **≈7,9 đầu** | **≈12,6%** |

Yêu cầu là 8,5 đầu, tương đương khoảng 11,8%. Với chiều cao khoảng 894 px, đầu cần khoảng 105 px thay vì khoảng 113 px hiện tại. Chênh lệch đủ để không cho qua cổng; số đo là xấp xỉ, không gán độ chính xác giả tới phần trăm nhỏ.

Đáy chậu chính diện ở khoảng y=488: cách đỉnh sọ khoảng 428 px, tức 47,9% chiều cao; chân trong khoảng 466 px, tức 52,1%. Điều kiện chiều dài chân trong đạt theo ước lượng, nhưng không bù cho tỷ lệ đầu chưa đạt. Khớp hông bị trang phục che, không có đủ bằng chứng để xác nhận chính xác điều kiện 52%. Vai khoảng y=210 và eo khoảng y=360, tương ứng khoảng 1,3 và 2,7 đầu từ đỉnh sọ; chưa khớp tốt mốc 1,5 và 3 đầu.

Thước bên phải có các vạch tại y ≈ 64; 162; 261; 359; 457,5; 556; 655; 753; 852; 911; 962 px (đọc độ sáng pixel bằng ImageMagick). Tám khoảng đầu dài khoảng 98–99 px, sau đó có hai khoảng 59 và 51 px: không phải tám khoảng đầu cộng nửa khoảng cuối. Thước không khớp đầu thật và cũng không chia đúng 8,5 khoảng bằng nhau. Vì vậy không thể dùng riêng thước để tuyên bố đạt. Góc nghiêng có kích thước đầu khác góc trước; góc sau không thấy cằm nên không báo số đầu đo trực tiếp cho góc sau. Chỉ góc trước đã đủ xác định thân nền không đạt.

## Bỏ qua theo điều kiện dừng

- Chưa tạo `crimson-bride`, `moon-blade`, `jade-noble`, `shadow-spider`.
- Chưa ghép `heroine-lookbook-436d.jpg` vì chưa có thân nền đạt và bốn bộ trang phục; không ghép tờ thiếu rồi gọi là hoàn tất.
- Không có số đo trang phục vì các ảnh đó chưa được tạo.

Owner cần xem thân nền thử 1 và lỗi đầu/thước nêu trên. Đây là bản thử chưa đạt, không phải nguồn đã được duyệt để dựng 3D hoặc đưa vào game. Không chấm điểm mỹ thuật thay hai giám khảo độc lập.

Không sửa code, không chạy build/test, không tạo video, không ghi đè hoặc xóa ảnh có sẵn, không đổi nhánh và không thực hiện thao tác ghi Git. Không gặp giới hạn công cụ; việc dừng là do cổng tỷ lệ trong phiếu.
