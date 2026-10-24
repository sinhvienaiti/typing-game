# build: ghép lớp, chuỗi cuối và sổ giấy phép

Module này dựng âm từ **công thức** (recipe JSON): ghép lớp thư viện CC0, file tự ghi, đầu ra mô hình và âm tổng hợp bằng mã, rồi chạy chuỗi xử lý cuối, xuất master WAV và file OGG cho game, kèm hồ sơ nguồn gốc. Hợp đồng: `docs/games/AUDIO_PIPELINE.md` mục 5.1–5.3, 10.5–10.7 và 11.

## Lệnh

```bash
R=tools/audio-lab/run.sh
bash $R build validate tools/audio-lab/build/examples/*.json                # kiểm công thức theo schema
bash $R build render  tools/audio-lab/build/examples/typing-survival.hit-demo.json --run thu-1
bash $R build render  RECIPE.json --seed 900 --count 12 --spec CARD.yaml
bash $R build release --run ~/AudioLab/work/<game>/<id>/<run> --variants 1,3,4   # mặc định vào staging
bash $R build licence-check [--game G] [--staging] [--art-src DIR --public DIR] [--json]
pnpm audio:licence-check                                     # = build.licence_check, quét games/**
bash $R build mark-ai --sources .../SOURCES.json --step critic:audiobox --model REPO@REV
bash $R build ledger add-model --art-src DIR --repo R --revision REV --licence L --licence-url U --role critic
bash $R build ledger add-acceptance --art-src DIR --licence LicenseRef-Stability-Community-2024 --version 2024-07-05 --who "<chủ dự án>" --file licences/stability-registration.txt --licence-url U
bash $R build ledger add-file --art-src DIR --path ghi-am.wav --licence LicenseRef-owner-recording --licence-url licences/owner-recordings.txt
bash $R build ledger add-tool --art-src DIR --name pedalboard --version 0.9.26 --licence GPL-3.0-only --licence-url https://github.com/spotify/pedalboard/blob/v0.9.26/LICENSE --path LICENSE
bash $R build synth fm_ping --params '{"carrierHz": 2400}' --out ~/AudioLab/work/_synth/ping.wav
```

Lệnh `render` mặc định ghi vào `~/AudioLab/work/<game>/<id>/<run>/`. Lệnh từ chối dựng (mã 1, file không đổi) nếu một lớp dùng nguồn có giấy phép bị cấm hoặc lạ, nguồn `commercial_ok=false`, trọng số phi thương mại, hoặc **nguồn bị cắt đỉnh trong file gốc** (cổng clip của mục 4.3.1, xem dưới). Lệnh `release` mặc định ghi vào `~/AudioLab/review/staging/<game>/` (`art-src/audio` và `public/assets/<game>/audio`). Chỉ người điều phối chép sang `games/**`, hoặc chạy lại `release` với `--art-src`/`--public` trỏ vào game.

## Công thức (`schemas/recipe.schema.json`, `audiolab.recipe/1`)

