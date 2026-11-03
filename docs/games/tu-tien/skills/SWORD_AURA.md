# Hào quang kiếm bay (sword aura): ba hướng cho anh chọn (03/11/2026)

**Trạng thái:** đề xuất, chờ anh xem mẫu trong lab rồi chọn một hướng. Chưa có mã. Mọi con số chi phí là ước tính, chưa đo; cổng thật là số đo ở §6.

**Đầu vào** (đã đọc hết):
- Nghiên cứu các thiết kế được yêu thích, mỗi tệp có bảng kiểm nguồn và đánh giá của Claude:
  - [`source/sword-aura-chatgpt-2026-11-03.md`](source/sword-aura-chatgpt-2026-11-03.md): ChatGPT, Chat, thinking High, có lượt tự rà soát;
  - [`source/sword-aura-gemini-2026-11-03.md`](source/sword-aura-gemini-2026-11-03.md): Gemini 4 Argon, mức Cao.
- Kỹ thuật và chi phí: [`source/sword-aura-tech-2026-11-03.md`](source/sword-aura-tech-2026-11-03.md). Tài liệu đó đọc mã, chưa đo; các mục A1–A3, B1–B4, C, D, E dưới đây là của nó.
- Luật:
  - [`ELEMENT_LAYER.md`](ELEMENT_LAYER.md) (D59);
  - [`../00-canon.md`](../00-canon.md) (D54–D59, §21.1 màu dành riêng);
  - [`WEAPON_DESIGN.md`](WEAPON_DESIGN.md) (Clear Wind) và [`SKILL_CATALOG_V2.md`](SKILL_CATALOG_V2.md);
  - [`VFX_STANDARD.md`](../../VFX_STANDARD.md) §3;
  - skill [`game-vfx-layered`](../../../../.agents/skills/game-vfx-layered/SKILL.md) và [`game-hero-presence-vfx`](../../../../.agents/skills/game-hero-presence-vfx/SKILL.md).
- Mã chỉ đọc, không sửa: `games/immortality-cultivation`, nhánh hiện tại chiều 03/11.
  - Trong `src/view/skills/`: `sword-material.ts`, `real-swords.ts`, `blades.ts`, `element-kit.ts`, `element-metal.ts`, `element-fire.ts`, `element-stage.ts`, `myriad-swords.ts`, `sword-skills.ts`, `weapons.ts`.
  - Ngoài ra: `src/view/trails.ts`, `src/lab/skills-main.ts`.
  - Changelog: `2026-11-03-lab-real-swords.md`, `2026-11-03-lab-element-fire.md`.

## 0. Tóm tắt

| | **A · Wind-Silk Mantle** | **B · Echo Cascade** | **C · Celestial Regalia** |
|---|---|---|---|
| Ý chính | Kiếm **mặc** một tấm áo lụa khí may đo theo lưỡi | Tốc độ **hiện hình**: kiếm kéo theo chuỗi tàn ảnh của chính nó | Kiếm là **bảo vật đội vương miện**: ánh sáng dồn vào mũi, vòng ngọc, chắn mây |
| Pitch | Clear Wind wears a tailored mantle of living qi: it hugs the blade outside its edges, parts around the jade ring, and pours off the pommel into the tassel's silk. | Speed made visible: every sword is chased by flat sword-light echoes of itself that fan open on each turn and snap shut into the strike, while a bow wave splits the air at its tip. | Clear Wind flies as a crowned relic: a star at its point, a slow-turning halo framing the hollow jade ring, twin streamers off the cloud guard and motes in orbit, with the steel left bare. |
| Lớp chính | `MantleSheath`, `MantleHull`, `SilkTail`, `MantleHalo` | `BowWave`, `EchoTrail`, `SweepSmear`, `EdgeThreads`, `StanceEcho` | `TipStar`, `RingHalo`, `GuardStreamers`, `OrbitMotes`, `HairlineRim`, `WaitMandorla` |
| 88 thanh ngoài kiếm chủ | Mọi thanh có áo, thanh xa có quầng trong impostor | Mọi thanh có tàn ảnh và sóng mũi | Chỉ viền mảnh, chấm ngọc, sao trên ngọn sóng sáng |
| Fire hết "sắt nung" nhờ | Lưỡi lửa liếm ra ngoài đường viền, ≥ 3 px ở 35 px | Sóng mũi và tàn ảnh cháy thành lửa phía sau | Vòng lửa quanh vòng ngọc, tua lửa, sao lửa |
| Phím 7, High (ước tính) | +0,07–0,16 ms, +2 lệnh vẽ | +0,10–0,20 ms, +3–4 lệnh vẽ | +0,07–0,13 ms, +3 lệnh vẽ |
| Phím 1 (ước tính) | +0,01–0,04 ms | +0,02–0,05 ms | +0,02–0,04 ms |
| Rủi ro chính | Ở 35–60 px đọc thành thanh kiếm béo và mờ | Tàn ảnh đọc thành "thêm kiếm", dòng sông thành mớ sọc | Dòng sông 88 thanh vẫn gần như trần, đúng lỗi anh vừa chê |

- **Claude nghiêng về A.** Lý do:
  - A là hướng duy nhất mặc cho cả 94 thanh ở cả ba tầng;
  - A sửa thẳng lỗi lửa "sắt nung";
  - A rẻ nhất và giữ thanh kiếm sạch nhất.
  - B đẹp nhất khi kiếm rẽ và bổ xuống. C sang nhất trên 6 kiếm chủ, nhưng yếu ở dòng sông.
- **Bước tiếp:** dựng cả ba trong lab sau một công tắc `?aura=off|a|b|c`, quay video và tấm ảnh như §5.5, gửi anh chọn. Hướng anh chọn mới được dựng cho mọi chiêu Kiếm và đưa hai giám khảo mù chấm.

## 1. Vì sao, và hào quang phải đạt gì

### 1.1 Lời anh và chẩn đoán

Lời anh chiều 03/11, sau khi xem tấm Sword × Fire: "mà vì sao các thanh kiếm đều chưa được xử lý để có hiệu ứng xung quanh thanh kiếm vậy, chứ hiện tại nhìn các thanh kiếm bay kiểu hơi thô, chưa đẹp cho lắm".

Chẩn đoán, ngắn:
- **Sáng 03/11 anh chê kiếm vẽ bằng code.** Lời anh: "bạn có vẻ đang tự style chứ k sử dụng hình ảnh nên hình kiếm đang rất xấu".
  - Lượt kiếm thật vì thế đưa model Clear Wind đã duyệt vào mọi chiêu: lưới đủ 14.728 tam giác, LOD 3.200 tam giác, atlas impostor cho kiếm xa.
  - Cùng lượt đó **bỏ mọi thứ vẽ quanh lưỡi**: thẻ sáng dọc lưỡi, dải "sống" trắng, dải thân sông.
- **Phần còn lại đều nằm trong đường viền:**
  - đường mép trắng nóng ≤ 30 % bề ngang lưỡi, phần duy nhất bloom;
  - rim mềm ≤ 0,9;
  - ánh ngọc;
  - chớp khi trúng.
  - Vệt duy nhất dài 0,14 m và bắt đầu từ đốc.
  - Ở camera chơi, kiếm là một vật kim loại rộng 4–5 px bay trên nền đá. Chưa ai thiết kế một lớp **mặc** cho thanh kiếm thật.
- **Fire đọc như sắt nung**, vì hai chỗ trong mã:
  - Vỏ lửa (`element-fire.ts` `sheathAt`) bị đẩy ra sau lưỡi (`lift = -0.35`) và làm mềm (`blur = 1.8`, `taper = 0.6`), nên chỉ một viền mờ ló ra.
  - Dải nhiệt cam của chế độ `furnace` lại phủ chính mặt lưỡi.
  - Lửa nằm **trên kim loại**, không liếm ra ngoài.

### 1.2 Hào quang phải đạt gì

1. **Thanh kiếm vẫn là Clear Wind thật** và đọc ra chính nó: lưỡi bạc, vòng ngọc rỗng, chắn mây, tua.
   - Hào quang mặc cho kiếm. Nó không che, không thay, không vẽ lại kiếm.
   - Không có hình thay thế nào vẽ bằng code.
2. **Rực rỡ, sống, sang ở camera chơi**, khi kiếm dài 35–130 px ở 1080p (trung vị ~100 px), và ở cận cảnh D57 (kiếm chủ tới ~600 px).
   - Khẩu vị của anh: anime, donghua, thần thoại; có hào quang, cuốn hút, sang, hiện đại, nhiều chi tiết.
   - Không lấy "như thật" làm đích (D56).
3. **Có ở cả ba tầng**: lưới đủ, LOD, impostor. Phím 7 trên High có 6 + 24 + 64 thanh; dòng sông là chính những thanh kiếm ấy.
4. **Hình của vũ khí, chất của hệ (D59).** Mỗi hướng là một bộ **hình**. Metal, Fire, rồi Water và các hệ sau chỉ cấp **chất** cho bộ hình đó (§4.8).
5. **Vừa ngân sách:** cả dòng sông thêm ≤ +0,6 ms p95 ở phím 7 lúc săn trên High; không cửa sổ nào vượt trần 11,5 ms. Hiện p95 là 10,2–10,5 ms.
6. **Anh xem mẫu và chọn trước khi dựng thật.** Sau đó hai giám khảo mù chấm, cổng 8,5. Khi cả hai cho ≥ 7, gửi anh một video demo.

### 1.3 Ký hiệu dùng trong tài liệu

| Ký hiệu | Nghĩa | Giá trị |
|---|---|---|
| `L` | Chiều dài kiếm, đốc tới mũi | Phím 7: kiếm chủ 2,8 m khi rời tay, 3,06 m trên sông; kiếm giữa 2,55 m; kiếm xa 2,3 m. Phím 1: ~2,4 m (2,35 × kiếm tay 1,02 m) |
| `W` | Bề ngang lưỡi chỗ rộng nhất | Đọc từ bảng nửa bề ngang `half[]` của `edgeField` lúc nạp. Ước tính ~4,5 % `L`: 0,14 m kiếm chủ, 0,115 m kiếm giữa, 0,10 m kiếm xa, 4–5 px ở 100 px |
| `px` | Điểm ảnh ở 1080p, DPR 1 | Ở 100 px, 1 px ≈ 0,025–0,031 m |
| `f` | Khung ở 60 Hz | Mọi nhịp chạy theo giây thế giới; số khung chỉ để đọc |
| `ω` | Tốc độ góc của hướng kiếm (rad/s) | "Rẽ" khi ω ≥ 4, đầy khi ω ≥ 10 |
| `v` | Tốc độ bay (m/s) | Sông phím 7 khoảng 15–25 m/s |
| `core` | Lõi HDR mảnh | 2,4–3,6 (như `EDGE_HOT` 3,6); ≤ 1 px ở camera chơi, ≤ 3 px cận cảnh. Phần duy nhất được bloom |
| `glow` | Thân sáng | ≤ 0,85 mỗi kênh trước tone map (luật ≤ 0,9, chừa 0,05) |
| `ink` | Lớp tối premultiplied | rgb tối, alpha 0,25–0,85, nằm trong cùng shader với phần sáng |

