# Phản hồi gõ chữ: rà đề xuất với mã đang chạy

Ngày 29/10/2026 · Làn phản hồi gõ · Trả lời §51 của [`TYPING_FEEDBACK_PROPOSAL_2026-10-29.md`](TYPING_FEEDBACK_PROPOSAL_2026-10-29.md) (ChatGPT viết, anh đưa làm tham khảo) · Nguồn kỹ thuật chữ: [`TYPING_BREAK_STUDY.md`](TYPING_BREAK_STUDY.md) (T1–T16).

**Lời anh (29/10):** chưa thấy chữ cái có hiệu ứng khi gõ tới như Typing Break; muốn ở giữa màn hình hiện từ đang gõ, chữ vừa gõ lóe sáng thật đẹp, và người chơi được chọn kiểu hiệu ứng.

**Kết luận: DUYỆT CÓ SỬA (APPROVE WITH CHANGES).** Lấy ý chính (sự kiện ngữ nghĩa, thứ bậc hiệu ứng, cường độ, nhiều mẫu âm có biến thể, phòng thí nghiệm A/B). Bỏ PixiJS, pixi-filters, Howler, Motion, tsParticles, âm tổng hợp khi phát hành và việc tải gói âm từ mạng. Dựng một module nhỏ trong kit: dải chữ DOM + một canvas 2D nhỏ + bộ âm Web Audio có sẵn mẫu.

---

## 1. Hôm nay mỗi game vẽ chữ đang gõ thế nào

| Game | Lõi gõ | Chữ đang gõ hiện ở đâu | Hiệu ứng mỗi phím hôm nay |
|---|---|---|---|
| Dragonhold | `src/sim/words.ts` `typeKey()` gọi `typeLetter` của kit (`src/kit/typing`). View nhận `SimEvent` `word-progress {word, typed, key, letter}`, `key` là `lock/advance/done/wrong/switch/stray/pair/back` | Nhãn DOM `.dh-tag` trên từng quái, trong `#dh-overlay` (`ui/tags.ts`), chữ 16–26 px. Khung học `.dh-learn` ở **giữa đáy** (`ui/learning-frame.ts`) | `dh-letter` 170 ms (−5 px, 1,45×), cả nhãn `dh-tag-tick` 140 ms; đốm lửa 3D 0,16 s (`view/fx.ts` `keySpark`). Sai: `dh-tag-shake` 180 ms |
| Wordwoven | Lõi riêng `src/typing/router.ts` (bản gốc của kit), `sim/systems/calls.ts` `typeKey()`. View nhận `{t:"wordKey", word, result}` | Thẻ DOM `.td-card` trong `#tdWords` (`view/words/cards.ts`), chữ 18–24 px; dải `.td-strip` 44 px ở **giữa đáy** (`ui/hud.ts` `stripHtml`) | `td-key` 0,18 s (−4 px, 1,5×). Sai: thẻ rung 6 px 220 ms |
| Last Line | Lõi riêng `sim/words.ts` `keyPress()`; vòng sự kiện `EV.keyOk/keyBad/word`, đọc bằng `TypeFeel.read` (`view/typing-feel.ts`) | `WordStrip` (`view/strip.ts`): chữ 42 px ngay trên mũi tàu (y ≈ 400–456 ở 720p); ô súng hai bên | Pop 1,25× + tia 170 px + vòng nở; tia điện 3D từ chữ về lõi tàu (`KEY_MARK`) |

Vì sao anh không thấy: ở Dragonhold và Wordwoven chữ nhỏ, nằm rải trên sân, pop 170 ms không có hạt hay lóe. Last Line có dải gần giống nhưng nằm thấp, chỉ một kiểu, không chọn được. Không game nào có một dải lớn ở chỗ mắt nhìn.

## 2. Bộ dựng hình

- `three@0.170.0` khai ở cả ba game, nhưng **Wordwoven là Canvas 2D**: không file nào trong `src/` import `three`. Mọi chữ của cả ba là DOM nằm trên canvas.
- Bloom: Dragonhold dựng `UnrealBloomPass` nhưng chỉ bật ở Ultra (mặc định High). Last Line bật ở High (0,85). Dải chữ là DOM nên bloom không chạm vào chữ.
- Không game nào có PixiJS, Howler, Motion, GSAP, tsParticles.
- Wordwoven đang sát trần gói: tập khởi động 84,97 kB của 85 kB gzip (còn 25 byte). Mọi thứ thêm vào phải nạp lười (`import()`).

## 3. Mã phản hồi dùng lại được

