# Phiếu 120 · Dragonhold · Trời và phông xa của ải rồng

Ngày giao: 29/10/2026, macOS, repo cha. **Đã có 12 ô bản chọn theo sửa bắt buộc 29/10, 8 alpha, prompt và hồ sơ kiểm. Chưa đánh dấu “xong/nhận”: kiểm hue bằng 0 và một phần kiểm nền sạch còn trượt; cần Claude quyết theo §5.** Điểm tự chấm mỹ thuật trên bản giao: **M = 8**, Q từng ô **8–9**. Đây không thay kết luận nghiệm thu của Claude.

## 1. Bản nào được giao

Thư mục: `games/dragon-hold/art-src/backdrops/pass-epic/`.

| Bản chọn | Lượt nguồn được chọn | Alpha |
| --- | ---: | --- |
| `sky-dawn-a.png` | 2 | Không cần |
| `sky-dawn-b.png` | 2 | Không cần |
| `sky-dawn-c.png` | 1 | Không cần |
| `sky-dawn-d.png` | 1 | Không cần |
| `layer-near-a.v2.png` | 3 | Có, cùng gốc tên `.alpha.png` |
| `layer-near-b.v2.png` | 2 | Có, cùng gốc tên `.alpha.png` |
| `layer-near-c.v2.png` | 1 | Có, cùng gốc tên `.alpha.png` |
| `layer-near-d.v2.png` | 1 | Có, cùng gốc tên `.alpha.png` |
| `layer-mid.v2.png` | 3 | Có, cùng gốc tên `.alpha.png` |
| `layer-mid-2.v2.png` | 1 | Có, cùng gốc tên `.alpha.png` |
| `layer-far.v2.png` | 3 | Có, cùng gốc tên `.alpha.png` |
| `layer-far-2.v2.png` | 2 | Có, cùng gốc tên `.alpha.png` |

Mọi bản chọn đều **1536 × 1024**; mọi alpha cũng **1536 × 1024**, min **0**, max **255**. Mỗi bản có prompt cùng gốc tên. [Manifest giao cuối](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-handoff.json) ghi chính xác file và nguồn; không dùng manifest nháp `delivery-manifest.json`.

**Tám ô núi chọn bản `.v2`; các ô núi tên không có `.v2` là bản thử hậu kỳ bị loại, giữ nguyên theo lệnh không ghi đè/xóa.** Bốn ô trời dùng tên chính không hậu tố. Cũng giữ nguyên mọi `.try*` đã có. Các tờ không hậu tố, `-final`, `-delivery`, `-selected` là chẩn đoán trung gian; **tờ nghiệm thu lần này mang `-selected-final`**, liên kết ngay dưới. Không thay tên hoặc ghi đè các tờ trước.

Cách xếp không lật:

- Trời: `sky-dawn-a | sky-dawn-b | sky-dawn-c | sky-dawn-d`.
- 170 m: `layer-near-a.v2 | layer-near-b.v2 | layer-near-c.v2 | layer-near-d.v2`.
- 260 m: `layer-mid.v2 | layer-mid-2.v2 | layer-mid.v2 | layer-mid-2.v2`.
- 380 m: `layer-far.v2 | layer-far-2.v2 | layer-far.v2 | layer-far-2.v2`.

Tăng sáu tên ban đầu thành 12 ô là để thực hiện chỉ đạo bốn ô nối tiếp cho trời/170 m, hai ô khác nhau cho 260/380 m. Chưa gắn vào runtime; không sửa mã.

## 2. Ảnh kiểm phải xem

- [Ảnh ghép bản giao, 1536 × 1024](../../games/dragon-hold/art-src/_review/120-composite-selected-final.jpg).
- [Tờ so với mẫu chủ dự án, cùng cao 640 px; phông cũ ở hàng dưới](../../games/dragon-hold/art-src/_review/120-vs-ref-selected-final.jpg).
- [Bốn vòng và cảnh chồng lớp](../../games/dragon-hold/art-src/_review/120-ring-selected-final.jpg); [vòng chồng đủ lớp 6144 × 1024](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-final-review/composite-ring.png).
- [Ảnh ghép 384 px](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-final-review/composite-384.jpg).
- [Tờ viền ×2 trên trời sáng/tối](../../games/dragon-hold/art-src/_review/120-edge-selected-final.jpg).
- Mỗi ô có tờ **bản sinh | bản hậu kỳ**, hai bên cùng 1536 × 1024, trong [selected-final-review](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-final-review/), tên `<tên>-generated-vs-post.jpg`. Ví dụ [cổng ải](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-final-review/layer-near-a-generated-vs-post.jpg), [núi xa](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-final-review/layer-far-generated-vs-post.jpg).

