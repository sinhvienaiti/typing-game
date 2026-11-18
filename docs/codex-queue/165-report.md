# Phiếu 165 · Wordwoven · Sáu nhà, cặp đèn lồng và hai icon khay mép

Ngày làm: 29/10/2026, repo cha trên Mac mini M4, macOS. Dùng **`image_gen` tích hợp**, không gọi API/CLI sinh ảnh khác.

**Đã giao 10 bản chọn 1024² và 30 bản thu, giữ đủ 11 lượt sinh cùng prompt. Cả 40 PNG giao đạt kiểm số; tự chấm M ≥ 8 và KA5 ≥ 8 ở bản gốc lẫn cỡ 720p. Chưa nghiệm thu Claude. Còn một khác biệt ở yêu cầu tờ so: chưa tìm thấy bốn icon độc lập của bộ mới đã được Claude nhận, nên dùng bốn phần tử khung 115 đã nhận; không tự gán trạng thái nhận cho các icon phiếu khác.**

## 1. Nơi giao và ảnh cần xem

- [Nhà](../../games/typing-defense/art-src/ui/buildings/): `keep.v2`, `archer.v2`, `cannon.v2`, `barracks.v2`, `gold-mine.v2`, `farm.v2`.
- [Đèn lồng](../../games/typing-defense/art-src/ui/lanterns/): `lantern-unlit.v2`, `lantern-lit.v2`.
- [Khay mép](../../games/typing-defense/art-src/ui/tray/): `tray-arrow`, `tray-call`.
- Mỗi tên có `.png`, `.256.png`, `.128.png`, `.64.png`, cùng `.prompt.txt` cạnh từng PNG. Mọi `.tryN.png` và `.tryN.prompt.txt` được giữ nguyên.
- [Tờ xem bốn hàng](../../games/typing-defense/art-src/_review/165-sheet.jpg), [so cũ–mới 64/32 px](../../games/typing-defense/art-src/_review/165-old-new.jpg), [720p cỡ thật và phóng nearest để soi](../../games/typing-defense/art-src/_review/165-720p.jpg).
- [Mười tờ bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/165/sheets/), [mười tờ so cùng vị trí và tỉ lệ](../../games/typing-defense/art-src/_review/165/registered-v2/). Tờ thứ hai chỉ crop/thu bản sinh để đặt đúng vị trí với ảnh giao; không key hoặc sửa phần vẽ ở vế bản sinh.
- [Hồ sơ, script và số đo](../../games/typing-defense/art-src/_review/165/), [kiểm cuối trên đúng file giao](../../games/typing-defense/art-src/_review/165/final-check/audit.json), [nguồn công cụ và đối chiếu bản thử](../../games/typing-defense/art-src/_review/165/final-check/summary.json).

Chỉ thêm file trong các đường dẫn phiếu cho phép. Không chạy lệnh Git, build/test game, game, dev server, trình duyệt hay mạng ngoài công cụ sinh ảnh; không đọc/ghi Tu Tiên hoặc `.wt-*`, không ghi game khác. Không tạo âm thanh hoặc sửa runtime. Không chép vào `public/`; Claude thực hiện khi nhận. Không có capture trình duyệt hay chuỗi raw frame cần prune.

## 2. Tham chiếu và prompt từng lượt

Bốn mẫu 115 đã được nhận ở `accept-29-10/verdict.md`: **banner, portrait-ring, crest, divider**. Đường dẫn thật là `ui/frames-epic/`, còn `ui/frames/` trong phiếu chưa tồn tại. Huy hiệu dùng đúng `ui/title-epic/emblem.png`; ảnh chủ đạo là `ui/title-epic/keyart.png`. Đã xem ảnh chủ dự án `_refs/owner-epic-2026-10-28.webp`, lấy mức hoàn thiện HUD, không chép nội dung.

