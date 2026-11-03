# Hào quang kiếm bay (sword aura): ba hướng cho anh chọn (03/11/2026)

**Trạng thái:** đề xuất, đã sửa theo một lượt phản biện độc lập cùng ngày (§8). Chưa có mã. Bước tiếp là **bước 0** (§5.0): bảng hình tham chiếu và phác ý tưởng vẽ chồng lên khung chụp thật, gửi anh chọn **trước khi** dựng bằng mã. Chỉ hướng anh chọn mới được dựng. Mọi con số chi phí là ước tính, chưa đo; cổng thật là số đo ở §6.

**Đầu vào** (đã đọc hết):
- Nghiên cứu các thiết kế được yêu thích, mỗi tệp có bảng kiểm nguồn và đánh giá của Claude:
  - [`source/sword-aura-chatgpt-2026-11-03.md`](source/sword-aura-chatgpt-2026-11-03.md): ChatGPT, Chat, thinking High, có lượt tự rà soát;
  - [`source/sword-aura-gemini-2026-11-03.md`](source/sword-aura-gemini-2026-11-03.md): Gemini 4 Argon, mức Cao.
- Kỹ thuật và chi phí: [`source/sword-aura-tech-2026-11-03.md`](source/sword-aura-tech-2026-11-03.md). Tài liệu đó đọc mã, chưa đo; các mục A1–A3, B1–B4, C, D, E dưới đây là của nó.
- Luật:
  - [`ELEMENT_LAYER.md`](ELEMENT_LAYER.md) (D59);
  - [`../00-canon.md`](../00-canon.md) (D54–D59, §21.1 màu dành riêng);
  - [`WEAPON_DESIGN.md`](WEAPON_DESIGN.md) (Clear Wind, §6: "mọi kiếm quang có vòng O và hai rãnh nhập một ở mũi") và [`SKILL_CATALOG_V2.md`](SKILL_CATALOG_V2.md);
  - [`VFX_STANDARD.md`](../../VFX_STANDARD.md) §3;
  - skill [`game-vfx-layered`](../../../../.agents/skills/game-vfx-layered/SKILL.md) và [`game-hero-presence-vfx`](../../../../.agents/skills/game-hero-presence-vfx/SKILL.md).
- Mã chỉ đọc, không sửa: `games/immortality-cultivation`, nhánh hiện tại chiều 03/11 (`2b09491`).
  - Trong `src/view/skills/`: `sword-material.ts`, `real-swords.ts`, `blades.ts`, `fxkit.ts`, `element-kit.ts`, `element-metal.ts`, `element-fire.ts`, `element-stage.ts`, `myriad-swords.ts`, `sword-skills.ts`, `weapons.ts`.
  - Ngoài ra: `src/view/trails.ts`, `src/view/swords.ts`, `src/view/fx.ts`, `src/lab/skills-main.ts`, `src/lab/tassel.ts`, `src/ui/skin.ts`, `src/typing/grading.ts`, `src/view/bench/meter.ts`, `src/content/rules.ts` (`TT_TIERS`, `TT_DYNAMIC_RES`), `src/kit/three/stage.ts`, `art-src/lab/models/weapons/clear-wind-impostor.json`.
  - Changelog: `2026-11-03-lab-real-swords.md`, `2026-11-03-lab-element-fire.md`.

## 0. Tóm tắt

| | **A · Wind-Silk Mantle** | **B · Echo Cascade** | **C · Celestial Regalia** |
|---|---|---|---|
| Ý chính | Kiếm **mặc** một tấm áo khí may đo, ghép từ các mảnh sắc | Tốc độ **hiện hình**: kiếm kéo theo chuỗi kiếm quang (bóng lưỡi) của chính nó | Kiếm là **bảo vật đội vương miện**: ánh sáng dồn vào mũi, vòng ngọc, chắn mây |
| Pitch | Clear Wind wears a tailored mantle of living qi: sharp qi plates lie flush along both edges in flight and shear apart on every cut, part around the jade ring, sew their two hems into a needle past the tip, and pour off the pommel as a tassel-silk tail. | Speed made visible: each sword is chased by flat, hollow sword-light echoes of its blade that hang back in a clean line in flight, fan open on every turn and snap shut into the strike, while a bow wave splits the air ahead of its tip. | Clear Wind flies as a crowned relic: a star at its point, a slow-turning halo standing behind the hollow jade ring, twin tassel-silk streamers off the cloud guard and motes in orbit, the steel left bare inside a jeweller's hairline. |
| Lớp chính | `MantleSheath`, `MantleHull`, `SilkTail`, `MantleHalo` | `BowWave`, `EchoTrail`, `SweepSmear`, `StanceEcho` | `TipStar`, `RingHalo`, `GuardStreamers`, `OrbitMotes`, `HairlineRim`, `WaitMandorla` |
| Dấu Clear Wind (WEAPON_DESIGN §6) | Hai đường may hai mép hội về mũi kim; mép áo cuộn mây ở cổ và đuôi | Đỉnh V của sóng mũi là hai rãnh nhập một | Quầng đóng khung vòng O; hai viền kim hoàn hội ở sao mũi |
| 88 thanh ngoài kiếm chủ | Kiếm giữa có áo; kiếm xa có quầng giải tích trong impostor | Mọi thanh có bóng lưỡi và sóng mũi, nhưng chỉ khi bay ≥ 4 m/s | Chỉ viền kim hoàn, chấm O, sao trên ngọn sóng |
| Fire hết "sắt nung" nhờ | Lưỡi lửa liếm ngoài viền ở kiếm chủ và ≤ 8 kiếm giữa; kiếm giữa khác mặc áo than; kiếm xa viền than | Bóng lưỡi cháy dần về sau; sóng nhiệt ở mũi | Vòng lửa sau vòng ngọc, sao lửa, hai dải lửa |
| Phím 7, High (ước tính) | +0,08–0,17 ms, +2 lệnh vẽ | +0,08–0,16 ms, +3 lệnh vẽ | +0,06–0,13 ms, +3 lệnh vẽ (+4 nếu dải ở pool riêng) |
| Phím 1 (ước tính) | +0,01–0,04 ms | +0,02–0,05 ms | +0,02–0,04 ms |
| Rủi ro chính | Ở 35–60 px đọc thành kiếm béo, mờ; Metal dễ thành viền phát sáng chung chung nếu mảnh và đường may không đọc ra | Bóng đọc thành "thêm kiếm"; khi bay chậm thì gần như trần | Dòng sông 88 thanh vẫn gần như trần, đúng lỗi anh vừa chê |

- **So sánh đủ ở §3.D.** Ý kiến của Claude, để sau bảng so sánh: nghiêng về A, vì A phủ đều nhất ở tầng kiếm giữa và kiếm xa, tức nhắm thẳng câu chê "không có gì quanh kiếm". C rẻ nhất và giữ thép sạch nhất, nhưng gần như trần ở dòng sông. B mạnh nhất lúc rẽ và lúc bổ, nhưng khi bay thẳng thì bóng lùi ra sau đốc, quanh thân kiếm gần như trống.
- **Bước tiếp (§5.0):** bảng hình tham chiếu 6–9 khung cho mỗi hướng, lượt nguồn tiếng Trung, rồi phác ý tưởng A/B/C vẽ chồng lên chính khung chụp camera chơi hiện tại (Metal và Fire, phím 1 và phím 7, cắt 35 và 100 px). Gửi anh chọn. Chỉ hướng được chọn mới được dựng trong lab (§5.3), quay video, rồi hai giám khảo mù chấm.

## 1. Vì sao, và hào quang phải đạt gì

### 1.1 Lời anh và chẩn đoán

Lời anh chiều 03/11, sau khi xem tấm Sword × Fire: "mà vì sao các thanh kiếm đều chưa được xử lý để có hiệu ứng xung quanh thanh kiếm vậy, chứ hiện tại nhìn các thanh kiếm bay kiểu hơi thô, chưa đẹp cho lắm".

Chẩn đoán, ngắn:
- **Sáng 03/11 anh chê kiếm vẽ bằng code.** Lời anh: "bạn có vẻ đang tự style chứ k sử dụng hình ảnh nên hình kiếm đang rất xấu".
  - Lượt kiếm thật vì thế đưa model Clear Wind đã duyệt vào mọi chiêu: lưới đủ 14.728 tam giác, LOD 3.200 tam giác, atlas impostor cho kiếm xa.
  - Cùng lượt đó **bỏ mọi thứ vẽ quanh lưỡi**: thẻ sáng dọc lưỡi, dải "sống" trắng, dải thân sông.
- **Phần còn lại trên thân kiếm đều nằm trong đường viền:**
  - đường mép trắng nóng ≤ 30 % bề ngang lưỡi, phần duy nhất bloom;
  - rim mềm ≤ 0,9;
  - ánh ngọc;
  - chớp khi trúng.
- **Phía sau kiếm chỉ có vệt** (đọc từ mã):
  - Phím 1, kiếm bay: một dải sáng `RibbonPool` rộng 0,14 m (`TrailLook.widthM` của Metal) bắt đầu sau đốc; với Metal thêm một dải lụa màu tua (`startSilk`), một sao lóe nhỏ ở mũi (`twinkle`) và hạt rơi.
  - Phím 1, kiếm chờ sau vai: một tia lóe chạy dọc lưỡi mỗi 0,9 s (`twinkle`).
  - Phím 7, 6 kiếm chủ: một dải `RibbonPool` màu `trailCore`.
  - Phím 7, kiếm giữa và kiếm xa: một tia `BeamPool` một khung sau đốc, rộng `TRAIL_M` 0,14 m × 1,3 → × 0,5, dài 0,45 `L` trên sông, 0,9 `L` khi bổ, 0,6 `L` khi gom (kiếm xa sáng × 0,55).
  - Ở camera chơi, kiếm là một vật kim loại rộng 4–5 px bay trên nền đá. Chưa ai thiết kế một lớp **mặc** cho thanh kiếm thật.
- **Fire đọc như sắt nung:**
  - Ở cả phím 1 lẫn kiếm sông phím 7, dải nhiệt cam của chế độ `furnace` phủ chính mặt lưỡi (`sword-material.ts`, `heatFrom` 0,05). Lửa nằm **trên kim loại**, không liếm ra ngoài.
  - Kiếm sông phím 7 **không có** vỏ lửa: `FireLayers.streamTravel` chỉ vẽ `sheathAt` cho cls 0 (6 kiếm chủ). Vỏ lửa của kiếm sông đã bị bỏ ngay trong lượt Fire, vì ~90 tấm lửa trên sân đọc thành "tấm ván cháy" (changelog Fire, mục "Lựa chọn và lý do").
  - Ở kiếm chủ phím 7 và kiếm phím 1 (móc `SwordHooks.waiting`, `SwordHooks.travel`, `StreamHooks.travel`), vỏ lửa `sheathAt` bị đẩy ra sau lưỡi (`lift = -0.35`) và làm mềm (`blur = 1.8`, `taper = 0.6`), nên chỉ một viền mờ ló ra.

### 1.2 Hào quang phải đạt gì

1. **Thanh kiếm vẫn là Clear Wind thật** và đọc ra chính nó: lưỡi bạc, vòng ngọc rỗng, chắn mây.
   - Kiếm bay không có tua: tua (`src/lab/tassel.ts`) chỉ có ở kiếm cầm tay trong lab. Nhận diện tua trên kiếm bay hiện chỉ là dải lụa màu tua ở phím 1 Metal.
   - Hào quang mặc cho kiếm. Nó không che, không thay, không vẽ lại kiếm.
   - Không có hình thay thế nào vẽ bằng code.
2. **Rực rỡ, sống, sang ở camera chơi**, khi kiếm dài 35–130 px ở 1080p (trung vị ~100 px), và ở cận cảnh D57 (kiếm chủ tới ~600 px).
   - Khẩu vị của anh: anime, donghua, thần thoại; có hào quang, cuốn hút, sang, hiện đại, nhiều chi tiết.
   - Không lấy "như thật" làm đích (D56). Một viền phát sáng chung chung là trượt.
3. **Có ở cả ba tầng**: lưới đủ, LOD, impostor. Phím 7 trên High có 6 + 24 + 64 thanh; dòng sông là chính những thanh kiếm ấy.
4. **Hình của vũ khí, chất của hệ (D59).** Mỗi hướng là một bộ **hình**. Metal, Fire, rồi Water và các hệ sau chỉ cấp **chất** cho bộ hình đó (§4.8).
5. **Vừa ngân sách.** Mốc hiện tại (p95, High, DPR 1, trung vị các lượt): phím 7 săn 10,2–10,5 ms; nhát kết 10,3–10,9 ms, có lượt Fire 11,9 ms (ELEMENT_LAYER §5 ghi chung 10,2–10,9 ms).
   - Metal: hào quang trừ `off` ≤ +0,6 ms lúc săn và ≤ +0,5 ms ở gom và nhát kết (F168–207, chỗ 94 thanh dồn sát nhau, vẽ chồng lớn nhất).
   - Fire: phần Fire hơn Metal (cùng bật hào quang) tính vào trần 0,85 ms của Fire, trong đó thân và vật bay ≤ 0,20 ms (D59).
   - Không cửa sổ nào có trung vị p95 vượt 11,5 ms (§6).
6. **Anh xem mẫu và chọn trước khi dựng thật.** Bước 0 là phác ý tưởng; chỉ hướng anh chọn mới dựng bằng mã. Sau đó hai giám khảo mù chấm, cổng 8,5. Khi cả hai cho ≥ 7, gửi anh một video demo.

### 1.3 Ký hiệu dùng trong tài liệu

| Ký hiệu | Nghĩa | Giá trị |
|---|---|---|
| `L` | Chiều dài kiếm, đốc tới mũi | Phím 7: kiếm chủ 2,8 m khi rời tay, 3,06 m trên sông; kiếm giữa 2,55 m; kiếm xa 2,3 m. Phím 1: ~2,4 m (2,35 × kiếm tay 1,02 m) |
| Lưỡi | Từ `bladeFrom` tới mũi | `WeaponHold.bladeFrom` 0,38 (atlas: `bladeFromU` 0,389), nên lưỡi dài ~0,62 `L`; chắn bắt đầu ở `guardU` 0,311 |
| `W` | Bề ngang lưỡi chỗ rộng nhất | Đọc từ bảng nửa bề ngang `half[]` của `edgeField` lúc nạp. Ước tính ~4,5 % `L`: 0,14 m kiếm chủ, 0,115 m kiếm giữa, 0,10 m kiếm xa, 4–5 px ở 100 px |
| `px` | Điểm ảnh **CSS** ở 1080p | Ở 100 px, 1 px ≈ 0,025–0,031 m. Trong shader, mọi sàn tính bằng px CSS × `uDpr` (High và Ultra trôi DPR 1–2 theo `TT_DYNAMIC_RES`), không bằng `fwidth` thô |
| `f` | Khung ở 60 Hz | Mọi nhịp chạy theo giây thế giới; số khung chỉ để đọc |
| `ω` | Tốc độ góc của hướng kiếm (rad/s) | "Rẽ" khi ω ≥ 4, đầy khi ω ≥ 10 |
| `v` | Tốc độ bay (m/s) | Sông phím 7 khoảng 15–25 m/s |
| `core` | Lõi HDR mảnh | 2,4–3,6 (như `EDGE_HOT` 3,6); ≤ 1 px ở camera chơi, ≤ 3 px cận cảnh. Phần duy nhất được bloom; đỉnh HDR chỉ ở f0–2 (VFX_STANDARD §3.4) |
| `glow` | Thân sáng | ≤ 0,85 mỗi kênh trước tone map (luật ≤ 0,9, chừa 0,05) |
| `ink` | Lớp tối premultiplied | rgb tối, alpha 0,25–0,85, nằm trong cùng shader với phần sáng |

Màu đều là tuyến tính, trừ chỗ ghi mã hex sRGB. Sắc (hue) của mã hex tính trên sRGB.

## 2. Học được gì từ các thiết kế được yêu thích

### 2.1 Các lớp lặp lại

ChatGPT và Gemini đưa ra cùng một chồng lớp. **Đây không phải bằng chứng độc lập:** đề bài gửi cả hai (mục A của tệp nguồn) đã liệt kê sẵn các lớp (sheath, edge light, afterimages, streamers, motes, tip star…) và luật lớp tối, lõi HDR. Bảng dưới chỉ là thứ tự ưu tiên hai bên cùng đưa ra trong khung đó.

| Thứ tự | Lớp | Ở 35 px | Ghi chú |
|---|---|---|---|
| 1 | Kiếm thật, đục | Còn | Nhận diện: lưỡi, vòng ngọc, chắn mây |
| 2 | Lớp tối đỡ phía sau | Còn | Tách kiếm khỏi nền đá sáng; nằm trong shader của lớp sáng |
| 3 | Vỏ khí theo hệ (≤ 0,9) | Còn | Hình chính của hào quang |
| 4 | Lõi HDR mảnh | Còn | Phần duy nhất bloom |
| 5 | Sao hoặc kim ở mũi | Còn | Cho biết hướng |
| 6 | Đuôi hoặc vây theo tốc độ | Còn | Cho biết tốc độ |
| 7 | Nhịp lóe ở vòng ngọc, dải lụa, tàn ảnh khi rẽ | Mất | Chỉ cho kiếm chủ, từ ~70 px |
| 8 | Hạt, bùa văn, vòng nhỏ, méo không khí | Mất | Thành nhiễu dưới ~90 px |

Ở 35 px chỉ còn sáu điều: có một thanh kiếm thật, một viền tối, một bóng hào quang, một đường sáng mảnh, một mũi rõ, một đuôi cho biết tốc độ (ChatGPT §5).

### 2.2 Vì sao người xem thích

- **Kiếm vẫn là kiếm.**
  - Bản beta của Qingxiao (Wuthering Waves) bị chê là kiếm "less physical and very transparent and overdone, so they all meld together". **Reddit, chưa kiểm** (ChatGPT đưa; Reddit bị chặn trong môi trường này). Chỉ dùng làm gợi ý.
  - Qingxiao có thật: Resonator Aero dùng kiếm, ra ở bản 3.6; bản 3.7 nhắc trạng thái "Sword Flight". Claude đã kiểm trên trang của Kuro.
  - Ý này trùng luật của anh: hào quang không được nuốt thanh kiếm.
