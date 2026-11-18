# Lô 1: bản thiết kế

> **Ngày:** 24/10/2026. **Trạng thái:** thiết kế, chưa tạo âm nào. Lô 1 bắt đầu khi người điều phối duyệt bản này.
> **Dựa trên:** [`AUDIO_PIPELINE.md`](../../docs/games/AUDIO_PIPELINE.md) mục 3.2, 4.6, 5, 6, 8, 9, 16; [`DECISIONS.md`](DECISIONS.md) Q1–Q5; bản hiệu chỉnh 1 (`critic/calibration/owner-v1.json`, báo cáo `~/AudioLab/work/_calibration/owner-v1.md`); điểm chấm của anh ở `~/AudioLab/review/<game>/ratings.jsonl` (lô 0a, 0b); mã phát âm hiện tại của ba game (chỉ đọc).
> **Luật làm việc:** dữ liệu nặng chỉ ở `~/AudioLab`; mã chỉ sửa trong `tools/audio-lab`; không sửa `games/**` (nối âm vào game là bước sau); mỗi lúc một mô hình nặng (Stable Audio 3 khoảng 2 GB, bộ chấm tới 4 GB) và một tiến trình tạo; Hugging Face offline, không token.
> Mã băm 8 ký tự (ví dụ `00d0eb0f`) là mã của bản trong file điểm, để tra lại đúng file.

---

## 0. Tóm tắt

- **28 id của mục 9**, cộng **4 id làm lại** mà điểm chấm và bản hiệu chỉnh chỉ ra (`enemy.quadruped.howl`, `call-chop`, `ui-move`, `ui-pick`), cộng `trap.pine-bomb.trigger` nếu còn thời gian.
- **Súng Xung được thiết kế lại thành một họ âm "liên thanh"** (mục 3), trả lời ghi chú duy nhất của anh: "không liên thanh, ngắt quãng, thiếu sự liên tục, lực trong chiến đấu". Họ gồm phát đơn có đuôi chồng lên phát sau, một lớp nền cơ khí chạy suốt lúc bắn, một đuôi khi ngừng bắn, và hai bộ nhấn (nặng, nhẹ) xoay vòng. Đề xuất hai id mới: `gun.xung.loop`, `gun.xung.tail`.
- **Một bài thử mới, "Liên thanh 3 s"**: dựng 3 s bắn liên tục đúng nhịp thật của game (10 viên mỗi giây) qua một bộ trộn giống game (bus, nén, giới hạn tiếng), kèm chuỗi "gõ xong từ → nạp đạn → giọng đọc". Bản dựng thành một **bối cảnh mới trên Bảng Nghe**. Đây là việc P0, làm trước mọi lượt tạo âm.
- **Mã phát hiện tại của Tuyến Cuối tự nó đã làm súng nghe ngắt quãng** (mục 5): game bắn 10 viên mỗi giây nhưng chỉ phát tiếng cho một nửa số viên; mỗi tiếng tắt sau khoảng 90 ms; bộ nén mỗi bus bắt trong 2 ms nên ăn mất đầu tiếng. Có 24 chỗ cần sửa ở bước nối (8 ở Tuyến Cuối, 7 ở kit, 6 ở Rồng Giữ Ải, 3 ở Lời Gọi), ghi kèm file và dòng.
- **Nguồn theo điểm chấm:** Stable Audio 3 thô cho `hit.t1`, `amb.forest`, tiếng tru, `call-chop` (anh chọn bản thô); công thức ghép lớp cho súng và cầu lửa (công thức được 3/5, súng tổng hợp 0a được 4/5); bộ phát mẫu cho đàn tranh, kèn, kẻng.
- **Thứ tự sản xuất** (mục 6): P0 công cụ → P1 Tuyến Cuối súng và trúng → P2 Rồng Giữ Ải trận đánh → P3 Rồng Giữ Ải nền và báo đợt → P4 Tuyến Cuối phần còn lại → P5 Lời Gọi. Sáu phiên nghe, mỗi phiên dưới 20 phút, tổng khoảng 2 giờ của anh.

---

## 1. Tai anh đã nói gì

### 1.1 Điểm chấm lô 0a và 0b

| Id | Lô | Anh chọn | Sao | Bản thua | Hướng cho lô 1 |
|---|---|---|---|---|---|
| `gun.xung` | 0a | v2, công thức tổng hợp: sub 95→45 Hz, nổ giòn 2–9 kHz, khóa nòng Kenney (`00d0eb0f`) | **4/5** | v3 cùng công thức 3/5 | Giữ nổ giòn và khóa nòng; thêm liên tục và thân |
| `gun.xung` | 0b | v1, công thức có thân Stable Audio 3 lọc 1,5 kHz (`1a95bc4b`) | 3/5 | v3 3/5 | Thân Stable Audio 3 dùng được, chưa hơn 0a |
| `hit.t1` | 0a | v4, crest 19,9 dB (`45ff4588`) | 3/5 | v2 2/5 | Crest cao thắng |
| `hit.t1` | 0b | Stable Audio 3 thô C s1006, bản dò (`7120c956`) | 3/5 | Hai công thức thân dày 2/5 | Nguyên khối, thân vừa (10–35 %) |
| `hit.t2` | 0a | v2 ít sub, bản dò (`e169bbdd`) | 3/5 | v4 2/5; v1 nặng sub nhất (78 % dưới 150 Hz) 1/5 | Bớt sub |
| `fire.impact.a` | 0a | v3, 55 % dưới 150 Hz, bản dò (`c58fa0c7`) | 3/5 | v4, v2 (84 % dưới 150 Hz) 2/5 | Bớt sub |
| `fire.impact.a` | 0b | Công thức Stable Audio 3, v4 (`77e0dd55`) bằng v2 (`af84aad3`) | 3/5 | — | Công thức thành mẫu của họ |
| `trap.pine-bomb.trigger` | 0a | v3, nứt gỗ Kenney (`19438fdb`) | 3/5 | v2 2/5 | Sửa nhẹ |
| `wave.horn` | 0a | v1, hai kèn co Rê–La (`d6e963bf`) | 3/5 | Kèn co trên trombone 2/5; trombone trầm 1/5 | Kèn co, không trombone |
| `amb.forest` | 0b | E s2006, sáng, xì qua lá kim, bản dò (`10c80671`) | **4/5** | H s2004 ù trầm 3/5; G 2/5 | Hướng sáng |
| `enemy.quadruped.howl` | 0b | B s1004, trọn tiếng tru, lớn dần 138,5 ms (`b9ef6989`) | 3/5 | A s1001 2/5 | Giữ trọn tiếng gọi |
| `call-chop` | 0b | A s1006 (`1bbffcc4`), bằng E s2003 (`3e5ee6dc`) | 3/5 | B s1002 kiểu mõ 2/5 | Gõ trầm; cấm mõ |
| `word-hit` | 0a | C4, bản dò (`e79e84d1`) | 3/5 | C5 rung 2/5; C5 1/5 | Hạ một quãng tám |
| `leak` | 0a | Kẻng sắt VCSL Anvil, ba nhát (`0d842a87`) | **4/5** | Cồng VCSL Gong 1 3/5 | Kẻng |
| `ui-pick` | 0a | Phách gỗ và Hand Chimes A5 (`2b7be772`) | 3/5 | G5 2/5; C6 1/5 | A5 |
| `ui-move` | 0a | Trống khe VCSL Slit Drum (`ea8b0706`) | 3/5 | Mõ gỗ click2 2/5; click3 1/5 | Trống khe |

**Những gì lặp lại qua các id:**

- Không bản nào 5/5. Phần lớn id 3/5 ("dùng được nếu sửa nhẹ"). Bốn bản 4/5: `gun.xung` 0a, `amb.forest`, `leak`, `calib-3`.
- Ở cả 6/6 id có bản dò, anh chọn bản dò. Bản máy xếp đầu chỉ được chọn ở 8/19 id. Bản hiệu chỉnh 1 nâng mức khớp từ 13/37 lên 24/37 cặp, nhưng con số này đo trên chính dữ liệu đã dùng để chọn luật. Lô 1 là phép thử thật.
- **Trúng:** bản được chấm cao sáng hơn ở 10/13 cặp và ít năng lượng dưới 150 Hz hơn ở 8/12 cặp.
- **Bắn:** bản có cú nảy 20 ms đầu mạnh hơn thắng 3/3 cặp.
- **Âm đơn:** bản đuôi ngắn hơn thắng 23/36 cặp. Vì vậy sự liên tục của súng phải đến từ lớp nền và phần thân chồng lên nhau ở mức thấp, **không** đến từ đuôi ngân dài (mục 3).
- **Mọi lượt chấm đều nghe bằng loa.** Nếu đó là loa trong của Mac mini (mục 2 của kế hoạch: một loa nhỏ), loa phát rất yếu dưới 150 Hz, và lực anh nghe được nằm chủ yếu ở 150–500 Hz và ở đầu tiếng. Người chơi trên laptop cũng nghe như vậy.
- Lô 0b chấm xong trong 2,9 phút cho 15 bản; `amb.forest` chỉ nghe một vòng ở "Một mình". Không có cặp mốc, không có nhãn "rè/lỗi".

### 1.2 Ghi chú "không liên thanh": đo được gì

Ghi chú nằm ở `calib-1`: một tiếng trúng nặng tổng hợp (`syn_punchy_impact`) cùng hai bản làm hỏng, phát ở bối cảnh Lặp, **2 lần mỗi giây** (cách 500 ms). Anh chọn bản "mỏng" 3/5 nhưng gắn **"chậm"**; bản gốc 2/5; bản "đục" 1/5 nhưng được gắn **"hợp game"**. Đọc cùng ghi chú: anh muốn sức nặng của bản đục, độ sạch của bản mỏng, và nhịp nhanh, liền. Ghi chú nói về cảm giác chiến đấu nói chung, nên áp cho mọi âm phát dày: súng, trúng, Tia, tên bắn.

