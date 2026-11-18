# Phiếu 124 · Dragonhold · Sáu ảnh nguồn mốc ải

**Ngày giao:** 29/10/2026. **Trạng thái:** đủ sáu bản chọn 1254 × 1254; cả sáu qua kiểm 2–6 bằng mặt nạ `-fuzz 18%` của phiếu 106, tự chấm M từ 8 và Q từ 9. Chờ Claude chấm lại. KA1 của phiên tiếp tục chỉ có tệp thêm; KA1 so với kiểm kê lịch sử có ba tệp vắng từ trước phiên, ghi riêng bên dưới, không tuyên bố lịch sử đạt.

## 1. Phạm vi và nguồn đã đọc

Đã đọc `ART_DIRECTION_2026-10-28.md` (thang M, bible Dragonhold), `ART_ACCEPTANCE.md` (đặc biệt §5), hai prompt `houses/herb-hut.prompt.txt`, `traps/spikes.prompt.txt` và mục tách nền của phiếu 106. Đã xem ảnh tham chiếu chủ dự án, tờ model `games/.wt-dh-mappilot/tmp/map-pilot-a2/sheets/kit3-models-sheet.jpg`, Moss Grunt và các tờ so của phiếu 119, 120.

Khi bắt đầu phiên này, `landmarks/` đã có chín PNG lượt sinh, chín prompt; `_review/124/` đã có baseline, prompt tổng, đường dẫn ảnh gốc từ thư mục `generated_images` của Codex, script và một ảnh tách nền. Tiếp tục từ các ảnh đó, không ghi đè hay tạo lại các lượt đã có. Hồ sơ công cụ sinh nằm ở [`generated-paths.json`](../../games/dragon-hold/art-src/_review/124/generated-paths.json); phiên tiếp tục không phát sinh lời gọi tạo ảnh mới. Không dùng API 3D, không gọi Tripo.

Chỉ thêm tệp tại các đường dẫn được phiếu cho phép. Không chạy Git, build, test suite, trình duyệt, dev server hoặc mạng; không đọc hay ghi các đường dẫn Tu Tiên. Không có âm thanh trong phạm vi phiếu.

## 2. Bản chọn và lịch sử prompt

MODEL và TAIL giữ nguyên văn. Bổ sung ở lượt 2 chỉ nằm trong phần riêng. Dòng nền nằm cuối prompt. Prompt bản chọn khớp byte với prompt lượt đã chọn.

| Vật | Lượt giữ | Nền | Cỡ thật khi dựng | Lượt 1 và phần sửa ở lượt 2 |
|---|---:|---|---|---|
| `hold-gate` | 1 | G · #00FF00 | Rộng 18 m, cao 16 m | Đúng cổng vòm tròn, song sắt nâng nửa, hai tháp vuông, đầu rồng đỡ mái và hai lò chưa đốt; giữ lượt 1. |
| `hold-wall` | 1 | G · #00FF00 | Dài 12 m, cao 10 m | Đúng tường thẳng, lối đi, hai trụ chống; đầu đoạn phẳng để nối; giữ lượt 1. |
| `watchtower` | 1 | G · #00FF00 | Cao 14 m | Đúng tháp tròn, lỗ châu mai, hành lang gỗ, mái đá phiến và chong chóng rồng; giữ lượt 1. |
| `dragon-statue` | 2 | M · #FF00FF | Cao 12 m cả bệ | Lượt 1 cúi đầu. Lượt 2 thêm cổ thẳng kiêu hãnh, cằm trên vai, mõm hướng trước và hơi ngẩng; cánh đá khép sát lưng và hông. |
| `ruined-arch` | 2 | M · #FF00FF | Cao 8 m | Lượt 1 vẫn nối trọn vòm. Lượt 2 chỉ còn mẩu vòm trên trụ trái; trụ phải gãy nửa chiều cao, khoảng nền trống tách hai phần; ngưỡng đá nối chân thành một vật. |
| `brazier` | 2 | G · #00FF00 | Cao 3 m cả bệ | Lượt 1 giá đỡ giống đầu rồng. Lượt 2 nhấn bốn bàn chân rồng bằng sắt, mỗi chân có ba móng lớn móc miệng chậu; cẳng có vảy nối bệ và chậu. |

