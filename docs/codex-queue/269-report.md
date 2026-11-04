# Báo cáo phiếu 269 · Tu Tiên · Bậc to, đầu tiếng release-k7 và send vang chung

Ngày: **04/11/2026**. Trạng thái: **xong phần Codex, chưa commit; chờ Claude kiểm lại và anh nghe**. Không có giới hạn công cụ hoặc hạn mức cản việc.

## Phạm vi và nền

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-sound`, nhánh `codex/lab-sound-tiers`, HEAD `2381c7b`. Lúc nhận chỉ có `?? node_modules` là symlink do Claude chuẩn bị; không sửa symlink này. Mọi đường ghi đều qua `/Volumes`.

Áp dụng `agent-orchestration` và `game-sfx`, vai trò worker một làn, không tạo agent phụ. Làm theo lời giải đã chốt và ngoại lệ giao ngay lúc 21:30 ghi trong phiếu; không mở lại bước thiết kế hoặc quy trình phản biện. Không dùng trình duyệt, dev server, mạng, công cụ tạo ảnh hay tạo âm AI. Các lệnh kiểm game bên dưới là các lệnh phiếu 269 yêu cầu riêng, chỉ chạy trong worktree âm.

Đã ghi đúng bảy tệp của worktree:

1. `src/lab/sound.ts` — dùng chung BUS_GAIN/MASTER_GAIN, áp trim theo id thực sau resolve; thêm send trước bus và hạ return trong hush.
2. `src/lab/sound-tiers.ts` — bậc, đích, gain chuẩn, staticDb, bảng trim ghi sẵn, trimGain, SEND_LEVEL và VERB_RETURN.
3. `scripts/visual/mix-lab-sound.mjs` — nhánh ướt, nền đủ dài, chuẩn hóa IR theo S, hush chung, cờ `--ir`, tương thích bản ghi cũ.
4. `scripts/audio/lab-sound-tiers.mjs` — measure, attack, trims, ir, ir --check; in lệnh ffmpeg trước khi chạy, chặn ghi đè file mới trong art-src.
5. `tests/lab/sound-tiers.test.ts` — 15 test Node, không WebAudio.
6. `tests/lab/fixtures/sound-audit-summary.json` — 34 sự kiện, gồm 10 id `-fire`; nguồn đánh giá và take mới ghi trong trường `source`.
7. `docs/changelog/2026-11-04-lab-sound-tiers.md` — thay đổi, số đo, kiểm và phần chờ nghe.

Thêm đúng bốn tệp vào art-src thật ở `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/audio/`:

| Đường tương đối dưới audio | Số byte |
|---|---:|
| `release-k7/03a.ogg` | 48381 |
| `ir/hall-a.wav` | 460844 |
| `ir/hall-a.json` | 1106 |
| `manifest.next.json` | 1800 |

Tệp thứ mười hai là báo cáo này: `docs/codex-queue/269-report.md` ở repo cha. Không ghi vào mã game thật, src/kit, skills-main.ts, events.ts, SOURCES.json hoặc manifest đang chạy.

## Phần mã và bản ghi

- `trim = round0.1(min(target − mMax, −1 − tp) − staticDb)`. Các hệ số động power/xô/tier trong `on()` và `update()` giữ nguyên; voice trim 0 dB. Bản fire lấy trim theo id thực đã resolve. Gain ghi vào take đã gồm trim và gain bus, chưa gồm master.
- Nhánh send live rẽ sau panner, trước gain bus; take ghi `send = SEND_LEVEL[id] / BUS_GAIN[bus]`. Các marker hush/reset ghi send 0.
- Đồ thị vang được tạo một lần trong unlock: delay 25 ms → highpass 200 Hz → convolver normalize → lowpass 6500 Hz → return 0,7 → master 0,9. Q hai biquad là −3,0103 dB. Nạp IR bằng fetch/decode như âm khác; khi chưa nạp xong đường khô vẫn chạy. Hush hạ cả return và các bus xuống 8 % trong 12 ms, hồi trong 10 ms.
- Offline cộng nhánh ướt trước hush/master/limiter. Nhánh ướt có nền anullsrc dài hết duration, `afir=irnorm=-1:irgain=1`, volume S, bộ lọc Q 0,7071 và return 0,7. Có send mà thiếu IR/metadata thì thoát lỗi; bản ghi cũ thiếu send hiểu là 0.
- `--ir=<file.wav>` đọc `<file.json>` cạnh WAV. Do worktree không có art-src, khi Claude trộn âm hãy truyền `--root=/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation` hoặc gốc bản thử đang phục vụ manifest mới. Mặc định duration là lastEnd + 0,025 + dài IR khi có send; không send là lastEnd + 0,25.

## Kiểm 1–7

| Kiểm | Kết quả |
|---|---|
| 1. `node node_modules/typescript/bin/tsc --noEmit -p .` | Thoát 0, không lỗi. |
| 2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4` | Trước: **86 tệp, 917/917 test**, 6,42 s. Sau: **87 tệp, 932/932 test**, 6,50 s. Thêm đúng 15 test. |
| 3. Xóa outDir cũ; `IC_VITE_CACHE_DIR=/private/tmp/codex-269-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-269-dist --configLoader runner` | Thoát 0, 183 module, dựng 1,01 s. `grep -rl "SOUND_TRIM_DB\|hall-a" /private/tmp/codex-269-dist` không in gì, mã 1 của grep là không có kết quả. Thư mục đã được xóa sau kiểm, gồm âm chạy thử tạm. |
| 4. `node scripts/audio/lab-sound-tiers.mjs trims` | Thoát 0; lần kiểm và lần ghi báo cáo đều **fixture: unchanged**. Bảng ở dưới. |
| 5. `node scripts/audio/lab-sound-tiers.mjs measure release-k7/03a.ogg` | Thoát 0; cả năm chốt đều true, số cạnh take gốc ở dưới. |
| 6. `node scripts/audio/lab-sound-tiers.mjs ir --check` | Thoát 0; S, RT60 trùng JSON; kiểm xung qua cả hai kênh. Chạy ir tạo file đúng một lần; các lần sau chỉ ir --check. MD5 WAV/JSON trước/sau lần check cuối trùng nhau. |
| 7. diff/status, ls bốn file mới, MD5 bảy file gốc | Chỉ các tệp được phép và symlink node_modules có sẵn; manifest.next chỉ đổi release-k7. MD5 gốc trùng trước/sau, bảng ở dưới. |