- `feedback/tiers.ts`, `profiles.ts`: bậc T0–T5 và hồ sơ từng game. Dùng làm thang cho "cấp hiệu ứng" của dải (phím, từ, hoàn hảo, mốc chuỗi).
- `feedback/trauma.ts`: rung chỉ cho cảnh 3D, HUD không rung. Đúng luật cho dải: dải không bao giờ rung.
- `feedback/reaction.ts` (chớp trắng quái), `numbers.ts`, `debris.ts`, `hitstop.ts`: phía mục tiêu, game giữ.
- `feedback/quads.ts` (instanced quads của Three): **không dùng cho dải** (xem §5).
- `feedback/audio-cues.ts`: âm tổng hợp `key()`/`word()`. Giữ làm "bản thế tạm" trong Lab, ghi rõ nhãn.
- `typing/session.ts`, `router.ts`: mã `KEY` (`stray/lock/advance/done/wrong/switch/group/forgiven`). Chỉ Dragonhold dùng kit; Last Line có `feedback` mà không có `typing` trong `kit.config.json`, nên `typing-fx` **không được import** `../typing` (lệnh chép sẽ từ chối). Bộ chuyển `kitKind()` chỉ chép số, test đối chiếu với `KEY` thật.

## 4. Âm thanh dùng lại được

- Cả ba game đều dùng Web Audio thẳng: kit `audio/` (`SceneAudio`, `BusMix`) ở Last Line; engine riêng ở Dragonhold (`audio/index.ts`, `bank.ts` đã có đường nạp manifest file); `audio-min.ts` ở Wordwoven. Chưa game nào có file âm cho phím.
- Vậy nên bộ âm gõ dùng `AudioBuffer` nạp trước, nối vào bus của game (`destination`), dùng chung `AudioContext` của game (`context`). Không cần thư viện.

## 5. Chỗ đề xuất sai hoặc yếu

1. **PixiJS + pixi-filters:** thêm một ngữ cảnh WebGL thứ hai cạnh Three (Dragonhold, Last Line) tốn bộ nhớ GPU và một lớp ghép; ở Wordwoven nó là WebGL duy nhất. Glow/Bloom làm nhòe chữ, chính §13 của đề xuất cũng cảnh báo. **Bỏ.**
2. **Hạt trong cảnh Three (instanced quads):** cảnh 3D nằm dưới lớp DOM, có bloom và rung camera; hạt ở đó không thể nằm đúng quanh chữ DOM, và Wordwoven không có Three. **Dùng một canvas 2D nhỏ** cỡ dải (không phủ cả màn), đặt sau chữ.
3. **Howler:** trùng Web Audio đang có, thêm khoảng 10 kB gzip, Wordwoven không còn chỗ. **Bỏ.**
4. **Âm tổng hợp (§23) khi phát hành:** trái luật anh 28/10. Chỉ là bản thế tạm có nhãn trong Lab.
5. **Tải gói OpenGameArt hoặc dùng âm Monkeytype (GPL-3.0):** không. Quyết định của anh (29/10): mọi âm phím làm trong Audio Lab, không dùng gói tải về (xem §16).
6. **Công thức chữ quá yếu (§6, §45):** 1,08–1,14× và sáng 1,8 là đúng thứ anh chê. Typing Break dùng chữ 2,3–3,4× đóng xuống trong 50 ms và vòng hai tông 150 ms (T1, T2). Các kiểu dùng số của Typing Break; kiểu Minimal giữ cho người thích đọc.
7. **"TypingFeedbackEngine" với event bus:** ba game có ba lõi gõ khác nhau. Một bus tạo đối tượng mỗi phím là thừa. Đủ dùng: một giao diện `TypingFxSink` (gọi hàm, không tạo đối tượng) và một `TypingFxDriver` so trạng thái (từ nào, đã gõ mấy chữ) để phát lệnh. Phản hồi không bao giờ tự quyết đúng sai.
8. **Đề xuất không nói tới dải giữa màn hình**, là thứ anh muốn nhất. Đây là phần chính của module.
9. **Combo:** Typing Break không có bộ đếm combo (study §2.7). Ta dùng đường cong có trần `min(combo/20, 1)`; mốc 10, 25, 50, 100 nâng hiệu ứng từ, không chồng thêm.

## 6. Cách tốt hơn

- Chữ là `span` cố định, chỉ đổi `transform` và `opacity`; tư thế từng khung lấy theo bậc như Typing Break (đổi theo khung, không nội suy mượt), nên dễ đọc và nhẹ.
- Một canvas 2D nhỏ sau chữ cho vòng, tia, mảnh, mực; nghĩa tiếng Việt nằm trên canvas trong vùng bảo vệ.
- Chữ bay về mục tiêu là `span` lấy từ pool, không vẽ trên canvas cả màn.
- Âm: pool `AudioBuffer`, xoay vòng ngẫu nhiên không lặp liền, ±cao độ và âm lượng nhỏ, trần 6 tiếng cho phím và 2 tiếng riêng cho bộ `space` (xong từ).

## 7. Kiến trúc chốt

```text
lõi gõ của game (không đổi)
   └─ sự kiện của game (word-progress / wordKey / EV.keyOk …)
        └─ TypingFxDriver.progress({kind, word, text, meaning, typed, combo, perfect})
             ├─ FocusStrip   (DOM + canvas 2D nhỏ + pool chữ bay)   feedback/typing-fx/strip.ts
             └─ TypingSounds (AudioBuffer pool, hồ sơ âm)              feedback/typing-fx/audio.ts
cài đặt: { typingFx: { style, intensity, soundProfile, volume } }       feedback/typing-fx/settings.ts
```