Số đo trên các bản súng và trúng anh đã chấm, khi phát lặp đúng nhịp:

| Bản | Tắt xuống −20 dB sau | Thời gian ở dưới đỉnh hơn 20 dB khi lặp 5 lần/s | Khi lặp 10 lần/s | Mất trên loa nhỏ (lọc cao 200 Hz) | Năng lượng dưới 150 Hz / 150–500 Hz / 2–6 kHz |
|---|---|---|---|---|---|
| `gun.xung` 0a v2 (4/5) | 48 ms | 76 % | 52 % | −7,6 dB | 82 % / 10 % / 3 % |
| `gun.xung` 0b v1 (3/5) | 47 ms | 77 % | 53 % | −6,5 dB | 75 % / 14 % / 1 % |
| `gun.xung` 0b v3 (3/5) | 40 ms | 80 % | 61 % | −4,6 dB | 61 % / 18 % / 1 % |
| `hit.t1` 0b C s1006 (3/5) | 47 ms | 76 % | 51 % | 0,0 dB | 0 % / 2 % / 37 % |

- Mỗi phát súng tắt hẳn sau khoảng 50 ms. Ở nhịp 5 lần mỗi giây, ba phần tư thời gian thấp hơn đỉnh quá 20 dB, gần như lặng: đúng cảm giác "ngắt quãng".
- Phần lớn năng lượng của súng nằm dưới 150 Hz, dải mà loa nhỏ phát rất yếu. Hai bản 0a v2 và 0b v1 mất 6,5–7,6 dB trên loa nhỏ, trong khi kế hoạch cho phép tối đa 6 dB (bài F). Thứ còn lại là 10–18 % thân 150–500 Hz và 1–3 % tiếng giòn: đúng cảm giác "thiếu lực".
- Bảng Nghe phát Lặp không có bộ nén và không có tiếng trận. Trong game còn tệ hơn: xem mục 5.

---

## 2. Luật chung cho lô 1

**Nguồn**

- Chọn nguồn theo điểm chấm, không theo thói quen. Anh chọn Stable Audio 3 thô ở `hit.t1`, `amb.forest`, tiếng tru, `call-chop`: các id cùng họ thử bản thô trước, ghép lớp chỉ khi bản thô thiếu một phần rõ ràng (đầu tiếng chưa xác minh, thiếu thân).
- Công thức được 3/5 (`fire.impact.a.sa3-r2`, `gun.xung.sa3-r2`) là mẫu cho họ của chúng. Công thức thân dày của `hit.t1` (2/5) **không** thành mẫu cho `hit.t2`, `hit.t4` (DECISIONS Q1).
- Stable Audio 3: 4 prompt × 6 seed cho mỗi id mới; độ dài tạo chỉ 1, 2, 3 hoặc 10 s (`gen/README.md`); cfg 1,0, không negative prompt. Dùng lại bản thô đã có trong `~/AudioLab/work/<game>/<id>/sa3-trial/raw` trước khi tạo mới.
- **Prompt cấm cho Lời Gọi (Q2):** không dùng prompt B, D của `call-chop` và không viết prompt có "tok", "tốc", "hollow tube", "temple block", "wooden fish", "mõ" cho mọi `call-*` và UI của Lời Gọi. P0 thêm bước chặn vào `gen.sa3`.
- Không dùng VCSL Hand Bells Nepalese. Chuông và cồng của Lời Gọi theo mục 16 #5 (đã chốt kẻng Anvil cho `leak`, Hand Chimes cho UI).

**Chấm máy**

- Bản hiệu chỉnh 1 bật mặc định (`critic run` dùng bản mới nhất). Lô 1 là phép thử: chấm xong chạy `bash tools/audio-lab/run.sh critic agreement --batch 1`.
- Cổng L1 không đổi, trừ tiếng gọi trọn: `attack_max_ms: 150` cho `enemy.quadruped.howl` sau khi người điều phối sửa mục 4.3.1 (Q3). Trước đó tiếng tru vào phiên với vai trò "bị luật chặn" như lô 0b.
- Bản chưa xác minh đầu tiếng, bản có cờ hai đầu tiếng (trừ id cố ý có hai nhịp như `word.load`), bản lệch kênh không vào phiên.
- **Loa nhỏ:** mọi âm trận đánh mất không quá 6 dB ở lọc cao 200 Hz (bài F); súng và trúng nặng nhắm 4 dB. Lực phải nghe được trên loa của anh: thân 150–500 Hz và họa âm của sub (bão hòa nhẹ) gánh phần này.

**Biến thể và phát**

- Theo mục 5.3; xoay vòng ngẫu nhiên, không lặp 2 bản gần nhất. Âm thưởng hiếm, UI, báo nguy giữ cố định.
- Âm phát sau mỗi từ (`fire.cast`, `word.load`, `word.perfect`, `word-hit`, `word-hit-bell`) theo luật mục 6.2: năng lượng 1–4 kHz giảm ít nhất 15 dB trong 100 ms sau đầu tiếng. Không đạt thì ghi "giọng chờ 150 ms" vào thẻ, không tự sửa mã game.

**Phiên nghe**

- Danh sách nghe: bản đứng đầu, bản khác nhất, bản dò ở khoảng 30 % số id (mục 4.6). Mỗi phiên chèn 4–6 cặp mốc lấy từ lô 0a, 0b để đo độ nhất quán.
- Nhắc anh dùng **tai nghe** cho phiên súng và phiên nền, rồi nghe lại súng một lượt bằng loa.
- Nền lặp nghe ở bối cảnh Lặp, ít nhất 3 vòng.
- Nhắc gắn **"rè/lỗi"** khi nghe thấy, để có dữ liệu chỉnh L1b.
- Âm phát dày (súng, trúng, Tia, tên, mực, xu) chấm ở bối cảnh **Liên thanh** (mục 3.5) khi đã có bản dựng.

**Khi nào dừng:** tối đa 3 vòng sửa prompt mỗi id; sau đó đổi nguồn (mục 5.5).

---

## 3. Súng Xung liên thanh

### 3.1 Vì sao nghe ngắt quãng

Ba nguyên nhân cộng lại:

1. **Âm:** mỗi phát tắt sau khoảng 50 ms (mục 1.2). Không có gì nối phát này với phát sau.
2. **Nhịp:** game bắn 10 viên mỗi giây (`XUNG` 24 viên trong 2,4 s; từ gõ nhanh ×1,15 thành 11,5 viên mỗi giây), nhưng chỉ phát tiếng cho viên chẵn (`src/view/combat.ts:139`). Mắt thấy 10 chớp nòng mỗi giây, tai nghe 5 tiếng: tiếng chậm hơn hình một nửa.
3. **Bộ trộn:** bộ nén mỗi bus của Tuyến Cuối bắt trong 2 ms và nhả trong 140 ms. Mỗi phát vượt ngưỡng, đầu tiếng bị ép trước khi kịp nảy, rồi mức bơm lên xuống theo nhịp bắn (mục 5, T3).

Thiết kế dưới đây sửa phần âm, và ghi phần nhịp, bộ trộn thành hợp đồng cho bước nối.

### 3.2 Họ âm `gun.xung`

Ba id. Hai id sau là đề xuất mới, chờ sửa `THEME_SOUND_LIST.md` của Tuyến Cuối (giống `hit.sub`, `hit.tail`).

| Id | Phát khi | Dài | Lớp | Số file |
|---|---|---|---|---|
| `gun.xung` | Mỗi viên rời nòng | Đầu 0–120 ms, đuôi tắt dần tới khoảng 350 ms | Tiếng nổ giòn, khóa nòng, thân, sub | 8: bộ **nặng** A (4) và bộ **nhẹ** B (4) |
| `gun.xung.loop` (mới) | Suốt lúc súng đang bắn | Vòng lặp 2,0–3,0 s, liền mối | Nền cơ khí: tiếng lách cách của băng đạn, động cơ tháp pháo, ù trầm | 2 (đổi vòng ở mỗi loạt) |
| `gun.xung.tail` (mới) | Khi súng ngừng (hết đạn, mất mục tiêu) | 0,4–0,7 s | Vang thép của sảnh rộng, máy dừng | 2 |

**`gun.xung`: một phát**

| Lớp | Dải | Thời gian | Nguồn | Ghi chú |
|---|---|---|---|---|
| Nổ giòn | 2–6 kHz (tới 9 kHz) | 0–15 ms | Nhiễu trắng như công thức 0a (lớp `crack`) | Đầu tiếng lên dưới 3 ms. Đây là phần anh thích ở 0a |
| Khóa nòng | 1,2–6 kHz | 10–45 ms | Kenney Impact Metal light/heavy, RPG `metalClick`, `metalLatch` | Cắt ngắn, không ngân ở 1–4 kHz (bài học vòng 2 của 0a) |
| Thân | **150–500 Hz** (tới 800 Hz) | 0–120 ms, đuôi tắt dần tới 350 ms | Thân Stable Audio 3 lọc thông thấp 1,5–2 kHz (4 thân đã kiểm không có đầu tiếng thứ hai: A s1005, D s1002, C s1002, D s1005), cộng thân mới | **Lớp gánh "lực" trên loa.** Đuôi thân là thứ chồng lên phát sau |
| Sub | 45–90 Hz | ≤ 120 ms | `sub_thump` 95→45 Hz | Bão hòa nhẹ để có họa âm 90–270 Hz nghe được trên loa nhỏ. Chỉ có ở bộ A |

