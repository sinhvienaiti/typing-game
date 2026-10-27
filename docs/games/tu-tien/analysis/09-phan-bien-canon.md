# Tu Tiên Thủ Ải: 09. Phản biện canon và kế hoạch M0a (25/10/2026)

> **Vai:** người phản biện đối kháng, chỉ đọc. Tìm chỗ hỏng trong [`00-canon.md`](../00-canon.md) và [`M0A_PLAN.md`](../M0A_PLAN.md) vừa viết, trước khi bước 0 bắt đầu. Không viết lại thiết kế; mỗi mục có cách sửa cụ thể để người giữ canon chép vào.
> **Đã đọc:** toàn văn `00-canon.md`, `M0A_PLAN.md`; `DANH_GIA_2026-10-24.md` §3–§8 và Phụ lục A, B; `analysis/08-phan-bien.md`; `docs/games/BALANCE.md`; `docs/games/dragon-lane/00-canon.md`; `docs/games/SPLIT_PLAN.md` §9–§10. Mã đã mở: `games/dragon-hold/{AGENTS.md, LANES.md, package.json, src/sim/fixed.ts, src/typing/deck.ts, src/view/crowd.ts, src/view/bench.ts, scripts/visual/scenarios/dh-bench.mjs, tests/boundary.test.ts}`; `shared/game-kit/{README.md, three/{stage,hero,particles,model-contracts}.ts, typing/{budget,config,session}.ts, balance/pace.ts, feedback/{audio-cues,profiles,numbers}.ts, platform/safe-storage.ts, tools/cdp-run.mjs}`; `games/typing-survival/src/view/{crowd,fx}.ts`; các tệp nối repo cha (`package.json`, `dev.sh`, `play.sh`, `infra/nginx/*`, `media/media.config.json`, `portal/public/games.json`, `portal/tests/learning-bridge.test.mjs`, `scripts/*`, `.github/workflows/ci.yml`).
> **Đã chạy (chỉ đọc):** `node --test scripts/media/test/unit.test.mjs` (lọc một test), `node scripts/validate-space-integration.mjs`, `node scripts/validate-play-mode.mjs`.
> **Mức** (như `08`): **chặn** = phải chốt trước khi làn liên quan viết mã · **lớn** = phải sửa trước khi chạy vòng cổng M0a (hoặc trước mốc ghi trong mục) · **nhỏ** = sửa ở lượt sửa canon kế.
> **Bằng chứng** ghi `tệp §mục`; "canon" là `00-canon.md`, "kế hoạch" là `M0A_PLAN.md`, "đánh giá" là `DANH_GIA_2026-10-24.md`. Mọi số tôi tính lại đều ghi phép tính để người sửa kiểm được.
> **Trạng thái (25/10, sau lượt sửa):** mọi mục PB-01 đến PB-37 đã áp vào canon (quyết định D32–D46, mã `PB-xx` ghi tại chỗ sửa) và kế hoạch M0a. Chỗ người sửa chọn khác đề xuất ở đây, có ghi lý do trong canon: từ nền vẫn lên ô 2, ô 5, Ấn qua bước lùi "quen hơn" để trận lạnh chơi được (canon §17.1, câu hỏi mở 13); vế "bot gõ mọi chữ cần ≥ 3 phiên" của HC4b thành báo cáo vì công thức điểm không cho phép (câu hỏi mở 11); hết đợt theo luật của Rồng (mọi toán đã sinh và 0 thú sống); Vương t đích 120 s áp cho mọi trận có Vương (W 64); cửa sổ Trận Quyết `max(T₂; max(8 s; T₂) / k)` để không ghế nào dưới T₂. Tệp này giữ làm nhật ký lý do.

## 1. Kết luận ngắn

1. **Ba chỗ phải chốt trước khi viết mã.** (a) Ranh giới `local` và sim chưa khép: Hộ thân "đỡ một nửa khi đứng trên vạch", "che điểm nhãn trong 2 m", đan hồi Sinh lực, ví Linh Sa đều cần vị trí hoặc trạng thái của người thật trong thế giới chung, trái D28 (PB-01). (b) `deck.ts` của Rồng mà kế hoạch định chép coi 50 từ chưa từng gặp là "đã thuộc" và đổi nhãn từ mới thành "đang học", nên từ chưa gặp lên ô gấp mà HC1 vẫn xanh (PB-02). (c) Thang lùi HN0 cắt kiếm của "vạn kiếm" trước khi đụng tới đám đông, trái đúng câu anh chọn ở D03: "phần nào trượt thì phần đó xuống" (PB-03).
2. **Nhiều số không cùng đứng được.** Đại Triều thực tế 13–15,5 phút (đánh giá cho ≤ 12); ô 1 là 30 % sát thương gõ chứ không 20 %; "một từ ô 1 hạ Phong Lang" ra 0,999 W; quỹ học 15 % của Linh Sa nhỏ hơn tổng thưởng học cố định; thú Nhỏ tới Kết Giới trong 4,5–7,9 s chứ không 8–12 s; thú được gọi thêm không tính vào máu đợt.
3. **Hại việc học còn bốn lỗ:** từ mới trong trận chỉ gặp một lần (Rồng có cổng G12 "gặp ≥ 2 lần", canon không có); Tĩnh Tu cho lĩnh ngộ sau 3 phiên không gõ phím nào (sàn 40 điểm); Tham Ngộ bắt phân biệt Tâm ma không nhãn với Thường bằng chủ đề trong khi Thường không bị giới hạn chủ đề; trần đổi hồ sơ ±10 %/phiên hai chiều làm người mới gõ nhanh phải chơi ~9 phiên quá dễ.
4. **Cổng chung giữ được dải**, nhưng hai chỗ làm cổng không đo được: cổng học B8 và HC chạy bằng bot trong khi luật nói bot không tạo sự kiện học; Nhàn I theo "nhàn quyết định" phụ thuộc chỗ người chơi đứng và trùng tick với Áp lực P.
5. **Kế hoạch làn khả thi nếu sửa bốn điểm:** phần nối repo cha **đã làm xong** (kế hoạch §2.3 còn ghi "thêm", và test media đang đỏ vì mục game mới); kit `feedback` phát âm tổng hợp bằng `OscillatorNode` và hồ sơ `tutien` cần sửa kit chung mà không làn nào giữ; kit `three` chỉ có `Hero` là nhân vật **bay** và hợp đồng model đòi clip `Hero_Fly`, `Boss_Idle_Hover`; sổ cái từ mới đặt trong `src/typing` sẽ trượt test ranh giới chép từ Rồng.
6. **Hướng 3D làm được với kit `three`** (một `Stage3D`, đám đông instanced chép từ Rồng, VAT và impostor viết mới), nhưng phán quyết HN0 phải đo theo số thú mà luật thật dùng (60 ở M0a, 120 ở M1) và có ngân sách con cho từng phần, nếu không bench 300 thú sẽ đẩy đám đông xuống 2D ở mức game không bao giờ chạm tới (PB-19).

## 2. Bảng vấn đề

| # | Vấn đề | Mức | Nhóm |
|---|---|---|---|
| PB-01 | Ranh giới `local`/sim: Hộ thân trên vạch, che nhãn 2 m, đan lên Sinh lực, ví Linh Sa | **chặn** | Mâu thuẫn, kiến trúc |
| PB-02 | `deck.ts` của Rồng: khởi đầu lạnh và từ lấp chỗ đưa từ chưa gặp lên ô gấp, HC1 không bắt | **chặn** | Học, cổng |
| PB-03 | Thang lùi HN0 cắt kiếm trước đám đông, không theo phần trượt | **chặn** (Làn 1) | Quyết định của anh, 3D |
| PB-04 | Thời lượng trận vượt trần của đánh giá; thiếu cổng thời lượng | lớn | Số |
| PB-05 | Ô 1 = 29,8 % sát thương gõ, không phải ~20 %; CB3 nằm trên mép | lớn | Số, cổng |
| PB-06 | "Một từ ô 1 hạ Phong Lang" ra 0,999 W; Tích Kiếm phá thêm | lớn | Số |
| PB-07 | Quỹ học 15 % Linh Sa nhỏ hơn thưởng học cố định; test "đúng 1.325" không đứng | lớn | Số, kinh tế |
| PB-08 | Hình học sân và tốc thú không cho 8–12 s tới Kết Giới | lớn | Số |
| PB-09 | Thú gọi thêm không vào máu đợt; đợt 5 vượt dải đợt giữa | lớn | Số |
| PB-10 | Sổ cái từ mới: trái test ranh giới, trùng tên kit, thiếu nghĩa, không vào replay | lớn | Học, định nghĩa |
| PB-11 | Từ mới trong trận chỉ gặp một lần | lớn | Học |
| PB-12 | Tĩnh Tu: lĩnh ngộ sau 3 phiên không gõ | lớn | Học |
| PB-13 | Tham Ngộ: Tâm ma không nhãn và Thường không phân biệt được | lớn | Học |
| PB-14 | Trần đổi hồ sơ ±10 %/phiên hai chiều | lớn | Công bằng |
| PB-15 | Bàn Quyết lúc nghỉ, Cast `fizzled` cho Chân Nguyên, Dưỡng, Văn Khí | lớn | Định nghĩa, cân bằng |
| PB-16 | Trận Quyết 8 s không theo công thức T (M1) | lớn | Công bằng |
| PB-17 | Nhàn I phụ thuộc vị trí, trùng P; chính sách đi của bot chuẩn chưa định | lớn | Cổng chung |
| PB-18 | Cổng học chấm bằng bot trong khi bot không tạo sự kiện học | lớn | Cổng chung |
| PB-19 | HN0 đo 300 thú nhưng luật dùng 60/120; thiếu ngân sách con | lớn | 3D, đo |
| PB-20 | Kit `feedback` phát âm tổng hợp; hồ sơ `tutien` cần sửa kit chung | lớn | Âm, khả thi |
| PB-21 | Kit `three`: `Hero` bay, hợp đồng model đòi `Hero_Fly`, `Boss_Idle_Hover` | lớn (M0b) | 3D, khả thi |
| PB-22 | Nối repo cha đã có; kế hoạch §2.3 cũ; test media đỏ; cờ cổng trùng | lớn | Khả thi |
| PB-23 | Thiếu phím cho cửa hàng và đặt cơ quan | lớn | Định nghĩa |
| PB-24 | Thiếu luật số nguyên, ĐĐ, `WaveDef`, `TelegraphDef`, thời điểm chạm | lớn | Định nghĩa |
| PB-25 | Thiếu định dạng replay, nhật ký, bản lưu; golden không băm `local` | lớn | Định nghĩa |
| PB-26 | Thiếu thứ tự lùi khi không có từ thỏa luật chữ | lớn | Định nghĩa, học |
| PB-27 | Báo trước dưới 1,2 s (Nham Viên 0,8 s, Thiết Giáp Trư 0,9 s) | nhỏ | Mâu thuẫn |
| PB-28 | CB5 có mệnh đề hiển nhiên; preset Học thiếu độ dài Ấn; đòn bẩy `telegraphScale` | nhỏ | Cổng, số |
| PB-29 | Lệch đánh giá chưa ghi quyết định: pháp bảo, tu vi "mỗi bậc ải", tu vi 1,1 lần | nhỏ | Mâu thuẫn |
| PB-30 | Đơn vị: canon ghi mm, kế hoạch dùng u | nhỏ | Mâu thuẫn |
| PB-31 | `hintUsed` của Minh lần hai; Văn Khí đếm theo lần gõ hay theo từ; sự kiện Voice | nhỏ | Học |
| PB-32 | Công bằng 15 và 90 WPM ở Dưỡng, Chân Nguyên, ưu tiên ô 4 | nhỏ | Công bằng |
| PB-33 | Chấp Ảnh không có đường giải không gõ; Trận Quyết, Chấp Ảnh ngoài trần chữ sống | nhỏ (M1) | Học |
| PB-34 | VAT: lý lẽ sai số, bố cục kết cấu, impostor 4 pha, bench E, kiếm đồng đội | nhỏ | 3D |
| PB-35 | Đo: bộ nhớ JS, draw call hậu kỳ, phím tới đòn, tông màu, `StageTier` | nhỏ | Đo |
| PB-36 | Chồng việc giữa làn; Làn 1 quá ít ngày | nhỏ | Khả thi |
| PB-37 | Lặt vặt: "triều 300 con", HC7 ≥ 90 %, chốt M0a khi B9 còn mở | nhỏ | Mâu thuẫn |

