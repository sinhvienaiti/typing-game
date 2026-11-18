# Phiếu 155 · Dragonhold · Đường đá núi

Ngày giao: 29/10/2026. Công cụ sinh: **image_gen tích hợp của Codex**. Đã có ba bản chọn: đá lát, vai đường và tờ tám decal. Kiểm kỹ thuật mục 2–7 đạt; Codex tự chấm M ≥ 8, Q ≥ 8 trên bản hậu kỳ. **Chờ Claude chấm lại; chưa ghi nhận là đã được Claude nhận.**

## 1. Tệp giao

Thư mục ảnh: [ground-v3/road](../../games/dragon-hold/art-src/ground-v3/road/).

| Bản chọn | Khổ và kênh | Nguồn chọn |
|---|---|---|
| [road-flagstone.png](../../games/dragon-hold/art-src/ground-v3/road/road-flagstone.png) | 1024 × 1024, sRGB, RGB, không alpha | `road-flagstone.try2.png` |
| [road-verge.png](../../games/dragon-hold/art-src/ground-v3/road/road-verge.png) | 1024 × 1024, sRGB, RGB, không alpha | `road-verge.try2.png` |
| [road-edges.png](../../games/dragon-hold/art-src/ground-v3/road/road-edges.png) | 2048 × 1024, sRGB, RGBA; lưới 4 × 2 | `road-edges-left.try1.png` + `road-edges-right.try1.png` |
| [road-edges.alpha.png](../../games/dragon-hold/art-src/ground-v3/road/road-edges.alpha.png) | Cùng dữ liệu RGBA với `road-edges.png` | Bản cùng nội dung cho đường dẫn `.alpha.png` |

Mọi lượt sinh giữ nguyên `.tryN.png` và `.tryN.prompt.txt`. Bản chọn có `.prompt.txt` bên cạnh; bản `.alpha.png` cũng có `road-edges.alpha.prompt.txt`. Hai tờ nguồn trái/phải có bản chọn và prompt riêng. Ảnh nguồn image_gen trả về 1254² được giữ nguyên; chỉ bản hậu kỳ mới đổi về khổ giao.

Thứ tự atlas, đọc từ trái sang phải:

| Hàng / cột | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Trên | 1 · Hàng đá bờ thẳng | 2 · Hàng đá bờ cong | 3 · Phiến vỡ tràn cỏ | 4 · Quạt sỏi |
| Dưới | 5 · Cỏ trùm mép đá | 6 · Vệt bánh xe có nước | 7 · Rêu sẫm và lá thông | 8 · Ba bậc đá |

Mỗi ô 512² tương ứng 4 m. Ghép bốn ô của tờ trái thành hàng trên, bốn ô của tờ phải thành hàng dưới; không nối ngang nguyên hai tờ vuông. Hai tệp atlas giao đều có alpha thật; mặt nạ xám riêng nằm ở `_review/155/road-edges-mask.png`.

## 2. Đọc trước và các lượt sinh

Đã xem ảnh mẫu chủ dự án, cỏ `grass-a.webp` và bản ghép `120-composite-selected-final.jpg`; đọc và đo tám ô nền `public/assets/dragon-hold/ground/pine-river/*.webp`, đọc `PATH_QUALITY.md`, `ART_ACCEPTANCE.md` §5 và Bible Dragonhold. Giữ đá kem, bóng đá lam xám, rêu và cỏ ô liu; không chép cảnh của ảnh mẫu. Phong cảnh 120 chỉ dùng để đối chiếu bảng màu, không ghép vào texture.

Thư mục đã có `road-flagstone.try1.png`, prompt lượt một của hai ô, `base-prompt.txt` và `md5-before.txt` lúc bắt đầu phiên này. Tất cả giữ nguyên. Lượt một đá lát có sẵn được tính vào giới hạn ba lượt.