Không vật nào quá hai lượt. Không sinh lượt 3 vì bản chọn đã đạt mức tự chấm và phép kiểm quy định; giữ nguyên cả chín `.try*.png` và chín `.try*.prompt.txt`.

Sáu PNG giao và sáu prompt nằm trong [`landmarks/`](../../games/dragon-hold/art-src/landmarks/): `hold-gate`, `hold-wall`, `watchtower`, `dragon-statue`, `ruined-arch`, `brazier`, cùng đuôi `.png` và `.prompt.txt`.

## 3. Hậu kỳ và phép đo

Chạy bằng Python chuẩn và ImageMagick 7, `ART_MAGICK=/opt/homebrew/bin/magick`; font tờ kiểm `/System/Library/Fonts/Supplemental/Arial.ttf`. Script mới: [`finalize.py`](../../games/dragon-hold/art-src/_review/124/finalize.py); các lệnh thật đã chạy được giữ trong [`finalization/commands.txt`](../../games/dragon-hold/art-src/_review/124/finalization/commands.txt).

Tách màu nền, cắt phần nền rỗng theo hộp bao, thu đồng tỉ lệ vào 1130 × 1090, thêm nền rỗng để ra 1254 × 1254. Không cắt giữa ảnh nguồn không vuông vì sẽ mất hai tháp hoặc ngọn tháp; đây là khác biệt có chủ đích để giữ trọn phần vẽ theo §5. Không sửa gamma, không chỉnh sáng, không phủ màu lên vật, không vẽ lại hay xóa chi tiết. Đáy đặt cách mép 84 px trước phép phân đoạn kiểm; lề trên rộng ở hai vật nằm ngang để bảo toàn tỉ lệ.

Chuỗi ImageMagick tạo khung (sau khi tách nền và trim):

```sh
magick <cutout> -filter Lanczos -resize 1130x1090   -gravity south -background none -extent 1254x1170   -gravity north -extent 1254x1254 <cutout-1254>
magick <cutout-1254> -background <màu-nền> -alpha remove -alpha off <bản-chọn>
```

Phép kiểm chính dùng đúng `-fuzz 18%` của phiếu 106; bước `-transparent` cùng màu chỉ tách thêm các lỗ nền kín trong song sắt hoặc dưới chậu. Không thay PNG giao. Áp một cách cho cả sáu vật, không chọn riêng phương pháp theo vật:

```sh
magick <bản-chọn> -alpha set -fuzz 18% -fill none   -draw 'color 0,0 floodfill' -transparent '<#00FF00 hoặc #FF00FF>'   -alpha extract -depth 8 gray:-
```

Script [`check-18pct.py`](../../games/dragon-hold/art-src/_review/124/check-18pct.py) đếm vật từ mặt nạ alpha > 127, hue theo HSV độ, thành phần liền theo tám hướng. Tất cả mặt nạ kiểm được giữ dưới `_review/124/*-mask-18pct.png`. Kết quả đầy đủ: [`metrics-18pct.json`](../../games/dragon-hold/art-src/_review/124/metrics-18pct.json).

Tất cả ảnh giao vuông **1254 × 1254**. Sai lệch RGB lớn nhất ở dải mép 10 px là **(0, 0, 0)** cho cả sáu; ngưỡng cho phép mỗi kênh 12. Không chữ, số, logo, chữ ký, cờ, biển hay khiên có hình hiệu; đầu rồng chạm đá và chong chóng là bộ phận đề bài yêu cầu, không phải huy hiệu.