## 3. Ba chỗ chặn

### PB-01 · Ranh giới `local` và sim chưa khép · **chặn**

- **Bằng chứng:** canon §9.1 ("Vị trí, Sinh lực và **đồ nhặt** của chính mình do máy mình giữ… Thế giới chung không giữ vị trí người thật; mọi tác động của người chơi lên thế giới đi qua lệnh có `origin`"); canon §12.1 ô 3 ("chặn 3 lần trúng … vào mình **hoặc vào bot, điểm nhãn trong 2 m**; **đứng trên vạch** đòn lớn thì đỡ một nửa"); canon §10.5 P2 cách (c) ("Hộ thân rồi đứng trên vạch: Trận Lực chỉ mất một nửa"); canon §9.3 và §14.2 ("Linh Sa và Thú Hạch ghi sổ ngay tick thú chết" trong sim); canon §12.3 (Hồi Xuân Đan, Kim Thân Phù tác động lên Sinh lực); kế hoạch §5 (`guardAt(world, seat)` của Làn 4, Làn 5 dùng để "đỡ một nửa", `local` dùng để "chặn đòn"); kế hoạch §4 (Làn 4 giữ `src/sim/consumables.ts`, Làn 2 giữ `local/zones.ts` "khiên, Hộ thân").
- **Vì sao hỏng:** "đứng trên vạch lúc chạm" và "nhãn nằm trong 2 m của người" là vị trí người thật **ở tick chạm**, mà sim không có. `origin` của lệnh phím là vị trí lúc gõ xong, có thể trước tick chạm tới 5 s. Hai làn sẽ cài hai cách khác nhau (Làn 4 lấy `origin` lúc cast, Làn 2 lấy vị trí thật), và replay đội ở M3 sẽ lệch băm. "Đồ nhặt" ở §9.1 lại mâu thuẫn với Linh Sa ghi sổ trong sim. Đan hồi Sinh lực nằm trong sim nhưng Sinh lực nằm ở `local`.
- **Sửa (ghi vào canon §9.1, §12.1, §10.5 và kế hoạch §5):**
  1. Đổi "đồ nhặt" ở §9.1 thành "Sinh lực, khiên, trạng thái gục của chính mình". Ví Linh Sa, Thú Hạch, loot là **thế giới** (sim, theo ghế), đúng với §19.1 loot tất định.
  2. Hộ thân tạo **một vật thế giới** `ward{seat, origin, r 2 m, đến tick, còn 3 lần}` tại `origin` của Cast, đứng yên 5 s (như điểm khiêu khích của Thổ thể). Tác dụng lên thế giới tính từ `ward`: đỡ đòn vào bot, điểm nhãn nằm trong vòng; Thiết Bối Xung mất một nửa nếu vòng `ward` cắt vạch ở tick chạm. Tác dụng lên chính mình do `local` tính khi người đứng trong vòng. Đổi `guardAt` thành `wardAt(world, seat)` trả `origin`, bán kính, số lần còn.
  3. Đan, phù: lệnh `consumable` vào sim (số viên, hồi chung, Linh Sa); sim phát sự kiện `consumable{seat, kind}`; tác dụng lên mình (hồi, khiên) do `local/consumables.ts` (Làn 2) áp; tác dụng lên thế giới (Lôi Hỏa Phù, Định Thân Phù) do Làn 4 áp.
  4. Golden và `ic-replay` so cả `hashWorld` và `hashLocal(local)` (mỗi 600 tick và cuối trận).

### PB-02 · Khởi đầu lạnh và từ lấp chỗ của `deck.ts` · **chặn**

- **Bằng chứng:** kế hoạch §6.3 bước 1 ("`typing/deck.ts` (Source: `games/dragon-hold/src/typing/deck.ts`)"); `games/dragon-hold/src/typing/deck.ts` dòng 89–92 (hồ sơ trống: 50 từ đầu cấp được gắn nhóm `"known"`) và dòng 101–105 (lấp chỗ: `add(candidate, candidate.isNew ? "learning" : groupOf(candidate))`); canon §6.3 ("Ô gấp (không bao giờ nhận từ mới): ô 1, ô 3, ô 5, Ấn, Tẩy…"), §6.4 ("Từ mới chỉ ở Học trước, Tĩnh Tu, Chiêu B"), HC1.
- **Vì sao hỏng:** trận đầu của mọi người mới (và mọi trận M0a hộp xám, vì không có lõi học) là hồ sơ trống. Khi đó 50 từ chưa từng gặp mang nhãn "đã thuộc" và đi thẳng lên ô 1, ô 3, Ấn, Tẩy. Ở hồ sơ có dữ liệu, mọi từ chưa có bản ghi dùng để lấp bộ 70–100 từ mang nhãn "đang học" và lên ô 2, ô 4 ngoài sổ cái từ mới. HC1 đếm theo **nhãn** nên vẫn ra 0. Đây là đúng lỗi C1 mà `08` xếp **chặn**, nay quay lại qua mã chép.
- **Sửa:**
  1. Canon §17 thêm mục "Khởi đầu lạnh": hồ sơ trống thì trận dạy 1 dùng **từ nền**: tối đa 40 từ tần suất cao nhất của cấp **thấp hơn** cấp hồ sơ một bậc (cấp 1 thì lấy 40 từ đầu của danh sách A1), gắn cờ `assumed: true`, chỉ cho ô 1, ô 3, Tẩy. Mọi từ khác chưa có bản ghi là **từ mới** và đi qua sổ cái.
  2. Khi chép `deck.ts`: bỏ nhánh `candidate.isNew ? "learning"`; nhóm thiếu thì thu nhỏ bộ từ (sàn 40 từ) và cho `WordPicker` lặp lại sớm hơn, không đổi nhãn. Ghi vào `docs/SYNC_DEBT.md` là chỗ cố ý khác Rồng.
  3. HC1 đếm theo **bản ghi**: "từ không có bản ghi học trước trận và không thuộc danh sách từ nền" xuất hiện trên ô gấp = lỗi. Báo cáo in số lần dùng từ nền.

### PB-03 · Thang lùi HN0 không theo phần trượt · **chặn** cho Làn 1

- **Bằng chứng:** canon D03 ("Phần nào trượt ngân sách (nhiều khả năng là đám đông) xuống impostor 2D…; phần còn lại giữ 3D"); tin của anh 25/10 ("skill vạn kiếm quy tông triển khai rất nhiều kiếm, nếu đo được vẫn ổn khi là 3D thì cứ triển khai"); canon §20.3 bảng nấc (L1 VFX trang trí → **L2 hạ số kiếm 500 → 300 → 150 → 80** → L3 bầy impostor → L4 → L5).
- **Vì sao hỏng:** thang chạy theo thứ tự cố định, không theo phần nào trượt. Nếu đám đông là phần nặng (đúng như D03 dự đoán), L2 vẫn cắt kiếm xuống 300 rồi 150 trước khi thử impostor cho bầy. Kết quả trái chữ của anh: phần không trượt (kiếm) bị hạ. Canon cũng không có cách quy chi phí cho từng phần, nên Làn 1 không biết phần nào trượt.
- **Sửa (thay bảng nấc ở canon §20.3):**
  1. **Quy chi phí:** đo thêm ca **0 `base`** (sân, camera, hậu kỳ, không thú). Chi phí đám đông = p95(B) − p95(0); kiếm và VFX = p95(C) − p95(B); có xương = p95(E) − p95(C). Ghi cả CPU p95 cho từng hiệu.
  2. **Ngân sách con (số thử, khung p95 trên Dell):** High 12 ms = nền ≤ 2 + đám đông ≤ 5 + kiếm, VFX, số ≤ 3,5 + có xương ≤ 1,5. Medium 10 ms = 2 + 4 + 2,5 + 1,5. Low 8 ms = 1,5 + 3 + 2 + 1,5.
  3. **Lùi theo phần vượt:** phần nào vượt ngân sách con thì đi thang **của chính nó** trước: đám đông theo L3 → L4 → L5; kiếm theo L1 → L2; có xương theo LOD rồi giảm số `SkinnedMesh` dự phòng. Chỉ khi không phần nào vượt mà tổng vẫn trượt thì đi đám đông trước (đúng dự đoán của D03), rồi L1, cuối cùng mới L2.
  4. Ghi vào §20.4 cột "phần vượt" và hiệu từng phần, để anh thấy vì sao một phần xuống 2D.

## 4. Số không cùng đứng được

### PB-04 · Thời lượng trận vượt trần của đánh giá · lớn

