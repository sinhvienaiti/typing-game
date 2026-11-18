# Phiếu 198 · Kit dùng chung · Kho âm từ file theo manifest v2: biến thể, giải mã lười, nhạc qua bus

**Nguồn:**
- `docs/games/AUDIO_PIPELINE.md` §6.3 mục 1: "Kit `SceneAudio` đang có 4 hạn chế: mỗi id chỉ có một file, mọi file được giải mã hết lúc `unlock()` …". Cách sửa ghi ngay ở đó: đưa `FileBank`, `LayeredBank` và schema manifest của Dragonhold vào `shared/game-kit/audio`. Schema v2 ở §11.
- `AGENTS.md` (chủ dự án 28/10): âm thanh là file thật, không phải bản tổng hợp tạm.
- Hiện trạng:
  - Last Line phát qua `SceneAudio` với `sounds: {}` (`games/typing-survival/src/audio/theme-audio.ts:101`). Mọi tiếng đều làm bằng mã.
  - Wordwoven chưa có bộ tải file (§6.3 mục 6).
  - File Firefly của chủ dự án tới thì hai game chưa có chỗ phát.
- Chủ dự án 29/10: "tăng thêm việc cho codex cho tôi".

**Báo cáo:** `docs/codex-queue/198-report.md` (tiếng Việt), thư mục `docs/codex-queue/198/`.

**Không trùng:**
- 189, 190: bộ tiếng phím và danh sách chọn.
- 191–193: gắn tiếng phím vào game, đi đường `feedback/typing-fx`.
- 168–170: gói và kit tiếng Anh. 171: manifest JSON ngoài Git.

Phiếu này gộp đề xuất "Last Line: phát SFX từ file thật". Phần ghép `hit.sub`, `hit.tail` (§6.3 mục 3) sẽ thành một phiếu gắn nhỏ của Last Line, sau khi kit được đồng bộ và có file Firefly.

**Sau phiếu này:** Claude duyệt, commit, đồng bộ kit vào game. Dragonhold giữ bank riêng tới một phiếu chuyển sau.

## Nơi làm

- Repo cha, chạy ở gốc repo (`.`), nhánh hiện tại `feat/space-typing-admin-uiux`. Làn `s1` (một làn Codex).
- Chỉ ghi vào:
  - `shared/game-kit/audio/` (mã và test);
  - một mục mới trong `shared/game-kit/README.md`;
  - một dòng trong `shared/game-kit/DRIFT.md`;
  - `docs/changelog/<ngày>-kit-audio-file-bank.md` (file riêng theo chủ đề; không sửa `docs/changelog/README.md`, Claude thêm hàng khi commit);
  - báo cáo và thư mục `198/`.
- Repo cha đang bẩn vì việc khác. Trước khi sửa gì, lưu `git status --short -uall` và `git diff --stat` vào `198/status-before.txt`.
- Đọc trước (chỉ đọc):
  - `games/dragon-hold/src/audio/bank.ts`: `FileBank` (dòng 77), `LayeredBank` (dòng 155), dạng manifest v1 ở chú thích đầu file;
  - `shared/game-kit/audio/scene-audio.ts`, `scene-audio.test.ts`, `mix.ts`, `util.ts`, `index.ts`;
  - `docs/games/AUDIO_PIPELINE.md` §5.3 (biến thể), §6.1 bài E và G, §6.3, §11 (manifest v2);
  - `games/typing-survival/src/audio/theme-audio.ts`: cách Last Line dùng `scene.synth` hôm nay.

## Luật chung (phiếu mã)

- Test trước, mã sau. Chú thích tiếng Anh. Kit không có chữ người chơi thấy; nếu buộc phải có thì tiếng Anh.
- Module `audio/` không import module kit khác (`../<module>/`). Game chỉ khai `audio` vẫn phải đồng bộ được.
- Không thêm thư viện. Chỉ dùng Web Audio có sẵn.
- Test dùng `fetch` và `AudioContext` giả. Không gọi mạng thật.

