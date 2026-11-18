# Spike bố cục Rồng L2-cau (28/10/2026)

**Đọc cho ai:** điều phối viên Map Factory, người viết phiếu 030–033, làn Rồng ở giai đoạn 3.

**Nguồn:** [MAP_FACTORY.md](../MAP_FACTORY.md) §1.1, §6.2, §6.6 mục 1, §8, §12. Ảnh mẫu `tmp/map-studio/owner-reference-haven-grove.webp` (nửa trên, "BEFORE"). Ảnh M0b `tmp/map-studio/now-rong-giu-ai-m0b.png`.

**Ở đâu:** worktree `games/.wt-dh-mapspike`, nhánh `map-spike` (tách từ `m0b-models`, **không bao giờ gộp**). Mã chỉ trong `src/view/` và hai kịch bản `scripts/visual/scenarios/dh-mapspike*.mjs`. Sim, nội dung, golden không đổi.

**Trạng thái:** xong. 6.6 mục 1 đạt sát ngưỡng (trung vị 7,25; thấp nhất 6,5; nheo mắt vẫn đọc rõ làn). Chưa có người chấm thứ hai (xem mục 8).

## Tóm tắt

- **Điểm:** trung vị **7,25/10**, thấp nhất **6,5** (p75-y180), cạnh ảnh mẫu. M0b cùng góc khoảng 5 (chấm nhanh trên tấm ảnh baseline). Đạt 6.6 mục 1: trung vị ≥ 7, không ảnh nào dưới 6, nheo mắt vẫn đọc rõ hai làn, sông, bệ, ao.
- **Nguyên nhân giới hạn:** 9/12 ảnh do **kit**: không có đèn, rào, cọc dọc lối mòn; không có cây sắc ấm (đỏ, cam); không có đá vách; không có cụm cỏ hoa 3D. 3/12 ảnh do **bố cục** (rừng phía tây quá đặc, vách lộ thành dải sọc ở mép ảnh). Không ảnh nào bị giới hạn bởi luật chơi.
- **Luật dừng (§12):** trung vị ≥ 7 nên không cần thêm vòng chỉnh. Muốn lên ≥ 8 ở giai đoạn 3 thì phải có kit: danh sách món thiếu ở mục 7 (thành một lô ảnh Codex, rồi chủ dự án dựng Tripo).
- **Hiệu năng (`dh-bench`, 220 quái có xương, High, 1080p):** bản đồ spike 7,23 ms, p95 8,6 ms, 69 draw call; so với đất trống cùng sân khấu: chênh trung bình **+2,62 ms**, chênh p95 **+2,9 ms**, **+30 draw call**, **+0,73 M tam giác** (mọi lượt vẽ), tam giác prop **452 k** (trần 550 k). Tổng trong trần của Rồng. Chênh trung bình vượt cổng bản đồ 2 ms khoảng 0,6 ms; cách sửa đã biết: nướng lớp sơn đất vào render target lúc nạp (§3.2). Trận thật đợt 1–2: p95 6,9–7,0 ms. `dh-crowd` 1080p: `ok`.
- **Phần sinh lúc nạp:** luật bố cục 4 ms, mặt nạ sơn 76 ms, kế hoạch rải 13 ms (Node, M4): dưới cổng 300 ms.
- **Codex 030–033 đi tiếp được.** Mục 6 là danh sách luật kèm tham số để viết thuật toán chính xác.

---

## 1. Đã làm gì

Mỗi luật là một khối riêng, có tham số, theo thứ tự lớp của Map Factory. Tất cả ở `src/view/layout.ts` (`LAYOUT_RULES`), trừ sơn đất (`paint.ts`), vòng xa (`impostor.ts`, `scatter.ts`) và nước ao (`water.ts`).

| Lớp | Luật | File |
|---|---|---|
| L1 | Trường khoảng cách: làn (kèm vệt sau cổng), làn trời, sông, ô, bệ, lối mòn, ao | `layout.ts` `LayoutFields` |
| L2 | Một dấu vách ở vòng ngoài tây bắc, mặt bậc thang, đá lớn ở chân, mặt và mép vách | `layout.ts` `buildCliff`, `terrain.ts` |
| L3 | Một ao trang trí tự chọn chỗ trống nhất; đáy lòng chảo, lá súng, viền bọt, đá viền | `layout.ts` `sitePond`, `water.ts` |
| L4 | 5 lối mòn cong (Bézier bậc hai), sửa khoảng cách, thu hẹp ở bệ; không dẫn tới ô | `layout.ts` `routeFootpaths` |
| L6 | Lùm cây theo tâm cụm, đổi sắc từng lùm và từng cây; cây lẻ; bụi viền; gỗ mục; hàng đá dọc sông, mép làn, ao, vách | `layout.ts` |
| L6 | Rừng mép: rải đều cũ chỉ từ mép rừng ra; tán tím 18 % thay vì 40 % | `scatter.ts` |
| Vòng xa | Thay cầu và nón tạm bằng model pine-river: gần (bóng), giữa (không bóng), xa (impostor, một atlas, một draw call) | `scatter.ts`, `impostor.ts` |
| L7 | Mặt nạ RGBA (đất, lối mòn, hoa, bóng tán) nướng lúc nạp; 8 ô đất làm nét cọ; 4 tờ decal rải kiểu texture bombing | `paint.ts` |

Commit trên `map-spike`: `f491432` (bản dở của lượt trước, đã kiểm và giữ), `972e3ae`, `d558832`, `f7f1576`. Không commit media. `git diff 3f3390d..f7f1576` không chạm `src/sim`, `src/content`, `src/ui`, `tests`; `tsc --noEmit` đạt; vitest 425 test đạt (một test thời gian `tags-bodies` trượt một lần khi máy đang chạy bench, chạy riêng thì đạt).

Script phụ (không commit, trong `tmp/` của worktree): `stats.ts` (số đếm, khoảng cách tới ô, làn), `bands.ts` (tam giác prop theo dải), `timing.ts` (thời gian sinh), `plan.ts` (sơ đồ SVG). Chạy bằng `npx tsx tmp/<file>.ts`.

Chạy lại:

