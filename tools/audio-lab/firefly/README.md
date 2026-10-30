# Nhận âm Adobe Firefly

Phiếu 217 dựng bước nhận WAV của chủ dự án, tách và chọn take, dựng bằng `build`, rồi tạo bản nghe để duyệt. Công cụ không gắn âm vào game và không tự phát hành. Inbox chỉ đọc; `--inbox` và `--out` luôn phải chỉ rõ, không có mặc định trỏ tới `~/AudioLab`.

## Ba lệnh

Điều phối chạy ngoài sandbox, trong repo cha:

```bash
bash tools/audio-lab/run.sh firefly ingest --game dragon-hold --inbox ~/AudioLab/inbox/firefly --out ~/AudioLab/work/firefly
bash tools/audio-lab/run.sh firefly listen --game dragon-hold --out ~/AudioLab/work/firefly
bash tools/audio-lab/run.sh firefly status --game dragon-hold --inbox ~/AudioLab/inbox/firefly --out ~/AudioLab/work/firefly --json ~/AudioLab/work/firefly/status.json
```

Ba game: `dragon-hold`, `typing-defense`, `typing-survival`. Đặt nguồn ở `<inbox>/<game>/<id>/*.wav`. `ingest` và `listen` nhận `--id` để làm một id. `ingest --run NAME` đặt tên lần chạy; bỏ qua thì dùng ngày giờ tới microsecond. `--date YYYY-MM-DD` ghi đè ngày nguồn; mặc định lấy ngày địa phương từ mtime WAV. `--model` mặc định `Adobe Firefly Audio Model`; chỉ nhận họ model Adobe đã ghi trong `build/policy.py`.

`ingest` và `status` nhận `--list FILE`: định dạng thật của 212 là object `{game, rows: [{id, prompt, ...}]}`. Danh sách giới hạn id, nhưng mỗi id vẫn cần thẻ `specs/<game>/<id>.yaml`; không tự tạo thẻ hay suy từ mã game. Bản `typing-survival.json` hiện chưa có đường xuất. Nếu hàng có `export.path` hoặc `exportPath`, công cụ dùng đường đó; nếu chưa có thì dùng `firefly/<id>` và ghi rõ **đường tạm** trong `description`. Không dùng trường `inbox` trong danh sách làm đường ghi.

`status` liệt kê cả id chưa có WAV, số file inbox, lần chạy mới nhất, số take tìm thấy/qua/chọn, biến thể so với đích và min, cổng final, bản nghe. Id lạ và file không phải WAV được liệt kê riêng. `--json` phải nằm dưới `--out`.

## Tách, chấm và chọn take

| Tham số | Mặc định | Ý nghĩa |
|---|---|---|
| `--split auto\|onset\|whole` | `auto` | Vòng lặp hoặc `source_class: ambience/music` giữ cả file; còn lại tách theo đầu tiếng |
| `--threshold-db` | −35 | Ngưỡng hoạt động tương đối với đỉnh toàn file |
| `--min-gap-ms` | 150 | Khoảng lặng tối thiểu để mở take mới; tăng để gộp |
| `--pre-ms` | 5 | Giữ số mẫu trước đầu tiếng |
| `--tail-floor-db` | −60 | Điểm cắt đuôi tương đối với đỉnh take; giữ thêm một khung 1 ms |

Mặc định dựa trên giả định WAV Firefly 48 kHz stereo, khoảng 12 giây, nhiều cú như lô bàn phím 189. Chưa phải kết luận về mọi lô Firefly. Bộ phát hiện dùng khung đỉnh 1 ms, thêm phép dò năng lượng tăng gấp đôi trên nền đuôi còn chạy để nhận cú chồng. Cú sau đến khi đuôi trước chưa xuống 40 dB làm **cả hai** bị đánh dấu và loại khỏi chọn; giữ file để xem. Hình dạng phức tạp hoặc có phần tụ lực cần điều phối xem lại `takes.json` và chọn tham số phù hợp, không tự nới L1.

Mỗi take là lát PCM nguyên mẫu từ WAV gốc: giữ sample rate, số kênh, subtype và endian; không chuẩn hóa, fade hay lọc ở bước cắt. `critic.hygiene.gate(stage="raw")` loại các lỗi trong `UNFIXABLE`. File im lặng không có take và được ghi lý do cùng kết quả raw L1. File hỏng làm lần nhận lỗi.

Một bảng trọng số duy nhất (`pipeline.SCORE_WEIGHTS`): độ dài gần `duration.target_ms` 60%, khoảng trước onset sạch 20%, nền ở 20 ms cuối đuôi sạch 20%. Điểm thành phần nằm trong 0–1, cùng số dB và điểm tổng được lưu. Theo điểm giảm dần, chọn tới `variants.target`; tương quan chéo chuẩn hóa, mọi độ trễ và đảo cực, phải ≤0,95 với mọi take đã chọn (dùng hàm của 189). Thiếu thì dựng đúng số có; dưới `variants.min` ghi “dưới min”, trả mã 1. Không nhân bản hay đổi cao độ.

Công thức có một lớp `source.file`, dòng sổ đầy đủ, `vary.swap`, `swapMode: cycle`. Biến thể n dùng take được chọn thứ n, không lệch ngẫu nhiên cao độ hay mức. Nhóm, kênh, vòng lặp, thời lượng tối đa và mức đích lấy từ thẻ. Khi `loudness.proposal` là null (như `amb.forest`), dùng trường `loudness.file`; giới hạn đỉnh thiếu thì dùng −1 dBTP của build. Vòng lặp qua crossfade 50 ms của build; take gốc vẫn nguyên mẫu. OGG dùng quality 1,0 để giảm lệch LUFS sau giải mã (quality 0,6 của build mặc định có một ca fixture lệch 0,574 dB). Build có thể hạ mức cả id để giữ độ nhọn và giới hạn ép; xem `render.json.idLevel`.

