# Phiếu 020c · Lời Gọi · V37 Lò Đúc Tiền nguội

Ngày 27/10/2026. Sinh ảnh bằng `image_gen`, ba lượt. **Chọn lượt 3**, Codex tự chấm **8,5/10, Đạt theo ngưỡng ảnh 2D**, không thấy vùng phát sáng. **Chờ Claude chấm lại trước khi gửi Tripo.**

**Ngoại lệ kiểm md5:** 43/43 file có từ đầu giữ nguyên. Diff toàn thư mục có thêm một file `.fix.png` ngoài phiếu, nên chưa đạt nguyên văn chốt “diff chỉ có file `.try*` mới”. Giữ đầy đủ diff thô; không xóa hoặc sửa file của công việc đồng thời để làm sạch kết quả.

## 1. Bản giao và tự chấm

- Bản chọn: [gold-mine-lo-duc-tien.try3.png](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try3.png), [prompt chính xác](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try3.prompt.txt).
- Hai lượt trước: [lượt 1](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try1.png), [prompt 1](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try1.prompt.txt); [lượt 2](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try2.png), [prompt 2](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try2.prompt.txt).
- Tờ xem nhanh: [020c-v37.jpg](../../games/typing-defense/art-src/_review/020c-v37.jpg). Hàng 1: gốc, lượt 1, lượt 2, lượt 3; hàng 2: bản chọn cạnh Hầm Sâu ở đúng 128 px, rồi đúng 64 px; có nhãn.
- [Hồ sơ kiểm và ảnh raw](../../games/typing-defense/art-src/_review/020c/): ba ảnh raw giữ nguyên, prompt cạnh từng ảnh, bản alpha trung gian, ảnh nhỏ, số đo và mã tái lập.

Đã đọc prompt cũ, V37 trong `02-tripo-buildings-props-vs.md`, `ART_FIX_QUEUE.md` §5.1 và thang điểm `ART_ACCEPTANCE.md` §1–2.2. Mọi prompt giữ nguyên toàn bộ prompt cũ ở đầu, cộng câu yêu cầu lò nguội và các ràng buộc bên dưới. Lượt 1–2 đính kèm ảnh V37 hiện tại; lượt 3 đính kèm ảnh hiện tại làm mẫu bố cục và lượt 2 làm ảnh cần chỉnh vật liệu.

Chấm trên ảnh thu xuống 128 px. Thứ tự năm điểm trong bảng: **Đúng đề / Đọc được trong game / Hợp bộ / Hình khối / Dùng được cho bước sau**, mỗi tiêu chí tối đa 2.

| Lượt | Prompt thêm | Điểm 5 tiêu chí | Tổng | Có vùng phát sáng? | Còn thiếu |
|---|---|---|---:|---|---|
| 1 | Lò nguội, lòng lò đá ám muội có chiều sâu; ba thỏi nguội thay dòng vàng; vàng đất quanh `#C8962E`; giữ bố cục và nền BG-G. | 1,5 / 1,5 / 2 / 2 / 1 | 8 | Viền vàng còn lóe, dễ gợi cảm giác nóng; không có lửa hoặc quầng sáng. | Mặt vàng bóng và đá sáng còn nhiều điểm gắt; hộp gộp chỉ giảm 54,35%, chưa đạt kiểm. |
| 2 | Thêm vật liệu lì, màu vàng `#B5872C`–`#C8962E`, bỏ viền trắng/vàng chanh; hạ mặt đá sáng, giữ đá ám muội. | 1,5 / 1,5 / 2 / 2 / 1,5 | 8,5 | Không thấy vùng tự phát sáng ở 128 px; còn vài vệt bóng sáng trên vàng/đá. | Miệng lò giảm 83,07%, nhưng máng 76,41%, hộp gộp 74,78%; tiếp tục để đạt mục Kiểm. |
| **3 · chọn** | Khóa vật liệu lì: mặt vàng sáng nhất quanh `#C8962E`, mặt chính `#B07F25`, đá sáng `#B8AEA0`; yêu cầu kênh màu vật thể ≤205, bỏ mọi chấm/viền lóe. Giữ hình học lượt 2. | **1,5 / 1,5 / 1,5 / 2 / 2** | **8,5** | **Không. Lòng lò tối có chiều sâu, thỏi rắn màu vàng đất, không quầng sáng hoặc ánh sáng hắt.** | Cụm chi tiết nhỏ hơi rối ở 128 px; sắc độ lì trầm hơn Hầm Sâu. Vẫn thiếu cửa hầm/ray như ảnh gốc, không tự thêm. |

