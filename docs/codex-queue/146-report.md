# Phiếu 146 · Dragonhold · Tám mảnh UI nhỏ

**Ngày:** 29/10/2026. **Thực hiện:** Codex, `image_gen` tích hợp.

**Đã giao đủ tám ảnh, ba bản thu mỗi ảnh, prompt và hồ sơ kiểm. Chưa nghiệm thu toàn bộ:** còn ngoại lệ hue, ba cặp IoU và cách hiểu yêu cầu nền tương phản; giữ tranh theo `ART_ACCEPTANCE.md` §5. `checks-v2.json` ghi `strict_acceptance_pass: false`. Chưa có Claude chấm nhận.

## 1. Bản chọn và tờ xem

- **Bộ chọn cuối:** [`games/dragon-hold/art-src/ui/parts/selected/`](../../games/dragon-hold/art-src/ui/parts/selected/). Tám tên đúng phiếu; mỗi tên có `.png`, `.prompt.txt`, `.256.png`, `.128.png`, `.64.png` và prompt hậu kỳ của từng bản thu.
- **Nguồn sinh và prompt nguyên văn:** [`ui/parts/`](../../games/dragon-hold/art-src/ui/parts/), mỗi tên có `.try1.png` và `.try1.prompt.txt`. Giữ cả bộ hậu kỳ đầu ở đây; bộ đầu chưa sửa alpha ringing, không phải bộ chọn cuối.
- [Tờ chung bốn hàng](../../games/dragon-hold/art-src/_review/146-sheet.jpg), [tờ ba cỡ 9-slice và chữ](../../games/dragon-hold/art-src/_review/146-nine-slice.jpg).
- [Script, hồ sơ và cách tái kiểm](../../games/dragon-hold/art-src/_review/146/README.md); [khổ/kênh 32 PNG](../../games/dragon-hold/art-src/_review/146/final-checks/identify.txt); [số đo cuối](../../games/dragon-hold/art-src/_review/146/final-checks/metrics.json); [28 cặp IoU](../../games/dragon-hold/art-src/_review/146/final-checks/iou.json); [kiểm bảo toàn RGB và cỡ game](../../games/dragon-hold/art-src/_review/146/verification.json).

Đã đọc báo cáo 162 và dùng tờ khung chọn 162 làm tham chiếu đính kèm; bộ 162 còn mục kỹ thuật chờ phân xử, không ghi nhận thay cho người duyệt. Đã xem hai icon bắt buộc `skill-fire-breath.png`, `gold.png`, mock tựa 119 và ảnh thương mại chủ dự án. Tờ chung đặt cạnh bốn icon v2 đang có, mảnh HUD ảnh thương mại và bộ 162; lấy mức hoàn thiện, không chép nội dung.

## 2. Lượt sinh và hậu kỳ

Tám lần gọi công cụ, mỗi ảnh một lượt `try1`; không có lượt 2/3. STYLE-UI nguyên văn ở AD §3.2, tiếp theo KIND PART, phần vật riêng và nền M `#FF00FF`. Prompt bằng tiếng Anh, lưu đúng chuỗi đã gửi trong `prompts.json` và cạnh từng ảnh. Hai trạng thái là lượt chỉnh sửa bằng công cụ tạo ảnh, không phải hiệu ứng vẽ bằng mã.

