# Báo cáo 109 · Tuyến Cuối / Last Line · Bốn ảnh minh họa ải

Ngày 29/10/2026, tại repo cha trên Mac mini M4, macOS.

**Đã hoàn thành phần tạo ảnh và kiểm của Codex:** bốn bản chọn tự chấm
**9–9,5/10**, qua mục Kiểm 1–5. Mỗi ảnh sinh **1 lượt**, tổng **4 lượt**,
bằng công cụ tích hợp `image_gen`; giữ nguyên cả bốn bản `.try1` và prompt.
**Chờ Claude chấm lại từ 8 để nhận**, rồi gắn vào thẻ ải và màn Hành trình.

## File bàn giao

Các đường dẫn dưới đây nằm trong `games/typing-survival/art-src/ui/stages/`.
Bốn PNG chọn đều **1536 × 864, sRGB, nền đặc**, không chữ hoặc HUD.

| Ải | Bản chọn | Prompt chính xác | Bản sinh giữ lại |
| --- | --- | --- | --- |
| 1 · Ca trực đầu | [c1-s1.png](../../games/typing-survival/art-src/ui/stages/c1-s1.png) | [c1-s1.prompt.txt](../../games/typing-survival/art-src/ui/stages/c1-s1.prompt.txt) | `c1-s1.try1.png`, `c1-s1.try1.prompt.txt` |
| 2 · Săn Pack Leader | [c1-s2.png](../../games/typing-survival/art-src/ui/stages/c1-s2.png) | [c1-s2.prompt.txt](../../games/typing-survival/art-src/ui/stages/c1-s2.prompt.txt) | `c1-s2.try1.png`, `c1-s2.try1.prompt.txt` |
| 3 · Vách nứt | [c1-s3.png](../../games/typing-survival/art-src/ui/stages/c1-s3.png) | [c1-s3.prompt.txt](../../games/typing-survival/art-src/ui/stages/c1-s3.prompt.txt) | `c1-s3.try1.png`, `c1-s3.try1.prompt.txt` |
| 4 · Khiên sáng | [c1-s4.png](../../games/typing-survival/art-src/ui/stages/c1-s4.png) | [c1-s4.prompt.txt](../../games/typing-survival/art-src/ui/stages/c1-s4.prompt.txt) | `c1-s4.try1.png`, `c1-s4.try1.prompt.txt` |

Tờ so theo tên phiếu: [109-sheet.jpg](../../games/typing-survival/art-src/_review/109-sheet.jpg),
**1984 × 1952**. Có bốn ảnh rộng 768 px, bản 384 × 216 và
`concept-fight.png` rộng 768 px bên cạnh. Bản này xếp hàng sát nhau nên
phần chân ảnh tham chiếu chạm hàng kế tiếp; giữ nguyên, bổ sung
[109-sheet-fullref.jpg](../../games/typing-survival/art-src/_review/109-sheet-fullref.jpg),
**1984 × 2304**, để xem trọn ảnh tham chiếu và nhãn riêng từng hàng.

Bằng chứng nằm trong
[`art-src/_review/109/`](../../games/typing-survival/art-src/_review/109/):
MD5 trước/sau và diff; số đo; lệnh cắt/co; script đo;
tám PNG thu 768/384; tờ bốn thumbnail và tờ tham chiếu sáu loại quái.

## Đối chiếu mã và mỹ thuật

Đã đọc `src/content/chapter-1.ts`, đối chiếu thêm `content/stage-rules.ts`
và `content/foes.ts`, không sửa mã.

| Ải | Mục tiêu trong mã | Cảnh bàn giao và khác biệt với bảng phiếu |
| --- | --- | --- |
| `c1-s1` | Trụ vững **150 giây = 2:30** | Swarm hình cầu gai đông đặc, vài Scout xanh, một Brute hổ phách đi sau; Pulse Gun xanh và Heat Beam cam cùng bắn. Khớp phiếu. |
| `c1-s2` | Hạ **3 Pack Leader**, giới hạn **240 giây** | Đúng ba Pack Leader gân vàng nhạt, mỗi con có một quầng sáng mảnh dưới chân. Đây là hình tổng hợp mục tiêu: mã cho các đợt Leader ở giây **20, 58, 96, 134, 172**, không quy định ba con xuất hiện đồng thời. |
| `c1-s3` | Trụ vững **165 giây = 2:45**; rift lần đầu giây **25**, chu kỳ **30 giây** | Theo mã, rift mở ở **vách bên**, tại khoảng **13–17 m**; ảnh dùng vách trái bị xé, vết nứt cam tím lan vào phía hành lang, Swarm chui ra. Không dùng một vết nứt chắn ngang toàn bộ hành lang như cách đọc sát bảng phiếu. |
| `c1-s4` | Trụ vững **165 giây = 2:45**; Shield Guard từ giây **20**, tỉ lệ pack **10%**; quy tắc học `missing` | Năm Shield Guard giơ khiên xanh, đạn vỡ trên mặt khiên; Swarm và Scout theo sau. **Bỏ Splitter theo mã:** `packs` của ải chỉ có `shield`, không có `splitter`; pack khiên có Swarm hộ tống. Không vẽ chữ để minh họa quy tắc thiếu chữ. |

