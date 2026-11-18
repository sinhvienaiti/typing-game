# Phiếu 118 · Wordwoven · Đá và gỗ sử thi v3, v4

Ngày giao: 29/10/2026. Công cụ sinh: `image_gen` tích hợp của Codex; hậu kỳ bằng ImageMagick 7, Node và Python trực tiếp trên macOS.

**Đã giao đủ 8/8 bản chọn; 12 lượt sinh, tối đa 3 lượt một ảnh. Tám ảnh qua kiểm kỹ thuật 2–7; tự chấm M ≥ 8 và Q ≥ 8. Cảnh ghép M = 8,0. Chờ Claude chấm nhận, chưa coi tự chấm là nghiệm thu cuối.**

Chạy ngay theo chỉ đạo mới, không chờ 117. Hồ sơ cũ chưa sinh ảnh; giữ nguyên tám prompt `.try1.prompt.txt` và toàn bộ script cũ. Bản báo cáo trước khi tiếp nối được giữ tại `_review/118/resume-20261029/report-before-resume.md`. Ngoài báo cáo này, không sửa tài liệu, mã, tài nguyên cũ hay game khác; không dùng Git, mạng, trình duyệt, dev server, build hoặc test suite.

## 1. Bản giao

Các đường dẫn dưới đây tính từ `games/typing-defense/art-src/`. Mỗi ảnh có prompt cùng tên `.prompt.txt`. Mọi lượt sinh giữ nguyên byte nguồn ở `.tryN.png`, kèm `.tryN.prompt.txt`; không xóa lượt bị loại.

| Bản chọn | Lượt chọn / đã sinh | Khổ giao | Nền |
|---|---:|---|---|
| [rock-medium-v3.png](../../games/typing-defense/art-src/scenery/meadow/rock-medium-v3.png) | 2 / 2 | 1254 × 1254 | M `#FF00FF` |
| [rock-medium-v4.png](../../games/typing-defense/art-src/scenery/meadow/rock-medium-v4.png) | 2 / 2 | 1254 × 1254 | M `#FF00FF` |
| [rock-small-v3.png](../../games/typing-defense/art-src/scenery/meadow/rock-small-v3.png) | 3 / 3 | 1536 × 1024 | M `#FF00FF` |
| [rock-small-v4.png](../../games/typing-defense/art-src/scenery/meadow/rock-small-v4.png) | 1 / 1 | 1536 × 1024 | M `#FF00FF` |
| [rotten-log-v3.png](../../games/typing-defense/art-src/scenery/meadow/rotten-log-v3.png) | 1 / 1 | 1536 × 1024 | M `#FF00FF` |
| [rotten-log-v4.png](../../games/typing-defense/art-src/scenery/meadow/rotten-log-v4.png) | 1 / 1 | 1536 × 1024 | M `#FF00FF` |
| [tree-stump-v3.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v3.png) | 1 / 1 | 1254 × 1254 | M `#FF00FF` |
| [tree-stump-v4.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v4.png) | 1 / 1 | 1254 × 1254 | M `#FF00FF` |

Tất cả có rêu hoặc lá xanh, không có hồng/tím, nên dùng nguyên câu BG-M của §3.8. STYLE + MAP + SCENERY giữ nguyên văn và đúng thứ tự ở mọi prompt. Bốn ảnh vuông do công cụ trả về **1254 × 1254**, đủ ngưỡng ≥1254; giữ khổ gốc, không phóng giả lên 1536. Bốn ảnh ngang đúng 1536 × 1024.

## 2. Prompt và lựa chọn từng lượt

