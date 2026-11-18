# Wordwoven · Map 1 Silverfall Meadow · Danh sách Adobe Firefly SFX

**61 hàng · 85 lượt dự kiến** (P0 43, P1 30, P2 12)

Chỉ dành cho **Adobe Firefly Generate Sound Effects** do chủ dự án tạo. Chưa tạo âm, chưa nghe duyệt, chưa gắn vào game. Nguồn: `td-1c@2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7`; checkout chỉ đọc `a2-days@f9abfd09987dadd519233c2f38692758d35cefca`.

## Cách dùng

Độ dài bên dưới là một cú đã cắt, không phải độ dài file kết quả. Dự toán theo [README](README.md): 12 s/file, một giây lặng sau mỗi cú, tối đa 8 cú, giả định 75% dùng được và thêm một file dự phòng P0. Một lượt là một file kết quả; số thao tác và credit chưa biết. Tỷ lệ 75% chưa đo. Tất cả hàng hiện là cú rời, riêng boss-lull là một đoạn single; không có loop âm nền vì mã chưa phát id nền.

Giữ tên WAV Firefly đặt, giữ gốc và prompt. Thư mục nhận là dữ liệu, chưa được tạo. 217 chọn/cắt/chuẩn hóa; phiếu gắn sau giữ nguyên tick sim và trần âm hiện tại. Prompt có phần chuẩn bị cực ngắn tại đầu cú khi hành động có; A của đòn chữ chạy trong lúc gõ, không thêm gồng sau phím cuối. Kho 3D FxPool (src/view/3d/fx-pool.ts:175–218) tạo bit ở tuổi 0, cập nhật theo dt; pool không chứng minh từng đòn đã đủ pha. Các mốc view dưới đây là đọc mã, chưa phải nghiệm thu hình hoặc nghe. Ở 60 Hz, I khớp event; lớp hình sau có thể lệch 2–3 khung theo chuẩn, không dời sát thương.

Giọng đọc từ được ưu tiên: âm dày có đầu sáng ngắn, phần ngân dưới 1 kHz hoặc trên 4 kHz; mục tiêu giảm dải 1–4 kHz ít nhất 15 dB trong 100 ms thuộc bước nghe/ingest, prompt chưa chứng minh đạt. Bus giữ nguyên busOf. Khả năng dùng gợi ý giọng của Firefly chưa biết; voiceHint hiện null.

## Tổng theo buổi tạo

| Nhóm | Hàng | Lượt |
|---|---:|---:|
| gõ và lời gọi | 16 | 25 |
| đạn, trúng, chết | 13 | 25 |
| boss Mộc Tinh | 12 | 14 |
| ngày và đêm | 8 | 8 |
| công trình và kinh tế | 8 | 9 |
| UI và nền | 4 | 4 |

## Tóm tắt từng id

| `id` | Tên trong game | Ưu tiên | Lượt |
|---|---|---|---:|
| `key-wrong` | — | P0 | 2 |
| `key-lock` | — | P0 | 2 |
| `key-group` | — | P0 | 2 |
| `word-hit` | — | P0 | 3 |
| `word-hit-bell` | — | P0 | 2 |
| `chain-step` | — | P0 | 2 |
| `chain-tier` | — | P0 | 2 |
| `chain-callout` | — | P0 | 2 |
| `call-power` | Power | P1 | 1 |
| `call-build` | Build | P1 | 1 |
| `call-harvest` | Reap | P1 | 1 |
| `call-chop` | Chop | P1 | 1 |
| `call-mine` | Dig | P1 | 1 |
| `call-quiz` | Quiz | P1 | 1 |
| `call-ult` | Spell | P1 | 1 |
| `call-direct` | Stop | P1 | 1 |
| `wordshot-fire` | Word Shot | P0 | 2 |
| `arrow-fire` | Archer Tower | P0 | 2 |
| `cannon-fire` | Cannon Tower | P0 | 2 |
| `bolt-fire` | Fort | P0 | 2 |
| `fireball-fire` | — | P0 | 2 |
| `hit` | — | P0 | 2 |
| `blast` | — | P0 | 2 |
| `ink-puff` | — | P0 | 2 |
| `block` | Soldier | P1 | 1 |
| `soldier-down` | Soldier | P0 | 2 |
| `fizzle` | Word Shot | P0 | 2 |
| `direct-break` | Stop | P0 | 2 |
| `ult-cast` | Fire Feather Rain | P0 | 2 |
| `boss-warn` | — | P1 | 1 |
| `boss-lull` | — | P1 | 2 |
| `boss-emerge` | — | P1 | 1 |
| `boss-phase` | — | P1 | 1 |
| `boss-roots` | — | P1 | 1 |
| `boss-roots-hit` | — | P1 | 1 |
| `boss-slam` | — | P1 | 1 |
| `boss-drain` | — | P1 | 1 |
| `boss-drain-hit` | — | P1 | 1 |
| `boss-summon` | — | P1 | 1 |
| `boss-hit` | — | P0 | 2 |
| `boss-retreat` | — | P1 | 1 |
| `night-fall` | — | P1 | 1 |
| `dawn` | Dawn | P1 | 1 |
| `day-countdown` | — | P2 | 1 |
| `wave-start` | — | P1 | 1 |
| `night-called` | — | P1 | 1 |
| `leak` | Fort | P1 | 1 |
| `defeat` | Defeat | P1 | 1 |
| `victory` | Village saved | P1 | 1 |
| `build-start` | Build | P2 | 1 |
| `build-done` | — | P2 | 1 |
| `sell` | — | P2 | 1 |
| `house-stun` | — | P1 | 1 |
| `harvest-done` | Rice Field | P2 | 1 |
| `tree-fall` | Chop | P2 | 2 |
| `coin` | Gold | P2 | 1 |
| `helper-panic` | — | P1 | 1 |
| `ui-move` | — | P2 | 1 |
| `ui-pick` | — | P2 | 1 |
| `ui-off` | — | P2 | 1 |
| `ui-lamp` | — | P2 | 1 |

# Buổi tạo: gõ và lời gọi

## `key-wrong`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: phím sai hoặc lạc khi gõ bất kỳ lời gọi nào.

**Độ dài:** 32–48 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A fingertip-sized bamboo clapper slips against its damp wooden mate, a dull offset click with a compact woody body and a quick natural decay. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Thẻ cũ giữ tổng hợp; mục 6 của phiếu giữ phím sai thành hàng riêng, xác nhận commit 646e889; đổi gỗ đục thành phách tre lệch theo §8.2.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/key-wrong.yaml: duration.min_ms=32, max_ms=48, variants.target=2; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/key-wrong/`.

## `key-lock`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: phím khóa từ; cùng nhịp key-right.

**Độ dài:** 30–60 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A small bamboo latch seats firmly, a tight click with a brief hollow body and a clean close decay. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · charge:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=30–60 ms, variants=3 theo src/view/sound-map.ts:37, src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/sound-map.ts:37; src/sim/events.ts:66: mốc kết quả lock, không có độ dài mẫu trong mã.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/sound-map.ts:37; src/sim/events.ts:66: mốc kết quả lock, không có độ dài mẫu trong mã.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/key-lock/`.

## `key-group`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: router chấp nhận một nhóm chữ.

**Độ dài:** 40–90 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A pair of thin bamboo slats settles together, a compact interlocking rattle and a short woody release. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · charge:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=40–90 ms, variants=3 theo src/view/sound-map.ts:37, src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/sound-map.ts:37; src/sim/events.ts:66: mốc kết quả group, không có độ dài mẫu trong mã.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/sound-map.ts:37; src/sim/events.ts:66: mốc kết quả group, không có độ dài mẫu trong mã.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/key-group/`.

## `word-hit`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Luôn phát theo wordHit: mỗi từ hoàn tất; cao độ tùy điểm và chuỗi.

**Độ dài:** 640–960 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 7; **3 lượt**, 6 cú/lượt dự kiến; **P0**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A small bronze hand bell is struck with a light beater, a bright precise onset followed by a warm pitched ring and a delicate rising bend. Create six pentatonic pitches C4 D4 F4 G4 A4 C5 and one upward inflection across the sequence. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Thẻ và THEME_SOUND_LIST:32 dùng đàn tranh; §8.2 đòi chuông đồng nhỏ nên chọn chuông. Giữ 7 biến thể, đề xuất 6 cao độ và 1 luyến, chưa phải engine chọn theo nốt.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/word-hit.yaml: duration.min_ms=640, max_ms=960, variants.target=7; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/word-hit/`.

## `word-hit-bell`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: wordHit đạt Perfect hoặc Flash, thêm trên word-hit.

**Độ dài:** 400–600 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **2 lượt**, 7 cú/lượt dự kiến; **P0**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A tiny bronze hand bell receives a delicate strike, a high clear shimmer with a slender ringing body and a graceful fading tail. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** kept — Giữ chuông đồng nhỏ của thẻ và §8.2; viết lại ASCII, bổ sung hình dạng thân và đuôi.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/word-hit-bell.yaml: duration.min_ms=400, max_ms=600, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/word-hit-bell/`.

## `chain-step`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: tăng chuỗi mà chưa lên bậc và chưa tới mốc gọi.

**Độ dài:** 160–300 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A small Vietnamese sixteen-string zither gives one ascending pentatonic pluck, a crisp fingertip release, a warm resonant body and a brief open-air decay. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=160–300 ms, variants=3 theo src/view/sound-map.ts:39, src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/sound-map.ts:39; src/sim/events.ts:70: mỗi lần chuỗi tăng chưa qua tier.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/sound-map.ts:39; src/sim/events.ts:70: mỗi lần chuỗi tăng chưa qua tier.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/chain-step/`.

## `chain-tier`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: chuỗi vừa vượt ngưỡng bậc, chưa có callout.

