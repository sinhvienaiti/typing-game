# Phiếu 121 · Last Line · Bảy bản chọn, chờ xử lý các mục chưa đạt

Ngày 29/10/2026, Codex. Đã tạo **7 bản chọn bằng `image_gen` tích hợp, 16 lượt sinh**, giữ đủ mọi `.tryN.png` và prompt nguyên văn cạnh ảnh. Không ảnh nào quá ba lượt. **Chưa đủ điều kiện “xong khi” của phiếu:** vùng bảng của kho súng và màn thắng còn vượt ngưỡng độ lệch chuẩn; hue trung vị cả bộ chưa đạt; hai tên alpha đầu của logo chưa sạch, ứng viên đã sửa được giữ riêng trong review theo luật không ghi đè.

Điều kiện chọn hướng đã đủ: [phiếu 156](156-ts-lightbearer-tripo.md) ghi rõ chủ dự án chọn **B · Lightbearer sáng 29/10/2026**; các phiếu 151–152 cũng ghi quyết định này. Không tự chọn B từ điểm tự chấm ở báo cáo 112.

## 1. Ảnh và hồ sơ giao

Gốc media: `games/typing-survival/art-src/`. Bảy bản chọn dưới đây có prompt cùng tên `.prompt.txt`, giống nguyên văn prompt của lượt đã chọn.

| Ảnh | Lượt chọn / số lượt | Bản chọn | Tờ bản sinh và bản hậu kỳ |
| --- | --- | --- | --- |
| Màn chính | 2 / 2 | [menu-bg.png](../../games/typing-survival/art-src/ui/screens-epic/menu-bg.png) | [Đối chiếu](../../games/typing-survival/art-src/_review/121/menu-bg-before-after.jpg) |
| Thẻ ải | 3 / 3 | [briefing-bg.png](../../games/typing-survival/art-src/ui/screens-epic/briefing-bg.png) | [Đối chiếu](../../games/typing-survival/art-src/_review/121/briefing-bg-before-after.jpg) |
| Nạp súng | 3 / 3 | [loadout-bg.png](../../games/typing-survival/art-src/ui/screens-epic/loadout-bg.png) | [Đối chiếu](../../games/typing-survival/art-src/_review/121/loadout-bg-before-after.jpg) |
| Hành trình | 2 / 2 | [journey-bg.png](../../games/typing-survival/art-src/ui/screens-epic/journey-bg.png) | [Đối chiếu](../../games/typing-survival/art-src/_review/121/journey-bg-before-after.jpg) |
| Thắng | 3 / 3 | [results-win-bg.png](../../games/typing-survival/art-src/ui/screens-epic/results-win-bg.png) | [Đối chiếu](../../games/typing-survival/art-src/_review/121/results-win-bg-before-after.jpg) |
| Thua | 2 / 2 | [results-lose-bg.png](../../games/typing-survival/art-src/ui/screens-epic/results-lose-bg.png) | [Đối chiếu](../../games/typing-survival/art-src/_review/121/results-lose-bg-before-after.jpg) |
| Logo | 1 / 1 | [logo.png](../../games/typing-survival/art-src/ui/screens-epic/logo.png), nguồn magenta | [Nguồn và ứng viên alpha sạch](../../games/typing-survival/art-src/_review/121/logo-before-after.jpg) |

**Logo để Claude xem và dùng khi duyệt:** [bản alpha sạch 2172 px](../../games/typing-survival/art-src/_review/121/logo-clean.alpha.png), [bản sạch 512 px](../../games/typing-survival/art-src/_review/121/logo-clean-final.512.png). Hai file `ui/screens-epic/logo.alpha.png` và `logo.512.png` là lần tách đầu **không đạt**; giữ nguyên, không dùng để tích hợp. Việc ứng viên sạch chưa nằm ở hai tên đích chính là một sai khác giao nhận còn phải xử lý, không coi là đã đạt mục 5 tại đường dẫn yêu cầu.

