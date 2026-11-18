# Last Line · First Shift (`c1-s1`) · danh sách âm Firefly hướng B

**37 hàng · 66 lượt dự kiến** (P0 50, P1 11, P2 5). Công thức và giả định ở [README](README.md).

150 s; không hiểm họa; Scout từ 12 s; Brute từ 80 s; hai đợt dồn gốc 50/115 s; chọn 2 trong 5 súng nên cả 5 được tính. Đây là danh sách sản xuất, chưa tạo hay nghe âm. `hit.sub`, `hit.tail`, `kill.chime` là lớp dành cho bước gắn sau; `hit.tail` chưa có tình huống T4 trong ải này.

| Id | Tên trong game | Ưu tiên | Lượt |
|---|---|---|---|
| `word.load` | — | P0 | 2 |
| `word.perfect` | — | P0 | 2 |
| `word.full` | — | P0 | 2 |
| `streak.up` | — | P0 | 2 |
| `gun.xung` | Pulse Gun | P0 | 2 |
| `gun.xung.tail` | Pulse Gun | P0 | 2 |
| `gun.tia.start` | Heat Beam | P0 | 2 |
| `gun.tia.loop` | Heat Beam | P0 | 3 |
| `gun.tia.end` | Heat Beam | P0 | 2 |
| `gun.tia.pulse` | Heat Beam | P0 | 2 |
| `gun.tan.fire` | Scatter Gun | P0 | 2 |
| `gun.ray.armed` | Rail Gun | P0 | 3 |
| `gun.ray.charge` | Rail Gun | P0 | 2 |
| `gun.ray.fire` | Rail Gun | P0 | 2 |
| `gun.phao.launch` | Star Mortar | P0 | 2 |
| `gun.phao.burst` | Star Mortar | P0 | 2 |
| `hit.t1` | — | P0 | 2 |
| `hit.t2` | — | P0 | 2 |
| `hit.armour` | Armor | P0 | 2 |
| `hit.sub` | — | P0 | 2 |
| `hit.tail` | — | P0 | 2 |
| `kill.swarm` | Swarm | P0 | 2 |
| `kill.elite` | Scout | P0 | 2 |
| `kill.chime` | — | P0 | 2 |
| `foe.shot` | Scout | P1 | 1 |
| `foe.shot.down` | Scout | P1 | 1 |
| `hurt.hull` | Armor | P1 | 1 |
| `hurt.breach` | Armor | P1 | 1 |
| `hurt.drain` | Armor | P1 | 1 |
| `alarm.surge` | — | P1 | 2 |
| `end.win` | — | P1 | 2 |
| `end.lose` | — | P1 | 2 |
| `support.repair` | Armor | P2 | 1 |
| `star.get` | — | P2 | 1 |
| `ui.move` | — | P2 | 1 |
| `ui.select` | — | P2 | 1 |
| `ui.back` | — | P2 | 1 |

## `word.load`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Gõ xong từ và nạp được vào súng.
- Pha: release; khớp VFX: Vòng ký hiệu đóng quanh súng canh, lóe nạp ngay EV.word.
- Độ dài phần cắt: 200–300 ms; dạng `hits`; 3 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/word.load/`
- Gợi ý diễn bằng giọng: Lướt lên rồi khóa chắc, ngân thấp.
- Thời kỳ: `reworded`. Băng đạn đóng đổi thành vòng ký hiệu khóa quanh súng canh.

```text
An edited sequence of isolated a luminous glyph ring closing around a floating sentinel gun, a quick energy rise, a crisp loading lock and a compact resolving chord, a short bright attack, then a low ringing body below one kilohertz, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/word.load.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/typing-feel.ts:140–146; games/typing-survival/src/audio/theme-audio.ts:234–238 Gõ trong bất kỳ bến súng nào; content/chapter-1.ts:39–53

## `word.perfect`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Từ đạt điều kiện perfect và nạp được.
- Pha: release; khớp VFX: Vòng vàng trắng khép, áo choàng lóe ở EV.word.
- Độ dài phần cắt: 360–540 ms; dạng `hits`; 2 biến thể; 7 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/word.perfect/`
- Gợi ý diễn bằng giọng: Khóa chắc rồi ngân sáng cao, gọn.
- Thời kỳ: `reworded`. Nạp băng kèm điện đổi thành vòng ký hiệu vàng trắng khóa và chuông cao, cùng điều kiện perfect.

```text
An edited sequence of isolated a perfected energy loading gesture, a swift charge rise and a crystalline locking strike, a short bright attack, then a low ringing body below one kilohertz and a delicate bell shimmer above four kilohertz, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/word.perfect.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/typing-feel.ts:140–146; games/typing-survival/src/audio/theme-audio.ts:234–238 Gõ trong bất kỳ bến súng nào; content/chapter-1.ts:39–53

## `word.full`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Gõ xong từ khi bến súng đã đầy.
- Pha: release; khớp VFX: Viền bến sáng đều tại EV.word, không thêm đạn.
- Độ dài phần cắt: 100–100 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/word.full/`
- Gợi ý diễn bằng giọng: Chạm nhẹ rồi hạ giọng ngay.
- Thời kỳ: `reworded`. Chốt băng đạn hụt đổi thành phản hồi vòng năng lượng đã đầy; vẫn không nhận thêm đạn.

```text
An edited sequence of isolated a full energy chamber acknowledging a completed glyph ring, a brief bright glass contact followed by a compact low resonant answer below one kilohertz, restrained and dry, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Thẻ trống hoặc chưa có: lấy mốc tác giả từ THEME_SOUND_LIST.md và hàm phát; không phải số đo Firefly. THEME_SOUND_LIST.md:48,57 và type-audio.ts:72–77: 100 ms; biến thể mặc định 1 theo THEME_SOUND_LIST §2, không thuộc nhóm cần 4–6. games/typing-survival/src/view/typing-feel.ts:140–146; games/typing-survival/src/audio/type-audio.ts:72–77 Từ vẫn hoàn tất khi bến đã đầy: view/typing-feel.ts:140–146; content/chapter-1.ts:39–53