`git diff --check` thoát 0. Lần `trims` đầu tạo fixture và in bảng, thoát 1 vì bảng ghi cứng khi đó còn rỗng; đã chép đúng số in ra vào mã rồi chạy kiểm lại, thoát 0. Không thay số đo hoặc công thức để làm kiểm qua.

Test bao phủ đủ id SOUND_IDS và fire trong fixture, trimGain, công thức có gain tĩnh/trần true peak, thứ bậc lúc phát, chín sự kiện chuẩn qua record() với fetch giả, fire sau resolve, power 0 và voice/hush/reset. Test không đọc file ngoài repo.

Chạy thử bổ sung bộ trộn trên take `03a`, pan 0,3, rate 1: có send và có hush đều tạo WAV dài mặc định **5,279 s**, bản ghi cũ không send **3,104 s**; thiếu IR theo cờ --ir thoát 1 với thông báo yêu cầu IR/metadata. Đo được đuôi sau take (2,91–3,20 s, RMS −79,55 dBFS) và hệ số hush 3,015–3,045 s là **0,07734** so với mức 0,08, trên PCM16 rất nhỏ. Đây là kiểm kỹ thuật của bộ trộn, không phải nghe duyệt trong lab. Không giữ bản WAV tạm.

## Đo đầu tiếng release-k7

Lệnh đầu tiên đo ba take cũ bằng ebur128 có đệm cuối 1 s, kết quả khớp đánh giá chính xác ở độ phân giải 0,1:

| Take cũ | mMax đo / đánh giá (LUFS) | TP đo / đánh giá (dBTP) |
|---|---:|---:|
| 01 | −8,4 / −8,4 | −2,7 / −2,7 |
| 02 | −7,6 / −7,6 | −1,5 / −1,5 |
| 03 | −8,4 / −8,4 | −2,1 / −2,1 |

Đường bao mono 16 kHz, cửa sổ RMS 10 ms, bước 1 ms; tPeak tính ở đầu cửa sổ. Take 03 có tPeak **0,139 s**, nên start **0,109 s**. Lệnh đã chạy:

```sh
ffmpeg -hide_banner -nostdin -n -i /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/audio/release-k7/03.ogg -ar 48000 -af atrim=start=0.109000,asetpts=PTS-STARTPTS,afade=t=in:d=0.003 -c:a libopus -b:a 128k /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/audio/release-k7/03a.ogg
```

| Số đo | 03.ogg gốc | 03a.ogg sau Opus | Chốt |
|---|---:|---:|---|
| Dài âm giải mã | 2,95625 s | **2,84725 s** | ≥ 1 s: đạt |
| mMax | −8,4 LUFS | **−8,3 LUFS** | Lệch 0,1 ≤ 1,5 LU: đạt |
| True peak | −2,1 dBTP | **−2,3 dBTP** | ≤ −1: đạt |
| tPeak | 139 ms | **27 ms** | Đầu cửa sổ RMS cực đại |
| atk, từ ngưỡng đỉnh −20 dB | 121 ms | **27 ms** | ≤ 30: đạt |
| Mức +500 ms dưới đỉnh | −11,038989 dB | **−10,394762 dB** | ≥ −30: đạt |
| t40 sau đỉnh | 2696 ms | **2699 ms** | Ghi số theo yêu cầu measure |
| Kênh / tần số | stereo / 48 kHz | stereo / 48 kHz | Giữ nguyên |

Độ dài container ffprobe là 2,962729 / 2,853729 s; bảng dùng độ dài âm sau giải mã. Phần sau đầu tiếng chỉ mã hóa lại bằng Opus, không thêm xử lý đuôi. Chưa ai nghe so 03/03a.

`manifest.next.json` bằng manifest gốc theo cấu trúc, chỉ `release-k7` đổi sang `["03a.ogg"]`. `release-k5` giữ 01–03, `release-k7-fire` giữ nguyên. Không dùng --force.

## Bảng trim đã kiểm

Nguồn fixture: summary-by-event.json của đánh giá, giữ id/mMax/tp và chỉ thay release-k7 bằng max của take trong manifest.next (một take 03a). Các mức dB và LUFS dưới đây dùng dấu chấm như đầu ra công cụ. `playback` là đường khô ở lần phát chuẩn, gồm master; `shortfall LU` là phần thiếu trước làm tròn trim.

