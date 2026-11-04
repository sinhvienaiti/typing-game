# Kiểm tra âm thanh chiêu và giao chiến Tu Tiên Thủ Ải (04/11/2026)

Phạm vi: mọi file âm thanh lab chiêu đang phát (`games/immortality-cultivation/art-src/lab/audio/`, 91 file, 34 sự kiện, theo `manifest.json` và `SOURCES.json`). Game chính (`src/audio/catalog.ts`) vẫn là danh mục **im lặng** M0a (`silent: true`), chưa phát file nào.

Chỉ đo bằng số (ffmpeg). **Không ai nghe.** Mọi nhận xét về chất âm là `NOT LISTENED`, chờ tai anh.

- Số liệu: `typing-game-review/captures/tu-tien/sound-audit/measurements.json` (từng file) và `summary-by-event.json` (theo sự kiện), có `ABOUT.md`.
- Cách đo: `ebur128=peak=true` (integrated, true peak); momentary max có đệm 1 s im lặng; đường bao RMS 10 ms (16 kHz mono) cho thời gian lên đỉnh và đuôi tới −20/−40 dB sau đỉnh; năng lượng ba dải thấp < 250 Hz, giữa 250 Hz–4 kHz, cao > 4 kHz.
- Quy tắc so: `game-art-pipeline/references/audio.md` §5.3 (lớp), §5.4 (bậc to, theo momentary max), §5.8 (đuôi nướng sẵn cộng send vang trong game).
- `SOURCES.json` ghi rõ: "provisional, not owner-approved (03/11/2026)", lớp lấy từ lô Firefly 03/11 (`FIREFLY_BATCH_2026-11-03.md`).

## 1. Bảng đo theo sự kiện

Ô phím theo `skills-main.ts`: auto, k1, k2, guard (ô 3), dash (ô 6), k4, k5, k7; ultimate = k7 cùng ba sự kiện `world-*` [INFERENCE từ mã lab, chưa đối chiếu canon].

| Sự kiện | Lớp | Dài (s) | Mom. max (LUFS) | Integrated | TP max (dBTP) | Lên đỉnh (ms) | Đuôi −40 dB (ms) | Thấp / giữa / cao |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| cast | 1 | 1.71 | −17.0 | −20.0 | −7.4 | 327 | 927 | .59 / .22 / .19 |
| release | 2 | 1.62 | −11.4 | −14.0 | −1.5 | 327 | 880 | .67 / .29 / .04 |
| release-auto | 1 | 2.10 | −15.0 | −18.0 | −8.5 | 223 | 1383 | .19 / .18 / .64 |
| release-k1 | 2 | 2.10 | −10.2 | −14.0 | −4.3 | 217 | 1413 | .29 / .17 / .54 |
| release-k1-fire | 2 | 1.94 | −13.5 | −16.0 | −4.6 | 463 | 1310 | .92 / .08 / .00 |
| release-k2 | 3 | 1.78 | −10.2 | −14.0 | −1.0 | 330 | 1017 | .72 / .23 / .05 |
| release-guard | 2 | 3.21 | −7.6 | −12.9 | −1.2 | 427 | 2163 | .00 / .57 / .43 |
| release-dash | 1 | 1.43 | −14.2 | −17.0 | −5.4 | 320 | 857 | .68 / .29 / .03 |
| release-k4 | 3 | 2.95 | −9.6 | −14.6 | −1.2 | 167 | 2657 | .85 / .04 / .12 |
| release-k5 | 2 | 2.89 | −8.5 | −14.1 | −1.2 | **2137** | **470** | .89 / .09 / .03 |
| release-k7 | 2 | 2.89 | −7.6 | −12.5 | −1.5 | **1823** | 977 | .72 / .11 / .17 |
| release-k7-fire | 2 | 2.99 | −9.7 | −14.0 | −1.2 | 393 | 2550 | .95 / .05 / .00 |
| flyby | 1 | 1.39 | −15.9 | −19.0 | −8.6 | 413 | 763 | .11 / .37 / .52 |
| flyby-fire | 1 | 1.39 | −18.7 | −21.0 | −9.7 | 367 | 940 | .77 / .23 / .00 |
| impact-flesh | 2 | 1.86 | −10.6 | −15.0 | −1.1 | 173 | 1387 | .78 / .19 / .03 |
| impact-flesh-fire | 2 | 1.82 | −11.2 | −15.0 | −1.5 | 133 | 1507 | .94 / .05 / .01 |
| impact-stone | 2 | 1.44 | −10.1 | −14.5 | −1.3 | 117 | 1147 | .66 / .23 / .11 |
| impact-stone-fire | 2 | 1.82 | −10.5 | −15.2 | −1.1 | 123 | 1590 | .93 / .05 / .02 |
| impact-spirit | 2 | 2.34 | −10.2 | −15.7 | −1.6 | 90 | 1537 | .83 / .12 / .04 |
| impact-spirit-fire | 2 | 1.89 | −10.3 | −14.9 | −1.6 | 43 | 1810 | .96 / .04 / .01 |
| death | 2 | 2.16 | −13.0 | −16.1 | −2.3 | 360 | 1523 | .66 / .27 / .07 |
| death-fire | 2 | 1.79 | −11.9 | −18.1 | −1.4 | 140 | 1540 | .92 / .08 / .00 |
| world-open | 2 | 5.90 | −11.9 | −15.2 | −2.6 | 1880 | 3237 | .93 / .06 / .01 |
| world-open-fire | 2 | 5.29 | −9.2 | −14.3 | −1.2 | 773 | 4040 | .94 / .06 / .00 |
| world-climax | 3 | 4.00 | −10.6 | −16.3 | −1.0 | 103 | 3817 | .98 / .01 / .00 |
| world-climax-fire | 3 | 3.97 | −8.8 | −12.3 | −1.0 | 193 | 3693 | .96 / .04 / .00 |
| world-close | 2 | 5.55 | −10.2 | −17.0 | −1.0 | 343 | 3653 | .72 / .26 / .01 |
| world-close-fire | 2 | 5.07 | −10.7 | −18.0 | −2.7 | 483 | 2333 | .88 / .11 / .01 |
| callout (hey/ha) | 2 take | 0.94 | −10.7 | −14.5 | −1.1 | 90 | 705 | .20 / .77 / .03 |
| callout-k2 | 1 | 2.37 | −11.2 | −14.1 | −1.4 | 830 | 1350 | .27 / .66 / .07 |
| callout-guard | 1 | 1.59 | −11.2 | −15.0 | −1.5 | 20 | 1290 | .08 / .92 / .00 |
| callout-k4 | 1 | 2.01 | −11.2 | −13.1 | −1.4 | 740 | 1030 | .11 / .87 / .02 |
| callout-k5 | 1 | 3.21 | −10.4 | −13.0 | −2.2 | 1450 | 1480 | .06 / .89 / .05 |
| callout-k7 | 1 | 2.80 | −9.3 | −13.0 | −1.4 | 450 | 1130 | .37 / .55 / .07 |

