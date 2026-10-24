# context: âm trong bối cảnh trận

Dựng một đoạn trận ngắn để nghe một ứng viên **như trong game**: cùng các âm khác của cảnh, qua bộ trộn giống game, có giọng đọc từ. Hợp đồng: mục 3.5 của [`BATCH1_BRIEF.md`](../BATCH1_BRIEF.md), bài C, D, F ở mục 6.1 và luật mục 6.2 của [kế hoạch](../../../docs/games/AUDIO_PIPELINE.md). Chỉ numpy, scipy, soundfile, soxr; không mô hình nặng.

## Lệnh

```bash
R=tools/audio-lab/run.sh
bash $R context scenarios                       # dh-*, ts-*, td-wordhit-chain, td-night, td-menu
bash $R context voices                          # ghi giọng macOS một lần vào ~/AudioLab/work/_context/voices
bash $R context render --scenario dh-cast-chain --slot fire.cast=A.wav --slot fire.impact.a=B.wav \
    --slot amb.forest=C.wav --focus fire.cast --out ~/AudioLab/work/_context/thu/a.wav
```

Mỗi lần dựng ra `<tên>.wav` (48 kHz 24-bit stereo, đã hạ chung −4 dB để gần mức −23 LUFS-M của Bảng Nghe), `<tên>.json` (dòng thời gian, mức đặt, số đo) và `<tên>.png` (đường mức của bản trộn, của ứng viên và của giọng; dải 1–4 kHz; mức ép của bộ giới hạn và mức hạ tiếng từng bus).

## Bộ trộn (`mixer.py`)

Số lấy từ mã âm của game (chỉ đọc). Rồng Giữ Ải (`games/dragon-hold/src/audio/mix.ts`, `mixer.ts`):

| Phần | Giá trị |
|---|---|
| Hạ tiếng khi đọc | world −6, enemies −6, traps −6, ambience −4, stingers −2, dragon −3 dB; xuống 80 ms, lên 400 ms (`setTargetAtTime`, tau = thời gian / 3) |
| Vang rừng | đúng bộ sinh `forestImpulse` (0,9 s, cùng LCG), gửi world 0,12, enemies 0,14, traps 0,12, stingers 0,16; trả về 0,4; chuẩn hóa như `ConvolverNode` của Chromium |
| Master | bộ nén −3 dB, tỉ lệ 20, bắt 2 ms, nhả 120 ms, bù mức tự động của Chromium; rồi bộ chặn mềm (thẳng tới 0,8, gối tanh tới 0,96) |
| Giọng đọc | `speechSynthesis` nằm ngoài đồ thị âm của game: cộng sau master, không bị hạ, không bị nén |

- **Mức đặt:** mỗi âm đặt ở giữa khoảng "Mức trong bản trộn" của thẻ spec (mục 4.3.3); nền rừng −26 LUFS-I, các nền khác theo chênh lệch `gainDb` của `catalog.ts` (suối −8, bầy −7, thú −6 dB so với rừng). Vì vậy mọi ứng viên của một id ngồi cùng một mức, chỉ âm là khác.
- **Hai cấu hình hạ tiếng:** `request` (đề xuất, mục 6.2 bước 4: hạ từ lúc game xin đọc) và `voice` (hiện tại: hạ khi giọng cất lên).
- **Xấp xỉ:** bộ nén là bộ dò đỉnh có làm mượt bắt/nhả, không có nhìn trước 6 ms và nhả thích nghi của Chromium. Báo cáo nào cũng ghi câu này.

## Kịch bản Rồng Giữ Ải (`scenes.py`)

| Kịch bản | Dài | Có gì |
|---|---|---|
| `dh-cast-chain` | 9,6 s | Nền rừng; 6 từ, mỗi 1,5 s (40 WPM): `fire.cast` cùng lúc với yêu cầu đọc, giọng đọc sau 150 ms, cầu lửa trúng 0,6 s sau, theo lượt a, b, c (đòn to ở từ thứ 3 và 6) |
| `dh-pack` | 8 s | Nền rừng; vó thú vào từ 0,6 s; tiếng tru ở 1,0 s và 4,6 s; ba từ có cầu lửa |
| `dh-trap` | 7 s | Nền rừng, bầy lạo xạo; bốn từ; Bom Hạt Thông nổ ở 2,2 s và 5,2 s |
| `dh-beds` | 18 s | Nền rừng 3 vòng, suối; tù và báo đợt ở 3 s; bầy và thú vào dần; tù và tướng G01 ở 9,5 s; bốn từ có cầu lửa từ 12 s |

Một bản dựng thay đúng một chỗ (`--focus`) bằng ứng viên, các chỗ khác giữ nguyên. Độ lệch cao độ, mức và vị trí trái phải của từng sự kiện chỉ phụ thuộc kịch bản, nên giống nhau cho mọi ứng viên.

## Số đo (`metrics.py`)

