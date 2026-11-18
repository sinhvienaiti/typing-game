# Hào quang quanh chiêu (skill radiance): kiểm từng chiêu, từng pha (03/11/2026)

**Trạng thái:** tài liệu kiểm và đề xuất, chưa có mã. Chụp trên lab ở `games/immortality-cultivation` `67b2026` (vòng 3 của Fire đã vào; hào quang kiếm của `SWORD_AURA.md` chưa dựng). Mọi chi phí là ước tính, phải đo.

**Đầu vào:**
- Lời anh 03/11 (§0), luật `AGENTS.md` mục "Skill effects sparkle too" và skill `game-vfx-layered` bước 3 "Every shape sparkles".
- [`FIRE_STYLE.md`](FIRE_STYLE.md): chẩn đoán lửa phím 1, ba hướng A · Brushfire Calligraphy, B · Starfire Jewel, C · Halo Seal, ba mảnh dùng chung `GlintPool`, chế độ vệt của `EmberPool`, vòng mảnh. Tài liệu này dùng lại các mảnh đó, không đề xuất lại.
- [`SWORD_AURA.md`](SWORD_AURA.md): hào quang quanh kiếm bay, anh đã chọn "A + sao mũi của C". **Ngoài phạm vi ở đây:** mọi lớp quanh thanh kiếm (lúc chờ sau vai, lúc bay, sao mũi `TipStar`).
- [`ELEMENT_LAYER.md`](ELEMENT_LAYER.md) (D59, bảng màu, trần 0,85 ms, bẫy §8), canon `../00-canon.md` §21.1 (màu dành riêng) và D54 (Fire dùng lửa cam đỏ thật), [`VFX_STANDARD.md`](../../VFX_STANDARD.md) §3.4 (nhịp), §3.8 (giảm chuyển động).
- Mã chỉ đọc: `src/view/skills/sword-skills.ts`, `myriad-swords.ts`, `element-kit.ts`, `element-metal.ts`, `element-fire.ts`, `embers.ts`, `fxkit.ts`, `heat-rings.ts`, `fire-points.ts`, `src/lab/skills-main.ts`.

**Tấm khung để xem** (không vào Git; mỗi chiêu một tấm, bốn hàng: Metal ở camera chơi, Fire ở camera chơi, Metal cận cảnh, Fire cận cảnh; mỗi cột một pha, nhãn dưới ô):

| Phím lab | Chiêu | Tấm |
|---|---|---|
| 0 | Flying Sword (K0, đòn thường) | `games/immortality-cultivation/tmp/shots/fire-style/audit/audit-k0.jpg` |
| 1 | Threefold Sword Command (K1) | `…/audit/audit-k1.jpg` |
| 2 | Cloud-Piercing Line (K2) | `…/audit/audit-k2.jpg` |
| 3 | Returning Sword Aegis (K3A) | `…/audit/audit-k3.jpg` |
| 4 | Flowing-Light Step (K3B) | `…/audit/audit-k4.jpg` |
| 5 | Falling Sword Array (K4) | `…/audit/audit-k5.jpg` |
| 6 | Milky-Way Sword Rain (K5, tuyệt kỹ) | `…/audit/audit-k6.jpg` |
| 7 | Myriad Swords (chiêu cả sân) | `…/audit/audit-k7.jpg` |

Đề bài ghi "phím 1–6 (K0–K5)"; trong lab phím 0 là K0 và phím 6 là K5 (`skills-main.ts` `KEYS`), nên tài liệu kiểm đủ tám chiêu lab vẽ, phím 0 tới 7.

## 0. Lời anh và tóm tắt

Lời anh (03/11): "như tôi đã nói, bạn luôn thiếu các hiệu ứng xung quanh, ví dụ trước đó đã nói về vũ khí, bây giờ là với kỹ năng, bạn cũng cần phải xử lý để nó lấp lánh, long lanh hào quang đẹp hơn chứ".

**Kết quả:**
1. **Metal có bộ từ vựng hào quang, nhưng chỉ sống vài khung.** Sao bốn cánh (`star_07`), flare (`star_09`), tia, vòng, cột sáng, quầng sau lưng, hạt bay lên đều có, đọc được ở camera chơi lúc phóng và lúc trúng (3–8 khung). Sau ~0,8 s gần như trống. Hạt và tia lửa là đĩa tròn mềm (`circle_05`), vòng xung là vành dày như bong bóng, mọi sao cùng một hình, cùng một nhịp.
2. **Bộ chất Fire của riêng nó không có một ngôi sao, vòng mảnh, tia sáng hay ánh chạy nào** ở mọi pha của phím 1 và phím 7, đúng hai chiêu anh đã xem. Hook `glint` của phím 7 vẽ một chấm tròn.
3. **Fire ở phím 0, 2–6 là "Metal tô lại".** Fire chỉ thay các pha chung (tụ lực, phóng, va chạm, nhát cắt, dư âm, chết); các lớp riêng của từng chiêu vẫn là ánh sáng cộng của Metal, nhuộm bằng bảng màu lửa. Trên đá chúng ra **hồng cam nhạt**: ba cung của phím 3, lục giác của phím 5, vạch của phím 2, mũi tên của phím 4, các vòng xung, cột và tia. Đây đúng là bẫy `ELEMENT_LAYER` §8. Chỉ ấn dưới chân người là đặc (`sigSeal.setSolid`); sáu ấn của chiêu thì không.
4. **Tuyệt kỹ phím 6 trong Fire vẫn lam:** vòng cổng trời, bốn cột sáng, vệt mưa kiếm, sao nứt và khe nứt 22 m kết thúc chiêu như một tia sét lam trên sân lửa. Tranh cut-in cũng là thiên hà lam.
5. **Ấn, vạch, vết cắt không có ánh chạy** và không có sao ở chỗ nét giao nhau, ở cả hai hệ: chúng sáng đều rồi tắt.
6. Đề xuất: **bảy lớp dùng chung dựng một lần** (§6), cho mọi chiêu và mọi hệ. Hệ chỉ cấp màu qua một bảng `radiance` mới trong `ElementKit` (§3). Chỗ đặt lớp hào quang thuộc **hình** của chiêu, nên hook của hệ không còn vô tình xóa nó.
7. **Ngân sách** (§7): phím 7 gần như không còn chỗ sau hào quang kiếm. Lớp hào quang chiêu ở phím 7 phải bù bằng cách bỏ lớp cũ (flipbook `fire-sparks`, chấm `ember()`, vòng xung `circle_03`); các chiêu khác còn rộng.
8. **Thứ tự** (§8): anh chọn kiểu trên bảng FIRE_STYLE và trả lời §9, rồi dựng lớp dùng chung, rồi 3–5 ứng viên phím 1 và phím 7, rồi bù phần Fire còn thiếu ở phím 0, 2–6, rồi lấp lánh cho các chiêu còn lại.

## 1. Cách kiểm

- **Chụp:** kịch bản riêng của lượt này, `tmp/shots/fire-style/audit/tools/audit-scenario.mjs`, nằm ngoài repo, đặt cạnh tấm để chạy lại. Chạy qua `src/kit/tools/cdp-run.mjs`, server Vite không HMR của Claude ở cổng 3187, qua `../../.local/bin/heavy.sh --gpu`.
  - Lab: `skills-lab.html?fixed=1&ui=0&dpr=1&typed=1&weapon=clear-wind&cutin=0.9&element=metal|fire`, bậc High, 1920×1080, nền đá mặc định `#7c848b`.
  - Chữ gõ ở 45 WPM: khung "charge50" và "charge90" là lúc gõ được 50 % và 90 % chữ. Phím 0 và phím 7 phát ngay, không có chữ.
  - Khung phóng là khung lab đếm sự kiện `release`; các cột sau đó tính từ khung phóng.
  - Phím 6 có khung cut-in, giữ 0,9 s (`cutin=0.9`, như các kịch bản đo cũ; mặc định là 1,7 s).
  - Cận cảnh: camera 55° đặt lại theo pha, lúc tụ lực và phóng nhìn vào người, lúc trúng nhìn vào đích.
- **Tấm:** `tools/sheets.sh`.
  - Hàng camera chơi là **cắt 1:1** khung 1080p, nên cỡ trên tấm đúng cỡ người chơi thấy. Riêng phím 2 sau khi phóng cắt ×2/3; phím 6 và 7 là cả khung ×1/4.
  - Hàng cận cảnh là cả khung ×1/4.
- **Tỉ lệ ở camera chơi:** ~**39 px/m** (đo: hai góc trái và phải của trận phím 5, cách nhau 6,15 m, cách nhau ~250 px trên khung 1080p, tức ~40 px/m theo chiều ngang ở giữa sân; FIRE_STYLE đo ~38 px/m ở người). Người cao ~64 px.
- **Cách chấm cột "đọc ở camera chơi":**
  - **Có:** thấy rõ sao, vòng, tia hay quầng ở cắt 1:1;
  - **Yếu:** có nhưng < 4 px, sống ≤ 3 khung, hoặc lẫn vào lớp khác;
  - **Không:** không có lớp nào quanh hình chính.
