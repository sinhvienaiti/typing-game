# Phiếu 100 · Lời Gọi · Decal nứt rễ báo trước và dải bọt thác

Ngày thực hiện: 29/10/2026, Mac mini M4. Game: **Wordwoven**, `games/typing-defense`, map `w1-silverfall`.

**Đã giao hai ảnh 1024², qua toàn bộ kiểm số của phiếu. KA5 tự chấm: nứt 9,5/10 ở cỡ đầy đủ, 9/10 ở ô 64 px; bọt 9/10 ở cả 1024 và 256 px.** Mỗi ảnh dùng một lượt sinh bằng `image_gen` tích hợp, sau đó hậu kỳ miễn phí. Chưa có điểm chấm lại của Claude; chưa chép vào `public/`.

## 1. Bàn giao

Thư mục: `games/typing-defense/art-src/vfx/`.

| Ảnh | Bản dùng để tích hợp | Bản nền khóa để kiểm | Prompt chính xác của lượt chọn |
| --- | --- | --- | --- |
| Nứt rễ báo trước | [root-crack-warn.alpha.png](../../games/typing-defense/art-src/vfx/root-crack-warn.alpha.png) | [root-crack-warn.png](../../games/typing-defense/art-src/vfx/root-crack-warn.png), nền `#FF00FF` | [root-crack-warn.prompt.txt](../../games/typing-defense/art-src/vfx/root-crack-warn.prompt.txt) |
| Bọt thác cuộn dọc | [waterfall-foam.alpha.png](../../games/typing-defense/art-src/vfx/waterfall-foam.alpha.png) | [waterfall-foam.png](../../games/typing-defense/art-src/vfx/waterfall-foam.png), nền đen | [waterfall-foam.prompt.txt](../../games/typing-defense/art-src/vfx/waterfall-foam.prompt.txt) |

Mỗi tên còn giữ nguyên **`.try1.png` và `.try1.prompt.txt`**. Tổng cộng **10 file mới** trong `vfx/`: sáu PNG, bốn TXT. Không có lượt 2 hoặc 3. Hai prompt chính trùng byte với prompt lượt 1, mở đầu nguyên văn hai đoạn đầu của `ma-troi-wisp.prompt.txt`.

Bản chọn `.png` là dẫn xuất đã hậu kỳ, không phải bản sao byte từ ảnh thô: công cụ sinh trả về 1254², nên giữ nguyên kích thước đó trong `.try1.png`; chuẩn hóa cả `.png` và `.alpha.png` về **1024 × 1024**, sRGB 8 bit. `.alpha.png` là RGBA thẳng; `.png` được ghép lại trên nền khóa tương ứng.

## 2. Brief, prompt và hậu kỳ

Chuẩn: [ART_ACCEPTANCE §2.2](../games/ART_ACCEPTANCE.md), [VFX_STANDARD §3.3 và §5.6](../games/VFX_STANDARD.md). Mẫu phong cách là hai đoạn đầu prompt `vfx/ma-troi-wisp.prompt.txt`, cùng bảng màu bạc–lam của `water-splash` và mực tím nâu của bộ VFX hiện có; giữ son cam làm tín hiệu nguy hiểm theo phiếu.

| Ảnh | Lượt 1: phần riêng của prompt | Thiếu sau sinh và cách sửa | Lượt sau |
| --- | --- | --- | --- |
| `root-crack-warn` | Nhìn thẳng từ trên xuống, nứt mực tím nâu, lõi son cam mảnh, lưới 4 × 4; cùng mạng nhánh lan dần ở khung 1–10, giữ hình và sáng hai nhịp ở 11–16. Ghi rõ đây là cảnh báo giữ cuối, thay quy tắc tan cuối chung của prompt mẫu. | Nguồn có nhánh xê dịch nhẹ, khung sau lan sát mép. Lấy nguyên hình sinh ở ô 10 làm mẫu chung, tách phông, thu đồng tỷ lệ, rồi mở mặt nạ bán kính tăng dần. Giữ nguyên hình khung 10–16, tăng sáng riêng lõi cam ở 11 và 14. Sau tăng sáng còn 34 pixel lọt dải hue cấm, đã hạ S của đúng các pixel ấy xuống 0,35. | Không sinh tiếp; lỗi sửa được bằng công cụ. |
| `waterfall-foam` | Một texture liên tục, ghi rõ thay bố cục flipbook chung bằng ảnh đơn; dải bọt bạc trắng, xanh xám, chảy dọc trên đen, nối đầu–cuối, không có hồ, đá hay cảnh vật. | Hai mép dọc chưa khớp. Hòa chồng 128 hàng đầu–cuối bằng cosin, giữ đoạn giữa, nội suy chu kỳ 896 hàng về 1024; đặt hai hàng biên bằng trung bình của chúng. Lấy alpha theo L và làm mờ hai mép ngang trong 41 cột mỗi bên. | Không sinh tiếp; lỗi sửa được bằng công cụ. |

