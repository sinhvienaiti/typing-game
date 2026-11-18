from pathlib import Path
p = Path('shared/game-kit/README.md')
s = p.read_text()
section = '''### audio/: file theo manifest

`SceneAudio` nhận `manifest` là URL tương đối dưới `audioBase` (mặc định
`/assets/audio/`), URL tuyệt đối, hoặc object. Không khai thì không có yêu cầu
manifest. `parseAudioManifest(json: unknown)` và `loadAudioManifest(url)` trả
`AudioManifest { sounds, music, errors }`; mục hỏng bị bỏ riêng, phiên bản lớn
hơn 2 làm rỗng cả manifest. HTTP lỗi, mạng lỗi và JSON hỏng chỉ ghi lỗi, không ném.
`AudioManifestV1`, `AudioManifestV2`, `AudioManifestSource`, `ManifestSound` và
`ManifestTrack` là các kiểu công khai. Hai dạng đầu vào:

```json
{ "sounds": { "hit": ["sfx/hit-1.ogg", "sfx/hit-2.ogg"] }, "music": { "calm": "music/calm.ogg" } }
```

```json
{ "version": 2, "sounds": { "hit": { "files": ["sfx/hit-1.ogg", "sfx/hit-2.ogg"], "durationMs": [118, 121], "loop": false } }, "music": { "calm": { "file": "music/calm.ogg", "bpm": 96, "bars": 8 } } }
```

Manifest chỉ giữ metadata file; bus, gain, gap và thứ tự ưu tiên thuộc bảng âm
và cấu hình game. Spec object được bỏ `url`: `{ bus, gain, gap }`. **Khi một id
có cả URL trong bảng và file hợp lệ trong manifest, file manifest thắng**;
URL cũ không tải, bus/gain/gap vẫn lấy từ bảng. Mục manifest hỏng bị bỏ thì
URL cũ tiếp tục dùng. Spec chuỗi và `{ url }` vẫn tải trong `unlock()` nếu
không có mục manifest thay thế.

`unlock()` tải metadata trước, giải mã hết biến thể của từng id trong
`preload: readonly S[]` đúng thứ tự (phím → UI → thưởng), rồi mới tới file
bảng cũ và bản ghi `dragonSamples`. Id còn lại chỉ tải ở lần `play` đầu;
nhạc chỉ tải khi gọi phát. `decodeConcurrency` mặc định 4, chặn cả số việc
fetch/giải mã đồng thời; mọi URL dùng chung cache. `ready(): Promise<void>`
đợi metadata, ưu tiên, file cũ và bản ghi rồng, không đợi id lười hay nhạc.
Yêu cầu phát sớm cũng chờ hàng ưu tiên để tải file, nhưng lượt phát đó không
được xếp lịch phát bù.

`VariantPicker<S>({ random = Math.random, avoidLast = 1 })` chọn ngẫu nhiên
trong các bản đã giải mã, tránh bản vừa phát. `avoidLast` nhận số hoặc bảng
theo id, kẹp tối đa số bản sẵn trừ 1; phím đúng có thể đặt 2. Một bản thì luôn
chọn bản đó. `PlayOptions.variant` là **chỉ số từ 0 trong manifest**, ghi đè
ngẫu nhiên và lịch sử tránh lặp; chỉ số chưa sẵn thì im, không chuyển sang
bản khác hay móc. Chỉ số không bị đổi khi một file lỗi. `play()` và
`playFile()` trả giây thực tế từ `buffer.duration / playbackRate`, hoặc 0
khi không phát. Tốc độ vẫn giữ dao động ±5 % cũ của `SceneAudio`.

`FileBank<S>` dùng độc lập: `unlock(context, eagerFiles = [])`, `ensure(id)`,
`entry(id)`, `url(id)`, `has(id)`, `select(id, variant?)`, `duration(id, variant = 0)`,
`loopBuffer(id)`, `track(name)`, `file(path)`, `cached(path)`, `stats()`.
`duration()` lấy giây đo được trước, metadata chỉ dùng khi bản đó chưa sẵn.
`stats().durationMismatches` ghi `{ id, variant, expectedMs, actualMs }` nếu
lệch quá 20 ms. `loop: true` không phát bằng `play`; game tự dùng
`loopBuffer(id): AudioBuffer | null` và điều khiển vòng lặp của mình.
`eagerFiles` là các URL bổ sung cần tải tại mở khóa (bản ghi rồng của kit).

`missing: Partial<Record<S, MissingHook>>` là móc riêng cho **mã âm hiện có
của game**: `(context, out, noise, now) => number | void`. `LayeredBank` chọn
file trước, móc sau; không có công thức tổng hợp mới trong kit. File chưa
sẵn thì gọi móc ngay hoặc im, hoàn tất tải không phát muộn. File đã sẵn thì
không gọi móc, kể cả khi chỉ số biến thể được yêu cầu chưa sẵn. Móc đi cùng
chuỗi gain → panner → bus, cùng gap (mặc định 0,03 giây) với `synth()`;
file và móc dùng chung gap theo id. `stats().plays[id]` đếm `file`, `hook`,
`silent` (gồm tắt âm, chưa mở khóa, bị gap, vòng lặp và thiếu file).
Đây là **đường chuyển tiếp có gắn cờ theo luật 28/10: âm là file thật**.
Xóa móc từng id khi có file được chủ dự án duyệt, đã kiểm mức trong bản trộn
và thống kê không còn gọi móc trong các ca chơi đại diện. Không viết bản tạm mới.

`musicBus: B` nối bus đó thẳng ra `destination`, các bus hiệu ứng vẫn qua
master SFX. `playMusic(path | null)` và `playTrack(name | null)` (tên trong
manifest) đi qua bus nhạc, chịu gain/duck của bus và `musicVolume`, không
nhân `sfxVolume`. Game nên dành bus này riêng cho nhạc. Bỏ `musicBus` thì
nhạc vẫn nối thẳng loa như cũ. Giữ crossfade: nhạc cũ giảm với hằng số
0,4 giây, dừng sau 2 giây; nhạc mới lên với hằng số 0,6 giây. Dừng hoặc đổi
track khi đang tải hủy lượt cũ, không phát track đến trễ.

Ví dụ nối Last Line sau khi đồng bộ (chỉ minh họa; `BUSES` và
`existingHitHook` là bảng/mã hiện có của game, không thêm công thức):

```ts
const scene = new SceneAudio<"hit.t1", Bus>({
  sounds: { "hit.t1": { bus: "impacts", gain: 1, gap: 0.038 } },
  buses: BUSES, audioBase: "/assets/typing-survival/audio/",
  manifest: "manifest.json", preload: ["hit.t1"],
  missing: { "hit.t1": existingHitHook }, musicBus: "music",
  dragonSamples: false,
});
scene.unlock(); // First user gesture.
scene.play("hit.t1");
void scene.playTrack("calm");
```

'''
s = s.replace('### `balance/`', section + '### `balance/`', 1)
p.write_text(s)
p = Path('shared/game-kit/DRIFT.md')
s = p.read_text()
line = '| 2026-10-30 | `audio/` | `src/scene3d/sfx.ts` | Kit | Phiếu 198: manifest v1/v2, FileBank/LayeredBank giải mã lười và ưu tiên, biến thể tránh lặp, móc mã game hiện có có thống kê, nhạc qua bus độc lập master SFX | Space chưa có; Claude duyệt rồi đồng bộ Last Line và Dragonhold; Wordwoven sau khi gộp `td-keys` |\n'
s = s.replace('|---|---|---|---|---|---|\n', '|---|---|---|---|---|---|\n' + line, 1)
p.write_text(s)