Màu đều là tuyến tính, trừ chỗ ghi mã hex sRGB.

## 2. Học được gì từ các thiết kế được yêu thích

### 2.1 Các lớp lặp lại

Cả ChatGPT lẫn Gemini, mỗi bên tự đi tới cùng một chồng lớp, nên kết luận này đáng tin hơn từng bên.

| Thứ tự | Lớp | Ở 35 px | Ghi chú |
|---|---|---|---|
| 1 | Kiếm thật, đục | Còn | Nhận diện: lưỡi, vòng ngọc, chắn mây, tua |
| 2 | Lớp tối đỡ phía sau | Còn | Tách kiếm khỏi nền đá sáng; nằm trong shader của lớp sáng |
| 3 | Vỏ khí theo hệ (≤ 0,9) | Còn | Hình chính của hào quang |
| 4 | Lõi HDR mảnh | Còn | Phần duy nhất bloom |
| 5 | Sao hoặc kim ở mũi | Còn | Cho biết hướng |
| 6 | Đuôi hoặc vây theo tốc độ | Còn | Cho biết tốc độ |
| 7 | Nhịp lóe ở vòng ngọc, tua, tàn ảnh khi rẽ | Mất | Chỉ cho kiếm chủ, từ ~70 px |
| 8 | Hạt, bùa văn, vòng nhỏ, méo không khí | Mất | Thành nhiễu dưới ~90 px |

Ở 35 px chỉ còn sáu điều: có một thanh kiếm thật, một viền tối, một bóng hào quang, một đường sáng mảnh, một mũi rõ, một đuôi cho biết tốc độ (ChatGPT §5).

### 2.2 Vì sao người xem thích

- **Kiếm vẫn là kiếm.**
  - Bản beta của Qingxiao (Wuthering Waves) bị chê là kiếm "less physical and very transparent and overdone, so they all meld together".
  - Đây là câu trích Reddit do ChatGPT đưa, Claude chưa mở được vì Reddit bị chặn. Chỉ dùng làm gợi ý.
  - Qingxiao có thật: Resonator Aero dùng kiếm, ra ở bản 3.6; bản 3.7 nhắc trạng thái "Sword Flight". Claude đã kiểm trên trang của Kuro.
  - Ý này trùng luật của anh: hào quang không được nuốt thanh kiếm.
- **Nhỏ thì tinh, to thì dễ rẻ.** Một bài review Sword of Coming (Reddit, chưa kiểm):
  - khen tàn ảnh và sóng năng lượng tinh tế ở cỡ nhỏ;
  - chê các đòn mưa kiếm năng lượng cỡ lớn là "especially lacklustre".
  - Bài học: không nhân một lớp sáng lên 94 thanh rồi gọi là giàu.
- **Có thứ bậc, cả trong không gian lẫn thời gian.**
  - Đòn mưa kiếm của Wuchen (Naraka) xen kiếm nhỏ với kiếm lớn. Câu "enduring sword rain" Claude đã kiểm trên trang chính thức.
  - Vài kiếm dẫn đầu đủ chi tiết, phần còn lại bơi theo.
  - ChatGPT thêm một luật hay: 6 kiếm chủ thỉnh thoảng phải "chứng minh" cả dòng là Clear Wind, bằng một lần ngọc lóe và tua quất.
- **Ngôn ngữ ngọc, mây, sáng tối.** Bài Developer Insight về Xiao (Genshin, Claude đã đọc) nói ngọc cho cảm giác trường thọ, vải có hoa văn mây cho vẻ cổ, và sáng tối đan nhau trong đòn đánh. Clear Wind có đúng vòng ngọc, chắn mây và tua.
- **Kiềm chế để đọc được.** Trang VFX của Riot (Claude đã kiểm) nói nghệ sĩ mang "heavy burden of restraint": hiệu ứng phải đẹp mà vẫn rõ đòn của ai.

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
- **Atlas impostor theo kênh ngữ nghĩa** là ý hay. Nhưng không cần nung lại atlas màu đã duyệt: chỉ thêm một atlas hào quang riêng (§5.2).

### 2.5 Cả hai cùng thiếu, và tài liệu này lấp thế nào

| Thiếu | Ở đây |
|---|---|
| Lửa phải **liếm**, không như sắt nung | Mỗi hướng có cách riêng để lửa vượt ra ngoài viền kiếm ≥ 3 px ở 35 px; đề xuất bớt dải nhiệt trên mặt lưỡi (§3, câu hỏi Q3) |
| Gắn với việc gõ | Kiếm chờ lớn hào quang theo ba bậc của mức gõ; từ không lỗi cho một nhịp lóe ở vòng ngọc (§4.9) |
| Phép thử chữ gõ vẫn đọc được | Cổng ở §6 |
| Phép thử kiếm vẫn đọc được | Đo phần điểm ảnh lưỡi giữ màu (§6) |
| Cách anh duyệt | Video và tấm ảnh ở 35, 70, 130 px, nền sáng, nền tối, ảnh xám (§5.5) |
| Nguồn tiếng Trung (Bilibili, Zhihu, GameRes, UOD) | Chưa có. Đáng chạy một lượt khi anh đã chọn hướng, để tinh chỉnh hướng đó |

### 2.6 Chọn ba hướng nào, và vì sao

Ba hướng phải khác nhau ở **ý**, không chỉ ở màu:
- **A mặc lên bề mặt:** một lớp liền quanh lưỡi.
- **B dùng thời gian:** quá khứ của đường bay hiện ra.
- **C dùng điểm nhấn:** ánh sáng dồn vào vài "trạm" như đồ trang sức.

| Hướng | Lấy cảm hứng từ | Phần riêng của mình |
|---|---|---|
| A · Wind-Silk Mantle | River-Silk Sheath (ChatGPT) | Áo may từ chính bảng bề ngang đo được của lưỡi; khe cổ áo để trần vòng ngọc; đuôi áo chảy liền vào dải lụa tua (nhận diện Clear Wind); lửa liếm ra ngoài viền |
| B · Echo Cascade | Tàn ảnh bậc thang (Gemini), lời khen tàn ảnh của Sword of Coming, vệt chữ V (Gemini) | Tàn ảnh rỗng tâm, màu phẳng; "bóng tư thế" để lại chỗ phóng; sóng mũi tách khỏi viền, nên 94 sóng mũi tự thành vảy chữ V của cả dòng mà không cần dải cấp dòng |
| C · Celestial Regalia | Sovereign Halos (Gemini), đóng khung ngọc (ChatGPT, Lattice) | Quầng tròn đóng khung đúng vòng ngọc rỗng, dấu chữ ký của Clear Wind (WEAPON_DESIGN §6); tua đôi từ hai mút chắn mây; vầng mandorla khi kiếm chờ sau vai, đúng bộ radiance anh muốn |

Không lấy:
- **Calligraphy Wake / Calligraphic Slipstream:** mực làm ý chính, lý do ở §2.4.
- **Jade Meridian Lattice:** không đọc được ở camera chơi.
- **Dragon-Scale Wake** như một hướng riêng: che mép lưỡi.

Không hướng nào chép hình chữ ký của một game cụ thể:
- không dùng bố trí kiếm hay biểu tượng Heart Sword của Qingxiao;
- không dùng bố cục tuyệt kỹ của Yanqing;
- không dùng nhịp mưa kiếm của Wuchen;
- không dùng chữ Hán hay chữ thư pháp của ai.

## 3. Ba hướng

Chung cho cả ba (chi tiết ở §4):
- Mỗi lớp là một module, có `enabled` và `intensity`.
- Tối và sáng nằm trong cùng một shader, trộn premultiplied.
- Có mức sàn bề ngang theo px.
- Chạy theo thời gian thế giới; không cấp phát mỗi khung; biên dịch sẵn trong `prewarm`.
- Không lớp nào cộng sáng lên mặt lưỡi. Đường mép trắng nóng sẵn có nằm **trong** đường viền và giữ nguyên.

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

**Pitch:** Clear Wind wears a tailored mantle of living qi: it hugs the blade outside its edges, parts around the jade ring, and pours off the pommel into the tassel's silk.

**Ý:** một tấm áo khí may đo theo đúng thanh kiếm, như lụa của một bảo vật đang bay.
- Áo bắt đầu ngay **ngoài** mép lưỡi, nên mặt lưỡi luôn trần.
- Áo hở ở "cổ áo", nên vòng ngọc và chắn mây nằm trong khoảng trống.
- Áo thon thành một mũi kim vượt quá mũi kiếm.
- Phía sau, áo nối liền vào dải lụa tua của Clear Wind.
- Mỗi hệ đổi chất của tấm áo: khí lụa (Metal), lưỡi lửa (Fire), ống nước (Water).

**Nhìn nhanh** (nhìn ngang, mũi bên phải):

```
     silk tail (tassel)          collar gap      mantle: outside both edges, ink hem         needle
  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ (O){    ..:::::::::::::::::::::::::::::::::::::::::::..
                              (O){ ====================== real blade ======================>  - -
                              (O){    '':::::::::::::::::::::::::::::::::::::::::::''
                          ring + cloud guard: bare
```

| Cỡ trên màn | Thấy gì |
|---|---|
| 35 px | Thanh kiếm, mỗi bên 2 px áo sáng, viền mực 1 px, một đuôi ngắn. Đọc thành "kiếm đang tỏa khí", không thành ống sáng |
| 100 px | Áo có dòng chảy từ mũi về đốc, khe cổ áo quanh vòng ngọc, mũi kim, đuôi lụa |
| Cận cảnh | Thêm hai nếp gấp dọc trong thân áo, đường may sáng sát mép, viền vỏ ngược ôm khối 3D ở kiếm chủ, đuôi lụa phấp phới |

**Các lớp:**

