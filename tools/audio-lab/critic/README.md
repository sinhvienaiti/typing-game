# Tai AI nhiều lớp (`critic/`)

Bộ phê bình của mục 4 trong [`AUDIO_PIPELINE.md`](../../../docs/games/AUDIO_PIPELINE.md). Nó **loại bản hỏng** và **xếp hạng** bản còn lại trong cùng một id hoặc một nhóm. Nó không quyết định âm nào hay: tai chủ dự án trên Bảng Nghe là cổng cuối (L8).

## Lệnh

```bash
pnpm audio:critic run <file|thư mục>... [--spec THẺ.yaml|THƯ_MỤC] [--refs ÂM_ĐÃ_DUYỆT...] \
    [--layers L1,L1b,L2,L3,L4,L5,L6 | fast | all] [--out THƯ_MỤC] [--stage final|raw] \
    [--sources SOURCES.json] [--group NHÓM] [--game GAME] [--variant-set] [--blind-cards] [--fail-on-block]
pnpm audio:critic groups      # bảng nhóm âm: độ dài, ngưỡng lên, im lặng đầu, lặp, stereo, họ bẩn, mục tiêu L2
pnpm audio:critic schema      # JSON Schema của file kết quả
pnpm audio:critic pairs OUT   # so cặp bản gốc / bản làm hỏng (<tên>__clipped|muddy|thin), cổng của lô 0a
```

Ví dụ:

```bash
# Ứng viên của một id, thẻ spec do làn Specs sinh, mọi lớp
bash tools/audio-lab/run.sh critic run ~/AudioLab/work/typing-survival/gun.xung/r1 \
    --spec tools/audio-lab/specs/typing-survival/gun.xung.yaml --out ~/AudioLab/work/typing-survival/gun.xung/r1/critic

# Nhanh, không nạp mô hình (L1, L1b, L2, thẻ ảnh)
bash tools/audio-lab/run.sh critic run a.wav b.wav --layers fast --group hit_heavy

# File vừa tạo, chưa qua chuỗi sửa: chỉ clip chặn, lỗi khác thành việc sửa
bash tools/audio-lab/run.sh critic run raw/ --stage raw
```

- Đầu vào: WAV, FLAC, OGG Vorbis, MP3, AIFF (libsndfile, không cần ffmpeg). Thư mục được tìm đệ quy.
- `--out` mặc định là `~/AudioLab/work/_critic/<giờ>`. Bộ chấm từ chối ghi vào `games/**` và cảnh báo khi ghi trong repo.
- Mã thoát: 0 khi chạy xong; 1 khi có `--fail-on-block` và có file bị chặn; 2 khi tham số sai.
- **File hỏng không làm dừng cả lần chấm.** File không đọc được, 0 byte hay 0 khung, có mẫu NaN hoặc Inf, hay làm bộ đo lỗi đều thành kết quả `BLOCK` với kiểm L1 riêng (`unreadable`, `empty`, `not_finite`, `analysis_error`) và lý do bằng tiếng Việt; các file khác vẫn được chấm. File nhiều hơn 5 kênh được đo (kênh thứ 6 trở đi có trọng số 1,0) và trượt kiểm số kênh.

## Các lớp

