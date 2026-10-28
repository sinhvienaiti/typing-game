# Phiếu 095 · Lời Gọi · Sáu ô đất meadow cho map 1

Ngày thực hiện: 28/10/2026, Mac mini M4. Game: `games/typing-defense`, bộ `meadow`, map `w1-silverfall`.

**Kết quả: sáu bản chọn đạt toàn bộ kiểm số 2–6; KA5 tự chấm 9–9,5 điểm ở 1024 px và 9,5 điểm ở 256 px.** Mỗi ảnh dùng một lượt sinh bằng công cụ `image_gen` tích hợp, sau đó sửa màu, giảm mảng sáng tối và làm liền mép bằng công cụ. Chưa có điểm chấm lại của Claude; chưa chép vào `public/`.

## 1. Bàn giao

Thư mục mới: `games/typing-defense/art-src/scenery/meadow/ground/`.

| Ô | Bản chọn | Prompt chính xác của lượt chọn |
| --- | --- | --- |
| Cỏ chính | [grass-a.png](../../games/typing-defense/art-src/scenery/meadow/ground/grass-a.png) | [grass-a.prompt.txt](../../games/typing-defense/art-src/scenery/meadow/ground/grass-a.prompt.txt) |
| Cỏ ba lá | [grass-b-clover.png](../../games/typing-defense/art-src/scenery/meadow/ground/grass-b-clover.png) | [grass-b-clover.prompt.txt](../../games/typing-defense/art-src/scenery/meadow/ground/grass-b-clover.prompt.txt) |
| Đường đất | [dirt-road.png](../../games/typing-defense/art-src/scenery/meadow/ground/dirt-road.png) | [dirt-road.prompt.txt](../../games/typing-defense/art-src/scenery/meadow/ground/dirt-road.prompt.txt) |
| Đất chuyển tiếp | [trail-worn.png](../../games/typing-defense/art-src/scenery/meadow/ground/trail-worn.png) | [trail-worn.prompt.txt](../../games/typing-defense/art-src/scenery/meadow/ground/trail-worn.prompt.txt) |
| Bờ suối | [stream-bank.png](../../games/typing-defense/art-src/scenery/meadow/ground/stream-bank.png) | [stream-bank.prompt.txt](../../games/typing-defense/art-src/scenery/meadow/ground/stream-bank.prompt.txt) |
| Sân đá | [stone-yard.png](../../games/typing-defense/art-src/scenery/meadow/ground/stone-yard.png) | [stone-yard.prompt.txt](../../games/typing-defense/art-src/scenery/meadow/ground/stone-yard.prompt.txt) |

Mỗi tên còn có **`<tên>.try1.png` và `<tên>.try1.prompt.txt`**, giữ nguyên đầu ra sinh và prompt. Tổng cộng 24 file mới trong `ground/`: 12 PNG, 12 TXT. Không có lượt 2 hoặc 3 vì bản sửa từ lượt 1 đã đạt. Bản chọn PNG là dẫn xuất đã chuẩn hóa của `.try1.png`, không phải bản sao byte ảnh thô; prompt bản chọn trùng byte với prompt lượt 1.

## 2. Prompt và xử lý từng ảnh

Đã đọc prompt `tall-grass-v1`, mở ảnh màu `layer-140-a.png` và bảng `sheet-keyframes.jpg`. Giữ nguyên câu đầu về phong cách nhà:

> Bright hand-painted storybook fantasy art for a cozy tower-defense game set in a Vietnamese-inspired folk valley of rice terraces, bamboo villages, silver waterfalls and white limestone hills.

Các prompt viết bằng tiếng Anh, đều có đúng câu **“seamless tileable texture, edges wrap on all four sides”**, bảng màu nhà, ô 8 × 8 m, nhìn thẳng từ trên xuống, bề mặt phẳng, ánh sáng đều, vệt cọ lớn và không viền mực. Không đưa nền magenta, vật đứng hay góc nhìn billboard của cây cảnh vào prompt ô đất.