Chạy final L1 trên từng master; master bị chặn được giữ để kiểm. Mã thoát `ingest`: 0 khi các id đạt cổng và đủ min; 1 khi bị chặn hoặc nguồn/dựng lỗi; 2 khi tham số sai. Id lạ và file không phải WAV chỉ được bỏ qua có lý do. Không có id hợp lệ thì báo cáo rỗng, không nhận là có âm đã được duyệt.

## Bố cục đầu ra

```text
<out>/<game>/ingest.json                   # hash + mtime inbox trước/sau, id bỏ qua
<out>/<game>/<id>/takes.json               # lần nhận gần nhất, tham số, điểm, raw/final L1
<out>/<game>/<id>/takes/<id>-tNN.wav        # lát nguyên mẫu, kể cả take bị loại
<out>/<game>/<id>/recipe.json
<out>/<game>/<id>/<run>/
  masters/<id>-vN.wav
  runtime/<export.path>-N.ogg
  render.json
  SOURCES.json
  licences.rows.jsonl
  manifest.fragment.json
  recipe.json
  firefly.json                            # bản chụp kết quả của lần chạy
<out>/listen/<game>/<id>-20s.mp3
<out>/listen/<game>/<id>-20s.json
```

Chạy lại cùng `--run` chỉ thay âm được ghi trong `firefly.json` của lần đó; không ghi đè thư mục lần chạy của công cụ khác. Tên run không được trùng thư mục `takes` hoặc `listen`. Không chấp nhận `--out` chứa symlink; inbox và out không được trùng hoặc chứa nhau. So sánh SHA-256 và mtime từng file trước/sau trong báo cáo nhận, kể cả file bị bỏ qua.

## Bản nghe 20 giây

`listen` dùng master của lần nhận gần nhất. Nếu id có chỗ trong kịch bản `context/`, dùng id đó làm focus, các chỗ khác im. Có thể thêm nhiều `--slot sid=FILE` để nghe cùng âm đã chọn khác. Dùng bộ dựng và bộ trộn hiện có, không gọi lệnh ghi giọng. Thiếu một giọng cần cho cảnh thì chuyển sang `sequence`; cảnh menu không dùng giọng vẫn dựng context được. Các âm phím tổng hợp có sẵn trong cảnh Wordwoven bị bỏ; nếu chỉ định `--slot key=FILE` thì đọc đúng file đó.

Chế độ `sequence` phát lần lượt các biến thể, thời gian từ đầu tiếng này đến đầu tiếng sau là `max(min_gap_ms, độ dài + 400 ms)`. Mức đặt ở giữa `loudness.mix_target.range`; trường range null thì lấy mức số trong proposal hoặc file của thẻ. Bản nghe dùng hàm MP3 192 kbps của 189 (mono), dài đúng 20 giây và fade 50 ms cuối. JSON ghi chế độ, kịch bản, focus, dòng thời gian, LUFS-I, LUFS-M max và đỉnh thật đo từ MP3 giải mã. Context lặp cảnh để đủ 20 giây, dùng biến thể đầu làm focus. Đây là bản nghe phục vụ duyệt, không phải chứng nhận thẩm mỹ hoặc quyền phát hành giọng cache.

## Giấy phép và bước duyệt

Lớp `LicenseRef-Adobe-Firefly-owner`, điều kiện `adobe-model`, là bản ghi quyết định của chủ dự án ngày 29/10/2026. Chỉ model Adobe; không model đối tác, không bán hoặc phát lại file thô/gói âm. Tên model hiện cho phép `Adobe Firefly Audio Model` và hậu tố phiên bản số (ví dụ `v2`, `2.1`), so khớp từ đầu và hết chuỗi. Claude cần xác nhận danh sách này.

Dòng sổ mang `origin: generated`, generator, model, author, prompt của danh sách nếu có, hash file gốc, mốc cắt, và `licenceCopy: licences/adobe-firefly-owner-2026-10-29.txt`. Bản gốc ở `firefly/licences/` được trỏ qua `source.licenceText` → `Loaded.copies` → `render.json.licenceCopies` → `ledger.copy_licence_texts` khi release. `ai_input_allowed: true` chỉ biểu thị chấm cục bộ trên máy; Claude xác nhận lại, không phải cho phép huấn luyện hay đưa file vào dịch vụ AI khác.

File giấy phép là **ghi chú của chủ dự án**, chưa phải bản lưu điều khoản Adobe. Codex làm offline; Claude bổ sung bản lưu có ngày, URL điều khoản và duyệt mã/lớp giấy phép trước commit. Chủ dự án nghe duyệt rồi điều phối mới gắn vào game. Công cụ này không tự release.

## Test offline

```bash
/Users/toandx/AudioLab/.venv/bin/python -B docs/codex-queue/217/run-tests.py
/Users/toandx/AudioLab/.venv/bin/python -B docs/codex-queue/217/run-tests.py firefly/tests build/tests/test_build_firefly_licence.py
/Users/toandx/AudioLab/.venv/bin/python -B docs/codex-queue/217/demo.py --voice-cache /đường/cache/giọng/có-sẵn
```

Wrapper chuyển pycache, numba, matplotlib, pytest và basetemp vào `tmp/firefly-ingest/`. Fixture sinh lúc chạy, không đưa âm vào Git. Test gọi trực tiếp `firefly.main(argv)`, không qua `run.sh`, và kiểm cả thư mục giả của `common.env` vẫn rỗng sau ba lệnh.