- [Mock sáu màn](../../games/typing-survival/art-src/_review/121-mock.jpg), mỗi nền cắt giữa 16:9, kính tối 60%, chỉ chữ thử tiếng Anh; logo sạch trên màn chính.
- [Tờ so tham chiếu](../../games/typing-survival/art-src/_review/121-vs-ref.jpg): hàng trên ba ảnh mới và ảnh chủ dự án, từng ảnh cao 640 px; hàng dưới là màn chính hôm nay cắt từ sheet có sẵn.
- [Tờ 384 px](../../games/typing-survival/art-src/_review/121/thumbnails.jpg); ảnh nhỏ riêng cùng tên trong `_review/121/`.
- [Số đo bản chọn](../../games/typing-survival/art-src/_review/121/measurements-selected.json), [độ đồng bộ](../../games/typing-survival/art-src/_review/121/set-consistency.json), [kiểm bản sinh và prompt](../../games/typing-survival/art-src/_review/121/artifact-check.json).

Đã xem ảnh chuẩn của chủ dự án, cả hai concept B và sheet màn hôm nay trước khi sinh. Mọi nền đính kèm `b-lightbearer-keyart.png` để giữ nhân vật, vật liệu và màu; logo sinh riêng. Không dùng ảnh chuẩn để chép nội dung.

## 2. Các lượt sinh và sửa prompt

Khối STYLE, phần cảnh và câu REF bắt buộc giữ nguyên văn; các đoạn sửa được thêm sau đó để làm rõ bố cục và sửa lỗi thực tế. Lượt đầu thêm khổ ngang 1536 × 1024, vùng cắt giữa và yêu cầu vùng tối phải là phần tranh tự nhiên. Logo dùng STYLE-UI, thay đúng câu cấm chữ cuối bằng khối LOGO, thêm khổ rộng 3:1 và lề.

| Ảnh | Lượt | Quan sát và sửa |
| --- | --- | --- |
| menu-bg | 1 | Bám cảnh chiến đấu của tham chiếu, còn bầy quái và súng bắn; loại cho màn chính. |
| menu-bg | 2 | Chỉ rõ cảnh nghỉ một mình, nhân vật nhỏ phía phải, hai súng canh ở vai, không giao chiến. Chọn; giữ được quy mô hố đen và khoảng tối bên trái. |
| briefing-bg | 1 | Có cột cổng nhưng vẫn là cảnh nhân vật bắn bầy; vùng giữa sáng và rối. |
| briefing-bg | 2 | Đổi thành cảnh kiến trúc trống nhìn từ trong cổng, bỏ nhân vật và bầy; đĩa sáng vẫn lọt vào vùng giữa. σ vùng bảng 0,190521, chưa đạt. |
| briefing-bg | 3 | Thêm xà cổng lớn, nhìn sâu hơn từ trong đường hầm; giới hạn đĩa sáng ở góc trên phải, vùng giữa là đường đắp và kiến trúc xa. Chọn; σ 0,119812. Cánh cửa mở chưa tách hình rõ bằng cột và xà cổng. |
| loadout-bg | 1 | Có năm bệ nhưng nhân vật và leviathan còn chiếm cảnh, cột sáng quá mạnh. |
| loadout-bg | 2 | Kho súng trống, cửa sổ cao, năm bệ thấp và tia sáng mảnh. Không còn nhân vật; σ dải giữa 0,144387, chưa đạt. |
| loadout-bg | 3 | Hạ tương phản cả các cột ở mép trong dải thẻ; yêu cầu graphite có ánh hắt vàng dịu để gần bộ hơn. Chọn vì kiến trúc và vật liệu hoàn thiện hơn; σ 0,152238 vẫn chưa đạt. Không giảm sáng quá giới hạn hoặc phủ hộp tối vào tranh. |
| journey-bg | 1 | Còn nhân vật, giao chiến và năm đèn mốc; loại. |
| journey-bg | 2 | Góc nhìn xa từ trên cao, đường đắp trống cong trong khoảng không, đúng bốn đèn tròn. Chọn; không sinh thêm chỉ để đổi màu khoảng không cho hợp một thống kê hue. |
| results-win-bg | 1 | Có xác kính nhưng hai súng vẫn bắn, trung tâm quá sáng. |
| results-win-bg | 2 | Nhân vật sang phải, súng nghỉ, trung tâm là sàn; trời sáng còn nằm trong vùng bảng, σ 0,217057. |
| results-win-bg | 3 | Nhìn xuống sàn nhiều hơn, đẩy chân trời lên cao; nhân vật và tia tan rã nằm ở mép phải. Chọn; súng hạ rõ, cảnh thắng đọc được. σ 0,139931 vẫn chưa đạt. |
| results-lose-bg | 1 | Đã quỳ nhưng súng rơi vẫn sáng, sàn và đĩa làm vùng giữa quá sáng. |
| results-lose-bg | 2 | Đẩy nhân vật quỳ sang phải; súng rơi tối, súng còn lại mờ; bầy ở xa, trung tâm là sàn nứt và khói. Chọn; giảm sáng toàn ảnh nhẹ để qua ngưỡng. |
| logo | 1 | Đúng hai từ “Last Line”, đủ tám chữ, hai chữ L hoa. Không cần sinh lại; lỗi tách nền xử lý bằng công cụ. |

