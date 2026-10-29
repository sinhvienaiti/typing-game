# Animation nhân vật dùng chung: kiểm kê, thiết kế, kế hoạch (29/10/2026)

Hệ animation nhân vật cho Dragonhold (`games/dragon-hold`), Wordwoven (`games/typing-defense`) và Last Line (`games/typing-survival`), đặt trong kit `shared/game-kit/`. Mức nhận theo `SHARED_SYSTEMS_BAR.md`: **hai giám khảo độc lập cùng chấm từ 9**, không hạng mục con nào dưới 8,5. Tài liệu này chỉ kiểm kê và thiết kế, không sửa mã.

## 0. Tóm tắt

| Mục | Nội dung |
|---|---|
| Hôm nay | Cao nhất 6,8 (tàu Last Line, sắp bị thay). Rồng và quái Dragonhold 5,2–5,9. Wordwoven chưa có nhân vật 3D nào trong game. Lightbearer của Last Line chưa có model. |
| Lỗ lớn nhất | Chuyển tiếp giữa các clip (3,5–4): mọi đòn, cú trúng và cú chết của quái bật về tư thế nghỉ trong một khung; Hỏa Long nằm rạp 70° trong một khung mỗi lần ra đòn. |
| Hướng thiết kế | Ưu tiên thư viện (§5.2): `AnimationMixer` của three.js, clip CC0 (Mesh2Motion, Quaternius), lò xo `@pixiv/three-vrm-springbone` (MIT). Phần ta tự làm: kit `anim/` (máy trạng thái, chuyển tiếp quán tính, sự kiện clip, đám đông skin trên GPU), Animation Lab, cách chấm. |
| Game đi trước | Dragonhold: game duy nhất có nhân vật 3D đang chơi, có đủ ba tầng (rồng, đám đông, lính ta), làn VFX cần sự kiện tung đòn ngay. Wordwoven thứ hai, phải xong trước khi làn C5 và C7 của 1C bắt đầu (03/11 và 06/11). |
| Bước đầu | Kit `anim/` lõi (chuyển tiếp quán tính, sự kiện, clip cộng có clip tham chiếu), sửa hai lỗi bật tư thế của Dragonhold, Animation Lab tối thiểu để chụp trước và sau. |

## 1. Luật áp

| Luật | Nguồn |
|---|---|
| Từ 9 với cả hai giám khảo, không hạng mục nào dưới 8,5; chủ dự án xem trực tiếp là cổng cuối | `SHARED_SYSTEMS_BAR.md` §2 |
| Tám hạng mục: chuẩn bị và theo đà, khối lượng, chuyển tiếp, bị đánh, chết, đi và đứng, đám đông lệch nhịp, đọc rõ ở camera chơi | `SHARED_SYSTEMS_BAR.md` §4 |
| Thư viện trước; mã MIT, BSD, ISC, Apache-2.0, MPL-2.0; tài sản CC0 hay CC-BY có ghi công; không GPL, NC, ND; kiểm giấy phép tại nguồn; tải tài sản cần chủ dự án đồng ý từng gói | `SHARED_SYSTEMS_BAR.md` §5, `THIRD_PARTY.md` |
| Tripo chỉ cho hình. Clip, chuyển động thủ tục, đám đông, VFX là của ta | quy tắc của chủ dự án |
| Sàn số mặt, bậc Ultra là file gốc | `MODEL_QUALITY.md` §2, §2b |
| Không thứ gì vẽ bằng mã thay cho hình thật | `AGENTS.md` |
| Đạn rời miệng ≤ 50 ms sau phím cuối; phần gồng chạy theo tiến độ gõ | `VFX_STANDARD.md` §3.1 luật 3 |
| Animation chỉ là phần nhìn: không đổi sim, không đổi thời điểm của sim, ván vàng giữ nguyên | `AGENTS.md` từng game |

## 2. Kiểm kê hôm nay

Đọc mã ở Dragonhold `main` (`1f1de48`), Wordwoven `a2-days` (`f9abfd0`), Last Line `main` (`79db628`), các worktree `.wt-dh-vfx` (`49aedee`), `.wt-dh-models` (`9db9d5e`), `.wt-td-1c` (`bc05e67`); xem tờ khung trong `tmp/` của các game.

### 2.1 Kit hôm nay (`shared/game-kit/three/`)

| Phần | Có gì | Thiếu |
|---|---|---|
| `Hero` (`hero.ts:97-352`) | Một `AnimationMixer`; ba vòng lặp Idle, Fly, Boost trộn theo trọng số (`animate`, `:325-353`); clip một lần (`play`, `:247`) với fade vào/ra cố định; tùy chọn `additive` (`:73`, dùng `makeClipAdditive` không có clip tham chiếu ở `:155`); bảng `release` (`:270`); lò xo knock khi trúng (`:303-307`); nhún theo nhịp cánh (`:308-318`); tô màu trúng, phát sáng, tan kiểu hash (`setLook`) | Sự kiện clip, máy trạng thái, chuyển tiếp quán tính, nhìn theo mục tiêu, lò xo phụ, IK, clip tham chiếu cho clip cộng |
| `createGuideScene` (`guide-scene.ts:98-207`) | Idle lặp, hành động `crossFadeFrom` 0,18–0,35 s | Như trên |
| Hợp đồng model (`model-contracts.ts:43-127`) | Tên clip theo loại (`Hero_*`, `Enemy_*`, `Unit_*`, `Boss_*`, `Guide_*`, `Prop_*`), socket `FX_*` | Bộ clip tối thiểu theo họ xương, sự kiện, metadata chuyển tiếp |
| `feedback/` (`reaction.ts`, `hitstop.ts`) | Lóe trắng 1–4 khung, đẩy lùi giả theo hướng đòn, nén 0,91 / giãn 1,07 trong 120 ms; hit stop theo hồ sơ game | Phản ứng ở mức xương |
| Đám đông skin trên GPU | **Không có trong kit**: chỉ ở Dragonhold (`crowd.ts`, `crowd-rig.ts`, `motion.ts`) | — |

### 2.2 Dragonhold

