# Quyết định của Audio Lab

Sổ này ghi những quyết định đã chốt cho Audio Lab: nguồn của quyết định, bằng chứng bằng số, việc đã làm trong `tools/audio-lab` và việc còn lại. Sổ không thay kế hoạch [`AUDIO_PIPELINE.md`](../../docs/games/AUDIO_PIPELINE.md). Người điều phối đưa từng mục vào kế hoạch; khi đó mục được ghi thêm "đã vào kế hoạch".

---

## Dữ liệu chủ dự án, 23–24/10/2026

Điểm chấm mù trên Bảng Nghe, các bản trong một id đã cân cùng độ to. Lượt chấm ghi lúc 21:16–23:52 ngày 23/10/2026; Claude đọc, so với máy và chốt ngày 24/10/2026.

| Lô | Id | Bản | Thời gian chấm | Nguồn âm |
|---|---|---|---|---|
| 0a | 13 (3 id hiệu chỉnh `calib-*`) | 35 | 12,8 phút | Kenney, VCSL, VSCO-2-CE, tổng hợp, bộ phát mẫu |
| 0b vòng 2 | 6 | 15 | 2,9 phút | Stable Audio 3 (thô hoặc trong công thức ghép lớp) |

- **Điểm cao nhất:** phần lớn id 3/5 ("dùng được nếu sửa nhẹ"). Ba id 4/5: `leak`, `gun.xung` (0a), `calib-3`; thêm `amb.forest` (0b) 4/5. Không bản nào 5/5.
- **Bản dò:** ở cả 6 id có bản dò (bản máy xếp ở nửa dưới), anh đều chọn bản dò: 4/4 id ở 0a (`calib-3`, `fire.impact.a`, `word-hit`, `hit.t2`) và 2/2 ở 0b (`amb.forest`, `hit.t1`). Bản máy xếp đầu được chọn ở 8/19 id.
- **Ghi chú duy nhất** (`calib-1`, một tiếng trúng tổng hợp anh nghe ở bối cảnh Lặp): "âm thanh chưa đạt, cảm giác không liên thanh, ngắt quãng, thiếu đi sự liên tục, lực trong chiến đấu". Anh vẫn chọn bản "mỏng" của id này (3/5).
- **Giới hạn của dữ liệu** (đọc kèm mọi quyết định bên dưới):
  - Mọi lượt chấm ghi thiết bị **loa**, không có lượt nào bằng tai nghe. Phần dưới 150 Hz có thể nghe thiếu.
  - Lô 0b chỉ mất 2,9 phút cho 15 bản; nhiều bản chỉ được phát một lần.
  - `amb.forest` chỉ được nghe ở bối cảnh "Một mình" (một vòng 6 s), chưa nghe "Lặp" 3 vòng như hướng dẫn.
  - Không có cặp mốc chấm lại, nên chưa đo được độ nhất quán (mục 4.6 bước 6).
  - Không có nhãn "rè/lỗi" nào, nên chưa có gì để chỉnh bộ dò L1b. Phần thêm `0a-them` (8 nhóm hiệu chỉnh) chưa được chấm.

---

## Q1. Stable Audio 3 dùng tiếp: điều kiện đi tiếp của mục 9 đã đạt

**Nguồn:** dữ liệu chủ dự án, 23–24/10/2026.

- Điều kiện của chủ dự án (mục 9): ít nhất 3/6 id có một bản từ 3/5. **Kết quả: 6/6 id.**

  | Id | Bản tốt nhất | Sao |
  |---|---|---|
  | `amb.forest` | Stable Audio 3 thô, prompt E (sáng, lá kim), seed 2006 | 4/5 |
  | `enemy.quadruped.howl` | Stable Audio 3 thô, tiếng tru trọn, prompt B, seed 1004 | 3/5 |
  | `fire.impact.a` | Công thức: đầu Kenney Impact, thân lửa Stable Audio 3, sub ngắn (v2 và v4 bằng nhau) | 3/5 |
  | `call-chop` | Stable Audio 3 thô, gõ trầm (A s1006 và E s2003 bằng nhau) | 3/5 |
  | `hit.t1` | Stable Audio 3 thô, không ghép lớp (C s1006) | 3/5 |
  | `gun.xung` | Công thức: khóa nòng Kenney, thân Stable Audio 3 lọc thấp 1,5 kHz, sub tổng hợp (v1 và v3 bằng nhau) | 3/5 |