Ảnh kiểm là ghép tĩnh bằng ImageMagick, không phải ảnh chụp game. Bản ghép dùng đúng thứ tự trời → xa → giữa → gần, cùng khung và không thêm vật vẽ bằng mã.

**Đứng cạnh được, ở M = 8:** có tường ải/cổng khổng lồ, tượng rồng, vách lớn, tuyết và tầng sương; nắng vàng có hướng, bóng lam/xanh, chi tiết đá và thông hoàn thiện hơn phông cũ. Chưa tới M = 9 của mẫu: thiếu nhân vật làm thước đo và khoảnh khắc hành động; cảnh nhiều chi tiết, các ô gần còn chứa một phần núi tuyết được vẽ sẵn nên tách chiều sâu chưa lý tưởng.

Ở 384 px: **tường ải/cổng: nhận ra; tượng rồng: nhận ra; đỉnh tuyết: nhận ra**. Cổng sáng là trọng tâm. Không dùng phần mây đẹp để che lỗi alpha.

## 3. Nguồn và các lượt sửa prompt

Khi bắt đầu phiên này đã có PNG lượt sinh, canvas nối tiếp 25%, stage0/stage1 và bốn dải nối từ các lần làm dở. Báo cáo cũ vẫn ghi 0/6 nên không dùng làm bằng chứng chưa tiêu lượt. Giữ nguyên chúng, đọc prompt và chọn tiếp từ hiện trạng. Các `.try1.prompt.txt` của sáu tên ban đầu chỉ là prompt chuẩn bị; không có `.try1.png` tương ứng trong thư mục tại lúc tiếp nhận.

Đã đọc chỉ đạo 28/10, bible Dragonhold, luật hậu kỳ §5, kết luận 119/120/159 của đợt chấm 29/10b, README `art-normalize`, prompt phông cũ; đã xem mẫu chủ dự án, map A2, `title-backdrop.png` và `keyart.png` của 119. Màu đá kem, bóng lam và nắng vàng theo 119; không chờ phiếu khác.

| Ảnh/lượt | Điều đã sửa trong prompt, kết quả chọn |
| --- | --- |
| Sáu prompt try1 chuẩn bị | Khối gốc còn luật dải lặng/lật. Giữ lịch sử, không dùng để tạo vòng mới. |
| `sky-dawn-a.try2` | Bỏ câu dải 8%/lật; giới hạn chỉ vẽ lớp trời, khớp nắng/màu 119. Chọn. |
| `sky-dawn-b.try2`, `sky-dawn-c.try1`, `sky-dawn-d.try1` | Sửa nối tiếp từ 25% mép phải ô trước; khóa phần trái, vẽ mây khác về phải, giữ sáng/sương. Chọn cả ba, không lật. |
| `layer-far.try2` → `try3` | Try2 lẫn cảnh hoàn chỉnh. Try3 yêu cầu chỉ giữ ba dãy tuyết xa, thay công trình/tượng/rừng gần bằng chân núi và sương lam. Chọn try3; đã tới nhãn lượt 3. |
| `layer-far-2.try1` → `try2` | Hai canvas nối tiếp được giữ; bản try2 nối tiếp từ far try3, hợp lớp xa hơn. Chọn try2. |
| `layer-mid.try2` → `try3` | Đưa tượng về trái để đọc rõ; try3 cô lập vách, bỏ tường/cổng/cầu/sông, giữ tượng, thác và sương. Chọn try3; không tạo lượt 4. |
| `layer-mid-2.try1` | Nối tiếp từ mid; phần riêng đổi sang vách tự nhiên, không tạo tượng thứ hai trong ô mới. Chọn. |
| `layer-near-a.try2` → **try3 phiên này** | Try2 có tượng trái gần trùng tượng lớp giữa, ghép thành hai đầu sát nhau. Try3 sửa riêng 36% trái thành sườn đá thấp/rừng thông, mở chỗ cho tượng giữa; giữ cổng và tượng phải. Chọn try3; không tạo lượt 4. |
| `layer-near-b.try2`, `layer-near-c.try1`, `layer-near-d.try1` | Nối tiếp 25% từ ô trước, cảnh tự nhiên khác nhau, không công trình và không lật. Chọn. |
| `sky/far/mid/near-join.try1` đã có | Sửa dải trung tâm quanh mối cuối → đầu, giữ hai bên. Chọn sky/far/mid; near try1 theo bố cục cũ nên thay. |
| **`near-join.try2` phiên này** | Vẽ lại sườn nối d → a sau khi hạ tượng trái; giữ sương xanh và rừng/đá liền. |
| **`near-join.try3` phiên này** | Sửa vệt hồng trên đỉnh tuyết nhỏ ở x400–560, y300–390 thành tuyết/đá bắt nắng vàng với bóng lam; giữ phần còn lại. Chọn dải này; hết ba lượt của dải nối near. |

