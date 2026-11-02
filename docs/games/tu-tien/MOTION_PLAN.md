# Kế hoạch: chiêu Kiếm và nhân vật mượt (lab Tu Tiên)

Không sửa `shared/game-kit` và `src/kit` (D44). Mã mới đặt ở `src/lab/anim/`, chỗ kit còn thiếu thì ghi vào `docs/SYNC_DEBT.md`. `kiem.ts`, `fxkit.ts` và `skills-main.ts` chỉ được sửa sau khi làn đang giữ chúng commit.

## Bước 1. Đo trước

Tạo file mới `src/lab/motion-probe.ts`, đọc qua `__lab.metrics()`. Mỗi khung ghi:
- xương: vận tốc góc so với đỉnh clip, khoảng cách tới tư thế bind;
- gốc: tốc độ, tốc xoay;
- chân: tốc độ khi đang chạm (cao < 4 cm);
- VFX: duyệt cây cảnh, mỗi mesh ghi `visible`, alpha, scale thế giới (không phải sửa file VFX);
- mốc: phím cuối, `release` của thân, khung VFX nhả.

Ngưỡng:
- Theo §5.11:
  - vận tốc góc lúc chuyển ≤ 1,5 × đỉnh clip;
  - trượt chân ≤ 0,05 m/s;
  - mối nối vòng lặp ≤ 1 cm;
  - xuyên đất ≤ 2 % chiều cao;
  - sự kiện lệch ≤ 1 khung;
  - phím cuối tới lúc nhả ≤ 50 ms;
  - dáng gồng khác dáng nhả ≥ 15 %.
- Không khung nào gần tư thế bind.
- Alpha hay cỡ của một lớp không đổi quá 30 % trong 1 khung, trừ lóe đã khai báo (VFX_STANDARD §3.1 luật 5).

Kịch bản `scripts/visual/scenarios/lab-motion.mjs` (cdp-run, `?fixed=1`) chạy chuỗi của Bước 4 và ghi vào `tmp/shots/motion/<lần>/`:
- `metrics.json`;
- tờ chuyển tiếp: 6 khung quanh mỗi lần đổi trạng thái;
- clip nửa tốc độ: bước 1/60 s, ffmpeg ghép ở 30 fps;
- thêm một lượt rAF ở 120 Hz.

Chụp xong thì xóa khung thô bằng `prune.mjs --apply`. Chạy kịch bản trên lab hôm nay trước để có mốc so sánh.

## Bước 2. Nhân vật: `Animator` cục bộ

`caster.ts` gọi Animator thay cho `play()`.

1. Lỗi nền: đặt `clampWhenFinished = true`; về Idle trước khi clip hết, Idle chạy từ khung 0; chỉ một listener; chiêu lặp lại không gọi `reset()`.
2. Chuyển tiếp quán tính từng xương. Half-life:
   - vào nhả 0,04 s;
   - vào gồng 0,06 s;
   - về Idle 0,09 s;
   - dash: vào 0,04 s, ra 0,08 s;
   - trúng đòn 0,03 s.
3. Gồng theo gõ (§5.6): `time = tiến_độ × release`. Phím cuối thì chạy tiếp từ `release` (Attack và Skill1 0,267 s; Skill2 0,708 s; Ult 1,083 s). Đoạn vung chạy ×1,3, đoạn thu ×0,9. Khi VFX còn tick sau lúc clip hết (K1, K5) thì giữ dáng thu tới tick cuối. VFX phát từ `FX_HAND_R`, sau `mixer.update`.
4. Lúc load, lấy mẫu lại quaternion từ 24 lên 60 fps bằng squad, làm trong bộ nhớ.
5. Máy trạng thái theo §5.5:
   - Idle + Fidget;
   - Walk↔Run theo tốc độ, nhịp bước khớp mặt đất;
   - Start/Stop;
   - xoay tại chỗ khi lệch > 60°;
   - Gồng, Nhả, Thu, Dash;
   - Hit dạng lớp cộng (vào 0,03 s, ra 0,25 s).
6. Yaw dùng lò xo tới hạn, half-life 0,06 s. Vị trí có tăng tốc và giảm tốc. Dash: easeInOut, thêm 2 khung khom, clip khớp 0,2 s đi + 0,15 s hồi.
7. Nhìn theo: lò xo 0,09 s, chia head 0,6, neck 0,4, spine_03 0,2; kẹp ở 20°.
8. Khóa chân: IK hai đốt thigh, calf, foot. Coi là chạm khi chân < 0,12 m/s và < 4 cm. Xoay tại chỗ thì đặt lại chân ở 45–60°.
9. Lò xo phụ: rig 31 xương không có tay áo hay dải lụa, nên dùng đuôi, tai và `bag_r`. Dùng `@pixiv/three-vrm-springbone` (MIT), bước cố định 60 Hz, `center = root`.
10. Lớp cộng: thở 0,25 Hz (spine 1°); giật lùi bằng lò xo 5 Hz, ζ 0,6 lúc nhả.

Clip còn thiếu: Walk, Start/Stop, Turn 90°/180°, Strafe, lùi, Hit sau. Nguồn CC0 (§5.2):
- Mesh2Motion người: có sẵn ở `games/typing-defense/art-src/anim/mesh2motion/`, dùng trước.
- Quaternius UAL1 và UAL2 Standard: cần chủ dự án đồng ý tải.

Chuyển clip sang xương Lam trong Blender (`td_rig_*`). Không dùng Mixamo.

## Bước 3. VFX chiêu, theo mức dễ thấy

1. K5, kiếm đã cắm còn trượt vòng: chốt góc ngay lúc cắm.
2. K5, sigil nhảy góc lúc nhả: cộng dồn pha trên CPU, vành kiếm dùng chung pha đó.
3. K5, vòng 24 kiếm sau lưng đứng rồi biến mất: vẫn cho quay, thu cỡ dần.
4. Ribbon tắt phụt: fade 0,18 s, đuôi co lại; lấy mẫu theo thời gian.
5. K2, kiếm nằm im ở đầu xa: cho trượt quá đích rồi mờ dần.
6. Đòn bay lật thẳng đứng lúc trúng: giữ hướng bay cuối, bám theo quái bị đẩy.
7. Vầng sáng sau lưng bật tắt, sigil hiện theo nấc phím: dùng smoothstep cho alpha và mép.
8. Dash: cập nhật `this.c` sau khi di chuyển nhân vật.
9. K5 lao xuống: nội suy hướng, đặt roll rõ ràng.
10. Hộ thân, K1, K4: kiếm scale-in khi hiện, mờ dần khi kết thúc, điểm đỡ đi theo lò xo.
11. Việc nhỏ (cách sửa theo báo cáo kiểm tra):
    - sao ở mũi kiếm;
    - đèn chớp va chạm (lab tự quản đèn);
    - rung camera, thoát hit-stop;
    - quái trong lab;
    - `auraBig`;
    - bước cố định 60 Hz có nội suy.

Sau mỗi mục, chạy lại `lab-motion.mjs`.

## Bước 4. Demo di chuyển

Chuỗi dài 60 s, gõ ở 45 WPM:
- Idle thở → đi → lên chạy theo đường cung → dừng.
- Xoay 90° rồi 180°, đi ngang, dash.
- Ra đòn: đòn thường, K1, K2, hộ thân, K4, K5.
- Trúng đòn, rồi về Idle.

Cách quay và nộp:
- Camera chơi quay cả chuỗi, rồi quay lại ở cận cảnh 55°, cách 6 m.
- File: MP4 1920×1080 60 fps, kèm bản nửa tốc độ, tờ chuyển tiếp và tóm tắt số đo.
- Hai giám khảo mù độc lập chấm trước khi đọc số đo, theo các hạng mục: theo đà, khối lượng, chuyển tiếp, trúng đòn, đi và đứng, đọc rõ ở camera chơi, VFX mượt.
- Chỉ gửi chủ dự án khi cả hai giám khảo cho ≥ 7 ở mọi hạng mục.
- Gửi kèm hai danh sách:
  - đã làm được gì ở mức 7, với số đo trước và sau;
  - còn gì ngăn tới 8,5 (năm cách sửa của mỗi giám khảo).