| Lớp | Tầng | Hình và cỡ | Ánh sáng | Trộn | Bloom |
|---|---|---|---|---|---|
| `MantleSheath` (A1 `SheathCard`) | Kiếm chủ, kiếm giữa | Thẻ instanced dọc trục lưỡi, từ chắn kiếm tới mũi + 0,12 `L`; kiếm giữa thêm đuôi áo 0,35 `L` sau đốc (kiếm chủ đã có `SilkTail`, nên không có đuôi áo). Khoảng cách tới mép `d = \|x\| − w(y)`, `w(y)` đọc từ bảng `half[]` 96 mẫu. Nửa bề ngang áo `m(y) = widthW · W · p(y)`: Metal `widthW` 0,6 (0,06–0,085 m), Fire 0,5 cộng lưỡi lửa. `p(y)` bằng 0 ở cổ áo, lên 1 sau 20 % lưỡi, xuống 0,7 gần mũi, rồi thành mũi kim dài 0,12 `L`. Sàn 2 px mỗi bên lúc bay đều, 3 px lúc phóng và trúng. Không có thân áo trong dải chắn kiếm (từ đầu chắn tới `bladeFrom` + 0,03 `L`) | Ba vùng trong một shader: (1) đường may `d` < 1 px, glow 0,85, chỉ thành core 2,4 ở f0–3 lúc phóng và lúc trúng; (2) thân glow ≤ 0,85 có hai quãng tám nhiễu cuộn từ mũi về đốc; (3) viền mực ở 30 % ngoài cùng, rgb của hệ, alpha theo `ink.alpha` | Premultiplied; đẩy sau lưỡi 0,08 m theo độ sâu; mềm với mặt đất 0,15 m | Chỉ đường may, chỉ ≤ 4 khung |
| `MantleHull` (A2 `AuraHull`) | Kiếm chủ, High và Ultra | Vỏ ngược phồng 1,5 px + 0,015 m theo pháp tuyến đã làm mượt (`aSmoothNormal`); chỉ phủ lưỡi, không phủ chắn | Cùng hàm chất với A1 | Vẽ mặt sau, `depthWrite` tắt | Không |
| `SilkTail` | Kiếm chủ | Dải lụa tua sẵn có (`startSilk`, `RibbonPool`), được thay kiểu. Dài 0,9 `L` ở phím 1, 0,6 `L` ở kiếm chủ phím 7. Rộng 0,11 → 0,16 m (ở 25 %) → 0,03 m. Rung 15/23 Hz và 11 Hz như hiện tại | Thân trộn 50/50 giữa màu tua `#A9C4EA` × 0,7 và thân của hệ, ≤ 0,7; mép tối chàm `#2E3A78` × 0,55 | Như `RibbonPool` | Không |
| `MantleHalo` (A3 `ImpostorHalo`) | Kiếm xa | Trong shader impostor, đọc atlas hào quang SDF (§5.2): áo 2 px, viền mực 1 px. Đuôi là tia `BeamPool` sẵn có, tô lại màu lụa (thay, không thêm) | Như A1, không nhân `SWORD_LIGHT` | Trên diện tích quad sẵn có | Không |

- Ở kiếm chủ, thẻ và vỏ thay chỗ nhau theo góc nhìn:
  - trọng số thẻ = `smoothstep(0.85, 0.6, |dir·view|)`; vỏ lấy phần còn lại;
  - khi kiếm chĩa vào camera, tấm phẳng không lộ ra và hai lớp không chồng nhau.

**Theo trạng thái:**

| Trạng thái | Áo làm gì |
|---|---|
| Chờ | Bề ngang theo mức gõ ba bậc: 0,4 / 0,7 / 1,0. Thở chu kỳ 2,4 s, ±8 %. Dòng chậm, 0,15 `L`/s, theo luật của hệ (Fire bốc lên theo trục thế giới). Đuôi lụa thả trôi |
| Phóng | Áo mở từ cổ tới mũi trong 4 khung; f0 đã có 25 % đầu sáng đủ. Đường may core 2,4 ở f0–3, về glow ở f8. Bề ngang vọt 1,3× rồi lắng về 1,0 ở f18 |
| Bay đều | Bề ngang 1,0. Dòng chảy 0,6 + 0,04 `v` chiều dài lưỡi mỗi giây. Đuôi lụa duỗi |
| Rẽ | Bên ngoài đường cong nở tới 1,6×, bên trong co 0,7×, theo dấu của độ cong. Hai nếp gấp sáng ×1,2. Đuôi lụa quất theo quán tính sẵn có |
| Bổ, trúng | f0–3: áo co về 0,5×, đường may core 3,0 (1 px). f3–13: áo bung 1,4× rồi bị nhiễu ăn mòn hết. Nếu thanh kiếm còn bay tiếp, áo mọc lại trong 12 khung |
| Về, tan | Áo tan **trước** lưỡi: cùng ngưỡng nhiễu với `iFx.z`, sớm hơn 0,15. Dòng chảy đảo chiều về vòng ngọc. Đuôi lụa tắt sau cùng (0,32 s, như hiện tại) |

**Theo tầng hiển thị:**

| Tầng | Có |
|---|---|
| Lưới đủ (kiếm chủ) | `MantleSheath` + `MantleHull` (đổi theo góc) + `SilkTail` |
| LOD (kiếm giữa) | `MantleSheath`, đuôi áo 0,35 `L` sau đốc nằm luôn trong thẻ |
| Impostor (kiếm xa) | `MantleHalo` trong shader impostor; tia sau đốc tô màu lụa |

**Theo bậc đồ họa:**

| Bậc | Có |
|---|---|
| Low | `MantleSheath` cho kiếm chủ và kiếm giữa, một quãng tám nhiễu. Kiếm xa dùng quầng rẻ: đọc alpha atlas ở mip mờ (A3a). Không có vỏ ngược. Đuôi lụa chỉ ở phím 1 |
| Medium | Hai quãng tám. Kiếm xa dùng quầng SDF. Đuôi lụa cho mọi kiếm chủ |
| High | Thêm `MantleHull` cho kiếm chủ; nếp gấp khi kiếm ≥ 90 px |
| Ultra | Thêm quãng tám thứ ba; vỏ ngược cho thiên kiếm và kiếm chờ K1; kẹp trước `pow` cho MSAA |

**Chất theo hệ:**
- **Metal** (`mode: "qi"`), làm ngay:
  - thân bạc lam `[0.30, 0.62, 0.85]`, sắc ~200°, xa màu gõ `#7FF5E0` (170°);
  - các vạch khí thẳng song song lưỡi, không gợn (`curl` 0), mép cứng 0,7, hai nếp gấp;
  - mực chàm `[0.020, 0.028, 0.060]`, alpha 0,35;
  - lõi là lõi Metal `[0.62, 0.88, 1.0]` × 3,0.
  - Không vàng, không ngọc bích, không bạc hà, như `METAL_STREAM`.
  - Cảm giác: rèn và kiềm chế, không phải "đũa nhựa phát sáng".
- **Fire** (`mode: "flame"`), làm ngay:
  - Áo thành **lưỡi lửa liếm ra ngoài viền**: gốc dày 0,5 `W`, lưỡi lửa vươn thêm tới 1,6 `W`, tổng ~2 `W` từ mép ở giữa lưỡi (~9 px ở 100 px). Sàn: đầu lửa vượt viền ≥ 3 px ở 35 px.
  - Đầu lưỡi lửa sắc (cạnh 0,85, không `blur`).
  - Hướng lửa = 0,7 × (−vận tốc) + 0,3 × trục thế giới lên: lửa bị gió bạt về sau và bốc lên. Lửa chập chờn 8–12 Hz.
  - Dải màu của `element-fire.ts`:
    - bồ hóng `#240715` alpha 0,85 ở viền ngoài;
    - son `#D93800` → cam `#FF8A2A` → hổ phách `#FFB703`, alpha thật 0,9;
    - lõi trắng vàng `#FFFDF0` × 2,4, chỉ ở gốc lửa sát mép, ≤ 1 px.
  - Áo này **thay** vỏ lửa `sheathAt` ở các móc `waiting`, `travel`, `streamTravel` (thay, không chồng).
  - Tàn lửa (`EmberPool`) giữ 40/s cho kiếm chủ đang bay, thêm 8/s cho kiếm giữa.
  - Đề xuất kèm (Q3): lưỡi chế độ `furnace` nhẹ hơn, để lưỡi là thép tối nóng mép còn lửa nằm quanh.
- **Water** (`mode: "water"`), phác:
  - áo thành ống nước bám kiếm, thân chàm alpha thật 0,9, đường bọt cứng ở mép;
  - dòng chữ S bằng flow map hai pha (Vlachos, Portal 2);
  - đuôi cuộn lại sau đốc;
  - không có thân cộng sáng. Khúc xạ chỉ có khi pass méo dùng chung đã dựng.
- **Các hệ sau, mỗi hệ một dòng:**
  - Wood: gai lá mọc ra từ mép rồi rụng thành lá.
  - Earth: áo vỡ thành phiến khoáng nặng (cắt alpha) nghiến dọc lưỡi.
  - Thunder: ống sét gãy khúc, UV nhảy bậc.
  - Wind: gần như vô hình, chỉ viền mực và phần méo.
  - Ice: vỏ pha lê mặt phẳng cứng, viền sương, đứng yên.

**Bản giảm chuyển động:**
- `MantleSheath` làm dịu: dòng × 0,3, không thở, không vọt lúc phóng, đỉnh đường may × 0,6. Lửa chập chờn ở 2 Hz, lưỡi lửa giữ hình.
- `SilkTail` làm dịu: ngắn 0,6×, không rung.
- `MantleHull` và `MantleHalo` giữ.
- Mức gõ giữ thành một độ sáng đứng yên, vì nó mang thông tin.

**Chi phí, ước tính** (High, DPR 1, phím 7 lúc săn):

| Lớp | Lệnh vẽ | Ước tính |
|---|---|---|
| `MantleSheath`, 30 thẻ, ~2,4 nghìn px mỗi thẻ (Fire ~3,5 nghìn) | +1 | 0,03–0,08 ms |
| `MantleHull`, 6 vỏ thấp đa giác | +1 | 0,01–0,03 ms |
| `MantleHalo` trong impostor | 0 | 0,01–0,03 ms |
| `SilkTail`: dải sẵn có của kiếm chủ, đổi kiểu | 0 | ~0,01 ms |

- **Tổng phím 7: +0,07–0,16 ms, +2 lệnh vẽ.**
  - Với Fire, áo thay 6 vỏ lửa `sheathAt`, nên phần +0,23 ms của Fire được trả lại một phần.
  - Ở cận cảnh, 6 kiếm chủ cỡ ~600 px: thêm khoảng 0,1–0,2 ms.
  - Ở DPR 2, phần diện tích nhân 4.
- **Phím 1:** +0,01–0,04 ms.

**Rủi ro chính:**
- Ở 35–60 px, áo 2–3 px mỗi bên có thể đọc thành "thanh kiếm béo hơn, mờ hơn" thay vì lụa.
- Thân áo sáng quá sẽ dựng lại "ống sáng" mà anh đã chê.
- Fire trên 30 thanh có thể lại thành "tấm ván cháy". Đã có ~90 tấm lửa đọc như vậy hôm nay.

Cách chặn: lưỡi lửa chỉ ở ngoài viền; thu bề ngang khi kiếm dày đặc (§4.7); viền mực; đo phần điểm ảnh lưỡi giữ màu (§6).

### 3.B Echo Cascade

**Pitch:** Speed made visible: every sword is chased by flat sword-light echoes of itself that fan open on each turn and snap shut into the strike, while a bow wave splits the air at its tip.