**Độ dài:** 300–600 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **2 lượt**, 7 cú/lượt dự kiến; **P0**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A small Vietnamese sixteen-string zither answers with two rising pentatonic plucks, clear string releases, linked resonant bodies and a compact resolving tail. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=300–600 ms, variants=3 theo src/view/sound-map.ts:39, src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/sound-map.ts:39; src/sim/events.ts:70: một nhịp lên bậc, đề xuất hai nốt ngắn.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/sound-map.ts:39; src/sim/events.ts:70: một nhịp lên bậc, đề xuất hai nốt ngắn.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/chain-tier/`.

## `chain-callout`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: đạt mốc chuỗi có callout.

**Độ dài:** 360–540 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **2 lượt**, 7 cú/lượt dự kiến; **P0**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A Vietnamese bamboo flute plays three rising pentatonic notes, a clean breath onset, a clear open bore tone and a short airy release across a limestone courtyard. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Giữ câu sáo ba nốt; bỏ chất vui làng nhỏ, chuyển không gian sân đá vôi rộng theo §2.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/chain-callout.yaml: duration.min_ms=360, max_ms=540, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/chain-callout/`.

## `call-power`

**Tên trong game:** Power

Có điều kiện: thẻ Power sáng; ban đêm, tháp hoặc Fort có mục tiêu.

**Độ dài:** 320–480 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. Two quick strokes on a two-headed Vietnamese rice-paste barrel drum, a taut skin attack, a warm mid-low shell body, the second stroke gentler, and a short stone-courtyard resonance. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Giữ chức năng báo lời gọi; diễn bằng chất liệu hành động trong sân đá vôi rộng (§2, §8.2), không thêm giọng người.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/call-power.yaml: duration.min_ms=320, max_ms=480, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/call-power/`.

## `call-build`

**Tên trong game:** Build

Có điều kiện: thẻ Build sáng; mở việc xây hoặc nâng cấp.

**Độ dài:** 240–360 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A small hammer lifts and taps a substantial bamboo scaffold twice, crisp contacts spaced 0.13 seconds apart, hollow post resonance and a brief airy decay. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Giữ chức năng báo lời gọi; diễn bằng chất liệu hành động trong sân đá vôi rộng (§2, §8.2), không thêm giọng người.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/call-build.yaml: duration.min_ms=240, max_ms=360, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/call-build/`.

## `call-harvest`

**Tên trong game:** Reap

Có điều kiện: thẻ Reap sáng; Rice Field có lúa chín.

**Độ dài:** 720–1080 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 5 cú/lượt dự kiến; **P1**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A hand-sized iron sickle sweeps through ripe rice, a bright blade swish, a crisp stalk cut, a soft grain rustle and a light metallic fading ring. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Thẻ cũ dùng chuông; §8.2 đòi liềm nên đổi thành lưỡi liềm và lúa.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/call-harvest.yaml: duration.min_ms=720, max_ms=1080, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/call-harvest/`.

## `call-chop`

**Tên trong game:** Chop

Có điều kiện: thẻ Chop sáng; chọn cây để chặt.

**Độ dài:** 200–300 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A hand axe draws back and bites a mountain-tree trunk, a firm wooden crack, a resonant timber body, falling splinters and a short valley reflection. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Giữ chức năng báo lời gọi; diễn bằng chất liệu hành động trong sân đá vôi rộng (§2, §8.2), không thêm giọng người.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/call-chop.yaml: duration.min_ms=200, max_ms=300, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/call-chop/`.

## `call-mine`

**Tên trong game:** Dig

Có điều kiện: thẻ Dig sáng; Gold Mine đã mở ngày 3, đống vàng đủ ngưỡng.

**Độ dài:** 240–360 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A small iron hoe lifts and touches limestone twice, clear high contacts spaced 0.06 seconds apart, a fine stone scrape and a compact metallic decay. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Giữ chức năng báo lời gọi; diễn bằng chất liệu hành động trong sân đá vôi rộng (§2, §8.2), không thêm giọng người.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/call-mine.yaml: duration.min_ms=240, max_ms=360, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/call-mine/`.

## `call-quiz`

**Tên trong game:** Quiz

Có điều kiện: thẻ Quiz sáng; ban ngày có Helper và từ trong sổ ôn.

**Độ dài:** 280–420 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A palm-sized bronze hand bell sounds a curious rising two-note signal, clear light contacts, a gentle pitched body and a brief airy decay. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Thẻ cũ dùng sáo; chọn chuông cho Quiz theo thứ tự chất liệu lời gọi trong §8.2.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/call-quiz.yaml: duration.min_ms=280, max_ms=420, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=typing; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/call-quiz/`.

## `call-ult`

**Tên trong game:** Spell

Có điều kiện: thẻ Spell sáng; từ Đêm 3, thi triển chiêu cuối đủ năng lượng.

**Độ dài:** 400–800 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 6 cú/lượt dự kiến; **P1**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A medium two-headed Vietnamese rice-paste barrel drum gathers a short accelerating roll, a firm accented release, a rounded skin resonance and a compact stone-courtyard tail. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Giữ chức năng báo lời gọi; diễn bằng chất liệu hành động trong sân đá vôi rộng (§2, §8.2), không thêm giọng người.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=400–800 ms, variants=2 theo src/view/sound-map.ts:12,36, src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295; src/sim/systems/ult.ts:67; src/content/rules.ts:94: cửa sổ Spell lifeS=4, không phải độ dài âm báo.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295; src/sim/systems/ult.ts:67; src/content/rules.ts:94: cửa sổ Spell lifeS=4, không phải độ dài âm báo.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/call-ult/`.

## `call-direct`

**Tên trong game:** Stop

Có điều kiện: thẻ Stop sáng; Đêm 4, Raccoon Dog bắt đầu cơ chế trong tầm.

**Độ dài:** 250–500 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `typing`.

```text
An edited Foley sequence of isolated sound effects. A small iron alarm plate is struck once with a hard wooden beater, a clear urgent contact, a compact metallic body and a short open-air decay. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sự kiện RareEvent ở frame đọc (src/view/audio-min.ts:168–184), thẻ chữ đọc cùng nhịp. Ý đồ §8.2: mực vàng và chỉ dệt ở chữ; không thêm chờ vào sim.

**Chất liệu:** reworded — Giữ chức năng báo lời gọi; diễn bằng chất liệu hành động trong sân đá vôi rộng (§2, §8.2), không thêm giọng người.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=250–500 ms, variants=2 theo src/view/sound-map.ts:12,36, src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295; src/content/slice-1a.ts:118,190; src/view/sound-map.ts:12,36: lời gọi ngắt Raccoon Dog ở đêm 4.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/words/cards.ts:29; src/sim/systems/economy.ts:286–295; src/content/slice-1a.ts:118,190; src/view/sound-map.ts:12,36: lời gọi ngắt Raccoon Dog ở đêm 4.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/call-direct/`.

# Buổi tạo: đạn, trúng, chết

## `wordshot-fire`

**Tên trong game:** Word Shot

Có điều kiện: hoàn tất Power ở tháp và còn mục tiêu trong tầm.

**Độ dài:** 280–420 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A quick arm draw tensions an arm-sized paper-and-bamboo projectile; it releases with a tight whip crack and a high bronze ting, a fast rushing papery body travels away, and a short low limestone-valley echo fades behind it. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: rewards.ts:55 dùng launch với attack của tháp, không có SPEED riêng: Archer Tower 30 m/s, 10–12 m → 333–400 ms; Cannon Tower 18 m/s, 9–10 m → 500–556 ms (slice-1a.ts:41–59; compile.ts:42). Fort dùng bolt, không phải wordShot (rewards.ts:51). Ý đồ §8.2: A trong gõ, R vút mạnh và ting tại tháp, T chữ theo đạn, I hit hoặc blast; không đợi đuôi âm.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/wordshot-fire.yaml: duration.min_ms=280, max_ms=420, variants.target=4; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/content/slice-1a.ts:25–30,41–59,148; src/sim/systems/combat.ts:76–86,135–137; src/sim/systems/rewards.ts:44–55. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/wordshot-fire/`.

## `arrow-fire`

**Tên trong game:** Archer Tower

Có điều kiện: Archer Tower sẵn nhịp và có mục tiêu, trần 4/s.

**Độ dài:** 160–240 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A small bamboo bow flexes briefly, the taut string snaps forward, a slender arrow hisses into the distance, and a short low reflection crosses the limestone courtyard. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: FX.fire tại tháp (combat.ts:76–86,135–137); 30 m/s, tầm 10/11/12 m nên bay tới mục tiêu đứng yên ở rìa tầm khoảng 333/367/400 ms (20/22/24 khung 60 Hz); slice-1a.ts:41–45. Ý đồ §8.2: A căng dây trong gõ, R ở cung ngay tick bắn, T theo tên, I dùng hit, F rung; không đợi toàn file mới bắn.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/arrow-fire.yaml: duration.min_ms=160, max_ms=240, variants.target=4; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/content/slice-1a.ts:25–30,41–59,148; src/sim/systems/combat.ts:76–86,135–137; src/sim/systems/rewards.ts:44–55. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/arrow-fire/`.

## `cannon-fire`

**Tên trong game:** Cannon Tower

Có điều kiện: từ ngày 3, Cannon Tower có mục tiêu mặt đất.

**Độ dài:** 400–800 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **2 lượt**, 6 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A waist-high bronze cannon releases from a ready breech with a forceful muzzle crack, a dense pressure roar and a shell hiss receding outward, followed by a low stone-valley echo. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: FX.fire tại nòng; 18 m/s, tầm 9/9,5/10 m nên khoảng 500/528/556 ms (30/32/34 khung); slice-1a.ts:55–59, combat.ts:135–137. Ý đồ §8.2: A sẵn nòng, R lửa và khói tại nòng, T đạn rít, I blast khi tới; không chèn nổ mục tiêu vào file phát.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=400–800 ms, variants=4 theo src/view/sound-map.ts:13,48 (FIRES), src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/content/slice-1a.ts:25–30,41–59,148; src/sim/systems/combat.ts:76–86,135–137; src/sim/systems/rewards.ts:44–55; src/sim/systems/combat.ts:86,135; src/content/slice-1a.ts:55–59: nhịp pháo 2,6/2,4/2,2 s, đề xuất phần phát dưới 0,8 s.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/content/slice-1a.ts:25–30,41–59,148; src/sim/systems/combat.ts:76–86,135–137; src/sim/systems/rewards.ts:44–55; src/sim/systems/combat.ts:86,135; src/content/slice-1a.ts:55–59: nhịp pháo 2,6/2,4/2,2 s, đề xuất phần phát dưới 0,8 s.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/cannon-fire/`.