| Ảnh / lượt | Prompt và kết quả | Quyết định |
|---|---|---|
| Đá lát · 1, có sẵn | Phiến dài, hai vệt bánh xe và rêu đúng đề. Hạt khoáng dày làm năng lượng gradient ngang/dọc chỉ **1,0344**. | Giữ nguồn, không chọn. |
| Đá lát · 2 | Giữ nguyên STYLE + MAP + TOP và phần riêng; sửa phần bổ sung: mặt đá mòn yên hơn, mảng khoáng rộng, phiến dài khoảng 4:1, khe dọc mạnh, giảm hạt li ti. Hai vệt mòn vẫn chạy dọc. | Chọn. Tỷ số nguồn **1,5166**, sau hậu kỳ **1,5466**. |
| Vai đường · 1 | Sinh bằng prompt lượt một đã có. Đủ đất, sỏi, đá vỡ, cỏ nhưng luma **0,3884**, thấp hơn cỏ **0,4647**. | Giữ nguồn. Không tăng sáng hàng chục phần trăm để ép số. |
| Vai đường · 2 | Giữ nguyên các khối bắt buộc; đổi phần bổ sung sang vai sỏi bạc sáng, khoảng hai phần ba là mảnh hoa cương và đất khoáng sáng, đất sẫm lộ trong khe, cỏ ô liu thành cụm. | Chọn. Nguồn **0,5396**; sau sửa mép **0,5487**, không chỉnh sáng. |
| Decal trái · 1 | STYLE + MAP + TOP + bốn món 1–4 + dòng nền M nguyên văn. Đính kèm hai texture đã chọn và câu “Use the attached images only for material and colour. Paint the new pieces as described.” | Chọn ngay; thẳng, cong, phiến vỡ, sỏi đều đủ. |
| Decal phải · 1 | Cùng cấu trúc, bốn món 5–8; đúng hai ảnh tham chiếu chất liệu trên. Nước phản trời lam lạnh, khe rêu sẫm, đúng ba bậc. | Chọn ngay. |

Phiên này gọi image_gen **5 lần**; cộng lượt đá lát có sẵn là 6 ảnh nguồn. Mỗi ô đất dùng hai lượt, mỗi tờ decal dùng một lượt; không cần lượt ba. Prompt gửi nguyên văn được lưu cạnh từng ảnh và trong [prompt-archive.json](../../games/dragon-hold/art-src/_review/155/prompt-archive.json). [generation-manifest.json](../../games/dragon-hold/art-src/_review/155/generation-manifest.json) ghi nguồn, tham chiếu và lựa chọn.

## 3. Hậu kỳ và đối chiếu §5

Hai ô đất: đổi cỡ nguồn về 1120², ghép dải chồng 96 px bằng đường cắt có chênh màu nhỏ nhất, hòa 3 px mỗi bên đường cắt để ra ô 1024². Chỉ dùng hai dải của chính ảnh nguồn, không vẽ thêm hoặc san phẳng mặt đá. Sau đó dịch vòng nguyên pixel để vị trí xuất ô có trung bình hai dải mép tương đồng. Phần giữa giữ chất liệu và độ tương phản đã vẽ.

Đá lát tăng sáng toàn ảnh **6 %**, trong giới hạn ±10 %. Có 267 kênh màu bị chặn ở 255 trên 3.145.728 kênh, tương đương **0,0085 %**; không thấy mất mảng sáng hay bạc chất đá. Vai đường không tăng sáng. Không dùng gamma để san màu. Các vị trí dịch vòng và thông số nằm trong [tile-processing.json](../../games/dragon-hold/art-src/_review/155/tile-processing.json).

Decal: tách từng ô, thu toàn ô còn 90 % để thêm lề, không cắt phần vẽ; khóa màu magenta, rồi làm mềm alpha **8 px vào trong** bằng khoảng cách tới nền. Lòng đá, nước, rêu vẫn nguyên màu; RGB tại pixel alpha 0 đặt về 0. Không phủ màu chống viền lên phần vẽ. Không thấy quầng hồng trên nền sáng hoặc tối. Lá/cỏ cực mảnh sát ngoài cùng dịu đi theo dải alpha bắt buộc; các khối cỏ chính còn nguyên.

Tờ **bản sinh | bản hậu kỳ**, hai bên cùng cỡ:

- [Đá lát](../../games/dragon-hold/art-src/_review/155/road-flagstone-before-after.jpg).
- [Vai đường](../../games/dragon-hold/art-src/_review/155/road-verge-before-after.jpg).
- [Tám decal](../../games/dragon-hold/art-src/_review/155/road-edges-before-after.jpg): bên trái là tám ô nguồn đã sắp đúng hàng; bên phải là atlas alpha trên cỏ hiện dùng.
- [Alpha trên nền tối](../../games/dragon-hold/art-src/_review/155/road-edges-dark.jpg), [trên nền sáng](../../games/dragon-hold/art-src/_review/155/road-edges-light.jpg).

