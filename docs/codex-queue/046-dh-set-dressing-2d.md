# Phiếu 046 · Rồng Giữ Ải · Ảnh 2D cho 8 món trang trí bản đồ (ảnh nguồn Tripo đợt 3)

**Luật:** ảnh 2D phải đạt từ 8 điểm (chủ dự án 27/10, `docs/games/ART_ACCEPTANCE.md` §2.2). Chưa đạt thì sửa prompt, tối đa 3 lượt mỗi ảnh. Ảnh nguồn Tripo không có ánh sáng hay vùng phát sáng nướng sẵn.

**Bối cảnh:**
- Map Factory đang thử bố cục bản đồ Rồng L2-cau (`docs/tools/map-factory/spike-l2-cau.md`).
- Người chấm độc lập cho trung vị 6,75 trên 10. Khoảng một nửa khoảng cách tới ảnh mẫu là do thiếu món trong bộ `pine-river`: không đèn, rào, đá vách, cụm cỏ hoa 3D, lau sậy, cầu tàu.
- Phiếu này vẽ ảnh nguồn cho 8 món đó. Claude chấm lại, rồi chủ dự án dựng trên web Tripo.
- **Không làm** Maple Tree (cây lá đỏ cam): luật màu của Rồng (`05` §2.2) giữ đỏ, cam, vàng kim cho tín hiệu. Làn Rồng quyết món này sau.