- **Bằng chứng:** đánh giá §3.1 ("Đại Triều … ≤ 12 phút ở 35 WPM"), câu 8 ("trận ≤ 7 phút ở Thư giãn"); canon §4.1 bảng loại trận, nghỉ 20 s ở Cân bằng, báo đợt 5 s, bày trận 20 s; §10.5 Vương t 150 s; §15.3 Thiên Kiếp 60–90 s; canon §18.4 không có cổng thời lượng (Rồng có G17 "Thời lượng", `dragon-lane/00-canon.md` §7).
- **Tính lại (35 WPM, k = 1, không tính bảng mở):**
  - Đại Triều: 20 + 8 × 5 + 8 × (45–60) + 7 × 20 + 8 + 150 + (60–90) = **778–928 s = 13,0–15,5 phút** > 12.
  - Trận trộn: 20 + 6 × 5 + 6 × (45–60) + 5 × 20 = 420–510 s = **7,0–8,5 phút**, bảng ghi 6–7.
  - Trận trộn ở Thư giãn với bot Trẻ em (k 0,75, giờ đợt × 1,33; nghỉ bấm Enter sau ~15 s): 20 + 30 + 6 × (45–60) × 1,33 + 5 × 15 = 485–605 s = **8,1–10,1 phút** > 7.
  - Ải M0a: 20 + 30 + 305 + 100 + 8 + 150 = 613 s = 10,2 phút (bảng ghi 9–10, chấp nhận được).
- **Sửa:**
  1. Đại Triều: **7 đợt × 40–50 s**, nghỉ trong Đại Triều 15 s (Cân bằng), Vương t đích **120 s** (W_Vương = round(0,7 × D_đơn × 120 / 60)). Tính lại: 20 + 35 + 280–350 + 90 + 8 + 120 + 60–90 = 613–713 s = **10,2–11,9 phút**. Hồ sơ trẻ em giữ bản 6 đợt.
  2. Trận trộn: **6 đợt × 40–45 s** (390–420 s = 6,5–7,0 phút). Ở Thư giãn bớt một đợt (5 đợt): 20 + 25 + 5 × 42,5 × 1,33 + 4 × 15 = 388 s = 6,5 phút.
  3. Thêm cổng **CB9 Thời lượng** (nguồn: Rồng G17): bot Chuẩn ở Cân bằng nằm trong cột "thời lượng đích" của §4.1; bot Trẻ em ở Thư giãn ≤ 7 phút mỗi trận dạy và trận trộn; Đại Triều ≤ 12 phút với bot Chuẩn. Đo không tính thời gian bảng mở.
  4. Hệ quả cho tu vi: chương còn 15 + 12 + 7 = 34 đợt; xem PB-29.

### PB-05 · Ô 1 là 30 % sát thương gõ, không phải 20 % · lớn

- **Bằng chứng:** canon §12.1 ("Ước ở 35 WPM (D_ref): ô 1 ~14 W/phút (~20 % sát thương gõ, dưới trần CB3 30 %), ô 2 ~14, ô 4 ~11, tuyệt kỹ ~8"); §7.4 ("gõ ~47"); CB3 (ô 1 ≤ 30 % sát thương gõ ở **mọi bot Mới → Nhanh**).
- **Vì sao hỏng:** 14 / 47 = **29,8 %**, nằm trên mép CB3 ngay ở bot Chuẩn. Ô 2 (8 s) và ô 4 (12 s) bị hồi chiêu chặn, còn ô 1 hồi 0, nên mọi từ dư của người nhanh đổ vào ô 1. Ở 70 WPM (C ≈ 31,8 từ/phút: E_eff = 70 × 0,976 × 0,925 = 63,2; ℓ̄ 5,5) ô 1 nhận khoảng 18 từ/phút, gần gấp đôi ở bot Chuẩn, trong khi ô 2, ô 4 gần như đứng yên. Với số ước của chính canon, CB3 sẽ trượt ở bot Khá và Nhanh. Canon cũng không nói bot chọn ô theo thứ tự nào, nên số ước không kiểm được.
- **Sửa:**
  1. Sửa câu §12.1 và chia lại D_ref gõ cho đúng đích ~20 %: **ô 1 ~10 W/phút** (~8 từ/phút × ~1,2 W), **ô 2 ~18**, ô 4 ~11, tuyệt kỹ ~8 (cộng 47).
  2. Ghi **chính sách chọn ô của bot** vào canon §18.3: Tẩy → Ấn → ô 5 → ô 2 → ô 4 → ô 3 (khi có đòn báo trúng mình) → ô 1. Bot "Vừa" bỏ ô đã sẵn 1–2 s ngẫu nhiên theo seed, bot "Tốt" không bỏ.
  3. Làn 7 in phần ô 1 theo từng bot ngay vòng đầu. Nếu Khá, Nhanh vượt 30 %: hạ sát thương kiếm ô 1 (xem PB-06 về bất biến) hoặc tăng sức ô 2, ô 4 trước khi tăng tải.

### PB-06 · "Một từ ô 1 hạ Phong Lang" ra 0,999 W · lớn

- **Bằng chứng:** canon §10.2 ("Thú Nhỏ 1 W chết với một từ ô 1 không Ẩu (3 kiếm × 0,37 W × 0,90 = 1,0 W)"; "Thú bầy chết với một kiếm … (0,37 W × 0,90 ≥ 0,33 W)"); §7.1 ("Sim lưu số nguyên… W × 100 (`w100`)"; máu = W × 90 × g(K)); §12.1 Tích Kiếm ("Đợt 1: −8 % sát thương chiêu").
- **Vì sao hỏng:** 3 × 0,37 × 0,90 = **0,999 W < 1,0 W**. Tính bằng máu: Phong Lang 90 máu; một kiếm 0,37 × 90 = 33,3 → × 0,9 = 29,97; làm tròn xuống thì 29 × 3 = 87 < 90 (sống), làm tròn gần nhất thì 30 × 3 = 90 (chết). Bất biến phụ thuộc cách làm tròn mà canon không ghi. Tích Kiếm ở đợt 1: 29,97 × 0,92 = 27,6 → 3 kiếm 82,7 < 90, bất biến gãy dù làm tròn kiểu gì. Thạch Thử 0,33 W = 29,7 máu: cùng chuyện ở biên.
- **Sửa:**
  1. Ghi vào §7.1: máu thú lưu **số nguyên máu** = round(W × 90 × g(K) × hệ số preset); sát thương tính bằng máu với `mulDiv` làm tròn nửa lên sau mỗi hệ số (thứ tự ở PB-24). Bỏ cách ghi `w100` trong trạng thái (chỉ dùng trong dữ liệu).
  2. Ô 1: sát thương **một từ** = P × M_q × … tính một lần rồi chia 3 kiếm, phần dư vào kiếm cuối. Một từ Vừa ở K0 = 100 × 0,9 = 90 máu, đúng bằng Phong Lang.
  3. Bất biến ghi rõ phạm vi: "không tâm pháp R, không khắc hệ ×0,80". Test của Làn 4: `tests/sim/combat-kill-invariants.test.ts` kiểm hai bất biến ở Thư giãn, Cân bằng, Thử thách (bầy và Nhỏ không nhân preset).

### PB-07 · Quỹ học 15 % nhỏ hơn thưởng học cố định · lớn

- **Bằng chứng:** canon §14.2 ("học 15 % (Học trước +5 mỗi từ, tối đa +40; Thẻ Ôn +10 mỗi câu đúng, tối đa 3 câu mỗi lần nghỉ)"; "Ví dụ ải M0a: 200 + 1.125 = 1.325"); §17 Thẻ Ôn "+10 Linh Sa"; KT4 ("hơn 10–15 %, không bao giờ > 15 %"); kế hoạch §6.4 nghiệm thu ("Linh Sa ải M0a đúng **1.325**").
- **Vì sao hỏng:** ải M0a: quỹ học = 0,15 × 1.125 = 168,75, nhưng trần thật = 5 lần nghỉ × 3 × 10 + 40 = **190**, nên tổng tối đa là 1.346, không phải 1.325. Trận dạy một cổng (f = 0,6): quỹ học 81, trần thật 4 × 30 + 40 = **160**; bot làm đủ học hơn bot bỏ qua 160 / (200 + 459) = **24 %**, vượt trần 15 % của KT4.
- **Sửa:** thưởng học tính từ quỹ, không cố định: Thẻ Ôn mỗi câu đúng = round(0,15 × 900 × f × 0,8 / (3 × số lần nghỉ)); Học trước mỗi từ = round(0,15 × 900 × f × 0,2 / 8). Ải M0a: Thẻ Ôn 9, Học trước 4 (tổng 135 + 32 = 167). Trận dạy một cổng: Thẻ Ôn 5, Học trước 2 (tổng 60 + 16 = 76). Khi đó KT4 đúng theo cấu tạo (M0a +14,4 %; trận dạy +11,5 %) và test "đúng 1.325" đúng với sai số làm tròn ≤ 3. Sửa cùng câu ở §17 ("Đúng: +10 Linh Sa" → "theo §14.2").

### PB-08 · Sân và tốc thú không cho 8–12 s tới Kết Giới · lớn

- **Bằng chứng:** canon §8.1 ("Sân 40 × 26 m. Trận Tâm cách mép sau ~8 m. Hai cổng … cách Trận Tâm ~20 m theo đường đi; đường trời vào từ mép trên. Thú Nhỏ đi từ cổng tới mép Kết Giới trong **8–12 s**"); §10.2 (Phong Lang 1,4 m/s, Hỏa Nha 2,0 m/s, cả hai là bậc Nhỏ); §10.3 Cuồng +30 % tốc; §10.4 hào quang tướng +15 %; kế hoạch §6.2 nghiệm thu ("Thú Nhỏ đi từ cổng tới mép Kết Giới trong 8–12 s ở k = 1 (test)").
- **Tính lại:** Phong Lang: (20 − 9) / 1,4 = **7,9 s**; Cuồng 6,0 s; trong hào quang tướng 6,8 s. Hỏa Nha vào từ mép trên, cách Trận Tâm 26 − 8 = 18 m: (18 − 9) / 2,0 = **4,5 s**. Test nghiệm thu của Làn 2 sẽ đỏ ngay.
- **Sửa (canon §8.1, dữ liệu `stage-m0a.ts`):** đặt Trận Tâm ở gốc; cổng đất ở **(±15 m; −18 m)**, đường đi ~24 m (Phong Lang tới mép Kết Giới 15 / 1,4 = 10,7 s; Cuồng 8,2 s; Thạch Thử 9,4 s); đường trời vào từ hai **góc trên (±20 m; −18 m)**, bay thẳng 26,9 m (Hỏa Nha 17,9 / 2,0 = 9,0 s). Test của Làn 2 viết theo từng loài: Phong Lang và Hỏa Nha 8–12 s ở k = 1; thú Cuồng và trong hào quang ≥ 6 s (ghi là ngoại lệ có chủ ý).