| Trường | Ý nghĩa |
|---|---|
| `game`, `id`, `group`, `family` | `group` là nhóm biến thể của mục 5.3, cùng tên với thẻ spec: `key-ok`, `key-bad`, `word-reward`, `rare-fixed`, `shot`, `hit-small`, `hit-heavy`, `blast`, `death-swarm`, `none` (vòng lặp, nhạc), `default` (chưa có nhóm, không giới hạn). Khoảng cao độ và độ to của biến thể bị thu về giới hạn của nhóm. Có `--spec CARD.yaml` thì lấy `randomisation {pitch_cents, gain_db}` của thẻ (`gain_db: null` nghĩa là 0 dB; cả hai `null` là không giới hạn) và `variants.target` làm số biến thể nếu công thức không ghi |
| `layers[]` | `id`, `role`, `source`, `offsetMs`, `gainDb`, `pitchSemitones`, `pitchMode` (`varispeed` như playbackRate, hoặc `preserve`), `trim {startMs, endMs}`, `fadeInMs`, `fadeOutMs`, `reverse`, `filters[]`, `mute`, `vary`, `allowClip` (lý do bằng chữ khi cố ý dùng một nguồn bị cắt đỉnh; hiếm) |
| `source` | Đúng một trong: `{"library": "kenney/impact-sounds/Audio/x.ogg"}`, `{"synth": "noise_burst", "params": {…}}`, `{"file": "...", "ledger": "<khóa licences.jsonl hoặc cả dòng>"}`, `{"gen": {tool, model, licence, file, record, prompt, seed, cfg, window, initAudio, initNoise}}` (`record`: hồ sơ ứng viên của `gen/sa3.py`; bộ dựng kiểm SHA-256 rồi mang dòng sổ mô hình, bản đăng ký Stability và điều khoản Gemma vào lần dựng), `{"sampler": {instrument, notes, bpm, lengthS, tail, tuning, seed}}` (bộ phát mẫu dựng ngay trong lúc dựng) hoặc `{"sampler": {"render": "x.wav"}}` (bản phát mẫu có sẵn, kèm `x.json`) |
| `layers[].vary` | `pitchCents`, `gainDb`, `offsetMs` (khoảng `[min, max]`), `swap[]` (nguồn thay thế; mỗi biến thể chọn một), `swapMode` (`random` mặc định; `cycle`: biến thể n dùng nguồn thứ n, để ứng viên khác nhau có chủ đích), `reseed` (âm tổng hợp đổi seed theo biến thể, mặc định có) |
| `filters[]` | `highpass`, `lowpass`, `bandpass` (Butterworth), `peak`, `lowshelf`, `highshelf` (biquad RBJ). Mọi bộ lọc là nhân quả, không tạo tiếng vọng trước đầu tiếng |
| `chain` | `dcHpfHz` (35), `hpfHz`, `filters`, `saturation {driveDb, mix}`, `headTrim {thresholdDb −50, preRollMs 0,5}`, `maxLengthMs`, `tail {floorDb −60, fadeMs 10}` hoặc `tail {floorDb −60, shape: "exp", kneeMs}` (mũ hàm mũ: từ điểm gối, mặc định 35 % độ dài và không trước đỉnh + 5 ms, mức giảm thẳng theo dB tới `floorDb` ở mẫu cuối; dùng khi `maxLengthMs` cắt một tiếng còn ngân, thay cho cắt phẳng rồi làm mờ), `loopCrossfadeMs`, `normalise {mode, target}`, `limiter {ceilingDbtp −1, releaseMs, maxGrDb 6}` |
| `normalise.mode` | `lufs-m-max` (mặc định, −20, đệm đủ 0,4 s), `lufs-s-max`, `lufs-i` (nền, nhạc), `peak`, `none` |
| `variants` | `count`, `seed`, `includeBase` (biến thể 1 không ngẫu nhiên, làm bản gốc), `pitchCents`, `gainDb` (lệch so với mức chung) |
| `loop` | Vòng lặp: không cắt đầu, không làm mờ đuôi, mặc định LUFS-I −26; `loopCrossfadeMs` nối đuôi vào đầu |
| `export` | `path` (gốc tên file trong `public/assets/<game>/audio`, ví dụ `sfx/dragon/fire-impact-a`), `ogg`, `oggQuality` |

Bộ tạo âm (`synth.py`, có seed, đỉnh 1,0): `noise_burst`, `noise_sweep`, `tone` (sine, square, saw, triangle có trượt cao độ), `sub_thump`, `fm_ping`, `click`.

Mẫu trong `examples/`: `typing-survival.hit-demo.json` (Kenney Impact và tổng hợp), `dragon-hold.key-demo.json` (chỉ tổng hợp), `typing-defense.leak-demo.json` (VCSL Anvil và sub). Cả ba chỉ là mẫu, chưa qua chủ dự án; đừng phát hành vào game.

## Chuỗi cuối

Thứ tự: lọc cao bỏ DC → EQ → bão hòa nhẹ (tùy chọn) → cắt im lặng đầu (giữ 0,5 ms, làm mờ phần giữ lại) → giới hạn độ dài → cắt đuôi dưới −60 dB và làm mờ → chuẩn hóa → bộ giới hạn `BrickwallLimiter` của pedalboard (đỉnh thật, trần −1,3 dBTP) → chốt an toàn đỉnh thật ≤ −1 dBTP. DC chỉ được bỏ bằng bộ lọc cao. Bước `dcTrim` cũ (trừ một khối hình Hann cho trung bình về 0) đã bỏ: nó chỉ làm đẹp số đo trung bình của một âm sub ngắn, không bỏ DC thật (mục 5.5). Bộ phê bình nay đo DC thật (`critic.audio.dc_estimate`), và `render.json` › `dcPercent` dùng cùng số đo. Bộ giới hạn không ép quá `maxGrDb`. Âm quá ngắn (phím 15–60 ms) không đạt LUFS-M max −20 nếu không ép mạnh, nên cả id hạ về cùng một mức và `render.json` ghi rõ mức đó (`idLevel`, cảnh báo). Phần bù nằm ở `gainDb` của catalog.