**Được ghi** (`art-src` là media, không vào Git):
- `games/dragon-hold/art-src/props/pine-river/<tên>.png` và `<tên>.prompt.txt` cho bản chọn; mỗi lượt thử là `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3);
- `games/dragon-hold/art-src/_review/046-*.jpg` và `_review/046/`;
- `docs/codex-queue/046-report.md`.

**Cấm:**
- ghi đè, đổi tên, xóa file có sẵn;
- chạy git;
- sửa mã hay tài liệu khác;
- dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
- đụng game khác, đụng Tu Tiên.

## Phong cách: giữ nguyên bộ `pine-river`

Đọc `docs/games/dragon-lane/art-requests/m0/03-pine-river-props.md` (§1 Luật chung, §3 prompt K01–K12, §4 Kiểm ảnh) và xem các ảnh có sẵn trong `games/dragon-hold/art-src/props/pine-river/*.png`, nhất là `pine-tall.png`, `rock-boulder.png`, `bridge-old.png`, `bush-moss.png`.

Mỗi prompt giữ **nguyên văn** các dòng chung của bộ: Image-to-3D source…, House style…, View…, Colour rules…, Light…, Build…, Never draw…, Background `#E6E6E6`. Chỉ thay dòng "Kit prop (pine-river forest, spring): …" bằng mô tả của món.

## Tám món

| Tên file | Tên (tiếng Anh) | Cỡ thật | Khổ | Mô tả cho dòng "Kit prop" |
|---|---|---|---|---|
| `lantern-post` | Lantern Post | cao 2,2 m | 1024×1536 | Cột gỗ vuông nâu ấm, chân đá thấp phẳng đáy. Một tay gỗ ngắn treo một đèn lồng giấy tròn màu kem, khung gỗ sẫm, **không thắp, không sáng**, có mái gỗ nhỏ trên đèn. Gỗ dày, chắc. |
| `rail-fence` | Rail Fence | dài 2,4 m, cao 1 m | 1536×1024 | Một đoạn rào gỗ mộc: hai cọc tròn đầu vạt, hai thanh ngang hơi cong, buộc dây thừng dày. Gỗ nâu xám có rêu nhẹ ở chân. Đứng thẳng, hai đầu cắt gọn để nối tiếp. |
| `cliff-rock-a` | Cliff Rock | cao 4 m | 1024×1536 | Một khối đá vách xám nhạt ấm, mặt gãy phẳng có cạnh sắc vừa, vài vạch tầng ngang, đỉnh hơi bằng. **Không rêu phủ mặt**, chỉ chút rêu ở chân. Khối đứng, cao hơn rộng. |
| `cliff-rock-b` | Cliff Rock (wide) | cao 2,5 m, rộng 4 m | 1536×1024 | Cùng chất đá với `cliff-rock-a`: hai khối gãy tựa nhau, thấp và rộng, mặt trên nghiêng. Dùng làm chân vách và mép vách. |
| `grass-tuft` | Grass Tuft | cao 0,5 m | 1024×1024 | Một cụm cỏ xuân xanh lá tươi, gom thành 3–4 khối lá tròn mềm như búi, đáy phẳng. Không sợi cỏ rời. |
| `wildflower-clump` | Wildflower Clump | cao 0,45 m | 1024×1024 | Một cụm cỏ thấp xanh, điểm hoa tròn nhỏ màu kem và tím nhạt (`#8E7CC3` nhạt hơn), gom thành khối, đáy phẳng. **Không hoa đỏ, cam, vàng.** |
| `reed-clump` | Reed Clump | cao 1,2 m | 1024×1536 | Một bụi lau sậy ven nước: các lá dẹt thẳng gom thành 4–5 bó dày, vài bông lau màu kem nâu ở ngọn, đáy phẳng. Không sợi mảnh. |
| `wooden-jetty` | Wooden Jetty | dài 4 m, rộng 1,6 m | 1536×1024 | Một cầu tàu gỗ nhỏ: mặt ván dày đặt trên bốn cọc tròn, đầu cọc nhô lên một chút, một bậc nhỏ ở đầu bờ. Gỗ nâu ấm, mép ván mòn. Cùng chất với `bridge-old.png`. |

## Việc

1. Viết prompt cho từng món theo khuôn ở trên. Ghi `.tryN.prompt.txt` cạnh mỗi lượt.
2. Tạo ảnh. Tự chấm từng lượt theo 5 tiêu chí của `ART_ACCEPTANCE.md` §2.2, ở cỡ đầy đủ và ở 128 px.
   - Đạt từ 8 thì dừng.
   - Chưa đạt thì sửa prompt; tối đa 3 lượt.
3. Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`. Không xóa các file `.try*`.

## Kiểm (bắt buộc)

1. **md5:** chạy `md5 -r` cho mọi file trong `props/pine-river/` trước (`_review/046/md5-before.txt`) và sau. `diff` chỉ được có dòng của file mới.
2. **Khổ và nền:**
   - `magick identify`: đúng khổ ở bảng.
   - Độ lệch chuẩn màu của 10 px mép trên, trái, phải, dưới ≤ 6/255, và màu trung bình gần `#E6E6E6` (mỗi kênh lệch ≤ 8).
   - Ghi số đo cho từng ảnh.
3. **Lề:** cắt nền bằng `magick <ảnh> -fuzz 12% -trim -format '%X %Y %w %h' info:`. Vật phải cách mép ảnh ≥ 24 px ở cả bốn phía.
4. **Màu giữ riêng:**
   - Đếm tỉ lệ px có hue đỏ, cam, vàng kim (0–50°) hoặc xanh ngọc (165–190°), với saturation > 0,55 và value > 0,5.
   - Mỗi ảnh phải ≤ 2 %. Riêng `lantern-post` tính cả giấy đèn kem; nếu vượt thì ghi rõ vùng nào.
5. **Tờ xem nhanh** `_review/046-sheet.jpg`:
   - hàng 1: 8 bản chọn;
   - hàng 2: cùng 8 ảnh ở 128 px, đặt cạnh `pine-tall.png`, `rock-boulder.png`, `bridge-old.png` cùng cỡ, để xem có hợp bộ không;
   - có nhãn;
   - một bản nền tối `#2A2A2A` của hàng 1.

## Báo cáo `docs/codex-queue/046-report.md`

- Bảng `| Món | Lượt | Prompt thêm hay sửa | Điểm 5 tiêu chí | Tổng | Còn thiếu |`.
- Bản chọn của từng món.
- Đầu ra của 5 mục Kiểm.

**Xong khi:** cả 8 món có lượt đạt từ 8 điểm, hoặc đủ 3 lượt và đã ghi bản tốt nhất kèm lý do chưa đạt.
