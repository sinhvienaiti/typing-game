# Bộ kit chung cho game (`shared/game-kit`)

Kit là **nguồn chuẩn** của mã dùng chung cho các game mới tách từ Space Typing:
Rồng Giữ Ải (`dragon-hold`), Lời Gọi (`typing-defense`), Tuyến Cuối (`typing-survival`).
Kit chỉ có TypeScript và test, không có ảnh, âm thanh hay model.

Kế hoạch đầy đủ: `docs/games/SPLIT_PLAN.md` §4.

## Quy tắc quan trọng

- **Không bao giờ sửa tay `src/kit/` trong một game.** Mọi file ở đó được chép từ đây
  và kiểm sha256. Sửa tay thì `pnpm check` của game sẽ đỏ.
- Muốn đổi kit: sửa ở `shared/game-kit`, chạy test, rồi chép lại vào từng game.
- Kit chép **từ** Space. Space giữ bản gốc, không đổi ở giai đoạn này.
- Sửa lỗi ở một bên (kit hoặc Space) thì ghi một dòng vào `DRIFT.md`.
- Mã trong một module chỉ import trong kit bằng đường dẫn tương đối
  (ví dụ `../platform/rng`), để chạy được cả ở đây lẫn ở `src/kit/` của game.

## Các module

| Thư mục | Nội dung | Nguồn |
|---|---|---|
| `platform/` | RNG có seed, vòng khung hình, lưu trữ an toàn, trạng thái canvas | Space `src/platform/*` (không đổi) |
| `input/` | Bảng phím, chuẩn hoá chữ gõ (`typingText`, `normalizeWord`) | Space `src/scene3d/keys.ts`, `src/logic.ts` |
| `vocab/` | Nạp từ vựng, chọn từ theo độ dài, lọc từ nhạy cảm | Space `src/vocabulary.ts`, `src/scene3d/words.ts` |
| `learning/` | Gửi sự kiện học về portal (`gameId` bắt buộc), hàng đợi khi chạy riêng | Space `src/learning/shared.ts`, `shared/learning/message-contract.mjs` |
| `speech/` | Đọc từ bằng giọng máy, cài đặt hẹp `{ enabled, rate, volume }` | Space `src/speech.ts` |
| `audio/` | Bộ trộn nhiều bus, nhận bảng âm của từng game | Space `src/scene3d/sfx.ts`, `src/audio/mix.ts` |
| `ui/` | Màu ngữ nghĩa, biến CSS, font chữ trận, khung học cơ bản, bảng cài đặt nhanh trong trận (`quick-settings/`) | Mới |
| `tools/` | `cdp-run.mjs` (chạy kịch bản trình duyệt), plugin Vite phục vụ `/vocabulary/`, `/typing-texts/` | Space `scripts/visual/cdp-run.mjs`, `scripts/dev/vite.worktree.config.ts` |
| `typing/` | Bộ định tuyến gõ, chữ, chọn từ, chấm điểm | Space `src/td/typing/*` (làn Kit B) |
| `three/` | Nạp model, vật liệu, hạt, sân khấu 3D | Space `render3d/*`, `scene3d/*` (làn Kit B) |
| `feedback/` | Phản hồi gõ theo hồ sơ game | Space `src/feedback/*` ở thẻ `survival-s0` (a292d1ac, làn Kit B) |
| `balance/` | Cân bằng nhiều yếu tố: hồ sơ năng lực, `effectiveE`/`paceK`, dải đích, FlowMeter, bộ điều nhịp, bot gõ giống người, cổng B1–B9 | Mới, theo `docs/games/BALANCE.md` §8 |

Mỗi module có `index.ts` xuất API công khai và test `*.test.ts` nằm cạnh.

### audio/: file theo manifest

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
ngẫu nhiên và lịch sử tránh lặp; khi id đã có bản sẵn, chỉ số được yêu cầu
chưa sẵn thì im, không chuyển sang bản khác hay móc. Chỉ số không bị đổi khi một file lỗi. `play()` và
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