## `streak.up`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Chuỗi sạch đạt 3, 6, 10, 20 từ.
- Pha: null (ngoài đòn); khớp VFX: Số chuỗi nảy và ánh kính mũ tăng ở bậc mới.
- Độ dài phần cắt: 260–260 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/streak.up/`
- Gợi ý diễn bằng giọng: Hai nốt liền, nốt sau cao hơn.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
An edited sequence of isolated two delicate crystalline reward strikes sixty milliseconds apart, A5 then E6, each with a brief bright attack and a fine shimmer above four kilohertz, compact and restrained, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Thẻ trống hoặc chưa có: lấy mốc tác giả từ THEME_SOUND_LIST.md và hàm phát; không phải số đo Firefly. THEME_SOUND_LIST.md:49,58 và type-audio.ts:81–86: cú thứ hai ở 60 ms, ngân 200 ms, tổng 260 ms; biến thể mặc định 1 theo THEME_SOUND_LIST §2. games/typing-survival/src/view/typing-feel.ts:160–162; games/typing-survival/src/audio/type-audio.ts:81–86 Gõ trong bất kỳ bến súng nào; content/chapter-1.ts:39–53

## `gun.xung`

- Tên: Pulse Gun; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Mỗi viên Pulse Gun rời nòng.
- Pha: release; khớp VFX: Sao đầu nòng và viên lam xuất hiện cùng EV.shot.
- Độ dài phần cắt: 96–380 ms; dạng `hits`; 6 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.xung/`
- Gợi ý diễn bằng giọng: Căng rất ngắn, bật giòn, thân nặng.
- Thời kỳ: `reworded`. Súng cơ khí thời tàu đổi thành Pulse Gun canh bay: đầu tinh thể, thân plasma, vẫn phát mỗi viên.

```text
An edited sequence of isolated energy cannon shots from a floating sentinel gun, each with a brief loading catch, a bright crystalline crack, a dense plasma punch with weight, a short glassy shimmer settling into a low distant rumble, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.xung.yaml (duration.min_ms/max_ms, variants.target). Thẻ còn ghi phát nửa số viên; mã shots.ts:178 và THEME_SOUND_LIST §4 đã phát mỗi viên. Giữ duration thẻ theo phiếu, ingest phải nghe thử lặp 10–11 viên/s. games/typing-survival/src/view/shots.ts:178; games/typing-survival/src/audio/theme-audio.ts:248–250 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.xung.tail`

- Tên: Pulse Gun; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Đầu loạt, mỗi 0,5 s còn bắn và 150 ms sau viên cuối.
- Pha: aftermath; khớp VFX: Vệt sao chổi tàn, âm vang nối loạt; theo bộ hẹn hiện tại.
- Độ dài phần cắt: 400–700 ms; dạng `hits`; 1 biến thể; 7 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.xung.tail/`
- Gợi ý diễn bằng giọng: Rền thấp tan xa, vào mềm.
- Thời kỳ: `reworded`. Vang hành lang thép đổi thành dư âm plasma trên đường đắp thép than chì và đá cổ, giữ lịch gọi đuôi.

```text
An edited sequence of isolated diffuse low reports of plasma cannon fire rolling across a vast graphite steel and ancient stone causeway, a gentle onset, a broad dark resonant body below nine hundred hertz and a soft distant decay, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.xung.tail.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/shots.ts:181,431; games/typing-survival/src/audio/theme-audio.ts:254–256 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.tia.start`

- Tên: Heat Beam; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Heat Beam bắt đầu cháy.
- Pha: release; khớp VFX: Lóe mồi ở nòng tại EV.beamStart.
- Độ dài phần cắt: 480–720 ms; dạng `hits`; 1 biến thể; 6 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.tia.start/`
- Gợi ý diễn bằng giọng: Vo ngắn lên, xé điện rồi ù.
- Thời kỳ: `reworded`. Máy phát công nghiệp bật đổi thành súng canh gom năng lượng rồi mồi plasma, giữ EV.beamStart.

```text
An edited sequence of isolated a floating energy emitter igniting a sustained heat beam, a rapid power gathering whine, a forceful arc strike, dense plasma friction over a deep electrical hum, a short low echo, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.tia.start.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:261–266; games/typing-survival/src/audio/theme-audio.ts:260–267 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.tia.loop`

- Tên: Heat Beam; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Suốt lúc Heat Beam cháy, chỉ khi game đang chạy.
- Pha: travel; khớp VFX: Bám đoạn tia đang quét; dừng theo trạng thái beam.
- Độ dài phần cắt: 2000–2000 ms; dạng `loop`; 1 biến thể; 1 cú/lượt; **3 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.tia.loop/`
- Gợi ý diễn bằng giọng: Giữ ù đều một hơi.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
A continuous sound recording of a continuous steady plasma beam texture with a deep fifty five hertz electrical hum, dense low energy friction and fine electrical grains above five kilohertz, constant level and constant timbre throughout, seamless sustained material.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Thẻ trống hoặc chưa có: lấy mốc tác giả từ THEME_SOUND_LIST.md và hàm phát; không phải số đo Firefly. THEME_SOUND_LIST.md §4/§9: prompt vòng 2 s; gun-audio.ts:74–76: nền duy trì, nhỏ hơn âm khởi đầu; biến thể 1 là mặc định biên tập theo THEME_SOUND_LIST §2. games/typing-survival/src/view/beams.ts:172–184; games/typing-survival/src/audio/theme-audio.ts:206–214 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.tia.end`