- Ba điều kiện máy (tốc độ, RAM, số bản qua cổng vệ sinh) đã đạt ở vòng 1 (`~/AudioLab/review/batch-0b/README.md`).
- **Hệ quả cho lô 1:** Stable Audio 3 là nguồn chính cho lửa, nổ, nền và quái như mục 3.2.
  - Công thức `fire.impact.a` và `gun.xung` (đều 3/5) thành mẫu cho họ của chúng (`fire.impact.b`, `fire.impact.c`; các tiếng súng).
  - **`hit.t1`: bản Stable Audio 3 nguyên khối thắng hai công thức có thân dày** (3/5 so với 2/5 và 2/5). Công thức thân dày không thành mẫu cho `hit.t2`, `hit.t4`. Lô 1 thử Stable Audio 3 nguyên khối có chọn cửa sổ đầu tiếng, thân vừa phải (10–35 % năng lượng ở 200–800 Hz). Mục 3.2 ("Va chạm, trúng": hạng 1 là ghép lớp) cần người điều phối xem lại cho tiếng trúng thép nhỏ.
  - `gun.xung` ở 0a (tổng hợp và khóa nòng Kenney, không có Stable Audio 3) được 4/5, cao hơn công thức 0b (3/5). Hai lô ở hai phiên khác nhau nên không so trực tiếp được; lô 1 nên đặt hai hướng này cạnh nhau trong một phiên.
  - Ghi chú của `calib-1` ("không liên thanh, ngắt quãng, thiếu lực") hợp với `gun.xung` phát 5 lần mỗi giây: mỗi phát gọn có thể nghe rời rạc khi lặp. Lô 1 thử thêm một đuôi ngắn dùng chung (`hit.tail`, mục 6.3) để chuỗi phát nối thành loạt, và chấm ở bối cảnh Lặp.

---

## Q2. Cấm prompt kiểu mõ cho Lời Gọi (TK 22.1)

**Nguồn:** dữ liệu chủ dự án, 23–24/10/2026.

- **Bằng chứng (`call-chop`, 0b):** bản đối chứng B s1002 (tiếng "tốc" rỗng, cao: 2,5 % năng lượng dưới 300 Hz, trọng tâm phổ 3,7 kHz) được **2/5**, thấp nhất id. Hai bản gõ trầm A s1006 và E s2003 (79 % và 55 % dưới 300 Hz) được 3/5. Anh không gắn nhãn "sai chất liệu"; điểm thấp nhất cộng luật TK 22.1 (không mõ chùa) là đủ để cấm.
- **Quyết định:** với mọi lời gọi (`call-*`) và UI của Lời Gọi, không dùng prompt cho ra tiếng gõ rỗng, cao, có cao độ:
  - không dùng prompt B ("a single hollow knock on a large bamboo stalk…") và prompt D ("hollow bamboo tube, low resonant tok") của thẻ `call-chop`;
  - không viết prompt mới có "tok", "tốc", "hollow tube", "temple block", "wooden fish", "mõ".
- **Hướng:** gõ trầm, chắc (prompt A và E–G của thẻ `call-chop`).
- **Đã làm:** luật L2 `t-call-chop-knock` của bản hiệu chỉnh 1 phạt bản `call-chop` có dưới 30 % năng lượng ở dưới 300 Hz. Ở 0b, máy cũ xếp bản mõ thứ 5/41, trên cả hai bản anh chọn; nay bản anh chọn đứng 1/41.
- **Chưa làm:** thẻ spec vẫn giữ prompt B và D để tạo lại đúng ứng viên lô 0b. `gen.sa3` chưa có bước chặn prompt cấm; đề xuất thêm bước đó trước lô 1c.

---

## Q3. Nới luật đầu tiếng của sinh vật cho tiếng gọi trọn

**Nguồn:** dữ liệu chủ dự án, 23–24/10/2026.

- **Bằng chứng (`enemy.quadruped.howl`, 0b):** cả hai bản là tiếng tru trọn, đều bị luật L1 "lên ≤ 30 ms" (mục 4.3.1) chặn. Bản B s1004 (lên 138,5 ms) được **3/5**, cao nhất id. Bản A s1001 (lên 106,5 ms) được 2/5.
- Máy gắn cờ "rít cao" (`hf_hiss`) ở cả hai bản; anh không gắn "rè/lỗi".
- **Quyết định:** tiếng gọi trọn (tru, gầm dài từ khoảng 0,8 s: `enemy.*.howl`, `dragon.roar`) được lớn dần tới **150 ms**. Con số này là đề xuất ở `SESSION_0B.md`; bản 138,5 ms nằm trong đó. Tiếng sinh vật ngắn (`*.spawn`, `dragon.hurt`) giữ ≤ 30 ms.
- **Đã làm:** luật L2 `t-creature-whole-call` (mục tiêu lên ≤ 150 ms, hết điểm ở 300 ms) cho nhóm `creature` có id chứa `howl` hoặc `roar`.
- **Chưa làm, có chủ ý:** cổng L1 vẫn 30 ms, vì bản hiệu chỉnh không được đụng L1. Khi người điều phối sửa mục 4.3.1, thẻ spec của các id gọi trọn đặt `critic.attack_max_ms: 150` (ghi vào `manual_fields`). Không cần sửa mã bộ chấm.

---

## Q4. Hiệu chỉnh bộ chấm, bản 1 (`critic/calibration/owner-v1.json`)

**Nguồn:** dữ liệu chủ dự án, 23–24/10/2026 (19 id, 50 bản, 37 cặp sao khác nhau). Báo cáo đầy đủ: `~/AudioLab/work/_calibration/owner-v1.md` (lệnh `bash tools/audio-lab/run.sh critic agreement`).