### `balance/` (BALANCE.md §8)

TS thuần, tất định: không dùng `Date`, `performance`, `Math.random`, `window`; mọi số ngẫu nhiên đi qua `RngStream` của `platform/`.
Phân số tính bằng phần nghìn (‰, số nguyên 0–1000), riêng N (gần thua) là số đếm.
Game tự lưu hồ sơ (khóa `<game>.skill`), tự cấp bảng bậc và tự nối quyết định vào sim.

| File | Nội dung |
|---|---|
| `profile.ts` | `SkillProfile`: 13 yếu tố, mỗi yếu tố có giá trị và độ tin (số mẫu). Mặc định theo chế độ và theo trẻ em/người lớn. `updateSkill` sau mỗi ải hoặc đợt: EWMA 0,25, loại ải bỏ dở, AFK, quá ngắn, lệch xa. `blendSkill` trộn mặc định sang số đo theo độ tin. `serializeSkill`/`parseSkill` có phiên bản, đọc lỗi thì về mặc định từng trường |
| `pace.ts` | `effectiveE`, `capacity` (C(E)), `paceK` (0,75–1,30, hai chiều, làm tròn 1/1000), `scaleTicks`, `familiarityMix`, `newWordShare`, `telegraphScale`, `peakLanes`, `suggestDifficulty`, `skillAdvice` |
| `bands.ts` | `BANDS`: dải đích §3 cho Thư giãn, Cân bằng, Thử thách; `scoreBand` chấm trong/dưới/trên từng chỉ số; `bandModeFor` |
| `flow.ts` | `FlowMeter`: nhận ảnh chụp mỗi tick (hoặc mỗi N tick), tính P, I, O, S, N, Q theo cửa sổ 20 s và cả ải |
| `director.ts` | `PaceDirector`: mỗi 300 tick tính độ căng τ; 3 cửa sổ thấp thì tăng một bậc, 2 cửa sổ cao thì giảm; có trễ, tối đa 2 bậc mỗi đợt, trần ±15 % khoảng sinh và ±10 % W; tắt ở Lời Thề, Vương Miện, xếp hạng, Duel; ghi nhật ký `pace` |
| `typist.ts` | `HumanTypist`: bot gõ giống người (E, a, CV log-normal, thời gian nhận từ theo độ quen, Backspace, bỏ khóa, chọn mục tiêu, chú ý khi đông, thời gian nhìn bảng, mệt); `STANDARD_BOTS` (bộ bot chuẩn §6); `KeyPlayer` phát phím theo tick |
| `gates.ts` | `summarizeRuns` gộp các lượt của một bot ở một chế độ; `runGates` chấm B1–B9 (thiếu số thì "THIẾU SỐ", không bao giờ "ĐẠT"); `formatGates` in bảng Markdown chung |

`typing/tempo.ts` vẫn giữ `paceFactor` cũ (chỉ giãn, trần 1,0 theo D06). Việc mới dùng `paceK` của `balance/` (BALANCE.md §9.1 thay D06).

### `ui/quick-settings/` (`docs/games/IN_GAME_SETTINGS.md`)

Hai nút trong trận, **Settings** và **Sound**, ở góc trên phải của `host` (cùng góc ở mọi game), mở hai bảng phủ lên trận.
Bảng dùng `a11y-dialog` 8.1.5 (MIT): giữ Tab trong bảng, trả focus về ô gõ khi đóng. Thanh trượt là `<input type="range">` gốc.

