# Thanh Thạch Ải rộng — map 1 theo D66 (v1.2, 15/11/2026 — một đường, camera B 42° chốt theo đề xuất)

> **Vai:** ghi chú thiết kế cho D66 ("map rộng hơn, tầm nhìn vẫn vậy, rê chuột thấy đoạn xa hơn"). Bổ sung, không thay, [`MAP1_CONCEPT.md`](MAP1_CONCEPT.md): vật liệu, ánh sáng, màu tín hiệu và sự sống ở đó vẫn giữ; ở đây chỉ đổi kích thước sân, camera trượt, chỗ đặt và hệ quả.
> **Nguồn:** [`00-canon.md`](00-canon.md) D48, D53, D57, D64, D66; `src/view/renderer.ts` (`VIEW`, `fitCamera`); `src/content/rules.ts` (`CAMERA`, `FIELD`); ảnh engine `games/immortality-cultivation/tmp/plan-2026-11-01/capture-1080.log`; Codex 365 (tranh một khung try6/try7).
> **Greybox:** `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/map1-wide/` (`overview-B.png`, `incam-home.png`, `incam-nw.png`, script `base.mjs`). Anh xem trước khi dùng.
> **Duyệt ngoài:** Gemini, xem §11.

> **13/11 09:5x:** anh đổi hướng: "tạm thời cứ để nó là map đường đơn trước, và chỉnh làm sao để góc nhìn có thể thấy quái di chuyển từ xa, và tốc độ quái di chuyển sẽ phù hợp với góc nhìn". Bản đang làm là mục **13. Một đường**. Mục 2–10 (phương án B hai đường) **để sau**; phiếu 377 tạm dừng.

## 1. Camera thật (đo, không đoán)

- Giải ngược từ 10 điểm engine chụp ở 1920 × 1080 (`capture-1080.log`): nghiêng 55°, FOV dọc 28°, **cự ly 52,8 m**, nhìn vào (0; 0; −2,06); camera ở (0; 43,3; 28,2). Sai số lớn nhất 0,3 px (≤ 2 px theo skill). Đây là khung do `fitCamera` tính cho sân 40 × 26 m với `headroomM` 2,5 (mã hiện tại; D53 ghi ~5,5 m nhưng `VIEW.headroomM` vẫn 2,5).
- **D66 khoá khung này:** khi sân rộng ra, `fitCamera` **không** được fit theo sân mới nữa (nếu fit, camera sẽ lùi xa và mọi thứ bé lại, trái D66). Cự ly và nhìn được tính một lần theo khung tham chiếu 40 × 26 m rồi giữ; pan chỉ dịch điểm nhìn (x, z).
- **Một khung trên mặt đất** (cả 1080p và 720p cùng hình thang, vì cùng tỉ lệ 16 : 9): mép trên z = look − 19,5 m, rộng x ±28,4; giữa khung ±23,4; mép dưới z = look + 13,7, rộng ±19,9. Tức **một khung ≈ 47 m ngang × 33 m sâu**.
- px/m ở 1080p: 31 (z −30), 35 (mép xa cũ), 42 (Trận Tâm), 46 (mép gần cũ). Ở 720p nhân 2/3. Không thấy trời (mép trên 41° dưới chân trời) — giữ nguyên mọi luật chiều cao của MAP1_CONCEPT §1.
- Bàn Quyết (DOM) che từ y ≈ 930 ở 1080p: dải dưới ~5 m đất luôn bị che.

## 2. Kích thước sân: ba phương án

"Khung" = 47 × 33 m ở trên. Sân gốc 40 × 26 m vừa đúng một khung.

| | Kích thước | Khung | Lợi | Hại |
|---|---|---|---|---|
| **A** | 94 × 50 m (x ±47, z −40…+10) | 2 × 1,5 | Ít đổi nhịp trận; pan ngang chỉ ~1 khung mỗi bên; dựng nhanh | Chưa "rộng hơn nhiều lần" như anh nói; vẫn thấy gần hết sân chỉ với một cú rê |
| **B (anh chọn 13/11 09:4x)** | 140 × 66 m (x ±70, z −54…+12) | 3 × 2 | Đúng ý "nhiều lần"; mỗi phía một khung riêng có cổng, mốc và câu chuyện; đường thú dài ~71 m (gấp ~3 lần ~23 m hiện nay) cho đủ chỗ đặt trận pháp và đánh sớm | Phải đổi nhịp sim (tốc độ hoặc giờ xuất quái); cần chỉ báo quái ngoài khung tốt; đất gấp ~9 lần, phải dùng ô lặp + decal |
| **C** | 188 × 83 m | 4 × 2,5 | Rất hùng vĩ, hợp map trùm sau này | Người chơi mất dấu trận; đường đi > 100 m làm trận lê thê; chi phí đất và hiệu năng gấp 15 lần; trái tinh thần gõ phím (mắt phải ở chữ) |