### Máy đã khớp tai anh tới đâu (trước hiệu chỉnh)

| Lớp | Cặp khớp | Bản đầu của máy là bản anh chọn |
|---|---|---|
| Điểm tổng | 13/37 (35 %) | 6,5/19 |
| L2 đặc trưng | 15/37 (41 %) | 7,2/19 |
| L3 audiobox | 14/37 (38 %) | 7/19 |
| L4 CLAP/AST | 19/37 (51 %) | 7,2/19 |

Đoán ngẫu nhiên khớp khoảng 50 % số cặp. Điểm tổng thấp hơn mức đó. Theo họ, audiobox khớp 0/4 cặp ở bắn, 0/3 ở thưởng, 3/8 ở phím và UI, 4/13 ở trúng, nhưng 6/7 ở nền.

### Đặc trưng tách bản được chấm cao

- **Trúng:** bản được chấm cao sáng hơn ở 10/13 cặp và ít năng lượng dưới 150 Hz hơn ở 8/12 cặp.
- **`hit.t1`:** crest cao hơn thắng ở cả hai lô.
- **`amb.forest`:** bản 4/5 có 54 % năng lượng trên 3 kHz, so với 2 % của bản 3/5.
- **Không tách:** thời gian lên (15/29 cặp), thân 200–800 Hz trên mọi họ (20/37).
- **Đuôi:** bản được chấm cao có đuôi ngắn hơn ở 23/36 cặp; số liệu chưa đủ để thành luật.

### Đã đổi

- **Trọng số (mục 4.5):** họ trúng, bắn, phím và UI, thưởng: L3 audiobox **0,3 → 0,1**, L2 **0,6 → 0,8**. L4 giữ 0,1. Họ bẩn vẫn 0 cho audiobox. Họ nền, nổ, sinh vật giữ trọng số kế hoạch.
- **Mục tiêu L2:**

  | Luật | Áp cho | Thay đổi |
  |---|---|---|
  | `t-amb-forest-bright` | nền rừng | Thưởng phần trên 3 kHz (từ 30 %); nới phần dưới 300 Hz và 4–10 kHz (từ 45 %); cho độ to dao động tới 7 dB |
  | `t-hit-small-steel` | `hit_small` của Tuyến Cuối | Thân 200–800 Hz thành khoảng 10–35 % (trước: càng nhiều càng tốt, từ 25 %); crest được thưởng dần từ 12 tới 20 dB |
  | `t-hit-boom` | `hit_heavy`, `hit_fire` | Phần dưới 150 Hz không quá 70 % (hết điểm ở 90 %) |
  | `t-creature-whole-call` | tiếng tru, gầm | Thời gian lên tới 150 ms không bị trừ (Q3) |
  | `t-call-chop-knock` | `call-chop` | Từ 30 % năng lượng dưới 300 Hz (Q2) |

- **Không đổi:** L1 và L1b. File hiệu chỉnh nào có khóa L1, L1b bị từ chối.

### Sau hiệu chỉnh (đo lại trên chính 19 id)

| Cấu hình | Cặp khớp, điểm tổng | Bản đầu là bản anh chọn |
|---|---|---|
| Kế hoạch | 13/37 (35 %) | 6,5/19 |
| Chỉ trọng số | 15/37 (41 %) | 7,5/19 |
| Chỉ mục tiêu L2 | 19/37 (51 %) | 8,5/19 |
| **Bản 1 (cả hai)** | **24/37 (65 %)** | **10,5/19** |

- Riêng L2 khớp 15/37 → 22/37.
- Hạng máy của bản anh chọn trong cả nhóm:
  - `amb.forest`: 38/47 → 4/47;
  - `hit.t1` 0b: 21/27 → 5/27;
  - `call-chop`: 11/41 → 1/41;
  - `hit.t2`: 4/4 → 2/4;
  - `fire.impact.a` 0a: 4/4 → 2/4.
- Không id nào tụt.
- **Còn sai:**
  - `ui-move` (0/3 cặp): anh chọn bản ít năng lượng 1–5 kHz nhất, trái mục tiêu UI;
  - `word-hit` (1/3): quãng tám là việc của thẻ spec, không phải của L2;
  - `calib-1`;
  - tiếng tru (L3 quyết, một cặp).
- **Đã thử rồi bỏ**, vì không thêm cặp khớp nào:
  - hạ L2 của họ nền (còn kéo hạng bản rừng anh chọn từ 4 xuống 7);
  - nới thời gian lên của `fire.impact`;
  - hạ trọng số 1–5 kHz của UI.
- **Đọc con số này thế nào:** 24/37 là số đo trên chính dữ liệu dùng để chọn luật, nên lạc quan. Mục 4.6 bước 7 không cho tuyên bố gì khi một họ có dưới 30 bản dò đã chấm. Phép thử thật là lô 1: chấm với bản 1 đang bật, rồi chạy `critic agreement --batch 1`. Luật `t-hit-boom` và `t-amb-forest-bright` cần được nghe lại bằng tai nghe.
- **Cách dùng:** `critic run` dùng bản mới nhất trong `critic/calibration/`. `--calibration none` trả về trọng số và mục tiêu gốc của kế hoạch. Kiểm thử của bộ chấm chạy không hiệu chỉnh, trừ `test_calibration.py`.