"Lên đỉnh" tính từ lúc đường bao vượt −20 dB dưới đỉnh tới đỉnh; với release-k5, k7 và world-open, đỉnh nằm cuối file nên số này là độ dài phần dâng.

Lab (`src/lab/sound.ts`): ba bus combat 0.8, voice 0.95, world 0.85; duck bằng gain; **không có ConvolverNode, không có send vang** (grep "reverb/convolver" trống). Không thấy quyết định "chọn bản vang" nào đang chờ trong `docs/HANDOFF_CURRENT.md` (grep "reverb" trống).

## 2. So với quy tắc (chỉ số, chưa nghe)

| Quy tắc | Kết quả đo | Mức |
|---|---|---|
| Bậc to §5.4: trúng T3 −20 tới −16 | Sáu impact ở −10.1 tới −11.2, **to hơn mục tiêu 5–6 LU**, ngang ultimate | P0 |
| Ultimate T6 −10 tới −8, to nhất | world-climax (Kim) −10.6, world-open −11.9: dưới T6. release-k7 và release-guard −7.6, k5 −8.5: **to hơn cao trào ultimate** | P0, thứ bậc ngược |
| Chiêu ô thường T4 −15 tới −12 | k1/k2 −10.2, k4 −9.6: ở mức T5–T6. dash −14.2, auto −15.0 trong T4 | P1 |
| Phát nhanh (anh 03/11: chiêu ra ngay) | release-k5 dâng 2.1 s, release-k7 1.8 s trước đỉnh; phần còn lại 0.1–0.5 s | P0 cho k5, k7 |
| Tắt chậm (anh 03/11) | release-k5 đuôi −40 dB chỉ 470 ms sau đỉnh (cắt cụt); k7 977 ms. Đuôi dài đúng: world-* 2.3–4.0 s, k4 2.7 s, k7-fire 2.6 s | P1 |
| Bốn lớp (sweet / impact / body / tail) | Tối đa 3 lớp; 7 sự kiện chỉ 1 lớp (cast, auto, dash, flyby, flyby-fire, ba callout đơn). Chỉ k4 và climax có lớp sub (`common-sub`); chỉ world-close có lớp đuôi riêng (`sword-tail`) | P0 |
| Lớp lấp lánh (sweet, glint) theo luật "chiêu phải lấp lánh" | Bản Lửa có năng lượng > 4 kHz 0.00–0.02; mọi bản Lửa 92–96 % dưới 250 Hz. Không có lớp glint nào trong SOURCES | P0 cho Lửa |
| Send vang §5.8 | Không có trong lab; chỉ đuôi nướng sẵn | P1 |
| True peak ≤ −1 dBTP | Đạt hết (−1.0 tới −9.7) | Đạt |
| Hit confirm, mass-kill §5.3 | Không có tick xác nhận trúng riêng; không có lớp mass-kill; không có voice cap theo nhóm trong lab [INFERENCE từ đọc lướt] | P1 |
| Cut-in ultimate | Không có sự kiện cut-in nào trong lab | P0 |
| Callout | Có hey/ha, k2, guard, k4, k5, k7 (một giọng Firefly "brittney"). **Thiếu k1, dash, auto, ultimate world-open** | P1 |
| Nguồn | SOURCES ghi tạm thời, chưa duyệt; cần kiểm điều khoản Firefly Adobe model cho từng take | Chờ |