## `bolt-fire`

**Tên trong game:** Fort

Có điều kiện: Fort có mục tiêu; cả loạt thường và Power.

**Độ dài:** 180–350 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A large fortress crossbow releases its loaded latch, a crisp string crack and wooden frame recoil, a heavy bolt whistles outward, and a brief resonant timber tail settles. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: Fort dùng bolt (combat.ts:135; rewards.ts:51), 34 m/s, tầm 9 m: khoảng 265 ms, làm tròn lên 16 khung; slice-1a.ts:25–30. Ý đồ §8.2: A lên dây trong gõ, R chốt nỏ, T vệt trắng, I cắm dùng hit, F rung.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=180–350 ms, variants=4 theo src/view/sound-map.ts:13,48 (FIRES), src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/content/slice-1a.ts:25–30,41–59,148; src/sim/systems/combat.ts:76–86,135–137; src/sim/systems/rewards.ts:44–55; src/sim/systems/combat.ts:86,135; src/content/slice-1a.ts:25–30: nhịp Fort 1,2 s, nỏ có thân ngắn.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/content/slice-1a.ts:25–30,41–59,148; src/sim/systems/combat.ts:76–86,135–137; src/sim/systems/rewards.ts:44–55; src/sim/systems/combat.ts:86,135; src/content/slice-1a.ts:25–30: nhịp Fort 1,2 s, nỏ có thân ngắn.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/bolt-fire/`.

## `fireball-fire`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Draconis đứng đất, có mục tiêu trong tầm.

**Độ dài:** 600–900 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **2 lượt**, 6 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. The fire dragon gathers a quick throat breath and releases a pressurized fireball, a deep living rasp opens into a dense flame roar, the burning mass rushes away and a low valley echo rolls out. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: agents.ts:166 gọi fireAt; 20 m/s, tầm 9 m → khoảng 450 ms/27 khung, slice-1a.ts:148. Ý đồ §8.2: A hít rất gọn, R lửa từ miệng rồng, T cầu lửa rít, I blast, F than; R phải nghe ở nguồn trước I.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=600–900 ms, variants=4 theo src/view/sound-map.ts:13,48 (FIRES), src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/content/slice-1a.ts:25–30,41–59,148; src/sim/systems/combat.ts:76–86,135–137; src/sim/systems/rewards.ts:44–55; src/sim/systems/agents.ts:166–167; src/content/slice-1a.ts:148: nhịp 1,6 s; đề xuất 600–900 ms giữ thân lửa và đuôi theo Q6.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/content/slice-1a.ts:25–30,41–59,148; src/sim/systems/combat.ts:76–86,135–137; src/sim/systems/rewards.ts:44–55; src/sim/systems/agents.ts:166–167; src/content/slice-1a.ts:148: nhịp 1,6 s; đề xuất 600–900 ms giữ thân lửa và đuôi theo Q6.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/fireball-fire/`.

## `hit`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: đạn đơn chạm mục tiêu còn sống.

**Độ dài:** 100–250 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 6; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A fast small projectile bites into dense hide and timber, a sharp contact crack, a compact material vibration, a few loose fragments and a brief low outdoor reflection. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: FX.hit chỉ khi đạn đơn tới mục tiêu còn sống, cùng tick sát thương; FxPipe hit (src/view/fx-pipe.ts:46–48). Ý đồ §8.2: I theo vật liệu loài, F mảnh sau 2–3 khung; id hiện chung nên chưa có ngân hàng riêng từng loài.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=100–250 ms, variants=6 theo src/view/sound-map.ts:14,48 (RING), src/content/slice-1a.ts:25–45,87–99; src/sim/systems/projectile.ts:61–64; src/sim/systems/projectile.ts:61–64: mốc chạm đơn, đề xuất đầu và thân gọn vì có thể trúng dày.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:25–45,87–99; src/sim/systems/projectile.ts:61–64; src/sim/systems/projectile.ts:61–64: mốc chạm đơn, đề xuất đầu và thân gọn vì có thể trúng dày.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/hit/`.

## `blast`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: đạn có splash tới điểm đích; tối đa 2 mỗi frame âm.

**Độ dài:** 640–960 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **2 lượt**, 6 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A cannon-sized blast strikes limestone with a sharp pressure crack, a deep layered drum-like body, a turbulent dust rush and falling stone fragments, then a low rolling valley reflection. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: FX.burst khi tới đích, kể cả đích cũ; audio-min.ts:186–192 gom 2/frame. Ý đồ §8.2: I nổ ba lớp của Cannon Tower; F bụi, mảnh và dấu cháy, không phát nổ ở R. Cùng id còn dùng cho cầu lửa và lông lửa, chưa tách vật liệu.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/blast.yaml: duration.min_ms=640, max_ms=960, variants.target=3; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:55–59,148; src/sim/systems/projectile.ts:48–60. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/blast/`.

## `ink-puff`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: quái chết; chung mọi loài, tối đa 3/frame và 8/s.

**Độ dài:** 160–240 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 6; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A small ink-soaked paper body tears apart under tension, a sharp wet rip opens into a scattering ink spray, thin paper shreds flutter down and a brief airy stone-courtyard reflection fades. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · aftermath:** Mã: FX.death dùng chung, boss kết rút cũng có event; src/view/boss-2d.ts:109–125 đọc chết và trúng. Ý đồ §8.2: I/F riêng từng loài chưa có id, giữ hàng chung không giả vờ đã tách.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/ink-puff.yaml: duration.min_ms=160, max_ms=240, variants.target=6; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:87–129,187–192; src/sim/systems/deaths.ts:33; src/sim/systems/boss.ts:270. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/ink-puff/`.

## `block`

**Tên trong game:** Soldier

Có điều kiện: từ ngày 2, lính bắt được quái mặt đất.

**Độ dài:** 120–300 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A human-sized spear guard plants its wooden shaft and catches a charging creature, a firm shaft crack, braced leather strain and a short gritty foot scrape settling into the stone ground. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: FX.block tại lúc chặn (block.ts:79). Ý đồ §8.2: I cán giáo và chân bám, F giáp rung; tiếng hô người chưa có nguồn ghi nên không đưa vào prompt.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=120–300 ms, variants=4 theo src/view/sound-map.ts:14,48 (RING), src/content/slice-1a.ts:67–76,87–88,215; src/sim/systems/block.ts:79; src/sim/systems/block.ts:79; src/content/slice-1a.ts:69–73: chặn ban đầu, lính đánh nhịp 1,0/0,9 s.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:67–76,87–88,215; src/sim/systems/block.ts:79; src/sim/systems/block.ts:79; src/content/slice-1a.ts:69–73: chặn ban đầu, lính đánh nhịp 1,0/0,9 s.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/block/`.

## `soldier-down`

**Tên trong game:** Soldier

Có điều kiện: từ ngày 2, một Soldier hết máu.

**Độ dài:** 250–550 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **2 lượt**, 7 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A human-sized spear guard collapses, a wooden spear clatters down, leather folds with a heavy cloth scrape, loose paper fragments scatter and a low courtyard resonance fades. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · aftermath:** Mã: hurtSoldier phát FX.soldierDown khi chết (combat.ts:191). Ý đồ §8.2: I vũ khí chạm đất, F tan chữ bay lên; giữ nguồn vật liệu thay giọng hô người.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=250–550 ms, variants=4 theo src/view/sound-map.ts:14,48 (RING), src/content/slice-1a.ts:67–76,87–88,215; src/sim/systems/combat.ts:191; src/sim/systems/combat.ts:191: mốc chết một lính; đề xuất một lần vũ khí/áo rơi, không có file số đo.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:67–76,87–88,215; src/sim/systems/combat.ts:191; src/sim/systems/combat.ts:191: mốc chết một lính; đề xuất một lần vũ khí/áo rơi, không có file số đo.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/soldier-down/`.

## `fizzle`

**Tên trong game:** Word Shot

Có điều kiện: hoàn tất Power nhưng không còn mục tiêu.

**Độ dài:** 150–350 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. An arm-sized paper projectile loosens before launch, a brief taut bamboo release dissolves into fluttering paper, a light airy swirl and a short fading breath of open space. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · aftermath:** Mã: FX.fizzle trước launch khi found=0; không có R đạn thật hay I mục tiêu. Ý đồ: F chữ tản đi ở tháp, không thêm đạn hoặc đổi sát thương.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=150–350 ms, variants=3 theo src/view/sound-map.ts:14,48 (RING), src/content/slice-1a.ts:39–64; src/sim/systems/rewards.ts:44–47; src/sim/systems/rewards.ts:44–47: không có mục tiêu, đề xuất giấy tản ngắn ở nguồn.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:39–64; src/sim/systems/rewards.ts:44–47; src/sim/systems/rewards.ts:44–47: không có mục tiêu, đề xuất giấy tản ngắn ở nguồn.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/fizzle/`.

## `direct-break`

**Tên trong game:** Stop

Có điều kiện: Đêm 4, gõ thành công từ ngắt của Raccoon Dog.