---

## Q5. Hướng âm theo id (lô 0a và 0b)

| Game | Id | Anh chọn | Sao | Bản thua |
|---|---|---|---|---|
| Rồng Giữ Ải | `amb.forest` | Gió rít qua lá kim, sáng (prompt E) | 4/5 | ù trầm H 3/5; G 2/5 |
| Rồng Giữ Ải | `wave.horn` | Hai kèn co Rê–La như tài liệu | 3/5 | kèn co trên trombone 2/5; trombone trầm 1/5 |
| Rồng Giữ Ải | `trap.pine-bomb.trigger` | Bản nứt gỗ Kenney Impact Plank (v3) | 3/5 | v2 2/5 |
| Lời Gọi | `word-hit` | Đàn tranh **C4** | 3/5 | C5 ngân rung 2/5; C5 1/5 |
| Lời Gọi | `leak` | **Kẻng sắt** VCSL Anvil, ba nhát | 4/5 | Cồng VCSL Gong 1 3/5 |
| Lời Gọi | `ui-pick` | Phách gỗ và VCSL Hand Chimes A5 | 3/5 | G5 2/5; C6 1/5 |
| Lời Gọi | `ui-move` | Trống khe VCSL Slit Drum | 3/5 | mõ gỗ click2 2/5; click3 1/5 |
| Tuyến Cuối | `hit.t2` | Bản ít sub hơn (v2) | 3/5 | v4 2/5; v1 nặng sub nhất 1/5 |

Các id Stable Audio 3 ở Q1. `calib-*` là âm làm hỏng có chủ ý; chúng chỉ dùng để so máy với tai, không chọn hướng.

---

## Q6. Âm theo hình dạng của hành động; bỏ hướng "bụp, thụp"

**Nguồn:** chủ dự án nói trong chat ngày 24/10/2026 (trên máy Dell). Ý chính:
- Không thêm âm quê mùa, lỗi thời kiểu "bụp", "thụp".
- Mỗi âm phải đạt đúng loại hành động của nó.
- Ví dụ: rồng khè lửa ra quả cầu thì âm phải mạnh mẽ, vang vọng, không như ném quả bóng bay rồi nghe "thụp" hay "bụp".

Quyết định này **thay** hướng "phụt tròn" đang ghi trong thẻ `fire.cast` (prompt A, C, D), `fire.impact.*` ("phụt trầm, thân tròn") và trong `SESSION_1_DH.md` phiên S2. Nó cũng thay âm tạm trong game ("noise over a sine thump", `games/dragon-hold/src/audio/synth.ts:6`).

**Luật cho mọi âm hành động của ba game** (đòn đánh, phép, súng, nổ, trúng, sinh vật):
1. **Có hình dạng theo hành động**, đủ bốn phần, trừ khi hành động thật sự không có phần đó:
   - chuẩn bị: hít vào, tụ lực, lên nòng;
   - phát: đầu tiếng có lực;
   - thân: lửa cháy, lực đẩy, vật bay;
   - đuôi: vang trong không gian của bản đồ (thung lũng, rừng thông, hành lang thép).
2. **Cỡ âm theo cỡ thứ phát ra âm.** Rồng, boss, đòn to phải nghe to xác và có trọng lượng. Quái nhỏ thì nhỏ.
3. **Bỏ hẳn các hướng sau**, trong prompt, công thức ghép lớp và âm tổng hợp tạm:
   - "puff", "pop", "balloon";
   - "thump" hay "thud" đứng một mình;
   - "soft round whoomph";
   - âm kiểu đồ chơi, hoạt hình, retro, 8-bit, chiptune;
   - một tiếng trầm ngắn không có thân và đuôi.
   Một lớp sub hoặc tiếng nổ đục chỉ được làm lớp dưới, có thân và đuôi đè lên.
4. **Vẫn giữ luật giọng đọc** (mục 6.2): năng lượng 1–4 kHz phải tắt nhanh. Đuôi vang nằm dưới 1 kHz hoặc trên 4 kHz và nhường giọng đọc.
   Âm phát sau mỗi từ (khoảng 1,5 s một lần) giữ đuôi thấp để lặp 20 lần không mệt. Đòn to (`fire.impact.c`, `dragon.skyfire.*`, `dragon.inferno`) được đuôi dài và to hơn rõ.

**Rồng khạc cầu lửa (`fire.cast`).** Ba lớp:
1. Tiếng khè hoặc gầm họng ngắn của một sinh vật lớn.
2. Tiếng lửa phụt ra dưới áp lực: bắt lửa, rồi tiếng lửa gầm.
3. Cầu lửa lao đi: whoosh dày, có chuyển động ra xa.