| Phần | Nội dung |
|---|---|
| Tạo | `new QuickSettings({ host, getValues, onChange, onPreview, onPause, onResume, onQuit, icons, skin, countdownMs, zIndex, context })`; `open("settings" \| "sound")`, `close()`, `toggle()`, `isOpen`, `panel`, `blocking`, `refresh()`, `setIcons()`, `setContext()`, `context`, `destroy()` |
| Màn tựa | `context`: `"play"` (mặc định) hoặc `"title"`, hoặc hàm trả một trong hai (đọc mỗi lần `open()` và `refresh()`); `setContext()` đổi ngay. Ở `"title"` nút **Resume** và **Quit to title** (hàng `button` có `action` là `"resume"`/`"quit"`) ẩn đi, hàng nút trống cũng ẩn; nút riêng của game vẫn hiện. Focus đang ở nút bị ẩn thì sang Close |
| Phím | `F1` mở Settings, `F2` mở Sound, bấm lại hoặc `Esc` thì đóng. Phím chữ không bao giờ mở bảng. Nút góc mở bằng chuột mà không lấy focus của ô gõ |
| Dừng | Mở bảng gọi `onPause`. Đóng thì đếm 3, 2, 1 (mỗi bước `countdownMs`, mặc định 500 ms; 0 là chơi tiếp ngay; có thể là hàm, ví dụ trả 0 ở màn tựa) rồi gọi `onResume`. Mở lại lúc đang đếm thì hủy đếm, trận vẫn dừng. `Quit to title` gọi `onQuit`, không đếm |
| Khóa gõ | Khi bảng mở và lúc đếm, `blocking === true`. Một listener capture trên `window` nuốt mọi phím nhắm ra ngoài bảng; phím trong bảng đi vào nút, thanh trượt, rồi dừng ở gốc bảng. Game có listener capture riêng (trên `document`, hoặc trên `window` đăng ký trước kit) thì tự kiểm `qs.blocking` |
| Hàng | Dữ liệu: `slider`, `choice`, `toggle`, `button`, `slot`, `heading`. `defaultSoundRows(options)` và `defaultSettingsRows(options)` dựng đúng thứ tự spec; game lọc, đổi chỗ hay thêm hàng rồi đưa vào `soundRows`/`settingsRows`. Mục riêng của game: `gameRows`, `mountGameItems`; ô xem thử hiệu ứng gõ: `mountPreview`. Ô `slot` chỉ được gắn khi bảng mở, hàm dọn chạy khi đóng |
| Giá trị | Id cố định: `master`, `muted`, `music`, `effects`, `keyboard`, `keyboardVolume`, `voice`, `ui`, `fxStyle`, `fxIntensity`, `fxSize`, `quality`, `reducedMotion`, `learnMeaning`, `learnIpa`. Âm lượng 0–100. Đọc `getValues()` khi mở bảng; mỗi thay đổi gọi `onChange` ngay, game áp ngay và lưu vào save của mình (không có nút Lưu). Kéo thanh trượt gọi `onPreview(nhóm)` tối đa mỗi 150 ms; chọn hồ sơ phím gọi `onPreview("keyboard")` |
| Hình | Icon theo tên (phiếu Codex 180: `hud-settings`, `hud-sound`, `hud-sound-muted`, `vol-*`) qua `icons`/`setIcons`. Thiếu ảnh hoặc ảnh lỗi thì nút là chữ thường ("Settings", "Sound", "Sound off"), không vẽ icon bằng CSS, SVG, canvas hay emoji. Khung, nút, thanh trượt là ảnh qua `skin`. Màu là biến CSS `--kit-qs-*` trên `.kit-qs`; chữ trong bảng ≥ 7:1 (có test) |
| Icon hàng | Mọi hàng `slider`, `choice`, `toggle` có `icon` (tên bất kỳ, `QuickIconKey`). Hàng mặc định của kit: `vol-*`, `vol-keyboard-volume`, `fx-style`, `fx-strength`, `fx-size`, `gfx-quality`, `gfx-motion`, `learn-meaning`, `learn-ipa` (`QUICK_ROW_ICON_NAMES`, để riêng khỏi `QUICK_ICON_NAMES` mà game đang map ra file). Hàng của game tự đặt tên (ví dụ `game-pace`) và đưa URL qua `icons`. Tên chưa có ảnh: ô trống vẫn giữ rộng `--kit-qs-icon-size`, nhãn thẳng hàng; ô có `data-icon` |
| Thanh trượt | `<input type="range">` gốc nằm trong `.kit-qs__slider`, cùng hai lớp ảnh `aria-hidden`: rãnh rỗng (`.kit-qs__groove`) và phần đầy (`.kit-qs__fill`), cắt đúng tâm núm theo `--kit-qs-v` (0..1, kit đặt trên `.kit-qs__slider`). Hai lớp chỉ hiện khi có `skin.sliderFill` hoặc `skin.sliderEmpty`; thiếu cái nào thì dùng ảnh `sliderTrack` (phần đầy qua `--kit-qs-fill-filter`, mặc định sáng hơn). Vẽ ba mảnh: `--kit-qs-groove-slice` (cắt, px nguồn, ví dụ `0 64`), `--kit-qs-groove-cap` (rộng đầu rãnh khi vẽ); núm `--kit-qs-knob`, rãnh cao `--kit-qs-groove-h` |
| Nút tắt tiếng | Nút `toggle` của hàng trượt (Master: Mute) nằm ở cột `.kit-qs__aside` sau con số, rộng `--kit-qs-aside-w`; bảng có hàng trượt kèm nút thì mọi hàng trượt của bảng đó đều giữ cột này, nên mọi rãnh dài bằng nhau. Nút vẫn là `.kit-qs__btn[data-toggle]` với `aria-pressed`, trong `.kit-qs__row[data-row="master"]` |
| Danh sách âm phím | `skin.listRow` / `skin.listRowActive` (`QuickNineSlice`: `url`, `slice` theo thứ tự CSS, `edge` px; thiếu `url` thì là ảnh `button` / `buttonActive`) bật tấm ảnh chín mảnh cho từng dòng: bỏ khung bo tròn và nền phẳng, dòng đang chọn mang tấm active (không có ảnh active thì tấm thường sáng lên, `--kit-qs-list-active-filter`), focus là quầng sáng ôm tấm. Chỉnh thêm: `--kit-qs-list-inset` (tấm lùi vào trong dòng, mặc định `2px 0`), `--kit-qs-list-pad`; rê chuột: `--kit-qs-list-hover-filter` (mặc định sáng 1,3 kèm quầng `--kit-qs-glow`). Danh sách ngoài bảng có da (Lab) giữ nguyên |
| Cuộn danh sách âm phím | Mép trên/dưới mờ dần 10 px (nhân `--kit-qs-s`) chỉ khi còn dòng phía đó (`data-more-above` / `data-more-below`, `mask-image`); dòng và tiêu đề họ bám đầu (`scroll-snap-type: y proximity`, `scroll-padding` bằng dải mờ). Mở bảng: dòng đang chọn nằm khuất thì được đưa ra giữa danh sách; phím mũi tên cuộn ít nhất có thể và dừng đúng chỗ bám của một dòng; dòng đầu của một họ kéo theo tiêu đề họ. Chỉ một nút Listen nằm trong thứ tự Tab: của dòng đang focus (hoặc đang chọn); Tab từ danh sách tới Keyboard volume trong tối đa 2 lần bấm |
| Close, focus, tựa | `skin.close`: Close là nút icon ở góc trên phải của bảng, `--kit-qs-close-size` (32 px ở 720p), tên đọc "Close"; dời bằng `--kit-qs-close-x`/`-y`; ảnh lỗi thì về nút chữ. Có da (`button`, `close`, thanh trượt, tấm danh sách, icon góc) thì focus là quầng `--kit-qs-glow-filter` màu `--kit-qs-glow` (mặc định `--kit-qs-focus`) ôm theo ảnh, thay viền 2 px. `skin.buttonActive`: nút đang nhấn hay đang bật mang tấm này, chữ `--kit-qs-active-text`. Font: `--kit-qs-title-font` (tựa bảng), `--kit-qs-button-font` (nút, chip, nút chữ ở góc, dòng âm phím), `--kit-qs-label-font` (nhãn hàng, tiêu đề mục, tiêu đề họ); không đặt thì theo font của bảng. Ghi chú nhỏ giữ `--kit-qs-note-font` (mặc định font trận, Be Vietnam Pro). Núm luôn vẽ trên rãnh và phần đầy (`z-index` 1 trên 0). Mọi biến và mặc định: `QUICK_SETTINGS_VARS` |

