# Phiếu 172 · Wordwoven · Huy hiệu trạng thái trên thẻ chữ

Ngày làm: 29/10/2026, repo cha trên Mac mini M4, macOS. Sinh bằng **`image_gen` tích hợp**, không gọi API ngoài.

**Đã tạo đủ 8 ảnh, mỗi ảnh một lượt sinh; bộ chọn cuối có 32 PNG đạt kiểm số và đủ prompt. Chờ Claude chấm lại ≥ 8. Có một khác biệt về nơi giao cần đọc trước: bộ chọn cuối nằm trong [_review/172/delivery-final/](../../games/typing-defense/art-src/_review/172/delivery-final/).**

Thư mục [ui/badges/](../../games/typing-defense/art-src/ui/badges/) giữ 8 bản sinh nguyên byte, 8 bản gốc hậu kỳ và các bản thu đã xuất ban đầu. Tôi đã xuất các bản thu trước khi kiểm alpha đủ cả 32 file. Kiểm mở rộng phát hiện **7 bản thu có tổng 12 pixel alpha ngoài dải mép**. Đã làm bộ sửa hoàn chỉnh riêng, không ghi đè file nào. Claude lấy **đồng bộ 32 PNG trong `delivery-final/`** khi duyệt và tích hợp; không lấy lẫn bảy bản thu cũ liệt kê ở mục 4.

## 1. Phạm vi và ảnh tham chiếu

Chỉ ghi `games/typing-defense/art-src/ui/badges/`, `_review/172*` và báo cáo này. Không chạy Git, build, test suite, game, dev server, trình duyệt hay mạng ngoài công cụ sinh ảnh; không đọc/ghi Tu Tiên, không ghi game khác, không sửa mã hay tài liệu khác. Không có ảnh chụp trình duyệt mới hoặc chuỗi frame cần dọn bằng `capture-prune`.

Đã đọc `ART_ACCEPTANCE.md` §2.2, §5, phiếu 115, biên bản nhận 29/10 và định dạng ICON của Wordwoven. Dùng skill **imagegen**. Không dùng bộ STYLE cũ có từ “storybook”.

- Ba tham chiếu 115 đã nhận là `ui/frames-epic/banner.png`, `crest.png`, `divider.png`; đường dẫn `ui/frames/` trong phiếu chưa có trên máy. Cả ba được **đính kèm vào từng lượt sinh**.
- `ui/title-epic/keyart.png` của 113 cũng đính kèm vào cả tám lượt để giữ bảng màu và thế giới.
- Hai trạng thái `pip-full`, `pip-gold` đính kèm thêm chính `pip-empty.try1.png` để giữ ổ đá.
- Đã xem ảnh chủ dự án `_refs/owner-epic-2026-10-28.webp`; lấy mức hoàn thiện kim loại, khối ngọc và độ rõ HUD, không chép hình.
- Nền thử lấy từ `panel-large.v2.png` của 115: ngọc **`#051b14`** tại (512,512), đá vôi **`#cfc1b1`** tại (60,512). Bản này chỉ dùng lấy màu chất liệu. Có đo thêm hai màu tạm của phiếu trong JSON.
- Chỉ đọc ảnh có sẵn trong `games/.wt-td-1c/tmp/lane-l3/sheets3/` theo yêu cầu riêng của phiếu; không ghi vào worktree.

## 2. Lượt sinh và prompt

Mỗi prompt ghép **STYLE-UI mới của 115, nguyên văn + ICON của tài liệu định dạng, nguyên văn + khóa riêng của phiếu + nội dung ảnh + dòng nền M nguyên văn**. Khối riêng ghi rõ cách ưu tiên khi ICON cũ yêu cầu chiếm 80% và góc 3/4: phiếu 172 dùng vật chiếm 70%, nhìn thẳng, khối chạm nổi sáng rõ. Không có chữ, số, ký hiệu chữ cái, logo hay khung trang trí bao ngoài vật. Viền kim loại là một phần thân vật.