**Độ dài:** 200–450 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A small hand drum rhythm is stopped by a decisive bamboo strike, a tight skin crack, a collapsing wooden rattle, scattered paper flecks and a short courtyard tail. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: direct.ok, verb=0; src/view/fx-pipe.ts:4–6 tả trống vỡ thành chữ. Ý đồ §8.2: I ngắt cơ chế ngay từ cuối, F chữ; A chính là lúc gõ.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=200–450 ms, variants=3 theo src/view/sound-map.ts:41, src/content/slice-1a.ts:116–119,190; src/view/words/cards.ts:29; src/sim/systems/direct.ts:55–87; src/view/audio-min.ts:207: trống hiện có, đề xuất kéo thân/đuôi gọn theo Q6; src/content/slice-1a.ts:118 cơ chế ngắt.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:116–119,190; src/view/words/cards.ts:29; src/sim/systems/direct.ts:55–87; src/view/audio-min.ts:207: trống hiện có, đề xuất kéo thân/đuôi gọn theo Q6; src/content/slice-1a.ts:118 cơ chế ngắt.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/direct-break/`.

## `ult-cast`

**Tên trong game:** Fire Feather Rain

Có điều kiện: từ Đêm 3, bấm Ultimate đủ năng lượng và đúng tầm.

**Độ dài:** 700–1200 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **2 lượt**, 5 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A dragon-sized wing sweep gathers a rising roll on a large Vietnamese barrel drum, a forceful accented release opens into rushing feathers and fire, then a broad low limestone-valley resonance fades. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: ult ngay castUlt thành công; chân dung và bóng lông đọc ở src/view/fx-pipe.ts:2–6,63–100. Ý đồ §8.2: A trống tăng theo Spell, R ở rồng, T lông ~0,8 s (ult.ts:20–23,107; rules.ts:94), I blast, F than. Hiện ult-cast chỉ một mốc; không trì hoãn sim.

**Chất liệu:** reworded — Chưa có thẻ riêng; diễn hành động theo quy mô cõi đá vôi huyền ảo của §2 và chất liệu §8.2, thay cách gõ ngắn chung của nền cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=700–1200 ms, variants=3 theo src/view/sound-map.ts:28 (ONE), src/content/slice-1a.ts:215; src/sim/systems/ult.ts:55–70; src/ui/hud.ts:33; src/sim/systems/ult.ts:66–70; src/content/rules.ts:94: minGapS=45, rơi 0,8 s, đề xuất âm phát 700–1200 ms độc lập nhịp rơi.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:215; src/sim/systems/ult.ts:55–70; src/ui/hud.ts:33; src/sim/systems/ult.ts:66–70; src/content/rules.ts:94: minGapS=45, rơi 0,8 s, đề xuất âm phát 700–1200 ms độc lập nhịp rơi.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/ult-cast/`.

# Buổi tạo: boss Mộc Tinh

## `boss-warn`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Ngày 5 bắt đầu cảnh báo boss.

**Độ dài:** 600–1000 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 6 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. Two measured blows resonate through the trunk of an ancient tree spirit, massive timber flexes with a deep woody groan, root fibers creak and a distant limestone-valley echo settles. Each effect is followed by one second of silence.
```

**Nhịp VFX · charge:** Mã: bossWarn ngày 5. Ý đồ §8.2: A gầm gỗ theo vết rễ cảnh báo, hai nhịp rõ; chưa phải I đòn. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=600–1000 ms, variants=1 theo src/view/sound-map.ts:27 (ONE), src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: bossWarn ngày 5. Ý đồ §8.2: A gầm gỗ theo vết rễ cảnh báo, hai nhịp rõ; chưa phải I đòn. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: bossWarn ngày 5. Ý đồ §8.2: A gầm gỗ theo vết rễ cảnh báo, hai nhịp rõ; chưa phải I đòn. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-warn/`.

## `boss-lull`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, vào khoảng lặng trước boss, 12 s.

**Độ dài:** 12000–12000 ms/cú; **lặp:** không; **dạng:** single; **biến thể:** 1; **2 lượt**, 1 cú/lượt dự kiến; **P1**, bus `world`.

```text
An ancient tree spirit stirs beneath a limestone valley, a deep growing earth rumble and massive root creaks build under large skin-drum strokes at 0, 3, 6, 9, 10.5, 11.2 and 11.7 seconds, resolving into a short low resonance inside twelve seconds.
```

**Nhịp VFX · charge:** Mã: bossLull có end, lullS=12 (slice-1a.ts:214), SYNTH audio-min.ts:220. Ý đồ: A vết nứt và nhịp đất; một đoạn diễn tiến single, không loop; không tự kéo thời gian chờ. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=12000–12000 ms, variants=1 theo src/view/sound-map.ts:27 (ONE), src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: bossLull có end, lullS=12 (slice-1a.ts:214), SYNTH audio-min.ts:220. Ý đồ: A vết nứt và nhịp đất; một đoạn diễn tiến single, không loop; không tự kéo thời gian chờ. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: bossLull có end, lullS=12 (slice-1a.ts:214), SYNTH audio-min.ts:220. Ý đồ: A vết nứt và nhịp đất; một đoạn diễn tiến single, không loop; không tự kéo thời gian chờ. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-lull/`.

## `boss-emerge`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, Mộc Tinh trồi lên.

**Độ dài:** 700–1500 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 4 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. An ancient tree spirit of towering trunk size heaves through limestone soil, an abrupt earth fracture releases a massive woody roar, thick roots wrench upward, stones tumble and a broad low valley echo follows. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: bossEmerge, boss-2d.ts:83–88 văng đá/rễ 1,2–1,3 s. Ý đồ: R tại thân trước I đá, F đất lắng; gầm là chất liệu gỗ, không thoại. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=700–1500 ms, variants=2 theo src/view/sound-map.ts:27 (ONE), src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: bossEmerge, boss-2d.ts:83–88 văng đá/rễ 1,2–1,3 s. Ý đồ: R tại thân trước I đá, F đất lắng; gầm là chất liệu gỗ, không thoại. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: bossEmerge, boss-2d.ts:83–88 văng đá/rễ 1,2–1,3 s. Ý đồ: R tại thân trước I đá, F đất lắng; gầm là chất liệu gỗ, không thoại. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-emerge/`.

## `boss-phase`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, máu tới mốc 70%, đổi pha và choáng.

**Độ dài:** 900–1800 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 4 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. The bark of an ancient tree spirit splits with a sharp timber crack, a huge hollow wooden groan blooms beneath a bright bronze hand-bell accent, bark fragments scatter and a low valley resonance recedes. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: stagger 70%, stunS=5; boss.ts:225–252, boss-2d.ts:97–99. Ý đồ: I vỏ nứt, F sao choáng, không thêm cồng thường vào nhịp đánh. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=900–1800 ms, variants=2 theo src/view/sound-map.ts:27 (ONE), src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: stagger 70%, stunS=5; boss.ts:225–252, boss-2d.ts:97–99. Ý đồ: I vỏ nứt, F sao choáng, không thêm cồng thường vào nhịp đánh. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: stagger 70%, stunS=5; boss.ts:225–252, boss-2d.ts:97–99. Ý đồ: I vỏ nứt, F sao choáng, không thêm cồng thường vào nhịp đánh. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-phase/`.

## `boss-roots`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, bắt đầu báo Rễ Trồi có nhà trong tầm.

**Độ dài:** 1200–2000 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 4 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. Massive roots of an ancient tree spirit tense beneath a limestone courtyard, dense fibers creak, stone grit scrapes upward and a growing low wooden strain resolves into a soft earth resonance. Each effect is followed by one second of silence.
```

**Nhịp VFX · charge:** Mã: roots hit=false, warnS=1,5 s (90 khung cơ sở); nhân warnK rồi làm tròn ticks (boss.ts:31,133–134). Ý đồ: A chạy theo vòng và vết rễ (boss-2d.ts:161–185), I tách ở boss-roots-hit, không nổ sớm. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=1200–2000 ms, variants=2 theo src/view/sound-map.ts:43, src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: roots hit=false, warnS=1,5 s (90 khung cơ sở); nhân warnK rồi làm tròn ticks (boss.ts:31,133–134). Ý đồ: A chạy theo vòng và vết rễ (boss-2d.ts:161–185), I tách ở boss-roots-hit, không nổ sớm. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: roots hit=false, warnS=1,5 s (90 khung cơ sở); nhân warnK rồi làm tròn ticks (boss.ts:31,133–134). Ý đồ: A chạy theo vòng và vết rễ (boss-2d.ts:161–185), I tách ở boss-roots-hit, không nổ sớm. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-roots/`.

## `boss-roots-hit`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, hết cảnh báo Rễ Trồi.

**Độ dài:** 300–650 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **1 lượt**, 7 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A thick root of an ancient tree spirit breaks through limestone soil and strikes a building foundation, a hard timber crack, crushing stone grit and a heavy wooden vibration, then falling chips and a low courtyard tail. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: roots hit=true khi hết warnS=1,5 s × warnK; I cùng stun nhà. Ý đồ: I rễ chạm, F mảnh gỗ; boss-2d.ts:74–80, fx-2d.ts:85–95 rễ mọc 120 ms rồi tan, không đợi rễ mọc xong mới phát I. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=300–650 ms, variants=3 theo src/view/sound-map.ts:43, src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: roots hit=true khi hết warnS=1,5 s × warnK; I cùng stun nhà. Ý đồ: I rễ chạm, F mảnh gỗ; boss-2d.ts:74–80, fx-2d.ts:85–95 rễ mọc 120 ms rồi tan, không đợi rễ mọc xong mới phát I. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: roots hit=true khi hết warnS=1,5 s × warnK; I cùng stun nhà. Ý đồ: I rễ chạm, F mảnh gỗ; boss-2d.ts:74–80, fx-2d.ts:85–95 rễ mọc 120 ms rồi tan, không đợi rễ mọc xong mới phát I. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-roots-hit/`.

## `boss-slam`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, Quật cành hoặc Quật Fort tới mốc chạm.