Master: WAV 48 kHz PCM 24-bit. File game: OGG Vorbis 48 kHz. Sau khi mã hóa, bản dựng giải mã lại file OGG và đo đỉnh thật; nếu Vorbis đẩy đỉnh vượt trần thì hạ cả master lẫn OGG cho bằng nhau (`chain.oggSafetyGainDb`, `chain.oggTruePeakDbtp` trong `render.json`). Hai loại đều giống nhau từng byte khi cùng công thức và seed (số serial Ogg được cố định).

## Công thức cho id thật (`recipes/<game>/<id>.json`)

Mười công thức của lô 0, viết theo thẻ spec, không dùng Stable Audio 3: `dragon-hold/fire.impact.a`, `dragon-hold/trap.pine-bomb.trigger`, `dragon-hold/wave.horn` (kèn co và trombone VSCO-2-CE, trống khung VCSL, qua chuỗi cuối thành mono 2,2 s), `typing-survival/gun.xung`, `typing-survival/hit.t1`, `typing-survival/hit.t2`, `typing-defense/ui-move`, `typing-defense/ui-pick`, `typing-defense/word-hit` (đàn tranh qua bộ phát mẫu), `typing-defense/leak` (cồng VCSL hoặc kẻng VCSL Anvil). Trường `description` ghi lý do của từng lớp và các vòng sửa sau khi đọc thẻ ảnh. Chúng là bản nháp chờ chủ dự án nghe ở lô 0a; khi một bản được chọn, `release` chép công thức vào `art-src/audio/recipes/`.

## Đầu ra của một lần dựng

`masters/<id>-v<n>.wav`, `runtime/<path>-<n>.ogg`, `render.json` (kế hoạch biến thể, số đo bản trộn thô và bản cuối, `layersRawQa`, báo cáo chuỗi), `SOURCES.json`, `licences.rows.jsonl`, `manifest.fragment.json` (manifest v2), `recipe.json`.

## Cổng clip trên nguồn của từng lớp

Mục 4.3.1: clip trong file gốc không sửa được. Bản trộn và chuỗi cuối (lọc, chuẩn hóa, giới hạn) đẩy đỉnh phẳng xuống dưới 0,999, nên kiểm trên bản cuối không thấy. Vì vậy `render` chạy `critic.hygiene.clip_scan` trên **từng file nguồn đúng như đang lưu**, trước khi đổi tần số lấy mẫu, chỉnh mức hay trộn:

- lớp `library` và `file`: file nguồn; lớp `gen`: đoạn `window` của file mô hình tạo; lớp `sampler`: từng mẫu VCSL, VSCO-2-CE đã dùng; lớp `synth`: không (mã của dự án).
- Có clip (`clip_full_scale` hoặc `clip_flat_top`) thì `render` dừng với `RawClipError`, trừ khi lớp ghi `allowClip: "<lý do>"`.
- Kết quả ghi vào `SOURCES.json` › `layers[].rawQa` (`verdict`, từng file, `exception` nếu có) và `render.json` › `variants[].layersRawQa`. Bộ phê bình đọc nó qua `--sources` (kiểm `source_clip`, chặn ở mọi giai đoạn), và `licence-check` báo lỗi `raw-clip` cho lớp bị cắt đỉnh không có lý do.
- Quét toàn bộ 1 853 file thư viện ngày 23/10/2026: 6 file bị cờ (VSCO-2-CE `MOHorn_stac_F4_v3_rr1.wav` có 45 đoạn chạm trần, vài mẫu bộ gõ và cello tremolo, một mẫu VCSL FX), 0 file Kenney.

## Sổ giấy phép

