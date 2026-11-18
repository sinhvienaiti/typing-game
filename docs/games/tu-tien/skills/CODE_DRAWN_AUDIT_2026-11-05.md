# Rà hình vẽ bằng code trong chiêu Tu Tiên (05/11/2026)

**Vì sao.** 04/11 lúc 23:50 anh chê lưỡi lửa gai nhọn của nhát chém kết phím 7 hệ Hỏa (`flame-slash.ts`): "thực sự rất xấu". Luật (`game-vfx-production`, `AGENTS.md`): hình lấy từ art (Firefly Video/Image, Blender, tranh vẽ, gói CC0); code chỉ đặt, canh nhịp và cho chuyển động. Phiếu 275 đã lo `flame-slash.ts`. Tài liệu này liệt kê mọi hình **khác** mà dáng của nó do toán trong shader hay canvas quyết định.

**Phạm vi và cách đo.**
- Đọc mã `main` của game ở `5de0d22`, chỉ đọc: `src/view/skills/*.ts`, `src/lab/*.ts`. Không chụp, không chạy trình duyệt.
- Mọi tệp trong `src/view/skills` hiện **chỉ chạy trong lab chiêu** (`src/lab/skills-main.ts`); bản chơi chưa nhập chúng. "Camera chơi" là lab ở camera chơi, khoảng **38 px/m ở 1080p** (đo cũ 35–46 px/m). Cỡ trên màn trong bảng là ước tính từ số mét trong mã, chưa đo ảnh.
- Lab mặc định: hệ Metal (`DEFAULT_ELEMENT`), hào quang tắt (`auraIdOf` trả `off`). Hỏa chỉ chạy với `?element=fire`; hào quang với `?aura=a`.
- `vfx/` dưới đây là `games/immortality-cultivation/art-src/lab/vfx/`. "Ứng viên" là art có sẵn nhưng anh chưa duyệt hay chưa chấm; phải qua anh trước khi nối.

## 1. Bảng, sắp theo độ thấy (thấy nhiều nhất trước)