Đã xem ảnh chủ dự án `owner-epic-2026-10-28.webp` để đối chiếu độ sâu,
ánh sáng và quy mô; xem `concept-fight.png`, `hull-left.png`,
`far-structures.png` và sáu chân dung quái của phiếu 089 để khóa chất liệu,
màu và dáng. Không dùng `title-horizon.png`.

Lượt đầu đưa `concept-fight.png` và tờ sáu quái vào `image_gen` làm tham
chiếu. Ba lượt sau thêm `c1-s1.try1.png` để giữ tàu, camera và hành lang
cùng bộ. Ảnh dùng khối thép than chì khô, sọc cam đen, LED xanh điện,
hố đen cam, chiều sâu giàn thép nhiều lớp; quái giữ dáng cầu gai/côn trùng
và gân năng lượng riêng. Không dùng ảnh chụp hoặc mặt sàn ướt.

## Kiểm 1 · KA1 MD5

Chạy `/sbin/md5 -r` cho từng file đệ quy trong `art-src/`, sắp theo đường
dẫn. Trước khi tạo ảnh: **230 file**. Snapshot sau: **264 file**, gồm
**230 file cũ giữ nguyên + 34 file mới**. **0 file cũ đổi MD5, 0 file bị mất**.

- [md5-before.txt](../../games/typing-survival/art-src/_review/109/md5-before.txt)
- [md5-after.txt](../../games/typing-survival/art-src/_review/109/md5-after.txt)
- [md5-diff.txt](../../games/typing-survival/art-src/_review/109/md5-diff.txt)
- [md5-check.json](../../games/typing-survival/art-src/_review/109/md5-check.json)

`diff -u` trả **1** vì có file thêm; mọi dòng nội dung thêm đều là file
mới, không có dòng nội dung bị xóa hoặc đổi. Mỗi snapshot liệt kê toàn bộ
file đang tồn tại ngay trước khi tạo chính nó, tránh tự băm chính file
manifest. Snapshot sau chưa chứa `md5-after.txt` và hai kết quả lập sau nó
(`md5-diff.txt`, `md5-check.json`). Tổng cộng tạo **37 file mới trong
art-src**, cộng báo cáo này ở ngoài `art-src`. Không ghi đè, đổi tên hay xóa
file nào; không xóa `.try1`.

## Kiểm 2 · Khổ và nền

Cả bốn bản sinh trả **1672 × 941**, không đúng khổ yêu cầu. Cắt giữa về
**1664 × 936** đúng 16:9, rồi co Lanczos về **1536 × 864**, giữ nguyên bản
sinh. Áp dụng riêng cho từng tên `c1-s1` đến `c1-s4`:

```sh
/opt/homebrew/bin/magick <tên>.try1.png \
  -gravity center -crop 1664x936+0+0 +repage \
  -filter Lanczos -resize 1536x864 -alpha off <tên>.png
```

Lệnh đầy đủ từng file ở
[normalize-commands.txt](../../games/typing-survival/art-src/_review/109/normalize-commands.txt).
`magick identify` xác nhận **4/4: 1536 × 864, sRGB, opaque=True**;
[identify.txt](../../games/typing-survival/art-src/_review/109/identify.txt).
Prompt bản chọn trùng từng byte với prompt `.try1`: **4/4**.

## Kiểm 3–4 · Cỡ nhỏ, chữ và HUD

Thu trực tiếp bản chọn bằng `-filter Lanczos -resize 384x`, xác nhận
**4/4 là 384 × 216**. Đã xem tờ thumbnail ở kích thước gốc và từng bản
chọn ở đầy đủ **1536 × 864**.

| Ảnh | Tách tàu và bầy ở 384 px | Vật riêng của ải ở 384 px | Không chữ, số, logo, HUD ở khổ đầy đủ |
| --- | --- | --- | --- |
| `c1-s1` | **Được** | **Được**: hai luồng xanh/cam, Brute lớn ở sau; Swarm xa gộp thành khối bầy | **Được** |
| `c1-s2` | **Được** | **Được**: đếm đủ **3** Leader và **3** quầng vàng | **Được** |
| `c1-s3` | **Được** | **Được**: mép nứt cam tím ở trái và bầy tràn ra | **Được** |
| `c1-s4` | **Được** | **Được**: nhận ra hàng **5** khiên xanh và điểm đạn bị chặn | **Được** |

