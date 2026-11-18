# Phiếu 185 · Ba tranh ra mắt boss

Ngày 29/10/2026, Mac mini M4. **Đã giao 3/3 bản chọn, đúng 1600 × 900; tự chấm trên bản hậu kỳ: M ≥ 8, Q ≥ 8.** Sinh bằng `image_gen` tích hợp, tổng 5 lượt thành công: Dragonhold 2, Wordwoven 2, Last Line 1. Giữ mọi `.tryN.png` và prompt nguyên văn; không ảnh nào quá 3 lượt.

## 1. Bản chọn và tờ xem

| Game · boss | Bản chọn | Lượt | M · mức chợ | Q · chất lượng |
|---|---|---|---|---|
| Dragonhold · Moss Bannerman | [boss-moss-bannerman.png](../../games/dragon-hold/art-src/ui/boss/boss-moss-bannerman.png) | 2 | **8,7 · đạt** | **9,0 · đạt** |
| Wordwoven · Mộc Tinh | [boss-moc-tinh.png](../../games/typing-defense/art-src/ui/boss/boss-moc-tinh.png) | 2 | **8,8 · đạt** | **9,0 · đạt** |
| Last Line · Void Leviathan | [boss-void-leviathan.png](../../games/typing-survival/art-src/ui/boss/boss-void-leviathan.png) | 1 | **8,8 · đạt** | **9,1 · đạt** |

Tờ tổng bắt buộc: [185-sheet.jpg](../../games/typing-defense/art-src/_review/185-sheet.jpg). Ba bản hậu kỳ hiện ở **480 × 270**, cạnh ảnh mốc thương mại của chủ dự án cùng chiều cao; nhận xét tự chấm: **đứng cạnh được**. Đây là tranh ra mắt boss, chưa phải ảnh tích hợp trong game.

Trong từng thư mục `games/<id>/art-src/ui/boss/` có:

- `<tên>.png`, `<tên>.prompt.txt`: bản chọn và đúng prompt đã gửi cho lượt chọn.
- `<tên>.tryN.png`, `<tên>.tryN.prompt.txt`: bản sinh gốc và prompt từng lượt.
- `<tên>.480.png`, `<tên>.480.prompt.txt`: bản thu nhỏ đã xem để kiểm dáng; prompt giữ nguyên từ bản chọn.
- `<tên>-before-after.jpg`, `<tên>-before-after.prompt.txt`: tờ đối chiếu; tệp prompt là prompt của tranh nguồn, cách ghép được ghi ở mục 3.

## 2. Tham chiếu và điều chỉnh từng lượt

Prompt bắt đầu bằng nguyên văn STYLE trong `ART_DIRECTION_2026-10-28.md`: Dragonhold §3.2, Wordwoven §2.2, Last Line §4.3 hướng B; sau đó là mô tả boss, bố cục và vùng chữ. Có dòng yêu cầu dùng ảnh đính kèm để giữ thế giới, nhân vật, màu và vật liệu, rồi vẽ tranh mới.

| Boss | Hai ảnh thực sự đính kèm | Điều chỉnh |
|---|---|---|
| Moss Bannerman | `dragon-hold/art-src/generals/moss-banner.png`; `dragon-hold/art-src/ui/title-epic/keyart.png` | Lượt 1 đúng mặt nạ gỗ, mắt vàng xanh, giáp đá tím xám và cờ lá, nhưng trái còn núi sáng, nhiều thông; đầu cán cờ sát mép. Lượt 2 yêu cầu sương bóng thông tối che cảnh bên trái, toàn bộ cán cờ nằm trong khung; bỏ rồng phun lửa để boss làm điểm nhìn chính. Chọn lượt 2. |
| Mộc Tinh | `typing-defense/art-src/portraits/moc-tinh.png`; `typing-defense/art-src/ui/title-epic/keyart.png` | Lượt 1 có mặt già, râu gỗ, quả cam và bàn tay lớn; trái còn mái nhà, nước và núi rõ. Lượt 2 yêu cầu sương giông teal tối che chi tiết trái, gom cảnh sáng về phải, giữ tán trong khung. Chọn lượt 2; tán vẫn rất sát mép trên. |
| Void Leviathan | `typing-survival/art-src/concepts/b-lightbearer-keyart.png`; `typing-survival/art-src/concepts/b-lightbearer-fight.png` | Một lượt. Giữ đầu thuôn khổng lồ, xúc tu kính đen nứt cam, hố đen và vòng trạm vỡ. Không đưa Lightbearer vào tiền cảnh để tránh tranh điểm nhấn. |