Kiểu chữ (`styles.ts`): Stamp, Flare, Smash, Shatter, Rune, Minimal. Cường độ (`intensity.ts`): Off/Low/Normal/High/Ultra, mặc định Normal, theo `prefers-reduced-motion`. Thứ bậc: phím 1, từ 2, hoàn hảo 3, mốc chuỗi 4; hiệu ứng từ xóa hạt của chữ cuối, mốc chuỗi nâng hiệu ứng từ. Pool hạt (`pool.ts`) dạng mảng số, có trần, cướp hạt cũ nhất ưu tiên thấp nhất.

## 8. Điểm nối từng game (làm sau khi anh chọn kiểu, do làn của game)

| Game | Gắn dải vào | Sự kiện đưa vào driver | Đích cho chữ bay |
|---|---|---|---|
| Dragonhold | `#dh-overlay`, có `data-dh-avoid` để nhãn né dải | `word-progress` trong `onEvents` (`kind` = `key` của sự kiện, `pair` bỏ qua); `word-released` → `release` | Miệng Hỏa Long `heroes.mouth(out)` chiếu qua `map.stage.project` |
| Wordwoven | `#tdWords`; nạp lười bằng `import()` (trần gói) | `{t:"wordKey", result}` qua `kitKind(result)` (mã `KEY` giống kit); `wordHit` → `done` | Lũy (`buildings` ô 0) hoặc Draconis, qua `DebugView.project(x, z)` |
| Last Line | `#svHud`; dải thay `WordStrip` (chỉ giữ một dải) | `EV.keyOk` → `advance`, `EV.keyBad` → `wrong`/`stray`, `EV.word` → `done` trong `TypeFeel.read` | Lõi tàu `Ship.core(out)` qua `Stage.project(…, still)` |

## 9. Rủi ro hiệu năng

- `text-shadow` lớn: chỉ đặt tĩnh trên lớp "nóng" của chữ, chỉ đổi `opacity` → không vẽ lại mỗi khung.
- Đọc layout: chỉ một lần mỗi từ (`setWord`) và khi đổi cỡ màn; không đọc layout mỗi phím.
- Canvas: cỡ dải (≈ 22 × 4,2 chiều cao chữ), không xóa khi không có hạt.
- GC: pool hạt và tư thế là mảng số, không tạo đối tượng mỗi phím. Riêng Web Audio bắt buộc tạo một `AudioBufferSourceNode` mỗi lần phát (theo chuẩn, dùng một lần); nút gain lấy từ pool.
- Last Line đã có tia 3D mỗi phím: khi dùng dải mới, tắt pop của `WordStrip` cũ để không hai lớp phản hồi.

## 10. Rủi ro giấy phép và phụ thuộc

Không thêm phụ thuộc nào. Không tải file. Không dùng tài sản Monkeytype. Âm phím do Audio Lab làm ([`AUDIO_PIPELINE.md`](AUDIO_PIPELINE.md)); hồ sơ âm có trường `source` (`audio-lab` hoặc `synth`) và `licence`. Âm tổng hợp của kit chỉ là "Kit synth (test only)" trong Lab.

## 11. Các giai đoạn

0. Rà (văn bản này). 1. Module kit `feedback/typing-fx/` có test. 2. Typing Feedback Lab (`tools/typing-feedback-lab/`) để anh thử. 3. Anh chọn kiểu và hồ sơ âm. 4. Làn từng game nối vào (một game một lần, bắt đầu từ Last Line vì đã có dải). 5. Audio Lab làm mẫu âm thật theo danh sách §16.

## 12. File

- Mới: `shared/game-kit/feedback/typing-fx/{index,settings,intensity,pool,styles,driver,audio,draw,strip,css}.ts` và test (`logic`, `driver`, `audio`, `styles`); `tools/typing-feedback-lab/` (trang Vite, `scripts/capture.mjs`, `scripts/perf.mjs`, `scripts/sheets.py`); `.claude/launch.json` thêm `typing-fx-lab`; một dòng `shared/game-kit/DRIFT.md`.
- Không sửa: mã của game, `feedback/index.ts` (game import thẳng `kit/feedback/typing-fx`).

## 13. Kế hoạch test

- Đơn vị (vitest, cạnh mã): pool (trần, cướp, xóa theo chủ), thứ bậc và đường cong combo, cường độ, chọn biến thể không lặp liền, trần tiếng, driver với phiên gõ thật của kit, cài đặt hỏng về mặc định, mỗi kiểu xong trong ngân sách thời gian.
- Lab trong trình duyệt: gõ thật ở tốc độ cao, chuỗi khung ≥ 10 khung trong 1 s quanh phím, phím sai, xong từ, cho từng kiểu, ở 1280 và 1920; tờ ghép cạnh tờ Typing Break; số FPS, hạt, tiếng, phím/giây.
- Sau khi nối vào game: kịch bản trình duyệt của từng game, golden sim không đổi.

