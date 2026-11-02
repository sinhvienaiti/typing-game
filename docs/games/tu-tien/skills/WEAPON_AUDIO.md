# Âm vũ khí và bộ chiêu Kiếm: spec (02/11/2026)

> **Trạng thái:** spec để tạo âm sau. Chưa tạo, chưa nghe file nào. Hình vũ khí chưa chốt (anh đang duyệt tờ ý tưởng), nên prompt lớp B (§3.4) là bản nháp, soát lại khi anh chốt từng món.
> **Nguồn thắng:** canon [D55, §12.1 (tick chạm), §22 (Q6, bus, ưu tiên, 32/16 tiếng)](../00-canon.md); [`WEAPON_DESIGN.md`](WEAPON_DESIGN.md) §5–6; [`SKILL_CATALOG.md`](SKILL_CATALOG.md) §1–2; skill `game-art-pipeline` [`references/audio.md`](../../../../.agents/skills/game-art-pipeline/references/audio.md) §5 (thắng mọi luật viết cho phím); [`AUDIO_PIPELINE.md`](../../AUDIO_PIPELINE.md) §4–7; [`ART_AUDIO_VFX_PLAN.md`](../ART_AUDIO_VFX_PLAN.md) §5–6.

**Phong cách (canon D56, anh 02/11, thắng mọi dòng bên dưới):** "chúng ta k làm ra kiểu âm thanh như thật… phải bùng nổ, đẹp, hào quang, thu hút của các phim anime hoặc các thần thoại, tiểu thuyết".
- Mọi cue của chiêu là **cảnh tượng phép thuật kiểu anime và donghua**, không phải foley như thật. Mỗi cue có đủ:
  - dồn năng lượng (energy surge, riser);
  - vút lấp lánh (shimmering whoosh);
  - chuông hoặc ngân pha lê;
  - hợp xướng hoặc synth dâng ở tuyệt kỹ;
  - bùm trầm, đuôi lấp lánh, va chạm vang lớn.
- Tiếng thép, ngọc, đá, nước ghi thật trong các bảng dưới chỉ là **nguyên liệu nằm dưới lớp phép**, không bao giờ là cả cue. Một cue nghe như tiếng kiếm thật, dù sạch, vẫn hỏng.
- Lớp mới **P phép** (§3.10) phát ở mọi pha có lóe và mang chất hào quang. Lớp B và C đổi theo món, lớp P đổi theo bậc chiêu. Bậc độ to và luật vang giữ nguyên.
- Mốc so sánh khi nghe: tiếng chiêu của Genshin Impact, Honkai: Star Rail, Wuthering Waves và các donghua Đấu La, Đấu Phá, Phàm Nhân Tu Tiên.

**Luật nền**
- Âm chiến đấu theo audio.md §5: ghép lớp, có bậc độ to, bùng nổ, vang. Luật phím mềm (AUDIO_PIPELINE §6.2 và dòng "Luật giọng đọc" của canon §22) chỉ áp cho `key-*` và âm chữ thành chiêu `key-word`.
- Pha nào có lóe thì có tiếng **cùng khung** (skill `game-vfx-layered` bước 8). Âm đi theo sự kiện của view; không đổi tick sim.
- Chỉ file thật: Firefly Generate Sound Effects, model Adobe, do anh tạo. Sub tổng hợp chỉ được làm một lớp nướng sẵn bên trong file thật (audio.md §5.7 bước 2). Game không có `OscillatorNode` (canon §22, D44).
- Mọi mẫu gửi anh duyệt (D55). Agent không nghe được: máy chỉ gắn cờ và xếp hạng, tai anh quyết.

## 1. Mô hình lớp

### 1.1 Năm loại lớp

| Lớp | Thuộc về | Đổi khi | Ví dụ |
|---|---|---|---|
| **A họ** | kiếm, đao, thương | đổi họ (đổi luôn bộ chiêu K → Đ, T) | kiếm "shing" cao |
| **B món** | 1 trong 10 món đợt 1 | đổi món | tiếng ngọc của Clear Wind |
| **C hệ** | 8 hệ | đổi sang món khác hệ | Lôi: sét đánh |
| S chiêu | từng chiêu: trận, vòng hộ thân, cột sáng, bầy kiếm | không đổi theo món | 3 kiếm quay của K3A |
| Chung | sub, đuôi không gian hẻm núi | không đổi | vọng hẻm đá vôi |

- **Ranh giới B và C:** B là **vật** (thép, ngọc, đá, gỗ, băng kết tinh, khe rỗng), C là **năng lượng** (lửa, nước, gió, sét…). B và C không được là cùng một tiếng. Ví dụ Ember Crest: B là thép nung xèo, C Hỏa là lửa bùng.
- Bộ Kiếm chỉ dùng họ kiếm và 4 món kiếm. Món đao và thương thuộc bộ Đ và T (làm sau). Lớp A của hai họ đó có id ở §3 để đặt nền từ đầu.

### 1.2 Lớp A: họ

| Họ | Chữ ký (WEAPON_DESIGN §5) | Phát (R) | Bay (T) | Trúng (I) | Đuôi (F) | Dải chính | Dùng cho |
|---|---|---|---|---|---|---|---|
| Kiếm | "shing" cao, thép reo | rút kiếm reo sắc, vung xé gió | rít mảnh, nhanh | thép chém đá giòn, thân chém dày, tiếng reo có cao độ | vọng thép trong hẻm đá vôi | đầu 3–8 kHz | K0–K5 (đợt này) |
| Đao | "whum" trầm, nặng | rút đao nghiến thép, vung ù | ù trầm | chẻ đá dữ, thân chặt nặng | vọng nặng hẻm sâu | thân 80–300 Hz | Đ0–Đ5 (sau) |
| Thương | "thuk" gọn | đâm gọn, cán quất gió | cán quất, xé gió | đâm xuyên giáp gọn, thân đẩy chắc | vọng khe núi | đẩy 100–250 Hz, nứt 2–5 kHz | T0–T5 (sau) |

Kiếm reo cao **không** được miễn luật trầm của T4–T6 (§4.1): mọi cue T4 trở lên của bộ Kiếm có lớp sub chung.

### 1.3 Lớp B: món (theo WEAPON_DESIGN §6)

| Món | Họ · Hệ | Dấu hình 40 px | Tiếng món (B) | Vai riêng | Đợt |
|---|---|---|---|---|---|
| Clear Wind | Kiếm · Kim | lưỡi xuyên vòng ngọc rỗng | ngọc bích reo khi thép chạm | nốt chữ ký của mọi cú trúng; "tiếng thép kèm tiếng ngọc" | S1 |
| Winter Vein | Kiếm · Băng | hai vai lục giác thấp | thép đông reo, mép giòn kết tinh | trúng để lại tiếng rạn ngắn (residue Băng 0,6–1 s) | S2 |
| Thunder Seal | Kiếm · Lôi | hộ thủ X bẹt, ấn thoi | ấn đồng đóng xuống, điện ù | ba tiếng điện khác nhau cho ba kiếm: biến thể cố định theo thứ tự kiếm, không ngẫu nhiên | bước đổi món |
| Verdant Branch | Kiếm · Mộc | lưỡi lá, hộ thủ Y lệch | lá thép xào xạc sắc | bầy kiếm K5 nghe như đàn lá kim loại (kit trail chồng lên bed bầy) | S2 |
| Ember Crest | Đao · Hỏa | gai lửa ở sống | thép nung xèo | lửa cam đỏ thật ở lớp C (D54) | L |
| Mountain Verdict | Đao · Thổ | sống ba bậc | lưỡi đá nghiến, cào đá trầm | tiếng đá dưới tiếng thép | L |
| Tidal Crescent | Đao · Thủy | cong nông ≤ 20° | lưỡi cong rạch nước | cung nước dài, không thành vòng | L |
| Sky Thread | Thương · Phong | khe giọt nước rỗng | gió rít qua khe, có cao độ | còi kéo dài trong 1–4 kHz: xử như đuôi (hạ 2–4 dB, nhường giọng đọc) | L |
| Resonant Fang | Thương · Kim | cổ bát giác rỗng | thép ngân dài | mỗi cú trúng một tiếng ngân 0,8–1,2 s; không được nghe thành chuông chùa | L |
| Storm Pin | Thương · Lôi | khe sét một nét | mũi thép rít điện cao | tia ziczac ở lõi: snap điện gọn | L |

Đợt: S1 lát cắt demo, S2 phần còn lại của bộ Kiếm, L sau khi có bộ Đ, T (§4.3).

### 1.4 Lớp C: hệ

| Hệ | Màu nhấn (SKILL_CATALOG §1) | Ignite (phát, bay) | Burst (trúng) | Residue (dư âm) | Họ "bẩn" (AUDIO_PIPELINE §4.4) |
|---|---|---|---|---|---|
| Kim | `#D6CFC0` | thép lấp lánh | thép va, vỡ sáng | ngân lấp lánh | không |
| Mộc | `#6E8B5E` | cành gãy giòn | rễ xé đá, gỗ toác | lá cuộn trong gió | không |
| Thủy | `#2E4A78` | nước dâng | sóng đập | nước chảy trên đá | không |
| Hỏa | `#FF7A2A` (D54) | lửa bùng | cầu lửa nổ | than nổ lách tách | có |
| Thổ | `#A08C6A` | đá nghiến | tảng đá nện | sỏi lăn, bụi | có |
| Lôi | `#9AA6FF` | hồ quang bật | sét đánh | tĩnh điện lách tách | có |
| Phong | `#BFD8C8` | gió giật | gió nổ | gió hú hẻm núi | không |
| Băng | `#CFE6F5` | băng rạn | băng vỡ | sương giá lan, rạn | có |