Phiên này có **ba lần gọi `image_gen.imagegen` tích hợp**: `layer-near-a.try3`, `near-join.try2`, `near-join.try3`. Không dùng CLI/API thay thế, không mạng ngoài công cụ. Mọi PNG và prompt nguyên văn được giữ sát nhau trong `pass-epic/`; [nhật ký hai lượt đầu](../../games/dragon-hold/art-src/_review/120/delivery-20261029/generation-this-session.json) và tệp `.try3.prompt.txt`/PNG của dải nối ghi lượt cuối. Không tự nhận đã gọi các lượt có sẵn từ phiên trước.

## 4. Hậu kỳ và bảo toàn tranh

Nguồn đều 1536 × 1024. Ô nối tiếp giữ 384 cột trái làm ngữ cảnh: cắt **1152 × 1024+384+0**, Lanczos về 1536 × 1024; đó là phần vẽ mới. Ô neo không cần cắt giữa/đổi khổ. Các script stage0 cũ giữ công thức chính xác.

```sh
/opt/homebrew/bin/magick input.png -crop 1152x1024+384+0 +repage -filter Lanczos -resize 1536x1024! output.png
```

Không san đường chân núi về 58/60/62%, không tô dải mép trống, không phủ đáy để ép thành một màu. Không chỉnh gamma/độ sáng toàn ảnh. Bản nháp hòa cosin rộng làm magenta lọt vào vách; bản cắt tự động tạo khe tam giác ở hai dải khép vòng. Hai kiểu đó bị loại ở khu vực lỗi. Bản chọn giữ trọn **768 cột giữa (x384–1151)** của dải nối do công cụ sinh ảnh vẽ, hòa tối đa 48 px ở vùng sơn khớp hai bên; silhouette lấy nguyên của dải sinh, tránh cắt qua nền của ảnh khác. Ngoài dải nối giữ cảnh đã sinh. Far giữ phương án hòa cosin cũ vì phương án cắt tạo bậc màu ở sương đáy, nhìn thấy trên vòng riêng.

Tách nền dùng **chính hàm `normalize.key` của `tools/art-normalize/normalize.py` mà `key-alpha.sh` gọi**, nền `#FF00FF`, mode `global`, despill `protect-interior`; bản sửa bật `no_key_hue=True`. Không chạy wrapper shell nguyên trạng vì nó ghi WORK mặc định ngoài đường dẫn cho phép. Chỉ chuyển `normalize.WORK` vào hồ sơ phiếu, không sửa công cụ chung. Đây là khác biệt cách gọi được ghi công khai, không phải tự viết bộ tách nền thay thế.

Khử màu khóa bổ sung chỉ trong dải 6 px cạnh alpha bằng 0, chỉ pixel thuộc hue 285–330° và S > 0,5; giữ nguyên alpha và lòng vật. [Số pixel thật đã đổi](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-final/despill.json) ghi riêng từng ô. Không xóa pixel, không đổi màu bóng tối ở sâu trong tranh để ép kiểm 8 bằng 0.

## 5. Số đo bản chọn cuối

[JSON đo đầy đủ](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-final-review/metrics.json). Khổ **12/12 = 1536 × 1024**; alpha **8/8 min 0/max 255**.