Các đường dẫn ở bảng tính từ `games/`. Đã xem trực tiếp sáu ảnh nguồn và `typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`; ảnh mốc chủ dự án dùng để so mức chợ, không phải ảnh ghép vào tranh.

## 3. Hậu kỳ theo ART_ACCEPTANCE §5

Cả năm ảnh sinh có khổ **1672 × 941**. Ba bản chọn chỉ đổi cỡ bằng ImageMagick 7, Lanczos:

```text
/opt/homebrew/bin/magick <bản-sinh> -filter Lanczos -resize 1600x900! <bản-chọn>
```

Tỉ lệ nguồn lệch 16:9 khoảng **0,053 %**; đổi cỡ trực tiếp rất nhẹ theo hai trục, không cắt mất phần vẽ. Không chỉnh sáng, gamma, màu, tách nền, xóa chi tiết, phủ hộp tối hoặc san phẳng nền. Vùng trái tối có sẵn trong tranh sinh. Không có ngưỡng số nào phải đạt bằng cách phá tranh.

Đã xem bản giao đầy đủ 1600 × 900, bản thu nhỏ đúng 480 × 270 và ba tờ **“Bản sinh | Bản hậu kỳ”**:

- [Moss Bannerman](../../games/dragon-hold/art-src/ui/boss/boss-moss-bannerman-before-after.jpg)
- [Mộc Tinh](../../games/typing-defense/art-src/ui/boss/boss-moc-tinh-before-after.jpg)
- [Void Leviathan](../../games/typing-survival/art-src/ui/boss/boss-void-leviathan-before-after.jpg)

Mỗi phía của tờ đối chiếu hiển thị tranh cùng cỡ 800 × 450; nhãn nằm ngoài tranh. Tờ tổng ghép ba hàng, mỗi tranh giao 480 × 270 cạnh ảnh mốc cao 270 px. Nhãn dùng Arial tại `/System/Library/Fonts/Supplemental/Arial.ttf`. Chữ chỉ có trên tờ kiểm; ba tranh giao không có chữ, số, logo, viền hoặc watermark. Lá vàng trên cờ là họa tiết nhận diện boss.

## 4. Kiểm bố cục và số đo

[185-metrics.json](../../games/typing-defense/art-src/_review/185-metrics.json) lưu số đo trên bản hậu kỳ. Chia trái `x=0..532`, phải `x=533..1599`, toàn chiều cao 900 px. Luma sRGB ở bảng là `0,2126R + 0,7152G + 0,0722B`, RGB chuẩn hóa 0–1; JSON còn có luminance tuyến tính sau giải mã sRGB. Không dùng số đo để sửa tranh.

| Boss | Luma TB trái | Luma TB phải | Độ lệch chuẩn trái | Độ lệch chuẩn phải | Tỉ lệ σ trái/phải |
|---|---|---|---|---|---|
| Moss Bannerman | 0,131868 | 0,391723 | 0,050635 | 0,231587 | **0,2186** |
| Mộc Tinh | 0,135389 | 0,473247 | 0,060660 | 0,239262 | **0,2535** |
| Void Leviathan | 0,080526 | 0,375361 | 0,057666 | 0,275290 | **0,2095** |

Cả ba vùng trái tối hơn và ít biến thiên hơn phần phải. Các khối boss và chi tiết nhận diện nằm trong hai phần ba phải: mặt nạ, tay giương cờ và thân Bannerman; mặt già, bàn tay và thân rễ Mộc Tinh; đầu thuôn và xúc tu Leviathan. Ở 480 × 270 vẫn nhận ra ba dáng này; không dựa vào chữ để nhận diện.

Vùng yên không hoàn toàn đồng màu: Bannerman còn vài mũi giáo nhỏ gần ranh giới dưới; Mộc Tinh còn bóng núi chìm trong sương; Leviathan còn sao và bụi vũ trụ, một số điểm sao đạt trắng. Vì vậy “tối và yên” không có nghĩa mọi pixel đều tối hoặc bảo đảm tương phản chữ tại mọi tọa độ. Đây là quan sát trên tranh, không phải kiểm bố trí chữ thật trong game; không xóa các điểm vẽ để làm đẹp số.