- **Nhỏ thì tinh, to thì dễ rẻ.** Một bài review Sword of Coming (**Reddit, chưa kiểm**):
  - khen tàn ảnh và sóng năng lượng tinh tế ở cỡ nhỏ;
  - chê các đòn mưa kiếm năng lượng cỡ lớn là "especially lacklustre".
  - Bài học: không nhân một lớp sáng lên 94 thanh rồi gọi là giàu.
- **Có thứ bậc, cả trong không gian lẫn thời gian.**
  - Wuchen (Naraka): câu "enduring sword rain" của tuyệt kỹ Blade Storm Claude đã kiểm trên trang chính thức.
  - Nhịp "xen kiếm nhỏ với kiếm lớn" của đòn đó là quan sát của người chơi trên Reddit (**chưa kiểm**).
  - Vài kiếm dẫn đầu đủ chi tiết, phần còn lại bơi theo.
  - ChatGPT thêm một luật hay: 6 kiếm chủ thỉnh thoảng phải "chứng minh" cả dòng là Clear Wind, bằng một lần ngọc lóe.
- **Ngôn ngữ ngọc, mây, sáng tối.** Bài Developer Insight về Xiao (Genshin, Claude đã đọc) nói ngọc cho cảm giác trường thọ, vải có hoa văn mây cho vẻ cổ, và sáng tối đan nhau trong đòn đánh. Clear Wind có đúng vòng ngọc, chắn mây và tua.
- **Kiềm chế để đọc được.** Trang VFX của Riot (Claude đã kiểm) nói nghệ sĩ mang "heavy burden of restraint": hiệu ứng phải đẹp mà vẫn rõ đòn của ai.
- **Còn thiếu:** phần "được yêu thích" ở trên chủ yếu là lời fan chưa kiểm.
  - Lượt nguồn tiếng Trung đã chạy ngày 03/11 (§2.7). Nó thêm nguồn của người làm nghề đã kiểm, nhưng vẫn chưa có lời người chơi kiểm được nói riêng về hình kiếm bay: NGA và 巴哈姆特 chặn, Zhihu không có trong chỉ mục.
  - Bảng hình 9 khung mỗi hướng đã làm ngày 03/11, chỉ từ kênh chính thức đã kiểm (Qingxiao 3.6, Yanqing, Wuchen, Phàm Nhân Tu Tiên của Made By Bilibili): `games/immortality-cultivation/tmp/shots/sword-aura/concept/board/board-a.jpg`, `board-b.jpg`, `board-c.jpg`, nguồn từng khung trong `board-sources.md` cùng thư mục (không vào Git).
  - Còn phác ý tưởng vẽ chồng lên khung chụp thật (§5.0 mục 3–4) trước khi gửi anh.

### 2.3 Hai bên cùng đồng ý (nên lấy)

- **Mỗi kiếm chỉ một mặt trong suốt ở mỗi điểm ảnh.** Lớp tối, thân, lõi là ba vùng của cùng một shader, trộn premultiplied (`ONE, ONE_MINUS_SRC_ALPHA`). Không chồng ba tấm.
- **Mỗi tầng một cách vẽ:**
  - kiếm chủ có vỏ lưới và phụ kiện;
  - kiếm giữa có vỏ instanced;
  - kiếm xa có một quad mang mọi vùng.
- **Màu theo hệ lấy từ một dải màu (ramp hoặc LUT).** Khớp với "Element ramp atlas" của `ELEMENT_LAYER.md` §3.
- **Theo pha:**
  - phát chiêu sáng ngay khung 0, vỏ mở từ chắn kiếm ra mũi;
  - bay đều là pha yên nhất;
  - **độ cong** của đường bay quyết định độ giàu, không phải tốc độ;
  - lúc chém thì vỏ co lại, lõi vọt lên, rồi mới loang ra;
  - lúc về không phát ngược lúc phóng.

### 2.4 Chỗ tôi không đồng ý

**Với ChatGPT:**
- **Fire của River-Silk Sheath** là "lụa hổ phách, mép sau bị bào nhọn, cứng gần lưỡi". Ở 35–130 px tả như vậy sẽ lặp lại đúng lỗi sắt nung. Lửa phải vượt ra ngoài đường viền và có đầu lưỡi lửa sắc (§3.A).
- **Calligraphy Wake** (nét mực tối, kiếm làm ngòi bút) rõ ở xa, nhưng:
  - đi ngược khẩu vị "rực sáng, có hào quang" của anh;
  - trên nền tối thành vệt bẩn;
  - mực là motif quá phổ biến (Gemini cũng nghĩ ra nó).
  Tôi không lấy làm hướng.
- **Jade Meridian Lattice** chỉ đẹp ở cận cảnh. Camera mình phần lớn thời gian chỉ thấy kiếm 35–130 px, nên các "đường kinh mạch" gộp lại còn một viền. Phần đáng giữ của nó (đóng khung vòng ngọc) đi vào hướng C.
- **4–8 ribbon cấp cả dòng sông:** sáng 03/11 anh vừa thấy dải "thân sông" bị bỏ vì là hình tự vẽ. Dựng lại một dải chạy dọc dòng sông dễ chạm đúng lời chê đó. Không hướng nào dưới đây có dải cấp dòng.
- **Độ sáng lõi 1,3–2,1:** quy ước của mình là lõi mảnh 2,4–3,6 (như `EDGE_HOT`), nhưng ≤ 1 px. Đây chỉ là chênh số, không đổi ý.
- **Depth fade bằng kết cấu độ sâu cảnh:** composer chưa có kết cấu độ sâu. Mặt đất phẳng, nên dùng hạt mềm giải tích với y = 0 (`vxSoftGround`).
- ChatGPT tự rút một câu về bài 80.lv của Matt Schwartz. Claude đã kiểm: câu đó vốn đúng.

**Với Gemini:**
- **26–28 ribbon sống** gần chạm trần 32 của High, không chừa chỗ cho va chạm, đất, thú.
- **Vỏ tách đôi chỉ bám hai mép vát, để trần sống lưỡi:** ở 4–5 px bề ngang, hai mép vát chỉ là một điểm ảnh. Không đọc được.
- **Bùa văn trên vòng ngọc ở 0,75–0,9** không đọc được dưới ~90 px. Chỉ cho kiếm chủ, khi kiếm lớn.
- **Vây chữ V che ~35 % mép lưỡi** (Dragon-Scale Wake), trái luật không che kiếm. Ý đồng pha cho cả dòng lại rất hay, nên hướng B lấy nó dưới dạng sóng mũi **tách khỏi** đường viền.
- **Nguồn yếu:**
  - nhiều câu dựa vào wiki fandom;
  - một chuỗi Reddit của game khác được dẫn cho Sword Flight, ghi sai là bản 3.5;
  - con số "7 tỷ lượt xem" của RMJI không có trong nguồn dẫn;
  - câu "Genshin luôn có viền mực sau lưỡi sáng" là ý kiến, không có nguồn.
- **Atlas impostor theo kênh ngữ nghĩa** là ý hay, nhưng không cần: quầng kiếm xa tính bằng giải tích từ bảng bề ngang lưỡi (§5.2), atlas màu đã duyệt giữ nguyên.

### 2.5 Cả hai cùng thiếu, và tài liệu này lấp thế nào

| Thiếu | Ở đây |
|---|---|
| Lửa phải **liếm**, không như sắt nung | Mỗi hướng có cách riêng để lửa vượt ra ngoài viền kiếm, chia tầng để dòng sông không thành "tấm ván cháy" (§3); đề xuất bớt dải nhiệt trên mặt lưỡi (Q3) |
| Gắn với việc gõ | Kiếm chờ lớn hào quang theo ba bậc của mức gõ; hạng `perfect`/`flash` của từ cho một nhịp lóe ở vòng ngọc (§4.9) |
| Phép thử chữ gõ vẫn đọc được | Cổng ở §6 |
| Phép thử kiếm vẫn đọc được | Đo phần điểm ảnh lưỡi, vòng ngọc, chắn giữ màu bằng mặt nạ hình học (§6) |
| Cách anh duyệt | Bước 0: bảng hình và phác ý tưởng chồng lên khung chụp thật; sau khi chọn: video và tấm ảnh ở 35, 70, 130 px, nền sáng, nền tối, ảnh xám, Low không bloom (§5) |
| Nguồn tiếng Trung (Bilibili, Zhihu, GameRes, UOD) | Đã chạy ngày 03/11 ở bước 0 (§2.7, [`source/sword-aura-chinese-2026-11-03.md`](source/sword-aura-chinese-2026-11-03.md)): GameRes, báo chí, Bilibili, TapTap, trang chính thức đã kiểm; Zhihu, NGA, 巴哈姆特 không đọc được |

### 2.6 Chọn ba hướng nào, và vì sao

Ba hướng phải khác nhau ở **ý**, không chỉ ở màu:
- **A mặc lên bề mặt:** một tấm áo quanh lưỡi, ghép từ các mảnh.
- **B dùng thời gian:** quá khứ của đường bay hiện ra.
- **C dùng điểm nhấn:** ánh sáng dồn vào vài "trạm" như đồ trang sức.

| Hướng | Lấy cảm hứng từ | Phần riêng của mình |
|---|---|---|
| A · Wind-Silk Mantle | River-Silk Sheath (ChatGPT) | Áo may từ chính bảng bề ngang đo được của lưỡi; mảnh khí sắc xếp thẳng khi bay, trượt cắt khi bổ ("align → shear"); hai đường may hội về mũi kim; khe cổ áo để trần vòng ngọc, mép áo cuộn mây; đuôi lụa màu tua; lửa liếm ra ngoài viền |
| B · Echo Cascade | Tàn ảnh bậc thang (Gemini), vệt chữ V (Gemini); lời khen tàn ảnh của Sword of Coming (Reddit, chưa kiểm) | Bóng chỉ là lưỡi (kiếm quang, không phải thêm kiếm), rỗng tâm, màu phẳng, cách kiếm thật một khoảng; "bóng tư thế" để lại chỗ phóng; sóng mũi tách khỏi viền, nên 94 sóng mũi tự thành vảy chữ V của cả dòng mà không cần dải cấp dòng |
| C · Celestial Regalia | Sovereign Halos (Gemini), đóng khung ngọc (ChatGPT, Lattice) | Quầng tròn sau vòng ngọc rỗng, dấu chữ ký của Clear Wind (WEAPON_DESIGN §6); dải lụa đôi từ hai mút chắn mây thay cho dải lụa đơn; vầng mandorla khi kiếm chờ sau vai, đúng bộ radiance anh muốn |

Không lấy:
- **Calligraphy Wake / Calligraphic Slipstream:** mực làm ý chính, lý do ở §2.4.
- **Jade Meridian Lattice:** không đọc được ở camera chơi.
- **Dragon-Scale Wake** như một hướng riêng: che mép lưỡi.

Không hướng nào chép hình chữ ký của một game cụ thể:
- không dùng bố trí kiếm hay biểu tượng Heart Sword của Qingxiao;
- không dùng bố cục tuyệt kỹ của Yanqing;
- không dùng nhịp mưa kiếm của Wuchen;
- không dùng chữ Hán hay chữ thư pháp của ai.

### 2.7 Nguồn tiếng Trung thêm gì (03/11/2026)

Nguồn: [`source/sword-aura-chinese-2026-11-03.md`](source/sword-aura-chinese-2026-11-03.md) (ChatGPT Chat, thinking High, có tự rà soát; Gemini 4 Argon; Claude kiểm từng nguồn ở mục G, đánh giá ở mục H).

**Thêm, đã kiểm:**
- **Hình trước, sáng sau.** Bốn nguồn nói cùng một ý:
  - đạo diễn mỹ thuật 《仙逆》: chiêu đi từ "quang hiệu đơn thuần" sang vật có hình, tránh pháp trận sáng diện rộng;
  - họa sĩ 《逆水寒》: gió, khí, đao quang phải quy về hình học có đường viền và hướng, hạt vụn khó lên hình;
  - 网易雷火: "特效并不是无脑加一些发光的效果就可以";
  - 《剑来》: kiếm khí thủy mặc là cách 化繁为简.
  Điều này củng cố luật "không viền phát sáng chung chung" (§1.2) và ý mảnh có hình của A.
- **Lớp tối rộng, tắt chậm dưới lớp sáng mảnh, tắt nhanh** (NEXT Studios; một blog học tập thêm: lớp đen tắt sau cùng). Khớp lớp mực và lõi HDR của mình. Điều mới là **thứ tự tắt**: mực ở lại sau lõi.
- **Nhịp là chuẩn số một** của chất lượng hiệu ứng, và màu phong phú không có nghĩa là nhiều màu (网易游戏学堂). Củng cố §2.3: bay đều là pha yên nhất, sự kiện mới sáng.
- **Vạn kiếm khác nhau từng thanh:** cảnh 万剑归宗 của phim 《风云Ⅱ》 điều khiển tốc độ, hướng, cảm giác nặng của từng thanh. Gợi ý cho dòng sông 94 thanh.
- **Người chơi đòi thứ bậc, không đòi ít hiệu ứng hơn.** Lời chê "光污染", "特效太花" kiểm được đều ở game khác, và có người chơi "不想关闭特效影响爽感". Không có lời khen hay chê nào kiểm được nói riêng về hình kiếm bay.
- **Neo văn hóa** để trình bày với anh: 剑影分光术 (kiếm quang hóa thành bóng kiếm), 剑丝 của 大庚剑阵, và cặp "thân kiếm trầm, uy nghiêm" với "kiếm khí rực rỡ" làm nền cho nhau trong lời quảng cáo của NetEase.

**Mâu thuẫn, hoặc cần dè chừng:**
- Trong truyện, bóng của 剑影分光 giống hệt phi kiếm. B vẫn giữ "bóng chỉ là lưỡi", để không đọc thành thêm kiếm.
- Cả hai công cụ đề nghị ghép A (nhận diện), B (chuyển động), C (thứ bậc). Đó là suy luận của chúng từ một đề bài đã liệt kê ba hướng, không phải nguồn. Quy trình giữ nguyên: anh chọn một hướng; mượn lớp của hướng khác chỉ sau khi hướng đó đạt (§3.D).
- Lời quảng cáo kiếm bay của Trung Quốc hay dùng vàng; Metal của mình không có vàng (§4.4).
- Không có nguồn tiếng Trung riêng cho "lửa liếm quanh lưỡi, không như sắt nung". Phần Fire vẫn dựa trên luật lửa chung (vài nhóm lưỡi lửa, tia lửa, lớp tối tắt sau cùng) và chẩn đoán ở §1.1.

**Đề xuất (chưa áp vào §3; chỉ xét cho hướng anh chọn):**

| Hướng | Đề xuất 1 | Đề xuất 2 |
|---|---|---|
| A | **Khe mực 1 px giữa mép thép và áo** (mực ở mép trong, thêm vào viền mực ngoài sẵn có), để ở 35–60 px áo không nhập vào lưỡi thành "kiếm béo", tức rủi ro chính của A. Gemini đề xuất; khớp lớp tối tách lớp sáng của NEXT | **Mảnh không đều, nhạt dần về cổ áo:** mỗi bên 2–3 mảnh lớn nhỏ khác nhau thay cho 4 mảnh đều, khe là khoảng trống thật; thân áo đặc ở mũi, tan thành sợi về phía chắn. ChatGPT và Gemini; khớp "quy về hình học" của 逆水寒 |
| B | **Sóng mũi là sự kiện:** chỉ hiện khi tăng tốc, rẽ vào và bổ (vài khung), không thường trực khi bay đều. ChatGPT; khớp "nhịp là chuẩn số một" | **Bóng nguội dần cả sắc lẫn độ sáng**, không chỉ alpha: bóng 1 có viền sáng mảnh, bóng 2–3 chuyển chàm tối có mực, để mắt tách kiếm thật với bóng. Gemini |
| C | **Sao mũi thành tia lóe theo trục kiếm**, đỉnh sáng chỉ ở phóng và trúng; hạt quỹ đạo chỉ khi chờ và bay chậm. Bớt rủi ro "lấp lánh rẻ tiền" (§3.C). Cả hai công cụ | **Quầng là "vòng ngọc vọng" có khuyết:** 2–3 cung hở rõ, lòng trong suốt, để vòng ngọc thật luôn thắng. ChatGPT |

Cho cả ba (đề xuất): lớp mực tắt sau lõi sáng khi tan; ở dòng sông, lệch pha nhỏ theo từng thanh cho nhịp hào quang (thở, lấp lánh, độ dài vệt), để dòng không "xếp hàng".

## 3. Ba hướng

Chung cho cả ba (chi tiết ở §4):
- Mỗi lớp là một module, có `enabled` và `intensity`, và ghi rõ bản giảm chuyển động: tắt, làm dịu hay giữ (VFX_STANDARD §3.8).
- Tối và sáng nằm trong cùng một shader, trộn premultiplied.
- Có mức sàn bề ngang theo px CSS.
- Chạy theo thời gian thế giới; không cấp phát mỗi khung; biên dịch sẵn trong `prewarm`.
- Không lớp nào cộng sáng lên mặt lưỡi, và không lớp nào đổi đường mép sẵn có. Đường mép trắng nóng nằm **trong** đường viền và giữ nguyên.
- Mỗi hướng **thay** một số lớp vệt đang có, không chồng thêm. Bảng thay ở §4.6.
- Mỗi hướng mang dấu Clear Wind của WEAPON_DESIGN §6: vòng O và hai rãnh nhập một ở mũi.

Chiêu dùng để làm mẫu, như kế hoạch Fire:
- **Phím 1, Threefold Sword Command (`k1`):** ba thanh hiện sau vai ở mức gõ 0,15 / 0,45 / 0,75, rời vai trước các mốc trúng +6, +36, +66.
- **Phím 7, Myriad Swords (`myriad-swords.ts`):**
  - F0: kiếm chủ rời tay;
  - F4–30: kiếm mọc lên từ sân;
  - F30–168: săn;
  - F168–192: gom kiếm;
  - F192: nhát kết;
  - F192–207: dòng kiếm gấp lại.