- **Bộ A (nặng):** đủ bốn lớp. **Bộ B (nhẹ):** nổ giòn, khóa nòng, thân mỏng hơn; không sub; nhỏ hơn A 4–6 dB. Game phát A và B xen nhau ở 10 viên mỗi giây: sub chỉ 5 lần mỗi giây nên không đục, nhịp tai khớp nhịp mắt.
- **Hình đuôi:** tắt theo hàm mũ; xuống −20 dB ở 140–180 ms, xuống −40 dB trước 350 ms. Ở nhịp 100 ms, đuôi phát trước còn khoảng −12 dB khi phát sau tới: liền mà không nhòe. Phần 1–4 kHz phải tắt xuống −20 dB trong 60 ms (giọng đọc).
- **Biến thể:** trong một bộ, đổi thân và khóa nòng (`swapMode: cycle`), giữ nổ giòn cùng một khuôn. Lệch cao độ khi phát: A ±40 cent, B ±70 cent; ±1 dB. Lệch lớn hơn nghe như súng "lắc".

**`gun.xung.loop`: nền liên thanh**

- Thứ làm tai nghe một **loạt** đạn thay vì nhiều phát rời. Không chứa phát súng nào nổi lên: mọi đầu tiếng trong vòng thấp hơn đỉnh phát đơn ít nhất 12 dB, để nhịp đến từ phát đơn, không lệch với nó.
- **Không có chu kỳ rõ ở 5–15 Hz** (tự tương quan đường bao ở độ trễ 60–220 ms dưới 0,3). Nhờ vậy khi từ gõ nhanh đẩy súng lên 11,5 viên mỗi giây, nền không lệch nhịp và mã không phải đổi tốc độ phát của nền.
- Phổ: phần chính 80–500 Hz (ù động cơ, rung tháp pháo) cộng một lớp lách cách 3–8 kHz rất nhỏ. Năng lượng 1–4 kHz thấp hơn dải 100–500 Hz của chính nó ít nhất 18 dB.
- Mức trong game: thấp hơn đỉnh phát đơn 11–18 dB (bài thử chọn mức, mục 3.4). Vào 30–60 ms, ra 80–120 ms dưới `gun.xung.tail`.
- Nguồn ứng viên: VSCO-2-CE `Ratchet1-Fast` và `Snare2-roll` (lách cách băng đạn), Kenney Sci-fi `engineCircular`, `spaceEngineLow` (động cơ; bản `spaceEngineLow` có lỗi mối nối đã biết, chỉ dùng đoạn giữa), Stable Audio 3 dài 10 s rồi cắt vòng bằng `gen/process.py` (chế độ nền lặp, kiểm mối nối L1).

**`gun.xung.tail`: khi ngừng bắn**

- Vang thép của sảnh rộng cộng tiếng máy dừng (servo hạ, chốt). Dùng chung chất liệu với `hit.tail` (VCSL Anvil, Brake Drum, vang phòng tổng hợp), lọc thấp hơn, ngắn hơn.
- Phần 1–4 kHz xuống −20 dB trong 150 ms. Không có bước nhảy mức trên 6 dB trong 10 ms (ngừng bắn không được nghe như bị cắt).

### 3.3 Cách phát: hợp đồng cho bước nối vào game

Đây là thứ bài thử dựng theo, và là việc của bước nối (mục 5 ghi chỗ sửa):

1. Phát tiếng cho **mọi viên**, A và B xen nhau, theo **thời điểm mô phỏng** của viên đó (không gom về đầu khung hình).
2. `gun.xung.loop` chạy từ viên đầu của loạt tới viên cuối; ngừng thì phát `gun.xung.tail` và mờ nền trong 80–120 ms. Mỗi loạt bắt đầu ở một điểm ngẫu nhiên trong vòng.
3. Tối đa 4 tiếng `gun.xung` cùng lúc (mục 5.3); đầy thì cướp tiếng cũ nhất, mờ trong 20–30 ms, không bao giờ cắt cứng. Nền và đuôi không bị cướp.
4. Bộ nén bus súng: bắt 10–20 ms, nhả 250–400 ms, một phát đơn không bị ép quá 2 dB.
5. Khi đọc từ: bus súng hạ −6 dB như tài liệu game, bắt đầu từ lúc game gửi yêu cầu đọc (mục 6.2 bước 4).

### 3.4 Nguồn và ứng viên cho phiên nghe

- **Ba hướng**, mỗi hướng một bộ đủ (8 phát, 2 vòng nền, 2 đuôi):
  1. **0a nâng cấp:** công thức 0a (bản 4/5) giữ nổ giòn và khóa nòng, thân 150–500 Hz dày thêm khoảng 6 dB, đuôi mới, sub bão hòa. Nền ở −16 dB.
  2. **Thân Stable Audio 3:** công thức 0b với 4 thân đã kiểm cộng 4 thân mới, khóa nòng đổi sang `impactMetal_light` như 0a. Nền ở −16 dB.
  3. **Như hướng 2, nền to:** nền ở −11 dB, để biết anh muốn nền rõ tới đâu.
- **Tạo mới bằng Stable Audio 3:**
  - Thân: 4 prompt × 6 seed, 1 s. Prompt nhấn thân và lực, ví dụ "TrackType: SFX, heavy autocannon firing a single round inside a steel turret, deep chesty body, punchy low-mid thump, short, close, dry, industrial".
  - Nền: 3 prompt × 4 seed, 10 s. Ví dụ "TrackType: SFX, continuous mechanical rattle of an ammunition feed belt and a turret motor running, steady, no gunshots, close, dry, industrial", "Steady heavy machinery hum and fast metallic clatter, constant, no impacts".
  - Đuôi: 2 prompt × 6 seed, 3 s. Ví dụ "Gunfire stops in a huge steel hall, metallic echo fading, servo winding down, short".
- Bản 0a v2 (`00d0eb0f`, 4/5) dựng bằng chính bài thử, phát theo cách game đang phát (viên chẵn, không nền), làm **cặp mốc**: đo xem cách phát mới có hơn không, tách khỏi phần âm mới.

### 3.5 Bài thử "Liên thanh 3 s" và bối cảnh mới trên Bảng Nghe (P0)

**Module mới `tools/audio-lab/context`.** Lệnh đề xuất: `bash tools/audio-lab/run.sh context render --scenario ts-xung-3s --set <bộ ứng viên>.json --out ~/AudioLab/work/_context/<lần chạy>/`. Chỉ numpy, scipy, soundfile; không mô hình nặng.

**Kịch bản `ts-xung-3s` (Tuyến Cuối), số lấy từ mã game:**

| Thời điểm | Sự kiện |
|---|---|
| 0,00 s | Gõ xong từ 1: `word.load` (bus `alerts`, lệch trái 0,35) và yêu cầu đọc từ: bắt đầu hạ tiếng |
| 0,05 s | Băng đạn 1 bắn: một viên mỗi 100 ms |
| 0,15 s | Giọng đọc từ 1 cất lên (quét thêm 0 s và 0,40 s ở bản báo cáo) |
| +150–300 ms sau mỗi viên | Viên trúng (seed cố định): T1, khoảng 9 % là T2 (chí mạng 5 % + 4 % gõ sạch); gom 38 ms như mã; T2 thêm `hit.sub` |
| 1,40 s | Gõ xong từ 2: `word.load`, giọng đọc ở 1,55 s; băng đạn 2 nối tiếp, súng không ngừng |
| 3,05 s | Ngừng bắn (mất mục tiêu): `gun.xung.tail` |
| tới khoảng 3,8 s | Đuôi tắt |

- **Bộ trộn đơn giản giống game:** bus và mức của `theme-audio.ts` (súng 0,42, trúng 0,6, hạ quái 0,55, cảnh báo 0,8); hạ khi đọc (súng ×0,5, trúng ×0,5, cảnh báo ×0,8; hằng số thời gian 50 ms như `SceneAudio`); bộ nén mỗi bus (ngưỡng −12 dB, knee 6, tỉ lệ 8). Hai cấu hình: **"game hiện tại"** (viên chẵn, không nền, nén bắt 2 ms nhả 140 ms) và **"đề xuất"** (mục 3.3). Bộ nén là phép xấp xỉ `DynamicsCompressorNode`, ghi rõ trong báo cáo.
- **Giới hạn tiếng:** tối đa 4 tiếng mỗi vũ khí, cướp tiếng cũ nhất (mờ 25 ms); cùng một id cách nhau ít nhất 30 ms; hạ quái tối đa 4 trong 120 ms.
- **Giọng đọc:** 2–3 giọng tiếng Anh của macOS ghi bằng `say -v <giọng> -o …` (bài C), lưu ở `~/AudioLab/work/_context/voices/`. Từ mẫu: "harbor", "lantern".
- **Cân độ to trước khi trộn:** stem súng của mọi ứng viên về cùng LUFS-S max, nên giọng đọc và `word.load` giữ đúng mức so với súng.
- **Ra:** WAV 48 kHz 24-bit stereo; stem từng bus; dòng thời gian JSON; số đo JSON; thẻ ảnh PNG có đường bao và các chỗ trũng.
- **Số đo** (đều là điểm xuất phát, chỉnh lại sau lần chạy đầu trên 0a v2):

