# gen: thư viện CC0 (và sau này là lớp gọi mô hình)

Phần đã có: tải thư viện CC0 của mục 3.4 trong [kế hoạch](../../../docs/games/AUDIO_PIPELINE.md), lập chỉ mục và ghi sổ giấy phép. Lớp gọi Stable Audio 3 và ACE-Step **chưa có**, chờ bước 0 của chủ dự án.

## Lệnh

```bash
bash tools/audio-lab/run.sh gen.fetch_libraries              # Kenney (cả 10 gói âm), VCSL, VSCO-2-CE
bash tools/audio-lab/run.sh gen.fetch_libraries --only vcsl --extra "vcsl:Membranophones/Struck Membranophones/Timpani 1"
bash tools/audio-lab/run.sh gen.fetch_libraries --offline    # không mạng: kiểm lại file, ghi lại mã băm và sổ
bash tools/audio-lab/run.sh gen.index_library                # ~/AudioLab/libraries/index.json (chạy lại chỉ đọc file đổi)
bash tools/audio-lab/run.sh gen.index_library --verify-pitch # đo f0 từng mẫu có cao độ (khoảng 40 s)
bash tools/audio-lab/run.sh gen.index_library --summary      # bảng nhạc cụ
bash tools/audio-lab/run.sh gen.licence_lines <báo cáo render .json | đường dẫn file>   # dòng licences.jsonl
```

Chạy lại bao nhiêu lần cũng được. Lệnh tải bị ngắt giữa chừng thì chạy lại: zip tải tiếp bằng `Range`, git tải nốt các blob còn thiếu, file đã giải nén đúng CRC thì giữ nguyên.

## Nguồn đã ghim

| Thư viện | Lấy gì | Ghim | Kiểm giấy phép |
|---|---|---|---|
| Kenney | Cả 10 gói âm trên `kenney.nl/assets/category:Audio` | URL zip trên trang và SHA-256 của zip | Trang phải có dòng License trỏ tới CC0 1.0. `License.txt` trong zip phải ghi CC0 |
| VCSL | Dan Tranh, Folk Harp, Gong 1, Gong 2, Slit Drum, Woodblock, Anvil, Brake Drum, Hand Chimes, Tubular Bells 1 và 2, Frame Drum | `master` `c1ea7bcc3c73…`, SFZ `sfz` `dfcf4a491877…` | File `LICENSE` của kho là CC0 1.0 |
| VSCO-2-CE | Cello Section, Harp, Flute, F Horn, Tenor Trombone, Percussion | `master` `440300901dfe…`, SFZ `SFZ` `6dd651d55dde…` | File `LICENSE` của kho là CC0 1.0 |

- **Không bao giờ tải** VCSL "Hand Bells, Nepalese" và VSCO "NepaleseBells" (mục 8.2). Xin cả thư mục cha cũng bị từ chối.
- Brake Drum có trong mục 3.4 và được dùng cho `hit.tail`, `leak` (mục 8.3, 9), nên tải sẵn.
- VCSL và VSCO-2-CE tải bằng git: chỉ một commit (`--depth 1`), không tải blob ngoài thư mục đã chọn (sparse checkout, partial clone). Git chạy với cấu hình người dùng bị bỏ qua (`GIT_CONFIG_GLOBAL=/dev/null`), không hook, không credential, chỉ HTTPS.
- File `.sfz` chỉ là bảng nốt và cường độ (văn bản). Ta dùng chúng để xác nhận nốt của từng mẫu, không chạy gì từ đó.
- `Readme.txt` của VSCO-2-CE **xin** đừng bán lại mẫu thô và xin ghi công Versilian Studios/Sam Gossner và Ivy Audio/Simon Dalzell. Đây không phải điều kiện của CC0. Sổ ghi ở `attribution_requested`. Luật dự án vẫn là không bao giờ phát hành file thư viện thô.

## Dữ liệu ở `~/AudioLab/libraries`

| Đường dẫn | Có gì |
|---|---|
| `SOURCES.jsonl` | Sổ: mỗi gói Kenney hoặc mỗi thư mục nhạc cụ một dòng. Có `licence`, `licence_version`, `licence_url`, `downloaded`, `licence_copy`, `commercial_ok`, `attribution_required`, `ai_input_allowed`, `raw_redistribution_allowed`, `genai_preference`, `sha256` (zip, hoặc mã băm nội dung thư mục với git), `commit`, `version`, `url`, `page`, `verified` |
| `<thư viện>/LICENSE-<ngày>.txt` | Bản lưu giấy phép kèm ngày tải, commit hoặc mã băm zip, lời trên trang |
| `<thư viện>/CHECKSUMS.sha256` | SHA-256 của mọi file âm |
| `vcsl-sfz/`, `vsco2ce-sfz/` | Bảng SFZ của nhánh sfz |
| `index.json` | Chỉ mục mọi file âm (xem dưới) |
| `.sha256-cache.json` | Bộ nhớ đệm mã băm theo kích thước và thời gian sửa |

