# Phiếu 135 · Wordwoven · Tem hạng và sao

Ngày làm: 29/10/2026, Mac mini M4, macOS; repo cha.

**Đã giao đủ tám ảnh và 24 bản thu. Tự chấm M ≥ 8, Q ≥ 8 trên bản hậu kỳ. Chưa nhận: chờ Claude chấm lại và quyết mâu thuẫn IoU chung/riêng của phiếu.** Không tự coi kiểm IoU chung ≤ 0,80 là đạt: sáu tem cùng khung tròn làm kiểm này trượt theo đúng yêu cầu riêng ≥ 0,90.

## 1. Nơi giao

- Ảnh và prompt: [ui/grades/](../../games/typing-defense/art-src/ui/grades/).
- **Tờ xem bản giao:** [135-sheet-final.jpg](../../games/typing-defense/art-src/_review/135-sheet-final.jpg), đủ bốn hàng theo phiếu.
- [Hồ sơ, script và số đo](../../games/typing-defense/art-src/_review/135/); [số đo trực tiếp trên ảnh đã giao](../../games/typing-defense/art-src/_review/135/delivery-check/metrics.json); [identify đủ 32 PNG](../../games/typing-defense/art-src/_review/135/identify.txt).
- [Dải cỡ thật và phóng nearest-neighbour](../../games/typing-defense/art-src/_review/135/sheets-selected/), có 16, 20, 28, 34, 36, 44 px.
- Mỗi ảnh có `<tên>.compare-audit.jpg`: **bản sinh | bản hậu kỳ**, cùng tỉ lệ vật, lấy crop từ key nhưng RGB bên trái từ nguồn sinh. [Thông số từng tờ](../../games/typing-defense/art-src/_review/135/compare-audit.json). Các `<tên>.full-selected.jpg` cho xem bản giao 1024² trên ngọc.

Không chạy bất cứ lệnh Git, build, test suite, dev server, trình duyệt hay mạng ngoài `image_gen`. Không ghi public, mã game, game khác hoặc Tu Tiên; không đụng `.wt-*`. Không tạo âm thanh. Không có frame trình duyệt phải dọn.

## 2. Tham chiếu và prompt

Dùng kỹ năng `imagegen`, công cụ tích hợp `image_gen`, chín lượt tổng cộng. Đính kèm mỗi lượt: `panel-large.v2.png` của 115/160 tại `ui/frames-epic/`, `keyart.png` của 113 và ảnh thương mại chủ dự án. Tên `ui/frames/` trong phiếu đã cũ; vị trí thật được xác nhận trong báo cáo 115 và 160. Không phải chờ vì ảnh khung đã có. Các tem sau flash còn đính kèm flash; sao tắt đính kèm sao sáng. Hồ sơ `generation-references.json` ghi rõ.

Mỗi prompt giữ nguyên STYLE-UI của 115, khối ICON định dạng, phần riêng và dòng nền M. Khối bổ sung khóa hướng chính diện, vật chiếm 70%, chất liệu nổi và ánh sáng có hướng; ghi rõ thay chỉ dẫn viền mực/mảng phẳng cũ bằng hoàn thiện thương mại theo AD. Nền khóa #FF00FF không có trong vật. Không thêm chữ, số, logo hay viền bao ảnh; vành vật lý là bộ phận của con tem.

| Ảnh | Lượt chọn | Thay đổi từng lượt |
| --- | --- | --- |
| grade-flash | try1 | Tia chớp lớn màu vàng ngà, nền đồng, vành vàng; một lượt. |
| grade-perfect | try1 | Mặt trời Đông Sơn lớn, vàng lá; một lượt. Chỉ tăng fit hậu kỳ 717 → 731 px, không đổi prompt. |
| grade-good | try1 | Một hoa sen chạm ngọc, cánh celadon lớn; một lượt. |
| grade-fair | try1 | Đồng trơn, một vòng nổi rộng, không thêm hình giữa; một lượt. |
| grade-sloppy | try1 | Đất nung xỉn, mép sứt và một vệt mực bẩn lớn, không chữ; một lượt. |
| grade-redeemed | **try2** | Try1 bị mặt trời chiếm giữa, đường vá khó đọc ở 36 px. Try2 thay riêng mô tả giữa bằng ba mảng đồng trơn, đường vá vàng chữ Y rộng 12% đường kính. Tái sinh phần vẽ bằng image_gen; giữ nguyên try1, không xóa họa tiết bằng công cụ. |
| star-lit | try1 | Sao năm cánh vàng lá, sáng bên trong, khe rõ; một lượt. |
| star-unlit | try1 | Giữ sao sáng làm tham chiếu hình học; đổi sang đồng sẫm, không phát sáng; một lượt. |

