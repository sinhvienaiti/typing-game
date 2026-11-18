# Gói âm quái, tinh anh, boss · 12/11/2026

**Ai làm:** phiên lab-flipbooks, ngay sau gói âm Ngũ Lôi (`five-thunder-sound.md`). Chưa commit. Không đụng `src/lab/five-thunder.ts`; nối vào lab qua `src/lab/sound.ts` và `sound-tiers.ts` (mục `LAB_TAKES`/`SPRINT_TAKES`) chỉ sau khi anh nghe clip thử và gật.

**Anh chọn (12/11 14:5x):** sau Ngũ Lôi làm âm cho **quái và boss** trước, vì người chơi nghe nhiều nhất. Luật chung: nguyên liệu Firefly có sẵn trước, Firefly tạo mới chỉ cho chỗ thiếu; agent không nghe được, nên sản phẩm chính là **clip nghe thử** và số đo; anh là người chấm.

## Nguyên liệu
`S = art-src/lab/firefly-sprint-2026-11-05/sound`: `beast` 36 việc/192 bản (sói, quạ, lợn, vượn, chuột, chung), `boss` 20/108, `elite` 13/68, `captain` 5/28, `enemy` 12/60 (báo đòn vòng/nón/tia). Bảng mức đã có trong `sound-tiers.ts` (`FIREFLY_LEVELS`). Danh sách sự kiện lab trong `src/lab/sound.ts` (`SOUND_IDS`, các bucket impact/death 40–50 ms).

## Việc
1. **Bản đồ sự kiện quái:** cho mỗi loài (sói, quạ, lợn, vượn, chuột) và cấp (thường, tinh anh, captain, Thú Vương): spawn, di chuyển loop (bầy), gầm/hú, đòn (báo đòn → vung → chạm), trúng nhẹ/nặng, chết, tan mực; boss thêm: breath loop, charge buildup/launch/impact, pillar crash, rend strike. Ghi bảng sự kiện → file → bản chọn → tầng dB → bucket.
2. **Chọn bản** bằng kiểm máy (transient ở 0 ms, không clip, true peak ≤ −1 dBTP, không tiếng lạ, dài hợp vai: hit ≤ 0,4 s, chết ≤ 1,2 s, loop có mối nối sạch), cắt gọn, chuẩn hoá theo tầng (quái thường thấp hơn chiêu 6 dB, tinh anh 3 dB, boss ngang chiêu; luật bucket 40–50 ms cho bầy: không 500 one-shot).
3. **Clip nghe thử:** ghép tiếng lên một clip lab có bầy quái đi, bị đánh, chết (dùng clip Ngũ Lôi v16 hoặc chụp một kịch bản lab riêng 10 s có sói, chuột, quạ, lợn, vượn bị đánh và một pha boss nếu có), đúng khung sự kiện, có bucket cho bầy; đo LUFS và true peak; xuất `owner-review/2026-11-12/tu-tien/five-thunder-lab/foe-sound-preview.mp4` (hoặc thư mục `foe-sound/` mới có ABOUT.md).
4. **Thiếu gì:** liệt kê sự kiện không có tiếng hợp (ví dụ captain, tinh anh thiếu loài nào) thành danh sách việc Firefly SFX kèm prompt tiếng Anh, chưa chạy.
5. Báo cáo ≤ 150 chữ: số sự kiện có tiếng/thiếu, số bản chọn, LUFS, đường dẫn clip.


## Kết quả v2 (lab-flipbooks, 12/11 16:45)

25 job "gap foe-pack" đã có âm thật; mọi chỗ "dùng tạm" của bản đầu đã thay, bảng "Thiếu" bỏ.

| Đã dùng tạm | Nay |
|---|---|
| rat-hurt, rat-death (cắt từ rít bầy) | `rat-hurt/take2`, `rat-death/take4` |
| spawn sói, quạ, vượn (mượn spawn lợn/chuột) | `wolf-spawn/take3`, `crow-spawn/take3`, `ape-spawn/take3` |
| gầm lợn (không có; mượn gầm vượn) | `boar-roar/take3` |
| trúng nặng = hurt + ink-dissolve | `<loài>-hurt-heavy` riêng (wolf take2, boar take3, rat take4, crow take3, ape take2); layers vẫn có ink-dissolve −6 dB |
| `elite-roar` chung | `elite-<loài>-roar` ×5 (wolf take2 có 7 mẫu clip, ít nhất trong 4; còn lại 0) |
| `captain-howl` chung (giọng sói) | `captain-<loài>-call` ×5 (0 mẫu clip) |
| `boss-charge-launch` (cả 4 bản 13 mẫu clip) | `boss-charge-launch-clean/take4` (0 clip); tên cũ `boss-charge-launch` giữ làm bí danh để lab không vỡ |
| Thú Vương dùng boss-* chung | `boss-boar-king-bellow` (take1), `-charge` (take3), `-death` (take1), tất cả 0 mẫu clip |

Chưa có IR hồi vang: clip vẫn dùng `aecho`.