- **Không làm:** không sửa mã, không đổi hình lửa (FIRE_STYLE), không đụng lửa lưu lâu (agent vòng 3), không đụng quanh kiếm (SWORD_AURA). Chưa chụp nền đá sáng `#d6d0c2`: phải chụp khi dựng, vì lấp lánh cộng sáng dễ mất trên nền sáng (FIRE_STYLE §1.2).

## 2. Hiện trạng chung

### 2.1 Metal

| Lớp | Có ở đâu | Đọc thế nào |
|---|---|---|
| Sao bốn cánh `star_07` (`twinkle`, `starPair`, sao ở tay, sao ở mũi) | phím, phóng, kiếm đến, va chạm, giao điểm của phím 2, góc trận phím 5, mưa kiếm phím 6 | Có ở camera chơi, nhưng **một hình, một nhịp**: lóe một lần 0,1–0,2 s, không có lớn–nhỏ lệch nhịp, không lấp lánh lại |
| Flare `star_09` | phóng, đòn lớn phím 6 | Có, hơi trắng (lõi rộng) |
| Tia `rays` (BeamPool) | phóng, va chạm, đỡ đòn, mở trận | Có, nhưng dày 0,1–0,2 m (4–8 px), đọc như vạch tốc độ hơn là tia sáng mảnh |
| Vòng `circle_02` (mảnh), vòng xung `circle_03` (dày) | phóng, va chạm, ấn | Vòng dày đọc thành **bong bóng mềm** (phím 0 "impact+3", phím 3 "landed", "parry") |
| Quầng sau lưng `light_01` ×2 + đĩa sáng | lúc tụ lực | Có: đây là "hào quang" duy nhất lúc gõ |
| Hạt bay lên, hạt khí xoáy vào tay, tia lửa (`circle_05`) | tụ lực, phóng, va chạm, dư âm | **Đĩa tròn mềm 2–4 px**, như Fire: "bokeh" nhỏ, không lấp lánh |
| Ấn (`GroundSigil`) | dưới chân và ở đích (6 ấn của chiêu) | Sáng đều, lên xuống theo phím; không có ánh chạy, không sao ở giao điểm |
| Dư âm | quầng đất + hạt tròn 1–1,2 s | Sau ~0,8 s trống (phím 0, 1, 2, 4 cột "linger") |

Giữa sao va chạm của phím 0 và 1 là **một sao gai đen**. Khung đồ họa cục bộ (F15, `screen-fx.ts`: một chùm tám tia đảo màu, 3 khung) đảo lóe trắng thành gai đen, cộng thêm vết mực bắn ra (`basicImpact`). Ở camera chơi nó to ~200 px và đọc như vết mực hơn là lóe sáng. Fire đã đổi khung này sang hình lửa ở vòng 3; Metal giữ nguyên từng bit.

### 2.2 Fire

Fire thay các pha chung bằng hook (`element-fire.ts`):
- **`chargeFrame`** vẽ flipbook `fire-charge`, chấm trắng vàng, tàn lửa hút vào, đất tối.
  - Hook trả `true`, nên Metal **không** vẽ quầng `light_01`, đĩa sáng, hạt bay lên, hạt khí.
  - Lúc tụ lực của Fire không còn hào quang nào.
- **`chargeKey`** (mỗi phím): vòng tàn lửa hút vào. Kiếm đến chỗ thì có hoa sen nhỏ, điểm lửa và tia nan bánh xe.
  - Không có sao ở tay, không vòng đất.
- **`release`**: điểm lửa, vòng lửa áp suất, hoa sen sau lưng, flipbook tia nan bánh xe, tàn lửa.
  - **Giống hệt nhau ở mọi chiêu**, từ phím 0 tới phím 7; chỉ to hơn ở bậc 3 trở lên.
- **`impact`, `cut`, `aftermath`, `death`**: điểm lửa, hoa sen, tia nan, tàn lửa tròn, trăng lửa, đất cháy, khói, tàn lửa bay lên.
- **Không có hook `areaHit`, `areaBurst`.** Đòn nhẹ trong vùng (phím 2, 5, 6) và nổ vùng vẫn là của Metal, tô màu lửa.
- **Phím 7** (`stream`): điểm nhỏ, tia nan và 3 tàn lửa ở mỗi kiếm dòng sông; hoa sen ở kiếm dẫn đầu.
  - `glint` vẽ một **chấm tròn** `CORE × 2,4`; dòng sông rơi ra chấm tàn lửa.
  - Vết chém lửa, vết cháy, khe nóng chảy và cắm kiếm thì có lửa, nhưng không có sao, vòng mảnh hay tia.

Vì vậy, ở phím 1 và phím 7, **mọi** lấp lánh của Metal đã bị thay bằng thân lửa, và Fire không có gì thay vào chỗ lấp lánh.

### 2.3 Fire ở phím 0, 2–6: lớp Metal tô lại

| Lớp của chiêu (không có hook) | Trong Fire hôm nay | Thấy ở tấm |
|---|---|---|
| Sáu ấn của chiêu `sigLine`, `sigArcs`, `sigArrow`, `sigHex`, `sigSpiral`, `sigCrack` | ánh sáng cộng màu `FIRE_GLOW`, **hồng cam nhạt** trên đá; chỉ `sigSeal` dưới chân là đặc | `audit-k3` mọi cột, `audit-k5` "fall", "open", "mid", `audit-k4` "charge" |
| Tia kiếm quét (`beamAt`), cột sáng (`pillar`), tia (`rays`), vòng xung (`shockAt`, `groundShockAt`) | cùng hồng cam nhạt | `audit-k2` "travel", "aftermath"; `audit-k5` "open" |
| `twinkle` của Metal (phím 2 dọc vạch, phím 4 lúc đến, phím 5 góc trận, phím 6 mưa) | **sao bốn cánh màu kem gần trắng**: chỗ duy nhất Fire có sao, nhưng là sao Metal, không phải sao lửa | `audit-k4` "arrive", `audit-k5` "open", `audit-k6` "wave2–3" |
| Vòng ngọc của Clear Wind (`motifAt`, `uJade` trên mọi ấn) | vẫn ngọc ở Fire (dấu O trên ấn; nổ vùng phím 2, 5) | `audit-k3`, `audit-k5` cận cảnh |
| Phím 6: cổng trời (`SkyGate`), bốn cột (`LightStrips`), vệt mưa, sao nứt và khe nứt (`GroundMarks` `MARK_STAR`, `MARK_RIFT`) | **lam như Metal** | `audit-k6` "gate" tới "aftermath" |

## 3. Bảng màu hào quang theo hệ, và màu dành riêng

Đề xuất thêm vào `ElementKit` một mục `radiance` (sáu vai dưới). Các lớp dùng chung ở §6 chỉ đọc mục này. Metal lấy từ màu đang có; Fire lấy từ dải màu của `element-fire.ts` và FIRE_STYLE §4.1, đã tránh màu dành riêng.

| Vai | Dùng cho | Metal | Fire | Lớp sáng |
|---|---|---|---|---|
| `core` | lõi sao, đầu vệt, lõi tia | trắng lam `[0.62, 0.88, 1.0]` (`METAL.ramp.core`) × 2,5–3,5 | ngà `#FFF4DC` × 2,5–3 | HDR, **chỉ 1–2 px** |
| `arm` | cánh sao, thân tia mảnh | vành của ô (`CLEAR_WIND_TONE`, ví dụ phím 1 `#1f9ee8`) pha 40 % về `#CFEFFF` | hổ phách cam `#FF9A3C` (sắc ~29°) | ≤ 0,85 |
| `ring` | vòng mảnh, cung, đoạn ấn | như `arm` | thân son `SEAL_BODY` `#E0561A`, vạch trong `SEAL_LIT` (`#FFAE34` × 0,9) | ≤ 0,9 |
| `run` | ánh chạy dọc nét | trắng lam × 2 (lõi 1 px) | `SEAL_CORE` `[1, 0.72, 0.3]` × 2 | lõi 1 px HDR |
| `glit` | bụi lấp lánh | bạc `#DCEBF2` | ngà vàng nhạt `#FFE6BE` | ≤ 0,85; lóe 2 khung, lõi × 2 |
| `soot` | lót tối dưới sao, vòng trên đá sáng | mực `[0.045, 0.05, 0.065]` | than `SEAL_SOOT` `#17140F` | trộn thường |

**Màu dành riêng** (canon §21.1). Cổng của SWORD_AURA §6: điểm ảnh hào quang trong ±6° sắc và ±0,1 độ sáng của `#FFB020`, `#FFC83A`, `#7FF5E0` ≤ 3 %, và không gì gần `#FF4A4A`.
- **Vàng kim `#FFC83A` là tiền và đồ rơi.** Bụi vàng lấp lánh rất dễ đọc thành "rơi đồ". Vì vậy `glit` của Fire là ngà nhạt (độ sáng ~0,87, cách dải dành riêng > 0,1), không phải vàng bão hòa. `arm` là cam 29°, ngoài dải 34–49°.
  - **Chỗ ngược với FIRE_STYLE:** các màu "vàng" `#FFB43A` (A), `#FFD866` (B), "sáng" `#FFB703` (B) đều nằm trong dải của `#FFC83A` hoặc `#FFB020`. Làm nét mảnh thì còn dưới 3 %. Làm **bụi vàng của hướng B** thì không; ở đó dùng `#FFE6BE`.