- Hướng anh chọn sau đó mới áp cho K0–K5 và thiên kiếm.

Các trạng thái dùng ở mọi bảng:

| Trạng thái | Phím 1 | Phím 7 | Pha VFX |
|---|---|---|---|
| Chờ | Ba thanh lơ lửng sau vai lúc gõ | Kiếm mọc lên (`S_SEED`); vầng K5 khi gõ | A (gồng) |
| Phóng | Thanh rời vai | F0 kiếm chủ rời tay; kiếm sông hiện ra | R |
| Bay đều | Đường bay về thú | `S_RIVER`, năm làn bện | T |
| Rẽ | Vòng cung tìm mục tiêu | `S_DIVE` theo đường cong, xoắn lúc `S_GATHER` | T |
| Bổ, trúng | Trúng thú | `impactAt`, kiếm chủ bổ xuống | I |
| Về, tan | Tan vào ánh sáng sau khi trúng | `S_FADE`, `S_WOUND`, ngược dòng, gấp lại F192–207, tan vào nhát kết | F |

### 3.A Wind-Silk Mantle

**Pitch:** Clear Wind wears a tailored mantle of living qi: sharp qi plates lie flush along both edges in flight and shear apart on every cut, part around the jade ring, sew their two hems into a needle past the tip, and pour off the pommel as a tassel-silk tail.

**Ý:** một tấm áo khí may đo theo đúng thanh kiếm, như giáp lụa của một bảo vật đang bay.
- Áo bắt đầu ngay **ngoài** mép lưỡi, nên mặt lưỡi luôn trần.
- **Áo ghép từ mảnh, không liền.** Mỗi bên 4 mảnh khí sắc (Low và Medium: 3), so le nửa mảnh giữa hai bên, đầu trước vát chữ V.
  - Khi bay đều, các mảnh xếp thẳng hàng thành một vỏ, giữa các mảnh có khe 1 px (từ 70 px).
  - Khi rẽ, bổ, trúng, các mảnh **trượt cắt** dọc lưỡi và hé ra ngoài, như vảy giáp hay lông vũ.
  - Đây là dấu hiệu "align → shear" của A, đọc được ở 70–130 px. Nó làm áo khác một viền phát sáng chung chung.
- **Hai đường may sáng** chạy ở mép ngoài áo hai bên, hội về một mũi kim vượt quá mũi kiếm: đúng motif "hai rãnh nhập một ở mũi" của Clear Wind.
- Áo hở ở "cổ áo", nên vòng ngọc và chắn mây nằm trong khoảng trống. **Mép áo ở khe cổ và ở cuối đuôi cuộn hình mây**, lặp lại chắn mây.
- Phía sau, đuôi lụa màu tua (`SilkTail`) **thay** dải sáng.
- Thân áo dùng một texture vệt khí vẽ tay hoặc một flow map, làm qua `game-art-pipeline` và anh duyệt mẫu. Nhiễu chỉ dùng để ăn mòn, không làm thân. Như vậy thân áo là hình vẽ có chủ đích, không phải "tự style" bằng nhiễu.
- Mỗi hệ đổi chất của tấm áo: khí (Metal), lưỡi lửa (Fire), ống nước (Water).

**Nhìn nhanh** (nhìn ngang, mũi bên phải):

```
   silk tail (tassel colours)   cloud-curl hem   plates: flush in flight, shear apart on a cut        two seams meet
  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~@(O){  <:::::|<:::::|<:::::|<:::::::.                                      in a needle
                               (O){ ====================== real blade ======================>  - - - -
                               (O){    <:::::|<:::::|<:::::|<::::::'
                          ring + cloud guard: bare
```

| Cỡ trên màn | Thấy gì |
|---|---|
| 35 px | Thanh kiếm, mỗi bên 2 px áo sáng (các khe mảnh nhập lại), viền mực 1 px, một mũi kim ngắn, một đuôi ngắn. Đọc thành "kiếm đang tỏa khí", không thành ống sáng |
| 100 px | Mảnh áo so le có khe, hai đường may hội ở mũi kim, khe cổ áo quanh vòng ngọc, mép mây, đuôi lụa. Khi bổ thấy các mảnh trượt ra |
| Cận cảnh | Thêm vệt khí vẽ tay chảy trong từng mảnh, viền vỏ ngược ôm khối 3D ở kiếm chủ, đuôi lụa phấp phới |

**Các lớp:**

| Lớp | Tầng | Hình và cỡ | Ánh sáng | Trộn | Bloom | Giảm chuyển động |
|---|---|---|---|---|---|---|
| `MantleSheath` (A1 `SheathCard`) | Kiếm chủ, kiếm giữa | Thẻ instanced dọc trục lưỡi, từ `bladeFrom` + 0,03 `L` tới mũi + 0,12 `L`; kiếm giữa thêm đuôi áo 0,35 `L` sau đốc (0,6 `L` khi bổ). Khoảng cách tới mép `d = \|x\| − w(y)`, `w(y)` đọc từ bảng `half[]` 96 mẫu. Nửa bề ngang áo `m(y) = 0,55 W · p(y)`: `p(y)` bằng 0 ở cổ áo, lên 1 sau 20 % lưỡi, xuống 0,7 gần mũi, rồi thành mũi kim dài 0,12 `L`. Mảnh: 4 mỗi bên, dài (lưỡi / 4) × 1,15, bên phải lệch nửa mảnh, đầu trước vát chữ V dài 1,5 bề ngang mảnh, khe 1 px (tắt dưới 50 px). Trượt cắt: mảnh thứ k lệch dọc trục `shear · k · 0,06 L` và nghiêng ra 6°. Sàn 2 px mỗi bên lúc bay đều, 3 px lúc phóng và trúng. Không có thân áo trong dải chắn kiếm | Ba vùng trong một shader: (1) đường may `d` < 1 px ở mép ngoài, glow 0,85, chỉ thành core 2,4 ở f0–2 lúc phóng và lúc trúng; (2) thân glow ≤ 0,85, texture vệt khí cuộn từ mũi về đốc; (3) viền mực ở 30 % ngoài cùng, rgb của hệ, alpha theo `ink.alpha` | Premultiplied; đẩy sau lưỡi 0,08 m theo độ sâu; mềm với mặt đất 0,15 m | Chỉ đường may, chỉ f0–2 | Làm dịu: dòng × 0,3, không thở, trượt cắt × 0,3, đỉnh đường may × 0,6 |
| `MantleHull` (A2 `AuraHull`) | Kiếm chủ, High và Ultra | Vỏ ngược phồng 1,5 px + 0,015 m theo pháp tuyến đã làm mượt; chỉ phủ lưỡi, không phủ chắn. Vỏ là một lưới vô hình 200–600 tam giác dựng trong Blender, chỉ bọc lưỡi. Nếu không đạt thì tính pháp tuyến mượt lúc nạp vào một thuộc tính mới của LOD (hiện chưa có thuộc tính nào như vậy) | Cùng hàm chất với A1 (mảnh và đường may chiếu lên vỏ) | Vẽ mặt sau, `depthWrite` tắt | Không | Giữ |
| `SilkTail` | Kiếm chủ phím 7, kiếm bay phím 1 | Dải `RibbonPool` từ sau đốc, **thay** dải sáng (và ở phím 1 thay luôn dải lụa sẵn có: một dải thay hai). Dài 0,9 `L` ở phím 1, 0,6 `L` ở kiếm chủ phím 7. Rộng 0,11 → 0,16 m (ở 25 %) → 0,03 m. Rung theo `pushSilk` sẵn có: sin(t·15), sin(t·23), cos(t·11) rad/s (≈ 2,4 / 3,7 / 1,75 Hz) | Metal: thân lụa `silkLight` (`#A9C4EA` × 0,7) pha 30 % thân của hệ, ≤ 0,7, alpha thật 0,85; mép tối `silkDeep` (`#2E3A78` × 0,55) alpha thật. Fire: chính dải lửa sẵn có (chất lửa, không có lụa) | Chương trình premultiplied của `RibbonPool` với chế độ theo từng dải (§5.2) | Không | Làm dịu: ngắn 0,6×, không rung |
| `MantleHalo` (A3 `ImpostorHalo`) | Kiếm xa | Trong shader impostor, **tính giải tích**: khoảng cách tới đường viền lấy từ `AuraAnchors.profile` (`DataTexture` 96 × 1) theo trục của quad, nhân hệ số bề ngang của hàng lăn (`rollWidth`, thêm vào meta). Áo 2 px CSS, viền mực 1 px; mảnh và khe không có (quá nhỏ); mũi kim 0,08 `L` khi kiếm ≥ 60 px, dưới đó không có. Lề quad nới thêm khi trọng số hào quang > 0. Tia `BeamPool` sau đốc giữ, tô màu lụa (thay kiểu, không thêm) | Như A1, không nhân `SWORD_LIGHT` | Trên quad impostor đã nới lề | Không | Giữ |

- Ở kiếm chủ, thẻ và vỏ thay chỗ nhau theo góc nhìn:
  - trọng số thẻ = `smoothstep(0.85, 0.6, |dir·view|)`; vỏ lấy phần còn lại;
  - khi kiếm chĩa vào camera, tấm phẳng không lộ ra và hai lớp không chồng nhau.

**Theo trạng thái:**

| Trạng thái | Áo làm gì |
|---|---|
| Chờ | Bề ngang theo mức gõ ba bậc: 0,4 / 0,7 / 1,0. Thở chu kỳ 2,4 s, ±8 %. Dòng chậm, 0,15 `L`/s, theo luật của hệ (Fire bốc lên theo trục thế giới). Mảnh xếp thẳng |
| Phóng | Mảnh mở lần lượt từ cổ tới mũi trong 4 khung; f0 đã có mảnh đầu sáng đủ. Đường may core 2,4 ở f0–2, về glow ≤ 0,85 từ f3. Bề ngang vọt 1,3× rồi lắng về 1,0 ở f18 |
| Bay đều | Bề ngang 1,0, mảnh thẳng hàng (`shear` 0). Dòng chảy 0,6 + 0,04 `v` chiều dài lưỡi mỗi giây. Đuôi lụa duỗi |
| Rẽ | Bên ngoài đường cong nở tới 1,6×, bên trong co 0,7×. Mảnh bên ngoài trượt (`shear` 0,5). Đuôi lụa quất theo quán tính sẵn có |
| Bổ, trúng | f0–2: áo co về 0,5×, đường may core 3,0 (1 px). f3–13: mảnh trượt cắt hết cỡ (`shear` 1) và bung 1,4×, rồi bị nhiễu ăn mòn. Nếu thanh kiếm còn bay tiếp, mảnh xếp lại trong 12 khung |
| Về, tan | Áo tan **trước** lưỡi: cùng ngưỡng nhiễu với `iFx.z`, sớm hơn 0,15. Dòng chảy đảo chiều về vòng ngọc. Đuôi lụa tắt sau cùng: 0,32 s ở phím 1 (như `ribbons.stop(f.silk, 0.32)` hiện tại), 0,12–0,2 s ở kiếm chủ phím 7 (như hiện tại) |

**Theo tầng hiển thị:**

| Tầng | Có |
|---|---|
| Lưới đủ (kiếm chủ) | `MantleSheath` + `MantleHull` (đổi theo góc) + `SilkTail` |
| LOD (kiếm giữa) | `MantleSheath`, đuôi áo nằm luôn trong thẻ, thay tia sau đốc |
| Impostor (kiếm xa) | `MantleHalo` giải tích trong shader impostor; tia sau đốc tô màu lụa |

**Theo bậc đồ họa:**

| Bậc | Có |
|---|---|
| Low (không bloom, vẽ thẳng ra màn) | `MantleSheath` cho kiếm chủ và kiếm giữa, 3 mảnh mỗi bên, texture vệt khí một lớp. Kiếm xa: `MantleHalo` không có mũi kim. Không có vỏ ngược. Đuôi lụa chỉ ở phím 1. Phải đọc được khi không bloom: đường may glow 0,85 + viền mực |
| Medium (có bloom) | 3 mảnh mỗi bên, hai lớp vệt khí. Đuôi lụa cho mọi kiếm chủ |
| High | 4 mảnh mỗi bên; thêm `MantleHull` cho kiếm chủ |
| Ultra | Thêm lớp vệt khí thứ ba; vỏ ngược cho thiên kiếm và kiếm chờ K1; kẹp trước `pow` cho MSAA |

**Chất theo hệ:**
- **Metal** (`mode: "qi"`), làm ngay:
  - thân bạc lam `[0.30, 0.62, 0.85]`, sắc ~200°, xa màu gõ `#7FF5E0` (169°);
  - mảnh sắc mép cứng 0,7, vệt khí thẳng song song lưỡi, không gợn (`curl` 0);
  - mực chàm `[0.020, 0.028, 0.060]`, alpha 0,35;
  - lõi là lõi Metal `[0.62, 0.88, 1.0]` × 3,0.
  - Không vàng, không ngọc bích, không bạc hà, như `METAL_STREAM`.
  - Cảm giác: rèn và kiềm chế, có trật tự mảnh giáp, không phải "đũa nhựa phát sáng".
- **Fire** (`mode: "flame"`), làm ngay, **chia tầng** để dòng sông không thành "tấm ván cháy":
  - **Kiếm chủ phím 7 và kiếm phím 1:** mảnh áo thành gốc của **lưỡi lửa liếm ra ngoài viền**. Gốc dày 0,5 `W`, lưỡi lửa vươn thêm tới 1,6 `W` (`reachW`), tổng ~2 `W` từ mép ở giữa lưỡi (~9 px ở 100 px). Sàn: đầu lửa vượt viền ≥ 3 px ở 35 px.
  - **Kiếm giữa:** "áo than hồng": mực bồ hóng + đường may nóng chảy ≤ 1 px, không lưỡi lửa. Lưỡi lửa chỉ bật khi kiếm đang bổ (`diving`) hoặc trên ngọn sóng sáng (`brightAt` ≥ 0,85), tối đa 8 thanh cùng lúc (ưu tiên thanh đang bổ, rồi thanh sáng nhất).
  - **Kiếm xa:** chỉ "viền than": bồ hóng 1 px + một đường than hồng ≤ 1 px bị ăn mòn đứt khúc, chập chờn chậm 3–4 Hz. Nó khác Metal ở dáng (đứt khúc, chập chờn), không chỉ ở màu.
  - Số thanh có lưỡi lửa ≤ 14 mỗi khung (6 kiếm chủ + 8 kiếm giữa); phím 1: 3.
  - Đầu lưỡi lửa sắc (cạnh 0,85, không `blur`). Hướng lửa = 0,7 × (−vận tốc) + 0,3 × trục thế giới lên: lửa bị gió bạt về sau và bốc lên. Lửa chập chờn 8–12 Hz.
  - Dải màu, lấy từ `element-fire.ts`:
    - bồ hóng `#240715` alpha 0,85 ở viền ngoài;
    - thân son `#D93800` → cam `#FF8A2A` (sắc 15–27°), alpha thật 0,9;
    - hổ phách `#FFB703` (sắc 43°, sát vàng tiền) chỉ là một dải chuyển mảnh sát lõi, ≤ 15 % điểm ảnh hào quang;
    - lõi trắng vàng `#FFFDF0` × 2,4, chỉ ở gốc lửa sát mép, ≤ 1 px.
  - Áo này **thay** vỏ lửa `sheathAt` ở `SwordHooks.waiting`, `SwordHooks.travel` và `StreamHooks.travel` (cls 0). Kiếm sông vốn không có vỏ lửa.
  - Tàn lửa (`EmberPool`) giữ 40/s cho kiếm phím 1 đang bay; thêm 8/s cho kiếm giữa đang có lưỡi lửa.
  - Đề xuất kèm (Q3): lưỡi chế độ `furnace` nhẹ hơn, để lưỡi là thép tối nóng mép còn lửa nằm quanh.
- **Water** (`mode: "water"`), phác:
  - áo thành ống nước bám kiếm; mảnh thành các tấm nước cuộn, thân chàm alpha thật 0,9, đường bọt cứng ở mép;
  - dòng chữ S bằng flow map hai pha (Vlachos, Portal 2);
  - đuôi cuộn lại sau đốc;
  - không có thân cộng sáng. Khúc xạ chỉ có khi pass méo dùng chung đã dựng.
- **Các hệ sau, mỗi hệ một dòng:**
  - Wood: mảnh thành gai lá mọc ra từ mép rồi rụng thành lá.
  - Earth: mảnh thành phiến khoáng nặng (cắt alpha) nghiến dọc lưỡi.
  - Thunder: mảnh thành ống sét gãy khúc, UV nhảy bậc.
  - Wind: gần như vô hình, chỉ viền mực và phần méo.
  - Ice: mảnh thành vỏ pha lê mặt phẳng cứng, viền sương, đứng yên.

**Bản giảm chuyển động:** như cột cuối của bảng lớp. Lửa chập chờn ở 2 Hz, lưỡi lửa giữ hình. Mức gõ giữ thành một độ sáng đứng yên, vì nó mang thông tin.

**Chi phí, ước tính** (High, DPR 1, phím 7 lúc săn):

| Lớp | Lệnh vẽ | Ước tính |
|---|---|---|
| `MantleSheath`, 30 thẻ, ~2,4 nghìn px mỗi thẻ | +1 | 0,03–0,08 ms |
| `MantleHull`, 6 vỏ thấp đa giác | +1 | 0,01–0,03 ms |
| `MantleHalo` giải tích trong impostor, quad nới lề ~10 % | 0 | 0,02–0,04 ms |
| `SilkTail`: 6 dải sẵn có của kiếm chủ, đổi chế độ | 0 (chương trình `RibbonPool` có chế độ theo dải); +1 nếu dùng pool lụa riêng | ~0,01 ms |
| Đếm mật độ trên CPU | 0 | ~0,01 ms CPU |