| id | tier | mMax | tp | staticDb | trim | playback | capped | shortfall LU | missing |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| callout | voice | -10.7 | -1.1 | -1.36 | 0.0 | -12.06 | false | 0.0 | false |
| callout-guard | voice | -11.2 | -1.5 | -1.36 | 0.0 | -12.56 | false | 0.0 | false |
| callout-k2 | voice | -11.2 | -1.4 | -1.36 | 0.0 | -12.56 | false | 0.0 | false |
| callout-k4 | voice | -11.2 | -1.4 | -1.36 | 0.0 | -12.56 | false | 0.0 | false |
| callout-k5 | voice | -10.4 | -2.2 | -1.36 | 0.0 | -11.76 | false | 0.0 | false |
| callout-k7 | voice | -9.3 | -1.4 | -1.36 | 0.0 | -10.66 | false | 0.0 | false |
| cast | T2 | -17 | -7.4 | -8.87 | 7.9 | -17.97 | false | 0.0 | false |
| death | T3 | -13 | -2.3 | -7.29 | 2.3 | -17.99 | false | 0.0 | false |
| death-fire | T3 | -11.9 | -1.4 | -7.29 | 1.2 | -17.99 | false | 0.0 | false |
| flyby | T2 | -15.9 | -8.6 | -8.05 | 5.9 | -18.05 | false | 0.0 | false |
| flyby-fire | T2 | -18.7 | -9.7 | -8.05 | 8.7 | -18.05 | false | 0.0 | false |
| impact-flesh | T3 | -10.6 | -1.1 | -3.77 | -3.6 | -17.97 | false | 0.0 | false |
| impact-flesh-fire | T3 | -11.2 | -1.5 | -3.77 | -3.0 | -17.97 | false | 0.0 | false |
| impact-spirit | T3 | -10.2 | -1.6 | -3.77 | -4.0 | -17.97 | false | 0.0 | false |
| impact-spirit-fire | T3 | -10.3 | -1.6 | -3.77 | -3.9 | -17.97 | false | 0.0 | false |
| impact-stone | T3 | -10.1 | -1.3 | -3.77 | -4.1 | -17.97 | false | 0.0 | false |
| impact-stone-fire | T3 | -10.5 | -1.1 | -3.77 | -3.7 | -17.97 | false | 0.0 | false |
| release | T4 | -11.4 | -1.5 | -4.26 | 2.2 | -13.46 | false | 0.0 | false |
| release-auto | T2 | -15 | -8.5 | -7.29 | 4.3 | -17.99 | false | 0.0 | false |
| release-dash | T4 | -14.2 | -5.4 | -4.26 | 5.0 | -13.46 | false | 0.0 | false |
| release-guard | T4 | -7.6 | -1.2 | -4.26 | -1.6 | -13.46 | false | 0.0 | false |
| release-k1 | T4 | -10.2 | -4.3 | -4.26 | 1.0 | -13.46 | false | 0.0 | false |
| release-k1-fire | T4 | -13.5 | -4.6 | -4.26 | 4.3 | -13.46 | false | 0.0 | false |
| release-k2 | T4 | -10.2 | -1 | -4.26 | 1.0 | -13.46 | false | 0.0 | false |
| release-k4 | T4 | -9.6 | -1.2 | -4.26 | 0.4 | -13.46 | false | 0.0 | false |
| release-k5 | T5 | -8.5 | -1.2 | -2.85 | -0.1 | -11.45 | false | 0.0 | false |
| release-k7 | T5 | -8.3 | -2.3 | -4.26 | 1.1 | -11.46 | false | 0.0 | false |
| release-k7-fire | T5 | -9.7 | -1.2 | -4.26 | 2.5 | -11.46 | false | 0.0 | false |
| world-climax | T6 | -10.6 | -1 | -2.33 | 2.3 | -10.63 | true | 1.6 | false |
| world-climax-fire | T6 | -8.8 | -1 | -2.33 | 2.1 | -9.03 | false | 0.0 | false |
| world-close | T5 | -10.2 | -1 | -3.74 | 2.4 | -11.54 | false | 0.0 | false |
| world-close-fire | T5 | -10.7 | -2.7 | -3.74 | 2.9 | -11.54 | false | 0.0 | false |
| world-open | T5 | -11.9 | -2.6 | -3.74 | 4.1 | -11.54 | false | 0.0 | false |
| world-open-fire | T5 | -9.2 | -1.2 | -3.74 | 1.4 | -11.54 | false | 0.0 | false |

**capped:** chỉ `world-climax`, thiếu **1,6 LU**; trim +2,3 dB đưa mức khô lúc phát tới −10,63 LUFS (sai khác làm tròn 0,1 dB). **missing:** không có sự kiện nào thiếu đo trong 34 id hiện tại. Mọi voice trim 0, không bù gain tĩnh.

## IR và kiểm xung

IR là nhiễu trắng hai kênh độc lập, mulberry32 seed 0x7ab1e / 0x7ab1f, bao exp(−6,91·t/2,2), 8 ms đầu bằng 0, fade 50 ms cuối, đỉnh −1 dBFS; WAV PCM16 stereo 48 kHz, 2,4 s. S và T30 tính từ chính mẫu PCM16 đã ghi, JSON giữ độ chính xác double.

**IR là bộ xử lý, không phải âm thay thế. Anh nghe và quyết IR này có đạt không.** Khi có IR thu thật CC0, thay cặp WAV/JSON với S tính lại; chưa chấp nhận chất âm của IR hiện tại.

| Số | Kết quả |
|---|---:|
| RT60 qua Schroeder/T30 | **2,1987286194219933 s**, trong 2,2 ± 0,15 s |
| S Web Audio | **0,0085949610853689** |
| Lệch tương đối S tính lại so JSON | **0** |
| Lệch RT60 tính lại so JSON | **0 s** |
| Xung stereo 48 kHz | **2,5 s**, đủ dài hơn IR |
| Năng lượng trái so S × h | **−0,0000005593137569061132 dB** |
| Năng lượng phải so S × h | **−0,0000005456508936101916 dB** |
| Onset trái, ngưỡng đỉnh −60 dB | **384**, mẫu h khác 0 đầu tiên: 384 |
| Onset phải, ngưỡng đỉnh −60 dB | **384**, mẫu h khác 0 đầu tiên: 384 |

Không dùng phép so khác 0 cho đầu ra FFT. Lệnh kiểm dùng `afir=irnorm=-1:irgain=1,volume=0.0085949610853689`. WAV/JSON không đổi byte khi chạy `ir --check`.