- Mốc 8,5 cuối cùng chấm trong bản chơi, không dùng cờ URL.

## Bước 5. Rủi ro và việc cần chủ dự án quyết

- **Cần đồng ý:** tải Quaternius UAL1/UAL2 Standard (CC0). Trong lúc chờ thì dùng Mesh2Motion.
- **Cần quyết:** animation nhân vật là hệ dùng chung (luật ≥ 9). Đề xuất: lab nhắm 8,5, bản kit sau này nhắm 9.
- Lam là nhân vật mượn: Animator phải tách khỏi rig; clip sẽ phải chuyển lại cho anh hùng thật.
- Mã cục bộ sẽ thành một bản sao trước khi có kit `anim/`: ghi vào SYNC_DEBT, giữ API theo §5.5–5.8.
- Clip CC0 trên tỉ lệ cách điệu dễ trượt chân: xử lý bằng khóa chân.
- Clip 24 fps có thể vẫn máy móc sau khi lấy mẫu lại: khi đó làm lại đoạn vung ở 60 fps trong Blender.

## Kết quả vòng 1 (02/11/2026, tối; commit game `ca730aa`)

Bước 1–4 đã làm trong lab (chi tiết trong các changelog `2026-11-02-lab-motion-*` và `2026-11-02-lab-vfx-smoothing` của repo game; bảng số ở `tmp/shots/motion/final/metrics-table.md`). Số đo ở 60 Hz, trước → sau:

| Mục | Trước | Sau | Ngưỡng |
|---|---|---|---|
| Chuyển clip vượt 1,5 × đỉnh | 5/20 | 2/26 (bắt đầu đi, dừng) | 0 |
| Khung qua tư thế bind | 24 | 0 | 0 |
| Trượt chân trụ p95 | 1,42 m/s | 0,26 m/s (tốc Lam 0,12) | 0,05 |
| Xoay gốc lớn nhất | 10.800 °/s | 487 °/s | — |
| Phím cuối → thân nhả | tới 817 ms | 33 ms | ≤ 50 ms |
| Lớp VFX bật / tắt phụt | 102 / 33 | 0 / 0 | 0 |
| Lỗi kiếm (hiện, tắt, đổi cỡ, giật hướng) | 37 / 27 / 22 / 306 | 0 | 0 |

Hai giám khảo mù (MJ1, MJ2) chấm demo: **5,4 và 5,4**. Kỹ thuật đã mượt, nhưng thiếu phần diễn:
- thân gần như đứng yên khi ra chiêu, không lấy đà, không vặn thân, VFX gánh hết lực;
- sau K5 nhân vật dang ngang tay đứng im khoảng 1,5 s, sau K2 quay gần 180°;
- trúng đòn chỉ đổi màu cả người trong một khung; quái không phản ứng;
- dash không đổ người, không nén, không bước hãm;
- hộ thân và K4 dùng chung một clip;
- mọi chiêu cùng một khuôn trận trắng; lóe lúc nhả xóa mất nhân vật ở cận cảnh;
- ở camera chơi nhân vật chỉ cao 30–70 px nên khó đọc.

Chưa gửi demo cho chủ dự án (mốc gửi là 7). Vòng 2 đang chạy: làn diễn xuất (lấy đà, phát lực, giữ thế, hồi chiêu, dash, trúng đòn, bước xoay và bước dừng), rồi làn va chạm (hit-stop, rung camera, lóe khu trú, mờ dần, mỗi chiêu một hình và màu riêng, quái phản ứng, vòng sáng dưới chân), mỗi làn có phản biện, sau đó demo và hai giám khảo mới.

## Phụ lục (báo cáo chỉ đọc, 02/11/2026)

### A. Kiểm kê rig và clip của Lam

### Kiểm kê rig Lam (lam.glb) cho phòng thí nghiệm chiêu Kiếm

Tôi chỉ đọc, không sửa file nào trong repo. Mesh cao 2,7 đơn vị và caster thu về 1,75 m, nên 1 đơn vị = 0,648 m. Mọi số tính bằng mét bên dưới là ở cỡ trong lab.

#### 1. Rig
- File do Blender I/O 5.2 xuất. Skin `lam_rig` có **31 xương**, không phải 25 như comment trong `caster.ts` ghi. Mesh 20.000 tam giác, 12.698 đỉnh.
- Trọng số skin tốt: 73% đỉnh chịu nhiều xương. Đây không phải bản auto-rig Tripo lỗi mà CHARACTER_ANIMATION §5.3 nhắc tới.
- Cây xương:
  - `lam_rig` (xoay 180° quanh Y) chứa `root` (−90° quanh X, kiểu Z-up của Blender), rồi tới `pelvis`.
  - Từ `pelvis` có: `bag_r` (gắn `FX_TOOL`), `spine_01` → `spine_02` → `spine_03`.
  - Từ `spine_03`: hai tay `clavicle` → `upperarm` → `lowerarm` → `hand_l/r` (gắn `FX_HAND_L/R`), và `neck_01` → `head` (gắn `ear_l`, `ear_r`, `FX_HEAD`). `FX_CORE` gắn vào `spine_02`.
  - Từ `pelvis` còn có đuôi `tail_01` đến `tail_05`, và hai chân `thigh` → `calf` → `foot` → `ball` mỗi bên.
  - `FX_FEET` là con trực tiếp của `root`.
- Không có xương vũ khí hay kiếm.
- Metadata trong extras của `lam_rig`:
  - `td_clips` ghi loop, giây, `crossfade_s` từng clip, một số ghi chú, và `groundSpeed_mps` (Run để null, Dash 2,58).
  - `td_lookAt` cho xương head: yaw và pitch 20°. Quá khoảng 25° thì viền mũ trùm bị giãn.

#### 2. Clip
Đặc điểm chung của cả 13 clip:
- Mỗi clip có 93 kênh: 31 xương × T/R/S, khóa 24 fps, nội suy LINEAR.
- Kênh STEP và kênh scale đều chỉ có giá trị hằng.
- Chỉ xoay và tịnh tiến của `pelvis` là thật sự chuyển động.
- **Không clip nào có root motion**: `root` đứng yên, mọi clip đều tại chỗ.

| Clip | Giây | Loop (meta) | Crossfade meta | Pelvis | Mối nối và ghi chú | Lab dùng |
|---|---|---|---|---|---|---|
| Hero_Idle | 3,125 | có | 0,15 | ≤4 mm | nối vị trí 0°, vận tốc liền; đuôi ≤13°, calf ≤8,6° | idle |
| Hero_Run | 0,833 | có | 0,15 | nảy dọc 7,7 cm | nối 0°, vận tốc ≈ liền; nghiêng 15°; chân chạm đất lùi 3,1–3,7 m/s ở tốc 1× | không |
| Hero_Attack | 0,833 | không | 0,1 | y 11 cm, z 6,5 cm | tay phải đạt tốc đỉnh 19 m/s ở **0,267 s**; khung cuối = Idle@0 (0,7°) | auto, k1 |
| Hero_Skill1 | 1,667 | không | 0,1 | y 17 cm | 0,83 s đầu giống Attack; tay trái đạt đỉnh ở 0,567 s; khung cuối = Idle@0 | k2 |
| Hero_Skill2 | 1,917 | không | 0,1 | 1–2 cm, chân khóa | tay trái đạt đỉnh 21,8 m/s ở 0,700 s; khung cuối = Idle@0 | guard, k4 |
| Hero_Ult | 1,667 | không | 0,1 | y 8 cm | hai tay đạt đỉnh 6,5 m/s ở 1,083 s; khung cuối = Idle@0 | k5 |
| Hero_Assist | 2,667 | có | 0,15 | 0 | tư thế tay lệch Idle 83° | không |
| Hero_Hit | 0,417 | không | 0,1 | hạ 27 cm | chỉ một hướng | không |
| Hero_Death | 2,167 | không | 0,15 | −10 cm, khung cuối nằm | chỉ một kiểu | không |
| Hero_Respawn | 1,417 | không | 0,1 | 25 cm | bắt đầu ngồi (lệch 96°), kết thúc ở Idle | không |
| Hero_Victory | 2,208 | không | 0,1 | 3 cm | chân khóa | không |
| Hero_Idle_Fidget | 2,5 | không | 0,1 | 27 cm | đầu quay 25° | không |
| Hero_Dash | 0,708 | **có** (đây là chu kỳ chạy) | 0,15 | 6 cm | nghiêng 22°, tốc mặt đất đo được ≈2,5 m/s | dash |