- **Metal phím 3 (Returning Sword Aegis)** dùng champagne `#cfa65a` (sắc ~39°, độ sáng ~0,58). Màu này nằm trong dải của cả `#FFB020` lẫn `#FFC83A`, nên phải đo; lớp hào quang thêm vào phím 3 dùng ngà trắng `#FFF6E0`, không thêm champagne.
- **Metal phím 5, 6** dùng ngọc `#7fdcaa`, `#86e2b6` (sắc 147–151°, cách xanh ngọc sức gõ 170° khoảng 20°). Lấp lánh của hai chiêu này dùng bạc, không dùng ngọc, để không trôi về màu sức gõ.
- **Không lớp hào quang nào nằm trên thẻ chữ hay trên thú** (luật "Every shape sparkles"): sao va chạm đặt lệch khỏi thân thú về phía nhát chém; trần độ sáng trong vùng chữ như SWORD_AURA §6.

## 4. Từng chiêu, từng pha

**Cách đọc bảng đề xuất:**
- **Cỡ** tính ở camera chơi 1080p (~39 px/m). Ngoặc là cỡ kẹp ở cận cảnh: sao và tia của `GlintPool` có **kẹp cỡ trên màn hình** (FIRE_STYLE §4), để cận cảnh không thành sao giao diện khổng lồ.
- **Nhịp** tính theo khung 60 Hz từ f0 của pha. "1–1–4" nghĩa là lên 1 khung, giữ 1, xuống 4.
- **Màu** ghi theo vai ở §3, áp cho mọi hệ.
- **Bloom:** "lõi" là lõi HDR 1–2 px; "≤ 0,9" là không bloom.
- **Giảm chuyển động** theo VFX_STANDARD §3.8:
  - `keep`: giữ, vì mang thông tin (mức nạp, vùng trúng);
  - `soften`: đỉnh × 0,6, số × 0,6, không lấp lánh lại, ánh chạy đứng yên thành vạch sáng;
  - `drop`: bỏ.
- **Chi phí** là ước tính p95 ở High, chưa đo (§7).

Hào quang ở mỗi pha theo luật Riot đã kiểm ở FIRE_STYLE §2: **một họ chính mỗi pha**, sang nhờ chỗ đặt chứ không nhờ số lượng; đòn thường tiết chế, tuyệt kỹ mới dày.

### 4.0 Phím 0 · Flying Sword (K0, `auto`, đòn thường, bậc 1)

| Pha | Hình chính | Quanh hình · Metal | Quanh hình · Fire | Đọc ở camera chơi (M / F) |
|---|---|---|---|---|
| Tụ lực | không có (đòn không chữ) | — | — | — |
| Phóng f0 | chớp ở tay, ấn dưới chân bừng | flare, sao lõi, sao sau lưng, 8 + 6 tia, hai vòng xoay ở tay, vòng xung, vòng đất, 10 tia lửa tròn, 8 hạt | điểm lửa, vòng lửa ở tay, hoa sen sau lưng, tia nan bánh xe, tàn lửa tròn | Có (sao 60–80 px, 3–8 khung, hơi trắng) / Không |
| Bay | kiếm thật | (SWORD_AURA) | (SWORD_AURA) | ngoài phạm vi |
| Va chạm +18 | khung đồ họa cục bộ, bóng thú lóe | sao kép, 6 tia, vòng đất, vòng xung dày, tia lửa vệt + hạt tròn, vết mực; khung F15 là sao gai đen | điểm lửa, hoa sen, tia nan, tàn lửa tròn, trăng lửa | Có nhưng thô (bong bóng, sao gai đen) / Không |
| Dư âm | — | quầng đất, hạt tròn 1,2 s | đất cháy, lửa thấp, khói, tàn lửa tròn | Yếu / Không |

| Mã | Pha | Lớp (§6) | Neo | Cỡ | Nhịp | Màu | Bloom | Giảm | Chi phí |
|---|---|---|---|---|---|---|---|---|---|
| R0.1 | Phóng | `GlintPool`: 1 sao lớn + 2 sao nhỏ | tay, đẩy 0,2 m theo hướng ném; sao nhỏ lệch ±0,3 m | 10–12 / 5–7 px (20–28 / 12–16) | lớn f0, 1–1–4; nhỏ f2, f4 | `core`, `arm` | lõi | soften | < 0,01 ms |
| R0.2 | Phóng | `ThinRays`: 3–4 tia mảnh theo hướng ném (thay 14 tia dày) | tay | 1,5 px × 25–40 px | f0–f6 | `arm`, lõi `core` | lõi 1 px | drop | < 0,01 |
| R0.3 | Va chạm | `GlintPool` "ting ting": 1 lớn + 2 nhỏ nối nhau, lệch khỏi thân thú về phía nhát | điểm trúng | 12–14 / 6–8 px | f0, f2, f4; mỗi sao 6 khung | `core`, `arm` | lõi | soften | < 0,01 |
| R0.4 | Va chạm | `HairlineRing` trên đất (thay vòng xung `circle_03` dày) | chân thú | 1,5–2 px; r 0,3 → 1,2 m (12 → 47 px), một cung vỡ | f1–f14 | `ring` | ≤ 0,9 | keep | < 0,01 |
| R0.5 | Va chạm | `GlitterMotes` họ vệt: 4–6 vệt mảnh trong 2 chùm theo hướng đòn (thay tia lửa tròn và hạt tròn) | điểm trúng | 1,5 × 8–16 px, đầu sáng | f0–f18 | đầu `core`, thân `arm` | đầu 1 px | soften | 0 (trong pool S3) |
| R0.6 | Dư âm | `GlitterMotes` họ bụi: 3–4 hạt lắng xuống; Fire thêm 0–1 lóe/s trên khe nứt của vết cháy | vết trúng | 1,5–2 px; lóe 5 px | 0,6–1,0 s | `glit` | ≤ 0,85 | soften | 0 |

### 4.1 Phím 1 · Threefold Sword Command (K1, `k1`, bậc 2)

| Pha | Hình chính | Quanh hình · Metal | Quanh hình · Fire | Đọc ở camera chơi (M / F) |
|---|---|---|---|---|
| Tụ lực (5 chữ) | ấn dưới chân + ba kiếm hiện sau vai | quầng `light_01` hai lớp sau lưng, đĩa sáng, hạt bay lên, hạt khí xoáy vào tay; mỗi phím chấm sáng + sao + vòng đất; kiếm đến: cột sáng + sao + hạt | ấn đặc (son trên than), `fire-charge` ở tay, chấm trắng vàng, tàn lửa hút vào; kiếm đến: hoa sen nhỏ + điểm lửa + tia nan | Có (quầng, hạt 2–4 px) / Yếu (lửa ở tay đọc; không quầng, không sao) |
| Phóng f0 | chớp ở tay | như phím 0, bậc 2 | như phím 0 | Có / Không |
| Phóng kiếm 2, 3 (+30, +60) | kiếm rời vai | flare, sao, vòng xung, 5 tia ở vai | hoa sen 1 m, điểm lửa, tia nan | Có / Không |
| Bay | ba kiếm | (SWORD_AURA) | (SWORD_AURA) | ngoài phạm vi |
| Va chạm ×3 (+6, +36, +66) | đòn xuyên + trăng cắt | như phím 0 (sao kép, bong bóng, sao gai đen) | hoa sen, điểm lửa, trăng lửa, tàn lửa tròn | Có, thô / Không |
| Dư âm | — | quầng đất, hạt tròn; sau ~0,8 s trống | đất cháy, lửa thấp, tàn lửa tròn | Yếu / Không |