**Mỗi game chép `ui` phải thêm `a11y-dialog@8.1.5` vào `package.json` của mình** (lệnh chép không kiểm gói npm).
Hiện `dragon-hold` và `immortality-cultivation` chép `ui`.

Test DOM dùng `happy-dom` (devDependency của kit) và ghi `// @vitest-environment happy-dom` ở đầu file; môi trường mặc định của kit vẫn là `node`.

## Lệnh

Chạy ở repo cha (`/Users/toandx/htdocs/typing-game`):

| Lệnh | Làm gì |
|---|---|
| `pnpm kit:test` | Chạy test của kit |
| `pnpm kit:sync --target games/<id>` | Chép các module khai trong `games/<id>/kit.config.json` vào `games/<id>/src/kit/`, ghi `kit-manifest.json`, `verify-kit.mjs` và `README.md` |
| `pnpm kit:sync --target games/<id> --allow-missing` | Như trên, bỏ qua module chưa có (chưa có `index.ts`). `kit:check` vẫn đỏ tới khi chép đủ |
| `pnpm kit:check` | Kiểm mọi game có `kit.config.json` (bỏ qua thư mục bắt đầu bằng `.`, như worktree): không ai sửa tay, đúng bản kit hiện tại hoặc bản ghim. Lỗi thì thoát mã 1 |
| `pnpm kit:drift` | So từng file kit với bản gốc ghi ở dòng `// Source:` đầu file, in tóm tắt. Chỉ để biết, luôn thoát mã 0 |