| Số đo | Cách đo | Đạt khi |
|---|---|---|
| Độ sâu chỗ trũng | Giữa hai phát liền, đỉnh đường bao RMS 5 ms trừ đáy, trên stem súng | Trung vị ≤ 12 dB, lớn nhất ≤ 18 dB |
| Thời gian hổng | Phần thời gian đang bắn mà stem súng thấp hơn đỉnh trượt 300 ms quá 20 dB | ≤ 5 % (bản 0a v2 lặp 5 lần mỗi giây: 76 %) |
| Đều nhịp | Độ lệch chuẩn khoảng cách giữa các đầu tiếng, bỏ phần lệch cố ý | ≤ 8 ms |
| Lực | Bộ A: crest ≥ 12 dB; stem súng: 40–150 Hz 20–40 %, 150–500 Hz ≥ 25 %, 2–6 kHz 5–15 % | Đủ cả ba |
| Loa nhỏ | Mất ở lọc cao 200 Hz, stem súng | ≤ 4 dB (0a v2: 7,6 dB) |
| Bơm | Mức ép của bộ nén bus súng | Trung vị ≤ 3 dB; dao động theo nhịp bắn ≤ 2 dB |
| Giọng đọc | Bài C: 300 ms đầu của giọng, dải 1–4 kHz | Giọng cao hơn phần còn lại ≥ 10 dB |
| Ngừng bắn | Đường bao sau viên cuối | Không bước nhảy > 6 dB trong 10 ms; tới −60 dB trong 800 ms |
| Lặp biến thể | Thứ tự phát | Không bản nào phát hai lần liền |
| Đỉnh | Toàn bản trộn | ≤ −1 dBTP, không clip |

**Kịch bản khác dùng cùng module** (cho P2, P5): `dh-cast-chain` (Rồng Giữ Ải: gõ xong → `fire.cast` → giọng đọc → `fire.impact.*` cách 0,6 s), `td-wordhit-chain` (Lời Gọi: chuỗi `word-hit` theo bậc → giọng đọc, `arrow-fire` 4 lần mỗi giây từ 3 tháp, `ink-puff` 8 lần mỗi giây, `coin` 3 lần mỗi giây). Mỗi kịch bản có hai cấu hình "game hiện tại" và "đề xuất".

**Bối cảnh mới trên Bảng Nghe:**

- Khóa `burst`, nhãn **"Liên thanh 3 s"**. Ứng viên có thêm `ctx: {"burst": [file]}` trong file phiên; bảng phát đúng file đã dựng, không tự lặp. Không có bản dựng thì nút bị mờ.
- Bối cảnh mặc định đầu tiên cho `gun.xung`, `hit.t1`, `gun.tia.pulse`, `kill.swarm`, `arrow-fire`, `ink-puff`, `coin` khi có bản dựng.
- Thêm nhãn **"ngắt quãng"** vào bộ nhãn cố định. Cách sửa định sẵn (mục 5.4): kéo dài đuôi thân, nâng nền, kiểm nhịp phát.
- Sửa ở `board/config.py` (CONTEXTS, TAGS), `board/session.py` (kiểm `ctx`), `board/server.py` (phục vụ file `ctx`), `board/static/app.js` (phát), kèm kiểm thử.

### 3.6 Kiểm nhận cho họ súng

- **Máy:** mỗi phát qua L1 (lên ≤ 3 ms ở bộ A, im lặng đầu ≤ 5 ms, một đầu tiếng); mọi số đo của bảng trên đạt ở cấu hình "đề xuất"; `gun.xung.loop` qua kiểm mối nối L1; không cờ L1b mới.
- **Anh:** ở "Liên thanh 3 s", hướng thắng từ 4/5 (ngang bản 0a) và anh không gắn "ngắt quãng", "đục", "yếu/mỏng". Ở "Một mình" vẫn từ 3/5.
- Hướng thắng thắng cả cặp mốc (0a v2 phát theo cách game hiện tại). Nếu thua: lỗi nằm ở cách phát hoặc ở nền, không phải ở phát đơn; ghi lại và sửa đúng phần đó.

---

## 4. Từng id

Khuôn mỗi id: **vai trò** trong game; **anh đã nghe** gì; **nguồn**; **tham chiếu** (bản anh chấm cao nhất); **biến thể**; **kiểm nhận**. Luật ở mục 2 áp cho mọi id, không ghi lại.

### 4.1 Tuyến Cuối (trạm thép bên mép hố đen)