[Chỉ mục 16 lượt](../../games/typing-survival/art-src/_review/121/generation-index.json) ghi đường dẫn công cụ trả, prompt nguyên văn và tham chiếu của từng lượt. Đã đối chiếu: mọi bản try chép nguyên byte từ ảnh công cụ trả; mọi prompt bản chọn khớp lượt chọn.

## 3. Hậu kỳ, khổ và vùng bảng

Sáu nền đều **1536 × 1024 ngay từ bản sinh**, không phóng, không cắt ảnh giao. Logo nguồn **2172 × 724**, đúng tỷ lệ 3:1 và cạnh dài ≥1536. Các tờ kiểm dùng Lanczos để thu; mock cắt giữa bằng `-gravity center -crop 1536x864+0+0 +repage`, tương ứng bỏ 80 px trên và dưới.

Chỉ `menu-bg` và `results-lose-bg` giảm RGB **toàn ảnh 6%** bằng `-channel RGB -evaluate multiply 0.94 +channel`; không có mask cục bộ. Bốn nền còn lại chép nguyên byte từ bản try đã chọn. Không xóa, san phẳng, phủ màu hoặc thay phần vẽ. Các khối kính tối chỉ tồn tại ở ảnh mock riêng.

Luma tính trên RGB sRGB 0–1: `Y = 0,2126R + 0,7152G + 0,0722B`, không chuyển sang ánh sáng tuyến tính. Tọa độ dưới đây thuộc bản cắt 1536 × 864; hộp phần trăm làm tròn ra ngoài.

| Nền | Hộp x, y, rộng, cao | Luma vùng TB | σ vùng | TB ≤0,40; σ ≤0,12 | Luma toàn ảnh | Hue trung vị |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| menu-bg | 0, 0, 614, 864 | 0,104056 | 0,119569 | Đạt | 0,243315 | 41° |
| briefing-bg | 307, 129, 922, 606 | 0,161957 | 0,119812 | Đạt | 0,167624 | 25° |
| loadout-bg | 0, 259, 1536, 433 | 0,172429 | **0,152238** | **Chưa đạt** | 0,208142 | 26° |
| journey-bg | Không có vùng bảng quy định trong phiếu | — | — | Không áp dụng | 0,234542 | 230° |
| results-win-bg | 384, 129, 768, 606 | 0,166860 | **0,139931** | **Chưa đạt** | 0,236358 | 38° |
| results-lose-bg | 384, 129, 768, 606 | 0,186203 | 0,119363 | Đạt | 0,213849 | 232° |

Menu: σ trước → sau **0,127218 → 0,119569**. Màn thua: **0,126994 → 0,119363**. Ở kho súng, chỉ nhân sáng đồng đều để đạt σ sẽ cần giảm khoảng **21,2%**; màn thắng cần khoảng **14,2%**, đều vượt giới hạn ±10%. Giữ nguyên tranh và ghi mâu thuẫn theo [ART_ACCEPTANCE §5](../games/ART_ACCEPTANCE.md), không ghi hai ảnh này đạt mục 6.

