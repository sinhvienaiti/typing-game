# Phiếu 160 · Wordwoven · Làm lại năm khung UI từ try1

Ngày làm: 29/10/2026, macOS, repo cha.

**Đã giao năm bộ `.v2` cạnh bản cũ: 10 PNG, 10 prompt và 5 JSON. Giữ nguyên mật độ pixel nguồn, toàn bộ góc đồng, mây cuộn và rail chạm; active dựng từ chính nút v2. Alpha và tương phản đạt các số đo bên dưới. Tự chấm năm ảnh M = 8, mock M = 8. Chưa thay runtime, chưa có chấm nhận của Claude. Ngoại lệ cần xem: đường cắt lớn hơn ước lượng, lòng nút nhân 0,55 và rail dùng cả dải nguồn làm ô lặp, chưa khóa thành một hoa văn đơn có pha nối tuyệt đối.**

## 1. Bản giao và ảnh cần mở

Thư mục: [ui/frames-epic/](../../games/typing-defense/art-src/ui/frames-epic/). Mỗi tên `panel-large`, `plate-long`, `button`, `button-active`, `tooltip` có:

- `<tên>.v2.png`: tranh hậu kỳ trên nền khóa magenta;
- `<tên>.v2.alpha.png`: bản trong suốt để tích hợp;
- `<tên>.v2.prompt.txt`, `<tên>.v2.alpha.prompt.txt`: prompt nguồn nguyên văn và công thức hậu kỳ thực tế;
- `<tên>.v2.json`: khổ, đường cắt, `repeat`, `display`, nguồn và vùng chữ.

**Bằng chứng cuối dùng bộ `handoff-02`, không dùng các ứng viên làm dở có trước phiên này.** Những file cũ trong `_review/160/` được giữ nguyên.

| Nội dung | Đường dẫn |
| --- | --- |
| HUD và menu Pause, mỗi cảnh 1280 × 720, cạnh ảnh tham chiếu | [160-mock.jpg](../../games/typing-defense/art-src/_review/160-mock.jpg) |
| Bản sinh và bản hậu kỳ, cùng crop, cùng mật độ pixel 1:1, đủ năm ảnh | [raw-vs-final/publish/](../../games/typing-defense/art-src/_review/160/raw-vs-final/publish/) |
| Năm khung mới, bốn trang trí đã nhận, ba cỡ dựng thử mỗi khung | [160-sheet-final.jpg](../../games/typing-defense/art-src/_review/160-sheet-final.jpg) |
| Cả bốn rail của từng khung, mỗi rail ghép ba lần | [160-rails-final.jpg](../../games/typing-defense/art-src/_review/160-rails-final.jpg) |
| Mép alpha phóng 4× trên nền tối, kem và xám | [160-edge-final.jpg](../../games/typing-defense/art-src/_review/160-edge-final.jpg) |
| Ba chuỗi chữ bắt buộc, Arial 24 px | [160-text-final.jpg](../../games/typing-defense/art-src/_review/160-text-final.jpg) |
| Năm khung 320 × 96; crest và ring 64 px | [160-small-final.jpg](../../games/typing-defense/art-src/_review/160-small-final.jpg) |
| Mock, tham chiếu và HUD cũ | [160-vs-ref-final.jpg](../../games/typing-defense/art-src/_review/160-vs-ref-final.jpg) |
| Ba sắc ngọc từ crest đã nhận | [160-jade-final.jpg](../../games/typing-defense/art-src/_review/160-jade-final.jpg) |
| Mock riêng 720p, dựng lại 1080p và số đo | [handoff-02/evidence/](../../games/typing-defense/art-src/_review/160/handoff-02/evidence/) |

Mock dùng `title-backdrop.v2.png` đã có của phiếu 158, giữ nguyên màu tranh. Bốn ảnh `banner`, `portrait-ring`, `crest`, `divider` đã nhận chỉ được đọc để ghép kiểm. Chữ kiểm đều tiếng Anh. Đây là mock tĩnh bằng ImageMagick, không phải ảnh chạy runtime.

## 2. Nguồn, hậu kỳ và prompt

Đã đọc phiếu 115, báo cáo 115, verdict 29/10 và tờ `115-frames-vs-ref.jpg`; đã xem nguồn try1, ảnh chủ dự án và HUD cũ. Dùng specialist `threejs-game-ui-designer` để kiểm bố cục mock.

**Không có lượt sinh mới.** Bốn khung lấy đúng `<tên>.try1.png`, kể cả tooltip. Active dùng `button.v2.alpha.png`, không dùng `button-active.try1.png`. Không cần áp prompt sửa rail bằng `image_gen` trong phiên này; giới hạn rail được khai báo ở mục 6.