Có clip Hit, Death, Run và hai biến thể Idle (Idle, Idle_Fidget). Không có Walk, Turn hay Strafe.

#### 3. Lab gọi clip thế nào (`caster.ts`, `kiem.ts`)
- Chiêu nào chạy clip nào:
  - auto, k1 → Attack
  - k2 → Skill1
  - guard, k4 → Skill2
  - dash → Dash
  - k5 → Ult
  - còn lại → Idle (LoopRepeat)
- Mỗi lần gọi `play()`: `reset()`, đặt `LoopOnce` với `clampWhenFinished=false`, rồi nhảy thẳng tới `time = min(0,3·dur, 0,25)`. Với Dash là 0,2125 s, các chiêu khác 0,25 s. Sau đó `crossFadeTo` 0,08 s, ngắn hơn mức 0,1–0,15 s mà meta ghi. Khi nhận sự kiện `finished` thì `play("idle")`, cũng fade 0,08 s.

#### 4. Chỗ giật đo được
1. **Bỏ mất pha gồng.** Attack và Skill1 bắt đầu ở 0,25 s, chỉ 17 ms trước tốc tay đỉnh (0,267 s). Cú chém hiện ra giữa đường, và tư thế phải nhảy so với Idle:
   - Attack, Skill1: lowerarm_r 68°, tay lệch 0,47 m
   - Ult: calf_r 62°, tay lệch 0,43 m
   - Skill2: 32°
   - Dash: thigh_r 102°, tay lệch 0,46 m

   Cả bước nhảy đó nén vào 0,08 s, khoảng 5 khung ở 60 Hz.
2. **Trong lúc gõ, nhân vật không động gì.** `setCharge` không gọi animation nên nhân vật đứng Idle suốt lúc gõ. Chưa có phần tua gồng theo tiến độ gõ (§5.6).
3. **Mỗi lần hết chiêu đều hiện tư thế nghỉ khi rig.** Tôi đã kiểm trong three 0.170: `clampWhenFinished=false` làm action bị tắt khi hết clip. Idle lại fade lên từ 0, nên phần trọng số còn thiếu bị lấp bằng tư thế nghỉ khi rig (bind pose), tức `PropertyMixer` khi weight < 1. Khoảng cách giữa tư thế nghỉ khi rig và Idle: calf_r 43,5°, tay 15 cm, pelvis 3 cm. Ở giữa lúc fade, gối giật khoảng 22° và tay lệch khoảng 7 cm. Thêm nữa, Idle chạy tiếp từ thời điểm bị dừng chứ không quay về khung 0, trong khi các chiêu được làm để kết thúc đúng Idle@0.
4. **Khóa 24 fps nội suy tuyến tính, mỗi khóa xoay rất xa.** Bước lớn nhất mỗi khóa:
   - lowerarm_l 97° (Skill2)
   - upperarm 74° (Skill1)
   - calf_r 68° (Run)
   - foot_r 64° (Dash)

   Ở 60 Hz chuyển động sẽ gãy góc tại từng khóa.
5. **Dash là clip lặp nhưng bị chơi một lần.** Vị trí trượt 0,2 s theo easeOutCubic, chân lùi 2,5 m/s, nên chân trượt so với mặt đất.
6. **`face()` và `moveTo()` xoay tức thì.** Hai hàm gán thẳng `rotation.y`, không có lò xo hay giới hạn tốc độ quay.
7. **Đuôi và tai dùng khóa sẵn trong clip**, không có springbone. Ở Run, tail_04 đi tới 36° mỗi khóa.
8. **Điểm nhả chiêu đặt ở cổ tay.** `hand()` lấy xương `hand_r` (cổ tay), trong khi `FX_HAND_R` nằm ở lòng bàn tay và đã có sẵn.

#### 5. Còn thiếu để di chuyển mượt
- **Walk.** Run ở tốc 1× cần khoảng 3,4 m/s. Muốn đi bộ 1,4 m/s thì phải chậm xuống khoảng 0,4×, trông sẽ sai. Cần clip Walk và trộn Walk↔Run theo tốc độ.
- **Start và Stop**: từ Idle sang Run, từ Run về Idle.
- **Xoay**: Turn L/R tại chỗ, quay 90° và 180°.
- **Strafe**: sang trái, sang phải, lùi.
- **Nghiêng khi rẽ** bằng thủ tục.
- **Tốc mặt đất trong metadata**: Run đang để null nên tốc phải khớp bằng code.
- **Mốc sự kiện** `foot_l/r` (lúc chân chạm), `windup_end`, `release`.
- **IK chân** và **nhìn theo** bằng `td_lookAt` (yaw/pitch 20°), hiện lab chưa dùng.
- **Chuyển tiếp quán tính hoặc crossfade đúng.** Trước hết là `clampWhenFinished=true` và fade về Idle trước khi hết clip.
- **Lấy mẫu lại** mượt hơn: 30–60 fps hoặc cubic.
- **Lò xo phụ** cho đuôi và tai.
- **Lab chưa có máy trạng thái di chuyển.** Nhân vật chỉ được đặt vị trí tức thì hoặc trượt khi dash.

Script và số liệu thô nằm trong scratchpad:
- /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/glb-inventory.mjs
- /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/glb-fk.mjs
- /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/seam.mjs
- /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/lam-inventory.json

### B. Chỗ giật, bật, dịch chuyển tức thời trong lab

**Kiểm tra độ liền mạch chuyển động: skills lab Kiếm (Tu Tiên)**

Phạm vi: chỉ đọc code (không sửa file nào trong repo) và đo `lam.glb` bằng script. Chưa chạy trình duyệt nên chưa có ảnh chụp xác nhận. Số dòng lấy theo cây làm việc lúc 13:28 ngày 02/11; `kiem.ts`, `fxkit.ts`, `skills-main.ts` đang được agent khác sửa (lần sửa cuối 13:06), tôi đã đối chiếu lại các dòng chính và chúng còn đúng. Ở camera chơi, 1 m ≈ 23 px ở 720p, nên nhân vật cao khoảng 40 px.

**Số đo `lam.glb`** (script ở `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/`: `clips.mjs`, `xfade.mjs`, `peak.mjs`, `interp.mjs`, `seam.mjs`):
- Độ dài clip: Attack 0,833 s; Skill1 1,667 s; Skill2 1,917 s; Ult 1,667 s; Dash 0,708 s.
- Key là LINEAR ở 24 fps. Chỉ pelvis có translation (nhún dọc), không có root motion tiến tới.
- Các clip bắt đầu và kết thúc gần đúng tư thế Idle (lệch khoảng 0,1–0,5°), riêng Dash lệch tới 104°.
- Vòng lặp Idle khít, không có mối nối.
- Tư thế bind lệch Idle: calf_r 43°, lowerarm_r 39°, clavicle_r 34°.

**Xếp hạng theo mức dễ thấy ở camera chơi** (mỗi mục: chỗ trong code, người xem thấy gì, cách sửa trong một dòng)