Không có ngưỡng số nào buộc phải phá tranh. Không xóa hay thay phần vẽ để đạt số. Điểm bên dưới chấm bản hậu kỳ và bản ghép, không lấy điểm của nguồn sinh thay cho ảnh giao.

## 4. Số đo bắt buộc

Luma dùng **Y′ sRGB = (0,2126 R′ + 0,7152 G′ + 0,0722 B′) / 255**, không giải mã về ánh sáng tuyến tính. Gradient là sai phân bậc nhất; năng lượng là tổng bình phương sai phân. Dải mép là hiệu tuyệt đối giữa trung bình của hai dải đối diện rộng 8 px. Các định nghĩa được dùng thống nhất cho nền cũ và ảnh mới.

| Kiểm | Kết quả | Mức yêu cầu |
|---|---:|---|
| Đá lát / vai đường | 1024² / 1024², sRGB RGB | Đúng; không alpha |
| Atlas / atlas `.alpha` | 2048 × 1024, sRGB RGBA | Đúng; có alpha |
| Mock lớn / nhỏ | 2048 × 1152 / 1024 × 576 | Đúng |
| Dải mép đá lát · trái/phải | **0,00000822** | ≤ 0,03 |
| Dải mép đá lát · trên/dưới | **0,00002244** | ≤ 0,03 |
| Dải mép vai đường · trái/phải | **0,00001676** | ≤ 0,03 |
| Dải mép vai đường · trên/dưới | **0,00002843** | ≤ 0,03 |
| Gradient ngang/dọc đá lát · năng lượng | **1,5466** | ≥ 1,2 |
| Gradient ngang/dọc đá lát · tổng trị tuyệt đối, thêm để đối chiếu | **1,2390** | Cũng ≥ 1,2 |
| Luma cỏ `grass-a` | **0,464724** | Mốc nền đang dùng |
| Luma đá lát | **0,615246** | Sáng hơn cỏ |
| Đá lát trừ cỏ | **0,150522** | ≥ 0,12 theo phiếu; cũng ≥ 0,15 theo PATH_QUALITY |
| Luma vai đường | **0,548708** | Nằm giữa cỏ và đá lát |
| Pixel màu tín hiệu · đá lát | **0,000191 %** | ≤ 2 % |
| Pixel màu tín hiệu · vai đường | **0,008488 %** | ≤ 2 % |
| Pixel alpha > 0 còn mang magenta | **0 / 650.768 = 0 %** | ≤ 0,2 % |
| Pixel alpha trung gian | **102.857** | Chỉ trong dải mép |
| Khoảng cách xa nhất của alpha trung gian tới alpha 0, kiểm độc lập | **8,4853 px** | Trong dải 12 px |
| Pixel alpha trung gian ngoài dải 12 px | **0** | Bên ngoài chỉ 0 hoặc 255 |
| Decal trên tờ thử | **12 món**, có đủ tám loại | 10–14 món |

Số đầy đủ: [metrics.json](../../games/dragon-hold/art-src/_review/155/metrics.json), [verification.json](../../games/dragon-hold/art-src/_review/155/verification.json), [decal-processing.json](../../games/dragon-hold/art-src/_review/155/decal-processing.json). `magick identify` đã xác nhận khổ, sRGB và số kênh; `verify.cjs` kiểm alpha từ tệp đã xuất, không dùng lại bản đồ khoảng cách của bước tách nền.

Luma các ô đang dùng còn lại: đất 0,2915; cỏ B 0,4186; rêu 0,4347; đường cũ 0,5669; lá thông 0,2904; cát sông 0,7353; đá 0,3997. Các ô cũ giữ nguyên.

Đã xem hai bản `-roll +512+512` ở cỡ 1024²: **không thấy đường nối thẳng** ở giữa ảnh. Phiến vẫn liền khối, rêu không thành sọc phủ ngang. Vai đường vẫn là các cụm sỏi và đá vỡ, không có đường phân màu hình chữ thập. Có thêm tờ lát 2 × 2 để kiểm lặp:

