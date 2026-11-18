# Phiếu 179 · Wordwoven · Năm vòng liền, bỏ lật gương

Ngày giao: 29/10/2026, Mac mini M4/macOS. Theo phiếu 114, 159, 179; mục «159, năm vòng» của bản chấm nhận 29/10b và ART_ACCEPTANCE §5. Dùng skill `imagegen`, công cụ tích hợp **image_gen**; không dùng API/CLI tạo ảnh.

**Đã giao bộ `.v3`: 16 ô 1536 × 1024, 8 alpha, 16 bản thu 384 × 256; đủ 9 ô mới, 5 dải khép vòng và 1 dải sửa bổ sung cho 220. Không xếp gương trong vòng. Tự chấm M = 8 trên các vòng hậu kỳ, Q = 8–9 từng ô. Còn ngoại lệ kỹ thuật: biến thiên nét sương nguồn vượt 3/255 và 28 pixel tím đục rời; không tự tuyên bố đạt nguyên văn hai chốt này. Claude duyệt rồi mới đổi tên đang dùng.**

## 1. Bộ giao và thứ tự gắn

Ảnh ở [backdrops/w1-silverfall-epic/](../../games/typing-defense/art-src/backdrops/w1-silverfall-epic/). Mỗi PNG có `.prompt.txt` cùng tên. Giữ đủ `.v3.try1.png` và prompt của cả chín lượt sinh ô mới; không đụng bản chính, `.v2`, bản sinh hay prompt cũ.

| Vòng | Thứ tự trái → phải, mỗi tên thêm `.v3.png` | Nguồn giữ lại |
| --- | --- | --- |
| Ngày | `sky-day-a`, `sky-day-b`, `sky-day-c`, `sky-day-d` | a từ `.v2`; b từ `.v2` lật theo nguyên văn bản chấm. c nối b, d nối c. |
| Đêm | `sky-night`, `sky-night-b`, `sky-night-c`, `sky-night-d` | Ô đầu từ `sky-night.v2`, chứa trăng duy nhất. b–d sinh nối tiếp; **không dùng `sky-night-b.v2`**. |
| 320 m | `layer-320`, `layer-320-2`, `layer-320`, `layer-320-2` | L từ `.v2`; L2 mới, không lật. |
| 220 m | `layer-220`, `layer-220-2`, `layer-220`, `layer-220-2` | L từ `.v2`; L2 mới, không lật. |
| 140 m | `layer-140-a`, `layer-140-b`, `layer-140-c`, `layer-140-d` | a từ `.v2`; b từ `.v2` lật để giữ mối tốt; c nối b, d nối c. |

Với tám ô núi, dùng **`.v3.alpha.png`** để chồng lớp. Các file b đã lưu sẵn chiều hiển thị; **không lật thêm khi gắn**. Thứ tự tên alpha đầy đủ nằm trong [manifest.json](../../games/typing-defense/art-src/_review/179/manifest.json).

Các ô có thêm `.v3.384.png` để xem nhỏ. Tổng PNG mới cạnh bộ cũ: **49** = 16 bản chọn + 8 alpha + 16 bản thu + 9 bản sinh. Cộng prompt: **98 file**.

## 2. Sinh nối tiếp và hậu kỳ

Tổng **15 lượt image_gen**: 9 ô, 5 dải khép và 1 dải sửa 220. Mỗi kết quả sinh được giữ nguyên byte với prompt nguyên văn; các dải nằm trong [_review/179/](../../games/typing-defense/art-src/_review/179/), không lẫn vào tên tài sản đang dùng. Không dùng lượt sinh thứ hai hoặc thứ ba cho ô nào.

Chín đầu vào đều có canvas **1536 × 1024**: 384 cột trái lấy đúng 25% mép phải ô trước, theo chiều hiển thị; phần còn lại là magenta đối với núi, màu trời theo hàng đối với trời. Prompt bắt đầu nguyên văn:

```text
Continue this panorama to the right: the left quarter of the attached image is fixed and must stay unchanged; paint the rest as the same scene continuing naturally to the right, with the same light, haze, colours, skyline height band and bottom haze. A different arrangement of towers and clouds, never a mirror of the left part. Rice terraces are deep jade green and muted ripe gold, not lemon yellow.
```