### PB-09 · Thú gọi thêm không vào máu đợt; đợt 5 vượt dải · lớn

- **Bằng chứng:** canon §13.1 ("Đợt giữa 0,75–1,00"; "Đợt cuối 1,05–1,25, đỉnh ≤ 1,30"; "Lọc giải tích … máu đợt tính bằng công thức"); §13.3 (đợt 5 L **1,05**, 72 W; đợt 4 và 6 có Lang Đầu Đàn); §10.4 (Tru Đàn gọi 3 Phong Lang, tối đa 1 lần mỗi 20 s); §10.5 (Gọi Đàn: 1 cụm Thạch Thử + 2 Phong Lang mỗi 20 s ở P1, mỗi 12 s ở P3).
- **Vì sao hỏng:** đợt 5 không phải đợt cuối mà L = 1,05 > 1,00. Tru Đàn thêm tới 6 W ở đợt 4 (55 s, 2 lần) và 9 W ở đợt 6 (60 s, 3 lần): L thật 1,04 và **1,27** (> trần dải 1,25). Gọi Đàn của Vương thêm 4,31 W mỗi lần; trong ~150 s có 3 lần ở P1 (~60 s) và 3–4 lần ở P3 (~45 s), tức **26–30 W** (thêm 2 lần nếu P2 cũng gọi), bằng +32–38 % so với 80 W máu Vương, không nằm trong công thức W_Vương. Thú gọi thêm cũng chiếm suất của trần 60 thú sống.
- **Sửa:** (1) đợt 5 hạ về L 1,00 = 68,75 W (bỏ 1 Nham Viên và 1 Phong Lang: 68,6 W, 92 con). (2) Canon §13.1: "Máu đợt gồm W gọi tối đa của mọi thú triệu hồi trong đợt; thành phần gốc giảm tương ứng; lọc giải tích tính cả phần gọi." (3) §10.5: W_Vương tính trên D_đơn; thêm dòng "tải phụ của Gọi Đàn ≤ 30 % W_Vương" và giảm nhịp gọi (P1 mỗi 30 s, P3 mỗi 18 s) để đứng trong số đó. (4) Gọi chỉ khi trần thú sống còn chỗ; không thì bỏ lượt gọi, không xếp hàng.

## 5. Hại việc học, công bằng tốc độ, Voice

### PB-10 · Sổ cái từ mới chưa viết được như ghi · lớn

- **Bằng chứng:** canon §6.4 ("≤ 8 từ mới cho mỗi 20 phút … Sổ cái ở khóa `immortality-cultivation.newwords` (kit `safe-storage`)… Khi hồ sơ có > 80 từ đến hạn, từ mới mỗi trận ≤ 4"); kế hoạch §3.1 (`src/typing` thuần: không `window`, `Date`…), §5 (`budgetLedger(storage)`: `canTake`, `take`, `remaining`, ở `src/typing/budget-ledger.ts`); `games/dragon-hold/tests/boundary.test.ts` dòng 46 (cấm `Date`, `localStorage`, `globalThis`, và theo chuỗi import cấm cả `kit/platform/safe-storage.ts`); `shared/game-kit/typing/budget.ts` (kit đã có lớp `BudgetLedger`, nghĩa là **trần chữ sống**).
- **Vì sao hỏng:** cửa sổ 20 phút cần đồng hồ tường, lưu cần `localStorage`, cả hai bị test ranh giới chép từ Rồng chặn trong `src/typing`. Tên `budgetLedger` trùng nghĩa với `BudgetLedger` của kit. Canon không nói: một từ gặp ở Học trước rồi ở ô 4 tính một hay hai lần; "phiên chơi" là gì; Tĩnh Tu cần 6 từ một lúc mà sổ chỉ còn 3 thì sao; trận lấy số còn lại lúc nào. Nếu trận đọc sổ trong lúc chạy, replay và golden không tất định.
- **Sửa:**
  1. Tên và chỗ: `src/typing/new-word-ledger.ts`, kiểu `NewWordLedger`, **thuần**: `createNewWordLedger(snapshot: { v: 1; entries: { wordId: string; firstSeenMs: number; channel: "learn-ahead" | "tinh-tu" | "slot4" }[] })`, `remaining(nowMs)`, `take(wordId, nowMs, channel)`. Đọc, ghi `localStorage` ở `src/app/storage.ts` (Tích hợp) qua `safe-storage`.
  2. Nghĩa: cửa sổ **trượt 20 phút** theo `firstSeenMs`; một từ tính **một lần** ở lần gặp đầu, kênh nào cũng vậy (Học trước rồi ô 4 = 1); `take` lặp lại cùng `wordId` không trừ thêm. Bỏ khái niệm "phiên chơi".
  3. Trận: lúc nạp trận lấy `remaining` một lần, ghi vào đầu replay (`newWordAllowance`); sim chỉ dùng số đó. Khi > 80 từ đến hạn, `newWordAllowance = min(remaining, 4)`.
  4. Tĩnh Tu: còn < 6 thì không mở bài mới; Tĩnh Thất hiện "còn N phút nữa đủ 6 từ" và cho phiên ôn (chỉ Thường). Không bao giờ dạy nửa bài.

### PB-11 · Từ mới trong trận chỉ gặp một lần · lớn

- **Bằng chứng:** canon §6.3 ô 4 (từ mới chỉ ở đợt 1–2), §17 ("Không lặp từ tới khi dùng hết nhóm (kit `WordPicker`)"; "Một sự kiện có chấm cho mỗi từ mỗi trận"); Rồng `00-canon.md` §7 G12 ("mỗi từ mới gặp ≥ 2 lần"); canon §18.4 không có cổng tương ứng.
- **Vì sao hỏng:** bộ trận 70–100 từ, bot Chuẩn gõ ~120 từ một trận. Một từ mới lên ô 4 ở đợt 1 rồi về nhóm "đang học"; `WordPicker` không trả lại nó tới khi dùng hết nhóm, nên nhiều từ mới chỉ gặp **một lần** trong trận, đúng chỗ học yếu nhất. Thẻ Ôn chỉ chọn 3 câu mỗi lần nghỉ và có thể bị tắt.
- **Sửa:** canon §6.4 thêm: "Mỗi từ mới của trận gặp **≥ 3 lần**: Học trước (nếu làm) hoặc lần đầu ở ô 4; rồi ≥ 2 lần nữa ở ô 2 hoặc ô 4 với nhãn đang học, cách nhau ≥ 45 s, hết trước đợt 4." `WordPicker` ưu tiên trả từ mới của trận cho ô 2, ô 4. Thêm **HC8** (M0a): "mỗi từ mới gặp ≥ 3 lần trong trận ở 100 % lượt bot Chuẩn, ≥ 2 lần ở bot Trẻ em" (nguồn: Rồng G12).

### PB-12 · Tĩnh Tu cho lĩnh ngộ khi không gõ · lớn

- **Bằng chứng:** canon §16 ("điểm phiên = `clamp(40 + 5 × Minh + 2 × Thường − 3 × chọn nhầm ; 40 ; 100)`, cộng dồn qua phiên; 100 là lĩnh ngộ. Hoàn thành phiên luôn cho ≥ 40"); đánh giá §3.6 ("hoàn thành phiên luôn cho ≥ 40 % tiến độ"); lĩnh ngộ cho +8 % chiêu, +5 Văn Khí, +5 tu vi (§15.6, §14.1, §15.2).
- **Vì sao hỏng:** ba phiên 60 s không bấm phím nào: 40 + 40 + 40 = 120 ≥ 100 → lĩnh ngộ. Thưởng học (Văn Khí, tu vi) đến mà không học. Sàn 40 cũng xóa phạt "chọn nhầm" cho người gõ bừa mọi chữ.
- **Sửa (giữ chữ "≥ 40" của đánh giá, định nghĩa "hoàn thành"):** "Hoàn thành phiên = đã gõ xong mỗi từ trong 6 từ Minh **ít nhất một lần** trong phiên. Phiên hoàn thành: điểm như công thức. Phiên chưa hoàn thành: điểm = max(0; 5 × Minh + 2 × Thường − 3 × chọn nhầm), không sàn." Kiểm khả thi: 6 từ 4,5 chữ ở E 15 mất 6 × 5,1 = 31 s; bot Trẻ em (E_eff 10,9) mất 6 × 7,0 = 42 s; đều trong 60 s. Thêm **HC4b**: bot Không gõ không lĩnh ngộ sau 10 phiên; bot gõ mọi chữ (kể cả Tâm ma) cần ≥ 3 phiên.

### PB-13 · Tham Ngộ: Tâm ma không nhãn và Thường không phân biệt được · lớn

- **Bằng chứng:** canon §16 bảng (Thường: "Từ đến hạn ôn", nhận bằng "Giấy trơn"; Tâm ma: "từ nhóm chủ đề **xa** bài (khác nhóm trong 15 nhóm)"), bậc Tham Ngộ ("1/3 Tâm ma không nhãn; nhận theo việc từ có thuộc chủ đề bài không"); `08` C2 (chủ đề mơ hồ: 101 chủ đề, 835 khóa từ, phần lớn A1–A2).
- **Vì sao hỏng:** Tâm ma không nhãn trông như giấy trơn, tức như Thường. Người chơi phải đoán bằng chủ đề, nhưng Thường lấy từ **mọi** từ đến hạn, không chỉ chủ đề bài; một từ Thường thuộc chủ đề khác trông hệt Tâm ma. "Khác nhóm" cũng gồm nhóm sát bên. Gõ nhầm bị −3 điểm vì một phân biệt không làm được.
- **Sửa:** ở Tham Ngộ, (1) màn hiện tên nhóm chủ đề của bài; (2) Thường không nhãn chỉ lấy từ đến hạn **cùng nhóm** với bài; Thường khác nhóm giữ dấu riêng (viền nhạt và biểu tượng giọt mực) như ở Nhập Môn; (3) Tâm ma lấy từ nhóm cách bài ≥ 3 bậc trên bản đồ 15 nhóm (ghi bảng khoảng cách vào dữ liệu `src/tinh-tu/sim/topics.ts`); (4) bỏ khỏi cả Thường và Tâm ma mọi từ thuộc ≥ 2 nhóm. Thêm **HC6b**: bot Chuẩn ở Tham Ngộ có tỉ lệ chọn nhầm ≤ 10 % (bot đoán theo nhóm, có lỗi đọc theo `HumanTypist`).

### PB-14 · Trần đổi hồ sơ ±10 %/phiên hai chiều · lớn