**Ý:** kiếm ảnh kiểu donghua.
- Thanh kiếm thật là vật duy nhất được chiếu sáng, đi đầu.
- Theo sau là hai, ba "bóng ánh sáng" phẳng, rỗng tâm của chính nó.
- Quanh mũi có một sóng áp suất xé gió, tách khỏi viền và mở về phía sau.
- Hướng này đẹp ở chuyển động:
  - bay thẳng thì bóng xếp sát và mờ;
  - rẽ thì bóng xòe theo cung;
  - lúc trúng, các bóng đuổi kịp và gập vào lưỡi.
- Khi đứng chờ, kiếm có một "bóng tư thế" lớn hơn nó một chút phía sau, như linh hồn của kiếm. Lúc phóng, bóng đó ở lại chỗ cũ và tan.
- 94 sóng mũi cùng hướng trên dòng sông tự thành vảy chữ V, không cần dải cấp dòng.

**Nhìn nhanh:**

```
  echo 3        echo 2           echo 1                         bow wave arms (apart from the edges)
 [=-   -=]   [==-    -==]   [===-      -===]           .-''''''''''''''''''''''-.
 hollow, flat, fading                               (O){ ========= real blade =========>*
                                                         '-......................-'
```

| Cỡ trên màn | Thấy gì |
|---|---|
| 35 px | Thanh kiếm, một chữ V mảnh ở mũi, một bóng nhạt phía sau. Cả dòng thành vảy chữ V đồng hướng |
| 100 px | Hai, ba bóng rỗng tâm cách nhau ~0,55 `L`, mờ dần; sóng mũi hai cánh; khi rẽ có mảng quét |
| Cận cảnh | Thêm hai sợi khí mảnh từ hai mép của kiếm chủ; bóng tư thế quanh kiếm chờ; mảng quét có mép trước HDR |

**Các lớp:**

| Lớp | Tầng | Hình và cỡ | Ánh sáng | Trộn | Bloom |
|---|---|---|---|---|---|
| `BowWave` (A1 với hàm hình khác) | Kiếm chủ, kiếm giữa | Hai cánh xuất phát từ điểm mũi + 0,03 `L` (vừa trong quad impostor), mở về sau một góc nửa 9° (ở 20 m/s) tới 16° (ở 8 m/s). Cánh tách dần khỏi viền: 0 ở 70 % lưỡi, 0,6 `W` ngang tầm chắn. Cánh tắt trước khi tới chắn kiếm, nên không chạm vòng ngọc. Bề ngang cánh 0,25 `W`, sàn 1,5 px. Dài theo `clamp(v/20, 0.3, 1)` × 0,75 `L`. Dưới 4 m/s không có cánh | Đường sáng mảnh glow ≤ 0,85 phía trong; viền mực 1 px alpha 0,3 phía ngoài; đỉnh V thành core 2,4 (≤ 1 px) chỉ lúc bổ xuống và lúc trúng | Premultiplied, sau lưỡi 0,05 m | Đỉnh V, chỉ lúc bổ |
| `EchoTrail` (B1 `GhostTrail`) | Mọi tầng | Vòng tư thế cũ (đốc, mũi, góc lăn) lấy mẫu theo thời gian thế giới, mỗi Δ = `clamp(0.55 L / v, 0.035, 0.12)` s (2–7 khung). Số bóng High: kiếm chủ 3, kiếm giữa 2, kiếm xa 1. Bóng thứ k rộng 0,94^k, dài 1,0 | Vẽ bằng atlas impostor ở chế độ "echo": màu phẳng của hệ, không ánh kim loại. Rỗng tâm: độ đậm = bóng dáng × (0,35 + 0,65 × trường mép), nên mép sáng, giữa nhạt. Alpha 0,50 / 0,32 / 0,18 × (0,6 + 0,4 × ω chuẩn hóa). ≤ 0,75. Có một chút mực premultiplied (alpha × 0,25), để trên nền sáng bóng đọc như kính màu, không như màn trắng | Một lệnh vẽ instanced, `SwordImpostors` thứ hai ở chế độ echo | Không bao giờ |
| `SweepSmear` (B3) | Kiếm chủ, kiếm giữa | Một tấm 4 đỉnh giữa đường lưỡi khung trước và khung này, chỉ khi đường lưỡi quét ngang > 6 rad/s: K2 quét, K4 xoay, phím 7 rẽ để bổ xuống, xoắn lúc gom. Sống 1–2 khung. Tối đa 1 tấm mỗi kiếm mỗi khung | Mép trước core 2,4 (≤ 1 px); thân ≤ 0,8, tắt về mép sau | Premultiplied | Mép trước |
| `EdgeThreads` | Kiếm chủ | Hai sợi khí từ chỗ lưỡi rộng nhất, lệch ±(`W`/2 + 0,03 m). Dài 0,8 `L` (phím 1), 0,5 `L` (phím 7). Rộng 0,025 m, sàn 1 px | Lõi `pow(s, 7)` × 2,2; thân ≤ 0,55 | Vệt GPU `trails.ts`, sửa sang premultiplied | Lõi sợi |
| `StanceEcho` | Kiếm chờ | Một bóng cùng tư thế, to 1,08 lần, ngay sau kiếm | Thân ≤ 0,45 theo mức gõ: 0,15 / 0,30 / 0,45 | Như `EchoTrail` | Không |

- Ở phím 7, tia một khung sau đốc của kiếm giữa và kiếm xa **bị bỏ** khi bật B: bóng tàn ảnh thay nó (thay, không chồng).
- Dải lụa tua của phím 1 giữ nguyên, chỉ tô lại theo hệ, vì nó là nhận diện của Clear Wind.

**Theo trạng thái:**

| Trạng thái | Làm gì |
|---|---|
| Chờ | `StanceEcho` sau kiếm, thở 2,4 s, đậm theo mức gõ. Chưa có sóng mũi |
| Phóng | Bóng tư thế **ở lại** chỗ phóng, tan trong 10 khung: kiếm để lại bóng của mình. Tàn ảnh bắt đầu tích từ khung 0. Sóng mũi mọc theo tốc độ trong 4 khung |
| Bay đều | Bóng xếp sát (cách 0,35 `L` khi ω < 2), alpha × 0,6: pha yên nhất. Sóng mũi đứng yên |
| Rẽ | Bóng xòe theo cung (cách 0,7 `L`), alpha × 1,0. Cánh ngoài của sóng mũi dài 1,3×. Có mảng quét khi lưỡi quét ngang |
| Bổ, trúng | f0–3: các bóng đuổi kịp và gập vào lưỡi, đỉnh V sóng mũi lên core 3,0. Chớp mép lưỡi sẵn có × 1,3. Sau đó chuỗi bóng tích lại từ đầu |
| Về, tan | Thanh kiếm tan vào chính các bóng của nó: bóng cuối tắt sau cùng, sau lưỡi 8 khung. Lúc gấp dòng, các bóng hội tụ |

**Theo tầng hiển thị:**

| Tầng | Có |
|---|---|
| Lưới đủ | `BowWave`, 3 bóng, `SweepSmear`, `EdgeThreads`, `StanceEcho` khi chờ |
| LOD | `BowWave`, 2 bóng, `SweepSmear` |
| Impostor | 1 bóng; sóng mũi vẽ trong chính shader impostor (cánh nằm trong quad: nửa bề cao quad 0,125 `L` > 0,6 `W`) |

**Theo bậc đồ họa** (số bóng của kiếm chủ / giữa / xa):

| Bậc | Có |
|---|---|
| Low | Bóng 1 / 1 / 0; sóng mũi chỉ cho kiếm chủ và giữa; không mảng quét, không sợi khí |
| Medium | Bóng 2 / 1 / 1; mảng quét |
| High | Bóng 3 / 2 / 1; sợi khí cho kiếm chủ |
| Ultra | Bóng 3 / 3 / 2; mảng quét cả khi rẽ vừa (> 4 rad/s) |

**Chất theo hệ:**
- **Metal**, làm ngay:
  - bóng bạc lam `[0.36, 0.66, 0.88]` ≤ 0,75, trường mép làm sắc;
  - sóng mũi là một đường áp suất thẳng, cứng;
  - mảng quét có mép trước sắc;
  - sợi khí lõi trắng lam;
  - mực chàm alpha 0,3.
- **Fire**, làm ngay:
  - Mỗi bóng cháy từ mép sau thành lưỡi lửa, theo nhiễu bốc lên. Màu nguội theo tuổi: bóng 1 hổ phách, bóng 2 cam, bóng 3 son rồi bồ hóng (mực alpha 0,5 ở mép bị ăn).
  - Cả chuỗi đọc thành ngọn lửa của thanh kiếm đang cháy dần lại phía sau.
  - Sóng mũi thành sóng lửa: lưỡi lửa bóc khỏi hai cánh về sau, vươn 1,2 `W`.
  - Tàn lửa rơi từ bóng cuối, 20/s cho kiếm chủ.
  - Lửa nằm ở cánh và ở bóng, ngoài thân kiếm, nên không còn sắt nung.
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

**Bản giảm chuyển động:**
- `EchoTrail` làm dịu: 1 bóng cho kiếm chủ và giữa, alpha × 0,6, không gập lúc trúng (mờ đi thay vì gập).
- `SweepSmear` tắt.
- `BowWave` giữ, bề ngang đứng yên.
- `StanceEcho` giữ (mang mức gõ), không thở.

**Chi phí, ước tính** (High, phím 7 lúc săn):

| Lớp | Lệnh vẽ | Ước tính |
|---|---|---|
| `BowWave`, 30 thẻ hẹp | +1 | 0,03–0,06 ms |
| `EchoTrail`, 6 × 3 + 24 × 2 + 64 × 1 = 130 bóng, ~2,5 nghìn px mỗi bóng (~16 % khung) | +1 | 0,05–0,10 ms |
| `SweepSmear` | +1 | < 0,02 ms |
| `EdgeThreads`: 12 vệt GPU | +1 (hoặc 0 nếu gộp vào pool vệt sẵn có) | 0,01–0,02 ms |
| Sóng mũi kiếm xa trong impostor; bỏ tia sau đốc | 0 | +0,01 / −0,01 ms |

- **Tổng phím 7: +0,10–0,20 ms, +3–4 lệnh vẽ.**
- **Phím 1:** +0,02–0,05 ms.

**Rủi ro chính:**
- Bóng có thể đọc thành "thêm kiếm", gấp ba số kiếm, và rối.
- Bóng có thể đọc thành một vệt nhòe chuyển động.
- Ở làn dày của dòng sông, các chuỗi bóng chồng nhau thành một mớ sọc.
- Khi rẽ, bóng có thể quét qua vùng chữ.

Cách chặn: bóng phẳng, rỗng tâm, màu hệ, nhỏ dần; bớt bóng theo mật độ (§4.7); dồn bóng sát lại khi bay thẳng; đo độ chồng lớp.

### 3.C Celestial Regalia

**Pitch:** Clear Wind flies as a crowned relic: a star at its point, a slow-turning halo framing the hollow jade ring, twin streamers off the cloud guard and motes in orbit, with the steel left bare.

