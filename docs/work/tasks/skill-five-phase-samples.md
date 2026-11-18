# 2 chiêu mẫu đủ 5 pha (Hỏa): sao băng từ trời và lưỡi liềm từ kiếm

**Mục tiêu (≤ 3 dòng):** cho anh xem một chiêu đúng chuẩn từ lúc tung tới lúc tàn, trước khi áp cho mọi chiêu lab.
**Cách đã chốt:** anh, 06/11 ~11:10: "sao băng là 1 chuyện, cả lưỡi liềm là 1 chuyện, cái chính là vfx khi tung chiêu, chiêu bay như nào, và vào quái sẽ ra sao, xung quanh chiêu đó animation sẽ như nào".
- Theo `docs/games/VFX_STANDARD.md` (5 pha: tụ lực, phóng ở người tung, bay, chạm, dư âm) và skill `game-vfx-layered`.
- Luật 03/11: mỗi pha có lớp hào quang (tia lấp lánh, hạt sáng, quầng mềm, vòng sáng ≤ 0,9 mỗi kênh).
- Mọi hình lấy từ clip và tranh của hệ (`art-src/lab/vfx/fire/manifest.json`: charge, release, ribbon, sheath, impact, burst, groundImpact, sparkle, comet; vệt cháy từ tranh). Không vẽ hình bằng mã.
- Anh chấm; làm mẫu trước, chưa áp cho các chiêu khác.

## Mẫu 1: sao băng Hỏa (D62, chiêu từ trời)
1. **Tụ lực ở người tung (0,15–0,3 s):** clip `charge` Hỏa ở tay hoặc kiếm; người sáng viền cam; tia lửa và hạt sáng hút vào; vòng phù văn dưới chân.
2. **Phóng (khung đầu sáng đủ):** clip `release` ở tay; chớp sáng; camera giật nhẹ; vệt sáng bắn lên trời (ra khỏi khung trên), báo chiêu đi lên.
3. **Bay:**
   - Ấn đánh dấu trên đất dưới từng con bị chọn, 0,15–0,25 s.
   - Sao băng (clip `comet`, `i2v-fire-comet`) rơi chéo 15–25°, đầu đi trước, đuôi `ribbon`, rắc hạt lửa dọc đường. Nhiều quả cách nhau 0,2–0,35 s.
4. **Chạm vào từng con quái:**
   - Clip `impact` Hỏa ở thân quái.
   - Quái lóe sáng màu lửa (viền hoặc tô màu 0,1 s), bị đẩy lùi hoặc giật, cháy lửa nhỏ trên người 1–2 s.
   - Số sát thương; dưới đất có `groundImpact` và vòng lửa xoay; hit-stop và rung theo bậc.
   - Quái chết tan thành tàn lửa.
5. **Dư âm (1,5–2,5 s, tàn bằng erosion):** vết cháy từ tranh trên đất, than hồng, khói đen nhạt bay lên.

## Mẫu 2: lưỡi liềm Hỏa (phím 2, chiêu từ kiếm)
1. **Tụ lực:** kiếm sáng dần (lớp bao `sheath`), hạt lửa xoáy quanh lưỡi kiếm, vòng sáng dưới chân.
2. **Phóng:** chớp ở mũi kiếm, vòng sóng xung quanh, giật camera nhẹ, lưỡi liềm (video `fire-crescent-sym`) tách khỏi kiếm.
3. **Bay:** lưỡi liềm bay thẳng; vệt năng lượng mềm phía sau (đã có `6116402`); tia lấp lánh từ hai sừng; khí nóng gợn quanh.
4. **Chạm:** như mẫu 1, cộng vệt chém hình lưỡi liềm in trên thân hoặc đất ở chỗ trúng; xuyên qua hàng quái thì mỗi con trúng một lần.
5. **Dư âm:** vết chém cháy trên đất từ tranh, tàn chậm.

**Nghiệm thu (số):**
- Từ phím tới phóng ≤ 50 ms; khung chạm đầu ≥ 95 % đỉnh; lõi trắng ≤ 25 % bề ngang.
- Chữ trên quái ≥ 7:1.
- Video cho anh: 2 mẫu, mỗi mẫu quay ở camera chơi và cận cảnh, 1080p, < 30 MB, vào `typing-game-review/owner-review/2026-11-06/tu-tien/five-phase-samples/`. Cập nhật 4310.