Nền sạch kiểm ở top 10 px và phần cạnh bên 10 px thực sự ở trên silhouette (chừa 4 px AA); không kiểm đáy hay phần cạnh có tranh. “Lỗi nền / mẫu” là số px có ít nhất một kênh lệch #FF00FF quá 12. Hue khóa trong vật đếm trên alpha ≥250; hue tín hiệu ghi cả số px alpha >0 và tỉ lệ trên phần đục.

| Ô | Skyline trái/phải, px từ trên | Lỗi nền / mẫu | Lệch kênh nền lớn nhất | Hue khóa trong vật | Px hue tín hiệu còn thấy | % hue tín hiệu phần đục |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `layer-near-a` | 176 / 269 | 1624 / 19412 | 117 | 0.000971% | 29 | 0.002816% |
| `layer-near-b` | 274 / 332 | 53 / 21233 | 69 | 0.000710% | 25 | 0.002217% |
| `layer-near-c` | 320 / 336 | 5 / 21636 | 38 | 0.001015% | 29 | 0.002676% |
| `layer-near-d` | 327 / 196 | 1961 / 20437 | 139 | 0.001194% | 20 | 0.001837% |
| `layer-mid` | 92 / 414 | 156 / 20183 | 23 | 0.002815% | 72 | 0.006988% |
| `layer-mid-2` | 414 / 92 | 25 / 20182 | 32 | 0.002541% | 72 | 0.006534% |
| `layer-far` | 424 / 441 | 1 / 23744 | 14 | 0.000104% | 1 | 0.000104% |
| `layer-far-2` | 443 / 425 | 0 / 23785 | 9 | 0.000000% | 0 | 0.000000% |

**Hue khóa trong vật: qua ≤0,5% ở cả tám ô. Kiểm tín hiệu 0%: chỉ `layer-far-2` qua tuyệt đối; bảy ô còn lại không qua.** Số khác 0 không được làm tròn thành 0. Nền sạch cũng chưa qua tuyệt đối ở bảy ô; không tô màu nền đè lên nhánh thông hoặc AA để xóa số.

Theo §5, dừng việc ép hai ngưỡng này và giữ bản đẹp để Claude quyết: sau tách nền không thấy nền magenta thành một mảng trời, nhưng phép đo còn bắt những pixel bóng tối/sát mép. Không xem ngoại lệ đã được chấp thuận. Nếu Claude yêu cầu 0 tuyệt đối, cần thống nhất cách đếm vùng mép/độ sáng hoặc sửa bằng ảnh ở đúng vùng lỗi; không dùng lọc hue toàn tranh.

## 6. Vòng 6144 px và các mối ở 1 : 1

Đã dựng mỗi vòng 6144 × 1024 và góc nhìn 90° ở **bốn mối và giữa bốn ô**, cả từng lớp và cảnh chồng. Tên `*-seam-1` là d→a, `seam-2` là a→b, `seam-3` b→c, `seam-4` c→d; với mid/far, hai mối lặp lại ở 180°. Không có phép lật ảnh trong script giao.

[Bốn mối cảnh chồng](../../games/dragon-hold/art-src/_review/120/delivery-20261029/selected-final-review/): `composite-seam-1.jpg` đến `composite-seam-4.jpg`; tương tự `sky`, `far`, `mid`, `near`. Các ảnh `*-centre-1..4.jpg` là bốn góc nhìn giữa ô. Đây là file 1536 × 1024 để xem 1 : 1, không chỉ tờ thu nhỏ.

Trời: không thấy sọc nối đứng; mây chạy qua cạnh, không trục gương. Far: không thấy sọc nối đứng, cặp đỉnh lặp ở 180° đúng phương án L/L2. Mid: dải khép vòng đã hết khe cắt và quầng tím rộng; vẫn là một vách dốc tự nhiên mạnh ở đoạn L2→L. Near: không còn vạn hoa hoặc đảo tách rời; **b→c còn bậc silhouette khoảng 12 px ở mép mẫu**, nên chưa tuyên bố đạt tuyệt đối câu “không mối nào thấy được”. Không ép đường núi phẳng để giấu bậc đó. Tượng mid ở góc nhìn phía đối diện còn bị dãy tuyết vẽ sẵn trong lớp near che một phần; Q đã trừ cho việc chia lớp chưa sạch.