## 14. Lùi lại

Module chỉ thêm, game tự chọn dùng. Trong game: cường độ Off (dải tĩnh) hoặc không gắn dải. Trong kit: hoàn một commit.

## 15. Phán quyết

**DUYỆT CÓ SỬA.** Đồng ý với người điều phối ở cả bốn điểm (không PixiJS, không Howler, bloom tắt mặc định, phản hồi chỉ nhận sự kiện). Thêm một điểm phản biện có bằng chứng: không dùng instanced quads trong cảnh Three cho dải (Wordwoven là Canvas 2D; hạt 3D nằm dưới DOM và chịu bloom và rung), dùng canvas 2D nhỏ.

---

## 16. Âm phím: quyết định của anh (29/10)

- Mọi âm phím làm trong Audio Lab, không gói tải về. Cài đặt có một mục "Keyboard sound": năm hồ sơ và Off.

| id | Tên cho người chơi |
|---|---|
| `creamy` | Creamy |
| `thock` | Thock |
| `clicky` | Clicky |
| `dome` | Soft Dome |
| `spring` | Classic Spring |

- Mỗi hồ sơ: `key-01` … `key-10` và `space-01` … `space-03`, cân độ to giữa các hồ sơ, kèm `keys-manifest.json` trong `~/AudioLab/review/staging/keys/<id>/`.
- Kit (`audio.ts`): `TypingSounds.loadKeyboard(base, id)` đọc `<base>/<id>/keys-manifest.json`. Manifest dạng nào cũng được: mọi chuỗi kết thúc bằng `key-NN.<đuôi>` hoặc `space-NN.<đuôi>` được lấy, xếp theo số; đường dẫn ra ngoài thư mục bị bỏ. Đuôi nhận: ogg, opus, webm, m4a, mp3, wav, flac. Nạp và giải mã hết trước khi chơi. Không có manifest: "pending", im lặng, không có gì thế chỗ.
- Chữ đúng, chữ sai, phím lạc dùng bộ `key`; xong từ và phím cách dùng bộ `space`. Thứ bậc bằng độ to (`TYPING_SOUND_MAP`): lạc 0,32 < sai 0,42 < phím 0,55 < cách 0,6 < từ 0,68 < hoàn hảo 0,78 < mốc chuỗi 0,88. Không cần file riêng cho sai, hoàn hảo, mốc.
- Lab trỏ `/lab-keys/` vào thư mục staging. Hôm nay (29/10, 10:50) thư mục chưa có: cả năm hồ sơ hiện "(pending)".

## 17. Kết quả giai đoạn 1–2 (29/10)

**Module kit** `shared/game-kit/feedback/typing-fx/`: 45 test mới; cả kit 51 file, 764 test xanh; `tsc` sạch. Không import `typing/`, `three` hay module khác.

**Sáu kiểu chữ** (điểm tự chấm so với Typing Break, 10 là ngang bản tốt nhất của họ):

| Kiểu | Trông thế nào | Điểm |
|---|---|---|
| Stamp | Bản sao chữ 3× nghiêng −9° rơi xuống, đóng 1× ở 50 ms (T1); đĩa trắng và vòng sơn màu chữ bung ra khi chạm | 8 |
| Smash | Chữ 2,1× dưới đĩa trắng 2 khung, rồi vòng trắng dày, vòng màu viền tối, cung trắng, cung xoay 40°/khung (T2), xong ở 150 ms | 8 |
| Flare | Chữ trắng nóng phồng 1,24×, quầng màu chỉ trên chữ, tia lấp lánh 4 cánh ở góc, 3–4 tia bay lên | 7 |
| Shatter | Chữ tách đôi theo một nhát chém, hai nửa bật ra rồi khép lại ở 110 ms, 5–9 mảnh văng | 7 |
| Rune | Đường sáng vẽ viền chữ trong 120 ms giữa vòng phù văn xoay, chữ bừng sáng khi nét khép | 7 |
| Minimal | Đổi màu và nảy 1,12×, không hạt; cho người muốn đọc yên | 5 (cố ý nhẹ) |

Chung cho mọi kiểu:
- **Phím sai:** chữ đang chờ đỏ và giật ngang 4 khung (không phóng to), viền tấm đỏ 140 ms, dấu nhỏ theo kiểu.
- **Xong từ:** viền bật ra rồi ôm tấm (T3, vàng khi hoàn hảo), cả từ lóe, từ bị bóp ngang (T7), từng chữ bay lên khỏi tấm rồi vòng hai bên tấm về đích của game. Chữ không bao giờ đè lên từ mới.
- **Mốc chuỗi** (10, 25, 50, mỗi 50): nâng hiệu ứng từ (vòng sóng lớn, nhãn "25 COMBO"), không chồng thêm.