| Mã | Pha | Lớp | Neo | Cỡ | Nhịp | Màu | Bloom | Giảm | Chi phí |
|---|---|---|---|---|---|---|---|---|---|
| R1.1 | Tụ lực | `CasterMandorla`: quầng sau lưng + một vòng mảnh khép lại theo phím. Metal: quầng `light_01` hiện có + vòng; Fire: quầng nhiệt (thân `arm` ≤ 0,6) + vòng son vàng | sau lưng người (`behindCaster`) | quầng 1,6 → 4 m (60 → 150 px); vòng 1,5 px, r 1,1 → 0,8 m | theo mức gõ, ease | `arm`, `ring` | ≤ 0,9 | keep (mức nạp) | ~0,01 |
| R1.2 | Mỗi phím | `GlintPool` 1 sao nhỏ ở chuôi kiếm trong tay + `RunningLight` chạy một vòng quanh ấn | tay; nét ấn | 6–8 px; đoạn sáng 8–12 px trên nét 1,5–2 px | sao 1–0–4; đoạn chạy 0,25 s | `core`, `run` | lõi | soften | < 0,01 |
| R1.3 | Tụ lực | `GlitterMotes` họ bụi xoáy vào tay (thay hạt khí và tàn lửa tròn), lóe 2 khung khi gần tay | vòng 1,4–2,4 m quanh tay | 1–2 px | sống 0,25–0,45 s | `glit` | ≤ 0,85 | soften | 0 |
| R1.4 | Kiếm đến chỗ | `GlintPool` 1 sao vừa ở mũi kiếm + `HairlineRing` mặt camera nhỏ (Fire: thay tia nan bánh xe) | ổ sau vai | sao 8–10 px; vòng r 0,2 → 0,6 m (8 → 23 px) | sao 1–1–4; vòng f1–f10 | `core`, `arm`, `ring` | lõi | soften | < 0,01 |
| R1.5 | Phóng | như R0.1, R0.2 + một `HairlineRing` mặt camera ở tay, trễ 2 khung sau vòng lửa (Fire) hoặc thay vòng xung dày (Metal) | tay | vòng r 0,3 → 1,2 m, 1,5 px | f2–f14 | `ring` | ≤ 0,9 | soften | < 0,01 |
| R1.6 | Phóng kiếm 2, 3 | 1 sao vừa + 2 tia mảnh theo hướng bay | vai | 8–10 px; tia 1,5 × 20 px | 1–1–4 | `core`, `arm` | lõi | soften | < 0,01 |
| R1.7 | Va chạm ×3 | R0.3–R0.5; đòn thứ ba (lớn) thêm vòng thứ hai trễ 3 khung và sao lớn 14 px | điểm trúng | như R0.3, R0.4 | như R0.3, R0.4 | như trên | lõi | soften / keep | < 0,02 |
| R1.8 | Dư âm | R0.6; Fire thêm `RunningLight` dọc mép nóng của vết cháy (`GroundDecalPool` heat edge), một lượt | vết cháy | đoạn sáng 6–10 px | 0,6–1 s, một vòng | `run` | lõi 1 px | soften | 0 |

### 4.2 Phím 2 · Cloud-Piercing Line (K2, `k2`, bậc 3)

| Pha | Hình chính | Quanh hình · Metal | Quanh hình · Fire | Đọc ở camera chơi (M / F) |
|---|---|---|---|---|
| Tụ lực (6 chữ) | vạch ấn 14 m hiện dần trên đất, kiếm ở tay | vạch sáng lam, quầng và hạt quanh người | vạch hồng cam nhạt (Metal tô lại), không quầng | Có / Yếu, sai chất |
| Phóng f0 | chớp, cột sáng sau lưng, hai tia kiếm quét 14 m | flare, sao, tia, cột | hoa sen + vòng lửa; tia quét và cột hồng cam nhạt | Có / Yếu |
| Bay (0,2 s) | kiếm chạy dọc vạch | sao mũi 2 m chạy theo lưỡi, tia tách hai bên (vệt tròn), dải | như Metal; sao là sao Metal màu kem | Có / Yếu |
| Va chạm +12 | khung đồ họa tối; trăng cắt ở từng thú; vạch bừng; nổ đầu xa | 9 sao + 9 trăng dọc vạch cùng lúc; nổ đầu xa (sao kép, quầng, vòng xung, tia lửa tròn, vòng ngọc) | hoa sen ở từng thú, trăng lửa; 9 sao Metal màu kem; vạch hồng; vòng ngọc vẫn ngọc | Có (sau khung đồ họa) / Yếu |
| Dư âm | vạch nguội thành tro, khói xám, ba điểm dư âm | hạt tròn bay lên; tắt trong ~1 s | ba đất cháy, vạch hồng tắt | Yếu / Không |

| Mã | Pha | Lớp | Neo | Cỡ | Nhịp | Màu | Bloom | Giảm | Chi phí |
|---|---|---|---|---|---|---|---|---|---|
| R2.1 | Tụ lực | `RunningLight` dọc vạch ấn, mỗi phím một đoạn chạy từ chân tới đầu đang lan; một sao nhỏ dẫn ở đầu vạch. Fire: vạch thành ấn đặc (`SigilLook` cho `sigLine`, §8 bước 3) | vạch ấn | đoạn sáng 10–16 px trên nét 2 px; sao 6 px | đoạn 0,2 s mỗi phím; sao sống suốt lúc gõ, thở 0,6–1 | `run`, `core` | lõi 1 px | soften | < 0,01 |
| R2.2 | Phóng | R0.1 (bậc 3: sao lớn 12–14 px) + `ThinRays` 4–6 tia; Metal giữ cột sáng; Fire: cột thành trụ lửa mảnh lõi vàng (hướng C của FIRE_STYLE) | tay, sau lưng | sao 12–14 px; tia 1,5 × 30–45 px | 1–1–5 | `core`, `arm` | lõi | soften | < 0,02 |
| R2.3 | Bay | sao mũi do `TipStar` của SWORD_AURA lo (ngoài phạm vi); tia tách hai bên thành `GlitterMotes` họ vệt | đầu kiếm | vệt 1,5 × 10–20 px | suốt 0,2 s | `core`, `arm` | đầu 1 px | soften | 0 |
| R2.4 | Va chạm | `GlintPool` **chuỗi sao chạy**: một sao mỗi 1,5 m dọc vạch, theo thứ tự từ gốc tới ngọn, mỗi sao trễ 1 khung, lớn nhỏ xen (thay 9 sao Metal cùng lúc); đầu xa 1 sao lớn + `HairlineRing` hai lớp. Fire: vòng ngọc thay bằng vòng của hệ | dọc vạch; đầu xa | 10 / 6 px xen; đầu xa 14 px, vòng r 0,3 → 2,2 m | chạy 9 khung; mỗi sao 1–1–4; vòng 2 trễ 3 khung | `core`, `arm`, `ring` | lõi | soften | ~0,01 |
| R2.5 | Dư âm | `RunningLight` một lượt dọc vạch khi nguội; 0–2 lóe/s trên vạch trong 1,2 s; `GlitterMotes` bụi bay lên (thay hạt tròn). Fire: vạch thành khe nóng chảy như vết cắt phím 7 | vạch | đoạn 12 px; lóe 5–7 px | 0,5 s chạy; lóe 1,2 s | `run`, `glit` | lõi 1 px | soften | < 0,01 |

### 4.3 Phím 3 · Returning Sword Aegis (K3A, `guard`, bậc 3, giữ 5 s)

| Pha | Hình chính | Quanh hình · Metal | Quanh hình · Fire | Đọc ở camera chơi (M / F) |
|---|---|---|---|---|
| Tụ lực (5 chữ) | ba cung quanh người (r 2 m) + ấn | cung champagne, hạt, quầng | cung **hồng cam nhạt**, không quầng | Có / Yếu, sai chất |
| Phóng f0 | ba kiếm vào quỹ đạo, vòng xung r 2,6 m | flare, sao, cột, vòng xung dày | hoa sen, vòng lửa, vòng xung hồng | Có (vòng như bong bóng) / Yếu |
| Giữ (5 s) | ba cung nhịp sáng, vạch nét đứt, ba dấu O, ba kiếm quay + dải | cung sáng đều, vài hạt tròn | cung hồng, dấu O ngọc | Yếu / Yếu |
| Đỡ đòn | kiếm gần nhất chặn | sao kép, trăng, 7 tia, vòng đất, cột, vòng xung 2,4 m | hoa sen ở chỗ đỡ, trăng lửa, tia và vòng hồng | Có, to và mềm / Yếu |
| Đóng | kiếm vỡ | hạt + một sao | hạt + sao Metal màu kem | Yếu / Yếu |

| Mã | Pha | Lớp | Neo | Cỡ | Nhịp | Màu | Bloom | Giảm | Chi phí |
|---|---|---|---|---|---|---|---|---|---|
| R3.1 | Tụ lực | `RunningLight` vẽ cung theo phím, đầu cung đang mở có sao nhỏ; `CasterMandorla` (R1.1) | cung; sau lưng | sao 6 px; nét 2 px | theo phím | `run`, `core` | lõi 1 px | keep (cung là vùng đỡ) | < 0,01 |
| R3.2 | Phóng | `HairlineRing` hai vòng camera (thay vòng xung dày `circle_03`); một sao lớn ở tay | người | 2 px; r 0,4 → 2,6 m (16 → 100 px), vòng 2 trễ 3 khung | f1–f16 | `ring`, `core` | ≤ 0,9 / lõi | keep | < 0,01 |
| R3.3 | Giữ | **vành hào quang**: một đoạn sáng chạy quanh cung, cùng tốc độ quỹ đạo kiếm (`RunningLight` trên `sigArcs`); mỗi kiếm qua dấu O thì lóe một sao nhỏ; 2–4 hạt lấp lánh/s trong vòng, bay lên chậm. Fire: cung thành nét son đặc trên than, vạch vàng chạy | cung; dấu O | đoạn 12–18 px; sao 6–8 px; hạt 1–2 px | đoạn quay liên tục; sao 1–1–4 | `run`, `core`, `glit` (Metal: ngà trắng `#FFF6E0` thay champagne, §3) | lõi 1 px | soften | < 0,02 |
| R3.4 | Đỡ đòn | 1 sao lớn + 2 nhỏ; một cung vỡ `HairlineRing` nở về hướng đòn; 3 tia mảnh (thay 7 tia dày và vòng xung 2,4 m) | chỗ đỡ | 14 / 7 px; cung r 0,3 → 1,6 m | f0, f2, f4; cung f1–f12 | `core`, `arm`, `ring` | lõi | soften / keep | < 0,01 |
| R3.5 | Mất một nấc, đóng | dấu O tắt bằng một sao nhỏ + 4 hạt lấp lánh (thay hạt tròn) | dấu O | 6 px; hạt 1–2 px | 1–1–4; hạt 0,6 s | `core`, `glit` | lõi | soften | 0 |

