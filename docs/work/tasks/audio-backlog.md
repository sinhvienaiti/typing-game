# Âm thanh: bảng việc tồn đọng toàn bộ Tu Tiên Thủ Ải (12/11/2026)

Người làm: Claude (tổng hợp từ nguồn, không nghe file nào, không mở ảnh). Số đếm lấy bằng `ls`, `find`, `grep`, `python` trên cây mã ngày 12/11. Ô nào ghi "không rõ" là chưa kiểm được.

## 1. Tóm tắt

1. **Nguyên liệu thô:** 657 việc trong `docs/work/tasks/firefly-sprint-sound.json`; trên đĩa `art-src/lab/firefly-sprint-2026-11-05/sound/` có 659 thư mục, 3.144 bản WAV (nhiều nhất: `x` 30 việc/240, `el` 56/224, `beast` 36/192, `ult` 21/152, `twin` 19/116, `world` 21/116, mỗi hệ trong 14 hệ 22–23 việc/88–100). Thêm 4 tiếng hô (`callouts/`, 12 bản WAV) và lô 03/11 đã nằm trong `audio/` (91 file Kim + Lửa).
2. **Đã nối trong lab (`.wt-ic-lab-all/src/lab`):** 24 sự kiện gốc `SOUND_IDS`; 132 thư mục sự kiện theo hệ (13 hệ × 10, Lửa 12; 396 file `.ogg`, 3 bản mỗi thư mục); 71 mục `SPRINT_TAKES` và 11 mục `LAB_TAKES` phát thẳng bản Firefly; 129 dòng đo mức trong `FIREFLY_LEVELS`.
3. **Đã chấm:** chỉ **đo máy** (ffmpeg ebur128: 34 sự kiện lô 03/11; 129 bản Firefly; 12 việc Ngũ Lôi). **Chưa có tai người nào nghe và chưa có điểm 8,5 của giám khảo mù** cho bất kỳ âm nào của Tu Tiên (`SOUND_AUDIT_2026-11-04.md`, `SOURCES.json` ghi "NOT LISTENED").
4. **Trong game thật:** `games/immortality-cultivation/src/audio/catalog.ts` vẫn mở đầu bằng "mọi id `silent: true`" (71 id). Chưa thấy hook phát file nào (chưa kiểm hết `hooks.ts`).
5. **Năm khoảng trống lớn nhất theo tác động người chơi:** (a) tai anh chưa nghe gì và game im lặng; (b) Ngũ Lôi và 12 hệ chiêu còn lại chưa chọn bản, chưa chuẩn hoá mức; (c) quái, boss, tinh anh, tiếng gầm/chết/trúng phần lớn chưa nối; (d) không có nhạc nền, không có tiếng môi trường nối; (e) tiếng hô k1, dash, ult, Song Long có file nhưng chưa thấy nối.

## 2. Theo hệ thống

Ký hiệu: Nguồn = tệp đã đọc. "Chọn" = đã chọn bản và chuẩn hoá bằng số đo. P = ưu tiên 1–3 (1 là gấp nhất).