| Ảnh | Lượt 1 | Sửa lượt 2 | Sửa lượt 3 / quyết định |
|---|---|---|---|
| `rock-medium-v3` | Đúng đá vôi sáng nhưng thành núi phủ cây; loại vì sai tỷ lệ vật 2–4 m. | Khóa tảng đá 3 m, 4–7 mặt khối, rêu bám sát mặt đá; loại cây, rừng và phong cảnh khỏi nội dung. | Chọn lượt 2: đỉnh cao nghiêng trái, rãnh đứng sâu; không cần lượt 3. |
| `rock-medium-v4` | Hai khối nhưng có cây như núi thu nhỏ; loại. | Cùng sửa tỷ lệ và rêu như v3, giữ hai khối thấp rộng, đỉnh chính bên phải. | Chọn lượt 2; không cần lượt 3. |
| `rock-small-v3` | Thành cụm vách đá và dương xỉ; loại vì sai dáng đá nhỏ tròn. | Thêm v1 làm **tham chiếu dáng**: đá cao ngang gối, rộng 0,9 m, vai trái cao, khối tròn liền; cấm lấy viền mực và màu xanh nõn cũ. Dáng đã đúng nhưng chất liệu còn chấm vụn. | Lượt 3 dùng try2 chỉ cho dáng và `rock-medium-v4.try2.png` cho chất liệu; tăng mặt đá vôi sáng lớn, rãnh lạnh và rêu thấp. Chọn try3; rêu còn hơi có nét cọ nhỏ khi xem lớn, không sinh quá giới hạn. |
| `rock-small-v4` | Phiến thấp rộng với mép phải nhô lên, rãnh xói rõ. | Không cần. | Chọn lượt 1. |
| `rotten-log-v3` | Thân dài thẳng, miệng rỗng phải, vỏ nứt và dương xỉ gắn trên gỗ. | Không cần. | Chọn lượt 1. |
| `rotten-log-v4` | Thân cong ngắn, miệng rỗng trái, chạc gãy vươn phía phải. | Không cần sinh lại: vấn đề màu mép do bước đổi cỡ được giải quyết bằng giữ hình gốc, xem §3. | Chọn lượt 1. |
| `tree-stump-v3` | Gốc cao, vành gãy cao bên trái, mặt vòng tuổi lõm và rễ bạnh. | Không cần. | Chọn lượt 1. |
| `tree-stump-v4` | Gốc thấp rộng, mặt cắt bầu dục sạch có vòng tuổi, rễ lớn. | Không cần. | Chọn lượt 1. |

Không đính kèm ảnh cũ như tham chiếu phong cách. Đã xem ảnh mẫu chủ dự án, phông ngày 114, tờ và tám bản chọn 116, cùng v1/v2 của bốn loại. 117 đã có bản chọn trong lúc làm, nên cảnh kiểm dùng thêm `fern-v3` và `tall-grass-v4`.

## 3. Hậu kỳ theo ART_ACCEPTANCE §5

Chỉ tách màu khóa magenta, cắt nền rỗng, đổi cỡ đồng tỷ lệ và thêm lề. Không chỉnh sáng, gamma hay màu; không san phẳng đá, xóa rêu/lá, phủ vùng vẽ, thêm viền mực hoặc loại vùng theo diện tích. Mặt nạ loại màu khóa hue 300±18°, S > 0,35 hoặc khoảng cách RGB tới `#FF00FF` ≤60; không coi các khe tối trong vật là nền. Không ép alpha sau đổi cỡ.

**Trường hợp cần giữ tranh:** bản thử hậu kỳ `rotten-log-v4` thu nhỏ về 88% khung tạo 0,6484% pixel sát màu khóa, vượt 0,5%. Dừng hướng ép ngưỡng bằng cắt lá hoặc siết alpha. Hộp bao nguồn đã là `(48,102,1442,807)`; chỉ dịch trái **1 px**, không đổi cỡ. Hộp bao giao `(47,102,1442,807)`, hai lề 47 px, chân cách đáy 115 px; nhiễm màu về **0%**. Toàn bộ pixel vật sau tách nền giữ nguyên. Bản thử không giao vẫn nằm trong hồ sơ, không ghi đè.

