# Phiếu 269 · Tu Tiên · Code và âm: mix lại âm lab theo bậc to, bỏ đoạn dâng của `release-k7` (`release-k5` để phiếu sau), thêm send vang chung

**Loại việc:** code và xử lý âm (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã chốt trong phiếu. Codex không thiết kế lại bậc, số hay cách đo. Chỗ nào không làm được đúng như viết thì dừng ở đó và ghi vào báo cáo.

**Báo cáo:** `docs/codex-queue/269-report.md` (tiếng Việt).

**Đường duyệt:**
- Claude viết lúc 20:20 ngày 04/11, từ `docs/games/tu-tien/skills/SOUND_AUDIT_2026-11-04.md` (số đo ffmpeg) và luật âm `.agents/skills/game-art-pipeline/references/audio.md` §5.
- Phản biện bởi agent Claude (bước 9 skill `agent-orchestration`). Ghi kết quả ở mục "Phản biện" cuối phiếu.
- Sửa sau phản biện vòng 1 lúc 20:50 ngày 04/11: mục 1, 2, 3, 4, 5, Kiểm và "Claude làm sau" đổi theo D1–D10 (xem "Phản biện").
- Sửa sau phản biện vòng 2 lúc 21:05 ngày 04/11: tên phiếu, mục 4 (`trims`, `ir --check`, luật không ghi đè), mục 5 test 1, Kiểm 4 và 6, "Claude làm sau" đổi theo E1–E3 (xem "Phản biện").
- Sửa sau phản biện vòng 3 ngày 04/11: mục 4 (`ir`, `ir --check`), Kiểm 6, "Claude làm sau" và dòng E2 đổi theo F1–F2 (xem "Phản biện").

## Bối cảnh
- Âm lab: `games/immortality-cultivation/src/lab/sound.ts` (`LabSound`).
  - Bus: `combat` 0,8, `voice` 0,95, `world` 0,85; master 0,9.
  - `on(e)` chọn sự kiện và gain; `update(dt)` đóng xô impact và death; `record()` ghi `SoundTake` cho bản quay cố định bước.
  - Mix offline của bản quay: `scripts/visual/mix-lab-sound.mjs` (ffmpeg).
- File: `games/immortality-cultivation/art-src/lab/audio/<event-id>/NN.ogg` cùng `manifest.json` (`{ "<event-id>": ["01.ogg", …] }`). `art-src/` không nằm trong Git.
- Số đo từng sự kiện: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/sound-audit/summary-by-event.json`, gồm `id`, `mMax` (momentary max, LUFS), `tp` (true peak, dBTP), `atk` (ms), `t40` (ms). Số đo từng file nằm ở `measurements.json` cùng thư mục.
- Ba lỗi phiếu này sửa (theo đánh giá):
  1. **Thứ bậc to ngược:**
     - sáu impact ở −10,1 tới −11,2, tức to hơn bậc trúng T3 5–6 LU;
     - release-k7 và release-guard ở −7,6, to hơn cao trào `world-climax` (−10,6).
  2. **Ra chậm:** `release-k5` dâng 2,1 s, `release-k7` dâng 1,8 s trước đỉnh. Anh muốn chiêu ra ngay.
     - Phiếu này chỉ sửa được `release-k7` (một take, mục 2).
     - `release-k5` còn nợ: cắt sẽ mất thân âm (xem mục 2). Phải dựng lại từ stem ở phiếu sau.
  3. **Không có send vang** trong game; chỉ có đuôi nướng sẵn.
- Âm lab hiện có gain tĩnh khác 1: gain theo sự kiện, bus và master. Phiếu này gộp chúng vào trim để mức **khi phát** đúng bậc (mục 1).
- Phiếu này **chỉ** dùng file sẵn có. Âm mới (cut-in, tiếng hô, Song Long, lớp lấp lánh của Lửa) là việc làm trong Firefly sau, không thuộc phiếu.

## Làm ở đâu
- **Worktree riêng:** `games/.wt-ic-sound`, nhánh `codex/lab-sound-tiers`, từ `main` của game.
  - Claude tạo trước khi chạy: `git -C …/games/immortality-cultivation worktree add ../.wt-ic-sound -b codex/lab-sound-tiers main`, cộng symlink `node_modules` như phiếu 255.
  - Mọi lệnh Vitest và Vite chạy với các cờ của phiếu 258 (mục Kiểm).
- **File âm mới** ghi vào `art-src` thật của game, đường tuyệt đối `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/audio/`, vì worktree không có `art-src`. Chỉ **thêm** file mới, không sửa hay xóa file đang có, **không sửa `manifest.json`** (lab đang chạy dùng nó).

### Được ghi
- `games/.wt-ic-sound/src/lab/sound.ts`;
- `games/.wt-ic-sound/src/lab/sound-tiers.ts` (tạo mới);
- `games/.wt-ic-sound/scripts/visual/mix-lab-sound.mjs`;
- `games/.wt-ic-sound/scripts/audio/lab-sound-tiers.mjs` (tạo mới: công cụ đo, cắt và tạo IR);
- `games/.wt-ic-sound/tests/lab/sound-tiers.test.ts` (tạo mới);
- `games/.wt-ic-sound/tests/lab/fixtures/sound-audit-summary.json` (tạo mới, mục 4 `trims`);
- `games/.wt-ic-sound/docs/changelog/2026-11-04-lab-sound-tiers.md` (tạo mới);
- trong `art-src/lab/audio/` của game (đường tuyệt đối ở trên), chỉ các file mới:
  - `release-k7/03a.ogg` (một file duy nhất; không tạo file `a` nào cho `release-k5`);
  - `ir/hall-a.wav`, `ir/hall-a.json`;
  - `manifest.next.json`;
- `docs/codex-queue/269-report.md`.

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`.
- Sửa hay xóa bất kỳ file âm đang có, hay `manifest.json`, `SOURCES.json`.
- Sửa file ngoài danh sách trên, nhất là `src/kit/**`, `skills-main.ts`, `events.ts`.
- Chạy dev server, mở trình duyệt, tải âm từ mạng, sinh âm bằng AI.
- Chạy Vitest hay Vite thiếu các cờ ở mục Kiểm.

## Việc (lời giải đã chốt)

### 1. Bảng bậc và trim (`src/lab/sound-tiers.ts`)
Đích theo momentary max (LUFS) của luật §5.4, tính ở **mức khi phát** (file × gain sự kiện chuẩn × bus × master). Mỗi bậc có một số đích trong khoảng:

| Bậc | Khoảng | Đích | Sự kiện |
|---|---|---:|---|
| T2 | −19 … −17 | −18 | `cast`, `release-auto`, `flyby`, `flyby-fire` |
| T3 | −20 … −16 | −18 | `impact-flesh`, `impact-stone`, `impact-spirit` và ba bản `-fire`; `death`, `death-fire` |
| T4 | −15 … −12 | −13,5 | `release`, `release-k1`, `release-k1-fire`, `release-k2`, `release-guard`, `release-dash`, `release-k4` |
| T5 | −12 … −9 | −11,5 | `release-k5`, `release-k7`, `release-k7-fire`, `world-open`, `world-open-fire`, `world-close`, `world-close-fire` |
| T6 | −10 … −8 | −9 | `world-climax`, `world-climax-fire` (cao trào, chỉ một) |
| voice | — | giữ nguyên | mọi `callout*` (trim 0 dB, không gộp gain tĩnh) |

Đích T5 là −11,5 (không phải −10,5): `world-climax` bị trần true peak giữ ở −10,6, nên mọi T5 phải nằm dưới nó ít nhất 0,9 LU (D5).

- **Gain tĩnh của một sự kiện** (dB): `staticDb(id) = 20·log10(NOMINAL_GAIN[id] × BUS_GAIN[bus(id)] × MASTER_GAIN)`.
  - `bus(id)`: `callout*` là `voice`, `world-*` là `world`, còn lại là `combat`.
  - `NOMINAL_GAIN` là gain mà `on()` cho ở lần phát chuẩn của sự kiện:
    - `cast` 0,5; `flyby*` 0,55; `death*` 0,6 (take đầu xô);
    - `impact-*` 0,9 (một đòn đứng riêng, `power` 1);
    - `release-auto` 0,6; `release-k5` 1 (ultimate); mọi `release*` khác 0,85 (skill, `release` dự phòng cũng vậy);
    - `world-open*`, `world-close*` 0,85; `world-climax*` 1.
  - Bản `-fire` dùng số của bản gốc.
- **Trim của một sự kiện** (dB): `trim = min(đích − mMax, −1,0 − tp) − staticDb(id)`. Làm tròn 0,1 dB.
  - Như vậy mức khi phát (`mMax + trim + staticDb`) tới đích, và true peak khi phát không vượt −1 dBTP. Trim có thể dương (gain > 1 trên nút `volume` là hợp lệ).
  - Khi số hạng thứ hai nhỏ hơn thì ghi `capped: true` cùng số thiếu (LU) = `(đích − mMax) − (−1,0 − tp)`. Ví dụ có thể đoán trước: `world-climax` (mMax −10,6, tp −1,0, `staticDb` −2,33) có trim +2,3, phát ở −10,6, thiếu 1,6 LU. Chỗ này cần bản render có limiter làm sau, không phải việc của phiếu này.
  - Ví dụ kiểm tay: `impact-flesh` (mMax −10,6, tp −1,1, `staticDb` −3,77) có trim −3,6, phát ở −18,0.
  - Lấy `mMax` và `tp` từ `tests/lab/fixtures/sound-audit-summary.json` (mục 4 `trims` tạo nó). Sự kiện có ở bảng mà không có trong JSON (chẳng hạn chưa có file) thì trim 0, ghi `missing: true`.
  - Fixture là `summary-by-event.json` của đánh giá, chỉ thay dòng `release-k7` bằng số đo của file mới `release-k7/03a.ogg` (mục 2). Gộp như đánh giá: `mMax` lớn nhất và `tp` lớn nhất qua các take trong `manifest.next.json`; ở đây chỉ có một take. `release-k5` giữ số cũ, vì file của nó không đổi.
- **Export:**
  - `SOUND_TIER: Record<string, "T2" | "T3" | "T4" | "T5" | "T6" | "voice">`;
  - `TIER_TARGET`;
  - `BUS_GAIN` và `MASTER_GAIN` (0,9) chuyển từ `sound.ts` sang đây; `sound.ts` import lại, không giữ bản chép thứ hai;
  - `NOMINAL_GAIN`, `staticDb(id)`;
  - `SOUND_TRIM_DB: Record<string, number>`: bảng sinh sẵn. Công cụ ở mục 4 in bảng này và kiểm khớp. Ghi cứng số vào mã kèm chú thích nguồn đo, để lab không phải đọc JSON lúc chạy;
  - `trimGain(id: string): number`, bằng `10 ** (SOUND_TRIM_DB[id] / 20)`, và 1 khi không có trong bảng.
- **Áp trim:** trong `LabSound.play`, nhân `trimGain(use)` vào `gain`, với `use` là id thật sau `resolve` (bản `-fire` có trim riêng). Áp cho cả đường live lẫn đường `record` (`SoundTake.gain` đã gồm trim). Các hệ số động (`power`, xô, `tier`) và các gain tĩnh trong `on()` giữ nguyên; trim đã bù phần tĩnh ở lần phát chuẩn. Một impact `power` 0 vì thế phát thấp hơn đích khoảng 5 dB; đó là chủ ý.

### 2. Bỏ đoạn dâng: chỉ `release-k7/03` (file mới, giữ bản cũ)
Vì sao chỉ một take (Claude đo lại, cùng cách đo của đánh giá, ra đúng số cũ):
- Trong `release-k5/01`, `02` và `release-k7/01`, `02`, đỉnh RMS là cuối lớp `tt-sfx-sword-river-swell`. Lớp này là tiếng dâng đảo ngược, lên tới tận cuối file: đỉnh nằm 80–170 ms trước khi file hết.
- Cắt ở `tPeak − 30 ms` chỉ giữ 0,11 s hoặc 0,21 s. Cả lớp cast hay rút kiếm mất, chỉ còn đuôi của tiếng dâng: momentary max còn −13,2 / −10,4 (k5) và −14,9 / −11,6 (k7).
- `release-k5/03` giữ 1,33 s nhưng còn −14,2 (cũ −9,2), và ở +500 ms chỉ còn −33 dB dưới đỉnh. Không đạt luật tắt chậm (audio.md §5.10: T4–T6 không thấp hơn −30 dB ở +500 ms).
- Chỉ `release-k7/03` còn thân sau khi cắt: bỏ 0,109 s, giữ 2,85 s, −8,3 (cũ −8,4), −11 dB ở +500 ms.

Quyết:
- `release-k7`: một take mới, `03a.ogg`, cắt từ `03.ogg`. `manifest.next.json` ghi `"release-k7": ["03a.ogg"]`. Take 01 và 02 (kết bằng tiếng dâng) ra khỏi manifest mới; file của chúng vẫn giữ nguyên.
- `release-k5`: **không cắt** ở phiếu này, giữ 01–03 trong `manifest.next.json`. Dựng lại từ stem (cast làm đầu, bỏ tiếng dâng hay đảo nó) là việc thiết kế âm của phiếu sau. Anh cũng có thể quyết giữ tiếng dâng cho ultimate như đoạn dồn lực vào `world-open`. Ghi việc này là nợ còn mở trong báo cáo.

Các bước, cho `release-k7/03.ogg`:
1. Giải mã sang mono 16 kHz. Tính đường bao RMS cửa sổ 10 ms, bước 1 ms. `tPeak` là thời điểm **đầu** cửa sổ có RMS lớn nhất (dự kiến khoảng 0,139 s). `atk` ở bước 4 đo cùng quy ước này.
2. `start = max(0, tPeak − 0,030 s)` (dự kiến khoảng 0,109 s).
3. Từ file gốc, giữ đủ kênh và 48 kHz:
   `-af "atrim=start=<start>,asetpts=PTS-STARTPTS,afade=t=in:d=0.003" -c:a libopus -b:a 128k 03a.ogg`.
   - `asetpts` là bắt buộc. Thiếu nó, `atrim` giữ mốc thời gian gốc, `afade` (mặc định `st` 0) đã chạy xong từ trước, và file bắt đầu bằng một cú cắt cứng (tiếng click).
   - libopus vì bản ffmpeg 9.0.2 trên máy không có libvorbis (chỉ có `vorbis` thử nghiệm) và không có `oggenc`. File đang có cũng là Opus trong Ogg, 48 kHz stereo, khoảng 125 kb/s.
   - Không đổi gì ở phần sau đỉnh.
4. Đo lại file mới bằng `measure`: `atk` (từ lúc đường bao vượt −20 dB dưới đỉnh tới đỉnh), `mMax` và `tp` bằng `ebur128=peak=true` như đánh giá, cùng mức đường bao ở +500 ms sau đỉnh mới. Ghi số vào báo cáo.
5. **Chốt chặn** (lệnh `attack` kiểm sau khi ghi file; hỏng một điều thì xóa chính file vừa ghi, dừng và báo cáo):
   - độ dài mới ≥ 1,0 s;
   - đường bao ở +500 ms sau đỉnh mới ≥ đỉnh − 30 dB;
   - `|mMax mới − mMax take gốc|` ≤ 1,5 LU;
   - `atk` ≤ 30 ms;
   - `tp` ≤ −1,0 dBTP.

   Claude đã mô phỏng bằng WAV (chưa qua Opus): 2,847 s, −8,3 LUFS, −2,1 dBTP, `atk` 30 ms, −11 dB ở +500 ms. Cả năm điều đều qua.
6. `manifest.next.json`: bản chép của `manifest.json`, chỉ đổi `release-k7` sang `["03a.ogg"]`. `release-k5` và `release-k7-fire` giữ nguyên (`release-k7-fire` đã lên trong 393 ms).

`release-k7` giờ chỉ còn một take; rate ±5 % của lab vẫn tạo chút khác biệt. Take 01 và 02 của `release-k5` hết 80–170 ms sau đỉnh. Phần tắt chậm của cả hai do send vang ở mục 3 gánh, với mức send riêng cao hơn (0,4).

### 3. Send vang chung
- **Đồ thị** (tạo trong `unlock()`, một lần): bus `verb` gồm
  `DelayNode` (0,025 s) → `BiquadFilterNode` highpass 200 Hz → `ConvolverNode` (`normalize = true`, buffer = IR) → `BiquadFilterNode` lowpass 6500 Hz → `GainNode` (`VERB_RETURN` = 0,7) → `master`.
  - **Q của hai bộ lọc là `−3.0103`**, không phải 0,707. Với lowpass và highpass, Web Audio hiểu Q theo dB (spec W3C: "the Q value is interpreted to be in dB"). −3,0103 dB là Q tuyến tính 0,7071 (Butterworth, −3 dB ở tần số cắt), khớp mặc định `t=q:w=0.707` của ffmpeg. Q 0,707 dB sẽ là Q tuyến tính 1,085, lồi +0,7 dB ở tần số cắt, lệch bản quay khoảng 3,7 dB.
- **Mỗi take:** sau `panner`, một nhánh `GainNode` (mức send `SEND_LEVEL[use]`) nối vào đầu bus `verb`, song song với đường khô vào bus của nó. Nhánh này rẽ **trước** gain bus, nên đường ướt = file × gain (đã gồm trim) × pan × send.
- **Hush:** `duck()` hạ cả nút `VERB_RETURN` cùng các bus: xuống 8 % trong 12 ms, giữ, về lại `VERB_RETURN` trong 10 ms, cùng hình dạng. Hush là khoảng gần im lặng trước cao trào; đuôi vang 2,2 s mà không bị hạ thì sẽ lấp kín nó (audio.md §5.4 cũng hạ return dưới lời nói).
- **Mức send theo sự kiện (`SEND_LEVEL`):**
  - `impact-*` 0,05;
  - `death*` 0,1;
  - `cast` 0,05; `flyby*` 0,1; `release-auto` 0,1;
  - các `release-*` bậc T4 0,25;
  - `release-k5`, `release-k7`, `release-k7-fire` 0,4;
  - `world-open*`, `world-close*` 0,4; `world-climax*` 0,45;
  - `callout*` 0,08.
- **IR:**
  - Chưa có IR thu thật. Phiếu này tạo một IR xác định, lưu thành file `ir/hall-a.wav` (48 kHz, stereo, 2,4 s, 16 bit), kèm `ir/hall-a.json` ghi thuật toán, hạt giống và số đo.
  - Thuật toán: hai kênh nhiễu trắng độc lập, hạt giống cố định (`mulberry32(0x7ab1e)` kênh trái, `mulberry32(0x7ab1f)` kênh phải), nhân bao `exp(−6,91·t/RT60)` với RT60 = 2,2 s. 8 ms đầu là 0 (pre-delay của IR). Mép sau mờ dần 50 ms cuối. Chuẩn hóa đỉnh −1 dBFS.
  - `hall-a.json` ghi thêm `webAudioScale` S: hệ số mà `ConvolverNode` (`normalize = true`) nhân vào IR, tính từ chính các mẫu 16 bit đã ghi của `hall-a.wav` ở 48 kHz theo thuật toán của spec W3C:
    - `power = sqrt(Σ mọi kênh h² / (số kênh × số mẫu))`; nếu nhỏ hơn 0,000125 (hoặc không hữu hạn) thì lấy 0,000125;
    - `S = 0,00125 × 44100 / 48000 / power` (hệ số 0,5 cho IR 4 kênh không áp dụng);
    - dự kiến khoảng 0,0086.
  - `sound.ts` nạp IR này như mọi file (`fetch` rồi `decodeAudioData`). Chưa nạp xong thì send không kêu, đường khô vẫn chạy.
  - Ghi trong báo cáo và changelog: IR là bộ xử lý, không phải âm thay thế. Khi có IR thu thật (CC0), chỉ cần thay file. **Anh nghe và quyết** IR này có đạt không.
- **`SoundTake`** thêm trường `send: number`. Bản quay phải mix được giống live.
  - `send = SEND_LEVEL[use] / BUS_GAIN[bus]`. Lý do: `SoundTake.gain` đã gồm gain bus, còn nhánh send live rẽ trước bus. Nhân `gain × send` offline thì ra đúng `gain sự kiện × trim × SEND_LEVEL` như live.
  - Chú thích trường này trong mã nói rõ điều đó.
- **`mix-lab-sound.mjs`:**
  - dựng nhánh ướt: mỗi take, sau gain, pan và rate, tách (`asplit`) một bản nhân `send` vào track `wet`;
  - track `wet` phủ **hết độ dài đầu ra**: cộng các bản ướt với một nền `anullsrc` dài `duration` (`amix … normalize=0`), vì `afir` chỉ cho ra dài bằng đầu vào (audio.md §5.7 Gotchas). Thiếu nền này thì đuôi 2,4 s bị cắt sau take cuối;
  - track `wet` qua: `adelay` 25 ms → `highpass=f=200:t=q:w=0.7071` → `afir=irnorm=-1:irgain=1` với `ir/hall-a.wav` → `volume=<S>` (S đọc từ `hall-a.json`) → `lowpass=f=6500:t=q:w=0.7071` → `volume=0.7`;
    - `irnorm=-1` để `afir` không đổi IR (mặc định `irnorm=1` chia IR cho chuẩn L1, lệch hàng chục dB so với live); `volume=S` làm đúng việc `normalize = true` làm trong Web Audio;
  - cộng `wet` vào các track khô **trước** `aeval` của hush, để hush hạ cả hai, như live (ở trên). Sau đó master 0,9 và limiter như cũ;
  - IR ở `<root>/art-src/lab/audio/ir/hall-a.wav` (cờ `--ir=<file>` đổi được). Có take với `send` > 0 mà thiếu IR thì dừng và báo lỗi, không im lặng bỏ nhánh ướt;
  - `duration` mặc định: `lastEnd + 0,025 + độ dài IR` khi có take `send` > 0, còn không thì `lastEnd + 0,25` như cũ;
  - take không có `send` (bản quay cũ) thì `send` = 0.

### 4. Công cụ `scripts/audio/lab-sound-tiers.mjs`
- `measure <file…>`: in `mMax`, `tp`, `atk`, `t40` và mức ở +500 ms sau đỉnh của từng file, cùng cách đo với đánh giá (ebur128 `peak=true`, đệm 1 s im lặng cho momentary; đường bao RMS 10 ms ở 16 kHz mono). Chạy trên ba take cũ của `release-k7` phải ra lại số của `measurements.json` (mMax −8,4 / −7,6 / −8,4; tp −2,7 / −1,5 / −2,1); lệch quá 0,1 thì dừng.
- `trims`:
  - dựng fixture: `summary-by-event.json` của đánh giá, giữ `id`, `mMax`, `tp`; thay dòng `release-k7` bằng số đo của `release-k7/03a.ogg` (gộp như đánh giá: `mMax` lớn nhất, `tp` lớn nhất qua các take của `manifest.next.json`). Ghi `tests/lab/fixtures/sound-audit-summary.json`, kèm trường `source` ghi hai nguồn này;
    - ghi lại fixture **ở mỗi lần chạy** (ghi đè, không cần cờ). Kết quả xác định: cùng nguồn thì ra cùng byte. Vì thế JSON không có dấu thời gian hay trường nào đổi giữa các lần chạy; thứ tự dòng theo `id`, thứ tự khóa cố định;
    - in `fixture: created` (chưa có file), `fixture: unchanged` hoặc `fixture: changed` (so từng byte với bản trước). Số lệch thì bước kiểm bảng dưới đây bắt;
  - in bảng trim theo công thức mục 1 (có `staticDb`, `capped`, `missing`), cùng mức khi phát của từng sự kiện;
  - thoát khác 0 nếu bảng trong `sound-tiers.ts` lệch quá 0,05 dB so với bảng vừa tính.
- `attack <event>/<file>…`: làm mục 2 cho từng file được nêu (phiếu này chỉ chạy `release-k7/03.ogg`), có chốt chặn ở mục 2 bước 5.
- `ir`:
  - làm IR ở mục 3, tính S và ghi `hall-a.json`;
  - in RT60 đo lại bằng tích phân Schroeder (T30), phải nằm trong 2,2 ± 0,15 s;
  - kiểm `afir` (kiểm xung): một xung đơn vị 48 kHz stereo **dài 2,5 s** (dài hơn IR 2,4 s; `afir` chỉ cho ra dài bằng đầu vào, xung 0,5 s mất 0,20 dB năng lượng của S × h):
    `ffmpeg -f lavfi -i "aevalsrc='if(eq(n,0),1,0)|if(eq(n,0),1,0)':s=48000:d=2.5" -i hall-a.wav -filter_complex "[0:a][1:a]afir=irnorm=-1:irgain=1,volume=<S>" -f f32le <out>`
    (hay xung ngắn hơn rồi `apad=whole_dur=2.5`). Đầu ra phải bằng S × h, với h là các mẫu 16 bit của `hall-a.wav` chia 32768:
    - năng lượng mỗi kênh (cộng hết đầu ra so với cộng hết S × h) lệch ≤ 0,1 dB;
    - **onset** của mỗi kênh là mẫu đầu tiên có |v| > đỉnh của kênh đó − 60 dB (|v| > 0,001 × đỉnh). Onset phải trùng chỉ số mẫu khác 0 đầu tiên của h trong file, tức 384 (8 ms ở 48 kHz), ở cả hai kênh;
    - **không** so `!== 0`: `afir` nhân chập bằng FFT, nên 8 ms pre-delay của đầu ra không đúng bằng 0 (Claude đo trên ffmpeg 9.0.2: 358–368 trong 384 mẫu đầu khác 0, lớn nhất khoảng 1e−9).
    Claude đã thử đúng lệnh trên (IR làm theo mục 3, S 0,008595): năng lượng lệch 0,0000 dB, onset 384 ở cả hai kênh, `irnorm=-1` giữ nguyên IR.
  - `hall-a.json` ghi S và RT60 đo được ở đủ độ chính xác của số double (không làm tròn), để `--check` so được.
- `ir --check`: **không ghi gì**. Dùng cho Kiểm 6 và mọi lần chạy lại:
  - đọc `ir/hall-a.wav` và `ir/hall-a.json` đang có; thiếu một trong hai thì thoát khác 0;
  - đo lại RT60 (T30) từ file: trong 2,2 ± 0,15 s và lệch số trong json ≤ 0,01 s;
  - tính lại S từ các mẫu 16 bit của file theo công thức mục 3: lệch tương đối so với S trong json ≤ 1e−6;
  - chạy lại kiểm xung `afir` ở trên (dùng S của json, cùng xung 2,5 s, cùng định nghĩa onset theo ngưỡng −60 dB, không so `!== 0`);
  - in cả ba số; hỏng một điều thì thoát khác 0.
- Mọi lệnh ffmpeg in ra trước khi chạy.
- **Không ghi đè** chỉ áp cho file trong `art-src`: `release-k7/03a.ogg` và `manifest.next.json` (lệnh `attack`), `ir/hall-a.wav` và `ir/hall-a.json` (lệnh `ir`). File đã có thì dừng và thoát khác 0, trừ khi có `--force`. `--force` chỉ ghi đè chính bốn file này, không bao giờ file âm cũ hay `manifest.json`. Fixture trong repo do `trims` ghi lại mỗi lần (ở trên), không theo luật này.

### 5. Test `tests/lab/sound-tiers.test.ts` (Node, không WebAudio)
1. Mọi id trong `SOUND_IDS` và mọi id kết bằng `-fire` trong fixture `tests/lab/fixtures/sound-audit-summary.json` đều có bậc trong `SOUND_TIER` (test không đọc ngoài repo, như test 3).
2. `trimGain` khớp `10 ** (dB/20)`, và bằng 1 với id lạ.
3. Với số trong `tests/lab/fixtures/sound-audit-summary.json` (fixture của mục 4; test không đọc ngoài repo), bảng `SOUND_TRIM_DB` theo đúng công thức mục 1, kể cả `staticDb` và trần true peak, lệch ≤ 0,05 dB.
4. **Thứ bậc khi phát** (`mMax + trim + staticDb`, số từ fixture):
   - mọi T3 < mọi T4 < mọi T5 ≤ T6 lớn nhất;
   - không sự kiện nào ngoài T6 và voice to hơn `world-climax` (dự kiến: T5 ở −11,5, `world-climax` ở −10,6).
5. `LabSound` ở chế độ ghi (`record()`), với file giả (đặt `files` qua manifest giả bằng `fetch` stub):
   - với `cast`, `release-auto`, `release-k1`, `release-k5`, `flyby`, `impact-flesh` (`power` 1), `death`, `world-open`, `world-climax`: `SoundTake.gain` = `NOMINAL_GAIN[id]` × `BUS_GAIN[bus]` × `trimGain(id)`. Kiểm này giữ `NOMINAL_GAIN` khớp các số trong `on()`;
   - `send` = `SEND_LEVEL[id] / BUS_GAIN[bus]`.

## Kiểm bắt buộc (trong `games/.wt-ic-sound`)
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua. Ghi số test trước và sau.
3. Xóa `/private/tmp/codex-269-dist` nếu có, rồi `IC_VITE_CACHE_DIR=/private/tmp/codex-269-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-269-dist --configLoader runner`: thoát 0. `grep -rl "SOUND_TRIM_DB\|hall-a" /private/tmp/codex-269-dist` phải không in gì (lab không vào bản dựng). Xóa thư mục sau khi kiểm.
4. `node scripts/audio/lab-sound-tiers.mjs trims`: thoát 0 (chạy lại bao nhiêu lần cũng được; lần chạy kiểm phải in `fixture: unchanged`). Báo cáo dán bảng trim, đánh dấu `capped` và `missing`.
5. `node scripts/audio/lab-sound-tiers.mjs measure` trên `release-k7/03a.ogg`: đạt cả năm chốt chặn ở mục 2 bước 5 (dài ≥ 1,0 s; +500 ms ≥ đỉnh − 30 dB; mMax trong ±1,5 LU của take gốc; `atk` ≤ 30 ms; `tp` ≤ −1,0 dBTP). Dán số vào báo cáo, cạnh số của `03.ogg`.
6. `node scripts/audio/lab-sound-tiers.mjs ir --check` (sau khi `ir` đã tạo file đúng một lần): thoát 0; RT60 2,2 ± 0,15 s; S tính lại khớp `hall-a.json`; kiểm xung `afir` (xung 2,5 s) lệch năng lượng ≤ 0,1 dB mỗi kênh, onset (ngưỡng đỉnh − 60 dB) ở mẫu 384 cả hai kênh. Dán số, cả onset từng kênh. Không chạy lại `ir` không có `--check` để kiểm.
7. `git -C games/.wt-ic-sound diff --stat` và `status --short`: chỉ các file được ghi (fixture nằm trong danh sách). `ls` các file mới trong `art-src/lab/audio/`: chỉ `release-k7/03a.ogg`, `ir/hall-a.wav`, `ir/hall-a.json`, `manifest.next.json`. `md5` của `manifest.json` và của sáu file `release-k5/0N.ogg`, `release-k7/0N.ogg` trước và sau: phải không đổi.

## Claude làm sau
- Đọc diff, chạy lại Kiểm 1–7 (Kiểm 4 chạy lại `trims`; Kiểm 6 bằng `ir --check`, không chạy lại `ir`).
- Dev server của worktree (cấu hình bọc có `server.fs.allow`, như phiếu 258). Chép `manifest.next.json` sang `manifest.json` của bản thử (giữ bản cũ).
- Quay cảnh lab có tiếng (`__lab.soundRecord()`, `mix-lab-sound.mjs`). Phím theo `KEYS` của `src/lab/skills-main.ts` (dòng 1104; `tierOf` dòng 287–288), không theo bản đánh giá. Mỗi phím phát nhiều sự kiện chồng nhau (số dòng ở `main` 2381c7b, giống 35f1b77):
  - phím 1 (ô `k1`): `release-k1` và `callout-k1` cùng khung (`emitRelease`, dòng 356–377);
  - phím 6 (ô `k5`, ultimate) phát bốn sự kiện:
    - lúc cut-in bắt đầu: `callout-k5` và `world-open` (`startUltimate`, dòng 727–728);
    - khi cut-in xong: `release-k5` (`ULT_HOLD` mặc định 1,7 s, dòng 697; `fireUltimate` dòng 738–743, gọi ở dòng 1261);
    - ở đòn kết: `world-climax` (`screenImpact`, dòng 312).
    - Theo `measurements.json`, `world-open` lên đỉnh 1,5–3,4 s sau lúc cut-in bắt đầu, `release-k5` lên đỉnh 3,4–4,5 s: hai cái chồng nhau;
  - phím 7 (ô `k7`): `release-k7` và `callout-k7` cùng khung (dòng 978); `world-open` một tick sau `myriad.cast()` (`T_SEAM`, `src/view/skills/myriad-swords.ts` dòng 134), rồi hush, `world-climax` ở `T_FIN` (3,2 s), `world-close` (skills-main dòng 646–661). `callout-k7` lên đỉnh 0,48 s sau `release-k7`;
  - phím 5 là ô `k4`, không dùng.
- **Đo mức từng sự kiện trên bản trộn chỉ có take của nó:** lọc `takes.json` theo `url` (chẳng hạn chỉ take có `/release-k5/`), rồi mới chạy `mix-lab-sound.mjs`, rồi đo momentary max. Không đo mức một sự kiện trên bản trộn đủ: cửa sổ 400 ms gộp cả các sự kiện chồng ở trên, cùng vang của chúng.
  - Nhánh ướt của chính take giữ nguyên. Ước tính từ S và mức send, nó thêm khoảng 0,1 LU.
  - Đích của một take = đích bậc − (mMax của sự kiện − mMax của take đó trong `measurements.json`), ± 1 LU. Trim tính theo take to nhất, nên take nhỏ hơn phát thấp hơn đích. Ví dụ `impact-flesh/02` thấp hơn 1,6 LU, `release-k5/03` thấp hơn 0,7 LU.
  - Các mức cần đạt:
    - một impact ở `power` 1: −18 ± 1 LU theo cách tính trên (ở `power` 0 thấp hơn khoảng 5 dB, do hệ số động);
    - `release-k7` (một take, `03a`): −11,5 ± 1 LU;
    - `release-k5`: −11,5 ± 1 LU theo cách tính trên (file chưa cắt, vẫn dâng 2,1 s; chỉ kiểm mức);
    - `world-climax`: lớn nhất trong các sự kiện không phải voice.
- Trên bản trộn đủ của phím 6 và phím 7, ghi momentary max theo thời gian và chỗ nó xảy ra. Nếu cửa sổ `release-k7` + `callout-k7` (hay cut-in của phím 6) to hơn `world-climax`, ghi thành nợ mở: voice chưa hạ các bus khác, trim voice là 0 dB. Không sửa ở phiếu này.
- Nghe `release-k7/03.ogg` cạnh `03a.ogg`: nếu cú cắt 0,109 s làm mất tiếng rút kiếm ở đầu thì dùng `03.ogg` (lên đỉnh trong 120–140 ms) và ghi lại.
- Gửi anh video có tiếng để nghe. Chỉ gộp sau khi anh nghe.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
Thay đổi trong worktree, chưa commit; file âm mới trong `art-src`. Claude đọc diff, chạy lại kiểm, quay cảnh có tiếng, rồi mới commit.

## Phản biện

### Vòng 1 (04/11, 20:50): một agent Claude độc lập, 10 lỗi D1–D10; Claude kiểm từng lỗi ở mã và nguồn
Nhận cả 10; không bác lỗi nào. D8 nhận nhưng sửa phần hush theo cách khác. D1 và D10 là chỗ Claude chốt.

| Lỗi | Kiểm ở đâu | Kết luận | Đã sửa |
|---|---|---|---|
| D1 (P0) cắt ở đỉnh RMS phá 4/6 take | Mô phỏng lại mục 2 (đệm 1 s như đánh giá, số cũ ra đúng). Mới: k5 −13,2 / −10,4 / −14,2, k7 −14,9 / −11,6 / −8,3; độ dài giữ lại 0,112 / 0,206 / 1,33 s (k5) và 0,112 / 0,206 / 2,85 s (k7). `SOURCES.json`: k5 = swell + magic-cast, k7 = sword-draw + swell. Đường bao 100 ms của stem cho thấy swell là tiếng dâng đảo ngược, lên tới tận cuối file. | Đúng | Mục 2: chỉ cắt `release-k7/03` thành `03a`, manifest mới chỉ có take này. `release-k5` không cắt, ghi nợ dựng lại từ stem. Thêm năm chốt chặn cho `attack`, Kiểm 5 và 7 theo đó. |
| D2 không có libvorbis | `ffmpeg -encoders` (9.0.2): chỉ `vorbis` thử nghiệm, `libopus`, không có `oggenc`; audio.md §5.7 Gotchas; ffprobe `release-k5/01.ogg`: opus 48 kHz stereo, 124,8 kb/s. | Đúng | `-c:a libopus -b:a 128k`. |
| D3 `afade` không chạy sau `atrim` | Thử trên tín hiệu hằng 0,5: không có `asetpts`, mẫu đầu = 0,5; có `asetpts=PTS-STARTPTS`, dốc 0 → 0,0035 → 0,0069. | Đúng | Thêm `asetpts=PTS-STARTPTS`, ghi lý do. |
| D4 fixture ngoài "Được ghi"; test 3 lệch §1 | Phiếu cũ: test 3 nêu fixture, "Được ghi" thiếu, "Cấm" và Kiểm 7 chặn. | Đúng | Fixture vào "Được ghi". `trims` dựng nó (thay `release-k7` bằng số của `03a`, gộp max như đánh giá). Test 3 và 4 đọc nó. |
| D5 T5 −10,5 to hơn `world-climax` −10,6 | Tính lại: mọi T5 tới −10,5, `world-climax` bị trần giữ ở −10,6. | Đúng | Đích T5 −11,5; mọi T5 dưới cao trào 0,9 LU, mọi T4 ở −13,5 vẫn dưới T5. |
| D6 Q của biquad | Spec Web Audio 1.1 (đọc 04/11): "For lowpass and highpass filters the Q value is interpreted to be in dB", `α = sin ω0 / (2·10^(Q/20))`. `ffmpeg -h filter=highpass`: mặc định `t=q`, `w=0.707`. | Đúng | Web Audio Q = −3,0103; ffmpeg ghi rõ `t=q:w=0.7071`. |
| D7 gain của `afir` mơ hồ | `ffmpeg -h filter=afir`: `irnorm` mặc định 1, `irgain` 0–1. Thử xung: IR 0,5 và 0,25 ra 0,667 và 0,333 (chuẩn L1); `irnorm=-1` ra đúng 0,5 và 0,25, không trễ. Spec: `GainCalibration` 0,00125, `GainCalibrationSampleRate` 44100, `MinPower` 0,000125. | Đúng | `afir=irnorm=-1:irgain=1,volume=S`, S tính theo spec, ghi vào `hall-a.json`; thêm kiểm xung ≤ 0,1 dB. |
| D8 send offline lệch bus; hush | `sound.ts`: `record` ghi `gain * BUS_GAIN[bus]`; nhánh send live rẽ sau `panner`, trước bus. | Đúng | `send = SEND_LEVEL / BUS_GAIN`. Hush: critic đề nghị cộng nhánh ướt sau `aeval` cho khớp live. Claude chọn cách khác: cho `duck()` hạ cả `VERB_RETURN` live, và cộng nhánh ướt trước `aeval` offline. Hai bên vẫn khớp nhau, và hush giữ đúng nghĩa gần im lặng (đuôi 2,2 s không lấp nó). |
| D9 đuôi vang bị cắt | audio.md §5.7 Gotchas (`afir` dài bằng đầu vào); `mix-lab-sound.mjs`: `duration` mặc định `lastEnd + 0.25`. | Đúng | Track `wet` có nền `anullsrc` dài `duration`; mặc định `lastEnd + 0,025 + độ dài IR` khi có send. |
| D10 gain tĩnh làm mức khi phát lệch bậc | `on()`: cast 0,5, flyby 0,55, death 0,6, impact 0,5–0,9, release 0,6 / 0,85 / 1, world 0,85 / 1; bus 0,8 / 0,85 / 0,95; master 0,9. Impact `power` 1 phát ở −21,8, `world-climax` ở −12,9. audio.md §5.4 đòi gain gần 1 để file mang đúng nghĩa. | Đúng | Chọn (a): `trim = min(đích − mMax, −1 − tp) − staticDb(id)`. Trần true peak tính ở mức khi phát. `NOMINAL_GAIN`, `BUS_GAIN`, `MASTER_GAIN` nằm trong `sound-tiers.ts`; test 5 giữ chúng khớp `on()`. Kiểm trên bản trộn ghi lại theo mức khi phát. |

Claude ghi thêm (ngoài danh sách của critic):
- Theo D10, mỗi âm khi phát có true peak tới −1 dBTP. Ví dụ `world-climax` trước đây phát ở khoảng −3,3 dBTP.
- Live chưa có limiter an toàn ở master, nên nhiều âm chồng nhau có thể vượt 0 dBFS. Bản quay offline đã có limiter.
- Limiter master live (audio.md §5.8) để phiếu sau; Claude nghe bản live khi chạy dev server ở bước "Claude làm sau".
- Cắt 0,109 s đầu của `release-k7/03` có thể mất đoạn mở của tiếng rút kiếm. Claude nghe so `03` với `03a` trước khi chốt manifest.

### Vòng 2 (04/11, 21:05): một agent Claude độc lập, 3 lỗi E1–E3; Claude kiểm từng lỗi ở mã và nguồn
Nhận cả 3; không bác lỗi nào. Chưa có `269-report.md` (Codex chưa nhận phiếu), nên sửa thẳng trong phiếu.

| Lỗi | Kiểm ở đâu | Kết luận | Đã sửa |
|---|---|---|---|
| E1 (vừa) luật không ghi đè chặn chạy lại `trims` và `ir` | Phiếu cũ, mục 4 dòng cuối: luật áp cho mọi file công cụ ghi, `--force` chỉ cho file mục 2 và 3. `trims` ghi fixture mỗi lần và phải chạy ít nhất hai lần (lần đầu lấy bảng để ghi cứng vào `SOUND_TRIM_DB`, rồi Kiểm 4, rồi Claude chạy lại Kiểm 1–7), nên từ lần hai nó dừng. Chạy lại `ir` cho Kiểm 6 cũng gặp `hall-a.wav` đã có. | Đúng | Chọn (a) + (b) + (c) của critic: luật không ghi đè chỉ áp cho bốn file trong `art-src`, kể tên theo lệnh; `trims` luôn ghi lại fixture, kết quả xác định (không dấu thời gian, thứ tự cố định), in `created` / `unchanged` / `changed`; thêm `ir --check` chỉ đọc (RT60, S tính lại so json ≤ 1e−6, kiểm xung). Kiểm 4 ghi rõ chạy lại được và phải `unchanged`; Kiểm 6 và "Claude làm sau" dùng `ir --check`. `hall-a.json` giữ S và RT60 không làm tròn để so được. |
| E2 (thấp) "phím 5 (ultimate)" sai | `src/lab/skills-main.ts` ở `main` 2381c7b, dòng 1104: `KEYS` = `"5": "k4"`, `"6": "k5"`, `"7": "k7"`; dòng 287–288 `tierOf`: `k5` → `ultimate`. `sound.ts` dòng 324: `release-<slot>` với gain 1 khi `tier` là `ultimate`. Bản đánh giá dòng 14 ghi "dash (ô 6)", "ultimate = k7": sai so với `KEYS`. Bậc màn hình ultimate là `k5`. `world-*` thì cả hai ô cùng phát: `k7` ở dòng 646–661, `k5` phát `world-open` ở dòng 728 và `world-climax` ở dòng 312 (vòng 2 ghi sai là chỉ `k7`; sửa ở vòng 3, F2). | Đúng | "Claude làm sau": phím 1 (`k1`), phím 6 (`k5`, ultimate), phím 7 (`k7`), dẫn `KEYS` làm nguồn; thêm kiểm mức `release-k5` −11,5 ± 1 LU. Vòng 3 (F2) ghi đủ các sự kiện mỗi phím phát và đo mức trên bản trộn chỉ có take của sự kiện. |
| E3 (thấp) test 1 đọc file ngoài repo | Test 3 cấm đọc ngoài repo; `summary-by-event.json` ở `typing-game-review`. Fixture (34 dòng) có đủ 10 id `-fire` của bản đánh giá: `death`, `flyby`, ba `impact-*`, `release-k1`, `release-k7`, ba `world-*`. | Đúng | Test 1 lấy các id `-fire` từ `tests/lab/fixtures/sound-audit-summary.json`. |

Claude ghi thêm (ngoài danh sách của critic):
- Tên phiếu đổi "ô 7 / ô 5" thành `release-k7` / `release-k5`, vì "ô 5" dễ đọc thành phím 5 (là `k4`).
- Bản đánh giá `SOUND_AUDIT_2026-11-04.md` dòng 14 còn ghi sai ô phím. Phiếu này không được sửa file đó; Claude sửa khi commit phiếu.

### Vòng 3 (04/11): một agent Claude độc lập, 2 lỗi F1–F2; Claude kiểm từng lỗi ở mã và nguồn
Critic đặt tên D1, D2; phiếu đổi thành F1, F2 để không trùng vòng 1. Nhận cả 2; không bác lỗi nào. Chưa có `269-report.md`, nên sửa thẳng trong phiếu.

| Lỗi | Kiểm ở đâu | Kết luận | Đã sửa |
|---|---|---|---|
| F1 (vừa) kiểm xung `afir` không chạy được như viết | Claude làm lại IR theo mục 3 (S 0,0085952, đúng số critic), chạy `afir=irnorm=-1:irgain=1,volume=S` trên ffmpeg 9.0.2, đầu ra f32. Xung 0,5 s: năng lượng −0,2018 / −0,2024 dB, đầu ra dài 24 000 mẫu. Xung 2,5 s (`aevalsrc d=2.5`, hoặc xung 0,5 s + `apad=whole_dur=2.5`): −0,0000 dB cả hai kênh. Cả hai trường hợp: mẫu khác 0 đầu tiên ở chỉ số 0 (368 và 358 trong 384 mẫu đầu khác 0, lớn nhất 1,0e−9 và 1,4e−9). Mẫu đầu tiên trên 1e−6, hay trên đỉnh − 60 dB, ở 384, trùng mẫu khác 0 đầu tiên của h. | Đúng | Mục 4 `ir`: xung 2,5 s, ghi rõ lệnh; onset là mẫu đầu tiên có \|v\| > đỉnh kênh − 60 dB, phải ở 384 cả hai kênh; cấm so `!== 0`, nêu lý do FFT. `ir --check` và Kiểm 6 dùng đúng định nghĩa này. Câu cũ "`afir` không thêm trễ" sửa thành số đo. |
| F2 (thấp) E2 sai, kiểm mức `release-k5` lẫn sự kiện khác | `skills-main.ts` ở 2381c7b và 35f1b77 (cùng số dòng): `startUltimate` phát `callout-k5` (727) và `world-open` k5 (728); `screenImpact` phát `world-climax` k5 ở đòn kết (312); `ULT_HOLD` 1,7 (697); `fireUltimate` (738–743, gọi ở 1261) phát `release-k5`. `measurements.json`: `world-open` lên đỉnh 1,51 / 3,39 / 1,67 s sau lúc cut-in bắt đầu; `release-k5` lên đỉnh 1,7 + 1,66…2,82 s. | Đúng | E2 sửa tại chỗ. "Claude làm sau" ghi đủ sự kiện của phím 1, 6, 7 cùng số dòng. Mức từng sự kiện đo trên bản trộn chỉ có take của nó (lọc `takes.json` theo `url` trước `mix-lab-sound.mjs`). |

Claude ghi thêm (ngoài danh sách của critic; cùng gốc với F2):
- Phím 7 cũng lẫn: `emitRelease` phát `callout-k7` cùng khung với `release-k7` (dòng 372–376). `callout-k7` có mMax −9,3, trim voice 0 dB, gain 1 × bus 0,95 × master 0,9, nên phát ở khoảng −10,7, lên đỉnh 0,48 s sau. `world-open` k7 đến một tick sau (`T_SEAM`). Vì thế kiểm `release-k7` cũng đo trên bản trộn chỉ có take của nó.
- Cũng vì `callout-k7` phát ngang `world-climax` (−10,6), câu cũ "`world-climax` phải là đỉnh to nhất" trên bản trộn đủ có thể hỏng chỉ vì voice. Kiểm đó chuyển sang các bản trộn riêng (lớn nhất trong các sự kiện không phải voice, như test 4). Trên bản trộn đủ, Claude chỉ ghi số và chỗ đỉnh; nếu voice cùng release to hơn cao trào thì ghi nợ mở (voice chưa hạ các bus khác).
- Trim tính theo take to nhất của sự kiện (mMax gộp max), mà các take lệch nhau tới 1,6 LU (`impact-flesh` −10,6 / −11,8 / −12,2). Kiểm ± 1 LU trên một take vì thế lấy đích riêng của take: đích bậc − (mMax sự kiện − mMax take).
- Nhánh ướt của chính take giữ trong bản trộn riêng. Ước tính: tỉ lệ biên độ ướt/khô 0,4 × 0,7 / 0,8 = 0,35, năng lượng của S × h khoảng 0,15. Nhánh ướt nhỏ hơn đường khô khoảng 17 dB, thêm khoảng 0,1 LU.