Họ "bẩn": audiobox có trọng số 0, chỉ xếp hạng bằng L2 và lựa chọn của anh.

### 1.5 Lớp nào phát ở pha nào

| Pha | A họ | S chiêu | B + C (món) | Chung |
|---|---|---|---|---|
| Gồng | — | bed gồng (K2–K5), swell (K2, K5) | kit `appear` (K1), kit `charge` | — |
| Phát | rút, vung | lớp riêng của K2, K3A, K3B, K4, K5 | chữ ký B + ignite C, **nướng trong cue** | sub từ T4 |
| Bay | rít bay | bed bầy K5 | kit `trail` (ignite C kéo dài; còi Sky Thread, điện Thunder Seal): nướng vào `cue-sword-travel`, chỉ K5 chồng lúc chạy | — |
| Trúng | đầu, thân, tiếng reo | chém tuyến, cắm, đỡ, mưa kiếm | nốt B + burst C, **nướng trong cue** | sub từ T4 |
| Dư âm | đuôi họ | đóng, hết | kit `residue` (C) | đuôi không gian, send |

### 1.6 Đổi vũ khí

- **Cue nướng theo món:** mọi cue một phát (phát, bay, trúng, mở, nhịp, đỡ, loạt) là một file cho mỗi món, dựng offline từ A hoặc S cộng B và C (§3.8). Một tiếng mỗi cue, mỗi file đúng bậc của nó (audio.md §5.4: "file nói đúng mức của nó").
- **Kit của món:** 4 stem `tt-sfx-kit-<món>-{appear,charge,trail,residue}`. `appear`, `charge`, `residue` chồng lên lúc chạy; `trail` nướng vào cue bay, chỉ K5 chồng nó lúc chạy (§3.7).
- **Dùng chung, không đổi theo món:** bed gồng, swell, vòng lặp K3A và K4, bed bầy K5, đuôi.
- **Đổi món** (chọn trước trận, đề xuất WEAPON_DESIGN §7): nạp và giải mã bộ cue nướng và 4 stem kit của món mới lúc vào trận; trong trận không đổi. Ước ~50 file mỗi món kiếm, ~4 MB sau giải mã.
- **Ví dụ:**
  - Clear Wind → Thunder Seal: A giữ, B đổi, C Kim → Lôi.
  - Clear Wind → Resonant Fang: A kiếm → thương (và bộ chiêu T), B đổi, C giữ Kim.
- **Nếu anh chốt hệ tách khỏi món** (câu hỏi D55 và D23 còn mở): dựng lại cue theo cặp (món, hệ) bằng cùng công thức. Master nguyên liệu B và C giữ riêng nên chỉ chạy lại script, không tạo lại âm.
- **Kiểm đổi món:** hai bản trộn cùng kịch bản, chỉ khác món. Khoảng cách âm học giữa hai món (mel 0–50 ms, đường bao; AUDIO_PIPELINE §5.2) phải lớn hơn độ trải giữa các biến thể của cùng món. Anh nghe mù và đoán đúng món.

## 2. Bộ Kiếm theo pha

### 2.1 Luật chung

- **Gồng (A)** theo tiến độ gõ 0–20–40–60–80–100 %:
  - File bed đặt ở −24 LUFS-M max; code hạ theo tiến độ: −10, −8, −6, −4, −2, 0 dB (tức −34 → −24). Lọc thấp mở dần.
  - Không thêm tiếng mỗi chữ: phím đã có tiếng (bus `typing`). Bed luôn ở dưới hoặc bằng mức phím trong bản trộn (−28 đến −24).
  - Khi còn 1 chữ, bed hạ −6 dB trong 60 ms. Đây là nhịp "hít" trước phát, thay khoảng lặng 40–80 ms của súng nặng (audio.md §5.3): game không biết trước lúc phím cuối đến, còn phát phải ≤ 50 ms sau phím cuối.
  - Phím cuối: cắt bed trong 10 ms. Từ hụt hoặc Esc: tắt trong 120 ms.
- **Phát (R)** đúng khung lóe R của view (≤ 50 ms sau phím cuối), chung khung với `key-word`. `key-word` thuộc hệ phím chung (mốc 9), không bị hạ.
- **Bay (T):** whoosh được lên lịch từ tick Cast để kết thúc đúng tick chạm. Pan theo x của mục tiêu, |pan| ≤ 0,6. Doppler bằng `playbackRate` ±3 %.
- **Trúng (I)** đúng tick canon, theo sự kiện sát thương của sim:
  - Gom mọi cú trúng trong 38 ms thành một cue. Bậc cao nhất trong lô thắng. Lô có ≥ 3 thú thêm lớp mass: thêm lớp, không chỉ thêm gain.
  - Thân của nạn nhân (lông, đá, giáp) thuộc danh sách thú (`beast-hit-*`); cue vũ khí không chứa tiếng thú. Mỗi lô 38 ms có tối đa 1 tiếng thú.
- **Dư âm (F):**
  - Đuôi là file riêng (`.tail`), dưới phần khô 8 LU (T2–T4) hoặc 6 LU (T5–T6).
  - Lọc 200 Hz–6,5 kHz, trễ trước 25 ms. Dải 1–4 kHz hạ 2–4 dB và nhường giọng đọc.
- **Dừng hình** (K2 35 ms, K5 70 ms): âm không dừng, không chậm lại (bài H).
- **Bậc gõ thêm lớp, không thêm gain:**
  - Hoàn hảo: nốt B sáng hơn (biến thể "bright" của cue trúng).
  - Chớp: thêm sub chung và một nốt B cao hơn một quãng tám. Cố định, để người chơi học được.
  - Kiếm Tâm: kiếm thứ 4 của băng dùng nốt bậc 3 cộng lớp Chớp.
- **Biến thể:** 3–5 bản cho đầu và thân; runtime thêm ngẫu nhiên ±60 cent. Cú trúng và nốt chữ ký gần như cố định (±20 cent), để người chơi học được.
- **Định dạng:** cue khô là mono (game pan theo vị trí). Đuôi, bed, vòng lặp và mọi cue của K5 là stereo.

### 2.2 Bảng mỗi chiêu

Tick 60 Hz tính từ tick Cast (canon §12.1). "Bậc" là LUFS-M max của file sau khi đặt bậc (audio.md §5.4). "Nhóm" là nhóm tiếng ở §2.3.

