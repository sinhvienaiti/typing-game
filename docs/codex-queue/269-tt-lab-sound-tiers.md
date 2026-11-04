# Phiếu 269 · Tu Tiên · Code và âm: mix lại âm lab theo bậc to, bỏ đoạn dâng của ô 5 và ô 7, thêm send vang chung

**Loại việc:** code và xử lý âm (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã chốt trong phiếu. Codex không thiết kế lại bậc, số hay cách đo. Chỗ nào không làm được đúng như viết thì dừng ở đó và ghi vào báo cáo.

**Báo cáo:** `docs/codex-queue/269-report.md` (tiếng Việt).

**Đường duyệt:**
- Claude viết lúc 20:45 ngày 04/11, từ `docs/games/tu-tien/skills/SOUND_AUDIT_2026-11-04.md` (số đo ffmpeg) và luật âm `.agents/skills/game-art-pipeline/references/audio.md` §5.
- Phản biện bởi agent Claude (bước 9 skill `agent-orchestration`). Ghi kết quả ở mục "Phản biện" cuối phiếu.

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
  3. **Không có send vang** trong game; chỉ có đuôi nướng sẵn.
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
- `games/.wt-ic-sound/docs/changelog/2026-11-04-lab-sound-tiers.md` (tạo mới);
- trong `art-src/lab/audio/` của game (đường tuyệt đối ở trên), chỉ các file mới:
  - `release-k5/01a.ogg`, `02a.ogg`, `03a.ogg`;
  - `release-k7/01a.ogg`, `02a.ogg`, `03a.ogg`;
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
Đích theo momentary max (LUFS) của luật §5.4. Mỗi bậc có một số đích ở giữa khoảng:

| Bậc | Khoảng | Đích | Sự kiện |
|---|---|---:|---|
| T2 | −19 … −17 | −18 | `cast`, `release-auto`, `flyby`, `flyby-fire` |
| T3 | −20 … −16 | −18 | `impact-flesh`, `impact-stone`, `impact-spirit` và ba bản `-fire`; `death`, `death-fire` |
| T4 | −15 … −12 | −13,5 | `release`, `release-k1`, `release-k1-fire`, `release-k2`, `release-guard`, `release-dash`, `release-k4` |
| T5 | −12 … −9 | −10,5 | `release-k5`, `release-k7`, `release-k7-fire`, `world-open`, `world-open-fire`, `world-close`, `world-close-fire` |
| T6 | −10 … −8 | −9 | `world-climax`, `world-climax-fire` (cao trào, chỉ một) |
| voice | — | giữ nguyên | mọi `callout*` (trim 0 dB) |

- **Trim của một sự kiện** (dB): `trim = min(đích − mMax, −1,0 − tp)`. Nghĩa là không bao giờ đẩy true peak lên trên −1 dBTP. Làm tròn 0,1 dB.
  - Một sự kiện mà trần true peak chặn không cho tới đích thì ghi `capped: true` cùng số thiếu (LU). Ví dụ có thể đoán trước: `world-climax` (mMax −10,6, tp −1,0) chỉ trim được 0, thiếu 1,6 LU. Chỗ này cần bản render có limiter làm sau, không phải việc của phiếu này.
  - Lấy `mMax` và `tp` từ `summary-by-event.json`. Sự kiện có ở bảng mà không có trong JSON (chẳng hạn chưa có file) thì trim 0, ghi `missing: true`.
  - Sự kiện `release-k5` và `release-k7` sau mục 2 dùng số đo của **file mới** (mục 2 đo lại), không dùng số cũ.
- **Export:**
  - `SOUND_TIER: Record<string, "T2" | "T3" | "T4" | "T5" | "T6" | "voice">`;
  - `TIER_TARGET`;
  - `SOUND_TRIM_DB: Record<string, number>`: bảng sinh sẵn. Công cụ ở mục 4 in bảng này và kiểm khớp. Ghi cứng số vào mã kèm chú thích nguồn đo, để lab không phải đọc JSON lúc chạy;
  - `trimGain(id: string): number`, bằng `10 ** (SOUND_TRIM_DB[id] / 20)`, và 1 khi không có trong bảng.
- **Áp trim:** trong `LabSound.play`, nhân `trimGain(use)` vào `gain`, với `use` là id thật sau `resolve` (bản `-fire` có trim riêng). Áp cho cả đường live lẫn đường `record` (`SoundTake.gain` đã gồm trim). Các hệ số động hiện có (`power`, xô, `tier`) giữ nguyên: chúng là tương quan trong bậc.

### 2. Bỏ đoạn dâng của `release-k5` và `release-k7` (file mới, giữ bản cũ)
Với mỗi take `release-k5/0N.ogg` và `release-k7/0N.ogg` (N = 1..3):
1. Giải mã sang mono 16 kHz. Tính đường bao RMS cửa sổ 10 ms, bước 1 ms. Tìm `tPeak`, thời điểm đường bao lớn nhất.
2. `start = max(0, tPeak − 0,030 s)`.
3. Từ file gốc, giữ đủ kênh và tần số lấy mẫu: `atrim=start=<start>`, `afade=t=in:d=0.003`. Không đổi gì ở phần sau đỉnh. Ghi `0Na.ogg` (libvorbis, `-q:a 6`).
4. Đo lại file mới: `atk` (từ lúc đường bao vượt −20 dB dưới đỉnh tới đỉnh) phải ≤ 30 ms; `mMax` và `tp` bằng `ebur128=peak=true` như đánh giá. Ghi số vào báo cáo.
5. `manifest.next.json`: bản chép của `manifest.json`, chỉ đổi `release-k5` và `release-k7` sang `["01a.ogg","02a.ogg","03a.ogg"]`. `release-k7-fire` giữ nguyên (đã lên trong 393 ms).

Đuôi của `release-k5` còn ngắn (−40 dB sau 470 ms). Phần tắt chậm do send vang ở mục 3 gánh, với mức send riêng cao hơn (0,4).

### 3. Send vang chung
- **Đồ thị** (tạo trong `unlock()`, một lần): bus `verb` gồm
  `DelayNode` (0,025 s) → `BiquadFilterNode` highpass 200 Hz (Q 0,707) → `ConvolverNode` (`normalize = true`, buffer = IR) → `BiquadFilterNode` lowpass 6500 Hz (Q 0,707) → `GainNode` (`VERB_RETURN` = 0,7) → `master`.
- **Mỗi take:** sau `panner`, một nhánh `GainNode` (mức send) nối vào đầu bus `verb`, song song với đường khô vào bus của nó.
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
  - `sound.ts` nạp IR này như mọi file (`fetch` rồi `decodeAudioData`). Chưa nạp xong thì send không kêu, đường khô vẫn chạy.
  - Ghi trong báo cáo và changelog: IR là bộ xử lý, không phải âm thay thế. Khi có IR thu thật (CC0), chỉ cần thay file. **Anh nghe và quyết** IR này có đạt không.
- **`SoundTake`** thêm trường `send: number` (mức send của take). Bản quay phải mix được giống live.
- **`mix-lab-sound.mjs`:**
  - dựng nhánh ướt: mỗi take nhân `send` (sau gain, pan, rate) cộng vào một track `wet`;
  - track `wet` qua `adelay` 25 ms → `highpass=f=200` → `afir` với `ir/hall-a.wav` (gain chuẩn hóa như `normalize = true`; ghi rõ cách khớp) → `lowpass=f=6500` → nhân 0,7;
  - cộng vào track khô trước master 0,9 và limiter như cũ;
  - take không có `send` (bản quay cũ) thì `send` = 0.

### 4. Công cụ `scripts/audio/lab-sound-tiers.mjs`
- `measure <file…>`: in `mMax`, `tp`, `atk`, `t40` của từng file, cùng cách đo với đánh giá (ebur128 `peak=true`, đệm 1 s im lặng cho momentary; đường bao RMS 10 ms ở 16 kHz mono).
- `trims`: đọc `summary-by-event.json` cộng số đo của sáu file mới ở mục 2, in bảng trim. Thoát khác 0 nếu bảng trong `sound-tiers.ts` lệch quá 0,05 dB.
- `attack`: làm mục 2.
- `ir`: làm IR ở mục 3; in RT60 đo lại bằng tích phân Schroeder (T30), phải nằm trong 2,2 ± 0,15 s.
- Mọi lệnh ffmpeg in ra trước khi chạy. Không ghi đè file đã có: nếu đã có thì dừng, trừ khi có `--force` cho chính file mới của mục 2 và 3.

### 5. Test `tests/lab/sound-tiers.test.ts` (Node, không WebAudio)
1. Mọi id trong `SOUND_IDS` và các bản `-fire` có trong `summary-by-event.json` đều có bậc trong `SOUND_TIER`.
2. `trimGain` khớp `10 ** (dB/20)`, và bằng 1 với id lạ.
3. Với số đo gốc, bảng `SOUND_TRIM_DB` theo đúng công thức mục 1, kể cả trần true peak. Test đọc một bản chép số đo đặt cạnh test (`tests/lab/fixtures/sound-audit-summary.json`, Codex tạo từ JSON đánh giá), vì test không đọc ngoài repo.
4. **Thứ bậc sau trim** (mMax + trim): mọi T3 < mọi T4 < mọi T5 ≤ T6 lớn nhất, và không sự kiện thường nào to hơn `world-climax` sau trim.
5. `LabSound` ở chế độ ghi (`record()`): một `impact-flesh` và một `world-climax` cho `SoundTake.gain` đúng gain cũ × bus × `trimGain`, và có `send` đúng bảng. Dựng `LabSound`, gọi `record()`, `on(event)` với file giả (đặt `files` qua manifest giả bằng `fetch` stub).

## Kiểm bắt buộc (trong `games/.wt-ic-sound`)
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua. Ghi số test trước và sau.
3. Xóa `/private/tmp/codex-269-dist` nếu có, rồi `IC_VITE_CACHE_DIR=/private/tmp/codex-269-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-269-dist --configLoader runner`: thoát 0. `grep -rl "SOUND_TRIM_DB\|hall-a" /private/tmp/codex-269-dist` phải không in gì (lab không vào bản dựng). Xóa thư mục sau khi kiểm.
4. `node scripts/audio/lab-sound-tiers.mjs trims`: thoát 0. Báo cáo dán bảng trim, đánh dấu `capped` và `missing`.
5. `node scripts/audio/lab-sound-tiers.mjs measure` trên 6 file mới: `atk` ≤ 30 ms, `tp` ≤ −1,0 dBTP. Dán số vào báo cáo.
6. `ir`: RT60 2,2 ± 0,15 s. Dán số.
7. `git -C games/.wt-ic-sound diff --stat` và `status --short`: chỉ các file được ghi. `ls` các file mới trong `art-src/lab/audio/` và `md5` của `manifest.json` trước và sau: phải không đổi.

## Claude làm sau
- Đọc diff, chạy lại Kiểm 1–7.
- Dev server của worktree (cấu hình bọc có `server.fs.allow`, như phiếu 258). Chép `manifest.next.json` sang `manifest.json` của bản thử (giữ bản cũ).
- Quay cảnh lab có tiếng (`__lab.soundRecord()`, `mix-lab-sound.mjs`): phím 1, phím 5 (ultimate) và phím 7. Đo momentary trên bản trộn: `world-climax` phải là đỉnh to nhất; impact nằm trong T3 ± 1 LU.
- Gửi anh video có tiếng để nghe. Chỉ gộp sau khi anh nghe.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
Thay đổi trong worktree, chưa commit; file âm mới trong `art-src`. Claude đọc diff, chạy lại kiểm, quay cảnh có tiếng, rồi mới commit.

## Phản biện
(chưa có)