| Hệ thống | Nguyên liệu có | Chọn và chuẩn hoá | Đã nối | Đã chấm | Còn thiếu | P | Nguồn |
|---|---|---|---|---|---|---|---|
| Gõ phím / typing feedback | 5 hồ sơ phím (Creamy, Thock, Clicky, Soft Dome, Classic Spring) × 10 phím + 3 phím cách, làm bằng Stable Audio 3 | Có cổng L1–L6 của Audio Lab; chọn bộ bằng `keys/pick.py` | Lab nạp bộ "Typing Feel" dùng chung, `KEYS_MIX` (bus +7 dB, dip 4 kHz −3 dB) trong `sound-tiers.ts` | Máy L1–L6; **điểm tai anh cho Tu Tiên: không rõ** (không thấy `keys.ratings` trong `owner-data/ratings`) | Chuẩn chung 9 (hai giám khảo + anh); đo "bài lặp 20 lần"; chưa rõ bộ nào hiện đang chọn | 2 | `SHARED_SYSTEMS_BAR.md`, `tools/audio-lab/SESSION_KEYS.md`, `TYPING_FEEL_SERVICE.md`, `sound.ts` |
| Kỹ năng theo 14 hệ × pha (cast, flyby, release, dash, impact vật/đá/hồn, world mở/đỉnh/đóng) | 14 hệ × ~22 việc `tt-sfx-<hệ>-*` (Kim 22, Lửa 23, Lôi 23, Phong 23, còn lại 22), 4 việc hệ × chiêu năm pha (`el-*` 56 việc) | **Chưa chuẩn hoá**: ba bản đầu mỗi việc, Vorbis q5, "không chuẩn hoá" (phiếu 330). Chỉ Kim và Lửa có `SOUND_TRIM_DB` và bậc `SOUND_TIER` | 13 hệ × 10 thư mục (Lửa 12) trong `audio/`, phát `<sự kiện>-<hệ>` khi chọn hệ | Chỉ Kim + Lửa đo (04/11). 12 hệ còn lại không đo | Trim và bậc cho 12 hệ; lớp lấp lánh (Lửa cao tần 0–2 %); `el-*` (gồng/ấn/sao/tai ương) chưa thấy nối | 1 | `SOURCES.json`, `sound-tiers.ts`, `SOUND_AUDIT_2026-11-04.md`, `firefly-sprint-sound.json` |
| Vũ khí × hệ (kiếm, đao, thương; 42 việc hệ × vũ khí + melee 14 hệ) | 14 việc `sabre-swing`, `spear-thrust`, `combo-finisher`, `flying-sword-launch` mỗi loại, 13 `sword-swing`; 42 việc `element × sword/sabre/spear` | Như dòng trên | Lớp `sword-*`/`hit-*` nằm trong các thư mục sự kiện (72 + 72 lớp trong SOURCES) | Không | Đao và Thương chưa có sự kiện riêng trong `SOUND_IDS`; chưa rõ tách lớp theo vũ khí đã nối chưa | 2 | `WEAPON_AUDIO.md`, `WEAPON_AUDIO_FIREFLY_BATCH1.md`, `firefly-sprint-sound.json` |
| Tuyệt kỹ (k5/k7, world-open/climax/close, `ult-*`) | `ult` 21 việc/152 bản, `world` 21 việc (đa số là nền, xem dòng môi trường), `k5` 3, `k7` 1 | Có mức cho 20 mục `ult-*`/`k5-*`/`world-open-punch`; k5-release-instant đo −32,6 LUFS nên có gain bù | 20 mục trong `SPRINT_TAKES` | Chỉ đo; 04/11 phát hiện thứ bậc ngược (k7, guard to hơn đỉnh) | Chưa nghe; kiểm lại thứ bậc to sau trộn (`lab-sound-mix` chưa duyệt); tiếng hô ult chưa nối | 1 | `sound.ts`, `sound-tiers.ts`, `SOUND_AUDIT_2026-11-04.md`, `captures/tu-tien/lab-sound-mix/ABOUT.md` |
| Ngũ Lôi Oanh Đỉnh | 12 việc đã phân tích: `thunder-cast/crack/big-burst/tail/hit-light/hit-heavy/combo-finisher`, `el-thunder-seal/affliction`, `trib-lightning-strike/strike-warning/thunder-roll-loop` | Chưa chọn (có `takes.json` đo transient, TP, phổ; **tệp `five-thunder-sound.md` không tồn tại** dù bài khác nhắc) | Chưa thấy `thunder-five` trong `src/lab` | Chỉ đo | Chọn, cắt, mức, gán 5 pha (trận pháp mặt đất, dồn dập 12–20 tia, đòn kết, dư âm); tạo mới nếu cần | 1 | `five-thunder-lab.md`, `captures/tu-tien/five-thunder-sound/{ABOUT.md,takes.json}` |
| Chiêu mở rộng 30 (A1–D8) | 30 việc `tt-sfx-x-*`, 240 bản | Mức đo cho cả 30 (ví dụ `x-nine-heavens-tribulation-net/take2` −7,7); take-chọn trong `clip-skills.ts` | 30 mục trong `FIREFLY_LEVELS`, trường `sound` trong `clip-skills.ts` | Chỉ đo | Chưa nghe; một bản (progenitor-avatar take 4) gần câm −37 nên đổi take 3 | 2 | `sound-tiers.ts`, `clip-skills.ts`, `SKILLS_EXPANSION_2026-11-05.md` |
| Song Long (k2) | 19 việc `twin-*`/116 bản (chuông, gầm A–C, vút lửa, boom, vọng núi, lách tách, lấp lánh) | Có mức cho cả 19 | 19 mục `SPRINT_TAKES` | Chỉ đo | Bản cuối còn đổi thiết kế (bầy rồng khí): cue sheet F0–F65 cần dựng lại theo nhịp mới; tiếng hô twin chưa nối | 2 | `SOUND_AUDIT_2026-11-04.md` §4, `twin-dragons.md`, `sound.ts` |
| Quái, tinh anh, boss (trúng, chết, gầm) | `beast` 36 việc/192 bản (sói, quạ, lợn, vượn, chuột, chung), `boss` 20/108, `elite` 13/68, `captain` 5/28, `enemy` 12/60 (báo đòn, đòn vòng/nón/tia) | Có mức cho beast 9, boss 6, elite 3, enemy 1 | 19 mục trong `SPRINT_TAKES` (sói, quạ, lợn chết/đau, boss vào/pha 2/chết, elite hào quang/chết, khiên) | Chỉ đo | Chưa nối: vượn, chuột, captain (5), báo đòn (11), elite còn 10, boss còn 14 | 1 | `sound.ts`, `sound-tiers.ts`, `firefly-sprint-sound.json` |
| Trúng, hạ, bầy | `confirm-*` 4 việc, `mass` 2, `swarm` 1, `impact` 3 | Mức −24 / −18 | 3 xác nhận + 2 mass-kill + 1 swarm trong `SPRINT_TAKES` | Chỉ đo | Tick xác nhận theo chất liệu đã nối; đuôi đồng cho elite có; chưa nghe độ mỏi khi lặp | 2 | `sound.ts`, `SOUND_AUDIT_2026-11-04.md` §2 |
| Cơ quan, bẫy, phù, trận | `mech` 3 (khóa lưới ấn, cọc kiếm, xích lôi), `pillar` 3, `guard` 2, `meteor` 1, `channel` 4, `streak` 4 | Có mức cho pillar 3, guard 2, meteor 2, channel 5, streak 4; `mech` không | Các mục trên nối; `mech` không thấy | Chỉ đo | `mech` 3 chưa chọn, chưa nối; trận pháp, Kết Giới, Trận Tâm: không thấy việc riêng | 2 | `firefly-sprint-sound.json`, `sound.ts`, `sound-tiers.ts` |
| UI và menu | `ui` 16 việc/76, `reward` 11/60, `meditation` 4/20, `meta` 1 | Mức cho 6 `ui-*` (−28 đến −18) | 6 mục UI trong `SPRINT_TAKES` | Chỉ đo | `reward` 11, `meditation` 4, `ui` còn 10 chưa nối; không rõ danh sách UI cần so với `catalog.ts` | 2 | `sound.ts`, `ART_AUDIO_VFX_PLAN.md` §5 |
| Callout / giọng | Cũ: 6 tiếng hô (hey/ha, k2, guard, k4, k5, k7), một giọng Brittney qua Firefly Speech. Mới: 4 câu × 3 bản (`callout-k1/dash/ult/twin`, 12 WAV) | Cũ có EQ và vang riêng; mới chưa xử lý | Cũ nối (`SOUND_IDS`); mới **chưa thấy** trong `SOUND_TIER` | Chỉ đo cũ (04/11); anh duyệt 4 câu 05/11 | Chọn bản, cắt, nối `callout-k1/dash/ult/twin`; chưa có tiếng hô Ngũ Lôi và chiêu mở rộng | 2 | `callouts.md`, `SOURCES.json`, `sound-tiers.ts` |
| Môi trường và nhạc nền | `world` 21 việc: ambience trận/ải, formation hum, tide, wave start/clear/warning, victory, defeat, heart pulse; `trib` 10 (Thiên Kiếp) | Chưa | Chưa: bus nhạc chỉ nhận `?music=<url>`, không có file nhạc | Không | **Nhạc nền chưa có file nào** (kế hoạch: `music.hold` 4 lớp); 20 tiếng thế giới và 10 Thiên Kiếp chưa nối | 2 | `ART_AUDIO_VFX_PLAN.md` §5, `sound-tiers.ts` (`MUSIC`), `firefly-sprint-sound.json` |
| Cut-in | `cutin` 9 việc/48 bản | Có mức cho 8 | 8 mục `cutin-*` trong `SPRINT_TAKES` | Chỉ đo | Một việc chưa nối; cut-in vẫn "chờ sửa phiếu 268" nên canh khung theo cut-in mới | 3 | `sound.ts`, `BOARD.md` (Đỗ lại) |
| Hạ tầng trộn | Bus combat/voice/world, trần giọng, send vang chung (`VERB_RETURN`, `SEND_LEVEL`), duck nhạc | Bậc T2–T6, `TIER_TARGET`, `CALLOUT_TRIM_DB` | Có trong lab | Test: `sound-tiers`, `sound-mix`, `sound-element`, `lane5`, `laneB3` | Chưa duyệt bằng tai; âm 285 (gộp tiếng, ép bus) chưa đạt cổng 3 LU, đang đỗ | 1 | `sound-tiers.ts`, `tests/lab/*sound*`, `BOARD.md` |