```bash
cd games/.wt-dh-mapspike
npx vite --host 127.0.0.1 --port 4156 --strictPort &
URL=http://127.0.0.1:4156/ TAG=final2 .local/bin/heavy.sh --gpu node scripts/visual/cdp-run.mjs \
  scripts/visual/scenarios/dh-mapspike.mjs --width=1920 --height=1080
# bench: bản đồ spike / đất trống (decor=0&paint=m0b)
EXTRA="decor=0&paint=m0b" CHROME_FLAGS="--disable-gpu-vsync --disable-frame-rate-limit" URL=http://127.0.0.1:4156/ \
  Q=high MODE=bones GROUND=painted .local/bin/heavy.sh --perf node scripts/visual/cdp-run.mjs \
  scripts/visual/scenarios/dh-mapspike-bench.mjs --width=1920 --height=1080
```

Công tắc chỉ cho spike, đọc từ URL của trang: `decor=0` (không cây, bụi, đá), `paint=m0b` (sơn đất thủ tục của M0b), `decals=0`, `tiles=0`, `props=0` (trang `?view=terrain` không nạp model).

## 2. Ảnh

Thư mục (bị `.gitignore`, không vào Git): `games/.wt-dh-mapspike/tmp/shots/mapspike/`.

| Gì | Đường dẫn |
|---|---|
| 12 ảnh chấm điểm + mặc định 1920×1080 + mặc định 1280×720 | `final2/` |
| Phép nheo mắt (thu 1/8, làm mờ 1,2 px, phóng lại) | `final2/squint/`, tấm ghép `final2-squint-sheet.jpg`; ảnh mẫu nheo mắt `final2/squint/reference-before-squint.png` |
| Tấm ghép 12 ảnh | `final2-sheet.jpg`; theo từng góc nghiêng `final2/quad-p40.jpg`, `quad-p55.jpg`, `quad-p75.jpg`, `quad-default.jpg` |
| M0b trước spike | `baseline/`, `baseline-sheet.jpg`; so cạnh nhau `m0b-vs-spike-p55-y0.jpg` |
| Các vòng chỉnh | `r1`–`r6`, `final` (trước khi dời dải xa về 42 m), `gate` (kiểm hình sau khi tối ưu sơn đất: giống `final`) |
| Bench | `bench/`, log `bench-*.log` |

## 3. Điểm

Chấm từng ảnh cạnh nửa "BEFORE" của ảnh mẫu (ảnh mẫu là 10). Đã xem đủ 12 ảnh và 2 ảnh mặc định ở cỡ đầy đủ (`final`), rồi xem lại cả 12 ảnh `final2` (chỉ khác ngoài 42 m) trên các tấm ghép 2 × 2.

| Nghiêng \ Hướng | 0° | 90° | 180° | 270° |
|---|---|---|---|---|
| **40°** | **7,5** kit | **7,5** kit | **7,0** bố cục + kit | **7,5** kit |
| **55°** | **7,5** kit | **7,5** kit | **7,0** bố cục + kit | **7,5** kit |
| **75°** | **7,0** kit | **7,0** kit | **6,5** bố cục + kit | **7,0** kit |

Mặc định của game (yaw 0°, 55°, nhìn 4 m bắc bệ): 1920×1080 **7,5**; 1280×720 **7,0** (lộ nhiều vòng xa và vách hơn).

- **Trung vị 7,25; thấp nhất 6,5; trung bình 7,2.**
- **Kit (9 ảnh):** dọc lối mòn trống trơn, ảnh mẫu có đèn cách đều làm nhịp; điểm nhấn màu chỉ có tán tím (bị luật làn giới hạn), ảnh mẫu có tán đỏ, cam; vách là sườn dốc sơn đá có các tảng đá phủ rêu, ảnh mẫu là khối đá xám chồng nhau; bãi cỏ chỉ có hoa decal phẳng.
- **Bố cục (hướng 180°):** rừng phía tây thành một bức tường tối dày; vách tây bắc lộ ở mép phải thành dải sọc. Sửa được bằng luật (mục 8), không cần thêm món.
- **Góc 75°:** nhìn thẳng xuống làm tán cây thành đốm tròn; mất phần lớn cái đẹp 3D. Đây cũng là giới hạn của kit (thân, bóng), không do bố cục.
- **Nheo mắt:** hai làn đất (rộng 2,6–3 m) đọc rõ tới bệ; lối mòn (1,05 m, phủ 78 %, có cỏ giữa, thu hẹp ở bệ) đọc thành nét phụ mảnh hơn. Sông, bệ, ao, cầu đọc rõ. Tán tím thành chấm, chỉ ở mép rừng. So với ảnh mẫu nheo mắt: ảnh mẫu thoáng hơn (khoảng 60 % là bãi cỏ sáng, ta khoảng 40 %), vì vòng rừng của Rồng đóng khung sân 32 m.

## 4. So với các phần làm ảnh mẫu đẹp (§1.1)

| Phần của ảnh mẫu | M0b | Spike | Còn thiếu |
|---|---|---|---|
| Đất mòn dưới gốc cây, quanh ngã ba; mép đường mềm | Không | Có: đĩa đất dưới mọi cây lùm, cây lẻ; vệt mòn hai bên làn; sân đất quanh bệ; viền cỏ sáng quanh mọi chỗ đất | Đĩa đất hơi tròn đều; có thể thêm nhiễu biên |
| Lối mòn rẽ nhiều ngả | Không | Có: 5 lối, ao là đầu mối 3 lối, một lối rừng ở tây bắc | Đèn, rào, cọc (kit) |
| Cây thành lùm, nhiều sắc | Rải đều, đốm | Có: 10 lùm, 5 sắc, cây lẻ, bụi viền | Sắc ấm đỏ, cam (kit) |
| Ao có lá súng, cầu nhỏ | Không | Ao 4,6 m, lá súng, viền bọt, đá viền, bụi bờ | Bến gỗ, lau sậy (kit) |
| Vách đá đóng khung | Không | Dấu vách 9 m, bậc thang, đá lớn ở chân, mặt, mép | Đá vách thật (kit); vách quay lưng về mặt trời |
| Đèn, rào, cọc dọc đường | Không | Không | Toàn bộ là kit |
| Bãi trống có hoa cỏ nhỏ | Phẳng | Hoa decal theo mảng và quanh mép đất | Cụm cỏ hoa 3D rẻ (kit) |
| Vòng xa | Cầu, nón tạm | Model pine-river, impostor từ 42 m | — |