Đủ chín `.tryN.png` nguyên byte nguồn công cụ, chín prompt lượt sinh. `generation-records.json` và `generation-record-try2.json` xác nhận byte/MD5; không xóa lượt nào. Prompt chọn và prompt ba bản thu trùng nguyên văn prompt được chọn. Không có lượt 3.

## 3. Hậu kỳ giữ tranh

Nguồn công cụ là 1254², giữ nguyên ở `.try*`. Sao chép nguyên trạng bốn file của `tools/art-normalize` vào `_review/135/art-normalize/`, để mọi WORK nằm trong phạm vi được phép. Chạy với `ART_MAGICK=/opt/homebrew/bin/magick`, `PYTHONDONTWRITEBYTECODE=1`:

```sh
bash games/typing-defense/art-src/_review/135/art-normalize/key-alpha.sh   IN.tryN.png OUT.key.png --bg '#FF00FF' --mode global   --despill protect-interior --no-key-hue
```

Trim toàn vật, Lanczos giữ tỉ lệ vào fit 717²; riêng perfect 731²; canh giữa trên canvas 1024², sRGB, PNG32. Không cắt bỏ phần vẽ. Sau thu, chốt alpha mềm nằm ngoài dải Disk:3 quanh alpha ≥ 128 về 0/255; chỉ 0–2 pixel mỗi ảnh, RGB bước này không đổi. Giữ toàn bộ alpha trong mép 3 px. Không phủ màu, ghép lại, san phẳng, làm nét, chỉnh sáng hay gamma. Tách nền có khử sắc khóa ở mép theo mô hình của công cụ; không có màu tím hợp lệ trong tranh. Ba bản thu được lấy **trực tiếp từ 1024**, không chuyền qua bản 256 hay 128, không làm nét bản 64.

## 4. Số đo

Khổ: **8/8 bản gốc 1024² và 24/24 bản thu đúng 256²/128²/64²; 32/32 srgba**. Alpha min/max 0/255. Tất cả tâm lệch dưới 2%; cạnh dài dưới đây nằm trong 68–72%.

Luma dùng `(0,2126R + 0,7152G + 0,0722B) / 255`, trung bình có trọng số alpha. Lấy ngọc thực tế từ giữa panel-large.v2: **#061e16**; đá vôi từ dải `400x20+400+28`: **#b9ab95**. Đây là màu ảnh 115/160 hiện có, không dùng hai màu tạm của phiếu. Hai màu được dùng nguyên trạng trong tờ xem. Hue khóa: lệch ≤ 15° so với 300°, S > 0,5; mẫu số là số pixel alpha > 0. Dải mép 3 px lấy từ mask alpha ≥ 128 bằng morphology Dilate/Erode Disk:3.

| Ảnh | Cạnh dài % | Lệch tâm lớn nhất % | Alpha mềm ngoài mép 3 px | Pixel sắc khóa / pixel hiện (%) | Δ luma ngọc gốc | Δ ngọc 720p | Δ ngọc 1080p |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| grade-flash | 70.020 | 0.049 | 0 | 175 / 369775 (0.0473%) | 0.3408 | 0.3411 | 0.3413 |
| grade-perfect | 71.387 | 0.049 | 0 | 240 / 370269 (0.0648%) | 0.3556 | 0.3558 | 0.3562 |
| grade-good | 70.020 | 0.049 | 0 | 150 / 368682 (0.0407%) | 0.3765 | 0.3765 | 0.3768 |
| grade-fair | 70.020 | 0.049 | 0 | 294 / 404794 (0.0726%) | 0.3130 | 0.3131 | 0.3130 |
| grade-sloppy | 70.020 | 0.049 | 0 | 36 / 395682 (0.0091%) | 0.3152 | 0.3154 | 0.3154 |
| grade-redeemed | 70.020 | 0.049 | 0 | 211 / 369156 (0.0572%) | 0.3573 | 0.3575 | 0.3577 |
| star-lit | 70.020 | 0.049 | 0 | 87 / 229862 (0.0378%) | 0.4197 | 0.4195 / 0.4201 | 0.4184 / 0.4203 |
| star-unlit | 70.020 | 0.049 | 0 | 205 / 230347 (0.0890%) | 0.2553 | 0.2560 / 0.2559 | 0.2551 / 0.2560 |

720p/1080p của tem: 36/44 px. Sao ghi theo thứ tự tựa/kết quả: 16/28 và 20/34. Mọi Δ ngọc ≥ 0,25; thấp nhất sao tắt 20 px ≈ 0,2551. Nền đá chỉ là đối chứng sáng, không được tính thay cho điều kiện nền tối. Số của cả hai nền có trong JSON.