| Ảnh | Lượt 1: nội dung riêng của prompt | Phần thiếu sau sinh; cách sửa miễn phí | Sửa prompt lượt sau |
| --- | --- | --- | --- |
| `grass-a` | Cỏ xanh mạ ấm, mảng cọ rộng, chênh sáng tối rất nhẹ | Hue 78,26°, sáng hơn mục tiêu và mép chưa liền; dịch hue +15,739°, cân L, giảm mảng và sửa mép | Không sinh tiếp |
| `grass-b-clover` | Cùng nền cỏ, cụm ba lá 30–60 cm, sáu đốm hoa trắng lớn, khoảng cỏ trống rộng | Hue 74,69° ngoài ngưỡng, L cao hơn cỏ A; dịch hue +19,306°, cân về cùng L và sửa mép | Không sinh tiếp |
| `dirt-road` | Đất nện vàng nâu, hai vệt bánh xe dọc mờ, sỏi thành mảng | L hơi cao và mép chưa liền; hạ L, giảm tương phản và sửa mép | Không sinh tiếp |
| `trail-worn` | Đất nén xen cỏ thưa, vật liệu chuyển tiếp phủ toàn ô | Mép chưa liền; cân L nhẹ, giảm mảng và sửa mép | Không sinh tiếp |
| `stream-bank` | Bùn ướt nâu xám ấm, cuội tròn nằm sát mặt đất | Bùn quá tối so với bộ; nâng L, giảm tương phản và sửa mép | Không sinh tiếp |
| `stone-yard` | Đá ong nhạt xen đá vôi, viên lớn không đều, mạch vữa mờ | Đốm thấp tần 0,106925 vượt 0,10, mép chưa liền; giảm mảng, hạ L và sửa mép | Không sinh tiếp |

**Chuỗi xử lý:** ImageMagick 7 thu Lanczos về 1024 × 1024, sRGB 8 bit RGB; Node tính màu bằng số thực; chỉ làm tròn khi tạo RGB cuối. Giữ ảnh thô trong `.try1.png`.

Sau dịch hue của hai ô cỏ, gọi `L₀` là luma, `B = box129(L₀)` tuần hoàn và `m = median(L₀)`. Cân độ sáng theo `T = m + c·(L₀ − B) + g·(B − m)`, rồi cộng một độ lệch để trung vị T đạt mục tiêu. Cộng cùng lượng thay đổi luma vào R/G/B, chặn về 0–255. Phương pháp giảm mảng chậm mà vẫn giữ nét cọ và màu vật liệu.

| Ảnh | L mục tiêu trước vá mép | c, tương phản chi tiết | g, mảng thấp tần |
| --- | ---: | ---: | ---: |
| `grass-a` | 0,56 | 0,84 | 0,40 |
| `grass-b-clover` | 0,56 | 0,84 | 0,40 |
| `dirt-road` | 0,69 | 0,88 | 0,68 |
| `trail-worn` | 0,61 | 0,86 | 0,60 |
| `stream-bank` | 0,50 | 0,80 | 0,65 |
| `stone-yard` | 0,73 | 0,88 | 0,65 |

Làm liền theo cách **tuần tự X rồi Y của phiếu 093**, dịch vòng nửa ô 512 px, mặt nạ cosin `a = 24`, `b = 96`. Mỗi nhánh giữ dải tâm 49 px, chuyển tiếp 96 px mỗi phía và về 0 từ khoảng cách 120 px. Với `X`, `Y` là dịch vòng từng trục:

```text
S = (1 − wx) · X(T) + wx · T
O = (1 − wy) · Y(S) + wy · S
```

Cách này không đưa mép X lỗi trở lại qua nhánh Y. Không dùng ghép chữ thập một bước. Các tham số và số trước/sau lưu trong [metrics-finalize.json](../../games/typing-defense/art-src/_review/095/metrics-finalize.json).

## 3. KA1 và định dạng

Chạy `/sbin/md5 -r` **mọi file trong `games/typing-defense/art-src/scenery/`**, sắp theo đường dẫn, trước khi ghi prompt/ảnh và sau khi ghi đủ tài sản.

| Số đo | Kết quả |
| --- | ---: |
| File trước | 120 |
| File sau | 144 |
| File cũ đổi nội dung | **0** |
| File cũ mất | **0** |
| File thêm | **24**, đúng các tên được phép trong `meadow/ground/` |
| Dòng nội dung bị bỏ trong `diff -U 0` | **0** |