| Nhân vật | Rig | Clip | Lớp thủ tục | Chuyển tiếp | Trúng, chết, ra quân | LOD |
|---|---|---|---|---|---|---|
| **Hỏa Long** (`heroes.ts`, GLB `draconis-v2`) | Rig Space từ `--rig-json`, `make_flight_clips` (`scripts/models/blender/space_typing_model_tools.py:1351`) | `Hero_Idle_Hover`, `Attack_L/R/Both`, `Cast`, `Hit`, `Death`, `Victory` (`heroes.ts:50-59`) | Kit `Hero`: nhún, knock, xoay neo về quái 5,5 rad/s (`:331`), không nghiêng khi xoay | Clip đánh phát **không cộng** (`:214-222`), fade vào 0,04 s | Hit khi đòn ≥ 20 (`:428-430`); Death giữ; không có ra quân | Không; Low dùng khối tạm |
| Hỏa Long, làn VFX (`.wt-dh-vfx/src/view/heroes.ts`) | như trên | Clip "strike" cắt từ khung tung đòn (`FIRE_RELEASE_S` `:73`, `strikeClip` `:99`) | **Gồng theo gõ**: cổ, đầu, ngực ngả tới 0,2 rad theo phần đã gõ (`COIL` `:82`, `pose` `:427`); đầu giật lò xo khi nhả (`:562`); dải lửa ở đầu cánh (`:444`) | Như trên | Như trên | Không |
| **Bạch Long** (`heroes.ts:267-318`, `draconis-v4`) | Rig Space, `make_guide_clips` | `Guide_Idle`, `Wave`, `Talk`, `Flap` | Không | `crossFadeFrom` 0,18–0,35 s | Không phản ứng | Không |
| **Quái** Moss Grunt, Moss Archer, Blight Wolf, Tusk Boar, Thorn Wasp, Thorn Ant (`model-specs.ts:282-289`) | Tripo không xương; **xương viết bằng mã** theo họ (hai chân, bốn chân, bay, sáu chân), đặt theo mốc đo trên ảnh chiếu, trọng số theo khoảng cách tới đoạn xương (`crowd-rig.ts:101-200`, `skinWeights` `:802`) | Tư thế viết bằng hàm sin và smoothstep (`bipedClips` `:204`, `quadClips` `:468`, `flyerClips` `:578`, `antClips` `:653`): Idle, Move, Run, Attack, Hit, Death; nướng vào texture xương (`bakeRig` `:1010`), nâng thân để chân không lún (`sinkOf` `:983`) | Lóe, đẩy lùi, nén từ kit `Reactions`; lắc khi choáng (`actors.ts:562`); bóng mờ, viền tối, bóng xuyên tường (`crowd.ts:747-830`) | Mỗi con 2 clip (A, B, trộn); **trộn tuyến tính ma trận** (`crowd.ts:191-192`); bước đi khớp tốc độ (`motion.ts:113-141`) | Hit là lớp B trọng số 0,9 trong 0,35 s (`motion.ts:170-175`); Death của họ rồi tan 0,4 s (`actors.ts:610-616`); ong rơi xoáy; **ra quân: hiện ra ngay**, chỉ có vòng VFX ở làn VFX | Không có LOD nhân vật; làn models dùng lưới Medium cho viền và bóng (`.wt-dh-models/src/view/crowd.ts`) |
| **Moss Bannerman** (G01) | Hai chân + cán cờ, lá cờ | Thêm Intro (phất cờ), Cast (cắm cờ), Death (quỳ, gập, cờ gãy) (`crowd-rig.ts:350-465`) | Cờ đung đưa viết trong clip | Như quái | Chìm vào rêu, nhuộm rêu khi chết (`actors.ts:618-624`) | Không |
| **Moss Warden** (lính ta) | Hai chân, `ours` | Block, Down, Rise thêm vào (`crowd-rig.ts:390-422`) | Khối "nụ" khi ngã | Như quái | Khuỵu rồi **thu cỡ về 0,4 trong một khung** (`actors.ts:663`) | Không |

Lệch nhịp: mỗi con một pha ngẫu nhiên (`actors.ts:191-202`, `motion.ts:56`), nhịp bước theo tốc độ thật. Cùng biên độ, cùng thời lượng, một biến thể mỗi họ.

### 2.3 Wordwoven

| Phần | Hôm nay |
|---|---|
| Trong game (`a2-days`) | View 2D canvas (`src/view/debug-2d.ts`): quái là chấm mực, Thư Đồng là đĩa có chữ, Draconis là tam giác có cánh (`:714-741`). Mộc Tinh 2D có chuẩn bị và vượt đà (ngả sau trước Quật cành, nhún và nén khi bước, tán lá trễ nhịp; `boss-2d.ts:309-356`). **Không nhân vật 3D nào.** |
| View 3D 1C (`.wt-td-1c/src/view/3d/`) | Sân, camera, đường, suối, nhà, thẻ chữ. Chưa có nhân vật. Kế hoạch: `heroes.ts` (C5, C8, làn L2 từ 03/11), `units.ts` đám đông instanced (C7, làn L3 từ 06/11); ≤ 8 nhân vật có xương mỗi khung ở High (`docs/td/BUILD_1C_MAP1.md` §6, §7); VAT và rig Draconis P18 để sau (§1) |
| Đường ống Blender (`scripts/models/blender/td_rig_*.py`, 4.456 dòng; preset `scripts/models/presets/td-rigs/*.json`) | Đủ nhất trong ba game: xương người Mesh2Motion, clip CC0 chuyển sang xương model (`td_rig_clips.py`), clip viết bằng khóa và bằng mã cho khối mềm, rắn (`td_rig_creatures.py`), khóa chân IK, giữ đầu, độ chúi đều, lò xo nướng cho đuôi, tai, vạt áo, xích về Idle cuối clip (`td_rig_post.py`), sự kiện clip (`land`, `takeOff`, `impact`, `split`, `spit`), metadata GLB `td_clips` (loop, seconds, `crossfade_s`, events) và `td_lookAt` (`td_rig_attach.py:13, 83`), bảng kiểm trượt chân, giãn lưới, mối nối vòng lặp (`td_rig_review.py`) |
| Đã dựng (24/10) | Lam, Cương Thi, Lính Giáo, Tanuki, Troll, Nuppeppō, Thuồng Luồng, Mầm Gỗ, cú Thư Đồng chung cho Chấm, Phẩy, Gạch (13 clip). **Mộc Tinh chỉ có `Boss_Idle`.** Mọi preset `reviewed: false`. Người làng chưa có rig. Draconis dùng tạm `draconis-v2` của Space |

Tờ khung ở `~/AudioLab/work/_td-models/rig/<id>/contact.png`. Lính Giáo đọc tốt (đâm giáo có bước lao, ngã ngồi, giáo rơi). Cú Thư Đồng: Idle, Walk, Scared, Assist gần giống nhau ở camera 55°, biên độ nhỏ.

### 2.4 Last Line

| Nhân vật | Hôm nay |
|---|---|
| **Tàu** (`src/view/ship.ts`) | Kit `Hero` với `Ship_Idle` (Vanguard) hay `draconis` (`:116-126`, `bob: false`); mọi chuyển động là lò xo thủ tục của `ship-rules.ts`: trôi theo phía bầy ép, nghiêng khi trôi, xoay về đòn nặng nhất, giật lùi theo súng, lao 0,35 m khi nạp từ, lơ lửng (`springStep` `:204, 225`). Có bản giảm chuyển động. **Hướng B thay tàu bằng Lightbearer.** |
| **Lightbearer + hai súng canh** | Chưa có model. Bible đòi clip: đứng, lướt trái phải, giơ tay bắn trái, bắn phải, bị đánh, quỳ, đứng dậy, thắng; áo choàng cần xương phụ hay shader vải (`ART_DIRECTION_2026-10-28.md` §4.2, §4.3) |
| **Bầy** (`src/view/crowd.ts`) | Model cứng (họ "rainbow" của Space, chỉ có Idle), một `InstancedMesh` mỗi loại; mọi động tác nằm trong ma trận từng con (`:246-270`): nhìn tàu, chúi theo tốc độ, nhún, lắc, Trâu và Đầu Đàn bước nặng 1,1 Hz, Khiên khom, Tách run 2 Hz, kéo méo chậm; trúng: lóe, lùi theo `FLINCH` từng loại, nén; chết: giữ 3 khung trắng nóng (`DEATH_FLASH` `:51`, `ghost` `:295`) rồi mảnh vỡ (`chunks.ts`). **Ra quân: hiện ra ngay** |

