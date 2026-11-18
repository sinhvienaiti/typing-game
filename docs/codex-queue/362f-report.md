# Phiếu 362f · Bốn loài thường v6

Đã sửa trực tiếp tám ảnh gốc bằng `image_gen`: 15/20 lượt tạo, 10/24 lượt `view_image`. Giữ chất ảnh sắc, lông và dáng cũ; không dùng bản v5 hay ảnh bên thứ ba.

`A = games/immortality-cultivation/art-src`.

- Tám ảnh: `A/beasts/{thiet-giap-tru,nham-vien,thach-thu,hoa-nha}.v6-{q,front}-final.png`.
- Có đủ tám bản `-raw.png` được chọn và tám `-final.prompt.txt`: nguyên văn prompt, ảnh gốc, phép chuẩn hoá, mặt nạ đo và số kiểm.
- [Tấm ghép gốc–mới, hai góc, boss v7 cùng bộ ở ô 66 px](../../games/immortality-cultivation/art-src/beasts/bestiary-362f-sheet.jpg).

Kiểm bằng Python/ImageMagick, không căn chỉnh lại ảnh khi so:

| Loài | Cao q/front (px) | Lệch | MAE ngoài vùng sửa q/front |
|---|---:|---:|---:|
| Thiết Giáp Trư | 586/570 | 2,73% | 11,01/12,52 |
| Nham Viên | 713/713 | 0% | 13,66/10,76 |
| Thạch Thử | 558/551 | 1,25% | 13,23/12,46 |
| Hỏa Nha | 678/679 | 0,15% | 17,04/13,77 |

MAE RGB trên thang 255, chỉ tính hợp vùng nhân vật ngoài các hộp sửa; tính cả nền là 1,18–2,53. Sai khác nhỏ nhưng không bằng không. Tất cả: 1024², lề ≥10,16%, một khối liên thông, alpha đặc sạch; viền 82 px đúng `#00FF00`.

Tự chấm cả bộ: (a) hung ác 66 px **8,0**; (b) đồng bộ **8,7**; (c) khớp hai góc **8,2**; (d) nguồn Tripo **8,6**; (e) tiên hiệp/độc đáo **8,3**; (f) thương mại **8,1**. Điểm cuối **8,0 — CHƯA ĐẠT 8,5**. Cần xem vân vai vượn, độ vồng vảy chuột giữa hai góc; quạ còn tối khi thu nhỏ.

Không bỏ ảnh nào. Không sửa bản cũ, boss, mã hoặc tài liệu game; không build/test. Chưa dựng Tripo, chấm mù hay kiểm trong game vì ngoài phiếu.
