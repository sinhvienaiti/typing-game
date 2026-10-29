# Chấm nhận ảnh 29/10, lượt b: phiếu 116, 117, 118, 158, 159 (Wordwoven) và 119, 120, 140 (Dragonhold)

Người chấm: Claude, chấm lại độc lập theo `ART_DIRECTION_2026-10-28.md` §1.3 (M), `ART_ACCEPTANCE.md` §2.2 (Q) và §5 (hậu kỳ không phá tranh). Nhận khi **M ≥ 8 và Q ≥ 8**. Q ghi theo thứ tự Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp.

Tôi xem từng ảnh giao ở cỡ đầy đủ và ở cỡ trong game, không chỉ tờ của Codex. Tờ so của tôi (cùng thư mục, mỗi tờ dưới 1 MB):
- `158-vs-ref.jpg`: ảnh mẫu; `title-backdrop.v2` cắt 16 : 9 có logo 113 đặt thử; `poster.v2` (try2), `poster.v2.try1` và con rồng của try2 ở 1 : 1;
- `159-ring.jpg`: vòng ngày và vòng đêm chồng đủ lớp, cả 360°; từng vòng riêng (trời ngày, trời đêm, 320, 220, 140); góc nhìn 90° tại mối a|b~ và tại mối b|b~; bậc màu sương ở 1 : 1; ảnh mẫu;
- `116-raw-vs-final.jpg`: tám cặp bản sinh (nền M) | bản giao (alpha);
- `116-on-game-frame.jpg`: tám cây đặt lên khung game Wordwoven 1080p thật (`games/.wt-td-1c/tmp/lane-l3/road-sheets/td-1c-road-1920x1080-default.jpg`), cỡ theo mét ở 18 px/m (FOV 38°, 58 m), billboard ngả 22° (TK §23.10: 0,4 × 55°), cạnh ảnh mẫu; thêm bản 720p và phóng ×2 xem mép alpha;
- `140-icons.jpg`: mười icon, bản sinh | bản giao; cỡ 1080p và 720p trên vỏ cây `#2b2118` và kem `#f1e3c4` (phóng ×4, không làm mượt); dải 64 px cạnh mười icon 137–139 đã nhận; dải cỡ thật ×3 cạnh `gold` và `check`.

## Tổng

| Phiếu | Game | Nhận | Làm lại | Ghi chú |
|---|---|---:|---:|---|
| 116 | Wordwoven | 8 | 0 | Cả tám cây đạt; hậu kỳ giữ nguyên tranh |
| 117 | Wordwoven | — | — | **Chưa xong:** không có `117-report.md`, không có bản chọn (chỉ có `.try*` của năm loại). Không chấm |
| 118 | Wordwoven | — | — | **Chưa xong:** báo cáo ghi 0/8, chưa gọi `image_gen` (chờ 117). Không chấm |
| 119 | Dragonhold | — | — | **Chưa xong:** báo cáo ghi 0/5, chưa sinh (chờ 118). Chưa có logo nên chưa kiểm được chính tả "Dragonhold" |
| 120 | Dragonhold | — | — | **Chưa xong:** báo cáo ghi 0/6, chưa sinh (chờ 119). Có một câu hỏi cần tôi quyết, trả lời ở mục 120 |
| 140 | Dragonhold | 9 | 1 | `easier` |
| 158 | Wordwoven | 1 | 1 | Nhận `title-backdrop.v2`; `poster.v2` làm lại, đổi cách |
| 159 | Wordwoven | 0 | 8 | Hết "đảo", nối a\|b đẹp; nhưng xếp lật gương thành vạn hoa. Bốn ô giữ làm nền cho vòng liền |
| **Cộng** | | **18** | **10** | |

**Hậu kỳ (§5).** Lượt này không phiếu nào phá tranh:
- 116: chỉ tách nền, cắt, đổi cỡ, thêm lề, ngưỡng alpha 50 % ở mép;
- 158: bản giao trùng byte bản sinh (MD5 kiểm lại);
- 140: tách nền, căn lề, `status-new` sáng +4 % (trong ±10 %);
- 159: giữ tranh, chỉ hòa mép và tách nền. Một lỗi nhỏ do chính bước nối: bậc màu sương ở dải nối 140 (sửa bằng công cụ, mục 159).

Codex đã dừng đúng chỗ ở mọi ngưỡng số mâu thuẫn với tranh, và ghi lại để tôi quyết. Các quyết định nằm ở từng phiếu dưới đây.