## 3. Việc tiếp theo

| Id | Việc | Đầu vào có sẵn | Ai làm | Ước lượng |
|---|---|---|---|---|
| A1 | Buổi nghe 1 cho anh: bản trộn lab hiện tại (Kim, Lửa, Song Long, tuyệt kỹ, cut-in), anh chấm từng nhóm | `captures/tu-tien/lab-sound-mix/`, `sound-tiers/` | Phiên lab, Claude gửi video | 1 phiên, anh nghe 20–30 phút |
| A2 | Ngũ Lôi: chọn bản, cắt, đặt mức, gán 5 pha, nối vào lab, viết `docs/work/tasks/five-thunder-sound.md` | `takes.json`, 12 việc ở mục 2 | Phiên lab (flipbooks) | 1 phiên |
| A3 | Chuẩn hoá 12 hệ còn lại: đo, trim, bậc, đặt vào `SOUND_TRIM_DB` và `SOUND_TIER` | 132 thư mục sự kiện hệ, `scripts/audio/lab-sound-tiers.mjs` | Phiên lab (Claude) | 1 phiên |
| A4 | Nối tiếng hô mới k1/dash/ult/twin; chọn bản, EQ, vang | `callouts/` 12 WAV, `callouts.md` | Phiên lab | nửa phiên |
| B1 | Nối quái, boss, tinh anh, captain, báo đòn (phần chưa nối) và chọn bản theo mức | 5 nhóm ở mục 2, `FIREFLY_LEVELS` | Phiên lab | 1–2 phiên |
| B2 | Dựng lại cue sheet Song Long theo thiết kế bầy rồng khí | `twin-dragons.md`, 19 mục `twin-*` | Phiên lab sau khi sim xong | 1 phiên |
| B3 | Lớp lấp lánh cho Lửa (cao tần) và 12 hệ: tạo mới khi bản hiện có dưới 8 % phổ > 4 kHz | `SOUND_AUDIT` §2 | Firefly tạo mới (giới hạn ≈ 70 bản/ngày) | không rõ, phụ thuộc đo ở A3 |
| B4 | Nối `reward`, `meditation`, `ui` còn lại, `trib`, `mech` | ≈ 40 việc đã có bản | Phiên lab | 1–2 phiên |
| C1 | Nhạc nền `music.hold` 4 lớp và nền môi trường | `ART_AUDIO_VFX_PLAN.md` §5; Firefly Soundtrack (đang không rõ có không) | Firefly tạo mới hoặc Audio Lab | không rõ, chưa có nguyên liệu |
| C2 | Nối thật vào game (`catalog.ts` bỏ `silent`, hook theo sự kiện) | lab đã có mix | Claude, phiếu Codex khi đủ hạn mức (≥ 15 %) | 1–2 phiếu |
| C3 | Chấm mù hai giám khảo ≥ 8,5 trong bản chơi; tiếng phím ≥ 9 | Quy trình `game-art-pipeline` | Claude + anh nghe | sau C2 |