Với trời, thay hai câu cuối bằng `A different arrangement of clouds, never a mirror of the left part.` như chỉ dẫn bỏ towers/terraces. Phần bổ sung khóa khổ, hướng nhìn, màu, vùng yên và chi tiết riêng từng lớp. Ô đêm mới yêu cầu không trăng, Ngân Hà tiếp từ ngữ cảnh và đèn thưa dần. Toàn bộ đầu vào/prompt ở [inputs/](../../games/typing-defense/art-src/_review/179/inputs/).

**Cách lấy ô mới:** cắt `1152x1024+384+0`, đổi cỡ ngang Lanczos về 1536 × 1024; không cắt đỉnh hay đáy tranh. Đây là lựa chọn cho chỗ chưa rõ của phiếu: canvas 1536 có 384 cột ngữ cảnh nên phần mới chỉ còn 1152 cột, trong khi ô giao vẫn cần rộng 1536. Có giãn ngang 4/3; không gọi đó là giữ nguyên tỉ lệ. Hình khối sau đổi cỡ được xem lại trong tờ nguồn/hậu kỳ.

Tại mối nối tiếp, dùng lại phần ngữ cảnh đã được image_gen sửa ở mép phải ô trước, hòa cosin 192 px phía trên và 224 px ở sương đáy; giữ phần giữa. Không chép lại 25% ngữ cảnh vào đầu ô mới, nên không lặp cả cụm núi ở mối.

**Khép vòng:** mỗi đầu vào 768 × 1024 gồm 384 cột cuối ô cuối ở trái và 384 cột đầu ô đầu ở phải. Sửa vùng giữa x = 154…613 rồi chỉ lấy **230 px mỗi ô**, tương tự 159. Núi hòa cosin 64 px ở trên, tăng mềm lên **224 px dưới y = 870**; trời dùng **224 px toàn chiều cao**. Nguồn dải có khổ 1086 × 1448, thu Lanczos về 768 × 1024, giữ tỉ lệ 3:4.

Hai ô 140 giữ cổng, thác, bậc thang và phần giữa. Riêng sương dưới 85%, hòa phần sửa cũ về sương của bản sinh 114 bằng cosin ngang **224 px**, thay vai hòa 32 px của 159. Không lấy một màu trung bình rồi đổ lên sương. [Kiểm nguồn](../../games/typing-defense/art-src/_review/179/source-preservation-and-fog.json) xác nhận **1.076 cột giữa của cả bảy ô giữ lại trùng RGB/alpha với nguồn `.v2` theo đúng chiều hiển thị**.

**Một sửa bổ sung sau kiểm:** lượt L2 của 220 để lại vách bắt đầu bằng cạnh đứng tại mối L → L2, lặp ở hai phía vòng. Sinh `forward-220.v3.try1.png`, chỉ ghép cùng dải 230 px mỗi bên; vách nay chạy liền. Vì vậy có **6 dải sửa**, hơn ước tính năm dải của phiếu. [Tờ nguồn/hậu kỳ của dải bổ sung](../../games/typing-defense/art-src/_review/179/raw-vs-final-final-r2/forward-220.jpg).

Tách nền bằng `tools/art-normalize/normalize.py key-alpha`, tương đương wrapper `key-alpha.sh`:

```text
ART_MAGICK=/opt/homebrew/bin/magick
--bg #FF00FF --mode global --despill protect-interior --no-key-hue
```

WORK chuyển vào `_review/179/normalize-work/` bằng runner; không sửa công cụ và không ghi vào thư mục công cụ. Cảnh báo góc dưới còn alpha là đúng: sương kín đáy. Không đổi gamma, tô mảng, san núi hoặc phủ sáng/tối lên tranh. Phép nhân RGB đêm **0,36 / 0,45 / 0,58** chỉ áp cho núi trong ảnh kiểm, không nằm trong PNG giao.

## 3. Tờ so, góc nhìn và tự chấm