- Tên: Heat Beam; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Heat Beam ngừng cháy.
- Pha: aftermath; khớp VFX: Heat Beam tắt tại EV.beamEnd, còn vệt cháy sàn.
- Độ dài phần cắt: 320–480 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.tia.end/`
- Gợi ý diễn bằng giọng: Vuốt thấp dần, tắt gọn.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
An edited sequence of isolated an energy beam extinguishing, a descending electrical release, a contracting plasma body and a low resonant decay below one kilohertz across a wide ancient stone and graphite steel causeway, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.tia.end.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:269–271; games/typing-survival/src/audio/theme-audio.ts:270–271 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.tia.pulse`

- Tên: Heat Beam; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Một nhịp Heat Beam có quái trúng.
- Pha: impact; khớp VFX: Lóe cắt trên quái, gom theo khung có tiaHits.
- Độ dài phần cắt: 40–60 ms; dạng `hits`; 4 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.tia.pulse/`
- Gợi ý diễn bằng giọng: Xẹt rất ngắn, gọn.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
An edited sequence of isolated tiny concentrated beam contacts biting into cracked black glass, a crisp electrical strike, a tightly compressed sizzling body and a fine high frequency decay above four kilohertz, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.tia.pulse.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:193,294; games/typing-survival/src/audio/theme-audio.ts:275–280 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.tan.fire`

- Tên: Scatter Gun; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Scatter Gun tung một loạt 7 viên.
- Pha: release; khớp VFX: Lóe nòng rộng và chùm đạn rời tại EV.volley.
- Độ dài phần cắt: 240–360 ms; dạng `hits`; 4 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.tan.fire/`
- Gợi ý diễn bằng giọng: Khóa ngắn rồi bật rộng có lực.
- Thời kỳ: `reworded`. Khóa bơm và vỏ đạn cơ khí đổi thành nổ chùm plasma từ súng canh, giữ một âm mỗi volley.

```text
An edited sequence of isolated wide energy scatter blasts from a floating sentinel gun, a brief loading catch, a sharp crystalline release, a heavy spreading plasma body and sparkling fragments over a short low causeway echo, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.tan.fire.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/gunfx.ts:71–72 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.ray.armed`

- Tên: Rail Gun; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Rail Gun có băng chờ, chưa vào nhịp nạp.
- Pha: charge; khớp VFX: Đạn sáng lơ lửng ở nòng; vòng điện giữ sẵn.
- Độ dài phần cắt: 2000–2000 ms; dạng `loop`; 1 biến thể; 1 cú/lượt; **3 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.ray.armed/`
- Gợi ý diễn bằng giọng: Ù nhỏ đều, hơi điện rất cao.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
A continuous sound recording of a small charged energy capacitor held ready, a quiet continuous hum below four hundred hertz and a faint electric glitter above five kilohertz, constant level and constant timbre throughout, seamless sustained material.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Thẻ trống hoặc chưa có: lấy mốc tác giả từ THEME_SOUND_LIST.md và hàm phát; không phải số đo Firefly. THEME_SOUND_LIST.md §4/§9: prompt vòng 2 s; gun-audio.ts:74–76: nền duy trì, nhỏ hơn âm khởi đầu; biến thể 1 là mặc định biên tập theo THEME_SOUND_LIST §2. games/typing-survival/src/view/beams.ts:163–165; games/typing-survival/src/audio/gun-audio.ts:76 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.ray.charge`

- Tên: Rail Gun; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Rail Gun bắt đầu nạp một phát, 0,15 s.
- Pha: charge; khớp VFX: Vòng điện co về nòng tại EV.charge; không lùi tick bắn.
- Độ dài phần cắt: 120–180 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.ray.charge/`
- Gợi ý diễn bằng giọng: Rít lên dốc rồi dứt ở đỉnh.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
An edited sequence of isolated a rail emitter gathering power for a shot, a tightly rising capacitor whine and concentrated electrical tension ending precisely at its peak, a compact preparation gesture, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.ray.charge.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/gunfx.ts:73–74 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.ray.fire`

- Tên: Rail Gun; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Rail Gun bắn tia xuyên.
- Pha: release; khớp VFX: Đầu tia thẳng bật ở nòng tại EV.rail.
- Độ dài phần cắt: 560–840 ms; dạng `hits`; 4 biến thể; 6 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.ray.fire/`
- Gợi ý diễn bằng giọng: Bật đanh, thân nặng rồi ngân xa.
- Thời kỳ: `reworded`. Nổ súng ray cơ khí đổi thành nhát xả năng lượng xuyên có đuôi ion, giữ EV.rail.

```text
An edited sequence of isolated a powerful rail energy discharge from a floating sentinel gun, an extremely sharp crystalline crack, a dense low plasma body, electricity tearing above four kilohertz and a dark resonant tail below one kilohertz, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.ray.fire.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/gunfx.ts:75–76 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.phao.launch`