## Việc

1. **Manifest** (file mới `audio/manifest.ts`).
   - `parseAudioManifest(json)` nhận hai dạng:
     - v1 (Dragonhold hôm nay): `{ "sounds": { "<id>": ["a.ogg", "b.ogg"] }, "music": { "<tên>": "music/x.ogg" } }`;
     - v2 (§11): `{ "version": 2, "sounds": { "<id>": { "files": [...], "durationMs": [...], "loop": false } }, "music": { "<tên>": { "file": "...", "bpm": 96, "bars": 8 } } }`.
   - Trả một dạng chung, kèm danh sách lỗi.
   - Mục hỏng thì bỏ riêng mục đó và ghi lỗi: `files` không phải mảng chuỗi, đường dẫn rỗng, `durationMs` khác độ dài `files`.
   - `version` lớn hơn 2: coi cả manifest là rỗng, ghi lỗi.
   - Manifest không mang mức to, bus hay độ ưu tiên (§11). Các thứ đó lấy từ bảng âm của game.
   - `loadAudioManifest(url)`: 404, lỗi mạng, JSON hỏng đều cho manifest rỗng có lỗi. Không ném.
2. **Chọn biến thể** (file mới `audio/variants.ts`).
   - Mỗi id có nhiều file. Mỗi lần phát chọn ngẫu nhiên, không trùng bản vừa phát (§5.3; §6.1 bài E).
   - `random` tiêm được, mặc định `Math.random`.
   - `avoidLast` mặc định 1, tối đa bằng số biến thể trừ 1. Phím đúng của §5.3 dùng 2.
   - Một biến thể thì luôn phát bản đó.
   - `PlayOptions.variant` chọn đích danh một bản, như `params.variant` của Dragonhold.
3. **Kho file** (file mới `audio/file-bank.ts`): bản kit của `FileBank`.
   - **Giải mã lười.** Lúc `unlock()` chỉ fetch manifest JSON và các id ưu tiên. Id khác chỉ fetch và giải mã ở lần `play` đầu.
   - **Ưu tiên.** Tùy chọn `preload: readonly S[]` được giải mã trước tiên, đúng thứ tự (phím, UI, âm thưởng: §6.1 bài G). Sau đó mới tới file của bảng âm kiểu cũ. `dragonSamples` nạp như cũ.
   - Giới hạn số việc giải mã cùng lúc: `decodeConcurrency`, mặc định 4.
   - Giải mã một id thì giải mã cả các biến thể của nó. Chọn biến thể chỉ trong các bản đã sẵn.
   - Nhạc không bao giờ giải mã lúc `unlock()`. Chỉ khi được gọi phát.
   - **Độ dài** đo từ buffer đã giải mã (`duration`). `durationMs` của manifest chỉ dùng khi chưa giải mã xong. Lệch quá 20 ms thì ghi vào `stats()`.
   - Id `loop: true`: `play` không phát. Game lấy buffer qua `loopBuffer(id)`.
4. **`SceneAudio`** nối kho file, vẫn tương thích ngược.
   - Tùy chọn mới `manifest`: URL dưới audio base, hoặc object đã có. Không có tùy chọn này thì không fetch gì (không 404).
   - Spec dạng object được phép bỏ `url`: id chỉ khai `bus`, `gain`, `gap`, rồi chờ file từ manifest.
   - Spec chuỗi và `{ url }` chạy y như hôm nay (giải mã lúc `unlock()`).
   - Id có cả `url` trong bảng và file trong manifest: file manifest thắng. `bus`, `gain`, `gap` vẫn theo bảng. Ghi quyết định này vào README.
   - `play()` trả số giây đã phát: độ dài biến thể chia tốc độ, 0 khi không phát. Hôm nay hàm trả `void`, nên người gọi cũ không vỡ.
   - Id có trong manifest mà chưa giải mã xong: không phát muộn khi giải mã xong. Lần đó dùng móc (mục 5) nếu có, không thì im.