| Ảnh | Nội dung lượt 1 và điều chỉnh prompt |
| --- | --- |
| `keycap` | Hoa cương kem, mặt trống phẳng, sắt rèn, góc cắt nhẹ. Nhận được trang trí vàng/men ở bốn góc hợp bộ 162; không cắt bỏ để biến thành phím CSS. |
| `keycap-active` | Dùng keycap làm mục tiêu chỉnh sửa; đổi phần viền sang men than hồng, yêu cầu giữ dáng và vị trí. IoU sau hậu kỳ 1,0000. |
| `tag-plate-enemy` | Đá phiến tối, đầu nhọn, đoạn giữa yên và rail thẳng để kéo 9-slice. Nguồn có thêm hoa cương/vảy ở đầu, giữ nguyên. |
| `tag-plate-general` | Đổi thành viền đồng kép, bốn sừng ngắn ở hai đầu; giữ lòng tối và đoạn giữa kéo được. |
| `tag-plate-urgent` | Viền men đỏ cam, hai đầu đuôi chẻ; giữ đoạn giữa trống. |
| `level-badge` | Huy hiệu tròn, mặt sắt trống, vòng vảy rồng; cùng bộ kim loại và điểm men 162. |
| `pip-lit` | Hạt than hồng đặc, lõi sáng, mặt khoáng có khối, ánh sáng nằm trong dáng vật. Nguồn trả vật nhỏ hơn lề yêu cầu; sửa bằng crop lề và phóng đồng tỷ lệ. |
| `pip-unlit` | Dùng pip-lit làm mục tiêu chỉnh sửa thành sắt tối với phản sáng bạc; căn lại lề sau sinh. IoU cặp 0,9782. |

Tách nền bằng thuật toán `tools/art-normalize`, global, protect-interior, no-key-hue; WORK nằm trong hồ sơ 146, không ghi vào công cụ chung. Chỉ crop khoảng trống, Lanczos và căn giữa; không san phẳng hay phủ lòng đế, không chỉnh sáng/gamma toàn ảnh. Bản đầu có alpha ringing do nội suy: bộ chọn cuối sửa riêng alpha bán trong suốt ngoài dải mép 3 px về 0/255. [Số pixel sửa](../../games/dragon-hold/art-src/_review/146/alpha-repair.json) và kiểm độc lập xác nhận **0 pixel đổi RGB** so với bộ hậu kỳ đầu, cả tám ảnh. Đây là sửa mép/độ đục, không xóa phần vẽ trong lòng.

Nguồn vuông 1254², nguồn đế 2172 × 724. Bản giao phím/huy hiệu/chấm 1024²; ba đế theo bảng riêng 1536 × 512. Bản thu là ô vuông đúng 256²/128²/64², giữ tỷ lệ và thêm lề alpha, Lanczos trực tiếp từ bản gốc, không làm nét 64. Toàn bộ 32 PNG là sRGB RGBA; ImageMagick 7 in `srgba 4.0`.

Pip-lit phóng khoảng **2,234×**, pip-unlit **1,175×** từ phần vật nguồn; không tuyên bố thêm chi tiết thật do phóng. Chấm chỉ dùng ở 6/9 px, đã xem ở hai cỡ này. Các tỷ lệ/crop khác nằm trong `processing.json`.

## 3. Khổ, alpha, lề và dáng

Tỷ lệ hue lấy trên **pixel alpha > 0**, hue cách 300° không quá 15°, S > 0,5; ngưỡng ≤0,2%. Alpha ngoài dải mép 3 px phải nhị phân. Bbox dùng alpha > 16; cạnh dài phải 68–72%, lệch tâm từng trục ≤2%. IoU dùng mặt nạ 32 × 32, giữ tỷ lệ/căn giữa, alpha > 16; bảng bỏ cặp trạng thái cùng vật khi tìm IoU lớn nhất.

| Ảnh | Bbox alpha >16 | Cạnh dài/canvas | Lệch tâm lớn nhất | Alpha lửng ngoài 3 px | Pixel hue khóa / % thấy được | IoU khác vật lớn nhất |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `keycap` | 717 × 694 | 70.02% | 0.049% | 0 | 21 / 0.00429% | 0.7691 · `pip-unlit` |
| `keycap-active` | 717 × 694 | 70.02% | 0.049% | 0 | 27 / 0.00551% | 0.7691 · `pip-unlit` |
| `tag-plate-enemy` | 1075 × 158 | 69.99% | 0.033% | 0 | 53 / 0.03703% | 0.8596 · `tag-plate-general` |
| `tag-plate-general` | 1075 × 219 | 69.99% | 0.098% | 0 | 404 / 0.23048% | 0.8596 · `tag-plate-enemy` |
| `tag-plate-urgent` | 1075 × 156 | 69.99% | 0.033% | 0 | 149 / 0.10822% | 0.6667 · `tag-plate-general` |
| `level-badge` | 718 × 704 | 70.12% | 0.000% | 0 | 245 / 0.07403% | 0.8596 · `pip-lit` |
| `pip-lit` | 699 × 719 | 70.21% | 0.049% | 0 | 7 / 0.00179% | 0.8596 · `level-badge` |
| `pip-unlit` | 706 × 718 | 70.12% | 0.098% | 0 | 183 / 0.04643% | 0.8491 · `level-badge` |