### 2.5 Lỗi tìm thấy

| # | Lỗi | Chứng cứ | Sửa (§5) |
|---|---|---|---|
| L1 | **Hỏa Long nằm rạp trong một khung mỗi lần ra đòn.** Clip `Hero_Attack_*`, `Hit`, `Cast` của `make_flight_clips` dựng quanh tư thế lướt G0 (thân nghiêng 70°, `space_typing_model_tools.py:1472`) để phát **cộng** trên vòng Fly. Dragonhold phát chúng đủ trọng số trên `Hero_Idle_Hover` (thân 4°) với fade 0,04 s | Mã `heroes.ts:214-222` (không `additive`); tờ khung `.wt-dh-vfx/tmp/vfx/judge-r4/s-1080-light-strike-zoomA.jpg`: khung a-04 đứng thẳng, f000 nằm ngang | Đánh dấu `additive` cho Attack, Hit, Cast (đúng như Space phát chúng). Clip strike của làn VFX cần clip gốc làm tham chiếu (`makeClipAdditive(strike, 0, original)`): kit `Hero` chưa nhận tham số này (P1) |
| L2 | **Quái bật về tư thế nghỉ ở mọi đòn, cú trúng, cú chết.** `Motion.write` đặt clip một lần vào lớp A với trộn 0 (`motion.ts:145-155`); khung 0 của Attack, Death là tư thế nghỉ (`crowd-rig.ts:297-320, 445-460`). Hit vào lớp B ngay ở 0,9 (`motion.ts:173`) mà khung 0 của Hit cũng là nghỉ (`crowd-rig.ts:278`): chân đang bước ±24° nhảy về 0 trong một khung | Mã; tờ `dragon-hold/tmp/mac-2026-10-27/m0b/samples/grunt-1280x720.png` (Hit 0,08 s gần như nghỉ) | Chuyển tiếp từ tư thế đóng băng (§5.5) |
| L3 | Làn VFX bỏ phần gồng của clip (clip bắt đầu ở khung tung đòn); gồng thay bằng ba xương xoay ≤ 0,2 rad. Thân, cánh, tay không gồng | `.wt-dh-vfx/src/view/heroes.ts:73-117, 427-441` | `anim/charge.ts`: tua phần gồng thật của clip theo tiến độ gõ |
| L4 | Trộn tuyến tính hai ma trận xương: hai tư thế khác xa (đi sang chết) làm thân co lại giữa chừng | `crowd.ts:191-192` | Texture xương lưu quaternion và tịnh tiến, trộn nlerp |
| L5 | Clip quái viết bằng hàm: mọi chuyển động dùng smoothstep cân hai đầu, không vượt đà, không lắng; Heo và Sói cùng nhịp chỉ khác biên độ | `crowd-rig.ts:82-90` và các clip | Clip CC0 chuyển xương + clip khóa trong Blender (§5.3) |
| L6 | Lính ta khi ngã thu cỡ 0,55 → 0,4 trong một khung | `actors.ts:663` | Clip Down giữ, tỉ lệ qua lò xo |
| L7 | Không con nào ra quân bằng thân (Dragonhold, Last Line); không biến thể chết theo hướng đòn | `actors.ts:500-540`, `typing-survival/src/view/crowd.ts` | Trạng thái Spawn, Death có biến thể (§5.4) |
| L8 | Bậc Ultra (làn models) skin lưới gốc Tripo bằng trọng số tính lúc nạp theo khoảng cách: tốn thời gian nạp, vùng nách và áo choàng dễ rách | `crowd-rig.ts:802`; `.wt-dh-models` commit `92e16a3` | Trọng số từ Blender (bone heat), làm trên lưới gốc rồi giảm mặt giữ nhóm đỉnh |

## 3. Điểm hôm nay

Điểm của trưởng thiết kế, đọc mã và tờ khung có sẵn, **không thay giám khảo độc lập**; là mốc xuất phát. A chuẩn bị và theo đà, B khối lượng, C chuyển tiếp, D bị đánh, E chết, F đi và đứng, G đám đông lệch nhịp, H đọc rõ ở camera chơi. "—" là không áp.

| Nhân vật | A | B | C | D | E | F | G | H | TB |
|---|---|---|---|---|---|---|---|---|---|
| Hỏa Long (`main`) | 4 | 5 | 3,5 | 5 | 5,5 | 6,5 | — | 7 | 5,2 |
| Hỏa Long (làn VFX, gồng theo gõ) | 6 | 5,5 | 3,5 | 5 | 5,5 | 6,5 | — | 7,5 | 5,6 |
| Bạch Long | 5 | 5 | 7 | — | — | 6,5 | — | 6 | 5,9 |
| Quái DH (Grunt, Archer, Wolf, Boar, Ant) | 6 | 5 | 4 | 6 | 6 | 6,5 | 6,5 | 7 | 5,9 |
| Thorn Wasp | 5,5 | 4,5 | 4 | 5,5 | 6 | 6 | 6 | 6,5 | 5,5 |
| Moss Bannerman | 6,5 | 5 | 4 | 6 | 6,5 | 6 | — | 7 | 5,9 |
| Moss Warden | 5 | 5 | 4 | 5,5 | 5 | 6 | — | 6 | 5,2 |
| Wordwoven trong game | không có nhân vật 3D | | | | | | | | — |
| Lính Giáo (Blender, chưa vào game) | 6,5 | 6,5 | — | 6 | 6,5 | 7 | — | 6 | 6,4 |
| Cú Thư Đồng (Blender, chưa vào game) | 5 | 5 | — | 5 | — | 5,5 | — | 5 | 5,1 |
| Tàu Last Line (sẽ bị thay) | 6,5 | 7 | 7 | 6,5 | — | 7 | — | 7 | 6,8 |
| Bầy Last Line | 4 | 6 | 6 | 6,5 | 5,5 | 6 | 7 | 7 | 6,0 |
| Lightbearer, súng canh | chưa có | | | | | | | | 0 |

Khoảng cách tới 9: lớn nhất ở C (3,5–4), rồi A ở rồng (4), B (4,5–5), D và E (5–6). F, G, H ở 6–7.

## 4. Mốc thương mại (theo nguyên tắc, không chép)