- `SOURCES.json` (`schemas/sources.schema.json`): mỗi file phát hành một hồ sơ, khóa là đường dẫn trong `public/assets/<game>/audio` (kiểm tra cũng nhận tên file trần như ví dụ ở mục 10.5). Có lớp, nguồn, mã băm, giấy phép, công cụ và phiên bản, mô hình, `aiSteps`, `aiInputAllowed`.
- `licences.jsonl` (`schemas/licences.schema.json`): mỗi dòng là một `source`, `library`, `model`, `acceptance` hoặc `tool`. Dòng nào cũng có ngày, URL giấy phép và mã băm. Bản lưu giấy phép có ngày được chép vào `art-src/audio/licences/`.
- Công cụ nào đưa file đã dựng vào mô hình (ví dụ audiobox, CLAP) phải gọi `ledger.mark_ai_step()` hoặc `build mark-ai`. Sau mỗi lần chấm: `build mark-ai --run RUN_DIR --from-critic CRITIC_OUT` (`critic_link.py`) khớp JSON của bộ phê bình với hồ sơ theo SHA-256, ghi mọi bước AI và thêm dòng `model` cho audiobox (CC-BY-4.0), hai bản CLAP (Apache-2.0) và AST (BSD-3-Clause) vào `licences.rows.jsonl`. File có `aiInputAllowed=false` thì không được đưa vào mô hình (đọc trước bằng `ledger.ai_input_allowed()` hoặc `render.json` › `variants[].aiInputAllowed`). `model` là `repo@revision` đúng như bộ chấm đã nạp (`critic.learned.ai_steps`, revision ghim trong `common/fetch_models.py`). Chỉ khi thiếu `@revision` mới tra bảng ghim đó; không bao giờ đọc `refs/main` của cache, vì một lần tải sau có thể dời nó (mục 10.8). Mô hình đó cần một dòng `ledger add-model`.
- Thư viện Sonniss và mọi thứ dưới `~/AudioLab/libraries/_no-ai/` luôn mang `ai_input_allowed=false`, bất kể dòng sổ ghi gì.
- Lớp `sampler` ghi `sources[]`: mỗi mẫu VCSL hay VSCO-2-CE đã dùng có một dòng `source` và dòng `library` riêng; `licence-check` kiểm từng mẫu.
- Lớp `gen` có `initAudio` (audio-to-audio): nếu là đường dẫn có thật, bản dựng ghi `tên sha256:<mã>`. `licence-check` lần theo mã đó tới dòng sổ hoặc hồ sơ của file gốc, và coi mọi nguồn trong file gốc là đã qua bước AI.
- Bản lưu giấy phép đặt tên theo `licence_copy` của thư viện: `kenney/impact-sounds/LICENSE-<ngày>.txt` thành `licences/kenney-impact-sounds-LICENSE-<ngày>.txt`; cả VCSL dùng chung `licences/vcsl-LICENSE-<ngày>.txt`.
- Dòng `tool` (`ledger add-tool`): công cụ chạy trên máy, ví dụ pedalboard (GPL, mục 10.9) hay file LICENSE của mô hình nghe L7 (mục 10.2). `licence-check` không chặn dòng `tool`, vì công cụ không đóng vào game.
- `licence-check` chặn: file thiếu hồ sơ, mã băm lệch, nguồn thiếu dòng sổ, giấy phép lạ hoặc bị cấm (NC, Sampling+, ND, research…), `commercial_ok=false`, trọng số phi thương mại, nguồn cấm AI đã qua bước AI, Sonniss trong bước AI, Stable Audio 3 chưa có dòng đăng ký, bản ghi của người khác thiếu giấy đồng ý, CC-BY thiếu `CREDITS.md`, thiếu bản lưu giấy phép, lớp có nguồn bị cắt đỉnh mà không có `allowClip` (`raw-clip`). Bảng chính sách ở `policy.py`.

Lệnh mặc định (`pnpm audio:licence-check`) quét 4 game:

- Game đã có `SOURCES.json`, `licences.jsonl` hay manifest v2: kiểm đủ luật trên `art-src/audio` và thư mục âm phát hành.
- Game chưa có: **không tính là đạt**. Thư mục âm phát hành (`public/assets/<game>/audio`; Space Typing: `public/assets/audio` và `src/assets/audio`) vẫn được quét. Mỗi file phải nằm trong danh sách file cũ được miễn `build/legacy-audio.json` với đúng sha256 (mục 16 #9: 116 file CC0 của Space Typing đã có trong Git). File lạ là lỗi `missing-record`; file cũ đổi nội dung là lỗi `legacy-changed`.
- Không game nào được kiểm thì dòng cuối là **BỎ QUA**, không bao giờ là ĐẠT. `--json` có `state`, `checked`, `legacy`.
- `--freeze-legacy space-typing` sinh lại danh sách miễn từ git HEAD của game (blob đã commit, không lấy cây làm việc).
- Ghi `--game G` thì kiểm game đó dù chưa dùng đường ống. `--art-src` trỏ vào thư mục không có thì trả mã 2.

## Kiểm thử

`bash tools/audio-lab/run.sh test build -q`. Test tự sinh âm và thư viện giả lúc chạy, không cần mạng, không cần Kenney.
