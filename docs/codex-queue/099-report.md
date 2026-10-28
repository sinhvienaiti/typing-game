# Phiếu 099 · Lời Gọi · Ghost Flame: tham chiếu và flipbook chết

Ngày 29/10/2026 · Sinh bằng **image_gen tích hợp**, hậu kỳ ngoại tuyến bằng ImageMagick 7.1.2-34 và Python 3. **Hai lần sinh tổng cộng: một lượt cho mỗi ảnh.** Không cần lượt 2–3.

Đã giao `ma-troi-sheet.png` đúng prompt gốc và `ma-troi-death.alpha.png` qua toàn bộ kiểm 2–4. Death tự chấm **9/10 ở ô 256 px, 8,5/10 ở ô 64 px**. Đây là tự chấm; **chờ Claude chấm lại từ 8 điểm** trước khi tích hợp.

## 1. File giao và prompt

Gốc media: `games/typing-defense/art-src/`.

| File trong `vfx/` | Vai trò |
|---|---|
| `ma-troi-sheet.try1.png`, `ma-troi-sheet.try1.prompt.txt` | Nguồn sinh lượt 1, 1536 × 1024, nền navy; giữ nguyên. |
| `ma-troi-sheet.png` | Bản chọn, chép nguyên byte từ try1. Prompt cạnh ảnh là `ma-troi-sheet.prompt.txt` **có sẵn, giữ nguyên**. |
| `ma-troi-death.try1.png`, `ma-troi-death.try1.prompt.txt` | Nguồn sinh lượt 1 trên đen, thực tế 1254 × 1254; giữ nguyên. |
| `ma-troi-death.png`, `ma-troi-death.prompt.txt` | Chép nguyên byte ảnh nguồn và prompt lượt 1; ảnh này là nguồn RGB, chưa phải bản alpha để tích hợp. |
| `ma-troi-death.alpha.png` | Bản hậu kỳ được chọn: **1024 × 1024, RGBA thẳng, 16 ô 256 px**. |

**Sheet, lượt 1:** gửi nguyên văn `ma-troi-sheet.prompt.txt`, không thêm hay sửa yêu cầu. Ảnh có bảy Ghost Flame tròn ở các độ cao/cỡ khác nhau; mắt tối, lửa trắng xanh, lõi tím, vệt mực tím đen ở con lớn nhất; bên phải là ba bước lửa → vỡ → tia thủy tinh. Nền navy, không chữ hay đường khung. Đường cỏ không được vẽ thành cảnh: giữ nền navy của tờ tham chiếu như prompt. Không hậu kỳ ảnh này.

**Death, lượt 1:** mở đầu nguyên văn hai đoạn đầu của `ma-troi-wisp.prompt.txt`. Thay đoạn loop bằng one-shot chết 16 khung: sống → co/chập chờn → nhắm mắt 4–5 → vỡ thành tia tinh thể 6–10 → rơi và co tới một tia cuối. Bổ sung kích thước wisp tham chiếu khoảng 140 × 191 px/ô, màu viền cobalt–lõi tím, thứ tự từng hàng, giới hạn lề, hình còn hiện trong ô 16 và tan bằng giảm kích thước. Tham chiếu trực tiếp `ma-troi-wisp.alpha.png` khi gọi image_gen. Prompt chính xác nằm cạnh try1 và bản chọn; không sửa prompt sau khi sinh.

## 2. Hậu kỳ đã dùng

Script chạy lại được, chỉ tạo file mới:

- [`refine-alpha.py`](../../games/typing-defense/art-src/_review/099/refine-alpha.py): chuẩn hóa, sửa hình và chuyển alpha; dùng `--name candidate-v2` nếu cần chạy lại, không ghi đè v1.
- [`verify.py`](../../games/typing-defense/art-src/_review/099/verify.py): đo và ghép ảnh kiểm; dùng `--tag <tên-mới>` khi chạy lại.
- [`deliver.py`](../../games/typing-defense/art-src/_review/099/deliver.py): chép bản chọn bằng chế độ độc quyền, chạy `md5 -r`, đối chiếu KA1. Chế độ `--snapshot <tên-mới.txt>` tạo snapshot mới.

Các bước death:

1. Resize nguồn 1254² về 1024² bằng Triangle; ngưỡng `max(R,G,B) ≤ 3/255` đưa về đen để bỏ nhiễu nền khoảng 1/255.
2. Nguồn trước sửa có bbox khung 1 ở ngưỡng alpha dự kiến > 0,1 là 146 × 195, rộng hơn wisp 14,06%. Thu đồng đều **0,90** toàn chuỗi, dùng cùng gốc `(128,124)` để khớp kích thước và giữ chuyển động các pha đầu.
3. Bỏ đốm sáng phụ nhỏ bằng connected components ngưỡng 25/255, kết nối 8 hướng: ô 7 bỏ ba đốm, ô 8 bỏ một thành phần 1 px, ô 10 bỏ một đốm. Không vẽ lại tia chính. Tọa độ và diện tích từng vùng sửa ở [`candidate-v1.postprocess.json`](../../games/typing-defense/art-src/_review/099/candidate-v1.postprocess.json).
4. Ô 11–16 nhân thêm kích thước **0,95 / 0,85 / 0,75 / 0,65 / 0,50 / 0,20**; tâm bbox lần lượt xuống y = **164 / 172 / 180 / 188 / 196 / 204**. Giữ đỉnh sáng sau resize bằng hệ số bù được ghi trong JSON. Không nhân giảm alpha toàn ô để giả tắt. Ô 16 còn một tia 7 × 8 px tính cả quầng; vùng alpha > 0,1 là 5 × 6 px.
5. Công thức từ `_review/043/refine-alpha.py`: với RGB chuẩn hóa và `E = max(R,G,B)`, đặt `RGB_mới = RGB/E`, `A_mới = A_key × E`; E = 0 thì RGBA = 0. Ở đây nền đã khóa nhị phân nên `A_key = 1` cho phần giữ lại. Script 099 lưu chính xác bản điều chỉnh đã chạy; không chạy script 043 vì script đó ghi vào thư mục ngoài phạm vi.

Lệnh thực tế, từ repo cha:

```sh
python3 games/typing-defense/art-src/_review/099/refine-alpha.py
python3 games/typing-defense/art-src/_review/099/verify.py --candidate --tag candidate
python3 games/typing-defense/art-src/_review/099/deliver.py
python3 games/typing-defense/art-src/_review/099/verify.py
```

## 3. KA1 · Chỉ thêm file

Snapshot `md5 -r` toàn bộ file trong `vfx/` trước lần ghi đầu và sau giao: **49 → 57 file; thêm 8, sửa 0, xóa 0**. `diff` ngoài tiêu đề và dòng ngữ cảnh chỉ có dòng thêm. Hồ sơ: [`md5-before.txt`](../../games/typing-defense/art-src/_review/099/md5-before.txt), [`md5-after.txt`](../../games/typing-defense/art-src/_review/099/md5-after.txt), [`md5.diff`](../../games/typing-defense/art-src/_review/099/md5.diff), [`md5-comparison.json`](../../games/typing-defense/art-src/_review/099/md5-comparison.json).

| File bảo vệ | MD5 trước = sau |
|---|---|
| `ma-troi-sheet.prompt.txt` | `8639db820cc63e1569ff1c1b34d07900` |
| `ma-troi-wisp.png` | `2c989ea36b21b89351443b217a6a45b0` |
| `ma-troi-wisp.alpha.png` | `c03227607b818e891a1635e53cef1a5b` |
| `ma-troi-wisp.prompt.txt` | `2ff8f302dd072905b73153e6f3698af5` |

Kiểm byte xác nhận sheet.try1.prompt bằng prompt sheet gốc; death.try1.prompt mở đầu đúng hai đoạn wisp. Không ghi lại prompt sheet có sẵn.

## 4. Kiểm 2–4 · Số đo bản alpha giao

Chi tiết và trạng thái từng cổng: [`verification.json`](../../games/typing-defense/art-src/_review/099/verification.json). Bbox dùng tọa độ cận phải/dưới loại trừ. Kiểm ở cả alpha > 0 và alpha > 0,1; lề bên dưới dùng **mọi pixel alpha > 0**, chặt hơn ngưỡng 043.

| Kiểm | Số đo | Ngưỡng | Kết quả |
|---|---|---|---|
| Khổ/kênh | `1024 1024 srgba 4.0` | 1024² RGBA | Đạt |
| Ô có hình | 16/16, cả ở alpha > 0,1 | 16/16 | Đạt |
| Lề nhỏ nhất | **29 px**, ô 11 | ≥ 24 px | Đạt |
| Alpha lớn nhất ở viền 4 px mỗi ô | **0/255** | 0 | Đạt |
| Viền nền đen | **0 px**; trong vùng 0,05 < alpha < 0,95 không có pixel RGB tối dư (`max RGB < 254/255`) | 0 px | Đạt; xem thêm ghép nền sáng |
| Bbox khung 1, alpha > 0 | death `[57,35,200,220]`, wisp `[58,32,198,223]`; lệch cỡ X/Y **2,14% / 3,14%** | ≤ 10% | Đạt |
| Bbox khung 1, alpha > 0,1 | death `[63,38,195,214]`, wisp `[64,35,192,216]`; lệch cỡ X/Y **3,13% / 2,76%** | ≤ 10% | Đạt |
| Lệch tọa độ bbox | tối đa **2,34%** chiều bbox tham chiếu | ≤ 10% | Đạt |
| Hue trung vị, alpha > 0,1 | death **218,70°**, wisp **217,95°**; lệch **0,75°** | ≤ 10° | Đạt |
| Hue, loại pixel saturation < 0,05 | lệch **0,93°** ở alpha > 0,1; **2,43°** trên mọi alpha > 0 | ≤ 10° | Đạt |
| Tổng alpha khung 16 / khung 1 | **1.976 / 3.484.964 = 0,05670%**, đơn vị alpha 8-bit | ≤ 5% | Đạt |