**Người chấm thứ ba (§4).** Hai chỗ nằm hai phía ngưỡng:
- `easier` của 140: Codex 8, tôi 7,5;
- vòng 159: Codex M 8, tôi 6,5–7,5.

Lỗi của cả hai thấy ngay trên tờ: `easier` đọc thành chiếc giày ở 16–24 px; vòng 159 thành vạn hoa ở mối b|b~. Sinh lại rẻ (`easier` mới dùng 1/3 lượt), nên tôi đề nghị làm lại luôn. Điều phối có thể gọi người thứ ba nếu muốn.

---

## 116 · Wordwoven · cây lớn và mép rừng (v3, v4)

Trên khung game thật, tám cây đọc ngay là bàng, thông, tre, mép rừng ở cả 1080p và 720p. Vẽ thật, khối lớn, không viền mực, mép alpha sạch ở ×2. Chúng nâng hẳn cảnh so với bộ v1, v2. Phần kéo cảnh xuống hôm nay là mặt cỏ một màu của khung game (việc của làn L, không phải của phiếu này).

M chung của lớp cây: **8**, "đứng cạnh được" về chất liệu và dáng. Cả cảnh trên khung đó chỉ khoảng 6, vì đất.

Hue trung vị của tán: bàng 81–82°, tre 96–98°, thông 115–117°, khối tán 142–143°, đều trong khoảng 80–150° của bible. Tre và khối tán có độ bão hòa 0,57–0,63, hơi trên 0,55. Luật 0,55 là luật cỏ; ở cây thì chấp nhận được.

| File (`scenery/meadow/`) | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `almond-tree-v3.png` | 8 | 9 (2/2/1,5/2/1,5) | **Nhận** | Bàng cổ thụ ba tầng, thân bạnh rõ. Tán ngả vàng ô liu hơn ngọc, dáng hơi giống bonsai lớn. Nguồn 1254 px được phóng lên 1536 (không thêm chi tiết, không hại). |
| `almond-tree-v4.png` | 8 | 9 (2/2/1,5/2/1,5) | **Nhận** | Hai thân tách gốc, hai tầng rộng, khác v3 rõ; cùng ghi chú màu tán. |
| `mountain-pine-v3.png` | 8 | 9 (2/1,5/2/2/1,5) | **Nhận** (sát ngưỡng) | Thông đá thân đỏ uốn, bốn đệm kim. Thân mảnh, đệm nhỏ ở 720p, nhưng dáng vẫn đọc. Codex 8,1, tôi 8: cùng phía ngưỡng. |
| `mountain-pine-v4.png` | 8 | 8,5 (2/2/2/1,5/1) | **Nhận** | Thấp rộng, nhánh chết bạc đọc tốt. Canvas trống 49 % phía trên: cắt sát vật khi đóng gói billboard (công cụ, miễn phí), để khỏi tốn diện tích vẽ. |
| `bamboo-clump-v3.png` | 8 | 8,5 (2/1,5/2/2/1) | **Nhận** | Khóm tre cao cong trái, thân ngọc vàng có đốt. Lá còn vài sợi mảnh, ở camera 55° vẫn gom thành khối. |
| `bamboo-clump-v4.png` | 8 | 9 (2/2/2/2/1) | **Nhận** | Khóm đứng dày, thân khô nhạt; khác v3 rõ. |
| `canopy-block-v3.png` | 8 | 9 (1,5/2/2/2/1,5) | **Nhận** | Bốn tán hạ bậc, bóng teal, ngọn vàng. Lộ thân nhiều hơn brief, ở mép rừng lại hợp. |
| `canopy-block-v4.png` | 8,5 | 9,5 (2/2/2/2/1,5) | **Nhận** | Đẹp nhất bộ: hai hàng tán lệch, hàng sau tối, đúng kiểu mép rừng của TK §23.10. |

Khi gắn: tắt viền mực của `prepare-scenery` cho v3, v4; giữ ramp 3 bậc, đáy tối 25 %, rim 15 % (bible §2.7). Thôi dùng v1, v2 nhưng không xóa. Cần một bóng tiếp đất mềm dưới gốc (tờ của tôi có đốm bóng; không có thì cây trông như tấm dán).

## 117, 118 · Wordwoven · cây thấp, cỏ, hoa; đá và gỗ