| Nguyên tắc | Game cho thấy | Mục tiêu đo được của ta |
|---|---|---|
| Tư thế rõ ở cỡ nhỏ, phóng đại | Kingdom Rush, Warcraft III | Tư thế gồng và tư thế ra đòn khác bóng dáng ≥ 15 % số điểm ảnh của thân ở camera chơi (quái DH 20–40 px, lính TD 28 px) |
| Gồng chậm, ra đòn nhanh, giữ, thu | Hades, StarCraft II (khung sát thương gắn khung clip) | Khung cuối gồng tới tư thế chạm ≤ 3 khung 60 Hz; thu ≥ 2 lần thời gian ra đòn; vượt đà 5–12 % rồi lắng |
| Khối lượng | Monster Hunter, Diablo IV | Con nặng: chân chạm làm thân lún 2–6 % chiều cao, lắng 0,25–0,4 s, bụi và rung nhẹ; con nhẹ: nảy nhanh, lắng ≤ 0,15 s |
| Chuyển tiếp không bật | mọi game hành động hiện đại (trộn quán tính) | Không khung nào có vận tốc góc của xương ở lúc chuyển vượt 1,5 lần vận tốc lớn nhất của chính clip |
| Bị đánh theo hướng | Diablo IV, Hades | Thân giật ra xa hướng đòn; bậc nặng: loạng choạng toàn thân 0,4–0,6 s |
| Chết đa dạng, có va đất | Diablo IV, They Are Billions | ≥ 2 biến thể mỗi họ, ngã xa hướng đòn, sự kiện chạm đất (bụi, tiếng), nằm 0,3–0,6 s trước khi tan |
| Đám đông lệch nhịp | Total War, They Are Billions | Pha, tốc độ ±8 %, biên độ ±10 %, biến thể Idle; < 10 % cặp hàng xóm cùng loại trùng pha quá 1 s |
| Vật phụ theo đà | Destiny (áo choàng, Ghost bay), rồng của Monster Hunter | Đuôi, áo choàng, cánh, cờ, tán lá trễ 2–6 khung, không xuyên thân |
| Rồng có nhịp cánh nâng thân | Monster Hunter, Spyro | Thân nhô lên sau mỗi nhịp đập xuống, đầu giữ ổn định |

Giám khảo xem clip tham chiếu trên máy, không lưu vào Git, không phát lại cho ai.

## 5. Thiết kế hệ dùng chung

### 5.1 Ba tầng nhân vật

| Tầng | Ai | Cách chạy | Lý do |
|---|---|---|---|
| **H — nhân vật chính** | Hỏa Long, Bạch Long, Draconis, Mộc Tinh, Lightbearer (súng canh là vật cứng theo lò xo) | `SkinnedMesh` + `AnimationMixer` trên CPU, đủ lớp thủ tục, lò xo phụ, IK | Ít con (≤ 8–12), gần camera, cần đẹp nhất |
| **C — đám đông có xương** | Quái, lính, người làng, Thư Đồng, cây luật | Texture xương nướng sẵn, skin trong shader của `InstancedMesh`, CPU chỉ chọn clip và thời gian | 100–400 con, vài draw call (cách của Dragonhold hôm nay, đo 220 con 5,93 ms cả khung ở High) |
| **R — bầy cứng** | Bầy Last Line (Hollow Swarm giữ lưới cứng) | Ma trận từng con + biến dạng trong shader (rung, nứt sáng theo nhịp) | Đến 700 con, model không có chi |

### 5.2 Chọn thư viện trước (kiểm giấy phép tại nguồn, 29/10)

| Thành phần | Chọn | Giấy phép (nguồn) | Cỡ | Hợp với Tripo và rig của ta | Chủ dự án cần |
|---|---|---|---|---|---|
| Máy chạy clip, clip cộng, sao chép skin, chuyển clip lúc chạy, IK CCD | three.js `AnimationMixer`, `AnimationUtils.makeClipAdditive` (có tham số clip tham chiếu), `SkeletonUtils.clone` và `retargetClip`, `CCDIKSolver` | MIT (`node_modules/three/LICENSE`, 0.170.0 ở cả ba game) | Đã trong gói | Lõi của tầng H. Chuyển clip làm ở Blender là chính; `retargetClip` lúc chạy chỉ cho Lab | Không |
| Xương và clip CC0 theo họ | **Mesh2Motion** (`github.com/mesh2motion/mesh2motion-app`): rig người, chim, rắn (đã có ở `games/typing-defense/art-src/anim/mesh2motion/`, dùng từ 24/10); thêm rồng, cáo, ngựa, nhện, kaiju | Tài sản CC0 (`LICENSE-CC0.MD`: "All 3d models, blend files, rigs, animations"), mã MIT | Người base 5,7 MB, addon 5,3 MB (đã có); rồng 0,75, cáo 0,79, ngựa 1,09, nhện 0,60, kaiju 1,05 MB | Người → Lightbearer, người làng, lính, Grunt, Archer, Bannerman, Warden; cáo → Blight Wolf; ngựa → Tusk Boar; nhện → Thorn Ant (bỏ một cặp chân); kaiju → Troll, Mộc Tinh; rồng → thử cho Hỏa Long. **Không dùng** `human-mocap-animations.glb` và thư mục `CarnegieMellonAnimations` (dữ liệu CMU, `readme.txt` trỏ tới một gói itch.io: giấy phép chưa kiểm) | Đồng ý tải 5 file rig + 5 file clip (~4,3 MB) |
| Clip người CC0 nhiều hơn | **Quaternius Universal Animation Library** bản Standard (120+ clip: đi 8 hướng, chạy, chiến đấu, súng, chết, biểu cảm) | CC0 (trang `quaternius.com/packs/universalanimationlibrary.html`) | Trang không ghi; đo khi tải | Bổ sung cho Lightbearer (bắn, bị đánh, quỳ), lính | Đồng ý tải bản Standard (miễn phí); bản Source trả phí, không cần |
| Clip cận chiến, nông, xác sống | **Quaternius Universal Animation Library 2** bản Standard (130+: combo cận chiến chia từng đòn, nông trại, đi kiểu xác sống) | CC0 (trang `.../universalanimationlibrary2.html`) | Trang không ghi | Lính cận chiến, người làng ở Rice Field, Moss Grunt đi lê | Đồng ý tải bản Standard |
| Lò xo phụ (đuôi, áo choàng, cánh, cờ, tán lá) | **`@pixiv/three-vrm-springbone`** 3.5.5 | MIT (`LICENSE` của repo `pixiv/three-vrm`, `package.json`), peer `three >= 0.137` | npm 0,42 MB chưa nén (nhiều bản build); đo gzip khi cài | `VRMSpringBoneJoint(bone, child, settings)` nhận mọi `Object3D`: dùng được trên xương của ta, không cần file VRM. Chỉ tầng H; tầng C nướng lò xo ở Blender (đã có ở Wordwoven) | Không (cài gói mã là việc thường ngày) |
| Rút gọn, lấy mẫu lại clip sau Blender | **glTF-Transform** `@gltf-transform/functions` 4.5.1 (`resample`, `dedup`, lượng tử hóa) | MIT (`LICENSE.md` của repo) | Chỉ trong script, 0 byte lúc chạy | Bước cuối của đường ống, trước manifest | Không |
| Skin instanced có LOD, cull từng con | `@three.ez/instanced-mesh` 0.3.16 | MIT, peer `three >= 0.159` | npm 0,87 MB | Skin bằng mixer CPU cho từng con (`setBonesAt`): đắt hơn texture xương của ta khi > 200 con. **Chưa chọn**; xem lại nếu cần cull hay LOD trên 400 con | Không |
| Clip người từ dịch vụ | Mixamo (Adobe) | Bài FAQ của nhân viên Adobe (cộng đồng Adobe, 29/09/2022): miễn phí, không phí bản quyền cho game; **cấm phân phối file thô**; không cần ghi công; cấm dùng huấn luyện máy học. Trang FAQ chính thức từ chối truy cập (403) nên chưa kiểm được bản hiện hành | — | Phải tải model Tripo lên Adobe; game web phát GLB công khai, gần với "file thô". **Không dùng mặc định**; chỉ khi CC0 thiếu một clip, chủ dự án đọc điều khoản hiện hành trong tài khoản và quyết | Quyết định nếu cần |
| Nướng VAT trong Blender | OpenVAT | Add-on GPL-3.0 (tác giả nói đầu ra tự do), shader cho engine MIT; theo trang tác giả, chưa đọc `LICENSE` của repo | — | Không cần: ta tự nướng texture xương; bầy cứng không cần VAT. **Không dùng** | Không |
| Nhân vật động CC0 | Kenney Animated Characters 1–3 | CC0 (trang Kenney) | 8 file mỗi gói | Clip gắn với nhân vật của Kenney, trang không liệt kê clip; ít giá trị cho model Tripo. **Không dùng** | Không |
| Phần mềm dựng | Blender, gồm bone heat và Rigify | GPL (công cụ, không phát hành; đầu ra là của ta) | — | Đã dùng ở cả hai đường ống | Không |