- **Bằng chứng:** canon §6.5 ("`t_kỳ_vọng` … đổi **≤ 10 % mỗi phiên**. Ngưỡng Chớp có sàn ứng với E hồ sơ của 5 phiên gần nhất"); D18 ("chưa biết thì dùng 25 WPM và đo ở đợt 1"); §7.5 (k theo hồ sơ); BALANCE §2 (độ tin theo số mẫu, `blendSkill` trộn dần theo độ tin).
- **Vì sao hỏng:** người gõ 60 WPM chọn "chưa biết" bắt đầu ở 25. Lên tối đa 10 % mỗi phiên thì cần ln(60/25) / ln(1,1) ≈ **9,2 phiên** mới tới số thật. Suốt thời gian đó k bị kẹp 0,75 thay vì 1,30 và gần như mọi từ sạch là Chớp: game quá dễ, B1 trượt với người thật dù bot đạt. Người khai quá cao (chọn 60, gõ 25) cũng mắc kẹt ~9 phiên quá khó. Chống cố ý gõ chậm (`08` G5) chỉ cần chặn **chiều giảm**.
- **Sửa:** canon §6.5: "Trần ±10 % mỗi phiên chỉ áp **chiều giảm**, và chỉ khi E có độ tin ≥ 60 từ đo được qua ≥ 3 phiên. Chiều tăng, và mọi chiều khi độ tin còn thấp, dùng `blendSkill` của kit không trần." Thêm: "Trận đầu của hồ sơ 'chưa biết': hết đợt 1, k của ghế tính lại từ số đo của đợt 1 (lệnh `pace-update` ghi vào replay, áp từ đợt 2)."

### PB-15 · Bàn Quyết lúc nghỉ và Cast `fizzled` · lớn

- **Bằng chứng:** canon §6.1 ("Không có đích hợp lệ: ô giữ trạng thái 'đã gõ' 3 s… hết 3 s thì Cast tắt, ô nhận từ kế ngay, không hồi. Sự kiện học của từ đó vẫn ghi"); §6.6 ("+5 mỗi từ Chớp hoặc Hoàn hảo… Thanh giữ qua nghỉ đợt"); §8.2 Tâm nhãn Dưỡng ("khi người chơi gõ xong một từ trong 3 s gần nhất"); §14.1 Văn Khí ("từ đến hạn gõ đúng +1"). Không mục nào nói Bàn Quyết có sống lúc bày trận và nghỉ không.
- **Vì sao hỏng:** nếu ô 1 sống lúc nghỉ, người chơi gõ ô 1 không đích để nạp đầy Chân Nguyên trước mỗi đợt (tuyệt kỹ ngay giây đầu), hồi Trận Lực bằng Dưỡng, và nhận Văn Khí. Bot "Tốt" của Làn 7 sẽ tìm ra và làm méo mọi cổng.
- **Sửa:** canon §6.1: "Bàn Quyết chỉ sống từ lúc **báo đợt** tới hết đợt và trong pha Vương; lúc bày trận và nghỉ, ô hiện mờ, phím chữ đi vào bảng đang mở hoặc bị bỏ. Chân Nguyên, Dưỡng, điểm luyện công pháp chỉ tính cho Cast `resolved`; Cast `fizzled` chỉ ghi sự kiện học (vẫn một sự kiện có chấm mỗi từ mỗi trận)."

### PB-16 · Trận Quyết 8 s bỏ rơi người gõ chậm (M1) · lớn

- **Bằng chứng:** canon §8.4 ("Trận Quyết 2 từ của riêng mình, gõ trong 8 s. Sức = 40 % + 20 % cho mỗi người gõ xong"); §6.3 (Trận Quyết 3–6 chữ); §10.6 ("Áp cho **mọi đòn có đáp án gõ**"; T theo E_sàn); `08` D3 (người chậm không được thua cuộc đua).
- **Tính lại:** bot Trẻ em (E_eff 10,9): mỗi từ 4,5 chữ = 12 × 5,5 / (0,86 × 10,9) = 7,0 s, hai từ 14 s + nhận từ ≈ **15,8 s**; ngay cả E thô 15 cũng ~12 s. Ghế 15 WPM không bao giờ góp 20 % của mình; ở Lưỡng Nghi với hai người chậm, Hợp Trận chỉ còn 40 %.
- **Sửa:** Trận Quyết theo công thức T cho hai từ: `T₂ = 1,6 × (0,4 + 2 × (0,5 + 12 × (ℓ + 1) / (0,86 × E_sàn)) + 0,2)`, với ℓ = 4 (Trận Quyết đổi thành 3–4 chữ). Thư giãn 17,4 s; Cân bằng 11,5 s; Thử thách 8,9 s. Cửa sổ của mỗi ghế = max(8 s; T₂) / k_ghế. CB5 phủ cả Trận Quyết.

### PB-31 · `hintUsed` của Minh lần hai; Văn Khí; sự kiện Voice · nhỏ

- **Bằng chứng:** canon §16 ("Minh … mỗi từ ≥ 2 lần mỗi phiên; lần đầu luôn hiện nghĩa"; "Minh gõ xong → `review-card` kèm `hintUsed: true`"); §17 ("`hintUsed` = nghĩa hoặc IPA **đang hiện** lúc gõ"; "Lần nhớ đúng = … `review-card` **không** có `hintUsed`"); §14.1 Văn Khí; §6.1 `channel`; §17 bảng `activityType` không có cột kênh.
- **Vì sao hỏng:** Minh lần hai không hiện nghĩa, nên theo định nghĩa chung của §17 nó là `hintUsed: false`, tức **lần nhớ đúng**, chỉ vài giây sau thẻ Khẩu Quyết. Nghĩa trên Bàn Quyết sẽ ẩn quá sớm. Văn Khí "+1 mỗi từ đến hạn gõ đúng" không nói theo lần gõ hay theo từ, nên người nhanh gõ lặp nhiều lần hơn. Voice (M4) gửi `typing-skill` sẽ khai là luyện chính tả.
- **Sửa:** §17 thêm ngoại lệ "Tĩnh Tu Minh và Khẩu Quyết luôn `hintUsed: true`, mọi lần". Văn Khí "+1 cho mỗi **từ khác nhau** đến hạn, gõ đúng lần đầu trong trận". Sự kiện học có trường `channel`; Voice dùng `activityType` riêng do lõi học định nghĩa ở M4, không dùng `typing-*`.

### PB-32 · Công bằng 15 và 90 WPM ở Dưỡng, Chân Nguyên, ô 4 · nhỏ

- **Bằng chứng:** §8.2 Dưỡng (cửa sổ 3 s cố định); §6.6 (Chân Nguyên theo số từ, không theo k); §6.2 thứ tự ưu tiên Thư giãn và Học ("… ô 5 > ô 4"); §8.4 "cùng thời gian cho mọi tốc gõ" của nạp nhãn.
- **Vì sao hỏng:** bot Trẻ em gõ ~8 từ/phút, một từ mỗi 7,5 s, nên Dưỡng chỉ bật ~40 % thời gian; bot Chuẩn ~100 %. Chân Nguyên đầy sau ~3 phút ở bot Trẻ em, ~68 s ở Chuẩn, ~37 s ở 90 WPM: em nhỏ hiếm khi thấy "vạn kiếm", điểm nhấn của game. Ở Học (preset dành cho học), ô 4, ô duy nhất trong trận nhận từ mới, lại có ưu tiên thấp nhất. "Cùng thời gian cho mọi tốc gõ" của nạp nhãn chỉ đúng trong khoảng k không bị kẹp; bot Mới (k thô 0,69) và Trẻ em (0,41) đều bị kẹp ở 0,75.
- **Sửa:** Dưỡng: cửa sổ = 3 s / k_ghế. Chân Nguyên: +5/+3/+2 nhân 1 / k_ghế (làm tròn), để thời gian đầy bằng nhau trong khoảng kẹp. Ở Học, ô 4 đứng trước ô 5 trong thứ tự ưu tiên. Sửa câu §8.4 thành "cùng thời gian cho mọi tốc gõ trong khoảng k 0,75–1,30".

### PB-33 · Chấp Ảnh, Trận Quyết và trần chữ sống (M1) · nhỏ

- **Bằng chứng:** §15.3 (3–4 Chấp Ảnh đi chậm vào Trận Tâm, gõ xong là tan); `08` C3 sửa ("Mọi chữ bắt buộc phải có một đường giải không cần gõ"); §6.2 trần chữ sống (5 ô + 2 Ấn + 1 khẩn).
- **Sửa:** Chấp Ảnh nhận sát thương của chiêu vùng và cơ quan (máu 1 W mỗi bóng); tốc đi tính để thời gian tới Trận Tâm ≥ T của preset với ℓ = 7. Trong Thiên Kiếp và trong cửa sổ Trận Quyết, ô 2–5 tạm mờ (không là chữ sống), để Chấp Ảnh và Trận Quyết nằm trong trần 8 (5 ở Thư giãn).

## 6. Toàn vẹn cổng chung

### PB-17 · Nhàn I phụ thuộc vị trí và trùng P · lớn

- **Bằng chứng:** canon D14, §18.2 (I khi cả hai: "(a) không ô nào ngoài ô 1 có chữ sống…; (b) không thú nào trong 12 m quanh người chơi và không thú nào trong Kết Giới"); §18.2 P ("Trận Lực mất máu trong 2 s gần nhất"); §10.2 Nham Viên ("Dừng cách đích 12 m, ném mỗi 3 s"); §18.3 bot Cơ động ("đi để giữ cụm đông trong 12 m"); BALANCE §3 (I là "không có chữ nào để gõ **và** không có quyết định nào"), B1.
- **Vì sao hỏng:** (1) Điều kiện (b) đo theo chỗ người đứng, nên cùng một trận cho I khác nhau tùy bot đi hay đứng; bot Cơ động gần như được thiết kế để làm I về 0. Canon không nói 9 bot chuẩn của B1 đi theo chính sách nào. (2) Nham Viên đứng 12 m ném Trận Tâm thì tick đó vừa là P (Trận Lực mất máu) vừa có thể là I. I và P chồng nhau làm B1 khó đọc. Phần (a) là cách chặt hơn nghĩa chữ của BALANCE nên không nới dải; giữ.
- **Sửa:** §18.2: "I = (a) ∧ (b) ∧ **không phải P**; (b) tính **từ Trận Tâm**: không thú nào trong 12 m của Trận Tâm và không thú nào trong tầm ô 1 của người chơi." §18.3: "9 bot chuẩn của B1–B8 dùng chính sách đi **Đứng yên** (đứng ở Tâm nhãn); báo cáo in thêm I của bot Chuẩn Cơ động để so." Nham Viên dừng cách đích **11 m** để ô 1 với tới từ Trận Tâm, hoặc ghi rõ là cố ý.