5. **Móc khi thiếu file** (tùy chọn `missing: Partial<Record<S, MissingHook>>`).
   - `MissingHook` cùng chữ ký với hàm dựng của `synth()` hôm nay: `(context, out, noise, now)`. Được trả số giây.
   - Kit chỉ gọi móc khi id chưa có file sẵn. Có file thì không bao giờ gọi móc.
   - Mục đích: game giữ đúng tiếng hiện tại cho tới khi có file. Kit **không** chứa công thức tổng hợp mới nào. Móc là mã cũ của game.
   - Móc để ở một tùy chọn riêng, để xóa dần theo từng id.
   - `stats()` đếm cho mỗi id: số lần phát từ file, từ móc, và im. Nhìn vào đó biết id nào còn thiếu file.
   - Báo cáo phải gắn cờ móc này theo luật chủ dự án 28/10 (âm là file thật): đây là đường chuyển tiếp, không phải bản tạm mới.
6. **Nhạc qua bus.**
   - Tùy chọn `musicBus: B`. Có thì `playMusic` và hàm mới `playTrack(tên | null)` đi qua bus đó. `playTrack` phát nhạc theo tên trong manifest.
   - Nhạc vì thế nhường giọng đọc theo `duck` của bus.
   - Bus nhạc nối thẳng ra loa, không qua master hiệu ứng. Độ to nhạc chỉ theo `musicVolume`, không nhân `sfxVolume`.
   - Không có `musicBus` thì như cũ (nối thẳng `destination`). Giữ crossfade như `playMusic` hôm nay.
7. **Xuất** mọi API mới, có kiểu, trong `audio/index.ts`.
8. **Tài liệu.**
   - `shared/game-kit/README.md`: mục `### audio/: file theo manifest` gồm dạng v1 và v2, ưu tiên và giải mã lười, biến thể, móc khi thiếu file và luật xóa, nhạc qua bus. Thêm ví dụ nối cho Last Line khoảng 10 dòng (chỉ trong README, không sửa game).
   - `DRIFT.md`: một dòng (bên sửa: Kit; Space chưa có).
   - Changelog theo luật của `docs/changelog/README.md`: yêu cầu, quyết định, file đổi, lệnh kiểm, việc còn lại.

## Test (viết trước, đặt trong `audio/`)

- File test mới: `manifest.test.ts`, `variants.test.ts`, `file-bank.test.ts`, `scene-audio-files.test.ts`. Không sửa `scene-audio.test.ts`.
- Đồ giả dùng chung để ở `audio/fake-audio.test-helper.ts` (lệnh đồng bộ bỏ qua đuôi này). Fetch giả trả promise theo lệnh, để kiểm thứ tự.
- **Parse:** v1; v2; mục hỏng bị bỏ riêng; `version: 3`; manifest 404; JSON hỏng.
- **Biến thể:** 1.000 lượt, 3 bản, seed cố định: 0 lần lặp liền, mỗi bản 20–47 %. Thêm: `avoidLast: 2` với 4 bản; 1 bản; `variant` đích danh.
- **Giải mã:**
  - lúc `unlock()` chỉ fetch manifest, rồi id `preload` đúng thứ tự, rồi file bảng cũ;
  - id khác chưa fetch; lần `play` đầu mới fetch;
  - giải mã xong không phát muộn;
  - không bao giờ quá `decodeConcurrency` việc cùng lúc.
- **Độ dài:** `play` trả độ dài buffer chia tốc độ; số trong manifest bị thay bằng số đo; lệch quá 20 ms có trong `stats()`.
- **Móc:** gọi khi thiếu file; không gọi khi có file; cùng chuỗi nút (gain, panner, bus) và cùng luật `gap` như `synth()`.
- **Manifest rỗng giữ nguyên lịch phát.** Chạy cùng một chuỗi `play` (có móc, có spec chuỗi) ba lần: không manifest; `{ "version": 2, "sounds": {} }`; manifest 404. Ba lần ghi ra cùng danh sách (id, thời điểm, bus, gain, nguồn file hay móc) và cùng số nút tạo ra.
- **Nhạc:** đi qua `musicBus`; không đổi khi `sfxVolume` đổi; nhường giọng theo `duck`; không có `musicBus` thì như cũ.