- Tên: Star Mortar; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Star Mortar phóng một quả.
- Pha: release; khớp VFX: Cầu sáng rời nòng và bắt đầu cung bay tại EV.launch.
- Độ dài phần cắt: 400–600 ms; dạng `hits`; 4 biến thể; 7 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.phao.launch/`
- Gợi ý diễn bằng giọng: Khóa, phóng có lực, rít xa.
- Thời kỳ: `reworded`. Đạn trượt vào ống thép đổi thành quả sáng khóa năng lượng và phóng theo cung từ súng canh.

```text
An edited sequence of isolated a heavy luminous mortar orb launching from a floating sentinel gun, a brief chamber lock, a forceful launch crack with a weighty resonant body, a high ion whistle receding through space and a short low causeway echo, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.phao.launch.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/gunfx.ts:77–78 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `gun.phao.burst`

- Tên: Star Mortar; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Quả Star Mortar nổ; tiếng riêng thay hit.* trong vùng.
- Pha: impact; khớp VFX: Lóe nổ vùng tại EV.burst; các nổ liền leo nửa cung theo mã.
- Độ dài phần cắt: 480–720 ms; dạng `hits`; 3 biến thể; 6 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/gun.phao.burst/`
- Gợi ý diễn bằng giọng: Nứt giòn rồi nổ nặng, mảnh rơi.
- Thời kỳ: `reworded`. Nổ mảnh trên sàn thép đổi thành quả plasma phá kính đen trên đường đắp đá cổ, giữ tiếng nổ vùng riêng.

```text
An edited sequence of isolated a heavy plasma orb detonating on graphite steel and ancient stone, a sharp crystalline rupture, a deep expansive blast with a dense energy body, black glass fragments scattering and a low rolling spatial decay, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/gun.phao.burst.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/gunfx.ts:79–82; games/typing-survival/src/view/combat.ts:197–198 Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53

## `hit.t1`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Đòn bậc T1 trúng, gom khoảng 38 ms.
- Pha: impact; khớp VFX: Lóe trúng nhẹ sau cửa sổ gom; không thêm thời gian chờ.
- Độ dài phần cắt: 112–168 ms; dạng `hits`; 6 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/hit.t1/`
- Gợi ý diễn bằng giọng: Keng kính gọn, thân nhỏ.
- Thời kỳ: `reworded`. Keng nhẹ trên vỏ thép đổi thành nứt kính đen nhỏ, vẫn là đầu và thân của bậc T1.

```text
An edited sequence of isolated small energy projectiles striking cracked black glass, a bright crisp fracture, a compact solid glass body and a brief high shimmer above four kilohertz, tightly focused impact material, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/hit.t1.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:185–198; games/typing-survival/src/audio/theme-audio.ts:294–303 Đòn thường/crit/perfect có T1–T3; content/chapter-1.ts:39–53

## `hit.t2`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Đòn bậc T2 hoặc T3 trúng, gom khoảng 38 ms.
- Pha: impact; khớp VFX: Lóe crit hoặc perfect tại mục tiêu; mã giữ mức theo số trúng.
- Độ dài phần cắt: 208–312 ms; dạng `hits`; 4 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/hit.t2/`
- Gợi ý diễn bằng giọng: Nứt chắc, thân dày hơn bậc nhẹ.
- Thời kỳ: `reworded`. Keng trên thép dày đổi thành va chạm kính đen dày, vẫn là đầu và thân T2–T3 để ghép sub sau.

```text
An edited sequence of isolated medium energy impacts on thick cracked black glass, a hard bright fracture and a dense resonant glass body below one kilohertz, a compact high shimmer above four kilohertz, focused impact material, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/hit.t2.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:185–198; games/typing-survival/src/audio/theme-audio.ts:294–303 Đòn thường/crit/perfect có T1–T3; content/chapter-1.ts:39–53

## `hit.armour`

- Tên: Armor; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Armor của quái chặn phần lớn đòn, gồm Brute.
- Pha: impact; khớp VFX: Các tia lửa bật khỏi giáp tại EV.hit có FLAG.armour.
- Độ dài phần cắt: 240–360 ms; dạng `hits`; 6 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/hit.armour/`
- Gợi ý diễn bằng giọng: Keng chắc bật ra, gọn.
- Thời kỳ: `reworded`. Đòn bị vỏ máy chặn đổi thành đạn năng lượng bật khỏi Armor; vai trò báo bị chặn giữ nguyên.

```text
An edited sequence of isolated energy projectiles glancing off thick armor, a bright metallic strike with a solid plate body, sparks scattering above four kilohertz and a short low resonance across graphite steel, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/hit.armour.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:185–190; games/typing-survival/src/audio/theme-audio.ts:82 Brute Armor 4 từ 80 s; content/foes.ts:46; content/chapter-1.ts:49; affix giáp còn có ở sim/pace.ts:244–250