### 4.4 Phím 4 · Flowing-Light Step (K3B, `dash`, bậc 2)

| Pha | Hình chính | Quanh hình · Metal | Quanh hình · Fire | Đọc ở camera chơi (M / F) |
|---|---|---|---|---|
| Tụ lực (4 chữ) | mũi tên ấn 5 m + ấn | quầng, hạt | mũi tên hồng cam nhạt, không quầng | Có / Yếu |
| Phóng f0 | người rời chỗ, bụi, dải thân, 4 vạch tốc độ | flare, sao, tia | hoa sen sau lưng, **ở lại điểm xuất phát** khi người đã đi | Có / Yếu |
| Lướt (0,2 s) | bóng mờ (cột sáng dọc 1,9 m) dọc đường, dải | cột sáng xếp hàng | cột hồng cam | Có / Yếu |
| Đến | bụi, vòng đất 1,8 m, sao, 6 tia | sao 1,6 m, tia, vòng | sao Metal màu kem, vòng hồng | Có / Có (nhưng là sao Metal) |
| Dư âm | — | hạt tròn | đất cháy nhỏ | Yếu / Yếu |

| Mã | Pha | Lớp | Neo | Cỡ | Nhịp | Màu | Bloom | Giảm | Chi phí |
|---|---|---|---|---|---|---|---|---|---|
| R4.1 | Tụ lực | `RunningLight` dọc mũi tên mỗi phím; sao nhỏ ở đầu mũi tên | mũi tên | đoạn 10 px; sao 6 px | 0,2 s mỗi phím | `run`, `core` | lõi 1 px | soften | < 0,01 |
| R4.2 | Phóng | 1 sao vừa + 3 tia mảnh ngược hướng lướt | chân người lúc rời | 10 px; tia 1,5 × 25 px | 1–1–4 | `core`, `arm` | lõi | soften | < 0,01 |
| R4.3 | Lướt | `GlitterMotes` họ vệt: 8–12 vệt song song hướng lướt, rơi lại sau người; mỗi bóng mờ một lóe nhỏ ở đỉnh | đường lướt | vệt 1,5 × 15–30 px; lóe 5 px | 0,2 s + tắt 0,4 s | `arm`, `core` | đầu 1 px | soften | 0 |
| R4.4 | Đến | 1 sao lớn + 2 nhỏ, `HairlineRing` đất, 4 tia mảnh; Fire tô bằng màu hệ (bỏ sao Metal kem) | điểm đến | 12 / 6 px; vòng r 0,3 → 1,8 m | f0, f2, f4; vòng f1–f14 | `core`, `arm`, `ring` | lõi | soften / keep | < 0,01 |
| R4.5 | Dư âm | bụi lấp lánh dọc đường lắng xuống | đường lướt | 1–2 px | 0,6 s | `glit` | ≤ 0,85 | soften | 0 |

### 4.5 Phím 5 · Falling Sword Array (K4, `k4`, bậc 3, giữ 5 s)

| Pha | Hình chính | Quanh hình · Metal | Quanh hình · Fire | Đọc ở camera chơi (M / F) |
|---|---|---|---|---|
| Tụ lực (6 chữ) | lục giác r 3,55 m hiện dần ở đích; mỗi phím một góc sáng | hạt, cột sáng 2,2 m, sao ở góc; quầng ở người | góc: hoa sen nhỏ + điểm lửa + tia nan; lục giác hồng cam nhạt | Có / Yếu |
| Phóng f0 | chớp ở người | như phím 2 | như phím 2 | Có / Yếu |
| Rơi +8, mở +12 | 6 kiếm cắm ở 6 góc; nổ giữa | va chạm ở góc, cột 4,8 m, vòng đất, vòng 3,7 m, 10 tia 3,2 m, sao kép giữa, vòng ngọc | hoa sen ở góc; lục giác, tia, cột **hồng**; sao Metal kem | Có (rất sáng) / Yếu, sai chất |
| Nhịp (mỗi 30 khung, 5 s) | tia nối góc, đòn nhẹ lên thú trong trận | sao ở thú đánh dấu, tia lửa tròn, mực; sao giữa, vòng xung | như Metal nhưng hồng | Có / Yếu |
| Giữ | đĩa tối, vết nứt giữa, cột ở góc thở | sáng đều | hồng | Yếu / Yếu |
| Đóng +300, dư âm | kiếm vỡ, dư âm r 3,2 m | hạt + sao, hạt bay lên | **tấm lửa đất lớn, đáy thẳng** ở giữa trận (§10) | Yếu / Không |

| Mã | Pha | Lớp | Neo | Cỡ | Nhịp | Màu | Bloom | Giảm | Chi phí |
|---|---|---|---|---|---|---|---|---|---|
| R5.1 | Tụ lực | mỗi góc hiện: 1 sao vừa + `HairlineRing` đất nhỏ; `RunningLight` nối góc vừa hiện với góc trước, như nét bút sáng vẽ cạnh lục giác | góc; cạnh | sao 8–10 px; vòng r 0,2 → 0,6 m; đoạn 12 px | sao 1–1–4; đoạn 0,25 s | `core`, `ring`, `run` | lõi | keep (vùng trận) | < 0,01 |
| R5.2 | Mở | 6 sao ở 6 góc **lệch nhịp theo chiều kim đồng hồ**, mỗi góc trễ 1 khung (thay 6 sao cùng lúc); `HairlineRing` hai lớp ở tâm; 10 tia giữ số nhưng mảnh 1,5 px | góc; tâm | sao 10–12 px; vòng r 0,5 → 3,7 m (20 → 145 px) | 6 khung chạy; vòng 2 trễ 3 khung, f1–f18 | `core`, `arm`, `ring` | lõi | soften / keep | ~0,01 |
| R5.3 | Nhịp | một đoạn sáng chạy một vòng quanh lục giác mỗi nhịp; sao nhỏ ở góc khi đoạn sáng đi qua; sao ở thú trúng chỉ cho phần thú đánh dấu, trần 12 mỗi nhịp | cạnh; góc; thú | đoạn 14 px; sao 6–8 px; sao thú 5–7 px | vòng chạy 0,25 s; sao 1–0–4 | `run`, `core` | lõi 1 px | soften | < 0,02 |
| R5.4 | Giữ | 3–6 hạt lấp lánh/s bay lên trong trận (trần 24 sống); 0–1 lóe/s ở chỗ vết nứt giao nét ấn | trong lục giác | hạt 1–2 px; lóe 6 px | hạt 0,8–1,2 s | `glit` (Metal: bạc, không ngọc), `core` | ≤ 0,85 / lõi | soften | < 0,01 |
| R5.5 | Đóng | 6 sao nhỏ tắt nối nhau ở 6 góc; vòng mảnh co về tâm (đảo của lúc mở) | góc; tâm | 6 px; vòng r 3,7 → 0,5 m | 6 khung chạy; vòng 14 khung | `core`, `ring` | lõi | soften | < 0,01 |

Fire: lục giác thành ấn đặc với vạch vàng chạy. Hướng C · Halo Seal của FIRE_STYLE khớp đúng chiêu này (trụ lửa đứng ở góc, vòng mảnh, sao ở giao điểm).

### 4.6 Phím 6 · Milky-Way Sword Rain (K5, `k5`, tuyệt kỹ, bậc 5)

| Pha | Hình chính | Quanh hình · Metal | Quanh hình · Fire | Đọc ở camera chơi (M / F) |
|---|---|---|---|---|
| Tụ lực (8 chữ) | ấn xoắn ốc ở đích, vùng tối 7,2 m; vòng 24 kiếm sau lưng người | hạt lam bay lên trong vùng, quầng ở người | xoắn ốc hồng cam; kiếm có lớp cam (phần kiếm: SWORD_AURA); không hạt | Có / Yếu |
| Cut-in (0,9 s ở lượt chụp) | tranh + lời hô | tranh thiên hà lam | **cùng tranh lam** | (khung màn hình) |
| Phóng f0 | cột sáng 26 m từ tay lên trời, vòng đất 3,2 m | flare, sao, tia, cột | hoa sen, vòng lửa; cột sáng màu kem hồng | Có / Yếu |
| Cổng +10 | vòng cổng trời trên cao, bốn cột sáng xuống sân | vòng lam trắng, cột lam | **vẫn lam** | Có / sai hệ |
| Mưa +24 tới +66 | kiếm dẫn đầu, ba đợt mưa; mỗi kiếm chạm đất: tia lửa, vòng, sao, dấu sao nứt | sao 1,2–2,6 m, vòng xung lam, bóng thú trắng | hoa sen ở thú lớn; vệt mưa **lam**, sao Metal kem, dấu sao nứt **lam** | Có (dày) / lẫn hai hệ |
| Cao trào +93 | khung đồ họa đảo màu | lam | cam (đã đúng hệ) | Có / Có |
| Kiếm trời +110 | kiếm khổng lồ rơi; flare, vòng 11 m, vòng xung 7 m, 20 tia lửa, khe nứt 22 m | khe nứt lam như sét, sao nứt | **khe nứt lam như sét** trên sân lửa | Có / sai hệ |
| Dư âm tới +234 | khe nứt nguội, hạt bay lên dọc khe; cổng đóng | lam | lam | Yếu / sai hệ |