---

## 5. Hiệu năng

**Cách đo:** `dh-bench` MODE=bones, 220 quái có xương, đủ hiệu ứng, High, 1920×1080, Chrome không khóa nhịp, máy M4 dùng chung với các làn khác (số dao động ±0,3 ms giữa các lượt). "Đất trống" là cùng sân khấu sơn của game (đất, sông, bệ, cầu, bóng, hậu kỳ) với `decor=0&paint=m0b`: không cây, bụi, đá, sơn đất của M0b. Đất phẳng của bench (`GROUND=flat`, 3,19 ms) không có bóng và hậu kỳ nên không dùng làm mốc.

**Số cuối** (mã ở `f7f1576`):

| Lượt | Trung bình | p95 | Draw call | Tam giác (mọi lượt vẽ) | Tam giác prop (một lượt) |
|---|---|---|---|---|---|
| Đất trống (`decor=0&paint=m0b`) | 4,61 ms | 5,7 ms | 39 | 1,81 M | 0 |
| Bản đồ spike | 7,23 ms | 8,6 ms | 69 | 2,53 M | 452 k |
| **Chênh** | **+2,62 ms** | **+2,9 ms** | **+30** | **+0,73 M** | **+452 k** |

**Tách chi phí** (cùng mã trước khi tối ưu sơn đất, lượt 1–2):

| Biến thể | Trung bình | p95 |
|---|---|---|
| Spike, sơn đất mỗi khung tính đủ 11 mẫu ô đất + 4 lớp decal | 8,55 | 10,0 |
| Tắt decal | 7,86 | 9,7 |
| Tắt decal và ô đất | 7,07 | 8,7 |
| Sơn đất M0b, giữ bố cục và prop spike | 6,42 | 8,2 |
| Sau tối ưu (mỗi ô đất, mỗi lớp decal chỉ lấy mẫu nơi nó hiện được) | 7,10–7,59 | 8,5–9,4 |
| Đất trống (không decor, sơn M0b) | 4,84–5,12 | 6,3–6,8 |

**Đọc số:**
- Sơn đất là phần đắt nhất: vẽ thủ tục mỗi khung trên toàn màn hình. Tối ưu nhánh đã bớt khoảng 1,4 ms; vẫn còn khoảng 0,7–1 ms so với sơn M0b. Cách sửa đúng là **nướng lớp sơn (mặt nạ, ô đất, decal) vào một render target lúc nạp** (§3.2: 2048² cho hình vuông 104 m là 5 cm một texel), shader đất chỉ còn đọc một texture trong hình vuông sơn. Việc này thuộc giai đoạn 3.
- Prop: dải xa từ 46 m xuống 42 m và bỏ đá rải ngoài 42 m đưa tam giác prop từ 677 k xuống 452 k (trần High 0,55 M: đạt). Cây xa là impostor: một draw call, 2 tam giác một cây.
- Draw call: +30 so với đất trống (trần bản đồ High 40 theo công thức §4.2).
- Ba cặp đo (spike / đất trống, cùng phiên) cho chênh trung bình 2,47–2,62 ms, chênh p95 2,6–2,9 ms. **Cổng bản đồ §4.2:** chênh p95 ≤ 3 ms đạt (sát); chênh trung bình ≤ 2 ms **chưa đạt** (+0,6 ms); draw call của bản đồ +30 ≤ 40 đạt; tam giác prop 452 k ≤ 550 k đạt. Tổng của trận vẫn trong trần Rồng: 7,23 ≤ 8 ms, 8,6 ≤ 12 ms, 69 ≤ 150 draw call.
- **Trận thật** (`dh-perf`, bot gõ, tốc độ 2, 1920×1080, không khóa nhịp): đợt 1 trung bình 5,90 ms, p95 6,9 ms, tối đa 17,3 ms, 52 draw call, 1,00 M tam giác; đợt 2: 5,91 ms, 7,0 ms, 12,0 ms, 50 draw call. M0b ngày 27/10 đo p95 5,6–6,2 ms ở đợt 1–5, nên bản đồ spike thêm khoảng 0,8–1 ms p95 trong trận thật; vẫn xa trần 12 ms. Log `wave-1920.log`.

**Phần sinh lúc nạp** (Node 24, M4, trung vị 5 lần): luật bố cục 4 ms; trường cao độ cả bố cục 162 ms (đã có từ M0b, spike thêm ao và vách); nướng mặt nạ sơn 76 ms (JS số thực, 416² điểm); kế hoạch rải 13 ms. Phần spike thêm khoảng 95 ms, dưới cổng 300 ms. Atlas impostor nướng trên GPU lúc nạp model (7 ô 256 px), không đo riêng.

**Chữ trên quái (`dh-crowd`, 1920×1080, seed 5):** `ok` cả năm phần. 17.917 khung đo từ đợt 3; quái xa: 0 khung có thân bị che ≥ 40 % (che lớn nhất 31 %); quái trong 10 m: lớn nhất 25 %; cảnh báo đỏ: lớn nhất 30 %; không tag nào nhảy rồi bật lại; Thiên Hỏa chạy. Ảnh `crowd/`, log `crowd-1920.log`. Đã xem ảnh: chữ đọc rõ trên nền cỏ, đất và nước của bản đồ mới.

---

## 6. Danh sách luật