Đã xem đủ sáu bản giao ở khổ nguồn và từng bản 384 px: không thấy chữ, số, chữ ký, HUD, khung hay viền. Các dấu trên vật liệu là hoa văn hình học, không thành từ. Journey có đúng bốn đèn xanh tròn. Loadout có đúng năm bệ trống.

## 4. Logo: chữ và alpha

Duyệt chữ bằng [tờ từng chữ phóng đúng 4×](../../games/typing-survival/art-src/_review/121/logo-spelling-corrected-4x.jpg), cạnh mẫu **Last Line** bằng **Arial**, font `/System/Library/Fonts/Supplemental/Arial.ttf`. Thấy đúng **L-a-s-t / L-i-n-e**, một khoảng cách giữa hai từ; không dùng font dựng lại logo.

Tờ `logo-spelling-4x.jpg` đầu dùng tọa độ theo preview 2048 px, trong khi nguồn thật rộng 2172 px, nên ô chữ i bị lệch. Giữ tờ đầu, không dùng để duyệt; tờ có chữ `corrected` đã đổi tọa độ theo nguồn thật. Không sửa ảnh logo để sửa lỗi tờ kiểm.

Tách nền bằng bản sao **nguyên byte** của `tools/art-normalize/key-alpha.sh` và các phụ thuộc ở `_review/121/key-alpha-tool/`, với `ART_MAGICK=/opt/homebrew/bin/magick`, `--bg '#FF00FF' --mode global --despill protect-interior --no-key-hue`. Bản sao giữ thư mục `.tmp` của công cụ trong vùng được phép ghi. Nền nguồn có nhiễu màu nhẹ quanh magenta, không hoàn toàn đồng nhất #FF00FF; tách được bằng khóa màu.

| File | Khổ | Alpha min / max | Pixel magenta còn alpha >0 | % toàn ảnh | Lề trái / trên / phải / dưới | Kết quả |
| --- | --- | --- | ---: | ---: | --- | --- |
| ui/screens-epic/logo.alpha.png | 2172 × 724 | 0 / 255 | 849 | 0,053989% | 180 / 185 / 127 / 234 | **Không đạt** |
| ui/screens-epic/logo.512.png | 512 × 171 | 0 / 255 | 74 | 0,084521% | 40 / 41 / 30 / 53 | **Không đạt** |
| _review/121/logo-clean.alpha.png | 2172 × 724 | 0 / 255 | **0** | **0%** | 180 / 185 / 127 / 234 | Ứng viên đạt số đo |
| _review/121/logo-clean-final.512.png | 512 × 171 | 0 / 255 | **0** | **0%** | 40 / 41 / 30 / 53 | Ứng viên đạt số đo |

Phép đếm dùng đúng HSV hue 285–330°, S >0,5 và alpha >0. Ứng viên chỉ khử dư sắc khóa ở **849 pixel RGB**, giữ nguyên toàn bộ alpha: `R=min(R,G)`, giữ G/B, trên đúng tập pixel chưa đạt. Sau thu Lanczos sang 512 px, ringing tạo 54 pixel thuộc tập này; khử lại cùng công thức, không co mép hay bỏ phần chữ. File trung gian `logo-clean.512.png` còn 54 pixel nên không dùng.

Đã xem [mép phóng 4×](../../games/typing-survival/art-src/_review/121/logo-clean-edge-4x.jpg) và ứng viên đầy đủ: không thấy viền hồng; lề nhỏ nhất 127 px ở nguồn, 30 px ở bản nhỏ. Đây là xử lý dư khóa màu, không thay nét vẽ, không đổi alpha. [Số đo nguồn](../../games/typing-survival/art-src/_review/121/logo-candidate-measurements.json), [bản 512 cuối](../../games/typing-survival/art-src/_review/121/logo-final512-measurements.json).