1. **Kiếm K5 đã cắm xuống đất vẫn trượt vòng.** `kiem.ts:2045, 2062–2065, 2076–2082`
   - Thấy: góc `th` vẫn cộng `rot = k.t·1,1`, nên những thanh đã cắm (y = 0,35) trượt quanh vòng tròn 13 m với tốc độ 1,2–6,3 m/s. Đợt 1 trượt khoảng 2,6 s, đợt 3 khoảng 1,1 s.
   - Sửa: khi `dive > 0`, chốt góc ở `(hitT − 0,16)·1,1` thay vì `rot`.

2. **Nhân vật giật về tư thế bind ở cuối mọi clip.** `caster.ts:75, 84–92`
   - Nguyên nhân (three 0.170): `clampWhenFinished = false` làm action tự tắt khi hết clip (`AnimationAction.js:527`). Trọng số của nó về 0 ngay khung đó, còn Idle chỉ bắt đầu fade-in từ 0, nên `PropertyMixer.js:152` trộn vào tư thế gốc.
   - Thấy: 1 khung tư thế bind (calf_r 44°, lowerarm_r 39°; Dash: upperarm_r 125°, lowerarm_r 86°), rồi 80 ms trở về Idle. Lúc xảy ra: 0,58 s (Attack), 1,42 s (Skill1, Ult), 1,67 s (Skill2), 0,5 s (Dash) sau lúc ra đòn. Bước nhảy bằng 1,7–4,8 lần tốc độ góc của xương nhanh nhất trong clip, vượt luật ≤ 1,5× ở §5.11.
   - Sửa: `clampWhenFinished = true` và lên lịch crossfade về Idle 0,2 s trước khi clip hết (hoặc dùng lớp quán tính §5.5), không chờ sự kiện `finished`.

3. **Sigil xoắn ốc K5 nhảy góc lúc ra đòn.** `fxkit.ts:911` (`rot = uTime·uCount`), `kiem.ts:1590` (0,35) chuyển sang `kiem.ts:2138` (1,1)
   - Thấy: các nhánh thiên hà rộng 13,5 m xoay đột ngột một góc `uTime·0,75` rad, tùy trang đã mở bao lâu. Sau đó nhánh sigil không khớp với các vành kiếm.
   - Sửa: cộng dồn pha trên CPU (`uPhase += tốc_độ·dt`) và cho vành kiếm dùng chung pha đó.

4. **Vòng 24 thanh kiếm sau lưng (vầng hào quang K5) đứng hình rồi biến mất.** `kiem.ts:2156–2164`; nhánh nạp ở 1581–1617 thôi chạy khi đã ra đòn
   - Thấy: vòng ngừng quay ngay lúc ra đòn, đứng yên 0,3 s rồi cả 24 thanh biến mất trong 1 khung.
   - Sửa: sau khi ra đòn vẫn cập nhật vị trí và quay, nhân scale với `1 − k.t/0,3` (hoặc phóng từng thanh vào vành).

5. **Vệt sáng (ribbon) tắt phụt.** `fxkit.ts:484–486, 495–497`; `kiem.ts:1793` (K2), `1924` (dash), `1822/1869` (hộ thân)
   - Thấy: vệt K2 dài 14 m đông cứng ở độ sáng tối đa 0,33 s rồi mất trong 1 khung. Vệt dash đông cứng 0,23 s rồi mất.
   - Sửa: `stop(i, fade = 0,18 s)` vẫn đẩy vị trí đầu cuối cùng (để đuôi co lại) và hạ alpha về 0.

6. **Thanh kiếm K2 nằm im ở đầu xa rồi biến mất.** `kiem.ts:1728–1731, 1791–1792`
   - Thấy: thanh kiếm cỡ ×1,7, tint 2,6, đứng yên cách 14 m trong 0,33 s rồi mất.
   - Sửa: cho trượt quá đích khoảng 0,5 m, giảm tốc, rồi giảm scale và tint về 0 trong 0,25 s.

7. **Đòn bay lật thẳng đứng lúc trúng** (mọi đòn thường và K1). `kiem.ts:1675–1677, 1635`
   - Thấy: `f.sx` bị ghi đè bằng vị trí mục tiêu, nên hướng lúc đứng trong vết thương thành (0, −0,4, 0). Thanh kiếm xoay 70–90° trong 1 khung, mũi đâm xuống dưới đất. Hướng −Y tuyệt đối còn làm roll ngẫu nhiên (`blades.ts:313`). Quái bị đẩy lùi còn kiếm thì đứng tại chỗ.
   - Sửa: lưu hướng bay cuối trước khi ghi đè, giữ hướng đó lúc tan, lùi lại 0,2 m và bám theo `T.x/T.z`.

8. **Xoay mặt tức thì.** `caster.ts:95–119`; `skills-main.ts:187`; `kiem.ts:1893`
   - Thấy: dash quay 90° trong 1 khung. K4 (mục tiêu −5, −7) quay 27°. Skill sau dash quay ngược 90°.
   - Sửa: yaw lò xo tắt hãm tới hạn khoảng 12 rad/s; lệch quá 60° thì xoay tại chỗ (§5.5).

9. **Ra đòn nhảy thẳng vào giữa clip, lúc gõ thân không động.** `caster.ts:77`; nạp ở `skills-main.ts:191–206`
   - Thấy: 0,25 s đầu (đoạn gồng) không bao giờ hiện. Thân đứng Idle suốt lúc gõ, rồi trong 80 ms đổi sang giữa đòn (lowerarm_r 68°, upperarm_r 50°; Ult calf_r 62°; Dash thigh_r 102°). Ult lowerarm_r 14,3°/khung so với đỉnh 6,2° của clip (×2,3).
   - Thấy thêm: chớp sáng ra đòn phát ở vị trí tay lúc còn Idle (cast chạy trước `mixer.update`), nên cánh tay vung đi còn chớp sáng ở lại.
   - Sửa: tua gồng theo tiến độ gõ (§5.6: `time = p·t_release`, `timeScale = 0`), ra đòn chạy tiếp từ `release`, phát VFX theo xương tay sau khi cập nhật mixer.

10. **Vầng sáng sau lưng bật và tắt phụt.** `kiem.ts:1431` (`if (a <= 0,01) return`); màu và alpha ở `1442, 1451, 1453`
    - Thấy: vầng 1,6 m ở 45 % độ sáng và đĩa sáng alpha 0,3 biến mất trong 1 khung, khoảng 0,37 s sau mỗi lần ra đòn. Ở phím đầu chúng hiện ngay ở 45 %.
    - Sửa: nhân alpha với `smoothstep(0, 0,3, a)`.

11. **Sigil hiện theo từng nấc phím, mép cứng.** `fxkit.ts:886, 901, 921, 949, 956–958` (`step`); `kiem.ts:1531, 1545, 1562, 1573, 1586` (tiến độ thô)
    - Thấy: đường K2 dài 14 m hiện theo 6 bước, mỗi bước khoảng 2,3 m, mép cắt cứng.
    - Sửa: làm mượt mức hiện về `p` (khoảng 12/s) và dùng mép mềm bằng `smoothstep`.

12. **Dash.** `kiem.ts:1889–1893`; clip ở `caster.ts`; `this.c` đọc ở `kiem.ts:1371`
    - Thấy: khung đầu đã đi 1,15 m (75 m/s), không có đà lấy trớn. Tư thế dash còn giữ 0,3 s sau khi đã đứng yên. Ấn, vầng sáng và đĩa sáng trễ 1 khung (tới 1,15 m) vì `this.c` được đọc trước `moveCaster`.
    - Sửa: easeInOut kèm 2 khung khom gồng, tua clip khớp 0,2 s di chuyển + 0,15 s hồi, cập nhật `this.c` sau khi di chuyển nhân vật.

13. **K5 lúc lao xuống.** `kiem.ts:2070` so với `2082`
    - Thấy: khoảng 100 thanh mỗi đợt chúi từ 14° xuống 63° trong 1 khung. Lúc cắm xong, hướng thành (0, −1, 0) đúng tuyệt đối, roll nhảy và mặt thép lóe chớp.
    - Sửa: nội suy hướng bằng `smoothstep(dive)`, giữ lệch tiếp tuyến tối thiểu 0,02 hoặc truyền roll rõ ràng.