**Qua:** khổ/kênh của đủ 32 PNG, lề và tâm của cả tám bản gốc, alpha ngoài dải mép của cả tám, hai cặp trạng thái: keycap **1,0000**, pip **0,9782** (ngưỡng ≥0,95).

**Chưa qua hue:** riêng general **404 pixel / 0,23048%**, vượt 0,2%. 403 pixel có V < 90/255, một pixel V=97; gồm các sắc rất tối và mép alpha thấp. Đã chạy tách nền/despill; giữ phần còn lại, không xóa thêm nét nguồn để đổi trạng thái số. Người duyệt cần xem mép ở bản đầy đủ; không thay điều kiện hue bằng điều kiện độ sáng để công bố đạt.

**Chưa qua ba cặp IoU khác vật:** enemy/general **0,8596**; badge/pip-lit **0,8596**; badge/pip-unlit **0,8491**. Giữ đầu đế và dáng huy hiệu/hạt tròn đúng đề. Đổi huy hiệu/hạt sang hình khác chỉ để giảm IoU sẽ mâu thuẫn nội dung; dừng theo §5. Bảng 28 cặp giữ nguyên các `pass: false`.

## 4. Cỡ dùng, tương phản và 9-slice

Luma mã hóa Y′ có trọng số alpha, đo trên phần vật thu về đúng chiều cao dùng. WCAG ở phần tiếp theo dùng độ chói sRGB tuyến tính riêng. Phím/huy hiệu/chấm bỏ lề trống **chỉ khi dựng tờ kiểm**, để vật cao đúng số px; file giao vẫn giữ lề chuẩn. Đế ở tờ chung dựng 9-slice cao 26/32, rộng 128 để nằm trong mỗi ô; tờ chữ riêng giữ đúng ba khổ bắt buộc.

| Ảnh | Cao 720p / 1080p | ΔY′ vỏ cây 720p / 1080p | ΔY′ kem 720p / 1080p |
| --- | ---: | ---: | ---: |
| `keycap` | 14 / 20 | 0.474 / 0.476 | 0.283 / 0.282 |
| `keycap-active` | 14 / 20 | 0.507 / 0.508 | 0.251 / 0.250 |
| `tag-plate-enemy` | 26 / 32 | 0.156 / 0.156 | 0.602 / 0.602 |
| `tag-plate-general` | 26 / 32 | 0.104 / 0.105 | 0.654 / 0.652 |
| `tag-plate-urgent` | 26 / 32 | 0.101 / 0.100 | 0.657 / 0.658 |
| `level-badge` | 16 / 24 | 0.274 / 0.275 | 0.484 / 0.483 |
| `pip-lit` | 6 / 9 | 0.301 / 0.300 | 0.457 / 0.458 |
| `pip-unlit` | 6 / 9 | 0.137 / 0.136 | 0.621 / 0.622 |

Cả tám vượt ΔY′ ≥0,25 trên ít nhất một trong **hai nền được liệt kê**. Tuy nhiên phiếu lại viết “ít nhất một trong hai nền tối”, trong khi kem là nền sáng. Hồ sơ chặt hơn kiểm riêng vỏ cây: ba đế và pip-unlit chưa đạt. Không làm sáng lòng đế để ép số vì sẽ làm yếu chữ và đổi vật liệu; pip-unlit cần giữ trạng thái tối. Tờ xem cho thấy viền vẫn phân cách được; điều đó không thay cho kết quả số. Đề nghị Claude phân xử cách hiểu ngưỡng, không tự coi là đã qua nền tối.