Số dưới là MAE RGB giữa hai cột tiếp giáp, không phải kiểm dải 8% đã bỏ. “Trước” lấy stage0; “sau” đo alpha bản chọn trên cùng trời kem. Chênh dưới chân núi từng hàng và AA có thể lớn tại nhánh/đỉnh thật; bảng này là bằng chứng bổ sung, không tự cấp đạt khi còn bậc nhìn thấy.

| Mối | MAE trước /255 | MAE sau /255 | Trung bình kênh R/G/B sau |
| --- | ---: | ---: | --- |
| `sky:1:sky-dawn-a|sky-dawn-b` | 9.42 | 1.79 | 2.71 / 1.50 / 1.15 |
| `sky:2:sky-dawn-b|sky-dawn-c` | 8.87 | 1.12 | 1.49 / 0.93 / 0.93 |
| `sky:3:sky-dawn-c|sky-dawn-d` | 11.09 | 1.24 | 1.56 / 1.07 / 1.08 |
| `sky:4:sky-dawn-d|sky-dawn-a` | 25.11 | 2.70 | 4.15 / 2.26 / 1.69 |
| `near:1:layer-near-a|layer-near-b` | 9.31 | 8.53 | 9.52 / 8.96 / 7.11 |
| `near:2:layer-near-b|layer-near-c` | 12.61 | 11.73 | 15.29 / 12.44 / 7.46 |
| `near:3:layer-near-c|layer-near-d` | 18.15 | 16.32 | 20.52 / 15.82 / 12.62 |
| `near:4:layer-near-d|layer-near-a` | 52.17 | 13.79 | 14.75 / 14.57 / 12.04 |
| `mid:1:layer-mid|layer-mid-2` | 12.32 | 10.93 | 13.04 / 11.15 / 8.59 |
| `mid:2:layer-mid-2|layer-mid` | 67.02 | 18.03 | 23.52 / 19.40 / 11.16 |
| `mid:3:layer-mid|layer-mid-2` | 12.32 | 10.93 | 13.04 / 11.15 / 8.59 |
| `mid:4:layer-mid-2|layer-mid` | 67.02 | 18.03 | 23.52 / 19.40 / 11.16 |
| `far:1:layer-far|layer-far-2` | 4.09 | 1.65 | 1.85 / 1.63 / 1.46 |
| `far:2:layer-far-2|layer-far` | 13.63 | 2.87 | 3.44 / 3.06 / 2.11 |
| `far:3:layer-far|layer-far-2` | 4.09 | 1.65 | 1.85 / 1.63 / 1.46 |
| `far:4:layer-far-2|layer-far` | 13.63 | 2.87 | 3.44 / 3.06 / 2.11 |

Viền ×2 trên trời sáng/tối: đã xem cổng, tuyết và các góc dải khép từng có lỗi. Không còn khe tam giác; vệt hồng trên tuyết đã sửa bằng lượt sinh 3. Vài pixel ấm/đỏ ở ngọn thông và các số hue trong bảng còn cần Claude soi. Không tuyên bố quét hết mọi pixel ở ×4 bằng mắt; đã có crop ×4 đi kèm ở các vị trí kiểm.

## 7. Điểm tự chấm KA5

M = **8 trên cảnh chồng bản hậu kỳ và vòng**, không dùng điểm ô lẻ để thay điểm toàn cảnh. Q theo thứ tự: đúng đề / đọc được / hợp bộ / hình khối / bước sau, mỗi mục tối đa 2. Cột 384 là chấm lại ô ở cỡ nhỏ; không nâng điểm vì chỉ nhìn bản sinh.

| Ô (núi dùng `.v2`) | M trên cảnh ghép | Q đầy đủ (năm mục) | Q ở 384 px |
| --- | ---: | --- | ---: |
| `sky-dawn-a` | 8 | 9 (2/2/2/2/1) | 8.5 |
| `sky-dawn-b` | 8 | 8.5 (2/2/2/1.5/1) | 8.5 |
| `sky-dawn-c` | 8 | 8.5 (2/2/2/1.5/1) | 8.5 |
| `sky-dawn-d` | 8 | 8.5 (2/2/2/1.5/1) | 8.5 |
| `layer-near-a` | 8 | 8.5 (2/2/2/1.5/1) | 8.5 |
| `layer-near-b` | 8 | 8 (1.5/2/2/1.5/1) | 8 |
| `layer-near-c` | 8 | 8 (1.5/2/2/1.5/1) | 8 |
| `layer-near-d` | 8 | 8 (1.5/2/2/1.5/1) | 8 |
| `layer-mid` | 8 | 8 (1.5/2/2/1.5/1) | 8 |
| `layer-mid-2` | 8 | 8 (1.5/2/2/1.5/1) | 8 |
| `layer-far` | 8 | 8.5 (1.5/2/2/2/1) | 8 |
| `layer-far-2` | 8 | 8.5 (1.5/2/2/2/1) | 8 |