Tám tờ «bản sinh | bản hậu kỳ» cùng cỡ canvas, có nhãn; đã xem từng tờ để đối chiếu hình vẽ:
- [rock-medium-v3](../../games/typing-defense/art-src/_review/118-before-after-rock-medium-v3.jpg)
- [rock-medium-v4](../../games/typing-defense/art-src/_review/118-before-after-rock-medium-v4.jpg)
- [rock-small-v3](../../games/typing-defense/art-src/_review/118-before-after-rock-small-v3.jpg)
- [rock-small-v4](../../games/typing-defense/art-src/_review/118-before-after-rock-small-v4.jpg)
- [rotten-log-v3](../../games/typing-defense/art-src/_review/118-before-after-rotten-log-v3.jpg)
- [rotten-log-v4](../../games/typing-defense/art-src/_review/118-before-after-rotten-log-v4.jpg)
- [tree-stump-v3](../../games/typing-defense/art-src/_review/118-before-after-tree-stump-v3.jpg)
- [tree-stump-v4](../../games/typing-defense/art-src/_review/118-before-after-tree-stump-v4.jpg)

## 4. Kiểm kỹ thuật

Phép đo chạy trên **đúng PNG được giao**, đối chiếu SHA-256 với ứng viên đã đo. Lấy RGB 8 bit bằng `magick <ảnh> -alpha off -depth 8 rgb:-`; vật là pixel có độ lệch tới nền >60 ở ít nhất một kênh, đúng định nghĩa phiếu. Từ mặt nạ này tính hộp bao, vùng liền 8 hướng và dải mép trong dày 3 px bằng lân cận vuông 7×7. Luma dùng `(0,2126R + 0,7152G + 0,0722B)/255`. Các con số chưa làm tròn nằm trong JSON.

| Ảnh | Hộp bao x,y,w,h (px) | Lề trái/phải/trên/đáy (%) | Lệch mép 10 px tối đa | Nhiễm màu (%) | Vùng >1% |
|---|---|---|---:|---:|---:|
| `rock-medium-v3` | 212,75,830,1104 | 16.906/16.906/5.981/5.981 | 0 | 0.2034 | 1 |
| `rock-medium-v4` | 75,454,1104,725 | 5.981/5.981/36.204/5.981 | 0 | 0.2030 | 1 |
| `rock-small-v3` | 92,146,1352,817 | 5.990/5.990/14.258/5.957 | 0 | 0.1342 | 1 |
| `rock-small-v4` | 92,293,1352,670 | 5.990/5.990/28.613/5.957 | 0 | 0.2816 | 1 |
| `rotten-log-v3` | 92,411,1352,552 | 5.990/5.990/40.137/5.957 | 0 | 0.4920 | 1 |
| `rotten-log-v4` | 47,102,1442,807 | 3.060/3.060/9.961/11.230 | 0 | 0.0000 | 1 |
| `tree-stump-v3` | 75,76,1104,1103 | 5.981/5.981/6.061/5.981 | 0 | 0.2981 | 1 |
| `tree-stump-v4` | 75,532,1104,647 | 5.981/5.981/42.424/5.981 | 0 | 0.3059 | 1 |

Tất cả: mép ≤12; nhiễm màu ≤0,5%; lề trái/phải/trên ≥3%; đáy ≤12%; đúng một vùng liền >1%. Không có xóa vùng nhỏ để ép phép đo.

| Ảnh | Luma trung vị toàn vật | Luma trung vị mép 3 px | Mép / toàn vật | Ngưỡng ≥0,6 |
|---|---:|---:|---:|---|
| `rock-medium-v3` | 0.4524 | 0.4554 | 1.0066 | Đạt |
| `rock-medium-v4` | 0.5028 | 0.5119 | 1.0181 | Đạt |
| `rock-small-v3` | 0.4788 | 0.4193 | 0.8756 | Đạt |
| `rock-small-v4` | 0.4141 | 0.3054 | 0.7375 | Đạt |
| `rotten-log-v3` | 0.2798 | 0.3766 | 1.3462 | Đạt |
| `rotten-log-v4` | 0.2736 | 0.3446 | 1.2594 | Đạt |
| `tree-stump-v3` | 0.3616 | 0.3784 | 1.0464 | Đạt |
| `tree-stump-v4` | 0.3879 | 0.3325 | 0.8570 | Đạt |