| Mã | Pha | Lớp | Neo | Cỡ | Nhịp | Màu | Bloom | Giảm | Chi phí |
|---|---|---|---|---|---|---|---|---|---|
| R6.1 | Tụ lực | `RunningLight` chạy dọc ba nhánh xoắn ốc theo phím; `GlitterMotes` bụi bay lên trong vùng (thay hạt tròn); `CasterMandorla` cỡ tuyệt kỹ | ấn xoắn; vùng r 6 m; người | đoạn 16 px; hạt 1–2 px | theo phím | `run`, `glit`, `arm` | lõi 1 px | keep (vùng) / soften | < 0,02 |
| R6.2 | Phóng | 1 **sao sáu cánh** (biến thể tuyệt kỹ của `GlintPool`) ở tay + 8 `ThinRays`; cột lên trời giữ, Fire thành cột lửa lõi vàng | tay | 20–28 px (cận 40); tia 2 × 40–60 px | 1–2–8 | `core`, `arm` | lõi | soften | < 0,01 |
| R6.3 | Cổng | cổng thành ba `HairlineRing` đồng tâm có ánh chạy, một vòng ánh cầu vồng nhẹ (khung 9 của FIRE_STYLE); sao nhỏ ở chân mỗi cột. Fire: cổng lửa (§8 bước 3) | vòng cổng; chân cột | vòng 1,5–2 px; sao 8 px | mở 0,35 s; ánh chạy 1 vòng/s | `ring`, `run`, `core` | ≤ 0,9 / lõi 1 px | keep | ~0,01 |
| R6.4 | Mưa | sao chỉ ở kiếm dẫn đầu khi chạm (1 lớn + 1 nhỏ); kiếm thường 30 % có sao nhỏ, trần 16 sao sống; tia lửa thành vệt (`GlitterMotes`) | điểm chạm | 14 / 6 px | 1–1–4 | `core`, `arm` | lõi | soften | ~0,02 |
| R6.5 | Kiếm trời | sao sáu cánh lớn ở tâm + vòng mảnh 11 m thay vòng xung dày; 8 tia mảnh | tâm | 28–36 px; vòng 2 px r 0,8 → 11 m | f0 1–2–10; vòng f1–f24 | `core`, `ring` | lõi | soften / keep | ~0,01 |
| R6.6 | Dư âm | `RunningLight` dọc khe nứt (Fire: khe nóng chảy; Metal: khe ánh lam), 0–3 lóe/s ở chỗ khe rẽ nhánh, bụi lấp lánh bay lên (trần 120) | khe 22 m | đoạn 20 px; lóe 6–8 px | 2 s, ánh chạy 2 lượt | `run`, `core`, `glit` | lõi 1 px | soften | < 0,02 |

### 4.7 Phím 7 · Myriad Swords (`k7`, chiêu cả sân)

| Pha | Hình chính | Quanh hình · Metal | Quanh hình · Fire | Đọc ở camera chơi (M / F) |
|---|---|---|---|---|
| Phóng F0 | 8 kiếm rời tay, chớp, cột sau lưng | flare, sao, tia, cột (bậc 3) | hoa sen 1,55×, vòng lửa, vết cháy, chớp ấm | Có / Không |
| Mở F1–20 | thế giới tối, khe ngọc trên trời, hạt giống bay lên | lam | lam (khe trời không đổi theo hệ) | Yếu / Yếu |
| Săn F30–168 | dòng sông kiếm (phần kiếm: SWORD_AURA), kiếm lao xuống thú | đòn sông: vệt cắt hẹp, sao ×3,2 trong 0,09 s, 2 vệt; kiếm dẫn: một vòng đất lớn (sprite `marks`, cỡ 1,2 → 6,5); dòng sông rơi lấp lánh (90/s, `glitter`, sao) | đòn sông: điểm nhỏ, tia nan, 3 tàn lửa tròn; kiếm dẫn: hoa sen + đất cháy; `glint` và dòng sông: **chấm tròn** | Có / Không |
| Gom F168–192 | mọi kiếm xoắn rồi xếp thành một nét chéo | lam | cam | Yếu / Yếu |
| Nhát kết F192 | vết chém cả sân; khung đồ họa; vết cắt trên thú lớn; cắm kiếm (thú anh hùng) | đầu vệt trắng chạy, vòng lam ở chỗ cắm, sao ở chỗ cắm | vết chém lửa có lưỡi lửa, khe nóng chảy, hoa sen ở chỗ cắm, vòng lửa trên đất | Có / Yếu (lửa đọc, không sao) |
| Dư âm F207+ | vết mực và khe sáng (Metal), vết cháy + lửa thấp + khe nóng chảy (Fire) | vài sao, khe sáng | tàn lửa tròn, khe mảnh | Yếu / Không |

| Mã | Pha | Lớp | Neo | Cỡ | Nhịp | Màu | Bloom | Giảm | Chi phí |
|---|---|---|---|---|---|---|---|---|---|
| R7.1 | Phóng | như R2.2 (bậc 3) | tay | 12–14 px | 1–1–5 | `core`, `arm` | lõi | soften | < 0,01 |
| R7.2 | Săn, đòn sông | Fire: hook `glint` vẽ sao bốn cánh nhỏ (thay chấm tròn), đòn sông có một sao 5–7 px ở 1/3 số đòn; bỏ tia nan bánh xe. Metal giữ sao hiện có, đổi hạt tròn thành vệt | thú trúng, lệch khỏi thân | 5–7 px | 1–0–3 | `core`, `arm` | lõi | soften | **≤ 0** (bỏ `fire-sparks` bù vào) |
| R7.3 | Săn, kiếm dẫn | 1 sao lớn + 1 nhỏ + một `HairlineRing` đất (Fire thêm vào; Metal đổi vòng `marks` dày sang vòng mảnh) | điểm bổ | 14 / 6 px; vòng r 0,4 → 1,8 m (16 → 70 px) | f0, f2; vòng f1–f30 | `core`, `ring` | lõi | soften / keep | < 0,01 |
| R7.4 | Săn, lấp lánh dòng sông | `GlitterMotes` họ bụi thay chấm `ember()` của Fire: hạt 1–2 px lóe 2 khung, trôi theo dòng; số giữ 90/s | dọc dòng sông | 1–2 px | 0,2–0,4 s | `glit`, `core` | lõi × 2 lúc lóe | soften | **≤ 0** (thay chấm tròn) |
| R7.5 | Nhát kết | `RunningLight` theo đầu vết chém (đã có đầu trắng ở Metal; Fire thêm vào `FlameSlash`); sao ở mỗi chỗ cắm kiếm; bụi lấp lánh rơi khỏi đuôi vết | vết chém; chỗ cắm | đoạn 20–30 px; sao 12 px | 0,26 s chạy; sao 1–1–5 | `run`, `core`, `glit` | lõi | soften | < 0,02 |
| R7.6 | Dư âm | `RunningLight` dọc khe nóng chảy (Fire) hoặc khe sáng (Metal), 0–2 lóe/s ở khe, trần 8 sao sống | khe | đoạn 16 px; lóe 6 px | 1,5–3 s | `run`, `core` | lõi 1 px | soften | < 0,01 |

Ở phím 7, trần 48 sao sống (FIRE_STYLE §5.3) giữ nguyên. Dòng sông 88 thanh không được thành "rắc kim tuyến khắp nơi".

## 5. Xếp hạng chỗ thiếu: anh sẽ thấy cái nào trước