## Cấm

- Mọi lệnh git có ghi.
- Sửa `games/**`, kể cả `bank.ts` của Dragonhold và `src/kit/**` của mọi game. Chạy `kit:sync`.
- Sửa `shared/game-kit/feedback/typing-fx/*` và `shared/game-kit/ui/quick-settings/*`: làn TF2 có sửa chưa commit ở đó.
- Sửa `media/`, `scripts/media/`: diff của phiếu 171.
- Sửa `.gitignore`: đường đi của manifest JSON cùng media (171) chưa chốt.
- Thêm công thức âm tổng hợp mới hay file âm vào kit.
- Dev server, trình duyệt, mạng. Ghi ra ngoài repo.
- Đụng Tu Tiên.

## Kiểm (ghi số)

1. `pnpm kit:test`: số file test và số test, trước và sau (`198/tests-before.txt`, `198/tests-after.txt`).
   - Đỏ chỉ vì file đang dở của TF2: ghi tên từng test đỏ. Rồi chạy riêng `pnpm --dir shared/game-kit exec vitest run audio/`, lưu vào `198/tests-audio.txt`.
2. `pnpm --dir shared/game-kit typecheck`: 0 lỗi (`198/typecheck.txt`).
3. Bảng test mới theo từng nhóm của mục Test, có số test mỗi nhóm.
4. `git diff --quiet shared/game-kit/audio/scene-audio.test.ts`: mã thoát 0. Bốn test cũ qua mà không sửa.
5. `grep -n 'from "\.\./' shared/game-kit/audio/*.ts`: 0 dòng.
6. Không có tổng hợp mới: `grep -nE 'createOscillator|createBiquadFilter|noiseBuffer\('` trên ba file mới và trên các dòng `+` của `git diff shared/game-kit/audio/scene-audio.ts`: 0 dòng. Ngoại lệ duy nhất: dòng cấp `noise` cho móc, dùng lại đúng mẫu `this.noise ??= noiseBuffer(context)` của `synth()`; ghi rõ dòng đó.
7. `git status --short -uall` và `git diff --stat` sau, lưu `198/status-after.txt`.
   - So với `status-before.txt`: dòng mới hay đổi chỉ là đường dẫn của phiếu này.
   - Ba file của TF2 giữ nguyên số dòng đổi.
   - Dòng lạ do làn khác chạy cùng lúc thì ghi riêng, không đụng.
8. Không chạy `kit:check`: các game sẽ lệch kit tới khi Claude đồng bộ. Đó là trạng thái chờ đúng.

## Báo cáo

- API mới: tên, chữ ký, mặc định.
- Quyết định: thứ tự giữa bảng và manifest; hành vi khi id đang giải mã; bus nhạc.
- Mục riêng "Móc khi thiếu file": cờ theo luật 28/10, game nào sẽ dùng, khi nào xóa từng id.
- Việc kế cho Claude:
  - đồng bộ kit vào Last Line (`main`) và Dragonhold;
  - Wordwoven: `audio` đã vào `kit.config.json` ở nhánh `td-keys` (`81baf46`), chưa gộp vào `a2-days`; đồng bộ sau khi gộp;
  - phiếu gắn Last Line (`hit.sub`, `hit.tail`, §6.3 mục 3) khi có file Firefly;
  - phiếu chuyển Dragonhold sang kho file của kit.

**Xong khi:** đủ API và test của mục Việc; test kit (hoặc test `audio/` khi TF2 làm đỏ phần khác) và typecheck xanh; có mục README, dòng DRIFT, changelog và báo cáo có số. Claude duyệt, commit, rồi đồng bộ vào game.