**Chốt B** (anh chọn 13/11 09:4x, đã xem greybox). Lý do: D66 nói "rộng hơn nhiều lần", A chưa đạt; C quá dài với một trận gõ 3–6 phút và làm mắt rời Bàn Quyết quá lâu. B giữ khung nhà là toàn bộ phòng tuyến hiện nay (Trận Tâm, Kết Giới, Trận Trụ, 6 ô) nên luật gameplay gần cũ, phần mới là **đường tới** và cảnh.

## 3. Bố cục (B, đã chốt) (toạ độ mét, bắc = −z)

| Mã | Vật | Ở đâu | Ghi chú |
|---|---|---|---|
| A | Trận Tâm | (0; 0), không đổi | Khung nhà nhìn vào (0; −2,06) như hiện nay |
| B | Trận Trụ T/P | (∓6,4; −7,7) | Không đổi |
| H | 6 ô cơ quan | như `FIELD` hiện nay | Không đổi; có thể thêm ô xa ở pha sau (không trong note này) |
| D | **Ải trong** A/B | (∓15; −18), cao 5 m | Chỗ cổng cũ thành cổng chắn thứ hai: thú đi qua, không xuất hiện ở đây nữa |
| C | **Cổng ngoài** A/B | (∓58; −46), cao 7 m | Nơi thú xuất hiện; ngoài khung nhà, chỉ thấy khi pan |
| 2 | Hành lang A/B | rộng 6 m, uốn từ cổng ngoài → (∓48; −28) → (∓22; −22) → ải trong → Kết Giới | Dài ~71 m; uốn khúc để có góc đặt trận và để khung pan nào cũng có đường |
| E | **Thiên Đàn** (mốc chính mới) | (0; −40), 14 × 10 m; sàn trùm đứng ≤ 3 m, vòm trang trí phía sau (z −43) ≤ 8,5 m | Đài tế cổ, trận văn cổ khắc (theo D64), nơi trùm xuất hiện ở đợt cuối; nhìn thấy khi pan bắc |
| F | Vọng lâu đổ nát | (−44; −12), cao ≤ 10 m | Mốc phụ phía tây |
| 7 | Thác Đông | x 44…56, z −30…0 | Mốc phụ phía đông: vách đá, thác đổ xuống biển mây (nhìn từ trên) |
| G | Tường thành bắc | z −56, cao 3 m | Biên bắc; ngoài là biển mây. Lưới đất (váy) 160 × 72 m: x ±80, z −58…+14, để góc khung và lề chiêu không lộ khoảng trống |
| ✦ | Lối trời | hai góc bắc (±70; −54) | Thú bay vào từ góc, bay thẳng về Trận Tâm |
| 6 | Sơn Môn | nam, z +8…+12 | Như cũ; nằm dưới Bàn Quyết |
| 4/5 | Biển mây, vực | ngoài biên | Chỉ thấy ở góc khung khi đứng sát biên |

Thứ tự mắt nhìn ở **khung nhà**: Trận Tâm → hai ải trong và thú đổ vào → hai Trận Trụ. Ở **khung xa**: cổng ngoài hoặc mốc của khung đó → đường sáng. Mỗi khung pan chỉ một mốc (không hai điểm nhấn cạnh tranh).

## 4. Luật trượt mép (edge-pan)