**Ý:** biến thanh kiếm thành một bảo vật thiên giới, như bộ radiance anh muốn cho nhân vật (halo, hạt sáng, dải sáng), áp cho vật.
- Ánh sáng không phủ thân kiếm mà dồn vào ba "trạm":
  - một ngôi sao ở mũi;
  - một quầng tròn **đóng khung đúng vòng ngọc rỗng**, chữ ký của Clear Wind ("lưỡi thẳng xuyên vòng ngọc bích rỗng", WEAPON_DESIGN §6);
  - hai dải sáng từ hai mút chắn mây.
- Thân thép giữa các trạm để trần, chỉ có đường mép sẵn có và một viền mảnh như đường kim hoàn.
- Khi kiếm chờ sau vai, mỗi thanh có một vầng mandorla mờ lớn dần theo mức gõ.

**Nhìn nhanh:**

```
   guard streamers (2) + tassel silk     halo around the hollow O     bare steel, hairline rim          tip star
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\        .-.                                                           |
                                     >     ( (O) ){ ===============================================>   --*--
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/        '-'    .  motes  .         .                                  |
```

| Cỡ trên màn | Thấy gì |
|---|---|
| 35 px | Một chòm hai điểm: sao ở mũi và chấm sáng ở vòng ngọc, cho biết ngay hướng kiếm. Thân kiếm có viền mảnh. Kiếm xa không có sao |
| 100 px | Quầng tròn quanh vòng ngọc, sao bốn cánh kéo theo hướng bay, hai dải sáng đuôi én, vài hạt bay quanh |
| Cận cảnh | Vòng 12 vạch ấn quay chậm trong quầng, hạt sáng trên hai quỹ đạo nghiêng, dải sáng bện nhau khi rẽ |

**Các lớp:**

| Lớp | Tầng | Hình và cỡ | Ánh sáng | Trộn | Bloom |
|---|---|---|---|---|---|
| `TipStar` | Kiếm chủ luôn có; kiếm giữa chỉ khi trên ngọn sóng sáng (`brightAt` ≥ 0,7) hoặc khi bổ xuống; kiếm xa không | Sao bốn cánh ở mũi + 0,02 `L`. Cánh dọc hướng bay 0,12 `L` (0,37 m ở kiếm 3,06 m, ~12 px ở 100 px), cánh ngang 0,04 `L`. Hướng cánh đổi theo vận tốc trong 4 khung | Lõi đĩa ≤ 2 px, core 3,0 (0,7 màu lõi hệ + ≤ 0,3 trắng). Cánh glow ≤ 0,85, thon dần. Sau sao có một sao mực to 1,3× alpha 0,3. Lấp lánh: nền 0,6, mỗi 1,4–2,2 s (seed riêng) lên 1,0 trong 10 khung | Pool `stars` sẵn có của phím 7 (`SpritePool`) | Lõi sao |
| `RingHalo` | Kiếm chủ, kiếm giữa; kiếm xa là chấm O trong impostor | Quad SDF đặt ở tâm vòng ngọc, cùng mặt phẳng lưỡi (lăn theo `FaceRoll`), nên luôn là vòng tròn bao quanh chữ O. Bán kính 1,7 × bán kính ngoài vòng ngọc (đọc từ model; ước tính ~0,085 `L`, ~8–9 px ở 100 px). Nét max(1,5 px, 0,012 m); quầng mềm 3 px ra ngoài, 1 px vào trong; **lòng vòng trong suốt**, chữ O luôn trống. Vòng ấn chỉ ở kiếm chủ ≥ 90 px: 12 vạch ngắn giữa 1,0 và 1,25 bán kính, quay một vòng mỗi 8 s | Nét glow 0,75–0,85; vạch ≤ 0,75; một vành mực 1 px alpha 0,3 ngay ngoài. Nét thành core 2,4 chỉ ở kiếm chủ, lúc phóng (f0–5) và nhịp từ không lỗi | Một lệnh vẽ instanced | Nét, chỉ lúc phóng |
| `GuardStreamers` | Kiếm chủ (kiếm giữa: hai đường kẻ trong tia sẵn có) | Hai dải từ hai mút chắn mây (±nửa bề ngang chắn). Dài 0,9 `L` (phím 1), 0,6 `L` (phím 7). Rộng 0,06 → 0,01 m, chẻ đuôi én ở cuối. Song song khi bay đều, bện nhau khi rẽ (lệch pha 0,12 s). Dải lụa tua vẫn ở giữa, tô lại theo hệ | Thân ≤ 0,7; lõi `pow(s, 7)` × 2,0 | Vệt GPU `trails.ts`. Kiếm giữa: tia `BeamPool` sẵn có vẽ thành hai lõi mảnh ±0,35 `W` | Lõi dải |
| `OrbitMotes` | Kiếm chủ | 10 hạt mỗi kiếm trên hai quỹ đạo elip nghiêng ±25° quanh thân kiếm: ngang 0,12 `L`, dọc 0,3 `L`. 2–3 rad/s. Cỡ 0,01–0,02 `L` (≥ 2 px). Quỹ đạo tính trong vertex shader (công thức P4) | Glow ≤ 0,85; 2/10 hạt có tâm core 2,0 | Gộp vào pool glow sẵn có | 2 hạt |
| `HairlineRim` (A1 hẹp) | Mọi tầng | Một viền kim hoàn 1–1,5 px glow ngay ngoài đường viền, thêm 1 px mực. Kiếm xa: trong shader impostor | Glow ≤ 0,6; mực alpha 0,3 | Premultiplied | Không |
| `WaitMandorla` | Kiếm chờ (phím 1 sau vai, vầng K5) | Vầng hình hạt hạnh nhân sau mỗi thanh, cao 1,25 `L`, rộng 0,35 `L` | Glow ≤ 0,45; mực ≤ 0,2. Lớn theo ba bậc của mức gõ | `SpritePool` sẵn có | Không |

**Theo trạng thái:**

| Trạng thái | Làm gì |
|---|---|
| Chờ | Mandorla theo mức gõ. Quầng ngọc quay chậm. Hạt bay quỹ đạo chậm. Sao mờ 0,4 |
| Phóng | Nét quầng lên core 2,4 (f0–5), nở 1,25× rồi về 1,0 trong 12 khung. Sao sáng đủ ngay f0. Hai dải sáng bắt đầu. Mandorla ở lại chỗ cũ, tan trong 10 khung |
| Bay đều | Sao 0,6, thỉnh thoảng lấp lánh. Quầng đứng yên 0,75. Hạt bay theo kiếm. Hai dải song song |
| Rẽ | Hai dải bện nhau. Hạt bên ngoài đường cong văng xa 1,3×. Cánh sao xoay theo hướng mới trong 4 khung |
| Bổ, trúng | Sao bùng 1,6× cỡ, core 3,6 trong 3 khung, rồi co lại trong 6 khung. Quầng co 0,8× rồi đập ra 1,2× (≤ 0,9) trong 10 khung. Hạt tung ra và tắt trong 8 khung |
| Về, tan | Sao tắt trước (4 khung). Quầng thu dần về vòng ngọc (12 khung). Hạt xoáy vào vòng ngọc. Dải sáng tắt sau cùng |

**Theo tầng hiển thị:**

| Tầng | Có |
|---|---|
| Lưới đủ | Đủ sáu lớp; mandorla chỉ khi chờ |
| LOD | Sao (chỉ trên ngọn sóng và khi bổ), quầng (không vạch ấn), tia hai đường kẻ, viền kim hoàn |
| Impostor | Chấm O ≤ 0,85 ở vị trí vòng ngọc trên atlas, viền kim hoàn trong shader, tia sau đốc mảnh |

**Theo bậc đồ họa:**

| Bậc | Có |
|---|---|
| Low | Sao cho kiếm chủ, quầng không vạch, viền kim hoàn, chấm O. Không hạt, không dải GPU: dải lụa tua giữ ở phím 1 |
| Medium | Thêm hai dải sáng cho kiếm chủ; 6 hạt mỗi kiếm chủ |
| High | Đủ như bảng lớp |
| Ultra | 14 hạt mỗi kiếm chủ; vạch ấn từ 70 px; sao cho kiếm giữa cả khi rẽ |

**Chất theo hệ:**
- **Metal**, làm ngay:
  - sao lõi `[0.62, 0.88, 1.0]` × 3,0;
  - quầng bạch kim `[0.62, 0.72, 0.85]` ≤ 0,8;
  - dải sáng lam thép `[0.45, 0.62, 0.85]` × 0,7;
  - hạt là sao bạc bốn cánh; mực chàm.
  - Không vàng: Kiếm và Metal giữ bạc, lam (`METAL_STREAM`), và vàng là màu tiền (`#FFC83A`).
- **Fire**, làm ngay:
  - Sao thành "tia mặt trời": lõi trắng vàng, cánh hình lưỡi lửa uốn và chập chờn, màu hổ phách.
  - Quầng thành **vòng lửa**: một dải lửa mảnh liếm ra ngoài từ vòng tròn, lưỡi lửa dài 0,4 × bán kính, bốc lên; mực bồ hóng.
  - Hai dải sáng thành dải lửa (`RibbonPool.setFlame` có sẵn).
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

**Bản giảm chuyển động:**
- Vòng ấn không quay.
- Hạt chậm × 0,3, không lấp lánh. Sao đứng yên.
- Bùng lúc trúng × 0,6.
- Dải sáng ngắn lại, không bện.
- Mandorla giữ, vì mang mức gõ.

**Chi phí, ước tính** (High, phím 7 lúc săn):

| Lớp | Lệnh vẽ | Ước tính |
|---|---|---|
| `TipStar`: 6 kiếm chủ + ~8 kiếm giữa trên ngọn sóng, trong pool `stars` | 0 | ~0,01 ms |
| `RingHalo`, 30 quad ~18 × 18 px | +1 | 0,01–0,02 ms |
| `GuardStreamers`, 12 vệt GPU; tia kiếm giữa đổi kiểu | +1 | 0,02–0,04 ms |
| `OrbitMotes`, 60 hạt | 0 | ~0,01 ms |
| `HairlineRim`, 30 thẻ hẹp | +1 | 0,02–0,04 ms |
| Chấm O và viền trong impostor | 0 | 0,01–0,02 ms |

- **Tổng phím 7: +0,07–0,13 ms, +3 lệnh vẽ.**
- **Phím 1:** có 3 mandorla và 30 hạt khi chờ, +0,02–0,04 ms.

**Rủi ro chính:**
- **Dòng sông 88 thanh vẫn gần như trần:** chỉ có viền mảnh, chấm ngọc, và sao trên ngọn sóng. Ở camera chơi anh có thể vẫn thấy "thô", đúng lời vừa chê.
- 6 kiếm chủ dễ thành "lấp lánh" rẻ tiền nếu sao nháy nhiều.
- Vòng lửa của Fire dễ đọc thành màu tiền vàng `#FFC83A`.
- **Vòng ngọc của model Tripo hiện ra màu bạc như crôm,** trong khi ảnh đã duyệt là ngọc trắng viền vàng (changelog kiếm thật). Quầng sẽ rọi đúng vào chỗ lệch đó (Q4).