Tái sử dụng bản key đã có trong `_review/160/`, xác nhận trùng nguyên byte với bản key từ try1 của phiếu 115. Các bản đó do `tools/art-normalize/key-alpha.sh` tạo, với `ART_MAGICK=/opt/homebrew/bin/magick`, `--bg '#FF00FF' --mode global --despill protect-interior --no-key-hue`. Không chạy lại công cụ vào thư mục tạm ngoài phạm vi.

Sau key: cắt bao toàn vật, chừa lề 12 px; **không thu/phóng bản giao**, không ghép lại góc, không lấy một tiết diện thay rail, không tô lại lòng bằng `fill`. Lòng ngọc nối tâm được nhân đều ba kênh RGB, giữ vân và quan hệ ánh sáng. Mọi pixel ngoài lòng giữ nguyên, trừ khử sắc khóa còn sót: chỉ hạ B về G ở pixel hue 285–330°, S > 0,5.

Active nhận ánh `#FFAE3B` theo vàng lá, quầng ngoài Gaussian sigma 8 px, ánh hắt sát mép lòng sigma 16 px. Hình và đường cắt kế thừa nút v2; alpha gốc không bị giảm, thêm **52.913 pixel quầng**. Không thêm chữ vào tài sản giao.

[Kiểm pixel độc lập với ảnh mock](../../games/typing-defense/art-src/_review/160/handoff-02/pixel-audit.json) xác nhận:

- đủ toàn vật sau crop, mật độ pixel **1:1**;
- alpha bốn khung thường trùng hoàn toàn bản key sau crop;
- mọi khác biệt RGB được giải thích bằng phép nhân sáng hoặc sửa sắc khóa; **0 pixel thay đổi ngoài hai loại đó**;
- số pixel sửa sắc khóa panel / plate / button / tooltip: **157 / 817 / 57 / 456**;
- không có thao tác thay phần vẽ, san hoa văn, tạo mặt ngọc phẳng hoặc chỉnh sáng toàn cảnh.

## 3. Khổ và 9-slice

Canvas nguồn vuông **1254 × 1254**, nguồn ngang **2172 × 724**. Khổ giao là khổ vật sau crop, khác bảng 115 theo yêu cầu mới giữ độ phân giải try1.

| Tên | Khổ v2 | Crop nguồn `[x,y,w,h]` | Slice L / R / T / B, px nguồn | Display L / R / T / B, px ở 1080p |
| --- | --- | --- | --- | --- |
| panel-large | 1183 × 1152 | 36, 36, 1183, 1152 | 210 / 210 / 210 / 210 | 56 / 56 / 56 / 56 |
| plate-long | 2134 × 460 | 20, 124, 2134, 460 | 300 / 300 / 185 / 185 | 60 / 60 / 37 / 37 |
| button | 2079 × 502 | 46, 96, 2079, 502 | 260 / 260 / 170 / 170 | 54 / 54 / 35,31 / 35,31 |
| button-active | như button | cùng nguồn button | như button | như button |
| tooltip | 1173 × 1151 | 41, 41, 1173, 1151 | 215 / 215 / 215 / 215 | 40 / 40 / 40 / 40 |

Các đường cắt lớn hơn ước lượng của verdict vì lấy **toàn cụm trang trí**, gồm cả đuôi mây, thay vì chỉ vòng mặt trời. Plate ban đầu thử L/R = 250 còn vướng đuôi mây; đã đưa vào 300 mà không thay một pixel tranh. Panel 210 tương đương khoảng 18% cạnh vật, khác gợi ý khoảng 11%; hạ xuống 125 sẽ đưa phần mây góc vào rail lặp.

Cả năm JSON có **`"repeat": "round"`** và **`"display"`**. Ở 720p, display nhân 2/3 rồi làm tròn theo pixel. Góc được thu đồng nhất khi dựng thử; phần giữa dùng tranh nguồn, rail dùng số ô lặp nguyên theo `round`. Không dùng màu `fill` của JSON để vẽ lòng; đó chỉ là metadata màu.

Ví dụ tích hợp panel ở 1080p: dùng `.v2.alpha.png`, `border-image-slice: 210 fill`, `border-image-width: 56px`, `border-image-repeat: round`. Kích thước góc nguồn vẫn là 210 px trong ảnh; 56 px chỉ là cỡ hiển thị.

## 4. Số đo

WCAG đo sRGB tuyến tính với chữ **`#f3ead2`**, lấy pixel nền sáng nhất trong toàn vùng chữ an toàn được ghi trong JSON. Cột cuối đo lại dưới các nét chữ thực tế của ba chuỗi bắt buộc trên khung dựng 500 × 160, Arial 24 px.