## 5. KA5 · Tự chấm trên bản hậu kỳ

M theo thang mức chợ §1.3, so với ảnh chủ dự án ở tờ tổng. Ba tranh có quy mô lớn, lớp gần/giữa/xa và trời hoặc không gian vũ trụ, ánh sáng có hướng, vật liệu hoàn thiện và điểm nhấn rõ. Chưa tự nhận mức 9: Bannerman còn hơi thiên về cảnh chiến thuật, Mộc Tinh có nhiều chi tiết rễ, Leviathan dùng cấu trúc đầu khá trừu tượng.

Q gồm năm tiêu chí 0–2 theo ART_ACCEPTANCE; đánh giá cả bản đầy đủ và cỡ thẻ 480 × 270, lấy đánh giá thận trọng hơn:

| Boss | Đúng đề | Đọc được | Hợp bộ | Hình khối | Dùng tiếp | Tổng Q |
|---|---|---|---|---|---|---|
| Moss Bannerman | 1,8 | 1,8 | 1,8 | 1,6 | 2,0 | **9,0** |
| Mộc Tinh | 1,8 | 1,8 | 1,8 | 1,6 | 2,0 | **9,0** |
| Void Leviathan | 1,8 | 1,9 | 1,9 | 1,5 | 2,0 | **9,1** |

Điểm còn thiếu: cờ Bannerman lặp biểu tượng lá hai lần thay vì một; một số lớp rêu/giáp nhập nhau ở cỡ nhỏ. Tán Mộc Tinh sát mép trên, bàn tay rễ có phối cảnh mạnh và các nhánh chân chồng nhau; cảm giác “mất tên” truyền bằng nét mặt, không có ký hiệu kể chuyện riêng. Đầu Leviathan bám ảnh nguồn nhưng không có hàm rõ; mắt cam nhập với đường nứt, nhiều xúc tu chồng nhau bên phải. Các điểm này chưa làm mất nhận diện hoặc vùng chữ. Đây là **tự chấm của Codex**, chưa có chấm nhận độc lập hoặc duyệt cuối của chủ dự án.

## 6. KA1 · MD5 và phạm vi

Trước tác vụ, cả ba thư mục `ui/boss/` chưa tồn tại. Đã băm MD5 mọi tệp trong từng thư mục đích và cả `_review/` dùng chung trước/sau:

- [185-ka1-before.json](../../games/typing-defense/art-src/_review/185-ka1-before.json)
- [185-ka1-after.json](../../games/typing-defense/art-src/_review/185-ka1-after.json)

**10.367 tệp có trước: 0 đổi, 0 mất.** Ba thư mục boss chỉ thêm lần lượt 10, 10 và 8 tệp. `_review/` có thêm tệp của các phiếu khác đang chạy; bản kê lưu chúng để phân biệt công việc đồng thời, không nhận là sản phẩm của phiếu 185. Tệp của phiếu này ở `_review/` chỉ mang tiền tố `185-`; bản kê sau không tự băm chính nó. Prompt bản chọn đã đối chiếu bằng byte với prompt lượt chọn; mọi ảnh trong ba thư mục boss đều có prompt cạnh nó.

| Bản chọn | MD5 |
|---|---|
| `boss-moss-bannerman.png` | `4d68843fad1c71e2c9da7eff9ece3795` |
| `boss-moc-tinh.png` | `d5c0f43b59216faa4f2b13dfaeae8e56` |
| `boss-void-leviathan.png` | `902682ded1d3f89b0a92972adb2d9cbb` |

## 7. Phần bỏ qua và chủ dự án cần xem

Không bỏ thiếu ảnh nào. Không sinh âm, gọi Tripo hoặc tích hợp thẻ boss vì ngoài phiếu. Không chạy Git, game, dev server, trình duyệt, build hoặc test; không sửa mã, ảnh nguồn, tài liệu khác hay Tu Tiên. Media giữ trong `art-src`, không đưa vào Git. Không chụp render nên không có khung chụp thô cần dọn.

Chủ dự án xem **185-sheet.jpg**, rồi mở bản giao đầy đủ và các tờ trước/sau để duyệt nét mặt Mộc Tinh, cờ hai lá của Bannerman và dáng đầu Leviathan. Bước đặt tên/câu giới thiệu bằng tiếng Anh thực hiện trong game ở phiếu tích hợp riêng.