| # | Hình (tệp: hàm) | Phím, chiêu, pha | Độ thấy ở camera chơi | Mặc định | Art có sẵn thay được |
|---|---|---|---|---|---|
| 1 | Ấn dưới chân người phát chiêu: `fxkit.ts` `GroundSigil("seal")`, `SIGIL_FRAGMENT` với glyph `SEAL_SHAPE`; vẽ trong `sword-skills.ts` `update()` (khối `const seal = this.sigSeal`, khoảng dòng 2896). Hỏa chỉ đổi màu (`setSolid(FIRE.sigil)`) | Mọi phím 0–7; charge (suốt lúc gõ chữ) và chớp lúc release | 4 m ≈ 150 px (≈ 230 px ở tuyệt kỹ), hiện mỗi chữ đang gõ, tắt khoảng 0,3 s sau | Bật, cả Metal và Fire | Fire: ứng viên `vfx/fire/fire-halo-seal-loop` (ff-c3-c3, hai giám khảo 7 và 6,5), `vfx/fire/fire-halo-ring` (ff-c3-c2). A10 (ấn vẽ tay) chưa làm. Metal và 6 glyph: **cần art mới** (B1) |
| 2 | Sigil chiêu trên đất: `GroundSigil` kiểu `line` 14×1,8 m, `arcs` 4,8 m, `arrow` 5×0,9 m, `hex` 7,2 m, `spiral` 13,5 m, và nứt `crack` 7 m (`sigCrackS`, `startCrack`); dựng ở `sword-skills.ts` dòng 691–699 | Phím 2 (K2), 3 (Hộ thân), 4 (Lưu Quang), 5 (K4, có nứt), 6 (K5); charge tới release | 180–530 px, mỗi lần dùng chiêu, suốt charge cộng lúc tắt | Bật | Không có. **Cần art mới** (B2). Nứt: xem hàng 3 |
| 3 | Vết nứt và rãnh của mưa kiếm: `sword-rain.ts` `GroundMarks` (`MARK_FRAGMENT`: `MARK_STAR` sao nứt 1,7–7,5 m, `MARK_RIFT` rãnh 22 m); gọi ở `sword-skills.ts` `markAt()` và khối K5 (khoảng dòng 4548, 4566, 4632) | Phím 6 (K5 Thiên Hà Kiếm Vũ); impact và aftermath | Rãnh ≈ 840 px ngang nền; sao nứt 65–285 px, sống 1,3–3,2 s; mỗi lần tuyệt kỹ | Bật. Anh đã chê "vết nứt vẽ bằng code" | Ứng viên cần chấm: Dragonhold `games/dragon-hold/art-src/vfx/fissure-a.png`, `fissure-b.png`, `fissure-c.png` (mặt nạ xám vẽ tay, phong cách storybook); `art-src/skills/impact-tex/cracked-brush-burst-mask.png`; Last Line `games/typing-survival/art-src/arena-v2/deck-decals-crack.try1.png`. `vfx/marks/fire-r1/` đang rỗng. Rãnh 22 m: **cần art mới** (B3) |
| 4 | Cổng trời và cột sáng: `sword-rain.ts` `SkyGate` (`GATE_FRAGMENT`: elip giải tích, vành trắng nóng, vầng gai) và `LightStrips` (`STRIP_FRAGMENT`: cột trời–đất, đoạn sáng chạy) | Phím 6; release tới impact | Cổng rộng khoảng 44 % màn (≈ 850 px) trong khoảng 2,4 s (`RAIN_GATE_CLOSE_AT`); 4 cột cộng cột đáp | Bật | Không có. **Cần art mới** (B4, B5) |
| 5 | Vết cháy Hỏa: `ground-decals.ts` nhánh `PROCEDURAL` (blob uốn miền, nứt Voronoi `gdCells`), vì `element-fire.ts` đặt `SCORCH.texture = null`; gọi ở `burnGround()`, `release()` (đòn lớn), `plant()`, `finisher()` (13 vết dọc nhát chém kết), `leadStrike()` | Phím 1 (aftermath mỗi đòn), phím 7 (release, cắm kiếm, chém kết) | Mỗi vết 1,9–2,6 m (70–100 px), sống 5,2–5,6 s; nhát chém kết phủ khoảng 20 m | Chỉ `?element=fire`. Phiếu 264 tắt vết này ở đòn phím 1 bản nét cọ; phím 7 vẫn còn | Ứng viên cần chấm: Dragonhold `games/dragon-hold/art-src/vfx/scorch.png`; Last Line `arena-v2/deck-decals-scorch.try1.png`, `try2.png`. Kenney `scorch_01–03` đã bị loại ("vết mực"). Nếu dưới 8,5: **cần art mới** (B6) |
| 6 | Điểm lửa: `fire-points.ts` (`FRAGMENT`: sao lưỡi lửa chia theo góc); `element-fire.ts` `point()` | Hỏa: kiếm phím 1 hiện lúc charge, `release()`, `launch()`, `impact()`, `death()`; phím 7 mọi nhát kiếm sông (`strike()`, 14–20 nhát mỗi 100 ms), `plant()` | 0,4–1,9 m (15–70 px), 0,18–0,34 s; dày nhất ở phím 7 | Chỉ Fire. Phiếu 264 bỏ ở đòn phím 1 | Ứng viên: `vfx/fire/fire-twinkle-set` (ff-b3-c1), `vfx/aura/glint-starburst-set` (ff-g1-c1), `vfx/aura/tip-star-glint` (ff-g1-c2, 7/7); đòn lớn dùng `vfx/fire/impact-k1-r2` (anh đã duyệt) |
| 7 | Tàn lửa: `embers.ts` (`FRAGMENT`: đốm tròn có quầng, nhấp nháy bằng sin); `element-fire.ts` `emberBurst()`, `ringEmbers()`, `risingEmbers()`, `finisherSlash()` | Hỏa, mọi pha từ release tới aftermath, phím 1 và 7 | Từng đốm 3–13 px, tới khoảng 1.850 đốm cùng lúc ở phím 7, sống 0,7–2,4 s | Chỉ Fire | Ứng viên: `vfx/fire/fire-gold-dust` (ff-b3-c3, dải bụi lặp, không phải sprite rời). `vfx/fire/dragonhold-embers` bị chê "cục gai" khi to. Tấm bụi A9 chưa làm: **cần art mới** (A9 của kế hoạch tích hợp) |
| 8 | Tia và cột sáng Metal: `fxkit.ts` `BeamPool` (`BEAM_FRAGMENT`: dải gradient, lõi `pow(s,12)`, gợn sin); `sword-skills.ts` `rays()` (24 chỗ gọi), `pillar()`, `beamAt()` | Metal: mọi đòn trúng và mọi release (tia 1,1–3,2 m, 0,12–0,22 s); cột 2,2–4,8 m, 0,3–0,5 s ở góc K4, đòn lớn, release bậc cao | Tia 40–120 px, rất thường; cột 85–180 px cao | Bật (Metal) | Tia: ứng viên `vfx/fire/fire-spark-spray` (ff-b2-c2, tô màu theo hệ), Kenney `tex/trace_01–07`, `spark_01–07`. Cột: **cần art mới** (B5) |
| 9 | Vạch nóng chảy: `element-fire.ts` `finisher()` (dài l + 3 m, 3 s) và `cutSeam()` (thú lớn, 0,85 s), cả hai qua `BeamPool`; Metal: `myriad-swords.ts` vết cắt đất của nhát chém kết (khoảng dòng 1478–1510, vạch trắng và vết mực) | Phím 7, aftermath | Vạch khoảng 20 m ≈ 760 px, mảnh 6–11 px, sống 3 s | Bật (Metal); Fire với `?element=fire` | Fire: `vfx/aura/strips/strip-fire-ribbon-v2.rgba.png` hay `strip-fire-sheath.rgba.png` (anh đã chọn sheath, 19:40 ngày 04/11) cuộn dọc vạch. Metal: **cần art mới** (B7) |
| 10 | Vòng nhiệt: `heat-rings.ts` (`FRAGMENT`: vòng có lưỡi lửa giải tích, vạch nóng đứt đoạn); `element-fire.ts` `release()` (vòng áp lực ở tay) và `plant()` (vòng lửa trên đất) | Hỏa: mọi release phím 1 và 7; phím 7 cắm kiếm (tối đa 7 lần) | Ở tay 0,25 → 1,3 m (tới ≈ 150 px), 0,3 s; trên đất 1,4 m, 0,62 s | Chỉ Fire | Ứng viên: `vfx/fire/fire-halo-ring` (ff-c3-c2), `vfx/fire/fire-halo-seal-loop` (ff-c3-c3); hoặc A10 |
| 11 | Đốm tròn Hỏa: `element-fire.ts` `dot()`, `ember()`, `slashSpark()`, `glint()`, đốm hút vào tay ở `chargeKey()`/`chargeFrame()`; sprite Kenney `circle_05`. Dáng không do toán, nhưng là đốm tròn, thứ kế hoạch tích hợp cấm ("không đốm tròn") | Hỏa: điểm nạp ở tay suốt lúc gõ (0,16–0,38 m, HDR); 40 đốm mỗi giây mỗi kiếm đang bay; tia của nhát chém kết | 4–15 px, rất nhiều | Chỉ Fire | Ứng viên: `vfx/fire/fire-spark-spray`, `vfx/fire/fire-twinkle-set`, Kenney `spark_01–07`; tấm tia lửa A9 chưa làm |
| 12 | Vòng chân trong lab: `src/lab/presence.ts` P7, `GroundSigil("presence")` (ba cung chậm) | Mọi lúc, theo người phát chiêu | 1,6 m ≈ 60 px, tương phản thấp, luôn hiện | Bật (`ringOn = true`) | Ứng viên: `fire-halo-ring` tô màu theo chiêu. Không thì **cần art mới** (B8) |
| 13 | Áo khí và lưỡi lửa bọc lưỡi: `aura-mantle.ts` `CARD_FRAGMENT` (tấm khí chữ V, đường may, mây cuộn; Fire: lưỡi lửa liếm giải tích) và `HULL_FRAGMENT` | Hào quang kiếm: mọi kiếm dẫn và kiếm giữa, chờ và bay | Dọc mỗi lưỡi, 2–3 px mỗi bên, suốt chiêu | **Tắt** (cần `?aura=a`) | Anh đã chọn dải A7: `vfx/aura/strips/strip-metal-windsilk`, `strip-fire-sheath`; thêm ứng viên `vfx/aura/aura-*`. Mặt nạ A5, A6 chưa làm. Thuộc CX-D (số 260, chưa viết) |
| 14 | Sao mũi: `aura-mantle.ts` `STAR_FRAGMENT` (hàm `arm()`) | Hào quang: mũi kiếm dẫn, phím 1, kiếm giữa lúc lao | 12–32 px | **Tắt** | `vfx/aura/tip-star-glint` (ff-g1-c2, giám khảo 7/7), `glint-gold-twinkle-set`, `glint-starburst-set`. Thuộc CX-E (261, chưa viết) |
| 15 | Vạch hào của kiếm xa và đuôi lụa: `real-swords.ts` `FRAGMENT_HALO` (`MantleHalo`), `fxkit.ts` `MODED_RIBBON_FRAGMENT` (`SilkTail`: vạch bóng, nếp gấp bằng toán) | Hào quang, phím 7 | Mảnh, 1–3 px | **Tắt** | `vfx/aura/strips/strip-metal-windsilk-v2`, `vfx/aura/qi-streak-1..4`. Nên gộp vào CX-D |
| 16 | Sợi hồn lúc chết: `src/lab/death-fx.ts` `threads` (`BeamPool`) | Mọi con thú chết (lab) | Mảnh, 0,65–0,9 s | Bật | Kenney `trace_01–07`; hoặc tấm A9 |
| 17 | Vệt lưỡi: `src/lab/blade-smear.ts` | Release có key-pose, 1–2 khung | Hầu như không thấy | Bật | Giữ: đây là dáng chuyển động của chính lưỡi, không phải hình trang trí |