## 5. Mock, cùng bộ và đứng cạnh tham chiếu

Tờ mock dùng kính tối 60% đúng hộp bảng; dải kho súng có năm thẻ riêng. Chữ kem đọc rõ ở cả sáu màn; hố đen, cổng, mái vòm và đường cong vẫn tạo quy mô lớn. Nhân vật thắng/thua ở ngoài vùng bảng, không bị bảng che phần chính. Mock là kiểm thị giác của Codex, không thay số đo trên nền trần và không phải bằng chứng tích hợp trong game.

Độ lệch luma trung bình của năm nền, bỏ màn thua: **0,075691 ≤0,10, đạt**. Hue lấy trung vị HSV toàn ảnh, không lọc pixel tối hay ít bão hòa; ghi theo bin 1°. Các trung vị từ **25° đến 232°**; chênh lớn nhất giữa cặp theo khoảng cách vòng tròn là **171° >20°, chưa đạt mục 8**. Phần trời navy chiếm nhiều diện tích ở hành trình và màn thua; graphite hắt vàng chiếm nhiều hơn ở các cảnh khác. Không nhuộm trời hay phủ vàng để ép trung vị, vì sẽ phá kịch bản màu đã yêu cầu; giữ tranh để Claude quyết theo §5.

Trên tờ so, với ảnh chuẩn chủ dự án làm mốc M=9:

- **menu-bg: đứng cạnh được** — nhân vật nhỏ, hố đen và vòng trạm tạo quy mô, ánh sáng có hướng, nhiều lớp xa. Kém ảnh chuẩn ở bề mặt phản sáng hơi dày và ít khoảng thở hơn.
- **loadout-bg: đứng cạnh được về mức tranh** — mái vòm cao, vật liệu và viền sáng hoàn thiện, đủ năm bệ. Chưa đạt số đo dải thẻ; ánh phản ở cột ngoài còn mạnh.
- **journey-bg: đứng cạnh được** — đường cong và các đèn mốc dẫn mắt qua khoảng không, vòng vỡ và trụ xa tạo chiều sâu; chi tiết vụn trong trời còn dày hơn ảnh chuẩn.

## 6. KA5 · Tự chấm trên bản hậu kỳ

Đã xem bản giao đầy đủ và từng ảnh nhỏ riêng có cạnh dài 384 px. M theo mức chợ, không theo bộ cũ. Q theo năm tiêu chí Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp, mỗi mục tối đa 2; bảng tiêu chí ở §1, ngưỡng 2D ở §2.2 của ART_ACCEPTANCE. Điểm tự chấm **không thay kết quả chưa đạt các ngưỡng số**.

| Ảnh | M đầy đủ / 384 | Q đầy đủ: năm tiêu chí | Tổng Q | Q 384: năm tiêu chí | Tổng Q 384 | Điểm còn thiếu |
| --- | --- | --- | ---: | --- | ---: | --- |
| menu-bg | 8,5 / 8,2 | 2 / 2 / 2 / 2 / 1,5 | 9,5 | 2 / 1,5 / 2 / 2 / 1,5 | 9,0 | Nhân vật khá nhỏ; sàn nhiều ánh phản. |
| briefing-bg | 8,2 / 8,0 | 1,5 / 2 / 2 / 2 / 1,5 | 9,0 | 1,5 / 1,5 / 2 / 2 / 1,5 | 8,5 | Cánh cửa nửa mở chưa rõ bằng xà và cột cổng. |
| loadout-bg | 8,3 / 8,1 | 2 / 1,5 / 2 / 2 / 1 | 8,5 | 2 / 1,5 / 2 / 2 / 1 | 8,5 | Hai mép dải thẻ còn tương phản mạnh; bệ nhỏ ở 384 px. |
| journey-bg | 8,6 / 8,3 | 2 / 2 / 2 / 2 / 1,5 | 9,5 | 2 / 1,5 / 2 / 2 / 1,5 | 9,0 | Trời nhiều vụn, thống kê hue lệch bộ. |
| results-win-bg | 8,2 / 8,0 | 2 / 1,5 / 2 / 2 / 1 | 8,5 | 2 / 1,5 / 2 / 2 / 1 | 8,5 | Nhiều sàn để dành bảng, chân trời còn sáng trong hộp đo. |
| results-lose-bg | 8,4 / 8,1 | 2 / 2 / 2 / 2 / 1,5 | 9,5 | 2 / 1,5 / 2 / 2 / 1,5 | 9,0 | Bầy ở xa nhỏ, sắc trời làm hue trung vị nghiêng xanh. |
| logo, ứng viên sạch | 8,5 / 8,2 | 2 / 2 / 2 / 2 / 1,5 | 9,5 | 2 / 1,5 / 2 / 2 / 1,5 | 9,0 | Nét kim loại khá cầu kỳ; chưa đặt ứng viên sạch vào hai tên đích đầu. |

