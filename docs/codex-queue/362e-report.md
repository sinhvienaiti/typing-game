# Phiếu 362e · Bộ quái v5

Đủ 10 ảnh: `image_gen` **26/26 lượt**, `view_image` **24/30 lượt**.

`A = games/immortality-cultivation/art-src`. Bàn giao:
- `A/kings/thiet-boi-lang-vuong.v5-{q,front}-{raw,final}.png`.
- `A/beasts/{hoa-nha,nham-vien,thach-thu,thiet-giap-tru}.v5-{q,front}-{raw,final}.png`.
- Mười `-final.prompt.txt`: prompt nguyên văn, tham chiếu và hậu xử lý.
- `A/beasts/bestiary-362e-sheet.jpg`: v4 | v5 và mười ô 66 px bằng magick; ghi rõ ba loài v4 giữ v3.

Biến dị riêng từng loài; sói đầu cao, ngực mở, vương miện đá liền, vòng cổ ấn ngọc; tăng đầu/mắt/miệng, gom cánh, dày ngón. Đã vẽ lại nhóm khó đọc; loại lượt vượn thừa chân.

Python + magick, fuzz 18%, liên thông tám hướng: mỗi ảnh **một khối**; lề **≥8,008%**, ngang **70,215–79,492%**, lệch cao **≤0,12%**; alpha **255**, nền `#00FF00`. Dọn bốn pixel rời, ghi trong prompt.

Tự chấm ảnh final; a: hung ác ở 66 px; b: cùng bộ; c: nhất quán hai góc; d: nguồn Tripo; e: tiên hiệp/độc đáo; f: sức hút/thương mại.

| Loài | a | b | c | d | e | f | min |
|---|---:|---:|---:|---:|---:|---:|---:|
| Lang Vương | 8,6 | 8,7 | 8,5 | 8,6 | 8,7 | 8,6 | 8,5 |
| Nham Viên | 8,7 | 8,7 | 8,5 | 8,6 | 8,6 | 8,6 | 8,5 |
| Giáp Trư | 8,6 | 8,7 | 8,5 | 8,7 | 8,7 | 8,6 | 8,5 |
| Hỏa Nha | 8,6 | 8,7 | 8,5 | 8,5 | 8,7 | 8,6 | 8,5 |
| Thạch Thử | 8,6 | 8,7 | 8,5 | 8,5 | 8,7 | 8,6 | 8,5 |

**Điểm cuối: 8,5**, tự chấm nguồn, chưa thay giám khảo mù. Không bỏ ảnh. Tripo/runtime ngoài phiếu; boss ×2,5 cần xác nhận khi dựng. Anh xem hàng 66 px, nhất là sói/quạ. Bản cũ nguyên vẹn; không build/test/Git ghi.

