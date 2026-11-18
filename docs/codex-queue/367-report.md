# Phiếu 367 · Cột lôi bạch kim

Đã dùng **10/10 image_gen**, **8/12 view_image**. Chỉ thêm ảnh, prompt, tấm ghép và báo cáo; không sửa mã, không chạy build/test, không ghi Git.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

## Đã tạo
- `S/thunder-column-{a,b,c}.v1-try1.png`: bện chặt / bện thoáng / hai bó quấn nhau; 1024×1536.
- Core: `S/thunder-column-a-core.v1-try{1,2,3}.png`, `S/thunder-column-{b,c}-core.v1-try{1,2}.png`.
- Mỗi ảnh có `.prompt.txt` ghi nguyên prompt và đường dẫn tham chiếu của repo.
- `S/thunder-column-367-sheet.jpg`: ba nguồn, kèm bản cao 120 px và core so cạnh nhau.

## Kiểm tra
Script đọc RGB bằng ImageMagick; biên nội dung lấy maxRGB > 8. Lề nhỏ nhất A/B/C: **7,10 / 6,18 / 6,18 %**. Trắng thuần (minRGB > 245): **0,062 / 0,222 / 0,201 %**; mọi core ≤ **1,274 %**, dưới 6 %.

Hàng chân A/B/C: **1304 / 1287 / 1295 px**; lệch giữa ba ảnh **17 px = 1,11 %** chiều cao. Quầng chân trong dải ±10 px quanh hàng chính rộng theo trục dọc **15/12/12 px**.

Tự chấm nguồn theo mặt yếu nhất: **A 8,1; B 8,0; C 8,2**. Đọc thành cột sợi, khe tối rõ, khác kiểu bện, hợp bạch kim; B thoáng nhất. Đây là tự chấm nguồn, chưa phải nghiệm thu hiệu ứng trong game.

## Chưa đạt
Nền ngoài lề còn nhiễu RGB=1; chưa đen tuyệt đối.

**Core chưa chồng khít.** Bản gần nhất: A thử 2, B/C thử 1. Mặt nạ minRGB > 160, vùng y=300–1229: khớp đúng pixel **52,53/82,56/75,79 %**; trong bán kính 2 px **84,51/96,12/95,00 %**. Không gắn PASS.

Dừng tạo thêm vì hết 10 lượt được phép. Giữ mọi thử; cần hướng xử lý core bảo toàn pixel trước khi dùng nhấp nháy. Anh xem tấm ghép, chọn kiểu cột; chưa tích hợp runtime.