Quy ước:
- Mét, độ; hướng (bearing) 0° = bắc (−z), 90° = đông (+x). Lõi đổi sang cm nguyên và tra bảng hướng, không gọi sin, cos (§8.5).
- `h(luật, a, b)` là băm trong [0, 1), một luồng cho mỗi luật. Spike dùng `hash2` số thực của `terrain.ts` với seed bố cục `terrain.seed XOR 0x6d61`; lõi dùng `cellSeed(layerSeed, …)` của phiếu 027.
- `lerp(a, b, t)`, `smooth(e0, e1, x)` là smoothstep.
- Trường (L1): `laneGap` = khoảng cách tới tim làn gần nhất trừ nửa bề rộng, tính cả vệt sau cổng (đoạn đầu kéo dài 16 m ra ngoài, nửa bề rộng × 0,8); `skyDist` = khoảng cách tới đường làn trời; `riverEdge` = khoảng cách tới tim sông (Catmull-Rom mỗi 1,5 m, kéo dài 150 m hai đầu) trừ nửa bề rộng nội suy; `slotDist` = khoảng cách tới ô gần nhất (mọi loại ô); `r` = khoảng cách tới tâm bệ; `pathGap` = khoảng cách tới tim lối mòn trừ nửa bề rộng tại đó; `pondEdge` = khoảng cách có dấu tới bờ ao (âm trong nước).
- Thứ tự (mỗi luật chỉ đọc kết quả của luật trước): L3 ao → L2 vách → L4 lối mòn → L6 lùm → cây trong lùm, bụi viền, gỗ mục → cây lẻ → đá sông → đá mép làn → đá viền ao, bụi bờ ao → đá chân vách, mặt vách, mép vách → L7 đĩa đất → mặt nạ → rừng mép.
- Ứng viên rải dùng chung một cách: lưới ô `cell`, mỗi ô một điểm lệch ±0,4 ô theo băm, hạng = `h(luật, i, 3j)`; duyệt theo hạng tăng dần, hòa thì so id ô. Tăng số lượng chỉ thêm vật, không dời vật cũ (§3.1 nguyên tắc 4).

### 6.1 L3 Ao

| Tham số | Giá trị |
|---|---|
| Bán kính danh nghĩa R | 4,6 m |
| Vành tâm ao tính từ bệ | 14–23 m |
| Lưới tìm chỗ | 1 m, trong hình vuông ±23 m quanh bệ |
| Điểm của một chỗ | `min(laneGap − R − 7, slotDist − R − 7, skyDist − R − 6, riverEdge − R − 9)`; bỏ nếu < 0; lấy chỗ điểm cao nhất (hòa: + h × 0,001) |
| Bờ | 8 bán kính điều khiển ở hướng k × 45°: R × (1 + 0,24 × (2h − 1)); Catmull-Rom khép kín mỗi 0,5 m |
| Mực nước | cao độ đất khô ở tâm − 0,3 m |
| Bờ và đáy | trong 3,5 m quanh bờ san về mực nước + 0,8 × bờ sông (0,4 m); đáy sâu 0,2 + 0,85 × smooth(0, 0,75R, −pondEdge) |
| Mặt nước | lá súng: lưới 1,4 m, 40 % ô có lá, bán kính 0,24–0,44 m, khuyết một múi, chỉ chỗ sâu > 12–30 %; 35 % lá có hoa; viền bọt ở bờ |
| Đá viền | 10 viên, viên k ở cung (k + 0,6h)/10 của chu vi, đẩy ra ngoài 0,15–0,65 m theo bán kính; bỏ nếu `pathGap` < 0,6 (chừa chỗ lối mòn chạm nước); cứ 3 viên một phiến đá (slab), còn lại sỏi sông; cỡ 0,6–1,35 |
| Bụi bờ | 3 bụi ở 1/6, 3/6, 5/6 chu vi, cách bờ 1,5 m; bụi giữa có hoa |

L2-cau: ao ở (0; 23), cách mép ô gần nhất 12,6 m, mép làn 17,5 m.

### 6.2 L2 Dấu vách

| Tham số | Giá trị |
|---|---|
| Đường vách (spec, vẽ tay) | (−19; −40), (−28; −33), (−35,5; −22), (−39; −10), (−40; 0); Catmull-Rom mỗi 1 m. Nằm ở vòng ngoài tây – tây bắc, r 40–46 m |
| Độ lệch s | khoảng cách có dấu tới đường (+ là phía xa bệ) trừ mép răng cưa (nhiễu(dọc/6 m) − 0,5) × 2 × 1,3 m |
| Cao độ cộng thêm | 9 m × [0,72 × smooth(−0,8; 0,5; s) + 0,28 × smooth(1,1; 2,3; s)] × (1 − smooth(14; 30; s)) × đầu, với đầu = smooth(0; 7; dọc) × smooth(L; L − 7; dọc) |
| Sơn | đá nơi độ dốc (1 − n.y) qua 0,26–0,42 (± nhiễu 0,09); màu đá ấm (0,78; 0,66; 0,54) × ô đá triplanar 4,5 m; vạch tầng mỗi 1,8 m chiều cao (tối 50 %), mặt trên mỗi tầng sáng hơn |
| Đá chân vách | mỗi 2 m dọc đường, 80 %, đẩy về phía bệ 1,2–3 m, cỡ 1,0–2,6; tảng tròn (boulder) 55 %, còn lại phiến; bỏ nếu `laneGap` < 3 hoặc `riverEdge` < 0,5 |
| Đá mặt vách | mỗi 2,4 m (± 0,72 m), 85 %, đặt đúng tại s ∈ [−0,2; 1,0], cỡ 2,6–4,4 × độ mờ đầu (bỏ nếu < 1); tảng tròn 65 % |
| Đá mép vách | mỗi 3,1 m, 70 %, s ∈ [2,4; 3,6], cỡ 1,8–3,0; phiến 65 % |
| Đất vụn chân vách | mỗi 2,6 m, đĩa đất r 1,6–3,0 m, cách 1,5–3 m về phía bệ, rìa 1,4, độ mạnh 0,75 |
| Rừng | không cây rải đều trên mặt vách: s ∈ (−2,5; 6) nơi đầu > 0,2 |

**Bài học về ánh sáng:** mặt trời của Rồng ở tây nam (`SUN_DIRECTION` (−0,55; 1,05; 0,62)). Vách ở tây bắc quay mặt về bệ, tức về đông nam, nên nằm trong bóng và bị ánh trời tím nhuộm. Luật cho lõi: chọn đoạn vòng ngoài mà pháp tuyến mặt vách (hướng về bệ) · hướng nắng (xz) ≥ 0,3, tức phía bắc, đông bắc, đông với ánh sáng này; nếu bố cục buộc vách vào bóng thì dùng màu đá ấm như trên.

### 6.3 L4 Lối mòn