Điểm chung của phần xong từ: 8. Ta hơn Typing Break ở chỗ năng lượng đi về đích; kém ở chỗ tấm là kính CSS. Theo luật art của anh, làn game phải bọc tấm bằng art thật (`plateClass`).

**Lab:**
- Cách mở: `http://127.0.0.1:4192/`, tên chạy `typing-fx-lab` trong `.claude/launch.json` (`node shared/game-kit/node_modules/vite/bin/vite.js --config tools/typing-feedback-lab/vite.config.mjs`).
- Có ba nền chụp từ ba game, từ vựng ghim của từng game, mục "Today (approx.)" để so A/B, cùng bộ đếm FPS, hạt, tiếng, phím/giây và phím → khung.
- Phím `` ` `` ẩn/hiện bảng điều khiển.

**Tờ ghép:** nằm ở `tools/typing-feedback-lab/tmp/sheets/` (không vào Git).
- Mỗi kiểu ở mỗi cỡ một tờ, `sheet-<kiểu>-<1920x1080|1280x720>.jpg`: phím, phím sai, xong từ, mỗi loại 13 khung từ +0 đến +1000 ms. Bên dưới là tờ Typing Break tương ứng (T1 hoặc T2, rồi T3 và T7).
- Hai tờ tổng hợp: `sheet-overview-key-*.jpg`, `sheet-overview-word-*.jpg`.
- Khung thô đã xóa bằng `capture-prune` (468 file).

**Hiệu năng** (Apple M4, Chrome headless có GPU, `heavy.sh --perf`):
- Cách đo: bot 15 phím/giây (đo được 13,8–14,8), 4 % phím sai, 6 s mỗi ô, sáu kiểu × Normal/Ultra, ở 1920 và 1280. Số thô: `tools/typing-feedback-lab/tmp/perf/perf-*.json`.

| Chỉ số | 1920×1080 | 1280×720 |
|---|---|---|
| FPS | 60 mọi ô | 60 mọi ô |
| Khung p95 | ≤ 16,8 ms | ≤ 16,8 ms |
| `strip.update` mỗi khung, p95 (max) | 0,2–0,5 ms (0,9) | 0,2–0,5 ms (1,1) |
| Hạt đỉnh Normal / Ultra (trần 160 / 320) | 83 / 104 | 75 / 110 |
| Task dài | 0 | 0 |
| Phím thật (CDP) → khung, trung bình / max | 6,9 / 16,3 ms | 7,6 / 15,6 ms |
| JS heap cả Lab | 3,0–4,0 MB, không tăng | |

- Hiệu ứng chạy ngay trong khung của phím: tư thế khung 0 được ghi ngay trong lệnh `key()`.
- Không có ngữ cảnh WebGL mới. Chỉ một canvas 2D cỡ dải (≈ 24 × 4,6 cỡ chữ).
- Tiếng: đỉnh 3–4 trên trần 6 + 2. Số này đo bằng file thử Kenney trước quyết định của anh; giờ hồ sơ còn pending nên sẽ đo lại bằng `PROFILE=creamy` khi Audio Lab giao file.
- Gõ thật trong trình duyệt của app: 36 phím, 7 từ, 0 sai, hạt đỉnh 121.

## 18. Việc nối vào từng game (làm sau khi anh chọn)

Chung cho cả ba game:
- `new FocusStrip({ root, anchor, palette, settings, target, font, plateClass })`.
- `new TypingSounds({ context: <AudioContext của game>, destination: <bus sfx> })`, rồi `loadKeyboard(<base của game>, id)` cho hồ sơ người chơi chọn.
- `new TypingFxDriver([strip, sounds])`. Mỗi sự kiện gõ điền một `TypingFxProgress` dùng lại.
- Cài đặt: `typingFx { style, intensity, soundProfile, volume }`, lưu trong save của game, đọc qua `sanitizeTypingFx`.
- Đồng hồ ngược (ván mới): `strip.reset()`.

| Game | Gắn vào | Sự kiện → `kind` | Đích (`target(out)`, tọa độ trong root) | Lưu ý |
|---|---|---|---|---|
| Dragonhold | `#dh-overlay` (tấm mang `data-dh-avoid`, nhãn tự né) | `word-progress.key`: `lock/advance/done/wrong/switch/stray/back` dùng thẳng, `pair` bỏ qua; `word-released` → `release`; `typed` từ sự kiện; combo = chuỗi của HUD | Miệng Hỏa Long: `heroes.mouth(out)` qua `map.stage.project` | Khung học ở đáy vẫn giữ; xem có cần bớt `dh-letter` trên nhãn khi dải bật |
| Wordwoven | `#tdWords`; `import()` lười (trần gói 85 kB còn 25 byte) | `{t:"wordKey", result}` qua `kitKind(result)` (mã KEY giống kit); `wordHit` → `done`; lời gọi tự khóa → `show` | Lũy (`buildings` ô 0) hoặc Draconis: `DebugView.project(x, z)` | Thêm `feedback` vào `kit.config.json` |
| Last Line | `#svHud`; thay `WordStrip` (chỉ một dải) | `EV.keyOk` → `advance` (`typed` = value), `EV.keyBad` → `wrong` (ô −1 → `stray`), `EV.word` → `done`, đọc trong `TypeFeel.read` | Lõi tàu: `Ship.core(out)` qua `Stage.project(…, still)` | Tia 3D mỗi phím của game vẫn giữ; tắt pop của `WordStrip` cũ |