`diff` chỉ có dòng nội dung thêm; không tính hai dòng tiêu đề tệp của công cụ. Bằng chứng: [md5 trước](../../games/typing-defense/art-src/_review/095/md5-before.txt), [md5 sau](../../games/typing-defense/art-src/_review/095/md5-after.txt), [diff](../../games/typing-defense/art-src/_review/095/md5-diff.txt), [đối chiếu](../../games/typing-defense/art-src/_review/095/md5-verification.json).

**Cả sáu PNG chọn: 1024 × 1024, sRGB, RGB ba kênh, 8 bit, không alpha.** [identify.txt](../../games/typing-defense/art-src/_review/095/identify.txt) ghi đầu ra `magick identify` từng ảnh. Giải mã lại sáu PNG trùng từng byte RGB với kết quả tính lại bằng script; prompt chọn trùng sáu prompt `.try1`.

## 4. Mép liền và chữ thập

Đo trên RGB sRGB 0–1, `L = 0,2126R + 0,7152G + 0,0722B`; không tuyến tính hóa sRGB. `E` và `I` lấy trung bình hai trục đúng định nghĩa phiếu. **“Trước” là ảnh lượt 1 đã thu Lanczos về 1024, chưa sửa màu hoặc vá mép. “Sau” là PNG giao được giải mã lại.**

| Ảnh | E trước | I trước | E/I trước | E sau | I sau | E/I sau ≤ 1,25 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `grass-a` | 0,014748081 | 0,007631361 | 1,932562 | 0,006498717 | 0,006014209 | **1,080561** |
| `grass-b-clover` | 0,024961723 | 0,014393874 | 1,734191 | 0,010622969 | 0,011553955 | **0,919423** |
| `dirt-road` | 0,030262230 | 0,012165644 | 2,487516 | 0,010984733 | 0,010176378 | **1,079434** |
| `trail-worn` | 0,030961395 | 0,017127741 | 1,807675 | 0,015408042 | 0,014175622 | **1,086939** |
| `stream-bank` | 0,024188027 | 0,013100326 | 1,846368 | 0,010531019 | 0,010053257 | **1,047523** |
| `stone-yard` | 0,029002932 | 0,020363449 | 1,424264 | 0,019233318 | 0,017317052 | **1,110658** |

Chữ thập: `C` là trung bình sai khác cột 511/512 và hàng 511/512. Trước vá, tính trên ảnh nguồn đã roll +512+512: `C = E_nguồn`, `I_roll = I_nguồn + (E_nguồn − C_nguồn)/1023`.

| Ảnh | C trước vá | I trước vá | C/I trước vá | C sau | C/I sau ≤ 1,25 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `grass-a` | 0,014748081 | 0,007638039 | 1,930873 | 0,006498717 | **1,080561** |
| `grass-b-clover` | 0,024961723 | 0,014405730 | 1,732763 | 0,010622969 | **0,919423** |
| `dirt-road` | 0,030262230 | 0,012182525 | 2,484069 | 0,010984733 | **1,079434** |
| `trail-worn` | 0,030961395 | 0,017139489 | 1,806436 | 0,015408042 | **1,086939** |
| `stream-bank` | 0,024188027 | 0,013110773 | 1,844897 | 0,010531019 | **1,047523** |
| `stone-yard` | 0,029002932 | 0,020370055 | 1,423802 | 0,019233318 | **1,110658** |

I sau của chữ thập là I sau ở bảng trên. Với phép vá này, C sau bằng E sau vì lấy cùng cặp pixel nội bộ nguồn tại tâm theo hai trục. Cả sáu qua kiểm mép và chữ thập. Số từng trục có trong JSON, không thay ngưỡng trung bình của phiếu bằng ngưỡng khác.

## 5. Độ rối, đốm lặp và màu

Độ rối = trung bình `|L − box5(L)|`; đốm lặp = `p95 − p5` trên `box129(L)`. Hai bộ lọc đều tuần hoàn, phân vị nội suy tuyến tính. Hue và S theo HSV; hue, S, L trong bảng là trung vị trên toàn ô.