| Tham số | Giá trị |
|---|---|
| Bề rộng | 1,05 m × nhiễu 0,92–1,08 (sóng 4 m) |
| Đầu ở bệ (`plaza`) | bắt đầu 0,4 bề rộng, đủ bề rộng sau 5 m, để lối không đọc như một nan làn |
| Đầu ở mép rừng (`edge`) | thu về 0,6 bề rộng trong 8 m cuối |
| Neo | `plaza`: tâm bệ + hướng × (bán kính bệ + 2,4 m), hướng về ao nếu `dais: "pond"`; `edge(b)`: r = bán kính sân + 6 m ở hướng b; `pond(b)`: đi từ tâm ao theo hướng b mỗi 0,25 m tới khi `pondEdge` ≥ 0,5; `pond(true)`: hướng về đầu kia; `river(b)`: đi từ r = 10 m theo hướng b mỗi 0,25 m tới khi `riverEdge` < 1; `path(id, t)`: điểm ở t × chiều dài của một lối đã có |
| Đường | dây cung a → b dài L; Bézier bậc hai với điểm điều khiển = trung điểm + n × uốn × L (n là pháp tuyến trái của a → b); lấy mẫu mỗi 3 m; lượn thêm (nhiễu(s/14 m) − 0,5) × 2 × 2,2 m theo n, giảm dần trong 6 m đầu và cuối |
| Sửa khoảng cách | 10 vòng: mỗi điểm trong có thiếu hụt d = min(`slotDist` − 4,6; `laneGap` − 2,2; `riverEdge` − 1,6 trừ khi một đầu là sông; `pondEdge` − 1,6 trừ khi một đầu là ao) < 0 thì dời theo −∇d một đoạn 1,1 × \|d\| (gradient sai phân trung tâm 0,25 m); sau mỗi vòng làm trơn: 0,5 × điểm + 0,25 × mỗi điểm kề. Rồi Catmull-Rom mỗi 0,5 m |
| Không dẫn tới ô | bỏ cả lối nếu một đầu tự do (`edge`, `pond`, `river`) cách ô < 7 m |
| Ngã ba | mỗi đầu lối trong sân có một đĩa đất r 1,9 m, rìa 1,2, độ mạnh 0,75 |
| Sơn | kênh G: 1 − d / (2 × nửa bề rộng); phủ = smooth(0,47; 0,55; G + nhiễu) × 0,78 trên đất phẳng; dải cỏ giữa nơi G qua 0,66–0,9 (nhiễu); màu đất nhạt pha 22 % cỏ sáng |

Các lối của L2-cau (đo trên bố cục cuối):

| id | Từ | Tới | Uốn | Dài | Mép lối – ô gần nhất | Mép lối – mép làn | Đầu tự do – ô |
|---|---|---|---|---|---|---|---|
| fp-pond | bệ, hướng ao | ao | 0,10 | 11,1 m | 4,79 m (đầu ở bệ) | 6,98 m | 12,1 m |
| fp-west | fp-pond tại 0,45 | sông, hướng 236° | −0,14 | 34,8 m | 6,03 m | 10,65 m | 19,3 m |
| fp-south | ao, hướng 218° | mép rừng 196° | 0,16 | 12,7 m | 19,6 m | 24,5 m | 20,2 m |
| fp-east | ao, hướng 84° | mép rừng 116° | −0,18 | 29,4 m | 14,2 m | 23,2 m | 16,4 m |
| fp-north | mép rừng 324° | mép rừng 283° | 0,30 | 27,4 m | 17,6 m | 15,5 m | 17,9 m |

Phép kiểm cho phiếu 032 (`checks/decor.ts`): mép lối cách mọi ô ≥ 4,4 m; đầu tự do cách mọi ô ≥ 7 m; mép lối cách mép làn ≥ 2,2 m; lối không chạm làn và không cắt làn trời trong 10 m. Đề xuất thêm (chưa làm trong spike): trong 14 m quanh một làn, hướng lối lệch hướng làn ≥ 25° (fp-west chạy gần song song làn Suối, cách 10,65 m).

### 6.4 L6 Lùm cây

| Tham số | Giá trị |
|---|---|
| Ứng viên | lưới 6 m trong hình vuông ±30 m (11 × 11), duyệt theo hạng; tối đa 12 lùm |
| Vành tâm lùm | r 11–30 m |
| Bán kính | min(muốn, `laneGap` − 3,4, `slotDist` − 4,8, `skyDist` − 3, `riverEdge` + 0,4, `pathGap` + 2,2, `pondEdge` − 3, r − 9, bán kính sân + 3,5 − r), muốn = lerp(3,8; 7,5; h); bỏ nếu < 2,6 m. Đĩa lùm được vươn tới 0,4 m qua mép sông và 2,2 m qua lối mòn; từng cây vẫn giữ khoảng cách riêng |
| Cách nhau | hai đĩa lùm cách nhau ≥ 3,5 m (mép – mép) |
| Lùm tím | khi min(`laneGap`, `skyDist`) − bán kính ≥ 9 m (05 §2.2) |
| Số cây | max(3; round(π R² × 0,11)), tức 0,11 cây/m² |
| Đặt cây | ném phi tiêu: (u, v) ∈ [−1; 1]² theo băm, bỏ ngoài đĩa đơn vị, vị trí = tâm + (u, v) × R; tối đa 25 × số cây lần thử; gốc cách nhau ≥ 2,1 m |
| Khoảng cách của một cây | `laneGap` ≥ 3,3; `riverEdge` ≥ 0,95; `slotDist` ≥ 3,5; `skyDist` ≥ 2,7; r ≥ 10,2; `pathGap` ≥ 1,1; `pondEdge` ≥ 1,2 |
| Loài theo ρ = \|(u, v)\| | lùm tím, ρ < 0,6, cuộn < 0,35: cây tím, cao 5,2 + 3 × cuộn; ρ < 0,55: tán tròn (4,6 + 2,2 × cuộn) hoặc thông cao (5,6 + 2,2 × cuộn), mỗi loại 50 %; ngoài: thông non 50 % (2,6 + 1,6 × cuộn), thông cao 28 %, tán tròn 22 % (4,2 + 1,6 × cuộn), trần × 0,85 |
| Trần chiều cao | min(8; 3,6 + 0,26 × (r − 10)) m: gần bệ cây thấp, nên bệ và làn không bị che |
| Sắc | mỗi lùm một trong 5 sắc nhân vào texture: gốc (1; 1; 1), nắng (1,05; 1,06; 0,9), mát (0,86; 0,97; 1,08), trầm (0,84; 0,89; 0,88), tươi (0,97; 1,09; 0,93); mỗi cây × 0,94–1,06. Không bao giờ vàng (màu của Héo) |
| Bán kính tán trên đất | chiều cao × 0,55 (tán tròn), 0,5 (tím), 0,28 (thông) |
| Bụi viền | round(2πR × 0,22) bụi, mỗi bụi ở bán kính R + 0,4 + 1,3h theo một hướng băm; khoảng cách của bụi: `laneGap` ≥ 1,3; `riverEdge` ≥ 0,6; `slotDist` ≥ 2,8; r ≥ 8; `pathGap` ≥ 0,5; `pondEdge` ≥ 0,6; bụi hoa 40 %, bụi rêu 60 %; cỡ 1,5–2,5 |
| Gỗ mục | 60 % số lùm có một khúc gỗ (50 %) hoặc gốc cây ở (u, v) × 0,7R, cách gốc cây ≥ 1,2 m |

