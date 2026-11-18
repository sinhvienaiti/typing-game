# Phiếu 166 · Wordwoven · Vẽ lại icon tài nguyên

Ngày làm: 29/10/2026, repo cha trên Mac mini M4, macOS. Dùng **`image_gen` tích hợp**, theo skill `imagegen`; không gọi dịch vụ sinh ảnh khác.

**Đã giao đủ 8 icon: 7 bản vẽ lại và Seeds mới; 32 PNG chọn cùng prompt, giữ đủ 10 lượt sinh và prompt. Kiểm số trên đúng 32 file giao đều đạt. KA5 tự chấm ở bản gốc và 720p từ 9; mức mỹ thuật thương mại M từ 8. Chưa nghiệm thu Claude. Yêu cầu đặt cạnh bốn icon mới đã nhận chưa thể đáp ứng đúng trạng thái: chưa tìm thấy bốn icon có kết luận nhận; tờ cuối dùng bốn phần tử khung 115 đã nhận, kèm tờ riêng cạnh bốn icon 134 ghi rõ “chờ nhận”.**

## 1. File giao và ảnh cần xem

- [Tài nguyên](../../games/typing-defense/art-src/ui/resources/): `gold.v2`, `wood.v2`, `food.v2`, `lives.v2`, `knowledge.v2`, `wave.v2`, `seeds`.
- [Đèn lồng](../../games/typing-defense/art-src/ui/lanterns/): `lantern-blazing.v2`.
- Mỗi tên có `.png` 1024², `.256.png`, `.128.png`, `.64.png` và prompt cạnh từng PNG. Giữ nguyên toàn bộ tên và byte của bộ cũ. Không chép vào `public/`.
- **Tờ xem cuối:** [166-sheet-final.jpg](../../games/typing-defense/art-src/_review/166-sheet-final.jpg). Bốn hàng: gốc 256 px; cỡ 1080p hai nền; cỡ 720p hai nền; mỗi icon cạnh bốn mẫu 115 và mảnh HUD thương mại.
- [So cũ–mới 64 và 32 px](../../games/typing-defense/art-src/_review/166-old-new.jpg), [so bộ icon 134](../../games/typing-defense/art-src/_review/166-new-set.jpg), [cỡ 720p nguyên tỉ lệ](../../games/typing-defense/art-src/_review/166/native/720-native.png), [phóng nearest ×6 để soi](../../games/typing-defense/art-src/_review/166-720p.jpg).
- [Tám tờ bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/166/sheets/before-after/), [tám tờ cùng vị trí và tỉ lệ](../../games/typing-defense/art-src/_review/166/sheets/registered/). Vế sinh của tờ thứ hai chỉ cắt khoảng trống và thu giữ tỉ lệ; giữ nguyên nền M và phần vẽ.
- [Số đo trước công bố](../../games/typing-defense/art-src/_review/166/metrics-selected/metrics.json), [kiểm trên đúng file giao](../../games/typing-defense/art-src/_review/166/final-check/audit.json), [32 dòng identify](../../games/typing-defense/art-src/_review/166/final-check/identify.txt), [hồ sơ và script](../../games/typing-defense/art-src/_review/166/).

Tờ đúng tên yêu cầu [166-sheet.jpg](../../games/typing-defense/art-src/_review/166-sheet.jpg) vẫn giữ làm bản đầu: hàng tham chiếu dùng PNG nền khóa của 115. Tờ `166-sheet-final.jpg` dùng các bản `.alpha.png` của cùng bốn mẫu để so dễ hơn; không ghi đè tờ đầu.

Không chạy lệnh Git, game, build/test suite, dev server, trình duyệt hoặc mạng ngoài `image_gen`. Không đọc/ghi Tu Tiên, không đụng `.wt-*`, không ghi game khác, mã game hoặc tài liệu ngoài báo cáo này. Không tạo âm thanh. Không có capture trình duyệt hoặc chuỗi raw frame cần prune.

## 2. Tham chiếu và prompt từng lượt

Đã xem ảnh chủ dự án `_refs/owner-epic-2026-10-28.webp`, lấy độ hoàn thiện HUD, không chép nội dung. Bốn phần tử **banner, portrait-ring, crest, divider** của 115 được Claude nhận trong `accept-29-10/verdict.md`; đường dẫn thật là `ui/frames-epic/`, không phải `ui/frames/`. Bảng tham chiếu `_review/166/115-accepted-style-board.png` là bản sao nguyên byte bảng bốn mẫu từ phiếu 165, chỉ dùng để cấp tham chiếu, không làm ảnh giao.