## 3. Thiếu theo từng chiêu

- **Đánh thường (auto):** 1 lớp, mom. −15.0, 64 % năng lượng trên 4 kHz. Cần lớp body và low punch; giữ ở T2–T3 vì phát nhiều. Chưa có bản Lửa.
- **Ô 1 (k1):** Kim 2 lớp to cỡ T5. Lửa (−13.5) gần như chỉ có dải trầm, không có tia sáng. Thiếu callout. Thiếu lớp đuôi.
- **Ô 2 (k2, sẽ thành Song Long):** 3 lớp nhưng chưa có lớp đuôi, chưa có bản Lửa. Toàn bộ nhịp Song Long chưa có file (mục 4).
- **Ô 3 (guard):** −7.6, to nhất cùng k7; dải trầm 0 % (chuông và hào quang). Cần hạ về T4 và thêm thân trầm nhẹ. Chưa có bản Lửa.
- **Ô 6 (dash):** 1 lớp, chưa callout, chưa bản Lửa.
- **Ô 4 (k4):** 3 lớp, có sub, đuôi 2.7 s. Hạ về T4–T5; thiếu lớp lấp lánh; chưa bản Lửa.
- **Ô 5 (k5):** dâng 2.1 s rồi đuôi bị cắt. Cần đổi sang tấn công tức thì, đỉnh giữ, đuôi 1.5–2.5 s. Chưa bản Lửa.
- **Ô 7 / ultimate (k7 + world-*):** release-k7 dâng 1.8 s và to hơn cao trào. world-climax cần lên T6 (−9 ± 1) và là đỉnh duy nhất cả trận; world-open cần lớp "pre-verb swell" ngắn và một cú bật rõ. Thiếu cut-in (whoosh vào, đánh khung, đuôi chuông), thiếu callout ultimate riêng.
- **Trúng / hạ quái:** sáu impact quá to (T5 thay vì T3); chưa có tick xác nhận, chưa có lớp mass-kill, death chưa có đuôi đồng/chuông cho quái lớn (elite §5.3).
- **Lửa (mọi sự kiện):** thiếu dải cao (tiếng lách tách sáng, ember ticks, shimmer); release-k1-fire và flyby-fire nhỏ hơn bản Kim. Chỉ có Lửa cho k1, k7, flyby, impact, death, world.
- **Callout:** thiếu k1, dash, ultimate, Song Long. Ngôn ngữ: luật AGENTS.md nói chữ người chơi đọc là tiếng Anh; DRAGON_SKILL gợi ý câu Hán "双龙——夺珠！". **Cần anh chọn** tiếng Anh hay giữ câu Hán cho tiếng hô.

## 4. Song Long (Twin Dragons, ô 2) cần gì

Theo `DRAGON_SKILL.md` §3 A (chiêu đang thiết kế lại thành phủ cả sân, nhịp âm giữ nguyên). Không file nào trong lab hiện có làm được các nhịp này (không có tiếng rồng gầm, chuông đồng cao, chuông lớn Bồ Lao).