Công cụ nhận tối đa **5 đường dẫn tham chiếu**. Vì vậy ghép nguyên bốn ảnh khung thành [một bảng tham chiếu](../../games/typing-defense/art-src/_review/165/115-accepted-style-board-v2.png), chỉ thu giữ tỉ lệ và bố trí bốn ô không chồng nhau. Mỗi lượt nhà/đèn tắt đính kèm: ảnh cũ cùng tên, bảng bốn khung, emblem, keyart, ảnh chủ dự án. Hai icon mới đính kèm bốn ảnh tham chiếu sau, không có vật cũ. Lượt đèn sáng dùng: đèn tắt mới làm ảnh sửa chính, đèn sáng cũ để giữ nhận diện, bảng bốn khung, emblem, keyart; không đính kèm thêm ảnh chủ dự án vì giới hạn 5 ảnh.

Mỗi prompt mở bằng **STYLE-UI mới của 115 nguyên văn + ICON của tài liệu định dạng nguyên văn**, sau đó ghi rõ ưu tiên mới khi hai khối mâu thuẫn: chất liệu hoàn thiện có chiều sâu, bỏ viền mực/tô phẳng, cạnh dài 70% thay cho 80%, trình bày gần chính diện và giữ nhận diện vật. Phần riêng kết thúc bằng dòng nền M nguyên văn. Tám ảnh vẽ lại có đúng câu **“Keep the same object identity as the attached image. Repaint it in the new style as described.”** Không dùng STYLE storybook cũ.

| Tên | Lượt giữ / chọn | Khóa nội dung và thay đổi prompt |
|---|---|---|
| `keep.v2` | 1 / try1 | Fort tròn, hai tầng mái ngói son, cờ kem trống, cổng và bậc đá; thêm vật liệu ngọc/đồng/vàng của bộ mới. |
| `archer.v2` | 1 / try1 | Tháp cao hẹp, mái chóp tranh, cung và tên lớn, chân đá; giữ nhận diện tre/gỗ, nâng chất liệu và đầu nối đồng. |
| `cannon.v2` | 1 / try1 | Pháo đồng chĩa lên phải, lỗ nòng tối viền sáng, ụ tròn thấp, đạn sắt bên trái. |
| `barracks.v2` | 1 / try1 | Nhà mái tranh rộng, rào gỗ, trống son bên trái và ba khiên bên phải; đồng chạm và ngọc tiết chế. |
| `gold-mine.v2` | **1, 2 / try2** | Try1 đẹp nhưng dáng bè, IoU với Cannon **0,8056**, với Farm **0,8186**. Lượt 2 yêu cầu vách đá vôi nhọn cao, tời chiếm 1/3 trên, xe quặng nhỏ ở cửa, nền hẹp; bỏ sàn phụ trải rộng, giữ cửa mỏ, mái ngói, tời, cờ và quặng. Không bóp méo alpha bằng công cụ để qua IoU. |
| `farm.v2` | 1 / try1 | Ruộng nước bạc–ngọc, nhà sàn mái tranh góc trên phải, bù nhìn nón lá; bờ đá vôi và phụ kiện đồng cùng bộ. |
| `lantern-unlit.v2` | 1 / try1 | Giấy ngà không lửa trong, gân đồng, nắp ngọc, quai và tua son; giấy đủ sáng nhờ ánh ngoài để đọc ở 16 px. |
| `lantern-lit.v2` | 1 / try1 | **Sửa chính ảnh unlit mới**, khóa nguyên hình, nắp, gân, quai, tua, vị trí; chỉ đổi ánh giấy sang hổ phách từ bên trong, ánh nằm trong vật, không halo ngoài. |
| `tray-arrow` | 1 / try1 | Mũi tên đồng chỉ phải, đầu tam giác rộng, chuôi ngắn khuyết mây, khảm ngọc và cạnh vàng sáng. |
| `tray-call` | 1 / try1 | Vòng ngọc rỗng lớn, ba đầu sợi ánh gọi gắn vào góc trên phải; lòng vòng khóa M để tách trong suốt. |