14. **Hộ thân.** `kiem.ts:1814–1817, 1866–1880, 1808/1829`
    - Thấy: thanh đỡ đòn nhảy tới 2 m và xoay trong 1 khung. Khi hết lượt đỡ sớm, vòng chắn, xoáy (alpha 0,55), đĩa sáng và sigil tắt ở độ sáng tối đa (chỉ đường kết thúc sau 5 s mới có fade). Kiếm bật hiện đủ cỡ ở độ cao 5 m.
    - Sửa: di chuyển tới điểm đỡ bằng lò xo 50 ms; kết thúc sớm thì mờ dần 0,4 s; scale-in khi kiếm xuất hiện.

15. **K1.** `kiem.ts:1516, 521, 527`; thứ tự gọi `1375–1376`
    - Thấy: kiếm bật hiện đủ cỡ sau vai. Thanh 2 và 3 tắt mất 1 khung lúc phóng (bị ẩn rồi mới bay ở khung sau). Lúc phóng nhảy cao 0,55 m và xoay khoảng 90°. Chuyến bay 0,1 s chỉ có 6 mẫu cho khoảng 8 m.
    - Sửa: scale-in 0,12 s; đặt tư thế bay ngay trong khung phóng; bắt đầu bay từ tư thế đang hiển thị và quay hướng trong 30 % đầu đường bay.

16. **Phát lại cùng clip và listener trùng.** `caster.ts:73, 84, 87–91`
    - Thấy: đánh thường liên tiếp, hay hộ thân rồi K4 (cùng `skill2`), gọi `reset()` không crossfade nên tư thế giật. Mỗi lần `play` thêm một listener `finished`; lần `play('idle')` thứ hai gọi `setEffectiveWeight(1)` làm dừng fade, Idle bật vào cái một.
    - Sửa: hai action A/B cho mỗi clip; đăng ký một listener duy nhất trong `load()` và kiểm `e.action`.

17. **Capture bước cố định khác với chạy rAF.** `skills-main.ts:337–339` so với `355–363`
    - Thấy: capture luôn bước 1/60 s; chạy thật thì dt thay đổi, kẹp ở 50 ms, không có accumulator hay nội suy. Các thứ sinh theo khung (`kiem.ts:1661–1673` motes, `1734` tia lửa K2, `2088` lấp lánh K5) dày gấp đôi ở 120 Hz; ribbon ngắn một nửa. Giám khảo chấm ảnh 60 Hz trong khi chủ dự án có thể xem ở 120 Hz.
    - Sửa: bước cố định 60 Hz + nội suy khi vẽ (hoặc dùng tốc độ theo giây); chụp thêm một lượt rAF ở 120 Hz.

18. **Ribbon lấy mẫu theo khung.** `fxkit.ts:469–478` (18 điểm)
    - Thấy: đường vệt gãy khúc ở các chuyến bay nhanh. Trong hit-stop các điểm trùng nhau nên vệt co ngắn rồi dài lại.
    - Sửa: lấy mẫu theo thời gian thế giới, chia bước con có nội suy, lưu tuổi từng điểm.

19. **Ngôi sao ở mũi kiếm xoay ngẫu nhiên mỗi khung.** `kiem.ts:881`, gọi từ `1660` và `1733`
    - Thấy: sao 2–3 m đổi góc ±0,4 rad mỗi khung, nháy như đèn chớp.
    - Sửa: `rot = time·k` thay cho số ngẫu nhiên.

20. **Đèn chớp va chạm nhảy chỗ.** `src/kit/three/stage.ts:178–182` (kit, không được sửa), gọi từ `skills-main.ts:91–93`
    - Thấy: chỉ có một đèn điểm; mỗi lần chớp nó dời ngay sang chỗ mới và giữ cường độ lớn nhất, nên vùng sáng trên đất và quái nhảy (K1, K4).
    - Sửa (phía lab hoặc view): chỉ dời khi cường độ mới ≥ 0,5× hiện tại, hoặc tự quản 2–3 đèn.

21. **Quái đứng thế (chỉ trong lab nhưng có trong demo).** `herd.ts:237–239, 268–278, 255–263, 285–287`
    - Thấy: bị đẩy lùi 0,12–0,47 m trong 1 khung; chết thì teo tới 45 % rồi biến mất; hồi sinh và march thì dịch chuyển tức thời; khi march là tượng trượt, không có chân bước.
    - Sửa: đẩy lùi dạng vận tốc qua lò xo; teo về 0 bằng ease-in; hồi sinh có fade-in.

22. **K4.** `kiem.ts:1949–1961, 2007–2019, 1954`
    - Thấy: cột sáng ở các góc tắt cái một khi `out` qua 0,5; vòm và đĩa sáng (alpha 0,2) tắt ở `T_K4_LIFE`; kiếm bật hiện đủ cỡ ở 6,5 m.
    - Sửa: nhân với `out` hoặc fade 0,3 s.

23. **Rung camera và hit-stop.** `skills-main.ts:296–300, 285–289`
    - Thấy: rung chỉ là một nhịp 1–2 px giảm tuyến tính, kéo dài 2–8 khung, vào cái một, trông như giật hơn là rung. Hit-stop bật và tắt cứng ở 5 %, làm tròn theo khung (2 khung ở 60 Hz, 4 khung ở 120 Hz).
    - Sửa: lò xo tắt hãm (ω ≈ 35, ζ ≈ 0,35) nhận xung vận tốc, đổi đơn vị theo px; thoát hit-stop bằng ease trong 30 ms.

24. **Key 24 fps nội suy tuyến tính.** `lam.glb`
    - Thấy: vận tốc góc đổi gấp mỗi 41,7 ms, các động tác nhanh (25–40°/khung) có cảm giác máy móc.
    - Sửa: lấy mẫu lại 60 fps bằng nội suy cubic hoặc squad, làm offline (`QuaternionKeyframeTrack` của three không có chế độ smooth).

25. **Ấn K5 còn to ở skill sau.** `kiem.ts:1411–1412`
    - Thấy: `auraBig` không giảm khi rảnh, nên ấn và vầng sáng của skill sau K5 bắt đầu ở ×1,5 rồi co lại khoảng 0,2 s.
    - Sửa: cho giảm cả khi `p < 0`.

**Ghi chú**
- Các lớp nổ sáng nhất ngay khung đầu là đúng thiết kế (VFX_STANDARD §3.1 luật 5) nên tôi không tính là lỗi.
- Nhịp thân và hiệu ứng lệch nhau: clip Attack hết ở 0,58 s trong khi kiếm K1 thứ ba phóng ở +1,0 s; Ult hết ở 1,42 s trong khi đòn cuối K5 ở +2,0 s.
- Chưa có di chuyển thật: `Hero_Run` không được dùng, `moveTo` là dịch chuyển tức thời. Muốn có demo di chuyển cho chủ dự án thì phải làm locomotion trước (đi/chạy trộn theo tốc độ, xoay tại chỗ, dừng).
- Lõi HDR mảnh dưới 1 px (`kiem.ts:1347–1363`) có thể làm bloom lấp lánh. Điểm này chưa xác nhận, cần chụp kiểm.

### C. Kỹ thuật làm mượt và thông số khởi đầu

### Nghiên cứu: làm mượt chiêu thức và cử động nhân vật trong lab Kiếm (three.js 0.170)

#### 1. Kết luận chính

Trong lab hiện tại, đòn đánh bị giật chủ yếu do cách gọi clip, không phải do clip của Lam xấu. Tôi tìm ra 3 lỗi và đều đo được hoặc dựng lại được bằng script. Tôi không sửa file nào trong repo.