## `hit.sub`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Lớp dưới dùng chung từ T2, dành cho phiếu gắn sau.
- Pha: impact; khớp VFX: Ghép đúng đầu trúng T2+ theo cờ bass, không phát riêng.
- Độ dài phần cắt: 80–120 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/hit.sub/`
- Gợi ý diễn bằng giọng: Hơi trầm nén rất gọn.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
An edited sequence of isolated low frequency reinforcement layers for a heavy energy impact, a controlled pressure onset, a compact forty to ninety hertz body and a quick natural decay, isolated lower layer material for composite impacts, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/hit.sub.yaml (duration.min_ms/max_ms, variants.target). Thẻ trống hoặc chưa có: lấy mốc tác giả từ THEME_SOUND_LIST.md và hàm phát; không phải số đo Firefly. Chưa có id phát trong mã. AUDIO_PIPELINE.md §6.3 mục 3, §8.3 ưu tiên hơn ghi chú cũ THEME_SOUND_LIST.md:31; theme-audio.ts:294–307 hiện ghép sub trong flush(), tone 160 ms; trần 120 ms lấy AUDIO_PIPELINE.md:632. Khoảng 80–120 ms là mục tiêu biên tập đề xuất. games/typing-survival/src/audio/theme-audio.ts:294–303 Lớp dự kiến tách file, chưa có id riêng trong SOUND_IDS. AUDIO_PIPELINE §6.3 mục 3 / §8.3; Sự kiện nền tảng có trong ải.

## `hit.tail`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Lớp đuôi dùng chung theo cờ tail, dành cho phiếu gắn sau.
- Pha: aftermath; khớp VFX: Bắt theo tiếng trúng đủ bậc; hiện First Shift chỉ có T1–T3.
- Độ dài phần cắt: 500–700 ms; dạng `hits`; 2 biến thể; 7 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/hit.tail/`
- Gợi ý diễn bằng giọng: Ngân trầm lan xa, vào mềm.
- Thời kỳ: `reworded`. Đuôi kim loại trong hành lang đổi thành ngân thấp của thép than chì và đá cổ trên đường đắp rộng.

```text
An edited sequence of isolated low resonant aftermath layers spreading across graphite steel and ancient stone, a soft onset, a dark ringing body below one kilohertz and a spacious fading decay, isolated tail material for composite impacts, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/hit.tail.yaml (duration.min_ms/max_ms, variants.target). Thẻ trống hoặc chưa có: lấy mốc tác giả từ THEME_SOUND_LIST.md và hàm phát; không phải số đo Firefly. Chưa có id phát trong mã. AUDIO_PIPELINE.md §6.3 mục 3; THEME_SOUND_LIST.md:31 nói lớp đề xuất; theme-audio.ts:294–307 flush() có thân đuôi 500/700 ms từ T4. Giữ theo yêu cầu phiếu 212 dù c1-s1 hiện không đạt T4. games/typing-survival/src/audio/theme-audio.ts:294–307 Lớp dự kiến tách file, chưa có id riêng trong SOUND_IDS. AUDIO_PIPELINE §6.3 mục 3 / §8.3; T4 chưa đạt trong ải.

## `kill.swarm`

- Tên: Swarm; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Quái không mang cờ Scout chết, có gom cụm; Brute cũng đi nhánh này.
- Pha: impact; khớp VFX: Kính đen vỡ và nứt cam tắt ở EV.kill; Brute có VFX chết lớn riêng.
- Độ dài phần cắt: 200–300 ms; dạng `hits`; 6 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/kill.swarm/`
- Gợi ý diễn bằng giọng: Rạn, vỡ vụn, mảnh lăn.
- Thời kỳ: `reworded`. Kim loại vỡ đổi thành kính đen vỡ; Brute vẫn dùng cùng nhánh âm hiện tại.

```text
An edited sequence of isolated small void creatures of cracked black glass breaking apart, a compressed rupture, crunchy glass fragmentation, a compact low energy collapse and bright shards scattering across ancient stone with a short dark decay, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/kill.swarm.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:351–366; games/typing-survival/src/audio/theme-audio.ts:319 Swarm và Brute không mang cờ Scout; content/foes.ts:44,46; content/chapter-1.ts:39–53

## `kill.elite`

- Tên: Scout; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Cụm chết có cờ Scout; không phải mọi quái lớn.
- Pha: impact; khớp VFX: Scout vỡ tại EV.kill, mảnh kính và phóng điện.
- Độ dài phần cắt: 400–600 ms; dạng `hits`; 3 biến thể; 7 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/kill.elite/`
- Gợi ý diễn bằng giọng: Vỡ mạnh, điện xé, mảnh rơi.
- Thời kỳ: `reworded`. Máy thép nổ đổi thành Scout kính đen tan cùng phóng điện.

```text
An edited sequence of isolated a medium armored void creature of black glass collapsing, a tense crystalline fracture, a forceful energy rupture with a dense body, electrical discharge and falling glass fragments, a short low spatial decay, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/kill.elite.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:351–366; games/typing-survival/src/audio/theme-audio.ts:319 Cụm có Scout từ 12 s, không lấy kích cỡ làm cờ; content/chapter-1.ts:48; view/combat.ts:337,351,366

## `kill.chime`

- Tên: —; ưu tiên **P0**. Đòn chữ, súng, trúng và chết: nhóm tạo lực chiến đấu được làm trước.
- Khi nào: Lớp nốt của chuỗi hạ, hiện còn nhúng trong kill().
- Pha: aftermath; khớp VFX: Nốt đi cùng cụm chết; mã đổi cao độ theo chuỗi dưới 1 s.
- Độ dài phần cắt: 240–240 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/kill.chime/`
- Gợi ý diễn bằng giọng: Một nốt rõ, ngân cao nhẹ.
- Thời kỳ: `reworded`. Thanh thép leo nốt đổi chất âm tinh thể; sự kiện nốt thưởng vẫn còn.

