# Phiếu 218 · Mở rộng bộ tiếng phím Firefly

Ngày 30/10/2026 · Mac mini M4. **Bàn giao 32 bộ đạt từ 6 điểm; không đạt mục tiêu 80 bộ.** Mỗi bộ có **70–80 phím thường và 8 phím cách**, preview 1 giây; đủ manifest, danh mục và 7 bài nghe. Dừng ở số đạt cổng, không thêm bộ gần trùng để đủ 80. Đây là kết quả tìm kiếm theo các ngưỡng bên dưới, không phải chứng minh rằng mọi cách phân cụm khác đều không thể đạt 80.

**Ngoại lệ tên file:** mã `keyboardFiles()` đang có trong `shared/game-kit/feedback/typing-fx/audio.ts` thực tế dùng `\d{2}`, không phải số chữ số bất kỳ như giả định trong phiếu. Vì cấm sửa `shared/**`, bản giao dùng `key-01.ogg`…`key-80.ogg`, `space-01.ogg`…`space-08.ogg`. Đã gửi lựa chọn cho chủ dự án trong phiên làm việc; chưa nhận được trả lời nên chọn cách tương thích hiện tại. Không tạo alias âm trùng. Nếu muốn tên `key-001.ogg`, phiếu 219 phải đổi bộ đọc và đổi tên đồng bộ. Test chạy nguyên hàm hiện hành trên đủ 32 manifest, không chỉ bản mô phỏng Python.

## Bản giao và nghe thử

- [Danh mục gốc](../../tmp/keys-firefly/staging-v2/keys-firefly/keys-manifest.json): `tmp/keys-firefly/staging-v2/keys-firefly/`. Có **2.652 biến thể OGG** (2.396 phím, 256 cách), **32 preview**, 33 manifest; không có WAV. OGG Vorbis q0,6, mono 48 kHz.
- [Deep · 6 giây](../../tmp/keys-firefly/listen-v2/so-sanh-deep.mp3), [Warm · 12 giây](../../tmp/keys-firefly/listen-v2/so-sanh-warm.mp3), [Rounded · 2 giây](../../tmp/keys-firefly/listen-v2/so-sanh-rounded.mp3), [Solid · 4 giây](../../tmp/keys-firefly/listen-v2/so-sanh-solid.mp3), [Crisp · 12 giây](../../tmp/keys-firefly/listen-v2/so-sanh-crisp.mp3), [Clear · 8 giây](../../tmp/keys-firefly/listen-v2/so-sanh-clear.mp3), [Bright Clack · 20 giây](../../tmp/keys-firefly/listen-v2/so-sanh-bright-clack.mp3). Mỗi bộ 2 giây, đúng thứ tự danh mục; MP3 192 kbps, tổng 64 giây.
- Tổng thư mục bàn giao **19.397.442 byte = 19,40 MB**, trong đó OGG **14,10 MB**, phần còn lại chủ yếu là manifest có nguồn và số đo. Bài nghe **1,55 MB**; cộng hai nơi **20,94 MB**, dưới 70 MB. Cache phân tích trong `tmp/keys-firefly/build-v2-cache/` không thuộc bản giao.

Giữ nguyên 7 id `deep`, `warm`, `rounded`, `solid`, `crisp`, `clear`, `bright-clack` cho bộ điểm cao nhất của từng họ; mặc định Bright Clack và save cũ vẫn trỏ được. Danh mục theo họ trầm → sáng; trong họ theo điểm giảm dần. Họ là so sánh cả phổ với mốc 189, không chỉ xếp trọng tâm phổ, nên trọng tâm từng bộ có thể chồng nhau giữa hai họ.

## Vì sao chỉ có 32 bộ

Khảo sát hiện có thực tế chứa **22.076 hàng cú gõ, 7.303 hàng được detector đánh dấu sạch**, khác số ước lượng 23.900/8.300 trong phiếu. Nguồn vẫn đủ **408 WAV, 9 thư mục**. Đã kiểm SHA-256 toàn bộ nguồn trước/sau: **408/408 không đổi**, không sửa tên hay vị trí. [Bảng băm](218/source-hashes.json).