1. **Hết chiêu là nhân vật nháy về tư thế gốc trong 1 khung.** Lỗi nằm ở `LabCaster.play()` (`src/lab/caster.ts`). Clip chạy `LoopOnce` với `clampWhenFinished=false`, nên khi chạy xong thì three tự tắt action (`enabled=false`). Sự kiện `finished` lại gọi `crossFadeTo(idle)`, và idle bắt đầu từ trọng số 0. Tổng trọng số bằng 0 thì `PropertyMixer.apply` trộn về giá trị gốc của GLB (dòng 152–159 trong `three/src/animation/PropertyMixer.js`).
   - Tôi dựng lại bằng mô hình nhỏ, góc xương theo từng khung là: `… 33.4 32.5 0.0* 6.3 12.5 18.7 25.0 30.0` (dấu * là khung `finished` chạy).
   - Trên Lam, tư thế gốc lệch Idle tới calf_r 43°, lowerarm_r 39°, clavicle_r 34°. Cuối mỗi chiêu người xem sẽ thấy một khung A-pose.
2. **Phần lấy đà bị bỏ, và thân với VFX lệch nhịp.** Lab bắt đầu clip ở `min(0.3·dur, 0.25 s)`. Đỉnh tốc độ tay phải (thời điểm vung, đo bằng FK trên GLB):

   | Clip | Đỉnh tay phải | Ghi chú |
   |---|---|---|
   | Attack, Skill1 | 0,267 s | Lab bắt đầu gần như ngay lúc vung, pha lấy đà mất hết. Tư thế lúc 0,25 s lệch Idle 68° nhưng chỉ cross-fade trong 0,08 s, nên nhìn như giật. |
   | Skill2 | 0,708 s | Thân vung sau VFX khoảng 0,46 s. |
   | Ult | 1,083 s | Thân vung sau VFX khoảng 0,83 s. |
   | Dash | — | Khung đầu và khung cuối đều lệch Idle 104° (upperarm_r). |

3. **Một số lỗi giật nhỏ hơn:**
   - `face()` gán góc quay ngay lập tức, nên xoay 180° xảy ra trong 1 khung.
   - Gọi lại cùng một chiêu thì `reset()` nhảy thẳng về đầu clip.
   - Listener `finished` không kiểm tra `e.action`. Khi một chiêu bị ngắt, listener còn sót gọi `play('idle')` lần hai. Lần này `setEffectiveWeight(1)` gọi `stopFading()`, nên idle bật lên trọng số 1 ngay.
   - `fadeOut()` luôn chạy từ 1 về 0 (`_scheduleFading(duration, 1, 0)`), nên ngắt giữa một lần fade sẽ giật.
   - Trong game, `player-view.ts` xoay với tốc độ cố định 12 rad/s, nên lúc bắt đầu và lúc dừng xoay đều gắt.

Dữ liệu đúng khác với mô tả trong task: Lam có **31 khớp, không phải 25**. Trong đó có tail_01–05, ear_l/r và bag_r, rất hợp để gắn lò xo phụ. Clip có khóa ở khoảng 24 khung/s, nội suy LINEAR. Các kênh STEP đều là hằng số nên không gây giật.

#### 2. Kỹ thuật, nguồn và tham số khởi điểm

##### 2.1 `AnimationMixer.crossFadeTo` / `warp` và giới hạn

- **Cách hoạt động:**
  - `crossFadeFrom` gọi `fadeOut` cho clip cũ và `fadeIn` cho clip mới. Trọng số chạy theo đường thẳng (Interpolant tuyến tính của mixer), nên tư thế liền nhưng vận tốc gãy ở đầu và cuối lần fade.
  - `warp=true` đổi dần timeScale theo tỉ lệ độ dài hai clip. Nó dành cho hai chu kỳ đi bộ có độ dài khác nhau. Ví dụ chính thức `webgl_animation_skinning_blending` dùng `warp=true` và chờ sự kiện `loop` của clip cũ rồi mới fade (đi→chạy 2,5 s, chạy→đi 5 s).
  - `warp` vô ích cho đòn đánh.
- **Giới hạn:**
  - Mixer phải tính cả hai clip trong lúc fade.
  - Nếu tổng trọng số nhỏ hơn 1 thì phần thiếu bị trộn về tư thế gốc.
  - Fade nối tiếp nhau sẽ giật, vì `fadeOut` luôn bắt đầu từ 1.
  - Track quaternion không có nội suy mượt: `QuaternionKeyframeTrack.InterpolantFactoryMethodSmooth = undefined`.
- **Đo trên rig thử (một xương, chuyển 90° sang một clip đang chạy):**

  | Cách chuyển | Bước lớn nhất mỗi khung | Gãy gia tốc lớn nhất |
  |---|---|---|
  | crossFade 0,08 s | 19,5° | 15,3°/khung² |
  | Quán tính, half-life 0,06 s | 13,2° | 5,9°/khung² |

- **Nếu vẫn giữ cross-fade (chỉ cho chu kỳ di chuyển):**
  - idle↔walk 0,2–0,25 s, walk↔run 0,3–0,5 s kèm `warp`.
  - Clip một lần luôn đặt `clampWhenFinished=true`, và bắt đầu chuyển về idle trước khi clip hết, không đợi `finished`.

##### 2.2 Chuyển tiếp quán tính, cài cho từng xương (khuyên dùng cho mọi chiêu)

- **Ý tưởng (Bollo, GDC 2018, Gears of War 4):** bỏ trộn hai clip. Lúc chuyển, chuyển hẳn sang clip mới và lưu độ lệch giữa tư thế đang hiện trên màn hình và tư thế mới. Độ lệch này tắt dần như một bước hậu kỳ, nên chỉ phải tính một clip mỗi khung. Tôi chưa mở được slide của Bollo (Vault chỉ có trang mô tả), nên công thức dưới đây lấy theo Holden.
- **Dạng lò xo của Holden:**
  - Lúc chuyển: `off_x = (src+off) − dst`, `off_v = src_v − dst_v`.
  - Mỗi khung: `j1 = v + x·y`, `x = e^{−y dt}(x + j1 dt)`, `v = e^{−y dt}(v − j1·y·dt)`, với `y = 2·ln2/halflife`.
  - Với quaternion: `off = scaled_angle_axis(quat_abs(src·inv(dst)))`, rồi áp `q = exp(off)·q_anim` (nhân bên trái). Trong three là `bone.quaternion.premultiply(...)`.
  - Vận tốc góc lấy bằng sai phân khung: `log(abs(curr·inv(prev)))/dt`.
- **Biến thể:**
  - "Cubic inertializer" về đúng 0 tại `blendtime` (`d=x`, `c=v·T`, `b=−3d−2c`, `a=2d+c`). Hợp khi cần mốc kết thúc chính xác.
  - "Dead blending" ngoại suy tư thế cũ rồi trộn smoothstep, khoảng 0,2 s là thời gian trộn bình thường.
  - Unreal 5.8 có sẵn cả ba trong `SpringMath`, chứng tỏ đây là cách làm phổ biến trong ngành.
- **Thứ tự mỗi khung trong three:** `mixer.update` → bù quán tính → các lớp cộng (thở, giật lùi, nhìn theo) → IK chân → lò xo phụ → `updateMatrixWorld` → render.
- **Cách đọc half-life:** độ lệch còn dưới 5% sau khoảng 3,5 × half-life (đo: 0,04 s → 138 ms, 0,06 → 208, 0,08 → 275, 0,10 → 346, 0,15 → 517).

| Chuyển | Half-life | Ghi chú |
|---|---|---|
| Idle → nhả đòn (phím cuối) | 0,035–0,05 s | Nhanh nhưng không giật |
| Gõ → giữ pha gồng | 0,06 s | |
| Đòn → Idle | 0,08–0,10 s | Thay hẳn `finished` + crossFade |
| Dash bắt đầu / kết thúc | 0,04 / 0,08 s | |
| Trúng đòn | 0,03 s vào | Khớp §5.5 của CHARACTER_ANIMATION (0,08–0,25 s) |