**Vai trò VFX:** nứt là lớp decal của **pha A, quái/boss ra đòn**, dùng cho Rễ Trồi của Mộc Tinh. Phần R/T/I/F và ánh tụ tại người ra đòn thuộc làn tích hợp, không nằm trong hai ảnh phiếu này. Bọt thác là môi trường lặp, không phải đòn đánh. Không tuyên bố hai texture đã chứng minh đủ năm pha trong game.

**Kịch bản kiểm:** nứt 16 khung trên `scenery/meadow/ground/grass-a.png` đã giao ở [095](095-report.md), xem ở ô 256 và 64 px; bọt lát dọc 1 × 3 trên `#8a8f94`, xem ở bề rộng 1024 và 256 px. Không bloom, không trình duyệt. Ngưỡng nghiệm thu số là mục 2–3 của phiếu, ghi ở phần 3 dưới đây.

### Công thức và script

Script đã dùng, chỉ nằm trong thư mục được phép:

- [process.py](../../games/typing-defense/art-src/_review/100/process.py): tách phông, chuẩn hóa, diễn tiến nứt, nối bọt, ảnh kiểm v1 và đo v1.
- [finalize.py](../../games/typing-defense/art-src/_review/100/finalize.py): sửa 34 pixel sau tăng sáng, tạo bản giao, đọc lại PNG đã ghi để kiểm, ghép ảnh kiểm cuối, chụp MD5 sau giao.