```text
An edited sequence of isolated crystalline reward notes struck at C5 as neutral pitch source material, a brief bright contact, a compact low ringing body and a delicate high shimmer above four kilohertz, consistent pitch across takes, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/kill.chime.yaml (duration.min_ms/max_ms, variants.target). Thẻ trống hoặc chưa có: lấy mốc tác giả từ THEME_SOUND_LIST.md và hàm phát; không phải số đo Firefly. Giữ vì sự kiện nốt hạ vẫn còn ở hướng B. THEME_SOUND_LIST.md §5, AUDIO_PIPELINE.md §6.4/§8.3 yêu cầu tách nốt; theme-audio.ts:315–328 hiện nốt nhúng 240 ms, chưa có id riêng. Mục tiêu biên tập 240 ms, biến thể 1 theo thẻ. Không nhúng nốt vào prompt kill.swarm/elite. games/typing-survival/src/audio/theme-audio.ts:315–328 Lớp dự kiến tách file, chưa có id riêng trong SOUND_IDS. AUDIO_PIPELINE §6.3 mục 3 / §8.3; Sự kiện nền tảng có trong ải.

## `foe.shot`

- Tên: Scout; ưu tiên **P1**. Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.
- Khi nào: Scout bắn cầu plasma về tuyến từ sau giây 12.
- Pha: release; khớp VFX: Lóe nòng Scout tại EV.foeShot, đạn bắt đầu bay.
- Độ dài phần cắt: 200–300 ms; dạng `hits`; 4 biến thể; 8 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/foe.shot/`
- Gợi ý diễn bằng giọng: Vo lên ngắn rồi xé lao tới.
- Thời kỳ: `reworded`. Cầu plasma của lính máy đổi bối cảnh thành phát bắn của Scout kính đen, giữ nạp ngắn và tiếng lao tới.

```text
An edited sequence of isolated small hostile plasma shots, a quick rising charge, a sharp energetic release and a rushing compact plasma body moving toward the listener, a short low spatial decay, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/foe.shot.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:233–235; games/typing-survival/src/audio/theme-audio.ts:336 Scout từ 12 s; content/chapter-1.ts:48; foe.shot.down cần Pulse Gun trong lựa chọn 2/5

## `foe.shot.down`

- Tên: Scout; ưu tiên **P1**. Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.
- Khi nào: Pulse Gun bắn hạ đạn Scout giữa đường.
- Pha: impact; khớp VFX: Đạn vỡ và tia lửa tại EV.shotDown.
- Độ dài phần cắt: 120–180 ms; dạng `hits`; 6 biến thể; 8 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/foe.shot.down/`
- Gợi ý diễn bằng giọng: Tách giòn, mảnh nhỏ tan.
- Thời kỳ: `reworded`. Đạn kim loại vỡ đổi thành cầu plasma bị chặn với tia lửa và mảnh tinh thể, giữ EV.shotDown.

```text
An edited sequence of isolated small plasma projectiles intercepted in midair, a crisp crystalline fracture, a tiny compressed energy breakup, bright sparks and fine fragments dispersing into a short high decay, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/foe.shot.down.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:237–240; games/typing-survival/src/audio/theme-audio.ts:344 Scout từ 12 s; content/chapter-1.ts:48; foe.shot.down cần Pulse Gun trong lựa chọn 2/5

## `hurt.hull`

- Tên: Armor; ưu tiên **P1**. Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.
- Khi nào: Đạn Scout chạm người chơi.
- Pha: impact; khớp VFX: Giáp Lightbearer lóe khiên lam, áo choàng giật tại EV.playerHit.
- Độ dài phần cắt: 320–480 ms; dạng `hits`; 3 biến thể; 8 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/hurt.hull/`
- Gợi ý diễn bằng giọng: Va chắc rồi ngân thấp.
- Thời kỳ: `reworded`. Thân tàu bị đập đổi thành giáp Lightbearer lóe khiên lam và áo choàng giật.

```text
An edited sequence of isolated a plasma projectile striking an armored caped guardian's blue energy shield, a sharp glasslike collision, a dense protective resonance, a brief electrical scatter and a low fading rumble, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/hurt.hull.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:223–228; games/typing-survival/src/audio/theme-audio.ts:352–365 Scout từ 12 s; content/chapter-1.ts:48; foe.shot.down cần Pulse Gun trong lựa chọn 2/5

## `hurt.breach`

- Tên: Armor; ưu tiên **P1**. Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.
- Khi nào: Quái vượt vạch cuối, làm mất Armor.
- Pha: impact; khớp VFX: Vòng đỏ và giật người tại EV.breach.
- Độ dài phần cắt: 640–960 ms; dạng `hits`; 1 biến thể; 6 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/hurt.breach/`
- Gợi ý diễn bằng giọng: Nổ có thân, hai nhịp báo ngắn.
- Thời kỳ: `reworded`. Thủng thân trạm đổi thành tuyến phòng thủ bị phá và mất Armor của nhân vật, giữ va chạm kèm báo động.

```text
An edited sequence of isolated a defensive line breached on an ancient stone and graphite steel causeway, a forceful pressure rupture, a deep resonant structural body and a brief two tone warning, a low rolling decay, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/hurt.breach.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:213–218; games/typing-survival/src/audio/theme-audio.ts:352–360 Để quái áp sát/vượt tuyến hoặc Armor cạn; content/chapter-1.ts:24,42–53; sim/pace.ts:119–145

## `hurt.drain`

- Tên: Armor; ưu tiên **P1**. Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.
- Khi nào: Quái trong vùng gần hút Armor; tối đa một tiếng mỗi 420 ms.
- Pha: impact; khớp VFX: Đốm sáng giáp và luồng hút tại EV.drain.
- Độ dài phần cắt: 120–180 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/hurt.drain/`
- Gợi ý diễn bằng giọng: Rè điện nhỏ, bám rồi tắt.
- Thời kỳ: `reworded`. Điện hút trên tấm thép đổi thành hồ quang hút trường bảo vệ quanh giáp nhân vật, vẫn giới hạn mỗi 420 ms.