- **Tổng phím 7, Metal: +0,08–0,17 ms, +2 lệnh vẽ.** Ở gom và nhát kết, vẽ chồng tăng; dự kiến 1,3–1,5 lần, phải đo (§6).
- **Fire hơn Metal:** lưỡi lửa trên ≤ 14 thanh (~3,5 nghìn px mỗi thanh), trừ 6 vỏ `sheathAt` được trả lại. Phần này tính vào 0,20 ms "thân và vật bay" của Fire.
- Ở cận cảnh, 6 kiếm chủ cỡ ~600 px: thêm khoảng 0,1–0,2 ms. Ở DPR 2, phần diện tích nhân 4.
- **Phím 1:** +0,01–0,04 ms.

**Rủi ro chính:**
- Ở 35–60 px, áo 2–3 px mỗi bên có thể đọc thành "thanh kiếm béo hơn, mờ hơn" thay vì áo khí.
- Ở 70–130 px, nếu khe mảnh và hai đường may không đọc ra, Metal thành viền phát sáng chung chung. Tấm ảnh §5.5 có một cột riêng hỏi giám khảo đúng câu đó.
- Thân áo sáng quá sẽ dựng lại "ống sáng" mà anh đã chê.
- Fire: phiên trước có ~90 tấm lửa đọc thành "tấm ván cháy", đã bỏ. A chặn lỗi đó bằng chia tầng và trần 14 thanh có lưỡi lửa; có một tấm so với ảnh cũ (§5.5).

Cách chặn: áo chỉ ở ngoài viền; thu bề ngang khi kiếm dày đặc (§4.7); viền mực; đo phần điểm ảnh lưỡi giữ màu (§6).

### 3.B Echo Cascade

**Pitch:** Speed made visible: each sword is chased by flat, hollow sword-light echoes of its blade that hang back in a clean line in flight, fan open on every turn and snap shut into the strike, while a bow wave splits the air ahead of its tip.

**Ý:** kiếm quang kiểu donghua.
- Thanh kiếm thật là vật duy nhất được chiếu sáng, đi đầu.
- Theo sau, **cách một khoảng**, là hai, ba "kiếm quang" phẳng, rỗng tâm: bóng **chỉ của lưỡi** (từ `bladeFrom` tới mũi, ~0,62 `L`), không có chuôi, chắn hay vòng ngọc. Vì vậy bóng đọc ra "vệt ánh kiếm", không thành "thêm kiếm".
- Quanh mũi có một sóng áp suất xé gió, tách khỏi viền và mở về phía sau. **Đỉnh V của sóng mũi chính là hai rãnh nhập một ở mũi** của Clear Wind.
- Hướng này đẹp ở chuyển động:
  - bay thẳng thì bóng xếp thành một hàng gọn, mờ;
  - rẽ thì bóng xòe theo cung;
  - lúc trúng, các bóng đuổi kịp và gập vào lưỡi.
- Khi đứng chờ, kiếm có một "bóng tư thế" lớn hơn nó một chút phía sau, như linh hồn của kiếm. Lúc phóng, bóng đó ở lại chỗ cũ và tan.
- 94 sóng mũi cùng hướng trên dòng sông tự thành vảy chữ V, không cần dải cấp dòng.

**Nhìn nhanh:**

```
  echo 3 (blade only)     echo 2 (blade only)     echo 1 (blade only)   gap     real sword          bow wave
 [=-          -=>]      [==-         -==>]      [===-       -===>]    ≥0.1 L   (O){ ======= blade =======>*  .-V
 hollow, flat, fading, never over the real sword                                                           (apex = the two grooves meeting)
```

| Cỡ trên màn | Thấy gì |
|---|---|
| 35 px | Thanh kiếm, một chữ V mảnh ở mũi, một vệt sáng nhạt phía sau đốc. Cả dòng thành vảy chữ V đồng hướng |
| 100 px | Hai, ba kiếm quang rỗng tâm xếp hàng sau đốc, mờ dần; sóng mũi hai cánh; khi rẽ có mảng quét |
| Cận cảnh | Bóng tư thế quanh kiếm chờ; mảng quét có mép trước HDR; đỉnh V sóng mũi lóe khi bổ |

**Các lớp:**

| Lớp | Tầng | Hình và cỡ | Ánh sáng | Trộn | Bloom | Giảm chuyển động |
|---|---|---|---|---|---|---|
| `BowWave` (A1 với hàm hình khác) | Kiếm chủ, kiếm giữa; kiếm xa trong impostor | Hai cánh là **đường cách đều** từ `AuraAnchors.profile`: đỉnh ở mũi + 0,03 `L`; khoảng tách khỏi mép sep(y) = 0 từ đỉnh tới 70 % lưỡi, rồi lên 0,6 `W` ở `bladeFrom` + 0,05 `L` (smoothstep). Cánh dài ≤ (chiều dài lưỡi − 0,05 `L`) ≈ 0,57 `L`, nên tắt trước chắn kiếm, không chạm vòng ngọc. Góc mở suy ra từ đó (~5° ở gốc cánh). Bề ngang cánh 0,25 `W`, sàn 1,5 px. Dài theo `clamp(v/20, 0.3, 1)`. Dưới 4 m/s không có cánh. Mép ngoài xa nhất ~1,35 `W` < nửa bề cao quad impostor (~3 `W`) | Đường sáng mảnh glow ≤ 0,85 phía trong; viền mực 1 px alpha 0,3 phía ngoài; đỉnh V thành core 2,4 (≤ 1 px) chỉ ở f0–2 lúc bổ và lúc trúng | Premultiplied, sau lưỡi 0,05 m | Đỉnh V, chỉ f0–2 | Giữ, bề ngang đứng yên |
| `EchoTrail` (B1 `GhostTrail`) | Mọi tầng | Vòng lịch sử tư thế (đốc, mũi, góc lăn) lấy mẫu theo thời gian thế giới; bóng chọn theo **quãng đường đã bay** (tra độ dài cung trong vòng lịch sử), không theo Δt cố định. Bóng 1: mũi bóng cách mũi kiếm 1,1 `L` theo đường bay, nên khi bay thẳng nó bắt đầu ≥ 0,1 `L` sau đốc. Các bóng sau cách nhau 0,7 `L` (khe 0,08 `L`, không chồng nhau khi bay thẳng). Mỗi bóng **chỉ là lưỡi**: cắt bằng cờ lưỡi `m.g` của atlas mặt nạ. Bóng k rộng 0,94^k. Số bóng High: kiếm chủ 3, kiếm giữa 2, kiếm xa 1. Dưới 4 m/s bóng mờ dần và tắt. **Cắt theo viên nang:** mỗi instance mang đốc và mũi hiện tại của thanh thật; điểm ảnh cách đoạn đốc–mũi ≤ `W`/2 + 2 px thì alpha = 0 (mềm 1 px) | Atlas impostor ở chế độ "echo": màu phẳng của hệ, không ánh kim loại. Rỗng tâm: độ đậm = bóng dáng × (0,35 + 0,65 × trường mép). Alpha 0,50 / 0,32 / 0,18 × (0,6 + 0,4 × ω chuẩn hóa), ≤ 0,75. Mực premultiplied alpha × 0,25 | Một lệnh vẽ instanced, `SwordImpostors` thứ hai ở chế độ echo | Không bao giờ | Làm dịu: 1 bóng cho kiếm chủ và giữa, alpha × 0,6, không gập lúc trúng |
| `SweepSmear` (B3) | Kiếm chủ, kiếm giữa | Một tấm 4 đỉnh giữa đường lưỡi khung trước và khung này, chỉ khi lưỡi quét ngang > 6 rad/s: K2 quét, K4 xoay, phím 7 rẽ để bổ xuống, xoắn lúc gom. Sống 1–2 khung. Tối đa 1 tấm mỗi kiếm mỗi khung. Tấm bắt đầu từ mép lưỡi khung trước, không phủ thanh thật khung này | Mép trước core 2,4 (≤ 1 px); thân ≤ 0,8, tắt về mép sau | Premultiplied | Mép trước | Tắt |
| `StanceEcho` | Kiếm chờ | Một bóng cùng tư thế, to 1,08 lần, ngay sau kiếm theo độ sâu (0,06 m), chỉ phần ló ra ngoài viền | Thân ≤ 0,45 theo mức gõ: 0,15 / 0,30 / 0,45 | Như `EchoTrail` | Không | Giữ (mang mức gõ), không thở |

- Không có `EdgeThreads` nữa: hai sợi khí từ mép sẽ chạy đè lên chuỗi bóng, thành ≥ 3 lớp trong suốt ở một điểm ảnh. Chuỗi bóng đã là vệt của B.
- B **thay** mọi vệt sau đốc bằng chuỗi bóng: dải sáng, dải lụa (phím 1), tia `BeamPool` (kiếm giữa, kiếm xa). Bảng thay ở §4.6.
- Đường mép sẵn có trên lưỡi **không đổi**. Điểm nhấn ở mũi nằm ngoài đường viền: đỉnh V của `BowWave`.

**Theo trạng thái:**

| Trạng thái | Làm gì |
|---|---|
| Chờ | `StanceEcho` sau kiếm, thở 2,4 s, đậm theo mức gõ. Chưa có sóng mũi |
| Phóng | Bóng tư thế **ở lại** chỗ phóng, tan trong 10 khung: kiếm để lại bóng của mình. Lịch sử bắt đầu tích từ khung 0; bóng 1 hiện khi kiếm đã bay đủ 1,1 `L`. Sóng mũi mọc theo tốc độ trong 4 khung |
| Bay đều | Bóng xếp thành hàng gọn sau đốc, alpha × 0,6: pha yên nhất. Sóng mũi đứng yên |
| Rẽ | Bóng xòe theo cung, alpha × 1,0. Cánh ngoài của sóng mũi tách xa 1,3× (vẫn trong lưỡi). Có mảng quét khi lưỡi quét ngang |
| Bổ, trúng | f0–2: các bóng đuổi kịp và gập về phía đốc (dừng ở mép viên nang, không đè lưỡi), đỉnh V sóng mũi lên core 3,0. Sau đó chuỗi bóng tích lại từ đầu |
| Về, tan | Thanh kiếm tan vào chính các bóng của nó: bóng cuối tắt sau cùng, sau lưỡi 8 khung. Lúc gấp dòng, các bóng hội tụ |

**Theo tầng hiển thị:**

| Tầng | Có |
|---|---|
| Lưới đủ | `BowWave`, 3 bóng, `SweepSmear`, `StanceEcho` khi chờ |
| LOD | `BowWave`, 2 bóng, `SweepSmear` |
| Impostor | 1 bóng; sóng mũi vẽ trong chính shader impostor (cánh nằm trong quad) |

**Theo bậc đồ họa** (số bóng của kiếm chủ / giữa / xa):

| Bậc | Có |
|---|---|
| Low (không bloom) | Bóng 1 / 1 / 0; sóng mũi chỉ cho kiếm chủ và giữa; không mảng quét. Đỉnh V và mép bóng phải đọc được khi không bloom |
| Medium | Bóng 2 / 1 / 1; mảng quét |
| High | Bóng 3 / 2 / 1 |
| Ultra | Bóng 3 / 3 / 2; mảng quét cả khi rẽ vừa (> 4 rad/s) |

**Chất theo hệ:**
- **Metal**, làm ngay:
  - bóng bạc lam `[0.36, 0.66, 0.85]` ≤ 0,75, trường mép làm sắc;
  - sóng mũi là một đường áp suất thẳng, cứng;
  - mảng quét có mép trước sắc;
  - mực chàm alpha 0,3.
- **Fire**, làm ngay, chia tầng như A:
  - Bóng của kiếm chủ, kiếm phím 1 và ≤ 8 kiếm giữa (đang bổ hoặc `brightAt` ≥ 0,85) cháy từ mép sau thành lưỡi lửa, theo nhiễu bốc lên. Màu nguội theo tuổi: bóng 1 cam `#FF8A2A` với dải hổ phách mảnh sát lõi, bóng 2 cam son, bóng 3 son `#D93800` rồi bồ hóng (mực alpha 0,5 ở mép bị ăn). Trần ≤ 14 thanh có lưỡi lửa mỗi khung.
  - Bóng của kiếm giữa còn lại và kiếm xa: màu than hồng phẳng, mép bồ hóng, không lưỡi lửa.
  - Cả chuỗi đọc thành ngọn lửa của thanh kiếm đang cháy dần lại phía sau.
  - Sóng mũi thành sóng nhiệt: đường son có mực bồ hóng; chỉ ở kiếm chủ, lưỡi lửa bóc khỏi hai cánh về sau, vươn 1,2 `W`.
  - Tàn lửa rơi từ bóng cuối, 20/s cho kiếm chủ.
  - Thay `sheathAt` như ở A.
- **Water**, phác:
  - bóng thành "dấu nước": thân chàm alpha thật, viền bọt;
  - bóng không mờ đi mà vỡ: bóng cuối tan thành giọt;
  - sóng mũi là bụi nước mũi thuyền với đường bọt cứng.
- **Các hệ sau, mỗi hệ một dòng:**
  - Thunder: bóng nhảy bậc như dịch chuyển chớp, nối bằng tia 1 px.
  - Wind: bóng áp suất gần như không màu, chỉ mực và phần méo.
  - Ice: bóng đóng băng tại chỗ thành tượng sương, vỡ sau 6 khung.
  - Earth: bóng là bụi đá rơi xuống, trộn thường, màu đất son.
  - Wood: bóng mọc gai lá rồi rụng thành lá.

**Chi phí, ước tính** (High, phím 7 lúc săn):

| Lớp | Lệnh vẽ | Ước tính |
|---|---|---|
| `BowWave`, 30 thẻ hẹp | +1 | 0,03–0,06 ms |
| `EchoTrail`, 6 × 3 + 24 × 2 + 64 × 1 = 130 bóng chỉ lưỡi, ~1,6 nghìn px mỗi bóng, cộng phép cắt viên nang | +1 | 0,04–0,08 ms |
| `SweepSmear` | +1 | < 0,02 ms |
| Sóng mũi kiếm xa trong impostor; bỏ tia sau đốc (88 tia) và dải sáng (6) | 0 | +0,01 / −0,01 ms |

- **Tổng phím 7, Metal: +0,08–0,16 ms, +3 lệnh vẽ.** Gom và nhát kết phải đo riêng (§6).
- **Phím 1:** +0,02–0,05 ms.

**Rủi ro chính:**
- Bóng có thể vẫn đọc thành "thêm kiếm" và rối, dù chỉ là lưỡi.
- Khi bay thẳng, bóng lùi ra sau đốc nên quanh thân kiếm gần như trống: trả lời câu chê yếu nhất khi bay chậm, bay thẳng.
- Ở làn dày của dòng sông, các chuỗi bóng chồng nhau thành một mớ sọc.
- Khi rẽ, bóng có thể quét qua vùng chữ.

Cách chặn: bóng chỉ lưỡi, phẳng, rỗng tâm, màu hệ, nhỏ dần; cắt viên nang; bớt bóng theo mật độ (§4.7); đo độ phủ và độ chồng lớp (§6).

### 3.C Celestial Regalia

**Pitch:** Clear Wind flies as a crowned relic: a star at its point, a slow-turning halo standing behind the hollow jade ring, twin tassel-silk streamers off the cloud guard and motes in orbit, the steel left bare inside a jeweller's hairline.

**Ý:** biến thanh kiếm thành một bảo vật thiên giới, như bộ radiance anh muốn cho nhân vật (halo, hạt sáng, dải sáng), áp cho vật.
- Ánh sáng không phủ thân kiếm mà dồn vào ba "trạm":
  - một ngôi sao ở mũi;
  - một quầng tròn **đứng sau vòng ngọc rỗng**, đóng khung chữ ký của Clear Wind ("lưỡi thẳng xuyên vòng ngọc bích rỗng", WEAPON_DESIGN §6);
  - hai dải lụa sáng từ hai mút chắn mây, hội lại phía sau.
- Thân thép giữa các trạm để trần, chỉ có đường mép sẵn có và một viền mảnh như đường kim hoàn. **Hai viền kim hoàn hai bên sáng dần về mũi và hội ở sao mũi**: đó là "hai rãnh nhập một ở mũi", vẽ ngoài đường viền.
- Khi kiếm chờ sau vai, mỗi thanh có một vầng mandorla mờ lớn dần theo mức gõ.

**Nhìn nhanh:**

```
   two silk streamers (tassel colours), meeting behind    halo behind the hollow O, cut at the sword     hairline rims brighten and meet at the star
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\                 .-.                                                            |
                                      >--            ( (O) ){ ===============================================>    --*--
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/                 '-'    .  motes  .         .                                   |
```

| Cỡ trên màn | Thấy gì |
|---|---|
| 35 px | Một chòm hai điểm: sao ở mũi và chấm sáng ở vòng ngọc, cho biết ngay hướng kiếm. Thân kiếm có viền mảnh. Kiếm xa không có sao |
| 100 px | Quầng tròn sau vòng ngọc, sao bốn cánh kéo theo hướng bay, hai viền hội về sao, hai dải lụa đuôi én, vài hạt bay quanh |
| Cận cảnh | Vòng 12 vạch ấn quay chậm trong quầng, hạt sáng trên hai quỹ đạo nghiêng, dải lụa bện nhau khi rẽ |

**Các lớp:**