| Ảnh | Lượt / bản chọn | Nội dung khóa trong prompt |
| --- | --- | --- |
| `pip-empty` | try1 / try1 | Ổ ngọc tròn, bát rỗng tối, môi đá vôi sáng; tâm tối chiếm nửa đường kính. |
| `pip-full` | try1 / try1 | Giữ chính ổ rỗng đính kèm, chỉ thay tâm thành hạt ngọc mint lồi, sáng; ánh sáng nằm trong vật. |
| `pip-gold` | try1 / try1 | Giữ cùng ổ, tâm vàng hổ phách, khác rõ tâm ngọc ở 8 px. |
| `badge-ok` | try1 / try1 | Thân ấn là nét kiểm bất đối xứng, hai nhánh dày, không có đĩa nền. |
| `badge-flash` | try1 / try1 | Thân ấn là tia chớp ngọc hai bậc, dáng đứng hẹp; không có đĩa nền. |
| `badge-calling` | try1 / try1 | Ba cung sóng dày, khe thoáng rộng, mọc từ hạt ngọc ở dưới trái. |
| `badge-review` | try1 / try1 | Mũi tên cuộn ba phần tư vòng, khe dưới phải, lá ngọc đứng ở giữa. |
| `badge-chain` | try1 / try1 | Đúng hai vòng ngọc lồng chéo, hai lỗ lớn, viền đồng/vàng cùng bộ. |

**Không có lượt 2 hoặc 3.** Các điểm thiếu còn lại là độ dày hoa văn khi thu rất nhỏ; không cần sinh lại để chữa lỗi alpha nội suy. Toàn bộ `.try1.png` và `.try1.prompt.txt` giữ nguyên. Prompt chính xác nằm cạnh từng PNG sinh, bản chọn và bản thu; bảng tổng ở [prompts.json](../../games/typing-defense/art-src/_review/172/prompts.json). [generation-records.json](../../games/typing-defense/art-src/_review/172/generation-records.json) ghi nguồn công cụ và toàn bộ ảnh đính kèm. SHA-256 xác nhận **8/8 bản thử trùng nguyên byte nguồn công cụ**.

## 3. Hậu kỳ giữ tranh · ART_ACCEPTANCE §5

Ảnh sinh vuông **1254 × 1254** được giữ nguyên. Bản giao là 1024² sRGB RGBA sau tách nền M. Dùng bản sao nguyên trạng của bốn file `art-normalize` trong vùng cho phép; băm xác nhận trùng công cụ repo. WORK của công cụ nằm dưới `_review/172/art-normalize/.tmp/`, không ghi vào `tools/`.

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash games/typing-defense/art-src/_review/172/art-normalize/key-alpha.sh \
  INPUT.try1.png KEY.png --bg '#FF00FF' --mode global \
  --despill protect-interior --no-key-hue
