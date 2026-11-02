# Âm vũ khí và bộ chiêu Kiếm: spec (02/11/2026)

> **Trạng thái:** spec để tạo âm. Chưa tạo, chưa nghe file nào. Lượt soát 2 (02/11, sau D56) và lượt soát 3 (02/11: luật, sim, chất D56) đã xong; danh sách lỗi đã sửa ở §5. Lô đầu cho anh tạo: [`WEAPON_AUDIO_FIREFLY_BATCH1.md`](WEAPON_AUDIO_FIREFLY_BATCH1.md).
> **Hình món:** đang vẽ lại theo binh khí Trung Hoa có thật (phương pháp mới ở [`art-requests/weapons/JUDGING.md`](../art-requests/weapons/JUDGING.md), vòng 2). Lớp B (§1.3, §3.4) viết theo bóng dáng mới nhận ngày 02/11 và vẫn là nháp tới khi anh duyệt tấm vũ khí.
> **Nguồn thắng:** canon [D55, D56, §12.1 (tick chạm), §22 (Q6, bus, ưu tiên, 32/16 tiếng)](../00-canon.md); [`WEAPON_DESIGN.md`](WEAPON_DESIGN.md) §5–6; [`SKILL_CATALOG.md`](SKILL_CATALOG.md) §1–2; skill `game-art-pipeline` [`references/audio.md`](../../../../.agents/skills/game-art-pipeline/references/audio.md) §5 (thắng mọi luật viết cho phím); [`AUDIO_PIPELINE.md`](../../AUDIO_PIPELINE.md) §4–7; [`ART_AUDIO_VFX_PLAN.md`](../ART_AUDIO_VFX_PLAN.md) §5–6; lab chiêu `games/immortality-cultivation/src/view/skills/kiem.ts` (khung lóe).

**Phong cách (canon D56, anh 02/11, thắng mọi dòng bên dưới):** "chúng ta k làm ra kiểu âm thanh như thật… phải bùng nổ, đẹp, hào quang, thu hút của các phim anime hoặc các thần thoại, tiểu thuyết".
- Mọi cue của chiêu là **cảnh tượng phép kiểu anime, donghua và thần thoại**, không phải foley như thật. Chất phép đi theo pha và lớn dần theo bậc, để đòn thường vẫn nhỏ hơn tuyệt kỹ (audio.md §5.4):

| Pha | Chất phép (lớp P) | Bậc thấp (T2–T3: K0, K1, nhịp K4) | Bậc cao (T4–T6: K2, K3A đỡ, K4 mở, K5) |
|---|---|---|---|
| Gồng | dồn năng lượng: ngân rền lấp lánh, dâng | bed ngân dưới phím; kiếm hiện, góc trận sáng có hạt lấp lánh | thêm swell dâng từ 80 % (K2, K5) |
| Phát | bùng phép, vút lấp lánh | `magic-cast`: 120–250 ms, đầu sắc | `magic-release`: đủ thân, có sub |
| Bay | vệt lấp lánh | hạt lấp lánh trên tiếng rít | bầy kiếm; hợp xướng hoặc synth dâng (chỉ K5) |
| Trúng | bùm năng lượng, hạt lấp lánh | `magic-hit`: đầu sáng có hạt lấp lánh, không sub (trừ kiếm 3 của K1) | `magic-impact`: bùm trầm, sub, sóng chấn |
| Dư âm | đuôi hào quang lấp lánh | đuôi 0,8–1,2 s | đuôi T4 1,5–2,5 s, T5–T6 2–3 s, vang hẻm núi |

Các cue T3 không phải đòn thường (K3A dựng, K3B lướt, K4 phát: 250–500 ms) dùng lớp P bậc thấp (`magic-cast`) nhưng dài hơn, vì chúng là một phát lớn mỗi từ, không lặp 0,83 lần/s như K0.

- Tiếng thép, ngọc, đá, nước thật chỉ là **nguyên liệu nằm dưới lớp phép**, không bao giờ là cả cue. Một cue nghe như tiếng kiếm thật, dù sạch, vẫn hỏng.
- Lớp **P phép** (§3.10) nướng trong cue cùng lớp đầu của pha, nên không thêm tiếng chạy. B và C đổi theo món; P đổi theo bậc chiêu. Bậc độ to, trần tiếng và luật vang giữ nguyên.
- "Chuông pha lê" của D56 nằm ở lớp B và P qua các chữ crystalline, chime, shimmer. Prompt không dùng chữ bell (tránh chuông chùa, canon §22). Hợp xướng là giọng không lời, không được nghe như tụng (canon §22).
- Mốc so sánh khi nghe: tiếng chiêu của Genshin Impact, Honkai: Star Rail, Wuthering Waves và các donghua Đấu La, Đấu Phá, Phàm Nhân Tu Tiên.

**Luật nền**
- Âm chiến đấu theo audio.md §5: ghép lớp, có bậc độ to, bùng nổ, vang. Luật phím mềm (AUDIO_PIPELINE §6.2 và dòng "Luật giọng đọc" của canon §22) chỉ áp cho `key-*` và âm chữ thành chiêu `key-word`.
- Pha nào có lóe thì có tiếng **cùng khung** (skill `game-vfx-layered` bước 8). Âm đi theo sự kiện của view; không đổi tick sim.
- Chỉ file thật: Firefly Generate Sound Effects, model Adobe, do anh tạo (audio.md §2; canon §22 dòng Nguồn còn ghi CC0 hoặc Stable Audio 3: việc mở 14). Chữ "synth" trong prompt là chất của file Firefly tạo, không phải âm dựng bằng code. Sub tổng hợp chỉ được làm một lớp nướng sẵn bên trong file thật (audio.md §5.7 bước 2). Game không có `OscillatorNode` (canon §22, D44).
- Mọi mẫu gửi anh duyệt (D55). Agent không nghe được: máy chỉ gắn cờ và xếp hạng, tai anh quyết.

## 1. Mô hình lớp

### 1.1 Sáu loại lớp

| Lớp | Thuộc về | Đổi khi | Ví dụ |
|---|---|---|---|
| **A họ** | kiếm, đao, thương | đổi họ (đổi luôn bộ chiêu K → Đ, T) | kiếm "shing" cao, sáng |
| **B món** | 1 trong 10 món đợt 1 | đổi món | Clear Wind: vòng ngọc ngân pha lê |
| **C hệ** | 8 hệ | đổi sang món khác hệ | Lôi: sét thần nổ |
| **P phép** | mọi chiêu | đổi theo bậc chiêu, không theo món | bùng phép, vệt lấp lánh, bùm năng lượng, đuôi hào quang |
| S chiêu | từng chiêu: trận, vòng hộ thân, cột sáng, bầy kiếm | không đổi theo món | 3 kiếm sáng quay của K3A |
| Chung | sub, đuôi không gian hẻm núi | không đổi | vọng hẻm đá vôi |

- **Ranh giới B, C, P:**
  - B là **giọng riêng của món**: một nốt có cao độ hoặc một chất riêng (vòng ngọc, băng kết tinh, ấn sấm, cánh sen ngọc).
  - C là **kết cấu năng lượng của hệ** (sét, lửa, sóng, gió, băng vỡ…), thường không có cao độ.
  - P là **phép chung**: dồn, bùng, vệt, bùm, hạt lấp lánh không cao độ, hào quang.
  - Ba lớp không được là cùng một tiếng. Ví dụ Winter Vein: B là tiếng ngân băng pha lê có cao độ, C Băng là băng vỡ, P là bùm và hạt lấp lánh. Ember Crest: B là gai lửa bùng xèo, C Hỏa là lửa linh bùng.
- Bộ Kiếm chỉ dùng họ kiếm và 4 món kiếm. Món đao và thương thuộc bộ Đ và T (làm sau). Lớp A của hai họ đó có id ở §3 để đặt nền từ đầu.

### 1.2 Lớp A: họ

A là đầu tiếng và thân nằm dưới lớp P: nó cho mỗi họ một dáng âm riêng, còn chất phép do P mang.

| Họ | Chữ ký (WEAPON_DESIGN §5) | Phát (R) | Bay (T) | Trúng (I) | Đuôi (F) | Dải chính | Dùng cho |
|---|---|---|---|---|---|---|---|
| Kiếm | "shing" cao, thép reo sáng | rút kiếm reo sáng, chém vút có năng lượng | rít ngân, nhanh | kiếm linh chém đá giòn, thân chém dày, tiếng reo có cao độ | vọng thép lấp lánh trong hẻm đá vôi | đầu 3–8 kHz | K0–K5 (đợt này) |
| Đao | "whum" trầm, nặng | rút đao nghiến thép, chém cung trăng ù trầm | ù trầm | chẻ đá dữ, thân chặt nặng | vọng nặng hẻm sâu | thân 80–300 Hz | Đ0–Đ5 (sau) |
| Thương | "thuk" gọn | đâm xuyên có năng lượng, cán quất | cán quất, vút lấp lánh | đâm xuyên giáp gọn, thân đẩy chắc | vọng khe núi lấp lánh | đẩy 100–250 Hz, nứt 2–5 kHz | T0–T5 (sau) |

Kiếm reo cao **không** được miễn luật trầm của T4–T6 (§4.1): mọi cue T4 trở lên của bộ Kiếm có lớp sub chung (`common-sub`); loạt 3 của K5 thêm `magic-sub`.

### 1.3 Lớp B: món (bóng dáng mới 02/11; nháp tới khi anh duyệt tấm vũ khí)

| Món | Họ · Hệ | Bóng dáng (binh khí gốc) | Tiếng món (B) | Vai riêng | Đợt |
|---|---|---|---|---|---|
| Clear Wind | Kiếm · Kim | jian, đốc vòng | vòng ngọc nhạt ngân pha lê, có cao độ | nốt chữ ký của mọi cú trúng: thép reo kèm nốt ngọc | S1 |
| Winter Vein | Kiếm · Băng | jian, hộ thủ rộng hai thùy | lưỡi rèn băng ngân, hạt băng pha lê | trúng để lại tiếng rạn băng lấp lánh ngắn (residue Băng 0,6–1 s) | S2 |
| Thunder Seal | Kiếm · Lôi | jian, hộ thủ chữ nhật bậc | ấn sấm đóng xuống, ngân điện rền | ba nốt điện khác cao độ cho ba kiếm: biến thể cố định theo thứ tự kiếm, không ngẫu nhiên | Đổi |
| Verdant Branch | Kiếm · Mộc | jian, hộ thủ sen bốn cánh thấp | sen ngọc nở bùng, cánh pha lê ngân, có cao độ | bầy kiếm K5 nghe như mưa cánh sen ngọc (kit trail chồng lên bed bầy) | S2 |
| Ember Crest | Đao · Hỏa | yanmaodao, một gai ở sống | gai lửa bùng xèo | lửa cam đỏ thật ở lớp C (D54) | L |
| Mountain Verdict | Đao · Thổ | niuweidao (đao đuôi trâu) | thép nặng ngân trầm như núi | tiếng núi dưới tiếng thép | L |
| Tidal Crescent | Đao · Thủy | liuyedao (đao lá liễu) | lưỡi cong rạch nước lấp lánh | cung nước dài, không thành vòng | L |
| Sky Thread | Thương · Phong | qiang mũi lá dài | mũi thương hát trong gió, còi có cao độ | còi kéo dài trong 1–4 kHz: xử như đuôi (hạ 2–4 dB, nhường giọng đọc) | L |
| Resonant Fang | Thương · Kim | ji một lưỡi bên | lưỡi bên ngân dài pha lê | mỗi cú trúng một tiếng ngân 0,8–1,2 s; không được nghe thành chuông chùa | L |
| Storm Pin | Thương · Lôi | ji hai lưỡi bên ngắn | rít điện dâng cao | snap điện gọn ở lõi | L |

- **Chất chung của bộ** (thép satin bạc lạnh, sứ trắng, điểm ngọc nhạt, lụa chàm): tiếng nghe sạch, lạnh, sang. Ngân trong, không rỉ, không lạch cạch kiểu giáp trung cổ.
- **Đợt:** S1 lát cắt demo, S2 phần còn lại của bộ Kiếm, L sau khi có bộ Đ, T (§4.3).

### 1.4 Lớp C: hệ

| Hệ | Màu nhấn (SKILL_CATALOG §1) | Ignite (phát, bay) | Burst (trúng) | Residue (dư âm) | Họ "bẩn" (AUDIO_PIPELINE §4.4) |
|---|---|---|---|---|---|
| Kim | `#D6CFC0` | năng lượng kim loại bùng, hạt lấp lánh | mưa mảnh kim loại sáng, va ngân | ngân bạc lấp lánh tắt dần | không |
| Mộc | `#6E8B5E` | dây linh mộc trồi, gỗ nứt | rễ linh phá đá, gỗ toác | lá phát sáng cuộn trong gió | không |
| Thủy | `#2E4A78` | nước phép dâng | sóng linh đập | nước phép xoáy trên đá | không |
| Hỏa | `#FF7A2A` (D54) | lửa linh bùng | cầu lửa nổ rền | than hồng, tàn lửa lấp lánh | có |
| Thổ | `#A08C6A` | phép đất rền, đá nghiến | phép đất nện, đá vỡ | sỏi lăn, bụi lắng | có |
| Lôi | `#9AA6FF` | phép sấm bật hồ quang | sét thần nổ | dư điện lách tách, tia lấp lánh | có |
| Phong | `#BFD8C8` | gió linh giật, vút lấp lánh | lốc nổ | gió linh hú hẻm núi | không |
| Băng | `#CFE6F5` | băng phép kết tinh | băng phép vỡ, va pha lê | sương giá lan, lấp lánh | có |

Họ "bẩn": audiobox có trọng số 0, chỉ xếp hạng bằng L2 và lựa chọn của anh.

### 1.5 Lớp nào phát ở pha nào

| Pha | A họ | S chiêu | B + C (món) | P phép | Chung |
|---|---|---|---|---|---|
| Gồng | — | bed gồng (K2–K5), swell (K2, K5) | `kit-appear` (kiếm K1 hiện, góc K4 sáng), `kit-charge` | ngân rền trong bed; dâng trong swell | — |
| Phát | rút, vung | lớp riêng của K2, K3A, K3B, K4, K5 | chữ ký B + ignite C, **nướng trong cue** | `magic-cast` (T2–T3) hoặc `magic-release` (T4–T5), nướng | sub từ T4 |
| Bay | rít bay | bed bầy K5 (có hợp xướng) | `kit-trail` (ignite C kéo dài; còi Sky Thread, điện Thunder Seal): nướng vào `cue-sword-travel` và `cue-k1-launch`; chỉ K5 chồng lúc chạy | `magic-trail`, nướng | — |
| Trúng | đầu, thân, tiếng reo | chém tuyến, cắm, đỡ, mưa kiếm | nốt B + burst C, **nướng trong cue** | `magic-hit` (T2–T3) hoặc `magic-impact` (T4–T6), nướng; loạt 3 K5 thêm `magic-sub` | sub từ T4 và ở kiếm 3 của K1 |
| Dư âm | đuôi họ | đóng, hết | `kit-residue` (C) | `magic-aura` trong đuôi | đuôi không gian, send |

### 1.6 Đổi vũ khí