Mốc cổng đọc rõ, nắng/màu khớp bộ 119. Trừ Q ở một số ô vì núi tuyết đã nằm trong lớp gần, hình khối đá có chỗ dày, chân núi không ở mốc prompt cũ và việc dùng tiếp còn vướng kiểm kỹ thuật nêu trên. **Các điểm ≥8 là tự chấm mỹ thuật, không có nghĩa mọi kiểm đã qua. Chưa được Claude chấm nhận.**

## 8. KA1 · không đổi file cũ

Đã chạy `md5 -r` từng file trong `backdrops/`, đệ quy, trước ghi phiên này và sau bàn giao.

| Đối chiếu | Số |
| --- | ---: |
| File trước phiên | 62 |
| File sau giao | 124 |
| File thêm | 62 |
| File trước phiên đổi / mất | 0 / 0 |
| File ở mốc gốc `_review/120/md5-before.txt` đổi / mất | 0 / 0 |

[MD5 trước phiên](../../games/dragon-hold/art-src/_review/120/delivery-20261029/md5-before.txt), [MD5 sau](../../games/dragon-hold/art-src/_review/120/delivery-20261029/md5-after.txt), [diff](../../games/dragon-hold/art-src/_review/120/delivery-20261029/md5-diff.txt), [KA1 JSON](../../games/dragon-hold/art-src/_review/120/delivery-20261029/ka1.json). Diff nội dung chỉ thêm dòng; header `---/+++` không phải file bị xóa. `pine-river-far*` và mọi `.try*` có sẵn giữ nguyên byte.

## 9. Script, phạm vi và phần còn lại

Script trong [hồ sơ phiên](../../games/dragon-hold/art-src/_review/120/delivery-20261029/): `prepare_delivery.py`, `review.py`, `refine.py`, `refine_haze.py`, `repair_closure.py`, `repair_closure_v3.py`, `select_final.py`, `handoff.py`, `edge_corners.py`, `write_report.py`; các script nháp được giữ để truy vết. Writer media mở độc quyền, từ chối đích đã có. Để chạy lại phải chọn thư mục/tên đích mới trong phạm vi phiếu; không xóa nguồn hoặc lách chặn ghi đè. Cần cả các stage0/nguồn try và script kế thừa trong `run-20261029`/`resume-20261029-1442` để tái hiện các bước đầu.

`ART_MAGICK=/opt/homebrew/bin/magick`; Python 3 chuẩn, không cài thư viện; font `/System/Library/Fonts/Supplemental/Arial.ttf`. Đọc/ghi ảnh cục bộ, không dev server, trình duyệt, Git, build hoặc test suite game; không âm thanh, không đụng game khác/công cụ chung/Tu Tiên. Không có capture trình duyệt/render nên không chạy dọn capture; giữ mọi nguồn sinh theo phiếu.

**Chưa làm và lý do:** chưa gắn vào game vì phiếu chỉ làm media; chưa có nhận của Claude; chưa sửa màu toàn tranh để ép hue 0 hoặc san mép núi để ép mốc chiều cao, do §5 cấm phá tranh. Near-a đã đến lượt 3; mid/far cũng đã có nhãn try3; dải nối near hết ba lượt. Các ô chưa hết lượt không được coi tự động hết ngân sách.

**Chủ dự án/Claude cần xem:** ảnh ghép `120-composite-selected-final.jpg`, bốn góc nhìn mối, góc dải nối ×2, bậc near b→c và hai ngưỡng số đang trượt. Đề xuất nhận mỹ thuật M/Q nếu đồng ý, đồng thời quyết phạm vi đếm nền/hue; nếu vẫn giữ kiểm tuyệt đối, ghi phiếu sửa đúng dải near b→c và các pixel được định vị, không sửa rộng cả tranh. **Không báo phiếu đã nhận hoặc đã qua mục 2–5 và 8.**