- **Vùng mép:** 24 px CSS mỗi cạnh trái, phải, trên (≈ 1,25 % ngang ở 1080p). **Cạnh dưới:** dải 24 px **ngay trên** Bàn Quyết (y 906–930 ở 1080p, theo mép trên thật của Bàn Quyết); chuột vào Bàn Quyết thì ngắt pan (sửa sau Gemini: v0.1 không có pan nam).
- **Tốc độ:** theo độ sâu trong dải, từ 0 ở mép trong dải tới **30 m/s** sát mép (≈ 0,65 khung/s; đi hết bề ngang 93 m của vùng clamp trong ~3,1 s). Góc màn hình = pan chéo, chuẩn hoá để chéo không nhanh hơn.
- **Gia tốc:** tăng tới tốc độ đích trong 0,15 s, dừng trong 0,12 s (damp mũ, không giật). Đợi **0,15 s** chuột nằm trong dải mới bắt đầu (lướt qua để bấm nút gần mép không làm trượt).
- **Kẹp:** điểm nhìn x ∈ [−43,6; +43,6], z ∈ [−36,5; −2,06] (nam khoá đúng khung nhà). Góc trên khung khi sát biên tới x ±72, z −56; váy đất 160 × 72 m phủ cả lề chiêu 2 m. Phần ngoài sân 140 × 66 m là vực, biển mây, tường — không để trống.
- **Buông:** đứng yên chỗ đó (D66). Không tự quay về.
- **Không tự về nhà.** Gemini đề xuất tự kéo camera về sau 3 ký tự hoặc 2,2 s; bác vì trái D66 ("buông thì đứng yên"). Nếu anh muốn, thêm làm tuỳ chọn Settings "Tự về khi gõ", mặc định Tắt.
- **Về nhà:** một thao tác (nút trên HUD, hoặc nhấp đúp vào minimap/chỉ báo Trận Tâm) đưa về (0; −2,06) trong 0,35 s. Nhấp vào chỉ báo quái ngoài khung → pan tới đó.
- **Tắt khi:** chuột ra khỏi cửa sổ, cửa sổ mất focus, đang mở menu/Settings/Shop, đang cut-in hoặc cảnh phim, đang zoom cận D57 (khi zoom, camera đi theo anh hùng; pan mép chỉ hoạt động ở mức zoom toàn khung).
- **Gõ phím an toàn:** pan **không bao giờ** gắn phím chữ, số, Space, Enter, Backspace, Esc hay mũi tên (mũi tên đã là `arrow-*` của `KEY_BINDINGS`). Bàn Quyết giữ focus; pan chỉ đọc vị trí con trỏ. Không có bàn phím pan mặc định ở MVP.
- **Giảm chuyển động / trợ năng (Settings):** "Rê mép để xem xa": Bật (mặc định) / Chậm (15 m/s) / Tắt. Khi `prefers-reduced-motion`, mặc định Chậm. Khi Tắt: chỉ kéo chuột giữa và nhấp chỉ báo/minimap. Kéo chuột giữa luôn có.
- Pan chỉ là view: sim, hitbox, hash vàng không đổi vì pan.

## 5. Quái vào ở đâu, và chỉ báo quái ngoài khung

- Thú bộ xuất hiện ở **cổng ngoài** A/B (ngoài khung nhà), đi ~71 m qua ải trong vào Kết Giới. Thú bay từ hai góc bắc. Trùm đợt cuối xuất hiện trên **Thiên Đàn** rồi xuống đường giữa (một nhánh ngắn từ Thiên Đàn nhập vào hai hành lang tại (∓22; −22); chốt ở bước sim).
- **Chỉ báo ngoài khung** (cùng hệ D57 khi zoom): mũi tên mảnh trên **vòng cung bán elip quanh Bàn Quyết** (tâm (960; 860), bán kính 400 × 180 px ở 1080p; y 680–880), không phải ở mép trên xa mắt (sửa sau Gemini). Hướng mũi tên = hướng từ tâm khung tới cụm, gộp cụm trong 8 m; ≤ 40 % đục để không che hành lang gần Kết Giới; số đếm ≥ 20 px. Giữa vòng cung và dải pan dưới có 26 px đệm chết. Màu theo tín hiệu canon: thường xám trắng, tinh anh cam `#FFB020`, trùm/đòn sắp đánh đỏ `#FF4A4A`. Kèm số đếm, nhịp đập khi cụm đến ải trong. Không che dải chữ, không vào Bàn Quyết; ở cạnh dưới đặt ngay trên y 930.
- Chỉ báo cũng là nút: nhấp → pan tới cụm.
- Một **minimap nhỏ** (góc trên phải, ~180 × 85 px) là tuỳ chọn ở pha sau; MVP dùng chỉ báo mép.

## 6. Anh hùng, Trận Tâm, trận pháp