| Vật | Cỡ nguồn bản chọn | Hộp bao x, y, rộng, cao (px) | Lề trái/phải/trên/dưới (px) | Vùng liền > 1% ảnh |
|---|---|---|---|---:|
| `hold-gate` | 1536 × 1024 | 62, 309, 1130, 860 | 62 / 62 / 309 / 85 | 1 |
| `hold-wall` | 1536 × 1024 | 63, 372, 1129, 798 | 63 / 62 / 372 / 84 | 1 |
| `watchtower` | 1024 × 1536 | 392, 81, 469, 1089 | 392 / 393 / 81 / 84 | 1 |
| `dragon-statue` | 1254 × 1254 | 299, 80, 655, 1090 | 299 / 300 / 80 / 84 | 1 |
| `ruined-arch` | 1312 × 1199 | 143, 80, 968, 1090 | 143 / 143 / 80 / 84 | 1 |
| `brazier` | 1222 × 1287 | 160, 80, 933, 1089 | 160 / 161 / 80 / 85 | 1 |

Lề trái/phải/trên thấp nhất 4,944%; đáy xa mép nhiều nhất 6,778%, đều qua ngưỡng 3% và 12%. Chân phẳng được kiểm bằng mắt ở ảnh đầy đủ: hai chân cổng cùng mặt đứng, chân tường cắt ngang, đáy tròn tháp và các bệ nằm phẳng; đá đổ của vòm dính vào ngưỡng đá. Số vùng liền chỉ kiểm trên ảnh, không thay cho kiểm topology sau khi dựng Tripo.

| Vật | Pixel vật | Pixel hue nền | Hue nền / vật (%) ≤ 0,5 | Màu tín hiệu / vật (%) ≤ 3 | Kiểm 2–6 |
|---|---:|---:|---:|---:|---|
| `hold-gate` | 635,506 | 2,109 | 0.33186 | 0.00378 | Đạt |
| `hold-wall` | 577,364 | 1,504 | 0.26049 | 0.00000 | Đạt |
| `watchtower` | 345,343 | 1,338 | 0.38744 | 0.02461 | Đạt |
| `dragon-statue` | 438,312 | 1,030 | 0.23499 | 0.00000 | Đạt |
| `ruined-arch` | 446,112 | 1,602 | 0.35910 | 0.02981 | Đạt |
| `brazier` | 759,797 | 2,288 | 0.30113 | 0.00000 | Đạt |

**Sai khác phép phân đoạn, giữ nguyên tranh:** script hậu kỳ ban đầu dùng điều kiện `max(|RGB − nền|) > 60` để ước lượng vật. Điều kiện này không tương đương khoảng cách màu `-fuzz 18%` của ImageMagick. Bộ đo ban đầu nằm ở [`finalization/metrics.json`](../../games/dragon-hold/art-src/_review/124/finalization/metrics.json): tháp 0,59779%, vòm 0,56364%, vượt 0,5%. Kiểm phụ cho thấy 2.026/2.069 pixel bị đếm ở tháp và 2.420/2.520 pixel ở vòm nằm sát nền trong bán kính một pixel. Dữ liệu chi tiết: [`edge-diagnostic.json`](../../games/dragon-hold/art-src/_review/124/edge-diagnostic.json).

Đã dừng chỉnh tranh, giữ nguyên PNG, đối chiếu bằng phép tách được phiếu dẫn và ghi cả hai kết quả. Không dùng xói mép hay tô đè để ép số. Nếu Claude yêu cầu điều kiện RGB > 60 làm chuẩn thay cho mặt nạ 18%, hai ảnh này vẫn **chưa đạt điều kiện đó**; không được diễn giải bảng trên thành đạt mọi cách phân đoạn. Script `finalize.py` giữ nguyên lần dừng kiểm ban đầu; dùng `check-18pct.py` để chạy lại phép kiểm chính.

## 4. Tờ kiểm và thang người lính