Gốc prompt: *industrial, steel, close, punchy*. Lớp chữ ký: tia điện và thép ngân. Bậc trúng ghép lúc chạy từ lớp đầu tiếng + thân của từng bậc, cộng `hit.sub` và `hit.tail` dùng chung (mục 6.3, câu hỏi 16 #6 còn mở: lô 1 làm đủ lớp và kèm bản ghép sẵn để nghe).

#### #11 `gun.xung` (+ `gun.xung.loop`, `gun.xung.tail`)

Xem mục 3. Tham chiếu: 0a v2 (`00d0eb0f`, 4/5), 0b v1 (`1a95bc4b`, 3/5). Biến thể: 8 phát (A4 + B4), 2 vòng nền, 2 đuôi.

#### #12 `hit.t1` · đạn Xung trúng vỏ thép

- **Vai trò:** mỗi viên trúng, gom 38 ms; tới 10 lần mỗi giây khi bắn liền. 64–96 ms, ±150 cent, ±2 dB, bus `impacts`.
- **Anh đã nghe:** 0b chọn Stable Audio 3 thô C s1006 (3/5, thân 5,5 %, crest 17,9 dB) trên hai công thức thân dày (2/5). 0a chọn bản crest cao nhất. Luật `t-hit-small-steel`: thân 200–800 Hz 10–35 %, crest 12–20 dB.
- **Nguồn:** Stable Audio 3 thô, chọn cửa sổ có đầu tiếng đã xác minh. Prompt C ("metal impact one-shot, small projectile hitting an armored steel door, crisp transient, short gritty clank, no tail") là gốc; thêm A, D và một prompt mới nghiêng "sáng hơn, thân vừa". Xử lý lại bản thô họ C đã có, rồi tạo thêm 12 seed. Không nướng sub hay đuôi vào file. Chỉ thêm lớp tách Kenney khi đầu tiếng chưa xác minh.
- **Tham chiếu:** 0b C s1006 (`7120c956`), 0a v4 (`45ff4588`).
- **Biến thể:** 6 (thêm 2 dự phòng).
- **Kiểm nhận:** thân 10–35 %; crest 12–20 dB; có đầu tiếng 2–6 kHz; trọng tâm phổ không thấp hơn tham chiếu; một đầu tiếng; không đuôi dài (độ liền của chuỗi do súng gánh, mục 1.1). Trong "Liên thanh 3 s": tiếng trúng không che đầu tiếng súng. Anh từ 3/5, không "chói", không "nhàm khi lặp".

#### #13 `hit.t2` + `hit.sub` · chí mạng

- **Vai trò:** chí mạng, gõ chuẩn (T2, T3); 128–192 ms; ±80 cent, ±1 dB. `hit.sub` (đề xuất): sub dùng chung, mã thêm từ T2.
- **Anh đã nghe:** chọn v2 ít sub (3/5); bản nặng sub nhất 1/5. Luật `t-hit-boom`: dưới 150 Hz không quá 70 %.
- **Nguồn:** `hit.t2` = đầu tiếng + thân: Stable Audio 3 thô ("heavy bullet impact on thick steel armor, clank") có cửa sổ, hoặc đầu Kenney Impact Metal heavy trên thân Stable Audio 3. `hit.sub`: `sub_thump` 85→45 Hz, 90 ms, bão hòa 3 dB, 1 file (2 bản thử).
- **Tham chiếu:** 0a v2 (`e169bbdd`).
- **Biến thể:** 4 + 1.
- **Kiểm nhận:** bản ghép `hit.t2` + `hit.sub` có 35–55 % dưới 150 Hz; mất trên loa nhỏ ≤ 5 dB; nặng và dài hơn `hit.t1` rõ ràng (bài I). Anh nghe bản ghép sẵn, từ 3/5.

#### #14 `hit.t4` + `hit.tail` · đòn lớn

- **Vai trò:** T4 trở lên, thép dầm ngân, 720–1080 ms. `hit.tail` (đề xuất): đuôi kim loại dùng chung, mã thêm từ T4; cũng là chất liệu của `gun.xung.tail`.
- **Anh đã nghe:** chưa.
- **Nguồn:** `hit.t4` đầu + thân: Stable Audio 3 ("massive impact on a steel beam, deep thump"), cửa sổ 300 ms. `hit.tail`: bộ phát mẫu VCSL Anvil, Brake Drum (VSCO-2-CE `BrakeDrum1`, `Anvil`) cộng vang sảnh tổng hợp, 600–900 ms.
- **Biến thể:** 3 + 1–2.
- **Kiểm nhận:** `hit.tail` không ngân ở 1–4 kHz quá 300 ms trên −30 dB; T1 → T2 → T4 to dần và dài dần (bài I); ghép đủ lớp vẫn dưới 70 % năng lượng dưới 150 Hz.

#### #15 `kill.swarm` · bầy quái vỡ

- **Vai trò:** hàng trăm lần mỗi trận, gom theo ô; tối đa 4 trong 120 ms; 200–300 ms; ±300 cent, ±3 dB; họ bẩn. Nốt `kill.chime` tách riêng.
- **Anh đã nghe:** chưa. Mang theo hướng chung: sáng, ít sub, nhiều tiếng vỡ nhỏ.
- **Nguồn:** Stable Audio 3 ("small metal creature shattering, crunchy breaking metal, scattering shards, low boom"), cửa sổ 250 ms, bỏ phần ngân có cao độ. `kill.chime`: lô 1 giữ tổng hợp trong mã. Thang leo tới 28 bán cung nên một file không đủ; nếu làm file thì 3 nốt gốc (C5, C6, C7).
- **Biến thể:** 8.
- **Kiểm nhận:** không có cao độ ổn định quá 200 ms; dưới 150 Hz ≤ 40 %; 8 bản khác nhau trong khoảng P10–P90 của các họ Kenney Impact; bài D (40 con chết trong 120 ms): không clip, mức ép ≤ 3 dB. Đây là âm chữ ký của bảng phong cách: phiên S4 đặt 2 hướng (vỡ khô, vỡ có vang) cạnh nhau.

#### #16 `kill.elite` · lính tinh nhuệ nổ

- **Vai trò:** 400–600 ms, 3 biến thể, họ bẩn.
- **Nguồn:** Stable Audio 3 ("large armored machine creature exploding, heavy metal tearing, deep boom") cộng tia điện tổng hợp (numpy, 2–8 kHz).
- **Kiểm nhận:** tiếng thịch 60–150 Hz; dưới 150 Hz ≤ 70 %; nghe khác hẳn `kill.swarm`; tia điện không vượt mức P90 độ chói của âm tham chiếu.

#### #17 `word.load` · nạp băng đạn

- **Vai trò:** gõ xong một từ; "cạch-chắc"; 200–300 ms; ±20–30 cent; đang ở bus `alerts` (chỉ hạ −2 dB). Cùng mốc với giọng đọc và với viên đầu của loạt.
- **Anh đã nghe:** chưa.
- **Nguồn:** Stable Audio 3 ("heavy rifle magazine slammed into a steel receiver, two-part ka-chunk with a latch click") cộng Kenney RPG `metalLatch`, `metalClick`.
- **Biến thể:** 3.
- **Kiểm nhận:** hai nhịp cách nhau 40–70 ms là **cố ý**: đặt `expected_onsets: 2` để cờ hai đầu tiếng không loại nhầm. Luật mục 6.2 (1–4 kHz giảm 15 dB trong 100 ms). Trong "Liên thanh 3 s": giọng đọc vẫn cao hơn 10 dB ở 1–4 kHz. Âm chữ ký: phiên S4 đặt 2 hướng.

#### #18 `word.perfect` · nạp chuẩn

- **Vai trò:** như `word.load`, thêm tiếng nạp điện rít lên và vài tia lửa; 360–540 ms; 2 biến thể.
- **Nguồn:** `word.load` cộng tiếng rít tổng hợp. Tiếng rít của mã hiện tại đi 620 → 1.900 Hz, ngay giữa dải giọng: bản file đặt tiếng rít dưới 1 kHz hoặc trên 4 kHz, tia lửa trên 5 kHz.
- **Kiểm nhận:** luật mục 6.2; nếu vẫn trượt bài C thì ghi "giọng chờ 150 ms" vào thẻ.

#### #19 `gun.tia.pulse` · tia điện chích

- **Vai trò:** mỗi nhịp 0,1 s của Tia có trúng quái; 40–60 ms; ±150 cent; họ bẩn. Tia cũng là âm phát liền, nên ghi chú "liên thanh" áp ở đây.
- **Nguồn:** tổng hợp numpy, pedalboard (tách điện 2–8 kHz, ù 50/100 Hz), cộng kết cấu Stable Audio 3 ("electric arc crackle burning through metal").
- **Biến thể:** 6 (thẻ cho 4–8).
- **Kiểm nhận:** ở "Liên thanh 3 s" (Tia 10 nhịp mỗi giây): chỗ trũng ≤ 12 dB khi có ù nền; năng lượng 2–5 kHz dưới mức P90 khi đông quái. Mã hiện tại có lỗ hổng riêng: tiếng ù của Tia chỉ dài 0,6 s trong khi Tia kéo dài 2,5 s (mục 5, T6). Đề xuất id mới `gun.tia.loop` cho bước sau.

#### #20 `hurt.breach` · tuyến bị phá

- **Vai trò:** báo nguy chính; 480–720 ms; một bản cố định.
- **Nguồn:** Stable Audio 3 ("station hull breach, deep boom, groaning stressed steel") cộng còi hai nốt tổng hợp (440/330 Hz, vuông lọc thấp, mỗi nốt 90 ms).
- **Kiểm nhận:** còi chỉ là hai nhịp ngắn, không ngân ở 1–4 kHz; dưới 150 Hz ≤ 70 %; nghe khác `hurt.hull`. Anh từ 3/5.

### 4.2 Rồng Giữ Ải (rừng thần thoại vẽ tay)

Gốc prompt: *painterly fantasy forest, warm, organic, outdoor*. Lớp chữ ký: than hồng lách tách và đàn hạc. Đã có `FileBank`, nên đây là game ghép file sớm nhất ở bước nối.

#### #1 `fire.cast` · Hỏa Long khạc lửa

- **Vai trò:** gõ xong từ có mục tiêu; cùng mốc với giọng đọc (mục 6.2); 272–408 ms; ±30 cent; bus `world`.
- **Anh đã nghe:** chưa. Âm chữ ký của bảng phong cách.
- **Nguồn:** Stable Audio 3 thô ("dragon short throaty spit with a deep fireball whoomph launch, no laser hiss") 4 × 6 seed, có cửa sổ. Lớp gầm thú thêm sau (chờ anh tải Freesound CC0 hoặc tự gầm).
- **Tham chiếu:** thân lửa của `fire.impact.a` 0b (`77e0dd55`) cho chất lửa.
- **Biến thể:** 4.
- **Kiểm nhận:** lên ≤ 10 ms; dưới 150 Hz ≤ 50 %; 1–4 kHz giảm 15 dB trong 100 ms; kịch bản `dh-cast-chain`: giọng đọc cao hơn 10 dB ở 1–4 kHz. Phiên S2 đặt 2 hướng (phụt tròn, khạc có hơi thở).

#### #2 `fire.impact.a` · cầu lửa trúng (mẫu của họ)

- **Vai trò:** đòn trúng nghe nhiều nhất; gom 45 ms; xen kẽ với `.b`; 272–408 ms; ±80 cent.
- **Anh đã nghe:** 0a chọn bản dò v3 (55 % dưới 150 Hz) trên hai bản 84 %; 0b hai công thức Stable Audio 3 đều 3/5.
- **Nguồn:** công thức `fire.impact.a.sa3-r2` (đầu Kenney Wood heavy, thân lửa Stable Audio 3 họ B, sub 80→45 Hz, than hồng). Tạo thêm 24 thân họ B để có từ 8 thân không có hai đầu tiếng. Sub rút còn 90 ms và nhỏ đi 3 dB; đầu tiếng thử thêm `impactSoft_heavy`, `impactGeneric_light` cho sáng hơn.
- **Tham chiếu:** 0b v4 (`77e0dd55`), v2 (`af84aad3`); 0a v3 (`c58fa0c7`).
- **Biến thể:** 4 (thêm 2 dự phòng).
- **Kiểm nhận:** `t-hit-boom` (dưới 150 Hz 45–60 %, trần 70 %); lên ≤ 10 ms; một đầu tiếng; tắt xuống −60 dB trước 400 ms; mất trên loa nhỏ ≤ 6 dB. Anh từ 3/5, mục tiêu 4/5 ở `dh-cast-chain`.

#### #3 `fire.impact.b` · biến thể tối hơn

- **Vai trò:** như `.a`, tối hơn, có lách tách; 304–456 ms.
- **Nguồn:** công thức của `.a`, giữ đầu tiếng, đổi thân sang Stable Audio 3 prompt C ("warm deep flame burst, crackling embers"), 3–4 tiếng than hồng, dịch ±cent.
- **Biến thể:** 3.
- **Kiểm nhận:** cùng họ với `.a` (gần tâm bộ `.a` hơn tâm âm của game khác) nhưng phân biệt được (khoảng cách mel 0–50 ms trong P10–P90); dưới 150 Hz ≤ 60 %.

#### #4 `fire.impact.c` · bùng lửa lớn

- **Vai trò:** T3 trở lên, Hoàn hảo, Chớp; nhóm `blast`; 416–624 ms; mức trong bản trộn −16 đến −14.
- **Nguồn:** `.a` cộng tiếng bùng lửa Stable Audio 3 ("big fire burst, roaring flames") 300–500 ms, sub ≤ 150 ms.
- **Biến thể:** 3.
- **Kiểm nhận:** dưới 150 Hz ≤ 70 %; to và dài hơn `.a` rõ ràng; không có tiếng nổ thứ hai.

#### #5 `wave.horn` · tù và báo đợt

- **Vai trò:** báo đợt (P1), một bản cố định, 1,76–2,64 s.
- **Anh đã nghe:** chọn hai kèn co Rê–La (3/5); trombone 1–2/5.
- **Nguồn:** bộ phát mẫu VSCO-2-CE F Horn và trống khung VCSL. Ba ứng viên cùng hướng kèn co, khác hình câu: một hơi dài; hai hơi (ngắn, dài); một hơi có trống đôi. Thêm chút vang rừng (gửi 0,16 như bus `stingers`).
- **Tham chiếu:** 0a v1 (`d6e963bf`).
- **Kiểm nhận:** đúng Rê–La; gộp mono; không có âm kéo dài 1–4 kHz trên mức cảnh báo cho phép; anh từ 3/5, mục tiêu 4/5.

#### #6 `general.g01.horn` · tù và của tướng

- **Vai trò:** G01 xuất hiện; trầm hơn `wave.horn`, mở dần, "gỗ, rêu", đáng sợ; 2,2 s.
- **Nguồn:** kèn co quãng thấp (không trombone: anh chấm trombone 1–2/5, mục 1.1) cộng kết cấu Stable Audio 3 ("low wooden war horn, mossy, swelling"). Chỉ dùng quãng năm Rê–La để không va với stem `general` (câu hỏi 16 #8 còn mở).
- **Biến thể:** 1 (2–3 ứng viên).
- **Kiểm nhận:** nghe khác `wave.horn` ngay nhịp đầu; không có Si hay Si giáng.

#### #7 `amb.forest` · gió rừng thông

- **Vai trò:** luôn chạy, nhỏ lại khi có đợt; vòng 6 s stereo; −26 LUFS-I.
- **Anh đã nghe:** chọn E s2006 sáng, xì qua lá kim (4/5) trên bản ù trầm (3/5). Chỉ nghe một vòng ở "Một mình", bằng loa.
- **Nguồn:** Stable Audio 3 prompt E, F (sáng, lá kim), 10 s, cắt vòng 6 s bằng `gen/process.py`. Ứng viên: E s2006 chuẩn hóa lại (tham chiếu); 2 seed mới của E/F; một bản E cộng 20 % lớp trầm kiểu H (để thử bằng tai nghe xem bản sáng thuần có mệt tai không).
- **Tham chiếu:** `10c80671`.
- **Kiểm nhận:** mối nối L1; `t-amb-forest-bright` (từ 30 % trên 3 kHz); độ to dao động ≤ 7 dB; không chim, không côn trùng; cân hai kênh. Anh nghe **3 vòng ở Lặp, bằng tai nghe**. Có nhãn "nhàm khi lặp" thì câu hỏi 16 #7 nghiêng về nền dài hơn (hai vòng 6 s xen nhau, hoặc 12 s).

#### #8 `amb.river` · suối

- **Vai trò:** luôn chạy khi bản đồ có suối; vòng 5 s; mức −18 dB so với nền rừng.
- **Nguồn:** Stable Audio 3, 4 × 6 seed, 10 s, cắt vòng 5 s.
- **Kiểm nhận:** như `amb.forest`; không có âm có cao độ lặp lại (bộ dò dấu vòng); nghe chung với `amb.forest` (hai nền cùng chạy).

#### #9 `enemy.swarm.march` · bầy lạo xạo

- **Vai trò:** vòng lặp khi có bầy, mono, 4 s, to theo số quái sống, mã đặt trái phải.
- **Nguồn:** Stable Audio 3 ("dense ant swarm skittering on leaves"), 10 s, cắt vòng 4 s.
- **Kiểm nhận:** mối nối; không có nhịp rõ ở tần số vòng (0,25 Hz); không che phím (dải 4–8 kHz dưới mức phím ở bài D).

#### #10 `enemy.quadruped.march` · vó chạy

- **Vai trò:** vòng lặp khi có thú, mono, 4 s.
- **Nguồn:** Stable Audio 3 ("several four-legged animals trotting on dirt, gallop triplets"), 10 s. Điểm cắt vòng đặt đúng ranh giới một chu kỳ phi.
- **Kiểm nhận:** mối nối; không có tiếng vó đôi ở chỗ nối; nhịp phi đều qua 3 vòng.

### 4.3 Lời Gọi (làng tre Việt)

Gốc prompt: *bamboo, wood, bronze, paper, Vietnamese village, dry, outdoor*. Lớp chữ ký: tre, chuông đồng, đàn tranh. Luật TK 22.1: không chuông chùa, không mõ chùa, không tụng. Chưa có bộ tải file, nên ghép vào game muộn nhất; nốt đàn tranh không cần AI nên làm được bất cứ lúc nào.

#### #21 `word-hit` · nốt đàn tranh sau mỗi từ

- **Vai trò:** gõ xong một từ; nốt theo bậc chuỗi. Mã hiện tại (`folk.ts` `note`) phát A4 cho từ ẩu và C5, D5, F5, G5, A5, C6 theo bậc. Hạ một quãng tám thành **A3, C4, D4, F4, G4, A4, C5** (7 file). Bản "Chớp" vuốt lên: mã đang trượt 1 bán cung trong 90 ms; làm bằng mã trên cùng file, hoặc dùng mẫu Gliss của VCSL.
- **Anh đã nghe:** C4 3/5 > C5 rung 2/5 > C5 1/5. Mục 16 #4 đã chốt C4–C5 (thẻ spec còn ghi C5–C6, chờ sửa).
- **Nguồn:** bộ phát mẫu VCSL Dan Tranh Normal (thật ra phủ B2–B5, nên mỗi nốt dời tối đa 1–2 bán cung); công thức 0a: tiếng gảy đủ dải 120 ms, phần ngân lọc thấp 1 kHz. Không dùng lối rung (2/5).
- **Tham chiếu:** `e79e84d1`.
- **Kiểm nhận:** cao độ lệch ≤ 10 cent; luật mục 6.2; AST "Zither". Anh nghe cả thang theo thứ tự bậc trong kịch bản `td-wordhit-chain`, có giọng đọc. Không được nghe như đàn tranh Trung Quốc.

#### #22 `word-hit-bell` · chuông khi Hoàn hảo, Chớp

- **Vai trò:** thêm khi Hoàn hảo hoặc Chớp; 0,5 s; cố định.
- **Anh đã nghe:** Hand Chimes dùng được cho UI (A5 3/5). Tubular Bells chưa nghe (16 #5 còn mở).
- **Nguồn:** ba ứng viên: VCSL Hand Chimes C7 và A6, VSCO-2-CE Tubular Bells `TB_hit_C5`. Nốt chuông nào cũng nằm gần dải giọng (C7 là 2.093 Hz, đúng nốt mã hiện tại dùng), nên tách hai lớp như `word-hit`: tiếng "ting" đủ dải chỉ giữ 100 ms, phần ngân dài chỉ giữ họa âm trên 4 kHz hoặc dưới 1 kHz. Tubular Bells không đo được cao độ tin cậy: chỉ dùng sau khi anh nghe.
- **Kiểm nhận:** luật mục 6.2 (phần 1–4 kHz giảm 15 dB trong 100 ms); không đạt mà anh vẫn thích thì ghi "giọng chờ 150 ms" cho bậc Hoàn hảo, Chớp. Nằm trong thang Hò–Xự–Xang–Xê–Cống; anh duyệt văn hóa (không chuông chùa).

#### #23 `wordshot-fire` · Phát Chữ bay ra

- **Vai trò:** mỗi lần bắn chữ; 144–216 ms; ±100 cent.
- **Nguồn:** Stable Audio 3 ("a fast bamboo arrow whoosh with a dry paper flutter") cộng tiếng giấy (Kenney RPG `bookFlip`). File mono; mã đặt trái phải.
- **Biến thể:** 4.
- **Kiểm nhận:** lớp đầu tiếng là tiếng vút: thẻ đổi `onset.class` sang "whoosh" (mục 4.3.1 không kiểm thời gian lên của tiếng vút); CLAP nghiêng tre, giấy, không laser, không kim loại.

#### #24 `arrow-fire` · Tháp Cung bắn

- **Vai trò:** tối đa 4 lần mỗi giây mỗi game; nhẹ, nền; 64–96 ms.
- **Nguồn:** Stable Audio 3 ("a soft twang of a small bamboo bow string, very short, quiet"); tự ghi tiếng dây cung tre là phương án sau.
- **Biến thể:** 4.
- **Kiểm nhận:** −24 đến −18 trong bản trộn; không gắt ở 2–5 kHz. Ở `td-wordhit-chain` (3 tháp): nhịp đều, không thành từng cụm rồi im (mã hiện tại gây ra cụm, mục 5, L1). Âm chữ ký: phiên S5 đặt 2 hướng.

#### #25 `ink-puff` · Mực Câm tan

- **Vai trò:** tối đa 8 lần mỗi giây, 3 mỗi khung; mềm, không máu; 120–180 ms; ±300 cent, ±3 dB.
- **Nguồn:** Stable Audio 3 ("a soft puff of an ink-soaked paper bag popping, muffled").
- **Biến thể:** 6.
- **Kiểm nhận:** không có tiếng tách nổi trên 6 kHz; dưới 150 Hz nhỏ; 8 lần mỗi giây không thành tiếng rè. Âm chữ ký: phiên S5 đặt 2 hướng.

#### #26 `blast` · tiếng nổ trống và giấy

- **Vai trò:** Tháp Pháo, cụm Phát Chữ; tối đa 2 mỗi khung; 320–480 ms.
- **Nguồn:** VCSL Frame Drum hoặc VSCO-2-CE Timpani qua bộ phát mẫu, cộng Stable Audio 3 ("a burst of paper scraps and dust"). Không nổ lách tách, không chất taiko.
- **Biến thể:** 3.
- **Kiểm nhận:** dưới 150 Hz ≤ 70 %; không tiếng lách tách; AST "Drum" hoặc "Wood", không "Explosion" đứng đầu.

#### #27 `coin` · đồng xu rơi

- **Vai trò:** tối đa 3 lần mỗi giây; 240–360 ms.
- **Nguồn:** Kenney RPG `handleCoins` (va chạm) cộng VCSL Hand Chimes (nốt ngũ cung cao, đã được anh chấp nhận cho UI).
- **Biến thể:** 4.
- **Kiểm nhận:** tiếng ngân trên 4 kHz hoặc tắt nhanh trong 1–4 kHz (âm dày giữa trận); không nhàm ở 3 lần mỗi giây. Âm chữ ký: phiên S5 đặt 2 hướng.

#### #28 `leak` · quái lọt Lũy

- **Vai trò:** báo nguy, cách nhau ít nhất 0,8 s; một bản cố định; 1,2 s.
- **Anh đã nghe:** kẻng sắt Anvil ba nhát 4/5 > cồng 3/5. Đã chốt kẻng (16 #5).
- **Nguồn:** công thức 0a, bản kẻng (bộ phát mẫu VCSL Anvil, sub nhẹ, khoét 1–4 kHz). Chỉ hoàn thiện: nhịp ba nhát, đuôi, mức. Thêm một ứng viên có trống hội nhỏ bên dưới.
- **Tham chiếu:** `0d842a87`.
- **Kiểm nhận:** −17 đến −14 trong bản trộn; anh xác nhận bản cuối không thấp hơn 4/5.

### 4.4 Làm lại ngoài danh sách 28

| Id | Vì sao | Làm gì | Kiểm nhận |
|---|---|---|---|
| `enemy.quadruped.howl` | Âm chữ ký của Rồng Giữ Ải; bản trọn tiếng 3/5 bị luật đầu tiếng chặn (Q3) | Stable Audio 3 prompt B, tạo 2–3 s, giữ trọn tiếng gọi (`--whole`); tham chiếu `b9ef6989`; 3 biến thể. Cần `attack_max_ms: 150` sau khi sửa mục 4.3.1 | Tiếng gọi 0,9–1,3 s; lớn dần ≤ 150 ms; AST Howl hay Animal, không Speech; anh nghe kỹ cờ rít cuối tiếng (máy gắn ở cả hai bản 0b, anh không gắn) |
| `call-chop` | Q2: cấm mõ; máy cũ xếp bản mõ thứ 5/41 | Prompt A, E, F, G; 4 × 6 seed; bỏ bản có hai đầu tiếng sát nhau; tham chiếu `1bbffcc4`, `3e5ee6dc` | `t-call-chop-knock` (từ 30 % dưới 300 Hz); không "sai chất liệu"; anh từ 3/5 |
| `ui-move` | Máy vẫn sai ở id này (0/3 cặp) | Bản cuối từ trống khe VCSL Slit Drum, 40 ms; tham chiếu `ea8b0706` | Lên ≤ 3 ms; anh xác nhận |
| `ui-pick` | Hướng đã chọn (A5) | Bản cuối phách gỗ + Hand Chimes A5; tham chiếu `2b7be772` | Anh xác nhận |
| `trap.pine-bomb.trigger` | 3/5, "sửa nhẹ"; làm nếu còn thời gian | Thêm 2 ứng viên Stable Audio 3 cạnh công thức v3; tham chiếu `19438fdb` | Nứt 2–8 kHz trong 30 ms đầu; mất trên loa nhỏ ≤ 6 dB |

---

## 5. Mã phát trong game: chỗ làm tiếng liền thành rời

Đọc ngày 24/10/2026, chỉ đọc. Sửa ở bước nối âm vào game, không phải bây giờ. Số dòng theo bản hiện tại.

### Tuyến Cuối (`games/typing-survival`)

| # | Chỗ | Vì sao nghe ngắt quãng hoặc mất lực | Sửa ở bước nối |
|---|---|---|---|
| T1 | `src/view/combat.ts:139` `if ((this.shots++ & 1) === 0) this.audio.shot(…)` | Súng bắn 10 viên mỗi giây (11,5 khi gõ nhanh), tiếng chỉ phát cho viên chẵn: tai nghe nửa nhịp của mắt | Phát mọi viên, bộ A và B xen nhau (mục 3.3) |
| T2 | `src/audio/theme-audio.ts:185–191` `shot()` | Sin 90 ms, nhiễu 35 ms và 70 ms, tắt hàm mũ về 0,0001: mỗi phát hết sau khoảng 100 ms, còn lại là lặng | File có đuôi chồng phát sau, cộng `gun.xung.loop` |
| T3 | `src/audio/theme-audio.ts:107–118` nén mỗi bus (ngưỡng −12 dB, tỉ lệ 8, bắt 2 ms, nhả 140 ms) | Mỗi phát vượt ngưỡng; bắt 2 ms ép mất đầu tiếng (mất lực); nhả 140 ms so với nhịp 100–200 ms làm mức bơm theo nhịp bắn | Bus súng và trúng: bắt 10–20 ms, nhả 250–400 ms, một phát ép ≤ 2 dB; hoặc chỉ một bộ giới hạn ở master |
| T4 | `src/audio/theme-audio.ts:145` `at: ctx.currentTime`; `src/sim/weapons.ts:78` vòng `while` bắn nhiều viên trong một bước | Mọi tiếng bắt đầu ở đầu khung hình đang đọc sự kiện: lệch tới 16,7 ms; sau một khung giật, nhiều viên chồng cùng lúc rồi im | Mang thời điểm mô phỏng theo sự kiện, đặt lịch `ctx.currentTime + trễ cố định + (t_sự_kiện − t_khung)` |
| T5 | `src/sim/weapons.ts:80` súng ngừng khi không có mục tiêu; hết băng | Không có sự kiện "bắt đầu, ngừng loạt", nên không có chỗ để bật nền và đuôi | Thêm sự kiện bắt đầu và ngừng loạt (hoặc suy từ `G.rounds`, `G.mags` ở view) |
| T6 | `src/audio/theme-audio.ts:198–201` tiếng ù của Tia 0,6 s; `:212` `pulse()` im khi không trúng ai; Tia kéo dài 2,5 s (`TIA.seconds`) | Tia đang hiện mà phần lớn thời gian không có tiếng | Thêm nền `gun.tia.loop` chạy suốt Tia |
| T7 | `src/audio/theme-audio.ts:238` tiếng trúng 80–100 ms | Ở 10 lần mỗi giây, chuỗi trúng cũng rời rạc | File `hit.t1` có đuôi tắt dần tự nhiên; nền súng gánh phần liền |
| T8 | `src/audio/theme-audio.ts:78` `sounds: {}` | Chưa có file nào; khi có file sẽ đi qua `SceneAudio` với các giới hạn ở K1–K6 | Nâng kit trước (mục 6.3 #1) |

### Kit (`shared/game-kit`, bản chép trong `games/*/src/kit`)

| # | Chỗ | Vấn đề | Sửa |
|---|---|---|---|
| K1 | `audio/scene-audio.ts:186–187` `start()` bỏ qua khi file chưa giải mã | Những phát đầu sau khi mở khóa âm bị câm | Giải mã sẵn trước trận; tiếng tổng hợp thay chỗ cho tới khi file sẵn sàng |
| K2 | `audio/scene-audio.ts:84` mỗi id một URL | Không có biến thể: cùng một file 10 lần mỗi giây ("hiệu ứng súng máy" lặp y hệt) | Danh sách biến thể, xoay vòng ngẫu nhiên không lặp 2 bản gần nhất |
| K3 | `audio/scene-audio.ts:193` tốc độ phát ×U(0,95; 1,05) cho mọi âm | Khoảng ±85 cent cho cả âm thưởng và UI; đổi cả độ dài | Lệch theo nhóm (mục 5.3); súng A ±40, B ±70 cent |
| K4 | `audio/scene-audio.ts` không có trần tiếng, không cướp tiếng | Không có lỗi ngắt quãng, nhưng không có gì giữ trần 4 tiếng mỗi vũ khí | Trần theo nhóm, cướp tiếng cũ nhất với mờ 20–30 ms |
| K5 | `audio/scene-audio.ts:240–262` vòng lặp chỉ có `playMusic`, nối thẳng ra loa (`:260`) | Không có cách chạy nền âm hiệu ứng trên một bus | Thêm `startLoop(id, bus)` và `stopLoop(id, fadeMs, tailId)` |
| K6 | `audio/scene-audio.ts:105–112` hạ tiếng khi giọng đã cất lên | Giọng qua mạng đến muộn: tiếng súng che đầu từ | Hạ từ lúc gửi yêu cầu đọc (mục 6.2 bước 4) |
| K7 | `feedback/audio-cues.ts:204–209` phát bắn 35–50 ms; `:80–84` giới hạn ngưỡng −10 dB, bắt 2 ms, nhả 120 ms | Cùng kiểu lỗi như T2, T3. Hiện chỉ Space Typing (đấu đôi) dùng | Sửa như T2, T3 nếu một game mới dùng lại |

### Rồng Giữ Ải (`games/dragon-hold`)

| # | Chỗ | Vấn đề | Sửa |
|---|---|---|---|
| D1 | `src/audio/engine.ts:67` độ dài tiếng lấy từ `lengthMs` của bản tổng hợp | Khi file có đuôi dài hơn, bảng tiếng sai; tiếng bị coi là đã tắt (mục 6.3 #4) | Nhận độ dài thật của file trước khi xin chỗ |
| D2 | `src/audio/limiter.ts:189` chỉ cướp tiếng kém quan trọng hơn hẳn | Khi 32 chỗ đầy tiếng P4, cú trúng P4 mới bị từ chối: lỗ hổng giữa đợt đông | Cho cướp tiếng cùng hạng đã qua phần đầu (cũ hơn 120 ms), mờ 25 ms |
| D3 | `src/audio/bank.ts:128` `FileBank` xoay vòng đúng thứ tự | Vòng a, b, c, a, b, c nghe ra được | Ngẫu nhiên, không lặp 2 bản gần nhất |
| D4 | `src/audio/engine.ts:61` ±4 % cao độ cho mọi âm `world`, `enemies` | Không theo nhóm | Theo nhóm (mục 5.3) |
| D5 | `src/audio/mixer.ts:15` giới hạn master −3 dB, tỉ lệ 20, bắt 2 ms, nhả 120 ms | Có thể bơm khi tiếng trúng bằng file to hơn | Kiểm ở bài D; nới bắt và nhả nếu mức ép quá 3 dB hơn 5 % thời gian |
| D6 | `src/audio/map-events.ts:272` `fire.cast` cùng sự kiện với giọng đọc | Che đầu từ (mục 6.2) | Luật âm xong từ; hạ từ lúc gửi yêu cầu đọc |

### Lời Gọi (`games/typing-defense`)

| # | Chỗ | Vấn đề | Sửa |
|---|---|---|---|
| L1 | `src/view/audio-min.ts:133–137` `room()` đếm trong cửa sổ trượt 1 s | Tên bắn, mực tan, xu thành từng cụm: 4 tiếng đầu phát rồi im tới hết giây | Khoảng cách tối thiểu (tên 250 ms, mực 125 ms, xu 333 ms) hoặc thùng thẻ nạp đều; tỉa đều thay vì cắt đuôi |
| L2 | `src/view/audio-min.ts:159` mọi tiếng bắt đầu ở `ctx.currentTime` của khung | Các sự kiện cùng khung chồng đúng một thời điểm | Đặt lịch theo tick của sự kiện |
| L3 | Chưa có bộ tải file | — | Mục 6.3 #6 |

---

## 6. Thứ tự sản xuất

Mỗi bước chạy hết rồi mới sang bước sau. Trong một bước: tạo bằng Stable Audio 3 → xử lý → dựng công thức → chấm (tiến trình riêng, sau khi Stable Audio 3 đã tắt) → dựng bối cảnh → lập phiên. Không bao giờ chạy Stable Audio 3 và bộ chấm cùng lúc, không chạy hai tiến trình tạo cùng lúc. Máy ở lô 0b: 24 ứng viên mất 17–25 s khi mô hình nằm sẵn; bộ chấm khoảng 1 s mỗi file.

| Bước | Việc | Mô hình nặng | Ra | Phiên |
|---|---|---|---|---|
| **P0** công cụ | Module `context` và 3 kịch bản; bối cảnh "Liên thanh 3 s" và nhãn "ngắt quãng" trên Bảng Nghe; chặn prompt cấm trong `gen.sa3`; thẻ spec đề xuất `gun.xung.loop`, `gun.xung.tail` (`PLAN_PROPOSED` như `hit.sub`); `expected_onsets` cho `word.load`. Chạy bài thử trên 0a v2 và 0b v1: phải ra lại số đo của mục 1.2 (khoảng 75 % thời gian hổng) trước khi tin nó | Không | Mã và kiểm thử trong `tools/audio-lab`; bản dựng thử ở `~/AudioLab/work/_context/` | — |
| **P1** Tuyến Cuối súng và trúng | `gun.xung`, `gun.xung.loop`, `gun.xung.tail`, `hit.t1`, `hit.sub`, `hit.t2`, `hit.t4`, `hit.tail` | Stable Audio 3, rồi bộ chấm | 3 hướng súng dựng ở "Liên thanh 3 s"; các bậc trúng ghép sẵn | **S1** |
| **P2** Rồng Giữ Ải trận đánh | `fire.cast`, `fire.impact.a`, `.b`, `.c`, `enemy.quadruped.howl` (làm lại), `trap.pine-bomb.trigger` (nếu còn thời gian) | Stable Audio 3, rồi bộ chấm | Kịch bản `dh-cast-chain` | **S2** |
| **P3** Rồng Giữ Ải nền và báo đợt | `amb.forest`, `amb.river`, `enemy.swarm.march`, `enemy.quadruped.march`, `wave.horn`, `general.g01.horn` | Stable Audio 3 (10 s), rồi bộ chấm | Vòng lặp đã kiểm mối nối; kèn qua bộ phát mẫu | **S3** |
| **P4** Tuyến Cuối phần còn lại | `kill.swarm`, `kill.elite`, `word.load`, `word.perfect`, `gun.tia.pulse`, `hurt.breach` | Stable Audio 3, rồi bộ chấm | `ts-xung-3s` có thêm hạ quái và nạp đạn thật | **S4** |
| **P5** Lời Gọi | `word-hit` (7 file), `word-hit-bell`, `wordshot-fire`, `arrow-fire`, `ink-puff`, `blast`, `coin`, `leak`, `call-chop` (làm lại), `ui-move`, `ui-pick` | Bộ phát mẫu (không nặng); Stable Audio 3 cho tiếng vút, tên, mực, giấy, `call-chop`; rồi bộ chấm | Kịch bản `td-wordhit-chain` | **S5**, **S6** |

**Vì sao súng đi trước** (mục 9 đặt Rồng Giữ Ải trước vì ghép file sớm nhất): ghi chú duy nhất của anh là về súng; súng là âm phát dày nhất của cả ba game; `hit.tail` dùng chung cho súng và bậc trúng; và bài thử "Liên thanh" cần được kiểm trên đúng ca khó nhất trước khi dùng cho game khác. Nối âm vào game là bước sau và phụ thuộc các làn khác, nên thứ tự sản xuất không làm chậm việc ghép. Nếu người điều phối muốn theo thứ tự ghép, đổi P1 với P2, P3; chỉ P0 phải đi trước.

**Sau mỗi phiên:** đọc điểm, chạy `critic agreement --batch 1`, ghi quyết định vào `DECISIONS.md`. Bản được chọn từ 3/5 vào lượt biến thể (mục 5.1 bước 9–10), rồi vào `~/AudioLab/review/staging/<game>/` khi anh duyệt. Lượt biến thể khoảng 30 s mỗi id, ghép vào đầu phiên kế tiếp.

---

## 7. Phiên nghe

| Phiên | Game | Id | Bối cảnh chính | Thiết bị | Thời gian |
|---|---|---|---|---|---|
| S1 | Tuyến Cuối | Họ súng (3 hướng), `hit.t1`, `hit.t2` + sub, `hit.t4` + đuôi; cặp mốc 0a v2 | **Liên thanh 3 s**, rồi Một mình | Tai nghe, rồi loa một lượt cho súng | 20 phút |
| S2 | Rồng Giữ Ải | `fire.cast` (2 hướng), `fire.impact.a/b/c`, tiếng tru, Bom Hạt Thông | Trận thô `dh-cast-chain`, Lặp | Tai nghe | 15 phút |
| S3 | Rồng Giữ Ải | `amb.forest`, `amb.river`, hai vòng hành quân, `wave.horn`, `general.g01.horn` | Lặp liền 3 vòng, Một mình | Tai nghe | 20 phút |
| S4 | Tuyến Cuối | `kill.swarm` (2 hướng), `kill.elite`, `word.load` (2 hướng), `word.perfect`, `gun.tia.pulse`, `hurt.breach`; lượt biến thể của S1 | Liên thanh 3 s, Một mình | Tai nghe | 15 phút |
| S5 | Lời Gọi | Thang `word-hit`, `word-hit-bell`, `wordshot-fire`, `arrow-fire` (2 hướng), `ink-puff` (2 hướng), `blast`, `coin` (2 hướng) | `td-wordhit-chain`, Lặp | Tai nghe | 20 phút |
| S6 | Lời Gọi | `leak` bản cuối, `call-chop`, `ui-move`, `ui-pick`; duyệt văn hóa chuông | Một mình | Loa | 10 phút |

Mỗi phiên tối đa 10 id và 20 phút, có 4–6 cặp mốc. Tổng khoảng 100 phút cộng các lượt biến thể: khoảng 2 giờ, đúng ước tính của mục 0 trong kế hoạch.

Bảng phong cách (mục 9 bước 2) rút gọn vào các phiên trên: lô 0a, 0b đã chọn hướng cho 6/12 âm chữ ký (`fire.impact.a`, tiếng tru, `amb.forest`, `gun.xung`, `hit.t1`, `word-hit`); 6 âm còn lại chưa nghe (`fire.cast`, `kill.swarm`, `word.load`, `arrow-fire`, `ink-puff`, `coin`) được đặt 2 hướng cạnh nhau trong phiên của game đó. Nền nhạc thô (mục 6.1) chưa có: các bản dựng bối cảnh chưa có nhạc; bài C, D chạy lại khi có nhạc.

---

## 8. Việc của người điều phối

1. **Duyệt bản này**, rồi giao P0.
2. **`THEME_SOUND_LIST.md` của Tuyến Cuối** (lượt sửa game): thêm `gun.xung.loop`, `gun.xung.tail`, `hit.sub`, `hit.tail`, và về sau `gun.tia.loop`; ghi `gun.xung` là "đầu 120 ms, đuôi tắt dần tới 350 ms" thay cho "120 ms"; ghi súng phát mọi viên với hai bộ nhấn.
3. **`AUDIO_PIPELINE.md`:**
   - mục 4.3.3, hàng "Bắn, khạc": thêm thân 150–500 Hz từ 25 %, mất trên loa nhỏ ≤ 4 dB; nới "từ 25 % dưới 150 Hz" thành 20–40 % (anh nghe bằng loa, bản 82 % dưới 150 Hz mất 7,6 dB);
   - mục 6.1: thêm bài thử "Liên thanh" (mục 3.5 ở đây);
   - mục 7: bối cảnh "Liên thanh 3 s", nhãn "ngắt quãng";
   - mục 9: các id mới và thứ tự P1–P5;
   - các mục đã ghi trong `DECISIONS.md` (3.2, 4.3.1, 4.5, 8.2, 16).
4. **Thẻ spec:** `word-hit` đổi nốt thành A3, C4, D4, F4, G4, A4, C5; `attack_max_ms: 150` cho tiếng gọi trọn sau khi sửa mục 4.3.1; `wordshot-fire` đổi `onset.class` sang tiếng vút.
5. **Bước nối âm vào game** (sau các làn đang làm game): danh sách T1–T8, K1–K7, D1–D6, L1–L3 ở mục 5.

**Câu hỏi còn mở cho anh** (trả lời ngay trong phiên, không chặn sản xuất):

- Nền liên thanh nên rõ tới đâu: hướng 2 (nền nhỏ) hay hướng 3 (nền to) ở S1.
- Tubular Bells hay Hand Chimes cho `word-hit-bell` (S5).
- `amb.forest` vòng 6 s có nhàm không khi nghe 3 vòng bằng tai nghe (S3, câu hỏi 16 #7).