| Loại | W/H v3 | W/H v4 | Độ lệch so với v3 | ≥15% |
|---|---:|---:|---:|---|
| `rock-medium` | 0.7518 | 1.5228 | 102.55% | Đạt |
| `rock-small` | 1.6548 | 2.0179 | 21.94% | Đạt |
| `rotten-log` | 2.4493 | 1.7869 | 27.05% | Đạt |
| `tree-stump` | 1.0009 | 1.7063 | 70.48% | Đạt |

Công thức khác biệt: `abs(r4-r3)/r3 × 100`. Không cần viện đến vị trí đỉnh để qua ngưỡng. Hai loại đá đổi đỉnh trái → phải; gỗ đổi thân thẳng → cong có chạc; gốc đổi cao gãy → thấp mặt cắt.

## 5. Tờ kiểm và mức chợ

- [Tờ v1/v2/v3/v4 theo tên phiếu](../../games/typing-defense/art-src/_review/118-sheet.jpg). Tờ đầu dùng ô rộng 850 px, riêng đầu khúc gỗ v1 cũ bị hụt khoảng 5 px mỗi bên; giữ tờ đã ghi để không ghi đè, không ảnh nguồn nào bị cắt.
- [Tờ đầy đủ không hụt mép — dùng tờ này khi duyệt](../../games/typing-defense/art-src/_review/118-sheet-complete.jpg): mỗi vật cao 256 px, ô rộng 1100 px, nền `#3f5a48`, đủ toàn vật cũ và mới.
- [Tám ảnh ở cỡ 128 px cạnh dài](../../games/typing-defense/art-src/_review/118-small.jpg): cả tám nhận ra loại vật; đá thấy rãnh đứng, gỗ thấy miệng rỗng/chạc, gốc thấy rễ và mặt cắt. Chi tiết vòng tuổi và lá nhỏ gom lại, dáng chính vẫn rõ.
- [Cảnh kiểm 1536 × 1024](../../games/typing-defense/art-src/_review/118-mock.jpg): phông 114 và vật liệu đất đá sẵn có được ghép bằng script; cây 116, dương xỉ/cỏ 117. Không sinh thêm tranh, không vẽ vật thay thế bằng mã.
- [Cảnh kiểm cạnh ảnh mẫu, cùng cao 640 px](../../games/typing-defense/art-src/_review/118-vs-ref.jpg). **Đứng cạnh được về chất liệu và khối cảnh vật:** đá vôi có mặt sáng và khe lạnh, gỗ có vỏ/rễ thật, bỏ cảm giác hình dán có viền mực; đi cùng cây mới và thế giới karst. Chưa ngang mức 9 của ảnh mẫu: đất ghép còn đều, thiếu bóng tiếp xúc và bố cục tiền cảnh còn là cảnh kiểm. **M chung cảnh kiểm = 8,0.**

Thước mét ở tiền cảnh: 76 px/m; lính giáo nguồn cao 1,8 m → 137 px. Đá vừa v3 cao 3,4 m, v4 rộng 3,9 m; đá nhỏ rộng 1,1/1,2 m; khúc gỗ dài 5,8/4,4 m; gốc v3 cao 2,3 m và v4 rộng 2,5 m. Hai cây 116 là lớp sau, 30 px/m; không lấy cùng tỷ lệ tiền cảnh. `scene-final/layout.json` ghi vị trí, kích cỡ và vai trò từng ảnh. Đây là ghép tĩnh kiểm vật liệu/tỷ lệ; không giả làm nghiệm thu camera runtime 55° từ 58 m.