| Số đo | Cách đo | Đạt khi |
|---|---|---|
| Giọng đọc (bài C) | 300 ms đầu của mỗi từ, dải 1–4 kHz: giọng so với phần còn lại của bản trộn | ≥ 10 dB ở từ kém nhất |
| Quét bài C | Hai cấu hình hạ tiếng × trễ giọng 0, 150, 400 ms; ca xấu nhất, và ca xấu nhất khi giọng nhỏ đi 6 dB | Ghi lại, chủ dự án nghe ca xấu nhất |
| Luật âm xong từ (mục 6.2) | Năng lượng 1–4 kHz của file ứng viên tụt bao nhiêu sau 100 ms tính từ đầu tiếng | ≥ 15 dB, không thì ghi "giọng chờ 150 ms" |
| Loa nhỏ (bài F) | LUFS-M max mất đi qua lọc cao 200 Hz, trên phần của ứng viên trong bản trộn | ≤ 6 dB |
| Bộ giới hạn (bài D) | Mức ép lớn nhất, phần trăm thời gian ép quá 3 dB | < 5 % |
| Đỉnh | Đỉnh thật của bản trộn | Ghi lại |

## Tuyến Cuối (`ts_scenes.py`)

Số lấy từ `games/typing-survival/src/audio/theme-audio.ts`, `src/view/combat.ts`, `src/kit/audio/scene-audio.ts` (chỉ đọc, 24/10/2026): bus súng 0,42 (hạ khi đọc 0,5), trúng 0,6 (0,5), hạ quái 0,55 (0,56), cảnh báo 0,8 (0,8); mỗi bus một bộ nén (ngưỡng −12 dB, knee 6, tỉ lệ 8, bù mức tự động của Chromium); không có bộ giới hạn master; hạ tiếng bằng `setTargetAtTime` tau 50 ms.

| Cấu hình | Cách phát |
|---|---|
| `current` (game hiện tại) | Chỉ viên chẵn (`combat.ts:139`), một file mỗi id, tốc độ ×U(0,95; 1,05), mọi tiếng bắt đầu ở đầu khung 60 Hz, không nền, không đuôi, nén 2 ms / 140 ms, hạ tiếng khi giọng cất lên |
| `proposed` (đề xuất, BATCH1_BRIEF §3.3) | Mọi viên, bộ A và B xen nhau, đúng thời điểm mô phỏng, nền `gun.xung.loop` (vào 45 ms, ra 100 ms) và `gun.xung.tail` khi ngừng, tối đa 4 tiếng súng (cướp tiếng cũ nhất, mờ 25 ms), lệch A ±40, B ±70 cent, ±1 dB, nén bus súng và trúng 15 ms / 300 ms, hạ tiếng từ lúc xin đọc |

| Kịch bản | Dài | Có gì |
|---|---|---|
| `ts-xung-3s` | 4,0 s | Hai từ cách 1,4 s; Xung bắn 0,05–2,95 s (30 viên); trúng 150–300 ms sau mỗi viên (T1, 9 % T2), gom 38 ms; một đòn lớn T4 ở 2,30 s; ngừng bắn ở 3,05 s |
| `ts-xung-3s-kills` | 4,0 s | Như trên, 35 % số lần trúng làm vỡ một quái bầy (tối đa 4 trong 120 ms), lính tinh nhuệ nổ ở 1,90 s, từ thứ hai là từ gõ chuẩn (`word.perfect`) |
| `ts-tia-3s` | 3,4 s | Một từ, rồi Tia 2,5 s: một nhịp `gun.tia.pulse` mỗi 0,1 s, vài quái vỡ |
| `ts-breach` | 3,2 s | Xung bắn, hai từ, tuyến bị phá ở 1,20 s |

- **Mức:** âm ngắn vào bus ở mức đề xuất của thẻ (LUFS-M max −20). Một bộ súng được nâng hạ chung để dòng viên đạn có cùng LUFS-S max (−20) ở mọi ứng viên, nên bậc A/B trong bộ được giữ. Nền thấp hơn LUFS-M max trung bình của phát A `--bed-db` dB (16 hoặc 11), đuôi thấp hơn 4 dB.
- **Số đo "Liên thanh"** (`burst_numbers`, trên stem súng sau bộ nén, trước mức bus): chỗ trũng giữa hai phát (đường bao RMS 5 ms, chặn ở 60 dB), thời gian hổng (thấp hơn đỉnh trượt 300 ms quá 20 dB), độ lệch chuẩn khoảng cách đầu tiếng, tỉ lệ năng lượng 40–150 Hz, 150–500 Hz, 2–6 kHz, mất trên loa nhỏ, mức ép của bộ nén (trung vị, dao động P90−P10), bước tụt lớn nhất trong 10 ms sau khi ngừng bắn (RMS 20 ms; sàn ở −60 dB so với mức bắn, nên đuôi hàm mũ chạm im lặng số ở cuối file không bị tính là cắt), thời gian tới −60 dB, số lần một file phát hai lần liền.
- **Kiểm lại bài thử (P0):** 0a v2 ở cấu hình `current`: hổng 74,7 % (BATCH1_BRIEF đo 76 % khi lặp 5 lần/s); 0b v1 75,4 % (77 %), 0b v3 79,9 % (80 %); ở 10 viên/s: 52,2 / 53,7 / 61,3 % (52 / 53 / 61 %).