Tổng **11 lượt sinh thành công**; không ảnh nào vượt 2 lượt. Prompt chính xác nằm cạnh bản thử và bản chọn, cùng từng `*.tryN.record.json` trong review. **11/11 bản thử trùng nguyên byte với PNG nguồn công cụ; 11/11 prompt khớp bản đã gửi** (chỉ bỏ newline cuối khi đối chiếu văn bản).

## 3. Hậu kỳ và đối chiếu không phá tranh

Giữ nguyên PNG sinh trong `.tryN.png`; bản chọn được tách alpha và thu về **1024 × 1024, sRGB RGBA**. Dùng bản sao nguyên trạng của bốn file `key-alpha.sh`, `common.sh`, `normalize.py`, `seam_analysis.py` trong review, có SHA-256 ở `art-normalize-source-sha256.json`, để WORK của công cụ không ghi ra ngoài vùng phiếu.

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash games/typing-defense/art-src/_review/165/art-normalize/key-alpha.sh \
  IN.tryN.png OUT.key.png --bg '#FF00FF' --mode global \
  --despill protect-interior
```

Không bật `--no-key-hue`, không chỉnh sáng, gamma, bão hòa hoặc vật liệu. Cắt khoảng trống quanh **toàn bộ alpha > 0**, thêm 4 px nguồn rồi Lanczos fit trong 724², đặt giữa canvas 1024². Hộp alpha > 16 thực tế còn cạnh dài **720 px = 70,3125%**. Không cắt phần vẽ để đạt lề. Ba bản thu đều lấy **trực tiếp từ bản gốc 1024²**, không thu nối tiếp, không làm nét bản 64.

Phép thu Lanczos phát sinh alpha 254 trong vùng đục và ringing rất yếu ở ngoài mép. Chỉ sửa **alpha** ngoài dải Disk:3 quanh ranh alpha ≥ 128: phía trong về 255, phía ngoài về 0, RGB giữ nguyên. Trên 10 bản gốc: **264 pixel trong + 34 pixel ringing ngoài**; ringing ngoài có alpha tối đa **22/255**. Trên 30 bản thu: **337 pixel trong + 56 pixel ngoài**, alpha ringing ngoài tối đa **4/255**. Toàn bộ bản trước sửa giữ trong review, kèm nhật ký từng ảnh; không xóa `.try*`, không phủ màu hoặc thay phần vẽ.

Riêng `lantern-lit.v2.64.png` còn **2 pixel AA tím tối** làm tỷ lệ sắc khóa thành **0,2336%**. Hai pixel ở **(17,30), alpha 19** và **(18,36), alpha 41** đều nằm trong dải mép 3 px. Khử sắc khóa bằng lấy RGB mép đồng liền kề ở (18,30) và (19,36), giữ nguyên alpha; không làm nét. [Tờ trước–sau ×10](../../games/typing-defense/art-src/_review/165/registered-v2/lantern-lit-64-edge-before-after.jpg), tọa độ/RGBA đầy đủ ở `package-ready/lit64-edge-repair.json`. Bản giao 64 này còn **0 pixel sắc khóa**.

Hai thử nghiệm `edge-repair.py`/`edge-repair-v2.py` định khử mọi sắc khóa đã **tự dừng trước khi viết ảnh** vì gặp pixel nằm trong vùng đục hoặc lỗ rất nhỏ không đủ điều kiện sửa mép. Không dùng chúng cho bộ giao, không đổi sơn để ép 0%. Giữ tỷ lệ còn dư trong mức ≤ 0,2% của phiếu. Chuỗi giao thật là `final-stage → package-stage → package-final → package-ready → ui/`.

## 4. KA1, khổ, alpha, tương phản và dáng

**MD5** trên mọi file đệ quy trong ba thư mục đích `ui/buildings`, `ui/lanterns`, `ui/tray`, cùng đường dẫn tương đối và thứ tự trước/sau:

| Mốc | Số file |
|---|---:|
| Trước | 37 |
| Sau | 139 |
| Thêm | **102** = 22 file thử/prompt + 80 file giao/prompt |
| Sửa / xóa file cũ | **0 / 0** |
| Dòng `<` trong diff | **0** |

[MD5 trước](../../games/typing-defense/art-src/_review/165/md5-before.txt), [MD5 sau](../../games/typing-defense/art-src/_review/165/md5-after.txt), [diff chỉ thêm](../../games/typing-defense/art-src/_review/165/md5-diff.txt). Review và báo cáo không nằm trong phép băm media này, tránh tự băm chính file danh sách.

**Khổ:** đã chạy `magick identify -format '%f %wx%h %[channels]\n'` trên đúng **40 PNG giao**: 10 × 1024², 10 × 256², 10 × 128², 10 × 64²; tất cả **`srgba`**, alpha min **0**, max **255**. [Đủ 40 dòng identify](../../games/typing-defense/art-src/_review/165/final-check/identify.txt). SHA-256 xác nhận 80 file chọn/prompt trong UI trùng bộ đã kiểm trước công bố; mọi đích đều được guard không tồn tại rồi mở độc quyền.

**Alpha:** dải mép dùng Disk bán kính 3 px quanh ranh alpha ≥ 128, gồm cả lỗ bên trong vật. Ngoài dải đó, đếm mọi pixel có 0 < alpha < 255. Sắc khóa đếm trên mọi pixel alpha > 0, hue 285–315°, S > 0,5; mẫu số là số pixel alpha > 0, chặt hơn chia cho toàn canvas.

| Ảnh | Alpha mềm ngoài mép, 1024/256/128/64 | Sắc khóa %, 1024 / 256 / 128 / 64 |
|---|---|---|
| `keep.v2` | 0 / 0 / 0 / 0 | 0,0766 / 0,0390 / 0,0373 / 0,0000 |
| `archer.v2` | 0 / 0 / 0 / 0 | 0,1405 / 0,0717 / 0,0591 / 0,1050 |
| `cannon.v2` | 0 / 0 / 0 / 0 | 0,0795 / 0,0373 / 0,0000 / 0,0000 |
| `barracks.v2` | 0 / 0 / 0 / 0 | 0,1562 / 0,0649 / 0,0622 / 0,0000 |
| `gold-mine.v2` | 0 / 0 / 0 / 0 | 0,0435 / 0,0246 / 0,0000 / 0,0000 |
| `farm.v2` | 0 / 0 / 0 / 0 | 0,0672 / 0,0143 / 0,0182 / 0,0000 |
| `lantern-unlit.v2` | 0 / 0 / 0 / 0 | 0,0258 / 0,0174 / 0,0000 / 0,0000 |
| `lantern-lit.v2` | 0 / 0 / 0 / 0 | 0,0435 / 0,0521 / 0,0326 / 0,0000 |
| `tray-arrow` | 0 / 0 / 0 / 0 | 0,1569 / 0,0440 / 0,0410 / 0,0000 |
| `tray-call` | 0 / 0 / 0 / 0 | 0,1732 / 0,1044 / 0,0241 / 0,0831 |

**Tương phản:** lấy màu từ `panel-large.v2.png` hiện có của 115: ngọc **`#071f16`** là trung bình vùng `200x200+412+412`, đá vôi **`#bcad98`** là trung bình vùng `200x40+470+35`. [Palette và cách lấy mẫu](../../games/typing-defense/art-src/_review/165/metrics-final-stage/palette.json). Bản panel chỉ dùng lấy màu, không khẳng định đã nhận lại năm khung sửa. Dùng luma Rec.709 trên kênh sRGB chuẩn hóa: **Y′ = 0,2126 R′ + 0,7152 G′ + 0,0722 B′**, trung bình vật có trọng số alpha. Độ chênh là trị tuyệt đối giữa trung bình vật và nền. JSON ghi thêm luminance tuyến tính để truy vết, không trộn hai đại lượng hoặc đổi sang WCAG để chấm luma.

