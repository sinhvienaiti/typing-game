# Phiếu 127 · Last Line · Chín khung UI hướng B, chưa nghiệm thu

Ngày 29/10/2026, Codex. Đã sinh **16 lượt cho 9 ảnh**, giữ đủ bản thử và prompt; mỗi ảnh tối đa ba lượt. Có chín bản chọn đúng khổ, chín alpha, sáu JSON 9-slice và các tờ kiểm. **Chưa đạt điều kiện giao nhận:** cả chín alpha còn pixel tím rất tối; `panel-large` có một thành phần rời 2 px, `divider` có 40 thành phần dưới 20 px. Không coi các điểm M/Q tự chấm dưới đây là thay thế cho những chốt kỹ thuật đang trượt.

Điều kiện chọn hướng đã đủ: [ART_DIRECTION_2026-10-28 §4.3](../games/ART_DIRECTION_2026-10-28.md#43-bible-last-line-hướng-b-chủ-dự-án-chọn-2910) ghi chủ dự án chọn **B · Lightbearer sáng 29/10** và cho phép phiếu 127 chạy. Không tự suy ra lựa chọn từ điểm ở báo cáo 112.

## Ảnh và hồ sơ giao

Gốc media: [`games/typing-survival/art-src/ui/frames-epic/`](../../games/typing-survival/art-src/ui/frames-epic/). Tên cơ sở trong bảng có đủ `.png`, `.prompt.txt`, `.alpha.png`; sáu khung đầu có thêm `.json`. Bản chọn `.png` còn nền magenta; bản `.alpha.png` dùng cho ghép. Prompt của bản chọn là nguyên văn prompt của đúng lượt được chọn.

| Tên | Bản chọn | Khổ giao | 9-slice |
| --- | --- | --- | --- |
| `panel-large` | try2 | 1024 × 1024 | Có |
| `bay-card` | try2 | 1536 × 512 | Có |
| `word-plate` | try2 | 1536 × 512 | Có |
| `plate-long` | try2 | 1536 × 512 | Có |
| `button` | try3 | 1536 × 512 | Có |
| `button-active` | try1, đính kèm bản `button.png` đã chọn | 1536 × 512 | Cùng đường cắt với `button` |
| `banner` | try2 | 1536 × 512 | Không |
| `portrait-ring` | try1 | 1024 × 1024 | Không |
| `divider` | try1 | 1536 × 512 | Không |

Ảnh kiểm:

- [Tờ chín bản chọn, 18 bản dựng 9-slice và cặp nút](../../games/typing-survival/art-src/_review/127-sheet.jpg).
- [Mock trận 1920 × 1080](../../games/typing-survival/art-src/_review/127-mock.jpg): hai thẻ súng, bảng từ trên đầu nhân vật, Armor và banner. Toàn bộ chữ thêm vào mock là tiếng Anh.
- [Tờ so với tham chiếu](../../games/typing-survival/art-src/_review/127-vs-ref.jpg): mock và ảnh chủ dự án cùng cao 640 px; hàng dưới lấy ô đầu của tờ trận hôm nay. Nhận xét: **chưa** — chất liệu và màu hợp cảnh sử thi, nhưng alpha và độ đều của nét cạnh cần xử lý trước nghiệm thu.
- [Mép phóng 4×](../../games/typing-survival/art-src/_review/127-edge.jpg) và [bổ sung mép thật của banner, vòng chân dung, divider](../../games/typing-survival/art-src/_review/127-edge-detail.jpg). Ở ba ô sau của tờ đầu, góc bbox có vùng trống; tờ bổ sung lấy đúng phần vẽ ở mép.
- [Chữ thử và tương phản](../../games/typing-survival/art-src/_review/127/text-proof.jpg).

Mỗi bản có tờ “bản sinh | bản hậu kỳ”, cùng kích thước hiển thị, bản hậu kỳ đặt trên nền xám để nhìn alpha:

| Ảnh | Tờ kiểm |
| --- | --- |
| Panel | [panel-large](../../games/typing-survival/art-src/_review/127/panel-large-before-after.jpg) |
| Thẻ súng | [bay-card](../../games/typing-survival/art-src/_review/127/bay-card-before-after.jpg) |
| Bảng từ | [word-plate](../../games/typing-survival/art-src/_review/127/word-plate-before-after.jpg) |
| Thanh HUD | [plate-long](../../games/typing-survival/art-src/_review/127/plate-long-before-after.jpg) |
| Nút thường | [button](../../games/typing-survival/art-src/_review/127/button-before-after.jpg) |
| Nút chọn | [button-active](../../games/typing-survival/art-src/_review/127/button-active-before-after.jpg) |
| Banner | [banner](../../games/typing-survival/art-src/_review/127/banner-before-after.jpg) |
| Vòng chân dung | [portrait-ring](../../games/typing-survival/art-src/_review/127/portrait-ring-before-after.jpg) |
| Dải phân cách | [divider](../../games/typing-survival/art-src/_review/127/divider-before-after.jpg) |

## Các lượt sinh và thay đổi prompt

Dùng skill `imagegen` và công cụ tích hợp `image_gen`, mỗi lần một ảnh; không gọi API/CLI hay mạng khác. STYLE-UI, phần riêng, FRAME khi áp dụng và dòng nền M của phiếu được giữ nguyên văn. Phần bổ sung kỹ thuật ghi rõ khổ, một vật trọn vẹn, lề và glyph hình học không thành chữ. Câu cấm khung/viền trong luật chung được hiểu là không thêm khung trình bày bên ngoài; chính vật thể được yêu cầu trong phiếu là khung UI.

| Ảnh | Lượt | Kết quả và sửa đúng chỗ thiếu |
| --- | --- | --- |
| Panel | 1 | Có vật liệu tốt nhưng đính nút và hình thoi giữa các cạnh; không chọn. |
| Panel | 2 | Thêm yêu cầu hoa văn chỉ trong bốn góc nhỏ, cạnh là một dải kim loại liên tục, độ sáng đều. Chọn; không xóa hoa văn lượt 1 bằng công cụ. |
| Thẻ súng | 1 | Có bậc lõm giữa cạnh dưới. |
| Thẻ súng | 2 | Khóa góc gọn, giữa cạnh không nút/khía/điểm sáng riêng; giữ đường lam phía trên. Chọn. |
| Bảng từ | 1 | Có hình thoi ở giữa cạnh trên/dưới. |
| Bảng từ | 2 | Cùng chỉ dẫn 9-slice chặt hơn, giữ kính tối và ánh lam phía dưới. Chọn. |
| Thanh HUD | 1 | Hình thoi và chấm trang trí nằm dọc cạnh ngang. |
| Thanh HUD | 2 | Gom dấu và ánh sáng riêng vào góc; cạnh thẳng liền. Chọn. |
| Nút | 1 | Hoa văn và vết xước trải sâu vào lòng, cạnh chưa gọn. |
| Nút | 2 | Thu góc và làm liền cạnh ngang; vẫn có một đoạn đèn riêng giữa hai cạnh ngắn. |
| Nút | 3 | Sửa riêng hai cạnh ngắn thành dải liên tục; bỏ cung chòm sao khỏi lòng bằng prompt. Chọn; đã dùng đủ ba lượt. |
| Nút chọn | 1 | Đính kèm `button.png` đã chọn, có nguyên câu SAME. Giữ dáng và góc, tăng viền cyan và sáng trắng vàng bên trong. Chọn. |
| Banner | 1 | Huy chương/hố đen giữa ảnh và hoa văn dày làm thiếu chỗ đặt tên ải. |
| Banner | 2 | Chừa vùng kính tối ở giữa, đưa đường sáng xuống nửa dưới, giữ hai đầu cam vàng. Chọn. Đây là điều chỉnh bố cục của đường sáng so với câu riêng ban đầu, để chữ không chạm đường sáng. |
| Vòng chân dung | 1 | Đủ vòng thép, bốn chốt, chỉ vàng trắng, lòng magenta; chọn. |
| Divider | 1 | Đọc được đường vàng và tâm lam; chọn về hình thức nhưng nhiều chấm quá nhỏ sau tách nền. Giữ phần vẽ theo §5, chưa đạt chốt thành phần rời. |

Toàn bộ `.tryN.png` và `.tryN.prompt.txt` còn nguyên. Không có ảnh nào vượt ba lượt.

## Hậu kỳ và khổ

Hai ảnh vuông được công cụ trả **1254 × 1254**, các bản ngang được chọn là **2172 × 724**. Tỷ lệ đã đúng, nên bước cắt giữa không bỏ nội dung; thu Lanczos về đúng bảng. Lệnh thực tế, khổ đầu vào và hình chữ nhật cắt của từng ảnh nằm trong `_review/127/<tên>-selection.json`.

Ví dụ lệnh thu nút:

```sh
/opt/homebrew/bin/magick button.try3.png -gravity center -crop 2172x724+0+0 +repage -filter Lanczos -resize '1536x512!' button.png
```

Chạy `tools/art-normalize/key-alpha.sh` với `ART_MAGICK=/opt/homebrew/bin/magick`, `--bg '#FF00FF' --mode global --despill protect-interior --no-key-hue`. Prompt loại sắc magenta khỏi chủ thể nên có cơ sở dùng `--no-key-hue`. Không co mask, không thay nền kính hay san phẳng cạnh. Nhật ký từng ảnh là `_review/127/<tên>-alpha-log.txt`.

Wrapper mặc định ghi thư mục tạm vào `tools/art-normalize/.tmp/`, ngoài phạm vi cho phép. Shim `_review/127/bin/python3` nạp nguyên module, chỉ đổi biến `WORK` trong bộ nhớ sang `_review/127/normalize-work/`, rồi gọi CLI hiện có. Vẫn chạy shell `key-alpha.sh`; không sửa file công cụ và không ghi thư mục tạm của công cụ dùng chung.

**Sai sót về thứ tự xử lý:** tên `.alpha.png` được chốt trước khi đo đầy đủ. Vì phiếu cấm ghi đè file đã có, không thay các file này bằng một bản chỉnh tiếp. Các số dưới đây đo chính alpha đã giao, không đo một bản tạm đẹp hơn. Cần xử lý lại thành bộ mới trước khi tích hợp.

## Alpha: chưa qua chốt 3

Đo RGB 8-bit của mọi pixel có alpha > 0; HSV hue 285–330°, S > 0,5. Phần trăm trong bảng tính trên toàn canvas; số pixel tuyệt đối cũng ghi để không làm tròn lỗi nhỏ thành 0. Thành phần rời dùng liên thông 8 hướng, alpha > 0, ngưỡng nhỏ hơn 20 px.

| Bản chọn | Alpha min/max | Pixel tím | % canvas | Thành phần < 20 px |
| --- | --- | ---: | ---: | ---: |
| Panel | 0 / 255 | 24 | 0,002289% | 1 |
| Thẻ súng | 0 / 255 | 296 | 0,037638% | 0 |
| Bảng từ | 0 / 255 | 54 | 0,006866% | 0 |
| Thanh HUD | 0 / 255 | 177 | 0,022507% | 0 |
| Nút | 0 / 255 | 223 | 0,028356% | 0 |
| Nút chọn | 0 / 255 | 46 | 0,005849% | 0 |
| Banner | 0 / 255 | 268 | 0,034078% | 0 |
| Vòng chân dung | 0 / 255 | 509 | 0,048542% | 0 |
| Divider | 0 / 255 | 127 | 0,016149% | 40 |

Tâm `portrait-ring` có **alpha 0**. Các pixel tím còn lại rất tối: kênh RGB lớn nhất theo ảnh từ 24 đến 75/255; không phải mảng hồng rực, nhưng vẫn **trượt yêu cầu đúng 0**. Không thể gọi viền sạch chỉ vì ở cỡ thường khó thấy. Không xóa chấm vẽ để làm số đạt: nhiều thành phần nhỏ của divider nằm trên chính các đường/chấm chòm sao. Đây là mâu thuẫn cần Claude xử lý theo ART_ACCEPTANCE §5. Đốm panel có diện tích 2 px, bbox `[70, 402, 1, 2]`.

Số đo và bbox từng thành phần: [measurements-v1.json](../../games/typing-survival/art-src/_review/127/measurements-v1.json).

## 9-slice và độ đều cạnh

JSON dùng tọa độ pixel của ảnh nguồn, `fill` là trung vị RGB của vùng 100 × 50 px ở giữa lòng. Không dùng màu fill để phủ lên phần vẽ trong các tờ dựng. Ba cỡ mỗi khung là **480 × 160, 320 × 320, 720 × 120**.

Nguồn được coi là asset mật độ **4×**: góc hiển thị bằng 1/4 số pixel nguồn và giữ cùng cỡ giữa ba bản dựng. Nếu giữ góc ở kích thước pixel nguồn, riêng tổng hai góc cao đã vượt 120 px. Chỉ các dải giữa được kéo độc lập; góc thu đồng đều bằng Lanczos. Đây là quy ước dựng thử cần được người tích hợp giữ lại, không phải thay đổi runtime.

Độ lệch chuẩn dưới đây đo profile luma sRGB 0–1 theo chiều kéo: mỗi vị trí lấy trung bình vuông góc trên toàn dải cạnh. Dải trong suốt giữ RGB 0; khai báo rõ để không nhầm với phép đo chỉ trên phần sơn.

| Khung | L / R / T / B nguồn | σ trên | σ dưới | σ trái | σ phải |
| --- | --- | ---: | ---: | ---: | ---: |
| Panel | 200 / 200 / 200 / 200 | 0,01049 | 0,01080 | 0,00905 | 0,00894 |
| Thẻ súng | 300 / 300 / 200 / 200 | 0,01085 | 0,00450 | 0,00391 | 0,00787 |
| Bảng từ | 230 / 230 / 220 / 220 | 0,00659 | 0,00662 | 0,00262 | 0,00189 |
| Thanh HUD | 240 / 240 / 220 / 220 | 0,00813 | 0,00500 | 0,00316 | 0,00244 |
| Nút | 190 / 190 / 200 / 200 | 0,00599 | 0,00347 | 0,00289 | 0,00546 |
| Nút chọn | 190 / 190 / 200 / 200 | 0,01086 | 0,00773 | 0,00304 | 0,00336 |

Sáu khung đạt ≤ 0,05 **theo phép đo profile trên**. Xem trực tiếp ba cỡ: không còn huy chương hay đinh riêng ở giữa cạnh ngang; các góc không bị kéo dài. Lòng có vệt chất liệu nhẹ khi kéo thành vuông.

Đã giữ thêm phép đo chặt hơn: σ lớn nhất của từng hàng/cột riêng trong dải, ở `measurements-v1.json`. Phép đó cho cực đại khoảng **0,066–0,263** tùy khung, nhạy với đường viền sáng lượn/đổi vị trí vài pixel. Đường cắt của phép chẩn đoán đầu tiên cũng khác T/B cuối cùng ở một số khung, nên không xem hai bảng là cùng một mẫu. Không gọi đây là chốt cạnh tuyệt đối đã đạt; Claude cần thống nhất cách đo. Không san phẳng hoặc tô lại cạnh để ép σ thấp. [Profile và đường cắt cuối](../../games/typing-survival/art-src/_review/127/edge-profiles.json).

## Chữ thử và tương phản

Font Arial của macOS; chữ `#f2f4f8`, 24 px, riêng `thank` 42 px. WCAG dùng luma tuyến tính sRGB, đo nền bên dưới mọi pixel thuộc mặt nạ nét chữ trước khi vẽ chữ; báo cáo giá trị thấp nhất, không tính pixel khử răng cưa của chữ như màu chữ mới.

| Khung | Chữ | Cỡ | Tương phản nhỏ nhất |
| --- | --- | ---: | ---: |
| Panel | Stage 1 · First Watch | 24 | 15,74:1 |
| Thẻ súng | Pulse Gun | 24 | 16,35:1 |
| Bảng từ | thank | 42 | 15,68:1 |
| Thanh HUD | Armor 100 | 24 | 15,77:1 |
| Nút | Resume | 24 | 15,59:1 |
| Nút chọn | Resume | 24 | 15,52:1 |
| Banner | Stage 1 · First Watch | 24 | 13,48:1 |

**7/7 đạt ≥ 7:1.** Banner được thử chữ phía trên đường sáng, không đặt chữ đè lên đường trắng vàng. Số đo này thuộc tờ chữ thử, không phải một phép đo toàn bộ HUD trong runtime. [Dữ liệu](../../games/typing-survival/art-src/_review/127/text-contrast.json).

## KA5 · Tự chấm trên bản hậu kỳ

Đã xem chín alpha ở khổ đầy đủ, cặp trước/sau, tờ dựng và mock. M của từng khung chấm chất liệu, độ hoàn thiện, khả năng đọc ở cỡ UI và sự hợp cảnh sử thi theo cách diễn giải cho khung UI ở phiếu 115; không đòi một khung độc lập phải chứa cảnh ba tầng và trời. M cảnh được chấm riêng trên mock. Đây là điểm Codex, **chưa có Claude chấm lại**.

Q theo thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí tối đa 2. Trừ khả năng dùng tiếp vì alpha và các giới hạn kéo cạnh; divider còn trừ khả năng đọc nét nhỏ. Không lấy tổng Q để bỏ qua chốt kỹ thuật.

| Bản chọn | M | Năm điểm Q | Q | Nhận xét |
| --- | ---: | --- | ---: | --- |
| Panel | 8,1 | 2 / 2 / 2 / 1,5 / 1 | 8,5 | Góc có chiều sâu; một đốm nhỏ và viền chưa sạch tuyệt đối. |
| Thẻ súng | 8,0 | 2 / 2 / 2 / 1,5 / 1 | 8,5 | Đường lam trên đọc rõ; kính gọn, còn pixel tím tối. |
| Bảng từ | 8,1 | 2 / 2 / 2 / 1,5 / 1 | 8,5 | Chữ nổi, ánh lam phía dưới đúng vai trò; cạnh ngắn cần duyệt thêm. |
| Thanh HUD | 8,0 | 1,5 / 2 / 2 / 1,5 / 1 | 8,0 | Đầu thanh thiên về bốn góc hơn hai end-cap riêng, vẫn hợp bộ. |
| Nút | 8,0 | 1,5 / 2 / 2 / 1,5 / 1 | 8,0 | Lượt 3 mềm dáng hơn graphite tablet ban đầu; viền đọc rõ. |
| Nút chọn | 8,1 | 2 / 2 / 2 / 1,5 / 1 | 8,5 | Trạng thái khác rõ, cùng dáng; cần kiểm chuẩn alpha trước dùng. |
| Banner | 8,1 | 1,5 / 2 / 2 / 2 / 1 | 8,5 | Đọc tên ải tốt; đường sáng được đưa xuống nửa dưới so với mô tả đầu. |
| Vòng chân dung | 8,1 | 2 / 2 / 2 / 2 / 1 | 9,0 | Bốn chốt và lòng trong suốt rõ; mép còn pixel tím rất tối. |
| Divider | 8,0 | 2 / 1 / 2 / 2 / 0,5 | 7,5 | Hợp bộ nhưng nhiều chi tiết nhỏ bị rời; chưa dùng trực tiếp. |

**M chung của `127-mock.jpg`: 8,0.** Kính khói, chỉ vàng trắng và lam hợp nhân vật, có phân cấp chữ; cảnh nền mang quy mô và chiều sâu của hướng B. Điểm giới hạn: banner lớn che một phần bầy và cảnh vẫn dày ánh sáng; đây là mock tĩnh, không phải ảnh nghiệm thu trong game. Về hình thức đã gần mức phát hành, nhưng toàn bộ phiếu **chưa đạt** vì KA3, Q divider và cách chốt cạnh còn cần xử lý.

## KA1 và phạm vi

Đã chạy `/sbin/md5 -r` từng file đệ quy trong `games/typing-survival/art-src/` trước lần ghi đầu: **1488 file**. Snapshot sau có **1690 file**, **202 đường dẫn thêm**, **0 thay đổi**, **0 bị mất** so với baseline. Diff chỉ có dòng nội dung thêm. Không quy mọi file thêm trong một repo có nhiều agent thành sản phẩm riêng của phiếu này.

- [Manifest trước](../../games/typing-survival/art-src/_review/127/md5-before.txt).
- [Manifest sau](../../games/typing-survival/art-src/_review/127/md5-after.txt).
- [Diff](../../games/typing-survival/art-src/_review/127/md5-diff.txt).
- [Kết quả](../../games/typing-survival/art-src/_review/127/md5-summary.json).

Manifest sau được tính trước khi ghi chính nó, diff và JSON kết quả; ba file này không tự băm đệ quy. Báo cáo nằm ngoài cây art-src. Không tạo thêm media sau snapshot.

Script và cấu hình nằm trong `_review/127/`: `baseline.py`, `prepare.py`, `refine.py`, `extra-prompts.py`, `select.py`, `alpha-run.py`, shim `bin/python3`, `measure.py`, `proofs.py`, `edge-details.py`, `audit.py`, `jobs.json`. Các writer từ chối tên đích đã có. Khối sửa prompt panel lượt 2 được lưu nguyên văn ngay cạnh bản try; tái sinh bằng công cụ tích hợp với chính prompt đó. Không có runner mạng khác.

`select.py` trùng tên module chuẩn Python `select`, nên lần chạy trực tiếp đầu bị lỗi import trước khi viết bản chọn. Giữ nguyên script và chạy từ repo root qua `runpy.run_path`, không thêm thư mục script vào `sys.path`. Các script sau dùng cùng cách gọi:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -c 'import runpy; runpy.run_path("games/typing-survival/art-src/_review/127/measure.py", run_name="__main__")'
```

Lệnh trên là mẫu cho một lô trống; chạy lại trên hồ sơ này sẽ bị chặn để giữ các mốc đo. Không chạy Git, dev server, trình duyệt, build/test game. Không đọc/ghi Tu Tiên; không sửa mã game, công cụ dùng chung hay tài liệu khác. Không làm icon/hình nhỏ của ô, không tạo âm thanh vì ngoài phạm vi phiếu. Không có capture trình duyệt hay raw frame cần prune; các try bắt buộc giữ nguyên.

## Cần xem trước khi cho dùng

Chủ dự án xem mock và tờ so tham chiếu để xét độ hợp hướng B. Claude cần chấm lại M/Q, xử lý xung đột chấm chòm sao với ngưỡng thành phần rời, và chốt cách đo cạnh. Cần một lượt hậu kỳ mới tách/khử sắc viền rồi đo trước khi chốt tên xuất; không sửa bộ đã ghi trong lượt này. **Chưa tích hợp và chưa tuyên bố hoàn tất phiếu 127.**