```text
An edited sequence of isolated small parasitic energy arcs draining an armored guardian's protective field, a crisp electrical attachment, a restrained low sizzling body and a fine high crackle fading above four kilohertz, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/hurt.drain.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:245–250; games/typing-survival/src/audio/theme-audio.ts:372–378 Để quái áp sát/vượt tuyến hoặc Armor cạn; content/chapter-1.ts:24,42–53; sim/pace.ts:119–145

## `alarm.surge`

- Tên: —; ưu tiên **P1**. Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.
- Khi nào: Đợt dồn bắt đầu, mốc gốc 50 và 115 s có thể được pace dời.
- Pha: null (ngoài đòn); khớp VFX: Khớp peak đổi sang dương khi đang play; hướng B quái vật xa ngẩng lên.
- Độ dài phần cắt: 1040–1560 ms; dạng `single`; 1 biến thể; 1 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/alarm.surge/`
- Gợi ý diễn bằng giọng: Hai lượt lên xuống, trầm và rộng.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
A single urgent warning gesture at the edge of a distant black hole, two rising and falling resonant calls over a deep pressure drone, a broad ominous body and a low fading spatial tail.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/alarm.surge.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/app/main.ts:649; games/typing-survival/src/audio/theme-audio.ts:392–399 Hai surge gốc 50/115 s; content/chapter-1.ts:47; pace có thể dời, sim/pace.ts:223–225

## `end.win`

- Tên: —; ưu tiên **P1**. Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.
- Khi nào: Giữ đủ 150 s và thắng.
- Pha: null (ngoài đòn); khớp VFX: EV.end thắng mở băng rôn trước thẻ kết quả 0,9 s.
- Độ dài phần cắt: 1600–2400 ms; dạng `single`; 1 biến thể; 1 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/end.win/`
- Gợi ý diễn bằng giọng: Mở hợp âm chắc rồi thả nhẹ.
- Thời kỳ: `reworded`. Hợp âm máy kèm xả hơi đổi thành hợp âm năng lượng và âm bội tinh thể vàng trắng, cùng sự kiện thắng.

```text
A single victorious science fiction resolution, a weighty A power chord opening into white gold crystalline overtones, a brief bright crest, a deep relieved body and a spacious low decay.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/end.win.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:283–285; games/typing-survival/src/audio/theme-audio.ts:403–409 Giữ đủ 150 s; content/chapter-1.ts:42

## `end.lose`

- Tên: —; ưu tiên **P1**. Quái bắn, bị đánh, đợt dồn hoặc kết trận: nhóm báo tình trạng sau P0.
- Khi nào: Armor cạn, tuyến thua.
- Pha: null (ngoài đòn); khớp VFX: EV.end thua mở băng rôn trước thẻ kết quả 0,9 s.
- Độ dài phần cắt: 1600–2400 ms; dạng `single`; 1 biến thể; 1 cú/lượt; **2 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/end.lose/`
- Gợi ý diễn bằng giọng: Hạ dần, rạn rồi chìm.
- Thời kỳ: `reworded`. Máy hạ điện và thép sụp đổi thành trường năng lượng tắt, kính đen lắng trên đá cổ, cùng sự kiện thua.

```text
A single defeated energy field collapse, a descending power resonance, cracked black glass settling in several weighted contacts on ancient stone, a deep fading body and a dark spatial decay.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/end.lose.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:283–285; games/typing-survival/src/audio/theme-audio.ts:403–415 Để quái áp sát/vượt tuyến hoặc Armor cạn; content/chapter-1.ts:24,42–53; sim/pace.ts:119–145

## `support.repair`

- Tên: Armor; ưu tiên **P2**. UI, sao hoặc tiếp tế: nhóm phụ sau P0 và P1.
- Khi nào: Pace chọn support khi gần thua và director bật.
- Pha: null (ngoài đòn); khớp VFX: Vòng xanh từ trên xuống, Armor tăng tại EV.support.
- Độ dài phần cắt: 720–1080 ms; dạng `hits`; 1 biến thể; 5 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/support.repair/`
- Gợi ý diễn bằng giọng: Nâng lên, khép êm, ngân nhẹ.
- Thời kỳ: `reworded`. Khoang sửa cập đổi thành vòng xanh từ trên xuống, vẫn tăng Armor.

```text
An edited sequence of isolated a restorative green energy ring descending around an armored guardian, a smooth gathering rise, a precise crystalline closure, a warm low resonant body and a soft high shimmer, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/support.repair.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/view/combat.ts:253–258; games/typing-survival/src/sim/pace.ts:229–233 Director bật và chọn support khi nguy; content/chapter-1.ts:52; content/stage-rules.ts:103; sim/pace.ts:97–98,229–233

## `star.get`

- Tên: —; ưu tiên **P2**. UI, sao hoặc tiếp tế: nhóm phụ sau P0 và P1.
- Khi nào: Kết ải có ít nhất một sao; hiện mã gọi một lần cho cả nhóm.
- Pha: null (ngoài đòn); khớp VFX: Khớp settle kết ải có stars.some(Boolean), không đợi từng sao bay.
- Độ dài phần cắt: 400–600 ms; dạng `hits`; 1 biến thể; 7 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/star.get/`
- Gợi ý diễn bằng giọng: Một ting sáng, ngân gọn.
- Thời kỳ: `kept`. Cùng sự kiện và vai trò; giữ hình dạng âm, diễn đạt bằng vật liệu hướng B.

```text
An edited sequence of isolated a small crystalline reward star arriving, a precise bright contact, a delicate ringing body and a short airy shimmer above four kilohertz, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/star.get.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/app/main.ts:182–186 Ải khác s0 và stars.some(Boolean); app/main.ts:182–186; content/chapter-1.ts:39–42