Chưa xong, không chấm:
- **117:** không có báo cáo. Có `.try1` (và `wildflowers-v3.try2`) của `fern`, `reed-clump`, `tall-grass`, `wildflowers`, `raspberry-bush`, nhưng chưa có bản chọn.
- **118:** báo cáo nói rõ 0/8, chỉ ghi sẵn tám prompt, chờ 117.

## 119, 120 · Dragonhold · màn tựa, logo; trời và phông xa

Chưa xong, không chấm (0/5 và 0/6). Codex dừng vì dòng "Thứ tự: sau 118" và "sau 119", và đã hỏi chủ dự án trong phiên.

**Đề nghị cho điều phối:**
1. **Cho 119 chạy ngay.** "Sau 118" là thứ tự hàng đợi, không phải phụ thuộc nội dung: 119 không dùng ảnh nào của 117 hay 118.
2. **120 vẫn chạy sau 119**, vì cần màu và nắng của màn tựa.
3. **Sửa phiếu 120 trước khi Codex chạy.** Phiếu đang chép đúng thiết kế đã hỏng ở 114/159: mép 8 % lặng, "no cloud touches the edge", xếp lật gương. Sửa như sau:
   - Bỏ câu "The left 8% and the right 8% … calm and plain … when mirrored" trong khối RING, và câu "The left 8% and the right 8% are plain open sky … no cloud touches or crosses the left or right edge, so tiles join … when mirrored" trong khối SKY.
   - Vòng 170 m và vòm trời dùng **bốn ô khác nhau vẽ nối tiếp**: `a | b | c | d`. Mỗi ô sau sinh bằng sửa ảnh nối tiếp từ 25 % mép phải của ô trước; khép vòng `d → a` bằng sửa ảnh dải nối như 159 đã làm. Vòng 260 và 380 m dùng **hai ô khác nhau, không lật**: `L | L2 | L | L2`.
   - Kiểm 3 "nền sạch 10 px bốn mép": **chỉ kiểm phía trên đường chân núi.** Hai cạnh bên và đáy dưới chân núi là tranh. Đây là trả lời cho câu hỏi Codex ghi trong báo cáo 120.
   - Bỏ kiểm 4 về dải 8 % và "≤ 6/255 hai dải trời". Thay bằng: ghép vòng 6144 px; cắt góc nhìn 90° tại cả bốn mối; không trục gương nào, không mối nào thấy được ở 1 : 1.
   - Bỏ ngưỡng "≤ 5 % cột alpha mềm". Thay bằng soi ×2 trên trời sáng và trời tối: không quầng, không viền hồng.

---

## 140 · Dragonhold · kết quả (10 icon)

Cùng chất liệu với 137–139 (granite kem, vàng búa, men than). Đặt cạnh mười icon đã nhận ở 64 px thì thấy cùng một bộ. Sách, bia và bậc vẽ xiên 3/4, hơi lệch "flat, straight on" của STYLE-UI; tôi đã trừ ở Hợp bộ.

| File (`ui/icons/`) | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `star-lit` | 8,5 | 9,5 (2/2/2/2/1,5) | **Nhận** | Sao vàng búa năm cánh vát, rõ ở 37 px. |
| `star-unlit` | 8 | 8,5 (2/1,5/2/2/1) | **Nhận (ngoại lệ tương phản)** | Trên vỏ cây ΔY 0,17, nhưng ở 37–55 px dáng sao vẫn đọc nhờ cạnh vát sáng. Câu "một trong hai nền tối" của phiếu là lỗi viết: hai nền là một tối, một kem. Tôi đọc là "một trong hai nền", nên kem 0,58 đạt. Không làm sáng sao sắt. Trên thẻ kết quả tối, đặt sao trong ổ (khung UI), đừng sửa ảnh. |
| `stat-accuracy` | 8 | 8,5 (2/1,5/1,5/2/1,5) | **Nhận** | Bia bắn đọc rõ ở 20 px; tên chẻ chỉ còn một nét. |
| `stat-new-words` | 8 | 9 (2/1,5/2/2/1,5) | **Nhận** | Sách mở có ánh than, rõ ở 20 px. |
| `stat-words-seen` | 8 | 8,5 (2/1,5/1,5/2/1,5) | **Nhận** | Chồng bia đá; ở 20 px là "chồng phiến", đủ khác `stat-new-words` (IoU 0,78). |
| `retry` | 8 | 8 (2/1,5/2/1,5/1) | **Nhận** (sát ngưỡng) | Mũi tên tròn than hồng rõ ở 24 px. Ở 16 px (720p) đọc thành chữ "C", điều đáng tránh trong game gõ chữ. Ở 720p hiện nút này ≥ 20 px. Khi tiện thì khép cung tới khoảng 300°. Codex 8, tôi 8: cùng phía. |
| `easier` | 7,5 | 7,5 (2/1/1,5/2/1) | **Làm lại** | Bậc đá hạ và lông vũ, vẽ xiên. Ở 16–24 px cả khối đọc thành một chiếc giày hay dép, không ra "dễ hơn". |
| `status-learned` | 8 | 8 (2/1/2/2/1) | **Nhận** (sát ngưỡng) | Dấu sáp vàng có dấu kiểm. Ở 20 px thấy dấu kiểm; ở 14 px thành đĩa vàng, khác dáng chồng xu của `gold` nhưng mất dấu kiểm. Ở 720p dùng ≥ 20 px, hoặc dùng `check` (138) cho cỡ 14 px. |
| `status-review` | 8 | 8,5 (2/1,5/2/2/1) | **Nhận** | Trang giấy có dải đánh dấu và ngọn lửa; khác hẳn hai trạng thái kia ở 14 px. |
| `status-new` | 8 | 8,5 (2/1,5/2/2/1) | **Nhận** | Mầm than hai lá, dáng chữ Y rõ ở 14 px. |