| Lớp | Việc | Quyền ở lô 1 | Mã |
|---|---|---|---|
| L0 | Đọc thẻ spec: nhóm, độ dài, ngưỡng lên, im lặng đầu, lặp, stereo, họ bẩn, nhãn AST | — | `spec.py`, `groups.py` |
| L1 | Cổng vệ sinh, ngưỡng mục 4.3.1: clip (3 mẫu ≥ 0,999 FS; 4 mẫu cùng độ lớn trên −20 dBFS), **clip trong file nguồn của từng lớp** (đọc `rawQa` trong `SOURCES.json` qua `--sources`), thời gian lên, im lặng đầu, lệch DC, đỉnh thật ≤ −1 dBTP, độ dài ±20 % so với thẻ, đuôi (−60 dB hoặc làm mờ 5 ms), mối nối vòng lặp, 48 kHz, mono, tương quan stereo, đúng số ô nhịp | **Chặn** | `hygiene.py` |
| L1b | Lỗi do mô hình tạo (mục 4.3.2): đầu tiếng nhòe, tiếng vọng trước đầu tiếng, rít cao tần, xoáy pha, rung cao độ, hai kênh lệch, nền nhiễu; thêm cờ `low_bit_depth` cho PCM 8-bit | Gắn cờ | `artifacts.py` |
| L2 | Đặc trưng theo nhóm (mục 4.3.3): lên, độ nảy, crest, độ sắc lớp tách, trọng tâm, rolloff, độ phẳng, năng lượng theo dải, đuôi, sub, LUFS-M max (đệm 0,4 s), LUFS cửa sổ 100 ms (`lufs_100ms_max`), độ khớp độ dài (theo dung sai của thẻ), mất trên loa nhỏ; MoSQITo độ chói và độ gắt | Xếp hạng | `features.py`, `psycho.py` |
| L3 | audiobox-aesthetics PQ, CE | Xếp hạng, trọng số 0 với họ bẩn | `learned.py` |
| L4 | CLAP (2 mô hình) loại âm zero-shot, cặp chất liệu, AST nhãn AudioSet | Chỉ gắn cờ, trọng số tối đa 0,1 | `learned.py`, `vocab.py` |
| L5 | Khoảng cách tới âm đã duyệt (CLAP lớn), KAD khi có từ 20 | Trọng số 0 khi chưa có 5 âm tham chiếu | `learned.py` |
| L6 | Thẻ ảnh PNG cho mỗi file | Claude đọc top-6, bản dò và mọi ca bị cờ | `card.py` |

Điểm tổng (mục 4.5, `score.py`): mỗi lớp thành z-score trong cùng nhóm xếp hạng (cùng id nếu có, không thì cùng nhóm), rồi cộng theo trọng số của giai đoạn (`batch1`, `batch1-dirty`, `ref5`, `ref5-dirty`). Lớp không chạy thì bỏ ra và chia lại trọng số. File bị chặn không được xếp hạng.

- **Hỏi chủ dự án** khi hạng L2 và L3 lệch quá 3 bậc, khi có cờ L1b hay L5, hoặc khi có cờ L4 **tách được các bản trong cùng id** (có bản bị cờ, có bản không). Cờ L4 mà mọi bản cùng id đều có là đặc điểm của id hay của mô hình, không của từng bản. Cờ AST "thiếu nhãn mong đợi" (`ast_expected_missing`) và "khó nhận ra" (`ast_low_conf`) không tính vào hỏi cho đến khi AST được hiệu chỉnh bằng điểm của chủ dự án. Mỗi cờ có trường `ask`; `summary.md` và `_batch.json` (`ask_stats`) ghi tỉ lệ hỏi và tỉ lệ từng loại cờ.
- **Danh sách nghe** (mục 4.6 bước 2): bản đứng đầu, bản khác nhất, và ở khoảng 30 % số id (theo `--seed`) một bản dò rút từ **nửa dưới** của xếp hạng máy. Các mục ghi theo `stem` duy nhất của lần chấm (`gun.xung-v1`, `gun.xung-v1__2`), không theo tên file, nên hai file trùng tên ở hai thư mục không lẫn nhau.

### Giai đoạn `final` và `raw`

- `final` (mặc định): file sắp phát hành. Trượt kiểm nào cũng chặn.
- `raw`: file vừa tạo. Clip, đỉnh phẳng và file im lặng vẫn chặn (không sửa được). Kiểm khác thành việc sửa (`trim_head`, `hpf`, `limit`, `fade_tail`, `resample`, `mono`…), kết luận `NEEDS_FIX`. Sửa xong phải chấm lại với `final`.