M tự chấm trên **bản hậu kỳ**, đặt trong cảnh ghép; kiểm thêm ảnh đầy đủ và bản thu 128 px. Q theo năm tiêu chí 0–2: đúng đề / đọc được / hợp bộ / hình khối / dùng được. Điểm 128 được ghi riêng, không suy từ việc số đo đã qua.

| Ảnh | M đầy đủ | M 128 | Q năm tiêu chí đầy đủ | Q đầy đủ | Q 128 | Nhận xét còn lại |
|---|---:|---:|---|---:|---:|---|
| `rock-medium-v3` | 8,2 | 8,1 | 2/2/2/2/2 | 10 | 9,5 | Đỉnh trái và rãnh đá hùng, rêu thấp; rãnh nhỏ mất bớt ở 128. |
| `rock-medium-v4` | 8,2 | 8,1 | 2/2/2/2/2 | 10 | 9,5 | Hai khối liên chân rõ, sáng ngà và khe teal hợp bộ. |
| `rock-small-v3` | 8,0 | 8,0 | 2/2/1,5/2/2 | 9,5 | 9,5 | Dáng gọn, vai trái cao; rêu còn hơi nét cọ vụn so với đá vừa. |
| `rock-small-v4` | 8,0 | 8,0 | 2/2/2/1,5/2 | 9,5 | 9,5 | Phiến dẹt đọc rõ; mặt trên hơi rộng, mép phải dựng mạnh. |
| `rotten-log-v3` | 8,4 | 8,1 | 2/1,5/2/2/2 | 9,5 | 9,5 | Vỏ xếp lớp và miệng rỗng tốt; dương xỉ còn chi tiết nhỏ. |
| `rotten-log-v4` | 8,4 | 8,2 | 2/1,5/2/2/2 | 9,5 | 9,5 | Dáng cong/chạc mạnh, miệng rỗng tách rõ; cùng hạn chế lá nhỏ. |
| `tree-stump-v3` | 8,3 | 8,1 | 2/2/2/2/2 | 10 | 9,5 | Rễ bạnh và vành gãy tốt; vòng tuổi nhỏ bớt rõ ở 128. |
| `tree-stump-v4` | 8,3 | 8,2 | 2/2/2/2/2 | 10 | 9,5 | Mặt cắt, rễ và vỏ già cùng đọc được. |

Ở các hàng Q đầy đủ 10 và Q 128 9,5, tiêu chí đọc được giảm từ 2 xuống 1,5 do chi tiết nhỏ mất khi thu; bốn tiêu chí còn lại giữ nguyên. Các hàng Q đầy đủ 9,5 giữ cùng phân bổ ở 128. Không có ảnh dưới ngưỡng sau ba lượt.

## 6. KA1 và tính toàn vẹn

- Mốc trước lượt tiếp nối: **405 → 437 file; thêm 32, đổi 0, mất 0**.
- Mốc đầu hồ sơ 118 cũ: **256 → 437 file; thêm 181, đổi 0, mất 0**.

Mốc tiếp nối có đúng **32 file thêm của phiếu này**: 12 PNG lượt sinh, 4 prompt sửa mới, 8 PNG chọn và 8 prompt chọn. So mốc hồ sơ cũ có 181 dòng thêm vì giữa hai phiên còn có tài nguyên của phiếu khác; không nhận các tài nguyên ấy là sản phẩm 118. Cả hai diff chỉ có dòng dữ liệu thêm, không có dòng dữ liệu bớt hay đổi. Mọi file được chụp bằng `md5 -r` đệ quy trên toàn `scenery/`, trước khi ghi ở phiên tương ứng và sau khi giao.

12/12 bản `.tryN.png` trùng SHA-256 và nguyên byte với nguồn `image_gen`. 8/8 bản chọn trùng SHA-256 với ảnh đã đo; prompt chọn chép từ prompt của đúng lượt. Tám prompt try1 được chuẩn bị trước có newline cuối file, nội dung gửi lấy từ manifest cùng văn bản; các prompt sửa được gửi nguyên nội dung file.