| Lớp | Tầng | Hình và cỡ | Ánh sáng | Trộn | Bloom | Giảm chuyển động |
|---|---|---|---|---|---|---|
| `TipStar` | Kiếm chủ luôn có; kiếm giữa chỉ khi trên ngọn sóng sáng (`brightAt` ≥ 0,7) hoặc khi bổ xuống; kiếm xa không | Sao bốn cánh ở mũi + 0,02 `L`. Cánh dọc hướng bay 0,12 `L` (0,37 m ở kiếm 3,06 m, ~12 px ở 100 px), cánh ngang 0,04 `L`. Hướng cánh đổi theo vận tốc trong 4 khung | Lõi đĩa ≤ 2 px, core 3,0 (0,7 màu lõi hệ + ≤ 0,3 trắng). Cánh glow ≤ 0,85, thon dần. Sau sao có một sao mực to 1,3× alpha 0,3, **trong cùng shader**. Lấp lánh: nền 0,6, mỗi 1,4–2,2 s (seed riêng) lên 1,0 trong 10 khung | Pool mới `SwordAuraSprites` (premultiplied, sáng và mực trong một shader, có tone map) | Lõi sao | Làm dịu: sao đứng yên, không lấp lánh |
| `RingHalo` | Kiếm chủ, kiếm giữa; kiếm xa là chấm O trong impostor | Quad **hướng về camera**, tâm ở tâm vòng ngọc, **đẩy ra sau lưỡi 0,05–0,08 m theo độ sâu**, nên luôn là vòng tròn và không đánh nhau độ sâu với lưới đục. Bán kính 1,7 × bán kính ngoài vòng ngọc (đọc từ model; ước tính ~0,085 `L`, ~8–9 px ở 100 px). Nét max(1,5 px, 0,012 m); quầng mềm 3 px ra ngoài, 1 px vào trong. **Nét bị cắt** ở chỗ giao với bóng dáng kiếm (lưỡi, chuôi, mút chắn mây), chừa khe 1 px, tính từ `AuraAnchors.profile`, `guardHalf` và trục kiếm trên màn. **Lòng vòng trong suốt**, chữ O luôn trống. Vòng ấn chỉ ở kiếm chủ ≥ 90 px: 12 vạch ngắn giữa 1,0 và 1,25 bán kính, quay một vòng mỗi 8 s | Nét glow 0,75–0,85; vạch ≤ 0,75; một vành mực 1 px alpha 0,3 ngay ngoài. Nét thành core 2,4 chỉ ở kiếm chủ, f0–2 lúc phóng và nhịp từ `perfect`/`flash` | Một lệnh vẽ instanced | Nét, chỉ f0–2 | Giữ; vòng ấn không quay |
| `GuardStreamers` | Kiếm chủ phím 7, kiếm bay phím 1 (kiếm giữa: hai đường kẻ trong tia sẵn có) | Hai dải `RibbonPool` từ hai mút chắn mây (±`guardHalf`), **thay** dải sáng và dải lụa sẵn có. Dài 0,9 `L` (phím 1), 0,6 `L` (phím 7). Rộng 0,06 → 0,01 m, chẻ đuôi én ở cuối, hội lại sau đốc ở 0,5 dài dải. Song song khi bay đều, bện nhau khi rẽ (lệch pha 0,12 s). Kiếm giữa: tia `BeamPool` sẵn có vẽ thành hai lõi mảnh ±0,35 `W` (thay kiểu, không thêm) | Metal: thân lụa `silkLight` ≤ 0,7, mép `silkDeep` alpha thật, lõi lam thép `pow(s, 7)` × 2,0 mảnh. Fire: chất lửa | Chương trình premultiplied của `RibbonPool` với chế độ theo từng dải (§5.2); capacity `RibbonPool` phím 7 từ 6 lên 12 | Lõi dải | Làm dịu: ngắn lại, không bện |
| `OrbitMotes` | Kiếm chủ | 10 hạt mỗi kiếm trên hai quỹ đạo elip nghiêng ±25° quanh thân kiếm: ngang 0,12 `L`, dọc 0,3 `L`. 2–3 rad/s. Cỡ 0,01–0,02 `L` (≥ 2 px). Quỹ đạo tính trong vertex shader từ một `DataTexture` tư thế 94 × 2 (tâm và hướng của từng kiếm), không tích phân trên CPU | Glow ≤ 0,85; 2/10 hạt có tâm core 2,0 | `SwordAuraSprites` | 2 hạt | Làm dịu: chậm × 0,3, số hạt × 0,6, không lấp lánh |
| `HairlineRim` (A1 hẹp) | Mọi tầng | Một viền kim hoàn 1–1,5 px glow ngay ngoài đường viền, thêm 1 px mực. Từ 60 % lưỡi tới mũi, viền sáng dần (0,4 → 0,8) và hai bên hội vào sao mũi. Kiếm xa: trong shader impostor | Glow ≤ 0,6 (≤ 0,8 ở chỗ hội); mực alpha 0,3 | Premultiplied | Không | Giữ |
| `WaitMandorla` | Kiếm chờ (phím 1 sau vai, vầng K5) | Vầng hình hạt hạnh nhân sau mỗi thanh, cao 1,25 `L`, rộng 0,35 `L` | Glow ≤ 0,45; mực ≤ 0,2, trong cùng shader. Lớn theo ba bậc của mức gõ | `SwordAuraSprites` | Không | Giữ (mang mức gõ) |

**Theo trạng thái:**

| Trạng thái | Làm gì |
|---|---|
| Chờ | Mandorla theo mức gõ. Quầng ngọc quay chậm. Hạt bay quỹ đạo chậm. Sao mờ 0,4 |
| Phóng | Nét quầng lên core 2,4 ở f0–2, về glow ≤ 0,85 từ f3; nở 1,25× rồi về 1,0 trong 12 khung. Sao sáng đủ ngay f0. Hai dải bắt đầu. Mandorla ở lại chỗ cũ, tan trong 10 khung |
| Bay đều | Sao 0,6, thỉnh thoảng lấp lánh. Quầng đứng yên 0,75. Hạt bay theo kiếm. Hai dải song song |
| Rẽ | Hai dải bện nhau. Hạt bên ngoài đường cong văng xa 1,3×. Cánh sao xoay theo hướng mới trong 4 khung |
| Bổ, trúng | Sao bùng 1,6× cỡ, core 3,6 ở f0–2, rồi co lại trong 6 khung. Quầng co 0,8× rồi đập ra 1,2× (≤ 0,9) trong 10 khung. Hạt tung ra và tắt trong 8 khung |
| Về, tan | Sao tắt trước (4 khung). Quầng thu dần về vòng ngọc (12 khung). Hạt xoáy vào vòng ngọc. Dải tắt sau cùng |

**Theo tầng hiển thị:**

| Tầng | Có |
|---|---|
| Lưới đủ | Đủ sáu lớp; mandorla chỉ khi chờ |
| LOD | Sao (chỉ trên ngọn sóng và khi bổ), quầng (không vạch ấn), tia hai đường kẻ, viền kim hoàn |
| Impostor | Chấm O ≤ 0,85 ở vị trí vòng ngọc (từ meta), viền kim hoàn trong shader, tia sau đốc mảnh |

**Theo bậc đồ họa:**

| Bậc | Có |
|---|---|
| Low (không bloom) | Sao cho kiếm chủ, quầng không vạch, viền kim hoàn, chấm O. Không hạt. Dải lụa đôi chỉ ở phím 1. Sao và nét quầng phải đọc được khi không bloom (glow 0,85 + mực) |
| Medium | Thêm hai dải cho kiếm chủ phím 7; 6 hạt mỗi kiếm chủ |
| High | Đủ như bảng lớp |
| Ultra | 14 hạt mỗi kiếm chủ; vạch ấn từ 70 px; sao cho kiếm giữa cả khi rẽ |

**Chất theo hệ:**
- **Metal**, làm ngay:
  - sao lõi `[0.62, 0.88, 1.0]` × 3,0;
  - quầng bạch kim `[0.62, 0.72, 0.85]` ≤ 0,8;
  - dải lụa màu tua, lõi lam thép `[0.45, 0.62, 0.85]`;
  - hạt là sao bạc bốn cánh; mực chàm.
  - Không vàng: Kiếm và Metal giữ bạc, lam (`METAL_STREAM`), và vàng là màu tiền (`#FFC83A`).
- **Fire**, làm ngay:
  - Sao thành "tia mặt trời": lõi trắng vàng, cánh là các lá của một flipbook lửa (dùng lại flipbook Dragonhold trước khi tạo mới), thân cánh cam `#FF8A2A`, hổ phách chỉ sát lõi.
  - Quầng thành **vòng lửa**: một dải lửa mảnh liếm ra ngoài từ vòng tròn, lưỡi lửa dài 0,4 × bán kính, bốc lên; thân son → cam (15–30°); mực bồ hóng.
  - Hai dải thành dải lửa (chế độ lửa của `RibbonPool`).
  - Hạt là tàn lửa (`EmberPool`). Viền kim hoàn thành viền than có bồ hóng.
  - Lửa nằm ở vòng, ở mũi, ở dải; mặt thép không cháy.
- **Water**, phác:
  - sao là ánh giọt nước có chữ thập bọt;
  - quầng là một vòng nước xoay, alpha thật, mép bọt;
  - dải là dải nước viền bọt; hạt là giọt nước có điểm sáng.
- **Các hệ sau, mỗi hệ một dòng:**
  - Thunder: sao là tâm bão có 2–3 tia nhỏ nối về vòng ngọc; quầng đứt khúc, lách tách.
  - Wood: vòng mọc vạch lá; hạt là hạt giống.
  - Earth: vòng là chuỗi hạt đá quay; sao là một mặt ngọc cắt.
  - Wind: vòng áp suất, chỉ mực và phần méo; hạt là bụi.
  - Ice: vòng vạch sương lục giác; sao là ánh pha lê.

**Bản giảm chuyển động:** như cột cuối của bảng lớp. Bùng lúc trúng × 0,6.

**Chi phí, ước tính** (High, phím 7 lúc săn):

| Lớp | Lệnh vẽ | Ước tính |
|---|---|---|
| `SwordAuraSprites`: sao (6 kiếm chủ + ~8 kiếm giữa) và 60 hạt | +1 | 0,01–0,02 ms |
| `RingHalo`, 30 quad ~18 × 18 px | +1 | 0,01–0,02 ms |
| `GuardStreamers`, 12 dải thay 6 dải; tia kiếm giữa đổi kiểu | 0 (`RibbonPool` có chế độ theo dải); +1 nếu pool riêng | 0,01–0,03 ms |
| `HairlineRim`, 30 thẻ hẹp | +1 | 0,02–0,04 ms |
| Chấm O và viền trong impostor | 0 | 0,01–0,02 ms |

- **Tổng phím 7, Metal: +0,06–0,13 ms, +3 lệnh vẽ (+4 nếu dải ở pool riêng).**
- **Phím 1:** có 3 mandorla và 30 hạt khi chờ, +0,02–0,04 ms.

**Rủi ro chính:**
- **Dòng sông 88 thanh vẫn gần như trần:** chỉ có viền mảnh, chấm ngọc, và sao trên ngọn sóng. Ở camera chơi anh có thể vẫn thấy "thô", đúng lời vừa chê.
- 6 kiếm chủ dễ thành "lấp lánh" rẻ tiền nếu sao nháy nhiều.
- Vòng lửa của Fire dễ đọc thành màu tiền vàng `#FFC83A`: giữ thân ở 15–30°, hổ phách ≤ 15 %.
- **Vòng ngọc của model Tripo hiện ra màu bạc như crôm,** trong khi ảnh đã duyệt là ngọc trắng viền vàng (changelog kiếm thật). Quầng sẽ rọi đúng vào chỗ lệch đó (Q4).

### 3.D So sánh, và tôi nghiêng về hướng nào

| | A · Wind-Silk Mantle | B · Echo Cascade | C · Celestial Regalia |
|---|---|---|---|
| Trả lời "không có gì quanh kiếm" | Mạnh nhất ở kiếm giữa và kiếm xa: thanh nào cũng có áo hoặc quầng | Mạnh khi rẽ và bổ; khi bay thẳng, bóng lùi sau đốc nên quanh thân gần như trống; dưới 4 m/s không có gì | Mạnh ở 6 kiếm chủ, yếu ở dòng sông |
| Giữ kiếm đọc được | Tốt (áo ngoài viền, cổ áo hở) | Tốt sau khi cắt viên nang; vẫn có thể làm loãng "đâu là kiếm thật" | Tốt nhất (thép trần) |
| Ở 35 px | Kiếm có viền khí và mũi kim | Vảy chữ V đồng hướng | Chòm hai điểm, kiếm xa gần trần |
| Ở 100 px, chữ ký | Mảnh so le, hai đường may hội ở mũi kim | Đỉnh V sóng mũi, chuỗi kiếm quang | Quầng sau vòng O, hai viền hội ở sao |
| Cận cảnh | Đẹp (mảnh trượt cắt, vệt khí vẽ tay, viền ôm khối) | Đẹp khi rẽ và bổ | Đẹp nhất (vòng ấn, hạt, dải bện) |
| Fire | Lưỡi lửa liếm quanh lưỡi ở ≤ 14 thanh, còn lại áo than | Bóng cháy dần lại phía sau | Vòng lửa, sao lửa |
| Water sau này | Ống nước bám kiếm, hợp "flow → engulf" nhất | Dấu nước vỡ thành giọt | Vòng nước, giọt |
| Chi phí phím 7 (Metal) | 0,08–0,17 ms, +2 lệnh vẽ | 0,08–0,16 ms, +3 | 0,06–0,13 ms, +3 |
| Rủi ro | Kiếm béo, mờ; viền chung chung | Rối, "thêm kiếm"; trần khi bay thẳng | Vẫn trần ở xa |

**Ý kiến của Claude (không phải kết luận):** nghiêng về A.
- A phủ đều nhất ở tầng kiếm giữa và kiếm xa, tức đúng chỗ anh chê: 88 thanh của dòng sông là phần lớn những gì anh thấy ở camera chơi.
- Với mảnh "align → shear" và hai đường may hội ở mũi kim, A có một chữ ký riêng thay vì một viền phát sáng.
- A hợp với Water nhất.
- Nhưng: C rẻ nhất và giữ thép sạch nhất; B mạnh nhất lúc rẽ và lúc bổ. Không hướng nào thắng ở mọi dòng của bảng. Anh chọn sau khi xem bảng hình và phác ý tưởng (§5.0).

Thêm:
- Nếu anh thích A nhưng muốn sang hơn ở kiếm chủ, có thể mượn **một** lớp của hướng khác **sau khi** A đạt: sao mũi của C, hoặc mảng quét của B. Không ghép cả ba: đó là đường quay lại mớ VFX rối (ChatGPT cũng cảnh báo vậy).
- Cả ba đều còn dư so với +0,6 ms lúc săn, nhưng nhát kết chỉ còn +0,5 ms (§1.2). Phần dư dành cho Ultra, DPR > 1 và chất của hệ. Không dùng phần dư để chồng thêm lớp.

## 4. Luật chung cho cả ba hướng

1. **Clear Wind luôn đọc được.**
   - **Mặt lưỡi:** không lớp hào quang nào vẽ lên mặt lưỡi, và không lớp nào đổi đường mép sẵn có.
   - **Phủ lưỡi:** không lớp nào phủ quá **10 %** diện tích lưỡi ở bất kỳ khung nào. Riêng chớp lúc trúng, tối đa 3 khung, được tới 20 %. Bóng của B phủ lưỡi, chắn, vòng ngọc ≤ **3 %**.
   - **Vùng cấm quanh chắn:** từ đầu chắn kiếm tới `bladeFrom` + 0,03 `L`, không có thân hào quang.
     - ≥ 95 % điểm ảnh của vòng ngọc và chắn mây giữ màu, ở **từng khung**.
     - Chỉ `RingHalo` của C được đóng khung vòng ngọc, từ phía sau và bị cắt ở bóng dáng kiếm; lòng chữ O luôn trống.
   - Cách đo ở §6.
2. **Không thành màn trên nền sáng.**
   - Mọi lớp sáng có lớp mực trong cùng shader: premultiplied, `rgb = tối × a` với `a > 0` cộng `rgb = sáng` với `a = 0`.
   - Kênh trong suốt luôn tách khỏi màu; không lấy độ sáng làm alpha (DRAGON_FIRE_DIAGNOSIS).
   - Các pool sẵn có `SpritePool` "add", `BeamPool` và chương trình sáng của `RibbonPool` đều cộng sáng (`ONE, ONE`), không vẽ được mực. Vì vậy lớp nào cần mực đi vào pool premultiplied mới hoặc chương trình premultiplied (§5.2).
   - Trên đá `#d6d0c2`, phần "nhạt" ≤ 10 % điểm ảnh của hào quang. Trên nền `#2a2c30`, không có vành đen.
3. **Ánh sáng.**
   - Chỉ lõi mảnh được vượt 1: HDR 2,4–3,6, ≤ 1 px ở camera chơi, ≤ 3 px ở cận cảnh, ≤ 30 % bề ngang của lớp đó.
   - Đỉnh HDR chỉ ở f0–2, về glow ≤ 0,85 từ f3 (VFX_STANDARD §3.4: lóe 2–3 khung).
   - Thân, quầng, vòng, bóng, hạt ≤ 0,85 mỗi kênh.
   - Quầng không nhân `SWORD_LIGHT` hay `uGain`.
   - Không đổi bloom chung (strength, radius, threshold), exposure hay tone map.
   - Khung đầu sáng đủ: lớp mới sinh vẽ ở tuổi 0.
   - Bậc Low không bloom phải đạt nhờ glow 0,85 và mực (VFX_STANDARD §3.5 luật 2).
4. **Màu.**
   - Không bao giờ dùng đỏ cảnh báo `#FF4A4A`.
   - Không thành mảng phẳng sáng mạnh ở các màu dành riêng (canon §21.1):
     - cam khẩn `#FFB020` (sắc 39°);
     - vàng tiền `#FFC83A` (sắc 43°);
     - xanh ngọc của sức gõ `#7FF5E0` (sắc 169°).
   - Điểm ảnh hào quang trong ±6° sắc và ±0,1 độ sáng của ba màu đó ≤ 3 %.
   - Lửa luôn là dải chuyển màu, không phải một mảng. Thân lửa ở `#D93800` → `#FF8A2A` (15–30°); hổ phách `#FFB703` (43°) chỉ là dải chuyển mảnh sát lõi, ≤ 15 % điểm ảnh hào quang.
   - Metal không có vàng.