Mỗi lượt vẽ lại đính kèm đủ: **ảnh cũ cùng tên, bảng 115, đúng `ui/title-epic/emblem.png`, `keyart.png` của 113, ảnh chủ dự án**. Seeds không có ảnh cũ ở thư mục đích nên đính kèm bốn tham chiếu phong cách. Bảng bốn mẫu giúp giữ trong giới hạn 5 ảnh đính kèm của công cụ.

Prompt tiếng Anh mở bằng **STYLE-UI 115 nguyên văn + ICON §3.5 nguyên văn**. Phần sau ghi rõ STYLE mới được ưu tiên so với viền mực/tô phẳng của ICON cũ, cạnh dài 70% thay 80%; giữ chất liệu tự nhiên của từng tài nguyên. Không dùng STYLE storybook. Bảy ảnh vẽ lại có nguyên câu **“Keep the same object identity as the attached image. Repaint it in the new style as described.”** Dòng cuối khóa nền M nguyên văn. Mỗi prompt chính xác nằm cạnh `.tryN.png`; prompt bản chọn trùng lượt được chọn.

| Tên | Lượt giữ / chọn | Nội dung và sửa prompt |
|---|---|---|
| `gold.v2` | 1 / try1 | Giữ ba đồng tiền lỗ vuông chồng lên nhau; vàng búa, ngọc và nét đồng Đông Sơn, không chữ. |
| `wood.v2` | 1, 2 / **try2** | Hai khúc gỗ có mặt cắt nhìn phải. Try1 quá vuông, IoU với Lives 0,8082. Try2 yêu cầu gỗ dài, bó thấp, mặt cắt nhỏ hơn; giữ cả hai khúc và vỏ gỗ. |
| `food.v2` | 1, 2 / **try2** | Giữ bó lúa chín, không đổi sang bát cơm. Try1 xòe rộng, IoU với Lives 0,8345. Try2 yêu cầu bó cao hẹp, hai khối bông rủ gọn phía trên và cán thân hẹp phía dưới. Không bóp méo bằng hậu kỳ. |
| `lives.v2` | 1 / try1 | Giữ thẻ gỗ tròn có tim đỏ; nền ngà, đai tre và đồng, tim sơn son có chiều sâu. Vành là một phần đồ vật gốc, không thêm khung bao UI. |
| `knowledge.v2` | 1 / try1 | Sách mở và bút lông lớn chéo trang phải; trang trống, bìa ngọc, góc đồng và dấu son nhỏ. |
| `wave.v2` | 1 / try1 | Giữ cờ rách và cán nghiêng; đổi vải tím cũ sang ngọc sẫm, nếp vàng sáng để hợp bộ và tránh sắc khóa M. Không đổi thành tù và. |
| `lantern-blazing.v2` | 1 / try1 | Giữ đèn giấy tròn, quai và tua; giấy hổ phách có lửa lớn bên trong, lửa gọn trên nắp, gân đồng và nắp ngọc. Không halo trên nền khóa. |
| `seeds` | 1 / try1 | Túi vải ngà buộc dây ngọc, hạt lúa vàng đổ ra phía dưới phải; dáng túi cổ thắt khác đèn và bó lúa. |

**10 lượt sinh thành công, tối đa 2 lượt/ảnh. 10/10 PNG thử trùng nguyên byte với nguồn công cụ; 10/10 prompt khớp bản đã gửi.** `*.tryN.record.json` lưu đường dẫn nguồn và prompt. Kế hoạch đầu được sửa nội dung trước khi sinh sau khi xem ảnh cũ: Food là bó lúa, Lives là thẻ tim, Knowledge có bút, Wave là cờ; đây không phải những lượt sinh bị bỏ.

## 3. Hậu kỳ không phá tranh

Công cụ trả nguồn **1254 × 1254** cho cả 10 lượt, không phải 1024². Giữ nguyên nguồn trong `.tryN.png`; bản chọn được tách nền, thu và thêm lề về 1024². Không giả nhận nguồn nguyên sinh 1024².