## 158 · Wordwoven · làm lại nền tựa và poster (113)

| File (`ui/title-epic/`) | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `title-backdrop.v2.png` | 8 | 8,5 (2/2/2/1,5/1) | **Nhận** | Một lượt sửa ảnh, hậu kỳ không đụng (trùng byte nguồn). Hộp tối đã hết; rồng xuống thung bên trái và đọc tốt; tháp nhọn sang phải. Chi tiết ở 1 : 1 giữ ngang try1. Logo 113 đặt thử đọc rõ trên trời tự nhiên; Fort nằm dưới nét lượn, rùa ở bên phải logo, không chồng. Trừ: vẫn "dày kiểu AI", ít vùng nghỉ; ruộng bậc thang bên phải còn vàng chanh rực. |
| `poster.v2.png` (= `poster.v2.try2.png`) | 7,5 | 7,5 (1/2/2/1/1,5) | **Làm lại, đổi cách** | Đã hết ba lượt (113 try1, v2.try1, v2.try2). Hai cánh vẽ thành hai thân rắn phủ vảy có diềm lông, uốn chữ S (thấy ở 1 : 1); đây là lỗi giải phẫu ngay ở trọng tâm. Vách trái vẫn cao hơn tán cây; cánh phải lấn vùng trời 22 % dành cho logo. Codex tự chấm Q 7,5, đúng. |

**Các mâu thuẫn Codex ghi lại, tôi quyết:**
- **Bỏ ngưỡng độ lệch chuẩn luma ≤ 0,14 của vùng menu.** Menu nằm trên bảng khung 115, khung lo tương phản. Không làm tối tranh.
- **Dải logo: nhận như hiện tại.** Mép đầu rùa và mái Fort chạm rìa dải, nhưng logo đặt thật không chồng lên gì.
- **Ruộng vàng chanh: không chặn.** Ghi vào `ART_REPLACE_LATER.md` (2D, 8 điểm, "ruộng bậc thang phải còn vàng chanh"). Khi tiện, sửa bằng một lượt sửa ảnh, không chỉnh màu cục bộ bằng công cụ (§5):
  ```text
  Edit the attached image. Make the rice terraces on the right a deeper jade green with muted ripe-gold, not lemon yellow. Keep everything else identical.
  ```

## 159 · Wordwoven · làm lại vòng trời và phông xa (114)

Tôi tự ghép vòng như game xếp: ngày, đêm và 140 là `a | b~ | b | b~`; 320 và 220 là `L | L~ | L | L~`. Tôi xem từng vòng riêng, rồi chồng đủ lớp, rồi cắt các góc nhìn 90° tại từng mối.

**Đã sửa được:**
- Hết vai phẳng, hết dải phẳng, hết "đảo" ở 140.
- Hai dải nối 140 (sửa ảnh) rất tốt. Góc nhìn tại mối a|b~ đạt khoảng 8: cổng, thác, trời mây chạy liền.
- Mép alpha sạch ở ×2 trên trời sáng và tối.
- Vệt cột tím ở 140-a đã hết.