- [MD5 trước lượt tiếp nối](../../games/typing-defense/art-src/_review/118/resume-20261029/md5-before.txt)
- [MD5 sau giao](../../games/typing-defense/art-src/_review/118/resume-20261029/md5-after.txt)
- [Diff lượt tiếp nối](../../games/typing-defense/art-src/_review/118/resume-20261029/md5-resume-diff.txt)
- [Diff từ mốc cũ](../../games/typing-defense/art-src/_review/118/resume-20261029/md5-initial-diff.txt)
- [Đối chiếu nguồn và bản giao](../../games/typing-defense/art-src/_review/118/resume-20261029/audit.json)
- [Số đo bản giao](../../games/typing-defense/art-src/_review/118/resume-20261029/final-metrics.json)
- [Khác biệt biến thể](../../games/typing-defense/art-src/_review/118/resume-20261029/pairs.json)
- [Kết quả magick identify](../../games/typing-defense/art-src/_review/118/resume-20261029/identify-delivered.txt)
- [Nhật ký gọi công cụ và ảnh tham chiếu](../../games/typing-defense/art-src/_review/118/resume-20261029/tool-calls.json)

## 7. Script, phần không làm và việc cần duyệt

Script đã chạy đều trong `_review/118/`; phần mới nằm ở `resume-20261029/`:
- `pipeline.mjs process`: tách nền/đặt khung ứng viên ban đầu; `pipeline-final.mjs review` và `publish`: tờ trước/sau, tờ nhỏ và giao bản chọn, từ chối ghi đè.
- `keep-native-log.mjs`: giữ kích thước và dịch khúc gỗ v4 1 px; `sheet-complete.mjs`: tờ so đủ mép.
- `mock-final.mjs`: cảnh kiểm cuối; `audit.py`: MD5, đối chiếu byte, tổng hợp số đo và bản sao báo cáo cũ; `report.py`: báo cáo này. `measure.mjs` của hồ sơ cũ đo hộp bao, vùng liền, nền và luma.
- `pipeline.mjs review` và `mock.mjs` cũng đã chạy cho tờ kiểm đầu; giữ chúng và kết quả trung gian để truy nguyên. Không dùng chúng để chọn nhầm bản gỗ v4 đã thu nhỏ.

Lệnh mẫu (chạy từ repo cha, trên đường dẫn đầu ra chưa tồn tại):
```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/118/resume-20261029/pipeline.mjs process
node games/typing-defense/art-src/_review/118/resume-20261029/keep-native-log.mjs
node games/typing-defense/art-src/_review/118/resume-20261029/pipeline-final.mjs review
node games/typing-defense/art-src/_review/118/resume-20261029/mock-final.mjs
node games/typing-defense/art-src/_review/118/resume-20261029/sheet-complete.mjs
```
Các script dùng `mkdir` và ghi độc quyền để không đè kết quả; chạy lại trong bản sao thư mục kiểm sạch hoặc đổi thư mục đích. Phép tách nền tương đương được ghi đầy đủ trong script; không chạy `prepare-scenery` hay thay cấu hình game.

**Không làm:** tích hợp runtime và tắt viền mực là việc Claude theo phiếu; không xóa v1/v2 hay `.try*`, không sửa danh sách nâng ảnh của game vì ngoài đường dẫn cho phép, không chạy build/test hoặc trình duyệt. Đây là ảnh nguồn và tờ kiểm, không có capture trình duyệt/raw frame cần dọn. Không làm âm thanh.

**Claude/chủ dự án cần xem:** PNG giao ở cỡ đầy đủ, `118-small.jpg`, tám tờ trước/sau, `118-sheet-complete.jpg` và `118-vs-ref.jpg`; chấm lại M/Q, chú ý nét cọ rêu của đá nhỏ v3 và dương xỉ trên gỗ ở cỡ chơi. Khi tích hợp dùng bộ v3/v4 không viền mực; giữ bộ cũ trên đĩa.