L2-cau: 10 lùm (5 tím), bán kính 2,6–6,1 m, 58 cây; mép đĩa lùm cách ô ≥ 4,8 m; cây tím cách mép làn ≥ 13,0 m, cách làn trời ≥ 15,6 m.

**Luật ô ẩn:** đĩa lùm lùi khỏi ô hơn chính bán kính của nó cộng 4,8 m, cây lẻ 5,2 m, nên không lùm nào bao quanh một ô và không có khoảng trống hình ô. Mọi cây cách ô ≥ 3,5 m như luật rải cũ.

### 6.5 L6 Cây lẻ

| Tham số | Giá trị |
|---|---|
| Ứng viên | lưới 5 m trong ±29 m, theo hạng; tối đa 8 |
| Điều kiện | r 12–29 m; `laneGap` ≥ 4,2; `slotDist` ≥ 5,2; `skyDist` ≥ 4; `riverEdge` ≥ 2; `pathGap` ≥ 2,4; `pondEdge` ≥ 3; ngoài mọi đĩa lùm ≥ 2,5 m; cách cây lẻ khác ≥ 7 m |
| Loài | tán tròn 55 % (5 + 2 × cuộn), thông cao (5,8 + 2 × cuộn), theo trần ở 6.4 |
| Đất | đĩa đất r 2,1 m |

L2-cau: 5 cây lẻ (phần còn lại của sân bị lùm, lối, ao, ô chiếm).

### 6.6 L6 Hàng đá

| Hàng | Bước | Bắt đầu một dãy | Dài dãy | Vị trí | Cỡ, loại | Bỏ khi |
|---|---|---|---|---|---|---|
| Bờ sông (hai bờ) | 1,5 m dọc tim sông | 42 % mỗi đoạn 6 m | 3–7 viên | mép nước + 0,1–0,9 m; chỉ trong r ≤ bán kính sân + 6 m | 0,5–1,1; sỏi sông 55 %, phiến 30 %, tảng (× 0,8) 15 % | `laneGap` < 2,6 (cắt dãy); `pathGap` < 0,3 |
| Mép làn (hai bên) | 2 m | 34 % mỗi đoạn 7 m | 2–5 viên | nửa bề rộng + 0,7–1,3 m | 0,35–0,6 (nhỏ, không đọc thành vật chặn); sỏi 70 %, phiến | trong 2,5 m quanh cầu, chỗ lội; `slotDist` < 4; r < 9; `riverEdge` < 0,3; `pathGap` < 0,3 |
| Viền ao, chân, mặt, mép vách | | | | 6.1, 6.2 | | |

L2-cau: 99 đá (35 sỏi sông, 27 phiến, 34 tảng, 3 gỗ).

### 6.7 L6 Rừng mép và vòng xa

| Tham số | Giá trị |
|---|---|
| Ranh giới | rải đều (luật M0b) chỉ từ r ≥ bán kính sân − 2 m (± 1,5 m nhiễu) ra ngoài; bên trong là lùm, cây lẻ, đá của bố cục |
| Mật độ | như M0b: `forest` = mix(ngoài, trong, trong sân) × smooth(9; 14; r), ngoài = 0,45 + 0,55 × smooth(0,3; 0,6; fbm(0,05/m)); ô cây 2,6 m (High) |
| Tán tím | 18 % tán tròn ở `laneGap` > 9 m và r > bán kính sân − 4 (M0b 40 %) |
| Trừ | lối mòn (`pathGap` < 1,2 với cây, < 0,6 với bụi), mặt vách |
| Dải gần | r ≤ bán kính sân + 6 = 38 m: model đầy đủ, đổ bóng (trừ đồ vụn: sỏi, phiến, gốc, gỗ) |
| Dải giữa | 38–42 m: model đầy đủ, không bóng |
| Dải xa | > 42 m: cây là impostor (một atlas, một InstancedMesh, một draw call, 2 tam giác một cây, không bóng, có sương); bụi và đá rải đều bỏ; đá của bố cục (vách) giữ model |
| Atlas impostor | nướng lúc nạp từ model: ô 256 px, 4 cột, chiếu trực giao từ 55° trên mặt đất, đèn trời 2,0 + nắng 2,2; tấm luôn quay về camera, neo ở gốc; lật ngẫu nhiên; sắc 0,86–1,06; cắt alpha 0,5. Lõi sẽ nướng một lần mỗi kit bằng `bake_impostor.py` |

### 6.8 L7 Sơn đất

**Mặt nạ:** RGBA8 phủ hình vuông ±52 m quanh bệ, ô 0,25 m (416²), có mipmap. Thế của một đĩa: trong r là 1 − 0,5 × (d/r)², ngoài r là 0,5 × (1 − smooth(r; r + rìa; d)), nhân độ mạnh; một kênh lấy max.