**Hỏng mới do cách xếp lật gương.** Ở mối b|b~ và b~|b, cả bốn lớp cùng đối xứng quanh một trục. Góc nhìn 90° tại đó là một bức **vạn hoa** (Rorschach), khoảng M 6. Ở 320 và 220, cả bốn mối đều là trục gương, nên cả vòng chỉ là một cặp đỉnh (320) hay một cặp tháp sinh đôi (220) lặp bốn lần. Đó vẫn là cái "giấy dán tường" mà chỉ đạo cấm, chỉ đổi từ đảo sang gương.

**Trời:**
- Trời ngày riêng: bốn cụm mây cách nhau, hai cụm soi gương.
- Trời đêm: ô trăng thành một bức riêng (mật độ đèn khác hẳn, dải sương khác). Mối a|b có một sọc tối rộng khoảng 230 px, do hòa 115 px mỗi bên. Ngân Hà gập thành chữ V ở hai mối gương.

**Lỗi nhỏ do bước nối:** sương đáy của dải nối bên trái mỗi ô 140 sáng hơn thân ô (a: 40,122,133 so với 54,111,121). Tạo một khối sương sáng có cạnh đứng, thấy ở 1 : 1.

Tôi nhận các ngoại lệ kỹ thuật Codex nêu:
- cột alpha mềm 16–22 %: soi ×2 không thấy quầng;
- 1–8 pixel tím rời: không thấy ở cỡ thật;
- trời không qua "≤ 6/255 hai dải 8 %";
- đường chân núi không đúng mốc cũ.

Luật mới thay các ngưỡng đó nằm ở mục sửa dưới đây.

| File (`backdrops/w1-silverfall-epic/`) | M (trên vòng) | Q (từng ô) | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `sky-day-a.v2.png` | 7 | 8,5 (2/2/2/2/0,5) | **Làm lại vòng; giữ ô làm ô 1** | Ô đẹp. Vòng thành bốn cụm mây, hai cụm soi gương. |
| `sky-day-b.v2.png` | 7 | 8,5 (2/2/2/2/0,5) | **Làm lại vòng; giữ ô làm ô 2 (lật)** | Nối với a tốt. Tự soi gương ở b\|b~. |
| `sky-night.v2.png` | 6,5 | 7,5 (2/2/1,5/2/0) | **Làm lại** | Ô trăng là một bức riêng; sọc tối ở mối với b. |
| `sky-night-b.v2.png` | 6,5 | 7,5 (2/2/1,5/2/0) | **Làm lại** | Vẽ như một ảnh khác, không nối tiếp ô trăng; Ngân Hà gập chữ V ở mối gương. |
| `layer-320.v2.png` / `.alpha` | 7 | 8 (1/2/2/2/1) | **Làm lại vòng; giữ ô làm L** | Liền, nhưng một cặp đỉnh soi gương lặp bốn lần. |
| `layer-220.v2.png` / `.alpha` | 6,5 | 8 (2/2/2/1,5/0,5) | **Làm lại vòng; giữ ô làm L** | Cặp tháp sinh đôi và khe thấp lặp bốn lần, đọc như giấy dán tường. |
| `layer-140-a.v2.png` / `.alpha` | 7,5 | 8,5 (2/2/2/2/0,5) | **Làm lại vòng; giữ ô làm ô 1** | Cổng một lần, nối a\|b~ đẹp. Còn trục gương ở b\|b~ và bậc sương ở dải nối trái. |
| `layer-140-b.v2.png` / `.alpha` | 7,5 | 8 (2/2/1,5/2/0,5) | **Làm lại vòng; giữ ô làm ô 2 (lật)** | Như a; ruộng sáng và dày hơn a. |

---

## Sửa cho từng ảnh làm lại (dán vào phiếu làm lại)

### 140 `easier` (sinh lượt 2; còn 2 lượt)

```text
Three broad steps of weathered cream granite seen exactly from the side, descending from the upper left to the lower right, with one bold hammered-gold arrow pointing down along the steps and a soft ember glow on its tip; a compact silhouette that fills a square; flat and straight on, no perspective, no feather, no boot or shoe shape.
```

Kiểm:
- ở 16 và 24 px trên vỏ cây và kem, đọc ra "bậc đi xuống";
- IoU với mọi icon khác của 140 ≤ 0,80;
- chiều bậc và mũi tên ngược với `upgrade` (138);
- tờ bản sinh | bản giao như cũ.