**Không tính** (dáng đã từ art, hoặc chỉ là màu hay nhịp):
- `qi-slash.ts`: dáng từ mặt nạ vẽ tay `slash-crescent-mask`.
- `flame-slash.ts`: phiếu 275.
- Các flipbook `fire-burst`, `fire-ground`, `fire-trail`, `fire-charge`, `fire-sparks`, `dragonhold-flame-trail`. Riêng `fire-sparks` ("tia nan bánh xe") phiếu 264 đã bỏ ở đòn phím 1.
- Sprite Kenney trong `sword-skills.ts` (`circle_05`, `star_07`, `star_09`, `circle_02`, `circle_03`, `dirt_03`).
- Khung va chạm toàn màn (mặt nạ `art-src/skills/impact-tex/*`).
- `element-metal.ts`: chỉ có màu, không có hình riêng.
- `sword-material.ts`: vạch mép và vòng ngọc là chất liệu trên model thật.
- `groundInk`: vệt tối mềm dưới chân, không có dáng.
- Nhiễu xói của `flipbook.ts`: chỉ là nhịp.
- `twin-pearl-greybox.ts`: hộp xám có chủ đích, sau cờ.

**Ngoài phạm vi, nên rà sau:** `src/view/telegraphs.ts` `markTexture()` vẽ hình tròn bằng canvas 2D, và chạy trong **bản chơi**.