## `ui.move`

- Tên: —; ưu tiên **P2**. UI, sao hoặc tiếp tế: nhóm phụ sau P0 và P1.
- Khi nào: Đổi mục hoặc giá trị cài đặt.
- Pha: null (ngoài đòn); khớp VFX: Nút đổi focus hoặc rê chuột, lóe lam.
- Độ dài phần cắt: 12–18 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/ui.move/`
- Gợi ý diễn bằng giọng: Chạm kính rất gọn.
- Thời kỳ: `reworded`. Rơ-le chọn mục đổi thành chạm kính khói rất ngắn, giữ hành động đổi focus.

```text
An edited sequence of isolated tiny smoked glass interface contacts, a dry precise crystalline tick with a tightly controlled brief resonance, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/ui.move.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/app/main.ts:393,472,502; games/typing-survival/src/app/journey.ts:222,235 Menu, cài đặt và chọn súng quanh First Shift; app/journey.ts:142,194–205; app/main.ts:390–416

## `ui.select`

- Tên: —; ưu tiên **P2**. UI, sao hoặc tiếp tế: nhóm phụ sau P0 và P1.
- Khi nào: Chọn mục, nút hoặc súng.
- Pha: null (ngoài đòn); khớp VFX: Nút lóe lam, bảng mở bằng đường sáng.
- Độ dài phần cắt: 120–180 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/ui.select/`
- Gợi ý diễn bằng giọng: Chạm chắc rồi ù thấp.
- Thời kỳ: `reworded`. Công tắc nặng đổi thành chạm kính khói và cộng hưởng xác nhận thấp, giữ hành động chọn.

```text
An edited sequence of isolated smoked glass interface selections, a crisp glass contact, a compact low confirmation resonance and a fine white gold shimmer, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/ui.select.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/app/main.ts:416,579; games/typing-survival/src/app/journey.ts:205,261 Menu, cài đặt và chọn súng quanh First Shift; app/journey.ts:142,194–205; app/main.ts:390–416

## `ui.back`

- Tên: —; ưu tiên **P2**. UI, sao hoặc tiếp tế: nhóm phụ sau P0 và P1.
- Khi nào: Đóng bảng hoặc quay lại.
- Pha: null (ngoài đòn); khớp VFX: Bảng khép, đường sáng rút khi Esc hoặc back.
- Độ dài phần cắt: 120–180 ms; dạng `hits`; 1 biến thể; 8 cú/lượt; **1 lượt**.
- Thư mục nhận: `~/AudioLab/inbox/firefly/typing-survival/ui.back/`
- Gợi ý diễn bằng giọng: Chạm thấp hơn chọn, tắt nhẹ.
- Thời kỳ: `reworded`. Công tắc hạ đổi thành kính khói khép và ngân thấp đi xuống, giữ hành động quay lại.

```text
An edited sequence of isolated smoked glass interface closures, a lower gentle crystalline contact, a compact descending low resonance and a soft brief decay, each one followed by a second of silence.
```

Căn cứ: Hướng B: docs/games/ART_DIRECTION_2026-10-28.md:547–575; hình dạng Q6: tools/audio-lab/DECISIONS.md §Q6. Độ dài và số biến thể: tools/audio-lab/specs/typing-survival/ui.back.yaml (duration.min_ms/max_ms, variants.target). games/typing-survival/src/app/main.ts:398,483; games/typing-survival/src/app/journey.ts:200,267 Menu, cài đặt và chọn súng quanh First Shift; app/journey.ts:142,194–205; app/main.ts:390–416

## Loại trừ

| Id | Lý do | Ải đầu tiên |
|---|---|---|
| `key.ok` | Tiếng phím do bộ Firefly 189–191 phụ trách, không làm trùng. | s0 |
| `key.bad` | Tiếng phím do bộ Firefly 189–191 phụ trách, không làm trùng. | s0 |
| `music.calm` | Nhạc là stem 96 BPM La thứ theo AUDIO_PIPELINE §8.3, không phải SFX. | s0 |
| `music.surge` | Nhạc là stem 96 BPM La thứ theo AUDIO_PIPELINE §8.3, không phải SFX. | s0 |
| `leader.horn` | Cần Pack Leader, chỉ objective hunt đưa vào. | c1-s2 |
| `leader.down` | Cần tiến độ hunt tăng sau khi hạ Pack Leader. | c1-s2 |
| `rift.warn` | Cần telegraph Rift; First Shift hazard null. | c1-s3 |
| `rift.open` | Cần Rift mở; First Shift hazard null. | c1-s3 |
| `shield.hit` | Cần Shield Guard; First Shift chỉ có brute pack. | c1-s4 |
| `shield.break` | Cần Shield Guard; First Shift chỉ có brute pack. | c1-s4 |
| `foe.split` | Cần Splitter; chưa có ải nào trong CHAPTER_1 hoặc Trial khai báo splitter pack. | Chưa có trong mã hiện tại |
| `hit.t4` | Không đạt T4: combat.ts chỉ truyền T1–T3 vào audio.hit; chưa có ải đầu tiên phát được trong mã hiện tại. | Chưa có trong mã hiện tại |

## Id cũ dừng sản xuất

| Id | Lý do | Ải đầu tiên |
|---|---|---|
| `gun.xung.loop` | Nền cơ khí liên thanh thời tàu không còn sự kiện âm riêng trong hướng B: Pulse Gun phát từng viên và có đuôi riêng, không có lệnh loop này. | Chưa có trong mã hiện tại |