5. **Không phụ thuộc tốc độ khung.**
   - Lịch sử tư thế và vệt lấy mẫu theo thời gian thế giới (như `RIBBON_SAMPLE_S`). Mọi tốc độ tính theo giây.
   - Khi dừng hình, mọi thứ đứng yên. 60 Hz và 120 Hz trông như nhau.
   - Không lớp nào nhảy alpha hay cỡ quá 30 % trong một khung, ngoài các chớp có chủ ý.
   - Mọi sàn tính bằng px CSS × `uDpr`, nên bề ngang không phập phồng khi DPR trôi.
6. **Thay, không chồng (D59).** Mỗi hướng thay các lớp vệt sẵn có theo bảng dưới. Không lớp hiện có nào ở lại chồng với lớp mới cùng vai.

   | Chỗ | Đang có, Metal | Đang có, Fire | A | B | C |
   |---|---|---|---|---|---|
   | Phím 1, chờ | Tia lóe chạy dọc lưỡi mỗi 0,9 s (`twinkle`) | `SwordHooks.waiting`: `sheathAt` nguội + tàn lửa bốc lên | `MantleSheath` thay tia lóe / thay `sheathAt`; giữ tàn lửa | `StanceEcho` thay tia lóe / thay `sheathAt`; giữ tàn lửa | `WaitMandorla` + `RingHalo` thay tia lóe / thay `sheathAt`; giữ tàn lửa |
   | Phím 1, bay | Dải sáng (`TrailLook.widthM` 0,14 m) + dải lụa + sao lóe mũi + hạt rơi | Dải lửa + `sheathAt` + tàn lửa 40/s | `SilkTail` thay dải sáng và dải lụa (Fire: dải lửa sẵn có là `SilkTail`); `MantleSheath` thay `sheathAt`; mũi kim thay sao lóe mũi; giữ hạt rơi / tàn lửa | `EchoTrail` thay dải sáng, dải lụa / dải lửa; `BowWave` thay sao lóe mũi; bỏ `sheathAt`; giữ hạt rơi; tàn lửa 20/s | `GuardStreamers` thay dải sáng và dải lụa / dải lửa; `TipStar` thay sao lóe mũi; `OrbitMotes` thay hạt rơi; bỏ `sheathAt`; tàn lửa giữ |
   | Phím 7, 6 kiếm chủ | Dải `RibbonPool` màu `trailCore` | Dải lửa + `sheathAt` (`StreamHooks.travel`, cls 0) | `SilkTail` thay dải; `MantleSheath` + `MantleHull` thay `sheathAt` | `EchoTrail` 3 bóng thay dải; bỏ `sheathAt` | `GuardStreamers` thay dải; bỏ `sheathAt` |
   | Phím 7, 24 kiếm giữa | Tia `BeamPool` một khung sau đốc: 0,45 `L` sông, 0,9 `L` bổ, 0,6 `L` gom | Như Metal, tông lửa (không có vỏ lửa) | Đuôi áo trong thẻ thay tia | `EchoTrail` 2 bóng thay tia | Tia giữ, vẽ thành hai lõi mảnh (đổi kiểu) |
   | Phím 7, 64 kiếm xa | Tia như kiếm giữa, sáng × 0,55 | Như Metal, tông lửa | Tia giữ, tô màu lụa / than (đổi kiểu); `MantleHalo` trong impostor | `EchoTrail` 1 bóng thay tia | Tia mảnh giữ; chấm O và viền trong impostor |

   - Phép thử `tests/view/sword-aura.test.ts` đếm số lớp đang sống ở mỗi chỗ trong bảng, theo hướng và theo hệ.
   - **Chồng lớp:** trong vùng của mỗi kiếm, ≤ 2 lớp trong mờ ở mọi điểm ảnh (ELEMENT_LAYER §5), đo ở khung đỉnh (F60–F160 và gom F168–207). Con số cả sân của VFX_STANDARD §3.7 (High: trung bình ≤ 3, đỉnh ≤ 8 trong ≤ 10 khung) chỉ báo cáo, không dùng để nới luật của ELEMENT_LAYER. Chỗ hai luật lệch nhau là câu Q6.
7. **Thu theo mật độ.**
   - Khi một thanh có ≥ 3 thanh khác trong 40 px trên màn, hào quang của nó thu bề ngang × 0,8.
   - Các lớp phụ tắt trước: bóng thứ hai trở đi, hạt, sao.
   - CPU đếm mật độ trong vòng vẽ kiếm sẵn có (94² phép so, ~0,01 ms).
8. **Hào quang thuộc vũ khí, chất thuộc hệ.** Hai hợp đồng, tên tiếng Anh, chưa sửa mã.
   - **Phía vũ khí:** neo hào quang đo từ GLB lúc nạp, trong `blades.ts`, gắn vào `SwordModel`. Hệ trục là hệ jian của `blades.ts`: chắn ở y = 0, mũi ở y = 1, cả chuôi ở y < 0 (đốc ở `pommelY` ≈ −0,61).

     ```ts
     /** Where a weapon's aura sits on its unit blade (measured from its GLB at load). */
     export interface AuraAnchors {
       readonly profile: Float32Array;   // 96 blade half-widths from bladeFrom to the tip (edgeField's half[])
       readonly bladeFrom: number;       // unit y where the blade starts
       readonly guardFrom: number;       // unit y where the guard band starts (no aura body from here to bladeFrom + 0.03)
       readonly ring: { readonly y: number; readonly r: number } | null; // jade ring centre and outer radius (unit)
       readonly guardHalf: number;       // half width of the cloud guard (streamer roots)
       readonly tasselFrom: number;      // tassel or silk root on the unit axis (≤ pommelY: past the pommel end)
     }
     ```

     - Kiếm xa không có `SwordModel`: neo của nó lấy từ `SwordAtlasMeta` (`u0`, `u1`, `guardU`, `bladeFromU`), thêm `ringU`, `ringR` và `rollWidth` (bề ngang tương đối của 4 hàng lăn). Bảng `profile` dùng chung với kiếm gần, vì cùng một GLB.
   - **Phía hệ:** một mục `swordAura` mới trong `ElementKit` (`element-kit.ts`), cùng kiểu với `blade` và `trail`. Đặt cho mọi lớp bằng `applySwordAuraLook(kit.swordAura)`, một bộ uniform chung `SWORD_AURA_LOOK` như `SWORD_LOOK`. `applySwordAuraLook` kẹp thân ≤ 0,85 mỗi kênh (hôm nay `ramp.body` của Metal là `[0.05, 0.56, 0.9]` và của Fire là `#FF7A2A`, R tuyến tính 1,0; cả hai vượt). Mỗi `mode` là một define, một chương trình, biên dịch lúc nạp.

     ```ts
     /** The sword aura's matter (canon D59): the weapon's aura shape drawn in the element's material. Matter only. */
     export interface SwordAuraLook {
       readonly mode: "qi" | "flame" | "water";   // later: "arc" | "leaf" | "stone" | "frost" | "gust"
       readonly ramp: ElementRamp;                 // roles: core (unit, × coreHdr), edge, body (clamped ≤ 0.85), soot
       readonly coreHdr: number;                   // thin core gain, 2.4–3.6
       readonly ink: { readonly rgb: Rgb; readonly alpha: number }; // premultiplied dark under-layer
       readonly edge: number;                      // 0 soft … 1 hard (eroded tongues, foam lines, plate edges)
       readonly flow: {
         readonly speed: number;                   // blade lengths per second at rest
         readonly perMps: number;                  // added per m/s of flight
         readonly scale: number;
         readonly buoyancy: number;                // 0 along the blade … 1 world up (Fire)
         readonly curl: number;                    // 0 straight (Metal) … 1 S-flow (Water)
         readonly twoPhase: boolean;               // flow map with two half-period phases (Water)
       };
       readonly breakup: number;                   // erosion into tongues, foam or shards (0 none … 1 full)
       readonly reachW: number;                    // how far broken pieces pass the shape, in blade widths
       readonly flickerHz: number;                 // 0 steady
       readonly shed: "none" | "glints" | "embers" | "droplets";
       readonly distortion: number;                // share of the shared distortion pass (0 for now)
       readonly reduced: { readonly flow: number; readonly flickerHz: number }; // reduced-motion multipliers
     }
     ```

   - **Phía hướng (mô-đun kiếm, không thuộc hệ):** bề ngang hình (`widthW`), sàn theo px CSS (`minPx`), số mảnh, số bóng, cỡ sao và quầng nằm trong mô-đun của hướng. Màu của sao, vòng, bóng, hạt lấy từ các vai của dải màu (`core`, `edge`, `body`, `soot`), không phải trường riêng của hệ. Vì vậy một hệ mới (Water, Wood…) chỉ điền `SwordAuraLook`, không soạn trường cho từng hướng.
   - **Kết nối:**
     - Mô-đun kiếm giữ `SwordAura` (phần chung) như `BladeSet` và `SwordImpostors`: host tạo một bản dùng chung rồi truyền cho `sword-skills.ts` và `myriad-swords.ts`. Nó chạy cả khi `setElement(kit, null)` không có `ElementStage`.
     - `ElementStage` không giữ hào quang; hệ chỉ cấp `SwordAuraLook` qua kit.
     - Đổi vũ khí là đổi neo; đổi hệ là đổi uniform hoặc define; không thêm tấm.
     - Fire chuyển phần `sheathAt` vào `swordAura.mode = "flame"`.
     - Đề xuất kèm cho Fire (Q3): thêm vào `BladeLook` trường `heatFrom` (hiện 0,05; đề xuất 0,55) và `char` 0,12 → 0,4. Dải nhiệt khi đó chỉ còn sát mép, lưỡi là thép tối nóng mép.
9. **Gắn với việc gõ.**
   - **Kiếm chờ:** hào quang lớn theo ba bậc của mức gõ (`ChargeFrameArgs.level`; ở phím 1 là ba thanh hiện ở 0,15 / 0,45 / 0,75).
   - **Từ không lỗi:** từ có hạng `perfect` hoặc `flash` (`src/typing/grading.ts`, `gradeOf`) cho một nhịp lóe ≤ 0,9 trong 8 khung ở vòng ngọc lúc phóng. Lab hiện chưa nối hạng; bước 2 nối `gradeOf` vào lượt gõ của lab. Khi chưa có hạng thì không lóe, không lấy mức gõ thay (nếu lấy thì lần gõ đủ nào cũng lóe).
   - **Bản giảm chuyển động:** giữ mức gõ thành một độ sáng đứng yên.
   - Từ phím đúng cuối tới lúc phóng vẫn ≤ 50 ms; hào quang không bao giờ giữ đòn lại.
10. **Thứ tự vẽ.** Pool một mesh nằm ở gốc tọa độ, nên three chỉ xếp theo `renderOrder`:

    | `renderOrder` | Lớp |
    |---|---|
    | 11 | `MantleSheath`, `MantleHull`, `BowWave`, `HairlineRim`, `EchoTrail` (sau lưỡi), lớp lửa của hào quang |
    | 12 | `RingHalo` (đã đẩy ra sau lưỡi theo độ sâu), `SilkTail`, `GuardStreamers`, `SweepSmear` |
    | 13 | `OrbitMotes`, tàn lửa |
    | 14 | `TipStar` |

11. **Kỹ thuật bắt buộc:**
    - Kẹp trước `pow` và chặn `normalize(0)`, vì MSAA ở Ultra làm điểm mẫu ở mép tam giác vượt ±1, sinh NaN.
    - Không cấp phát mỗi khung.
    - Shader mới vào `prewarm`.
    - Shader mới gọi `#include <tonemapping_fragment>` và `<colorspace_fragment>`. Lý do: Low vẽ thẳng ra màn, không qua composer (`Stage3D.render`: bloom tắt thì `renderer.render`); Medium, High, Ultra qua composer có bloom. Các pool của `fxkit.ts` hiện đặt `toneMapped: false` và không gọi tone map; pool mới của hào quang thì gọi.
    - Mọi sàn bề ngang tính bằng px CSS × uniform `uDpr`.
    - Không dùng `discard` để tạo hình cho lớp trộn.
12. **Tiếng.** Bước mẫu không thêm tiếng riêng. Lóe của hào quang trùng khung với âm chiêu sẵn có (phóng, trúng, bay ngang qua 8–12 thanh gần nhất).

## 5. Kế hoạch

### 5.0 Bước 0: bảng hình, phác ý tưởng, anh chọn (chưa có mã game)

1. **Bảng hình tham chiếu**, 6–9 khung cho mỗi hướng, chỉ lấy từ trailer và trang chính thức đã kiểm: Qingxiao (Wuthering Waves 3.6/3.7), Yanqing (Honkai: Star Rail), Wuchen (Naraka), Phàm Nhân Tu Tiên. Mỗi khung ghi nguồn và ngày kiểm. Không dùng khung để chép; chỉ để anh thấy "loại vẻ đẹp" của từng hướng.
2. **Lượt nguồn tiếng Trung** (Bilibili, Zhihu, GameRes) qua ChatGPT Chat, thinking High, và Gemini; Claude kiểm từng nguồn, như hai tệp nghiên cứu hiện có. Kết quả bổ sung vào §2 trước khi gửi anh.
3. **Khung nền:** chụp bằng kịch bản sẵn có (`lab-element-fire.mjs`), `?aura` chưa tồn tại nên là đúng hôm nay: phím 1 lúc bay và phím 7 F90, F140, Metal và Fire, camera chơi, cắt kiếm ở 35 và 100 px, cộng một khung cận cảnh.
4. **Phác ý tưởng A/B/C** bằng ChatGPT (Chat, High) hoặc Gemini, vẽ chồng lên **chính** các khung đó:
   - Thanh kiếm thật được dán lại lên trên bản phác, nguyên điểm ảnh, để công cụ không vẽ lại kiếm.
   - Mỗi hướng: Metal và Fire; phím 1 và phím 7; 35 px, 100 px, cận cảnh.
   - B thêm một dải 4–5 khung liên tiếp (bay thẳng, rẽ, bổ), vì ý của B nằm ở chuyển động.
   - Theo luật "ba lần không lên thì bàn lại": bản phác nào hỏng ba lần thì dừng, xem lại đề bài.
5. **Gửi anh:** bảng hình, các bản phác, câu hỏi §7. Anh chọn một hướng.
6. **Nếu anh muốn xem chuyển động trước khi chọn:** một phép thử rẻ, một commit sau cờ `?aura`: chỉ thẻ `MantleSheath` Metal ở phím 7, hoặc chỉ `EchoTrail`. Không đi bước 1–8 cho cả ba hướng.

Ảnh nền và bản phác vào `games/immortality-cultivation/tmp/shots/sword-aura/concept/`, không vào Git.

### 5.1 Công tắc (sau khi anh chọn)

- **URL:** `?aura=off|<hướng>`. Mặc định `off`, tức giống hệt hôm nay.
  - Tên mã: `a` = `wind-silk-mantle`, `b` = `echo-cascade`, `c` = `celestial-regalia`. Chỉ hướng được chọn có mã.
- **Bảng điều khiển:** một ô chọn "Aura" cạnh ô "Element".
- **Phím:** `A` bật tắt hào quang (chưa dùng trong lab; đã dùng: 0–7, B, R, W, E, Z, =, -).
- **Lệnh lab:**
  - `__lab.aura(id)` đặt hướng;
  - `__lab.auraLayer(name, on, intensity)` bật tắt từng lớp, để chấm riêng từng lớp như skill hero-presence bước 5.
- **Giảm chuyển động:** `?motion=reduce` qua `resolveReducedMotion` sẵn có (`src/ui/skin.ts`; nó đọc cờ URL, rồi cài đặt, rồi `prefers-reduced-motion`). Game dùng cùng hàm đó qua dòng "giảm chuyển động" của bảng Settings (`docs/games/IN_GAME_SETTINGS.md`), không dùng `screen.intensity`.
- **Bay mẫu một thanh:** `__lab.auraSolo()`, kịch bản 6 s:
  - một thanh Clear Wind đủ chờ sau vai 1 s trong lúc gõ;
  - phóng, bay chữ S 2 s ở 18 m/s, cao 1,2–2 m;
  - rẽ gắt 120°, bổ xuống một con thú;
  - bay lên, về tay, tan.
  - Đồng hồ cố định, nên lần chụp nào cũng như nhau.

### 5.2 Dựng trên hệ thống sẵn có