- [Đá lát dịch nửa ô](../../games/dragon-hold/art-src/_review/155/road-flagstone-roll.jpg), [lát 2 × 2](../../games/dragon-hold/art-src/_review/155/road-flagstone-tile2x2.jpg).
- [Vai đường dịch nửa ô](../../games/dragon-hold/art-src/_review/155/road-verge-roll.jpg), [lát 2 × 2](../../games/dragon-hold/art-src/_review/155/road-verge-tile2x2.jpg).

## 5. Tờ thử và điểm M/Q

[Tờ thử 2048 × 1152](../../games/dragon-hold/art-src/_review/155-mock.jpg) · [bản 1024 × 576](../../games/dragon-hold/art-src/_review/155-mock-small.jpg) · [cắt đoạn cong](../../games/dragon-hold/art-src/_review/155/mock-corner-detail.jpg) · [cắt ngã ba](../../games/dragon-hold/art-src/_review/155/mock-junction-detail.jpg).

Tờ thử lát đúng `grass-a.webp` đang dùng; lõi đá theo UV dọc đường chữ S và nhánh ngã ba; vai đường có mép nhiễu độc lập hai bên. Lõi từng nhánh rộng **4–5 m**, thay đổi dọc đường; ngã ba mở rộng theo hai nhánh gặp nhau. Vai cơ sở rộng **0,46–0,66 m** mỗi bên. Rải 12 decal, dùng cả tám loại, xoay theo tiếp tuyến đường. Mỗi ô decal biểu diễn 4 m. Cấu hình và tọa độ rải nằm trong [mock-layout.json](../../games/dragon-hold/art-src/_review/155/mock-layout.json).

**“Đường có trông như vệt quệt không?” — Không.** Ở cả hai cỡ, hàng phiến và khe đá đi theo khúc cua; rêu, sỏi, phiến vỡ, bờ đá và nước chia nhịp hai bên. Lõi đường có sắc kem, xám lạnh và hai dải mòn; vai đường có chất liệu riêng, không phải viền mờ đồng đều.

[Tờ so cùng chiều cao với ảnh chủ dự án](../../games/dragon-hold/art-src/_review/155-vs-ref.jpg): **đứng cạnh được về chất liệu đường và độ đọc ở xa**. Điểm M của các mảnh nền được chấm trên ảnh ghép theo ART_DIRECTION §1.4 và tiêu chí riêng của phiếu. Không chấm một tờ thử texture thành cảnh sử thi hoàn chỉnh: trời, mốc lớn và đèn game thuộc cảnh 3D, không được vẽ nung vào ô đất TOP.

| Bản hậu kỳ | M · cỡ đầy đủ / ảnh ghép lớn | Q · cỡ đầy đủ | M · tờ thử nhỏ | Q · tờ thử nhỏ |
|---|---:|---:|---:|---:|
| Đá lát | **8,2** | **9,5** | **8,1** | **9,0** |
| Vai đường | **8,0** | **9,0** | **8,0** | **9,0** |
| Tờ tám decal | **8,2** | **9,5** | **8,0** | **9,0** |

Q theo năm tiêu chí 0–2:

| Ảnh | Đúng đề | Đọc trong game | Hợp bộ | Hình khối | Dùng bước sau | Tổng |
|---|---:|---:|---:|---:|---:|---:|
| Đá lát | 2 | 2 | 1,5 | 2 | 2 | 9,5 |
| Vai đường | 2 | 1,5 | 1,5 | 2 | 2 | 9,0 |
| Decal | 2 | 1,5 | 2 | 2 | 2 | 9,5 |

Điểm chưa tới 9 ở M: nhịp phiến dài vẫn khá đều khi nhìn cả con đường; vai đường có nhiều sỏi sáng nên ở cỡ nhỏ gần màu lõi; một phần lá thông và cỏ mảnh chỉ góp chất liệu, không đọc thành từng lá. Cỏ nền đang dùng mềm và cách điệu hơn đá mới; không thay cỏ trong phiếu này. Bờ đá, phiến vỡ và vũng nước vẫn đọc rõ ở cỡ nhỏ. Đây là điểm tự chấm của Codex, cần Claude kiểm lại trên tệp đầy đủ và mock nhỏ.

## 6. KA1 và cách chạy lại