### Chỗ khác với chữ của kế hoạch (ghi rõ để chủ dự án duyệt)

- **Đỉnh phẳng:** chỉ tính đoạn nằm trong 1 dB dưới đỉnh của kênh, vì trần clip luôn là đỉnh của file (kể cả sau khi chuẩn hóa: trường hợp Stable Audio 3 ghi PCM 16-bit). Đỉnh tròn của nốt trầm ở 16-bit (ví dụ mẫu kèn co D2 của VSCO) cho vài mẫu bằng nhau ở mức thấp hơn đỉnh nhiều, nên không bị tính. Đoạn mà bước vào và bước ra đều dưới khoảng 4 LSB cũng bỏ qua.
- **Sóng vuông vẽ bằng mã:** đoạn phẳng mà bước vào và bước ra là cú nhảy qua số 0 (lớn hơn chính độ cao của đoạn) được đếm riêng là `plateau_runs`, không tính là clip.
- **File số thực và file nén mất dữ liệu** (WAV float, OGG Vorbis, Opus, MP3): bộ giải mã vọt quá 1,0 mà không hề bị cắt. Đoạn chạm trần chỉ tính khi các mẫu thật sự bằng nhau. Phần vọt vẫn bị kiểm đỉnh thật bắt, và hạ mức là sửa được. Trước đây 17/50 file Kenney RPG bị chặn nhầm vì lý do này.
- **PCM 8-bit:** mẫu bằng nhau là do lượng tử, nên không kiểm đỉnh phẳng; file được gắn cờ L1b `low_bit_depth` thay vì "đã cắt đỉnh".
- **Lệch DC:** đo DC thật, không lấy trung bình của cả file. Trung bình có trọng số Hann trên khung 40 ms, rồi lấy trung vị trên các khung lặng (thấp hơn khung to nhất 30 dB), hoặc trên mọi khung khi âm không có đoạn lặng. Một tiếng trúng 120 ms ở 180 Hz không có DC có trung bình 0,26 % FS và trước đây trượt kiểm; số đo mới cho khoảng 0. Trung bình thô vẫn ghi ở `metrics.mean_abs` để tham khảo.
- **Im lặng đầu và thời gian lên:** giá trị `null` ghi tường minh trong thẻ nghĩa là "không kiểm" (vòng lặp và nhạc không kiểm im lặng đầu; nhóm `music`, `ambience` mặc định cũng vậy).
- **Clip trong nguồn của lớp:** khi truyền `--sources SOURCES.json` của bản dựng, kiểm `source_clip` chặn file có lớp mà file nguồn bị cắt đỉnh (`rawQa.verdict = BLOCK`) mà công thức không ghi lý do `allowClip`. Bản trộn và chuỗi cuối giấu đỉnh phẳng dưới 0,999, nên kiểm trên bản cuối không đủ.
- **Bước nhảy ở mối nối:** tính phần vượt quá bước nhảy P95 bình thường trong file, rồi so với −40 dBFS. Đo bước nhảy thô thì mọi nền có nhiễu sáng đều bị chặn.
- **Mối nối của nhạc:** vòng nhạc chỉ bị chặn bởi bước nhảy mẫu. RMS và trọng tâm phổ ở hai đầu được ghi lại nhưng không chặn, vì phách mạnh ở ô nhịp đầu luôn to hơn đuôi ô nhịp cuối. Nền lặp vẫn kiểm đủ ba điều.
- **Im lặng đầu:** thời gian trước mẫu đầu tiên trên −60 dBFS.
- **Đầu tiếng nhòe (L1b):** thời gian lên 10–90 % của lớp trên 2 kHz, **chỉ xét từ 2 ms trước đến 50 ms sau đầu tiếng**, cờ khi quá min(5 ms, ngưỡng lên của nhóm). Tiếng lách tách đến muộn (than hồng ở 85 ms của `fire.impact.a`) là đuôi, không phải lớp tách. Từ 3 âm tham chiếu, P90 của chúng chỉ được nới ngưỡng này, không siết. Mục tiêu L2 `hf_attack_ms` dùng cùng số đo.
- **Rung cao độ (L1b):** khi đường f0 đổi nốt (bước nhảy trên 80 cent), chỉ nốt giữ lâu nhất được xét. Với file mà sổ nguồn cho biết không do mô hình tạo (lớp thư viện, bộ phát mẫu, mã; file trong `~/AudioLab/libraries`; bản phát mẫu có báo cáo `.json` bên cạnh) thì vẫn đo nhưng **không gắn cờ**: đàn tranh thật và lối ngân rung cố ý vốn trôi cao độ.
- **Khuôn L2 mới:** `hit_fire` cho `fire.impact.*` của Rồng Giữ Ải ("phụt lửa trầm, thân tròn": không đòi lớp tách 2 kHz, crest và dải đục nới); `shot_launch` thêm ngưỡng dưới cho thân 150–800 Hz để bản mỏng không đạt mọi mục; mục tiêu độ dài lấy đúng dung sai của thẻ (độ dài trong spec không bao giờ tô đỏ).
- **Nhóm `generic`:** không kiểm thời gian lên (mục 4.3.1 chỉ kiểm phím, UI, trúng, bắn, nổ, sinh vật).
- Mọi ngưỡng L1b và mục tiêu L2 là điểm xuất phát, chưa hiệu chỉnh. Khi một id có từ 5 âm tham chiếu, mục tiêu L2 thành khoảng P10–P90 của bộ đó.