**Gói:** `games/immortality-cultivation/art-src/lab/audio/foes/` — 98 sự kiện, 220 file (wav 24-bit + ogg 48 kHz), `manifest.json`. Luật "Components first": âm là nguyên liệu ghép lúc chạy, nên mỗi sự kiện có `variants` (73/98 sự kiện có 2–3 take đạt: ≤ 2 mẫu clip hoặc không hơn bản chính, onset ≤ 160 ms; vòng lặp và vài sự kiện chỉ có một bản đạt) và `layers` (transient/body/tail với offset và gain, ví dụ chết = thân + ink-dissolve −3 dB, boss death + dissolve +400 ms). `pitchJitter` 0,03: runtime chọn biến thể (không lặp liền) và lệch cao độ ±3 %. Tên sự kiện cũ giữ nguyên. Mọi file đầu tiếng tại transient, true peak ≤ −1 dBTP (không file nào vượt), momentary max theo mức: thường = chiêu T4 −6 dB (hit/chết −19,5, tiếng −18, hurt-heavy −17, vòng −25), tinh anh −3 dB (−16,5/−15/−22), captain (−14,5/−21), Thú Vương ngang chiêu (hit −13,5, lớn −11,5, vòng −19).

**Nối lab (không đụng five-thunder.ts):**
- `src/lab/foe-levels.ts` (sinh bởi `captures/tu-tien/foe-sound/gen_foe_ts.py` từ manifest; không sửa tay): mức đo từng file, bảng sự kiện (`FOE_EVENTS`: variants, target, bucket, nhóm giọng, layers), `FOE_PITCH_JITTER`.
- `src/lab/sound-tiers.ts`: `FIREFLY_LEVELS` gộp `FOE_LEVELS`, nên `fireflyGain` tính gain như mọi take Firefly.
- `src/lab/sound.ts`: `LabSound.foe(id, options)` chọn biến thể, lệch cao độ, đặt layers, gộp bucket 40 ms (trúng, đòn chạm) và 50 ms (chết) rồi đếm vào `foeMerged`, nhóm giọng impact/death/big theo `VoiceGroup`; `prepareFoes(ids?)` nạp trước các file (gói lớn: nên chỉ nêu loài đang dùng). Hook vào herd/hit (`skills-main.ts`) chưa làm, chờ anh gật clip.
- Test: `tests/lab/foe-sounds.test.ts` (5 test: mọi biến thể có mức, TP ≤ −1, tên cũ và mới đủ, không lặp biến thể và pitch trong ±3 %, layers, bucket). Cả `tests/lab`: 34 file, 420 test qua; `tsc` không báo lỗi ở các file chạm.

**Clip nghe thử v2:** `owner-review/2026-11-12/tu-tien/five-thunder-lab/foe-sound-v2-web.mp4` (26,5 s, 2,8 MB; foe + tiếng Ngũ Lôi −9 dB để cân): integrated **-20.7 LUFS** (loãng vì phần đuôi thưa), momentary max -15.5 LUFS, true peak **-5.8 dBTP**. 0–7,0 s: hình v16 với bầy sói/lợn/chuột (3 vòng bầy, spawn, gầm sói + gầm lợn, 24 tia: trúng nhẹ hoặc `-hurt-heavy` theo cỡ tia, 23 chết + dissolve, bucket gộp 5 tiếng, đòn kết = dissolve-chain). 7,0–26,5 s: hình dừng ở khung cuối để nghe các tiếng không có trong hình: 7,5 s elite-reveal + elite-wolf-roar; 10,5 s captain-entrance + captain-wolf-call; 14,0 s boss-entrance-roar rồi 14,8 s boss-boar-king-bellow; 18,5 s boss-boar-king-charge (+ boss-charge-impact lúc 19,8 s); 21,5 s boss-boar-king-death (+ dissolve). Danh sách 95 cue (biến thể và hệ số pitch từng tiếng): `captures/tu-tien/foe-sound/preview-measure-v2.json`. Bản v1 (`foe-sound-preview*.mp4`) giữ để so.

Kiểm máy 556 take (456 + 100): `captures/tu-tien/foe-sound/takes-foe.json`; script `build_foe.py` (bản trước `build_foe.v1.py`), `preview_foe_v2.py`, `gen_foe_ts.py`.

### Bản đồ loài (thường)
| Loài | spawn | di chuyển (loop) | gầm/hú | đòn (báo → chạm) | trúng nhẹ / nặng | chết | tinh anh | captain |
|---|---|---|---|---|---|---|---|---|
| wolf | wolf-spawn | wolf-run-loop | wolf-howl | wolf-snarl → wolf-bite | wolf-hurt / wolf-hurt-heavy | wolf-death + ink-dissolve + ink-dissolve | elite-wolf-roar | captain-wolf-call |
| boar | boar-spawn | boar-move-loop | boar-roar / boar-roar | boar-charge → boar-ram | boar-hurt / boar-hurt-heavy | boar-death + ink-dissolve + ink-dissolve | elite-boar-roar | captain-boar-call |
| rat | rat-spawn | rat-horde-loop | — | — → rat-gnaw | rat-hurt / rat-hurt-heavy | rat-death + ink-dissolve + ink-dissolve | elite-rat-roar | captain-rat-call |
| crow | crow-spawn | crow-flock-loop | crow-cry | crow-dive → crow-dive-hit | crow-hurt / crow-hurt-heavy | crow-death + ink-dissolve + ink-dissolve | elite-crow-roar | captain-crow-call |
| ape | ape-spawn | ape-steps-loop | ape-roar | ape-throw → ape-rock-hit | ape-hurt / ape-hurt-heavy | ape-death + ink-dissolve + ink-dissolve | elite-ape-roar | captain-ape-call |