Không ghi đè mốc `md5-before.txt` có sẵn. Trước lần ghi đầu tiên của phiên, chạy **`/sbin/md5 -r` đệ quy mọi tệp trong art-src**, lưu thêm `md5-before-session.txt`. Sau khi xong media và script, chạy lại cùng lệnh; kết quả cuối ở [ka1-final.json](../../games/dragon-hold/art-src/_review/155/ka1-final.json).

| Mốc so | Tệp mốc | Tệp tại lần chụp cuối | Đổi nội dung | Mất | Chỉ thêm |
|---|---:|---:|---:|---:|---:|
| `md5-before.txt` có sẵn | 4.958 | 5.325 | **0** | **0** | **367** |
| `md5-before-session.txt` | 5.266 | 5.325 | **0** | **0** | **59** |

Các tệp thêm toàn art-src gồm cả công việc đồng thời của các làn khác; không coi toàn bộ số thêm là sản phẩm của phiếu này. Hai bản diff chỉ có dòng nội dung thêm, không có dòng nội dung xóa: [mốc gốc](../../games/dragon-hold/art-src/_review/155/md5-diff-original-final.txt), [mốc đầu phiên](../../games/dragon-hold/art-src/_review/155/md5-diff-session-final.txt). [md5-after-final.txt](../../games/dragon-hold/art-src/_review/155/md5-after-final.txt) chứa hash của tất cả tệp đã có tại lúc lấy danh sách. Bốn tệp kết quả của chính lần audit cuối được ghi sau đó, không tự hash đệ quy chính chúng.

Script chỉ nằm trong `_review/155/`. Chạy từ repo cha, không cần cài thư viện hoặc mạng:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/dragon-hold/art-src/_review/155/prompts.cjs
node games/dragon-hold/art-src/_review/155/ingest.cjs
node games/dragon-hold/art-src/_review/155/prepare.cjs tiles
node games/dragon-hold/art-src/_review/155/prepare.cjs proofs
node games/dragon-hold/art-src/_review/155/decals.cjs
node games/dragon-hold/art-src/_review/155/prepare.cjs metrics
node games/dragon-hold/art-src/_review/155/mock.cjs
node games/dragon-hold/art-src/_review/155/verify.cjs
python3 games/dragon-hold/art-src/_review/155/audit.py --tag kiem-lai-01
```

`ingest.cjs` chép nguyên byte từ nơi image_gen lưu mặc định; bỏ qua bước này khi đã có các `.tryN.png`. Prompt và nguồn sinh đều đã nằm trong thư mục giao. Các bước hậu kỳ có thể dựng lại đầu ra của phiên này nhưng bảo vệ mọi tệp có trong mốc đầu phiên. Audit chạy lại dùng tag mới để không ghi đè lần kiểm trước. Không chạy Git, dev server, trình duyệt, build hoặc bộ test game.

## 7. Chỗ khác phiếu và việc còn chờ

Không bỏ ảnh nào. Giữ lượt một đá lát và các tệp chuẩn bị có sẵn thay vì tạo lại hoặc đổi tên. Thêm mốc MD5 đầu phiên để chứng minh phần tiếp tục này không sửa tệp cũ. Giữ nguồn 1254² của công cụ, đổi đúng khổ ở bản hậu kỳ. Hai tên atlas giao cùng một ảnh RGBA để tránh nhầm `.alpha.png` là mặt nạ xám; mặt nạ riêng ở thư mục kiểm.

Không đưa media vào `public/assets`, không sửa mã R2, không thay cỏ và không sửa danh sách nâng ảnh dùng chung vì ngoài đường dẫn cho phép. Tờ thử là ảnh ghép bằng script, chưa phải bản chụp gameplay. Việc dựng độ lún, bờ đổ bóng, ánh sáng và kiểm ở các góc camera thật thuộc làn map R2 sau khi nhận media. Không đọc hoặc ghi khu vực Tu Tiên.

Chủ dự án/Claude cần xem trước **mock nhỏ**, **hai ảnh roll**, **tờ decal trên nền sáng/tối** và **ba tờ trước/sau**, rồi chấm lại M và Q. Trọng tâm xem lại là nhịp phiến lặp và độ phân biệt của vai sỏi ở xa. Chưa có điểm Claude hoặc chữ ký nhận của chủ dự án.