| Kênh | Gì |
|---|---|
| R đất | các đĩa đất bên dưới |
| G lối mòn | 6.3 |
| B hoa | mở × (0,85 × mảng + 0,6 × viền) × (1 − smooth(bán kính sân; + 6; r)) × smooth(7,5; 10; r); mở = smooth(0,8; 2,6; `laneGap`) × smooth(0,8; 2,2; mép nước) × (1 − smooth(0,25; 0,5; R)) × (1 − smooth(0,3; 0,5; G)) × (1 − smooth(0,25; 0,55; A)); mảng = smooth(0,42; 0,66; fbm(x/11, z/11)); viền = dải ngay ngoài mép đất và mép lối |
| A bóng tán | mỗi cây bố cục: r = 1,15 × tán, tầm r + 1,4: 0,5 × (1 − smooth(0; tầm; d)) + 0,5 × (1 − smooth(0,5r; r; d)), × 0,75; cộng rừng mép `forest` × smooth(bán kính sân − 6; + 2; r) |

**Đĩa đất (kênh R):**

| Nguồn | Bán kính | Rìa | Độ mạnh |
|---|---|---|---|
| Sân bệ | 6,5 m | 1,6 | 1 |
| Tâm mỗi lùm | 0,62 × R | 1,6 | 0,9 |
| Mỗi cây trong lùm | max(1,1; 0,78 × tán) | 1,3 | 1 |
| Mỗi cây lẻ | 2,1 m | 1,3 | 1 |
| Đầu lối mòn trong sân | 1,9 m | 1,2 | 0,75 |
| Hai đầu mỗi cầu, chỗ lội của làn (cách mép 1,2 m ra ngoài) | 3,1 m | 1,5 | 0,9 |
| Vệt mòn mép làn: dọc làn và vệt sau cổng mỗi 3,5–6,5 m, r > 7,5 m, ngoài cầu, chỗ lội ± 1 m, một bên ngẫu nhiên, lệch nửa bề rộng + 0–0,45 m | 0,7–1,5 m | 0,8 | 0,62 |
| Đất vụn chân vách | 6.2 | | |

L2-cau: 110 đĩa.

**Shader (nhận mặt nạ, vẽ mỗi khung trong spike; giai đoạn 3 nướng vào render target):**
- Đất: cắt ở R + nhiễu qua 0,46–0,54, chỉ trên đất phẳng (độ dốc < 0,22–0,38); lõi đậm nơi R qua 0,7–0,95; viền cỏ sáng nơi max(R, G) qua 0,16–0,42, pha 50 %.
- Làn: đất tới 0,9–1,06 nửa bề rộng (± nhiễu), mép mòn 0,62–0,96, hai vệt bánh ở 0,46, vai cỏ sáng tới 1,9 nửa bề rộng.
- Nền rừng: nơi bóng tán qua 0,32–0,72, ô rêu và lá kim.
- 8 ô đất (T1–T8) làm nét cọ trên bảng màu đã vẽ (ô chia màu trung bình của chính nó), lặp: cỏ A 7 m + xoay 10,5 m, cỏ B 8,5 m theo mảng, rêu 6, lá kim 6, đất lối 6,5, đất 5,5, cát 6, đá triplanar 4,5. Mỗi ô chỉ lấy mẫu nơi lớp của nó hiện được.
- 4 tờ decal (D1–D4), mỗi ô lưới một decal, tâm giữ trong ô, mật độ đọc tại tâm decal (nên không decal nào bị cắt), chỉ nơi độ dốc < 0,18:

| Decal | Ô lưới | Cỡ | Mật độ đọc | Dải |
|---|---|---|---|---|
| D2 hoa | 2,1 m | 0,7–1,25 m | B | 0,15–1,1 |
| D4 rêu (2 góc rêu) | 2,7 m | 1,0–1,7 m | 0,35B + 0,9A | lên 0,18–0,5, xuống 0,75–1,0 |
| D1 đất (nhuộm về màu đất kit) | 3,2 m | 1,1–1,9 m | 0,5R | lên 0,1–0,24, xuống 0,32–0,45 (chỉ viền đất) |
| D3 vụn rừng (sỏi, lá kim, cành; không lá cam) | 1,8 m | 0,7–1,2 m | 0,6R + 0,7A | 0,45–0,85 |

### 6.9 Spec L2-cau đề xuất (thay khối Rồng ở §8.1)

