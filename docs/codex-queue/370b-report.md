# Phiếu 370b · Sói Núi Đá v7

**image_gen: 3/10 lượt; view_image: 5/12 lượt.**

## Bàn giao

Trong `games/immortality-cultivation/art-src/kings/`:
- `thiet-boi-lang-vuong.v7-{q,front}-final.png`: hai ảnh 1024 × 1024.
- `thiet-boi-lang-vuong.v7-{q,front}-raw.png`: hai bản sinh nguyên trạng.
- `thiet-boi-lang-vuong.v7-{q,front}-final.prompt.txt`: prompt, tham chiếu, lịch sử, hậu kỳ.
- `boss-370b-sheet.jpg`: v6 | v7 hai góc, silhouette cao đúng 66 px và gốc | hậu kỳ.

## Quan sát và kiểm

Ba phần tư: sáu tảng đá tù cao, khe tối, vương miện lớn, mõm dài, hàm gầm và nanh lộ. Chính diện: tai nhọn, đầu thuôn, sống mũi nổi, một mắt bịt vảy, một mắt trắng ngà; chân mở rộng.

Script xác nhận: ngang vật 800 px (**78,13%**); cao q/front **767/790 px**, lệch **2,91%**. Lề q L/R/T/B **10,94/10,94/12,50/12,60%**; front **10,94/10,94/11,43/11,43%**. Mỗi ảnh một khối liền **100%**, không mảnh rời; kiểm bóng PASS, nền góc **#00FF00**, alpha toàn ảnh **255** theo chuẩn nền đục. Hậu kỳ chỉ tách nền, khử tràn xanh ở viền, thu đồng tỉ lệ và căn giữa.

## Tự chấm

| Tiêu chí | Điểm |
|---|---:|
| a · Hung ác ở 66 px | 8,6 |
| b · Đồng bộ bộ ảnh | 8,8 |
| c · Nhất quán hai góc | 8,5 |
| d · Nguồn Tripo | 9,0 |
| e · Tiên hiệp, độc đáo | 8,8 |
| f · Sức hút, thương mại | 8,5 |

**Điểm cuối: 8,5 — đạt tự chấm.** Chính diện đọc ra sói: **có**. 66 px thấy núi và vương miện: **có**, các tảng phía sau chồng nhau ở chính diện.

Bỏ bản nháp chính diện hẹp; giữ mọi bản cũ. Không build/test, Git hoặc tích hợp. Chủ cần xem mõm chính diện và ô 66 px; tự chấm chưa thay nghiệm thu mù.