## 19. Còn lại

- Anh chọn kiểu mặc định (đề xuất: Stamp hoặc Smash), cường độ và vị trí dải trong Lab.
- Audio Lab giao năm hồ sơ phím; Lab tự nhận khi `keys-manifest.json` có mặt (tải lại trang). Sau đó đo lại tiếng bằng `perf.mjs` với `PROFILE=<id>`.
- Làn từng game: nối theo §18, bọc tấm bằng art thật, rồi chạy kịch bản trình duyệt của game.

## 20. Cập nhật 29/10 chiều: việc đã làm và việc còn lại (dừng vì hết ngữ cảnh)

**Đã làm (commit trong repo cha, chưa push):**
- `33836dc2`: cài đặt cỡ dải `size` (Medium / Large / Huge, mặc định Large: chữ hoa ~40 px ở 720p, ~56 px ở 1080p; Huge ~52 / 72). Mặc định Stamp. `setAnchorPx(x, y, "bottom")` để game ghim đáy dải vào một đường. Lab có nút Size.
- `9fb51362`: mặt nạ chữ (`mask`, luật "Thiếu chữ" của Last Line: chữ ẩn hiện "_" tới khi gõ hoặc lộ ra), `glyphPoint()` (gốc tia 3D của Last Line), `rect()` (vùng cấm số sát thương).
- Commit này nâng cấp Stamp theo mức 9 điểm:
  - bóng tối rơi dưới bản sao chữ;
  - chạm đáy thì bẹp, vọt rồi đứng (khung 60 Hz);
  - vết sơn có mép tối;
  - giọt sơn rơi có trọng lực, đập xuống đường kẻ thì bẹt ra;
  - vòng chạm dẹt ở chân chữ, ánh lóe;
  - ánh sáng lan sang chữ kế bên;
  - xong từ thì đóng một con dấu khung đôi lên cả từ.
- Móc texture `setTextures({ spark, ink, seal, ember })` cho gói tranh Codex 173–175. Chưa có texture thì vẽ hình thủ tục.
- `scripts/ab_sheet.py`: tờ A/B cạnh khung Typing Break cắt thẳng từ `typing_break.mov`, cùng thời điểm, cùng cỡ.
- Kit 48 test xanh.

**Tờ A/B Stamp:** `tools/typing-feedback-lab/tmp/sheets/ab-stamp-1920x1080.jpg`. Điểm tự chấm sau nâng cấp, chưa đạt 9:

| Hạng mục | Điểm | Còn thiếu |
|---|---|---|
| Phím | 8,5 | Vết sơn dưới chữ thiếu tương phản trên tấm tối; cần sprite `ink-splash` thật hoặc tấm sáng hơn quanh chữ đang gõ |
| Xong từ | 8,5–9 | Đạt dáng; cần judge |
| Gõ sai | 8 | Cần một nhịp mạnh hơn mà không che chữ sau, ví dụ vết đỏ dưới chữ và gạch chân giật |

Bản 1280 chưa chụp: lần chụp chờ GPU của làn khác quá giờ.

**Còn lại, theo thứ tự người điều phối (29/10):**

1. **Khảo sát thư viện miễn phí** (luật mới §5 của `SHARED_SYSTEMS_BAR.md`: MIT, BSD, ISC, Apache-2.0, MPL-2.0; không GPL hay NC; kiểm giấy phép tại nguồn; ghi `docs/games/THIRD_PARTY.md`).
   - Ứng viên: Motion, anime.js v4 (MIT), GSAP (kiểm điều khoản "no charge" của Webflow), một thư viện tách chữ.
   - Hạt: tsParticles chỉ khi hợp DOM + canvas nhỏ; với Three thì three.quarks hoặc three-nebula, pmndrs `postprocessing` cho glow.
   - Chọn theo chất lượng, độ mượt, cỡ gói (Wordwoven phải nạp lười) rồi ghi lý do vào đây.
   - Gói tài sản (texture, âm) cần anh duyệt từng gói: chỉ liệt kê tên, nguồn, giấy phép, cỡ.