Chạy từ repo cha, dùng Python chuẩn và `/opt/homebrew/bin/magick`; không cài thư viện hay dùng mạng. Đã đặt `ART_MAGICK=/opt/homebrew/bin/magick`. Script cố ý từ chối ghi đè đầu ra; muốn tái lập phải dùng bản sao sạch của đầu ra phiếu 100 và giữ các ảnh nguồn `.try1.*`.

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
python3 games/typing-defense/art-src/_review/100/process.py
python3 games/typing-defense/art-src/_review/100/finalize.py
```

Lần chạy `process.py` kết thúc bằng assertion báo còn pixel hue cấm; đó là kiểm v1 trước sửa, vẫn giữ nguyên hồ sơ. Sau đó `finalize.py` sửa lỗi này và kết thúc thành công với mọi kiểm bằng `true`. Không dùng `processed-v1/` để tích hợp. Trường phụ `crack_scale_side_px` trong `metrics-v1.json` bị biến vòng lặp ghi thành nhãn `right`; không dùng trường đó để nghiệm thu. Các kích thước, lề và bán kính cuối được tính lại trực tiếp từ PNG giao trong `metrics-final.json`.

Nứt: crop nguồn ô 10 tại `313x313+314+627`, key theo mức trội hồng, khử màu phông ở rìa trước nội suy. Thu hình quanh tâm về lề ít nhất 24 px. Mặt nạ lan theo khoảng cách tới `(127,5; 127,5)` của ô 256²; ở khung 1–10 bán kính tăng từ 18% tới 100% mẫu. Không tạo nhánh bằng mã. Ở 11–16 dùng cùng alpha với khung 10, hệ số sáng lõi lần lượt `1,55 / 1,15 / 1 / 1,55 / 1,15 / 1`; sau chặn RGB kiểm hue lại để không sinh sắc khóa mới.

Bọt: với RGB nguồn 0–1 sau nối dọc, đặt `L = 0,2126R + 0,7152G + 0,0722B`, `A = L × feather`. `feather = (1 − cos(πu)) / 2`, với `u = min(1, x/41, (1023−x)/41)`. RGB thẳng là `clamp(RGB/L)` khi alpha khác 0, còn pixel alpha 0 có RGB 0. Cách này chuyển ánh sáng trên đen thành RGBA thẳng theo hướng hai ảnh lặp của 043; alpha dùng **L**, đúng yêu cầu riêng của phiếu 100.

## 3. Kiểm số bắt buộc

Số cuối lấy từ [metrics-final.json](../../games/typing-defense/art-src/_review/100/metrics-final.json), tính trên PNG đã ghi, không chỉ trên mảng ảnh trước xuất. Cả hai `.png` là `1024 1024 srgb 3.0`; cả hai `.alpha.png` là `1024 1024 srgba 4.0`.

### KA1 · MD5

Đã chạy **`md5 -r` mọi file** trong `games/typing-defense/art-src/vfx/` trước lần ghi đầu tiên và sau khi giao ảnh:

| Kiểm | Kết quả |
| --- | ---: |
| Số file trước | 57 |
| Số file sau | 67 |
| Dòng thêm | 10 |
| Dòng cũ đổi hoặc bị xóa | **0** |

Hồ sơ: [md5-before.txt](../../games/typing-defense/art-src/_review/100/md5-before.txt), [md5-after.txt](../../games/typing-defense/art-src/_review/100/md5-after.txt), [md5.diff](../../games/typing-defense/art-src/_review/100/md5.diff), [ka1-final.json](../../games/typing-defense/art-src/_review/100/ka1-final.json). Ngoài hai dòng tiêu đề, diff chỉ thêm dòng; không có dòng trừ.

### Nứt · 16 ô, lề, sắc khóa và diễn tiến

BBox/lề lấy trên **alpha > 0**, không bỏ qua pixel mờ. Hue/S dùng HSV từ RGB sRGB; đếm mọi pixel alpha > 0, kể cả pixel bán trong suốt.

| Khung | Diện tích alpha > 0, px | Tổng alpha quy về px đặc | Lề nhỏ nhất, px | Bán kính xa nhất, px |
| --- | ---: | ---: | ---: | ---: |
| 1 | 1105 | 921,031 | 108 | 20,112 |
| 2 | 1959 | 1533,039 | 98 | 30,438 |
| 3 | 2863 | 2123,671 | 87 | 40,700 |
| 4 | 3839 | 2798,000 | 77 | 50,936 |
| 5 | 4980 | 3596,306 | 67 | 61,160 |
| 6 | 6081 | 4250,592 | 57 | 71,390 |
| 7 | 6965 | 4774,639 | 46 | 81,624 |
| 8 | 7787 | 5240,639 | 37 | 91,829 |
| 9 | 8334 | 5518,518 | 26 | 102,100 |
| 10 | 8464 | 5576,600 | 24 | 112,368 |
| 11–16, từng ô | 8464 | 5576,600 | 24 | 112,368 |

- **16/16 ô** có hình; lề thấp nhất **24 px**, đạt ≥ 24.
- Pixel `alpha > 0`, hue 285–330° và S > 0,5: **0 px, 0%**, đạt ở cả 16 ô.
- Diện tích alpha và tổng alpha đều **không giảm từ 1 đến 10**. Vùng đã hiện giữ nguyên vị trí; chỉ mở thêm đoạn ra ngoài.
- Khung 10: bán kính ô là 128 px; điểm xa nhất đạt **112,368 px = 87,79%**, vượt 80%. Kiểm thêm trên alpha ≥ 0,5 vẫn đạt **111,591 px = 87,18%**, nên không dựa vào pixel gần trong suốt để qua ngưỡng.
- Alpha/hình học khung **10–16 giống nhau hoàn toàn**. Trung bình L của cùng mặt nạ lõi cam: `0,243326` ở khung 10, `0,364526 / 0,278429 / 0,243326` ở 11–13, lặp đúng dãy đó ở 14–16. Đỉnh tăng khoảng **1,498 lần**: đủ hai nhịp, không đổi bán kính.

### Bọt · Nối dọc và mờ mép ngang

Đo theo Y: `E = mean |hàng 0 − hàng 1023|`; `I = mean |hàng y − hàng y−1|` cho toàn bộ 1023 cặp hàng trong ảnh. L tính trên RGB thẳng của PNG; đo thêm L đã nhân alpha để đối chiếu hình khi ghép.

| Kênh | E theo Y | I theo Y | 1,25 × I | E/I | Kết quả |
| --- | ---: | ---: | ---: | ---: | --- |
| L sRGB | 0,000000000 | 0,063519552 | 0,079399440 | 0 | Đạt |
| Alpha | 0,000000000 | 0,015288964 | 0,019111204 | 0 | Đạt |
| L × alpha, kiểm thêm | 0,000000000 | 0,015232576 | 0,019040721 | 0 | Đạt |

| Dải ngoài cùng | Số cột | Alpha trung bình | Giới hạn | Kết quả |
| --- | ---: | ---: | ---: | --- |
| Trái | 41 | **0,000511212** | ≤ 0,05 | Đạt |
| Phải | 41 | **0,000447790** | ≤ 0,05 | Đạt |

41 cột là làm tròn lên của 4% × 1024 = 40,96. Hai cột biên ngoài cùng có alpha 0. Đã xem dải 1 × 3 ở hai cỡ; không thấy đường cắt ngang cứng tại chỗ lặp. Có vùng hòa hai nét trong đoạn nối; không đánh đồng E = 0 với nghiệm thu chuyển động trong game.

## 4. Ảnh kiểm và KA5

Ảnh kiểm nằm đúng `art-src/_review/`, không nằm trong `public/` hay `docs/`:

- [100-crack.jpg](../../games/typing-defense/art-src/_review/100-crack.jpg): đúng 16 ô 64 px, ghép lên cỏ của 095; giữ bản kiểm v1 theo luật không ghi đè. Sau khi sửa 34 pixel ở nguồn 1024², có [100-crack-final.jpg](../../games/typing-defense/art-src/_review/100-crack-final.jpg) ghép trực tiếp từ PNG giao. Dùng bản **final** để chấm cuối.
- [100-crack-full-final.jpg](../../games/typing-defense/art-src/_review/100-crack-full-final.jpg): 16 ô 256 px; bản v1 `100-crack-full.jpg` cũng được giữ.
- [100-foam.jpg](../../games/typing-defense/art-src/_review/100-foam.jpg): 1024 × 3072, lát **1 × 3 theo dọc** trên `#8a8f94`, đúng PNG bọt giao.
- [100-foam-small.jpg](../../games/typing-defense/art-src/_review/100-foam-small.jpg): 256 × 768, cùng ba chu kỳ ở bề rộng 256 px.