- [Tờ thang 124-scale.jpg](../../games/dragon-hold/art-src/_review/124-scale.jpg): 30 px/m, chung vạch chân; cổng 480 px, tường 300 px, tháp 420 px, tượng 360 px, vòm 240 px, lò 90 px; Moss Grunt 54 px tương ứng 1,8 m. Các tỉ số chiều cao lần lượt 8,89; 5,56; 7,78; 6,67; 4,44; 1,67 lần lính. Cổng, tháp và tượng làm lính nhỏ lại rõ. Chiều rộng mô hình thật cần đặt 18 m và 12 m khi dựng; tờ này kiểm chiều cao nhìn thấy của ảnh ba phần tư, không suy diễn hình học 3D từ phép chiếu.
- [Tờ so tham chiếu đã kiểm hàng vách đá](../../games/dragon-hold/art-src/_review/124-vs-ref-checked.jpg): tờ thang và ảnh tham chiếu đều cao 640 px, hàng dưới cắt đúng `cliff-rock-a` từ tờ model 2160 × 2880 bằng `-crop 2160x360+0+720`. **Đứng cạnh được** về quy mô, khối đá cổ, sắt rèn và độ hoàn thiện; nét vẽ khối chắc đi cùng kit cũ. Đây là đánh giá ảnh nguồn tách nền; không tự nhận đã có chất lượng cảnh game M=9 như tham chiếu.
- [Sáu ảnh ở 256 px](../../games/dragon-hold/art-src/_review/124-small.jpg).

Tờ `124-vs-ref.jpg` ban đầu cắt vào hàng rào nhưng nhãn ghi vách đá do giả định sai kích thước tờ model; giữ lại nguyên trạng theo luật không ghi đè. Dùng **124-vs-ref-checked.jpg** làm tờ đối chiếu nhận. Script bổ sung: [`compare-checked.py`](../../games/dragon-hold/art-src/_review/124/compare-checked.py).

Sáu tờ “bản sinh | bản hậu kỳ”, hai ô cùng cỡ 640 × 640, giữ toàn bộ vật:

- [hold-gate](../../games/dragon-hold/art-src/_review/124-hold-gate-before-after.jpg).
- [hold-wall](../../games/dragon-hold/art-src/_review/124-hold-wall-before-after.jpg).
- [watchtower](../../games/dragon-hold/art-src/_review/124-watchtower-before-after.jpg).
- [dragon-statue](../../games/dragon-hold/art-src/_review/124-dragon-statue-before-after.jpg).
- [ruined-arch](../../games/dragon-hold/art-src/_review/124-ruined-arch-before-after.jpg).
- [brazier](../../games/dragon-hold/art-src/_review/124-brazier-before-after.jpg).

## 5. KA5 · Tự chấm bản hậu kỳ

Đã xem trực tiếp cả sáu PNG giao ở 1254 px, tờ 256 px, tờ thang và ảnh tham chiếu. M chấm theo tiêu chuẩn ảnh nguồn của phiếu: dáng lớn, cổ, hùng, vật liệu hoàn thiện; không thêm trời hay ánh sáng điện ảnh vào ảnh nguồn vì trái TAIL. Q ghi theo thứ tự: đúng đề / đọc được / hợp bộ / hình khối / dùng tiếp; mỗi mục 0–2.