2. **Nâng Stamp lên 9:** áp các sửa của bảng trên, chụp lại hai cỡ, rồi hai judge chấm.
3. **Nâng năm kiểu kia lên 9** cùng cách: bóng hoặc độ sâu, theo đà, ánh sáng lan sang chữ bên, cách xong từ riêng của từng kiểu, móc texture.
   - Smash: vòng hai tông quanh cả từ.
   - Flare: chùm sáng và tia lửa `ember`.
   - Shatter: cả từ vỡ thành mảnh trước khi bay.
   - Rune: vòng phù văn bao cả từ.
   - Minimal: giữ nhẹ nhưng tinh.
   Mỗi kiểu có tờ A/B (`ab_sheet.py`) trước khi gọi là xong.
4. **Kit `shared/game-kit/ui/quick-settings/`** (spec `docs/games/IN_GAME_SETTINGS.md`, chưa đọc). Có test.
   - Hai nút trong trận: bánh răng Settings và loa Sound, cùng góc trên phải ở mọi game; mở bằng chuột, `F1`/`F2`; đóng bằng `Esc`.
   - Panel mở thì game dừng và gõ không nhận phím. Đóng thì đếm 3-2-1, không mất từ đang gõ.
   - Đổi là áp ngay và lưu vào save của game.
   - Panel Sound: Master (thanh trượt và tắt tiếng), Music, Effects, Voice, Interface; Keyboard sound (Off và năm hồ sơ, nghe thử khi chọn); Keyboard volume.
   - Panel Settings: kiểu chữ, cường độ, cỡ (có xem trước nhỏ); đồ họa Low–Ultra; giảm chuyển động; các công tắc học; Resume và Quit to title; một chỗ cho mục riêng của game.
   - Icon là ảnh thật (Codex 180) nhận theo tên. Chưa có ảnh thì dùng nút chữ, không vẽ bằng CSS.
   - Cân nhắc thư viện slider hoặc panel có sẵn, truy cập được, nếu tốt hơn bản tự làm.
5. **Last Line** (worktree `games/.wt-ts-typefx`, nhánh `ts-typefx` từ `79db628`, kit đã đồng bộ ở `9fb51362`, chưa sửa mã game). Cần đồng bộ lại sau mỗi commit kit. Kế hoạch đã dò:
   - **Module mới `src/view/type-fx.ts`** giữ `FocusStrip`, `TypingSounds`, `TypingFxDriver`:
     - đáy dải ghim ở đường cũ: `setAnchorPx(stage.width / 2, line, "bottom")`; `line` lấy từ `Hud.layout`, thêm `placed.line`;
     - đích chữ bay: `ship.core(v)` rồi `stage.project(v.x, -v.z, v.y, out)`, như `TypeFeel.probe`;
     - màu theo súng: `--xung` / `--tia` = `--volt` / `--hot`, `#ffc53d`, `#8fa3ff`, `#ff3f6c`. Gọi `setPalette` khi súng đổi; nên thêm bộ đệm sprite theo bảng màu trong `FxCanvas`.
   - **Sự kiện, trong `TypeFeel.read`:**
     - `EV.keyOk` (`slot`, `value` = số chữ đã gõ) → `advance`. Id từ = `slot * 100000 + chỉ số deck`. Nếu cùng tick có `EV.word` của ô đó thì lấy chỉ số deck từ `R.ref` của nó, vì `T.word[slot]` có thể đã đổi.
     - `EV.keyBad`: ô −1 → `stray`, còn lại → `wrong`, với `mask = T.hidden[s] & ~T.shown[s]`.
     - `EV.word` → `done`: `perfect` = `FLAG.perfect`, combo = `streak.n` sau khi `streak.word()`.
     - Mỗi khung: khóa mất thì `release`; `T.typed` giảm thì `back`.
   - **`WordStrip` cũ:** ẩn tấm `.sv-strip` và `.sv-strip-ghost` bằng class trên `#svHud`. Giữ đèn chuỗi "CLEAN ×N", cảnh báo rift và vạch quái gần, nhưng đặt theo `rect()` của dải mới (thêm chế độ `host` trong `strip.ts`). `TypeFeel.land` dùng `glyphPoint()` thay `strip.anchor()`. `Hud.protectedRects` dùng hộp rộng nhất của dải mới.
   - **Âm phím:**
     - `TypingSounds({ context, destination })` nối vào context và bus sfx của `ThemeAudio`; cần thêm getter context và bus vào `theme-audio.ts`.
     - Gốc URL `/assets/typing-survival/audio/keys/`.
     - Hồ sơ còn "pending" thì giữ tiếng tổng hợp cũ (`audio.key` / `audio.keyBad`) và báo anh. Hồ sơ sẵn sàng thì thay. "Off" thì tắt cả hai.
   - **Cài đặt:** `survival.settings.typingFx` qua `sanitizeTypingFx`. Các dòng Options (Letter effect, Effect strength, Word size, Keyboard sound, Keyboard volume) chuyển vào quick-settings của bước 4.
   - **Kiểm:** `pnpm check` xanh; golden không đổi (chỉ sửa view và app); tờ khung 1280 và 1920 cho phím, phím sai, xong từ, combo qua `heavy.sh --gpu`; xóa khung thô; changelog `docs/changelog/2026-10-29-typing-fx.md`; commit trên `ts-typefx`, không merge, không push.