## 2. Art mới cần làm (một dòng mỗi món)

Ảnh tĩnh do AI-vẽ (ChatGPT, rồi Gemini) hoặc Firefly Image; video do Firefly Video. Mọi bản nền đen đục. Anh xem mẫu trước khi nối.
- **B1. Ấn chân và glyph** (Firefly Image): "1024 square xianxia caster seal seen straight down on pure black: two hair-thin broken rings, engraved ticks and cloud hooks between them, empty centre; plus six 256 px glyph masks white on black: three strokes and a head, one long cut, three arcs, two points and a slash, a hexagon with six inward swords, three spiral arms round a dark heart". Bản Hỏa dùng A10.
- **B2. Sigil chiêu** (Firefly Image, 5 mặt nạ trắng trên đen, nhìn thẳng từ trên): một dải chém 4096×512; ba cung hộ thân; một mũi tên lao; lục giác trận; xoắn ba nhánh 2048. Nét chạm khắc mảnh, đứt đoạn, không có chữ.
- **B3. Nứt và rãnh** (Firefly Image): "top-down painted ground fissure masks on pure black: four star-shaped jagged crack clusters radiating from an impact, branching hairline ends; and one long glowing rift strip 4096×1024 with torn edges and side branches; no glow haze, no text".
- **B4. Cổng trời** (Firefly Video, 1:1 1080p, nền đen, 24 fps): "a celestial ring gate tears open in a night sky: white-hot rim, torn cyan corona, dark aperture; opens fast, holds, closes inward; fixed view, pure black, no swords, no text". Kiếm quanh vành vẫn là model thật.
- **B5. Cột sáng** (Firefly Video, 9:16, nền đen): "a thin vertical white-hot light column with a cyan body, bright segments racing down it, flaring at the foot; fixed view, pure black". Dùng cho `LightStrips` và `pillar()`.
- **B6. Vết cháy** (Firefly Image, chỉ khi ba ứng viên ở hàng 5 đều dưới 8,5): "top-down painted burn mark masks on pure black, four variants: crisp irregular lobed edge, charred ring inside the edge, network of ember cracks, never a star or a splat".
- **B7. Vạch nứt sáng Metal** (Firefly Image): "2048×128 strip on pure black: a hair-thin white-hot fissure with broken segments and tiny side cracks, tileable in x".
- **B8. Vòng chân** (Firefly Image): "512 square thin presence ring on pure black, three slow arc marks, soft dark backing, no text".