| Tên | Nhân RGB lòng | WCAG nguồn trước → sau | WCAG thấp nhất dưới ba chuỗi ở cỡ dựng |
| --- | ---: | ---: | ---: |
| panel-large | 1,00 | 7,072 → **7,072** | **12,921** |
| plate-long | 0,90 | 6,330 → **7,234** | **8,366** |
| button | 0,55 | 2,854 → **7,138** | **12,741** |
| button-active | kế thừa 0,55 | **7,138** sau ánh hắt | **12,741** |
| tooltip | 1,00 | 12,173 → **12,173** | **13,914** |

Lòng nút cần tối hơn gợi ý khoảng 0,7 để bảo đảm **mọi pixel** trong vùng chữ rộng đạt 7. Hệ số 0,55 chỉ áp lên thành phần ngọc trong lòng theo ngoại lệ làm tối lòng của phiếu; không áp lên viền/góc hay toàn ảnh. Tờ so button cho thấy vẫn còn đủ vân, không bị thay bằng mảng phẳng. Đây là điểm cần Claude xem về cảm nhận.

Tất cả năm alpha: **min 0, max 255; 0 pixel sắc khóa bị cấm; 0 đốm rời dưới 20 px**. Mép 4× không còn viền hồng. Không xóa thành phần hình vẽ để đạt số.

Đã dựng đủ **480 × 160, 320 × 320, 720 × 120**, thêm **320 × 96** cho cả năm khung. Cỡ nhỏ vẫn đọc ra huy chương mặt trời và góc mây; rest/active phân biệt rõ. Crest và ring 64 px giữ nguyên bản đã nhận, nhận ra được.

Số đo đầy đủ: [metrics.json](../../games/typing-defense/art-src/_review/160/handoff-02/evidence/metrics.json), [text-metrics.json](../../games/typing-defense/art-src/_review/160/handoff-02/evidence/text-metrics.json), [rail-metrics.json](../../games/typing-defense/art-src/_review/160/handoff-02/evidence/rail-metrics.json).

## 5. Ba sắc ngọc chuẩn

Lấy từ **`ui/frames-epic/crest.alpha.png` đã nhận**. Lọc pixel đục thuộc ngọc xanh, bỏ vàng/son/đá vôi; lấy trung vị RGB trong các dải luma quanh phân vị 15%, 50%, 90%. Không đổi màu crest hay áp màu phẳng vào năm khung.

| Sắc | Mã chuẩn |
| --- | --- |
| Sáng | **`#3B5530`** |
| Giữa | **`#27351B`** |
| Tối | **`#131C0A`** |

Mẫu giữa dành cho ngọc của huy hiệu; mẫu sáng cho phần bắt sáng, mẫu tối cho rãnh và lòng cần đọc chữ. Các phiếu sau dùng ba mẫu này làm mốc vật liệu, đồng thời giữ vân và ánh sáng thực của tranh. [Dữ liệu lấy mẫu](../../games/typing-defense/art-src/_review/160/handoff-02/evidence/jade-palette.json).

## 6. Tự chấm trên bản hậu kỳ và giới hạn rail

Q theo thứ tự: đúng đề / đọc được / hợp bộ / hình khối / dùng được cho bước sau. Điểm dưới đây tính từ đúng bản giao và các cỡ dựng, không chấm thay bằng try1.

| Tên | M | Q | Nhận xét |
| --- | ---: | ---: | --- |
| panel-large | **8** | **9 = 2/2/2/2/1** | Giữ đá chạm và bốn mặt trời; rail lặp còn thay đổi pha nhẹ ở chỗ nối khi soi lớn. |
| plate-long | **8** | **8,5 = 2/2/2/1,5/1** | Giữ trọn đầu mây; dáng rail cạnh bên vốn cong, hiện rõ hơn ở thử vuông cực đoan. |
| button | **8** | **9 = 2/2/2/2/1** | Đủ viền đá, góc đồng và vân ngọc; lòng tối hơn nguồn, vân đổi tỷ lệ ở khổ dựng rất khác nguồn. |
| button-active | **8** | **9 = 2/2/2/2/1** | Cùng hình với button, ánh hổ phách rõ, chữ đạt tương phản. |
| tooltip | **8** | **9 = 2/2/2/2/1** | Try1 giữ đủ huy chương và mây nhỏ, đọc được ở 320 × 96. |

**Mock HUD và Pause: M = 8. “Đứng cạnh được” về chất liệu và độ hoàn thiện khung ở cỡ sử dụng.** Góc đồng, rail đá và vân ngọc đều còn thấy ở 720p/1080p. Chưa ngang M = 9 của tham chiếu: tham chiếu có hệ icon/nội dung HUD hoàn chỉnh hơn, ngoài phạm vi phiếu này.