| Vật | M đầy đủ | Q đầy đủ (5 mục) | M ở 256 px | Q ở 256 px (5 mục) | Nhận xét trên bản giao |
|---|---:|---|---:|---|---|
| `hold-gate` | 8,5 | 2/2/2/2/2 = 10 | 8,5 | 2/2/2/2/2 = 10 | Khối tháp nặng, vòm lớn, đá cũ và đầu rồng rõ; cấu trúc cổng đọc ngay. |
| `hold-wall` | 8 | 2/2/2/2/2 = 10 | 8 | 2/2/2/2/2 = 10 | Tường chịu lực, lối đi và hai trụ rõ; đầu đoạn ít trang trí, hợp nối kit. |
| `watchtower` | 8 | 2/2/2/2/2 = 10 | 8 | 2/1/2/2/2 = 9 | Tỉ lệ đứng cao, gỗ/sắt/đá phân biệt; chong chóng nhỏ ở 256 px nên giảm một điểm đọc. |
| `dragon-statue` | 8,5 | 2/2/2/2/2 = 10 | 8,5 | 2/2/2/2/2 = 10 | Đầu ngẩng, ngực và cánh đá lớn, bệ chịu lực; rêu sẫm làm rõ tuổi đá. |
| `ruined-arch` | 8 | 2/2/2/2/2 = 10 | 8 | 2/2/2/2/2 = 10 | Vết gãy đọc rõ, khoảng trống lớn, thông mọc trong khe, đá chân gắn liền. |
| `brazier` | 8 | 2/2/2/2/2 = 10 | 8 | 2/2/2/2/2 = 10 | Bốn chân rồng ôm chậu rõ, sắt cũ và bệ đá chắc; không lửa, không hiệu ứng tín hiệu. |

M=8–8,5 vẫn cần Claude chấm độc lập theo quy định; bảng này là tự chấm, không thay nhận của Claude hoặc chủ dự án. Chưa kiểm chất lượng model, mặt sau, tam giác hay topology; sáu model do chủ dự án dựng Tripo thủ công sau duyệt.

## 6. KA1 · Bảo toàn tệp cũ

Đã chạy `md5 -r` đệ quy từng tệp `games/dragon-hold/art-src/` trước khi ghi trong phiên và sau khi giao ảnh. Script [`audit.py`](../../games/dragon-hold/art-src/_review/124/audit.py); xem [`md5-audit.json`](../../games/dragon-hold/art-src/_review/124/md5-audit.json).

| Mốc so | Số tệp trước | Số tệp sau | Thêm | Đổi hash | Vắng |
|---|---:|---:|---:|---:|---:|
| Baseline lịch sử `md5-before.txt` | 4.777 | 5.262 | 488 | 0 | 3 |
| Baseline phiên tiếp tục `md5-session-before.txt` | 5.180 | 5.262 | 82 | 0 | 0 |

[`md5-session-diff.txt`](../../games/dragon-hold/art-src/_review/124/md5-session-diff.txt) chỉ có dòng thêm. Baseline cũ được giữ nguyên; [`md5-diff.txt`](../../games/dragon-hold/art-src/_review/124/md5-diff.txt) có ba dòng mất thuộc:

```text
games/dragon-hold/art-src/_review/178/md5-before.json
games/dragon-hold/art-src/_review/178/md5-before.txt
games/dragon-hold/art-src/_review/178/sources.json
```

Ba tệp này **đã vắng trong baseline phiên tiếp tục**, trước mọi thao tác ghi của phiên. Không biết tác giả hay lý do thay đổi, không phục hồi và không chạm phiếu 178. Vì vậy KA1 lịch sử chưa đủ điều kiện “diff chỉ thêm”; KA1 của phiên tiếp tục đạt. Manifest sau không liệt kê chính nó và các tệp diff/kết luận sinh từ nó để tránh vòng tự băm. Báo cáo này nằm ngoài cây art-src.

## 7. Việc còn lại khi nhận

Claude xem sáu bản chọn ở cỡ đầy đủ và 256 px, chấm M/Q độc lập; xem rõ ghi chú hai cách xác định mép ở mục 3 và sai khác KA1 lịch sử ở mục 6. Không có ảnh bị bỏ; không cần thêm lượt sinh trong phiên này. Không sửa danh sách nâng ảnh hay tài liệu khác vì ngoài phạm vi được ghi.

Sau khi Claude nhận, chủ dự án dựng sáu model từ sáu PNG trong `landmarks/`, đặt kích thước theo bảng mục 2. Chưa gọi Tripo và chưa tích hợp vào game.