| Hạng | Chỗ thiếu | Ở đâu | Vì sao anh thấy ngay |
|---|---|---|---|
| 1 | **Fire không có một điểm lấp lánh nào của riêng nó** (sao, vòng mảnh, tia, ánh chạy) | phím 1, phím 7, mọi pha; `glint` của phím 7 là chấm tròn | Đúng hai chiêu anh đã xem và chê; đúng chữ "lấp lánh, long lanh hào quang" |
| 2 | **Tuyệt kỹ phím 6 trong Fire vẫn lam**: cổng, cột, vệt mưa, sao nứt, khe nứt như sét, tranh cut-in | `audit-k6` từ "gate" tới "aftermath" | Chiêu to nhất, kéo dài 4 s, kết thúc bằng sét lam trên sân lửa; trái D59 ("chủ đạo phải là lửa") |
| 3 | **Ánh sáng Metal tô lửa thành hồng cam nhạt**: ba cung, lục giác, vạch, mũi tên, vòng xung, cột, tia | phím 2–6 trong Fire | Đây là các hình lớn nhất trên màn (lục giác ~250 px, vòng cung ~160 px). Chúng không ra lửa, cũng không ra vàng rực; trúng bẫy §8 của ELEMENT_LAYER |
| 4 | **Lúc tụ lực, Fire mất quầng hào quang** (quầng `light_01`, hạt bay lên, hạt khí) | mọi phím có chữ, Fire | Khoảnh khắc "hào quang" duy nhất khi gõ biến mất; người đứng giữa ấn trơ |
| 5 | **Dư âm trơ trọi** | Metal: sau ~0,8 s không còn gì ở phím 0, 1, 2, 4; Fire: chỉ vết cháy và tàn lửa tròn | Anh vừa chê lửa "biến mất hơi nhanh"; lấp lánh cũng tắt cùng lúc |
| 6 | **Hạt tròn ở cả hai hệ** (đĩa `circle_05` của Metal, tàn lửa và chấm `ember()` của Fire) | mọi pha có hạt | Anh đã gọi tia lửa là "khá thô"; hạt lam của Metal là cùng một lỗi, chỉ nhỏ hơn |
| 7 | **Ấn và vạch không có ánh chạy, không sao ở giao điểm** | 7 ấn, vạch phím 2, khe phím 6 và 7, vết nứt đất cháy | Hình lớn đứng yên vài giây mà không "sống"; hướng C của bảng FIRE_STYLE dựa đúng vào lớp này |
| 8 | **Va chạm Metal thô**: một kiểu sao, giữa là sao gai đen của khung F15, vòng xung dày như bong bóng, tia dày 4–8 px | phím 0, 1, 3, 5 | Metal có sao nhưng không ra trang sức; anh đồng ý Metal cũng đổi (SWORD_AURA Q2) |
| 9 | Fire phóng giống hệt nhau ở mọi chiêu (cùng hoa sen sau lưng) | phím 0–7 | Mất dấu riêng của từng chiêu (skill bước 3 "Give each action its own shape") |
| 10 | Vòng ngọc Clear Wind (`motifAt`, `uJade`) vẽ bằng ngọc trong Fire | dấu O trên ấn, nổ vùng | Lẫn màu; gần màu sức gõ nếu ngọc sáng lên |
| 11 | Champagne của Metal phím 3 nằm trong dải vàng dành riêng | `audit-k3` hàng Metal | Cần đo; anh có thể đọc là "vàng" |

## 6. Lớp dùng chung (dựng một lần cho mọi chiêu, mọi hệ)

Nguyên tắc:
- **Chỗ đặt hào quang thuộc hình của chiêu**, trong `sword-skills.ts` và `myriad-swords.ts`, như đường bay và số kiếm.
- **Màu thuộc hệ**, qua `ElementKit.radiance` (§3).
- Lớp hào quang **luôn chạy**, kể cả khi hook của hệ đã vẽ thân pha đó. Hôm nay hook `release` của Fire trả `true` thì mọi sao của Metal ở pha đó mất theo; tách ra thì Fire, Water và các hệ sau đều lấp lánh như nhau mà không cần mỗi kit tự vẽ lại.
- Luật "thay, không chồng" vẫn giữ: lớp hào quang thay sao, tia, vòng, hạt cũ của Metal (`twinkle`, `starPair`, `rays`, `shockAt`, `circle_05`), không vẽ chồng lên chúng.
- Công tắc lab `?radiance=off|on`: `off` phải trùng khít Metal hôm nay (`lab-element-parity.mjs`).

| Mã | Lớp | Dựng trên | Làm gì | Dùng ở | Lệnh vẽ | Ước tính |
|---|---|---|---|---|---|---|
| S1 | `GlintPool` | FIRE_STYLE §5.1 mục 1 (cùng một thứ, không dựng hai lần) | Sao vẽ giải tích, bốn cánh và sáu cánh (tuyệt kỹ). Cánh ≤ 0,85, lõi 1–2 px HDR. Cỡ tính bằng px, có kẹp. Lệch pha, xoay 0/45°. Thêm so với FIRE_STYLE: (a) **lấp lánh lại** (sao sống lâu, lóe lại mỗi 0,4–0,9 s, cho dư âm và vành giữ); (b) **neo theo vật** (một điểm của ấn, góc trận, kiếm khi chạm); (c) **chuỗi sao** (n sao dọc một đoạn, mỗi sao trễ k khung). **Hàm sao giải tích dùng chung với `TipStar` của SWORD_AURA** (`SwordAuraSprites`): một đoạn shader trong `fxkit.ts`, hai pool | mọi pha của mọi chiêu | +1 | 0,03–0,08 ms ở 48–64 sao sống |
| S2 | `HairlineRingPool` | FIRE_STYLE §5.1 mục 3 (mở rộng `HeatRingPool`, `GroundSigil`) | Vòng giải tích rộng 1,5–2 px qua `fwidth`; cung vỡ; một đoạn sáng chạy; mặt đất hoặc mặt camera; ≤ 0,9. Fire có thêm lớp lót than trong cùng shader | thay `circle_02`, `circle_03`, vòng `marks` của phím 7; vòng phóng, va chạm, cổng trời | 0–1 | 0,05–0,12 ms ở 24 vòng sống |
| S3 | `GlitterMotes` | chế độ vệt của `EmberPool` (FIRE_STYLE §5.1 mục 2), đưa ra dùng chung cho mọi hệ | Ba họ trong một pool GPU: **vệt** (tia lửa hình viên con nhộng, đầu nóng), **vảy** (tàn bay lên, thon), **bụi lấp lánh** (1–2 px, lóe 2 khung theo pha riêng của từng hạt, trôi hoặc lắng). Phát theo chùm hình nón, không đều 360° | thay hạt `circle_05` của Metal (`riseMote`, `burstMotes`, `sparkBurst`, `hitSparks`, hạt khí xoáy) và `ember()`, `dot()`, `emberBurst` tròn của Fire | 0 ở Fire; +1 ở Metal (Metal chưa có pool này) | ±0,05 ms (vệt mảnh tô ít điểm ảnh hơn đĩa tròn) |
| S4 | `RunningLight` | uniform trong shader sẵn có | Một đoạn sáng hẹp chạy dọc tọa độ nét: `GroundSigil` (7 ấn), `BeamPool` (vạch), `FlameSlash`, `QiSlash`, mép nóng của `GroundDecalPool`. Chỗ nét giao nhau gọi S1 | ấn, vạch, khe, vết chém, vết cháy | 0 | < 0,02 ms |
| S5 | `ThinRays` | preset của `BeamPool` | Tia 1–2 px theo `fwidth`, nhọn hai đầu, lõi 1 px; thay tia dày 0,1–0,2 m | phóng, va chạm lớn, đỡ đòn, mở trận, kiếm trời | 0 | 0,01–0,03 ms |
| S6 | `CasterMandorla` | pool `aura` (`light_01`) sẵn có + S2 + S3 | Quầng sau lưng lúc tụ lực, theo hệ: Metal giữ quầng hiện có và thêm vòng mảnh khép theo phím; Fire có quầng nhiệt + vòng son vàng + bụi lấp lánh xoáy vào. Đây là lớp bù cho hook `chargeFrame` của Fire | lúc tụ lực của 6 chiêu có chữ | 0–1 | 0,01–0,02 ms |
| S7 | `DarkUnderlay` | `GroundDecalPool` (FIRE_STYLE §5.1 mục 5), mở rộng cho mọi hệ | Đốm tối tạm thời dưới va chạm và dưới ấn lớn, để sao và vòng cộng sáng còn đọc được trên đá sáng | va chạm, mở trận, cổng | 0 | < 0,02 ms |

Còn thiếu ở `ElementKit` để hào quang đúng hệ: mục `radiance` (§3); `SigilLook` cho cả sáu ấn của chiêu, không chỉ `sigSeal`; hook `areaHit` và `areaBurst` cho Fire; cổng trời, cột, mưa và khe nứt của phím 6 đọc `StreamTone` hoặc một mục `ultimate` của kit thay cho màu Metal cố định; vòng ngọc (`motifAt`, `uJade`) đổi theo hệ.

## 7. Ngân sách

Mốc lấy từ lượt kiểm lại vòng 3 (changelog `games/immortality-cultivation/docs/changelog/2026-11-03-lab-element-fire.md`, phần 5 recheck):
- Fire − Metal p95, trung vị: nghỉ +0,10, phím 1 +0,30, phím 7 săn +0,20, nhát kết +0,35, K5 +0,50 ms. Cổng là ≤ 0,85.
- Trung vị p95 cao nhất 8,3 ms (K5 Fire); lượt tệ nhất 11,8 ms (Metal, nhát kết). Nhiễu giữa các vòng tới ±1,5 ms.
- SWORD_AURA giữ cho hào quang kiếm tới +0,6 ms lúc săn và +0,5 ms ở gom và nhát kết. Mốc của tài liệu đó cho phím 7: săn 10,2–10,5 ms, nhát kết 10,3–10,9 ms.

