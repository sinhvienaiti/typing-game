# gen: thư viện CC0, lớp gọi Stable Audio 3 và chuỗi xử lý đầu ra mô hình

Phần đã có: tải thư viện CC0 của mục 3.4 trong [kế hoạch](../../../docs/games/AUDIO_PIPELINE.md), lập chỉ mục và ghi sổ giấy phép; lớp gọi Stable Audio 3 (`sa3.py`, chủ dự án đã xong bước 0 ngày 23/10/2026) và chuỗi xử lý đầu ra mô hình thành ứng viên nghe (`process.py`). ACE-Step **chưa có**, chờ chủ dự án chấp nhận giấy phép.

## Stable Audio 3 (`sa3.py`)

```bash
R=tools/audio-lab/run.sh
bash $R sa3 plan --spec tools/audio-lab/specs/dragon-hold/amb.forest.yaml --variant E --seeds 2001-2006   # in job, không chạy
bash $R sa3 run  --spec tools/audio-lab/specs/dragon-hold/amb.forest.yaml --variant E --seeds 2001-2006 --run sa3-r2
bash $R sa3 run  --spec .../enemy.quadruped.howl.yaml --variant A --seconds 3 --tag-seconds --run sa3-r2   # tên ...__A3s__s1001
```

- **Prompt lấy từ thẻ spec:** `prompt.variants` (mỗi chuỗi dạng `"E: văn bản"` giữ khóa E; chuỗi không khóa được đặt A, B, C… theo thứ tự); thẻ không có biến thể thì dùng `prompt.text`. `--prompt KHÓA=văn bản` thêm prompt tạm, không ghi vào thẻ.
- **Prompt bị cấm (DECISIONS Q2, TK 22.1):** với mọi id của Lời Gọi, `build_job` từ chối prompt có "tok", "tốc", "hollow tube", "temple block", "wooden fish", "mõ", và từ chối prompt B, D của `call-chop` (tiếng gõ rỗng, cao giống mõ). Bảng ở `FORBIDDEN_TERMS`, `FORBIDDEN_KEYS` trong `sa3.py`.
- **Chữ cấm Q6 (DECISIONS Q6, 24/10/2026), cả ba game:** `build_job` từ chối prompt có puff, pop, poof, plop, balloon, whoomp (cả whoomph, woomp, fwoomp), thoomp, boing, bonk, toy, cartoon, retro, 8-bit, chiptune, "bụp", "thụp" (`Q6_TERMS`; poof, plop, các cách viết whoomp và thoomp thêm ngày 25/10 theo hai gói prompt `04-audio*.md` của Lời Gọi). "oomph" (nghĩa "có lực") không bị chặn. "thump", "thud" đứng riêng cũng bị cấm, nhưng cần ngữ cảnh (lớp trầm dưới thân và đuôi thì được), nên lượt soát Q6 đọc chúng, không phải danh sách chữ. Test `tests/test_sa3_q6.py` chỉ cần PyYAML: `numpy`, `soundfile` chỉ được nạp trong các hàm đọc file âm.
- **Độ dài tạo chỉ 1, 2, 3, 10 s.** Bản cài này cho ra nhiễu toàn thang ở 0,5 s và 1,5 s (cả CLI `./sa3`). Không ghi `--seconds` thì lấy mức nhỏ nhất chứa được `duration.max_ms` của thẻ cộng khoảng dư (âm ngắn 1 s, tiếng tru 1,1 s → 2 s, nền 6 s → 10 s), rồi cắt sau.
- **cfg mặc định 1,0** (mục 5.1): negative prompt khi đó không có tác dụng, chỉ được ghi vào hồ sơ (`negative_prompt_written_not_applied`). Bản thử cfg 3 cộng negative không cho kết quả tốt hơn.
- **Chạy:** `~/AudioLab/models/sa3-meta/tools/batch_run.sh JOB OUTDIR` (mô hình nằm sẵn trong một tiến trình, giống từng byte với CLI), Hugging Face offline, không token. Mỗi lần một mô hình nặng: không chạy cùng lúc với bộ phê bình.
- **Mỗi ứng viên** trong `~/AudioLab/work/<game>/<id>/<run>/raw/`: `<tên>.wav` (16-bit như CLI, bộ ghi cắt cứng phần |x| > 1), `<tên>.f32.wav` (bản float chưa bị cắt: cổng L1 đọc bản này) và `<tên>.json` (`audiolab.sa3.candidate/1`: prompt, seed, steps, cfg, độ dài, mô hình kèm revision và SHA-256 trọng số, SHA-256 hai file, số đo thô như số đoạn bộ ghi cắt, tương quan stereo, dòng sổ). Ứng viên đã có thì bỏ qua. Báo cáo lô: `raw/_batch-report-<giờ>.json`.
- **Sổ giấy phép:** `<run>/licences.rows.jsonl` nhận dòng `model` (vai trò `generate`, giấy phép `LicenseRef-Stability-Community-2024`) và hai dòng `acceptance` (bản đăng ký Stability, điều khoản Gemma của bộ mã hóa chữ T5Gemma) qua `build.ledger.append_rows`. Lớp `gen` của công thức ghi `"record": "<tên>.json"`: `build render` kiểm SHA-256 của file với hồ sơ rồi mang các dòng đó và bản giấy phép có ngày vào lần dựng, nên `licence-check` thấy cả dòng mô hình lẫn bản đăng ký (mục 10.7). Hồ sơ của bản thử lô 0b (cũ hơn) không có dòng sổ: bộ dựng tự lập lại từ `install-record.json`.