Dùng bản sao nguyên trạng bốn file `key-alpha.sh`, `common.sh`, `normalize.py`, `seam_analysis.py` trong `_review/166/art-normalize/`, để WORK nằm trong đường dẫn phiếu cho phép. Kiểm SHA-256 xác nhận cả bốn bản sao trùng công cụ repo.

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash games/typing-defense/art-src/_review/166/art-normalize/key-alpha.sh   IN.tryN.png OUT.key.png --bg '#FF00FF' --mode global   --despill protect-interior
```

Không bật `--no-key-hue`. Giữ toàn bộ alpha > 0 khi tính khung cắt, thêm 4 px nguồn, Lanczos fit trong 724² và đặt giữa 1024². Hộp alpha > 16 cuối có cạnh dài 720 px. Ba bản thu lấy **trực tiếp từ master 1024²**, không thu nối tiếp và không làm nét.

Sửa alpha do nội suy ngoài dải Disk:3 quanh ranh alpha ≥128: trong vật về 255, ringing ngoài về 0; giữ RGB. Bản trước sửa, số pixel và alpha cũ nằm trong từng `processing.json`. Hai cụm matte cần xem riêng: Food có 2 pixel dư hồng alpha 76/83; đèn có 4 pixel xám alpha 105–107 trong khe nền cạnh lửa/quai. Đây là dư tách nền, không phải nét lúa hoặc dây; giữ ảnh fitted và ảnh soi khe đèn để đối chiếu. Không cắt mất đầu bông, tua, bút hoặc mép cờ.

**Wave:** bản đầu có sắc khóa 1,4760% và chênh luma 0,2283, trượt. Sửa miễn phí trước khi tính sinh lại: thay RGB của **2.695 pixel sắc khóa trong dải mép 3 px** bằng màu sơn liền kề trong bán kính tối đa 6 px, giữ alpha; bỏ qua 8 pixel trong lòng. Sau đó tăng sáng **toàn RGB ×1,09 (+9%)**, không gamma, không đổi bão hòa; nằm trong ±10% của §5. Master đạt tương phản nhưng Lanczos bản 256 phát sinh 59 pixel sắc khóa, sửa riêng cùng cách ở mép và giữ alpha. Các bản 128/64 không sửa RGB. Nhật ký từng tọa độ/RGBA nằm ở `wave-edge-light/edge-repair-pixels.json` và `wave-ready/edge-repair256-pixels.json`.

Không phủ mảng, san phẳng, vẽ lại vật liệu hoặc xóa phần vẽ để đạt số. Đã xem các tờ hậu kỳ và so cùng vị trí; bản Wave sáng hơn nhẹ, vẫn giữ vân vải, bóng và nếp gấp. Không có ngưỡng nào còn buộc phá tranh; không tự miễn kiểm số.

## 4. KA1 · MD5 và khổ

Băm `md5 -r` mọi file đệ quy trong hai thư mục đích `ui/resources/` và `ui/lanterns/`, cùng thứ tự và đường dẫn tương đối. Review và báo cáo không nằm trong danh sách băm media để tránh tự băm chính danh sách.

| Trước | Sau | Thêm | Sửa | Xóa | Dòng `<` trong diff |
|---:|---:|---:|---:|---:|---:|
| 40 | 124 | **84** | **0** | **0** | **0** |

84 file thêm = 20 PNG thử/prompt + 64 PNG chọn/prompt. [Trước](../../games/typing-defense/art-src/_review/166/md5-before.txt), [sau](../../games/typing-defense/art-src/_review/166/md5-after.txt), [diff chỉ thêm](../../games/typing-defense/art-src/_review/166/md5-diff.txt). Bản băm kiểm lại ban đầu `md5-before-rerun.txt` giống nguyên byte bản đầu.

Đã chạy `magick identify -format '%f %wx%h %[channels] %[colorspace]\n'` trên đúng **32 PNG giao**: 8 × 1024², 8 × 256², 8 × 128², 8 × 64². Tất cả **`srgba`, sRGB**, alpha min 0/max 255; SHA-256 trùng các ứng viên đã kiểm trước công bố. `open xb` chặn ghi đè ở mọi đích media.

## 5. Số đo alpha, lề, tương phản và dáng

Dải mép dùng Disk bán kính 3 px quanh mask alpha ≥128, gồm lỗ trong vật. Ngoài dải đó đếm mọi pixel 0 < alpha <255. Sắc khóa: hue 285–315°, S >0,5 và alpha >0; mẫu số là **pixel alpha >0**, chặt hơn chia toàn canvas. Luma là Y′ = 0,2126R′ + 0,7152G′ + 0,0722B′, kênh sRGB chuẩn hóa 0–1, trung bình vật có trọng số alpha. JSON ghi thêm luminance tuyến tính, không lẫn hai đại lượng.

Hai nền lấy từ **`ui/frames-epic/panel-large.v2.png`**: ngọc trung bình vùng `200x200+412+412` = **`#071f16`**; đá/vàng vùng `200x40+470+35` = **`#bcad98`**. Không dùng hai màu tạm vì panel đã có. Tờ cỡ thật đặt lên cả hai nền; bảng tương phản bên dưới ghi trên nền ngọc.

