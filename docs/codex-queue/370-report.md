# Phiếu 370 · Sói Núi Đá v6

**image_gen** 5/10 lượt; xem ảnh 11/12 lượt. Đọc nghiên cứu và tiêu chí 368. Chỉ dùng ảnh dự án; giữ nguyên v3–v5.

Trong `games/immortality-cultivation/art-src/kings/`:
- `thiet-boi-lang-vuong.v6-q-final.png`, `thiet-boi-lang-vuong.v6-front-final.png`;
- hai bản `v6-q-raw.png`, `v6-front-raw.png`;
- hai bản `v6-{q,front}-final.prompt.txt`, chứa prompt nguyên văn, tham chiếu và hậu kỳ;
- `boss-370-sheet.jpg`: v3 | v6 hai góc, ô 66 px, bản phóng 2× và raw | final.

Đã sửa tỉ lệ chính diện và tăng điểm mắt bằng image_gen.

Kiểm script: cả hai 1024², rộng 768 px (**75%**); cao q **687**, front **670** px, lệch **2,47%**. Lề trái/phải **12,5%**; trên/dưới q **16,41/16,50%**, front **17,29/17,29%**. Mỗi ảnh đúng một khối 8-liên thông, nền ngoài đúng `#00FF00`, không bóng rời. Final là PNG nền khóa RGB như v3, **không phải alpha trong suốt**; matte trung gian nhị phân, alpha hiển thị toàn đục.

| Tiêu chí | Tự chấm |
|---|---:|
| a · Hung ác ở 66 px | 8,5 |
| b · Đồng bộ bộ ảnh | 8,8 |
| c · Nhất quán hai góc | 8,5 |
| d · Phù hợp dựng Tripo | 9,0 |
| e · Chất tiên hiệp, độc đáo | 9,0 |
| f · Sức hút thương mại | 8,5 |

Điểm cuối **8,5**. Dãy núi đọc rõ ở q; ba chóp và mắt ngà còn đọc được nhưng nhỏ. Front che chồng dãy đá, vai trông rộng hơn q; cần anh xem kỹ. Không còn vòng cổ, đuôi cuộn hay dáng chó cảnh.

Chỉ tự chấm ảnh nguồn góc 32°; chưa kiểm camera chơi 55°, chưa duyệt mù. Không làm model, tích hợp, build/test hay Git vì ngoài phạm vi.