## Lời Gọi (`td_scenes.py`)

Số lấy từ `games/typing-defense/src/view/audio-min.ts`, `folk.ts`, `ui/settings.ts` (chỉ đọc, 24/10/2026): master 0,64 (thanh trượt 80 bình phương) rồi bộ giới hạn (−3 dB, tỉ lệ 20, bắt 2 ms, nhả 120 ms); sfx 1,4 × 0,64 = 0,896; vang 0,8 s (nhiễu × (1 − k/n)^2,6, gửi 0,12, trả 0,5); bus typing (word-hit, chuông, lời gọi, phím) qua bộ nén −18 dB, tỉ lệ 3, bắt 3 ms, nhả 100 ms, knee 30; bus world nhân 0,9; bus ui đi thẳng. Game chỉ hạ nhạc khi đọc (chưa có nhạc), không hạ hiệu ứng.

| Cấu hình | Cách phát |
|---|---|
| `current` (game hiện tại) | Mọi tiếng bắt đầu ở đầu khung 60 Hz; giới hạn `room()` đếm trong cửa sổ trượt 1 s (tên 4, mực 8, xu 3, lời gọi 3); nổ 2 và mực 3 mỗi khung; `leak` cách nhau 0,8 s |
| `proposed` (BATCH1_BRIEF L1, L2) | Đúng thời điểm mô phỏng; thùng thẻ nạp đều thay cho cửa sổ (tên 4/s, mực 8/s cho phép dồn 3, xu 3/s, lời gọi 3/s); giữ giới hạn mỗi khung |

| Kịch bản | Dài | Có gì |
|---|---|---|
| `td-wordhit-chain` | 11,6 s | 7 từ cách 1,5 s (40 WPM, 5 phím mỗi từ, tiếng phím tổng hợp của game) leo Chuỗi: `word-hit` A3 (ẩu) C4 D4 F4 (Hoàn hảo + chuông) G4 A4 C5 (Chớp: vuốt lên 1 bán cung trong 90 ms + chuông), mỗi từ một Phát Chữ và giọng đọc sau 150 ms; ba tháp cung (0,7, 0,7, 0,8 s), hai tháp pháo; Mực Câm tan, xu rơi |
| `td-night` | 9,0 s | Đêm: 5 từ có `word-hit` và Phát Chữ, hai tháp cung, lời gọi Chặt sáng hai lần (1,6 s, 5,9 s), quái lọt Lũy hai lần (3,4 s giữa hai từ, 7,2 s trùng một từ) |
| `td-menu` | 4,2 s | Màn đầu: 5 bước chuyển mục rồi chọn, hai lượt |

- **Mức:** mỗi âm vào bus ở giữa khoảng "Mức trong bản trộn" của thẻ (LUFS-M max); `word-hit` theo bậc Chuỗi từ −22 tới −16 (chữ của thẻ), từ ẩu −24; thẻ chưa có khoảng: `call-chop` −19, `coin` −23. Bản dựng hạ chung −11 dB cho gần −23 LUFS-M của Bảng Nghe.
- **Số đo:** giọng đọc (bài C) quét trễ 0, 150, 400 ms, không hạ và có hạ −6 dB bus typing, world từ lúc xin đọc (mục 6.2 bước 4, game chưa có); luật âm xong từ (1–4 kHz tụt sau 100 ms) cho `word-hit` (cả 7 nốt), `word-hit-bell`, `wordshot-fire`; loa nhỏ; bộ giới hạn và bộ nén bus typing; số tiếng mô phỏng xin, được phát, bị bỏ, khoảng im dài nhất và số tiếng nhiều nhất trong 250 ms của tên, mực, xu, nổ ở cả hai cấu hình.

## Bảng Nghe

Bản dựng Tuyến Cuối thành bối cảnh **"Liên thanh 3 s"** (khóa `burst`; `ts-breach` dùng `scene`). Bản dựng thành bối cảnh **"Trong trận thô"** (khóa `scene`) của ứng viên: `ctx: {"scene": "<file>"}` trong file phiên. Bảng phát đúng file đó, không lặp, không chỉnh mức (các bản dựng đã cùng một mức). Item chỉ hiện bối cảnh này khi mọi ứng viên đều có bản dựng.

Giọng macOS chỉ dùng để dựng bài thử trên máy này; không phát hành, không gửi đi đâu.