Sau cổng nguồn còn **3.853 cú**. Loại 17.538 hàng ở luật khảo sát, 15 hàng không khớp phát hiện lại, 661 hàng có nền tại mức bàn giao trên −60 dBFS, 9 hàng thiếu dự phòng đỉnh. [Chi tiết](218/preparation.json). Nới attack/main lên tối đa 40 ms, nhận tick/rattle nhỏ; không còn luật loại mọi thành phần phụ của 189. Vẫn yêu cầu detector xác nhận đã tắt trước cú kế, không clip (kiểm cả hai kênh thô), cửa sổ 30–240 ms, cú kế cách ít nhất cửa sổ + 2 ms, T60 đo được không quá 160 ms. Không cắt cụt thân dài để ép lọt giới hạn.

Thử **3.773 tâm**: trung vị từng take, tối đa ba cụm k-means có seed cố định trong take đủ mẫu, và các cú thật cách tâm đã có ít nhất 0,3. Với mỗi tâm, chỉ lấy cú trong bán kính 1,35 và trọng tâm lệch không quá 0,65 octave; lấy tối đa tám take. Ưu tiên cùng thư mục nếu đủ nguồn gần để lấy ít nhất 80 ứng viên phím; nếu thiếu, mở sang các take của thư mục khác vẫn ở trong bán kính. Trong tập hợp đó ưu tiên take có nhiều cú hợp âm sắc rồi xét khoảng cách.

| Kết quả thử tâm | Số |
|---|---:|
| Không đủ 70 phím trong tám take | 2.366 |
| Thiếu phím sau khi bỏ tương quan cao/dành phím cách | 383 |
| Không đủ sáu phím cách | 3 |
| Phím cách không còn trầm/dài sau khi chọn phím | 2 |
| Điểm dưới 6 | 529 |
| Đủ số lượng và điểm trước loại gần trùng | 490 |
| Loại vì gần một bộ có điểm cao hơn | 458 |
| Bàn giao | **32** |

Chọn bộ điểm cao trước; một bộ mới phải cách **mọi** bộ đã nhận ít nhất 0,52 trước codec (0,02 dự phòng). Khoảng cách công bố cho OGG cuối phải ≥0,50. Không gộp bắc cầu. Không hạ ngưỡng khoảng cách để đẩy con số lên 80. Kết quả còn thiếu **48 bộ** theo cách tìm này.

Cả 32 bộ dùng đúng **8 take/bộ**, thuộc 3–7 thư mục. Nguồn của từng file có trong manifest, danh sách take trong [selection.json](218/selection.json). Các bộ có thể dùng lại cú của nhau: 2.652 file biến thể dùng **940 cú nguồn khác nhau**, một cú xuất hiện nhiều nhất ở **11 bộ**; không nhân bản trong cùng bộ. [Thống kê dùng lại](218/source-reuse.json). Vì vậy 32 là số tổ hợp âm sắc qua ngưỡng, không phải 32 bàn phím vật lý đã được xác nhận hay 2.652 cú nguồn riêng biệt.

## Khoảng cách và công thức điểm

Vector 9 chiều của phím gồm `log2(trọng tâm Hz)/0,25`, sáu năng lượng dải chuẩn hóa chia 3 dB, `log2(T60 ms)/0,5`, `log2(độ dài ms)/0,5`. Sáu dải của khảo sát: 80–150, 150–400, 400–2.000, 2.000–4.000, 4.000–8.000, 8.000 Hz trở lên. T60 không ước lượng được dùng giá trị quy ước 40 ms cho vector, không giả ghi là số đo. Khoảng cách là căn trung bình bình phương chênh chín chiều; tâm bộ là trung vị từng chiều của phím thường. Thang đo cố định, không fit lại theo lô để đạt 80.

Gán họ theo mốc phổ 7 bộ 189, so khoảng cách trên bảy chiều phổ đầu. Tâm OGG cuối đo lại từ âm giải mã; T60 vẫn là phép đo nguồn. Khoảng cách nhỏ nhất **0,503556**, cặp `bright-clack` / `bright-clack-pebble`. [Đủ 496 cặp](218/timbre-distances.csv). Đây là tiêu chí phân biệt bằng máy; chưa có kết luận nghe rằng mọi cặp đều khác rõ.

Với `clamp(x) = min(1, max(0, x))`, lấy trung bình trên phím + cách trừ thành phần đều chỉ xét phím thường:

- **Sạch C:** trung bình `clamp(1 − max(0, attack_ms − 3)/15)`.
- **Đều E:** `clamp(1 − trung bình khoảng cách phím đến tâm bộ / 2)`.
- **Lặp R:** `clamp((0,95 − tương quan cặp lớn nhất)/0,55)`; tương quan chuẩn hóa mọi độ trễ, lấy trị tuyệt đối để bắt cả đảo cực.
- **Nền N:** trung bình `clamp((−nền_dBFS − 60)/20)`, nền nguồn trước gate ở mức −36 LUFS-M chung.
- **Đuôi T:** trung bình `clamp(1 − max(0, T60_ms − 60)/160)`. Không ước lượng được T60 dùng 80 ms để chấm thận trọng.

**Điểm = 10 × (0,25C + 0,25E + 0,20R + 0,15N + 0,15T)**. Các cổng clip/chồng tiếng/nền/đuôi phải đạt trước khi chấm; điểm cao không bù cho lỗi cấm. Điểm lấy từ ứng viên xử lý trước codec; bản OGG kiểm riêng mọi cổng cuối. Điểm **6,0216–6,9508**, trung vị **6,1957**; cả 32 bộ trong khoảng [6,7), không có bộ dưới 6. Đây là điểm ước lượng từ số đo, chưa hiệu chỉnh theo điểm nghe của chủ dự án.

## Danh sách

Phân bố: **Deep 3 · Warm 6 · Rounded 1 · Solid 2 · Crisp 6 · Clear 4 · Bright Clack 10**. Phím thường nhỏ nhất/trung vị/lớn nhất **70 / 74,5 / 80**; phím cách **8 / 8 / 8**.

| Tên / id | Điểm | Phím + cách | Cách mượn | Tương quan lớn nhất OGG |
|---|---:|---:|---:|---:|
| Deep Velvet · `deep` | 6.3729 | 72 + 8 | 3 | 0.8148 |
| Deep Amber · `deep-amber` | 6.2501 | 74 + 8 | 7 | 0.8285 |
| Deep Cedar · `deep-cedar` | 6.1877 | 77 + 8 | 3 | 0.8174 |
| Warm Velvet · `warm` | 6.2269 | 80 + 8 | 4 | 0.8864 |
| Warm Amber · `warm-amber` | 6.2037 | 70 + 8 | 5 | 0.8313 |
| Warm Cedar · `warm-cedar` | 6.1645 | 78 + 8 | 8 | 0.8474 |
| Warm Pebble · `warm-pebble` | 6.1575 | 76 + 8 | 7 | 0.8174 |
| Warm Slate · `warm-slate` | 6.0783 | 73 + 8 | 7 | 0.8850 |
| Warm Silk · `warm-silk` | 6.0285 | 80 + 8 | 4 | 0.8622 |
| Rounded Velvet · `rounded` | 6.1582 | 80 + 8 | 1 | 0.8852 |
| Solid Velvet · `solid` | 6.9508 | 71 + 8 | 8 | 0.6969 |
| Solid Amber · `solid-amber` | 6.3993 | 79 + 8 | 7 | 0.8148 |
| Crisp Velvet · `crisp` | 6.5395 | 74 + 8 | 2 | 0.8188 |
| Crisp Amber · `crisp-amber` | 6.5043 | 70 + 8 | 5 | 0.8293 |
| Crisp Cedar · `crisp-cedar` | 6.3210 | 71 + 8 | 8 | 0.8293 |
| Crisp Pebble · `crisp-pebble` | 6.2789 | 75 + 8 | 5 | 0.8068 |
| Crisp Slate · `crisp-slate` | 6.0655 | 70 + 8 | 5 | 0.8254 |
| Crisp Silk · `crisp-silk` | 6.0566 | 80 + 8 | 7 | 0.8670 |
| Clear Velvet · `clear` | 6.7535 | 70 + 8 | 8 | 0.7122 |
| Clear Amber · `clear-amber` | 6.4944 | 72 + 8 | 7 | 0.8173 |
| Clear Cedar · `clear-cedar` | 6.2836 | 70 + 8 | 8 | 0.8188 |
| Clear Pebble · `clear-pebble` | 6.0930 | 75 + 8 | 8 | 0.8646 |
| Bright Clack Velvet · `bright-clack` | 6.3979 | 80 + 8 | 4 | 0.8930 |
| Bright Clack Amber · `bright-clack-amber` | 6.3863 | 80 + 8 | 7 | 0.8646 |
| Bright Clack Cedar · `bright-clack-cedar` | 6.2242 | 70 + 8 | 4 | 0.8378 |
| Bright Clack Pebble · `bright-clack-pebble` | 6.1822 | 73 + 8 | 3 | 0.8926 |
| Bright Clack Slate · `bright-clack-slate` | 6.1392 | 70 + 8 | 5 | 0.8777 |
| Bright Clack Silk · `bright-clack-silk` | 6.1220 | 78 + 8 | 4 | 0.8408 |
| Bright Clack Copper · `bright-clack-copper` | 6.0750 | 80 + 8 | 2 | 0.8777 |
| Bright Clack Walnut · `bright-clack-walnut` | 6.0586 | 77 + 8 | 7 | 0.8651 |
| Bright Clack Moss · `bright-clack-moss` | 6.0403 | 71 + 8 | 2 | 0.8408 |
| Bright Clack Ember · `bright-clack-ember` | 6.0216 | 80 + 8 | 7 | 0.8467 |