| Ảnh | Độ rối trước → sau | Ngưỡng | Đốm trước → sau | Ngưỡng | Hue sau | L sau | S sau | Pixel tím cấm |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| `grass-a` | 0,007292 → **0,005690** | 0,030 | 0,038869 → **0,020028** | 0,08 | **94,029851°** | **0,560325** | 0,800000 | **0 / 0%** |
| `grass-b-clover` | 0,014230 → **0,011338** | 0,030 | 0,032846 → **0,022138** | 0,08 | **93,750000°** | **0,560561** | 0,838150 | **0 / 0%** |
| `dirt-road` | 0,011409 → **0,009506** | 0,040 | 0,059334 → **0,042858** | 0,10 | 37,254902° | **0,692696** | 0,626728 | **0 / 0%** |
| `trail-worn` | 0,015974 → **0,013173** | 0,040 | 0,054567 → **0,034785** | 0,10 | 43,361345° | 0,611536 | 0,620321 | **0 / 0%** |
| `stream-bank` | 0,012545 → **0,009565** | 0,040 | 0,049129 → **0,032902** | 0,10 | 31,914894° | **0,500909** | 0,274648 | **0 / 0%** |
| `stone-yard` | 0,018870 → **0,016028** | 0,040 | 0,106925 → **0,067736** | 0,10 | 33,658537° | **0,726425** | **0,194444** | **0 / 0%** |

| Quan hệ bắt buộc | Số đo sau | Kết quả |
| --- | ---: | --- |
| Hai hue cỏ trong 75–110° | 94,029851° / 93,750000° | Đạt |
| Hai cỏ lệch hue ≤ 8° | **0,279851°** | Đạt |
| Hai cỏ lệch L ≤ 0,05 | **0,000236** | Đạt |
| L đường − L cỏ A ≥ 0,08 | **0,132371** | Đạt |
| L sân − L cỏ A ≥ 0,10 | **0,166100** | Đạt |
| S sân ≤ 0,30 | **0,194444** | Đạt |
| L đường − L bờ suối ≥ 0,05 | **0,191787** | Đạt |
| Hue 285–330°, S > 0,5 | **0 pixel ở cả sáu ô** | Đạt |

Bằng chứng đo lại từ PNG giao: [metrics-decoded.json](../../games/typing-defense/art-src/_review/095/metrics-decoded.json). Ngưỡng đốm lặp đạt không có nghĩa là không nhận ra mô típ lặp; quan sát bên dưới ghi riêng điều này.

## 6. Ảnh kiểm và quan sát

Đã mở sáu PNG chọn và sáu bản roll ở **1024 px**, hai bảng kiểm, mock **2048 × 1152** và bản thu **1280 × 720**, cùng bảng **256 px**, bằng trình xem ảnh, không dùng trình duyệt.

- [095-tiles.jpg](../../games/typing-defense/art-src/_review/095-tiles.jpg), **3072 × 1056**: sáu cột đúng thứ tự tên; mỗi cột gồm nhãn 32 px, một ô 512 × 512, rồi lát 3 × 3 thu về 512 × 512. Chữ chỉ nằm trong ảnh kiểm, không nằm trong PNG tài sản.
- [095-mock.jpg](../../games/typing-defense/art-src/_review/095-mock.jpg), **1280 × 720**: nền cỏ A, hai vùng cỏ ba lá, đường đất viền đất chuyển tiếp, suối viền bùn cuội và sân đá. [mock-full.jpg](../../games/typing-defense/art-src/_review/095/mock-full.jpg) giữ bản **2048 × 1152**.
- [095-256.jpg](../../games/typing-defense/art-src/_review/095-256.jpg), **1536 × 284**: mỗi ô đúng 256 × 256, nhãn 28 px.
- Sáu bản dịch nửa ô: [cỏ A](../../games/typing-defense/art-src/_review/095/grass-a.roll.jpg), [cỏ ba lá](../../games/typing-defense/art-src/_review/095/grass-b-clover.roll.jpg), [đường](../../games/typing-defense/art-src/_review/095/dirt-road.roll.jpg), [chuyển tiếp](../../games/typing-defense/art-src/_review/095/trail-worn.roll.jpg), [bờ suối](../../games/typing-defense/art-src/_review/095/stream-bank.roll.jpg), [sân](../../games/typing-defense/art-src/_review/095/stone-yard.roll.jpg).