## Xử lý đầu ra mô hình (`process.py`)

```bash
bash $R process ~/AudioLab/work/<game>/<id>/sa3-trial/raw ~/AudioLab/work/<game>/<id>/sa3-r2/raw \
    --spec tools/audio-lab/specs/<game>/<id>.yaml --out ~/AudioLab/work/<game>/<id>/sa3-r2/processed [--notch-comb] [--whole] [--two-part]
```

Đọc bản float, đổi sang 48 kHz (soxr VHQ), lọc cao 35 Hz, rồi:

| Bước | Âm ngắn | Nền lặp |
|---|---|---|
| Đầu tiếng | Mỗi âm là một đoạn mức 10 ms vượt (đỉnh − 30 dB; sinh vật − 40 dB). **Đầu tiếng thật** là điểm bắt đầu đoạn đó, tìm cùng một cách cho mọi cửa sổ, kể cả cửa sổ đầu tiên, không giới hạn lùi; đầu file cũng tính. Đoạn bắt đầu ngay sau đuôi của âm trước (28 ms trước nó trên −30 dB so với đỉnh) là "cắt ngang", không bao giờ làm điểm đầu. Không còn đầu tiếng thật thì ứng viên vào thư mục `<out>-rejected` kèm lý do. **Đầu file chỉ được tin khi có bằng chứng** (vòng soát 2): 1,5 ms đầu thấp hơn đỉnh của âm ≥ 30 dB, hoặc đỉnh dải trên 2 kHz nằm trong 5 ms đầu (âm ngắn; sinh vật chỉ dùng điều kiện mức). Không đạt thì vẫn giữ để chấm máy nhưng ghi `"onset_verified": false` và `onset_note` "đầu tiếng chưa xác minh"; bộ chọn ưu tiên cửa sổ có bằng chứng, và `batch0b` không đưa bản đó vào phiên nghe | — |
| Cửa sổ | Độ dài tự nhiên (tới −40 dB), chặn ở `max_ms` của thẻ. Sinh vật (hoặc `--whole`) giữ trọn tiếng gọi, kể cả đoạn lớn dần. `--two-part` (âm hai nhịp có chủ ý như `word.load` "cạch-chắc"): nhịp nhẹ 20–90 ms trước nhịp chính được giữ và ghi vào `two_part`, không bị loại là gõ hai lần. Không bao giờ qua âm sau; trong một đoạn, phát thứ hai cách ≥ 30 ms, to ngang phát đầu (trong 6 dB) sau một chỗ trũng ≥ 12 dB **kéo dài ≥ 8 ms** thì cửa sổ dừng ở chỗ trũng (loạt đạn giữ phát đầu; chỗ chập chờn ngắn của một tiếng phụt lửa không tính) | Tìm điểm bắt đầu trên lưới 25 ms: khớp mức và màu hai đầu, đều mức, không có tiếng gõ hay chiêm chiếp bên trong, mối nối 50 ms đạt |
| Loại bỏ | Vào `<out>-rejected` kèm lý do: không có đầu tiếng thật; phát đầu ngắn hơn `min_ms` của thẻ vì phát sau đến sớm; **gõ hai lần** (một tiếng nhỏ hơn ≥ 6 dB, rồi chỗ trũng ≥ 12 dB dưới tiếng chính kéo dài ≥ 8 ms, rồi tiếng chính sau ≥ 20 ms: cắt vào tiếng chính sẽ cắt giữa đuôi tiếng đầu). Tiếng nổ giòn rồi tiếng ùm 14–19 ms sau của súng không phải gõ hai lần. Chạy lại thì một ứng viên chuyển thư mục, không bao giờ nằm ở cả hai | Mối nối vẫn trượt sau 12 lần thử |
| Đuôi | **Mũ hàm mũ** (`build.dsp.exp_cap_tail`, cũng là `chain.tail.shape: "exp"` của công thức): từ điểm gối, một đường thẳng theo dB (tức tắt dần theo hàm mũ) đi tới −60 dB ở mẫu cuối; âm giữ nguyên chỗ đã nằm dưới đường; độ lợi chỉ giảm. Không còn kiểu cắt phẳng rồi làm mờ | Crossfade công suất đều 500 ms, rồi **kiểm mối nối** bằng chính số đo L1 của bộ phê bình; trượt thì thử điểm khác (tới 12 lần) |
| Kênh | Theo thẻ: mono theo luật 5.1 (giữa nếu mất ≤ 3 dB) | Theo thẻ: stereo giữ nguyên, ghi tương quan; bản mono nhân đôi được đánh dấu `dual_mono`. **Cân hai kênh theo từng 1/3 octave** (vòng soát 2: H s2004 nghiêng phải 5,9 dB, 6,6 dB dưới 150 Hz nhưng 2,7 dB ở 4–16 kHz): tỉ lệ năng lượng trái/phải dài hạn mỗi 1/3 octave, làm mượt 3 dải, mỗi kênh nhận một nửa chênh lệch qua bộ lọc FIR pha tuyến tính đặt giữa (không trễ). Ghi `lr_balance` (trước, sau) trong `<tên>.proc.json` |
| Lọc lược | — | `--notch-comb`: ở mỗi vạch k × 44100/256 Hz (172,27 Hz) trên 10 kHz nhô ≥ 3 dB (bộ giải mã của mô hình để lại các vạch này), một bộ lọc đỉnh rộng 24 Hz, pha không, **cắt đúng bằng độ nhô của vạch**: vạch về ngang nền, không thành hố (khấc sâu vô hạn làm vạch tụt 10 dB dưới nền) |
| Mức | Theo thẻ (`loudness.file`: đỉnh −1 dBTP) | Theo thẻ (LUFS-I −26), giới hạn ≤ 3 dB |

Ra: `<out>/<tên>.wav` (PCM 24-bit), `<tên>.proc.json` (cửa sổ, đầu tiếng, các ứng viên cửa sổ, đuôi, kênh, mối nối, lọc khấc, chuỗi), `SOURCES.json` (một lớp `gen` cho mỗi file, kèm kiểm clip trên **bản float** trong đúng cửa sổ, để `critic run --sources` dùng) và `licences.rows.jsonl`.

`common/batch0b.py` (`run.sh batch0b all`) chạy cả vòng 2 của lô 0b: tạo, xử lý, dựng công thức ghép lớp, chấm, ghi sổ, kiểm giấy phép trên cây thử, lập phiên nghe. Từng bước: `run.sh batch0b generate|process|recipes|critic|link|session|report [--force]`. Phiên đã có không bị ghi đè nếu thiếu `--force`. Báo cáo: `~/AudioLab/work/_batch0b/sa3-r2/REPORT.md` và `summary.json`; hướng dẫn nghe cho chủ dự án: [`SESSION_0B.md`](../SESSION_0B.md).

## Thư viện CC0: lệnh

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