Ba JSON 9-slice ở `final-checks/<tên>.9slice.json`, có bbox nội dung và khoảng cắt tính từ bbox: mỗi đầu 18% chiều rộng, trên/dưới 27% chiều cao. Dựng chín mảnh từ nguyên tranh, co giãn lòng; không phủ màu, không làm phẳng vân. σ đo ở đoạn giữa 50% chiều rộng, 24% chiều cao, tránh rail và đầu trang trí; ghi tọa độ ROI trong JSON.

| Đế | σY′ nguồn giữa | WCAG chữ/giữa nguồn | σY′ / WCAG tại 80×26 · 160×26 · 240×32 |
| --- | ---: | ---: | --- |
| `tag-plate-enemy` | 0.02911 | 11.426:1 | 0.01440 / 11.259:1 · 0.02020 / 11.387:1 · 0.02062 / 11.413:1 |
| `tag-plate-general` | 0.04119 | 12.013:1 | 0.01754 / 11.946:1 · 0.01956 / 11.887:1 · 0.02180 / 11.857:1 |
| `tag-plate-urgent` | 0.02366 | 12.260:1 | 0.01857 / 12.592:1 · 0.01532 / 12.247:1 · 0.01763 / 12.213:1 |

**Cả ba qua σ≤0,05 và WCAG≥4,5** ở nguồn và cả ba khổ dựng. Chữ thử `WORD`, Arial 20 px, màu `#f5ecd8`. Ở **80 × 26**, từ bốn chữ chạm vùng đầu trang trí; tương phản trung vị đạt không đồng nghĩa đủ chiều rộng chữ. Giữ tờ này để người gắn thấy giới hạn; nên chọn chiều rộng theo độ dài từ, không tự thay cỡ chữ hay cắt bỏ đầu trang trí trong phiếu ảnh. 160 × 26 và 240 × 32 có chỗ chữ rõ.

## 5. Tự chấm KA5 trên bản hậu kỳ

Đã xem các bản giao đầy đủ, tờ cỡ 720p/1080p và tờ 9-slice cạnh tham chiếu thương mại. Q theo Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp, mỗi mục 0–2. “Dùng tiếp” chỉ cho 2 ở cặp phím đã qua các kiểm riêng; ảnh còn ngoại lệ giữ 1. M là mức hoàn thiện so với UI thương mại, không phải điểm cảnh nền; không dùng Q cao để thay các phép kiểm chưa qua.

| Ảnh | Q ở gốc | Q ở 720p | M gốc / 720p | Nhận xét |
| --- | --- | --- | ---: | --- |
| keycap | 10 (2/2/2/2/2) | 9,5 (2/1,5/2/2/2) | 8,5 / 8 | Hoa cương có khối, lòng trống; trang trí góc gom nhỏ khi cao 14 px. |
| keycap-active | 10 (2/2/2/2/2) | 9,5 (2/1,5/2/2/2) | 8,5 / 8 | Cùng dáng phím, viền sáng phân trạng thái; chi tiết vảy không đọc riêng ở 14 px. |
| tag-plate-enemy | 9 (2/2/2/2/1) | 8,5 (2/1,5/2/2/1) | 8 / 8 | Đầu nhọn rõ, lòng tối tốt; chờ IoU/nền, khổ 80 chật chữ. |
| tag-plate-general | 9 (2/2/2/2/1) | 8 (2/1/2/2/1) | 8 / 8 | Sừng và viền kép có thứ bậc; sừng nhỏ, chờ hue/IoU/nền. |
| tag-plate-urgent | 9 (2/2/2/2/1) | 8,5 (2/1,5/2/2/1) | 8,5 / 8 | Đuôi chẻ khác dáng, men đỏ cam rõ; khổ 80 chật chữ, chờ nền. |
| level-badge | 9 (2/2/2/2/1) | 8,5 (2/1,5/2/2/1) | 8,5 / 8 | Vòng vảy và mặt sắt có khối, ornament dày ở 16 px; chờ IoU. |
| pip-lit | 9 (2/2/2/2/1) | 9 (2/2/2/2/1) | 8 / 8 | Lõi than hồng rõ ở 6 px; nguồn vật nhỏ phải phóng, chờ IoU với badge. |
| pip-unlit | 9 (2/2/2/2/1) | 8,5 (2/1,5/2/2/1) | 8 / 8 | Phản sáng bạc giữ nhận diện hạt tắt; hơi chìm trên vỏ cây, chờ IoU/nền. |