### PB-18 · Cổng học chấm bằng bot mà bot không tạo sự kiện học · lớn

- **Bằng chứng:** canon §17 ("Chỉ người thật tạo sự kiện học; bot … thì không"); §18.3 ("Bot … không tạo sự kiện học"); BALANCE §7 B8 ("Cổng học riêng của game vẫn đạt ở **mọi bot**"); canon §18.4 HC1–HC3 (replay mọi bot), HC7 (bộ kiểm sự kiện); kế hoạch §7 (M0a chấm HC1–HC3 bằng Làn 7).
- **Vì sao hỏng:** nếu bot không tạo sự kiện, B8 và HC7 cho trận không có gì để chấm; HC7 hiện chỉ áp cho Tĩnh Tu. Lỗi `activityType`, `hintUsed`, "một sự kiện có chấm mỗi từ mỗi trận" trong trận chỉ bị bắt bằng test đơn vị.
- **Sửa:** §17: "Bot **không gửi** sự kiện học. Báo cáo bot chạy bộ dựng sự kiện ở chế độ nháp (`dryRun: true`, không bao giờ gửi) để chấm cổng học." Mở rộng HC7 sang trận M0a: bot Chuẩn × 20 seed, 100 % sự kiện nháp đúng bảng `activityType` và luật `hintUsed`.

### PB-37 · Lặt vặt về cổng và lời văn · nhỏ

- §6.2 "Triều 300 con vẫn chỉ có ≤ 8 chữ" trái §13.3 (trần 60 ở M0a, 120 ở M1). Sửa: "kể cả khi trần thú sống lên 120".
- HC7 "≥ 90 % đúng luật" cho phép 10 % sự kiện sai vào lõi học **chung** của mọi game. Giữ số của đánh giá §6, thêm hai điều kiện cứng: 0 sự kiện `hintUsed: false` khi nghĩa đang hiện; 0 sự kiện có nguồn là bot.
- Kế hoạch §7 có B9 trong bảng cổng M0a nhưng canon §25 hoãn B9. Ghi rõ: "M0a chốt có điều kiện; B9 mở, chạy khi Rồng qua B9".

## 7. Khả thi: làn, mã có sẵn, repo cha, renderer 3D

### PB-19 · HN0 phải đo theo số thú mà luật dùng · lớn

- **Bằng chứng:** canon §13.3 ("Trần thú sống của luật: 60 ở M0a… đề xuất 120 ở M1 nếu HN0 đạt ở Low với 300 thú"); §20.3 (ca B, C, D, E đều 300 thú; thang lùi áp khi trượt); D03.
- **Vì sao hỏng:** game M0a không bao giờ vẽ quá 60 thú (M1: 120). Nếu 300 thú trượt ở Low, thang lùi đẩy đám đông xuống impostor ở **mọi** mức đông, kể cả 60 thú mà 3D đầy đủ có thể chạy tốt. Đó là bỏ 3D ở chỗ anh muốn giữ, chỉ vì một số thú game không dùng.
- **Sửa:** ca B, C, E chạy ở **N = 60, 120, 300**. Phán quyết mỗi bậc = N lớn nhất đạt ở 3D đầy đủ. Thang lùi (PB-03) chỉ áp khi **N của luật** (60 ở M0a, 120 ở M1) trượt; kết quả ở 300 chỉ ghi là dư địa (cho Thất Tinh, Triều Vô Tận). Bảng §20.4 thêm cột "N đạt 3D đầy đủ".

### PB-20 · Kit `feedback` phát âm tổng hợp; hồ sơ `tutien` cần sửa kit · lớn

- **Bằng chứng:** canon §21.1 ("qua bậc phản hồi T0–T5 của `kit/feedback` (thêm hồ sơ `tutien`)"); D26, §22 ("Không âm tổng hợp thuần"; "M0a: móc âm im lặng"); `shared/game-kit/feedback/audio-cues.ts` dòng 3 ("Combat sounds made in code") và dòng 137 (`new OscillatorNode`); `shared/game-kit/audio/dragon-voice.ts` (dòng 273, 317, 324: `createOscillator`); `shared/game-kit/feedback/profiles.ts` dòng 10 (`FeedbackProfileId = "ship" | "dragon" | "td"`); kế hoạch §6.6 bước 7 (test chặn `OscillatorNode` chỉ trong `src/audio`).
- **Vì sao hỏng:** nối `kit/feedback` theo mẫu của các game kia sẽ kéo `AudioCues` phát tiếng tổng hợp, trái Q6, mà test của Làn 6 không quét `src/kit/**`. Thêm hồ sơ `tutien` nghĩa là sửa `shared/game-kit` ở repo cha, chạy `kit:sync` lại cho cả 4 game và commit; không làn nào trong kế hoạch giữ việc này.
- **Sửa:** (1) Test ranh giới (bước 0) cấm import `kit/feedback/audio-cues` và `kit/audio/dragon-voice` từ mọi tệp của game. (2) M0a không sửa kit: hồ sơ phản hồi để cục bộ ở `src/view/feedback-profile.ts` (Làn 6), dùng `FeedbackProfile` với `id: "dragon"` làm khung rồi đè số, ghi vào `SYNC_DEBT.md`. (3) Đề xuất đưa hồ sơ `tutien` vào kit chỉ khi số đã ổn (M0b), như một việc riêng của repo cha.

### PB-21 · Kit `three` chưa có nhân vật đi bộ và hợp đồng model hợp · lớn (M0b; ca E của HN0)

- **Bằng chứng:** canon §20.3 ("Người, bot, thú tướng, Vương dùng `SkinnedMesh` thật như `Hero` của kit"), §21.2 ("kiểm theo `MODEL_CONTRACTS` của kit (`heroes`, `enemies`, `bosses`, `props`)"), §21.3 (clip Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory); `shared/game-kit/three/hero.ts` dòng 6 (`Locomotion = "idle" | "fly" | "boost"`), dòng 87 ("The flown character"), độ chúi theo bay; `shared/game-kit/three/model-contracts.ts` (`heroes.requiredClips: ["Hero_Fly"]`; `bosses.requiredClips: ["Boss_Idle_Hover"]`, ổ cắm `FX_HALO`).
- **Vì sao hỏng:** Kiếm tu đi bộ, Thú Vương là sói: không có `Hero_Fly`, không bay lơ lửng. Dùng nguyên hợp đồng kit thì model đúng sẽ bị báo thiếu clip; dùng `Hero` thì phải ánh xạ "fly" thành "run" và tắt độ chúi, tức dùng sai lớp.
- **Sửa:** viết cục bộ `src/view/walker-rig.ts` (Source: `kit/three/hero.ts`, chỉ lấy phần trộn clip và ổ cắm; locomotion `idle | run | dash`) và `src/content/model-contracts.ts` với các loại `cultivators` (clip bắt buộc Idle, Run, Cast_Short, Hit; 8.000–30.000 tam giác), `beasts` (Idle, Move, Attack, Death; 800–3.000 cho LOD VAT), `beast-kings` (12.000–45.000). Ca E của HN0 dùng `walker-rig` với khối tạm có xương. Đưa lên kit khi game thứ hai cần.

### PB-22 · Nối repo cha đã có; kế hoạch §2.3 cũ; test media đỏ · lớn

- **Bằng chứng (repo hiện tại):** đã có `portal/public/games.json` dòng 76–80; `portal/tests/learning-bridge.test.mjs` dòng 18, 30; `infra/nginx/typing-game.local.dev.conf` dòng 3, 304–330; `infra/nginx/typing-game.local.play.conf` dòng 3, 232–259; `scripts/setup-nginx.sh` dòng 48; `package.json` cha dòng 11 (`dev` có `dev:tutien:app`), 23 (`build:local`), 74–76; `dev.sh`; `play.sh` dòng 212, 337–347; `scripts/play.sh` dòng 27; `scripts/game-dir.sh` dòng 24; `scripts/bootstrap.sh`; `scripts/validate-play-mode.mjs` dòng 48–51; `scripts/validate-space-integration.mjs` dòng 65–68; `media/media.config.json` dòng 56–64; `AGENTS.md` dòng 33; `docs/AGENT_SKILLS_SETUP.md` dòng 99. Kế hoạch §2.3 vẫn ghi mọi dòng là "Thêm".
- **Đã chạy:** `node --test scripts/media/test/unit.test.mjs` (test "config: games[] keeps Space first…") **trượt**: dòng 464 so đúng 4 id, nay `media.config.json` có 5. `validate-space-integration` qua; `validate-play-mode` qua, kèm cảnh báo "games/immortality-cultivation is not checked out yet".
- **Thêm:** `docs/games/SPLIT_PLAN.md` chưa nhắc 3008 hay game thứ tư (§10 dòng "Cổng đang dùng"). `dev:tutien:app` của repo cha truyền `--host 127.0.0.1 --port 3008 --strictPort` cho `pnpm dev`, trong khi kế hoạch §2.1 cũng đặt các cờ đó vào `dev` của game; các game khác chỉ đặt ở game (`dev:dragon:app` gọi `pnpm dev` trơn). Cờ lặp làm trình đọc cờ của Vite nhận mảng cho `--port`.
- **Sửa:** kế hoạch §2.3 đổi thành "đã có, chỉ kiểm" cho mọi dòng trên. Việc còn lại: (1) sửa `scripts/media/test/unit.test.mjs` dòng 464 (thêm `'immortality-cultivation'`) và vòng lặp dòng 479, chạy lại `node --test scripts/media/test/unit.test.mjs`; (2) SPLIT_PLAN §10: thêm 3008 vào dòng cổng và một mục ngắn "Game thứ tư"; (3) bỏ cờ cổng khỏi `dev:tutien:app` cho giống `dev:dragon:app` (cờ chỉ ở `package.json` của game); (4) nghiệm thu bước 0 thêm: `validate-play-mode` qua **không còn** cảnh báo "not checked out".

### PB-36 · Chồng việc giữa làn; Làn 1 quá ít ngày · nhỏ