[179-ring.jpg](../../games/typing-defense/art-src/_review/179-ring.jpg): năm vòng chồng lớp theo thứ tự trời → 320 → 220 → 140, cạnh ảnh tham chiếu chủ dự án; mỗi vòng có nhận xét riêng. Vòng 320/220 chồng tới chính lớp đó; hàng ngày/đêm/140 chồng đủ ba lớp. Không thêm rùa đã nhận vào phép kiểm mối nối.

[checks-final-r2/](../../games/typing-defense/art-src/_review/179/checks-final-r2/) giữ vòng nguồn **6144 × 1024**, vòng chồng lớp, bốn góc 90° tại các mối và bốn góc giữa ô. Tờ `*-90deg-1to1.jpg` có tám crop **1536 × 1024**, không thu nhỏ phần hình; bản `isolated` xem từng lớp riêng, bản `stack` xem chồng lớp. `*-120deg-1to1.jpg` kiểm lặp chi tiết ở bốn hướng, mỗi crop **2048 × 1024**.

| Vòng hậu kỳ | Nhận xét | M |
| --- | --- | ---: |
| Ngày | **Liền như một dãy núi**; không còn cặp cụm mây soi gương. Mối khép chuyển vàng sang kem mềm hơn sau hòa 224 px; nguồn a vẫn nhạt hơn các ô mới. | 8 |
| Đêm | **Liền như một dãy núi**; đúng một trăng; đèn nhiều quanh trăng rồi thưa; không sọc tối 115 px hay Ngân Hà gập do lật ảnh. Dải sao chuyển hướng theo từng đoạn, cần người chấm xem toàn vòng. | 8 |
| 320 | **Liền như một dãy núi**; đỉnh và yên núi nối tự nhiên, không cặp đỉnh soi gương. Hai ô lặp đúng ở 180°. | 8 |
| 220 | **Liền như một dãy núi**; đã bỏ vách cắt L → L2; thác và ruộng có hướng, không tháp sinh đôi quanh mối. | 8 |
| 140 | **Liền như một dãy núi**; cổng một lần, c–d khác bố cục, không cạnh sương đứng của 159. Ruộng b/c/d vẫn sáng và nhiều hơn a. | 8 |

Đã xem các crop mối, cảnh chồng lớp và mép alpha; không thấy vết cắt cảnh hoặc trục gương. Không thấy cả một tháp/cụm mây giống nhau hai lần trong góc 120°; 320/220 chỉ lặp lại sau 180°. Đây là nhận xét thị giác, không suy ra chỉ từ số đo MAE.

**30 tờ «bản sinh | bản hậu kỳ»** ở [raw-vs-final-final-r2/](../../games/typing-defense/art-src/_review/179/raw-vs-final-final-r2/): 16 PNG đục, 8 alpha trên magenta để đối chiếu và 6 dải sửa. Với ô mới, bên nguồn giữ cả 25% ngữ cảnh; bên hậu kỳ đã cắt ngữ cảnh, nên vị trí/độ rộng núi khác đúng phép cắt/đổi cỡ đã nêu. Hai bên cùng cỡ, không đánh tráo bản sinh và bản giao. Nguồn b cũ được lật cùng chiều hiển thị trước khi so.

Q theo đúng đề / đọc được / hợp bộ / hình khối / dùng cho bước sau; chấm bản hậu kỳ đầy đủ và bản thu 384 px:

| Ô `.v3` | Q đầy đủ / 384 px | Thành phần | Trừ điểm chính |
| --- | --- | --- | --- |
| `sky-day-a` | 8,5 / 8,5 | 2/2/1,5/2/1 | Sương kem nhạt hơn trời mới. |
| `sky-day-b` | 9 / 9 | 2/2/2/2/1 | Giữ ô cũ, chỉ sửa mép. |
| `sky-day-c` | 9 / 9 | 2/2/2/2/1 | Mây hoàn thiện; có giãn ngang khi lấy ô mới. |
| `sky-day-d` | 9 / 9 | 2/2/2/2/1 | Như c; chuyển sắc khép vòng cần Claude xem. |
| `sky-night` | 8,5 / 8,5 | 2/2/1,5/2/1 | Mật độ đèn cao hơn phần còn lại, đúng điểm nhấn trăng. |
| `sky-night-b` | 9 / 9 | 2/2/2/2/1 | Không trăng, nối từ ô trăng. |
| `sky-night-c` | 9 / 9 | 2/2/2/2/1 | Ngân Hà/đèn thưa, không mirror. |
| `sky-night-d` | 9 / 9 | 2/2/2/2/1 | Đoạn yên rộng, khép về vùng có đèn. |
| `layer-320` | 8 / 8 | 1,5/2/1,5/2/1 | Giữ tầm đỉnh và độ đậm nguồn; không sửa để ép mốc cũ. |
| `layer-320-2` | 8,5 / 8,5 | 2/2/1,5/2/1 | Núi hơi đậm/chi tiết hơn L. |
| `layer-220` | 8,5 / 8,5 | 2/2/1,5/2/1 | Ruộng vẫn vàng sáng; một pixel tím rời. |
| `layer-220-2` | 8,5 / 8,5 | 2/2/1,5/2/1 | Như L; vách đã sửa liền. |
| `layer-140-a` | 8,5 / 8,5 | 2/2/1,5/2/1 | Còn ngoại lệ số sương và pixel tím. |
| `layer-140-b` | 8 / 8 | 2/2/1/2/1 | Ruộng sáng, dày hơn a; giữ theo chỉ dẫn. |
| `layer-140-c` | 8,5 / 8,5 | 2/2/1,5/2/1 | Ruộng/rừng dày, thác vẫn đọc ở 384 px. |
| `layer-140-d` | 8,5 / 8,5 | 2/2/1,5/2/1 | Điểm cao thấp khác c, nhưng ruộng còn vàng sáng. |

M là điểm cảnh vòng **sau hậu kỳ**, không lấy điểm tranh sinh lẻ thay cho vòng. Chưa tới M 9 của tham chiếu: vẫn nhiều ruộng/rừng, sắc vàng sáng và ít tiền cảnh thật. Không sửa tài liệu `ART_REPLACE_LATER.md` vì ngoài phạm vi ghi của phiếu; các điểm cần nâng đã ghi ở đây.

## 4. Số đo thật và ngoại lệ giữ tranh

[measurements-final-r2.json](../../games/typing-defense/art-src/_review/179/measurements-final-r2.json) và [source-preservation-and-fog.json](../../games/typing-defense/art-src/_review/179/source-preservation-and-fog.json).

- 16 ô và 8 alpha đúng **1536 × 1024**; alpha min/max **0/255**. 16 bản thu đúng **384 × 256**.
- Tất cả tám alpha có **0 pixel khác 0 ở 80 hàng đầu**. Nền khóa chỉ xét phía trên núi; không đòi magenta ở sương/đáy/hai cạnh bên.
- Không có mối đối xứng hoàn toàn trong 20 mối vòng. MAE đối xứng lấy mẫu ±384 px quanh mối từ **8,7 đến 49,1/255** ở bản kiểm đầu; số cuối đầy đủ trong JSON. Chỉ dùng số để hỗ trợ xem tranh, không coi MAE khác 0 là chứng minh hết đối xứng thị giác.
- [Alpha ×2 sáng/tối](../../games/typing-defense/art-src/_review/179/alpha-detail-2x.jpg); các tờ toàn ảnh ×2 của từng ô nằm ở `checks-final-r2/edge-*-2x.jpg`. Không thấy quầng hoặc viền hồng liên tục; giữ rim sáng và núi lam có sẵn trong tranh.

**Ngoại lệ 3/255 của sương:** dốc ngang đã dùng 224 px. Tại ranh ngoài dải nối x = 230/1306, dưới y = 870, 320 và 220 có bước màu tối đa **1–3/255**, đạt. 140-a có **9/11**, b **2/1**, c **14/6**, d **6/8**. Các cực đại này **đã có trong nét sương/đá nguồn**: bước kênh sau trừ bước kênh nguồn tại ranh bằng **0** ở cả tám ô núi. Nếu kiểm thêm cột x = 224, cực đại 140-c là **18/255**. Không san nét đá/sương để ép mọi hàng xuống 3: dừng phần ép số theo ART_ACCEPTANCE §5, giữ tranh và gửi Claude quyết ngoại lệ. Không ghi chốt này là đã qua ở a/c/d.