Test của lệnh chép: `node --test scripts/sync-game-kit.test.mjs`.

Khi chép, lệnh:

- Bỏ test: `*.test.ts`, `*.spec.ts`, `*.test-helper.ts`, thư mục `__tests__`, `__fixtures__`.
- Từ chối file media (ảnh, âm, video, model, font) trong kit.
- Từ chối khi một module import module khác (`../<module>/...`) mà game chưa khai. Hiện tại: `vocab` cần `input`; `learning` cần `platform`, `vocab`; `speech` cần `platform`; `typing` cần `platform`; `balance` cần `platform`.
- Xoá file thừa trong `src/kit/`, chỉ ghi file đổi nội dung.
- Ghi vào `kit-manifest.json`: phiên bản kit, `parentCommit` (commit cuối của repo cha có đổi `shared/game-kit`), `parentDirty` (kit có thay đổi chưa commit), danh sách module, sha256 từng file.

Chạy riêng trong kit:

```bash
pnpm --dir shared/game-kit install
pnpm --dir shared/game-kit exec vitest run
pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit
```

## Cấu hình của game

`games/<id>/kit.config.json`:

```json
{ "modules": ["platform", "input", "vocab", "learning", "speech", "audio", "ui", "typing", "three", "feedback"] }
```

Có thể ghim một bản cũ bằng `"pinned": { "commit": "<sha>", "reason": "<lý do>" }`.
Khi đó `kit:sync` chép kit ở đúng commit đó (đọc từ Git), còn `kit:check` so với commit đó, không đòi bản mới nhất.
Thiếu lý do thì lệnh báo lỗi.

Game chạy `node src/kit/verify-kit.mjs` trong lệnh `check` của mình.
Script này tự đứng một mình, nên vẫn chạy khi repo game được clone riêng.
Test của game có thể gọi `verifyKit()` mà nó xuất ra: trả về danh sách lỗi, rỗng là đúng.

Kit chỉ dùng trong `vite.config.ts` và script Node: `tools/` (cần `vite`, `node:fs`). Mã chạy trong trình duyệt không import `tools/`.