- **Bằng chứng:** kế hoạch §4 (Làn 1 `hitfx.ts`: "số sát thương bằng `NumberField` … khói mực tạm khi chết"; Làn 6 `numbers.ts`, `fx.ts`: "lóe trúng, khói mực tạm…, số sát thương bằng `NumberField`"); Làn 7 giữ `scripts/visual/scenarios/lib/**` mà `ic-bench.mjs` (Làn 1) cần; mọi làn thêm trạng thái vào `World` qua `world.ts` của Làn 2; §1 Làn 1 "3–5 ngày" cho renderer, đám đông 3 kiểu vẽ, VAT, impostor, kiếm, vệt, VFX, bench 6 ca × 3 bậc × 3 N × 3 lượt, `bake_vat.py`, lượt GLB (Rồng: `bench.ts` 41 KB, `crowd.ts` 39 KB).
- **Sửa:** số sát thương và khói mực chỉ ở Làn 1 (`hitfx.ts` xuất `createDamageNumbers`, `createInkSmoke`); Làn 6 chỉ nối. `ic-bench.mjs` tự chứa (không import `lib/**`). Bước 0 khai sẵn **mọi trường trạng thái** của `World` theo canon (thú, chữ, Cast, `ward`, nhãn, cơ quan, ví, Thế, báo đòn), mỗi làn chỉ điền hàm khởi tạo và băm của phần mình. Làn 1 giao **mốc 1a sau 2 ngày**: `createRenderer`, `Projector`, `createCrowd(…, "procedural")` cho Làn 6; mốc 1b (VAT, impostor, kiếm, bench) 6–8 ngày.

### PB-34 · VAT, impostor, bench E, kiếm đồng đội · nhỏ

- **Bằng chứng:** canon §20.3 ("VAT: mỗi đỉnh chỉ 1–2 lần đọc kết cấu (bones cần 4 ma trận, 12–16 lần đọc)"; "nội suy giữa hai khung và trộn hai clip"; "~1.800 đỉnh × 135 khung"); kế hoạch §6.1 bước 3 ("hàng = khung, cột = đỉnh") và nghiệm thu ("chỉ số texel VAT (`khung × rộng + đỉnh`)"); §20.3 ca D (impostor 16 hướng × **4 pha**); ca E (6 `SkinnedMesh`) so với §20.2 (High ≤ 8, Thất Tinh 10); §20.2 hệ số VFX đồng đội.
- **Vì sao hỏng và sửa:**
  - Nội suy hai khung × hai kết cấu (vị trí, pháp tuyến) = 4 lần đọc; trộn hai clip = 8. Lợi thật của VAT là **CPU**: không phải tính ma trận xương cho 300 instance mỗi khung (300 × ~25 xương × 64 byte ≈ 480 KB tải lên mỗi khung). Sửa câu lý lẽ; quyết định VAT giữ nguyên.
  - "Cột = đỉnh" vượt `MAX_TEXTURE_SIZE` tối thiểu của WebGL2 (2048) khi mesh 3.000 tam giác có > 2.048 đỉnh sau khi tách đường may UV. Dùng bố cục quấn: texel = khung × số đỉnh + đỉnh, rộng 1.024 hoặc 2.048; khớp với công thức test.
  - Impostor 4 pha một chu kỳ đi là chuyển động giật, trái luật "không chuyển động cứng" của anh. Dùng **8 pha** và trộn mờ giữa hai pha kề. Bộ nhớ ở Low: 16 × 8 × 128² × 4 B = 8,4 MB mỗi loài, 5 loài 42 MB, vẫn dưới 64 MB. Khi đổi một thú giữa VAT và impostor (L4), có trễ: chỉ đổi sau 1 s ở phía bên kia ngưỡng, trộn 0,2 s.
  - Ca E chạy số `SkinnedMesh` bằng trần của bậc (Low, Medium 6; High 8) và một lượt 10 cho Thất Tinh; khối tạm có xương ghi số tam giác (người 15.000, Vương 45.000) và số xương.
  - "Vạn kiếm" của đồng đội: đặt **một bể kiếm chung** bằng số của bậc (150/300/500); chiêu của đồng đội lấy từ bể theo hệ số 0,4–0,6, không cộng thêm.

### PB-35 · Đo và renderer · nhỏ

- **Bằng chứng:** kế hoạch §6.1 nghiệm thu (`performance.memory.usedJSHeapSize` tăng ≤ 2 MB trong 10 s); §20.2 ("Draw call ≤ 80 / 110 / 150"; "Phím tới đòn ≤ 50 ms"); §21.1 (`NeutralToneMapping`, `TT_TIERS`); `shared/game-kit/three/stage.ts` dòng 12 (`StageTier = { dpr, particles, bloom, tipsPerSide, trail }`), dòng 88 (`ACESFilmicToneMapping` cố định), dòng 190–193 (`render` đếm cả lượt bloom khi bật); `model-loader.ts` (`VisualQuality` có `ultra`).
- **Sửa:** chạy bench với `CHROME_FLAGS` thêm `--enable-precise-memory-info` (không có cờ này Chrome làm tròn và cập nhật thưa giá trị bộ nhớ, phép đo 2 MB vô nghĩa). Ghi rõ draw call **gồm** lượt hậu kỳ (bloom khoảng 10–13 lượt ở High). "Phím tới đòn" = từ `keydown` của chữ cuối tới khung đầu tiên có nét thư pháp rời Bàn Quyết (§21.1, 0,15 s là thời gian bay, không tính); đo bằng kịch bản mới `ic-hitstop-keys.mjs` của Làn 7 (Source: `games/dragon-hold/scripts/visual/scenarios/dh-hitstop-keys.mjs`). `TT_TIERS` khai đủ 4 khóa `low | medium | high | ultra` (ultra = high ở MVP); số kiếm, tam giác LOD, trần draw call để ở bảng riêng `TT_BUDGETS` trong `rules.ts` vì `StageTier` không có chỗ. Tông màu: đặt `stage.renderer.toneMapping = THREE.NeutralToneMapping` sau khi dựng (`renderer` công khai, `OutputPass` đọc giá trị này).

## 8. Mâu thuẫn nhỏ còn lại

### PB-27 · Báo trước dưới 1,2 s · nhỏ

- **Bằng chứng:** §10.6 ("Đòn **không** có đáp án gõ…: báo ≥ 1,2 s + (nửa bề rộng vùng ÷ 5 m/s)"); §10.5 (nguồn Rồng 02 §4.1: "đòn thường báo trên đất ≥ 1,2 s"); §10.2 T04 Nham Viên ("vòng báo **0,8 s**", vùng 2 m quanh điểm nhãn), T05 Thiết Giáp Trư ("vạch đỏ **0,9 s** + thời gian ra khỏi vạch").
- **Sửa:** Nham Viên báo 1,2 + 2 / 5 = **1,6 s**; Thiết Giáp Trư 1,2 s + thời gian ra khỏi vạch. Làn 5 thêm test dữ liệu `tests/sim/telegraph-floor.test.ts`: mọi `TelegraphDef` không có đáp án gõ đạt sàn này.

### PB-28 · CB5, preset Học, `telegraphScale` · nhỏ

- **Bằng chứng:** §10.6 ("`nạp = max(T_preset, nạp_gốc / k)`"; "CB5: … với k = 1,30 vẫn ≥ T"); §6.3 Ấn ("Thư giãn 3–5 · Cân bằng 4–6 · Thử thách 4–7", không có Học); BALANCE §4.1 (đòn bẩy "Thời gian báo trước đòn lớn × 0,85–1,5 theo phản xạ báo trước"); kit `balance/pace.ts` dòng 83 (`telegraphScale`).
- **Sửa:** vì `max()` đã kẹp, mệnh đề "k = 1,30" của CB5 luôn đúng; viết lại: "test gọi đúng hàm runtime `chargeTicks(def, preset, k)` với k ∈ {0,75; 1; 1,30} và ℓ lớn nhất; kết quả ≥ T". Học dùng độ dài Ấn của Thư giãn (3–5). Ghi quyết định: "M0a không dùng `telegraphScale`; khi dùng, `nạp = max(T, nạp_gốc × telegraphScale / k)`, không bao giờ dưới T".

### PB-29 · Lệch đánh giá chưa ghi thành quyết định · nhỏ

- **Bằng chứng và sửa:**
  - Pháp bảo: đánh giá §4 ghi "2 món mỗi trường phái", §6 ghi "1 pháp bảo"; canon §14.5 chọn 1 mà không có dòng D. Thêm D32 "1 món mỗi trường phái ở MVP (đã chọn theo đề xuất, theo §6 của đánh giá)".
  - Tu vi: đánh giá §3.1 và Phụ lục A4 "mỗi đợt một lần cho mỗi **bậc ải**"; canon §4.1 "mọi preset tính chung". Ghi D33 nêu rõ nghĩa đã chọn.
  - Tu vi "≈ 1,1 lần": 35 × 8 + 80 = 360 so với 357 cần là **1,008 lần** khi bỏ học tùy chọn; với 34 đợt (PB-04) còn 352 < 357 và Thiên Kiếp không mở. Đặt **9 tu vi mỗi đợt** ở K0: 34 × 9 + 80 = 386 = 1,08 lần (≈ 1,1 khi có học). Điều kiện Thiên Kiếp không được phụ thuộc phần học tùy chọn.

### PB-30 · Đơn vị · nhỏ

- **Bằng chứng:** canon §7.1 ("Sim lưu số nguyên: phần nghìn, **mm**, tick 60 Hz"), §6.1 (`origin` "mm, lượng tử 10 cm"); kế hoạch §3.1 ("u, 1 m = 60.000 u", như `games/dragon-hold/src/sim/fixed.ts` dòng 3–13).
- **Sửa:** canon §7.1: "Dữ liệu ghi mm; sim lưu u (1 m = 60.000 u, nguồn: Rồng `fixed.ts`)". §6.1: "`origin` lượng tử 100 mm = 6.000 u".

## 9. Định nghĩa còn thiếu cho agent viết mã

### PB-23 · Phím cho cửa hàng và đặt cơ quan · lớn