| Hệ thống | Dùng cho | Thay đổi |
|---|---|---|
| `sword-material.ts` | Bảng bề ngang lưỡi; mặt nạ đo | `edgeField` giữ lại mảng `half[]` (hiện bị bỏ) và xuất `bladeProfile()`; một `DataTexture` 96 × 1 cho mỗi vũ khí. **Không** đổi đường mép. Đề xuất Fire `heatFrom` sau cờ `?bladeHeat=edge` (Q3). Mặt nạ vòng ngọc theo hình học chỉ khi anh duyệt Q4 |
| `real-swords.ts` | Kiếm xa của hướng được chọn; bóng của B | `iFx` từ vec2 thành vec3 (glow, flash, **trọng số hào quang**, mặc định 0); chỉ `myriad-swords.ts` đẩy 1, nên vòng 16 kiếm cổng trời của K5 (`gateSwords`, `depthTest` false) không đổi. Nhánh hào quang giải tích theo define của hướng: áo (A), sóng mũi (B), chấm O và viền (C), dùng `profile` và `rollWidth`; nới lề quad khi trọng số > 0. Không nhân `SWORD_LIGHT`. B: chế độ `"echo"` cho `SwordImpostors` (tham số constructor): màu phẳng, chỉ lưỡi (`m.g`), cắt viên nang theo đốc và mũi hiện tại của từng instance |
| `scripts/models/blender/bake_sword_impostor.py` | Meta | Chỉ thêm vào `clear-wind-impostor.json`: `ringU`, `ringR`, `rollWidth`. **Không** có atlas hào quang mới; atlas màu đã duyệt giữ nguyên |
| Mới: `src/view/skills/sword-aura.ts` | Phần chung | `SwordAura` (chủ: `begin / push / end` như `SwordImpostors`, đếm mật độ, bảng tư thế 94 × 2), `SwordAuraCards` (thẻ instanced, một lệnh vẽ cho mọi thanh; hàm hình theo hướng), `SwordAuraHull` (vỏ ngược, chỉ A), `SwordAuraSprites` (pool premultiplied mới: sáng và mực trong một shader, quỹ đạo trong vertex shader từ bảng tư thế, có tone map, lá flipbook cho sao lửa; chỉ C), `SWORD_AURA_LOOK` và `applySwordAuraLook` |
| Mới: **một trong** `aura-mantle.ts`, `aura-echo.ts`, `aura-regalia.ts` | Hướng được chọn | Bộ lớp hình, `enabled`, `intensity`, cách giảm chuyển động cho từng lớp, bề ngang và sàn |
| `fxkit.ts` `RibbonPool` | `SilkTail` (A), `GuardStreamers` (C) | Một chương trình premultiplied duy nhất với thuộc tính `aMode` theo từng dải: `light` (ghi alpha 0, nên ra đúng như cộng sáng hôm nay), `silk` (thân `silkLight`, mép `silkDeep` alpha thật), `flame` (như `setFlame` hôm nay, theo dải thay vì cả pool). Vẫn một lệnh vẽ. Kiểm parity Metal bằng `lab-element-parity.mjs`. Nếu không đạt parity: pool lụa riêng, +1 lệnh vẽ, sửa bảng chi phí |
| `fxkit.ts` `BeamPool`, `SpritePool` | Tia sau đốc | Không đổi pool; tia đổi màu, thành hai đường kẻ, hoặc bị bỏ theo bảng §4.6 |
| `src/view/trails.ts` | Không dùng | **Không chạm.** Đây là vệt và quầng của "Vạn kiếm" cũ (`src/view/swords.ts`, do `src/view/fx.ts` dùng trong bản chơi), không thuộc hệ kiếm chiêu |
| `element-kit.ts` | Hợp đồng | `SwordAuraLook`, `ElementKit.swordAura` |
| `element-metal.ts`, `element-fire.ts` | Chất | Điền `swordAura`. Fire bỏ `sheathAt` ở `waiting`, `travel`, `streamTravel` khi hào quang bật; giữ tàn lửa; áp trần ≤ 14 thanh có lưỡi lửa |
| `element-stage.ts` | — | Không đổi |
| `src/lab/skills-main.ts` (host) | Lab | Tạo một `SwordAura` dùng chung, truyền cho `sword-skills.ts` và `myriad-swords.ts`; `?aura`, ô chọn, phím `A`, `__lab.aura*`, `prewarm`, `__lab.bladeKeep()` (§6), `resolveReducedMotion`, nối `gradeOf` |
| `myriad-swords.ts` | Phím 7 | `drawSwords` đẩy từng thanh vào hào quang (tâm, hướng, chiều dài, tầng, độ sáng sóng, độ tan, bổ xuống); thay tia và dải theo §4.6; C: capacity `RibbonPool` 6 → 12 |
| `sword-skills.ts` | Phím 1, sau đó các chiêu Kiếm | Kiếm bay và kiếm chờ sau vai đẩy vào hào quang; thay `twinkle`, dải sáng, dải lụa theo §4.6; sau đó K2, K4, K5 |
| `blades.ts` | Neo | `AuraAnchors` đo lúc nạp; vỏ thấp đa giác cho `MantleHull` (chỉ A) |
| `src/view/bench/meter.ts` | Đo | `GpuTimer` sẵn có (`EXT_disjoint_timer_query_webgl2`) bọc từng lệnh vẽ của hào quang trong lab, để đo chi phí từng lớp |
| Mới: `scripts/visual/scenarios/lab-sword-aura.mjs` | Chụp và đo | `PLAN=owner`, `sheet`, `gates`; `lab-element-perf.mjs` thêm biến `AURA` |
| Mới: `tests/view/sword-aura.test.ts` | Kiểm thử | Hợp đồng, kẹp thân ≤ 0,85, sắc màu, số lớp sống theo §4.6, không cấp phát |

### 5.3 Thứ tự commit trong `games/immortality-cultivation` (chỉ hướng anh chọn)

Một commit một bước. Sau mỗi bước, `tsc`, `pnpm test` và `pnpm build` phải xanh. Lab không vào `dist`.

1. **Hợp đồng:** `SwordAuraLook`, `ElementKit.swordAura`, `AuraAnchors`; điền Metal và Fire. Chưa đổi hình nào: `?aura=off` giữ nguyên hôm nay, kiểm bằng `lab-element-parity.mjs`.
2. **Phần chung:** bảng bề ngang lưỡi, `sword-aura.ts` (phần hướng cần), host tạo `SwordAura`, công tắc `?aura`, ô chọn, phím `A`, `prewarm`, `__lab.bladeKeep()`, `?motion=reduce`, `gradeOf`, đo `GpuTimer` từng lớp.
3. **Dải** (A và C): chương trình `RibbonPool` có `aMode`; parity Metal.
4. **Impostor:** trọng số hào quang theo instance, nhánh giải tích, meta `ringU`/`ringR`/`rollWidth`; B thêm chế độ echo. Kiểm parity K5 với `?aura=<hướng>`.
5. **Hướng, Metal.**
6. **Hướng, Fire:** chia tầng, trần lưỡi lửa, thay `sheathAt`.
7. **Bay mẫu và kịch bản chụp:** `__lab.auraSolo()`, `lab-sword-aura.mjs`, biến `AURA` của `lab-element-perf.mjs`.
8. **Changelog** `docs/changelog/<date>-lab-sword-aura.md` (`<date>` dạng YYYY-MM-DD): ảnh trước và sau, số đo, các điểm nhìn để anh quyết.

### 5.4 Người làm, media và ảnh chụp

- Claude dựng trong lab, theo bước 1–8.
- Texture vệt khí của A (nếu chọn A) làm qua `game-art-pipeline`, có mẫu cho anh duyệt trước khi dùng.
- Media (ảnh, texture, video) không vào Git.
- Ảnh chụp vào `games/immortality-cultivation/tmp/shots/sword-aura/`. Khung thô được tỉa bằng `node tools/capture-prune/prune.mjs <folder> --apply` sau khi chấm, chỉ giữ tấm ảnh, video và JSON.
- Mọi lượt GPU chạy qua `.local/bin/heavy.sh --gpu` (đo hiệu năng dùng `--perf`), một lượt mỗi lúc.

### 5.5 Kế hoạch chụp cho anh (sau khi dựng hướng đã chọn)

**Thông số chung:**
- Lượt chính: High, 1920 × 1080, 60 khung/s, DPR ghim 1, đồng hồ cố định.
- Lượt phụ cùng khung: High DPR 2; Medium; **Low (không bloom, vẽ thẳng ra màn)**.
- Có tiếng: bus tiếng của lab.
- Chữ chú thích tiếng Anh in trên video, dạng "Wind-Silk Mantle · Metal · key 7 · play camera".

**Video** `owner-aura-<a|b|c>-<date>.mp4`, khoảng 50 s. Cả Metal lẫn Fire, mỗi hệ năm cảnh:
1. Một thanh bay mẫu (`__lab.auraSolo`) ở cận cảnh, camera xoay chậm 30° trong 6 s, để thấy hào quang cả lúc nhìn ngang lẫn lúc kiếm chĩa vào camera.
2. Phím 1 ở camera chơi.
3. Phím 1 ở cận cảnh (zoom D57).
4. Phím 7 ở camera chơi.
5. Phím 7 ở cận cảnh.

Thêm một video `owner-aura-off-<date>.mp4` cùng các cảnh, làm mốc so (hôm nay).

**Tấm ảnh tĩnh** cho mỗi hệ:
- **Hàng:** kiếm cắt ở 35, 70 và 130 px, lấy từ phím 7 F90 và F140, gom F180, và một khung bay của phím 1.
- **Cột:**
  - đá sáng `#d6d0c2`;
  - nền giữa `#7c848b`;
  - nền tối `#2a2c30`;
  - ảnh xám của nền giữa;
  - Low (không bloom) trên nền giữa.
- **Thêm** một cặp cùng khung, hào quang tắt và bật.
- **Thêm** một cột 100 px với câu hỏi cho giám khảo: "Có đọc thành một viền phát sáng chung chung không?" và "Có nhận ra vòng O và hai rãnh nhập một ở mũi không?"
- **Fire thêm** một tấm so với "tấm ván cháy": cùng khung phím 7 khi bật lại vỏ lửa cho kiếm sông bằng một cờ lab tạm (lượt Fire trước không giữ ảnh của lỗi này).
- Bản 1080p và bản 720p.

**Gửi anh:** video hướng đã chọn, video mốc và các tấm ảnh. Tấm cho giám khảo mù không in số đo.

### 5.6 Sau khi dựng

1. Dựng hướng đã chọn cho mọi chiêu Kiếm: K0–K5, thiên kiếm, kiếm cắm đất. Giữ `off`.
2. Đo lại đủ cổng §6.
3. **Lượt chấm hướng ở lab:** trước lượt chấm, đặt mặc định của lab thành hướng đã chọn (không cần cờ URL), ghi rõ đây là lượt chấm hướng ở lab. Hai giám khảo mù chấm riêng, so với mốc thương mại.
4. **Lượt nghiệm thu 8,5** chỉ làm khi chiêu đã vào bản build chơi: cài đặt của người chơi, không cờ URL.
5. Khi cả hai giám khảo cho ≥ 7, gửi anh video demo, rồi tiếp tục tới 8,5. Không có lượt "tạm được".
6. Ba lần làm lại mà điểm không lên thì dừng, cùng ChatGPT tìm cách khác (gửi clip, ghi chú giám khảo, những gì đã thử) trước lần thứ tư.
7. Water dùng đúng bộ hình đã chọn, chỉ đổi chất. Pass méo dùng chung dựng cùng Water.

## 6. Cổng

| Cổng | Ngưỡng | Đo bằng |
|---|---|---|
| Thời gian khung | Mốc: phím 7 săn 10,2–10,5 ms, nhát kết 10,3–10,9 ms. **Metal:** hào quang trừ `off` ≤ **+0,6 ms** p95 lúc săn (mục tiêu ≤ +0,45) và ≤ **+0,5 ms** ở gom và nhát kết (F168–207). **Fire:** (Fire hào quang − Metal hào quang) tính vào trần 0,85 ms của Fire, phần thân và vật bay ≤ 0,20 ms. Không cửa sổ nào (nghỉ, phím 7 săn, gom, nhát kết, K5, phím 1) có trung vị p95 vượt **11,5 ms**, cả Metal lẫn Fire | `lab-element-perf.mjs` với `AURA=off,<hướng>` xen kẽ: 7 vòng × 3–5 lượt, DPR ghim 1, máy rảnh, qua `heavy.sh --perf`. Báo trung vị và trung bình p95. Vì nhiễu p95 giữa các vòng tới ±1,5 ms, chi phí **từng lớp** đo bằng `GpuTimer` bọc từng lệnh vẽ của hào quang (trung vị trên ≥ 600 khung); nếu trình duyệt không có extension thì bật tắt từng lớp với nhiều vòng hơn. Báo thêm một lượt DPR 2, DPR trung bình của độ phân giải động, và Ultra (không chặn) |
| Từ phím tới lúc phóng | Không đổi: VFX 0 ms, thân 33 ms, cổng ≤ 50 ms. Khung chậm nhất của lần phóng đầu ≤ 50 ms (hiện 46) khi đã `prewarm` | `lab-power.mjs PHASE=latency`; trang mới mở |
| Không NaN | Không NaN hay Inf trong bộ đệm sáng của bloom | Quét ≥ 2.000 khung, mọi chiêu, High và Ultra (MSAA 4), camera chơi và cận cảnh |
| Kiếm đọc được | Phần điểm ảnh lưỡi giữ màu (ΔE OKLab ≤ 0,04 so với `off` cùng khung): ≥ 90 % ở kiếm chủ và kiếm giữa, ≥ 85 % ở kiếm xa. Vòng ngọc và chắn mây ≥ 95 % ở **từng khung**. Không lớp nào phủ > 10 % lưỡi (chớp ≤ 3 khung: 20 %); bóng của B phủ lưỡi, chắn, vòng ngọc ≤ 3 %. Ảnh xám ở 40–100 px vẫn thấy lưỡi, vòng ngọc, chắn. "Thấy tua" chỉ đòi ở kiếm cầm tay, nơi có vẽ tua | `__lab.bladeKeep()`: cùng khung cố định vẽ hai lần (`off`, rồi bật). Mặt nạ lưỡi, vòng ngọc, chắn lấy từ một lượt vẽ mã màu theo **hình học**: dải y đơn vị `ring.y ± ring.r` và `guardFrom … bladeFrom` của `AuraAnchors`; kiếm xa theo `guardU`, `bladeFromU`, `ringU` của meta (không dùng mặt nạ `JADE` theo sắc, vì vòng ngọc hiện ra bạc). Đo độ phủ **khi tắt bloom**, rồi một số riêng khi bật bloom (bloom của lõi loang lên lưỡi). Nếu Q3 được duyệt, mốc so là `off` có cùng cờ `?bladeHeat`. Lấy mẫu phím 7 F60–F160 mỗi 10 khung, gom F168–207, và phím 1 lúc bay. Giám khảo xem ảnh xám |
| Chữ gõ đọc được | Phần điểm ảnh gần trắng (độ sáng > 0,92) ở 70 % trên của khung ≤ `off` + 0,15 % mỗi khung. Khi vào game: tương phản thẻ chữ ≥ 7 : 1 ở p99. Hào quang thêm ≤ 10 % độ sáng trong vùng chữ | Như phép đo Fire (changelog Fire phần 2); trong game, thanh chữ là DOM ngoài canvas |
| Nền sáng, nền tối | Đá `#d6d0c2`: phần "nhạt" ≤ 10 % điểm ảnh hào quang. Nền `#2a2c30`: phần điểm ảnh hào quang tối hơn nền quá 0,05 độ sáng ≤ 20 % (không vành đen). Đường viền kiếm tương phản với nền **cao hơn** khi bật | Ba nền như phép đo Fire |
| Bloom và trắng xóa | Điểm ảnh > 1 do hào quang thêm ≤ +0,3 % khung (`__lab.bright`, HdrProbe). Độ sáng ≥ 0,95 ≤ 6 % sân lúc đỉnh. Riêng hào quang, khi không có chiêu nào khác, ≤ 1 % | Ba nền, camera chơi và cận cảnh |
| Không bloom và DPR | Ở Low (không bloom), giám khảo vẫn đọc ra hào quang và dấu Clear Wind. Bề ngang hào quang theo px CSS không đổi quá 10 % khi DPR trôi 1 → 2 | Tấm Low; cùng khung ở DPR 1 và 2, đo bề ngang |
| Màu | Không điểm ảnh nào gần `#FF4A4A`. Điểm ảnh hào quang trong ±6° sắc và ±0,1 độ sáng của `#FFB020`, `#FFC83A`, `#7FF5E0` ≤ 3 % | Bản đồ điểm ảnh sau tone map |
| Lửa liếm | Kiếm chủ và kiếm phím 1: đầu lửa vượt viền ≥ 3 px ở kiếm 35 px, ở ≥ 60 % khung lấy mẫu. Kiếm giữa có lưỡi lửa: như trên. Kiếm xa: có viền than đứt khúc ≥ 1 px, khác Metal ở dáng chứ không chỉ ở màu (giám khảo phân biệt được ở ảnh xám). Số thanh có lưỡi lửa ≤ 14 mỗi khung. Thân lửa sau tone map: sắc 15–30°, bão hòa ≥ 0,5; hổ phách ≤ 15 % điểm ảnh hào quang. Giám khảo gọi ra "lửa" không cần tên, và không gọi dòng sông là "tấm ván cháy" khi so với tấm cũ | Bản đồ điểm ảnh khung cố định; phép thử màu Fire sẵn có; đếm trong lab |
| Chồng lớp | Trong vùng mỗi kiếm: ≤ 2 lớp trong suốt ở mọi điểm ảnh, đo ở khung đỉnh (F60–F160 và gom). Cả sân: báo theo VFX_STANDARD §3.7 (không chặn cho tới khi anh trả lời Q6) | Một lượt đếm chồng lớp, ghi vào `meta.json` của lượt chụp |
| Thay, không chồng | Số lớp sống ở mỗi chỗ đúng như bảng §4.6 | `tests/view/sword-aura.test.ts` |
| Mượt | Không lớp nào nhảy alpha hay cỡ quá 30 % trong một khung ngoài chớp. 60 Hz và 120 Hz giống nhau. Đứng yên khi dừng hình | Motion probe của lab; một clip nửa tốc độ |
| Metal `off` không đổi | `?aura=off` trùng khít điểm ảnh với bản trước, cả phím 1, phím 7 và K5 | `lab-element-parity.mjs` |
| K5 không đổi | Với `?aura=<hướng>`, vòng kiếm cổng trời của K5 trùng khít với `off` | `lab-element-parity.mjs`, khung K5 |
| Mã | `tsc`, `pnpm test`, `pnpm build` xanh; grep `dist` không thấy mã lab hay mã hào quang của lab | Như các lượt trước |

## 7. Câu hỏi cho anh

- **Q1. Hướng nào:** A (Wind-Silk Mantle), B (Echo Cascade) hay C (Celestial Regalia)? Anh trả lời sau khi xem bảng hình và các bản phác ở bước 0. Nếu anh muốn thấy chuyển động trước khi chọn, Claude làm một phép thử rẻ (§5.0 mục 6). Claude nghiêng về A (§3.D, là ý kiến).
- **Q2. Metal cũng đổi.** Lớp hệ từng hứa "Metal không đổi". Nhưng thanh kiếm anh chê là chính bộ Metal, nên hào quang phải áp cho Metal. Anh đồng ý chứ? Bản `off` vẫn giữ để so.
- **Q3. Lưỡi Fire.** Đề xuất bớt dải cam trên mặt lưỡi: lưỡi thành thép tối nóng mép, còn lửa liếm **quanh** lưỡi, thay cho cả thanh cam như sắt nung. Việc này đổi hình lưỡi Fire đã chụp. Anh đồng ý chứ?
- **Q4. Vòng ngọc.** Model Tripo hiện cho vòng ngọc màu bạc như crôm, trong khi ảnh đã duyệt là ngọc trắng viền vàng. Hướng nào cũng làm vòng ngọc nổi hơn (C nhất). Sửa nghĩa là đổi model đã duyệt, nên cần anh cho phép, và không phải việc nhỏ:
  - mặt nạ `JADE` hiện chọn theo sắc trên texture màu, không bắt được vòng crôm;
  - cách làm đề xuất: mặt nạ vòng ngọc theo hình học trong `sword-material.ts` (dải `ring.y ± ring.r`), cho màu ngọc trắng viền vàng nhạt, giữ sắc và độ sáng xa vàng tiền `#FFC83A`; nếu không đạt thì vẽ lại texture qua `game-art-pipeline`;
  - gửi anh ảnh trước và sau rồi mới quay mẫu.