| Cửa sổ | Hào quang kiếm (SWORD_AURA) | Hào quang chiêu, đề xuất (mọi hệ, so với `radiance=off`) | Fire còn trong 0,85 ms | Cách bù |
|---|---|---|---|---|
| Phím 1 | +0,01–0,04 | ≤ +0,15 ms | ~0,55 | không cần |
| Phím 0, 2, 3, 4 | — | ≤ +0,15 ms | chưa đo | không cần |
| Phím 5 (trận 5 s) | — | ≤ +0,2 ms | chưa đo | thay tia dày và vòng xung bằng S2, S5 |
| Phím 6 (K5) | chưa ước tính (SWORD_AURA §6 chỉ đòi vòng kiếm cổng trời trùng khít) | ≤ +0,25 ms | ~0,35 | trần 16 sao ở mưa; vòng mảnh thay vòng xung 11 m |
| Phím 7 săn | ≤ +0,6 | **≤ +0,1 ms, lấy từ chỗ bỏ** | ~0,65 | bỏ flipbook `fire-sparks` (pool 64 thẻ cộng sáng), chấm `ember()` và `dot()` (`circle_05`, pool 900), vòng `marks` dày |
| Phím 7 gom, nhát kết | ≤ +0,5 | **≤ 0 ms (bù hết)** | ~0,50 | như trên; sao ở chỗ cắm kiếm trong trần 48 |

- **Số đếm:** sao sống ≤ 64 (≤ 48 ở phím 7); vòng mảnh ≤ 24; bụi và vệt nằm trong số hạt hiện có, vì chúng thay hạt tròn, không thêm (Fire ~1.900 lúc đông nhất); ánh chạy không tốn hạt.
- **Chồng lớp:** ≤ 2 lớp trong suốt ở một điểm ảnh (ELEMENT_LAYER §5). Ghi vào `meta.json` của lượt chụp.
- **Đo:** `lab-element-perf.mjs` với `radiance=off,on` xen kẽ, cùng cách đo của SWORD_AURA §6. Đo **khi đã bật hào quang kiếm**, vì hai lớp chia nhau khoảng trống ở phím 7. Chi phí từng lớp đo bằng `GpuTimer` nếu có.
- **Bloom và trắng xóa:** điểm ảnh > 1 do hào quang thêm ≤ +0,3 % khung; độ sáng ≥ 0,95 ≤ 6 % sân lúc đỉnh; lõi trắng ≤ 30 % một hình (VFX_STANDARD). Đo trên ba nền: mặc định, đá sáng `#d6d0c2`, nền tối.

## 8. Thứ tự làm

0. **Anh xem trước, chưa có mã:**
   - tám tấm `audit-k0.jpg` … `audit-k7.jpg`;
   - bảng hình của FIRE_STYLE (`board-fire-all.jpg`), trả lời FIRE_STYLE §7 câu 1–3 (hướng, độ dày lấp lánh, vòng ở mọi đòn hay chỉ đòn lớn);
   - các câu ở §9 dưới.
   Hướng anh chọn ở FIRE_STYLE quyết hình của S1, S2, S4 cho mọi hệ (sao kiểu trang sức của B, vòng và ấn của C, nét bút của A).
1. **Dựng lớp dùng chung** S1–S7 và mục `radiance`, sau khi vòng 3 của Fire xong và cùng lúc với `SwordAuraSprites` của SWORD_AURA (chung hàm sao).
   - Công tắc lab `?radiance=off|on`; Metal `off` trùng khít.
   - Mỗi lớp một commit, kèm test và ảnh chụp.
2. **Phím 1 và phím 7, cả Metal lẫn Fire:** 3–5 ứng viên cùng lúc theo kiểu anh chọn (ví dụ ba mật độ lấp lánh × có hoặc không có vòng), như FIRE_STYLE §6 bước 2.
   - Video và tấm ở camera chơi và cận cảnh, đá sáng và tối. Khi hai giám khảo chấm ≥ 7 thì gửi anh ngay.
   - Anh chọn một ứng viên.
3. **Bù phần Fire còn thiếu ở phím 0, 2–6.** Đây là nợ của lớp hệ, nhưng chặn lấp lánh, vì không thể rắc sao lên một lục giác màu hồng.
   - Sáu ấn của chiêu dùng `SigilLook` đặc.
   - Tia, cột, vòng xung, tia kiếm quét bằng chất lửa.
   - Hook `areaHit`, `areaBurst` cho Fire.
   - Phím 6: cổng, cột, mưa, sao nứt, khe nứt bằng lửa; tranh cut-in theo hệ là việc tranh, anh duyệt (`game-art-pipeline`).
   - Vòng ngọc theo hệ.
4. **Lấp lánh cho phím 0, 2–6** theo các bảng ở §4, mật độ theo ứng viên anh chọn ở bước 2, cả hai hệ.
5. **Dư âm lấp lánh** (R0.6, R1.8, R2.5, R5.4, R6.6, R7.6), sau khi độ lưu của vòng 3 được duyệt, để ánh chạy và lóe thưa sống cùng thân lửa.
6. **Đo đủ cổng** (§7, màu dành riêng ở §3, phần nhạt ≤ 15 % ở khung va chạm, thẻ chữ, giảm chuyển động). Sau đó hai giám khảo mù ≥ 8,5 ở bản chơi, không cờ URL. Anh xem cuối.
   - Ba lượt không lên điểm thì dừng, bàn với ChatGPT trước lượt thứ tư.

## 9. Câu hỏi cho anh

1. Độ dày lấp lánh ở camera chơi: tiết chế (đòn thường 1 sao lớn + 2 nhỏ, tuyệt kỹ dày) hay dày đều ở mọi chiêu?
2. Bụi lấp lánh của Fire: ngà nhạt (đề xuất, tránh màu vàng của tiền và đồ rơi), hay anh muốn vàng rực và chấp nhận gần màu đồ rơi?
3. Cổng trời của tuyệt kỹ trong Fire: thành cổng lửa (theo D59), hay giữ cổng trời "thiên giới" trung tính cho mọi hệ, chỉ mưa và khe nứt đổi theo hệ?
4. Metal có lấp lánh thêm như Fire không (đề xuất: có, cùng các lớp, màu Metal; anh đã đồng ý Metal đổi ở hào quang kiếm)?

## 10. Lỗi khác thấy khi chụp (không thuộc lớp hào quang)

Ghi lại để người điều phối chuyển cho đúng làn; tài liệu này không sửa.
- **Fire phím 5, dư âm:** lửa đất lớn giữa trận là một tấm lửa đáy thẳng, nửa dưới là vết cháy tối hình chữ nhật (`audit-k5` "close", "aftermath"). Lửa đất nhỏ ở phím 1, 2 cũng có gốc phẳng như cái mũ. Đây là phần hình lửa của FIRE_STYLE và vòng 3.
- **Fire phím 4:** hoa sen lúc phóng đứng lại ở điểm xuất phát, trong khi người đã lướt đi 5 m.
- **Tranh cut-in của tuyệt kỹ** là thiên hà lam ở mọi hệ.
- **Metal phím 0, 1:** khung đồ họa cục bộ (F15) vẫn là sao gai đen, ~200 px ở camera chơi, đọc như vết mực (Fire đã đổi ở vòng 3, Metal thì chưa).

## Nguồn

- Tấm và kịch bản: `games/immortality-cultivation/tmp/shots/fire-style/audit/` (`audit-k0.jpg` … `audit-k7.jpg`, `tools/audit-scenario.mjs`, `tools/sheets.sh`). Khung thô đã xóa sau khi làm tấm.
- Mã đọc, không sửa (`games/immortality-cultivation` `67b2026`):
  - `src/view/skills/sword-skills.ts`: `keyBeat`, `releaseFlash`, `impact`, `basicImpact`, `hitSparks`, `slashAt`, `strikeLight`, `areaHitMetal`, `burstAt`, `motifAt`, `aftermath`, `updateAura`, `updateCharge`, `updateK2`, `updateGuard`, `updateDash`, `updateK4`, `updateK5`, `setElement`, `applyColours`;
  - `src/view/skills/myriad-swords.ts`: `riverLight`, `impactAt`, `leadImpact`;
  - `src/view/skills/element-fire.ts`, `element-metal.ts`, `element-kit.ts`;
  - `src/lab/skills-main.ts`: `KEYS`, `WORD_LEN`, `TARGET`, `type`, API `__lab`.
- Tài liệu: `FIRE_STYLE.md` (§1–§6), `SWORD_AURA.md` (§1.2, §6, §7), `ELEMENT_LAYER.md` (§1, §2, §5, §8), `../00-canon.md` (§21.1, D54, D59), `../../VFX_STANDARD.md` (§3.4, §3.8), changelog Fire phần 5 recheck.