##### 2.3 Lò xo tắt hãm tới hạn cho xoay, vị trí và nhìn theo (Holden; Driscoll)

- **Bộ giảm chấn chính xác:** `lerp(x, g, 1 − exp(−ln2·dt/halflife))`. `THREE.MathUtils.damp(x, y, λ, dt)` là cùng công thức với `λ = ln2/halflife` (Driscoll giải thích vì sao lerp hệ số cố định mỗi khung lại phụ thuộc fps).
- **Lò xo quaternion (Holden):** `x = exp(e^{−y dt}(j0 + j1 dt))·goal`, với `j0 = log(x·inv(goal))`.

| Lớp | Tham số |
|---|---|
| Xoay thân (yaw) | Logic quay ngay; phần hiển thị là lò xo tới hạn, half-life 0,05–0,07 s. Đo với 0,06 s: 180° xong 95% sau khoảng 12 khung (0,2 s), không vượt đà. VFX vẫn bắn theo hướng mục tiêu nên không phải chờ thân. |
| Vị trí hiển thị | Theo vị trí logic với half-life 0,03–0,05 s (chỉ cho phần dừng của dash). Đường dash tự thân giữ easing. |
| Đầu nhìn theo | Kẹp yaw ±40°, pitch ±20° (Unreal Locomotor mặc định `AngleMax` 30°). Chia head 0,6, neck 0,4, phần dư sang spine_03 0,2. |
| Đầu dẫn, hông theo sau | Half-life head 0,08–0,10, ngực 0,15, hông 0,20 s. Đầu dẫn trước, hông theo sau tạo chồng lớp tự nhiên. |
| Áp xoay lên rig Tripo | Trục cục bộ không rõ, nên xoay theo hệ thế giới: `L' = inv(P)·d·P·L`, với P là quaternion thế giới của xương cha (cần matrixWorld mới). |

##### 2.4 Khóa chân và IK hai đốt

- **Công cụ:**
  - `CCDIKSolver(mesh, iks)` của three nhận `target`, `effector`, `links` (có `rotationMin/Max`, `limitation`), `iteration`, `minAngle/maxAngle`.
  - IK giải tích của Holden (luật cosin, kẹp khoảng cách vào `[eps, l1+l2−eps]`, kẹp dot vào [−1, 1]) chính xác hơn và rẻ hơn. Trục gập nên lấy từ vector "đầu gối hướng tới" `d`, vì mặt phẳng hông–gối–gót không ổn định khi chân gần thẳng.
  - Xích của Lam: thigh → calf → foot (ball_* là mũi chân).
- **Tham số khởi điểm:**
  - Coi là chạm đất khi tốc độ bàn chân dưới 0,1–0,15 m/s và độ cao dưới 3–5 cm. Khi chạm thì khóa vị trí bàn chân.
  - Nhả khóa bằng bộ giảm chấn half-life 0,05–0,08 s.
  - `eps` = 1–2 cm. Hạ hông tối đa 4–6 cm để chân với tới.
  - Xoay tại chỗ: giữ hai chân khóa tới lệch 45–60° rồi mới đặt lại chân (§5.5 ghi > 60°).
- Sân lab phẳng, nên khóa chân chủ yếu chống trượt khi xoay và khi dừng dash. Theo §5.9 chỉ bật ở High/Ultra.

##### 2.5 Lò xo phụ: `@pixiv/three-vrm-springbone`

- **Gói:** bản 3.5.5, MIT, peer `three >=0.137`, chưa cài ở game nào. Dùng `new VRMSpringBoneJoint(bone, child, settings, colliderGroups)` trên xương thường, không cần file VRM, rồi `manager.addJoint` → `setInitState()` sau khi load → `update(delta)` mỗi khung → `reset()` khi bấm R.
- **Giá trị mặc định trong mã:** stiffness 1,0, gravityPower 0, gravityDir (0, −1, 0), dragForce 0,4, hitRadius 0. Spec VRM: dragForce trong 0–1, collider là cầu hoặc capsule. `center` dùng khi "rung quá mạnh lúc đi hay chạy": quán tính tính trong hệ center, trọng lực tính trong hệ thế giới.
- **Lưu ý quan trọng:** quán tính nhân `(1 − dragForce)` mỗi lần gọi, không nhân theo dt, nên kết quả phụ thuộc fps. Cần chạy bước cố định 60 Hz bằng accumulator. Hàm `update` cũng không tự kẹp delta lớn.

| Xương của Lam | Thiết lập khởi điểm |
|---|---|
| tail_01→05 | stiffness 1,2 giảm dần về 0,6 dọc xích; drag 0,35–0,45; gravity 0,2–0,4; hitRadius 0,04–0,06 |
| ear_l/r | stiffness 2,5–3,5; drag 0,5; gravity 0 |
| bag_r | stiffness 0,8; drag 0,3; gravity 0,6 |
| Collider | Cầu ở pelvis r 0,12–0,15; capsule ở hai đùi r 0,07 |
| `center` | Đặt là root, nếu không dash 0,2 s sẽ giật đuôi rất mạnh |

##### 2.6 Lớp cộng: thở, giật lùi, trúng đòn

- **Clip cộng:** `AnimationUtils.makeClipAdditive(clip, referenceFrame=0, referenceClip, fps=30)` chuyển clip sang dạng cộng (đặt `blendMode = AdditiveAnimationBlendMode`). Ví dụ chính thức đặt trọng số bằng `setEffectiveWeight`.
- **Thở (thủ tục):**
  - 0,2–0,3 Hz; spine_02/03 cúi ngửa 0,8–1,5°; clavicle nâng 0,5–1° theo nhịp hít; đầu bù ngược 0,3°.
  - Nhân với (1 − cường độ chiêu), tối thiểu 0,3. Lệch pha ngẫu nhiên.
- **Giật lùi khi nhả đòn:** lò xo dưới tới hạn (Holden: `stiffness = (2πf)²`, `damping = ratio·2√stiffness`).
  - spine_03 nghiêng ngược hướng đòn 4–8°, pelvis 1–2 cm.
  - f = 6 Hz, ζ = 0,5: vượt đà khoảng 16%, lắng khoảng 0,21 s.
  - f = 5 Hz, ζ = 0,6: vượt đà khoảng 9,5%, lắng khoảng 0,21 s.
  - Chạy bước cố định từ 120 Hz trở lên.
- **Trúng đòn:** hướng theo đòn, vào 0,03 s, ra 0,25 s (§5.5).

##### 2.7 Nội suy hiển thị cho sim bước cố định (Fiedler, "Fix Your Timestep!")

- Công thức: accumulator, kẹp frameTime ở 0,25 s, `alpha = accumulator/dt`, `state = cur·alpha + prev·(1−alpha)`. Thiếu bước này hình sẽ "rung nhẹ khó chịu".
- Game đã làm đúng (`src/app/loop.ts` có `timing.alpha`; `player-view.ts` lerp vị trí).
- Lab chạy dt biến thiên (kẹp 0,05 s): mixer và các lò xo exact dùng dt render được, còn lò xo phụ và giật lùi chạy bước cố định.
- Cần sửa trong game: thay xoay tốc độ cố định 12 rad/s bằng lò xo tới hạn (mục 2.3).

##### 2.8 Easing cho alpha và kích thước VFX để lớp không bật tắt đột ngột

- smoothstep `3x²−2x³` có đạo hàm bậc 1 bằng 0 ở hai đầu. smootherstep `6x⁵−15x⁴+10x³` (Perlin) có thêm đạo hàm bậc 2 bằng 0. Cả hai có sẵn trong `THREE.MathUtils`.
- easeOutBack của easings.net: `1 + c3(x−1)³ + c1(x−1)²`, `c3 = c1+1`. Vượt đà đo được: c1 1,70158 → 10%, 1,2 → 5,3%, 1,0 → 3,7%.
- `expImpulse(x,k) = h·e^{1−h}` với `h = k·x` (Inigo Quilez) lên nhanh, xuống chậm, đỉnh tại x = 1/k. k = 12 cho đỉnh ở 8% thời gian sống.