Đây là kiểm bằng mắt, không phải kết quả OCR. Chữ nhãn chỉ có trên tờ
review, không nằm trong PNG bàn giao. Bằng chứng cỡ nhỏ:
[thumbnails-384.jpg](../../games/typing-survival/art-src/_review/109/thumbnails-384.jpg).

## Kiểm 5 · Cùng bộ

Đo trên **bản chọn đã lưu**, toàn bộ **1.327.104 pixel/ảnh**, không cắt ROI
hay loại pixel tối. Luma là trung bình `0,2126R + 0,7152G + 0,0722B` với
kênh sRGB chuẩn hóa 0–1. Hue là trung vị kênh H của HSL, cùng định nghĩa
hue với HSV, lượng tử 16 bit, đổi sang độ; gồm cả pixel ít bão hòa.
Các trung vị xa đường nối 0°/360°, dùng `max − min` để so cả bộ.

| Ảnh | Luma trung bình | Hue trung vị |
| --- | ---: | ---: |
| `c1-s1` | 0,183454 | 213,7478° |
| `c1-s2` | 0,196881 | 208,4193° |
| `c1-s3` | 0,199646 | 212,6683° |
| `c1-s4` | 0,195397 | 222,8556° |

**Chênh luma 0,016192 ≤ 0,06: đạt. Chênh hue 14,4363° ≤ 15°: đạt.**
Không cần chỉnh màu. Số cuối ở
[final-metrics.json](../../games/typing-survival/art-src/_review/109/final-metrics.json),
phép đo ở [verify.py](../../games/typing-survival/art-src/_review/109/verify.py).
`candidate-metrics.json` là số đo trước khi ghi PNG chọn 8 bit, chỉ giữ để
truy vết; bảng trên dùng số đo lại từ file bàn giao.

## Kiểm 7 · KA5 tự chấm

Theo năm tiêu chí 0–2 điểm của `ART_ACCEPTANCE.md` §1 và ngưỡng ảnh 2D
từ 8 của §2.2. Điểm dưới đây là **Codex tự chấm**, chưa phải điểm nhận
của Claude.

| Ảnh / cỡ xem | Đúng đề | Đọc được trong game | Hợp bộ | Hình khối | Dùng được cho bước sau | Tổng / mức |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `c1-s1` · 1536 | 1,5 | 2 | 2 | 1,5 | 2 | **9 · Đạt** |
| `c1-s1` · 384 | 1,5 | 1,5 | 2 | 2 | 2 | **9 · Đạt** |
| `c1-s2` · 1536 | 1,5 | 2 | 2 | 2 | 2 | **9,5 · Đạt** |
| `c1-s2` · 384 | 1,5 | 2 | 2 | 2 | 2 | **9,5 · Đạt** |
| `c1-s3` · 1536 | 1,5 | 2 | 1,5 | 2 | 2 | **9 · Đạt** |
| `c1-s3` · 384 | 1,5 | 2 | 1,5 | 2 | 2 | **9 · Đạt** |
| `c1-s4` · 1536 | 1,5 | 2 | 2 | 2 | 2 | **9,5 · Đạt** |
| `c1-s4` · 384 | 1,5 | 2 | 2 | 2 | 2 | **9,5 · Đạt** |

Điểm trừ cụ thể: tàu của cả bộ rộng khoảng **29% khung ngang**, lớn hơn
ý “tàu nhỏ” trong phiếu/prompt, dù nằm sát mép dưới và chiếm ít diện tích
so với toàn cảnh. Ải 1 có Brute lơ lửng khá cao, cảm giác trọng lượng chưa
bằng chân dung mẫu; ở 384 px các Swarm xa không còn tách từng con.
Ải 3 có mảng cam tím mạnh hơn ba ảnh kia, nhưng vẫn qua phép đo cùng bộ.
Không thấy lỗi chi thừa hoặc phối cảnh lớn ở các chủ thể chính.

Không sinh lượt 2–3 vì bốn ảnh đã tự chấm từ 8 và qua mục Kiểm 1–5.

## Việc bỏ qua và phần chủ/Claude cần xem

Không gắn ảnh vào game: phiếu giao việc đó cho Claude. Không sửa mã,
tài liệu khác, game khác hay Tu Tiên; không chạy Git, build, bộ test,
dev server hoặc trình duyệt. Không có công việc âm thanh trong phiếu.

Claude cần chấm lại cả bộ, nhất là kích thước tàu ở tiền cảnh, độ rõ của
ba Leader khi thu nhỏ, và điểm trừ màu của ảnh rift. Xin duyệt bản
`109-sheet-fullref.jpg` để so với ảnh sân đấu đầy đủ. Quyết định bỏ
Splitter ở ải 4 bám mã hiện tại, đã ghi rõ ở bảng đối chiếu; không tự thêm
quái chưa có trong ải.