```json
{
  "format": "map-spec/0", "id": "L2-cau", "game": "dragon-hold", "unit": "cm", "seed": 20261028,
  "generator": { "factory": "0.1.0", "layers": { "fields": 1, "height": 1, "water": 1, "paths": 1, "vegetation": 1, "paint": 1 } },
  "layers": {
    "height": { "stamps": [{ "id": "north-west-bluff", "kind": "cliff", "outsidePlay": true,
      "line": [[-1900, -4000], [-2800, -3300], [-3550, -2200], [-3900, -1000], [-4000, 0]],
      "heightCm": 900, "ledgePermille": 720, "faceCm": [-80, 50, 110, 230], "plateauCm": 1400, "backCm": 1600,
      "capCm": 700, "raggedCm": 130, "raggedWaveCm": 600 }] },
    "water": { "river": "fromGameplay", "ponds": [{ "id": "pond", "site": "auto", "radiusCm": 460, "ringCm": [1400, 2300],
      "clearCm": { "lane": 700, "slot": 700, "sky": 600, "river": 900 }, "wobblePermille": 240, "depthCm": 85, "belowCm": 30,
      "lily": { "cellCm": 140, "permille": 400 } }] },
    "paths": { "widthCm": 105, "plazaTaper": { "permille": 400, "overCm": 500 }, "edgeTaper": { "permille": 600, "overCm": 800 },
      "stepCm": 300, "wobbleCm": 220, "wobbleWaveCm": 1400, "edgeOutCm": 600,
      "clearCm": { "slot": 460, "lane": 220, "water": 160 }, "endClearSlotCm": 700, "repairIterations": 10,
      "footpaths": [
        { "id": "fp-pond", "from": { "dais": "pond" }, "to": { "pond": true }, "bendPermille": 100 },
        { "id": "fp-west", "from": { "path": "fp-pond", "atPermille": 450 }, "to": { "river": 236 }, "bendPermille": -140 },
        { "id": "fp-south", "from": { "pond": 218 }, "to": { "edge": 196 }, "bendPermille": 160 },
        { "id": "fp-east", "from": { "pond": 84 }, "to": { "edge": 116 }, "bendPermille": -180 },
        { "id": "fp-north", "from": { "edge": 324 }, "to": { "edge": 283 }, "bendPermille": 300 } ],
      "neverEndAt": "slots" },
    "vegetation": {
      "groves": { "cellCm": 600, "countMax": 12, "radiusCm": [380, 750], "minRadiusCm": 260, "ringCm": [1100, 3000],
        "clearCm": { "lane": 340, "slot": 480, "sky": 300, "riverOver": 40, "pathOver": 220, "pond": 300 }, "gapCm": 350,
        "densityPerM2Permille": 110, "treeGapCm": 210, "heightCapCm": { "a": 360, "perMPermille": 260, "max": 800 },
        "violetClearCm": 900, "tints": 5, "rimBushPerMPermille": 220, "clutterPermille": 600 },
      "solitary": { "cellCm": 500, "count": 8, "ringCm": [1200, 2900], "gapCm": 700, "dirtCm": 210 },
      "rocks": { "river": { "stepCm": 150, "runPermille": 420, "run": [3, 7] }, "lane": { "stepCm": 200, "runPermille": 340, "run": [2, 5] },
                 "pond": { "count": 10 }, "cliff": { "foot": 200, "face": 240, "lip": 310 } },
      "edge": { "insideCm": 200, "violetPermille": 180, "bandsCm": { "near": 3800, "far": 4200 } },
      "keepClearOf": ["lanes", "sky", "slots", "dais"] },
    "paint": { "maskHalfCm": 5200, "maskCellCm": 25, "plazaCm": 650, "groveDirtPermille": 620, "canopyDirtPermille": 780,
      "loneDirtCm": 210, "junctionCm": 190, "crossingCm": 310, "scuffStepCm": [350, 650], "scuffCm": [70, 150],
      "flowerPatchWaveCm": 1100, "decals": { "flowers": 210, "moss": 270, "dirt": 320, "litter": 180 } }
  },
  "budget": { "high": { "propTriangles": 550000, "drawCalls": 40, "loadMs": 300 } }
}
```

---

## 7. Kit còn thiếu (theo thứ tự ưu tiên)

Tên theo luật "In-game names" (tiếng Anh). Mỗi món là một ảnh 2D Codex rồi một model Tripo của chủ dự án. Không món nào là của luật chơi; tất cả là decor, đặt ngoài làn và ô.

| # | Món | Vai trò | Vì sao trước | Cỡ, ngân sách |
|---|---|---|---|---|
| 1 | **Lantern Post** (cột đèn gỗ, đèn lồng) và **Rail Fence** (đoạn rào gỗ 2,4 m) | L5 đồ dọc lối mòn (phiếu 033 `along.ts`) | Ảnh mẫu dựa vào đèn và rào để làm nhịp dọc đường; 9/12 ảnh giới hạn chủ yếu ở đây | ≤ 600 tam giác mỗi món; đèn cao 2,2 m |
| 2 | **Maple Tree** (tán đỏ cam) | Điểm nhấn màu ấm trong lùm (5–10 % số cây) | Ảnh mẫu có tán đỏ, cam; tán tím của ta bị luật làn đẩy ra xa (05 §2.2). Màu đỏ, cam phải xa làn và không trùng màu cảnh báo của Héo: cần làn Rồng duyệt màu | ≤ 1.500 tam giác, như tán tròn |
| 3 | **Cliff Rock** (2–3 khối đá xám nhạt, cạnh gãy, không phủ rêu) | L2 dấu vách | Tảng đá hiện có (rock-boulder) tròn và phủ rêu, xếp lên mặt vách trông như trứng; vách là chỗ yếu nhất ở hướng 180° | ≤ 800 tam giác, cỡ danh nghĩa 4 m |
| 4 | **Grass Tuft**, **Wildflower Clump** (cụm cỏ, cụm hoa nhỏ) | Đồ vụn 3D trên bãi trống | Bãi cỏ của ta chỉ có decal phẳng; ảnh mẫu có cụm cỏ nổi | ≤ 300 tam giác, không bóng, instanced |
| 5 | **Reed Clump** (lau sậy) và **Wooden Jetty** (bến gỗ nhỏ) | Bờ ao, bờ sông | Ao đẹp nhưng bờ trơn; ảnh mẫu có cầu nhỏ trên ao | Lau ≤ 400; bến ≤ 1.500 tam giác |

---

## 8. Còn mở

- **Người chấm thứ hai:** 5/12 ảnh rơi vào vùng giáp ranh 6,5–7,5 (§6.2 đòi một subagent chấm độc lập). Làn spike này không có công cụ gọi subagent; điều phối viên chạy một lượt chấm độc lập trên `final2/`.
- **Hiệu năng:** chênh trung bình +2,62 ms so với đất trống (cổng ≤ 2 ms). Nướng sơn đất vào render target lúc nạp (§3.2) là bước đầu của giai đoạn 3; ước bớt 0,7–1 ms. Tam giác tổng (mọi lượt vẽ, cả 220 quái và bóng) 2,53 M, trên trần 2 M; nhưng riêng đất trống đã 1,81 M và M0b được duyệt ở 3,09 M, nên làn Rồng cần xác nhận cách đếm trần này.
- **Bố cục còn sửa được:** (1) rừng phía tây đặc thành tường: thêm một lùm thưa hoặc một khoảng trống ở mép rừng tây (luật "mép rừng có khe" mỗi 60–90°); (2) fp-west gần song song làn Suối: thêm luật góc ≥ 25° hoặc đổi hướng tới 220°; (3) đĩa đất dưới cây tròn đều: thêm nhiễu biên.
- **Ô đất và decal** được nạp từ `/art-src` trong dev (chỉ spike). Vào game phải đi qua `prepare-ground`, `prepare-decals` và media của Rồng.
- **Chưa thử** tier Medium, Low; chưa đo trên Firefox.
- **Mặt nạ sơn** nướng bằng JS số thực mất 76 ms; lõi tính bằng số nguyên (§8.5) sẽ chậm hơn hoặc nhanh hơn tùy cách tô; vẫn xa cổng 300 ms.