## 4. Không chắc (đã kiểm gì)

- **Game thật phát âm hay không:** mới đọc đầu `catalog.ts` và `silent: true`; chưa đọc `hooks.ts` và chưa chạy bản chơi.
- **Mục "đã nối" của `SPRINT_TAKES`:** đếm bằng `grep` dòng khai báo (71) và `FIREFLY_LEVELS` (129 dòng); chưa chạy lab để biết mục nào thực sự được sự kiện gọi.
- **Tiếng phím Tu Tiên:** không thấy tệp điểm của anh cho bộ phím (`owner-data/ratings` chỉ có dragon-hold, typing-defense, typing-survival, _calib); nên không rõ anh đã nghe chưa.
- **Lô 03/11** (`FIREFLY_BATCH_2026-11-03.md`) và `WEAPON_AUDIO.md` (763 dòng): chỉ đọc tiêu đề và lô 1; số bản lô 03/11 lấy từ `SOURCES.json` và `SOUND_AUDIT` (91 file, 34 sự kiện).
- **Số "việc" so với "thư mục":** JSON có 657 việc, đĩa có 659 thư mục; chênh 2 chưa tìm nguyên nhân. Ghi chú `counts: 83 việc` trong JSON là số cũ của vòng 1.
- **Việc Firefly hôm nay:** BOARD ghi giới hạn ≈ 70 bản/ngày và bộ chạy chưa sửa cho giao diện mới; không kiểm trạng thái tài khoản.
- **Tiếng hô cũ so với mới:** `SOUND_AUDIT` nói thiếu k1/dash/ult; `SOUND_IDS` vẫn chưa có chúng, nhưng có thể được nối ở `skills-main.ts` (chưa đọc kỹ).
- **Thiên Kiếp và mục `world`:** coi là "chưa nối" vì không thấy trong `SPRINT_TAKES` hoặc `FIREFLY_LEVELS`; chưa tìm chỗ gọi khác ngoài `sound.ts`, `sound-tiers.ts`, `showcase.ts`, `clip-skills.ts`.