Tự làm (không có thư viện vừa): máy trạng thái theo bảng, chuyển tiếp quán tính, sự kiện clip, texture xương và shader đám đông (mở rộng của Dragonhold), tua gồng theo gõ, Animation Lab. Sổ giấy phép: `THIRD_PARTY.md`.

### 5.3 Đường ống clip

| Bước | Làm gì | Công cụ |
|---|---|---|
| 1. Model | GLB Tripo không xương, tư thế A, khe hở giữa tay và thân, áo choàng không dính chân, mức mặt cao nhất (`MODEL_QUALITY.md` §2). **Không dùng auto rig của Tripo**: đo 24/10 trên Lam, 14.071/14.132 đỉnh dính cứng vào `Hips` (`typing-defense/scripts/models/README.md`) | Chủ dự án trên web Tripo |
| 2. Xương | Họ xương Mesh2Motion (người, cáo, ngựa, nhện, chim, rắn, rồng, kaiju) đặt theo mốc lưới; xương phụ cho đuôi, áo choàng, cánh, cờ, tán lá; trọng số bone heat trong vùng, khóa vùng cứng (đầu, mũ, giáp) | Đưa `td_rig_tools.py`, `td_rig_survey.py` của Wordwoven lên repo cha thành `scripts/models/blender/rig/` (công cụ chung như `static_model_tools.py`); mỗi game giữ preset của mình |
| 3. Clip | Chuyển clip CC0 sang xương model; clip khóa cho đòn riêng (Quật cành, Cắm Cờ, đòn chữ của rồng); clip viết bằng mã cho khối mềm, rắn | `td_rig_clips.py`, `td_rig_creatures.py` (lên repo cha) |
| 4. Hậu kỳ | Khóa chân IK, giữ đầu nhìn thấy mặt, độ chúi đều, lò xo nướng, xích về Idle cuối clip, tốc độ mặt đất | `td_rig_post.py` |
| 5. Metadata | Extras GLB `anim` (mở rộng `td_clips`): `loop`, `seconds`, `crossfade_s`, `events` (tên → giây), `contacts` (khung chân chạm), `rootSpeed_mps`, `release_s`, `variant`, `mask` | `td_rig_attach.py` |
| 6. Kiểm | Tờ khung trước, cạnh, camera chơi; trượt chân, giãn lưới, mối nối vòng lặp, xuyên đất | `td_rig_review.py`, `td_rig_compare.py` |
| 7. Tầng | Rig trên lưới gốc (Ultra) rồi giảm mặt giữ nhóm đỉnh cho High, Medium, Low; lưới viền và bóng mờ giữ cùng chỉ số xương | `scripts/models/m0b-tiers.mjs` (làn models) gọi sau bước 6 |
| 8. Đóng gói | Lấy mẫu lại 30 khung/s (cánh 60), bỏ khóa thừa, lượng tử hóa | glTF-Transform, `pnpm models:prepare` |

Rồng: giữ rig Space (`make_flight_clips`, `make_guide_clips`); thêm bộ clip Dragonhold dựng quanh tư thế Hover (đòn chữ ba hướng, Sky Fire, Long Hống, Hit trước và bên, Death trên bệ, Intro bay xuống bệ). Quái Dragonhold: chuyển từ xương viết bằng mã sang rig Blender khi clip mới qua Lab; bộ nướng `bakeRig` nhận GLB có xương nên phần chạy không đổi. Xương viết bằng mã giữ làm đường lùi.

### 5.4 Hợp đồng clip theo họ

| Nhóm | Bắt buộc | Nên có | Sự kiện bắt buộc |
|---|---|---|---|
| Đi đất (người, bốn chân, sáu chân) | `Idle`, `Idle.b`, `Walk`, `Run`, `Attack` (gồng, nhả, thu trong một clip có mốc), `Hit.front`, `Hit.back`, `Death.a`, `Death.b`, `Spawn` | `Idle.fidget`, `Turn.l/r`, `Stagger`, `Victory`/`Cheer`, `Attack.b` | `foot_l`, `foot_r` (bốn chân: `foot_fl/fr/bl/br`), `windup_end`, `release`, `recover`, `fall_impact` |
| Bay (ong, chim, Alicanto) | `Fly`, `Attack`, `Hit`, `Death` (cánh gập), `Spawn` | `Hover`, `Dive` | `wing_down`, `release`, `fall_impact` |
| Rồng (H) | `Hover`, `Hover.b`, `Attack.l/r/both`, `Cast`, `Roar`, `Hit.front/side`, `Death`, `Intro`, `Victory` | `Turn.l/r`, `Land`, `TakeOff` | `wing_down`, `release`, `breath_start/end` |
| Người chính (Lightbearer, Draconis người) | `Idle`, `Strafe.l/r`, `Cast.l/r` (giơ tay bắn), `Hit.front`, `Kneel`, `Rise`, `Victory`, `Death` | `Idle.fidget`, `Cast.both`, `Load` (nạp từ) | `foot_*`, `release`, `kneel_impact` |
| Boss (Mộc Tinh) | `Idle`, `Walk`, `Quat_Canh` (Quật cành), `Re_Troi` (Rễ Trồi), `Stagger`, `Phase2`, `Retreat`, `Emerge` | `Re_Hut` (Rễ hút sinh khí) | `foot_*`, `release`, `root_strike`, `sink` |

Tên trong GLB theo kiểu hôm nay: `<Loại>_<Hành động>[.<biến thể>]` (`Enemy_Hit.front`, `Hero_Attack_L`). Gồng là một đoạn của clip Attack có mốc `windup_end` và `release`, không phải clip riêng, để tua theo gõ và giữ chờ sim.

### 5.5 Máy trạng thái và chuyển tiếp