## Thẻ spec, âm tham chiếu, sổ nguồn

- `--spec` nhận một file YAML (một thẻ hoặc danh sách) hoặc thư mục thẻ của làn Specs (`specs/<game>/`). File ứng viên khớp thẻ theo id dài nhất ở đầu tên file (`gun.xung-3.wav` → `gun.xung`). Không có thẻ thì nhóm suy ra từ tên file, cuối cùng là `generic`. Khóa đọc được ở đầu `critic/spec.py`.
- Độ dài: `duration: {target_ms, tolerance_pct}` của làn Specs được dùng đúng một lần dung sai; `tolerance_ms` (nhạc) thành khoảng chính xác ±1 ms.
- Âm tham chiếu: `refs` (hoặc `references: [{path}]`) trong thẻ chỉ dùng cho file của thẻ đó. `--refs` dùng cho file không có refs trong thẻ, nên chạy mỗi lần một id hoặc một nhóm.
- **Không đưa vào AI** (mục 10.2, 10.7): file có `/_no-ai/` hoặc Sonniss trong đường dẫn, file thuộc gói có `ai_input_allowed=false` trong `~/AudioLab/libraries/SOURCES.jsonl`, và file có `aiInputAllowed=false` trong sổ truyền qua `--sources` (khớp SHA-256 hoặc tên file) không bao giờ tới L3–L5. Thẻ ảnh của chúng có `cloud_ok: false`: không gửi cho AI chạy trên mây.
- Bộ chấm **không ghi** sổ nguồn. Mỗi JSON có `ai_steps` (`critic:audiobox`, `critic:clap`, `critic:ast`, kèm tên mô hình) để người dựng gọi `build.ledger.mark_ai_step` cho file phát hành.

## Kết quả