## Nhật ký (mỗi dòng một sự kiện: ngày giờ · ai · việc · kết quả)
- 06/11 11:15 · Claude · tạo việc, giao lab-element-kits (sau phần D62 thay sao băng)
- 06/11 11:35 · Claude · công cụ nhắn giữa phiên bị treo (timeout 300 s): việc này do agent con của phiên điều phối làm trong `games/.wt-ic-lab-elements` (nhánh claude/lab-element-kits). lab-element-kits: đừng làm trùng
- 06/11 12:05 · Claude (agent con) · xong, commit `4f98fb3` (nhánh claude/lab-element-kits, 1084 test qua, git sạch), 4310 = `4f98fb3`: Hỏa phím M và phím 2 đủ 5 pha bằng clip của hệ (`src/lab/five-phase.ts`; thấy pha tụ lực với `?typed=1`: http://127.0.0.1:4310/skills-lab.html?element=fire&typed=1); sao băng mọi hệ dùng clip `comet` của hệ (video 1080p, đầu dẫn; 14/14 hệ + lớp thân `dark-comet-white`, entry manifest của lab-flipbooks giữ nguyên); phím tới phóng cùng khung, khung chạm đầu sao băng = đỉnh (1,00) · video `owner-review/2026-11-06/tu-tien/five-phase-samples/fire-meteor-five-phase.mp4` (8,3 MB), `fire-crescent-five-phase.mp4` (8,7 MB) · chưa làm: khí nóng gợn quanh lưỡi liềm; chưa đo chữ ≥ 7:1 (nhánh chưa có thẻ chữ) và lõi trắng ≤ 25 %
- 06/11 12:45 · Anh (xem 2 video mẫu): "tôi muốn chiêu rộng hơn, mạnh mẽ hơn, hiệu ứng mạnh hơn khi va chạm, hiện tại nhìn vẫn hơi bé và cảm giác hơi yếu, nhất là thiên thạch". Vòng 2, tăng uy lực (lab-element-kits làm, sau khi gộp readability và sound-mix):
  - **Sao băng (M):**
    - 5 quả, cách nhau 0,25 s, rải trên các cụm quái dày nhất, phủ khoảng 20 m.
    - Thẻ sao băng to gấp 2,5–3 lần: đầu khoảng 3 m, cả thân 10–12 m.
    - Mỗi cú chạm:
      - `burst` hoặc `big-burst` của hệ rộng 7–9 m, giữ đỉnh 0,5–0,8 s, tan 1,2 s;
      - `groundImpact` 8 m; vòng sóng xung kích (`ring-burst` nếu có, không thì `groundImpact` nở rộng) lan ra 10–12 m trong 0,4 s;
      - tàn lửa và mảnh vụn văng 6–8 m.
    - Vùng sát thương 4–5 m mỗi quả, khớp với hình. Quái bị hất văng 2–3 m theo đường cong, lảo đảo.
    - Hit-stop 0,10 s ở cú đầu, 0,05 s ở các cú sau. Bậc rung "tuyệt kỹ". Camera giật xuống. Chớp ấm toàn màn ≤ 0,6 trong 2 khung. Đèn chạm bán kính 12 m.
    - Dư âm: vết cháy 6–8 m, đất cháy (`fire-ground-burn-loop-w2`) 2–3 s, cột khói.
    - Âm: `tt-sfx-el-fire-comet` (đang về), chồng tiếng nổ trầm.
  - **Lưỡi liềm (2):** sải 6 m, dày hơn. Mỗi cú trúng nổ 3–4 m. Nhát cuối ở cuối đường: `big-burst` 6 m + vòng sóng + hất văng.
  - Chữ trên quái vẫn ≥ 7:1 (nhánh readability đã gộp).
  - Video mới, camera chơi và cận cảnh; khung so sánh trước/sau.
- 06/11 12:50 · Anh thêm: "thiên thạch phải làm dạng mưa thiên thạch, rơi nhiều nơi trong map, và rơi trong khoảng 5-8s". Thay phần sao băng ở dòng 12:45:
  - **Mưa thiên thạch (M), kéo dài khoảng 6,5 s, nằm trong 5–8 s:**
    - 18–24 quả rơi khắp bản đồ, không chỉ ở cụm quái: khoảng 60 % vào các cụm quái dày, 40 % rải đều sân.
    - Nhịp 0,2–0,4 s, có lệch ngẫu nhiên; dồn dày ở giữa, thưa ở hai đầu.
    - Cỡ khác nhau: khoảng 30 % quả lớn (đầu 3 m, nổ 7–9 m, vòng sóng 10–12 m), 50 % quả vừa, 20 % quả nhỏ.
    - Kết thúc bằng một quả lớn nhất rơi vào cụm dày nhất (nổ 10 m, hit-stop 0,12 s).
  - Mỗi quả có ấn đánh dấu, nổ, vòng sóng, mảnh vụn, hất văng như dòng 12:45. Đất cháy tích dần, tối đa khoảng 12 mảng cùng lúc, tàn bằng erosion.
  - **Hiệu năng:**
    - Mọi quả cùng hệ dùng chung một VideoTexture của clip `comet`; nổ và vòng sóng dùng atlas.
    - Không quá 6 cụm nổ cộng sáng chồng nhau.
    - Rung theo từng quả, quả lớn mạnh hơn, không cộng dồn thành rung liên tục.
- 06/11 12:52 · Anh thêm: "cục thiên thạch cũng cần làm to hơn". Cỡ thân sao băng tăng: quả lớn đầu 4–5 m, thân 14–16 m; quả vừa đầu khoảng 3 m; quả nhỏ đầu khoảng 2 m. Đầu thiên thạch phải là khối rõ, đặc, sáng (không chỉ là đốm sáng).
- 06/11 12:37 · Claude (lab-element-kits) · vòng 2 xong, commit `b8ebd51` (trước đó gộp `claude/lab-readability` → `29dbf95` và `claude/lab-sound-mix` → `9aed0d3`, sửa 1 xung đột ở `clip-skills.ts`, giữ cả hai), 4310 = `b8ebd51`, 106 tệp 1097 test qua.
  - **Mưa thiên thạch M (mọi hệ):** lịch rơi theo hạt giống (`meteor-plan.ts`): 21 quả trong khoảng 6,45 s, cách nhau 0,2–0,4 s, dày ở giữa. Mở bằng quả lớn, kết bằng quả lớn nhất vào cụm dày nhất.
    - Cỡ: lớn đầu khoảng 4,2 m, nổ 8 m, vòng sóng 11 m; quả cuối đầu 4,8 m, nổ 10 m, vòng sóng 12 m; vừa đầu 3 m; nhỏ đầu 2 m.
    - Đầu sao chổi vẽ thêm một lớp đặc; mọi quả cùng hệ dùng chung VideoTexture.
    - Chọn chỗ rơi lúc quả bắt đầu rơi: 60 % vào cụm quái, còn lại trên sân. Hất văng 2–3 m (`herd.launch`).
    - Dừng hình 0,10 / 0,05 / 0,12 s; rung riêng từng quả (`ScreenFx.jolt`, không cộng dồn); chớp ấm sớm 20 ms.
    - Đo: tối đa 6 vụ nổ cùng lúc, 10 mảng đất cháy.
  - **Vụ nổ Hỏa (`FivePhase.blast`, chỉ clip của hệ):** vòng chớp, sen lửa phun, phun tia, vòng `qi-burst` lan, tàn lửa và tia văng; đất cháy `fire-ground-burn-loop-w2` 2,5 s.
  - **Lưỡi liềm phím 2:** thẻ 3,6 → 4,2 (sừng khoảng 7,5 m), vùng trúng ±3 m. Mỗi con trúng nổ 3,6 m. Cuối đường nổ 6 m, đánh và hất văng mọi con trong 3,2 m.
  - **Số đo:**
    - Chữ ≥ 7:1 ở mọi lúc đo, thấp nhất 7,64:1 (lưỡi liềm nổ cuối đường). Phím 2 nay cũng giảm sáng sau thẻ chữ còn 0,12 như phím M; trước đó có 1 thẻ chỉ 5,84:1.
    - Khung chạm đầu: 97 % đỉnh của chính vụ nổ, đo khô như vòng 1. Khi có đòn, số và lóe viền quái hiện ở khung sau (+30 %), phần đó thuộc đường đánh chung.
  - **Sửa:** sau khi gộp readability, hai bản vá shader khai báo `uPivot` trước `main` hỏng biên dịch; nay khai báo ở đầu.
  - **Video:** `owner-review/2026-11-06/tu-tien/five-phase-samples/fire-meteor-five-phase-v2.mp4` (18,4 MB) và `fire-crescent-five-phase-v2.mp4` (10,3 MB), kèm `meteor-truoc-sau-v2.jpg`, `crescent-truoc-sau-v2.jpg`.
  - **Chưa làm:**
    - Âm `tt-sfx-el-fire-comet` đã về (4 bản lúc 11:58) nhưng chưa nối: cần đo độ to và điểm bắt đầu.
    - Khí nóng gợn quanh lưỡi liềm.
    - Hai giám khảo mù.