### 3.D So sánh, và tôi nghiêng về hướng nào

| | A · Wind-Silk Mantle | B · Echo Cascade | C · Celestial Regalia |
|---|---|---|---|
| Trả lời "không có gì quanh kiếm" | Mạnh nhất: mọi thanh, mọi tầng | Mạnh khi bay nhanh, yếu khi bay chậm | Mạnh ở 6 kiếm chủ, yếu ở dòng sông |
| Giữ kiếm đọc được | Tốt (áo ngoài viền, cổ áo hở) | Tốt (sóng tách viền), nhưng bóng có thể làm loãng "đâu là kiếm thật" | Tốt nhất (thép trần) |
| Ở 35 px | Kiếm có viền khí | Vảy chữ V đồng hướng | Chòm hai điểm, kiếm xa gần trần |
| Cận cảnh | Đẹp (nếp lụa, viền ôm khối) | Đẹp khi rẽ và bổ | Đẹp nhất (vòng ấn, hạt, dải bện) |
| Fire | Lưỡi lửa liếm quanh lưỡi | Lửa cháy dần lại phía sau | Vòng lửa, sao lửa |
| Water sau này | Ống nước bám kiếm, hợp "flow → engulf" nhất | Dấu nước vỡ thành giọt | Vòng nước, giọt |
| Chi phí phím 7 | 0,07–0,16 ms | 0,10–0,20 ms | 0,07–0,13 ms |
| Rủi ro | Kiếm béo, mờ | Rối, "thêm kiếm" | Vẫn trần ở xa |

- **Claude nghiêng về A**, vì nó trả lời đúng câu anh hỏi cho cả 94 thanh, sửa lửa sắt nung, và hợp với Water nhất.
- Nếu anh thích A nhưng muốn sang hơn ở kiếm chủ, có thể mượn **một** lớp của hướng khác **sau khi** A đạt: sao mũi của C, hoặc mảng quét của B. Không ghép cả ba: đó là đường quay lại mớ VFX rối (ChatGPT cũng cảnh báo vậy).
- Cả ba đều còn dư nhiều so với +0,6 ms. Phần dư dành cho:
  - Ultra;
  - DPR > 1;
  - chất của hệ: Fire +0,23 ms hôm nay, Water có khúc xạ.
  Không dùng phần dư để chồng thêm lớp.

## 4. Luật chung cho cả ba hướng

1. **Clear Wind luôn đọc được.**
   - **Mặt lưỡi:** không lớp hào quang nào vẽ lên mặt lưỡi. Đường mép trắng nóng sẵn có nằm trong viền và giữ nguyên.
   - **Phủ lưỡi:** không lớp nào phủ quá **10 %** diện tích lưỡi ở bất kỳ khung nào. Riêng chớp lúc trúng, tối đa 3 khung, được tới 20 %.
   - **Vùng cấm quanh chắn:** từ đầu chắn kiếm tới `bladeFrom` + 0,03 `L`, không có thân hào quang.
     - ≥ 95 % điểm ảnh của vòng ngọc và chắn mây giữ màu.
     - Chỉ `RingHalo` của C được đóng khung vòng ngọc, và chỉ từ bên ngoài; lòng chữ O luôn trống.
   - Cách đo ở §6.
2. **Không thành màn trên nền sáng.**
   - Mọi lớp sáng có lớp mực trong cùng shader: premultiplied, `rgb = tối × a` với `a > 0` cộng `rgb = sáng` với `a = 0`.
   - Kênh trong suốt luôn tách khỏi màu; không lấy độ sáng làm alpha (DRAGON_FIRE_DIAGNOSIS).
   - Trên đá `#d6d0c2`, phần "nhạt" ≤ 10 % điểm ảnh của hào quang. Trên nền `#2a2c30`, không có vành đen.
3. **Ánh sáng.**
   - Chỉ lõi mảnh được vượt 1: HDR 2,4–3,6, ≤ 1 px ở camera chơi, ≤ 3 px ở cận cảnh, ≤ 30 % bề ngang của lớp đó.
   - Thân, quầng, vòng, bóng, hạt ≤ 0,85 mỗi kênh.
   - Quầng không nhân `SWORD_LIGHT` hay `uGain`.
   - Không đổi bloom chung (strength, radius, threshold), exposure hay tone map.
   - Khung đầu sáng đủ: lớp mới sinh vẽ ở tuổi 0.
4. **Màu.**
   - Không bao giờ dùng đỏ cảnh báo `#FF4A4A`.
   - Không thành mảng phẳng sáng mạnh ở các màu dành riêng (canon §21.1):
     - cam khẩn `#FFB020`;
     - vàng tiền `#FFC83A`;
     - xanh ngọc của sức gõ `#7FF5E0`.
   - Lửa luôn là dải chuyển màu, không phải một mảng.
   - Metal không có vàng.
5. **Không phụ thuộc tốc độ khung.**
   - Lịch sử tư thế và vệt lấy mẫu theo thời gian thế giới (như `RIBBON_SAMPLE_S`). Mọi tốc độ tính theo giây.
   - Khi dừng hình, mọi thứ đứng yên. 60 Hz và 120 Hz trông như nhau.
   - Không lớp nào nhảy alpha hay cỡ quá 30 % trong một khung, ngoài các chớp có chủ ý.
6. **Thay, không chồng.**
   - Hào quang **thay** vỏ lửa `sheathAt` của Fire, và thay tia sau đốc ở hướng nào ghi vậy.
   - Mỗi vùng kiếm ≤ 2 lớp trong suốt mỗi điểm ảnh (ELEMENT_LAYER §5). Trung bình sân ≤ 3, đỉnh ≤ 8 trên High (VFX_STANDARD §3.7).
7. **Thu theo mật độ.**
   - Khi một thanh có ≥ 3 thanh khác trong 40 px trên màn, hào quang của nó thu bề ngang × 0,8.
   - Các lớp phụ tắt trước: bóng thứ hai trở đi, hạt, sao.
   - CPU đếm mật độ trong vòng vẽ kiếm sẵn có (94² phép so, ~0,01 ms).
8. **Hào quang thuộc vũ khí, chất thuộc hệ.** Hai hợp đồng, tên tiếng Anh, chưa sửa mã.
   - **Phía vũ khí:** neo hào quang đo từ GLB lúc nạp, trong `blades.ts`, gắn vào `SwordModel`:

     ```ts
     /** Where a weapon's aura sits on its unit blade (measured from its GLB at load). */
     export interface AuraAnchors {
       readonly profile: Float32Array;   // 96 blade half-widths from bladeFrom to the tip (edgeField's half[])
       readonly bladeFrom: number;       // unit y where the blade starts
       readonly guardFrom: number;       // unit y where the guard band starts (no aura body from here to bladeFrom + 0.03)
       readonly ring: { readonly y: number; readonly r: number } | null; // jade ring centre and outer radius (unit)
       readonly guardHalf: number;       // half width of the cloud guard (streamer roots)
       readonly tasselFrom: number;      // tassel root on the unit axis (below 0: past the pommel end)
     }
     ```

   - **Phía hệ:** một mục `aura` mới trong `ElementKit` (`element-kit.ts`), cùng kiểu với `blade` và `trail`. Đặt cho mọi lớp bằng `applyAuraLook(kit.aura)`, một bộ uniform chung `AURA_LOOK` như `SWORD_LOOK`. Mỗi `mode` là một define, một chương trình, biên dịch lúc nạp.

     ```ts
     /** The aura's matter (canon D59): the weapon's aura shape drawn in the element's material. */
     export interface AuraLook {
       readonly mode: "qi" | "flame" | "water";   // later: "arc" | "leaf" | "stone" | "frost" | "gust"
       readonly ramp: ElementRamp;                 // core (unit, × coreHdr), edge, body (≤ 0.85), soot
       readonly coreHdr: number;                   // thin core gain, 2.4–3.6
       readonly ink: { readonly rgb: Rgb; readonly alpha: number }; // premultiplied dark under-layer
       readonly widthW: number;                    // body half width outside the blade edge, in blade widths
       readonly minPx: number;                     // per-side floor at the play camera
       readonly edge: number;                      // 0 soft … 1 hard (eroded tongues, foam lines)
       readonly flow: {
         readonly speed: number;                   // blade lengths per second at rest
         readonly perMps: number;                  // added per m/s of flight
         readonly scale: number;
         readonly buoyancy: number;                // 0 along the blade … 1 world up (Fire)
         readonly curl: number;                    // 0 straight (Metal) … 1 S-flow (Water)
         readonly twoPhase: boolean;               // flow map with two half-period phases (Water)
       };
       readonly breakup: number;                   // erosion into tongues, foam or shards (0 none … 1 full)
       readonly reachW: number;                    // how far broken pieces pass the body, in blade widths
       readonly flickerHz: number;                 // 0 steady
       readonly echo: { readonly tint: Rgb; readonly old: Rgb };   // direction B: body at birth and at end of life
       readonly star: { readonly core: Rgb; readonly arm: Rgb };   // direction C: tip star
       readonly ring: Rgb;                         // direction C: ring halo line
       readonly motes: { readonly tint: Rgb; readonly hdrShare: number };
       readonly shed: "none" | "glints" | "embers" | "droplets";
       readonly distortion: number;                // share of the shared distortion pass (0 for now)
       readonly reduced: { readonly flow: number; readonly flickerHz: number }; // reduced-motion multipliers
     }
     ```

   - **Kết nối:** hướng (A, B, C) là bộ lớp hình trong mô-đun kiếm; nó đọc `AuraAnchors` của vũ khí và `AuraLook` của hệ.
     - Đổi vũ khí là đổi neo; đổi hệ là đổi uniform hoặc define; không thêm tấm.
     - Fire chuyển phần `sheathAt` vào `aura.mode = "flame"`.
     - Đề xuất kèm cho Fire (Q3): thêm vào `BladeLook` trường `heatFrom` (hiện 0,05; đề xuất 0,55) và `char` 0,12 → 0,4. Dải nhiệt khi đó chỉ còn sát mép, lưỡi là thép tối nóng mép.
9. **Gắn với việc gõ.**
   - **Kiếm chờ:** hào quang lớn theo ba bậc của mức gõ (`ChargeFrameArgs.level`; ở phím 1 là ba thanh hiện ở 0,15 / 0,45 / 0,75).
   - **Từ không lỗi:** cho một nhịp lóe ≤ 0,9 trong 8 khung ở vòng ngọc lúc phóng. Khi lab chưa có tín hiệu "từ hoàn hảo", tạm dùng mức gõ.
   - **Bản giảm chuyển động:** giữ mức gõ thành một độ sáng đứng yên.
   - Từ phím đúng cuối tới lúc phóng vẫn ≤ 50 ms; hào quang không bao giờ giữ đòn lại.