Mock dùng mặt nạ mềm smoothstep vẽ bằng script, một ô lặp mỗi 512 px trên bản đầy đủ. Màu nước river silver là lớp màu do script vẽ trong JPG minh họa, không phải ô đất thứ bảy. Đây là bản ghép phẳng thử màu và khoảng nhìn; không phải ảnh render camera 3D đã được tích hợp.

| Ô | Cỡ đầy đủ, roll và lát 3 × 3 | Cỡ 256 px / mock |
| --- | --- | --- |
| `grass-a` | **Không thấy đường nối cứng** ở biên hoặc chữ thập. Khi nhìn có chủ ý bảng lát, nhận ra nhịp cụm cọ xanh sáng/tối lặp theo ô | Nền đọc yên, màu xanh còn bão hòa mạnh; không thấy lưới mép ô |
| `grass-b-clover` | **Không thấy đường nối cứng**. Hoa trắng và cụm ba lá là dấu lặp rõ nhất ở hàng dưới bảng lát; nét cỏ nhiều hơn A | Hoa còn đọc được; trộn vào A không tạo bước đổi sáng toàn vùng, vẫn thấy khác mật độ cỏ và hoa |
| `dirt-road` | **Không thấy đường nối cứng**; hai vệt bánh xe vẫn dọc ảnh, hơi ngắt/mềm ở vùng pha giữa. Lát ngang 3 ô tạo nhịp các vệt song song | Đường sáng hơn cỏ và đọc rõ làn; nhịp vệt vẫn nhận ra khi phủ cả bảng |
| `trail-worn` | **Không thấy đường nối cứng**. Cụm cỏ vàng xanh lặp nhẹ khi soi bảng lát | Hợp dải chuyển giữa đường và cỏ; một số nét nhỏ hòa vào nền khi thu |
| `stream-bank` | **Không thấy đường nối cứng**. Nhận ra cụm cuội lớn lặp theo ô; có sỏi nhỏ và sắc độ gợi khối nhẹ | Dải bờ tối hơn đường, tách được nước; chi tiết sỏi nhỏ giảm rõ ở khoảng nhìn thử |
| `stone-yard` | **Không thấy đường nối cứng**. Có vài mạch đá mờ chồng trong vùng pha x/y khoảng 392–632 px; nhóm viên đá ấm/xám lặp ở bảng lát | Sân đọc sáng, ít bão hòa; vết chồng mờ ít nổi hơn, vẫn cần Claude xem ở ảnh gốc |

Vì còn những mô típ nêu trên, **không khẳng định “không thấy lặp”**. Các số đo đạt và các phần thiếu đã trừ vào KA5; không dùng kết quả số thay cho quan sát.

## 7. KA5 tự chấm

Theo năm tiêu chí của `ART_ACCEPTANCE.md`: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Với ô đất, hình khối đánh giá mặt phẳng, góc nhìn và cấu trúc mảng. Chỉ cho Dùng tiếp **2** sau khi mọi kiểm bắt buộc 2–6 đạt.

| Ảnh | 1024 px: năm tiêu chí → tổng | 256 px: năm tiêu chí → tổng | Mức và điểm còn thiếu |
| --- | --- | --- | --- |
| `grass-a` | 2 / 2 / 1,5 / 2 / 2 → **9,5** | 2 / 2 / 1,5 / 2 / 2 → **9,5** | **Đạt**; xanh bão hòa khá mạnh so với một số mảng nền tham chiếu |
| `grass-b-clover` | 2 / 1,5 / 1,5 / 2 / 2 → **9** | 2 / 2 / 1,5 / 2 / 2 → **9,5** | **Đạt**; nhiều nét cỏ hơn A, hoa làm dấu lặp dễ nhận |
| `dirt-road` | 2 / 1,5 / 2 / 2 / 2 → **9,5** | 2 / 1,5 / 2 / 2 / 2 → **9,5** | **Đạt**; nhịp vệt bánh xe rõ khi lát ngang nhiều ô |
| `trail-worn` | 2 / 1,5 / 2 / 2 / 2 → **9,5** | 2 / 1,5 / 2 / 2 / 2 → **9,5** | **Đạt**; một số nét cỏ nhỏ hơn mảng cọ mong muốn |
| `stream-bank` | 2 / 1,5 / 2 / 1,5 / 2 → **9** | 2 / 2 / 2 / 1,5 / 2 → **9,5** | **Đạt**; sỏi nhỏ và sắc độ gợi khối nhẹ, cụm cuội có dấu lặp |
| `stone-yard` | 2 / 2 / 2 / 1,5 / 2 → **9,5** | 2 / 2 / 2 / 1,5 / 2 → **9,5** | **Đạt**; vài mạch đá mềm/chồng do vá mép |

