# Phiếu 098 · Lời Gọi · Năm ô Rice Field theo trạng thái

Ngày làm: 28/10/2026. Game: Lời Gọi, map meadow 1.

**Đã giao đủ năm ô, qua kiểm 2–5 và tự chấm KA5 từ 9 điểm ở cả 1024 px và 256 px.** Chưa có điểm duyệt lại của Claude; chưa chép vào public/.

## 1. Tài sản và prompt từng lượt

| Ô | Bản chọn | Prompt |
| --- | --- | --- |
| `rice-flooded` | [PNG chọn](../../games/typing-defense/art-src/scenery/meadow/rice/rice-flooded.png) | [Prompt chính xác](../../games/typing-defense/art-src/scenery/meadow/rice/rice-flooded.prompt.txt) |
| `rice-seedling` | [PNG chọn](../../games/typing-defense/art-src/scenery/meadow/rice/rice-seedling.png) | [Prompt chính xác](../../games/typing-defense/art-src/scenery/meadow/rice/rice-seedling.prompt.txt) |
| `rice-green` | [PNG chọn](../../games/typing-defense/art-src/scenery/meadow/rice/rice-green.png) | [Prompt chính xác](../../games/typing-defense/art-src/scenery/meadow/rice/rice-green.prompt.txt) |
| `rice-ripe` | [PNG chọn](../../games/typing-defense/art-src/scenery/meadow/rice/rice-ripe.png) | [Prompt chính xác](../../games/typing-defense/art-src/scenery/meadow/rice/rice-ripe.prompt.txt) |
| `rice-stubble` | [PNG chọn](../../games/typing-defense/art-src/scenery/meadow/rice/rice-stubble.png) | [Prompt chính xác](../../games/typing-defense/art-src/scenery/meadow/rice/rice-stubble.prompt.txt) |

Mỗi tên giữ đủ `.try1.png`, `.try1.prompt.txt`, `.png`, `.prompt.txt`: **20 file mới** trong rice/. Mỗi ảnh gọi **một lượt image_gen tích hợp**. Không có lượt 2–3. Ảnh thô do công cụ trả về là 1254 × 1254, được giữ nguyên byte; bản chọn là dẫn xuất chuẩn hóa 1024 × 1024. Prompt chọn trùng byte với prompt lượt 1. [Định dạng ảnh thô](../../games/typing-defense/art-src/_review/098/identify-raw.txt); [đầu vào tham chiếu từng lượt](../../games/typing-defense/art-src/_review/098/generation-inputs.json).

Giữ câu mở đầu phong cách của 095: “Bright hand-painted storybook fantasy art for a cozy tower-defense game set in a Vietnamese-inspired folk valley of rice terraces, bamboo villages, silver waterfalls and white limestone hills.” Tất cả prompt ghi nhìn thẳng từ trên, ô 4 × 4 m, ánh sáng phẳng, vệt cọ lớn, không viền mực, không chữ và “seamless tileable texture, edges wrap on all four sides”.

| Ảnh | Prompt lượt 1 và phần thiếu sau sinh | Sửa bằng công cụ | Prompt lượt sau |
| --- | --- | --- | --- |
| rice-green | Lúa xanh, đúng tám trục x = 64 + 128k; dùng grass-a của 095 làm tham chiếu nét vẽ. Thực tế sinh bảy hàng, mép chưa liền | Ghép thành tám hàng, căn pha; dịch hue về 100°, vá mép | Không sinh tiếp |
| rice-seedling | Mạ non thưa hơn green, nước bạc xanh giữa hàng, hue khoảng 95°; green thô làm tham chiếu. Thực tế bảy hàng và lá còn dài | Ghép tám hàng, hue 98°, căn pha sau xử lý, vá mép | Không sinh tiếp |
| rice-ripe | Giữ trục hàng green, lá vàng và bông hạt rủ lớn, hue 47°. Thực tế bảy hàng và mép lỗi | Ghép tám hàng, chỉnh hue nhẹ, căn pha, vá hẹp để giảm hạt chồng | Không sinh tiếp |
| rice-stubble | Giữ trục hàng green, gốc cắt và rạ xám nâu ít bão hòa. Thực tế bảy hàng, S = 0.511521 | Ghép tám hàng, hue 38°, chặn S từng pixel ở 0,30, căn pha và vá mép | Không sinh tiếp |
| rice-flooded | Bùn ngập nước, ánh trời bạc đều, chưa cấy; grass-a làm tham chiếu nét cọ. Mép chưa liền | Hạ L mục tiêu 0,55, chặn S 0,28, vá mép rộng | Không sinh tiếp |