- Anh hùng đứng ở Tâm nhãn (0; +3) như cũ; khung nhà không đổi so với trận hiện nay, nên toàn bộ tranh map một khung (Codex 365 try6/try7) vẫn đúng **cho khung nhà**, chỉ thay hai cổng bằng ải trong và mở đường ra ngoài.
- Trận pháp và ô cơ quan đặt trong khung nhà (luật cũ). Đặt ra xa là thiết kế sau, không trong note này.
- Sát thương chốt ngay khi gõ xong từ (sim không đợi hình bay); hình đạn tới đích xa ≤ 0,3 s (đường bay 76 m tới cổng ngoài không được kéo 3 s).
- Khi đang nhìn xa và một từ được gõ đúng, chiêu vẫn bắn từ anh hùng; nếu điểm phát ngoài khung, chỉ báo "đòn từ Trận Tâm" ở mép (một vệt sáng đi vào từ mép khung).

## 7. "Chiêu toả tới hết màn" nghĩa là gì bây giờ

Theo D66: **mép khung đang nhìn**, không phải mép sân.
- Vùng ảnh hưởng của chiêu toàn màn = hình thang mặt đất của khung hiện tại (tính bằng `groundAt` 4 góc, cộng 2 m lề), không phải 140 × 66 m.
- Hệ quả thiết kế: người chơi pan ra cổng ngoài rồi tung chiêu toàn màn là một lựa chọn chiến thuật (đánh sớm ở đường xa). Phải có giới hạn: chiêu vẫn tốn như cũ; Kết Giới không được bảo vệ bởi chiêu tung ở khung xa.
- VFX lớn (sét trời D65, mưa kiếm) sinh theo hình thang khung, không rải cả sân.

## 8. Hiệu năng: stream và cull

- Sân 9 240 m² ≈ 9 lần cũ, nhưng **mỗi lúc chỉ thấy ~1 600 m²** (~1 460 m² trên Bàn Quyết). Cắt theo frustum lưới 8 × 6 m cho mesh dựng sẵn; cảnh vật xa thì `visible = false`.
- **Đất:** váy 160 × 72 m chia 10 × 6 chunk 16 × 12 m; 6 vật liệu PBR lặp gom trong `sampler2DArray` (≤ 3 lớp trộn mỗi điểm, giữ dưới trần 16 texture unit) + mask vẽ tay 640 × 288 (4 px/m) + decal. Thử scissor bỏ vẽ dải dưới Bàn Quyết nếu nó đục.
- **Quái ngoài khung:** sim chạy đủ; view cho quái ngoài khung + 8 m dùng LOD thấp nhất hoặc không vẽ (impostor theo D36), không cập nhật xương, không VFX đi kèm. Âm thanh quái ngoài khung giảm theo khoảng cách tới tâm khung (mix có sẵn bus `enemies`).
- **Mốc lớn** (Thiên Đàn, Vọng lâu, Thác) tải khi trận bắt đầu (không stream giữa trận, tránh giật); mỗi mốc ≤ 1 draw-group chính + instancing cho đá, tùng.
- **Bóng:** shadow camera đi theo khung đang nhìn (bao hình thang + 5 m), dịch theo bội số texel bóng để bóng không rung khi pan.
- **Ngân sách:** đo lại p95 ở High (trần 12 ms) với pan liên tục qua cả sân và triều thú đầy; dynamic resolution D57 vẫn chạy.

## 9. Việc đổi ngoài view (cần chốt riêng)

- `FIELD` (sim) phải rộng ra và có đường mới. Đường tới **mép** Kết Giới: 14,4 m → ~70 m (**gấp ~4,8**, Gemini sửa đúng số của v0.1). Gợi ý của Gemini: tốc độ hai pha (ngoài ải ×2,6, trong ải ×1,0) để tổng ~22 s và giữ nguyên ~9 s phòng thủ trong khung nhà. Đây là quyết định cân bằng, chốt ở bước sim.
- `fitCamera` tách thành "khung tham chiếu cố định" + pan; test `ic-camera-frame` đổi sang kiểm khung nhà.
- D48 "luôn thấy toàn sân" không còn đúng với sân; ý của nó chuyển thành: khung nhà thấy toàn phòng tuyến, và quái ngoài khung luôn có chỉ báo.

## 10. Phần tranh cần vẽ