Câu yêu cầu giữ trong cả ba prompt: “The foundry is cold and idle: the furnace mouth is soot-black stone with no fire and no glow; the trough holds a few cooled gold ingots, matte ochre, not molten, no light, no emissive colour anywhere.” Các mã màu là chỉ dẫn sinh ảnh; không coi đó là bảng màu được lượng tử hóa tuyệt đối của đầu ra.

Bản chọn giữ ống khói, mái ngói đỏ, hai vòng xoắn đá, máng, bộ ép tiền, bao tiền, thùng vàng, bó gỗ, bàn tiền, bàn nghiêng phía trước bên phải, bệ gỗ và nền đá có vân quặng. Lòng lò là các khối đá riêng, không phải mảng màu phẳng tô đè. Ở 64 px vẫn phân biệt được mái đỏ, ống khói và lò tối, nhưng tiền lẻ/vòng xoắn không còn rõ từng nét.

## 2. Kiểm bắt buộc

### 2.1. Md5 toàn bộ `branches/`

Đo bằng `md5 -r`, duyệt toàn bộ file theo thứ tự đường dẫn:

| Hồ sơ | Kết quả |
|---|---|
| [md5-before.txt](../../games/typing-defense/art-src/_review/020c/md5-before.txt) | 43 file, chụp trước khi ghi prompt/ảnh lượt 1. |
| [md5-after-final.txt](../../games/typing-defense/art-src/_review/020c/md5-after-final.txt) | 52 file. 43 file ban đầu giữ nguyên; không file cũ đổi hoặc mất. |
| [md5-diff-final.txt](../../games/typing-defense/art-src/_review/020c/md5-diff-final.txt) | Diff thô từ `diff -u`; 9 dòng thêm, không dòng xóa/sửa dữ liệu. |
| [md5-diff-020c-only.txt](../../games/typing-defense/art-src/_review/020c/md5-diff-020c-only.txt) | Đối chiếu bổ sung, lọc rõ phạm vi: nền ban đầu + đầu ra 020c; chỉ thêm 6 file V37 `.try1/2/3.png` và `.try1/2/3.prompt.txt`. Không thay thế diff thô. |

Ba file thêm ngoài phiếu xuất hiện trong lúc chạy: `branches/barracks-giao-dai.try2.png`, `branches/barracks-giao-dai.try2.prompt.txt`, `branches/barracks-giao-dai.fix.png`. Phiếu này không tạo hoặc sửa các file đó. Riêng `.fix.png` làm **chốt diff toàn thư mục chưa đạt nguyên văn yêu cầu**. Không loại dòng này khỏi diff thô.

Md5 ảnh V37 gốc: `7049d4ca821e9b4b7f7127461a9baf4d`; prompt gốc: `8e07ebafdc9f6c815e9112d265435e56`. Md5 bản chọn: `f9924a48bf43e9e7d5c464575cbd38d9`.

### 2.2. Độ sáng miệng lò và máng

Hộp được chốt trước khi xem ảnh mới, ghi ở [roi-spec.txt](../../games/typing-defense/art-src/_review/020c/roi-spec.txt). Gốc tọa độ trên trái, đơn vị pixel; dùng **cùng tọa độ** trên gốc và bản chọn 1024×1024. Không trim hoặc căn lại vật thể để đổi vùng đo.

| Hộp (x, y, rộng, cao) | Trung bình gốc (0–1) | Trung bình chọn (0–1) | Pixel >0,85 gốc | Pixel >0,85 chọn | Giảm pixel sáng gắt |
|---|---:|---:|---:|---:|---:|
| Miệng lò (290, 490, 140, 125) | 0,435203 | 0,255625 | 3,308570% | 0,005714% | **99,83%** |
| Máng (340, 570, 170, 105) | 0,402220 | 0,328456 | 3,680670% | 0,005602% | **99,85%** |
| Gộp (290, 490, 220, 185) | 0,411322 | 0,304465 | 2,201470% | 0,002457% | **99,89%** |

**Đạt mục tiêu giảm ít nhất 80% ở cả ba hộp.** Hộp miệng lò và máng có phần chồng nhau; không cộng số pixel của hai hộp để tính hộp gộp. Hộp gộp bản chọn còn 1 pixel vượt ngưỡng, không tạo thành vùng phát sáng quan sát được.