## Diff, trạng thái và bảo toàn nguồn

`git -C games/.wt-ic-sound diff --stat`:

```text
 scripts/visual/mix-lab-sound.mjs | 43 +++++++++++++++++++++++-----
 src/lab/sound.ts                 | 62 +++++++++++++++++++++++++++++++---------
 2 files changed, 84 insertions(+), 21 deletions(-)
```

Stat chỉ hiện hai tệp đã được Git theo dõi; năm tệp mới vẫn untracked vì phiếu cấm git add/commit. `git -C games/.wt-ic-sound status --short --untracked-files=all`:

```text
 M scripts/visual/mix-lab-sound.mjs
 M src/lab/sound.ts
?? docs/changelog/2026-11-04-lab-sound-tiers.md
?? node_modules
?? scripts/audio/lab-sound-tiers.mjs
?? src/lab/sound-tiers.ts
?? tests/lab/fixtures/sound-audit-summary.json
?? tests/lab/sound-tiers.test.ts
```

`node_modules` có sẵn trước khi làm. Ngoài nó, mọi dòng đúng danh sách được ghi. Không chạy lệnh Git ngoài status/diff/log.

| Tệp gốc dưới audio | MD5 trước | MD5 sau |
|---|---|---|
| `manifest.json` | `cb9fe445c48a9e2c382d87f3d9c81b64` | `cb9fe445c48a9e2c382d87f3d9c81b64` |
| `release-k5/01.ogg` | `a3d504a4af68dfb0b6f1298507bc054f` | `a3d504a4af68dfb0b6f1298507bc054f` |
| `release-k5/02.ogg` | `92234360f169a8b61127d27e8d3dd0ad` | `92234360f169a8b61127d27e8d3dd0ad` |
| `release-k5/03.ogg` | `f4df2d90848fd4009652eb1867a4ef05` | `f4df2d90848fd4009652eb1867a4ef05` |
| `release-k7/01.ogg` | `62f716f1b2d631f354e5eb860b5af07a` | `62f716f1b2d631f354e5eb860b5af07a` |
| `release-k7/02.ogg` | `340e06f6fbc446e2dfcc49072f1aee6f` | `340e06f6fbc446e2dfcc49072f1aee6f` |
| `release-k7/03.ogg` | `f9051e024fd80f1b06b373da429dcc91` | `f9051e024fd80f1b06b373da429dcc91` |

## Phần bỏ qua và người tiếp nhận cần xem

1. **release-k5 còn nợ mở:** không cắt hoặc thêm bản a; vẫn dâng khoảng 2,1 s. Chỉ sửa mức theo bậc và send 0,4. Dựng lại từ stem hoặc quyết giữ tiếng dâng cho ultimate là phiếu sau.
2. Không tạo âm cut-in, callout mới, Song Long hoặc lớp lấp lánh của Lửa; không tải âm hay sinh âm AI; ngoài phạm vi.
3. Không thêm limiter live hoặc duck bus dưới voice. `world-climax` còn thiếu 1,6 LU do trần true peak; cần bản render xử lý sau. Đỉnh của bản trộn đủ có thể cao hơn cao trào vì voice cộng với release/world-open; để Claude ghi nợ sau khi quay, không suy từ bản thử một take.
4. Claude đọc diff, chạy lại kiểm 1–7, dùng **trims** và **ir --check** cho lần kiểm lại. Không gọi ir tạo lại để kiểm. Thử manifest.next trên bản thử, giữ manifest cũ. Trong lab dùng phím **1 → k1, 6 → k5, 7 → k7**.
5. Đo từng sự kiện bằng takes.json đã lọc chỉ các take của sự kiện đó, giữ send của nó. Mức đích mỗi take trừ phần nó thấp hơn take to nhất của sự kiện. Với bản trộn đủ phím 6/7, ghi momentary theo thời gian và vị trí đỉnh; kiểm chồng voice là phần sau.
6. **Anh cần nghe:** so 03.ogg với 03a.ogg xem có mất đầu rút kiếm; nghe thứ bậc và IR trong video lab có tiếng. Chỉ gộp khi anh đã nghe. Trạng thái chất âm: **NOT LISTENED**, chưa đạt nghiệm thu nghe hoặc nghiệm thu trong host.