| Ảnh | Alpha mềm ngoài mép 1024/256/128/64 | Sắc khóa % 1024 / 256 / 128 / 64 |
|---|---|---|
| `gold` | 0 / 0 / 0 / 0 | 0.0798 / 0.0449 / 0.0192 / 0.0709 |
| `wood` | 0 / 0 / 0 / 0 | 0.0413 / 0.0300 / 0.0000 / 0.0000 |
| `food` | 0 / 0 / 0 / 0 | 0.1159 / 0.0659 / 0.0000 / 0.0000 |
| `lives` | 0 / 0 / 0 / 0 | 0.0735 / 0.0491 / 0.0317 / 0.0000 |
| `knowledge` | 0 / 0 / 0 / 0 | 0.0895 / 0.0400 / 0.0000 / 0.0000 |
| `wave` | 0 / 0 / 0 / 0 | 0.1398 / 0.0000 / 0.0593 / 0.0000 |
| `lantern-blazing` | 0 / 0 / 0 / 0 | 0.0622 / 0.0856 / 0.0000 / 0.0000 |
| `seeds` | 0 / 0 / 0 / 0 | 0.1861 / 0.0573 / 0.0000 / 0.0000 |

Tất cả master: cạnh dài hộp alpha >16 **70,3125%**, lệch tâm tối đa **0,04883%** mỗi trục (ngưỡng 2%). IoU đo từ Lanczos trực tiếp 32 px, mask alpha >16 trên cùng canvas; JSON có thêm kết quả alpha ≥128. Phiếu chỉ có một đèn blazing, không có cặp sáng/tắt cần ngưỡng ≥0,95.

| Ảnh | Cỡ 720p / 1080p | Δluma gốc / 720p / 1080p | IoU lớn nhất | Với ảnh |
|---|---|---|---:|---|
| `gold` | 20 / 24 | 0.3985 / 0.3985 / 0.3990 | 0.74232 | `lives` |
| `wood` | 20 / 24 | 0.3173 / 0.3179 / 0.3167 | 0.79375 | `knowledge` |
| `food` | 20 / 24 | 0.4186 / 0.4181 / 0.4195 | 0.73529 | `lantern-blazing` |
| `lives` | 20 / 24 | 0.3832 / 0.3832 / 0.3839 | 0.74232 | `gold` |
| `knowledge` | 16 / 20 | 0.5293 / 0.5246 / 0.5258 | 0.79375 | `wood` |
| `wave` | 20 / 24 | 0.2546 / 0.2560 / 0.2556 | 0.53235 | `knowledge` |
| `lantern-blazing` | 16 / 20 | 0.5325 / 0.5232 / 0.5280 | 0.73529 | `food` |
| `seeds` | 20 / 24 | 0.4676 / 0.4668 / 0.4670 | 0.66842 | `gold` |

**32/32 PNG qua kiểm alpha; 8/8 master qua lề; tương phản ≥0,25 ở cả ba cỡ đo; 28/28 cặp IoU ≤0,80.** Cặp sát ngưỡng nhất Wood–Knowledge 0,79375; không hạ ngưỡng hay căn riêng mask để đạt. Wave tương phản sát ngưỡng nhất, giữ nguyên số để Claude nhìn thêm.

## 6. KA5 · Tự chấm trên bản hậu kỳ

Thứ tự: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. “Dùng tiếp” = 2 vì mọi kiểm số của bản chọn và ba bản thu đạt. Đây là điểm Codex, chưa phải kết luận nhận. M so với độ hoàn thiện HUD của game thương mại trong ảnh chủ dự án, không so bộ cũ.

| Ảnh | KA5 gốc | KA5 720p | M gốc / 720p | Hạn chế cần xem |
|---|---|---|---|---|
| Gold | 10 = 2/2/2/2/2 | 10 = 2/2/2/2/2 | 8,5 / 8 | Ba đồng và lỗ vuông rõ; chạm nhỏ chỉ còn chất liệu. |
| Wood | 10 = 2/2/2/2/2 | 9 = 2/1/2/2/2 | 8 / 8 | Hai khúc và mặt cắt đọc được; vân vỏ gộp ở 20 px. |
| Food | 10 = 2/2/2/2/2 | 9 = 2/1/2/2/2 | 8 / 8 | Dáng bó lúa phân biệt; không đọc từng hạt ở 20 px. |
| Lives | 10 = 2/2/2/2/2 | 10 = 2/2/2/2/2 | 8,5 / 8,5 | Tim đỏ trên nền ngà rõ nhất bộ; giữ vật tròn cũ. |
| Knowledge | 10 = 2/2/2/2/2 | 9 = 2/1/2/2/2 | 8,5 / 8 | Sách mở rõ; bút lông thành vệt sáng nhỏ ở 16 px. |
| Wave | 10 = 2/2/2/2/2 | 9 = 2/1/2/2/2 | 8 / 8 | Cờ/cán nhận ra; vải sẫm, tương phản vừa qua ngưỡng. |
| Lantern Blazing | 10 = 2/2/2/2/2 | 9 = 2/1/2/2/2 | 8 / 8 | Đèn hổ phách rõ; lửa trên nắp rất nhỏ ở 16 px, cần xem cạnh trạng thái lit khi gắn. |
| Seeds | 10 = 2/2/2/2/2 | 9 = 2/1/2/2/2 | 8,5 / 8 | Túi và hạt tràn nhận ra; hạt riêng gộp ở 20 px. |