`index.json`: mỗi file có `file`, `library`, `pack`, `licence`, `sha256`, `duration`, `sample_rate`, `channels`, `frames`, `family` (ví dụ `impact/metal`, `ui/click`, `instrument/plucked-string`), `tags`, `instrument_id` (ví dụ `vcsl/dan-tranh.normal`), `kind` (`pitched`, `unpitched`, `sfx`, `music`, `voice`, `preview`), `key`. Mẫu nhạc cụ có thêm `note` (như tên file), `midi` và `note_spn` (cao độ thật, C4 = 60), `midi_source`, `dyn`, `vel_layer`, `rr`, `mic`, `sfz` và `f0` (khi chạy `--verify-pitch`: `hz`, `cents`, `octave_off`, `conf`, `coarse_cents`, `drift_cents`, `stable`, `method`). Phần `instruments` tóm tắt quãng, số lớp cường độ, round robin, kiểm f0.

## Điều đã kiểm trên dữ liệu thật (23/10/2026)

**Đo cao độ** (`--verify-pitch`): pYIN tìm quãng tám, rồi lấy đỉnh phổ (FFT) trong khoảng ±150 cent quanh phím của bảng SFZ, ở tần số lấy mẫu gốc, trong cửa sổ 60–660 ms sau đầu tiếng. Mỗi mẫu ghi `cents`, `coarse_cents` (pYIN), `drift_cents` (độ trôi giữa hai nửa cửa sổ), `stable` (trôi ≤ 10 cent) và `method`. Đổi phương pháp thì lần chạy sau tự đo lại. Bản đo cũ chỉ dùng pYIN/YIN đã đọc sai thanh gõ (glockenspiel G4: −47 cent, thật ra +8 cent), nên đã thay.

- **Tên nốt của VCSL lệch một quãng tám** ở Dan Tranh, Folk Harp, Hand Chimes, Tubular Bells 1. Ví dụ file đàn tranh `B1_f_1.wav` là MIDI 47 (B2). Bảng SFZ của chính VCSL và phép đo f0 đều cho kết quả này (48/48 mẫu đàn tranh). Vì vậy đàn tranh VCSL thật ra phủ **B2–B5**, không phải B1–B4 như mục 3.2 và 8.2 đang ghi. `word-hit` ở C5–C6 chỉ cần dời tối đa 1–2 bán cung. Đề xuất hạ một quãng tám ở mục 8.2 không còn cần thiết. Chủ dự án vẫn phải nghe duyệt.
- **Đàn tranh Normal:** 20/48 mẫu lệch quá 10 cent, từ −26 đến +58 cent (C#3 `f`/`ff` cao khoảng +58 cent). Tiếng gảy mạnh ở quãng thấp trôi cao độ tới 20–40 cent. Bộ phát mẫu tự bù (`--tuning auto`, mặc định). Sau khi bù, 78 nốt C4–D6 × 3 lớp cường độ đo lại bằng hai cách độc lập (đỉnh FFT và YIN): không nốt nào lệch quá 10 cent, trung vị 0,8 và 3,6 cent. Riêng `F#2_ff_1.wav` trôi 42 cent nên không bù; `sampler info` có ghi chú.
- **Folk Harp:** bảng SFZ có `tune` cho 46 mẫu, nhưng nhiều mẫu vốn đã đúng cao độ, nên `tune` lại làm lệch (ví dụ D6 thành −15 cent). Ở `auto`, số đo f0 tin được thay cho `tune` của SFZ (40 mẫu đổi giá trị). Kết quả: 81 nốt C4–D6 không nốt nào lệch quá 10 cent (với `--tuning sfz`: 6 nốt). Hand Chimes có `tune` ở 15 mẫu, 12 mẫu được thay: 111 nốt C4–C7 không nốt nào lệch quá 10 cent theo FFT (với `sfz`: 12 nốt).
- **Glockenspiel và xylophone của VSCO-2-CE** kêu cao hơn bảng SFZ đúng một quãng tám (6/6 và 8/8 mẫu), và cao thêm 8–24 cent. Index ghi `octave_fix: 12`; bộ phát mẫu sửa quãng tám rồi bù cent. Sau khi bù, đỉnh FFT lệch 0 cent.
- **Tubular Bells 1 và 2** không đo được cao độ tin cậy (chuông có cao độ ảo, không trùng họa âm nào; số đo từ −320 đến +280 cent), nên không tự chỉnh. Chỉ dùng sau khi chủ dự án nghe.
- Cello pizzicato (cả dàn) cho hai cách đo khác nhau tới 20 cent, vì nhiều cây đàn lệch nhau. Không coi là lỗi của bộ phát mẫu.