Logo chấm trên ứng viên hậu kỳ sạch ở review, không lấy điểm này để nhận hai file alpha đầu chưa đạt. Màn chính, cổng, kho và hành trình đều có mốc lớn, lớp gần–giữa–xa và trời; logo chấm theo chất liệu chữ, độ sắc và đọc được, không áp tiêu chí ba lớp cảnh cho chữ logo.

## 7. KA1, tái lập và phạm vi

Baseline `md5 -r` lấy trước khi tạo file của phiếu: **997 file** trong toàn cây `games/typing-survival/art-src/`. Sau giao: **cả 997 file giữ nguyên; 0 sửa, 0 xóa**. Manifest sau thấy 1484 file, tăng 487 file trên toàn cây có các làn đồng thời; không quy toàn bộ phần tăng này cho phiếu 121. Diff chỉ thêm dòng. Các file manifest cuối không tự băm đệ quy.

[MD5 trước](../../games/typing-survival/art-src/_review/121/md5-before.txt), [sau](../../games/typing-survival/art-src/_review/121/md5-after.txt), [diff](../../games/typing-survival/art-src/_review/121/md5-diff.txt), [kết quả](../../games/typing-survival/art-src/_review/121/md5-summary.json).

Script, công thức và hướng dẫn nằm trong [_review/121/README.md](../../games/typing-survival/art-src/_review/121/README.md). Đã chạy `reproduce.py .../replay-check logo`: nguồn, alpha sạch và bản sạch 512 đều **giống pixel** bản đã giao, hai bước khử dư màu lần lượt 849 và 54 pixel. Script từ chối ghi đè; tái lập vào thư mục review mới. Không có runner API/mạng thay cho công cụ tích hợp.

Không chạy Git, build/test game, dev server hoặc trình duyệt. Không sửa mã, tài liệu khác, âm thanh, runtime hay asset đang dùng; không đọc/ghi các thư mục game và thiết kế Tu Tiên. Không có browser capture hoặc frame thô cần prune; mọi try là bản sinh phải giữ theo phiếu.

## 8. Claude và chủ dự án cần xem

1. Chấm lại M/Q trên bảy bản hậu kỳ ở khổ đầy đủ và cỡ nhỏ, xem các tờ bản sinh–hậu kỳ; điểm hiện tại chỉ là Codex tự chấm.
2. Quyết phần vùng bảng **loadout σ=0,152238** và **thắng σ=0,139931**, sau đủ ba lượt; không ép số bằng sửa phá tranh hoặc giảm sáng quá ±10%.
3. Quyết mâu thuẫn **hue trung vị lệch 171° theo vòng tròn** với kịch bản navy/cam của các cảnh có diện tích trời khác nhau.
4. Xem hai ứng viên logo sạch ở review; hai tên alpha đầu vẫn chưa đạt và được giữ nguyên. Cần thống nhất cách đưa ứng viên vào tên giao cuối mà không vi phạm luật không ghi đè của phiếu.

**Trạng thái: đã có đủ bảy bản chọn và hồ sơ kiểm; chưa nghiệm thu, chưa đủ điều kiện đóng phiếu 121.**