### 158 `poster` (đổi cách: sửa ảnh từ `poster.v2.try1.png`, tối đa 3 lượt sửa)

`poster.v2.try1` có cánh đúng giải phẫu (hai cánh lông gắn ở vai, như keyart) và cây lớn, chỉ có cánh phải chạm mép trên. Sửa từng việc một:

1. Đính kèm `poster.v2.try1.png` và `keyart.png`:
   ```text
   Edit the first attached image. Zoom out slightly and extend the storm sky upward: the whole dragon, including both wing tips, sits inside the frame, with open storm sky and soft god rays filling the top fifth above it. Keep the dragon's wings exactly like the second attached image: two broad feathered wings attached at the shoulders, never serpent-like. Keep the dragon, the Tree Spirit, the Fort, the river, the light and all colours identical.
   ```
2. Nếu vách trái vẫn cao hơn tán cây:
   ```text
   Edit the attached image. Lower the karst towers on the left behind the Tree Spirit so that its crown is the highest point in the left half of the image. Keep everything else identical.
   ```

Hậu kỳ: chỉ đổi cỡ về 1024 × 1536 (cắt giữa nếu tỉ lệ lệch). Kiểm thêm:
- ở 384 px, hai cánh trọn khung, gắn ở vai;
- tán cây cao hơn mọi vách ở nửa trái;
- 20 % trên cùng không có rồng; logo 113 đặt thử ở rộng 70 % vẫn đọc.

Trong lúc chờ: `poster.v2` (7,5) chỉ dùng tạm nếu có chỗ bắt buộc cần poster, và ghi vào `ART_REPLACE_LATER.md`. Màn tựa không cần poster.

### 159, năm vòng: bỏ lật gương, vẽ vòng liền

1. **Không xếp lật gương nữa.** Bỏ luật "ô `-b` lật ngang xen kẽ" của 114 và 159.
   - Trời ngày, trời đêm và 140: mỗi vòng **bốn ô khác nhau** `1 | 2 | 3 | 4`.
   - 320 và 220: **hai ô khác nhau, không lật**, `L | L2 | L | L2`. Mỗi chi tiết chỉ lặp ở 180°, không bao giờ nằm trong cùng một góc nhìn.
2. **Giữ những gì đã tốt làm ô đầu:**
   - 140: ô 1 = `layer-140-a.v2`, ô 2 = `layer-140-b.v2` lật ngang (giữ mối a|b~ đã nối);
   - trời ngày: ô 1 = `sky-day-a.v2`, ô 2 = `sky-day-b.v2` lật;
   - 320 và 220: L = bản `.v2`.
3. **Vẽ nối tiếp:** dựng canvas 1536 × 1024. 25 % trái là 384 cột mép phải của ô trước (đúng chiều đang hiện trong vòng); phần còn lại là nền magenta với ô núi, màu trời với ô trời. Sửa ảnh:
   ```text
   Continue this panorama to the right: the left quarter of the attached image is fixed and must stay unchanged; paint the rest as the same scene continuing naturally to the right, with the same light, haze, colours, skyline height band and bottom haze. A different arrangement of towers and clouds, never a mirror of the left part. Rice terraces are deep jade green and muted ripe gold, not lemon yellow.
   ```
   Với ô trời bỏ câu về towers và terraces. Cắt lấy ô mới. Ô 3 nối tiếp ô 2, ô 4 nối tiếp ô 3. 320 và 220: L2 nối tiếp L.
4. **Khép vòng:** mép phải ô 4 (hay L2) nối vào mép trái ô 1 (hay L) bằng đúng cách dải nối 159 đã làm cho 140 (sửa ảnh dải 15 % quanh mối, hòa cosin, giữ phần giữa).
5. **Trời đêm làm lại cả vòng:** ô 1 = `sky-night.v2` (ô trăng duy nhất). Ô 2–4 vẽ nối tiếp từ ô 1 theo bước 3. Ngân Hà chạy liền một dải, ít đèn dần ra xa trăng. Bỏ `sky-night-b.v2` và bước hòa 115 px.
6. **Bậc sương ở dải nối (công cụ, §5 cho phép "làm liền mép"):** dưới 85 % chiều cao, hòa màu sương của dải nối vào thân ô bằng dốc cosin ngang ≥ 200 px. Kiểm theo hàng: mỗi kênh lệch ≤ 3/255 qua ranh dải. Áp cho cả hai ô 140 hiện có và mọi dải nối mới.
7. **Kiểm nhận (thay các ngưỡng cũ):**
   - ghép vòng 6144 px như game, chồng đủ lớp;
   - cắt góc nhìn 90° tại cả bốn mối và giữa mỗi ô;
   - không có trục gương nào;
   - trong một góc 120° không thấy cùng một tháp hay cụm mây hai lần;
   - không mối nào thấy được ở 1 : 1;
   - đúng một mặt trăng;
   - nền magenta chỉ kiểm phía trên đường chân núi;
   - mép alpha soi ×2 trên trời sáng và tối: không quầng, không viền hồng.

   Bỏ các ngưỡng: mép 8 % lặng, "≤ 6/255 hai dải 8 %", "≤ 5 % cột alpha mềm", đường chân núi đúng 60/62 %.