Đo trực tiếp **32 mẫu ở đúng cỡ trong game**. Nhà có hai ngữ cảnh: team **20/24 px**, menu **28/34 px**; đèn **16/20 px**; khay **24/32 px** (720p/1080p). Bảng dưới ghi chênh nhỏ nhất qua mọi cỡ của ảnh, không lấy cỡ thuận lợi nhất. Tất cả đạt ≥ 0,25 trên ngọc tối.

| Ảnh | Cỡ 720p / 1080p | Δ luma ngọc tối, min | Δ luma đá vôi, min | IoU max với ảnh khác ở 32 px | Cặp gần nhất |
|---|---|---:|---:|---:|---|
| `keep.v2` | 20,28 / 24,34 | 0,3868 | 0,1986 | 0,7839 | `gold-mine` |
| `archer.v2` | 20,28 / 24,34 | 0,3964 | 0,1879 | 0,7123 | `gold-mine` |
| `cannon.v2` | 20,28 / 24,34 | 0,3225 | 0,2625 | 0,7743 | `farm` |
| `barracks.v2` | 20,28 / 24,34 | 0,2970 | 0,2876 | 0,7220 | `cannon` |
| `gold-mine.v2` | 20,28 / 24,34 | 0,3664 | 0,2191 | 0,7839 | `keep` |
| `farm.v2` | 20,28 / 24,34 | 0,3848 | 0,2010 | 0,7743 | `cannon` |
| `lantern-unlit.v2` | 16 / 20 | 0,5171 | 0,0642 | 0,5743 | `keep` |
| `lantern-lit.v2` | 16 / 20 | 0,5125 | 0,0685 | 0,5714 | `keep` |
| `tray-arrow` | 24 / 32 | 0,3564 | 0,2283 | 0,5032 | `barracks` |
| `tray-call` | 24 / 32 | 0,4046 | 0,1809 | 0,6077 | `cannon` |