## 3. Lô phiếu Codex

**Luật chung cho mọi lô:**
- Model `gpt-6.1-sol`, mức `xhigh`. Một làn, worktree riêng. Mỗi tệp chỉ một người ghi mỗi lúc.
- Đường cũ giữ sau cờ lab để so A/B (ví dụ `?fxcode=1`). Không cờ thì lab chạy bản art.

**Kiểm chung:**
1. `tsc` và `vitest` đều qua. Không cấp phát mỗi khung. Mỗi pool một lệnh vẽ.
2. **Trùng khít ngoài hiệu ứng:** `lab-element-parity.mjs` (ONLY theo lô, ELEMENT `metal` và `fire`). Hiệu ảnh trước/sau ≈ 0 ngoài hộp bao của lớp được thay.
3. **Không lớp cũ nào vẽ ngầm:** `__lab.fxNamed()` cho thấy pool cũ có `count = 0` trên đường đã thay.
4. **Thời gian khung:** `lab-element-perf.mjs`. Fire hơn Metal tối đa 0,85 ms p95; mọi cửa sổ dưới 11,5 ms.
5. **Ảnh trước/sau:** khung trước và sau ở camera chơi, 1920×1080, DPR 1, cùng số khung. Lưu ở `typing-game-review/captures/tu-tien/code-drawn/<lô>/`, có `ABOUT.md`.
6. Claude gửi anh video. Hai giám khảo mù chấm. Mức nhận là 8,5.

**Lô 1. Lớp nhỏ của Hỏa bằng art có sẵn.**
- **Tệp:** `element-fire.ts`, `element-stage.ts`, `vfx/fire/manifest.json`. Chờ phiếu 264 gộp, vì 264 sửa `impact()` trong cùng tệp.
- **Điều kiện:** anh chọn `fire-halo-ring` hay `fire-halo-seal-loop`, và chọn mẫu sao (`fire-twinkle-set` hay `glint-starburst-set`).
- **Thay:**
  - `point()` thành thẻ một lần của `FlipbookPool` với tấm sao đã chọn (một hàng ngẫu nhiên, cỡ = 2 × `reach`). Nhát kiếm sông phím 7 giữ cỡ nhỏ.
  - Vòng ở tay trong `release()` thành `fire-halo-ring`: quay về camera, chạy một lần, giữ nhịp 0,3 s.
  - Vòng đất trong `plant()` thành `fire-halo-seal-loop`: nằm phẳng, 0,62 s, tắt bằng xói.
  - Vạch trong `finisher()` và `cutSeam()` thành dải `strip-fire-sheath` nằm phẳng, cuộn dọc vạch, cùng cách `sheathAt()` dùng `dir` và `span`.
  - Bỏ đăng ký `FirePointPool` và `HeatRingPool` khỏi đường Hỏa; giữ tệp cho cờ A/B.
- **Kiểm riêng:** khung đầu đạt ít nhất 95 % đỉnh ở tuổi 0; phím 7 vẫn dưới trần pool (256 điểm).

**Lô 2. Vết cháy và vết nứt từ tranh vẽ.**
- **Tệp:** `ground-decals.ts` (đường có texture đã có sẵn: A là độ phủ, R là chi tiết), `element-fire.ts` (hằng `SCORCH`, `SCORCH_LINE`), `sword-rain.ts` (`MARK_FRAGMENT` đọc atlas thay vì toán), `sword-skills.ts` (`sigCrackS` chuyển sang `GroundMarks`).
- **Điều kiện:**
  - Claude chấm năm ứng viên của hàng 3 và hàng 5 ở cỡ chơi. Nếu dưới 8,5 thì làm B3 và B6.
  - Mặt nạ đóng gói theo kênh: A độ phủ, R vết nứt than hồng, G thứ tự sống sót (xói), B vạch nóng.
