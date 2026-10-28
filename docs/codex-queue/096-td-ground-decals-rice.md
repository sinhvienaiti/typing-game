# Phiếu 096 · Lời Gọi · Hai tờ decal mặt đất và ô ruộng lúa cho map 1 3D

**Vì sao:** kiểm kê map 1 ngày 28/10 (I2 và I3, P1, cổng G2). Mặt đất 3D của w1-silverfall (bước 1C) cần decal để phá lặp, cần dấu chỗ cây luật đứng, và cần ô ruộng cho từng trạng thái của Rice Field. Hôm nay chưa có ảnh nào.

**Báo cáo:** `docs/codex-queue/096-report.md`.

## Luật chung

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh ghi vào `games/typing-defense/art-src` (media, không vào Git).
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Tối đa 3 lượt tạo mỗi ảnh.
- **Chỉ được ghi:**
  - `games/typing-defense/art-src/scenery/meadow/decals/<tên>.*` và `games/typing-defense/art-src/scenery/meadow/rice/<tên>.*`, theo mẫu tên: `.tryN.png`, `.tryN.prompt.txt`, `.tryN.alpha.png`, `.tryN.tile.png`, bản chọn `<tên>.png` hay `<tên>.alpha.png` kèm `<tên>.prompt.txt`, và `<tên>.json` cho lưới;
  - `games/typing-defense/art-src/_review/096-*.jpg` và `_review/096/`;
  - file báo cáo.
- **Cấm:** ghi đè, đổi tên, xóa file có sẵn hay file `.try*`; mọi lệnh git; sửa mã hay tài liệu khác; dev server, trình duyệt, mạng ngoài công cụ tạo ảnh; đụng game khác; đọc hay ghi Tu Tiên; chữ, số, logo, người, con vật, nhà trong ảnh.

## Phong cách

- Mở đầu mỗi prompt bằng nguyên văn khối **STYLE** ở `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md` §3.1.
- Decal nhìn thẳng từ trên, ánh sáng phẳng, không bóng đổ, không viền mực (trừ gốc cây). Mỗi decal mép mềm dần vào nền, không có viền cứng.
- **Alpha:** dùng alpha thật nếu công cụ cho ra; nếu không, vẽ trên nền khóa màu đúng luật §3.8 (G, M hay B tùy màu của vật), rồi tách thành `.alpha.png` bằng công cụ, không để sót viền màu nền.
- Ô ruộng là ô đặc, nhìn từ trên, liền mép, như phiếu 095.

## Ảnh

### A. `decals-ground-a` · atlas 2048×1024, lưới 4 × 2, ô 512, alpha

Thứ tự ô, trái sang phải, trên xuống dưới:
1. mảng đất mòn tròn;
2. đất dưới tán cây (sẫm hơn, có lá mục);
3. mảng ngã ba lối mòn;
4. đoạn lối mòn thẳng, hai đầu mờ dần;
5. và 6. hai biến thể của ô 1;
7. và 8. hai biến thể của ô 4.

### B. `decals-ground-b` · atlas 2048×1024, lưới 4 × 2, ô 512, alpha

1. khóm hoa dại nhỏ, kem, vàng nhạt, tím nhạt;
2. cụm sỏi xám bạc;
3. lá rụng nâu vàng;
4. gốc cây nhìn từ trên (vòng gỗ, vỏ, có viền mực mảnh);
5. vòng vụn gỗ và dăm, dấu chỗ cây luật bị chặt;
6. biến thể của ô 1;
7. biến thể của ô 2;
8. biến thể của ô 5.

Mỗi tờ kèm `<tên>.json`: `{ "cols": 4, "rows": 2, "cell": 512, "names": [ 8 tên ô, theo thứ tự ] }`.

### C. Ô ruộng Rice Field · năm ô 1024×1024, đặc, liền mép

| Tên file | Trạng thái |
|---|---|
| `paddy-flooded` | ruộng bùn ngập nước, mặt nước bạc phản trời nhạt, bờ ruộng không vẽ (game tự vẽ bờ) |
| `paddy-seedling` | mạ non xanh mởn cắm thành hàng thưa trên nước |
| `paddy-green` | lúa xanh dày, hàng đều |
| `paddy-ripe` | lúa chín vàng, bông trĩu |
| `paddy-stubble` | gốc rạ vàng xám trên đất ẩm sau gặt |

Cả năm ô cùng cỡ hàng lúa, cùng hướng hàng (dọc ảnh) và cùng khoảng cách hàng, để chuyển trạng thái tại chỗ mà không nhảy. Làm liền mép bằng đúng cách ở phiếu 095, mục "Làm liền mép".

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/scenery/` (đệ quy) trước (`_review/096/md5-before.txt`) và sau. `diff` chỉ có dòng của file mới.
2. **Khổ và lưới:** `magick identify` đúng khổ.
   - Atlas: mỗi decal nằm trọn trong ô của nó, cách mép ô ≥ 24 px; dải 24 px quanh mỗi biên ô có alpha 0 ở 100 % số px.
3. **Alpha sạch** (hai atlas):
   - alpha min 0, max 255;
   - trên vùng alpha 1–254, không còn màu nền khóa: px có hue trong ±15° của màu nền và saturation > 0,5 chiếm ≤ 0,1 %;
   - đốm rời nhỏ hơn 20 px: 0.
4. **Ô ruộng liền mép:** `E ≤ 1,25 · I` như phiếu 095. Khoảng cách hàng lúa đo bằng tự tương quan theo trục X trên `paddy-seedling`, `paddy-green`, `paddy-ripe`: lệch nhau ≤ 5 %.
5. **Ảnh kiểm:**
   - `_review/096-decals.jpg`: hai atlas trên nền `grass-a` của phiếu 095 nếu đã có, nếu chưa thì trên nền xanh cỏ `#7FA35B`;
   - `_review/096-rice.jpg`: năm ô ruộng, mỗi ô lát 2 × 2, xếp theo thứ tự trạng thái.
6. **KA5 tự chấm:** 5 tiêu chí của §2.2, ở cỡ đầy đủ và ở 128 px.

## Báo cáo `docs/codex-queue/096-report.md`

Tiếng Việt: bảng lượt và điểm cho từng ảnh; đầu ra sáu mục Kiểm; bản chọn và lý do.

**Xong khi:** hai atlas và năm ô ruộng có bản chọn tự chấm từ 8 và qua mục Kiểm 1–4. **Nhận** khi Claude chấm lại từ 8.