- **Bằng chứng:** canon §5.1 ("nguồn duy nhất"; không có phím chọn món, chọn ô, nâng, bán); §14.3 ("Không gõ để mua, đặt, nâng"); §5.1 "Mọi việc có đường bàn phím"; kế hoạch §6.7 (`ic-keyboard-only`: chơi cả ải chỉ bằng bàn phím). Mũi tên đã dùng để đi; 1/2/3 dùng cho đan; Tab không dùng ở MVP.
- **Sửa (đề xuất, nguồn: Rồng `00-canon.md` §6 chế độ sửa):** lúc bày trận và nghỉ, **`` ` ``** (Backquote) mở chế độ cửa hàng: mũi tên chọn món và ô (người chơi không đi trong chế độ này), Enter mua hoặc đặt, `=` nâng (bấm hai lần), `-` bán (bấm hai lần), Esc thoát. Ngoài chế độ cửa hàng, Enter bắt đầu đợt. Thêm vào màn đổi phím.

### PB-24 · Luật số nguyên và kiểu dữ liệu · lớn

Canon cần một mục "Hợp đồng dữ liệu" (bước 0 viết `types.ts` theo đó):

| Thiếu | Đề xuất |
|---|---|
| Thứ tự và làm tròn sát thương | Máu số nguyên (PB-06). `D = P → × M_q → × M_hệ → × (1 + Σ bucket) → × M_dễ_tổn_thương → giáp hoặc kháng (đòn không gõ) → trần cụm → trần máu còn lại`. Mỗi bước `pm()` làm tròn nửa lên. Sổ phần sát thương (CB2, CB3) cộng **sát thương hiệu dụng** (≤ máu còn), không cộng phần thừa |
| Phần đe dọa để trả 60 % Linh Sa hạ thú (§14.2) | ĐĐ = W gốc của thú ở K0 Cân bằng; cụm bầy = tổng W cụm, trả khi con cuối chết; tinh anh W × 1,6; thú gọi thêm trả 50 % |
| Trần 4 W của Lạc Kiếm Trận (§12.1) | Tổng một lần tung, mọi thú cộng lại |
| Thời điểm chạm | Ô 1: 3 kiếm ở tick +6, +36, +66 sau Cast; ô 2: +12; ô 4: mở ở +12, mỗi 30 tick một nhịp; ô 5: 3 loạt ở +30, +75, +120; đánh nền: +18. Sim áp sát thương đúng tick đó; view đồng bộ theo sự kiện |
| "Cụm đông nhất trong r" | Ứng viên là vị trí các thú sống trong tầm; điểm = tổng W trong bán kính của chiêu; hòa thì gần Trận Tâm hơn, rồi `beastId` nhỏ hơn |
| "Gần Trận Tâm nhất" | Thú đất theo khoảng cách trường hướng; thú bay theo khoảng cách thẳng; hòa thì `beastId` nhỏ hơn |
| Chồng hiệu ứng chậm | Khác nguồn nhân (Kết Giới 15 %, Kiếm Thung 25 %, Lạc Kiếm Trận 20 %), trần chậm tổng 60 %; khống chế cứng (trói, choáng, ngã) tính vào trần 35 % thời gian sống |
| `WaveDef` | `{ id, durationMs, gates, peaks: {atMs, lenMs}[], groups: {atMs, gate, species, count, cluster?, elite?, general?}[] }`; `atMs` nhân 1/k; luật cổng 1,5 s / 0,6 s kẹp sau khi nhân |
| `TelegraphDef` | `{ id, shape: circle | cone | line | cell, sizeMm, typedAnswer: boolean, answers: ("seal" | "move" | "ward" | "pillar" | "mech")[], chargeMs: number | "T", strike }`; CB5 và PB-27 chạy trên mọi bản |
| Hết đợt, thắng | Đợt hết khi đồng hồ đợt hết. Toán còn chờ ở cổng vì trần thú sống không sinh lúc nghỉ; nó dời sang đầu đợt kế. Ở đợt cuối, trận chờ tới khi mọi toán đã sinh. Thắng khi đợt cuối hết, không còn thú sống và Vương (nếu có) đã ngã |
| Gọi Đàn ở P2 | §10.5 ghi Gọi Đàn ở P1 và P3, không ghi P2. Chốt: P2 không gọi |
| Gục | Lúc gục: Bàn Quyết mờ, không gõ; Dưỡng tắt; không nhặt |
| Bậc hình mặc định | Lần đầu: High nếu chuỗi `renderer` là GPU rời, Medium nếu Apple, Low nếu khác; sau 10 s đầu trận, p95 > ngân sách của bậc thì gợi ý hạ một bậc (không tự đổi giữa trận) |
| L của Tĩnh Tu | "E người chơi" = E_eff của hồ sơ |

### PB-25 · Replay, nhật ký, bản lưu · lớn

- **Bằng chứng:** canon §23 (danh sách thứ lưu, không có cấu trúc), §18.3 B9 ("game xuất nhật ký; bot cùng E, a chạy lại cùng trận"), §18.4 golden; kế hoạch §6.2 (`runLog(world, local, log, untilTick)`), §6.9 (`save.ts` "lưu v1 tối thiểu").
- **Vì sao hỏng:** bộ từ đến từ lõi học (bất đồng bộ), k từ hồ sơ, số từ mới từ sổ cái; nếu đầu replay không chứa những thứ đó thì replay của người thật không chạy lại được (B9) và golden phụ thuộc máy.
- **Sửa:** canon §23 thêm cấu trúc:
  - Đầu replay: `{ v: 1, gameId, rulesHash, seed, stageId, preset, pacing: on | off, seats: [{ seat, profile: { e, a, cv }, kPm }], deck: [{ wordId, text, group, mastery, recalls, assumed }], newWordAllowance, loadout }`; thân: lệnh theo tick và đầu vào `local` (`move-to`, `arrows`); đuôi: `hashWorld`, `hashLocal` mỗi 600 tick.
  - Khóa lưu: `.save` `{ v, progress… }`, `.skill` (kit `serializeSkill`), `.newwords` (PB-10), `.settings` `{ v, motion, textScale, keymap, pacing, quality }`, `.pace` (bỏ nếu không dùng). Mỗi khóa một hàm chuyển đổi và một tệp mẫu trong `tests/app/save-migrate.test.ts`.

### PB-26 · Thứ tự lùi khi không có từ thỏa luật chữ · lớn

- **Bằng chứng:** canon §6.2 (chữ đầu khác nhau, không tiền tố, khoảng sửa > 1, chữ nghỉ 1 s, trần 8/5), §6.3 (loại từ và độ dài theo ô); Rồng `00-canon.md` §5 (`N_max = min(16 ; A − 3)`); kit `typing/budget.ts` (`letterBudget(available, rules)`).
- **Vì sao hỏng:** ô 3 (đã thuộc, 3–5 chữ) và Tẩy (đã thuộc, 3–4 chữ) có thể không còn từ nào sau khi trừ chữ đầu của 7 chữ sống, nhất là bộ từ trẻ em. Canon không nói lùi thế nào; mỗi agent sẽ tự chọn, có người sẽ lấy từ mới.
- **Sửa:** §6.2: "Trần chữ sống = min(trần preset; A − 3), A = số chữ cái có ≥ 3 từ hợp lệ trong bộ trận (nguồn: Rồng §5). Không có từ thỏa: (1) nới độ dài ±1 trong 3–8; (2) nới loại về phía **quen hơn** (đang học → đến hạn → đã thuộc), không bao giờ về phía từ mới; (3) ô chờ mờ và ghi 'nghẽn' cho báo cáo bot." Dùng `BudgetLedger` của kit cho trần theo nguồn.

## 10. Đã kiểm và đứng được

- Bảng T của §10.6 đúng với công thức (ví dụ ℓ 5: 1,6 × (0,4 + 0,5 + 72 / 12,9 + 0,2) = 10,69 s ở E 15; 7,12 s ở E 25; 5,59 s ở E 35). Với k kẹp 0,75 và E_eff của bot Trẻ em (10,9), Ấn 5 chữ cần ~8,8 s, nằm trong 10,7 s.
- C_ref: E_eff(35; 95 %; 0,25) = 29,43; C = 60 / (0,45 + 66 / 25,31) = 19,62 từ/phút.
- Máu đợt M0a khớp `L × 75 × phút` (30 / 42 / 53 / 65 / 72 / 86 W, cộng 348) và khớp thành phần từng đợt trong 1–2 W; tổng 459 con, 294 con bầy (64 %); tinh anh 5 / 165 = 3 %.
- Phần D_ref: gõ 47 / 75 = 62,7 %, đánh nền 16 %, cơ quan và trận pháp 21 %, khớp dải §7.3. Chân Nguyên ở 35 WPM: ~4,5 điểm mỗi từ × 19,6 từ/phút → đầy sau ~68 s, khớp 55–70 s.
- Quỹ Linh Sa M0a theo công thức là 1.325 (trước khi sửa PB-07). Dải Linh Sa 36 % mức dựng tối đa hơi vượt câu "15–35 %"; canon đã ghi phần trừ đan còn ~30 %.
- `kit/tools/cdp-run.mjs` mặc định `--dpr=1` nên số đo DPR 1 của §20.2 đúng mà không cần cờ thêm. `Stage3D` đặt `powerPreference: "high-performance"`, nên trên laptop Dell trình duyệt sẽ chọn RTX; kiểm chuỗi `renderer` vẫn cần.
- Mã nguồn kế hoạch định chép đều có thật: Rồng `src/sim/{fixed,hash,events,world,waves,spawn,director,combat,economy,shop,boss}.ts`, `src/typing/{deck,grading}.ts`, `src/app/{learning,typing-pace,pace-card,contracts}.ts`, `src/ui/{learning-frame,screen-zones}.ts`, `src/view/{crowd,bench,telegraphs,number-field}.ts`, `scripts/balance/*`, `scripts/visual/scenarios/dh-*.mjs`; `games/typing-defense/src/sim/nav/{grid,astar,connectivity}.ts`; `games/typing-survival/src/view/fx.ts` (`Glows`); `games/space-typing/scripts/models/blender/bake_impostor.py`. Lưu ý: sim của Rồng đi theo **làn** (`lanes.ts`, `movement.ts`), còn game này đi theo trường hướng và có lớp `local`, nên `world.ts`, `waves.ts`, `spawn.ts` là "viết lại có tham chiếu" hơn là chép; header `// Source:` vẫn đúng, nhưng ước 2–3 ngày cho `createWorld`, `step` là sát.

## 11. Thứ tự sửa

1. **Trước bước 0:** PB-01, PB-02, PB-10, PB-24, PB-25, PB-26 (đều vào `types.ts`, `rules.ts` và test ranh giới), PB-22 (sửa §2.3, test media), PB-20 (luật import).
2. **Trước khi Làn 1 chạy ma trận GPU:** PB-03, PB-19, PB-34, PB-35; Làn 1 giao mốc 1a trước (PB-36).
3. **Trước vòng cổng M0a:** PB-04 đến PB-09, PB-11, PB-14, PB-15, PB-17, PB-18, PB-23, PB-27, PB-28, PB-30, PB-37.
4. **Trước khi chạy bot Tĩnh Tu (HC4–HC7):** PB-12, PB-13, PB-31.
5. **Trước M1:** PB-16, PB-21, PB-29, PB-32, PB-33.

Mọi số đề xuất ở trên là **số thử**, chờ bot của Làn 7 và buổi chơi thử của anh. Những chỗ tôi ghi "đề xuất" mà canon chưa có là đổi luật, nên khi chép vào canon ghi **đã chọn theo đề xuất** kèm ngày.