**IoU ở 32 px:** mask alpha > 16, trên toàn canvas 32²; không trim riêng để làm đẹp kết quả. Bảng sau ghi cả cực đại và cực tiểu trong nhóm tem. Chênh kiểu trang trí giữa các vành được giữ nguyên; không vẽ lại mask.

| Ảnh | IoU lớn nhất toàn phiếu | Cặp lớn nhất | IoU nhỏ nhất với tem khác |
| --- | ---: | --- | ---: |
| grade-flash | 0.9975 | grade-redeemed | 0.9097 |
| grade-perfect | 0.9949 | grade-redeemed | 0.9167 |
| grade-good | 0.9924 | grade-flash | 0.9028 |
| grade-fair | 0.9653 | grade-sloppy | 0.9028 |
| grade-sloppy | 0.9653 | grade-fair | 0.9353 |
| grade-redeemed | 0.9975 | grade-flash | 0.9120 |
| star-lit | 0.9962 | star-unlit | — |
| star-unlit | 0.9962 | star-lit | — |

- **Kiểm riêng sáu tem đạt:** mọi cặp IoU ≥ **0,9028**, ngưỡng ≥ 0,90. Sau fit perfect tăng nhẹ, cặp perfect/fair từ 0,8750 lên 0,9167. Chỉ thay tỉ lệ toàn vật trong lề được phép, không đụng phần vẽ.
- **Cặp sao đạt:** IoU **0,9962** ≥ 0,95.
- Các cặp tem/sao có IoU ≤ 0,80; ma trận đầy đủ trong JSON.
- **Kiểm chung IoU ≤ 0,80 giữa mọi ảnh khác nhau không đạt cho các cặp tem**, mâu thuẫn trực tiếp yêu cầu riêng cùng khung tròn ≥ 0,90. Theo ART_ACCEPTANCE §5, dừng sửa dáng để đuổi ngưỡng này, giữ tranh; cần Claude quyết ngoại lệ. Không ghi “mọi kiểm số đạt” khi câu chung chưa được xử lý.

Đọc hình giữa ở 36 px: tia chớp; mặt trời có tia; hoa sen; vòng đồng rỗng; vệt mực chéo; ba nhánh vá vàng. Hình redeemed try2 rõ hơn try1. Sao đọc được ở 16 px bằng năm cánh và hai trạng thái sáng/tối; chi tiết hoa văn chỉ có tác dụng ở cỡ lớn. Đã xem tờ cỡ thật, bản phóng nearest-neighbour, bản đầy đủ và tờ bản sinh/hậu kỳ.

## 5. KA5 · Tự chấm trên bản giao

M chấm theo mức thương mại: vật liệu có khối, bevel và ánh sáng gọn; đứng cạnh được ở mức phát hành, chưa đạt độ tiết chế/ưu tiên tín hiệu của HUD thương mại tham chiếu. Không lấy chi tiết ảnh lớn làm thay cho độ đọc cỡ nhỏ. Q theo năm tiêu chí của ART_ACCEPTANCE. **Dùng tiếp giữ 1/2 cho mọi ảnh**, vì còn mâu thuẫn kiểm IoU cần Claude quyết; không chấm 2 khi mọi kiểm số chưa đồng thời đạt.

Trong mỗi ô Q: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp = Tổng**.

| Ảnh | M gốc / 720p | Q gốc | Q 720p | Nhược điểm giữ lại |
| --- | --- | --- | --- | --- |
| grade-flash | 8,5 / 8,5 | 2 / 2 / 2 / 2 / 1 = **9** | 2 / 2 / 2 / 2 / 1 = **9** | Vành hơi nhiều trang trí nhưng chớp vẫn rõ. |
| grade-perfect | 8,5 / 8 | 2 / 2 / 2 / 2 / 1 = **9** | 2 / 1,5 / 2 / 2 / 1 = **8,5** | Tia mặt trời bắt đầu dồn khi thu; vẫn khác sen và vòng trơn. |
| grade-good | 8,5 / 8 | 2 / 2 / 2 / 2 / 1 = **9** | 2 / 1,5 / 2 / 2 / 1 = **8,5** | Hoa sen là khối sáng rõ; độ trong ngọc chỉ đọc ở cỡ lớn. |
| grade-fair | 8 / 8 | 2 / 2 / 2 / 2 / 1 = **9** | 2 / 2 / 2 / 2 / 1 = **9** | Cố ý ít trang trí; hình tròn giữa không cầu kỳ. |
| grade-sloppy | 8 / 8 | 1,5 / 2 / 2 / 2 / 1 = **8,5** | 1,5 / 2 / 2 / 2 / 1 = **8,5** | Đất nung còn bắt sáng hơi mạnh, ít xỉn hơn ý; vệt mực và mép sứt đúng. |
| grade-redeemed | 8,5 / 8,5 | 2 / 2 / 2 / 2 / 1 = **9** | 2 / 2 / 2 / 2 / 1 = **9** | Try2 dùng đường vá ba nhánh rộng, ít giống mặt trời hơn. |
| star-lit | 8,5 / 8,5 | 2 / 2 / 2 / 2 / 1 = **9** | 2 / 2 / 2 / 2 / 1 = **9** | 16 px chỉ còn hình và ánh vàng; phù hợp vai trò. |
| star-unlit | 8,5 / 8 | 2 / 2 / 2 / 2 / 1 = **9** | 2 / 1,5 / 2 / 2 / 1 = **8,5** | 20 px sát ngưỡng tương phản; đọc được, cần Claude xem trên HUD thật khi gắn. |

