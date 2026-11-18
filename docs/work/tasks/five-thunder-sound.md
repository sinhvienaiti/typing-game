# Âm thanh Ngũ Lôi Oanh Đỉnh · 12/11/2026

**Ai làm:** phiên lab-flipbooks (anh 12/11 14:3x: "xử lý luôn phần âm thanh còn thiếu"). Chưa commit; không đụng `src/lab/five-thunder.ts`. Agent không nghe được: **clip nghe thử là sản phẩm chính**, anh là người quyết.

## Sản phẩm
- Bộ tiếng: `games/immortality-cultivation/art-src/lab/audio/five-thunder/` (13 file wav 24-bit 48 kHz + 13 ogg Vorbis q6 + `manifest.json` ánh xạ sự kiện → file, tầng, số đo, lý do, cue sheet).
- Clip nghe thử: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/five-thunder-lab/ngu-loi-v16-sound-preview.mp4` (hình v16, tiếng ghép theo `raw-v16/run.json`: 24 tia 0,60–3,23 s, đòn kết 3,417 s).
  - Đo clip: integrated **-17.4 LUFS**, momentary max -14.2 LUFS, true peak **-2.8 dBTP**.
  - Reverb: không có impulse response trong repo nên dùng `aecho` nhẹ (38/71/113 ms, 0,22/0,14/0,08) trên cả mix, rồi `alimiter` −1 dBTP, makeup +4 dB. Nếu anh thấy khô hoặc dội quá, đổi ở `captures/tu-tien/five-thunder-sound/build.py`.
- Kiểm máy từng take (onset, lên đỉnh, true peak, LUFS, mẫu clip, ba dải, tâm phổ): `captures/tu-tien/five-thunder-sound/takes.json` (62 take).

## Cách chuẩn hoá (theo `SOUND_AUDIT_2026-11-04.md` và `sound-tiers.ts`)
Mỗi file: cắt từ đúng transient mạnh nhất (đầu tiếng tại 0 ms), fade ra ngắn; đưa **momentary max (400 ms)** về mức tầng: T2/T3 −18, T4 −13,5, T5 −11,5, T6 −9 LUFS; rồi trần **true peak −1 dBTP** (file chạm trần thì nằm dưới mức tầng, có ghi). Các take Firefly gốc đều đỉnh 0 dBTP và vài bản có mẫu clip; chọn bản ít clip nhất, clip còn lại bị trần −1 dBTP nuốt.

## Bảng sự kiện → file → bản chọn → tầng → lý do
| Sự kiện | File | Nguồn Firefly | Tầng (mục tiêu) | Đo | Lý do chọn |
|---|---|---|---|---|---|
| five-thunder-charge-loop | five-thunder-charge-loop.wav / five-thunder-charge-loop.ogg | tt-sfx-trib-thunder-roll-loop/take3.wav | T2 (-18.0 LUFS) | đo mom. -18.0 · TP -8.5 · 4.0 s | take3: bắt đầu ngay (onset 0 ms), đuôi về -41 dB nên ghép vòng 4 s êm, có dải giữa (13,6 %) để nghe ra sấm chứ không chỉ ù; take1/4 đỉnh 0 dBTP và lên chậm 1,2-1,9 s, take2 tắt hẳn ở cuối |
| five-thunder-warning | five-thunder-warning.wav / five-thunder-warning.ogg | tt-sfx-trib-strike-warning/take6.wav | T3 (-18.0 LUFS) | đo mom. -18.0 · TP -4.7 · 1.195 s | take6: lấp lánh cao (73 % năng lượng > 4 kHz) nghe như điện tích tụ, lên 214 ms, tắt sạch (-59 dB), không clip; take3/8 nặng trầm và bị cắt cụt cuối, take4 đỉnh -9,5 LUFS quá to và bẩn |
| five-thunder-release | five-thunder-release.wav / five-thunder-release.ogg | tt-sfx-thunder-cast/take3.wav + tt-sfx-el-thunder-seal/take2.wav (-6 dB) | T4 (-13.5 LUFS) | đo mom. -13.5 · TP -4.2 · 1.2 s | cast take3: nhiều dải cao nhất trong 4 bản (28,8 % > 4 kHz) nên nghe ra tiếng 'snap' nối điện, không clip; seal take2 (không clip, TP -0,2) đặt dưới -6 dB cho phần nặng; cast take1/4 có mẫu clip, take2 ít cao hơn |
| five-thunder-bolt-1 | five-thunder-bolt-1.wav / five-thunder-bolt-1.ogg | tt-sfx-trib-lightning-strike/take2.wav | T3 (-18.0 LUFS) | đo mom. -18.0 · TP -7.6 · 0.45 s | take2: ít clip nhất (2 mẫu), lên nhanh nhất (229 ms), dải giữa 29 %; cắt 0,45 s từ đúng transient (đầu tiếng tại 0 ms), fade 120 ms |
| five-thunder-bolt-2 | five-thunder-bolt-2.wav / five-thunder-bolt-2.ogg | tt-sfx-trib-lightning-strike/take8.wav | T3 (-18.0 LUFS) | đo mom. -18.0 · TP -5.1 · 0.45 s | take8: 2 mẫu clip, sáng nhất (tâm phổ 535 Hz, có 2,8 % > 4 kHz) khác màu với 1; cắt 0,45 s từ đúng transient (đầu tiếng tại 0 ms), fade 120 ms |
| five-thunder-bolt-3 | five-thunder-bolt-3.wav / five-thunder-bolt-3.ogg | tt-sfx-trib-lightning-strike/take6.wav | T3 (-18.0 LUFS) | đo mom. -18.0 · TP -9.4 · 0.45 s | take6: dải giữa 54 % (khô, 'crack' hơn là 'rumble'), 8 mẫu clip ở đỉnh được giới hạn lại; cắt 0,45 s từ đúng transient (đầu tiếng tại 0 ms), fade 120 ms |
| five-thunder-bolt-4 | five-thunder-bolt-4.wav / five-thunder-bolt-4.ogg | tt-sfx-trib-lightning-strike/take4.wav | T3 (-18.0 LUFS) | đo mom. -18.0 · TP -10.1 · 0.45 s | take4: tâm phổ 529 Hz với 5,4 % > 4 kHz, đuôi 1,6 s ngắn gọn; bỏ take7 (31 mẫu clip), take1/3/5 giống nhau và toàn trầm; cắt 0,45 s từ đúng transient (đầu tiếng tại 0 ms), fade 120 ms |
| five-thunder-crack | five-thunder-crack.wav / five-thunder-crack.ogg | tt-sfx-thunder-crack/take1.wav | T3 (-18.0 LUFS) | đo mom. -19.3 · TP -1.0 · 0.3 s · chạm trần −1 dBTP | take1: duy nhất có dải giữa đáng kể (36,6 %, tâm 237 Hz) nên nghe ra 'rắc'; take2-4 gần như chỉ trầm < 100 Hz và nhỏ (-19..-24 LUFS); cắt 0,3 s từ transient |
| five-thunder-hit-light | five-thunder-hit-light.wav / five-thunder-hit-light.ogg | tt-sfx-thunder-hit-light/take2.wav | T3 (-18.0 LUFS) | đo mom. -18.0 · TP -8.3 · 0.35 s | take2: lên đỉnh 40 ms (nhanh nhất), 42 % > 4 kHz cho tiếng giật điện trên da, không clip, tắt sạch |
| five-thunder-hit-heavy | five-thunder-hit-heavy.wav / five-thunder-hit-heavy.ogg | tt-sfx-thunder-hit-heavy/take1.wav | T3 (-18.0 LUFS) | đo mom. -18.0 · TP -8.3 · 0.5 s | take1: 1 mẫu clip (ít nhất cùng take4), onset 20 ms, đuôi -40 dB 1,36 s dài hơn take4 (0,74 s); cắt 0,5 s từ transient |
| five-thunder-hush | (duck) | – | – | hạ −40 dB, 10/60/40 ms | 60 ms im lặng trước đòn kết: hạ mọi bus combat -40 dB trong 10 ms, giữ 60 ms, nhả 40 ms khi tiếng nổ vào; không cần file |
| five-thunder-finisher | five-thunder-finisher.wav / five-thunder-finisher.ogg | tt-sfx-thunder-big-burst/take3.wav + tt-sfx-thunder-combo-finisher/take2.wav | T6 (-9.0 LUFS) | đo mom. -11.2 · TP -1.0 · 3.0 s · chạm trần −1 dBTP | big-burst take3: không clip, bắt đầu ngay, đuôi -40 dB 4,4 s, dải giữa 35,7 % (sáng nhất); finisher take2: 3 mẫu clip (ít nhất), trầm 185 Hz làm thân nổ; hai lớp cộng rồi giới hạn -1 dBTP |
| five-thunder-roll-tail | five-thunder-roll-tail.wav / five-thunder-roll-tail.ogg | tt-sfx-trib-thunder-roll-loop/take3.wav | T4 (-13.5 LUFS) | đo mom. -13.9 · TP -1.0 · 1.5 s · chạm trần −1 dBTP | 1,5 s sấm rền sau đòn kết, cùng nguồn với nền tụ lực để liền màu, fade ra 0,9 s |
| five-thunder-crackle | five-thunder-crackle.wav / five-thunder-crackle.ogg | tt-sfx-el-thunder-affliction/take3.wav | T2 (-18.0 LUFS) | đo mom. -18.0 · TP -4.6 · 2.4 s | take3: 85,6 % năng lượng > 4 kHz (lách tách), TP -0,8, không clip; cắt 8 hạt 160 ms tại các đỉnh bao, đặt thưa dần (0,22 → 0,72 s) và nhỏ dần 10 %/hạt; thunder-tail take2/3 cũng sáng nhưng là hơi rít liền, không rời hạt |

## Cue sheet dùng trong clip (và đề nghị cho lab)
| Lúc | Tiếng |
|---|---|
| 0,00 → 0,50 s | charge-loop (fade in 100 ms, fade out 150 ms khi phóng) |
| 0,35 s | warning (trận đạt cỡ) |
| 0,50 s | release (tia đầu − 0,1 s) |
| 0,60 → 3,23 s | 24 tia: bolt-1..4 xoay vòng, pan theo x màn hình (±0,7), gain theo scale tia (±2 dB); crack chồng mỗi tia thứ ba (−3 dB); hit-light (+30 ms, −4 dB), hit-heavy cho tia scale ≥ 1,15 |
| 3,357 s | hush: hạ −40 dB trong 10 ms, giữ 60 ms, nhả 40 ms |
| 3,417 s | finisher (big-burst + combo-finisher) |
| 3,567 s | roll-tail 1,5 s |
| 4,217 s | crackle: 8 hạt thưa dần tới ≈ 6,6 s |

## Tiếng còn thiếu, cần Firefly tạo
1. **Tiếng "rắc" khô cho tia đơn** (crack 50–150 ms, nhiều dải 2–8 kHz, không rumble): bộ `trib-lightning-strike` và `thunder-crack` đều nặng trầm (< 250 Hz chiếm 46–96 %), phần "xé" cao chỉ 0–5 %. Tia hiện nghe sẽ "ầm" hơn là "xoẹt".
2. **Hồi vang (IR) sân đấu**: repo chưa có impulse response; nên tạo hoặc lấy IR CC0 để thay `aecho`.
3. **Tiếng quái chết vì sét** (xác cháy, xèo) nếu muốn tách khỏi hit-heavy.

## Chưa làm
- Chưa nối vào `five-thunder.ts`/`sound.ts` (phiên lab-element-kits); manifest có cue sheet để nối.
- Chưa có người nghe: mọi số trên là kiểm máy.