Tranh ý tưởng vẽ **trên greybox** (`overview-B.png` cho bố cục, `incam-home.png` và `incam-nw.png` cho đúng camera): một tranh nhìn từ trên cả sân (để dựng ô đất và mốc) và hai tranh đúng camera (khung nhà, khung tây bắc). Chất liệu, ánh sáng (nắng sớm đông bắc), màu tín hiệu: theo MAP1_CONCEPT §3–5. Phiếu: [`../../codex-queue/377-tt-map1-wide-paint.md`](../../codex-queue/377-tt-map1-wide-paint.md).

## 11. Duyệt ngoài (Gemini)

Xem [`source/MAP1_WIDE_GEMINI_2026-11-13.md`](source/MAP1_WIDE_GEMINI_2026-11-13.md). Gemini (Argon, Cao): **7,4/10, đồng ý B có điều kiện**, tự duyệt FAIL → PASS → PASS. Nhận: váy đất và clamp, Thiên Đàn thấp, pan cạnh dưới, chỉ báo gần Bàn Quyết, số ×4,8, ngân sách texture. Bác: tự về nhà khi gõ (trái D66), phím Tab (MVP không gắn phím).

## 12. Câu hỏi cho anh

1. ~~Kích thước~~: đã chốt B (13/11 09:4x).
2. Có muốn tuỳ chọn "Tự về khung nhà khi gõ" (mặc định Tắt) không?
3. ~~Greybox~~: anh đã xem 13/11; phiếu vẽ `../../codex-queue/377-tt-map1-wide-paint.md`.

## 13. Một đường — **chốt camera B (42°), 15/11, theo đề xuất; anh xem sau**

> Anh (15/11): cứ làm theo đề xuất vì chưa có thời gian xem. Greybox chốt: `owner-review/2026-11-15/tu-tien/map1-wide/lane-B-final.png` (script `captures/tu-tien/map1-wide/lane-final.mjs`). Phiếu vẽ: [`../../codex-queue/384-tt-map1-lane-paint.md`](../../codex-queue/384-tt-map1-lane-paint.md).

Thú đi **một hành lang** rộng 6 m từ xa phía bắc (trục x ≈ 0) vào Kết Giới (mép z −9). Trận Tâm, Trận Trụ, Tâm nhãn giữ chỗ cũ. Sân vẫn có thể rộng hơn khung (D66, pan mép như §4) nhưng chỉ một đường; ô cơ quan dời dọc hai bên đường (chốt khi dựng sim). Thú bay vẫn từ góc bắc.

### 13.1 Ba cách cho góc nhìn thấy quái từ xa (đo, 1920 × 1080)

Mỗi cách đặt Tâm nhãn (0; +3) ở y 880, ngay trên Bàn Quyết (y 930). "Quái xa nhất" là quái cao 1,5 m còn lọt cả đầu trong khung; "đường thấy được" là phần đường từ đó tới mép Kết Giới. Script: `captures/tu-tien/map1-wide/lane.mjs`, `lane-views.mjs`.

| Cách | Camera | Giữ D66 "tầm nhìn vẫn vậy"? | Quái xa nhất | Cao 1,5 m ở đó | Ở Kết Giới | Đường thấy được | Ảnh |
|---|---|---|---|---|---|---|---|
| Hiện nay | 55°, FOV 28°, 52,8 m, nhìn z −2,06 | — | z −19 | 40 px | 38 px | **~10 m** đi thẳng | — |
| **A** | Giữ nguyên camera; đường gấp chữ S ngang khung | **Giữ** | z −19,4 | 40 px | 38 px | 51 m (nhưng dồn trong 25 % trên của màn, ba nhánh chồng nhau) | `lane-A.png` |
| **B** | Nghiêng **42°**, FOV 28°, cự ly 52,8 m (camera hạ 43,3 → 35,3 m), nhìn z −7,55 | Đổi góc | **z −31** | 42 px | 46 px | 34 m, uốn nhẹ | `lane-B.png` |
| **C** | Nghiêng **45°**, FOV 28°, cự ly 60 m (cao 42,4 m, gần như cũ), nhìn z −8,5 | Đổi góc, giữ độ cao | **z −33** | 37 px | 39 px | 35 m, uốn nhẹ | `lane-C.png` |

Cũng đã đo: chỉ dời điểm nhìn lên bắc giữ 55° thì quái xa nhất z −23 (đường ~14 m); FOV 38° thì z −25 (~16 m). Cả hai đều ít lợi, không đưa vào.