**Độ dài:** 400–800 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **1 lượt**, 6 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A great tree limb whips down with a dense woody rush, strikes stone with a forceful splitting crack, carries a broad timber resonance, then scatters bark and limestone chips into a low rolling echo. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: slam hit=true sau 1,2 s × warnK; keep hit=true cũng rơi vào boss-slam (sound-map.ts:44), sau 1,2 s × warnK; slice-1a.ts:205,208. Cả hai hit=false hiện im. Ý đồ: A cành/cung đỏ báo trước, I ngay tick kết, F gỗ đá; phần vung trong file chỉ sát đầu chạm, không dịch tick. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=400–800 ms, variants=3 theo src/view/sound-map.ts:44, src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: slam hit=true sau 1,2 s × warnK; keep hit=true cũng rơi vào boss-slam (sound-map.ts:44), sau 1,2 s × warnK; slice-1a.ts:205,208. Cả hai hit=false hiện im. Ý đồ: A cành/cung đỏ báo trước, I ngay tick kết, F gỗ đá; phần vung trong file chỉ sát đầu chạm, không dịch tick. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: slam hit=true sau 1,2 s × warnK; keep hit=true cũng rơi vào boss-slam (sound-map.ts:44), sau 1,2 s × warnK; slice-1a.ts:205,208. Cả hai hit=false hiện im. Ý đồ: A cành/cung đỏ báo trước, I ngay tick kết, F gỗ đá; phần vung trong file chỉ sát đầu chạm, không dịch tick. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-slam/`.

## `boss-drain`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, bắt đầu báo Rễ hút sinh khí.

**Độ dài:** 950–1600 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 4 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. An ancient tree spirit draws air through a root as thick as a trunk, a low intake gathers, fibers stretch with a rising wooden strain, fine leaves scrape inward and a hollow valley resonance gathers at the end. Each effect is followed by one second of silence.
```

**Nhịp VFX · charge:** Mã: drain hit=false, warnS=1,2 s × warnK. Ý đồ: A theo rễ bò từ boss tới Fort (boss-2d.ts:188–199), I tách boss-drain-hit; file cảnh báo cần cắt/chọn theo cửa sổ thực ở phiếu gắn. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=950–1600 ms, variants=2 theo src/view/sound-map.ts:43, src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: drain hit=false, warnS=1,2 s × warnK. Ý đồ: A theo rễ bò từ boss tới Fort (boss-2d.ts:188–199), I tách boss-drain-hit; file cảnh báo cần cắt/chọn theo cửa sổ thực ở phiếu gắn. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: drain hit=false, warnS=1,2 s × warnK. Ý đồ: A theo rễ bò từ boss tới Fort (boss-2d.ts:188–199), I tách boss-drain-hit; file cảnh báo cần cắt/chọn theo cửa sổ thực ở phiếu gắn. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-drain/`.

## `boss-drain-hit`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, Rễ hút sinh khí lấy mạng Fort.

**Độ dài:** 500–1000 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **1 lượt**, 6 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A massive root tightens against a stone fortress, a deep wooden crack releases a strong inward rush, a dark bronze hand-bell accent rings briefly, loose leaves spiral upward and a low hollow echo fades. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: drain hit=true sau 1,2 s × warnK; boss.ts:203–211 đồng thời FX.leak, nên leak có thể chồng cùng tick. Ý đồ: I lúc mất mạng, F xung sinh khí 0,7 s theo boss-2d.ts:188–200; chưa đổi bus/trần. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=500–1000 ms, variants=3 theo src/view/sound-map.ts:43, src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: drain hit=true sau 1,2 s × warnK; boss.ts:203–211 đồng thời FX.leak, nên leak có thể chồng cùng tick. Ý đồ: I lúc mất mạng, F xung sinh khí 0,7 s theo boss-2d.ts:188–200; chưa đổi bus/trần. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: drain hit=true sau 1,2 s × warnK; boss.ts:203–211 đồng thời FX.leak, nên leak có thể chồng cùng tick. Ý đồ: I lúc mất mạng, F xung sinh khí 0,7 s theo boss-2d.ts:188–200; chưa đổi bus/trần. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-drain-hit/`.

## `boss-summon`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5 pha 2, cả lúc báo và lúc Mầm Gỗ hiện.

**Độ dài:** 500–800 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **1 lượt**, 6 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. Four root-sized saplings push through dense soil, a gathering fibrous creak opens into clustered earth cracks, leafy shoots unfurl and loose grit settles with a short low valley reflection. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: sound-map.ts:44 trả cùng id cho summon hit=false và true; warnS=0,8 s cố định/48 khung (boss.ts:175–191), không nhân warnK. Ý đồ: A hạt/rễ, R mọc lúc hết báo; hiện cùng file phát hai lần, cần phiếu gắn tách A/R hoặc chọn phần, chưa có id mới. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=500–800 ms, variants=3 theo src/view/sound-map.ts:44, src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: sound-map.ts:44 trả cùng id cho summon hit=false và true; warnS=0,8 s cố định/48 khung (boss.ts:175–191), không nhân warnK. Ý đồ: A hạt/rễ, R mọc lúc hết báo; hiện cùng file phát hai lần, cần phiếu gắn tách A/R hoặc chọn phần, chưa có id mới. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: sound-map.ts:44 trả cùng id cho summon hit=false và true; warnS=0,8 s cố định/48 khung (boss.ts:175–191), không nhân warnK. Ý đồ: A hạt/rễ, R mọc lúc hết báo; hiện cùng file phát hai lần, cần phiếu gắn tách A/R hoặc chọn phần, chưa có id mới. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-summon/`.

## `boss-hit`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, đòn gây sát thương thực lên Mộc Tinh.

**Độ dài:** 180–400 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 6; **2 lượt**, 8 cú/lượt dự kiến; **P0**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A weapon strikes the dense bark of an ancient tree spirit, a sharp woody fracture opens into a deep trunk vibration, bark chips spin free and a short low valley echo settles. The brief bright onset settles within 100 milliseconds into a low body below one kilohertz or fine detail above four kilohertz. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: combat.ts:37 phát FX.bossHit khi dmg>0; boss-2d.ts:114–125 lóe và dăm gỗ, sát thương cháy cũng có event. Ý đồ: I vỏ gỗ đúng chất liệu, F mảnh; không thêm báo trước vào âm trúng. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=180–400 ms, variants=6 theo src/view/sound-map.ts:14,48 (RING), src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: combat.ts:37 phát FX.bossHit khi dmg>0; boss-2d.ts:114–125 lóe và dăm gỗ, sát thương cháy cũng có event. Ý đồ: I vỏ gỗ đúng chất liệu, F mảnh; không thêm báo trước vào âm trúng. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: combat.ts:37 phát FX.bossHit khi dmg>0; boss-2d.ts:114–125 lóe và dăm gỗ, sát thương cháy cũng có event. Ý đồ: I vỏ gỗ đúng chất liệu, F mảnh; không thêm báo trước vào âm trúng. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-hit/`.

## `boss-retreat`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Đêm 5, Mộc Tinh xuống 50% máu và rút.

**Độ dài:** 1600–2600 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 3 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. An ancient tree spirit folds its massive roots and sinks into limestone soil, a descending woody groan and leaf rush carry falling earth, a small bronze reward cascade glints at the end and a spacious low echo dissolves. Each effect is followed by one second of silence.
```

**Nhịp VFX · aftermath:** Mã: rút 2 s, Chest trả ngay bossRetreat (boss.ts:255–263; slice-1a.ts:203); boss-2d.ts:100–105 lá và giấy. Ý đồ: F lắng đất, chuỗi đồng thưởng nằm cuối; không dời mốc trả thưởng. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.

**Chất liệu:** reworded — Chưa có thẻ riêng; chọn gỗ cổ thụ, đá vôi và quy mô boss theo §2/§8.2, không chép chất liệu chuông/cồng của mã cũ.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=1600–2600 ms, variants=1 theo src/view/sound-map.ts:27 (ONE), src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: rút 2 s, Chest trả ngay bossRetreat (boss.ts:255–263; slice-1a.ts:203); boss-2d.ts:100–105 lá và giấy. Ý đồ: F lắng đất, chuỗi đồng thưởng nằm cuối; không dời mốc trả thưởng. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:199–215; src/sim/systems/boss.ts:31–34,125–217,225–277; src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95; Mã: rút 2 s, Chest trả ngay bossRetreat (boss.ts:255–263; slice-1a.ts:203); boss-2d.ts:100–105 lá và giấy. Ý đồ: F lắng đất, chuỗi đồng thưởng nằm cuối; không dời mốc trả thưởng. Căn cứ view: src/view/boss-2d.ts:69–125,161–200; src/view/fx-2d.ts:33–45,85–95.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/boss-retreat/`.

# Buổi tạo: ngày và đêm

## `night-fall`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Luôn phát khi chuyển phase sang night, trong năm đêm.

**Độ dài:** 2400–3600 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 2 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. Three broad festival-drum strokes, slow then closer together, announce night across a vast limestone valley, a solemn deep bronze gong answers, crickets stir and a low wind tail fades. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: phase được đọc ở audio-min.ts:114,168–184. Ý đồ §8.2: nhịp băng rôn/chuyển sáng hoặc kết trận cùng event, đuôi nằm sau; null vì đây là tín hiệu chu kỳ/UI, không phải pha đòn.

**Chất liệu:** reworded — gong: báo nguy trang nghiêm khi đêm xuống; giữ cồng theo thẻ nhưng chuyển quy mô sang thung lũng đá vôi §2; chủ dự án duyệt riêng.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/night-fall.yaml: duration.min_ms=2400, max_ms=3600, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/night-fall/`.

## `dawn`

**Tên trong game:** Dawn

Luôn phát khi chuyển phase sang dawn sau đêm còn sống.

**Độ dài:** 800–1200 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 5 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A distant rooster gives a natural crow across a towering limestone valley, clear animal breath and a resonant open call, with a fine morning wind and a short spacious fading tail. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: phase được đọc ở audio-min.ts:114,168–184. Ý đồ §8.2: nhịp băng rôn/chuyển sáng hoặc kết trận cùng event, đuôi nằm sau; null vì đây là tín hiệu chu kỳ/UI, không phải pha đòn.

**Chất liệu:** reworded — Thẻ cũ dùng sáo ba nốt; §8.2 đòi gà gáy xa và không khí bình minh nên chọn tiếng động vật thật, không giọng người.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/dawn.yaml: duration.min_ms=800, max_ms=1200, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/dawn/`.

## `day-countdown`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: mỗi giây trong 10 s cuối ngày, ba giây cuối cao hơn.

**Độ dài:** 30–80 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 8 cú/lượt dự kiến; **P2**, bus `ui`.