Đây là **tự chấm của Codex**; Claude cần chấm lại từng ô **≥ 8** trước khi tích hợp. Không sửa `ART_REPLACE_LATER.md` vì ngoài đường dẫn được phép; không có ảnh tự chấm 8–8,5 cần ghi bổ sung trong phiên này.

## 8. Script, chạy lại và khác biệt so với phiếu

Script trong [thư mục 095](../../games/typing-defense/art-src/_review/095/):

- `setup.mjs`: sáu prompt chính xác, danh sách tên, snapshot bằng `md5 -r`; `init` chỉ chạy trên thư mục chưa có đầu ra.
- `ingest.mjs`: sao chép đầu ra của công cụ tạo ảnh sang `.try1.png`, từ chối ghi đè.
- `process.mjs`: Lanczos, sửa màu, làm liền, đo số, xuất bản thử/chọn và tính lại để đối chiếu. Tham số cố định cho cả sáu ô.
- `make-review.mjs`: hai bảng kích thước, sáu bản roll và mock với mặt nạ mềm; font `/System/Library/Fonts/Supplemental/Arial.ttf`.
- `audit-v2.mjs`: đo lại PNG giao, kiểm định dạng, prompt và RGB, tạo mốc md5 sau cùng và diff. Giữ `audit.mjs` bản đầu vì luật không ghi đè; bản đầu dừng trước khi ghi kết quả do chỉ chờ `srgb`, trong khi ImageMagick 7 in thêm số kênh `3.0`. V2 nhận đúng định dạng ba kênh này.

Không cần NumPy/Pillow hay cài gói. Dùng Node, thư viện chuẩn và `/opt/homebrew/bin/magick`. Các tệp đầu ra đều ghi độc quyền hoặc dùng `COPYFILE_EXCL`.

Chuỗi xử lý đã dùng sau khi nhận sáu ảnh:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/095/process.mjs plan
node games/typing-defense/art-src/_review/095/process.mjs finalize
node games/typing-defense/art-src/_review/095/make-review.mjs
node games/typing-defense/art-src/_review/095/audit-v2.mjs
```

Không chạy lại các lệnh tạo đầu ra trên bộ đã tồn tại. Để **chạy lại phép tính, so từng byte RGB và không ghi file**:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/095/process.mjs replay
```

[metrics-plan.json](../../games/typing-defense/art-src/_review/095/metrics-plan.json) và sáu `<tên>.preview.jpg` trong thư mục 095 giữ bằng chứng xem bản xử lý trước khi xuất PNG; các preview có cùng RGB xử lý với bản chọn trước nén JPG.

**Khác biệt có chủ ý:** dùng vá tuần tự X–Y đã ghi ở 093 thay cho chữ thập một bước; các ô chọn được sửa bằng pixel nên không trùng byte ảnh thô lượt 1. Bổ sung bảng 256 px, sáu bản roll và mock đầy đủ để chấm. Không thay phạm vi tài sản, không tạo thêm loại đất. Phần nước chỉ có trong ảnh kiểm như đã giải thích.

**Bỏ qua:** lượt sinh 2–3 vì không cần; chưa tích hợp `public/` vì Claude là người duyệt và chép. Theo giới hạn phiếu, không chạy Git, dev server, trình duyệt, mạng ngoài `image_gen`, build/test game; không sửa mã game, tài liệu khác hoặc đọc/ghi vùng Tu Tiên. Không làm âm thanh. Ảnh kiểm là dẫn xuất tĩnh được báo cáo sử dụng, không phát sinh bộ frame chụp thô cần dọn.

**Claude/chủ dự án cần xem:** bảng lát và mock; kỹ nhất là hoa ba lá khi lặp, độ bão hòa hai ô cỏ, các cuội nhỏ và vùng mạch đá pha mềm. Sau điểm chấm lại ≥ 8 cho từng ô, Claude mới chép bản chọn vào `public/` theo quy trình tích hợp.