Lệnh đo trung bình: `magick IN -gravity NorthWest -crop WxH+X+Y +repage -colorspace Gray -format '%[fx:mean]' info:`. Đo tỉ lệ bằng cùng lệnh, thêm `-threshold 85%` trước `-format`. Tỉ lệ giảm = `100 × (1 − tỉ_lệ_chọn / tỉ_lệ_gốc)`.

Dữ liệu: [brightness-final.json](../../games/typing-defense/art-src/_review/020c/brightness-final.json), [cả ba lượt](../../games/typing-defense/art-src/_review/020c/brightness-all-tries.json). [Ảnh hộp gộp đối chiếu](../../games/typing-defense/art-src/_review/020c/roi-comparison-final.jpg) dùng cùng tọa độ, chỉ phóng gấp đôi để đọc vật liệu. Không dùng số đo sáng để thay cho kiểm cảm nhận phát sáng.

### 2.3. Khổ và nền

Đầu ra `magick identify`:

```text
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try3.png PNG 1024x1024 1024x1024+0+0 8-bit sRGB 1.04655MiB
```

| Ảnh | Trên trái | Trên phải | Dưới trái | Dưới phải |
|---|---|---|---|---|
| Gốc | (17,244,32) | (13,244,23) | (14,244,24) | (13,245,27) |
| Chọn | (0,255,0) | (0,255,0) | (0,255,0) | (0,255,0) |

Bản chọn có nền **BG-G `#00FF00`**. Kiểm thêm toàn bộ viền ngoài 16 px: **64.512 pixel, đúng một màu (0,255,0)**. Vành khử răng cưa quanh vật thể có màu pha, không tính là biến thiên nền trống. [Identify và bốn góc](../../games/typing-defense/art-src/_review/020c/identify-corners-final.txt), [kiểm viền](../../games/typing-defense/art-src/_review/020c/background-final.json).

Công cụ sinh ảnh trả raw 1254×1254 ở cả ba lượt. Dùng công cụ `normalize.key` hiện có với `ART_MAGICK=/opt/homebrew/bin/magick`, tách nền `auto`, fuzz 6%, global, bảo vệ phần trong; sau đó thu đều toàn canvas về 1024×1024 và ghép nền `#00FF00`. Không chỉnh màu/độ sáng công trình bằng hậu kỳ, không tô sửa miệng lò. `WORK` chuyển vào `_review/020c/work`, tắt bytecode Python để không ghi ra ngoài phạm vi. [Lệnh hậu kỳ đầy đủ](../../games/typing-defense/art-src/_review/020c/normalization-all.txt).

### 2.4. Tờ xem nhanh và hồ sơ

[020c-v37.jpg](../../games/typing-defense/art-src/_review/020c-v37.jpg) đủ ảnh gốc, mọi lượt, bản chọn cạnh `gold-mine-ham-sau.png` ở 128 và 64 px. Dùng Arial macOS; nhãn nằm ngoài hình. Bản sao hoàn chỉnh ở `_review/020c/020c-v37-final.jpg`.

[verify-final.py](../../games/typing-defense/art-src/_review/020c/verify-final.py) lưu cách đo và dựng tờ xem; dùng đích mới và sẽ từ chối nếu chạy lại vào file đã có. Hồ sơ lượt kiểm đầu được giữ nguyên để truy vết; chỉ dùng các file có hậu tố `final` làm kết quả cuối. `roi-comparison.jpg` thử đầu có lỗi kế thừa gravity ở ô thứ hai, không dùng; đã có bản sửa riêng và tờ `roi-comparison-final.jpg` đúng tọa độ. Số đo từng hộp không bị lỗi này.

## 3. Việc chưa làm và chủ dự án cần xem

Không tạo lượt 4 vì đã đủ ba lượt và lượt 3 đạt tự chấm, không vùng phát sáng, đạt kiểm sáng. Không thay ảnh gốc, không sửa `ART_*`, không nhập vào game hoặc gửi Tripo. Không chạy Git, build/test game; không ghi vào phiếu 020, 020b, Tu Tiên hoặc mã game.

Claude cần chấm độc lập bản chọn trên tờ xem nhanh, đặc biệt lòng lò, sắc vàng đất và độ hợp bộ với Hầm Sâu. Chủ dự án cần xem ngoại lệ md5 do file thêm ngoài phiếu trước khi coi toàn bộ mục Kiểm là đạt. Chưa có kết quả duyệt của Claude trong phiếu này.