Tự xem có biết brief, không phải phép thử nhận diện mù hoặc giám khảo độc lập. Đã xem cỡ thật 720p và các tờ so, không chỉ ảnh phóng. Các điểm/hạn chế 8–8,5 ghi ngay tại đây; không sửa `ART_REPLACE_LATER.md` vì ngoài đường dẫn phiếu cho phép.

## 7. Script và chạy lại

Script lưu trong `_review/166/`: `prepare.py`, `refine-prompts.py`, `process.py`, `measure.py`, `repair-wave.py`, `repair-wave-256.py`, `render.py`, `compare-new-set.py`, `final-sheet.py`, `publish.py`, `recheck.py`, `write-report.py`, `sidecars.py`. Các bước tạo ảnh chặn đích cũ hoặc dùng thư mục riêng; không chạy lại công bố lên các tên đã có.

Chạy lại kiểm trên đúng file giao, dùng tên thư mục mới:

```sh
PYTHONDONTWRITEBYTECODE=1 python3   games/typing-defense/art-src/_review/166/recheck.py recheck-owner-01
```

Đo lại ứng viên và 28 cặp IoU, dùng nhãn mới:

```sh
PYTHONDONTWRITEBYTECODE=1 python3   games/typing-defense/art-src/_review/166/measure.py   games/typing-defense/art-src/_review/166/selection-ready.json metrics-owner-01
```

`selection-ready.json` xác định đúng chuỗi giao: Gold/Lives/Knowledge/đèn/Seeds stage1, Wood/Food stage2, Wave `wave-ready`. Mọi bản trước sửa và lượt sinh không chọn vẫn được giữ.

## 8. Khác phiếu, phần chưa làm và việc chủ dự án cần xem

1. Tên phiếu ghi 7 nhưng danh sách cộng Seeds là **8**; giao đủ cả 8. Cỡ dùng không có bảng ngay trong phiếu 166 nên lấy từ kiểm kê UI WW-20/21/22/23/42: tài nguyên và Wave 20/24, Knowledge và đèn 16/20.
2. Dùng bốn mẫu đã nhận của 115 ở `frames-epic/`, do đường dẫn `frames/` chưa có. Emblem và keyart vẫn đính kèm đúng đường dẫn phiếu yêu cầu.
3. **Chưa có đủ bốn icon mới đã nhận để đặt cạnh.** Bốn mẫu 115 đã nhận nằm ở hàng cuối tờ chính; tờ `166-new-set.jpg` đặt từng icon mới cạnh Day, Night, Review Book, Seeds của đúng bộ cuối 134 và ghi rõ “chờ nhận”. Không tự gọi các icon 134 là đã được Claude nhận. Phần trạng thái nhận của yêu cầu này còn chờ Claude.
4. Giữ `166-sheet.jpg` bản đầu, thêm `166-sheet-final.jpg` để dùng bản alpha sạch của các tham chiếu. Không ghi đè file ảnh nào. Bản gốc công cụ 1254² được giữ và chuẩn hóa về 1024² như đã giải thích.
5. Chưa chấm lại bởi Claude, chưa chép `public/`, chưa gắn hoặc kiểm runtime vì ngoài phạm vi và phiếu cấm chạy game/trình duyệt. Không gọi đây là nghiệm thu cuối.

**Chủ dự án/Claude cần xem:** tờ cuối và cỡ 720p nguyên tỉ lệ; Wave sẫm nhưng đạt luma; bút của Knowledge và trạng thái blazing ở 16 px; so Wood–Knowledge sát ngưỡng IoU. Sau khi Claude chấm lại từ 8, Claude chọn đúng các bản `.v2`/Seeds và chép vào `public/` khi gắn.