```

Trim phần nền trong suốt, Lanczos giữ tỷ lệ để cạnh dài vật bằng **717 px**, đặt giữa canvas 1024². Không cắt phần vẽ, không ghép lại lòng hay viền, không san phẳng, không phủ màu, không chỉnh gamma/độ sáng. Sau đổi cỡ, làm tròn alpha gần nhị phân ở đúng các pixel lỗi ngoài dải mép: số pixel của tám bản gốc lần lượt **2 / 4 / 1 / 0 / 0 / 13 / 4 / 3**, đổi tối đa 5/255, **RGB đổi 0 pixel**. Chi tiết ở `edge-corrections.json`.

Ba bản thu **256², 128², 64² đều Lanczos trực tiếp từ bản 1024²**, không thu nối tầng, không làm nét bản 64. Trong bộ chọn cuối, bảy bản thu có bước sửa alpha mép sau Lanczos, chỉ đổi 12 pixel một mức 1/255; RGB nguyên vẹn. Đây là sửa mép được §5 cho phép, không thay tranh. Kiểm so sánh xác nhận mọi pixel khác đúng đầu ra Lanczos trực tiếp.

Mỗi ảnh có tờ **“bản sinh | bản hậu kỳ”**, hai canvas cùng 1024 px, xem trong [visual-delivered/](../../games/typing-defense/art-src/_review/172/visual-delivered/): `<tên>-before-after.jpg`. Đã xem cả tám bản hậu kỳ ở 1024² và ở cỡ thật trước khi chấm.

## 4. Khổ và alpha · bộ chọn cuối

**32/32 PNG đúng khổ và `srgba 4.0`**: mỗi ảnh có 1024², 256², 128², 64². Bảng identify đầy đủ ở [audit-final-bundle/identify.txt](../../games/typing-defense/art-src/_review/172/audit-final-bundle/identify.txt), chạy bằng `magick identify -format '%f %wx%h %[channels]\n'`.

Hộp bao alpha > 16 có cạnh dài **717/1024 = 70,0195%** cho cả tám ảnh. Lệch tâm lớn nhất theo mỗi trục **0,04883%**, dưới 2%. Alpha min/max **0/255**.

Phép kiểm mép: lấy đường biên alpha ≥ 128, nở/co **Disk:3** để có dải mép Euclid 3 px; đếm alpha 1–254 ngoài dải. Phép kiểm màu khóa: mọi pixel alpha > 0, hue 285–315°, S > 0,5; mẫu số là số pixel alpha > 0, chặt hơn chia cho toàn canvas. Không bỏ qua pixel alpha thấp.

| Ảnh | Alpha lẻ ngoài mép 3 px, cả 4 khổ | % màu khóa: 1024 / lớn nhất 4 khổ | Δ luma nền ngọc: 720p / 1080p | IoU lớn nhất ở 32 px, khác vật |
| --- | ---: | ---: | ---: | --- |
| `pip-empty` | 0 | 0.03863 / 0.03863 | 0.3942 / 0.3923 | 0.6753 · `badge-review` |
| `pip-full` | 0 | 0.04694 / 0.04694 | 0.5145 / 0.5149 | 0.6753 · `badge-review` |
| `pip-gold` | 0 | 0.04864 / 0.04864 | 0.4892 / 0.4886 | 0.6753 · `badge-review` |
| `badge-ok` | 0 | 0.07736 / 0.07736 | 0.3836 / 0.3853 | 0.3927 · `badge-chain` |
| `badge-flash` | 0 | 0.11705 / 0.11705 | 0.4859 / 0.4838 | 0.3321 · `badge-chain` |
| `badge-calling` | 0 | 0.13770 / 0.13770 | 0.4283 / 0.4281 | 0.5848 · `pip-empty` |
| `badge-review` | 0 | 0.07078 / 0.09679 | 0.4115 / 0.4132 | 0.6753 · `pip-empty` |
| `badge-chain` | 0 | 0.13833 / 0.13833 | 0.4555 / 0.4539 | 0.5892 · `pip-empty` |

Ngưỡng màu khóa ≤ 0,2%: **8/8 đạt** ở cả bốn khổ, cực đại **0,13833%**. Ngưỡng tương phản ≥ 0,25 trên ít nhất một nền: **8/8 đạt** ở cả 720p và 1080p; thấp nhất **0,38356** trên nền ngọc. Luma dùng Y′ sRGB = 0,2126R + 0,7152G + 0,0722B, chia 255; trung bình vật cân theo alpha. Số cho cả hai nền và hai màu tạm có trong [checks-delivered/metrics.json](../../games/typing-defense/art-src/_review/172/checks-delivered/metrics.json).

**Bảy bản thu ban đầu trong `ui/badges/` chưa thay:**

| File | Pixel phải sửa | Alpha |
| --- | ---: | --- |
| `badge-flash.256.png` | 2 | 1 → 0 |
| `badge-flash.128.png` | 2 | 1 → 0 |
| `badge-calling.256.png` | 1 | 254 → 255 |
| `badge-review.128.png` | 2 | 254 → 255 |
| `badge-review.64.png` | 1 | 1 → 0 |
| `badge-chain.256.png` | 2 | 254 → 255 |
| `badge-chain.128.png` | 2 | 254 → 255 |

Giữ [audit-all-sizes/audit.json](../../games/typing-defense/art-src/_review/172/audit-all-sizes/audit.json) ghi lỗi ban đầu; không xóa hay đổi kết quả trượt thành đạt. Bản sửa ở `delivery-final/` qua **32/32**, `partial_outside_sum = 0`, `all_pass = true`, theo [audit-final-bundle/audit.json](../../games/typing-defense/art-src/_review/172/audit-final-bundle/audit.json). Danh sách từng tọa độ và RGB được giữ ở `final-bundle-edge-corrections.json`. Khảo sát biên alpha > 16 có lưu riêng ở `edge-boundary-16-audit.json`; không dùng phép khảo sát đó để thay tiêu chí giữa chừng.

## 5. Dáng riêng và đọc được ở cỡ thật

Mặt nạ thu trực tiếp từ 1024 bằng Lanczos; IoU chính dùng alpha ≥ 128. Kiểm bổ sung alpha > 16 cũng ghi để tránh chỉ chọn ngưỡng có lợi.

- Ba cặp `pip-empty/full/gold`: **IoU 1,0000** ở 32 và 16 px; với ngưỡng alpha > 16, nhỏ nhất **0,99764** ở 32 px, vẫn ≥ 0,95.
- Giữa hai vật không cùng nhóm trạng thái: IoU 32 px cao nhất **0,67526**; kiểm alpha > 16 cao nhất **0,77358**. Cả hai đều ≤ 0,80.
- Riêng năm huy hiệu ở đúng **16 px**, cả 10 cặp đều ≤ 0,80:

| Huy hiệu | IoU lớn nhất ở 16 px | So với |
| --- | ---: | --- |
| `badge-ok` | 0.3671 | `badge-chain` |
| `badge-flash` | 0.3529 | `badge-chain` |
| `badge-calling` | 0.4884 | `badge-chain` |
| `badge-review` | 0.5114 | `badge-chain` |
| `badge-chain` | 0.5114 | `badge-review` |

Ở 8 px trên giấy thẻ và cỏ thật: rỗng có tâm ngọc sẫm, đầy có tâm mint sáng, hoàn hảo có tâm vàng; nhận ra cả ba trạng thái. Hoa văn trên môi đá chỉ còn thành vành sáng, không kỳ vọng đọc nét khắc ở cỡ này. Ở 16 px nhận ra dấu kiểm, tia chớp, sóng, vòng mũi tên/lá và hai mắt xích. Lá trong `badge-review` và điểm lồng của `badge-chain` nhỏ nhất, được trừ điểm đọc ở mục 6.

Đã ghép **cả tám trạng thái vào phần giấy trống của một thẻ gõ thật**, không che từ hay nhãn Chain, đúng 8/16 px ở 720p và 12/22 px ở 1080p. Nguồn là `td-1c-words-key-light-1280x720.jpg` và bản 1920x1080 trong thư mục `sheets3/` được phiếu chỉ định. Ảnh nguồn vốn là contact sheet: lấy ô viewport 480×270 đầu tiên và dựng lại kích thước viewport được ghi trên tờ trước khi cắt. Vì vậy chữ nền đã mờ từ nguồn; các huy hiệu ghép mới vẫn được thu trực tiếp về cỡ thật. Đây là **mock vị trí từ ảnh thật**, không phải kiểm runtime hoặc playtest mới.

Các tờ duyệt:

- [172-sheet.jpg](../../games/typing-defense/art-src/_review/172-sheet.jpg): đúng bốn hàng — 256 px; 1080p hai nền; 720p hai nền; bốn icon có sẵn (`call-harvest`, `call-power`, `call-shield-break`, `call-quiz`) và mảnh HUD thương mại cùng cao 256 px. Tên nằm dưới từng ảnh.
- [172-small.jpg](../../games/typing-defense/art-src/_review/172-small.jpg): cỡ thật và phóng nearest ×4 để soi pixel, không làm nét.
- [172-card.jpg](../../games/typing-defense/art-src/_review/172-card.jpg): thẻ thật trước/sau ghép, cỡ thật và phóng ×2.
- [172-pips.jpg](../../games/typing-defense/art-src/_review/172-pips.jpg): ba trạng thái trên giấy và cỏ thật, cỡ 8/12 px và phóng ×4.
- [Tám tờ bản sinh/bản hậu kỳ](../../games/typing-defense/art-src/_review/172/visual-delivered/): toàn canvas, cùng cỡ, giữ đầy đủ phần vẽ.

## 6. KA5 · Tự chấm trên bản hậu kỳ

So với HUD thương mại và bộ 115 đã nhận: độ hoàn thiện chất liệu **8,5/10** ở cỡ lớn. Ở 720p, `badge-review` và `badge-chain` ở mức **8/10**, các ảnh còn lại **8,5/10**. Ánh vàng và hoa văn hơi dày so với dấu hiệu trạng thái rất nhỏ; không coi việc qua số đo là điểm mỹ thuật 10.

Thứ tự năm tiêu chí: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi mục 0–2. Cột Dùng tiếp = 2 **chỉ áp dụng bộ chọn cuối đã qua 32/32**, không áp dụng bảy bản thu cũ còn giữ trong `ui/badges/`.

| Ảnh | 1024² · 5 tiêu chí | Tổng | 720p · 5 tiêu chí | Tổng | Điểm còn thiếu |
| --- | --- | ---: | --- | ---: | --- |
| `pip-empty` | 2/2/1/2/2 | 9 | 2/2/1/2/2 | 9 | Môi đá trang trí dày; ở 8 px chỉ còn vành/tâm tối. |
| `pip-full` | 2/2/1/2/2 | 9 | 2/2/1/2/2 | 9 | Như ổ rỗng; màu tâm sáng vẫn tách rõ. |
| `pip-gold` | 2/2/1/2/2 | 9 | 2/2/1/2/2 | 9 | Vàng sáng chiếm ưu thế; còn phân biệt được với ngọc. |
| `badge-ok` | 2/2/1/2/2 | 9 | 2/2/1/2/2 | 9 | Hoa văn phong phú hơn một nét ấn tối giản; dáng kiểm rõ. |
| `badge-flash` | 2/2/1/2/2 | 9 | 2/2/1/2/2 | 9 | Viền vàng hơi mạnh; tia chớp hẹp nhưng nhận được. |
| `badge-calling` | 2/2/1/2/2 | 9 | 2/2/1/2/2 | 9 | Chi tiết cuộn mây nhiều; ba cung sóng vẫn tách nhau. |
| `badge-review` | 2/2/1/2/2 | 9 | 2/1/1/2/2 | 8 | Ở 16 px nhận vòng quay và lá sáng; không rõ từng gân lá. |
| `badge-chain` | 2/2/1/2/2 | 9 | 2/1/1/2/2 | 8 | Hai lỗ vòng còn rõ; độ sâu điểm lồng giảm ở 16 px. |

**8/8 ảnh tự chấm ≥ 8** ở cả hai cỡ. Chưa có điểm Claude; chưa tuyên bố “Nhận”, chưa chép vào `public/`.

## 7. KA1 · MD5 và không ghi đè

Trước lúc ghi, `ui/badges/`, `_review/172/`, các tờ `_review/172-*.jpg` và báo cáo đều chưa có file. `md5-before.txt` rỗng đúng **0 file có trước trong các đích mới**. Sau giao, script chạy macOS **`md5 -r` trên mọi file trong các đích này**, gồm báo cáo, rồi `diff`; ba sản phẩm audit tự tham chiếu (`md5-after.txt`, diff, summary) được loại khỏi chính snapshot của chúng.

| Hạng mục | Số file |
| --- | ---: |
| Có trước trong phạm vi mới | 0 |
| `ui/badges/` | 80 = 40 PNG và 40 prompt |
| Bộ chọn cuối `delivery-final/` | 64 = 32 PNG và 32 prompt |
| File có trước bị sửa / xóa | 0 / 0 |

Hồ sơ: [md5-before.txt](../../games/typing-defense/art-src/_review/172/md5-before.txt), [md5-after.txt](../../games/typing-defense/art-src/_review/172/md5-after.txt), [diff](../../games/typing-defense/art-src/_review/172/md5-after.diff.txt), [md5-summary.json](../../games/typing-defense/art-src/_review/172/md5-summary.json). Diff chỉ có dòng thêm; summary ghi tổng file toàn phạm vi. Đây là audit của các đích phiếu 172, không phải lời khẳng định đã băm toàn kho ảnh của game.

## 8. Script chạy lại và việc Claude cần xem

Các script nằm trọn trong [_review/172/](../../games/typing-defense/art-src/_review/172/), chỉ cần Python 3 chuẩn và ImageMagick 7:

- `prepare-prompts.py`: ghép đúng STYLE-UI, ICON và phần riêng.
- `finish-one.py`: key, trim, căn 717 px và tạo ba cỡ Lanczos.
- `finish-edges.py`: sửa alpha gần nhị phân của bản gốc; không đổi RGB.
- `measure-set.py`, `measure-set-v2.py`: đo hộp bao, alpha, tương phản, IoU; v2 đọc đường dẫn bản chọn đã sửa mép.
- `deliver.py`: chép sang tên mới, chặn thay file khác byte.
- `audit-delivered.py`: giữ kết quả kiểm 32 bản thu ban đầu, có bảy file trượt.
- `prepare-final-bundle.py`: dựng bộ chọn cuối riêng, ghi đúng 12 pixel alpha sửa ở bản thu.
- `audit-final-bundle.py`: kiểm cả 32 file, nguồn sinh, bản sao công cụ và phép Lanczos kèm sửa mép được ghi rõ.
- `render-set-v2.py`: dựng tờ duyệt cuối; v1 giữ làm lịch sử vì lấy mảnh cỏ vướng mép HUD và ghi nhãn phóng ×8 chưa đúng. V2 dùng cỏ sạch và nearest ×4. Không thay ảnh game vì sửa tờ xem.
- `md5-audit.py`: băm mọi đích và lưu diff; `write-report.py`: ghi báo cáo này một lần.

Script tạo ảnh trung gian không ghi đè đầu ra; khi chạy lại phần kiểm, chọn tên thư mục mới:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
PYTHONDONTWRITEBYTECODE=1 python3 \
  games/typing-defense/art-src/_review/172/audit-final-bundle.py recheck-owner-01
PYTHONDONTWRITEBYTECODE=1 python3 \
  games/typing-defense/art-src/_review/172/measure-set-v2.py recheck-measure-owner-01 delivered
```

Lệnh đo thứ hai dùng tám bản 1024 trong `ui/badges/`, nguyên byte giống bộ chọn cuối; số IoU, tương phản và hộp bao vì vậy là số của đúng tranh chọn. Audit đầu tiên kiểm các bản thu của `delivery-final/`.

**Khác phiếu:** dùng `frames-epic/` vì là nơi thật của bộ 115 đã nhận; nguồn công cụ là 1254², bản giao đúng 1024²; có sửa alpha mép sau Lanczos; bộ chọn cuối ở review để không ghi đè bảy bản thu đã lỡ xuất. Không có ngưỡng nào buộc xóa hoặc phủ phần tranh. Không bỏ ảnh nào, không sinh quá một lượt mỗi ảnh. Bỏ qua tích hợp runtime, chép `public/`, âm thanh và nghiệm thu Claude vì ngoài phần việc được giao.

**Claude cần xem:** dùng `delivery-final/`, mở bản 1024 và tờ cỡ thật, chú ý lá review và điểm lồng chain ở 16 px; chấm lại ≥ 8 rồi mới chép vào `public/`. Bảy bản thu cũ không phải bản chọn cuối. Việc thay chúng trong `ui/badges/` chưa làm vì phiếu cấm ghi đè file có sẵn.