Có **84 cú space-like theo số đo, 172 cú mượn**; nguồn không ghi phím vật lý nên không khẳng định 84 cú đó là phím cách thật. Mỗi cú cách đều có trọng tâm <95% trung vị phím và độ dài >105% trung vị phím lúc chọn; kiểm OGG cuối vẫn trầm và dài hơn. Cú mượn ưu tiên trầm/dài trong chính tám take của bộ, không đổi cao độ hay kéo dài âm.

Danh sách từ mô tả tiếng Anh cố định trong mã (không tên hãng): Velvet, Amber, Cedar, Pebble, Slate, Silk, Copper, Walnut, Moss, Ember, Marble, Oak, Pearl, Stone, Linen, Maple, Birch, Rain, Brook, Reed, Quartz, Breeze, Willow, Ash, Satin, Clay, Flint, Crystal, Silver, Ivory, Dune, Fern, Grove, Meadow, River, Cove, Frost, Glade, Dawn, Drift, Cloud, Mist, Shell, Willowcrest, Opal, Jasper, Topaz, Garnet, Onyx, Coral, Bronze, Steel, Granite, Basalt, Sand, Laurel, Aspen, Hazel, Acorn, Pine, Spruce, Juniper, Olive, Almond, Chestnut, Cinder, Glow, Spark, Ripple, Wave, Cascade, Dew, Snow, Ice, Winter, Spring, Summer, Autumn, Twilight, Moonlight, Starlight, Sunlight, Halo, Beam, Gleam, Glint, Shimmer, Chime, Echo, Whisper, Murmur, Rustle, Patter, Cadence, Tempo, Rhythm, Pulse, Orbit, Prism, Facet, Lattice, Mosaic, Canvas, Loom, Thread, Weave, Ribbon. Chỉ dùng số từ cần thiết, kết hợp với họ để tên không trùng.

## Xử lý và kiểm cuối

Giữ chuỗi nhẹ 189: kiểm mất khi gập mono >1 dB thì chọn kênh SNR tốt hơn; lọc dưới âm 30 Hz bậc 2 pha không trên toàn take; cắt theo detector; mặt nạ mềm lặng hóa nền, fade-in ≤1 ms, fade-out tối đa 12 ms; thêm 20 ms lặng cho đuôi codec. Không tổng hợp, EQ tạo màu, đổi cao độ, kéo thời gian hoặc nén.

Mức chung **−36,0 LUFS-M max** (cửa sổ 400 ms, thêm lặng nếu clip ngắn). Cổng ứng viên giữ dự phòng −1,8 dBTP trước codec; loại cú không lên được mức chung, không giảm mức riêng cho cú đó. Đỉnh thật đo oversample ×4 như 189.

Nền nguồn dùng phân vị 10 của RMS cửa sổ 5 ms, bước 1 ms, trong đoạn trước/sau cú; tránh coi toàn đuôi đang tắt của cú trước là nền. Đây là ước lượng nền, không phải phép tách nhiễu hoàn hảo. Nền bàn giao là số lớn nhất giữa 5 ms cuối và lõi các vùng lặng ≥10 ms, bỏ 3 ms mỗi mép chuyển tiếp. Không dùng thân đang kêu làm nền. Manifest giữ tọa độ vùng đo và nguồn trước gate.

