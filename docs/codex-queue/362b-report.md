# Phiếu 362b — mẫu boss v3, chờ chủ dự án duyệt

Đã tạo bằng image_gen tích hợp **4 lượt/20**, xem ảnh bằng view_image **10 lượt/24**. Chỉ dùng ảnh nội bộ được phiếu chỉ định.

**A = `games/immortality-cultivation/art-src`.**

- Hai ảnh chốt: `A/kings/thiet-boi-lang-vuong.v3-q-final.png` và `A/kings/thiet-boi-lang-vuong.v3-front-final.png`.
- Giữ bốn ảnh thử `A/kings/thiet-boi-lang-vuong.v3-{q,front}-try{1,2}.png`; lượt 2 sửa xích thành hai đầu đứt, bỏ cảm giác vòng cổ.
- Tấm ghép: `A/beasts/bestiary-362b-sheet.jpg`, v2 | v3 cùng chiều cao vật 320 px, thêm ô nguyên canvas 66×66 px.
- Mọi ảnh có `.prompt.txt` cùng tên; ảnh chốt ghi cả nguồn và bước xử lý, tấm ghép ghi công thức ghép.

**Kiểm script:** canvas 1024×1024; bbox Q (93,202)–(930,822), trước (147,202)–(877,822). Lề nhỏ nhất lần lượt **9,08% / 14,36%**. Cả hai cao **620 px**, lệch **0%**. Mỗi ảnh một thành phần 8-liên thông; bỏ hai điểm biên rời ở góc trước. Nền đúng #00FF00, khử ám xanh; kiểm lại không còn pixel vật có G vượt max(R,B). Tấm ghép nền tối không thấy viền xanh. Không bóng đổ hoặc hào quang.

**Tự chấm ảnh nguồn, theo mặt yếu nhất:** đáng sợ ở ô 66 px **8,2**; hoang dại **8,0**; đồ sộ **8,6**; chuẩn bộ **8,7**; khả năng dựng Tripo **8,3**. Điểm thấp nhất **8,0**: lông vẫn khá đều thành khối; cần chủ dự án xem mức hoang dại đã đủ chưa. Đây chưa phải nghiệm thu mù hoặc kiểm chứng model Tripo.

Dừng đúng sau boss. Chưa vẽ Hỏa Nha, Nham Viên, Thạch Thử, Thiết Giáp Trư; chờ duyệt mẫu. Giữ nguyên toàn bộ v2, không sửa mã, chạy build/test hay ghi Git.