| Trạng thái | Clip | Ưu tiên | Vào (s) | Ngắt được bởi | Ghi chú |
|---|---|---|---|---|---|
| Idle | `Idle` + biến thể, `Idle.fidget` mỗi 4–9 s ngẫu nhiên | 1 | 0,25 | mọi thứ | Pha ngẫu nhiên |
| Locomotion | `Walk`↔`Run` trộn theo tốc độ, nhịp bước khớp tốc độ (giữ cách của `motion.ts`) | 1 | liên tục | mọi thứ | Xoay tại chỗ khi lệch hướng > 60° (tầng H) |
| Attack | Gồng: giữ ở `windup_end` tới sự kiện `strike` của sim (quái) hay tua theo tiến độ gõ (rồng, Lightbearer); nhả ở `release`; thu | 3 | 0,12 | Death, Stagger | Không bao giờ nhả trước sim; chuyển từ Gồng sang Nhả không trộn |
| Hit (lớp phủ) | Tầng H: clip cộng; tầng C: gập thân thủ tục trong shader theo hướng đòn (bên dưới) | 2 | 0,03 vào, 0,25 ra | — | Không cắt đòn đang ra |
| Stagger | `Stagger` toàn thân | 4 | quán tính 0,1 | Death | Chỉ khi sim báo choáng hay đẩy lùi; trạng thái của sim vẫn là màu, rung, nghiêng (Dragonhold 05 §6.2) |
| Death | `Death.a/b` chọn theo hướng và sức đòn cuối | 5 | quán tính 0,08 | — | Sự kiện `fall_impact`; nằm 0,3–0,6 s rồi tan hay chìm |
| Spawn | `Spawn` (bước ra khỏi rừng, bò khỏi vết nứt, trồi lên) | 5 | — | Death | Kèm VFX ra quân của làn VFX |
| Victory, Cheer | clip một lần | 1 | 0,2 | Hit | Đám đông: trễ ngẫu nhiên 0–150 ms mỗi con |

**Chuyển tiếp quán tính** (sửa L1, L2):
- Tầng H (`anim/inertial.ts`): lúc chuyển, lưu độ lệch quaternion từng xương giữa tư thế cũ và mới; độ lệch tắt dần bằng lò xo tắt hãm tới hạn trong 0,08–0,25 s, cộng lên tư thế mới. Không cần chạy hai clip song song.
- Tầng C (shader): con chuyển clip giữ clip cũ **đóng băng** ở thời điểm chuyển làm lớp B, trộn từ 1 về 0 theo ease-out trong 0,08–0,2 s. Không thêm texel nào.
- Texture xương đổi từ ma trận 3×4 sang quaternion + tịnh tiến (2 texel mỗi xương mỗi khung thay vì 3) và trộn nlerp (sửa L4).
- Gập thân khi trúng ở tầng C: thuộc tính mỗi con (tuổi cú trúng, hướng); shader xoay các xương trong mặt nạ thân trên (hông 0,3, ngực 0,7, đầu 1,0 của rig profile) quanh trục vuông góc hướng đòn, góc theo lò xo vượt đà. Có hướng, không cần clip Hit riêng cho mỗi hướng.

### 5.6 Lớp thủ tục

| Lớp | Làm gì | Tầng H | Tầng C | Từ đâu |
|---|---|---|---|---|
| Tua gồng theo gõ | Thời gian clip Attack = đầu gồng + phần đã gõ × (`release` − đầu gồng); xong từ thì chạy tiếp từ `release` (VFX_STANDARD §3.1, cách ưu tiên). Thay `FIRE_STRIKE` và `COIL` của làn VFX | có | — | tự làm, `anim/charge.ts` |
| Lò xo phụ | Đuôi, áo choàng, đầu cánh, cờ, tán lá, tai | `@pixiv/three-vrm-springbone` | nướng trong clip (Blender) | thư viện + `td_rig_post.py` |
| Nhìn theo | Đầu, cổ quay về mục tiêu, giới hạn ±20–40° (`td_lookAt` sẵn trong GLB Wordwoven) | có | xoay xương đầu theo góc mỗi con | tự làm, ~60 dòng |
| Giật lùi | Lò xo trên gốc và ngực khi bắn, khi trúng (gộp `Hero.hurt`, `springStep` của `ship-rules.ts`) | có | ma trận con (kit `Reactions`) | gộp mã có sẵn vào `anim/spring.ts` |
| Nén và giãn | Giữ thể tích, 0,92–1,08, ở chạm đất, ra đòn, trúng; theo phong cách nửa thật | có | có | kit `Reactions` |
| IK chân | Chân bám đất dốc, bệ, cầu | `CCDIKSolver` hay IK hai xương giải tích | không (khóa chân nướng sẵn; nghiêng cả thân theo pháp tuyến đất) | three.js |
| Nhiễu sống | Thở, lệch đầu chậm, không lặp đúng nhịp | có | pha, tốc độ, biên độ mỗi con | tự làm |
| Hit stop | Đồng hồ animation theo `hitstop.scale()` của kit | có | có | kit |

### 5.7 Đám đông

| Mục | Thiết kế |
|---|---|
| Lưu | Một texture xương mỗi model (các clip nối nhau); thuộc tính mỗi con: clip A + thời gian, clip B + thời gian, trộn, tuổi cú trúng + hướng, góc đầu |
| Lệch nhịp | Pha ngẫu nhiên; tốc độ ±8 %; biên độ ±10 % (nội suy giữa khung nghỉ và khung clip); 2–3 biến thể Idle và Death; lật trái phải cho clip đối xứng; cỡ ±5 % |
| Sự kiện | CPU biết thời gian clip mỗi con nên phát hiện vượt mốc rẻ; chỉ phát cho con trên màn hình gần camera nhất (trần theo bậc, §5.9) |
| Tiếng bước chân đám đông | Một vòng lặp "bầy hành quân" theo số con và tốc độ, cộng vài tiếng bước rời của con gần nhất; không phát mỗi bước của mỗi con |
| LOD | Dưới 12 px: không clip (thân cứng, nhún bằng shader); 12–30 px: clip, không gập thân, không nhìn theo; trên 30 px: đủ. Ngoài màn hình: CPU cập nhật 10 Hz. Lưới xa theo làn models |
| Bầy cứng (tầng R) | Giữ ma trận từng con của Last Line; thêm trong shader: thân dồn ép theo nhịp bước, phần đầu trễ nhịp so với thân (theo trục dài của lưới), vết nứt sáng theo pha; ra quân bò khỏi vết nứt (nâng dần, thân giãn rồi về), chết: vỡ theo hướng đòn trong 2–3 khung trước mảnh vỡ |
| VAT | Chỉ khi một bầy trên 400 con có chi mềm; nướng bằng script của ta, không cần OpenVAT |

### 5.8 Sự kiện clip

```ts
// shared/game-kit/anim/events.ts (phác thảo)
export type AnimEventName = "foot_l" | "foot_r" | "wing_down" | "windup_end" | "release" | "recover" | "fall_impact" | (string & {});
export interface AnimEvent { name: AnimEventName; entity: number; clip: string; at: THREE.Vector3; strength: number }
export interface AnimEventSink { emit(event: AnimEvent): void }
```

| Luật | Chi tiết |
|---|---|
| Phát hiện | Mốc nằm giữa thời gian clip khung trước và khung này (đúng khi clip lặp, đổi tốc độ, tua, nhảy cóc); sai lệch ≤ 1 khung |
| Vị trí | Lấy từ socket gần nhất (`FX_FOOT_L`, `FX_MOUTH`, `FX_WING_*`, `FX_TOOL`) |
| Ai nghe | VFX (bụi chân, lóe tung đòn pha R, bụi chạm đất), SFX (bước, vỗ cánh, vung, ngã), rung camera nhẹ cho con nặng |
| Không đổi sim | Sát thương, trúng, chết vẫn theo sự kiện sim; sự kiện clip chỉ là hình và tiếng |
| Hỏa Long | `release` của clip thay bảng đo tay `FIRE_RELEASE_S`; đạn rời ≤ 50 ms sau phím cuối |