Điểm này là tự chấm, không thay Claude hoặc chủ dự án. Không tự sửa ART_REPLACE_LATER vì phiếu chỉ cho phép viết báo cáo.

## 6. KA1 và khả năng chạy lại

Trước khi ghi, `ui/grades/`, `_review/135*` và báo cáo đều chưa có; tập file cần băm ban đầu rỗng. Đã lưu `md5-before.txt` trước khi tạo prompt. Lần sau dùng **`md5 -r` từng file**, gồm toàn bộ grades, review, các tờ 135-*.jpg và báo cáo; chỉ loại chính `md5-after.txt` và `md5.diff.txt` để tránh tự tham chiếu. Diff từ tập rỗng chỉ có dòng thêm, không có dòng nội dung bị xóa/thay. Xem [md5-after.txt](../../games/typing-defense/art-src/_review/135/md5-after.txt), [md5.diff.txt](../../games/typing-defense/art-src/_review/135/md5.diff.txt). Không ghi đè, đổi tên hay xóa file có sẵn; các bản kiểm trung gian cũng được giữ.

Các script dưới đây từ chối đầu ra đã có, nên chạy lại trên **một bản sao phiếu ở thư mục trống**, hoặc chỉ gọi hàm đo với tên thư mục kiểm mới. Không xóa bộ này để chạy lại:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
export PYTHONDONTWRITEBYTECODE=1
# Sau khi chép nguyên byte nguồn image_gen về .tryN.png và prompt đã lưu:
python3 games/typing-defense/art-src/_review/135/workflow.py process grade-flash 1
# Tương tự cho bảy ảnh còn lại và grade-redeemed 2.
python3 games/typing-defense/art-src/_review/135/finalize.py ready
python3 games/typing-defense/art-src/_review/135/selected.py prepare
python3 games/typing-defense/art-src/_review/135/selected.py measure
python3 games/typing-defense/art-src/_review/135/selected.py sheet
python3 games/typing-defense/art-src/_review/135/compare-audit.py
python3 games/typing-defense/art-src/_review/135/selected.py publish
python3 games/typing-defense/art-src/_review/135/finalize.py measure delivery-check
python3 games/typing-defense/art-src/_review/135/write-report.py
python3 games/typing-defense/art-src/_review/135/selected.py audit
```

`finish_clean.py` là bản cùng nội dung `finish-clean.py`, tên dùng được để import Python; cả hai được giữ. `workflow.py` kế thừa các hàm chuẩn từ hồ sơ 133; **không chạy `workflow.py sheets`** vì đó là bố cục phiếu 133. `selected.py`/`finalize.py` cung cấp bố cục và cỡ đúng cho 135. Không chạy test suite của game.

## 7. Khác phiếu và phần chờ nhận

1. Khung tham chiếu ở `frames-epic/`, không phải `frames/`; đã đọc bằng đường dẫn thực, không sửa nơi lưu.
2. Ngưỡng IoU chung và riêng trái nhau: giao theo yêu cầu riêng, ghi đúng cả phần trượt; chờ Claude quyết.
3. **`135-sheet.jpg` là tờ kiểm ứng viên đầu**, còn redeemed try1 và perfect fit 717. Do cấm ghi đè, tờ này giữ nguyên; **dùng `135-sheet-final.jpg` khi chấm bộ giao**, chứa redeemed try2 và perfect fit 731. Các tờ `compare-audit.jpg` là so sánh đúng tỉ lệ vật; tờ cũ giữ làm lịch sử.
4. Không sao chép vào public, không gắn runtime; Claude làm khi nhận. Chủ dự án/Claude cần xem **grade-sloppy** (độ xỉn đất nung), **star-unlit 20 px** (tương phản sát ngưỡng) và chốt mâu thuẫn IoU. Không nhờ agent khác chấm thay Claude.