Tám tờ **bản sinh | bản hậu kỳ**, mỗi bên nguyên canvas trong ô cùng cỡ:

- [keycap](../../games/dragon-hold/art-src/_review/146-keycap-raw-vs-final.jpg), [keycap-active](../../games/dragon-hold/art-src/_review/146-keycap-active-raw-vs-final.jpg).
- [enemy](../../games/dragon-hold/art-src/_review/146-tag-plate-enemy-raw-vs-final.jpg), [general](../../games/dragon-hold/art-src/_review/146-tag-plate-general-raw-vs-final.jpg), [urgent](../../games/dragon-hold/art-src/_review/146-tag-plate-urgent-raw-vs-final.jpg).
- [level-badge](../../games/dragon-hold/art-src/_review/146-level-badge-raw-vs-final.jpg), [pip-lit](../../games/dragon-hold/art-src/_review/146-pip-lit-raw-vs-final.jpg), [pip-unlit](../../games/dragon-hold/art-src/_review/146-pip-unlit-raw-vs-final.jpg).

## 6. KA1, khác phiếu và việc chờ duyệt

**KA1:** 1058 file trước, 1202 file sau trên toàn `art-src/ui/`; **0 đổi md5, 0 mất**, thêm 144 file của 146, không có file thêm của làn song song trong khoảng đo. `md5 -r` lưu trước/sau; `md5-diff.txt` chỉ có dòng thêm ngoài tiêu đề diff. Thư mục đích mới và báo cáo không có trước tác vụ.

Khác phiếu được ghi rõ:

1. Bộ chọn cuối đặt trong `ui/parts/selected/`, vẫn trong phạm vi cho phép, để giữ nguyên bộ hậu kỳ đầu khi sửa alpha và không ghi đè ảnh đã lưu. Khi gắn dùng bộ con này.
2. Ba đế 1536 × 512 theo bảng riêng, ưu tiên hơn câu chung 1024². Bản thu vuông giữ tỷ lệ, không bóp đế thành vuông.
3. Vật ở nguồn không đồng loạt đúng 70%; đã căn bằng công cụ. Hai pip có phóng, không giấu tỷ lệ.
4. Không tự ép hue/IoU/độ sáng bằng cách bỏ nét hoặc đổi dáng; giữ ngoại lệ theo §5. Chưa thỏa điều kiện “mọi kiểm đạt”, dù đủ file và điểm tự chấm từ 8.
5. Bộ đọc kiểm đầu hiểu sai chuỗi kênh của ImageMagick 7. Đã sửa bộ đọc, giữ kết quả cũ để truy nguyên; **`checks-v2.json` mới là tổng hợp đúng**, và kiểm độc lập `verification.json` xác nhận đủ 32 file đúng.

Không chạy Git, dev server, trình duyệt, game build hoặc test suite; không ghi runtime, `public/`, game khác, Tu Tiên, `.wt-*` hay công cụ chung. Không âm thanh và không chuỗi frame chụp trình duyệt cần prune. Chưa sửa các danh sách nâng chất lượng khác vì chỉ được ghi báo cáo này.

**Người duyệt cần xem:** hue general, ba cặp IoU, cách hiểu nền tương phản và chỗ chữ ở 80 × 26; chấm lại ít nhất 8 trên bộ `selected/` ở đủ khổ/cỡ thật. Claude quyết định nhận ngoại lệ và chép vào `public/` khi tích hợp. Chưa tuyên bố nghiệm thu hay tích hợp hoàn tất.