Không sửa prompt sau khi gọi công cụ. Các lần v2–v4 của **script xử lý pixel** không phải lượt sinh ảnh mới. Nhận xét mắt ban đầu rằng green đủ tám hàng đã được sửa sau khi đo: **cả bốn ảnh thô có bảy hàng**.

## 2. Cách sửa và chạy lại

ImageMagick 7 thu Lanczos về 1024 × 1024, RGB sRGB 8 bit; Node tính bằng số thực và làm tròn khi xuất. Không cài gói, không dùng mạng ngoài image_gen.

Để sửa số hàng, lấy profile L trung bình theo cột; tìm thành phần chu kỳ trong dải 6–10 hàng và tâm sáng trong khoảng ±18 px, sau làm mượt profile 25 px. Bốn nguồn đều có chu kỳ cơ sở 1024/7 = 146,285714 px. Từng dải được lấy mẫu ngang tuyến tính về bước 128 px; chỉ số hàng nguồn là **0, 1, 2, 3, 4, 5, 6, 3**, nên hàng thứ tám dùng lại hàng thứ tư. Tâm đích danh định: **64, 192, 320, 448, 576, 704, 832, 960 px**. Pha cosin trong kênh đất, rộng 12 px mỗi phía mối ghép; không vẽ thêm cây. Phép ghép có mô típ lặp, đã trừ điểm và ghi ở mục 6.

Sau dịch pha dưới pixel theo thành phần 128 px, chỉnh HSV và vá liền mép theo cách **tuần tự X rồi Y của 093**. Với T là ảnh đầu vào từng trục, roll 512 px rồi lấy O = (1 − w)·roll(T) + w·T; w = 1 khi d ≤ a, bằng cosin giảm về 0 trong b px tiếp theo, với d là khoảng cách tới tâm ảnh. Trục Y dùng kết quả X, tránh đưa mép X lỗi trở lại.

| Nhóm | X: a / b | Y: a / b |
| --- | --- | --- |
| Bốn ô có cây | 4 / 16 px | 8 / 32 px |
| flooded | 24 / 96 px | 24 / 96 px |

Đo tương quan chéo profile của từng bản đã vá với green, rồi roll ngang nguyên pixel: seedling **+12**, green **0**, ripe **+1**, stubble **−3**. Seedling có hiệu chỉnh cặp −2 px trong số +12 này để cả sáu cặp đều trong 8 px. Các tâm đo theo luma có thể lệch vài pixel vì hình lá và màu nước; không khẳng định từng cụm cây trùng từng pixel.

[process-final.mjs](../../games/typing-defense/art-src/_review/098/process-final.mjs) là bản dùng để giao. [core.mjs](../../games/typing-defense/art-src/_review/098/core.mjs) chứa giải mã, đo màu, box-blur tuần hoàn và vá mép. Giữ các bản script cũ vì luật cấm ghi đè: process.mjs thất bại pha cặp; v2 đạt nhưng pha rộng gây lá chồng; v3 thu hẹp vùng pha nhưng một cặp còn lệch 9 px; v4 hiệu chỉnh seedling và đạt. Bản final dùng v4 cho cây và vá rộng hơn cho flooded.