- **Q5. Ngân sách.** Metal: hào quang ≤ +0,6 ms lúc săn, ≤ +0,5 ms ở nhát kết. Fire: phần hơn Metal tính vào 0,85 ms của Fire. Mọi cửa sổ ≤ 11,5 ms. Đúng ý anh không?
- **Q6. Chồng lớp.** ELEMENT_LAYER §5 cho tối đa 2 lớp trong mờ ở một điểm ảnh, trong khi VFX_STANDARD §3.7 cho High trung bình ≤ 3, đỉnh ≤ 8 trên cả sân. Ở dòng sông phím 7, kiếm cắt qua nhau và các lớp hệ sẵn có đã chồng. Anh muốn giữ "≤ 2 ở mọi điểm ảnh" cho cả sân, hay "≤ 2 trong vùng mỗi kiếm" và cả sân theo VFX_STANDARD? Cho tới khi anh trả lời, cổng là "≤ 2 trong vùng mỗi kiếm" và cả sân chỉ báo cáo.

**Câu kỹ thuật Claude tự quyết theo đề xuất, có báo lại** (anh giao quyền theo đề xuất, 27/10):
- **Smear trên đỉnh của lưới thật** (B4 của tài liệu kỹ thuật): **không dùng**. Thanh kiếm đã duyệt không bị biến dạng; B chỉ dùng mảng quét tách rời.
- **Vỏ thấp đa giác cho `MantleHull`:** dựng trong Blender một vỏ vô hình 200–600 tam giác chỉ bọc lưỡi. Nó mang ánh sáng, không phải kiếm thay thế. Nếu không đạt thì tính pháp tuyến mượt lúc nạp cho LOD.
- **Quầng kiếm xa tính giải tích** từ bảng bề ngang lưỡi, không nướng atlas hào quang: ô 512 px với dải SDF ±16 px chỉ còn ±1–2 px trên màn ở 35–60 px, không chứa nổi áo hay lưỡi lửa.
- **Pass méo dùng chung:** dựng cùng Water như đã định; không hướng nào cần nó ở bước mẫu.
- **Giảm chuyển động:** `resolveReducedMotion` sẵn có, không dùng `screen.intensity`.

## 8. Phản biện đã xử lý (03/11/2026)

Một người phản biện độc lập đọc bản đầu và đưa 30 điểm. Claude kiểm từng điểm trên mã và nguồn. Kết quả:

| # | Điểm phản biện | Kết quả | Lý do, chỗ sửa |
|---|---|---|---|
| 1 | Bóng của B dài 1,0 `L` mà chỉ cách 0,35–0,7 `L`, nên luôn phủ chắn, vòng ngọc, gốc lưỡi | Đã sửa | Đúng theo số học. Bóng chỉ là lưỡi (0,62 `L`), chọn theo quãng đường (bóng 1 cách 1,1 `L`, sau đó 0,7 `L`), cắt viên nang quanh thanh thật; cổng phủ ≤ 3 % và ≤ 2 lớp (§3.B, §4.1, §6) |
| 2 | `SilkTail` không có sẵn ở phím 7 và ở Fire; `RibbonPool` cộng sáng, không vẽ được `silkDeep` | Đã sửa | Đúng: `startSilk` chỉ ở `sword-skills.ts`; Fire `silk: false`; `setFlame` đổi cả pool; vật liệu sáng `ONE, ONE`; `silkDeep` chưa dùng. Chọn cách (a): chương trình premultiplied có `aMode` theo dải, dự phòng pool riêng +1 lệnh vẽ (§3.A, §3.C, §5.2) |
| 3 | Thiếu bảng "lớp hiện có → giữ / thay / bỏ" | Đã sửa | Thêm bảng ở §4.6 và phép thử đếm lớp. C khác mặc định của phản biện: hai dải ở chắn thay **cả** dải sáng lẫn dải lụa (mang màu tua), để chỗ hai dải bện không chồng thành 3 lớp với dải lụa |
| 4 | Câu "~90 tấm lửa hôm nay" sai; A Fire gắn lại lưỡi lửa cho 88 thanh sông | Đã sửa | Đúng: `streamTravel` chỉ vẽ `sheathAt` cho cls 0. Sửa câu; A Fire chia tầng (lưỡi lửa ở kiếm chủ và ≤ 8 kiếm giữa, áo than, viền than), trần ≤ 14 thanh, tấm so "tấm ván cháy" (§3.A, §5.5, §6) |
| 5 | Atlas SDF ±16 px không chứa nổi áo hay lửa ở kiếm xa; quad chỉ vượt mũi 0,038 `L` | Đã sửa | Đúng: ô 512 px, `u1` 0,965. Bỏ atlas hào quang, tính quầng giải tích từ `profile` + `rollWidth`, nới lề quad, ghi rõ mũi kim kiếm xa (chỉ ≥ 60 px) và dáng Fire kiếm xa; kiếm xa vào cổng "Lửa liếm" (§3.A, §5.2, §6) |
| 6 | Mốc p95 ghi thấp; cổng chỉ đo lúc săn; trộn ngân sách Metal và Fire; nhiễu p95 không tách được lớp nhỏ | Đã sửa | Đúng theo hai changelog. Mốc 10,2–10,9 ms; cổng riêng cho gom và nhát kết (+0,5 ms); Fire tính vào 0,85 ms; đo từng lớp bằng `GpuTimer` (§1.2, §6, Q5) |
| 7 | `SpritePool` cộng sáng, không tone map, không vẽ được mực; phím 7 không có pool "glow" | Đã sửa | Đúng. Thêm pool `SwordAuraSprites` premultiplied, quỹ đạo trong vertex shader, có tone map, lá flipbook cho sao lửa. Chi phí C là +3 lệnh vẽ (không phải +4) vì dải đôi đi vào `RibbonPool` có chế độ; +4 nếu pool riêng (§3.C, §5.2) |
| 8 | `trails.ts` là của "Vạn kiếm" cũ trong bản chơi | Đã sửa | Đúng (`src/view/swords.ts` qua `src/view/fx.ts`). Không chạm `trails.ts`; dùng `RibbonPool` mở rộng vì nó đã nhận đầu vệt tùy ý và lấy mẫu theo thời gian thế giới (§5.2) |
| 9 | Lý do nghiêng về A tự mâu thuẫn với bảng | Đã sửa | Đúng. Viết lại lý do, đưa sau bảng so sánh, ghi là ý kiến (§0, §3.D) |
| 10 | Metal của A dễ thành viền phát sáng chung chung | Đã sửa | Đồng ý. Thêm dấu "align → shear" (mảnh so le, khe, trượt cắt), mép mây, texture vệt khí vẽ tay qua `game-art-pipeline`; cột câu hỏi riêng trong tấm ảnh (§3.A, §5.5) |
| 11 | Không hướng nào mang "hai rãnh nhập một ở mũi" | Đã sửa | Đúng (WEAPON_DESIGN §6). A: hai đường may hội về mũi kim; B: đỉnh V sóng mũi; C: hai viền kim hoàn hội ở sao mũi (vẽ ngoài viền, không theo gợi ý "vạch kép" của phản biện vì vạch đó sẽ nằm trên mặt lưỡi); cổng giám khảo (§0, §3, §5.5) |
| 12 | `RingHalo` cắt ngang lưỡi, chuôi, chắn; cùng mặt phẳng lưới; không luôn tròn | Đã sửa | Đúng (kiếm chờ lăn ±0,75 rad cộng `faceRoll`). Quad hướng camera, đẩy ra sau 0,05–0,08 m, cắt nét ở bóng dáng kiếm, cổng ≥ 95 % từng khung (§3.C, §6) |
| 13 | Số liệu `BowWave` tự mâu thuẫn; dài quá lưỡi | Đã sửa | Đúng (lưỡi 0,62 `L`). Định nghĩa cánh là đường cách đều từ `profile`, dài ≤ lưỡi − 0,05 `L`, góc suy ra (~5°), vẫn trong quad (§3.B) |
| 14 | B đổi đường mép trên lưỡi (× 1,4) | Đã sửa | Đúng. Bỏ hệ số; điểm nhấn ở đỉnh V ngoài viền (§3.B, §5.2) |
| 15 | Kiếm bay không có tua; mặt nạ `JADE` theo sắc; bloom loang lên lưỡi | Đã sửa | Đúng. Mặt nạ hình học, đo khi tắt bloom và riêng khi bật, "thấy tua" chỉ ở kiếm cầm tay, mốc cùng cờ `?bladeHeat` (§1.2, §6) |
| 16 | `AuraLook` chứa phần hình; ghi chú "body ≤ 0,85" sai với dải màu hiện có | Đã sửa | Đúng. `SwordAuraLook` chỉ còn chất; bề ngang, sàn, màu sao/vòng/bóng sang mô-đun hướng, lấy từ vai của dải màu; `applySwordAuraLook` kẹp thân (§4.8) |
| 17 | `SwordAura` không nên nằm trong `ElementStage` | Đã sửa | Đúng (`setElement(kit, null)` chạy được khi không có stage). Mô-đun kiếm giữ, host tạo và truyền (§4.8, §5.2) |
| 18 | Define trong `real-swords.ts` bật quầng cho cả K5 | Đã sửa | Đúng (`gateSwords`, `depthTest` false). Trọng số hào quang theo instance trong `iFx` (vec3), chỉ phím 7 đẩy 1; cổng parity K5 (§5.2, §6) |
| 19 | Hổ phách `#FFB703` sát vàng tiền và cam khẩn, ngoài dải 15–40° | Đã sửa | Đúng (43° so với 43° và 39°). Thân 15–30°, hổ phách ≤ 15 %, cổng màu dành riêng ≤ 3 % (§3, §4.4, §6) |
| 20 | Các câu tả mã sai: 0,14 m, Hz, 0,32 s, vỏ lửa kiếm sông, tên móc | Sửa một phần | Đúng với 0,14 m (là bề rộng), rad/s, vỏ lửa kiếm sông, tên móc (`StreamHooks.travel`, `streamTravel` là hàm của Fire). **Không đúng** với 0,32 s: dải lụa phím 1 tắt bằng `ribbons.stop(f.silk, 0.32)` (`sword-skills.ts`); 0,18 s chỉ là mặc định của `RibbonPool.stop`. Đã ghi cả hai (§1.1, §3.A) |
| 21 | Nghiên cứu: hai bên giống nhau do đề; câu Reddit chưa ghi nhãn; thiếu bảng hình; nguồn tiếng Trung để sau | Đã sửa | Đúng (mục A của tệp nguồn liệt kê sẵn các lớp). Sửa §2.1, gắn nhãn §2.2 và §2.6; bảng hình và nguồn tiếng Trung chuyển vào bước 0, trước khi gửi anh. Lượt nguồn tiếng Trung **chưa chạy** trong lần sửa này |
| 22 | Dựng cả ba bằng mã trước khi anh chọn là phí và chạm nhiều pool | Đã sửa | Đồng ý. Thêm bước 0 phác ý tưởng chồng lên khung chụp thật; chỉ dựng hướng được chọn; phép thử chuyển động rẻ nếu anh muốn (§5.0, §5.3) |
| 23 | Thiếu Low, Medium, DPR động; sàn theo `fwidth` phập phồng | Sửa một phần | Đúng với Low (không bloom, vẽ thẳng ra màn), DPR trôi 1–2 ở High/Ultra và sàn. **Không đúng** với Medium: `TT_TIERS.medium.bloom` là true, nên Medium qua composer có bloom. Sửa luôn câu sai tương tự ở §4.11 của bản đầu. Sàn theo px CSS × `uDpr`, chụp Low/Medium/DPR 2, hai cổng mới (§1.3, §4.11, §5.5, §6) |
| 24 | Tự nới luật chồng lớp và cách đếm trần | Đã sửa | Phần lớn đúng. Con số cả sân (trung bình 3, đỉnh 8) có thật trong VFX_STANDARD §3.7, không phải tự đặt; nhưng ELEMENT_LAYER §5 chặt hơn. Giữ ≤ 2 trong vùng mỗi kiếm, đo ở đỉnh, đưa phần cả sân thành Q6; bỏ câu tự quyết về cách đếm trần (§4.6, §6, §7) |
| 25 | Giảm chuyển động và hạng gõ chưa khớp mã; thiếu cột tắt/làm dịu/giữ | Đã sửa | Đúng (`resolveReducedMotion`, `?motion=reduce`, `gradeOf` có `perfect`/`flash`). Mọi lớp có cột giảm chuyển động; không lóe khi chưa có hạng (§3, §4.9, §5.1) |
| 26 | Quầng C giữ HDR 6 khung | Đã sửa | Đúng. Mọi đỉnh HDR chỉ f0–2 ở cả ba hướng (§1.3, §3, §4.3) |
| 27 | Ghi chú `tasselFrom` sai; kiếm xa chưa có nguồn neo | Đã sửa | Đúng. Ghi chú "≤ pommelY"; neo kiếm xa từ `SwordAtlasMeta` + `ringU`, `ringR`, `rollWidth` (§4.8) |
| 28 | Q4 không phải việc nhỏ | Đã sửa | Đúng (model đã duyệt; mặt nạ theo sắc không bắt vòng crôm). Bỏ chữ "nhỏ", ghi cách làm và ảnh trước/sau (§7) |
| 29 | Chỗ giữ chỗ tiếng Việt trong tên tệp; `aura` trùng tên sẵn có | Đã sửa | Đúng (`aura` là `SpritePool` và `updateAura` trong `sword-skills.ts`). `<date>`; `ElementKit.swordAura`, `SwordAuraLook`, `SWORD_AURA_LOOK`, `applySwordAuraLook`, `SwordAuraCards`, `SwordAuraHull`, `SwordAuraSprites` |
| 30 | "Chấm ở cài đặt người chơi, không cờ URL" không làm được trong lab | Đã sửa | Đúng. Lượt chấm hướng ở lab đặt mặc định lab thành hướng đã chọn; nghiệm thu 8,5 chỉ ở bản build chơi (§5.6) |

Thêm do Claude tự thấy khi sửa: bỏ `EdgeThreads` khỏi B (sẽ chồng lên chuỗi bóng thành ≥ 3 lớp); đường may của A ở bản đầu giữ HDR f0–3 (4 khung), nay f0–2.

## Nguồn

Trong repo, đã đọc 03/11/2026:
- [`source/sword-aura-chatgpt-2026-11-03.md`](source/sword-aura-chatgpt-2026-11-03.md):
  - mục A: đề bài (đã liệt kê sẵn các lớp);
  - mục C: câu trả lời sau tự rà soát;
  - mục E: Claude kiểm nguồn (16/17 nguồn chính thức đúng);
  - mục F: đánh giá.
- [`source/sword-aura-gemini-2026-11-03.md`](source/sword-aura-gemini-2026-11-03.md): mục B câu trả lời, mục C kiểm nguồn, mục D đánh giá và ba hướng gộp.
- [`source/sword-aura-tech-2026-11-03.md`](source/sword-aura-tech-2026-11-03.md):
  - lớp A1–A3, B1–B4, C, D, E, F;
  - ba gói kỹ thuật;
  - cách đo, các bẫy, bảng tổng.
- [`ELEMENT_LAYER.md`](ELEMENT_LAYER.md) (§5 ngân sách và chồng lớp, §7 cổng Fire), [`../00-canon.md`](../00-canon.md) (D54–D59, §21.1), [`WEAPON_DESIGN.md`](WEAPON_DESIGN.md) (§6 Clear Wind), [`SKILL_CATALOG_V2.md`](SKILL_CATALOG_V2.md).
- [`VFX_STANDARD.md`](../../VFX_STANDARD.md) §3.1–3.8.
- Skill [`game-vfx-layered`](../../../../.agents/skills/game-vfx-layered/SKILL.md), [`game-hero-presence-vfx`](../../../../.agents/skills/game-hero-presence-vfx/SKILL.md):
  - `references/layers.md`: P1–P10, trạng thái, kiềm chế, giảm chuyển động, bậc;
  - `references/worked-examples.md`: "Tu Tien: flying swords without an aura".
- `games/immortality-cultivation` (`2b09491`), chỉ đọc:
  - `src/view/skills/`: `sword-material.ts`, `real-swords.ts`, `blades.ts`, `fxkit.ts`, `element-kit.ts`, `element-metal.ts`, `element-fire.ts`, `element-stage.ts`, `myriad-swords.ts`, `sword-skills.ts`, `weapons.ts`;
  - `src/view/trails.ts`, `src/view/swords.ts`, `src/view/fx.ts`, `src/lab/skills-main.ts`, `src/lab/tassel.ts`, `src/ui/skin.ts`, `src/typing/grading.ts`, `src/view/bench/meter.ts`, `src/content/rules.ts`, `src/kit/three/stage.ts`;
  - `art-src/lab/models/weapons/clear-wind-impostor.json`;
  - `docs/changelog/2026-11-03-lab-real-swords.md`, `docs/changelog/2026-11-03-lab-element-fire.md`.

Nguồn web: chỉ qua ba tệp nghiên cứu trên, mỗi khẳng định ghi rõ đã kiểm hay chưa. Câu trích fan từ Reddit chưa ai kiểm được, vì Reddit bị chặn trong môi trường này; chúng chỉ là gợi ý, không là bằng chứng.