```text
An edited Foley sequence of isolated sound effects. A small lacquered wooden timing block receives a precise light strike, a crisp compact contact, a short hollow body and a fast natural decay. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: frame(day) được đọc ở audio-min.ts:114,168–184. Ý đồ §8.2: nhịp băng rôn/chuyển sáng hoặc kết trận cùng event, đuôi nằm sau; null vì đây là tín hiệu chu kỳ/UI, không phải pha đòn.

**Chất liệu:** reworded — Diễn chu kỳ trận trong không gian đá vôi hùng vĩ (§2/§8.2), giữ độ dài và biến thể của thẻ khi có.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=30–80 ms, variants=2 theo src/view/audio-min.ts:114, src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52; src/view/audio-min.ts:114,229: mỗi giây, gỗ hiện 0,04 s; đề xuất biên 30–80 ms, hai cao độ theo ba giây cuối.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52; src/view/audio-min.ts:114,229: mỗi giây, gỗ hiện 0,04 s; đề xuất biên 30–80 ms, hai cao độ theo ba giây cuối.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/day-countdown/`.

## `wave-start`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Luôn phát theo waveStart khi bắt đầu đợt quái của đêm.

**Độ dài:** 450–850 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 6 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A medium iron alarm plate is struck with a hard beater, a clear forward metallic attack, a firm resonant body and a short low valley echo. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: waveStart được đọc ở audio-min.ts:114,168–184. Ý đồ §8.2: nhịp băng rôn/chuyển sáng hoặc kết trận cùng event, đuôi nằm sau; null vì đây là tín hiệu chu kỳ/UI, không phải pha đòn.

**Chất liệu:** reworded — Diễn chu kỳ trận trong không gian đá vôi hùng vĩ (§2/§8.2), giữ độ dài và biến thể của thẻ khi có.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=450–850 ms, variants=1 theo src/view/sound-map.ts:28 (ONE), src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52; src/sim/systems/waves.ts:69–75: một tín hiệu đầu đợt, đề xuất kẻng dưới 850 ms.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52; src/sim/systems/waves.ts:69–75: một tín hiệu đầu đợt, đề xuất kẻng dưới 850 ms.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/wave-start/`.

## `night-called`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: người chơi gọi đêm sớm thành công.

**Độ dài:** 350–700 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 7 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A medium festival drum gives a deliberate double signal, tight skin attacks, an assertive wooden shell resonance and a short outdoor resolving tail. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: nightCalled được đọc ở audio-min.ts:114,168–184. Ý đồ §8.2: nhịp băng rôn/chuyển sáng hoặc kết trận cùng event, đuôi nằm sau; null vì đây là tín hiệu chu kỳ/UI, không phải pha đòn.

**Chất liệu:** reworded — Diễn chu kỳ trận trong không gian đá vôi hùng vĩ (§2/§8.2), giữ độ dài và biến thể của thẻ khi có.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=350–700 ms, variants=1 theo src/view/sound-map.ts:28 (ONE), src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52; src/sim/systems/waves.ts:86–92: tín hiệu gọi đêm thành công, đề xuất hai trống ngắn trước đuôi.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52; src/sim/systems/waves.ts:86–92: tín hiệu gọi đêm thành công, đề xuất hai trống ngắn trước đuôi.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/night-called/`.

## `leak`

**Tên trong game:** Fort

Có điều kiện: quái vào Fort hoặc boss lấy mạng; cách nhau trên 800 ms.

**Độ dài:** 960–1440 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 4 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A medium bronze warning gong is struck with a heavy padded beater, a clear low contact opens into a dark expanding metal body and a controlled valley echo signals danger. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: FX.leak tại mất mạng, audio-min.ts:186–195 cách >800 ms; boss keep/drain cũng phát FX.leak (boss.ts:210). Ý đồ §8.2: I Fort lóe đỏ đúng tick, F cảnh báo trầm, không chờ hết tiếng.

**Chất liệu:** reworded — gong: báo nguy Fort mất mạng, đúng §8.2; chủ dự án duyệt riêng.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/leak.yaml: duration.min_ms=960, max_ms=1440, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/leak/`.

## `defeat`

**Tên trong game:** Defeat

Có điều kiện: Fort hết mạng, trận thua.

**Độ dài:** 2400–3600 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 2 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A large low bronze gong marks the solemn loss of a fortress, a weighty padded strike blooms into a dark metallic body, a Vietnamese bamboo flute descends in three clear open-bore notes and the low resonance fades. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: defeat được đọc ở audio-min.ts:114,168–184. Ý đồ §8.2: nhịp băng rôn/chuyển sáng hoặc kết trận cùng event, đuôi nằm sau; null vì đây là tín hiệu chu kỳ/UI, không phải pha đòn.

**Chất liệu:** reworded — gong: khoảnh khắc trang trọng kết trận thất thủ; chủ dự án duyệt riêng.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/defeat.yaml: duration.min_ms=2400, max_ms=3600, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/defeat/`.

## `victory`

**Tên trong game:** Village saved

Có điều kiện: hoàn tất Đêm 5 và đoạn rút boss.

**Độ dài:** 1500–2500 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 3 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A broad festival drum resolves with two strong strokes, a small bronze hand bell answers with a bright rising pentatonic figure, the wooden shell rings warmly and a spacious limestone-valley tail fades. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: victory được đọc ở audio-min.ts:114,168–184. Ý đồ §8.2: nhịp băng rôn/chuyển sáng hoặc kết trận cùng event, đuôi nằm sau; null vì đây là tín hiệu chu kỳ/UI, không phải pha đòn.

**Chất liệu:** reworded — Diễn chu kỳ trận trong không gian đá vôi hùng vĩ (§2/§8.2), giữ độ dài và biến thể của thẻ khi có.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=1500–2500 ms, variants=1 theo src/view/sound-map.ts:28 (ONE), src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52; src/sim/systems/boss.ts:277; src/ui/hud.ts:52: kết trận, đề xuất stinger 1,5–2,5 s.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:187–215; src/sim/systems/waves.ts:91; src/ui/hud.ts:52; src/sim/systems/boss.ts:277; src/ui/hud.ts:52: kết trận, đề xuất stinger 1,5–2,5 s.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/victory/`.

# Buổi tạo: công trình và kinh tế

## `build-start`

**Tên trong game:** Build

Có điều kiện: bắt đầu xây hoặc nâng cấp hợp lệ.

**Độ dài:** 250–500 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **1 lượt**, 8 cú/lượt dự kiến; **P2**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A hand-sized builder hammer lifts and seats a heavy scaffold joint, a firm wooden contact, bamboo braces flex, a small grit scrape and a short stone-courtyard echo follows. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: built qua ONE/RING; audio-min.ts:168–195. Ý đồ §8.2: mốc hoàn tất/nhận tài nguyên hoặc hoảng cùng sự kiện; bụi, đồng/lúa/gỗ bay và phần đuôi theo sau, không sửa tiến độ việc.

**Chất liệu:** reworded — Giữ chức năng, chọn chất liệu hành động và sân đá vôi §2/§8.2; UI/kinh tế P2 để ưu tiên lực chiến đấu trước.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=250–500 ms, variants=3 theo src/view/sound-map.ts:28 (ONE), src/content/slice-1a.ts:21–83,171–180,215; src/sim/events.ts:36; src/view/sound-map.ts:28: bắt đầu việc, đề xuất một nhịp búa ngắn, không lấy 1,2 s mọc model làm độ dài âm.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:21–83,171–180,215; src/sim/events.ts:36; src/view/sound-map.ts:28: bắt đầu việc, đề xuất một nhịp búa ngắn, không lấy 1,2 s mọc model làm độ dài âm.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/build-start/`.

## `build-done`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: công trình hoặc nâng cấp hoàn tất.

**Độ dài:** 500–1000 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 6 cú/lượt dự kiến; **P2**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A substantial carved stone building settles onto its base, a final mallet contact, fitted timber and stone resonance, two bright bronze hand-bell notes and a short resolving courtyard tail. Each effect is followed by one second of silence.
```

**Nhịp VFX · aftermath:** Mã: finished qua ONE/RING; audio-min.ts:168–195. Ý đồ §8.2: mốc hoàn tất/nhận tài nguyên hoặc hoảng cùng sự kiện; bụi, đồng/lúa/gỗ bay và phần đuôi theo sau, không sửa tiến độ việc.

**Chất liệu:** reworded — Giữ chức năng, chọn chất liệu hành động và sân đá vôi §2/§8.2; UI/kinh tế P2 để ưu tiên lực chiến đấu trước.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=500–1000 ms, variants=2 theo src/view/sound-map.ts:28 (ONE), src/content/slice-1a.ts:21–83,171–180,215; src/sim/events.ts:37; src/view/sound-map.ts:28: hoàn tất việc, đề xuất stinger hai nốt §8.2.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:21–83,171–180,215; src/sim/events.ts:37; src/view/sound-map.ts:28: hoàn tất việc, đề xuất stinger hai nốt §8.2.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/build-done/`.

## `sell`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: bán hoặc hoàn tác công trình hợp lệ.

**Độ dài:** 300–650 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 2; **1 lượt**, 7 cú/lượt dự kiến; **P2**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A compact wooden scaffold is unlatched and folded, a crisp peg release, fitted boards slide and rattle, a few bronze coins settle into a tray and a short airy decay follows. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: sold qua ONE/RING; audio-min.ts:168–195. Ý đồ §8.2: mốc hoàn tất/nhận tài nguyên hoặc hoảng cùng sự kiện; bụi, đồng/lúa/gỗ bay và phần đuôi theo sau, không sửa tiến độ việc.