**Lề và tâm:** cả 10 bản gốc có cạnh dài alpha > 16 bằng **70,3125%**, lệch tâm lớn nhất theo mỗi trục **0,0489%**, trong mức 68–72% và ≤ 2%. [Hộp bao từng ảnh, đầy đủ 45 cặp IoU](../../games/typing-defense/art-src/_review/165/metrics-final-stage/metrics.json).

**IoU:** Lanczos trực tiếp 1024 → 32, alpha > 16, cùng canvas, không dịch riêng mặt nạ để có lợi. Ghi thêm đối chứng alpha ≥ 128. Có **44 cặp khác vật**, IoU lớn nhất **0,783862** (Keep/Gold Mine), đều ≤ 0,80. Cặp sáng/tắt của cùng đèn được tách khỏi cột max trên: **IoU 0,995025** với alpha > 16 và **1,000000** với alpha ≥ 128, đạt ≥ 0,95.

## 5. KA5 · Tự chấm trên bản hậu kỳ giao

Thứ tự Q: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Cỡ 720p dùng cỡ nhỏ nhất thực tế: nhà 20, đèn 16, khay 24 px. “Dùng tiếp” được 2 vì đủ khổ, alpha, sắc khóa, lề, tâm, luma và IoU; đây không phải điểm nghiệm thu của Claude. M là mức hoàn thiện so HUD thương mại của ảnh chủ dự án, không chấm theo bộ icon cũ của ta.