| File | Nội dung |
|---|---|
| `<tên>.json` | Schema `audiolab.critic.file/1` (`critic schema`): file và SHA-256, thẻ spec đã hiểu, `metrics`, `L1` (từng kiểm: đo trên gì, ngưỡng, cách sửa, có chặn không), `L1b`, `L2` (mục tiêu và điểm), `L3`–`L5`, `flags`, `score`, `ask_owner`, `read_card`, `notes_vi`, `ai_policy`, `ai_steps`, `refs` |
| `<tên>.blind.png` | Với `--blind-cards`: thẻ cho Bảng Nghe (trường `card_blind`). Chỉ có số đo và lỗi vệ sinh L1: không tên file, định dạng, nhóm, kết luận, hạng, điểm, "hỏi chủ dự án", thanh mục tiêu L2 hay cờ L1b/L4/L5. Phán quyết của máy hiện giữa các id sẽ dạy tai chủ dự án |
| `<tên>.png` | Thẻ ảnh khoảng 1500 × 1000 điểm ảnh: kết luận, hạng, số chính; dạng sóng có vạch clip và im lặng đầu; phóng đầu tiếng và cuối file (hoặc mối nối); mel spectrogram tới Nyquist có vạch 8 kHz; phổ trung bình; đường độ to (RMS 1 ms, LUFS-M 400 ms, LUFS cửa sổ 100 ms, đỉnh −60 dB); thanh mục tiêu L2. Với âm có cao độ, dải 200–500 Hz ghi "gồm nốt gốc" thay vì "ù" |
| `_batch.json` | Schema `audiolab.critic.batch/1`: số đạt, cần sửa, bị chặn; danh sách nghe (theo stem); `ask_stats`; mô hình đã nạp, thiết bị, thời gian; bộ âm tham chiếu; mỗi file có `name`, `stem`, `path` |
| `summary.md` | Bảng xếp hạng theo nhóm, file bị chặn và cách sửa, danh sách nghe, thẻ ảnh cần đọc |

Bảng Nghe đọc `_batch.json` bằng `board from-critic`.

## Mô hình

- Nạp lười, một lần mỗi tiến trình, từ cache Hugging Face ở `~/AudioLab/models/hf-cache` với `HF_HUB_OFFLINE=1`, không token.
- Chạy MPS khi có; `AUDIOLAB_DEVICE=cpu` ép CPU; lỗi MPS của audiobox tự chuyển CPU.
- Âm ngắn dưới 300 ms được L3–L5 chấm trên bản lặp 3–4 s theo nhịp của nhóm hoặc `rate_hz` của thẻ. `--variant-set` xoay vòng các biến thể trong bản lặp.
- Mô hình: `facebook/audiobox-aesthetics`, `laion/clap-htsat-unfused`, `laion/larger_clap_general`, `MIT/ast-finetuned-audioset-10-10-0.4593`. Mỗi mô hình được nạp **đúng revision đã ghim** trong `common/fetch_models.py` (mục 10.8), không theo `refs/main`. `ai_steps` ghi `repo@revision` đã nạp, và `build mark-ai` chép đúng giá trị đó vào sổ.
- **CLAP lặp lại được:** bộ tách đặc trưng của CLAP tự cắt ngẫu nhiên một đoạn 10 s (`rand_trunc`) khi file dài hơn, nên trước đây cùng một file 15 s cho điểm khác nhau mỗi lần. Giờ file dài hơn 10 s được cắt thành các cửa sổ 10 s cố định, cách đều (tối đa 6), rồi lấy trung bình vector.
- **File dài hơn 2 phút:** L3, L4, L5 chỉ nghe 6 đoạn 10 s cách đều (trường `input` của từng lớp và `long_file` trong JSON ghi rõ). File 10 phút trước đây mất khoảng 209 s và 4,4 GB RAM.

## Kiểm thử

```bash
bash tools/audio-lab/run.sh test tools/audio-lab/critic                          # không nạp mô hình
AUDIOLAB_TEST_MODELS=1 bash tools/audio-lab/run.sh test tools/audio-lab/critic   # thêm L3–L5 thật, offline
```

Âm thử được sinh lúc chạy (`tests/synth.py`): tiếng tách yếu, tiếng trúng nhiều lớp, bản clip, bản đục, im lặng đầu, đuôi cụt, đầu tiếng chậm, lệch DC, 44,1 kHz, stereo, đầu tiếng nhòe, vòng lặp liền và vòng lặp hở. L1 phải chặn đúng các bản hỏng; bản tốt xếp trên bản yếu, bản đục và bản nhòe.