**Chất liệu:** reworded — Giữ chức năng, chọn chất liệu hành động và sân đá vôi §2/§8.2; UI/kinh tế P2 để ưu tiên lực chiến đấu trước.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=300–650 ms, variants=2 theo src/view/sound-map.ts:28 (ONE), src/content/slice-1a.ts:21–83,171–180,215; src/sim/events.ts:38; src/view/sound-map.ts:28: bán/undo, đề xuất tháo vật liệu và tiền gọn.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:21–83,171–180,215; src/sim/events.ts:38; src/view/sound-map.ts:28: bán/undo, đề xuất tháo vật liệu và tiền gọn.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/sell/`.

## `house-stun`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: nhà bị rễ boss làm choáng ở Đêm 5.

**Độ dài:** 200–500 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A thick root clamps a stone building footing, a sharp timber crack, strained beams and gritty limestone scrape vibrate together, then loose chips settle into a short low echo. Each effect is followed by one second of silence.
```

**Nhịp VFX · impact:** Mã: stun cùng rễ chạm; boss-2d.ts:74–80 rung nhà 150 ms và rễ/bụi. Ý đồ §8.2: I lóe nhà, F mảnh; boss-roots-hit có thể cùng tick, phiếu gắn cần nghe chồng.

**Chất liệu:** reworded — Giữ chức năng, chọn chất liệu hành động và sân đá vôi §2/§8.2; UI/kinh tế P2 để ưu tiên lực chiến đấu trước.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=200–500 ms, variants=3 theo src/view/sound-map.ts:28 (ONE), src/content/slice-1a.ts:21–83,171–180,215; src/view/boss-2d.ts:74–80: rung 150 ms, dăm gỗ 420 ms, bụi 500 ms; đề xuất âm 200–500 ms.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:21–83,171–180,215; src/view/boss-2d.ts:74–80: rung 150 ms, dăm gỗ 420 ms, bụi 500 ms; đề xuất âm 200–500 ms.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/house-stun/`.

## `harvest-done`

**Tên trong game:** Rice Field

Có điều kiện: gặt xong một ô lúa chín.

**Độ dài:** 300–650 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **1 lượt**, 7 cú/lượt dự kiến; **P2**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A hand-sized sickle finishes a sheaf of rice, a clean stalk cut opens into a full dry grain rustle, the bundle sweeps toward a basket and a short soft outdoor tail fades. Each effect is followed by one second of silence.
```

**Nhịp VFX · aftermath:** Mã: harvested qua ONE/RING; audio-min.ts:168–195. Ý đồ §8.2: mốc hoàn tất/nhận tài nguyên hoặc hoảng cùng sự kiện; bụi, đồng/lúa/gỗ bay và phần đuôi theo sau, không sửa tiến độ việc.

**Chất liệu:** reworded — Giữ chức năng, chọn chất liệu hành động và sân đá vôi §2/§8.2; UI/kinh tế P2 để ưu tiên lực chiến đấu trước.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=300–650 ms, variants=3 theo src/view/sound-map.ts:29 (ONE), src/content/slice-1a.ts:21–83,171–180,215; src/sim/systems/economy.ts:131: một ô thu hoạch hoàn tất, đề xuất sột bó lúa 300–650 ms.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:21–83,171–180,215; src/sim/systems/economy.ts:131: một ô thu hoạch hoàn tất, đề xuất sột bó lúa 300–650 ms.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/harvest-done/`.

## `tree-fall`

**Tên trong game:** Chop

Có điều kiện: chặt xong cây trên bản đồ.

**Độ dài:** 700–1400 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **2 lượt**, 5 cú/lượt dự kiến; **P2**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A mature mountain tree yields to the final axe stroke, a strong trunk crack, long splitting fibers and a rushing canopy fall, branches scrape the earth and a low valley echo recedes. Each effect is followed by one second of silence.
```

**Nhịp VFX · aftermath:** Mã: felled qua ONE/RING; audio-min.ts:168–195. Ý đồ §8.2: mốc hoàn tất/nhận tài nguyên hoặc hoảng cùng sự kiện; bụi, đồng/lúa/gỗ bay và phần đuôi theo sau, không sửa tiến độ việc.

**Chất liệu:** reworded — Giữ chức năng, chọn chất liệu hành động và sân đá vôi §2/§8.2; UI/kinh tế P2 để ưu tiên lực chiến đấu trước.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=700–1400 ms, variants=4 theo src/view/sound-map.ts:29 (ONE), src/content/slice-1a.ts:21–83,171–180,215; src/sim/systems/economy.ts:198: cây đổ hoàn tất, đề xuất nứt/thân/lá/đuôi 700–1400 ms.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:21–83,171–180,215; src/sim/systems/economy.ts:198: cây đổ hoàn tất, đề xuất nứt/thân/lá/đuôi 700–1400 ms.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/tree-fall/`.

## `coin`

**Tên trong game:** Gold

Có điều kiện: quái chết rơi Gold, trần 3/s.

**Độ dài:** 240–360 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 4; **1 lượt**, 8 cú/lượt dự kiến; **P2**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. A small bronze coin lands on a lacquered wooden tray, a crisp bright metal contact, a tiny pitched ring and a short warm wooden decay. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: FX.coin qua ONE/RING; audio-min.ts:168–195. Ý đồ §8.2: mốc hoàn tất/nhận tài nguyên hoặc hoảng cùng sự kiện; bụi, đồng/lúa/gỗ bay và phần đuôi theo sau, không sửa tiến độ việc.

**Chất liệu:** reworded — Giữ chức năng, chọn chất liệu hành động và sân đá vôi §2/§8.2; UI/kinh tế P2 để ưu tiên lực chiến đấu trước.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/coin.yaml: duration.min_ms=240, max_ms=360, variants.target=4; playback.mode=one-shot, channels=mono, bus thẻ=world; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:21–83,171–180,215. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/coin/`.

## `helper-panic`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: Chấm, Phẩy hoặc Gạch bị quái áp sát và hoảng.

**Độ dài:** 100–250 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 3; **1 lượt**, 8 cú/lượt dự kiến; **P1**, bus `world`.

```text
An edited Foley sequence of isolated sound effects. The small scholar helpers scramble with quick tiny claw steps, two close high wooden taps, hurried feather rustle and a light airy settling tail. Each effect is followed by one second of silence.
```

**Nhịp VFX · release:** Mã: panic qua ONE/RING; audio-min.ts:168–195. Ý đồ §8.2: mốc hoàn tất/nhận tài nguyên hoặc hoảng cùng sự kiện; bụi, đồng/lúa/gỗ bay và phần đuôi theo sau, không sửa tiến độ việc.

**Chất liệu:** reworded — Âm hiện tại chỉ hai gõ cao; thêm chân và lông cho Helper theo §8.2. Không xin lời người hay giọng nhân vật.

**Nguồn độ dài và biến thể:** Không có thẻ. Đề xuất biên tập targetMs=100–250 ms, variants=3 theo src/view/sound-map.ts:27 (ONE), src/content/slice-1a.ts:21–83,171–180,215; src/sim/systems/agents.ts:121; src/view/audio-min.ts:210: hai gõ cách 100 ms, mỗi gõ 50 ms; đề xuất 100–250 ms gồm lông.; nhịp SYNTH/CAPS src/view/audio-min.ts:198–239 khi có âm cũ; docs/audio/THEME_SOUND_LIST.md:11–18,20–57 chỉ định chất liệu và mono cho tiếng ngắn, không cấp số cho id mới. Các số đề xuất không phải hằng số âm trong mã.

**Căn cứ map 1:** src/content/slice-1a.ts:21–83,171–180,215; src/sim/systems/agents.ts:121; src/view/audio-min.ts:210: hai gõ cách 100 ms, mỗi gõ 50 ms; đề xuất 100–250 ms gồm lông.. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/helper-panic/`.

# Buổi tạo: UI và nền

## `ui-move`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: đổi mục menu hoặc bảng tạm dừng.

**Độ dài:** 32–48 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 8 cú/lượt dự kiến; **P2**, bus `ui`.

```text
An edited Foley sequence of isolated sound effects. A tiny lacquered wooden slider touches its stop, a delicate crisp contact, a compact wooden body and an immediate natural decay. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: ui(sound) gọi ngay ui- + sound (audio-min.ts:127–129). Ý đồ §8.2: chạm gỗ sơn mài, đồng nhỏ, giấy cùng mốc focus/chọn/đèn; null vì không phải đòn.

**Chất liệu:** reworded — Đổi tre làng trong thẻ UI sang gỗ sơn mài theo giao diện đá vôi/ngọc của §2 và tiếng UI §8.2; giữ giấy đèn và đồng nhỏ.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/ui-move.yaml: duration.min_ms=32, max_ms=48, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=ui; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/audio-min.ts:127–129; docs/audio/THEME_SOUND_LIST.md:50–57. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/ui-move/`.

## `ui-pick`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: chọn một mục khả dụng.

**Độ dài:** 480–720 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 6 cú/lượt dự kiến; **P2**, bus `ui`.

```text
An edited Foley sequence of isolated sound effects. A small lacquered wooden control clicks into place, a firm clean contact followed by a tiny bronze hand-bell accent, a warm pitched body and a graceful short decay. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: ui(sound) gọi ngay ui- + sound (audio-min.ts:127–129). Ý đồ §8.2: chạm gỗ sơn mài, đồng nhỏ, giấy cùng mốc focus/chọn/đèn; null vì không phải đòn.

**Chất liệu:** reworded — Đổi tre làng trong thẻ UI sang gỗ sơn mài theo giao diện đá vôi/ngọc của §2 và tiếng UI §8.2; giữ giấy đèn và đồng nhỏ.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/ui-pick.yaml: duration.min_ms=480, max_ms=720, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=ui; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/audio-min.ts:127–129; docs/audio/THEME_SOUND_LIST.md:50–57. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/ui-pick/`.

## `ui-off`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: chọn mục đang khóa.

**Độ dài:** 48–72 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 8 cú/lượt dự kiến; **P2**, bus `ui`.

```text
An edited Foley sequence of isolated sound effects. A small lacquered wooden control meets a padded stop, a gentle dull contact, a compact woody vibration and a quick natural decay. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: ui(sound) gọi ngay ui- + sound (audio-min.ts:127–129). Ý đồ §8.2: chạm gỗ sơn mài, đồng nhỏ, giấy cùng mốc focus/chọn/đèn; null vì không phải đòn.