10. **Thứ tự vẽ.** Pool một mesh nằm ở gốc tọa độ, nên three chỉ xếp theo `renderOrder`:

    | `renderOrder` | Lớp |
    |---|---|
    | 11 | `MantleSheath`, `MantleHull`, `BowWave`, `HairlineRim`, `EchoTrail` (sau lưỡi), lớp lửa của hào quang |
    | 12 | `RingHalo`, `SilkTail`, `GuardStreamers`, `EdgeThreads`, `SweepSmear` |
    | 13 | `OrbitMotes`, tàn lửa |
    | 14 | `TipStar` |

11. **Kỹ thuật bắt buộc:**
    - Kẹp trước `pow` và chặn `normalize(0)`, vì MSAA ở Ultra làm điểm mẫu ở mép tam giác vượt ±1, sinh NaN.
    - Không cấp phát mỗi khung.
    - Shader mới vào `prewarm`.
    - Gọi `#include <tonemapping_fragment>` và `<colorspace_fragment>`, vì Low và Medium vẽ thẳng ra màn.
    - Không dùng `discard` để tạo hình cho lớp trộn.
12. **Tiếng.** Bước mẫu không thêm tiếng riêng. Lóe của hào quang trùng khung với âm chiêu sẵn có (phóng, trúng, bay ngang qua 8–12 thanh gần nhất).

## 5. Kế hoạch lab

### 5.1 Công tắc

- **URL:** `?aura=off|a|b|c`. Mặc định `off`, tức giống hệt hôm nay, cho tới khi anh chọn.
  - Tên mã của từng hướng: `a` = `wind-silk-mantle`, `b` = `echo-cascade`, `c` = `celestial-regalia`.
- **Bảng điều khiển:** một ô chọn "Aura" cạnh ô "Element".
- **Phím:** `A` xoay vòng off → a → b → c (chưa dùng trong lab; đã dùng: 0–7, B, R, W, E, Z, =, -).
- **Lệnh lab:**
  - `__lab.aura(id)` đặt hướng;
  - `__lab.auraLayer(name, on, intensity)` bật tắt từng lớp, để chấm riêng từng lớp như skill hero-presence bước 5.
- **Giảm chuyển động:** `?motion=reduced` trong lab. Game dùng dòng "giảm chuyển động" của bảng Settings (`docs/games/IN_GAME_SETTINGS.md`), không dùng `screen.intensity`.
- **Bay mẫu một thanh:** `__lab.auraSolo()`, kịch bản 6 s:
  - một thanh Clear Wind đủ chờ sau vai 1 s trong lúc gõ;
  - phóng, bay chữ S 2 s ở 18 m/s, cao 1,2–2 m;
  - rẽ gắt 120°, bổ xuống một con thú;
  - bay lên, về tay, tan.
  - Đồng hồ cố định, nên lần chụp nào cũng như nhau.

### 5.2 Dựng trên hệ thống sẵn có

| Hệ thống | Dùng cho | Thay đổi |
|---|---|---|
| `sword-material.ts` | Bảng bề ngang lưỡi | `edgeField` giữ lại mảng `half[]` (hiện bị bỏ) và xuất `bladeProfile()`; một `DataTexture` 96 × 1 cho mỗi vũ khí. B thêm hệ số đường mép phía mũi ×1,4 khi bay đều. Đề xuất Fire `heatFrom` (Q3) |
| `real-swords.ts` | Kiếm xa của A, B, C; bóng của B | Nhánh hào quang trong fragment, theo define của hướng: quầng SDF (A), sóng mũi (B), chấm O và viền (C). Không nhân `SWORD_LIGHT`. Thêm chế độ `"echo"` cho `SwordImpostors` (tham số của constructor) để vẽ bóng phẳng |
| `scripts/models/blender/bake_sword_impostor.py` | Atlas hào quang | Thêm `--aura`: ghi `clear-wind-impostor-aura.png`, tuyến tính, **không** premultiply, cùng bố cục ô. R là khoảng cách có dấu tới bóng dáng (±16 px). G là khoảng cách tới riêng đường viền lưỡi, để cắt vùng chắn. B là mặt nạ vòng ngọc. Atlas màu đã duyệt giữ nguyên |
| Mới: `src/view/skills/sword-aura.ts` | Phần chung | `AuraCards` (thẻ A1 instanced, một lệnh vẽ cho mọi thanh; hàm hình theo hướng), `AuraHull` (vỏ ngược), `AURA_LOOK` và `applyAuraLook`, đếm mật độ, `begin / push / end` như `SwordImpostors` |
| Mới: `aura-mantle.ts`, `aura-echo.ts`, `aura-regalia.ts` | Ba hướng | Mỗi tệp một bộ lớp, có `enabled` và `intensity` cho từng lớp |
| `fxkit.ts` `RibbonPool`, `BeamPool`, `SpritePool` | Dải lụa tua, tia sau đốc, sao, hạt, mandorla | Không thêm pool mới. `SilkTail` đổi kiểu `startSilk`; tia sau đốc đổi màu hoặc thành hai đường kẻ; `stars` và glow nhận sao, hạt |
| `src/view/trails.ts` | `EdgeThreads` (B), `GuardStreamers` (C) | Đổi `AdditiveBlending` sang premultiplied (hiện nhân alpha hai lần); thêm đường cong bề ngang, cuộn UV, ăn mòn; chế độ lửa |
| `element-kit.ts` | Hợp đồng | `AuraLook`, `ElementKit.aura` |
| `element-metal.ts`, `element-fire.ts` | Chất | Điền `aura`. Fire bỏ `sheathAt` khi hào quang bật, giữ tàn lửa |
| `element-stage.ts` | Tầng chung | Giữ một `SwordAura` dùng chung cho `sword-skills.ts` và `myriad-swords.ts`; `update` và `reset` cùng các pool khác |
| `myriad-swords.ts` | Phím 7 | `drawSwords` đẩy từng thanh vào hào quang (tâm, hướng, chiều dài, lớp, độ sáng sóng, độ tan, bổ xuống); bỏ tia sau đốc ở B |
| `sword-skills.ts` | Phím 1 và các chiêu Kiếm | Kiếm bay, kiếm chờ sau vai (móc `waiting`), K2, K4, K5 đẩy vào hào quang |
| `blades.ts` | Neo | `AuraAnchors` đo lúc nạp; vỏ thấp đa giác cho `MantleHull`. Nếu vỏ riêng không đạt (§7, câu kỹ thuật), dùng LOD có `aSmoothNormal` |
| `src/lab/skills-main.ts` | Lab | `?aura`, ô chọn, phím `A`, `__lab.aura*`, `prewarm`, `__lab.bladeKeep()` (§6) |
| Mới: `scripts/visual/scenarios/lab-sword-aura.mjs` | Chụp và đo | `PLAN=owner`, `sheet`, `gates`; `lab-element-perf.mjs` thêm biến `AURA` |
| Mới: `tests/view/sword-aura.test.ts` | Kiểm thử | Hợp đồng, màu, thay chứ không chồng, không cấp phát |

### 5.3 Thứ tự commit trong `games/immortality-cultivation`

Một commit một bước. Sau mỗi bước, `tsc`, `pnpm test` và `pnpm build` phải xanh. Lab không vào `dist`.

1. **Hợp đồng:** `AuraLook`, `ElementKit.aura`, `AuraAnchors`; điền Metal và Fire. Chưa đổi hình nào: `?aura=off` giữ nguyên hôm nay, kiểm bằng `lab-element-parity.mjs`.
2. **Phần chung:** bảng bề ngang lưỡi, `sword-aura.ts` (`AuraCards`, `AuraHull`, đếm mật độ), công tắc `?aura`, ô chọn, phím `A`, `prewarm`, `__lab.bladeKeep()`.
3. **Atlas hào quang:** `bake_sword_impostor.py --aura` và nhánh hào quang trong `real-swords.ts`.
4. **Hướng A:** `aura-mantle.ts`, Metal và Fire; Fire thay `sheathAt`.
5. **Hướng B:** `aura-echo.ts`, chế độ echo của impostor, `trails.ts` premultiplied.
6. **Hướng C:** `aura-regalia.ts`.
7. **Bay mẫu và kịch bản chụp:** `__lab.auraSolo()`, `lab-sword-aura.mjs`, biến `AURA` của `lab-element-perf.mjs`.
8. **Changelog** `docs/changelog/<ngày>-lab-sword-aura.md`: ảnh trước và sau, số đo, các điểm nhìn để anh quyết.

Phần đề xuất `heatFrom` cho lưỡi Fire nằm sau một cờ (`?bladeHeat=edge`) cho tới khi anh trả lời Q3.

### 5.4 Người làm, media và ảnh chụp

- Claude dựng trong lab, theo bước 1–8.
- Media (atlas, video) không vào Git.
- Ảnh chụp vào `games/immortality-cultivation/tmp/shots/sword-aura/`. Khung thô được tỉa bằng `node tools/capture-prune/prune.mjs <thư mục> --apply` sau khi chấm, chỉ giữ tấm ảnh, video và JSON.
- Mọi lượt GPU chạy qua `.local/bin/heavy.sh --gpu` (đo hiệu năng dùng `--perf`), một lượt mỗi lúc.

### 5.5 Kế hoạch chụp cho anh

**Thông số chung:**
- High, 1920 × 1080, 60 khung/s, DPR ghim 1, đồng hồ cố định.
- Có tiếng: bus tiếng của lab.
- Chữ chú thích tiếng Anh in trên video, dạng "Wind-Silk Mantle · Metal · key 7 · play camera".

**Mỗi hướng một video** `owner-aura-<a|b|c>-<ngày>.mp4`, khoảng 50 s. Cả Metal lẫn Fire, mỗi hệ năm cảnh:
1. Một thanh bay mẫu (`__lab.auraSolo`) ở cận cảnh, camera xoay chậm 30° trong 6 s, để thấy hào quang cả lúc nhìn ngang lẫn lúc kiếm chĩa vào camera.
2. Phím 1 ở camera chơi.
3. Phím 1 ở cận cảnh (zoom D57).
4. Phím 7 ở camera chơi.
5. Phím 7 ở cận cảnh.

Thêm một video `owner-aura-off-<ngày>.mp4` cùng các cảnh, làm mốc so (hôm nay).

**Mỗi hướng một tấm ảnh tĩnh** cho mỗi hệ:
- **Hàng:** kiếm cắt ở 35, 70 và 130 px, lấy từ phím 7 F90 và F140 và một khung bay của phím 1.
- **Cột:**
  - đá sáng `#d6d0c2`;
  - nền giữa `#7c848b`;
  - nền tối `#2a2c30`;
  - ảnh xám của nền giữa.
- **Thêm** một cặp cùng khung, hào quang tắt và bật.
- Bản 1080p và bản 720p.

**Gửi anh:** ba video, video mốc và các tấm ảnh, kèm câu hỏi §7. Tấm cho giám khảo mù không in số đo.

### 5.6 Sau khi anh chọn