- **A** là cách duy nhất giữ đúng D66, nhưng không "thấy từ xa": mép trên khung vẫn ở z −21; đường chỉ dài ra nhờ gấp khúc, các nhánh chồng ở dải trên màn và quái đi ngang chứ không tiến lại.
- **B** thấy xa nhất trong khi quái gần lại **to hơn** (46 px ở Kết Giới, hiện 38). Không thấy trời (mép trên 28° dưới chân trời). Cổng/trụ cao ở xa sẽ che đường nhiều hơn: ngân sách chiều cao ở mép xa phải đo lại.
- **C** thấy xa tương đương B, giữ độ cao camera, quái ở mức cỡ hiện nay.
- **Đề xuất: B**, vì vừa thấy xa vừa làm quái gần to hơn (đúng góp ý D57 của anh "quái và nhân vật bé"). Nếu anh muốn giữ cảm giác camera hiện nay nhất thì chọn C. Cả hai đều sửa D48/D66 về góc (55° → 42° hoặc 45°): cần anh chốt.

### 13.2 Tốc độ quái theo góc nhìn

Mục tiêu thời gian đi hết đường **thấy được**: quái thường ~12 s, nhanh ~8 s, chậm ~18 s, trùm ~25 s. Tốc độ hiện có (`src/content/data/beasts.ts`, `boss.ts`, mm/s): Thạch Thử 1 600, Phong Lang 1 400, Lang Đầu Đàn 1 400, Hỏa Nha (bay) 2 000, Nham Viên 1 000, Thiết Giáp Trư 1 000, Thiết Bối Lang Vương 1 200. Độ khó nhân thêm `speedPm` 900–1 050.

| | Thời gian đích | A (51 m) | **B (34 m)** | C (35 m) |
|---|---|---|---|---|
| Thường | 12 s | 4,3 m/s | **2,8 m/s** | 3,0 m/s |
| Nhanh | 8 s | 6,4 | **4,2** | 4,4 |
| Chậm | 18 s | 2,8 | **1,9** | 2,0 |
| Trùm | 25 s | 2,0 | **1,35** | 1,4 |

Với tốc độ hiện nay ở cách B: Phong Lang mất ~24 s, Nham Viên ~34 s: quá chậm so với khung mới. Đề xuất cho B (m/s; giữ thứ bậc giữa các loài): Thạch Thử 1,6 → **3,0** (11 s), Phong Lang 1,4 → **2,6** (13 s), Lang Đầu Đàn 1,4 → **2,4** (14 s), Nham Viên và Thiết Giáp Trư 1,0 → **1,9** (18 s), Thiết Bối Lang Vương 1,2 → **1,35** (25 s). Hỏa Nha bay thẳng, không theo đường: giữ 2,0 rồi đo lại khi chốt lối trời. Ở A các con số nhanh gấp 1,5 lần mà vẫn chỉ đi trong dải trên màn: lý do thêm để không chọn A.

- Thú sinh ngay trên mép trên khung (B: z ≈ −36), không đi một đoạn dài ngoài màn; nếu sân rộng hơn khung theo D66, đoạn ngoài màn chạy nhanh hơn hoặc thú sinh ở mép khung đang nhìn của đường.
- Đây là số cân bằng: sim, hash vàng và thử chơi (D18 WPM) chốt ở bước sim, không ở concept.

### 13.3 Đã chốt (15/11, theo đề xuất, anh xem sau)

- **Camera B:** nghiêng 42°, FOV 28°, cự ly 52,8 m, camera (0; 35,3; 31,7), nhìn (0; 0; −7,55). Tâm nhãn ở y 880 (1080p). Quái 1,5 m xa nhất thấy được ở z −31 (42 px); ở Kết Giới 46 px. Sửa góc của D48/D66 (55° → 42°); D66 phần "sân rộng hơn khung, pan mép" vẫn áp dụng nếu cần.
- **Bố cục greybox:** đường đá 6 m uốn mềm từ cổng ải (0; −40, ngoài khung, thấy khi pan) qua (−3; −34), (−6; −26), (−3; −19), (3; −14) vào Kết Giới; Vọng lâu đá (−15; −21) ≤ 6 m; tùng cổ và tảng đá (15; −25); vực và biển mây ngoài x ±22; 6 ô cơ quan dời dọc hai bên đường (H1 (−7; −20), H2 (5; −23), H3 (−9; −13), H4 (8; −17), H5 (−11; −4), H6 (11; −4); chốt ở sim). Trận Tâm, Trận Trụ, Tâm nhãn giữ chỗ.
- **Tốc độ quái (B, m/s, chờ sim và thử chơi):**