**Chất liệu:** reworded — Đổi tre làng trong thẻ UI sang gỗ sơn mài theo giao diện đá vôi/ngọc của §2 và tiếng UI §8.2; giữ giấy đèn và đồng nhỏ.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/ui-off.yaml: duration.min_ms=48, max_ms=72, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=ui; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/audio-min.ts:127–129; docs/audio/THEME_SOUND_LIST.md:50–57. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/ui-off/`.

## `ui-lamp`

**Tên trong game:** — (sự kiện không có nhãn riêng phù hợp)

Có điều kiện: đèn lồng ở màn tựa sáng.

**Độ dài:** 400–600 ms/cú; **lặp:** không; **dạng:** hits; **biến thể:** 1; **1 lượt**, 7 cú/lượt dự kiến; **P2**, bus `ui`.

```text
An edited Foley sequence of isolated sound effects. A small paper lantern opens and catches a flame, a delicate paper rustle and fine flame hiss, a faint high bronze shimmer and a soft airy settling tail. Each effect is followed by one second of silence.
```

**Nhịp VFX · không gán pha đòn:** Mã: ui(sound) gọi ngay ui- + sound (audio-min.ts:127–129). Ý đồ §8.2: chạm gỗ sơn mài, đồng nhỏ, giấy cùng mốc focus/chọn/đèn; null vì không phải đòn.

**Chất liệu:** reworded — Đổi tre làng trong thẻ UI sang gỗ sơn mài theo giao diện đá vôi/ngọc của §2 và tiếng UI §8.2; giữ giấy đèn và đồng nhỏ.

**Nguồn độ dài và biến thể:** tools/audio-lab/specs/typing-defense/ui-lamp.yaml: duration.min_ms=400, max_ms=600, variants.target=1; playback.mode=one-shot, channels=mono, bus thẻ=ui; bus hàng theo mã.

**Căn cứ map 1:** src/content/slice-1a.ts:20–83,212–215; src/ui/tips.ts:16–25; src/view/audio-min.ts:127–129; docs/audio/THEME_SOUND_LIST.md:50–57. Tên: src/view/words/cards.ts:29; `view.name` ở slice-1a.ts:36,50,64,76,81,83; ui/hud.ts:33,52,57 và ui/sheets.ts:42.

**Clip:** docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven. **Thư mục nhận:** `~/AudioLab/inbox/firefly/typing-defense/ui-lamp/`.

# Bị loại

- **`key-right`** — Phím đúng phát ở map 1 nhưng loại khỏi Firefly theo mục 6: thuộc các bộ tiếng phím 189–193; §8.2 giữ synth. Ải đầu: w1-silverfall. Căn cứ: src/view/sound-map.ts:37; docs/games/ART_DIRECTION_2026-10-28.md:517; Phiếu 221 mục 6; docs/audio/THEME_SOUND_LIST.md:16,30
- **`direct-pin`** — Zombie Leader chỉ có trong hộp cát, không nằm trong năm đêm của map 1; chưa có ải truyện mở. Ải đầu: chưa có. Căn cứ: src/content/slice-1a.ts:131–137,186–193; src/view/sound-map.ts:41
- **`direct-shield`** — Troll chỉ có trong hộp cát, không nằm trong năm đêm của map 1; chưa có ải truyện mở. Ải đầu: chưa có. Căn cứ: src/content/slice-1a.ts:131–143,186–193; src/view/sound-map.ts:41
- **`feather-fall`** — Có khóa FIRES nhưng chưa có đường phát: ult.drop thêm PROJECTILE.feather bằng P.add trực tiếp, không đẩy FX.fire. Chưa ải nào phát id; không đồng nghĩa không có lông lửa. Ải đầu: chưa có. Căn cứ: src/view/sound-map.ts:13,48; src/sim/systems/ult.ts:102–110; src/sim/stores/projectiles.ts:33–46; git grep FX.fire td-1c -- src: chỉ combat.ts:86 đẩy event. Nhịp T để phiếu gắn: ult.ts:20–23 SPEED=12/60 m/tick, FROM dài 9,6 m; rules.ts:94 fallS=0,8 → 48 khung cho đích đứng yên. I vẫn có blast (projectile.ts:60). Ý đồ §8.2: A/R ở rồng, T lông, I nổ, F than; không sửa sim ở phiếu này.
- **`amb-villager-call`** — Giọng người, chủ dự án ghi âm cùng người nhà và giấy đồng ý; không thành hàng Firefly SFX. Ải đầu: chưa có. Căn cứ: docs/games/AUDIO_PIPELINE.md:129 (§3.2): ghi 4 biến thể, Không dùng AI. tools/audio-lab/specs/typing-defense/amb-villager-call.yaml:13,96,102,170: source_class voice; now owner-recording; blocked_by chu-du-an-ghi-am, giay-dong-y. src/view/audio-min.ts:119–124 gọi thẳng goi mỗi 3–7 s ở màn tựa; src/view/folk.ts:135: tiếng tổng hợp không qua id. Phiếu gắn phải đưa nó qua amb-villager-call; không thêm vào fired-ids.
- **`amb-dusk`** — Chỉ có thẻ Màn đầu (chưa có); không có mã phát âm nền này. Ải đầu: chưa có. Căn cứ: tools/audio-lab/specs/typing-defense/amb-dusk.yaml:when; docs/audio/THEME_SOUND_LIST.md:64. git grep amb- td-1c -- src: 0 dòng; git grep dusk chỉ màu theme.css:23, title.css:6,14,31 và ảnh title.ts:2,17, không có âm.
- **`music-boss`** — Nhạc có đường riêng, ngoài danh sách Firefly SFX. Ải đầu: chưa có. Căn cứ: docs/games/AUDIO_PIPELINE.md §8.2; src/view/music.ts; docs/audio/THEME_SOUND_LIST.md:66–75; tools/audio-lab/specs/typing-defense/music-boss.yaml
- **`music-calm`** — Nhạc có đường riêng, ngoài danh sách Firefly SFX. Ải đầu: chưa có. Căn cứ: docs/games/AUDIO_PIPELINE.md §8.2; src/view/music.ts; docs/audio/THEME_SOUND_LIST.md:66–75; tools/audio-lab/specs/typing-defense/music-calm.yaml
- **`music-stingers`** — Nhạc có đường riêng, ngoài danh sách Firefly SFX. Ải đầu: chưa có. Căn cứ: docs/games/AUDIO_PIPELINE.md §8.2; src/view/music.ts; docs/audio/THEME_SOUND_LIST.md:66–75; tools/audio-lab/specs/typing-defense/music-stingers.yaml
- **`music-tension`** — Nhạc có đường riêng, ngoài danh sách Firefly SFX. Ải đầu: chưa có. Căn cứ: docs/games/AUDIO_PIPELINE.md §8.2; src/view/music.ts; docs/audio/THEME_SOUND_LIST.md:66–75; tools/audio-lab/specs/typing-defense/music-tension.yaml

`key-right` vẫn có `map1: true` trong fired-ids vì thực sự được gọi. Quy tắc phủ “map1=true phải là hàng” có ngoại lệ duy nhất do chính mục 6 yêu cầu: tiếng phím đúng ở excluded, thuộc bộ khác. Script công khai ngoại lệ, không đổi map1 thành false. `feather-fall` ngược lại chưa có emitter; nhịp 0,8 s vẫn được lưu trong căn cứ loại để phiếu gắn sửa sau.

# Bible đòi nhưng mã chưa có id

- Tiếng riêng mỗi loài khi ra, đi (vòng), đánh, trúng, chết: Hopping Zombie, Ghost Flame, River Serpent, Sapling, Raccoon Dog, Split Blob, Little Blob. Các id hit/ink-puff còn chung.
- A/R/I/F tách rõ ở Fort, Archer Tower, Cannon Tower; nổ ba lớp đúng Cannon Tower, hai lớp lửa của Draconis hiện dùng chung blast. Không tự thêm id.
- Nón lửa, gầm riêng và hành động tại miệng Draconis; trống tăng theo tiến độ Spell, tiếng từng lông chưa có FX.fire dù registry có feather-fall.
- Boss: báo trước slam/keep hiện không có id trả về; summon dùng cùng id cả đầu báo và lúc chạm. Cần phiếu gắn phân pha, không sửa tick trong danh sách.
- Xây/nâng/bán có id chung, chưa có âm đổ nát/sửa riêng; lính chưa có từng nhịp giáo hay hô ghi thật; Helper chưa có từng nhịp chân/giọng ghi riêng.
- Thác, gió, chim và nền cõi đá vôi chưa có id phát; amb-dusk chỉ là thẻ cũ. Seal Dais, Herb House, Lumber Camp ngoài sáu nhà map 1, không mở hàng.
- Giọng dân amb-villager-call: chủ dự án/người nhà ghi 4 biến thể kèm đồng ý (AUDIO_PIPELINE §3.2:129); phiếu gắn đưa goi trực tiếp qua id này. Hoàn toàn ngoài lô tạo Firefly SFX.

# Chủ dự án cần xem

Duyệt riêng các âm có cồng: **night-fall, leak, defeat**; lý do gong: nằm trong từng hàng. Quy mô mới là cõi đá vôi hùng vĩ (§2); các thẻ cũ “làng tre” không quyết định thang âm. word-hit chuyển đàn tranh → chuông; Reap chuyển chuông → liềm; Quiz chuyển sáo → chuông; Dawn chuyển sáo → gà gáy theo §8.2. Chuông nhỏ là nhạc cụ cầm tay; báo động dùng kẻng sắt/trống hội. Sáo có âm ống mở sạch.

**Chưa biết về Firefly:** giới hạn ký tự prompt; có chọn độ dài file được không và phạm vi nào; số kết quả mỗi thao tác/credit; giới hạn tốc độ; hiệu quả gợi ý giọng; khả năng cắt vòng liền; tỷ lệ cú dùng được và chất lượng lặp dày. Lô 189 từng có WAV 48 kHz stereo 16-bit khoảng 12 s chỉ là quan sát trong README, không phải giới hạn sản phẩm. Danh sách chưa qua nghe duyệt.