- **Cue nướng theo món:** mọi cue một phát (phát, rời kiếm, bay, trúng, mở, nhịp, đỡ, loạt) là một file cho mỗi món, dựng offline từ A, S, P cộng B và C (§3.8). Một tiếng mỗi cue, mỗi file đúng bậc của nó (audio.md §5.4: "file nói đúng mức của nó").
- **Kit của món:** 4 stem `tt-sfx-kit-<món>-{appear,charge,trail,residue}`. `appear`, `charge`, `residue` chồng lên lúc chạy; `trail` nướng vào cue bay, chỉ K5 chồng nó lúc chạy (§3.7).
- **Dùng chung, không đổi theo món:** bed gồng, swell, vòng lặp K3A và K4, bed bầy K5, đuôi. Lớp P cũng dùng chung: đổi món không đổi P.
- **Đổi món** (chọn trước trận, đề xuất WEAPON_DESIGN §7): nạp và giải mã bộ cue nướng và 4 stem kit của món mới lúc vào trận; trong trận không đổi. Ước ~60–65 file mỗi món kiếm (đếm theo §3.8), ~6 MB sau giải mã.
- **Ví dụ:**
  - Clear Wind → Thunder Seal: A giữ, B đổi, C Kim → Lôi, P giữ.
  - Clear Wind → Resonant Fang: A kiếm → thương (và bộ chiêu T), B đổi, C giữ Kim, P giữ.
- **Nếu anh chốt hệ tách khỏi món** (câu hỏi D55 và D23 còn mở): dựng lại cue theo cặp (món, hệ) bằng cùng công thức. Master nguyên liệu B và C giữ riêng nên chỉ chạy lại script, không tạo lại âm.
- **Kiểm đổi món:** hai bản trộn cùng kịch bản, chỉ khác món. Khoảng cách âm học giữa hai món (mel 0–50 ms, đường bao; AUDIO_PIPELINE §5.2) phải lớn hơn độ trải giữa các biến thể của cùng món. Anh nghe mù và đoán đúng món.

## 2. Bộ Kiếm theo pha

### 2.1 Luật chung

- **Gồng (A)** theo tiến độ gõ 0–20–40–60–80–100 %:
  - File bed đặt ở −24 LUFS-M max; code hạ theo tiến độ: −10, −8, −6, −4, −2, 0 dB (tức −34 → −24). Lọc thấp mở dần. Phần dâng do code làm, nên file bed là vòng lặp đều, không tự dâng.
  - Không thêm tiếng mỗi chữ: phím đã có tiếng (bus `typing`). Bed luôn ở dưới hoặc bằng mức phím trong bản trộn (−28 đến −24).
  - Khi còn 1 chữ, bed hạ −6 dB trong 60 ms. Đây là nhịp "hít" trước phát, thay khoảng lặng 40–80 ms của súng nặng (audio.md §5.3): game không biết trước lúc phím cuối đến, còn phát phải ≤ 50 ms sau phím cuối.
  - **Swell (K2, K5)** là vòng lặp sáng đều (§3.8); code dâng nó theo tiến độ như bed, không theo đồng hồ: bắt đầu ở 80 % với −30, tăng đều theo chữ, tới −22 khi còn 1 chữ; lọc thấp mở dần và `playbackRate` lên tối đa +1 bán cung (swell không chứa nốt B). Như vậy swell chỉ vượt mức phím (tối đa 2 LU) trong chữ cuối, ở mọi tốc gõ và mọi độ dài từ. Phím cuối cắt nó trong 10 ms.
  - Phím cuối: cắt bed trong 10 ms khi Cast resolve ngay. Từ hụt hoặc Esc: tắt trong 120 ms.
  - **Cast bị giữ** (không có mục tiêu, hoặc ô 1 đã có 2 băng chưa xong; `sim/cast.ts`, `sim/skills.ts`): phím cuối vẫn cắt swell; bed (nếu chiêu có) về −30 trong 60 ms và giữ tới `cast resolved` hoặc `fizzled`. Tiếng phát theo `cast resolved`. `fizzled` (sau 3 s) không có tiếng phát; nó phát `type.word-fizzle` (ART_AUDIO_VFX_PLAN §5.1) và tắt bed trong 120 ms.
- **Phát (R)** đúng khung lóe R của view, theo `cast resolved` (≤ 50 ms sau phím cuối khi Cast resolve ngay), chung khung với `key-word`. `key-word` thuộc hệ phím chung (mốc 9), không bị hạ.
- **Bay (T):** tiếng bay bắt đầu cùng khung kiếm rời tay hoặc rời vai, và kết thúc đúng tick chạm.
  - K0: kiếm rời ở tick Cast, bay 18 tick.
  - K1: mỗi kiếm, cả kiếm 1, rời 6 tick trước tick chạm (`launchTick` của sim): ở 0, +30, +60 tính từ **base của băng**. Base là tick Cast, hoặc tick chạm kiếm 3 của băng trước khi băng này nối sau (canon §12.1, `skills.ts`), nên kiếm 1 của băng nối có thể rời muộn tới 66 tick sau lóe R. Mỗi sự kiện `skill-fx` stage `volley` của ô 1 phát một `cue-k1-launch` 100 ms, kèm lóe ở vai; `cue-k1-release` chỉ là lóe phát, không chứa tiếng bay.
  - Hai lần rời cùng tick trong một băng (kiếm Kiếm Tâm rời cùng kiếm 3) gộp thành một `cue-k1-launch`.
  - Pan theo x của mục tiêu, |pan| ≤ 0,6. Không làm doppler bằng `playbackRate`, vì cue bay chứa `kit-trail` mang giọng B (luật nốt ±20 cent); cảm giác lướt qua do pan và lọc thấp theo khoảng cách.
- **Trúng (I)** đúng tick canon, theo sự kiện của chiêu:
  - K0, K1, K3A đỡ, nhịp K4 có thú: theo sự kiện `hit` (đỡ: `ward block`). K2: view hẹn ở tick Cast + 12 từ sự kiện `skill-fx` stage `line`, rồi chọn theo số `hit` của ô 2 trong tick đó: 0 → `cue-k2-impact-empty`, 1–2 → `cue-k2-impact`, ≥ 3 → `cue-k2-impact-mass`. K5: mỗi loạt theo sự kiện `skill-fx` stage `ultimate` (sim phát cả khi trúng 0 thú), không theo `hit`. Lý do: lab lóe và dừng hình ở các tick này dù không trúng thú, và pha nào lóe thì có tiếng.
  - Gom mọi cú trúng trong 38 ms thành một cue. Bậc cao nhất trong lô thắng.
  - Lớp mass chỉ có ở K2 (`cue-k2-impact-mass` khi lô ≥ 3 thú) và K5 (nướng sẵn trong mỗi loạt). K0, K1 và nhịp K4 không có bản mass: số thú hiện qua tiếng thú.
  - Thân của nạn nhân (lông, đá, giáp) thuộc danh sách thú (`beast-hit-*`); cue vũ khí không chứa tiếng thú. Mỗi lô 38 ms có tối đa 1 tiếng thú.
- **Dư âm (F):**
  - Đuôi là file riêng (`.tail`), dưới phần khô 8 LU (T2–T4) hoặc 6 LU (T5–T6).
  - Vang IR lọc 200 Hz–6,5 kHz. Dải 1–4 kHz hạ 2–4 dB và nhường giọng đọc.
  - **Trễ trước 25 ms do code làm:** file `.tail` bắt đầu ngay (qua cổng im lặng đầu ≤ 5 ms của L1), code hẹn giờ phát nó ở +25 ms sau cue khô. Cue có đuôi nướng (`cue-k3a-end`, `cue-k4-close`) và bản nghe giữ trễ trước 25 ms bên trong file, sau phần khô.
  - IR theo bậc (audio.md §5.7 bước 4): 2,5 s cho đuôi thường K0, K1 và đuôi nướng, cắt còn 1,2 s; 3,5 s cho T4, phát và loạt 1–2 của K5; 4 s cho đuôi loạt 3 của K5. Độ dài đuôi trong §2.2 là đích; đo sau bước 5, lệch thì đổi độ dài IR hoặc cắt bằng `atrim` và `afade`.
  - Lớp hào quang `magic-aura` trong đuôi lọc cao 150 Hz nhưng giữ hạt lấp lánh tới 12 kHz, và cũng hạ 3 dB ở 1–4 kHz. Lý do: luật lọc thấp 6–7 kHz của audio.md §5.5 giữ vang khỏi đục; hạt lấp lánh trên 6 kHz nằm ngoài dải giọng 1–4 kHz và là chữ ký D56 (việc mở 9).
- **Dừng hình** (theo lab: K2 30 ms, K3A đỡ 30 ms, K4 mở 30 ms, K5 loạt 3 70 ms; K4 mở có trong bản lab đang sửa ngày 02/11): âm không dừng, không chậm lại (bài H). Bản build dùng `IC_FEEDBACK_PROFILE` (`src/view/feedback-profile.ts`), hiện cho K2 (bậc phản hồi T2) 0 ms; lab và hồ sơ phải thống nhất (việc mở 17).
- **Bậc gõ thêm lớp, không thêm gain.** Bậc gõ chỉ có ở chiêu có từ; K0 tự động nên không có bậc.
  - Hoàn hảo: nốt B sáng hơn (bản Hoàn hảo của ba cue trúng K1).
  - Chớp: thêm sub chung và một nốt B cao hơn một quãng tám (bản Chớp). Cố định, để người chơi học được.
  - Kiếm Tâm: sim cho kiếm 4 chạm cùng tick với kiếm 3, nên hai kiếm vào cùng lô 38 ms và phát `cue-k1-hit-heart` (bản Chớp của kiếm 3 thêm một nốt B +7 bán cung).
  - Sự kiện `hit` và `skill-fx` `volley` hiện không cho biết kiếm thứ mấy. View cần trường `part` (0–3) và cờ `extra` (kiếm Kiếm Tâm) để chọn nốt leo 0, +2, +4, chọn `cue-k1-hit-heart` và chọn bản `kit-trail` của Thunder Seal (việc mở 6; chỉ thêm trường sự kiện, không đổi tick).
  - K2–K5: lát cắt chưa có bản theo bậc gõ (việc mở 10).
- **Biến thể:**
  - Offline: 3–5 bản cho cue có đầu và thân. Cue chứa nốt B hoặc `kit-trail` đổi take đầu, thân và lớp P trước khi trộn (như `cue-k0-hit`), không chạy `asetrate` của bước 9 trên cả cue. Bước 9 (±1,5 bán cung) chỉ cho cue không có B.
  - Lúc chạy: cue chứa nốt B hoặc `kit-trail` ±20 cent (Thunder Seal 0 cent, vì ba nốt điện là biến thể cố định); nốt leo của K1 ≤ ±10 cent để quãng 0, +2, +4 vẫn nghe rõ; cue không có B (`cue-k3b-land`, `cue-k4-beat-empty`) ±60 cent.
- **Định dạng:** cue khô là mono (game pan theo vị trí). Đuôi, bed, vòng lặp và mọi cue của K5 là stereo: đây là ngoại lệ với cổng L1 "mono" của AUDIO_PIPELINE §4.3.1 (việc mở 15). Khi làm đuôi từ cue khô mono, nâng phần khô lên stereo trước (§3.9).

### 2.2 Bảng mỗi chiêu

Tick 60 Hz tính từ tick Cast (canon §12.1); riêng K1 tính từ base của băng (§2.1, Bay). "Bậc" là LUFS-M max đích của cue (audio.md §5.4); cue có stem chồng lúc chạy đặt file thấp hơn 1 LU và đo tổng (§3.8). "Nhóm" là nhóm tiếng ở §2.3.