| Số đo OGG giải mã | Phím thường | Phím cách |
|---|---:|---:|
| Độ dài (ms) | 50,00–177,25 | 70,50–242,00 |
| Trước tiếng, ngưỡng −40 dB so đỉnh (ms) | 0,4167–2,7708 | 0,4167–1,6667 |
| LUFS-M max | −36,3139…−35,7977 | −36,2235…−35,8573 |
| Đỉnh thật lớn nhất (dBTP) | −2,3605 | −4,0319 |
| Nền lớn nhất (dBFS) | −65,6705 | −72,8488 |

Lệch LUFS lớn nhất trong bộ **0,4677 dB**, thấp hơn 1,5 dB. Tương quan cặp lớn nhất trong bộ **0,893032**, thấp hơn 0,95, kiểm mọi cặp OGG đã giải mã. Nền nguồn trước gate cao nhất **−60,009881 dBFS** ở mức chung. [2.652 hàng đo file](218/file-metrics.csv), [32 hàng đo bộ](218/set-metrics.csv), [tổng kiểm JSON](218/verification.json).

**32/32 preview = 1.000,0 ms**, đúng dung sai ±10 ms. Sáu phím rồi một cách, 100 WPM, nhịp ±3%, mức ±8%, xoay biến thể, fade cuối 50 ms. LUFS-M của câu **−30,3667…−29,8780**, đỉnh thật cao nhất **−2,95 dBTP**, nền 5 ms cuối **−200 dBFS** (sàn đồng hồ). Câu to hơn một cú vì cửa sổ chứa nhiều cú; không cân lại mức câu. [Bảng preview](218/preview-metrics.csv). MP3 mỗi họ đã giải mã kiểm đủ 2 giây/bộ.

## Mã, test và chạy lại

- Thêm `tools/audio-lab/keys/firefly_v2.py`, `firefly_v2_delivery.py`, `tests/test_firefly_v2.py`; thêm nhánh CLI nhỏ vào `firefly.py`. Không sửa bộ dựng 189, `codex182.py`, test cũ, cấu hình chung hay công việc audio-lab khác.
- Giữ cache ứng viên ở `tmp/keys-firefly/build-v2-cache/`, khóa theo hash nguồn và phần mã xử lý liên quan. Cổng băm toàn bộ nguồn vẫn chạy trước/sau build, không bỏ qua vì có cache.
- Test gồm cổng nguồn, bảo vệ đường dẫn/symlink, tương quan trễ/đảo cực, thang khoảng cách, điểm, tên/id/thứ tự, CLI và toàn bộ media thật. Chạy nguyên `keyboardFiles()` hiện hành qua Node strip types trên cả 32 manifest.

```bash
bash tools/audio-lab/run.sh keys firefly build-v2
bash tools/audio-lab/run.sh docs/codex-queue/218/run-tests.py
```

Lệnh dựng mặc định ghi đúng staging/listen/evidence của phiếu trong repo; có `--src`, `--survey`, `--out`, `--work`, `--evidence`, `--prepare-only`. Lệnh `keys firefly build` của 189 giữ nguyên. **Test keys cuối: 57 qua, 0 lỗi, 0 bỏ qua; 5 subtest qua**, gồm kiểm lại 189 và test có sẵn. [Log](218/tests-keys.txt). Không chạy build/test game.

[`git status --short -uall` toàn repo](218/git-status-full.txt) còn công việc sẵn có/đồng thời của agent khác, kể cả WAV nguồn dưới `typing-mp3/` đã hiện ngay lúc bắt đầu; không sửa, xóa hay đưa chúng vào Git. [Status phạm vi phiếu](218/git-status-task.txt) chỉ mã, test, tài liệu. Đầu ra media trong `tmp/` được `git check-ignore` xác nhận bỏ qua. Không chạy lệnh Git có ghi, tải mạng hay model tạo âm. Không chạm `games/**`, `shared/**`, Tu Tiên. Không tạo ảnh nên không có prompt ảnh.

## Chủ dự án cần xem

Nghe bảy file so sánh, nhất là khác biệt giữa các bộ trong một họ và phím cách mượn. Bản xử lý cuối **chưa được tôi nghe trực tiếp, chưa có phê duyệt nghe của chủ dự án**; điểm máy không thay thế bước đó. Phiếu 219 nên nhận **32 bộ thực tế**, không trình bày thành 80. Muốn thêm bộ cần nguồn có âm sắc/cú tách sạch đa dạng hơn, hoặc một quyết định mới về ngưỡng phân biệt; không sinh âm hay hạ cổng cấm trong phiếu này. Việc gắn vào ba game và Monkeytype được để lại đúng phạm vi phiếu sau.