## 21. Khảo sát thư viện (làn TF2, 29/10)

Luật: `SHARED_SYSTEMS_BAR.md` §5. Giấy phép đọc tại nguồn (file LICENSE trong repo hoặc trang giấy phép), cỡ gói đo bằng esbuild, minify, gzip -9, chỉ phần import thật dùng.

| Ứng viên | Bản | Giấy phép (nguồn) | Cỡ gzip | Kết luận |
|---|---|---|---|---|
| Motion (`motion`) | 14.7.1 | MIT (`LICENSE.md` repo motiondivision/motion) | `animate` 25,1 kB; `motion/mini` 3,3 kB; `spring` 1,9 kB | **Không dùng cho dải.** Xem lý do 1–3 |
| anime.js v4 (`animejs`) | 4.5.0 | MIT (`LICENSE.md` repo juliangarnier/anime) | `animate` 12,6 kB; thêm timeline 16,8 kB; `createSpring` 1,8 kB | **Không dùng cho dải**, cùng lý do |
| GSAP | 3.15.0 | "Standard no charge" của Webflow (gsap.com/standard-license), không phải MIT/BSD/ISC/Apache/MPL; Webflow đổi điều khoản thì dùng tiếp là chấp nhận; cấm dùng trong công cụ dựng animation trực quan | — | **Loại**: giấy phép ngoài danh sách §5 |
| SplitType | 0.3.4 | ISC (npm) | 4,5 kB | Không cần: dải tự dựng mỗi chữ một span từ chuỗi |
| tsParticles (`@tsparticles/slim`) | 4.5.0 | MIT | 48,3 kB | **Loại**: vòng lặp và canvas riêng, cấu hình theo cảnh, không bắn theo từng chữ; nặng gấp 4 lần cả module |
| three.quarks | 0.17.1 | MIT (`LICENSE` repo) | — | **Loại**: đòi `three >= 0.182`, ba game đang ở 0.170; lại chỉ vẽ trong cảnh 3D |
| three-nebula | 13.3.0 | MIT | — | Không giúp dải DOM; hạt 3D của game đã có `three/` của kit |
| pmndrs `postprocessing` | 6.39.5 | Zlib (`LICENSE.md` repo): dễ dãi nhưng **không có trong danh sách §5** | — | Không dùng: glow của dải là canvas 2D, bloom chỉ áp cảnh 3D. Muốn dùng cho cảnh thì xin anh duyệt Zlib |
| a11y-dialog | 8.1.5 | MIT (`LICENSE` repo KittyGiraudel/a11y-dialog) | 1,7 kB | **Dùng** cho hai bảng quick-settings: bẫy Tab, `Esc` đóng, trả focus về ô gõ, `aria-modal` |
| `@zag-js/slider` | 1.47.0 | MIT | 9,7 kB | Không dùng: cần lớp dán vanilla riêng; `<input type="range">` gốc đã truy cập được (phím mũi tên, Home/End, trình đọc màn hình) và nhận ảnh thật qua CSS |

**Vì sao dải không dùng thư viện tween:**
1. Phong cách đã chốt là bước theo khung 60 Hz như Typing Break (§17, T1–T2): mỗi khung là một tư thế đặt sẵn, mắt đọc "con dấu", không đọc đường tween. Tween mượt của Motion hay anime.js làm mất chính cái chất đó.
2. Chữ (DOM) và hạt (canvas) chạy chung một `requestAnimationFrame`, nên vết sơn hiện đúng khung chữ chạm đáy (50 ms). WAAPI của Motion chạy trên compositor, lệch nhịp với canvas.
3. Ở 15 phím/giây, mỗi phím tạo một animation mới là cấp phát và GC; dải hiện không cấp phát gì theo phím. Cả module nặng ~12 kB gzip, Wordwoven nạp lười.

Chỗ còn thiếu để lên 9 nằm ở **tranh** (vết mực, tia lửa, dấu ấn thật) và nhịp từng kiểu, không ở bộ tween. Vì vậy:

**Gói tài sản đề xuất (chưa tải, chờ anh duyệt từng gói):**

| Gói | Nguồn | Giấy phép (trang gói) | Cỡ | Cắm vào |
|---|---|---|---|---|
| Kenney Splat Pack | https://kenney.nl/assets/splat-pack | CC0 | 30 file | `setTextures({ ink })`: vết mực dưới chữ Stamp, vết đỏ khi gõ sai |
| Kenney Particle Pack | https://kenney.nl/assets/particle-pack | CC0 | 80 file, 512 × 512 | `spark`, `ember`, `star`: tia và ánh lóe cho Flare, Smash, Rune |

Hai gói CC0 không bắt ghi công (vẫn ghi vào `THIRD_PARTY.md` khi dùng). Codex 173–175 vẫn là đường chính; gói Kenney là đường nhanh nếu anh muốn xem trước.