### 5.9 Ngân sách theo bậc

Đo trên Mac mini M4, 1920 × 1080, cảnh nặng nhất của từng game (`dh-bench`, `td-1b-perf`, bench bầy). Thời gian CPU của animation đo riêng (p95).

| Mục | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Tầng H cập nhật mỗi khung | 0 (DH: khối tạm; TD: 2D) | 6 | 8 | 12 |
| Khớp lò xo phụ | 0 | 16 | 48 | 96 |
| IK chân | tắt | tắt | tầng H | tầng H |
| Tầng C có xương trên màn hình | 0 (dáng shader) | 220 | 320 | 400 |
| Gập thân, nhìn theo ở tầng C | tắt | gập thân | cả hai | cả hai |
| Biến thể mỗi họ | 1 | 2 | 3 | 3 |
| Sự kiện có tiếng mỗi khung | 2 | 4 | 6 | 8 |
| Bụi chân mỗi khung | 0 | 4 | 8 | 16 |
| CPU animation p95 | ≤ 0,2 ms | ≤ 0,5 ms | ≤ 0,8 ms | ≤ 1,2 ms |
| GPU thêm so với thân cứng | — | ≤ 0,4 ms | ≤ 0,6 ms | ≤ 0,9 ms |

Mốc hôm nay: Dragonhold 220 quái có xương, High 1080p, 5,93 ms trung bình, 7,8 ms p95, 70 draw call (`AGENTS.md` của game); Wordwoven 1C cho ≤ 8 nhân vật có xương ở High, ≤ 6 ở Medium (`BUILD_1C_MAP1.md` §6).

### 5.10 Animation Lab (`tools/anim-lab/`)

Trang Vite như `tools/typing-feedback-lab/`, chạy từ repo cha, gắn chỉ đọc `public/assets/<game>/models` của từng game.

| Phần | Làm gì |
|---|---|
| Chọn | Game → nhân vật → clip; mọi nhân vật của ba game, mọi tầng |
| Điều khiển | Nút trạng thái (đi, chạy, gồng giữ, nhả, trúng trước/sau, chết a/b, ra quân, thắng); thanh tiến độ gõ giả cho tua gồng; tốc độ 0,25 / 0,5 / 1; bước từng khung; lặp đoạn |
| Camera | Camera chơi của từng game (DH mặc định, TD 55° ở 58 m, LL sau lưng) và cận cảnh xoay quanh; nền đất của game |
| A/B | Trái cũ, phải mới, cùng thời điểm. Cũ: bản nướng hôm nay xuất `.anim.json` (texture xương), hay clip quay từ game (`dh-models.mjs`, `?bench=foes`) |
| Đám đông | 50 / 200 / 400 con cùng loại đi một làn: xem lệch nhịp, chỉ số trùng pha |
| Đo | Vận tốc góc xương lúc chuyển (đỏ khi bật), trượt chân, xuyên đất, nhật ký sự kiện kèm tiếng, thời gian CPU |
| Xuất | `scripts/capture.mjs` (tờ khung 12 khung mỗi clip ở camera chơi và cận cảnh, clip nửa tốc độ 3–5 s), `scripts/sheets.py` |
| Ảnh chụp | `tools/anim-lab/tmp/` (bỏ qua Git); xong thì `node tools/capture-prune/prune.mjs <thư mục> --apply`, giữ tờ khung và số |

### 5.11 Cách chấm

| Bước | Luật |
|---|---|
| 1. Làn nộp | Mỗi nhân vật: tờ khung 12 khung mỗi clip ở camera chơi và cận cảnh, 1280 và 1920; clip nửa tốc độ cạnh clip tham chiếu thương mại cùng cỡ (trên máy); tờ chuyển tiếp (6 khung quanh mỗi lần đổi trạng thái); tờ đám đông 200 con; số đo §5.10 |
| 2. Hai giám khảo | Agent không thuộc làn animation, độc lập nhau; chấm tám hạng mục 0–10 **trước khi đọc số đo**; mỗi người viết năm sửa cụ thể nhất nếu chưa đạt |
| 3. Đạt | Cả hai ≥ 9, không hạng mục nào < 8,5 |
| 4. Số đo kèm (không thay điểm) | Vận tốc góc lúc chuyển ≤ 1,5 lần đỉnh của clip; trượt chân ≤ 0,05 m/s khi chạm; mối nối vòng lặp ≤ 1 cm; xuyên đất ≤ 2 % chiều cao; sự kiện lệch ≤ 1 khung; phím cuối tới đạn ≤ 50 ms; < 10 % cặp hàng xóm trùng pha quá 1 s; bóng dáng gồng khác ra đòn ≥ 15 % |
| 5. Chủ dự án | Xem trong Lab và trong game; đồng ý thì mới gắn rộng |

## 6. Kế hoạch

| Pha | Việc | Tệp | Làn | Cổng |
|---|---|---|---|---|
| P0 (29–30/10) | Tài liệu này, sổ giấy phép. Thử nhanh: (a) Hỏa Long đánh dấu `additive` cho Attack, Hit, Cast với clip gốc (clip strike chờ tùy chọn clip tham chiếu của kit ở P1); (b) `three-vrm-springbone` trên đuôi và đầu cánh Hỏa Long | (a) `.wt-dh-vfx/src/view/heroes.ts` (làn VFX giữ tệp này); (b) nhánh thử | Thiết kế; VFX | Tờ khung a-04 → f000 không còn nằm rạp |
| P1 (31/10–02/11) | Kit `anim/` lõi | `shared/game-kit/anim/{index,clip-meta,events,animator,inertial,spring,springbones,look,ik,charge,profiles}.ts`, `anim/crowd/{bake,skin-glsl,motion,variation}.ts`, test; `three/hero.ts` thêm clip tham chiếu cho clip cộng và móc sự kiện (ghi `DRIFT.md`); README kit thêm dòng `anim/` | Kit | Test kit; Dragonhold build qua `node scripts/sync-game-kit.mjs --target games/dragon-hold` |
| P2 (01–03/11) | Animation Lab tối thiểu: chọn, phát, nửa tốc độ, A/B, tờ khung | `tools/anim-lab/{index.html,vite.config.mjs,src/main.ts,src/scenes.ts,src/ab.ts,scripts/capture.mjs,scripts/sheets.py}` | Thiết kế | Tờ trước và sau của L1, L2 |
| P3 (03–07/11) | **Dragonhold**: `motion.ts`, `crowd-rig.ts` dùng `anim/crowd`; `crowd.ts` dùng shader kit; `heroes.ts` dùng `Animator`, tua gồng, sự kiện; Warden không thu cỡ đột ngột; ra quân bằng thân; sự kiện tới `fx.ts`, `foe-fx.ts` | `src/view/{motion,crowd-rig,crowd,actors,heroes}.ts` | models (motion, crowd-rig); view-crowd-fx (crowd, actors, heroes) | `dh-bench` trong §5.9; giám khảo vòng 1 |
| P4 (04–10/11) | Rig Blender cho quái DH bằng họ Mesh2Motion + clip CC0; đưa `td_rig_*` lên repo cha | `scripts/models/blender/rig/*.py`; preset `games/dragon-hold/scripts/models/presets/dh-rigs/*.json` | models | Lab A/B: mới hơn cũ ở mọi hạng mục |
| P5 (03–12/11) | **Wordwoven** C5, C7, C8 dùng kit thay vì chép crowd của Dragonhold; Mộc Tinh đủ clip đòn; Thư Đồng tăng biên độ; người làng rig mới; Draconis khi có P18 | `src/view/3d/{heroes,units}.ts` (`.wt-td-1c`, theo `BUILD_1C_MAP1.md` §7); preset `td-rigs/*.json` | L2, L3 của 1C | Mã kit không tính vào trần dòng 1C (§3 trừ `src/kit`) |
| P6 (sau khi có model) | **Last Line**: Lightbearer và hai súng canh (súng: vật cứng theo lò xo trôi, nhắm, giật), áo choàng lò xo, lướt và giật thay cho tàu (giữ số của `ship-rules.ts`); bầy: ra quân và chết bằng thân trong shader | `src/view/hero.ts` mới thay vỏ của `ship.ts`; `src/view/crowd.ts` | T hay V | Sim và ván vàng không đổi |
| P7 | Vòng chấm từng game tới khi cả hai giám khảo ≥ 9 | tờ khung trong `tmp/` của Lab | Giám khảo | §5.11 |