1. Dựng hướng đã chọn cho mọi chiêu Kiếm: K0–K5, thiên kiếm, kiếm cắm đất. Bỏ hai hướng còn lại khỏi mã, giữ `off`.
2. Đo lại đủ cổng §6.
3. Hai giám khảo mù chấm, mỗi người riêng, ở cài đặt của người chơi, không cờ URL, so với mốc thương mại.
   - Chiêu còn ở lab, nên đây là lượt chấm hướng.
   - Lượt nghiệm thu thật là khi chiêu đã vào bản build chơi.
4. Khi cả hai giám khảo cho ≥ 7, gửi anh video demo, rồi tiếp tục tới 8,5. Không có lượt "tạm được".
5. Ba lần làm lại mà điểm không lên thì dừng, cùng ChatGPT tìm cách khác (gửi clip, ghi chú giám khảo, những gì đã thử) trước lần thứ tư.
6. Water dùng đúng bộ hình đã chọn, chỉ đổi chất. Pass méo dùng chung dựng cùng Water.
7. Một lượt tìm nguồn tiếng Trung (Bilibili, Zhihu, GameRes) cho đúng hướng đã chọn, trước vòng tinh chỉnh.

## 6. Cổng

| Cổng | Ngưỡng | Đo bằng |
|---|---|---|
| Thời gian khung | Hào quang trừ `off` ≤ **+0,6 ms** p95 ở phím 7 lúc săn trên High, mục tiêu ≤ +0,45. Không cửa sổ nào (nghỉ, phím 7 săn, nhát kết, K5, phím 1) có trung vị p95 vượt **11,5 ms**, cả Metal lẫn Fire | `lab-element-perf.mjs` với `AURA=off,<hướng>` xen kẽ: 7 vòng × 3–5 lượt, DPR ghim 1, máy rảnh, qua `heavy.sh --perf`. Báo trung vị và trung bình p95. Báo thêm một lượt DPR 2, DPR trung bình của độ phân giải động, và Ultra (không chặn) |
| Từ phím tới lúc phóng | Không đổi: VFX 0 ms, thân 33 ms, cổng ≤ 50 ms. Khung chậm nhất của lần phóng đầu ≤ 50 ms (hiện 46) khi đã `prewarm` | `lab-power.mjs PHASE=latency`; trang mới mở |
| Không NaN | Không NaN hay Inf trong bộ đệm sáng của bloom | Quét ≥ 2.000 khung, mọi chiêu, High và Ultra (MSAA 4), camera chơi và cận cảnh |
| Kiếm đọc được | Phần điểm ảnh lưỡi giữ màu (ΔE OKLab ≤ 0,04 so với `off` cùng khung): ≥ 90 % ở kiếm chủ và kiếm giữa, ≥ 85 % ở kiếm xa. Vòng ngọc và chắn mây ≥ 95 %. Không lớp nào phủ > 10 % lưỡi (chớp ≤ 3 khung: 20 %). Ảnh xám ở 40–100 px vẫn thấy lưỡi, vòng ngọc, chắn, tua | `__lab.bladeKeep()`: cùng khung cố định vẽ hai lần (`off`, rồi bật). Mặt nạ lưỡi lấy từ một lượt vẽ mã màu (`BladeSet` và impostor xuất màu mã, hào quang ẩn). Mặt nạ ngọc lấy từ mặt nạ `JADE` của `sword-material.ts` và kênh B của atlas hào quang. Lấy mẫu phím 7 F60–F160 mỗi 10 khung, và phím 1 lúc bay. Giám khảo xem ảnh xám |
| Chữ gõ đọc được | Phần điểm ảnh gần trắng (độ sáng > 0,92) ở 70 % trên của khung ≤ `off` + 0,15 % mỗi khung. Khi vào game: tương phản thẻ chữ ≥ 7 : 1 ở p99. Hào quang thêm ≤ 10 % độ sáng trong vùng chữ | Như phép đo Fire (changelog Fire phần 2); trong game, thanh chữ là DOM ngoài canvas |
| Nền sáng, nền tối | Đá `#d6d0c2`: phần "nhạt" ≤ 10 % điểm ảnh hào quang. Nền `#2a2c30`: phần điểm ảnh hào quang tối hơn nền quá 0,05 độ sáng ≤ 20 % (không vành đen). Đường viền kiếm tương phản với nền **cao hơn** khi bật | Ba nền như phép đo Fire |
| Bloom và trắng xóa | Điểm ảnh > 1 do hào quang thêm ≤ +0,3 % khung (`__lab.bright`, HdrProbe). Độ sáng ≥ 0,95 ≤ 6 % sân lúc đỉnh. Riêng hào quang, khi không có chiêu nào khác, ≤ 1 % | Ba nền, camera chơi và cận cảnh |
| Lửa liếm | Đầu lửa vượt viền ≥ 3 px ở kiếm 35 px, ở ≥ 60 % khung lấy mẫu (kiếm chủ, kiếm giữa). Thân lửa sau tone map: sắc 15–40°, bão hòa ≥ 0,5. Cách xa `#FF4A4A`. Giám khảo gọi ra "lửa" không cần tên | Bản đồ điểm ảnh khung cố định; phép thử màu Fire sẵn có |
| Chồng lớp | Trung bình ≤ 3 lớp trong suốt mỗi điểm ảnh trên sân, ≤ 2 trong vùng của một kiếm | Một lượt đếm chồng lớp, ghi vào `meta.json` của lượt chụp |
| Mượt | Không lớp nào nhảy alpha hay cỡ quá 30 % trong một khung ngoài chớp. 60 Hz và 120 Hz giống nhau. Đứng yên khi dừng hình | Motion probe của lab; một clip nửa tốc độ |
| Metal `off` không đổi | `?aura=off` trùng khít điểm ảnh với bản trước | `lab-element-parity.mjs` |
| Mã | `tsc`, `pnpm test`, `pnpm build` xanh; grep `dist` không thấy mã lab hay mã hào quang của lab | Như các lượt trước |

## 7. Câu hỏi cho anh

- **Q1. Hướng nào:** A (Wind-Silk Mantle), B (Echo Cascade) hay C (Celestial Regalia)? Anh trả lời sau khi xem ba video và các tấm ảnh. Claude nghiêng về A.
- **Q2. Metal cũng đổi.** Lớp hệ từng hứa "Metal không đổi". Nhưng thanh kiếm anh chê là chính bộ Metal, nên hào quang phải áp cho Metal. Anh đồng ý chứ? Bản `off` vẫn giữ để so.
- **Q3. Lưỡi Fire.** Đề xuất bớt dải cam trên mặt lưỡi: lưỡi thành thép tối nóng mép, còn lửa liếm **quanh** lưỡi, thay cho cả thanh cam như sắt nung. Việc này đổi hình lưỡi Fire đã chụp. Anh đồng ý chứ?
- **Q4. Vòng ngọc.** Model Tripo hiện cho vòng ngọc màu bạc như crôm, trong khi ảnh đã duyệt là ngọc trắng viền vàng. Hướng nào cũng làm vòng ngọc nổi hơn (C nhất). Có sửa vật liệu vòng ngọc trước khi quay mẫu không? Đề xuất: có, vì việc này nhỏ.
- **Q5. Ngân sách.** +0,6 ms là riêng cho hào quang, cộng trên phần chất của hệ (Fire hôm nay +0,23 ms), miễn tổng vẫn ≤ 11,5 ms. Đúng ý anh không?

**Câu kỹ thuật Claude tự quyết theo đề xuất, có báo lại** (anh giao quyền theo đề xuất, 27/10):
- **Cách đếm trần:** vệt và thẻ instanced (nhiều vệt trong một lệnh vẽ) được tính theo lệnh vẽ, diện tích và độ chồng lớp, không theo số vật của VFX_STANDARD §3.7. Cổng thật là thời gian khung và độ chồng.
- **Smear trên đỉnh của lưới thật** (B4 của tài liệu kỹ thuật): **không dùng**. Thanh kiếm đã duyệt không bị biến dạng; B chỉ dùng mảng quét tách rời.
- **Vỏ thấp đa giác cho `MantleHull`:** dựng trong Blender một vỏ vô hình 200–600 tam giác chỉ bọc lưỡi. Nó mang ánh sáng, không phải kiếm thay thế. Nếu không đạt thì dùng LOD có `aSmoothNormal`.
- **Pass méo dùng chung:** dựng cùng Water như đã định; không hướng nào cần nó ở bước mẫu.
- **Giảm chuyển động:** dùng dòng "giảm chuyển động" của bảng Settings, không dùng `screen.intensity`.

## Nguồn

Trong repo, đã đọc 03/11/2026:
- [`source/sword-aura-chatgpt-2026-11-03.md`](source/sword-aura-chatgpt-2026-11-03.md):
  - mục C: câu trả lời sau tự rà soát;
  - mục E: Claude kiểm nguồn (16/17 nguồn chính thức đúng);
  - mục F: đánh giá.
- [`source/sword-aura-gemini-2026-11-03.md`](source/sword-aura-gemini-2026-11-03.md): mục B câu trả lời, mục C kiểm nguồn, mục D đánh giá và ba hướng gộp.
- [`source/sword-aura-tech-2026-11-03.md`](source/sword-aura-tech-2026-11-03.md):
  - lớp A1–A3, B1–B4, C, D, E, F;
  - ba gói kỹ thuật;
  - cách đo, các bẫy, bảng tổng.
- [`ELEMENT_LAYER.md`](ELEMENT_LAYER.md), [`../00-canon.md`](../00-canon.md) (D54–D59, §21.1), [`WEAPON_DESIGN.md`](WEAPON_DESIGN.md), [`SKILL_CATALOG_V2.md`](SKILL_CATALOG_V2.md).
- [`VFX_STANDARD.md`](../../VFX_STANDARD.md) §3.1–3.8.
- Skill [`game-vfx-layered`](../../../../.agents/skills/game-vfx-layered/SKILL.md), [`game-hero-presence-vfx`](../../../../.agents/skills/game-hero-presence-vfx/SKILL.md):
  - `references/layers.md`: P1–P10, trạng thái, kiềm chế, giảm chuyển động, bậc;
  - `references/worked-examples.md`: "Tu Tien: flying swords without an aura".
- `games/immortality-cultivation`, chỉ đọc:
  - `src/view/skills/`: `sword-material.ts`, `real-swords.ts`, `blades.ts`, `element-kit.ts`, `element-metal.ts`, `element-fire.ts`, `element-stage.ts`, `myriad-swords.ts`, `sword-skills.ts`, `weapons.ts`;
  - `src/view/trails.ts`, `src/lab/skills-main.ts`;
  - `docs/changelog/2026-11-03-lab-real-swords.md`, `docs/changelog/2026-11-03-lab-element-fire.md`.

Nguồn web: chỉ qua ba tệp nghiên cứu trên, mỗi khẳng định ghi rõ đã kiểm hay chưa. Câu trích fan từ Reddit chưa ai kiểm được, vì Reddit bị chặn trong môi trường này; chúng chỉ là gợi ý, không là bằng chứng.