**Giới hạn còn lại:** mỗi rail giữ cả dải tranh nguồn giữa hai góc làm một ô `round`; dải có nhiều nét chạm, chưa phải một motif đơn được khóa pha tuyệt đối. Tờ ba lần vẫn cho thấy đổi pha hoặc vệt tối nhẹ ở một số mối nối panel; MAE RGB hai đầu các rail panel khoảng 10,7–25,3/255. Plate sau chuyển đường cắt còn khoảng 8,8–11,7/255. Không coi MAE là ngưỡng đạt mới, cũng không báo nối pixel tuyệt đối.

Đã dừng ở bản giữ tranh này để Claude quyết phần rail, thay vì san rail thành đường chỉ hay đổi phần đá chạm thành mảng trơn. Chưa thực hiện nhánh sửa ảnh `Make the straight sides plain bevelled limestone moulding, uniform along their length; keep the corners unchanged.` vì nhánh đó sẽ đổi phần chạm mà phiếu đang yêu cầu giữ. Đây là ngoại lệ còn mở của kiểm rail, không phải tuyên bố đã hoàn tất mọi điều kiện nghiệm thu.

## 7. KA1 và tái lập

`md5 -r` đệ quy toàn `art-src/ui/`, trước khi ghi và sau giao:

| Mốc | Số file |
| --- | ---: |
| Trước | **170** |
| Sau | **195** |
| Thêm | **25** |
| Sửa file có trước | **0** |
| Xóa file có trước | **0** |

[Trước](../../games/typing-defense/art-src/_review/160/handoff-01/md5-before.txt), [sau chuẩn hóa đường dẫn](../../games/typing-defense/art-src/_review/160/handoff-02/md5-after-normalized.txt), [diff chỉ thêm](../../games/typing-defense/art-src/_review/160/handoff-02/md5-normalized.diff.txt), [tổng kết](../../games/typing-defense/art-src/_review/160/handoff-02/md5-summary.json), [SHA-256 bản giao](../../games/typing-defense/art-src/_review/160/handoff-02/published-sha256.json).

Lượt audit sau giao đầu tiên so tên tuyệt đối với tên tương đối nên assertion báo sai; kiểm byte xác nhận không file cũ nào thay đổi. Đã chuẩn hóa đường dẫn, chạy lại thành công; giữ hồ sơ lỗi ban đầu để truy vết, chỉ dùng các file `normalized` ở trên.

Script cuối trong [_review/160/](../../games/typing-defense/art-src/_review/160/):

- `finish160-publish.py`: hậu kỳ từ key try1, giữ pixel, tạo active và metadata;
- `review160-publish.py`: dựng `round`, ảnh so, mép, chữ, ba cỡ và mock;
- `audit160-publish.py`: kiểm pixel, giao file độc quyền và kiểm MD5/SHA-256.

Chạy lại kiểm byte bản đã giao, không tạo lại ảnh hoặc ghi đè hồ sơ cũ:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
import hashlib, json
root = Path('/Users/toandx/htdocs/typing-game')
r = root / 'games/typing-defense/art-src/_review/160'
for name, digest in json.loads((r/'handoff-01/md5-before.json').read_text()).items():
    assert hashlib.md5((root/name).read_bytes()).hexdigest() == digest, name
for name, digest in json.loads((r/'handoff-02/published-sha256.json').read_text()).items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest, name
print('170 file cũ nguyên trạng; 25 file giao trùng SHA-256.')
PY
```

Các script sinh ảnh kiểm dùng writer tên mới; muốn dựng lại phải chọn thư mục/tiền tố mới. `160-mock.jpg` là bản cuối, trùng byte `160-mock-final.jpg`; bản nháp đầu do phiên này tạo được giữ ở `handoff-01/evidence/160-mock-first.jpg`.

## 8. Đã bỏ qua và việc người nhận cần xem

Không sinh lại ảnh, không sửa bốn trang trí đã nhận, không đổi logo/huy hiệu/màn tựa, không làm âm thanh, không sửa runtime hoặc game khác. Không chạy game, trình duyệt, dev server, build hay test suite; không có frame trình duyệt mới cần dọn. Không đọc/ghi Tu Tiên, không commit/push/reset/clean/stash.

Đầu phiên đã lỡ chạy **một lệnh chỉ đọc `git status --short`**, trái lệnh cấm mọi Git trong phiếu 115. Không dùng thêm lệnh Git sau khi đọc đầy đủ luật; không có thay đổi Git nào từ lệnh đó.

Claude cần mở **mock cuối**, **năm tờ trước–sau**, **rail ba lần** và **mẫu ngọc**; quyết ngoại lệ rail, mức tối 0,55 của nút và đường cắt theo toàn cụm góc. Chờ Claude chấm lại M/Q và đổi đường dẫn tích hợp sang `.v2` khi nhận. Không coi tự chấm là nghiệm thu.