| Khung | Nhịp | Lớp cần làm | Bậc |
|---|---|---|---|
| F0 | kiếm nứt sáng + chuông đồng cao | glint crack, bronze bell hit cao, body chém, sub ngắn | T4 |
| F3 | hai tiếng vút lửa trái và phải | fire whoosh ×2 (hai take khác nhau để pan ±0.8), flame flutter | T3–T4 |
| F43 | lặng | pre-duck nhạc 60–90 ms (không hạ tiếng gõ) | — |
| F47 | hai tiếng gầm stereo | dragon roar ×2 (anime, không thú thật), lớp rumble trầm | T5 |
| F51 | chuông Bồ Lao lớn + nổ trầm + đuôi vang núi ~3 s | giant bell strike, low boom, sub 30–50 Hz, mountain echo tail 3 s, glint shimmer | T6 (cao trào duy nhất của chiêu, nhưng phải dưới world-climax nếu ultimate là T6 đỉnh) |
| F65–F300 | dư âm lửa lách tách lấp lánh | ember crackle tail 2–4 s, sparkle ticks | T3 |
| — | tiếng hô | callout (chờ chọn ngôn ngữ) | voice |

## 5. Cần tai anh (không đo được)

1. Chất âm từng lớp: có "chiến đấu, bùng nổ, vang" như anh muốn không; Kim có ra kiếm khí sắc hay rỗng.
2. Giọng callout "brittney": hợp nhân vật không; phát âm.
3. Sau khi hạ impact 5–6 LU và nâng climax: thứ bậc có đúng cảm giác không.
4. Ngôn ngữ tiếng hô Song Long.
5. Duyệt từng mẫu trước khi nối vào lab (luật "anh duyệt mọi mẫu").

## 6. Brief cho luồng âm thanh tiếp theo (dán thẳng vào ChatGPT, theo double-review.md §1)

