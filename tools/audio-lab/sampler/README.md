# sampler: bộ phát mẫu Python

Phát MIDI hoặc danh sách nốt bằng mẫu thu thật CC0 (VCSL, VSCO-2-CE, hay thư mục mẫu tự ghi), ra WAV 48 kHz 24-bit stereo. Thay cho `sfizz_render` (mục 3.1 B và 3.4 của [kế hoạch](../../../docs/games/AUDIO_PIPELINE.md)). Chỉ dùng numpy, soundfile, soxr và mido. Không cần ffmpeg.

## Lệnh

```bash
L=tools/audio-lab/run.sh
bash $L sampler list --kind pitched                  # nhạc cụ có cao độ trong index
bash $L sampler info dan-tranh.normal                # gốc, tầm chơi được, lớp cường độ, round robin, chỉnh cent
bash $L sampler render -i dan-tranh.normal --notes "0:C5:0.5:100 0.25:D5:0.5:90 0.5:F5:1:110" -o ~/AudioLab/work/x/word-hit.wav
bash $L sampler render --midi nhac.mid --map "0=flute.susnv,1=harp,9=frame-drum" --bars 8 --tail wrap -o loop.wav
bash $L sampler render --instrument-dir ~/AudioLab/work/rec/chuong --notes "0:C5:1" -o chuong.wav
bash $L sampler phrase hand-chimes tubular-bells-2   # câu thử từng nhạc cụ
bash $L sampler phrases                               # câu thử cho mọi nhạc cụ, vào ~/AudioLab/work/_sampler/phrases
```

- `--notes`: các mục `bắt đầu:nốt:độ dài[:velocity[:phím]]`, tính bằng giây, hoặc bằng phách khi có `--bpm`. Nốt viết `C5`, `A#3` hay số MIDI. Với nhạc cụ không cao độ, viết tên phím (xem `info`), ví dụ `0:hdruml-hit:0.3:110`.
- `--notes-json`: mảng `{start, note|midi|key, dur, vel, instrument, cents, gain_db, pan, choke}`.
- `--map`: kênh MIDI (0–15) sang nhạc cụ. Không có `--map` thì mọi kênh dùng nhạc cụ đầu tiên.
- Mỗi WAV có file `.json` cùng tên: từng nốt lấy mẫu nào, gốc nào, dời bao nhiêu bán cung, chỉnh bao nhiêu cent, lớp và round robin nào, cùng danh sách `sources` (file, sha256, giấy phép). `run.sh gen.licence_lines <file .json>` đổi danh sách này thành dòng `licences.jsonl` (mục 10.6).

## Luật

- **Dời cao độ tối đa 3 bán cung** (mục 3.2). Trần tính cả khoảng cách nốt, `cents` của nốt và phần chỉnh tuning. `--max-shift` chỉ được nhỏ hơn 3. Nốt ngoài tầm thì báo lỗi, hoặc bỏ qua và ghi vào báo cáo khi có `--skip-out-of-range`. Dời bằng cách đổi tốc độ phát (resample bằng soxr VHQ), không kéo giãn thời gian.
- Chọn mẫu gốc gần nhất. Khi hai gốc cách đều, lấy gốc thấp hơn rồi dời lên, giống bảng SFZ của VCSL.
- **Lớp cường độ:** dùng `lovel`/`hivel` của SFZ khi có, nếu không thì chia đều 1–127 theo `v<n>` hoặc ký hiệu `pp…ff`. `--veltrack` (mặc định 0,5) thêm độ to theo velocity: v/127.
- **Round robin:** xoay vòng trong cùng lớp (`--rr cycle`), hoặc ngẫu nhiên không lặp bản vừa phát (`--rr random --seed N`). Mỗi lần render bắt đầu lại từ đầu, nên cùng đầu vào cho cùng đầu ra.
- **Đuôi:** mẫu gảy và gõ (`oneshot`) ngân hết đuôi tự nhiên. Mẫu ngân (`sus`, `trem`, `vib`…) tắt dần theo `release` sau khi nhả phím (lấy `ampeg_release` của SFZ, tối đa 3 s). `choke` buộc tắt dần cả mẫu oneshot. `--tail keep` để đuôi ngân quá độ dài. `cut` cắt ở `--length`/`--bars`. `wrap` gập đuôi về đầu để vòng lặp nhạc liền mạch.
- **Cắt đầu:** bỏ phần im lặng trước tiếng (ngưỡng −50 dB so với đỉnh, giữ 1 ms), làm mờ 0,5 ms. Làm mờ 5 ms ở cuối file để tránh tiếng tách.
- **Tuning** (`--tuning`): `auto` (mặc định) sửa quãng tám khi mọi mẫu đo được đều lệch đúng một quãng tám (glockenspiel, xylophone). Với mẫu có số đo f0 tin được (có đỉnh phổ rõ, độ trôi ≤ 30 cent, độ tin cậy pYIN ≥ 0,6, với chuông ≥ 0,9), số đo thay cho `tune` của SFZ: lệch 5–70 cent thì bù, lệch ≤ 5 cent thì để 0. Mẫu trôi quá 30 cent thì giữ nguyên và ghi vào `info`. Không chỉnh mẫu vibrato, tremolo, gliss, gong, bộ gõ. `sfz`: chỉ theo bảng SFZ (cả `tune`). `none`: không chỉnh. Trên dữ liệu thật, `auto` đưa đàn tranh, folk harp, hand chimes, harp, glockenspiel, xylophone về dưới 10 cent (xem `gen/README.md`).
- **Độ to ra:** `guard` (mặc định) chỉ hạ khi đỉnh vượt −1 dBFS. `peak` đưa đỉnh về −1 dBFS. Chuẩn hóa LUFS là việc của chuỗi dựng cuối (`build/`).
- Mẫu có nhiều vị trí micro: chỉ giữ vị trí phổ biến nhất, để không thành round robin giả.

## Trong Python

```python
from sampler.engine import Note, Sampler
from sampler.instrument import from_folder, from_index, load_index

s = Sampler()                                    # 48 kHz, trần 3 bán cung
s.add(from_index("dan-tranh.normal", load_index()), "tranh")
r = s.render([Note(0.0, 72, 100, 0.5, "tranh"), Note(0.25, 74, 90, 0.5, "tranh")])
r.write("word-hit.wav")                          # r.report: nốt, mẫu, dời, nguồn
```

`from_folder(thư_mục, octave_offset=12)` đọc mẫu tự ghi đặt tên kiểu `Ten_C4_v1_rr1.wav`. Dùng `octave_offset=12` khi tên ghi theo lối C3 là đô giữa.

## Kiểm thử

`bash tools/audio-lab/run.sh test tools/audio-lab/sampler tools/audio-lab/gen`. Test tự sinh mẫu sin và MIDI, không cần mạng hay thư viện thật. Riêng một test đọc index thật và tự bỏ qua khi chưa có index.