**K0 Phi Kiếm** (tự động, mỗi 1,2 s, tầm 10 m; catalog `kiem-auto`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | — | không: 0,83 lần/s, có tiếng gồng sẽ mỏi tai | | | | | |
| Phát | lệnh `auto`, khung lóe | `cue-k0-release` | T2 · −18 | 120–200 ms | đuôi chung kiếm | 0,10 | release |
| Bay | 0 → +18 | `cue-sword-travel` | dưới phát 3 LU | 250–300 ms | — | 0,05 | travel |
| Trúng | +18 | `cue-k0-hit` | T3 · −18 | 120–200 ms | — | 0,05 | hit |
| Dư âm | sau trúng | `cue-sword-tail` | khô − 8 LU | 0,8–1,2 s | là đuôi | 0 | tail |

**K1 Ngự Kiếm Quyết** (mỗi từ một băng 3 kiếm, chờ tối đa 2 băng; `kiem-volley`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | tiến độ 1/3 và 2/3 (kiếm hiện quanh vai) | kit `appear` | −30, dưới phím | 120 ms | — | 0 | charge |
| Phát | lóe R | `cue-k1-release`: một file cho cả 3 kiếm | T2 · −18 | 150–250 ms | — | 0,10 | release |
| Bay | tới +6, +36, +66 | `cue-sword-travel`, mỗi kiếm một; kiếm 1 nằm trong phát | dưới phát 3 LU | 250–400 ms | — | 0,05 | travel |
| Trúng | +6, +36, +66 | `cue-k1-hit-1/2/3`: nốt B 0, +2, +4 bán cung; kiếm 3 thêm sub | T3 · −19, −18, −17 | 120–220 ms (kiếm 3 ≤ 300 ms) | — | 0,05 | hit |
| Dư âm | sau kiếm 3 | `cue-sword-tail`, một đuôi mỗi băng | khô − 8 LU | 1–1,2 s | là đuôi | 0 | tail |

**K2 Nhất Tuyến Xuyên Vân** (đường 14 × 1,2 m; `kiem-line`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | lúc gõ; swell từ 80 % | `cue-charge-bed` + kit `charge`; `cue-k2-swell` | bed −34 → −24; swell ≤ −22 | theo gõ; swell 0,6 s | — | 0,05 | charge |
| Phát | lóe R | `cue-k2-release` (có sub) | T4 · −13 | 250–400 ms | `cue-k2-tail` | 0,25 | heavy |
| Bay | 0 → +12 | nằm trong file phát (0,2 s) | | | | | |
| Trúng | +12 | `cue-k2-impact`; lô ≥ 3 thú dùng bản `-mass` | T4 · −12 | 300–500 ms | `cue-k2-tail` | 0,25 | heavy |
| Dư âm | sau trúng (rãnh mực 4 s) | `cue-k2-tail` + kit `residue` | khô − 8 LU; residue −24 | 1,5–2,5 s | là đuôi | 0 | tail |

Cú trúng K2 hạ các cú trúng thường 3 dB trong 150 ms.

**K3A Hồi Kiếm Hộ Thân** (vòng r 2 m, 5 s, 3 lần đỡ; `kiem-ward`, `kiem-ward-block`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | lúc gõ | `cue-charge-bed` + kit `charge` | −34 → −24 | theo gõ | — | 0,05 | charge |
| Phát | lóe R (vòng triện dựng) | `cue-k3a-up` | T3 · −17 | 300–500 ms | — | 0,10 | release |
| Giữ | 5 s | `cue-k3a-loop`: một file chứa cả 3 kiếm quay | −22 | vòng 2–4 s, liền mối | — | 0,05 | loop |
| Đỡ | sự kiện `ward block` | `cue-k3a-block` | T4 · −13 | 250–450 ms | `cue-k3a-block-tail` 1–1,5 s | 0,25 | heavy |
| Hết | hết giờ hoặc hết 3 lần | `cue-k3a-end` | T2 · −19 | 300–450 ms, đuôi nướng | — | 0,10 | release |

**K3B Lưu Quang Bộ** (lướt 5 m, không sát thương; `kiem-dash`)

| Pha | Khi | Cue | Bậc | Dài | Send | Nhóm |
|---|---|---|---|---|---|---|
| Gồng | lúc gõ | `cue-charge-bed` | −34 → −24 | theo gõ | 0,05 | charge |
| Phát | lóe R | `cue-k3b-dash` | T3 · −17 | 250–400 ms | 0,08 | release |
| Đến | hết lướt (0,3 s) | `cue-k3b-land` (lớp phụ) | −22 | 120–200 ms | 0,05 | travel |

Không có pha trúng, không có đuôi riêng.

**K4 Lạc Kiếm Trận** (vùng r 3 m, 5 s; `kiem-zone`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | lúc gõ | `cue-charge-bed` + kit `charge` | −34 → −24 | theo gõ | — | 0,05 | charge |
| Phát | lóe R (kiếm vút lên) | `cue-k4-release` | T3 · −18 | 300–500 ms | — | 0,10 | release |
| Mở | +12 (`zone-open`) | `cue-k4-open`: 6 kiếm cắm, một file flam 6 cú trong 150–180 ms, sub ở cú 6; nhịp đầu nằm trong file này | T4 · −13 | 400–700 ms | `cue-k4-tail` 1,5–2 s | 0,25 | heavy |
| Giữ | +12 → +312 | `cue-k4-loop` | −22 | vòng 2–4 s | — | 0,05 | loop |
| Nhịp | +42, +72 … +282 (9 nhịp sau nhịp mở) | `cue-k4-beat` (có thú) / `cue-k4-beat-empty` | T3 · −19 / −23 | 150–250 ms | — | 0,05 | hit |
| Đóng | +312 (`zone-close`) | `cue-k4-close` + kit `residue` | T2 · −19 | 400–700 ms | nướng | 0,10 | release |

Nhịp xoay vòng 5 biến thể và không lặp liền. Lớp nhịp vẫn phát khi vùng trống, vì VFX vẫn lóe mỗi nhịp.

**K5 Thiên Hà Kiếm Vũ** (3 loạt, r 6 m; T5–T6, sự kiện P0; `kiem-ultimate`)

| Pha | Khi | Cue | Bậc | Dài | Đuôi | Send | Nhóm |
|---|---|---|---|---|---|---|---|
| Gồng | lúc gõ; swell từ 80 % | `cue-k5-charge-bed` (bed chung trộn sẵn lớp `charge-air`) + kit `charge`; `cue-k5-swell` | −34 → −24; swell ≤ −22 | theo gõ; 0,6 s | — | 0,05 | charge |
| Phát | lóe R (cột sáng, vòng đất) | `cue-k5-release` (sub, cắt mềm) | T5 · −10 | 0,4–0,5 s khô | `cue-k5-tail-0` 2 s | 0,40 | big |
| Bay | 0 → +120 | `cue-k5-swarm-low`, `-high`, `-whistle` + kit `trail`; đường bao phồng lên ở +30, +75, +120 | tổng −16 | 2,4 s | — | 0,20 | swarm |
| Loạt 1 | +30 | `cue-k5-volley-1` | T5 · −11 | 0,4–0,7 s | `cue-k5-tail-1` 2 s | 0,40 | big |
| Loạt 2 | +75 | `cue-k5-volley-2` (nốt B +1 bán cung) | T5 · −10 | 0,4–0,7 s | `cue-k5-tail-2` 2 s | 0,40 | big |
| Loạt 3 | +120 | `cue-k5-volley-3` (nốt B +2, thêm sub và đá vụn) | T6 · −8 | 0,6–1 s | `cue-k5-tail-3` 3 s | 0,40 | big |
| Dư âm | sau loạt 3 | đuôi 3 + kit `residue` | khô − 6 LU; residue −24 | 2–3 s | là đuôi | 0 | tail-big |

- Nhạc được hạ trước mỗi loạt ở tick +25, +70, +115 (83 ms trước cú chạm, trong khoảng 60–100 ms); bảng hạ tiếng ở §2.4.
- **Âm không theo số kiếm của bậc hình** (150/300/500 chỉ là hình, sim như nhau). Bậc Low bỏ `-high` và `-whistle` vì trần 16 tiếng.

### 2.3 Tiếng và chồng lớp

Trần canon §22: **32 tiếng (Low 16)**, mỗi âm ≤ 4 lần mỗi 100 ms. Chia (đề xuất, chỉnh bằng bài D):

| Kho | High | Low | Ghi chú |
|---|---|---|---|
| `typing` (phím, `key-word`) | 4 | 2 | kho riêng, combat không bao giờ cướp |
| `pronunciation` | 1 | 1 | kho riêng |
| `warnings` (báo đòn, Trận Lực < 30 %) | 3 | 2 | combat không cướp |
| nhạc, môi trường, trận pháp | 8 | 4 | danh sách khác quyết chia |
| thú (`enemies`, `world`: trúng, tan khói, triều) | 6 | 3 | danh sách thú |
| `self` (bộ Kiếm) | 10 | 4 | bảng dưới |

Nhóm trong kho `self` (trần nhóm theo audio.md §5.4; trần kho vẫn là 10 hoặc 4):

| Nhóm | High | Low | Gồm |
|---|---|---|---|
| charge | 3 | 1 | bed, kit `charge` hoặc `appear`, swell |
| release | 4 | 1 | phát K0, K1, K3A, K3B, K4; K3A hết, K4 đóng |
| travel | 3 | 1 | cue bay K0 và K1, kit `trail` của K5, K3B đến |
| hit | 6 | 2 | trúng K0, K1, nhịp K4 |
| heavy | 2 | 1 | K2, K3A đỡ, K4 mở |
| loop | 2 | 1 | K3A và K4, mỗi loại 1 |
| big | 1 | 1 | phát và các loạt K5 |
| swarm | 3 | 1 | bed bầy K5 |
| tail, tail-big | 2 + 2 | 1 | đuôi thường; đuôi K5 |

- **Thứ tự cướp:** trước hết cướp tiếng cũ nhất trong cùng nhóm, sau đó cướp tiếng ưu tiên thấp nhất (audio.md §5.4). Trong `self`, từ thấp lên cao:
  1. `appear`, swell
  2. travel
  3. tail thường
  4. nhịp K4
  5. trúng K0
  6. trúng K1
  7. loop
  8. release
  9. bed gồng
  10. heavy
  11. swarm
  12. big và tail-big: không bị cướp trong `self`

**Chồng lớp theo số kiếm**

| Số kiếm | Chiêu | Cách làm |
|---|---|---|
| 1 | K0 | 1 phát, 1 bay, 1 trúng |
| 3 | K1 (băng) | 1 phát cho cả băng. 3 tiếng bay nối nhau (≤ 3). 3 cú trúng cách nhau 0,5 s, nốt leo dần. Băng thứ hai nối sau băng trước; tiếng bay cũ nhất bị cướp trước |
| 3 | K3A (vòng) | 1 vòng lặp chứa cả 3 kiếm quay, không phải 3 tiếng |
| 4 | Kiếm Tâm | kiếm 4 = nốt bậc 3 + lớp Chớp |
| 6 | K4 | Mở là 1 file flam 6 cú nướng sẵn: offset 0, 30, 60, 90, 120, 150 ms ±10 ms, mỗi cú lấy từ một take khác. Mỗi nhịp 1 tiếng |
| 150–500 | K5 | **Không có tiếng cho từng kiếm.** Gồm 2–3 bed bầy (trầm, cao, rít), kit `trail`, 1 cue cho mỗi loạt (đã chứa lớp mass "trăm lưỡi chạm đá") và đuôi. Tối đa 7 tiếng ở High (1 big, 3 swarm, 1 trail, 2 đuôi; các đuôi 2–3 s gối nhau nên đuôi cũ nhất nhường), 4 ở Low (1 big, `swarm-low`, kit `trail`, 1 đuôi) |
| nhiều nguồn trong 38 ms | K0, K1, K4 | Gom thành 1 cue; bậc cao nhất thắng; lô ≥ 3 thú thêm lớp mass |

Đồng đội (M1): bus `allies`, ưu tiên 5, dưới `self` 6 dB. Lúc đó chia lại kho.

### 2.4 Ưu tiên và hạ tiếng

**Ưu tiên** theo canon §22 (số trong `catalog.ts`): phát âm từ của mình 1 → báo đòn và Trận Lực < 30 % 2 → phím 3 → chiêu của mình 4 → chiêu đồng đội và va chạm 5 → bầy và môi trường 6. Chiêu của mình không bao giờ hạ hay cướp tiếng phím, giọng đọc hay báo đòn.

**Hạ tiếng** (WebAudio không có sidechain: tự động hóa gain như hàm `duck()` ở audio.md §5.8)

| Nguồn kích | Đích | Mức | Thời gian |
|---|---|---|---|
| Giọng đọc từ. Canon: trong trận đọc từ < 40 độ thuộc **sau khi cast**, nên đúng lúc chiêu phát | nhạc | −6 dB (đề xuất; canon chưa ghi) | vào từ `pronouncer.request`; giữ tới `end`, tối đa 3 s; nhả 300–500 ms |
| | vang trả về, đuôi, vòng lặp, bed gồng, bed bầy | −6 dB | như trên |
| | phần khô của phát và trúng (cả K5) | tối đa −3 dB | như trên |
| | phím | theo hệ phím chung (mốc 9); spec này không đổi | — |
| K5: phát và mỗi loạt (P0) | combat thường: K0, K1, nhịp K4, trúng của thú, tan khói | 0,6 (−4,5 dB) | vào trong 8–12 ms, giữ 120–250 ms, về trong ~300 ms |
| | nhạc | −4 đến −6 dB | bắt đầu 83 ms trước cú chạm (tick −5) |
| | môi trường | −6 dB | như hàng combat |
| | phím, UI | tối đa −2 dB | như hàng combat |
| | báo đòn, giọng đọc | không hạ | — |
| K2 trúng, K3A đỡ, K4 mở (T4) | trúng thường | −3 dB | 150 ms |
| Bed gồng | phím | không hạ phím; bed tự nằm dưới phím | — |

### 2.5 Không gian và bus

- **Một không gian:** hẻm đá vôi Thanh Thạch Ải (canon Q6: "đuôi vang hẻm núi").
  - IR tự làm theo audio.md §5.7 bước 4: dài 3,5 s, thêm slapback vách xa `aecho=0.8:0.7:180|330:0.35|0.2`. Bản 3,5 s chưa chạy thử.
  - Thử thêm một IR CC0 "mountain ranges" hoặc "ravines" từ gói Tim_Verberne (đọc giấy phép từng trang, ghi vào THIRD_PARTY). Anh nghe rồi chọn một.
- **Send:** send → trễ trước 25 ms → lọc cao 180 Hz → ConvolverNode → lọc thấp 6,5 kHz → return 0,5. Return nhường giọng đọc.
  - Bậc Low không chạy convolver trực tiếp: nướng đuôi lúc nạp bằng `OfflineAudioContext`.
  - Đuôi đã nướng không đi vào send (send 0), để không vang hai lần.
- **Bus `self`:** level → duck → glue (ngưỡng −18, knee 6, tỉ lệ 3, attack 25 ms, release 150 ms) → gain bỏ makeup tự động ≈ −7,2 dB (đo bằng `OfflineAudioContext`) → master.
  - Không dùng compressor nhanh. Bus `typing` và `ui` đi vòng qua compressor của combat.
  - Master có limiter an toàn (−3, knee 0, tỉ lệ 20, 1 ms, 80 ms) rồi trim, để bản chụp trận ≤ −1 dBTP.
  - Không chép cấu hình glue từ `games/dragon-hold/src/audio/{mixer,limiter}.ts` mà không đo lại (bẫy của audio.md §5.1).

## 3. File và prompt Firefly

### 3.1 Quy ước

- **Id `tt-sfx-<nhóm>-<tên>`:**
  - Nguyên liệu Firefly: nhóm `sword`, `sabre`, `spear`, `common`, `item`, `elem`, `kiem`.
  - Cue dựng: nhóm `cue`. Cue nướng theo món thêm đuôi `-<món>`, ví dụ `tt-sfx-cue-k0-hit-clearwind`.
  - Stem kit của món: nhóm `kit`.
  - Tiền tố `tt-sfx-` để không lẫn với id Tĩnh Tu `tt-*` trong `src/audio/catalog.ts`.
- **Nhận file:** `~/AudioLab/inbox/firefly/immortality-cultivation/<id>/`, giữ tên Firefly đặt. Dòng nguồn: "Adobe Firefly Generate Sound Effects, generated by the project owner (Adobe model)".
- **Lượt tạo:** mỗi lần tạo cho 4 bản. Vòng 1 là một lần tạo cho mỗi id. Tối đa 3 vòng prompt mỗi id (audio.md §5.9).
- **Prompt:** ≤ 12 từ, ngăn bằng dấu phẩy, một lớp, tiếng Anh. Lớp đầu xin "dry, isolated", lớp đuôi xin "no transient".
  - Không dùng từ cấm của audio.md §5.6.
  - Không dùng từ cấm của Q6: puff, pop, balloon, thump hoặc thud đứng riêng.
- **Giọng mẫu:** lớp nào cần đúng đường bao thì anh ghi nhịp bằng giọng rồi dùng voice to sound effects của Firefly.
- **Cột "Cắt":** độ dài lớp sau khi cắt ở §5.7 bước 2, không phải độ dài file Firefly.
- **Đợt:** S1, S2, L như §1.3. Bước đổi món (Thunder Seal) ghi "Đổi".

### 3.2 Lớp A

| Id | Vai | Prompt | Cắt | Đợt |
|---|---|---|---|---|
| `tt-sfx-sword-draw` | đầu phát | `sword drawn from sheath, sharp ringing steel, punchy, dry, isolated` | 15–40 ms | S1 |
| `tt-sfx-sword-swing` | thân phát | `powerful sword swing, fast cutting whoosh, heavy, dry` | 80–150 ms | S1 |
| `tt-sfx-sword-flyby` | bay | `flying sword whizzing past, sharp whistling whoosh, fast, intense` | 250–400 ms | S1 |
| `tt-sfx-sword-hit-head` | đầu trúng | `sword striking stone armor, sharp metallic crack, punchy, dry, isolated` | 15–40 ms | S1 |
| `tt-sfx-sword-hit-body` | thân trúng | `heavy blade slash impact, dense, punchy, saturated, dry` | 80–150 ms | S1 |
| `tt-sfx-sword-ring` | nốt xác nhận trúng | `steel blade ringing, bright metallic ping, sharp attack, dry` | 25–90 ms | S1 |
| `tt-sfx-sword-tail` | đuôi | `sword clash echoing across vast limestone canyon, rolling echo, no transient` | 1–2 s | S1 |
| `tt-sfx-sabre-draw` | đầu phát | `heavy broadsword drawn, deep grinding steel, powerful, dry, isolated` | 20–50 ms | L |
| `tt-sfx-sabre-swing` | thân phát | `massive broadsword swing, deep heavy whoosh, powerful, dry` | 100–250 ms | L |
| `tt-sfx-sabre-hit-head` | đầu trúng | `broadsword cleaving stone, violent metallic crack, very loud, dry` | 15–40 ms | L |
| `tt-sfx-sabre-hit-body` | thân trúng | `heavy blade chopping impact, massive, deep, punchy, saturated` | 100–250 ms | L |
| `tt-sfx-sabre-tail` | đuôi | `heavy blade impact echoing through deep canyon, rolling echo, no transient` | 1–2 s | L |
| `tt-sfx-spear-thrust` | đầu phát | `spear thrust, sharp piercing jab, fast, punchy, dry, isolated` | 15–40 ms | L |
| `tt-sfx-spear-shaft` | thân phát, bay | `long spear shaft whipping through air, powerful swoosh, dry` | 100–300 ms | L |
| `tt-sfx-spear-hit-head` | đầu trúng | `spear piercing stone armor, sharp punchy crack, dry, isolated` | 15–40 ms | L |
| `tt-sfx-spear-hit-body` | thân trúng | `heavy spear impact, deep punchy strike, dense, saturated` | 80–200 ms | L |
| `tt-sfx-spear-tail` | đuôi | `spear strike echoing across mountain ravine, rolling echo, no transient` | 1–2 s | L |

Lớp đầu dưới 50 ms (`*-hit-head`, `sword-ring`, `*-draw`) là thứ AI làm kém. Nếu take nhòe đầu tiếng, lấy lớp CC0 thay (Kenney Impact Sounds; audio.md §5.9), ghi nguồn.

### 3.3 Lớp chung

| Id | Vai | Prompt | Cắt | Đợt |
|---|---|---|---|---|
| `tt-sfx-common-sub` | sub T4–T6 | `huge sub bass impact, deep pressure wave, cinematic` | 120–300 ms | S1 |

Nếu take không đạt, dùng sine rơi của audio.md §5.7 bước 2 làm lớp sub, nướng offline vào file thật. Không tạo sub bằng oscillator trong game.

### 3.4 Lớp B (nháp, soát lại khi anh chốt hình từng món)

| Id | Món | Prompt | Cắt | Đợt |
|---|---|---|---|---|
| `tt-sfx-item-clearwind` | Clear Wind | `jade disc struck by steel, bright crystalline chime, resonant, sharp attack` | 60–400 ms | S1 |
| `tt-sfx-item-wintervein` | Winter Vein | `frozen steel blade ringing, brittle crystalline edge, cold, sharp` | 60–400 ms | S2 |
| `tt-sfx-item-thunderseal` | Thunder Seal | `bronze seal stamped, charged electric buzz, sharp, punchy` | 80–400 ms; giữ 3 bản khác cao độ | Đổi |
| `tt-sfx-item-verdantbranch` | Verdant Branch | `flurry of steel leaves, sharp shimmering rustle, bright, fast` | 100–500 ms | S2 |
| `tt-sfx-item-embercrest` | Ember Crest | `red-hot steel hissing, sharp sizzling flare, fierce` | 100–400 ms | L |
| `tt-sfx-item-mountainverdict` | Mountain Verdict | `heavy stone blade grinding, deep rock scrape, massive` | 100–400 ms | L |
| `tt-sfx-item-tidalcrescent` | Tidal Crescent | `long curved blade slicing water, wet metallic swish, powerful` | 100–400 ms | L |
| `tt-sfx-item-skythread` | Sky Thread | `wind whistling through hollow spearhead, piercing airy tone, fast` | 150–600 ms | L |
| `tt-sfx-item-resonantfang` | Resonant Fang | `struck steel spear ringing, long singing metallic resonance, powerful` | 0,8–1,2 s | L |
| `tt-sfx-item-stormpin` | Storm Pin | `steel spike crackling with current, sharp high electric whine, intense` | 80–400 ms | L |

### 3.5 Lớp C

| Id | Prompt | Cắt | Đợt |
|---|---|---|---|
| `tt-sfx-elem-kim-ignite` | `steel shimmering, bright metallic sparkle, sharp attack` | 100–400 ms | S1 |
| `tt-sfx-elem-kim-burst` | `metal blades clashing, bright ringing crash, powerful, sharp` | 100–500 ms | S1 |
| `tt-sfx-elem-kim-residue` | `metallic shimmer ringing out, glittering resonance, echoing` | 1–2,5 s | S1 |
| `tt-sfx-elem-loi-ignite` | `electric arc ignition, violent crackling snap, sharp attack` | 100–400 ms | Đổi |
| `tt-sfx-elem-loi-burst` | `thunder strike, explosive electric crack, very loud` | 100–600 ms | Đổi |
| `tt-sfx-elem-loi-residue` | `static electricity crackling, fierce sparks, buzzing` | 1–2,5 s | Đổi |
| `tt-sfx-elem-bang-ignite` | `ice cracking, sharp freezing crackle, crisp` | 100–400 ms | S2 |
| `tt-sfx-elem-bang-burst` | `ice shattering, massive glassy crash, sharp, very loud` | 100–600 ms | S2 |
| `tt-sfx-elem-bang-residue` | `frost spreading, crackling ice, glittering` | 0,6–2,5 s | S2 |
| `tt-sfx-elem-moc-ignite` | `wooden branches snapping, sharp cracking wood, powerful` | 100–400 ms | S2 |
| `tt-sfx-elem-moc-burst` | `roots tearing through stone, heavy splintering wood, massive` | 150–600 ms | S2 |
| `tt-sfx-elem-moc-residue` | `leaves swirling in strong wind, dense rustling` | 1–2,5 s | S2 |
| `tt-sfx-elem-hoa-ignite` | `fire ignition, violent flame burst, sharp attack` | 100–400 ms | L |
| `tt-sfx-elem-hoa-burst` | `fireball explosion, roaring flames, very loud, powerful` | 200–800 ms | L |
| `tt-sfx-elem-hoa-residue` | `embers crackling, burning debris, fierce` | 1–2,5 s | L |
| `tt-sfx-elem-tho-ignite` | `heavy rock grinding, deep stone scrape, powerful` | 100–400 ms | L |
| `tt-sfx-elem-tho-burst` | `boulder smashing into ground, massive rock crunch, very loud` | 200–800 ms | L |
| `tt-sfx-elem-tho-residue` | `gravel and dust settling, rolling rocks, crumbling` | 1–2,5 s | L |
| `tt-sfx-elem-thuy-ignite` | `water surging, powerful rushing splash, sharp attack` | 100–400 ms | L |
| `tt-sfx-elem-thuy-burst` | `massive water wave crashing, heavy splash, powerful` | 200–800 ms | L |
| `tt-sfx-elem-thuy-residue` | `water rushing over stone, swirling, echoing` | 1–2,5 s | L |
| `tt-sfx-elem-phong-ignite` | `sharp wind gust, fast howling whoosh, powerful` | 100–400 ms | L |
| `tt-sfx-elem-phong-burst` | `violent wind blast, roaring gust, explosive` | 200–700 ms | L |
| `tt-sfx-elem-phong-residue` | `wind howling through canyon, swirling, spacious` | 1–2,5 s | L |

### 3.6 Lớp S của bộ Kiếm

| Id | Chiêu, vai | Prompt | Giọng mẫu | Cắt | Đợt |
|---|---|---|---|---|---|
| `tt-sfx-kiem-charge-bed` | gồng, nền | `deep humming energy gathering, rising, powerful, sustained` | — | vòng 2–4 s | S1 |
| `tt-sfx-kiem-charge-air` | gồng, lớp trên của K5 | `airy metallic shimmer rising, bright, intense, sustained` | — | vòng 2–4 s | S1 |
| `tt-sfx-kiem-line-release` | K2 phát | `piercing sword beam launching, violent tearing whoosh, very loud` | "mmmm-SHIIING" | 250–400 ms | S1 |
| `tt-sfx-kiem-line-slice` | K2 trúng | `long blade slicing through rock, sharp tearing crack, powerful` | — | 200–400 ms | S1 |
| `tt-sfx-kiem-ward-up` | K3A phát | `swords locking into a spinning ring, heavy metallic clang` | — | 300–500 ms | S2 |
| `tt-sfx-kiem-ward-loop` | K3A giữ | `three swords orbiting fast, steady spinning whoosh, metallic hum` | — | vòng 2–4 s | S2 |
| `tt-sfx-kiem-ward-block` | K3A đỡ | `massive shield clash, heavy metal impact, booming, sharp attack` | "KLANG" | 250–450 ms | S2 |
| `tt-sfx-kiem-ward-end` | K3A hết | `spinning blades slowing down, descending whoosh, metallic, echoing` | — | 300–450 ms | S2 |
| `tt-sfx-kiem-dash` | K3B phát | `fast dash, sharp air burst, powerful whoosh, dry` | — | 250–400 ms | S2 |
| `tt-sfx-kiem-dash-land` | K3B đến | `boots skidding on stone, sharp scrape, punchy, dry` | — | 120–200 ms | S2 |
| `tt-sfx-kiem-array-launch` | K4 phát | `swords shooting skyward, rising metallic whoosh, fast, intense` | — | 300–500 ms | S2 |
| `tt-sfx-kiem-array-stake` | K4 mở (một cú; 6 cú dựng offline) | `sword plunging into stone ground, heavy metallic impact, punchy` | "tsss-TAK" | 80–200 ms | S2 |
| `tt-sfx-kiem-array-loop` | K4 giữ | `sword formation humming, deep resonant drone, powerful, sustained` | — | vòng 2–4 s | S2 |
| `tt-sfx-kiem-array-beat` | K4 nhịp | `blade formation pulse, sharp metallic slash, punchy, dry` | — | 150–250 ms | S2 |
| `tt-sfx-kiem-array-close` | K4 đóng | `swords pulled from stone, grinding metallic scrape, echoing` | — | 400–700 ms | S2 |
| `tt-sfx-kiem-rain-release` | K5 phát | `radiant energy pillar erupting, massive blast, very loud, cinematic` | "hmmmm-VOOOM" | 0,4–0,5 s | S1 |
| `tt-sfx-kiem-rain-swarm-low` | K5 bay, bed trầm | `thousands of swords flying, roaring metallic swarm, massive` | — | 2,4 s | S1 |
| `tt-sfx-kiem-rain-swarm-high` | K5 bay, bed cao | `dense rain of blades, shimmering metallic hiss, intense` | — | 2,4 s | S1 |
| `tt-sfx-kiem-rain-swarm-whistle` | K5 bay, rít | `swords whistling overhead, many sharp whistles, cinematic` | — | 2,4 s | S1 |
| `tt-sfx-kiem-rain-impact-head` | K5 loạt, đầu | `massive blade storm striking ground, explosive crack, very loud, dry` | "pshh-KRAK" | 20–50 ms | S1 |
| `tt-sfx-kiem-rain-impact-body` | K5 loạt, thân | `huge cinematic impact, deep boom, powerful, debris` | — | 250–500 ms | S1 |
| `tt-sfx-kiem-rain-mass` | K5 loạt, trăm lưỡi | `hundreds of blades hitting stone, dense metallic clatter, violent` | — | 0,3–1 s | S1 |
| `tt-sfx-kiem-rain-debris` | K5 loạt 3, đá vụn | `rock debris raining down, heavy rubble, crumbling` | — | 0,5–1,5 s | S1 |
| `tt-sfx-kiem-rain-tail` | K5 đuôi (bản Firefly, so với đuôi IR) | `gigantic impact echoing across vast canyon, rolling echo, no transient` | — | 2–3 s | S1 |

**Tổng: 76 prompt.**

| Đợt | Gồm | Số prompt |
|---|---|---|
| S1 | 7 A kiếm, 1 chung, 1 B, 3 C Kim, 13 S | 25 |
| Đổi | 1 B, 3 C Lôi | 4 |
| S2 | 11 S, 2 B, 6 C | 19 |
| L | 10 A đao và thương, 6 B, 12 C | 28 |

### 3.7 Kit của mỗi món (4 stem runtime)

| Stem | Dựng từ | Dài | Mức (LUFS-M max) | Dùng ở |
|---|---|---|---|---|
| `tt-sfx-kit-<món>-appear` | B, cắt 120 ms, lọc cao 4 kHz | 120 ms | −30 | K1 gồng (kiếm hiện) |
| `tt-sfx-kit-<món>-charge` | residue C lọc cao 3 kHz, cộng B lặp | vòng 2–4 s | −30 khi đầy (dưới bed 6 LU) | gồng K2–K5 |
| `tt-sfx-kit-<món>-trail` | phần kéo dài của ignite C, cộng B (còi Sky Thread; 3 bản điện cố định theo thứ tự kiếm của Thunder Seal) | 250–600 ms | −24 | nướng vào `cue-sword-travel`; lúc chạy chỉ ở K5, trên bed bầy |
| `tt-sfx-kit-<món>-residue` | residue C, lọc 150 Hz–7 kHz | 1–2,5 s | −24 | dư âm K2, K4, K5; Winter Vein thêm 0,6–1 s sau mỗi cú trúng |

### 3.8 Cue dựng (offset tính từ đầu lớp đầu)

`B` là lớp món, `C·x` là lớp hệ phần x. Cột "Bước" là bước ở audio.md §5.7. Mọi cue có `B` hoặc `C` được nướng cho từng món.

| Cue | Nguyên liệu và offset | Bước | Bậc | Biến thể |
|---|---|---|---|---|
| `cue-k0-release` | sword-draw 0, sword-swing +3, B +5, C·ignite +5 | 2, 3, 8, 9 | T2 −18 | 3–5 |
| `cue-k0-hit` | sword-hit-head 0, sword-ring 0, sword-hit-body +3, B (nốt) +5, C·burst cắt 150 ms +5 | 2, 3, 8 | T3 −18 | 3 + bản "bright" + bản Chớp |
| `cue-sword-travel` | sword-flyby 0, kit trail 0 (Thunder Seal: bản 1, 2, 3 theo thứ tự kiếm) | 2, 3, 8 | −21 (dưới phát 3 LU) | 3 |
| `cue-sword-tail` | đuôi qua IR từ bản K0 trúng chỉ có lớp A; hoặc take `sword-tail` lọc cao 200 Hz | 4, 5 (BELOW 8) | khô − 8 | 2 |
| `cue-k1-release` | như K0 phát, thêm sword-swing thứ hai +8 | 2, 3, 8, 9 | T2 −18 | 3–5 |
| `cue-k1-hit-1/2/3` | K0 trúng, nốt B 0, +2, +4 bán cung (`asetrate` chỉ trên lớp B); hit-3 thêm common-sub +6 | 2, 3, 8 | T3 −19/−18/−17 | 1 nốt × 2 thân |
| `cue-charge-bed` | kiem-charge-bed, cắt vòng (crossfade 50 ms của build Audio Lab) | 2 | −24 (code hạ theo tiến độ) | 1 |
| `cue-k5-charge-bed` | kiem-charge-bed, kiem-charge-air dưới 6 LU, cắt vòng | 2, 3 | −24 (code hạ theo tiến độ) | 1 |
| `cue-k2-swell`, `cue-k5-swell` | pre-verb từ kiem-line-release, kiem-rain-release | 7 | ≤ −22 | 1 |
| `cue-k2-release` | kiem-line-release 0, sword-draw 0, B +5, C·ignite +5, common-sub +6 | 2, 3, 8 | T4 −13 | 3 |
| `cue-k2-impact` (`-mass`) | kiem-line-slice 0, sword-hit-head 0, sword-hit-body +3, B +5, C·burst +5, common-sub +6 (bản mass thêm rain-mass cắt 300 ms +10) | 2, 3, 8 | T4 −12 | 3 + 1 |
| `cue-k2-tail` | IR 3,5 s từ bản trúng chỉ có lớp A và S | 4, 5 (BELOW 8) | khô − 8 | 1 |
| `cue-k3a-up` | kiem-ward-up 0, B +5, C·ignite +5 | 2, 3, 8 | T3 −17 | 2 |
| `cue-k3a-loop` | kiem-ward-loop, cắt vòng | 2 | −22 | 1 |
| `cue-k3a-block` | kiem-ward-block 0, sword-hit-head 0, B +5, C·burst +5, common-sub +6 | 2, 3, 8 | T4 −13 | 3 |
| `cue-k3a-block-tail` | IR từ bản đỡ chỉ có lớp S | 4, 5 (BELOW 8) | khô − 8 | 1 |
| `cue-k3a-end` | kiem-ward-end + đuôi nướng | 2, 5, 6, 8 | T2 −19 | 1 |
| `cue-k3b-dash` | kiem-dash 0, sword-swing +3, B +5, C·ignite +5 | 2, 3, 8 | T3 −17 | 3 |
| `cue-k3b-land` | kiem-dash-land | 2, 8 | −22 | 3 |
| `cue-k4-release` | kiem-array-launch 0, B +5, C·ignite +5 | 2, 3, 8 | T3 −18 | 2 |
| `cue-k4-open` | 6 × kiem-array-stake (0/30/60/90/120/150 ms ±10, mỗi cú một take); cú 6 thêm common-sub +4, B và C·burst +5 | 2, 3, 8 | T4 −13 | 3 |
| `cue-k4-tail` | IR từ bản mở chỉ có lớp S | 4, 5 (BELOW 8) | khô − 8 | 1 |
| `cue-k4-loop` | kiem-array-loop, cắt vòng | 2 | −22 | 1 |
| `cue-k4-beat` / `-empty` | kiem-array-beat 0, sword-ring 0, B (nốt) +5, C·burst cắt 120 ms +5; bản `empty` bỏ C·burst | 2, 3, 8 | T3 −19 / −23 | 5 + 3 |
| `cue-k4-close` | kiem-array-close + đuôi nướng | 2, 5, 6, 8 | T2 −19 | 1 |
| `cue-k5-release` | kiem-rain-release 0, sword-draw ×3 (0/25/50), B +5, C·burst +5, common-sub +6; đẩy 6 dB vào tanh rồi đặt bậc | 2, 3, 8 (cắt mềm) | T5 −10 | 2 |
| `cue-k5-swarm-low/-high/-whistle` | rain-swarm-*; đường bao phồng ở 0,5 / 1,25 / 2,0 s (`volume` theo thời gian) | 2 | tổng −16 | 1 mỗi lớp |
| `cue-k5-volley-1/2/3` | rain-impact-head 0, rain-impact-body +3, common-sub +6, rain-mass +10, B +5 (0/+1/+2 bán cung), C·burst +5; loạt 3 thêm rain-debris +40 và sub thứ hai | 2, 3, 8 (cắt mềm) | −11 / −10 / T6 −8 | 1 mỗi loạt: cố định để học |
| `cue-k5-tail-0…3` | IR 3,5 s từ bản loạt chỉ có lớp S, **hoặc** take `kiem-rain-tail` lọc cao 200 Hz; thử cả hai | 4, 5 (BELOW 6) | khô − 6 | 1 mỗi cái |

- **Đặt bậc phần khô thấp hơn bậc 1 LU,** vì stem kit và đuôi cộng thêm lúc chạy. Đo tổng trên bản dựng offline với cùng offset như runtime (harness, AUDIO_PIPELINE §6.1). Lệch thì sửa file khô, không sửa gain bus.
- **Mỗi cue một công thức** `art-src/audio/recipes/<cue>.json`, nhận món làm tham số. Một lệnh dựng đủ cue cho mọi món.

### 3.9 Chuỗi ffmpeg (audio.md §5.7; chạy trong bash; định nghĩa `mmax`, `tp`, `crest` lấy từ bước 1)

Ví dụ `tt-sfx-cue-k0-hit-clearwind`:

```bash
# Build the Clear Wind K0 hit from Firefly takes (audio.md §5.7 steps 2, 3, 8). Mono dry cue.
FF="ffmpeg -hide_banner -loglevel error -y"
# Step 2: prepare each layer for its job.
$FF -i sword-hit-head.wav -af "aresample=48000,highpass=f=1800,afade=t=out:st=0.04:d=0.03,atrim=0:0.08" -ac 1 L_head.wav
$FF -i sword-ring.wav -af "aresample=48000,highpass=f=1500,afade=t=out:st=0.06:d=0.03,atrim=0:0.09" -ac 1 L_ring.wav
$FF -i sword-hit-body.wav -af "aresample=48000,highpass=f=90,equalizer=f=300:t=q:w=1.2:g=-3,lowpass=f=9000,afade=t=out:st=0.12:d=0.08,atrim=0:0.2" -ac 1 L_body.wav
$FF -i item-clearwind.wav -af "aresample=48000,highpass=f=400,afade=t=out:st=0.25:d=0.15,atrim=0:0.4" -ac 1 L_item.wav
$FF -i elem-kim-burst.wav -af "aresample=48000,highpass=f=300,afade=t=out:st=0.1:d=0.05,atrim=0:0.15" -ac 1 L_elem.wav
# Step 3: head 0, ring 0, body +3 ms, item and element +5 ms; parallel comp, tanh clip, 192 kHz limiter.
$FF -i L_head.wav -i L_ring.wav -i L_body.wav -i L_item.wav -i L_elem.wav -filter_complex \
"[2]adelay=3:all=1[b];[3]adelay=5:all=1[i];[4]adelay=5:all=1[e];\
[0][1][b][i][e]amix=inputs=5:weights=1 0.7 0.9 0.6 0.5:normalize=0:duration=longest,asplit=2[x][y];\
[y]acompressor=threshold=0.06:ratio=8:attack=25:release=90:makeup=3[c];[x][c]amix=inputs=2:weights=1 0.6:normalize=0,\
asoftclip=type=tanh:threshold=0.85,aresample=192000,alimiter=limit=0.84:attack=1:release=40:level=0,aresample=48000[o]" \
-map "[o]" k0_hit_dry.wav
# Step 8: tier T3 at -18 minus 1 LU for runtime layers.
T=-19; G=$(awk -v m="$(mmax k0_hit_dry.wav)" -v t=$T 'BEGIN{printf "%.2f",t-m}')
$FF -i k0_hit_dry.wav -af "volume=${G}dB,aresample=192000,alimiter=limit=-1.3dB:attack=0.5:release=40:level=false,aresample=48000" -c:a pcm_s24le tt-sfx-cue-k0-hit-clearwind.wav
```

Khác ví dụ gốc: lớp khô là mono (`-ac 1`, `adelay=…:all=1`), thêm hai lớp B và C. Các bước khác chép nguyên:
- **Đuôi:** bước 5, `BELOW=8` cho T2–T4, `6` cho T5–T6.
- **Bản nghe khô cộng đuôi:** bước 6.
- **Swell:** bước 7.
- **T5–T6:** cắt mềm rồi đặt bậc (bước 8).
- **Biến thể:** bước 9 (±1,5 bán cung offline, ±60 cent lúc chạy).

Các bẫy cũ vẫn áp dụng:
- `alimiter` luôn có `level=0` hoặc `level=false`;
- `amix` luôn có `normalize=0`;
- không chạy `loudnorm` trên một cú;
- không bật `oversample` cho `asoftclip`;
- OGG mã bằng build của Audio Lab, vì ffmpeg Homebrew không có libvorbis.

### 3.10 Lớp P phép (D56, thêm 02/11 sau khi anh chốt phong cách)

Lớp này mang chất anime và thần thoại cho mọi chiêu. Nó phát cùng khung với pha có lóe, nằm trên nguyên liệu thật của lớp A, B, C. Prompt theo luật audio.md §5: không quá 12 từ, không dùng từ cấm.

| Id | Pha | Prompt Firefly | Độ dài | Bậc |
|---|---|---|---|---|
| `tt-sfx-magic-surge` | gồng (A), theo chữ gõ | `rising magical energy surge, shimmering crystal sparkles, anime spell charge` | 0,6–1,5 s | T3 |
| `tt-sfx-magic-release` | phát (R) | `explosive magical burst, radiant shimmering whoosh, anime sword technique` | 0,2–0,5 s | T4 |
| `tt-sfx-magic-trail` | bay (T) | `glittering energy streak whoosh, sparkling magical trail, fast, airy` | 0,3–0,8 s | T3 |
| `tt-sfx-magic-impact` | trúng (I) | `huge magical impact boom, crystalline shatter sparkle, reverberant, cinematic` | 0,4–1,2 s | T4–T5 |
| `tt-sfx-magic-aura` | đuôi (F) | `glowing magical aura shimmer, sparkling chime tail, ethereal, wide` | 1–3 s | T2 |
| `tt-sfx-magic-choir` | tuyệt kỹ (K5) | `heavenly choir swell, epic magical rise, radiant, cinematic anime` | 1,5–3 s | T5 |
| `tt-sfx-magic-sub` | tuyệt kỹ, trúng lớn | `deep cinematic sub boom, magical shockwave, massive, reverberant` | 0,6–1,5 s | T6 |

- **Ghép:** lớp P vào chuỗi ffmpeg ở §3.9 như một lớp nữa, cùng offset với lớp đầu của pha. Nguyên liệu thép, ngọc, đá hạ xuống làm thân bên dưới.
- **Nghe thử:** lát cắt Clear Wind (§4) phải có lớp P ngay từ đầu. Bản demo cho anh nghe có hai bản cạnh nhau, "chỉ nguyên liệu" và "có lớp P", để anh thấy khác biệt.

## 4. Nghiệm thu

### 4.1 Cổng máy (mỗi file và mỗi cue dựng đủ)

| Cổng | Ngưỡng | Nguồn |
|---|---|---|
| L1 vệ sinh (chặn) | Không clip, không đỉnh phẳng. Im lặng đầu ≤ 5 ms. Thời gian lên ≤ 10 ms cho phát và trúng. DC < 0,1 %. ≤ −1 dBTP. Độ dài lệch ≤ 20 %. Đuôi xuống −60 dB. Vòng lặp: bước nhảy < −40 dBFS, RMS lệch < 1 dB, trọng tâm phổ lệch < 10 %. 48 kHz | AUDIO_PIPELINE §4.3.1 |
| L1b (gắn cờ) | Tiếng vọng trước đầu tiếng; rít cao tần; xoáy pha ("kim loại giả", cần soi kỹ ở tiếng ngọc, thép reo, Resonant Fang); rung cao độ ở đuôi > 20 cent | §4.3.2 |
| Bậc | LUFS-M max đúng bậc ở §2.2; ≤ −1 dBTP | audio.md §5.4, §5.10 |
| Crest | Lớp đầu ≥ 12 dB trước khi đặt bậc; T5–T6 ≥ 10 dB sau cắt mềm | §5.10 |
| Trầm | T4–T6 (K2, K3A đỡ, K4 mở, K5) có ≥ 25 % năng lượng dưới 150 Hz, đo trên cue đủ | §5.10 |
| Đuôi | Bản nghe T4–T6 còn năng lượng ở +500 ms, không thấp hơn đỉnh quá 30 dB. Stem đuôi lọc cao ≥ 150 Hz | §5.10 |
| L2–L5 (xếp hạng) | Xếp trong nhóm. Họ bẩn: audiobox trọng số 0. Danh sách nghe gồm bản đầu bảng, bản khác nhất, và ở ~30 % id thêm một bản dò | §4.4–4.6 |
| Đổi món | Khoảng cách âm học giữa hai món > độ trải biến thể của cùng món | §1.6; AUDIO_PIPELINE §5.2 |

### 4.2 Bài thử bản trộn (dựng bằng bộ trộn thật trong `OfflineAudioContext`)

| Bài | Kịch bản | Đạt |
|---|---|---|
| A bản trộn | 2–5 phút ở tốc gõ cao nhất (bot 80 WPM), đợt lớn, K2 có hạ thú, có K5 | −18 ±2 LUFS-I, ≤ −1 dBTP, LRA 10–18 LU. K5 cao hơn mức tích hợp 6–10 LU trong cửa sổ ngắn. Combat rõ trên phím |
| C giọng đọc | Từ < 40 độ thuộc được đọc ngay sau K2 và K5 | Ở ca xấu nhất, giọng cao hơn phần còn lại ≥ 10 dB ở 1–4 kHz; anh nghe xác nhận |
| D mật độ | 60 thú; K0, 2 băng K1, K4 và K5 cùng lúc | Không vượt 32/16 tiếng. Ép > 3 dB dưới 5 % thời gian. Không clip. Mỗi dải do đúng nhóm chiếm |
| E mỏi tai | 10 phút, K0 và K1 dày | Không biến thể nào phát hai lần liền. Anh nghe 3 phút từ phút 8, không gắn nhãn "nhàm khi lặp". Sửa bằng đỉnh ngắn và phân tầng, không làm nhỏ |
| G độ trễ | Phím cuối → tiếng phát | ≤ 50 ms |
| H dừng hình | K2 35 ms, K5 70 ms | Âm đúng khung, không khựng |

### 4.3 Thứ tự: lát cắt và demo trước, hàng loạt sau

| Bước | Làm | Cổng để sang bước sau |
|---|---|---|
| 0 | Audio Lab nhận game `immortality-cultivation`: lệnh `firefly ingest` hiện chỉ biết 3 game, cần thêm thẻ `specs/immortality-cultivation/<id>.yaml`. Làm IR hẻm núi | `firefly status` liệt kê đủ id S1 |
| 1 · S1 lát cắt | Clear Wind với họ kiếm: K0, K1, K2, K5 và không gian (25 prompt). Đúng nguyên tắc pilot của audio.md §5.9 (phát thường, phát nặng, trúng, sự kiện lớn, một không gian) | Qua cổng §4.1. Anh nghe mù ≥ 8,5 về lực, độ nảy, không gian và độ hợp game trên Bảng Nghe ("Một mình", "Lặp 20 lần" cho K0 và K1, "Trong trận") |
| 2 · demo | Clip trận 20–30 s trong lab chiêu: sân thật, camera chơi, 60 thú, K0, K1, K2, K5 có tiếng. Tiếng chết lấy từ danh sách thú (phụ thuộc) | Anh xem và nghe. Bài A, C, D, H đạt trên bản dựng offline |
| 3 · đổi món | Thunder Seal (Lôi, khác Clear Wind nhất): 4 prompt, bộ cue nướng và kit; cùng clip | Anh nghe mù đoán đúng món; cổng "Đổi món" ở §4.1 |
| 4 · S2 | K3A, K3B, K4 cho Clear Wind; rồi Winter Vein và Verdant Branch | Như bước 1 |
| 5 · hàng loạt | Đao và thương khi có bộ Đ, T | Như bước 1, sau khi anh chốt hình món |
| Cuối | Gắn vào game | Anh nghe trong bản build trên host chơi, đúng cài đặt người chơi, không cờ URL |

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
| Không dùng luật phím cho combat | audio.md §5.1 | Luật phím chỉ cho `key-*` và `key-word` (§0). Đuôi combat chỉ hạ 2–4 dB ở 1–4 kHz và nhường giọng, không bị cắt. Dòng "Luật giọng đọc" của canon §22 viết chung cho mọi âm: audio.md §5 thắng cho combat; xem việc mở 3 |
| Biến thể | §5.2, §5.7 bước 9 | 3–5 bản cho đầu và thân, ±60 cent lúc chạy; cú trúng và nốt gần cố định. Bảng AUDIO_PIPELINE §5.3 (±150 cent cho trúng nhỏ) là bản cũ, không dùng cho combat |
| Offset lớp | §5.3 | Đầu 0, thân +3, B và C +5, sub +4–6 ms; flam 6 kiếm và đá vụn có offset riêng ghi trong bảng |
| Bậc | §5.4 | Mọi cue nằm trong khoảng của bậc mình. Bed gồng (≤ −24), `appear` và `charge` (−30), vòng lặp K3A và K4 (−22) không phải đòn đánh mà là nền của trạng thái; lực nằm ở đỉnh (đỡ, mở, nhịp). Đây là phân tầng, không phải làm nhỏ đòn |
| Trần tiếng | §5.4; canon §22 | Canon thắng: 32 (Low 16), ≤ 4 lần mỗi 100 ms. Trần nhóm nằm trong khoảng của audio.md: heavy 2, big 1, hit 6, loop 1 mỗi loại, tail 2. Nhóm release là 4 (khoảng 4–6 của bắn nhanh); K0 và K1 bắn dưới 4 lần/s |
| Hạ tiếng P0 | §5.4 | 0,6 trong 8–12 ms, giữ 120–250 ms, về ~300 ms; nhạc −4 đến −6, môi trường −6, phím ≤ −2. Báo đòn không hạ (canon xếp trên chiêu) |
| Giọng đọc | §5.4, AUDIO_PIPELINE §6.2 | Khô ≤ −3 dB; nhạc, đuôi, vang trả về, vòng lặp, bed −6 dB (đề xuất); bắt đầu từ `pronouncer.request` |
| Dải tần | §5.5 | Đuôi 150–250 Hz đến 6–7 kHz. Thân được ở 1–4 kHz trong 80–250 ms. Còi Sky Thread và tiếng ngân Resonant Fang được xử như đuôi |
| Prompt | §5.6, Q6 | Đã đếm từng prompt (≤ 12 từ), đã dò từ cấm của §5.6 và Q6 (§3). Mỗi prompt một lớp. Lớp đầu có "dry", lớp đuôi có "no transient". Không có "bell" (tránh chuông chùa, canon §22) |
| Chuỗi | §5.7 | Có `level=0`, `normalize=0`; không `loudnorm` trên một cú; không `oversample`; OGG không mã bằng ffmpeg Homebrew |
| Mono và stereo | AUDIO_PIPELINE §4.3.1 so với audio.md §5.7 | Khô mono (đúng cổng định dạng L1, game tự pan). Đuôi, bed, vòng lặp và K5 stereo vì cần không gian; ví dụ `-ac 2` của audio.md không bắt buộc cho phần khô |
| Vang | §5.8 | Có cả đuôi nướng và send chung. Send: phát 0,10, trúng 0,05, phát và trúng nặng 0,25, K5 0,40, bed bầy 0,20, đuôi 0. Bậc Low nướng đuôi lúc nạp. Glue chậm, bỏ makeup tự động, không compressor nhanh |
| Nguồn | §5.9 | Firefly trước. CC0 cho lớp đầu dưới 50 ms. Luật dừng tính theo từng id lớp. Lát cắt trước bộ đầy đủ |
| Nghiệm thu | §5.10 | Có đủ ở §4.1–4.3; tai anh là cổng cuối, mốc 8,5 |
| Tick | canon §12.1; `src/sim/skills.ts` | K0 +18; K1 +6/+36/+66; K2 +12; K4 mở +12 rồi nhịp mỗi 30 tick tới +282, đóng +312 (10 nhịp); K5 +30/+75/+120. Tick 60 Hz |
| Không âm tổng hợp | canon D26, §22, D44 | Sub tổng hợp chỉ nướng offline thành một lớp trong file thật. Không có oscillator trong game |

Lỗi đã sửa trong lượt soát:
- **Đuôi K5 nhóm 1 tiếng:** đuôi 2–3 s gối lên nhau khi các loạt cách 0,75 s, nên nhóm `tail-big` lên 2 và đuôi cũ nhất nhường.
- **Phát K5:** rút còn 0,4–0,5 s để xong trước loạt 1 (nhóm big 1 tiếng).
- **Mức residue:** trước đó lệch giữa các cue (−26 và −22), nay thống nhất −24 để file đúng mức của nó.
- **Prompt Resonant Fang:** bỏ chữ "bell".
- **Tiếng bay K0 và K1:** flyby cộng kit `trail` từng là 2 tiếng mỗi kiếm, vượt nhóm travel (3) khi K0 bay cùng băng K1. Nay nướng thành `cue-sword-travel` theo món; `trail` chỉ còn chồng lúc chạy ở K5.
- **Gồng K5:** bed, `charge-air`, kit `charge` và swell là 4 tiếng, vượt nhóm charge (3). Nay `charge-air` trộn sẵn vào `cue-k5-charge-bed`.
- **Đầu loạt K5:** prompt `rain-impact-head` thiếu "dry"; đã thêm.

## 6. Việc mở (cho điều phối)

1. **Hình món chưa chốt:** prompt lớp B và vai riêng ở §1.3 phải soát lại theo tờ anh duyệt. Lớp A, C, S không phụ thuộc hình, nên tạo trước được.
2. **Catalog:** `src/audio/catalog.ts` hiện có một id cho mỗi chiêu (`kiem-zone` là một file 5 s). Spec này tách theo pha và thêm kit theo món, nên cần sửa thẻ, hook và `ART_AUDIO_VFX_PLAN.md` §5.1. Việc này của làn âm, không làm ở phiếu này.
3. **Canon §22, "Luật giọng đọc":** nên ghi rõ phạm vi là `key-*` và âm sau từ, vì audio.md §5 thắng cho combat. Sửa canon là việc của anh.
4. **Mức hạ tiếng dưới giọng đọc:** canon Tu Tiên chưa ghi. Spec đề xuất nhạc, đuôi, vang −6 dB; anh chốt.
5. **Audio Lab:** `firefly ingest` chỉ nhận dragon-hold, typing-defense, typing-survival. Cần thêm `immortality-cultivation` và thẻ spec từng id.
6. **Lab chiêu chưa có đường âm.** Demo bước 2 cần bộ nạp file (kiểu `FileBank`) và harness offline trong lab. Đây là việc mã.
7. **Phụ thuộc:** tiếng chết của lát cắt lấy từ danh sách thú; câu hỏi D55 và D23 (hệ của món có đổi hệ sát thương không) quyết C có tách khỏi B hay không.
8. **Chia 32/16 tiếng** ở §2.3 là đề xuất; bài D chỉnh lại.