| Ảnh | M gốc / 720p | Q gốc | Q 720p | Thiếu ở cỡ nhỏ |
|---|---|---|---|---|
| `keep.v2` | 8,5 / 8 | 10 = 2/2/2/2/2 | 9,5 = 2/1,5/2/2/2 | Hai tầng mái và cổng đọc được; nét chạm và khoen cửa không còn riêng. |
| `archer.v2` | 8 / 8 | 9,5 = 2/2/1,5/2/2 | 8,5 = 2/1/1,5/2/2 | Dáng tháp cao và mái nhọn rõ; cung/tên khó tách ở 20 px. Tre/tranh vẫn ấm hơn khung ngọc. |
| `cannon.v2` | 8,5 / 8 | 10 = 2/2/2/2/2 | 9,5 = 2/1,5/2/2/2 | Nòng nhô chéo đọc được; mất đạn và khắc nhỏ. |
| `barracks.v2` | 8 / 8 | 9,5 = 2/2/1,5/2/2 | 8,5 = 2/1/1,5/2/2 | Nhà rộng thấp khác tháp; trống/khiên không còn tách rõ ở 20 px. |
| `gold-mine.v2` | 8,5 / 8 | 10 = 2/2/2/2/2 | 9,5 = 2/1,5/2/2/2 | Núi nhọn, cửa mỏ tối, quặng vàng rõ; dây tời không còn đọc riêng. |
| `farm.v2` | 8 / 8 | 9,5 = 2/2/1,5/2/2 | 9 = 2/1,5/1,5/2/2 | Ruộng nước và nhà bên phải rõ; bù nhìn chỉ còn khối vàng. |
| `lantern-unlit.v2` | 8,5 / 8 | 10 = 2/2/2/2/2 | 9,5 = 2/1,5/2/2/2 | Giấy ngà đọc rõ, phân biệt đèn sáng; mất hoa văn nắp và tua. |
| `lantern-lit.v2` | 8,5 / 8 | 10 = 2/2/2/2/2 | 9,5 = 2/1,5/2/2/2 | Ánh hổ phách phân biệt trạng thái, cùng hình đèn; mất hoa văn. |
| `tray-arrow` | 8,5 / 8,5 | 10 = 2/2/2/2/2 | 10 = 2/2/2/2/2 | Đầu chỉ phải và chuôi mây rõ; khắc chỉ còn chất liệu. |
| `tray-call` | 8,5 / 8,5 | 10 = 2/2/2/2/2 | 10 = 2/2/2/2/2 | Lỗ vòng và ba đầu ánh gọi đọc được; hạt khảm chỉ còn điểm sáng. |

So cùng cỡ 64/32 px, bộ mới giữ nhận diện cũ, tăng chất liệu đá/đồng/ngọc và bỏ viền mực. Ở cỡ rất nhỏ, sắc giấy ngà/hổ phách còn tách trạng thái đèn; đèn trên đá vôi kém tương phản hơn trên ngọc, đã ghi nguyên số, không làm tối tranh để ép cả hai nền đạt. Mái tranh, tre và ruộng được giữ vì yêu cầu cùng vật; không tự đổi công trình sang bộ model khác.

## 6. Khác phiếu, việc chưa làm và bàn giao Claude