| Khung | Lề nhỏ nhất, px | Tổng alpha 8-bit | Khung | Lề nhỏ nhất, px | Tổng alpha 8-bit |
|---|---|---|---|---|---|
| 1 | 35 | 3.484.964 | 9 | 37 | 712.707 |
| 2 | 39 | 2.472.623 | 10 | 40 | 504.723 |
| 3 | 36 | 2.068.363 | 11 | 29 | 325.625 |
| 4 | 35 | 1.911.534 | 12 | 36 | 127.638 |
| 5 | 43 | 2.081.454 | 13 | 40 | 84.750 |
| 6 | 44 | 1.662.367 | 14 | 47 | 31.457 |
| 7 | 32 | 1.099.768 | 15 | 49 | 10.333 |
| 8 | 31 | 858.409 | 16 | 48 | 1.976 |

Ô 5 hơi nở lại so với ô 4, phù hợp pha chập chờn; pha sau vỡ giảm liên tục về tổng alpha. Tia cuối vẫn có đỉnh alpha 254/255: tắt bằng giảm diện tích, không phải giảm độ đục đồng loạt.

## 5. Ảnh kiểm và KA5

- [`099-sheet.jpg`](../../games/typing-defense/art-src/_review/099-sheet.jpg): đủ 16 khung ở **ô 64 px** trên `backdrops/w1-silverfall/sky-a.png` và cùng nền nhân RGB **0,25**; bên cạnh là tờ tham chiếu; thêm cặp khung 1 wisp/death.
- [`099-native.jpg`](../../games/typing-defense/art-src/_review/099-native.jpg): đủ khung ở **ô 256 px**, nền sáng và tối, ghép alpha thường, không bloom.
- [`099-compare.jpg`](../../games/typing-defense/art-src/_review/099-compare.jpg): khung 1 wisp/death ở ô 256 px cạnh nhau trên cùng nền.
- Bộ `099-candidate-*.jpg` ghi lại kiểm trước khi chép bản chọn; bản alpha giao cùng byte candidate-v1.

Đã xem ảnh sinh sheet ở khổ gốc 1536 × 1024, nguồn death, bộ ghép native và bộ ô 64 px. Năm tiêu chí theo ART_ACCEPTANCE §2.2, mỗi mục 0–2. “Dùng tiếp” được 2 vì toàn bộ số đo bắt buộc đã đạt.

| Ảnh / cỡ | Đúng đề | Đọc được | Hợp bộ | Hình khối | Dùng tiếp | Tổng |
|---|---|---|---|---|---|---|
| Death, ô 256 px | 2 | 1,5 | 1,5 | 2 | 2 | **9/10 · Đạt tự chấm** |
| Death, ô 64 px | 2 | 1 | 1,5 | 2 | 2 | **8,5/10 · Đạt tự chấm, cần Claude chấm lại** |
| Sheet, khổ gốc | 2 | — | 1,5 | — | — | **3,5/4**, chỉ hai tiêu chí theo phiếu |

Điểm còn thiếu: lửa và tinh thể hơi bóng so với chất giấy phẳng; mắt và các tia nhỏ ở cuối chuỗi khó thấy trên mây trắng, nhất là ô 64 px. Dáng flame, mắt nhắm và bước vỡ thành tinh thể vẫn rõ; tia cuối gần biến mất đúng ý tắt hẳn. Sheet đồng bộ bảng trắng xanh–tím của wisp, đủ đàn và dải chết, nhưng cũng hơi nhiều chuyển sắc.

## 6. Phạm vi và phần chờ

Đối chiếu VFX_STANDARD §3.3: đây là **quái chết T2**, vật liệu Ghost Flame → tia thủy tinh; texture phục vụ I/F. A/R/T không áp dụng cho hàng quái chết trong bảng chuẩn. Cảnh kiểm là chuỗi chết độc lập trên trời Silverfall sáng/tối, dùng wisp hiện có làm tham chiếu nhận diện. Không tuyên bố đã nghiệm thu timing, phối lớp, FPS, thẻ chữ hay cảm nhận trong trận.

Khác phiếu ở khổ ảnh sinh death: công cụ trả **1254²**, đã chuẩn hóa miễn phí thành alpha 1024². Bản `.png` vẫn giữ nguyên nguồn sinh theo luật chép bản chọn; làn tích hợp dùng `.alpha.png`. Các sửa kích thước, đốm thừa và đường rơi đều có script/JSON; không phát sinh lượt sinh lại.

Không làm âm thanh, runtime, public, tài liệu chung hay danh sách nâng cấp vì ngoài phạm vi cho phép. Không chạy Git, build, test suite, trình duyệt, dev server hay mạng ngoài image_gen; không đọc/ghi đường dẫn game bị tạm dừng. Không có raw capture trình duyệt/render cần dọn; nguồn try1 được giữ nguyên theo phiếu.

**Chủ dự án/Claude cần xem:** tờ `099-sheet.jpg`, nhất là độ đọc các tia trên trời sáng ở ô 64 px; chấm lại trước khi Claude chép alpha vào public. Chưa tích hợp và chưa nghiệm thu thay Claude.