**Ngoại lệ màu tín hiệu:** tám alpha còn pixel hue 285–330°, S > 0,5 theo thứ tự 320 L/L2 = **0/0**; 220 L/L2 = **1/1**; 140 a/b/c/d = **7/6/3/10**. Tổng **28 pixel đục**, không phải chỉ alpha rất nhỏ; từng tọa độ/RGBA nằm trong hồ sơ. Không thấy thành viền ở cỡ thật; vẫn **chưa đạt nguyên văn 0% của 114**. Không quét lại sơn trong lòng vật để lấy số 0. Bản chấm 29/10b đã nhận ngoại lệ pixel tím rời ở nguồn cũ; các ô mới vẫn cần Claude xem theo số thực này.

Không áp lại các ngưỡng đã bỏ: mép 8% lặng, sai khác ≤6/255 giữa hai dải trời, ≤5% cột alpha mềm, mốc đường núi 60/62%, magenta bốn mép. Không dùng ngoại lệ kỹ thuật để giấu mối hỏng: vách 220 đã được sửa bằng ảnh mới trước khi giao.

## 5. KA1, tái lập và việc bỏ qua

MD5 `/sbin/md5 -r`, toàn bộ `art-src/backdrops/` đệ quy: **112 → 210 file, thêm 98, sửa 0, xóa 0**. [Trước](../../games/typing-defense/art-src/_review/179/md5-before.txt), [sau](../../games/typing-defense/art-src/_review/179/md5-after.txt), [diff chỉ thêm](../../games/typing-defense/art-src/_review/179/md5-diff.txt), [audit](../../games/typing-defense/art-src/_review/179/md5-audit.json). Manifest ghi SHA-256 của từng PNG chọn.

[Kiểm bản giao](../../games/typing-defense/art-src/_review/179/delivery-audit.json): 16 ô, 8 alpha, 16 bản thu, 9 bản sinh và 30 tờ so; **0 lỗi** khổ, hash, prompt thiếu hoặc liên kết báo cáo hỏng. PNG chọn/alpha trùng byte stage đã chấm. Kiểm này không thay hai ngoại lệ nghệ thuật/kỹ thuật ở mục 4.

Script: `work.py` là phần chuẩn bị đã có trong hồ sơ 179, được dùng tiếp nguyên trạng; bổ sung `continue.py`, `review-v3.py`, `measure-v3.py`, `finish-v3.py`. Chốt từ **`final-r2/`**. `final/`, `checks/`, `raw-vs-final/` là lần kiểm trước khi sửa vách 220 và nới hòa trời; giữ đối chứng, **không phải bản giao**. Các writer từ chối ghi đè; muốn dựng lại cần dùng thư mục/tên mới và cập nhật biến stage tương ứng.

Không chờ phiếu khác; không sửa runtime hay chuyển bản chính. Không làm lại rùa/bóng đã nhận, không sinh âm thanh/model, không sửa game khác hoặc Tu Tiên. Không chạy Git, build, test suite, server, trình duyệt hay mạng ngoài image_gen. Không có browser/render capture hoặc raw frame cần prune; nguồn sinh và hồ sơ hậu kỳ khoảng **539 MB**, giữ theo luật lưu mọi lượt sinh và đối chứng hậu kỳ.

**Cần chủ dự án/Claude xem:** [năm vòng](../../games/typing-defense/art-src/_review/179-ring.jpg), [30 tờ nguồn/hậu kỳ](../../games/typing-defense/art-src/_review/179/raw-vs-final-final-r2/), các crop 90°/120° ở `checks-final-r2/`, sắc vàng của ruộng và hai ngoại lệ ở mục 4. Bộ `.v3` đã lưu đủ để duyệt; chưa thay tài sản đang dùng.