Đuôi vang của rừng núi dài khoảng 0,6–1,2 s ở mức thấp. Độ dài cũ 340 ms quá ngắn để có đuôi. Đề xuất: file 600–900 ms gồm cả vang sớm; bus `world` của game thêm vang chung cho đuôi dài.

**Cầu lửa trúng (`fire.impact.*`).** Lửa bùng nổ có thân, gồm ba phần: lửa bùng, tiếng nổ lách tách của than, mảnh văng. Có đuôi vang. Cấm nghe như "một cục rơi xuống". `.c` là đòn to: dài và nặng hơn rõ.

**Hệ quả cho lô 1:**
- Ứng viên hướng "phụt tròn" (`fire.cast` A, C; `fire.impact.a` "thân tròn") không còn là hướng được chọn.
- Phiên S2 vẫn chấm được để đo máy, nhưng lô 1c phải sinh lại họ lửa theo Q6.
- Các id cùng loại ở Lời Gọi (`arrow-fire`, `blast`, `wordshot-fire`) và Tuyến Cuối (súng, `hit.*`, `kill.*`) phải soát lại theo luật trên.

**Việc kéo theo:**
- Viết lại prompt, mục đích và độ dài trong thẻ spec, `docs/audio/*` và `src/audio/catalog.ts` của từng game.
- Đề xuất thêm một luật L2 cho bộ chấm: phạt âm hành động có đuôi quá ngắn, hoặc chỉ có một cú trầm không thân.
- Âm tổng hợp tạm trong game không được coi là âm thật. Âm thật về từ Audio Lab trên Mac sau phiên nghe của chủ dự án.

### Q6: đã làm trên máy Dell (24/10/2026)

Chi tiết từng id, độ dài và việc của lô 1c: [`Q6_REWRITE_2026-10-24.md`](Q6_REWRITE_2026-10-24.md).

- **Phân loại 149 thẻ.** 66 id là âm hành động. Còn lại: 25 UI và phím, 11 thưởng, 3 học, 18 báo nguy và stinger, 8 nền, 1 giọng, 9 nhạc, 8 foley không phải đòn đánh (đặt bẫy, dựng nhà, hồi máu, sửa tuyến).
- **Thẻ spec.**
  - 54 id viết lại theo bốn phần: purpose, prompt.text, prompt.variants, notes ("Q6 (24/10)"). Đường dẫn đã sửa ghi vào `manual_fields`.
  - 12 id soát và giữ thiết kế, chỉ bỏ biến thể có chữ cấm hoặc chữ phủ định:
    - ba tiếng lên đòn của quái;
    - các bậc trúng của Tuyến Cuối;
    - `gun.xung` và hai lớp loop, tail của nó;
    - `gun.tia.pulse`.
  - **Sai, đã sửa ở lượt sau review:** lượt này giữ các bậc trúng với lý do "đuôi là lớp dùng chung `hit.tail`, sub là `hit.sub`, do mã ghép". Mã game không ghép lớp nào: `theme-audio.ts` phát một tiếng cho mỗi bậc. Ba tiếng lên đòn cũng không có đuôi trong không gian (luật 1). Xem "Q6: sửa sau review" bên dưới.
  - Biến thể Q6 dùng khóa mới, không dùng lại khóa cũ, để tên ứng viên mới không trùng tên ứng viên lô 0b, lô 1. Chỉ giữ biến thể cũ đã hợp Q6, ví dụ howl B là bản anh chọn.
  - 4 id không phải âm hành động chỉ thay chữ cấm: `type.miss`, `ui.deny`, `trap.spikes.arm`, `key.bad`.
- **Danh sách âm của ba game** (`M0_SOUND_LIST.md`, hai `THEME_SOUND_LIST.md`) ghi cùng cảm giác, prompt và độ dài. Lệnh `specs generate --check` (mã thật của Audio Lab, chạy bằng Python hệ thống của máy Dell qua `common/launch.py`, không qua `pnpm` hay venv) cho 149/149 thẻ có sẵn "giữ nguyên", mã thoát 1 vì 14 id S1 của Tuyến Cuối chưa có thẻ (có từ trước).
- **Độ dài.**
  - `fire.cast` 340 → 750 ms: 750 ± 20 % đúng bằng khoảng 600–900 ms của đề xuất trên, **đã chọn theo đề xuất**.
  - Đòn to và họ lửa dài hơn trong `catalog.ts` của Rồng Giữ Ải.
  - Bốn id của Lời Gọi và hai id của Tuyến Cuối dài hơn trong prompt của danh sách.
- **Chưa làm ở lượt này** (hai việc đầu đã làm ở lượt sau review):
  - âm tổng hợp tạm trong game (`synth.ts` "sine thump") là mã game, không thuộc làn này;
  - bước chặn chữ cấm Q6 trong `gen.sa3`;
  - luật L2 dưới đây.

### Q6: sửa sau review (24/10/2026, máy Dell)