8. **Lượt sinh:** mỗi ô mới tối đa 3 lượt. Ước tính 9 ô mới (140: 2; trời ngày: 2; trời đêm: 3; 320: 1; 220: 1), cộng 5 dải khép vòng.

**Nếu bản demo cần vòng trước khi có bản liền (tạm, chưa nhận):**
- xoay vòng 220 lệch 1/8 vòng và 320 lệch 3/16 vòng so với 140, để các trục gương không trùng nhau;
- camera màn tựa nhìn về ô 140-a;
- không cho camera quay quanh qua mối b|b~.

---

## Sẵn sàng gắn

**Wordwoven** (`games/typing-defense/art-src/`)
- **116, cây v3/v4 (tám ảnh):**
  - `scenery/meadow/{almond-tree,mountain-pine,bamboo-clump,canopy-block}-{v3,v4}.png`, nền `#FF00FF`, cho `prepare-scenery` với viền mực tắt;
  - alpha đã tách để đối chiếu: `_review/116/handoff-v2/<tên>.final/alpha.png`;
  - cắt sát vật khi đóng gói (nhất là `mountain-pine-v4`, trống 49 % phía trên);
  - cỡ: bàng 14–18 m, thông 10–14 m, tre 12–16 m, khối tán 10–14 m;
  - mép rừng dựng từ `canopy-block-v3/v4`, hai đến bốn hàng lệch, hàng sau tối 8 %.
- **158, màn tựa:**
  - `ui/title-epic/title-backdrop.v2.png` (và `.v2.384.png`). Điều phối chép thành tên chính khi nhận, theo phiếu 158 ("Claude đổi sang khi nhận");
  - cắt giữa 16 : 9 là `1536x864+0+80`;
  - logo `ui/title-epic/logo.alpha.png` (đã là bản sạch, MD5 trùng `_review/113/delivery-alpha/logo.alpha.png`), rộng khoảng 45 %, giữa trên; không vệt tối nung vào tranh;
  - huy hiệu `ui/title-epic/emblem.alpha.png` / `.512.png` (đã sạch);
  - keyart `ui/title-epic/keyart.png` (nhận ở lượt trước);
  - menu nằm trên bảng khung 115.
- **159:** chưa có gì để gắn.

**Dragonhold** (`games/dragon-hold/art-src/ui/icons/`; Claude chép vào `public/` khi gắn)
- **140 (chín icon):** `star-lit`, `star-unlit`, `stat-accuracy`, `stat-new-words`, `stat-words-seen`, `retry`, `status-learned`, `status-review`, `status-new`. Mỗi tên có `.png` (1024), `.256.png`, `.128.png`, `.64.png`.
  - Cỡ hiện như bảng của phiếu, trừ: `retry` và `status-learned` ≥ 20 px ở 720p (hoặc `check` của 138 thay `status-learned` ở 14 px).
  - `star-unlit` đặt trong ổ sao trên nền tối.
  - Chưa gắn `easier`.

**Ghi vào `ART_REPLACE_LATER.md` (2D, 8–8,5, nâng khi tiện):**
- 116: `almond-tree-v3/v4` (tán ngả ô liu), `mountain-pine-v3` (thân mảnh), `mountain-pine-v4` và `bamboo-clump-v3` (8);
- 158: `title-backdrop.v2` (ruộng vàng chanh, dày);
- 140: `star-unlit` (ngoại lệ tương phản), `retry` (chữ C ở 16 px), `status-learned` (mất dấu kiểm ở 14 px), và các icon M 8.