Để **tính lại và so từng byte RGB, không ghi bất kỳ file nào**:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/098/process-final.mjs replay
```

Trên bản sao bộ đầu ra chưa có PNG chọn, chế độ finalize tạo tài sản; make-review.mjs tạo ảnh kiểm; audit-final.mjs đo lại và lập MD5. Tất cả dùng ghi độc quyền, từ chối ghi đè. Không chạy lại các chế độ ghi trên bộ đã tồn tại. setup.mjs lưu prompt chính xác và snapshot trước; ingest.mjs bảo toàn ảnh công cụ; write-report-v2.mjs sinh báo cáo này từ số đo.

## 3. KA1 và định dạng

Chạy **/sbin/md5 -r mọi file trong scenery/**, sắp theo đường dẫn, trước khi ghi prompt/ảnh và sau khi giao.

| Kiểm | Số đo |
| --- | ---: |
| File trước / sau | **172 / 192** |
| File cũ đổi / mất | **0 / 0** |
| File thêm | **20**, đúng năm bộ bốn file trong rice/ |
| Dòng nội dung bị bỏ trong diff | **0** |

[MD5 trước](../../games/typing-defense/art-src/_review/098/md5-before.txt); [MD5 sau](../../games/typing-defense/art-src/_review/098/md5-after-final.txt); [diff chỉ thêm](../../games/typing-defense/art-src/_review/098/md5-diff-final.txt); [đối chiếu đường dẫn](../../games/typing-defense/art-src/_review/098/md5-verification-final.json).

**Năm PNG chọn đều 1024 × 1024, sRGB, RGB ba kênh, 8 bit, không alpha.** [magick identify](../../games/typing-defense/art-src/_review/098/identify-final.txt). Audit giải mã lại PNG, xác nhận RGB đúng kết quả tính lại và prompt chọn đúng từng byte. [Số đo và cờ kiểm cuối](../../games/typing-defense/art-src/_review/098/metrics-decoded-final.json) có allPassed = true.

Hai bản audit trước được giữ để truy vết: audit.mjs đọc sai khoảng trắng của chuỗi kênh ImageMagick và cắt mất ký tự đầu đường dẫn MD5; audit-v2 sửa hai lỗi này nhưng áp thêm điều kiện FFT cực đại phải là 8, không có trong phiếu. audit-final bỏ điều kiện thừa đó, giữ đúng kiểm **tự tương quan** của phiếu, không thay ngưỡng nghiệm thu ảnh.

## 4. Mép liền, hàng lúa và pha

Đo RGB sRGB 0–1, không tuyến tính hóa; L = 0,2126R + 0,7152G + 0,0722B. E và I đúng trung bình hai trục của phiếu. C là sai khác trung bình cặp cột 511/512 và cặp hàng 511/512. “Trước” là ảnh thô đã thu về 1024; “sau” đo lại PNG giao.

| Ô | E/I trước | E sau | I sau | E/I sau ≤ 1,25 | C sau | C/I sau ≤ 1,25 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `rice-flooded` | 2.130505 | 0.007556014 | 0.007228739 | **1.045274** | 0.007556014 | **1.045274** |
| `rice-seedling` | 2.735538 | 0.010958169 | 0.014719968 | **0.744442** | 0.010958169 | **0.744442** |
| `rice-green` | 3.026275 | 0.012411285 | 0.018444586 | **0.672896** | 0.012411285 | **0.672896** |
| `rice-ripe` | 1.454745 | 0.032471592 | 0.034054151 | **0.953528** | 0.032471592 | **0.953528** |
| `rice-stubble` | 1.897791 | 0.015014241 | 0.025265625 | **0.594256** | 0.015014241 | **0.594256** |

Profile p(x) = mean_y L(x,y). Tự tương quan tuần hoàn chuẩn hóa A(d) = Σ(p(x)−mean p)(p(x+d)−mean p) / Σ(p(x)−mean p)². Tìm các cực đại địa phương trong d = 50…219 px và chọn cực đại cao nhất. Kết quả không bị giới hạn trước trong cửa sổ 124–132 px.

| Ô | Số hàng quan sát | Chu kỳ A(d) | A tại chu kỳ | A(64) để đối chiếu nửa chu kỳ | Pha Fourier tại 128 px |
| --- | ---: | ---: | ---: | ---: | ---: |
| `rice-seedling` | **8** | **128 px** | 0.604513 | 0.475825 | 64.200125 px |
| `rice-green` | **8** | **127 px** | 0.446525 | -0.651754 | 64.074889 px |
| `rice-ripe` | **8** | **128 px** | 0.317222 | -0.405658 | 64.928375 px |
| `rice-stubble` | **8** | **127 px** | 0.806949 | -0.860158 | 61.258063 px |

Seedling có sóng hài 64 px mạnh do cả lá và kênh nước sáng, nên đỉnh FFT mạnh nhất là tần số 16. **A(128) = 0,604513 vẫn cao hơn A(64) = 0,475825**; có tám hàng cây khi xem ảnh. Ghi rõ đặc điểm này để Claude kiểm, không dùng cực đại FFT thay cho phép tự tương quan mà phiếu yêu cầu.

Pha Fourier = vị trí cực đại của thành phần tần số 8, đơn vị px modulo 128. Độ lệch cặp lấy khoảng cách ngắn hơn trên vòng 128. Đo thêm dịch tương quan chéo toàn profile, tìm trên −64…64 px; ghi dấu theo thứ tự cặp.

| Cặp | Lệch pha Fourier ≤ 8 | Dịch tương quan chéo, trị tuyệt đối ≤ 8 |
| --- | ---: | ---: |
| `rice-seedling` ↔ `rice-green` | **0.125236 px** | **2 px** |
| `rice-seedling` ↔ `rice-ripe` | **0.728249 px** | **-7 px** |
| `rice-seedling` ↔ `rice-stubble` | **2.942062 px** | **-5 px** |
| `rice-green` ↔ `rice-ripe` | **0.853486 px** | **0 px** |
| `rice-green` ↔ `rice-stubble` | **2.816826 px** | **0 px** |
| `rice-ripe` ↔ `rice-stubble` | **3.670312 px** | **2 px** |

Lệch pha Fourier lớn nhất **3,670312 px**; trị tuyệt đối dịch tương quan chéo lớn nhất **7 px**. Chu kỳ **127–128 px**, đều trong **128 ± 4 px**.

## 5. Màu, độ rối và đốm lặp

Hue, S theo HSV, lấy trung vị toàn ô; L cũng lấy trung vị. Độ rối = mean |L − box5(L)|. Đốm lặp = p95 − p5 của box129(L), bộ lọc biên tuần hoàn. Phiếu 098 không đặt ngưỡng độ rối/đốm lặp; ghi số để duyệt, không tự gán thêm ngưỡng của phiếu 095.

| Ô | Hue trung vị | S trung vị | L trung vị | Độ rối | Đốm lặp | Kiểm màu |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `rice-flooded` | 38.181818° | 0.070423 | 0.552658 | 0.007052 | 0.042014 | Đạt |
| `rice-seedling` | 98.048780° | 0.605442 | 0.548293 | 0.015022 | 0.010234 | Đạt |
| `rice-green` | 100.000000° | 0.803797 | 0.526536 | 0.018944 | 0.048911 | Đạt |
| `rice-ripe` | 46.956522° | 0.813253 | 0.619031 | 0.035389 | 0.068691 | Đạt |
| `rice-stubble` | 38.048780° | 0.300000 | 0.483576 | 0.025998 | 0.035141 | Đạt |

Seedling/green trong 80–120°, ripe trong 40–55°, stubble trong 25–50° và S ≤ 0,35. Flooded S ≤ 0,30, L trong 0,45–0,65. Tất cả đạt.

## 6. Ảnh kiểm và KA5

Đã xem ảnh ở cỡ 1024 px, năm bản roll nửa ô, tờ lát và 256 px bằng trình xem ảnh tĩnh, không dùng trình duyệt.

- [098-states.jpg](../../games/typing-defense/art-src/_review/098-states.jpg), **2560 × 1056**: năm ô cạnh nhau đúng 512 px; dưới mỗi ô là lát 3 × 3 thu về 512 px.
- [098-swap.jpg](../../games/typing-defense/art-src/_review/098-swap.jpg), **2048 × 544**: tờ bốn khung cùng vị trí, seedling → green → ripe → stubble. Chọn phương án tờ bốn khung được phiếu cho phép, không tạo GIF.
- [098-256.jpg](../../games/typing-defense/art-src/_review/098-256.jpg), **1280 × 288**: năm ô đúng 256 px, thêm dải nhãn 32 px.
- Năm bản roll 1024 px: [rice-flooded](../../games/typing-defense/art-src/_review/098/rice-flooded.roll.jpg), [rice-seedling](../../games/typing-defense/art-src/_review/098/rice-seedling.roll.jpg), [rice-green](../../games/typing-defense/art-src/_review/098/rice-green.roll.jpg), [rice-ripe](../../games/typing-defense/art-src/_review/098/rice-ripe.roll.jpg), [rice-stubble](../../games/typing-defense/art-src/_review/098/rice-stubble.roll.jpg).

Chữ chỉ nằm ở dải nhãn JPG kiểm. PNG tài sản không có chữ, số, logo, khung hay viền. Không thấy đường nối cứng nổi bật khi xem roll và lát; vẫn nhận ra mô típ lặp của vệt bùn, bó lá và gốc rạ. Có vài cụm lá/bông pha mềm tại vùng ghép ngang; không khẳng định ảnh hoàn toàn không lộ thao tác ghép. Đổi trạng thái giữ được trục hàng, còn hình và mật độ cụm lá đổi theo trạng thái; tờ bốn khung không thay thế duyệt chuyển cảnh thực tế trong game.

KA5 theo thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Chỉ cho Dùng tiếp 2 sau khi mọi kiểm bắt buộc đạt.

| Ô | 1024 px: năm tiêu chí → tổng | 256 px: năm tiêu chí → tổng | Phần còn thiếu |
| --- | --- | --- | --- |
| `rice-flooded` | 2 / 2 / 1.5 / 2 / 2 → **9.5** | 2 / 2 / 1.5 / 2 / 2 → **9.5** | Nét nước bạc và bùn đọc rõ; mảng cọ nhỏ nhiều hơn nền cỏ 095, nhận ra mô típ bùn khi lát. |
| `rice-seedling` | 2 / 2 / 1.5 / 1.5 / 2 → **9** | 2 / 2 / 1.5 / 1.5 / 2 → **9** | Thưa hơn green và có nước giữa hàng; vài cụm lá còn dài và gợi dáng quạt nhìn hơi xiên, chưa thành toàn bộ cụm mạ nhỏ tách rời. |
| `rice-green` | 2 / 2 / 1.5 / 1.5 / 2 → **9** | 2 / 2 / 1.5 / 1.5 / 2 → **9** | Tám dải lúa xanh đọc rõ; màu bão hòa, cụm lá dạng quạt hơi đều và có đoạn lá pha mềm. |
| `rice-ripe` | 2 / 1.5 / 2 / 1.5 / 2 → **9** | 2 / 1.5 / 2 / 1.5 / 2 → **9** | Bông hạt vàng nhận ra; dày chi tiết nhất bộ, vài đầu hạt và lá chồng nhẹ trong vùng pha ngang. |
| `rice-stubble` | 2 / 2 / 2 / 1.5 / 2 → **9.5** | 2 / 2 / 2 / 1.5 / 2 → **9.5** | Gốc cắt xám nâu tách rõ khỏi lúa sống; một số bó rạ còn xòe như quạt và nhận ra cụm lặp. |

Mức: **Đạt theo tự chấm Codex**. [Điểm từng tiêu chí](../../games/typing-defense/art-src/_review/098/scores.json). Claude cần chấm lại từng ô ≥ 8 trước khi nhận. Các nhận xét về mạ còn dài, độ bão hòa, chi tiết bông và lá pha mềm là phần cần xem kỹ; số đo đạt không thay cho duyệt mỹ thuật.

## 7. Khác phiếu, bỏ qua và việc cần duyệt

Khác cách gợi ý: vẫn dùng green làm tham chiếu cho ba trạng thái, nhưng ảnh sinh đều thiếu một hàng nên **ghép/co dải hàng**, ngoài việc dời ngang. Có tái sử dụng một hàng nguồn; bản chọn không trùng byte PNG thô. Vá X–Y dùng hai độ rộng riêng cho cây để giảm lá chồng, giữ cách cosin tuần tự của 093. Bổ sung JPG 256 px và bản roll. Mọi script, JSON và ảnh thử xử lý nằm trong _review/098/; ảnh kiểm chính mang tiền tố 098-.

**Bỏ qua:** lượt sinh 2–3 vì sửa pixel đã đạt; tích hợp public/ vì Claude là người chấm lại và chép. Không chạy Git, dev server, trình duyệt, build hay test game. Không làm âm thanh, không sửa mã game/tài liệu khác, không đọc hoặc ghi vùng Tu Tiên. Không ghi ART_REPLACE_LATER.md vì ngoài phạm vi và điểm tự chấm đều từ 9. Không tạo frame chụp thô; các JPG dẫn xuất được báo cáo dẫn trực tiếp, nên không có bộ capture cần prune.

**Claude/chủ dự án cần xem:** tờ states và swap, kỹ nhất là dáng mạ, hạt lúa ở cỡ nhỏ, bó rạ và các đoạn pha mềm; xác nhận tự chấm ≥ 8 cho từng ô rồi Claude mới tích hợp.