- **Thay:**
  - Bỏ nhánh `PROCEDURAL` khỏi đường mặc định; vết cháy Hỏa đọc mặt nạ.
  - `MARK_STAR` đọc atlas 4 biến thể, xoay và đổi cỡ theo `markAt()`.
  - `MARK_RIFT` đọc dải rãnh, trải theo `RAIN_RIFT_M`.
  - Nhịp hiện, nguội và xói giữ như cũ.
- **Kiểm riêng:** trên đá sáng không thành "vết mực"; ΔE OKLab giữa vết và nền tối thiểu 0,25 (§2.8 kế hoạch tích hợp).

**Lô 3. Ấn chân và sigil chiêu vẽ tay.**
- **Tệp:** `fxkit.ts` (`GroundSigil` thêm chế độ `painted`), `sword-skills.ts` (`sigSeal`, `sigHex`, `sigSpiral`, `sigArcs`, `sigLine`, `sigArrow`), `src/lab/presence.ts`. Sửa `sword-skills.ts` thì chờ CX-J nếu CX-J đang chạy.
- **Điều kiện:** B1 (hoặc A10 cho Hỏa), B2, B8; anh chọn mẫu.
- **Thay:**
  - Chế độ `painted` đọc mặt nạ điều khiển RGBA: R dáng, G ink, B lõi nóng, A thứ tự hiện.
  - `uReveal` (theo phím gõ) so ngưỡng với A thay cho việc vẽ cung bằng toán.
  - Glyph theo chiêu đọc atlas B1; `uShape` thành chỉ số ô.
  - Màu, `uGlow`, `uInk`, `uFade` giữ.
- **Kiểm riêng:** ở 100 px vẫn tách được ít nhất 2 vòng; hiện dần theo chữ gõ, không nhảy; đổi glyph vẫn hòa trong 0,1–0,15 s như cũ.

**Lô 4. Tia lửa, bụi, đốm (mở rộng CX-F, số 262, chưa viết).**
- **Tệp:** mới `spark-sprites.ts` và `glint-pool.ts` (như CX-F); `embers.ts` (giữ vật lý trong vertex shader, chỉ đổi fragment từ đĩa tròn sang ô atlas A9); `element-fire.ts` (`dot()`, `ember()`, `slashSpark()`, `glint()`); `sword-skills.ts` `rays()`; `src/lab/death-fx.ts` `threads`.
- **Điều kiện:** tấm A9 (tia lửa và bụi) đã duyệt. `fire-spark-spray` dùng tạm cho `rays()` nếu anh chịu.
- **Thay:**
  - Đốm tròn thành ba họ tia (ngắn, cong, dài) và bụi vẽ tay, kéo dài theo vận tốc, kẹp cỡ theo px.
  - `rays()` của Metal thành tia sprite tô màu theo hệ.
- **Kiểm riêng:** không còn đốm tròn ở cỡ 12 px; hướng tia lệch ±10–25° quanh tiếp tuyến nhát chém; phím 7 vẫn dưới trần pool.

**Lô 5. Cổng trời và cột sáng phím 6.**
- **Tệp:** `sword-rain.ts` (`SkyGate`, `LightStrips`), `sword-skills.ts` `pillar()`.
- **Điều kiện:** B4 và B5 qua anh. Clip được cắt thành atlas bằng `tools/vfx-flipbook`.
- **Thay:**
  - `SkyGate` thành thẻ `FlipbookPool` quay về camera ở đúng chỗ `place()` tính ra. `swordAt()` và kiếm thật quanh vành giữ nguyên.
  - `LightStrips` và `pillar()` giữ hình học dải; fragment đọc dải B5 cuộn dọc cột.
- **Kiểm riêng:** `lab-k5-perf.mjs` không chậm hơn bản cũ quá 0,5 ms; khung đầu của cổng đạt ít nhất 95 %.

**Lô 6. Hào quang kiếm.** Không cần phiếu mới. Thêm `FRAGMENT_HALO` (`real-swords.ts`) và phần lụa của `MODED_RIBBON_FRAGMENT` (`fxkit.ts`) vào phạm vi CX-D (260). CX-E (261) giữ như kế hoạch tích hợp.

**Thứ tự đề xuất:**
- Lô 1: art có sẵn, chạy ngay sau khi 264 gộp.
- Lô 2: chờ chấm ứng viên.
- Lô 4: chờ A9. Riêng `rays()` có thể dùng `fire-spark-spray` trước.
- Lô 3 và Lô 5: chờ art mới.