Đã mở và xem nguồn sinh, ảnh ghép cỡ đầy đủ và cỡ nhỏ. Thứ tự điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2; chỉ cho Dùng tiếp = 2 sau khi mọi kiểm số của ảnh đạt.

| Ảnh, cỡ xem | Đúng đề | Đọc được | Hợp bộ | Hình khối | Dùng tiếp | Tổng | Nhận xét còn thiếu |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Nứt, ô 256 px | 2 | 2 | 2 | 1,5 | 2 | **9,5/10 · Đạt** | Dáng rễ gãy có mực tối và lõi son; các đầu nhánh ở pha mở bị mặt nạ cắt hơi dứt khoát. |
| Nứt, ô 64 px | 2 | 1,5 | 2 | 1,5 | 2 | **9/10 · Đạt** | Nhận ra vùng nguy hiểm và hai mức sáng; nhánh nhỏ và lõi cam mảnh mất bớt, nhất là khung đầu. |
| Bọt, rộng 1024 px | 2 | 2 | 1,5 | 1,5 | 2 | **9/10 · Đạt** | Dải bạc có hướng chảy rõ, nối được; nét nhiều hơn phong cách phẳng của bộ cũ, đoạn hòa có ít nét chồng. |
| Bọt, rộng 256 px | 2 | 2 | 1,5 | 1,5 | 2 | **9/10 · Đạt** | Các dòng chính vẫn rõ; vài giọt nhỏ nhập thành vệt, sắc trên đá hơi thiên lam ngọc. |

Điểm trên là **Codex tự chấm**, chưa thay điểm Claude. Mức cần để nhận là Claude chấm lại ≥ 8 theo phiếu. Không sửa danh sách nâng cấp mỹ thuật chung vì ngoài đường dẫn cho phép; thiếu sót đã ghi tại đây.

## 5. Khác phiếu, phần chưa làm và việc cần xem

Các điều chỉnh đã nêu rõ: nguồn sinh 1254² được giữ nguyên, đầu ra chuẩn hóa 1024²; lấy một ô sinh để bảo toàn hình học của chuỗi nứt; dùng nối dọc bằng công cụ cho bọt; giữ ảnh kiểm v1 và thêm hậu tố `final` cho nứt để không ghi đè file đã tạo. Không sinh lại vì các lỗi đều sửa được và bản sửa qua kiểm.

**Cần Claude/người duyệt xem** hai ảnh kiểm cuối ở cỡ nhỏ, nhất là độ rõ lõi cam trên cỏ và vùng hòa của dải bọt. Khi tích hợp, dùng `.alpha.png`, không dùng `.try1.png`. Nứt phải hiện **ít nhất 1,2 s trước khi trồi rễ**; ví dụ phát đủ 16 ô với 75 ms/ô cho tổng 1200 ms, giữ khung 16 nếu thời gian báo trước dài hơn. Đây là hướng dẫn thời lượng, **chưa được kiểm trong runtime**.

Không tích hợp `public/`, sửa mã, changelog game hoặc tài liệu khác; các việc đó ngoài phạm vi phiếu. Không làm âm thanh vì phiếu chỉ có ảnh. Không chạy Git, build, test suite, dev server, trình duyệt hay mạng ngoài `image_gen`; không đọc/ghi phần game đang tạm dừng, không ghi game khác. Không có khung chụp trình duyệt cần dọn; nguồn `.try1.*`, các bản sửa và ảnh kiểm đều được giữ.