**Vì sao Dragonhold trước:** chỉ game này có nhân vật 3D đang chơi; có đủ tầng H, C và lính ta; hai lỗi bật tư thế lộ rõ nhất; làn VFX đang cần mốc `release` và sự kiện quái; có sẵn bench, trang `?bench=foes`, kịch bản chụp. **Wordwoven thứ hai** vì làn C5 bắt đầu 03/11 và C7 06/11: kit phải có trước đó, không thì sẽ có bản chép thứ ba của đám đông Dragonhold. **Last Line sau cùng** vì Lightbearer chưa có model.

## 7. Cần gì

| Từ | Việc |
|---|---|
| Chủ dự án | Đồng ý tải từng gói (§5.2): Mesh2Motion rig và clip rồng, cáo, ngựa, nhện, kaiju (~4,3 MB, CC0); Quaternius UAL1 Standard (CC0); Quaternius UAL2 Standard (CC0) |
| Chủ dự án | Quyết: quái Dragonhold chuyển từ xương viết bằng mã sang rig Blender với clip CC0 (đề xuất: có) |
| Chủ dự án (Tripo) | Lightbearer: tư thế A, khe hở tay và thân, áo choàng tách khỏi chân (dừng trên gối hay chia vạt), mũ và giáp cứng, mức mặt cao nhất; **không chọn auto rig**. 5 súng canh: vật cứng, không rig. Draconis P18 và Mộc Tinh theo phiếu sẵn có |
| Chủ dự án | Mixamo: chỉ khi CC0 thiếu clip; đọc điều khoản hiện hành trong tài khoản Adobe rồi quyết |
| Chủ dự án | Duyệt trong Lab: tờ khung `contact.png` của 9 rig Wordwoven (chờ từ 24/10) và các vòng chấm |
| Codex (ảnh) | Tờ tư thế khóa 2D cho mỗi nhân vật H: gồng, nhả, thu, trúng, chết, ở camera chơi và cận cảnh (Hỏa Long đòn chữ và Sky Fire; Lightbearer bắn trái, phải, quỳ, đứng dậy, thắng; Mộc Tinh Quật cành, Rễ Trồi, choáng, rút); tờ bóng dáng quái theo họ (Grunt chém, Wolf vồ, Boar húc, Ant cắn) |

## 8. Rủi ro

| Rủi ro | Mức | Giảm |
|---|---|---|
| Lưới Tripo dính tay vào thân, áo choàng vào chân: rách khi cử động | Cao | Prompt tư thế A có khe; bản đồ giãn lưới của `td_rig_review.py`; chấp nhận tư thế hẹp hơn nếu cần |
| Clip người CC0 trên tỉ lệ cách điệu (đầu to, chân ngắn): trượt chân, xuyên | Trung bình | Khóa chân IK, giữ đầu trong hậu kỳ (đã có) |
| Ít clip bốn chân CC0 (cáo, ngựa): Heo từ ngựa có thể sai dáng | Trung bình | Clip khóa trong Blender cho Heo; xương viết bằng mã làm đường lùi |
| Hiệu năng Ultra: lưới gốc Tripo × đám đông có xương | Trung bình | §5.9; lưới viền và bóng mờ dùng Medium (đã có ở làn models) |
| Kit đang được làn typing-fx sửa (`shared/game-kit/feedback/typing-fx/*` đang đổi): xung đột khi đồng bộ | Thấp | `anim/` là thư mục mới; đồng bộ sau khi làn kia gộp |
| Hai làn sửa cùng tệp (`heroes.ts` của làn VFX, `crowd.ts` của làn models) | Trung bình | Thứ tự gộp ở §9; mỗi bước nói rõ tệp và làn |
| Animation làm lệch thời điểm của sim (đòn nhả trước sim) | Cao nếu sai | Gồng giữ tới sự kiện `strike` của sim; ván vàng không đổi |
| Giấy phép: tệp CMU lẫn trong Mesh2Motion; Mixamo chưa rõ bản hiện hành | Trung bình | Loại trừ rõ trong `THIRD_PARTY.md`; kiểm tại nguồn trước mỗi lần tải |
| Chủ dự án không đủ thời gian duyệt từng clip | Trung bình | Lab gom theo lô, giám khảo lọc trước, chủ dự án chỉ xem bản đã ≥ 9 |

## 9. Nối với các làn đang chạy

| Làn | Nối thế nào |
|---|---|
| VFX Dragonhold (`games/.wt-dh-vfx`, nhánh `dh-vfx`) | Giữ `heroes.ts`, `fx.ts`, `foe-fx.ts`, `skyfire.ts`. Thử P0 (a) đi qua làn này. `FIRE_RELEASE_S` và `COIL` được thay bằng mốc `release` và `anim/charge.ts` ở P3, sau khi vòng 7 gộp. Pha A và R của đòn quái (`foe-fx.ts`) giữ theo sự kiện `windup`/`strike` của sim, lấy vị trí vũ khí từ socket ở mốc `release` |
| Model theo bậc (`games/.wt-dh-models`, nhánh `dh-models`) | Giữ `models.ts`, `crowd-rig.ts`, `motion.ts`, `m0b-tiers.mjs`. Bậc phải sinh từ lưới đã rig (bước 7 của §5.3); lưới viền và bóng mờ giữ chỉ số xương (đã làm: `hull` mang `aSkinI`/`aSkinW`). Gộp `dh-models` trước P3 |
| Wordwoven 1C (`games/.wt-td-1c`) | C5, C7, C8 dùng `anim/` của kit; C11 (VFX năm pha) nghe sự kiện clip |
| VFX Wordwoven (`games/.wt-td-vfx`) | `FxPipe` nhận thêm sự kiện clip khi 3D có nhân vật |
| Hiệu ứng gõ (`shared/game-kit/feedback/typing-fx/`) | Tiến độ gõ dùng chung cho tua gồng (`anim/charge.ts` đọc cùng nguồn) |
| Âm thanh (`AUDIO_PIPELINE.md`) | Danh sách tiếng theo sự kiện clip: bước theo cỡ và mặt đất, vỗ cánh, vung, ngã, quỳ; vòng lặp bầy hành quân |