Review của lượt trên tìm ra 1 lỗi lớn, một số lỗi nhỏ và 1 việc còn mở. Chi tiết từng id: [`Q6_REWRITE_2026-10-24.md`](Q6_REWRITE_2026-10-24.md) mục 9.

- **Bậc trúng Tuyến Cuối viết lại theo Q6.** `hit.t1`, `hit.t2`, `hit.t4`: đầu tiếng giòn, thân thép, lớp trầm chỉ ở dưới, đuôi hành lang thép ngắn dưới 1 kHz, nằm trong file.
  - `hit.t1` 80 → 140 ms: vẫn theo hướng anh chọn (Stable Audio 3 nguyên khối, crest cao, thân vừa, Q1); đuôi ngắn nối các phát thành loạt (ghi chú `calib-1`).
  - `hit.t2` 160 → 260 ms: ít sub như bản anh chọn ở 0a (Q5).
  - `hit.t4` giữ 900 ms.
  - Ghi chú của `hit.sub`, `hit.tail`, `gun.xung`, `gun.xung.tail` nay nói rõ: các lớp dùng chung mới là đề xuất (mục 6.3 #3, 16 #6 còn mở); Audio Lab có ghép thì ghép sẵn vào file.
- **Chữ cấm còn sót.** "thump", "thud" đứng riêng ở `dragon.low`, `unit.warden.place`, `enemy.quadruped.march` (D), `call-chop` (F), `gun.xung` (B, D, H), `hit.t2`, `hit.t4`: đã sửa từng chỗ. Còn lại có chủ ý, ghi trong ghi chú của thẻ:
  - `call-chop` A, E: hai prompt anh chấm 3/5, Q2 gọi tên; "thud" nằm sau tiếng gõ có dăm tre lách tách;
  - `gun.xung` E: prompt thân của công thức lô 1, công thức ghép sẵn lớp đuôi.
- **Tiếng lên đòn của quái** (ba `*.windup`) thêm vang rừng thông ngắn.
- **`critic.loop_eval` bật lại** cho `gun.xung` (5 lần mỗi giây) và `wordshot-fire` (sau mỗi từ), giữ bằng `manual_fields`. Bộ sinh đã tắt nó khi prompt dài từ 300 ms. Bộ chấm không đọc khóa này: nó tự lặp 3–4 s các file dưới 300 ms (`critic/learned.py`).
- **`gen.sa3.FORBIDDEN_TERMS`** chặn chữ cấm Q6 cho cả ba game: puff, pop, balloon, whoomph, boing, bonk, toy, cartoon, retro, 8-bit, chiptune, bụp, thụp. Test: `gen/tests/test_sa3_q6.py`. "thump", "thud" không vào danh sách vì cần ngữ cảnh. `numpy` chuyển vào trong hàm của `sa3.py`, để bước dựng job và chặn chữ chạy được mà không cần bộ âm.
- **Bộ giới hạn tiếng của Rồng Giữ Ải** (đã chọn theo đề xuất): `lengthMs` giữ là đích của file thật. `synthMs` mới ghi độ dài âm tạm của 9 id dài ra ở Q6. Bộ giới hạn giữ chỗ theo độ dài thật của thứ đang phát (`VoiceLimiter.settle`): âm tạm, hoặc file khi có. Lời Gọi, Tuyến Cuối không đổi: mã của hai game không đọc độ dài trong danh sách âm.
- **Đuôi prompt chung của Lời Gọi** viết lại không có chữ phủ định. Hai gói prompt `04-audio.md`, `04-audio-vs.md` viết lại theo Q6: dòng SPACE cho âm hành động, mọi chữ cấm sửa theo ngữ cảnh.
- **Kiểm đã chạy trên máy Dell** (WSL, Python hệ thống 3.12, PyYAML 6.0.1, jsonschema 4.10.3; không venv, không pytest thật): ghi đúng ở mục 9 của `Q6_REWRITE`.

### Q6: đề xuất luật L2 cho bộ chấm (chưa làm trong mã)

**Mục đích:** phạt âm hành động có đuôi quá ngắn, hoặc chỉ là một cú trầm không thân.

**Đặc trưng dùng lại**, đều đã có trong `critic/features.py`, không cần đo mới:

| Đặc trưng | Đo gì |
|---|---|
| `tail_ms` | Từ khung to nhất tới khung cuối còn trên −60 dB so với đỉnh (đường bao 1 ms) |
| `punch_db` | Mức 20 ms đầu trừ mức 100–300 ms sau đầu tiếng (trần 40 dB). Cú trầm rồi tắt cho số rất lớn; âm có thân cho số vừa |
| `share_150_800` | Phần năng lượng ở thân 150–800 Hz |
| `share_below_150` | Phần năng lượng dưới 150 Hz |
| `sub_len_ms` | Độ dài lớp 40–90 Hz trong khoảng 20 dB dưới đỉnh của chính nó |

**Luật đề xuất**, viết theo dạng file hiệu chỉnh `critic/calibration/owner-v2.json`. Mọi con số là điểm xuất phát, **chưa đo trên file nào**:

| Id luật | Áp cho | Mục tiêu (good / bad) | Ghi chú tiếng Việt khi trượt |
|---|---|---|---|
| `t-q6-tail-cast` | id `^fire\.cast$` (nhóm thưởng) | `tail_ms` ≥ 300 / ≤ 120 | đuôi quá ngắn, chưa có vang thung lũng |
| `t-q6-tail-fire` | nhóm `hit_fire` | `tail_ms` ≥ 250 / ≤ 100 | đuôi quá ngắn, nghe như một cục rơi xuống |
| `t-q6-tail-heavy` | nhóm `hit_heavy`, id `^(impact\.multi\|general\.g01\.attack\|enemy\.quadruped\.charge\|trap\.spikes\.trigger\|hurt\.hull)$` | `tail_ms` ≥ 200 / ≤ 80 | đuôi quá ngắn |
| `t-q6-tail-blast` | nhóm `explosion` | `tail_ms` ≥ 500 / ≤ 200 | nổ không có đuôi vang |
| `t-q6-lone-low` | họ `trung`, `no`, `ban`, `chet` của Rồng Giữ Ải và Lời Gọi; id `^(kill\|hurt\|foe)\.` của Tuyến Cuối | `punch_db` trong [6, 20] / ngoài [0, 32]; `share_150_800` ≥ 0,12 / ≤ 0,03 | một cú trầm rồi tắt, không có thân |

- **Phạm vi của luật trầm đứng riêng** (sửa sau review): không áp cho `gun.xung` (5 phát mỗi giây, mỗi phát ngắn). Các bậc trúng của Tuyến Cuối nay tự có thân và đuôi trong file (mã không ghép lớp), nên chúng cần luật đuôi riêng theo cỡ: `t-q6-tail-tier`, id `^hit\.t[12]$`, `tail_ms` ≥ 60 / ≤ 25 cho T1 và ≥ 120 / ≤ 50 cho T2 (hai luật, hai id).
- **Hai chỗ hở khi làm thật** (review, 24/10):
  1. **Khóa `match` của một luật là "và", không phải "hoặc"** (`critic/calibration.py` › `_match`). Các hàng ghi "nhóm X, id Y" hay "họ của game A; id của game B" phải tách thành nhiều luật, mỗi luật một id. Viết gộp thì `t-q6-tail-heavy` chỉ khớp các id vừa thuộc `hit_heavy` vừa khớp regex. Còn nếu chỉ ghi `group: hit_heavy` thì luật trúng cả `hit.t2` và `hit.t4` của Tuyến Cuối, với ngưỡng không hợp cỡ của chúng. Cách làm: `t-q6-tail-heavy-g` (`group: hit_heavy`, `game: dragon-hold`), `t-q6-tail-heavy-id` (chỉ `id`), `t-q6-lone-low-dh` (`family`, `game: dragon-hold`), `t-q6-lone-low-td` (`family`, `game: typing-defense`), `t-q6-lone-low-ts` (`id`, `game: typing-survival`).
  2. **`punch_db` đo mức 100–300 ms sau đầu tiếng** (`critic/features.py` › `dynamics`). File dưới 100 ms không có số (luật bỏ qua). File 140–300 ms thì cửa sổ đó là cuối đoạn tắt, nên một tiếng trúng giòn, gọn cũng ra `punch_db` lớn và bị đọc nhầm là "cú trầm không thân". Luật trầm đứng riêng chỉ áp cho id có thẻ dài từ 400 ms (ghi bằng regex id, vì file hiệu chỉnh không khớp theo độ dài). Hoặc thêm một đặc trưng có cửa sổ theo độ dài file (cần mã, làn Critic).
- **Cách chồng lên mục tiêu cũ:** `set` của `punch_db` thay mục tiêu `PUNCH` (≥ 6 dB) cho các nhóm khớp, nên cận dưới vẫn còn. Luật nhóm `t-hit-boom` (dưới 150 Hz không quá 70 %) và giới hạn `sub_len_ms` (≤ 150 ms ở trúng, ≤ 300 ms ở nổ) giữ nguyên, hợp với luật Q6 "sub chỉ làm lớp dưới".
- **Thêm một cờ (cần mã, nhỏ):** `lone_low_hit` khi đồng thời có `share_below_150` ≥ 0,6, `tail_ms` < 150 và `punch_db` ≥ 25. Ghi chú: "một cú trầm không thân, không đuôi (Q6)". Cờ chỉ hiện trên thẻ ảnh và danh sách nghe, không chặn. File hiệu chỉnh không biểu diễn được điều kiện "và", nên cần cờ này.
- **Đi kèm:** khi làm luật này, sửa ghi chú "phụt lửa trầm, thân tròn" của nhóm `hit_fire` ở `critic/groups.py` và lý do ở `specs/taxonomy.CRITIC_GROUP_BY_ID`. Thẻ spec không đổi vì chỉ đọc tên nhóm.
- **Kiểm trước khi bật (trên Mac):**
  1. Thêm ca vào `critic/tests/test_calibration.py` bằng `critic/tests/synth.py`. Một cú sin 80 Hz dài 120 ms phải trượt cả `tail_ms` và luật trầm đứng riêng. Một tiếng trúng có thân 150–800 Hz và đuôi 300 ms phải đạt.
  2. Đo các ứng viên lô 1 có sẵn: `fire.cast` hướng "phụt tròn" (A, C) phải xếp dưới hướng có hơi thở (B, D); `fire.impact.*` cũng vậy.
  3. Sau phiên S2 của anh, chạy `critic agreement --batch 1` với và không có `owner-v2`. Chỉ bật khi số cặp khớp không giảm.
- **Vì sao chưa làm trong mã:**
  - ngưỡng chưa đo trên file nào;
  - máy Dell không có venv, trọng số hay file âm của Audio Lab;
  - mục 4.6 đòi hiệu chỉnh L2 dựa trên điểm chấm, và làn Critic giữ mã này.

---

## Mục 16 của kế hoạch: đã chốt và còn mở

| # | Câu hỏi | Trạng thái | Căn cứ hoặc điều còn thiếu |
|---|---|---|---|
| 1 | Ai sở hữu, điều kiện Stability Community | **Đã chốt trước lô 0b**, không phải bằng điểm chấm | Bước 0 xong (chủ dự án là cá nhân), Stable Audio 3 đã chạy. Mặc định "chưa tải Stable Audio 3" hết hiệu lực; điểm chấm chốt thêm điều kiện đi tiếp của mục 9 (Q1) |
| 2 | Nhạc nhường giọng đọc bao nhiêu | Còn mở | Cần bài C; điểm chấm không đụng tới |
| 3 | Âm xong từ và phím trong lúc đọc | Còn mở | Cần bài C |
| 4 | `word-hit` hạ một quãng tám thành C4–C5 | **Đã chốt bằng điểm chấm** | C4 3/5 > C5 ngân rung 2/5 > C5 1/5. Bộ 7 file theo thang làm ở C4–C5. Thẻ spec `word-hit` (intent đang ghi C5–C6) và tài liệu Lời Gọi cần sửa |
| 5 | Nguồn chuông và cồng của Lời Gọi | **Chốt một phần** | Chốt: `leak` dùng kẻng sắt VCSL Anvil (4/5 > Gong 1 3/5); VCSL Hand Chimes dùng được cho UI (A5 3/5); vẫn không dùng Hand Bells Nepalese. Còn mở: Tubular Bells chưa nghe; nguồn chuông cho `word-hit-bell`; cồng cho lúc trang trọng; VCSL Gong là tam-tam hay cồng có núm |
| 6 | Tách bậc trúng Tuyến Cuối thành lớp, thêm `hit.sub`, `hit.tail` | Còn mở | Điểm chấm hợp với mặc định (bản `hit.t2` nặng sub nhất bị 1/5; `hit.t1` tốt nhất không có sub), nhưng không quyết cách ghép lúc chạy |
| 7 | `amb.forest` giữ vòng 6 s | Còn mở | Bản 6 s được 4/5, nhưng anh chỉ nghe một vòng ("Một mình"), chưa nghe Lặp, nên chỗ nối và "nhàm khi lặp" chưa được thử |
| 8 | Stem `general` "D minor" trên Rê Dorian | Còn mở | Không liên quan điểm chấm |
| 9 | 116 file âm CC0 của Space Typing | Còn mở (giữ mặc định) | Không liên quan |
| 10 | Cài Surge XT | Còn mở (giữ mặc định: không cài) | Không liên quan |
| 11 | Dùng Sonniss | Còn mở (giữ mặc định: không dùng) | Không liên quan |
| 12 | Sửa mã âm trong game khi nào | Còn mở (giữ mặc định) | Không liên quan |

---

## Việc còn lại cho người điều phối

1. **`AUDIO_PIPELINE.md`** (Audio Lab không sửa file này):
   - mục 4.3.1: Q3;
   - mục 4.3.3: các hàng trúng nhỏ, trúng nặng, nền lặp theo Q4;
   - mục 4.5: trọng số audiobox theo họ;
   - mục 3.2: nguồn `hit.t1` (Q1);
   - mục 8.2: Q2 và `leak` dùng kẻng;
   - mục 9: điều kiện đi tiếp đã đạt;
   - mục 16: bảng trên.
2. **Thẻ spec và tài liệu game:**
   - `word-hit` C4–C5;
   - `attack_max_ms: 150` cho các id gọi trọn, sau khi mục 4.3.1 được sửa.
   - Tài liệu trong `games/**` chờ lượt sửa game.
3. **Phiên lô 1:**
   - nghe bằng tai nghe;
   - nền lặp nghe ở bối cảnh Lặp;
   - chèn cặp mốc để đo độ nhất quán;
   - nhắc anh gắn nhãn "rè/lỗi" khi nghe thấy, để có dữ liệu chỉnh L1b;
   - đặt `gun.xung` tổng hợp và `gun.xung` Stable Audio 3 trong cùng một phiên.