1. **Đường dẫn tham chiếu:** dùng `frames-epic/` thật của 115 thay `frames/` chưa có; đủ bốn ảnh đã nhận. Do giới hạn công cụ, bốn ảnh được ghép thành một bảng tham chiếu không chồng nhau, không bỏ mẫu nào.
2. **Bốn icon đã nhận để đặt cạnh:** chưa tìm thấy biên bản nhận bốn icon độc lập mới của Wordwoven. Phiếu 133, 172 và 180 còn ghi chờ Claude; không mượn trạng thái nhận của game khác. Mỗi ảnh mới đã đặt cạnh **bốn phần tử khung 115 được nhận** và crop HUD chủ dự án. Đây là mẫu thay thế có ghi nhãn, **chưa đáp ứng nguyên nghĩa “bốn icon độc lập đã nhận”**. Claude cần xác nhận dùng nhóm 115 làm mốc hoặc cung cấp bốn icon đã nhận để bổ sung tờ so; không cần sinh lại mười ảnh vì việc này.
3. **Kích thước trong game:** phiếu 165 không có bảng cho tám ảnh cũ; lấy đúng `UI_IMAGERY.md` WW-32, WW-37, WW-42. Keep dùng chung hai cỡ nhà để so nhất quán, có ghi rõ ngữ cảnh.
4. **Hậu kỳ:** không ép tỷ lệ sắc khóa về 0% trong phần vẽ. Giữ số dưới ngưỡng 0,2%, chỉ sửa alpha nội suy và hai pixel AA của bản đèn sáng 64. Không xóa/san/phủ phần tranh, không chỉnh sáng.
5. **Không chọn Gold Mine try1** vì IoU trượt; giữ nguyên cả PNG và prompt. Không dùng `edge-stage*` hoặc các ứng viên `package-stage`, `package-final` để gắn; bộ cuối đã được chép đúng tên vào **UI**.
6. **Chưa chép vào public, chưa tích hợp mã, chưa có điểm Claude**: các việc đó thuộc người nhận. Không sửa `ART_REPLACE_LATER.md` hoặc tài liệu khác vì phiếu chỉ cho ghi báo cáo này. Claude xem điểm M = 8 và các thiếu hụt cỡ nhỏ ở bảng trên khi quyết định ghi nâng cấp sau.

**Đề nghị xem trước:** tờ `165-sheet.jpg`, `165-old-new.jpg`, mười tờ `registered-v2/*-registered-before-after.jpg`, riêng tháp Archer/Barracks ở 20 px và hai trạng thái đèn ở 16 px. Kiểm số đã đạt; việc nhận toàn phiếu còn phụ thuộc Claude chấm lại ≥ 8 và xử lý mẫu so bốn icon nêu trên.

## 7. Script chạy lại và hồ sơ chuẩn

- `prepare.py`, `prepare-references.py`, `plan-final.json`, `plan-lit-edit.json`, từng `*.tryN.record.json`: prompt và đầu vào sinh. `115-accepted-style-board-v2.png` là bảng thật đã dùng; bản bảng đầu không dùng được giữ để truy vết.
- `process.py`: key và ứng viên lượt 1; `finish.py`: chọn Gold Mine try2, fit và sửa alpha gốc; `final-stage/processing.json` ghi lệnh/crop/số pixel.
- `package.py`, `package-final.py`, `package-ready.py`: Lanczos trực tiếp, sửa alpha bản thu, khử sắc khóa đúng hai pixel lit64. Các bản trung gian không ghi đè.
- `measure.py`, `measure-final.py`, `game-size-metrics.py`, `audit-package.py`: lề/tâm, luma, 45 cặp IoU và kiểm đủ 40 PNG. `metrics-try1/` giữ kết quả trượt; **`metrics-final-stage/`, `game-size-check/`, `final-check/`** là số dùng báo cáo.
- `render.py`, `registered-review-v2.py`: tờ xem và đối chiếu; Arial đúng `/System/Library/Fonts/Supplemental/Arial.ttf`. Prompt của tờ kiểm ghi lệnh ImageMagick, phân biệt với prompt sinh.
- `publish.py`: kiểm hết đích trước rồi mở độc quyền; `md5-audit.py`: `md5 -r`/diff; `recheck.py`: kiểm lại file UI và tính nguyên vẹn.

Kiểm lại vào **một nhãn mới**, không sinh ảnh, không ghi đè hoặc sửa UI:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
PYTHONDONTWRITEBYTECODE=1 python3 \
  games/typing-defense/art-src/_review/165/recheck.py recheck-owner-01
```

Mọi script xuất từ chối đích đã có; chọn nhãn mới khi chạy lại. **Không chạy `publish.py` lần hai lên bộ đã giao.** Ở lần kiểm cuối: 40/40 PNG đạt, 80/80 file chọn/prompt không đổi sau công bố, 11/11 lượt thử nguyên byte và đúng prompt; MD5 chỉ thêm 102 file.