```text
Role: you are the analyst for a game project. Research, analyse and propose a concrete solution.

Goal: plan the next sound workstream for "Tu Tien" (a browser typing game, three.js + Web Audio, anime/donghua xianxia sword arts, elements Metal and Fire). Every skill and combat sound must become layered, loud by tier, explosive and reverberant, with fast attack and slow decay, and the Twin Dragons skill needs its full sound set. Output: what to make in Adobe Firefly Sound Effects (one prompt per layer), the layer recipe per event, loudness targets per tier, the processing chain, and the acceptance checks.

Facts and current state (measured 04/11/2026 with ffmpeg ebur128; nobody has listened):
- 34 lab events, 91 files, 1-3 layers each, all from one Firefly batch (03/11), marked provisional, not owner-approved. The game itself still plays nothing (silent catalogue).
- Momentary max (LUFS, 400 ms): six impact events (flesh/stone/spirit, Metal and Fire) sit at -10.1 to -11.2, i.e. 5-6 LU above the hit tier. Skill releases: k1 -10.2, k2 -10.2, k4 -9.6, k5 -8.5, k7 -7.6, guard -7.6, dash -14.2, auto -15.0. Ultimate: world-open -11.9, world-climax -10.6 (Metal) / -8.8 (Fire), world-close -10.2. So a normal skill (k7, guard) is louder than the ultimate climax: the hierarchy is inverted.
- Attack: release-k5 rises for 2.1 s and release-k7 for 1.8 s before the peak; the owner wants instant casts. release-k5 then dies within 0.47 s of its peak (to -40 dB); the owner wants the peak held and a slow burn-down.
- Spectrum: every Fire event has 92-96 % of its energy below 250 Hz and 0-2 % above 4 kHz: no crackle, glint or shimmer layer. The owner requires every skill phase to "sparkle" (glints, star twinkles, fine light motes) in sound as well as in VFX.
- Layers: max 3; seven events have one layer. Only two events have a sub layer, one has a dedicated tail layer. No hit-confirm tick, no mass-kill layer, no ultimate cut-in sound, no in-game reverb send (only baked tails). True peak is fine everywhere (<= -1.0 dBTP).
- Callouts exist for k2, guard, k4, k5, k7 and a generic hey/ha (one Firefly voice); missing for k1, dash, ultimate and Twin Dragons.
- Twin Dragons (slot 2, being redesigned as field-wide; sound beats stay): F0 bright sword crack + high bronze bell; F3 two fire whooshes running left and right; F43 silence (music pre-duck 60-90 ms, typing never ducked); F47 two stereo dragon roars; F51 a huge temple bell in the style of the Pulao bell-dragon, a deep boom and a ~3 s mountain echo tail; aftermath sparkling fire crackle; a shouted callout. None of these exist yet.

Project rules (from the repo's audio rules, game-art-pipeline audio.md §5):
- Tiers by momentary max: T2 rapid -19..-17; T3 hits and swarm kills -20..-16; T4 skill releases, elite kills -15..-12; T5 explosions, big kills, boss hits -12..-9; T6 ultimate, boss death -10..-8 (rare, ducks the rest). Louder tiers come from more layers, not only gain. Reach T5-T6 at -1 dBTP with a soft clip before the limiter.
- Layer start offsets: head 0, body +2..5 ms, sub +4..8 ms. Big events: pre-verb swell, crack, body, sub drop, long tail 2-3 s. Hit confirm: bright tonal tick 25-90 ms plus a short body; gather hits within ~38 ms. Swarm kill: crunch plus low thump 100-220 ms, max 3-4 at once, a mass-kill layer past 6 kills in 100 ms.
- Reverb: baked tail per sound plus one shared in-game send: pre-delay 20-30 ms, high-pass 150-250 Hz, ConvolverNode, low-pass 6-7 kHz. Send levels: hit 0.05, swarm kill 0.1, skill/heavy 0.2-0.3, explosion/big kill 0.35-0.45, keys/UI 0.
- Keyboard rules (soft, short, dry) apply only to keys and UI, never to combat.
- Style: cinematic, magical, anime/donghua and myth; never realism as the goal; never small, quiet or plain. Fast attack, hold the peak, slow decay; never a quick fade.

Constraints:
- Sources: Adobe Firefly Sound Effects with the Adobe model only (no partner models), generated by hand in the owner's browser; real files only, no synthesized placeholders; no ripped game or film audio. No heavy local AI.
- Prompts: short, concrete, one sound per prompt (no "followed by" chains); never words like small, quiet, faint, gentle, soft, restrained, compact.
- 3-5 takes per layer for heads and bodies; confirms nearly fixed so players learn them.
- Each sample goes to the owner for listening before it is wired; acceptance needs two blind judges >= 8.5 in the built play host.
- Mac mini M4; processing with ffmpeg or the repo's Audio Lab.

Already decided by the owner (do not reopen): layered loud reverberant combat; per-skill sound plus callouts; Firefly Adobe model only; instant casts; slow decay; skills must sparkle; English for everything the player reads.

Taste: anime/donghua xianxia, radiant, luxurious, explosive, captivating; Metal = sharp qi-blade edge with a bright ring, not a hollow fantasy chime; Fire = hot rushing body with bright crackle and ember glitter, not white noise plus boom.

Deliver:
1) analysis of the problem and its causes;
2) the solution as ordered steps with the reason for each: (a) a per-event table for auto, k1, k2 (= Twin Dragons), guard, dash, k4, k5, k7, ultimate open/climax/close, cut-in, hit confirm per material, swarm kill, mass kill, elite kill, flyby, each with tier, momentary target, layers (sweet/glint, impact/head, body, sub, tail), start offsets, lengths, reverb send; Metal and Fire variants; (b) one Firefly prompt per layer, in English, at most ~25 words each, 3-5 take directions where useful; (c) the Twin Dragons cue sheet by frame (F0, F3, F43, F47, F51, aftermath) with stereo placement and ducking; (d) callout lines for missing slots (English, short, shouted); (e) the processing chain per layer (trim, fade, EQ, transient, saturation, soft clip, limiter) and the normalisation per tier;
3) risks and how to check each (masking, fatigue in long play, inverted hierarchy, Fire mud below 250 Hz, Web Audio compressor makeup gain);
4) acceptance checks with numbers: momentary max per tier +-1 LU, true peak <= -1 dBTP, attack to peak <= 30 ms for releases and impacts, tail to -40 dB >= 1.5 s for T4+, >= 2.5 s for T6, high-band share > 4 kHz >= 8 % for Fire and Metal skills, the ultimate climax the loudest event in a capture;
5) what you are not sure about.
Cite a source for every factual claim.
If you need clarifications, ask all of them in one message before you start.
```

Sau bản trả lời: chạy hai lượt tự duyệt liên tiếp (double-review.md §2), lấy handoff §2b, chuyển sang Gemini cùng brief, rồi gộp kế hoạch theo luật "Plan with ChatGPT and Gemini" của AGENTS.md trước khi tạo bất kỳ file nào.

## 7. Cách kiểm sau khi làm

- Chạy lại bộ đo này trên file mới; so cột mom. max với bậc, cột lên đỉnh (≤ 30 ms cho release và impact), đuôi −40 dB (≥ 1.5 s từ T4, ≥ 2.5 s ở T6), dải > 4 kHz (≥ 8 % cho chiêu Kim và Lửa).
- Ghi lại cảnh lab bằng `__lab.soundRecord()` và `scripts/visual/mix-lab-sound.mjs`; đo momentary trên bản trộn để chắc climax là đỉnh to nhất.
- Gửi anh từng mẫu; hai giám khảo mù ≥ 8.5 trong bản chơi.