Cấp: **tinh anh** = loài + elite-reveal, `elite-<loài>-roar` chồng gầm, elite-aura-loop, elite-hit, elite-armor-break, elite-stagger, elite-death (+3 dB). **Captain** = loài + captain-entrance, `captain-<loài>-call`, captain-aura-loop, captain-summon-arrive, captain-death (+5 dB). **Thú Vương (lợn)** = boss-boar-king-bellow / -charge / -death trên nền boss-*: entrance-roar + steps, breath-loop, seal-appear, charge-buildup → charge-launch(-clean) → charge-impact, rend-windup → rend-strike, pillar-crash, hit-heavy, stagger, phase-shockwave / phase2-roar / phase3-frenzy + frenzy-aura-loop, summon-howl, death → death-dissolve. Báo đòn: telegraph-circle/cone/line → telegraph-sting → strike-*, attack-cancelled. Bucket: trúng và đòn chạm 40 ms theo sự kiện, chết 50 ms (bucket đầy thêm `dissolve-chain`).

### Bảng sự kiện → nguồn (bản chính, rồi biến thể) → mức → bucket → đo → lý do
| Sự kiện | Nguồn Firefly | Mức (LUFS) | Bucket | Đo | Lý do |
|---|---|---|---|---|---|
| wolf-run-loop | wolf-pack-run-loop/take4 | common-loop (-25.0) | – | mom -25.0 · TP -11.8 · 4.0 s | take4: duy nhất lên đều không bị cắt cụt (take3 đuôi −16 dB); vòng 4 s mối nối 1 s |
| wolf-howl | wolf-howl/take8, beast-wolf-howl/take7, beast-wolf-howl/take4 | common-voice (-18.0) | – | mom -18.0 · TP -16.9 · 2.4 s | take8: không clip, tắt sạch (−64 dB), tiếng hú thuần dải giữa; take7 đuôi bị cắt (−34 dB) |
| wolf-snarl | wolf-snarl/take1 | common-attack (-19.5) | – | mom -19.5 · TP -13.5 · 0.6 s | take1: 2 mẫu clip (ít nhất), gầm gừ gọn; báo đòn cắn |
| wolf-bite | wolf-bite/take4 | common-attack (-19.5) | 40 | mom -19.5 · TP -7.6 · 0.4 s | take4: 4 mẫu clip (ít nhất trong 8), lên 89 ms, nhiều dải giữa 59 %; cắt 0,4 s |
| wolf-hurt | wolf-hurt/take3, beast-wolf-hurt/take2, beast-wolf-hurt/take4 | common-hit (-19.5) | 40 | mom -19.5 · TP -12.1 · 0.4 s | take3: lên 64 ms, không clip; cắt 0,4 s |
| wolf-death | wolf-death/take3, beast-wolf-death/take2 | common-death (-19.5) | 50 | mom -19.5 · TP -9.3 · 1.1 s | take3: không clip, đuôi −48 dB; take2 có 2 mẫu clip |
| boar-move-loop | boar-hoof-scrape/take8 | common-loop (-25.0) | – | mom -25.0 · TP -16.2 · 3.0 s | take8: móng cào có dải giữa 50 % (nghe ra móng), không clip; vòng 3 s |
| boar-spawn | boar-spawn/take3, beast-boar-spawn/take1, beast-boar-spawn/take2 | common-spawn (-21.0) | – | mom -21.0 · TP -12.9 · 1.2 s | take3: không clip, lên 79 ms, cân dải |
| boar-charge | boar-charge/take3, beast-boar-charge/take4 | common-attack (-19.5) | – | mom -19.5 · TP -10.4 · 1.2 s | take3: không clip, đuôi dài 1,25 s; báo đòn húc |
| boar-ram | boar-ram-impact/take1, beast-boar-ram-impact/take8 | common-attack (-19.5) | 40 | mom -19.5 · TP -12.5 · 0.45 s | take1: lên 12 ms (nhanh nhất), 5 mẫu clip như mọi bản, 23 % dải giữa |
| boar-hurt | boar-hurt/take2, beast-boar-hurt/take3 | common-hit (-19.5) | 40 | mom -19.5 · TP -8.8 · 0.4 s | take2: không clip, tắt sạch −60 dB; take3 sáng hơn nhưng có 1 mẫu clip |
| boar-death | boar-death/take3 | common-death (-19.5) | 50 | mom -19.5 · TP -12.8 · 1.2 s | take3: 3 mẫu clip (ít nhất), 22 % dải giữa; đuôi 1,37 s cắt về 1,2 s |
| rat-horde-loop | rat-horde-near-loop/take8 | common-loop (-25.0) | – | mom -25.0 · TP -14.1 · 4.0 s | take8: lách tách cao 97 %, không clip, mức đều (−12 LUFS, cuối −21 dB); vòng 4 s |
| rat-spawn | rat-spawn/take4, beast-rat-spawn/take3, beast-rat-spawn/take2 | common-spawn (-21.0) | – | mom -21.0 · TP -12.1 · 1.0 s | take4: lên 14 ms, 1 mẫu clip; take3 onset 125 ms chậm |
| rat-gnaw | rat-gnaw/take7, beast-rat-gnaw/take4, beast-rat-gnaw/take1 | common-attack (-19.5) | 40 | mom -19.5 · TP -4.9 · 0.4 s | take7: có thân (đuôi 0,64 s), không clip; take4 chỉ 53 ms quá cụt |
| rat-hurt | rat-hurt/take2, beast-rat-hurt/take3, beast-rat-hurt/take4 | common-hit (-19.5) | 40 | mom -19.5 · TP -14.0 · 0.4 s | take2: lên 33 ms, không clip, tắt sạch −59 dB (thay cắt tạm từ rít bầy) |
| rat-death | rat-death/take4, beast-rat-death/take1, beast-rat-death/take2 | common-death (-19.5) | 50 | mom -19.5 · TP -13.7 · 0.9 s | take4: onset 25 ms, không clip, tắt −69 dB (thay cắt tạm từ rít bầy) |
| crow-flock-loop | crow-flock-loop/take4 | common-loop (-25.0) | – | mom -25.0 · TP -5.6 · 4.0 s | take4: không clip, mức thấp đều (−22,6 LUFS); vòng 4 s từ 1,0 s |
| crow-cry | crow-cry/take8, beast-crow-cry/take4, beast-crow-cry/take2 | common-voice (-18.0) | – | mom -18.0 · TP -10.3 · 0.6 s | take8: onset 5 ms, 98 % dải giữa (tiếng quạ rõ), tắt −79 dB |
| crow-dive | crow-dive/take2, beast-crow-dive/take3, beast-crow-dive/take5 | common-attack (-19.5) | – | mom -19.5 · TP -10.4 · 1.2 s | take2: không clip, đuôi 1,5 s; báo đòn bổ nhào |
| crow-dive-hit | crow-dive-impact/take3, beast-crow-dive-impact/take4, beast-crow-dive-impact/take2 | common-attack (-19.5) | 40 | mom -25.5 · TP -1.0 · 0.282 s · trần | take3: không clip; take4 có 2 mẫu clip |
| crow-hurt | crow-hurt/take3, beast-crow-hurt/take2, beast-crow-hurt/take4 | common-hit (-19.5) | 40 | mom -19.5 · TP -11.0 · 0.4 s | take3: không clip, 97 % dải giữa, tắt −41 dB |
| crow-death | crow-death/take1, beast-crow-death/take4, beast-crow-death/take2 | common-death (-19.5) | 50 | mom -19.5 · TP -11.2 · 1.1 s | take1: không clip, đuôi dài hơn take4 (1,09 s), tắt −59 dB |
| ape-steps-loop | ape-footsteps/take2 | common-loop (-25.0) | – | mom -25.0 · TP -12.9 · 3.0 s | take2: không clip, tắt sạch; take4 bị cắt cụt (−2 dB cuối) |
| ape-roar | ape-roar/take4, beast-ape-roar/take7 | common-voice (-18.0) | – | mom -18.0 · TP -10.5 · 2.0 s | take4: lên 32 ms (gắt nhất), không clip; take7 lên chậm 634 ms |
| ape-throw | ape-throw/take4, beast-ape-throw/take1 | common-attack (-19.5) | – | mom -19.5 · TP -5.5 · 0.528 s | take4: không clip, 73 % dải giữa (vút tay) |
| ape-rock-flight | ape-rock-flight/take3, beast-ape-rock-flight/take1 | common-attack (-19.5) | – | mom -19.5 · TP -3.3 · 0.7 s | take3: không clip, êm; lớp bay của đá |
| ape-rock-hit | ape-rock-impact/take3, beast-ape-rock-impact/take7 | common-attack (-19.5) | 40 | mom -19.5 · TP -11.9 · 0.45 s | take3: 4 mẫu clip (ít nhất), lên 141 ms, 36 % dải giữa |
| ape-hurt | ape-hurt/take2, beast-ape-hurt/take3, beast-ape-hurt/take1 | common-hit (-19.5) | 40 | mom -19.5 · TP -11.9 · 0.4 s | take2: lên 94 ms, không clip, 94 % dải giữa |
| ape-death | ape-death/take3, beast-ape-death/take2 | common-death (-19.5) | 50 | mom -19.5 · TP -12.2 · 1.2 s | take3: 3 mẫu clip (bằng take2) nhưng 43 % dải giữa (rõ hơn) |
| ink-dissolve | common-ink-dissolve/take3, beast-common-ink-dissolve/take5, beast-common-ink-dissolve/take8 | common-death (-19.5) | 50 | mom -19.5 · TP -5.3 · 0.605 s | take3: không clip, 47 % > 4 kHz (mực tan xèo); lớp chồng lên mọi cái chết |
| dissolve-chain | common-dissolve-chain/take1, beast-common-dissolve-chain/take3, beast-common-dissolve-chain/take4 | common-death (-19.5) | – | mom -19.5 · TP -10.8 · 1.6 s | take1: không clip, 57 % > 4 kHz; bucket đầy (nhiều cái chết trong 50 ms) thêm một bản này |
| roar-canyon-tail | common-roar-canyon-tail/take1, beast-common-roar-canyon-tail/take3, beast-common-roar-canyon-tail/take4 | common-voice (-18.0) | – | mom -18.0 · TP -10.1 · 1.5 s | take1: bắt đầu ngay, không clip; đuôi vang cho gầm của tinh anh/boss |
| telegraph-circle | enemy-telegraph-circle/take6, enemy-telegraph-circle/take1, enemy-telegraph-circle/take5 | telegraph (-19.5) | – | mom -19.5 · TP -11.0 · 1.2 s | take6: không clip, có 26 % dải giữa (đọc được), tắt sạch |
| telegraph-cone | enemy-telegraph-cone/take1 | telegraph (-19.5) | – | mom -19.5 · TP -11.4 · 1.0 s | take1: không clip, onset 60 ms |
| telegraph-line | enemy-telegraph-line/take4 | telegraph (-19.5) | – | mom -19.5 · TP -7.3 · 1.0 s | take4: không clip; đuôi −7 dB bị cắt nên fade 0,3 s |
| telegraph-sting | enemy-telegraph-final-sting/take3, enemy-telegraph-final-sting/take2, enemy-telegraph-final-sting/take1 | telegraph (-19.5) | – | mom -19.5 · TP -9.6 · 0.6 s | take3: không clip, lên 136 ms, 36 % dải giữa; nốt cuối trước khi đòn rơi |
| strike-circle | enemy-strike-circle/take5 | elite-attack (-16.5) | – | mom -16.5 · TP -9.7 · 0.6 s | take5: không clip, onset 12 ms |
| strike-cone | enemy-strike-cone/take2, enemy-strike-cone/take1 | elite-attack (-16.5) | – | mom -16.5 · TP -9.6 · 0.5 s | take2: 2 mẫu clip (ít nhất) |
| strike-line | enemy-strike-line/take4 | elite-attack (-16.5) | – | mom -16.5 · TP -2.8 · 0.6 s | take4: 1 mẫu clip (ít nhất) |
| attack-cancelled | enemy-attack-cancelled/take4, enemy-attack-cancelled/take3, enemy-attack-cancelled/take1 | common-hit (-19.5) | – | mom -19.5 · TP -11.3 · 0.6 s | take4: không clip, có 21 % > 4 kHz (tiếng 'tịt') |
| elite-reveal | elite-reveal-aura/take7, elite-reveal-aura/take6, elite-reveal-aura/take3 | elite-voice (-15.0) | – | mom -15.0 · TP -8.0 · 1.6 s | take7: không clip, lên 118 ms, tắt −51 dB |
| elite-roar | elite-empowered-roar/take1, elite-empowered-roar/take2, elite-empowered-roar/take4 | elite-voice (-15.0) | – | mom -15.0 · TP -7.9 · 1.8 s | take1: không clip, 90 % dải giữa; chồng lên gầm loài |
| elite-aura-loop | elite-iron-hide-aura-loop/take2 | elite-loop (-22.0) | – | mom -22.0 · TP -12.9 · 4.0 s | take2: không clip, đuôi dài 4,2 s mức đều; vòng 4 s |
| elite-hit | elite-hit-iron-hide/take2, elite-hit-iron-hide/take4, elite-hit-iron-hide/take1 | elite-hit (-16.5) | 40 | mom -16.5 · TP -7.6 · 0.4 s | take2: lên 32 ms, 63 % > 4 kHz (kim loại), không clip |
| elite-armor-break | elite-armor-break/take4, elite-armor-break/take8 | elite-hit (-16.5) | – | mom -30.0 · TP -1.0 · 0.103 s · trần | take4: onset 3 ms, 4 mẫu clip (ít nhất) |
| elite-stagger | elite-stagger-fall/take1, elite-stagger-fall/take3, elite-stagger-fall/take4 | elite-hit (-16.5) | – | mom -16.5 · TP -9.3 · 0.9 s | take1: không clip, đuôi 1,0 s |
| elite-death | elite-death-roar/take1 + (lab chồng ink-dissolve), elite-death-roar/take2, elite-death-roar/take4 | elite-death (-16.5) | 50 | mom -16.5 · TP -9.4 · 1.2 s | take1: không clip, 60 % dải giữa với 39 % trầm (có thân) |
| elite-seal-appear | elite-seal-appear/take4, elite-seal-appear/take1, elite-seal-appear/take2 | elite-voice (-15.0) | – | mom -15.0 · TP -6.0 · 1.0 s | take4: không clip, −11 LUFS đủ nghe; take1 quá nhỏ |
| elite-seal-break | elite-seal-break/take1, elite-seal-break/take7, elite-seal-break/take8 | elite-hit (-16.5) | – | mom -23.7 · TP -1.0 · 0.526 s · trần | take1: lên 14 ms, 23 % > 4 kHz (vỡ), không clip |
| captain-entrance | captain-entrance/take4 | captain-voice (-14.5) | – | mom -14.5 · TP -3.5 · 1.6 s | take4: không clip; take3 có 7 mẫu clip và đuôi cắt |
| captain-howl | captain-howl-call/take2, captain-howl-call/take1, captain-howl-call/take3 | captain-voice (-14.5) | – | mom -14.5 · TP -7.8 · 2.4 s | take2: không clip, đuôi 2,8 s; gọi bầy |
| captain-aura-loop | captain-aura-loop/take3 | captain-loop (-21.0) | – | mom -21.0 · TP -13.7 · 4.0 s | take3: không clip, tắt sạch −67 dB nên vòng êm |
| captain-summon-arrive | captain-summon-arrive/take4 | captain-voice (-14.5) | – | mom -14.5 · TP -7.8 · 1.2 s | take4: không clip, onset 0,6 ms |
| captain-death | captain-death/take1, captain-death/take2, captain-death/take3 | captain-death (-14.5) | 50 | mom -14.5 · TP -13.0 · 1.5 s | take1: không clip, đuôi 2,5 s cắt 1,5 s |
| boss-entrance-roar | boss-entrance-roar/take6, boss-entrance-roar/take7 | boss-voice (-11.5) | – | mom -11.5 · TP -4.7 · 2.4 s | take6: không clip, 58 % dải giữa (gầm rõ) |
| boss-steps | boss-entrance-steps/take2 | boss-loop (-19.0) | – | mom -19.0 · TP -5.3 · 3.0 s | take2: không clip, tắt sạch; take1 cắt cụt (−5 dB) |
| boss-footstep | boss-footstep/take3, boss-footstep/take2, boss-footstep/take1 | boss-hit (-13.5) | – | mom -13.5 · TP -5.2 · 0.6 s | take3: không clip, −9,4 LUFS đầy; một bước |
| boss-breath-loop | boss-breath-loop/take4 | boss-loop (-19.0) | – | mom -19.0 · TP -10.4 · 4.0 s | take4: không clip, bắt đầu ngay, mức đều; vòng 4 s |
| boss-seal-appear | boss-seal-appear/take2, boss-seal-appear/take4, boss-seal-appear/take3 | boss-voice (-11.5) | – | mom -11.5 · TP -3.3 · 1.2 s | take2: không clip, onset 20 ms |
| boss-charge-buildup | boss-charge-buildup-loop/take2 | boss-loop (-19.0) | – | mom -19.0 · TP -13.3 · 3.0 s | take2: không clip; take3 có 8 mẫu clip và cắt cụt; vòng 3 s |
| boss-charge-launch | boss-charge-launch-clean/take4, boss-charge-launch-clean/take2 | boss-big (-11.5) | – | mom -11.5 · TP -2.3 · 0.981 s · alias | tên cũ giữ cho lab: nay trỏ bản sạch (take4); bản cũ 13 mẫu clip đã bỏ |
| boss-charge-impact | boss-charge-impact/take6, boss-charge-impact/take2 | boss-big (-11.5) | – | mom -11.5 · TP -3.7 · 1.6 s | take6: lên 54 ms (nhanh nhất), 21 % dải giữa, 4 mẫu clip; take2 ít clip hơn nhưng toàn trầm và lên 1,3 s |
| boss-rend-windup | boss-rend-windup/take4, boss-rend-windup/take2 | boss-voice (-11.5) | – | mom -11.5 · TP -2.5 · 1.2 s | take4: không clip, lên 196 ms, có 8 % > 4 kHz (rít) |
| boss-rend-strike | boss-rend-strike/take1 | boss-big (-11.5) | – | mom -11.5 · TP -4.8 · 0.9 s | take1: 1 mẫu clip (ít nhất), onset 66 ms cắt bỏ |
| boss-pillar-crash | boss-pillar-crash/take4 | boss-big (-11.5) | – | mom -11.5 · TP -2.1 · 2.0 s | take4: không clip, lên 147 ms, đuôi 2,4 s |
| boss-hit-heavy | boss-hit-heavy/take3, boss-hit-heavy/take2 | boss-hit (-13.5) | 40 | mom -13.5 · TP -5.1 · 0.6 s | take3: lên 94 ms, không clip, đuôi 0,75 s (take2 cụt 0,26 s) |
| boss-stagger | boss-stagger/take4, boss-stagger/take8, boss-stagger/take6 | boss-hit (-13.5) | – | mom -13.5 · TP -5.9 · 1.6 s | take4: không clip, lên 157 ms, 14 % dải giữa |
| boss-phase-shockwave | boss-phase-shockwave/take1 | boss-big (-11.5) | – | mom -11.5 · TP -3.8 · 1.6 s | take1: 2 mẫu clip (ít nhất) |
| boss-phase2-roar | boss-phase2-roar/take3 | boss-voice (-11.5) | – | mom -11.5 · TP -3.6 · 2.4 s | take3: không clip, đuôi 2,25 s |
| boss-phase3-frenzy | boss-phase3-frenzy/take6, boss-phase3-frenzy/take4 | boss-voice (-11.5) | – | mom -11.5 · TP -3.4 · 2.4 s | take6: 2 mẫu clip (ít nhất), 92 % dải giữa (gào) |
| boss-frenzy-aura-loop | boss-frenzy-aura-loop/take2 | boss-loop (-19.0) | – | mom -19.0 · TP -9.8 · 4.0 s | take2: không clip, 31 % dải giữa; vòng 4 s |
| boss-summon-howl | boss-summon-howl/take3, boss-summon-howl/take2, boss-summon-howl/take4 | boss-voice (-11.5) | – | mom -11.5 · TP -6.4 · 2.0 s | take3: không clip, tắt sạch −67 dB |
| boss-death | boss-death/take3, boss-death/take5 | boss-death (-11.5) | – | mom -11.5 · TP -4.8 · 3.0 s | take3: không clip, đuôi 2,8 s |
| boss-death-dissolve | boss-death-dissolve/take1, boss-death-dissolve/take4 | boss-death (-11.5) | – | mom -11.5 · TP -2.7 · 3.0 s | take1: không clip, 19 % > 4 kHz, đuôi 4 s; chồng sau boss-death 0,4 s |
| wolf-spawn | wolf-spawn/take3, beast-wolf-spawn/take1, beast-wolf-spawn/take2 | common-spawn (-21.0) | – | mom -21.0 · TP -9.9 · 0.836 s | take3: không clip, tắt sạch (cuối −36..−70 dB); âm thật cho spawn wolf thay mượn tiếng loài khác |
| crow-spawn | crow-spawn/take3, beast-crow-spawn/take1 | common-spawn (-21.0) | – | mom -21.0 · TP -1.4 · 0.861 s | take3: không clip, tắt sạch (cuối −36..−70 dB); âm thật cho spawn crow thay mượn tiếng loài khác |
| ape-spawn | ape-spawn/take3, beast-ape-spawn/take4, beast-ape-spawn/take2 | common-spawn (-21.0) | – | mom -21.0 · TP -5.8 · 0.974 s | take3: không clip, tắt sạch (cuối −36..−70 dB); âm thật cho spawn ape thay mượn tiếng loài khác |
| boar-roar | boar-roar/take3, beast-boar-roar/take4, beast-boar-roar/take2 | common-voice (-18.0) | – | mom -18.0 · TP -9.0 · 0.981 s | take3: không clip, onset 19 ms, tắt −49 dB; gầm riêng của lợn (trước đó thiếu) |
| wolf-hurt-heavy | wolf-hurt-heavy/take2, beast-wolf-hurt-heavy/take1, beast-wolf-hurt-heavy/take4 | common-hit-heavy (-17.0) | 40 | mom -17.0 · TP -9.4 · 0.45 s | take2: không clip, đuôi sạch; trúng nặng riêng cho wolf (trước đây wolf-hurt + ink-dissolve) |
| boar-hurt-heavy | boar-hurt-heavy/take3, beast-boar-hurt-heavy/take4, beast-boar-hurt-heavy/take2 | common-hit-heavy (-17.0) | 40 | mom -17.0 · TP -6.6 · 0.352 s | take3: không clip, đuôi sạch; trúng nặng riêng cho boar (trước đây boar-hurt + ink-dissolve) |
| rat-hurt-heavy | rat-hurt-heavy/take4, beast-rat-hurt-heavy/take2, beast-rat-hurt-heavy/take1 | common-hit-heavy (-17.0) | 40 | mom -17.0 · TP -7.3 · 0.45 s | take4: không clip, đuôi sạch; trúng nặng riêng cho rat (trước đây rat-hurt + ink-dissolve) |
| crow-hurt-heavy | crow-hurt-heavy/take3, beast-crow-hurt-heavy/take2, beast-crow-hurt-heavy/take4 | common-hit-heavy (-17.0) | 40 | mom -17.0 · TP -8.4 · 0.45 s | take3: không clip, đuôi sạch; trúng nặng riêng cho crow (trước đây crow-hurt + ink-dissolve) |
| ape-hurt-heavy | ape-hurt-heavy/take2, beast-ape-hurt-heavy/take3, beast-ape-hurt-heavy/take4 | common-hit-heavy (-17.0) | 40 | mom -17.0 · TP -9.6 · 0.45 s | take2: không clip, đuôi sạch; trúng nặng riêng cho ape (trước đây ape-hurt + ink-dissolve) |
| elite-wolf-roar | elite-wolf-roar/take2 | elite-voice (-15.0) | – | mom -15.0 · TP -9.8 · 1.8 s | take2: 7 mẫu clip, ít nhất trong 4 (take1 có 22); trần −1 dBTP nuốt đỉnh; gầm tinh anh riêng cho wolf (thay elite-roar chung) |
| elite-crow-roar | elite-crow-screech/take4, beast-elite-crow-screech/take1, beast-elite-crow-screech/take3 | elite-voice (-15.0) | – | mom -15.0 · TP -6.6 · 1.8 s | take4: không clip, tắt −68 dB; gầm tinh anh riêng cho crow (thay elite-roar chung) |
| elite-boar-roar | elite-boar-bellow/take2, beast-elite-boar-bellow/take4, beast-elite-boar-bellow/take3 | elite-voice (-15.0) | – | mom -15.0 · TP -7.3 · 1.8 s | take2: không clip, tắt −60 dB; gầm tinh anh riêng cho boar (thay elite-roar chung) |
| elite-ape-roar | elite-ape-roar/take2, beast-elite-ape-roar/take3 | elite-voice (-15.0) | – | mom -15.0 · TP -7.7 · 1.8 s | take2: không clip, tắt −66 dB; gầm tinh anh riêng cho ape (thay elite-roar chung) |
| elite-rat-roar | elite-rat-shriek/take2, beast-elite-rat-shriek/take4, beast-elite-rat-shriek/take1 | elite-voice (-15.0) | – | mom -15.0 · TP -6.9 · 1.8 s | take2: không clip, tắt −66 dB, đuôi 1,6 s; gầm tinh anh riêng cho rat (thay elite-roar chung) |
| captain-wolf-call | captain-wolf-call/take2, beast-captain-wolf-call/take4, beast-captain-wolf-call/take3 | captain-voice (-14.5) | – | mom -14.5 · TP -12.1 · 1.954 s | take2: không clip, đuôi 1,5 s; tiếng gọi bầy riêng của captain wolf |
| captain-crow-call | captain-crow-call/take3, beast-captain-crow-call/take2, beast-captain-crow-call/take4 | captain-voice (-14.5) | – | mom -14.5 · TP -7.0 · 1.997 s | take3: onset 3 ms, tắt −68 dB; tiếng gọi bầy riêng của captain crow |
| captain-boar-call | captain-boar-call/take2, beast-captain-boar-call/take3, beast-captain-boar-call/take4 | captain-voice (-14.5) | – | mom -14.5 · TP -5.0 · 1.944 s | take2: không clip, đuôi 1,7 s; tiếng gọi bầy riêng của captain boar |
| captain-ape-call | captain-ape-call/take4, beast-captain-ape-call/take1, beast-captain-ape-call/take3 | captain-voice (-14.5) | – | mom -14.5 · TP -4.3 · 1.978 s | take4: không clip, tắt −56 dB; tiếng gọi bầy riêng của captain ape |
| captain-rat-call | captain-rat-call/take2, beast-captain-rat-call/take1, beast-captain-rat-call/take3 | captain-voice (-14.5) | – | mom -14.5 · TP -7.5 · 1.965 s | take2: không clip, tắt −70 dB; tiếng gọi bầy riêng của captain rat |
| boss-charge-launch-clean | boss-charge-launch-clean/take4, boss-charge-launch-clean/take2 | boss-big (-11.5) | – | mom -11.5 · TP -2.3 · 0.981 s | take4: không clip (4 take cũ đều 13 mẫu clip), onset 38 ms |
| boss-boar-king-bellow | boss-boar-king-bellow/take1, boss-boar-king-bellow/take4, boss-boar-king-bellow/take3 | boss-voice (-11.5) | – | mom -11.7 · TP -1.0 · 2.98 s · trần | take1: không clip, lên 94 ms, đuôi 2,7 s, tắt −54 dB |
| boss-boar-king-charge | boss-boar-king-charge/take3, boss-boar-king-charge/take1, boss-boar-king-charge/take4 | boss-big (-11.5) | – | mom -11.5 · TP -4.8 · 1.969 s | take3: không clip, lên 116 ms, đuôi 1,7 s |
| boss-boar-king-death | boss-boar-king-death/take1, boss-boar-king-death/take3, boss-boar-king-death/take4 | boss-death (-11.5) | – | mom -11.5 · TP -4.2 · 2.992 s | take1: không clip, onset 8 ms, tắt −61 dB |

Còn thiếu: IR hồi vang sân (chưa có; đang dùng `aecho`). Chưa có tiếng riêng cho captain ở cấp cuối cùng ngoài sói (cả 5 loài đã có tiếng gọi), và chưa có footage lab với tinh anh, captain, Thú Vương nên chưa nghe được đúng khung hình của chúng.