| Quái | Hiện nay | Chốt cho B | Thời gian đi hết ~34 m thấy được |
|---|---|---|---|
| Thạch Thử | 1,6 | 3,0 | ~11 s |
| Phong Lang | 1,4 | 2,6 | ~13 s |
| Lang Đầu Đàn | 1,4 | 2,4 | ~14 s |
| Nham Viên | 1,0 | 1,9 | ~18 s |
| Thiết Giáp Trư | 1,0 | 1,9 | ~18 s |
| Thiết Bối Lang Vương (trùm) | 1,2 | 1,35 | ~25 s |
| Hỏa Nha (bay) | 2,0 | 2,0 (đo lại khi chốt lối trời) | — |

- Việc sau (không trong concept): `VIEW.tiltDeg` 42 và khung cố định (không fit theo sân), `FIELD` một đường, ô cơ quan mới, `speedMm` theo bảng, test `ic-camera-frame` theo khung mới; anh xem lại khi có thời gian.

### 13.4 Bề rộng đường (15/11, anh thấy "đang hơi bé", muốn nhiều quái hơn)

Ba greybox ở camera B 42°, mỗi bản rải **60 quái thường cao 1,5 m** thành bầy dọc phần đường thấy được (hàng ngang cách 1,3 m). Tấm ghép: `owner-review/2026-11-15/tu-tien/map1-wide/lane-width-8-12-16.jpg` (script `captures/tu-tien/map1-wide/lane-width.mjs <rộng> <số quái>`). Đường càng rộng thì chữ S càng mềm lại (biên độ nhân 7/rộng) để chỗ uốn không tự cắt; Trận Trụ và ô cơ quan dời ra theo mép đường.

| Rộng | Hàng ngang | Quái thấy được (trong 60) | Cao quái (px, 1080p) | Sức chứa phần đường thấy được (khít 1,3–1,4 m) | Mép đường gần nhất tới mép khung | Bàn Quyết che đường? | Trận Trụ x |
|---|---|---|---|---|---|---|---|
| 6 m (hiện) | 4 | — | 42–46 | ~70 | ~690 px | Không | ±6,4 |
| 8 m | 5 | 60 | 42–46 | ~91 | 657 px | Không (đáy đường y 560) | ±6,4 |
| **12 m** | 8 | 60 | 43–47 | **~134** | 648 px | Không (y 673) | **±7,6** |
| 16 m | 11 | 60 | 43–47 | ~178 | 604 px | Không (y 568) | ±9,6 (ra ngoài Kết Giới r 9) |

- Cỡ quái gần như không đổi theo bề rộng (camera không đổi): 42–47 px, trên sàn 36 px của quái Nhỏ (§21.1).
- Cả ba đều còn > 600 px tới mép khung mỗi bên: đường rộng vẫn nằm giữa, không lấp màn; Bàn Quyết không che.
- 16 m: đường gần như thẳng (S mất), bầy thành mảng chữ nhật, Trận Trụ phải ra x ±9,6, mất cảm giác "đường ải"; 8 m chỉ thêm ~30 % sức chứa.
- **Đề xuất 12 m:** gấp đôi bề rộng, sức chứa ~1,9 lần (~134 quái thấy cùng lúc), vẫn giữ chữ S mềm, Trận Trụ chỉ dời ±6,4 → ±7,6.
- **Số quái mỗi đợt (đề xuất cho 12 m, chờ sim và thử chơi):** đợt thường đang thiết kế cho đường 6 m, nhân **×1,8** số quái bầy (swarm) và ×1,4 quái thường; tinh anh và trùm giữ nguyên. Giữ đỉnh **≤ 90 quái** trên màn (≈ 2/3 sức chứa) để bầy còn đọc được hình đường và để từ gõ không chồng nhau; quá 90 thì thêm hàng chờ ngoài khung chứ không ép vào đường. Đo lại khung hình (High ≤ 12 ms) với 90 quái + VFX trước khi chốt.