| Lớp | Tham số |
|---|---|
| Lóe (flash) | Được sáng nhất ở khung đầu (VFX_STANDARD §3.1 luật 5) |
| Lớp sống lâu (vòng, ribbon, trận đồ, kiếm bay) | Hiện dần 40–80 ms bằng smoothstep; tắt dần 100–150 ms trở lên bằng easeInCubic hay smootherstep |
| Kiếm bay hiện / ẩn | Kích thước 0→1 bằng easeOutBack (c1 1,0–1,2) trong 80–120 ms, không gán ma trận tức thì |
| Kiếm đổi hướng | Bộ giảm chấn quaternion, half-life 0,03–0,05 s |
| Kiểm tra | Alpha hay kích thước nhảy quá 30% trong một khung (ngoài lóe) là lỗi bật tắt, đúng luật mới trong game-vfx-layered |

##### 2.9 Game hành động kiểu anime làm đòn mượt thế nào

- **Nguyên lý (12 nguyên lý hoạt hình):** lấy đà, theo đà và chồng lớp (tóc, áo, đuôi tiếp tục chuyển động rồi kéo về), chậm vào chậm ra, đường cong, phóng đại, nén giãn giữ thể tích.
- **Smear frame:** khung trung gian kéo dài 1–2 khung, hoặc nhiều bản sao dọc đường đi. Trong 3D làm bằng giãn lưới có chủ ý.
- **Áp vào lab:**
  - **Lấy đà nằm trong lúc gõ.** Tua clip theo tiến độ gõ, đúng thiết kế §5.6: `time = đầu_gồng + tiến_độ × (release − đầu_gồng)`. Phím cuối thì chuyển sang `release` bằng quán tính. `release` đo được ở mục 1: Attack/Skill1 ≈ 0,27 s, Skill2 ≈ 0,71 s, Ult ≈ 1,08 s.
  - **Nhả nhanh, thu chậm.** Đoạn vung chạy timeScale 1,2–1,5, đoạn thu 0,85–0,9. Giữ dáng ở tư thế cực 30–60 ms.
  - **Thời gian dừng hình.** Genshin: kiếm N1/N2 dừng 0,03 s, bắn tên trúng đầu 0,12 s, thêm 0,06 s khi địch chưa vỡ thế. Lab đang dùng 30–70 ms là cùng cỡ.
  - **Cửa sổ hủy đòn.** God of War: hủy trước hay sau mốc trúng, và giữ lệnh chờ (buffer). Chiêu mới ngắt phần thu của chiêu cũ bằng quán tính, không reset clip.
  - **Vượt đà.** Cổ tay và cẳng tay vượt 5–10° bằng lò xo dưới tới hạn.
  - **Theo đà.** Đuôi, tai, túi qua lò xo phụ.
  - **Smear / bóng mờ.** 1–2 bản sao mờ dọc cung vung, alpha 0,35→0 trong 80–120 ms; vệt kiếm giãn dài ở đỉnh tốc độ.
  - **Lấy mẫu vệt.** Ở đỉnh vung, tay đi khoảng 0,9 m giữa hai khóa 24 khung/s, vận tốc gãy ở mỗi khóa. Ribbon nên lấy mẫu vị trí tay theo Catmull-Rom. Về lâu dài, nướng đoạn vung 60 khung/s với Bézier trong Blender.

#### 3. Thứ tự đề xuất cho lab (để sớm đạt 7 rồi gửi demo di chuyển)

1. Thay `crossFadeTo` + `finished` bằng quán tính từng xương, và đặt `clampWhenFinished=true`. Việc này bỏ cả khung A-pose, cú giật 68° và lỗi listener.
2. Xoay thân, vị trí dừng dash và đầu nhìn theo dùng lò xo tới hạn.
3. Tua pha gồng theo gõ; nhả ở `release` đã đo.
4. Lò xo phụ cho đuôi, tai và túi (bước cố định 60 Hz, `center` = root).
5. Thở và giật lùi bằng lò xo.
6. Easing cho kiếm bay, ribbon và vòng; kiểm luật 30%/khung.
7. IK hoặc khóa chân khi xoay tại chỗ.

Mỗi bước đo theo §5.11: vận tốc góc lúc chuyển không quá 1,5 lần đỉnh của clip, trượt chân không quá 0,05 m/s, cộng tờ khung 6 khung quanh mỗi lần đổi trạng thái.

**Chưa kiểm được:** slide của Bollo (Vault chỉ có trang mô tả); PDF bài nói Guilty Gear Xrd (máy chủ từ chối kết nối), nên tôi không dẫn chi tiết từ đó; video hitstop của Sakurai tôi chưa xem.

#### 4. Nguồn đã mở

- Holden: https://theorangeduck.com/page/spring-roll-call · https://theorangeduck.com/page/dead-blending · https://theorangeduck.com/page/creating-looping-animations-motion-capture · https://theorangeduck.com/page/propagating-velocities-through-animation-systems · https://theorangeduck.com/page/simple-two-joint
- Bollo GDC 2018: https://www.gdcvault.com/play/1025165/Inertialization · https://gamedeveloper.com/art/video-high-performance-animation-transitions-in-i-gears-of-war-i-
- Unreal: https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/Core/SpringMath · https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/Locomotor/FLocomotorHeadSettings
- three r170:
  - https://raw.githubusercontent.com/mrdoob/three.js/r170/docs/api/en/animation/AnimationAction.html
  - …/docs/api/en/math/MathUtils.html
  - …/docs/api/en/animation/AnimationUtils.html
  - …/docs/examples/en/animations/CCDIKSolver.html
  - …/examples/webgl_animation_skinning_blending.html
  - …/examples/webgl_animation_skinning_additive_blending.html
  - mã nguồn trong `node_modules/three@0.170.0/src/animation/`
- Driscoll: http://www.rorydriscoll.com/2016/03/07/frame-rate-independent-damping-using-lerp/
- three-vrm:
  - https://raw.githubusercontent.com/pixiv/three-vrm/dev/packages/three-vrm-springbone/package.json
  - …/src/VRMSpringBoneJoint.ts
  - …/src/VRMSpringBoneManager.ts
  - https://github.com/vrm-c/vrm-specification/blob/master/specification/VRMC_springBone-1.0/README.md
- Fiedler: https://gafferongames.com/post/fix_your_timestep/
- Easing:
  - https://en.wikipedia.org/wiki/Smoothstep
  - https://easings.net/ và https://github.com/ai/easings.net/blob/master/src/easings/easingsFunctions.ts
  - https://iquilezles.org/articles/functions/ (mở bằng curl)
- Hoạt hình và game hành động:
  - https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation
  - https://en.wikipedia.org/wiki/Smear_frame
  - https://gdcvault.com/play/1020049/Animation-Bootcamp-An-Indie-Approach
  - https://www.gamedeveloper.com/pc/combat-canceled-i-god-of-war-i-action-game-design
  - https://library.keqingmains.com/combat-mechanics/frames

#### 5. File nháp (không đụng repo)

Tất cả trong `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/`:

- `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/motion-sketch.ts` — `BoneInertializer`, `DampedYaw`, `criticalSpring`, `decaySpring`, `springStep`, `quatLog`/`quatExp`, `rotateBoneWorld`. Đã qua tsc strict với three 0.170.
- `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/test-sketch.ts` — so sánh cross-fade với quán tính, chạy bằng tsx.
- `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/test-finish.ts` — dựng lại cú nháy tư thế gốc.
- `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/release.mjs` — FK trên lam.glb: thời điểm nhả đòn và độ lệch với Idle.
- `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/glbinfo.mjs`, `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/glbstep.mjs`, `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/motion/glbstep2.mjs` — đọc xương, clip và kiểu nội suy của GLB.