**K0 Phi Kiếm** (tự động, mỗi 1,2 s, tầm 10 m; catalog `kiem-auto`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | — | không: 0,83 lần/s, có tiếng gồng sẽ mỏi tai | | | | | |
| Phát | lệnh `auto`, khung lóe | `cue-k0-release` | T2 · −19 | 120–200 ms | — | 0,10 | release |
| Bay | 0 → +18 | `cue-sword-travel` | dưới phát 3 LU | 250–300 ms | — | 0,05 | travel |
| Trúng | +18 | `cue-k0-hit` | T3 · −19 | 150–250 ms | — | 0,05 | hit |
| Dư âm | sau trúng | `cue-sword-tail` | khô − 8 LU | 0,8–1,2 s | là đuôi | 0 | tail |

**K1 Ngự Kiếm Quyết** (mỗi từ một băng 3 kiếm, chờ tối đa 2 băng; `kiem-volley`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | tiến độ 15, 45, 75 % (mỗi kiếm hiện sau vai, theo lab) | `kit-appear` | −30, dưới phím | 120 ms | — | 0 | charge |
| Phát | lóe R (`cast resolved`) | `cue-k1-release`: một file cho cả băng, chỉ là lóe phát (tiếng bay ở `cue-k1-launch`) | T2 · −17 | 150–250 ms | — | 0,10 | release |
| Bay | mỗi kiếm rời 6 tick trước tick chạm: 0, +30, +60 tính từ base của băng (sự kiện `skill-fx` `volley`, lóe ở vai) | `cue-k1-launch` (Thunder Seal: bản theo `part`), kết thúc ở tick chạm; hai lần rời cùng tick gộp một | dưới phát 3 LU | 90–110 ms | — | 0,05 | travel |
| Trúng | +6, +36, +66 từ base của băng | `cue-k1-hit-1`, `cue-k1-hit-2`, `cue-k1-hit-3` (theo `part`): nốt B 0, +2, +4 bán cung; kiếm 3 thêm sub; bản Hoàn hảo và Chớp; Kiếm Tâm (cờ `extra`): `cue-k1-hit-heart` | T3 · −18, −17, −16 | 150–250 ms (kiếm 3 ≤ 300 ms) | — | 0,05 | hit |
| Dư âm | sau kiếm 3 | `cue-sword-tail`, một đuôi mỗi băng | khô − 8 LU | 1–1,2 s | là đuôi | 0 | tail |

**K2 Nhất Tuyến Xuyên Vân** (đường 14 × 1,2 m; `kiem-line`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | lúc gõ; swell từ 80 % | `cue-charge-bed` + `kit-charge`; `cue-k2-swell` | bed −34 → −24; swell −30 → −22 | theo gõ; swell vòng lặp, code dâng tới chữ cuối, cắt ở phím cuối | — | 0,05 | charge |
| Phát | lóe R | `cue-k2-release` (có sub) | T4 · −13 | 250–400 ms | — (một đuôi sau trúng) | 0,25 | heavy |
| Bay | 0 → +12 | nằm trong `cue-k2-release` (0,2 s) | | | | | |
| Trúng | +12 (hẹn từ `skill-fx` `line`), dừng hình 30 ms (lab) | `cue-k2-impact`; lô ≥ 3 thú dùng `cue-k2-impact-mass`; không trúng thú dùng `cue-k2-impact-empty` | T4 · −12 (trống −13) | 300–500 ms | `cue-k2-tail` | 0,25 | heavy |
| Dư âm | sau trúng (rãnh mực 4 s) | `cue-k2-tail` + `kit-residue` | khô − 8 LU; residue −24 | 2–2,5 s | là đuôi | 0 | tail |

Cú trúng K2 hạ các cú trúng thường 3 dB trong 150 ms.

**K3A Hồi Kiếm Hộ Thân** (vòng r 2 m, 5 s, 3 lần đỡ; `kiem-ward`, `kiem-ward-block`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | lúc gõ | `cue-charge-bed` + `kit-charge` | −34 → −24 | theo gõ | — | 0,05 | charge |
| Phát | lóe R (vòng triện dựng) | `cue-k3a-up` | T3 · −17 | 300–500 ms | — | 0,10 | release |
| Giữ | 5 s | `cue-k3a-loop`: một file chứa cả 3 kiếm quay | −22 | vòng 2–4 s, liền mối | — | 0,05 | loop |
| Đỡ | sự kiện `ward block`, dừng hình 30 ms | `cue-k3a-block` | T4 · −13 | 250–450 ms | `cue-k3a-block-tail` 1,5–2 s | 0,25 | heavy |
| Hết | hết giờ hoặc hết 3 lần | `cue-k3a-end` | T2 · −19 | khô 300–450 ms; cả đuôi nướng ≤ 1,2 s | nướng | 0 | release |

**K3B Lưu Quang Bộ** (lướt 5 m, không sát thương; `kiem-dash`)

| Pha | Khi | Cue | Bậc | Dài | Send | Nhóm |
|---|---|---|---|---|---|---|
| Gồng | lúc gõ | `cue-charge-bed` | −34 → −24 | theo gõ | 0,05 | charge |
| Phát | lóe R | `cue-k3b-dash` | T3 · −17 | 250–400 ms | 0,08 | release |
| Đến | hết lướt (sự kiện đến của view; game lướt 0,3 s theo `local/dash.ts`, lab đang 0,2 s: việc mở 6) | `cue-k3b-land` (lớp phụ) | −22 | 120–200 ms | 0,05 | travel |

Không có pha trúng, không có đuôi riêng.

**K4 Lạc Kiếm Trận** (vùng r 3 m, 5 s; `kiem-zone`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | lúc gõ; mỗi góc trận sáng ở 1/6 … 5/6 tiến độ (lab; góc 6 sáng cùng phím cuối, nằm trong phát) | `cue-charge-bed` + `kit-charge`; `kit-appear` mỗi góc | −34 → −24; `kit-appear` −30 | theo gõ; `kit-appear` 120 ms | — | 0,05 | charge |
| Phát | lóe R (kiếm vút lên) | `cue-k4-release` | T3 · −16 | 300–500 ms | — | 0,10 | release |
| Mở | +12 (`zone-open`; lab cắm cả 6 kiếm cùng khung), dừng hình 30 ms | `cue-k4-open`: một file flam 6 cú trong 0–40 ms, sub ở +6 ms; nhịp đầu nằm trong file này | T4 · −12 | 400–700 ms | `cue-k4-tail` 2–2,5 s | 0,25 | heavy |
| Giữ | +12 → +312 | `cue-k4-loop` | −22 | vòng 2–4 s | — | 0,05 | loop |
| Nhịp | +42, +72 … +282 (9 nhịp sau nhịp mở) | `cue-k4-beat` (có thú) / `cue-k4-beat-empty` | T3 · −17 / nền −23 | 150–250 ms | — | 0,05 | hit |
| Đóng | +312 (`zone-close`; lab đang đóng ở 5 s, tức +300: việc mở 6) | `cue-k4-close` + `kit-residue` | T2 · −18 | khô 400–700 ms; cả đuôi nướng ≤ 1,5 s | nướng | 0 | release |

Nhịp xoay vòng 5 biến thể và không lặp liền. Lớp nhịp vẫn phát khi vùng trống, vì VFX vẫn lóe mỗi nhịp.

**K5 Thiên Hà Kiếm Vũ** (3 loạt, r 6 m; T5–T6, sự kiện P0; `kiem-ultimate`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | lúc gõ; swell từ 80 % | `cue-k5-charge-bed` (bed chung trộn sẵn lớp `kiem-charge-air`) + `kit-charge`; `cue-k5-swell` | −34 → −24; swell −30 → −22 | theo gõ; swell vòng lặp, code dâng tới chữ cuối, cắt ở phím cuối | — | 0,05 | charge |
| Phát | lóe R (cột sáng, vòng đất) | `cue-k5-release` (sóng chấn, cắt mềm) | T5 · −11 | 0,4–0,5 s khô | `cue-k5-tail-0` 2 s | 0,40 | big |
| Bay | 0 → +120 | `cue-k5-swarm-low` (có hợp xướng), `cue-k5-swarm-high`, `cue-k5-swarm-whistle` + `kit-trail`; đường bao phồng lên ở +30, +75, +120 | tổng −16 | 2,4 s | — | 0,20 | swarm |
| Loạt 1 | +30 (sự kiện `skill-fx` `ultimate`, có cả khi trúng 0 thú) | `cue-k5-volley-1` | T5 · −10 | 0,4–0,7 s | `cue-k5-tail-1` 2 s | 0,40 | big |
| Loạt 2 | +75 (như loạt 1) | `cue-k5-volley-2` (nốt B +1 bán cung) | T5 · −9 | 0,4–0,7 s | `cue-k5-tail-2` 2 s | 0,40 | big |
| Loạt 3 | +120 (như loạt 1), dừng hình 70 ms | `cue-k5-volley-3` (nốt B +2, thêm sóng chấn thứ hai và đá vụn) | T6 · −8 | 0,6–1 s | `cue-k5-tail-3` 3 s | 0,40 | big |
| Dư âm | sau loạt 3 | `cue-k5-tail-3` + `kit-residue` (chỉ High) | khô − 6 LU; residue −24 | 2–3 s | là đuôi | 0 | tail-big |

- Nhạc được hạ trước mỗi loạt ở tick +25, +70, +115 (83 ms trước cú chạm, trong khoảng 60–100 ms); bảng hạ tiếng ở §2.4.
- **Âm không theo số kiếm của bậc hình** (150/300/500 chỉ là hình, sim như nhau). Bậc Low bỏ `cue-k5-swarm-high` và `cue-k5-swarm-whistle` vì kho `self` ở Low chỉ có 4 tiếng; hợp xướng vẫn còn vì nằm trong `cue-k5-swarm-low`.

### 2.3 Tiếng và chồng lớp

Trần canon §22: **32 tiếng (Low 16)**, mỗi âm ≤ 4 lần mỗi 100 ms. Chia (đề xuất, chỉnh bằng bài D):

| Kho | High | Low | Ghi chú |
|---|---|---|---|
| `typing` (phím, `key-word`) | 4 | 2 | kho riêng, combat không bao giờ cướp |
| `pronunciation` | 1 | 1 | kho riêng |
| `warnings` (báo đòn, Trận Lực < 30 %) | 3 | 2 | combat không cướp |
| nhạc, môi trường, trận pháp | 6 | 3 | danh sách khác quyết chia |
| `ui` (thẻ đợt, bảng, mua, Lĩnh ngộ) | 2 | 1 | combat không cướp |
| thú (`enemies`, `world`: trúng, tan khói, triều) | 6 | 3 | danh sách thú |
| `self` (bộ Kiếm) | 10 | 4 | bảng dưới |

Lớp P nướng trong cue nên không chiếm tiếng. Nhóm trong kho `self` (trần nhóm theo audio.md §5.4; trần kho vẫn là 10 hoặc 4):

| Nhóm | High | Low | Gồm |
|---|---|---|---|
| charge | 3 | 1 | bed, `kit-charge` hoặc `kit-appear` (kiếm K1, góc K4), swell |
| release | 4 | 1 | phát K0, K1, K3A, K3B, K4; K3A hết, K4 đóng |
| travel | 3 | 1 | `cue-sword-travel`, `cue-k1-launch` (cả kiếm 1), `kit-trail` của K5, `cue-k3b-land` |
| hit | 6 | 2 | trúng K0, K1, nhịp K4 |
| heavy | 2 | 1 | K2, K3A đỡ, K4 mở |
| loop | 2 | 1 | K3A và K4, mỗi loại 1 |
| big | 1 | 1 | phát và các loạt K5 |
| swarm | 3 | 1 | bed bầy K5 (Low chỉ `cue-k5-swarm-low`) |
| tail, tail-big | 2 + 2 | 1 | đuôi thường và `kit-residue`; đuôi K5. Low: `kit-residue` chỉ phát khi nhóm còn trống |

- **Thứ tự cướp:** trước hết cướp tiếng cũ nhất trong cùng nhóm, sau đó cướp tiếng ưu tiên thấp nhất (audio.md §5.4). Trong `self`, từ thấp lên cao:
  1. `kit-appear`, swell
  2. travel (gồm `cue-k1-launch`)
  3. tail thường và `kit-residue`
  4. nhịp K4
  5. trúng K0
  6. trúng K1
  7. loop
  8. release
  9. bed gồng
  10. heavy
  11. swarm
  12. big và tail-big: nhóm khác không cướp được; trong nhóm, tiếng mới cướp tiếng cũ nhất (đuôi cũ fade 80 ms)

**Chồng lớp theo số kiếm**

| Số kiếm | Chiêu | Cách làm |
|---|---|---|
| 1 | K0 | 1 phát, 1 bay, 1 trúng |
| 3 | K1 (băng) | 3 `kit-appear` lúc gõ. 1 phát cho cả băng (chỉ lóe phát). 3 tiếng rời kiếm 100 ms ở 0, +30, +60 tính từ base của băng, mỗi sự kiện `volley` một tiếng; hai lần rời cùng tick (kiếm Kiếm Tâm cùng kiếm 3) gộp một, nên không bao giờ chồng nhau trong một băng. 3 cú trúng cách nhau 0,5 s, nốt leo dần theo `part`. Băng thứ hai nối sau băng trước: base của nó là tick chạm kiếm 3 của băng trước |
| 3 | K3A (vòng) | 1 vòng lặp chứa cả 3 kiếm quay, không phải 3 tiếng |
| 4 | Kiếm Tâm | kiếm 4 chạm cùng tick kiếm 3: một lô, `cue-k1-hit-heart` |
| 6 | K4 | Lúc gõ: 5 `kit-appear` khi các góc sáng. Mở là 1 file flam 6 cú nướng sẵn: offset 0, 8, 16, 24, 32, 40 ms ±4 ms, mỗi cú lấy từ một take khác (lab cắm 6 kiếm cùng khung +12). Mỗi nhịp 1 tiếng |
| 150–500 | K5 | **Không có tiếng cho từng kiếm.** Gồm 2–3 bed bầy (trầm có hợp xướng, cao, rít), `kit-trail`, 1 cue cho mỗi loạt (đã chứa lớp mass "trăm lưỡi chạm đá") và đuôi. Tối đa 8 tiếng ở High (1 big, 3 swarm, 1 trail, 2 tail-big, 1 residue; các đuôi 2–3 s gối nhau nên đuôi mới cướp đuôi cũ nhất trong `tail-big`, mục 12), 4 ở Low (1 big, `cue-k5-swarm-low`, `kit-trail`, 1 đuôi) |
| nhiều nguồn trong 38 ms | K0, K1, K4 | Gom thành 1 cue; bậc cao nhất thắng; không có bản mass (§2.1) |

Đồng đội (M1): bus `allies`, ưu tiên 5, dưới `self` 6 dB. Lúc đó chia lại kho.

### 2.4 Ưu tiên và hạ tiếng

**Ưu tiên** theo canon §22 (số trong `catalog.ts`): phát âm từ của mình 1 → báo đòn và Trận Lực < 30 % 2 → phím 3 → chiêu của mình 4 → chiêu đồng đội và va chạm 5 → bầy và môi trường 6. Chiêu của mình không bao giờ cướp tiếng phím, giọng đọc hay báo đòn, và không bao giờ hạ giọng đọc hay báo đòn. Chỉ K5 (P0) được hạ phím, tối đa −2 dB (audio.md §5.4), trừ `key-word` cùng khung phát (§2.1).

**Hạ tiếng** (WebAudio không có sidechain: tự động hóa gain như hàm `duck()` ở audio.md §5.8)

| Nguồn kích | Đích | Mức | Thời gian |
|---|---|---|---|
| Giọng đọc từ. Canon §17: trong trận đọc từ < 40 độ thuộc **sau khi cast**, nên đúng lúc chiêu phát | nhạc | −6 dB (đề xuất; canon chưa ghi) | vào từ `pronouncer.request`; giữ tới `end`, tối đa 3 s; nhả 300–500 ms |
| | vang trả về, đuôi, vòng lặp, bed gồng, bed bầy (cả hợp xướng) | −6 dB | như trên |
| | phần khô của phát và trúng (cả K5) | tối đa −3 dB | như trên |
| | phím | theo hệ phím chung (mốc 9); spec này không đổi | — |
| K5: phát và mỗi loạt (P0) | combat thường: K0, K1, nhịp K4, trúng của thú, tan khói | 0,6 (−4,5 dB) | vào trong 8–12 ms, giữ 120–250 ms, về trong ~300 ms |
| | nhạc | −4 đến −6 dB | bắt đầu 83 ms trước cú chạm (tick −5) |
| | môi trường | −6 dB | như hàng combat |
| | phím (trừ `key-word`), UI | tối đa −2 dB | như hàng combat |
| | báo đòn, giọng đọc | không hạ | — |
| K2 trúng, K3A đỡ, K4 mở (T4) | trúng thường | −3 dB | 150 ms |
| Bed gồng | phím | không hạ phím; bed tự nằm dưới phím | — |

### 2.5 Không gian và bus

- **Một không gian:** hẻm đá vôi Thanh Thạch Ải (canon Q6: "đuôi vang hẻm núi").
  - IR tự làm theo audio.md §5.7 bước 4, thêm slapback vách xa `aecho=0.8:0.7:180|330:0.35|0.2` (lệnh ở §3.9). Ba độ dài: 2,5 s cho đuôi thường K0, K1 và đuôi nướng (cắt còn 1,2 s), 3,5 s cho T4, phát và loạt 1–2 của K5, 4 s cho loạt 3 (audio.md: "3–4 s for … big events"). Cú pháp đã chạy thử với `-f null` ngày 02/11; mức chưa đo, chưa nghe.
  - Lượt soát 3 chạy chuỗi bước 5 trên âm giả: IR 3,5 s cho đuôi K0 dài ~1,9 s, có 25 ms im lặng đầu (do `adelay`). Vì thế đuôi thường dùng IR 2,5 s cắt 1,2 s, và trễ trước 25 ms chuyển sang code (§2.1).
  - Thử thêm một IR CC0 "mountain ranges" hoặc "ravines" từ gói Tim_Verberne (đọc giấy phép từng trang, ghi vào THIRD_PARTY). Anh nghe rồi chọn một.
- **Send:** send → trễ trước 25 ms → lọc cao 180 Hz → ConvolverNode → lọc thấp 6,5 kHz → return 0,5. Return nhường giọng đọc.
  - Bậc Low không chạy convolver trực tiếp: nướng đuôi lúc nạp bằng `OfflineAudioContext`.
  - Đuôi đã nướng không đi vào send (send 0), để không vang hai lần. Điều này áp cả cho cue có đuôi nướng trong file (`cue-k3a-end`, `cue-k4-close`).
  - Prompt không phải đuôi không xin không gian ("echoing", "canyon", "spacious"): không gian chỉ đến từ IR và send (audio.md §5.6, "[space: tail prompts only]").
- **Bus `self`:** level → duck → glue (ngưỡng −18, knee 6, tỉ lệ 3, attack 25 ms, release 150 ms) → gain bỏ makeup tự động ≈ −7,2 dB (đo bằng `OfflineAudioContext`) → master.
  - Không dùng compressor nhanh. Bus `typing` và `ui` đi vòng qua compressor của combat.
  - Master có limiter an toàn (−3, knee 0, tỉ lệ 20, 1 ms, 80 ms) rồi trim, để bản chụp trận ≤ −1 dBTP.
  - Không chép cấu hình glue từ `games/dragon-hold/src/audio/{mixer,limiter}.ts` mà không đo lại (bẫy của audio.md §5.1).

## 3. File và prompt Firefly

### 3.1 Quy ước

- **Id `tt-sfx-<nhóm>-<tên>`:**
  - Nguyên liệu Firefly: nhóm `sword`, `sabre`, `spear`, `common`, `item`, `elem`, `kiem`, `magic`.
  - Cue dựng: nhóm `cue`. Cue nướng theo món thêm đuôi `-<món>`, ví dụ `tt-sfx-cue-k0-hit-clearwind`.
  - Stem kit của món: nhóm `kit` (trong spec viết tắt `kit-appear`, `kit-charge`, `kit-trail`, `kit-residue`).
  - Tiền tố `tt-sfx-` để không lẫn với id Tĩnh Tu `tt-*` trong `src/audio/catalog.ts`.
- **Nhận file:** `~/AudioLab/inbox/firefly/immortality-cultivation/<id>/`, giữ tên Firefly đặt. Dòng nguồn: "Adobe Firefly Generate Sound Effects, generated by the project owner (Adobe model)".
- **Lượt tạo:** mỗi lần tạo cho 4 bản.
  - Vòng 1: một lần tạo cho mỗi id. Id cần 3–5 biến thể (đầu, thân, bay, `magic-cast`, `magic-hit`, `magic-release`, `magic-impact`) tạo hai lần cùng prompt (8 bản).
  - Tối đa 3 vòng prompt mỗi id (audio.md §5.9); tạo lại cùng prompt không tính là vòng mới.
- **Prompt:** ≤ 12 từ, ngăn bằng dấu phẩy, một lớp, tiếng Anh, theo khuôn audio.md §5.6: `[nguồn + hành động], [cỡ], [chất], [không gian: chỉ lớp đuôi]`.
  - Lớp đầu (`*-draw`, `*-thrust`, `*-hit-head`, `sword-ring`, `kiem-rain-impact-head`) xin "dry, isolated". Lớp đuôi (`*-tail`, `magic-aura`) xin "no transient". Lớp residue là kết cấu dư âm, được có lách tách.
  - **Chất D56:** lớp P và S xin chất phép (magical, radiant, shimmering, celestial, glowing, enchanted, spirit, ethereal, epic). Lớp A xin chất điện ảnh (fantasy, enchanted, energy, cinematic). Nguyên liệu thật chỉ là danh từ nguồn (steel, jade, stone, water).
  - **Không dùng:**
    - từ cấm của audio.md §5.6;
    - từ cấm của Q6: puff, pop, balloon, thump, thud, whoomph; toy, cartoon, retro, 8-bit;
    - bell, chant, monk, temple, gong (canon §22: không chuông chùa, không tụng).
  - **Tránh thêm** (đặt cho game này):
    - anime, cute, twinkle, arcade, chiptune: với model âm thanh, các chữ này dễ kéo về tiếng hoạt hình mà Q6 cấm. Chất anime đến từ chữ epic, radiant, celestial, explosive;
    - sci-fi, laser, plasma, robot, beep: trôi sang khoa học viễn tưởng, lỗi tấm vũ khí đã mắc;
    - realistic, foley, field recording: trái D56.
- **Giọng mẫu:** lớp nào cần đúng đường bao thì anh ghi nhịp bằng giọng rồi dùng voice to sound effects của Firefly.
- **Cột "Cắt":** độ dài lớp sau khi cắt ở §5.7 bước 2, không phải độ dài file Firefly. Nguyên liệu không mang bậc: bậc đặt cho cả cue ở bước 8.
- **Đợt:** S1, S2, L như §1.3. Bước đổi món (Thunder Seal) ghi "Đổi".

### 3.2 Lớp A

| Id | Vai | Prompt | Cắt | Đợt |
|---|---|---|---|---|
| `tt-sfx-sword-draw` | đầu phát | `fantasy sword unsheathed, bright ringing steel shing, sharp attack, dry, isolated` | 15–40 ms | S1 |
| `tt-sfx-sword-swing` | thân phát | `powerful sword slash, energy-charged whoosh, fast, heavy, cinematic, dry` | 80–150 ms | S1 |
| `tt-sfx-sword-flyby` | bay | `enchanted flying sword whizzing past, sharp singing whoosh, fast, intense` | 100–400 ms | S1 |
| `tt-sfx-sword-hit-head` | đầu trúng | `spirit sword striking stone armor, sharp metallic crack, punchy, dry, isolated` | 15–40 ms | S1 |
| `tt-sfx-sword-hit-body` | thân trúng | `heavy sword energy slash impact, dense, punchy, saturated, cinematic, dry` | 80–150 ms | S1 |
| `tt-sfx-sword-ring` | nốt xác nhận trúng | `enchanted steel blade ringing, bright shimmering ping, sharp attack, dry, isolated` | 25–90 ms | S1 |
| `tt-sfx-sword-tail` | đuôi | `magical sword clash echoing across vast canyon, shimmering rolling echo, no transient` | 1–2 s | S1 |
| `tt-sfx-sabre-draw` | đầu phát | `heavy war sabre unsheathed, deep grinding steel, powerful, dry, isolated` | 20–50 ms | L |
| `tt-sfx-sabre-swing` | thân phát | `massive sabre crescent slash, deep energy whoosh, powerful, cinematic, dry` | 100–250 ms | L |
| `tt-sfx-sabre-hit-head` | đầu trúng | `sabre cleaving stone, violent metallic crack, very loud, dry, isolated` | 15–40 ms | L |
| `tt-sfx-sabre-hit-body` | thân trúng | `heavy sabre energy chop impact, massive, deep, punchy, saturated, cinematic` | 100–250 ms | L |
| `tt-sfx-sabre-tail` | đuôi | `mighty blade impact echoing through deep canyon, booming rolling echo, no transient` | 1–2 s | L |
| `tt-sfx-spear-thrust` | đầu phát | `spear thrust, piercing energy jab, sharp attack, punchy, dry, isolated` | 15–40 ms | L |
| `tt-sfx-spear-shaft` | thân phát, bay | `long spear shaft whipping, powerful shimmering swoosh, fast, dry` | 100–300 ms | L |
| `tt-sfx-spear-hit-head` | đầu trúng | `spear piercing stone armor, sharp metallic crack, punchy, dry, isolated` | 15–40 ms | L |
| `tt-sfx-spear-hit-body` | thân trúng | `heavy spear energy impact, deep punchy strike, dense, saturated, cinematic` | 80–200 ms | L |
| `tt-sfx-spear-tail` | đuôi | `spear strike echoing across mountain ravine, shimmering rolling echo, no transient` | 1–2 s | L |

Lớp đầu dưới 50 ms (`*-hit-head`, `sword-ring`, `*-draw`) là thứ AI làm kém. Nếu take nhòe đầu tiếng, lấy lớp CC0 thay (Kenney Impact Sounds; audio.md §5.9), ghi nguồn.

### 3.3 Lớp chung

| Id | Vai | Prompt | Cắt | Đợt |
|---|---|---|---|---|
| `tt-sfx-common-sub` | sub T4–T6, kiếm 3 của K1, bản Chớp | `huge sub bass impact, deep pressure wave, cinematic` | 120–220 ms (AUDIO_PIPELINE §4.3.3: sub trúng nặng ≤ 220 ms) | S1 |

Nếu take không đạt, dùng sine rơi của audio.md §5.7 bước 2 làm lớp sub, nướng offline vào file thật. Không tạo sub bằng oscillator trong game.

### 3.4 Lớp B (nháp theo bóng dáng mới; soát lại khi anh chốt tấm vũ khí)

| Id | Món | Prompt | Cắt | Đợt |
|---|---|---|---|---|
| `tt-sfx-item-clearwind` | Clear Wind | `magical jade ring chiming, radiant crystalline sparkle, sharp attack, bright` | 60–400 ms | S1 |
| `tt-sfx-item-wintervein` | Winter Vein | `frost-forged blade singing, glittering ice crystal chime, cold, sharp attack` | 60–400 ms | S2 |
| `tt-sfx-item-thunderseal` | Thunder Seal | `divine thunder sigil slamming down, crackling electric resonance, powerful, sharp attack` | 80–400 ms; giữ 3 bản khác cao độ | Đổi |
| `tt-sfx-item-verdantbranch` | Verdant Branch | `blooming jade lotus burst, shimmering crystalline petals, bright, sharp attack` | 100–500 ms | S2 |
| `tt-sfx-item-embercrest` | Ember Crest | `blazing sabre crest flaring, fierce sizzling ember hiss, sharp attack` | 100–400 ms | L |
| `tt-sfx-item-mountainverdict` | Mountain Verdict | `colossal sabre resonating, deep stone-heavy steel hum, massive` | 100–400 ms | L |
| `tt-sfx-item-tidalcrescent` | Tidal Crescent | `willow-leaf sabre slicing water, glistening liquid shimmer, powerful` | 100–400 ms | L |
| `tt-sfx-item-skythread` | Sky Thread | `radiant spearhead singing through wind, piercing shimmering whistle, fast, powerful` | 150–600 ms | L |
| `tt-sfx-item-resonantfang` | Resonant Fang | `halberd side blade flashing, long radiant crystalline ring, powerful, magical` | 0,8–1,2 s | L |
| `tt-sfx-item-stormpin` | Storm Pin | `twin-bladed halberd crackling, rising thunder energy surge, intense` | 80–400 ms | L |

### 3.5 Lớp C

| Id | Prompt | Cắt | Đợt |
|---|---|---|---|
| `tt-sfx-elem-kim-ignite` | `radiant metal energy surging, bright glittering sparkle, sharp attack` | 100–400 ms | S1 |
| `tt-sfx-elem-kim-burst` | `explosive radiant metal shard burst, sharp shimmering impact, powerful` | 100–500 ms | S1 |
| `tt-sfx-elem-kim-residue` | `glittering silver energy sparks scattering, shimmering metallic dust, radiant, lingering` | 1–2,5 s | S1 |
| `tt-sfx-elem-loi-ignite` | `thunder spell igniting, violent crackling arc snap, sharp attack` | 100–400 ms | Đổi |
| `tt-sfx-elem-loi-burst` | `divine lightning strike, explosive electric crack, very loud, booming` | 100–600 ms | Đổi |
| `tt-sfx-elem-loi-residue` | `lingering divine thunder energy crackling, fierce glittering sparks, powerful` | 1–2,5 s | Đổi |
| `tt-sfx-elem-bang-ignite` | `ice magic crystallizing, sharp freezing crackle, glittering, crisp` | 100–400 ms | S2 |
| `tt-sfx-elem-bang-burst` | `enchanted ice shattering, massive glassy crystal crash, very loud` | 100–600 ms | S2 |
| `tt-sfx-elem-bang-residue` | `magical frost spreading, crackling ice, glittering shimmer` | 0,6–2,5 s | S2 |
| `tt-sfx-elem-moc-ignite` | `spirit vines surging, sharp cracking wood, rustling energy, powerful` | 100–400 ms | S2 |
| `tt-sfx-elem-moc-burst` | `giant spirit roots bursting through stone, heavy splintering wood, massive` | 150–600 ms | S2 |
| `tt-sfx-elem-moc-residue` | `glowing leaves swirling in strong wind, dense shimmering rustle` | 1–2,5 s | S2 |
| `tt-sfx-elem-hoa-ignite` | `spirit fire igniting, violent roaring flame burst, sharp attack` | 100–400 ms | L |
| `tt-sfx-elem-hoa-burst` | `blazing fireball explosion, roaring flames, very loud, cinematic` | 200–800 ms | L |
| `tt-sfx-elem-hoa-residue` | `glowing embers crackling, sparkling cinders drifting, fierce` | 1–2,5 s | L |
| `tt-sfx-elem-tho-ignite` | `earth magic rumbling, heavy rock grinding, deep, powerful` | 100–400 ms | L |
| `tt-sfx-elem-tho-burst` | `colossal earth spell slam, massive rock crunch, very loud, booming` | 200–800 ms | L |
| `tt-sfx-elem-tho-residue` | `enchanted gravel settling, rolling rocks, crumbling dust, rumbling` | 1–2,5 s | L |
| `tt-sfx-elem-thuy-ignite` | `magical water surging, powerful glistening splash, sharp attack` | 100–400 ms | L |
| `tt-sfx-elem-thuy-burst` | `massive spirit wave crashing, heavy shimmering splash, powerful, booming` | 200–800 ms | L |
| `tt-sfx-elem-thuy-residue` | `enchanted water swirling over stone, glistening shimmer, powerful, lingering` | 1–2,5 s | L |
| `tt-sfx-elem-phong-ignite` | `spirit wind gust, fast howling shimmering whoosh, powerful` | 100–400 ms | L |
| `tt-sfx-elem-phong-burst` | `violent cyclone blast, roaring magical gust, explosive` | 200–700 ms | L |
| `tt-sfx-elem-phong-residue` | `spirit wind howling, swirling glittering shimmer, powerful, lingering` | 1–2,5 s | L |

### 3.6 Lớp S của bộ Kiếm

| Id | Chiêu, vai | Prompt | Giọng mẫu | Cắt | Đợt |
|---|---|---|---|---|---|
| `tt-sfx-kiem-charge-bed` | gồng, nền (vòng lặp đều; code làm phần dâng) | `deep magical energy gathering, shimmering crystalline swirl, powerful, sustained` | — | vòng 2–4 s | S1 |
| `tt-sfx-kiem-charge-air` | gồng, lớp trên của K5 (vòng lặp đều) | `airy celestial shimmer, swirling sword energy, bright, intense, sustained` | — | vòng 2–4 s | S1 |
| `tt-sfx-kiem-line-release` | K2 phát | `colossal radiant sword slash launching, tearing magical whoosh, very loud` | "mmmm-SHIIING" | 250–400 ms | S1 |
| `tt-sfx-kiem-line-slice` | K2 trúng | `giant radiant sword slash splitting rock, explosive tearing crack, powerful` | — | 200–400 ms | S1 |
| `tt-sfx-kiem-ward-up` | K3A phát | `radiant sword barrier forming, glowing blades whirling, shimmering, powerful` | — | 300–500 ms | S2 |
| `tt-sfx-kiem-ward-loop` | K3A giữ | `glowing swords orbiting fast, steady shimmering whoosh, magical, sustained` | — | vòng 2–4 s | S2 |
| `tt-sfx-kiem-ward-block` | K3A đỡ | `magical barrier deflecting blow, massive crystalline clang, booming, sharp attack` | "KLANG" | 250–450 ms | S2 |
| `tt-sfx-kiem-ward-end` | K3A hết | `sword barrier dissolving, descending shimmering whoosh, sparkling, powerful` | — | 300–450 ms | S2 |
| `tt-sfx-kiem-dash` | K3B phát | `flash-step dash, streaking energy burst, powerful shimmering whoosh, dry` | — | 250–400 ms | S2 |
| `tt-sfx-kiem-dash-land` | K3B đến | `magical dash landing, sparkling energy burst on stone, punchy, dry` | — | 120–200 ms | S2 |
| `tt-sfx-kiem-array-launch` | K4 phát | `glowing swords shooting skyward, rising shimmering whoosh, fast, intense` | — | 300–500 ms | S2 |
| `tt-sfx-kiem-array-stake` | K4 mở (một cú; 6 cú dựng offline) | `glowing sword plunging into stone, heavy energy impact, punchy, dry` | "tsss-TAK" | 80–200 ms | S2 |
| `tt-sfx-kiem-array-loop` | K4 giữ | `glowing sword formation spinning, deep shimmering magical energy, powerful, sustained` | — | vòng 2–4 s | S2 |
| `tt-sfx-kiem-array-beat` | K4 nhịp | `sword formation energy pulse, sharp shimmering slash, punchy, dry` | — | 150–250 ms | S2 |
| `tt-sfx-kiem-array-close` | K4 đóng | `glowing swords tearing free from stone, shimmering magical whoosh, powerful` | — | 400–700 ms | S2 |
| `tt-sfx-kiem-rain-release` | K5 phát | `celestial energy pillar erupting, massive radiant blast, very loud, cinematic` | "hmmmm-VOOOM" | 0,4–0,5 s | S1 |
| `tt-sfx-kiem-rain-swarm-low` | K5 bay, bed trầm | `thousands of glowing swords flying, roaring magical whoosh, massive` | — | 2,4 s | S1 |
| `tt-sfx-kiem-rain-swarm-high` | K5 bay, bed cao | `hundreds of shining blades streaking overhead, glittering magical shimmer, intense` | — | 2,4 s | S1 |
| `tt-sfx-kiem-rain-swarm-whistle` | K5 bay, rít | `enchanted swords singing overhead, piercing shimmering whoosh, fast, cinematic` | — | 2,4 s | S1 |
| `tt-sfx-kiem-rain-impact-head` | K5 loạt, đầu | `celestial blade storm striking ground, explosive crack, very loud, dry, isolated` | "pshh-KRAK" | 20–50 ms | S1 |
| `tt-sfx-kiem-rain-impact-body` | K5 loạt, thân | `huge magical sword impact, deep boom, powerful, cinematic, debris` | — | 250–500 ms | S1 |
| `tt-sfx-kiem-rain-mass` | K5 loạt, trăm lưỡi | `hundreds of glowing blades slamming into stone, dense shimmering impacts, violent` | — | 0,3–1 s | S1 |
| `tt-sfx-kiem-rain-debris` | K5 loạt 3, đá vụn | `rock debris raining down, heavy rubble, glittering dust, crumbling` | — | 0,5–1,5 s | S1 |
| `tt-sfx-kiem-rain-tail` | K5 đuôi (bản Firefly, so với đuôi IR) | `gigantic magical impact echoing across vast canyon, shimmering rolling echo, no transient` | — | 2–3 s | S1 |

**Tổng: 85 prompt** (76 của lượt 1 cộng 9 lớp P ở §3.10).

| Đợt | Gồm | Số prompt |
|---|---|---|
| S1 | 7 A kiếm, 1 chung, 1 B, 3 C Kim, 13 S, 9 P | 34 |
| Đổi | 1 B, 3 C Lôi | 4 |
| S2 | 11 S, 2 B, 6 C | 19 |
| L | 10 A đao và thương, 6 B, 12 C | 28 |

### 3.7 Kit của mỗi món (4 stem runtime)

| Stem | Dựng từ | Dài | Mức (LUFS-M max) | Dùng ở |
|---|---|---|---|---|
| `tt-sfx-kit-<món>-appear` (`kit-appear`) | B cắt 120 ms, lọc cao 4 kHz, cộng hạt lấp lánh của `magic-trail` dưới 4 LU | 120 ms | −30 | K1 gồng: mỗi kiếm hiện (15, 45, 75 %); K4 gồng: mỗi góc trận sáng (1/6 … 5/6) |
| `tt-sfx-kit-<món>-charge` (`kit-charge`) | residue C lọc cao 3 kHz, cộng B lặp | vòng 2–4 s | −30 khi đầy (dưới bed 6 LU) | gồng K2–K5 |
| `tt-sfx-kit-<món>-trail` (`kit-trail`) | phần kéo dài của ignite C, cộng B (còi Sky Thread; 3 bản điện cố định theo thứ tự kiếm của Thunder Seal, chọn theo `part`) | 250–600 ms | −24 | nướng vào `cue-sword-travel` và `cue-k1-launch`; lúc chạy chỉ ở K5, trên bed bầy |
| `tt-sfx-kit-<món>-residue` (`kit-residue`) | residue C, lọc 150 Hz–7 kHz | 1–2,5 s | −24 | dư âm K2, K4, K5 (K5 chỉ ở High); Winter Vein thêm 0,6–1 s sau mỗi cú trúng |

### 3.8 Cue dựng (offset tính bằng ms từ đầu lớp đầu)

`B` là lớp món, `C·x` là lớp hệ phần x; tên nguyên liệu bỏ tiền tố `tt-sfx-`. Cột "Bước" là bước ở audio.md §5.7; "2b" là bước đặt mức từng lớp ở §3.9. Mọi cue có `B` hoặc `C` được nướng cho từng món.

**Lớp P dẫn (D56).** Take Firefly có mức tùy ý, nên trọng số `amix` không phải độ to. Bước 2b đặt mức từng lớp trước khi trộn (LUFS-M max, điểm khởi đầu để anh nghe chỉnh): P −20 (lớp S của chiêu cũng −20 khi cue có S), B −25, thân A −27, đầu, tiếng reo và C −29; sub và lớp mass theo tai. Thép, ngọc, đá nằm dưới làm thân. Cổng "P dẫn" ở §4.1 đo việc này.

| Cue | Nguyên liệu và offset | Bước | Bậc | Biến thể |
|---|---|---|---|---|
| `cue-k0-release` | `magic-cast` 0 (cắt 150 ms), `sword-draw` 0, `sword-swing` +3, B +5, C·ignite +5 | 2, 2b, 3, 8 | T2 −19 | 3–5 (đổi take `magic-cast`, đầu và thân trước khi trộn; không chạy bước 9 trên cả cue) |
| `cue-k0-hit` | `magic-hit` 0 (cắt 200 ms, không sub), `sword-hit-head` 0, `sword-ring` 0, `sword-hit-body` +3, B (nốt, cắt 220 ms) +5, C·burst (cắt 150 ms) +5 | 2, 2b, 3, 8 | T3 −19 | 3 (đổi take đầu, thân và `magic-hit`; nốt B giữ nguyên) |
| `cue-sword-travel` | `magic-trail` 0, `sword-flyby` 0, `kit-trail` 0 (chỉ K0, một kiếm, một bản) | 2, 2b, 3, 8 | −22 (dưới phát 3 LU) | 3 (đổi take) |
| `cue-k1-launch` | `magic-cast` 0 (cắt 40 ms: lóe ở vai), 100 ms cuối của `sword-flyby` 0, `kit-trail` (cắt 100 ms) 0. Thunder Seal: 3 bản theo `part` 0, 1, 2 (`kit-trail` bản 1, 2, 3); món khác một bản cho cả 3 kiếm | 2, 2b, 3, 8 | −20 (dưới phát 3 LU) | 2 (Thunder Seal: 2 cho mỗi `part`) |
| `cue-sword-tail` | IR 2,5 s từ bản `cue-k0-hit` chỉ có lớp A và P, cộng `magic-aura`, cắt còn 1,2 s; hoặc take `sword-tail` lọc 200 Hz–6,5 kHz, hạ 3 dB ở 1–4 kHz, cộng `magic-aura` | 4, 5 (BELOW 8) | khô − 8 | 2 |
| `cue-k1-release` | như `cue-k0-release`, thêm `sword-swing` thứ hai +8; chỉ là lóe phát, không chứa tiếng bay | 2, 2b, 3, 8 | T2 −17 | 3–5 (đổi take, như `cue-k0-release`) |
| `cue-k1-hit-1`, `cue-k1-hit-2`, `cue-k1-hit-3` | như `cue-k0-hit` (lớp P là `magic-hit`); nốt B 0, +2, +4 bán cung (`asetrate` chỉ trên lớp B); hit-3 thêm `common-sub` +6. Bản Hoàn hảo: B sáng hơn. Bản Chớp: thêm `common-sub` +6 và nốt B quãng tám +5 | 2, 2b, 3, 8 | T3 −18/−17/−16 | mỗi nốt: 2 thân, 1 Hoàn hảo, 1 Chớp |
| `cue-k1-hit-heart` | bản Chớp của `cue-k1-hit-3`, thêm nốt B +7 bán cung ở +5 | 2, 2b, 3, 8 | T3 −16 | 1 |
| `cue-charge-bed` | `kiem-charge-bed`, cắt vòng (crossfade 50 ms của build Audio Lab) | 2 | −24 (code hạ theo tiến độ) | 1 |
| `cue-k5-charge-bed` | `kiem-charge-bed`, `kiem-charge-air` dưới 6 LU, cắt vòng | 2, 3 | −24 (code hạ theo tiến độ) | 1 |
| `cue-k2-swell` | `magic-surge`, cắt vòng (crossfade 50 ms); vòng sáng đều, code dâng theo tiến độ (§2.1) | 2 | −22 khi đầy (code hạ từ −30) | 1 |
| `cue-k5-swell` | `magic-surge` cộng `kiem-charge-air` dưới 6 LU, cắt vòng; code dâng theo tiến độ (§2.1) | 2, 3 | −22 khi đầy (code hạ từ −30) | 1 |
| `cue-k2-release` | `magic-release` 0, `kiem-line-release` 0, `sword-draw` 0, B +5, C·ignite +5, `common-sub` +6 | 2, 2b, 3, 8 | T4 −13 | 3 |
| `cue-k2-impact`, `cue-k2-impact-mass` | `magic-impact` 0, `kiem-line-slice` 0, `sword-hit-head` 0, `sword-hit-body` +3, B +5, C·burst +5, `common-sub` +6; bản mass thêm `kiem-rain-mass` cắt 300 ms ở +10 | 2, 2b, 3, 8 | T4 −12 | 3 + 1 |
| `cue-k2-impact-empty` | đường chém vào đá trống: `magic-impact` 0, `kiem-line-slice` 0, `common-sub` +6; không có B, C·burst, `sword-hit-head`, `sword-hit-body` | 2, 2b, 3, 8 | T4 −13 | 2 |
| `cue-k2-tail` | IR 3,5 s từ bản `cue-k2-impact` chỉ có lớp A, S, P; cộng `magic-aura` | 4, 5 (BELOW 8) | khô − 8 | 1 |
| `cue-k3a-up` | `magic-cast` 0, `kiem-ward-up` 0, B +5, C·ignite +5 | 2, 2b, 3, 8 | T3 −17 | 2 |
| `cue-k3a-loop` | `kiem-ward-loop`, cắt vòng | 2 | −22 | 1 |
| `cue-k3a-block` | `magic-impact` 0, `kiem-ward-block` 0, `sword-hit-head` 0, B +5, C·burst +5, `common-sub` +6 | 2, 2b, 3, 8 | T4 −13 | 3 |
| `cue-k3a-block-tail` | IR 3,5 s từ bản `cue-k3a-block` chỉ có lớp S và P; cộng `magic-aura` | 4, 5 (BELOW 8) | khô − 8 | 1 |
| `cue-k3a-end` | `kiem-ward-end`, `magic-aura` (cắt ≤ 0,8 s) dưới 6 LU; đuôi nướng bằng IR 2,5 s, trễ trước 25 ms nằm trong file sau phần khô; cả file ≤ 1,2 s | 2, 5, 6, 8 | T2 −19 | 1 |
| `cue-k3b-dash` | `magic-cast` 0 (cắt 200 ms), `kiem-dash` 0, `sword-swing` +3, B +5, C·ignite +5 | 2, 2b, 3, 8 | T3 −17 | 3 |
| `cue-k3b-land` | `kiem-dash-land` 0, `magic-trail` (cắt 120 ms) 0 | 2, 2b, 3, 8 | −22 | 3 |
| `cue-k4-release` | `magic-cast` 0, `kiem-array-launch` 0, B +5, C·ignite +5 | 2, 2b, 3, 8 | T3 −16 | 2 |
| `cue-k4-open` | `magic-impact` 0, 6 × `kiem-array-stake` (0/8/16/24/32/40 ±4, mỗi cú một take), `common-sub` +6, B và C·burst +5 | 2, 2b, 3, 8 | T4 −12 | 3 |
| `cue-k4-tail` | IR 3,5 s từ bản `cue-k4-open` chỉ có lớp S và P; cộng `magic-aura` | 4, 5 (BELOW 8) | khô − 8 | 1 |
| `cue-k4-loop` | `kiem-array-loop`, cắt vòng | 2 | −22 | 1 |
| `cue-k4-beat`, `cue-k4-beat-empty` | `kiem-array-beat` 0, `sword-ring` 0, `magic-hit` (cắt 120 ms) 0, B (nốt) +5, C·burst (cắt 120 ms) +5; bản empty bỏ B và C·burst | 2, 2b, 3, 8 | T3 −17 / nền −23 | 5 + 3 |
| `cue-k4-close` | `kiem-array-close`, `magic-aura` (cắt ≤ 1 s) dưới 6 LU; đuôi nướng bằng IR 2,5 s, trễ trước 25 ms nằm trong file sau phần khô; cả file ≤ 1,5 s | 2, 5, 6, 8 | T2 −18 | 1 |
| `cue-k5-release` | `magic-release` 0, `kiem-rain-release` 0, `sword-draw` ×3 (0/25/50), B +5, C·ignite +5, `common-sub` +6; đẩy 6 dB vào tanh rồi đặt bậc; cả cue ≤ 0,5 s để xong trước loạt 1 | 2, 2b, 3, 8 (cắt mềm) | T5 −11 | 2 |
| `cue-k5-swarm-low`, `cue-k5-swarm-high`, `cue-k5-swarm-whistle` | `kiem-rain-swarm-low` cộng `magic-choir` (hạ 3 dB ở 1–4 kHz); `kiem-rain-swarm-high` cộng `magic-trail` kéo dài; `kiem-rain-swarm-whistle`. Đường bao phồng ở 0,5 / 1,25 / 2,0 s (`volume` theo thời gian) | 2, 3 | tổng −16 | 1 mỗi lớp |
| `cue-k5-volley-1`, `cue-k5-volley-2`, `cue-k5-volley-3` | `magic-impact` 0, `kiem-rain-impact-head` 0, `kiem-rain-impact-body` +3, `common-sub` +6, `kiem-rain-mass` +10, B +5 (0/+1/+2 bán cung), C·burst +5; loạt 3 thêm `magic-sub` (cắt ≤ 300 ms) +6 và `kiem-rain-debris` +40 | 2, 2b, 3, 8 (cắt mềm) | T5 −10 / T5 −9 / T6 −8 | 1 mỗi loạt: cố định để học |
| `cue-k5-tail-0`, `cue-k5-tail-1`, `cue-k5-tail-2`, `cue-k5-tail-3` | IR 3,5 s (loạt 3: 4 s) từ bản phát hoặc loạt chỉ có lớp S và P, **hoặc** take `kiem-rain-tail` lọc cao 200 Hz; cộng `magic-aura`; thử cả hai | 4, 5 (BELOW 6) | khô − 6 | 1 mỗi cái |

- **Mức của file.** Cue có stem chồng lúc chạy (file `.tail` theo sau, hoặc `kit-residue` cùng lúc) là trúng K0, `cue-k1-hit-3`, `cue-k1-hit-heart`, trúng K2 (cả bản trống), K3A đỡ, K4 mở, K4 đóng, phát và loạt K5. Phần khô của chúng đặt thấp hơn bậc 1 LU, vì tổng mới là mức người chơi nghe; mọi số sau khi trừ vẫn nằm trong khoảng bậc. Cue khác (phát K0–K4, `cue-k1-launch`, `cue-sword-travel`, trúng kiếm 1 và 2 của K1, nhịp K4, `cue-k3a-end`, lớp nền) đặt đúng bậc, để file nói đúng mức của nó. Cổng Bậc (§4.1) đo trên tổng dựng offline với cùng offset như runtime (harness, AUDIO_PIPELINE §6.1). Lệch thì sửa file khô, không sửa gain bus.
- **Mỗi cue một công thức** `art-src/audio/recipes/<cue>.json`, nhận món làm tham số. Một lệnh dựng đủ cue cho mọi món.

### 3.9 Chuỗi ffmpeg (audio.md §5.7; chạy trong bash; định nghĩa `mmax`, `tp`, `crest` lấy từ bước 1)

Ví dụ `tt-sfx-cue-k0-hit-clearwind` (phần khô, dài ~0,225 s):

```bash
# Build the Clear Wind K0 hit from Firefly takes (audio.md §5.7 steps 2, 3, 8). Mono dry cue; the P layer leads.
FF="ffmpeg -hide_banner -loglevel error -y"
# Step 2: prepare each layer for its job; lengths follow the "Cắt" columns of §3.
$FF -i magic-hit.wav -af "aresample=48000,highpass=f=120,afade=t=out:st=0.14:d=0.06,atrim=0:0.2" -ac 1 L_magic.wav
$FF -i sword-hit-head.wav -af "aresample=48000,highpass=f=1800,afade=t=out:st=0.025:d=0.015,atrim=0:0.04" -ac 1 L_head.wav
$FF -i sword-ring.wav -af "aresample=48000,highpass=f=1500,afade=t=out:st=0.06:d=0.03,atrim=0:0.09" -ac 1 L_ring.wav
$FF -i sword-hit-body.wav -af "aresample=48000,highpass=f=90,equalizer=f=300:t=q:w=1.2:g=-3,lowpass=f=9000,afade=t=out:st=0.1:d=0.05,atrim=0:0.15" -ac 1 L_body.wav
$FF -i item-clearwind.wav -af "aresample=48000,highpass=f=400,afade=t=out:st=0.14:d=0.08,atrim=0:0.22" -ac 1 L_item.wav
$FF -i elem-kim-burst.wav -af "aresample=48000,highpass=f=300,afade=t=out:st=0.1:d=0.05,atrim=0:0.15" -ac 1 L_elem.wav
# Step 2b: level each layer so the P layer leads (D56); targets are momentary max in LUFS, start values (§3.8).
lv() { awk -v m="$(mmax "$1")" -v t="$2" 'BEGIN{printf "%.2f",t-m}'; }
GM=$(lv L_magic.wav -20); GI=$(lv L_item.wav -25); GB=$(lv L_body.wav -27); GH=$(lv L_head.wav -29); GR=$(lv L_ring.wav -29); GE=$(lv L_elem.wav -29)
# Step 3: magic, head and ring at 0, body +3 ms, item and element +5 ms; levels come from step 2b, so the weights stay equal.
$FF -i L_magic.wav -i L_head.wav -i L_ring.wav -i L_body.wav -i L_item.wav -i L_elem.wav -filter_complex \
"[0]volume=${GM}dB[m];[1]volume=${GH}dB[h];[2]volume=${GR}dB[r];[3]volume=${GB}dB,adelay=3:all=1[b];[4]volume=${GI}dB,adelay=5:all=1[i];[5]volume=${GE}dB,adelay=5:all=1[e];\
[m][h][r][b][i][e]amix=inputs=6:weights=1 1 1 1 1 1:normalize=0:duration=longest,asplit=2[x][y];\
[y]acompressor=threshold=0.06:ratio=8:attack=25:release=90:makeup=3[c];[x][c]amix=inputs=2:weights=1 0.6:normalize=0,\
asoftclip=type=tanh:threshold=0.85,aresample=192000,alimiter=limit=0.84:attack=1:release=40:level=0,aresample=48000[o]" \
-map "[o]" k0_hit_dry.wav
# Step 8: tier T3 at -19 minus 1 LU, because the shared tail stem plays over it at run time (§3.8).
T=-20; G=$(awk -v m="$(mmax k0_hit_dry.wav)" -v t=$T 'BEGIN{printf "%.2f",t-m}')
$FF -i k0_hit_dry.wav -af "volume=${G}dB,aresample=192000,alimiter=limit=-1.3dB:attack=0.5:release=40:level=false,aresample=48000" -c:a pcm_s24le tt-sfx-cue-k0-hit-clearwind.wav
```

Đuôi chung `cue-sword-tail` và bản nghe (bước 4–6). `k0_hit_ap.wav` là bản K0 trúng dựng như trên nhưng chỉ có lớp A và P, vì đuôi dùng chung cho mọi món:

```bash
# Step 4: the canyon IRs with the far-wall slapback of §2.5. 2.5 s for routine and baked tails; 3.5 s for T4 and K5 (same line with d=3.5, -t 3.5); 4 s for the K5 last volley.
$FF -filter_complex "anoisesrc=d=2.5:c=pink:a=0.5:r=48000:seed=7[l];anoisesrc=d=2.5:c=pink:a=0.5:r=48000:seed=11[r];[l][r]join=inputs=2:channel_layout=stereo,afade=t=out:st=0:d=2.5:curve=exp,lowpass=f=7000,aecho=0.9:0.6:95|180|310:0.45|0.3|0.2,aecho=0.8:0.7:180|330:0.35|0.2" -t 2.5 ir_canyon_2s5.wav
$FF -filter_complex "anoisesrc=d=3.5:c=pink:a=0.5:r=48000:seed=7[l];anoisesrc=d=3.5:c=pink:a=0.5:r=48000:seed=11[r];[l][r]join=inputs=2:channel_layout=stereo,afade=t=out:st=0:d=3.5:curve=exp,lowpass=f=7000,aecho=0.9:0.6:95|180|310:0.45|0.3|0.2,aecho=0.8:0.7:180|330:0.35|0.2" -t 3.5 ir_canyon_3s5.wav
# Step 5: lift the mono dry to stereo first; with a mono input afir and amix return mono and the IR's width is lost (tested 02/11, ffmpeg 9.0.2).
# No pre-delay in the file: the code starts the .tail 25 ms after the dry (§2.1), so the stem passes the L1 lead-silence gate (<= 5 ms).
IRLEN=$(ffprobe -v error -show_entries format=duration -of csv=p=0 ir_canyon_2s5.wav); BELOW=8
$FF -i k0_hit_ap.wav -i ir_canyon_2s5.wav -filter_complex "[0]pan=stereo|c0=c0|c1=c0,apad=pad_dur=$IRLEN,highpass=f=200,lowpass=f=6500[s];[s][1]afir=irnorm=2,equalizer=f=2000:t=o:w=2:g=-3[w]" -map "[w]" -c:a pcm_f32le tail_raw.wav
# Add the aura sparkle (D56): high-passed at 150 Hz, kept up to 12 kHz, 3 dB down at 1-4 kHz for the spoken word.
$FF -i tail_raw.wav -i magic-aura.wav -filter_complex "[1]aresample=48000,highpass=f=150,lowpass=f=12000,equalizer=f=2000:t=o:w=2:g=-3,atrim=0:$IRLEN,afade=t=in:d=0.03[a];[0][a]amix=inputs=2:weights=1 0.5:normalize=0:duration=first[m]" -map "[m]" -c:a pcm_f32le tail_mix.wav
# Level 8 LU under the dry, then cut the routine tail to 1.2 s (§2.2: K0 0.8-1.2 s, K1 1-1.2 s).
G=$(awk -v d="$(mmax k0_hit_ap.wav)" -v w="$(mmax tail_mix.wav)" -v b=$BELOW 'BEGIN{printf "%.2f",(d-b)-w}')
$FF -i tail_mix.wav -af "volume=${G}dB,atrim=0:1.2,afade=t=out:st=0.9:d=0.3" -c:a pcm_s24le tt-sfx-cue-sword-tail.wav
# Step 6: listening copy, dry plus tail; the dry is lifted to stereo the same way and the tail starts 25 ms late, as at run time.
$FF -i tt-sfx-cue-k0-hit-clearwind.wav -i tt-sfx-cue-sword-tail.wav -filter_complex "[0]pan=stereo|c0=c0|c1=c0,apad=pad_dur=$IRLEN,asplit=2[d][k];[1]adelay=25|25[t];[t][k]sidechaincompress=threshold=0.05:ratio=4:attack=2:release=250[w];[d][w]amix=inputs=2:normalize=0:duration=longest,aresample=192000,alimiter=limit=0.84:level=0,aresample=48000,areverse,silenceremove=start_periods=1:start_threshold=-70dB,areverse[o]" -map "[o]" -c:a pcm_s24le k0_hit_full.wav
```

Khác ví dụ gốc của audio.md:
- lớp khô là mono (`-ac 1`, `adelay=…:all=1`), thêm lớp B, C và lớp P;
- bước 2b đặt mức từng lớp trước khi trộn, để lớp P dẫn (D56), thay cho trọng số `amix`;
- bước 5–6 nâng phần khô lên stereo trước `afir` và `amix`;
- bước 5 không có `adelay`: file đuôi bắt đầu ngay, code hẹn +25 ms; bản nghe ở bước 6 trễ đuôi 25 ms như lúc chạy;
- đuôi thường dùng IR 2,5 s và cắt còn 1,2 s; vang hạ 3 dB ở 1–4 kHz sau `afir` (§2.1);
- đuôi có thêm lớp hào quang giữ tới 12 kHz (§2.1).

Các bước khác chép nguyên:
- **Swell:** `magic-surge` cắt vòng ở bước 2; phần dâng do code làm (§2.1), không có pre-verb.
- **T5–T6:** cắt mềm rồi đặt bậc (bước 8).
- **Biến thể:** bước 9 (±1,5 bán cung offline) chỉ cho cue không có nốt B hay `kit-trail`. Cue có B đổi take trước khi trộn (§2.1).

Các bẫy cũ vẫn áp dụng:
- `alimiter` luôn có `level=0` hoặc `level=false`;
- `amix` luôn có `normalize=0`;
- không chạy `loudnorm` trên một cú;
- không bật `oversample` cho `asoftclip`;
- OGG mã bằng build của Audio Lab, vì ffmpeg Homebrew không có libvorbis.

### 3.10 Lớp P phép (D56)

Lớp này mang chất anime và thần thoại cho mọi chiêu. Nó nướng trong cue cùng offset với lớp đầu của pha, nằm trên nguyên liệu của lớp A, B, C (bước 2b, §3.8), và không chiếm tiếng chạy. Nguyên liệu không mang bậc; bậc đặt cho cả cue (§3.8). **P đổi theo bậc bằng take riêng, không chỉ bằng cắt:** phát và trúng có một take bậc thấp (`magic-cast`, `magic-hit`: đầu sáng, ngắn, không bùm trầm) và một take bậc cao (`magic-release`, `magic-impact`: nổ, có thân trầm). Cắt một cú bùm to cho ngắn không bỏ được thân trầm nằm ngay đầu tiếng.

| Id | Pha | Prompt | Cắt theo bậc | Dùng ở cue | Đợt |
|---|---|---|---|---|---|
| `tt-sfx-magic-surge` | gồng: vòng lặp của swell (code dâng) | `magical energy surge, shimmering crystal sparkles, epic spell charge, sustained` | vòng 2–4 s | `cue-k2-swell`, `cue-k5-swell` | S1 |
| `tt-sfx-magic-cast` | phát (R), bậc thấp T2–T3 | `swift sparkling spell burst, bright shimmering whoosh, sharp attack, dry` | 120–200 ms (lóe rời kiếm K1: 40 ms) | `cue-k0-release`, `cue-k1-release`, `cue-k1-launch`, `cue-k3a-up`, `cue-k3b-dash`, `cue-k4-release` | S1 |
| `tt-sfx-magic-release` | phát (R), bậc cao T4–T5 | `explosive magical burst, radiant shimmering whoosh, very loud, sharp attack, cinematic` | 250–500 ms | `cue-k2-release`, `cue-k5-release` | S1 |
| `tt-sfx-magic-trail` | bay (T) | `glittering magical energy streak, fast shimmering whoosh, bright, intense` | 100–400 ms; K5 kéo dài 2,4 s | `cue-sword-travel`, `cue-k3b-land`, `cue-k5-swarm-high`, `kit-appear` | S1 |
| `tt-sfx-magic-hit` | trúng (I), bậc thấp T2–T3 | `bright magical strike, crystalline energy burst, sparkling, sharp attack, punchy, dry` | 120–200 ms | `cue-k0-hit`, `cue-k1-hit-1`, `cue-k1-hit-2`, `cue-k1-hit-3`, `cue-k1-hit-heart`, `cue-k4-beat`, `cue-k4-beat-empty` | S1 |
| `tt-sfx-magic-impact` | trúng (I), bậc cao T4–T6 | `huge magical impact, radiant energy boom, sparkling burst, punchy, dry` | 300–800 ms | `cue-k2-impact`, `cue-k2-impact-empty`, `cue-k3a-block`, `cue-k4-open`, các loạt K5 | S1 |
| `tt-sfx-magic-aura` | dư âm (F) | `glowing magical aura shimmer, sparkling crystalline tail, ethereal, wide, no transient` | đuôi: 1–3 s; trong `cue-k3a-end` ≤ 0,8 s, `cue-k4-close` ≤ 1 s | mọi đuôi, `cue-k3a-end`, `cue-k4-close` | S1 |
| `tt-sfx-magic-choir` | bay của K5 | `ethereal wordless female choir swell, epic magical rise, radiant, cinematic` | 2,4 s | `cue-k5-swarm-low` | S1 |
| `tt-sfx-magic-sub` | loạt 3 của K5 | `massive magical shockwave, deep cinematic sub boom, rumbling` | ≤ 300 ms (AUDIO_PIPELINE §4.3.3: sub của nổ ≤ 300 ms); phần rền dài để cho đuôi và `kiem-rain-impact-body` | `cue-k5-volley-3` | S1 |

- **Hợp xướng:** loại take nào nghe ra lời, tụng hoặc giọng tăng nhân (canon §22). Vòng 2 nếu vòng 1 trượt: `radiant synth swell, epic magical rise, shimmering, cinematic`.
- **Nghe thử:** lát cắt Clear Wind (§4.3) có lớp P ngay từ đầu. Bản demo cho anh nghe có hai bản cạnh nhau, "chỉ nguyên liệu" và "có lớp P", để anh thấy khác biệt.

## 4. Nghiệm thu

### 4.1 Cổng máy (mỗi file và mỗi cue dựng đủ)

| Cổng | Ngưỡng | Nguồn |
|---|---|---|
| L1 vệ sinh (chặn) | Không clip, không đỉnh phẳng. Im lặng đầu ≤ 5 ms. Thời gian lên ≤ 10 ms cho phát và trúng. DC < 0,1 %. ≤ −1 dBTP. Độ dài lệch ≤ 20 %. Đuôi xuống −60 dB. Vòng lặp: bước nhảy < −40 dBFS, RMS lệch < 1 dB, trọng tâm phổ lệch < 10 %. 48 kHz. Mono, trừ các file stereo của §2.1 (đuôi `.tail`, bed, vòng lặp, cue K5; ngoại lệ chờ ghi vào AUDIO_PIPELINE, việc mở 15). Stem `.tail` bắt đầu ngay (trễ trước 25 ms do code hẹn), nên cũng qua luật im lặng đầu | AUDIO_PIPELINE §4.3.1 |
| L1b (gắn cờ) | Tiếng vọng trước đầu tiếng; rít cao tần; xoáy pha ("kim loại giả", cần soi kỹ ở tiếng ngọc, thép reo, Resonant Fang); rung cao độ ở đuôi > 20 cent. **Lớp P và lớp lấp lánh** (shimmer, sparkle, aura) cố ý có xoáy và hạt cao tần: so với bộ tham chiếu của chính lớp P, không so với thép; cờ chỉ để tai soi | §4.3.2 |
| Bậc | LUFS-M max đúng bậc ở §2.2, đo trên tổng dựng offline (cue khô cộng stem chồng lúc chạy, §3.8); ≤ −1 dBTP | audio.md §5.4, §5.10 |
| P dẫn | Cue đủ cao hơn bản "chỉ nguyên liệu" (bỏ lớp P và S, cùng chuỗi) ≥ 3 LU momentary max, tức lớp phép mang ít nhất nửa năng lượng | canon D56; §3.8 bước 2b |
| Crest | Lớp đầu ≥ 12 dB trước khi đặt bậc; T5–T6 ≥ 10 dB sau cắt mềm | §5.10 |
| Trầm | T4–T6 (K2, K3A đỡ, K4 mở, K5) có ≥ 25 % năng lượng dưới 150 Hz, đo trên cue đủ. Lớp P sáng dễ kéo tỉ lệ này xuống: sửa bằng sub, không cắt lớp P | §5.10 |
| Đuôi | Bản nghe T4–T6 còn năng lượng ở +500 ms, không thấp hơn đỉnh quá 30 dB. Stem đuôi lọc cao ≥ 150 Hz | §5.10 |
| L2–L5 (xếp hạng) | Xếp trong nhóm. Họ bẩn: audiobox trọng số 0. Danh sách nghe gồm bản đầu bảng, bản khác nhất, và ở ~30 % id thêm một bản dò | §4.4–4.6 |
| Đổi món | Khoảng cách âm học giữa hai món > độ trải biến thể của cùng món | §1.6; AUDIO_PIPELINE §5.2 |

### 4.2 Bài thử bản trộn (dựng bằng bộ trộn thật trong `OfflineAudioContext`)

| Bài | Kịch bản | Đạt |
|---|---|---|
| A bản trộn | 2–5 phút ở tốc gõ cao nhất (bot 80 WPM), đợt lớn, K2 có hạ thú, có K5 | −18 ±2 LUFS-I, ≤ −1 dBTP, LRA 10–18 LU. K5 cao hơn mức tích hợp 6–10 LU trong cửa sổ ngắn. Combat rõ trên phím |
| C giọng đọc | Từ < 40 độ thuộc được đọc ngay sau K2 và K5 (K5 có hợp xướng) | Ở ca xấu nhất, giọng cao hơn phần còn lại ≥ 10 dB ở 1–4 kHz; anh nghe xác nhận |
| D mật độ | 60 thú; K0, 2 băng K1, K4 và K5 cùng lúc | Không vượt 32/16 tiếng. Ép > 3 dB dưới 5 % thời gian. Không clip. Mỗi dải do đúng nhóm chiếm |
| E mỏi tai | 10 phút, K0 và K1 dày | Không biến thể nào phát hai lần liền. Anh nghe 3 phút từ phút 8, không gắn nhãn "nhàm khi lặp". Sửa bằng đỉnh ngắn và phân tầng, không làm nhỏ |
| G độ trễ | Phím cuối (Cast resolve ngay) hoặc `cast resolved` (Cast bị giữ, §2.1) → tiếng phát | ≤ 50 ms |
| H dừng hình | Số dừng hình đọc từ `IC_FEEDBACK_PROFILE` của bản build, không lấy số lab (lab hiện: K2 30 ms, K3A đỡ 30 ms, K4 mở 30 ms, K5 loạt 3 70 ms; build hiện cho K2 0 ms, việc mở 17) | Âm đúng khung, không khựng |

### 4.3 Thứ tự: lát cắt và demo trước, hàng loạt sau

| Bước | Làm | Cổng để sang bước sau |
|---|---|---|
| 0 | Audio Lab nhận game `immortality-cultivation`: lệnh `firefly ingest` hiện chỉ biết 3 game, cần thêm thẻ `specs/immortality-cultivation/<id>.yaml`. Danh sách Firefly của game vào `docs/games/audio/firefly/immortality-cultivation.json` (theo `schema.json`) và `.md`, như audio.md §2 đòi; lô 1 trỏ tới đó (việc mở 16). Làm IR hẻm núi | `firefly status` liệt kê đủ id S1 |
| 1a · lô 1 | Clear Wind với họ kiếm: K0 và K1 đủ 5 pha, có lớp P (15 prompt, [`WEAPON_AUDIO_FIREFLY_BATCH1.md`](WEAPON_AUDIO_FIREFLY_BATCH1.md)) | Qua cổng §4.1. Anh nghe mù ≥ 8,5 về lực, độ nảy, không gian, độ hợp game và chất phép D56 trên Bảng Nghe ("Một mình", "Lặp 20 lần", "Trong trận"; A/B "chỉ nguyên liệu" và "có lớp P") |
| 1b · S1 còn lại | K2, K5 và không gian (19 prompt còn lại của S1, gồm `magic-release` và `magic-impact` bậc cao). Đúng nguyên tắc pilot của audio.md §5.9 (phát thường, phát nặng, trúng, sự kiện lớn, một không gian) | Như bước 1a |
| 2 · demo | Clip trận 20–30 s trong lab chiêu: sân thật, camera chơi, 60 thú, K0, K1, K2, K5 có tiếng. Tiếng chết lấy từ danh sách thú (phụ thuộc) | Anh xem và nghe. Bài A, C, D, H đạt trên bản dựng offline |
| 3 · đổi món | Thunder Seal (Lôi, khác Clear Wind nhất): 4 prompt, bộ cue nướng và kit; cùng clip | Anh nghe mù đoán đúng món; cổng "Đổi món" ở §4.1 |
| 4 · S2 | K3A, K3B, K4 cho Clear Wind; rồi Winter Vein và Verdant Branch | Như bước 1a |
| 5 · hàng loạt | Đao và thương khi có bộ Đ, T | Như bước 1a, sau khi anh chốt hình món |
| Cuối | Gắn vào game | Qua cổng §4.1 (bộ phê bình Audio Lab) và anh nghe mù ≥ 8,5 về lực, độ nảy, không gian, độ hợp game và chất D56, trong bản build trên host chơi, đúng cài đặt người chơi, không cờ URL |

- **Luật dừng:** mỗi id tối đa 3 vòng prompt. Sau 3 vòng mà dưới 3 take qua cổng, hoặc anh chê hai lần liền, thì đổi nguồn theo thứ tự:
  1. lớp CC0;
  2. tự xử lý (hạ cao độ, bão hòa, sub tổng hợp bên trong file thật);
  3. giọng mẫu hoặc tự thu;
  4. danh sách "thu hoặc mua sau".
- **Hồ sơ:**
  - mỗi file một dòng `SOURCES.json` và `licences.jsonl`;
  - changelog của game;
  - ảnh và clip chụp nằm dưới `games/immortality-cultivation/tmp/`, chấm xong thì xóa khung thô bằng `tools/capture-prune/prune.mjs`.

## 5. Tự soát với audio.md §5 và canon

| Luật | Nguồn | Spec này |
|---|---|---|
| Không dùng luật phím cho combat | audio.md §5.1 | Luật phím chỉ cho `key-*` và `key-word` (Luật nền). Đuôi combat chỉ hạ 2–4 dB ở 1–4 kHz và nhường giọng, không bị cắt. Dòng "Luật giọng đọc" của canon §22 viết chung cho mọi âm: audio.md §5 thắng cho combat; xem việc mở 3 |
| Phong cách | canon D56; audio.md §5 "cinematic and magical" | Mọi cue có lớp P; thép, ngọc, đá, nước chỉ là nguyên liệu. Chất phép theo pha và bậc, không dồn đủ năm chất vào đòn thường |
| Biến thể | §5.2, §5.7 bước 9 | 3–5 bản cho cue có đầu và thân; cue có nốt B hoặc `kit-trail` đổi take trước khi trộn, không chạy bước 9 trên cả cue. Lúc chạy ±20 cent cho cue có B hoặc `kit-trail` (Thunder Seal 0), ≤ ±10 cent cho nốt leo K1, ±60 cent cho cue không có B; không doppler bằng `playbackRate`. Bảng AUDIO_PIPELINE §5.3 (±150 cent cho trúng nhỏ) là bản cũ, không dùng cho combat |
| Offset lớp | §5.3 | P, đầu 0; thân +3; B và C +5; sub +6 ms; flam 6 kiếm (0–40 ms) và đá vụn (+40) có offset riêng ghi trong bảng |
| Bậc | §5.4 | Mọi đòn nằm trong khoảng của bậc mình. Lớp nền không phải đòn: bed gồng (≤ −24), `kit-appear` và `kit-charge` (−30), swell (−30 → −22, code dâng tới chữ cuối), vòng lặp K3A và K4 (−22), `cue-k3b-land` (−22), `cue-k4-beat-empty` (−23). Lực nằm ở đỉnh (đỡ, mở, nhịp có thú). Đây là phân tầng, không phải làm nhỏ đòn |
| Trần tiếng | §5.4; canon §22 | Canon thắng: 32 (Low 16), ≤ 4 lần mỗi 100 ms. Trần nhóm nằm trong khoảng của audio.md: heavy 2, big 1, hit 6, loop 1 mỗi loại, tail 2. Nhóm release là 4 (khoảng 4–6 của bắn nhanh); K0 và K1 bắn dưới 4 lần/s. Lớp P nướng, không thêm tiếng. Bus `ui` có kho riêng 2 (Low 1) |
| Hạ tiếng P0 | §5.4 | 0,6 trong 8–12 ms, giữ 120–250 ms, về ~300 ms; nhạc −4 đến −6, môi trường −6, phím ≤ −2 (trừ `key-word`). Chỉ K5 được hạ phím. Báo đòn, giọng đọc không hạ (canon xếp trên chiêu) |
| Giọng đọc | §5.4, AUDIO_PIPELINE §6.2 | Khô ≤ −3 dB; nhạc, đuôi, vang trả về, vòng lặp, bed (cả hợp xướng) −6 dB (đề xuất); bắt đầu từ `pronouncer.request` |
| Dải tần | §5.5 | Vang IR 200 Hz–6,5 kHz. Lớp hào quang giữ tới 12 kHz, hạ 3 dB ở 1–4 kHz (lệch có lý do, việc mở 9). Thân được ở 1–4 kHz trong 80–250 ms. Còi Sky Thread, tiếng ngân Resonant Fang và hợp xướng được xử như đuôi |
| Prompt | §5.6, Q6, canon §22 | 85 prompt đã đếm (≤ 12 từ) và dò từ cấm bằng script (§3.1). Mỗi prompt một lớp. Lớp đầu có "dry, isolated", lớp đuôi có "no transient". Không có bell, chant, gong, anime |
| Chuỗi | §5.7 | Có `level=0`, `normalize=0`; không `loudnorm` trên một cú; không `oversample`; OGG không mã bằng ffmpeg Homebrew. Cú pháp §3.9 đã chạy với nguồn sine `lavfi` và `-f null` |
| Mono và stereo | AUDIO_PIPELINE §4.3.1 so với audio.md §5.7 | Khô mono (đúng cổng định dạng L1, game tự pan). Đuôi, bed, vòng lặp và K5 stereo vì cần không gian: ngoại lệ với cổng L1 và bước "gộp về mono" của AUDIO_PIPELINE §5.1, chờ ghi vào pipeline (việc mở 15). Bước 5–6 nâng khô lên stereo trước |
| Vang | §5.8 | Có cả đuôi nướng và send chung. Send: phát 0,10, trúng 0,05, phát và trúng nặng 0,25, K5 0,40, bed bầy 0,20, đuôi và cue có đuôi nướng 0. Prompt không phải đuôi không xin không gian. Bậc Low nướng đuôi lúc nạp. Glue chậm, bỏ makeup tự động, không compressor nhanh |
| Nguồn | §5.9 | Firefly trước. CC0 cho lớp đầu dưới 50 ms. Luật dừng tính theo từng id lớp. Lát cắt trước bộ đầy đủ |
| Nghiệm thu | §5.10 | Có đủ ở §4.1–4.3; tai anh là cổng cuối, mốc 8,5 |
| Tick | canon §12.1; `src/content/data/school-kiem.ts`; lab `kiem.ts` | K0 +18; K1 +6/+36/+66 tính từ base của băng (tick Cast, hoặc tick chạm kiếm 3 của băng trước khi băng nối), mỗi kiếm rời 6 tick trước chạm (0/+30/+60); K2 +12; K4 mở +12 rồi nhịp mỗi 30 tick tới +282, đóng +312 (10 nhịp); K5 +30/+75/+120. Tick 60 Hz. Dừng hình theo lab: K2 30, K3A đỡ 30, K4 mở 30, K5 loạt 3 70 ms; bản build theo `IC_FEEDBACK_PROFILE` (việc mở 17) |
| Không âm tổng hợp | canon D26, §22, D44 | Sub tổng hợp chỉ nướng offline thành một lớp trong file thật. Không có oscillator trong game |

Lỗi đã sửa trong lượt soát 1:
- **Đuôi K5 nhóm 1 tiếng:** đuôi 2–3 s gối lên nhau khi các loạt cách 0,75 s, nên nhóm `tail-big` lên 2 và đuôi cũ nhất nhường.
- **Phát K5:** rút còn 0,4–0,5 s để xong trước loạt 1 (nhóm big 1 tiếng).
- **Mức residue:** trước đó lệch giữa các cue (−26 và −22), nay thống nhất −24 để file đúng mức của nó.
- **Prompt Resonant Fang:** bỏ chữ "bell".
- **Tiếng bay K0 và K1:** flyby cộng `kit-trail` từng là 2 tiếng mỗi kiếm, vượt nhóm travel (3) khi K0 bay cùng băng K1. Nay nướng thành `cue-sword-travel` theo món; `kit-trail` chỉ còn chồng lúc chạy ở K5.
- **Gồng K5:** bed, `charge-air`, `kit-charge` và swell là 4 tiếng, vượt nhóm charge (3). Nay `charge-air` trộn sẵn vào `cue-k5-charge-bed`.
- **Đầu loạt K5:** prompt `rain-impact-head` thiếu "dry"; đã thêm.

Lỗi đã sửa trong lượt soát 2 (02/11, sau D56):
- **Phong cách:** "mỗi cue có đủ năm chất" trái phân tầng (K0 phát 0,83 lần/s không thể có hợp xướng). Nay chất phép đi theo pha và bậc (bảng đầu file).
- **Lớp P có bậc riêng** (T3 ở gồng, T2 ở đuôi) trái luật bed dưới mức phím và luật đuôi khô − 8 LU. Nguyên liệu không mang bậc; bậc đặt cho cả cue.
- **`magic-surge` "theo chữ gõ"** trái luật không thêm tiếng mỗi chữ: nay chỉ là riser của swell.
- **Độ dài lớp P** (trúng 0,4–1,2 s) dài hơn cả cue trúng K0, K1: nay cắt theo bậc.
- **`magic-impact`, `magic-sub` xin "reverberant"** dù nướng vào phần khô: bỏ; vang nằm ở đuôi và send. **`magic-aura`** thiếu "no transient": đã thêm.
- **Swell K2, K5** là pre-verb "kết thúc đúng lúc phát", nhưng game không biết trước phím cuối: nay là riser 1–1,5 s, phím cuối cắt.
- **Bed gồng và `charge-air` xin "rising"** dù là vòng lặp liền mối (cổng L1: RMS lệch < 1 dB): bỏ "rising"; code làm phần dâng.
- **Bay K1:** cue 250–400 ms "kết thúc ở tick chạm" bắt đầu trước khi kiếm 2, 3 rời vai. Sim và lab cho kiếm rời 6 tick trước tick chạm, lóe ở +30, +60. Nay là `cue-k1-launch` 100 ms đúng khung lóe.
- **Kiếm K1 hiện** ở 15, 45, 75 % tiến độ (lab), không phải 1/3 và 2/3: ba lần `kit-appear`.
- **K4 mở:** flam 150 ms trong khi lab cắm 6 kiếm cùng khung +12: nay 0–40 ms.
- **Dừng hình K2** là 30 ms trong lab, không phải 35; thêm K3A đỡ 30 ms và K4 mở 30 ms.
- **Biến thể Hoàn hảo và Chớp** nằm ở `cue-k0-hit`, nhưng K0 tự động không có từ: chuyển sang ba cue trúng K1. Kiếm Tâm chạm cùng tick kiếm 3, nên thành một lô: `cue-k1-hit-heart`.
- **±60 cent lúc chạy** trên cue đã nướng nốt B trái luật nốt ±20 cent: nay tách theo loại cue.
- **Lớp mass "lô ≥ 3 thú"** cho K0, K1, K4 không có file: nay chỉ K2 và K5 có lớp mass.
- **K0 trúng:** lớp B cắt 0,4 s làm cue dài 0,4 s, trái bảng 120–200 ms. Nay B cắt 0,22 s, bảng 150–250 ms.
- **Bước 5–6 với khô mono:** `afir` và `amix` trả mono (đã thử 02/11), mất độ rộng của IR hai seed. Nay nâng khô lên stereo trước (§3.9).
- **`cue-k4-beat-empty` ghi "T3 −23"**, dưới khoảng T3 (−20 đến −16): nay ghi "nền −23", cùng loại với các lớp nền ở dòng Bậc.
- **`kit-residue` không thuộc nhóm tiếng nào:** nay vào nhóm tail; ở Low chỉ phát khi nhóm còn trống.
- **Hạt lấp lánh của D56** bị luật lọc thấp 6,5 kHz của đuôi cắt mất: lớp hào quang giữ tới 12 kHz (việc mở 9).
- **Tổng 76 prompt** không đếm lớp P: nay 83; S1 có 32.
- **Lớp B** viết lại theo bóng dáng mới (đốc vòng, hộ thủ hai thùy, hộ thủ chữ nhật bậc, hộ thủ sen, yanmaodao, niuweidao, liuyedao, qiang mũi lá, ji một và hai lưỡi bên).

Lỗi đã sửa trong lượt soát 3 (02/11, luật, sim và chất D56):
- **Băng K1 nối:** sim cho kiếm 1 của băng nối rời ở tick chạm kiếm 3 của băng trước, muộn tới 66 tick sau lóe R, nhưng tiếng bay của kiếm 1 nằm trong cue phát. Nay mỗi sự kiện `volley` (cả kiếm 1) phát `cue-k1-launch`; tick K1 tính từ base của băng.
- **Đuôi trượt cổng L1:** IR 3,5 s cho đuôi K0 ~1,9 s và 25 ms im lặng đầu. Nay đuôi thường dùng IR 2,5 s cắt 1,2 s; file đuôi bắt đầu ngay, code hẹn +25 ms.
- **`magic-sub` 0,6–1 s trong cue phát K5 0,4–0,5 s:** phá lần sửa "xong trước loạt 1". Nay phát K5 dùng `common-sub`, `magic-sub` cắt ≤ 300 ms chỉ ở loạt 3; `magic-aura` trong hai cue đuôi nướng cắt ngắn, độ dài hai cue tính cả đuôi.
- **Thunder Seal:** 3 nốt điện cần biết kiếm thứ mấy; `cue-sword-travel` (một kiếm) ghi nhầm "bản 1, 2, 3". Nay `cue-k1-launch` có bản theo `part`; sự kiện cần trường `part` và `extra` (việc mở 6).
- **Hạ tiếng phím:** câu luật nói không bao giờ hạ phím, bảng cho K5 hạ −2 dB. Nay chỉ K5 được hạ phím (audio.md §5.4), trừ `key-word`.
- **Luật −1 LU** đẩy `cue-k3a-end`, `cue-k4-close` ra ngoài khoảng T2. Nay −1 LU chỉ cho cue có stem chồng lúc chạy; K4 đóng lên T2 −18.
- **Biến thể đè nốt B:** bước 9 và ±60 cent, doppler ±3 % chạy trên cue có B hoặc `kit-trail`. Nay cue có B đổi take trước khi trộn, lúc chạy ±20 cent, không doppler bằng rate.
- **Lóe không tiếng:** K2 trúng trống và K5 loạt trúng 0 thú vẫn lóe. Nay K2 hẹn từ `skill-fx` `line` và có `cue-k2-impact-empty`; K5 theo `skill-fx` `ultimate`.
- **Cast bị giữ hoặc hụt** chưa có luật âm. Nay bed về −30 khi giữ, phát theo `cast resolved`, hụt phát `type.word-fizzle`; bài G đo đúng ca này.
- **Thiếu kho `ui`:** chia lại 32/16, `ui` 2 (Low 1).
- **Stereo trái cổng L1 mono:** ghi lại "Mono" vào L1, thêm việc mở 15.
- **Vang hai, ba lần:** hai cue đuôi nướng send 0,10, prompt không phải đuôi xin "echoing", "canyon", "spacious". Nay send 0, bỏ chữ không gian khỏi các prompt đó.
- **Swell 1–1,5 s cố định** không bảo đảm "trên mức phím chỉ trong chữ cuối". Nay swell là vòng lặp, code dâng theo tiến độ tới −22 khi còn 1 chữ.
- **Độ dài sub, lớp đầu và thân** lệch luật nguồn và cột Cắt; vang đuôi thiếu hạ 1–4 kHz: đã sửa ở §3.3, §3.9, §3.10.
- **Lớp P không đổi theo bậc:** `magic-impact` ("huge … boom") và `magic-release` ("explosive") bị chặt cho đòn T2–T3. Nay có take bậc thấp `magic-cast`, `magic-hit`; take bậc cao chuyển sang lô 1b. Tổng nay 85 prompt, S1 có 34.
- **Độ to không tăng theo bậc chiêu:** K0 to ngang K1, K4 nhỏ ngang K0, K5 xẹp sau phát. Nay K0 −19, K1 −17 (phát) và −18 → −16 (trúng), K4 phát −16, mở −12, nhịp −17, K5 −11 rồi −10, −9, −8.
- **P không chắc dẫn:** trọng số `amix` không phải độ to. Nay bước 2b đặt mức từng lớp và §4.1 có cổng "P dẫn".
- **Prompt dễ ra foley, sci-fi hoặc chuông:** Clear Wind, Thunder Seal, Verdant Branch, Storm Pin, Resonant Fang, Sky Thread; Kim ignite, burst, residue; Lôi residue; K2 "sword beam"; các bed "resonant hum"; bầy K5; ward-up, dash-land, array-close; hợp xướng; `magic-trail` "airy". Đã viết lại theo chất phép.
- **Đuôi bậc cao** ngắn gần bằng đuôi thường: K2, K4 nay 2–2,5 s, K3A đỡ 1,5–2 s. Bảng phong cách khớp số §2.2.
- **Thứ tự cướp** của big và tail-big tự mâu thuẫn: nay trong nhóm cướp tiếng cũ nhất, nhóm khác không cướp được.
- **Cổng cuối** thiếu mốc 8,5 mù; **góc K4 sáng** và **K3B đến** thiếu móc hoặc tiếng; **dừng hình** lấy số lab thay vì hồ sơ build: đã thêm vào §4.3, §2.2, §6.

## 6. Việc mở (cho điều phối)

1. **Hình món chưa chốt:** lớp B (§1.3, §3.4) theo bóng dáng mới điều phối giao ngày 02/11, nhưng `WEAPON_DESIGN.md` §6 vẫn ghi dấu hình cũ (vòng ngọc xuyên lưỡi, hộ thủ X, chữ Y, khe giọt nước). Soát lại prompt B khi anh duyệt tấm vũ khí. Lớp A, C, S, P không phụ thuộc hình, nên tạo trước được.
2. **Catalog:** `src/audio/catalog.ts` hiện có một id cho mỗi chiêu (`kiem-zone` là một file 5 s). Spec này tách theo pha và thêm kit theo món, nên cần sửa thẻ, hook và `ART_AUDIO_VFX_PLAN.md` §5.1. Việc này của làn âm, không làm ở phiếu này.
3. **Canon §22, "Luật giọng đọc":** nên ghi rõ phạm vi là `key-*` và âm sau từ, vì audio.md §5 thắng cho combat. Sửa canon là việc của anh.
4. **Mức hạ tiếng dưới giọng đọc:** canon Tu Tiên chưa ghi. Spec đề xuất nhạc, đuôi, vang −6 dB; anh chốt.
5. **Audio Lab:** `firefly ingest` chỉ nhận dragon-hold, typing-defense, typing-survival. Cần thêm `immortality-cultivation` và thẻ spec từng id.
6. **Lab chiêu chưa có đường âm.** Demo bước 2 cần bộ nạp file (kiểu `FileBank`), harness offline và các móc sự kiện của view: kiếm K1 hiện (15, 45, 75 %), mỗi kiếm K1 rời (cả kiếm 1, theo `skill-fx` `volley`, tính từ base của băng), góc K4 sáng lúc gõ, K4 cắm, nhịp K4, K3B đến, K2 chém (hẹn từ `skill-fx` `line`), loạt K5 (theo `skill-fx` `ultimate`), Cast bị giữ và `fizzled`. Đây là việc mã. Thêm:
   - sự kiện `hit` và `skill-fx` `volley` của ô 1 mang `part` (0–3) và cờ `extra` (kiếm Kiếm Tâm); chỉ thêm trường sự kiện, không đổi tick sim (`PendingStrike` đã có `part`);
   - lab và game chốt một số: K3B lướt 0,2 s trong lab, 0,3 s trong game (`local/dash.ts`, `DASH.unpushableMs`); lab nên đổi sang 0,3 s. Lab đóng K4 ở 5 s (+300), sim đóng ở +312; lab nên đóng ở +312.
7. **Phụ thuộc:** tiếng chết của lát cắt lấy từ danh sách thú; câu hỏi D55 và D23 (hệ của món có đổi hệ sát thương không) quyết C có tách khỏi B hay không.
8. **Chia 32/16 tiếng** ở §2.3 là đề xuất; bài D chỉnh lại.
9. **Lọc thấp đuôi 6–7 kHz** (audio.md §5.5) và hạt lấp lánh của D56: spec cho lớp hào quang giữ tới 12 kHz. Nếu anh nghe thấy đúng, nên ghi ngoại lệ này vào audio.md §5.5 (việc của điều phối).
10. **Bậc gõ cho K2–K5** (bản Hoàn hảo và Chớp) chưa làm ở lát cắt. Đề xuất: bản Chớp của cue phát thêm nốt B quãng tám.
11. **K4 mở:** nếu lab đổi sang cắm 6 kiếm lệch nhau (2 khung mỗi kiếm, đẹp hơn), đổi flam về 33 ms mỗi cú.
12. **`ART_AUDIO_VFX_PLAN.md` §5.1**, hàng Kiếm, còn ghi "thép lạnh, gió xé" (trước D56). Điều phối sửa khi soát kế hoạch.
13. **Nếu vòng 1 nghe quá "Hollywood thật"**, vòng 2 thêm cho riêng lớp P các chữ "fantasy spell", "celestial", "epic"; không dùng "anime" (§3.1, Q6).
14. **Canon §22 lệch spec:** dòng Nguồn chỉ ghi CC0 hoặc Audio Lab (Stable Audio 3), nên thêm Firefly Generate Sound Effects (model Adobe, audio.md §2); số id Kiếm ("Kiếm 8") đổi theo §3.8 (cue và kit theo món). Sửa canon là việc của anh.
15. **Ngoại lệ stereo:** AUDIO_PIPELINE §4.3.1 (hàng Định dạng) và §5.1 bước 4 (gộp về mono) cần ngoại lệ cho stem `.tail`, bed, vòng lặp và cue K5; thẻ `specs/immortality-cultivation/*.yaml` khai `playback.channels: stereo`. Việc của điều phối và làn âm.
16. **Danh sách Firefly theo game:** tạo `docs/games/audio/firefly/immortality-cultivation.json` (theo `schema.json`: prompt, inbox, phase, targetMs, takes mỗi hàng) và `.md`; lệnh `--list` của Audio Lab đọc dạng `{game, rows}` này. Lô 1 trỏ tới đó. Phiếu này chỉ sửa spec, không tạo file đó.
17. **Dừng hình lab và build lệch:** `IC_FEEDBACK_PROFILE` xếp K2 ở bậc phản hồi T2 với 0 ms, lab dùng 30 ms; K5 loạt 3 và K3A đỡ, K4 mở cũng cần một số chung. Lab và `feedback-profile.ts` phải thống nhất trước bài H.
